#!/usr/bin/env bash
set -euo pipefail

INSTALLER="/Users/chenxinyu/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"
MANAGER="scripts/skills-manager.py"

if [[ ! -f "$MANAGER" ]]; then
  echo "[ERROR] $MANAGER not found. Run this script from the repo root." >&2
  exit 1
fi

if [[ ! -f "$INSTALLER" ]]; then
  echo "[ERROR] Codex skill installer not found at $INSTALLER" >&2
  exit 1
fi

python "$INSTALLER" --repo hanzoskill/web-design-guidelines --path . --name web-design-guidelines
python "$INSTALLER" --repo hanzoskill/vercel-react-best-practices --path . --name vercel-react-best-practices
python "$INSTALLER" --repo JimLiu/baoyu-skills --path \
  skills/baoyu-cover-image \
  skills/baoyu-infographic \
  skills/baoyu-diagram \
  skills/baoyu-translate \
  skills/baoyu-format-markdown

echo "[OK] Installed recommended skills. Restart Codex to pick up new skills."
echo "[OK] You can list managed skills with: python scripts/skills-manager.py list"

python "$MANAGER" doctor

