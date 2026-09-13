# ⚠️ Matriz de Riscos — FarmTech Vision (Fase 6)

> **FIAP Challenge — Fase 6** · 14 riscos identificados no planejamento — 3 P0, 5 P1, 4 P2, 2 P3
> Escala: Impacto (Baixo/Médio/Alto/Crítico) × Probabilidade (Baixa/Média/Alta)

---

## Matriz

| ID | Risco | Impacto | Probabilidade | Prioridade | Mitigação | Responsável | Status |
|:--:|-------|:-------:|:--------------:|:----------:|-----------|:------------:|:------:|
| P0-1 | Commit após 13/10/2026 desclassifica a entrega | Crítico | Média | **P0** | Reservar 13/10 só para revisão/submissão; travar commits a partir de 12/10 | Gerson | 🔲 |
| P0-2 | Ambiente de treino (GPU Colab) não validado antes do início | Crítico | Média | **P0** | Validar runtime GPU e cota na semana 1; plano B documentado | Gerson | 🔲 |
| P0-3 | Dataset com menos de 80 imagens corretamente rotuladas | Crítico | Média | **P0** | Checklist de contagem mínima; validação cruzada por 2 membros | Carlos | 🔲 |
| P1-1 | Atraso na coleta/organização das 80 imagens | Alto | Média | P1 | Iniciar coleta na semana 1, dividida entre os 3 membros | Carlos | 🔲 |
| P1-2 | Equipe reduzida (3 efetivos) sobrecarregada | Alto | Média | P1 | Não alocar Lucas em caminho crítico; balancear tarefas | Gerson | 🔲 |
| P1-3 | Notebook sem versionamento incremental (commits grandes) | Alto | Média | P1 | Commits pequenos por etapa, mensagens padronizadas | Gerson | 🔲 |
| P1-4 | Falta de validação cruzada rigorosa treino/val/teste | Alto | Média | P1 | Split fixo 32/4/4 documentado, métricas nos 3 conjuntos | Gerson | 🔲 |
| P1-5 | Dependência do Make Sense IA sem plano de contingência | Alto | Média | P1 | LabelImg/Roboflow como backup documentado | Carlos | 🔲 |
| P2-1 | Complexidade do escopo opcional 2 sem tempo real disponível | Médio | Média | P2 | Só iniciar após checkpoint de 07/10 confirmar folga | Gerson | 🔲 |
| P2-2 | Links quebrados no README (notebook/vídeo) | Médio | Média | P2 | Testar manualmente cada link antes da entrega final | Ryann | 🔲 |
| P2-3 | Falta de padronização de nomenclatura (Drive/repo) | Médio | Média | P2 | Convenção de nomes definida já na semana 1 | Ryann | 🔲 |
| P2-4 | Vídeo pode exceder o limite de 5 minutos | Médio | Média | P2 | Roteiro e duração-alvo definidos antes da gravação | Ryann | 🔲 |
| P3-1 | Ausência de changelog de decisões técnicas | Baixo | Baixa | P3 | Manter `DECISIONS.md` com registro breve por marco | Gerson | 🔲 |
| P3-2 | Ausência de testes de sanidade no notebook | Baixo | Baixa | P3 | Células de assert básicas antes de blocos de treino | Carlos | 🔲 |

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
- Nenhum risco tem probabilidade "Alta" isolada — todos giram em torno de "Média", refletindo um projeto com plano bem definido, mas ainda não executado (sem histórico real de execução para calibrar melhor).
- Este documento é a base para a Matriz GUT (`gut_matrix.md`) e para o Diagrama de Ishikawa (`ishikawa.md`).
