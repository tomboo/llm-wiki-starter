# LLM Wiki Lint Skill

This skill is for validating note structure, source links, and metadata.

Lint behavior should include:

- validating compiled Wiki note frontmatter and allowed tags
- checking `sources:` links exist under `Raw/Sources/`
- verifying `source_count` matches the number of linked sources
- validating Raw source frontmatter includes `Title`, `Reference`, `Created`, `Processed`, and `tags`
- failing if a source is marked processed but has no Wiki coverage
