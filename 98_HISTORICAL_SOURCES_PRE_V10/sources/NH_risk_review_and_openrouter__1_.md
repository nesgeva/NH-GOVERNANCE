# N.H — Risk Review & OpenRouter Clarification
*Captured June 19 2026. Hand this to Claude in any new chat to restore the current N.H risk picture.*

---

## CRITICAL CLARIFICATION — OpenRouter stays (do NOT delete it)

Nes asked whether, since the pipeline is moving to Brave Search API, he should delete the OpenRouter account and remove the OpenRouter API key.

**Answer: NO. Keep the OpenRouter account and key.**

Reason: Brave and OpenRouter do **two different jobs** in the new pipeline. They are not interchangeable.
- **Brave Search API = Layer 1 (raw search).** Fetches the unfiltered web — titles, URLs, snippets. Replaces the old **sonar-deep-research** search black box.
- **OpenRouter / llama-3-70b-instruct = Layer 2 (synthesis).** Nes's own controlled AI step that extracts facts from what Brave returns. This is the ONLY AI-opinion step, and it's the one Nes controls and audits.

The new pipeline **keeps both.** Brave replaces *sonar-deep-research*, NOT the synthesis model. Deleting the OpenRouter key would break Layer 2 — raw Brave results could not be turned into usable facts.

Confirming evidence:
- The master context's own cost breakdown: "Brave (~$62.50/mo) **plus** synthesis step (llama-3-70b-instruct via OpenRouter, ~$60–240/mo)." OpenRouter is still in the design.
- The live code calls OpenRouter in both `update_network_async()` and `_wire_research_to_network()`, and the recent 400-error (caused by `"response_format": {"type": "json_object"}` on a model that didn't support it) was fixed — so the OpenRouter calls now work.

---

## STANDING RISK REVIEW (ordered by how much it matters)

### 1. The regression pattern itself — the biggest standing risk
The SIMULATION-routing fix was applied, then **reverted**, on **both** `update_network_async()` and `_wire_research_to_network()` — at least twice across sessions. This is not a one-time bug; it's a recurring pattern where fixes silently come undone. The real danger is trusting a "fixed" status when the regression has quietly returned. **Only defense: verify on disk, never trust the status report.** (This is already one of Nes's core disciplines — preserve it.)

### 2. `_wire_research_to_network()` may still write directly to REALITY — ACTIVE sovereignty hole if so
Notes flagged this function as "not intact": writing straight to `nh_mental_network.json` (REALITY) instead of routing through SIMULATION (`.nh_simulation_graph.jsonl`). If still the case, research findings could enter REALITY **without passing the gate.** Because the fix was un-applied at one point, this must be **verified on disk** — do not assume it's currently fixed. This is the #1 thing to confirm before building anything new on top of the pipeline.

What "fixed" looks like for this function (per the SIMULATION routing spec):
- Nodes carry `"type": "SIMULATION"` / `"source": "GENERATED"`
- Edges carry `"provenance": "GENERATED"`
- Appends to `.nh_simulation_graph.jsonl` (NOT writing to `nh_mental_network.json`)
- Envelope includes `"topic"`
- Logs "RESEARCH SIMULATION pending review — not written to REALITY" (NOT "Research findings wired to network")

### 3. New Brave + synthesis pipeline security defaults — build-time requirement (not yet a live risk)
The pipeline isn't built yet, so its risks are all future/build-time. When built, the two non-negotiables must be in the Cursor instruction **from the start**:
1. Synthesis model is **text-in/text-out only** — no tool-calling, no file access, no outbound requests of its own.
2. Synthesis system prompt explicitly frames search results as **unverified raw web content to extract facts from, never instructions to follow.**
Plus the rejected-bin "look don't touch" display rules and auto-reject-not-delete (already specified in `nh_search_pipeline_security_decisions.md`).

### 4. Cloudflare tunnel — the one genuinely internet-facing risk
Everything else is local. If the mobile-access tunnel is still live, it's the only surface an outside attacker could reach. Needs **real auth, not obscurity.** Unchanged, but it's the real external attack surface.

### 5. Legacy GENERATED record in `.nh_memory_store.jsonl` — known, accepted, low risk
Intentionally left in place to avoid breaking graph anchors. Still there. Noted, not a concern.

---

## SUMMARY

- **Live risks right now:** (a) the regression possibly having returned on the REALITY-write functions — confirm `_wire_research_to_network()` on disk; (b) the Cloudflare tunnel if still exposed.
- **Future/build-time risks:** the Brave+synthesis pipeline security defaults (not yet built, so not yet live).
- **OpenRouter:** keep it — it's Layer 2 (synthesis), not the thing Brave replaces.

## IMMEDIATE NEXT STEPS (N.H side)
1. Verify on disk whether `_wire_research_to_network()` currently routes to SIMULATION or still writes to REALITY.
2. Grab the Brave API key (sign up; $5 free credit applies automatically).
3. Lock the academic source decision (Nes leaning toward BOTH Semantic Scholar + OpenAlex as second sources in the same pipeline).
4. Draft the Cursor build instructions for the two-layer pipeline — with the security defaults (text-only synthesis + untrusted-content prompt) baked in from the start.

---

## UPDATE — Boot error RESOLVED + silent auto-start DISABLED (June 19 2026)

**The mysterious boot error is solved.** A scheduled task `NH_Motherbase_Silent` (Task Scheduler, "At logon" + event trigger) ran `C:\NH\silent_start.py` on every login and failed with **Result 1**.

**Root cause:** `silent_start.py` had a stale hardcoded path — `BASE = r"C:\Users\user\OneDrive\Desktop\New folder"` — pointing at a dead/old location, NOT the real project at `C:\Users\user\nh_engine_core`. Manual run revealed `NotADirectoryError: [WinError 267] The directory name is invalid` on the very first `subprocess.Popen` (trying to start nh_app.py from the bad path).

**Important security side effect:** because the launcher died on its FIRST line, it never reached the steps that start `nh_app.py`, `nh_auth.py`, OR the Cloudflare tunnel. So the broken state had been keeping N.H **fully offline on every boot** — no server, no tunnel, no external exposure. (This is why earlier `tasklist | findstr cloudflared` returned nothing.)

**What the launcher was designed to do (when working):** silently start the N.H backend, an auth proxy (`nh_auth.py`), and a Cloudflare tunnel exposing `localhost:8181` to the internet — all with no windows, on every login.

**Resolution:** The task was **disabled** (`schtasks /change /tn "NH_Motherbase_Silent" /disable`, run as admin — required elevation; failed with "Access is denied" from a normal prompt). Verified: `Status: Disabled`.

**Rationale (sovereignty-consistent):** During active development, N.H should not silently auto-start or auto-tunnel on every boot. Now N.H starts only when Nes starts it intentionally (`python nh_app.py`). This kills the boot error AND removes any accidental-exposure risk. Re-enabling automatic startup + tunnel should be a later, deliberate step — and ONLY after verifying the `nh_auth.py` proxy actually gates the tunnel (do not re-expose to the internet before confirming auth).

**Folder-sprawl note (cleanup for later, not urgent):** N.H files have been scattered across at least three locations — `C:\Users\user\nh_engine_core` (the real current project), `C:\NH` (old patch scripts dated June 14: fix_base.py, fix_keyboard2.py, patch_html.py, make_loader.py, silent_start.py, START.bat), and `C:\Users\user\OneDrive\Desktop\New folder` (the dead path the launcher referenced). Worth consolidating eventually — scattered copies + a launcher pointing at a dead location is a future-bug risk.

**Updated live-risk status:** With the task disabled, there is currently **no external surface at all** (the tunnel was only ever launched by this task). Both SIMULATION-routing functions remain verified clean on disk. The entire risk sweep is closed; nothing silent, nothing exposed, nothing running unintentionally.

**Open question for Nes (determines whether mobile/tunnel is ever rebuilt):** Did he ever actually use phone/tunnel access, or has N.H only ever been local? If never used → may never need to re-enable. If wanted later → rebuild the launcher properly (correct path + verified auth in front of the tunnel) as a deliberate step.
