#!/usr/bin/env bash
# Setup für den lokalen Text-zu-Musik-Generator (MusicGen / Meta AudioCraft).
set -euo pipefail

cd "$(dirname "$0")"

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Fertig. Test:"
echo "  python generate.py --prompt 'epischer Synthwave, 120 BPM' --seconds 8 --out out/song.wav"
