# 📅 Cronograma — FarmTech Vision (Fase 6)

> **FIAP Challenge — Fase 6** · Período: 15/09/2026 – 13/10/2026 (21 dias úteis)

![Jornada do Projeto](./cronograma_fase6.png)

---

## Tarefas

| Código | Tarefa | Responsável | Início | Fim | Prioridade | Status |
|:------:|--------|:-----------:|:------:|:---:|:----------:|:------:|
| F6-01 | Setup do repositório `grupo-3-farmtech-fase6` | Gerson | 15/09 | 15/09 | Alta | ✅ Concluída |
| F6-02 | Coletar e organizar 80 imagens (tomate/pimentão) em pastas treino/val/teste | Carlos | 16/09 | 18/09 | Crítica | ✅ Concluída |
| F6-03 | Rotular imagens de treino via Make Sense IA (com backup LabelImg/Roboflow) | Ryann | 21/09 | 22/09 | Crítica | ✅ Concluída |
| F6-04 | Desenvolver notebook Entrega 1 (YOLO customizado, 2 simulações de épocas) | Gerson | 23/09 | 28/09 | Crítica | ✅ Concluída (30/09) |
| F6-05 | Gravar vídeo Entrega 1 (até 5min, YouTube não listado) e finalizar README | Ryann | 29/09 | 09/10 | Alta | 🔲 Pendente (reagendada de 05/10) |
| F6-06 | Checkpoint de decisão — avaliar folga real antes de investir em escopo opcional | Gerson | 07/10 | 07/10 | Alta | ✅ Concluída (antecipada para 02/10) |
| F6-07 | Desenvolver notebook Entrega 2 (YOLO tradicional + CNN do zero + comparação) | Gerson | 01/10 | 05/10 | Crítica | ✅ Concluída (via F6-11 a F6-14) |
| F6-08 | *Escopo opcional 1* — webcam reconhecendo tomate/pimentão em tempo real com o `best.pt` da Entrega 1 | Lucas | 08/10 | 09/10 | Baixa | ✅ Concluída (via F6-15) |
| F6-09 | *Escopo opcional 2* — Transfer Learning + segmentação | Ryann | 08/10 | 12/10 | Baixa | ✅ Concluída (via F6-16) |
| F6-10 | QA final — testar links, revisar README, congelar commits, submeter | Gerson | 13/10 | 13/10 | Crítica | 🔲 Pendente |
| F6-11 | Entrega 2 — YOLO tradicional (YOLOv8n com pesos do COCO, sem treino no dataset) aplicado ao teste | Gerson | 01/10 | 01/10 | Crítica | ✅ Concluída |
| F6-12 | Entrega 2 — CNN treinada do zero para classificar a imagem inteira | Gerson | 01/10 | 02/10 | Crítica | ✅ Concluída |
| F6-13 | Entrega 2 — Comparação crítica das 3 abordagens (facilidade de uso, precisão, tempo de treino e de inferência) | Gerson | 02/10 | 05/10 | Crítica | ✅ Concluída |
| F6-14 | Entrega 2 — Notebook executado no Colab + README atualizado | Gerson | 02/10 | 05/10 | Crítica | ✅ Concluída |
| F6-15 | *Escopo opcional 1* — detecção em tempo real via webcam com o `best.pt` da Entrega 1 (script + README) | Gerson | 02/10 | 09/10 | Baixa | ✅ Concluída (03/10) |
| F6-16 | *Escopo opcional 2* — CNN do zero × Transfer Learning com Fine Tuning (MobileNetV2), com e sem segmentação (U2-Net) | Gerson | 03/10 | 12/10 | Baixa | ✅ Concluída (03/10) |
| F6-17 | Gravar vídeo do escopo opcional 1 (até 5min, YouTube não listado) | Gerson | 09/10 | 09/10 | Baixa | 🔲 Pendente (reagendada de 06/10) |
| F6-18 | Gravar vídeo do escopo opcional 2 (até 5min, YouTube não listado) | Gerson | 09/10 | 09/10 | Baixa | 🔲 Pendente (reagendada de 07/10) |

> **Subtarefas da Entrega 2:** F6-11 a F6-14 detalham a F6-07 (criadas em 01/10, quando a Entrega 2 começou); com as quatro concluídas e a revisão final do notebook feita, a F6-07 foi concluída.
>
> **Subtarefa do escopo opcional 1:** a F6-15 detalha a F6-08 e foi antecipada para 02/10, porque as Entregas 1 e 2 já estavam executadas; usa webcam no lugar da ESP32-CAM, por falta da placa. Concluída em 03/10 (script, README e teste ao vivo), o que fechou também a F6-08.
>
> **Subtarefa do escopo opcional 2:** a F6-16 detalha a F6-09 e foi antecipada para 03/10; compara 4 combinações (CNN do zero ou MobileNetV2 com Fine Tuning, com ou sem segmentação pela U2-Net) na mesma divisão das Entregas 1 e 2. Concluída em 03/10 (notebook executado, resultados e conclusões), o que fechou também a F6-09.
>
> **Tarefas de vídeo:** a gravação é uma atividade separada do trabalho técnico, cada uma com tarefa e prazo próprios — F6-05 (Entrega 1), F6-17 (escopo opcional 1) e F6-18 (escopo opcional 2), as três com prazo em 09/10 (reagendadas de 05/10, 06/10 e 07/10, respectivamente). Cada uma termina quando o vídeo de até 5 minutos estiver publicado no YouTube como "não listado" e com o link no README.
>
> **Checkpoint F6-06 (decisão tomada em 02/10):** com as Entregas 1 e 2 já executadas, o checkpoint previsto para 07/10 foi antecipado e decidiu **fazer** os dois escopos opcionais. A execução foi feita nas subtarefas F6-15 (escopo 1) e F6-16 (escopo 2), ambas concluídas em 03/10, com Lucas e Ryann seguindo como responsáveis formais de F6-08 e F6-09; os vídeos estão nas F6-17 e F6-18. Os escopos opcionais não valem nota de boletim.

---

## Entregáveis formais

| Código | Entregável | Prazo | Responsável |
|:------:|-----------|:-----:|:-----------:|
| E01 | Repositório GitHub público, estrutura organizada | 15/09 | Gerson |
| E02 | Dataset de 80 imagens organizado (treino/val/teste) | 18/09 | Carlos |
| E03 | Rotulações exportadas (formato YOLO) | 22/09 | Ryann |
| E04 | Notebook Entrega 1 (YOLO customizado, 2 simulações) | 28/09 | Gerson |
| E05 | Vídeo + README da Entrega 1 | 09/10 | Ryann |
| E06 | Notebook Entrega 2 (comparação de 3 abordagens) | 05/10 | Gerson |
| E07 | Escopo opcional 1 — sistema de detecção em tempo real via webcam | 09/10 | Lucas |
| E08 | Escopo opcional 2 — Transfer Learning + segmentação | 12/10 | Ryann |
| E09 | README final consolidado + link do vídeo | 13/10 | Gerson |

---

## Marcos principais

| Marco | Data | Observação |
|-------|:----:|------------|
| Início do projeto | 15/09/2026 | Setup do repositório concluído |
| Dataset pronto | 18/09/2026 | Fim da coleta de imagens |
| Rotulação concluída | 22/09/2026 | Pronto para treino |
| Entrega 1 completa | 09/10/2026 | Notebook concluído em 30/09; vídeo + README (F6-05) com prazo em 09/10 (reagendado de 05/10) |
| Checkpoint de decisão | 07/10/2026 | Go/no-go para o escopo opcional — antecipado: decisão de fazer tomada em 02/10 |
| Entrega 2 completa | 05/10/2026 | Comparação das 3 abordagens |
| Vídeos dos escopos opcionais | 09/10/2026 | F6-17 e F6-18 (reagendadas de 06/10 e 07/10) |
| Congelamento de commits | 12/10/2026 | A partir desta data, nenhum commit novo — só revisão (P0-1) |
| **Entrega final** | **13/10/2026** | Prazo improrrogável — nenhum commit após esta data |

---

## Observações

- Cronograma respeita apenas dias úteis (segunda a sexta) — fins de semana ficam como folga estratégica.
- Equipe efetiva de 3 membros (Gerson, Carlos, Ryann) para o caminho crítico — Lucas participa formalmente da equipe, alocado apenas em F6-08 (tarefa opcional, sem carga em nenhuma task obrigatória), por questão pessoal registrada.
