#!/usr/bin/env bash
set -euo pipefail

INSTALLER="/Users/chenxinyu/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py"

python "$INSTALLER" --repo hanzoskill/web-design-guidelines --path . --name web-design-guidelines
python "$INSTALLER" --repo hanzoskill/vercel-react-best-practices --path . --name vercel-react-best-practices
python "$INSTALLER" --repo JimLiu/baoyu-skills --path \
  skills/baoyu-cover-image \
  skills/baoyu-infographic \
  skills/baoyu-diagram \
  skills/baoyu-translate \
  skills/baoyu-format-markdown

echo "Installed recommended skills. Restart Codex to pick up new skills."

