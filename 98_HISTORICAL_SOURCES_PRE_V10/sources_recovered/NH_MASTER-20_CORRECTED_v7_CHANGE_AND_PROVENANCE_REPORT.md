# NH_MASTER-20_CORRECTED_v7 — CHANGE AND PROVENANCE REPORT

**Base file:** `NH_MASTER-20_CORRECTED_v6.md` (SHA-256: `4c67ba2194879feff9343c9ed02458886b060a4d560cbd6beb367927eecc2bad`)

---

## Changes (2 passages)

### Document Identity
**Old:** `NH_MASTER-20_CORRECTED_v6.md`
**New:** `NH_MASTER-20_CORRECTED_v7.md`

### §25 TSC Lifecycle Summary
**Old:** "TSC lifecycle: `active` → `sealed` (on session close) → `authorized` (after fingerprint) → `promoting` → `promoted` or `promotion_failed`."
**New:** "TSC session lifecycle: `active` normally becomes `sealed` when the session closes. A crashed live session becomes `interrupted` and remains separately sealed. `sealed` or `interrupted` waits indefinitely for authorization — no auto-expiration, no auto-deletion, no auto-promotion. After authorization: `authorized` → `promoting`. Promotion reaches `promoted` or `promotion_failed`. Successful retained-archive creation moves `promoted` → `archived`. `archived` may become `permanently_sealed` only after separate authorization. Permanent sealing never happens automatically. No `deleted` lifecycle state exists. (Full lifecycle detail: §7E-TSC §§12, 17, 23.)"
**Reason:** The old summary omitted `interrupted`, `archived`, and `permanently_sealed`, contradicting the detailed §7E-TSC lifecycle in §§4, 12, 17, 23, and 27.
