# LLM Wiki Maintain Skill

This skill is for running maintenance checks and keeping the core system healthy.

Maintenance actions include:

- running `python3 scripts/wiki_tool.py doctor`
- running `python3 scripts/wiki_tool.py build`
- running `python3 scripts/wiki_tool.py lint`
- running `python3 scripts/wiki_tool.py source-lint`
- running `python3 scripts/audit_public.py`

After source ingestion, also run:

- `python3 scripts/wiki_tool.py source-scan --update --accept-covered`
- `python3 scripts/wiki_tool.py source-lint`
