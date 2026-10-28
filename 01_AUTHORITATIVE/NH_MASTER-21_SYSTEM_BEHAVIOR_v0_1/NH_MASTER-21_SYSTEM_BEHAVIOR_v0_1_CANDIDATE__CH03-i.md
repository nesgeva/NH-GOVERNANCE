# Chapter 3-i — Group A: C-ENGINE-AB

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-i.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers the A/B engine boundary: bare and positional-context reading, quarantine output, the two gold-run entry points, benchmark protection, operation provenance, and the accepted no-surroundings rule. The twelve-field schema, including `story_layer`, belongs to C-READ.1 — Twelve-field reading representation v1 in CH03-b; the full reading writer is also there. Telling persistence and per-reading promotion are in CH03-c and CH03-d. The gold-set contents and scoring rules belong to CH03-l, the remaining evaluation bridge to CH03-m and CH03-n, and the general model layer to CH10-b. Recordkeeping and policy requirements retain their own design status alongside the built engine operations.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`. Authority order: V10 → Decision Defaults S19 v2_2 → cursorrules → Companion v1; the Map is subordinate.

<!-- BEGIN BEHAVIOR -->

### C-ENGINE-AB — Engines A & B (§7C, §16)
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Engine B rows] [V10 §5 / Accretive store + tooling] [V10 §7C]

ALONE
- What it is: BUILT — The two reading engines `nh_engine_minimal.py` and `nh_engine_b.py`: A reads the bare root; B adds preceding turns from the same thread. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Takes in: BUILT — A target root identified by `root_id`; B also receives the full content of up to three roots immediately preceding it in the same `source_title` thread. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Does: BUILT — A sends the bare root to the mouth; B frames the positional context as BACKGROUND. Each produces a twelve-field reading through its reading entry point and writes test output to quarantine. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Engine B rows] [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — Readings in `.nh_readings_quarantine.jsonl`; `run_on_gold()` evaluates A against the eight v1 cases and B against the seven v2-B cases. [V10 §5 / Accretive store + tooling] [V10 §6]
- Must never: DESIGNED — Write engine test output to production, invent meaning, or change benchmark-affecting behavior without Ness's authorization and a rerun of both sealed gold sets. [V10 §6A / PROTECTED FILES AND STORES] [V10 §7C] [MAP C-ENGINE-AB]
- Fails closed by: DESIGNED — When context is insufficient, produce an honest insufficient-context reading marked revisable. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] [DD §3D. Gold standards]

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.1 — Engine A: provides the bare-root reading route. [V10 §7C]
- Fed by: BUILT — C-ENGINE-AB.2 — Engine B: provides the positional-context reading route. [V10 §7C]
- Fed by: DESIGNED — C-ENGINE-AB.3 — MOUTH_MODEL: supplies the configured test-mouth value for both engines. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-ENGINE-AB.4 — Quarantine-only engine output: provides the separate destination for engine test readings. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]
- Fed by: DESIGNED — C-ENGINE-AB.6 — Engine operation records: supplies the required connected provenance and comparability records. [MAP C-ENGINE-AB]
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the target root and B's preceding roots from the same thread. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Fed by: BUILT — C-GOLD — Sealed gold sets v1, v2-B (§7C): supplies the eight bare-root cases and seven context-requiring cases to the respective gold-run entry points. [V10 §5 / Accretive store + tooling] [V10 §6]
- Fed by: DESIGNED — C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A): the worker is an upstream user in the designed live reading path. [MAP C-ENGINE-AB]
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: Ness's authorization and rerunning both sealed gold sets are required before adopting a benchmark-affecting change. [V10 §6A / PROTECTED FILES AND STORES]
- Gated by: BUILT — C-READ — Reading record, validator, writer (§6B): reading shape, referenced-root existence and committed idempotency keys are checked at the shared write boundary. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator and writer rows]
- Gated by: ACCEPTED — C-ENGINE-AB.7 — Reading without surrounding context: when surroundings are unavailable, preserve the reason and use only what the target supports. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Gated by: DESIGNED — C-ENGINE-AB.8 — Insufficient-context outcome: insufficient context requires an honest reading marked revisable. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row]
- Gated by: DESIGNED — C-ENGINE-AB.9 — Wider-thread reading boundary: wider-thread capability remains a future goal until benchmarked. [V10 §7C]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: receives A/B test readings; production remains a separate destination. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] [V10 §5 / Physical stores on disk]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-READ — Reading record, validator, writer (§6B) | A reading to preserve beside its source roots. | Supplies the A/B engine reading to the validated write boundary. | A separate quarantine reading; source roots remain intact. | [V10 §5 / Accretive store + tooling] [V10 §6B / READING record schema] |
| 2 · BUILT | C-READ.4 — Quarantine readings destination | Validated engine A and engine B gold-run readings through the reading writer. | Supplies validated engine A and engine B gold-run readings. | Nothing in this card. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE] [V10 §6B / ON DISK NOW] |

SUB-PARTS: C-ENGINE-AB.1 — Engine A; C-ENGINE-AB.2 — Engine B; C-ENGINE-AB.3 — MOUTH_MODEL; C-ENGINE-AB.4 — Quarantine-only engine output; C-ENGINE-AB.5 — Benchmark protection; C-ENGINE-AB.6 — Engine operation records; C-ENGINE-AB.7 — Reading without surrounding context; C-ENGINE-AB.8 — Insufficient-context outcome; C-ENGINE-AB.9 — Wider-thread reading boundary

### C-ENGINE-AB.1 — Engine A
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] [V10 §7C]

ALONE
- What it is: BUILT — The bare-root engine in `nh_engine_minimal.py`. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — One root, without surrounding context or story-layer reading. [V10 §7C]
- Does: BUILT — Sends the root to the mouth with the instruction to read what its speaker is doing, then produces a twelve-field reading in quarantine. [V10 §7C]
- Gives out: BUILT — A bare reading; the recorded gold-v1 result is approximately 5–6 out of eight cases. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] [V10 §7C]
- Must never: DESIGNED — Answer the root as a conversation, describe instead of reading the speaker's act, or invent meaning. [V10 §7C]
- Fails closed by: DESIGNED — Insufficient context yields an honest, revisable reading rather than invented missing meaning. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row]

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.1.1 — read_root(root_id): provides A's root-reading entry point. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-ENGINE-AB.1.2 — Bare-root reading instruction: supplies the speaker-act reading instruction. [V10 §7C]
- Fed by: BUILT — C-ENGINE-AB.1.3 — Engine A run_on_gold(): provides A's eight-case gold run. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the single target root. [V10 §7C]
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: changes to the engine's benchmark-affecting behavior require authorization and both gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: stores the resulting test reading. [V10 §5 / Accretive store + tooling]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | One root, without surrounding context or story-layer reading. | provides the bare-root reading route. | A bare reading; the recorded gold-v1 result is approximately 5–6 out of eight cases. | [V10 §7C] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] |
| 2 · BUILT | C-ENGINE-AB.4 — Quarantine-only engine output | One root, without surrounding context or story-layer reading. | supplies bare-root test readings. | A bare reading; the recorded gold-v1 result is approximately 5–6 out of eight cases. | [V10 §5 / Accretive store + tooling] [V10 §7C] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A row] |

SUB-PARTS: C-ENGINE-AB.1.1 — read_root(root_id); C-ENGINE-AB.1.2 — Bare-root reading instruction; C-ENGINE-AB.1.3 — Engine A run_on_gold()

### C-ENGINE-AB.1.1 — read_root(root_id)
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — Engine A's root-reading entry point. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — `root_id`, identifying the root to read. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Passes that root through the mouth and forms the twelve-field reading. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — The reading written to quarantine. [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Send engine test output into the production readings store. [MAP C-ENGINE-AB]
- Fails closed by: BUILT — The shared reading validator rejects a malformed output before append; uncertain readings remain valid. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6B / READING record schema]

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the root selected by `root_id`. [V10 §5 / Accretive store + tooling]
- Gated by: BUILT — C-READ.2 — _validate_reading: the resulting reading must pass the shared shape check before append. [V10 §6B / READING record schema]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: receives this entry point's reading. [V10 §5 / Accretive store + tooling]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.1 — Engine A | `root_id`, identifying the root to read. | provides A's root-reading entry point. | The reading written to quarantine. | [V10 §5 / Accretive store + tooling] |
| 2 · BUILT | C-ENGINE-AB.1.2 — Bare-root reading instruction | `root_id`, identifying the root to read. | supplies the target root for the mouth instruction. | The reading written to quarantine. | [V10 §5 / Accretive store + tooling] [V10 §7C] |

SUB-PARTS: NONE

### C-ENGINE-AB.1.2 — Bare-root reading instruction
Stamp: BUILT    Source: [V10 §7C]

ALONE
- What it is: BUILT — The instruction A sends with a bare root: “say what the {role} is doing, don't describe/answer/invent”. [V10 §7C]
- Takes in: BUILT — The root content and its carried speaker `role`. [V10 §7C]
- Does: BUILT — Directs the mouth to read the speaker's act in the root. [V10 §7C]
- Gives out: BUILT — Meaning and role reading without context or story-layer reading. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, The engine (2c) row] [V10 §7C]
- Must never: DESIGNED — Describe, answer, or invent instead of reading what the speaker is doing. [V10 §7C]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.1.1 — read_root(root_id): supplies the target root for the mouth instruction. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.1 — Engine A | The root content and its carried speaker `role`. | supplies the speaker-act reading instruction. | Meaning and role reading without context or story-layer reading. | [V10 §7C] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, The engine (2c) row] |

SUB-PARTS: NONE

### C-ENGINE-AB.1.3 — Engine A run_on_gold()
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — A's entry point for running the v1 gold cases. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — The eight bare-root cases of gold v1. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Runs Engine A on those eight cases. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — Quarantine test readings; the recorded result is approximately 5–6/8. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Quarantine readings store rows]
- Must never: DESIGNED — Change a sealed gold case or let the model decide pass/fail. [MAP C-GOLD]
- Fails closed by: BUILT — Malformed gold-run readings are rejected by the shared shape validator; uncertainty is not a rejection reason. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6B / READING record schema]

TOGETHER
- Fed by: BUILT — C-GOLD — Sealed gold sets v1, v2-B (§7C): provides the sealed v1 cases. [V10 §5 / Accretive store + tooling]
- Gated by: BUILT — C-READ.2 — _validate_reading: gold-run output passes the shared shape check before append. [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: changes to `run_on_gold` or gold-set handling require authorization and both gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: receives A's gold-run output. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.1 — Engine A | The eight bare-root cases of gold v1. | provides A's eight-case gold run. | Quarantine test readings; the recorded result is approximately 5–6/8. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Minimal engine A and Quarantine readings store rows] |

SUB-PARTS: NONE

### C-ENGINE-AB.2 — Engine B
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §7C]

ALONE
- What it is: BUILT — The positional-context engine in `nh_engine_b.py`. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — A target root and up to three immediately preceding roots in the same `source_title` thread, with their full content. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Does: BUILT — Obtains preceding turns, places them inside BACKGROUND/END BACKGROUND framing, invokes the mouth, and produces a twelve-field reading in quarantine. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §5 / Accretive store + tooling] [V10 §7C]
- Gives out: BUILT — Context-assisted test readings; the recorded tested setup scored 6.5/7 on gold v2-B. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row]
- Must never: DESIGNED — Replace positional preceding-turn retrieval with semantic search or truncate the supplied turns. [DD §3E. Engine design decisions]
- Fails closed by: DESIGNED — Context insufficiency is represented honestly in a revisable reading. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row]

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.2.1 — read_root_b(root_id): provides B's target-root entry point. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-ENGINE-AB.2.2 — _get_preceding_turns(n=3): supplies the same-thread preceding roots. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing: supplies the target/background separation. [V10 §7C]
- Fed by: BUILT — C-ENGINE-AB.2.4 — Engine B run_on_gold(): provides B's seven-case gold run. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies target and same-thread preceding roots. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: benchmark-affecting changes require Ness's authorization and both gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: receives the positional-context test reading. [V10 §5 / Accretive store + tooling]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | A target root and up to three immediately preceding roots in the same `source_title` thread, with their full content. | provides the positional-context reading route. | Context-assisted test readings; the recorded tested setup scored 6.5/7 on gold v2-B. | [V10 §7C] [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] |
| 2 · BUILT | C-ENGINE-AB.4 — Quarantine-only engine output | A target root and up to three immediately preceding roots in the same `source_title` thread, with their full content. | supplies positional-context test readings. | Context-assisted test readings; the recorded tested setup scored 6.5/7 on gold v2-B. | [V10 §5 / Accretive store + tooling] [V10 §7C] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] |

SUB-PARTS: C-ENGINE-AB.2.1 — read_root_b(root_id); C-ENGINE-AB.2.2 — _get_preceding_turns(n=3); C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing; C-ENGINE-AB.2.4 — Engine B run_on_gold()

### C-ENGINE-AB.2.1 — read_root_b(root_id)
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — Engine B's root-reading entry point. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — `root_id`, identifying the target for positional-context reading. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Calls `_get_preceding_turns(n=3)`, supplies BACKGROUND-framed context to the mouth, and forms the twelve-field reading. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — A reading written to quarantine. [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Write engine test output to production. [MAP C-ENGINE-AB]
- Fails closed by: BUILT — The shared reading validator rejects malformed output before append without rejecting uncertainty. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6B / READING record schema]

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.2.2 — _get_preceding_turns(n=3): returns the preceding turns for the target. [V10 §5 / Accretive store + tooling]
- Gated by: BUILT — C-READ.2 — _validate_reading: the resulting reading must satisfy the shared shape check before append. [V10 §6B / READING record schema]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: receives B's entry-point output. [V10 §5 / Accretive store + tooling]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2 — Engine B | `root_id`, identifying the target for positional-context reading. | provides B's target-root entry point. | A reading written to quarantine. | [V10 §5 / Accretive store + tooling] |

SUB-PARTS: NONE

### C-ENGINE-AB.2.2 — _get_preceding_turns(n=3)
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling] [V10 §7C]

ALONE
- What it is: BUILT — Engine B's position-based preceding-turn retrieval function. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — The target root's position and `source_title` grouping, with `n=3`. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Does: BUILT — Selects up to three roots immediately before the target in the same thread and returns their complete content. [V10 §7C]
- Gives out: BUILT — Positional preceding turns, without truncation. [V10 §7C]
- Must never: DESIGNED — Substitute semantic similarity for position or shorten the retrieved content. [DD §3E. Engine design decisions]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.2.2.1 — n: supplies the count bound of three. [V10 §7C]
- Fed by: BUILT — C-ENGINE-AB.2.2.2 — source_title grouping: supplies the target's same-thread restriction. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): supplies the roots from which preceding same-thread turns are selected. [V10 §5 / Accretive store + tooling]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2 — Engine B | The target root's position and `source_title` grouping, with `n=3`. | supplies the same-thread preceding roots. | Positional preceding turns, without truncation. | [V10 §5 / Accretive store + tooling] [V10 §7C] |
| 2 · BUILT | C-ENGINE-AB.2.1 — read_root_b(root_id) | The target root's position and `source_title` grouping, with `n=3`. | returns the preceding turns for the target. | Positional preceding turns, without truncation. | [V10 §5 / Accretive store + tooling] [V10 §7C] |
| 3 · BUILT | C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing | The target root's position and `source_title` grouping, with `n=3`. | supplies full positional context for the background section. | Positional preceding turns, without truncation. | [V10 §5 / Accretive store + tooling] [V10 §7C] |

SUB-PARTS: C-ENGINE-AB.2.2.1 — n; C-ENGINE-AB.2.2.2 — source_title grouping

### C-ENGINE-AB.2.2.1 — n
Stamp: BUILT    Source: [V10 §7C]

ALONE
- What it is: BUILT — The preceding-turn count parameter in Engine B's `_get_preceding_turns(n=3)`. [V10 §7C]
- Takes in: BUILT — The configured value `3`. [V10 §7C]
- Does: BUILT — Limits this built experiment to up to three immediately preceding same-thread roots. [V10 §7C]
- Gives out: BUILT — The count bound used by Engine B's positional retrieval. [V10 §7C]
- Must never: DESIGNED — Treat Engine B's value of three as the universal positional limit for future reading modes. [V10 §7F]
- Fails closed by: DESIGNED — The value of three stays Engine B's own bound and is never applied as the universal positional limit for future reading modes. [V10 §7C] [V10 §7F]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: changing the context-window behavior or `_get_preceding_turns` requires authorization and both sealed gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | The configured value `3`. | supplies the count bound of three. | The count bound used by Engine B's positional retrieval. | [V10 §7C] |

SUB-PARTS: NONE

### C-ENGINE-AB.2.2.2 — source_title grouping
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — The `source_title` equality used to keep Engine B's preceding-turn context within the target's thread. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — The target and candidate preceding roots' `source_title` values. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Restricts positional context to preceding roots in that same grouping. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — Same-thread membership for positional retrieval. [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Use semantic search as a replacement for the position-based, same-thread strategy. [DD §3E. Engine design decisions]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-STORE — Accretive store & sealed roots (§6B): carries the `source_title` values with each stored root. [V10 §5 / Accretive store + tooling] [V10 §6B]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | The target and candidate preceding roots' `source_title` values. | supplies the target's same-thread restriction. | Same-thread membership for positional retrieval. | [V10 §5 / Accretive store + tooling] |

SUB-PARTS: NONE

### C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing
Stamp: BUILT    Source: [V10 §7C]

ALONE
- What it is: BUILT — The prompt boundary that distinguishes Engine B's preceding turns from the target being read. [V10 §7C]
- Takes in: BUILT — Complete preceding-turn content and the target root. [V10 §7C]
- Does: BUILT — Places the preceding turns inside BACKGROUND/END BACKGROUND framing so the mouth reads the target rather than answering the conversation. [V10 §7C] [V10 §11 item 20 / ENGINE B BUILD LESSONS]
- Does: DESIGNED — For a short confirmation, says what the speaker is confirming. [DD §3E. Engine design decisions]
- Gives out: BUILT — The context-framed prompt used by Engine B. [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Reference the background in the output, quote or paraphrase it, invent meaning, or answer or continue the conversation instead of reading. [DD §3E. Engine design decisions]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.2.2 — _get_preceding_turns(n=3): supplies full positional context for the background section. [V10 §5 / Accretive store + tooling] [V10 §7C]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2 — Engine B | Complete preceding-turn content and the target root. | supplies the target/background separation. | The context-framed prompt used by Engine B. | [V10 §7C] [V10 §5 / Accretive store + tooling] |

SUB-PARTS: NONE

### C-ENGINE-AB.2.4 — Engine B run_on_gold()
Stamp: BUILT    Source: [V10 §5 / Accretive store + tooling]

ALONE
- What it is: BUILT — B's entry point for running gold v2-B. [V10 §5 / Accretive store + tooling]
- Takes in: BUILT — The seven context-requiring cases of gold v2-B. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Runs the positional-context engine on those cases. [V10 §5 / Accretive store + tooling]
- Gives out: BUILT — Quarantine test readings; the recorded tested setup scored 6.5/7. The remaining miss's cause is not isolated among model capability, prompt framing, context format and run variance. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §7C]
- Must never: DESIGNED — Alter sealed gold cases, let the model judge pass/fail, or treat 7/7 as a promised result. [MAP C-GOLD] [V10 §11 item 20]
- Fails closed by: BUILT — The shared validator rejects malformed gold-run output before append and permits uncertain readings. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6B / READING record schema]

TOGETHER
- Fed by: BUILT — C-GOLD — Sealed gold sets v1, v2-B (§7C): provides the seven sealed v2-B cases. [V10 §5 / Accretive store + tooling]
- Gated by: BUILT — C-READ.2 — _validate_reading: the gold-run reading must pass shape validation before append. [V10 §6B / READING record schema]
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: changes to this run or gold-set handling require authorization and both gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: holds B's gold-run output. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB.2 — Engine B | The seven context-requiring cases of gold v2-B. | provides B's seven-case gold run. | Quarantine test readings; the recorded tested setup scored 6.5/7. The remaining miss's cause is not isolated among model capability, prompt framing, context format and run variance. | [V10 §5 / Accretive store + tooling] [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine B row] [V10 §7C] |

SUB-PARTS: NONE

### C-ENGINE-AB.3 — MOUTH_MODEL
Stamp: DESIGNED    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Mouth model choice row] [V10 §5 / Accretive store + tooling]

ALONE
- What it is: DESIGNED — The model-selection constant in both A/B engine files. [V10 §5 / Accretive store + tooling]
- Takes in: DESIGNED — `dolphin-llama3`, the recorded current test-model value. [V10 §5 / Accretive store + tooling]
- Does: DESIGNED — Selects the mouth used by each built engine. [V10 §5 / Accretive store + tooling]
- Gives out: DESIGNED — Engine proposals from that test mouth. [V10 §5 / Accretive store + tooling]
- Must never: DESIGNED — Treat the current test model as the final adopted Interactive Translator, or replace it without authorization and testing against both sealed gold sets. [V10 §6A / PROTECTED FILES AND STORES] [V10 §16]
- Fails closed by: DESIGNED — The current test model is not adopted as the final Interactive Translator, and no replacement is made without authorization and testing against both sealed gold sets. [V10 §5 / Accretive store + tooling] [V10 §6A / PROTECTED FILES AND STORES] [V10 §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-ENGINE-AB.5 — Benchmark protection: changing `MOUTH_MODEL` requires Ness's authorization and both sealed gold reruns. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB — Engines A & B (§7C, §16) | `dolphin-llama3`, the recorded current test-model value. | supplies the configured test-mouth value for both engines. | Engine proposals from that test mouth. | [V10 §5 / Accretive store + tooling] |

SUB-PARTS: NONE

### C-ENGINE-AB.4 — Quarantine-only engine output
Stamp: BUILT    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]

ALONE
- What it is: BUILT — The A/B test-output destination `.nh_readings_quarantine.jsonl`, separate from production. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]
- Takes in: BUILT — The engines' twelve-field readings, including their gold-run output. [V10 §5 / Accretive store + tooling]
- Does: BUILT — Stores those readings in the quarantine sibling. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row]
- Gives out: BUILT — Preserved test readings outside `.nh_readings_store.jsonl`. [V10 §5 / Physical stores on disk]
- Must never: DESIGNED — Write engine test or gold-run output directly to production. [MAP C-ENGINE-AB]
- Fails closed by: BUILT — The shared shape validator rejects malformed readings before append; uncertainty alone is not rejected. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

TOGETHER
- Fed by: BUILT — C-ENGINE-AB.1 — Engine A: supplies bare-root test readings. [V10 §5 / Accretive store + tooling]
- Fed by: BUILT — C-ENGINE-AB.2 — Engine B: supplies positional-context test readings. [V10 §5 / Accretive store + tooling]
- Gated by: BUILT — C-READ.2 — _validate_reading: reading shape is checked before append; uncertainty is not a rejection reason. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Changes: BUILT — C-READ.4 — Quarantine readings destination: adds test readings through the reading write boundary. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] [V10 §5 / Accretive store + tooling]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · BUILT | C-ENGINE-AB — Engines A & B (§7C, §16) | The engines' twelve-field readings, including their gold-run output. | provides the separate destination for engine test readings. | Preserved test readings outside `.nh_readings_store.jsonl`. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] [V10 §5 / Accretive store + tooling] [V10 §5 / Physical stores on disk] |

SUB-PARTS: NONE

### C-ENGINE-AB.5 — Benchmark protection
Stamp: DESIGNED    Source: [V10 §6A / PROTECTED FILES AND STORES]

ALONE
- What it is: DESIGNED — The authorization and retesting boundary for changes that could affect the meaning or comparability of A/B benchmark results. [V10 §6A / PROTECTED FILES AND STORES]
- Takes in: DESIGNED — A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. [V10 §6A / PROTECTED FILES AND STORES]
- Does: DESIGNED — Requires Ness's authorization and a rerun of both sealed gold sets before the change is adopted. [V10 §6A / PROTECTED FILES AND STORES]
- Gives out: DESIGNED — The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. [V10 §6A / PROTECTED FILES AND STORES] [V10 §16]
- Must never: DESIGNED — Adopt a benchmark-affecting change without the required authorization and both gold reruns, or change `n=3`, BACKGROUND/END BACKGROUND framing or context truncation behavior without first understanding the B3 miss cause. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]
- Fails closed by: DESIGNED — Without Ness's authorization and both sealed gold-set reruns, the change is not adopted; a passing test alone never installs a replacement mouth. [V10 §6A / PROTECTED FILES AND STORES] [CR §7. PROTECTED FILES / LAYER 3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness's authorization is required before a benchmark-affecting change may be adopted. [V10 §6A / PROTECTED FILES AND STORES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB — Engines A & B (§7C, §16) | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | Ness's authorization and rerunning both sealed gold sets are required before adopting a benchmark-affecting change. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 2 · DESIGNED | C-ENGINE-AB.1 — Engine A | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | changes to the engine's benchmark-affecting behavior require authorization and both gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 3 · DESIGNED | C-ENGINE-AB.1.3 — Engine A run_on_gold() | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | changes to `run_on_gold` or gold-set handling require authorization and both gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 4 · DESIGNED | C-ENGINE-AB.2 — Engine B | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | benchmark-affecting changes require Ness's authorization and both gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 5 · DESIGNED | C-ENGINE-AB.2.2.1 — n | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | changing the context-window behavior or `_get_preceding_turns` requires authorization and both sealed gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 6 · DESIGNED | C-ENGINE-AB.2.4 — Engine B run_on_gold() | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | changes to this run or gold-set handling require authorization and both gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |
| 7 · DESIGNED | C-ENGINE-AB.3 — MOUTH_MODEL | A proposed change to `MOUTH_MODEL`, prompt text, context-window behavior, `_get_preceding_turns`, `run_on_gold`, output destination, gold-set handling, or any other benchmark-affecting behavior. | changing `MOUTH_MODEL` requires Ness's authorization and both sealed gold reruns. | The requirement for two-set benchmark comparability before adoption; test passing alone never installs or adopts a replacement mouth. | [V10 §6A / PROTECTED FILES AND STORES] [V10 §16] |

SUB-PARTS: NONE

### C-ENGINE-AB.6 — Engine operation records
Stamp: DESIGNED    Source: [V10 §0B] [MAP C-ENGINE-AB]

ALONE
- What it is: DESIGNED — Permanent, connected, append-only records of each gold run and each reading produced. [V10 §0B] [MAP C-ENGINE-AB]
- Takes in: DESIGNED — The actual engine operations, reading provenance and gold-run comparability metadata. [MAP C-ENGINE-AB]
- Does: DESIGNED — Records each gold run, each reading's model/digest/engine/prompt/config provenance, and the run's comparability metadata. [MAP C-ENGINE-AB]
- Gives out: DESIGNED — Traceable engine records that remain available as living memory under the access and authorization rules. [V10 §0B] [MAP C-ENGINE-AB]
- Must never: DESIGNED — Leave engine operations silent, destroy their records, treat a log as extra independent evidence, or create an automatic infinite log-about-log chain. [V10 §0B]
- Fails closed by: DESIGNED — A component without its traceable operation record is incomplete by design and is not adopted. [V10 §0B]

TOGETHER
- Fed by: DESIGNED — C-READ.1.9 — reading.produced_by: supplies the engine reading's required reproducibility-grade provenance, including origin, model, digest, engine_version, prompt_version, config and retrieval_inputs. [V10 §6B / READING record schema] [MAP C-ENGINE-AB]
- Fed by: DESIGNED — C-ENGINE-AB.6.1 — Run comparability metadata: supplies the metadata recorded for each run. [MAP C-ENGINE-AB]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): recording does not grant ordinary access to protected contents or override internal-use restrictions. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-AB]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): identity/security authorization remains applicable where required. [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-AB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB — Engines A & B (§7C, §16) | The actual engine operations, reading provenance and gold-run comparability metadata. | supplies the required connected provenance and comparability records. | Traceable engine records that remain available as living memory under the access and authorization rules. | [MAP C-ENGINE-AB] [V10 §0B] |

SUB-PARTS: C-ENGINE-AB.6.1 — Run comparability metadata

### C-ENGINE-AB.6.1 — Run comparability metadata
Stamp: DESIGNED    Source: [MAP C-ENGINE-AB]

ALONE
- What it is: DESIGNED — The metadata by which an engine run's benchmark comparability is recorded. [MAP C-ENGINE-AB]
- Takes in: DESIGNED — Comparability metadata for the actual run. [MAP C-ENGINE-AB]
- Does: DESIGNED — Records that metadata for each gold run. [MAP C-ENGINE-AB]
- Gives out: DESIGNED — A preserved comparability record associated with the run. [MAP C-ENGINE-AB]
- Must never: DESIGNED — Leave a gold run's required comparability metadata unrecorded. [MAP C-ENGINE-AB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB.6 — Engine operation records | Comparability metadata for the actual run. | supplies the metadata recorded for each run. | A preserved comparability record associated with the run. | [MAP C-ENGINE-AB] |

SUB-PARTS: NONE

### C-ENGINE-AB.7 — Reading without surrounding context
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]

ALONE
- What it is: ACCEPTED — The “Those Three To Become A One” reading rule when no surrounding context is available. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Takes in: ACCEPTED — The target Origin alone and the fact that no surroundings are available, with the reason. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Does: ACCEPTED — Records the absence of surroundings and why, runs the same reading process on the target alone, and uses only what that Origin supports. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Gives out: ACCEPTED — A context-limited, revisable reading; later context may produce a new reading beside the old one. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Must never: ACCEPTED — Invent missing meaning, replace the earlier reading, or rewrite it when later context becomes available. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Fails closed by: ACCEPTED — Limits the reading to support in the target and marks its context limitation instead of filling the missing surroundings. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — No surrounding context is available; only support in the target Origin may be used. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-ENGINE-AB — Engines A & B (§7C, §16) | The target Origin alone and the fact that no surroundings are available, with the reason. | when surroundings are unavailable, preserve the reason and use only what the target supports. | A context-limited, revisable reading; later context may produce a new reading beside the old one. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4] |
| 2 · ACCEPTED | C-ENGINE-AB.8 — Insufficient-context outcome | The target Origin alone and the fact that no surroundings are available, with the reason. | when surroundings are absent, use only the target's support and preserve the context limitation. | A context-limited, revisable reading; later context may produce a new reading beside the old one. | [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4] |

SUB-PARTS: NONE

### C-ENGINE-AB.8 — Insufficient-context outcome
Stamp: DESIGNED    Source: [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] [DD §3D. Gold standards]

ALONE
- What it is: DESIGNED — The engine's honest outcome when the available context does not support a fuller reading. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] [DD §3D. Gold standards]
- Takes in: DESIGNED — An insufficient-context reading situation. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row]
- Does: DESIGNED — Writes an honest insufficient-context reading and marks it revisable. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] [DD §3D. Gold standards]
- Gives out: DESIGNED — A revisable reading that preserves the insufficiency. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row]
- Must never: ACCEPTED — Invent the missing meaning or rewrite an earlier reading when more context becomes available. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Fails closed by: DESIGNED — Emits the honest context-limited outcome instead of claiming a supported fuller reading. [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] [DD §3D. Gold standards]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-ENGINE-AB.7 — Reading without surrounding context: when surroundings are absent, use only the target's support and preserve the context limitation. [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3.4]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB — Engines A & B (§7C, §16) | An insufficient-context reading situation. | insufficient context requires an honest reading marked revisable. | A revisable reading that preserves the insufficiency. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Engine failure-behavior row] |

SUB-PARTS: NONE

### C-ENGINE-AB.9 — Wider-thread reading boundary
Stamp: DESIGNED    Source: [V10 §7C] [V10 §16]

ALONE
- What it is: DESIGNED — The future full-thread reading goal beyond Engine B's built preceding-turn experiment. [V10 §7C] [V10 §16]
- Takes in: DESIGNED — A larger-model and larger-context-window candidate to be benchmarked. [V10 §7C]
- Does: DESIGNED — Requires benchmark testing before wider-thread reading is treated as working. [V10 §7C] [V10 §16]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Assume that a larger model, more VRAM, or a larger context window automatically establishes successful full-thread reading. [V10 §7C] [V10 §16]
- Fails closed by: DESIGNED — Until benchmark testing establishes it, wider-thread reading is not treated as working. [V10 §7C] [V10 §16]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Successful wider-thread behavior must be established by benchmarking; it is not an assumed consequence of the upgrade. [V10 §7C] [V10 §16]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-ENGINE-AB — Engines A & B (§7C, §16) | A larger-model and larger-context-window candidate to be benchmarked. | wider-thread capability remains a future goal until benchmarked. | NOT DECIDED | [V10 §7C] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece continuation entries

Both endpoints are named together; the earlier files remain unchanged.

| Using card | Defining or supplying card | Reciprocal entry | Source |
|---|---|---|---|
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the target root and B's preceding roots from the same thread. | [V10 §5 / Accretive store + tooling] [V10 §7C] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — USED BY continuation for Fed by: supplies the eight bare-root cases and seven context-requiring cases to the respective gold-run entry points. | [V10 §5 / Accretive store + tooling] [V10 §6] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-7GA — Live post-root reading path: queue, worker, recovery (§7G-A) | DESIGNED — USED BY continuation for Fed by: the worker is an upstream user in the designed live reading path. | [MAP C-ENGINE-AB] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-READ — Reading record, validator, writer (§6B) | BUILT — USED BY continuation for Gated by: reading shape, referenced-root existence and committed idempotency keys are checked at the shared write boundary. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator and writer rows] |
| C-ENGINE-AB — Engines A & B (§7C, §16) | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: receives A/B test readings; production remains a separate destination. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] [V10 §5 / Physical stores on disk] |
| C-ENGINE-AB.1 — Engine A | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the single target root. | [V10 §7C] |
| C-ENGINE-AB.1 — Engine A | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: stores the resulting test reading. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.1.1 — read_root(root_id) | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the root selected by `root_id`. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.1.1 — read_root(root_id) | C-READ.2 — _validate_reading | BUILT — USED BY continuation for Gated by: the resulting reading must pass the shared shape check before append. | [V10 §6B / READING record schema] |
| C-ENGINE-AB.1.1 — read_root(root_id) | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: receives this entry point's reading. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.1.3 — Engine A run_on_gold() | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — USED BY continuation for Fed by: provides the sealed v1 cases. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.1.3 — Engine A run_on_gold() | C-READ.2 — _validate_reading | BUILT — USED BY continuation for Gated by: gold-run output passes the shared shape check before append. | [V10 §6B / READING record schema] |
| C-ENGINE-AB.1.3 — Engine A run_on_gold() | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: receives A's gold-run output. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] |
| C-ENGINE-AB.2 — Engine B | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies target and same-thread preceding roots. | [V10 §5 / Accretive store + tooling] [V10 §7C] |
| C-ENGINE-AB.2 — Engine B | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: receives the positional-context test reading. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.2.1 — read_root_b(root_id) | C-READ.2 — _validate_reading | BUILT — USED BY continuation for Gated by: the resulting reading must satisfy the shared shape check before append. | [V10 §6B / READING record schema] |
| C-ENGINE-AB.2.1 — read_root_b(root_id) | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: receives B's entry-point output. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: supplies the roots from which preceding same-thread turns are selected. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.2.2.2 — source_title grouping | C-STORE — Accretive store & sealed roots (§6B) | BUILT — USED BY continuation for Fed by: carries the `source_title` values with each stored root. | [V10 §5 / Accretive store + tooling] [V10 §6B] |
| C-ENGINE-AB.2.4 — Engine B run_on_gold() | C-GOLD — Sealed gold sets v1, v2-B (§7C) | BUILT — USED BY continuation for Fed by: provides the seven sealed v2-B cases. | [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.2.4 — Engine B run_on_gold() | C-READ.2 — _validate_reading | BUILT — USED BY continuation for Gated by: the gold-run reading must pass shape validation before append. | [V10 §6B / READING record schema] |
| C-ENGINE-AB.2.4 — Engine B run_on_gold() | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: holds B's gold-run output. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] |
| C-ENGINE-AB.4 — Quarantine-only engine output | C-READ.2 — _validate_reading | BUILT — USED BY continuation for Gated by: reading shape is checked before append; uncertainty is not a rejection reason. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, READING RECORD validator row] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] |
| C-ENGINE-AB.4 — Quarantine-only engine output | C-READ.4 — Quarantine readings destination | BUILT — USED BY continuation for Changes: adds test readings through the reading write boundary. | [V10 / THE ONE AUTHORITATIVE STATUS TABLE, Quarantine readings store row] [V10 §5 / Accretive store + tooling] |
| C-ENGINE-AB.6 — Engine operation records | C-READ.1.9 — reading.produced_by | DESIGNED — USED BY continuation for Fed by: supplies the engine reading's required reproducibility-grade provenance, including origin, model, digest, engine_version, prompt_version, config and retrieval_inputs. | [V10 §6B / READING record schema] [MAP C-ENGINE-AB] |
| C-ENGINE-AB.6 — Engine operation records | C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — USED BY continuation for Gated by: recording does not grant ordinary access to protected contents or override internal-use restrictions. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-AB] |
| C-ENGINE-AB.6 — Engine operation records | C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — USED BY continuation for Gated by: identity/security authorization remains applicable where required. | [V10 §0B / ACCESS AND AUTHORIZATION BOUNDARY] [MAP C-ENGINE-AB] |
| C-READ — Reading record, validator, writer (§6B) | C-ENGINE-AB — Engines A & B (§7C, §16) | BUILT — The existing CH03-b Fed by link is reciprocated in this piece’s C-ENGINE-AB USED BY table. | [V10 §5 / Accretive store + tooling] [V10 §6B / READING record schema] |

## Appendix A carry-forward — this piece

| Part | Field | Occurrence | Value |
|---|---|---|---|
| C-ENGINE-AB.1.2 — Bare-root reading instruction | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-AB.1.2 — Bare-root reading instruction | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.1.2 — Bare-root reading instruction | Gated by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2 — _get_preceding_turns(n=3) | Gated by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2.1 — n | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2.1 — n | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2.2 — source_title grouping | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2.2 — source_title grouping | Gated by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.2.2 — source_title grouping | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.2.3 — BACKGROUND/END BACKGROUND framing | Gated by | 1 | NOT DECIDED |
| C-ENGINE-AB.3 — MOUTH_MODEL | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.3 — MOUTH_MODEL | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.5 — Benchmark protection | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.5 — Benchmark protection | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.6 — Engine operation records | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.6.1 — Run comparability metadata | Fails closed by | 1 | NOT DECIDED |
| C-ENGINE-AB.6.1 — Run comparability metadata | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.6.1 — Run comparability metadata | Gated by | 1 | NOT DECIDED |
| C-ENGINE-AB.6.1 — Run comparability metadata | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.7 — Reading without surrounding context | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.7 — Reading without surrounding context | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.8 — Insufficient-context outcome | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.8 — Insufficient-context outcome | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.9 — Wider-thread reading boundary | Gives out | 1 | NOT DECIDED |
| C-ENGINE-AB.9 — Wider-thread reading boundary | Fed by | 1 | NOT DECIDED |
| C-ENGINE-AB.9 — Wider-thread reading boundary | Changes | 1 | NOT DECIDED |
| C-ENGINE-AB.9 — Wider-thread reading boundary | USED BY row 1 / Changes there | 1 | NOT DECIDED |

## Source coverage and explicit deferrals

| Source scope | Card or later piece | Coverage boundary |
|---|---|---|
| V10 status table, A/B, quarantine and engine-failure rows | C-ENGINE-AB; .1; .2; .4; .8 | Built engine/output behavior is separated from decided failure behavior. |
| V10 §5, A/B engine entries and their output/model references | C-ENGINE-AB.1–.4 | Both files, both reading entry points, both run_on_gold entry points, MOUTH_MODEL, positional retrieval and destination. |
| V10 §7C, A/B engine-layer paragraphs | C-ENGINE-AB.1; .2; .9 | Bare root; speaker act; preceding same-thread turns; n=3; full content; BACKGROUND framing; future wider-thread boundary. |
| V10 §6A / PROTECTED FILES AND STORES, A/B paragraph | C-ENGINE-AB.5 | All eight named classes of benchmark-affecting change and the authorization/two-gold-rerun requirements. |
| DD §3E, A/B context and four prompt instructions | C-ENGINE-AB.2; .2.2; .2.3 | Positional retrieval, no truncation, no referencing/quoting/paraphrasing background, no invention, short confirmations. |
| DD §3D, engine-failure bullet | C-ENGINE-AB.8 | Honest revisable reading. General retry orchestration belongs to CH05-a and CH05-d. |
| CR §7, the two engine entries | C-ENGINE-AB.5 | B3-understanding restriction retained as a designed constraint, not an implemented gate. |
| V10 §7F, Engine B n=3 paragraph | C-ENGINE-AB.2.2.1 | Three is not the universal future positional limit. Full context-retrieval mechanics belong to CH05-c. |
| V10 §16, current-mouth and wider-thread distinctions | C-ENGINE-AB.3; .9 | Current test model is not final; successful benchmarking is required. General model-layer policy, old produced_by preservation and replacement behavior belong to CH10-b. |
| MAP C-ENGINE-AB | C-ENGINE-AB; .5; .6; .6.1; existing C-READ.1.9 and its member cards | Engine and logging names are covered. Reading provenance reuses the existing C-READ.1.9 member cards; no second provenance schema is created. |
| V10 §0B, engine recordkeeping and access obligations | C-ENGINE-AB.6 | One real operation/one log; no recursive logging loop, silence, destruction or double evidence. Full shared log lifecycle remains in CH02. |
| Bundle 6 policy §4 / A3.4 | C-ENGINE-AB.7 | Absent surroundings and reason recorded; target-only support; context-limited and revisable; later new reading never rewrites old. |
| MAP C-GOLD, gold-case preservation and judge boundary | C-ENGINE-AB.1.3; .2.4 | Only these gold-use boundaries enter here; full scoring rules, cases and story-gold scope are in CH03-l. |
| V10 §11 item 20, B background and result cautions | C-ENGINE-AB.2.3; .2.4 | No promised 7/7 or isolated B3 cause; individual gold-case IDs belong to CH03-l. |

## Review of plain gates

| Card | Reason no other card is named |
|---|---|
| C-ENGINE-AB.5 — Benchmark protection | A person's authorization, explicitly permitted by lessons 3.3. |
| C-ENGINE-AB.7 — Reading without surrounding context | The card's own no-surroundings precondition, explicitly permitted by lessons 3.3. |
| C-ENGINE-AB.9 — Wider-thread reading boundary | The card's own evidence-before-capability-claim precondition, explicitly permitted by lessons 3.3. |

## Coverage matrix — carried source inventory

The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.


### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c scoped reread: status table, §0/0A/0B, reading schema, §7G-A RC sequence and §7K; Chapter 3-d focused status-table, §0B and §§6A/6B checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c C-READ/C-7K and adjacent interfaces searched/reopened; Chapter 3-d C-READ and CY-G/B16 owner checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Newly read whole for this correction, all 1,938 lines; pinned Git blob verified; Chapter 3-c focused retry/malformed searches and §§2.8/3.7 excerpts; prior whole-read credit retained | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Detailed source landing map

| Bridge section | Cards in this piece |
|---|---|
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |


## READ RECORD

The source files below match their Git blobs at `6a7160ba688ba4e433a31899162815df7e2bab17`. The covered source sections were reopened; the scope table lists them. The Bundle 6 package-complete receipt was read whole. No fresh whole-file credit is claimed for the other source files, which were reread in the scoped sections listed above. Earlier whole-read credits remain those recorded in the preceding pieces. Contract §§5–11 were reopened before writing; §11.3 is reopened after writing for the checks below. The lessons sheet and run instructions were read in full.

| Source file | SHA-256 |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/cursorrules` | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |

Instruction fingerprints:
- `NH_MASTER-21_SYSTEM_BEHAVIOR_BUILD_CONTRACT_FOR_CHATGPT_v1_0.md` — SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- `NH_MASTER-21_WRITER_LESSONS_FROM_AUDITS_v0_1.md` — SHA-256 `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- `NH_MASTER-21_WRITER_RUN_INSTRUCTIONS_v0_2.md` — SHA-256 `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |

### READ-folder files not yet read whole

The inherited pending list contains 98 files. Scoped rereads here do not remove any pending entry; the ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 20 behavior cards reviewed; protected engine boundaries retained as source behavior, delivery records kept outside cards.
§1.4 every gap written as NOT DECIDED: PASS — 31 empty fields/cells, with exactly matching carry-forward entries.
§1.5 conflicts marked, none resolved: PASS — no new conflict introduced; earlier conflict registers remain unchanged.
§3 exactly one stamp per line: PASS — 176 populated field lines, 33 USED BY rows and 20 headers checked; empty fields use only NOT DECIDED.
§4 every behavior line cited in the exact format: PASS — 32 distinct citations resolve in pinned source sections; every populated field and USED BY row cited. Source support reviewed manually.
§5.4 one name per thing: PASS — 20 IDs checked against earlier cards, with no collision; relationship names checked against the corrected CH00 index and established sub-part names.
§6 all template fields present, in order, for every part: PASS — 20 complete templates and 206 field lines.
§6.3 reciprocity within this chapter: PASS — 31 internal links reciprocated; 27 outward links have continuation rows naming both ends. The 28 continuation rows include the existing incoming C-READ link.
§6.4 every decided detail written in, no citation used in place of content: PASS — source-scope map reviewed against the authored boxes; deferred gold, schema, model and shared-log details named explicitly.
§6.5 sub-parts recursed to the bottom: PASS — 20 cards; named functions, retrieval parameter, thread grouping, prompt boundary, output boundary and operation metadata represented; established provenance cards reused.
§9 coverage matrix rows added for every file used: PASS — 6 current source files fingerprinted and included in the carried inventory; the scope map records new placements. Receipt supplies status only.
§10.11 no recommendation, no sentence addressed to Ness: PASS — all behavior cards reviewed; references to authorization describe the source-defined boundary.
Files read whole for this chapter: the writer lessons sheet v0_1 and run instructions v0_2; the Bundle 6 package-complete receipt. Other source use consists of the scoped rereads listed above, with prior whole-read credit retained. Contract §§5–11 reopened before writing and §11.3 after writing.

Self-check output, computed from the finished file before this block:

| Check | Result |
|---|---|
| cards | 20 |
| field_lines | 206 |
| populated_fields | 176 |
| not_decided_fields_and_cells | 31 |
| used_by_rows | 33 |
| relationships | 58 |
| internal_relationships | 31 |
| external_relationships | 27 |
| continuation_rows | 28 |
| plain_gates | 3 |
| step_cards | 8 |
| source_names_checked | 28 |
| unique_citations | 32 |
| source_identities | 6 |
| earlier_identities | 11 |
| pending_source_paths | 98 |
| built_field_lines | 97 |
| misfiled_scan_fields | 206 |
| empty_restriction_failure_gate_boxes_reviewed | 10 |
| formula_hits | 0 |
| wording_hits | 0 |
| errors | 0 at writing; audit 1B later confirmed errors, corrected in round 4B |

The misfiled-box scan covered every field; each remaining empty restriction/failure/gate was reviewed against the full card and its sources. Every step names a rule card. All plain gates are justified in the gate-review table. Each BUILT field was checked against the V10 status table and the specific documented behavior; model choice, worker, policy and recordkeeping links retain their non-BUILT status. Statements about scope, counts and deferrals were checked against this file. Source paths were checked at the pin. Runtime filenames were checked against V10’s description, including the explicitly absent production store; no access to the live N.H filesystem is claimed. P-MAIN has no direct C-ENGINE-AB step; side-path placement is carried to CH11.
