# Agent Guidance for LLM Wiki

This folder is a core LLM Wiki. Follow these rules when editing, compiling, or querying content.

## Primary rules

- Treat `Raw/Sources/` as source material only. Do not write reusable knowledge there.
- Write compiled, reusable knowledge only under `Wiki/`.
- Keep every compiled Wiki note linked to one or more files in `Raw/Sources/`.
- Search `Wiki/catalog.jsonl` before opening broad Raw context.
- If a relevant Wiki note already exists, prefer updating it and preserving source links.
- Do not invent citations or unsupported claims.
- Run `build`, `lint`, and source checks before committing.

## Where to write what

- `Raw/Sources/`: original source notes, raw captures, reference material.
- `Wiki/Concepts/`: concise knowledge notes about ideas and concepts.
- `Wiki/Topics/`: topic-driven, structured overview notes.
- `Wiki/Entities/`: notes about people, organizations, tools, or objects.
- `Wiki/Projects/`: actionable plans, workflows, or project summaries.
- `Wiki/Logs/`: audit entries and maintenance notes.

## Note integrity

- Compiled Wiki notes must include `sources:` and an accurate `source_count`.
- Source notes must include metadata fields: `Title`, `Reference`, `Created`, `Processed`, and `tags`.
- Do not mark a source as processed unless it is covered by at least one compiled Wiki note.

## Maintenance gate

Before every meaningful commit run:

```bash
python3 scripts/wiki_tool.py doctor
python3 scripts/wiki_tool.py build
python3 scripts/wiki_tool.py lint
python3 scripts/wiki_tool.py source-lint
python3 scripts/audit_public.py
```

After editing sources, also run:

```bash
python3 scripts/wiki_tool.py source-scan --update --accept-covered
python3 scripts/wiki_tool.py source-lint
```
