# Command Reference for scripts/wiki_tool.py

- `doctor`: run non-mutating health checks for required folders and Python version.
- `build`: generate `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder index files.
- `lint`: validate compiled Wiki note frontmatter and `source_count`.
- `source-scan [--update] [--accept-covered]`: list Raw sources and optionally update `Schema/source-manifest.jsonl`.
- `source-lint`: validate source manifest and coverage.
- `search-catalog --query "text"`: search compiled Wiki notes via `Wiki/catalog.jsonl`.
- `log --title "t" --details "d"`: append a log entry to `Wiki/log.md`.
