# 🇪🇺 EU AI Act Compliance Scanner

**Classify any AI system against Regulation (EU) 2024/1689 in under 10 minutes. No signup, no server, no data leaves your browser.**

**Live app:** [jeevan-0508.github.io/eu-ai-act-scanner](https://jeevan-0508.github.io/eu-ai-act-scanner)
**License:** All Rights Reserved — see [LICENSE](LICENSE)
**Regulatory basis:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689) (EU AI Act)

---

## What it does

A four-step wizard that turns a plain-English description of an AI system into a legally-grounded risk classification, a gap-analysis checklist, and an exportable compliance report.

```
  STEP 1              STEP 2                STEP 3                STEP 4
System Profile  →  Risk Qualifiers   →  Technical Controls  →  Results & Report
 (name, team,      (14 questions          (36 requirements       (score, gaps,
  purpose)          mapped to Arts.        MUST/SHOULD,           HTML export,
                     5/50/51-55/            tier-specific)         ISO 42001 tab)
                     Annex III)
```

### Classification logic

```
                    AI SYSTEM
                        │
          ┌─────────────┼──────────────────────┐
          ▼             ▼                      ▼
   Art. 5 triggers   Annex III use case    Art. 51 GPAI /
  (social scoring,   (employment, infra,    foundation model
   biometric ID,      law enforcement,          │
   subliminal)        education, justice,       ▼
          │            migration, credit)   GPAI MODEL
          ▼                  │              (Arts. 51-55)
     PROHIBITED              ▼
      (Art. 5)          HIGH RISK
                        (Annex III)
                              │
                    else → chatbot / deepfake /
                           emotion inference?
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              LIMITED RISK          MINIMAL RISK
               (Art. 50)             (Art. 95)
```

## Features

- **14 risk-qualifier questions**, each mapped to a specific EU AI Act article, with an "explain why" panel (plain-English + logistics/Amazon-style examples)
- **36 compliance requirements** across all 5 tiers, tagged **MUST** (legally mandatory) or **SHOULD** (best practice)
- **Compliance Timeline** — the actual phased rollout (Aug 2024 → Aug 2027), flags deadlines that have already passed
- **ISO/IEC 42001:2023 crosswalk** for High-Risk and GPAI tiers — 13 management-system clauses mapped to their AI Act article equivalents, scored separately
- **Exportable HTML report** — client-generated, no server round-trip
- **PWA** — installable, works offline, network-first service worker (always fetches the latest version when you're online)
- **Regulation-currency tracking** — a "last verified" badge plus a one-click "check for updates" flow against the live EUR-Lex text (see [CHANGELOG.md](CHANGELOG.md))

## Stack

Single `index.html`. Vanilla JS, no framework, no build step, no dependencies. `manifest.json` + `sw.js` for PWA install.

## Regulatory basis

> **Regulation (EU) 2024/1689** of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act) and amending certain Union legislative acts. Official Journal of the European Union, L 2024/1689, 12 July 2024.

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689)

This is a static tool — its compliance data does not update itself. See [CHANGELOG.md](CHANGELOG.md) for how currency is tracked and reviewed.

**Disclaimer:** For internal compliance self-assessment only. Not legal advice. Consult qualified legal counsel for binding compliance decisions.

## License

All rights reserved. See [LICENSE](LICENSE) — no permission is granted to copy, modify, redistribute, or reuse this code without written permission from the author.

## Author

Built by **[Jeevan Kumar](https://github.com/Jeevan-0508)** — Amazon Transportation Risk & Fraud Operations, transitioning into AI Governance / AI Risk.
