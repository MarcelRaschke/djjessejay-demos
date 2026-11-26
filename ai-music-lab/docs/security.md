# Security-Checkliste: eigene Anwendung mit Musik-KI

Orientiert an OWASP LLM Top 10, angepasst auf Text-zu-Musik-Pipelines.

## Bedrohungen & Gegenmassnahmen

- [ ] **Prompt Injection** (OWASP LLM01): Lyrics/Prompts koennen Befehle enthalten.
      Test mit Payloads; serverseitig filtern, Prompts nicht ungefiltert an nachgelagerte Systeme weiterreichen.
- [ ] **API-Key-Lecks**: Keys im Vault (z. B. Doppler/HashiCorp), nie in Env-Files im Repo;
      `pre-commit` + gitleaks/trufflehog im CI; Keys rotieren.
- [ ] **PII in Prompts/Lyrics**: personenbezogene Daten vor der Verarbeitung entfernen/loggen.
- [ ] **Kosten/Missbrauch**: Rate-Limiting pro Nutzer/Key, Budget-Caps, Queue mit Prioritaet.
- [ ] **Lizenz-Compliance**: Modell + Checkpoint + Lizenz pro Generation loggen;
      kommerzielle Nutzung nur mit passender Lizenz (siehe `licenses.md`).
- [ ] **Keine unofficial API-Wrapper** (Cookie-Diebstahl, Captcha-Solver, scripted Browser):
      verstossen gegen ToS, sind instabil und rechtlich riskant.
- [ ] **Output-Provenance**: C2PA-Metadaten / Wasserzeichen, KI-Nutzung dokumentieren.
- [ ] **Modell-Sicherheit**: Safety-Filter fuer Lyrics (Hass, Selbstschaedigung etc.),
      Content-Moderation der Prompts.
- [ ] **Infra**: GPU-Workloads isoliert, keine ungeprueften Uploads (Audio-Dateien parsen),
      TLS ueberall, Audit-Logging (wer hat wann welchen Prompt generiert).

## Review-Workflow (analysieren → Hypothese → Test → Dokumentieren)

1. Threat-Model als Markdown (Assets, Angreifer, Annahmen)
2. Hypothesen formulieren (z. B. „Prompt-Feld ermoeglicht Injection in nachgelagertes LLM")
3. Tests durchfuehren (Payload-Liste, Rate-Limit-Tests, Key-Exposure-Scan)
4. Ergebnisse + Fixes dokumentieren (dieses File fortschreiben)
