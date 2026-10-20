# N.H

Local personal memory, contextual interpretation, conversation, and explicit simulation. Ness owns decisions. N.H preserves sources and adds revisable readings.

| Read | Contains |
|---|---|
| [SYSTEM.md](SYSTEM.md) | Purpose, owners, main path, models, build status |
| [MEMORY.md](MEMORY.md) | Intake, records, reading, retrieval, stories, people, state, connections |
| [SECURITY.md](SECURITY.md) | Privacy, access, biometrics, caches, delivery, actions, maintenance |
| [EXPERIENCE.md](EXPERIENCE.md) | Conversation, World/Wonder, speech, mobile, learning, future intentions |
| [OPERATIONS.md](OPERATIONS.md) | Shared commitment/recovery rules, queue, evaluation, coordination, research |
| [DECISIONS.md](DECISIONS.md) | Authority, real gaps, conflicts, implementation boundaries |
| [AGENTS.md](AGENTS.md) | Editing rules and token budget |
| [PROVENANCE.md](PROVENANCE.md) | Original-source location and consolidation scope |

## LLM input

Provide these files together. They define the current project without claiming runtime implementation or authorizing building it.

Count every project file, including tools and filename labels, with both token encodings:

```bash
python3 tools/check_project.py
```

Export the exact counted input outside this project:

```bash
python3 tools/check_project.py --bundle /tmp/NH-LLM.md
```

Install [tools/requirements.txt](tools/requirements.txt) in an external Python environment. The check fails at 20,000 tokens. Different models use different tokenizers; these counts cover `cl100k_base` and `o200k_base`, not every model. Leave room for the task and reply.

Full originals are preserved in the sibling archive documented in [PROVENANCE.md](PROVENANCE.md). Use them for historical or exact-contract questions, not as the default prompt.
