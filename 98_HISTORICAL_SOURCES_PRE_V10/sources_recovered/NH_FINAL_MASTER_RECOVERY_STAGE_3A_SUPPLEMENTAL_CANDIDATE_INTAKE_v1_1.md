# N.H — FINAL-MASTER RECOVERY — STAGE 3A: SUPPLEMENTAL CANDIDATE INTAKE v1.1

**Material correction successor to v1.** Only authority-scope, file-vs-feature status, security-conflict,
and recovery-workflow classifications were corrected. Candidate deltas, hashes, source ranges, feature
content, and conflict evidence were otherwise preserved. The original v1 remains unchanged.

**Pre-Stage-3B intake of three newly supplied candidate files.** This document hashes, verifies, and
maps the three candidates against current authority, the two accepted companions, and the Stage 3A
baseline (v1 + v1.2). It is an **intake**, not an adoption. Nothing here adopts, integrates, patches, or
reconciles any candidate; no contradiction is resolved; no N.H design is changed; no architecture is
decided for Ness; the historical Stage 3B comparison is **not** begun.

**Authority is unchanged by this intake.** Current architectural, behavioral, and operational authority
remains **Master v7_1 · Defaults v2.2 · Cursor Rules v3.2**. The governance companion v1 remains
controlling only within its stated governance, accepted-design, handoff, and provenance scope; it is
**not architectural authority**. SUP-001–SUP-003 are **candidate files only** (see §3).

**Conventions.** Candidate line numbers are the candidate's own body line numbers (`v8 L#`, `v2.3 L#`,
`v3.3 L#`). Current-authority and companion citations use the conventions of the Stage 3A baseline
(`src001 L#` / `src002 L#` are the standalone accepted-companion body line numbers). This intake is
document-based; it performed **no fresh disk inspection** of Ness's machine.

---

## DIRECT-SOURCE VERIFICATION REPORT

All three candidate files were located in `/mnt/project`, their complete direct bodies read, and their
SHA-256 hashes + byte/line counts compared to the externally-supplied values. **All three match exactly.**

| SUP id | Canonical file | Bytes (found / expected) | Lines (found / expected) | SHA-256 (found) | Match |
|---|---|---|---|---|---|
| SUP-001 | `NH_MASTER-19_CORRECTED_v8.md` | 317740 / 317740 | 2039 / 2039 | `6c5511f99f5cb32a601fe727405ebe5848bc79e7691cfe9708fdf7e1d9affbe3` | ✓ exact |
| SUP-002 | `NH_DECISION_DEFAULTS-S19_v2_3.md` | 40009 / 40009 | 322 / 322 | `6f123a6c55ef1b0ef1c842de68f645b6981c040f5326924cabe9c2381441fd50` | ✓ exact |
| SUP-003 | `cursorrules_v3_3` | 37050 / 37050 | 750 / 750 | `d971e7ad7320216e6fc77a0c9178fd61b19012a8d8028904f4f3e8e8395826b3` | ✓ exact |

**What was read directly:** the complete bodies of all three candidates; and, for comparison, the complete
bodies of `NH_MASTER-19_CORRECTED_v7_1.md`, `NH_DECISION_DEFAULTS-S19_v2_2.md`, Cursor Rules v3.2
(`cursorrules__1_`), the standalone SRC-001 and SRC-002 companion bodies, and the Stage 3A baseline v1 +
v1.2 (all read in prior Stage 3A turns). The original 92-source preservation set was **not** altered.

---

## 1. SUPPLEMENTAL INTAKE MANIFEST

| Field | SUP-001 | SUP-002 | SUP-003 |
|---|---|---|---|
| Uploaded name | `NH_MASTER-19_CORRECTED_v8(1).md` | `NH_DECISION_DEFAULTS-S19_v2_3(1).md` | `cursorrules_v3_3(2)` |
| Canonical identity | `NH_MASTER-19_CORRECTED_v8.md` | `NH_DECISION_DEFAULTS-S19_v2_3.md` | `cursorrules_v3_3` |
| Bytes | 317,740 | 40,009 | 37,050 |
| Lines | 2,039 | 322 | 750 |
| SHA-256 | `6c5511f9…fbe3` | `6f123a6c…1fd50` | `d971e7ad…826b3` |
| Provenance | Supplied by Ness this session; present in `/mnt/project`; **outside** the original SRC-001–SRC-092 preservation set | same | same |
| Self-declared relation | "supersedes `NH_MASTER-19_CORRECTED_v6.md`" (inherited v7 line); preamble dates a June 28 2026 design session | "Synced to `NH_MASTER-19_CORRECTED_v8.md`"; "Supersedes `…v2_2.md`" | "supersedes all previous `.cursorrules` versions in this project" |
| Authority status (this intake) | **CANDIDATE — NOT CURRENT AUTHORITY** | **CANDIDATE — NOT CURRENT AUTHORITY** (self-labeled "CANDIDATE — pending adoption by Ness") | **CANDIDATE — NOT CURRENT AUTHORITY** |
| Current authority it would replace if adopted | Master v7_1 | Defaults v2.2 | Cursor Rules v3.2 |

Stable identifiers assigned: **SUP-001 = Master v8 · SUP-002 = Decision Defaults v2.3 · SUP-003 = Cursor
Rules v3.3.** These sit outside the SRC-001–092 set and do not renumber or modify it.

---

## 3. ADOPTION-EVIDENCE AUDIT

A filename, version number, "supersedes" statement, or internal claim of authority is **never** treated as
evidence that Ness adopted a file. File-level adoption requires an explicit Ness adoption statement applying
to that exact version. The findings below establish only what the candidate bodies themselves prove.
Feature-level acceptance or adoption in historical source conversations remains for Stage 3B to determine.

**SUP-001 — Master v8: NO v8-specific adoption statement found.**
- v8's preamble adoption line reads, verbatim: "This file (NH_MASTER-19_CORRECTED_**v7**.md) is the adopted
  authoritative N.H Master, explicitly adopted by Ness (June 28 2026). It supersedes
  NH_MASTER-19_CORRECTED_v6.md." (`v8 L8`). This is the **inherited v7 adoption statement** — it names v7
  as the adopted file and v6 as superseded; it does **not** state that v8 was adopted, and the file name it
  cites inside its own adoption sentence is v7, not v8.
- The only v8-specific note is the June 28 2026 design-session change-log star line (`v8 L10`), which
  describes the three added laws and asserts "No existing settled design was changed or removed. This file
  is NH_MASTER-19_CORRECTED_v8.md." This is an internal change description, **not** an adoption statement.
- **Conclusion:** no direct **file-level** adoption evidence appears inside v8 itself. Master authority
  remains **v7_1** unless Stage 3B finds separate direct evidence that Ness formally adopted this exact file.

**SUP-002 — Defaults v2.3: explicitly self-labeled NOT adopted.**
- Header reads, verbatim: "**CANDIDATE — pending adoption by Ness after Master v8 review.**" (`v2.3 L7`)
  and "Hash of authoritative Master: **[to be computed after Master adoption]**" (`v2.3 L4`).
- **Conclusion:** v2.3 self-declares as a candidate awaiting adoption. Defaults authority remains **v2.2**.

**SUP-003 — Cursor Rules v3.3: only a self-declared supersession line; NO adoption statement.**
- v3.3 carries "This file supersedes all previous `.cursorrules` versions in this project." (`v3.3 L15`)
  and a v3.3 change note (`v3.3 L12–14`). Per the rule above, a "supersedes" line is **not** adoption
  evidence. No explicit Ness-adoption statement for v3.3 appears anywhere outside that supersession line.
- **Conclusion:** no direct **file-level** adoption evidence appears inside v3.3 itself. Cursor authority
  remains **v3.2** unless Stage 3B finds separate direct evidence that Ness formally adopted this exact file.

**Cross-candidate consistency note (recorded, not resolved):** Defaults v2.3 is synced to **Master v8**,
and Cursor v3.3 cites **§0A/§0B/§7Q** (the v8 sections) — yet **Master v8's own §6A still references Cursor
Rules v3.2** (`v8 L429`, `v8 L403`), not v3.3. So the three candidates are not fully cross-consistent about
which coding-rules version the candidate Master points to. Marked for Stage 3B; not resolved here.

---

## 2. EXACT CANDIDATE-DELTA MAP

Classification vocabulary: **additive · clarification · correction · explicit replacement · conflict with
current authority · conflict with accepted companion · unresolved · purely propagated**. A single change
may carry more than one tag. (Section appears after §1 and §3 by document layout; it is deliverable 2.)

### 2A. Master v8 vs v7_1

v7_1 = 1937 lines; v8 = 2039 lines. Diff: 29 lines only in v7_1, 131 lines only in v8. **One** new heading
(§0B). Changes cluster in five places.

| # | Change (v8 vs v7_1) | Direct range | Classification |
|---|---|---|---|
| M1 | Preamble change-log star line added describing the three June-28 laws; asserts "No existing settled design was changed or removed." | `v8 L10` | additive · **internal candidate contradiction / unsupported no-change claim** (see K1; M2/M4/M5 materially replace settled current-authority rules) |
| M2 | §0A "pure-tape note" replaced with a **two-level sensitive-content protection model** (Level 1 sealed-never-exposed / Level 2 available-to-Ness-after-ID), "true destruction prohibited," safe references + opaque protected-record IDs | `v8 L201–225` | explicit replacement · additive · **conflict with accepted companion** (see §4) |
| M3 | **§0B added** — the Full-Transparency and Living-Record Law (universal recording; active living memory; triggered recursive self-examination; mandatory use/non-use records; append-only growth; mandatory connections; two protection levels) | `v8 L226–287` | additive |
| M4 | §7Q rewritten: **five operations → six** (adds Sealed isolation); deletion redefined from blocking/verification-based **removal** to **non-destructive visibility removal**; cryptographic erasure prohibited; the earlier unresolved-deletion "make inaccessible to all internal functions" rule marked **REJECTED**; influence-removal made a **separate** instruction; five outcome states replaced (`verified_complete…` → `protected_complete…`); "FOUR SENSITIVITY LEVELS" → "FOUR SENSITIVITY TIERS" mapped to the two protection Levels; Layer A rewritten for Level-1 sealed processing | `v8 L1120–1185` | explicit replacement · **conflict with current authority** · **conflict with accepted companion** |
| M5 | Status table: "Pure-tape redaction/destruction path" row changed PARTIALLY CONCEPTUALLY DESIGNED → **SUPERSEDED (June 28 2026)**; two new DESIGNED rows added (Full-transparency law; Two-level protection); §7Q row updated five→six operations | `v8 L57–80` | explicit replacement · correction · **conflict with current authority** (contradicts M1's "nothing settled changed") |
| M6 | Closing principle changed: "**DELETION IS BLOCKING AND VERIFICATION-BASED** … five outcomes; tombstone only" → "**DELETION IS NON-DESTRUCTIVE VISIBILITY REMOVAL** … six operations; five outcome states; history record not tombstone" | `v8 L1805` (v7_1 L1703) | explicit replacement · **conflict with current authority** |
| M7 | §6A still references **Cursor Rules v3.2** (not v3.3); §25 recovery log unchanged from v7_1; no v8-specific adoption statement added | `v8 L403, L429, L2002–2039` | unchanged-from-v7_1 (recorded for the cross-candidate note) |

### 2B. Defaults v2.3 vs v2.2

v2.2 = 314 lines; v2.3 = 322 lines. Diff: 8 lines only in v2.2, 16 only in v2.3. Every substantive change
is a propagation of v8's three laws into the behavioral guide.

| # | Change (v2.3 vs v2.2) | Direct range | Classification |
|---|---|---|---|
| D1 | Header: "AUTHORITATIVE — adopted by Ness" → "**CANDIDATE — pending adoption by Ness after Master v8 review**"; synced to v8; Master hash "[to be computed after Master adoption]"; supersedes v2.2 | `v2.3 L3–8` | explicit replacement (of the adoption header) · self-declared non-adoption |
| D2 | "CHANGES FROM v2_2" note added listing the three propagated changes | `v2.3 L13–18` | additive (changelog) |
| D3 | §0 BEHAVIORAL OVERRIDES: new item — full-transparency and living-record law enforcement (every component must record its own internal operations; silent operations prohibited) | `v2.3 L33` | additive · **purely propagated** from v8 §0B |
| D4 | §3 SETTLED DESIGN: §7Q entry rewritten — five→six operations; four sensitivity tiers; two protection levels; deletion non-destructive; five new outcome states; history record replaces tombstone; stopping-influence separate | `v2.3 L137` | explicit replacement · **purely propagated** from v8 §7Q · **conflict with current authority** (mirrors M4) |
| D5 | §6 FIRST-CLASS PRINCIPLES: new principle "EVERYTHING IS RECORDED, CONNECTED, AND ACTIVELY USABLE" added | `v2.3 L309` | additive · **purely propagated** from v8 §0B |
| D6 | §6 FIRST-CLASS PRINCIPLES: "DELETION IS BLOCKING AND VERIFICATION-BASED" → "DELETION IS NON-DESTRUCTIVE VISIBILITY REMOVAL" | `v2.3 L313` | explicit replacement · **purely propagated** from v8 §7Q · **conflict with current authority** (mirrors M6) |
| D7 | §6 pure-tape principle updated for the two protection levels ("append-only means nothing is erased; Level 1 sealed; Level 2 available after ID") | `v2.3 L317` | clarification · **purely propagated** from v8 §0A |

### 2C. Cursor Rules v3.3 vs v3.2

v3.2 = 717 lines; v3.3 = 750 lines. Diff: 1 line only in v3.2 (the version header), 34 only in v3.3. v3.3's
own note: "full-transparency and living-record law enforcement rule added to §1A; no-destruction
prohibition added to §1A; **No other rules changed or removed.**"

| # | Change (v3.3 vs v3.2) | Direct range | Classification |
|---|---|---|---|
| C1 | Header v3.2 → v3.3 + change note; self-declared supersession line retained | `v3.3 L1, L12–15` | additive (versioning) |
| C2 | §1A PERMANENT PROHIBITIONS: new rule — never write code that performs any internal N.H operation without a mandatory append-only linked record (enumerates the operations + required record fields; "a function … without producing such a record is a prohibited function") | `v3.3 L79–103` | additive · **purely propagated** from v8 §0B (enforcement) |
| C3 | §1A PERMANENT PROHIBITIONS: new rule — never write code that permanently destroys or cryptographically erases the only copy of any content; deletion is always non-destructive visibility removal | `v3.3 L105–108` | additive · **purely propagated** from v8 §0A/§0B/§7Q (enforcement) · **conflict with accepted companion** (see §4: SRC-001 requires destruction of single-use security material) |

---

## 4. FOCUSED CONFLICT AUDIT

Every item preserves both sides and is marked **CONFLICTING** or **UNCLEAR**. None is resolved. None
changes any design. These are preserved for Stage 3B's historical evidence comparison. They are **not an
active Ness decision queue**: current settled authority remains in force unless Stage 3B finds direct
feature-level acceptance/adoption evidence or Ness explicitly reopens a choice.

**K1 — v8's "no settled design changed" claim vs its own supersession of the deletion path. → CONFLICTING.**
v8 `L10` asserts "No existing settled design was changed or removed." v8 itself `L57`/`L1805`/`L1120–1162`
changes the settled deletion design: the status-table "Pure-tape redaction/destruction path" row becomes
**SUPERSEDED**, the closing principle flips from "DELETION IS BLOCKING AND VERIFICATION-BASED" to
"NON-DESTRUCTIVE VISIBILITY REMOVAL," and §7Q's deletion operation + outcome states are replaced. The
assertion and the edits cannot both be true as written.

**K2 — v7_1 deletion (blocking, verification-based removal) vs v8 deletion (non-destructive visibility
removal). → CONFLICTING.** v7_1 §7Q: "DELETION IS BLOCKING AND VERIFICATION-BASED — N.H may confirm
complete deletion only when every known location has been removed or verified clean; five distinct
outcomes (`verified_complete`…); content-free tombstone; while a deletion case remains unresolved,
affected material must be immediately prevented from retrieval, display, analysis, simulation, or use."
v8 §7Q (`L1138–1162`): deletion is "always and only a non-destructive state change affecting visibility";
"Cryptographic erasure that destroys the only copy of any content is prohibited"; content "remains
preserved, internally connected, and internally usable"; new outcome states (`protected_complete`…);
history record "not a tombstone." v8 additionally marks the v7_1 unresolved-deletion blocking rule as a
**REJECTED DESIGN** (`v8 L1140`). The two definitions of "deletion" are opposite.

**K3 — v8 universal no-destruction rule vs accepted security rules requiring destruction (SRC-001). →
CONFLICTING.** v8 (`L223–225`, `L284–286`, `L1138`): "No information, record, credential, secret, log,
derivative … may ever be permanently erased … Cryptographic erasure that destroys the only copy … is
prohibited," and for Level-1 material "If a deletion request is received … the content remains in Level 1
sealed protected storage." SRC-001 **requires destruction** of specific single-use security material:
- initial QR + temporary pairing secret "permanently destroyed" at pairing State 2 (`src001 L1093–1097`,
  L1112–1119);
- phone-side recovery-code local copy "immediately erases its local copy" after activation
  (`src001 L1161`); a failed new code is "destroyed" while the old remains valid (`src001 L1150`);
- failed provisional emergency-recovery material: "All provisional new material destroyed"
  (`src001 L1239`);
- BGMM rollback packages "securely deleted" after completion/rollback (`src001 L1552`, L1569);
- BAI one-time tokens "consumed → permanently unusable" (`src001 L964–965`) — invalidation, marked
  **UNCLEAR** below.
The accepted security designs treat destruction/erasure of these single-use items as a safety requirement;
v8's universal no-destruction rule forbids exactly that.

**K4 — v8 no-destruction rule vs BGMM / device-trust / recovery / emergency-recovery. → CONFLICTING /
UNCLEAR BY MECHANISM.** v8 §0A also claims "Existing security and identity protections are entirely
unchanged" (`v8 L223`-area). SRC-001 uses two different mechanisms that must not be merged: **actual
destruction/erasure** (QR, temporary pairing secret, failed provisional material, phone-side recovery-code
copy, rollback packages), which directly conflicts with the universal no-destruction rule; and **revocation /
invalidation** (old codes, old recovery sheet, prior trusted phones), which is not by itself proven to be
destruction. The latter becomes a conflict only if v8's requirement that preserved credentials remain
"internally usable" is intended to preserve authorization capability after revocation. That narrower issue
remains K9. The broad claim that security is entirely unchanged is still unsupported.

**K5 — v8 deletion/influence rules vs TSC privacy, exclusion, retained archive, deletion (SRC-002). →
CONFLICTING.** SRC-002 §25 + §30 require that **excluded content is never held**: "Raw content not held
in §7E or TSC at any point … raw content replaced with non-reconstructive exclusion metadata"
(`src002 L734–743`); "TSC must not retain excluded content in the active database, the §7E pre-ingest
record, or the retained safety archive" (`src002 L907–909`); deletion writes a **tombstone**
(`src002 L708–709`); the retained archive holds "structural records and references — not raw content
excluded under §7Q" (`src002 L681–686`). v8 §7Q redefines exclusion as **moving raw content to sealed
protected storage** (preserved, `v8 L1122`) and deletion as non-destructive (content preserved, history
record "not a tombstone"). v8's "preserve everything in sealed storage" conflicts with TSC's "never hold
excluded content / tombstone-only."

**K6 — Full-Transparency Law: record every use AND non-use. → UNCLEAR (unbounded self-reference risk).**
v8 §0B (`L260`) requires that "every time N.H uses a record … that use event must itself be recorded," and
non-use "must also be recorded." A use-record is itself an operational record; using or examining a
use-record is itself a use that the same rule says must be recorded. Whether this terminates or generates
an unbounded chain of use-records-about-use-records is not specified. v8's triggered-recursion limit
(`L256–258`) bounds *examination* but does not on its face bound *use-recording*. **UNCLEAR** — preserved
for Ness.

**K7 — Triggered recursive examination vs uncontrolled recursion. → UNCLEAR.** v8 §0B (`L256–258`):
"Recursive examination is triggered — not automatic … There is no fixed maximum depth when deeper
examination serves a real purpose. There is also no uncontrolled automatic recursion in the absence of a
trigger." Whether "triggered, no fixed max depth" sufficiently bounds depth/cost once a trigger fires
(e.g., a trigger that recursively re-triggers) is not specified. **UNCLEAR.**

**K8 — Privacy / storage-volume / performance / retrieval-weighting / double-influence. → UNCLEAR.**
v8 §0B makes every operational record "part of N.H's living memory … subject to the same retrieval,
connection-building, reading, interpretation, and reread rules as any other stored material" (`L252`).
Open, unresolved implications: (a) **storage volume** — recording every operation + every use + every
non-use of every record is large and grows super-linearly; (b) **performance** — retrieval/ranking over an
ever-growing operational corpus; (c) **retrieval-weighting / double-influence** — if the record of *using*
a reading is itself a retrievable, rankable memory, a single underlying fact may influence an output both
as the reading and as the use-record of that reading; v8 does not state how operational records are
weighted vs primary roots/readings, or how double-counting is prevented; (d) **privacy** — operational
records "carry only the opaque protected-record identifier" for Level-1/sealed material (`L211`, `L278`),
but the volume of handling metadata is itself a new surface. All **UNCLEAR**; none resolved.

**K9 — Permanently preserving Level-1 secrets vs credential rotation / invalidation / revocation /
destruction. → CONFLICTING / UNCLEAR.** v8 §0A/§0B/§7Q: Level-1 live secrets and credentials are "never
permanently destroyed"; on a deletion request "the content remains in Level 1 sealed protected storage"
(`v8 L1185`). The security purpose of credential handling is the opposite for compromised/rotated
material: a leaked key, an old recovery code, a consumed one-time code, or a revoked token is meant to be
rotated, invalidated, revoked, or destroyed so it can never be used again — SRC-001 explicitly destroys
the QR/pairing-secret/recovery-code-copies/failed-provisional-material and makes old codes "permanently
invalid." Whether v8's "seal, never destroy" is compatible with "invalidate/revoke so it can never grant
access again" — i.e., whether revocation-without-destruction is sufficient security, and whether
permanently retaining every superseded secret is acceptable — is the core **CONFLICTING** (vs SRC-001
destruction) / **UNCLEAR** (whether revoke ≠ destroy resolves it) question. Not resolved here.

**K10 — v8 §0A "security entirely unchanged" vs the new no-destruction rule. → CONFLICTING.** v8 asserts
in two places that the two protection levels "do not weaken or replace identity verification, biometric
authorization, SACL, BAI, anti-impersonation, or any other security layer" (`v8 L223`-area, `L282`). Yet
the universal no-destruction rule materially changes how BAI/pairing/recovery/BGMM handle single-use
secret material (K3–K4, K9). The "unchanged" claim and the new universal rule are in tension. **CONFLICTING.**

---

## 5. CANDIDATE FEATURE REGISTER (new mechanisms introduced by the candidates)

Every entry is a feature carried by a non-authoritative candidate file. The **file-level** status is
**CANDIDATE — NOT CURRENT AUTHORITY**. Do not infer from that label that the feature itself was never
accepted, integrated, or built: Stage 3B must determine feature-level acceptance/adoption, integration, and
build evidence separately. Purpose / behavior / dependencies / exact direct-source ranges are stated here;
this intake itself integrates nothing.

**F1 — Two-level sensitive-content protection.** *Purpose:* protect different sensitive material at the
right strength — Level 1 (live secrets/credentials) vs Level 2 (private personal info). *Behavior:* Level 1
is sealed, never displayed/quoted/exported/summarized in raw form under any circumstance including to Ness;
Level 2 is protected from unauthorized access but available to Ness by default after identity verification.
*Dependencies:* §0B handling records; §7Q operations; identity verification/SACL/BAI (claimed unchanged).
*Status:* CANDIDATE. *Source:* `v8 §0A L201–225`, `§0B L272–282`, `§7Q tiers L1163–1185`.

**F2 — Sealed execution boundary.** *Purpose:* let authorized functions use Level-1 raw content without
exposing it. *Behavior:* raw Level-1 content is processed only inside a protected boundary; only the
"minimum safe result" may leave; the result must not reconstruct/reveal/allow-inference of the raw content;
every entry is logged via the opaque ID. *Dependencies:* F1, F3, F4. *Status:* CANDIDATE. *Source:*
`v8 §0A L213`, `§0B L274`, `§7Q Layer A L1177–1185`.

**F3 — Opaque protected-record identifiers.** *Purpose:* let ordinary records reference sealed items
without leaking where/how they are stored. *Behavior:* ordinary records carry only an opaque ID + the full
handling/use log; they never carry the raw content, physical location, encryption details, or access path.
*Dependencies:* F1, F2, F4. *Status:* CANDIDATE. *Source:* `v8 §0A L205–215`, `§0B L278`, `§7Q L1122–1130`.

**F4 — Full-Transparency and Living-Record Law (§0B).** *Purpose:* permanently record and connect
everything N.H does, as active memory. *Behavior:* universal recording of all external info and all
internal cognition/operations; each record carries 10 specified fields; records are living memory subject
to retrieval/connection/reread (not passive audit); invisibility-in-chat is not an exception to recording;
mandatory connections. *Dependencies:* every component; the meaning engine; §7Q. *Status:* CANDIDATE.
*Source:* `v8 §0B L226–287`.

**F5 — Mandatory use and non-use records.** *Purpose:* record how every record is used, including when it
is deliberately not used. *Behavior:* every retrieval/read/pass-to-mouth/accept/reject/ignore/connect/
examine is a recorded use event with stated fields; a candidate evaluated and set aside is a recorded
**non-use** with its reason. *Dependencies:* F4. *Status:* CANDIDATE. *Source:* `v8 §0B L260`; enforced in
`DD §0 L33` and `Cursor §1A L79–103`. *Open:* see conflict K6 (self-reference) and K8 (double-influence).

**F6 — Triggered recursive self-examination.** *Purpose:* let N.H examine its own logs/decisions/
understandings and use the results, without continuous auto-recursion. *Behavior:* examination is
triggered (relevance signal, system purpose, design rule, detected inconsistency, Ness's question, or
authorized trigger), runs as deep as the trigger requires with no fixed maximum, and is itself recorded;
"no uncontrolled automatic recursion in the absence of a trigger." *Dependencies:* F4. *Status:* CANDIDATE.
*Source:* `v8 §0B L254–258`. *Open:* see conflict K7.

**F7 — Six privacy operations.** *Purpose:* a distinct, non-interchangeable operation set for §7Q.
*Behavior:* Exclusion, **Sealed isolation (new)**, Hiding, Restriction, Redaction, Deletion — each defined,
each preserving internal usability "unless a separate influence-removal instruction applies." *Dependencies:*
F1, F8, F9. *Status:* CANDIDATE. *Source:* `v8 §7Q L1120–1136`. *Replaces:* v7_1's five operations
(conflict K2/K5).

**F8 — Non-destructive deletion.** *Purpose:* redefine "deletion" as visibility removal, never erasure.
*Behavior:* deletion removes material from ordinary visible output/paths only; content is preserved,
connected, internally usable; cryptographic erasure of the only copy is prohibited; outcome states
`protected_complete` / `protected_with_declared_limits` / `incomplete` / `blocked` / `failed`; a positive
**history record** (not a tombstone) is kept; the prior "make inaccessible to all internal functions" rule
is marked REJECTED. *Dependencies:* F4, F9. *Status:* CANDIDATE. *Source:* `v8 §7Q L1138–1162`,
`§0A L223–225`, `§0B L284–286`. *Conflicts:* K2, K3, K5, K9.

**F9 — Separate influence-removal instruction.** *Purpose:* separate "hide from view" from "stop
influencing N.H." *Behavior:* stopping a record's internal influence (readings/retrieval/connections/
reasoning) requires an explicit separate instruction stating scope, affected components, and start time;
it does not follow automatically from deletion or hiding, and is recorded separately. *Dependencies:* F8,
F4. *Status:* CANDIDATE. *Source:* `v8 §7Q L1146–1148`.

**F10 — Defaults (v2.3) enforcement rules.** *Purpose:* propagate F4/F7/F8 into the behavioral guide.
*Behavior:* §0 override requiring per-component operational recordkeeping (silent operations prohibited);
§3 §7Q entry restated to six operations / two levels / non-destructive deletion / five outcome states; §6
new "EVERYTHING IS RECORDED" principle + deletion principle flipped + pure-tape principle updated.
*Dependencies:* F4–F9. *Status:* CANDIDATE (file self-labeled "pending adoption"). *Source:* `v2.3 L33,
L137, L309, L313, L317`.

**F11 — Cursor (v3.3) enforcement rules.** *Purpose:* propagate F4/F8 into the coding rules. *Behavior:*
§1A rule making any internal operation without a mandatory append-only linked record a "prohibited
function" (enumerated operations + required fields); §1A rule forbidding code that permanently destroys or
cryptographically erases the only copy of any content (deletion = non-destructive visibility removal).
*Dependencies:* F4, F8. *Status:* CANDIDATE (no adoption evidence beyond the supersession line).
*Source:* `v3.3 §1A L79–103` (transparency), `L105–108` (no-destruction). *Conflict:* K3 (vs SRC-001
destruction requirements).

---

## 6. CANDIDATE EVIDENCE-AND-CONFLICT REGISTER (not an active decision queue)

These candidate files do **not** create new unresolved Ness decisions merely by existing. Stage 3B must
classify the following questions through direct historical evidence without reopening current settled rules.
An item becomes an active Ness decision only if the evidence leaves a genuine unresolved conflict and Ness
explicitly chooses to revisit it.

- R1 — Determine whether direct evidence formally adopted Master v8, Defaults v2.3, or Cursor v3.3 as files.
  Absent exact-version adoption evidence, each remains a non-authoritative candidate.
- R2 — Determine whether Ness separately accepted the v8 **non-destructive deletion** behavior at the
  feature level after the current-authority deletion design, even if the v8 file itself was never adopted.
- R3 — Determine whether Ness separately accepted the **universal no-destruction / preserve-everything**
  rule, and preserve any direct reconciliation he gave for security materials that SRC-001 requires to be
  destroyed or erased.
- R4 — Determine whether the historical evidence explicitly distinguishes **invalidate / revoke** from
  **destroy**, and whether retained revoked credentials are allowed to remain stored but permanently unable
  to authorize anything. Do not treat invalidation as destruction without evidence.
- R5 — Determine the feature-level acceptance status of the **two-level protection model**, including the
  rule that Level-1 raw material may remain inaccessible even to Ness.
- R6 — Determine whether later accepted design changed **exclusion** from non-capture/removal to sealed
  preservation. Preserve the direct evidence and do not silently reconcile the opposite TSC rule.
- R7 — Determine the feature-level acceptance status of the **Full-Transparency and Living-Record Law** and
  preserve any accepted bounds for use-record recursion, recursive examination, storage growth, performance,
  retrieval weighting, privacy, and double influence.
- R8 — Determine whether operational records were accepted as retrieval/ranking candidates alongside roots
  and readings, and whether any weight or anti-double-counting rule was accepted.
- R9 — Record v8's "no settled design changed" sentence as an internal provenance error unless direct
  historical evidence shows a narrower intended meaning. This is a correction issue, not a concept choice.
- R10 — Record the candidate-set Cursor-version mismatch (v8 §6A says v3.2 while Defaults v2.3 and Cursor
  v3.3 assume the v8 laws) as a cross-file consistency defect. Do not ask Ness to choose a version unless
  file adoption later becomes live.
- R11 — For every feature proven accepted but not integrated, record the exact integration gap against the
  Master, Defaults, Cursor Rules, SRC-001, and SRC-002. Accepted does not automatically mean integrated;
  do not silently patch or reconcile it during recovery.

---

## 7. STAGE-3B PLACEMENT NOTE

SUP-001 (Master v8), SUP-002 (Defaults v2.3), and SUP-003 (Cursor Rules v3.3) are **retained in the
later feature-comparison queue for Stage 3B**, even though none is adopted authority. They enter Stage 3B
as **candidate successors** to be compared, feature-by-feature, against the current authority baseline
(v7_1 / v2.2 / v3.2) and against the Stage 3A recovery (v1 + v1.2) and the accepted companions
(SRC-001 / SRC-002). Their presence in the queue is **not file adoption** and does **not** change current authority. Equally,
file-level non-adoption must not be used as proof that every carried feature was never accepted. Stage 3B
must trace each material feature to direct historical evidence and classify file adoption, feature acceptance,
integration, conflict, unresolved status, and build evidence separately.

---

## STATE AFTER SUPPLEMENTAL INTAKE (nothing adopted, nothing changed)
- Three candidates hash-verified (exact match) and read in full; assigned SUP-001–SUP-003; **outside** the
  SRC-001–092 set, which was not altered.
- Current architectural, behavioral, and operational authority unchanged: **Master v7_1 · Defaults v2.2 ·
  Cursor Rules v3.2**. The governance companion remains controlling only within its stated non-architectural
  scope. No candidate body contains exact-version file-adoption evidence (v8 carries the inherited v7 line;
  v2.3 self-labels "pending adoption"; v3.3 carries only a supersession line); Stage 3B must still test
  separate historical evidence and feature-level acceptance.
- Delta map, conflict audit (10 items, all marked CONFLICTING/UNCLEAR, none resolved), candidate-carried
  feature register (11 mechanisms), and evidence-and-conflict register (11 items; not an active decision
  queue) produced.
- No candidate adopted, integrated, patched, or reconciled; no contradiction resolved; no N.H design
  changed; no architecture decided for Ness; no final Master drafted; **Stage 3B not begun.**

**SUPPLEMENTAL CANDIDATE INTAKE COMPLETE. AWAITING NESS.**
