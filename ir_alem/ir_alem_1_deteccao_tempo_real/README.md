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

- Python 3.12 ou 3.13
- `ultralytics` (traz o PyTorch) e `opencv-python` — ambos já estão no [`requirements.txt`](../../requirements.txt) da raiz. Para instalar só o necessário:

```bash
pip install ultralytics==8.4.170 opencv-python==5.0.0.93
```

- Uma webcam (a do notebook serve) — ou, alternativamente, um arquivo de vídeo ou o stream de uma ESP32-CAM.

### O modelo (`best.pt`)

O arquivo de pesos **não fica no repositório** (arquivos `.pt` são ignorados pelo Git). Use o modelo oficial da Entrega 1, que está no Google Drive do projeto:

```
FarmTech_Fase6/Resultados/epocas_60_gerson/treino-2/weights/best.pt
```

Baixe esse arquivo e coloque-o em `modelo/best.pt`, dentro desta pasta (é o caminho que o script procura por padrão), ou informe outro caminho com `--modelo`.

## ▶️ Como rodar

A partir desta pasta (`ir_alem/ir_alem_1_deteccao_tempo_real/`):

```bash
python deteccao_tempo_real.py
```

Abre a webcam padrão e uma janela com o vídeo e as detecções. No canto superior esquerdo aparecem os quadros por segundo (FPS) e o que foi detectado no quadro atual.

| Tecla | Ação |
|:-----:|------|
| `s` | Salva o quadro atual, com as detecções desenhadas, em `prints/` (nome com data e hora) |
| `q` ou `Esc` | Encerra |

### Opções

| Opção | Padrão | Para que serve |
|-------|--------|----------------|
| `--fonte` | `0` | Índice da webcam (`0`, `1`…), URL de stream (ESP32-CAM) ou arquivo de vídeo |
| `--modelo` | `modelo/best.pt` | Caminho do modelo |
| `--conf` | `0.5` | Confiança mínima para mostrar uma detecção — o mesmo limiar usado no teste da Entrega 1 |
| `--imgsz` | `640` | Tamanho de entrada da rede (o mesmo do treino) |
| `--device` | automático | `cpu`, `0` (GPU NVIDIA) ou `mps` (GPU do Mac com Apple Silicon) |
| `--pasta-prints` | `prints/` | Onde salvar os prints |
| `--sem-janela` | — | Não abre janela: processa os quadros e salva todos (útil para testar sem tela) |
| `--max-quadros` | `0` (sem limite) | Encerra depois de N quadros |

Exemplos:

```bash
python deteccao_tempo_real.py --fonte 1                               # segunda webcam
python deteccao_tempo_real.py --conf 0.6                              # mostra só detecções mais confiantes
python deteccao_tempo_real.py --fonte http://192.168.0.50:81/stream   # ESP32-CAM na rede local
python deteccao_tempo_real.py --fonte video.mp4 --sem-janela          # arquivo de vídeo, salvando cada quadro
```

> **macOS:** na primeira execução o sistema pede permissão para usar a câmera. Se a janela não abrir ou o script avisar que a câmera "não entregou nenhuma imagem", libere a câmera para o Terminal (ou para o editor que está rodando o script) em **Ajustes do Sistema → Privacidade e Segurança → Câmera** e rode de novo.

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
