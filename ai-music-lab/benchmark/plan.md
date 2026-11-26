# Benchmark-Plan: lokale Text-zu-Musik-Modelle vergleichen

Ziel: **ACE-Step 1.5** vs. **YuE2-3B** vs. **MusicGen-medium** auf gleicher Hardware,
strukturiert nach: Hypothese aufstellen → belegen/widerlegen → dokumentieren.

## Hypothesen

- **H1**: ACE-Step 1.5 erzeugt mit < 4 GB VRAM hörbare Songs mit Vocals.
- **H2**: MusicGen-medium ist die beste Instrumental-Qualitaet pro VRAM, aber auf
  ~30 s begrenzt und ohne Vocals.
- **H3**: YuE2 liefert die kohärenteste Songstruktur (Verse/Chorus), braucht aber
  ~24 GB VRAM und ist am langsamsten.
- **H4**: Nur ACE-Step (Apache 2.0) und Bark (MIT) sind ohne Umsatzlimit kommerziell nutzbar.

## Metriken

| Metrik | Skala | Erfassung |
|---|---|---|
| MOS (Mean Opinion Score) | 1–5 | Blindtest, n ≥ 10 Hörer |
| ELO | Paarvergleich | Blindtest, randomisierte Reihenfolge |
| Lyrics-Adhärenz | 0–2 | nur Vocal-Modelle (0=ignoriert, 2=vollständig) |
| Songlänge | Sekunden | automatisch |
| Inferenzzeit | Sekunden | gemessen |
| VRAM-Peak | GB | nvidia-smi / torch.cuda.max_memory_allocated |
| Lizenz-Score | 0=NC, 1=eingeschränkt, 2=freigegeben | aus docs/licenses.md |

## Ablauf

1. **Prompts**: 10 Stück (Genres × Stimmungen), identische Seeds pro Modell.
2. **Generierung**: pro Modell 10 Läufe → 30 Audios; Metadaten in `results.csv`.
3. **Blindtest**: Hörer bewerten ohne Modellkenntnis; Reihenfolge randomisiert.
4. **Auswertung**: Mittelwerte + Wilcoxon-Vorzeichen-Rang-Test (p < 0,05) für Paarvergleiche.
5. **Dokumentation**: `results.csv` + `report.md` mit H1–H4: **belegt / widerlegt / unentscheidbar**.

## Ergebnis-Template (`results.csv`)

```csv
modell,prompt_id,seed,mos,elo,lyrics_adhaerenz,laenge_s,inferenz_s,vram_gb,lizenz_score
```

## Offene Punkte

- [ ] ACE-Step 1.5 Basis-Modell auf < 4 GB VRAM verifizieren (ggf. quantisierte Variante)
- [ ] YuE2-3B: Gewicht-Lizenz (CC-BY-NC) → Benchmark nur nicht-kommerziell sinnvoll
- [ ] GPU fuer Benchmark bereitstellen (lokal oder Cloud: Spheron o. ä.)
