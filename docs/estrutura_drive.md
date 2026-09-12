# Estrutura de Pastas — Google Drive (Fase 6)

## Passo a passo para criar

Crie essa estrutura de pastas no seu Google Drive (pessoal ou do grupo — compartilhe com Carlos e Ryann como Editor):

```
FarmTech_Fase6/
├── dataset_bruto/
│   ├── tomate/          ← as 40 fotos de tomate, antes de qualquer divisão
│   └── pimentao/        ← as 40 fotos de pimentão, antes de qualquer divisão
│
├── dataset_dividido/
│   ├── tomate/
│   │   ├── treino/      ← 32 imagens
│   │   ├── validacao/   ← 4 imagens
│   │   └── teste/       ← 4 imagens
│   └── pimentao/
│       ├── treino/      ← 32 imagens
│       ├── validacao/   ← 4 imagens
│       └── teste/       ← 4 imagens
│
├── rotulacoes/
│   └── (aqui entram os arquivos gerados pelo Make Sense IA — 
│        exporta como YOLO format, um .txt por imagem)
│
└── resultados/
    ├── epocas_30/       ← outputs do treino com 30 épocas
    └── epocas_60/       ← outputs do treino com 60 épocas
```

## Por que essa estrutura

- **`dataset_bruto/`** — mantém as fotos originais intactas, caso precise refazer a divisão treino/val/teste depois
- **`dataset_dividido/`** — já no formato exato que o YOLO espera (pastas separadas por split)
- **`rotulacoes/`** — centraliza os arquivos de anotação, separados das imagens (facilita conferir se todas as imagens têm rótulo correspondente)
- **`resultados/`** — separa as duas simulações de época (30 vs 60) pedidas no enunciado, facilitando comparar depois

## Como dividir 40 em 32/4/4

Depois de ter as 40 fotos de cada classe na pasta `dataset_bruto/`, a divisão pode ser:
- Ordenar as fotos (ex: por nome de arquivo)
- Pegar as primeiras 32 → `treino/`
- Próximas 4 → `validacao/`
- Últimas 4 → `teste/`

Ou, melhor ainda (evita viés de ordem): embaralhar aleatoriamente antes de dividir. Isso pode ser feito com poucas linhas de código Python dentro do próprio Colab (usando `random.shuffle`), então não precisa fazer manualmente — dá pra automatizar essa etapa dentro do notebook.
