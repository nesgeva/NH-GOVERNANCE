# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, AND the code rules — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–12. **Session 13 (June 23 2026, late-night, continuous from S12) is a BUILD-and-investigate session → this is MASTER-14.** S13 (1) ran the owed [BUILT]-CLAIMS SWEEP — all six high-risk S12 claims (5,521 count, 7-field schema, restored module, append-only, Chroma 116k, 1.78 GB) VERIFIED on disk; only one minor phantom (`nh_peek.py` not on disk, harmless — superseded by `nh_log.py`); (2) **BUILT the 2a PLUMBING — the two-file split + the SEALED roots** (dry-run-and-approved, verified on disk). ⚠ **NOT the full reading record:** what is built is the physical routing (`append_reading`→a sibling file) and the seal; the on-disk `append_reading` still takes ROOT-SHAPED fields (`subject, content, re_reads, role`) and `_validate_record` still validates the 7-field ROOT schema. The **8-field reading record (`id·reads·meaning·confidence·role·story_layer·mode·timestamp`) is DESIGN-LOCKED but NOT coded** — no reading validator, no reading writer, zero real readings on disk. (3) **closed the open DESIGN fork inside the reading record** — `story_layer` = a LIST of tellings (holds clash), `mode` = an OPEN word + confidence (no fixed menu), unknown parts OMITTED (never placeholder-filled); (4) **went deep on 2b — the speaker detector** — a full, honest, ten-method investigation that established the shape ceiling (~91.6%), then broke past it with meaning (embeddings), landing at a cross-validated **honest 94.89%** (embed+shape features, LogisticRegression C=0.1, 5-fold); recipe locked, NOT deployed (read-only probes). The forced build order (§7C/§11) is UNCHANGED. **Net: 2a is HALF-built (plumbing yes, reading-record no); 2b is investigated-and-recipe-locked; the reading-record code + the engine (2c) are the next milestone — fresh-head.***

---

> ## ★ THE ONE AUTHORITATIVE STATUS TABLE (single source of truth — every other section must AGREE with this; if prose anywhere conflicts, THIS wins)
> *Added S13 after the external critique proved that repeating status in prose let an overstatement ("2a built") propagate to ten places. Status lives HERE, once. Prose may describe, never re-assert a different status.*
>
> | Component | Status | Proof / Note |
> |---|---|---|
> | Clean accretive store — 5,521 roots, 7-field, role-carried | **BUILT & VERIFIED** | `find /c` = 5521; schema checked on disk |
> | Roots file SEALED (`.nh_roots.sealed`) | **BUILT & VERIFIED** | append refused, roots stayed 5521 |
> | Two-file ROUTING (`append_reading`→sibling) | **BUILT & VERIFIED** | test write landed in sibling, roots untouched |
> | 8-field READING RECORD — validator | **DESIGNED, NOT BUILT** | `_validate_record` still enforces 7-field ROOT |
> | 8-field READING RECORD — writer | **DESIGNED, NOT BUILT** | `append_reading` still root-shaped (`subject,content,re_reads,role`) |
> | Real readings on disk | **ZERO** | sibling file empty/absent |
> | `story_layer`=list · `mode`=open word · unknowns omitted | **DESIGN-LOCKED** | settled S13; not yet coded |
> | Speaker detector recipe (embed+shape→LogReg C=0.1→94.89%) | **INVESTIGATED & PROVEN, NOT DEPLOYED** | read-only probes; fallback only |
> | Ingest pipeline (`nh_ingest_chatgpt.py`) | **BUILT & VERIFIED** | ran on all 3 JSON sources |
> | Chroma `nh_reality_core` (116,391) | **BUILT — but OLD/unaligned index** | rebuild from clean roots later |
> | The engine (2c) — chain of webs | **DESIGNED, NOT BUILT** | the next milestone |
> | Multi-box (sealed-batch) architecture | **NOT DESIGNED** | §11 item 18 |
> | Confidence semantics (4 separate things) | **NOT DECIDED** | §11 item 19 |
> | Gold-standard test set | **NOT BUILT** | §11 item 20 — highest-value next move |
> | Pure-tape redaction/destruction path | **NOT DESIGNED** | §0A correction + §11 item 24 |
>
> **2a overall = PARTIALLY built (plumbing yes, reading record no). NOT complete.**

---
>
> **0. ★ THE 2a PLUMBING IS BUILT — TWO-FILE ROUTING + SEALED ROOTS ARE LIVE. THE READING RECORD ITSELF IS NOT YET CODED.** Be precise about what's on disk vs designed:
>    - **BUILT & verified:** `append_reading` now writes a SIBLING file `.nh_readings_store.jsonl` (NOT the roots file). Mechanism: `_append_record` gained an optional `path=STORE_PATH` param; `append_root` calls it with the default (roots file), `append_reading` passes `READINGS_PATH`. Proven on disk: a test reading landed in the sibling, roots stayed at exactly 5,521.
>    - **BUILT & verified:** the roots file is SEALED. A marker file `.nh_roots.sealed` exists; `append_root` checks for it FIRST and raises `RuntimeError` (writes nothing) if present. Proven: an attempted root append was refused, roots stayed 5,521. Physical wall (seal) + logical wall (`re_reads` validation) both stand. Backup `.nh_accretive_store.jsonl.bak_preseal` made before sealing.
>    - **⚠ NOT built:** the on-disk `append_reading(subject, content, re_reads, role, ...)` still takes ROOT-SHAPED fields, and `_validate_record` still enforces the 7-field ROOT schema. The test reading that proved the routing was itself root-shaped — so what's proven is the ROUTING, not the reading schema. The **8-field reading record (`id·reads·meaning·confidence·role·story_layer·mode·timestamp`) has NO validator, NO writer, and ZERO real records on disk.** Coding it (a reading-shaped `append_reading` + a reading validator) is the FIRST 2c-adjacent job. *(This correction caught an overstatement in the first MASTER-14 draft — the verify-on-disk discipline applied to the doc itself. The test proved a file got written, not that a reading-shaped record exists.)*
>    - **The seal is per-BATCH, not "no more data ever."** Sealing protects the 5,521 verified roots from any future mistake reaching them; NEW raw goes into NEW roots files (new sealed boxes), never by reopening this one. ⚠ **OPEN: the multi-box architecture is undesigned** — no manifest, no root-id→file resolution, no cross-batch dedup, no `read_all`-over-many-boxes. The seal protects ONE file; managing many sealed boxes is an unsolved design problem (§11 item 18). *(Ness's own framing of why-seal: "the file itself is what's in it, not changed by mistake.")*
>
> **1. ★ THE OPEN DESIGN FORK INSIDE THE READING RECORD IS CLOSED — `story_layer` and `mode` insides settled (DESIGN, not yet code).** The 8-field reading record is `id · reads · meaning · confidence · role · story_layer · mode · timestamp`. The two complex fields are now design-locked:
>    - **`story_layer` = a LIST of tellings** (not one telling). A list so two people can read the same root in opposing ways and BOTH are kept side-by-side — the clash stays, nothing wins. Each telling has optional parts: `whose · stance · firmness · telling · theme · when`. Empty list = no story-reading yet (honest). **The reading's top-level `role` (who spoke, from source) ≠ a telling's `whose` (in whose story it's about).**
>    - **`mode` = an OPEN word + confidence** (register: chat/composed/story/question/…), NOT a fixed menu. Reason: a fixed menu would re-introduce a manual gate — Ness would have to bless each new "kind" before the filter could use it, the exact deciding-ahead-of-time the system refuses (R5, הכל יחסי). Open word = the filter names it, no gate. *(Ness caught this contradiction himself.)*
>    - **Unknown parts are OMITTED, never placeholder-filled** (no `"firmness": "unknown"`). A blank is honest; the word "unknown" is a fake answer. Absence is read later, at read-time. (Absence-is-read made physical.)
>
> **2. ★ THE [BUILT]-CLAIMS SWEEP (§11 item 13) — DONE, FLOOR CONFIRMED.** All six high-risk S12 claims verified on disk: roots = 5521 ✓; 7-field schema with real `role`+`source_title` ✓; module loads with all 4 public functions ✓; append-only (only `"a"`/`"r"` opens, no `"w"`) ✓; Chroma `nh_reality_core`=116,391 ✓; `chroma.sqlite3`≈1.78 GB ✓. Protected core files (9) all present; source files (5) all present; both LLMs + the MiniLM model present; `.cursorrules`=15,303 bytes. **One minor phantom: `nh_peek.py` is NOT on disk** (the master listed it — it's the retired old peek tool, superseded by `nh_log.py`). Unlike S12 (wrong 5×), the doc was wrong ONCE, on something inert. 2a was NOT built on a phantom.
>
> **3. ★ 2b — THE SPEAKER DETECTOR INVESTIGATED IN FULL; HONEST CEILING ESTABLISHED AND BROKEN. RECIPE LOCKED AT ~94.89%.** A complete ten-method investigation (all read-only probes, none deployed). The ladder, every rung proven on disk with honest train/test grading:
>    - length-only threshold → 90.89% · +structure (code/lists/bold) → 90.98% (redundant) · **conversation-RELATIVE length** (word_count − its conversation's median; T=−3) → 91.65%, and it FIXED the lopsidedness (user 88→91, assistant stays ~92).
>    - honest train/test of relative-length → **91.60%** (proved 91.65 was NOT overfit — train/test match).
>    - decision tree (depth 6) → 91.38% · random forest → 90.80% — **shape MAXED**; `rel_length` carries ~95% of the tree's importance; style flags + shorthand are near-redundant once length is in.
>    - **content tells** measured: 23 of Ness's 29 chat-shortcuts are CLEAN (assistant used them literally 0×) — `pls·btw·thx·u·bruh·tbh·rn·ur·lol`… + his Hebrew (`בבקשה·אוקיי·בכללי·בקשר`). Perfect-but-RARE (~4% of his msgs) → can't move the number alone. Traps caught: `ok`, `yeah` (assistant uses them too).
>    - **style signals** measured (these are COMMON, not rare): `no_uppercase` (Ness 55% / AI 20%), `no_end_punct` (40% / 11%), `starts_lowercase` (29% / 7%). The real lever.
>    - logistic regression on hand-features → 78.9% (FAILED — wrong tool: length is a hard STEP, not a smooth curve; also needed scaling).
>    - **EMBEDDINGS (meaning, `all-MiniLM-L6-v2`, already on disk) → 93.48%** — broke past the shape ceiling. Meaning reads the AI's explaining/helping stance vs Ness's asking/reacting, invisible to shape. ~2 min one-time, no LLM grind.
>    - **EMBED + 5 shape features (389-dim) + LogisticRegression → 94.71%** — meaning and shape catch DIFFERENT mistakes, so combining beat both (neither redundant).
>    - tuned: **LogisticRegression C=0.1** (more regularization) won at 95.29% on one split; boosting did worse.
>    - **★ HONEST 5-FOLD CROSS-VALIDATION:** the 95.29 was the lucky single fold. Real number = **94.89% (±0.36%)** across 5 folds — tight, stable, trustworthy. C=0.1 genuinely beats C=1.0 (94.89 vs 94.48), so the tuning is real. **THIS IS THE LOCKED DETECTOR RECIPE: embed+shape (389-dim) → StandardScaler → LogisticRegression(C=0.1) → ~94.9% honest.**
>    - **The detector is a FALLBACK, not deployed.** It only matters when a future source LACKS `role` (a damaged import). The 5,521 roots carry true role from source — the detector never touches them. The recipe is known/proven; building the live detector is a LATER job. The full LLM (`dolphin-llama3`) is PARKED as an overnight job for the last ~1 point — not worth the 4–5 hr grind now.
>
> **4. NET FOR THE BUILD:** **Forced order: 2a ✓ (built+sealed) → 2b ✓ (investigated, recipe locked) → 2c THE ENGINE is now the next milestone — fresh-head.** The readings channel is open and the roots are sealed beneath it, so the engine has a clean, safe place to write into.

> **★ DECISIONS LOCKED IN SESSION 13 (protect from re-litigation):**
> - **`story_layer` = a LIST of tellings** (holds clash, nothing wins); parts `whose·stance·firmness·telling·theme·when`, all optional, empty list allowed. SETTLED.
> - **`mode` = an OPEN word + confidence**, never a fixed menu (a menu = a re-introduced manual gate). SETTLED.
> - **Unknown reading-parts are OMITTED, never placeholder-filled** ("unknown" is a fake answer; a blank is honest). SETTLED.
> - **The two-file ROUTING is BUILT** — `append_reading`→`READINGS_PATH` via `_append_record(path=…)`; `append_root` still→`STORE_PATH`. Don't re-route. ⚠ But `append_reading` is still ROOT-SHAPED; the reading-record validator/writer is NOT built.
> - **The roots are SEALED via `.nh_roots.sealed`** — `append_root` refuses if the marker exists. The seal is per-batch (new raw → new files), and protects the verified 5,521 from future mistakes. Don't propose un-sealing to add to THIS batch.
> - **The detector recipe = embed+shape(389) → StandardScaler → LogisticRegression(C=0.1) → ~94.89% honest (5-fold).** Don't re-derive from scratch; shape alone tops out ~91.6% (proven), meaning is the lever. The detector is a FALLBACK, not deployed, only used when role is absent.
> - **The LLM detector is PARKED** (overnight job, last ~1 point) — not a fork to re-open, a deferred option.

> **PRIOR DELTA (SESSION 12 → MASTER-13) — condensed for continuity:**
> - **The store became real & clean: 5,521 verified roots** (7-field `id·subject·timestamp·content·re_reads·source_title·role`, role carried from source, real timestamps, true order; the old 188 stub retired, backed up). **Five disk-truths corrected the master** (count wrong twice; `nh_accretive_store.py` was MISSING — recovered from `.pyc`; `append_reading` was not a stub; 188 had `source_title` inlined; Chroma=116,391 not ~11k). **`role` added to the root (6→7 fields).** **Clean ChatGPT-export ingest pipeline built & proven** (`nh_ingest_chatgpt.py`, tree-walk true order). **§11.15 closed by action** (flat=sealed roots-of-record, Chroma=rebuildable index). **`gpt_purified` (0 unique, scrambled) + `cleaned_history` (damaged) correctly NOT ingested.** **The TWO-DESTINATIONS shape** (every input → raw root + a reading beside it; raw stays raw; this is why two files) — Ness re-derived it himself.

> **PRIOR DELTAS (sessions 4–11) — condensed for continuity:**
> - **S11 (→ MASTER-12):** MODEL LAYER resolved (borrowed frozen mouth; two models wording+search; local-first; `dolphin-llama3` uncensored on disk; `all-MiniLM-L6-v2` search model); PERSON-BOXES designed (gather over readings by `whose`, bounded by Ness's knowing); PURE TAPE (verbatim append-only ground floor); WONDER/SIMULATION (kept-and-shown never decided); CATALOG (front-door RAW→CATALOG); SOUL CORRECTION (engine never decides, Ness affirms off-board, affirming closes nothing); "memory is understood knowledge that grows, night-search feeds the memory not the mouth." All DESIGN. Disk numbers it gave (188, ~11k Chroma) were S12-superseded.
> - **S10:** 2a shaped (two files; 8-field reading record; six-part absence-aware story_layer); DUMB vs SMART (psychologics) frame (§0A); "N.H is Ness's HELPER, not his DECIDER"; reality-layer re-souled to per-person STORY-layer; N.H not a teller (weightless NOTE, cannot harden); mode = peer web; firmness READ; clash is a feature.
> - **S9:** the PREMISE §0 (never close the book into a fact; danger = reasoning hardening into authority); reality → per-person filter READING; the "why" = non-decisive NOTE; read-only tools built (`nh_log.py`, `nh_probe.py`, `nh_probe_truth.py`); speaker settled on ground truth (carry `role`; length strong, "?" a trap); tunnel block commented.
> - **S8:** §13 LIVE LOOP (fire-and-let-go) + §14 CHAT FRONT DOOR + the GUARD + design-to-fit-Ness compass.
> - **S7:** unit/segmentation DISSOLVED — a unit is a span-claim not a cut; two places (dumb memory + fast calculator); why shown by pointers; forced build order recorded.
> - **S6:** A13 WhatsApp data-rescue (2012→2024, encrypted, archived, NOT ingested); auto-start/tunnel disabled; FREEZE INGEST.
> - **S5:** `nh_peek.py` built; JSON + gpt_purified ingested (OLD ingest — superseded by S12 clean ingest); `cleaned_history` set aside.
> - **S4:** accretive store skeleton built; first 188 records (RETIRED in S12); schema settled.

> **THE NAME:** He is **Ness** (male). He signs **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. As of S13: the clean store + the role schema + the ingest pipeline + **the 2a PLUMBING (two-file routing + sealed roots)** are **[BUILT & VERIFIED]**. ⚠ The **8-field reading record (validator + reading-shaped writer) is [DESIGNED], NOT built** — `append_reading` is still root-shaped, zero real readings. The **speaker-detector recipe is INVESTIGATED & PROVEN (~94.9%) but NOT deployed** (read-only probes). The filter/engine (2c), the reading-record code, the readings-layer *population*, the model wiring, the person-boxes, the tape, the wonder, the catalog are **[DESIGNED]**. The old REALITY/SIMULATION gate still runs harmlessly while the engine doesn't exist.

> **★ A STANDING LESSON CARRIED FROM S12, NOW DISCHARGED IN S13 — the [BUILT]-CLAIMS SWEEP IS DONE.** S12 was wrong five times about "built" things. S13 ran the owed sweep before building 2a: all six high-risk claims held on disk; one minor inert phantom (`nh_peek.py` absent — superseded by `nh_log.py`). Lesson stands for the future: trust disk, never the doc's remembered state — including this file's. Before the NEXT build that touches existing "built" code, a quick existence-and-shape check is still owed on anything not re-verified since.

---

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

**The line:** The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact. The AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time, and even wonder/simulate forward at night — and do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**The crystallization:** **N.H is Ness's HELPER, not Ness's DECIDER.** A helper reads, connects, lays out what it sees, even leans — then hands it to the person, who decides. A decider closes the book.

**★ THE SOUL CORRECTION (S11) — three truths held at once, never collapsed:**
1. **Nothing is real — it's a story** (§3G). There is no fact-box. "Real" is not a place a thing goes.
2. **Ness still decides / affirms.** He is the decider, the membrane. The system does NOT decide what is real — *and neither does it pretend nothing is ever decided.* Ness decides.
3. **★ His deciding is NOT a node in the engine.** It happens out in real life, engine absent. **There is no step after "show."** The engine wonders and shows; the deciding is *off the board.*

**Why a fact is the forbidden thing:** a fact is *the book shut* — true-for-everyone, no longer subjective to Ness. N.H is *his* (הכל יחסי). A fact is the one thing he does not own.

**The crucial distinction:** "never decide facts" does NOT mean "never hold anything firmly." Something can be held with full weight and still never close the book. The enemy was open-vs-closed, not weak-vs-strong.

**★ S13 SHARPENING (from external critique — the wording was too absolute; narrow its JURISDICTION, don't remove the principle):** "never decide facts" must NOT be read as "there are no facts." The clean distinction: **the DUMB machinery MAY establish directly-verifiable machine-state and provenance facts** (this file exists, this hash matches, this record has 8 fields, this role came directly from source, this root-id points here, this write succeeded). **The SMART machinery MAY interpret, connect, and lean — but may NEVER silently promote an interpretation into an established fact.** The authority for any such promotion is Ness, off-board, never the engine. So: *machine-state & provenance truth is decided freely; interpretive meaning is never closed into truth-for-everyone.* Collapsing those two into one prohibition (the old wording) would treat a file hash or a source role as "only a story" — which absurdly WEAKENS the evidence discipline the system exists to protect.

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame]

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The pure tape, the append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), the role-carried-from-source, the catalog's who/when/where marking, the mode/form-naming, the person-box GATHER, the live loop's fire-and-let-go. One law: **never interpret, never close — only add / point / carry / sort / gather.** Safe BECAUSE it cannot interpret.

> **★ S13 CORRECTION — THE PURE TAPE NEEDS A REDACTION/DESTRUCTION PATH (safety, not philosophy).** "Captures always, append-only, untouchable" is epistemically clean but a real hazard: the tape could capture passwords, access tokens, other people's private info, accidental pastes, medical details, things recorded during distress, or material someone later has a legitimate right to remove. **"Append-only" must NOT mean "permanent recoverable storage of every secret forever."** The corrected rule allows: (i) **capture exclusions** for credentials and known secrets (don't record them at all); (ii) encrypted storage; (iii) explicit **retention boundaries**; (iv) **cryptographic erasure** of selected content; (v) an append-only **TOMBSTONE** that retains *that* a deletion occurred and when, WITHOUT retaining the deleted plaintext; (vi) special treatment for third-party and childhood data. This does not violate append-only HISTORY — the record can say content was removed without continuing to preserve the harmful content itself. *(Applies to the tape AND the sealed roots: sealing protects from accidental MUTATION; it must still allow DELIBERATE, audited destruction of genuinely sensitive content — seal ≠ un-deletable.)* Owed alongside §11 item 24 (privacy/threat model).

> **★ S13 CORRECTION — "ABSENCE IS READ" NEEDS A GUARD (or it becomes pseudo-psychology).** Absence is meaningful ONLY when (i) the system EXPECTED the information, (ii) the collection process was CAPABLE of observing it, (iii) the absence is contextually relevant, and (iv) the interpretation is held explicitly WEAK. Unguarded, "absence is read" turns missing-data artifacts (a parser failure, a field never evaluated, an old schema) into manufactured significance — a sophisticated hallucination. So omission needs to distinguish, at least in processing metadata, between `not_observed` / `not_evaluated` / `not_applicable` / `withheld` / `collection_failed`. A blank in a reading is still honest (don't write `"unknown"`), and these labels live BESIDE the reading as provenance about WHY a field is absent — they do not fill the story fields themselves. The engine must not read every blank as psychological evidence — only the ones that pass the four-part guard.
- **SMART (psychologics) MACHINERY — reads the *person*.** The meaning webs (Theory of Mind, the STORY-layer with its six parts, gap-reading, firmness-as-read), clash-surfacing, the wonder/simulation, and the NOTE. One law: **everything here is weightless, dated, confidence-tagged, rejectable — NEVER a fact.** Safe BECAUSE it cannot close.
- **THE BORROWED MOUTH (§16) sits at the seam, used by SMART.** The wording model turns understood meaning into sentences — a swappable tool. The embedding/search model is a DUMB tool (sorts by meaning-distance; does not interpret).

**The membrane (§7A R7) is the boundary between them** — creation (SMART) never closes into memory (DUMB).

**OPEN PINS (fresh-head):** (i) the name — "smart" vs "psychologics machinery"; (ii) whether the note + clash file under SMART or are called out inside it.

---

## 1. WHAT N.H IS

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The one-line soul:** **N.H is Ness's HELPER, not Ness's DECIDER.** The loop, in Ness's words: *real life → into N.H for help → it helps him see and understand his own thinking and do what he needs in the way that fits how he thinks → he returns to real life with a solution that is his own.*

**★ WHAT JARVIS ACTUALLY IS:** Jarvis is NOT the model. The model is a borrowed, frozen mouth (§16). **Jarvis is the memory + the soul + the gathering + the mouth, wired together.** Everything that makes him *him and grows him* lives outside the model.

**★ MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS.** The memory is not a pile of raw text — it is comprehension that accretes. New input is *read* by the webs and lands as a reading (meaning + confidence + story-layer). Jarvis understands more tomorrow, and the growth lands in the memory, never in the frozen mouth.

**★ THE TWO-DESTINATIONS SHAPE (S12, Ness re-derived it):** every input goes to TWO places at once — (1) the **RAW ROOT**, saved untouched and sealed; (2) **THROUGH THE FILTER**, which READS it and lays a **READING** beside the root, pointing back by id, never altering the raw. The filter never "filters" the root; raw stays raw forever, understanding accretes beside it. This is exactly why there are TWO FILES. *(S12 built place 1 — the raw roots. The filter, place 2, reads them later as its own pass.)*

**The two functions (NOT two truth-boxes):**
- **SIMULATION — the create-space / workshop, with a live function (§7B Part 6.5):** where things get made and wondered forward.
- **"REALITY" as a box of decided facts — DISSOLVED (§3G).** "How real" is not a place; it is "how does this sit in *whose* story" — a per-person telling the filter reads, layered, revisable, never closed.

**The two purposes, always running together (THE CORE — Ness's framing):**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside — the pattern he can't see because he's inside it. *(The 5,521 clean roots ingested in S12 are the inward eye's raw material.)*
- **OUTWARD — the engine:** take new external data and translate it through the lens of how *his* mind connects things — not generic explanation, not retrieval.
- **ONE FILTER, BOTH DIRECTIONS.** Same method (read meaning through Ness's lens, never close the book); only the direction it faces changes. The two feed each other: outward reading lands in memory as new roots/readings, which enrich the next inward read. *"A mind that runs alongside another mind — one looking inward, one looking outward — both at full speed."*

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED]

N.H is input-agnostic. Text, images, video, audio — all flow through the SAME engine. New input types get a new **front door** (a small model turning that input into pieces the engine reads), not a new engine. The front door has two stages (§14): RAW capture → CATALOG (who/when/where). The live chat itself is a front door. *(The S12 ChatGPT-export parser is a worked text front door.)*

**The deepest "why" — הכל יחסי:** nothing about *meaning* is final — a thing means what it means only relative to ever-growing context, and relative to whom. This is why memory only adds, classification is never locked, "unknown" is honest, and the affirmation surface is a per-person STORY, not a shared fact-box.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time.** He asks "why yes / why no" and wants real tradeoffs. **He often asks for things "plainly" — give the plain version directly.**
- **Verify on disk, never trust status reports.** *(S12 proof, the strongest yet: FIVE doc claims fell to disk checks in one session — the count, a missing module, a not-a-stub, an inlined field, a 116k-vs-11k Chroma. Trust disk, never the doc — including this master.)*
- **Honest correction over flattery** — explicitly, repeatedly asked for.
- **Don't inform, just flag and keep going.** A one-line flag, then continue.
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, elongated punctuation ("ssstttiiilll nottt 11") are NOT distress; they're thinking out loud / staying in flow.
- **He catches things.** When he pushes back, he is usually right. *(S12: he caught Claude attributing decisions to him that Claude had made — "you said not me" — a real correction. Don't put words in his mouth; offer, let him confirm.)*
- **He is not afraid of work.** A wall is almost never "this is hard" — it is "this move would destroy/forfeit something." Diagnose blockers as *"what irreversible/lossy thing is this asking?"*
- **He re-derives his own design from the inside.** *(S12: he reconstructed the two-files / two-destinations shape himself from the data side. The design is genuinely his — offer shapes, let him rebuild and steer.)*
- **Backup before any destructive step, always.** *(S12: he insisted "of course backup first" before clearing the 188 — correct instinct, kept.)*
- **Primary risk pattern: scope-expansion before consolidation.** Finish and verify what's in front before the next thing.
- **Claude's role:** architecture, audit, security, strategy — the brain that checks the work ("JARVIS"). Cursor writes code; Ness runs every command in cmd and verifies on disk. *(S12 exception: for the bytecode recovery + the small ingest/store modules, Claude wrote the exact code directly so the recovered constants wouldn't drift; Ness still ran and verified everything on disk.)*
- **Session workflow:** one topic per chat; start fresh when a topic closes. End of session: regenerate the master + a short delta → Ness swaps the file in. **Ness prefers to start a fresh chat from a corrected master rather than continue a long session on fumes** (stated S12).

---

## 3. THE EVOLUTION — OLD vs NEW (key points)

- **A. Manual gate → MEMBRANE.** Memory only ADDS, never edits. Sovereignty = a position (the membrane), not an action. [Accretive store BUILT; clean roots S12.]
- **B. Many "is this real?" gates → ONE UNIVERSAL FILTER.** Sorts/reads; never closes the book; reads story-layers per person. [DESIGNED §7A.]
- **C. AI creativity → the membrane.** Bridging/wondering only in chat (Ness present), barred from closing into fact in memory.
- **D. Security holes found on disk → fixed.** [ALL BUILT.] *(⚠ S11 note still stands: `cloudflared.exe` (54 MB) inert but on disk — convenience-sweep item.)*
- **G. Affirmation surface → per-person STORY-layers** (REPLACES the old REALITY-box). Told, firm-and-open, per-person, never collapsed; six optional parts with absence-as-a-read. N.H not a teller. [DESIGNED.]
- **H. The person → PERSON-BOXES** — each a GATHER over readings by `whose`, bounded by Ness's knowing, never synthesised. [DESIGNED §7B Part 2.6.]
- **I. "Do I train a model?" → BORROW A FROZEN MOUTH** (§16). [DESIGNED + partly on disk.]
- **★ J. (S12) The store — from a 188-stub with a MISSING module + inlined source_title → 5,521 CLEAN roots with a restored module + role schema.** [BUILT & VERIFIED.] The biggest doc/disk gap-set to date; the proof-case for verify-on-disk.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2). Python **3.13.14**.
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM) — verified 24/7-safe.
- **Launched via** `run_app.pyw` → pywebview at `http://localhost:8080/`. PC has ONE mode — native window, local only, no internet.
- **★ MODEL HARDWARE REALITY:** a 6GB 2060 runs 3B-class models normally (~35–50 tok/s); 7B/8B run but SLOW (~7–9 tok/s). Both current local models are 8B (`dolphin-llama3`, `llama3`). A used RTX 3060 12GB (~$200–250) is the known cheap upgrade — noted, NOT now. Runtime = Ollama; models = quantized GGUF; context ~2048.
- **Windows sign-in:** Kensington VeriMark fingerprint key (distinct from N.H's own auth).

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` (`promote_to_memory()` — OLD-model gate) · `nh_context_router.py` · `nh_reality_graph.py` · `nh_simulation_graph.py` · `nh_epistemic_sandbox.py` · `nh_evidence_integrity.py` · `nh_jarvis_core.py` · `nh_crypto.py` · **`nh_vector_memory.py`** (ChromaDB).
*(This OLD REALITY/SIMULATION gate stack still runs harmlessly while ingest is frozen. Do NOT rip out before the new filter exists.)*

**Physical stores on disk (verified S13):**
- **`.nh_accretive_store.jsonl` — 5,521 CLEAN roots, NOW SEALED** (7-field schema). The roots-of-record. `append_root` refuses to write while the seal marker exists.
- **`.nh_roots.sealed` — the SEAL MARKER** (empty file, S13). Its existence makes `append_root` raise and write nothing. The physical wall.
- **`.nh_readings_store.jsonl` — the SIBLING readings file (S13).** `append_reading` writes here, NOT the roots file. *(Currently empty/absent on disk — only a test reading was written then deleted; no real readings exist yet. It is created the moment the first real reading is appended.)*
- **`.nh_accretive_store.jsonl.bak_preseal`** — backup of the 5,521 roots made just before sealing (S13).
- **`.nh_accretive_store.jsonl.bak_188_preclean`** — backup of the retired 188 stub (S12).
- **`chroma_db\` — ChromaDB, `chroma.sqlite3` ≈ 1.78 GB.** Collections: `nh_reality_core` = **116,391** (the big OLD index — chunked/old data, NOT aligned to the clean roots; rebuild later, keep until proven), `nh_test_asm` = 1,180, `nh_simulation_core` = 263. The three sub-dirs map to the three collections (the 195 MB `742b7d32` = `nh_reality_core`).
- OLD-model stores: `.nh_memory_store.jsonl` · `.nh_reality_store.jsonl` / `.nh_simulation_store.jsonl` · `.nh_simulation_graph.jsonl` / `nh_mental_network.json`.
- `peek.txt` (5,041 lines = the OLD 188 reformatted — stale), `nh_log.html`.

**Source files on disk (the ingest inputs):**
- `conversations-000.json` (100 convs → 2,172 roots), `conversations-001.json` (100 → 3,179), `conversations-002.json` (23 → 170). **All three INGESTED CLEAN S12.**
- `gpt_purified_history.txt` (202 convs, ALL already covered — NOT ingested), `cleaned_history (1).txt` (damaged — NOT ingested).

**Models on disk (verified S13):** Ollama `dolphin-llama3:latest` (UNCENSORED, 4.7 GB, 8B) · `llama3:latest` (4.7 GB, 8B). `models\all-MiniLM-L6-v2` (embedding/search model — 90 MB safetensors + tokenizer; its vectors fill the OLD Chroma; **also = the detector's embedding model, §11C**).

**Accretive store + tooling [BUILT & VERIFIED]:**
- **`nh_accretive_store.py`** — restored S12 from bytecode, extended S13. Append-only (every `open()` is `"a"`/`"r"`, no `"w"`; verified — only the docstring mentions `"w"`); schema validated before every append. **7-field ROOT schema:** `id · subject · timestamp · content · re_reads · source_title · role`. **S13 additions:** `SEALED_MARKER = ".nh_roots.sealed"` + `READINGS_PATH = ".nh_readings_store.jsonl"` constants; `append_root` raises `RuntimeError` if the seal marker exists (guard is the FIRST statement); `_append_record(record, path=STORE_PATH)` takes an optional path; `append_reading` passes `READINGS_PATH` (the two-file split). Functions: `_coerce_source_title`, `_validate_record`, `_append_record`, `_new_record`, `append_root(subject, content, role, source_title=None, timestamp=None)`, `append_reading(subject, content, re_reads, role, source_title=None, timestamp=None)`, `read_all`, `read_by_subject`.
- **`nh_ingest_chatgpt.py`** — RESTORED/BUILT S12. The clean ChatGPT-export ingest (tree-walk ordering, clean fields, junk-skip, DRY_RUN flag). Reusable for any ChatGPT-export JSON by changing `SOURCE_FILE` + `SUBJECT_TAG`.
- `verify_rt.py` — round-trip checker.
- `nh_log.py`→`nh_log.html` · `nh_probe.py` / `nh_probe_truth.py` (read-only tools). **⚠ `nh_peek.py` is NOT on disk** (master previously listed it — retired, superseded by `nh_log.py`).
- **★ S13 DETECTOR-INVESTIGATION PROBES (all read-only, none deployed):** `nh_detect_speaker.py` (length), `nh_detect_speaker_v2.py` (+structure), `nh_detect_speaker_v3.py` (relative length — 91.65%), `nh_find_tells.py` (token skew), `nh_find_shortcuts.py` (29 chat-shortcuts), `nh_find_style.py` (style features), `nh_classify_speaker.py` (logreg on hand-features — failed, 78.9%), `nh_honest_threshold.py` (honest train/test of the threshold — 91.60%), `nh_tree_vs_forest.py` (tree/forest — shape maxed), `nh_embed_speaker.py` (embeddings — 93.48%), `nh_embed_plus_speaker.py` (embed+shape — 94.71%), `nh_embed_tuned_speaker.py` (C-sweep + boosting — C=0.1 best), `nh_embed_confirm_speaker.py` (5-fold CV — **honest 94.89%**). These are scaffolding/experiments; the live detector is built LATER from the locked recipe (§11C). Candidate for tidy-up (keep `nh_embed_tuned_speaker.py`/`nh_embed_confirm_speaker.py` as the reference recipe; the rest are dead-ends).

**`.cursorrules` v3.1 (in-force):** §6A. On disk = 15,303 bytes. **⚠ §6A still describes the OLD root schema (no role) and the one-gate model — needs a reconciliation pass to reflect the 7-field root + the sealed two-file store. INCOMING, not yet done. (S13 note: `.cursorrules` §7 protected list also names files NOT in §5's sweep — `nh_research_engine.py`, `nh_auth.py`, `nh_metrics_tracker.py` — part of the same owed reconciliation.)**

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **★ THE CLEAN ACCRETIVE STORE — 5,521 roots, 7-field schema, role-carried, real timestamps, true order, zero junk, verified (S12); NOW SEALED (S13).**
- **★ 2a PLUMBING BUILT (S13): the two-file routing** (`append_reading`→`.nh_readings_store.jsonl`) **+ the sealed roots** (`.nh_roots.sealed` guard in `append_root`). ⚠ The 8-field READING RECORD itself (validator + reading-shaped writer) is DESIGNED, NOT built — `append_reading` is still root-shaped, zero real readings on disk.
- **★ The restored store module** (`nh_accretive_store.py`, extended S13) + **the clean ingest pipeline** (`nh_ingest_chatgpt.py`).
- **★ The speaker-detector recipe INVESTIGATED & PROVEN (S13): embed+shape → StandardScaler → LogisticRegression(C=0.1) → ~94.89% honest (5-fold).** NOT deployed — read-only probes only.
- The OLD REALITY/SIMULATION two-layer gate (still runs) · `promote_to_memory()` · encryption at rest · all §3D security fixes · pywebview real HUD.
- The OLD populated vector memory — ChromaDB ~1.78 GB, `all-MiniLM-L6-v2`, 116k-item `nh_reality_core` (the OLD index — to be rebuilt).
- Two local LLMs in Ollama — `dolphin-llama3` (uncensored) + `llama3`, both 8B.
- Read-only tooling; tunnel block commented; boot hygiene; `.cursorrules` (v3.1, pre-role).

**Known regression pattern:** verify on disk; the doc's remembered state has been wrong repeatedly.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE — but pre-S12, needs reconciliation)

*The in-force ruleset Cursor obeys against the CURRENT system (the OLD per-record manual gate). §§0–11 IN FORCE; §12 INCOMING. The §0 premise, §0A frame, §3G story rework, §16 model layer, person-boxes, tape, the S12 clean store + 7-field root, and the two-destinations shape are DESIGN/NEW — they extend §7A and the §12 INCOMING block; they do NOT silently rewrite the in-force body. **S12 ADDS to the INCOMING block: I13 — the root schema is now SEVEN fields incl. `role` carried-from-source; I14 — the clean ingest pipeline exists; I15 — Chroma `nh_reality_core` is the OLD index, rebuild from clean roots when wiring search, keep-until-proven.**)*

*(Full §6A v3.1 body unchanged from MASTER-12 — the one-gate rule, the absolute prohibitions, the protected-file list, the dry-run protocol §6A.8, pull-sovereignty §6A.10. Preserve verbatim from disk `.cursorrules`. NOT reproduced in full here to avoid drift; the disk file is authoritative for the in-force body. Reconciliation to the 7-field root is an INCOMING item, not yet applied to the live ruleset.)*

---

## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED]

*The running code of the accretive/membrane direction. A deliberately dumb, append-only store — the DUMB-MACHINERY heart (§0A). Wired to NOTHING by design.*

**Module:** `nh_accretive_store.py` (restored S12, extended S13). 4 public + 4 private functions; every `open()` is `"a"`/`"r"`, no `"w"`; schema validated before every append. **The roots file is SEALED (S13):** `append_root` raises if `.nh_roots.sealed` exists.

**★ ROOT record schema (SEVEN fields, S12):** `id` (uuid4) · `subject` · `timestamp` (ISO 8601, validated) · `content` · `re_reads` (list; `[]` = root, non-empty = reading) · `source_title` (string or None; optional/absence-tolerated on read) · **`role`** (speaker carried from source — `user`/`assistant`; required on new writes; tolerated-absent on read for legacy records).

**★ READING record schema — DESIGN-LOCKED (S13), NOT YET CODED.** ⚠ The sibling file `.nh_readings_store.jsonl` is *wired* (`append_reading` routes there) but `append_reading` is still ROOT-SHAPED (`subject, content, re_reads, role, …`) and `_validate_record` enforces the 7-field ROOT schema. The 8-field reading record — `id · reads (root id(s)) · meaning · confidence · role · story_layer · mode · timestamp` — has NO validator and NO writer yet; ZERO real readings exist. A reading NEVER copies root text — it points. Show = read readings → follow `reads` ids into sealed roots → stitch. A re-read is a NEW reading beside the old (R6). **FIRST 2c-adjacent build job: a reading-shaped `append_reading` + a reading validator.** **The two complex fields, design-settled S13:**
- **`story_layer` = a LIST of tellings** (so opposing readings of the same root both stay — clash kept, nothing wins). Each telling: optional `whose · stance · firmness · telling · theme · when`. Empty list = no story-reading yet (honest). Unknown parts OMITTED, never `"unknown"`-filled (absence read at read-time). The top-level `role` (who spoke) ≠ a telling's `whose` (in whose story).
- **`mode` = an OPEN word + confidence** (register: chat/composed/story/question/…). NOT a fixed menu — a menu would re-add a manual gate (R5 / הכל יחסי). One mode per reading; a different reading later is a NEW reading, not an edit.

**★ ON DISK NOW (verified S13):** **5,521 clean root records, SEALED**, all `re_reads=[]` (all roots — no real readings written yet), all 7-field, role-carried, source-timestamped, clean source_title. The sibling readings file is wired but holds **no real readings yet** (a test reading was written and deleted). *(The ~116k Chroma is the OLD unaligned index — §5/§11.15.)* **The remaining 2a-adjacent work is POPULATING readings — and that only happens once the engine (2c) exists to produce them.**

**No `reason`/`why` field, by design** — the why is shown by what a layer points at; the AI's view is the NOTE (§7B Part 7.5).

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [DESIGNED — not built]

*(§7A operating rules, §7B the meaning-engine mechanism, §7C build order — all UNCHANGED from MASTER-12 in substance. Preserved by reference; the key points below.)*

### 7A — THE UNIVERSAL FILTER (operating rules, full set unchanged):
R0 reader/layer-er not judge; R0.5 never close the book (may wonder/simulate); R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; **R5.5 the affirmation surface is a per-person STORY-layer (six optional parts: whose·when·stance·firmness·telling·theme; absence is itself read; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE);** R6 memory only ADDS (KEYSTONE); R7 the membrane (creation in chat, never closes in memory); R8 associative bridging as relevance-trigger; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is (the model does not grow).

### 7B — THE MEANING ENGINE (mechanism, full depth unchanged):
Part 0 THE PURE TAPE (deepest DUMB layer — verbatim, append-only, outside memory, captures always); Parts 1–2 the chain of webs (intent, deixis, common ground, implicature, theory-of-mind, time, re-reading, mode); Part 2.5 THE STORY-LAYER WEB (six optional parts, absence-read, clash); **Part 2.6 PERSON-BOXES (a GATHER over readings by `whose`, bounded by Ness's knowing, never synthesised; the tag is the wall; no-ruin + no-contaminate);** Part 3 webs combine (one camera, many lenses); Part 4 nightly research inward+outward (feeds the MEMORY, never the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live exception: catalog MAY ask, Ness present); **Part 6.5 THE WONDER/SIMULATION (kept-and-shown never decided; two walls — file door + eyes door; no scratch→memory path);** Part 7 THE LOG (read-only, subject-tagged, clickable); Part 7.5 THE NOTE/THE WHY (the AI's whole perspective, weightless, cannot harden, confidence never aggregates).

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) two-file routing + sealed roots — ✅ PLUMBING BUILT (S13); ⚠ READING RECORD NOT CODED.** What's on disk: `append_reading`→sibling file, roots sealed. What's NOT: the 8-field reading validator/writer (`append_reading` is still root-shaped). Reading record DESIGN-locked (`story_layer`=list, `mode`=open word, unknowns omitted). **The reading-record code is the FIRST job of the next milestone, folded into 2c.** → **(2b) the detector — ✅ INVESTIGATED, RECIPE LOCKED (S13).** Full read-only investigation: shape tops out ~91.6% (proven), meaning (embeddings) breaks it; locked recipe = embed+shape → StandardScaler → LogisticRegression(C=0.1) → **~94.89% honest (5-fold)**. NOT deployed — a FALLBACK for sources lacking `role`; build the live detector later from the recipe. → **(2c) the engine — THE NEXT MILESTONE — first code the reading-record writer/validator, then the chain-of-webs that READS a root and produces a real READING; fresh-head, the heart of the system.** **★ Build the LIVE path (memory → search → mouth → speak) BEFORE the nightly deepening.**

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. Findings land in the MEMORY as readings (§16), never the mouth.

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]
Access/auth (dry/personal/step-up); mobile three modes; interactive canvas; behavioral-baseline wellbeing; HUD redesign; the per-person STORY-layer "according to whom" field + person-boxes gather; image front door (§9A); phone-data importer; memory browser; voice in/out; ChromaDB cleanup; folder cleanup.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Metadata (firmly-told) → plain-description (low-opinion, confidence) → context-meaning (re-reading layer) → Ness confirms. The image front door is the PRECONDITION for the WhatsApp media ingest (§12).

## 10. ORIGINALITY (honest calibration)
The combination ships nowhere: the inverted default + per-person never-closing STORY model + DUMB/SMART split + person-boxes-as-gather + pure tape + wonder-kept-and-shown + memory-grows-not-the-mouth + two-destinations/two-files. Never claim inventing local AI, approval gates, or a trained model.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ BUILT + **5,521 CLEAN roots, SEALED (S13)** + verified. (c) wire the store into live flow — STILL OPEN; part of the model-wiring/live-path.
2. **THE FORCED ORDER — 2a half ✅ → 2b ✅ → 2c (READING-RECORD CODE + ENGINE) is NEXT:** **(2a) two-file ROUTING + sealed roots — ✅ BUILT (S13); ⚠ the 8-field reading-record validator/writer is NOT built (`append_reading` still root-shaped, zero real readings).** **(2b) detector — ✅ INVESTIGATED, recipe locked (S13).** → **(2c) THE NEXT MILESTONE, fresh-head:** FIRST code the reading-record (reading-shaped `append_reading` + reading validator), THEN the chain of webs (§7B) that READS a root and lays a real READING beside it. This POPULATES the empty readings file. **LIVE path (memory → search → mouth → speak) before nightly.**
2b. **★ THE DETECTOR — RECIPE LOCKED, LIVE BUILD DEFERRED (S13).** Recipe: embed (`all-MiniLM-L6-v2`) + 5 shape features (rel_length, no_uppercase, no_end_punct, starts_lowercase, has_code) → StandardScaler → LogisticRegression(C=0.1) → **~94.89% honest (5-fold)**. It's a FALLBACK — only used when a source LACKS `role` (a damaged import; the 5,521 carry true role). Building the live detector (train once, save the model, classify new role-less input) is a LATER job. **PARKED:** the full-LLM detector (`dolphin-llama3`, ~4–5 hr one-time grind) for the last ~1 point — an overnight job, not now.
3. **★ THE MODEL WIRING (§16) — local-first.** Wire `dolphin-llama3` (mouth) + the embedding search. **This is where the CHROMA REBUILD lives:** rebuild a search index FROM the 5,521 clean roots (the old `nh_reality_core` 116k is unaligned — keep until the new one is proven). **Forks (Ness's):** 8B-now vs 3B-fast; Llama vs Qwen — TEST on real Hebrew; VRAM-vs-context dial.
4. **★ NIGHT-SEARCH (committed, LATER).** Feeds the MEMORY as readings, never the mouth.
5. **Image-ingest front door (§9A)** — precondition for WhatsApp media.
6. **Universal Filter / meaning engine** — the §7 build = item 2's (2c).
7. **ChromaDB rebuild/cleanup** — see item 3; do NOT destroy the old 116k index before the new one is proven.
8. **Research pipeline build.**
9. **Hetzner sovereignty sync.**
10–12. nh_service (✅ disabled) · mobile + canvas · HUD redesign.
13. **★ THE [BUILT]-CLAIMS SWEEP — ✅ DONE (S13).** All six high-risk claims verified on disk; one inert phantom (`nh_peek.py` absent). Future builds touching old code still owe a quick existence-and-shape check.
14. **Folder cleanup** — incl. inert `cloudflared.exe`; the stale `peek.txt`; `verify_rt.py` scratch; AND **the ~12 S13 detector-investigation probe files** (`nh_detect_speaker*.py`, `nh_find_*.py`, `nh_classify_speaker.py`, `nh_honest_threshold.py`, `nh_tree_vs_forest.py`, `nh_embed_*.py`) — keep `nh_embed_tuned_speaker.py` + `nh_embed_confirm_speaker.py` as the recipe reference, the rest are dead-ends.
15. **★ §11.15 STORE-COUNT RECONCILIATION — ✅ CLOSED BY ACTION (S12).** Clean roots-of-record live in the flat store (5,521); Chroma stays as the to-be-rebuilt index; gpt_purified/cleaned_history correctly skipped.
16. **WhatsApp archive → eventual ingest (deferred):** decrypt `.crypt14` → SQLite front door → image front door for media → child-data call → ingest only with engine. Carry the sender. The most "Ness" data N.H will hold.
17. **Open design threads (low):** (a) spine re-draw / propagation; (b) old gate lags design (harmless while frozen, don't rip out); (c) `.cursorrules` reconciliation to the 7-field root + sealed two-file store + the §7-protected-list extras (`nh_research_engine.py`/`nh_auth.py`/`nh_metrics_tracker.py`); (d) clash + gap-read + kept-simulation UI surfacing; (e) write the §0A DUMB/SMART section into final place; (f) ~24 unreviewed Cursor batch files (`git status`); (g) person-box mechanics (multi-box tagging: one reading multiple `whose`? or `whose`+`about`?).

### ★ NEW OPEN PROBLEMS — surfaced by the S13 external critique (real gaps, named so 2c doesn't trip on them):
18. **★ MULTI-BOX (sealed-batch) ARCHITECTURE — undesigned.** The seal protects ONE file; the plan is "new raw → new sealed files," but there is no: batch naming scheme, root-id→batch resolution, manifest, cross-batch dedup, `read_all`-over-many-boxes, crash-safety between writing a root and updating a manifest, or decision on whether the batch id is part of the address (vs assuming UUIDs globally unique). **Must be designed before a SECOND batch is ever written.** Likely answer: a small append-only manifest + batch-prefixed addressing; design it, don't wing it.
19. **★ CONFIDENCE IS NAMED BUT NOT DEFINED — and one number hides four.** "confidence" currently conflates: (i) **interpretation confidence** (how sure the engine is of its reading), (ii) **source reliability** (how trustworthy the originating evidence is), (iii) **story firmness** (how firmly a person holds a telling — already a story_layer part), (iv) **retrieval relevance** (how well a memory matches a query). Collapsing them into one number = HIDDEN AUTHORITY (a soul violation — §0). **Decision owed: keep these as SEPARATE fields, never a single blended score.** Also: confidence must NOT rise just because several readings copied the same original error (no false corroboration), and a later reading must not silently inherit a prior's confidence.
20. **★ NO MEASURABLE DEFINITION OF "UNDERSTANDING" — build a gold-standard set.** "Memory is understood knowledge that grows" is an aspiration, not a spec. **The single highest-value next move (per the critique, and agreed): hand-annotate a small set of ~10–30 real roots with their true readings (meaning, mode, story-layer), and test the engine against it.** This (a) forces the reading-record code to actually exist, (b) makes "understanding" falsifiable, (c) exposes the confidence + context problems in practice not theory, (d) ends constitution-vs-machine drift. Distinguishes: retrieve-right-sentence vs identify-speaker vs read-intent vs connect-to-earlier vs recollection-vs-claim vs preserve-disagreement vs answer-accurately.
21. **★ RE-READ LIFECYCLE — append-only needs view/dedup rules.** A single root may accrete: initial + contextual + corrected + per-person + nightly + new-model readings, some contradictory. Append-only is fine philosophically but unbounded computationally. **Owed: when is a re-read justified; near-duplicate detection; can a reading explicitly SUPERSEDE another (a pointer, not a delete); how old readings stay visible without dominating retrieval; how nightly jobs are stopped from spawning endless paraphrases.** Lifecycle moves into pointers and views, it doesn't disappear.
22. **★ PERSON-BOX CONTAMINATION — needs per-element provenance.** A gather can mix: what a person literally said · what Ness thought they meant · what N.H inferred · what someone ELSE said about them · old vs current. "Bounded by Ness's knowing / never synthesised" is the right principle but needs teeth: each gathered element carries its provenance so retrieval can't make a cluster feel like a settled identity.
23. **★ OFF-BOARD AFFIRMATION HAS NO FEEDBACK PATH — readings can't be learned-from.** If Ness's reactions stay entirely outside the engine, N.H can't tell that a reading was useful / mistaken / rejected, so it may resurface interpretations he already dismissed. **Fix consistent with the soul: record the reaction as a STORY-LAYER EVENT ("Ness accepted/rejected this reading for this purpose at this time"), NOT as a promoted fact.** Not a truth-button — a dated, weightless note that retrieval can read. *(This is the one place the off-board principle needs a careful seam — the affirmation stays off-board as TRUTH, but its OCCURRENCE can be recorded as story.)*
24. **★ PRIVACY / THREAT MODEL — first-class before sensitive ingest.** Encryption-at-rest is necessary not sufficient. Owed before WhatsApp/child-data (already frozen): which processes can decrypt; do logs/Ollama-prompts expose plaintext; do embeddings leak sensitive content; backup encryption; same-Windows-account malware exposure; **and a REDACTION/DESTRUCTION path (see §0A-PURE-TAPE correction below).**

---

## 11-SETTLED. (condensed)
- **S4:** unit = per-message; honest provenance placeholder subject; ChatGPT `title` rides in `source_title` not subject; read-only on sources; pick the choice that destroys least.
- **S5:** gpt_purified per-turn on role markers; cleaned_history set aside (0 structure + damaged).
- **S7:** unit = span-claim not cut; two places; why shown by pointers; only span = `re_reads`.
- **S9 (speaker):** store dropped speaker on gpt_purified; SOURCE files carry `[NESS]:`/`[AI_RECALL]:`; alternation broken (flip 27.9% — detector must NOT assume turn-taking); length powerful (NESS median 9, AI median 170); "?" a TRAP (31.8%); **CARRY `role`, back-filled from source — do NOT re-derive from shape.** *(S12 applied this exactly: the ChatGPT JSON `author.role` is carried straight onto every root.)*
- **S9–S10 (soul):** premise §0; reality → per-person STORY-layer; N.H not a teller; mode = peer web; firmness READ; clash a feature; DUMB/SMART; Helper-not-Decider; two-file 2a.
- **S11 (model + subsystems):** borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction (three truths); memory-grows-not-the-mouth.
- **★ S12 (the build):** store restored from bytecode; `role` added (7-field root); clean ingest pipeline built; 5,521 clean roots; gpt_purified/cleaned_history skipped; §11.15 closed; Chroma is the old unaligned 116k index; reading-records = organized-fields + two-files (both walls); the two-destinations shape (raw root + filter-reading-beside).
- **★ S13 (2a plumbing built + detector investigated):** [BUILT]-claims sweep done (floor confirmed, 1 inert phantom `nh_peek.py`); **2a PLUMBING BUILT** — `append_reading`→sibling `.nh_readings_store.jsonl`, roots SEALED via `.nh_roots.sealed` (per-batch). ⚠ The 8-field reading record is DESIGN-locked (`story_layer`=LIST, `mode`=OPEN word, unknowns OMITTED) but NOT coded — `append_reading` still root-shaped, no validator, zero real readings. **2b DETECTOR investigated** (10 methods, honest grading): shape ceiling ~91.6%; embeddings broke it → 93.5%; embed+shape → 94.7%; tuned C=0.1 + 5-fold → honest **94.89%**. Recipe locked, NOT deployed (fallback for role-less sources); LLM detector parked.

---

## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN]
A13 WhatsApp 2012→2024 (age 7 → 2024), encrypted (`msgstore.db.crypt14` + backups, ~118 MB), copied to `C:\Phone_A13_Backup` + Drive. **SETTLED: ingest FROZEN** — archive now, ingest later. When it enters: decrypt → SQLite front door (carry the sender) → **image front door for media (§9A, precondition)** → child-data call → ingest. *(S12 clarified: the MEDIA is a concrete blocker — a text parser can't ingest photos; the image front door must exist first. Alongside: encryption, child-data sensitivity, engine-first.)*

---

## 13. THE LIVE LOOP  [DESIGNED — not built]
A figure-eight, cache outside. Fire-and-let-go starter; deep side (memory · filter · search model · mouth · wonder), each on its own clock. **★ The live path (memory → search → mouth → speak) is this loop's everyday cycle — build it first.**

## 14. THE CHAT FRONT DOOR  [DESIGNED-IN-PROGRESS]
The live chat is itself an input. **TWO STAGES:** RAW (untouched words → root material, onto the tape) → CATALOG (file by who/when/where; "who is he?" = deixis from local context, revisable; live chat MAY ask, Ness present; nightly never asks). Memory is PULLED every turn as context (by meaning, keeping clashes/gaps), used silently; reply words generated fresh by the mouth from the read, never the raw, never narrating the mechanism; the point-back is the one surfaced thread. Capture resolved by the tape (capture always; crossing into memory deliberate).

## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done]
Boot HUD traced to Windows "reopen apps" + a disguised launcher (handled); Kensington fingerprint key; `nh_vector_memory.py` added to `.cursorrules` §7; stray `install_startup.bat` deleted.

---

## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk]

**THE CENTRAL TRUTH.** The language model is a borrowed, FROZEN mouth + general knowledge — a commodity. Everything that makes N.H *N.H* lives OUTSIDE the model. Engine vs car: the model is the engine; N.H is the car. *Jarvis is the memory + soul + gathering + mouth, wired together.*

**WHY NOT TRAIN ONE.** Training a base model is the wrong resource category (thousands of GPUs, millions of dollars). Putting knowledge in the MEMORY instead keeps it yours, dated, layered, point-back-able, never-closed.

**★ TWO MODELS, TWO JOBS.** (a) WORDING/generation — the mouth, writes the reply word-by-word (heavy load); (b) SEARCHING/retrieval — the embedding model, finds memories by meaning not words (tiny, near-free). **ORDER: search first, word last.** On disk: `all-MiniLM-L6-v2` + ChromaDB. *(★ S12: the current Chroma `nh_reality_core` (116k) is the OLD index over OLD data — when wiring search, REBUILD it from the 5,521 clean roots so search and roots share one world; keep the old one until the new is proven.)*

**★ GROWTH LANDS IN THE MEMORY, NEVER THE MOUTH.** Night-search lands in the store as new readings. Jarvis knows more tomorrow because his understood-memory grew, not because his brain did.

**THE DECISION — LOCAL-FIRST.** Sovereign, offline, private, uncensored. The model is swappable behind the meaning step (an API "reach" could be added later without re-architecting), but local is the chosen default.

**ON-DISK STATE + FORKS (Ness's):** `dolphin-llama3` (UNCENSORED, 8B) — the uncensored mouth, already pulled. `llama3` (8B). `all-MiniLM-L6-v2` — the search model. Runtime Ollama, GGUF. **FORK (i):** keep 8B (uncensored now, slow ~7–9 tok/s) vs pull an uncensored 3B (fast ~35–50). **FORK (ii):** Llama 3.2 3B (speed) vs Qwen 2.5 3B (Hebrew) — **TEST on real Hebrew before locking.** **FORK (iii):** the VRAM-vs-context dial. **FUTURE (not now):** used RTX 3060 12GB.

---

**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk — re-proven through S13; the honest 5-fold check caught a lucky-split number and gave the real one) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step (the roots were backed up `bak_preseal` before sealing) · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board (§0)** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary (§0A)** · **the affirmation surface is a per-person STORY — firm-but-open, never collapsed, never closed; absence is read; N.H is NOT a teller (weightless note that cannot harden)** · **★ TWO DESTINATIONS: every input → raw root (sealed) + a reading beside it (the filter's read); raw stays raw, understanding accretes; this is why TWO FILES — the ROUTING is built (S13), the reading record itself is not yet coded** · **★ `story_layer` is a LIST so clash is kept and nothing wins; `mode` is an OPEN word so no manual gate sneaks back in; unknowns are OMITTED not faked (S13)** · **★ CARRY THE SPEAKER, DON'T GUESS IT — `role` lives on the root, from source (S12); and where role is ABSENT, the detector is a measured FALLBACK (~94.9% honest), never an override (S13)** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE records every move, outside memory; capture always, commit deliberately** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; two models; night-search feeds the MEMORY not the mouth; local-first; never train a base model** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read, never narrates its mechanism; the point-back is the one surfaced thread** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id, never copying** · **ONE FILTER, BOTH DIRECTIONS — inward the mirror, outward the engine, each feeding the other** · memory only adds · the membrane · a unit is a span-claim not a cut · input-agnostic, many front doors (RAW → CATALOG) · archive don't ingest · הכל יחסי — meaning is relative, revisable, and relative-to-whom · don't overclaim · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them now clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — gathering each person into a box that is Ness's own knowing of them and never them, recording every move on an untouchable tape underneath, wondering forward at night and keeping every wonder shown rather than decided, so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone; every input lands in two places at once — raw into the sealed root, and through the filter that reads it and lays understanding beside it — the dumb machinery holds the data and cannot interpret, the smart machinery reads the person and cannot close, the membrane stands between them, the mouth is a swappable tool that grows nothing while all the growth lands in the understood memory it speaks from, and where two tellings disagree the system shows the clash rather than choosing — because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
