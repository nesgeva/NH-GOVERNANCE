# NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md

## Status

- **Class:** Intent capture — INACTIVE CANDIDATE. Not a design. Not adopted.
  Decides nothing. Authorizes no implementation.
- **Owner of the concept:** Ness (Register A). This file records Ness's own
  concept in preserved form so it cannot be lost; all meaning, policy, and
  acceptance authority remain with Ness.
- **Origin:** Stated by Ness during the 2026-09-21 build session
  (Claude-assisted capture, same route as
  `NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`). ChatGPT's independent review of this
  capture is expected at its next audit pass.
- **Intended folder:** `05_INACTIVE_CANDIDATE/`
- **Authority:** Subordinate to NH_MASTER-20_CORRECTED_v10.md and the full
  authority order. Nothing here overrides, reopens, or modifies any
  accepted design, seal, store, or decision.
- **Build order (stated by Ness, binding on this intent):** built only
  **after the whole system is complete** — estimated a year out. Nothing in
  the current Bundle 1–6 build depends on it or changes for it.

## The concept, in Ness's own terms

1. **Files unreadable at rest — to everyone, including Ness.** The stores
   on disk appear as meaningless scrambled data. Opening them by hand — in
   an editor, by an intruder, from a stolen drive, from a leaked backup —
   shows only gibberish. (Mechanism: standard encryption at rest; never a
   homemade scrambling scheme.)

2. **"Seeing without seeing" — knowledge exists only in N.H's running
   memory.** The readable content exists nowhere on disk, ever. It exists
   only inside N.H's running process (RAM), only during an opened session.
   When the session closes, the readable form stops existing anywhere.
   Ness accesses his own memory *through* N.H, not by reading files raw.

3. **Fingerprint-opened sessions (TPM-held key).** The decryption key is
   sealed in the machine's hardware vault (TPM) and released only by
   Ness's live fingerprint (Windows Hello class mechanism). The fingerprint
   is the door, not the key: touch → hardware releases the key to the
   running session → N.H can know → key evaporates at session close. No
   fingerprint, no key; a copied disk or copied files decrypt nothing.

4. **Two keys, two meanings — daily use vs. maintenance.**
   - **Thumb (daily key):** opens a knowing session. Read-side life with
     N.H. No file editing is possible in this mode, by anyone.
   - **Outside maintenance key (surgical authority):** a separate,
     deliberately inconvenient credential kept physically outside the PC
     (long printed passphrase in a drawer, or an external hardware key).
     Only it opens **maintenance mode**, in which stores decrypt to
     workable form for a bounded repair (e.g., a small bug fix after
     completion), and are re-sealed afterward. The inconvenience is the
     feature: opening the hood is a ceremony, not a shortcut.

5. **Witnessed opens — no silent surgery.** Every session open/close and
   every maintenance open/close produces its own append-only §0B record,
   so N.H can always answer "when was my hood last open, and why." The
   same one-operation/one-log honesty the engine already runs on, applied
   to its own skin.

6. **Sovereign recovery path — unreadable to the world, never unreachable
   to Ness.** A sealed offline recovery credential (printed/stored outside
   the PC) guarantees that a dead fingerprint sensor, dead TPM, or dead
   machine never means permanent loss of the stores. "Impossible even for
   me" is explicitly rejected as a goal; the goal is: unreadable to
   intruders, always recoverable by Ness.

## Threat model honesty (recorded so the intent stays truthful)

- **Defeated by this concept:** stolen drive; hand-browsing at the PC;
  copied store files; leaked backups; any at-rest access without Ness's
  live fingerprint or the maintenance key.
- **NOT defeated by this concept:** malicious code running *inside* an
  open session, at the moment the knowledge exists in RAM. No
  architecture defeats that; the design's answer is deliberate, short,
  evidenced sessions plus ordinary machine hygiene.
- **Interim measure (outside N.H, available now, no code):** full-disk
  encryption (BitLocker + TPM) with Windows Hello fingerprint login, with
  the recovery key stored offline. This is operational hygiene, not part
  of this intent's future package.

## Open questions (future design work — none answered here)

- Interplay of encrypted stores with the existing seal/hash evidence
  chains (hashes of plaintext vs. ciphertext; how integrity proofs are
  re-verified inside sessions).
- Exact scope of encrypted stores (roots, readings, module state/logs,
  gold sets, configs — which, and whether tiered).
- Session boundaries: what opens one, what closes one, idle behavior,
  crash-during-session recovery (fail-closed expectations).
- Key custody details: TPM binding, maintenance-key medium, recovery
  credential format and storage discipline.
- Whether git history and the governance repo fall inside or outside the
  encrypted boundary.
- Relationship to multi-box / future storage-technology choices (the
  design must not leak storage technology into identity, per B11 §4.1
  spirit).

## Boundaries and must-nevers of this capture

- No implementation, no code, no store changes now.
- No modification of any authoritative, adopted, or historical file.
- Not Register-A work performed by Claude: the concept is Ness's; this
  file only preserves it verbatim in structured form.
- Formal packaging (a real candidate design) proceeds only through the
  normal route: Ness's decisions → ChatGPT's exact task instruction →
  versioned candidate → Ness's acceptance.

*End of v0_1.*
