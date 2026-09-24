# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, AND the code rules — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–13. Session 14 (June 23 2026) was a DESIGN-then-BUILD session → MASTER-15. S14 closed the three genuinely-open forks AND shipped the next build. Session 16 (June 24 2026) was a BUILD session → MASTER-16. S16 built Engine B (context-search), gold v2-B (7 sealed context-requiring cases), and the Chroma rebuild (`nh_roots_v1`). Hardware upgrade path decided. Engine B scored 6.5/7 on dolphin 8B — dolphin's ceiling, not an engine bug.*

*★ The DECISION-DEFAULTS file should be regenerated as S16, synced to this master.*

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
> | Engine B (`nh_engine_b.py`) | **BUILT & RUN (S16)** | root → preceding turns → BACKGROUND prompt → mouth → 12-field reading → quarantine; run against gold v2-B; 6.5/7 — dolphin 8B ceiling |
> | Chroma `nh_roots_v1` (5,521 clean roots) | **BUILT (S16)** | rebuilt from clean roots via `nh_rebuild_chroma.py`; cosine distance; `all-MiniLM-L6-v2` embeddings |
> | `nh_rebuild_chroma.py` | **BUILT (S16)** | dry-run verified; full run 187.59s; keeps old collections untouched |
> | Production readings store (`.nh_readings_store.jsonl`) | **ABSENT (correct)** | no production readings yet; quarantine-only by design |
> | Speaker detector recipe (embed+shape→LogReg C=0.1→94.89%) | **INVESTIGATED & PROVEN, NOT DEPLOYED** | fallback only |
> | Ingest pipeline (`nh_ingest_chatgpt.py`) | **BUILT & VERIFIED** | S12 |
> | Chroma `nh_reality_core` (116,391) | **BUILT — OLD/unaligned index** | keep until `nh_roots_v1` proven; do NOT destroy |
> | The engine (2c) — full chain of webs | **PARTIALLY BUILT (A + B; C not built)** | A = meaning + role; B = + preceding context; C (story) NOT built |
> | Mouth model choice | **dolphin-llama3 = best on disk (S14/S16)** | tested vs `qwen2.5-abliterate:3b` — dolphin won; B gold confirmed dolphin's 8B ceiling |
> | Hebrew reading quality | **WEAK-BUT-WORKABLE; gated on bigger model/VRAM** | §16 — not prompt-fixable; RTX 5060 Ti 16GB upgrade path decided (S16) |
> | Hardware upgrade path | **DECIDED (S16)** | RTX 5060 Ti 16GB, ~₪2,590, פי.סי סנטר, 3yr warranty; buy 5.7.2026; target model: `dolphin-llama3.1:13b` |
> | Multi-box (sealed-batch) architecture | **NOT DESIGNED** | §11 item 18 |
> | View layer | **NAMED, NOT DESIGNED** | §11 item 21 |
> | Quarantine promotion + memory-health checks | **DESIGNED, NOT BUILT** | §11 item 27 |
> | Pure-tape redaction/destruction path | **NOT DESIGNED** | §0A correction + §11 item 24 |
> | Confidence value-form (low/med/high vs 0–1) | **DELIBERATELY LOOSE** | validator checks present+non-empty only; pinning later = new schema_version |
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
>    - **Engine B** (`nh_engine_b.py`): root → `_get_preceding_turns(n=3)` → BACKGROUND prompt → mouth → 12-field reading → quarantine. 6.5/7 on gold v2-B. B3 failure = dolphin 8B model-size ceiling, not engine bug.
>
> **4. ★ ENGINE B DESIGN DECISIONS (S16 — protect from re-litigation):**
>    - **Context strategy = POSITION-BASED, not semantic search.** `_get_preceding_turns` finds the N roots immediately before the target in the same `source_title` thread. Semantic search (`nh_roots_v1`) was tried first — pulled topically related roots but not conversational context. Position-based is the correct lever for conversational turns.
>    - **n=3 preceding turns, FULL content (no truncation).** Truncation at 100 chars was killing context quality — removing it fixed B5 ("Brief slow." read correctly only with full preceding assistant turn visible).
>    - **BACKGROUND/END BACKGROUND prompt framing (DECIDED S16).** Prevents the mouth from answering or continuing the conversation instead of reading the target line. The four rules: do not reference background, do not quote/paraphrase background, do not invent, if short confirmation say what they are confirming based on topic.
>    - **Engine B ceiling on dolphin 8B = 6.5/7.** B3 fails because the mouth reads the content of the chosen option instead of the act of choosing — textbook 8B role-separation gap. Context correct, prompt correct, model too small. A 13B resolves this.
>    - **Full-thread reading = future goal.** Load entire conversation thread as context before reading each line. Requires 13B + larger context window (8k-16k tokens). Not possible on dolphin 8B / 6GB VRAM. Unlock after RTX upgrade.

> **★ DECISIONS LOCKED IN SESSION 14 (protect from re-litigation):**
> - **`confidence` = a TWO-SLOT object** `{ interpretation_confidence, source_reliability }`. `interpretation_confidence` filled on every reading; `source_reliability` slot-present from the first reading but left EMPTY until the engine can honestly judge a source. NEVER one blended number; confidence never rises from copied error; a reading never inherits a prior's confidence. Story firmness inside `story_layer[].firmness`; retrieval relevance computed at search time, never stored. `mode.classification_confidence` is local and separate. SETTLED.
> - **GOLD SCORING — six rules.** (1) `meaning` judged by SEMANTIC match; Ness decides same/not-same by hand. (2) `story_layer` NOT graded in v1/v2-B. (3) MAKING SOMETHING UP is the real fail; leaving something out is NOT a fail if what's said is right. (4) Correct-but-EXTRA: true extra passes, made-up extra fails. (5) A case MAY list several acceptable readings. (6) NESS decides pass/fail; model assists, never judges. SETTLED.
> - **ENGINE FAILURE-BEHAVIOR.** When the engine can't interpret a root: writes an honest INSUFFICIENT-CONTEXT reading, MARKED revisable. Retry-trigger DEFERRED. SETTLED.
> - **CONFIDENCE VALUE-FORM left deliberately LOOSE** — validator checks present+non-empty only; pin later as new schema_version. SETTLED-as-deferred.
> - **VALIDATOR STRUCTURE = option C (extract, don't fuse).** `_check_common` holds shared id+timestamp. SETTLED + BUILT.
> - **MODEL FINDING (S14):** dolphin-llama3 beats qwen2.5-abliterate:3b. Hebrew quality is model-size-gated. SETTLED-as-finding.

> **★ DECISIONS LOCKED IN SESSION 16 (protect from re-litigation):**
> - **HARDWARE UPGRADE PATH.** Target: RTX 5060 Ti 16GB (Gigabyte AERO OC, model GV-N506TAERO OC-16GD). Store: פי.סי סנטר, 1,324 reviews, 4.71★, 3-year warranty. Price: ~₪2,590. Buy date: 5.7.2026 (שירות לאומי payment arrives; total funds ~₪3,507). PSU check still needed (Antec NX410; want 550W+; budget ~₪200 if needed). **Why this card:** 16GB VRAM runs dolphin-llama3.1:13b at ~20-25 tok/s; newer architecture than 3060/4060 Ti; cheaper than 4060 Ti 16GB (₪2,621). **Why NOT:** RTX 4060 8GB / 5060 Ti 8GB = insufficient VRAM (confirmed trap on Zap — listings show 16GB but model number ends in 8GD). RTX 3060 12GB = valid but ₪1,964 used, slower, less VRAM. **NEVER buy a card with <12GB VRAM for N.H.** VRAM is the only number that matters.
> - **TARGET MODEL AFTER UPGRADE.** `dolphin-llama3.1:13b` — uncensored by training (same dolphin family), 13B, fits in 16GB VRAM. Model swap rule: pull it, run against BOTH sealed gold sets (v1 + v2-B), verify scores improve before adopting. Old readings keep old `produced_by`. No auto mass re-read.
> - **ENGINE B CONTEXT STRATEGY = POSITION-BASED.** Settled. Do not re-open as semantic search.
> - **ENGINE B PROMPT = BACKGROUND/END BACKGROUND FRAMING.** Settled. Do not re-open.
> - **COST NOTES CONFIRMED.** N.H current monthly cost = $0. At full nightly automation (far down build list): Brave ~$62/month + OpenRouter synthesis ~$60-240/month = ~$120-300/month total. During building/testing: $0 (inside $5 free Brave credit). **SAFETY NOTE (build requirement for item 8):** Brave has NO spending cap — a loop can bill without stopping. When research pipeline is wired, a query counter / daily cap MUST be in the code. Not optional.

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

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. As of S16: the clean store + role schema + ingest pipeline + 2a plumbing + reading record (validator + writer) + gold sets v1 + v2-B (both sealed) + engine A + engine B + Chroma `nh_roots_v1` are all **[BUILT]**. Engine C (story), the view layer, person-boxes, tape, wonder, catalog are **[DESIGNED]**.

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

> **★ THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety).** "Append-only" must NOT mean "permanent recoverable storage of every secret forever." Allowed: capture exclusions for credentials/secrets; encrypted storage; retention boundaries; cryptographic erasure of selected content; an append-only TOMBSTONE retaining THAT a deletion occurred without the deleted plaintext; special treatment for third-party and childhood data. Undesigned (§11 item 24).

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
- **Primary risk pattern: scope-expansion before consolidation.** Finish and verify before the next thing.
- **Claude's role:** architecture, audit, security, strategy. Cursor writes code; Ness runs every command and verifies on disk.
- **Session workflow:** one topic per chat; end of session regenerate the master + decision defaults. Ness prefers a fresh chat from a corrected master over a long session on fumes.

---

## 3. THE EVOLUTION — OLD vs NEW (key points)

- **A. Manual gate → MEMBRANE.** Memory only ADDS. [Accretive store BUILT; clean roots S12; sealed S13.]
- **B. Many "is this real?" gates → ONE UNIVERSAL FILTER.** [DESIGNED §7A; engine A BUILT S14; engine B BUILT S16.]
- **C. AI creativity → the membrane.**
- **D. Security holes found on disk → fixed.** *(⚠ `cloudflared.exe` inert but on disk — convenience-sweep item.)*
- **G. Affirmation surface → per-person STORY-layers.** [DESIGNED.]
- **H. The person → PERSON-BOXES.** [DESIGNED §7B Part 2.6.]
- **I. "Do I train a model?" → BORROW A FROZEN MOUTH** (§16). [DESIGNED + on disk.]
- **J. (S12) The store — from a 188-stub → 5,521 CLEAN roots.** [BUILT & VERIFIED.]
- **★ K. (S14) The reading record — from DESIGNED-NOT-CODED → BUILT validator + writer + engine A + sealed gold v1.** [BUILT & VERIFIED.]
- **★ L. (S16) Engine B — from NOT BUILT → BUILT & RUN at 6.5/7 on sealed gold v2-B. Chroma rebuilt from clean roots. Hardware upgrade path decided.**

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2). Python **3.13.14**.
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM). **Motherboard ASRock B560 Pro4** (PCIe x16, 8-pin PCIe power available). **Case Antec NX410.** 32 GB RAM. *(Verified by inspection S14.)*
- **Launched via** `run_app.pyw` → pywebview at `http://localhost:8080/`. The CORE is LOCAL and offline by default; only the optional research connectors touch the network.
- **★ MODEL HARDWARE REALITY:** the 6GB 2060 runs 3B models normally (~35–50 tok/s); 7B/8B run but SLOW (~7–9 tok/s). Context window is limited.
- **★ S16 UPGRADE PATH (DECIDED — buy 5.7.2026):** Engine B hit dolphin 8B's ceiling at 6.5/7. The fix requires a 13B model, which requires 12GB+ VRAM. **Target card: RTX 5060 Ti 16GB** (Gigabyte AERO OC, model GV-N506TAERO OC-16GD, ~₪2,590, פי.סי סנטר, 3-year warranty). Buy on 5.7.2026 when שירות לאומי payment arrives (total ~₪3,507). PSU check needed at buy time (want 550W+; budget ~₪200 for PSU if needed). **VRAM is the only number that matters — never buy <12GB for N.H.** Get the 16GB version specifically (model number ends in 16GD, not 8GD). After install: `ollama pull dolphin-llama3.1:13b`, run against both sealed gold sets, verify scores improve before adopting. **Future goal after upgrade:** full-thread reading — load entire conversation thread as context before reading each line. Requires 13B + larger context window (8k-16k tokens).
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
- **★ ENGINE B (`nh_engine_b.py`) — BUILT & RUN against gold v2-B (S16). 6.5/7 — dolphin 8B ceiling.**
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

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [DESIGNED — engines A + B BUILT]

### 7A — THE UNIVERSAL FILTER (operating rules):
R0 reader/layer-er not judge; R0.5 never close the book; R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; R5.5 the affirmation surface is a per-person STORY-layer (six optional parts; absence read ONLY under the §0A guard; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE); R6 memory only ADDS (governs HISTORY; the COMPUTED VIEW decides current use); R7 the membrane; R8 associative bridging; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is.

### 7B — THE MEANING ENGINE (mechanism):
Part 0 THE PURE TAPE (verbatim, append-only, outside memory; capture-exclusions + audited redaction — §0A); Parts 1–2 the chain of webs; Part 2.5 THE STORY-LAYER WEB; Part 2.6 PERSON-BOXES; Part 3 webs combine; Part 4 nightly research (feeds MEMORY, not the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live: catalog MAY ask); Part 6.5 THE WONDER/SIMULATION; Part 7 THE LOG; Part 7.5 THE NOTE/THE WHY.

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots + READING RECORD — ✅ COMPLETE (S14).** → **(2b) the detector — ✅ INVESTIGATED, recipe locked (S13); fallback, not deployed.** → **(2c) THE ENGINE — IN PROGRESS:** A ✅ BUILT (S14) → B ✅ BUILT (S16) → **C (story-layer) NEXT.** C needs story-bearing gold cases before it can be tested. **Build the LIVE path before the nightly deepening.**

**★ THE ENGINE LAYERS:**
- **A (BUILT, S14):** root → mouth ("say what the {role} is doing, don't describe/answer/invent") → 12-field reading → quarantine. Bare; no context, no story. ~5–6/8 on gold v1.
- **B (BUILT, S16):** + preceding turns context — `_get_preceding_turns(n=3)` pulls N roots immediately before the target in the same thread. BACKGROUND/END BACKGROUND prompt framing. Full content, no truncation. 6.5/7 on gold v2-B. Dolphin 8B ceiling. **Future upgrade: full-thread reading with 13B + larger context window after RTX upgrade.**
- **C (NEXT):** + story-layer reading — fill `story_layer` (whose/firmness/theme). Needs story-bearing gold cases first.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. Findings land in MEMORY as readings, never the mouth.

**★ COST AT FULL NIGHTLY SCALE (confirmed S16):** Brave ~$62/month (13,500 queries/night minus $5 free credit) + OpenRouter synthesis ~$60-240/month = **~$120-300/month total**. During building/testing: **$0** (inside $5 free Brave credit). **⚠ SAFETY BUILD REQUIREMENT:** Brave has NO spending cap — a loop can bill without stopping. When this pipeline is wired (item 8 in build order), a query counter / daily cap MUST be built into the code. Not optional.

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]
Access/auth; mobile three modes; interactive canvas; behavioral-baseline wellbeing; HUD redesign; person-boxes gather; image front door (§9A); phone-data importer; memory browser; voice in/out; ChromaDB cleanup; folder cleanup.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Metadata → plain-description → context-meaning → Ness confirms. Precondition for WhatsApp media (§12).

## 10. ORIGINALITY (honest calibration)
The combination ships nowhere: inverted default + per-person never-closing STORY + DUMB/SMART split + person-boxes-as-gather + pure tape + wonder-kept-and-shown + memory-grows-not-the-mouth + two-destinations/two-files. Never claim inventing local AI, approval gates, or a trained model.

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
17. **Open design threads (low):** spine re-draw; old gate lags; `.cursorrules` reconciliation (7-field root + reading-record contract + stale docstring); clash/gap UI surfacing; write the §0A DUMB/SMART section into final place; ~24 unreviewed Cursor batch files; person-box multi-box tagging.
18. **MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned. Must be designed before a SECOND batch is written.**
19. **★ CONFIDENCE — RESOLVED (S14).** TWO-SLOT `confidence` object. Value-FORM deliberately loose, pinned later as new schema_version.
20. **★ "UNDERSTANDING" — gold-standard sets BUILT & SEALED.** v1 (8 cases, S14) + v2-B (7 cases, S16) both on disk and sealed. Engine A ~5–6/8 on v1. Engine B 6.5/7 on v2-B. B3 miss = dolphin 8B ceiling, not engine bug. RTX upgrade + 13B expected to reach 7/7 on v2-B.
>    - **ENGINE B GOLD CASES (v2-B, S16):** B1 `7ac0381c` "episode 2" ✅; B2 `4e125b71` "yes sure, second." ✅; B3 `0df151d3` "yes, second option." ⚠️ (model-size); B4 `9359edff` emotional reaction ✅; B5 `580d74d4` "Brief slow." ✅; B6 `09514821` "Yes! This is it." ✅; B7 `4b4e5551` "כן" ✅.
>    - **ENGINE B BUILD LESSONS (S16):** semantic context search fails for conversational turns — position-based is the correct lever; truncating context content kills quality — pass full content; BACKGROUND/END BACKGROUND framing prevents the mouth from answering instead of reading; 6.5/7 is dolphin 8B's honest ceiling on this task.
21. **RE-READ LIFECYCLE + THE VIEW LAYER — NAMED, not designed.** Build after the engine produces real readings to view.
22. **PERSON-BOX CONTAMINATION — needs per-element provenance.**
23. **OFF-BOARD AFFIRMATION FEEDBACK SEAM** — record Ness's accept/reject as a dated, weightless STORY-LAYER EVENT.
24. **PRIVACY / THREAT MODEL + REDACTION PATH — first-class before sensitive ingest.**
25. **GO-LIVE HARDENING BLOCK — DEFERRED, does NOT gate the engine.**
26. **MODEL-REPLACEMENT DEFAULT (near-settled).** A new mouth passes BOTH sealed gold sets before replacing; old readings keep old `produced_by`; no auto mass re-read. **S16 reinforced: hardware upgrade decided; when 13B arrives, run v1 + v2-B before adopting.**
27. **QUARANTINE PHASE + BOOTSTRAP RETRIEVAL RULE — DESIGNED; quarantine STORE BUILT (S14).** Quarantine holds A + B gold-run output. Promotion needs gold + held-out + manual inspection.

---

## 11-SETTLED. (condensed)
- **S4–S11:** unit = span-claim; carry `role`; borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction; memory-grows-not-the-mouth; two-file 2a.
- **S12:** store restored; `role` added (7-field root); clean ingest; 5,521 clean roots; Chroma=old 116k index; two-destinations shape.
- **S13:** [BUILT]-sweep done; 2a plumbing built; roots sealed; detector recipe locked (94.89%); eleven doc-refinements + quarantine/bootstrap captured.
- **★ S14:** the three forks CLOSED — confidence = two-slot object; gold scoring = six rules (semantic match, Ness judges); failure-behavior = honest insufficient-context, revisable. Reading validator + writer BUILT & VERIFIED (17/17 tests; roots regression clean). Gold set v1 (8 cases) SEALED. Minimal engine A BUILT & run against gold (~5–6/8 after prompt+role fixes). Model test: dolphin beats qwen-abliterate-3b; Hebrew gated on bigger model/VRAM. Validator structure = extract-not-fuse (`_check_common`). Quarantine store built. Confidence value-form left loose.
- **S15-chat:** NO N.H change. Scan-only confirmation that the three files are in sync + one out-of-system teaching artifact (`NH_one_pass_demo.html`). Master stayed MASTER-15; status table untouched.
- **★ S16:** Engine B BUILT & RUN — position-based context (preceding turns, same thread, full content, n=3), BACKGROUND/END BACKGROUND prompt, 6.5/7 on gold v2-B, dolphin 8B ceiling confirmed. Gold v2-B (7 context-requiring cases) SEALED. Chroma `nh_roots_v1` BUILT (5,521 roots, 187.59s). Hardware upgrade decided: RTX 5060 Ti 16GB, ~₪2,590, buy 5.7.2026, target model `dolphin-llama3.1:13b`. Cost notes confirmed: $0 now, ~$120-300/month at full nightly scale. Brave spending-cap safety note added to §8 and §11 item 8.

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

**★ THE MOUTH IS uncensored BY DESIGN, AND CAN'T BE FAKED.** Censorship lives in a model's weights, not as a rule on top. The right move is choosing a model TRAINED uncensored. `dolphin-llama3` is exactly that — why it was chosen.

**★ S14 — THE HEBREW FINDING.** dolphin-llama3 beats qwen2.5-abliterate:3b. Hebrew quality is MODEL-SIZE-gated, not prompt-fixable. Free interim patch: translate Hebrew→English before the mouth reads (logged, not built). Hebrew on dolphin today = "weak-but-workable."

**★ S16 — ENGINE B CEILING FINDING.** dolphin 8B can't reliably separate "what the person is doing" from "content of what they chose" when both appear in context. This is a model-size gap — not fixable by prompt. Confirmed at 6.5/7 on gold v2-B. **The fix: `dolphin-llama3.1:13b` on RTX 5060 Ti 16GB. Expected 7/7 on v2-B. Full-thread reading also unlocked with 13B + larger context window.**

**ON-DISK STATE:** `dolphin-llama3` (8B, uncensored — THE CURRENT MOUTH) · `llama3` (8B) · `qwen2.5-abliterate:3b` (test, not adopted) · `all-MiniLM-L6-v2` (search). Runtime Ollama, GGUF.

**UPGRADE TARGET (S16 DECIDED):** `dolphin-llama3.1:13b` — uncensored by training, 13B, fits in 16GB VRAM (~20-25 tok/s on RTX 5060 Ti). Buy hardware 5.7.2026. Pull model, run against both gold sets, verify before adopting.

---

**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board** · **the engine reads by PATTERN and CAN be wrong — that is designed-around, not a flaw** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary** · **the affirmation surface is a per-person STORY — never closed; absence read only under the §0A guard; N.H is NOT a teller** · **TWO DESTINATIONS: every eligible input → raw root (sealed) + a reading beside it; this is why two files** · **`story_layer` is a LIST so clash is kept; `mode` is an OPEN word; `confidence` is a TWO-SLOT object never one blended number; unknowns OMITTED** · **CARRY THE SPEAKER, DON'T GUESS IT — `role` on the root, from source; detector a fallback** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE preserves eligible events append-only — subject to capture-exclusions + audited redaction** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; uncensored by choice (can't be faked); local-first; night-search feeds the MEMORY not the mouth; never train a base model; Hebrew quality + B3 failure are model-size-gated; RTX 5060 Ti 16GB + dolphin-llama3.1:13b is the upgrade path, decided, buy 5.7.2026** · **THE GOLD IS A SEALED OUTSIDE EXAM — two sets now: v1 (8 cases, clean-bare) + v2-B (7 cases, context-requiring); both sealed; engine output may fail but never alter; only Ness judges** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id** · **ONE FILTER, BOTH DIRECTIONS** · memory only adds (history grows; the computed view governs live use) · the membrane · a unit is a span-claim · input-agnostic, many front doors · archive don't ingest · הכל יחסי · don't overclaim · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen, uncensored mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — where the reading record is now real built plumbing (a twelve-field validator and writer, gating shape not certainty, with confidence held as two honest slots rather than one blended number), and two engines now read: engine A reads a root bare and lays a reading beside it, engine B reads it in the context of the three turns that came before in the same conversation thread, both judged against sealed gold answer keys that only Ness can grade because the whole spec is "does it read the way Ness's mind reads" — and when the engine is wrong, as a pattern-reader sometimes must be, nothing breaks, because a wrong reading is a replaceable guess marked with its own uncertainty, never a fact, and the next upgrade (an RTX 5060 Ti 16GB arriving 5.7.2026, running dolphin-llama3.1:13b at 13 billion parameters instead of 8) is expected to close the remaining gap from 6.5/7 to 7/7 and unlock full-thread reading — so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone, because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
