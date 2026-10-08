# ⚠️ Matriz de Riscos — FarmTech Vision (Fase 6)

> **FIAP Challenge — Fase 6** · 14 riscos identificados no planejamento — 3 P0, 5 P1, 4 P2, 2 P3
> Escala: Impacto (Baixo/Médio/Alto/Crítico) × Probabilidade (Baixa/Média/Alta)

---

## Matriz

| ID | Risco | Impacto | Probabilidade | Prioridade | Mitigação | Responsável | Status |
|:--:|-------|:-------:|:--------------:|:----------:|-----------|:------------:|:------:|
| P0-1 | Commit após 13/10/2026 desclassifica a entrega | Crítico | Média | **P0** | Reservar 13/10 só para revisão/submissão; travar commits a partir de 12/10 | Gerson | 🔲 Aberto |
| P0-2 | Ambiente de treino (GPU Colab) não validado antes do início | Crítico | Média | **P0** | Validar runtime GPU e cota na semana 1; plano B documentado | Gerson | ✅ Fechado |
| P0-3 | Dataset com menos de 80 imagens corretamente rotuladas | Crítico | Média | **P0** | Checklist de contagem mínima; validação cruzada por 2 membros | Carlos | ✅ Fechado |
| P1-1 | Atraso na coleta/organização das 80 imagens | Alto | Média | P1 | Iniciar coleta na semana 1, dividida entre os 3 membros | Carlos | ✅ Fechado |
| P1-2 | Equipe reduzida (3 efetivos) sobrecarregada | Alto | Média | P1 | Não alocar Lucas em caminho crítico; balancear tarefas | Gerson | 🔲 Aberto |
| P1-3 | Notebook sem versionamento incremental (commits grandes) | Alto | Média | P1 | Commits pequenos por etapa, mensagens padronizadas | Gerson | 🟡 Mitigado |
| P1-4 | Falta de validação cruzada rigorosa treino/val/teste | Alto | Média | P1 | Split fixo 32/4/4 documentado, métricas nos 3 conjuntos | Gerson | 🟡 Mitigado |
| P1-5 | Dependência do Make Sense IA sem plano de contingência | Alto | Média | P1 | LabelImg/Roboflow como backup documentado | Carlos | ✅ Fechado |
| P2-1 | Complexidade do escopo opcional 2 sem tempo real disponível | Médio | Média | P2 | Só iniciar após checkpoint de 07/10 confirmar folga | Gerson | ✅ Fechado |
| P2-2 | Links quebrados no README (notebook/vídeo) | Médio | Média | P2 | Testar manualmente cada link antes da entrega final | Ryann | 🔲 Aberto |
| P2-3 | Falta de padronização de nomenclatura (Drive/repo) | Médio | Média | P2 | Convenção de nomes definida já na semana 1 | Ryann | ✅ Fechado |
| P2-4 | Vídeo pode exceder o limite de 5 minutos | Médio | Média | P2 | Roteiro e duração-alvo definidos antes da gravação | Ryann | 🟡 Mitigado |
| P3-1 | Ausência de changelog de decisões técnicas | Baixo | Baixa | P3 | Manter `DECISIONS.md` com registro breve por marco | Gerson | 🔲 Aberto |
| P3-2 | Ausência de testes de sanidade no notebook | Baixo | Baixa | P3 | Células de assert básicas antes de blocos de treino | Carlos | 🟡 Mitigado |

**Legenda de status:** ✅ Fechado (não se materializou ou foi resolvido) · 🟡 Mitigado (efeito reduzido, ainda acompanhado) · 🔲 Aberto (acompanhamento até a entrega).

### Situação atualizada (01/10 a 08/10/2026)

| ID | Situação | Evidência |
|:--:|:--------:|-----------|
| P0-2 | ✅ Fechado | GPU T4 do Colab validada; os treinos das Entregas 1 e 2 rodaram nela |
| P0-3 | ✅ Fechado | 80 imagens e 80 rótulos conferidos (32/4/4 por classe); a verificação automática do notebook falha se faltar algum |
| P1-1 | ✅ Fechado | Coleta concluída em 16–17/09, dentro do prazo |
| P1-3 | 🟡 Mitigado | Notebooks versionados em commits por etapa (dataset → treino → avaliação → análise) |
| P1-4 | 🟡 Mitigado | Métricas nos 3 conjuntos: treino e validação nas duas entregas e, na Entrega 2, mAP no teste da YOLO customizada (mAP50 = 0,970). Segue mitigado, não fechado: o teste tem só 8 imagens |
| P1-5 | ✅ Fechado | Rotulação concluída no Make Sense IA, sem precisar do plano B |
| P2-3 | ✅ Fechado | Nomes do Drive padronizados por script (`scripts/organizar_dataset_yolo.py`), documentados em `estrutura_drive.md` |
| P2-1 | ✅ Fechado | O checkpoint de decisão foi antecipado para 02/10, com as Entregas 1 e 2 já executadas, e decidiu fazer o escopo opcional 2. Os treinos foram executados no Colab e o notebook ficou completo em 03/10 (F6-16 concluída), sem atrasar as Entregas 1 e 2; só falta o vídeo, acompanhado na F6-18 |
| P2-4 | 🟡 Mitigado | Roteiros de gravação da Entrega 1 (≈4min20s) e do escopo opcional 1 (≈3min50s) definidos, cronometrados e validados. A gravação dos três vídeos (F6-05, F6-17 e F6-18) foi reagendada para 09/10. Fecha quando os vídeos publicados tiverem até 5 minutos |
| P3-2 | 🟡 Mitigado | Verificações automáticas antes do treino: a célula 2.2 da Entrega 1 e a célula 2.0 da Entrega 2 conferem contagens, rótulos e classes e interrompem a execução com erro se algo faltar |

---

## Resumo por prioridade

| Prioridade | Quantidade | Foco |
|:----------:|:----------:|------|
| **P0** (crítico) | 3 | Bloqueadores de aprovação — prazo, ambiente de treino, dataset mínimo |
| **P1** (alto) | 5 | Risco significativo de atraso/qualidade — coleta, sobrecarga, versionamento, validação, dependência externa |
| **P2** (médio) | 4 | Impacto pontual, mitigável — escopo opcional, links, nomenclatura, duração do vídeo |
| **P3** (baixo) | 2 | Melhoria recomendada, não bloqueante — changelog, testes de sanidade |

---

## Observações

- Os 3 riscos P0 concentram-se nas fases iniciais do projeto (semana 1) — validar ambiente e iniciar coleta cedo reduz a maior parte do risco crítico.
- Nenhum risco tem probabilidade "Alta" isolada — todos giram em torno de "Média", refletindo um projeto com plano bem definido, mas ainda não executado no momento do planejamento (sem histórico real de execução para calibrar melhor). A situação atualizada de cada risco está na seção "Situação atualizada".
- Este documento é a base para a Matriz GUT (`gut_matrix.md`) e para o Diagrama de Ishikawa (`ishikawa.md`).
