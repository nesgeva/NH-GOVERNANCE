# DERIVED READER COPY — DO NOT EDIT INDEPENDENTLY

**Authoritative source:** `NH_MASTER-17_FULL_DRAFT_CORRECTED_v2.md`  
**Source SHA-256:** `cfdaefe9b0b6c134a911f102ae6479fb845662165a1cf216aec465ff816ce152`

This file is a reader/working copy for focused use with Claude or ChatGPT.  
The complete source file remains authoritative. Section wording below is copied from the source and must not be edited independently. Any real change must be made in a new complete Master version, then the reader copies regenerated.

---

# N.H — MASTER-17 (complete, self-contained, full S17 draft)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, the code rules, AND the complete S17 conceptual design — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–13. Session 14 (June 23 2026) was a DESIGN-then-BUILD session → MASTER-15. S14 closed the three genuinely-open forks AND shipped the next build. Session 16 (June 24 2026) was a BUILD session → MASTER-16. S16 built Engine B (context-search), gold v2-B (7 sealed context-requiring cases), and the Chroma rebuild (`nh_roots_v1`). Hardware upgrade path decided. Engine B scored 6.5/7 on the tested dolphin 8B setup. Current evidence points to a model-capability or prompt/context interaction limit rather than a confirmed engine defect; this remains a hypothesis to re-test on a stronger model.*

*Session 17 (June 24 2026) was a broad conceptual-design session. S17 completed the core conceptual architecture of the major components addressed during the session, while several larger areas remain open. No code was written in S17. S17 additions are [CONCEPTUALLY DESIGNED, NOT BUILT] or [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] as stated in the authoritative status table.*

*★ The DECISION-DEFAULTS file should be regenerated as S17, synced to this master.*

*★ CORRECTION PASS (June 24 2026, S16): interaction-control wording was separated from project workflow; direct artifact delivery was clarified; several predictions and hardware/cost claims were changed from certainty to testable hypotheses or dated decision snapshots; one query-volume unit error was corrected. No prior master was overwritten.*

*★ S17 CONSOLIDATION (June 24 2026): core conceptual architecture added for the catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, contradiction and clash handling, story layer, person-boxes, computed view, action surfacing, action-result return path, and permission and authority boundaries; the Living State Web and privacy/deletion/sensitive-data handling were partially conceptually designed. Interface and world design log incorporated. Engine B overclaims corrected throughout. `subject` field audited and documented. §7D revised from conceptual destination to partial design. New §§7E–7Q added. New §§18–19 added.*

*★ S17 DOCUMENT-CORRECTION PASS (June 24 2026): removed build-script debris; reconciled status wording; restored the historical S16 provenance line; aligned privacy access rules with Ness-private access being open by default; kept action outcomes and causation revisable; clarified View Layer versus Computed View ordering, append-only clash history, pre-ingest metadata-only visibility, action-risk mapping, and the presentation-only default for world manipulation. The original full draft was not overwritten.*

---

> ## ★ THE ONE AUTHORITATIVE STATUS TABLE (single source of truth — every other section must AGREE with this; if prose anywhere conflicts, THIS wins)
> *Status lives HERE, once. Prose may describe, never re-assert a different status.*
>
> | Component | Status | Proof / Note |
> |---|---|---|
> | Clean accretive store — 5,521 roots, 7-field, role-carried | **BUILT & VERIFIED** | `find /c` = 5521; re-verified S14 |
> | Roots file SEALED (`.nh_roots.sealed`) | **BUILT & VERIFIED** | append refused; re-verified S14 (0 bytes, dated 06/22 23:05) |
> | Two-file ROUTING (`append_reading`→sibling) | **BUILT & VERIFIED** | S13 |
> | READING RECORD — validator (`_validate_reading`, 12-field) | **BUILT & VERIFIED (S14)** | new function; 17/17 fixture tests pass; gates on shape not confidence |
> | READING RECORD — writer (reading-shaped `append_reading`) | **BUILT & VERIFIED (S14)** | signature now `(reads, meaning, confidence, role, story_layer, mode, produced_by, schema_version, derived_from, idempotency_key, record_id, timestamp)`; root-verify + idempotency + atomic append |
> | Shared `_check_common` helper (id+timestamp) | **BUILT & VERIFIED (S14)** | extract-not-fuse; roots still validate clean through it |
> | Reading-record `confidence` representation | **DECIDED (S14)** | §11 item 19 — TWO-SLOT object `{interpretation_confidence, source_reliability}`; source_reliability slot-present / value-empty-until-knowable; NEVER one blended number |
> | Reading-record SHAPE overall | **SETTLED (S14)** | last open piece (confidence) resolved; validator now enforces it |
> | Gold scoring rule | **DECIDED (S14)** | §11 item 20 — six rules below; semantic match, Ness judges |
> | Engine failure-behavior | **DECIDED (S14)** | §11 item 20 — honest insufficient-context reading, marked revisable; retry-trigger deferred |
> | GOLD SET v1 — 8 cases, annotated + SEALED | **BUILT & SEALED (S14)** | `NH_GOLD_SET_v1.md` (4,951 B) + `.nh_gold_v1.sealed` marker on disk |
> | GOLD SET v2-B — 7 context-requiring cases, annotated + SEALED | **BUILT & SEALED (S16)** | `NH_GOLD_SET_v2_B.md` (5,449 B) + `.nh_gold_v2_B.sealed` marker on disk |
> | Quarantine readings store (`.nh_readings_quarantine.jsonl`) | **BUILT (S14)** | separate test file; holds A + B gold-run output; production readings store still absent |
> | Minimal engine A (`nh_engine_minimal.py`) | **BUILT & RUN (S14)** | root → mouth → 12-field reading → quarantine; run against the 8 gold; ~5–6/8 solid after prompt+role fixes |
> | Engine B (`nh_engine_b.py`) | **BUILT & RUN (S16)** | root → preceding turns → BACKGROUND prompt → mouth → 12-field reading → quarantine; run against gold v2-B; 6.5/7 on the tested setup; cause of B3 miss not yet proven |
> | Chroma `nh_roots_v1` (5,521 clean roots) | **BUILT (S16)** | rebuilt from clean roots via `nh_rebuild_chroma.py`; cosine distance; `all-MiniLM-L6-v2` embeddings |
> | `nh_rebuild_chroma.py` | **BUILT (S16)** | dry-run verified; full run 187.59s; keeps old collections untouched |
> | Production readings store (`.nh_readings_store.jsonl`) | **ABSENT (correct)** | no production readings yet; quarantine-only by design |
> | Speaker detector recipe (embed+shape→LogReg C=0.1→94.89%) | **INVESTIGATED & PROVEN, NOT DEPLOYED** | fallback only |
> | Ingest pipeline (`nh_ingest_chatgpt.py`) | **BUILT & VERIFIED** | S12 |
> | Chroma `nh_reality_core` (116,391) | **BUILT — OLD/unaligned index** | keep until `nh_roots_v1` proven; do NOT destroy |
> | The engine (2c) — full chain of webs | **PARTIALLY BUILT (A + B; C not built)** | A = meaning + role; B = + preceding context; C (story) NOT built |
> | Mouth model choice | **dolphin-llama3 = best tested on current disk (S14/S16)** | it outperformed `qwen2.5-abliterate:3b` on the tested cases; this does not prove a universal 8B ceiling |
> | Hebrew reading quality | **WEAK-BUT-WORKABLE; gated on bigger model/VRAM** | §16 — prompt changes alone did not solve it in the tested runs; larger-model/VRAM experiment planned (S16) |
> | Hardware upgrade path | **PLANNED (S16; verify at purchase time)** | candidate RTX 5060 Ti 16GB; quoted snapshot ~₪2,590 from פי.סי סנטר with stated 3-year warranty; intended purchase date 5.7.2026; exact stock, price, PSU compatibility, and model tag must be re-verified |
> | Multi-box (sealed-batch) architecture | **NOT DESIGNED** | §11 item 18 |
> | View layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | two-view rule settled S17; §7I |
> | Quarantine promotion + memory-health checks | **DESIGNED, NOT BUILT** | §11 item 27 |
> | Pure-tape redaction/destruction path | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | policy, operation types, tombstone rule, blocking behavior, and verification outcomes designed in §7Q; storage mechanics, derivative discovery, cryptographic erasure, and verification implementation remain open |
> | Confidence value-form (low/med/high vs 0–1) | **DELIBERATELY LOOSE** | validator checks present+non-empty only; pinning later = new schema_version |
> | `subject` field (v1 roots) | **DOCUMENTED AS LEGACY PROVENANCE-BATCH TAG** | S17 audit; values are seed:conversations_000/001/002; rename deferred to next schema version; §6B |
> | Pre-ingest holding area | **CONCEPTUALLY DESIGNED, NOT BUILT** | seven lifecycle states, blocker list, unified store; §7E |
> | Catalog front door | **CONCEPTUALLY DESIGNED, NOT BUILT** | two gates, intake envelope, enrichment boundary; §7E |
> | Context retrieval layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | two channels, per-mode parameters, bounded; §7F |
> | Meaning Engine interior flow | **CONCEPTUALLY DESIGNED, NOT BUILT** | one-pass rule, reading proposal acceptance check; §7G |
> | Reading Proposal Acceptance Check | **CONCEPTUALLY DESIGNED, NOT BUILT** | explicit validation step independent of mouth self-assessment; §7G |
> | Model confidence is metadata not authority | **FIRST-CLASS PRINCIPLE (S17)** | applies to all present and future models; §7G |
> | Story-layer evidence rules | **CONCEPTUALLY DESIGNED, NOT BUILT** | two channels, circular support prohibited; §7G |
> | Reread lifecycle | **CONCEPTUALLY DESIGNED, NOT BUILT** | three trigger types, full provenance; §7H |
> | Contradiction and clash handling | **CONCEPTUALLY DESIGNED, NOT BUILT** | six types, two detection modes, response events; §7J |
> | Story Layer | **CONCEPTUALLY DESIGNED, NOT BUILT** | structured perspective, firmness, hybrid themes; §7K |
> | Person-Boxes | **CONCEPTUALLY DESIGNED, NOT BUILT** | proposal-based creation, seven-section view; §7L |
> | Computed View | **CONCEPTUALLY DESIGNED, NOT BUILT** | seven-factor ordering, triggered snapshots; §7M |
> | Living State Web | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | node/edge types, grounding, currency, action surfacing, return path designed; schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control, purpose-aware lenses, world model undesigned; §7D |
> | Action surfacing | **CONCEPTUALLY DESIGNED, NOT BUILT** | permission-controlled hybrid, possibility-disposition states; §7N |
> | Action-result return path | **CONCEPTUALLY DESIGNED, NOT BUILT** | two result types, six result states, three linked objects; §7O |
> | Permission and authority boundaries | **CONCEPTUALLY DESIGNED, NOT BUILT** | two layers, four risk levels, three action states, violation/correction rule; §7P |
> | Privacy, deletion, and sensitive-data handling | **PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT** | five operations, four sensitivity levels, deletion framework, exclusion system, third-party baseline, two-stage access control, private-access presumption designed; detection methods, verification procedures, implementation mechanics undesigned; §7Q |
> | Interface, World, and Interaction System | **IN-PROGRESS DESIGN, NOT BUILT** | architectural content incorporated; simulation interior, gesture vocabulary, VR, camera, accessibility substantially undesigned; design paused; §19 |
> | Attention and relevance control | **NOT DESIGNED** | identified as remaining area |
> | Wonder and simulation mechanism | **CONCEPT LEVEL ONLY, MECHANISM NOT DESIGNED** | concept in §7B; interface concepts in §19 |
> | World model | **NOT DESIGNED** | named in Living State Web domain list |
> | End-to-end cycle | **IDENTIFIED, NOT YET DESIGNED** | the major components addressed in S17 have core conceptual architecture; attention/relevance control, simulation mechanism, world model, and the single connected end-to-end sequence remain open |
>
> **2a = COMPLETE. 2b = INVESTIGATED (not deployed). 2c = STARTED: A ✅ B ✅ C next.**

---

> **0. ★ THE READING RECORD IS BUILT — VALIDATOR + WRITER LIVE ON DISK (S14).** What changed from S13:
>    - **BUILT & verified (S14):** `_validate_reading` — the 12-field shape gate. Rejects malformed, never rejects uncertain (R5). A low/weak/empty-story/insufficient-context reading is WRITTEN-and-marked, never refused. 17/17 fixture tests pass.
>    - **BUILT & verified (S14):** reading-shaped `append_reading` — verify-referenced-root-before-commit, idempotency reject on `idempotency_key`, atomic append (flush+fsync), append-only, writes to a target path.
>    - **BUILT & verified (S14):** `_check_common` — shared id+timestamp checks, extracted ONCE; `_validate_record` (roots) now delegates to it. The 5,521 sealed roots STILL validate clean through the helper (regression proven).
>    - **The reading record contract (12 fields):** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. `confidence` is now the TWO-SLOT object (see §6B). Coded, gated, verified.
>    - **The seal is per-BATCH, not "no more data ever."** ⚠ multi-box architecture still undesigned (§11 item 18).
>
> **1. ★ THE READING-RECORD SHAPE IS FULLY SETTLED (S14) — confidence resolved.** `story_layer` = a LIST of tellings; `mode` = an OPEN word + classification_confidence; unknown parts OMITTED. **And the last open piece, `confidence`, is resolved: a TWO-SLOT object** (`interpretation_confidence` + `source_reliability`), never one blended number. The validator enforces the whole shape.
>
> **2. ★ THE GOLD SETS ARE SEALED.** Two sealed gold sets on disk:
>    - **v1 (S14):** 8 clean-bare cases — each judged as a standalone line, no surrounding context needed. `NH_GOLD_SET_v1.md` + `.nh_gold_v1.sealed`.
>    - **v2-B (S16):** 7 context-requiring cases — each unreadable without preceding turns. `NH_GOLD_SET_v2_B.md` + `.nh_gold_v2_B.sealed`. Cases: B1 `7ac0381c` "episode 2"; B2 `4e125b71` "yes sure, second."; B3 `0df151d3` "yes, second option."; B4 `9359edff` emotional reaction to outline; B5 `580d74d4` "Brief slow."; B6 `09514821` "Yes! This is it."; B7 `4b4e5551` "כן".
>    - The gold seal holds for both: engine output may FAIL a case but may NEVER alter it; a correction is a NEW versioned gold.
>
> **3. ★ ENGINE A IS BUILT AND RAN (S14). ENGINE B IS BUILT AND RAN (S16).**
>    - **Engine A** (`nh_engine_minimal.py`): root → mouth → 12-field reading → quarantine. No context. ~5–6/8 on gold v1.
>    - **Engine B** (`nh_engine_b.py`): root → `_get_preceding_turns(n=3)` → BACKGROUND prompt → mouth → 12-field reading → quarantine. 6.5/7 on gold v2-B. B3 miss may reflect model-size, prompt-role separation, or context-format interaction; the present run does not prove which cause dominates.
>
> **4. ★ ENGINE B DESIGN DECISIONS (S16 — protect from re-litigation):**
>    - **Context strategy = POSITION-BASED, not semantic search.** `_get_preceding_turns` finds the N roots immediately before the target in the same `source_title` thread. Semantic search (`nh_roots_v1`) was tried first — pulled topically related roots but not conversational context. Position-based is the correct lever for conversational turns.
>    - **n=3 preceding turns, FULL content (no truncation).** Truncation at 100 chars was killing context quality — removing it fixed B5 ("Brief slow." read correctly only with full preceding assistant turn visible).
>    - **BACKGROUND/END BACKGROUND prompt framing (DECIDED S16).** Prevents the mouth from answering or continuing the conversation instead of reading the target line. The four rules: do not reference background, do not quote/paraphrase background, do not invent, if short confirmation say what they are confirming based on topic.
>    - **Observed Engine B score on the tested dolphin 8B setup = 6.5/7.** B3 read the content of the chosen option rather than the act of choosing. The leading hypothesis is a role-separation/model-capability limit, but context selection, prompt framing, and run variance remain possible contributors. A 13B model is a test, not a guaranteed fix.
>    - **Full-thread reading = future goal.** Load more or all of a conversation thread before reading each line. On the current 6GB setup this is likely impractical at the desired quality and speed. A larger-VRAM card and a model with a larger usable context window may make it practical, but must be benchmarked rather than assumed.

> **★ DECISIONS LOCKED IN SESSION 14 (protect from re-litigation):**
> - **`confidence` = a TWO-SLOT object** `{ interpretation_confidence, source_reliability }`. `interpretation_confidence` filled on every reading; `source_reliability` slot-present from the first reading but left EMPTY until the engine can honestly judge a source. NEVER one blended number; confidence never rises from copied error; a reading never inherits a prior's confidence. Story firmness inside `story_layer[].firmness`; retrieval relevance computed at search time, never stored. `mode.classification_confidence` is local and separate. SETTLED.
> - **GOLD SCORING — six rules.** (1) `meaning` judged by SEMANTIC match; Ness decides same/not-same by hand. (2) `story_layer` NOT graded in v1/v2-B. (3) MAKING SOMETHING UP is the real fail; leaving something out is NOT a fail if what's said is right. (4) Correct-but-EXTRA: true extra passes, made-up extra fails. (5) A case MAY list several acceptable readings. (6) NESS decides pass/fail; model assists, never judges. SETTLED.
> - **ENGINE FAILURE-BEHAVIOR.** When the engine can't interpret a root: writes an honest INSUFFICIENT-CONTEXT reading, MARKED revisable. Retry-trigger DEFERRED. SETTLED.
> - **CONFIDENCE VALUE-FORM left deliberately LOOSE** — validator checks present+non-empty only; pin later as new schema_version. SETTLED-as-deferred.
> - **VALIDATOR STRUCTURE = option C (extract, don't fuse).** `_check_common` holds shared id+timestamp. SETTLED + BUILT.
> - **MODEL FINDING (S14):** dolphin-llama3 beats qwen2.5-abliterate:3b. Hebrew quality is model-size-gated. SETTLED-as-finding.

> **★ DECISIONS LOCKED IN SESSION 16 (protect from re-litigation):**
> - **HARDWARE UPGRADE PLAN — dated decision snapshot, not a permanent market fact.** Candidate: RTX 5060 Ti 16GB (Gigabyte AERO OC, model GV-N506TAERO OC-16GD). At the time of the S16 discussion, a פי.סי סנטר listing was reported at ~₪2,590 with a stated 3-year warranty. Intended purchase date: 5.7.2026. Before purchase, re-check exact model, VRAM, seller, stock, current price, physical clearance, power connectors, PSU quality/wattage, and return/warranty terms. 16GB VRAM is preferred for larger local models, but VRAM is not the only relevant factor; model quantization, context length, memory bandwidth, thermals, PSU, and software support also matter. The exact `dolphin-llama3.1:13b` tag and expected speed must be verified by an actual pull/benchmark. Cards below 12GB are disfavored for this specific upgrade goal, not categorically unusable for all N.H work.
> - **TARGET MODEL AFTER UPGRADE.** A 13B-class uncensored model is the target. `dolphin-llama3.1:13b` is the current candidate name, but the exact available Ollama tag, license, quantization, VRAM fit, speed, and quality must be verified at installation time. Model swap rule: run the candidate against BOTH sealed gold sets (v1 + v2-B) and adopt only if the measured results improve. Old readings keep old `produced_by`. No auto mass re-read.
> - **ENGINE B CONTEXT STRATEGY = POSITION-BASED.** Settled. Do not re-open as semantic search.
> - **ENGINE B PROMPT = BACKGROUND/END BACKGROUND FRAMING.** Settled. Do not re-open.
> - **COST NOTES CONFIRMED.** N.H current monthly cost = $0. At full nightly automation (far down build list): Brave ~$62/month + OpenRouter synthesis ~$60-240/month = ~$120-300/month total. During building/testing: $0 (inside $5 free Brave credit). **SAFETY NOTE (build requirement for item 8):** Brave has NO spending cap — a loop can bill without stopping. When research pipeline is wired, a query counter / daily cap MUST be in the code. Not optional.

> **★ DECISIONS LOCKED IN SESSION 17 (protect from re-litigation):**
> - **CATALOG FRONT DOOR:** Two gates (raw capture and root ingestion). Minimum intake envelope defined. Pre-ingest store with seven lifecycle states and blocker list. Speaker and thread resolution rules. Four enrichment categories. All settled; §7E.
> - **CONTEXT RETRIEVAL:** Two channels (positional and semantic), kept separate and labeled. Per-mode retrieval parameters. Genuine no-context handling. System failure separation. All settled; §7F.
> - **MEANING ENGINE INTERIOR:** One reading per pass. Flow: root + context → mouth proposal → Reading Proposal Acceptance Check → reading record. Model confidence is metadata not authority (first-class principle). Story-layer two-channel evidence rule. Circular support prohibited. All settled; §7G.
> - **REREAD LIFECYCLE:** Three trigger types (manual, condition-based, scheduled-retry-only). All settled; §7H.
> - **VIEW LAYER:** Two-view rule (current and history). Ordering is presentation only. All settled; §7I.
> - **CLASH HANDLING:** Six clash types. Two detection modes. Ness response as separate event. All settled; §7J.
> - **STORY LAYER:** Structured perspective model. Firmness as engine inference. Hybrid theme system. All settled; §7K.
> - **PERSON-BOXES:** Proposal-based creation. Seven-section default view. All settled; §7L.
> - **COMPUTED VIEW:** Seven-factor ordering. Triggered immutable snapshots. All settled; §7M.
> - **ACTION SURFACING:** Permission-controlled hybrid. Possibility-disposition states defined. All settled; §7N.
> - **ACTION-RESULT RETURN PATH:** Two result types. Six result states. Three linked objects. All settled; §7O.
> - **PERMISSION AND AUTHORITY BOUNDARIES:** Two layers. Four risk levels. Three action states. Stop-and-surface violation rule. Narrow emergency stop exception. All settled; §7P.
> - **PRIVACY, DELETION, SENSITIVE-DATA:** Five operations. Four sensitivity levels. Deletion blocking/verification rule. Capture exclusion two-layer system. Third-party baseline. Two-stage access control. Private access for Ness open by default. Model-provider limitations recorded as mouth limitations. These core rules are locked, but the area remains **partially conceptually designed** because several policy details and implementation mechanisms are still open; §7Q.
> - **LIVING STATE WEB:** Node/edge types, grounding rule, currency rule, action surfacing, action-result return path, and relationships to Computed View/Story Layer/Person-Boxes/authority/privacy designed. Schema, evidence thresholds, and several domains remain undesigned; §7D.

> **PRIOR DELTA (SESSION 13 → MASTER-14) — condensed for continuity:**
> - [BUILT]-claims sweep done. 2a PLUMBING BUILT. Detector investigated (94.89%). Eleven doc-refinements + quarantine/bootstrap captured.

> **PRIOR DELTAS (sessions 4–12) — condensed for continuity:**
> - **S12:** store restored; `role` added (7-field); clean ingest; 5,521 clean roots; Chroma=old 116k; two-destinations shape.
> - **S11:** MODEL LAYER resolved; PERSON-BOXES, PURE TAPE, WONDER/SIMULATION, CATALOG, SOUL CORRECTION.
> - **S10:** 2a shaped; DUMB vs SMART frame; HELPER not DECIDER; story-layer; mode = peer web.
> - **S9:** the PREMISE §0; reality → per-person READING; speaker = carry `role`.
> - **S4–S8:** accretive store skeleton; unit = span-claim; forced build order; WhatsApp data-rescue (NOT ingested); live loop + chat front door + guard.
> - **S14:** three forks CLOSED. Reading validator + writer BUILT (17/17 tests). Gold v1 (8 cases) SEALED. Engine A BUILT & run (~5–6/8). dolphin beats qwen-abliterate-3b. Confidence value-form left loose.
> - **S15-chat:** NO N.H change. Scan-only + one teaching artifact (`NH_one_pass_demo.html`).
> - **S16:** Engine B BUILT & run (6.5/7 on gold v2-B). Gold v2-B (7 cases) SEALED. Chroma `nh_roots_v1` BUILT (5,521 roots). Hardware upgrade path decided. Cost notes confirmed.

> **THE NAME:** He is **Ness** (male). He signs **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = verified on disk today. **[CONCEPTUALLY DESIGNED, NOT BUILT]** = the core conceptual architecture and governing rules are settled, while exact schemas, thresholds, implementation details, or interface mechanics may remain open where explicitly listed. **[DESIGNED]** = older shorthand for decided but not coded. **[PARTIALLY CONCEPTUALLY DESIGNED]** = some core rules are settled while material conceptual areas remain open. As of S17: the clean store + role schema + ingest pipeline + 2a plumbing + reading record (validator + writer) + gold sets v1 + v2-B (both sealed) + engine A + engine B + Chroma `nh_roots_v1` are **[BUILT]**. The catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, clash handling, story layer, person-boxes, computed view, action lifecycle, and permission boundaries are **[CONCEPTUALLY DESIGNED, NOT BUILT]**. The Living State Web and privacy/deletion/sensitive-data handling are **[PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]**. Engine C is not built; attention/relevance control, the wonder/simulation mechanism, the world model, and the end-to-end cycle remain not designed or concept-level only.

> **★ STANDING LESSON (carried, still in force): trust disk, never the doc — including this file.** Before any build, existence-and-shape check first.

---

## AI WORKING MAP

Use these files as follows:

- `NH_MASTER-17_00_INDEX_STATUS.md` — authority notice, complete preamble, authoritative status table, and this navigation map.
- `NH_MASTER-17_01_FOUNDATION_BUILT.md` — §§0–6B: philosophy, system identity, interaction rules, machine/codebase state, schemas, and built components.
- `NH_MASTER-17_02_CONCEPTUAL_ARCHITECTURE.md` — §§7–7Q: Universal Filter, Meaning Engine, Living State Web, catalog, retrieval, rereads, views, clashes, Story Layer, Person-Boxes, Computed View, actions, authority, and privacy.
- `NH_MASTER-17_03_ROADMAP_INTERFACE_HISTORY.md` — §§8–19 plus closing principles: research pipeline, roadmap, session history, model layer, correction logs, and Interface/World system.

### Which file to give the AI

- **Focused architecture work:** upload `00_INDEX_STATUS` plus the relevant part.
- **Cross-component audit, adoption, defaults regeneration, or status reconciliation:** upload the complete authoritative Master.
- **Never treat a reader copy as a replacement for the complete Master.**

---

