#!/usr/bin/env python3
"""Lokaler Text-zu-Musik-Generator (MusicGen / Meta AudioCraft).

Beispiel:
  python generate.py --prompt "melancholischer Jazz-Piano in regnerischer Bar" \
      --seconds 10 --out out/song.wav

WICHTIG (Lizenz): Die MusicGen-Gewichte stehen unter CC-BY-NC 4.0.
Generierter Output ist damit nur NICHT-kommerziell nutzbar.
Fuer kommerzielle Nutzung siehe docs/licenses.md (ACE-Step, Bark, Stable Audio Open).
"""
import argparse
import pathlib

import torch
import torchaudio
from audiocraft.models import MusicGen

MODELS = {
    "small": "facebook/musicgen-small",
    "medium": "facebook/musicgen-medium",
    "large": "facebook/musicgen-large",
    "melody": "facebook/musicgen-melody",
}


def main() -> None:
    ap = argparse.ArgumentParser(description="Text -> Musik, lokal generiert")
    ap.add_argument("--prompt", required=True, help="z. B. 'epischer Synthwave, 120 BPM'")
    ap.add_argument("--model", default="small", choices=MODELS.keys())
    ap.add_argument("--seconds", type=float, default=8.0, help="Gewuenschte Laenge in Sekunden")
    ap.add_argument("--out", default="out/song.wav")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--cfg", type=float, default=3.0, help="Classifier-free guidance scale")
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"device={device} model={args.model} prompt={args.prompt!r}")

    model = MusicGen.get_pretrained(MODELS[args.model], device=device)
    model.set_generation_params(
        duration=args.seconds,
        cfg_coef=args.cfg,
        temperature=1.0,
        top_k=250,
        top_p=0.0,
    )
    wav = model.generate([args.prompt])  # [1, channels, samples]

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    torchaudio.save(str(out), wav[0].cpu(), model.sample_rate)
    print(f"gespeichert: {out} ({model.sample_rate} Hz, {args.seconds}s)")


if __name__ == "__main__":
    main()
