<div align="center">

# EU AI Act Compliance Scanner

**Classify any AI system against Regulation (EU) 2024/1689 in under 10 minutes.**
No signup. No server. No data ever leaves your browser.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-jeevan--0508.github.io-6366f1?style=for-the-badge)](https://jeevan-0508.github.io/eu-ai-act-scanner)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge)](LICENSE)
[![Stack](https://img.shields.io/badge/Stack-Vanilla%20JS%20%7C%20No%20Deps-22c55e?style=for-the-badge)](#tech-stack)
[![PWA](https://img.shields.io/badge/PWA-Installable-818cf8?style=for-the-badge)](#tech-stack)

</div>

---

## Preview

<p align="center">
  <img src="screenshots/landing.png" alt="EU AI Act Scanner — landing page" width="800"><br><br>
  <img src="screenshots/wizard.png" alt="EU AI Act Scanner — System Profile wizard step" width="800">
</p>

## The problem

The EU AI Act (Regulation 2024/1689) is 144 pages long, has a five-tier risk system, and applies phased deadlines through 2027. Most teams building or buying an AI system have no fast way to answer: *"which tier are we in, and what do we actually have to do about it?"*

This tool answers that in four steps, in the browser, with every answer traced back to a specific article.

## How it works

```mermaid
flowchart LR
    A["① System Profile\nname · team · purpose"] --> B["② Risk Qualifiers\n14 questions → Arts. 5 / 50 / 51-55 / Annex III"]
    B --> C["③ Technical Controls\n36 requirements, MUST / SHOULD"]
    C --> D["④ Results & Report\nscore · gaps · HTML export · ISO 42001 tab"]
```

## Classification logic

```mermaid
flowchart TD
    S[AI System] --> P{Art. 5 trigger?\nsocial scoring, biometric ID,\nsubliminal manipulation}
    P -->|yes| PR[🚫 PROHIBITED — Art. 5]
    P -->|no| H{Annex III use case?\nemployment, infra, law enforcement,\neducation, justice, migration, credit}
    H -->|yes| HR[⚠️ HIGH RISK — Annex III]
    H -->|no| G{GPAI / foundation model?}
    G -->|yes| GP[🤖 GPAI MODEL — Arts. 51-55]
    G -->|no| L{Chatbot, deepfake,\nor emotion inference?}
    L -->|yes| LR[⚡ LIMITED RISK — Art. 50]
    L -->|no| MR[✅ MINIMAL RISK — Art. 95]
```

## Features

| | |
|---|---|
| **14 risk-qualifier questions** | Each mapped to a specific article, with an "explain why" panel in plain English + Amazon/logistics-style examples |
| **36 compliance requirements** | Across all 5 tiers, tagged **MUST** (legally mandatory) or **SHOULD** (best practice) |
| **Compliance Timeline** | Real phased rollout Aug 2024 → Aug 2027, flags deadlines already passed |
| **ISO/IEC 42001:2023 crosswalk** | 13 management-system clauses mapped to AI Act articles, scored separately (High-Risk / GPAI tiers) |
| **Exportable HTML report** | Generated entirely client-side, no server round-trip |
| **PWA** | Installable, works offline, network-first service worker so updates are never stuck behind a stale cache |
| **Regulation-currency tracking** | "Last verified" badge + one-click check against the live EUR-Lex text — see [CHANGELOG.md](CHANGELOG.md) |

## Tech stack

Single `index.html`. Vanilla JS, zero dependencies, zero build step. `manifest.json` + `sw.js` for PWA install.

## Regulatory basis

> **Regulation (EU) 2024/1689** of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union, L 2024/1689, 12 July 2024.

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689)

This is a static tool — its compliance data does not update itself. See [CHANGELOG.md](CHANGELOG.md) for how currency is tracked.

**Disclaimer:** For internal compliance self-assessment only. Not legal advice.

## License

All rights reserved — see [LICENSE](LICENSE). No permission is granted to copy, modify, redistribute, or reuse this code without written permission from the author.

---

<div align="center">

Built by **[Jeevan Kumar](https://github.com/Jeevan-0508)** — Amazon Transportation Risk & Fraud Operations, transitioning into AI Governance / AI Risk.

</div>
