# N.H — SIMPLE BUILD CHECKLIST
### V = built & verified on disk · X = not built yet
*Snapshot June 20 2026. Honest status, no inflation. Ness's project.*

---

## CORE — THE FOUNDATION (the hard, novel part)

- **[V]** REALITY / SIMULATION two-layer memory — enforced in code
- **[V]** SIMULATION→REALITY gate — `promote_to_memory()`, the one authorized gate
- **[V]** `update_network_async()` routes to SIMULATION (not REALITY)
- **[V]** `_wire_research_to_network()` routes to SIMULATION, stamps GENERATED
- **[V]** `/review` UI — Promote / Reject cards, tested end-to-end
- **[V]** ChromaDB `nh_reality_core` indexes REALITY only (SIMULATION excluded)
- **[V]** REPORTED_SPEECH evidence type ("true they said it," not "it's true")
- **[V]** Encryption at rest (AES-256, `enc:v1:` prefix) for sensitive records
- **[V]** Web results labeled INFERRED, not "OBJECTIVE FACTS"
- **[V]** TEST_MODE flag (no burning API money while testing)
- **[V]** `run:` arbitrary-command trigger removed (security hole closed)
- **[V]** Chat interface + HUD server running (port 8080)
- **[V]** Silent auto-start disabled (no accidental internet exposure)

---

## RESEARCH PIPELINE

- **[V]** Two-layer design decided (Brave raw → llama synthesis)
- **[X]** Brave Search API wired in and working (`test_brave.py` still pending)
- **[X]** Academic source added (Semantic Scholar / OpenAlex)
- **[X]** Security defaults baked in (text-only synthesis, untrusted-content prompt)
- **[X]** Nightly autonomous scraper actually running (`nh_nightly.py` exists, not wired)

---

## THE NEW DESIGN — UNIVERSAL FILTER & MEANING ENGINE

- **[V]** Designed (rules file + meaning-engine file — done today)
- **[X]** Append-only accretive store (the buildable-now skeleton)
- **[X]** Read-only, subject-tagged, clickable log
- **[X]** The chain-of-webs reader (intent, deixis, common ground, implicature, ToM...)
- **[X]** Nightly inward+outward research to fill webs
- **[X]** Hold-until-enough + inform-don't-ask loop
- **[X]** Universal Filter replacing the old "REALITY by filename" path
- **[X]** ChromaDB `nh_reality_core` cleanup (on hold until filter is built)

---

## AUTH / SECURITY (designed, not built)

- **[X]** Dry mode (default, no personal data loaded)
- **[X]** Personal mode (PIN unlocks history/medical/speech)
- **[X]** Tiered step-up auth (fingerprint > PIN > voice)
- **[X]** Raw-vs-derived dial (shaped-by data without spilling raw records)
- **[X]** `do_GET()` auth (currently no auth before routes — flagged)
- **[X]** Audit `nh_sovereignty_sync.py`, `nh_service.py` (never reviewed)

---

## MOBILE COMPANION (designed, not built)

- **[X]** Mode 1 — full tunnel to real N.H (fingerprint-opened)
- **[X]** Mode 2 — local AI, online, own memory
- **[X]** Mode 3 — local AI, offline
- **[X]** Manual sync (phone data → SIMULATION review gate)
- **[X]** Phone-side modes (emergency record, breathing, night lockout, kill switch)

---

## INTERACTIVE CANVAS (designed, prototypes only)

- **[V]** Standalone HTML prototypes exist (C2+D2 style)
- **[X]** Full icon set built
- **[X]** Icons as live controls (click store → records)
- **[X]** `/generateincanvas` backend (built LAST — touches real system)

---

## OTHER UNBUILT

- **[X]** Phone-data importer (every item enters as SIMULATION)
- **[X]** Behavioral baseline wellbeing engine (Ness-vs-Ness divergence)
- **[X]** Memory browser (read-only view of the store)
- **[X]** Personality modeling (rehearse hard conversations from call transcripts)
- **[X]** Voice in/out (Whisper + TTS)
- **[X]** Multi-project folder split (Different vs Invasives isolation)
- **[X]** Multi-perspective "according to whom" field
- **[X]** Folder cleanup (scattered across nh_engine_core, C:\NH, dead OneDrive path)

---

## THE HONEST PICTURE

**The foundation — the part that decides what's allowed to become true — is built and verified.** That's the hardest, most novel piece, and it's real. Everything marked **[X]** builds *on top of* it; none of it requires re-architecting.

**Smallest real thing to build next** (your own master file says so): the **append-only store + read-only log**. The `.jsonl` stores already append, so it's "almost easy" and captures most of the value. Build that, verify on disk, stop. One concrete step — not a batch.
