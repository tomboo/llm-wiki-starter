# LLM Wiki Ingest Skill

This skill is for compiling Raw sources into Wiki notes.

When ingesting new sources:

- Search `Wiki/catalog.jsonl` before opening broad source context.
- Preserve raw source text in `Raw/Sources/` and do not edit it without good reason.
- Create or update notes in `Wiki/` that are concise, factual, and linked to sources.
- Add source file paths to `sources:` and keep `source_count` accurate.
- Avoid broad generalization; keep notes focused and directly grounded in the source.
