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

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

**The line:** The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact. The AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time, even wonder/simulate forward at night — and do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**The crystallization:** **N.H is Ness's HELPER, not Ness's DECIDER.** A helper reads, connects, lays out what it sees, even leans — then hands it to the person, who decides. A decider closes the book.

**★ THE SOUL CORRECTION — three truths held at once, never collapsed:**
1. **Interpretive meaning is never stored as a universal fact — it remains a situated story** (§3G). There is no fact-box for *meaning*.
2. **Ness still decides / affirms.** He is the decider, the membrane. The system does NOT decide what is real — and neither does it pretend nothing is ever decided.
3. **★ His deciding is NOT a node in the engine.** It happens out in real life, engine absent. There is no step after "show." *(S13 cross-link: recording THAT he reacted is allowed — item 23's seam stores the OCCURRENCE as a dated, weightless story-layer event so a dismissed reading stops resurfacing. What stays off-board is the TRUTH-verdict.)*

**The crucial distinction:** "never decide facts" does NOT mean "never hold anything firmly." Something can be held with full weight and still never close the book.

**★ S13 SHARPENING:** the DUMB machinery MAY establish directly-verifiable machine-state & provenance facts. The SMART machinery MAY interpret, connect, lean — but may NEVER silently promote an interpretation into an established fact. The authority for any such promotion is Ness, off-board.

**★ S14 LIVE EXPRESSION OF §0 — the engine reads by PATTERN, so it can be wrong, and that is designed-around, not a flaw.** The mouth places a line by similarity to millions of lines it has seen; it does not truly understand. So it WILL misread sometimes. Every guard exists precisely because of this: never-close-the-book, confidence, only-adds, Ness-decides-off-board, and the gold. A system that assumed it was always right would be the dangerous one.

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame]

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The pure tape, the append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), role-carried-from-source, the catalog's who/when/where marking, CARRYING/STORING the `mode` label once SMART has named it, the person-box GATHER, the live loop's fire-and-let-go. One law: **never interpret, never close — only add / point / carry / sort / gather.** Safe BECAUSE it cannot interpret.

> **★ THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety).** "Append-only" must NOT mean "permanent recoverable storage of every secret forever." Allowed: capture exclusions for credentials/secrets; encrypted storage; retention boundaries; cryptographic erasure of selected content; an append-only TOMBSTONE retaining THAT a deletion occurred without the deleted plaintext; special treatment for third-party and childhood data. The governing policy is partially conceptually designed in §7Q; exact storage mechanics, cryptographic-erasure methods, derivative discovery, backup handling, and verification implementation remain undesigned (§11 item 24).

> **★ "ABSENCE IS READ" NEEDS A GUARD.** Absence is meaningful ONLY when the system EXPECTED the info, the process was CAPABLE of observing it, the absence is relevant, and the interpretation is held WEAK. Distinguish `not_observed`/`not_evaluated`/`not_applicable`/`withheld`/`collection_failed` in processing metadata; a blank in a reading stays honest (never `"unknown"`).

- **SMART (psychologics) MACHINERY — reads the *person*.** The meaning webs (Theory of Mind, the STORY-layer, gap-reading, firmness-as-read), the mode/register NAMING (open-word `mode` + classification_confidence), clash-surfacing, the wonder/simulation, the NOTE. One law: **everything here is weightless, dated, confidence-tagged, rejectable — NEVER a fact.** Safe BECAUSE it cannot close.
- **THE BORROWED MOUTH (§16) sits at the seam, used by SMART.** The wording model turns meaning into sentences — swappable. The embedding/search model is a DUMB tool (sorts by meaning-distance).

**The membrane (§7A R7) is the boundary between them** — creation (SMART) never closes into memory (DUMB).

---

## 1. WHAT N.H IS

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The one-line soul:** **N.H is Ness's HELPER, not Ness's DECIDER.** The loop: *real life → into N.H for help → it helps him see and understand his own thinking in the way that fits how he thinks → he returns to real life with a solution that is his own.*

**★ WHAT JARVIS ACTUALLY IS:** Jarvis is NOT the model. The model is a borrowed, frozen mouth (§16). **Jarvis is the memory + the soul + the gathering + the mouth, wired together.**

**★ MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS.** New input is *read* by the webs and lands as a reading (meaning + confidence + story-layer). The growth lands in the memory, never in the frozen mouth.

**★ THE TWO-DESTINATIONS SHAPE (Ness re-derived it):** every **eligible accepted** input goes to TWO places at once — (1) the **RAW ROOT**, saved untouched and sealed; (2) **THROUGH THE FILTER**, which READS it and lays a **READING** beside the root, pointing back by id, never altering the raw. The only change a root can undergo is deliberate, audited destruction (§0A). This is exactly why there are TWO FILES.

**The two purposes, always running together:**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside.
- **OUTWARD — the engine:** translate new external data through the lens of how *his* mind connects things.
- **ONE FILTER, BOTH DIRECTIONS.** The two feed each other.

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED]

Text, images, video, audio — all flow through the SAME engine. New input types get a new **front door**, not a new engine. Two stages (§14): RAW capture → CATALOG (who/when/where). The live chat itself is a front door.

**The deepest "why" — הכל יחסי:** nothing about *meaning* is final — a thing means what it means only relative to ever-growing context, and relative to whom. This is why memory only adds, classification is never locked, "unknown" is honest, and the affirmation surface is a per-person STORY, not a shared fact-box.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time.** He asks "why yes / why no" and wants real tradeoffs. He often asks for things "plainly" — give the plain version directly. **(S14: when explanations didn't land, the fix was always to go simpler and more concrete, with a worked example — never more abstraction.)**
- **Verify on disk, never trust status reports.**
- **Honest correction over flattery** — explicitly, repeatedly asked for.
- **Don't inform, just flag and keep going.**
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, elongated punctuation are NOT distress.
- **He catches things.** When he pushes back, he is usually right.
- **He works to UNDERSTAND before moving.** This is not hesitation — it's him needing the mechanism to fit his head. Honor it; go slower, not faster.
- **He is not afraid of work.** A wall is almost never "this is hard" — it is "this move would destroy/forfeit something."
- **He re-derives his own design from the inside.** Offer shapes, let him rebuild and steer.
- **Backup before any destructive step, always.**
- **Primary risk pattern: scope-expansion before consolidation.** Finish and verify the current project task before expanding scope. This governs task order only; it does not authorize ending, pausing, or redirecting the conversation.
- **Assistant role:** architecture, audit, security, strategy, explanation, and direct artifact creation. Cursor may write or edit code when Ness chooses to use it; Cursor is not required for ordinary documents or Markdown files. Ness runs and verifies commands that affect his machine or project state.
- **Session authority:** Ness alone decides when a session begins, pauses, ends, or moves to a fresh chat. Do not suggest sleep, rest, wrapping up, a fresh chat, or end-of-session documentation unless Ness explicitly initiates it. End-of-session master/defaults regeneration is an optional workflow triggered only by Ness.

---

### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED

- **Latest instruction wins.** If Ness rejects a method, stop using and mentioning that method unless he later reopens it.
- **Anti-loop rule.** After the same misunderstanding is corrected twice, abandon the current plan, restate the exact requested deliverable in one sentence, and produce it directly.
- **Actual-file rule.** When Ness asks to create, update, rebuild, or deliver a file, return the actual downloadable file. Do not substitute Cursor, CMD, PowerShell, terminal, Notepad, copy-paste, or manual-creation instructions unless Ness explicitly asks for that workflow.
- **Version safety.** Create a new versioned file; never silently overwrite, rename, delete, or replace the previous authoritative master. The prior master remains authoritative until Ness reviews and adopts the new one.
- **No false human-state explanations.** Do not explain mistakes by claiming tiredness, impatience, being on fumes, or "losing it." Say plainly that the instruction was misread or an incorrect plan was repeated.
- **No session pressure.** Project discipline such as "finish and verify" applies to task order, never to whether Ness should sleep, stop, document, or close the session.

---

## 3. THE EVOLUTION — OLD vs NEW (key points)

- **A. Manual gate → MEMBRANE.** Memory only ADDS. [Accretive store BUILT; clean roots S12; sealed S13.]
- **B. Many "is this real?" gates → ONE UNIVERSAL FILTER.** [DESIGNED §7A; engine A BUILT S14; engine B BUILT S16.]
- **C. AI creativity → the membrane.**
- **D. Security holes found on disk → fixed.** *(⚠ `cloudflared.exe` inert but on disk — convenience-sweep item.)*
- **G. Affirmation surface → per-person STORY-layers.** [DESIGNED.]
- **H. The person → PERSON-BOXES.** [CONCEPTUALLY DESIGNED §7L.]
- **I. "Do I train a model?" → BORROW A FROZEN MOUTH** (§16). [DESIGNED + on disk.]
- **J. (S12) The store — from a 188-stub → 5,521 CLEAN roots.** [BUILT & VERIFIED.]
- **★ K. (S14) The reading record — from DESIGNED-NOT-CODED → BUILT validator + writer + engine A + sealed gold v1.** [BUILT & VERIFIED.]
- **★ L. (S16) Engine B — from NOT BUILT → BUILT & RUN at 6.5/7 on sealed gold v2-B. Chroma rebuilt from clean roots. Hardware upgrade path decided.**
- **★ M. (S17) Broad conceptual design of the major components addressed during the session** — core conceptual architecture for the catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, clash handling, story layer, person-boxes, computed view, action lifecycle, and permission and authority boundaries; partial conceptual design of privacy/deletion/sensitive-data handling and the Living State Web. Several larger areas remain open. No code written.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2). Python **3.13.14**.
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM). **Motherboard ASRock B560 Pro4** (PCIe x16, 8-pin PCIe power available). **Case Antec NX410.** 32 GB RAM. *(Verified by inspection S14.)*
- **Launched via** `run_app.pyw` → pywebview at `http://localhost:8080/`. The CORE is LOCAL and offline by default; only the optional research connectors touch the network.
- **★ MODEL HARDWARE REALITY:** the 6GB 2060 runs 3B models normally (~35–50 tok/s); 7B/8B run but SLOW (~7–9 tok/s). Context window is limited.
- **★ S16 UPGRADE PATH (PLANNED — verify on 5.7.2026 before purchase):** Engine B scored 6.5/7 on the current tested setup. A larger-VRAM GPU and a 13B-class model are the next experiment, not a guaranteed fix. **Current candidate card: RTX 5060 Ti 16GB** (Gigabyte AERO OC, model GV-N506TAERO OC-16GD); the S16 price/warranty details are a dated snapshot and must be checked again. PSU quality, wattage, connectors, case clearance, thermals, exact VRAM variant, and return terms must be verified before purchase. After installation, verify the exact available model tag, benchmark it against both sealed gold sets, and adopt only if results improve. **Future goal:** determine whether wider or full-thread context becomes practical at acceptable speed and quality.
- **Windows sign-in:** Kensington VeriMark fingerprint key.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` · `nh_context_router.py` · `nh_reality_graph.py` · `nh_simulation_graph.py` · `nh_epistemic_sandbox.py` · `nh_evidence_integrity.py` · `nh_jarvis_core.py` · `nh_crypto.py` · `nh_vector_memory.py`. *(OLD REALITY/SIMULATION gate stack — still runs harmlessly; do NOT rip out before the new filter is complete.)*

**Physical stores on disk (verified S14/S16):**
- **`.nh_accretive_store.jsonl` — 5,521 CLEAN roots, SEALED** (7-field). Roots-of-record.
- **`.nh_roots.sealed`** — seal marker (0 bytes, 06/22 23:05). `append_root` refuses while it exists.
- **`.nh_readings_store.jsonl`** — production readings sibling. **ABSENT** (no production readings yet — correct).
- **`.nh_readings_quarantine.jsonl` (S14)** — QUARANTINE test readings file. Both engines write here, never production.
- **`NH_GOLD_SET_v1.md` (S14)** — sealed gold answer key, 8 clean-bare cases (4,951 B).
- **`.nh_gold_v1.sealed` (S14)** — gold v1 seal marker (0 bytes).
- **`NH_GOLD_SET_v2_B.md` (S16)** — sealed gold answer key, 7 context-requiring cases (5,449 B).
- **`.nh_gold_v2_B.sealed` (S16)** — gold v2-B seal marker (0 bytes).
- Backups: `.bak_preseal` (roots), `.bak_188_preclean`, `nh_accretive_store.py.bak_pre_minimal_engine_A_*` (S14).
- **`chroma_db\` — ChromaDB.** `nh_roots_v1` = 5,521 (NEW, clean roots, S16) · `nh_reality_core` = 116,391 (OLD index — keep until proven) · `nh_test_asm` = 1,180 · `nh_simulation_core` = 263.

**Source files on disk:** `conversations-000/001/002.json` (all INGESTED CLEAN S12). `gpt_purified_history.txt` + `cleaned_history (1).txt` (NOT ingested — redundant/damaged).

**Models on disk (verified S14/S16):** Ollama `dolphin-llama3:latest` (UNCENSORED, 4.7 GB, 8B — **the chosen mouth**) · `llama3:latest` (4.7 GB, 8B) · `huihui_ai/qwen2.5-abliterate:3b` (1.9 GB — pulled S14 for Hebrew test; read worse than dolphin, NOT adopted). `models\all-MiniLM-L6-v2` (embedding/search + detector embedding model).

**Accretive store + tooling [BUILT & VERIFIED]:**
- **`nh_accretive_store.py`** — restored S12, extended S13, extended S14. Append-only; schema validated before every append. S14 additions: `_check_common`, `_validate_reading`, reading-shaped `append_reading`, `QUARANTINE_READINGS_PATH`.
- **`nh_engine_minimal.py` (S14, NEW)** — Engine A: `read_root(root_id)` → mouth → 12-field reading → quarantine. `run_on_gold()` runs the 8 v1 gold cases. `MOUTH_MODEL` constant = `dolphin-llama3`.
- **`nh_engine_b.py` (S16, NEW)** — Engine B: `read_root_b(root_id)` → `_get_preceding_turns(n=3)` → BACKGROUND prompt → mouth → 12-field reading → quarantine. `run_on_gold()` runs the 7 v2-B gold cases. `MOUTH_MODEL` constant = `dolphin-llama3`. Context = position-based preceding turns from same `source_title`, full content, no truncation.
- **`nh_rebuild_chroma.py` (S16, NEW)** — rebuilds `nh_roots_v1` from clean roots. `--dry-run` flag for 10-root test + retrieval check. Full run: 5,521 roots, 187.59s. Never touches old collections.
- **`test_reading_validator.py` / `test_minimal_engine_dryrun.py` (S14)** — fixture harnesses (temp paths only).
- `nh_ingest_chatgpt.py`, `verify_rt.py`, `nh_log.py`, `nh_probe*.py`, the S13 detector probes (`nh_embed_confirm_speaker.py` = the recipe reference).

**`.cursorrules` v3.1 (in-force):** §6A. **⚠ Still describes the OLD root schema (no role) and the one-gate model — reconciliation owed.** Stale "188 seed records" docstring in `_validate_record` also needs cleanup.

**Out-of-system artifacts (NOT components):** `NH_one_pass_demo.html` (S15-chat) — teaching visualization only; does NOT appear in the status table.

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **★ THE CLEAN ACCRETIVE STORE — 5,521 roots, 7-field, role-carried, SEALED.**
- **★ 2a COMPLETE: two-file routing + sealed roots + the READING RECORD (validator + writer, 12-field contract) — BUILT & VERIFIED (S14).**
- **★ THE GOLD SET v1 — 8 clean-bare cases, SEALED (S14).**
- **★ THE GOLD SET v2-B — 7 context-requiring cases, SEALED (S16).**
- **★ ENGINE A (`nh_engine_minimal.py`) — BUILT & RUN against gold v1 (S14). ~5–6/8.**
- **★ ENGINE B (`nh_engine_b.py`) — BUILT & RUN against gold v2-B (S16). Tested dolphin 8B setup scored 6.5/7; cause of remaining miss not isolated.**
- **★ CHROMA `nh_roots_v1` — BUILT (S16). 5,521 clean roots, `all-MiniLM-L6-v2` embeddings.**
- **★ `nh_rebuild_chroma.py` — BUILT (S16). Dry-run verified.**
- The restored store module + clean ingest pipeline.
- The speaker-detector recipe INVESTIGATED & PROVEN (~94.89%), NOT deployed.
- The OLD REALITY/SIMULATION gate (still runs harmlessly).
- The OLD populated vector memory (~1.78 GB, 116k `nh_reality_core` — keep until `nh_roots_v1` proven).
- Three local models in Ollama (dolphin, llama3, qwen2.5-abliterate-3b).

**Known regression pattern:** verify on disk; the doc's remembered state has been wrong repeatedly.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE — pre-S12, needs reconciliation)

*The in-force ruleset Cursor obeys. §§0–11 IN FORCE; §12 INCOMING. The §0 premise, §0A frame, §3G story rework, §16 model layer, person-boxes, tape, the clean store, the 7-field root, the two-destinations shape, AND the S14/S16 engine code are DESIGN/NEW that EXTEND §7A and the §12 INCOMING block; they do NOT silently rewrite the in-force body. Disk `.cursorrules` is authoritative for the in-force body. Reconciliation to the 7-field root + the reading-record contract is owed.*

---

## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED]

*The DUMB-MACHINERY heart (§0A). Append-only; schema validated before every append; roots file SEALED.*

**★ ROOT record schema (SEVEN fields):** `id` (uuid4) · `subject` · `timestamp` (ISO 8601) · `content` · `re_reads` (list; `[]`=root) · `source_title` (string/None) · `role` (speaker from source; required on new writes).

**★ `subject` FIELD AUDIT (S17):** In v1 roots, `subject` is a provenance/import-batch tag, not a semantic topic. All 5,521 roots use only: `seed:conversations_000`, `seed:conversations_001`, `seed:conversations_002`. `nh_ingest_chatgpt.py` explicitly defines `SUBJECT_TAG` as "provenance tag for this batch." `nh_log.py` confirms: "groups every record by subject (provenance for now; real subjects arrive with the engine)." `read_by_subject()` and `nh_probe.py` actively depend on the field. **Rules:** (1) Do not modify or reinterpret `subject` in existing v1 roots. (2) Document it honestly as a legacy provenance-batch field in v1 despite the misleading name. (3) Future schema version: consider replacing with a clearly named field such as `source_batch` or `provenance_batch` — exact name undecided. (4) If N.H later needs a true semantic subject/topic, design it as a separate field or derived reading-layer object. Do not silently reuse this field. (5) No files or schemas change now.

**★ READING record schema — BUILT & VERIFIED (S14), 12 fields:** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. A reading NEVER copies root text — it points (`reads`). Show = read readings → follow `reads` into sealed roots → stitch. A re-read is a NEW reading beside the old. The validator (`_validate_reading`) gates SHAPE, never confidence: reject malformed, never reject uncertain.

- **`reads`** — list of root id(s), non-empty; the writer verifies each exists in the sealed roots before commit.
- **`meaning`** — the read (string). The honest insufficient-context read ("seen this, couldn't read it") is a VALID meaning.
- **★ `confidence` = a TWO-SLOT OBJECT (S14, DECIDED).** `{ interpretation_confidence, source_reliability }`, never a bare number. `interpretation_confidence` = how sure the engine is of THIS reading (present on every reading; value-form deliberately loose for now). `source_reliability` = how trustworthy the source was — SLOT present from the first reading, VALUE empty/omitted until the engine can honestly judge a source (empty-when-unknown is honest). NEVER blended; confidence never rises from copied error; a reading never inherits a prior's confidence. Story firmness inside `story_layer[].firmness`; retrieval relevance computed at search time, never stored.
- **`role`** — who spoke, from the root.
- **`story_layer`** = a LIST of tellings (clash kept, nothing wins). Each: optional `whose · stance · firmness · telling · theme · when`. Empty list legal. Unknowns OMITTED, never `"unknown"`.
- **`mode`** = `{ label (open word: chat/composed/story/question/…), classification_confidence (local) }`. Not a fixed menu. `classification_confidence` is LOCAL, ≠ top-level confidence.
- **`produced_by`** = reproducibility-grade provenance. `origin` ∈ {observed, imported, simulated, generated, reaction, human_annotation} (REQUIRED). Engine readings carry model/digest/engine_version/prompt_version/config/retrieval_inputs. `human_annotation` readings (gold) carry annotator/when/context_version/change_reason.
- **`schema_version`** = present on every NEW record, `v1` for the first. Un-retrofittable.
- **`derived_from`** = list of parent reading ids; `[]` when fresh from roots.
- **`idempotency_key`** = operation identity, separate from `id`; the writer rejects an already-committed key.
- **`timestamp`** = CREATION time (≠ source/event/ingest).

**★ ON DISK NOW (verified S14/S16):** 5,521 clean root records, SEALED, all `re_reads=[]`. Production readings file ABSENT. Quarantine readings file holds both engine A and engine B gold-run output (test-only). The validator + writer are live; both engines write real readings through them into quarantine.

**No `reason`/`why` field, by design** — the why is shown by what a layer points at; the AI's view is the NOTE (§7B Part 7.5).

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed]

### 7A — THE UNIVERSAL FILTER (operating rules):
R0 reader/layer-er not judge; R0.5 never close the book; R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; R5.5 the affirmation surface is a per-person STORY-layer (six optional parts; absence read ONLY under the §0A guard; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE); R6 memory only ADDS (governs HISTORY; the COMPUTED VIEW decides current use); R7 the membrane; R8 associative bridging; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is.

### 7B — THE MEANING ENGINE (mechanism):
Part 0 THE PURE TAPE (verbatim, append-only, outside memory; capture-exclusions + audited redaction — §0A); Parts 1–2 the chain of webs; Part 2.5 THE STORY-LAYER WEB; Part 2.6 PERSON-BOXES; Part 3 webs combine; Part 4 nightly research (feeds MEMORY, not the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask); Part 6.5 THE WONDER/SIMULATION; Part 7 THE LOG; Part 7.5 THE NOTE/THE WHY.

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots + READING RECORD — ✅ COMPLETE (S14).** → **(2b) the detector — ✅ INVESTIGATED, recipe locked (S13); fallback, not deployed.** → **(2c) THE ENGINE — IN PROGRESS:** A ✅ BUILT (S14) → B ✅ BUILT (S16) → **C (story-layer) NEXT.** C needs story-bearing gold cases before it can be tested. **Build the LIVE path before the nightly deepening.**

**★ THE ENGINE LAYERS:**
- **A (BUILT, S14):** root → mouth ("say what the {role} is doing, don't describe/answer/invent") → 12-field reading → quarantine. Bare; no context, no story. ~5–6/8 on gold v1.
- **B (BUILT, S16):** + preceding turns context — `_get_preceding_turns(n=3)` pulls N roots immediately before the target in the same thread. BACKGROUND/END BACKGROUND prompt framing. Full content, no truncation. Tested dolphin 8B setup scored 6.5/7 on gold v2-B; the cause of the remaining miss has not been isolated — model capability, prompt framing, context format, and run variance remain possible contributors. **Future upgrade: full-thread reading with a larger model + larger context window — must be benchmarked, not assumed.**
- **C (NEXT):** + story-layer reading — fill `story_layer` (whose/firmness/theme). Needs story-bearing gold cases first.

---

## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT

WHY IT EXISTS. N.H currently models what something means, who said it, what story it belongs to, and what memories relate to it. That is a strong foundation. But a person is not only meanings and memories. At every moment a person also occupies a state — emotional, cognitive, bodily, practical — and moves through transitions between states across time, pressure, choices, and consequences. The Living State Web is the name for the future layer that would let N.H model that movement, rather than only interpreting individual messages.

WHAT DEPTH IT ADDS. The current engine reads a root and lays a reading beside it. The Living State Web would eventually allow N.H to understand not only what something means, but: what state may have shaped or accompanied it, what may have changed across relevant states, events, and readings over time, what is currently active and unresolved, what may be reachable from the present state, and what happened after action was taken. That is the difference between a meaning system and a partner that can model a living person moving through time.

CURRENT STATUS. PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT. S17 designed node and edge types, grounding rules, currency rules, action surfacing (§7N), the action-result return path (§7O), and relationships to Computed View, Story Layer, Person-Boxes, authority boundaries, and privacy boundaries. Several domains and all implementation details remain undesigned.

WHAT WAS DESIGNED IN S17 AT THE STRUCTURAL CONCEPT LEVEL.

Node and edge types: state nodes (time-bounded representations of experienced states), transition edges (possible connections between states with evidence), position nodes (simultaneous internal stances), open loop nodes (unresolved items consuming attention), relationship state edges (time-bounded connection states with people), causal hypothesis edges (proposed causal connections, always marked as hypotheses), counterfactual nodes (modeled possible worlds, always separated from actual states), value and constraint nodes (active values, fears, protected boundaries).

Grounding rule: every node carries (a) immediate source object IDs (readings, tellings, clashes, Ness response events, or other explicitly permitted derived objects) and (b) direct root IDs ultimately grounding it. Full derivation chain must remain inspectable. Circular support is forbidden — derived material cannot validate itself without root support. A node may not exist solely because another derived object asserted it. Weak or broken chains produce omission or an insufficiently-grounded marking, never invention.

Currency rule: state existence and currentness are two independent properties. Every state node records evidence time range, `last_supported_at`, currentness status, reason for that status, and rule/version used to assess currency. Six conceptual statuses: `current`, `possibly_current`, `stale`, `currentness_unknown`, `ended_by_evidence`, `superseded_by_evidence`. Time passing may move a node toward stale or currentness_unknown but may never alone mark a state ended. A state may be marked ended or superseded only through relevant new root evidence, a Ness response, or another explicitly authorized evidence-based rule. Different state types use different currency rules — a brief condition and a long-term constraint do not age at the same rate. Currentness is never a hidden decay score.

Action surfacing and return path: designed in full at §7N and §7O respectively. The Living State Web provides the state, open loop, value, and constraint evidence that action surfacing draws from.

RELATIONSHIPS NOW DESIGNED.

Computed View: the Living State Web is one source the Computed View draws from when assembling the current picture. The Computed View's seven-factor ordering and triggered snapshot rules apply when Living State Web material is surfaced.

Story Layer: story tellings are eligible source objects for Living State Web nodes. Tellings supply perspective and theme context. Story Layer rules on circular support and firmness apply when tellings are used as evidence.

Person-Boxes: relationship state edges in the Living State Web point to Person-Box identity anchors. Person-Box confirmation status and merge-proposal rules govern which identity anchor an edge may point to.

Permission and authority boundaries: action possibilities surfaced from the Living State Web pass through the authority system before any execution. §7P governs what may be done with surfaced possibilities.

Privacy boundaries: Living State Web nodes derived from third-party material follow the third-party data rules in §7Q. Pre-retrieval eligibility and pre-output review apply when Living State Web content is shown.

FUTURE DOMAINS — PARTIALLY DESIGNED AT THE STRUCTURAL CONCEPT LEVEL. The following had supporting structures designed in S17 (node types, edge types, currency, or retrieval rules), but their complete behavior, evidence requirements, interaction rules, and update mechanisms are not yet settled: transitions between states and what drives them; multiple simultaneous internal positions; relationship state and relational safety; possible causal chains; counterfactual paths; temporal identity across past, present, and possible future states; the loop act → observed result → reread (§7O); identity continuity across time and contexts (the currency rule supports temporal tracking but does not complete identity continuity design).

FUTURE DOMAINS — NOT YET DESIGNED AT ANY LEVEL: current emotional, cognitive, bodily, and practical state schema; needs, fears, protected boundaries, and active constraints schema; current capacity and cognitive/emotional load (open loop nodes may relate to capacity but are not the same — capacity/load representation is not yet designed); attention and relevance control; purpose-aware reading lenses; a world model beside the self model.

REMAINING UNRESOLVED: exact schema for all node and edge types; minimum evidence requirements and grounding-strength rules; currency time windows and state-type-specific aging rules; transition condition definitions; relevance triggers for condition-based action surfacing; mapping of specific action categories to the four risk levels and category-specific evidence/permission thresholds; detection rules for automatic result detection; confirmation workflow for result connections; attention and relevance control mechanism; purpose-aware reading lenses; world model beside the self model; build order position relative to other components.

HOW IT FITS N.H PHILOSOPHY. The Living State Web maps the state-space and possible movement. It never chooses the path. It never promotes its interpretation into settled truth. Ness remains the decider; the engine remains a helper. These are not new rules — they are the same soul rules that govern every existing layer.

---

## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO GATES. Raw capture and root ingestion are separate. A root cannot be written to the sealed store until all required catalog fields are resolved. Raw material is never destroyed merely because a field is unresolved.

MINIMUM INTAKE ENVELOPE. Every front door must produce the same minimum before the pre-ingest store accepts the capture: (1) one stable unique `capture_id`; (2) the exact raw payload or a stable immutable reference to it; (3) capture timestamp; (4) front-door / source type; (5) payload format or media type; (6) source-provided metadata, preserved without reinterpretation; (7) enough provenance to trace how and where the capture occurred. Front doors may additionally provide any reliable source-derived catalog fields they already know. They must not guess missing values to satisfy handoff.

DESIGN BOUNDARY. `front door = capture and normalize` / `pre-ingest catalog = evaluate completeness and manage resolution`. A front door cannot hand over an unidentifiable blob. A malformed capture that cannot meet the minimum envelope enters an explicit capture-error path with available material preserved. Never silent drop.

PRIVACY AND EXCLUSION PRECEDENCE. The catalog's preservation rules apply only to eligible, non-excluded material. The privacy rules in §7Q override catalog preservation for live credentials, non-negotiable secrets, Ness-configured exclusions, redaction, deletion, and mixed-content separation. When excluded material is present, N.H may preserve only the safe permitted remainder and non-reconstructive exclusion metadata; it must never preserve the excluded content merely to satisfy the catalog's no-silent-drop rule.

PRE-INGEST HOLDING AREA. One unified pre-ingest store. One item, one `capture_id`, one stable location, a list of blockers (e.g. `["speaker_unresolved"]`, `["thread_unresolved"]`, or both). Raw payload never rewritten. Material may remain in `held` indefinitely. Held material is invisible to the Meaning Engine unless an explicitly designed inspection mode says otherwise. One blocked item never blocks unrelated ready items. Silent deletion never permitted. Idempotent: repeated processing never creates duplicate roots. Promotion to the root store is atomic. After promotion, the pre-ingest record stays as provenance with the resulting `root_id` recorded.

LIFECYCLE STATES (conceptual): `held` → `ready` → `promoting` → `promoted`; plus `rejected`/`excluded` (intentional, with reason) and `error` (processing failed, material preserved).

CONCEPTUAL RECORD SHAPE includes at minimum: `capture_id`, raw payload or stable reference, capture timestamp, front-door type, source metadata, proposed catalog fields, blocker list, proposal provenance and uncertainty, resolution history, lifecycle state, resulting `root_id` if promoted.

SPEAKER RESOLUTION RULE. `role` must come from source, not be guessed. Raw capture may happen without a known speaker; root ingestion cannot. Live interactive use: ask Ness when the speaker is necessary and cannot be identified. Unattended processing: hold as `speaker_unresolved`. A speaker detector may propose a candidate — that proposal is uncertain and remains a proposal until confirmed by Ness or supported by source evidence. Never silently promoted into the `role` field.

SOURCE TITLE RULE. `source_title` is a grouping key for Engine B's positional context retrieval. Rules: (1) Source provides a real thread identifier → carry it exactly. (2) Source missing but items provably belong together → one unique non-semantic placeholder per capture session: `untitled:paste:<capture-session-id>`, `untitled:voice:<capture-session-id>`. (3) Isolated item → unique singleton placeholder. (4) Grouping genuinely uncertain → live: ask Ness; unattended: hold as `thread_unresolved`. A machine-generated topic or summary must never become `source_title`. Future schema: separate `thread_id` (stable grouping key) from optional human-readable display label. Sealed roots are never rewritten; later clarification goes through an alias/correction layer (design deferred).

FOUR ENRICHMENT CATEGORIES.

**A. Source-carried facts — accepted as catalog facts.** Sender/speaker, source role, original timestamp, thread/conversation identifier, platform name, source title, message ordering, filename, attachment identifier, source media type. Provenance of each fact recorded.

**B. Deterministic mechanical derivations — allowed.** Content length, file size, checksum/hash, image dimensions, audio/video duration, encoding, normalized format, ordering index, normalized timestamp. Rules: preserve the original source value; store derived value separately; record method and version; never replace original with normalized form; derivation failure does not alter or destroy the capture.

**C. Machine-inferred classifications — proposals only.** Detected language, suspected speaker, probable thread membership, probable duplicate, quoted-text detection, possible continuation. Stored only as proposals with: proposed value, producer/model/rule, evidence, confidence, timestamp, confirmation status. Never becomes a settled catalog fact without confirmation by source evidence, Ness, or an explicitly authorized resolution rule.

**D. Semantic interpretation — forbidden in the catalog.** Topic, intent, emotion, motive, psychological state, importance, relevance, meaning, relationship interpretation, truth judgment, summary, inferred life event, what a person "really meant." These belong to the Meaning Engine, reading layer, story layer, or later systems.

BOUNDARY TESTS. "Does this describe what the material physically/source-wise *is*, or does it explain what the material *means*?" And: "Could two reasonable readers disagree because they interpret the content differently?" If yes to the second, it belongs outside the catalog.

The raw captured payload is never rewritten. Enrichment metadata develops around it. Exact schemas, field names, and which derived values enter the future root schema remain undesigned.

---

## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO CHANNELS, ALWAYS SEPARATE. Positional context answers: "What was happening immediately before this root in the same thread?" Semantic context answers: "What other stored material may relate to this root?" These are different kinds of evidence. A semantically similar memory may come from a completely different time, person, event, or situation. Similarity is not proof of relevance.

Positional and semantic retrieval are separate channels. Every retrieved item carries retrieval provenance: retrieval type, why it was selected, source root ID, source thread/grouping, timestamp, retrieval score or position where relevant. When both are supplied, the prompt structure must show them in separate sections. The model must not be able to mistake a semantic match for a preceding turn. A conflict between positional and semantic context is surfaced, not silently resolved. Semantic retrieval never overrides or silently repairs positional context.

CHANNEL COMBINATIONS. The engine may receive: positional only, semantic only, both channels, or neither — depending on the explicitly designed reading mode.

FOUR CONCEPTUAL MODE CATEGORIES (not final names or settings): bare (no context), local-context (positional only), associative (semantic only), combined (both channels, still separated).

RETRIEVAL PARAMETERS ARE PER-MODE, NOT UNIVERSAL CONSTANTS. Every reading mode explicitly declares its own: positional-context limit, semantic-result limit, semantic threshold or ranking rule, eligible source scope, time range if any, token/size budget, and fallback behavior when insufficient context is found. Parameter values must be tested empirically against gold sets before defaults are locked. Testing must examine reading quality, whether relevant context was retrieved, whether irrelevant context was introduced, whether semantic matches were mistaken for direct context, reproducibility, latency, cost, and sensitivity to changing the limits.

All retrieval is bounded. No mode may request unlimited results. Hard safety ceilings exist above mode-level settings so a configuration error cannot retrieve unbounded material. Exact ceiling values remain undesigned.

Engine B's n=3 remains the configuration of the built Engine B experiment. It does not establish 3 as the universal future positional limit.

AUDIT TRAIL. Reading record must eventually preserve: reading mode, configured parameters, retrieval system/model/index version, exact roots supplied, scores or positions, exclusions or truncation caused by limits, execution timestamp.

GENUINE NO-CONTEXT HANDLING. When retrieval returns nothing because no relevant context exists — first root in thread, or no semantic results above threshold — these are normal conditions, not failures. Engine proceeds with the target root only. Reading record must state: which channel returned nothing, why, that bare fallback was used, that the reading is context-limited and revisable. The system must not invent, lower thresholds silently, or substitute unrelated memories.

SYSTEM FAILURE SEPARATION. Index error, stale/incomplete index, timeout, unreachable service are system failures, distinct from genuine empty results. System must never claim retrieval succeeded when it failed. Exact fallback behavior for system failures remains undesigned.

Trigger conditions for semantic retrieval, exact retrieval limits, ranking methods, thresholds, and safety ceiling values remain undesigned.

---

## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT]

ONE READING PER PASS. One pass, one reading record, one target root. Multiple angles require multiple explicit passes. Every pass declares its reading mode, purpose, or angle. Multiple readings may point to the same root; each is separate with its own context inputs, engine version, configuration, and timestamp. A new reading never overwrites an older one. Conflicts between readings stay visible, never silently merged. Later synthesis is a separate layer and does not rewrite existing readings. The engine must not create hidden secondary interpretations outside the reading record.

ENGINE FLOW. Target root + optional positional context + optional semantic context + declared reading mode → mouth proposal → Reading Proposal Acceptance Check → reading record.

★ FIRST-CLASS PRINCIPLE — MODEL CONFIDENCE IS METADATA, NOT AUTHORITY. This principle applies to all present and future models used inside N.H, regardless of model size, architecture, or claimed capability.
1. Model confidence is metadata, not authority.
2. A confident response may still be wrong, unsupported, or invented.
3. Acceptance depends on grounding in the target root, supplied context, declared reading mode, and explicit evidence — not on what the model claims about itself.
4. Unsupported certainty must be rejected or downgraded by the acceptance layer.
5. Honest uncertainty is preferable to confident fabrication.
6. No reading is accepted solely because the mouth model labels itself confident.
7. The acceptance layer must record why a proposal passed or failed — not just the outcome, the reasoning.

READING PROPOSAL ACCEPTANCE CHECK. An explicit acceptance step runs between the mouth's proposal and the reading record. The mouth does not judge its own output alone.

The acceptance check verifies at minimum: required fields present and valid; meaning grounded in the target root or supplied context; no claims invented beyond available evidence; positional and semantic context not confused with each other; uncertainty expressed honestly; response does not contradict its own evidence; declared reading mode was followed.

A response fails acceptance when it: invents facts, overstates certainty, relies on context not supplied, confuses semantic similarity with direct context, violates the reading mode, is malformed or incomplete, or cannot support a meaningful interpretation from available evidence.

ON ACCEPTANCE FAILURE. The proposal is rejected and the specific failure reason is recorded separately. `insufficient_context` is used only when the available root/context cannot support a grounded interpretation. Fabrication, unsupported certainty, positional/semantic channel confusion, reading-mode violation, malformed output, and incomplete output are recorded as distinct proposal-rejection reasons rather than being mislabeled as context insufficiency. Under a future explicitly designed bounded fallback/retry rule, the engine may make a fresh proposal; if it still cannot produce a grounded reading, it writes the honest revisable `insufficient_context` reading required by the S14 engine-failure rule. The rejected proposal may be preserved in an audit log, but it must never silently become the accepted reading. The engine never invents.

Acceptance result, reasons, validator version, and relevant checks should eventually be recorded for reproducibility. Exact criteria, thresholds, retry behavior, and whether validation uses rules, another model, or both remain undesigned.

STORY-LAYER EVIDENCE RULES. The story-layer pass may retrieve both prior roots and prior readings, but they must remain in separate, clearly labeled context channels.

Two separate context channels for story-layer passes: (1) root evidence channel — original source material, higher evidential status; (2) prior reading context channel — previous interpretations, interpretive status only. Roots and readings must never be merged into one undifferentiated evidence block.

Grounding rule: every story telling must be grounded in supporting root IDs. Prior reading IDs may support continuity, comparison, or discovery, but a telling is never accepted solely because earlier readings stated it.

Circular support is forbidden: a reading cannot become true merely because later readings repeat it; derived material cannot endlessly validate other derived material without root support; an unfinished output from the current pass may not be used as its own evidence; only completed prior readings are eligible.

Conflict rule: conflicting readings remain visible and are not silently resolved. The story layer surfaces clash; it does not arbitrate it.

On weak evidence: if root support is insufficient, the telling is omitted or marked `insufficient_context`. Never invented.

Audit trail: every root ID and reading ID supplied to the story-layer pass must be preserved.

Exact retrieval scope, ranking, limits, and firmness criteria remain undesigned.

---

## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT]

A reread never happens without an explicit recorded reason. Three trigger types are allowed, each bounded.

MANUAL. Ness may request a reread at any time. No further justification required.

CONDITION-BASED. Triggered when materially relevant new information becomes available: new positional context, new root evidence, resolved speaker or thread information, corrected provenance, a newly available required context channel. Time passing alone is not a condition. Any new memory does not automatically trigger rereading everything. Relevance must be established under an explicitly designed rule.

SCHEDULED AUTOMATIC RETRY. Allowed only for temporary system conditions: model/service timeout, unavailable or stale index, interrupted processing, other explicitly retryable technical failures. Not for reinterpretation. Bounded, idempotent, protected against duplicate rereads and endless retry loops.

ON NESS REJECTING A READING. The rejection is recorded. The reading is marked and may become eligible for reread. Rejection does not prove the opposite interpretation is correct.

EVERY REREAD RECORDS. Trigger type, trigger reason, who or what initiated it, new evidence or changed condition, previous reading IDs, new configuration and timestamp.

A reread creates a new reading. It never overwrites, edits, or deletes the earlier reading. A revisable reading may remain unrevisited indefinitely if no trigger occurs.

Exact relevance rules, retry limits, scheduling, and orchestration remain undesigned.

---

## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO VIEWS. Simple by default, complete on demand. Ordering is presentation only — it never resolves conflict or grants authority.

CURRENT VIEW (default). In a simple per-root reading list, surfaces the newest usable reading first. Usable = passed acceptance, not marked rejected or `insufficient_context`. This does not mean it is true or final. Conflicts must be surfaced explicitly — for example: "A conflicting reading also exists." Revisable, rejected, and insufficient-context readings remain visible with clear labels. Whenever the interface claims to show the **current best-supported** reading or assembles a broader current picture, §7M's seven-factor ordering governs; recency is only a limited tie-breaker.

HISTORY VIEW (complete record). Every reading in strict chronological order. Ness may switch to it at any time. Always available, never hidden.

STANDING RULES. No reading is deleted, hidden permanently, or overwritten. Different reading modes may be grouped separately when helpful, but the original chronology remains available. Ordering is presentation only. Newest reading shown first does not make it authoritative, correct, or final. Simple by default, complete on demand.

Exact grouping rules, labels, interface layout, and definition of "current usable reading" remain undesigned.

---

## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT]

SIX CLASH TYPES.
1. **Direct contradiction** — two readings of the same root produce mutually exclusive meanings.
2. **Interpretive divergence** — same evidence, different conclusions, neither strictly excludes the other.
3. **Temporal change** — inconsistency between readings at different times that may reflect genuine change, not error.
4. **Perspectival difference** — different speakers' or observers' framings of the same event, each accurate within its own perspective.
5. **Evidence insufficiency** — conflict because neither reading had enough context to be reliable.
6. **Context mismatch** — apparent contradiction from different reading modes or retrieval configurations, not a real conflict in the material.

GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE. Core test: could both statements be simultaneously true under the same conditions, for the same person, at the same time, in the same context? If yes — contextual difference. If no — genuine contradiction. N.H records the distinction, never resolves it.

CLASH RECORD SHAPE (conceptual). Stable identifier, clash type, pointers to exact readings and roots involved, description of what specifically conflicts, retrieval configurations and reading modes of conflicting readings, detection mode, confidence of clash detection, lifecycle state, Ness response status, timestamp. Every clash record points to the exact supporting roots and readings. Original roots and readings remain unchanged.

TWO DETECTION MODES, SAME RECORD TYPE.

Triggered detection: runs when a new reading is written. Compares against readings of the same root, readings in the same thread, and other explicitly related readings.

Periodic or on-demand detection: scans wider scope — across roots, threads, people, time periods, story layers. Catches slow-developing and cross-thread contradictions.

Both modes produce the same conceptual clash-record type. Every clash record states its detection mode. The same clash must not produce two independent records — later detection appends a new detection-history event linked to the existing clash. Wider scans may append evidence or propose a refined classification through linked events, but they do not mutate the original clash, rewrite original readings, or spawn duplicate clashes. Detection mode does not affect authority. Neither mode may resolve, rank, or select a winner. Periodic scans are bounded and configurable.

NESS'S RESPONSE AS SEPARATE EVENT. Every response has its own stable event ID and points to the clash ID. It does not live inside the clash record. Every response event records: response type, Ness's exact statement or selection, timestamp, evidence or explanation supplied, any requested downstream action.

Response types include: one reading accepted over another, both valid in different contexts, genuine change over time, insufficient evidence to judge, detection artifact, deferred judgment, request for reread, or another explicitly defined type.

Ness may respond multiple times. Later responses do not erase earlier ones. Full response history always preserved. Current view may show the latest Ness response; full response history available on demand.

Downstream actions are separate linked records. A response event and the action it triggers are distinct records that point to each other. Ness choosing one reading does not delete the other — his judgment is recorded and may affect the computed view or presentation. It does not alter the underlying readings, roots, or clash record.

A clash is not automatically an error. N.H never silently resolves it. Exact schemas, detection methods, schedules, deduplication logic, and downstream effects remain undesigned.

---

## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Receiving tellings produced by engine passes and recording them without alteration. Organizing tellings by whose perspective they reflect, what theme they belong to, and when they were produced. Surfacing how a narrative thread has developed, shifted, or fractured across time. Preserving clash between tellings without resolving it. Making it possible to ask: what has been said about this person, theme, or period — and from whose perspective, with what firmness, supported by what roots. Distinguishing temporal change from contradiction. Keeping each person's story separate from every other person's.

MUST NEVER. Merge conflicting tellings into one synthesized narrative. Promote a repeated telling into established fact merely because it appears often. Assign a single authoritative story to a person, relationship, or event. Invent connective tissue between tellings that the roots do not support. Treat a gap in tellings as evidence of absence. Flatten temporal change into a single stable description. Allow one person's perspective to silently overwrite another's. Resolve whose telling is correct — that is Ness's judgment, off-board.

TELLING VS ONGOING STORY. A telling is one interpretation, produced in one engine pass, about one root, from one perspective, at one moment — local, bounded, specific. An ongoing story is the collection of tellings across time — with agreements, shifts, contradictions, silences — organized so that patterns can be seen without being hardened into conclusions. The story layer can surface the sequence; it cannot conclude from it.

CONNECTIONS ACROSS TIME. Tellings connect through explicit shared attributes: same `whose`, same theme, same thread or source, overlapping time period, or shared root IDs. These are navigational links, not logical merges. Always labeled with what they are based on, always pointing back to supporting roots and readings.

STRUCTURED PERSPECTIVE MODEL. Three minimum fields per telling:
- `root_speaker` — who produced the source root.
- `subject` — who or what the telling is about.
- `perspective_owner` — whose viewpoint, belief, feeling, or framing the telling claims to represent.
Optional: `attribution_path` — used when perspectives are nested (e.g. `friend → quoted by father → reported by Ness`). Populated only when the root supports the chain. Never invented.

These roles may refer to the same person or different people. The Story Layer never assumes the root speaker is automatically the subject or perspective owner. Evidence relationship must be recorded for every telling: direct self-report, direct quotation, reported speech, observation, or engine inference. Reported speech is not direct access to the reported person's internal state. The engine's interpretive lens stays separate from the human perspective represented in the telling. Unknown attribution stays explicitly unresolved. Existing flat `whose` field may remain for v1 compatibility; future schema should use the structured perspective fields.

OBJECT-IDENTITY SEAM — EXPLICITLY UNRESOLVED. In the built v1 reading schema, tellings are embedded entries inside the reading record's `story_layer` list; no separate first-class telling record is built. S17 treats a telling conceptually as something other components may link to, but it did not choose its future storage identity. Before Story Layer, Person-Box, clash, or deletion code relies on telling-level links, one identity method must be designed explicitly: either a separate immutable telling record or a stable composite reference within its immutable parent reading. This master does not choose between those options, and no implementation may assume standalone telling IDs until that seam is settled.

FIRMNESS RULE. Firmness and model confidence are separate dimensions. `firmness` = how strongly the perspective owner appears to hold the stance. `confidence` = how well-grounded the engine believes its reading to be. These are independent.

Firmness may be inferred from observable signals: explicit certainty words, hedging, repetition, emphasis, consistency within the root, direct statements of commitment or doubt. Every firmness value records its evidence basis. Firmness is always provisional and revisable. Direct self-report of certainty is stronger evidence than tone, wording style, or repetition alone. Reported speech or uncertain attribution lowers evidential strength. N.H must never present firmness as direct access to a person's internal state. Conflicting signals produce mixed firmness, uncertain firmness, or omission — never a forced resolution. If the root does not support a firmness judgment, the field is omitted. Exact scale, labels, thresholds, and scoring method remain undesigned.

HYBRID THEME SYSTEM. Engine proposes freely. Only Ness confirms. Confirmed themes are navigation categories, never facts.

Engine-proposed themes start as `proposed`, never as settled categories. May be generated from a single telling or patterns across multiple tellings. Every proposed theme records: supporting root IDs, supporting telling/reading IDs, who or what proposed it, why those items appear connected, timestamp, uncertainty.

Ness may: confirm, rename, merge, split, reject, or leave a proposed theme unresolved indefinitely. Unresolved proposed themes do not become confirmed by aging or repetition.

A telling may belong to no theme, one theme, or multiple themes. Membership is not exclusive. Circular support is forbidden — pattern-derived themes must retain root support. Repetition does not confirm. A theme cannot validate itself by being frequently proposed.

Proposed themes must not silently shape future readings. If a confirmed or proposed theme is used to retrieve context for a future engine pass, that influence must appear in the retrieval audit trail. Future readings may challenge, omit, or contradict an existing confirmed theme.

Ness-controlled vocabulary is open and extensible. Theme aliases may connect different labels across time without rewriting older tellings. Exact theme schema, similarity grouping, confirmation process, and retrieval influence remain undesigned.

---

## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT]

RESPONSIBILITIES. Maintaining a stable identity anchor for a person. Linking roots where this person appears, is mentioned, is quoted, or is the subject of a telling. Linking readings and tellings that involve this person in any perspective role. Linking clashes that involve this person. Linking Ness's responses where relevant. Recording how each link was established and how certain it is. Tracking proposed identity connections without silently merging them. Surfacing what has changed over time about how this person appears across the store.

MUST NEVER. Synthesize linked material into a summary description or personality profile. Promote a frequently appearing interpretation into a settled fact about the person. Treat a report about someone as equivalent to that person's own perspective. Merge two uncertain identity references without explicit resolution. Treat absence of information as evidence of anything. Resolve contradictions between tellings. Allow one perspective owner's framing to silently become the authoritative view of the subject. Invent connections not explicitly supported. Become a diagnosis, personality model, fixed character description, or closed identity. Claim to represent what a person is like — only what N.H has observed or been told, from whom, with what certainty, at what time.

LINKABLE OBJECT TYPES. Roots, readings, story tellings, themes (with confirmation status), clash records, Ness response events, other Person-Boxes (where identity connection proposed or confirmed), and **metadata-only** references to pre-ingest records where the person appears. Held pre-ingest raw content remains invisible to Person-Box semantic analysis unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be linked. Every link records: what it connects, why, who or what established the connection, certainty, and timestamp. Links are never copies — the original object stays where it is.

UNCERTAIN IDENTITY. Uncertain identity is the normal state. A reference anchor records: the label or name used, where it appeared, when, what evidence connects it to a specific person, and current certainty level. Multiple anchors may exist for what might be the same person. They remain separate until a resolution rule — Ness confirmation, strong source evidence, or another explicitly authorized rule — merges them.

PROPOSAL-BASED CREATION. N.H may detect a new person reference and create a proposed identity anchor, but it must not silently create a confirmed Person-Box or decide that two references are the same person.

Every Person-Box has a stable system-generated ID. Human-readable names, labels, and roles attach separately and may change. A new unrecognized reference may generate a proposed anchor when encountered through a front door, root, reading, story telling, or other authorized source. A proposed anchor is not a confirmed Person-Box.

Before proposing a new anchor, N.H must search: confirmed Person-Boxes, unresolved identity anchors, aliases, and previous merge proposals. Similar names or labels alone are not sufficient to merge. Possible duplicates produce a separate merge proposal, never a silent merge.

Ness may: confirm, reject, rename, keep unresolved, link to an existing Person-Box, or propose a merge. Strong source evidence may confirm identity only under an explicitly authorized resolution rule.

Confirmed merge: links identity anchors under one stable identity view. Does not rewrite roots, readings, tellings, or historical links. If a merge is later found wrong, correction is recorded through new events or links. History is never rewritten.

Unresolved references may remain separate indefinitely. Exact matching rules, evidence thresholds, confirmation workflow, and merge mechanics remain undesigned.

DEFAULT VIEW. Seven separate sections: roots, readings, story tellings, clashes, Ness response events, themes, unresolved identity anchors and merge proposals. Every section states what it contains and its evidential status. These are never visually flattened into equivalent claims. Section order is navigation only — not authority, reliability, importance, or truth. Frequency and recency do not silently determine reliability.

Ness may filter or reorganize by: time, perspective role, theme, source/thread, lifecycle or confirmation status. Full chronological view always available. Conflicts, unresolved identity questions, and uncertain links surfaced clearly. Simple by default, complete on demand.

Exact layout, section order, filters, and labels remain undesigned.

---

## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The present-facing surface of N.H. Its job is to take all accumulated material and produce a navigable, useful picture of what N.H currently has reason to show, without altering any underlying objects or pretending that one interpretation has won.

RESPONSIBILITIES. Assembling the most useful current picture using explicit derivation rules. Surfacing the current best-supported reading for a root, story thread, person, or theme while preserving access to alternatives and history. Reflecting Ness's explicit responses without treating them as rewrites of history. Distinguishing evidence, engine interpretation, Ness's explicit judgment, and unresolved material. Updating automatically when triggered. Preserving a record of what the view showed at previous points in time.

MUST NEVER. Rewrite, alter, merge, or delete any root, reading, telling, clash, or response event. Silently select one reading as authoritative. Treat most recent or most frequent interpretation as more reliable without explicit justification. Present engine inference as settled fact. Present Ness's response as a rewrite of history. Suppress conflicts. Store new interpretations. Decide what is true.

OBJECT TYPES USED. Roots, readings, tellings, clashes, Ness response events, Person-Box links, themes, and **metadata-only** pre-ingest references. Held pre-ingest raw content must not influence Computed View ranking, interpretation, or output unless an explicitly authorized inspection mode is later designed; only safe source-carried metadata, lifecycle state, and blocker information may be surfaced. All objects are linked, never copied.

SEVEN-FACTOR PRIORITY ORDER (explicit, no hidden truth score):
1. Ness's explicit current judgment, when relevant.
2. Strength and directness of supporting root evidence.
3. Acceptance status and grounding quality of readings.
4. Relevance to the current question or view purpose.
5. Context quality and retrieval provenance.
6. Active clashes, unresolved uncertainty, and contrary evidence — surfaced beside the item, not suppressed.
7. Recency as a limited tie-breaker only. Never as authority.

Every surfaced item must state why it was prioritized. No single hidden score may collapse evidence, interpretation, judgment, and uncertainty into one number. Direct root support outranks repetition, frequency, or model confidence. A highly supported item with an active clash must display the clash beside it. The view must be able to say "no clear current view" when support is too conflicted or weak.

DECLARED ORDERING PROFILES. Different view purposes may use different profiles — current situation, person-focused, project-focused, historical review, or others. Each profile discloses its ordering rules. Alternatives and full provenance remain accessible from any profile.

UPDATE TIMING. Triggered updates, not continuous recomputation. Three update triggers: (1) Ness opens the view; (2) Ness manually requests a refresh; (3) a materially relevant event occurs — new accepted reading, new or changed active clash, Ness response event, confirmed theme or identity resolution, or another event explicitly defined as relevant to that view profile. Unrelated new material does not force every Computed View to recalculate.

Every completed update creates a new immutable snapshot. Previous snapshots remain accessible and never overwritten. Every snapshot records: update trigger, view profile, source objects used, derivation-rule version, timestamp, what changed from the previous snapshot, and why it changed. Normal interface shows the newest valid snapshot. If an update fails, the last valid snapshot remains visible, clearly marked as possibly stale. Failure is never silently treated as a successful refresh. The view may state that nothing materially changed — a null update is a valid outcome.

Exact relevance rules, significance thresholds, refresh scheduling, and snapshot schema remain undesigned.

---

## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT]

PERMISSION-CONTROLLED HYBRID. N.H surfaces possible actions when asked or when an explicitly authorized relevance rule applies. Never instructions. Never decisions. Ness remains sole decision-maker.

TWO SURFACING MODES. (1) On explicit request from Ness — always permitted. (2) Proactive — permitted only when an explicitly authorized relevance rule says the possibility is useful enough to show. Controllable by Ness's settings. May be disabled entirely.

Every surfaced possibility is labeled as derived, not instructed. Required language: "one possible option," "this may be reachable," "you could consider." Prohibited language: "you should," "you need to," "you must."

Every possibility records: the state, open loop, value, constraint, or evidence it was derived from; why it may be reachable now; important assumptions; uncertainty; possible limitations or risks.

Ness may: accept, reject, modify, postpone, ignore, or ask for alternatives. All responses are valid. Ignoring or rejecting a suggestion is never treated as failure, resistance, or evidence against Ness. No repeated surfacing of the same suggestion without a new request, materially changed evidence, or another explicitly authorized trigger.

Weak, conflicted, stale, or insufficient evidence: N.H either withholds the suggestion or labels it clearly as uncertain. Higher-impact actions require stronger permission and review rules than small reversible actions. The four risk levels are defined in §7P; what remains undesigned is the mapping of specific action categories to those levels, category-specific evidence and permission thresholds, and interface wording.

A surfaced possibility is not an action record until Ness chooses or performs something. The suggestion and any later real action remain separate linked objects.

NESS-RESPONSE STATES FOR SURFACED POSSIBILITIES (before or instead of execution):

- **Accepted and acted on** — Ness confirms and performs or authorizes the action. A new action record is created. The possibility and action record are linked but remain separate objects.
- **Rejected** — recorded as a rejection event pointing to the possibility. Not treated as failure, resistance, or evidence against Ness. The possibility is not resurfaced without a new trigger.
- **Modified** — Ness changes the scope, target, or form of the suggestion before acting. The modification is recorded. The modified version becomes the basis for the action record, not the original suggestion.
- **Postponed** — recorded with a reason if given. The possibility remains eligible for resurfacing only when a new trigger or request occurs. Time alone does not resurface it.
- **Ignored** — no response event required. The possibility is not resurfaced without a new trigger.
- **Alternative requested** — Ness asks for different options. A new surfacing pass is initiated. Prior suggestions remain in record but are not repeated in the new pass.

Exact relevance triggers, mapping of specific action categories to the four risk levels, category-specific evidence and permission thresholds, and interface wording remain undesigned.

---

## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT]

TWO RESULT TYPES, KEPT SEPARATE. Neither grants direct system access to reality.

EXPLICIT REPORTED RESULT. Ness directly reports what happened through a normal front door. Enters catalog and ingestion as normal — becomes a root only after standard checks. Labeled as Ness's report of the result. Not direct system observation of reality.

DETECTED POSSIBLE RESULT. N.H notices incoming material that may relate to an earlier action. Creates a proposal linking new material to the action. Never silently declares the material is the action's result.

Every possible-result proposal records: action ID, new root or capture ID, why they may be connected, timing, uncertainty, alternative explanations, who or what detected the connection.

Ness may: confirm, reject, modify, or leave the proposed connection unresolved indefinitely.

CAUSATION RULES. Timing alone does not prove causation. Similarity alone does not prove an observed event resulted from the action. Confirmation of a result connection does not automatically confirm why it happened.

THREE SEPARATE LINKED OBJECTS. Action record, result root, connection between them. Never merged.

N.H must distinguish: (1) the observed or reported event; (2) the claim that it resulted from the action; (3) interpretations of what that result means.

A confirmed result connection may trigger: reread, state update, open-loop update, or another explicitly designed process. Automatic detection may be disabled or restricted by Ness.

SIX RESULT STATES:

- **Success** — the action may have produced the expected or intended effect. Success may be recorded as confirmed when Ness confirms it. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with the intended effect, but this remains a revisable interpretation and does not establish causation. The observed event, the inferred relationship to the action, and Ness's confirmation or judgment remain separately represented.
- **Partial success** — may be recorded as confirmed when Ness confirms that some but not all intended effects occurred. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with partial success, but this remains a revisable interpretation and does not establish causation. The record describes what appears achieved and what appears unmet while keeping the observed outcome, the proposed relationship to the action, and Ness's judgment separately represented. Does not automatically trigger a retry.
- **Failure** — may be recorded as confirmed when Ness judges that the intended effect did not occur or that the result was negative. Without Ness's confirmation, N.H may record that the observed outcome appears consistent with failure, but this remains a revisable interpretation and does not establish causation. The observed outcome, the proposed relationship to the action, and Ness's judgment remain separately represented. Does not automatically trigger a retry or a new surfaced suggestion. Ness decides what to do next.
- **Cancellation** — the action was authorized but stopped before completion, either by Ness, by a pre-authorized emergency stop, or by a system condition. The cancellation is recorded with its trigger, reason, and the state of the action at the point of cancellation. Partially completed effects are recorded separately from intended effects.
- **No result or unknown result** — the action was taken but no observable result has arrived or can be confirmed. Recorded as result-unknown. Any open loop or state node remains active and marked with uncertainty. The system does not assume success or failure. Time passing alone does not resolve this.
- **Incorrect or disputed result linkage** — a proposed connection between a result and an action is found to be wrong, contested by Ness, or contradicted by later evidence. The incorrect linkage is recorded as a rejected connection event. The action record and result root remain as separate objects. A corrected linkage may be proposed. The original action record is never rewritten to remove the disputed connection — the dispute is recorded alongside it.

Exact detection rules, confirmation workflow, classification criteria and subcategories within the six result states, and downstream triggers remain undesigned.

---

## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT IS. The formal boundary between N.H as a helper and N.H as an actor in the world. Defines what N.H may do on its own, what it must prepare and show before doing, what it must ask Ness before doing, and what it may never do regardless of any instruction.

MUST NEVER ALLOW. N.H acting on the world without recorded authorization. Silence, absence, or non-response interpreted as consent to act. A permission granted for one action being silently extended to a different action. Past permission automatically remaining valid for future similar actions. N.H proceeding when its authority level is unclear. Preview being skipped for actions requiring approval. An irreversible action taken on the basis of reversible-action authorization. Cascading permissions. N.H deciding what counts as a successful result of an action it took.

THREE ACTION STATES WITH DISTINCT AUTHORITY REQUIREMENTS.

**Suggesting** — N.H surfaces a possibility for Ness to consider. No external effect, external write, or execution occurs. Authorized Level 1 internal read-only retrieval may occur to derive the possibility, but no message is sent, no external account or system is changed, and no executable action is staged. Lowest authority level; always permitted within action-surfacing rules.

**Preparing** — N.H assembles something ready to act but not yet acted. A draft exists but has not been sent. A change is staged but not saved. The prepared object is real and inspectable but no external effect has occurred. Ness reviews before anything is committed. Requires higher authority than suggesting. Must be shown to Ness before execution.

**Executing** — N.H takes an action with real-world effect. Something irreversible may have occurred. Requires the highest authority level, explicit prior approval for the specific action, and a complete record of what was done. The boundary between preparing and executing is: has anything outside N.H changed? If yes, execution has occurred.

FOUR RISK LEVELS.

**Level 1 — Internal read-only.** N.H accesses its own stores, indexes, and records. No external effect. No change to any object. Autonomous within normal operating parameters.

**Level 2 — Internal write.** N.H writes a new reading, appends a new state node, state-version, or currentness event, creates a clash record, or produces another derived object inside its own stores. Existing state nodes and other historical records are not modified in place. Append-only operations at this level are lower risk than modifying existing objects. Autonomous within established schema and validation rules for normal append operations; flagged for any exceptional operation that would alter an existing record.

**Level 3 — Prepared external action.** N.H drafts, stages, or assembles something intended to have external effect. The prepared object is shown to Ness before anything is committed. Ness must explicitly approve before execution. Silence is not approval.

**Level 4 — Executed external action.** N.H takes an action with real-world effect. Requires explicit prior approval for the specific action, a pre-execution preview, and a post-execution record. Irreversible actions require additional confirmation. Actions in heightened-risk categories require their own special boundary rules regardless of whether they appear small or reversible.

TWO AUTHORITY LAYERS.

**Layer 1 — Standing permissions.** General abilities Ness enables or disables. May authorize: Level 1 internal read-only, normal validated Level 2 append-only internal actions, Level 3 preparation within clearly defined boundaries. Cannot silently authorize broad categories of external execution.

**Layer 2 — Moment-level approval.** Permission for one specific action at one specific moment. Required for Level 4 external execution after Ness sees the exact action preview. Preparing something does not authorize executing it.

RECURRING EXECUTION AUTHORIZATION. Ness may create a narrowly scoped recurring authorization, but it must explicitly define: exact action type, destination or recipient, frequency or trigger, content or value limits, permitted tools, start and expiry conditions, audit and notification requirements, and how it can be paused or revoked. It is its own recorded authority object — not inferred from general settings or past approvals. Actions outside its exact scope require new approval.

ABSOLUTE BOUNDARY — ALWAYS REQUIRES SPECIFIC PER-INSTANCE CONFIRMATION REGARDLESS OF STANDING PERMISSIONS. Medical, legal, financial, privacy-sensitive, relationship-affecting, destructive, or irreversible actions.

STOP CONDITIONS. Changed conditions, ambiguity, expired permission, or unexpected output require N.H to stop and seek reconfirmation before proceeding. Silence is never approval. In any layer, at any level.

AUTHORITY VIOLATION AND CORRECTION RULE.

Stop-and-surface is the default. On detecting a violation or unexpected result, N.H must immediately: stop all related autonomous action; prevent any further steps in the same action chain; record the full event (what was intended, what actually happened, the authority N.H believed it had, where the boundary was crossed, what unexpected result occurred, what is known/unknown/still changing, which tools and external systems were involved); surface the event clearly to Ness without minimizing, hiding, or reframing it; present possible corrective actions separately as proposals.

Ness's approval required before: reversal, compensation, follow-up communication, deletion, restoration, or any other real-world corrective action.

Corrective action is a new action with its own risk level, preview, permission requirement, execution record, and possible consequences. It is never automatically authorized by the fact that it is corrective.

N.H must never assume that reversal restores the original state completely. N.H must never mark the incident resolved merely because a reversal attempt succeeded technically.

FIVE SEPARATE LINKED OBJECTS. Original action, violation record, corrective proposal, approved correction, observed result. Never merged.

NARROW PRE-AUTHORIZED EMERGENCY STOP EXCEPTION. Permitted only when all five conditions are met simultaneously: (1) the original action is still actively in progress; (2) stopping prevents additional effects rather than undoing completed effects; (3) the stop mechanism is mechanically bounded and previously authorized; (4) stopping cannot reasonably create a larger consequence than continuing; (5) the emergency stop and its authority basis are immediately recorded and surfaced to Ness.

This exception explicitly does not permit: recalling or deleting a completed message, restoring or modifying external data, sending an apology or explanation, making a compensating payment, contacting another person, or any other completed-world reversal without Ness's approval.

Exact permission categories, authorization object schema, and interface remain undesigned.

---

## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT]

WHAT IT GOVERNS. What N.H may capture, how it classifies and protects sensitive material, who and what may access it under what conditions, what appears in views and chat, and what happens to material when Ness removes, restricts, or deletes it. Operates at every stage: before capture, during storage, during retrieval and display, and during deletion.

MUST NEVER ALLOW. Capturing material that was explicitly excluded at the front door. Storing credentials or secrets in plain recoverable form anywhere. Surfacing sensitive material merely because it is relevant. Retaining deleted material through any indirect path. Allowing derived objects to preserve the content of deleted roots after deletion is confirmed. Treating a deletion marker as equivalent to actual deletion. Displaying another person's sensitive information without an explicitly designed rule authorizing it. Permission to store being silently extended to permission to analyze, simulate, display, or share. Partial deletion claimed as complete. N.H confirming deletion when it cannot verify that deletion was carried out in all relevant locations.

FIVE OPERATIONS — DISTINCT, NOT INTERCHANGEABLE.

**Exclusion** — material never enters N.H at all. Filtered at the front door before capture. Cleanest boundary because there is nothing to manage afterward.

**Hiding** — material exists in the store but is not displayed in normal views or surfaced in retrieval. A presentation rule, not a data operation. Reversible without data recovery.

**Restriction** — material exists and may be physically present, but access is limited by explicit rules. More granular than hiding, more targeted than deletion.

**Redaction** — specific content within a root or derived object is removed or obscured while the containing record remains. The sensitive portion is removed and replaced with a tombstone or placeholder. Must propagate to derived objects that contained the redacted content.

**Deletion** — the root and all material derived from it are removed from every location. A tombstone record may remain to preserve that something was deleted, when, and by what authority — without preserving the deleted content. Deletion is the strongest operation and the hardest to verify as complete.

FOUR SENSITIVITY LEVELS.

**Level 1 — General personal.** Everyday conversation, preferences, projects, general life events. Standard N.H privacy rules apply.

**Level 2 — Sensitive personal.** Health information, financial details, relationship difficulties, emotional material, and things Ness has explicitly marked as private. For Ness's authenticated private use, this material is eligible by default unless Ness explicitly restricted or hid it, it was excluded/redacted/deleted, an unresolved deletion case applies, it contains non-negotiably excluded secrets, or another explicit compartment rule applies. External exposure, shared screens, exports, tool use, notifications, and secondary uses require explicit authorization under the two-stage access-control rules below.

**Level 3 — Third-party and relationship data.** Information about other people. Requires separate rules from Ness's own data because other people did not consent to being in N.H.

**Level 4 — Credentials, secrets, and high-harm material.** Authentication material, passwords, keys, financial credentials. Must never enter normal stores. If encountered at capture, must be excluded or immediately isolated.

DELETION AS BLOCKING, VERIFICATION-BASED OPERATION. N.H may confirm complete deletion only when every known location has been removed or verified clean.

A deletion request creates a deletion case with a complete dependency and location search. N.H must identify and check: the original root, direct readings, story tellings, state nodes, clash records, Computed View snapshots, Person-Box links, indexes, embeddings, caches, temporary processing files, exports, backups, model-context records, and any other known derivative or storage location. Indirect traces must also be searched: quotations, paraphrases, summaries, semantic representations, inferred states grounded partly in the root, copied text without a preserved source link.

Every identified derivative must be deleted, redacted, rebuilt without the deleted source, or explicitly marked unresolved if safe removal cannot yet be verified. Multi-root derived objects may be recomputed without the deleted root only if the deleted content is no longer recoverable from them, their meaning is re-evaluated without that evidence, and their provenance records that they were rebuilt. Embeddings and indexes derived from deleted content must be removed and rebuilt where necessary. Backups follow an explicit deletion or expiry process.

FIVE DELETION OUTCOMES.
- `verified_complete` — every known location and derivative removed or safely rebuilt and verified. The only outcome that may be described as complete deletion.
- `completed_with_declared_limits` — removed from all controllable locations; one or more locations cannot be fully verified.
- `incomplete` — one or more identified traces remain.
- `blocked` — deletion cannot safely proceed yet.
- `failed` — an attempted deletion operation failed.

For every outcome other than `verified_complete`, Ness must be told plainly: what was removed, what remains, what could not be checked, why, whether the remaining trace is accessible or usable, and what further action may be possible. N.H must never confirm deletion merely because the root record is gone. N.H must never hide uncertainty behind the phrase "best effort."

A content-free tombstone may remain containing only: deleted object identifier, deletion time, deletion authority, deletion outcome, verification record. No deleted content, no reconstructive metadata.

While a deletion case remains unresolved: affected material must be immediately prevented from retrieval, display, analysis, simulation, or use in new derivations.

CAPTURE EXCLUSION — TWO-LAYER SYSTEM.

**Layer A — Non-negotiable core.** Narrow by design. Covers material that could directly grant access or cause immediate serious harm if stored: passwords, private cryptographic keys, authentication tokens, recovery codes, one-time security codes, payment-card security codes, and equivalent live access credentials. Must never enter root stores, readings, indexes, embeddings, caches, logs, model context retained by N.H, or normal backups. Cannot be disabled by Ness for normal N.H memory stores. A dedicated secrets vault, if ever built, is a separate system with separate authority, encryption, access, and deletion rules.

**Layer B — Ness-configured exclusions.** Rules Ness controls and can extend, narrow, pause, or remove. May be based on: content category, person, source, date range, front door, project, sensitivity, or intended use. May specify that material should be fully excluded, held for review, entered only after confirmation, entered with specified parts redacted, or entered under immediate restriction. Sensitive but context-dependent material — medical details, childhood memories, third-party information, relationship material, emotional disclosures — must not be placed in the non-negotiable core merely because it is sensitive. These require explicit handling rules but are not automatically excluded in every context.

Mixed-content capture: when one input contains both permitted and excluded material, N.H must isolate and remove the excluded portion, preserve the permitted portion when safe, record that exclusion occurred without recording the excluded content, and tell Ness what category of material was removed. If safe separation is not possible, the entire capture is held before ingestion and Ness is asked what to do. Ambiguous suspected secrets enter a protected pre-ingest hold, not normal memory, until classified. Exclusion happens as early as technically possible at every front door. Exclusion event records may retain only non-reconstructive metadata: time, front door, exclusion category, rule used, outcome. Never the excluded content itself.

THIRD-PARTY DATA RULES.

Universal minimum baseline — applies to every person other than Ness without exception: preserves source and speaker of third-party material; distinguishes the person's actual words or actions from Ness's interpretation and N.H's interpretation; does not present inferred feelings, intentions, diagnoses, motives, or private states as facts; does not share third-party material externally without Ness's specific authorization; does not use third-party material merely because it is relevant; does not silently expand one piece of information into a fixed profile of the person.

Context-sensitive rules above the baseline may vary based on: relationship to Ness, amount and frequency of data, sensitivity, source and front door, whether the person spoke directly or was described by someone else, whether content was private/public/forwarded/recorded/inferred, age or vulnerability, and intended use. Relationship closeness does not reduce protection automatically. A close family member appearing frequently may require stronger safeguards because more material exists.

Ness may configure person-specific or group-specific rules covering permitted storage, retrieval, display, analysis, simulation, retention, redaction, restriction, or exclusion. Configuration may make protections stricter. It may not remove the universal baseline.

Four separate operations with increasingly stronger privacy requirements: (1) understanding Ness's experience of another person; (2) recording what that person actually said or did; (3) interpreting what the person may have meant; (4) constructing a model of the person. N.H may normally perform the first. Each subsequent operation requires stronger authorization.

Third-party simulations must never be presented as the real person. Always labeled as bounded hypothetical models derived from limited material, with uncertainty and missing information visible. Minors and highly vulnerable people receive stronger default restriction. Large-volume imported third-party data does not become fully usable merely because it was imported. Public availability does not automatically authorize unrestricted storage, combination, profiling, or simulation.

TWO-STAGE OUTPUT ACCESS CONTROL.

★ CENTRAL RULE. Private access for Ness is open by default unless Ness explicitly restricts it. External exposure and secondary uses are restricted by default.

★ N.H may use material when the current purpose is authorized by Ness. It blocks material from unauthorized uses, not from Ness's own understanding by default.

**Layer 1 — Pre-retrieval eligibility control.** Before material becomes a retrieval candidate, N.H checks whether it is eligible for the current operation and purpose. For Ness's authenticated private use, material is eligible by default. N.H does not remove material from Ness's private self-understanding merely because it is sensitive, emotional, medical, traumatic, sexual, relationship-related, controversial, or uncomfortable. Third-party involvement does not automatically block Ness from understanding his own experiences. "Sensitive" alone is never a sufficient reason to withhold information from Ness. Material is blocked from Ness's private use only when: Ness explicitly restricted or hid it; it was excluded, redacted, or deleted; a deletion case remains unresolved; it contains live credentials or non-negotiably excluded secrets; a specific compartment rule applies; or another explicit rule chosen by Ness applies. For other purposes — external sharing, tool use, exports, secondary analysis, notifications, shared screens — eligibility is restricted by default and requires explicit authorization. Ineligible material must not be ranked, semantically compared, selected, passed to the mouth, used for simulation, or allowed to influence the response indirectly. Privacy filtering happens before semantic ranking so restricted material cannot influence selection even indirectly.

**Layer 2 — Pre-output privacy review.** After authorized material is retrieved and a response, view, suggestion, or derived output is formed, N.H reviews the final result before showing it. The output review is not a general content-safety or emotional-sanitization filter. It checks specifically for: accidental exposure outside the authorized private context; deleted or restricted content appearing in output; live secrets or non-negotiably excluded material; unauthorized secondary uses; unintended third-party profiling beyond the current authorized purpose; external sharing, notifications, tool outputs, or exports carrying private material; disclosure through shared screens or other unintended channels; several permitted pieces combining into a disclosure that exceeds the authorized purpose; generated language revealing more than the authorized sources themselves support. N.H must not soften, omit, or replace truthful relevant material merely because it may be upsetting to Ness.

MODEL-PROVIDER LIMITATIONS ARE RECORDED SEPARATELY. Any refusal or limitation from the mouth model — such as a Claude refusal — is recorded as a mouth limitation. It is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false. The material remains in the store under its existing rules. The limitation is attributed to the borrowed mouth, not to N.H's privacy system.

When permissions are ambiguous, outdated, unavailable, or conflicting for a non-private-Ness purpose — access defaults to withheld.

On output failure: withhold affected content for the unauthorized purpose, produce a safer version when possible, state plainly that material was withheld and why. Components receive only the minimum material needed for their authorized task. A component must not receive sensitive content merely so it can later decide not to display it.

Privacy checks apply to: chat, Computed View, Story Layer, Person-Boxes, Living State Web, memory browsing, search results, simulations, proactive suggestions, notifications, exports, tool use, and external sharing.

Every privacy decision records: operation requested, purpose, material considered, applicable privacy rule, authorization basis, eligibility decision, output-review result, and any withholding or transformation performed.

Remaining undesigned: exact eligibility rules, purpose categories, privacy-policy evaluation order, safe-transformation rules, interface behavior, core exclusion detection methods, mixed-content separation process, backup deletion/expiry mechanics, derivative-discovery methods, cryptographic erasure mechanisms, verification procedures, person-specific control interface, minor-data specific rules, volume thresholds for large imports, simulation permission specifics.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. Findings land in MEMORY as readings, never the mouth.

**★ COST AT FULL NIGHTLY SCALE (confirmed S16):** Brave roughly ~$62/month at about 13,500 queries/month under the quoted pricing assumptions, after the reported monthly credit + OpenRouter synthesis ~$60-240/month = **~$120-300/month total**. During building/testing: **$0** (inside $5 free Brave credit). **⚠ SAFETY BUILD REQUIREMENT:** Brave has NO spending cap — a loop can bill without stopping. When this pipeline is wired (item 8 in build order), a query counter / daily cap MUST be built into the code. Not optional.

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED]
Access/auth; mobile three modes; interactive canvas; behavioral-baseline wellbeing; HUD redesign; person-boxes gather (§7L); image front door (§9A); phone-data importer; memory browser; voice in/out; ChromaDB cleanup; folder cleanup. Catalog front door (§7E), context retrieval (§7F), meaning engine interior (§7G), reread lifecycle (§7H), view layer (§7I), clash handling (§7J), story layer (§7K), computed view (§7M), action surfacing (§7N), action-result return path (§7O), and permission and authority boundaries (§7P) are core-conceptually designed S17, not yet built. Privacy/deletion/sensitive-data handling (§7Q) is partially conceptually designed, not built.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Metadata → plain-description → context-meaning → Ness confirms. Precondition for WhatsApp media (§12).

## 10. ORIGINALITY (honest calibration)
The combination ships nowhere: inverted default + per-person never-closing STORY + DUMB/SMART split + person-boxes-as-gather + pure tape + wonder-kept-and-shown + memory-grows-not-the-mouth + two-destinations/two-files + living state web + structured perspective model + hybrid theme system + proposal-based identity anchors + blocking deletion verification + private-access-open-by-default. Never claim inventing local AI, approval gates, or a trained model.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ BUILT, 5,521 sealed. (c) wire into live flow — part of model-wiring/live-path.
2. **THE FORCED ORDER — 2a ✅ → 2b ✅ → 2c IN PROGRESS:** A ✅ B ✅. **NEXT: Engine C (story-layer). C needs story-bearing gold cases first.**
2b. **THE DETECTOR — recipe locked, live build deferred.** Fallback for role-less sources.
3. **★ THE MODEL WIRING (§16) — local-first.** Wire dolphin (mouth) + embedding search. **CHROMA REBUILD ✅ DONE (S16) — `nh_roots_v1` built from 5,521 clean roots.** Old 116k kept. **Hardware upgrade decided: RTX 5060 Ti 16GB on 5.7.2026 → `dolphin-llama3.1:13b` → re-run both gold sets.**
4. **NIGHT-SEARCH (committed, LATER).** Feeds MEMORY as readings. Cost ~$120-300/month at full scale; $0 during build. Brave spending-cap safety note: query counter required in code.
5. **Image-ingest front door (§9A).**
6. **Universal Filter / meaning engine** — = item 2's (2c), now in progress.
7. **ChromaDB — `nh_roots_v1` BUILT (S16). Old 116k kept until proven.**
8. **Research pipeline build.** ⚠ Brave spending cap — query counter / daily cap required in code when built.
9. **Hetzner sovereignty sync.**
10–12. nh_service (✅ disabled) · mobile + canvas · HUD redesign.
13. **THE [BUILT]-CLAIMS SWEEP — ✅ DONE (S13).** Future builds owe a quick existence-and-shape check.
14. **Folder cleanup** — `cloudflared.exe`; stale `peek.txt`; the ~12 S13 detector probes (keep the recipe reference); the stale "188 seed records" docstring in `_validate_record`.
15. **§11.15 STORE-COUNT RECONCILIATION — ✅ CLOSED BY ACTION (S12).**
16. **WhatsApp archive → eventual ingest (deferred):** decrypt → SQLite front door → image front door → child-data call → ingest only with engine.
17. **Open design threads (low):** spine re-draw; old gate lags; `.cursorrules` reconciliation (7-field root + reading-record contract + stale docstring); clash/gap UI surfacing; write the §0A DUMB/SMART section into final place; ~24 unreviewed Cursor batch files; person-box multi-box tagging; `source_title` alias/correction layer design (deferred); future root schema version (rename `subject` field).
18. **MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned. Must be designed before a SECOND batch is written.**
19. **★ CONFIDENCE — RESOLVED (S14).** TWO-SLOT `confidence` object. Value-FORM deliberately loose, pinned later as new schema_version.
20. **★ "UNDERSTANDING" — gold-standard sets BUILT & SEALED.** v1 (8 cases, S14) + v2-B (7 cases, S16) both on disk and sealed. Engine A ~5–6/8 on v1. Engine B 6.5/7 on v2-B on the tested dolphin 8B setup; the cause of the remaining miss has not been isolated — model capability, prompt framing, context format, and run variance remain possible contributors. RTX upgrade + a 13B-class model must be benchmarked; 7/7 is a goal, not an expectation or promise.
>    - **ENGINE B GOLD CASES (v2-B, S16):** B1 `7ac0381c` "episode 2" ✅; B2 `4e125b71` "yes sure, second." ✅; B3 `0df151d3` "yes, second option." ⚠️ (cause not isolated); B4 `9359edff` emotional reaction ✅; B5 `580d74d4` "Brief slow." ✅; B6 `09514821` "Yes! This is it." ✅; B7 `4b4e5551` "כן" ✅.
>    - **ENGINE B BUILD LESSONS (S16):** semantic context search fails for conversational turns — position-based is the correct lever; truncating context content kills quality — pass full content; BACKGROUND/END BACKGROUND framing prevents the mouth from answering instead of reading; tested dolphin 8B setup scored 6.5/7; cause of B3 miss not isolated.
21. **RE-READ LIFECYCLE + THE VIEW LAYER — CONCEPTUALLY DESIGNED (S17), NOT BUILT.** §7H, §7I.
22. **PERSON-BOX CONTAMINATION — GOVERNING RULE CONCEPTUALLY DESIGNED.** §7L requires per-element provenance; the exact link schema, validation rules, and implementation remain open.
23. **OFF-BOARD AFFIRMATION FEEDBACK SEAM** — record Ness's accept/reject as a dated, weightless STORY-LAYER EVENT.
24. **PRIVACY / THREAT MODEL + REDACTION PATH — PARTIALLY CONCEPTUALLY DESIGNED (S17), NOT BUILT.** §7Q. Implementation mechanics, detection methods, verification procedures remain undesigned.
25. **GO-LIVE HARDENING BLOCK — DEFERRED, does NOT gate the engine.**
26. **MODEL-REPLACEMENT DEFAULT — SETTLED.** A new mouth must be tested against BOTH sealed gold sets before replacing the current mouth; old readings keep old `produced_by`; no automatic mass reread. The future 13B-class candidate remains unverified and must be benchmarked on v1 + v2-B before adoption.
27. **QUARANTINE PHASE + BOOTSTRAP RETRIEVAL RULE — DESIGNED; quarantine STORE BUILT (S14).** Quarantine holds A + B gold-run output. Promotion needs gold + held-out + manual inspection.
28. **LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED (S17), NOT BUILT (§7D).** Node/edge types, grounding rule, currency rule, action surfacing (§7N), return path (§7O), and relationships to Computed View/Story Layer/Person-Boxes/authority/privacy designed. Schema, evidence thresholds, aging rules, trigger specifics, attention/relevance control, purpose-aware lenses, world model, and build order remain undesigned.
29. **ATTENTION AND RELEVANCE CONTROL — NOT DESIGNED.** Identified as remaining area. Must be designed before it can be built.
30. **WONDER AND SIMULATION MECHANISM — CONCEPT LEVEL ONLY, NOT DESIGNED.** Concept in §7B; interface concepts in §19. Mechanism undesigned.
31. **WORLD MODEL — NOT DESIGNED.** Named in Living State Web domain list. Must be designed separately.
32. **END-TO-END CYCLE — IDENTIFIED, NOT YET DESIGNED.** The major components addressed in S17 now have core conceptual architecture, while attention/relevance control, the wonder/simulation mechanism, and the world model remain open. The complete flow from a new input arriving through every relevant component to something appearing in the Computed View or chat response has not yet been designed and written as a single connected sequence.
33. **INTERFACE, WORLD, AND INTERACTION SYSTEM — IN-PROGRESS DESIGN, NOT BUILT.** Architectural content in §19. Simulation interior, gesture vocabulary, VR, camera, and accessibility substantially undesigned. Design paused and resumable.

---

## 11-SETTLED. (condensed)
- **S4–S11:** unit = span-claim; carry `role`; borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction; memory-grows-not-the-mouth; two-file 2a.
- **S12:** store restored; `role` added (7-field root); clean ingest; 5,521 clean roots; Chroma=old 116k index; two-destinations shape.
- **S13:** [BUILT]-sweep done; 2a plumbing built; roots sealed; detector recipe locked (94.89%); eleven doc-refinements + quarantine/bootstrap captured.
- **★ S14:** the three forks CLOSED — confidence = two-slot object; gold scoring = six rules (semantic match, Ness judges); failure-behavior = honest insufficient-context, revisable. Reading validator + writer BUILT & VERIFIED (17/17 tests; roots regression clean). Gold set v1 (8 cases) SEALED. Minimal engine A BUILT & run against gold (~5–6/8 after prompt+role fixes). Model test: dolphin beats qwen-abliterate-3b; Hebrew gated on bigger model/VRAM. Validator structure = extract-not-fuse (`_check_common`). Quarantine store built. Confidence value-form left loose.
- **S15-chat:** NO N.H change. Scan-only confirmation that the three files are in sync + one out-of-system teaching artifact (`NH_one_pass_demo.html`). Master stayed MASTER-15; status table untouched.
- **★ S16:** Engine B BUILT & RUN — position-based context (preceding turns, same thread, full content, n=3), BACKGROUND/END BACKGROUND prompt, tested dolphin 8B setup scored 6.5/7 on gold v2-B, cause of B3 miss not isolated. Gold v2-B (7 context-requiring cases) SEALED. Chroma `nh_roots_v1` BUILT (5,521 roots, 187.59s). Hardware upgrade decided: RTX 5060 Ti 16GB, ~₪2,590, buy 5.7.2026, target model `dolphin-llama3.1:13b`. Cost notes confirmed: $0 now, ~$120-300/month at full nightly scale. Brave spending-cap safety note added to §8 and §11 item 8.
- **★ S17:** Broad conceptual design of the major components addressed during the session, while several larger areas remain open. Catalog front door (§7E), context retrieval (§7F), meaning engine interior including Reading Proposal Acceptance Check and model-confidence-is-metadata-not-authority first-class principle (§7G), reread lifecycle (§7H), view layer (§7I), contradiction and clash handling (§7J), story layer with structured perspective model, firmness rule, and hybrid themes (§7K), person-boxes with proposal-based creation and seven-section view (§7L), computed view with seven-factor ordering and triggered snapshots (§7M), action surfacing with possibility-disposition states (§7N), action-result return path with six result states (§7O), permission and authority boundaries with stop-and-surface violation rule (§7P), and privacy/deletion/sensitive-data handling including private-access-open-by-default and model-provider-limitations-as-mouth-limitations (§7Q). Living state web partially designed (§7D). `subject` field audited as legacy provenance-batch tag. Interface and world design log incorporated (§19). Engine B overclaims corrected throughout. No code written in S17.

---

## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN]
A13 WhatsApp 2012→2024, encrypted (~118 MB), archived to `C:\Phone_A13_Backup` + Drive. SETTLED: ingest FROZEN — decrypt → SQLite front door → image front door → child-data call → ingest only with engine.

## 13. THE LIVE LOOP  [DESIGNED — not built]
A figure-eight, cache outside. Fire-and-let-go starter; deep side (memory · filter · search model · mouth · wonder). **The live path (memory → search → mouth → speak) is built first.**

## 14. THE CHAT FRONT DOOR  [DESIGNED-IN-PROGRESS]
TWO STAGES: RAW → CATALOG (who/when/where; live chat MAY ask, nightly never asks). Memory PULLED every turn as context, used silently; reply generated fresh by the mouth from the read; the point-back is the one surfaced thread.

## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done]
Boot HUD traced + handled; Kensington fingerprint key; stray `install_startup.bat` deleted.

---

## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk]

**THE CENTRAL TRUTH.** The language model is a borrowed, FROZEN mouth + general knowledge — a commodity. Everything that makes N.H *N.H* lives OUTSIDE the model.

**WHY NOT TRAIN ONE.** Wrong resource category. Put knowledge in the MEMORY instead — yours, dated, layered, never-closed.

**★ TWO MODELS, TWO JOBS.** (a) WORDING/generation — the mouth (heavy); (b) SEARCHING/retrieval — the embedding model (tiny). **ORDER: search first, word last.** On disk: `all-MiniLM-L6-v2` + ChromaDB. `nh_roots_v1` is the new clean index (S16). Old 116k kept until proven.

**★ GROWTH LANDS IN THE MEMORY, NEVER THE MOUTH.**

**THE DECISION — LOCAL-FIRST.** Sovereign, offline, private, uncensored. The model is swappable behind the meaning step.

**★ THE MOUTH IS UNCENSORED BY DESIGN, BUT MODEL BEHAVIOR IS A STACK PROPERTY.** Refusal and restriction can arise from model weights, fine-tuning, system prompts, runtime filters, or surrounding software. A prompt alone cannot reliably turn a restricted model into the intended mouth. The design choice is therefore to use a model trained for low restriction and keep the surrounding runtime transparent and auditable. `dolphin-llama3` remains the current chosen mouth because it best fit that goal among the tested local candidates.

**★ S14 — THE HEBREW FINDING.** dolphin-llama3 beats qwen2.5-abliterate:3b. Current evidence suggests Hebrew quality is substantially model-capability-gated; prompt changes alone did not solve it in the tested runs. Free interim patch: translate Hebrew→English before the mouth reads (logged, not built). Hebrew on dolphin today = "weak-but-workable."

**★ S16 — ENGINE B LIMIT OBSERVED.** On the tested dolphin 8B setup, one case confused the act of choosing with the content chosen, yielding 6.5/7 on gold v2-B. The leading hypothesis is a model-capability/role-separation limit, but this is not conclusively isolated from prompt, context formatting, or run variance. **Next experiment:** test a verified 13B-class candidate on a larger-VRAM GPU against both sealed gold sets. Wider-thread reading is a benchmark goal, not an assumed unlock.

**★ S17 — MODEL-PROVIDER LIMITATIONS AS MOUTH LIMITATIONS (FIRST-CLASS RULE).** Any refusal or limitation from the mouth model is recorded as a mouth limitation, never as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false. See §7Q.

**ON-DISK STATE:** `dolphin-llama3` (8B, uncensored — THE CURRENT MOUTH) · `llama3` (8B) · `qwen2.5-abliterate:3b` (test, not adopted) · `all-MiniLM-L6-v2` (search). Runtime Ollama, GGUF.

**UPGRADE TARGET (S16 PLAN):** test a verified 13B-class uncensored candidate on the planned 16GB GPU. `dolphin-llama3.1:13b` is a candidate name, not yet verified here. Do not assume fit or speed; confirm the exact tag, quantization, license, VRAM usage, and measured throughput. Run both gold sets before adoption.

---

## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical)

*This log records corrections made during the S16 correction pass (June 24 2026). It is historical and describes changes from MASTER-15 to MASTER-16.*

1. **Session control:** removed language implying that long chats should end or that the assistant may tell Ness to sleep, wrap up, or move to a fresh chat.
2. **Task order vs conversation control:** clarified that "finish and verify" governs project sequencing only.
3. **Cursor boundary:** changed "Cursor writes code" from a universal routing rule into an optional code tool; direct document/file creation remains the assistant's job when requested.
4. **Artifact delivery:** added an actual-file rule, version safety, latest-instruction priority, and an anti-loop recovery rule.
5. **Human-state claims:** prohibited explanations such as being tired, "on fumes," impatient, or "losing it."
6. **Engine B causality:** changed "proven 8B ceiling / not an engine bug" into the fairer statement that model capability is the leading hypothesis but has not been isolated from prompt, context formatting, or run variance.
7. **13B outcome:** changed "13B resolves this / expected 7/7" into a benchmarkable goal with no guaranteed result.
8. **Hardware claims:** converted store, price, warranty, speed, fit, and availability into a dated decision snapshot that must be re-verified at purchase/install time.
9. **VRAM wording:** removed "VRAM is the only number that matters"; retained VRAM as a major constraint while acknowledging quantization, context, bandwidth, thermals, PSU, and software support.
10. **Cost math:** corrected the query volume from **13,500 per night** to **about 13,500 per month** and labeled all provider costs/credits as estimates requiring re-check before launch.
11. **Original safety:** this was a new file; the uploaded MASTER-16 was not overwritten.

---

## 18. S17 CONSOLIDATION AND CORRECTION LOG

*This log records what S17 added, changed, or corrected versus MASTER-16 / NH_MASTER-17_DRAFT.md.*

1. **Header updated:** title changed from MASTER-16 to MASTER-17; S17 session description added to preamble.
2. **Status table:** added rows for all S17-designed components; corrected Living State Web status from "CONCEPTUAL DESTINATION, NOT DESIGNED" to "PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT"; corrected view layer status from "NAMED, NOT DESIGNED" to "CONCEPTUALLY DESIGNED, NOT BUILT"; added end-to-end cycle as "IDENTIFIED, NOT YET DESIGNED"; added interface/world system row.
3. **Engine B overclaims corrected throughout:** removed "dolphin 8B ceiling," "ceiling confirmed," and "not engine bug" from §6, §7C, §11 items 20 and 11-SETTLED S16 entry, and closing material. Replaced with: "The tested dolphin 8B setup scored 6.5/7. The cause of the remaining miss has not been isolated; model capability, prompt framing, context format, and run variance remain possible contributors."
4. **`subject` field audited (S17):** documented in §6B as a legacy provenance-batch tag in v1. All 5,521 roots use seed:conversations_000/001/002. Rename deferred to next schema version. Future semantic subject/topic must be a new field, not a reuse of this one.
5. **§7D revised:** Living State Web section rewritten from "CONCEPTUAL DESTINATION, NOT DESIGNED" to "PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT." Node/edge types, grounding rule, currency rule, relationships now designed. Future domains updated with honest partial-design status. Remaining unresolved items listed explicitly.
6. **New §§7E–7Q added:** catalog front door, context retrieval, meaning engine interior, reread lifecycle, view layer, contradiction and clash handling, story layer, person-boxes, computed view, action surfacing, action-result return path, permission and authority boundaries, privacy/deletion/sensitive-data handling. All full settled rules preserved without replacement by summaries.
7. **Action lifecycle given dedicated sections:** §7N (action surfacing), §7O (action-result return path), §7P (permission and authority boundaries). Authority violation and correction is a major subsection of §7P. Five linked-object rules explicit.
8. **Reading Proposal Acceptance Check naming:** renamed from "Mouth response acceptance step" throughout.
9. **Model confidence is metadata not authority:** elevated to first-class principle in §7G; cross-referenced in §16.
10. **Model-provider limitations as mouth limitations:** new rule in §7Q and §16. Any Claude or other model-provider refusal is recorded as a mouth limitation, not an N.H privacy rule.
11. **Private access for Ness open by default:** central rule added to §7Q two-stage access control. Output review is not a content-safety or sanitization filter.
12. **§11 open items updated:** items 21–27 updated to reflect S17 design status; new items 29–33 added for remaining undesigned areas.
13. **§11-SETTLED:** S17 entry added.
14. **§3 evolution:** entry M added for S17.
15. **§17 labeled as historical:** S16 correction log clearly labeled as historical record of S16 changes.
16. **§19 added:** Interface, World, and Interaction System — all architectural content from NH_INTERFACE_WORLD_DESIGN_LOG.md incorporated, organized into settled decisions, provisional concepts, unanswered questions, paused design points, and open dependencies.
17. **Closing principles:** updated with S17 first-class rules; Engine B overclaims removed; truest single sentence updated.
18. **No source files modified:** NH_MASTER-16_FINAL_CORRECTED.md and NH_MASTER-17_DRAFT.md remain unchanged.
19. **S17 document-correction pass:** removed build-script debris; corrected status and provenance contradictions; aligned private access rules; kept partial-success/failure causal judgments revisable; reconciled View Layer with Computed View ordering; made clash-history additions append-only; restricted pre-ingest visibility to safe metadata; clarified risk-level mapping; and made world manipulation presentation-only by default.
20. **Final consistency pass:** corrected the pre-ingest lifecycle count; clarified category-to-risk-level mapping and result-state criteria; made Level 2 state changes explicitly append-only; added privacy precedence over catalog preservation; separated acceptance-rejection reasons from genuine insufficient context; recorded the unresolved Story Layer object-identity seam without selecting a new feature; corrected Person-Box/model-replacement status wording; and softened legacy model-behavior claims without changing the chosen mouth.

---

## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT]

*Architectural and design content incorporated from NH_INTERFACE_WORLD_DESIGN_LOG.md. Purely procedural continuation instructions have been omitted. This design is paused and resumable.*

---

### 19A. SETTLED INTERFACE DECISIONS

**Core direction.** N.H should feel like entering Ness's own mind or world, not like opening a normal app with chat inside it. The world is called: **Ness's World.**

**Modes.** Conversation mode (one clear place where N.H speaks with Ness) and World mode (Ness moves through his inner world) are named. Automatic switching may change presentation when the situation clearly benefits, but must not secretly begin a new action or simulation. Manual switching: Ness can command changes through chat or voice. More modes are expected.

**Opening Ness's World.** Requires identity confirmation through a private code or thumb/fingerprint verification. After verification, N.H says: "Identity confirmed. Open Ness's World?" Ness then confirms. A normal command alone is not enough.

**Initial state and growth.** Ness's World begins as a blank space. As Ness types, speaks, imports, creates, remembers, and interacts: memories appear, people appear, places appear, projects appear, paths and categories form. The world keeps growing; structure can change over time; Ness can reorganize or transform it.

**World properties.** The world is infinite. Ness may move by walking, flying, or instantly pulling himself toward things. New things may appear automatically, but Ness may also place them manually. Visual form changes depending on content. The world itself reacts to Ness's mood/state. Weather, lighting, and sound may change with Ness's state. Categories may appear as places, objects, beings, portals, or whatever fits. Areas may reorganize automatically over time. Important things may glow or call to Ness. Multiple versions of the same thing may exist in different places. Ness may grab, move, merge, split, and reshape parts of the world by hand. Time may move normally, pause, rewind, or speed up. Moving between related spaces should feel smooth; moving between unrelated spaces may use a clear doorway. Ness may pause automatic world changes.

**World-manipulation boundary.** Grabbing, moving, merging, splitting, reshaping, rewinding, or speeding up world elements changes presentation, navigation, or an explicitly labeled simulation by default. It does not rewrite roots, readings, tellings, Person-Box identity links, themes, state nodes, permissions, deletion state, or external systems. Any operation that would change underlying records or have real-world effect is a separate proposed action governed by the relevant proposal, correction, privacy, and authority rules (§§7J–7Q).

**The white door.** The default doorway is always a plain white wooden door. It does not automatically change with the theme. It is not mainly for objects entering the world — Ness enters through it. Ness moves through doors into spaces he is creating or exploring. Previous spaces remain behind him. The last two generated spaces should remain especially easy to return to. Spaces may be built using memories.

**Chat as N.H's presence.** Chat remains available inside Ness's World. It is not a fixed sidebar. It may be movable, draggable, resizable, brought closer, pushed away, partly hidden, summoned by voice, dismissed by voice. Chat is N.H's presence inside Ness's World, not merely a text box.

**N.H's form.** N.H has no single fixed form. It may appear as a person, a floating panel, an object, a voice with no visible form, or another form that fits the situation. Form may change automatically, when Ness commands it, in response to mood, purpose, environment, state, or the type of help needed. Visual form and voice may change independently.

**Reading the room.** Small visual changes may happen naturally. Big changes should ask Ness first without ruining the moment. N.H may ask through voice, a small gesture, light, a quiet symbol, hand tracking, or subtle movement in the space. If N.H reads the room incorrectly, Ness may correct it immediately by voice. N.H may then adjust immediately and silently, briefly acknowledge, or ask one short clarification.

**Voice.** N.H can speak and listen by voice. Ness may summon, silence, dismiss, or turn N.H off through voice. N.H's voice may change in pace, warmth, distance, intensity, presence, emotional tone, and role/persona — while still feeling like the same N.H underneath. Two distinct voice modes: **Replay mode** (actual recorded or documented words) and **Simulation mode** (new generated words in a requested voice, only when Ness asks). Before simulated voice begins, N.H says: "Simulating voice." That phrase starts in N.H's normal voice and shifts smoothly and gradually into the simulated voice.

**N.H reacting to Ness.** N.H's appearance may react to Ness's state even while silent. The strength of reaction may vary automatically. N.H should learn from Ness's corrections gradually — one correction must not instantly become a permanent rule. N.H should not automatically announce every new pattern it notices. Ness must be able to inspect what N.H has learned: current learned patterns, earlier patterns, how each changed, what evidence caused the change, current certainty. Ness wants to inspect and provide small corrections through conversation. Ness's exact correction words must be preserved as direct evidence, separate from N.H's interpretation.

**Simulation basics.** Actual replay and simulation remain separate. Simulation must not begin secretly. Entering simulation is a major change and requires Ness's approval, but the request should preserve the moment. A simulated voice is introduced with "Simulating voice." Simulation may involve memories, reconstructed voices, people, possible futures, environments, alternative choices, remembered situations, generated spaces.

**Deep structure.** Ness's World must allow extremely deep nesting (e.g. World → People → Family → Mother → Specific period → Specific event → Specific conversation → Specific sentence → Specific meaning). The category system remains open and must eventually support many more branches, sub-branches, and ways of reaching the same object.

**Physical interaction methods desired.** VR, camera-based hand tracking, microphone, voice, mouse, keyboard, touch. Possible hand-tracked actions: grabbing, moving, pulling, pushing, merging, splitting, reshaping, opening, closing, summoning, dismissing.

---

### 19B. PROVISIONAL CONCEPTS

**Strongest current concept.** Ness's World is an infinite, initially blank, living world that grows from Ness's life. It can reorganize, transform, react, and deepen without a fixed final form. Ness moves through it physically or instantly, manipulates it directly, travels between distinct spaces through plain white wooden doors, and can always summon N.H as a changing presence through voice, form, panel, person, object, or environment.
*(Individual claims within this concept have varying levels of settlement — it is a synthesis statement, not a fully settled specification.)*

Whether the world has a stable home or center depends on Ness's mood. Whether manually placed objects stay fixed depends on rules/configuration. When Ness goes deep into one branch, the visibility of the rest of the world may change depending on the situation.

---

### 19C. UNANSWERED QUESTIONS

The design session paused with these questions unanswered:

1. Should a new space start blank when Ness is creating something from scratch?
2. Should it start partly formed when N.H already has enough memories and context?
3. Should Ness be able to choose: blank, memory-built, or mixed?
4. Should N.H sometimes choose one automatically?
5. If N.H chooses automatically, should Ness be able to change it instantly by voice?

Additional unanswered: exact visual transition on opening; same-screen versus full-screen opening; desktop/mobile/VR differences in opening behavior; exact backtracking order between spaces; whether each recent space has its own direct door; whether the full context of each correction is preserved automatically; how learned interaction patterns are displayed; how Ness challenges or limits one learned pattern without directly editing the whole model.

---

### 19D. PAUSED DESIGN POINTS

The following are substantially undesigned:

**Simulation interior:** how simulation starts; whether it opens through a white door; whether it changes the whole world or one area; first-person vs observer vs both; time controls; branching and reset; simulated people; N.H's form inside simulation; memory replay vs simulation visual difference; evidence/reconstruction/invention labeling; instant exit; emotional-overload handling; saving and revisiting simulations; whether simulation outputs become plans or remain possibilities; hand tracking and voice inside simulation.

**Physical interaction:** gesture vocabulary; accidental-gesture prevention; tracking failure behavior; camera privacy; VR body/avatar; accessibility alternatives; how voice and gesture combine; whether camera mode mirrors VR mode.

**N.H's adaptive behavior:** how Ness challenges or limits one learned pattern; how the full learning history is displayed and navigated.

**Exact visual language:** how spaces look, how transitions animate, how different object types appear in the world, how mood/state changes manifest visually.

---

### 19E. OPEN DEPENDENCIES (cross-audit results)

Cross-audit of the interface log against settled component rules identified one direct integration ambiguity: the merge/split/reshape language could be read as mutating underlying records. §19A now resolves that ambiguity by making world manipulation presentation-, navigation-, or explicitly labeled simulation-only by default. No remaining direct contradiction was found. Three open dependencies require future design attention:

1. **Approval explicitness vs. interface unobtrusiveness (permission and authority gap).** The authority system requires explicit approval for Level 3 and Level 4 actions. Entering simulation is described as requiring Ness's approval but the request should "preserve the moment" — with N.H potentially asking through gesture, light, or subtle movement. How explicit approval must be when the interface is designed to be unobtrusive is an open design gap to resolve when simulation and authority-level interaction are designed together.

2. **Camera and VR as new front doors (privacy dependency).** Camera-based hand tracking and VR are desired future interaction methods. Camera input is a new front door subject to the capture exclusion rules in §7Q, including the pre-retrieval eligibility rules and the non-negotiable core exclusion layer. Capture exclusion rules for camera/VR input will need to be explicitly designed when those front doors are built.

3. **External actions triggered from within Ness's World (authority dependency).** When Ness takes actions with real-world effect from within the world environment (sending messages, calling tools, writing files), the full authority chain from §7P applies regardless of the interface context. This dependency will need explicit design when tool use and external action capabilities are added to the world interface.

---

**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board** · **the engine reads by PATTERN and CAN be wrong — that is designed-around, not a flaw** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary** · **the affirmation surface is a per-person STORY — never closed; absence read only under the §0A guard; N.H is NOT a teller** · **TWO DESTINATIONS: every eligible input → raw root (sealed) + a reading beside it; this is why two files** · **`story_layer` is a LIST so clash is kept; `mode` is an OPEN word; `confidence` is a TWO-SLOT object never one blended number; unknowns OMITTED** · **CARRY THE SPEAKER, DON'T GUESS IT — `role` on the root, from source; detector a fallback** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE preserves eligible events append-only — subject to capture-exclusions + audited redaction** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; uncensored by choice; local-first; night-search feeds the MEMORY not the mouth; do not train a base model for this role; current evidence suggests Hebrew quality and B3 miss are strongly model-capability-related but cause not isolated; the RTX 5060 Ti 16GB plus a verified 13B-class model is the planned next experiment, subject to purchase-time and benchmark verification** · **THE GOLD IS A SEALED OUTSIDE EXAM — two sets now: v1 (8 cases, clean-bare) + v2-B (7 cases, context-requiring); both sealed; engine output may fail but never alter; only Ness judges** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id** · **ONE FILTER, BOTH DIRECTIONS** · memory only adds (history grows; the computed view governs live use) · the membrane · a unit is a span-claim · input-agnostic, many front doors · archive don't ingest · הכל יחסי · don't overclaim · **RAW CAPTURE ≠ ROOT INGESTION — two gates; the pre-ingest store holds what is not yet eligible; a blocker is removed only when its requirement is actually resolved** · **MODEL CONFIDENCE IS METADATA, NOT AUTHORITY — applies to all present and future models; a confident response may still be wrong; acceptance depends on grounding in the root, supplied context, declared mode, and explicit evidence** · **PRIVATE ACCESS FOR NESS IS OPEN BY DEFAULT — sensitive, emotional, medical, traumatic, or uncomfortable material is not blocked merely because of its subject; external exposure and secondary uses are restricted by default** · **MODEL-PROVIDER LIMITATIONS ARE MOUTH LIMITATIONS — a Claude refusal or any model-provider constraint is never interpreted as an N.H privacy rule, a Ness restriction, or evidence that the underlying material is forbidden or false** · **DELETION IS BLOCKING AND VERIFICATION-BASED — N.H may confirm complete deletion only when every known location has been removed or verified clean; five distinct outcomes; tombstone only** · **STOP-AND-SURFACE IS THE DEFAULT FOR AUTHORITY VIOLATIONS — corrective action is a new action requiring its own approval; five separate linked objects; the narrow emergency stop exception does not permit any completed-world reversal without Ness's approval** · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen, uncensored mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — where the reading record is now real built plumbing (a twelve-field validator and writer, gating shape not certainty, with confidence held as two honest slots rather than one blended number), and two engines now read: engine A reads a root bare and lays a reading beside it, engine B reads it in the context of the three turns that came before in the same conversation thread, both judged against sealed gold answer keys that only Ness can grade because the whole spec is "does it read the way Ness's mind reads" — and when the engine is wrong, as a pattern-reader sometimes must be, nothing breaks, because a wrong reading is a replaceable guess marked with its own uncertainty, never a fact, and the planned upgrade (currently an RTX 5060 Ti 16GB candidate for 5.7.2026, paired with a verified 13B-class model) will be tested to see whether it improves the remaining 6.5/7 gap and makes wider-thread reading practical — and around this foundation S17 has now designed the core conceptual architecture for the major components addressed in the session—while attention/relevance control, the wonder/simulation mechanism, the world model, and the connected end-to-end cycle remain open: the front door that captures without interpreting, the context retrieval that keeps positional and semantic evidence separate and labeled, the meaning engine that runs a Reading Proposal Acceptance Check and treats model confidence as metadata not authority, the story layer that holds tellings across time by structured perspective without merging them, the person-boxes that gather without profiling, the computed view that assembles what N.H has reason to show using an explicit seven-factor order with no hidden truth score, the living state web that maps the state-space without choosing the path, the action lifecycle that labels every suggestion as a possibility and every result as a separate linked object, the authority boundaries that require stop-and-surface before any corrective action, and the privacy system that keeps Ness's own access open by default while restricting external exposure by default and recording every model-provider limitation as a mouth limitation never a system rule — so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone, because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
