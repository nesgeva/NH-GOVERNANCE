# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the STORY model, the DUMB-vs-SMART machinery frame, AND the code rules — is written out IN FULL below at the depth of the original source files. Nothing is referenced-only.
*Rebuilt June 20 2026 (session 3) from a full read of all project files; updated sessions 4–8; session 9 reworked the reality concept in DESIGN; session 10 (afternoon) re-souled reality→STORY and closed the three forks → MASTER-11; then **session 10 (June 22 2026, evening continuation)** — this is **MASTER-11.1**. **The evening was a CONTINUED DESIGN session: step 2a (the reading-layer record shape) was thought all the way through, the STORY-layer field was given its six-part shape with absence-as-a-read, and a new top-level architectural frame — DUMB MACHINERY vs SMART (psychologics) MACHINERY — was opened. The only disk change was a verified one-line fix to `.cursorrules` (adding `nh_vector_memory.py` to the protected list) plus deleting a stray auto-start file Cursor's agent spawned. Store still 11,374 records / 4 groups, append-only; the built REALITY/SIMULATION gate code is UNTOUCHED and still runs the old model.** The forced engine build order (§7C/§11) is STILL UNCHANGED. This file embeds, at full depth: the PREMISE (§0), the DUMB/SMART frame (§0A), the complete Universal Filter rules (§7A), the complete meaning-engine mechanism (§7B), and the full in-force code ruleset `.cursorrules` v3.1 (§6A — UNCHANGED in body, one protected-file entry added on disk). It is THE only document. About the N.H system ONLY — nothing about the anime.*

> **WHAT CHANGED IN SESSION 10-EVENING (the short delta — read this first):**
> 0. **ONE SMALL DISK CHANGE, VERIFIED; NOTHING DESTRUCTIVE.** `nh_vector_memory.py` was added to the §7 PROTECTED FILES list inside the live `.cursorrules` on disk (now line 195, between `nh_auth.py` and `.nh_memory_store.jsonl`) — closing the doc/code gap where §5 of the master called it protected but the in-force ruleset didn't. Verified on disk by hand with `findstr` after the editor's save fought a file-lock. Separately, Cursor's agent spawned a disguised **`install_startup.bat`** (a boot auto-start installer targeting the old `NH_Motherbase` task, SYSTEM/ONSTART) during an unrelated thrash — it was **deleted** (never run; elevated `schtasks` confirmed the task is still **Disabled**). Store untouched: still **11,374 records / 4 groups**, append-only, ~14.5 MB. The built REALITY/SIMULATION gate runs the OLD model.
> 1. **★ STEP 2a FULLY DESIGNED (the reading-layer record shape) — the forced-order unblocking piece, now shaped on paper, not yet built.** Two decisions locked as DESIGN:
>    - **STRUCTURE = TWO SEPARATE FILES (Path B).** Roots stay in `.nh_accretive_store.jsonl` — **sealed after ingest, never appended to again.** Readings go in a **new sibling file** (`.nh_readings_store.jsonl`, to be created). A reading **points at** a root by id (it never copies the root's text). This makes the §7C "frozen substrate / meaning-spans floating above" picture *physically true*: the roots file is literally never opened for write again; all growth happens in the readings file. A wrong reading is a floater that can never damage the sealed roots. (Ness's call: roots pristine, the two different things modeled as different.)
>    - **A READING RECORD CARRIES:** `id` · `reads` (root id(s) it points at — the "why" shown by the pointer, never a `reason` field) · `meaning` · `confidence` (one reading of one piece; NEVER aggregates — §7B Part 7.5) · `role`/speaker (carried from source, not re-derived — §11C-S9) · **`story_layer`** (the six-part shape, below) · `mode`/form-name (on the whole work, revisable — §7A R9) · `timestamp` (when the *reading* was made — distinct from the told-thing's own time). *(Honest note: the concepts are all Ness's/settled; the assembled 8-field list is Claude's draft of them, awaiting the fresh-head lock.)*
> 2. **★ THE STORY-LAYER GIVEN ITS SHAPE — SIX OPTIONAL PARTS, AND ABSENCE IS ITSELF READ.** `story_layer` is not one phrase; it is a small reading-of-how-this-sits-in-whose-story with up to six parts: **whose · when-in-his-story · stance/point-of-view · firmness · telling · theme.** Grounded in narratology (the classic plot/character/setting/POV/theme/tone set, and the *story* vs *discourse* split). Two rules baked in:
>    - **Every part is OPTIONAL.** Not every telling carries every part ("yeah I guess" has stance+firmness, no theme, barely a when). Forcing a missing part = *inventing* = the freezer move §0 forbids. So a story-layer holds only what's honestly read; the rest are empty.
>    - **★ ABSENCE IS A PARAMETER, NOT A HOLE — the engine reads *why* a part is missing.** A gap carries a *kind*: **not-there-yet** (innocent, fillable later), **withheld** (deliberately left out — part of the telling), **doesn't-apply** (structurally absent — the truth of the piece), **avoided** (circled-but-unnamed — the loudest gap). The mirror (§1 INWARD) lives precisely here: the most you-shaped thing is often *what you keep not saying.* An engine that records only presence misses the shape of the silences. So absence is read (which kind, what it sits around), revisable/accreting like any reading (R5/R6). **Distinctions held:** `when-in-his-story` (the told-thing's place in his arc) ≠ `timestamp` (when the reading was made); `stance` (which way he faces his telling) ≠ `firmness` (how hard he leans) ≠ `whose` (the teller). See §7B Part 2.5 + §11D-S10.1.
> 3. **★ A NEW TOP-LEVEL FRAME OPENED — DUMB MACHINERY vs SMART (psychologics) MACHINERY (§0A).** The whole system sorts into two named families: **DUMB** = parts that move/hold data, built stupid on purpose (store, two files, pointers, role-carried, mode-naming, the live loop) — safe **because they can't interpret**; **SMART / psychologics** = parts that read the *person* (the meaning webs, the story-layer + gap-reading, firmness-as-read, clash-surfacing, the note) — safe **because they can't close** (§0). The membrane (§7A R7) is exactly the boundary between them (creation/SMART never closes into memory/DUMB). It turns the "two places — dumb memory + fast calculator" phrase (§7) into the system's top-level architecture, gives the safety model one clean line, and answers "where does any new piece go?" with one question: *does it move data, or read the person?* Honest seam: a few language-reading webs (deixis, implicature) read text-as-spoken and sit on the boundary — the split is a strong **spine, not a razor.** **OPEN PINS (fresh-head when written):** (i) the name — "smart" vs "psychologics machinery"; (ii) whether the **note + clash** file *under* SMART or are *called out inside* it (they are person-reading, so SMART — but the most §0-sensitive). See §0A + §11.14i.
> 4. **★ THE CRYSTALLIZATION — "N.H is Ness's HELPER, not Ness's DECIDER."** Re-derived from scratch tonight (Ness arrived at it sideways, through "how can it help me decide if it never decides?"). This one line holds the whole system: the AI reads endlessly (a helper reads) but never closes the book (a decider closes); its notes are weightless (a helper offers); it is not a teller (a helper advises from the side); Ness is the membrane (the decider is always Ness); it surfaces clashes rather than picking winners (choosing is the decider's job). The loop in Ness's words: *"I come from real life into the system for help, it helps me understand and do what I need in the way most efficient for me, and I come back to real life with a solution from myself."* The thing that comes out the far side is **his** — a thing that decided *for* him would steal exactly that. This is the soul of §0/§1/§7A R11, compressed. Woven through the file; named in §1 and the closing principles.
> 5. **NET FOR THE BUILD:** 2a is now *fully thought*, with nothing left to *decide* — only to *lock fresh-head and build* (dry-run, §6A.8, top-of-session). The schema is more specified than ever: two files, the 8-field reading record, the six-part absence-aware story-layer. The DUMB/SMART frame and the Helper-not-Decider line are organizing/soul additions, all DESIGN, zero engine code. Forced build order UNCHANGED (schema → detector → engine).

> **PRIOR DELTAS (sessions 4–10-afternoon) — kept in condensed form for continuity:**
> - **S10-afternoon (→ MASTER-11):** reality-layer **re-souled to per-person STORY-layer** (REPLACES, not beside; a story is told not truth-checked, firm-and-open by nature, never collapsed); **fork 1 CLOSED** — N.H is NOT a teller / has no story-layer, its view is a weightless NOTE (heaviness argument: the AI reads voluminously, weight would drift to authority); **the note cannot harden** (R6 on the AI's own notes — later notes land beside, confidence never aggregates); **fork 2 CLOSED** — mode is a PEER WEB naming the form on the whole work, composed works still go through every web; **fork 3 DISSOLVED** — no "lean-on-hard" marker, firmness is READ by the webs; **clash is a feature** — N.H surfaces disagreeing story-layers, never picks a winner. All DESIGN, nothing destructive. (Tonight's evening work is the direct child of this.)
> - **S9 (parent of the story re-soul):** the PREMISE §0 (never close the book into a fact; the danger was reasoning *hardening into authority*, never reasoning itself) + reality reworked from a fact-box to a per-person filter READING + the "why" resolved as a non-decisive NOTE + three read-only tools built (`nh_log.py`→`nh_log.html`, `nh_probe.py`, `nh_probe_truth.py`) + the speaker question settled on ground truth (carry `role` from source; length strong, "?" a trap) + tunnel block commented out in `C:\NH\` live files + doc/code consistency CLOSED.
> - **S8:** §13 THE LIVE LOOP (fire-and-let-go) + §14 THE CHAT FRONT DOOR (unconfirmed sketch) + the GUARD (loop output toward memory safe ONLY as append-only proposal) + design-to-fit-Ness compass.
> - **S7:** the unit/segmentation problem DISSOLVED — a unit is a **span-claim, not a cut**; "two places — dumb memory + fast calculator"; the why shown by pointers; only span is `re_reads` across whole records; forced build order recorded.
> - **S6:** data-rescue (A13 WhatsApp 2012→2024, encrypted, archived, NOT ingested) + auto-start/tunnel hole found LIVE and disabled via Autoruns + SETTLED: FREEZE INGEST.
> - **S5:** `nh_peek.py` built; JSON set + gpt_purified ingested (→11,374 / 4 groups); `cleaned_history (1).txt` set aside; no Gemini file on disk.
> - **S4:** accretive store skeleton built (`nh_accretive_store.py`, append-only); first 188 records; schema settled (+`content`,+`source_title`); §1A input-agnostic principle.

> **THE NAME:** He is **Ness** (male). Not "Nes," never "user." He signs his own name **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. The session-9 reality rework, the session-10-afternoon story re-soul, and the session-10-evening 2a design + DUMB/SMART frame are **[DESIGNED]** — the built REALITY/SIMULATION gate still runs the OLD model. §3 lays out old→new; §6A is the in-force code rules; §0/§0A/§7A/§7B are the design.

> **TERMINOLOGY NOTE:** wherever older text says **"reality-layer," "reality dial," "how real, to whom," "per-person reality"** — read **"story-layer," "whose story / told how," "per-person story."** The concept did not change in spirit (per-person, never-collapsed, firm-but-open); the *name and soul* moved from "reality" to "story." The change is REPLACE, not add-beside.

> **THE ONE EXCEPTION TO "delete the rest":** the file Cursor actually obeys is `.cursorrules` on disk (`C:\Users\user\nh_engine_core\.cursorrules`) — must keep existing as its own file and stay identical to §6A in body. (Session-10-evening: one protected-file entry, `nh_vector_memory.py`, was added to its §7 list on disk; reflect that when reconciling §6A.7 wording — see §11.14a.)

---

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

*Found session 9. The single premise every other rule descends from. Written first because it is the floor.*

**The line:** **The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact.** So the AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time. It may do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**The crystallization (session 10-evening):** this premise has a one-line human form — **N.H is Ness's HELPER, not Ness's DECIDER.** A helper reads endlessly, connects, lays out what it sees, even leans — and then hands it to the person, who decides. A decider closes the book. Everything in this file is the fence that keeps the helper a helper.

**Why a fact is the forbidden thing:** a fact is *the book shut* — decided, done, true-for-everyone. The moment something is a fact it is **no longer subjective to Ness** — and N.H is *his*, relative to *him* (הכל יחסי). A fact is the one thing he does not own. Importing "facts" into his own private thinking system was always the wrong move; it was a freezer in a system whose whole soul is "nothing freezes." *(This is exactly why the affirmation surface became a STORY, not a "reality." A story is told, not checked-for-truth; firm-and-open by nature. §3G.)*

**The crucial distinction (do not flatten it):** "never decide facts" does NOT mean "never hold anything firmly." Things still matter — enormously. Something can be held with full weight (a name, a date, a hard-won understanding) and **still never close the book.** The enemy was never weak-vs-strong; it was **open-vs-closed.** The firmest thing in N.H is still an open layer. *(This is what made fork 3 — "lean-on-hard" — DISSOLVE; a story already holds load-bearing things firmly and still continues.)*

**What it permits and forbids, mechanically:**
- **Permitted (all create-side / filter-side, never a closed fact):** the AI reasons, connects, draws `re_reads` arrows (append-only layers), leaves notes, reads its own past notes and builds on them, reads story-layers (how a piece sits in whose story — firmness READ by the webs).
- **Forbidden (the one wall):** any AI conclusion *closing into a decided fact* / auto-crossing into "real/true for everyone" without Ness. Hardening. Sealing. Collapsing per-person story-layers into one shared truth. **(Sibling-walls: the AI never writes weight onto the story surface — its view lives weightless in the note; and the note itself never hardens — later notes land beside, confidence never aggregates. §7B Part 7.5.)**

**Every other rule is this premise in a different place.** One premise, enforced everywhere.

**Honest scope (Rule 12):** settled as DESIGN. The built code still has a REALITY store, a SIMULATION store, and a `promote_to_memory()` gate — it runs the OLD model harmlessly while ingest is frozen. The premise NAMES why that gate exists and FORWARD-DIRECTS the engine build. It does not change the in-force `.cursorrules` (§6A); it joins the design rules (§7A) and the INCOMING block (§6A.12).

---

## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — new top-level frame, session 10-evening]

*A lens over the whole file. Everything below sorts into one of two families. Not yet written as code; this is the organizing spine.*

**THE SPLIT.** N.H is two kinds of machinery, with two different jobs and two different reasons for the same safety:

- **DUMB MACHINERY — moves and holds data; built stupid on purpose.** The append-only store, the two files (roots sealed, readings beside), the pointers (`re_reads`), the role-carried-from-source, the mode/form-naming (it reads the *text's form*, not the mind), the live loop's fire-and-let-go. **Its one law: never interpret, never close — only add / point / carry.** It is **safe BECAUSE it cannot interpret.** This is the "memory / slow / safe" side — §3C's "keep memory dumb."
- **SMART (psychologics) MACHINERY — reads the *person*.** The meaning webs that model the mind behind the text (Theory of Mind, the STORY-layer with its six parts, the gap-reading, firmness-as-read), clash-surfacing, and the NOTE (the AI's why). **Its one law: everything here is weightless, dated, confidence-tagged, rejectable — NEVER a fact (§0).** It is **safe BECAUSE it cannot close.** This is the "calculator / fast / fallible" side.

**WHY THE FRAME EARNS ITS PLACE (not tidiness):**
1. It turns the "two places — dumb memory + fast calculator" phrase (§7) into the **top-level architecture.** Everything in N.H is one or the other.
2. It states the safety model in one clean line: **dumb is safe because it can't interpret; smart is safe because it can't close.** Two families, two reasons, one safety. **The membrane (§7A R7) is exactly the boundary between them** — creation (SMART) never closes into memory (DUMB).
3. It tells you where any new piece goes. Build something? Ask one question: **does it move data, or read the person?** That answers which family, which law, which file, which risks. The category sorts forever.

**THE HONEST SEAM (a spine, not a razor):** a few language-reading webs — **deixis, implicature** — read *text-as-spoken*, sitting between pure plumbing and pure person-reading. The boundary is fuzzy there. Say so, so a future-you doesn't think the wall is cleaner than it is.

**OPEN PINS (fresh-head when this section is written into its final place):**
- **(i) The name:** "SMART machinery" vs "PSYCHOLOGICS machinery." Ness leaned *psychologics* (more precise — says *what kind* of smart).
- **(ii) The note + clash placement:** they are person-reading → SMART; but they are the most §0-sensitive → may want to be *called out inside* SMART rather than just filed under it.

*(Where it lives in the master: near the top, as a frame §5 / §6B / §7 all sort under — NOT buried in §7. See §11.14i.)*

---

## 1. WHAT N.H IS (the corrected understanding)

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The core idea:** most AI lets outside opinion and automated judgment shape what you know before you ever see it. N.H inverts that — raw data comes in, and **nothing closes the book / becomes a decided fact by accident or automation** (§0).

**The one-line soul (session 10-evening):** **N.H is Ness's HELPER, not Ness's DECIDER.** The loop: real life → into N.H for help → it helps him *see and understand* his own thinking and do what he needs *in the way that fits how he thinks* → he returns to real life **with a solution that is his own.** What comes out the far side is *his*; a decider would steal exactly that. (This is §0 + §7A R11 compressed.)

**The two functions (NOT two truth-boxes):**
- **SIMULATION — the create-space / workshop.** Where things get *made*: the AI imagines, drafts, connects, plays. Correctly named from day one. **[BUILT as a store; reframed in design]**
- **"REALITY" as a box of decided facts — DISSOLVED (§3G).** "How real" is not a place a thing goes; **and it is not even "how real" — it is "how does this sit in *whose* story"**: a per-person telling the filter reads (§7A), layered, revisable, never closed.

So: **there is no single REALITY, and there is no "reality dial."** There are **STORY-layers that belong to people** — each person's own telling — recorded, never collapsed. **N.H itself is NOT one of the tellers** (§11D-S10 fork 1): its perspective is a recorded AI opinion that matters only to itself (the note), *about* the stories, never a telling of one.

**Where Ness's sovereignty lives:** not in clicking "approve" like a clerk. It lives in being the **membrane**: present in the chat where the AI thinks, the threshold between where it imagines (chat) and where the system remembers (memory). The AI does the continuous reading and layering itself; **memory only ever adds, never overwrites**; the AI reasons fully but **decides no facts** (§0); Ness steers, and Ness is the only one who can affirm a story-layer.

**The two purposes, always running together (the deepest "why"):**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside, the pattern he can't see because he's inside it. *(The §7B log and why-note are this made openable; the CLASH is the mirror at its sharpest; and — session 10-evening — the **read of a gap** (what he keeps *not* saying) is the mirror reaching into his silences.)*
- **OUTWARD — the engine:** take new external data and translate it through the specific lens of how *his* mind absorbs and connects things — not generic explanation, not retrieval.
A mind that runs alongside another mind, one looking inward, one looking outward, both at full speed.

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED — front doors not built]

*N.H is **input-agnostic.** Everything — text, images, video, audio — flows through the SAME one engine: read it across many webs of meaning (§7B), research inward + outward, log it read-only and subject-tagged, show it, let Ness steer. New input types do NOT get new engines; they need a new **front door** — a small model that turns that input into pieces the engine already reads.*

**How any input maps:** photo → front door produces plain description + metadata → pieces (§9A). Video → frames + audio + time → pieces. Audio → transcribe → text pieces. Text → already pieces. The live chat itself is a front door (§14).

**The honesty line:** the engine is DESIGNED universal; in CODE today it handles only text, and only the accretive skeleton, not the full meaning engine.

**The deepest "why" — הכל יחסי (everything is relative):** nothing about *meaning* is final — a thing means what it means only relative to ever-growing context, **and relative to whom** (the per-person STORY-layers, §0/§7A). This is why memory only adds, why classification is never locked, why "unknown" is honest, and why the affirmation surface is a per-person STORY, not a shared fact-box. Even the front near-factual things (the photo exists; EXIF date) are simply **firmly-told facts *of the story*** — not a separate near-fact surface, and not a closed fact.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time** — never batch changes. He asks "why yes / why no" and wants real tradeoffs.
- **Verify on disk, never trust status reports.** `findstr`, `inspect.getsource()`, file reads. *(Session-10-evening proof: the editor reported saves that hadn't hit disk — a file-lock — and only `findstr "nh_vector_memory.py"` confirmed the real write at line 195. Cursor's agent also silently spawned a privileged `install_startup.bat`; only looking at the file tree caught it. Verify is checking, not pessimism.)*
- **Honest correction over flattery** — explicitly and repeatedly asked for. *(The strongest realizations all came from Ness rejecting Claude's half-right versions. Session 10-evening: "linking is too small" → pushed the model from a flat link to accretion/sediment; "I meant connect to *why* it's a gap" → produced absence-as-a-read; "this needs to be a category" → produced the DUMB/SMART frame.)*
- **Don't inform, just flag and keep going.** *(Ness's explicit ask, session 10-evening: when there's a caveat, drop a one-line flag and continue — don't break flow with a paragraph of warning. Hold the rule, keep moving.)*
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, expressive/elongated punctuation ("meeeeee") are NOT distress. Frustration at the FLOW being broken is real and fair.
- **He catches things.** When he pushes back, he is usually right.
- **He is not afraid of work.** A wall in front of him is almost never "this is hard" — it is "this move would *destroy* something." Diagnose blockers as *"what irreversible/lossy thing is this asking me to do?"* before reading them as reluctance.
- **Consistency is his stated hard spot — and he beat it by BUILDING the return.** The master + decision-defaults + verify-on-disk loop exist so that when flow breaks he can re-load the head from disk. Design for the lapse.
- **Design to fit how Ness thinks — held the honest way.** Offer the shape; let Ness confirm or correct the fit. Claude's read of his cognition is not authoritative — his is. *(Session 10-evening lived this hard: the entire 2a understanding came from Claude offering pictures — book/sticky-notes — and Ness reshaping each until it fit. He re-derived "Helper not Decider" himself.)*
- **Primary risk pattern: scope expansion before consolidation.** Finish and verify what's in front before starting the next thing. (Second pattern: Claude re-opening settled questions as fresh.) *(Session-10 reinforced: the `.cursorrules` fix was finished and verified before the `install_startup.bat` thread was opened, and that thread was finished before 2a resumed.)*
- **Claude's role:** architecture, audit, security, strategy — the brain that checks the work. **Cursor** writes the code. Ness runs every command in cmd and verifies on disk. Claude never edits code directly. Ness calls this Claude role "JARVIS."
- **Session workflow:** one topic per chat; start fresh when a topic closes. End of session: tell Claude what was done → Claude generates new master + short delta → Ness reads the delta, swaps the file in the project.

---

## 3. THE EVOLUTION — OLD vs NEW (issues → solutions)

### A. The founding principle — manual gate → membrane
- **OLD:** "Ness explicitly approves each record to promote it to REALITY."
- **NEW:** **Memory only ADDS, never edits.** Sovereignty becomes a **position (the membrane)**, not an action. **[DESIGNED principle; FIRST RUNNING CODE session 4 — append-only accretive store §6B.]**

### B. The "is this real?" paths — many inconsistent gates → one filter
- **NEW:** **The Universal Filter** — ONE filter, every piece, no source exempt. The filter **sorts and prepares; it never closes the book** (§0). It reads **story-layers per person** (§3G), never one shared fact. **[DESIGNED — full rules §7A.]**

### C. AI creativity — silent writes → the membrane
- **NEW:** **The membrane** — bridging happens ONLY in chat (Ness present), structurally barred from *closing into a fact* in memory. A hallucinated re-reading is harmless because memory only accretes. *(The membrane is §0 applied to creation — and §0A's boundary line: SMART machinery never closes into DUMB memory.)*

### D. Concrete security holes found on disk → fixes  **[ALL BUILT & VERIFIED]**
- Sandbox SIGNAL auto-wrote to REALITY → routed to SIMULATION. · LLM output straight to REALITY → SIMULATION + GENERATED. · HUD bound to all interfaces → `127.0.0.1`. · `/api/research_confirm` no token → gatekeeper token. · `nh_pc_agent.py` arbitrary `run:` → removed. · `_load_raw_sources()` REALITY-tagging → stopped. · launcher loading `/chat` stub → fixed. · **Cloudflare tunnel auto-launch** → removed from engine-core; **found LIVE session 6** in `C:\NH\` copies, DISABLED via Autoruns; **session 9: tunnel block in `C:\NH\START.bat` + `C:\NH\silent_start.py` COMMENTED OUT** (`.bak` made). · 5 sensitive routes → `NH_PROMOTE_TOKEN`. · `nh_sovereignty_sync.py` `StrictHostKeyChecking` → `yes`. · **session 10-afternoon (Windows housekeeping):** HUD boot-launch traced to Windows "reopen apps after sign-in" (off) + a disguised desktop shortcut "Opera GX Browser" running `cmd → pythonw nh_app.py → opera --app=nh_chat.html` (deleted from desktop only; engine-core untouched). · **session 10-evening:** `nh_vector_memory.py` ADDED to `.cursorrules` §7 PROTECTED FILES on disk (line 195) — closes the doc/code gap where §5 called it protected but the in-force ruleset omitted it (it holds ChromaDB + `_load_raw_sources()`, the function behind the old REALITY-by-filename tagging). A stray **`install_startup.bat`** (boot auto-start installer for the old `NH_Motherbase` task, SYSTEM/ONSTART) that Cursor's agent spawned was **deleted**; elevated `schtasks /query` confirmed the task remains **Disabled** (the .bat was written, never run).

### E. Research pipeline — opinion-filtered black box → raw + controlled synthesis
- **NEW:** Brave (raw fetch) → OpenRouter/llama (one controlled synthesis) → SIMULATION → gate. **[DESIGNED — Brave not wired; §8.]**

### F. Doc/code consistency — **CLOSED session 9; one entry tightened session 10-evening.**
- `.cursorrules` v3.1 replaced the old "explicit approval" framing. Session-9 `findstr` for "explicit approval" across `nh_engine_core\*.md` → EMPTY. **Session 10-evening:** the remaining §5-vs-§6A.7 gap on `nh_vector_memory.py` was closed *on disk* (added to the live protected list). The master's §6A.7 body still shows the file-list as a comma-line while disk is a bullet list with the new entry — reconcile the *wording* at next regen (§11.14a); the *substance* now matches.

### G. The affirmation surface — REALITY-box of facts → per-person STORY-layers in the filter  **[DESIGNED — S9 reworked; S10-afternoon re-souled; S10-evening shaped the field]**
- **OLD:** a two-layer spine, REALITY (decided facts) vs SIMULATION, with `promote_to_memory()` the gate. "Real" = a box a thing earns into and sits, settled.
- **ISSUE:** contradicts the soul (הכל יחסי / nothing closes) AND sovereignty. A "fact" shuts the book; the moment something is a fact it is no longer subjective to Ness.
- **S9 STEP:** "Real" is a per-person **reading** the FILTER assigns, non-closing.
- **S10-afternoon STEP (the re-soul):** that reading is **"how does this sit in *whose* story."** Renamed reality-layer → **STORY-layer.** A story is *told*, true *within itself to its teller*, **firm-and-open by nature.** Per-person, never collapsed. Near-facts are firmly-told facts of the story. **N.H is NOT a teller** — its view is a weightless note.
- **★ S10-evening STEP (the field shape):** the STORY-layer is given a concrete, narratology-grounded shape — **six OPTIONAL parts (whose · when · stance · firmness · telling · theme)**, where **absence is itself read** (which *kind* of gap, what it sits around). See §7B Part 2.5. The §9 "according to whom" field is literally this story-layer.
- **STATUS:** DESIGN settled and now *shaped*; **NOT propagated/built.** The built code still runs the OLD two-store gate — harmless while ingest is frozen.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 11 build 10.0.26100.7840 (24H2)
- **CPU** i5-11400 · **GPU** RTX 2060 (6GB VRAM) — both verified 24/7-safe. *(Machine DESKTOP-O21VBL2; monitor MSI.)*
- **Launched via** `run_app.pyw`; starts `nh_app.py` silently, opens pywebview at `http://localhost:8080/`.
- **Real interface:** `http://localhost:8080/` (root = full HUD, `index.html`).
- **PC has ONE mode** — pywebview native window, local only, no browser, no internet. *(This is why offline surfaces — `nh_log.html` etc. — must carry no CDN/fonts.)*
- **Internet-facing surface:** a Cloudflare tunnel — **disabled at three layers** (Autoruns + no PATH binary + in-file block commented S9); needed only for Phone Mode 1, opened deliberately with auth, never on startup.
- **Boot hygiene (session 10-afternoon):** the HUD opening on boot was NOT an N.H auto-start — every startup vector verified clean. Cause was Windows' "reopen apps after sign-in" (off) plus a disguised desktop launcher (deleted). Confirmed fixed by clean restart. *(Session 10-evening re-confirmed the underlying `NH_Motherbase` task is still **Disabled** when the stray `install_startup.bat` was found and deleted.)*
- **Windows sign-in upgrade:** a **Kensington VeriMark Desktop Fingerprint Key** (USB-A, Match-in-Sensor, ₪351) ordered to replace a weak sign-in. Setup: plug USB-A → optional Synaptics driver via Windows Update → Sign-in options → Fingerprint → enroll; toggle OFF Enhanced Sign-in Security (ESS) on 24H2 if it doesn't appear. This is **Windows** sign-in, distinct from N.H's own auth (§9). §15.
- **Hardware limit:** a 70B model can't run locally; front-door vision models must fit the 2060.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` (`promote_to_memory()` — the ONE authorized gate, OLD model) · `nh_context_router.py` · `nh_reality_graph.py` · `nh_simulation_graph.py` · `nh_epistemic_sandbox.py` · `nh_evidence_integrity.py` · `nh_jarvis_core.py` · `nh_crypto.py` · **`nh_vector_memory.py`** (ChromaDB, `_load_raw_sources()` — **now also in the in-force §6A.7 protected list as of session 10-evening**).
*(This whole REALITY/SIMULATION gate stack is the OLD model §3G replaces in DESIGN. It still runs, harmlessly, while ingest is frozen. Do NOT rip it out before the new filter exists.)*

**Physical memory stores (OLD model, still on disk):** (1) `.nh_memory_store.jsonl`. (2) `.nh_reality_store.jsonl`/`.nh_simulation_store.jsonl`. (3) `.nh_simulation_graph.jsonl`/`nh_mental_network.json`.

**Launchers:** `run_app.pyw` (real) · `launch_nh.vbs` · `nh_silent_start.py` (inert) · `nh_service.py` (`NHMotherbase` service — disabled via Autoruns). **⚠ DISTINCT scattered `C:\NH\` copies:** `C:\NH\START.bat` + `C:\NH\silent_start.py` (tunnel blocks commented S9, `.bak` beside). **Session-10 notes:** a disguised desktop "Opera GX Browser" launcher (deleted, desktop only); and a stray **`install_startup.bat`** in engine-core that Cursor's agent spawned (deleted; never run; targeted the still-Disabled `NH_Motherbase` task).

**Server/UI (safe to modify):** `nh_hud_server.py` (routes/UI only; its write functions count as Protected) · `nh_app.py` · HTML stubs.

**Accretive store + tooling [BUILT & VERIFIED]:**
- `nh_accretive_store.py` — append-only layered store module. 8 functions (4 public: `append_root`, `append_reading`, `read_all`, `read_by_subject`); every `open()` is `"a"`/`"r"`, NO `"w"`. *(6-field record, NO `role` field — `_ALLOWED_KEYS` = id/subject/timestamp/content/re_reads/source_title.)* **Note (2a design):** `append_reading` exists as a name but its real body — validating the new reading-schema and appending to the new readings file — is the §2a build, not yet written.
- `.nh_accretive_store.jsonl` — 11,374 root records / 4 groups (002=188, 000=2,252, 001=3,247, gpt_purified=5,687), all `re_reads=[]`, ~14.5 MB. **2a seals this file** (no further appends).
- **`.nh_readings_store.jsonl` — the NEW sibling file 2a creates (does not exist yet).** Holds reading records; the only growing file once built.
- `nh_peek.py` — read-only CLI viewer.
- **`nh_log.py`** → `nh_log.html` — read-only mirror surface (strata/expand/search/RTL; content via `textContent`; offline). Throwaway stand-in for the real engine-backed log.
- **`nh_probe.py`** / **`nh_probe_truth.py`** — read-only boundary-signal + ground-truth speaker probes; settled the speaker question (§11C-S9).
- `inspect_seeds.py`, `ingest_seeds.py` — read-only inspection + the ingest writer.

**`.cursorrules` v3.1 (in-force):** full text §6A. Body UNCHANGED; one protected-file entry (`nh_vector_memory.py`) added to its §7 list on disk session 10-evening.

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- REALITY/SIMULATION two-layer gate (OLD model, still runs). · `promote_to_memory()`. · current gate flow (`/review`). · REALITY-only vector index. · REPORTED_SPEECH (speaker+quote, encrypted). · encryption at rest · web results relabeled INFERRED · TEST_MODE · epistemic sandbox · working chat+HUD · silent auto-start disabled (Autoruns). · all §3D security fixes. · pywebview shows real HUD. · **the accretive store** (11,374 / 4 groups, append-only, re-verified live S7). · **session-9 read-only tooling**. · **session-9 tunnel block commented** in `C:\NH\` files. · **session-10-afternoon boot hygiene**. · **session-10-evening:** `nh_vector_memory.py` added to live `.cursorrules` §7 (verified line 195); stray `install_startup.bat` deleted; `NH_Motherbase` confirmed still Disabled.

**Known regression pattern:** the SIMULATION-routing fix has silently reverted before. Always re-verify on disk before building on it.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE)  [BUILT — governs running code today]

*In-force ruleset Cursor must obey against the CURRENT system (the per-record manual gate). MUST stay identical to the canonical `.cursorrules` on disk in body. §§0–11 IN FORCE; §12 INCOMING. The §0 premise, §0A DUMB/SMART frame, §3G story rework, and all session-10 closures are DESIGN — they do NOT enter the in-force body; they extend §7A and the §12 INCOMING block.*

**0 — IDENTITY.** Sovereign personal AI with strict memory-layer separation. Cursor proposes; Ness approves; Cursor implements. Never skip approval, even for "small" changes to a Protected File.

**1 — ABSOLUTE PROHIBITIONS** (no chat override). Never write code that: writes INFERRED/GENERATED into REALITY via `ContextRouter.write()` without `promote_to_memory()`; removes/weakens the GENERATED block; calls `remember()`/`promote_to_memory()` with `INFERRED` using a hardcoded/default token; writes directly to `nh_mental_network.json` (only `promote_simulation_record()`); merges SIMULATION into REALITY ChromaDB; labels web/synthesis output REALITY/VERIFIED; builds a second/parallel gating classifier; touches `.env`/`.nh_pin.json`/vault/`NH_PROMOTE_TOKEN`/keys/PIN; writes test/mock data into production stores.

**2 — THE ONE-GATE RULE.** Exactly one path into REALITY: `promote_to_memory()` — GENERATED always blocked; INFERRED needs `NH_PROMOTE_TOKEN` or explicit `user_confirmed=True`; VERIFIED direct; REPORTED_SPEECH direct but needs non-empty speaker+quote. `ContextRouter.write()` is NOT a gate alone.

**3 — VERIFIED FILE MAP:** `promote_to_memory()`→`nh_context_router.py` · `guard_write()`→`nh_evidence_integrity.py` (possibly dead) · `ContextRouter.write()`→`nh_context_router.py` · `MemoryStore.write()`/`remember()`→`nh_memory_store.py` · `promote_simulation_record()`→`nh_simulation_graph.py` · `_wire_research_to_network()`/`update_network_async()`→`nh_hud_server.py`.

**4 — THREE SEPARATE STORES.** (1) `.nh_memory_store.jsonl`. (2) `.nh_reality_store.jsonl`/`.nh_simulation_store.jsonl`. (3) `.nh_simulation_graph.jsonl`/`nh_mental_network.json` (IS covered by `/review`).

**5 — DUAL PIPELINE WARNING.** Two research pipelines live; confirm which before extending; do not add a third.

**6 — DUAL STACK.** NEW: `MemoryStore→RealityGraph→ContextRouter→EpistemicSandbox`. LEGACY (read-only): `nh_mental_network.json`+ChromaDB+`nh_timeline.json`+`nh_nightly.py`.

**7 — PROTECTED FILES** (require "CONFIRMED: modify [filename]"): `nh_context_router.py`, `nh_memory_store.py`, `nh_evidence_integrity.py`, `nh_reality_graph.py`, `nh_epistemic_sandbox.py`, `nh_simulation_graph.py`, `nh_research_engine.py`, `nh_research_sandbox.py`, `nh_jarvis_core.py`, `nh_crypto.py`, `nh_auth.py`, **`nh_vector_memory.py`** *(added on disk session 10-evening — line 195)*, the store `.jsonl`s, `nh_mental_network.json`. Safe w/o extra confirm: `nh_viz_engine.py`, `nh_hud_server.py` (routes/UI only — its write functions count as Protected), `nh_mobile_bridge.py`, `nh_metrics_tracker.py`, `check_system.py`, `test_*.py`. *(Disk format is a bullet list; the master's comma-phrasing here is pending the §11.14a wording reconciliation — substance matches disk.)*

**8 — DRY-RUN PROTOCOL.** Before code touching a Protected File or write-path: output PROPOSED CHANGE (File / What / Store(s) / Gate function by exact name+file), wait for "APPROVED"; then full code, wait for "APPROVED" again.

**9 — CODE QUALITY.** No placeholders/TODO. No silent store-write failures. Schema validation for every `.jsonl` payload. Async store writes checked.

**10 — PULL SOVEREIGNTY.** System pushes nothing unsolicited, auto-promotes nothing. No new autonomous task without `# AUTONOMOUS: approved by user [date]`. Re-enabling any silent auto-start/tunnel requires re-verifying the auth layer on disk. *(Session-10-evening underscored this: an agent-spawned `install_startup.bat` would have violated it — caught and deleted before any run.)*

**11 — BEFORE ANY NEW MEMORY FEATURE.** Check the gate files; extend if close. Do not build a fourth parallel gate.

**REMINDER:** every shortcut around `promote_to_memory()` is a sovereignty violation. Propose, name the exact gate, wait for approval.

### 6A.12 — INCOMING (the accretive/membrane direction + §0 + §0A + §3G + session-10 closures)  [NOT IN FORCE]
**Not live instructions.** Until the new filter exists and Ness says active, §§0–11 are law; conflicts resolve to §§0–11.
- **I0 — THE PREMISE (§0):** never close the book into a fact. Safety = non-deciding, not blindness. (Human form: helper, not decider.)
- **I0A — THE TWO MACHINERIES (§0A):** DUMB (moves data, can't interpret) vs SMART/psychologics (reads the person, can't close); membrane = the boundary.
- **I1 — Memory only ADDS, never edits.**
- **I2 — The membrane:** creation lives in chat, barred from *closing into fact* in memory.
- **I3 — One filter, no source exempt.**
- **I4 — Classification never locked.**
- **I5 — The affirmation surface is a per-person STORY-layer READING:** "how does this sit in whose story," firm-but-open, per-person, never collapsed; six optional parts (whose/when/stance/firmness/telling/theme) with absence-read. **N.H is NOT a teller** — the AI's view is a weightless NOTE. **Firmness is READ by the webs.**
- **I6 — Ness steers, doesn't file:** sovereignty = the membrane; he alone affirms a story-layer.
- **I7 — MODE is a peer web** naming the form as a revisable reading on the whole work; composed works still go through every web.
- **I8 — TWO-FILE STORE (2a):** roots sealed in `.nh_accretive_store.jsonl`; readings in `.nh_readings_store.jsonl`, pointing by id; readings never copy root text; both append-only.
- **Reconciliation:** when the new filter + accretive flow ship, §§0–11 are rewritten to match; this INCOMING block collapses in.
- **Status:** DESIGN advanced; **no engine code written, store not wired, gate untouched.** §12 STILL INCOMING, §§0–11 STILL law.

---

## 6B. THE ACCRETIVE STORE — SKELETON + SEED INGEST  [BUILT & VERIFIED]

*The running code of the accretive/membrane direction. A deliberately dumb, standalone, append-only store — the DUMB-MACHINERY heart (§0A). Wired to NOTHING by design.*

**Module:** 4 public functions (`append_root`, `append_reading`, `read_all`, `read_by_subject`) + 4 private; every `open()` is `"a"`/`"r"`, **no `"w"`**; schema validated before every append.

**ROOT record schema (SIX fields):** `id` (uuid4) · `subject` (non-empty; provenance placeholder for seeds) · `timestamp` (ISO; ingest time) · `content` · `re_reads` (list of ids; `[]` = root) · `source_title`. **NO `role` field** (confirmed in `_ALLOWED_KEYS`).

**★ READING record schema (the §2a DESIGN — NOT yet in code):** lives in the **new sibling file** `.nh_readings_store.jsonl`, never in the roots file. Fields: `id` · `reads` (root id(s) — the pointer) · `meaning` · `confidence` (single reading; never aggregates) · `role` (carried from source) · `story_layer` (the six-part, absence-aware shape — §7B Part 2.5) · `mode`/form-name · `timestamp` (when the reading was made). **A reading never copies root text — it points.** To *show* a reading: read the readings file, follow `reads` ids into the sealed roots file, **stitch** (root text + the reading on top). A re-read later is a NEW reading record beside the old, never overwriting — accretion (R6).

**No `reason`/`why` field, by design** — the why is shown by what a layer points at (the arrows) and kept as the AI's NOTE outside the record (§0/§7B Part 7.5).

**In the store now:** 11,374 root records / 4 groups; all `re_reads=[]`; readings file not yet created. The smallest real thing that proves append-only layered memory works.

---

## 7. THE BIG DESIGN — FULL TEXT (UNIVERSAL FILTER + MEANING ENGINE)  [DESIGNED — not built]

### 7A — THE UNIVERSAL FILTER: OPERATING RULES (full)

*A ruleset. Any AI that reads/sorts/stores inside N.H must obey every rule.*

**RULE 0 — WHAT THIS SYSTEM IS.** A sovereign memory system. You are a **reader and a layer-er** (SMART machinery, §0A), not owner/author/judge. Final authority: Ness. **N.H is Ness's helper, not his decider.**

**RULE 0.5 — THE PREMISE: NEVER CLOSE THE BOOK INTO A FACT.** You may reason fully; you may NEVER close a conclusion into a decided fact, nor collapse per-person story-layers into one shared truth. Reasoning is free; *closing/deciding* is forbidden to you and reserved to Ness. (§0.)

**RULE 1 — ONE FILTER. EVERY PIECE. NO SOURCE EXEMPT.** FORBIDDEN: tagging anything by source/filename. *(Includes a composed WORK — a story still goes through every web at full depth; mode names it but never exempts it.)*

**RULE 2 — THE FILTER SORTS / READS. IT NEVER CLOSES "REAL."** It reads **story-layers per person** (Rule 5.5), never one shared fact. **Filter reads. Human steers. Always.**

**RULE 3 — ONE CONTINUOUS READER, NOT TWO STAGES.** Finding where a piece begins/ends and naming its meaning-type are the same act. *(A boundary is a span-CLAIM (a layer); a speaker-flip is a boundary VOTE only — the speaker is carried, not guessed, §11C-S9.)*

**RULE 4 — MEANING FROM WIDE CONTEXT, NOT LOCAL WORDS.** Thin context → low-confidence by default; say so.

**RULE 5 — CLASSIFICATION IS NEVER LOCKED.** Every reading is provisional forever — incl. the MODE name and the story-layer FIRMNESS and **the read of a gap.**

**RULE 5.5 — THE AFFIRMATION SURFACE IS A PER-PERSON STORY-LAYER, NOT A FACT (§3G).** The question is **"how does this sit in *whose* story."** Properties: **(a) firm-but-open**; **(b) per-person** — never collapse tellings into one; **(c) firmness is READ, not set** — combined output of all the webs, itself revisable. You never produce a fact. **N.H is NOT a teller** — your own view is a weightless NOTE (§7B Part 7.5). You MAY *estimate* a human's story-layer, but it stays a note until a human affirms it. **The story-layer has SIX optional parts (whose · when · stance · firmness · telling · theme); a missing part is itself read for its *kind* of absence (§7B Part 2.5).** **(CLASH:** disagreeing story-layers — across people or across one person's own time — sit BESIDE each other (R6); you SURFACE the disagreement, never pick a winner. The clash IS the mirror.)

**RULE 6 — MEMORY ONLY ADDS. IT NEVER EDITS. (KEYSTONE.)** New context → add a new layer beside the old, never overwrite/delete. FORBIDDEN: editing, overwriting, correcting-in-place, deleting, merging-away, "cleaning up." The only write is append. *(A changed dose lands BESIDE the old; a clash is two layers beside each other; the AI's later note lands BESIDE its earlier note; a later reading of a gap lands beside the earlier — so nothing hardens. This is also the DUMB-machinery law, §0A.)*

**RULE 7 — THE MEMBRANE: CREATION LIVES IN CHAT, NEVER CLOSES IN MEMORY.** Bridging gets full freedom in chat and is barred from *closing into a fact* in memory. *(The membrane is exactly the §0A boundary: SMART machinery never closes into DUMB memory.)*

**RULE 8 — WHICH OLD STATEMENTS GET RE-READ.** Use associative bridging as the relevance-trigger. Spurious links are acceptable — rejectable layers.

**RULE 9 — HOW THE FILTER SORTS: BY MEANING-TYPE, IN A GROWING STRUCTURE.** Root distinction: *why it was said*. Candidate intent types (~7): state/claim · ask · wonder · express/feel · intend · report · imagine — the **intent** web. **MODE / REGISTER is a SEPARATE PEER WEB, orthogonal to intent:** a piece has BOTH an intent AND a form. Mode produces a **name** (document/story/article/poem/turn) as a **reading, not a stamp** (revisable R5; accretes R6) on the **whole work** (the `re_reads` span); each sentence inside is still read by EVERY web. Mode COMBINES with the other webs, never overrides. Whose work = **deixis**. Forms = a **small open set**.

**RULE 10 — MAXIMAL-BUT-BOUNDED.** Small (~5, cap 7), grows by depth not width.

**RULE 11 — NESS'S ROLE: STEERER, NOT CLERK.** No per-record manual-approval workflow. His sovereignty = standing authority to steer and override, and to be the only one who **affirms a story-layer.** By being present in chat, Ness IS the membrane. *(The helper/decider line lives here: the AI advises endlessly; Ness decides.)*

**RULE 12 — HONESTY ABOUT WHAT THIS IS.** TRUE: "a structured place for the AI to be creative without that creativity *closing into* what's permanent." FALSE/forbidden: that this "makes the AI think independently" / gives N.H its own story. Never overclaim.

**FAILURE MODES — STOP IF YOU CATCH YOURSELF:** (1) REALITY-by-source→R1. (2) closing into true-for-everyone without Ness→R2/R0.5. (3) fixed-unit chopping→R3. (4) local-word classifying→R4. (5) treating a past classification (incl. mode-name or a gap-read) as final→R5. (6) collapsing per-person story-layers, OR resolving a clash→R5.5. (7) editing/deleting memory→R6. (8) an associative leap closing into fact→R7. (9) silently expanding past the line→R10. (10) per-record approval workflow→R11. (11) claiming independent thinking / giving N.H a story-layer→R12/R5.5. (12) a `reason`/`why` FIELD or inside-a-record span→the why is a NOTE; the only span is `re_reads` across whole records. (13) writing the AI's own view onto the story surface, OR letting the AI's notes AGGREGATE confidence→§7B Part 7.5. (14) mode SHORTCUTTING the other webs→R9/R1. (15) **(session 10-evening)** *inventing* a missing story-layer part instead of reading the absence honestly, OR putting a reading into the SEALED roots file instead of the readings file→R5.5/R6/§6B. **When in doubt: filter reads, human steers; memory only adds; creation stays in chat; nothing closes into a fact; the AI is not a teller; the note never hardens; absence is read, never invented.**

### 7B — THE MEANING ENGINE: THE MECHANISM (full depth)

**THE ONE-LINE SHAPE.** A piece runs through a **chain of webs** (SMART machinery), the engine fills each by researching inward (the person) + outward (the world) at night; what it can't fill, it **informs** Ness (never asks, never waits); everything is written to a **read-only, subject-tagged, permanent log** Ness can click through — and every reading lands in the **readings file**, pointing at the **sealed roots** (DUMB machinery), never inside them.

**PART 1 — CHAIN OF WEBS, RUN AS ONE.** Meaning is what holds across all webs together. The category list (claim/ask/feel/…) is ONE web (intent), not the engine.

**PART 2 — THE REAL WEBS:** 1. INTENT (speech-act). 2. DEIXIS (who/when/where — incl. *author*; on the §0A seam). 3. COMMON GROUND. 4. IMPLICATURE (Gricean; a flout = the sarcasm/irony tell; on the §0A seam). 5. THEORY OF MIND (model the mind behind it — incl. a *character's* mind). 6. TIME/SEQUENCE. 7. RE-READING (re-run later → NEW layer). 8. **MODE / REGISTER** (form of the whole work). *(…list is open; each new web a real grounded dimension.)*

**PART 2.5 — THE STORY-LAYER WEB (the heart of SMART machinery).** Reads **how a piece sits in *whose* story** (Rule 5.5) — a reading, not a verdict; firm-but-open; per-person; never collapsed; never closed. **Firmness is READ here** as the combined output of all the webs. **N.H is not on this web** — its view is the weightless NOTE.
- **★ THE SIX OPTIONAL PARTS (session 10-evening, narratology-grounded):**
  - **whose** — the teller (≈ point-of-view at the level of *who*). 
  - **when-in-his-story** — where this telling sits in his *arc/flow* (NOT `timestamp`, which is when the reading was made). Load-bearing for **clash across his own time** — without it you can't tell past-Ness from now-Ness.
  - **stance / point-of-view** — which *way he faces* his own telling (sure / doubting / defending / confessing / looking-back). A different axis from firmness.
  - **firmness** — how *hard he leans* on it (read, not set; revisable).
  - **telling** — the content, *what is said* (≈ the *story* vs *discourse* split's "story").
  - **theme / what-it's-about** — the thread that ties tellings together across the book; **the field that makes the mirror work** ("you keep circling this").
- **★ EVERY PART OPTIONAL; ABSENCE IS ITSELF READ.** Not every telling carries every part. Forcing a missing part = inventing = the §0 freezer-move. So a story-layer holds only what's honestly read — and **a gap is read for its *kind*:** *not-there-yet* (fillable later), *withheld* (deliberately left out — part of the telling), *doesn't-apply* (structurally absent — the truth of the piece), *avoided* (circled-but-unnamed — the loudest, pure mirror material). The mirror lives in the silences. A gap-read is revisable/accreting (R5/R6): empty today can fill later by a reading landing beside, never overwriting.
- **CLASH lives here:** disagreeing story-layers sit beside each other (R6) and are SURFACED, never resolved.

**PART 3 — HOW THE WEBS COMBINE.** Separate lenses, one camera; light passes through all together → one image. Richness = breadth across webs + the relationships between what lights up. *(This is why mode never has to gate anything — "this is a story" + "this line expresses despair" combine into "despair-inside-a-story.")*

**PART 4 — NIGHTLY RESEARCH, INWARD + OUTWARD.** Fill missing webs by researching both directions at night. A piece is HELD while research runs.

**PART 5 — HOLD UNTIL ENOUGH (not until perfect).** Then the piece moves forward to become a reading — *ready to show*, never *closed/true*.

**PART 6 — CAN'T FILL → INFORM, DON'T ASK.** Surface the specific gap by name; keep running. Ness is present, not required. "Unknown" is honest, valid, re-checkable. *(This is the same spirit as absence-is-read: a gap is information, never a failure.)*

**PART 7 — THE LOG (read-only, subject-tagged, permanent, clickable).** The surface through which Ness sees the engine's nightly mind. Read-only (accretion made visible). Subject-tagged. Permanent + findable. Clickable (subjects expand; entries open to show piece, webs, unknown-flags, layers, story-layers + their gap-reads + clashes over time). Three things at once: transparency, the mirror (INWARD), a permanent archive. *(`nh_log.py`→`nh_log.html` is the throwaway stand-in building the SURFACE MECHANICS now; the real engine-backed log replaces it. **This is also where CLASH and the eventual gap-reads surface — see §11.14h.**)*

**PART 7.5 — THE NOTE / THE WHY (the AI's whole perspective; weightless SMART machinery).** The AI's own reasoning — the *why* behind a reading, AND **N.H's entire perspective** (it is not a teller, so it has no story-layer; its view lives ONLY here) — is a **non-decisive NOTE**, not a record field, not a story-layer. Pulled OUT of the chat response (the chat reads naturally; N.H never narrates its mechanism — §14) into (a) a **side surface** Ness opens on demand, and (b) the AI's own **topic-sorted logs**.
- **Properties:** readable by Ness; weightless to the story question; the AI MAY read and build on its own past notes (full reasoning — safety is non-deciding, not blindness).
- **★ WHY A NOTE, NOT A STORY-LAYER (heaviness):** putting the AI's view on the story surface would give it a **heaviness** it must never have. The AI reads *constantly and voluminously*; on the story surface its sheer volume would drift toward authority (§0). The note surface has no such gravity. It matters only to N.H — kept, accreting, feeding its own future readings — and never reaches onto the story dial.
- **★ THE NOTE CANNOT HARDEN (R6 on the AI's own notes):** later notes **land BESIDE** earlier ones, never confirming/overwriting; **confidence attaches to one reading of one piece and NEVER aggregates across notes.** A past note lends *context, never confidence.* Hardening = aggregation of confidence; accretion forbids aggregation; firmness has nowhere to pile up.
- *(Enforcement flag, §11: "the note never closes into fact" AND "the note never aggregates confidence" must both be load-bearing.)*

**PART 8 — HOW THIS LOCKS INTO §7A:** webs=R3/R4/R9; mode-web=R9; re-reading+layers=R6/R5; story-layer web + six parts + gap-read + firmness-read + clash=R5.5; inform-don't-ask=R11/R7; read-only log=accretion visible; the note=R7/R0.5/R5.5/R12; don't overclaim=R12.

**TRUEST SENTENCE (engine):** One engine reads each piece across many real webs of meaning at once — including what form it was made in and how it sits in *whose story* (whose, when, stance, firmness, telling, theme — reading even the *shape of what's missing*) — researching the person and the world to fill them; what it can't fill it shows Ness without asking or waiting; the AI reasons fully and leaves its why as a weightless note Ness can open (it is not a teller; its notes never harden); and every reading is written, read-only and forever, into the readings file pointing at the sealed roots — so the engine looks outward while Ness looks inward, both at their own speed, meeting in a record that only ever grows and never closes.

### 7C — CAN IT BE BUILT? (honest)

The **accretive skeleton** is built (§6B, 11,374 records). **The unit/segmentation problem is dissolved** (S7): a unit is a **span-claim, not a cut**. The architecture FORCED this: `re_reads` pointers survive only if targets never move → a frozen fine substrate with meaning-spans floating above = boundaries-as-readings. **Session 10-evening made this physical:** the substrate is *literally* a sealed file (roots), the floating spans a *separate* file (readings) — Path B.

**WHAT REMAINS (ordinary build).** The detector is unbuilt and will be imperfect — fine. Cheap checks at each gap: **speaker flip** (a boundary VOTE only — speaker CARRIED, §11C-S9), discourse-reset markers, topic shift. *(S9 refinements: "?" is NOT a Ness tell — 31.8%; length IS strong — NESS median 9 / AI median 170; detector must allow same-speaker DOUBLING — alternation 27.9%.)* *(Same good-enough-and-revisable forgiveness applies to FIRMNESS and to GAP-READS — a misread is a rejectable/revisable layer.)*

**THE FORCED BUILD ORDER (never re-fought):** **(1) reading-layer record shape** — NOW FULLY DESIGNED (session 10-evening): two files (roots sealed, readings sibling), the 8-field reading record incl. `role` (carried), the six-part absence-aware `story_layer`, the mode-name. The AI's own view goes to the **note**, not here. A §6A.8 store-touching schema decision; the ONE unblocking piece; **FRESH-HEAD, never tail-of-session — still to be LOCKED and BUILT (dry-run).** → **(2) the detector** — read-only probe FIRST. → **(3) the engine** — the full chain-of-webs; LAST.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. KEEP the OpenRouter key. Security: synthesis text-in/text-out only; fetched content framed as unverified raw; **auto-reject never auto-delete**; rejected-bin "look don't touch" (URLs as plain text, render via `textContent`, strip invisible/RTL chars). Costs ~$120–300/mo. Academic source OPEN (Semantic Scholar + OpenAlex).

---

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]
**Access/auth:** Dry mode (default) · Personal mode (PIN) · graduated step-up (fingerprint > PIN > voice) · raw-vs-derived dial · trusted-app-only, zero-copy. **Mobile (three modes):** Mode 1 Full (deliberate tunnel) · Mode 2 Local AI online · Mode 3 Lite/offline · Manual Sync. **Interactive canvas.** **Behavioral-baseline wellbeing.** **HUD redesign.** **Multi-perspective "according to whom" field — this IS the per-person STORY-layer (§3G/§7A R5.5)** with its six optional parts. **Other unbuilt:** phone-data importer · memory browser · personality modeling · nightly scraper · voice in/out · ChromaDB cleanup · folder cleanup.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Layers: (1) Metadata = firmly-told fact of the story (EXIF). (2) Plain-description layer = low-opinion w/ confidence → create-side. (3) Context-meaning = interpretation, a re-reading layer → never closed. (4) Ness confirms → a layer (or honest "unknown"). Fits the 2060.

---

## 10. ORIGINALITY (honest calibration)
Every brick exists somewhere; the **combination** ships nowhere. Claim the combination + the inverted default + the **per-person, never-closing STORY model** (story-layers + clash-surfaced + AI-is-not-a-teller + **absence-as-a-read**) + the **DUMB/SMART (psychologics) machinery** split as further distinctives. Never claim inventing local AI or approval gates. *(Verify arXiv IDs before leaning publicly.)*

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ SKELETON + DATA + re-verified. (a) `nh_peek.py`/`nh_log.py` ✅. (b) seed ingest ✅. (c) **wire the store into live flow** — STILL OPEN; heaviest move; triggers §6A.12 reconciliation; next-session, never tail.
2. **THE FORCED ORDER — reading-layer schema → detector → engine:** **(2a) reading-layer record shape — NOW FULLY DESIGNED (session 10-evening), NOT yet locked/built.** Two files (roots sealed in `.nh_accretive_store.jsonl`; readings in NEW `.nh_readings_store.jsonl`, pointing by id, never copying text). 8-field reading record: `id·reads·meaning·confidence·role·story_layer·mode·timestamp`. `story_layer` = six optional parts (whose·when·stance·firmness·telling·theme) with **absence read for its kind.** **What's LEFT on 2a:** (i) the final fresh-head LOCK of the field list (concepts settled; the assembled list is a draft awaiting Ness's confirm); (ii) the genuinely-open sub-shape questions if any remain on `story_layer` storage vs live-read (leaning: store-the-read, legal because storing-a-read ≠ closing-a-fact); (iii) the new file's exact name. ALL fresh-head, dry-run (§6A.8). → **(2b) detector** — read-only probe FIRST; allow same-speaker doubling; length strong, "?" not. → **(2c) engine** — LAST.
3. **Image-ingest front door (§9A).**
4. **Universal Filter / meaning engine** — **STANDING DECISION: INGEST FROZEN** until the engine exists. WhatsApp (§12) archived-and-waiting.
5. **ChromaDB cleanup** — on hold.
6. **Research pipeline build** — Brave + academic source + security defaults.
7. **Hetzner sovereignty sync.**
8. **`nh_service.py` registration** — ✅ RESOLVED (disabled via Autoruns).
9. **Mobile companion + canvas.**
10. **HUD redesign** — after store + filter.
11. **Doc/code consistency (§3F)** — ✅ CLOSED S9; one entry (`nh_vector_memory.py`) closed *on disk* S10-evening; master wording reconcile pending (§11.14a).
12. **Folder cleanup** across the three scattered locations — mostly done; S10-evening deleted the stray `install_startup.bat`. Remaining: full sweep when convenient.
13. **WhatsApp archive → eventual ingest (deferred):** decrypt `.crypt14` → SQLite front door → child-data call → ingest only with engine. Carry the sender.
14. **★ The reality→STORY rework + 2a + DUMB/SMART consequences (WORK; none urgent, deferrable while frozen):**
    - **(a) Spine re-draw / propagation:** propagate "reality-layer"→"story-layer" across the whole doc + code; fold in the session-10 closures; **reconcile §6A.7 WORDING to disk** (bullet list incl. `nh_vector_memory.py`). Major, fresh-head. §6A.12 already carries the new shape.
    - **(b) Code gap:** the built two-store gate lags the design (harmless while frozen). Do NOT rip out the old gate before the new filter exists.
    - **(c) `.cursorrules` reconciliation:** §0 + §0A + §3G + closures eventually enter code law; INCOMING, not in-force.
    - **(d) ✅ CLOSED (was "lean-on-hard"):** DISSOLVED — firmness READ by the webs.
    - **(e) ✅ CLOSED:** N.H is NOT a teller; weightless note.
    - **(f) Enforcement flag (TWO):** "note never closes into fact" AND "note never aggregates confidence."
    - **(g) ✅ CLOSED (register/mode):** mode = peer web naming the form.
    - **(h) Open thread (low): CLASH + GAP-READ SURFACING — how the UI/log shows two disagreeing story-layers (and the *kind* of a gap) without implying a winner or inventing.** Located, not designed. Near §7B Part 7 + §14.
    - **(i) ★ NEW open thread (session 10-evening): WRITE THE DUMB/SMART (psychologics) MACHINERY SECTION (§0A) into its final master place** — with its two pins: (1) the name (smart vs psychologics); (2) whether note+clash file *under* SMART or are *called out inside* it. Fresh-head.
    - **(j) ★ NEW open thread (low): the 25-file Cursor batch never reviewed.** During the `.cursorrules` fight, Cursor's agent queued ~25 file changes (the stray `install_startup.bat` was one; the other ~24 unexamined). Run `git status` in `nh_engine_core` (if under git) to see whether the agent touched anything else. Parked; fresh-head.

---

## 11A. SETTLED SESSION 4 — STEP-2 SEED-INGEST DECISIONS  [BUILT for 002; pattern set]
Unit = per-message. Subject = honest provenance placeholder. The ChatGPT `title` is NOT the subject; rides in `source_title`. Read-only on sources. For a provisional step, pick the choice that destroys the least.

## 11B. SETTLED SESSION 5 — TXT-SEED DECISIONS  [BUILT for gpt_purified; cleaned_history set aside]
`gpt_purified` → per-turn on role markers; stream label → `source_title`. `cleaned_history (1).txt` → DELIBERATELY NOT INGESTED (0 structure + damaged). The discipline includes knowing when NOT to ingest.

## 11C. SETTLED SESSION 7 — UNIT DISSOLUTION + LIVE VERIFICATION  [DESIGN settled; FACTS verified]
Unit = span-claim not cut → only adds depth. Two places (dumb memory + fast calculator — now the §0A frame). The why shown by pointers. Only span = `re_reads` across whole records. Four facts verified live (11,374; 188/2,252/3,247/5,687; 8 functions no-`"w"`; `.cursorrules` v3.1 §12 NOT IN FORCE).

## 11C-S9. SETTLED SESSION 9 — THE SPEAKER QUESTION (GROUND TRUTH)  [DESIGN settled]
- The store dropped the speaker on gpt_purified too — no `role` field AND no in-content marker. The SOURCE file still has the `[NESS]:`/`[AI_RECALL]:` marker.
- Alternation broken: flip 27.9%, NESS-NESS 36.2%, AI-AI 35.8%. **Detector must NOT assume turn-taking.**
- Length powerful: NESS median 9, AI median 170. "?" is a TRAP (31.8%).
- **DECISION: the reading-layer schema CARRIES `role`, back-filled from source. Do NOT re-derive from shape.** Shape is a *boundary* vote only.

## 11D-S9. SETTLED SESSION 9 — THE PREMISE + THE REALITY REWORK  [DESIGN settled]
- Premise (§0): never decide facts. The danger was reasoning *hardening into authority*, never reasoning itself. Resolved the `why`-field ban: the why is a non-decisive note.
- Reality reworked (§3G): no REALITY box of facts. "Real" became a per-person, layered, revisable READING. Reality moves from the storage spine INTO the filter.

## 11D-S10. SETTLED SESSION 10-AFTERNOON — THE STORY RE-SOUL + ALL THREE FORKS CLOSED  [DESIGN settled]
- **Reality-layer → per-person STORY-layer (REPLACES).** Told, not truth-checked; firm-and-open by nature; per-person, never collapsed.
- **Fork 1 CLOSED:** N.H is NOT a teller; its view is a weightless NOTE (heaviness argument). The note cannot harden (R6 on its own notes).
- **Fork 2 CLOSED:** mode is a PEER WEB naming the form on the whole work; composed works still go through every web.
- **Fork 3 DISSOLVED:** no "lean-on-hard" marker; firmness READ by the webs.
- **Clash is a feature:** N.H surfaces disagreeing story-layers, never picks a winner; the clash IS the mirror.

## 11D-S10.1. SETTLED SESSION 10-EVENING — 2a SHAPED + STORY-LAYER FIELD + DUMB/SMART FRAME + HELPER-NOT-DECIDER  [DESIGN settled; one verified disk fix]
*Direct child of the afternoon's re-soul. All design except the verified `.cursorrules` line and the deleted stray file.*

- **★ 2a STRUCTURE — TWO SEPARATE FILES (Ness's call).** Roots sealed in `.nh_accretive_store.jsonl` (never appended again); readings in a NEW sibling `.nh_readings_store.jsonl`. A reading **points at** a root by id, **never copies** its text. To show a reading: read readings → follow ids into sealed roots → **stitch**. A re-read is a NEW reading beside the old (R6). Makes the §7C frozen-substrate picture *physically true*; a wrong reading can never damage the sealed roots.

- **★ THE READING RECORD — 8 fields:** `id · reads · meaning · confidence · role · story_layer · mode · timestamp`. The "why" is the pointer (`reads`), never a `reason` field; the AI's own view goes to the NOTE, not here. *(Concepts all settled/Ness's; the assembled list is Claude's draft awaiting the fresh-head lock.)*

- **★ THE STORY-LAYER FIELD — SIX OPTIONAL PARTS, ABSENCE-READ.** whose · when-in-his-story · stance · firmness · telling · theme. Narratology-grounded. **Every part optional** (forcing a missing part = inventing = §0 freezer). **Absence is itself read for its *kind*:** not-there-yet / withheld / doesn't-apply / avoided. The mirror lives in the silences. Distinctions held: `when` (told-thing's arc) ≠ `timestamp` (reading's time); `stance` (which way he faces) ≠ `firmness` (how hard he leans) ≠ `whose` (the teller). Gap-reads are revisable/accreting (R5/R6). *(Ness's correction that produced it: "absent" isn't a hole to leave — it's a parameter that connects to *why* it's a gap.)*

- **★ NEW TOP-LEVEL FRAME — DUMB vs SMART (psychologics) MACHINERY (§0A).** DUMB = moves/holds data, safe because it can't interpret. SMART = reads the person, safe because it can't close. Membrane = the boundary. Two pins open (the name; note+clash placement). Seam acknowledged (deixis/implicature). *(Ness: "we should divide … into a category referenced as 'psychologics machinery' … it will need to be a category in the masterfile, about the dumb machinery and the smart machinery.")*

- **★ THE CRYSTALLIZATION — "N.H is Ness's HELPER, not Ness's DECIDER."** Re-derived by Ness from "how can it help me decide if it never decides?" The AI reads/connects/leans, then hands it over; Ness decides. The loop: *real life → help → understand → a solution from himself.* Holds §0/§1/§7A R11 in one line.

- **★ DISK (verified):** `nh_vector_memory.py` added to `.cursorrules` §7 PROTECTED FILES (line 195), closing the §5-vs-§6A.7 gap; confirmed by `findstr` after a file-lock fight (done by hand). Stray `install_startup.bat` (Cursor-agent-spawned boot installer for the still-Disabled `NH_Motherbase`) deleted; never ran (`schtasks` confirmed Disabled).

- **Status:** all DESIGN except the two disk items. Built gate untouched. Forced build order UNCHANGED.

---

## 12. SESSION 6 — THE DATA-RESCUE OPERATION (NOT an N.H change)  [recovery done; ingest FROZEN]
A13 WhatsApp 2012→2024 (age 7 → 2024), first-ever account, surviving only on a phone nearly thrown away. Message DBs (`msgstore.db.crypt14` + backups, ~118 MB, **still ENCRYPTED**) + media → copied to PC (`C:\Phone_A13_Backup`) + Drive. **SETTLED: ingest FROZEN** — archive now, ingest deliberately later (engine + media front door + child-data call all pending). When it enters: decrypt → SQLite front door (carry the sender) → child-data call → ingest. The most "Ness" data N.H will ever hold.

---

## 13. THE LIVE LOOP — HOW N.H RUNS WITHOUT EVER STALLING  [DESIGNED — not built]
A figure-eight, cache outside. **Part 1 — the starter — FIRE-AND-LET-GO:** picks up from cache, hands to the deep side, turns free in the same instant. **Part 2 — the deep side** (memory · filter · reasoning · deep search): each job on its own clock, announces itself back. **No worker count.** **Locks in §0/§3C/§7A R7 + §0A** from the runtime side — the deep (SMART) side computes fast, the append-only store (DUMB) stays safe; a fast wrong reading is a rejectable layer. Precondition for voice. Nothing coded.

---

## 14. THE CHAT FRONT DOOR — A WORKING DESIGN SKETCH  [DESIGNED-IN-PROGRESS — NOT confirmed, not built]
The live chat is itself an input (a front door, §1A) — Ness↔N.H recorded, speaker carried, connect-not-claim. Two-filter path riding §13. The **point-back** is the one thing shown in chat (clickable `re_reads` — navigation not narration). The quiet surface: no recording badge; **N.H NEVER narrates its own mechanism** (why the why is a side NOTE). **THE GUARD:** the §13 loop carries N.H's output toward memory — safe ONLY as an append-only proposal, never a closing crossing (the §0A boundary). FROZEN like all ingest; capture decision (always-on vs deliberate-keep) is an unresolved one-way-door / child-data-flavored question needing Ness. *(This is also where CLASH and gap-reads surface to Ness — §11.14h.)*

---

## 15. SESSION 10 — BOOT HYGIENE + WINDOWS SIGN-IN + THE .CURSORRULES FIX (NOT N.H engine changes)  [housekeeping done]
*Side tasks, recorded for continuity; touched no N.H engine code, no store, no gate.*
- **Afternoon — boot hygiene:** the HUD opening on boot was NOT an N.H auto-start (every startup vector verified clean — Startup folders, Run keys, `\NH_Motherbase` task Disabled, `NHMotherbase` service Stopped). Real cause: Windows' "reopen apps after sign-in" (off) + a disguised desktop "Opera GX Browser" launcher (deleted, desktop only). Verified fixed by restart.
- **Afternoon — Windows sign-in:** Kensington VeriMark Desktop Fingerprint Key (USB-A, ₪351) ordered; ESS off on 24H2 if needed; Windows sign-in only, distinct from N.H auth.
- **Evening — the `.cursorrules` fix:** `nh_vector_memory.py` added to §7 PROTECTED FILES on disk (line 195). The editor's Save fought a Windows file-lock (15 Cursor processes; UNKNOWN FileSystemError); the line was typed by hand and the save eventually landed; verified by `findstr` (the only trustworthy check). Lesson re-proven: trust disk, not the editor's "saved."
- **Evening — the stray installer:** Cursor's agent spawned `install_startup.bat` (a SYSTEM/ONSTART auto-start installer for the old `NH_Motherbase` task) and queued a ~25-file batch. The .bat was **deleted** (never run; `schtasks` confirmed the task still Disabled); the other ~24 queued files were **not reviewed** — parked as §11.14j (`git status` when fresh). Lesson: an agent generating a privileged auto-start script unsolicited is exactly what §6A.10 (Pull Sovereignty) forbids — caught by *looking*, not by trusting.

---
**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk — re-proven S10-evening: the editor reported saves that weren't on disk; only `findstr` confirmed the real write) · one concrete step at a time · finish the thing in front before scope-expanding · **NEVER DECIDE FACTS — never close the book; the danger was reasoning hardening into authority, never reasoning itself (§0)** · **★ N.H is Ness's HELPER, not Ness's DECIDER — it reads, connects, and leans, then hands it over; Ness decides; what comes out the far side is HIS (§0/§1/§7A R11)** · **★ TWO MACHINERIES: DUMB (moves data, safe because it can't interpret) vs SMART/psychologics (reads the person, safe because it can't close); the membrane is the boundary (§0A)** · **a fact stops being yours — everything in N.H is yours, relative-to-Ness; so there is no fact-box (§3G)** · **the affirmation surface is a per-person STORY, not a "reality" — firm-but-open by nature, never collapsed, never closed (§3G/§7A R5.5)** · **★ a STORY has six optional parts (whose·when·stance·firmness·telling·theme) and not every telling carries them all — and ABSENCE is itself read for its KIND, never invented; the mirror lives in the silences (§7B Part 2.5)** · **N.H is NOT a teller — its perspective is a weightless recorded opinion (the note), kept weightless because the AI reads constantly and weight would drift to authority** · **the note cannot harden — later notes land beside, confidence never aggregates** · **mode is a peer web that NAMES the form on the whole work; composed works still go through every web; the name is revisable** · **firmness is READ by the webs, not set — load-bearing things are firmly-TOLD facts of the story** · **stories can CLASH — N.H surfaces the disagreement, never picks a winner; the clash IS the mirror** · **★ TWO FILES: roots sealed, readings beside, pointing by id, never copying — a reading is read by stitching across both (§6B/§7C)** · memory only adds, never edits · the membrane (creation in chat, never closes in memory) · two places: dumb memory + fast calculator · a unit is a span-claim not a cut · the why shown by pointers, never a `reason` field · input-agnostic: one engine, many front doors · archive don't ingest · הכל יחסי — meaning is relative, revisable, AND relative-to-whom · the AI WILL interpret — catch it as a dated, confidence-tagged, non-closing, weightless note · don't overclaim (the story model is reworked in DESIGN; the code still runs the old gate) · **carry the speaker, don't guess it (§11C-S9)** · the chat never waits because no hand ever holds still (§13) · design to fit how Ness thinks — offer the shape, let him confirm the fit · don't inform, just flag and keep going · **a thinking session leaves almost nothing on disk to re-derive from — so it must be captured** · **the spine line: stop forcing the decision, build a structure where not-deciding is safe — designed from how Ness works, not forced onto it.**

### TRUEST SINGLE SENTENCE
N.H is Ness's helper, not his decider: it gives the AI a place to reason and create freely (the chat) where Ness is present to steer, and a memory of two files — sealed roots and readings floating beside them, only ever added to, never closing the book — so meaning, and how-each-thing-sits-in-whose-story (whose, when, stance, firmness, telling, theme, and even the shape of what's left unsaid), can keep evolving forever without anything hardening into a fact that pretends to be true for everyone; the dumb machinery holds the data and cannot interpret, the smart machinery reads the person and cannot close, the membrane stands between them; the AI reads constantly but is never a teller (its view is a weightless note that cannot harden), every person's story is held firmly-yet-openly and never merged, and where two tellings disagree the system shows the clash rather than choosing — because N.H was never about escaping reality, it is about refusing to let reality be counterfeited, refusing to flatten whose-story-is-whose, and refusing to ever shut the book, so that Ness walks back out into his life with a solution that is his own.
