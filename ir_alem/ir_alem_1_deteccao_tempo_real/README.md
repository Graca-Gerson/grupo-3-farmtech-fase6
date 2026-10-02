# Ir Além 1 — Detecção de tomate e pimentão em tempo real

> **FIAP — Fase 6 · Escopo opcional 1** · Reconhecimento em tempo real usando o modelo `best.pt` da Entrega 1

## 🎯 Objetivo

Levar o modelo treinado na Entrega 1 (YOLO customizado, 60 épocas, mAP50 = 0,916 na validação) para fora do notebook: capturar imagens de uma câmera **ao vivo** e reconhecer tomate e pimentão em cada quadro, mostrando na tela a caixa, a classe e a confiança de cada detecção.

## 📷 Por que webcam, e não ESP32-CAM

O enunciado propõe uma ESP32-CAM **ou** uma webcam. O grupo não tem uma ESP32-CAM física disponível, então a captura é feita pela webcam do computador. A arquitetura é a mesma nos dois casos — só muda a origem da imagem:

| Etapa | Com ESP32-CAM | Com webcam (este projeto) |
|-------|---------------|---------------------------|
| Captura | Câmera da placa, enviada por Wi-Fi como stream de vídeo | Câmera do computador (USB ou integrada) |
| Leitura dos quadros | `cv2.VideoCapture('http://<ip-da-placa>:81/stream')` | `cv2.VideoCapture(0)` |
| Inferência | `best.pt` da Entrega 1, rodando no computador | Igual |
| Saída | Caixas, classe e confiança na tela + prints | Igual |

Nos dois casos a placa ou a webcam apenas **captura**; a inferência roda no computador, porque a ESP32-CAM não tem capacidade para executar o YOLO. Por isso o script já aceita uma URL de stream no lugar do índice da webcam (`--fonte`): se uma ESP32-CAM ficar disponível, basta carregar nela o exemplo *CameraWebServer* da Arduino IDE e apontar o script para o endereço do stream. Essa variante **não foi testada**, por falta da placa.

## 🧱 Fluxo

```
câmera ──► quadro (OpenCV) ──► YOLO customizado (best.pt) ──► caixas + classe + confiança ──► janela na tela
                                                                                          └──► tecla "s" → print em prints/
```

## 📦 Requisitos

- **Python 3.12 ou 3.13** (confira com `python --version`; no Mac pode ser `python3 --version`).
- As bibliotecas usadas pelo script — `ultralytics` (YOLO, já traz o PyTorch) e `opencv-python` (câmera e janela) — estão no [`requirements.txt`](../../requirements.txt) da raiz do projeto, nas mesmas versões dos notebooks.
- Uma webcam (a integrada do notebook serve). Sem webcam, dá para usar um arquivo de vídeo ou o stream de uma ESP32-CAM — ver a seção **Sem webcam própria** mais abaixo.
- O modelo `best.pt` da Entrega 1 (passo 3 abaixo).

## ▶️ Como Executar

Os passos 1 e 2 são os mesmos da execução local descrita no [README principal](../../README.md#4-execução-local-opcional--alternativa-ao-colab); se o ambiente virtual já existe, pule para o passo 3.

### Passo 1 — Baixar o projeto e criar o ambiente virtual

No terminal (macOS: app **Terminal** ou iTerm; Windows: **PowerShell**):

```bash
git clone https://github.com/Graca-Gerson/grupo-3-farmtech-fase6.git
cd grupo-3-farmtech-fase6
python -m venv .venv
```

Ative o ambiente — o comando muda conforme o sistema:

| Sistema | Comando para ativar |
|:--------|:--------------------|
| 🍎 macOS | `source .venv/bin/activate` |
| 🪟 Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| 🪟 Windows (Prompt de Comando) | `.venv\Scripts\activate.bat` |

Com o ambiente ativo, o nome `(.venv)` aparece no início da linha do terminal. Ative-o de novo sempre que abrir um terminal novo.

> 🪟 **Windows:** se o PowerShell recusar o `Activate.ps1` com erro de "execução de scripts desabilitada", rode antes `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` (vale só para aquela janela) e ative de novo. Se o comando `python` não for encontrado, use `py -m venv .venv` no lugar de `python -m venv .venv`.

### Passo 2 — Instalar as dependências

Na raiz do projeto (`grupo-3-farmtech-fase6/`), com o ambiente ativo — o comando é o mesmo no macOS e no Windows:

```bash
pip install -r requirements.txt
```

Pode levar vários minutos (PyTorch e TensorFlow são grandes). O esperado é terminar sem nenhuma linha `ERROR`. No Windows com placa de vídeo NVIDIA, para usar a GPU, siga a ordem de instalação do [README principal](../../README.md#4-execução-local-opcional--alternativa-ao-colab) — sem isso o script funciona do mesmo jeito, só que em CPU.

### Passo 3 — Copiar o modelo `best.pt` para a pasta `modelo/`

O arquivo de pesos **não fica no repositório** (arquivos `.pt` são ignorados pelo Git). Use o modelo oficial da Entrega 1, que está no Google Drive do projeto:

```
FarmTech_Fase6/Resultados/epocas_60_gerson/treino-2/weights/best.pt
```

Baixe esse arquivo pelo navegador (botão direito → **Fazer download**) e mova-o para:

```
grupo-3-farmtech-fase6/ir_alem/ir_alem_1_deteccao_tempo_real/modelo/best.pt
```

A pasta `modelo/` não vem no repositório — crie-a. Supondo que o download foi para a pasta Downloads e que o terminal está na raiz do projeto:

**🍎 macOS (Terminal):**

```bash
mkdir -p ir_alem/ir_alem_1_deteccao_tempo_real/modelo
mv ~/Downloads/best.pt ir_alem/ir_alem_1_deteccao_tempo_real/modelo/best.pt
```

**🪟 Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Force ir_alem\ir_alem_1_deteccao_tempo_real\modelo
Move-Item "$HOME\Downloads\best.pt" ir_alem\ir_alem_1_deteccao_tempo_real\modelo\best.pt
```

> Se já havia um `best.pt` na pasta Downloads, o navegador salva o novo como `best (1).pt` — ajuste o nome no comando. O arquivo tem cerca de 6 MB.

### Passo 4 — Liberar a câmera para o terminal

O sistema só entrega as imagens da câmera a programas autorizados.

- **🍎 macOS:** **Ajustes do Sistema → Privacidade e Segurança → Câmera** → ative a chave do aplicativo de terminal que você usa (**Terminal** ou **iTerm**; se rodar pelo VS Code, o **Visual Studio Code**). Na primeira execução o macOS costuma abrir esse pedido sozinho; se a permissão for dada com o terminal aberto, feche-o e abra de novo antes de rodar.
- **🪟 Windows 11:** **Configurações → Privacidade e segurança → Câmera** → deixe ativados **Acesso à câmera** e **Permitir que aplicativos da área de trabalho acessem sua câmera**. (No Windows 10: **Configurações → Privacidade → Câmera**, mesmas duas opções.)

Feche outros programas que estejam usando a câmera (Teams, Zoom, Meet no navegador): em geral só um programa por vez consegue abri-la.

### Passo 5 — Rodar o script

Entre na pasta do Ir Além 1 e rode:

**🍎 macOS:**

```bash
cd ir_alem/ir_alem_1_deteccao_tempo_real
python deteccao_tempo_real.py
```

**🪟 Windows (PowerShell):**

```powershell
cd ir_alem\ir_alem_1_deteccao_tempo_real
python deteccao_tempo_real.py
```

O terminal mostra o modelo carregado (`classes: {0: 'tomate', 1: 'pimentao'}`) e abre uma janela com o vídeo da webcam. Cada tomate ou pimentão reconhecido aparece com uma caixa, o nome da classe e a confiança (0 a 1). No canto superior esquerdo ficam os quadros por segundo (FPS) e o resumo do que foi detectado no quadro atual.

Se a câmera não for a padrão (por exemplo, uma webcam USB num notebook que também tem a integrada), use `--fonte 1`.

### Passo 6 — Usar as teclas e salvar prints

Com a **janela do vídeo em foco** (clique nela antes de apertar as teclas — no terminal elas não têm efeito):

| Tecla | Ação |
|:-----:|------|
| `s` | Salva o quadro atual, com as detecções desenhadas |
| `q` ou `Esc` | Encerra o programa |

Os prints ficam em **`ir_alem/ir_alem_1_deteccao_tempo_real/prints/`** (a pasta é criada no primeiro print), com nome de data e hora — por exemplo, `prints/deteccao_20261002_153012_482913.jpg`. O terminal mostra o caminho e as detecções de cada print salvo.

### Se algo der errado

| Mensagem | O que fazer |
|----------|-------------|
| `modelo não encontrado em ...` | Confira o passo 3: o arquivo precisa estar em `modelo/best.pt`, com esse nome exato |
| `não foi possível abrir a fonte de vídeo "0"` | Câmera em uso por outro programa ou inexistente — feche os outros programas ou tente `--fonte 1` |
| `a câmera abriu, mas não entregou nenhuma imagem` | Falta de permissão — refaça o passo 4 e abra o terminal de novo |
| `ModuleNotFoundError: No module named 'cv2'` (ou `'ultralytics'`) | O ambiente virtual não está ativo — refaça a ativação do passo 1 |

## 🎞️ Sem webcam própria: vídeo ou ESP32-CAM

O script não depende de webcam: a opção `--fonte` aceita também um **arquivo de vídeo** ou o **stream de uma ESP32-CAM**. Assim, quem não tiver câmera pode testar com um vídeo gravado no celular (tomates e pimentões filmados de perto):

```bash
python deteccao_tempo_real.py --fonte video_tomates.mp4                 # mostra a janela com as detecções
python deteccao_tempo_real.py --fonte video_tomates.mp4 --sem-janela    # sem janela: salva todos os quadros em prints/
python deteccao_tempo_real.py --fonte http://192.168.0.50:81/stream     # ESP32-CAM na mesma rede (exemplo CameraWebServer)
```

No modo `--sem-janela`, **cada quadro** é salvo em `prints/` — para vídeos longos, limite com `--max-quadros 30`, por exemplo.

### Todas as opções

| Opção | Padrão | Para que serve |
|-------|--------|----------------|
| `--fonte` | `0` | Índice da webcam (`0`, `1`…), URL de stream (ESP32-CAM) ou arquivo de vídeo |
| `--modelo` | `modelo/best.pt` | Caminho do modelo |
| `--conf` | `0.5` | Confiança mínima para mostrar uma detecção — o mesmo limiar usado no teste da Entrega 1 |
| `--imgsz` | `640` | Tamanho de entrada da rede (o mesmo do treino) |
| `--device` | automático | `cpu`, `0` (GPU NVIDIA) ou `mps` (GPU do Mac com Apple Silicon) |
| `--pasta-prints` | `prints/` | Onde salvar os prints |
| `--sem-janela` | — | Não abre janela: processa os quadros e salva todos |
| `--max-quadros` | `0` (sem limite) | Encerra depois de N quadros |

## ✅ O que já foi verificado

- Mensagens de erro claras quando o modelo não é encontrado, quando a câmera não abre e quando ela abre sem entregar imagens.
- Execução completa com o `best.pt` oficial, usando como fonte um vídeo montado com as 8 imagens de teste da Entrega 1 (sem janela, em CPU): 8 quadros processados, caixas, classe e confiança desenhadas e salvas, cerca de 9 FPS em CPU num Mac.
- **Ainda não testado ao vivo com a webcam** — o teste com câmera real e a gravação do vídeo são os próximos passos.

## ⚠️ Limitações esperadas

- **O modelo aprendeu com apenas 64 fotos de treino**, tiradas de perto, com o fruto ocupando boa parte da imagem. Com a câmera ao vivo, distância, enquadramento, fundo e iluminação diferentes podem trocar a classe. Isso já apareceu no teste com o vídeo montado: a foto `tomate_37` foi reduzida para caber no quadro (o fruto ficou menor, com faixas escuras em volta) e passou a ser detectada como "pimentão" (0,80), embora a mesma foto, no tamanho original, dê "tomate" (0,97) no teste da Entrega 1. Nesse vídeo, 6 de 8 quadros foram classificados corretamente.
- **Pimentões alaranjados** tendem a ser confundidos com tomate — o mesmo erro do teste da Entrega 1 (`pimentao_23`).
- Para resultados mais estáveis ao vivo: aproximar o fruto da câmera, usar fundo liso e boa iluminação, e manter o limiar de confiança em 0,5 ou mais.
- O FPS depende do computador: em CPU, a inferência a cada quadro limita a fluidez; com GPU (`--device 0` ou `--device mps`) fica mais fluido.

## 📁 Arquivos

```
ir_alem/ir_alem_1_deteccao_tempo_real/
├── README.md                  ← este arquivo
├── deteccao_tempo_real.py     ← captura + inferência + prints
├── modelo/best.pt             ← (não versionado) copiar do Google Drive
└── prints/                    ← criada ao salvar o primeiro print (tecla "s")
```
