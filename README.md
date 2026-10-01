# 👁️ FarmTech Vision
## Sistema de Visão Computacional para Detecção e Classificação de Objetos (YOLO + CNN)

> **FIAP Challenge — Fase 6:** FIAP — IA - Inteligência Artificial, Fase 6, 2026
> **Período:** 15/09/2026 – 13/10/2026

---

## 👥 Grupo

| Nome | RM | GitHub |
|------|-----|--------|
| Gerson Ferreira da Graça | RM 569624 | [@Graca-Gerson](https://github.com/Graca-Gerson) |
| Lucas Braga | RM 568712 | [@lucaspbmotta](https://github.com/lucaspbmotta) |
| Carlos Leonardo Mazieri | RM 572809 | [@maishumanosmpb-hub](https://github.com/maishumanosmpb-hub) |
| Ryann Pinto | RM 571003 | [@RyannCarlos](https://github.com/RyannCarlos) |

**Turma:** A | **Tutor:** Nicolly de Souza (`nicollycrs`)
**Instituição:** FIAP — IA - Inteligência Artificial, Fase 6, 2026

---

## 🎯 Objetivos

| # | Objetivo | Status |
|---|----------|--------|
| 1 | Montar dataset customizado (80 imagens: 40 tomate + 40 pimentão) | ✅ |
| 2 | Rotular imagens de treino | ✅ |
| 3 | Treinar YOLO customizado com 2 configurações de épocas (30 e 60) | ✅ |
| 4 | Comparar YOLO customizado × YOLO tradicional × CNN treinada do zero | 🔲 |
| 5 | Documentar achados, conclusões e limitações (notebook + README) | 🔄 Entrega 1 documentada no notebook |
| 6 | Gravar vídeo demonstrativo (até 5min, YouTube não listado) | 🔲 |
| 7 | *(Escopo opcional)* Sistema de coleta em tempo real via ESP32-CAM/webcam | 🔲 |
| 8 | *(Escopo opcional)* Transfer Learning + segmentação de imagem | 🔲 |

---

## ✅ Status do Projeto

> 🔄 **Entrega 1 concluída no notebook** — dataset coletado e rotulado, YOLO customizado treinado em 2 simulações (30 e 60 épocas), comparação, teste e conclusões documentados. Próximas etapas: vídeo da Entrega 1 e Entrega 2.

| Etapa | Status | Observação |
|:------|:------:|:-----------|
| Repositório GitHub criado | ✅ | Público, `grupo-3-farmtech-fase6` |
| Planejamento e cronograma | ✅ | 10 tarefas (F6-01 a F6-10), 14 riscos mapeados |
| Protocolo de captura de imagens definido | ✅ | Ver [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) |
| Estrutura do Google Drive organizada | ✅ | Ver [`docs/estrutura_drive.md`](./docs/estrutura_drive.md) |
| Coleta das 80 imagens | ✅ | 40 tomate + 40 pimentão, divididas em 32/4/4 (treino/validação/teste) por classe |
| Rotulação | ✅ | 80 rótulos em formato YOLO |
| Treino YOLO (Entrega 1) | ✅ | 2 simulações: 30 e 60 épocas — melhor resultado com 60 épocas (mAP50 = 0,916 na validação); comparação nas seções 4 a 6 do [notebook](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb) |
| Teste em imagens nunca vistas | ✅ | 7 de 8 imagens corretas — seção 7 do notebook e prints em [`prints_teste/`](./prints_teste/) |
| Conclusões da Entrega 1 | ✅ | Pontos fortes, limitações e aprendizados na seção 8 do notebook |
| Vídeo da Entrega 1 | 🔲 | Próxima etapa |
| Comparação de abordagens (Entrega 2) | 🔲 | Próxima etapa |
| README final + vídeo | 🔲 | Última etapa antes da entrega |

---

## 🗂️ Estrutura do Projeto

```
grupo-3-farmtech-fase6/
├── GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb   ← Notebook principal (Entrega 1)
├── docs/
│   ├── protocolo_captura_fotos.md    ← Regras de captura das imagens do dataset
│   ├── estrutura_drive.md            ← Organização de pastas no Google Drive
│   ├── macroprocesso.md              ← Fluxo de gestão do projeto (planejamento → entrega)
│   ├── macroprocesso_fase6.png
│   ├── cronograma.md                 ← Cronograma detalhado + jornada visual
│   ├── cronograma_fase6.png
│   ├── raci.md                       ← Responsabilidades da equipe
│   ├── raci_fase6.png
│   ├── matriz_riscos.md              ← Riscos identificados (Impacto × Probabilidade)
│   ├── gut_matrix.md                 ← Priorização dos riscos (GUT)
│   ├── gut_fase6.png
│   ├── ishikawa.md                   ← Causas raiz (diagrama de Ishikawa)
│   └── ishikawa_fase6.png
├── prints_teste/                     ← Prints do teste do modelo (imagens nunca vistas)
│   ├── tomate_23_acerto.jpg          ← Tomate detectado corretamente (confiança 0,91)
│   └── pimentao_23_erro.jpg          ← Erro: pimentão classificado como tomate
├── scripts/
│   └── organizar_dataset_yolo.py     ← Gera a estrutura images/labels do YOLO no Drive (usado pelo notebook)
├── requirements.txt                  ← Dependências para execução local (macOS e Windows)
└── README.md
```

> 📁 **Dataset e resultados de treino** ficam no Google Drive (fora do repositório, por tamanho) — estrutura completa documentada em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

---

## 🌱 Sobre o Problema

A FarmTech Solutions está expandindo seus serviços de IA para além do agronegócio — atuando também em saúde animal, segurança patrimonial, controle de acesso e análise documental. Como parte dessa expansão, a empresa está desenvolvendo capacidade de **visão computacional**, demonstrando na prática como um sistema de detecção e classificação de objetos funciona.

Este projeto usa **YOLO** (You Only Look Once) para detectar e diferenciar dois objetos visualmente distintos — **tomate** e **pimentão** — a partir de um dataset customizado, fotografado e rotulado pela própria equipe.

---

## 🤖 Solução Técnica

### Pipeline (Entrega 1)

```
Captura de imagens (celular, 80 fotos: 40 tomate + 40 pimentão)
              ↓
    Google Drive (Dataset_bruto/ → Dataset_dividido/ → images/ + labels/)
              ↓
   Rotulação manual   ← anotação das bounding boxes
              ↓
   Google Colab        ← treino YOLO customizado
              ↓
  2 simulações (30 e 60 épocas) → comparação de métricas
              ↓
     Teste em imagens nunca vistas → prints dos resultados
```

Prints do teste: [`prints_teste/`](./prints_teste/) (resultados completos na seção 7 do notebook).

### Entrega 2 — Comparação de Abordagens

Sobre a mesma base de dados (tomate × pimentão), três abordagens são comparadas:

| Abordagem | Descrição |
|:----------|:----------|
| YOLO customizado | Modelo da Entrega 1, fine-tuned no dataset próprio |
| YOLO tradicional | Modelo padrão, sem customização |
| CNN treinada do zero | Rede convolucional construída e treinada especificamente para este dataset |

Critérios de comparação: facilidade de uso/integração, precisão, tempo de treinamento, tempo de inferência.

### Escopo Opcional (não vale nota — soma pontos entre Fases 5, 6 e 7)

- **Opção 1:** ESP32-CAM (ou webcam) reconhecendo tomate/pimentão em tempo real, usando o modelo `best.pt` da Entrega 1
- **Opção 2:** Transfer Learning + Fine Tuning (VGG/Inception/MobileNet) + segmentação de imagem antes da classificação

---

## ▶️ Como Executar

### 1. Pré-requisitos

| Ferramenta | Observação |
|:-----------|:-----------|
| Conta Google | Para Google Drive e Google Colab |
| Navegador | Não é necessário instalar nada localmente — o treino roda no Colab (execução local é opcional, ver seção 4) |

### 2. Acessar o notebook

O notebook principal está na raiz deste repositório:
[`GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb)

1. Baixe o notebook (ou abra direto pelo GitHub → "Open in Colab", se disponível)
2. Faça upload para o [Google Colab](https://colab.research.google.com)
3. Garanta que o dataset esteja organizado no seu Google Drive, na estrutura descrita em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md)
4. Execute as células em ordem — a primeira célula monta o Google Drive automaticamente

### 3. Dataset

O dataset (80 imagens + rotulações) não está neste repositório — fica no Google Drive, conforme o protocolo em [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) e a estrutura em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

### 4. Execução local (opcional — alternativa ao Colab)

> No **Google Colab não é preciso instalar nada**: a primeira célula de código do notebook instala o `ultralytics`, e o Colab já traz PyTorch e TensorFlow com GPU. **Não rode `pip install -r requirements.txt` no Colab** — isso substituiria o PyTorch com GPU do Colab.

Para rodar na própria máquina, use **Python 3.12 ou 3.13** (confira com `python --version`; no Mac pode ser `python3 --version`). Com Python 3.11 ou anterior a instalação falha.

**Passo 1 — Baixar o projeto e criar um ambiente virtual** (evita conflito com bibliotecas de outros projetos):

```bash
git clone https://github.com/Graca-Gerson/grupo-3-farmtech-fase6.git
cd grupo-3-farmtech-fase6
python -m venv .venv
```

Ative o ambiente — o comando muda conforme o sistema:

| Sistema | Comando para ativar |
|:--------|:--------------------|
| macOS / Linux | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Prompt de Comando) | `.venv\Scripts\activate.bat` |

**Passo 2 — Instalar as dependências** (conforme o sistema):

**🍎 macOS** — um único comando:

```bash
pip install -r requirements.txt
```

O PyTorch instalado já usa a GPU da Apple (MPS) automaticamente nos Macs com chip M1/M2/M3/M4.

**🪟 Windows sem placa de vídeo NVIDIA** — o mesmo comando único (treino roda em CPU, mais lento):

```bash
pip install -r requirements.txt
```

**🪟 Windows com placa de vídeo NVIDIA** — instale primeiro o PyTorch com suporte a GPU (CUDA), **depois** o restante:

```bash
pip install torch==2.14.0 torchvision==0.29.0 --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
```

A ordem importa: se o `requirements.txt` for instalado primeiro, o Windows fica com o PyTorch só de CPU. Para confirmar que a GPU foi reconhecida, rode `python -c "import torch; print(torch.cuda.is_available())"` — o esperado é `True`. Se aparecer `False`, atualize o driver da NVIDIA e rode de novo o primeiro comando acrescentando `--force-reinstall` no final (sem essa opção o pip mantém a versão de CPU já instalada).

> 💡 **TensorFlow no Windows** (usado na CNN da Entrega 2) roda só em CPU — o TensorFlow não oferece GPU nativa no Windows. Funciona normalmente, apenas mais devagar; para treinar com GPU, prefira o Colab.

**Resultado esperado da instalação:** nenhuma linha com `ERROR`. Pode levar vários minutos (PyTorch e TensorFlow são grandes, cerca de 1–2 GB no total).

**Passo 3 — Abrir o notebook:**

```bash
jupyter notebook GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb
```

> ⚠️ A primeira célula do notebook monta o Google Drive (`google.colab`), que só existe no Colab. Na execução local, pule essa célula e ajuste a variável `BASE_PATH` para a pasta onde está o dataset na sua máquina.

---

## 🔗 Links Rápidos

| Recurso | Link |
|:--------|:-----|
| 🌐 **Repositório GitHub** | [Graca-Gerson/grupo-3-farmtech-fase6](https://github.com/Graca-Gerson/grupo-3-farmtech-fase6) — Público |
| 🎬 **Vídeo Demonstrativo** | *(a publicar após a Entrega 1 e 2 estarem concluídas)* |
| 📓 Notebook Principal | [GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb) |
| 📸 Protocolo de Captura de Imagens | [docs/protocolo_captura_fotos.md](./docs/protocolo_captura_fotos.md) |
| 📁 Estrutura do Google Drive | [docs/estrutura_drive.md](./docs/estrutura_drive.md) |
| 🔄 Fluxo do Macroprocesso | [docs/macroprocesso.md](./docs/macroprocesso.md) |
| 📅 Cronograma | [docs/cronograma.md](./docs/cronograma.md) |
| 👥 Matriz RACI | [docs/raci.md](./docs/raci.md) |
| ⚠️ Matriz de Riscos | [docs/matriz_riscos.md](./docs/matriz_riscos.md) |
| 🎯 Matriz GUT | [docs/gut_matrix.md](./docs/gut_matrix.md) |
| 🐟 Diagrama de Ishikawa | [docs/ishikawa.md](./docs/ishikawa.md) |

---

<div align="center">

**FarmTech Vision** · FIAP IA - Inteligência Artificial 2026 · Fase 6
Turma A · Gerson (569624) · Lucas (568712) · Carlos (572809) · Ryann (571003)

</div>
