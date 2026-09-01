# EU AI Act Compliance Scanner

> Scan any AI system for EU AI Act (Regulation 2024/1689) compliance — risk classification, gap analysis, and exportable reports.

**Live:** [jeevan-0508.github.io/eu-ai-act-scanner](https://jeevan-0508.github.io/eu-ai-act-scanner)

---

## What it does

A free, browser-based compliance wizard that:

1. **Classifies** your AI system into the correct EU AI Act risk tier
2. **Generates** a tailored requirements checklist for your tier
3. **Scores** your current compliance posture
4. **Exports** a printable HTML compliance report

All classification logic is derived directly from **Regulation (EU) 2024/1689** (Official Journal L 2024/1689, 12 July 2024).

---

## Risk tiers covered

| Tier | Articles | Description |
|------|----------|-------------|
| 🚫 Prohibited | Article 5 | Social scoring, real-time biometric ID, subliminal manipulation |
| ⚠ High Risk | Annex III | Employment, infrastructure, law enforcement, education, finance, migration, justice |
| ⚡ Limited Risk | Article 50 | Chatbots, deepfakes, emotion inference — transparency obligations |
| 🤖 GPAI Model | Articles 51–55 | Foundation models, LLMs — documentation and copyright obligations |
| ✓ Minimal Risk | Article 95 | Everything else — voluntary codes encouraged |

---

## Features

- **14 risk qualifier questions** mapped to exact EU AI Act articles
- **27+ compliance requirements** tagged MUST / SHOULD
- **SVG compliance score ring** with live checklist
- **Exportable HTML report** with citation to official OJ text
- **PWA** — installable, works offline
- **No server, no signup** — runs 100% in your browser

---

## Stack

Pure HTML/CSS/JS — single `index.html`. No dependencies, no build step.

---

## Regulatory basis

This tool is based on:

> **Regulation (EU) 2024/1689** of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act) and amending certain Union legislative acts.
> Official Journal of the European Union, L 2024/1689, 12 July 2024.

Full text: [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689)

**Disclaimer:** This tool is for internal compliance self-assessment only and does not constitute legal advice. Consult qualified legal counsel for binding compliance decisions.

---

## Author

Built by [Jeevan Kumar](https://github.com/Jeevan-0508) · Amazon Transportation Risk & Fraud Operations
