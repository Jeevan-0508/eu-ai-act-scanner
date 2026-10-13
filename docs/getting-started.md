# Getting started

AI Compliance Scanner is a static browser application with three independent checklists: EU AI Act, ISO/IEC 42001 and NIST AI RMF. It stores answers locally in the browser and generates a downloadable HTML report from the EU AI Act flow.

## Try it

Open the [live scanner](https://jeevan-0508.github.io/eu-ai-act-scanner). Start from Home, choose a framework, complete the checklist or wizard, and review the score, gaps and recommended next actions. Use the report export only as a working record for human review.

## Run locally

The repository is deployable as static files. Serve the repository root with any HTTP server, or use the GitHub Pages site. The PWA manifest and service worker support installation and offline use after the initial load.

```bash
python3 -m http.server 4173
```

Open <http://localhost:4173/> and inspect the browser console if a local asset is missing.

## Scope boundary

The scanner is a structured self-assessment aid. Its plain-language requirement model is not a legal opinion, certification, audit result or substitute for reading the official frameworks and obtaining qualified advice. Scores describe the answers entered, not the organisation's objective compliance.
