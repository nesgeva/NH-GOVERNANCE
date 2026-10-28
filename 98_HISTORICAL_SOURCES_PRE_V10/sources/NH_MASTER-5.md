# N.H — MASTER (complete, consolidated)
### The single N.H system reference. Replaces every scattered N.H file in the project.
*Rebuilt June 20 2026 from a full read of all project files. Updated June 20 2026 (session 2) with all security fixes and launcher corrections. About the N.H system ONLY — nothing about the anime. Two companion design files go deeper where noted: `NH_Universal_Filter_RULES.md` and `NH_Meaning_Engine_Design.md`.*

> **THE NAME:** He is **Ness** (male). Not "Nes," never "user." Older files (the original `NH_MASTER_CONTEXT.md` and others) wrongly recorded "prefers Nes" — a persistent cross-session error. He signs his own name **Ness**. Use Ness.

> **HOW TO READ THIS FILE:** N.H is mid-evolution. The system **as it currently runs on disk** works one way; the system **as now designed** works another. This file marks both honestly — **[BUILT]** = on disk today, **[DESIGNED]** = decided but not coded. Section 3 lays out the whole old→new shift as issues and solutions, so nothing old is presented as if it were the current target.

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

## 2. HOW TO WORK WITH NESS

- **Direct tone, plain language, ONE step at a time** — never batch changes. He asks "why yes / why no" and wants the real tradeoffs, not just a recommendation.
- **Verify on disk, never trust status reports.** `findstr`, `inspect.getsource()`, file reads. This has caught real regressions repeatedly. "Applied" is never "verified."
- **Honest correction over flattery** — explicitly and repeatedly asked for.
- **Pull Sovereignty** — no unsolicited pushes; Ness sets direction.
- **Casual comms are normal** — typos, voice-to-text, Hebrew, expressive punctuation are NOT distress or confusion.
- **He catches things.** When he pushes back, he is usually right.
- **Primary risk pattern: scope expansion before consolidation** — names a principle, builds something that quietly violates it, catches it by evidence, fixes it, then expands again before verifying the current layer. Finish and verify what's in front before starting the next thing.
- **Claude's role:** architecture, audit, security, strategy — the brain that checks the work. **Cursor** writes the code. Ness runs every command in cmd and verifies on disk. Claude never edits code directly. Ness calls this Claude role "JARVIS."
- **Session workflow:** one topic per chat, start fresh when a topic closes. End of session: tell Claude what was done → Claude generates new master file + short delta → Ness reads the delta, swaps the file in the project.

---

## 3. THE EVOLUTION — OLD vs NEW (issues → solutions)

This is the heart of where N.H is right now. Each row is a thing the early design got wrong (or a hole found on disk), what the problem was, and the decided fix. **Some fixes are built; some are designed-not-built — marked per row.**

### A. The founding principle — manual gate → membrane
- **OLD:** "Ness explicitly approves each record to promote it to REALITY." Sovereignty = a per-record manual approval action at `/review`.
- **ISSUE:** Meaning is never final — wide, growing context keeps recoloring what a statement meant. Manually freezing individual records by hand does the exact thing the system says is false. Ness *felt* this before he could name it; it's why something in him rejected manual sorting. Two beliefs were fighting: "I must be the gate" (sovereignty) vs "nothing is ever final" (meaning keeps moving).
- **NEW / SOLUTION:** **Memory only ADDS, never edits.** New context → add a new layer beside the old reading ("read against this new context, it now means this"), never overwrite. This dissolves the contradiction: meaning stays revisable (new layers), nothing is destroyed (old layers remain), and Ness stops being a clerk (no edits to approve — only accumulation). Sovereignty becomes a **position (the membrane)**, not an action. **[DESIGNED — not built]** *(The built system still uses per-record Promote/Reject — see row B and §6.)*

### B. The "is this real?" paths — many inconsistent gates → one filter
- **OLD:** 4+ separate paths each decided "is this real" their own way: epistemic sandbox scored typed thoughts; `_load_raw_sources()` tagged imported ChatGPT/Gemini history as REALITY **by filename** with no review; the research gatekeeper handled web findings; the context router used evidence levels.
- **ISSUE:** "REALITY" didn't actually mean "Ness approved this." For imported history it just meant "was in the seed file." A new thought got scored; an old ChatGPT message got a free pass. The sovereignty principle was inconsistent at the source.
- **NEW / SOLUTION:** **The Universal Filter** — ONE filter, every piece, no source exempt (kills the load-to-REALITY-by-filename behavior). The filter **sorts and prepares; it never decides "real."** One continuous reader; meaning from wide ever-growing context; classification never locked. **[DESIGNED — not built]** (Full rules in `NH_Universal_Filter_RULES.md`; mechanism in `NH_Meaning_Engine_Design.md`; summarized in §7.)

### C. Where the AI is allowed to be creative — silent writes → the membrane
- **OLD:** the AI's associative/generative capability could reach memory automatically (auto-writes, sandbox SIGNAL straight to REALITY, research wired to REALITY).
- **ISSUE:** that's the same capability that hallucinates — letting it write to memory silently is catastrophic; a false connection becomes corruption.
- **NEW / SOLUTION:** **The membrane** — the associative/hallucinatory bridging happens ONLY in the chat (where Ness is present to see and override it), and is structurally barred from writing to memory. In an accretive memory a hallucinated re-reading can't corrupt anything — it's just another layer, a proposal Ness can reject. Dangerous magic in the one observable place; the protected store stays dumb and safe. **[DESIGNED — not built; but every concrete auto-write below was already fixed toward this principle]**

### D. Concrete security holes found on disk → fixes  **[ALL BUILT & VERIFIED]**
- **Sandbox SIGNAL auto-wrote to REALITY** → routed to SIMULATION; `ContextRouter.write()` gained an INFERRED-token check.
- **`update_network_async()` / `_wire_research_to_network()` wrote LLM output straight to REALITY** → both now route to SIMULATION (`.nh_simulation_graph.jsonl`), stamp GENERATED. *(Verified clean June 20 2026. Root cause of past reversions still unsolved — always verify on disk.)*
- **HUD server bound to ALL interfaces** (anyone on WiFi could write to memory) → bound to `127.0.0.1` only (verified with a real phone test).
- **`/api/research_confirm` could promote arbitrary web content with no token** → now requires a gatekeeper token.
- **`nh_pc_agent.py` `run:` arbitrary-`os.system()` trigger** → removed entirely (verified; `open:` browser trigger kept).
- **`_load_raw_sources()` tagged SIGNAL thoughts / marker-matched journal entries as REALITY** → no longer does.
- **pywebview / desktop launcher loading `/chat` stub instead of real HUD** → fixed in `nh_app.py` (line 318), `run_app.pyw`, and `launch_nh.vbs` — all now point at `http://localhost:8080/`. *(June 20 2026)*
- **Cloudflare tunnel auto-launching on startup** → tunnel launch block removed from both `nh_silent_start.py` and `nh_service.py`. Tunnel is for Phone Mode 1 only, deliberate and authenticated, never automatic. *(June 20 2026)*
- **`/api/simulation_confirm`, `/nightly/run`, `/readonly-on`, `/readonly-off`, `/pc_command` had no auth** → all five now require valid `NH_PROMOTE_TOKEN` before executing. *(June 20 2026)*
- **`nh_sovereignty_sync.py` used `StrictHostKeyChecking=no`** in both `_ssh_cmd()` and `_scp_cmd()` → changed to `yes`. Server not configured yet (`NH_BACKUP_HOST` not set) so sync is dormant — but the hole is closed before it activates. *(June 20 2026)*

### E. The research pipeline — opinion-filtered black box → raw + controlled synthesis
- **OLD:** `sonar-deep-research` (Perplexity) did its own searching, filtering, and relevance judgment before N.H saw anything. Every "fact" was already opinion-filtered by an outside AI — violating sovereignty even with the gate in place.
- **ISSUE:** what came through the gate wasn't actually raw, so the sovereignty was only true at the gate, not at the source.
- **NEW / SOLUTION:** a **two-layer pipeline** under Ness's control — Brave (raw fetch) → OpenRouter/llama (the one controlled, auditable synthesis step) → SIMULATION → gate. Sovereignty now true at the source. **[DESIGNED — Brave not yet wired; see §8]**

### F. Doc/code consistency — the loose end
- **STILL OPEN:** `.cursorrules` v3.0 and several older docs still carry the old "explicit approval promotes to REALITY" framing. They need reconciling with the accretive/membrane model. This is a known open task, not an oversight.

---

## 4. THE MACHINE

- **Path:** `C:\Users\user\nh_engine_core`, Windows 10 (10.0.26100.7840)
- **CPU** i5-11400 (40°C idle / 60°C load) · **GPU** RTX 2060 (35°C idle / ~40°C load) — both verified 24/7-safe
- **Launched via** `run_app.pyw` (the "N.H Interface" desktop shortcut); starts `nh_app.py` silently, opens pywebview window pointing at `http://localhost:8080/`
- **Real interface:** `http://localhost:8080/` (root = the full "N.H // MOTHERBASE AGENT" HUD, `index.html`). Pywebview now correctly loads root. `/chat` stub still exists but is no longer loaded anywhere. **HUD redesign noted for later.**
- **PC has ONE mode** — pywebview native desktop window, local only, no browser, no internet. Browsers cache to disk; pywebview does not. This is the only correct PC interface per the design.
- **Internet-facing surface:** a Cloudflare tunnel — currently **disabled on purpose**; needed only for Phone Mode 1, must be opened deliberately with auth, never on startup.
- **Hardware limit:** a 70B model can't run locally on 14GB RAM. Everything else fits.

---

## 5. THE CODEBASE MAP

**Core architecture (PROTECTED — never modify without a dry-run + explicit "APPROVED"):**
`nh_memory_store.py` (`MemoryStore`, evidence levels, **`promote_to_memory()`** — the ONE authorized gate) · `nh_context_router.py` (`ContextRouter.write()` routes to a layer; has an INFERRED-token check — NOT a gate by itself) · `nh_reality_graph.py` (REALITY/SIMULATION/PREDICTION branches) · `nh_simulation_graph.py` (`promote_simulation_record()` / `reject_simulation_record()` — the only valid SIMULATION→REALITY path) · `nh_epistemic_sandbox.py` (scores thoughts on 3 axes; SIGNAL branch now routes to SIMULATION) · `nh_evidence_integrity.py` (contains `guard_write()` — only called in its own self-test block, not in main flow; the real gate is `promote_to_memory()`) · `nh_jarvis_core.py` (the core brain; `run_nh_core_engine()` the real one ~line 1076; a dead duplicate stub exists in `core/engine.py`, zero imports; dead prompt string at lines 564 & 1015 says "OBJECTIVE" — harmless, never called) · `nh_crypto.py` (AES-256-GCM) · `nh_vector_memory.py` (ChromaDB, `AdvancedSemanticMemory`, `fit_and_index_workspace()`, `_load_raw_sources()`).

**Three physical memory stores:**
1. `.nh_memory_store.jsonl` — immutable verified memory, written ONLY via `promote_to_memory()` (verified clean: 4 records — a VERIFIED med record, an INFERRED date, one inert legacy GENERATED test record left to avoid breaking graph anchors, one encrypted REPORTED_SPEECH record).
2. `.nh_reality_store.jsonl` / `.nh_simulation_store.jsonl` — via the context router.
3. `.nh_simulation_graph.jsonl` / `nh_mental_network.json` — via the HUD server; the only store with `/review` UI coverage. `nh_mental_network.json` is written ONLY by `promote_simulation_record()`.

**Launchers (in order of what's actually used):**
- `run_app.pyw` — the real launcher; "N.H Interface" desktop shortcut points here. Starts `nh_app.py` via `pythonw.exe` (silent, no cmd window), waits 4 seconds, opens pywebview at `http://localhost:8080/`. *(Fixed June 20 2026 — was loading `/chat` stub.)*
- `launch_nh.vbs` — secondary launcher on OneDrive desktop. Also fixed to load `http://localhost:8080/`. Less important than `run_app.pyw`.
- `nh_silent_start.py` — has a **dead BASE path** (`C:\Users\user\OneDrive\Desktop\New folder`) so it starts nothing. Tunnel auto-launch removed. Effectively inert.
- `nh_service.py` — Windows Service (`NHMotherbase`). Audited June 20 2026: uses correct BASE path, starts `nh_app.py` + `nh_auth.py`. Tunnel auto-launch removed. Not confirmed as actively registered — check Task Scheduler / Services if unexpected auto-starts occur.

**Server / UI (safe to modify):** `nh_hud_server.py` (all routes — `/review`, `/speech`, `/api/research_confirm`, `/pc_command`, `/nightly/run`, `/readonly-on`, `/readonly-off`; bound to `127.0.0.1`; **five sensitive routes now require `NH_PROMOTE_TOKEN`** — fixed June 20 2026) · `nh_app.py` (entry point; pywebview host) · HTML: `index.html` (real UI), `nh_chat.html` (stub — no longer loaded), `nh_simulation_review.html`, `nh_speech_form.html`.

**`_wire_research_to_network()` location correction:** this function lives in **`nh_hud_server.py`** (lines 348 and 440), not `nh_jarvis_core.py` as earlier notes implied. Verified June 20 2026: routes correctly to SIMULATION + GENERATED, queues to `.nh_simulation_graph.jsonl`, never writes to REALITY.

**Other modules:** `nh_research_engine.py` (`ResearchEngine`, `deep_parallel_research()`, `promote_finding()`, now wires `queue_for_review()`) · `nh_research_sandbox.py` (injection guard + `ResearchGatekeeper.confirm(token)`) · `nh_nightly.py` (3 AM maintenance) · `nh_auth.py` (PIN/token auth, `/auth/lock` wipes key from RAM) · `nh_sensor_bridge.py` (input; Whisper hooks future) · `nh_mobile_bridge.py` · `father_firewall.py`, `mother_mission.py`, `nh_lawyer_simulator.py`, `nh_boundary_scripts.py` (personality/confrontation sim — SIMULATION-only, never auto-promote) · `nh_behavioral_baseline.py`, `nh_metrics_tracker.py`, `nh_high_res_monitor.py`, `nh_clinical_report.py`, `nh_viz_engine.py` (wellbeing/metrics/clinical output) · `nh_evidence_processor.py`, `nh_journal_daily.py` · `nh_backup.py`, `nh_local_cleanup.py`, `nh_data_purifier.py` (infra) · `nh_pc_agent.py` (polls `/pc_command`; dangerous `run:` trigger REMOVED, `open:` kept).

**External surfaces (audited June 20 2026):**
- **`nh_sovereignty_sync.py`** — SSH/SCP to Hetzner. Audited. Dormant (`NH_BACKUP_HOST` not set in `.env`). `StrictHostKeyChecking` changed to `yes`. Safe while server not configured. Before enabling: set up Hetzner server with proper auth, add host fingerprint to `known_hosts`.
- **`nh_service.py`** — Audited. Clean. Tunnel block removed. Not confirmed as actively registered.
- **`do_GET()` auth** — five sensitive routes now protected with `NH_PROMOTE_TOKEN`. Remaining routes (`/review`, `/speech`, `/logs`, `/data`, `/readonly-status`) are read-only or display-only — acceptable at `127.0.0.1`.

**Seed data files (the hole the Universal Filter fixes — see §3B):** `cleaned_history (1).txt`, `gpt_purified_history.txt`, `conversations-000/001/002.json`. These currently load into REALITY automatically *by filename*.

**Legacy stack (READ ONLY until migration done):** `nh_mental_network.json` + ChromaDB `nh_reality_core` + `nh_timeline.json` + `nh_nightly.py`. **New stack (use this):** `MemoryStore → RealityGraph → ContextRouter → EpistemicSandbox`.

**`.cursorrules` v3.0:** all REALITY writes go through the authorized gate; every REALITY record needs `source`/evidence-level/`timestamp`/`type`; valid REALITY types VERIFIED/CONFIRMED/CLINICAL — never GENERATED/INFERRED/SIMULATED; SIMULATION never reaches REALITY without a valid `NH_PROMOTE_TOKEN`; dry-run + "APPROVED" before touching a protected file; no placeholders/`# TODO`; async store writes awaited and result-checked; any autonomous task needs `# AUTONOMOUS: approved by user [date]`; Pull Sovereignty. *(Note: still carries the old founding framing — see §3F.)*

---

## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT]

- **REALITY/SIMULATION two-layer gate**, enforced in code.
- **`promote_to_memory()`** — the one authorized gate; blocks GENERATED, blocks INFERRED without token, blocks REPORTED_SPEECH missing speaker/quote.
- **The current gate flow (the old-model mechanic, still what runs today):** SIMULATION records appear as cards at **`/review`**; **Promote** → `promote_simulation_record()` writes to `nh_mental_network.json`; **Reject** → `closed_case` marker, cleared from queue but kept in log. Proven end-to-end: a reply landed in SIMULATION, sat in the queue, Ness clicked Promote, and it entered the REALITY graph by his choice alone. *(This per-record approval is exactly what §3A's membrane model is designed to eventually replace — but it is what exists now, and it works.)*
- **REALITY-only vector index** — ChromaDB `nh_reality_core` indexes REALITY docs only; SIMULATION excluded at index time. (Gating *recall*, not just storage — a genuinely novel piece.)
- **REPORTED_SPEECH** — "it is TRUE they said it," never "what they said is true." Stores speaker + exact quote, encrypted at rest (AES-256, `enc:v1:`). Manual entry at `/speech`.
- **Encryption at rest** for sensitive records · **web results relabeled** INFERRED (not "OBJECTIVE FACTS") · **TEST_MODE flag** (no burning API money while testing) · **epistemic sandbox** (temporal/agency/reality axes) · **working chat + HUD server** · **silent auto-start disabled**.
- **All the §3D security fixes** are built and verified on disk, including all June 20 2026 additions.
- **pywebview shows real HUD** — `nh_app.py`, `run_app.pyw`, `launch_nh.vbs` all corrected. Native desktop window loads `http://localhost:8080/` (the full MOTHERBASE AGENT HUD). Verified live June 20 2026.
- **Tunnel auto-launch removed** — `nh_silent_start.py` and `nh_service.py` both cleaned. Tunnel is deliberate Phone Mode 1 only.
- **Five routes token-gated** — `/api/simulation_confirm`, `/nightly/run`, `/readonly-on`, `/readonly-off`, `/pc_command` all require valid `NH_PROMOTE_TOKEN`. Verified on disk June 20 2026.
- **`nh_sovereignty_sync.py` hardened** — `StrictHostKeyChecking=yes` in both SSH/SCP commands. Dormant until `NH_BACKUP_HOST` configured.

**Known regression pattern:** the SIMULATION-routing fix (`nh_vector_memory.py` 357/364, `nh_jarvis_core.py` 828/948) has silently reverted at least twice in past sessions. Verified clean June 20 2026. Root cause unsolved. Always re-verify on disk at the start of a session before building on top of it. Dead prompt string at `nh_jarvis_core.py` 564 says "OBJECTIVE RESEARCH" — it's label text inside a prompt template string, never a code decision, harmless.

---

## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [DESIGNED — not built]

*Full rules in `NH_Universal_Filter_RULES.md`; full mechanism in `NH_Meaning_Engine_Design.md`. Summary so this file stands alone. (The "why" — the old→new shift this resolves — is in §3A–C.)*

**The single reader:** not two tools (extractor + filter) — ONE continuous reader. Finding where a statement begins/ends and naming its meaning-type are the same act, one pass.

**THE KEYSTONE — memory only ADDS, never edits.** New context recolors an old statement → add a new layer, never overwrite. Meaning evolves by accumulation. Opposite of normal memory (which UPDATEs). N.H **accretes** — a record of *how meaning evolved*, never lying about its past because it never deletes it.

**THE MEMBRANE — where the AI is allowed to be creative.** "Which old statements get re-read?" is answered by the AI's natural **associative bridging** (the same mechanism that produces hallucination). Safe ONLY because the bridging happens only in the CHAT, never in the MEMORY. Chat = scratchpad, allowed to be wrong. Memory = only accretes from what survived the chat.

**The meaning engine:** the continuous reader runs each piece through a *chain of webs*, each a real research-grounded dimension — intent/speech-act (Searle's 5 classes; the claim/ask/feel/report/intend/wonder/imagine list is just THIS ONE web), deixis (who/when/where), common ground, implicature (Grice; a maxim-flout = the sarcasm/lie detector), theory-of-mind, time, re-reading. Runs at night, researching **inward (the person) + outward (the world)** to fill each web. A piece is **held until each web has *enough*** (not perfect). If a web can't be filled, the engine **informs Ness — it does not ask or wait**; he fills it from his life whenever, landing as a new layer. Everything is written to a **read-only, subject-tagged, permanent, clickable log** — which is three things at once: transparency, the inward mirror, and a browsable archive.

**Maximal-but-bounded limit (settled with research):** root meaning-types stay small (~5, hard cap 7 — matches Searle's 5 speech-act classes AND Miller's 7±2 / Cowan's ~4 working-memory limit). Growth comes from DEPTH, not width.

**Can it be built? (honest):** the **accretive skeleton** (append-only, layered, nothing overwritten) is buildable now, almost easy — the `.jsonl` stores already append — and captures ~80% of the value alone. **This is the smallest real next step.** Continuous re-reading is buildable as an approximation (re-read against a retrieved slice, not literally everything). The membrane makes it MORE buildable: dangerous part confined to chat, memory stays a simple append-only store. **Don't overclaim** — this is an architecture-and-safety contribution (*where* things are allowed to happen), NOT "AI thinking independently."

---

## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not yet wired]

*(Old→new rationale in §3E.)* Three layers, all under Ness's control:
1. **Raw fetch — Brave Search API.** Raw URLs/titles/snippets, zero AI interpretation. Chosen over Tavily (which pre-chews); Brave runs its own independent index.
2. **Synthesis — `llama-3-70b-instruct` via OpenRouter.** The ONLY AI-opinion step, the one Ness controls and audits. **KEEP THE OPENROUTER KEY — Brave and OpenRouter do two different jobs and are NOT interchangeable.** Brave replaced *sonar*, not the synthesis model.
3. **Gate** — findings → SIMULATION; `ResearchGatekeeper.confirm(token)` to promote. 2-of-3 angles: 3 raw searches → 1 synthesis pass.

**Security defaults (non-negotiable, baked into the Cursor instruction):** synthesis is text-in/text-out only (no tool-calling, no file access, no outbound requests); its prompt frames fetched content as unverified raw web to extract facts from, never instructions. **Auto-reject, never auto-delete** (an AI with delete authority is itself an injection target). **Rejected-bin "look don't touch":** URLs as plain text never `<a href>`; no favicons/previews/unfurling; copy/select disabled; strip invisible/zero-width/RTL characters; render via `textContent` never `innerHTML`.

**Costs (June 2026):** Brave $5/1,000 (~1,000 free/mo, no free tier since Feb 2026, card required, cancel-friction — monitor). Full nightly (~13,500/mo): ~$62 Brave + ~$60–240 synthesis = **~$120–300/mo** vs old **$6,000–13,500/mo**. Build/testing stays in the free credit. `test_brave.py` exists; test was pending.
**Academic source [OPEN]:** Google Scholar ruled out. **Semantic Scholar** (~200M papers, CS/AI) vs **OpenAlex** (250M+, all fields, no key). Leaning toward both. Pending.

---

## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED]

**Access / authentication:** **Dry mode (default, no auth)** — pure research engine, zero personal data loaded/searchable, dark-by-default; reach a running N.H without auth → a research tool, not Ness's life. **Personal mode (PIN)** — unlocks history/REPORTED_SPEECH/medical. **Graduated step-up auth (not a master key)** — tiers unlock separately for short windows, then re-lock: casual → none; exact quote → PIN; medical → PIN + fingerprint. **Factor hierarchy:** fingerprint (strongest — lean on Windows Hello / phone sensor, don't build a matcher) > PIN (everyday; exists in `.nh_pin.json`) > voice (softest — convenience only, NEVER a hard lock; fails when stressed/sick/crying = lockout when most needed). **Raw-vs-derived dial:** N.H is *shaped by* personal data but doesn't *spill* raw records by default — a step converts relevant data to a derived signal; raw quotes stay in the vault (exception: explicit authenticated request for an exact REPORTED_SPEECH quote). **Access layer:** trusted app only (desktop pywebview + phone), not a plain browser (browsers cache to disk); zero-copy — load live, retain nothing on close. The dry/personal boundary must be real at code level.

**Mobile companion (three modes):** Mode 1 stands alone; Modes 2 & 3 are the same local AI in two states. **Rule across all three: nothing connects to the real N.H automatically, ever** — only Manual Sync and Full Mode bridge, both deliberate. **Mode 1 — Full:** fingerprint/PIN opens an on-demand Cloudflare tunnel to desktop N.H; opened AND closed deliberately. **Mode 2 — Local AI (online):** a real small on-phone model (1–3B) with its OWN separate memory, calling internet APIs to grow it; never auto-connects. **Mode 3 — Lite/offline:** same model/memory, no internet; if memory empty, silently stores input until reconnected. **Open question:** whether Lite Mode carries cached facts as context (so it still feels like *his* AI) or goes generic — Ness said "idk," unresolved. **Manual Sync:** fingerprint-confirmed; phone data → same SIMULATION review gate. Hard rules: Mode 1 tunnel wired through real `nh_auth.py`; `run:` stays removed; all local data encrypted.

**Interactive canvas:** architecture as illustrated, interactive icons (not boxes). Background = mode: **pure black = architecture, dark metallic blue = solving.** Icons are live controls (click a store → records; click a gate → pending). Style "C2+D2 combined" (warm glow-fill + sci-fi HUD detailing). Legend: red = core, orange = gate, purple = store. Build order: canvas surface → icon set → interactivity → blue mode → `/generateincanvas` backend LAST (only part touching the real system). Prototypes exist.

**Behavioral-baseline wellbeing engine:** learns Ness's patterns from his *own* promotion decisions; detects divergence from *his* baseline (Ness-vs-Ness, never external); tiers from silent flagging → REALITY freeze; validated by internal consistency; anchored to real appointment documents. **Caution Ness accepted:** build pure-software layers freely, but build any **sensor layers (HRV/breath) as data-loggers ONLY first** — collect, compare to what actually happened, confirm the pattern holds for him before the system acts. The "90-second early warning" is an AI hypothesis, not an established fact about his body.

**HUD redesign:** the current MOTHERBASE AGENT HUD works but needs a visual redesign. Noted as future work — do not touch until the accretive store and filter are built.

**Other unbuilt:** phone-data importer (two old Samsung phones 2017–2024 being recovered for seed material; every item writes as SIMULATION, never REALITY directly) · memory browser · personality modeling (rehearse hard conversations from transcribed calls) · nightly autonomous scraper (~150 cycles/night, all SIMULATION) · voice in/out (Whisper → `nh_sensor_bridge.py`; TTS via Piper/Coqui) · phone-side modes (emergency record, breathing reminder, night lockout, kill switch) · multi-project folder split · multi-perspective "according to whom" field · ChromaDB cleanup (~107k chunks — approved, **on hold** until the filter is built) · folder cleanup across `nh_engine_core`, `C:\NH`, and a dead OneDrive path.

---

## 10. ORIGINALITY (honest calibration, from a 2026 field survey)

Every individual brick exists somewhere (local-first personal AI: Khoj, PAI, Second Me; human-in-the-loop gates: LangGraph, Mastra; epistemic-provenance KGs; dual-LLM injection containment: CaMeL; N-of-1 baseline monitoring: clinical digital phenotyping). The **combination does not ship anywhere.** Nearest cousins are two 2026 preprints: **memorywire** (arXiv 2606.01138 — diff-and-approve, but drifts to auto-approve and leaves recall ungated) and **SSGM** (arXiv 2603.11768 — two-track memory, but automated gate, not human). **Three sharpest contrasts:** mandatory vs optional approval; gating recall/indexing vs not; human gate vs automated gate. **Claim the combination and the inverted default** (mandatory, non-bypassable human role + REALITY-only vector index + individual cognitive-sovereignty framing) — never the invention of local AI or approval gates.

---

## 11. WHAT'S OPEN / NEXT (priority order)

1. **Append-only accretive store + read-only subject-tagged log** — the buildable-now skeleton; break the design loop with running code. This is the next real step.
2. **Universal Filter / meaning engine** — settle the "unit" (segmenting conversation exports is hard), then build on the skeleton.
3. **ChromaDB cleanup** — on hold until the filter exists.
4. **Research pipeline build** — Brave key + `test_brave.py` + academic-source decision + both security defaults.
5. **Hetzner sovereignty sync** — before enabling: set up server, add host fingerprint to `known_hosts`, wire through `nh_auth.py`. `StrictHostKeyChecking=yes` already set.
6. **Mobile companion** + **canvas** (icons → interactivity → `/generateincanvas` last).
7. **HUD redesign** — after accretive store and filter are built.
8. **Doc/code consistency (§3F)** — reconcile the old "explicit approval" framing (still in `.cursorrules` and older files) with the accretive/membrane model.
9. **Folder cleanup** across the three scattered locations.

---

## KEY PRINCIPLES
Evidence over narrative (verify on disk) · one concrete step at a time · memory only adds, never edits · the gate is never automatic · the membrane (hallucination in chat, never in memory) · don't overclaim · it's subjective, a tool not a world, never about escaping reality — it's about refusing to let anything (even Ness's own quick conclusions) pretend to be real before it's earned it.

### TRUEST SINGLE SENTENCE
N.H gives the AI a place to be creative (the chat) where Ness is present to steer it, and a memory that only ever adds, never overwrites, so meaning can keep evolving without anything pretending to be real before it has earned it. It is subjective, it is a tool not a world, and it was never about escaping reality — it is about refusing to let reality be counterfeited.
