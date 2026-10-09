#!/usr/bin/env bash
# Publish to rjcn.dev: check the repo, rebuild the `wordpress` branch, and push
# main and wordpress to Gitea and GitHub. The GitHub push fires the Git It Write
# webhook, which updates the site. Run with `make publish`.
set -euo pipefail
cd "$(dirname "$0")/.."

# The build reads the working tree, so anything uncommitted would reach the
# site without being on main.
if [ "$(git branch --show-current)" != main ]; then
    echo "publish: switch to main first" >&2; exit 1
fi
if [ -n "$(git status --porcelain)" ]; then
    echo "publish: commit or stash your changes first" >&2; git status --short >&2; exit 1
fi

python3 scripts/check.py
python3 scripts/wordpress.py
git push origin main wordpress
git push github main wordpress
