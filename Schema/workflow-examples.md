# Workflow Examples

## Ingest workflow

1. Add cleaned Markdown source to `Raw/Sources/`.
2. Search the catalog with `python3 scripts/wiki_tool.py search-catalog --query "..."`.
3. Open the most relevant Wiki notes.
4. Create or update focused notes in `Wiki/`.
5. Add raw source links to `sources:` and keep `source_count` accurate.
6. Run:

```bash
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```

## Query workflow

1. Start from `Wiki/index.md`.
2. Search `Wiki/catalog.jsonl` before reading Raw sources.
3. Open the most relevant compiled Wiki notes.
4. Open Raw sources only when needed for evidence or verification.
5. Cite both the compiled note and Raw source when using source material.
