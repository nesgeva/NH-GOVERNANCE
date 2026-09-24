# NH_MASTER-20_CORRECTED_v8 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v7.md` (SHA-256: `4e89eb90e8e04140bb71951a0a9584e7ceb21bfb45f4136408277326e4bb215d`)

---

## Changes (5 passages)

### Document Identity
**Old:** `NH_MASTER-20_CORRECTED_v7.md`
**New:** `NH_MASTER-20_CORRECTED_v8.md`

### 1 — §16 Authorization Failure (preserve interrupted identity)
**Old:** "session remains `"sealed"`."
**New:** "the session remains in its existing sealed waiting state (`"sealed"` or `"interrupted"`). Failure to authorize does not rewrite an interrupted session into a normal sealed session. Both remain immutable waiting states and continue waiting indefinitely."

### 2+3 — §17 Phase 3 (blocked items prevent completion; promotion_failed session-level only)
**Old:** "All items are `"promoted"`, `"excluded"`, `"blocked"`, or `"promotion_failed"`. If none `"promotion_failed"`: session → `"promoted"`... Blocked items remain in `promotion_state` as pending, resuming automatically..."
**New:** Rewritten to: while any item is `"blocked"`, session remains `"promoting"`, completion and archiving blocked; `promotion_failed` is a session-level state triggered by non-retryable/exhausted failures; item failures tracked in `promotion_state`; completion gate: only when every item is `"promoted"` or `"excluded"` with no blocked or failed item remaining.

### 4a — §23 promotion_failed Definition
**Old:** "promotion_failed — promotion incomplete; awaiting new authorization"
**New:** "promotion_failed — promotion incomplete; next action depends on the recorded failure class and §20 (temporary technical failures retry automatically without new fingerprint; non-retryable or exhausted retries may require Ness to request a new attempt; new biometric authorization required only when the session was never successfully authorized or the original BAI token was revoked before promotion began)"

### 4b — §27 Startup Recovery for promotion_failed
**Old:** "Ness has been notified. Awaits new authorization attempt."
**New:** "Inspect the recorded failure class and follow §20: temporary technical failures retry automatically without new fingerprint; if retries exhausted or failure is non-retryable, Ness may request a new attempt. New biometric promotion authorization is required only when the session was never successfully authorized or the original BAI token was revoked before promotion began."
