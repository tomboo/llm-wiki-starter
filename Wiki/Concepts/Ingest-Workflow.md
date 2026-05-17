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

# Ingest Workflow

Key steps for transforming new Raw files into the Wiki:

1. Detect new Raw files (e.g., `scripts/wiki_tool.py source-scan`).
2. Create focused notes using templates (`_templates/`), adding `sources:` and `source_count`.
3. Rebuild catalog/index (`scripts/wiki_tool.py build`) and validate with lint/source-lint.
4. Record the operation in a log note for traceability.

Keep Raw content intact and ground all claims in explicit sources.
