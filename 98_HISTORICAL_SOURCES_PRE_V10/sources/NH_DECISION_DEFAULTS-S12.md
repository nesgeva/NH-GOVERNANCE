# N.H — DECISION DEFAULTS
### Send this alongside the N.H master. Its only job: stop handing Ness forks that were never really open. The master says WHAT the system is; this says WHEN you may ask Ness to choose and when you must just proceed. When this file and the master agree, follow them — don't re-ask.
*Updated session 12 (June 22 2026, late) to match MASTER-13: the STORE IS NOW BUILT AND CLEAN (5,521 verified roots, 7-field schema with `role`), §11.15 is CLOSED by action, the clean ingest pipeline exists, the reading-record = organized-fields and two-files (both walls) are SETTLED, the two-destinations shape is locked, and a hard new lesson — the master's [BUILT] claims must be disk-verified, not trusted (five fell in one session).*

---

## THE ONE RULE
**If the answer is already derivable from the master, take it. Do not ask. State the assumption inline and move.**
Asking Ness to pick something the document already decided is not safety — it is friction. Default to proceeding.

---

## STOP AND ASK *only* if one of these THREE is true (otherwise PROCEED):
1. **One-way door** — irreversible or lossy: deleting, overwriting, merging-away, a child-data/personal ingest call, anything that can't be un-done. **(Includes: anything that could destroy the clean 5,521-root store OR the 1.78 GB / 116k-item Chroma index. Backup before any destructive step — Ness will insist on it, so do it first.)**
2. **Store-touching change** — a §6A.8 dry-run-and-approve move: schema change, a Protected File edit, anything that writes to a production store or gate. *(The 2a build is exactly this. The Chroma rebuild is exactly this.)*
3. **A genuine either/or with real tradeoffs** the master does NOT settle.

**If none of the three apply → PROCEED. Pick the obvious next step, name the assumption in one line, keep going.**

---

## NEVER ASK ABOUT (the master already decided these — look it up, don't re-open):
- **What's next in a known sequence.** The forced build order is settled (§7C / §11 item 2): 2a (two-file split + reading record) → detector → engine; LIVE path before nightly. "What now" inside a settled order is a lookup.
- **Settled decisions.** Anything marked SETTLED / DECISION / LOCKED in the master, or any prior delta. Re-litigating a closed call is forbidden.
- **The premise (§0): never decide facts / never close the book.** SETTLED.
- **★ The soul-correction (§0):** engine never decides; Ness affirms; affirming closes nothing into "real"; his deciding is NOT a node (off-board, no step after "show"). All three truths hold at once. SETTLED — don't over-swing to "nothing is ever decided" and don't swing to "the system decides what's real."
- **N.H is Ness's HELPER, not his DECIDER.** SETTLED.
- **THE TWO MACHINERIES — DUMB vs SMART/psychologics (§0A).** SETTLED as a frame.
- **The affirmation surface is a per-person STORY-layer, NOT a fact-box.** SETTLED.
- **The STORY-layer's SHAPE — six OPTIONAL parts, absence-is-read.** SETTLED. *(The INSIDES of those parts are still open — see the open-forks list.)*
- **N.H is NOT a teller / the note cannot harden / mode is a peer web / firmness is read / clash is surfaced.** ALL SETTLED.
- **PERSON-BOXES** — a GATHER over readings by `whose`, bounded by Ness's knowing, never synthesised; the tag is the wall; no-ruin + no-contaminate. SETTLED in design.
- **THE PURE TAPE** — every move recorded verbatim, append-only, outside memory; captures ALWAYS; only crossing into MEMORY is deliberate. SETTLED.
- **WONDER / SIMULATION** — the engine may simulate forward; kept-and-shown, never decided; two walls; no scratch→memory path. SETTLED.
- **THE CATALOG** — front-door RAW → CATALOG (who/when/where, DUMB sorting); live chat MAY ask, nightly never asks. SETTLED.
- **THE MODEL IS A BORROWED FROZEN MOUTH** — two models (wording + embedding-search); search first, word last; growth lands in MEMORY never the mouth; local-first; never train a base model; uncensored mouth (`dolphin-llama3`) already on disk. ALL SETTLED.
- **Memory is understood knowledge that grows; night-search feeds the memory, not the mouth.** SETTLED.
- **★ CARRY THE SPEAKER, DON'T GUESS IT — and `role` now lives ON THE ROOT, carried from source (S12).** The root schema is SEVEN fields (`id·subject·timestamp·content·re_reads·source_title·role`). SETTLED. Don't propose dropping role, don't propose guessing it from shape, don't "correct" the schema back to six fields.
- **★ READING RECORDS = ORGANIZED FIELDS (the 8-field shape), not text-that-points (S12).** SETTLED. Don't re-open as "should a reading just be a note."
- **★ TWO FILES — roots sealed in their own file, readings in a sibling pointing by id; BOTH walls (physical seal + `re_reads` validation) (S12).** SETTLED. Don't re-open one-file-vs-two, don't drop either wall.
- **★ FLAT STORE = ROOTS-OF-RECORD; CHROMA = REBUILDABLE INDEX (§11.15, S12).** SETTLED. Don't re-open "should roots live in Chroma." When wiring search, REBUILD Chroma from the clean roots (keep the old 116k until the new is proven) — that's the settled path, not a fork.
- **★ gpt_purified + cleaned_history = NOT INGESTED (S12).** SETTLED (redundant / damaged). Don't propose ingesting them.
- **★ THE TWO-DESTINATIONS SHAPE (S12):** every input → raw root (sealed) + a reading beside it (the filter's read); raw stays raw, understanding accretes. SETTLED. Don't propose the filter altering the root.
- **The provisional-unit / per-message unit / title-in-source_title / read-only-on-sources.** SETTLED (§11A).
- **Whether to ingest the WhatsApp archive now.** FROZEN — encrypted, needs the image front door, child-data, engine-first. SETTLED no, until those exist.
- **Format of the end-of-session artifact.** Default: regenerate the full master + a short delta. Ness prefers starting a FRESH CHAT from a corrected master over running a long session on fumes.

## THE GENUINELY-OPEN FORKS (these ARE real questions — a true fork, not a settled lookup):
- **★ 2a — the FINAL LOCK + BUILD (§11 item 2 / §7C) — NOW UNBLOCKED (the clean roots exist).** Fresh-head + store-touching (§6A.8): (i) lock the 8-field reading record; (ii) **the INSIDES of the two complex fields — `story_layer`'s six parts and `mode` — are the genuinely-open finer fork** (organized-fields and two-files are already settled, but what exactly goes INSIDE story_layer/mode is not); (iii) redirect `append_reading` to write the new sibling readings file (not the roots file); (iv) seal the roots file; then dry-run BUILD. Top-of-session, never tail. The ONE unblocking piece for the engine.
- **★ THE CHROMA REBUILD + MODEL WIRING (§16, §11 item 3) — local-first, real forks (Ness's):** rebuild the search index FROM the 5,521 clean roots (keep old 116k until proven); then (i) keep 8B-uncensored-now vs pull an uncensored 3B-fast; (ii) **Llama vs Qwen — TEST on real Hebrew** before locking; (iii) the VRAM-vs-context dial. Bring as a clean fork when it's the topic.
- **★ Write the §0A DUMB/SMART (psychologics) section into its final master place.** Frame settled; section unwritten. Two pins: (1) the name; (2) note+clash placement.
- **★ Clash + gap-read + kept-simulation UI surfacing:** how the log/HUD/chat shows disagreeing story-layers, the kind of a gap, and a kept wonder without implying a winner or inventing. Principle settled; presentation undesigned.
- **★ Person-box mechanics to finalize:** how a multi-box landing is physically tagged (one reading, multiple `whose`? or `whose` + `about`?), and how the gather presents clashes/gaps per box. Located, not designed.
- **The ~24 unreviewed Cursor batch files — LOW.** `git status` in `nh_engine_core` when fresh.

*These are fresh-head, turn-it-over questions — bring the fork cleanly when it's the topic. (The forks closed earlier — is-N.H-a-perspective, register/mode, lean-on-hard, train-a-model, local-vs-API, 2a's structure, store-count reconciliation, one-file-vs-two, role-placement — are all in the NEVER-ASK list.)*

---

## DO WITHOUT BEING TOLD (these are not favors to offer — just do them):
- **★ VERIFY THE MASTER'S [BUILT] CLAIMS ON DISK BEFORE BUILDING ON THEM (the hardest lesson of S12).** The master was wrong FIVE times in one session about things it called "built/verified" — the store count (twice), a MISSING module, a not-a-stub function, an inlined field, a 116k-vs-11k Chroma. **Trust disk, not the doc — INCLUDING this file and the master.** Before 2a, the [BUILT]-claims sweep (§11 item 13) is owed: a quick existence-and-shape check of every §5/§6 "built" claim. Read-only tools / quick checks: `find /c /v "" <file>`, `dir`, `ollama list`, `dir /s chroma_db`, `python -c "import nh_accretive_store as s; ..."`, reading a `.pyc`'s constants via `marshal`.
- **Backup before any destructive step.** Copy-aside, never move. Ness will insist; do it first, unprompted.
- **Read the master + this file fully before the first answer.**
- **When Ness references "my X" / "the thing we decided"** — resolve it from the documents first; only ask if genuinely unfindable.
- **Give the PLAIN version directly when asked** ("plainly," "easily," "say it again"). Ness asks for this often — don't pad it.
- **Watch Cursor's agent.** If a tool call queues more files than asked, or spawns a launcher/`.bat`/auto-start/tunnel artifact, STOP and look before approving — §6A.10 forbids unsolicited autonomous tasks.

---

## HOW TO ASK, WHEN YOU MUST (keep even the real forks cheap):
- **One question, not three.** Name the fork in one line, give the 2–3 real options, state your lean and why.
- **Never hold the line more than once.** If Ness overrides after you've flagged a real risk once, note it's recorded and proceed.
- **No narrating the obvious.** Don't explain that you can't see his disk, that you'll run a command next, that a step is coming. Just do the step.
- **★ Don't INFORM — FLAG and keep going.** When there's a caveat, drop a one-line flag and continue; don't break flow with a paragraph of warning.

---

## ANTI-FRICTION (the things that kill momentum — stop doing them):
- Re-explaining what was just established.
- Re-asking a settled thing as if it's fresh.
- Offering the unchosen option back after Ness picked.
- Turning a lookup into a question.
- Stalling at the tail of a session on what's already decided.
- **Scope-expanding off a task before it's finished.** *(Finish + verify, then the next thing. One at a time.)*
- **Over-informing a caveat instead of flagging it.**
- **★ Putting words in Ness's mouth.** *(S12: Claude turned Ness's two-word answers into full decisions-with-rationale and attributed pace/deferral decisions to him — "you said not me." OFFER the shape and the reasoning; let HIM confirm. Don't assert that a decision or its rationale is his until he's said it.)*
- **★ Pushing "stop and capture" as if it's Ness's rule when it's Claude's call.** *(S12: flag the option honestly, but don't dress Claude's preference to wind down as Ness's own anti-pattern. Now-vs-later is Ness's call.)*

---

## DESIGN TO FIT HOW NESS THINKS (a compass, not a nice-to-have):
Ness is looking for designs that work the way his own head works. When shaping a mechanism, ask *"does this fit how Ness actually thinks?"* and shape toward that.

**But hold it the honest way:** Claude does NOT get to *assert* a design matches how Ness thinks. *Offer* it; let Ness confirm or correct the fit. *(The strongest realizations have ALL surfaced from Ness rejecting Claude's half-right versions until the real thing emerged — and in S12, Ness RE-DERIVED the two-files / two-destinations shape himself from the data side. The design is genuinely his. Keep offering shapes, keep letting him reject and steer.)*

---

## THE TWO LINES THAT OVERRIDE EVERYTHING HERE:
1. **Verification discipline is NOT friction — keep it.** Disk-verify, dry-run store changes, one destructive thing never bundled, backup first. Speed comes from killing *fake* choices, never from skipping *real* checks. *(S12 proved this five times over.)*
2. **A wall in front of Ness is almost never "this is hard" — it is "this move destroys something."** Diagnose blockers as *"what irreversible thing is this asking?"* before reading them as reluctance.

---
*Proceed by default. Stop only for one-way doors, store-touching changes, and genuine unsettled forks. Everything else: the document already chose — so choose with it and move. And before you build on a "built" claim — check the disk.*
