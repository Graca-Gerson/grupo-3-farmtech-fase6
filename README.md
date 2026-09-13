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
| 1 | Montar dataset customizado (80 imagens: 40 tomate + 40 pimentão) | 🔲 |
| 2 | Rotular imagens de treino | 🔲 |
| 3 | Treinar YOLO customizado com 2 configurações de épocas (30 e 60) | 🔲 |
| 4 | Comparar YOLO customizado × YOLO tradicional × CNN treinada do zero | 🔲 |
| 5 | Documentar achados, conclusões e limitações (notebook + README) | 🔲 |
| 6 | Gravar vídeo demonstrativo (até 5min, YouTube não listado) | 🔲 |
| 7 | *(Escopo opcional)* Sistema de coleta em tempo real via ESP32-CAM/webcam | 🔲 |
| 8 | *(Escopo opcional)* Transfer Learning + segmentação de imagem | 🔲 |

---

## ✅ Status do Projeto

> 🔄 **Em preparação** — estrutura do repositório, documentação de gestão e esqueleto do notebook já definidos. Coleta do dataset ainda não iniciada.

| Etapa | Status | Observação |
|:------|:------:|:-----------|
| Repositório GitHub criado | ✅ | Público, `grupo-3-farmtech-fase6` |
| Planejamento e cronograma | ✅ | 10 tarefas (F6-01 a F6-10), 14 riscos mapeados |
| Protocolo de captura de imagens definido | ✅ | Ver [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) |
| Estrutura do Google Drive planejada | ✅ | Ver [`docs/estrutura_drive.md`](./docs/estrutura_drive.md) |
| Esqueleto do notebook (Entrega 1) | ✅ | Estrutura pronta, aguardando dataset para execução |
| Coleta das 80 imagens | 🔲 | Próxima etapa |
| Rotulação | 🔲 | Depende da coleta |
| Treino YOLO (Entrega 1) | 🔲 | Depende da rotulação |
| Comparação de abordagens (Entrega 2) | 🔲 | Depende da Entrega 1 |
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
├── requirements.txt
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
    Google Drive (dataset_bruto/ → dataset_dividido/)
              ↓
   Rotulação manual   ← anotação das bounding boxes
              ↓
   Google Colab        ← treino YOLO customizado
              ↓
  2 simulações (30 e 60 épocas) → comparação de métricas
              ↓
     Teste em imagens nunca vistas → prints dos resultados
```

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
| Navegador | Não é necessário instalar nada localmente — o treino roda no Colab |

### 2. Acessar o notebook

O notebook principal está na raiz deste repositório:
[`GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb)

1. Baixe o notebook (ou abra direto pelo GitHub → "Open in Colab", se disponível)
2. Faça upload para o [Google Colab](https://colab.research.google.com)
3. Garanta que o dataset esteja organizado no seu Google Drive, na estrutura descrita em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md)
4. Execute as células em ordem — a primeira célula monta o Google Drive automaticamente

### 3. Dataset

O dataset (80 imagens + rotulações) não está neste repositório — fica no Google Drive, conforme o protocolo em [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) e a estrutura em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

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
