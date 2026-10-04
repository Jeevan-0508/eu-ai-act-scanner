#!/usr/bin/env python3
"""Check the official EU AI regulatory sources this static app cites.

This monitor is deliberately separate from the scanner's compliance logic. It
records normalized source hashes and provenance; it never rewrites rules,
requirements, deadlines, or scoring. A changed source is REVIEW_REQUIRED for a
human, and a failed fetch leaves the last valid state untouched.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "data" / "regulatory-monitor.json"
HISTORY_PATH = ROOT / "data" / "regulatory-changes.jsonl"
USER_AGENT = "eu-ai-act-scanner-regulatory-monitor/1.0"

SOURCES = [
    {
        "id": "eu-ai-act-consolidated",
        "kind": "LEGAL_TEXT",
        "title": "Regulation (EU) 2024/1689 — Artificial Intelligence Act",
        # EUR-Lex serves this CELEX record with HTTP 202 to unattended clients;
        # the Publications Office resource is the same official legal record
        # and exposes a stable machine-readable representation.
        "url": "https://publications.europa.eu/resource/celex/32024R1689",
    },
    {
        "id": "eu-ai-act-commission-framework",
        "kind": "IMPLEMENTATION_INFORMATION",
        "title": "European Commission — Regulatory framework for AI",
        "url": "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai",
    },
]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalized_text(blob: bytes) -> str:
    text = blob.decode("utf-8", "replace")
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def fetch_source(source: dict) -> dict:
    request = urllib.request.Request(source["url"], headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            blob = response.read()
            status = response.status
            final_url = response.geturl()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"{source['id']} unavailable: {exc}") from exc

    normalized = _normalized_text(blob)
    if not normalized:
        raise RuntimeError(f"{source['id']} returned no usable text")
    return {
        **source,
        "http_status": status,
        "final_url": final_url,
        "bytes": len(blob),
        "content_hash": hashlib.sha256(normalized.encode("utf-8")).hexdigest(),
    }


def load_previous() -> dict:
    if not STATE_PATH.exists():
        return {"schema_version": "1.0", "sources": []}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def main() -> int:
    try:
        previous = load_previous()
        old_by_id = {item["id"]: item for item in previous.get("sources", [])}
        current = []
        changes = []
        checked_at = _now()

        for source in SOURCES:
            fetched = fetch_source(source)
            old = old_by_id.get(source["id"])
            if old and old.get("content_hash") == fetched["content_hash"]:
                fetched["retrieved_at"] = old.get("retrieved_at", checked_at)
                fetched["review_status"] = old.get("review_status", "NONE")
            else:
                fetched["retrieved_at"] = checked_at
                fetched["review_status"] = "REVIEW_REQUIRED"
                changes.append({
                    "source_id": source["id"],
                    "kind": source["kind"],
                    "source": source["url"],
                    "previous_hash": old.get("content_hash") if old else None,
                    "current_hash": fetched["content_hash"],
                    "retrieved_at": checked_at,
                    "review_status": "REVIEW_REQUIRED",
                })
            current.append(fetched)

        state = {
            "schema_version": "1.0",
            "checked_at": previous.get("checked_at", checked_at),
            "source_of_truth": "official EU sources only; monitoring does not change compliance logic",
            "sources": current,
        }

        if changes:
            state["checked_at"] = checked_at
            STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
            STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            with HISTORY_PATH.open("a", encoding="utf-8") as history:
                for change in changes:
                    history.write(json.dumps(change, sort_keys=True) + "\n")
            print(f"{len(changes)} source change(s) detected; REVIEW_REQUIRED recorded.")
        else:
            print("NO_CHANGE: official source hashes match the last valid state.")
        return 0
    except (OSError, ValueError, RuntimeError, urllib.error.HTTPError) as exc:
        print(f"FAILURE: {exc}", file=sys.stderr)
        print("Last valid regulatory state was preserved; the next scheduled run will retry.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
