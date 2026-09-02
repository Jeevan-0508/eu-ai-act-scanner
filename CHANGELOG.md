# Changelog

Tracks when the scanner's compliance content (risk qualifiers, requirements, deadlines, ISO 42001 crosswalk) was last reviewed against the source regulation, and what changed.

Source of truth: [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) (EU AI Act), consolidated text on EUR-Lex.

## How this works

This is a static, client-side tool — it has no backend and cannot read or rewrite its own compliance data automatically. The "Check for regulation updates" button in the app opens the live EUR-Lex text in a new tab for manual review and lets you mark a review date, which is stored locally in your browser (not synced to this repo).

When the regulation actually changes in a way that affects this tool (new implementing/delegated act, Annex III category change, deadline shift), update:
- The `QS` (qualifier questions) and `RQ` (requirements) data objects in `index.html`
- The `TIMELINE` array (phased deadlines)
- This changelog, with the date and what changed
- The `REG_LAST_REVIEWED` constant in `index.html`

## History

### 2026-09-02
- Added regulation-currency tracking: "last verified" badge (footer + results page) and a manual "Check for regulation updates" flow that opens the EUR-Lex source text.
- No content changes to the underlying compliance data this cycle — regulation confirmed current as of this date.

### 2026-09-01 (initial release)
- Built scanner covering: Prohibited (Art. 5), High-Risk (Annex III), Limited Risk (Art. 50), GPAI (Arts. 51-55), Minimal Risk.
- Added Compliance Timeline (Aug 2024 → Aug 2027 phased deadlines) and ISO/IEC 42001:2023 crosswalk for High-Risk and GPAI tiers.
