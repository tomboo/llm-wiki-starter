## Todo

- Automation to run full maintenance loop periodically
- Automation: run a heartbeat that checks for new Raw files (e.g., every 10 minutes) and, when found, runs the full ingest + maintenance loop (ingest → build catalog/index → lint → source-scan/audit).
- How To Build LLM Wiki In Obsidian? 🧠 A Memory Layer For Any Agentic AI
  - 27:04 Part 2: Advanced Features  
  - 27:40 Advanced Feature 1: Obsidian Firewall  
  - 29:39 Advanced Feature 2: Local Model Setup  
  - 31:03 Local Model Launcher Buttons  
  - 31:27 Testing The Local Model  
  - 32:37 Other Advanced Options  
  - Checking repo status so the next recommendation matches the current branch state.

## What to work on next

### 1. Clean up local state first
- You have local changes in workspace.json and todo.md.md.
- Decide whether to keep them, discard them, or add notes / .obsidian to your .gitignore if they are personal scratch files.

### 2. Highest-value next work
- Automate raw-source ingestion more fully:
  - create a script or agent skill that detects new `Raw/Sources/*` files and creates Wiki notes automatically.
  - add a heartbeat or watcher workflow that runs the full ingest → build → lint loop.

### 3. Strengthen the repo tooling
- Implement the currently stubbed `source-delta` and `source-coverage` commands in wiki_tool.py.
- Add a small README or command-reference.md expansion explaining the maintenance/query/ingest workflow.

### 4. Expand the Wiki
- Add more granular `Entities` and `Projects` from the new source material.
- Link the new concept notes to each other with `[[wikilinks]]` so the graph is more connected.

If you want, I can also make one of these concrete:
- add .gitignore entries for .obsidian and notes
- implement `source-coverage` in wiki_tool.py
- create a heartbeat automation example script