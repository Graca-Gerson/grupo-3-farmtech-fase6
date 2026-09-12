# Protocolo de Captura — Dataset Tomate x Pimentão (Fase 6)

## Objetivo
80 imagens totais: 40 de tomate + 40 de pimentão, com variedade suficiente para o modelo generalizar bem (não decorar um único cenário).

## Regras gerais de captura

1. **Câmera:** celular é suficiente. Resolução mínima recomendada: 1080p (a maioria dos celulares atuais já atende).
2. **Formato:** salvar em `.jpg` (menor tamanho de arquivo, suficiente para o YOLO).
3. **Um objeto por foto:** cada imagem deve conter só **um** tomate OU **um** pimentão como sujeito principal — não misturar os dois na mesma foto (o modelo aprende a diferenciar classes, não a contar objetos).
4. **Variedade de cor (aproveitando o que já decidimos):**
   - Tomate: variar entre vermelho maduro, verde, e se possível algum tipo alaranjado/amarelo
   - Pimentão: variar entre vermelho, amarelo e verde
5. **Variedade de ângulo:** não fotografar todos de cima — misturar ângulo frontal, lateral, de cima, ligeiramente de baixo.
6. **Variedade de fundo:** evitar fundo sempre idêntico (ex: sempre a mesma bancada branca). Usar pelo menos 3-4 fundos diferentes (mesa de madeira, bancada, pano neutro, dentro de uma sacola/cesto).
7. **Variedade de iluminação:** misturar luz natural (perto de janela) e luz artificial de ambiente — evita que o modelo dependa só de um tipo de iluminação pra reconhecer o objeto.
8. **Distância:** variar um pouco a distância da câmera (não todas no mesmo zoom) — ajuda o modelo a reconhecer o objeto em tamanhos diferentes na imagem.

## Meta de distribuição por classe (40 fotos cada)

Sugestão de divisão para garantir variedade sem complicar a logística:

| Variação | Quantidade sugerida (de 40) |
|---|---|
| Cor 1 (ex: vermelho) | ~15 fotos |
| Cor 2 (ex: verde) | ~15 fotos |
| Cor 3 (ex: amarelo/laranja) | ~10 fotos |

Dentro de cada grupo de cor, já variar ângulo/fundo/luz naturalmente enquanto fotografa.

## Checklist antes de considerar o dataset pronto

- [ ] 40 fotos de tomate, todas nítidas (sem desfoque)
- [ ] 40 fotos de pimentão, todas nítidas
- [ ] Pelo menos 3 fundos diferentes usados em cada classe
- [ ] Pelo menos 3 ângulos diferentes usados em cada classe
- [ ] Nenhuma foto com os dois objetos juntos
- [ ] Nomes de arquivo organizados (sugestão: `tomate_001.jpg`, `tomate_002.jpg`... `pimentao_001.jpg`...)

## Depois da captura

1. Revisar rapidamente todas as fotos — descartar qualquer uma borrada, cortada ou com o objeto pouco visível
2. Fazer upload para a pasta correta no Google Drive (ver estrutura em `estrutura_drive.md`)
3. Seguir para a rotulação no Make Sense IA (task F6-03)
