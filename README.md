# N.H

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

Review the [proposal list and scoped decision status](https://github.com/nesgeva/NH-GOVERNANCE/issues/3) separately, outside the default LLM input. Accepted behavior belongs in the domain documents. Unreviewed rows remain proposals.

## LLM input

Provide these files together.

Count every project file, including tools and filename labels, with both token encodings:

```bash
python3 tools/check_project.py
```

Export the exact counted input outside this project:

```bash
python3 tools/check_project.py --bundle /tmp/NH-LLM.md
```

Install [tools/requirements.txt](tools/requirements.txt) outside the project. The checker covers two encodings, not every model's tokenizer. Leave room for the task and reply.

Use [PROVENANCE.md](PROVENANCE.md) for historical or exact-contract sources, outside the default prompt.

## Preparing implementation with a coding agent

Ask the coding agent to read AGENTS.md and all listed documents. OPERATIONS.md owns the build draft, DECISIONS.md the gaps, and PROVENANCE.md historical contracts. The draft grants no implementation permission.

Suggested first request:

> Read AGENTS.md and all documents in the README table. Review the build plan draft in OPERATIONS.md against the domain rules. Report the first milestone's remaining decisions, required source artifacts, component contracts and acceptance checks. Do not change runtime code, adopt proposals, select models or activate services. This checkout does not establish the state of external implementation code.

After scope approval and implementation authorization, inspect supplied code before choosing reuse/replacement. Track progress through Git and existing owners. Runtime commands remain unverified until that inspection.
