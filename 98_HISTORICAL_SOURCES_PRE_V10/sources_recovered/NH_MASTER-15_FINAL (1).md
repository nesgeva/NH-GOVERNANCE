# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, AND the code rules — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–13. **Session 14 (June 23 2026) is a DESIGN-then-BUILD session → this is MASTER-15.** S14 closed the three genuinely-open forks AND shipped the next build. Net: the reading record went from DESIGNED-NOT-CODED to **BUILT & VERIFIED on disk**; the gold set is **SEALED**; a **minimal engine (A) is BUILT** and was run against the sealed gold; and the Llama-vs-Qwen Hebrew fork was **tested on real Hebrew**. The forced build order (§7C/§11) advanced from "reading-record code is next" to "the engine is being grown, layer by layer."*

*★ **VERSION BUMP 14 → 15.** The frozen DECISION-DEFAULTS provenance pointer must update to name `NH_MASTER-15_FINAL.md` in the same pass, or the pair goes stale. (See the defaults' provenance line.)*

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
> | Quarantine readings store (`.nh_readings_quarantine.jsonl`) | **BUILT (S14)** | separate test file; production readings store still absent |
> | Minimal engine A (`nh_engine_minimal.py`) | **BUILT & RUN (S14)** | root → mouth → 12-field reading → quarantine; run against the 8 gold; ~5–6/8 solid after prompt+role fixes |
> | Production readings store (`.nh_readings_store.jsonl`) | **ABSENT (correct)** | no production readings yet; quarantine-only by design |
> | Speaker detector recipe (embed+shape→LogReg C=0.1→94.89%) | **INVESTIGATED & PROVEN, NOT DEPLOYED** | fallback only |
> | Ingest pipeline (`nh_ingest_chatgpt.py`) | **BUILT & VERIFIED** | S12 |
> | Chroma `nh_reality_core` (116,391) | **BUILT — OLD/unaligned index** | rebuild from clean roots later |
> | The engine (2c) — full chain of webs | **PARTIALLY BUILT (A only)** | A = meaning + role + defaults; B (context) + C (story) NOT built |
> | Mouth model choice | **dolphin-llama3 = best on disk (S14)** | tested vs `qwen2.5-abliterate:3b` — dolphin won; abliterate-3B read worse, gave up on Hebrew |
> | Hebrew reading quality | **WEAK-BUT-WORKABLE; gated on bigger model/VRAM** | §16 — not prompt-fixable; optional RTX 3060 12GB upgrade (~₪1,400), buy-time, NOT a blocker |
> | Multi-box (sealed-batch) architecture | **NOT DESIGNED** | §11 item 18 |
> | View layer | **NAMED, NOT DESIGNED** | §11 item 21 |
> | Quarantine promotion + memory-health checks | **DESIGNED, NOT BUILT** | §11 item 27 |
> | Pure-tape redaction/destruction path | **NOT DESIGNED** | §0A correction + §11 item 24 |
> | Confidence value-form (low/med/high vs 0–1) | **DELIBERATELY LOOSE** | validator checks present+non-empty only; pinning later = new schema_version |
>
> **2a = COMPLETE (routing + seal + reading record all built). 2c = STARTED (minimal engine A built & tested; B/C next).**

---
>
> **0. ★ THE READING RECORD IS NOW BUILT — VALIDATOR + WRITER LIVE ON DISK (S14).** What changed from S13:
>    - **BUILT & verified (S14):** `_validate_reading` — the 12-field shape gate. Rejects malformed, never rejects uncertain (R5). A low/weak/empty-story/insufficient-context reading is WRITTEN-and-marked, never refused. 17/17 fixture tests pass.
>    - **BUILT & verified (S14):** reading-shaped `append_reading` — verify-referenced-root-before-commit, idempotency reject on `idempotency_key`, atomic append (flush+fsync), append-only, writes to a target path.
>    - **BUILT & verified (S14):** `_check_common` — shared id+timestamp checks, extracted ONCE; `_validate_record` (roots) now delegates to it. The 5,521 sealed roots STILL validate clean through the helper (regression proven).
>    - **The reading record contract (12 fields):** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. `confidence` is now the TWO-SLOT object (see §6B). Coded, gated, verified.
>    - **The seal is per-BATCH, not "no more data ever."** ⚠ multi-box architecture still undesigned (§11 item 18).
>
> **1. ★ THE READING-RECORD SHAPE IS NOW FULLY SETTLED (S14) — confidence resolved.** `story_layer` = a LIST of tellings; `mode` = an OPEN word + classification_confidence; unknown parts OMITTED. **And the last open piece, `confidence`, is resolved: a TWO-SLOT object** (`interpretation_confidence` + `source_reliability`), never one blended number. The validator enforces the whole shape.
>
> **2. ★ THE GOLD SET IS SEALED (S14).** 8 hand-annotated cases (`NH_GOLD_SET_v1.md` + `.nh_gold_v1.sealed`). Each case = target root + frozen context + Ness's gold answer, human-annotation provenance. The gold seal holds: engine output may FAIL a case but may NEVER alter it; a correction is a NEW versioned gold.
>
> **3. ★ A MINIMAL ENGINE (A) IS BUILT AND WAS RUN (S14).** `nh_engine_minimal.py`: load a root → ask the mouth "what is the {role} doing" → build the 12-field reading → write to QUARANTINE. Run against the 8 gold roots. After two small fixes (prompt sharpened from "say what this line is" → "say what the person is doing"; role passed to the mouth so it stops guessing speaker), it read ~5–6/8 solidly. The remaining misses are model-quality (small 8B mouth, Hebrew weakness, run-to-run wobble), not engine bugs — exactly what the gold was built to surface.
>
> **4. NET FOR THE BUILD:** **2a complete; the loop is alive — read → compare to gold → fix → re-read. The next milestone is GROWING the engine: A (meaning, ✓) → B (add context-search) → C (add story-layer). B and C each need their OWN gold cases (ones that require context / have a story) before they can be tested.**

> **★ DECISIONS LOCKED IN SESSION 14 (protect from re-litigation):**
> - **`confidence` = a TWO-SLOT object** `{ interpretation_confidence, source_reliability }`. `interpretation_confidence` filled on every reading; `source_reliability` slot-present from the first reading but left EMPTY until the engine can honestly judge a source (sarcastic/fictional/copied/manipulated) — empty-when-unknown is honest, never faked. NEVER one blended number; confidence never rises from copied error; a reading never inherits a prior's confidence. The other two "kinds of sure" stay home: story firmness inside `story_layer[].firmness`; retrieval relevance computed at search time, never stored. `mode.classification_confidence` is local and separate. SETTLED.
> - **GOLD SCORING — six rules.** (1) `meaning` judged by SEMANTIC match (means the same, not exact words); Ness decides same/not-same by hand, model may show the pair but never holds the verdict. (2) `story_layer` NOT graded in v1 (meaning only; add partial story-scoring later, weighted from real engine behavior). (3) MAKING SOMETHING UP is the real fail; leaving something out is NOT a fail if what's said is right. (4) Correct-but-EXTRA: true extra passes, made-up extra fails (same rule as #3). (5) A case MAY list several acceptable readings, each with a "why it holds" note; engine passes on any one, the note shows which perspective. (6) NESS decides pass/fail; model assists, never judges (the spec is "reads like Ness," so the only valid reference is Ness). Annotating gold is recording REACTIONS/opinions off to the side, sealed, used once — NOT the forbidden manual gate, NOT deciding truth. SETTLED.
> - **ENGINE FAILURE-BEHAVIOR.** When the engine can't interpret a root: it does NOT fake a minimal read and does NOT stay silent. It writes an honest INSUFFICIENT-CONTEXT reading (a real record: "seen this, couldn't read it — not enough context"), MARKED revisable, so a later read can accrete BESIDE it (only-adds; the honest "couldn't read" record is never overwritten). The retry-TRIGGER (when/whether the engine revisits marked records) is DEFERRED — "marked revisable" ≠ "churn the pile nightly"; the insufficient-context records ARE the visible countable backlog. SETTLED.
> - **CONFIDENCE VALUE-FORM left deliberately LOOSE** — validator checks `interpretation_confidence` present+non-empty only; whether it's low/med/high or 0–1 is pinned LATER (a new schema_version), once real engine output exists to calibrate against. SETTLED-as-deferred.
> - **VALIDATOR STRUCTURE = option C (extract, don't fuse).** `_check_common` holds shared id+timestamp; `_validate_record` (roots) and `_validate_reading` (readings) each call it then do their own checks. The proven root validator keeps its simple body; reading path is its own walled-off function. SETTLED + BUILT.
> - **MODEL FINDING (S14):** tested `huihui_ai/qwen2.5-abliterate:3b` (uncensored Qwen, pulled to disk) against the sealed gold vs `dolphin-llama3`. The abliterated 3B read WORSE — collapsed to bare stubs, gave up on the Hebrew cases (abliteration cost + 3B too small). **dolphin-llama3 remains the best mouth on disk; the engine reverted to it.** Hebrew quality is model-size-gated (see §16). SETTLED-as-finding.

> **PRIOR DELTA (SESSION 13 → MASTER-14) — condensed for continuity:**
> - [BUILT]-claims sweep done (floor confirmed, 1 inert phantom `nh_peek.py`). **2a PLUMBING BUILT** — `append_reading`→sibling `.nh_readings_store.jsonl`, roots SEALED via `.nh_roots.sealed` (per-batch). The 8-field reading record was provisionally settled (`story_layer`=LIST, `mode`=OPEN word, unknowns OMITTED) but `confidence` OPEN and not coded. **2b DETECTOR investigated** (10 methods): shape ceiling ~91.6%; embeddings → 93.5%; embed+shape → 94.7%; tuned C=0.1 + 5-fold → honest **94.89%**. Recipe locked, NOT deployed; LLM detector parked. The S13 doc-pass folded eleven refinements (gold case unit, gold seal, validator sequencing, `produced_by`, `schema_version`, view layer, interpretation-integrity constraint, model-replacement default, go-live hardening block, lineage `derived_from`, writer-contract pins) and item 27 (quarantine + bootstrap).

> **PRIOR DELTAS (sessions 4–12) — condensed for continuity:**
> - **S12 (→ MASTER-13):** store became real & clean — **5,521 verified roots** (7-field `id·subject·timestamp·content·re_reads·source_title·role`, role carried from source). Five disk-truths corrected the master. `role` added (6→7 fields). Clean ChatGPT-export ingest pipeline built. §11.15 closed (flat=sealed roots-of-record, Chroma=rebuildable index). `gpt_purified`+`cleaned_history` correctly NOT ingested. The TWO-DESTINATIONS shape (every input → raw root + a reading beside it) — Ness re-derived it himself.
> - **S11 (→ MASTER-12):** MODEL LAYER resolved (borrowed frozen mouth; two models wording+search; local-first; `dolphin-llama3` uncensored; `all-MiniLM-L6-v2` search). PERSON-BOXES, PURE TAPE, WONDER/SIMULATION, CATALOG, SOUL CORRECTION (engine never decides, Ness affirms off-board), "memory is understood knowledge that grows." All DESIGN.
> - **S10:** 2a shaped; DUMB vs SMART (psychologics) frame (§0A); "HELPER not DECIDER"; reality → per-person STORY-layer; N.H not a teller; mode = peer web; firmness READ; clash a feature.
> - **S9:** the PREMISE §0; reality → per-person READING; the "why" = non-decisive NOTE; read-only tools; speaker settled on ground truth (carry `role`).
> - **S4–S8:** accretive store skeleton; unit = span-claim; forced build order; WhatsApp data-rescue (archived, NOT ingested); live loop + chat front door + guard.

> **THE NAME:** He is **Ness** (male). He signs **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. As of S14: the clean store + role schema + ingest pipeline + 2a plumbing + **the reading record (validator + writer) + the gold set (sealed) + a minimal engine (A)** are all **[BUILT]**. The full engine (B context, C story), the view layer, person-boxes, tape, wonder, catalog, model wiring/Chroma-rebuild are **[DESIGNED]**. The old REALITY/SIMULATION gate still runs harmlessly while the new engine is grown.

> **★ STANDING LESSON (carried, still in force): trust disk, never the doc — including this file.** Before any build that touches existing "built" code, a quick existence-and-shape check is owed. S14 honored this — step 1 of the engine build re-verified `append_reading`, `_validate_record`, the constants, the seal, the gold seal before touching anything.

---

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

**The line:** The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact. The AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time, even wonder/simulate forward at night — and do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**The crystallization:** **N.H is Ness's HELPER, not Ness's DECIDER.** A helper reads, connects, lays out what it sees, even leans — then hands it to the person, who decides. A decider closes the book.

**★ THE SOUL CORRECTION — three truths held at once, never collapsed:**
1. **Interpretive meaning is never stored as a universal fact — it remains a situated story** (§3G). There is no fact-box for *meaning*.
2. **Ness still decides / affirms.** He is the decider, the membrane. The system does NOT decide what is real — and neither does it pretend nothing is ever decided.
3. **★ His deciding is NOT a node in the engine.** It happens out in real life, engine absent. There is no step after "show." *(S13 cross-link: recording THAT he reacted is allowed — item 23's seam stores the OCCURRENCE as a dated, weightless story-layer event so a dismissed reading stops resurfacing. What stays off-board is the TRUTH-verdict.)*

**The crucial distinction:** "never decide facts" does NOT mean "never hold anything firmly." Something can be held with full weight and still never close the book.

**★ S13 SHARPENING:** the DUMB machinery MAY establish directly-verifiable machine-state & provenance facts (this file exists, this hash matches, this role came from source, this write succeeded). The SMART machinery MAY interpret, connect, lean — but may NEVER silently promote an interpretation into an established fact. The authority for any such promotion is Ness, off-board.

**★ S14 LIVE EXPRESSION OF §0 — the engine reads by PATTERN, so it can be wrong, and that is designed-around, not a flaw.** The mouth places a line by similarity to millions of lines it has seen; it does not truly understand. So it WILL misread sometimes. Every guard exists precisely because of this: never-close-the-book (a wrong read is a replaceable guess, never a fact), confidence (a shaky read is marked shaky), only-adds (a better read accretes beside a worse one), Ness-decides-off-board, and the gold (wrongness is caught on a sealed test before the engine is trusted). A system that assumed it was always right would be the dangerous one.

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame]

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The pure tape, the append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), role-carried-from-source, the catalog's who/when/where marking, CARRYING/STORING the `mode` label once SMART has named it, the person-box GATHER, the live loop's fire-and-let-go. One law: **never interpret, never close — only add / point / carry / sort / gather.** Safe BECAUSE it cannot interpret. *(NAMING the register is interpretation → produced by SMART, §6B's open-word `mode`.)*

> **★ THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety).** "Append-only" must NOT mean "permanent recoverable storage of every secret forever." Allowed: capture exclusions for credentials/secrets; encrypted storage; retention boundaries; cryptographic erasure of selected content; an append-only TOMBSTONE retaining THAT a deletion occurred without the deleted plaintext; special treatment for third-party and childhood data. Applies to the tape AND the sealed roots (seal protects from accidental MUTATION; still allows deliberate, audited destruction). Undesigned (§11 item 24).

> **★ "ABSENCE IS READ" NEEDS A GUARD.** Absence is meaningful ONLY when the system EXPECTED the info, the process was CAPABLE of observing it, the absence is relevant, and the interpretation is held WEAK. Otherwise missing-data artifacts become manufactured significance. Distinguish `not_observed`/`not_evaluated`/`not_applicable`/`withheld`/`collection_failed` in processing metadata; a blank in a reading stays honest (never `"unknown"`).

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
- **Verify on disk, never trust status reports.** *(S14 honored this as build-step-1 every time.)*
- **Honest correction over flattery** — explicitly, repeatedly asked for. *(S14: he asked directly "should I buy the RTX, tell me honestly" — the right answer was a real yes-but-later with reasoning, not a sale.)*
- **Don't inform, just flag and keep going.**
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, elongated punctuation are NOT distress.
- **He catches things.** When he pushes back, he is usually right. *(S14: he caught that an "attractiveness analysis" root Claude dismissed as junk was actually real-but-context-only-Ness-has — reinforcing that only Ness can sort his own material.)*
- **He works to UNDERSTAND before moving.** *(S14: he repeatedly stopped to fully grasp the gold / the engine / why-it-can-be-wrong before proceeding. This is not hesitation — it's him needing the mechanism to fit his head. Honor it; go slower, not faster.)*
- **He is not afraid of work.** A wall is almost never "this is hard" — it is "this move would destroy/forfeit something."
- **He re-derives his own design from the inside.** Offer shapes, let him rebuild and steer.
- **Backup before any destructive step, always.**
- **Primary risk pattern: scope-expansion before consolidation.** Finish and verify before the next thing. *(S14: the guard "build the smallest testable engine, don't broadly redesign" held — A before B before C, each tested.)*
- **Claude's role:** architecture, audit, security, strategy. Cursor writes code; Ness runs every command and verifies on disk.
- **Session workflow:** one topic per chat; end of session regenerate the master + a short delta. Ness prefers a fresh chat from a corrected master over a long session on fumes.

---

## 3. THE EVOLUTION — OLD vs NEW (key points)

- **A. Manual gate → MEMBRANE.** Memory only ADDS. [Accretive store BUILT; clean roots S12; sealed S13.]
- **B. Many "is this real?" gates → ONE UNIVERSAL FILTER.** [DESIGNED §7A; minimal engine A BUILT S14.]
- **C. AI creativity → the membrane.**
- **D. Security holes found on disk → fixed.** *(⚠ `cloudflared.exe` inert but on disk — convenience-sweep item.)*
- **G. Affirmation surface → per-person STORY-layers.** [DESIGNED.]
- **H. The person → PERSON-BOXES.** [DESIGNED §7B Part 2.6.]
- **I. "Do I train a model?" → BORROW A FROZEN MOUTH** (§16). [DESIGNED + on disk.]
- **J. (S12) The store — from a 188-stub → 5,521 CLEAN roots.** [BUILT & VERIFIED.]
- **★ K. (S14) The reading record — from DESIGNED-NOT-CODED → BUILT validator + writer + a working minimal engine + a sealed gold.** [BUILT & VERIFIED.] The reading layer is now real plumbing with a first engine writing through it.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2). Python **3.13.14**.
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM). **Motherboard ASRock B560 Pro4** (PCIe x16, 8-pin PCIe power available). **Case Antec NX410.** 32 GB RAM. *(Verified by inspection S14.)*
- **Launched via** `run_app.pyw` → pywebview at `http://localhost:8080/`. The CORE is LOCAL and offline by default; only the optional research connectors touch the network.
- **★ MODEL HARDWARE REALITY:** the 6GB 2060 runs 3B models normally (~35–50 tok/s); 7B/8B run but SLOW (~7–9 tok/s). **★ S14 UPGRADE PATH (optional, NOT a blocker):** Hebrew reading is gated on running a bigger model, which needs more VRAM than 6GB. The known cheap fix is a **used/new RTX 3060 12GB (~₪1,400–1,800 in Israel; Ivory ~₪1,410, compare on Zap).** Get the **12GB** version, never 8GB — VRAM is the number that matters. It physically fits this machine (slot, space, PCIe power all confirmed); the only buy-time check is PSU wattage (want 550W+; if under, add a ~₪200 PSU). **WHEN to buy: not on a deadline — when the engine is far enough along that weak Hebrew is actually blocking real understanding, AND the money is comfortable (not last savings). Hebrew is "weak-but-workable" on dolphin until then.**
- **Windows sign-in:** Kensington VeriMark fingerprint key.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` · `nh_context_router.py` · `nh_reality_graph.py` · `nh_simulation_graph.py` · `nh_epistemic_sandbox.py` · `nh_evidence_integrity.py` · `nh_jarvis_core.py` · `nh_crypto.py` · `nh_vector_memory.py`. *(OLD REALITY/SIMULATION gate stack — still runs harmlessly; do NOT rip out before the new filter is complete.)*

**Physical stores on disk (verified S14):**
- **`.nh_accretive_store.jsonl` — 5,521 CLEAN roots, SEALED** (7-field). Roots-of-record.
- **`.nh_roots.sealed`** — seal marker (0 bytes, 06/22 23:05). `append_root` refuses while it exists.
- **`.nh_readings_store.jsonl`** — production readings sibling. **ABSENT** (no production readings yet — correct).
- **`.nh_readings_quarantine.jsonl` (S14)** — the QUARANTINE test readings file. The minimal engine writes here, never production.
- **`NH_GOLD_SET_v1.md` (S14)** — the sealed gold answer key (8 cases, 4,951 B).
- **`.nh_gold_v1.sealed` (S14)** — gold seal marker (0 bytes).
- Backups: `.bak_preseal` (roots), `.bak_188_preclean`, `nh_accretive_store.py.bak_pre_minimal_engine_A_*` (S14).
- **`chroma_db\` — ChromaDB ≈ 1.78 GB.** `nh_reality_core` = 116,391 (OLD index — rebuild later, keep until proven), `nh_test_asm` = 1,180, `nh_simulation_core` = 263.

**Source files on disk:** `conversations-000/001/002.json` (all INGESTED CLEAN S12). `gpt_purified_history.txt` + `cleaned_history (1).txt` (NOT ingested — redundant/damaged).

**Models on disk (verified S14):** Ollama `dolphin-llama3:latest` (UNCENSORED, 4.7 GB, 8B — **the chosen mouth**) · `llama3:latest` (4.7 GB, 8B) · **`huihui_ai/qwen2.5-abliterate:3b` (1.9 GB — pulled S14 for the Hebrew test; read worse than dolphin, NOT adopted)**. `models\all-MiniLM-L6-v2` (embedding/search + detector embedding model).

**Accretive store + tooling [BUILT & VERIFIED]:**
- **`nh_accretive_store.py`** — restored S12, extended S13, extended S14. Append-only; schema validated before every append. **S14 additions:** `_check_common` (shared id+timestamp); `_validate_reading` (12-field shape gate); reading-shaped `append_reading` (root-verify + idempotency + atomic append, optional target `path`); `QUARANTINE_READINGS_PATH` constant. `_validate_record` now delegates id/timestamp to `_check_common`.
- **`nh_engine_minimal.py` (S14, NEW)** — the minimal engine (A): `read_root(root_id)` → mouth → 12-field reading → quarantine; `run_on_gold()` lays the 8 reads beside the gold for manual review (no auto-scoring). Mouth model in a `MOUTH_MODEL` constant (currently `dolphin-llama3`).
- **`test_reading_validator.py` / `test_minimal_engine_dryrun.py` (S14)** — fixture harnesses (temp paths only).
- `nh_ingest_chatgpt.py`, `verify_rt.py`, `nh_log.py`, `nh_probe*.py`, the S13 detector probes (`nh_embed_confirm_speaker.py` = the recipe reference).

**`.cursorrules` v3.1 (in-force):** §6A. **⚠ Still describes the OLD root schema (no role) and the one-gate model — reconciliation owed.** *(S14 note: `_validate_record`'s docstring still references "the existing 188 seed records" — stale wording, code correct; fold into the same cleanup.)*

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **★ THE CLEAN ACCRETIVE STORE — 5,521 roots, 7-field, role-carried, SEALED.**
- **★ 2a COMPLETE: two-file routing + sealed roots + the READING RECORD (validator + writer, 12-field contract) — BUILT & VERIFIED (S14).**
- **★ THE GOLD SET v1 — 8 cases, SEALED (S14).**
- **★ A MINIMAL ENGINE (A) — BUILT & RUN against the gold (S14).** Writes to quarantine only.
- The restored store module + clean ingest pipeline.
- The speaker-detector recipe INVESTIGATED & PROVEN (~94.89%), NOT deployed.
- The OLD REALITY/SIMULATION gate (still runs) · encryption at rest · §3D security fixes.
- The OLD populated vector memory (~1.78 GB, 116k `nh_reality_core` — to be rebuilt).
- Three local models in Ollama (dolphin, llama3, qwen2.5-abliterate-3b).

**Known regression pattern:** verify on disk; the doc's remembered state has been wrong repeatedly.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE — pre-S12, needs reconciliation)

*The in-force ruleset Cursor obeys. §§0–11 IN FORCE; §12 INCOMING. The §0 premise, §0A frame, §3G story rework, §16 model layer, person-boxes, tape, the clean store, the 7-field root, the two-destinations shape, AND the S14 reading-record code are DESIGN/NEW that EXTEND §7A and the §12 INCOMING block; they do NOT silently rewrite the in-force body. Disk `.cursorrules` is authoritative for the in-force body. Reconciliation to the 7-field root + the reading-record contract is owed.*

---

## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED]

*The DUMB-MACHINERY heart (§0A). Append-only; schema validated before every append; roots file SEALED.*

**★ ROOT record schema (SEVEN fields):** `id` (uuid4) · `subject` · `timestamp` (ISO 8601) · `content` · `re_reads` (list; `[]`=root) · `source_title` (string/None) · `role` (speaker from source; required on new writes).

**★ READING record schema — BUILT & VERIFIED (S14), 12 fields:** `id · reads · meaning · confidence · role · story_layer · mode · timestamp · produced_by · schema_version · derived_from · idempotency_key`. A reading NEVER copies root text — it points (`reads`). Show = read readings → follow `reads` into sealed roots → stitch. A re-read is a NEW reading beside the old. The validator (`_validate_reading`) gates SHAPE, never confidence: reject malformed, never reject uncertain.

- **`reads`** — list of root id(s), non-empty; the writer verifies each exists in the sealed roots before commit.
- **`meaning`** — the read (string). The honest insufficient-context read ("seen this, couldn't read it") is a VALID meaning.
- **★ `confidence` = a TWO-SLOT OBJECT (S14, DECIDED).** `{ interpretation_confidence, source_reliability }`, never a bare number. `interpretation_confidence` = how sure the engine is of THIS reading (present on every reading; value-form deliberately loose for now). `source_reliability` = how trustworthy the source was — SLOT present from the first reading, VALUE empty/omitted until the engine can honestly judge a source (empty-when-unknown is honest). NEVER blended; confidence never rises from copied error; a reading never inherits a prior's confidence. The other two "kinds of sure" live elsewhere: **story firmness** inside `story_layer[].firmness`; **retrieval relevance** computed at search time, never stored.
- **`role`** — who spoke, from the root.
- **`story_layer`** = a LIST of tellings (clash kept, nothing wins). Each: optional `whose · stance · firmness · telling · theme · when`. Empty list legal. Unknowns OMITTED, never `"unknown"`.
- **`mode`** = `{ label (open word: chat/composed/story/question/…), classification_confidence (local) }`. Not a fixed menu. `classification_confidence` is LOCAL, ≠ top-level confidence.
- **`produced_by`** = reproducibility-grade provenance. `origin` ∈ {observed, imported, simulated, generated, reaction, human_annotation} (REQUIRED). Engine readings carry model/digest/engine_version/prompt_version/config/retrieval_inputs — **validated if present, not hard-required (S14 loosening: an early engine reading missing e.g. `prompt_version` still passes; only `origin` is mandatory).** `human_annotation` readings (gold) carry annotator/when/context_version/change_reason.
- **`schema_version`** = present on every NEW record, `v1` for the first. Un-retrofittable. Pinning the confidence value-form later = a new version.
- **`derived_from`** = list of parent reading ids; `[]` when fresh from roots. Governing rule: derived material is never independent evidence; one lineage = one evidence path.
- **`idempotency_key`** = operation identity, separate from `id`; the writer rejects an already-committed key.
- **`timestamp`** = CREATION time (≠ source/event/ingest).

**★ ON DISK NOW (verified S14):** 5,521 clean root records, SEALED, all `re_reads=[]`. Production readings file ABSENT. **Quarantine readings file holds the minimal engine's gold-run output** (test-only). The validator + writer are live; the engine writes real readings through them into quarantine.

**No `reason`/`why` field, by design** — the why is shown by what a layer points at; the AI's view is the NOTE (§7B Part 7.5).

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [DESIGNED — minimal engine A BUILT]

### 7A — THE UNIVERSAL FILTER (operating rules):
R0 reader/layer-er not judge; R0.5 never close the book; R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; R5.5 the affirmation surface is a per-person STORY-layer (six optional parts; absence read ONLY under the §0A guard; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE); R6 memory only ADDS (governs HISTORY; the COMPUTED VIEW decides current use); R7 the membrane; R8 associative bridging; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is.

### 7B — THE MEANING ENGINE (mechanism):
Part 0 THE PURE TAPE (verbatim, append-only, outside memory; capture-exclusions + audited redaction — §0A); Parts 1–2 the chain of webs; Part 2.5 THE STORY-LAYER WEB; Part 2.6 PERSON-BOXES; Part 3 webs combine; Part 4 nightly research (feeds MEMORY, not the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask); Part 6.5 THE WONDER/SIMULATION; Part 7 THE LOG; Part 7.5 THE NOTE/THE WHY.

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots + READING RECORD — ✅ COMPLETE (S14).** → **(2b) the detector — ✅ INVESTIGATED, recipe locked (S13); fallback, not deployed.** → **(2c) THE ENGINE — STARTED (S14):** a minimal engine (A: meaning + role) is BUILT and tested against the sealed gold. **Grow it: A ✅ → B (add context-search) → C (add story-layer).** B and C each need their OWN gold cases (requiring context / having a story) before they're testable. **Build the LIVE path before the nightly deepening.**

**★ THE ENGINE LAYERS (S14 design):**
- **A (BUILT):** root → mouth ("say what the {role} is doing, don't describe/answer/invent") → 12-field reading → quarantine. Bare; no context, no story.
- **B (NEXT):** + context-search — pull nearby roots by meaning before the mouth reads, so it reads in context. Needs the search model wired AND context-requiring gold cases.
- **C (AFTER B):** + story-layer reading — fill `story_layer` (whose/firmness/theme). Needs story-bearing gold cases.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. Findings land in MEMORY as readings, never the mouth.

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]
Access/auth; mobile three modes; interactive canvas; behavioral-baseline wellbeing; HUD redesign; person-boxes gather; image front door (§9A); phone-data importer; memory browser; voice in/out; ChromaDB cleanup; folder cleanup.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Metadata → plain-description → context-meaning → Ness confirms. Precondition for WhatsApp media (§12).

## 10. ORIGINALITY (honest calibration)
The combination ships nowhere: inverted default + per-person never-closing STORY + DUMB/SMART split + person-boxes-as-gather + pure tape + wonder-kept-and-shown + memory-grows-not-the-mouth + two-destinations/two-files. Never claim inventing local AI, approval gates, or a trained model.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ BUILT, 5,521 sealed. (c) wire into live flow — part of model-wiring/live-path.
2. **THE FORCED ORDER — 2a ✅ COMPLETE → 2b ✅ → 2c STARTED:** minimal engine A built & tested. **NEXT: grow the engine — B (context), then C (story). LIVE path before nightly.**
2b. **THE DETECTOR — recipe locked, live build deferred.** Fallback for role-less sources.
3. **★ THE MODEL WIRING (§16) — local-first.** Wire dolphin (mouth) + embedding search. **CHROMA REBUILD lives here** (rebuild from the 5,521 clean roots; keep old 116k until proven). **Forks:** 8B-now vs 3B-fast (S14: 3B abliterate read worse — 8B dolphin stays); **Hebrew quality gated on a bigger model → RTX 3060 12GB (§4, §16), optional/buy-time;** VRAM-vs-context dial.
4. **NIGHT-SEARCH (committed, LATER).** Feeds MEMORY as readings.
5. **Image-ingest front door (§9A).**
6. **Universal Filter / meaning engine** — = item 2's (2c), now in progress.
7. **ChromaDB rebuild/cleanup** — do NOT destroy the old 116k before the new is proven.
8. **Research pipeline build.**
9. **Hetzner sovereignty sync.**
10–12. nh_service (✅ disabled) · mobile + canvas · HUD redesign.
13. **THE [BUILT]-CLAIMS SWEEP — ✅ DONE (S13).** Future builds owe a quick existence-and-shape check.
14. **Folder cleanup** — `cloudflared.exe`; stale `peek.txt`; the ~12 S13 detector probes (keep the recipe reference); **the stale "188 seed records" docstring in `_validate_record` (S14)**.
15. **§11.15 STORE-COUNT RECONCILIATION — ✅ CLOSED BY ACTION (S12).**
16. **WhatsApp archive → eventual ingest (deferred):** decrypt → SQLite front door → image front door → child-data call → ingest only with engine.
17. **Open design threads (low):** spine re-draw; old gate lags; `.cursorrules` reconciliation (7-field root + reading-record contract + the stale docstring); clash/gap UI surfacing; write the §0A DUMB/SMART section into final place; ~24 unreviewed Cursor batch files; person-box multi-box tagging.
18. **MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned. Must be designed before a SECOND batch is written.** Batch naming, root-id→batch resolution, manifest, cross-batch dedup, read_all-over-many-boxes, crash-safety. Likely: append-only manifest + batch-prefixed addressing.
19. **★ CONFIDENCE — RESOLVED (S14).** Was: one number hides four (interpretation confidence · source reliability · story firmness · retrieval relevance). **Decision: a TWO-SLOT `confidence` object** (interpretation_confidence + empty-until-knowable source_reliability); firmness lives in story_layer; relevance computed at search. Never blended; no false corroboration; no inherited confidence. The value-FORM (low/med/high vs 0–1) is deliberately loose, pinned later as a new schema_version. The anti-inheritance anchors (`produced_by`, `schema_version`, `derived_from`) are built.
20. **★ "UNDERSTANDING" — gold-standard set BUILT & SEALED (S14); the locked sequence advanced.** Steps: (1) disk-verify ✅; (2) confidence representation ✅ DECIDED; (3) gold format ✅ + scoring rule ✅ DECIDED; (4) annotate + SEAL gold ✅ (8 cases sealed); (5) reading validator + writer ✅ BUILT; (6) minimal engine into quarantine ✅ BUILT & RUN; (7) compare to sealed gold ✅ DONE (first pass: ~5–6/8 solid after prompt+role fixes; remaining misses are model-quality, not engine bugs).
>    - **THE GOLD CASE UNIT** = target root + frozen allowed-context + annotation. (The 8 v1 cases are clean-bare: context = "the line stands alone.")
>    - **THE GOLD SEAL** = v1 sealed before any engine output seen; output may FAIL but not ALTER; a correction is a NEW versioned gold. ✅ on disk.
>    - **THE SIX SCORING RULES (DECIDED S14)** — see the S14 lock block above.
>    - **ENGINE FAILURE-BEHAVIOR (DECIDED S14)** = honest insufficient-context reading, marked revisable; retry-trigger deferred.
>    - **S14 BUILD-LESSONS:** building gold is partly SORTING (keep clean roots, drop unfair ones); only Ness can tell "junk" from "real-but-context-only-Ness-has"; a bare prompt makes the mouth DESCRIBE or ANSWER instead of reading WHAT THE PERSON IS DOING (fixed by sharpening the prompt + passing role); the mouth is non-deterministic run-to-run (a temp-0 setting would stabilize — deferred); mode-tagging lags meaning (tags questions as "answer" sometimes — deferred).
21. **RE-READ LIFECYCLE + THE VIEW LAYER — NAMED, not designed.** Append-only HISTORY underneath + a COMPUTED CURRENT-USE VIEW above (current/contradicted/superseded/rejected/low-confidence/historically-weak); retrieval reads the VIEW. **INTERPRETATION-INTEGRITY CONSTRAINT:** the more inferential a reading, the easier it must be to trace, challenge, suppress, replace in the view. Build after the engine produces real readings to view.
22. **PERSON-BOX CONTAMINATION — needs per-element provenance.**
23. **OFF-BOARD AFFIRMATION FEEDBACK SEAM** — record Ness's accept/reject as a dated, weightless STORY-LAYER EVENT (not a promoted fact); feeds the view's `rejected` bucket.
24. **PRIVACY / THREAT MODEL + REDACTION PATH — first-class before sensitive ingest.**
25. **GO-LIVE HARDENING BLOCK — DEFERRED, does NOT gate the engine.** Injection / identity resolution / time semantics / audit-log integrity / backup-restore TESTING / dependency locking / resource limits / observability / degraded mode / process boundaries. **`schema_version` is the near-term hook — ✅ now on every reading from the first (S14).**
26. **MODEL-REPLACEMENT DEFAULT (near-settled).** A new mouth passes the SEALED gold before replacing; old readings keep old `produced_by`; no auto mass re-read. **S14 reinforced this concretely: dolphin vs qwen-abliterate was run against the gold; dolphin won and stayed. The gold IS the model-swap bench.**
27. **QUARANTINE PHASE + BOOTSTRAP RETRIEVAL RULE — DESIGNED; quarantine STORE now BUILT (S14).** Validator success permits only TEST execution → a SEPARATE quarantine store (✅ `.nh_readings_quarantine.jsonl` exists, holds the engine's gold-run output). Quarantine readings do NOT enter retrieval/answers/person-boxes/production. Promotion needs gold + held-out + manual inspection. BOOTSTRAP: early runs read raw roots + human-affirmed material; prior machine readings excluded/low-trust; no machine reading auto-feeds the next. "human-affirmed" = approved-for-context, still a dated revisable reading. MEMORY-HEALTH CHECKS deferred.

---

## 11-SETTLED. (condensed)
- **S4–S11:** unit = span-claim; carry `role`; borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction; memory-grows-not-the-mouth; two-file 2a.
- **S12:** store restored; `role` added (7-field root); clean ingest; 5,521 clean roots; Chroma=old 116k index; two-destinations shape.
- **S13:** [BUILT]-sweep done; 2a plumbing built; roots sealed; detector recipe locked (94.89%); eleven doc-refinements + quarantine/bootstrap captured.
- **★ S14:** the three forks CLOSED — confidence = two-slot object; gold scoring = six rules (semantic match, Ness judges); failure-behavior = honest insufficient-context, revisable. Reading validator + writer BUILT & VERIFIED (17/17 tests; roots regression clean). Gold set v1 (8 cases) SEALED. Minimal engine A BUILT & run against gold (~5–6/8 after prompt+role fixes). Model test: dolphin beats qwen-abliterate-3b; Hebrew gated on bigger model/VRAM → optional RTX 3060 12GB. Validator structure = extract-not-fuse (`_check_common`). Quarantine store built. Confidence value-form left loose.

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

**★ TWO MODELS, TWO JOBS.** (a) WORDING/generation — the mouth (heavy); (b) SEARCHING/retrieval — the embedding model (tiny). **ORDER: search first, word last.** On disk: `all-MiniLM-L6-v2` + ChromaDB. *(Rebuild Chroma from the 5,521 clean roots when wiring search; keep the old 116k until proven.)*

**★ GROWTH LANDS IN THE MEMORY, NEVER THE MOUTH.**

**THE DECISION — LOCAL-FIRST.** Sovereign, offline, private, uncensored. The model is swappable behind the meaning step.

**★ S14 — THE MOUTH IS uncensored BY DESIGN, AND CAN'T BE FAKED.** Censorship lives in a model's weights, not as a rule on top — Jarvis can't reliably make a censored model stop refusing (prompts help, but it'll still refuse/sanitize on heavy material). The right move is choosing a model TRAINED uncensored (or abliterated). `dolphin-llama3` is exactly that — why it was chosen.

**★ S14 — THE HEBREW FINDING (tested on real Hebrew, the open fork answered).** Pulled `huihui_ai/qwen2.5-abliterate:3b` (uncensored Qwen, Hebrew-strong family) and ran the SAME sealed gold through it vs `dolphin-llama3`. Result: the abliterated 3B read WORSE — collapsed to bare stubs ("the user is stating."), gave up on the Hebrew cases entirely. Abliteration cost + 3B too small. **dolphin-llama3 remains the best mouth on disk; the engine reverted to it.** **Conclusion: meaningfully better Hebrew is MODEL-SIZE-gated, not prompt-fixable** — it needs a bigger model, which needs more VRAM than the 6GB 2060 holds. The cheap path is an RTX 3060 12GB (§4): **optional, buy-when-comfortable-and-actually-blocked, NOT a blocker.** Free interim patch if Hebrew ever blocks before the card: translate Hebrew→English before the mouth reads (logged, not built). Hebrew on dolphin today = "weak-but-workable."

**ON-DISK STATE + FORKS:** `dolphin-llama3` (8B, uncensored — THE MOUTH) · `llama3` (8B) · `qwen2.5-abliterate:3b` (test, not adopted) · `all-MiniLM-L6-v2` (search). Runtime Ollama, GGUF. **FORK (i):** 8B-now vs 3B-fast — S14: 3B abliterate worse, 8B stays. **FORK (ii):** Hebrew — bigger model needed, RTX 3060 12GB path. **FORK (iii):** VRAM-vs-context dial. **FUTURE (optional):** RTX 3060 12GB.

---

**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board** · **the engine reads by PATTERN and CAN be wrong — that is designed-around, not a flaw (§0, S14)** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary** · **the affirmation surface is a per-person STORY — never closed; absence read only under the §0A guard; N.H is NOT a teller** · **TWO DESTINATIONS: every eligible input → raw root (sealed) + a reading beside it; this is why two files — and the reading record is now BUILT (validator + writer, 12-field, S14)** · **`story_layer` is a LIST so clash is kept; `mode` is an OPEN word; `confidence` is a TWO-SLOT object never one blended number (S14); unknowns OMITTED** · **CARRY THE SPEAKER, DON'T GUESS IT — `role` on the root, from source; detector a fallback** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE preserves eligible events append-only — subject to capture-exclusions + audited redaction** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; uncensored by choice (can't be faked); local-first; night-search feeds the MEMORY not the mouth; never train a base model; Hebrew quality is model-size-gated, an optional RTX-3060-12GB upgrade, not a blocker** · **THE GOLD IS A SEALED OUTSIDE EXAM the engine must pass to be trusted — built & sealed (S14); the engine reads like Ness or it doesn't, and only Ness judges** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id** · **ONE FILTER, BOTH DIRECTIONS** · memory only adds (history grows; the computed view governs live use) · the membrane · a unit is a span-claim · input-agnostic, many front doors · archive don't ingest · הכל יחסי · don't overclaim · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen, uncensored mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — where the reading record is now real built plumbing (a twelve-field validator and writer, gating shape not certainty, with confidence held as two honest slots rather than one blended number), and a first small engine already reads a root and lays a reading beside it, judged against a sealed gold answer key that only Ness can grade because the whole spec is "does it read the way Ness's mind reads" — and when the engine is wrong, as a pattern-reader sometimes must be, nothing breaks, because a wrong reading is a replaceable guess marked with its own uncertainty, never a fact; so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone — the dumb machinery holds the data and cannot interpret, the smart machinery reads the person and cannot close, the membrane stands between them, the mouth is a swappable tool that grows nothing while all the growth lands in the understood memory it speaks from (and reads Hebrew only weakly until a bigger mouth on a bigger card is worth buying, which is later, not now), and where two tellings disagree the system shows the clash rather than choosing — because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
