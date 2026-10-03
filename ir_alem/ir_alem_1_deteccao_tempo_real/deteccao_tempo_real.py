"""
Ir Além 1 — Detecção de tomate e pimentão em tempo real com o modelo da Entrega 1.

Lê quadros de uma câmera (webcam do computador, stream de uma ESP32-CAM ou arquivo de
vídeo), roda o YOLO customizado (best.pt da Entrega 1) em cada quadro e mostra na tela
as caixas, a classe e a confiança de cada detecção.

Teclas (com a janela de vídeo em foco):
    s       salva o quadro atual, já com as detecções desenhadas, na pasta de prints
    q / Esc encerra

Câmera: sem --fonte, o script procura as câmeras do computador. Com uma só, usa essa câmera direto;
com duas ou mais (ex.: webcam integrada + webcam USB, ou iPhone/iPad oferecidos pelo macOS), mostra um
menu no terminal para escolher antes de abrir a janela.

Exemplos (a partir desta pasta):
    python deteccao_tempo_real.py                                  # procura as câmeras (menu se houver mais de uma)
    python deteccao_tempo_real.py --fonte 1                        # usa direto a câmera de índice 1, sem menu
    python deteccao_tempo_real.py --fonte http://192.168.0.50:81/stream   # ESP32-CAM
    python deteccao_tempo_real.py --modelo /caminho/para/best.pt --conf 0.6
"""

import argparse
import contextlib
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime

# Silencia os avisos internos do OpenCV ao testar índices de câmera que não existem
# (ex.: "out device of bound"); precisa ser definido antes de importar o cv2.
os.environ.setdefault('OPENCV_LOG_LEVEL', 'ERROR')
import cv2
from ultralytics import YOLO

PASTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
MODELO_PADRAO = os.path.join(PASTA_SCRIPT, 'modelo', 'best.pt')
PRINTS_PADRAO = os.path.join(PASTA_SCRIPT, 'prints')
NOME_JANELA = 'FarmTech - deteccao em tempo real (s = salvar print, q = sair)'


def ler_argumentos():
    parser = argparse.ArgumentParser(description='Detecção de tomate/pimentão em tempo real com o best.pt da Entrega 1.')
    parser.add_argument('--fonte', default=None,
                        help='índice da webcam (0, 1, ...), URL de stream (ex.: ESP32-CAM) ou arquivo de vídeo. '
                             'Padrão: procura as câmeras do computador e, se houver mais de uma, pergunta qual usar')
    parser.add_argument('--modelo', default=MODELO_PADRAO, help=f'caminho do best.pt. Padrão: {MODELO_PADRAO}')
    parser.add_argument('--conf', type=float, default=0.5,
                        help='confiança mínima para mostrar uma detecção (0 a 1). Padrão: 0.5, o mesmo do teste da Entrega 1')
    parser.add_argument('--imgsz', type=int, default=640, help='tamanho de entrada da rede (mesmo do treino). Padrão: 640')
    parser.add_argument('--device', default=None,
                        help="dispositivo de inferência: 'cpu', '0' (GPU NVIDIA) ou 'mps' (Mac). Padrão: escolha automática")
    parser.add_argument('--pasta-prints', default=PRINTS_PADRAO, help=f'onde salvar os prints. Padrão: {PRINTS_PADRAO}')
    parser.add_argument('--sem-janela', action='store_true',
                        help='não abre janela: processa os quadros e salva cada um com as detecções (útil para testes)')
    parser.add_argument('--max-quadros', type=int, default=0,
                        help='encerra depois de N quadros (0 = sem limite). Padrão: 0')
    return parser.parse_args()


@contextlib.contextmanager
def sem_avisos_do_sistema():
    """Esconde, só durante o bloco, as mensagens que o OpenCV escreve direto no terminal ao testar índices de câmera
    inexistentes (no macOS: "out device of bound", "camera failed to properly initialize!")."""
    try:
        sys.stderr.flush()
        original = os.dup(2)
        nulo = os.open(os.devnull, os.O_WRONLY)
    except OSError:
        yield
        return
    os.dup2(nulo, 2)
    try:
        yield
    finally:
        os.dup2(original, 2)
        os.close(nulo)
        os.close(original)


def listar_cameras(maior_indice=4, falhas_seguidas_max=2, tentativas_leitura=5):
    """Testa os índices 0..maior_indice e devolve (câmeras que entregam imagem, índices que abrem sem entregar imagem).

    Cada câmera encontrada vem como (índice, largura, altura) — a resolução do quadro lido ajuda a reconhecer qual é qual.

    A busca para depois de `falhas_seguidas_max` índices seguidos sem câmera. Cada câmera é aberta, lida e
    fechada em seguida; algumas só entregam imagem depois de alguns quadros, por isso há mais de uma tentativa.
    """
    encontradas, sem_imagem = [], []
    falhas = 0
    for indice in range(maior_indice + 1):
        with sem_avisos_do_sistema():
            captura = cv2.VideoCapture(indice)
            abriu = captura.isOpened()
            leu = None
            if abriu:
                for _ in range(tentativas_leitura):
                    ok, quadro = captura.read()
                    if ok and quadro is not None:
                        leu = (quadro.shape[1], quadro.shape[0])
                        break
            captura.release()
        if leu:
            encontradas.append((indice, *leu))
            falhas = 0
        else:
            if abriu:
                sem_imagem.append(indice)
            falhas += 1
            if falhas >= falhas_seguidas_max:
                break
    return encontradas, sem_imagem


def nomes_cameras_sistema():
    """Nomes das câmeras informados pelo sistema, quando possível; lista vazia caso contrário.

    O OpenCV não informa o nome do dispositivo. No macOS, o system_profiler lista as câmeras (inclusive iPhone/iPad
    oferecidos pela Câmera de Continuidade). Qualquer falha aqui só faz o menu usar nomes genéricos.
    """
    if platform.system() != 'Darwin':
        return []
    try:
        saida = subprocess.run(['system_profiler', 'SPCameraDataType', '-json'],
                               capture_output=True, text=True, timeout=10).stdout
        return [c.get('_name', '') for c in json.loads(saida).get('SPCameraDataType', [])]
    except Exception:
        return []


def escolher_camera(encontradas, nomes_sistema):
    """Uma câmera: devolve o índice direto. Duas ou mais: mostra um menu e pede o número até receber uma opção válida.

    O menu identifica cada câmera pelo número e pela resolução. Os nomes do sistema aparecem à parte, sem associar a
    um número: o OpenCV não informa nomes e a ordem do sistema pode ser diferente da dele (num Mac com iPhone por
    Câmera de Continuidade, o system_profiler listou a FaceTime HD primeiro, mas para o OpenCV ela era a câmera 1).
    """
    indices = [indice for indice, _, _ in encontradas]
    if len(encontradas) == 1:
        return indices[0]

    print(f'\nForam encontradas {len(encontradas)} câmeras neste computador:')
    for indice, largura, altura in encontradas:
        print(f'  [{indice}] Dispositivo {indice} — imagem de {largura}x{altura}')
    if nomes_sistema:
        print(f'  Câmeras que o sistema informa: {", ".join(nomes_sistema)}.')
        print('  (a ordem desses nomes pode não ser a mesma dos números acima)')
    print('  Se a imagem que abrir não for da câmera desejada, aperte q na janela e rode de novo escolhendo outro número.')

    if not sys.stdin.isatty():
        print(f'Sem teclado para escolher — usando a câmera {indices[0]}.')
        return indices[0]

    opcoes = ', '.join(str(i) for i in indices)
    while True:
        try:
            resposta = input(f'Digite o número da câmera que deseja usar ({opcoes}) e aperte Enter: ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit('Escolha de câmera cancelada.')
        if resposta.isdigit() and int(resposta) in indices:
            return int(resposta)
        print(f'"{resposta}" não é uma opção válida. Digite apenas um destes números: {opcoes}.')


def abrir_fonte(fonte):
    """Abre a webcam (índice numérico) ou a URL/arquivo informado."""
    origem = int(fonte) if fonte.isdigit() else fonte
    captura = cv2.VideoCapture(origem)
    if not captura.isOpened():
        dica = ('Confira se a câmera não está em uso por outro programa e, no macOS, se o Terminal tem '
                'permissão em Ajustes do Sistema > Privacidade e Segurança > Câmera.'
                if isinstance(origem, int) else 'Confira o endereço/arquivo e se o dispositivo está na mesma rede.')
        sys.exit(f'ERRO: não foi possível abrir a fonte de vídeo "{fonte}". {dica}')
    return captura


def resumir_deteccoes(resultado):
    """Texto curto com as detecções do quadro, ex.: 'tomate 0.93, pimentao 0.71'."""
    nomes = resultado.names
    itens = [f'{nomes[int(caixa.cls)]} {float(caixa.conf):.2f}' for caixa in resultado.boxes]
    return ', '.join(itens) if itens else 'nenhuma detecção'


def escrever_status(quadro, texto):
    """Escreve uma linha de status no canto superior esquerdo, com fundo escuro para legibilidade."""
    (largura, altura), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
    cv2.rectangle(quadro, (0, 0), (largura + 16, altura + 16), (0, 0, 0), -1)
    cv2.putText(quadro, texto, (8, altura + 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)


def salvar_print(quadro, pasta, resumo):
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f'deteccao_{datetime.now():%Y%m%d_%H%M%S_%f}.jpg')
    cv2.imwrite(caminho, quadro)
    print(f'print salvo: {caminho} ({resumo})')
    return caminho


def main():
    args = ler_argumentos()

    if not os.path.isfile(args.modelo):
        sys.exit(f'ERRO: modelo não encontrado em "{args.modelo}". Copie o best.pt oficial da Entrega 1 para esse '
                 'caminho ou informe outro com --modelo (ver README desta pasta).')
    modelo = YOLO(args.modelo)
    print(f'modelo: {args.modelo} | classes: {modelo.names}')

    if args.fonte is None:
        print('procurando câmeras...')
        encontradas, sem_imagem = listar_cameras()
        if not encontradas:
            if sem_imagem:
                sys.exit('ERRO: a câmera abriu, mas não entregou nenhuma imagem. No macOS, libere a câmera para o '
                         'Terminal (ou para o editor que está rodando o script) em Ajustes do Sistema > '
                         'Privacidade e Segurança > Câmera e rode de novo. No Windows, confira em Configurações > '
                         'Privacidade e segurança > Câmera.')
            sys.exit('ERRO: nenhuma câmera encontrada. Confira se a câmera está conectada e se não está em uso por '
                     'outro programa (FaceTime, Zoom, Teams, Meet).')
        args.fonte = str(escolher_camera(encontradas, nomes_cameras_sistema() if len(encontradas) > 1 else []))

    captura = abrir_fonte(args.fonte)
    print(f'fonte de vídeo: {args.fonte} | confiança mínima: {args.conf}')
    if not args.sem_janela:
        print('teclas: s = salvar print | q ou Esc = sair')

    quadros = 0
    fps = 0.0
    try:
        while True:
            ok, quadro = captura.read()
            if not ok:
                if quadros == 0 and args.fonte.isdigit():
                    print('ERRO: a câmera abriu, mas não entregou nenhuma imagem. No macOS, libere a câmera para o '
                          'Terminal (ou para o editor que está rodando o script) em Ajustes do Sistema > '
                          'Privacidade e Segurança > Câmera e rode de novo.')
                else:
                    print('fim do vídeo ou falha na leitura da câmera — encerrando.')
                break

            inicio = time.perf_counter()
            resultado = modelo.predict(quadro, conf=args.conf, imgsz=args.imgsz, device=args.device, verbose=False)[0]
            duracao = time.perf_counter() - inicio
            fps = 1 / duracao if fps == 0 else 0.9 * fps + 0.1 / duracao   # média móvel, para o número não "piscar"

            anotado = resultado.plot()   # caixas, classe e confiança desenhadas pelo Ultralytics
            resumo = resumir_deteccoes(resultado)
            escrever_status(anotado, f'{fps:.1f} FPS | {resumo}')
            quadros += 1

            if args.sem_janela:
                salvar_print(anotado, args.pasta_prints, resumo)
            else:
                cv2.imshow(NOME_JANELA, anotado)
                tecla = cv2.waitKey(1) & 0xFF
                if tecla == ord('s'):
                    salvar_print(anotado, args.pasta_prints, resumo)
                elif tecla in (ord('q'), 27):   # 27 = Esc
                    break

            if args.max_quadros and quadros >= args.max_quadros:
                break
    except KeyboardInterrupt:
        print('interrompido pelo teclado.')
    finally:
        captura.release()
        if not args.sem_janela:
            cv2.destroyAllWindows()
    print(f'quadros processados: {quadros}')


if __name__ == '__main__':
    main()
