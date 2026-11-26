# Architektur-Vergleich: Text-zu-Musik-Systeme

Stand: Ende 2025 / Anfang 2026. Quellen: publizierte Paper (arXiv) und Modellkarten.

## Gemeinsame Pipeline

```
Text / Lyrics ──► Text-Encoder (T5 / CLAP / MuLan-Embedding)
                     │  Conditioning (+ Classifier-Free Guidance)
                     ▼
           Generator ("Musik-Gehirn")
           • autoregressiv: Transformer ueber diskrete Audio-Tokens
           • Diffusion: Rauschen in einem Latent schrittweise entfernen
                     │
   Waveform ◄── Decoder/Vocoder ◄── komprimierte Repraesentation
                     ▲
   Neural Codec (EnCodec / SoundStream, RVQ)  ODER  VAE-Latent
```

## Kernfakten

- **Neural Codecs**: EnCodec (Meta) komprimiert 32-kHz-Audio auf 50 Frames/s × 4
  Codebooks = **200 Token/s** (je Codebook 2048 Eintraege, Residual Vector Quantization).
  SoundStream (Google) arbeitet aehnlich mit 24 kHz.
- **AudioLM** (Google 2022): fuehrt die Aufteilung in *semantische* Tokens (Struktur)
  und *akustische* Tokens (Detail) ein — heute Standard.
- **MusicGen** (Meta 2023, Copet et al.): *ein* Transformer (300M / 1.5B / 3.3B Parameter,
  ~20k h lizenzierte Musik), Delay-Interleaving der 4 Codebooks; 30 s Audio ≈ 1500
  Vorhersageschritte; Text per Cross-Attention, Guidance Scale 3.0.
- **Stable Audio** (2024): Latent Diffusion auf kontinuierlichem VAE-Latent,
  44,1 kHz Stereo, Timing-Embeddings (Laenge ist Teil der Konditionierung), Guidance 7.0.
- **MuLan** (Google 2022): gemeinsamer Text-Audio-Einbettungsraum — natuerlichsprachige
  Prompts steuern die Musik direkt.

## System-Vergleich

| System | Repraesentation | Generator | typische Laenge | Vocals |
|---|---|---|---|---|
| MusicGen | EnCodec-Tokens, 32 kHz, 200 Tok/s | 1-stufiger Transformer + Delay | ~30 s | nein |
| Stable Audio (Open 1.x) | VAE-Latent, 44,1 kHz Stereo | Latent Diffusion + Timing | ≤ 47 s | nein |
| AudioLM / MusicLM | semantische + akustische Tokens | hierarchisches LM | Minuten | nein |
| YuE / YuE2, ACE-Step | Lyrics + Flow-Tokens | LLM/DiT-basiert | voller Song | ja |
| Bark (Suno-Gruender) | Audio-Tokens | autoregressiv | Sekunden | ja (Stimme) |
| Suno (Bark + Chirp) | nicht oeffentlich dokumentiert | – | bis 8 Min (v4.5), v5 mit 12 Stems | ja |

## Suno-Versionen (oeffentlich bekannt)

- v3.5 (2024): 4 Min., bessere Songstruktur
- v4 (Nov 2024): Vocal-Qualitaet, Persona/Cover
- v4.5 (2025): bis 8 Min., Add Vocals/Instrumental, Extend
- v5 (Sept 2025, Codename „chirp-crow"): Multi-Track-Latent-Streams, 12 Stems,
  320 kbps Export, ELO ~1293; Suno Studio als DAW (Premier)

Suno publiziert keine Architektur-Papers. Interne Details per Reverse Engineering
zu gewinnen, ist nicht zulaessig (ToS/zh. IP) — siehe Security-Checkliste.
