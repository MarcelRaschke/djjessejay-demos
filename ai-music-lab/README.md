# ai-music-lab — lokaler Text-zu-Musik-Generator

Lokales Experimentieren mit offenen Text-zu-Musik-Modellen (kein Cloud-Dienst,
keine unofficial API-Wrapper, volle Datenkontrolle). Enthält:

- `generate.py` — CLI: Text-Prompt → WAV (MusicGen / Meta AudioCraft)
- `setup.sh`, `requirements.txt` — reproduzierbares Setup
- `docs/` — Architektur-Vergleich, Lizenz-Matrix, Security-Checkliste
- `benchmark/` — Plan zum Vergleich lokaler Modelle (ACE-Step vs. YuE vs. MusicGen)

## Quickstart

```bash
bash setup.sh
source .venv/bin/activate
python generate.py --prompt "epischer Synthwave, 120 BPM" --seconds 8 --out out/song.wav
```

## Modelle & Hardware (Richtwerte)

| Modell-Shortcut | Hugging-Face-Checkpoint | VRAM (ca.) | Hinweis |
|---|---|---|---|
| `small` (default) | `facebook/musicgen-small` | 4–6 GB | schnell, fuer Tests |
| `medium` | `facebook/musicgen-medium` | 8–12 GB | gute Qualitaet |
| `large` | `facebook/musicgen-large` | 16+ GB | beste MusicGen-Qualitaet |
| `melody` | `facebook/musicgen-melody` | 8–12 GB | zusaetzlich Melodie-Conditioning |

CPU-Fallback funktioniert, ist aber sehr langsam. Gewichte belegen ca. 1–6 GB
Plattenplatz (Download beim ersten Lauf).

## ⚠️ Lizenz-Hinweis (wichtig)

- MusicGen-**Gewichte** sind **CC-BY-NC 4.0** → Output nur **nicht-kommerziell**.
- Kommerziell uneingeschraenkt nutzbar: **ACE-Step 1.5** (Apache 2.0) und **Bark** (MIT).
- **Stable Audio Open**: kommerziell bis 1 Mio. $ Jahresumsatz (Stability Community License).
- Details siehe `docs/licenses.md`. Immer die Lizenz des **konkreten Checkpoints** prüfen.

## Erweiterungen (geplant)

- Gleiches CLI für **ACE-Step 1.5**: `pip install git+https://github.com/ACE-Editor/ACE-Step.git`
- **YuE2** (volle Songs mit Vocals) über Hugging Face — braucht ~24 GB VRAM.
- Lyrics-Pipeline: eigenes LLM erzeugt Lyrics + Struktur-Tags (`[Verse]`, `[Chorus]`),
  die das Musik-Modell konditionieren.

## Verwandte Themen in diesem Repo

`beat-architekt/` (Beat Architekt) und `ivdj-v3..v5` sind die Browser-Demos;
dieses Verzeichnis ist bewusst **kein** Pages-Eintrag (siehe `pages.yml`-Exclude).
