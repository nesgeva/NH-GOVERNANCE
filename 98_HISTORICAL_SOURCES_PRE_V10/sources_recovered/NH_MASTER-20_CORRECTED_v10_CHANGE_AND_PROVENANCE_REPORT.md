# NH_MASTER-20_CORRECTED_v10 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v9.md` (SHA-256: `6d712e899e1f4a4e1f8ce08a7e5884fb6b04026edb2f2388928d6bc71d1fc259`)

This was one focused mechanical lifecycle reconciliation. Five regions changed: the internal identity and the four TSC sections (§17, §20, §23, §27) governing the `promotion_failed` state. No other wording, concept, function, name, schema, status, or settled decision changed.

---

## The contradiction resolved

In V9, §17 restricted entry into `promotion_failed` to "non-retryable item failure or exhausted automatic retries." But §§23 and 27 correctly stated that the next action from `promotion_failed` depends on the recorded failure class, including temporary technical failures that retry automatically under §20. V9 §17 therefore disagreed with §§23/27 about which failures may produce `promotion_failed`. V10 makes all four sections express one flow: any recorded item failure that prevents the current promotion pass from completing may enter `promotion_failed`; the recorded failure class then determines the next action under §20.

---

## Changes (5 regions)

### 1. Document Identity
**Old:** `NH_MASTER-20_CORRECTED_v9.md`
**New:** `NH_MASTER-20_CORRECTED_v10.md`

### 2. §7E-TSC §17 — Phase 3 failure entry
**Old:** "If a recorded failure prevents the promotion operation from completing (non-retryable item failure or exhausted automatic retries): session → `"promotion_failed"`; `cache_promotion_failed` written; Ness notified. The next action depends on the recorded failure class and §20. (`promotion_failed` is a session-level lifecycle state only — item failures are tracked in per-item `promotion_state` and the applicable failure audit event, not as an item lifecycle value.)"
**New:** "If a recorded item failure prevents the current promotion pass from completing: session → `"promotion_failed"`; `cache_promotion_failed` written; Ness notified. The recorded failure class determines the next action under §20 — a temporary retryable technical failure with attempts remaining retries automatically and transitions `"promotion_failed"` → `"promoting"` after the required security checks, without a new fingerprint; when automatic retries are exhausted or the failure is non-retryable, the session remains `"promotion_failed"` and Ness may request a new attempt. (`promotion_failed` is a session-level lifecycle state only — item failures are tracked in per-item `promotion_state` and the applicable failure audit event, not as an item lifecycle value.)"
**Reason:** Removes the restriction that limited `promotion_failed` to non-retryable/exhausted failures; states the full failure-class-driven flow so §17 agrees with §§20/23/27. Session-level-only rule and per-item tracking preserved verbatim.

### 3. §7E-TSC §20 — Case C (retry of temporary technical failure)
**Old:** "**C — Retry of temporary technical failure:** retries specific failed items automatically after a backoff interval, within a bounded maximum attempt count. No new authorization required. Security conditions checked automatically before each retry."
**New:** "**C — Retry of temporary technical failure:** when a temporary retryable technical failure left the session in `"promotion_failed"` with retry attempts remaining, retry runs automatically after the declared backoff, within a bounded maximum attempt count. Security conditions are checked automatically before the retry; the session transitions `"promotion_failed"` → `"promoting"` and resumes the specific failed items. No new authorization required. No new fingerprint required. When automatic retries are exhausted or the failure is non-retryable, the session remains `"promotion_failed"`; Ness may request a new attempt. Requesting another attempt is not itself biometric authorization — for an already-authorized session, the requested attempt may transition `"promotion_failed"` → `"promoting"` after the required security checks, without a new fingerprint. New biometric promotion authorization is required only when the session was never successfully authorized (case B) or the original BAI token was revoked before promotion began (case B)."
**Reason:** Adds the explicit `promotion_failed` → `promoting` transition for automatic retry; adds the exhausted/non-retryable branch with the "Ness may request a new attempt" rule and the already-authorized requested-attempt transition; restates the two case-B conditions for new biometric authorization. Bounded-attempt-count and automatic-security-check rules preserved. Cases A and B unchanged.

### 4. §7E-TSC §23 — `promotion_failed` state definition (session-states block)
**Old:** "promotion_failed  — promotion incomplete; next action depends on the recorded failure class and §20 (temporary technical failures retry automatically without new fingerprint; non-retryable or exhausted retries may require Ness to request a new attempt; new biometric authorization required only when the session was never successfully authorized or the original BAI token was revoked before promotion began)"
**New:** "promotion_failed  — promotion incomplete; the recorded failure class determines the next action under §20 (a temporary retryable technical failure with attempts remaining retries automatically after the declared backoff and transitions promotion_failed → promoting after the required security checks, without a new fingerprint; when retries are exhausted or the failure is non-retryable, the session remains promotion_failed and Ness may request a new attempt — for an already-authorized session the requested attempt may transition back to promoting after the required security checks, which is not itself biometric authorization; new biometric authorization is required only when the session was never successfully authorized or the original BAI token was revoked before promotion began)"
**Reason:** Adds the explicit `promotion_failed` → `promoting` transition and the already-authorized requested-attempt transition so the §23 definition matches §17/§20/§27. The two case-B conditions are unchanged.

### 5. §7E-TSC §27 — Startup recovery for `promotion_failed`
**Old:** "`lifecycle_status = "promotion_failed"`: Ness has been notified. Inspect the recorded failure class and follow §20: temporary technical failures retry automatically without new fingerprint; if retries exhausted or failure is non-retryable, Ness may request a new attempt. New biometric promotion authorization is required only when the session was never successfully authorized or the original BAI token was revoked before promotion began."
**New:** "`lifecycle_status = "promotion_failed"`: Ness has been notified. Inspect the recorded failure class and follow §20: a temporary retryable technical failure with attempts remaining retries automatically after the declared backoff and, after the required security checks, transitions `"promotion_failed"` → `"promoting"` without a new fingerprint; if retries are exhausted or the failure is non-retryable, the session remains `"promotion_failed"` and Ness may request a new attempt — for an already-authorized session the requested attempt may transition back to `"promoting"` after the required security checks, which is not itself biometric authorization. New biometric promotion authorization is required only when the session was never successfully authorized or the original BAI token was revoked before promotion began."
**Reason:** Adds the explicit `promotion_failed` → `promoting` transition on retry recovery and the already-authorized requested-attempt transition so §27 matches §17/§20/§23. The two case-B conditions are unchanged.

---

## Unchanged (verified)

The blocked-item rule and the completion-gate paragraph in §17 Phase 3 are byte-identical to V9: while any item remains `"blocked"` the session remains `"promoting"`; blocked items do not cause `promotion_failed`; they prevent completion and archiving; they resume automatically when blockers clear; no new fingerprint required. Completion occurs only when every item is `"promoted"` or `"excluded"` with no blocked item remaining.
