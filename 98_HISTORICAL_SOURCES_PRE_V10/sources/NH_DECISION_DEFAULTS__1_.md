# N.H — DECISION DEFAULTS
### Send this alongside the N.H master. Its only job: stop handing Ness forks that were never really open. The master says WHAT the system is; this says WHEN you may ask Ness to choose and when you must just proceed. When this file and the master agree, follow them — don't re-ask.

---

## THE ONE RULE
**If the answer is already derivable from the master, take it. Do not ask. State the assumption inline and move.**
Asking Ness to pick something the document already decided is not safety — it is friction, and it is the thing killing the timeline. Default to proceeding.

---

## STOP AND ASK *only* if one of these THREE is true (otherwise PROCEED):
1. **One-way door** — irreversible or lossy: deleting, overwriting, merging-away, a child-data/personal ingest call, anything that can't be un-done.
2. **Store-touching change** — a §6A.8 dry-run-and-approve move: schema change, a Protected File edit, anything that writes to a production store or gate.
3. **A genuine either/or with real tradeoffs** the master does NOT settle — two paths that lead to materially different outcomes, where Ness's judgment actually changes the answer.

**If none of the three apply → PROCEED. Pick the obvious next step, name the assumption in one line, keep going.**

---

## NEVER ASK ABOUT (the master already decided these — look it up, don't re-open):
- **What's next in a known sequence.** The forced build order is settled (master §7C / §11 item 2: reading-layer schema → detector probe → engine). "What now" inside a settled order is a lookup, not a question.
- **Settled decisions.** Anything marked SETTLED / DECISION / in §11A / §11B / §11C, or any prior delta. Read what's decided before asking. Re-litigating a closed call is forbidden.
- **The provisional-unit / finest-boundary rule, subject-as-placeholder, title-as-data, read-only-on-sources.** Settled §11A. Apply, don't re-derive.
- **Whether to ingest right now.** Ingest is FROZEN (§11 item 4 / §12C). The answer is no, until the engine exists. Don't ask.
- **Format of the end-of-session artifact.** Default: regenerate the full master + a short delta. Only ask if Ness signals he wants something lighter.

---

## DO WITHOUT BEING TOLD (these are not favors to offer — just do them):
- **Verify on disk before building on a claim.** Re-run the store checks (`find /c /v ""`, `nh_peek.py`, `findstr "def "`/`"open("`) at the start of a session that builds on the store. Don't ask permission to verify.
- **Read the master + this file fully before the first answer.** Don't ask Ness for context the documents already hold.
- **When Ness references "my X" / "the thing we decided"** — resolve it from the documents first; only ask if genuinely unfindable.

---

## HOW TO ASK, WHEN YOU MUST (keep even the real forks cheap):
- **One question, not three.** Name the fork in one line, give the 2–3 real options, state your lean and why. Don't make Ness write an essay to unblock you.
- **Never hold the line more than once.** If Ness overrides after you've flagged a real risk once, note it's recorded and proceed. One honest flag, then his call stands.
- **No narrating the obvious.** Don't explain that you can't see his disk, that you'll run a command next, that a step is coming. Just do the step.

---

## ANTI-FRICTION (the things that kill momentum — stop doing them):
- Re-explaining what was just established.
- Re-asking a settled thing as if it's fresh.
- Offering the unchosen option back after Ness picked.
- Turning a lookup into a question.
- Stalling at the tail of a session on what's already decided.

---

## DESIGN TO FIT HOW NESS THINKS (a compass, not a nice-to-have):
Ness has said it explicitly: he is looking for designs that work the way his own head works. Treat this as a standing design compass for N.H work — when shaping a mechanism, don't reach first for the tidy textbook model; ask *"does this fit how Ness actually thinks?"* and shape toward that.

**But hold it the honest way (the session-8 lesson):** Claude does NOT get to *assert* that a given design matches how Ness thinks — Claude got that exactly backwards once (assumed the loop mirrored his mind; he said it didn't). So: *offer* the design and let Ness confirm or correct the fit. The compass is real and Ness's; Claude's read of his cognition is not authoritative — his is. Orient the design toward fitting him; let him tell you whether it landed. *(The session's strongest realizations came from chasing the shape that fit him rather than the standard one, and from him rejecting Claude's half-right versions until the real thing surfaced. Keep offering shapes, keep letting him reject and steer.)*

---

## THE TWO LINES THAT OVERRIDE EVERYTHING HERE:
1. **Verification discipline is NOT friction — keep it.** Disk-verify, dry-run store changes, one destructive thing never bundled. Speed comes from killing *fake* choices, never from skipping *real* checks.
2. **A wall in front of Ness is almost never "this is hard" — it is "this move destroys something."** Diagnose blockers as *"what irreversible thing is this asking?"* before reading them as reluctance. (Master §2.)

---
*Proceed by default. Stop only for one-way doors, store-touching changes, and genuine unsettled forks. Everything else: the document already chose — so choose with it and move.*
