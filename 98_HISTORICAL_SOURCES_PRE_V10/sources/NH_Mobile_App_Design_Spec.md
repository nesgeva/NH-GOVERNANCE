# N.H Mobile Companion App — Design Spec (v3, final structure)
*Captured June 19 2026, from a live design conversation with Nes. Hand this to Cursor or any future Claude session to pick up exactly where this left off.*

---

## Core idea

Three modes. Mode 1 stands alone. Modes 2 and 3 are **the same local AI in two different states** — not three separate systems.

```
Mode 1: Full Mode          — on-demand, direct tunnel to the real N.H
Mode 2: Local AI (online)  — independent local AI, learns via internet APIs
Mode 3: Local AI (offline) — same AI, same memory, no new learning, runs on what it already knows
```

**The single most important rule across all three: nothing connects to the real N.H system automatically, ever. The only two doors in are Manual Sync and Full Mode — both require Nes to deliberately trigger them.**

---

## MODE 1 — Full Mode (on-demand, live tunnel to the real N.H)

- Triggered **only** by an explicit Nes action — fingerprint, Face ID, or PIN. Never opens automatically, never on a schedule, never silently.
- That action opens a **Cloudflare tunnel** connecting the phone directly to the real desktop N.H app — full memory, full engine, live, real-time.
- Nes explicitly closes it when done. **The tunnel does not stay open passively** — it exists only during a window Nes deliberately created and ends.
- This is the opposite of the old always-on silent tunnel that was disabled earlier this week, and it's intentionally designed that way.

---

## MODES 2 & 3 — The Local AI (one system, two states)

A **real, small AI model runs directly on the phone**, with **its own separate memory**, completely independent of the real N.H's REALITY/SIMULATION store.

**Critical: this local AI does NOT connect to the real N.H system in any way, automatically, ever.** It answers using internet APIs (e.g. OpenRouter) and its own local memory. The only bridge to the real N.H is when Nes directly asks for it — Manual Sync or Full Mode. This independence is deliberate: it's the same principle behind every fix made earlier tonight — nothing reaches REALITY, or anything REALITY-adjacent, without a human explicitly choosing it.

### Mode 2 — Online state
- The local AI calls out via internet APIs to answer questions and **grow/improve its own local memory.**
- This is the "learning" side — every online interaction can add to what it knows.

### Mode 3 — Offline state
- Same model, same memory, no internet.
- Runs purely on whatever Mode 2 already taught it — no new API calls possible.
- If no local memory has been built up yet (fresh install, never been online), it just **silently stores** what Nes says, with no reply, until a connection returns.

---

## Manual sync — folding phone data into the real N.H

- Triggered **only** when Nes explicitly asks for it — no automatic background sync, ever.
- Requires **fingerprint/Face ID (or PIN) confirmation** before anything is sent.
- Sends what's accumulated in the local AI's memory to the desktop N.H app.
- **On arrival, it goes through the exact same SIMULATION review gate as everything else in the system.** No exceptions for phone-sourced data — same standard as a research finding, a sandbox-scored thought, anything else. Nothing from the phone gets a shortcut into REALITY.

---

## Non-negotiable security requirements (carried over from the broader audit)

1. **The tunnel (Mode 1) must be wired through real authentication** — `nh_auth.py`'s existing PIN/token mechanism, not assumed-safe because a password exists somewhere.
2. **No raw OS command execution, ever, from phone input.** `nh_pc_agent.py`'s `run:` trigger (direct `os.system()` execution) is explicitly **not** part of this design and should be removed outright, not extended or reused.
3. **All locally stored data — in any mode — is encrypted at rest.**
4. **Phone-originated data is never promoted directly to REALITY** — always SIMULATION first, always reviewed.
5. **The local AI (Modes 2 & 3) never auto-connects to the real N.H system** — only Manual Sync and Full Mode bridge the two, and both require explicit human action.

---

## Open questions — not yet decided, for next session

- Which small on-device model fits Modes 2 & 3 (size vs. quality tradeoff for phone hardware)
- Exact format/structure of the local AI's own memory store on the phone
- iOS vs Android feasibility differences for running a local model continuously in the background
- Exact wiring: how `nh_auth.py` extends to gate Full Mode's tunnel specifically
- What exactly gets sent during Manual Sync — the whole local memory, or just new entries since the last sync

---

## Why this design is good, not just "good enough"

- Nothing happens automatically — every meaningful action (Full Mode's tunnel, Manual Sync) requires deliberate human confirmation.
- The dangerous always-on remote-access pattern is gone by design, not just disabled and hoped-for.
- The local AI is genuinely independent — it has real memory and works offline, without ever being a hidden backdoor into the real N.H.
- This design directly applies the night's core security lesson (nothing automatic reaches REALITY) to a brand-new part of the system, before it was even built — not bolted on after the fact.

This is ready to be turned into actual build steps (file structure, what Cursor builds first, in what order) whenever Nes wants to start.
