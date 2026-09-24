# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the model layer, the person-boxes, the tape, the DUMB-vs-SMART machinery frame, AND the code rules — is written out IN FULL below. Nothing is referenced-only.

*Rebuilt June 20 2026 (session 3); updated sessions 4–11. **Session 12 (June 22 2026, late) is a LARGE BUILD-and-verify session → this is MASTER-13.** Unlike S11 (design + diagnosis), S12 **wrote real code to disk and ran the first clean ingest.** It (1) discovered and CORRECTED the master's deepest errors by disk verification — including that `nh_accretive_store.py` was MISSING from disk (recovered from bytecode), `append_reading` was NOT a stub, the design said two-files but the code did one-file, the 188 records had `source_title` inlined into content, Chroma holds 116,391 items not "~11k"; (2) RESTORED the store module from its compiled `.pyc`; (3) ADDED `role` to the root schema (six → seven fields) — a deliberate, reasoned schema change; (4) BUILT a clean ChatGPT-export ingest parser (tree-walk ordering, clean fields, junk-skip); (5) RAN it for real on all three JSON sources → **5,521 clean roots on disk, fully verified**; (6) checked and correctly SKIPPED `gpt_purified` (0 unique — fully covered, scrambled, no timestamps) and `cleaned_history` (damaged); (7) CLOSED §11.15 by action — the store-count reconciliation is resolved, clean roots live in the flat store; (8) verified Chroma is the OLD unaligned index (116k items) to be rebuilt later. The forced build order (§7C/§11) is STILL UNCHANGED; 2a is now properly unblocked.*

---

> **WHAT CHANGED IN SESSION 12 (the short delta — read this first):**
>
> **0. ★ THE STORE IS NOW REAL AND CLEAN — 5,521 VERIFIED ROOTS ON DISK.** The flat accretive store `.nh_accretive_store.jsonl` now holds **5,521 clean root records**, all verified: every one has `role` (carried from source), `source_title` in its own field, real source timestamp, true conversation order, no junk prefix, zero rejects. Split by source: `seed:conversations_001` = 3,179 · `seed:conversations_000` = 2,172 · `seed:conversations_002` = 170. Span Oct 2024 → May 2026, 202 conversations, near-even dialogue (2,675 user / 2,846 assistant). **This replaces the old 188-record stub entirely** (the 188 were retired; backed up at `.nh_accretive_store.jsonl.bak_188_preclean`).
>
> **1. ★ FIVE DISK-TRUTHS THAT CORRECTED THE MASTER (verify-on-disk earned its place five times in one session):**
>    - **(a) The store count was wrong AGAIN, twice over.** S11 corrected 11,374 → 188. S12 found peek.txt (5,041 lines) is just the SAME 188 reformatted (pretty-printed JSON — near-identical byte size, ~240 KB each), NOT a third corpus. So the "three counts" collapsed to: 188 flat (=peek) + a separate Chroma corpus.
>    - **(b) `nh_accretive_store.py` WAS MISSING FROM DISK.** The master called it [BUILT & VERIFIED]; it was not on disk at all. Only its compiled bytecode survived (`__pycache__\nh_accretive_store.cpython-313.pyc`). The source `.py` had been deleted; the 188-record `.jsonl` was an orphan with no live writer. **RECOVERED:** the function list + all string constants + schema were read out of the `.pyc` via Python's built-in `marshal`/`dis`; the module was reconstructed faithful to the recovered constants and the data's actual shape, and verified (round-trip: read the existing records without crash).
>    - **(c) `append_reading` was NOT a stub.** The master said it was an empty stub awaiting the §2a build. The recovered constants show it had real validation/append logic, writing readings into the SAME file as roots (distinguished by `re_reads`: empty = root, non-empty = reading). So the deployed code was a ONE-FILE design — contradicting the master's settled TWO-FILE design (which was never actually built in code).
>    - **(d) The 188 seed records had `source_title` INLINED into content** as a `[source_title: ...]` text prefix, NOT in a structured field. The records were five-field (id, subject, timestamp, content, re_reads) with no `source_title` key and no `role`. (All 188 retired in the re-ingest, so this is moot going forward — the new 5,521 are clean.)
>    - **(e) Chroma holds 116,391 items, not "~11k".** Collections: `nh_reality_core` = **116,391**, `nh_test_asm` = 1,180, `nh_simulation_core` = 263. The big one is ~20× the clean roots and ~10× the master's guess — it is the OLD index (chunked / old raw data / accumulated), NOT a search index over the clean roots. It does NOT align with the flat store and must be REBUILT from the clean roots when the search/model layer is wired (§16 / §11 item 3). Keep it (don't delete — 1.78 GB of old work) until the new index is proven.
>
> **2. ★ SCHEMA CHANGE — `role` ADDED TO THE ROOT (six → seven fields), on purpose.** The root schema is now: `id · subject · timestamp · content · re_reads · source_title · role`. `role` is the speaker (`user`/`assistant`) carried STRAIGHT FROM SOURCE — never guessed (master rule §11C-S9). REQUIRED on new writes; `read_all` tolerates old records lacking it (read-tolerance). Reasoning: a root with no speaker would force the readings layer to GUESS who spoke — the exact thing forbidden. Keeping Ness's voice and the AI's voice separate at the root is the membrane applied to ingest. **This CORRECTS the prior master line "ROOT record has NO role field" — that was the design when role was meant to live only on readings; S12 moved it onto the root because the source carries it and it must not be lost.** `append_root`/`append_reading` also gained an optional `timestamp` param so the real source time is preserved (not stamped "now").
>
> **3. ★ THE CLEAN INGEST PIPELINE — BUILT AND PROVEN.** `nh_ingest_chatgpt.py`: reads a ChatGPT-export JSON (list of conversation dicts), walks each `mapping` tree in TRUE order (backward from `current_node` via `parent` links, then reversed — skipping abandoned edit/regenerate branches), keeps only real text messages (`message` present, `content_type == "text"`, role in {user, assistant}, non-empty), and writes ONE clean root per message via `append_root` with role + real timestamp + clean `source_title` (the conversation `title`) + no inline prefix. DRY_RUN flag (prints-vs-writes). Per-message unit (§11A, unchanged). Proven on all three JSON sources.
>
> **4. ★ §11.15 CLOSED BY ACTION.** The store-count reconciliation is resolved: the clean roots-of-record live in the FLAT store (5,521), Chroma stays as the (to-be-rebuilt) search index. The decision was A (flat = sealed roots, Chroma = rebuildable index over them) — chosen because roots living only inside a search index is fragile, and the sources were confirmed recoverable on disk. Forks 2 (rebuild-188-clean) and 3 (flat-vs-Chroma) MERGED into the single clean ingest.
>
> **5. ★ `gpt_purified` and `cleaned_history` — both correctly NOT ingested.** `gpt_purified_history.txt`: 202 conversations, **ALL 202 already in the store** from the JSON sources (0 unique). It is scrambled (answer-before-question — no parent links, no timestamps, order unrecoverable) and 100% redundant → SKIP, like its cousin `cleaned_history` (damaged, §11B). Don't force damaged/duplicate data into the clean set.
>
> **6. NET FOR THE BUILD:** The floor is built and clean. **Forced build order UNCHANGED:** (2a) two-file split + lock the reading record → (2b) detector → (2c) engine; LIVE path before nightly. **2a is now properly unblocked** — its roots exist, clean, where the code expects. Chroma rebuild is a LATER (model-wiring) job, now documented not lurking. WhatsApp still frozen (encrypted, needs image front-door, child-data, engine-first).

> **★ DECISIONS LOCKED IN SESSION 12 (protect from re-litigation):**
> - **Reading records = ORGANIZED FIELDS** (the 8-field shape), NOT just text-that-points. Chosen because person-boxes/clash/firmness all need structured fields to gather on. *(The INSIDES of the two complex fields — `story_layer`'s six parts and `mode` — are still OPEN, a finer fork for fresh-head 2a.)*
> - **TWO FILES** — roots sealed in their own file, readings in a sibling pointing by id. Ness wanted BOTH walls: the physical seal (roots file goes quiet once readings file exists) AND the logical `re_reads` validation wall. Different failure modes, both covered.
> - **`role` on the root, carried from source** (§ schema change above).
> - **Flat store = roots-of-record; Chroma = rebuildable index** (§11.15 resolution).
> - **`gpt_purified` + `cleaned_history` = NOT ingested** (redundant / damaged).
> - **The TWO-DESTINATIONS shape (Ness re-derived it himself):** every input goes to TWO places — (1) the RAW ROOT, saved untouched/sealed; (2) THROUGH THE FILTER, which READS it and lays a READING beside the root (never altering the raw). The filter does not "filter" the root — raw stays raw forever; understanding accretes beside it. This IS why there are two files. The roots ingested in S12 are place 1; the filter (place 2) reads them later, as its own pass — which is why raw-in-now and filter-reads-later are not a contradiction but the two ordered steps.

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

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. As of S12: the clean store + the role schema + the ingest pipeline are **[BUILT & VERIFIED]**. The filter/engine, the readings layer (2a), the model wiring, the person-boxes, the tape, the wonder, the catalog are **[DESIGNED]**. The old REALITY/SIMULATION gate still runs harmlessly while the engine doesn't exist.

> **★ A STANDING LESSON FROM S12 — the [BUILT]-CLAIMS SWEEP IS OWED.** The master was wrong FIVE times tonight about things it called "built/verified" (the count twice, the missing module, the not-a-stub, the inline source_title, the Chroma size). Before building 2a, do a quick existence-and-shape sweep of every remaining [BUILT] claim in §5/§6, so 2a isn't built on a sixth phantom. Trust disk, never the doc's remembered state — including this file's.

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

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame]

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The pure tape, the append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), the role-carried-from-source, the catalog's who/when/where marking, the mode/form-naming, the person-box GATHER, the live loop's fire-and-let-go. One law: **never interpret, never close — only add / point / carry / sort / gather.** Safe BECAUSE it cannot interpret.
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

**Physical stores on disk (verified S12):**
- **`.nh_accretive_store.jsonl` — 5,521 CLEAN roots** (~the new clean corpus; 7-field schema). The roots-of-record.
- **`.nh_accretive_store.jsonl.bak_188_preclean`** — backup of the retired 188 stub.
- **`chroma_db\` — ChromaDB, `chroma.sqlite3` ≈ 1.78 GB.** Collections: `nh_reality_core` = **116,391** (the big OLD index — chunked/old data, NOT aligned to the clean roots; rebuild later, keep until proven), `nh_test_asm` = 1,180, `nh_simulation_core` = 263.
- OLD-model stores: `.nh_memory_store.jsonl` · `.nh_reality_store.jsonl` / `.nh_simulation_store.jsonl` · `.nh_simulation_graph.jsonl` / `nh_mental_network.json`.
- `peek.txt` (5,041 lines = the OLD 188 reformatted — stale now), `nh_log.html`.

**Source files on disk (the ingest inputs):**
- `conversations-000.json` (100 convs → 2,172 roots), `conversations-001.json` (100 → 3,179), `conversations-002.json` (23 → 170). **All three INGESTED CLEAN S12.**
- `gpt_purified_history.txt` (202 convs, ALL already covered — NOT ingested), `cleaned_history (1).txt` (damaged — NOT ingested).

**Models on disk (verified S11):** Ollama `dolphin-llama3:latest` (UNCENSORED, 4.7 GB, 8B) · `llama3:latest` (4.7 GB, 8B). `models\all-MiniLM-L6-v2` (embedding/search model — its vectors fill the OLD Chroma).

**Accretive store + tooling [BUILT & VERIFIED]:**
- **`nh_accretive_store.py`** — RESTORED S12 from bytecode + extended with `role`. Append-only (every `open()` is `"a"`/`"r"`, no `"w"`); schema validated before every append. **7-field ROOT schema:** `id · subject · timestamp · content · re_reads · source_title · role`. 8 functions: `_coerce_source_title`, `_validate_record`, `_append_record`, `_new_record`, `append_root(subject, content, role, source_title=None, timestamp=None)`, `append_reading(subject, content, re_reads, role, source_title=None, timestamp=None)`, `read_all`, `read_by_subject`. `append_reading` currently writes to the SAME file (one-file); the §2a build splits it to a sibling readings file.
- **`nh_ingest_chatgpt.py`** — RESTORED/BUILT S12. The clean ChatGPT-export ingest (tree-walk ordering, clean fields, junk-skip, DRY_RUN flag). Reusable for any ChatGPT-export JSON by changing `SOURCE_FILE` + `SUBJECT_TAG`.
- `verify_rt.py` — round-trip checker.
- `nh_peek.py` · `nh_log.py`→`nh_log.html` · `nh_probe.py` / `nh_probe_truth.py` (read-only tools).

**`.cursorrules` v3.1 (in-force):** §6A. On disk = 15,303 bytes. **⚠ S12 note: §6A still describes the OLD root schema (no role) and the one-gate model — it needs a reconciliation pass to reflect the 7-field root + the clean store. INCOMING, not yet done.**

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **★ THE CLEAN ACCRETIVE STORE — 5,521 roots (S12), 7-field schema, role-carried, real timestamps, true order, zero junk, verified.**
- **★ The restored store module** (`nh_accretive_store.py`) + **the clean ingest pipeline** (`nh_ingest_chatgpt.py`).
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

**Module:** `nh_accretive_store.py` (restored S12). 4 public + 4 private functions; every `open()` is `"a"`/`"r"`, no `"w"`; schema validated before every append.

**★ ROOT record schema (SEVEN fields, S12):** `id` (uuid4) · `subject` · `timestamp` (ISO 8601, validated) · `content` · `re_reads` (list; `[]` = root, non-empty = reading) · `source_title` (string or None; optional/absence-tolerated on read) · **`role`** (speaker carried from source — `user`/`assistant`; required on new writes; tolerated-absent on read for legacy records).

**★ READING record schema (the §2a DESIGN — NOT yet built as a separate file):** the 8-field reading record lives in a NEW sibling `.nh_readings_store.jsonl` (does not exist yet). Fields: `id · reads (root id(s)) · meaning · confidence · role · story_layer · mode · timestamp`. A reading NEVER copies root text — it points. Show = read readings → follow `reads` ids into sealed roots → stitch. A re-read is a NEW reading beside the old (R6). **The §2a build: (1) lock the reading record (the INSIDES of `story_layer`'s six parts + `mode` are the open fork); (2) redirect `append_reading` to write the sibling readings file instead of the roots file; (3) seal the roots file.**

**★ ON DISK NOW (verified S12):** **5,521 clean root records**, all `re_reads=[]` (all roots, no readings yet), all 7-field, role-carried, source-timestamped, clean source_title. The readings file does not yet exist. *(The ~116k Chroma is the OLD unaligned index — §5/§11.15.)*

**No `reason`/`why` field, by design** — the why is shown by what a layer points at; the AI's view is the NOTE (§7B Part 7.5).

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [DESIGNED — not built]

*(§7A operating rules, §7B the meaning-engine mechanism, §7C build order — all UNCHANGED from MASTER-12 in substance. Preserved by reference; the key points below.)*

### 7A — THE UNIVERSAL FILTER (operating rules, full set unchanged):
R0 reader/layer-er not judge; R0.5 never close the book (may wonder/simulate); R1 one filter, no source exempt; R2 sorts/reads, never closes "real"; R3 one continuous reader; R4 meaning from wide context; R5 classification never locked; **R5.5 the affirmation surface is a per-person STORY-layer (six optional parts: whose·when·stance·firmness·telling·theme; absence is itself read; CLASH surfaced not resolved; N.H not a teller, its view a weightless NOTE);** R6 memory only ADDS (KEYSTONE); R7 the membrane (creation in chat, never closes in memory); R8 associative bridging as relevance-trigger; R9 sort by meaning-type, mode a separate peer web; R10 maximal-but-bounded; R11 Ness steers, affirms off-board; R12 honesty about what this is (the model does not grow).

### 7B — THE MEANING ENGINE (mechanism, full depth unchanged):
Part 0 THE PURE TAPE (deepest DUMB layer — verbatim, append-only, outside memory, captures always); Parts 1–2 the chain of webs (intent, deixis, common ground, implicature, theory-of-mind, time, re-reading, mode); Part 2.5 THE STORY-LAYER WEB (six optional parts, absence-read, clash); **Part 2.6 PERSON-BOXES (a GATHER over readings by `whose`, bounded by Ness's knowing, never synthesised; the tag is the wall; no-ruin + no-contaminate);** Part 3 webs combine (one camera, many lenses); Part 4 nightly research inward+outward (feeds the MEMORY, never the mouth); Part 5 hold-until-enough; Part 6 can't-fill→inform-don't-ask (live exception: catalog MAY ask, Ness present); **Part 6.5 THE WONDER/SIMULATION (kept-and-shown never decided; two walls — file door + eyes door; no scratch→memory path);** Part 7 THE LOG (read-only, subject-tagged, clickable); Part 7.5 THE NOTE/THE WHY (the AI's whole perspective, weightless, cannot harden, confidence never aggregates).

### 7C — THE FORCED BUILD ORDER (never re-fought):
**(2a) reading-layer record shape + two-file split** — FULLY DESIGNED; the §6A.8 store-touching, fresh-head, top-of-session piece; **NOW UNBLOCKED (its roots exist clean, S12).** Left: lock the 8-field reading record (INSIDES of `story_layer`/`mode` are the open fork), redirect `append_reading` to the sibling file, seal the roots file. → **(2b) the detector** — read-only probe FIRST (length strong, "?" a trap, allow doubling). → **(2c) the engine** — the full chain-of-webs; LAST. **★ Build the LIVE path (memory → search → mouth → speak) BEFORE the nightly deepening.**

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

1. **Append-only accretive store** — ✅ BUILT + **5,521 CLEAN roots (S12)** + verified. (c) wire the store into live flow — STILL OPEN; part of the model-wiring/live-path.
2. **THE FORCED ORDER — 2a → detector → engine:** **(2a) two-file split + lock the reading record — DESIGNED, NOT built, NOW UNBLOCKED.** Fresh-head, dry-run, top-of-session. Open inside it: the INSIDES of `story_layer` (six parts) + `mode`. → (2b) detector → (2c) engine. LIVE path before nightly.
3. **★ THE MODEL WIRING (§16) — local-first.** Wire `dolphin-llama3` (mouth) + the embedding search. **This is where the CHROMA REBUILD lives:** rebuild a search index FROM the 5,521 clean roots (the old `nh_reality_core` 116k is unaligned — keep until the new one is proven). **Forks (Ness's):** 8B-now vs 3B-fast; Llama vs Qwen — TEST on real Hebrew; VRAM-vs-context dial.
4. **★ NIGHT-SEARCH (committed, LATER).** Feeds the MEMORY as readings, never the mouth.
5. **Image-ingest front door (§9A)** — precondition for WhatsApp media.
6. **Universal Filter / meaning engine** — the §7 build.
7. **ChromaDB rebuild/cleanup** — see item 3; do NOT destroy the old 116k index before the new one is proven.
8. **Research pipeline build.**
9. **Hetzner sovereignty sync.**
10–12. nh_service (✅ disabled) · mobile + canvas · HUD redesign.
13. **★ THE [BUILT]-CLAIMS SWEEP (NEW, S12 — do before 2a).** The doc was wrong 5× tonight about "built" things. Sweep §5/§6 existence-and-shape so 2a isn't built on a sixth phantom.
14. **Folder cleanup** — incl. inert `cloudflared.exe`; the stale `peek.txt`; `recovered_accretive.txt`, `nh_accretive_store_v2.py`, `verify_rt.py` scratch from S12.
15. **★ §11.15 STORE-COUNT RECONCILIATION — ✅ CLOSED BY ACTION (S12).** Clean roots-of-record live in the flat store (5,521); Chroma stays as the to-be-rebuilt index; gpt_purified/cleaned_history correctly skipped.
16. **WhatsApp archive → eventual ingest (deferred):** decrypt `.crypt14` → SQLite front door → image front door for media → child-data call → ingest only with engine. Carry the sender. The most "Ness" data N.H will hold.
17. **Open design threads (low):** (a) spine re-draw / propagation; (b) old gate lags design (harmless while frozen, don't rip out); (c) `.cursorrules` reconciliation to the 7-field root (now NAMED, S12); (d) clash + gap-read + kept-simulation UI surfacing; (e) write the §0A DUMB/SMART section into final place; (f) ~24 unreviewed Cursor batch files (`git status`); (g) person-box mechanics (multi-box tagging: one reading multiple `whose`? or `whose`+`about`?).

---

## 11-SETTLED. (condensed)
- **S4:** unit = per-message; honest provenance placeholder subject; ChatGPT `title` rides in `source_title` not subject; read-only on sources; pick the choice that destroys least.
- **S5:** gpt_purified per-turn on role markers; cleaned_history set aside (0 structure + damaged).
- **S7:** unit = span-claim not cut; two places; why shown by pointers; only span = `re_reads`.
- **S9 (speaker):** store dropped speaker on gpt_purified; SOURCE files carry `[NESS]:`/`[AI_RECALL]:`; alternation broken (flip 27.9% — detector must NOT assume turn-taking); length powerful (NESS median 9, AI median 170); "?" a TRAP (31.8%); **CARRY `role`, back-filled from source — do NOT re-derive from shape.** *(S12 applied this exactly: the ChatGPT JSON `author.role` is carried straight onto every root.)*
- **S9–S10 (soul):** premise §0; reality → per-person STORY-layer; N.H not a teller; mode = peer web; firmness READ; clash a feature; DUMB/SMART; Helper-not-Decider; two-file 2a.
- **S11 (model + subsystems):** borrowed frozen mouth; two models; local-first; person-boxes; pure tape; wonder kept-and-shown; catalog; soul-correction (three truths); memory-grows-not-the-mouth.
- **★ S12 (the build):** store restored from bytecode; `role` added (7-field root); clean ingest pipeline built; 5,521 clean roots; gpt_purified/cleaned_history skipped; §11.15 closed; Chroma is the old unaligned 116k index; reading-records = organized-fields + two-files (both walls); the two-destinations shape (raw root + filter-reading-beside).

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
Evidence over narrative (verify on disk — re-proven FIVE times in S12) · one concrete step at a time · finish the thing in front before scope-expanding · backup before any destructive step · **NEVER DECIDE FACTS — never close the book (§0)** · **N.H is Ness's HELPER, not his DECIDER; the engine never decides; Ness affirms off the board (§0)** · **TWO MACHINERIES: DUMB (can't interpret) vs SMART (can't close); the membrane is the boundary (§0A)** · **the affirmation surface is a per-person STORY — firm-but-open, never collapsed, never closed; six optional parts; absence is read; N.H is NOT a teller (weightless note that cannot harden)** · **★ TWO DESTINATIONS: every input → raw root (sealed) + a reading beside it (the filter's read); raw stays raw, understanding accretes; this is why TWO FILES** · **★ CARRY THE SPEAKER, DON'T GUESS IT — `role` lives on the root, from source (S12)** · **a PERSON-BOX is a GATHER bounded by Ness's knowing, never synthesised** · **THE PURE TAPE records every move, outside memory; capture always, commit deliberately** · **N.H WONDERS forward, keeps every wonder SHOWN not decided** · **THE MODEL IS A BORROWED FROZEN MOUTH; two models; night-search feeds the MEMORY not the mouth; local-first; never train a base model** · **MEMORY IS UNDERSTOOD KNOWLEDGE THAT GROWS** · **the chat PULLS memory silently, speaks fresh from the read, never narrates its mechanism; the point-back is the one surfaced thread** · **mode is a peer web; firmness READ; clash surfaced never resolved** · **TWO FILES: roots sealed, readings beside, pointing by id, never copying** · **ONE FILTER, BOTH DIRECTIONS — inward the mirror, outward the engine, each feeding the other** · memory only adds · the membrane · a unit is a span-claim not a cut · input-agnostic, many front doors (RAW → CATALOG) · archive don't ingest · הכל יחסי — meaning is relative, revisable, and relative-to-whom · don't overclaim · the spine line: **stop forcing the decision, build a structure where not-deciding is safe.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it borrows a frozen mouth to put words to meaning, runs a tiny search model to find memories by meaning not words, and keeps a memory of two files — sealed roots (5,521 of them now clean on disk, each carrying who-spoke from source) and readings floating beside them pointing by id, only ever added to, never closing the book — gathering each person into a box that is Ness's own knowing of them and never them, recording every move on an untouchable tape underneath, wondering forward at night and keeping every wonder shown rather than decided, so meaning and how-each-thing-sits-in-whose-story can keep evolving forever without hardening into a fact that pretends to be true for everyone; every input lands in two places at once — raw into the sealed root, and through the filter that reads it and lays understanding beside it — the dumb machinery holds the data and cannot interpret, the smart machinery reads the person and cannot close, the membrane stands between them, the mouth is a swappable tool that grows nothing while all the growth lands in the understood memory it speaks from, and where two tellings disagree the system shows the clash rather than choosing — because N.H was never about escaping reality or training a brain, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
