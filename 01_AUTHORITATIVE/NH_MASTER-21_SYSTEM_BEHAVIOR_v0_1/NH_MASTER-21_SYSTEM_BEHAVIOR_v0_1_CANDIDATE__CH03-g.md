# Chapter 3-g — Group A: C-GOLD, judgment chains and conditional authority proofs

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH03-g.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This pair continues C-GOLD.1 under CY-G. Chapter 3-g decomposes bridge §§7.11–7.12: the judgment chain, authority modes and each conditional proof lifecycle. Chapter 3-h decomposes §7.13: the claim record, states, transitions, one-winner scope, replacement gates and fences, together with protected judgment recovery and logging. The complete result-derivation and per-reading applicability rules remain for later pieces; this pair does not complete C-GOLD, the evaluation bridge or Group A.

Authority order: V10 → Decision Defaults v2_2 → cursorrules → Companion v1; the Map is subordinate. All new behavior and relationship rows are ACCEPTED from the exact accepted bridge v1.7. Receipt §§3–5 binds acceptance to SHA-256 `04dd5abc42e59afb61b4d280a0bb69d647d187fd0da385bc5c567eddbca81a41`; its frozen candidate header does not change that standing. None of these bridge behaviors or links has BUILT standing in V10’s status table.

Citation keys: `05/` = `05_ACTIVE_CANDIDATE/`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = Design and Wiring Map v1.6. NHD-B16EEB identifies the accepted bridge. Its open decisions use the receipt’s globally unique NHD-B16EEB-D… identifiers. All source-proposed field, record, event and state names remain proposed; no option, policy value, physical representation or implementation is selected.

Continuation entries stay in this piece; joining the pieces concatenates them and does not merge or edit passed cards. C-GOLD’s existing top-card continuation remains C-GOLD.1 — Promotion evaluation-evidence bridge, both as a SUB-PART and as Fed by. The protected stages remain linked durable stages; only E9 + E16 is one O-APPEND atomic commit.

<!-- BEGIN CHAPTER 3-g BEHAVIOR -->

### C-GOLD.1.6 — Judgment chains and conditional authority proofs
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The per-output judgment chain and the accepted conditional authority protocol. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Effectively completed outputs, E1 scoring bindings and E9 authority references. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Maintains one current authorized judgment head and verifies the proof selected by NHD-B16EEB-D16 at its event-time boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Authorized chain heads, or refused/unavailable/indeterminate judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Choose the open proof option, use model assistance as authority or resolve a fork by recency. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No Ness judgment before NHD-B16EEB-D16 is accepted; forks, contradictions and unverifiable committed authority fail closed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1 — Per-output judgment-chain rules: Defines a single current head only while the chain has no fork or contradiction; authorized corrections append new E9 records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: Requires the authority matching the case’s declared judgment mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: Commits the claim first; when BAI is required it separately consumes and flushes its receipt; O-APPEND then atomically commits only E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: Follows claim → flushed bai_token_consumed receipt → committed E9 + E16; only the flushed receipt proves durable consumption after a crash. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5 — Conditional SACL session proof: At O-JUDGE commit verifies the required state was fresh and valid then, and records an immutable event-time reference in E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.6 — Conditional combined BAI and SACL proof: Applies both sets of requirements: consumed token with bound durable receipt, and session state verified and immutably referenced at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.5 — judgment-authority requirement: NHD-B16EEB-D16 must be accepted before any Ness judgment can commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Maintains one current authorized judgment head and verifies the proof selected by NHD-B16EEB-D16 at its event-time boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1 — Promotion evaluation-evidence bridge | Effectively completed outputs, E1 scoring bindings and E9 authority references. | Maintains one current authorized judgment head and verifies the proof selected by NHD-B16EEB-D16 at its event-time boundary. | Authorized chain heads, or refused/unavailable/indeterminate judgments. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.5.2.6 — O-JUDGE [proposed] | Effectively completed outputs, E1 scoring bindings and E9 authority references. | O-JUDGE follows the complete judgment-chain and conditional authority protocol. | Authorized chain heads, or refused/unavailable/indeterminate judgments. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.11.17 — NHD-B16EEB-D16 authority-proof choice | Available accepted identity/security patterns: a `recognized_ness` SACL session, a BAI purpose-bound artifact including `extended:<purpose_id>`, or their combination. | Supplies the already-defined conditional proof mechanics without selecting an option. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] |

SUB-PARTS: C-GOLD.1.6.1 — Per-output judgment-chain rules; C-GOLD.1.6.2 — E1-bound judgment authority; C-GOLD.1.6.3 — Linked protected-judgment protocol; C-GOLD.1.6.4 — Conditional BAI artifact proof; C-GOLD.1.6.5 — Conditional SACL session proof; C-GOLD.1.6.6 — Conditional combined BAI and SACL proof

### C-GOLD.1.6.1 — Per-output judgment-chain rules
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — One chain per effectively completed output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — planned_trial_output_key and committed E9 records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Defines a single current head only while the chain has no fork or contradiction; authorized corrections append new E9 records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — A unique current head or judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Rewrite an old judgment, choose by recency or extend a forked chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Forks and contradictions make the trial, run aggregate head and all downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1.1 — Judgment-chain key and creation: Keys the chain by planned_trial_output_key once that output is effectively completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: Selects the unique committed E9 with no committed successor, only while no fork or contradiction exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.3 — First and later judgment predecessor: The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.4 — Authorized append-only judgment correction: Appends the correction; preserves the previous judgment byte-identically and stops treating it as the head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.5 — Judgment fork: Marks the chain judgment_indeterminate; marks the trial, run aggregate head and every downstream result indeterminate; preserves both judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.6 — Judgment contradiction: Marks the chain judgment_indeterminate and all dependent trial/run/result state indeterminate; preserves conflicting records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: Consumes exactly its current authorized head and records the consumed set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.9.8 — EB-8 — Protected judgment: Judgments require an effectively completed output and an E1-matching authority reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | planned_trial_output_key and committed E9 records. | Defines a single current head only while the chain has no fork or contradiction; authorized corrections append new E9 records. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.2 — Claim ownership separation | planned_trial_output_key and committed E9 records. | The judgment chain owns the head. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.10.1 — INV-22 protected constraint | planned_trial_output_key and committed E9 records. | The defining rule supplies this invariant’s exact condition and outcome. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | planned_trial_output_key and committed E9 records. | The affected judgment chain becomes judgment_indeterminate. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.6.1 — Two winning claims | planned_trial_output_key and committed E9 records. | The scope and chain become judgment_indeterminate; preserve all records. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.6.2 — Receipt names absent claim | planned_trial_output_key and committed E9 records. | The scope and chain become judgment_indeterminate; preserve all records. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.7.6.3 — Receipt mismatches claim | planned_trial_output_key and committed E9 records. | The scope and chain become judgment_indeterminate; preserve all records. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.6.4 — Two receipts for one claim | planned_trial_output_key and committed E9 records. | The scope and chain become judgment_indeterminate; preserve all records. | A unique current head or judgment_indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.1.1 — Judgment-chain key and creation; C-GOLD.1.6.1.2 — Unique current judgment head; C-GOLD.1.6.1.3 — First and later judgment predecessor; C-GOLD.1.6.1.4 — Authorized append-only judgment correction; C-GOLD.1.6.1.5 — Judgment fork; C-GOLD.1.6.1.6 — Judgment contradiction; C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10

### C-GOLD.1.6.1.1 — Judgment-chain key and creation
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment-chain key and creation rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The output’s planned_trial_output_key and E7 attempt_completed or E7r resolved_output_found. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Keys the chain by planned_trial_output_key once that output is effectively completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — One output-keyed chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit a judgment for an output without effective completion or extend a forked chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An output without effective completion cannot accept a judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — An invalid output is refused with judgment_refused_output_invalid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.2] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal [proposed] (E7): E7 attempt_completed establishes effective completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.3.8 — trial_attempt_resolution [proposed] (E7r): E7r resolved_output_found establishes effective completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.7 — trial_attempt_terminal [proposed] (E7): E7 attempt_completed or C-GOLD.1.3.8 — trial_attempt_resolution [proposed] (E7r): E7r resolved_output_found establishes effective completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Keys the chain by planned_trial_output_key once that output is effectively completed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | The output’s planned_trial_output_key and E7 attempt_completed or E7r resolved_output_found. | Keys the chain by planned_trial_output_key once that output is effectively completed. | One output-keyed chain. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.2 — Unique current judgment head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Unique current judgment head rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Committed E9 records for this chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Selects the unique committed E9 with no committed successor, only while no fork or contradiction exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The single current judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Use recency to choose between conflicting judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A fork or contradiction leaves no single valid head and makes the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The chain has no fork and no contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: CAS-3 alone advances the unique current judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Selects the unique committed E9 with no committed successor, only while no fork or contradiction exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | Committed E9 records for this chain. | Selects the unique committed E9 with no committed successor, only while no fork or contradiction exists. | The single current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.1.4 — Authorized append-only judgment correction | Committed E9 records for this chain. | The correction extends exactly the single current head. | The single current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | Committed E9 records for this chain. | Supplies the unique current head for each output. | The single current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | One effectively completed output’s planned_trial_output_key, expected judgment head or none, and E9 content. | expected_previous_judgment_head is still the current head and CAS-1 also holds; identical submission may absorb. | At most one successor for a current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.1.5 — Judgment fork | Two committed successors of one predecessor. | A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.1.6 — Judgment contradiction | Different content under one E9 identity, or E9 bytes that do not match the identity. | A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | Every meaning-dependent effectively completed output in the run. | Exactly one current authorized head exists for each such output. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.6 — Contradictory claim and receipt evidence | Two winning claims, a nonexistent/mismatched receipt claim, or two receipts for one claim. | A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. | Indeterminate protected-judgment scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.3 — First and later judgment predecessor
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The First and later judgment predecessor rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The proposed E9 and the chain’s current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — A predecessor-bound E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Extend a forked chain with no single head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit a judgment for an output without effective completion or extend a forked chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A stale competing expected head is refused non-retryably. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — O-APPEND ends refused_domain_precondition and O-JUDGE ends judgment_refused_stale_head on a stale expected head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1.3.1 — Identical E9 absorption: Absorbs the identical committed E9 without adding another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: CAS-3 requires the expected head to equal the unique current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: CAS-3 compares the exact expected judgment head before extension. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | The proposed E9 and the chain’s current head. | The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. | A predecessor-bound E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.1 — CR-24 — Two O-JUDGEs extend the same head concurrently | The proposed E9 and the chain’s current head. | The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. | A predecessor-bound E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.1.3.1 — Identical E9 absorption

### C-GOLD.1.6.1.3.1 — Identical E9 absorption
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Identical E9 absorption rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Takes in: ACCEPTED — An identical E9 re-submission. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Does: ACCEPTED — Absorbs the identical committed E9 without adding another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Gives out: ACCEPTED — absorbed [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Must never: ACCEPTED — Create a second judgment for identical key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Different content under one E9 identity is an integrity contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The re-submitted E9 is identical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Absorbs the identical committed E9 without adding another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.3 — First and later judgment predecessor | An identical E9 re-submission. | Absorbs the identical committed E9 without adding another judgment. | absorbed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.2 — CR-25 — Identical E9 re-submitted | An identical E9 re-submission. | Absorbs the identical committed E9 without adding another judgment. | absorbed | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.4 — Authorized append-only judgment correction
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authorized append-only judgment correction rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — A new authorized E9 naming the single current head and carrying change_reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Appends the correction; preserves the previous judgment byte-identically and stops treating it as the head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — A new authorized current head and unchanged earlier judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Edit the previous judgment or extend without the exact current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A forked chain cannot be extended. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1.4.1 — change_reason: Records the reason carried by the new correction E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): The new E9 is authorized and its expected head is the unique current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: The correction extends exactly the single current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: A correction is a new authorized E9, not an edit to its predecessor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): The new authorized E9 becomes head; the predecessor remains byte-identical. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | A new authorized E9 naming the single current head and carrying change_reason. | Appends the correction; preserves the previous judgment byte-identically and stops treating it as the head. | A new authorized current head and unchanged earlier judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.1.4.1 — change_reason | A new authorized E9 naming the single current head and carrying change_reason. | An authorized correction carries this reason and extends the single current head. | A new authorized current head and unchanged earlier judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.1.4.1 — change_reason

### C-GOLD.1.6.1.4.1 — change_reason
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The change_reason member of Authorized append-only judgment correction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The reason carried by the new correction E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records the reason carried by the new correction E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The change_reason member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Omit change_reason when superseding a judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The new superseding E9 carries its change_reason. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.1.4 — Authorized append-only judgment correction: An authorized correction carries this reason and extends the single current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.4 — Authorized append-only judgment correction | The reason carried by the new correction E9. | Records the reason carried by the new correction E9. | The change_reason member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.5 — Judgment fork
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment fork rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Two committed successors of one predecessor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Marks the chain judgment_indeterminate; marks the trial, run aggregate head and every downstream result indeterminate; preserves both judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No usable current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Choose by recency, extend the forked chain or use NHD-B16EEB-D10/D11 to resolve it. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The chain stays indeterminate; no fork-resolution procedure is defined. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | Two committed successors of one predecessor. | Marks the chain judgment_indeterminate; marks the trial, run aggregate head and every downstream result indeterminate; preserves both judgments. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.3 — CR-26 — Fork found (two committed successors of one predecessor) | Two committed successors of one predecessor. | Marks the chain judgment_indeterminate; marks the trial, run aggregate head and every downstream result indeterminate; preserves both judgments. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.6 — Judgment contradiction
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment contradiction rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Different content under one E9 identity, or E9 bytes that do not match the identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Marks the chain judgment_indeterminate and all dependent trial/run/result state indeterminate; preserves conflicting records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No usable current head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Choose by recency or extend the contradictory chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory judgment evidence stays indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1.6.1 — Same E9 identity, different content: Treats this as a judgment contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.6.2 — E9 bytes do not match identity: Treats this as a judgment contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: A single non-contradictory judgment head is required for further extension; contradictory state cannot authorize a new judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | Different content under one E9 identity, or E9 bytes that do not match the identity. | Marks the chain judgment_indeterminate and all dependent trial/run/result state indeterminate; preserves conflicting records. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.1.6.1 — Same E9 identity, different content | Different content under one E9 identity, or E9 bytes that do not match the identity. | The contradiction rule governs this condition. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.1.6.2 — E9 bytes do not match identity | Different content under one E9 identity, or E9 bytes that do not match the identity. | The contradiction rule governs this condition. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.9.4 — CR-27 — E9 bytes do not match its identity, or same identity with different content | Different content under one E9 identity, or E9 bytes that do not match the identity. | Marks the chain judgment_indeterminate and all dependent trial/run/result state indeterminate; preserves conflicting records. | No usable current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.1.6.1 — Same E9 identity, different content; C-GOLD.1.6.1.6.2 — E9 bytes do not match identity

### C-GOLD.1.6.1.6.1 — Same E9 identity, different content
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Same E9 identity, different content rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Different content under one E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Treats this as a judgment contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — judgment_indeterminate for the chain; indeterminate trial, run head and results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Use this evidence as a valid judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The chain and its dependents are indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.6 — Judgment contradiction: The contradiction rule governs this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): judgment_indeterminate for the chain; indeterminate trial, run head and results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.6 — Judgment contradiction | Different content under one E9 identity. | Treats this as a judgment contradiction. | judgment_indeterminate for the chain; indeterminate trial, run head and results. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.6.2 — E9 bytes do not match identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E9 bytes do not match identity rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — A record whose bytes do not match its E9 identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Treats this as a judgment contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — judgment_indeterminate for the chain; indeterminate trial, run head and results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Use this evidence as a valid judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The chain and its dependents are indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.6 — Judgment contradiction: The contradiction rule governs this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): judgment_indeterminate for the chain; indeterminate trial, run head and results. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.6 — Judgment contradiction | A record whose bytes do not match its E9 identity. | Treats this as a judgment contradiction. | judgment_indeterminate for the chain; indeterminate trial, run head and results. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Current judgment-head set consumed by E10 rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Every meaning-dependent effectively completed output in the run. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Consumes exactly its current authorized head and records the consumed set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The exact current authorized head set used by E10. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let any other judgment contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing head gives incomplete; forked, contradictory, unverifiable-authority or integrity-failed chain gives indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: Supplies the unique current head for each output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7.1 — Missing judgment head: Derives incomplete for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7.2 — Forked judgment input: Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7.3 — Contradictory judgment input: Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7.4 — Unverifiable judgment authority: Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.1.7.5 — Judgment integrity failure: Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.1.2 — Unique current judgment head: Exactly one current authorized head exists for each such output. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: Only current authorized judgment heads may contribute to passed/eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): Binds E10 to exactly the consumed current judgment-head set. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1 — Per-output judgment-chain rules | Every meaning-dependent effectively completed output in the run. | Consumes exactly its current authorized head and records the consumed set. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.1.7.1 — Missing judgment head | Every meaning-dependent effectively completed output in the run. | The exact current-head consumption rule governs this input. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.1.7.2 — Forked judgment input | Every meaning-dependent effectively completed output in the run. | The exact current-head consumption rule governs this input. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.1.7.3 — Contradictory judgment input | Every meaning-dependent effectively completed output in the run. | The exact current-head consumption rule governs this input. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.1.7.4 — Unverifiable judgment authority | Every meaning-dependent effectively completed output in the run. | The exact current-head consumption rule governs this input. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.1.7.5 — Judgment integrity failure | Every meaning-dependent effectively completed output in the run. | The exact current-head consumption rule governs this input. | The exact current authorized head set used by E10. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.8.1.5.1 — Sealed-gold aggregate scoring | Ness's current authorized per-case judgment heads under the six settled rules and the accepted gold aggregate rule from the frozen epoch, identified by bridge decision NHD-B16EEB-D2. | Supplies only current authorized gold judgments. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.1] |
| 8 · ACCEPTED | C-GOLD.1.8.5 — Derivation prohibitions | Suite/policy/case bindings, judgment authority and heads, all-run evidence, current aggregates, actual coverage and attempt history used in derivation. | Gates this place: derivation counts only current authorized heads. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.5] |
| 9 · ACCEPTED | C-GOLD.1.8.1.3.4 — Current judgment missing | The effectively completed output and its judgment-chain state. | Supplies exactly the current heads of meaning-dependent completed outputs. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] |

SUB-PARTS: C-GOLD.1.6.1.7.1 — Missing judgment head; C-GOLD.1.6.1.7.2 — Forked judgment input; C-GOLD.1.6.1.7.3 — Contradictory judgment input; C-GOLD.1.6.1.7.4 — Unverifiable judgment authority; C-GOLD.1.6.1.7.5 — Judgment integrity failure

### C-GOLD.1.6.1.7.1 — Missing judgment head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Missing judgment head rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — A meaning-dependent completed output has no head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Derives incomplete for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let this input contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E10 is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: The exact current-head consumption rule governs this input. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): incomplete [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | A meaning-dependent completed output has no head. | Derives incomplete for E10 from this condition. | incomplete | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.7.2 — Forked judgment input
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Forked judgment input rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment chain has a fork. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let this input contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E10 is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: The exact current-head consumption rule governs this input. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | The judgment chain has a fork. | Derives indeterminate for E10 from this condition. | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.7.3 — Contradictory judgment input
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Contradictory judgment input rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment chain is contradictory. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let this input contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E10 is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: The exact current-head consumption rule governs this input. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | The judgment chain is contradictory. | Derives indeterminate for E10 from this condition. | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.7.4 — Unverifiable judgment authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Unverifiable judgment authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The chain’s authority cannot be verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let this input contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E10 is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: The exact current-head consumption rule governs this input. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | The chain’s authority cannot be verified. | Derives indeterminate for E10 from this condition. | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.1.7.5 — Judgment integrity failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment integrity failure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The chain fails integrity verification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Derives indeterminate for E10 from this condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Let this input contribute to passed or eligible. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — E10 is indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10: The exact current-head consumption rule governs this input. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): indeterminate [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | The chain fails integrity verification. | Derives indeterminate for E10 from this condition. | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2 — E1-bound judgment authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment_authority_ref check enforced at O-JUDGE / EB-8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — E1 case scoring binding and the proposed E9 authority reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Requires the authority matching the case’s declared judgment mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — An authorized reference or a refused judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Accept a bare annotator name or model-only authority; invent an authentication method. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Absent, unverifiable, mismatched or unauthorized proof refuses E9; an unjudged output is incomplete. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.3.2 — evaluation_suite_manifest [proposed] (E1): Supplies the case judgment mode and scoring-rule/checker binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: Requires event-time proof under accepted §25 mechanisms that Ness performed this recorded judgment act. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: Requires the exact declared checker configuration identity and version plus its execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.3 — Held-out judgment authority boundary: Requires the authority defined by an accepted held-out policy under NHD-B16EEB-D7; that policy is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.4 — Model assistance carries no authority: Records model assistance only as assistance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.5 — Annotation provenance supplements verified authority: Records provenance in addition to verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.2.12 — Per-case scoring binding: The proof matches E1’s scoring binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.10.6 — judgment_authority_ref: E9 binds the verifiable authority reference required by that E1 mode. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | E1 case scoring binding and the proposed E9 authority reference. | Requires the authority matching the case’s declared judgment mode. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | E1 case scoring binding and the proposed E9 authority reference. | The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.5 — Conditional SACL session proof | E1 case scoring binding and the proposed E9 authority reference. | The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.6 — Conditional combined BAI and SACL proof | E1 case scoring binding and the proposed E9 authority reference. | The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | E1 case scoring binding and the proposed E9 authority reference. | The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.10.2 — INV-23 protected constraint | E1 case scoring binding and the proposed E9 authority reference. | The defining rule supplies this invariant’s exact condition and outcome. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §10] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.1.4 — Authorized append-only judgment correction | E1 case scoring binding and the proposed E9 authority reference. | A correction is a new authorized E9, not an edit to its predecessor. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | E1 case scoring binding and the proposed E9 authority reference. | Only current authorized judgment heads may contribute to passed/eligible. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | E1 case scoring binding and the proposed E9 authority reference. | The E1-bound proof must be present and verifiable at commit. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.3.10.6 — judgment_authority_ref | E1 case scoring binding and the proposed E9 authority reference. | The recorded authority reference must satisfy the E1-bound judgment mode. | An authorized reference or a refused judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.7.2 — Claim ownership separation | The claim, BAI token/receipt, judgment head and E9/E16 append. | The claim coordinates only; BAI’s valid durable receipt or the selected commit-time SACL proof is required for authority. | Separated state and authority ownership. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.8.5 — Derivation prohibitions | Suite/policy/case bindings, judgment authority and heads, all-run evidence, current aggregates, actual coverage and attempt history used in derivation. | Gates this place: accepted judgments require verified authority matching the frozen suite contract. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §8.5] |
| 13 · ACCEPTED | C-GOLD.1.11.17 — NHD-B16EEB-D16 authority-proof choice | Available accepted identity/security patterns: a `recognized_ness` SACL session, a BAI purpose-bound artifact including `extended:<purpose_id>`, or their combination. | Gates this place: a recorded judgment must carry verifiable authority of the accepted mode required by its frozen suite. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] |

SUB-PARTS: C-GOLD.1.6.2.1 — ness_meaning_judgment authority; C-GOLD.1.6.2.2 — deterministic_checker authority; C-GOLD.1.6.2.3 — Held-out judgment authority boundary; C-GOLD.1.6.2.4 — Model assistance carries no authority; C-GOLD.1.6.2.5 — Annotation provenance supplements verified authority

### C-GOLD.1.6.2.1 — ness_meaning_judgment authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The ness_meaning_judgment authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — All sealed-gold cases and B24 meaning-dependent cases; the accepted NHD-B16EEB-D16 requirement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Requires event-time proof under accepted §25 mechanisms that Ness performed this recorded judgment act. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified proof of this judgment act. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Use an annotator name alone or treat a token’s own successful consumed state as refusal. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Until NHD-B16EEB-D16 is accepted every Ness judgment is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.1 — Authority absent: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.2 — Authority unverifiable: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.3 — Wrong required proof kind: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.4 — Not Ness: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.5 — Token expired at consume time: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.6 — Token revoked at consume time: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.7 — Token purpose mismatch: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.8 — Token previously consumed: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.9 — Consumption receipt missing: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.10 — Consumption receipt unreadable: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.11 — Consumption receipt mismatch: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.12 — Consumption receipt contradictory: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.13 — Session proof invalid at commit: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.1.14 — Judgment proof choice unset: Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.5 — judgment-authority requirement: The proof has the required kind, purpose and scope, and proves Ness at the required event time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2 — E1-bound judgment authority | All sealed-gold cases and B24 meaning-dependent cases; the accepted NHD-B16EEB-D16 requirement. | Requires event-time proof under accepted §25 mechanisms that Ness performed this recorded judgment act. | A verified proof of this judgment act. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.2.1.1 — Authority absent | The authority reference is absent. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.2.1.2 — Authority unverifiable | The authority reference cannot be verified. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.2.1.3 — Wrong required proof kind | The proof is not of the NHD-B16EEB-D16-required kind. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.2.1.4 — Not Ness | The proof does not establish Ness. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.2.1.5 — Token expired at consume time | The token was expired at its consume time. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.2.1.6 — Token revoked at consume time | The token was revoked at its consume time. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.2.1.7 — Token purpose mismatch | The token’s purpose does not match the accepted judging purpose. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.6.2.1.8 — Token previously consumed | The token was consumed before this judgment’s own consumption. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.6.2.1.9 — Consumption receipt missing | The required receipt is missing. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.6.2.1.10 — Consumption receipt unreadable | The required receipt is unreadable. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.6.2.1.11 — Consumption receipt mismatch | The required receipt does not match this judgment. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.6.2.1.12 — Consumption receipt contradictory | The required receipt evidence is contradictory. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.6.2.1.13 — Session proof invalid at commit | The required session state was not fresh and valid at commit time. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.6.2.1.14 — Judgment proof choice unset | NHD-B16EEB-D16 has not been accepted. | The accepted authority requirement must be satisfied. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.2.1.1 — Authority absent; C-GOLD.1.6.2.1.2 — Authority unverifiable; C-GOLD.1.6.2.1.3 — Wrong required proof kind; C-GOLD.1.6.2.1.4 — Not Ness; C-GOLD.1.6.2.1.5 — Token expired at consume time; C-GOLD.1.6.2.1.6 — Token revoked at consume time; C-GOLD.1.6.2.1.7 — Token purpose mismatch; C-GOLD.1.6.2.1.8 — Token previously consumed; C-GOLD.1.6.2.1.9 — Consumption receipt missing; C-GOLD.1.6.2.1.10 — Consumption receipt unreadable; C-GOLD.1.6.2.1.11 — Consumption receipt mismatch; C-GOLD.1.6.2.1.12 — Consumption receipt contradictory; C-GOLD.1.6.2.1.13 — Session proof invalid at commit; C-GOLD.1.6.2.1.14 — Judgment proof choice unset

### C-GOLD.1.6.2.1.1 — Authority absent
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authority absent rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The authority reference is absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The authority reference is absent. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.2 — Authority unverifiable
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Authority unverifiable rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The authority reference cannot be verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The authority reference cannot be verified. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.3 — Wrong required proof kind
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Wrong required proof kind rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The proof is not of the NHD-B16EEB-D16-required kind. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The proof is not of the NHD-B16EEB-D16-required kind. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.4 — Not Ness
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Not Ness rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The proof does not establish Ness. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The proof does not establish Ness. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.5 — Token expired at consume time
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Token expired at consume time rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The token was expired at its consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The token was expired at its consume time. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.6 — Token revoked at consume time
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Token revoked at consume time rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The token was revoked at its consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The token was revoked at its consume time. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.7 — Token purpose mismatch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Token purpose mismatch rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The token’s purpose does not match the accepted judging purpose. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The token’s purpose does not match the accepted judging purpose. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.8 — Token previously consumed
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Token previously consumed rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The token was consumed before this judgment’s own consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The token was consumed before this judgment’s own consumption. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.9 — Consumption receipt missing
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Consumption receipt missing rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The required receipt is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The required receipt is missing. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.10 — Consumption receipt unreadable
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Consumption receipt unreadable rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The required receipt is unreadable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The required receipt is unreadable. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.11 — Consumption receipt mismatch
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Consumption receipt mismatch rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The required receipt does not match this judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The required receipt does not match this judgment. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.12 — Consumption receipt contradictory
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Consumption receipt contradictory rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The required receipt evidence is contradictory. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The required receipt evidence is contradictory. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.13 — Session proof invalid at commit
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Session proof invalid at commit rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The required session state was not fresh and valid at commit time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | The required session state was not fresh and valid at commit time. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.1.14 — Judgment proof choice unset
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Judgment proof choice unset rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — NHD-B16EEB-D16 has not been accepted. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Refuses the proposed Ness judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Commit the judgment on this invalid authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; its output remains unjudged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.1 — ness_meaning_judgment authority: The accepted authority requirement must be satisfied. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | NHD-B16EEB-D16 has not been accepted. | Refuses the proposed Ness judgment. | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.2 — deterministic_checker authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The deterministic_checker authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted E1 checker identity/configuration/version and this check’s execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Requires the exact declared checker configuration identity and version plus its execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — An authorized deterministic checker finding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Use another checker, version or configuration. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Another checker/version/configuration or a missing execution record refuses the judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.2.2.1 — checker configuration identity: Records the exact checker configuration identity declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.2.2 — checker version: Records the exact version declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.2.2.3 — check execution record: Records the execution record of this check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.10.6 — judgment_authority_ref: Exact accepted E1 checker binding and an execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2 — E1-bound judgment authority | The accepted E1 checker identity/configuration/version and this check’s execution record. | Requires the exact declared checker configuration identity and version plus its execution record. | An authorized deterministic checker finding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.2.2.1 — checker configuration identity | The accepted E1 checker identity/configuration/version and this check’s execution record. | All checker-authority requirements apply to this member. | An authorized deterministic checker finding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.2.2.2 — checker version | The accepted E1 checker identity/configuration/version and this check’s execution record. | All checker-authority requirements apply to this member. | An authorized deterministic checker finding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.2.2.3 — check execution record | The accepted E1 checker identity/configuration/version and this check’s execution record. | All checker-authority requirements apply to this member. | An authorized deterministic checker finding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.2.2.1 — checker configuration identity | The exact checker configuration identity declared in accepted E1. | The accepted E1 binding and execution record match. | The checker configuration identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.2.2.2 — checker version | The exact version declared in accepted E1. | The accepted E1 binding and execution record match. | The checker version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.2.2.3 — check execution record | The execution record of this check. | The accepted E1 binding and execution record match. | The check execution record member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.2.2.1 — checker configuration identity; C-GOLD.1.6.2.2.2 — checker version; C-GOLD.1.6.2.2.3 — check execution record

### C-GOLD.1.6.2.2.1 — checker configuration identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The checker configuration identity member of deterministic_checker authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact checker configuration identity declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact checker configuration identity declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The checker configuration identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute an undeclared checker binding or omit the execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused when the checker binding differs or the execution record is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: The accepted E1 binding and execution record match. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: All checker-authority requirements apply to this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.2 — deterministic_checker authority | The exact checker configuration identity declared in accepted E1. | Records the exact checker configuration identity declared in accepted E1. | The checker configuration identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.2.2 — checker version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The checker version member of deterministic_checker authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact version declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact version declared in accepted E1. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The checker version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute an undeclared checker binding or omit the execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused when the checker binding differs or the execution record is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: The accepted E1 binding and execution record match. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: All checker-authority requirements apply to this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.2 — deterministic_checker authority | The exact version declared in accepted E1. | Records the exact version declared in accepted E1. | The checker version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.2.3 — check execution record
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The check execution record member of deterministic_checker authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — The execution record of this check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records the execution record of this check. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — The check execution record member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute an undeclared checker binding or omit the execution record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused when the checker binding differs or the execution record is missing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: The accepted E1 binding and execution record match. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2.2 — deterministic_checker authority: All checker-authority requirements apply to this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2.2 — deterministic_checker authority | The execution record of this check. | Records the execution record of this check. | The check execution record member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.3 — Held-out judgment authority boundary
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Held-out judgment authority boundary rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Held-out cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Requires the authority defined by an accepted held-out policy under NHD-B16EEB-D7; that policy is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No held-out E9 while its authority is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Assume sealed-gold authority for held-out cases. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Held-out judgments are refused while their authority policy is unset. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — An accepted held-out policy must define judgment authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2 — E1-bound judgment authority | Held-out cases. | Requires the authority defined by an accepted held-out policy under NHD-B16EEB-D7; that policy is unset. | No held-out E9 while its authority is unset. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.4 — Model assistance carries no authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Model assistance carries no authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — Optional model_assist_ref. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records model assistance only as assistance. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — No judgment authority from the model. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Count model assistance as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A model-only E9 is refused with judgment_refused_authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.10.6 — judgment_authority_ref: A separate verified authority reference is required; a model-only E9 is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2 — E1-bound judgment authority | Optional model_assist_ref. | Records model assistance only as assistance. | No judgment authority from the model. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.2.5 — Annotation provenance supplements verified authority
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Annotation provenance supplements verified authority rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Takes in: ACCEPTED — human_annotation provenance and a verified authority reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Does: ACCEPTED — Records provenance in addition to verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Gives out: ACCEPTED — Annotation provenance plus verified authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Must never: ACCEPTED — Treat an annotator name alone as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Bare-name authority is refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.3.10.6 — judgment_authority_ref: The authority reference is independently verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.2 — E1-bound judgment authority | human_annotation provenance and a verified authority reference. | Records provenance in addition to verified authority. | Annotation provenance plus verified authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.3 — Linked protected-judgment protocol
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Linked protected-judgment protocol rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Commits the claim first; when BAI is required it separately consumes and flushes its receipt; O-APPEND then atomically commits only E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Linked durable stages; the flushed BAI receipt is the authorization commit point. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Describe O-JUDGE as one atomic transaction, let O-APPEND consume authority, or trust an earlier proof check without commit-time re-verification. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — O-APPEND re-verifies the bound receipt or session reference before E9 commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim: Commits the one-winner authorization claim before touching a token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt: BAI rechecks, consumes only that token and flushes bai_token_consumed; durable receipt marks authorization committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16: O-APPEND re-verifies proof and atomically commits E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-BAI — Biometric Authorization Interface (§25.6): BAI rechecks immediately before consumption; C-GOLD.1.5.2.13 — O-APPEND [proposed]: O-APPEND re-verifies proof and enforces CAS-1/CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.9.8 — EB-8 — Protected judgment: EB-8 contains linked recoverable stages, with only E9 + E16 atomic. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.6 — O-JUDGE [proposed]: Defines the linked protected stages owned by O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | Commits the claim first; when BAI is required it separately consumes and flushes its receipt; O-APPEND then atomically commits only E9 + E16 under CAS-1 and CAS-3. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | Commits the claim first; when BAI is required it separately consumes and flushes its receipt; O-APPEND then atomically commits only E9 + E16 under CAS-1 and CAS-3. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.4.2 — Winning-token consumption order | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.4.3 — E9 durable receipt binding | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.7 — Pre-receipt crash rule | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.4.8 — In-process receipt-write failure | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.6.4.11 — Head breach after a durable receipt | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.6.4.12 — Orphaned durable receipt | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.6.4.13 — Later invalid consumption proof | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 14 · ACCEPTED | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 15 · ACCEPTED | C-GOLD.1.6.5.4 — Later discovery of invalid session proof | O-JUDGE, its claim, conditional BAI receipt and E9/E16 append. | The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. | Linked durable stages; the flushed BAI receipt is the authorization commit point. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim; C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt; C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16

### C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Protected stage 1 — commit the claim step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — A new protected O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Commits the one-winner authorization claim before touching a token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The winning claimed record. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Touch a token before the claim or treat the claim as authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A losing claimant consumes nothing. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.2 — Winning-token consumption order: Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: Exactly one claim wins the authorization scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Each real operation owns exactly one terminal/log; claim transitions are canonical state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Commits the one-winner authorization claim before touching a token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.3 — Linked protected-judgment protocol | A new protected O-JUDGE. | Commits the one-winner authorization claim before touching a token. | The winning claimed record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Protected stage 2 — BAI receipt step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token, if the selected option requires BAI. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — BAI rechecks, consumes only that token and flushes bai_token_consumed; durable receipt marks authorization committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A durable receipt and consumed_pending_commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Report success before the receipt is durable or perform this stage in SACL-only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No valid durable receipt means no committed authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: The selected option requires BAI and consume-time checks pass. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.2 — Winning-token consumption order: Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI reruns the consume-time checks immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Each real operation owns exactly one terminal/log; claim transitions are canonical state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: A durable bound receipt advances the claim to consumed_pending_commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.3 — Linked protected-judgment protocol | The winning claim’s attached token, if the selected option requires BAI. | BAI rechecks, consumes only that token and flushes bai_token_consumed; durable receipt marks authorization committed. | A durable receipt and consumed_pending_commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Protected stage 3 — commit E9 and E16 step. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The bound durable receipt or required fresh SACL reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — O-APPEND re-verifies proof and atomically commits E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A committed E9 with its scope entry. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Consume authority or first verify it only inside O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable proof or failed domain comparison prevents commitment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.9.8 — EB-8 — Protected judgment: Both CAS comparisons and the selected proof requirements hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: Commits the claim first; when BAI is required it separately consumes and flushes its receipt; O-APPEND then atomically commits only E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append: This compare condition must hold for the E9 + E16 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend: This compare condition must hold for the E9 + E16 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The E1-bound proof must be present and verifiable at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.7 — Protected-judgment log ownership: Each real operation owns exactly one terminal/log; claim transitions are canonical state only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed]: The named E9/E16 commit advances the claim to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): O-APPEND re-verifies proof and atomically commits E9 + E16 under CAS-1 and CAS-3. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.3 — Linked protected-judgment protocol | The bound durable receipt or required fresh SACL reference. | O-APPEND re-verifies proof and atomically commits E9 + E16 under CAS-1 and CAS-3. | A committed E9 with its scope entry. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.3 — E9 durable receipt binding | bai_token_consumed identity, integrity and the claim it was consumed for. | The bound receipt verifies before E9 commits. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4 — Conditional BAI artifact proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Conditional BAI artifact proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — NHD-B16EEB-D16 selecting a one-time BAI artifact. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Follows claim → flushed bai_token_consumed receipt → committed E9 + E16; only the flushed receipt proves durable consumption after a crash. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — One receipt-bound authorized judgment when all conditional requirements hold. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Choose a BAI purpose/scope, reconstruct tokens, reuse consumption or substitute token presence for a receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replay is refused; missing proof prevents commit; later invalid committed proof makes the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: Requires valid, unexpired, unrevoked, unconsumed, purpose-matched status and exact judgment-operation or approved judging-scope binding; BAI reruns both checks immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.2 — Winning-token consumption order: Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: Binds E9 to that durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.4 — Consumed is successful authorization state: Preserves the valid judgment; currentness remains about ledger heads. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.5 — One token per judgment: Uses one token for one judgment unless an accepted NHD-B16EEB-D16 option explicitly selects a separately defined session-scoped mechanism. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.6 — BAI replay and reuse refusal: Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.7 — Pre-receipt crash rule: After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.8 — In-process receipt-write failure: Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion: The losing O-APPEND ends lost_race_technical; a B9-admitted new O-APPEND uses a new operation ID and unchanged E9 key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.11 — Head breach after a durable receipt: Does not force stale E9; records the contradiction, marks judgment_indeterminate and closes the claim closed_after_breach linked to that contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.12 — Orphaned durable receipt: Records the orphaned receipt; commits nothing and leaves the judgment unavailable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.13 — Later invalid consumption proof: Makes an uncommitted judgment unavailable; if already committed, makes its chain judgment_indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — Applies only if accepted NHD-B16EEB-D16 selects this option. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | NHD-B16EEB-D16 selecting a one-time BAI artifact. | Follows claim → flushed bai_token_consumed receipt → committed E9 + E16; only the flushed receipt proves durable consumption after a crash. | One receipt-bound authorized judgment when all conditional requirements hold. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.6 — Conditional combined BAI and SACL proof | NHD-B16EEB-D16 selecting a one-time BAI artifact. | The full BAI lifecycle applies to this same judgment. | One receipt-bound authorized judgment when all conditional requirements hold. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | The winning claim’s attached token, if the selected option requires BAI. | The selected option requires BAI and consume-time checks pass. | A durable receipt and consumed_pending_commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-BAI.20 — Conditional evaluation-judgment proof producer | The winning proposed `judgment_authorization_claim`, its attached token and the exact accepted judging purpose/scope, if such an option is selected. | Supplies the already-defined conditional claim/receipt/commit sequence. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: C-GOLD.1.6.4.1 — BAI consume-time validity checks; C-GOLD.1.6.4.2 — Winning-token consumption order; C-GOLD.1.6.4.3 — E9 durable receipt binding; C-GOLD.1.6.4.4 — Consumed is successful authorization state; C-GOLD.1.6.4.5 — One token per judgment; C-GOLD.1.6.4.6 — BAI replay and reuse refusal; C-GOLD.1.6.4.7 — Pre-receipt crash rule; C-GOLD.1.6.4.8 — In-process receipt-write failure; C-GOLD.1.6.4.9 — Post-receipt forward completion; C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion; C-GOLD.1.6.4.11 — Head breach after a durable receipt; C-GOLD.1.6.4.12 — Orphaned durable receipt; C-GOLD.1.6.4.13 — Later invalid consumption proof

### C-GOLD.1.6.4.1 — BAI consume-time validity checks
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The BAI consume-time validity checks rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token and its BAI pending record/challenge. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Requires valid, unexpired, unrevoked, unconsumed, purpose-matched status and exact judgment-operation or approved judging-scope binding; BAI reruns both checks immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A consume-time-valid token bound no wider than the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Trust checks performed earlier or broaden the scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failing authority condition refuses the judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.1 — valid token condition: The attached token is valid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.2 — unexpired token condition: The attached token is unexpired at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.3 — unrevoked token condition: The attached token is unrevoked at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.4 — unconsumed token condition: The token has not already been consumed before this judgment’s consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.5 — purpose matched token condition: The purpose equals the accepted NHD-B16EEB-D16 judging purpose. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.1.6 — judgment or approved scope bound token condition: The pending record/challenge binds this exact O-JUDGE or the NHD-B16EEB-D16-approved judging scope, nothing wider. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-BAI — Biometric Authorization Interface (§25.6): BAI checks validity and exact purpose/scope immediately before consuming. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Requires valid, unexpired, unrevoked, unconsumed, purpose-matched status and exact judgment-operation or approved judging-scope binding; BAI reruns both checks immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | The winning claim’s attached token and its BAI pending record/challenge. | Requires valid, unexpired, unrevoked, unconsumed, purpose-matched status and exact judgment-operation or approved judging-scope binding; BAI reruns both checks immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.1.1 — valid token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.4.1.2 — unexpired token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.4.1.3 — unrevoked token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.4.1.4 — unconsumed token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.1.5 — purpose matched token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.4.1.6 — judgment or approved scope bound token condition | The winning claim’s attached token and its BAI pending record/challenge. | BAI rechecks this condition immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | The winning claim’s attached token and its BAI pending record/challenge. | BAI reruns the consume-time checks immediately before consumption. | A consume-time-valid token bound no wider than the accepted scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 9 · ACCEPTED | C-BAI.20.1 — Judgment consume-time checks | The winning attached token and its pending-record/challenge binding. | Gates this place: all six canonical token conditions must hold now. | Nothing in this card. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: C-GOLD.1.6.4.1.1 — valid token condition; C-GOLD.1.6.4.1.2 — unexpired token condition; C-GOLD.1.6.4.1.3 — unrevoked token condition; C-GOLD.1.6.4.1.4 — unconsumed token condition; C-GOLD.1.6.4.1.5 — purpose matched token condition; C-GOLD.1.6.4.1.6 — judgment or approved scope bound token condition

### C-GOLD.1.6.4.1.1 — valid token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The valid token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The attached token is valid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The attached token is valid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The attached token is valid. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.1.2 — unexpired token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The unexpired token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The attached token is unexpired at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The attached token is unexpired at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The attached token is unexpired at consume time. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.1.3 — unrevoked token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The unrevoked token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The attached token is unrevoked at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The attached token is unrevoked at consume time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The attached token is unrevoked at consume time. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.1.4 — unconsumed token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The unconsumed token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The token has not already been consumed before this judgment’s consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The token has not already been consumed before this judgment’s consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The token has not already been consumed before this judgment’s consumption. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.1.5 — purpose matched token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The purpose matched token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The purpose equals the accepted NHD-B16EEB-D16 judging purpose. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The purpose equals the accepted NHD-B16EEB-D16 judging purpose. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The purpose equals the accepted NHD-B16EEB-D16 judging purpose. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.1.6 — judgment or approved scope bound token condition
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The judgment or approved scope bound token condition rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The winning claim’s attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The pending record/challenge binds this exact O-JUDGE or the NHD-B16EEB-D16-approved judging scope, nothing wider. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The stated consume-time condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Rely on an earlier check or consume outside the accepted scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A failed condition refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — The pending record/challenge binds this exact O-JUDGE or the NHD-B16EEB-D16-approved judging scope, nothing wider. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.1 — BAI consume-time validity checks: BAI rechecks this condition immediately before consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.1 — BAI consume-time validity checks | The winning claim’s attached token. | The pending record/challenge binds this exact O-JUDGE or the NHD-B16EEB-D16-approved judging scope, nothing wider. | The stated consume-time condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.2 — Winning-token consumption order
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Winning-token consumption order rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The committed winning claim and its attached token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — BAI verifies purpose on every consume call; accepted single-use consumption makes the token permanently unusable afterward. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — One ordered protected judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Report consumption success before its receipt is durable or consume a losing claim’s token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Only the winning claim’s attached token may be consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.3 — One-winner judgment-authorization scope: The one-winner claim precedes BAI consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | The committed winning claim and its attached token. | Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. | One ordered protected judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | The committed winning claim and its attached token. | Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. | One ordered protected judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | The committed winning claim and its attached token. | Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. | One ordered protected judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.3 — E9 durable receipt binding
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The E9 durable receipt binding rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — bai_token_consumed identity, integrity and the claim it was consumed for. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Binds E9 to that durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — An immutable receipt-bound E9 authority reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Use reusable presence of the original token as authorization. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing, unreadable, mismatched or contradictory proof prevents commit or makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.4.3.1 — bai_token_consumed identity: Records the durable consumption receipt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.3.2 — receipt integrity: Records the integrity reference of that receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.3.3 — consumed-for claim: Records the exact claim for which the token was consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16: The bound receipt verifies before E9 commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Binds E9 to that durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | bai_token_consumed identity, integrity and the claim it was consumed for. | Binds E9 to that durable receipt. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.3.1 — bai_token_consumed identity | bai_token_consumed identity, integrity and the claim it was consumed for. | The exact durable receipt binding governs this member. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.4.3.2 — receipt integrity | bai_token_consumed identity, integrity and the claim it was consumed for. | The exact durable receipt binding governs this member. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.4.3.3 — consumed-for claim | bai_token_consumed identity, integrity and the claim it was consumed for. | The exact durable receipt binding governs this member. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.7.1.8.1 — durable receipt identity | bai_token_consumed identity, integrity and the claim it was consumed for. | The durable receipt binding must verify. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.7.1.8.2 — durable receipt integrity | bai_token_consumed identity, integrity and the claim it was consumed for. | The durable receipt binding must verify. | An immutable receipt-bound E9 authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.4.3.1 — bai_token_consumed identity | The durable consumption receipt’s identity. | The receipt matches this judgment and verifies at commit. | The bai_token_consumed identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.4.3.2 — receipt integrity | The integrity reference of that receipt. | The receipt matches this judgment and verifies at commit. | The receipt integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.6.4.3.3 — consumed-for claim | The exact claim for which the token was consumed. | The receipt matches this judgment and verifies at commit. | The consumed-for claim member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 10 · ACCEPTED | C-BAI.20.2 — Judgment durable receipt | The token attached to the winning committed claim and its exact purpose/scope binding. | Takes this place's change: supplies the receipt identity, integrity and exact claim binding. | Supplies the receipt identity, integrity and exact claim binding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB-D16] |

SUB-PARTS: C-GOLD.1.6.4.3.1 — bai_token_consumed identity; C-GOLD.1.6.4.3.2 — receipt integrity; C-GOLD.1.6.4.3.3 — consumed-for claim

### C-GOLD.1.6.4.3.1 — bai_token_consumed identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The bai_token_consumed identity member of E9 durable receipt binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable consumption receipt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records the durable consumption receipt’s identity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The bai_token_consumed identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Use original-token presence in place of durable proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Invalid proof makes the judgment unavailable, or its already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The receipt matches this judgment and verifies at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The exact durable receipt binding governs this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.3 — E9 durable receipt binding | The durable consumption receipt’s identity. | Records the durable consumption receipt’s identity. | The bai_token_consumed identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.3.2 — receipt integrity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt integrity member of E9 durable receipt binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The integrity reference of that receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records the integrity reference of that receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The receipt integrity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Use original-token presence in place of durable proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Invalid proof makes the judgment unavailable, or its already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The receipt matches this judgment and verifies at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The exact durable receipt binding governs this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.3 — E9 durable receipt binding | The integrity reference of that receipt. | Records the integrity reference of that receipt. | The receipt integrity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.3.3 — consumed-for claim
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The consumed-for claim member of E9 durable receipt binding. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The exact claim for which the token was consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records the exact claim for which the token was consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The consumed-for claim member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Use original-token presence in place of durable proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Invalid proof makes the judgment unavailable, or its already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The receipt matches this judgment and verifies at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.3 — E9 durable receipt binding: The exact durable receipt binding governs this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.3 — E9 durable receipt binding | The exact claim for which the token was consumed. | Records the exact claim for which the token was consumed. | The consumed-for claim member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.4 — Consumed is successful authorization state
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Consumed is successful authorization state rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The token’s consumed state from this judgment’s own successful consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Preserves the valid judgment; currentness remains about ledger heads. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No retroactive invalidation from successful consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Refuse or later invalidate the judgment merely because this token is consumed. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Missing, unreadable, mismatched or contradictory proof is separately unavailable or judgment_indeterminate; the own-consumption success state is not such a failure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.4.3 — Authoritative current result: Ledger-head currentness, not the post-consumption token state, governs availability for new checks. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Preserves the valid judgment; currentness remains about ledger heads. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | The token’s consumed state from this judgment’s own successful consumption. | Preserves the valid judgment; currentness remains about ledger heads. | No retroactive invalidation from successful consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.5 — One token per judgment
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The One token per judgment rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — A one-time token and this judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Uses one token for one judgment unless an accepted NHD-B16EEB-D16 option explicitly selects a separately defined session-scoped mechanism. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No reusable token authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Invent a session-scoped lease or scoped artifact. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Replay/reuse is refused as judgment_refused_authority, non-retryably, and logged. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Any different scope must be explicitly selected and separately defined by accepted NHD-B16EEB-D16. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | A one-time token and this judgment. | Uses one token for one judgment unless an accepted NHD-B16EEB-D16 option explicitly selects a separately defined session-scoped mechanism. | No reusable token authority. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.6 — BAI replay and reuse refusal
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The BAI replay and reuse refusal rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — A second O-JUDGE presents a token with an existing receipt, or BAI reports it consumed, expired or revoked. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A refused and logged O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Reuse a prior consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — judgment_refused_authority; non-retryable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-BAI — Biometric Authorization Interface (§25.6): A token already consumed before this judgment, expired or revoked cannot authorize this O-JUDGE. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | A second O-JUDGE presents a token with an existing receipt, or BAI reports it consumed, expired or revoked. | Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. | A refused and logged O-JUDGE. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.8 — CR-33 — BAI option: replay / reuse of a consumed, expired, or revoked token | A second O-JUDGE presents a token with an existing receipt, or BAI reports it consumed, expired or revoked. | Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. | A refused and logged O-JUDGE. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.7 — Pre-receipt crash rule
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Pre-receipt crash rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Crash after claim, after validation, or during/immediately after in-memory consumption, with no valid durable receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Recovery may reference a genuinely pre-existing BAI event only; missing BAI history is never proof that a consume attempt occurred. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Failed authorization and an eligible no-receipt release; a later attempt needs a new flow, token, O-JUDGE and linked new claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reconstruct/resurrect/reuse the original token, consume it during recovery, or create/backfill any BAI event. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Treat missing BAI history as evidence that a consume attempt occurred. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No receipt means no committed authorization; unverifiable evidence is resolved by lookup, never assumed absent. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Release requires durable non-success and positive proof that no valid durable receipt exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Release is allowed only after durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | Crash after claim, after validation, or during/immediately after in-memory consumption, with no valid durable receipt. | After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. | Failed authorization and an eligible no-receipt release; a later attempt needs a new flow, token, O-JUDGE and linked new claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.6 — CR-31 — BAI option: crash before the durable receipt (after claim, after validation, or during/after in-memory consumption) | Crash after claim, after validation, or during/immediately after in-memory consumption, with no valid durable receipt. | After restart the original in-memory token is gone; no authority was committed; O-JUDGE reaches judgment_authorization_failed with one log; release is linked only after its durable non-success and positive no-receipt proof. | Failed authorization and an eligible no-receipt release; a later attempt needs a new flow, token, O-JUDGE and linked new claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.8 — In-process receipt-write failure
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The In-process receipt-write failure rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — Receipt write fails or cannot be verified in the same process, including possible in-memory consumption. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — No reused uncertain token. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Retry that token or reconstruct BAI state from bridge records. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Authorization fails; contradictory/unreadable receipt evidence cannot establish the positive no-receipt proof for release. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: The release rule requires durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.4 — Claim state released: Release is allowed only after durable non-success and positive no-receipt proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | Receipt write fails or cannot be verified in the same process, including possible in-memory consumption. | Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. | No reused uncertain token. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.10 — CR-35 — BAI option: receipt-write failure in-process (possible in-memory consumption) | Receipt write fails or cannot be verified in the same process, including possible in-memory consumption. | Treats the uncertain token as terminal and never retries it; O-JUDGE reaches judgment_authorization_failed; no-receipt release follows only with its release proofs; a new token and new O-JUDGE are required. | No reused uncertain token. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9 — Post-receipt forward completion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Post-receipt forward completion rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — A durable flushed receipt exists before E9 commits. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Consume again, fabricate a judgment, lose/duplicate/redirect authorization or permit a competing successor. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Orphaned receipt commits nothing; unreadable/contradictory proof is indeterminate until lookup; a head breach refuses stale E9 and closes the receipt-bearing claim after breach. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.1 — receipt chain: The receipt is bound to the intended judgment chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.2 — receipt expected head: The receipt matches the claim’s expected judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.3 — receipt E9 content identity: The receipt binds the exact E9 content identity named by the claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.4 — receipt purpose and scope: The receipt has the required accepted purpose and scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.5 — receipt token: The receipt names the token attached to the winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.4.9.6 — receipt integrity check: The receipt integrity is verifiable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — Receipt chain, expected head, E9 content identity, purpose/scope, token and integrity all verify. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed]: The receipt-bearing claim fences the exact judgment scope during recovery. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.1 — judgment_authorization_claim [proposed]: Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | A durable flushed receipt exists before E9 commits. | Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.4.9.1 — receipt chain | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.4.9.2 — receipt expected head | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.4.9.3 — receipt E9 content identity | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.4.9.4 — receipt purpose and scope | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.4.9.5 — receipt token | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.4.9.6 — receipt integrity check | A durable flushed receipt exists before E9 commits. | Every named receipt binding must verify before forward completion. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed] | A durable flushed receipt exists before E9 commits. | Receipt-bound forward completion verifies this claim binding before committing the exact named E9. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.7.1.4 — e9_content_identity [proposed] | A durable flushed receipt exists before E9 commits. | Receipt-bound forward completion verifies this claim binding before committing the exact named E9. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 10 · ACCEPTED | C-GOLD.1.7.1.2 — judgment_chain_key [proposed] | A durable flushed receipt exists before E9 commits. | Receipt-bound forward completion verifies this claim binding before committing the exact named E9. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 11 · ACCEPTED | C-GOLD.1.7.1.8 — durable_receipt_ref [proposed] | A durable flushed receipt exists before E9 commits. | Receipt-bound forward completion verifies this claim binding before committing the exact named E9. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 12 · ACCEPTED | C-GOLD.1.7.8.2 — Pending after authority consumption | A durable flushed receipt exists before E9 commits. | Recovery may complete only this exact named E9. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| 13 · ACCEPTED | C-GOLD.1.7.9.7 — CR-32 — BAI option: crash after flushed receipt, before E9 commit | A durable flushed receipt exists before E9 commits. | Keeps consumed_pending_commit fenced; verifies the receipt and forward-completes exactly the winning claim’s named E9 once through O-APPEND. | Exactly that receipt-bound E9 and E16, or a preserved blocking contradiction. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.4.9.1 — receipt chain; C-GOLD.1.6.4.9.2 — receipt expected head; C-GOLD.1.6.4.9.3 — receipt E9 content identity; C-GOLD.1.6.4.9.4 — receipt purpose and scope; C-GOLD.1.6.4.9.5 — receipt token; C-GOLD.1.6.4.9.6 — receipt integrity check

### C-GOLD.1.6.4.9.1 — receipt chain
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt chain rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt is bound to the intended judgment chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.2 — judgment_chain_key [proposed]: The receipt is bound to the intended judgment chain. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt is bound to the intended judgment chain. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9.2 — receipt expected head
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt expected head rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt matches the claim’s expected judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed]: The receipt matches the claim’s expected judgment head. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt matches the claim’s expected judgment head. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9.3 — receipt E9 content identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt E9 content identity rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt binds the exact E9 content identity named by the claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.4 — e9_content_identity [proposed]: The receipt binds the exact E9 content identity named by the claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt binds the exact E9 content identity named by the claim. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9.4 — receipt purpose and scope
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt purpose and scope rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt has the required accepted purpose and scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed]: The receipt has the required accepted purpose and scope. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt has the required accepted purpose and scope. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9.5 — receipt token
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt token rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt names the token attached to the winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.7 — attached_token_ref [proposed]: The receipt names the token attached to the winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt names the token attached to the winning claim. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.9.6 — receipt integrity check
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The receipt integrity check rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The durable receipt and winning claim. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The receipt integrity is verifiable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verified forward-completion condition. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Redirect the receipt to another judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Mismatched/unreadable/contradictory proof blocks commitment and remains indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.7.1.8.2 — durable receipt integrity: The receipt integrity is verifiable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4.9 — Post-receipt forward completion: Every named receipt binding must verify before forward completion. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4.9 — Post-receipt forward completion | The durable receipt and winning claim. | The receipt integrity is verifiable. | A verified forward-completion condition. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Unrelated ledger movement during forward completion rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The receipt-bound E9 loses only the scope-ledger CAS-1 race. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — The losing O-APPEND ends lost_race_technical; a B9-admitted new O-APPEND uses a new operation ID and unchanged E9 key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Retry of only the E9/E16 append under B9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Re-establish or consume authorization again. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Without B9 admission no new O-APPEND proceeds. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.5.6.7 — Committed B9 R1 admission: B9 admission governs the new O-APPEND. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.5.2.13 — O-APPEND [proposed]: A lost CAS-1 race ends that O-APPEND; B9 may admit a new O-APPEND with unchanged E9 key/content. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | The receipt-bound E9 loses only the scope-ledger CAS-1 race. | The losing O-APPEND ends lost_race_technical; a B9-admitted new O-APPEND uses a new operation ID and unchanged E9 key/content. | Retry of only the E9/E16 append under B9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.13 — CR-38 — Unrelated ledger movement during forward completion | The receipt-bound E9 loses only the scope-ledger CAS-1 race. | The losing O-APPEND ends lost_race_technical; a B9-admitted new O-APPEND uses a new operation ID and unchanged E9 key/content. | Retry of only the E9/E16 append under B9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.11 — Head breach after a durable receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Head breach after a durable receipt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Takes in: ACCEPTED — The judgment head changed contrary to the receipt-bearing claim’s fence. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Does: ACCEPTED — Does not force stale E9; records the contradiction, marks judgment_indeterminate and closes the claim closed_after_breach linked to that contradiction. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Gives out: ACCEPTED — Preserved receipt and a non-replaceable receipt-bearing closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Must never: ACCEPTED — Reapply the receipt, admit a replacement claim, consume another token or extend the chain absent a future accepted resolution policy. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The scope and chain remain blocked; no such resolution policy exists. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed]: Preserves the consumed receipt in the non-replaceable breach closure. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | The judgment head changed contrary to the receipt-bearing claim’s fence. | Does not force stale E9; records the contradiction, marks judgment_indeterminate and closes the claim closed_after_breach linked to that contradiction. | Preserved receipt and a non-replaceable receipt-bearing closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed] | The judgment head changed contrary to the receipt-bearing claim’s fence. | Only a recorded judgment-head integrity breach ends a receipt-bearing claim this way. | Preserved receipt and a non-replaceable receipt-bearing closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.7.9.14 — CR-39 — Judgment head changed contrary to the fence (integrity breach) during forward completion | The judgment head changed contrary to the receipt-bearing claim’s fence. | Does not force stale E9; records the contradiction, marks judgment_indeterminate and closes the claim closed_after_breach linked to that contradiction. | Preserved receipt and a non-replaceable receipt-bearing closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed] | A consumed_pending_commit claim whose named E9 became unusable because the judgment head breached its fence. | A receipt-bearing head-integrity breach is recorded. | A receipt-bearing, non-replaceable breach closure. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.12 — Orphaned durable receipt
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Orphaned durable receipt rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — A durable receipt’s claim is absent or does not match. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records the orphaned receipt; commits nothing and leaves the judgment unavailable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No committed judgment from that receipt. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Use that receipt for any other judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Nothing commits; contradictory claim/receipt evidence makes the scope and chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Contradictory claim/receipt evidence is preserved and makes scope and chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | A durable receipt’s claim is absent or does not match. | Records the orphaned receipt; commits nothing and leaves the judgment unavailable. | No committed judgment from that receipt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.4.13 — Later invalid consumption proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Later invalid consumption proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Missing, unreadable, mismatched or contradictory consumption proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Makes an uncommitted judgment unavailable; if already committed, makes its chain judgment_indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Unavailable or judgment_indeterminate according to commit state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Treat invalid proof as usable authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — No usable judgment until lookup verifies the proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.4 — Conditional BAI artifact proof | Missing, unreadable, mismatched or contradictory consumption proof. | Makes an uncommitted judgment unavailable; if already committed, makes its chain judgment_indeterminate until verified by lookup. | Unavailable or judgment_indeterminate according to commit state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | Missing, unreadable, mismatched or contradictory consumption proof. | Makes an uncommitted judgment unavailable; if already committed, makes its chain judgment_indeterminate until verified by lookup. | Unavailable or judgment_indeterminate according to commit state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5 — Conditional SACL session proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Conditional SACL session proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — NHD-B16EEB-D16 selecting recognized-Ness session proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — At O-JUDGE commit verifies the required state was fresh and valid then, and records an immutable event-time reference in E9. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A judgment authorized by the required valid commit-time session proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute a stale earlier assessment or erase valid judgment merely because the session later ends. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Invalid proof at judgment time refuses the judgment or makes a committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: Verifies the NHD-B16EEB-D16-required state is fresh and valid at that moment inside EB-8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: Records all three in E9 as immutable proof of the event-time fact. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.3 — Ordinary later session expiry: Preserves judgment validity as a fact about its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.4 — Later discovery of invalid session proof: Marks the committed chain judgment_indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — Applies only under an accepted NHD-B16EEB-D16 SACL option; no BAI consumption stage exists for SACL-only. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | NHD-B16EEB-D16 selecting recognized-Ness session proof. | At O-JUDGE commit verifies the required state was fresh and valid then, and records an immutable event-time reference in E9. | A judgment authorized by the required valid commit-time session proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.6 — Conditional combined BAI and SACL proof | NHD-B16EEB-D16 selecting recognized-Ness session proof. | The full SACL commit-time lifecycle applies to this same judgment. | A judgment authorized by the required valid commit-time session proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.5.1 — SACL validity at judgment commit; C-GOLD.1.6.5.2 — Immutable SACL event-time reference; C-GOLD.1.6.5.3 — Ordinary later session expiry; C-GOLD.1.6.5.4 — Later discovery of invalid session proof

### C-GOLD.1.6.5.1 — SACL validity at judgment commit
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The SACL validity at judgment commit rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The required SACL/SIA identity/session assessment at E9 commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The source gives a fresh, non-stale recognized_ness assessment for the Ness stream as an example of the state named by NHD-B16EEB-D16; the accepted option still determines the actual requirement. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Verifies the NHD-B16EEB-D16-required state is fresh and valid at that moment inside EB-8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — Verified event-time identity state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Trust an earlier assessment that has become invalid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — State not fresh/valid at commit refuses authority. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.5.1.1 — Commit-time invalidation: speaker change: Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.1.2 — Commit-time invalidation: stale SIA: Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.1.3 — Commit-time invalidation: spoofing suspicion: Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.1.4 — Commit-time invalidation: session end: Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.1.5 — Commit-time invalidation: security event: Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.2.3.5 — judgment-authority requirement: The accepted proof requirement determines the required state and invalidating conditions. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Verifies the NHD-B16EEB-D16-required state is fresh and valid at that moment inside EB-8. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5 — Conditional SACL session proof | The required SACL/SIA identity/session assessment at E9 commit. The source gives a fresh, non-stale recognized_ness assessment for the Ness stream as an example of the state named by NHD-B16EEB-D16; the accepted option still determines the actual requirement. | Verifies the NHD-B16EEB-D16-required state is fresh and valid at that moment inside EB-8. | Verified event-time identity state. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.5.1.1 — Commit-time invalidation: speaker change | The accepted §25 speaker change condition invalidates the required state at commit. | The required state must be fresh and valid at commit. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.5.1.2 — Commit-time invalidation: stale SIA | The accepted §25 stale SIA condition invalidates the required state at commit. | The required state must be fresh and valid at commit. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.5.1.3 — Commit-time invalidation: spoofing suspicion | The accepted §25 spoofing suspicion condition invalidates the required state at commit. | The required state must be fresh and valid at commit. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.5.1.4 — Commit-time invalidation: session end | The accepted §25 session end condition invalidates the required state at commit. | The required state must be fresh and valid at commit. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.5.1.5 — Commit-time invalidation: security event | The accepted §25 security event condition invalidates the required state at commit. | The required state must be fresh and valid at commit. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | SACL/SIA assessment identity, version and the timestamp checked at judgment commit. | The reference proves the required valid state at the commit moment. | A verifiable event-time reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 8 · ACCEPTED | C-GOLD.1.6.5.3 — Ordinary later session expiry | Later ordinary expiry, session closure or passage of time after a validly recorded judgment. | The original judgment proof was fresh and valid at its commit moment. | The committed judgment remains valid. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 9 · ACCEPTED | C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes | SACL option: session later expires or closes | The original judgment proof was fresh and valid at its commit moment. | Committed judgment unaffected | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.5.1.1 — Commit-time invalidation: speaker change; C-GOLD.1.6.5.1.2 — Commit-time invalidation: stale SIA; C-GOLD.1.6.5.1.3 — Commit-time invalidation: spoofing suspicion; C-GOLD.1.6.5.1.4 — Commit-time invalidation: session end; C-GOLD.1.6.5.1.5 — Commit-time invalidation: security event

### C-GOLD.1.6.5.1.1 — Commit-time invalidation: speaker change
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Commit-time invalidation: speaker change rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted §25 speaker change condition invalidates the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Ignore a commit-time invalidation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; later discovery of invalidity at judgment time makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The required state must be fresh and valid at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | The accepted §25 speaker change condition invalidates the required state at commit. | Rejects this proof as not fresh/valid at judgment time. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.1.2 — Commit-time invalidation: stale SIA
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Commit-time invalidation: stale SIA rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted §25 stale SIA condition invalidates the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Ignore a commit-time invalidation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; later discovery of invalidity at judgment time makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The required state must be fresh and valid at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | The accepted §25 stale SIA condition invalidates the required state at commit. | Rejects this proof as not fresh/valid at judgment time. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.1.3 — Commit-time invalidation: spoofing suspicion
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Commit-time invalidation: spoofing suspicion rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted §25 spoofing suspicion condition invalidates the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Ignore a commit-time invalidation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; later discovery of invalidity at judgment time makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The required state must be fresh and valid at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | The accepted §25 spoofing suspicion condition invalidates the required state at commit. | Rejects this proof as not fresh/valid at judgment time. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.1.4 — Commit-time invalidation: session end
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Commit-time invalidation: session end rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted §25 session end condition invalidates the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Ignore a commit-time invalidation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; later discovery of invalidity at judgment time makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The required state must be fresh and valid at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | The accepted §25 session end condition invalidates the required state at commit. | Rejects this proof as not fresh/valid at judgment time. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.1.5 — Commit-time invalidation: security event
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Commit-time invalidation: security event rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The accepted §25 security event condition invalidates the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Rejects this proof as not fresh/valid at judgment time. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Ignore a commit-time invalidation. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The judgment is refused; later discovery of invalidity at judgment time makes an already committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The required state must be fresh and valid at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): No authorized E9 under this invalid proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.1 — SACL validity at judgment commit | The accepted §25 security event condition invalidates the required state at commit. | Rejects this proof as not fresh/valid at judgment time. | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.2 — Immutable SACL event-time reference
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Immutable SACL event-time reference rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — SACL/SIA assessment identity, version and the timestamp checked at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records all three in E9 as immutable proof of the event-time fact. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — A verifiable event-time reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Replace the commit-time fact with later session state. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unreadable, mismatched, contradictory or commit-time-invalid proof makes the committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: ACCEPTED — C-GOLD.1.6.5.2.1 — SACL/SIA assessment identity: Records identity of the assessment verified at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.2.2 — assessment version: Records version of that assessment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fed by: ACCEPTED — C-GOLD.1.6.5.2.3 — verified commit timestamp: Records the commit timestamp against which the assessment was verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The reference proves the required valid state at the commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.3.19 — Evaluation privacy and access: Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Records all three in E9 as immutable proof of the event-time fact. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5 — Conditional SACL session proof | SACL/SIA assessment identity, version and the timestamp checked at judgment commit. | Records all three in E9 as immutable proof of the event-time fact. | A verifiable event-time reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.6.5.2.1 — SACL/SIA assessment identity | SACL/SIA assessment identity, version and the timestamp checked at judgment commit. | The immutable event-time proof includes this member. | A verifiable event-time reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 3 · ACCEPTED | C-GOLD.1.6.5.2.2 — assessment version | SACL/SIA assessment identity, version and the timestamp checked at judgment commit. | The immutable event-time proof includes this member. | A verifiable event-time reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 4 · ACCEPTED | C-GOLD.1.6.5.2.3 — verified commit timestamp | SACL/SIA assessment identity, version and the timestamp checked at judgment commit. | The immutable event-time proof includes this member. | A verifiable event-time reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 5 · ACCEPTED | C-GOLD.1.6.5.2.1 — SACL/SIA assessment identity | Identity of the assessment verified at judgment commit. | The reference verifies the required state at commit. | The SACL/SIA assessment identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 6 · ACCEPTED | C-GOLD.1.6.5.2.2 — assessment version | Version of that assessment. | The reference verifies the required state at commit. | The assessment version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 7 · ACCEPTED | C-GOLD.1.6.5.2.3 — verified commit timestamp | The commit timestamp against which the assessment was verified. | The reference verifies the required state at commit. | The verified commit timestamp member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: C-GOLD.1.6.5.2.1 — SACL/SIA assessment identity; C-GOLD.1.6.5.2.2 — assessment version; C-GOLD.1.6.5.2.3 — verified commit timestamp

### C-GOLD.1.6.5.2.1 — SACL/SIA assessment identity
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The SACL/SIA assessment identity member of Immutable SACL event-time reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Identity of the assessment verified at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records identity of the assessment verified at judgment commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The SACL/SIA assessment identity member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute later session state for the recorded commit-time proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable or originally invalid proof makes the committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The reference verifies the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The immutable event-time proof includes this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | Identity of the assessment verified at judgment commit. | Records identity of the assessment verified at judgment commit. | The SACL/SIA assessment identity member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.2.2 — assessment version
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The assessment version member of Immutable SACL event-time reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Version of that assessment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records version of that assessment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The assessment version member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute later session state for the recorded commit-time proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable or originally invalid proof makes the committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The reference verifies the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The immutable event-time proof includes this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | Version of that assessment. | Records version of that assessment. | The assessment version member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.2.3 — verified commit timestamp
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The verified commit timestamp member of Immutable SACL event-time reference. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — The commit timestamp against which the assessment was verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Records the commit timestamp against which the assessment was verified. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The verified commit timestamp member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Substitute later session state for the recorded commit-time proof. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Unverifiable or originally invalid proof makes the committed chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The reference verifies the required state at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5.2 — Immutable SACL event-time reference: The immutable event-time proof includes this member. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | The commit timestamp against which the assessment was verified. | Records the commit timestamp against which the assessment was verified. | The verified commit timestamp member. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.3 — Ordinary later session expiry
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Ordinary later session expiry rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Later ordinary expiry, session closure or passage of time after a validly recorded judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Preserves judgment validity as a fact about its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — The committed judgment remains valid. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Retroactively erase a valid judgment because time passed or its session ended. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — A later discovery of proof invalid at judgment time, unlike ordinary expiry, makes the chain judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.5.1 — SACL validity at judgment commit: The original judgment proof was fresh and valid at its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Preserves judgment validity as a fact about its commit moment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5 — Conditional SACL session proof | Later ordinary expiry, session closure or passage of time after a validly recorded judgment. | Preserves judgment validity as a fact about its commit moment. | The committed judgment remains valid. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.9 — CR-34 — SACL option: session later expires or closes | Later ordinary expiry, session closure or passage of time after a validly recorded judgment. | Preserves judgment validity as a fact about its commit moment. | The committed judgment remains valid. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.5.4 — Later discovery of invalid session proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Later discovery of invalid session proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — Original proof unreadable, mismatched, contradictory or invalid at judgment time, including a security event effective before commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Marks the committed chain judgment_indeterminate until verified by lookup. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — No usable authorized head while proof remains invalid or unverifiable. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Confuse ordinary later expiry with original invalidity. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — The chain is judgment_indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-GOLD.1.6.3 — Linked protected-judgment protocol: The selected option uses linked durable stages; proof is reverified at its actual consumption/commit boundary. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10): An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6.5 — Conditional SACL session proof | Original proof unreadable, mismatched, contradictory or invalid at judgment time, including a security event effective before commit. | Marks the committed chain judgment_indeterminate until verified by lookup. | No usable authorized head while proof remains invalid or unverifiable. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| 2 · ACCEPTED | C-GOLD.1.7.9.5 — CR-28 — A committed E9's authority proof later found unreadable, mismatched, contradictory, or invalid at judgment time | Original proof unreadable, mismatched, contradictory or invalid at judgment time, including a security event effective before commit. | SACL proof invalid at judgment time is also indeterminate; ordinary later expiry is not. | No usable authorized head while proof remains invalid or unverifiable. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.1] [NHD-B16EEB] |

SUB-PARTS: NONE

### C-GOLD.1.6.6 — Conditional combined BAI and SACL proof
Stamp: ACCEPTED    Source: [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

ALONE
- What it is: ACCEPTED — The Conditional combined BAI and SACL proof rule. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Takes in: ACCEPTED — NHD-B16EEB-D16 selecting both proof kinds for the same judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Does: ACCEPTED — Applies both sets of requirements: consumed token with bound durable receipt, and session state verified and immutably referenced at commit. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gives out: ACCEPTED — One judgment satisfying both selected authority requirements. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Must never: ACCEPTED — Let either proof substitute for the other or apply proofs to different judgments. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Fails closed by: ACCEPTED — Either failing causes refusal or indeterminacy under the respective proof lifecycle. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — Both requirements hold for the same judgment within the protected protocol. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.4 — Conditional BAI artifact proof: The full BAI lifecycle applies to this same judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.5 — Conditional SACL session proof: The full SACL commit-time lifecycle applies to this same judgment. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Gated by: ACCEPTED — C-GOLD.1.6.2 — E1-bound judgment authority: The accepted E1-bound authority requirement applies; NHD-B16EEB-D16 remains unset, so Ness judgments are refused. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]
- Changes: ACCEPTED — C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9): Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB]

USED BY
| # | Used in (part ID, and path ID if path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-GOLD.1.6 — Judgment chains and conditional authority proofs | NHD-B16EEB-D16 selecting both proof kinds for the same judgment. | Applies both sets of requirements: consumed token with bound durable receipt, and session state verified and immutably referenced at commit. | One judgment satisfying both selected authority requirements. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

SUB-PARTS: NONE

<!-- END CHAPTER 3-g BEHAVIOR -->

## Continuation and reciprocal entries

Every entry below stays in this piece. The old endpoint is named exactly; no previous card is rewritten.

| Existing owner / endpoint | New counterpart | Relation | Behavior | Source |
|---|---|---|---|---|
| C-GOLD.1 — Promotion evaluation-evidence bridge | C-GOLD.1.6 — Judgment chains and conditional authority proofs | ACCEPTED — SUB-PARTS addition and Fed by continuation | Maintains one current authorized judgment head and verifies the proof selected by NHD-B16EEB-D16 at its event-time boundary. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.7 — trial_attempt_terminal [proposed] (E7) | C-GOLD.1.6.1.1 — Judgment-chain key and creation | ACCEPTED — reciprocal USED BY entry for Fed by | E7 attempt_completed establishes effective completion. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.8 — trial_attempt_resolution [proposed] (E7r) | C-GOLD.1.6.1.1 — Judgment-chain key and creation | ACCEPTED — reciprocal USED BY entry for Fed by | E7r resolved_output_found establishes effective completion. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | C-GOLD.1.6.1.3 — First and later judgment predecessor | ACCEPTED — reciprocal USED BY entry for Gated by | CAS-3 compares the exact expected judgment head before extension. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7 — Current judgment-head set consumed by E10 | ACCEPTED — reciprocal USED BY entry for Changes | Binds E10 to exactly the consumed current judgment-head set. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.2 — evaluation_suite_manifest [proposed] (E1) | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — reciprocal USED BY entry for Fed by | Supplies the case judgment mode and scoring-rule/checker binding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10.6 — judgment_authority_ref | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — reciprocal USED BY entry for Gated by | E9 binds the verifiable authority reference required by that E1 mode. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.6.3 — Linked protected-judgment protocol | ACCEPTED — reciprocal USED BY entry for Changes | Defines the linked protected stages owned by O-JUDGE. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.9.8 — EB-8 — Protected judgment | C-GOLD.1.6.3 — Linked protected-judgment protocol | ACCEPTED — reciprocal USED BY entry for Gated by | EB-8 contains linked recoverable stages, with only E9 + E16 atomic. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.4.3 — Authoritative current result | C-GOLD.1.6.4.4 — Consumed is successful authorization state | ACCEPTED — reciprocal USED BY entry for Gated by | Ledger-head currentness, not the post-consumption token state, governs availability for new checks. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §6.2] [NHD-B16EEB] |
| C-GOLD.1.5.8.1 — CAS-1 ledger compare-and-append | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | ACCEPTED — reciprocal USED BY entry for Gated by | This compare condition must hold for the E9 + E16 commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | ACCEPTED — reciprocal USED BY entry for Gated by | This compare condition must hold for the E9 + E16 commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.5 — Judgment fork | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.6 — Judgment contradiction | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.4.13 — Later invalid consumption proof | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.5.4 — Later discovery of invalid session proof | ACCEPTED — reciprocal USED BY entry for Changes | An indeterminate judgment chain makes the dependent trial/run aggregate and downstream results indeterminate. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.2 — deterministic_checker authority | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.3 — Held-out judgment authority boundary | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.4 — Model assistance carries no authority | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.5 — Annotation provenance supplements verified authority | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4 — Conditional BAI artifact proof | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5 — Conditional SACL session proof | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.6 — Conditional combined BAI and SACL proof | ACCEPTED — reciprocal USED BY entry for Changes | Controls whether the proposed evaluation judgment has acceptable authority; no authority choice is selected here. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.19 — Evaluation privacy and access | C-GOLD.1.6.4.3 — E9 durable receipt binding | ACCEPTED — reciprocal USED BY entry for Gated by | Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.3.19 — Evaluation privacy and access | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | ACCEPTED — reciprocal USED BY entry for Gated by | Records/logs carry identities and integrity references, not copied gold/root/reading text; §7Q precedes §7R; SACL applies where required; access failure is unauthorized. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §5] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.4] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6 — Judgment chains and conditional authority proofs | ACCEPTED — reciprocal USED BY entry for Changes | Maintains one current authorized judgment head and verifies the proof selected by NHD-B16EEB-D16 at its event-time boundary. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.2 — Unique current judgment head | ACCEPTED — reciprocal USED BY entry for Changes | Selects the unique committed E9 with no committed successor, only while no fork or contradiction exists. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.3 — First and later judgment predecessor | ACCEPTED — reciprocal USED BY entry for Changes | The first E9 names none; each later E9 names exactly the current head it extends under CAS-3. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.3.1 — Identical E9 absorption | ACCEPTED — reciprocal USED BY entry for Changes | Absorbs the identical committed E9 without adding another judgment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.1 — Judgment-chain key and creation | ACCEPTED — reciprocal USED BY entry for Changes | Keys the chain by planned_trial_output_key once that output is effectively completed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4.2 — Winning-token consumption order | ACCEPTED — reciprocal USED BY entry for Changes | Commits claimed before touching the token; attaches one token; BAI consumes only that token and flushes bai_token_consumed; advances to consumed_pending_commit; O-APPEND commits receipt-bound E9 + E16; advances to judgment_committed. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4.3 — E9 durable receipt binding | ACCEPTED — reciprocal USED BY entry for Changes | Binds E9 to that durable receipt. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4.1 — BAI consume-time validity checks | ACCEPTED — reciprocal USED BY entry for Changes | Requires valid, unexpired, unrevoked, unconsumed, purpose-matched status and exact judgment-operation or approved judging-scope binding; BAI reruns both checks immediately before consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4.6 — BAI replay and reuse refusal | ACCEPTED — reciprocal USED BY entry for Changes | Refuses judgment_refused_authority non-retryably and logs once; BAI’s duplicate/delayed rejections apply. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1 — SACL validity at judgment commit | ACCEPTED — reciprocal USED BY entry for Changes | Verifies the NHD-B16EEB-D16-required state is fresh and valid at that moment inside EB-8. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.2 — Immutable SACL event-time reference | ACCEPTED — reciprocal USED BY entry for Changes | Records all three in E9 as immutable proof of the event-time fact. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.4.4 — Consumed is successful authorization state | ACCEPTED — reciprocal USED BY entry for Changes | Preserves the valid judgment; currentness remains about ledger heads. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.3 — Ordinary later session expiry | ACCEPTED — reciprocal USED BY entry for Changes | Preserves judgment validity as a fact about its commit moment. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | ACCEPTED — reciprocal USED BY entry for Changes | O-APPEND re-verifies proof and atomically commits E9 + E16 under CAS-1 and CAS-3. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7.1 — Missing judgment head | ACCEPTED — reciprocal USED BY entry for Changes | incomplete | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7.2 — Forked judgment input | ACCEPTED — reciprocal USED BY entry for Changes | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7.3 — Contradictory judgment input | ACCEPTED — reciprocal USED BY entry for Changes | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7.4 — Unverifiable judgment authority | ACCEPTED — reciprocal USED BY entry for Changes | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.7.5 — Judgment integrity failure | ACCEPTED — reciprocal USED BY entry for Changes | indeterminate | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.6.1 — Same E9 identity, different content | ACCEPTED — reciprocal USED BY entry for Changes | judgment_indeterminate for the chain; indeterminate trial, run head and results. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.11 — suite_aggregate_result [proposed] (E10) | C-GOLD.1.6.1.6.2 — E9 bytes do not match identity | ACCEPTED — reciprocal USED BY entry for Changes | judgment_indeterminate for the chain; indeterminate trial, run head and results. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.1 — Authority absent | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.2 — Authority unverifiable | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.3 — Wrong required proof kind | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.4 — Not Ness | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.5 — Token expired at consume time | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.6 — Token revoked at consume time | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.7 — Token purpose mismatch | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.8 — Token previously consumed | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.9 — Consumption receipt missing | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.10 — Consumption receipt unreadable | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.11 — Consumption receipt mismatch | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.12 — Consumption receipt contradictory | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.13 — Session proof invalid at commit | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.2.1.14 — Judgment proof choice unset | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1.1 — Commit-time invalidation: speaker change | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1.2 — Commit-time invalidation: stale SIA | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1.3 — Commit-time invalidation: spoofing suspicion | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1.4 — Commit-time invalidation: session end | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.5.1.5 — Commit-time invalidation: security event | ACCEPTED — reciprocal USED BY entry for Changes | No authorized E9 under this invalid proof. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND [proposed] | C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion | ACCEPTED — reciprocal USED BY entry for Changes | A lost CAS-1 race ends that O-APPEND; B9 may admit a new O-APPEND with unchanged E9 key/content. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.2.6 — O-JUDGE [proposed] | C-GOLD.1.6 — Judgment chains and conditional authority proofs | ACCEPTED — Gated by continuation; reciprocal row on new card | O-JUDGE follows the complete judgment-chain and conditional authority protocol. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.3.10.6 — judgment_authority_ref | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — Gated by continuation; reciprocal row on new card | The recorded authority reference must satisfy the E1-bound judgment mode. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD — Sealed gold sets v1, v2-B (§7C) | C-GOLD.1 — Promotion evaluation-evidence bridge | ACCEPTED — retained SUB-PARTS and Fed by continuation · CY-G | The evaluation-evidence bridge extends C-GOLD and supplies its separate narrow B16 evidence references; the top card names this exact bridge as a sub-part and supplier. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §2.5] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §3] [NHD-B16EEB] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §9] [NHD-B16EEB] |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.3 — Linked protected-judgment protocol | ACCEPTED — reciprocal USED BY entry for Gated by | BAI rechecks immediately before consumption; O-APPEND re-verifies proof and enforces CAS-1/CAS-3. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.4.1 — BAI consume-time validity checks | ACCEPTED — reciprocal USED BY entry for Gated by | BAI checks validity and exact purpose/scope immediately before consuming. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-BAI — Biometric Authorization Interface (§25.6) | C-GOLD.1.6.4.6 — BAI replay and reuse refusal | ACCEPTED — reciprocal USED BY entry for Gated by | A token already consumed before this judgment, expired or revoked cannot authorize this O-JUDGE. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.2.3.5 — judgment-authority requirement | C-GOLD.1.6 — Judgment chains and conditional authority proofs | ACCEPTED — reciprocal USED BY entry for Gated by | NHD-B16EEB-D16 must be accepted before any Ness judgment can commit. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.9.8 — EB-8 — Protected judgment | C-GOLD.1.6.1 — Per-output judgment-chain rules | ACCEPTED — reciprocal USED BY entry for Gated by | Judgments require an effectively completed output and an E1-matching authority reference. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.8.4 — CAS-3 judgment-head compare-and-extend | C-GOLD.1.6.1.2 — Unique current judgment head | ACCEPTED — reciprocal USED BY entry for Gated by | CAS-3 alone advances the unique current judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.9] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.4 — Authorized append-only judgment correction | ACCEPTED — reciprocal USED BY entry for Gated by | The new E9 is authorized and its expected head is the unique current head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10 — evaluation_judgment [proposed] (E9) | C-GOLD.1.6.1.4 — Authorized append-only judgment correction | ACCEPTED — reciprocal USED BY entry for Changes | The new authorized E9 becomes head; the predecessor remains byte-identical. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.2.12 — Per-case scoring binding | C-GOLD.1.6.2 — E1-bound judgment authority | ACCEPTED — reciprocal USED BY entry for Gated by | The proof matches E1’s scoring binding. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.2.3.5 — judgment-authority requirement | C-GOLD.1.6.2.1 — ness_meaning_judgment authority | ACCEPTED — reciprocal USED BY entry for Gated by | The proof has the required kind, purpose and scope, and proves Ness at the required event time. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10.6 — judgment_authority_ref | C-GOLD.1.6.2.2 — deterministic_checker authority | ACCEPTED — reciprocal USED BY entry for Gated by | Exact accepted E1 checker binding and an execution record. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10.6 — judgment_authority_ref | C-GOLD.1.6.2.4 — Model assistance carries no authority | ACCEPTED — reciprocal USED BY entry for Gated by | A separate verified authority reference is required; a model-only E9 is refused. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.3.10.6 — judgment_authority_ref | C-GOLD.1.6.2.5 — Annotation provenance supplements verified authority | ACCEPTED — reciprocal USED BY entry for Gated by | The authority reference is independently verified. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.11] [NHD-B16EEB] |
| C-GOLD.1.5.9.8 — EB-8 — Protected judgment | C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | ACCEPTED — reciprocal USED BY entry for Gated by | Both CAS comparisons and the selected proof requirements hold. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.3 — One-winner judgment-authorization scope | C-GOLD.1.6.4.2 — Winning-token consumption order | ACCEPTED — reciprocal USED BY entry for Gated by | The one-winner claim precedes BAI consumption. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.2 — judgment_chain_key [proposed] | C-GOLD.1.6.4.9.1 — receipt chain | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt is bound to the intended judgment chain. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.3 — expected_previous_judgment_head [proposed] | C-GOLD.1.6.4.9.2 — receipt expected head | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt matches the claim’s expected judgment head. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.4 — e9_content_identity [proposed] | C-GOLD.1.6.4.9.3 — receipt E9 content identity | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt binds the exact E9 content identity named by the claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.5 — d16_purpose_scope_ref [proposed] | C-GOLD.1.6.4.9.4 — receipt purpose and scope | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt has the required accepted purpose and scope. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.7 — attached_token_ref [proposed] | C-GOLD.1.6.4.9.5 — receipt token | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt names the token attached to the winning claim. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.7.1.8.2 — durable receipt integrity | C-GOLD.1.6.4.9.6 — receipt integrity check | ACCEPTED — reciprocal USED BY entry for Gated by | The receipt integrity is verifiable. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.6.7 — Committed B9 R1 admission | C-GOLD.1.6.4.10 — Unrelated ledger movement during forward completion | ACCEPTED — reciprocal USED BY entry for Gated by | B9 admission governs the new O-APPEND [proposed]. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.2.3.5 — judgment-authority requirement | C-GOLD.1.6.5.1 — SACL validity at judgment commit | ACCEPTED — reciprocal USED BY entry for Gated by | The accepted proof requirement determines the required state and invalidating conditions. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |
| C-GOLD.1.5.2.13 — O-APPEND [proposed] | C-GOLD.1.6.3 — Linked protected-judgment protocol | ACCEPTED — reciprocal USED BY entry for Gated by | O-APPEND [proposed] re-verifies proof and enforces CAS-1/CAS-3. | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

### Cross-piece relationships

| Using card | Defining/supplying card | Relation | Source |
|---|---|---|---|
| C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | C-GOLD.1.7.3 — One-winner judgment-authorization scope | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | C-GOLD.1.7.4.3 — Claim state judgment_committed [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.7 — Pre-receipt crash rule | C-GOLD.1.7.4.4 — Claim state released | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.8 — In-process receipt-write failure | C-GOLD.1.7.4.4 — Claim state released | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.11 — Head breach after a durable receipt | C-GOLD.1.7.4.6 — Claim state closed_after_breach [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.9 — Post-receipt forward completion | C-GOLD.1.7.4.2 — Claim state consumed_pending_commit [proposed] | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | C-GOLD.1.7.7 — Protected-judgment log ownership | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.6.3.2 — Protected stage 2 — BAI receipt | C-GOLD.1.7.7 — Protected-judgment log ownership | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.6.3.3 — Protected stage 3 — commit E9 and E16 | C-GOLD.1.7.7 — Protected-judgment log ownership | ACCEPTED — Gated by | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §13.5] [NHD-B16EEB] |
| C-GOLD.1.6.4.7 — Pre-receipt crash rule | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.8 — In-process receipt-write failure | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.4.9 — Post-receipt forward completion | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.13] [NHD-B16EEB] |
| C-GOLD.1.6.3.1 — Protected stage 1 — commit the claim | C-GOLD.1.7.1 — judgment_authorization_claim [proposed] | ACCEPTED — Changes | [05/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md §7.12] [NHD-B16EEB] |

## Register contributions

### NOT DECIDED register

Empty fields below are source-silent boxes, not inferred policy choices. Defined behavior has been placed in its matching box. Accepted mechanics left for later pieces are listed separately.

| Part ID | Field | Value | Why retained |
|---|---|---|---|
| C-GOLD.1.6.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.3.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.4.1 | Fails closed by | NOT DECIDED | The cited text assigns no separate failure outcome to this member or log-ownership boundary; no inferred validator or terminal is added. |
| C-GOLD.1.6.1.4.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.4.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.1.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.6.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.6.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.7.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.7.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.7.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.7.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.1.7.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.8 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.9 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.10 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.11 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.12 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.13 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.1.14 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.2.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.2.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.2.2.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.2.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.2.2.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.2.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.2.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.3.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.3.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.3.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.1.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.1.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.1.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.1.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.1.6 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.3.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.3.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.3.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.3.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.3.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.3.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.7 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.8 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.9.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.9.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.9.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.4 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.9.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.5 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.9.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.9.6 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.10 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.11 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.12 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.4.12 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.4.13 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.1.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.1.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.1.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.1.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.1.5 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.2.1 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.2.1 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.5.2.2 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.2.2 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.5.2.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.2.3 | Changes | NOT DECIDED | The cited text assigns no separate outward state mutation to this member or predicate; its defined member/result remains written in the card. |
| C-GOLD.1.6.5.3 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.5.4 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.6 | Fed by | NOT DECIDED | The cited text names the concrete input in Takes in, but no distinct supplying part for this atomic member or condition. |
| C-GOLD.1.6.2.3 | Held-out authority policy value | NOT DECIDED | NHD-B16EEB-D7 has no accepted value; the refusal while unset is already defined. |
| C-GOLD.1.6.2 | NHD-B16EEB-D16 option, purpose and scope | NOT DECIDED | The accepted bridge defines conditional mechanics but chooses no proof kind, BAI purpose identifier, per-judgment/session scope or new authentication policy. |
| C-GOLD.1.6.1.5 | Judgment-fork resolution policy | NOT DECIDED | No accepted fork-resolution procedure exists; NHD-B16EEB-D10 and D11 do not cover it. |
| C-GOLD.1.6.4.11 | Judgment-head breach resolution policy | NOT DECIDED | No accepted policy permits replacement, second consumption or chain extension after the recorded breach. |

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
| §7.11 | C-GOLD.1.6, C-GOLD.1.6.1, C-GOLD.1.6.1.1, C-GOLD.1.6.1.2, C-GOLD.1.6.1.3, C-GOLD.1.6.1.4, C-GOLD.1.6.1.4.1, C-GOLD.1.6.1.5, C-GOLD.1.6.1.6, C-GOLD.1.6.1.6.1, C-GOLD.1.6.1.6.2, C-GOLD.1.6.1.7, C-GOLD.1.6.1.7.1, C-GOLD.1.6.1.7.2, C-GOLD.1.6.1.7.3, C-GOLD.1.6.1.7.4, C-GOLD.1.6.1.7.5, C-GOLD.1.6.2, C-GOLD.1.6.2.1, C-GOLD.1.6.2.1.1, C-GOLD.1.6.2.1.2, C-GOLD.1.6.2.1.3, C-GOLD.1.6.2.1.4, C-GOLD.1.6.2.1.5, C-GOLD.1.6.2.1.6, C-GOLD.1.6.2.1.7, C-GOLD.1.6.2.1.8, C-GOLD.1.6.2.1.9, C-GOLD.1.6.2.1.10, C-GOLD.1.6.2.1.11, C-GOLD.1.6.2.1.12, C-GOLD.1.6.2.1.13, C-GOLD.1.6.2.1.14, C-GOLD.1.6.2.2, C-GOLD.1.6.2.2.1, C-GOLD.1.6.2.2.2, C-GOLD.1.6.2.2.3, C-GOLD.1.6.2.3, C-GOLD.1.6.2.4, C-GOLD.1.6.2.5, C-GOLD.1.6.3.3, C-GOLD.1.6.4, C-GOLD.1.6.4.13, C-GOLD.1.6.5, C-GOLD.1.6.5.4, C-GOLD.1.6.6 |
| §7.12 | C-GOLD.1.6, C-GOLD.1.6.1, C-GOLD.1.6.1.5, C-GOLD.1.6.1.6, C-GOLD.1.6.2, C-GOLD.1.6.2.1, C-GOLD.1.6.2.2, C-GOLD.1.6.2.3, C-GOLD.1.6.2.4, C-GOLD.1.6.2.5, C-GOLD.1.6.3, C-GOLD.1.6.3.1, C-GOLD.1.6.3.2, C-GOLD.1.6.3.3, C-GOLD.1.6.4, C-GOLD.1.6.4.1, C-GOLD.1.6.4.1.1, C-GOLD.1.6.4.1.2, C-GOLD.1.6.4.1.3, C-GOLD.1.6.4.1.4, C-GOLD.1.6.4.1.5, C-GOLD.1.6.4.1.6, C-GOLD.1.6.4.2, C-GOLD.1.6.4.3, C-GOLD.1.6.4.3.1, C-GOLD.1.6.4.3.2, C-GOLD.1.6.4.3.3, C-GOLD.1.6.4.4, C-GOLD.1.6.4.5, C-GOLD.1.6.4.6, C-GOLD.1.6.4.7, C-GOLD.1.6.4.8, C-GOLD.1.6.4.9, C-GOLD.1.6.4.9.1, C-GOLD.1.6.4.9.2, C-GOLD.1.6.4.9.3, C-GOLD.1.6.4.9.4, C-GOLD.1.6.4.9.5, C-GOLD.1.6.4.9.6, C-GOLD.1.6.4.10, C-GOLD.1.6.4.11, C-GOLD.1.6.4.12, C-GOLD.1.6.4.13, C-GOLD.1.6.5, C-GOLD.1.6.5.1, C-GOLD.1.6.5.1.1, C-GOLD.1.6.5.1.2, C-GOLD.1.6.5.1.3, C-GOLD.1.6.5.1.4, C-GOLD.1.6.5.1.5, C-GOLD.1.6.5.2, C-GOLD.1.6.5.2.1, C-GOLD.1.6.5.2.2, C-GOLD.1.6.5.2.3, C-GOLD.1.6.5.3, C-GOLD.1.6.5.4, C-GOLD.1.6.6 |
| §7.13 | C-GOLD.1.6.1, C-GOLD.1.6.1.5, C-GOLD.1.6.1.6, C-GOLD.1.6.3.1, C-GOLD.1.6.3.2, C-GOLD.1.6.3.3, C-GOLD.1.6.4, C-GOLD.1.6.4.7, C-GOLD.1.6.4.8, C-GOLD.1.6.4.9, C-GOLD.1.6.4.11, C-GOLD.1.6.4.12, C-GOLD.1.6.4.13, C-GOLD.1.6.5.4 |
| §7.2 | C-GOLD.1.6.1.1 |
| §7.9 | C-GOLD.1.6.1.1, C-GOLD.1.6.1.2, C-GOLD.1.6.1.3, C-GOLD.1.6.1.3.1, C-GOLD.1.6.3.3 |
| §13.1 | C-GOLD.1.6.1.3 |
| §5 | C-GOLD.1.6.1.4, C-GOLD.1.6.1.4.1, C-GOLD.1.6.4.3, C-GOLD.1.6.5.2 |
| §13.5 | C-GOLD.1.6.3.1, C-GOLD.1.6.3.2, C-GOLD.1.6.3.3 |
| §13.4 | C-GOLD.1.6.4.3, C-GOLD.1.6.5.2 |
| §6.2 | C-GOLD.1.6.4.4 |

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
§1.3 no history/actions/roles/workflow in this chapter: PASS — checked all 88 behavior cards and their reciprocal entries; runtime judgment authority is retained as machine behavior. Source-status/read accounting remains separate from behavior; no source work-session or audit narrative is imported.
§1.4 every gap written as NOT DECIDED: PASS — every card’s own text and source were reviewed for prohibition, failure and gate placement; 95 source-silent boxes and 4 explicit unchosen values/mechanics are registered. Defined mechanics deferred to later pieces are separately identified, not called undecided. Round 3A: all 77 listed unnamed TOGETHER lines reviewed: 62 disposition 1, 0 disposition 2, 15 disposition 3; no additional unnamed lines found.
§1.5 conflicts marked, none resolved: PASS — the inherited B16 input-3/E11a/E12 distinction remains visible in the source-conflict register; no earlier source or passed chapter is rewritten. V10 remains governing.
§3 exactly one stamp per line: PASS — 838 populated field lines and 225 USED BY rows checked; all new behavior and relations are ACCEPTED from the exact-byte accepted bridge. No box or link is stamped BUILT.
§4 every behavior line cited in the exact format: PASS — all populated field lines and relationship rows carry exact 05/file §section citations and NHD-B16EEB; all section targets resolve. Conditional authority, claim and recovery outcomes were checked against §§7.11–7.13 and §13.1/§13.5 rather than historical audit summaries.
§5.4 one name per thing: PASS — existing endpoint IDs/names are retained, new IDs remain under C-GOLD.1.6 and C-GOLD.1.7, and no new top-level or decision-slot ID is invented. The C-GOLD.1 — Promotion evaluation-evidence bridge SUB-PARTS/Fed by continuation is retained explicitly.
§6 all template fields present, in order, for every part: PASS — all 88 cards have all nine fields in order, ALONE, TOGETHER, USED BY and SUB-PARTS; child references resolve.
§6.3 reciprocity within this chapter: PASS — all 1441 unique forward card relationships in corrected CH03-e/CH03-f/CH03-g/CH03-h checked against USED BY rows or retained continuation entries. Every new disposition-1 reference has its reciprocal in the named card’s own file when that card is in this round, otherwise in the using chapter’s continuation table. Existing step-to-rule links remain; continuation entries stay in their own tables and are not merged at assembly.
§6.4 every decided detail written in, no citation used in place of content: PASS within this piece’s explicit scope — Judgment-chain key, current head, predecessor and correction; fork/contradiction propagation; exact E10 head consumption; E1 authority modes and refusal classes; linked three-stage protocol; every BAI lifecycle item including replay, both receipt-failure cases, forward completion and head breach; SACL event-time fields/invalidations and later-expiry distinction; combined-proof requirements. No open option is selected.
§6.5 sub-parts recursed to the bottom: PASS within this piece’s explicit scope — named record members, proof conditions, failure classes, claim states/transitions, duplicate/replacement gates and protected recovery outcomes have their own cards. No physical storage, digest algorithm, authentication method or policy value is fabricated.
§9 coverage matrix rows added for every file used: PASS — all 145 READ-folder files at the fixed source pin and all 107 V10 heading rows remain accounted for; bridge placement is updated and detailed source landings are listed. The bridge source and acceptance receipt SHA-256 fingerprints are listed in READ RECORD and match the pinned copies.
§10.11 no recommendation, no sentence addressed to Ness: PASS — checked behavior and register contributions; conditional options are source-defined mechanics, not recommendations or selected values.
Files read whole for this chapter: whole-read source credit is inherited from Chapters 3-e/3-f for `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` and its exact acceptance receipt in `04_ACCEPTED_STANDALONE_DESIGNS/`; no fresh whole-read source credit is claimed. The cloned contract and fix-request instructions were reopened; this pair’s scoped source checks and the remaining unread list are recorded in READ RECORD.

This is the producing assistant’s contract check, not an independent audit, acceptance, adoption or implementation authorization. The fixed source pin is 6a7160ba688ba4e433a31899162815df7e2bab17.
