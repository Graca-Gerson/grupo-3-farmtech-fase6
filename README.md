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
| 4 | Comparar YOLO customizado × YOLO tradicional × CNN treinada do zero | ✅ |
| 5 | Documentar achados, conclusões e limitações (notebook + README) | 🔄 Entregas 1 e 2 documentadas nos notebooks (seção 8 de cada) |
| 6 | Gravar vídeo demonstrativo (até 5min, YouTube não listado) | 🔲 |
| 7 | *(Escopo opcional)* Sistema de coleta em tempo real via ESP32-CAM/webcam | 🔲 |
| 8 | *(Escopo opcional)* Transfer Learning + segmentação de imagem | 🔲 |

---

## ✅ Status do Projeto

> 🔄 **Entregas 1 e 2 concluídas nos notebooks** — dataset coletado e rotulado, YOLO customizado treinado em 2 simulações (30 e 60 épocas), comparação, teste e conclusões documentados. Entrega 2: [notebook de comparação](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb) executado no Colab, com as três abordagens medidas nas mesmas 8 imagens de teste e a análise crítica na seção 8.

| Etapa | Status | Observação |
|:------|:------:|:-----------|
| Repositório GitHub criado | ✅ | Público, `grupo-3-farmtech-fase6` |
| Planejamento e cronograma | ✅ | 14 tarefas (F6-01 a F6-14), 14 riscos mapeados |
| Protocolo de captura de imagens definido | ✅ | Ver [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) |
| Estrutura do Google Drive organizada | ✅ | Ver [`docs/estrutura_drive.md`](./docs/estrutura_drive.md) |
| Coleta das 80 imagens | ✅ | 40 tomate + 40 pimentão, divididas em 32/4/4 (treino/validação/teste) por classe |
| Rotulação | ✅ | 80 rótulos em formato YOLO |
| Treino YOLO (Entrega 1) | ✅ | 2 simulações: 30 e 60 épocas — melhor resultado com 60 épocas (mAP50 = 0,916 na validação); comparação nas seções 4 a 6 do [notebook](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb) |
| Teste em imagens nunca vistas | ✅ | 7 de 8 imagens corretas — seção 7 do notebook e prints em [`prints_teste/`](./prints_teste/) |
| Conclusões da Entrega 1 | ✅ | Pontos fortes, limitações e aprendizados na seção 8 do notebook |
| Vídeo da Entrega 1 | 🔲 | Próxima etapa |
| Comparação de abordagens (Entrega 2) | ✅ | [Notebook](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb) executado: YOLO customizada e CNN do zero acertaram 7 de 8 imagens de teste; YOLO tradicional 0 de 8 (não conhece as classes), mas localizou os 8 objetos — tabela na seção 7 e análise crítica na seção 8 |
| README final + vídeo | 🔲 | Última etapa antes da entrega |

---

## 🗂️ Estrutura do Projeto

```
grupo-3-farmtech-fase6/
├── GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb            ← Notebook principal (Entrega 1)
├── GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb   ← Notebook da Entrega 2 (comparação de abordagens)
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
│   ├── tomate_17_acerto.jpg          ← Tomate detectado corretamente (confiança 0,92)
│   ├── tomate_23_acerto.jpg          ← Tomate detectado corretamente (confiança 0,91)
│   ├── tomate_29_acerto.jpg          ← Tomate detectado corretamente (confiança 0,96)
│   ├── tomate_37_acerto.jpg          ← Tomate detectado corretamente (confiança 0,97)
│   ├── pimentao_12_acerto.jpg        ← Pimentão detectado corretamente (confiança 0,94)
│   ├── pimentao_23_erro.jpg          ← Erro: pimentão classificado como tomate
│   ├── pimentao_29_acerto.jpg        ← Pimentão detectado corretamente (confiança 0,81)
│   ├── pimentao_36_acerto.jpg        ← Pimentão detectado corretamente (confiança 0,77)
│   └── entrega2/                     ← Prints da Entrega 2 (extraídos das saídas do notebook)
│       ├── yolo_customizada_x_tradicional_8_imagens_teste.png
│       ├── cnn_curvas_aprendizado.png
│       └── cnn_respostas_8_imagens_teste.png
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

> **Origem dos prints:** as 8 imagens de teste processadas pelo modelo oficial da Entrega 1 (60 épocas, `best.pt` do treino de 30/09, confiança mínima 0,5). `tomate_23` e `pimentao_23` foram extraídos da execução registrada no notebook; os outros 6 foram gerados com o mesmo `best.pt` e os mesmos parâmetros da célula de predição — as detecções são idênticas às da tabela da seção 7.1.

### Entrega 2 — Comparação de Abordagens

Sobre a mesma base de dados (tomate × pimentão), três abordagens são comparadas:

| Abordagem | Descrição |
|:----------|:----------|
| YOLO customizado | Modelo da Entrega 1 (`best.pt`), fine-tuned no dataset próprio |
| YOLO tradicional | YOLOv8n padrão, com os pesos genéricos do COCO, usado sem nenhum treino no dataset |
| CNN treinada do zero | Rede convolucional com arquitetura própria, treinada para classificar a imagem inteira |

Critérios de comparação: facilidade de uso/integração, precisão, tempo de treinamento, tempo de inferência — todos medidos nas mesmas 8 imagens de teste da Entrega 1.

**Resultado em uma linha:** a YOLO customizada (mAP50 de 0,970 no teste) é a indicada para detectar e localizar os frutos; a CNN do zero empatou na classificação da imagem inteira (7 de 8, errando outra imagem) com treino de cerca de 11 s; a YOLO tradicional sabe *onde* está o objeto, mas não *o que* ele é. Números, tempos e limitações na tabela da seção 7 e na seção 8 do notebook.

Notebook: [`GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb)

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

Os notebooks estão na raiz deste repositório:
- Entrega 1: [`GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb)
- Entrega 2: [`GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb)

Os passos abaixo valem para os dois.

1. **Crie o atalho da pasta do projeto no seu Drive (uma única vez).** A pasta `FarmTech_Fase6` fica no Google Drive de um integrante e é compartilhada com o grupo. No Google Drive, abra **Compartilhados comigo**, clique com o botão direito em `FarmTech_Fase6` → **Organizar** → **Adicionar atalho** → **Meu Drive**. Sem o atalho, o notebook não encontra o dataset e o treino não consegue salvar os resultados. A estrutura da pasta está em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).
2. **Abra o notebook direto do GitHub no Colab.** No [Google Colab](https://colab.research.google.com), use **Arquivo → Abrir notebook → GitHub**, informe `Graca-Gerson/grupo-3-farmtech-fase6` e escolha o notebook. Não use cópias antigas salvas no Drive.
3. **Ative a GPU.** Em **Ambiente de execução → Alterar tipo de ambiente de execução**, selecione **GPU T4**. A segunda célula de código confirma se a GPU foi reconhecida (o treino na CPU é muito mais lento).
4. **Troque o executor antes de rodar.** Na primeira célula de código, altere `EXECUTOR = 'gerson'` para o seu primeiro nome (minúsculo, sem acento). Os resultados do treino são gravados em `Resultados/epocas_30_<seu nome>/` e `Resultados/epocas_60_<seu nome>/`, e as imagens do teste com as detecções em `Resultados/predict_<seu nome>/teste/`, sem misturar com os resultados de outros integrantes.
5. **Execute as células em ordem.** A primeira monta o Google Drive (o Colab pede autorização de acesso).
6. **Não salve o notebook de volta no GitHub.** A versão do repositório guarda os resultados oficiais documentados. Se o Colab oferecer salvar no GitHub ou perguntar sobre alterações ao fechar, descarte.

> Como o treino usa semente fixa (`seed=0`, `deterministic=True`), uma nova execução com GPU T4 deve reproduzir as mesmas métricas registradas no notebook.

> **Entrega 2:** o notebook usa o modelo treinado na Entrega 1 (não treina o YOLO de novo) e a estrutura do dataset gerada pela seção 2.1 do notebook da Entrega 1 — os dois já existem no Drive. Os resultados (modelo da CNN, tabelas e imagens) são gravados em `Resultados/entrega2_<seu nome>/`. A CNN também usa semente fixa, mas na GPU pode variar ligeiramente entre execuções.

### 3. Dataset

O dataset (80 imagens + rotulações) não está neste repositório — fica no Google Drive, conforme o protocolo em [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) e a estrutura em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

### 4. Execução local (opcional — alternativa ao Colab)

> No **Google Colab não é preciso instalar nada**: a terceira célula de código do notebook instala o `ultralytics`, e o Colab já traz PyTorch e TensorFlow com GPU. **Não rode `pip install -r requirements.txt` no Colab** — isso substituiria o PyTorch com GPU do Colab.

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
| 🎬 **Vídeo Demonstrativo** | *(Entrega 1 — a publicar)* |
| 📓 Notebook Principal (Entrega 1) | [GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb) |
| 📓 Notebook da Entrega 2 | [GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb) |
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
