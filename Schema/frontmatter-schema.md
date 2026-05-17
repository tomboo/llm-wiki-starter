# Frontmatter Schema

Compiled Wiki notes should use this YAML schema:

```yaml
---
tags:
  - "concept"
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
---
```

Source notes should use this YAML schema:

```yaml
---
Title: ""
Author: ""
Reference: ""
ContentType:
  - "markdown"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
---
```

Allowed compiled note tags:

- topic
- concept
- entity
- project
- log
