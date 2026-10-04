# Chapter 3-h — Group A: C-GOLD, judgment-authorization claims and protected recovery

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-h.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This pair continues C-GOLD.1 under CY-G. Chapter 3-g decomposes bridge §§7.11–7.12: the judgment chain, authority modes and each conditional proof lifecycle. Chapter 3-h decomposes §7.13: the claim record, states, transitions, one-winner scope, replacement gates and fences, together with protected judgment recovery and logging. The complete result-derivation and per-reading applicability rules remain for later pieces; this pair does not complete C-GOLD, the evaluation bridge or Group A.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1; the Map is subordinate. All new behavior and relationship rows are ACCEPTED from the exact accepted bridge v1.7. Receipt §§3–5 binds acceptance to SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`; its frozen candidate header does not change that standing. None of these bridge behaviors or links has BUILT standing in V10’s status table.

Citation keys: `05/` = `05_ACTIVE_CANDIDATE/`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = Design and Wiring Map v1.6. NHD-B16EEB identifies the accepted bridge. Its open decisions use the receipt’s globally unique NHD-B16EEB-D… identifiers. All source-proposed field, record, event and state names remain proposed; no option, policy value, physical representation or implementation is selected.

Continuation entries stay in this piece; joining the pieces concatenates them and does not merge or edit passed cards. C-GOLD’s existing top-card continuation remains C-GOLD.1 — Promotion evaluation-evidence bridge, both as a SUB-PART and as Fed by. The protected stages remain linked durable stages; only E9 + E16 is one O-APPEND atomic commit.

<!-- BEGIN CHAPTER 3-h BEHAVIOR -->

### C-GOLD.1.7 — Judgment-authorization claims and protected recovery
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The one-winner coordination claim and its durable lifecycle, fences and lookup-first recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE identity, exact E9 identity, expected judgment head and authority proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Serializes one protected judgment scope without granting authority; preserves pending ownership and receipt-bearing non-replaceability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — A committed judgment, valid no-receipt closure or blocking receipt-bearing breach closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Release a pending owner, replace a receipt-bearing claim or reconstruct BAI authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory claim/receipt evidence makes scope and chain judgment_indeterminate; receipts without matching claims commit nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Coordinates access to BAI’s accepted authority or the SACL-only judgment commit; records append-only state transitions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.2 — Claim ownership separation: The bridge owns coordination; BAI owns token truth and receipt; the judgment chain owns its head; O-APPEND owns E9 + E16 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4 — Claim state and transition rules: Moves through the source-defined states without rewriting prior state records; distinguishes no-receipt release from receipt-bearing closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Admits a new deliberate O-JUDGE only when no claim owns the scope, or the prior claim is released/superseded with positive proof of no valid receipt and a durable non-success owner terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.6 — Contradictory claim and receipt evidence: Marks the scope and its chain judgment_indeterminate; preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Keeps claim transitions as canonical child state records; O-JUDGE logs its one terminal, naming the claim and final state and the O-APPEND that committed/refused E9. Each O-APPEND logs its own terminal; B9 logs only its own retry requests; BAI alone writes its security audit events. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.8 — Two protected pending situations: Keeps the pending O-JUDGE and its scope fence; follows only the permitted continuation for its proof stage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9 — Protected judgment lookup-first recovery: Looks up actual durable state and applies only the source-defined missing work once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.10 — Protected judgment invariants: Enforces INV-22, INV-23, INV-25, INV-26 and INV-27. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: Claim scope admits only one active-or-successful owner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Serializes one protected judgment scope without granting authority; preserves pending ownership and receipt-bearing non-replaceability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | O-JUDGE identity, exact E9 identity, expected judgment head and authority proof. | Serializes one protected judgment scope without granting authority; preserves pending ownership and receipt-bearing non-replaceability. | A committed judgment, valid no-receipt closure or blocking receipt-bearing breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE [proposed] | O-JUDGE identity, exact E9 identity, expected judgment head and authority proof. | O-JUDGE follows one-winner claim ownership, fence and recovery rules. | A committed judgment, valid no-receipt closure or blocking receipt-bearing breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-BAI.20.4 — Judgment post-receipt recovery | The flushed receipt and its chain, expected head, proposed E9 content identity, purpose/scope, token and integrity binding. | Gates this place: retains the scope fence and forbids replacement of receipt-bearing ownership. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16] |
| 4 · ACCEPTED | C-GOLD.1.12.1 — Open judgment-fork and breach resolution | A `judgment_indeterminate` [proposed] chain, including a `closed_after_breach` [proposed] claim whose valid durable receipt remains preserved. | Preserves the contradictory chain/claim/receipt evidence and non-replaceable breach closure. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] |
| 5 · ACCEPTED | C-BAI.20.3 — Judgment no-receipt failure | No verified durable consumption proof, including an uncertain in-memory consume attempt. | Takes this place's change: receives the no-receipt fact and applies its protected linked release rules. | Receives the no-receipt fact and applies its protected linked release rules. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB-D16] |

SUB-PARTS: C-GOLD.1.7.1 — judgment_authorization_claim [proposed]; C-GOLD.1.7.2 — Claim ownership separation; C-GOLD.1.7.3 — One-winner judgment-authorization scope; C-GOLD.1.7.4 — Claim state and transition rules; C-GOLD.1.7.5 — Claim fence and new-judgment admission; C-GOLD.1.7.6 — Contradictory claim and receipt evidence; C-GOLD.1.7.7 — Protected-judgment log ownership; C-GOLD.1.7.8 — Two protected pending situations; C-GOLD.1.7.9 — Protected judgment lookup-first recovery; C-GOLD.1.7.10 — Protected judgment invariants

### C-GOLD.1.7.1 — judgment_authorization_claim [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The canonical one-winner serialization slot for one judgment authorization scope; all names remain proposed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Coordinates access to BAI’s accepted authority or the SACL-only judgment commit; records append-only state transitions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A coordination record, never an authorization grant or operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute the claim for the durable receipt or treat it as a second authorization authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory claims or receipt evidence make the scope and its chain judgment_indeterminate; preserve all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.1.1 — judgment_claim_id [proposed]: Records a stable unique claim identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.2 — judgment_chain_key [proposed]: Records the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed]: Records the exact head this judgment intends to extend, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.4 — e9_content_identity [proposed]: Records digest of the exact E9 content to commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed]: Records the NHD-B16EEB-D16-declared purpose/scope reference: per judgment or its approved judging scope; no value is chosen here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.6 — judging_operation_id [proposed]: Records the owning O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.7 — attached_token_ref [proposed]: Records where applicable, the BAI token reference attached at attach time; only this token may be consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.8 — durable_receipt_ref [proposed]: Records after consumption, the flushed bai_token_consumed receipt identity and integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.9 — state [proposed]: Records current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.10 — supersedes_claim_ref [proposed]: Records the append-only explicit link to the prior released/superseded no-receipt claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.11 — superseded_by_claim_ref [proposed]: Records the append-only explicit link to the replacing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.12 — linked_contradiction_ref [proposed]: Records the append-only explicit link to the recorded judgment-head breach contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.13 — created_at [proposed]: Records the claim’s created_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.14 — terminal_at [proposed]: Records the claim’s terminal_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.15 — schema_version [proposed]: Records the claim’s schema_version field; no concrete version value is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.16 — claim integrity reference: Records the integrity reference required on each canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.1 — Canonical record preservation: Canonical state records remain immutable and append-only; corrections are new linked records, with integrity reference, schema_version and creating operation identity; no copied gold/root/reading text. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Coordinates access to BAI’s accepted authority or the SACL-only judgment commit; records append-only state transitions. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.1.1 — judgment_claim_id [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.1.2 — judgment_chain_key [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.1.4 — e9_content_identity [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.1.6 — judging_operation_id [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.1.7 — attached_token_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.7.1.8 — durable_receipt_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.7.1.9 — state [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.7.1.10 — supersedes_claim_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.7.1.11 — superseded_by_claim_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.7.1.12 — linked_contradiction_ref [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.7.1.13 — created_at [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.7.1.14 — terminal_at [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 16 · ACCEPTED | C-GOLD.1.7.1.15 — schema_version [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | This is a member of the coordination-only claim; it never substitutes for authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 17 · ACCEPTED | C-GOLD.1.7.4.7.1 — Admit → claimed | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 18 · ACCEPTED | C-GOLD.1.7.4.7.2 — claimed → consumed_pending_commit [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 19 · ACCEPTED | C-GOLD.1.7.4.7.3 — consumed_pending_commit [proposed] → judgment_committed [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 20 · ACCEPTED | C-GOLD.1.7.4.7.4 — claimed → judgment_committed [proposed] under SACL-only | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 21 · ACCEPTED | C-GOLD.1.7.4.7.5 — claimed → released | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 22 · ACCEPTED | C-GOLD.1.7.4.7.6 — released → superseded | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 23 · ACCEPTED | C-GOLD.1.7.4.7.7 — consumed_pending_commit [proposed] → closed_after_breach [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the stated canonical claim transition and preserves previous records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 24 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Serializes one protected judgment scope without granting authority; preserves pending ownership and receipt-bearing non-replaceability. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 25 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 26 · ACCEPTED | C-GOLD.1.7.3.4 — Claim duplicate admission | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Absorbs only an identical request with the same scope, O-JUDGE and content; refuses any other duplicate. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 27 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Moves through the source-defined states without rewriting prior state records; distinguishes no-receipt release from receipt-bearing closure. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 28 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends the linked state change when its exact gate holds. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 29 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Admits a new deliberate O-JUDGE only when no claim owns the scope, or the prior claim is released/superseded with positive proof of no valid receipt and a durable non-success owner terminal. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 30 · ACCEPTED | C-GOLD.1.7.5.1 — No-receipt replacement admission | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 31 · ACCEPTED | C-GOLD.1.7.5.6 — Only the winning attached token | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Consumes only the token attached to the winning claim; a second token returns the existing reference or fails closed without consumption. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 32 · ACCEPTED | C-GOLD.1.7.8.1 — Pending before authority consumption | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Keeps the same O-JUDGE pending with no terminal and its claim claimed/owned; continuation uses a new B9 episode under consumed real-change with unchanged canonical inputs and a new O-APPEND under the same O-JUDGE. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 33 · ACCEPTED | C-GOLD.1.7.8.2 — Pending after authority consumption | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Keeps the scope fenced; forward-completes exactly the named E9 through B9-admitted O-APPENDs if needed, or records a head breach and closes closed_after_breach. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 34 · ACCEPTED | C-GOLD.1.6.4.7 — Pre-receipt crash rule | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 35 · ACCEPTED | C-GOLD.1.6.4.8 — In-process receipt-write failure | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 36 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 37 · ACCEPTED | C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Commits the one-winner authorization claim before touching a token. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 38 · ACCEPTED | C-GOLD.1.7.4.1 — Claim state claimed | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Writes claimed before touching any token; grants no authority. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 39 · ACCEPTED | C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 40 · ACCEPTED | C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Records judgment_committed; the owning O-JUDGE reaches judgment_committed. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 41 · ACCEPTED | C-GOLD.1.7.4.4 — Claim state released | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 42 · ACCEPTED | C-GOLD.1.7.4.5 — Claim state superseded | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Records superseded and superseded_by_claim_ref without altering prior records. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 43 · ACCEPTED | C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 44 · ACCEPTED | C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 45 · ACCEPTED | C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 46 · ACCEPTED | C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption) | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 47 · ACCEPTED | C-GOLD.1.7.9.11 — CR-36 — Two concurrent claims for one scope | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 48 · ACCEPTED | C-GOLD.1.7.9.12 — CR-37 — Competing O-JUDGE [proposed] while the scope is consumed_pending_commit [proposed] | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 49 · ACCEPTED | C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 50 · ACCEPTED | C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim | Claim identity, output key, expected head, exact E9 content, purpose/scope, operation, optional attached token and receipt, state and append-only links. | Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach | A coordination record, never an authorization grant or operational log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| 51 · ACCEPTED | C-GOLD.1.7.1.16 — claim integrity reference | The integrity reference required on each canonical record. | The containing claim remains a canonical coordination record. | The claim integrity reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 52 · ACCEPTED | C-GOLD.1.7.8.2 — Pending after authority consumption | consumed_pending_commit with durable receipt and no E9 commit. | The durable receipt stays bound to its winning claim and exact E9. | Exact forward completion or non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.1.1 — judgment_claim_id [proposed]; C-GOLD.1.7.1.2 — judgment_chain_key [proposed]; C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed]; C-GOLD.1.7.1.4 — e9_content_identity [proposed]; C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed]; C-GOLD.1.7.1.6 — judging_operation_id [proposed]; C-GOLD.1.7.1.7 — attached_token_ref [proposed]; C-GOLD.1.7.1.8 — durable_receipt_ref [proposed]; C-GOLD.1.7.1.9 — state [proposed]; C-GOLD.1.7.1.10 — supersedes_claim_ref [proposed]; C-GOLD.1.7.1.11 — superseded_by_claim_ref [proposed]; C-GOLD.1.7.1.12 — linked_contradiction_ref [proposed]; C-GOLD.1.7.1.13 — created_at [proposed]; C-GOLD.1.7.1.14 — terminal_at [proposed]; C-GOLD.1.7.1.15 — schema_version [proposed]; C-GOLD.1.7.1.16 — claim integrity reference

### C-GOLD.1.7.1.1 — judgment_claim_id [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment_claim_id member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A stable unique claim identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records a stable unique claim identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The judgment_claim_id member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | A stable unique claim identity. | Records a stable unique claim identity. | The judgment_claim_id member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.2 — judgment_chain_key [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment_chain_key member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The judgment_chain_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Receipt-bound forward completion verifies this claim binding before committing the exact named E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The output’s planned_trial_output_key. | Records the output’s planned_trial_output_key. | The judgment_chain_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.1 — receipt chain | The durable receipt and winning claim. | The receipt is bound to the intended judgment chain. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The expected_previous_judgment_head member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact head this judgment intends to extend, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact head this judgment intends to extend, or none for the first judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The expected_previous_judgment_head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Receipt-bound forward completion verifies this claim binding before committing the exact named E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The exact head this judgment intends to extend, or none for the first judgment. | Records the exact head this judgment intends to extend, or none for the first judgment. | The expected_previous_judgment_head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.2 — receipt expected head | The durable receipt and winning claim. | The receipt matches the claim’s expected judgment head. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.4 — e9_content_identity [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The e9_content_identity member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Digest of the exact E9 content to commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records digest of the exact E9 content to commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The e9_content_identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Receipt-bound forward completion verifies this claim binding before committing the exact named E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | Digest of the exact E9 content to commit. | Records digest of the exact E9 content to commit. | The e9_content_identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.3 — receipt E9 content identity | The durable receipt and winning claim. | The receipt binds the exact E9 content identity named by the claim. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The d16_purpose_scope_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The NHD-B16EEB-D16-declared purpose/scope reference: per judgment or its approved judging scope; no value is chosen here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the NHD-B16EEB-D16-declared purpose/scope reference: per judgment or its approved judging scope; no value is chosen here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The d16_purpose_scope_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The NHD-B16EEB-D16-declared purpose/scope reference: per judgment or its approved judging scope; no value is chosen here. | Records the NHD-B16EEB-D16-declared purpose/scope reference: per judgment or its approved judging scope; no value is chosen here. | The d16_purpose_scope_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.4 — receipt purpose and scope | The durable receipt and winning claim. | The receipt has the required accepted purpose and scope. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.6 — judging_operation_id [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judging_operation_id member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The owning O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the owning O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The judging_operation_id member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE [proposed]: Supplies the owning O-JUDGE operation identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The owning O-JUDGE identity. | Records the owning O-JUDGE identity. | The judging_operation_id member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.7 — attached_token_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The attached_token_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Where applicable, the BAI token reference attached at attach time; only this token may be consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records where applicable, the BAI token reference attached at attach time; only this token may be consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The attached_token_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume a token other than the token attached to the winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A second token for an already claimed or committed scope is not consumed; return the existing reference or fail closed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | Where applicable, the BAI token reference attached at attach time; only this token may be consumed. | Records where applicable, the BAI token reference attached at attach time; only this token may be consumed. | The attached_token_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.5.6 — Only the winning attached token | Where applicable, the BAI token reference attached at attach time; only this token may be consumed. | Only this attached token may be consumed. | The attached_token_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.4.9.5 — receipt token | The durable receipt and winning claim. | The receipt names the token attached to the winning claim. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.5.6 — Only the winning attached token | A token presented for an already claimed or committed scope. | The token matches the winning claim’s attached_token_ref. | No second consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.8 — durable_receipt_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The durable_receipt_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — After consumption, the flushed bai_token_consumed receipt identity and integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records after consumption, the flushed bai_token_consumed receipt identity and integrity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The durable_receipt_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.1.8.1 — durable receipt identity: Records identity of the flushed bai_token_consumed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.1.8.2 — durable receipt integrity: Records integrity reference of that same flushed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Receipt-bound forward completion verifies this claim binding before committing the exact named E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | After consumption, the flushed bai_token_consumed receipt identity and integrity. | Records after consumption, the flushed bai_token_consumed receipt identity and integrity. | The durable_receipt_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed] | A durable receipt bound to this claim exists. | A valid durable bound receipt exists. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.4.4.1.1 — No claim receipt reference | Claim and security-audit receipt lookup. | No durable_receipt_ref exists on this claim. | One required no-receipt proof condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.1.8.1 — durable receipt identity; C-GOLD.1.7.1.8.2 — durable receipt integrity

### C-GOLD.1.7.1.8.1 — durable receipt identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The durable receipt identity member of durable_receipt_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Identity of the flushed bai_token_consumed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records identity of the flushed bai_token_consumed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The durable receipt identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat token presence as durable receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable or contradictory receipt evidence blocks usable judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The durable receipt binding must verify. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1.8 — durable_receipt_ref [proposed] | Identity of the flushed bai_token_consumed receipt. | Records identity of the flushed bai_token_consumed receipt. | The durable receipt identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.8.2 — durable receipt integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The durable receipt integrity member of durable_receipt_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Integrity reference of that same flushed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records integrity reference of that same flushed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The durable receipt integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat token presence as durable receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable or contradictory receipt evidence blocks usable judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The durable receipt binding must verify. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1.8 — durable_receipt_ref [proposed] | Integrity reference of that same flushed receipt. | Records integrity reference of that same flushed receipt. | The durable receipt integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.6 — receipt integrity check | The durable receipt and winning claim. | The receipt integrity is verifiable. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.9 — state [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The state member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The state member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Use released or superseded for a receipt-bearing claim; release while O-JUDGE remains pending. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4 — Claim state and transition rules: Receipt-bearing claims close only as judgment_committed or closed_after_breach; no-receipt release requires durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | Current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. | Records current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. | The state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.10 — supersedes_claim_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The supersedes_claim_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The append-only explicit link to the prior released/superseded no-receipt claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the append-only explicit link to the prior released/superseded no-receipt claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The supersedes_claim_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The append-only explicit link to the prior released/superseded no-receipt claim. | Records the append-only explicit link to the prior released/superseded no-receipt claim. | The supersedes_claim_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.11 — superseded_by_claim_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The superseded_by_claim_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The append-only explicit link to the replacing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the append-only explicit link to the replacing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The superseded_by_claim_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The append-only explicit link to the replacing claim. | Records the append-only explicit link to the replacing claim. | The superseded_by_claim_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.12 — linked_contradiction_ref [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The linked_contradiction_ref member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The append-only explicit link to the recorded judgment-head breach contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the append-only explicit link to the recorded judgment-head breach contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The linked_contradiction_ref member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The append-only explicit link to the recorded judgment-head breach contradiction. | Records the append-only explicit link to the recorded judgment-head breach contradiction. | The linked_contradiction_ref member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.13 — created_at [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The created_at member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The claim’s created_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the claim’s created_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The created_at member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The claim’s created_at field; no physical type or timestamp format is supplied. | Records the claim’s created_at field; no physical type or timestamp format is supplied. | The created_at member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.14 — terminal_at [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The terminal_at member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The claim’s terminal_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the claim’s terminal_at field; no physical type or timestamp format is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The terminal_at member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The claim’s terminal_at field; no physical type or timestamp format is supplied. | Records the claim’s terminal_at field; no physical type or timestamp format is supplied. | The terminal_at member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.15 — schema_version [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The schema_version member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The claim’s schema_version field; no concrete version value is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the claim’s schema_version field; no concrete version value is supplied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The schema_version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat this coordination member as authorization or an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — At claim-record level, contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate; all records are preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: This is a member of the coordination-only claim; it never substitutes for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The claim’s schema_version field; no concrete version value is supplied. | Records the claim’s schema_version field; no concrete version value is supplied. | The schema_version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.1.16 — claim integrity reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The claim integrity reference member of judgment_authorization_claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The integrity reference required on each canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the integrity reference required on each canonical record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The claim integrity reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Edit an immutable record or use claim identity as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: The containing claim remains a canonical coordination record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | The integrity reference required on each canonical record. | Records the integrity reference required on each canonical record. | The claim integrity reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.2 — Claim ownership separation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim ownership separation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The claim, BAI token/receipt, judgment head and E9/E16 append. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — The bridge owns coordination; BAI owns token truth and receipt; the judgment chain owns its head; O-APPEND owns E9 + E16 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Separated state and authority ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat the coordinator as an authorization authority or its record as an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A claim cannot substitute for a missing receipt; an unmatched receipt commits nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The judgment chain owns the head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The claim coordinates only; BAI’s valid durable receipt or the selected commit-time SACL proof is required for authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.13 — O-APPEND [proposed]: O-APPEND owns only the E9 + E16 atomic commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | The claim, BAI token/receipt, judgment head and E9/E16 append. | The bridge owns coordination; BAI owns token truth and receipt; the judgment chain owns its head; O-APPEND owns E9 + E16 commit. | Separated state and authority ownership. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3 — One-winner judgment-authorization scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The One-winner judgment-authorization scope rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly one concurrent winner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume a losing claimant’s token or admit multiple owning claims for one scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A losing O-JUDGE ends judgment_claim_lost with one terminal and one log; its token is untouched. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.3.1 — scope judgment_chain_key [proposed]: Records the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3.2 — scope expected_previous_judgment_head [proposed]: Records the exact predecessor head, including none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3.3 — scope wider-purpose reference: Records the NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3.4 — Claim duplicate admission: Absorbs only an identical request with the same scope, O-JUDGE and content; refuses any other duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: An existing owning claim blocks a competitor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | Exactly one claim wins the authorization scope. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.9.11 — CR-36 — Two concurrent claims for one scope | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | Claim scope admits only one active-or-successful owner. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.5.9.8.1 — Authorization claim first | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | The claim-first stage admits exactly one scope winner. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.2 — Winning-token consumption order | The committed winning claim and its attached token. | The one-winner claim precedes BAI consumption. | One ordered protected judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.3.1 — scope judgment_chain_key [proposed] | The output’s planned_trial_output_key. | The one-active-or-successful-claim rule applies to this scope tuple. | The scope judgment_chain_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.3.2 — scope expected_previous_judgment_head [proposed] | The exact predecessor head, including none for the first. | The one-active-or-successful-claim rule applies to this scope tuple. | The scope expected_previous_judgment_head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.7.3.3 — scope wider-purpose reference | The NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. | The one-active-or-successful-claim rule applies to this scope tuple. | The scope wider-purpose reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.7.4.1 — Claim state claimed | A newly admitted winning claim before any token is touched. | The one-winner scope gate admits this claim. | An owned claim with no authorization grant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.3.1 — scope judgment_chain_key [proposed]; C-GOLD.1.7.3.2 — scope expected_previous_judgment_head [proposed]; C-GOLD.1.7.3.3 — scope wider-purpose reference; C-GOLD.1.7.3.4 — Claim duplicate admission

### C-GOLD.1.7.3.1 — scope judgment_chain_key [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope judgment_chain_key member of One-winner judgment-authorization scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the output’s planned_trial_output_key. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The scope judgment_chain_key member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Broaden the accepted scope or admit competing owners. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Concurrent claim admission permits only one winner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: The one-active-or-successful-claim rule applies to this scope tuple. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | The output’s planned_trial_output_key. | Records the output’s planned_trial_output_key. | The scope judgment_chain_key member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3.2 — scope expected_previous_judgment_head [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope expected_previous_judgment_head member of One-winner judgment-authorization scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact predecessor head, including none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact predecessor head, including none for the first. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The scope expected_previous_judgment_head member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Broaden the accepted scope or admit competing owners. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Concurrent claim admission permits only one winner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: The one-active-or-successful-claim rule applies to this scope tuple. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | The exact predecessor head, including none for the first. | Records the exact predecessor head, including none for the first. | The scope expected_previous_judgment_head member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3.3 — scope wider-purpose reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The scope wider-purpose reference member of One-winner judgment-authorization scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records the NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The scope wider-purpose reference member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Broaden the accepted scope or admit competing owners. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Concurrent claim admission permits only one winner. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: The one-active-or-successful-claim rule applies to this scope tuple. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | The NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. | Records the NHD-B16EEB-D16 scope reference when that accepted option defines a wider scope. | The scope wider-purpose reference member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3.4 — Claim duplicate admission
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim duplicate admission rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A duplicate creation request and the existing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Absorbs only an identical request with the same scope, O-JUDGE and content; refuses any other duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — An absorbed exact duplicate or refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume another token for a duplicate claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any non-identical duplicate is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.3.4.1 — duplicate scope equality: The duplicate request has the same scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3.4.2 — duplicate O-JUDGE [proposed] equality: The duplicate request has the same O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.3.4.3 — duplicate content equality: The duplicate request has the same content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — Scope, O-JUDGE identity and content all match for absorption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Absorbs only an identical request with the same scope, O-JUDGE and content; refuses any other duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | A duplicate creation request and the existing claim. | Absorbs only an identical request with the same scope, O-JUDGE and content; refuses any other duplicate. | An absorbed exact duplicate or refusal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.3.4.1 — duplicate scope equality; C-GOLD.1.7.3.4.2 — duplicate O-JUDGE [proposed] equality; C-GOLD.1.7.3.4.3 — duplicate content equality

### C-GOLD.1.7.3.4.1 — duplicate scope equality
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The duplicate scope equality rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The duplicate request and current claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — The duplicate request has the same scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One exact-duplicate condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Absorb an unequal duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any other duplicate is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The duplicate request has the same scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3.4 — Claim duplicate admission | The duplicate request and current claim. | The duplicate request has the same scope. | One exact-duplicate condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3.4.2 — duplicate O-JUDGE [proposed] equality
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The duplicate O-JUDGE equality rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The duplicate request and current claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — The duplicate request has the same O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One exact-duplicate condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Absorb an unequal duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any other duplicate is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The duplicate request has the same O-JUDGE identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3.4 — Claim duplicate admission | The duplicate request and current claim. | The duplicate request has the same O-JUDGE identity. | One exact-duplicate condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.3.4.3 — duplicate content equality
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The duplicate content equality rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The duplicate request and current claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — The duplicate request has the same content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One exact-duplicate condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Absorb an unequal duplicate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Any other duplicate is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The duplicate request has the same content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.3.4 — Claim duplicate admission | The duplicate request and current claim. | The duplicate request has the same content. | One exact-duplicate condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4 — Claim state and transition rules
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The append-only state machine of a judgment-authorization claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Claim ownership, durable terminal/receipt evidence and E9/E16 commit state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Moves through the source-defined states without rewriting prior state records; distinguishes no-receipt release from receipt-bearing closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved state history and the current claim state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Release a pending operation or replace a receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory evidence makes scope and chain judgment_indeterminate; receipt-bearing breach keeps the scope blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.4.1 — Claim state claimed: Writes claimed before touching any token; grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: Records judgment_committed; the owning O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.5 — Claim state superseded: Records superseded and superseded_by_claim_ref without altering prior records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7 — Append-only claim transitions: Appends the linked state change when its exact gate holds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Pending claims remain owned; receipt-bearing claims are never released or replaced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Moves through the source-defined states without rewriting prior state records; distinguishes no-receipt release from receipt-bearing closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Claim ownership, durable terminal/receipt evidence and E9/E16 commit state. | Moves through the source-defined states without rewriting prior state records; distinguishes no-receipt release from receipt-bearing closure. | Preserved state history and the current claim state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.1.9 — state [proposed] | Current state carried through append-only transitions: claimed, consumed_pending_commit, judgment_committed, released, superseded or closed_after_breach. | Receipt-bearing claims close only as judgment_committed or closed_after_breach; no-receipt release requires durable non-success and positive no-receipt proof. | The state member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.4.1 — Claim state claimed; C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]; C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]; C-GOLD.1.7.4.4 — Claim state released; C-GOLD.1.7.4.5 — Claim state superseded; C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]; C-GOLD.1.7.4.7 — Append-only claim transitions

### C-GOLD.1.7.4.1 — Claim state claimed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state claimed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A newly admitted winning claim before any token is touched. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Writes claimed before touching any token; grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — An owned claim with no authorization grant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Touch a token before the claim or treat claimed as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A second token for the scope is never consumed; return the existing reference or fail closed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: The one-winner scope gate admits this claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Writes claimed before touching any token; grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | A newly admitted winning claim before any token is touched. | Writes claimed before touching any token; grants no authority. | An owned claim with no authorization grant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.1 — Admit → claimed | A newly admitted winning claim before any token is touched. | Writes claimed before touching any token; grants no authority. | An owned claim with no authorization grant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.5.2 — Replacement blocked by claimed | A newly admitted winning claim before any token is touched. | This state blocks replacement. | An owned claim with no authorization grant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.8.1 — Pending before authority consumption | A newly admitted winning claim before any token is touched. | The pending owner keeps this state and its scope. | An owned claim with no authorization grant. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.5.2 — Replacement blocked by claimed | The prior scope claim is claimed. | The stated prior claim retains the scope. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state consumed_pending_commit rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A durable receipt bound to this claim exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A receipt-bearing pending claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Let another O-JUDGE consume, win a claim or commit a competing successor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A competitor is refused before consumption; only forward completion or closed_after_breach can end this receipt-bearing pending state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.8 — durable_receipt_ref [proposed]: A valid durable bound receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | A durable receipt bound to this claim exists. | Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.2 — claimed → consumed_pending_commit [proposed] | A durable receipt bound to this claim exists. | Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.5.3 — Replacement blocked by consumed_pending_commit [proposed] | A durable receipt bound to this claim exists. | This state blocks replacement. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.8.2 — Pending after authority consumption | A durable receipt bound to this claim exists. | The receipt-bearing fence remains active. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | A durable receipt bound to this claim exists. | A durable bound receipt advances the claim to consumed_pending_commit. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | A durable receipt bound to this claim exists. | The receipt-bearing claim fences the exact judgment scope during recovery. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.9.12 — CR-37 — Competing O-JUDGE [proposed] while the scope is consumed_pending_commit [proposed] | A durable receipt bound to this claim exists. | Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. | A receipt-bearing pending claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.5.3 — Replacement blocked by consumed_pending_commit [proposed] | The prior scope claim is consumed_pending_commit. | The stated prior claim retains the scope. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state judgment_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The named E9 + E16 committed through O-APPEND appended/absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records judgment_committed; the owning O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A successful receipt-bearing or selected-proof judgment claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement claim or consume another token for this scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Competing claim/token admission is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.13 — O-APPEND [proposed]: The named E9 and E16 committed or their exact duplicate was absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Records judgment_committed; the owning O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | The named E9 + E16 committed through O-APPEND appended/absorbed. | Records judgment_committed; the owning O-JUDGE reaches judgment_committed. | A successful receipt-bearing or selected-proof judgment claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.3 — consumed_pending_commit [proposed] → judgment_committed [proposed] | The named E9 + E16 committed through O-APPEND appended/absorbed. | Records judgment_committed; the owning O-JUDGE reaches judgment_committed. | A successful receipt-bearing or selected-proof judgment claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.4.7.4 — claimed → judgment_committed [proposed] under SACL-only | The named E9 + E16 committed through O-APPEND appended/absorbed. | Records judgment_committed; the owning O-JUDGE reaches judgment_committed. | A successful receipt-bearing or selected-proof judgment claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.5.4 — Replacement blocked by judgment_committed [proposed] | The named E9 + E16 committed through O-APPEND appended/absorbed. | This state blocks replacement. | A successful receipt-bearing or selected-proof judgment claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | The named E9 + E16 committed through O-APPEND appended/absorbed. | The named E9/E16 commit advances the claim to judgment_committed. | A successful receipt-bearing or selected-proof judgment claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.5.4 — Replacement blocked by judgment_committed [proposed] | The prior scope claim is judgment_committed. | The stated prior claim retains the scope. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.4 — Claim state released
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state released rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A no-receipt released claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Release a pending owner or any receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without either durable non-success or positive no-receipt proof, release is prohibited. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Requires both no durable_receipt_ref on the claim and no verified bai_token_consumed receipt bound to it in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: No durable_receipt_ref and no verified bai_token_consumed receipt bound to this claim in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Both independent no-receipt checks must establish positive proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.5 — claimed → released | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.5.1 — No-receipt replacement admission | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | An owning pending operation cannot release its claim. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.4.7 — Pre-receipt crash rule | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | Release is allowed only after durable non-success and positive no-receipt proof. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.4.8 — In-process receipt-write failure | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | Release is allowed only after durable non-success and positive no-receipt proof. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.7 — Pre-receipt crash rule | Crash after claim, after validation, or during/immediately after in-memory consumption, with no valid durable receipt. | Release requires durable non-success and positive proof that no valid durable receipt exists. | Failed authorization and an eligible no-receipt release; a later attempt needs a new flow, token, O-JUDGE and linked new claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.4.8 — In-process receipt-write failure | Receipt write fails or cannot be verified in the same process, including possible in-memory consumption. | The release rule requires durable non-success and positive no-receipt proof. | No reused uncertain token. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.4.4.1 — Positive no-receipt proof | The claim’s receipt reference and BAI security-audit history. | Both no-receipt checks hold, and the owning O-JUDGE already has a durable applicable non-success terminal. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.4.4.1 — Positive no-receipt proof

### C-GOLD.1.7.4.4.1 — Positive no-receipt proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Positive no-receipt proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The claim’s receipt reference and BAI security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Requires both no durable_receipt_ref on the claim and no verified bai_token_consumed receipt bound to it in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Positive proof supporting no-receipt release/admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat a missing claim reference alone as sufficient or replace a valid consumed receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Absent positive proof blocks release and replacement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.4.4.1.1 — No claim receipt reference: No durable_receipt_ref exists on this claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt: No verified bai_token_consumed receipt bound to this claim exists in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Both no-receipt checks hold, and the owning O-JUDGE already has a durable applicable non-success terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.4 — Claim state released | The claim’s receipt reference and BAI security-audit history. | Requires both no durable_receipt_ref on the claim and no verified bai_token_consumed receipt bound to it in security-audit history. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.4.1.1 — No claim receipt reference | The claim’s receipt reference and BAI security-audit history. | Both checks and the durable non-success terminal are required. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt | The claim’s receipt reference and BAI security-audit history. | Both checks and the durable non-success terminal are required. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.4.4 — Claim state released | The claim’s receipt reference and BAI security-audit history. | Both independent no-receipt checks must establish positive proof. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.5.1 — No-receipt replacement admission | The claim’s receipt reference and BAI security-audit history. | Positive proof is required again at new admission. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | The claim’s receipt reference and BAI security-audit history. | Positive no-receipt proof is required before release or new admission. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption) | The claim’s receipt reference and BAI security-audit history. | Positive no-receipt proof is required before release or new admission. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim | The claim’s receipt reference and BAI security-audit history. | Positive no-receipt proof is required before release or new admission. | Positive proof supporting no-receipt release/admission. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.7.4.4 — Claim state released | An applicable durable O-JUDGE non-success terminal plus positive no-receipt proof. | No durable_receipt_ref and no verified bai_token_consumed receipt bound to this claim in security-audit history. | A no-receipt released claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.7.5.1 — No-receipt replacement admission | A prior released/superseded claim whose O-JUDGE reached judgment_authorization_failed or judgment_claim_lost. | Prior no-receipt release/supersession plus positive no-receipt proof. | A new deliberate authorization flow with preserved prior claim history. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.4.4.1.1 — No claim receipt reference; C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt

### C-GOLD.1.7.4.4.1.1 — No claim receipt reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The No claim receipt reference rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Claim and security-audit receipt lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — No durable_receipt_ref exists on this claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One required no-receipt proof condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Use only the other check to authorize release. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the condition is not established, release/replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.8 — durable_receipt_ref [proposed]: No durable_receipt_ref exists on this claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Both checks and the durable non-success terminal are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.4.1 — Positive no-receipt proof | Claim and security-audit receipt lookup. | No durable_receipt_ref exists on this claim. | One required no-receipt proof condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The No verified bound security-audit receipt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Claim and security-audit receipt lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — No verified bai_token_consumed receipt bound to this claim exists in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One required no-receipt proof condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Use only the other check to authorize release. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — If the condition is not established, release/replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-BAI — Biometric Authorization Interface (§25.6): No verified bai_token_consumed receipt bound to this claim exists in security-audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Both checks and the durable non-success terminal are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.4.1 — Positive no-receipt proof | Claim and security-audit receipt lookup. | No verified bai_token_consumed receipt bound to this claim exists in security-audit history. | One required no-receipt proof condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.5 — Claim state superseded
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state superseded rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A released no-receipt claim replaced by a new linked claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Records superseded and superseded_by_claim_ref without altering prior records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A linked prior no-receipt claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Supersede a receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked unless no-receipt release and positive no-receipt proof hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.5.1 — No-receipt replacement admission: The prior claim is released and a replacement is admitted under the replacement rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Records superseded and superseded_by_claim_ref without altering prior records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | A released no-receipt claim replaced by a new linked claim. | Records superseded and superseded_by_claim_ref without altering prior records. | A linked prior no-receipt claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.6 — released → superseded | A released no-receipt claim replaced by a new linked claim. | Records superseded and superseded_by_claim_ref without altering prior records. | A linked prior no-receipt claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim state closed_after_breach rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A receipt-bearing, non-replaceable breach closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reapply the receipt, admit a replacement claim, consume another token or extend the chain absent an accepted resolution policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope stays blocked; no accepted resolution policy exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.11 — Head breach after a durable receipt: A receipt-bearing head-integrity breach is recorded. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.11 — Head breach after a durable receipt: Only a recorded judgment-head integrity breach ends a receipt-bearing claim this way. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.7.7 — consumed_pending_commit [proposed] → closed_after_breach [proposed] | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.5.5 — Replacement blocked by closed_after_breach [proposed] | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | This state blocks replacement. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.8.2 — Pending after authority consumption | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | Only a recorded breach permits the other receipt-bearing closure. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.4.11 — Head breach after a durable receipt | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | Preserves the consumed receipt in the non-replaceable breach closure. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.5.5 — Replacement blocked by closed_after_breach [proposed] | The prior scope claim is closed_after_breach. | The stated prior claim retains the scope. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7 — Append-only claim transitions
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The source-defined state transitions and SACL-only successful completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Current claim state and its transition evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends the linked state change when its exact gate holds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved predecessor state plus a new canonical state record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite a state record, release a pending operation or manufacture an authorization grant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An unmet transition gate prevents that transition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.1 — Admit → claimed: Writes claimed before token access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.2 — claimed → consumed_pending_commit [proposed]: Appends consumed_pending_commit and activates its receipt-bearing fence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.3 — consumed_pending_commit [proposed] → judgment_committed [proposed]: Appends judgment_committed; O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.4 — claimed → judgment_committed [proposed] under SACL-only: Appends successful claim state after E9 + E16 commit; no BAI consumed_pending_commit is invented. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.5 — claimed → released: Appends linked released state after the owner’s terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.6 — released → superseded: Appends superseded and the explicit successor claim link. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.4.7.7 — consumed_pending_commit [proposed] → closed_after_breach [proposed]: Appends closed_after_breach linked to the contradiction, preserving the receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Pending claims remain owned; receipt-bearing claims are never released or replaced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the linked state change when its exact gate holds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | Current claim state and its transition evidence. | Appends the linked state change when its exact gate holds. | Preserved predecessor state plus a new canonical state record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.4.7.1 — Admit → claimed; C-GOLD.1.7.4.7.2 — claimed → consumed_pending_commit [proposed]; C-GOLD.1.7.4.7.3 — consumed_pending_commit [proposed] → judgment_committed [proposed]; C-GOLD.1.7.4.7.4 — claimed → judgment_committed [proposed] under SACL-only; C-GOLD.1.7.4.7.5 — claimed → released; C-GOLD.1.7.4.7.6 — released → superseded; C-GOLD.1.7.4.7.7 — consumed_pending_commit [proposed] → closed_after_breach [proposed]

### C-GOLD.1.7.4.7.1 — Admit → claimed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Admit → claimed step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A winning admitted O-JUDGE claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Writes claimed before token access. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — claimed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Touch a token before the claim or treat claimed as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A second token for the scope is never consumed; return the existing reference or fail closed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.1 — Claim state claimed: Writes claimed before touching any token; grants no authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | A winning admitted O-JUDGE claim. | Writes claimed before token access. | claimed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.2 — claimed → consumed_pending_commit [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The claimed → consumed_pending_commit step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A durable consumed receipt bound to the winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends consumed_pending_commit and activates its receipt-bearing fence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — consumed_pending_commit [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Let another O-JUDGE consume, win a claim or commit a competing successor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A competitor is refused before consumption; only forward completion or closed_after_breach can end this receipt-bearing pending state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | A durable consumed receipt bound to the winning claim. | Appends consumed_pending_commit and activates its receipt-bearing fence. | consumed_pending_commit | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.3 — consumed_pending_commit [proposed] → judgment_committed [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The consumed_pending_commit → judgment_committed step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact named E9 + E16 appended/absorbed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends judgment_committed; O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — judgment_committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement claim or consume another token for this scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Competing claim/token admission is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: Records judgment_committed; the owning O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | The exact named E9 + E16 appended/absorbed. | Appends judgment_committed; O-JUDGE reaches judgment_committed. | judgment_committed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.4 — claimed → judgment_committed [proposed] under SACL-only
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The claimed → judgment_committed under SACL-only step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — SACL-only E9 + E16 commit with fresh required proof and no BAI stage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends successful claim state after E9 + E16 commit; no BAI consumed_pending_commit is invented. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — judgment_committed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement claim or consume another token for this scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Competing claim/token admission is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: Records judgment_committed; the owning O-JUDGE reaches judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | SACL-only E9 + E16 commit with fresh required proof and no BAI stage. | Appends successful claim state after E9 + E16 commit; no BAI consumed_pending_commit is invented. | judgment_committed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.5 — claimed → released
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The claimed → released step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Applicable durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends linked released state after the owner’s terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — released [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Release a pending owner or any receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without either durable non-success or positive no-receipt proof, release is prohibited. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Appends released only after judgment_authorization_failed or judgment_claim_lost is durable and no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | Applicable durable non-success and positive no-receipt proof. | Appends linked released state after the owner’s terminal. | released | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.6 — released → superseded
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The released → superseded step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A new linked replacement admitted with positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends superseded and the explicit successor claim link. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — superseded [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Supersede a receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked unless no-receipt release and positive no-receipt proof hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.5 — Claim state superseded: Records superseded and superseded_by_claim_ref without altering prior records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | A new linked replacement admitted with positive no-receipt proof. | Appends superseded and the explicit successor claim link. | superseded | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.4.7.7 — consumed_pending_commit [proposed] → closed_after_breach [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The consumed_pending_commit → closed_after_breach step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Recorded head breach against a fenced receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Appends closed_after_breach linked to the contradiction, preserving the receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — closed_after_breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reapply the receipt, admit a replacement claim, consume another token or extend the chain absent an accepted resolution policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope stays blocked; no accepted resolution policy exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: Appends closed_after_breach linked to the contradiction; preserves its receipt and marks the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Appends the stated canonical claim transition and preserves previous records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | Recorded head breach against a fenced receipt-bearing claim. | Appends closed_after_breach linked to the contradiction, preserving the receipt. | closed_after_breach | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5 — Claim fence and new-judgment admission
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim fence and new-judgment admission rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The existing claim and its operation/receipt status for one scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Admits a new deliberate O-JUDGE only when no claim owns the scope, or the prior claim is released/superseded with positive proof of no valid receipt and a durable non-success owner terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One permitted owner or a blocked competing judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Replace claimed, consumed_pending_commit, judgment_committed or closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A pending claim retains ownership; any receipt-bearing claim remains non-replaceable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.5.1 — No-receipt replacement admission: Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5.2 — Replacement blocked by claimed: Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5.3 — Replacement blocked by consumed_pending_commit [proposed]: Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5.4 — Replacement blocked by judgment_committed [proposed]: Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5.5 — Replacement blocked by closed_after_breach [proposed]: Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.5.6 — Only the winning attached token: Consumes only the token attached to the winning claim; a second token returns the existing reference or fails closed without consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5.1 — No-receipt replacement admission: New admission after a prior claim requires no-receipt release/supersession and positive proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Admits a new deliberate O-JUDGE only when no claim owns the scope, or the prior claim is released/superseded with positive proof of no valid receipt and a durable non-success owner terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | The existing claim and its operation/receipt status for one scope. | Admits a new deliberate O-JUDGE only when no claim owns the scope, or the prior claim is released/superseded with positive proof of no valid receipt and a durable non-success owner terminal. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.10.5 — INV-27 protected constraint | The existing claim and its operation/receipt status for one scope. | The defining rule supplies this invariant’s exact condition and outcome. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.4 — Claim state and transition rules | The existing claim and its operation/receipt status for one scope. | Pending claims remain owned; receipt-bearing claims are never released or replaced. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.4.7 — Append-only claim transitions | The existing claim and its operation/receipt status for one scope. | Pending claims remain owned; receipt-bearing claims are never released or replaced. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.8 — Two protected pending situations | The existing claim and its operation/receipt status for one scope. | Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | The existing claim and its operation/receipt status for one scope. | Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The existing claim and its operation/receipt status for one scope. | Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.3 — One-winner judgment-authorization scope | judgment_chain_key and expected_previous_judgment_head, plus the scope reference where NHD-B16EEB-D16 defines a wider scope. | An existing owning claim blocks a competitor. | Exactly one concurrent winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.5.1 — No-receipt replacement admission; C-GOLD.1.7.5.2 — Replacement blocked by claimed; C-GOLD.1.7.5.3 — Replacement blocked by consumed_pending_commit [proposed]; C-GOLD.1.7.5.4 — Replacement blocked by judgment_committed [proposed]; C-GOLD.1.7.5.5 — Replacement blocked by closed_after_breach [proposed]; C-GOLD.1.7.5.6 — Only the winning attached token

### C-GOLD.1.7.5.1 — No-receipt replacement admission
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The No-receipt replacement admission rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A prior released/superseded claim whose O-JUDGE reached judgment_authorization_failed or judgment_claim_lost. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — A new deliberate authorization flow with preserved prior claim history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Replace an active or receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing proof or any prohibited prior state refuses admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Prior no-receipt release/supersession plus positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Positive proof is required again at new admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: An owning pending operation cannot release its claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | A prior released/superseded claim whose O-JUDGE reached judgment_authorization_failed or judgment_claim_lost. | Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. | A new deliberate authorization flow with preserved prior claim history. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim | A prior released/superseded claim whose O-JUDGE reached judgment_authorization_failed or judgment_claim_lost. | Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. | A new deliberate authorization flow with preserved prior claim history. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.4.5 — Claim state superseded | A released no-receipt claim replaced by a new linked claim. | The prior claim is released and a replacement is admitted under the replacement rule. | A linked prior no-receipt claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | The existing claim and its operation/receipt status for one scope. | New admission after a prior claim requires no-receipt release/supersession and positive proof. | One permitted owner or a blocked competing judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5.2 — Replacement blocked by claimed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Replacement blocked by claimed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The prior scope claim is claimed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Existing ownership or non-replaceable closure preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement or consume a competing token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.1 — Claim state claimed: The stated prior claim retains the scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.1 — Claim state claimed: This state blocks replacement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | The prior scope claim is claimed. | Refuses admission of a new competing claim. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5.3 — Replacement blocked by consumed_pending_commit [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Replacement blocked by consumed_pending_commit rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The prior scope claim is consumed_pending_commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Existing ownership or non-replaceable closure preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement or consume a competing token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: The stated prior claim retains the scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: This state blocks replacement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | The prior scope claim is consumed_pending_commit. | Refuses admission of a new competing claim. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5.4 — Replacement blocked by judgment_committed [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Replacement blocked by judgment_committed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The prior scope claim is judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Existing ownership or non-replaceable closure preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement or consume a competing token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: The stated prior claim retains the scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: This state blocks replacement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | The prior scope claim is judgment_committed. | Refuses admission of a new competing claim. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5.5 — Replacement blocked by closed_after_breach [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Replacement blocked by closed_after_breach rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The prior scope claim is closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refuses admission of a new competing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Existing ownership or non-replaceable closure preserved. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Admit a replacement or consume a competing token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replacement is blocked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: The stated prior claim retains the scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: This state blocks replacement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | The prior scope claim is closed_after_breach. | Refuses admission of a new competing claim. | Existing ownership or non-replaceable closure preserved. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.5.6 — Only the winning attached token
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Only the winning attached token rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A token presented for an already claimed or committed scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Consumes only the token attached to the winning claim; a second token returns the existing reference or fails closed without consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — No second consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume a competing token for the same scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The second token is untouched. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.7 — attached_token_ref [proposed]: The token matches the winning claim’s attached_token_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.1.7 — attached_token_ref [proposed]: Only this attached token may be consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Consumes only the token attached to the winning claim; a second token returns the existing reference or fails closed without consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.5 — Claim fence and new-judgment admission | A token presented for an already claimed or committed scope. | Consumes only the token attached to the winning claim; a second token returns the existing reference or fails closed without consumption. | No second consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.6 — Contradictory claim and receipt evidence
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Contradictory claim and receipt evidence rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Marks the scope and its chain judgment_indeterminate; preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Indeterminate protected-judgment scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Choose a winner from contradictory durable evidence or discard either record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No usable judgment from contradictory claim/receipt evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.6.1 — Two winning claims: Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.6.2 — Receipt names absent claim: Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.6.3 — Receipt mismatches claim: Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.6.4 — Two receipts for one claim: Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The affected judgment chain becomes judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | Marks the scope and its chain judgment_indeterminate; preserves all records. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.6.1 — Two winning claims | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | The contradiction rule governs this evidence. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.6.2 — Receipt names absent claim | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | The contradiction rule governs this evidence. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.6.3 — Receipt mismatches claim | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | The contradiction rule governs this evidence. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.6.4 — Two receipts for one claim | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | The contradiction rule governs this evidence. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.6.1 — Two winning claims; C-GOLD.1.7.6.2 — Receipt names absent claim; C-GOLD.1.7.6.3 — Receipt mismatches claim; C-GOLD.1.7.6.4 — Two receipts for one claim

### C-GOLD.1.7.6.1 — Two winning claims
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Two winning claims rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Two winning claims for one scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Discard a conflicting record or treat the evidence as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain are judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.6 — Contradictory claim and receipt evidence: The contradiction rule governs this evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The scope and chain become judgment_indeterminate; preserve all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | Two winning claims for one scope. | Marks the scope and chain judgment_indeterminate and preserves all records. | Preserved contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.6.2 — Receipt names absent claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Receipt names absent claim rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A receipt names a claim that does not exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Discard a conflicting record or treat the evidence as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain are judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.6 — Contradictory claim and receipt evidence: The contradiction rule governs this evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The scope and chain become judgment_indeterminate; preserve all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | A receipt names a claim that does not exist. | Marks the scope and chain judgment_indeterminate and preserves all records. | Preserved contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.6.3 — Receipt mismatches claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Receipt mismatches claim rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A receipt names a claim that does not match it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Discard a conflicting record or treat the evidence as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain are judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.6 — Contradictory claim and receipt evidence: The contradiction rule governs this evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The scope and chain become judgment_indeterminate; preserve all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | A receipt names a claim that does not match it. | Marks the scope and chain judgment_indeterminate and preserves all records. | Preserved contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.6.4 — Two receipts for one claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Two receipts for one claim rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Two receipts exist for the same claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Marks the scope and chain judgment_indeterminate and preserves all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Discard a conflicting record or treat the evidence as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain are judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.6 — Contradictory claim and receipt evidence: The contradiction rule governs this evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The scope and chain become judgment_indeterminate; preserve all records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | Two receipts exist for the same claim. | Marks the scope and chain judgment_indeterminate and preserves all records. | Preserved contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7 — Protected-judgment log ownership
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Protected-judgment log ownership rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps claim transitions as canonical child state records; O-JUDGE logs its one terminal, naming the claim and final state and the O-APPEND that committed/refused E9. Each O-APPEND logs its own terminal; B9 logs only its own retry requests; BAI alone writes its security audit events. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One operation-owned log per real terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Duplicate another owner’s log, turn a claim transition into an operational log or create/backfill/copy BAI events. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits for the operation’s own terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.7.1 — O-JUDGE [proposed] terminal log: Writes its matching eval_judgment_* log once, naming its claim, resulting closure state and O-APPEND that committed/refused E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.2 — Claim child state records: Records canonical child state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.3 — BAI-owned security audit: References only events actually written by BAI during its live operations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.4 — O-APPEND [proposed] terminal log: Writes exactly one matching eval_append_appended, eval_append_absorbed, eval_append_lost_race_technical or eval_append_refused_domain_precondition log for that ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.5 — B9 retry-request logs: Logs only its own retry requests and references O-APPEND identities. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.6 — Authorization-failure reason: pre-receipt crash: Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.7 — Authorization-failure reason: failed/unverifiable receipt write: Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.8 — Authorization-failure reason: refusal before consumption: Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.9 — Authorization-failure reason: head breach after receipt: Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.7.10 — Committed judgment missing its O-JUDGE [proposed] log: Appends the missing O-JUDGE log once, then acknowledges. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Keeps claim transitions as canonical child state records; O-JUDGE logs its one terminal, naming the claim and final state and the O-APPEND that committed/refused E9. Each O-APPEND logs its own terminal; B9 logs only its own retry requests; BAI alone writes its security audit events. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.7.1 — O-JUDGE [proposed] terminal log | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Every real operation owns only its own terminal log. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.7.2 — Claim child state records | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Every real operation owns only its own terminal log. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.7.3 — BAI-owned security audit | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Every real operation owns only its own terminal log. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.7.4 — O-APPEND [proposed] terminal log | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Every real operation owns only its own terminal log. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.7.5 — B9 retry-request logs | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Every real operation owns only its own terminal log. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.10.3 — INV-25 protected constraint | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | The defining rule supplies this invariant’s exact condition and outcome. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Each real operation owns exactly one terminal/log; claim transitions are canonical state only. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Each real operation owns exactly one terminal/log; claim transitions are canonical state only. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | O-JUDGE, its claim transitions, O-APPEND, BAI audit events and B9 retry-request operations. | Each real operation owns exactly one terminal/log; claim transitions are canonical state only. | One operation-owned log per real terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.7.1 — O-JUDGE [proposed] terminal log; C-GOLD.1.7.7.2 — Claim child state records; C-GOLD.1.7.7.3 — BAI-owned security audit; C-GOLD.1.7.7.4 — O-APPEND [proposed] terminal log; C-GOLD.1.7.7.5 — B9 retry-request logs; C-GOLD.1.7.7.6 — Authorization-failure reason: pre-receipt crash; C-GOLD.1.7.7.7 — Authorization-failure reason: failed/unverifiable receipt write; C-GOLD.1.7.7.8 — Authorization-failure reason: refusal before consumption; C-GOLD.1.7.7.9 — Authorization-failure reason: head breach after receipt; C-GOLD.1.7.7.10 — Committed judgment missing its O-JUDGE [proposed] log

### C-GOLD.1.7.7.1 — O-JUDGE [proposed] terminal log
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-JUDGE terminal log rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — One terminal of O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Writes its matching eval_judgment_* log once, naming its claim, resulting closure state and O-APPEND that committed/refused E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Uses the exact terminal-matched log: eval_judgment_committed, eval_judgment_absorbed, eval_judgment_refused_stale_head, eval_judgment_refused_authority, eval_judgment_refused_mode_mismatch, eval_judgment_refused_output_invalid, eval_judgment_claim_lost or eval_judgment_authorization_failed; one log for this O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Writes its matching eval_judgment_* log once, naming its claim, resulting closure state and O-APPEND that committed/refused E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Write a second O-JUDGE log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits until this operation’s terminal and its one matching log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Every real operation owns only its own terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE [proposed]: Completes O-JUDGE’s own terminal/log boundary before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | One terminal of O-JUDGE. | Writes its matching eval_judgment_* log once, naming its claim, resulting closure state and O-APPEND that committed/refused E9. | Writes its matching eval_judgment_* log once, naming its claim, resulting closure state and O-APPEND that committed/refused E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.2 — Claim child state records
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Claim child state records rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — An append-only claim transition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records canonical child state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Records canonical child state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Count a claim transition as an operational log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Every real operation owns only its own terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | An append-only claim transition. | Records canonical child state only. | Records canonical child state only. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.3 — BAI-owned security audit
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The BAI-owned security audit rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — bai_token_consumed, any live bai_token_consume_blocked and BAI audit history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — References only events actually written by BAI during its live operations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — References only events actually written by BAI during its live operations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Create, backfill, duplicate or copy a BAI event in bridge/recovery records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Every real operation owns only its own terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | bai_token_consumed, any live bai_token_consume_blocked and BAI audit history. | References only events actually written by BAI during its live operations. | References only events actually written by BAI during its live operations. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.4 — O-APPEND [proposed] terminal log
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The O-APPEND terminal log rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — A real O-APPEND terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Writes exactly one matching eval_append_appended, eval_append_absorbed, eval_append_lost_race_technical or eval_append_refused_domain_precondition log for that ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Writes exactly one matching eval_append_appended, eval_append_absorbed, eval_append_lost_race_technical or eval_append_refused_domain_precondition log for that ID. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Reuse an O-APPEND ID for a new terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits until this operation’s terminal and its one matching log exist. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Every real operation owns only its own terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | A real O-APPEND terminal. | Writes exactly one matching eval_append_appended, eval_append_absorbed, eval_append_lost_race_technical or eval_append_refused_domain_precondition log for that ID. | Writes exactly one matching eval_append_appended, eval_append_absorbed, eval_append_lost_race_technical or eval_append_refused_domain_precondition log for that ID. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.5 — B9 retry-request logs
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The B9 retry-request logs rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — B9 R0–R4 retry-request operations. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Logs only its own retry requests and references O-APPEND identities. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Logs only its own retry requests and references O-APPEND identities. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Re-log an O-APPEND terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Every real operation owns only its own terminal log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | B9 R0–R4 retry-request operations. | Logs only its own retry requests and references O-APPEND identities. | Logs only its own retry requests and references O-APPEND identities. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.6 — Authorization-failure reason: pre-receipt crash
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorization-failure reason: pre-receipt crash rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ends judgment_authorization_failed because of pre-receipt crash. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One honest authorization-failure log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent another terminal or log for that O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The non-success terminal is logged before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed: This log belongs only to O-JUDGE’s durable judgment_authorization_failed terminal and carries its exact reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | O-JUDGE ends judgment_authorization_failed because of pre-receipt crash. | Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. | One honest authorization-failure log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.7 — Authorization-failure reason: failed/unverifiable receipt write
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorization-failure reason: failed/unverifiable receipt write rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ends judgment_authorization_failed because of failed/unverifiable receipt write. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One honest authorization-failure log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent another terminal or log for that O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The non-success terminal is logged before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed: This log belongs only to O-JUDGE’s durable judgment_authorization_failed terminal and carries its exact reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | O-JUDGE ends judgment_authorization_failed because of failed/unverifiable receipt write. | Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. | One honest authorization-failure log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.8 — Authorization-failure reason: refusal before consumption
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorization-failure reason: refusal before consumption rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ends judgment_authorization_failed because of refusal before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One honest authorization-failure log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent another terminal or log for that O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The non-success terminal is logged before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed: This log belongs only to O-JUDGE’s durable judgment_authorization_failed terminal and carries its exact reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | O-JUDGE ends judgment_authorization_failed because of refusal before consumption. | Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. | One honest authorization-failure log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.9 — Authorization-failure reason: head breach after receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorization-failure reason: head breach after receipt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE ends judgment_authorization_failed because of head breach after receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One honest authorization-failure log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Invent another terminal or log for that O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The non-success terminal is logged before acknowledgement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed: This log belongs only to O-JUDGE’s durable judgment_authorization_failed terminal and carries its exact reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | O-JUDGE ends judgment_authorization_failed because of head breach after receipt. | Records the exact reason in eval_judgment_authorization_failed once, with claim and resulting closure state. | One honest authorization-failure log. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.7.10 — Committed judgment missing its O-JUDGE [proposed] log
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Committed judgment missing its O-JUDGE log rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — E9 + E16 committed, but O-JUDGE’s log is absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Appends the missing O-JUDGE log once, then acknowledges. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — One completed terminal/log pair. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Recommit E9 or duplicate a log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits for the missing log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The E9/E16 append already committed and lookup finds the O-JUDGE log missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.7 — Protected-judgment log ownership | E9 + E16 committed, but O-JUDGE’s log is absent. | Appends the missing O-JUDGE log once, then acknowledges. | One completed terminal/log pair. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.16 — CR-29 — Crash between O-JUDGE [proposed]'s O-APPEND [proposed] commit and O-JUDGE [proposed]'s log | E9 + E16 committed, but O-JUDGE’s log is absent. | Appends the missing O-JUDGE log once, then acknowledges. | One completed terminal/log pair. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.8 — Two protected pending situations
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The distinct pending states before and after durable authorization consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — B9 append exhaustion or a durable receipt awaiting E9 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the pending O-JUDGE and its scope fence; follows only the permitted continuation for its proof stage. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Honest pending ownership with no invented terminal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Make an operation pending and durably non-successful simultaneously. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A pending operation has no released claim; incomplete evidence blocks passing results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.8.1 — Pending before authority consumption: Keeps the same O-JUDGE pending with no terminal and its claim claimed/owned; continuation uses a new B9 episode under consumed real-change with unchanged canonical inputs and a new O-APPEND under the same O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.8.2 — Pending after authority consumption: Keeps the scope fenced; forward-completes exactly the named E9 through B9-admitted O-APPENDs if needed, or records a head breach and closes closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | B9 append exhaustion or a durable receipt awaiting E9 commit. | Keeps the pending O-JUDGE and its scope fence; follows only the permitted continuation for its proof stage. | Honest pending ownership with no invented terminal. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.8.1 — Pending before authority consumption; C-GOLD.1.7.8.2 — Pending after authority consumption

### C-GOLD.1.7.8.1 — Pending before authority consumption
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Pending before authority consumption rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — Ordinary O-APPEND exhaustion before authority consumption, in practice SACL-only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the same O-JUDGE pending with no terminal and its claim claimed/owned; continuation uses a new B9 episode under consumed real-change with unchanged canonical inputs and a new O-APPEND under the same O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Owned pending claim; no current output head, so incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Release the claim, admit a competing O-JUDGE, invent an exhausted domain terminal or hide a retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The output remains without a current head and incomplete; the pending run cannot close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.10.10 — Real-change continuation: A consumed real-change record authorizes the new B9 episode; the owner remains the same O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.1 — Claim state claimed: The pending owner keeps this state and its scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.13 — Requesting operation after append exhaustion: B9 exhaustion leaves the requesting domain operation honestly pending. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Keeps the same O-JUDGE pending with no terminal and its claim claimed/owned; continuation uses a new B9 episode under consumed real-change with unchanged canonical inputs and a new O-APPEND under the same O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.8 — Two protected pending situations | Ordinary O-APPEND exhaustion before authority consumption, in practice SACL-only. | Keeps the same O-JUDGE pending with no terminal and its claim claimed/owned; continuation uses a new B9 episode under consumed real-change with unchanged canonical inputs and a new O-APPEND under the same O-JUDGE. | Owned pending claim; no current output head, so incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.10.4 — INV-26 protected constraint | Ordinary O-APPEND exhaustion before authority consumption, in practice SACL-only. | The defining rule supplies this invariant’s exact condition and outcome. | Owned pending claim; no current output head, so incomplete. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.8.2 — Pending after authority consumption
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Pending after authority consumption rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Takes in: ACCEPTED — consumed_pending_commit with durable receipt and no E9 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Does: ACCEPTED — Keeps the scope fenced; forward-completes exactly the named E9 through B9-admitted O-APPENDs if needed, or records a head breach and closes closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gives out: ACCEPTED — Exact forward completion or non-replaceable breach closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Must never: ACCEPTED — Lose, duplicate, redirect or apply authorization to a different judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Every competing consume/successor is blocked; a breach stays non-replaceable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: The durable receipt stays bound to its winning claim and exact E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: The receipt-bearing fence remains active. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Recovery may complete only this exact named E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: Only a recorded breach permits the other receipt-bearing closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Keeps the scope fenced; forward-completes exactly the named E9 through B9-admitted O-APPENDs if needed, or records a head breach and closes closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.8 — Two protected pending situations | consumed_pending_commit with durable receipt and no E9 commit. | Keeps the scope fenced; forward-completes exactly the named E9 through B9-admitted O-APPENDs if needed, or records a head breach and closes closed_after_breach. | Exact forward completion or non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9 — Protected judgment lookup-first recovery
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The remaining judgment-specific lookup-first recovery cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Takes in: ACCEPTED — Durable claim, receipt, E9/E16 and operation/log evidence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Does: ACCEPTED — Looks up actual durable state and applies only the source-defined missing work once. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Gives out: ACCEPTED — A preserved state or exact missing commit/log; no invented authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Must never: ACCEPTED — Retry a stale semantic judgment mechanically, reconstruct tokens or backfill BAI history. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unknown/contradictory evidence remains indeterminate; unmatched receipts commit nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently: One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted: absorbed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor): Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content: Contradiction; as CR-26 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time: That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption): Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit: Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token: Refused (judgment_refused_authority), non-retryable, logged [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes: Committed judgment unaffected [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption): Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.11 — CR-36 — Two concurrent claims for one scope: One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.12 — CR-37 — Competing O-JUDGE [proposed] while the scope is consumed_pending_commit [proposed]: Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion: The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion: Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim: Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.9.16 — CR-29 — Crash between O-JUDGE [proposed]'s O-APPEND [proposed] commit and O-JUDGE [proposed]'s log: Append O-JUDGE's missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Durable claim, receipt, E9/E16 and operation/log evidence. | Looks up actual durable state and applies only the source-defined missing work once. | A preserved state or exact missing commit/log; no invented authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently; C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted; C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor); C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content; C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time; C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption); C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit; C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token; C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes; C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption); C-GOLD.1.7.9.11 — CR-36 — Two concurrent claims for one scope; C-GOLD.1.7.9.12 — CR-37 — Competing O-JUDGE [proposed] while the scope is consumed_pending_commit [proposed]; C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion; C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion; C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim; C-GOLD.1.7.9.16 — CR-29 — Crash between O-JUDGE [proposed]'s O-APPEND [proposed] commit and O-JUDGE [proposed]'s log

### C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-24 — Two O-JUDGEs extend the same head concurrently step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Two O-JUDGEs extend the same head concurrently [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Extend a forked chain with no single head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A stale competing expected head is refused non-retryably. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — O-APPEND ends refused_domain_precondition and O-JUDGE ends judgment_refused_stale_head on a stale expected head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.3 — First and later judgment predecessor: The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Two O-JUDGEs extend the same head concurrently | One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head | One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-25 — Identical E9 re-submitted step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Identical E9 re-submitted [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — absorbed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — absorbed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Create a second judgment for identical key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different content under one E9 identity is an integrity contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.3.1 — Identical E9 absorption: Absorbs the identical committed E9 without adding another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: An identical committed E9 absorbs under CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): absorbed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Identical E9 re-submitted | absorbed | absorbed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-26 — Fork found (two committed successors of one predecessor) step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Fork found (two committed successors of one predecessor) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Choose by recency, extend the forked chain or use NHD-B16EEB-D10/D11 to resolve it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The chain stays indeterminate; no fork-resolution procedure is defined. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.5 — Judgment fork: Marks the chain judgment_indeterminate; marks the trial, run aggregate head and every downstream result indeterminate; preserves both judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Fork found (two committed successors of one predecessor) | Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) | Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-27 — E9 bytes do not match its identity, or same identity with different content step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — E9 bytes do not match its identity, or same identity with different content [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Contradiction; as CR-26 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — Contradiction; as CR-26 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Choose by recency or extend the contradictory chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory judgment evidence stays indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.6 — Judgment contradiction: Marks the chain judgment_indeterminate and all dependent trial/run/result state indeterminate; preserves conflicting records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): Contradiction; as CR-26 [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | E9 bytes do not match its identity, or same identity with different content | Contradiction; as CR-26 | Contradiction; as CR-26 | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Treat invalid proof as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No usable judgment until lookup verifies the proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.13 — Later invalid consumption proof: Makes an uncommitted judgment unavailable; if already committed, makes its chain judgment_indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.4 — Later discovery of invalid session proof: SACL proof invalid at judgment time is also indeterminate; ordinary later expiry is not. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time | That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reconstruct/resurrect/reuse the original token, consume it during recovery, or create/backfill any BAI event. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No receipt means no committed authorization; unverifiable evidence is resolved by lookup, never assumed absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.7 — Pre-receipt crash rule: After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Positive no-receipt proof is required before release or new admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) | Original token gone after restart (BAI in-memory only); no receipt → no authority; recovery never consumes with the original token and never backfills a BAI event; O-JUDGE → judgment_authorization_failed (one terminal, one log); claim → released (linked); a new O-JUDGE with a new token and new claim is required (§7.12 A item 7) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-32 — BAI option: crash after flushed receipt, before E9 commit step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — BAI option: crash after flushed receipt, before E9 commit [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume again, fabricate a judgment, lose/duplicate/redirect authorization or permit a competing successor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Orphaned receipt commits nothing; unreadable/contradictory proof is indeterminate until lookup; a head breach refuses stale E9 and closes the receipt-bearing claim after breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | BAI option: crash after flushed receipt, before E9 commit | Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits | Claim consumed_pending_commit (fenced); recovery verifies the receipt and forward-completes exactly the named E9 once via O-APPEND; no re-consumption; no fabrication; no competing O-JUDGE may consume or commit for that scope meanwhile; orphaned receipt (no matching claim) → nothing commits | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — BAI option: replay / reuse of a consumed, expired, or revoked token [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refused (judgment_refused_authority), non-retryable, logged [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Refused (judgment_refused_authority), non-retryable, logged [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reuse a prior consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — judgment_refused_authority; non-retryable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.6 — BAI replay and reuse refusal: Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Refused (judgment_refused_authority), non-retryable, logged [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | BAI option: replay / reuse of a consumed, expired, or revoked token | Refused (judgment_refused_authority), non-retryable, logged | Refused (judgment_refused_authority), non-retryable, logged | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-34 — SACL option: session later expires or closes step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — SACL option: session later expires or closes [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Committed judgment unaffected [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Committed judgment unaffected [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Retroactively erase a valid judgment because time passed or its session ended. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A later discovery of proof invalid at judgment time, unlike ordinary expiry, makes the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.3 — Ordinary later session expiry: Preserves judgment validity as a fact about its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The original judgment proof was fresh and valid at its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Committed judgment unaffected [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | SACL option: session later expires or closes | Committed judgment unaffected | Committed judgment unaffected | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption)
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption) step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — BAI option: receipt-write failure in-process (possible in-memory consumption) [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Retry that token or reconstruct BAI state from bridge records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Authorization fails; contradictory/unreadable receipt evidence cannot establish the positive no-receipt proof for release. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.8 — In-process receipt-write failure: Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Positive no-receipt proof is required before release or new admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | BAI option: receipt-write failure in-process (possible in-memory consumption) | Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records | Terminal for that token; never retried; O-JUDGE → judgment_authorization_failed; claim → released; new token + new O-JUDGE required; BAI state never reconstructed from bridge records | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.11 — CR-36 — Two concurrent claims for one scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-36 — Two concurrent claims for one scope step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Two concurrent claims for one scope [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume a losing claimant’s token or admit multiple owning claims for one scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A losing O-JUDGE ends judgment_claim_lost with one terminal and one log; its token is untouched. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: Admits at most one active-or-successful claim per scope: claimed, consumed_pending_commit or judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Two concurrent claims for one scope | One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed | One wins; the loser's O-JUDGE → judgment_claim_lost, its token untouched (never consumed); only the winner's attached token may be consumed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.12 — CR-37 — Competing O-JUDGE [proposed] while the scope is consumed_pending_commit [proposed]
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-37 — Competing O-JUDGE while the scope is consumed_pending_commit step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Competing O-JUDGE while the scope is consumed_pending_commit [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Let another O-JUDGE consume, win a claim or commit a competing successor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A competitor is refused before consumption; only forward completion or closed_after_breach can end this receipt-bearing pending state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: Records consumed_pending_commit and fences the scope until exact forward completion or a recorded head breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Competing O-JUDGE while the scope is consumed_pending_commit | Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach | Refused before any consumption (judgment_refused_stale_head or claim refused); the fence holds until forward completion or breach | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-38 — Unrelated ledger movement during forward completion step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Unrelated ledger movement during forward completion [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Re-establish or consume authorization again. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission no new O-APPEND proceeds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion: The losing O-APPEND ends lost_race_technical; a B9-admitted new O-APPEND uses a new operation ID and unchanged E9 key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.13 — O-APPEND [proposed]: The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Unrelated ledger movement during forward completion | The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established | The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Judgment head changed contrary to the fence (integrity breach) during forward completion [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reapply the receipt, admit a replacement claim, consume another token or extend the chain absent a future accepted resolution policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain remain blocked; no such resolution policy exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.11 — Head breach after a durable receipt: Does not force stale E9; records the contradiction, marks judgment_indeterminate and closes the claim closed_after_breach linked to that contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Judgment head changed contrary to the fence (integrity breach) during forward completion | Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy | Do not force the stale E9; record the contradiction; chain judgment_indeterminate; claim → closed_after_breach (receipt-bearing, non-replaceable, linked to the contradiction); receipt preserved, never re-applied; no replacement claim, no second token consumption, no chain extension absent an accepted resolution policy | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.15 — CR-40 — New deliberate O-JUDGE [proposed] after a prior claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-40 — New deliberate O-JUDGE after a prior claim step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — New deliberate O-JUDGE after a prior claim [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Replace an active or receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing proof or any prohibited prior state refuses admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.5.1 — No-receipt replacement admission: Rechecks positive no-receipt proof; admits a new claim linked by supersedes_claim_ref, a new O-JUDGE and a new token where the selected proof uses BAI. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4.1 — Positive no-receipt proof: Positive no-receipt proof is required before release or new admission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | New deliberate O-JUDGE after a prior claim | Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach | Admitted only when the prior claim is released/superseded and positive proof exists that no valid durable receipt is bound to it (prior O-JUDGE at judgment_authorization_failed or judgment_claim_lost); new claim links supersedes_claim_ref; new token; new O-JUDGE ID. Refused while the prior claim is claimed (pending owner), consumed_pending_commit, judgment_committed, or closed_after_breach | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.9.16 — CR-29 — Crash between O-JUDGE [proposed]'s O-APPEND [proposed] commit and O-JUDGE [proposed]'s log
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The CR-29 — Crash between O-JUDGE's O-APPEND commit and O-JUDGE's log step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Crash between O-JUDGE's O-APPEND commit and O-JUDGE's log [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Append O-JUDGE's missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Append O-JUDGE's missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Recommit E9 or duplicate a log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits for the missing log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7.10 — Committed judgment missing its O-JUDGE [proposed] log: Appends the missing O-JUDGE log once, then acknowledges. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE [proposed]: Append O-JUDGE's missing log; then acknowledge [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.9 — Protected judgment lookup-first recovery | Crash between O-JUDGE's O-APPEND commit and O-JUDGE's log | Append O-JUDGE's missing log; then acknowledge | Append O-JUDGE's missing log; then acknowledge | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.10 — Protected judgment invariants
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Protected judgment invariants rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — Judgment heads, proof binding, operation identities and claim ownership. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — Enforces INV-22, INV-23, INV-25, INV-26 and INV-27. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — No ambiguous head, unauthorized judgment, duplicate terminal or replaceable consumed claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Resolve a judgment fork by recency, count model authority or release a pending/receipt-bearing claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Violating judgment evidence is unusable; forks/contradictions remain indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.7.10.1 — INV-22 protected constraint: Each effectively completed output has at most one current judgment head; heads change only by CAS-3; a fork or contradiction makes the chain judgment_indeterminate; recency never decides. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.10.2 — INV-23 protected constraint: No E9 commits without a present, verifiable, authorized authority reference matching its E1 judgment mode; model assistance never counts; no Ness judgment before NHD-B16EEB-D16 is accepted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.10.3 — INV-25 protected constraint: Every operation ID — including every O-APPEND — has exactly one terminal and one log; a lost race yields a new O-APPEND with a new ID and the unchanged canonical key and content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.10.4 — INV-26 protected constraint: No operation is simultaneously pending and durably non-successful: a claim is released only after its O-JUDGE's durable non-success terminal; a pending O-JUDGE's claim stays owned and fenced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.7.10.5 — INV-27 protected constraint: A claim with a durable consumption receipt is never replaced by another claim or another consumed token for the same scope — judgment_committed or closed_after_breach are its only closures; released/superseded are no-receipt states only; a new claim is admitted only with positive proof that no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: Lookup and continuation preserve one-winner ownership and receipt-bearing non-replaceability. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | Judgment heads, proof binding, operation identities and claim ownership. | Enforces INV-22, INV-23, INV-25, INV-26 and INV-27. | No ambiguous head, unauthorized judgment, duplicate terminal or replaceable consumed claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.10 — Evaluation invariants | Frozen epochs and plans, all evidentiary runs, attempts and outputs, current judgments/aggregates, ledger heads, actual coverage, result identities and protected claims/receipts. | Gates this place: INV-22, INV-23 and INV-25–INV-27 retain one current head, matching authority, one terminal/log and non-replaceable consumed authorization. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] |

SUB-PARTS: C-GOLD.1.7.10.1 — INV-22 protected constraint; C-GOLD.1.7.10.2 — INV-23 protected constraint; C-GOLD.1.7.10.3 — INV-25 protected constraint; C-GOLD.1.7.10.4 — INV-26 protected constraint; C-GOLD.1.7.10.5 — INV-27 protected constraint

### C-GOLD.1.7.10.1 — INV-22 protected constraint
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The INV-22 protected constraint rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment/claim state governed by this invariant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — Each effectively completed output has at most one current judgment head; heads change only by CAS-3; a fork or contradiction makes the chain judgment_indeterminate; recency never decides. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — Each effectively completed output has at most one current judgment head; heads change only by CAS-3; a fork or contradiction makes the chain judgment_indeterminate; recency never decides. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite an old judgment, choose by recency or extend a forked chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Forks and contradictions make the trial, run aggregate head and all downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: The defining rule supplies this invariant’s exact condition and outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The judgment/claim state governed by this invariant. | Each effectively completed output has at most one current judgment head; heads change only by CAS-3; a fork or contradiction makes the chain judgment_indeterminate; recency never decides. | Each effectively completed output has at most one current judgment head; heads change only by CAS-3; a fork or contradiction makes the chain judgment_indeterminate; recency never decides. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.10.2 — INV-23 protected constraint
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The INV-23 protected constraint rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment/claim state governed by this invariant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — No E9 commits without a present, verifiable, authorized authority reference matching its E1 judgment mode; model assistance never counts; no Ness judgment before NHD-B16EEB-D16 is accepted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — No E9 commits without a present, verifiable, authorized authority reference matching its E1 judgment mode; model assistance never counts; no Ness judgment before NHD-B16EEB-D16 is accepted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Accept a bare annotator name or model-only authority; invent an authentication method. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Absent, unverifiable, mismatched or unauthorized proof refuses E9; an unjudged output is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The defining rule supplies this invariant’s exact condition and outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The judgment/claim state governed by this invariant. | No E9 commits without a present, verifiable, authorized authority reference matching its E1 judgment mode; model assistance never counts; no Ness judgment before NHD-B16EEB-D16 is accepted. | No E9 commits without a present, verifiable, authorized authority reference matching its E1 judgment mode; model assistance never counts; no Ness judgment before NHD-B16EEB-D16 is accepted. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.10.3 — INV-25 protected constraint
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The INV-25 protected constraint rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment/claim state governed by this invariant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — Every operation ID — including every O-APPEND — has exactly one terminal and one log; a lost race yields a new O-APPEND with a new ID and the unchanged canonical key and content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — Every operation ID — including every O-APPEND — has exactly one terminal and one log; a lost race yields a new O-APPEND with a new ID and the unchanged canonical key and content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Duplicate another owner’s log, turn a claim transition into an operational log or create/backfill/copy BAI events. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Acknowledgement waits for the operation’s own terminal and log. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: The defining rule supplies this invariant’s exact condition and outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The judgment/claim state governed by this invariant. | Every operation ID — including every O-APPEND — has exactly one terminal and one log; a lost race yields a new O-APPEND with a new ID and the unchanged canonical key and content. | Every operation ID — including every O-APPEND — has exactly one terminal and one log; a lost race yields a new O-APPEND with a new ID and the unchanged canonical key and content. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.10.4 — INV-26 protected constraint
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The INV-26 protected constraint rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment/claim state governed by this invariant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — No operation is simultaneously pending and durably non-successful: a claim is released only after its O-JUDGE's durable non-success terminal; a pending O-JUDGE's claim stays owned and fenced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — No operation is simultaneously pending and durably non-successful: a claim is released only after its O-JUDGE's durable non-success terminal; a pending O-JUDGE's claim stays owned and fenced. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Release the claim, admit a competing O-JUDGE, invent an exhausted domain terminal or hide a retry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The output remains without a current head and incomplete; the pending run cannot close. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.8.1 — Pending before authority consumption: The defining rule supplies this invariant’s exact condition and outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The judgment/claim state governed by this invariant. | No operation is simultaneously pending and durably non-successful: a claim is released only after its O-JUDGE's durable non-success terminal; a pending O-JUDGE's claim stays owned and fenced. | No operation is simultaneously pending and durably non-successful: a claim is released only after its O-JUDGE's durable non-success terminal; a pending O-JUDGE's claim stays owned and fenced. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.7.10.5 — INV-27 protected constraint
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The INV-27 protected constraint rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment/claim state governed by this invariant. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Does: ACCEPTED — A claim with a durable consumption receipt is never replaced by another claim or another consumed token for the same scope — judgment_committed or closed_after_breach are its only closures; released/superseded are no-receipt states only; a new claim is admitted only with positive proof that no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Gives out: ACCEPTED — A claim with a durable consumption receipt is never replaced by another claim or another consumed token for the same scope — judgment_committed or closed_after_breach are its only closures; released/superseded are no-receipt states only; a new claim is admitted only with positive proof that no valid receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB]
- Must never: ACCEPTED — Replace claimed, consumed_pending_commit, judgment_committed or closed_after_breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A pending claim retains ownership; any receipt-bearing claim remains non-replaceable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.5 — Claim fence and new-judgment admission: The defining rule supplies this invariant’s exact condition and outcome. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.7.10 — Protected judgment invariants | The judgment/claim state governed by this invariant. | A claim with a durable consumption receipt is never replaced by another claim or another consumed token for the same scope — judgment_committed or closed_after_breach are its only closures; released/superseded are no-receipt states only; a new claim is admitted only with positive proof that no valid receipt exists. | A claim with a durable consumption receipt is never replaced by another claim or another consumed token for the same scope — judgment_committed or closed_after_breach are its only closures; released/superseded are no-receipt states only; a new claim is admitted only with positive proof that no valid receipt exists. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.12.1 — Open judgment-fork and breach resolution | A `judgment_indeterminate` [proposed] chain, including a `closed_after_breach` [proposed] claim whose valid durable receipt remains preserved. | Gates this place: consumed authorization remains non-replaceable; release/supersession require positive no-receipt proof. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-h BEHAVIOR -->

## Continuation and reciprocal entries

Every entry below stays in this piece. The old endpoint is named exactly; no previous card is rewritten.

| Existing owner / endpoint | New counterpart | Relation | Behavior | Source |
|---|---|---|---|---|
| C-GOLD.1 — Promotion evaluation-evidence bridge | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | ACCEPTED — SUB-PARTS addition and Fed by continuation | Serializes one protected judgment scope without granting authority; preserves pending ownership and receipt-bearing non-replaceability. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND [proposed] | C-GOLD.1.7.2 — Claim ownership separation | ACCEPTED — reciprocal USED BY entry for Changes | O-APPEND owns only the E9 + E16 atomic commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.5.13 — Requesting operation after append exhaustion | C-GOLD.1.7.8.1 — Pending before authority consumption | ACCEPTED — reciprocal USED BY entry for Gated by | B9 exhaustion leaves the requesting domain operation honestly pending. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted | ACCEPTED — reciprocal USED BY entry for Gated by | An identical committed E9 absorbs under CAS-3. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.19 — Evaluation privacy and access | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — reciprocal USED BY entry for Gated by | Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.3.19 — Evaluation privacy and access | C-GOLD.1.7.7 — Protected-judgment log ownership | ACCEPTED — reciprocal USED BY entry for Gated by | Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently | ACCEPTED — reciprocal USED BY entry for Changes | One wins (CAS-3); the other's O-APPEND ends refused_domain_precondition / O-JUDGE judgment_refused_stale_head — non-retryable; Ness may deliberately judge again against the new head | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted | ACCEPTED — reciprocal USED BY entry for Changes | absorbed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor) | ACCEPTED — reciprocal USED BY entry for Changes | Chain judgment_indeterminate; trial, run head, and results indeterminate; both preserved; no resolution defined (§20) | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content | ACCEPTED — reciprocal USED BY entry for Changes | Contradiction; as CR-26 | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | ACCEPTED — reciprocal USED BY entry for Changes | That chain judgment_indeterminate until verified by lookup. Not triggered by a token being consumed (the success state), by ordinary later session expiry or closure, or by the passage of time | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token | ACCEPTED — reciprocal USED BY entry for Changes | Refused (judgment_refused_authority), non-retryable, logged | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes | ACCEPTED — reciprocal USED BY entry for Changes | Committed judgment unaffected | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND [proposed] | C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion | ACCEPTED — reciprocal USED BY entry for Changes | The forward-completing O-APPEND may lose CAS-1 → lost_race_technical; B9 admits a new O-APPEND (new ID, unchanged E9 key/content); the receipt is not re-established | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.7.9.16 — CR-29 — Crash between O-JUDGE [proposed]'s O-APPEND [proposed] commit and O-JUDGE [proposed]'s log | ACCEPTED — reciprocal USED BY entry for Changes | Append O-JUDGE's missing log; then acknowledge | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.3.1 — Canonical record preservation | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — reciprocal USED BY entry for Gated by | Canonical state records remain immutable and append-only; corrections are new linked records, with integrity reference, schema_version and creating operation identity; no copied gold/root/reading text. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.7.1.6 — judging_operation_id [proposed] | ACCEPTED — reciprocal USED BY entry for Fed by | Supplies the owning O-JUDGE operation identity. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.7.7.1 — O-JUDGE [proposed] terminal log | ACCEPTED — reciprocal USED BY entry for Changes | Completes O-JUDGE’s own terminal/log boundary before acknowledgement. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.7 — Judgment-authorization claims and protected recovery | ACCEPTED — Gated by continuation; reciprocal row on new card | O-JUDGE follows one-winner claim ownership, fence and recovery rules. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.9.8.1 — Authorization claim first | C-GOLD.1.7.3 — One-winner judgment-authorization scope | ACCEPTED — Gated by continuation; reciprocal row on new card | The claim-first stage admits exactly one scope winner. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | C-GOLD.1 — Promotion evaluation-evidence bridge | ACCEPTED — retained SUB-PARTS and Fed by continuation · CY-G | The evaluation-evidence bridge extends C-GOLD and supplies its separate narrow B16 evidence references; the top card names this exact bridge as a sub-part and supplier. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.7.4.4.1.2 — No verified bound security-audit receipt | ACCEPTED — reciprocal USED BY entry for Gated by | No verified bai_token_consumed receipt bound to this claim exists in security-audit history. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.2 — E1-bound judgment authority | C-GOLD.1.7.2 — Claim ownership separation | ACCEPTED — reciprocal USED BY entry for Gated by | The claim coordinates only; BAI’s valid durable receipt or the selected commit-time SACL proof is required for authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND [proposed] | C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed] | ACCEPTED — reciprocal USED BY entry for Gated by | The named E9 and E16 committed or their exact duplicate was absorbed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.1.2 — Unique current judgment head | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | ACCEPTED — reciprocal USED BY entry for Gated by | A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed | C-GOLD.1.7.7.6 — Authorization-failure reason: pre-receipt crash | ACCEPTED — reciprocal USED BY entry for Gated by | This log belongs only to O-JUDGE [proposed]’s durable judgment_authorization_failed terminal and carries its exact reason. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed | C-GOLD.1.7.7.7 — Authorization-failure reason: failed/unverifiable receipt write | ACCEPTED — reciprocal USED BY entry for Gated by | This log belongs only to O-JUDGE [proposed]’s durable judgment_authorization_failed terminal and carries its exact reason. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed | C-GOLD.1.7.7.8 — Authorization-failure reason: refusal before consumption | ACCEPTED — reciprocal USED BY entry for Gated by | This log belongs only to O-JUDGE [proposed]’s durable judgment_authorization_failed terminal and carries its exact reason. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.2.6.8 — O-JUDGE [proposed] judgment_authorization_failed | C-GOLD.1.7.7.9 — Authorization-failure reason: head breach after receipt | ACCEPTED — reciprocal USED BY entry for Gated by | This log belongs only to O-JUDGE [proposed]’s durable judgment_authorization_failed terminal and carries its exact reason. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.5.6.10.10 — Real-change continuation | C-GOLD.1.7.8.1 — Pending before authority consumption | ACCEPTED — reciprocal USED BY entry for Gated by | A consumed real-change record authorizes the new B9 episode; the owner remains the same O-JUDGE [proposed]. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.6.5.1 — SACL validity at judgment commit | C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes | ACCEPTED — reciprocal USED BY entry for Gated by | The original judgment proof was fresh and valid at its commit moment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

### Cross-piece relationships

| Using card | Defining/supplying card | Relation | Source |
|---|---|---|---|
| C-GOLD.1.7.1.8.1 — durable receipt identity | C-GOLD.1.6.4.3 — E9 durable receipt binding | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.1.8.2 — durable receipt integrity | C-GOLD.1.6.4.3 — E9 durable receipt binding | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed] | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.1.4 — e9_content_identity [proposed] | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.1.2 — judgment_chain_key [proposed] | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.1.8 — durable_receipt_ref [proposed] | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.2 — Claim ownership separation | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Fed by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed] | C-GOLD.1.6.4.11 — Head breach after a durable receipt | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.8.2 — Pending after authority consumption | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently | C-GOLD.1.6.1.3 — First and later judgment predecessor | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted | C-GOLD.1.6.1.3.1 — Identical E9 absorption | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor) | C-GOLD.1.6.1.5 — Judgment fork | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content | C-GOLD.1.6.1.6 — Judgment contradiction | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | C-GOLD.1.6.4.13 — Later invalid consumption proof | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | C-GOLD.1.6.4.7 — Pre-receipt crash rule | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit | C-GOLD.1.6.4.9 — Post-receipt forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token | C-GOLD.1.6.4.6 — BAI replay and reuse refusal | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes | C-GOLD.1.6.5.3 — Ordinary later session expiry | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption) | C-GOLD.1.6.4.8 — In-process receipt-write failure | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion | C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion | C-GOLD.1.6.4.11 — Head breach after a durable receipt | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | C-GOLD.1.6.5.4 — Later discovery of invalid session proof | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |
| C-GOLD.1.7.10.1 — INV-22 protected constraint | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.10.2 — INV-23 protected constraint | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.7.6 — Contradictory claim and receipt evidence | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.6.1 — Two winning claims | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.6.2 — Receipt names absent claim | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.6.3 — Receipt mismatches claim | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.7.6.4 — Two receipts for one claim | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

## Register contributions

### NOT DECIDED register

Empty fields below are source-silent boxes, not inferred policy choices. Defined behavior has been placed in its matching box. Accepted mechanics left for later pieces are listed separately.

| Part ID | Field | Value | Why retained |
|---|---|---|---|
| C-GOLD.1.7.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.6 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.7 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.8 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.8.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.8.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.8.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.8.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.9 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.9 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.10 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.10 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.11 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.11 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.12 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.12 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.13 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.13 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.14 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.14 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.15 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.15 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.16 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.1.16 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.4.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.4.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.4.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.4.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.3.4.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.3.4.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.4.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.4.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.4.4.1.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.4.1.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.4.4.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.4.1.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.4.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.4.7.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.5.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.5.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.5.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.5.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.5.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.6.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.6.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.6.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.6.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.2 | Fails closed by | NOT DECIDED | The cited text assigns no separate failure outcome to this member or log-ownership boundary; no inferred validator or terminal is added. |
| C-GOLD.1.7.7.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.3 | Fails closed by | NOT DECIDED | The cited text assigns no separate failure outcome to this member or log-ownership boundary; no inferred validator or terminal is added. |
| C-GOLD.1.7.7.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.5 | Fails closed by | NOT DECIDED | The cited text assigns no separate failure outcome to this member or log-ownership boundary; no inferred validator or terminal is added. |
| C-GOLD.1.7.7.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.6 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.7 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.8 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.8 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.9 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.9 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.7.10 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.7.10 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.8 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.8.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.8.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.9.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.8 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.9 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.10 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.11 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.12 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.13 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.14 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.15 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.9.16 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.10.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.10.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.10.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.10.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.10.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.7.10.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.7.1.5 | Purpose/scope value | NOT DECIDED | The reference is defined; the accepted NHD-B16EEB-D16 value is not supplied. |
| C-GOLD.1.7.1 | Claim physical representation | NOT DECIDED | Physical serialization, digest/canonicalization algorithms, timestamp format and storage/CAS implementation are not chosen. |

### Source-conflict and status distinctions

No conflict is resolved by this pair. B16 v1.0 §5.3 retains its input-3 phrase “the recorded B24-architecture acceptance evidence for the applicable gold-set run”; the bridge separates E11a gold evidence from E12 system eligibility. The exact bridge contract is recorded here; the old source is not edited. [SOURCE CONFLICT: 04/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md §5.3 retains the earlier input-3 wording; 04/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §7 records its pending integration.]

The selected authority option remains open. The accepted conditional mechanics do not select BAI-only, SACL-only or both. Pending/no-receipt release and receipt-bearing breach closure retain the current §7.13/§13.5 rules; historical audit summaries in §21–§22 are not alternative runtime rules.

### Decided material not placed in this pair

- Bridge §§8–9: full aggregate/result derivation, state precedence and AP-1…AP-12 applicability. The prior E10/E11/E12/E13 record cards and this pair’s judgment effects remain present; their full result algorithms are still to be decomposed.
- Bridge §10: invariants other than INV-22, INV-23, INV-25, INV-26 and INV-27 remain with their previously placed rules or await the derivation/applicability pieces. This pair adds these five protected-judgment invariants only.
- Bridge §§11–12, §§13.2–13.3, §14 and §§16–17: remaining held-out/promotion boundaries, adverse-result/disagreement rules, the remainder of the failure/dependency matrices and complete policy-slot definitions remain for later pieces. No accepted mechanics are labelled undecided because they are deferred.
- Bridge §15 traces are source examples, not selected policy values; the mechanics covered by this pair are in the rule and recovery cards. Source recommendations and audit/work-session narratives are excluded under contract §1.3.
- Remaining Group A engines, index, sealed-gold foundation/story-gold package, ingest and detector remain for later pieces.

## Coverage matrix — cumulative contribution


### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c scoped reread: status table, §0/0A/0B, reading schema, §7G-A RC sequence and §7K; Chapter 3-d focused status-table, §0B and §§6A/6B checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; Chapter 3-c focused rule/boundary searches and excerpts, no new whole-read claim | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained; Chapter 3-c C-READ/C-7K and adjacent interfaces searched/reopened; Chapter 3-d C-READ and CY-G/B16 owner checks | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3 |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Newly read whole for this correction, all 1,938 lines; pinned Git blob verified; Chapter 3-c focused retry/malformed searches and §§2.8/3.7 excerpts; prior whole-read credit retained | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file for Chapter 3-a; pinned bytes verified; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Newly read whole in Chapter 3-c; exact pinned Git blob verified | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards. |
| F101 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F102 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F103 | `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F104 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F105 | `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F106 | `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F107 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F108 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F109 | `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F110 | `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F111 | `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Whole read carried from 3-e/3-f; scoped reread for 3-g/3-h; exact blob remains verified at 6a7160b. | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F123 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F124 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7A.10; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F125 | `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F126 | `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F127 | `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Identity/hash verified; Stage 2 reading pending except FR-0125 and FR-0608 rows checked for this correction (classification and accepted-home pointer only) | NOT PLACED: Appendix B requires Stage 2 rows by FR-ID/title only; no behavior sourced from the ledger. |
| F128 | `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F129 | `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F130 | `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F131 | `05_INACTIVE_CANDIDATE/NH_ISSUE_CHANNEL_INTENT_v0_1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F132 | `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F133 | `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F134 | `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F135 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F136 | `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED in Chapters 0–2 (carried placement): intent slot belongs to Appendix C; no mechanism may be sourced. Existing Chapter 1 slots stand. |
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136). |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H008 | ## 2. HOW TO WORK WITH NESS | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H009 | ### 2A. INTERACTION AND ARTIFACT DELIVERY — LOCKED | Chapter 1 placement retained. §2 wording is carried in the marked conflict at C-7B.8; no new C-2 behavior here. |
| V10-H010 | ## 3. THE EVOLUTION — OLD vs NEW (key points) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H011 | ## 4. THE MACHINE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H012 | ## 5. THE CODEBASE MAP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ; C-READ.3; C-READ.4 built functions and paths. |
| V10-H013 | ## 6. WHAT'S BUILT & VERIFIED ON DISK  [BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ built reading boundary.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H014 | ## 6A. THE CODE RULES — `.cursorrules` v3.2 (DUAL-ARCHITECTURE, IN FORCE) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ record and write constraints.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H015 | ### IDENTITY AND PERMANENT RULES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H016 | ### THE THREE-LAYER ARCHITECTURE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H017 | ### SOVEREIGNTY BOUNDARIES BY LAYER | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.2; C-READ.3; C-READ.5. |
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H044 | ## 7R. ATTENTION AND RELEVANCE CONTROL  [CORE CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H045 | ### DECISION 1 — OUTPUT FORM | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H046 | ### DECISION 2 — PRODUCER SELECTION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H047 | ### DECISION 3 — EVALUATION TIMING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H048 | ### DECISION 4 — TWO-TIER CONFIGURATION CONTRACT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H049 | ### DECISION 5 — NESS'S RELATIONSHIP | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H050 | ### DECISION 6 — VALIDATION OF MOUTH-PRODUCED DIMENSIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H051 | ### DECISION 7 — MINIMUM SHARED VOCABULARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H052 | ### DECISION 8 — LIVING STATE WEB BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H053 | ### DECISION 9 — TIER 1 PURPOSE FIELD | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H054 | ### DECISION 10 — UNRESOLVED DIMENSION HANDLING ACROSS THE TIER BOUNDARY | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H055 | ### DECISION 11 — DISAGREEMENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H056 | ### DECISION 12 — RELEVANCE EVENT RECORD SCHEMA | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H057 | ### DECISION 13 — PATTERN OBSERVATION CONDITIONS FOR PER-JUDGMENT OVERRIDES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H058 | ### DECISION 14 — UNRECOGNIZED PURPOSE TYPE HANDLING | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H059 | ### WHAT REMAINS OPEN FOR ATTENTION AND RELEVANCE CONTROL | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H060 | ## 8. THE RESEARCH PIPELINE  [DESIGNED — Brave not wired] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H061 | ## 9. DESIGNED, NOT BUILT — THE REST  [DESIGNED or CONCEPTUALLY DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H062 | ### §9 RECOVERED ACCESS AND AUTHENTICATION MODEL  [RECOVERED ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H063 | ### §9 RECOVERED VOICE INPUT/OUTPUT PIPELINE  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H064 | ### §9 FIVE PHONE-SIDE MODES  [RECOVERED NAMES ONLY — BEHAVIOR NOT DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H065 | ### §9 PERSONALITY-RELATED CONVERSATION REHEARSAL  [RECOVERED PARTIAL DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H075 | ## 17. S16 CORRECTION LOG — WHAT THE S16 CORRECTION PASS CHANGED (historical) | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H076 | ## 18. S17 CONSOLIDATION AND CORRECTION LOG | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H077 | ## 19. INTERFACE, WORLD, AND INTERACTION SYSTEM  [IN-PROGRESS DESIGN, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H078 | ### 19A. SETTLED INTERFACE DECISIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H079 | ### 19B. PROVISIONAL CONCEPTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H080 | ### 19C. UNANSWERED QUESTIONS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H081 | ### 19D. PAUSED DESIGN POINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H082 | ### 19E. OPEN DEPENDENCIES (cross-audit results) | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H083 | ### TRUEST SINGLE SENTENCE | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H084 | ## 20. S18 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 24 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H085 | ## 21. S19 CONSOLIDATION AND CHANGE LOG  [HISTORICAL SESSION SNAPSHOT — June 25 2026] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H086 | ## 22. WELLBEING AND BEHAVIORAL BASELINE SYSTEM  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H087 | ## 23. MOBILE APP — THREE-MODE COMPANION  [DESIGNED — full spec restored S19, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H088 | ## 24. CONNECTION CAPABILITY  [CONCEPTUALLY DESIGNED (S19), NOT BUILT] | Partial placement: C-7B.10.6.2.2; C-7B.10.6.2.3; C-7B.10.6.3.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H089 | ## 25. VOICE SECURITY AND IDENTITY SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H090 | ### Build-Time Implementation Settings | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H091 | ### 25.1. BOP — Behavioral Observation Processing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H092 | ### 25.2. Other-Speaker / Guest / Known-Person Architecture | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H093 | ### 25.3. SIA — Speaker Identity Assessment | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H094 | ### 25.4. SACL — Speaker Access-Control Layer | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H095 | ### 25.5. Wellbeing / Identity / Security Separation Rules | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H096 | ### 25.6. BAI — Biometric Authorization Interface | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H097 | ### One-Time Authorization Token | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H098 | ### Top-Security Biometric Lease | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H099 | ### 25.7. Initial Owner-Phone Pairing | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H100 | ### 25.8. Recovery-Code Lifecycle | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H101 | ### 25.9. Future-Phone Replacement Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H102 | ### 25.10. Atomic Emergency Recovery Flow | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H103 | ### 25.11. Initial Ness Voice-Profile Enrollment Bootstrap | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H104 | ### 25.12. Formally Adopted Vocabulary Additions | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H105 | ### 25.13. BGMM — Biometric-Gated Maintenance Mode | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H106 | ## 26. PERSONAL LEARNING AND ADAPTATION SYSTEM  [ACCEPTED DESIGN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H107 | ## 27. HISTORICAL RECOVERY AND CORRECTION LOG — JUNE 25 2026 | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |

### Additional READ-folder files at this source pin

| File | Placement |
|---|---|
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | NOT PLACED: outside this evaluation-evidence piece; no content borrowed. |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH01.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH02.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-a.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-b.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-c.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |
| `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-d.md` | EXCLUDED: previously delivered target chapter; assembly input, not an independent behavior source (§1.3). |

### Detailed source landing map

| Bridge section | Cards in this piece |
|---|---|
| §7.13 | C-GOLD.1.7, C-GOLD.1.7.1, C-GOLD.1.7.1.1, C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.5, C-GOLD.1.7.1.6, C-GOLD.1.7.1.7, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.1.9, C-GOLD.1.7.1.10, C-GOLD.1.7.1.11, C-GOLD.1.7.1.12, C-GOLD.1.7.1.13, C-GOLD.1.7.1.14, C-GOLD.1.7.1.15, C-GOLD.1.7.1.16, C-GOLD.1.7.2, C-GOLD.1.7.3, C-GOLD.1.7.3.1, C-GOLD.1.7.3.2, C-GOLD.1.7.3.3, C-GOLD.1.7.3.4, C-GOLD.1.7.3.4.1, C-GOLD.1.7.3.4.2, C-GOLD.1.7.3.4.3, C-GOLD.1.7.4, C-GOLD.1.7.4.1, C-GOLD.1.7.4.2, C-GOLD.1.7.4.3, C-GOLD.1.7.4.4, C-GOLD.1.7.4.4.1, C-GOLD.1.7.4.4.1.1, C-GOLD.1.7.4.4.1.2, C-GOLD.1.7.4.5, C-GOLD.1.7.4.6, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.5, C-GOLD.1.7.5.1, C-GOLD.1.7.5.2, C-GOLD.1.7.5.3, C-GOLD.1.7.5.4, C-GOLD.1.7.5.5, C-GOLD.1.7.5.6, C-GOLD.1.7.6, C-GOLD.1.7.6.1, C-GOLD.1.7.6.2, C-GOLD.1.7.6.3, C-GOLD.1.7.6.4, C-GOLD.1.7.7, C-GOLD.1.7.8, C-GOLD.1.7.9, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §13.1 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.10, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.11, C-GOLD.1.7.9.12, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14, C-GOLD.1.7.9.15, C-GOLD.1.7.9.16 |
| §13.5 | C-GOLD.1.7, C-GOLD.1.7.7, C-GOLD.1.7.7.1, C-GOLD.1.7.7.2, C-GOLD.1.7.7.3, C-GOLD.1.7.7.4, C-GOLD.1.7.7.5, C-GOLD.1.7.7.6, C-GOLD.1.7.7.7, C-GOLD.1.7.7.8, C-GOLD.1.7.7.9, C-GOLD.1.7.7.10, C-GOLD.1.7.8, C-GOLD.1.7.8.1, C-GOLD.1.7.8.2, C-GOLD.1.7.9, C-GOLD.1.7.9.16, C-GOLD.1.7.10, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4 |
| §10 | C-GOLD.1.7, C-GOLD.1.7.10, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2, C-GOLD.1.7.10.3, C-GOLD.1.7.10.4, C-GOLD.1.7.10.5 |
| §5 | C-GOLD.1.7.1, C-GOLD.1.7.1.16, C-GOLD.1.7.7 |
| §13.4 | C-GOLD.1.7.1, C-GOLD.1.7.7 |
| §7.12 | C-GOLD.1.7.1.2, C-GOLD.1.7.1.3, C-GOLD.1.7.1.4, C-GOLD.1.7.1.8, C-GOLD.1.7.1.8.1, C-GOLD.1.7.1.8.2, C-GOLD.1.7.2, C-GOLD.1.7.4.7, C-GOLD.1.7.4.7.1, C-GOLD.1.7.4.7.2, C-GOLD.1.7.4.7.3, C-GOLD.1.7.4.7.4, C-GOLD.1.7.4.7.5, C-GOLD.1.7.4.7.6, C-GOLD.1.7.4.7.7, C-GOLD.1.7.6, C-GOLD.1.7.9.5, C-GOLD.1.7.9.6, C-GOLD.1.7.9.7, C-GOLD.1.7.9.8, C-GOLD.1.7.9.9, C-GOLD.1.7.9.10, C-GOLD.1.7.9.13, C-GOLD.1.7.9.14 |
| §7.11 | C-GOLD.1.7.6, C-GOLD.1.7.9, C-GOLD.1.7.9.1, C-GOLD.1.7.9.2, C-GOLD.1.7.9.3, C-GOLD.1.7.9.4, C-GOLD.1.7.9.5, C-GOLD.1.7.10.1, C-GOLD.1.7.10.2 |
| §7.2 | C-GOLD.1.7.7.1, C-GOLD.1.7.7.4 |
| §7.9 | C-GOLD.1.7.9.1, C-GOLD.1.7.9.2 |

## READ RECORD

Round 3A correction: the attached `NH_MASTER-21_FIX_REQUEST_ROUND3_2026-09-26.md`, all listed cards and their cited source sections were checked; no fresh whole-read source credit or source-pin change is claimed.

### Whole-read source credit carried forward

- `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` — whole read for 3-e/3-f, retained here; 2,018 lines, 135,956 bytes; SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`. This pair performs scoped rereads and adds no fresh whole-read credit.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` — whole read carried from 3-e/3-f; identity/acceptance and unique slot-name sections checked for this pair. SHA-256 `298de053269f4a9e93e97dfd994d33b0b879d71af636b169769264e7183d9d4c`.
- Earlier authoritative/accepted whole-read accounting is inherited from the preceding pieces; no unread file supplies new behavior.

### Instructions read and scoped source checks for this pair

- Cloned build contract, SHA-256 `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`; governing sections reopened before writing and §11.3 reopened after writing for the checks below.
- `NH_MASTER-21_FIX_REQUEST_ROUND1_2026-09-25(1).md`: every-card field placement, exact source stamps, step-to-rule reciprocity and unchanged passed cards.
- Bridge §§5, 7.9, 7.11–7.13, 10, 13.1, 13.4–13.5, 14, 18–20 reread for this pair; existing §2.5/§3/§9 ownership continuation retained from the prior whole read.
- V10’s authoritative status table checked for exact behavior standing; the bridge is not built. Receipt §§3–5 and §§7–8 distinguish exact-byte acceptance, no implementation and open option values.
- The bridge source and acceptance receipt SHA-256 fingerprints listed above match the pinned copies. The fixed source pin is `6a7160ba688ba4e433a31899162815df7e2bab17`; no newer repository head is used as a source.

### READ-folder files not yet read whole

97 entries retain the earlier pending whole-read status. The three B16/receipt files already had older Chapter 0 reading credits and were not in that pending list; they were now reread whole at this pin. The bridge source has only its earlier credit plus the scoped current check, not a new whole read. Scoped searches/excerpts supply no whole-read credit. The ledger retains its Stage-2-only exception.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/02-NH_BUNDLE_6_A3_DECISIONS_WORKING_RECORD_v1-1-.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/HISTORICAL_ANSWER_PROVENANCE.json`
- `05_ACTIVE_CANDIDATE/Music_Media_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_A19_REMAINING_HUMAN_EXPERIENCE_DESIGN_PLAN_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md`
- `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md`
- `05_ACTIVE_CANDIDATE/NH_DESIGN_ANSWERS.md`
- `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md`
- `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md`
- `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md`
- `05_ACTIVE_CANDIDATE/Thought_Branches_and_Simulation_Intent.md`
- `05_INACTIVE_CANDIDATE/NH_FUTURE_MUSIC_UNDERSTANDING_AND_MUSIC_SERVICE_CONNECTIONS_PACKAGE_INTAKE_v1_0_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_PROVENANCE_FIRST_MULTI_INDEX_MEMORY_FABRIC_MECHANICAL_DESIGN_v1_4_CANDIDATE.md`
- `05_INACTIVE_CANDIDATE/NH_SECURITY_STORAGE_ENCRYPTION_INTENT_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_TOOLS_FOR_NH_CATEGORY_v0_1.md`
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`

- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` — newly present at this source pin; not used for this evaluation scope.

The unread list and cumulative coverage are carried forward at the fixed pin. Earlier passed target chapters are assembly inputs, not independent behavior sources. No new whole-read source credit is claimed for a scoped reread.

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — checked all 96 behavior cards and their reciprocal entries; runtime judgment authority is retained as machine behavior. Source-status/read accounting remains separate from behavior; no source work-session or audit narrative is imported.
§1.4 every gap written as NOT DECIDED: PASS — every card’s own text and source were reviewed for prohibition, failure and gate placement; 132 source-silent boxes and 2 explicit unchosen values/mechanics are registered. Defined mechanics deferred to later pieces are separately identified, not called undecided. Round 3A: all 36 listed unnamed TOGETHER lines reviewed: 31 disposition 1, 0 disposition 2, 5 disposition 3; no additional unnamed lines found.
§1.5 conflicts marked, none resolved: PASS — the inherited B16 input-3/E11a/E12 distinction remains visible in the source-conflict register; no earlier source or passed chapter is rewritten. V10 remains governing.
§3 exactly one stamp per line: PASS — 846 populated field lines and 236 USED BY rows checked; all new behavior and relations are ACCEPTED from the exact-byte accepted bridge. No box or link is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — all populated field lines and relationship rows carry exact 05/file §section citations and NHD-B16EEB; all section targets resolve. Conditional authority, claim and recovery outcomes were checked against §§7.11–7.13 and §13.1/§13.5 rather than historical audit summaries.
§5.4 one name per thing: PASS — existing endpoint IDs/names are retained, new IDs remain under C-GOLD.1.6 and C-GOLD.1.7, and no new top-level or decision-slot ID is invented. The C-GOLD.1 — Promotion evaluation-evidence bridge SUB-PARTS/Fed by continuation is retained explicitly.
§6 all template fields present, in order, for every part: PASS — all 96 cards have all nine fields in order, ALONE, TOGETHER, USED BY and SUB-PARTS; child references resolve.
§6.3 reciprocity within this chapter: PASS — all 1441 unique forward card relationships in corrected CH03-e/CH03-f/CH03-g/CH03-h checked against USED BY rows or retained continuation entries. Every new disposition-1 reference has its reciprocal in the named card’s own file when that card is in this round, otherwise in the using chapter’s continuation table. Existing step-to-rule links remain; continuation entries stay in their own tables and are not merged at assembly.
§6.4 every decided detail written in, no citation used in place of content: PASS within this piece’s explicit scope — Claim record and each member; ownership and authorization-scope tuple; duplicate admission conditions; six states and their defined transitions including conditional SACL-only completion; positive no-receipt proof; replacement gates, pending and receipt-bearing fences; contradiction classes; operation-specific log ownership; both pending situations; all sixteen remaining CR rows (24–29 and 31–40), each linked to its defining rule; INV-22, INV-23 and INV-25–27.
§6.5 sub-parts recursed to the bottom: PASS within this piece’s explicit scope — named record members, proof conditions, failure classes, claim states/transitions, duplicate/replacement gates and protected recovery outcomes have their own cards. No physical storage, digest algorithm, authentication method or policy value is fabricated.
§9 coverage matrix rows added for every file used: PASS — all 145 READ-folder files at the fixed source pin and all 107 V10 heading rows remain accounted for; bridge placement is updated and detailed source landings are listed. The bridge source and acceptance receipt SHA-256 fingerprints are listed in READ RECORD and match the pinned copies.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked behavior and register contributions; conditional options are source-defined mechanics, not recommendations or selected values.
Files read whole for this chapter: whole-read source credit is inherited from Chapters 3-e/3-f for `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` and its exact acceptance receipt in `04_ACCEPTED_STANDALONE_DESIGNS/`; no fresh whole-read source credit is claimed. The cloned contract and fix-request instructions were reopened; this pair’s scoped source checks and the remaining unread list are recorded in READ RECORD.

This is the producing assistant’s contract check, not an independent audit, acceptance, adoption or implementation authorization. The fixed source pin is 6a7160ba688ba4e433a31899162815df7e2bab17.
