# Ir Além 2 — Transfer Learning × CNN do zero, com e sem segmentação

> **FIAP — Fase 6 · Escopo opcional 2** · Classificação de tomate e pimentão com uma rede pré-treinada (MobileNetV2) e com pré-segmentação automática (GrabCut)

> 🔄 **Situação:** estrutura inicial. O notebook já carrega o dataset e segmenta as imagens (seções 1 a 3); os treinos, a tabela comparativa e as conclusões (seções 4 a 8) serão feitos na execução com GPU.

## 🎯 Objetivo

A Entrega 2 treinou uma **CNN do zero** para classificar a imagem inteira. Este escopo testa duas hipóteses, sobre as mesmas 80 imagens e a **mesma divisão** das Entregas 1 e 2 (32 treino / 4 validação / 4 teste por classe):

1. **Uma rede pré-treinada classifica melhor que uma treinada do zero?** Para isso, *Transfer Learning* com a **MobileNetV2**, pré-treinada na ImageNet: as camadas convolucionais ficam congeladas e só o classificador final é treinado com as nossas fotos.
2. **Separar o objeto do fundo antes de classificar ajuda?** Para isso, **segmentação automática com GrabCut** (OpenCV): o programa cria uma máscara do fruto sem nenhuma rotulagem manual nova, remove o fundo e recorta a imagem no objeto antes de ela entrar na rede.

## 🧪 Plano de comparação

As duas hipóteses se cruzam em 4 combinações, todas avaliadas nas mesmas 8 imagens de teste:

| | **Sem segmentação** | **Com segmentação (GrabCut)** |
|:--|:--:|:--:|
| **CNN do zero** | resultado da Entrega 2 (não é treinada de novo) | seção 4 do notebook |
| **Transfer Learning (MobileNetV2)** | seção 5 do notebook | seção 6 do notebook |

Para cada combinação, o notebook vai medir:
- a **acurácia no teste**;
- o **tempo de treino**;
- o **tempo de inferência por imagem**. Nas versões com segmentação, esse tempo inclui o GrabCut, porque ele faz parte do caminho até a resposta.

**Por que essas escolhas:**
- **MobileNetV2:** é leve, tem pesos da ImageNet prontos no Keras e aceita entrada de 128×128, o mesmo tamanho da CNN da Entrega 2, o que mantém a comparação justa.
- **GrabCut:** separa objeto e fundo a partir de um retângulo inicial, sem precisar de máscaras desenhadas à mão. O dataset tem caixas (do YOLO), mas não tem máscaras.

## 🔍 Primeiro teste da segmentação

As seções 1 a 3 do notebook foram executadas fora do Colab, sobre uma cópia do dataset, para validar o carregamento e o GrabCut **antes** dos treinos:
- **Carregamento:** a versão sem segmentação é **idêntica, pixel a pixel**, à entrada que a CNN da Entrega 2 recebeu.
- **Resultado do GrabCut nas 8 imagens de teste, avaliado visualmente:**
  - **5 recortes bons** (tomate_17, tomate_37, pimentao_23, pimentao_29 e pimentao_36);
  - **3 com problema**, todos em fotos com fundo carregado ou fruto fora do centro:
    - tomate_23 e pimentao_12 levaram junto parte do fundo;
    - no tomate_29, o GrabCut pegou a parede no lugar do fruto.

  Isso já indica que a segmentação pode **atrapalhar** em algumas imagens. A comparação da seção 7 vai medir o efeito real na classificação.
- **Custo:** cerca de 0,4 s por imagem em CPU. As 80 imagens levaram 29,5 s.

## ▶️ Como Executar

O notebook roda no **Google Colab**, um serviço do Google que executa o código no navegador, sem instalar nada no computador. Os passos são os mesmos dos notebooks das Entregas 1 e 2.

**O que você precisa:**
- uma **conta Google** com acesso à pasta `FarmTech_Fase6` no Google Drive (compartilhada com o grupo);
- um **navegador**.

**Passo 1 — Criar o atalho da pasta do projeto no seu Google Drive (só na primeira vez).**

1. Abra [drive.google.com](https://drive.google.com) e clique em **Compartilhados comigo**.
2. Clique com o botão direito em **`FarmTech_Fase6`** → **Organizar** → **Adicionar atalho** → **Meu Drive** → **Adicionar**.

**Deu certo se:** em **Meu Drive** aparece `FarmTech_Fase6` com uma pequena seta no ícone. Quem é dono da pasta já a vê ali e pode pular este passo.

**Passo 2 — Abrir o notebook no Colab, direto do GitHub.**

1. Abra [colab.research.google.com](https://colab.research.google.com). Se aparecer a janela "Abrir notebook", use-a; se não, clique em **Arquivo → Abrir notebook**.
2. Clique na aba **GitHub**, digite `Graca-Gerson/grupo-3-farmtech-fase6` e aperte **Enter**.
3. Na lista, clique em **`ir_alem/ir_alem_2_transfer_learning/GersonFerreiraDaGraca_rm569624_pbl_fase6_ir_alem_2.ipynb`**.

**Deu certo se:** o notebook abre com o título "Ir Além 2 — Transfer Learning × CNN do zero, com e sem segmentação".

**Passo 3 — Ligar a GPU.** Menu **Ambiente de execução → Alterar tipo de ambiente de execução** → escolha **GPU T4** → **Salvar**.

**Passo 4 — Colocar o seu nome.** Na **primeira célula de código** (a que começa com `# Conectar ao Google Drive`), troque `EXECUTOR = 'gerson'` pelo seu primeiro nome, em minúsculas e sem acento (por exemplo, `EXECUTOR = 'ryann'`). Os resultados vão para `Resultados/ir_alem_2_<seu nome>/` no Drive.

**Passo 5 — Executar tudo.** Menu **Ambiente de execução → Executar tudo**. Na primeira célula, aceite o pedido de acesso ao Google Drive (**Conectar ao Google Drive** → escolha a conta → **Permitir**).

**O que deve aparecer:**

| Célula | Resultado esperado |
|--------|--------------------|
| Primeira (Drive) | `Mounted at /content/drive` |
| Segunda (ambiente) | `GPU disponível: True`. Se aparecer `False`, refaça o passo 3 |
| 2.0 (dataset) | `treino: 64`, `validacao: 8`, `teste: 8` e `✅ Dataset conferido` |
| 3.1 (teste visual) | Uma figura com 3 linhas: original, máscara e imagem recortada |
| 3.2 (segmentação de todas) | O tempo total do GrabCut nas 80 imagens |

**Passo 6 — Não salvar o notebook de volta no GitHub.** Se o Colab perguntar sobre salvar alterações ao fechar, **descarte**. Não use **Arquivo → Salvar uma cópia no GitHub**.

**Se algo der errado:**

| O que aparece | O que significa | O que fazer |
|---------------|-----------------|-------------|
| `FileNotFoundError` com `/content/drive/MyDrive/FarmTech_Fase6` | O Colab não achou a pasta do projeto | Faça o passo 1 e execute tudo de novo |
| `RuntimeError: Problemas no dataset` | Faltam fotos nas pastas do Drive | Leia a lista na mensagem e confira as pastas em [`docs/estrutura_drive.md`](../../docs/estrutura_drive.md) |
| `GPU disponível: False` | Sem GPU | Refaça o passo 3 e execute tudo de novo |

## 📁 Arquivos

```
ir_alem/ir_alem_2_transfer_learning/
├── README.md                                                ← este arquivo
└── GersonFerreiraDaGraca_rm569624_pbl_fase6_ir_alem_2.ipynb   ← notebook (seções 1 a 3 prontas; treinos a executar)
```

No Drive, cada execução grava em `Resultados/ir_alem_2_<executor>/`. Hoje isso inclui a figura `grabcut_exemplos.png`; os modelos e a tabela comparativa entram quando os treinos forem implementados.
