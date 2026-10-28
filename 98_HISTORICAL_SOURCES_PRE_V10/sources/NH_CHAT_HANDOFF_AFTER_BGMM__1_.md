# NH_CHAT_HANDOFF_AFTER_BGMM.md

## Purpose

This file is a handoff record for the next N.H design chat session. It states
the current authority order, the state of all designs completed in the
security/identity/BGMM branch, and the starting point for the next session.

---

## Authoritative Files

The following files are the current authoritative N.H sources. They must always
be used together. No single file is sufficient without the others.

| File | Role | SHA-256 |
|---|---|---|
| `NH_MASTER-19_CORRECTED_v6.md` | Architectural authority — the complete settled N.H design | `8165f4bed94d2d57140d49e93d3c85b8e2b259053e0b30ac4c675fa7463a1bf9` |
| `NH_DECISION_DEFAULTS-S19_v1__1_.md` | Behavioral defaults companion — must be read alongside the Master | `ecea9224163681f9fc1d29327b0453c5e7ead42fd178786ab9dc6a6d4e1baaa6` |
| `NH_WORKING_ROLES.md` | Working relationship rules governing Claude, Ness, and ChatGPT | `a0281060abd7e7da791bb56a97316ab9ec41ab88fdd7884fac4c6434fa487619` |

**The next chat must inspect all uploaded files and confirm the authority order
before beginning any new design work.**

---

## Working Relationship Rules

`NH_WORKING_ROLES.md` governs the working relationship and must be followed:

- Claude is the architecture and audit brain. Cursor writes code. Ness runs all
  commands and verifies on disk.
- ChatGPT's role is limited to catching contradictions, gaps, and technical
  errors. ChatGPT must never fill open questions or propose what the system
  should do. All concept and meaning decisions belong entirely to Ness.
- One step at a time. No step proceeds without explicit Ness approval.
- Patch-only, no-loss discipline. No file is overwritten. No changes applied
  without explicit approval.

---

## Components Accepted and Complete

The following components were designed, corrected through multiple iterations,
and explicitly accepted by Ness during the security/identity/BGMM branch.
All are marked **ACCEPTED DESIGN — NOT YET BUILT** and are preserved in full
in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`.

1. **BOP — Behavioral Observation Processing** (detailed design)
2. **Other-Speaker / Guest / Known-Person Architecture** (high-level, final)
3. **SIA — Speaker Identity Assessment** (detailed design)
4. **SACL — Speaker Access-Control Layer** (detailed design)
5. **Wellbeing / Identity / Security Separation Rules**
6. **BAI — Biometric Authorization Interface** (detailed design)
7. **Initial Owner-Phone Pairing** (four states, QR lifecycle)
8. **Recovery-Code Lifecycle** (creation, save verification, local test,
   activation, rotation)
9. **Future-Phone Replacement Flow**
10. **Atomic Emergency Recovery Flow**
11. **Initial Ness Voice-Profile Enrollment Bootstrap**
12. **Formally Adopted Vocabulary Additions:**
    - BOP `session_authorization.authorization_type = "enrollment_declared"`
    - §7L `link_type = "enrollment_material_provisional"`
13. **BGMM — Biometric-Gated Maintenance Mode** (detailed design, all
    corrections applied)

**BGMM was the most recently completed component.**

---

## No Master Patch Has Been Authorized From This Branch

None of the designs listed above have been patched into the Master
(`NH_MASTER-19_CORRECTED_v6.md`), the Decision Defaults, or `.cursorrules`.
The accepted designs exist only in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`
and in the chat history.

Before any design from this branch enters the Master, the full patch-only,
no-loss, no-silent-deletion protocol must be followed. No patch is authorized
until Ness explicitly approves it.

---

## Next Unfinished Component

**Temporary Session Cache (TSC) — detailed design**

This is the next component requiring detailed design. It was established at the
high-level architecture stage (section 7 of the other-speaker architecture) but
has not received detailed component design.

### Settled TSC Rules Carried Forward

These rules are already settled and must be preserved exactly in the detailed
design:

- Third-party session material enters a TSC rather than the long-term shared
  store during the session.
- The TSC uses §7E's pre-ingest holding area with the new blocker:
  `"pending_fingerprint_authorization"`.
- Held material is invisible to the Meaning Engine while held.
- The TSC preserves the complete session context including Ness's words when
  they give meaning to another person's statements.
- Every speaker's exact contribution is preserved with speaker attribution,
  certainty, timing, turn order, branches, surrounding context, N.H outputs,
  BOP behavioral observation roots, SIA assessment events, and session metadata.
- TSC lifecycle: `active` → `sealed` (on session close) → `authorized` (after
  fingerprint for the relevant completed session) → `promoting` → `promoted` or
  `promotion_failed`.
- Cache sealing: on session close, TSC is sealed immediately; a `cache_sealed`
  security audit event is written immediately.
- The fingerprint authorizes the complete pending cache from the relevant
  completed session — not all sealed caches from all sessions simultaneously.
  Ness does not select individual people, memories, or items within the cache.
- After fingerprint authorization: all items with no remaining blockers proceed
  through §7E → sealed store → §7G → readings → §7J → §7M → §7L proposals
  without requiring additional manual Ness input.
- TSC promotion requires two independent conditions: purpose-bound BAI
  `one_time_authorization_token` with purpose `"tsc_promotion:<session_id>"`
  AND a currently valid recognized-Ness session (non-stale, from SACL) at
  consume time.
- If promotion fails partway through: items not yet promoted remain in
  `authorized` state; `append_root()` idempotency prevents duplicate writes;
  promotion resumes on restart for unpromoted items.
- The reading queue, Meaning Engine, clash detection, Computed View trigger,
  and Person-Box linking proposals all run through the mechanism's normal rules
  after promotion.
- Security audit events for TSC operations are written immediately:
  `cache_sealed`, `cache_authorization_received`, `cache_promotion_started`,
  `cache_promotion_completed`, `cache_promotion_failed`.

### What the TSC Detailed Design Must Add

The detailed design must cover at minimum:

- Exact TSC record schema and storage format.
- How the TSC relates to and extends the §7E pre-ingest holding area.
- How items within the TSC are attributed to their speakers with certainty.
- How branches and conversational context are preserved.
- How Ness's material within the TSC retains its own attribution and processing
  eligibility without being excluded from context.
- How the TSC handles a session that includes multiple different known persons.
- Exact promotion sequencing — which items promote first, how blockers are
  resolved, how speaker-unresolved items are handled.
- How the TSC survives app crashes, restarts, and unexpected session termination.
- Idempotency of promotion.
- How the TSC integrates with BAI (two-condition promotion check), SACL (session
  validity check at consume time), BOP (observation roots carried in the TSC),
  §7E (pre-ingest holding), §7G (reading after promotion), §7L (Person-Box
  proposals), and the security audit log.
- Failure, rollback, and fail-closed behavior.
- Privacy handling for third-party content in the TSC.

---

## Instructions for the Next Session

1. Inspect all uploaded files and confirm the SHA-256 hashes match those in
   this handoff document.
2. Confirm the authority order: Master → Decision Defaults → Working Roles →
   this handoff → the accepted designs file.
3. Read the full accepted TSC rules carried forward above before proposing any
   new design.
4. Begin detailed design of the Temporary Session Cache only.
5. Do not patch the Master or any existing file until Ness explicitly authorizes it.
6. Do not make concept decisions. Bring all genuine concept questions to Ness
   one at a time.

---

*End of NH_CHAT_HANDOFF_AFTER_BGMM.md*
