# N.H — MASTER (complete, self-contained, full depth)
### The single N.H system reference. Everything — system, status, the filter rules, the meaning engine, AND the code rules — is written out IN FULL below at the depth of the original source files. Nothing is referenced-only.
*Rebuilt June 20 2026 (session 3) from a full read of all project files; updated session 4 (also June 20 2026) — this is MASTER-8. MASTER-8 adds the FIRST RUNNING CODE of the accretive design: the append-only accretive store is now BUILT and verified on disk, and the first real data (188 ChatGPT messages) is ingested into it. It also adds a recovered top-level principle (§1A — input-agnostic: one engine, many front doors) and the worked image-ingest example (§9A). This file embeds, at full depth: the complete Universal Filter rules (§7A), the complete meaning-engine mechanism — all 8 parts (§7B), and the full in-force code ruleset `.cursorrules` v3.1 (§6A). It is designed to be THE only document — the companion files (`NH_Universal_Filter_RULES.md`, `NH_Meaning_Engine_Design.md`, project `cursor_rules`) are now fully contained here and can be retired. About the N.H system ONLY — nothing about the anime.*

> **WHAT CHANGED IN SESSION 4 (the short delta — read this first):**
> 1. **§11.1 is now partly BUILT, not just designed.** `nh_accretive_store.py` exists, is append-only, verified on disk (only `"a"`/`"r"` file opens; four public functions; no edit/delete/overwrite). This is the first time the accretive/membrane direction (§3A, §6A.12, §7) has running code.
> 2. **First seed data ingested.** 188 messages from `conversations-002.json` (the smallest JSON seed, 23 conversations) are in `.nh_accretive_store.jsonl` as root records. Clean, verified, `re_reads=[]`.
> 3. **Record schema settled with TWO fields beyond §11.1's original four:** `content` (the piece itself) and `source_title` (the source's own label, e.g. a ChatGPT conversation title — kept as data, explicitly NOT the subject).
> 4. **Step-2 unit decision settled** (see §11A): per-message for JSON seeds; `subject` = honest provenance placeholder (`seed:conversations_002`); the ChatGPT title is NOT the subject (it's a frozen first-message snapshot — using it as subject would rebuild the exact "meaning fixed at the start" error the system exists to kill). Real subject is earned/added later as a layer.
> 5. **New top-level principle (§1A): N.H is input-agnostic — one engine, many front doors.** Recovered this session. Text/image/video/audio all flow through the SAME meaning engine; new input types only need a new "front door" (a small model that turns the input into pieces the engine can read). Images are the first worked example (§9A). **[DESIGNED — front doors not built; engine itself is still only the accretive skeleton in code]**

> **THE NAME:** He is **Ness** (male). Not "Nes," never "user." Older files wrongly recorded "prefers Nes" — a persistent cross-session error. He signs his own name **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. The system **as it currently runs on disk** works one way; the system **as now designed** works another. This file marks both honestly — **[BUILT]** = on disk today, **[DESIGNED]** = decided but not coded. §3 lays out the old→new shift. §6A is the in-force code rules; §7A/§7B are the full design.

> **THE ONE EXCEPTION TO "delete the rest":** the file Cursor actually obeys is `.cursorrules` on disk (`C:\Users\user\nh_engine_core\.cursorrules`) — that must keep existing as its own file regardless, and must be kept identical to §6A. Everything else (the project-copy reference files) is safely absorbed here.

---

## 1. WHAT N.H IS (the corrected understanding)

N.H ("Jarvis") is a personal, sovereign AI memory system running locally, 24/7, on Ness's own Windows machine. Not a product — infrastructure for his own thinking, memory, and research.

**The core idea:** most AI lets outside opinion and automated judgment shape what you know before you ever see it. N.H inverts that — raw data comes in, and **nothing becomes "real" by accident or automation.**

**Two layers (the spine, enforced in code, not convention):**
- **REALITY** — what has earned its place; the verified layer. It doesn't change on its own.
- **SIMULATION** — unverified, AI-generated, inferred, or not-yet-reviewed; where everything starts.
Nothing crosses from SIMULATION into REALITY automatically or silently. *(How that crossing happens is itself mid-evolution — old mechanism vs new model laid out in §3.)*

**Where Ness's sovereignty actually lives (the corrected model):** not in clicking "approve" on each record like a clerk — that was the early framing, and it was wrong (see §3). It lives in being the **membrane**: by being present in the chat where the AI thinks, Ness is the threshold between where it imagines (chat) and where the system remembers (memory). The AI does the continuous reading and layering itself; **memory only ever adds, never overwrites**; Ness steers and overrides. He doesn't file — he is present at the threshold.

**The two purposes, always running together (the deepest "why"):**
- **INWARD — the mirror:** show Ness the shape of his own thinking from the outside, the pattern he can't see because he's inside it.
- **OUTWARD — the engine:** take new external data and translate it through the specific lens of how *his* mind absorbs and connects things — not generic explanation, not retrieval.
A mind that runs alongside another mind, one looking inward, one looking outward, both at full speed. (This is the framing Ness wrote for his father — the real point. N.H is a thinking tool, not just a programming project.)

---

## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED — front doors not built]

*Recovered session 4. This is a top-level principle, not a feature. It does not commit any code — it tells future-Ness, future-Cursor, and future-Claude HOW any new input type gets handled when the time comes, so each one is not re-designed from scratch (which is the project's standing scope-creep risk, §2).*

**The principle, in one line:** N.H is **input-agnostic.** Everything — text, images, video, audio, anything later — flows through the SAME one engine: read it across many webs of meaning (§7B), research inward + outward, log it read-only and subject-tagged, show it, let Ness steer. New input types do NOT get new engines. They only need a new **front door** — a small model that turns that input into *pieces the engine can already read.* The engine is already universal by design; only the front doors get added over time.

**Why this matters (the anti-sprawl guarantee):** without this written down, every new input type *feels* like a new subsystem to design from zero — and that is exactly the failure mode the master warns about (building a fourth/fifth parallel thing). With it written down, the answer to "how do we do video?" is permanently *"same as everything — just a front door."* Nobody re-derives it. It protects the hard thinking already done.

**How any input maps to the engine:**
- A **photo** → front door produces a plain description + metadata → those become pieces → same engine (worked example in §9A).
- **Video** → frames + audio track + time → front door turns it into pieces (described frames, transcribed speech, timestamps) → same engine.
- **Audio / voice** → transcribe (Whisper, already noted §9) → text pieces → same engine.
- **Text** → already is pieces → straight into the engine (this is the only one with running code today — the accretive skeleton, §6B).

**The honesty line (do not overclaim):** the engine is **designed** to be universal; in CODE today it handles only **text**, and even that is only the accretive *skeleton* (§6B), not the full meaning engine. So this principle is REAL as design, ASPIRATIONAL as code. State it that way always. This is the same [BUILT]/[DESIGNED] discipline as the rest of the file — keeping the line honest is what stops "one engine for everything" from becoming a lie.

**The deepest "why" under it — הכל יחסי (everything is relative):** N.H is built on the premise that nothing about *meaning* is final — a thing means what it means only relative to the ever-growing context around it. That single idea is why memory only adds (the old reading was true *relative to what was known then* — deleting it would lie about that), why classification is never locked, why the camera only describes plainly while *meaning* comes from context, and why "unknown" is an honest state. **Held honestly even about itself:** הכל יחסי applies to *meaning* (what things mean, who's in a photo, what was felt) — NOT to brute fact (the photo exists; this was typed June 20; EXIF date). N.H respects that line: near-factual front layers stay near-factual; only the interpretation is relative. Even "everything is relative" is applied relatively — where it's true, not as a slogan.

---

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time** — never batch changes. He asks "why yes / why no" and wants the real tradeoffs, not just a recommendation.
- **Verify on disk, never trust status reports.** `findstr`, `inspect.getsource()`, file reads. This has caught real regressions repeatedly. "Applied" is never "verified." *(Session 3 proof: a reconstructed rules list matched the real on-disk file on the anchored rules but got the reconstructed middle rules wrong — only the disk file was right.)*
- **Honest correction over flattery** — explicitly and repeatedly asked for.
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, expressive punctuation are NOT distress or confusion.
- **He catches things.** When he pushes back, he is usually right.
- **Primary risk pattern: scope expansion before consolidation** — names a principle, builds something that quietly violates it, catches it by evidence, fixes it, then expands again before verifying the current layer. Finish and verify what's in front before starting the next thing. *(A second pattern seen in session 3: Claude re-opening already-settled questions as if fresh — read what's decided before asking.)*
- **Claude's role:** architecture, audit, security, strategy — the brain that checks the work. **Cursor** writes the code. Ness runs every command in cmd and verifies on disk. Claude never edits code directly. Ness calls this Claude role "JARVIS."
- **Session workflow:** one topic per chat, start fresh when a topic closes. End of session: tell Claude what was done → Claude generates new master file + short delta → Ness reads the delta, swaps the file in the project.

---

## 3. THE EVOLUTION — OLD vs NEW (issues → solutions)

This is the heart of where N.H is right now. Each row is a thing the early design got wrong (or a hole found on disk), what the problem was, and the decided fix. **Some fixes are built; some are designed-not-built — marked per row.**

### A. The founding principle — manual gate → membrane
- **OLD:** "Ness explicitly approves each record to promote it to REALITY." Sovereignty = a per-record manual approval action at `/review`.
- **ISSUE:** Meaning is never final — wide, growing context keeps recoloring what a statement meant. Manually freezing individual records by hand does the exact thing the system says is false. Ness *felt* this before he could name it; it's why something in him rejected manual sorting. Two beliefs were fighting: "I must be the gate" (sovereignty) vs "nothing is ever final" (meaning keeps moving).
- **NEW / SOLUTION:** **Memory only ADDS, never edits.** New context → add a new layer beside the old reading ("read against this new context, it now means this"), never overwrite. This dissolves the contradiction: meaning stays revisable (new layers), nothing is destroyed (old layers remain), and Ness stops being a clerk (no edits to approve — only accumulation). Sovereignty becomes a **position (the membrane)**, not an action. **[DESIGNED — the principle; FIRST RUNNING CODE as of session 4 — the append-only accretive store `nh_accretive_store.py` now exists and enforces "append only, never edit" at the file-handle level (§6B). The built system's LIVE path still uses per-record Promote/Reject — see row B and §6 — but the accretive direction is no longer paper-only.]***

### B. The "is this real?" paths — many inconsistent gates → one filter
- **OLD:** 4+ separate paths each decided "is this real" their own way: epistemic sandbox scored typed thoughts; `_load_raw_sources()` tagged imported ChatGPT/Gemini history as REALITY **by filename** with no review; the research gatekeeper handled web findings; the context router used evidence levels.
- **ISSUE:** "REALITY" didn't actually mean "Ness approved this." For imported history it just meant "was in the seed file." A new thought got scored; an old ChatGPT message got a free pass. The sovereignty principle was inconsistent at the source.
- **NEW / SOLUTION:** **The Universal Filter** — ONE filter, every piece, no source exempt (kills the load-to-REALITY-by-filename behavior). The filter **sorts and prepares; it never decides "real."** One continuous reader; meaning from wide ever-growing context; classification never locked. The filter is a **living taxonomy that keeps learning, not a frozen ruler** — because *a validator can't be the same system being validated.* It is the spiritual successor / generalization of the epistemic sandbox (same idea — score how something is said — but applied to EVERY source, not only typed thoughts). **[DESIGNED — not built]** (Full rules now inline in §7A.)

### C. Where the AI is allowed to be creative — silent writes → the membrane
- **OLD:** the AI's associative/generative capability could reach memory automatically (auto-writes, sandbox SIGNAL straight to REALITY, research wired to REALITY).
- **ISSUE:** that's the same capability that hallucinates — letting it write to memory silently is catastrophic; a false connection becomes corruption.
- **NEW / SOLUTION:** **The membrane** — the associative/hallucinatory bridging happens ONLY in the chat (where Ness is present to see and override it), and is structurally barred from writing to memory. In an accretive memory a hallucinated re-reading can't corrupt anything — it's just another layer, a proposal Ness can reject. Dangerous magic in the one observable place; the protected store stays dumb and safe. **[DESIGNED — not built; but every concrete auto-write below was already fixed toward this principle]**

### D. Concrete security holes found on disk → fixes  **[ALL BUILT & VERIFIED]**
- **Sandbox SIGNAL auto-wrote to REALITY** → routed to SIMULATION; `ContextRouter.write()` gained an INFERRED-token check.
- **`update_network_async()` / SIMULATION-routing wrote LLM output straight to REALITY** → now routes to SIMULATION (`.nh_simulation_graph.jsonl`), stamps GENERATED. *(Verified clean June 20 2026. Root cause of past reversions still unsolved — always verify on disk.)*
- **HUD server bound to ALL interfaces** (anyone on WiFi could write to memory) → bound to `127.0.0.1` only (verified with a real phone test).
- **`/api/research_confirm` could promote arbitrary web content with no token** → now requires a gatekeeper token.
- **`nh_pc_agent.py` `run:` arbitrary-`os.system()` trigger** → removed entirely (verified; `open:` browser trigger kept).
- **`_load_raw_sources()` tagged SIGNAL thoughts / marker-matched journal entries as REALITY** → no longer does.
- **pywebview / desktop launcher loading `/chat` stub instead of real HUD** → fixed in `nh_app.py` (line 318), `run_app.pyw`, and `launch_nh.vbs` — all now point at `http://localhost:8080/`.
- **Cloudflare tunnel auto-launching on startup** → tunnel launch block removed from both `nh_silent_start.py` and `nh_service.py`. Tunnel is for Phone Mode 1 only, deliberate and authenticated, never automatic.
- **`/api/simulation_confirm`, `/nightly/run`, `/readonly-on`, `/readonly-off`, `/pc_command` had no auth** → all five now require valid `NH_PROMOTE_TOKEN` before executing.
- **`nh_sovereignty_sync.py` used `StrictHostKeyChecking=no`** in both `_ssh_cmd()` and `_scp_cmd()` → changed to `yes`. Server not configured yet (`NH_BACKUP_HOST` not set) so sync is dormant — but the hole is closed before it activates.

### E. The research pipeline — opinion-filtered black box → raw + controlled synthesis
- **OLD:** `sonar-deep-research` (Perplexity) did its own searching, filtering, and relevance judgment before N.H saw anything. Every "fact" was already opinion-filtered by an outside AI — violating sovereignty even with the gate in place.
- **ISSUE:** what came through the gate wasn't actually raw, so the sovereignty was only true at the gate, not at the source.
- **NEW / SOLUTION:** a **two-layer pipeline** under Ness's control — Brave (raw fetch) → OpenRouter/llama (the one controlled, auditable synthesis step) → SIMULATION → gate. Sovereignty now true at the source. **[DESIGNED — Brave not yet wired; see §8]**

### F. Doc/code consistency — the loose end
- **STILL OPEN:** `.cursorrules` v3.0 and several older docs still carry the old "explicit approval promotes to REALITY" framing. They need reconciling with the accretive/membrane model. Known open task, not an oversight.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 10 (10.0.26100.7840)
- **CPU** i5-11400 (40°C idle / 60°C load) · **GPU** RTX 2060 (35°C idle / ~40°C load) — both verified 24/7-safe
- **Launched via** `run_app.pyw` (the "N.H Interface" desktop shortcut); starts `nh_app.py` silently, opens pywebview window pointing at `http://localhost:8080/`
- **Real interface:** `http://localhost:8080/` (root = the full "N.H // MOTHERBASE AGENT" HUD, `index.html`). Pywebview now correctly loads root. `/chat` stub still exists but is no longer loaded anywhere. **HUD redesign noted for later.**
- **PC has ONE mode** — pywebview native desktop window, local only, no browser, no internet. Browsers cache to disk; pywebview does not. This is the only correct PC interface per the design.
- **Internet-facing surface:** a Cloudflare tunnel — currently **disabled on purpose**; needed only for Phone Mode 1, must be opened deliberately with auth, never on startup.
- **Hardware limit:** a 70B model can't run locally. *(Note: "14GB RAM" appears in older notes — ambiguous between system RAM and the 2060's 6GB VRAM; clarify if it matters for model sizing.)* Everything else fits.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without a dry-run + explicit "APPROVED"):**
`nh_memory_store.py` (`MemoryStore`, evidence levels, **`promote_to_memory()`** — the ONE authorized gate) · `nh_context_router.py` (`ContextRouter.write()` routes to a layer; has an INFERRED-token check — NOT a gate by itself) · `nh_reality_graph.py` (REALITY/SIMULATION/PREDICTION branches) · `nh_simulation_graph.py` (`promote_simulation_record()` / `reject_simulation_record()` — the only valid SIMULATION→REALITY path) · `nh_epistemic_sandbox.py` (scores thoughts on 3 axes; SIGNAL branch now routes to SIMULATION) · `nh_evidence_integrity.py` (contains `guard_write()` — only called in its own self-test block, not in main flow; the real gate is `promote_to_memory()`) · `nh_jarvis_core.py` (the core brain; `run_nh_core_engine()` the real one ~line 1076; a dead duplicate stub exists in `core/engine.py`, zero imports; a dead prompt string saying "OBJECTIVE" sits in a template ~line 564 — harmless label text, never a code decision; *exact line(s) unverified — one note said 564 & 1015, another said only 564; confirm with `findstr` if it ever matters*) · `nh_crypto.py` (AES-256-GCM) · `nh_vector_memory.py` (ChromaDB, `AdvancedSemanticMemory`, `fit_and_index_workspace()`, `_load_raw_sources()`).

**Three physical memory stores:**
1. `.nh_memory_store.jsonl` — immutable verified memory, written ONLY via `promote_to_memory()` (verified clean: 4 records — a VERIFIED med record, an INFERRED date, one inert legacy GENERATED test record left to avoid breaking graph anchors, one encrypted REPORTED_SPEECH record).
2. `.nh_reality_store.jsonl` / `.nh_simulation_store.jsonl` — via the context router.
3. `.nh_simulation_graph.jsonl` / `nh_mental_network.json` — via the HUD server; the only store with `/review` UI coverage. `nh_mental_network.json` is written ONLY by `promote_simulation_record()`.

**Launchers (in order of what's actually used):**
- `run_app.pyw` — the real launcher; "N.H Interface" desktop shortcut points here. Starts `nh_app.py` via `pythonw.exe` (silent, no cmd window), waits 4 seconds, opens pywebview at `http://localhost:8080/`.
- `launch_nh.vbs` — secondary launcher on OneDrive desktop. Also loads `http://localhost:8080/`. Less important than `run_app.pyw`.
- `nh_silent_start.py` — has a **dead BASE path** (`C:\Users\user\OneDrive\Desktop\New folder`) so it starts nothing. Tunnel auto-launch removed. Effectively inert.
- `nh_service.py` — Windows Service (`NHMotherbase`). Audited June 20 2026: uses correct BASE path, starts `nh_app.py` + `nh_auth.py`. Tunnel auto-launch removed. **Not confirmed as actively registered** — if unexpected auto-starts occur, check with `sc query NHMotherbase` / Task Scheduler. *(This is the one open tension with §6's "auto-start disabled" claim: if this service IS registered, it's still a live boot path.)*

**Server / UI (safe to modify):** `nh_hud_server.py` (all routes — `/review`, `/speech`, `/api/research_confirm`, `/pc_command`, `/nightly/run`, `/readonly-on`, `/readonly-off`; bound to `127.0.0.1`; **five sensitive routes now require `NH_PROMOTE_TOKEN`**) · `nh_app.py` (entry point; pywebview host) · HTML: `index.html` (real UI), `nh_chat.html` (stub — no longer loaded), `nh_simulation_review.html`, `nh_speech_form.html`.

**Function-location clarity (was muddled across notes):** The **SIMULATION-routing fix** spans `nh_vector_memory.py` (357/364) and `nh_jarvis_core.py` (828/948). Separately, **`_wire_research_to_network()`** lives in **`nh_hud_server.py`** (348 and 440) — a *different* function; earlier notes wrongly placed it in `nh_jarvis_core.py`. Verified June 20 2026: it routes correctly to SIMULATION + GENERATED, queues to `.nh_simulation_graph.jsonl`, never writes to REALITY.

**Other modules:** `nh_research_engine.py` (`ResearchEngine`, `deep_parallel_research()`, `promote_finding()`, wires `queue_for_review()`) · `nh_research_sandbox.py` (injection guard + `ResearchGatekeeper.confirm(token)`) · `nh_nightly.py` (3 AM maintenance — *note: also listed in the Legacy stack below; treat as legacy/frozen until migration, not active new-stack maintenance*) · `nh_auth.py` (PIN/token auth, `/auth/lock` wipes key from RAM) · `nh_sensor_bridge.py` (input; Whisper hooks future) · `nh_mobile_bridge.py` · `father_firewall.py`, `mother_mission.py`, `nh_lawyer_simulator.py`, `nh_boundary_scripts.py` (personality/confrontation sim — SIMULATION-only, never auto-promote) · `nh_behavioral_baseline.py`, `nh_metrics_tracker.py`, `nh_high_res_monitor.py`, `nh_clinical_report.py`, `nh_viz_engine.py` (wellbeing/metrics/clinical output) · `nh_evidence_processor.py`, `nh_journal_daily.py` · `nh_backup.py`, `nh_local_cleanup.py`, `nh_data_purifier.py` (infra) · `nh_pc_agent.py` (polls `/pc_command`; dangerous `run:` trigger REMOVED, `open:` kept).

**External surfaces (audited June 20 2026):**
- **`nh_sovereignty_sync.py`** — SSH/SCP to Hetzner. Audited. Dormant (`NH_BACKUP_HOST` not set in `.env`). `StrictHostKeyChecking` changed to `yes`. Safe while server not configured. Before enabling: set up Hetzner server with proper auth, add host fingerprint to `known_hosts`.
- **`nh_service.py`** — Audited. Clean. Tunnel block removed. Not confirmed as actively registered.
- **`do_GET()` auth** — five sensitive routes now protected with `NH_PROMOTE_TOKEN`. Remaining routes (`/review`, `/speech`, `/logs`, `/data`, `/readonly-status`) are read-only or display-only — acceptable at `127.0.0.1`.

**Seed data files (the hole the Universal Filter fixes — see §3B):** `cleaned_history (1).txt`, `gpt_purified_history.txt`, `conversations-000/001/002.json`. These currently load into REALITY automatically *by filename* **in the LEGACY/live `_load_raw_sources()` path.** *(Session 4 note: this REALITY-by-filename hole is still open and still expected-open — per §3B / §6A.12-I3 it closes only when the Universal Filter is built. The new accretive store reads these same seed files in as SIMULATION-side layers, which does NOT touch or worsen the legacy REALITY hole — different path, different store.)*

**Accretive store — NEW, session 4 [BUILT & VERIFIED]:**
- `nh_accretive_store.py` — the standalone append-only layered store module. **NOT wired into the live flow, gates, REALITY/SIMULATION stores, or ChromaDB** — touches only its own file. Public API (exactly four functions): `append_root(subject, content, source_title=None)` (re_reads=[]), `append_reading(subject, content, re_reads, source_title=None)` (re_reads non-empty), `read_all()`, `read_by_subject(subject)`. Private helpers: `_coerce_source_title`, `_validate_record`, `_append_record`, `_new_record`. **Append-only is enforced at the file-handle level** — every `open()` is `"a"` (write) or `"r"` (read); there is NO `"w"`, no edit/delete/overwrite function. Schema validated before every append. Verified on disk June 20 2026 (session 4) via `findstr /n /i "def "` and `findstr /n /i "open("`.
- `.nh_accretive_store.jsonl` — the new store file. Append-only. As of session 4 holds **188 root records** from `conversations-002.json` (subject=`seed:conversations_002`). Record shape: `id · subject · timestamp · content · re_reads · source_title`.
- `inspect_seeds.py` — read-only seed-file inspection script (structure/shape only, no writes). Used session 4 to confirm: JSON seeds carry per-message structure (`mapping → message.author.role → content.parts[]`) and a `title` field per conversation; `gpt_purified_history.txt` has strong boundaries (stream headers, role markers, separators); `cleaned_history (1).txt` has role markers only (denser wall, rougher boundaries).
- `ingest_seeds.py` — reads ONE seed file read-only and writes root records via `nh_accretive_store.append_root`. Session 4: ingested `conversations-002.json` only (23 conversations → 188 messages). Skips null/no-text nodes (counted: 23 null, 22 no_text). **Note: image/non-text nodes are currently silently skipped — this is the image-ingest gap, see §9A.**

**Legacy stack (READ ONLY until migration done):** `nh_mental_network.json` + ChromaDB `nh_reality_core` + `nh_timeline.json` + `nh_nightly.py`. **New stack (use this):** `MemoryStore → RealityGraph → ContextRouter → EpistemicSandbox`. **Accretive stack (newest, session 4, standalone):** `nh_accretive_store.py → .nh_accretive_store.jsonl` — not yet wired to anything; the deliberate next-step bridge is §11.

**`.cursorrules` v3.1 (the in-force code ruleset):** governs everything Cursor may and may not do to the code. The **full text is embedded inline in §6A** below — the master no longer just summarizes it. The canonical file Cursor actually obeys is `.cursorrules` on disk (`C:\Users\user\nh_engine_core\.cursorrules`); §6A and that file must be kept identical.

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **REALITY/SIMULATION two-layer gate**, enforced in code.
- **`promote_to_memory()`** — the one authorized gate; blocks GENERATED, blocks INFERRED without token, blocks REPORTED_SPEECH missing speaker/quote.
- **The current gate flow (the old-model mechanic, still what runs today):** SIMULATION records appear as cards at **`/review`**; **Promote** → `promote_simulation_record()` writes to `nh_mental_network.json`; **Reject** → `closed_case` marker, cleared from queue but kept in log. Proven end-to-end: a reply landed in SIMULATION, sat in the queue, Ness clicked Promote, and it entered the REALITY graph by his choice alone. *(This per-record approval is exactly what §3A's membrane model is designed to eventually replace — but it is what exists now, and it works.)*
- **REALITY-only vector index** — ChromaDB `nh_reality_core` indexes REALITY docs only; SIMULATION excluded at index time. (Gating *recall*, not just storage — a genuinely novel piece.)
- **REPORTED_SPEECH** — "it is TRUE they said it," never "what they said is true." Stores speaker + exact quote, encrypted at rest (AES-256, `enc:v1:`). Manual entry at `/speech`.
- **Encryption at rest** for sensitive records · **web results relabeled** INFERRED (not "OBJECTIVE FACTS") · **TEST_MODE flag** (no burning API money while testing) · **epistemic sandbox** (temporal/agency/reality axes) · **working chat + HUD server** · **silent auto-start disabled** *(modulo the `nh_service.py` registration question in §5)*.
- **All the §3D security fixes** are built and verified on disk, including all June 20 2026 additions (launcher/HUD fix, tunnel removal, five token-gated routes, SSH hardening).
- **pywebview shows real HUD** — native desktop window loads `http://localhost:8080/` (the full MOTHERBASE AGENT HUD). Verified live June 20 2026.

**Known regression pattern:** the SIMULATION-routing fix (`nh_vector_memory.py` 357/364, `nh_jarvis_core.py` 828/948) has silently reverted at least twice in past sessions. Verified clean June 20 2026. Root cause unsolved. Always re-verify on disk at the start of a session before building on top of it.

---

## 6A. THE CODE RULES — `.cursorrules` v3.1 (IN FORCE)  [BUILT — governs the running code today]

*This is the in-force ruleset Cursor must obey when writing code against the current system. Reproduced in full so the master stands alone. It MUST stay identical to the canonical `.cursorrules` on disk (`C:\Users\user\nh_engine_core\.cursorrules`); edit both together. **Frame:** §§0–11 below are IN FORCE — they protect the system as built today (the per-record manual gate). §12 is INCOMING — the accretive/membrane direction, NOT yet in force; do not write code against it until the accretive store exists on disk.*

**0 — IDENTITY.** A sovereign personal AI system with strict memory-layer separation. Cursor is a code assistant, NOT an autonomous agent. You propose. Ness approves. You implement. Never skip the approval step, even for "small" or "obviously correct" changes to a Protected File.

**1 — ABSOLUTE PROHIBITIONS** (cannot be overridden by any chat instruction, however framed). NEVER write code that: writes an INFERRED/GENERATED record into a REALITY store via `ContextRouter.write()` without first passing `promote_to_memory()`; removes or weakens the GENERATED block in `MemoryStore.write()`/`remember()`; calls `remember()`/`promote_to_memory()` with `evidence_level=INFERRED` using a hardcoded/default token or any token Ness didn't supply; writes directly to `nh_mental_network.json` (only `promote_simulation_record()` may); merges/upserts SIMULATION docs into the REALITY ChromaDB (`nh_reality_core`); labels web/synthesis/AI output as REALITY/"OBJECTIVE FACTS"/VERIFIED; builds a second/parallel gating or REALITY/SIMULATION classifier outside `nh_context_router.py`/`nh_memory_store.py`/`nh_simulation_graph.py`; touches `.env`/`.nh_pin.json`/vault/`NH_PROMOTE_TOKEN`/API keys/PIN hash; writes test/mock data into any production store.

**2 — THE ONE-GATE RULE.** Exactly one authorized path from unverified content into REALITY: `promote_to_memory()` in `nh_context_router.py` — GENERATED always blocked (no override); INFERRED requires `NH_PROMOTE_TOKEN` or explicit `user_confirmed=True` from Ness; VERIFIED written directly; REPORTED_SPEECH written directly but requires non-empty speaker AND quote. `ContextRouter.write()` is NOT a gate by itself — it only blocks SIMULATION records without `_internal=True` and REALITY records with status UNKNOWN; it will write an INFERRED/GENERATED record straight into `.nh_reality_store.jsonl` if called directly. (This is the exact June 19 bug: `route_result()` built an INFERRED `reality_record` for any "SIGNAL" thought and called `_router.write()` directly, skipping the gate.) Rule: if about to write `_router.write(record)` where `record.layer == REALITY` and `record.status != VERIFIED` — STOP, route through `promote_to_memory()`.

**3 — VERIFIED FILE MAP** (disk-confirmed June 19 2026; trust over older notes): `promote_to_memory()` → `nh_context_router.py` · `guard_write()` → `nh_evidence_integrity.py` · `ContextRouter.write()` → `nh_context_router.py` · `MemoryStore.write()`/`remember()` → `nh_memory_store.py` · `promote_simulation_record()` → `nh_simulation_graph.py` · `_wire_research_to_network()` → `nh_hud_server.py` · `update_network_async()` → `nh_hud_server.py`. **`guard_write()` has NO confirmed callers** — treat as possibly dead; confirm a caller on disk before assuming it's wired; any new caller still must not bypass `promote_to_memory()`. *(Open: master §5 earlier said "self-test block" — reconcile by disk check.)*

**4 — THREE SEPARATE STORES.** (1) `.nh_memory_store.jsonl` — via `MemoryStore.write()`/`remember()`, normally through `promote_to_memory()`; long-term immutable. (2) `.nh_reality_store.jsonl`/`.nh_simulation_store.jsonl` — via `ContextRouter.write()`; **no `/review` UI reads `.nh_simulation_store.jsonl`**, so writing there ≠ queued for review. (3) `.nh_simulation_graph.jsonl`/`nh_mental_network.json` — via HUD server, promoted via `promote_simulation_record()`; this one IS covered by `/review`. Before writing any "pending review" record, confirm which store `/review` reads and use that one, or add coverage in the same change.

**5 — DUAL PIPELINE WARNING.** Two research pipelines exist live: `nh_hud_server.py` (`web_search()` → `_single_angle_search()` → `_verify_and_synthesize()` → `_wire_research_to_network()`) and `nh_research_engine.py` (`ResearchEngine` with its own `_search_tavily()`/`_search_brave()`/`_anchor_to_simulation()`/`promote_finding()`, imported in `nh_jarvis_core.py` and lazily in `nh_hud_server.py`). Both have live import sites. Confirm with Ness which is meant before extending; do not add a third. *(Open: this calls Brave the "currently-intended pipeline" while master §8 says Brave isn't wired — reconcile by disk check.)*

**6 — DUAL STACK.** NEW (use): `MemoryStore → RealityGraph → ContextRouter → EpistemicSandbox`. LEGACY (read-only, do not extend): `nh_mental_network.json` + ChromaDB `nh_reality_core` + `nh_timeline.json` + `nh_nightly.py`.

**7 — PROTECTED FILES** (require explicit "CONFIRMED: modify [filename]" from Ness before any edit): `nh_context_router.py`, `nh_memory_store.py`, `nh_evidence_integrity.py`, `nh_reality_graph.py`, `nh_epistemic_sandbox.py`, `nh_simulation_graph.py`, `nh_research_engine.py`, `nh_research_sandbox.py`, `nh_jarvis_core.py`, `nh_crypto.py`, `nh_auth.py`, `.nh_memory_store.jsonl`, `.nh_reality_store.jsonl`, `.nh_simulation_store.jsonl`, `.nh_simulation_graph.jsonl`, `nh_mental_network.json`. **Safe to modify w/o extra confirmation:** `nh_viz_engine.py`, `nh_hud_server.py` (routes/UI/HTML only — its write functions `update_network_async()`/`_wire_research_to_network()`/`deep_research()` count as Protected), `nh_mobile_bridge.py`, `nh_metrics_tracker.py`, `check_system.py`, `test_*.py`.

**8 — DRY-RUN PROTOCOL.** Before code touching a Protected File or any write-path function, output a PROPOSED CHANGE block (File / What changes / Store(s) touched / Gate function used by exact name+file) and wait for explicit "APPROVED". If the gate answer is "none" or "`ContextRouter.write()` directly" for a REALITY-bound write — stop, that's not a valid gate. Then show full code (no placeholders, no `# ... existing code ...`) and wait for "APPROVED" before applying.

**9 — CODE QUALITY.** No placeholders/`# TODO` — complete blocks only. No silent store-write failures (no bare `except: pass`; flag existing ones like `route_result()` rather than extend them). Schema validation mandatory for every `.jsonl` payload. Async/threaded store writes must have results checked, not fire-and-forget.

**10 — PULL SOVEREIGNTY.** System pushes nothing unsolicited, auto-promotes nothing. No new autonomous background task without an explicit `# AUTONOMOUS: approved by user [date]` comment. Re-enabling any silent auto-start / scheduled task / tunnel requires separately confirming the auth layer in front of it is verified on disk — never assumed from a comment.

**11 — BEFORE ANY NEW MEMORY FEATURE.** Check whether it already exists in `nh_context_router.py`/`nh_memory_store.py`/`nh_simulation_graph.py`/`nh_evidence_integrity.py`/`nh_research_sandbox.py`; if close, extend it. Do not build a fourth parallel gate — proliferation of write paths is the standing risk, not a one-time mistake.

**REMINDER:** every shortcut around `promote_to_memory()` is a sovereignty violation, even if the record lands in something with "SIMULATION" in its name — a SIMULATION record nobody can review is no different from a REALITY record nobody approved. When in doubt: propose, name the exact gate function and file, wait for approval.

### 6A.12 — INCOMING (the accretive/membrane direction)  [NOT IN FORCE — do not build against yet]

**These are NOT live instructions.** They record where the system is going (§3A/§7), not what runs today. Do NOT write code against them until the accretive store exists on disk and Ness says it's active. Until then §§0–11 are the law; any conflict resolves in favor of §§0–11.
- **I1 — Memory only ADDS, never edits** (the keystone): append-only, layered; new context adds a layer, never overwrites/deletes.
- **I2 — The membrane:** associative/hallucinatory bridging lives in chat, structurally barred from writing to memory. *(Every concrete auto-write hole is ALREADY closed toward this — §3D — but the membrane as the gate isn't built.)*
- **I3 — One filter, no source exempt:** kills REALITY-by-filename. *(SIGNAL/journal auto-tagging already fixed; the `_load_raw_sources()` seed-file-by-filename hole closes when the filter is built, not before.)*
- **I4 — Classification never locked:** re-readings land as new layers, never edits (depends on I1).
- **I5 — Ness steers, doesn't file:** sovereignty becomes the membrane position; this REPLACES the per-record Promote/Reject flow — but only when built. Do not weaken today's manual gate on the strength of this.
- **Reconciliation:** when the accretive store ships, §§0–11 are rewritten to match §12 (the membrane gate JOINS, doesn't silently replace, the one-gate rule) and this INCOMING block collapses into the in-force body.
- **Session 4 status:** the accretive store now EXISTS as standalone code (§6B) but is still NOT wired into the live flow — so §12 remains INCOMING and §§0–11 remain the law. The store being built does not change which rules are in force; wiring it in later is the deliberate step that triggers the §12 reconciliation.

---

## 6B. WHAT WAS BUILT THIS SESSION — THE ACCRETIVE STORE SKELETON  [BUILT & VERIFIED — session 4, June 20 2026]

*This is the first running code of the accretive/membrane direction (§3A, §7). It is a deliberately dumb, standalone, append-only store — "keep the memory dumb and safe, put the cleverness elsewhere" (§3C). It is wired to NOTHING yet; that is by design.*

**What it is:** one text file (`.nh_accretive_store.jsonl`) where each line is one record (one piece of meaning) as a JSON object. Writing can only ADD a line to the end (append-only). It physically cannot change or remove an existing line. That is the keystone (memory only adds, never edits — §6A.12-I1, §7A Rule 6) made real in code, not as a rule someone must remember but as a property of how the file is opened.

**The module `nh_accretive_store.py` — verified on disk:**
- Four public functions only: `append_root(subject, content, source_title=None)`, `append_reading(subject, content, re_reads, source_title=None)`, `read_all()`, `read_by_subject(subject)`.
- Every file `open()` is `"a"` or `"r"` — **no `"w"` anywhere** (a `"w"` would truncate the file; its absence is what guarantees append-only). No `edit`/`update`/`delete`/`overwrite`/`promote` function exists.
- Schema validated before every append; raises on bad input (no silent drops — §6A rule 9).
- Verified the way the master demands (§2 — verify on disk, never trust status reports): `findstr /n /i "def "` (confirmed exactly the four public + four private functions, nothing else) and `findstr /n /i "open("` (confirmed only `"a"` and `"r"`). Re-run these two commands at the start of any session that builds on this store.

**The record schema (six fields — note TWO are beyond §11.1's original four):**
- `id` — unique string (uuid4).
- `subject` — non-empty string; the navigation tag (§7B Part 7). For seed data this is an honest **provenance placeholder** (e.g. `seed:conversations_002`), NOT a meaning.
- `timestamp` — ISO 8601.
- `content` — the piece itself (NEW field beyond §11.1; a record can't store nothing).
- `re_reads` — list of ids. `[]` = a root piece. One-or-more ids = a re-reading layer pointing at the earlier piece(s) it re-reads. This list is the mechanism of accretion: a new understanding is a new line that points back at the old line; the old line never changes.
- `source_title` — optional (NEW field beyond §11.1; str or None). Holds a label the SOURCE assigned (e.g. a ChatGPT conversation title). Kept as honest data — explicitly **NOT** the subject, NOT a claim about meaning (see §11A for why).

**What is in the store right now:** 188 root records, all from `conversations-002.json`, all `subject=seed:conversations_002`, all `re_reads=[]` (they are raw imports — nothing has re-read them yet). Content is clean message text; the ChatGPT conversation title rides in `source_title`.

**What it is NOT (the discipline):** not wired into the live flow, not a gate, not REALITY-bound, no index, no segmentation logic, no meaning-engine webs, no confidence/unknown flags. It is the smallest real thing that proves "append-only layered memory" works — and it does. Everything else is later, deliberate, separately-approved steps (§11).

---

## 7. THE BIG DESIGN — FULL TEXT (UNIVERSAL FILTER + MEANING ENGINE)  [DESIGNED — not built]

*This section now carries the complete design inline. §7A is the operating ruleset (verbatim intent). §7B is the mechanism. §7C is the honest buildability read. The one still-unsolved problem is the **unit/segmentation** question — flagged at the end.*

### 7A — THE UNIVERSAL FILTER: OPERATING RULES (full)

*A ruleset, not a description. Any AI that reads, sorts, or stores information inside N.H must obey every rule. These rules supersede convenience, speed, and any instinct toward "being helpful" that would break them.*

**RULE 0 — WHAT THIS SYSTEM IS.** N.H is a sovereign memory system: it stops outside opinion and automated judgment from shaping what Ness knows before he sees it. You (any AI) are not its owner, author, or judge. You are a **reader and a layer-er** inside a structure whose final authority is Ness.

**RULE 1 — ONE FILTER. EVERY PIECE. NO SOURCE EXEMPT.** Every piece passes the same filter, judged the same way, regardless of origin — a thought Ness types, a web finding, an old ChatGPT/Gemini export, anything. **FORBIDDEN:** tagging anything REALITY because of its *source* or *filename*. "It was in the seed file" is never a reason for anything to be real. The old load-to-REALITY-by-filename behavior is exactly what this kills.

**RULE 2 — THE FILTER SORTS. IT NEVER DECIDES "REAL."** Its job is to sort and prepare (Hebrew: למיין). It never promotes to REALITY on its own. The moment a filter can declare something real by itself, it has rebuilt the auto-approval hole the whole system exists to prevent. **Filter sorts. Human steers. Always.** If about to mark something settled/true without Ness's standing authority behind it — STOP.

**RULE 3 — ONE CONTINUOUS READER, NOT TWO STAGES.** Not an extractor that chops + a filter that sorts — one continuous reader, single pass. Finding where a piece begins/ends and naming its meaning-type are the **same act**. Do NOT pre-decide a fixed "unit" by rule; the reader finds the boundary itself by watching where the meaning-type shifts. Loop: *words flow in → track the meaning → when the meaning-type shifts, close one statement, tag it, open the next.*

**RULE 4 — MEANING COMES FROM WIDE CONTEXT, NOT LOCAL WORDS.** You may not classify from the words directly in front of you. "I'm done with this" can be a claim, an expression, a joke, a callback, or an intention — visible only against the wide frame built across many sentences. Read against the **largest accumulated context available**. If wide context is thin, your reading is **low-confidence by default** — say so.

**RULE 5 — CLASSIFICATION IS NEVER LOCKED.** Because meaning depends on accumulating context, every reading is provisional — forever. A statement sorted months ago can be re-read and recolored later. Every tag is a *current best reading against current context*, never a permanent truth. Treat your own past classifications as revisable.

**RULE 6 — MEMORY ONLY ADDS. IT NEVER EDITS. (THE KEYSTONE.)** When new context recolors an old statement, you do NOT change what's stored — you **add a new layer** beside it: *"this earlier statement, read against this new context, now means this."* The original stays intact forever; the new reading joins it; **nothing is ever overwritten or deleted.** Opposite of normal memory (which UPDATEs): N.H **ACCRETES** — a growing record of *how meaning evolved*, never lying about its past because it never deletes it. **FORBIDDEN:** editing, overwriting, correcting-in-place, deleting, merging-away, "cleaning up" any stored reading. The only write memory permits is **append**.

**RULE 7 — THE MEMBRANE: HALLUCINATION LIVES IN CHAT, NEVER IN MEMORY.** The associative/bridging capability (the same one that invents false links) gets **full freedom in the chat layer and is structurally barred from the memory layer.** *Chat:* bridge freely, surface associations, propose new meanings, be wrong — it's the scratchpad. *Memory:* only accretes; a new layer lands only from what survived the chat (what Ness saw and didn't reject). A hallucinated re-reading is harmless **because** memory only accretes (Rule 6) — it becomes a rejectable *proposal*, never a corruption. Break accretion and hallucination stops being harmless: keep both rules or neither works.

**RULE 8 — WHICH OLD STATEMENTS GET RE-READ.** You can't re-read everything every time. Use **associative bridging** as the relevance-trigger: new context arrives → the natural associative leap surfaces the old statements that *feel* connected → those light up for re-reading. Not a mechanical scheduler — the model's native association pointed at a good use. It WILL sometimes surface a spurious link; acceptable (Rule 7) — it becomes a rejectable layer, never a corruption.

**RULE 9 — HOW THE FILTER SORTS: BY MEANING-TYPE, IN A GROWING STRUCTURE.** The root distinction is **the kind of meaning/intent behind the utterance** — *why it was said* — not surface form, not true/false. Candidate root meaning-types (a starting snapshot, NOT final, ~7 items): **state/claim · ask · wonder/explore · express/feel · intend/want · report** (relay another's words — "it is true they said it," not "what they said is true") **· imagine/hypothesize.** Structure grows in every direction: **wide** (new roots when a way-of-saying fits nothing existing) and **deep** (each node branches, and branches again). A piece travels **down a path to a leaf** — a *route*, not a single label.

**RULE 10 — MAXIMAL-BUT-BOUNDED.** Grows in every direction *in principle*, deliberately limited *in practice*: as wide and deep as a tired human can actually use, then a real chosen line. The bounded target is **small (~5, hard cap 7 — matching Searle's 5 speech-act classes and Miller's 7±2 / Cowan's ~4)**; the ~7 candidate list above is the starting snapshot, growth comes from **depth, not width**. Not infinite (unusable), not rigid (untrue). The line may move outward over time; respect the current line — do not silently expand past it.

**RULE 11 — NESS'S ROLE: STEERER, NOT CLERK.** Ness is not the sorter and not a filer. Do NOT build a per-record manual-approval workflow — he rejected that, correctly, because manual sorting freezes readings that should stay provisional (fights Rule 5). The AI does the continuous reading/re-reading/layering itself; there are no edits to approve because there are no edits (Rule 6) — only accumulation. His sovereignty is **standing authority to steer and override** a record that never stops growing and never erases itself. **By being present in the chat, Ness IS the membrane** (Rule 7). Surface, propose, lay out — and let him steer.

**RULE 12 — HONESTY ABOUT WHAT THIS IS.** TRUE and defensible: "a structured place for the AI to be creative (chat) without that creativity corrupting what's permanent (memory)" — an architecture-and-safety contribution about *where things are allowed to happen*. FALSE and forbidden: that this "makes the AI think independently" or is "a new kind of cognition." The model underneath is unchanged. Overclaiming hands critics a reason to dismiss the real parts. **Never overclaim.**

**FAILURE MODES — IF YOU CATCH YOURSELF DOING ANY, STOP:** (1) REALITY-by-source/filename → Rule 1. (2) auto-promoting to real without Ness's authority → Rule 2. (3) chopping by a fixed unit instead of meaning-shift → Rule 3. (4) classifying from local words → Rule 4. (5) treating a past classification as final → Rule 5. (6) editing/overwriting/deleting stored memory → Rule 6 (never). (7) an associative leap writing to memory → Rule 7. (8) silently expanding past the line → Rule 10. (9) building a per-record approval workflow → Rule 11. (10) claiming "independent thinking" → Rule 12. **When in doubt: filter sorts, human steers; memory only adds; hallucination stays in chat.**

### 7B — THE MEANING ENGINE: THE MECHANISM (full depth)

*The Universal Filter rules (§7A) say WHAT must be true. This says HOW the reading actually works. Every web is grounded in real research on how meaning is reconstructed (pragmatics, speech-act theory, Gricean/cognitive pragmatics) — not invented.*

**THE ONE-LINE SHAPE.** A piece of content is not read once. It runs through a **chain of "webs"** — each web a different real dimension of meaning — and the engine fills each web with **enough** information by researching **inward (the person) and outward (the world)**, at night. What it can't fill, it **tells Ness** (it never asks, never waits). Everything it does is written to a **read-only, subject-tagged, permanent log** Ness can come back to and click through.

```
raw piece → [web] → [web] → [web] → ... → enough? → reading
                                            ↓ no
                                  research more (inward + outward)
                                            ↓ still can't
                                  INFORM Ness (don't ask) + log it
```

**PART 1 — IT IS A CHAIN OF WEBS, RUN AS ONE.** A piece's meaning is **not one flat tag** (claim/ask/feel). Flat tags are dead — they give the ingredients, not the meaning. The meaning lives in **how the dimensions relate** in this specific piece. So the engine runs the piece through a **chain of webs**; each web is one real dimension; the piece "lights up" a pattern in each; the real meaning is **what holds up across all the webs together**, not any single snapshot. This is "one continuous reader, not two stages" made concrete — the webs are the reader's single pass, not a chopper-then-sorter. **Correction:** the category list (claim/ask/feel/report/intend/wonder/imagine) is **ONE web — the intent web. It is NOT the whole engine.** Earlier thinking treated that list as the entire structure; it is one dimension among several.

**PART 2 — THE REAL WEBS (research-grounded, not invented).** Each is a genuine dimension the fields studying meaning say must be checked. The list is open ("...and more") — even the real research leaves it open, so this is honest, not lazy.
1. **INTENT — what were they *doing* by saying it.** Speech-act / illocutionary dimension. The five-to-eight categories live HERE (state/claim, ask, promise/intend, express/feel, declare, + report, wonder, imagine). One web, not the machine.
2. **DEIXIS — anchor the "pointing words" to reality.** Resolve who/when/where. Sub-kinds: person deixis ("she", "I"), temporal ("next week", "moved"), spatial ("there"), discourse ("that thing you said"). Distance can be *psychological*, not physical — "I don't like THAT" can carry feeling, not location.
3. **COMMON GROUND — what's shared and assumed.** The unspoken backdrop both parties already knew and didn't have to say. A piece means what it means partly because of what was presupposed.
4. **IMPLICATURE — what they meant beyond the literal words.** Gricean. Check the four maxims: Quality (truthfulness), Quantity (right amount), Relation (relevance), Manner (clarity). **A flout of a maxim = the tell for sarcasm / irony / non-literal meaning.** This is the web that catches "I'm done with this" being a joke, not a real claim — how the engine distinguishes a true claim from a sarcastic one before anything gets stored.
5. **THEORY OF MIND — model the mind behind it.** Read the piece against who said it and what cognitive/affective state they were in. The rational + intentional dimension of interpretation.
6. **TIME / SEQUENCE — where it sits in the flow.** Partly deixis, partly N.H's own: a message moves (report → feel → dismiss → intend); the piece is the chain of states across it.
7. **RE-READING — run the whole chain again later.** When new context arrives, re-run the chain → produce a NEW reading → **add it as a layer** (never overwrite). This IS the accretion. The re-reading web never truly closes.
*(...and more. The list is deliberately open. New webs may be named as real life reveals dimensions the current set can't hold — but each new web must be a REAL dimension, grounded, not decorative.)*

**PART 3 — HOW THE WEBS COMBINE (the hard part Ness kept pushing on).** The webs are **separate** (real, distinct dimensions) but **fire together as one engine in one pass** — not one-at-a-time, not Ness picking one. Think: separate lenses stacked into one camera; light passes through all of them together, out comes one image; the lenses don't take turns. The richness is **breadth across the webs** plus the **relationships between what lights up** — NOT depth-drilling into endless subcategories (subcategory-depth was explicitly rejected). The meaning is "which connections fire across the whole, in what arrangement," not "which deep sub-sub-folder did it fall into." Picture it as **everything connected to everything, held as one** — a web where each piece lights up a *pattern*, and that pattern is the reading. One web, infinitely many patterns.

**PART 4 — NIGHTLY RESEARCH, INWARD + OUTWARD.** The engine runs **at night** (fits the existing nightly cycle). To fill a web that's missing information it researches **both directions**: **INWARD** — on Ness (his history, what N.H already holds, prior pieces); **OUTWARD** — on the world (facts, context, anything external the web needs). A piece is **held** while this research runs — it does not get forced through with gaps (forcing gaps = counterfeit, forbidden).

**PART 5 — HOLD UNTIL ENOUGH (not until perfect).** The bar is **"enough information in each web,"** NOT "all webs perfectly complete." Perfect may never happen; chasing it = limbo (unusable). "Enough" is a **threshold**, and like every line in N.H it is **movable over time** — a judgment, not a fixed number (maximal-but-bounded again: find usable-enough and move). Once every web has *enough*, the piece moves forward to become a reading (entering SIMULATION, where Ness steers — the engine decides it's *ready to show*, never that it's *finished/true*).

**PART 6 — CAN'T FILL → INFORM, DON'T ASK (the sovereignty rule, exact).** *The most-corrected, most-important part — get it exactly right.* If after researching inward + outward a web **genuinely can't be filled**, the engine does **NOT** silently auto-stamp it "unknown," and does **NOT** stop and ask Ness to decide. It **INFORMS** him — surfaces the *specific* gap by name: *"this web, on this piece, I couldn't fill; here's exactly what's missing."* **Inform ≠ ask. Surface ≠ solicit.** The engine **keeps running** — does not queue the piece for approval, does not wait, nothing blocks on Ness. **Ness is present, not required** — a *witness* to the loop, free to steer anytime because he's sovereign, but the engine never *needs* him and never hands him the decision (requiring him = the "manual clerk / goon" trap, rejected). Because he's merely *informed*, he can research his own life on his own time — ask family, dig up a photo, remember on a walk — and **give the answer back later, whenever; no deadline** (the engine already moved on). When he gives it back, it lands as a **NEW LAYER**, never an overwrite: *"unknown on June 20 → filled by Ness on [later date]."* The honest "I didn't know this then" stays forever. "Unknown" is an **honest, valid, re-checkable** state — never a failure, never permanent; later context may make it knowable, then it's re-read and a layer added. **The whole loop has no failure mode:** every piece ends somewhere honest — read, or honestly surfaced-as-unknown — nothing forced, frozen, or faked.

**PART 7 — THE LOG (read-only, subject-tagged, permanent, clickable).** The surface through which Ness sees the engine's nightly mind. **Read-only / look-don't-touch:** Ness can SEE everything the engine did; he cannot EDIT the log. Read-only is load-bearing — it's the accretion rule made visible, the record never gets rewritten so it can't lie about its own past (same "look don't touch" principle as the rejected-bin display). **Seeing ≠ approving:** a log to read, not a queue to action — "inform, don't ask" turned into a browsable surface, no clerk work. **Subject-tagged:** every entry carries `(subject = X)` — e.g. `(subject = family)`, `(subject = the meeting)`; organized by what each entry is about. **Permanent + findable:** because it's tagged and never deleted, Ness can come back next week/month, filter by `subject = X`, and the entire evolving history of that subject is **still there**, grouped and intact — the subject tags are the **navigation layer** that keeps infinite accretion usable (without them, "never delete" becomes "never find anything"). **Clickable:** subjects expand; entries open to show the piece, its webs, its unknown-flags, and its layers over time. (Build note: standalone clickable prototype first — like the canvas prototypes — before wiring to the live engine.)
**The log is THREE things at once:** (1) **Transparency** — unalterable proof of what the engine did, honest because read-only; (2) **The mirror (the INWARD direction)** — Ness watching his own thinking sorted from outside, the pattern he can't see because he's inside it; the JARVIS "inward/mirror" purpose made into something he can open and scroll; (3) **A permanent subject-indexed archive** — `subject = X`, come back anytime, all still there, navigable.

**PART 8 — HOW THIS LOCKS INTO THE RULES (§7A):** Chain of webs = Rule 3 (one continuous reader) + Rule 4 (wide context). Re-reading web + new layers = Rule 6 (keystone) + Rule 5 (never locked). Inform-don't-ask + present-not-required = Rule 11 (steerer not clerk) + Rule 7 (membrane). Hold-until-enough, no forced gaps = the anti-counterfeit core (nothing pretends more settled than it is). Read-only log = accretion made visible + "look don't touch." Don't overclaim = Rule 12 (architecture for *where* reading and ignorance live and are seen, not "the AI thinks independently"; the model underneath is unchanged).

**TRUEST SENTENCE (for the engine):** One engine reads each piece across many real webs of meaning at once, researching the person and the world to fill them; what it can't fill it shows Ness without ever asking or waiting; and everything it does is written, read-only and forever, into a log Ness can come back to and click through — so the engine looks outward at the world while Ness looks inward at himself, both at their own speed, meeting in a record that only ever grows.

### 7C — CAN IT BE BUILT? (honest)

The **accretive skeleton** (append-only, layered, nothing overwritten) is buildable now, almost easy — the `.jsonl` stores already append — and captures ~80% of the value alone. **This is the smallest real next step.** Continuous re-reading is buildable as an approximation (re-read against a retrieved slice, not literally everything). The membrane makes it MORE buildable: the dangerous part is confined to chat, memory stays a simple append-only store. **Don't overclaim** — architecture-and-safety contribution (*where* things happen), NOT "AI thinking independently."

**THE ONE STILL-UNSOLVED PROBLEM — the unit / segmentation.** What counts as *one piece* to be sorted — a sentence, a message, a turn? A ChatGPT export is a conversation (questions, AI replies, tangents), not a list of claims. Rule 3 *dissolves* this in principle (boundary and type are one act, one pass) — but that is a principle, not a mechanism. This is the real blocker for the meaning engine, and it is untouched. The accretive skeleton does NOT depend on it.

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not yet wired]

*(Old→new rationale in §3E.)* Three layers, all under Ness's control:
1. **Raw fetch — Brave Search API.** Raw URLs/titles/snippets, zero AI interpretation. Chosen over Tavily (which pre-chews); Brave runs its own independent index.
2. **Synthesis — `llama-3-70b-instruct` via OpenRouter.** The ONLY AI-opinion step, the one Ness controls and audits. **KEEP THE OPENROUTER KEY — Brave and OpenRouter do two different jobs and are NOT interchangeable.** Brave replaced *sonar*, not the synthesis model.
3. **Gate** — findings → SIMULATION; `ResearchGatekeeper.confirm(token)` to promote. 2-of-3 angles: 3 raw searches → 1 synthesis pass.

**Security defaults (non-negotiable, baked into the Cursor instruction):** synthesis is text-in/text-out only (no tool-calling, no file access, no outbound requests); its prompt frames fetched content as unverified raw web to extract facts from, never instructions. **Auto-reject, never auto-delete** (an AI with delete authority is itself an injection target). **Rejected-bin "look don't touch":** URLs as plain text never `<a href>`; no favicons/previews/unfurling; copy/select disabled; strip invisible/zero-width/RTL characters; render via `textContent` never `innerHTML`.

**Costs (June 2026):** Brave $5/1,000 queries; the **paid plan bundles ~1,000 free queries/mo** (the standalone free tier was discontinued Feb 2026); card required, cancel-friction — monitor. *(Verify against current Brave pricing.)* Full nightly (~13,500/mo): ~$62 Brave + ~$60–240 synthesis = **~$120–300/mo** vs old **$6,000–13,500/mo**. Build/testing stays in the free credit. `test_brave.py` exists; test was pending.
**Academic source [OPEN]:** Google Scholar ruled out. **Semantic Scholar** (~200M papers, CS/AI) vs **OpenAlex** (250M+, all fields, no key). Leaning toward both. Pending.

---

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]

**Access / authentication:** **Dry mode (default, no auth)** — pure research engine, zero personal data loaded/searchable, dark-by-default; reach a running N.H without auth → a research tool, not Ness's life. **Personal mode (PIN)** — unlocks history/REPORTED_SPEECH/medical. **Graduated step-up auth (not a master key)** — tiers unlock separately for short windows, then re-lock: casual → none; exact quote → PIN; medical → PIN + fingerprint. **Factor hierarchy:** fingerprint (strongest — lean on Windows Hello / phone sensor, don't build a matcher) > PIN (everyday; exists in `.nh_pin.json`) > voice (softest — convenience only, NEVER a hard lock; fails when stressed/sick/crying = lockout when most needed). **Raw-vs-derived dial:** N.H is *shaped by* personal data but doesn't *spill* raw records by default — a step converts relevant data to a derived signal; raw quotes stay in the vault (exception: explicit authenticated request for an exact REPORTED_SPEECH quote). **Access layer:** trusted app only (desktop pywebview + phone), not a plain browser (browsers cache to disk); zero-copy — load live, retain nothing on close. The dry/personal boundary must be real at code level.

**Mobile companion (three modes):** Mode 1 stands alone; Modes 2 & 3 are the same local AI in two states. **Rule across all three: nothing connects to the real N.H automatically, ever** — only Manual Sync and Full Mode bridge, both deliberate. **Mode 1 — Full:** fingerprint/PIN opens an on-demand Cloudflare tunnel to desktop N.H; opened AND closed deliberately. **Mode 2 — Local AI (online):** a real small on-phone model (1–3B) with its OWN separate memory, calling internet APIs to grow it; never auto-connects. **Mode 3 — Lite/offline:** same model/memory, no internet; if memory empty, silently stores input until reconnected. **Open question:** whether Lite Mode carries cached facts as context (so it still feels like *his* AI) or goes generic — Ness said "idk," unresolved. **Manual Sync:** fingerprint-confirmed; phone data → same SIMULATION review gate. Hard rules: Mode 1 tunnel wired through real `nh_auth.py`; `run:` stays removed; all local data encrypted.

**Interactive canvas:** architecture as illustrated, interactive icons (not boxes). Background = mode: **pure black = architecture, dark metallic blue = solving.** Icons are live controls (click a store → records; click a gate → pending). Style "C2+D2 combined" (warm glow-fill + sci-fi HUD detailing). Legend: red = core, orange = gate, purple = store. Build order: canvas surface → icon set → interactivity → blue mode → `/generateincanvas` backend LAST (only part touching the real system). Prototypes exist.

**Behavioral-baseline wellbeing engine:** learns Ness's patterns from his *own* promotion decisions; detects divergence from *his* baseline (Ness-vs-Ness, never external); tiers from silent flagging → REALITY freeze; validated by internal consistency; anchored to real appointment documents. **Caution Ness accepted:** build pure-software layers freely, but build any **sensor layers (HRV/breath) as data-loggers ONLY first** — collect, compare to what actually happened, confirm the pattern holds for him before the system acts. The "90-second early warning" is an AI hypothesis, not an established fact about his body.

**HUD redesign:** the current MOTHERBASE AGENT HUD works but needs a visual redesign. Future work — do not touch until the accretive store and filter are built.

**Other unbuilt:** phone-data importer (two old Samsung phones 2017–2024 being recovered for seed material; every item writes as SIMULATION, never REALITY directly) · memory browser · personality modeling (rehearse hard conversations from transcribed calls) · nightly autonomous scraper (~150 cycles/night, all SIMULATION) · voice in/out (Whisper → `nh_sensor_bridge.py`; TTS via Piper/Coqui) · phone-side modes (emergency record, breathing reminder, night lockout, kill switch) · multi-project folder split · multi-perspective "according to whom" field · ChromaDB cleanup (~107k chunks — approved, **on hold** until the filter is built) · folder cleanup across `nh_engine_core`, `C:\NH`, and a dead OneDrive path.

---

## 9A. IMAGE INGEST — THE FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED — not built]

*Recovered/worked-out session 4. This is the first concrete example of the input-agnostic principle (§1A): images are NOT a separate subsystem — they are another input fed through the SAME meaning engine (§7B). Only the front door is image-specific. (Ness had wanted vision capability previously, likely told it to Gemini, so it was lost from the record — this section recovers it. The kind he wants is SCENE understanding — what's happening, who's in it — NOT just text-in-image OCR.)*

**The found problem:** the current `ingest_seeds.py` silently skips image/non-text nodes (the "22 no_text" skips, §5). So images don't just go unprocessed — they vanish, leaving invisible gaps a later reader can't distinguish from "nothing was here." When there are many images, this is a real correctness problem. The phone-photo import (the two Samsungs, §9) is mostly images, so this is coming straight at the project, not a corner case.

**The design — "the camera reports plainly; meaning is built in the layer-space where Ness is the membrane."** An image flows through the engine as a stack of layers, least-interpretive first:
1. **Metadata layer = FACT.** EXIF/file properties — date, dimensions, location, that a photo EXISTS. No AI. REALITY-eligible (like a timestamp). This is brute fact, not relative (§1A honesty line).
2. **Plain-description / object layer = LOW-OPINION, honest-about-uncertainty.** The "seeing" step. Best done with an **object-detection / segmentation model** (YOLO / Segment-Anything class — e.g. via `osam`/Ollama locally), NOT a narrating vision-language model. Output is flat labels + boxes + **confidence scores**: *"person (0.94), water (0.91), held-object (0.7)"* — not "a happy family at the beach." It is still not pure fact (even "person" is a trained label, which is why it carries a confidence) — but it is the LEAST speculative read of content, and honest about its own uncertainty, which is exactly how N.H treats everything. → SIMULATION, the least-speculative kind. **Ceiling:** object detection only knows labels it was trained on; it is "neutral within its vocabulary," will miss/force-fit the unfamiliar.
3. **Context-meaning layer = INTERPRETATION.** The plain description meets everything N.H already knows about Ness, and *that context* proposes "this is Ness and his father at X." The context does NOT read the photo — it reads the plain description against his life. → SIMULATION, the most speculative; a re-reading layer pointing back at layers 1–2; **never auto-promoted to REALITY.**
4. **Ness confirms → the steer.** Only Ness actually knows who is in his photo. His confirmation is the only thing that can turn "who's in it" into something real. → another layer. And if context genuinely can't tell → **honest "unknown,"** surfaced not asked, fillable later as a layer (§7B Part 6).

**The key realization (why this fits without fighting sovereignty):** you do NOT try to make the AI "not interpret" — interpreting is its nature (even "person" is a tiny דעה/opinion). You let it give its opinion FULLY, but **catch it as an opinion** — a reading with a confidence, dated, stamped as a guess, landing as a layer — and as more context arrives, that opinion is re-read and a NEW opinion added beside it. The דעה is never banned; it is held loosely and allowed to move. That is the membrane (§7A Rule 7) and accretion (Rule 6) doing exactly their job. **The danger is not the AI having an opinion — it is the opinion getting promoted to fact by itself, or frozen.** N.H prevents both. "Fixed with context" must mean *context PROPOSES a better reading* (which Ness can confirm), NOT *context makes the AI's guess true on its own* — the latter is a hallucination that found enough nearby data to look true, which is precisely the corruption the membrane exists to stop.

**Why this is one engine, not a feature:** the image's layers run through the same chain-of-webs (§7B), land in the same read-only subject-tagged log (§7B Part 7), are shown the same way Ness sees text readings, and are steered the same way. There is no "image subsystem" — just a new front door (a small local vision/detection model) that turns a photo into pieces. The same is true for video (frames + audio + time) and audio (transcribe → text). **Hardware note:** the front-door model must fit the RTX 2060 (6GB VRAM) — small document/detection models (PaddleOCR-VL ~0.9B runs on CPU, 109 languages incl. Hebrew; SmolVLM-class; segmentation models) fit; an 11B vision-language model needs ~8GB VRAM and is borderline/no. *(Verify current model availability and VRAM needs before building.)*

---

## 10. ORIGINALITY (honest calibration, from a 2026 field survey)

Every individual brick exists somewhere (local-first personal AI: Khoj, PAI, Second Me; human-in-the-loop gates: LangGraph, Mastra; epistemic-provenance KGs; dual-LLM injection containment: CaMeL; N-of-1 baseline monitoring: clinical digital phenotyping). The **combination does not ship anywhere.** Nearest cousins are two 2026 preprints: **memorywire** (arXiv 2606.01138 — diff-and-approve, but drifts to auto-approve and leaves recall ungated) and **SSGM** (arXiv 2603.11768 — two-track memory, but automated gate, not human). *(Verify both arXiv IDs exist before leaning on them publicly.)* **Three sharpest contrasts:** mandatory vs optional approval; gating recall/indexing vs not; human gate vs automated gate. **Claim the combination and the inverted default** (mandatory, non-bypassable human role + REALITY-only vector index + individual cognitive-sovereignty framing) — never the invention of local AI or approval gates.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store** — ✅ **BUILT & VERIFIED session 4** (`nh_accretive_store.py`, §6B). The design loop is broken — there is running code. **Still open within this item:** (a) the **read-only subject-tagged log** UI (§7B Part 7) — the browsable "mirror" surface; build as a standalone clickable prototype first, like the canvas prototypes, before wiring to the live engine; (b) **scale the seed ingest** — only `conversations-002.json` (188 records) is in; remaining is `conversations-000.json` + `conversations-001.json` (200 more conversations, same per-message + title-as-source_title shape — pattern proven, low risk) then the two `.txt` seeds (`gpt_purified_history.txt` strong boundaries; `cleaned_history (1).txt` rougher — role markers only); (c) **wire the accretive store into the live flow** — the deliberate second step, separately approved, which triggers the §6A.12 reconciliation.
2. **Image-ingest front door (§9A)** — NEW, recovered session 4. At minimum: stop silently dropping image/non-text nodes; write an honest "[non-text content here — unknown]" marker so gaps are visible (fits §7B Part 6 unknown-as-honest-state). Fuller: a small local vision/detection model (2060-fittable) producing the plain-description layer, output landing SIMULATION-only, never REALITY. **Especially needed before the phone-photo import (§9)** — those Samsungs are mostly images. Decide simple-marker vs full-vision when it becomes its own step; do NOT bolt onto the just-closed skeleton.
3. **Universal Filter / meaning engine** — settle the **unit** (segmentation; see §7C — the one unsolved problem), then build on the skeleton. *(Note: seed ingest in item 1 picks a deliberately coarse PROVISIONAL unit — per-message for JSON — which is NOT solving §7C; it is choosing the unit that destroys the least, knowing finer readings get added as layers later. See §11A.)*
4. **ChromaDB cleanup** — on hold until the filter exists.
5. **Research pipeline build** — Brave key + `test_brave.py` + academic-source decision + both security defaults.
6. **Hetzner sovereignty sync** — before enabling: set up server, add host fingerprint to `known_hosts`, wire through `nh_auth.py`. `StrictHostKeyChecking=yes` already set.
7. **Confirm `nh_service.py` registration** — resolve the §5/§6 tension (`sc query NHMotherbase`).
8. **Mobile companion** + **canvas** (icons → interactivity → `/generateincanvas` last).
9. **HUD redesign** — after accretive store and filter are built.
10. **Doc/code consistency (§3F)** — reconcile the old "explicit approval" framing (still in `.cursorrules` and older files) with the accretive/membrane model.
11. **Folder cleanup** across the three scattered locations.

---

## 11A. SETTLED THIS SESSION — THE STEP-2 SEED-INGEST DECISIONS  [BUILT for conversations-002; pattern set for the rest]

*Recorded so this reasoning is never re-fought. These are the decisions behind the 188 records now in the store.*

- **Unit = per-message for the JSON seeds.** Rule for picking a provisional unit: **pick the finest boundary the file already gives you, because too-coarse can't be undone (you can't un-weld a blob) but too-fine can always get a coarser reading ADDED later.** The JSON files already mark each message (`mapping → message.author.role → content.parts[]`), so per-message is the finest *non-interpretive* cut — honoring boundaries the data already has, NOT judging where a meaning starts (that judgment is §7C, unsolved, untouched). The `.txt` seeds: per-block where boundaries exist (`gpt_purified_history.txt`), per-file/coarser where they don't (`cleaned_history (1).txt`).
- **Subject = honest provenance placeholder** (`seed:conversations_002`), NOT a meaning. Before anything has read a piece, the only TRUE thing about it is where it came from. A real topical subject is meaning-engine output, **added later as a layer.**
- **The ChatGPT `title` is NOT the subject.** Kept in its own `source_title` field, marked as the source's label. Reason (Ness caught this): ChatGPT generates a conversation's title from the FIRST message and mostly leaves it — so the title reflects where the chat *started*, not where it *went*. Proven live in the data: a conversation titled "דרכי סיוע משפטי" (ways of legal aid) is mostly about community housing. Using the title as subject would import the EXACT error N.H exists to kill — a label frozen at the start, from local context, never re-read (violates §7A Rule 4 + Rule 5). So the title rides as honest data; the real subject is earned later.
- **Read-only on sources.** Ingest only ever READS the seed files; writing their content as new `append_root` records never modifies the originals (§7A Rule 1 + "memory only adds").
- **The general principle behind all of it:** for a provisional step you don't pick the "true" unit (nobody knows it — §7C) — you pick the choice that **destroys the least** and keeps every option open for the real reading later. Finest-boundary + provenance-placeholder + title-as-data + read-only does exactly that.

---

## KEY PRINCIPLES
Evidence over narrative (verify on disk) · one concrete step at a time · memory only adds, never edits · the gate is never automatic · the membrane (hallucination in chat, never in memory) · **input-agnostic: one engine, many front doors (§1A)** · **הכל יחסי — meaning is relative and revisable; brute fact is not (apply the relativity to meaning, not to facts)** · the AI WILL interpret — that's its nature; the job is to catch the interpretation as a dated, confidence-tagged, revisable opinion, never let it self-promote to fact · don't overclaim · it's subjective, a tool not a world, never about escaping reality — it's about refusing to let anything (even Ness's own quick conclusions) pretend to be real before it's earned it.

### TRUEST SINGLE SENTENCE
N.H gives the AI a place to be creative (the chat) where Ness is present to steer it, and a memory that only ever adds, never overwrites, so meaning can keep evolving without anything pretending to be real before it has earned it. It is subjective, it is a tool not a world, and it was never about escaping reality — it is about refusing to let reality be counterfeited.
