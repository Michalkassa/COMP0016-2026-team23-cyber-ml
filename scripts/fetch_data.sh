#!/usr/bin/env bash
# Fetch the Wendover web-log dataset into data/raw/wendover/ (git-ignored).
# Usage: scripts/fetch_data.sh [path/to/local/ucl-cybersecurity-ml]
set -euo pipefail

REPO_URL="https://github.com/elikling/ucl-cybersecurity-ml.git"
SUBDIR="data/wendoverswimmongpool"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/data/raw/wendover"
FILES=(access_log.csv error_log.csv attack_labels.csv)

mkdir -p "$DEST"

if [[ $# -ge 1 ]]; then
  SRC="$1/$SUBDIR"
else
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  git clone --depth 1 --filter=blob:none --sparse "$REPO_URL" "$TMP/src"
  git -C "$TMP/src" sparse-checkout set "$SUBDIR"
  SRC="$TMP/src/$SUBDIR"
fi

for f in "${FILES[@]}"; do
  cp "$SRC/$f" "$DEST/$f"
done

echo "Copied to $DEST:"
(cd "$DEST" && shasum -a 256 "${FILES[@]}" | tee SHA256SUMS)
