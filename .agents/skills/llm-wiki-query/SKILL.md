# LLM Wiki Query Skill

This skill is for finding answers in the compiled Wiki before using raw sources.

When querying:

- Start with `Wiki/index.md` and `Wiki/catalog.jsonl`.
- Search the catalog for the user query before opening Raw sources.
- Prefer existing Wiki notes that already summarize relevant knowledge.
- Only open Raw sources when the compiled Wiki note is insufficient or verification is required.
- Cite both the compiled note and Raw source when the answer depends on source material.
