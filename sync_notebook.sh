#!/bin/bash
# ============================================================
# sync_notebook.sh — Sincroniza fontes do NotebookLM
# Projeto: FarmTech Fase 6 — Visão Computacional (Grupo 3)
# Uso: bash sync_notebook.sh
# ============================================================
#
# Escopo de sync definido na criação do notebook (12/09/2026):
# README.md, CLAUDE.md, docs/protocolo_captura_fotos.md, docs/estrutura_drive.md,
# docs/briefing_fase6.md, docs/Diagnostico_Fase6_VIKI_CORRIGIDO.md.
# Lista fixa, não scan dinâmico de docs/ — revisar manualmente se novos
# documentos de processo relevantes forem criados (ex.: um novo docs/*.md).

set -uo pipefail

NB="6e477860-dcb0-4f30-90a0-89d3a9a1fe03"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

ERROS=0

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  FarmTech Fase 6 · Sync NotebookLM"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# ── Verificação de dependências (fail loud — sem isso, nada funciona) ───────
if ! command -v nlm &> /dev/null; then
  echo "✗ ERRO FATAL: nlm não encontrado."
  echo "  Instalar: uv tool install notebooklm-mcp-cli"
  exit 1
fi
if ! command -v jq &> /dev/null; then
  echo "✗ ERRO FATAL: jq não encontrado (necessário para match exato de título)."
  echo "  Instalar: brew install jq"
  exit 1
fi

# ── Sincroniza uma fonte: delete exato por título (se existir) + add ───────
sync_source() {
  local file="$1"
  local title="$2"

  if [ ! -f "$file" ]; then
    echo ""
    echo "✗ ERRO: arquivo não encontrado: $file (esperado no escopo de sync)"
    ERROS=$((ERROS + 1))
    return
  fi

  echo ""
  echo "→ Sincronizando: $title"

  # Match EXATO por título via JSON — evita falso-positivo de grep por
  # substring e captura TODAS as duplicatas existentes.
  local existing_ids
  existing_ids=$(nlm source list "$NB" --json 2>/dev/null | jq -r --arg t "$title" '.[] | select(.title == $t) | .id')

  if [ -n "$existing_ids" ]; then
    local n
    n=$(echo "$existing_ids" | wc -l | tr -d ' ')
    echo "  Encontrada(s) $n versão(ões) anterior(es) — deletando..."
    # shellcheck disable=SC2086  # word-splitting intencional: múltiplos IDs
    if ! nlm source delete $existing_ids --confirm; then
      echo "  ✗ ERRO ao deletar versão(ões) anterior(es) de '$title' — fonte NÃO sincronizada."
      ERROS=$((ERROS + 1))
      return
    fi
  fi

  echo "  Adicionando versão atual..."
  if ! nlm source add "$NB" --file "$file" --title "$title" --wait; then
    echo "  ✗ ERRO ao adicionar '$title'."
    ERROS=$((ERROS + 1))
    return
  fi

  echo "  ✓ $title sincronizado"
}

# ── Documentos do agente e do projeto ───────────────────────────────────────
sync_source "README.md"                                    "README.md"
sync_source "CLAUDE.md"                                     "CLAUDE.md"
sync_source "docs/protocolo_captura_fotos.md"                "docs/protocolo_captura_fotos.md"
sync_source "docs/estrutura_drive.md"                        "docs/estrutura_drive.md"
sync_source "docs/briefing_fase6.md"                         "docs/briefing_fase6.md"
sync_source "docs/Diagnostico_Fase6_VIKI_CORRIGIDO.md"       "docs/Diagnostico_Fase6_VIKI_CORRIGIDO.md"

# ── Resultado final ──────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ "$ERROS" -gt 0 ]; then
  echo "  ✗ Sync concluído com $ERROS erro(s) — revisar mensagens acima"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  exit 1
fi
echo "  ✓ NotebookLM sincronizado com sucesso"
echo "  Notebook: FarmTech Fase 6 - Grupo 3"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
