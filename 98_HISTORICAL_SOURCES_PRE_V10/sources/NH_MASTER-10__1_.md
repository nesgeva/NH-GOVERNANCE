# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, the reality model, AND the code rules — is written out IN FULL below at the depth of the original source files. Nothing is referenced-only.
*Rebuilt June 20 2026 (session 3) from a full read of all project files; updated sessions 4–8; then **session 9 (June 22 2026, past midnight)** — this is **MASTER-10**. **Session 9 was a DESIGN + read-only-tooling session: the founding REALITY/SIMULATION concept was reworked in DESIGN, three read-only tools were built, and the gpt_purified speaker question was settled with ground truth. NOTHING destructive happened on disk — store still 11,374 records / 4 groups, append-only; the built REALITY/SIMULATION gate code is UNTOUCHED and still runs the old model.** The forced engine build order (§7C/§11) is STILL UNCHANGED. This file embeds, at full depth: the new PREMISE (§0), the complete Universal Filter rules (§7A), the complete meaning-engine mechanism (§7B), and the full in-force code ruleset `.cursorrules` v3.1 (§6A — UNCHANGED, still governs the running code). It is THE only document. About the N.H system ONLY — nothing about the anime.*

> **WHAT CHANGED IN SESSION 9 (the short delta — read this first):**
> 0. **NOTHING DESTRUCTIVE ON DISK.** No records changed, no schema, no ingest, no edit to a protected store. Store still **11,374 records / 4 groups**, append-only, ~14.5 MB. Three NEW read-only tools were added (they only read the store / source and write their own output files). Two `C:\NH\` launcher files had their tunnel block commented out (verified on disk). The built REALITY/SIMULATION gate code is UNTOUCHED.
> 1. **THE PREMISE — "NEVER DECIDE FACTS / NEVER CLOSE THE BOOK" (the night's biggest find).** The danger N.H exists to stop was never *reasoning* — it was **reasoning hardening into authority** (a guess freezing into a closed, settled fact). So the AI may reason fully: connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time. It may do everything except one thing — **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real." Reasoning is free; *closing* is forbidden; *deciding what is real* is Ness's alone. Every other rule in this file — the membrane, accretion, non-decisive opinions, the note — is this single premise enforced in a different place. New **§0**. (Honest scope, Rule 12: this is settled as DESIGN; the built gate code still does the old promote-to-REALITY thing, harmlessly, while ingest is frozen.)
> 2. **THE REALITY CONCEPT WAS REWORKED (design-level, the deepest structural change since session 3).** The chain: **(a)** a "fact" = the book shut, decided, true-for-everyone — which is exactly what N.H must NOT make, because a fact stops being *subjective to Ness*, and the whole system is *his*, relative to *him* (הכל יחסי). **(b)** So there is no REALITY box of decided facts. "Real" is a **dial, not a box** — degrees of how-affirmed-something-is, revisable forever, with no "shut" at the top of the dial. **(c)** And the dial **belongs to people, not everyone-as-one** — reality-layers are PER-PERSON ("how real is this, *to whom*"), never collapsed into one shared truth; collapsing them is the forbidden move. **(d)** Therefore reality **leaves the storage spine and moves INTO the filter** — "how real, to whom" is a *reading the filter assigns*, an accreting layer, not a place a thing goes. **(e)** And **SIMULATION was always correctly named** — it is the create-space / workshop, where things get *made*; it never had an opposite. REALITY-as-fact-box was a *phantom* paired against a workshop — a category error (one was a place, the other a misfiled judgment). See the rewritten §1, the new §3G, and the §7A reality rules. (DESIGN; the built two-store gate still runs the old model — design-ahead-of-code, like the rest.)
> 3. **THE "WHY" RESOLVED — it is a NON-DECISIVE NOTE.** The §11C ban on a `why`/`reason` field was aiming at the wrong target. The danger was never the AI *reasoning* about why pieces connect — it was that reasoning *hardening into an asserted fact*. So the why is ALLOWED, as a **note**: the AI's own reasoning, pulled OUT of the chat response into a side surface (pop-up/panel) Ness opens on demand, and into the AI's own topic-sorted logs with the raw answer — **readable by Ness, write-only from the AI's side, decisive about nothing.** The AI MAY read and build on its own notes (full reasoning, Path A) — safety comes from *non-deciding*, NOT from blinding it. What stays forbidden is a `why` that *decides* (a closed fact in memory). See §7B note layer + §0. *(One honest enforcement flag: "the note never closes into fact" must be load-bearing; the note is a write-only sink toward memory — it informs Ness, it never auto-crosses into a decided layer.)*
> 4. **THREE READ-ONLY TOOLS BUILT (the *meanwhile* surfaces, like nh_peek).** **(a) `nh_log.py`** → emits `nh_log.html`, the §7B-Part-7 "mirror": a standalone clickable page that reads the store read-only and lays it out grouped by subject as **strata** (each seam's width = its real size), Hebrew/RTL rendered properly, content via `textContent` (never innerHTML, §8 rule), fully offline, point-back chips latent until `re_reads` exist. **(b) `nh_probe.py`** → read-only boundary-signal probe on a subject (length distribution, shape tells, apparent alternation). **(c) `nh_probe_truth.py`** → re-reads the gpt_purified SOURCE with the real `[NESS]:`/`[AI_RECALL]:` marker, gives TRUE alternation + calibrates shape-inference against ground truth. All three: read-only, write only their own output, discard when the real engine-backed surfaces ship. See §5/§6B/§11.
> 5. **THE SPEAKER QUESTION SETTLED ON GROUND TRUTH (issue 3 / schema item 2a) — and it's worse-then-better than recorded.** The store's gpt_purified **also dropped the speaker marker** (not just the JSON groups — the doc had implied the marker survived in content; on screen it does NOT). BUT the SOURCE file still has it, perfect. Ground-truth probe (every cross-check matched: 223 streams / 5,687 turns / NESS 2,803 / AI 2,884): **(a)** alternation is BROKEN and symmetric — only **27.9% flip**, NESS-NESS doubles 36.2%, AI-AI doubles 35.8% (Ness fires multiple short messages in a row; AI answers got split) → the detector must NOT assume turn-taking. **(b)** length is a POWERFUL signal — NESS median **9 words**, AI median **170**; words≤25→NESS **95.9%**, words≥60→AI **92.6%**, has-structure→AI **97.4%**. **(c)** "ends with ?" is a TRAP — only **31.8%** of question-enders are Ness (the AI asks questions constantly). **(d)** Throw the marker away and guess from shape → **90.6%** accurate on committed turns but **31.5% ambiguous** (the medium-length valley). **DECISION (evidence, not argument): the reading-layer schema CARRIES `role`, back-filled from the source — do NOT re-derive from shape** (it throws away ~1/3 of turns when perfect labels sit in the source for free); shape stays useful as a *boundary* vote (a big length jump = likely speaker change), never as the speaker *assignment*; and the detector must allow same-speaker doubling. See §11C-S9 + §11 item 2a.
> 6. **TUNNEL BLOCK NEUTRALIZED IN THE LIVE `C:\NH\` FILES (verified on disk).** `C:\NH\START.bat` and `C:\NH\silent_start.py` had their cloudflared-tunnel launch lines commented out behind a dated marker (`NH TUNNEL DISABLED 2026-06-21 - re-enable after nh_auth.py edits`); backups (`.bak`) made; backend + auth-proxy starts left intact. The tunnel auto-fire is now dead at THREE layers: Autoruns (task+service disabled, session 6), no `cloudflared.exe` on PATH, and now the block commented in-file. **Doc correction:** `silent_start.py` was NOT the "dead/inert" file §5 described — it had a live BASE path and a live tunnel block; the doc was describing the engine-core copy again. The tunnel CAPABILITY is still wanted (Phone Mode 1) — only the auto-fire was disabled. §11 item 12 is now mostly closed.
> 7. **DOC/CODE CONSISTENCY (item 11) CLOSED on disk.** `findstr` for "explicit approval" across `nh_engine_core\*.md` returned EMPTY (after stripping node_modules noise). No N.H reference doc carries the old framing; the old "explicit approval promotes to REALITY" language lived only in the retired `.cursorrules` v3.0, replaced by v3.1. Narrow caveat: differently-worded stragglers in a stray `.txt`/`.py` would be a 30-second delete, not a task. Item 11 = CLOSED.
> 8. **THE SPINE LINE (session 9, kept standalone):** *stop forcing the decision, and build a structure where not-deciding is safe — append-only is what makes not-choosing cost nothing; designed from how Ness works, not forced onto it (true on its own merit, seen because he lives it).* This is the same key as §0, aimed at the build instead of the AI.
> 9. **NEW OPEN ITEMS opened by the reality rework (WORK + one decision, none urgent, none an "issue").** (a) the REALITY/SIMULATION spine references across the doc + built code need reconciling to the new model — major but deferrable (frozen); (b) the built two-store gate now lags the design (a new, bigger design-ahead-of-code gap — harmless while ingest is frozen); (c) the premise→rule + spine-loses-concept eventually touch `.cursorrules` (protected-file-class, INCOMING not in-force); (d) **UNDESIGNED:** how to mark "things Ness leans on hard" (meds, dates) as a high-affirmation layer without it becoming a closed fact; (e) **OPEN DECISION (the one genuinely-owed question):** is **N.H itself** one of the people with a reality-layer stack (a perspective among perspectives, never above Ness), or do layers belong to humans only and the AI just records/reads them? (f) **OPEN QUESTION — register/mode (spotted, not thought-through):** how a composed WORK (story/article/poem, or internet text) is read vs a conversational TURN — "how it's told" includes "what form it was made in"; lives on or beside the intent web; axis-or-own-web unresolved. See §11.

> **PRIOR DELTAS (sessions 4–8) — kept in condensed form for continuity:**
> - **S8:** §13 THE LIVE LOOP (fire-and-let-go; deep side announces itself back; no worker count; deep search never blocks; parallel topics mechanically possible) + §14 THE CHAT FRONT DOOR (unconfirmed sketch — live chat as input, speaker carried, point-back the one shown thing, quiet surface, N.H never narrates its own mechanism) + the GUARD (the loop carries N.H's own output toward memory, safe ONLY as append-only proposal, never a REALITY crossing) + the design-to-fit-Ness compass (offer the shape, let Ness confirm the fit). Nothing built.
> - **S7:** the unit/segmentation problem DISSOLVED — a unit is a **span-claim, not a cut** (only adds depth, never loses data); "two places — dumb memory + fast calculator"; the "why" shown by pointers not written as a fact; the only span is `re_reads` across whole records; forced build order recorded (schema → detector probe → engine); four facts verified live on disk; issue 3 (JSON dropped the speaker) settled. Nothing built.
> - **S6:** data-rescue (A13 WhatsApp 2012→2024, encrypted, archived to PC+Drive, NOT ingested) + auto-start/tunnel hole found LIVE on disk and disabled via Autoruns + SETTLED: FREEZE INGEST. See §12.
> - **S5:** `nh_peek.py` built; JSON set + gpt_purified ingested (→11,374 / 4 groups); `cleaned_history (1).txt` set aside (structureless+damaged); no Gemini file on disk. §11B.
> - **S4:** accretive store skeleton built (`nh_accretive_store.py`, append-only); first 188 records; schema settled (+`content`,+`source_title`); §1A input-agnostic principle. §11A.

> **THE NAME:** He is **Ness** (male). Not "Nes," never "user." He signs his own name **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. **[BUILT]** = on disk today; **[DESIGNED]** = decided but not coded. The session-9 reality rework is **[DESIGNED]** — the built REALITY/SIMULATION gate still runs the OLD model. §3 lays out old→new; §6A is the in-force code rules; §0/§7A/§7B are the design.

> **THE ONE EXCEPTION TO "delete the rest":** the file Cursor actually obeys is `.cursorrules` on disk (`C:\Users\user\nh_engine_core\.cursorrules`) — must keep existing as its own file and stay identical to §6A.

---

## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule]

*Found session 9. This is the single premise every other rule in this file descends from. It is written first because it is the floor.*

**The line:** **The danger N.H exists to stop was never *reasoning* — it was reasoning *hardening into authority*: a living guess freezing into a closed, settled fact.** So the AI may reason fully — connect, guess, build on its own past reasoning, hold opinions, leave notes, get richer over time. It may do everything except one thing: **close the book on something into a decided fact.** Every conclusion stays a non-decisive, accreting layer; nothing it concludes ever promotes itself to "real."

**Why a fact is the forbidden thing:** a fact is *the book shut* — decided, done, no longer open, true-for-everyone. The moment something is a fact it is **no longer subjective to Ness** — and N.H is *his*, relative to *him* (הכל יחסי). A fact is the one thing he does not own, because facts claim to be true for everyone. So importing "facts" into his own private thinking system was always the wrong move; it was a freezer in a system whose whole soul is "nothing freezes."

**The crucial distinction (do not flatten it):** "never decide facts" does NOT mean "never hold anything firmly." Things still matter — enormously. Something can be held with full weight (a name, a date, a hard-won understanding) and **still never close the book.** The enemy was never weak-vs-strong; it was **open-vs-closed.** "Real" is *how strongly Ness holds something*, never *whether the book is shut*. There is no "shut" at the top of the dial. The firmest thing in N.H is still an open layer.

**What it permits and forbids, mechanically:**
- **Permitted (all create-side / filter-side, never a closed fact):** the AI reasons, connects, draws `re_reads` arrows (append-only layers — layers aren't facts), leaves notes (the why), reads its own past notes and builds on them (full reasoning — reading-and-building is not deciding), assigns reality-layers (how-affirmed, per person).
- **Forbidden (the one wall):** any AI conclusion *closing into a decided fact* / auto-crossing into a "this is now real for everyone" state without Ness. Hardening. Sealing. Collapsing per-person layers into one shared truth.

**Every other rule is this premise in a different place:** the membrane (§7A R7) = don't let *creation* close into fact. Accretion (§7A R6) = the structure that makes not-closing safe (a wrong layer can't corrupt what only ever adds). Non-decisive opinion / the note (§7B) = the AI reasons but decides nothing. Reality-as-per-person-reading (§7A reality rules) = "real" never collapses into one fact. **One premise, enforced everywhere.**

**Honest scope (Rule 12):** settled as DESIGN. The built code still has a REALITY store, a SIMULATION store, and a `promote_to_memory()` gate — it runs the OLD model harmlessly while ingest is frozen. The premise NAMES why that gate exists (only Ness opens it) and FORWARD-DIRECTS the engine build (full AI reasoning, all non-closing, reality as a per-person reading). It does not change the in-force `.cursorrules` (§6A); it joins the design rules (§7A) and the INCOMING block (§6A.12).

---

## 1. WHAT N.H IS (the corrected understanding)

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The core idea:** most AI lets outside opinion and automated judgment shape what you know before you ever see it. N.H inverts that — raw data comes in, and **nothing closes the book / becomes a decided fact by accident or automation** (§0).

**The two functions (NOT two truth-boxes — this was the session-9 correction):**
- **SIMULATION — the create-space / workshop.** Where things get *made*: the AI imagines, drafts, connects, plays. Correctly named from day one. It never had an opposite. **[BUILT as a store; reframed in design]**
- **"REALITY" as a box of decided facts — DISSOLVED in design (§3G).** It was a *phantom* paired against the workshop — a category error: one was a *place*, the other a *misfiled judgment*. "How real" is not a place a thing goes; it is a **reading the filter assigns** (§7A), per-person, layered, revisable, never closed. *(The built code still has a `.nh_reality_store.jsonl` + gate; that is the OLD model, design-ahead-of-code, harmless while frozen.)*

So: **there is no single REALITY.** There are **reality-layers that belong to people** — how-affirmed-is-this, *to whom* — recorded, never collapsed into one shared "fact." The collapse is precisely the forbidden move (§0).

**Where Ness's sovereignty lives (the corrected model):** not in clicking "approve" like a clerk (early framing, wrong — §3). It lives in being the **membrane**: by being present in the chat where the AI thinks, Ness is the threshold between where it imagines (chat) and where the system remembers (memory). The AI does the continuous reading and layering itself; **memory only ever adds, never overwrites**; the AI reasons fully but **decides no facts** (§0); Ness steers, and Ness is the only one who can move a reality-layer to maximum affirmation. He doesn't file — he is present at the threshold.

**The two purposes, always running together (the deepest "why"):**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside, the pattern he can't see because he's inside it. *(The §7B log and the why-note are this made openable.)*
- **OUTWARD — the engine:** take new external data and translate it through the specific lens of how *his* mind absorbs and connects things — not generic explanation, not retrieval.
A mind that runs alongside another mind, one looking inward, one looking outward, both at full speed. (The framing Ness wrote for his father. N.H is a thinking tool, not just a programming project.)

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED — front doors not built]

*Recovered session 4. Top-level principle: N.H is **input-agnostic.** Everything — text, images, video, audio — flows through the SAME one engine: read it across many webs of meaning (§7B), research inward + outward, log it read-only and subject-tagged, show it, let Ness steer. New input types do NOT get new engines; they need a new **front door** — a small model that turns that input into pieces the engine already reads.*

**How any input maps:** photo → front door produces plain description + metadata → pieces (§9A). Video → frames + audio + time → pieces. Audio → transcribe → text pieces. Text → already pieces (the only one with running code — the accretive skeleton §6B). The live chat itself is a front door (§14).

**The honesty line:** the engine is DESIGNED universal; in CODE today it handles only text, and only the accretive skeleton, not the full meaning engine. REAL as design, ASPIRATIONAL as code.

**The deepest "why" — הכל יחסי (everything is relative):** nothing about *meaning* is final — a thing means what it means only relative to ever-growing context, **and relative to whom** (the per-person reality-layers, §0/§7A). This is why memory only adds, why classification is never locked, why "unknown" is honest, and now why **reality is a per-person dial not a shared fact-box.** Held honestly even about itself: הכל יחסי applies to *meaning* (what things mean, who's in a photo, what was felt) — the front near-factual layers (the photo exists; EXIF date) stay near-factual. The open question of whether even those get a "lean-on-hard" marker is §11.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time** — never batch changes. He asks "why yes / why no" and wants real tradeoffs.
- **Verify on disk, never trust status reports.** `findstr`, `inspect.getsource()`, file reads. *(Session-9 proof: the doc implied gpt_purified kept the speaker marker in content — on screen it did NOT; and `silent_start.py`, called "inert," had a live tunnel block. Both caught by looking. Also session 9: the "explicit approval" doc-hole was already empty when checked — verify is checking, not pessimism.)*
- **Honest correction over flattery** — explicitly and repeatedly asked for. *(Session 9 ran on this: Claude proposed wrong walls — "blind the AI to its notes" — twice, and Ness corrected both; the real answer surfaced only by him rejecting half-right versions.)*
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, expressive punctuation are NOT distress. Frustration at the FLOW being broken (re-explaining, re-asking settled things, narrating the obvious) is real and fair.
- **He catches things.** When he pushes back, he is usually right.
- **He is not afraid of work.** A wall in front of him is almost never "this is hard" — it is "this move would *destroy* something." Diagnose blockers as *"what irreversible/lossy thing is this asking me to do?"* before reading them as reluctance.
- **Consistency is his stated hard spot — and he beat it by BUILDING the return.** The master + decision-defaults + verify-on-disk loop exist so that when flow breaks he can re-load the head from disk instead of climbing from nothing. He engineered the defense against his own failure mode into the project. Design for the lapse, don't pretend it won't come.
- **Design to fit how Ness thinks — held the honest way.** Offer the shape; let Ness confirm or correct the fit. Claude's read of his cognition is not authoritative — his is. The session's best realizations came from chasing the shape that fit him and from him rejecting half-right versions.
- **Primary risk pattern: scope expansion before consolidation.** Finish and verify what's in front before starting the next thing. (Second pattern: Claude re-opening settled questions as fresh — read what's decided before asking.)
- **Claude's role:** architecture, audit, security, strategy — the brain that checks the work. **Cursor** writes the code. Ness runs every command in cmd and verifies on disk. Claude never edits code directly. Ness calls this Claude role "JARVIS."
- **Session workflow:** one topic per chat; start fresh when a topic closes. End of session: tell Claude what was done → Claude generates new master + short delta → Ness reads the delta, swaps the file in the project.

---

## 3. THE EVOLUTION — OLD vs NEW (issues → solutions)

### A. The founding principle — manual gate → membrane
- **OLD:** "Ness explicitly approves each record to promote it to REALITY." Sovereignty = a per-record manual approval at `/review`.
- **ISSUE:** meaning is never final; manually freezing individual records does the exact thing the system says is false.
- **NEW:** **Memory only ADDS, never edits.** New context → add a new layer beside the old reading, never overwrite. Sovereignty becomes a **position (the membrane)**, not an action. **[DESIGNED principle; FIRST RUNNING CODE session 4 — append-only accretive store §6B.]**

### B. The "is this real?" paths — many inconsistent gates → one filter
- **OLD:** 4+ separate paths each decided "is this real" their own way; `_load_raw_sources()` tagged imported history REALITY by filename.
- **NEW:** **The Universal Filter** — ONE filter, every piece, no source exempt. The filter **sorts and prepares; it never closes the book** (§0). It assigns reality-*layers per person* (§3G), never one shared fact. **[DESIGNED — full rules §7A.]**

### C. AI creativity — silent writes → the membrane
- **OLD:** associative/generative capability could reach memory automatically.
- **NEW:** **The membrane** — bridging happens ONLY in chat (Ness present), structurally barred from *closing into a fact* in memory. A hallucinated re-reading is harmless because memory only accretes — a rejectable layer, never a corruption. *(Session-7 "two places — dumb memory + fast calculator." Session-9: the membrane is §0 applied to creation — create freely, never close.)*

### D. Concrete security holes found on disk → fixes  **[ALL BUILT & VERIFIED]**
- Sandbox SIGNAL auto-wrote to REALITY → routed to SIMULATION. · LLM output straight to REALITY → routes to SIMULATION + GENERATED. · HUD bound to all interfaces → `127.0.0.1`. · `/api/research_confirm` no token → gatekeeper token. · `nh_pc_agent.py` `run:` arbitrary-os.system → removed (`open:` kept). · `_load_raw_sources()` REALITY-tagging → stopped. · launcher loading `/chat` stub → fixed to root HUD. · **Cloudflare tunnel auto-launch** → block removed from engine-core copies (S-before-6); **⚠ found LIVE on disk session 6** in the scattered `C:\NH\` copies (task `\NH_Motherbase`→`START.bat` + `NHMotherbase` service); both DISABLED via Autoruns; **⚠ session 9: the tunnel block inside `C:\NH\START.bat` + `C:\NH\silent_start.py` is now COMMENTED OUT in-file (verified on disk, `.bak` backups made)** — auto-fire dead at three layers, capability still wanted for Phone Mode 1. · 5 sensitive routes → `NH_PROMOTE_TOKEN`. · `nh_sovereignty_sync.py` `StrictHostKeyChecking` → `yes`.

### E. Research pipeline — opinion-filtered black box → raw + controlled synthesis
- **NEW:** Brave (raw fetch) → OpenRouter/llama (one controlled synthesis) → SIMULATION → gate. **[DESIGNED — Brave not wired; §8.]**

### F. Doc/code consistency — **CLOSED session 9.**
- `.cursorrules` v3.0 carried old "explicit approval" framing; v3.1 replaced it. Session-9 `findstr` across `nh_engine_core\*.md` for "explicit approval" → EMPTY (node_modules stripped). No N.H reference doc carries the old framing. **Item CLOSED**, with the narrow caveat that a differently-worded straggler in a stray file would be a 30-second delete.

### G. The reality concept — REALITY-box of facts → per-person reality-layers in the filter  **[DESIGNED session 9 — the deepest structural change since session 3]**
- **OLD:** a two-layer spine, REALITY (decided/verified facts) vs SIMULATION (unverified), with `promote_to_memory()` the gate between them. "Real" = a box a thing earns its way into and sits, settled.
- **ISSUE:** this contradicts the project's soul (הכל יחסי / nothing closes) AND sovereignty. A "fact" shuts the book — decided, true-for-everyone — and the moment something is a fact it is **no longer subjective to Ness**, no longer *his*. The REALITY box was a freezer in a system whose whole job is to never freeze. It was tolerated from day one as "necessary"; it never was. SIMULATION, meanwhile, was *correctly* named — the create-space — and never needed an opposite. REALITY-as-fact-box was a phantom paired against a workshop (a place vs a misfiled judgment).
- **NEW / SOLUTION:** **"Real" is not a box — it is a reading the FILTER assigns** (§7A), with three properties: **(1) a dial, not a box** — degrees of how-affirmed, revisable forever, no "shut" at the top; **(2) per-person** — reality-layers belong to people ("how real, *to whom*"), never collapsed into one shared truth; **(3) non-closing** — the firmest layer is still open. SIMULATION stays as the create-space/workshop. **The premise §0 is the rule underneath: never close the book into a fact; never collapse per-person layers into one.**
- **STATUS:** DESIGN settled; **NOT propagated.** The built code still has `.nh_reality_store.jsonl` + `.nh_simulation_store.jsonl` + `promote_to_memory()` running the OLD model — harmless while ingest is frozen. Reconciling the spine across the doc + code is WORK (§11), not an issue. The §9 "according to whom" field (formerly a buried nice-to-have) is now the CORE SHAPE of reality.
- **OPEN under this:** (a) how to mark "lean-on-hard" things (meds/dates) as a high-affirmation layer without a closed fact; (b) **is N.H itself one of the people with a reality-layer stack** (a perspective among perspectives, never above Ness), or layers for humans only and the AI just records/reads them? — the one genuinely-owed decision.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 10 (10.0.26100.7840)
- **CPU** i5-11400 (40°C idle / 60°C load) · **GPU** RTX 2060 (35°C idle / ~40°C load) — both verified 24/7-safe
- **Launched via** `run_app.pyw` (the "N.H Interface" shortcut); starts `nh_app.py` silently, opens pywebview at `http://localhost:8080/`
- **Real interface:** `http://localhost:8080/` (root = full "MOTHERBASE AGENT" HUD, `index.html`). HUD redesign noted for later.
- **PC has ONE mode** — pywebview native window, local only, no browser, no internet. Browsers cache to disk; pywebview does not. *(This is why `nh_log.html` and other surfaces must be fully offline — no CDN/fonts.)*
- **Internet-facing surface:** a Cloudflare tunnel — currently **disabled at three layers** (Autoruns + no PATH binary + in-file block commented session 9); needed only for Phone Mode 1, opened deliberately with auth, never on startup.
- **Hardware limit:** a 70B model can't run locally. Front-door vision models must fit the 2060 (6GB VRAM).

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without dry-run + explicit "APPROVED"):**
`nh_memory_store.py` (`MemoryStore`, **`promote_to_memory()`** — the ONE authorized gate, OLD model) · `nh_context_router.py` (`ContextRouter.write()`; INFERRED-token check; NOT a gate alone) · `nh_reality_graph.py` (REALITY/SIMULATION/PREDICTION) · `nh_simulation_graph.py` (`promote_simulation_record()`/`reject_simulation_record()`) · `nh_epistemic_sandbox.py` (3 axes; SIGNAL→SIMULATION) · `nh_evidence_integrity.py` (`guard_write()` self-test only) · `nh_jarvis_core.py` (`run_nh_core_engine()` ~line 1076) · `nh_crypto.py` (AES-256-GCM) · `nh_vector_memory.py` (ChromaDB, `_load_raw_sources()`).
*(Session-9 note: this whole REALITY/SIMULATION gate stack is the OLD model §3G replaces in DESIGN. It still runs, harmlessly, while ingest is frozen. Do NOT rip it out before the new filter exists — that's the §11 reconciliation, a separate fresh-head move.)*

**Three physical memory stores (OLD model, still on disk):** (1) `.nh_memory_store.jsonl` (4 records, via `promote_to_memory()`). (2) `.nh_reality_store.jsonl`/`.nh_simulation_store.jsonl` (via router). (3) `.nh_simulation_graph.jsonl`/`nh_mental_network.json` (HUD server; only store with `/review`).

**Launchers:** `run_app.pyw` (real launcher) · `launch_nh.vbs` (secondary) · `nh_silent_start.py` in engine-core (dead BASE path, inert) · `nh_service.py` (`NHMotherbase` service — disabled via Autoruns session 6). **⚠ DISTINCT from the scattered `C:\NH\` copies:** `C:\NH\START.bat` + `C:\NH\silent_start.py` are the LIVE boot path; session 9 commented out their tunnel blocks (verified on disk, `.bak` backups beside them). These `C:\NH\` copies are the ones with teeth — the doc historically described the engine-core copies.

**Server/UI (safe to modify):** `nh_hud_server.py` (routes; `127.0.0.1`; 5 token-gated routes) · `nh_app.py` · HTML: `index.html`, `nh_chat.html` (stub), `nh_simulation_review.html`, `nh_speech_form.html`.

**Accretive store + tooling [BUILT & VERIFIED; store re-verified live session 7]:**
- `nh_accretive_store.py` — append-only layered store module. NOT wired to live flow/gates/ChromaDB. Exactly 8 functions; every `open()` is `"a"`/`"r"`, NO `"w"`. Public API: `append_root`, `append_reading`, `read_all`, `read_by_subject`. *(Session-9 re-read of the source confirms: 6-field record, NO `role` field — `_ALLOWED_KEYS` = id/subject/timestamp/content/re_reads/source_title.)*
- `.nh_accretive_store.jsonl` — 11,374 root records / 4 groups (002=188, 000=2,252, 001=3,247, gpt_purified=5,687), all `re_reads=[]`, ~14.5 MB.
- `nh_peek.py` — session 5, throwaway read-only CLI viewer.
- **`nh_log.py` — session 9, NEW.** Read-only; emits `nh_log.html` (the §7B-Part-7 "mirror"). Reads via `read_all()` only; writes only the HTML file; never touches the store. Standalone clickable page: groups by subject as **strata** (each seam's width = real size — the shape of the store at a glance), expand to read records content-first, Hebrew/RTL rendered per-line `dir=auto`, search across all records in-memory, `re_reads` rendered as point-back chips (latent until readings exist), content via `textContent` (never innerHTML — §8 rule), fully offline (no CDN/fonts — PC has no internet). ~13.5 MB output. Throwaway like nh_peek; discard when the real engine-backed log ships.
- **`nh_probe.py` — session 9, NEW.** Read-only boundary-signal probe on a subject (default gpt_purified): turn-length distribution, shape tells (ends-with-?, has-structure), best-effort speaker guess, apparent within-stream alternation. Inference only; prints, writes nothing.
- **`nh_probe_truth.py` — session 9, NEW.** Read-only GROUND-TRUTH probe: re-parses `gpt_purified_history.txt` keeping the real `[NESS]:`/`[AI_RECALL]:` marker; reports true alternation, length-by-true-speaker, single-feature reliability, and a shape-vs-truth confusion matrix. The tool that settled the speaker question (§11C-S9).
- `inspect_seeds.py`, `ingest_seeds.py` — read-only inspection + the ingest writer (two parsers: JSON walk `_iter_messages`, TXT `_iter_purified_turns`). *(Both parsers used `role` to walk and dropped it — the issue-3 lesson, now settled §11C-S9.)*

**Legacy stack (READ ONLY):** `nh_mental_network.json` + ChromaDB `nh_reality_core` + `nh_timeline.json` + `nh_nightly.py`. **New stack:** `MemoryStore → RealityGraph → ContextRouter → EpistemicSandbox`. **Accretive stack:** `nh_accretive_store.py → .nh_accretive_store.jsonl` + `nh_peek.py`/`nh_log.py`/`nh_probe*.py` + `ingest_seeds.py` — not wired to anything; the deliberate next-step bridge is §11.

**`.cursorrules` v3.1 (in-force):** full text §6A. UNCHANGED session 9. *(The premise §0 and reality-rework §3G are DESIGN — they join §7A and the §6A.12 INCOMING block, NOT the in-force §§0–11.)*

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- REALITY/SIMULATION two-layer gate (OLD model, still runs). · `promote_to_memory()` (one authorized gate; blocks GENERATED, INFERRED-without-token, REPORTED_SPEECH missing speaker/quote). · current gate flow (SIMULATION cards at `/review` → Promote/Reject). · REALITY-only vector index. · REPORTED_SPEECH (speaker+quote, encrypted). · encryption at rest · web results relabeled INFERRED · TEST_MODE · epistemic sandbox · working chat+HUD · silent auto-start disabled (Autoruns). · all §3D security fixes. · pywebview shows real HUD. · **the accretive store** (11,374 / 4 groups, append-only, re-verified live session 7). · **session-9 read-only tooling**: `nh_log.py`→`nh_log.html`, `nh_probe.py`, `nh_probe_truth.py` (all read-only, write only their own output). · **session-9 tunnel block commented out** in `C:\NH\START.bat` + `C:\NH\silent_start.py` (verified, `.bak` made).

**Known regression pattern:** the SIMULATION-routing fix has silently reverted before. Always re-verify on disk before building on it.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE)  [BUILT — governs running code today; UNCHANGED session 9]

*In-force ruleset Cursor must obey against the CURRENT system (the per-record manual gate). MUST stay identical to the canonical `.cursorrules` on disk. §§0–11 IN FORCE; §12 INCOMING (accretive/membrane direction, NOT in force). Session-9 note: the §0 premise and §3G reality-rework are DESIGN — they do NOT enter the in-force body; they extend §7A and the §12 INCOMING block. Do not write code against them until the new filter exists and Ness says it's active.*

**0 — IDENTITY.** Sovereign personal AI with strict memory-layer separation. Cursor proposes; Ness approves; Cursor implements. Never skip approval, even for "small" changes to a Protected File.

**1 — ABSOLUTE PROHIBITIONS** (no chat override). Never write code that: writes INFERRED/GENERATED into REALITY via `ContextRouter.write()` without `promote_to_memory()`; removes/weakens the GENERATED block; calls `remember()`/`promote_to_memory()` with `INFERRED` using a hardcoded/default token; writes directly to `nh_mental_network.json` (only `promote_simulation_record()`); merges SIMULATION into REALITY ChromaDB; labels web/synthesis output REALITY/VERIFIED; builds a second/parallel gating classifier; touches `.env`/`.nh_pin.json`/vault/`NH_PROMOTE_TOKEN`/keys/PIN; writes test/mock data into production stores.

**2 — THE ONE-GATE RULE.** Exactly one path into REALITY: `promote_to_memory()` — GENERATED always blocked; INFERRED needs `NH_PROMOTE_TOKEN` or explicit `user_confirmed=True`; VERIFIED direct; REPORTED_SPEECH direct but needs non-empty speaker+quote. `ContextRouter.write()` is NOT a gate alone. If about to write `_router.write(record)` where `record.layer==REALITY` and `status!=VERIFIED` — STOP, route through `promote_to_memory()`.

**3 — VERIFIED FILE MAP** (disk-confirmed): `promote_to_memory()`→`nh_context_router.py` · `guard_write()`→`nh_evidence_integrity.py` (no confirmed callers; treat as possibly dead) · `ContextRouter.write()`→`nh_context_router.py` · `MemoryStore.write()`/`remember()`→`nh_memory_store.py` · `promote_simulation_record()`→`nh_simulation_graph.py` · `_wire_research_to_network()`→`nh_hud_server.py` · `update_network_async()`→`nh_hud_server.py`.

**4 — THREE SEPARATE STORES.** (1) `.nh_memory_store.jsonl` (immutable). (2) `.nh_reality_store.jsonl`/`.nh_simulation_store.jsonl` (no `/review` reads the SIM one). (3) `.nh_simulation_graph.jsonl`/`nh_mental_network.json` (IS covered by `/review`). Confirm which store `/review` reads before writing a "pending review" record.

**5 — DUAL PIPELINE WARNING.** Two research pipelines live (`nh_hud_server.py` and `nh_research_engine.py`). Confirm which before extending; do not add a third.

**6 — DUAL STACK.** NEW: `MemoryStore→RealityGraph→ContextRouter→EpistemicSandbox`. LEGACY (read-only): `nh_mental_network.json`+ChromaDB+`nh_timeline.json`+`nh_nightly.py`.

**7 — PROTECTED FILES** (require "CONFIRMED: modify [filename]"): `nh_context_router.py`, `nh_memory_store.py`, `nh_evidence_integrity.py`, `nh_reality_graph.py`, `nh_epistemic_sandbox.py`, `nh_simulation_graph.py`, `nh_research_engine.py`, `nh_research_sandbox.py`, `nh_jarvis_core.py`, `nh_crypto.py`, `nh_auth.py`, the 5 store `.jsonl`s, `nh_mental_network.json`. Safe w/o extra confirm: `nh_viz_engine.py`, `nh_hud_server.py` (routes/UI only — its write functions count as Protected), `nh_mobile_bridge.py`, `nh_metrics_tracker.py`, `check_system.py`, `test_*.py`.

**8 — DRY-RUN PROTOCOL.** Before code touching a Protected File or write-path: output PROPOSED CHANGE (File / What / Store(s) / Gate function by exact name+file), wait for "APPROVED"; then full code (no placeholders), wait for "APPROVED" again.

**9 — CODE QUALITY.** No placeholders/TODO. No silent store-write failures (no bare `except: pass`). Schema validation for every `.jsonl` payload. Async store writes checked, not fire-and-forget.

**10 — PULL SOVEREIGNTY.** System pushes nothing unsolicited, auto-promotes nothing. No new autonomous task without `# AUTONOMOUS: approved by user [date]`. Re-enabling any silent auto-start/tunnel requires re-verifying the auth layer on disk.

**11 — BEFORE ANY NEW MEMORY FEATURE.** Check `nh_context_router.py`/`nh_memory_store.py`/`nh_simulation_graph.py`/`nh_evidence_integrity.py`/`nh_research_sandbox.py`; extend if close. Do not build a fourth parallel gate.

**REMINDER:** every shortcut around `promote_to_memory()` is a sovereignty violation. Propose, name the exact gate, wait for approval.

### 6A.12 — INCOMING (the accretive/membrane direction + the §0 premise + §3G reality-rework)  [NOT IN FORCE]
**Not live instructions.** Where the system is going; do NOT code against them until the new filter exists and Ness says active. Until then §§0–11 are law; conflicts resolve to §§0–11.
- **I0 — THE PREMISE (§0): never close the book into a decided fact.** The AI may reason fully and build on its own notes; it may NEVER close a conclusion into a fact or collapse per-person reality-layers into one shared truth. Safety = non-deciding, not blindness.
- **I1 — Memory only ADDS, never edits** (append-only, layered).
- **I2 — The membrane:** creation lives in chat, barred from *closing into fact* in memory.
- **I3 — One filter, no source exempt:** kills REALITY-by-filename.
- **I4 — Classification never locked** (re-readings are new layers).
- **I5 — Reality is a per-person filter READING (§3G), not a store of facts:** "how real, to whom," a dial not a box, never collapsed. The OLD REALITY store + gate are superseded by the filter when it ships.
- **I6 — Ness steers, doesn't file:** sovereignty = the membrane position; he is the only one who moves a layer to maximum affirmation. REPLACES per-record Promote/Reject — but only when built.
- **Reconciliation:** when the new filter + accretive flow ship, §§0–11 are rewritten to match (the membrane gate + reality-as-reading JOIN, don't silently replace, the one-gate rule); this INCOMING block collapses in.
- **Session-9 status:** the premise + reality-rework advanced the DESIGN; **no code written, store not wired, gate untouched** — §12 STILL INCOMING, §§0–11 STILL law. A dissolved/reworked concept does not change which rules are in force.

---

## 6B. THE ACCRETIVE STORE — SKELETON + SEED INGEST  [BUILT & VERIFIED; re-verified live S7; source re-read S9]

*The running code of the accretive/membrane direction. A deliberately dumb, standalone, append-only store — "keep memory dumb and safe, put the cleverness elsewhere" (§0/§3C). Wired to NOTHING by design.*

**Module — verified on disk:** 4 public functions (`append_root`, `append_reading`, `read_all`, `read_by_subject`) + 4 private; every `open()` is `"a"`/`"r"`, **no `"w"`**; schema validated before every append. Re-run `findstr "def "`/`"open("` at the start of any session building on it.

**Record schema (SIX fields):** `id` (uuid4) · `subject` (non-empty; provenance placeholder for seeds, e.g. `seed:gpt_purified`) · `timestamp` (ISO; **ingest** time, not when-said — original send-times mostly absent = honest unknown) · `content` · `re_reads` (list of ids; `[]` = root; non-empty = a re-reading layer pointing at earlier pieces — the accretion mechanism AND the only span N.H wants, ACROSS whole records, never inside one) · `source_title` (the source's own label, NOT the subject, NOT a claim). **NO `role`/speaker field** — confirmed in code session 9 (`_ALLOWED_KEYS`). The schema decision to ADD `role` (back-filled from source) is settled-as-input for the reading-layer schema, §11 item 2a.

**No `reason`/`why` field, by design (the why is a NOTE, not a stored fact — §0/§7B).** A `reason` field would be a place for a closed fact to live; barred. The "why" is shown by what a layer points at (the arrows) and kept as the AI's note outside the record (§7B note layer).

**In the store now:** 11,374 root records / 4 groups; all `re_reads=[]`. Append-only proven 4× on disk at ingest; total re-confirmed live S7.

**What it is NOT:** not wired to live flow, not a gate, no index, no segmentation, no meaning-engine webs, no confidence/unknown flags, no reality-layers yet. The smallest real thing that proves append-only layered memory works.

---

## 7. THE BIG DESIGN — FULL TEXT (UNIVERSAL FILTER + MEANING ENGINE)  [DESIGNED — not built]

### 7A — THE UNIVERSAL FILTER: OPERATING RULES (full)

*A ruleset. Any AI that reads/sorts/stores inside N.H must obey every rule. These supersede convenience, speed, and "being helpful."*

**RULE 0 — WHAT THIS SYSTEM IS.** A sovereign memory system: it stops outside opinion/automation from shaping what Ness knows before he sees it. You are a **reader and a layer-er**, not owner/author/judge. Final authority: Ness.

**RULE 0.5 — THE PREMISE (NEW, session 9): NEVER CLOSE THE BOOK INTO A FACT.** You may reason fully — connect, guess, build on your own past readings and notes, get richer. You may NEVER close a conclusion into a decided fact, nor collapse per-person reality-layers into one shared truth. Reasoning is free; *closing/deciding* is forbidden to you and reserved to Ness. Every rule below is this rule in a different place. (§0.)

**RULE 1 — ONE FILTER. EVERY PIECE. NO SOURCE EXEMPT.** FORBIDDEN: tagging anything by source/filename. "It was in the seed file" is never a reason.

**RULE 2 — THE FILTER SORTS / READS. IT NEVER CLOSES "REAL."** It sorts and prepares (למיין); it never closes the book. It assigns **reality-layers per person** (Rule 5.5), never one shared fact. The moment a filter can declare something real-for-everyone by itself, it rebuilds the auto-approval hole. **Filter reads. Human steers. Always.**

**RULE 3 — ONE CONTINUOUS READER, NOT TWO STAGES.** Finding where a piece begins/ends and naming its meaning-type are the same act. Don't pre-decide a fixed "unit." *(S7: the detector operationalizes this — a boundary is a span-CLAIM (a layer), so a wrong boundary only adds depth. S9: speaker-flip is a boundary VOTE only, never a speaker assignment — the speaker is carried, not guessed, §11C-S9.)*

**RULE 4 — MEANING FROM WIDE CONTEXT, NOT LOCAL WORDS.** Thin context → low-confidence by default; say so.

**RULE 5 — CLASSIFICATION IS NEVER LOCKED.** Every reading is provisional forever. Treat your own past classifications as revisable.

**RULE 5.5 — REALITY IS A PER-PERSON READING, NOT A FACT (NEW, session 9 — §3G).** "How real is this" is a reading you assign, with three properties: **(a) a dial, not a box** — degrees of affirmation, revisable, no "shut" at the top; **(b) per-person** — reality-layers belong to people ("how real, *to whom*"); record whose view it is, never collapse views into one; **(c) non-closing** — the firmest layer is still open. You never produce a fact. *(OPEN: whether N.H itself holds a reality-layer stack as a perspective; whether "lean-on-hard" items get a high-affirmation flag — §11.)*

**RULE 6 — MEMORY ONLY ADDS. IT NEVER EDITS. (KEYSTONE.)** New context → add a new layer beside the old, never overwrite/delete. N.H ACCRETES. FORBIDDEN: editing, overwriting, correcting-in-place, deleting, merging-away, "cleaning up." The only write is append. *(This is what makes never-closing SAFE — a wrong layer can't corrupt what only ever adds.)*

**RULE 7 — THE MEMBRANE: CREATION LIVES IN CHAT, NEVER CLOSES IN MEMORY.** Associative/bridging capability gets full freedom in chat and is barred from *closing into a fact* in memory. A hallucinated re-reading is harmless because memory only accretes — a rejectable proposal, never a corruption. *(S9: the membrane is §0 applied to creation. The why-NOTE (§7B) lives here: the AI reasons out loud / leaves a note, freely, deciding nothing.)*

**RULE 8 — WHICH OLD STATEMENTS GET RE-READ.** Use associative bridging as the relevance-trigger. Spurious links are acceptable (Rule 7) — rejectable layers, never corruptions.

**RULE 9 — HOW THE FILTER SORTS: BY MEANING-TYPE, IN A GROWING STRUCTURE.** Root distinction: *why it was said*, not surface form, not true/false. Candidate root types (~7, not final): state/claim · ask · wonder · express/feel · intend · report · imagine. A piece travels a route to a leaf, not a single label. *(OPEN, session 9 — register/mode: a piece's FORM — a composed WORK (story / article / poem Ness authored, or text from the internet) vs a conversational TURN — is "how it's told" too, and is NOT yet placed. Likely an axis on the intent web or its own thin web; spotted, not thought-through. §11.14g.)*

**RULE 10 — MAXIMAL-BUT-BOUNDED.** Small (~5, cap 7), grows by depth not width. Respect the current line; don't silently expand past it.

**RULE 11 — NESS'S ROLE: STEERER, NOT CLERK.** No per-record manual-approval workflow. The AI reads/re-reads/layers itself; no edits to approve because no edits (Rule 6). His sovereignty = standing authority to steer and override, and to be the only one who moves a layer to maximum affirmation. By being present in chat, Ness IS the membrane.

**RULE 12 — HONESTY ABOUT WHAT THIS IS.** TRUE: "a structured place for the AI to be creative without that creativity *closing into* what's permanent." FALSE/forbidden: that this "makes the AI think independently" or is "a new cognition." Never overclaim. *(S9 applications: "the reality model is rebuilt" would overclaim — the DESIGN is reworked, the code still runs the old gate. "The AI reasons freely now" is fine; "the AI decides what's real" is the forbidden thing it must never do.)*

**FAILURE MODES — STOP IF YOU CATCH YOURSELF:** (1) REALITY-by-source→R1. (2) closing something into real-for-everyone without Ness→R2/R0.5. (3) fixed-unit chopping→R3. (4) local-word classifying→R4. (5) treating a past classification as final→R5. (6) collapsing per-person reality-layers into one→R5.5. (7) editing/deleting memory→R6. (8) an associative leap closing into fact in memory→R7. (9) silently expanding past the line→R10. (10) per-record approval workflow→R11. (11) claiming independent thinking→R12. (12) a `reason`/`why` FIELD or an inside-a-record offset span→both reintroduce a closed fact or a cut; the why is a NOTE shown by pointers, the only span is `re_reads` across whole records. **When in doubt: filter reads, human steers; memory only adds; creation stays in chat; nothing closes into a fact.**

### 7B — THE MEANING ENGINE: THE MECHANISM (full depth)

**THE ONE-LINE SHAPE.** A piece runs through a **chain of webs** (each a real dimension of meaning), the engine fills each with *enough* info by researching inward (the person) + outward (the world) at night; what it can't fill, it **informs** Ness (never asks, never waits); everything is written to a **read-only, subject-tagged, permanent log** Ness can click through.

**PART 1 — CHAIN OF WEBS, RUN AS ONE.** Meaning is not one flat tag — it's what holds across all webs together. The category list (claim/ask/feel/…) is ONE web (intent), not the engine.

**PART 2 — THE REAL WEBS (research-grounded):** 1. INTENT (speech-act). 2. DEIXIS (anchor who/when/where; distance can be psychological). 3. COMMON GROUND (shared/assumed backdrop). 4. IMPLICATURE (Gricean maxims; a flout = the tell for sarcasm/irony). 5. THEORY OF MIND (model the mind behind it). 6. TIME/SEQUENCE (where it sits in the flow). 7. RE-READING (re-run later → NEW layer, never overwrite). *(…and more; the list is open; each new web must be a real grounded dimension.)*

**PART 2.5 — THE REALITY-LAYER WEB (NEW, session 9).** A web that assigns **how-affirmed-this-is, per person** (Rule 5.5) — a reading, not a verdict; a dial, not a box; never collapsed across people; never closed. This is where "reality" lives now (it left the storage spine, §3G).

**PART 3 — HOW THE WEBS COMBINE.** Separate lenses, one camera; light passes through all together, out comes one image. Richness = breadth across webs + the relationships between what lights up, NOT depth-drilling subcategories.

**PART 4 — NIGHTLY RESEARCH, INWARD + OUTWARD.** Fill missing webs by researching both directions at night. A piece is HELD while research runs; never forced through with gaps.

**PART 5 — HOLD UNTIL ENOUGH (not until perfect).** "Enough" is a movable threshold. Then the piece moves forward to become a reading (entering the create-space where Ness steers — *ready to show*, never *closed/true*).

**PART 6 — CAN'T FILL → INFORM, DON'T ASK.** If a web genuinely can't be filled: don't auto-stamp, don't stop and ask — **INFORM** (surface the specific gap by name), keep running. Ness is present, not required — a witness, free to steer anytime, never the bottleneck. Answers come back later as a NEW LAYER ("unknown on X → filled by Ness on Y"). "Unknown" is honest, valid, re-checkable. No failure mode.

**PART 7 — THE LOG (read-only, subject-tagged, permanent, clickable).** The surface through which Ness sees the engine's nightly mind. Read-only (accretion made visible — can't lie about its past). Seeing ≠ approving. Subject-tagged (the navigation layer that keeps infinite accretion usable). Permanent + findable. Clickable (subjects expand; entries open to show piece, webs, unknown-flags, layers, reality-layers over time). **Three things at once:** transparency, the mirror (INWARD), a permanent subject-indexed archive. *(Session-9: `nh_log.py`→`nh_log.html` is the throwaway stand-in that builds the SURFACE MECHANICS now — strata, expand, search, RTL — knowing it shows only `seed:` placeholder groups until real subjects exist (engine output). The real log replaces it.)*

**PART 7.5 — THE NOTE / THE WHY (NEW, session 9 — §0 resolution).** The AI's own reasoning — the *why* behind a reading or a connection — is a **non-decisive NOTE**, not a record field. It is pulled OUT of the chat response (the chat reads naturally; N.H never narrates its mechanism — §14) into: (a) a **side surface** (pop-up/panel) Ness opens on demand, copies, searches; and (b) the AI's own **topic-sorted logs** with the raw answer. Properties: **readable by Ness; write-only from the AI toward memory (the note never auto-closes into a fact/decided layer); the AI MAY read and build on its own past notes** (full reasoning — Path A; safety is non-deciding, not blindness). The note is the OUTWARD mirror pointed at the AI: Ness sees the AI's real meaning effortlessly, because the note is the AI's actual scratch, not a performance. *(Enforcement flag, §11: "the note never closes into fact" must be load-bearing — a write-only sink toward memory; if it ever feeds back as a decided layer, the §0 hole reopens. Held the disciplined way: navigable like the log, real scratch not theater.)*

**PART 8 — HOW THIS LOCKS INTO §7A:** webs=R3/R4; re-reading+layers=R6/R5; reality-layer web=R5.5; inform-don't-ask=R11/R7; hold-until-enough=anti-counterfeit; read-only log=accretion visible; the note=R7/R0.5 (creation in chat, decides nothing); don't overclaim=R12.

**TRUEST SENTENCE (engine):** One engine reads each piece across many real webs of meaning at once — including how-real-it-is-to-whom — researching the person and the world to fill them; what it can't fill it shows Ness without asking or waiting; the AI reasons fully and leaves its why as a note Ness can open; and everything is written, read-only and forever, into a log Ness can click through — so the engine looks outward while Ness looks inward, both at their own speed, meeting in a record that only ever grows and never closes.

### 7C — CAN IT BE BUILT? (honest)

The **accretive skeleton** is built (§6B, 11,374 records). Continuous re-reading is buildable as an approximation. The membrane makes it MORE buildable. **The unit/segmentation problem is dissolved** (S7): a unit is a **span-claim, not a cut** — only adds depth, no "wrong cut" to fear; the detector need only be good-enough-and-revisable because its mistakes are rejectable layers. The architecture FORCED this: `re_reads` pointers survive only if targets never move → a frozen fine substrate with meaning-spans floating above = boundaries-as-readings.

**WHAT REMAINS (ordinary build, not a paradox).** The detector is unbuilt and will be imperfect — fine. Cheap checks at each gap: **speaker flip** (now a boundary VOTE only — speaker itself is CARRIED from source, not guessed, §11C-S9), discourse-reset markers ("anyway/so/by the way"), topic shift (overlap/embedding distance). Count fired = boundary strength = confidence. *(S9 refinements: "ends with ?" is NOT a Ness tell — only 31.8% reliable; length IS a strong signal — NESS median 9 / AI median 170; the detector must allow same-speaker DOUBLING — true alternation is only 27.9%.)*

**THE FORCED BUILD ORDER (never re-fought):** **(1) reading-layer record shape** — where a computed reading (pointer + meaning + confidence + **role**/speaker, carried not derived, §11C-S9 + **per-person reality-layer**, §3G) lands; a §6A.8 store-touching schema decision; the ONE unblocking piece; **FRESH-HEAD, never tail-of-session.** → **(2) the detector** — read-only probe FIRST (like `nh_probe.py`/`nh_log.py` were). → **(3) the engine** — the full chain-of-webs; LAST. Wanting (3) doesn't move it up.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired]
Brave (raw) → OpenRouter/llama (one auditable synthesis) → create-space → gate. KEEP the OpenRouter key (Brave ≠ synthesis). Security: synthesis text-in/text-out only; fetched content framed as unverified raw, never instructions; **auto-reject never auto-delete**; rejected-bin "look don't touch" (URLs as plain text, render via `textContent` never `innerHTML`, strip invisible/RTL chars). Costs ~$120–300/mo vs old $6,000–13,500. Academic source OPEN (Semantic Scholar + OpenAlex, leaning both).

---

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]
**Access/auth:** Dry mode (default, no auth, no personal data) · Personal mode (PIN) · graduated step-up (fingerprint > PIN > voice-never-a-hard-lock) · raw-vs-derived dial · trusted-app-only, zero-copy. **Mobile (three modes):** Mode 1 Full (deliberate tunnel) · Mode 2 Local AI online (own memory) · Mode 3 Lite/offline · Manual Sync (fingerprint → review gate). Nothing auto-connects. **Interactive canvas** (icons not boxes; black=architecture, blue=solving). **Behavioral-baseline wellbeing** (Ness-vs-Ness; sensors as data-loggers FIRST). **HUD redesign** (later). **Multi-perspective "according to whom" field — PROMOTED session 9 from a buried nice-to-have to the CORE SHAPE OF REALITY (§3G/§7A R5.5):** reality-layers belong to people; this field is how the per-person dial is recorded. **Other unbuilt:** phone-data importer · memory browser · personality modeling · nightly scraper (all create-side) · voice in/out (Whisper→TTS) · ChromaDB cleanup (on hold) · folder cleanup.

## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED]
Camera reports plainly; meaning built where Ness is the membrane. Layers: (1) Metadata = near-fact (EXIF). (2) Plain-description/object layer = low-opinion w/ confidence (object-detection model, not a narrating VLM) → create-side. (3) Context-meaning = interpretation, a re-reading layer → create-side, never closed. (4) Ness confirms → a layer (or honest "unknown"). The AI's opinion is never banned — it's **caught as a non-decisive opinion** (a reading w/ confidence, dated, a layer), exactly §0. Fits the 2060 (small detection models, PaddleOCR-VL/SmolVLM-class).

---

## 10. ORIGINALITY (honest calibration)
Every brick exists somewhere; the **combination** ships nowhere. Nearest cousins: memorywire (drifts to auto-approve, recall ungated) and SSGM (automated gate). Claim the combination + the inverted default (mandatory non-bypassable human role + REALITY-only index + cognitive-sovereignty framing) — and now the **per-person, never-closing reality model** (§3G) as a further distinctive. Never claim inventing local AI or approval gates. *(Verify arXiv IDs before leaning publicly.)*

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ SKELETON + DATA + re-verified live. Sub-items: (a) `nh_peek.py` ✅, **`nh_log.py`→`nh_log.html` ✅ session 9** (the §7B-Part-7 mirror surface mechanics — strata/expand/search/RTL; shows `seed:` placeholders until real subjects exist); the real engine-backed log still later. (b) seed ingest ✅ DONE (cleaned_history set aside; no Gemini). (c) **wire the store into live flow** — STILL OPEN; the heaviest move; triggers §6A.12 reconciliation; explicitly next-session, never tail.
2. **THE FORCED ORDER — reading-layer schema → detector → engine (none started):** **(2a) reading-layer record shape** — fresh-head, store-touching. **Now carries two settled inputs:** it must hold **`role`/speaker** (back-filled from source, NOT re-derived — §11C-S9) and a **per-person reality-layer** (§3G/§7A R5.5). → **(2b) detector** — read-only probe FIRST (the `nh_probe*.py` were the first such probes); must allow same-speaker doubling; length is the strong signal, "?" is not. → **(2c) engine** — LAST.
3. **Image-ingest front door (§9A).**
4. **Universal Filter / meaning engine** — unit dissolved (§7C). **STANDING DECISION: INGEST FROZEN** until the engine exists. WhatsApp (§12) archived-and-waiting.
5. **ChromaDB cleanup** — on hold.
6. **Research pipeline build** — Brave + academic source + security defaults.
7. **Hetzner sovereignty sync** — server + fingerprint + auth before enabling.
8. **`nh_service.py` registration** — ✅ RESOLVED session 6 (disabled via Autoruns). Autoruns is the authoritative check.
9. **Mobile companion + canvas.**
10. **HUD redesign** — after store + filter.
11. **Doc/code consistency (§3F)** — ✅ **CLOSED session 9** (disk-empty for "explicit approval"; old framing lived only in retired v3.0).
12. **Folder cleanup** across the three scattered locations — ✅ **mostly done session 9**: tunnel block in `C:\NH\START.bat` + `silent_start.py` commented out (verified, `.bak` made). Remaining: full cleanup of scattered copies when convenient.
13. **WhatsApp archive → eventual ingest (deferred):** decrypt `.crypt14` → SQLite front door → child-data call → ingest only with engine. Carry the sender this time (issue-3 lesson).
14. **★ NEW session 9 — the reality-rework consequences (WORK + one decision; none urgent, none an issue; all deferrable while frozen):**
    - **(a) Spine re-draw:** reconcile REALITY/SIMULATION references across the doc + code to the §3G per-person-reality-layer model. Major, fresh-head.
    - **(b) Code gap:** the built two-store gate now lags the design (design-ahead-of-code; harmless while frozen). Do NOT rip out the old gate before the new filter exists.
    - **(c) `.cursorrules` reconciliation:** the §0 premise + §3G want to eventually enter the code law; INCOMING (§6A.12 I0/I5), not in-force; a protected-file-class move when the filter ships.
    - **(d) UNDESIGNED — "lean-on-hard" marker:** how to mark things Ness leans on hard (meds, dates) as a high-affirmation layer without a closed fact. Design work.
    - **(e) ★ OPEN DECISION (the one genuinely-owed question):** is **N.H itself** one of the people with a reality-layer stack (a perspective among perspectives, never above Ness), or are layers human-only and the AI just records/reads them? Changes how the filter is built. Top-of-session decision.
    - **(f) Enforcement flag:** "the note never closes into fact" (§7B Part 7.5) must be made load-bearing in the eventual build — a write-only sink toward memory.
    - **(g) ★ OPEN QUESTION — register / mode (spotted session 9, NOT thought through):** how is a *composed work* (a story, an article, a poem Ness authored, or text pulled from the internet) read by the filter — as distinct from a conversational TURN? "How it's told" should include *what form it was made in* (story / article / poem / offhand line). Likely lives on or beside the intent web (§7A R9 / §7B web 1) — **open whether it's an axis on the intent web or its own thin web.** Not designed, not pressure-tested — located only. A composed WORK is a different animal than a turn-in-a-stream; the filter currently treats everything as utterances and does not distinguish "Ness *wrote* this as a work" from "Ness *said* this in a chat." Fresh-head turn-it-over, like the reality rework was.

---

## 11A. SETTLED SESSION 4 — STEP-2 SEED-INGEST DECISIONS  [BUILT for 002; pattern set]
Unit = per-message (finest non-interpretive boundary the file gives — too-coarse can't be undone, too-fine can get a coarser layer added later). Subject = honest provenance placeholder. The ChatGPT `title` is NOT the subject (it's frozen at the chat's START — proven: "דרכי סיוע משפטי" → mostly housing); rides in `source_title`. Read-only on sources. General principle: for a provisional step, pick the choice that destroys the least and keeps every option open. *(S7: finest-boundary turned out load-bearing — the frozen fine substrate `re_reads` needs.)*

## 11B. SETTLED SESSION 5 — TXT-SEED DECISIONS  [BUILT for gpt_purified; cleaned_history set aside]
`gpt_purified` → per-turn on role markers; stream label → `source_title`; role-marker stripped from content; validated by dry-run sample, not raw count. `cleaned_history (1).txt` → DELIBERATELY NOT INGESTED (0 structure + damaged; any parser would invent boundaries — forbidden). The discipline includes knowing when NOT to ingest. *(S9 correction: "role marker stripped INTO content" was the doc's claim, but on-screen the markers are GONE from the store content too — see §11C-S9; the doc was imprecise. The store kept neither a `role` field NOR the in-content marker; only the SOURCE file has the marker.)*

## 11C. SETTLED SESSION 7 — UNIT DISSOLUTION + LIVE VERIFICATION  [DESIGN settled; FACTS verified]
Unit = span-claim not cut → only adds depth → detector need only be good-enough-and-revisable. Two places (dumb memory + fast calculator). The why shown by pointers, never a `reason` field. Only span = `re_reads` across whole records. Forced build order. The wall was never fear of work — it's refusal of a destructive move. Four facts verified live (11,374; 188/2,252/3,247/5,687; 8 functions no-`"w"`; `.cursorrules` v3.1 §12 NOT IN FORCE). Issue 3: JSON dropped the speaker.

## 11C-S9. SETTLED SESSION 9 — THE SPEAKER QUESTION (GROUND TRUTH)  [DESIGN settled; nothing built]
*The reading-layer schema's speaker question (item 2a / issue 3), settled with ground truth from `nh_probe_truth.py`. Cross-checks all matched: 223 streams / 5,687 turns / NESS 2,803 / AI 2,884.*
- **The store dropped the speaker on gpt_purified too** — no `role` field AND no in-content marker (worse than the doc implied). The SOURCE file still has the `[NESS]:`/`[AI_RECALL]:` marker, perfect.
- **Alternation is broken and symmetric:** flip 27.9%, NESS-NESS double 36.2%, AI-AI double 35.8%. Ness sends multiple short messages in a row; AI answers got split. **The detector must NOT assume turn-taking.**
- **Length is a powerful speaker signal:** NESS median 9 words, AI median 170. words≤25→NESS 95.9%; words≥60→AI 92.6%; has-structure→AI 97.4%.
- **"Ends with ?" is a TRAP:** only 31.8% of question-enders are Ness (the AI asks questions constantly).
- **Shape-vs-truth:** 90.6% accurate on committed turns, but 31.5% ambiguous (the medium-length valley).
- **DECISION (evidence): the reading-layer schema CARRIES `role`, back-filled from the source. Do NOT re-derive from shape** (throws away ~1/3 of turns when perfect labels sit in the source for free). Shape stays a *boundary* vote (length jump = likely speaker change), never a speaker assignment. Detector must allow same-speaker doubling.
- Also closed: 204-vs-223 streams was Claude's coarse store-grouping (same-titled streams merged), not a parse bug — source has 223, confirmed by `findstr`.

## 11D-S9. SETTLED SESSION 9 — THE PREMISE + THE REALITY REWORK  [DESIGN settled; nothing destructive on disk]
- **The premise (§0):** never decide facts / never close the book. The danger was reasoning *hardening into authority*, never reasoning itself. The AI reasons fully and may read its own notes; it never closes a conclusion into a fact. Safety = non-deciding, not blindness. Resolves the §11C `why`-field ban: the why is allowed, as a non-decisive note (§7B Part 7.5).
- **Things still matter / nothing closes:** the enemy is open-vs-closed, not weak-vs-strong; the firmest layer is still open; no "shut" at the top of the dial.
- **Reality reworked (§3G):** no REALITY box of facts. "Real" is a per-person, layered, revisable READING the filter assigns ("how real, to whom"), never collapsed into one shared fact. SIMULATION was always correctly named (the create-space); REALITY-as-fact-box was a phantom paired against a workshop.
- **Reality moves from the storage spine INTO the filter** (§7A R5.5 / §7B Part 2.5). The §9 "according to whom" field is now the core shape of reality, not a side-feature.
- **Status:** all DESIGN. The built REALITY/SIMULATION gate code is untouched and still runs the old model (design-ahead-of-code, harmless while frozen). The propagation is WORK (§11.14), not an issue. One genuinely-owed decision opened: is N.H itself a perspective with reality-layers (§11.14e)?

---

## 12. SESSION 6 — THE DATA-RESCUE OPERATION (NOT an N.H change)  [recovery done; ingest FROZEN]
A13 WhatsApp 2012→2024 (age 7 → 2024), the first-ever account, lost from cloud, surviving only on a phone Ness nearly threw away. Message DBs (`msgstore.db.crypt14` + dated backups, ~118 MB, **still ENCRYPTED**) + media → copied to PC (`C:\Phone_A13_Backup`) + Drive (`Whatsapp_Archive_A13`). A24 + A13 general media backed up too. The auto-start/tunnel regression found LIVE and disabled via Autoruns (the `C:\NH\` copies, not the engine-core ones the doc tracked). **SETTLED: ingest FROZEN** — archive now, ingest deliberately later. Reasons (the freeze STANDS even though the unit problem dissolved and reality was reworked): engine not built + media front door unbuilt + child-data one-way-door call unmade + no-engine-means-no-insight. When it enters N.H: decrypt → SQLite front door (`_iter_whatsapp_messages()`, carry the sender — issue-3 lesson) → child-data call → ingest. The most "Ness" data N.H will ever hold.

---

## 13. THE LIVE LOOP — HOW N.H RUNS WITHOUT EVER STALLING  [DESIGNED — not built]
*Session 8. Concept only, nothing on disk. Does NOT reorder the forced build (§7C/§11).*
A figure-eight, two parts, cache outside. **Cache** (outside the loop) decouples chat-speed from loop-speed. **Part 1 — the starter — FIRE-AND-LET-GO (keystone):** picks up from cache, hands to the deep side, turns free in the same instant; never holds/waits, only launches. **Part 2 — the deep side** (memory · filter · reasoning · deep search): each job on its own clock, in parallel, **announces itself back** when done. **No "worker count"** — a count is a ceiling; the principle is "no hand ever holds still." **Two consequences:** (1) deep search never blocks (just another deep-side job); (2) parallel topics mechanically possible. **Locks in:** it's §0/§3C/§7A R7 from the runtime side — the deep side computes fast, the append-only store under it stays dumb and safe, so a fast wrong reading is a rejectable layer never a corruption; fire-and-let-go is safe *because* the store only ever appends/never closes. Precondition for voice. Honest edges: nothing coded (widgets were browser concept-demos); the hard part is the engine that runs INSIDE the loop (§7C 2c), which doesn't exist.

---

## 14. THE CHAT FRONT DOOR — A WORKING DESIGN SKETCH  [DESIGNED-IN-PROGRESS — NOT confirmed, not built]
*Session 8. Ness did NOT confirm it; recorded so it isn't re-derived.* The live chat is itself an input (a front door, §1A) — Ness↔N.H recorded, speaker known and CARRIED (issue-3 lesson), connect-not-claim. Two-filter path (AI creation filter → meaning filter) riding §13 — the creation-filter-vs-mode split is the loosest part. The **point-back** is the one thing shown in chat (clickable `re_reads` made visible — navigation not narration). The quiet surface: no recording badge; tap-to-reveal errors; **N.H NEVER narrates its own mechanism** (this is why the why is a side NOTE, §7B Part 7.5, not woven into the chat). **THE GUARD:** the §13 loop carries N.H's own output toward memory — safe ONLY as an append-only proposal, never a closing/REALITY crossing (memory→chat = harmless READ; chat→memory = GUARDED write that can never auto-close into fact — §0). FROZEN like all ingest; capture decision (always-on vs deliberate-keep) is an unresolved one-way-door / child-data-flavored question needing Ness.

---
**CLOSING PRINCIPLES**
Evidence over narrative (verify on disk — proven AGAIN session 9: the store dropped the gpt_purified speaker the doc implied it kept, and `silent_start.py` had a live tunnel block) · one concrete step at a time · **NEVER DECIDE FACTS — never close the book; the danger was reasoning hardening into authority, never reasoning itself (§0)** · **a fact stops being yours — everything in N.H is yours, subjective, relative-to-Ness; so there is no fact-box (§3G)** · **reality is a per-person dial not a shared box — "how real, to whom," held in the FILTER, never collapsed, never closed (§3G/§7A R5.5)** · **SIMULATION was always the create-space; REALITY-as-fact was a phantom paired against a workshop** · **the why is a non-decisive NOTE — the AI reasons fully, reads its own notes, decides nothing (§7B Part 7.5)** · memory only adds, never edits · the membrane (creation in chat, never closes in memory) · two places: dumb memory + fast calculator · a unit is a span-claim not a cut · the why shown by pointers, never a `reason` field, never an offset-span inside a record · input-agnostic: one engine, many front doors · archive don't ingest · הכל יחסי — meaning is relative, revisable, AND relative-to-whom; brute fact is the only near-exception (and even it may only get a "lean-on-hard" layer, not a closed fact — OPEN) · the AI WILL interpret — catch it as a dated, confidence-tagged, non-closing opinion · don't overclaim (the reality model is reworked in DESIGN; the code still runs the old gate) · **carry the speaker, don't guess it (§11C-S9)** · the chat never waits because no hand ever holds still (§13) · design to fit how Ness thinks — offer the shape, let him confirm the fit · the live chat is itself an input (§14, unconfirmed) · THE GUARD: the fast loop must never become a closing/REALITY-write path · **a blocker dissolving or a concept reworking as DESIGN is real progress even with zero destructive disk change — but it must be recorded, because a thinking session leaves nothing on disk to re-derive from** · **the spine line: stop forcing the decision, build a structure where not-deciding is safe — designed from how Ness works, not forced onto it.**

### TRUEST SINGLE SENTENCE
N.H gives the AI a place to reason and create freely (the chat) where Ness is present to steer it, and a memory that only ever adds and never closes the book — so meaning, and how-real-something-is-to-each-person, can keep evolving forever without anything hardening into a fact that pretends to be true for everyone. It is subjective, it is a tool not a world, it was never about escaping reality — it is about refusing to let reality be counterfeited, and refusing to ever shut the book.
