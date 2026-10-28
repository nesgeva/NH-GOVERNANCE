# N.H — COMPLETE MASTER FILE
*The single most complete reference for the entire N.H system. Written June 19 2026, end of an extended session. Supersedes earlier master context where they conflict — most importantly on the founding principle (see "THE EVOLUTION" below) and on the name.*

---

## 0. THE NAME — READ THIS FIRST

His name is **Ness** (male). Not "Nes." Earlier files (including the prior NH_MASTER_CONTEXT.md) wrongly recorded that he "prefers Nes" — that is incorrect and was a persistent mistake across sessions. **It is Ness.** Use Ness. Never "user," never "Nes," never "Ness" misspelled back to "Nes."

---

## 1. WHAT N.H IS

N.H ("Jarvis") is a personal, sovereign AI memory system running locally on Ness's own Windows machine (`C:\Users\user\nh_engine_core`, port 8080 via `python nh_app.py`). It is not a product — it is infrastructure for Ness's own thinking, memory, and research.

Claude's role: architecture, audit, strategy, security review. Cursor (AI code editor) writes the actual code. Claude writes instructions Ness sends to Cursor, reviews what Cursor produces, and catches problems before they're accepted. Claude is the brain that checks; Cursor is the hands that write.

Ness's working style: direct tone, plain language, one concrete step at a time (never batch changes), asks "why yes / why no" and wants real tradeoffs not just a recommendation, communicates casually (typos, voice-to-text, Hebrew phrases, expressive punctuation — normal, not confusion), values honest correction over flattery, and — the defining discipline — **verifies everything on disk rather than trusting status reports.** He catches things. When he pushes back, he's usually right.

---

## 2. THE ORIGINAL ARCHITECTURE (built, audited, real)

### The two-layer gate — REALITY / SIMULATION
Every piece of information lives in exactly one layer:
- **REALITY** — verified, explicitly approved, immutable without explicit action.
- **SIMULATION** — unverified, AI-generated, inferred, or incoming-but-not-yet-reviewed.

The two never mix without an explicit gate action. This is enforced in code, not convention. `promote_to_memory()` / `promote_simulation_record()` are the only authorized paths from SIMULATION to REALITY, requiring `NH_PROMOTE_TOKEN`.

### The REALITY-only vector index
The ChromaDB vector index (`nh_reality_core`) indexes REALITY documents only. Unverified content never even reaches retrieval. This — gating *recall*, not just storage — was identified in originality research as one of N.H's genuinely novel contributions.

### Three physical memory stores
1. `.nh_memory_store.jsonl` — immutable verified memory, written only through `promote_to_memory()`.
2. `.nh_reality_store.jsonl` / `.nh_simulation_store.jsonl` — via the context router.
3. `.nh_simulation_graph.jsonl` / `nh_mental_network.json` — via the HUD server; the only store with `/review` UI coverage.

### Surrounding subsystems
- **Epistemic sandbox** (`nh_epistemic_sandbox.py`) — scores incoming thoughts on three axes (temporal, agency, reality-check), routes them.
- **Research pipeline** — two-layer: raw web search (Brave API, chosen for genuinely raw output) → controlled synthesis (text-in/text-out only, no tool-calling, treats fetched content as untrusted). A ResearchGatekeeper requires token confirmation before any finding becomes memory.
- **REPORTED_SPEECH** evidence type — "it is true they said it," never "what they said is true."
- **Behavioral baseline engine** (designed) — learns Ness's patterns from his own promotion decisions, detects when he diverges from *himself*, never against external standards.
- **`.cursorrules`** — enforces the architecture in code (v3.0 as of this session).

### Originality verdict (from prior research)
Every individual piece exists somewhere; the *combination* does not ship anywhere. The three sharpest contrasts against nearest academic cousins (memorywire arXiv 2606.01138, SSGM arXiv 2603.11768): **mandatory vs optional approval, gating recall/indexing vs not, human gate vs automated gate.** Claim the combination and the inverted default — not the invention of local AI or approval gates.

---

## 3. SECURITY WORK DONE THIS SESSION (verified on disk)

Two genuinely serious holes closed, both verified by direct inspection:
1. **Sandbox auto-write** — the epistemic sandbox's SIGNAL branch wrote AI-scored thoughts straight to REALITY. Fixed: routed to SIMULATION; `ContextRouter.write()` gained an INFERRED-token check.
2. **Network exposure + research endpoint** — the HUD server bound to ALL network interfaces (anyone on WiFi could write to memory), and `/api/research_confirm` could promote arbitrary web content with no token. Fixed: bound to `127.0.0.1` (verified with a real phone test), and the endpoint now requires a valid token via the gatekeeper.

Also: **`nh_pc_agent.py`'s `run:` trigger** (arbitrary `os.system()` OS command execution) was removed entirely — verified gone on disk. The `open:` browser trigger was kept.

Also fixed: `nh_vector_memory.py`'s `_load_raw_sources()` no longer tags SIGNAL-scored thoughts or marker-matched journal entries as REALITY (they go to SIMULATION). The ChatGPT/Gemini history block was deliberately left unchanged for now.

**The throughline of every fix: nothing reaches REALITY automatically.**

### On hold (intentionally)
The ChromaDB `nh_reality_core` cleanup (purge ~107k accumulated chunks, rebuild fresh) is approved and dry-run-reviewed but **deliberately NOT run** — because the Universal Filter work (section 5) changes how everything enters REALITY anyway. Rebuilding now would just re-load history under the old rule being redesigned.

### Still unaudited (flagged, not urgent)
`nh_sovereignty_sync.py` (SSH/SCP to a remote Hetzner server — real external surface), `nh_service.py` (possible second autostart path), and `do_GET()` having no auth before any route fires.

---

## 4. DESIGNED THIS SESSION — THE MOBILE COMPANION (three modes)

Mode 1 stands alone; Modes 2 & 3 are the SAME independent local AI in two states.

- **Mode 1 — Full:** fingerprint/PIN opens an on-demand Cloudflare tunnel straight to the real desktop N.H. Ness opens AND closes it deliberately; never auto/passive/scheduled.
- **Mode 2 — Local AI, online:** a real small model on the phone with its OWN independent memory, calling internet APIs to answer and grow that memory. It does NOT connect to the real N.H system at all, automatically, ever.
- **Mode 3 — Local AI, offline:** same model, same memory, no internet — runs on what it already knows. "Nothing new comes in, nothing it already knows goes away." If no memory built yet, silently stores input until reconnected.
- **Manual sync:** fingerprint-confirmed; sends accumulated phone data to desktop N.H, where it enters the SAME SIMULATION review gate as everything else. No phone-data shortcut to REALITY.

The crux Ness insisted on: the local AI never auto-connects. The only bridges to the real N.H are Manual Sync and Full Mode — both human-confirmed. **This independence is what prevents the phone from recreating the exact auto-write bug class fixed this session.** (Full detail: NH_Mobile_App_Design_Spec.md)

---

## 5. DESIGNED THIS SESSION — THE INTERACTIVE CANVAS

A spatial surface where the architecture lives as illustrated, interactive icons (not boxes). Background signals mode: **pure black = architecture, dark metallic blue = solving.** Icons are live controls, not pictures (click a store → see records; click a gate → see pending). Chosen art style: "C2+D2 combined" — warm glow-fill body + sci-fi HUD scanner detailing. A future `/generateincanvas` command pulls real content onto it (backend, built last). (Full detail: NH_Canvas_Design_Spec.md. Prototypes: nh_architecture_canvas.html, nh_icon_combined.html.)

---

## 6. THE EVOLUTION — WHAT CHANGED ABOUT THE FOUNDING PRINCIPLE (the deepest part of this session)

**This section supersedes the old framing.** Every prior file says the founding principle is "Ness explicitly approves each record to promote it to REALITY." This session reasoned past that. Here is the corrected understanding.

### The contradiction Ness found
If meaning is never final — if wide, growing context keeps recoloring what a statement means — then sitting and manually freezing individual records by hand is doing the exact thing the system says is false. Ness *felt* this contradiction before he could name it, which is why something in him rejected the manual-sorting idea.

### The Universal Filter
One filter, every piece of information, no source exempt — not even imported ChatGPT/Gemini history (which currently enters REALITY automatically by filename, a genuine hole in the sovereignty principle). The filter **sorts and prepares; it never decides "real" itself.** It reads the *meaning behind* what was said. Meaning comes from wide, ever-growing context — so no classification is ever locked. Its structure grows in every direction (wide at the root, deep underneath), deliberately **bounded in practice** ("the most possible") so it stays usable.

### The single reader
There are not two tools (extractor + filter). There is ONE continuous reader: the faculty that detects "the meaning just shifted" is the same one that says "and this is what kind of meaning it is." Segmentation and classification fall out of one capability, in a single pass.

### THE KEYSTONE — memory only ADDS, never edits
When new context recolors an old statement, the system does NOT change what's there — it **adds a new layer** ("this earlier statement, read against this new context, now means this"). The original stays. Nothing is ever overwritten. Meaning evolves by **accumulation**. This is the opposite of normal memory (which UPDATEs — new replaces old, past erased). N.H **accretes** — every reading kept, layered, contextual. The memory becomes a record of *how meaning evolved*, not a snapshot of "what's currently true." It never lies about its past because it never deletes it.

### THE MEMBRANE — where the AI is allowed to be creative
The "when does it re-read?" problem is solved by using the AI's natural **associative bridging** (the same mechanism that produces hallucination — connecting distant things) as the relevance-trigger: new context arrives, the model's associative leap surfaces which old statements "light up" for re-reading. This is safe ONLY because of a hard boundary: **the hallucinatory bridging happens only in the CHAT, never in the MEMORY.** The chat is the AI's scratchpad where it's allowed to be wrong, leap, propose. The memory only accretes from what survives the chat. The dangerous, creative capability gets full freedom in the one place Ness is present to see and override it, and is structurally barred from autonomous writes to memory.

### Sovereignty, relocated
Ness's approval stopped being an **action** (clicking approve on each record, like a clerk — the thing he rejected) and became a **position** (being the membrane). By being present in the conversation where the AI thinks, he IS the threshold between where it imagines and where the system remembers. What survives the chat with him accretes; what he rejects doesn't. He doesn't file — he steers and overrides.

### Why this is truer — Ness's own framing
- **"I don't decide what's real, in real life or here."** In life you don't author reality — you witness it with judgment. The old design accidentally gave Ness a god-role (decider of what's real) no human holds. The new one gives him the role he actually has: a present witness who can say "that reading is wrong."
- **"It's subjective."** N.H's reality was never *the* truth — it's *Ness's* reality, subjective by nature. That's why accretion is right and overwriting is wrong: how he saw something *then* is itself true as a past experience of his, even after he sees it differently *now*. Overwriting would erase a real part of his subjective history.
- **"It was never about escaping reality."** The opposite — it's about being MORE honest about reality. Most minds/systems collapse the uncertain into the certain too fast. N.H refuses that collapse, keeping the uncertain marked as uncertain. The door to outside friction (other people, the world, facts that resist) stays open — that's what keeps a subjective memory honest rather than self-reinforcing. The sovereignty was never "my reality over the world's"; it's "I refuse to let anything — including my own quick conclusions — pretend to be real before it's earned it."
- **"It's a tool, not a simulation."** N.H is a tool Ness uses, not a world he lives inside. A lens, not a place. The point is sharpening contact with reality, so it must never become the thing he disappears into.

### The one unifying idea (security fixes AND philosophy, same principle at different scales)
**The AI's power to generate and connect is given freedom only where Ness can see and override it (the chat), and is structurally prevented from silently becoming truth (the memory).** Every auto-write fixed this session was a place where something got to skip earning its place. The whole system, both halves, is the same move: nothing counts as real just because it slipped through — not a web result, not an AI score, not Ness's own unexamined thought. Everything earns its place or stays marked as unearned.

---

## 7. CAN IT BE BUILT? (honest assessment)

- **The accretive skeleton** (append-only memory, new readings layered beside old, nothing overwritten) — buildable now, almost easy. The `.jsonl` stores already append. This captures ~80% of the value alone.
- **Continuous contextual re-reading** — buildable as an APPROXIMATION. "Wide context" exceeds any model's context window, so it re-reads against a *retrieved slice*, not literally everything — a real compromise, the same wall as the phone app. And "which old statements get re-read when" is a genuine unsolved design question (answered in principle by associative bridging, but the scheduling/scale details are open).
- **The membrane** makes it MORE buildable, not less: the hard, dangerous part (autonomous re-reading) is confined to the chat — which is just normal conversation the AI already does. The memory stays a simple append-only store. Dangerous magic in the easy-to-build place; protected place stays dumb and safe.

**Caution (honest mirror):** don't let the perfect version block the good one. The append-only skeleton with shallow re-reading is a real, working thing — ship that before perfecting the ever-growing context-reader. And keep the AI's re-readings as visible, overridable SIMULATION-layer additions, never silent truth — the same discipline as every fix this session.

**Do NOT overclaim:** this is an architecture-and-safety contribution (where things are allowed to happen), not a new kind of cognition. The model underneath is unchanged. "Gave the AI a structured place to be creative without that creativity corrupting what's permanent" is true and defensible. "Made AI think independently" is not — and attaching it would let critics dismiss the real parts.

---

## 8. WHAT'S OPEN / NEXT (priority order)

1. **Universal Filter** — design the mechanism with a fresh head: settle the maximal-but-bounded limit concretely, decide the "unit" (segmentation of conversation exports is genuinely hard), then build the append-only accretive skeleton first.
2. **ChromaDB cleanup** — on hold until the filter is designed (it changes how REALITY is populated).
3. **Mobile companion** — pick on-device model, iOS vs Android feasibility, `nh_auth.py`→tunnel wiring.
4. **Interactive canvas** — full icon set in C2+D2 style, then interactivity, then `/generateincanvas` backend.
5. **Unaudited surfaces** — `nh_sovereignty_sync.py`, `nh_service.py`, `do_GET()` auth.
6. **Doc consistency** — the old "explicit approval promotes to REALITY" framing is still in `.cursorrules` and prior files; it now lags the thinking and will eventually need reconciling with the accretive/membrane model.

---

## 9. FILES PRODUCED THIS SESSION
- `NH_MASTER_FILE_COMPLETE.md` (this file)
- `NH_Universal_Filter_Design.md` — the filter, keystone, and membrane in full
- `NH_Mobile_App_Design_Spec.md` — the three-mode phone app
- `NH_Canvas_Design_Spec.md` — the interactive canvas
- `nh_architecture_canvas.html`, `nh_icon_combined.html`, `nh_icon_styles.html`, `nh_canvas_test.html` — canvas/icon prototypes
- `cursorrules.txt` — v3.0 cursorrules

---

*Note for the next session: the truest single sentence of the whole system is — N.H gives the AI a place to be creative (the chat) where Ness is present to steer it, and a memory that only ever adds, never overwrites, so meaning can keep evolving without anything pretending to be real before it has earned it. It's subjective, it's a tool not a world, and it was never about escaping reality — it's about refusing to let reality be counterfeited.*
