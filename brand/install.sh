#!/usr/bin/env bash
# Installa i file di brand INGLY DESIGN in ~/.claude/.
# I file già presenti vengono sovrascritti solo con --force (copia di backup .bak).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
DEST="$HOME/.claude"
FORCE="${1:-}"

put() {  # put <sorgente> <destinazione>
  mkdir -p "$(dirname "$2")"
  if [ -e "$2" ] && ! cmp -s "$1" "$2"; then
    if [ "$FORCE" = "--force" ]; then cp "$2" "$2.bak"; cp "$1" "$2"; echo "aggiornato (backup .bak): $2"
    else echo "SALTATO, esiste già ed è diverso (usa --force): $2"; fi
  else
    cp "$1" "$2"; echo "ok: $2"
  fi
}

put "$HERE/brand-voice-ingly.md"   "$DEST/brand-voice-ingly.md"
put "$HERE/instagram/voice.md"     "$DEST/instagram/voice.md"
put "$HERE/slop-it-ingly.json"     "$DEST/instagram/slop-it-ingly.json"
put "$ROOT/CLAUDE.md"              "$DEST/CLAUDE.md"
