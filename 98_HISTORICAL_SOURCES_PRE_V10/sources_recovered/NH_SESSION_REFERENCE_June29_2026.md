# N.H Project Session Reference — June 29 2026

*Compiled from: current session design work + audit of past project chats.*
*Authority: NH_MASTER-19_CORRECTED_v7_1.md (immutable baseline, SHA-256 = 0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf)*
*Status: reference document — does not modify the Master.*

---

## 1. Executive Summary

This session resumed N.H design work after the baseline lock-in (June 29 2026). The session established two new design decisions (TSC inspection prohibited; Computed View is internal-only, never surfaced to Ness unprompted), began mapping the complete end-to-end input cycle, and audited past chats for features that were fully designed and accepted but have not yet been patched into the Master.

The audit found one large cluster of accepted designs sitting in a companion file (`NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`, 1,724 lines) that were never integrated into the Master — the entire voice security and identity layer. It also found the async reading queue design (from the June 27 session) in the same pending state. Both are accepted and governing within their declared scope; they are not yet patched because patching was sequenced after baseline lock-in.

The session also produced three small but important design decisions about how N.H interacts with Ness: it reads the room and asks one gentle question when the moment calls for it; it drops a topic if Ness doesn't respond or says no; and it never narrates its internal picture of Ness back to him.

---

## 2. Decisions made in this session

These are new and must be recorded as settled before the next session.

**TSC inspection — PROHIBITED.**
No one, including Ness, may inspect a sealed Temporary Session Cache. No inspection token exists. No inspection mechanism exists. No authorized inspection path exists. A sealed cache waits for promotion authorization only. The current Master text in §7E-TSC refers to a `"tsc_inspection:<session_id>"` token and an "explicitly designed inspection mode" — both are now wrong and must be corrected in the next patch.

**Computed View — internal tool only.**
N.H uses the Computed View silently to inform its responses. It never surfaces the Computed View as output. It never shows Ness a summary or profile of what it knows about him. It never narrates its internal knowledge back. Ness may deliberately ask to look at it, but N.H never shows it unprompted.

**Action surfacing behavior — ask, don't tell.**
When N.H reads something that invites a suggestion, it asks one gentle question ("would you like to talk about this?") rather than volunteering suggestions automatically or staying silent forever. If Ness says no, ignores it, or doesn't respond, N.H drops the topic completely and does not bring it up again unless Ness does.

---

## 3. Fully designed features not yet in the Master

Everything in this section is accepted design, not a proposal. It is stored in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md` and the June-27 session design record. It is governing within its declared scope. It needs to be patched into the Master.

---

### 3A. BOP — Behavioral Observation Processing

What it is: BOP is the component that captures raw acoustic and behavioral measurements from voice input and stores them as sealed roots. It is the data-collection layer for identity — it does not make identity decisions.

What it captures: pitch range, amplitude, rhythm, room reverb level, microphone distance, signal compression. These are labeled as physical conditions (`acoustic_condition_notes`), not interpretations. BOP also records behavioral signals: session timing patterns, interaction rhythm, branch continuity evidence.

Key rules:
- BOP produces roots in the sealed root store via `append_root()` — the same store as all other roots.
- BOP roots from a TSC session remain held in §7E pre-ingest (with `"pending_fingerprint_authorization"` blocker) until the session is promoted. They never enter the sealed store prematurely.
- During a TSC session, BOP observation roots are interleaved in event-time order at promotion.
- One new vocabulary addition was formally adopted: `authorization_type = "enrollment_declared"` in BOP.

---

### 3B. SIA — Speaker Identity Assessment

What it is: SIA is strictly an identity assessor — it answers "is this Ness speaking?" It never makes authorization decisions. Authorization belongs entirely to SACL.

How it works: SIA takes BOP acoustic measurement roots and assesses identity across multiple dimensions simultaneously — voice acoustic match, behavioral pattern match, branch continuity, session continuity, timing rhythm. No single dimension is decisive; they combine into an `assessed_certainty` score.

Key rules:
- SIA never decides what Ness is allowed to do. That is SACL's job.
- Acoustic spoofing evidence and conversational identity evidence are kept separate inside SIA's anti-spoofing assessment.
- SIA does not issue routine voice challenges. It monitors and updates naturally.
- Identity uncertain vs spoofing suspected are distinct events with distinct responses:
  - Identity uncertain: may be natural variation. Access stays at current level. SIA monitors.
  - Spoofing suspected (medium or high): access drops to guest immediately. Private Ness alert queued.

Voice profiles are built as a range, not a fixed point — the system learns Ness's voice across different conditions (tired, stressed, different rooms, different devices). A lower match score in one dimension doesn't fail identity if other dimensions are strong.

**6–10 month calibration phase:** during the first months of active use, certainty thresholds are set conservatively. The system requires stronger combined evidence to reach `recognized_ness` level. Conservativeness reduces gradually as calibrated evidence accumulates.

---

### 3C. SACL — Speaker Access-Control Layer

What it is: SACL owns all authorization decisions. It takes SIA's identity assessment and maps it to an access level. SIA tells SACL who is speaking; SACL decides what that person is allowed to do.

Four access levels (from SIA's certainty output):
- `recognized_ness` — full private access
- `partial_match` — reduced access; sensitive operations blocked
- `guest` — visitor-level access only
- `unknown` — no access to private content

Key rules:
- Imitation-risk policy is Option A (Ness's choice): blocks top-security access only, not `recognized_ness` access.
- SACL owns the `§22 Wellbeing` / identity / security separation — the Wellbeing system never decides speaker identity or access levels.

---

### 3D. BAI — Biometric Authorization Interface

What it is: BAI is the token-issuing layer. When an authorized action requires proof that Ness is present and consenting, BAI produces a purpose-bound one-time token. Nothing can reuse a token or use it for a different purpose than the one it was issued for.

Token types:
- `"tsc_promotion:<session_id>"` — authorizes promotion of one specific sealed TSC
- Other purpose-bound tokens for other high-authorization actions

Key rules:
- Purpose-bound: a promotion token for session A cannot authorize promotion of session B.
- One-time: consumed on use; cannot be reused.
- Key separation: BAI uses different keys for different token purposes; manifest-signing and rollback-sealing keys in BGMM are separate.

---

### 3E. Owner-phone pairing

What it is: the mechanism by which Ness's phone is paired to N.H as a trusted device.

Four-state QR lifecycle:
1. QR generated on desktop
2. QR scanned by phone
3. Pairing confirmation on desktop
4. Pairing complete

Future-phone replacement: a separate authorized process exists for replacing the paired phone without losing access. The exact flow is recorded in `NH_ACCEPTED_SECURITY_IDENTITY_DESIGNS_AFTER_BGMM.md`.

---

### 3F. Recovery codes

What it is: an offline backup access mechanism for situations where biometric and phone-based authentication are unavailable.

Key rules:
- Recovery codes are generated at pairing time.
- Recovery codes are stored offline by Ness only.
- A used recovery code is invalidated immediately.
- The lifecycle (generation, use, invalidation, regeneration) is recorded in the accepted design file.

---

### 3G. Atomic emergency recovery

What it is: a last-resort full-system recovery path. If the primary authentication chain fails completely, atomic emergency recovery allows Ness to regain access without partial states.

Key rules:
- Atomic: no partial revocations. Either the full handover completes or nothing changes.
- A provisional intermediate state exists during the handover; it is temporary and explicitly labeled.
- Rollback packages contain full file content, not just hashes.
- Manifest-signing and rollback-sealing keys are separate (Ness corrected this during design).

---

### 3H. Ness voice-profile enrollment bootstrap

What it is: the process that runs the first time N.H collects enough voice data to build Ness's initial voice profile. It establishes the baseline from which SIA's variation ranges are calculated.

Key rules:
- Enrollment is declared, not assumed. `authorization_type = "enrollment_declared"` marks the session.
- The second adopted vocabulary addition: `link_type = "enrollment_material_provisional"` in §7L — a provisional link in Ness's Person-Box pointing to the enrollment material, marked provisional until the profile is confirmed.
- Enrollment material feeds into SIA's voice profile reading set. It does not bypass the reading path.

---

### 3I. BGMM — Biometric-Gated Maintenance Mode

What it is: a protected operating mode for system maintenance operations — rebuilding indexes, running diagnostics, applying patches — that requires biometric confirmation before entering. Prevents maintenance from being triggered by unauthorized input.

Key rules:
- Entering BGMM requires biometric verification (not just a PIN or password).
- Manifest-signing key and rollback-sealing key are separate inside BGMM.
- Operations inside BGMM are logged as a distinct event type.

---

## 4. In-progress / partially reflected features

---

### 4A. Async reading queue and reading-pass instruction log

What it is: the mechanism that manages reading jobs asynchronously — so that the reading engine can process roots in the background without blocking the chat.

Files involved:
- `.nh_reading_queue.jsonl` — the persistent queue of reading jobs
- `.nh_reading_pass_log.jsonl` — the instruction record for each pass

Key design decisions (all from the June-27 session, pending Master patch):
- Both files are append-only event logs. No mutable status fields.
- Mode assignment uses `thread_membership_v1` rules.
- Seven-step worker pass sequence.
- Three post-reading stage checkpoints, each append-only and linked by `job_id`:
  - `reading_written` — includes the `reading_id`
  - `clash_detection_completed` — records whether a clash was found and any clash record ID, or explicitly `no_clash`
  - `computed_view_completed` — records snapshot ID or `no_update`
- Crash recovery resumes from the latest completed checkpoint, not from the beginning.
- Queue-claim mechanism uses a lock file (`O_CREAT|O_EXCL`) with `job_claimed` and `claim_expired` events to prevent duplicate processing.

Status: fully designed, accepted in the June-27 session. Not yet patched into the Master.

---

### 4B. Knowledge Catcher (outside research — §8)

Two decisions settled (recorded in Master §8 and §11):
- The pipeline has two responsibilities: gathering new outside information, and checking stored information against outside sources.
- When preserving a source, N.H keeps both the relevant excerpt and the full source page whenever possible.

Two decisions still open:
- **Fallback when the full source page cannot be saved:** Option A (retain excerpt + provenance, mark as `SOURCE PRESERVATION INCOMPLETE`, require corroboration for important claims) is the current recorded approach in the Master — but the original session notes describe this as a proposed option, not a closed decision. Needs Ness to confirm it is closed.
- **How source pages are preserved:** the screenshot-as-inert-image proposal (save the full page as a visual-only inert image, not live content) was discussed and found consistent with N.H's spirit. It is a new proposal, not yet decided.
- **Academic source:** Semantic Scholar API vs OpenAlex vs both. Still open. Google Scholar is off the table.
- **Live-retrieval security boundary:** full-page retrieval is a new attack surface. Must occur inside a separately isolated capture environment. Implementation not yet designed.

---

### 4C. Chat front door (§14)

Status: design-in-progress, not confirmed, not built.

Two open questions that block finalizing this section:
1. **Creation filter as mechanism vs mode:** when Ness types something in the chat, is the filter that separates "what was created here" from "what was said here" a separate component, or just a mode of the main catalog front door?
2. **Always-capture vs deliberate-capture:** does every message Ness types automatically enter the reading pipeline, or does Ness have to deliberately mark something for capture?

---

### 4D. Features found in earlier chats, not in current Master

From the June-19 standalone master (`NH_MASTER_FILE_COMPLETE.md`), a session-11 audit found these things either reduced to one-liners or fully absent from v7_1:

- Full access/authentication model: dry mode vs personal mode, graduated step-up authentication, factor hierarchy
- Voice in/out pipeline detail beyond basic front-door description
- Five phone-side modes: emergency record, breathing reminder, stealth toggle, night lockout, kill switch
- Personality modeling (how N.H's interaction style adapts over time)

These are recorded as a gap in the review queue (`NH_BASE_AND_REVIEW_QUEUE_v1.md`, questions Q1–Q26). They are not yet resolved.

---

## 5. Next steps — clear path forward

In order:

**Step 1 — Authorize and apply the June-27 patch.**
This is the single biggest unblocking action. The patch covers: end-to-end input cycle design, async reading queue, all security/identity components (BOP, SIA, SACL, BAI, owner-phone pairing, recovery codes, atomic emergency recovery, voice enrollment bootstrap, BGMM), and TSC. It is fully designed and accepted. It needs Ness's explicit "APPROVED" before it can be applied to a new versioned Master (v7_2).

The TSC inspection correction (inspection prohibited) must be folded into this patch before it is applied.

**Step 2 — Continue the end-to-end cycle design.**
Three gaps were identified in this session:
- What triggers the Computed View to update after a new reading lands (now answered: internal only, Ness-on-demand)
- What makes action surfacing fire (relevance mode declarations for §7N not yet written)
- How Ness's response connects back to the original action (§7O result states exist; detection and confirmation flow is thin)

**Step 3 — Resolve the two chat front door questions.**
Creation filter as mechanism vs mode. Always-capture vs deliberate-capture. One question at a time.

**Step 4 — Close the Knowledge Catcher open decisions.**
Confirm whether Option A (excerpt + SOURCE PRESERVATION INCOMPLETE) is closed or still open. Decide the screenshot-as-inert-image proposal. Decide academic source (Semantic Scholar vs OpenAlex vs both).

**Step 5 — Work through the review queue gaps (Q1–Q26).**
The five phone-side modes, access/auth model, voice pipeline detail, and personality modeling need to be recovered, verified against earlier sources, and patched in if they belong in the current design.

---

*End of session reference document.*
*Next action: Ness authorizes the June-27 patch → copy v7_1 to v7_2 → apply patch → hash-verify.*
