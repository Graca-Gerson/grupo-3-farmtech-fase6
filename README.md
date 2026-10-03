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
| 7 | *(Escopo opcional)* Sistema de coleta em tempo real via ESP32-CAM/webcam | 🔄 Código e documentação prontos ([Ir Além 1](./ir_alem/ir_alem_1_deteccao_tempo_real/README.md)); teste ao vivo pendente |
| 8 | *(Escopo opcional)* Transfer Learning + segmentação de imagem | 🔲 |

---

## ✅ Status do Projeto

> 🔄 **Entregas 1 e 2 concluídas nos notebooks** — dataset coletado e rotulado, YOLO customizado treinado em 2 simulações (30 e 60 épocas), comparação, teste e conclusões documentados. Entrega 2: [notebook de comparação](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb) executado no Colab, com as três abordagens medidas nas mesmas 8 imagens de teste e a análise crítica na seção 8.

| Etapa | Status | Observação |
|:------|:------:|:-----------|
| Repositório GitHub criado | ✅ | Público, `grupo-3-farmtech-fase6` |
| Planejamento e cronograma | ✅ | 15 tarefas (F6-01 a F6-15), 14 riscos mapeados |
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
├── ir_alem/
│   └── ir_alem_1_deteccao_tempo_real/  ← Escopo opcional 1: detecção em tempo real via webcam com o best.pt
├── scripts/
│   ├── organizar_dataset_yolo.py     ← Gera a estrutura images/labels do YOLO no Drive (usado pelo notebook)
│   └── gerar_diagramas_fase6.py      ← Gera docs/estrutura_drive_fase6.png e docs/raci_fase6.png
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

- **Opção 1:** ESP32-CAM (ou webcam) reconhecendo tomate/pimentão em tempo real, usando o modelo `best.pt` da Entrega 1 — implementada com webcam: [`ir_alem/ir_alem_1_deteccao_tempo_real/`](./ir_alem/ir_alem_1_deteccao_tempo_real/README.md)
- **Opção 2:** Transfer Learning + Fine Tuning (VGG/Inception/MobileNet) + segmentação de imagem antes da classificação

---

## ▶️ Como Executar

Os notebooks rodam no **Google Colab** — um serviço do Google que executa o código no navegador, sem instalar nada no seu computador. É o caminho recomendado. A execução no próprio computador (seção 4) é opcional.

### 1. Pré-requisitos

| O que você precisa | Para quê |
|:-------------------|:---------|
| Uma **conta Google** com acesso à pasta `FarmTech_Fase6` no Google Drive (compartilhada com o grupo) | É onde ficam as 80 fotos, os rótulos e os resultados dos treinos |
| Um **navegador** (Chrome, Edge, Firefox ou Safari) | Para abrir o Google Drive e o Google Colab |

Os notebooks estão na raiz deste repositório:
- Entrega 1: [`GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb)
- Entrega 2: [`GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb`](./GersonFerreiraDaGraca_rm569624_pbl_fase6_entrega2.ipynb)

### 2. Rodar um notebook no Google Colab (passo a passo)

Os passos valem para os dois notebooks. O passo 1 é feito **uma única vez**; os demais, a cada execução.

**Passo 1 — Criar o atalho da pasta do projeto no seu Google Drive (só na primeira vez).**
A pasta `FarmTech_Fase6` fica no Drive de um integrante e foi compartilhada com você. O Colab só enxerga o que está em **Meu Drive**, por isso é preciso criar um atalho lá:

1. Abra [drive.google.com](https://drive.google.com) e clique em **Compartilhados comigo**, no menu da esquerda.
2. Clique com o botão direito em **`FarmTech_Fase6`** → **Organizar** → **Adicionar atalho**.
3. Escolha **Meu Drive** e clique em **Adicionar**.

**Deu certo se:** ao clicar em **Meu Drive**, aparece `FarmTech_Fase6` com uma pequena seta no ícone (o símbolo de atalho). Quem é dono da pasta já a vê em Meu Drive e pode pular este passo. A organização da pasta está descrita em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

**Passo 2 — Abrir o notebook no Colab, direto do GitHub.**

1. Abra [colab.research.google.com](https://colab.research.google.com). Se aparecer uma janela de "Abrir notebook", use-a; se não, clique em **Arquivo → Abrir notebook**.
2. Clique na aba **GitHub**.
3. No campo de busca, digite `Graca-Gerson/grupo-3-farmtech-fase6` e aperte **Enter**.
4. Clique no notebook desejado (Entrega 1 ou Entrega 2) na lista que aparece.

**Deu certo se:** o notebook abre com o título `GersonFerreiraDaGraca_rm569624_pbl_fase6...` no alto da página e as células de texto e código aparecem. Sempre abra pelo GitHub — **não** use cópias salvas no Drive, que podem estar desatualizadas.

**Passo 3 — Ligar a GPU (placa de vídeo do Google), que acelera o treino.**
Menu **Ambiente de execução → Alterar tipo de ambiente de execução** → em "Acelerador de hardware", escolha **GPU T4** → **Salvar**.

**Passo 4 — Colocar o seu nome no notebook.**
Na **primeira célula de código** (a que começa com `# Conectar ao Google Drive`), encontre a linha:

```python
EXECUTOR = 'gerson'
```

e troque `gerson` pelo **seu primeiro nome, em minúsculas e sem acento** — por exemplo, `EXECUTOR = 'ryann'`. Assim, os resultados do seu treino vão para pastas com o seu nome no Drive (`Resultados/epocas_30_ryann/`, `Resultados/epocas_60_ryann/`, `Resultados/predict_ryann/teste/` e, na Entrega 2, `Resultados/entrega2_ryann/`), sem misturar com os de outras pessoas.

**Passo 5 — Executar todas as células, em ordem.**
Menu **Ambiente de execução → Executar tudo**. O Colab roda as células de cima para baixo; cada uma mostra o resultado logo abaixo dela.

1. **Logo na primeira célula, aparece um pedido de acesso ao Google Drive.** Clique em **Conectar ao Google Drive**, escolha a sua conta e clique em **Permitir** (ou **Continuar**). **Deu certo se** a célula mostrar `Mounted at /content/drive`.
2. **A segunda célula confirma a GPU.** **Deu certo se** mostrar `GPU disponível: True` e `Dispositivo: Tesla T4`. Se mostrar `False`, refaça o passo 3 (o Colab vai pedir para reiniciar — aceite e repita o passo 5).
3. As células seguintes conferem o dataset, treinam e testam o modelo. **A execução terminou** quando a última célula de código mostrar resultado e nenhuma célula estiver com o ícone de "rodando" (círculo girando). Um treino de 60 épocas leva poucos minutos com a GPU T4.

**Passo 6 — Ao terminar, NÃO salvar o notebook de volta no GitHub.**
A versão do repositório guarda os resultados oficiais documentados. Não use **Arquivo → Salvar uma cópia no GitHub**, e, se o Colab perguntar sobre salvar alterações ao fechar a aba, **descarte**. Os resultados do seu treino já ficaram salvos no Drive, nas pastas com o seu nome.

> **Os números podem não sair idênticos aos do notebook.** O treino usa semente fixa (`seed=0`, `deterministic=True`), mas o Colab atualiza as bibliotecas da GPU sem aviso — numa nova execução em 01/10, com outra versão da CUDA, as métricas mudaram (detalhes na seção 6 do notebook da Entrega 1). A execução oficial documentada é a de 30/09.

> **Entrega 2:** o notebook não treina o YOLO de novo — usa o modelo oficial da Entrega 1 e a estrutura do dataset criada pelo notebook da Entrega 1, que já existem no Drive. Os resultados vão para `Resultados/entrega2_<seu nome>/`. A CNN também usa semente fixa, mas na GPU pode variar ligeiramente entre execuções.

**Se algo der errado no Colab:**

| O que aparece | O que significa | O que fazer |
|---------------|-----------------|-------------|
| Erro em vermelho com `FileNotFoundError` e `/content/drive/MyDrive/FarmTech_Fase6` | O Colab não encontrou a pasta do projeto no seu Drive | Faça o passo 1 (atalho em Meu Drive) e execute tudo de novo (passo 5) |
| `RuntimeError` dizendo que a estrutura do dataset tem problemas | Faltam fotos ou rótulos nas pastas do Drive | Leia a lista de problemas na própria mensagem e confira as pastas com [`docs/estrutura_drive.md`](./docs/estrutura_drive.md) |
| `GPU disponível: False` | O notebook está rodando sem a GPU | Refaça o passo 3 e execute tudo de novo |
| A primeira célula fica parada pedindo autorização | O pedido de acesso ao Drive não foi aceito | Clique em **Conectar ao Google Drive** e permita o acesso com a conta que tem a pasta do projeto |
| `ModuleNotFoundError: No module named 'ultralytics'` | Alguma célula foi pulada (a terceira célula é a que instala o YOLO) | Use **Executar tudo** em vez de rodar células soltas |

### 3. Dataset

O dataset (80 imagens + rotulações) não está neste repositório — fica no Google Drive, conforme o protocolo em [`docs/protocolo_captura_fotos.md`](./docs/protocolo_captura_fotos.md) e a estrutura em [`docs/estrutura_drive.md`](./docs/estrutura_drive.md).

### 4. Execução local (opcional — alternativa ao Colab)

> No **Google Colab não é preciso instalar nada** (a terceira célula de código do notebook instala o `ultralytics`, e o Colab já traz PyTorch e TensorFlow com GPU). **Não rode `pip install -r requirements.txt` no Colab** — isso substituiria o PyTorch com GPU do Colab. Esta seção é só para quem quer rodar no próprio computador.

**Passos 1 a 7 — preparar o computador (iguais aos do Ir Além 1).** Abrir o terminal, conferir o Python (3.12 ou 3.13), baixar o projeto, entrar na pasta, criar e ativar o ambiente virtual e instalar as bibliotecas são exatamente os passos 1 a 7 da receita do Ir Além 1, com a verificação de pasta em cada um:

- 🍎 [Receita para macOS — passos 1 a 7](./ir_alem/ir_alem_1_deteccao_tempo_real/README.md#macos)
- 🪟 [Receita para Windows — passos 1 a 7](./ir_alem/ir_alem_1_deteccao_tempo_real/README.md#windows)

Faça só até o passo 7 e volte para cá.

> 🪟 **Windows com placa de vídeo NVIDIA:** para treinar usando a placa, troque o passo 7 por estes dois comandos, nesta ordem (**neste momento você deve estar em `C:\Users\seunome\grupo-3-farmtech-fase6`, com `(.venv)`**):
>
> ```powershell
> pip install torch==2.11.0 torchvision==0.26.0 --index-url https://download.pytorch.org/whl/cu126
> pip install -r requirements.txt
> ```
>
> O primeiro instala o PyTorch com suporte à placa; o segundo, o restante. A ordem importa: na ordem inversa, o Windows fica com o PyTorch que só usa o processador. Para conferir, rode `python -c "import torch; print(torch.cuda.is_available())"` — **deu certo se** aparecer `True`. Se aparecer `False`, atualize o driver da NVIDIA e rode de novo o primeiro comando com `--force-reinstall` no final.
>
> 💡 O TensorFlow (usado na CNN da Entrega 2) roda só no processador no Windows — funciona, apenas mais devagar.

**Passo 8 — Abrir o notebook.**
**Neste momento você deve estar na pasta do projeto, com `(.venv)` no começo da linha** — confira com `pwd` (macOS: deve aparecer `/Users/seunome/grupo-3-farmtech-fase6`) ou `Get-Location` (Windows: `C:\Users\seunome\grupo-3-farmtech-fase6`). Se não, refaça os passos 4 e 6 da receita.

```bash
jupyter notebook GersonFerreiraDaGraca_rm569624_pbl_fase6.ipynb
```

Este comando abre o notebook no navegador (o Jupyter é o "Colab" local). **Deu certo se** abrir uma aba do navegador com o notebook. O terminal fica ocupado enquanto o Jupyter estiver aberto; para encerrar, feche a aba e aperte **Ctrl + C** no terminal.

> ⚠️ **Os notebooks foram feitos para o Colab.** A primeira célula de código conecta ao Google Drive, e isso só existe no Colab — no computador ela dá erro. Para rodar localmente: baixe a pasta `FarmTech_Fase6` do Google Drive para o seu computador, **não execute** a primeira célula e, no lugar dela, crie uma célula com o caminho da pasta baixada e o seu nome, por exemplo:
>
> ```python
> BASE_PATH = '/Users/seunome/Downloads/FarmTech_Fase6'   # Windows: r'C:\Users\seunome\Downloads\FarmTech_Fase6'
> EXECUTOR = 'seunome'
> ```
>
> Na Entrega 1, a célula **2.1** também usa um caminho que só existe no Colab (`/content/...`). Localmente, troque as duas linhas dela por esta, que usa a cópia do script que já vem no projeto:
>
> ```python
> !python scripts/organizar_dataset_yolo.py --base "{BASE_PATH}"
> ```

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
