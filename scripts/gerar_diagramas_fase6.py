"""
Gera os diagramas da documentação da Fase 6:

  docs/estrutura_drive_fase6.png  — estrutura de pastas do Google Drive
  docs/raci_fase6.png             — participantes e responsabilidades

Uso (a partir da raiz do repositório):

    python scripts/gerar_diagramas_fase6.py            # grava em docs/
    python scripts/gerar_diagramas_fase6.py --saida /tmp/teste

Se a estrutura do Drive ou a divisão de responsabilidades mudar, edite só os
dados em ESTRUTURA_DRIVE e EQUIPE abaixo e rode o script de novo.
Depende apenas do matplotlib (já listado no requirements.txt).
"""

import argparse
import os

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

# ---------------------------------------------------------------------------
# Dados dos diagramas (editar aqui quando algo mudar)
# ---------------------------------------------------------------------------

# Cada pasta/arquivo da raiz vira um cartão. "arvore" é uma lista de linhas
# (texto, comentário); o comentário aparece em cinza, alinhado à direita da árvore.
# Uma linha com texto vazio vira uma nota em cinza no recuo da árvore.
# Nas descrições, '\n' força uma quebra de linha.
ESTRUTURA_DRIVE = {
    'titulo': 'ESTRUTURA DO GOOGLE DRIVE',
    'centro': ('FarmTech_Fase6', 'Google Drive', 'PASTA RAIZ'),
    'esquerda': [
        {
            'nome': 'Dataset_bruto/',
            'descricao': 'Fotos originais, antes da divisão',
            'arvore': [
                ('├── Tomate/', '40 fotos'),
                ('└── Pimentao/', '40 fotos'),
            ],
        },
        {
            'nome': 'Dataset_dividido/',
            'descricao': 'Divisão 32/4/4 por classe + formato do YOLO',
            'arvore': [
                ('├── Tomate/', ''),
                ('│   ├── Treino/', '32 fotos'),
                ('│   ├── Validacao/', '4 fotos'),
                ('│   └── Teste/', '4 fotos'),
                ('├── Pimentao/', ''),
                ('│   ├── Treino/', '32 fotos'),
                ('│   ├── Validacao/', '4 fotos'),
                ('│   └── Teste/', '4 fotos'),
                ('', '(pastas abaixo geradas pelo script — formato do YOLO)'),
                ('├── treino/{images,labels}', '64 + 64'),
                ('├── validacao/{images,labels}', '8 + 8'),
                ('└── teste/{images,labels}', '8 + 8'),
            ],
        },
    ],
    'direita': [
        {
            'nome': 'Rotulacoes/',
            'descricao': 'Rótulos exportados do Make Sense IA (formato YOLO)',
            'arvore': [
                ('├── Tomate 01.txt … Tomate 40.txt', ''),
                ('└── Pimentao 01.txt … Pimentao 40.txt', ''),
            ],
        },
        {
            'nome': 'Resultados/',
            'descricao': 'Saídas separadas por quem executou (EXECUTOR)',
            'arvore': [
                ('├── epocas_30_<executor>/', 'treino com 30 épocas'),
                ('│   └── treino/weights/best.pt', ''),
                ('├── epocas_60_<executor>/', 'treino com 60 épocas'),
                ('│   └── treino/weights/best.pt', ''),
                ('├── predict_<executor>/teste/', 'imagens de teste anotadas'),
                ('└── entrega2_<executor>/', 'saídas da Entrega 2'),
            ],
        },
        {
            'nome': 'data.yaml',
            'descricao': 'Arquivo na raiz — configuração do dataset para o YOLO (criado pelo notebook)',
            'arvore': [],
        },
    ],
}

EQUIPE = {
    'titulo': 'PARTICIPANTES E RESPONSABILIDADES',
    'centro': ('EQUIPE', 'FASE 6', 'RESPONSABILIDADES'),
    'membros': [
        ('Gerson', 'Liderança, notebooks das Entregas 1 e 2,\ncheckpoint e QA final'),
        ('Carlos', 'Coleta e organização do dataset'),
        ('Ryann', 'Rotulação, vídeo e README da Entrega 1'),
        ('Lucas', 'Participação pontual no escopo opcional'),
    ],
}

# ---------------------------------------------------------------------------
# Estilo (mesma paleta e proporções dos diagramas originais)
# ---------------------------------------------------------------------------

AZUL_ESCURO = '#112a42'
FUNDO = '#f5f7fa'
BORDA_CARTAO = '#e1e5ea'
TEXTO = '#141e28'
TEXTO_SUAVE = '#747e87'
TEXTO_CENTRO_SUAVE = '#c8d0d8'
CORES = ['#17bebb', '#f5a623', '#1e968c', AZUL_ESCURO]

LARGURA = 1500
ALTURA_CABECALHO = 100
RAIO_CENTRO = 130
FONTE_MONO = 'DejaVu Sans Mono'


def px(valor):
    """Converte pixels em pontos tipográficos (a figura é salva com dpi=100)."""
    return valor * 72 / 100


def nova_figura(altura, titulo):
    fig = plt.figure(figsize=(LARGURA / 100, altura / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, LARGURA)
    ax.set_ylim(altura, 0)   # y cresce para baixo, como em coordenadas de imagem
    ax.axis('off')
    fig.patch.set_facecolor(FUNDO)
    ax.add_patch(Rectangle((0, 0), LARGURA, ALTURA_CABECALHO, color=AZUL_ESCURO, zorder=1))
    ax.text(45, ALTURA_CABECALHO / 2, titulo, color='white', fontsize=px(31), fontweight='bold',
            va='center', ha='left', zorder=2)
    return fig, ax


def quebrar_linhas(fig, ax, texto, largura_max, **estilo):
    """Quebra o texto em linhas que caibam em largura_max pixels ('\n' força a quebra)."""
    renderer = fig.canvas.get_renderer()
    linhas = []
    for paragrafo in texto.split('\n'):
        atual = ''
        for palavra in paragrafo.split():
            tentativa = f'{atual} {palavra}'.strip()
            medida = ax.text(0, 0, tentativa, **estilo)
            largura = medida.get_window_extent(renderer).width
            medida.remove()
            if largura > largura_max and atual:
                linhas.append(atual)
                atual = palavra
            else:
                atual = tentativa
        if atual:
            linhas.append(atual)
    return linhas


def desenhar_cartao(fig, ax, x, y, largura, altura, cor, numero, titulo, descricao, arvore=()):
    ax.add_patch(FancyBboxPatch((x, y), largura, altura, boxstyle='round,pad=0,rounding_size=10',
                                facecolor='white', edgecolor=BORDA_CARTAO, linewidth=1, zorder=3))
    ax.add_patch(Rectangle((x, y), 6, altura, color=cor, zorder=4))
    ax.add_patch(Circle((x + 45, y + 45), 22, color=cor, zorder=4))
    ax.text(x + 45, y + 45, f'{numero:02d}', color='white', fontsize=px(25), fontweight='bold',
            ha='center', va='center', zorder=5)
    ax.text(x + 90, y + 40, titulo, color=TEXTO, fontsize=px(20), fontweight='bold',
            ha='left', va='center', zorder=5)

    estilo_desc = dict(fontsize=px(14.5), color=TEXTO_SUAVE)
    linhas_desc = quebrar_linhas(fig, ax, descricao, largura - 90 - 20, **estilo_desc)
    for i, linha in enumerate(linhas_desc):
        ax.text(x + 90, y + 68 + i * 20, linha, ha='left', va='center', zorder=5, **estilo_desc)

    topo_arvore = y + 68 + len(linhas_desc) * 20 + 12
    col_comentario = x + 90 + max((len(t) for t, _ in arvore), default=0) * 8.6 + 14
    for i, (texto, comentario) in enumerate(arvore):
        yy = topo_arvore + i * 22
        if not texto:   # nota no recuo da árvore
            ax.text(x + 90, yy, comentario, fontsize=px(13.5), color=TEXTO_SUAVE, style='italic',
                    ha='left', va='center', zorder=5)
            continue
        ax.text(x + 90, yy, texto, family=FONTE_MONO, fontsize=px(14), color=TEXTO,
                ha='left', va='center', zorder=5)
        if comentario:
            ax.text(col_comentario, yy, comentario, fontsize=px(13.5), color=TEXTO_SUAVE,
                    ha='left', va='center', zorder=5)


def altura_cartao(fig, ax, largura, descricao, arvore, minimo=150):
    estilo_desc = dict(fontsize=px(14.5), color=TEXTO_SUAVE)
    n_desc = len(quebrar_linhas(fig, ax, descricao, largura - 90 - 20, **estilo_desc))
    altura = 68 + n_desc * 20 + (12 + len(arvore) * 22 if arvore else 0) + 22
    return max(minimo, altura)


def desenhar_centro(ax, cx, cy, linha1, linha2, linha3):
    ax.add_patch(Circle((cx, cy), RAIO_CENTRO, color=AZUL_ESCURO, zorder=3))
    ax.text(cx, cy - 20, linha1, color='white', fontsize=px(23), fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(cx, cy + 15, linha2, color=CORES[0], fontsize=px(24), fontweight='bold', ha='center', va='center', zorder=4)
    ax.text(cx, cy + 45, linha3, color=TEXTO_CENTRO_SUAVE, fontsize=px(14), ha='center', va='center', zorder=4)


def ligar(ax, x, y, cx, cy, cor):
    # A linha vai do cartão até o centro; o círculo (zorder maior) cobre o trecho interno.
    ax.plot([x, cx], [y, cy], color=cor, linewidth=1.6, zorder=2)


def gerar_estrutura_drive(caminho):
    dados = ESTRUTURA_DRIVE
    larg_cartao, margem, espaco = 600, 30, 30
    x_esq, x_dir = margem, LARGURA - margem - larg_cartao
    cx = LARGURA / 2

    # Mede os cartões numa figura provisória para descobrir a altura total
    fig, ax = nova_figura(1000, '')
    alturas = {lado: [altura_cartao(fig, ax, larg_cartao, c['descricao'], c['arvore'], minimo=110)
                      for c in dados[lado]] for lado in ('esquerda', 'direita')}
    plt.close(fig)
    total = max(sum(h) + espaco * (len(h) - 1) for h in alturas.values())
    altura_fig = ALTURA_CABECALHO + 30 + total + 40

    fig, ax = nova_figura(altura_fig, dados['titulo'])
    cy = ALTURA_CABECALHO + 30 + total / 2
    numero = 1
    for lado, x in (('esquerda', x_esq), ('direita', x_dir)):
        y = ALTURA_CABECALHO + 30
        for cartao, h in zip(dados[lado], alturas[lado]):
            cor = CORES[(numero - 1) % len(CORES)]
            desenhar_cartao(fig, ax, x, y, larg_cartao, h, cor, numero,
                            cartao['nome'], cartao['descricao'], cartao['arvore'])
            borda = x + larg_cartao if lado == 'esquerda' else x
            ligar(ax, borda, y + h / 2, cx, cy, cor)
            y += h + espaco
            numero += 1
    desenhar_centro(ax, cx, cy, *dados['centro'])
    fig.savefig(caminho, dpi=100, facecolor=FUNDO)
    plt.close(fig)


def gerar_raci(caminho):
    dados = EQUIPE
    altura_fig, larg_cartao, h_cartao = 950, 560, 150
    x, cx, cy = 60, 750, 475
    fig, ax = nova_figura(altura_fig, dados['titulo'])
    for i, (nome, frente) in enumerate(dados['membros']):
        y = 130 + i * 200
        cor = CORES[i % len(CORES)]
        desenhar_cartao(fig, ax, x, y, larg_cartao, h_cartao, cor, i + 1, nome, frente)
        ligar(ax, x + larg_cartao, y + 75, cx, cy, cor)
    desenhar_centro(ax, cx, cy, *dados['centro'])
    fig.savefig(caminho, dpi=100, facecolor=FUNDO)
    plt.close(fig)


def main():
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parser = argparse.ArgumentParser(description='Gera os diagramas da Fase 6 (estrutura do Drive e RACI).')
    parser.add_argument('--saida', default=os.path.join(raiz, 'docs'), help='pasta de destino (padrão: docs/)')
    args = parser.parse_args()
    os.makedirs(args.saida, exist_ok=True)

    plt.rcParams['font.family'] = 'DejaVu Sans'
    for nome, funcao in (('estrutura_drive_fase6.png', gerar_estrutura_drive), ('raci_fase6.png', gerar_raci)):
        caminho = os.path.join(args.saida, nome)
        funcao(caminho)
        print('gerado:', caminho)


if __name__ == '__main__':
    main()
