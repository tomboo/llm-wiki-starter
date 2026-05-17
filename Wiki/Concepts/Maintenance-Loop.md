---
tags:
  - "concept"
topics: ["LLM Wiki"]
status: seed
created: 2026-05-17
updated: 2026-05-17
sources:
  - "Raw/Sources/How To Build LLM Wiki In Obsidian? 🧠 A Memory Layer For Any Agentic AI.md"
source_count: 1
aliases: []

---

# Maintenance Loop

Routine operations to keep the wiki healthy:

- `doctor`: verify folders and environment.
- `build`: regenerate catalog and indexes.
- `lint`/`source-lint`: validate frontmatter, tags, and source coverage.
- `audit_public.py`: run audit checks for public exposures.
- `source-scan --update --accept-covered`: update manifest based on coverage.

Run these regularly (daily/weekly) depending on ingestion frequency.
