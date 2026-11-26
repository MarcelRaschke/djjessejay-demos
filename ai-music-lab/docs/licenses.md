# Lizenz-Matrix: Musik-Modelle & Output

Stand: Ende 2025 / Anfang 2026. **Immer die Lizenz des konkreten Checkpoints auf
Hugging Face pruefen** — Lizenzen aendern sich zwischen Versionen.

## Modelle

| Modell | Lizenz | kommerzielle Nutzung des Outputs? |
|---|---|---|
| ACE-Step 1.5 | Apache 2.0 | ✅ ja |
| Bark (Suno-Gruender) | MIT | ✅ ja |
| Riffusion | MIT | ✅ ja |
| MusicGen (Meta) | Code MIT, **Gewichte CC-BY-NC 4.0** | ❌ nein |
| Jukebox (OpenAI) | non-commercial | ❌ nein |
| Stable Audio Open 1.x | Stability AI Community License | ✅ bis 1 Mio. $ Jahresumsatz, danach kommerzielle Lizenz noetig |
| YuE v1 | Apache 2.0 | ✅ (Code), Gewichte separat pruefen |
| YuE2 | Code Apache 2.0, Gewichte CC-BY-NC + Creator-Permission | ❌ ohne Lizenz |
| MiniMax-Music | eigene ToS, Namensnennung | ⚠️ ab 20 Mio. $ Lizenz noetig |

## Gehostete Dienste

| Dienst | Modellzugang | kommerzielle Rechte |
|---|---|---|
| Suno (App) | Free/Pro/Premier; **keine oeffentliche API** (nur invite-only Partner) | Pro+ gewaehrt kommerzielle Lizenz, aber kein Eigentum am Output |
| Udio | App-Pläne | laut ToS eingeschraenkt |
| Drittanbieter-„Suno-API" (Reseller) | inoffiziell | ⚠️ rechtlich grau, instabil, ToS-Risiko |
| Unofficial Wrapper (Cookie + Captcha-Solver) | verstoss gegen ToS | ❌ nicht verwenden |

## Urheberrecht (USA, orientierend)

- US Copyright Office (Jan 2025): **rein KI-generiertes Material ist nicht
  urheberrechtlich schuetzbar**; Schutz entsteht durch menschliche Beitraege
  (Auswahl, Bearbeitung, Arrangement) — Einzelfallpruefung.
- In Deutschland/EU: aehnlich — urheberrechtlicher Schutz erfordert eine
  persoenliche geistige Schoepfung; KI-Output allein genuegt i. d. R. nicht.

## Praxis-Checkliste vor Veroeffentlichung

- [ ] Lizenz des verwendeten Checkpoints dokumentiert
- [ ] Bei CC-BY-NC: Output nur nicht-kommerziell (oder kommerzielle Lizenz erworben)
- [ ] Bei gehosteten Diensten: Nutzungsrechte laut Plan/ToS geprueft
- [ ] KI-Beteiligung transparent deklariert (C2PA-Metadaten / Wasserzeichen wo moeglich)
- [ ] Trainingsdaten-Risiko beachtet (Major-Labels-Klagen gegen Suno/Udio;
      Warner-Settlement Nov 2025 mit Lizenzpartnerschaft)
