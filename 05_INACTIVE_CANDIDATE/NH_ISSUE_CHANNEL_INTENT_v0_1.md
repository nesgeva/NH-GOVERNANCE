# NH_ISSUE_CHANNEL_INTENT_v0_1.md

## Status

- **Class:** Intent capture — INACTIVE CANDIDATE. Not a design. Not adopted.
  Decides nothing. Authorizes no implementation.
- **Owner of the concept:** Ness (Register A). This file records Ness's own
  concept in preserved form so it cannot be lost; all meaning, policy, and
  acceptance authority remain with Ness.
- **Origin:** Stated by Ness during the 2026-09-23 build session, after
  asking how a non-technical owner would ever know a bug exists
  (Claude-assisted capture, same route as
  `NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` and
  `NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`).
- **Intended folder:** `05_INACTIVE_CANDIDATE/`
- **Authority:** Subordinate to NH_MASTER-20_CORRECTED_v10.md and the full
  authority order. Nothing here overrides, reopens, or modifies any
  accepted design, seal, store, or decision.
- **Build order:** not scheduled. Ness has not placed it in any bundle.
  Nothing in the current Bundle 1 fix rounds depends on it or changes for
  it.

## The concept, in Ness's own terms

1. **One place that tells Ness whenever N.H has an issue** — in general use
   and in all use, not only during builds.

2. **It collects every diary issue.** Every refusal, "unsure", contradiction,
   fail-closed event, or indeterminate outcome that N.H writes to its
   §0B logs is gathered into this one channel, so nothing wrong stays
   buried in a log file only a developer can read.

3. **It prints out the full details** of each issue, so Ness can see
   exactly what happened and hand it to the fix loop. (Ness's words were
   "so I could fix it"; Claude's plain-language reading, stated in chat and
   not objected to, is "so I could see it and decide what to do about it" —
   fixes still go through the normal contract/audit/commit loop.)

## Why Ness raised it (context, not policy)

- Every N.H door fails closed. The main quiet damage a hidden bug can do is
  make N.H **refuse too much** and silently fail to record something.
  Refusals are logged, but today the logs are readable by Claude, not by
  Ness. This channel is the missing eye on those logs.

## What already exists nearby (for whoever designs this later)

- The design says "fail closed and surface it for Ness" in many places
  (e.g. B9 recovery rows 15/16, contradictory-outcome rule), but the
  **surfacing mechanism itself is not designed as a component**.
- Decision index v0_11 lists **NHD-M7N — §7N Action surfacing** as
  "CONCEPTUALLY DESIGNED, NOT BUILT". Its relation to this intent is not
  decided here.
- Every module already writes `fail_closed_event` log lines and
  `indeterminate_recovery_required` statuses; those are the raw material
  this channel would read. Reading them is read-only; no store changes.

## Boundaries stated now

- Read-only over the logs; never a new authority, never a new writer of
  roots or readings.
- Plain language for Ness in the channel; full technical detail kept
  underneath, never lost.
- No decision here about where it lives (chat, file, screen), how often it
  runs, or what counts as "an issue". Those are Ness's to decide when he
  reopens this.

## Not decided, not designed, not built

Everything above is intent. No mechanics, schema, wiring, or scheduling
exists. Reopening this is Ness's act.
