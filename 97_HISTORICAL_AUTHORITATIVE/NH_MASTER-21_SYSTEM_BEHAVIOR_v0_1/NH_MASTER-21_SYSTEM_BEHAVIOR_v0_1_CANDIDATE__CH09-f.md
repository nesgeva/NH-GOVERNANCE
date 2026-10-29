# Chapter 9-f — Group G: C-BGMM

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-f.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers the complete V10 §25.13 maintenance boundary, purposes, factors, protected records, file integrity, rollback, entry/change/relock sequences, state, privacy and immediate audit events. Canonical biometric artifacts and keys remain in CH09-e. Full pairing and recovery-material lifecycles belong to CH09-g, enrollment to CH09-h, Personal Mode mechanics to CH09-i, the complete durable-operation kernel to CH10-b, side paths to CH11 and final registers to CH12. No concrete maintenance timeout, hardware key mechanism, unprovided state vocabulary or record encoding is selected.

[SOURCE CONFLICT] The Companion's embedded security-design §13 says rollback packages are deleted after successful final verification or rollback and securely deleted after startup recovery. V10 §25.13 instead requires sealing and rendering them inaccessible, permanently after verified recovery. The V10 rule is retained; the conflicting Companion wording is neither applied nor edited. [COMP §13. BGMM — Biometric-Gated Maintenance Mode] [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Protected Startup Recovery Worker]

Source-wording variation: V10's `rollback_package` schema names `file_metadata`, while its Rollback paragraph says `prior_metadata`. Both source literals are retained in the restoration description; no second schema field or new mapping is asserted. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Rollback]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.

<!-- BEGIN BEHAVIOR -->

### C-BGMM — Biometric-Gated Maintenance Mode (§25.13)
Stamp: DESIGNED    Source: [V10 §25.13] [MAP C-BGMM]

ALONE
- What it is: DESIGNED — The only authorized path for changing protected N.H code, configuration, security policy and device-trust material, including the restricted emergency-recovery purpose. [V10 §25.13 / What BGMM Is and Is Not] [MAP C-BGMM]
- Takes in: DESIGNED — The exact declared purpose and change, its file scope, the purpose-specific authorization factors, current protected bytes and signed manifest, and relock or integrity-failure signals. [V10 §25.13]
- Does: DESIGNED — Opens only the authorized bounded maintenance window; records and flushes the change before touching a protected file; persists the encrypted rollback package; applies and verifies the declared change through the seven-step sequence; revokes the write token on any relock and rolls back a partial change. It operates offline. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Change Application] [V10 §25.13 / Automatic Relocking] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — Authorized changed files, recorded `hash_after` values, the newly signed manifest and executable signatures, permanent structural change/audit records, or verified restoration of the prior files and signed manifest. [V10 §25.13 / Change Application] [V10 §25.13 / Rollback] [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Enter remotely or through ordinary terminal/editor/script/installer access; widen the declared authority; write immutable memory records; reveal protected content through maintenance; store recovery-code values; or grant code/configuration authority through `emergency_recovery`. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Blocks out-of-scope and immutable writes; triggers immediate rollback after any post-touch step failure; keeps N.H stopped on integrity failure or failed startup recovery until the full normal maintenance authorization path succeeds. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Change Application] [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): supplies maintenance confirmation bound to the exact session and purpose; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the trusted-phone and applicable recovery authority. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Gated by: DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]
- Gated by: DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]
- Gated by: DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]
- Gated by: DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]
- Gated by: DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]
- Gated by: DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B]
- Changes: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): permits only the authorized device-trust or emergency-recovery change within the declared bounded scope. [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BAI — Biometric Authorization Interface (§25.6) | The session and purpose requested by maintenance. | Issues the exact purpose-bound maintenance confirmation artifact. | Another token purpose cannot satisfy the request. | [V10 §25.6] |
| 2 · DESIGNED | C-BAI.3.9.4 — Maintenance confirmation purpose | The maintenance session and declared purpose. | Binds bgmm_confirmation:<session_id>:<purpose> before prompting. | The confirmation remains purpose-specific. | [V10 §25.6 / Purpose Binding] |
| 3 · ACCEPTED | C-7P.2.6 — Strictest-rule and specialist authority boundary | BGMM authority for protected code, configuration, security and device-trust changes. | Retains specialist maintenance authorization rather than ordinary action authority. | A general action level cannot weaken the protected-change boundary. | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] |
| 4 · DESIGNED | C-BGMM.15 — Immediate security audit events | Actual maintenance operations and failures. | Records each real event with immediate flush. | Permanent security history gains structural facts only. | [V10 §25.13 / Immediate Security Audit Events] |
| 5 · DESIGNED | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | The applicable maintenance purpose and factors. | Uses bounded maintenance authority for device-trust changes and emergency recovery. | Code/configuration never become emergency-writable. | [V10 §25.13 / Purpose-Specific Authorization] |
| 6 · DESIGNED | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10), CY-I | The security cycle’s protected-change boundary. | Uses BGMM as the only authorized protected-material change path. | Trust recovery remains within its purpose-specific scope. | [MAP CY-I] [V10 §25.13 / Purpose-Specific Authorization] |

SUB-PARTS: C-BGMM.1 — Narrow maintenance boundary; C-BGMM.2 — Protected purposes and factors; C-BGMM.3 — Permanently unchangeable material; C-BGMM.4 — Normal-path write prevention; C-BGMM.5 — Signed-manifest trust anchor; C-BGMM.6 — Encrypted rollback package; C-BGMM.7 — Protected startup recovery worker; C-BGMM.8 — Maintenance entry sequence; C-BGMM.9 — Exact file-scope enforcement; C-BGMM.10 — Protected change sequence; C-BGMM.11 — Immediate automatic relocking; C-BGMM.12 — Idempotent rollback; C-BGMM.13 — Volatile maintenance session state; C-BGMM.14 — Maintenance privacy; C-BGMM.15 — Immediate security audit events; C-BGMM.16 — Crash, restart and offline behavior; C-BGMM.17 — Unconditional protected-core rules; C-BGMM.18 — Build-time maintenance settings

### C-BGMM.1 — Narrow maintenance boundary
Stamp: DESIGNED    Source: [V10 §25.13 / What BGMM Is and Is Not]

ALONE
- What it is: DESIGNED — Purpose-limited maintenance authority, not a general administrator mode. [V10 §25.13 / What BGMM Is and Is Not]
- Takes in: DESIGNED — The declared protected-material change. [V10 §25.13 / What BGMM Is and Is Not]
- Does: DESIGNED — Restricts maintenance access to what the declared purpose requires; protected files remain read-only outside the authorized path. [V10 §25.13 / What BGMM Is and Is Not]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Permit remote entry, ordinary terminal/editor/script/installer entry at any OS privilege level, broader access, or an override of immutable roots, provenance, privacy or protected architectural safeguards. [V10 §25.13 / What BGMM Is and Is Not]
- Fails closed by: DESIGNED — Keeps protected files read-only outside the authorized maintenance boundary. [V10 §25.13 / What BGMM Is and Is Not]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8 — Maintenance entry sequence | The local-only purpose-limited boundary. | Rejects remote or ordinary-administrator substitutes. | Entry still requires the full declared-factor path. | [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.2 — Protected purposes and factors
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — The five controlled maintenance purposes and their distinct material/factor limits. [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]
- Takes in: DESIGNED — One exact purpose and its declared change. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Distinguishes `code_change`, `configuration_change`, `security_policy_change`, `device_trust_change` and `emergency_recovery`; each uses its own stated factor conjunction and material boundary. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — The applicable authorization requirements and protected-material scope. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Treat a declared emergency purpose as permission to change code or configuration. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — The emergency scope guard blocks code and configuration writes regardless of the declaration. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: records the exact purpose and change before authorization. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2.1 — Code-change purpose | The code_change classification. | Applies its material boundary and factor pair. | Code authority stays purpose-limited. | [V10 §25.13 / Protected Material Boundary] |
| 2 · DESIGNED | C-BGMM.2.2 — Configuration-change purpose | The configuration_change classification. | Limits the purpose to non-code configuration. | Both required factors remain necessary. | [V10 §25.13 / Protected Material Boundary] |
| 3 · DESIGNED | C-BGMM.2.3 — Security-policy-change purpose | The security_policy_change classification. | Applies the security-policy material scope. | The purpose cannot override protected-core rules. | [V10 §25.13 / Protected Material Boundary] |
| 4 · DESIGNED | C-BGMM.2.4 — Device-trust-change purpose | The device_trust_change classification. | Uses the thumbprint-plus-normal-code branch. | Old-phone availability is not a required factor. | [V10 §25.13 / Protected Material Boundary] |
| 5 · DESIGNED | C-BGMM.2.5 — Emergency-recovery purpose | The emergency_recovery classification. | Applies all emergency factors and device-trust scope. | Code and configuration remain unwritable. | [V10 §25.13 / Protected Material Boundary] |
| 6 · DESIGNED | C-BGMM.8 — Maintenance entry sequence | The purpose-specific factor conjunction. | Runs the corresponding entry branch. | Opening follows the complete required factors. | [V10 §25.13 / Purpose-Specific Authorization] |
| 7 · DESIGNED | C-BGMM.8.6 — Scoped maintenance window | The exact purpose's requirements. | Requires the complete conjunction before opening. | A missing factor prevents the window. | [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking] |
| 8 · DESIGNED | C-BGMM.13.5 — Session authorization factors | The purpose's required factors. | Retains the applicable factor state. | One purpose cannot borrow another's authority. | [V10 §25.13 / Purpose-Specific Authorization] |

SUB-PARTS: C-BGMM.2.1 — Code-change purpose; C-BGMM.2.2 — Configuration-change purpose; C-BGMM.2.3 — Security-policy-change purpose; C-BGMM.2.4 — Device-trust-change purpose; C-BGMM.2.5 — Emergency-recovery purpose

### C-BGMM.2.1 — Code-change purpose
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — `code_change`, covering Python source, executable code, `.cursorrules` and engine config. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — Motherbase thumbprint and trusted-phone confirmation for the declared change. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Requires both factors within the declared code-change scope. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Purpose-bounded code-change authorization. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Open code-change authority without either required factor. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Does not authorize the code-change window unless both factors are supplied. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: supplies the controlled purpose/material classification. [V10 §25.13 / Protected Material Boundary]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: local thumbprint is required; C-BGMM.8.3 — Trusted-phone confirmation: the paired phone's explicitly confirmed, BAI-bound result is also required. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.2.2 — Configuration-change purpose
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — `configuration_change`, for non-code behavior configuration files. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — Local thumbprint and trusted-phone confirmation. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Requires both factors for this declared configuration change. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Authority bounded to the declared configuration files. [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / File Scope Enforcement]
- Must never: DESIGNED — Let the configuration purpose bypass the phone confirmation or local thumbprint. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Withholds this maintenance authority when either factor is missing. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: identifies the non-code configuration scope. [V10 §25.13 / Protected Material Boundary]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: requires the local factor; C-BGMM.8.3 — Trusted-phone confirmation: requires the independent phone confirmation. [V10 §25.13 / Purpose-Specific Authorization]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.2.3 — Security-policy-change purpose
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — `security_policy_change`, covering SACL thresholds, anti-spoofing policy and audit retention rules. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — Motherbase thumbprint and trusted-phone confirmation of the declared security-policy change. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Requires the two-factor conjunction before opening that purpose's bounded window. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Authority for the declared security-policy files only. [V10 §25.13 / File Scope Enforcement]
- Must never: DESIGNED — Use a security-policy declaration to override the protected-core safeguards. [V10 §25.13 / What BGMM Is and Is Not]
- Fails closed by: DESIGNED — Does not authorize this window when local thumbprint or phone confirmation is absent. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: identifies the security-policy scope. [V10 §25.13 / Protected Material Boundary]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: the local factor must pass; C-BGMM.8.3 — Trusted-phone confirmation: confirmation of this session and purpose must be present. [V10 §25.13 / Purpose-Specific Authorization]
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its thresholds may change only through the declared authorized security-policy scope. [V10 §25.13 / Protected Material Boundary]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.2.4 — Device-trust-change purpose
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — `device_trust_change`, covering trusted-phone bindings, pairing credentials and recovery-code authority records. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — Motherbase thumbprint and the current Bitwarden normal recovery code for local verification. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Requires those two factors; trusted-phone confirmation is not required because the old phone may be unavailable. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Bounded device-trust-change authority. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Store the recovery-code value in N.H or omit either required factor. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Does not open the device-trust window without the thumbprint and locally verified recovery code. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: supplies the device-trust material boundary. [V10 §25.13 / Protected Material Boundary]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: requires the local biometric factor; C-BGMM.8.4 — Normal recovery-code verification: requires the current Bitwarden code verified locally. [V10 §25.13 / Entering Maintenance Mode]
- Changes: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): permits the specifically authorized trust-record change. [V10 §25.13 / Protected Material Boundary]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-PAIR.3 — Future-phone replacement | The current Bitwarden normal recovery code, Ness's motherbase thumbprint through Maintenance Mode and a new phone. | Gates this place: supplies the bounded normal trust-change authority. | Nothing in this card. | [V10 §25.9] [V10 §25.13 / Purpose-Specific Authorization] |


SUB-PARTS: NONE

### C-BGMM.2.5 — Emergency-recovery purpose
Stamp: DESIGNED    Source: [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — `emergency_recovery`, limited to the accepted device-trust reset. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — Physical motherbase access, thumbprint, the emergency code and the printed recovery sheet together. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Requires that complete conjunction; does not require trusted-phone confirmation; keeps writable scope confined to device-trust records regardless of the declaration. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Emergency authority for device-trust records only. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Permit remote recovery or make code/configuration files writable through this purpose. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — The scope-enforcement guard unconditionally blocks code and configuration changes under emergency recovery. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: defines this restricted purpose. [V10 §25.13 / Protected Material Boundary]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: the local thumbprint is required; C-BGMM.8.5 — Emergency-factor verification: physical access and both emergency materials are required. [V10 §25.13 / Purpose-Specific Authorization]
- Changes: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies only its bounded emergency device-trust authority. [V10 §25.13 / Protected Material Boundary]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-PAIR.4 — Atomic emergency recovery | Simultaneous physical motherbase access, the separate outside-Bitwarden emergency code, physically secure printed sheet and Ness's motherbase thumbprint through BGMM. | Gates this place: authority is limited to device-trust/recovery material, with no code/configuration changes. | Nothing in this card. | [V10 §25.10 / Required Factors] [V10 §25.13 / Purpose-Specific Authorization] |


SUB-PARTS: NONE

### C-BGMM.3 — Permanently unchangeable material
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — The material maintenance cannot directly create, rewrite, delete or correct. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — A proposed write touching roots, readings/provenance, clashes/Person-Box links, audit records, gold records or recovery-code values. [V10 §25.13 / Protected Material Boundary]
- Does: DESIGNED — Preserves existing immutable records and the separate authority of normal governed append paths. [V10 §25.13 / Protected Material Boundary]
- Gives out: DESIGNED — Preserved history; a later normal-path interpretation may supersede an earlier interpretation without altering its record. [V10 §25.13 / Protected Material Boundary]
- Must never: DESIGNED — Treat maintenance access as permission to create, rewrite, delete or correct immutable memory records. [V10 §25.13 / Protected Material Boundary]
- Fails closed by: DESIGNED — Blocks immutable writes through scope enforcement and records `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.9.3 — Immutable-write refusal: blocks and logs a forbidden immutable write. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.3.1 — Sealed-root protection | The immutable-root boundary. | Rejects direct maintenance changes to roots. | Existing sealed roots remain unchanged. | [V10 §25.13 / Protected Material Boundary] |
| 2 · DESIGNED | C-BGMM.3.2 — Reading and provenance protection | The reading/provenance boundary. | Preserves existing readings and provenance. | Only governed later appends remain available. | [V10 §25.13 / Protected Material Boundary] |
| 3 · DESIGNED | C-BGMM.3.3 — Clash and Person-Box-link protection | The clash/link immutability rule. | Keeps earlier clashes and Person-Box links unchanged. | Maintenance supplies no correction shortcut. | [V10 §25.13 / Protected Material Boundary] |
| 4 · DESIGNED | C-BGMM.3.4 — Audit-entry protection | The append-only audit boundary. | Preserves existing security entries. | Actual new events append without altering history. | [V10 §25.13 / Protected Material Boundary] |
| 5 · DESIGNED | C-BGMM.3.5 — Gold-record protection | The protected gold-record boundary. | Keeps gold records outside writable scope. | No direct maintenance rewrite is allowed. | [V10 §25.13 / Protected Material Boundary] |
| 6 · DESIGNED | C-BGMM.3.7 — Normal governed append boundary | The permanent earlier-record boundary. | Allows only normal governed new appends. | Supersession never alters an earlier record. | [V10 §25.13 / Protected Material Boundary] |

SUB-PARTS: C-BGMM.3.1 — Sealed-root protection; C-BGMM.3.2 — Reading and provenance protection; C-BGMM.3.3 — Clash and Person-Box-link protection; C-BGMM.3.4 — Audit-entry protection; C-BGMM.3.5 — Gold-record protection; C-BGMM.3.6 — Recovery-value prohibition; C-BGMM.3.7 — Normal governed append boundary

### C-BGMM.3.1 — Sealed-root protection
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — Permanent protection of immutable roots in the sealed root store. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — An attempted maintenance write to a root. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Does: DESIGNED — Keeps the existing root unchanged even during authorized maintenance. [V10 §25.13 / Protected Material Boundary]
- Gives out: DESIGNED — The preserved root and the blocked-write event when attempted. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Must never: DESIGNED — Create, rewrite, delete or correct a root directly through maintenance. [V10 §25.13 / Protected Material Boundary]
- Fails closed by: DESIGNED — Blocks the write and records `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: the immutable-root boundary remains unconditional. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.3.2 — Reading and provenance protection
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — The immutable boundary for reading records and their provenance. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — An attempted direct maintenance write to those records. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Does: DESIGNED — Preserves existing readings, rereads and provenance; later interpretations can be appended only through normal architecture. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Gives out: DESIGNED — Preserved earlier reading/provenance records. [V10 §25.13 / Protected Material Boundary]
- Must never: DESIGNED — Use maintenance to create, rewrite, delete or correct readings or their provenance. [V10 §25.13 / Protected Material Boundary]
- Fails closed by: DESIGNED — Scope enforcement blocks the write and records `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: maintenance cannot override the reading/provenance boundary. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.3.3 — Clash and Person-Box-link protection
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — Permanent immutability of clash records, Person-Box links and their provenance. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — A direct maintenance write aimed at those records. [MAP C-BGMM]
- Does: DESIGNED — Preserves earlier clash/link records while normal governed append paths remain available. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Gives out: DESIGNED — Unaltered earlier clashes, links and provenance. [V10 §25.13 / Protected Material Boundary]
- Must never: DESIGNED — Directly create, rewrite, delete or correct those records through maintenance. [V10 §25.13 / Protected Material Boundary]
- Fails closed by: DESIGNED — Blocks and logs an attempted immutable write as `bgmm_immutable_write_blocked`. [MAP C-BGMM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: keeps these records outside writable maintenance scope. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.3.4 — Audit-entry protection
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — Append-only security-audit history whose existing entries are immutable. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — An attempted modification of an existing audit entry. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Does: DESIGNED — Preserves prior entries while recording real maintenance events through the authorized append path. [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — Permanent earlier audit history plus the actual new event records. [V10 §0B] [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Delete or alter an audit-log entry. [V10 §25.13 / Protected Material Boundary]
- Fails closed by: DESIGNED — Blocks an immutable-log write and records `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: existing audit records remain outside direct maintenance writes. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15 — Immediate security audit events | The immutable prior-audit boundary. | Appends new events without altering earlier entries. | Existing security history remains preserved. | [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Protected Material Boundary] |

SUB-PARTS: NONE

### C-BGMM.3.5 — Gold-record protection
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — The permanent maintenance boundary around gold-set records. [V10 §25.13 / Protected Material Boundary]
- Takes in: DESIGNED — An attempted direct write to a protected gold record. [MAP C-BGMM]
- Does: DESIGNED — Keeps those records immutable inside and outside maintenance. [V10 §25.13 / Protected Material Boundary]
- Gives out: DESIGNED — Preserved gold-set records. [V10 §25.13 / Protected Material Boundary]
- Must never: DESIGNED — Directly create, rewrite, delete or correct gold records through BGMM. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Fails closed by: DESIGNED — Blocks and logs the attempted immutable write. [MAP C-BGMM]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: gold records stay outside writable maintenance scope. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.3.6 — Recovery-value prohibition
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary]

ALONE
- What it is: DESIGNED — The prohibition on storing recovery-code values in N.H. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Takes in: DESIGNED — Recovery-code verification during the applicable maintenance purpose. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Keeps recovery values out of N.H storage despite authority records being within device-trust scope. [V10 §25.13 / Protected Material Boundary]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Store a recovery-code value in N.H. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.4 — Normal recovery-code verification | The prohibition on stored recovery values. | Verifies the current code without retaining its value. | Recovery authority records contain no raw code. | [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 2 · DESIGNED | C-BGMM.17 — Unconditional protected-core rules | The recovery-value boundary. | Preserves the unconditional storage prohibition. | Maintenance cannot retain recovery-code values. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 3 · DESIGNED | C-BGMM.8.5.2 — Emergency-code verification | The recovery-value storage prohibition. | Verifies the emergency factor without retaining its value. | The emergency code never enters N.H storage. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |

SUB-PARTS: NONE

### C-BGMM.3.7 — Normal governed append boundary
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]

ALONE
- What it is: DESIGNED — The distinction between direct maintenance writes and normal authorized architectural appends. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Takes in: DESIGNED — New roots, readings, rereads, links, revisions and later interpretations submitted through their own governed paths. [MAP C-BGMM]
- Does: DESIGNED — Preserves those append interfaces; a later interpretation may supersede an earlier one while the earlier record remains unchanged. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Gives out: DESIGNED — New records appended through normal architecture without rewriting prior records. [V10 §25.13 / Protected Material Boundary]
- Must never: DESIGNED — Classify authorized architectural appends as non-BGMM tampering, or use their existence to permit direct ungoverned writes to protected files. [MAP C-BGMM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.3 — Permanently unchangeable material: earlier records remain immutable when later records are appended. [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4 — Normal-path write prevention
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Five cooperating layers of tamper resistance and pre-run integrity detection. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — Ordinary user and administrator access attempts, executable modules, protected files, signed manifest and change-log history. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Does: DESIGNED — Combines ACL/service isolation, administrator resistance, code signing, signed-manifest integrity and change-log provenance. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — Blocked ordinary writes and detection of administrator tampering before N.H runs, within the stated physical-attacker limit. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Must never: DESIGNED — Claim universal physical impossibility or guaranteed detection against every sufficiently capable physical attacker. [MAP C-BGMM]
- Fails closed by: DESIGNED — Rejects unsigned/invalid modules and stops N.H on detected integrity failure. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.4.1 — ACL and service isolation | The ordinary-user blocking assignment. | Applies ACLs and nh_system isolation. | Ordinary direct writes are denied. | [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)] |
| 2 · DESIGNED | C-BGMM.4.2 — Administrator-level resistance | The combined integrity-chain context. | Adds administrator resistance beyond ACLs. | The architecture does not claim physical impossibility. | [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)] |
| 3 · DESIGNED | C-BGMM.4.6 — Qualified tamper guarantee | All five layer results. | Applies the qualified combined guarantee. | Detected integrity failure stops N.H. | [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)] |
| 4 · DESIGNED | C-BGMM.17 — Unconditional protected-core rules | Ordinary blocking and qualified tamper protection. | Preserves the protected-core access boundary. | Normal PC access cannot modify protected material. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |

SUB-PARTS: C-BGMM.4.1 — ACL and service isolation; C-BGMM.4.2 — Administrator-level resistance; C-BGMM.4.3 — Executable code signing; C-BGMM.4.4 — Signed-manifest integrity layer; C-BGMM.4.5 — Change-log provenance layer; C-BGMM.4.6 — Qualified tamper guarantee

### C-BGMM.4.1 — ACL and service isolation
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Layer 1: ACLs and `nh_system` account isolation. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — Ordinary user sessions, terminals, editors, scripts and installers attempting protected-file access. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Does: DESIGNED — Blocks their ordinary protected-file writes through ACLs and service isolation. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — Protected files unavailable for ordinary direct modification. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Must never: DESIGNED — Treat ACLs alone as prevention of all administrator or offline-disk tampering. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Fails closed by: DESIGNED — Denies ordinary ungoverned write access. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

TOGETHER
- Fed by: DESIGNED — C-BGMM.4 — Normal-path write prevention: assigns ordinary-user blocking to this layer. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4.2 — Administrator-level resistance
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Layer 2: resistance beyond ACLs against full Windows administrator privileges or offline disk access. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — The boot chain, disk, application-control policy and protected service configuration. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Does: DESIGNED — Uses Secure Boot, TPM-backed boot-chain trust, full-disk encryption, signed application control such as Windows Defender Application Control or equivalent, and protected service configuration to raise tampering cost and detectability. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — Substantially greater administrator-level resistance. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Must never: DESIGNED — Claim that those layers make tampering physically impossible; ownership takeover or OS recovery modification can remain possible. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.4 — Normal-path write prevention: supplies this layer's place in the combined integrity chain. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4.3 — Executable code signing
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Layer 3: all executable N.H code is signed. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — A module and its code signature before loading. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Does: DESIGNED — Verifies signatures before runtime loads a module. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — Rejection of unsigned or invalidly signed modules. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Must never: DESIGNED — Load a module without a valid code signature. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Fails closed by: DESIGNED — Rejects the unsigned or invalidly signed module. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.6 — Re-sign modified executables: supplies the updated executable signatures after an authorized change. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4.4 — Signed-manifest integrity layer
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Layer 4: every protected file is registered in a signed manifest. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — The signed manifest and actual protected files. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Verifies the manifest at startup; a protected file modified outside the authorized path produces a hash mismatch. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — A verified integrity result or detected signature/hash failure. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Start N.H after a failed manifest signature or protected-file hash. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — Stops startup, records the integrity failure and leaves repair to BGMM. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: provides the current signed version and trusted verification basis. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4.5 — Change-log provenance layer
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]

ALONE
- What it is: DESIGNED — Layer 5: append-only provenance of each maintenance change. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — The declared file paths, operations and hashes for the change. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Writes and flushes the change-log entry before the change is applied. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — Permanent pre-change provenance containing structural facts. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Touch the protected file before the change-log entry is flushed, or put file content into that log. [V10 §25.13 / Change Application] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — The protected change cannot proceed without its prior written-and-flushed entry. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.1 — Flush the change-log entry: performs the required pre-change write. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.4.6 — Qualified tamper guarantee
Stamp: DESIGNED    Source: [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)] [MAP C-BGMM]

ALONE
- What it is: DESIGNED — The exact combined tamper guarantee and its physical-attacker limit. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Takes in: DESIGNED — The five protection layers and their integrity results. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Does: DESIGNED — Blocks ordinary user paths; substantially resists administrator tampering and always detects it before N.H runs; recognizes that sufficiently capable physical attackers may bypass some layers. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gives out: DESIGNED — Fail-closed operation whenever an integrity failure is detected. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Must never: DESIGNED — Broaden the administrator detection guarantee into universal detection of every physical attacker. [MAP C-BGMM]
- Fails closed by: DESIGNED — Does not start N.H on a detected integrity failure; the repair path is BGMM. [MAP C-BGMM]

TOGETHER
- Fed by: DESIGNED — C-BGMM.4 — Normal-path write prevention: supplies the combined layer results. [V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible)]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.5 — Signed-manifest trust anchor
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The signed registry of expected hashes and versions for every protected file. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — Protected-file hashes and versions, the authorized signing key and the pinned public verification key. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Signs a new manifest after each authorized change; appends the prior signed version to permanent provenance history; verifies the current signature and every file hash at startup. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The current signed manifest, preserved earlier signed versions and startup integrity results. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Delete prior signed manifests or change the pinned public key merely because the manifest changes. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — Any failed signature or file hash prevents N.H startup, writes an integrity failure and leaves repair to the authorized maintenance path. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BAI.8.1 — Manifest-signing key: signs only authorized versions with the separated hardware-backed key; C-BGMM.5.1 — Expected protected-file hashes: supplies each expected digest; C-BGMM.5.2 — Protected-file versions: supplies the corresponding versions; C-BGMM.5.3 — Pinned public verification key: supplies the hardware-anchored verification basis. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: access to the manifest-signing private key is confined to an authorized BGMM session. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Changes: DESIGNED — C-BGMM.5.4 — Manifest provenance history: appends the prior signed manifest without deleting earlier history. [V10 §25.13 / Signed-Manifest Trust Anchor]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.4.4 — Signed-manifest integrity layer | The current signed manifest and trust basis. | Verifies startup integrity. | Signature/hash failure prevents startup. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 2 · DESIGNED | C-BGMM.5.4 — Manifest provenance history | The previous signed manifest. | Appends it to provenance history. | Earlier signed versions remain preserved. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 3 · DESIGNED | C-BGMM.5.5 — Startup manifest verification | The signed registry and verification basis. | Runs the ordered startup checks. | N.H cannot start on failed integrity. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 4 · DESIGNED | C-BGMM.7 — Protected startup recovery worker | The named prior signed-manifest state. | Restores only that verified prior version. | Automatic recovery gains no new-change authority. | [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 5 · DESIGNED | C-BGMM.10.5 — Update and sign the manifest | The current manifest and authorized update. | Produces its new signed version. | Prior signed provenance is preserved. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 6 · DESIGNED | C-BGMM.12 — Idempotent rollback | The prior signed-manifest target. | Returns it to its verified prior state. | Rollback restores the prior integrity registry. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 7 · DESIGNED | C-BGMM.12.5 — Restore the verified prior manifest | The manifest state being restored. | Installs the verified prior signed version. | Current manifest state returns to its prior version. | [V10 §25.13 / Rollback] |

SUB-PARTS: C-BGMM.5.1 — Expected protected-file hashes; C-BGMM.5.2 — Protected-file versions; C-BGMM.5.3 — Pinned public verification key; C-BGMM.5.4 — Manifest provenance history; C-BGMM.5.5 — Startup manifest verification

### C-BGMM.5.1 — Expected protected-file hashes
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The expected hashes of all protected files in the manifest. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — Each protected file's expected digest after an authorized change. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Change Application]
- Does: DESIGNED — Supplies the expected comparison value for that file's startup verification. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The manifest entry's expected hash. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Let N.H start after any hash mismatch. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.4 — Record the post-change hash: supplies the recorded `hash_after` before the manifest is updated. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | Each expected protected-file digest. | Carries it in the signed registry. | Startup has the expected comparison values. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6] |
| 2 · DESIGNED | C-BGMM.5.5.3 — Verify every protected-file hash | The expected hash for each protected file. | Compares it with the actual file hash. | Any mismatch prevents startup. | [V10 §25.13 / Signed-Manifest Trust Anchor] |

SUB-PARTS: NONE

### C-BGMM.5.2 — Protected-file versions
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The versions of all protected files carried by the manifest. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The version associated with each protected file. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Retains file versions alongside their expected hashes; the source chooses no version encoding. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The protected-file version entries. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | Protected-file version entries. | Retains versions alongside hashes. | The signed registry identifies file versions. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6] |

SUB-PARTS: NONE

### C-BGMM.5.3 — Pinned public verification key
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The pinned public key anchored in the TPM or equivalent hardware-backed trust store. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The manifest signature presented for verification. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Provides the fixed public verification basis when signed manifest versions change. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — A trust anchor for checking the manifest signature. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Change merely because the manifest changes. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — A failed signature keeps N.H stopped, and an unverified prior version is not restored. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | The pinned hardware-backed public key. | Uses it as the fixed verification basis. | Manifest changes do not replace the trust anchor. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6] |
| 2 · DESIGNED | C-BGMM.5.5.2 — Verify the manifest signature | The anchored public verification key. | Checks the current manifest signature. | Failed signatures keep N.H stopped. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 3 · DESIGNED | C-BGMM.12.5 — Restore the verified prior manifest | The pinned public verification basis. | Re-verifies the prior manifest signature. | Unverified prior versions cannot be restored. | [V10 §25.13 / Signed-Manifest Trust Anchor] |

SUB-PARTS: NONE

### C-BGMM.5.4 — Manifest provenance history
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — Append-only history of prior signed manifest versions. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The prior signed manifest when an authorized replacement version is signed. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Appends and preserves the old version for provenance and verified rollback. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The prior signed version required by restoration. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Delete a prior signed manifest from the history. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: hands over the prior signed version on an authorized manifest update. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | The append-only provenance destination. | Appends the prior signed manifest there. | Older versions are never deleted. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 2 · DESIGNED | C-BGMM.6.2.5 — Prior manifest version | The actual prior signed manifest. | Identifies its version in the package. | The restoration reference points to preserved provenance. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 3 · DESIGNED | C-BGMM.12 — Idempotent rollback | The prior signed version. | Restores it after signature verification. | Rollback recovers prior manifest truth. | [V10 §25.13 / Rollback] |
| 4 · DESIGNED | C-BGMM.12.5 — Restore the verified prior manifest | The prior signed bytes. | Re-verifies and restores that version. | The prior manifest replaces the changed current state. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.5.5 — Startup manifest verification
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — Ordered verification before N.H starts. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The current signed manifest, pinned public key and each actual protected file. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Reads the current manifest, verifies its signature against the pinned hardware-backed key, then verifies every protected file hash against its entry. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — A startup integrity result and the applicable immediate security event. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Start N.H when any checked signature or hash fails. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — Prevents startup and records the integrity failure; only BGMM can repair it. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: supplies the signed registry and trust basis. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5.5.1 — Read the current manifest | The current-manifest verification step. | Reads the current signed manifest first. | Signature checking receives the actual current manifest. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 2 · DESIGNED | C-BGMM.15.15 — Integrity-check-failed event | A failed startup integrity result. | Writes the integrity-failure event. | N.H stays stopped for authorized repair. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 3 · DESIGNED | C-BGMM.15.16 — Integrity-check-passed event | A successful integrity result. | Records the structural pass fact. | The actual check has its immediate audit record. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 4 · DESIGNED | C-BGMM.16 — Crash, restart and offline behavior | Startup integrity truth. | Selects recovery or failed-start behavior. | Failed integrity cannot reach normal startup. | [V10 §25.13 / Crash, Restart, Offline Behavior] |
| 5 · DESIGNED | C-BGMM.16.3 — Startup integrity failure | A failed signature or file-hash check. | Blocks startup and records failure. | Only BGMM remains the repair path. | [V10 §25.13 / Signed-Manifest Trust Anchor] |

SUB-PARTS: C-BGMM.5.5.1 — Read the current manifest; C-BGMM.5.5.2 — Verify the manifest signature; C-BGMM.5.5.3 — Verify every protected-file hash

### C-BGMM.5.5.1 — Read the current manifest
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The first startup-verification step. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The current signed manifest. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Reads that manifest for verification. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The manifest to be signature-checked. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Let startup continue with an invalid manifest signature. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5 — Startup manifest verification: establishes this first step and its current-manifest input. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5.5.2 — Verify the manifest signature | The read current signed manifest. | Checks its signature against the pinned key. | An invalid signature blocks startup. | [V10 §25.13 / Signed-Manifest Trust Anchor] |

SUB-PARTS: NONE

### C-BGMM.5.5.2 — Verify the manifest signature
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — The signature check against the pinned hardware-backed public key. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — The read manifest, its signature and the pinned key. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Verifies the signature without changing the public key for a new manifest version. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The signature verification result. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Permit startup after a failed signature check. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — Keeps N.H stopped and records integrity failure when verification fails. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5.1 — Read the current manifest: supplies the current signed bytes; C-BGMM.5.3 — Pinned public verification key: supplies the fixed trust anchor. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5.5.3 — Verify every protected-file hash | Manifest signature verification. | Requires it before relying on file entries. | Unverified manifest data cannot authorize startup. | [V10 §25.13 / Signed-Manifest Trust Anchor] |

SUB-PARTS: NONE

### C-BGMM.5.5.3 — Verify every protected-file hash
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor]

ALONE
- What it is: DESIGNED — Per-file startup verification against the signed manifest. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Takes in: DESIGNED — Actual protected files and their manifest entries. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Compares each protected file hash with its expected manifest hash. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The file-hash verification results. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Allow N.H to start with a failed file-hash check. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — A mismatch keeps N.H stopped, records integrity failure and requires the authorized BGMM repair path. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.1 — Expected protected-file hashes: supplies the per-file comparison values. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: DESIGNED — C-BGMM.5.5.2 — Verify the manifest signature: signature verification precedes reliance on the file entries. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.6 — Encrypted rollback package
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `rollback_package`, the protected full-content restoration record persisted before a protected write. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — `session_id`, `change_description`, `file_entries` and `created_at`; each file entry carries the exact prior bytes and restoration metadata. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Retains one entry per in-scope file; encrypts the package with the separate hardware-backed rollback-sealing key, integrity-protects it with a BGMM-verifiable MAC or signature and persists it before the first write. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — An encrypted, integrity-protected package for exact restoration; after successful final verification or rollback it is sealed and rendered inaccessible. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Expose package content to ordinary users, applications, terminals or normal N.H runtime; log/export either private key; replace exact prior content with hashes alone; or destroy the package after success. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / BGMM-Owned State] [V10 §0B]
- Fails closed by: DESIGNED — No first protected write proceeds before the package is persisted; failed recovery keeps it available to the protected repair path while N.H remains stopped. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.13.1 — Maintenance session identifier: supplies `session_id`; C-BGMM.6.1 — Rollback change description: supplies the declared change for audit linkage; C-BGMM.6.2 — Rollback file entries: supplies exact per-file restoration content; C-BGMM.6.3 — Rollback creation time: records creation before any write. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BAI.8.2 — Rollback-sealing key: only its separated hardware-backed rollback protection is used; C-BGMM.14 — Maintenance privacy: no protected content enters package metadata or audit fields. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.4 — Package sealing and integrity | The complete restoration package. | Encrypts and integrity-protects its contents. | The package is inaccessible to ordinary runtime. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.6.5 — Successful package closure | The protected package after verified use. | Seals it and makes it inaccessible on success. | The preserved package is not destroyed. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 3 · DESIGNED | C-BGMM.7 — Protected startup recovery worker | The expected protected restoration package. | Uses it only within verified bounded recovery. | Automatic access does not become general maintenance. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 4 · DESIGNED | C-BGMM.10.2 — Persist the rollback package | The full-content restoration structure. | Creates and persists it before the write. | The exact prior state is available for rollback. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 5 · DESIGNED | C-BGMM.12 — Idempotent rollback | Exact prior bytes and restoration metadata. | Restores the prior file state idempotently. | A hash-only checkpoint cannot replace the package. | [V10 §25.13 / Rollback] |
| 6 · DESIGNED | C-BGMM.13.11 — Rollback verification checkpoint | The actual encrypted backup. | References it from rollback_checkpoint. | Checkpoint hashes remain references rather than backups. | [V10 §25.13 / BGMM-Owned State] |
| 7 · DESIGNED | C-BGMM.14.2 — Rollback metadata privacy | Package content and metadata surfaces. | Keeps protected bytes separate from structural metadata. | No private content leaks through audit linkage. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 8 · DESIGNED | C-BGMM.16 — Crash, restart and offline behavior | Persistent prior-state restoration material. | Recovers after crash under the protected worker. | Volatile state loss does not erase the backup. | [V10 §25.13 / Crash, Restart, Offline Behavior] |

SUB-PARTS: C-BGMM.6.1 — Rollback change description; C-BGMM.6.2 — Rollback file entries; C-BGMM.6.3 — Rollback creation time; C-BGMM.6.4 — Package sealing and integrity; C-BGMM.6.5 — Successful package closure

### C-BGMM.6.1 — Rollback change description
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `change_description`, the declared change retained for audit linkage. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The declared maintenance change. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Links the package to that declared change using structural description. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The package's audit-linkage description. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Include private content in maintenance descriptions or metadata. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the recorded specific change. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.14.1 — Human-visible and phone descriptions: descriptions cannot carry private content. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6 — Encrypted rollback package | The structural change_description. | Retains the declared change for audit linkage. | Protected content stays outside descriptive metadata. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2 — Rollback file entries
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `file_entries`, one restoration entry per in-scope file. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — `file_path`, `prior_content`, `prior_hash`, `prior_signature` where applicable, `prior_manifest_version` and `file_metadata`. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Preserves the exact prior bytes, verification evidence and metadata required for restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — The complete listed restoration entries inside the protected package. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Substitute hash references for the byte-for-byte backup content. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2.1 — Rollback file path: identifies the file; C-BGMM.6.2.2 — Exact prior file content: supplies the backup bytes; C-BGMM.6.2.3 — Prior-content hash: supplies verification evidence; C-BGMM.6.2.4 — Prior code signature: supplies the signature when applicable; C-BGMM.6.2.5 — Prior manifest version: identifies the prior version; C-BGMM.6.2.6 — File restoration metadata: supplies permissions, timestamps and attributes. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: entries cover the in-scope files only. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / File Scope Enforcement]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6 — Encrypted rollback package | One full restoration entry per in-scope file. | Persists the complete protected content. | Rollback has exact prior bytes and metadata. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.7.3 — Exact recovery scope | The exact listed restoration entries. | Confines automatic recovery to those items. | No arbitrary file or scope expansion is allowed. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 3 · DESIGNED | C-BGMM.13.11.1 — Checkpoint file list | The files represented by restoration entries. | Carries their checkpoint references. | The list still points to the real package. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: C-BGMM.6.2.1 — Rollback file path; C-BGMM.6.2.2 — Exact prior file content; C-BGMM.6.2.3 — Prior-content hash; C-BGMM.6.2.4 — Prior code signature; C-BGMM.6.2.5 — Prior manifest version; C-BGMM.6.2.6 — File restoration metadata

### C-BGMM.6.2.1 — Rollback file path
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `file_path` in a rollback entry. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The path of the in-scope file. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Identifies exactly which file that entry restores. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — The named restoration destination. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Restore a path outside the declared in-scope list. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: only declared in-scope paths may be changed. [V10 §25.13 / File Scope Enforcement]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | The in-scope file_path. | Identifies the exact entry destination. | Restoration remains tied to the listed file. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.2 — Exact prior file content
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `prior_content`, the exact byte-for-byte content before the change. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The file's prior bytes. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Retains those complete bytes inside the encrypted, sealed, integrity-protected package for restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [MAP C-BGMM]
- Gives out: DESIGNED — Exact prior bytes to the authorized restoration boundary. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Expose these bytes through metadata, audit records, ordinary applications, users, terminals or normal runtime. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.6.4 — Package sealing and integrity: exact prior content remains protected within the package. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | Exact byte-for-byte prior_content. | Preserves the full backup bytes. | Hashes alone cannot stand in for restoration content. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.6.2.3 — Prior-content hash | The prior file bytes. | Supplies their SHA-256 verification evidence. | The hash refers to the actual backup content. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 3 · DESIGNED | C-BGMM.12.3 — Restore prior content | Verified exact prior bytes. | Restores them to the listed destination. | An already matching file receives no write. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.3 — Prior-content hash
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `prior_hash`, SHA-256 of `prior_content`. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The exact prior content's digest. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Supplies verification evidence when rollback checks the prior bytes. [V10 §25.13 / Rollback]
- Gives out: DESIGNED — The prior-content comparison hash. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Replace the backup bytes with this verification hash. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: DESIGNED — Failed verification cannot proceed to startup restoration. [V10 §25.13 / Rollback]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2.2 — Exact prior file content: its bytes are the hash's verification subject. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | The prior_hash value. | Retains it with its prior_content. | Restoration has verification evidence as well as bytes. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.12.2 — Verify prior-content bytes | The prior-content SHA-256. | Checks it against the backup bytes. | Failed verification cannot proceed to startup restoration. | [V10 §25.13 / Rollback] |

SUB-PARTS: NONE

### C-BGMM.6.2.4 — Prior code signature
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `prior_signature`, the prior code signature if applicable. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The signature associated with the prior executable content. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Retains that signature for exact restoration where a code signature applies. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Rollback]
- Gives out: DESIGNED — The signature to restore with the prior file. [V10 §25.13 / Rollback]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | The prior code signature when applicable. | Preserves it in the file entry. | Executable restoration retains the prior signature. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.12.4 — Restore prior signature and metadata | The prior_signature value. | Restores it where applicable. | The prior executable signature returns with its file. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.5 — Prior manifest version
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `prior_manifest_version` in each rollback file entry. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The prior signed-manifest version associated with that file. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Identifies the prior manifest version required by restoration. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The reference used to recover the prior signed version from provenance history. [V10 §25.13 / Rollback]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.4 — Manifest provenance history: preserves the actual prior signed version. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | The prior_manifest_version reference. | Includes it with each file entry. | Restoration identifies the required prior signed version. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.12.5 — Restore the verified prior manifest | The referenced prior manifest version. | Retrieves and verifies that signed version. | Rollback restores the correct prior manifest. | [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.6 — File restoration metadata
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `file_metadata`: permissions, timestamps and attributes for exact restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The file's prior permissions, timestamps and attributes. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Preserves those three metadata categories alongside the prior bytes; the Rollback paragraph calls the restored metadata `prior_metadata`. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Rollback]
- Gives out: DESIGNED — The metadata needed for exact restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Expose protected content through metadata. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2.6.1 — Prior permissions: supplies the permission values; C-BGMM.6.2.6.2 — Prior timestamps: supplies the timestamp values; C-BGMM.6.2.6.3 — Prior attributes: supplies the attribute values. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | Permissions, timestamps and attributes. | Preserves file_metadata for exact restoration. | The prior file is more than its content bytes. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.12.4 — Restore prior signature and metadata | The prior file metadata. | Restores its permissions, timestamps and attributes. | The exact prior metadata returns with the file. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: C-BGMM.6.2.6.1 — Prior permissions; C-BGMM.6.2.6.2 — Prior timestamps; C-BGMM.6.2.6.3 — Prior attributes

### C-BGMM.6.2.6.1 — Prior permissions
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — The permissions retained in `file_metadata`. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The prior file permissions. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Preserves them for exact restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — The prior permission values. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2.6 — File restoration metadata | The prior permissions. | Retains them in restoration metadata. | Exact restoration includes permission values. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.6.2 — Prior timestamps
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — The timestamps retained in `file_metadata`. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The file's prior timestamp values. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Carries those values for exact restoration; no timestamp format is selected by the source. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — The preserved timestamps. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2.6 — File restoration metadata | The prior timestamp values. | Keeps them with file_metadata. | Restoration retains the file's earlier timestamps. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.2.6.3 — Prior attributes
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — The attributes retained in `file_metadata`. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The file's prior attribute values. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Retains them as part of the exact-restoration metadata. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — The preserved attributes for restoration. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2.6 — File restoration metadata | The prior attributes. | Preserves them for restoration. | The prior attributes return with the file. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.3 — Rollback creation time
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — `created_at` in the rollback package. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The package creation time, before any write occurs. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Records creation on the pre-write side of the protected change boundary. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — The package's pre-write creation timestamp. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Treat a package created after the first protected write as satisfying the pre-write requirement. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.2 — Persist the rollback package: creates and persists the package before application. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6 — Encrypted rollback package | The pre-write created_at value. | Records when package creation occurred. | Creation remains before any protected write. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.4 — Package sealing and integrity
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages]

ALONE
- What it is: DESIGNED — Hardware-backed encryption and integrity protection of the full rollback content. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The complete rollback package and the separate rollback-sealing key. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Encrypts the package and protects it with a MAC or signature verifiable by BGMM; keeps it inaccessible to ordinary users, applications, terminals and normal runtime. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gives out: DESIGNED — Protected restoration content that must pass integrity checks before recovery restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Derive the rollback key from the manifest-signing key, export either private key, log either key or expose the package to normal access. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Fails closed by: DESIGNED — Recovery cannot restore files unless the protected package passes full integrity verification. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies the full content to protect; C-BAI.8.2 — Rollback-sealing key: supplies the independent hardware-backed protection. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2.2 — Exact prior file content | The encrypted, integrity-protected package boundary. | Keeps exact backup bytes inside it. | Ordinary access cannot expose prior_content. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |
| 2 · DESIGNED | C-BGMM.7.2 — Full package-integrity condition | The package and its integrity protection. | Requires full verification before restoring. | Failed verification halts recovery. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.6.5 — Successful package closure
Stamp: DESIGNED    Source: [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — Sealing and inaccessibility after successful final verification or successful rollback. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — A verified successful change or verified successful rollback. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Seals the package and renders it inaccessible; verified startup rollback renders it permanently inaccessible. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — Preserved sealed package content without ordinary access. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §0B]
- Must never: DESIGNED — Delete the package or make it inaccessible while recovery decryption, verification or restoration has failed. [V10 §0B] [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — A failed recovery halts with the package not made inaccessible yet and N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies the protected package whose successful use has ended. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.12 — Idempotent rollback: successful final verification, or a successful rollback with its verified prior-state result, precedes this closure. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.7.4 — Verified recovery completion | The success-only closure condition. | Seals and permanently restricts the used package. | Unsuccessful recovery cannot take successful closure. | [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.7 — Protected startup recovery worker
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — The minimal protected worker allowed automatic rollback access after a crash or unexpected restart. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — The expected measured-boot record and the protected rollback package. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Decrypts and verifies only under the expected secure/measured boot state; after both boot and package integrity checks pass, restores exactly the listed files, metadata, prior signatures and prior signed manifest. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — Verified prior state, a sealed permanently inaccessible package and `bgmm_rollback_completed`, or a halted recovery with N.H still stopped. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Edit arbitrary files, create a new change, expand scope, export package contents or open a general Maintenance Mode session. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — If decryption, integrity verification or restoration fails, halts without making the package inaccessible; requires the full normal BGMM authorization path while N.H remains stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies the exact bounded restoration material. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.7.1 — Expected measured-boot condition: expected secure/measured boot must match; C-BGMM.7.2 — Full package-integrity condition: the package must pass full verification before restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: restores only the named prior signed version with its verification. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Signed-Manifest Trust Anchor]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.7.5 — Recovery decryption failure | A failed decryption outcome. | Halts recovery without closing the package. | Full normal authorization is required for repair. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 2 · DESIGNED | C-BGMM.11.3 — Restart or crash relock | The bounded startup restoration route. | Runs it after crash revocation. | The old maintenance window is not reopened. | [V10 §25.13 / Crash, Restart, Offline Behavior] |
| 3 · DESIGNED | C-BGMM.12 — Idempotent rollback | The measured-boot and package-integrity boundary. | Keeps automatic rollback inside that boundary. | Recovery adds no new change authority. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 4 · DESIGNED | C-BGMM.15.12 — Rollback-failed event | The actual recovery failure. | Records bgmm_rollback_failed structurally. | N.H stays stopped for authorized repair. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 5 · DESIGNED | C-BGMM.16 — Crash, restart and offline behavior | The protected automatic-recovery conditions. | Requires them after crash/restart. | Unverified restoration never leads to startup. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 6 · DESIGNED | C-BGMM.16.1 — Open-session crash | The verified startup worker. | Restores the prior state after an open-session crash. | State and token authority remain lost. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 7 · DESIGNED | C-BGMM.16.2 — Crash during rollback | The same verified recovery boundary. | Re-runs interrupted rollback within it. | Restart does not expand recovery scope. | [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: C-BGMM.7.1 — Expected measured-boot condition; C-BGMM.7.2 — Full package-integrity condition; C-BGMM.7.3 — Exact recovery scope; C-BGMM.7.4 — Verified recovery completion; C-BGMM.7.5 — Recovery decryption failure; C-BGMM.7.6 — Recovery integrity failure; C-BGMM.7.7 — Recovery restoration failure

### C-BGMM.7.1 — Expected measured-boot condition
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — The expected secure and measured boot state required for automatic package access. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — The current boot state and expected measured-boot record. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Permits recovery access only when the boot state matches the expected record. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — The boot-state condition for bounded package decryption and verification. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Begin restoration outside the required verified boot state. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Withholds automatic restoration when the required boot match does not pass. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.7 — Protected startup recovery worker | The expected measured-boot match. | Requires it for automatic package access. | Unverified boot state cannot begin restoration. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 2 · DESIGNED | C-BGMM.7.3 — Exact recovery scope | A passing secure/measured-boot condition. | Requires it before listed restoration. | Recovery scope does not bypass boot verification. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 3 · DESIGNED | C-BGMM.12.1 — Decrypt the restoration package | The expected boot-state condition. | Limits automatic startup decryption to that state. | Decryption is not ordinary runtime access. | [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.7.2 — Full package-integrity condition
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — Full rollback-package integrity verification before any restoration begins. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — The protected package and its verifiable integrity protection. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Requires full package verification before granting restoration access. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — The package-integrity result. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Restore from a package whose integrity has not passed. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Verification failure halts the worker with N.H stopped and the package not made inaccessible. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.4 — Package sealing and integrity: supplies the encrypted, integrity-protected package. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.7 — Protected startup recovery worker | The full package-integrity result. | Requires a pass before restoration starts. | Failed verification keeps N.H stopped. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 2 · DESIGNED | C-BGMM.7.3 — Exact recovery scope | Verified package integrity. | Restores listed items only after the pass. | An unverified package cannot authorize writes. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 3 · DESIGNED | C-BGMM.7.6 — Recovery integrity failure | The failed verification result. | Halts recovery and retains the package. | Repair needs full normal authorization. | [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.7.3 — Exact recovery scope
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — The recovery worker's exclusive authority to restore the package-listed prior state. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — Exactly the listed files, metadata, prior signatures and prior signed manifest. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Restores those named items and nothing else. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — The listed prior state restored within the package boundary. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Edit arbitrary files, create a change, expand scope, export content or open a general maintenance session. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Stops on restoration failure and leaves N.H stopped for full normal authorization. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2 — Rollback file entries: specifies the exact file-by-file restoration boundary. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.7.1 — Expected measured-boot condition: boot state must pass; C-BGMM.7.2 — Full package-integrity condition: full package verification must pass before restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.7.4 — Verified recovery completion | Successful bounded restoration. | Records completion and seals the package. | Verified prior state exists before startup. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 2 · DESIGNED | C-BGMM.7.7 — Recovery restoration failure | The failed listed-item restoration. | Stops the worker and preserves repair material. | N.H remains stopped. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 3 · DESIGNED | C-BGMM.12.3 — Restore prior content | The listed-file restoration boundary. | Writes only the named destination. | No arbitrary-file change is authorized. | [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.7.4 — Verified recovery completion
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — The successful end of verified startup rollback. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — Verified completion of the bounded restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Seals the package, renders it permanently inaccessible and writes `bgmm_rollback_completed` before N.H starts. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — Restored prior state and the completed-rollback audit record. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Delete the package or report successful recovery before restoration verifies. [V10 §0B] [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Unsuccessful restoration remains halted instead of taking this completion path. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7.3 — Exact recovery scope: supplies the bounded restored state. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.6.5 — Successful package closure: only verified success permits final sealing and inaccessibility. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.11 — Rollback-completed event | Verified recovery completion. | Writes the completed event before N.H starts. | The restored state has its required audit fact. | [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.7.5 — Recovery decryption failure
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — Failure to decrypt the expected rollback package during startup recovery. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — The failed protected-package decryption result. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Halts the recovery worker, retains the package without making it inaccessible and keeps N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — A stopped system requiring full normal BGMM authorization. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Proceed with restoration or start N.H after failed decryption. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Remains halted until the full normal maintenance authorization path is entered. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: supplies the decryption-failure outcome. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: further repair requires the full normal authorization path. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.7.6 — Recovery integrity failure
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — Failure of the rollback package's integrity verification. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — A failed full-integrity result. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Stops the worker before restoration can proceed; keeps the package not yet inaccessible and N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — Failed-closed recovery requiring the full normal maintenance path. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Restore from the failed package or seal it as successfully completed. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Halts with N.H stopped until full BGMM authorization. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7.2 — Full package-integrity condition: supplies the failed verification. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: repair cannot bypass the full normal authorization path. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.7.7 — Recovery restoration failure
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — Failure while restoring the verified package's prior state. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — The failed restoration outcome. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Halts the worker, leaves the package not made inaccessible and keeps N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — A blocked startup with the package retained for authorized recovery. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Continue to normal N.H startup after a failed restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Requires full normal BGMM authorization before further repair. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7.3 — Exact recovery scope: supplies the failed restoration result within the listed scope. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: the failure grants no bypass of normal factors. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.8 — Maintenance entry sequence
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — The six-step entry sequence with purpose-specific factor branches. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — The declared purpose/change, motherbase thumbprint, and the phone, normal-recovery or emergency factors applicable to that purpose. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Records purpose and change first; obtains the local OS thumbprint result; obtains trusted-phone confirmation for code/configuration/security, the normal code for device trust, or emergency factors for emergency recovery; only then opens the exact scoped window. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — An `nh_system` write token for exactly the authorized in-scope files and purpose. [V10 §25.13 / Entering Maintenance Mode]
- Must never: DESIGNED — Open the window before its factors pass, demand the unavailable old phone as a required factor for device-trust/emergency recovery, or broaden the declared scope. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Keeps the maintenance window closed without the complete applicable factor conjunction. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.2 — Protected purposes and factors: supplies the exact applicable material/factor branch. [V10 §25.13 / Purpose-Specific Authorization]
- Gated by: DESIGNED — C-BGMM.1 — Narrow maintenance boundary: remote or ordinary administrator entry cannot substitute for this path; C-BGMM.9 — Exact file-scope enforcement: limits the granted token to the declared files and purpose. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Entering Maintenance Mode]
- Changes: DESIGNED — C-BGMM.13 — Volatile maintenance session state: opens the bounded session and its write-token state. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5 — Signed-manifest trust anchor | The authorized maintenance session. | Limits private signing-key access to that session. | Unapproved manifest signing gains no key access. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 2 · DESIGNED | C-BGMM.7.5 — Recovery decryption failure | The full normal repair-authorization path. | Requires it after failed decryption. | The failure grants no factor bypass. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 3 · DESIGNED | C-BGMM.7.6 — Recovery integrity failure | Normal maintenance authorization. | Requires it before repair after integrity failure. | N.H remains stopped without that path. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 4 · DESIGNED | C-BGMM.7.7 — Recovery restoration failure | The full required repair factors. | Keeps restoration failure inside normal authorization. | No general recovery authority is inferred. | [V10 §25.13 / Protected Startup Recovery Worker] |
| 5 · DESIGNED | C-BGMM.8.1 — Purpose declaration | The first entry-step ordering. | Records purpose before authorization. | The declaration precedes every factor step. | [V10 §25.13 / Entering Maintenance Mode] |
| 6 · DESIGNED | C-BGMM.8.2 — Motherbase thumbprint result | The ordered local-factor step. | Uses only native-OS success or failure. | No biometric content enters this result. | [V10 §25.13 / Entering Maintenance Mode] |
| 7 · DESIGNED | C-BGMM.8.4 — Normal recovery-code verification | The device-trust factor branch. | Requires current local code verification with thumbprint. | Old-phone confirmation remains unnecessary. | [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 8 · DESIGNED | C-BGMM.8.6 — Scoped maintenance window | The completed applicable authorization branch. | Opens the bounded maintenance window. | Only in-scope token authority is granted. | [V10 §25.13 / Entering Maintenance Mode] |
| 9 · DESIGNED | C-BGMM.10.5 — Update and sign the manifest | The authorized session boundary. | Uses the signing private key only within it. | Manifest signing cannot bypass entry factors. | [V10 §25.13 / Signed-Manifest Trust Anchor] |
| 10 · DESIGNED | C-BGMM.13 — Volatile maintenance session state | The authorized session opening. | Holds current volatile session state. | No active authority survives restart. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State] |
| 11 · DESIGNED | C-BGMM.13.5 — Session authorization factors | Verified applicable factor results. | Retains them as session factor state. | Recovery values and biometric content remain excluded. | [V10 §25.13 / Entering Maintenance Mode] |
| 12 · DESIGNED | C-BGMM.16.3 — Startup integrity failure | The authorized repair entry path. | Requires BGMM for startup-integrity repair. | Ordinary administrator access is no repair bypass. | [V10 §25.13 / Crash, Restart, Offline Behavior] |

SUB-PARTS: C-BGMM.8.1 — Purpose declaration; C-BGMM.8.2 — Motherbase thumbprint result; C-BGMM.8.3 — Trusted-phone confirmation; C-BGMM.8.4 — Normal recovery-code verification; C-BGMM.8.5 — Emergency-factor verification; C-BGMM.8.6 — Scoped maintenance window

### C-BGMM.8.1 — Purpose declaration
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Entry step 1, the exact purpose and specific change declared in plain language. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — Ness's declaration using one of the five controlled purpose values. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Records that purpose and change before any authorization step. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — The recorded declaration used by subsequent factor and scope checks. [V10 §25.13 / Entering Maintenance Mode]
- Must never: DESIGNED — Begin authorization before recording the declaration, or include private content in visible change descriptions. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — Authorization cannot precede the recorded declaration. [V10 §25.13 / Entering Maintenance Mode]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: places declaration before all authorization. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.14.1 — Human-visible and phone descriptions: private content is excluded from the description. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2 — Protected purposes and factors | The recorded purpose and change. | Chooses the applicable controlled-purpose branch. | The material/factor boundary follows that declaration. | [V10 §25.13 / Entering Maintenance Mode] |
| 2 · DESIGNED | C-BGMM.6.1 — Rollback change description | The declared change. | Carries its structural description for audit linkage. | The package refers to the actual declared change. | [V10 §25.13 / Entering Maintenance Mode] |
| 3 · DESIGNED | C-BGMM.8.2 — Motherbase thumbprint result | The previously recorded declaration. | Requires declaration before local biometric authorization. | The thumbprint cannot precede declared purpose. | [V10 §25.13 / Entering Maintenance Mode] |
| 4 · DESIGNED | C-BGMM.8.3 — Trusted-phone confirmation | Purpose and nonprivate change description. | Displays the request on the trusted phone. | Confirmation remains bound to the declared change. | [V10 §25.13 / Entering Maintenance Mode] |
| 5 · DESIGNED | C-BGMM.9 — Exact file-scope enforcement | Declared purpose and change. | Derives the exact file list. | The token cannot expand beyond that scope. | [V10 §25.13 / File Scope Enforcement] |
| 6 · DESIGNED | C-BGMM.13.2 — Declared maintenance purpose | The controlled purpose value. | Retains it in declared_purpose. | Current state reflects the pre-authorization declaration. | [V10 §25.13 / Entering Maintenance Mode] |
| 7 · DESIGNED | C-BGMM.13.3 — Declared maintenance change | The specific declared change. | Retains it in declared_change. | Scope and descriptions use the recorded change. | [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.2 — Motherbase thumbprint result
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Entry step 2, the motherbase's native-OS thumbprint result. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — Only `success` or `failure` from the native OS framework after Ness provides the thumbprint. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Uses that minimal local result for the factor required by all five maintenance purposes. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — The local thumbprint factor result. [V10 §25.13 / Entering Maintenance Mode]
- Must never: DESIGNED — Receive biometric content in place of the native OS's success/failure result. [V10 §25.13 / Entering Maintenance Mode]
- Fails closed by: DESIGNED — A failed local thumbprint cannot satisfy the required factor. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: places the local thumbprint after declaration. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.8.1 — Purpose declaration: the exact purpose and change must already be recorded. [V10 §25.13 / Entering Maintenance Mode]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2.1 — Code-change purpose | The local thumbprint result. | Requires it alongside phone confirmation. | A failed local factor cannot authorize code changes. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-BGMM.2.2 — Configuration-change purpose | The native-OS local result. | Requires successful local verification. | Configuration authority lacks no required local factor. | [V10 §25.13 / Purpose-Specific Authorization] |
| 3 · DESIGNED | C-BGMM.2.3 — Security-policy-change purpose | The local biometric success/failure fact. | Requires the local factor before security-policy authority. | Phone confirmation alone is insufficient. | [V10 §25.13 / Purpose-Specific Authorization] |
| 4 · DESIGNED | C-BGMM.2.4 — Device-trust-change purpose | The motherbase thumbprint result. | Combines it with local recovery-code verification. | The recovery code alone cannot open the window. | [V10 §25.13 / Entering Maintenance Mode] |
| 5 · DESIGNED | C-BGMM.2.5 — Emergency-recovery purpose | The required motherbase biometric factor. | Keeps it in the full emergency conjunction. | Emergency materials do not replace the thumbprint. | [V10 §25.13 / Purpose-Specific Authorization] |
| 6 · DESIGNED | C-BGMM.8.5 — Emergency-factor verification | The local thumbprint result. | Requires it with physical access and emergency materials. | No emergency-factor subset authorizes recovery. | [V10 §25.13 / Purpose-Specific Authorization] |
| 7 · DESIGNED | C-PAIR.4.1 — Emergency factor conjunction | Physical motherbase access, separate emergency code stored outside Bitwarden, printed recovery sheet kept physically secure and Ness's motherbase thumbprint through BGMM. | Gates this place: the local thumbprint is required. | Nothing in this card. | [V10 §25.10 / Required Factors] [V10 §25.13 / Entering Maintenance Mode] |
| 8 · DESIGNED | C-PAIR.3.1 — Replacement factor conjunction | Current Bitwarden normal recovery code and Ness's thumbprint through Maintenance Mode on the N.H desktop. | Gates this place: supplies the required desktop thumbprint factor. | Nothing in this card. | [V10 §25.9] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.3 — Trusted-phone confirmation
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Entry step 3 for code, configuration and security-policy changes. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — A purpose-bound request sent by the motherbase to the trusted paired phone, carrying the declared purpose and nonprivate change description. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Displays purpose and change; obtains Ness's explicit confirmation; requires the phone's own BAI `one_time_authorization_token` with `bgmm_confirmation:<session_id>:<purpose>` before sending confirmation. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — Phone confirmation bound to this maintenance session and purpose. [V10 §25.13 / Entering Maintenance Mode]
- Must never: DESIGNED — Send confirmation without that purpose-bound token, accept a different purpose's artifact, or include private content in the phone payload. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.6 / Purpose Binding] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — Withholds phone confirmation when its required BAI token or explicit confirmation is absent. [V10 §25.13 / Entering Maintenance Mode]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the declared purpose/change; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the trusted paired-phone identity. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BAI.3.9.4 — Maintenance confirmation purpose: requires the exact maintenance session/purpose binding; C-BAI.4 — One-time authorization token: the phone requires its own purpose-bound token before sending confirmation; C-BGMM.14.1 — Human-visible and phone descriptions: excludes private content from what is displayed or sent. [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2.1 — Code-change purpose | Explicit session/purpose-bound phone confirmation. | Requires it for code_change. | Local thumbprint alone cannot authorize code edits. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-BGMM.2.2 — Configuration-change purpose | The trusted phone's confirmed request. | Requires it for configuration_change. | Unconfirmed configuration changes remain unauthorized. | [V10 §25.13 / Purpose-Specific Authorization] |
| 3 · DESIGNED | C-BGMM.2.3 — Security-policy-change purpose | The BAI-bound phone confirmation. | Requires it for security_policy_change. | The security-policy window keeps both factors. | [V10 §25.13 / Purpose-Specific Authorization] |

SUB-PARTS: NONE

### C-BGMM.8.4 — Normal recovery-code verification
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Entry step 4 for `device_trust_change`. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — The current Bitwarden normal recovery code for local verification. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Verifies that code locally; no phone confirmation is required because the old trusted phone may be unavailable. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — The normal recovery-code factor result. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Store the code value in N.H or substitute phone availability for the stated recovery-code requirement. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Entering Maintenance Mode]
- Fails closed by: DESIGNED — A missing or failed current-code verification does not authorize the device-trust window. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current normal recovery authority for the local check. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: this factor is used with the required motherbase thumbprint for the device-trust purpose; C-BGMM.3.6 — Recovery-value prohibition: the value cannot enter N.H storage. [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2.4 — Device-trust-change purpose | The current normal-code verification result. | Requires the locally verified code with thumbprint. | Device-trust changes remain gated without requiring the old phone. | [V10 §25.13 / Entering Maintenance Mode] |
| 2 · DESIGNED | C-PAIR.3.1 — Replacement factor conjunction | Current Bitwarden normal recovery code and Ness's thumbprint through Maintenance Mode on the N.H desktop. | Gates this place: checks the current normal code locally. | Nothing in this card. | [V10 §25.9] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.5 — Emergency-factor verification
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — Entry step 5 for the restricted emergency-recovery purpose. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — Physical motherbase access, emergency code and printed recovery sheet, alongside the required local thumbprint. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Verifies the emergency code and printed sheet; requires physical access; no trusted-phone confirmation is required. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — The emergency-factor conjunction for device-trust recovery only. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Admit remote emergency entry, retain recovery-code values or extend emergency authority to code/configuration. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Fails closed by: DESIGNED — Does not authorize emergency recovery without all required simultaneous factors; the emergency scope guard remains unconditional. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the emergency code/sheet verification boundary; C-BGMM.8.5.1 — Physical motherbase presence: supplies the physical-access condition; C-BGMM.8.5.2 — Emergency-code verification: supplies the code factor; C-BGMM.8.5.3 — Printed-sheet verification: supplies the sheet factor. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Gated by: DESIGNED — C-BGMM.8.2 — Motherbase thumbprint result: the motherbase biometric factor remains required; C-BGMM.9.2 — Emergency scope override: even a declaration cannot authorize code/configuration. [V10 §25.13 / Purpose-Specific Authorization]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.2.5 — Emergency-recovery purpose | Physical access and verified emergency code/sheet. | Requires the full emergency conjunction. | Only device-trust recovery is authorized. | [V10 §25.13 / Purpose-Specific Authorization] |

SUB-PARTS: C-BGMM.8.5.1 — Physical motherbase presence; C-BGMM.8.5.2 — Emergency-code verification; C-BGMM.8.5.3 — Printed-sheet verification

### C-BGMM.8.5.1 — Physical motherbase presence
Stamp: DESIGNED    Source: [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — Required physical access to the motherbase for emergency recovery. [V10 §25.13 / Purpose-Specific Authorization]
- Takes in: DESIGNED — Physical presence at the motherbase. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Keeps physical access in the simultaneous emergency-factor conjunction. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — The physical-presence condition for emergency authorization. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Accept remote entry as satisfying physical motherbase access. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Emergency entry is not authorized without physical access. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.5 — Emergency-factor verification | Required physical motherbase access. | Keeps physical presence in the emergency conjunction. | Remote entry cannot authorize emergency recovery. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-PAIR.4.1 — Emergency factor conjunction | Physical motherbase access, separate emergency code stored outside Bitwarden, printed recovery sheet kept physically secure and Ness's motherbase thumbprint through BGMM. | Gates this place: physical access is mandatory. | Nothing in this card. | [V10 §25.10 / Required Factors] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.5.2 — Emergency-code verification
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Verification of the emergency code required by emergency recovery. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — The emergency code presented for the required verification. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Verifies that factor as part of the full emergency conjunction, without storing its value in N.H. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gives out: DESIGNED — The emergency-code factor result. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Store the recovery value or treat the code alone as complete emergency authority. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — An absent or unverified emergency code cannot satisfy the required factor. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the emergency-code authority boundary. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.3.6 — Recovery-value prohibition: the code value cannot enter N.H storage. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.5 — Emergency-factor verification | The emergency-code verification result. | Requires the verified code alongside the other factors. | A code alone is not complete emergency authority. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-PAIR.4.1 — Emergency factor conjunction | Physical motherbase access, separate emergency code stored outside Bitwarden, printed recovery sheet kept physically secure and Ness's motherbase thumbprint through BGMM. | Gates this place: the separate code must verify. | Nothing in this card. | [V10 §25.10 / Required Factors] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.5.3 — Printed-sheet verification
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Verification of the printed recovery sheet required by emergency recovery. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — The printed recovery sheet for verification. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Requires sheet verification alongside physical access, thumbprint and emergency code. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — The printed-sheet factor result. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Omit this factor or treat the sheet alone as emergency authorization. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Emergency recovery remains unauthorized without the required verified sheet. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the printed-sheet authority boundary. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.5 — Emergency-factor verification | The printed-sheet verification result. | Requires the verified sheet with the other emergency factors. | No partial factor set authorizes recovery. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-PAIR.4.1 — Emergency factor conjunction | Physical motherbase access, separate emergency code stored outside Bitwarden, printed recovery sheet kept physically secure and Ness's motherbase thumbprint through BGMM. | Gates this place: the sheet must verify. | Nothing in this card. | [V10 §25.10 / Required Factors] [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.8.6 — Scoped maintenance window
Stamp: DESIGNED    Source: [V10 §25.13 / Entering Maintenance Mode]

ALONE
- What it is: DESIGNED — Entry step 6, opening the authorized maintenance window. [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — The declared file list/purpose and successfully satisfied applicable factors. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Enforces exactly that scope and grants the `nh_system` write token only for in-scope files. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — A temporary purpose-bound maintenance window and scoped write token. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Must never: DESIGNED — Grant wider file access or make maintenance authorization permanent. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Fails closed by: DESIGNED — Required factors precede opening, out-of-scope writes are blocked, and every relock immediately revokes the token. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: supplies the completed authorization branch. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.2 — Protected purposes and factors: the complete required conjunction must pass; C-BGMM.9 — Exact file-scope enforcement: only the exact declared files are writable; C-BGMM.11 — Immediate automatic relocking: any relock trigger closes the window. [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking]
- Changes: DESIGNED — C-BGMM.13.9 — Write-token activity: records the active scoped token. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10 — Protected change sequence | The authorized scoped window. | Runs the declared seven-step change sequence. | Only in-scope files can be touched. | [V10 §25.13 / Entering Maintenance Mode] |
| 2 · DESIGNED | C-BGMM.13.7 — Maintenance opening time | The actual authorized opening time. | Retains opened_at. | Current session state records its opening. | [V10 §25.13 / Entering Maintenance Mode] |
| 3 · DESIGNED | C-BGMM.13.9 — Write-token activity | The scoped token grant. | Tracks current token activity. | A later relock immediately revokes it. | [V10 §25.13 / Entering Maintenance Mode] |
| 4 · DESIGNED | C-BGMM.15.2 — Session-opened event | The window-opening occurrence. | Writes the session-opened event. | The actual opening gains its structural record. | [V10 §25.13 / Entering Maintenance Mode] |
| 5 · DESIGNED | C-BGMM.15.3 — Write-token-granted event | The bounded write-token grant. | Records bgmm_write_token_granted. | The audit contains the grant fact without secret content. | [V10 §25.13 / Entering Maintenance Mode] |

SUB-PARTS: NONE

### C-BGMM.9 — Exact file-scope enforcement
Stamp: DESIGNED    Source: [V10 §25.13 / File Scope Enforcement]

ALONE
- What it is: DESIGNED — The guard restricting the `nh_system` write token to the exact declared file scope. [V10 §25.13 / File Scope Enforcement]
- Takes in: DESIGNED — The exact file list derived from declared purpose and change, plus each attempted write. [V10 §25.13 / File Scope Enforcement]
- Does: DESIGNED — Allows writes only inside that scope, while enforcing the unconditional emergency and immutable-record exclusions. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gives out: DESIGNED — A blocked out-of-scope attempt and immediate `bgmm_out_of_scope_write_attempt` record, or an in-scope write under the existing token. [V10 §25.13 / File Scope Enforcement]
- Must never: DESIGNED — Expand scope because of OS privilege, emergency declaration or an open maintenance window. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Blocks and immediately logs an out-of-scope write; immutable writes are blocked and logged separately. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the declared purpose/change from which the file list is derived. [V10 §25.13 / File Scope Enforcement]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.2 — Rollback file entries | The exact in-scope file list. | Limits package entries to those files. | The package grants no wider restore scope. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / File Scope Enforcement] |
| 2 · DESIGNED | C-BGMM.6.2.1 — Rollback file path | The declared file boundary. | Identifies only an in-scope destination. | Undeclared paths cannot be authorized writes. | [V10 §25.13 / File Scope Enforcement] |
| 3 · DESIGNED | C-BGMM.8 — Maintenance entry sequence | The declared files and purpose. | Limits the window's token to that scope. | Entry grants no general administrator authority. | [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Entering Maintenance Mode] |
| 4 · DESIGNED | C-BGMM.8.6 — Scoped maintenance window | The exact allowed file list. | Grants a token only within it. | Out-of-scope targets remain blocked. | [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking] |
| 5 · DESIGNED | C-BGMM.9.1 — Out-of-scope write refusal | The attempted target and allowed list. | Refuses an out-of-scope write. | The attempt is immediately audited. | [V10 §25.13 / File Scope Enforcement] |
| 6 · DESIGNED | C-BGMM.9.2 — Emergency scope override | The emergency purpose and target. | Rejects code/configuration writes unconditionally. | Device trust remains the sole emergency scope. | [V10 §25.13 / File Scope Enforcement] |
| 7 · DESIGNED | C-BGMM.9.3 — Immutable-write refusal | The attempted protected write. | Refuses immutable-memory modification. | The blocked immutable attempt is logged. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 8 · DESIGNED | C-BGMM.10 — Protected change sequence | The enforced target boundary. | Applies the seven-step change only in scope. | The sequence cannot widen writable files. | [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking] |
| 9 · DESIGNED | C-BGMM.10.3 — Apply the protected change | The authorized file scope. | Checks the actual change target. | Forbidden writes cannot be applied. | [V10 §25.13 / Change Application] [V10 §25.13 / File Scope Enforcement] |
| 10 · DESIGNED | C-BGMM.13.4 — Declared file scope | The enforced file-list boundary. | Retains the exact current scope. | The token cannot authorize undeclared files. | [V10 §25.13 / File Scope Enforcement] |

SUB-PARTS: C-BGMM.9.1 — Out-of-scope write refusal; C-BGMM.9.2 — Emergency scope override; C-BGMM.9.3 — Immutable-write refusal

### C-BGMM.9.1 — Out-of-scope write refusal
Stamp: DESIGNED    Source: [V10 §25.13 / File Scope Enforcement]

ALONE
- What it is: DESIGNED — Refusal of a write outside the exact allowed file list. [V10 §25.13 / File Scope Enforcement]
- Takes in: DESIGNED — The attempted target and the token's declared scope. [V10 §25.13 / File Scope Enforcement]
- Does: DESIGNED — Blocks the write and immediately writes `bgmm_out_of_scope_write_attempt` to the security audit log. [V10 §25.13 / File Scope Enforcement]
- Gives out: DESIGNED — A denied write and the immediate structural audit fact. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Apply the out-of-scope write or omit its immediate audit event. [V10 §25.13 / File Scope Enforcement]
- Fails closed by: DESIGNED — Refuses the write at the scope guard. [V10 §25.13 / File Scope Enforcement]

TOGETHER
- Fed by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: supplies the target and allowed file list. [V10 §25.13 / File Scope Enforcement]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.7 — Out-of-scope-attempt event | The actual blocked out-of-scope attempt. | Records its immediate audit event. | The attempted unauthorized write remains denied. | [V10 §25.13 / File Scope Enforcement] |

SUB-PARTS: NONE

### C-BGMM.9.2 — Emergency scope override
Stamp: DESIGNED    Source: [V10 §25.13 / Purpose-Specific Authorization]

ALONE
- What it is: DESIGNED — The unconditional device-trust-only scope of `emergency_recovery`. [V10 §25.13 / Purpose-Specific Authorization]
- Takes in: DESIGNED — An emergency declaration and any proposed file write. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Keeps code and configuration files unwritable regardless of what the session declares. [V10 §25.13 / Purpose-Specific Authorization]
- Gives out: DESIGNED — Emergency scope confined to device-trust records. [V10 §25.13 / Purpose-Specific Authorization]
- Must never: DESIGNED — Grant code-edit or configuration authority through an emergency session. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — The guard blocks those writes unconditionally. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: supplies the purpose and attempted file target. [V10 §25.13 / File Scope Enforcement]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.5 — Emergency-factor verification | The device-trust-only emergency scope. | Applies emergency factors without broadening scope. | Code and configuration remain unwritable. | [V10 §25.13 / Purpose-Specific Authorization] |
| 2 · DESIGNED | C-BGMM.17 — Unconditional protected-core rules | The emergency write prohibition. | Preserves it as a core rule. | Emergency recovery grants no code-edit authority. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |

SUB-PARTS: NONE

### C-BGMM.9.3 — Immutable-write refusal
Stamp: DESIGNED    Source: [V10 §25.13 / Protected-Core Rules (Unconditional)] [MAP C-BGMM]

ALONE
- What it is: DESIGNED — The scope guard's refusal to write immutable protected memory. [V10 §25.13 / Protected-Core Rules (Unconditional)] [MAP C-BGMM]
- Takes in: DESIGNED — An attempted direct write to immutable roots, readings, provenance, clashes, Person-Box links, audit or gold records. [V10 §25.13 / Protected Material Boundary] [MAP C-BGMM]
- Does: DESIGNED — Blocks the write and records `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)] [MAP C-BGMM]
- Gives out: DESIGNED — Preserved immutable material and a structural blocked-write event. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Treat an authorized maintenance window as an immutable-record override. [V10 §25.13 / What BGMM Is and Is Not]
- Fails closed by: DESIGNED — Refuses the immutable write. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: supplies the attempted protected-file write. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.3 — Permanently unchangeable material | The immutable-write refusal. | Keeps protected memory outside direct writable scope. | Forbidden writes are blocked and logged. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 2 · DESIGNED | C-BGMM.15.17 — Immutable-write-blocked event | The actual blocked immutable attempt. | Records bgmm_immutable_write_blocked. | The preserved record gains a structural refusal audit fact. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |
| 3 · DESIGNED | C-BGMM.17 — Unconditional protected-core rules | The immutable-write guard. | Retains the unconditional refusal. | Maintenance cannot override immutable history. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |

SUB-PARTS: NONE

### C-BGMM.10 — Protected change sequence
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — The exact seven-step protected-change order. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — An authorized in-scope change, current file bytes and signing/protection keys. [V10 §25.13 / Change Application] [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — (1) Writes and flushes the change-log entry; (2) creates and persists the rollback package; (3) applies the change; (4) computes and records `hash_after`; (5) updates and re-signs the manifest; (6) re-signs modified executables; (7) immediately writes `bgmm_change_applied`. The first two steps precede touching the file. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — Changed files, recorded hashes, signed manifest/executables and the immediate change-applied event, or rollback after failure. [V10 §25.13 / Change Application]
- Must never: DESIGNED — Touch a file before both pre-write steps or continue after a post-touch step failure without immediate rollback. [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — Any step failure after file touch triggers rollback immediately. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.6 — Scoped maintenance window: supplies the authorized file scope and active token. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: blocks forbidden targets; C-BGMM.11 — Immediate automatic relocking: revokes the token and rolls back a partial change on relock. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking]
- Changes: DESIGNED — C-BGMM.13.10 — Applied-change list: retains the append-only applied-change state. [V10 §25.13 / BGMM-Owned State]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.1 — Flush the change-log entry | The declared authorized change and first-step order. | Writes and flushes structural provenance first. | The file remains untouched until pre-write requirements finish. | [V10 §25.13 / Change Application] |
| 2 · DESIGNED | C-BGMM.10.3 — Apply the protected change | The authorized change operation. | Applies it after both pre-write steps. | Post-touch failure immediately triggers rollback. | [V10 §25.13 / Change Application] |
| 3 · DESIGNED | C-BGMM.10.6 — Re-sign modified executables | Modified executable files in the prescribed order. | Re-signs them with the code-signing key. | The final change event follows executable signing. | [V10 §25.13 / Change Application] |
| 4 · DESIGNED | C-BGMM.10.8 — Post-touch failure rollback | Any failed step after file touch. | Triggers rollback immediately. | The failed change cannot continue as success. | [V10 §25.13 / Change Application] |
| 5 · DESIGNED | C-BGMM.13 — Volatile maintenance session state | Actual applied-change facts. | Maintains the volatile applied-change state. | Persistent provenance remains in the permanent log. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State] |
| 6 · DESIGNED | C-BGMM.13.10 — Applied-change list | The sequence's applied changes. | Appends them to applied_changes. | The list retains earlier entries unchanged. | [V10 §25.13 / Change Application] [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: C-BGMM.10.1 — Flush the change-log entry; C-BGMM.10.2 — Persist the rollback package; C-BGMM.10.3 — Apply the protected change; C-BGMM.10.4 — Record the post-change hash; C-BGMM.10.5 — Update and sign the manifest; C-BGMM.10.6 — Re-sign modified executables; C-BGMM.10.7 — Record the applied change; C-BGMM.10.8 — Post-touch failure rollback

### C-BGMM.10.1 — Flush the change-log entry
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 1, completed before any file is touched. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The structural paths, operations and hashes describing the authorized change. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Appends and flushes the change-log entry. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — Durable pre-change provenance. [V10 §25.13 / Change Application]
- Must never: DESIGNED — Put file content in the log or touch the file before the entry is flushed. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — A failed pre-write log step cannot authorize touching the protected file. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10 — Protected change sequence: supplies the authorized change and first-step order. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.14.3 — Structural change-log content: limits the entry to structural facts. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.4.5 — Change-log provenance layer | The flushed pre-change log entry. | Preserves its permanent provenance. | No file touch precedes the recorded change. | [V10 §25.13 / Change Application] |
| 2 · DESIGNED | C-BGMM.10.2 — Persist the rollback package | Completion of the first pre-write step. | Creates and persists the rollback package next. | The exact pre-write sequence remains intact. | [V10 §25.13 / Change Application] |
| 3 · DESIGNED | C-BGMM.15.4 — Change-log-entry event | The actual pre-change entry operation. | Records its named event under immediate timing. | Structural provenance precedes the write. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.2 — Persist the rollback package
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 2, before any protected file write. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — Exact prior file contents, restoration metadata and the declared change identity. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Creates and persists the encrypted full-content rollback package. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — A persisted protected package before change application. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Must never: DESIGNED — Apply the change before package persistence. [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — The first write cannot proceed without its persisted package. [V10 §25.13 / Encrypted Full-Content Rollback Packages]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: defines the complete protected restoration record. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.10.1 — Flush the change-log entry: its completion precedes package creation/persistence in the exact sequence. [V10 §25.13 / Change Application]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.3 — Rollback creation time | Package creation before application. | Records the pre-write created_at. | The timestamp marks the required creation boundary. | [V10 §25.13 / Change Application] |
| 2 · DESIGNED | C-BGMM.10.3 — Apply the protected change | The persisted protected rollback package. | Requires it before first file touch. | No unbacked change begins. | [V10 §25.13 / Change Application] [V10 §25.13 / File Scope Enforcement] |

SUB-PARTS: NONE

### C-BGMM.10.3 — Apply the protected change
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 3, the protected-file modification. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The declared in-scope change under the active scoped token. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / File Scope Enforcement]
- Does: DESIGNED — Applies the authorized change only after the flushed log entry and persisted package exist. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — The changed protected file whose `hash_after` is next recorded. [V10 §25.13 / Change Application]
- Must never: DESIGNED — Write outside scope, skip either pre-write requirement or continue a failed post-touch sequence. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — A failure after touching the file triggers immediate rollback. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10 — Protected change sequence: supplies the declared change. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.10.2 — Persist the rollback package: package persistence must precede this write; C-BGMM.9 — Exact file-scope enforcement: permits only the authorized files. [V10 §25.13 / Change Application] [V10 §25.13 / File Scope Enforcement]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.4 — Record the post-change hash | The changed protected file. | Computes and records hash_after. | Manifest update follows the recorded hash. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.4 — Record the post-change hash
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 4, computing and recording `hash_after`. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The file after the applied change. [V10 §25.13 / Change Application]
- Does: DESIGNED — Computes its post-change hash and records it before the manifest update. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — Recorded `hash_after`. [V10 §25.13 / Change Application]
- Must never: DESIGNED — Skip recording the post-change hash. [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — Failure at this post-touch step triggers rollback immediately. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.3 — Apply the protected change: supplies the changed file. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.5.1 — Expected protected-file hashes | Recorded hash_after. | Supplies the changed file's expected digest. | The manifest update uses the recorded post-change hash. | [V10 §25.13 / Change Application] |
| 2 · DESIGNED | C-BGMM.10.5 — Update and sign the manifest | The computed post-change hash. | Updates and signs the manifest next. | Hash recording precedes manifest signing. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.5 — Update and sign the manifest
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 5, updating and re-signing the manifest. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The recorded changed-file hash and authorized manifest-signing key. [V10 §25.13 / Change Application]
- Does: DESIGNED — Updates the manifest, signs the new version and preserves the prior signed version in append-only history. [V10 §25.13 / Change Application] [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The newly signed manifest and preserved prior version. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Delete the previous signed manifest or use the rollback-sealing key as the signing key. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Fails closed by: DESIGNED — A post-touch update/signing failure triggers immediate rollback. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.4 — Record the post-change hash: supplies `hash_after`; C-BAI.8.1 — Manifest-signing key: signs the authorized new version. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: private signing-key access requires an authorized session. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Changes: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: becomes the new signed current version while preserving prior provenance. [V10 §25.13 / Signed-Manifest Trust Anchor]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.6 — Re-sign modified executables | The completed manifest-update/signing step. | Re-signs modified executables next. | The source's exact step order is retained. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.6 — Re-sign modified executables
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 6, re-signing modified executable files with the code-signing key. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The modified executables and code-signing key. [V10 §25.13 / Change Application]
- Does: DESIGNED — Re-signs those files after the manifest update step, in the source's stated order. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — Updated executable code signatures. [V10 §25.13 / Change Application]
- Must never: DESIGNED — Omit re-signing a modified executable. [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — Signing failure after file touch triggers rollback immediately. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10 — Protected change sequence: supplies the modified executables and ordered signing step. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.10.5 — Update and sign the manifest: precedes executable re-signing in the prescribed sequence. [V10 §25.13 / Change Application]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.4.3 — Executable code signing | Re-signed modified executable files. | Checks signatures before runtime loading. | Unsigned or invalid modules remain rejected. | [V10 §25.13 / Change Application] |
| 2 · DESIGNED | C-BGMM.10.7 — Record the applied change | Completion of the executable-signing step. | Immediately records the applied change next. | The prescribed seven-step order is retained. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.7 — Record the applied change
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — Change step 7, the immediate `bgmm_change_applied` security event. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The applied, hashed and signed change. [V10 §25.13 / Change Application]
- Does: DESIGNED — Writes the event immediately and flushes it before the producing function returns. [V10 §25.13 / Change Application] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The permanent structural change-applied audit record. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Delay the event beyond function return or include protected file content. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — Failure at this post-touch step triggers immediate rollback. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.6 — Re-sign modified executables: completes the preceding signing step. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires immediate write/flush and structural-only content. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.5 — Change-applied event | The actual final-step change event. | Records bgmm_change_applied immediately. | Post-touch logging failure triggers rollback. | [V10 §25.13 / Change Application] |

SUB-PARTS: NONE

### C-BGMM.10.8 — Post-touch failure rollback
Stamp: DESIGNED    Source: [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — The common failure branch after a protected file has been touched. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — Failure of any change-sequence step after file touch. [V10 §25.13 / Change Application]
- Does: DESIGNED — Triggers rollback immediately. [V10 §25.13 / Change Application]
- Gives out: DESIGNED — A rollback attempt using the prior protected package. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Leave the partial change as a successful result or defer the required rollback. [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — Takes the immediate rollback branch instead of continuing the failed change. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10 — Protected change sequence: reports the post-touch failure. [V10 §25.13 / Change Application]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BGMM.12 — Idempotent rollback: invokes restoration from the protected prior-content package. [V10 §25.13 / Change Application] [V10 §25.13 / Rollback]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.10 — Rollback-triggered event | The immediate post-touch rollback trigger. | Records that rollback was triggered. | The event does not claim restoration success. | [V10 §25.13 / Change Application] [V10 §25.13 / Automatic Relocking] |

SUB-PARTS: NONE

### C-BGMM.11 — Immediate automatic relocking
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Immediate maintenance-window closure on any of seven triggers. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — Completion, timeout, restart/crash, SACL security alert, phone disconnection, explicit abort or biometric expiry. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Closes the window immediately, revokes the write token, writes `bgmm_write_token_revoked` and triggers rollback if a change was partially applied. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — A relocked session, revoked write authority, the audit event and any required partial-change rollback. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Leave the write token active after any relock trigger or omit rollback of a partial change. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Every listed trigger immediately removes write authority; a partial change takes rollback. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.13 — Volatile maintenance session state: supplies the active window, expiry, token and applied-change state; C-SACL — Speaker Access-Control Layer (§25.4): supplies medium-or-higher spoofing or session-level alerts. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BGMM.13.9 — Write-token activity: becomes inactive immediately; C-BGMM.12 — Idempotent rollback: restores a partially applied change. [V10 §25.13 / Automatic Relocking]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.6 — Scoped maintenance window | Any immediate relock trigger. | Closes the authorized window and revokes its token. | Write authority ends immediately. | [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking] |
| 2 · DESIGNED | C-BGMM.10 — Protected change sequence | Relock during the change sequence. | Stops write authority and rolls back a partial change. | A partially applied change cannot keep running. | [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Automatic Relocking] |
| 3 · DESIGNED | C-BGMM.11.1 — Completion relock | The common completion response. | Revokes the token on applied/verified/logged completion. | No write window remains after completion. | [V10 §25.13 / Automatic Relocking] |
| 4 · DESIGNED | C-BGMM.11.2 — Timeout relock | The timeout response. | Closes at expires_at and rolls back partial work. | Expired authority cannot continue writing. | [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State] |
| 5 · DESIGNED | C-BGMM.11.3 — Restart or crash relock | The restart/crash closure rule. | Removes the old process's write authority. | Verified startup rollback precedes N.H startup. | [V10 §25.13 / Automatic Relocking] |
| 6 · DESIGNED | C-BGMM.11.4 — Security-alert relock | The security-alert response. | Immediately revokes the window on a qualifying alert. | A partial change rolls back. | [V10 §25.13 / Automatic Relocking] |
| 7 · DESIGNED | C-BGMM.11.5 — Phone-disconnection relock | The phone-disconnection response. | Closes the window during the open session. | The disconnected phone cannot leave write authority active. | [V10 §25.13 / Automatic Relocking] |
| 8 · DESIGNED | C-BGMM.11.6 — Explicit-abort relock | The explicit-abort response. | Revokes the token and rolls back a partial change. | The change does not continue after abort. | [V10 §25.13 / Automatic Relocking] |
| 9 · DESIGNED | C-BGMM.11.7 — Biometric-expiry relock | The biometric-expiry response. | Immediately removes maintenance write authority. | Expired verification cannot keep the window open. | [V10 §25.13 / Automatic Relocking] |
| 10 · DESIGNED | C-BGMM.13 — Volatile maintenance session state | The active-window closure rule. | Removes current write authority on any trigger. | Session state cannot preserve a revoked token. | [V10 §25.13 / Automatic Relocking] |
| 11 · DESIGNED | C-BGMM.13.9 — Write-token activity | An immediate revocation trigger. | Marks the token inactive. | No write authority survives relock. | [V10 §25.13 / Automatic Relocking] |
| 12 · DESIGNED | C-BGMM.15.9 — Write-token-revoked event | The actual token revocation. | Writes its structural audit event. | The revoked authority has a permanent record. | [V10 §25.13 / Automatic Relocking] |
| 13 · DESIGNED | C-BGMM.15.10 — Rollback-triggered event | A relock with partially applied change. | Records the required rollback trigger. | The event does not claim rollback completion. | [V10 §25.13 / Change Application] [V10 §25.13 / Automatic Relocking] |
| 14 · DESIGNED | C-BGMM.17 — Unconditional protected-core rules | The temporary-authority closure rule. | Preserves immediate token revocation. | Maintenance authorization cannot become permanent. | [V10 §25.13 / Protected-Core Rules (Unconditional)] |

SUB-PARTS: C-BGMM.11.1 — Completion relock; C-BGMM.11.2 — Timeout relock; C-BGMM.11.3 — Restart or crash relock; C-BGMM.11.4 — Security-alert relock; C-BGMM.11.5 — Phone-disconnection relock; C-BGMM.11.6 — Explicit-abort relock; C-BGMM.11.7 — Biometric-expiry relock

### C-BGMM.11.1 — Completion relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Closure when the change is applied, verified and logged. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The completed change with all three completion facts. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Immediately closes the maintenance window and revokes the write token with its event. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — A completed relocked session. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Leave write authority open after completion. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Completion removes the token immediately. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: supplies the common closure/revocation rule. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.8 — Session-completed event | Applied, verified and logged completion. | Records the session-completed event. | No incomplete change is substituted for completion. | [V10 §25.13 / Automatic Relocking] |

SUB-PARTS: NONE

### C-BGMM.11.2 — Timeout relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Closure when `expires_at` is reached. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The active session's expiration time. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Immediately closes the window, revokes/logs the token and rolls back a partial change. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — Expired maintenance authority and any necessary rollback. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Keep writing past the expiration time. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Timeout revokes the token immediately. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.13.8 — Maintenance expiration time: supplies `expires_at`; C-BGMM.11 — Immediate automatic relocking: supplies the common revocation/rollback response. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.13 — Session-timed-out event | The actual timeout occurrence. | Records bgmm_session_timed_out. | The expired session remains relocked. | [V10 §25.13 / Automatic Relocking] |

SUB-PARTS: NONE

### C-BGMM.11.3 — Restart or crash relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Immediate closure on restart or crash. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The restart/crash of an open maintenance session. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Does: DESIGNED — Loses volatile session state and revokes the write token through OS process exit; startup recovery performs required rollback before N.H starts. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — No surviving maintenance write authority. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Must never: DESIGNED — Restore an open write window merely because the previous process had one. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — The token is revoked and recovery precedes N.H startup. [V10 §25.13 / Crash, Restart, Offline Behavior]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: defines restart/crash as a closure trigger. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-BGMM.7 — Protected startup recovery worker: performs bounded rollback after the crash. [V10 §25.13 / Crash, Restart, Offline Behavior]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.11.4 — Security-alert relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Closure on a SACL medium-or-higher spoofing or session-level security alert. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The actual SACL security alert. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Closes immediately, revokes/logs the token and triggers rollback of a partial change. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — Removed maintenance authority after the alert. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Keep the maintenance window writable after the security trigger. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Immediately revokes the token. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies the qualifying alert; C-BGMM.11 — Immediate automatic relocking: defines its mandatory response. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.11.5 — Phone-disconnection relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Immediate closure on phone disconnection during an open session. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The disconnection fact during the open maintenance window. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Closes the window, revokes/logs the token and rolls back any partial change. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — A relocked window with no remaining write authority. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Continue using the open token after phone disconnection. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Revokes the token immediately. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: supplies the disconnection response. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.11.6 — Explicit-abort relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Closure on Ness's explicit abort. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The explicit abort instruction for the open maintenance session. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Closes immediately, revokes/logs the token and triggers rollback if the change is partial. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — An aborted, relocked maintenance session. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Keep applying the change after explicit abort. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Removes write authority immediately on the abort. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: governs the abort-triggered revocation and partial-change rollback. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15.14 — Session-aborted event | The explicit-abort occurrence. | Writes the structural abort event. | The token remains revoked after abort. | [V10 §25.13 / Automatic Relocking] |

SUB-PARTS: NONE

### C-BGMM.11.7 — Biometric-expiry relock
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — Immediate closure when biometric verification expires. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The biometric-expiry fact during maintenance. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Revokes/logs the token, closes the window and triggers rollback for a partial change. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — A relocked session without current write authority. [V10 §25.13 / Automatic Relocking]
- Must never: DESIGNED — Treat expired biometric verification as continuing maintenance authorization. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Biometric expiry removes the token immediately. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: supplies the exact expiry response. [V10 §25.13 / Automatic Relocking]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.12 — Idempotent rollback
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — Exact prior-state restoration from the encrypted full-content package. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — Every package file entry and the prior signed manifest in provenance history. [V10 §25.13 / Rollback]
- Does: DESIGNED — Decrypts; verifies `prior_hash` against `prior_content`; restores prior content, signature and metadata; restores the prior signed manifest after re-verifying its signature. A file already matching `prior_content` is not rewritten. [V10 §25.13 / Rollback] [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The exact prior files and signed manifest, or failed-closed recovery. [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Use hashes alone as backups, rewrite an already matching file or substitute arbitrary file changes for restoration. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Startup decryption, verification or restoration failure halts the worker and leaves N.H stopped for full normal maintenance authorization. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies exact prior bytes and metadata; C-BGMM.5.4 — Manifest provenance history: supplies the prior signed manifest. [V10 §25.13 / Rollback]
- Gated by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: automatic startup restoration remains bounded by its measured-boot and integrity conditions. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: returns to the verified prior signed version. [V10 §25.13 / Signed-Manifest Trust Anchor]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.8 — Post-touch failure rollback | The bounded exact-restoration operation. | Invokes it immediately after post-touch failure. | Prior state is restored from real backup content. | [V10 §25.13 / Change Application] [V10 §25.13 / Rollback] |
| 2 · DESIGNED | C-BGMM.11 — Immediate automatic relocking | The required partial-change rollback. | Invokes restoration on relock when needed. | A partial change does not remain applied by default. | [V10 §25.13 / Automatic Relocking] |
| 3 · DESIGNED | C-BGMM.12.1 — Decrypt the restoration package | The encrypted restoration package. | Decrypts within the protected boundary. | Package contents are not exported. | [V10 §25.13 / Rollback] |
| 4 · DESIGNED | C-BGMM.12.6 — Already-matching-file idempotency | Current files and their exact prior bytes. | Skips a write when the content already matches. | Repeated rollback remains idempotent. | [V10 §25.13 / Rollback] |
| 5 · DESIGNED | C-BGMM.16.2 — Crash during rollback | Idempotent restoration from current file state. | Runs rollback again after interruption. | Already restored files receive no repeat write. | [V10 §25.13 / Crash, Restart, Offline Behavior] |
| 6 · DESIGNED | C-BGMM.6.5 — Successful package closure | A verified successful change or verified successful rollback. | Proceeds only when successful final verification, or a successful rollback with its verified prior-state result, precedes this closure. | Nothing in this card. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: C-BGMM.12.1 — Decrypt the restoration package; C-BGMM.12.2 — Verify prior-content bytes; C-BGMM.12.3 — Restore prior content; C-BGMM.12.4 — Restore prior signature and metadata; C-BGMM.12.5 — Restore the verified prior manifest; C-BGMM.12.6 — Already-matching-file idempotency

### C-BGMM.12.1 — Decrypt the restoration package
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — The protected decryption step of rollback. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The encrypted full-content package. [V10 §25.13 / Rollback]
- Does: DESIGNED — Decrypts it within the authorized restoration boundary. [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — Package content available only to bounded restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Must never: DESIGNED — Export the package contents or expose them to ordinary users, applications, terminals or normal runtime. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Fails closed by: DESIGNED — Failed startup decryption halts recovery with N.H stopped and the package retained. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.12 — Idempotent rollback: supplies the expected encrypted restoration package. [V10 §25.13 / Rollback]
- Gated by: DESIGNED — C-BGMM.7.1 — Expected measured-boot condition: automatic startup decryption requires the expected boot state. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.12.2 — Verify prior-content bytes | The decrypted protected file entry. | Checks prior_hash against prior_content. | Unverified bytes cannot proceed to startup restoration. | [V10 §25.13 / Rollback] |

SUB-PARTS: NONE

### C-BGMM.12.2 — Verify prior-content bytes
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — Verification of `prior_hash` against `prior_content` before restoring a file. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The exact prior bytes and their SHA-256 verification evidence. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Checks the digest against those prior bytes. [V10 §25.13 / Rollback]
- Gives out: DESIGNED — The prior-content verification result. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Restore unverified content through the protected startup worker. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Verification failure in startup recovery halts the worker and keeps N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.12.1 — Decrypt the restoration package: supplies the protected entry; C-BGMM.6.2.3 — Prior-content hash: supplies its verification digest. [V10 §25.13 / Rollback]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.12.3 — Restore prior content | The prior-byte verification result. | Requires a successful check before restoration. | Failed verification keeps recovery halted. | [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker] |

SUB-PARTS: NONE

### C-BGMM.12.3 — Restore prior content
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — Restoration of the exact verified `prior_content`. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The listed destination and verified prior bytes. [V10 §25.13 / Rollback]
- Does: DESIGNED — Restores those bytes to that file; a file already matching them is not rewritten. [V10 §25.13 / Rollback]
- Gives out: DESIGNED — The file's exact prior content. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Write an unlisted destination or rewrite an already matching file. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Rollback]
- Fails closed by: DESIGNED — Failed startup restoration halts the worker and leaves N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2.2 — Exact prior file content: supplies the backup bytes. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.12.2 — Verify prior-content bytes: verification precedes restoration; C-BGMM.7.3 — Exact recovery scope: automatic recovery is confined to listed files. [V10 §25.13 / Rollback] [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.12.4 — Restore prior signature and metadata | Completion of prior-content restoration. | Restores signature and metadata next. | The source's restoration order is preserved. | [V10 §25.13 / Rollback] |

SUB-PARTS: NONE

### C-BGMM.12.4 — Restore prior signature and metadata
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — Restoration of `prior_signature` and the metadata named `prior_metadata` in rollback prose. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The prior code signature where applicable and the package's `file_metadata` containing permissions, timestamps and attributes. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Does: DESIGNED — Restores `prior_signature` and `prior_metadata` after prior-content restoration, as the rollback sequence specifies. [V10 §25.13 / Rollback]
- Gives out: DESIGNED — Prior signatures and file metadata restored with the prior bytes. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Extend automatic recovery beyond the metadata and prior signatures named in the package. [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Restoration failure during startup recovery leaves N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2.4 — Prior code signature: supplies the signature when applicable; C-BGMM.6.2.6 — File restoration metadata: supplies the three restoration metadata categories. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.12.3 — Restore prior content: prior-content restoration precedes this step. [V10 §25.13 / Rollback]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.12.5 — Restore the verified prior manifest
Stamp: DESIGNED    Source: [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — Restoration of the prior signed manifest version from provenance history. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The referenced prior signed version and its signature. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Re-verifies that version's signature and restores it as the signed manifest. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The verified prior signed-manifest state. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Must never: DESIGNED — Restore an unverified prior signed version. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Fails closed by: DESIGNED — Failed verification or restoration in startup recovery keeps N.H stopped. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.4 — Manifest provenance history: supplies the prior signed bytes; C-BGMM.6.2.5 — Prior manifest version: identifies the needed version. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.5.3 — Pinned public verification key: the prior signature is checked against the anchored public trust basis. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Changes: DESIGNED — C-BGMM.5 — Signed-manifest trust anchor: returns to the verified prior version. [V10 §25.13 / Rollback]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.12.6 — Already-matching-file idempotency
Stamp: DESIGNED    Source: [V10 §25.13 / Rollback]

ALONE
- What it is: DESIGNED — The no-write result when a file already matches `prior_content`. [V10 §25.13 / Rollback]
- Takes in: DESIGNED — The current file and its exact prior content. [V10 §25.13 / Rollback]
- Does: DESIGNED — Skips the write if they already match, so a restarted rollback can run again from the files' current state. [V10 §25.13 / Rollback] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — The already-correct prior file without another write. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Rewrite a file that already matches the prior content. [V10 §25.13 / Rollback]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.12 — Idempotent rollback: supplies the file and prior-content comparison. [V10 §25.13 / Rollback]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13 — Volatile maintenance session state
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `BGMM_session_state`, held in memory only across the active maintenance session. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — `session_id`, `declared_purpose`, `declared_change`, `scope`, `authorization_factors`, `session_status`, `opened_at`, `expires_at`, `write_token_active`, `applied_changes` and `rollback_checkpoint`. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — Holds session state without carrying it across restarts; maintains `applied_changes` as an append-only list and `rollback_checkpoint` as the file-list/`hash_before` verification reference into the encrypted package. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — Current maintenance state; persistent maintenance artifacts are the protected rollback package, permanent append-only change log, signed manifest and manifest provenance history. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Persist active-session authority across restart or treat checkpoint hashes as backups. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — A crash loses the state and OS process exit revokes the token; protected recovery must complete before N.H starts. [V10 §25.13 / Crash, Restart, Offline Behavior]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: establishes the authorized session; C-BGMM.10 — Protected change sequence: supplies applied-change facts. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State]
- Gated by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: any listed trigger closes current write authority. [V10 §25.13 / Automatic Relocking]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8 — Maintenance entry sequence | The current session-state destination. | Records the authorized opening and write token. | A bounded volatile window exists. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State] |
| 2 · DESIGNED | C-BGMM.11 — Immediate automatic relocking | Current expiry, token and applied-change state. | Closes and revokes on any listed trigger. | Partial changes take rollback. | [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State] |
| 3 · DESIGNED | C-BGMM.13.1 — Maintenance session identifier | The current maintenance identity. | Carries session_id. | State and package refer to the same session. | [V10 §25.13 / BGMM-Owned State] |
| 4 · DESIGNED | C-BGMM.13.4 — Declared file scope | The current declared scope. | Retains the exact file list. | No undeclared target is authorized. | [V10 §25.13 / BGMM-Owned State] |
| 5 · DESIGNED | C-BGMM.13.6 — Maintenance session status | The volatile session-status field. | Holds current status without inventing an enumeration. | Active status does not persist across restart. | [V10 §25.13 / BGMM-Owned State] |
| 6 · DESIGNED | C-BGMM.16.1 — Open-session crash | The open volatile state. | Loses it on process crash. | Old session authority is not restored. | [V10 §25.13 / Crash, Restart, Offline Behavior] |

SUB-PARTS: C-BGMM.13.1 — Maintenance session identifier; C-BGMM.13.2 — Declared maintenance purpose; C-BGMM.13.3 — Declared maintenance change; C-BGMM.13.4 — Declared file scope; C-BGMM.13.5 — Session authorization factors; C-BGMM.13.6 — Maintenance session status; C-BGMM.13.7 — Maintenance opening time; C-BGMM.13.8 — Maintenance expiration time; C-BGMM.13.9 — Write-token activity; C-BGMM.13.10 — Applied-change list; C-BGMM.13.11 — Rollback verification checkpoint

### C-BGMM.13.1 — Maintenance session identifier
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `session_id`, the maintenance-session identity carried in state and rollback package. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Takes in: DESIGNED — The identity of the maintenance session. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — Binds the session's state/package and the session component of `bgmm_confirmation:<session_id>:<purpose>`. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — The maintenance session reference. [V10 §25.13 / BGMM-Owned State]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.13 — Volatile maintenance session state: carries the current session identity. [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6 — Encrypted rollback package | The maintenance session_id. | Includes it in rollback_package. | The package stays linked to its session. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] |

SUB-PARTS: NONE

### C-BGMM.13.2 — Declared maintenance purpose
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `declared_purpose` in the active state. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — One of `code_change`, `configuration_change`, `security_policy_change`, `device_trust_change`, `emergency_recovery`. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Retains the purpose declared before authorization for factor and scope selection. [V10 §25.13 / Entering Maintenance Mode]
- Gives out: DESIGNED — The session's declared purpose. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Use this declaration to widen emergency recovery into code/configuration changes. [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the recorded controlled purpose. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.3 — Declared maintenance change
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `declared_change`, the specific intended maintenance change. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — Ness's plain-language change declaration. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Retains that recorded change as part of the active session and file-scope basis. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / File Scope Enforcement]
- Gives out: DESIGNED — The session's declared change. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Include private content in descriptions shown to Ness or sent to the phone. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the specific recorded change. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.14.1 — Human-visible and phone descriptions: excludes private content from the description surfaces. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.4 — Declared file scope
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `scope`, the exact file list derived from declared purpose and change. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / File Scope Enforcement]
- Takes in: DESIGNED — The declared purpose and specific change. [V10 §25.13 / File Scope Enforcement]
- Does: DESIGNED — Carries the file boundary enforced by the scoped `nh_system` token. [V10 §25.13 / File Scope Enforcement]
- Gives out: DESIGNED — The current session's exact allowed file scope. [V10 §25.13 / File Scope Enforcement]
- Must never: DESIGNED — Admit undeclared files or emergency code/configuration writes. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Purpose-Specific Authorization]
- Fails closed by: DESIGNED — Writes outside the scope are blocked and immediately logged. [V10 §25.13 / File Scope Enforcement]

TOGETHER
- Fed by: DESIGNED — C-BGMM.13 — Volatile maintenance session state: retains the session's scope. [V10 §25.13 / BGMM-Owned State]
- Gated by: DESIGNED — C-BGMM.9 — Exact file-scope enforcement: enforces this actual file list. [V10 §25.13 / File Scope Enforcement]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.5 — Session authorization factors
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `authorization_factors` in active maintenance state. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — The factor results required by the declared purpose. [V10 §25.13 / Purpose-Specific Authorization]
- Does: DESIGNED — Retains the applicable authorization-factor state without storing recovery-code values or biometric content. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gives out: DESIGNED — The session's factor state. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Treat a different purpose's factors as wider authority or retain raw recovery values. [V10 §25.13 / Purpose-Specific Authorization] [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Fails closed by: DESIGNED — Missing required factors do not open the maintenance window. [V10 §25.13 / Purpose-Specific Authorization]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: supplies the applicable verified factor results. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.2 — Protected purposes and factors: defines the required conjunction for the exact purpose. [V10 §25.13 / Purpose-Specific Authorization]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.6 — Maintenance session status
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `session_status`, the status field in `BGMM_session_state`. [V10 §25.13 / BGMM-Owned State]
- Takes in: NOT DECIDED
- Does: DESIGNED — Holds current maintenance-session status in volatile state; the source supplies no enumeration or serialized value set. [V10 §25.13 / BGMM-Owned State]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Persist active maintenance state across restart. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.13 — Volatile maintenance session state: owns this current status field. [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.7 — Maintenance opening time
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `opened_at`, the maintenance opening-time field. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — The time of the authorized maintenance-window opening. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Holds that opening time in the volatile session record. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — The current session's opening-time value. [V10 §25.13 / BGMM-Owned State]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.6 — Scoped maintenance window: supplies the authorized opening occurrence. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.13.8 — Maintenance expiration time
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `expires_at`, the maintenance timeout boundary. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — The session's expiration time under the build-time timeout setting. [V10 §25 / Build-Time Implementation Settings] [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Holds the time whose arrival immediately closes the window. [V10 §25.13 / Automatic Relocking]
- Gives out: DESIGNED — The timeout boundary for current maintenance authority. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Keep write authority active after `expires_at`. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Reaching the boundary triggers immediate revocation and partial-change rollback. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.18.1 — Empirical maintenance timeout: supplies the build-time calibrated duration without a fixed value selected here. [V10 §25 / Build-Time Implementation Settings]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.11.2 — Timeout relock | The current expires_at value. | Closes the window when reached. | Timeout removes write authority immediately. | [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: NONE

### C-BGMM.13.9 — Write-token activity
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `write_token_active`, the active state of the scoped `nh_system` token. [V10 §25.13 / BGMM-Owned State] [V10 §25.13 / Entering Maintenance Mode]
- Takes in: DESIGNED — Authorized token grant or any immediate relock/revocation. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Tracks current scoped write authority; relock immediately revokes it and process exit revokes it on crash. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — Current token activity within the volatile session. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Carry token activity across a relock or restart. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — Revocation immediately removes protected-file write authority. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.6 — Scoped maintenance window: supplies the bounded grant. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: any trigger revokes the token. [V10 §25.13 / Automatic Relocking]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.8.6 — Scoped maintenance window | The token-activity state. | Records the bounded token grant. | The authorized window has current write authority. | [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / BGMM-Owned State] |
| 2 · DESIGNED | C-BGMM.11 — Immediate automatic relocking | The active token state. | Revokes it immediately on relock. | Protected-file write authority ends. | [V10 §25.13 / Automatic Relocking] |

SUB-PARTS: NONE

### C-BGMM.13.10 — Applied-change list
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `applied_changes`, an append-only list in maintenance-session state. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — Applied maintenance-change entries. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — Appends the changes to the session's list without rewriting earlier entries in it. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — The active session's applied-change list. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Treat the list as a persistent replacement for the permanent change log or rewrite its earlier entries. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.10 — Protected change sequence: supplies the applied changes. [V10 §25.13 / Change Application] [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10 — Protected change sequence | The append-only applied-change state. | Appends actual applied changes. | Earlier list entries are not rewritten. | [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: NONE

### C-BGMM.13.11 — Rollback verification checkpoint
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `rollback_checkpoint`, a verification reference containing the file list and `hash_before` values. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — The file list and prior hashes that point into the encrypted rollback package. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — References that actual package for restoration evidence. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — The current verification checkpoint. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Treat hashes alone as backups or omit the actual full-content package. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: holds the real restoration content; C-BGMM.13.11.1 — Checkpoint file list: identifies the files; C-BGMM.13.11.2 — Checkpoint prior hashes: supplies `hash_before` verification values. [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.13.11.2 — Checkpoint prior hashes | The checkpoint's verification-reference role. | Retains hash_before as evidence only. | Hashes alone cannot restore file content. | [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: C-BGMM.13.11.1 — Checkpoint file list; C-BGMM.13.11.2 — Checkpoint prior hashes

### C-BGMM.13.11.1 — Checkpoint file list
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — The file-list component of `rollback_checkpoint`. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — The files referenced by the rollback checkpoint. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — Associates the verification reference with its listed restoration files. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — The checkpoint's file list. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Replace the package's actual restoration content with this list. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.6.2 — Rollback file entries: supplies the in-scope files whose restoration data the checkpoint references. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.13.11 — Rollback verification checkpoint | The checkpoint file list. | References the actual restoration entries. | The checkpoint does not become a backup. | [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: NONE

### C-BGMM.13.11.2 — Checkpoint prior hashes
Stamp: DESIGNED    Source: [V10 §25.13 / BGMM-Owned State]

ALONE
- What it is: DESIGNED — `hash_before` values in the rollback checkpoint. [V10 §25.13 / BGMM-Owned State]
- Takes in: DESIGNED — The prior-file verification hashes referenced by the checkpoint. [V10 §25.13 / BGMM-Owned State]
- Does: DESIGNED — Carries verification evidence pointing to the encrypted package. [V10 §25.13 / BGMM-Owned State]
- Gives out: DESIGNED — The checkpoint's prior-hash values. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Use these hashes as substitutes for byte-for-byte backups. [V10 §25.13 / BGMM-Owned State]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.13.11 — Rollback verification checkpoint: contains these values as verification references. [V10 §25.13 / BGMM-Owned State]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.13.11 — Rollback verification checkpoint | The hash_before verification values. | Carries prior-hash references into the protected package. | Exact backup content remains separately required. | [V10 §25.13 / BGMM-Owned State] |

SUB-PARTS: NONE

### C-BGMM.14 — Maintenance privacy
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — Protection of private content throughout an open maintenance window. [V10 §25.13 / Privacy During Maintenance]
- Takes in: DESIGNED — Human/phone descriptions, rollback metadata, change logs, security events and protected file content. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Keeps descriptions and logs structural-only while exact rollback bytes stay encrypted, sealed and integrity-protected inside their restricted package. [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM]
- Gives out: DESIGNED — Structural paths, operations and hashes in the permitted metadata/audit surfaces; protected content remains within its authorized boundary. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Grant human-visible protected-content access merely because maintenance is open, or put secrets, private memory, health records or sensitive content in maintenance descriptions, logs or phone-confirmation payloads. [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): its protection rules remain applicable throughout maintenance. [MAP C-BGMM]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6 — Encrypted rollback package | The maintenance privacy boundary. | Keeps protected content out of metadata/audit fields. | Exact prior bytes remain encrypted inside the package. | [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance] |
| 2 · DESIGNED | C-BGMM.14.1 — Human-visible and phone descriptions | The no-content-access rule. | Keeps visible and phone descriptions nonprivate. | Opening maintenance grants no content disclosure. | [V10 §25.13 / Privacy During Maintenance] |
| 3 · DESIGNED | C-BGMM.14.2 — Rollback metadata privacy | The metadata/content separation. | Keeps package metadata structural-only. | Private backup bytes remain in the protected package. | [V10 §25.13 / Privacy During Maintenance] |
| 4 · DESIGNED | C-BGMM.14.3 — Structural change-log content | The structural-only log rule. | Records paths, operations and hashes. | File content stays outside change logs. | [V10 §25.13 / Privacy During Maintenance] |
| 5 · DESIGNED | C-BGMM.14.4 — Structural security-audit content | The security-event content restriction. | Records structural facts only. | Protected file content cannot enter event fields. | [V10 §25.13 / Privacy During Maintenance] |
| 6 · DESIGNED | C-BGMM.14.5 — Sensitive maintenance-content exclusion | The continuing privacy boundary. | Excludes secrets and sensitive material across listed surfaces. | Maintenance does not relax those exclusions. | [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM] |

SUB-PARTS: C-BGMM.14.1 — Human-visible and phone descriptions; C-BGMM.14.2 — Rollback metadata privacy; C-BGMM.14.3 — Structural change-log content; C-BGMM.14.4 — Structural security-audit content; C-BGMM.14.5 — Sensitive maintenance-content exclusion

### C-BGMM.14.1 — Human-visible and phone descriptions
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — The privacy boundary on change descriptions shown to Ness or sent to the phone. [V10 §25.13 / Privacy During Maintenance]
- Takes in: DESIGNED — The declared change's visible or transmitted description. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Keeps that description free of private content. [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — A structural maintenance description or confirmation prompt. [MAP C-BGMM]
- Must never: DESIGNED — Include protected file content, secrets, private memory, health material or sensitive content in those descriptions or prompts. [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.14 — Maintenance privacy: an open maintenance window does not remove privacy restrictions. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.6.1 — Rollback change description | The private-content prohibition. | Keeps change_description structural. | Audit linkage does not reveal protected content. | [V10 §25.13 / Privacy During Maintenance] |
| 2 · DESIGNED | C-BGMM.8.1 — Purpose declaration | The allowed description boundary. | Records the purpose/change without private content. | The declaration remains safe for its visible surfaces. | [V10 §25.13 / Privacy During Maintenance] |
| 3 · DESIGNED | C-BGMM.8.3 — Trusted-phone confirmation | The phone-payload content restriction. | Displays only a nonprivate purpose/change description. | Confirmation cannot disclose protected file content. | [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance] |
| 4 · DESIGNED | C-BGMM.13.3 — Declared maintenance change | The visible-description privacy rule. | Retains a nonprivate declared_change. | Its display or transmission stays bounded. | [V10 §25.13 / Privacy During Maintenance] |

SUB-PARTS: NONE

### C-BGMM.14.2 — Rollback metadata privacy
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — The separation between encrypted rollback content and package metadata/audit fields. [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM]
- Takes in: DESIGNED — Rollback-package metadata and audit linkage. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Keeps these fields structural-only; the full prior bytes stay protected in the encrypted package. [MAP C-BGMM]
- Gives out: DESIGNED — Non-content metadata distinct from the exact restoration content. [MAP C-BGMM]
- Must never: DESIGNED — Expose private content through package metadata or audit fields. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies the package whose metadata/content boundary is preserved. [V10 §25.13 / Encrypted Full-Content Rollback Packages]
- Gated by: DESIGNED — C-BGMM.14 — Maintenance privacy: requires structural-only metadata. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.14.3 — Structural change-log content
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — The permitted content of the permanent maintenance change log. [V10 §25.13 / Privacy During Maintenance]
- Takes in: DESIGNED — File paths, operations and hashes. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Records those structural facts without file content. [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — Structural change provenance. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Write protected file content, secrets, private memory, health material or sensitive content into the log. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.14 — Maintenance privacy: the log remains content-free throughout maintenance. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.1 — Flush the change-log entry | The structural-only log boundary. | Writes paths, operations and hashes without content. | Pre-change provenance cannot expose protected files. | [V10 §25.13 / Privacy During Maintenance] |

SUB-PARTS: NONE

### C-BGMM.14.4 — Structural security-audit content
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — The structural-only maintenance security-audit boundary. [V10 §25.13 / Privacy During Maintenance]
- Takes in: DESIGNED — The real security event's structural facts. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Records the event without content from protected files. [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — A structural maintenance security-audit record. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Put protected content or sensitive material into security-event fields. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.14 — Maintenance privacy: the audit record retains the content prohibition. [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.15 — Immediate security audit events | The structural-only security-event boundary. | Excludes protected file content from every event. | Maintenance audit does not expose private content. | [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Protected Material Boundary] |

SUB-PARTS: NONE

### C-BGMM.14.5 — Sensitive maintenance-content exclusion
Stamp: DESIGNED    Source: [V10 §25.13 / Privacy During Maintenance]

ALONE
- What it is: DESIGNED — The exclusion of secrets, private memory, health records and sensitive content from maintenance communication and logs. [V10 §25.13 / Privacy During Maintenance]
- Takes in: DESIGNED — Any maintenance description, log entry or phone-confirmation payload. [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Preserves the privacy restriction across every listed surface even while maintenance is open. [V10 §25.13 / Privacy During Maintenance]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Place any of those sensitive content classes in a maintenance description, log entry or phone-confirmation payload. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.14 — Maintenance privacy: open maintenance cannot grant human-visible content access. [V10 §25.13 / Privacy During Maintenance] [MAP C-BGMM]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15 — Immediate security audit events
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — The maintenance security event vocabulary under immediate write-and-flush timing. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — Actual session, token, change, hash-registry, scope, rollback, integrity and immutable-write events. [V10 §25.13 / Immediate Security Audit Events]
- Does: DESIGNED — Writes and flushes every event before its producing function returns; preserves one permanent operational record per real event without an automatic log-about-logging chain. [V10 §25.13 / Immediate Security Audit Events] [V10 §0B]
- Gives out: DESIGNED — Structural-only permanent audit records for the seventeen named event kinds. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Return before the event is written and flushed, expose protected file content, alter earlier audit records or treat logs as extra truth evidence. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance] [V10 §0B]
- Fails closed by: DESIGNED — A failure at the post-touch `bgmm_change_applied` step triggers immediate rollback; no wider audit-failure mechanism is supplied here. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM — Biometric-Gated Maintenance Mode (§25.13): supplies its actual maintenance events. [V10 §25.13 / Immediate Security Audit Events]
- Gated by: DESIGNED — C-BGMM.14.4 — Structural security-audit content: forbids protected content in the records; C-BGMM.3.4 — Audit-entry protection: preserves earlier entries. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Protected Material Boundary]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.10.7 — Record the applied change | The immediate structural audit rule. | Writes and flushes bgmm_change_applied. | Failure at this post-touch step triggers rollback. | [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance] |
| 2 · DESIGNED | C-BGMM.15.1 — Session-initiated event | The initiation event name and recording rule. | Flushes the initiation fact before return. | No protected content enters the event. | [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance] |
| 3 · DESIGNED | C-BGMM.15.2 — Session-opened event | The opening-event timing boundary. | Flushes the structural opening record. | The producing function cannot defer its event. | [V10 §25.13 / Immediate Security Audit Events] |
| 4 · DESIGNED | C-BGMM.15.3 — Write-token-granted event | The token-grant recording rule. | Records the actual bounded grant immediately. | Secret token content stays out of ordinary audit fields. | [V10 §25.13 / Immediate Security Audit Events] |
| 5 · DESIGNED | C-BGMM.15.4 — Change-log-entry event | The named change-log-entry event rule. | Retains pre-change structural provenance. | The entry is flushed before file touch. | [V10 §25.13 / Immediate Security Audit Events] |
| 6 · DESIGNED | C-BGMM.15.5 — Change-applied event | The immediate change-applied audit rule. | Flushes the final-step event. | An audit-step failure invokes post-touch rollback. | [V10 §25.13 / Immediate Security Audit Events] |
| 7 · DESIGNED | C-BGMM.15.6 — Hash-registry-updated event | The hash-registry-updated name and flush rule. | Records that event structurally. | No additional registry schema is inferred. | [V10 §25.13 / Immediate Security Audit Events] |
| 8 · DESIGNED | C-BGMM.15.7 — Out-of-scope-attempt event | The immediate blocked-attempt recording rule. | Flushes the out-of-scope refusal fact. | The target write remains blocked. | [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance] |
| 9 · DESIGNED | C-BGMM.15.8 — Session-completed event | The completion-event recording boundary. | Flushes the actual session completion. | The record contains no protected change content. | [V10 §25.13 / Immediate Security Audit Events] |
| 10 · DESIGNED | C-BGMM.15.9 — Write-token-revoked event | The revocation event's flush requirement. | Records removal of write authority. | The relock fact is permanent and structural. | [V10 §25.13 / Immediate Security Audit Events] |
| 11 · DESIGNED | C-BGMM.15.10 — Rollback-triggered event | The rollback-trigger event rule. | Flushes the actual trigger. | Triggering is not represented as successful restoration. | [V10 §25.13 / Immediate Security Audit Events] |
| 12 · DESIGNED | C-BGMM.15.11 — Rollback-completed event | The completed-rollback recording rule. | Flushes verified completion before startup. | N.H cannot start before the required recovery record. | [V10 §25.13 / Immediate Security Audit Events] |
| 13 · DESIGNED | C-BGMM.15.12 — Rollback-failed event | The failure-event name and timing. | Flushes the actual rollback failure. | N.H remains stopped for authorized repair. | [V10 §25.13 / Immediate Security Audit Events] |
| 14 · DESIGNED | C-BGMM.15.13 — Session-timed-out event | The timeout-event recording requirement. | Records actual session expiration. | The event does not preserve expired write authority. | [V10 §25.13 / Immediate Security Audit Events] |
| 15 · DESIGNED | C-BGMM.15.14 — Session-aborted event | The abort-event timing rule. | Flushes the structural abort record. | The aborted window remains relocked. | [V10 §25.13 / Immediate Security Audit Events] |
| 16 · DESIGNED | C-BGMM.15.15 — Integrity-check-failed event | The integrity-failure recording boundary. | Writes and flushes the failed check. | Failed startup remains stopped. | [V10 §25.13 / Immediate Security Audit Events] |
| 17 · DESIGNED | C-BGMM.15.16 — Integrity-check-passed event | The integrity-pass event rule. | Records the successful check structurally. | The audit contains no protected file content. | [V10 §25.13 / Immediate Security Audit Events] |
| 18 · DESIGNED | C-BGMM.15.17 — Immutable-write-blocked event | The immutable-write-blocked recording rule. | Flushes the blocked attempt. | Immutable content stays unchanged and undisclosed. | [V10 §25.13 / Immediate Security Audit Events] |

SUB-PARTS: C-BGMM.15.1 — Session-initiated event; C-BGMM.15.2 — Session-opened event; C-BGMM.15.3 — Write-token-granted event; C-BGMM.15.4 — Change-log-entry event; C-BGMM.15.5 — Change-applied event; C-BGMM.15.6 — Hash-registry-updated event; C-BGMM.15.7 — Out-of-scope-attempt event; C-BGMM.15.8 — Session-completed event; C-BGMM.15.9 — Write-token-revoked event; C-BGMM.15.10 — Rollback-triggered event; C-BGMM.15.11 — Rollback-completed event; C-BGMM.15.12 — Rollback-failed event; C-BGMM.15.13 — Session-timed-out event; C-BGMM.15.14 — Session-aborted event; C-BGMM.15.15 — Integrity-check-failed event; C-BGMM.15.16 — Integrity-check-passed event; C-BGMM.15.17 — Immutable-write-blocked event

### C-BGMM.15.1 — Session-initiated event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_session_initiated`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — Structural facts of the maintenance-session initiation. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Immediate Security Audit Events]
- Does: DESIGNED — Records initiation and flushes its event before the producing function returns. [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The permanent initiation audit record. [V10 §0B] [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Put protected content in the initiation record or defer its flush beyond function return. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Immediate Security Audit Events]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: fixes the event vocabulary, timing and structural-only boundary. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.2 — Session-opened event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_session_opened`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The authorized window's opening fact. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Immediate Security Audit Events]
- Does: DESIGNED — Writes and flushes the structural opening event before function return. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The session-opening audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Expose the protected change content in that event. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.6 — Scoped maintenance window: supplies the actual opening. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires write/flush before the function returns. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.3 — Write-token-granted event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_write_token_granted`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The grant of the scoped `nh_system` write token. [V10 §25.13 / Entering Maintenance Mode]
- Does: DESIGNED — Records the structural grant fact immediately and flushes it before return. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The token-grant audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Include protected content or live secret values in the grant log. [V10 §25.13 / Privacy During Maintenance] [V10 §0B]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.8.6 — Scoped maintenance window: grants the actual bounded token. [V10 §25.13 / Entering Maintenance Mode]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires immediate structural recording. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.4 — Change-log-entry event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_change_log_entry`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The structural paths, operations and hashes recorded before the change. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Change Application]
- Does: DESIGNED — Preserves the pre-change entry under immediate write/flush timing. [V10 §25.13 / Change Application] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — Permanent structural change provenance. [V10 §25.13 / BGMM-Owned State]
- Must never: DESIGNED — Record file content or touch a protected file before the entry is flushed. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Change Application]
- Fails closed by: DESIGNED — The protected write cannot precede the flushed change-log entry. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.1 — Flush the change-log entry: supplies the actual pre-change operation. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: keeps this event within the immediate structural audit rule. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.5 — Change-applied event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Change Application]

ALONE
- What it is: DESIGNED — `bgmm_change_applied`, the seventh protected-change step's audit event. [V10 §25.13 / Change Application]
- Takes in: DESIGNED — The applied change after hashing and signing steps. [V10 §25.13 / Change Application]
- Does: DESIGNED — Writes the security event immediately and flushes it before the producing function returns. [V10 §25.13 / Change Application] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural change-applied record. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Treat an unrecorded applied change as completion or disclose the changed protected content. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — A failure at this post-touch step triggers immediate rollback. [V10 §25.13 / Change Application]

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.7 — Record the applied change: produces the actual final-step event. [V10 §25.13 / Change Application]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: governs the flush boundary. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.6 — Hash-registry-updated event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_hash_registry_updated`, a named immediate security event. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: NOT DECIDED
- Does: DESIGNED — Writes and flushes this event before its producing function returns; the event list does not define an additional registry schema. [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural hash-registry-update audit record. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Put protected file content into this audit entry. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: supplies the named event and mandatory write/flush timing. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.7 — Out-of-scope-attempt event
Stamp: DESIGNED    Source: [V10 §25.13 / File Scope Enforcement]

ALONE
- What it is: DESIGNED — `bgmm_out_of_scope_write_attempt`. [V10 §25.13 / File Scope Enforcement]
- Takes in: DESIGNED — A blocked attempt outside the declared file list. [V10 §25.13 / File Scope Enforcement]
- Does: DESIGNED — Records the attempt immediately in the security audit and flushes before return. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural out-of-scope-attempt record. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Omit the attempt record or include protected content in it. [V10 §25.13 / File Scope Enforcement] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — The associated out-of-scope write remains blocked. [V10 §25.13 / File Scope Enforcement]

TOGETHER
- Fed by: DESIGNED — C-BGMM.9.1 — Out-of-scope write refusal: supplies the actual blocked attempt. [V10 §25.13 / File Scope Enforcement]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: governs flush timing and structural content. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.8 — Session-completed event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_session_completed`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — Completion after the change is applied, verified and logged. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Records completion structurally with the mandatory immediate write/flush timing. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The maintenance-completion audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Include protected change content in the completion record. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.11.1 — Completion relock: supplies the actual completion boundary. [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires the event to be flushed before return. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.9 — Write-token-revoked event
Stamp: DESIGNED    Source: [V10 §25.13 / Automatic Relocking]

ALONE
- What it is: DESIGNED — `bgmm_write_token_revoked`. [V10 §25.13 / Automatic Relocking]
- Takes in: DESIGNED — Immediate write-token revocation on any relock. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Writes the revocation event and flushes it before the producing function returns. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural record of revoked write authority. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Omit the revocation record or leave token authority active after relock. [V10 §25.13 / Automatic Relocking]
- Fails closed by: DESIGNED — Revoked write authority cannot continue the protected change. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11 — Immediate automatic relocking: supplies the actual revocation. [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires structural recording and flushing. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.10 — Rollback-triggered event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_rollback_triggered`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The actual rollback trigger after a post-touch failure or relock with a partial change. [V10 §25.13 / Change Application] [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Records that rollback was triggered and flushes before function return. [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — A structural trigger record, without asserting rollback success. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Include protected package content in the event. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.10.8 — Post-touch failure rollback: triggers immediate rollback on failure; C-BGMM.11 — Immediate automatic relocking: triggers rollback for a partial change. [V10 §25.13 / Change Application] [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: fixes the recording boundary. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.11 — Rollback-completed event
Stamp: DESIGNED    Source: [V10 §25.13 / Protected Startup Recovery Worker]

ALONE
- What it is: DESIGNED — `bgmm_rollback_completed`. [V10 §25.13 / Protected Startup Recovery Worker]
- Takes in: DESIGNED — Verified successful rollback. [V10 §25.13 / Protected Startup Recovery Worker]
- Does: DESIGNED — Writes the completed-rollback fact before N.H starts and flushes it before the producing function returns. [V10 §25.13 / Crash, Restart, Offline Behavior] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural record of completed restoration. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Record unverified recovery as completed or start N.H before the required completion record. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — Failed recovery keeps N.H stopped and does not reach verified completion. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7.4 — Verified recovery completion: supplies the actual verified completion. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires immediate flush of the event. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.12 — Rollback-failed event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_rollback_failed`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The actual rollback failure's structural facts. [V10 §25.13 / Protected Startup Recovery Worker] [V10 §25.13 / Privacy During Maintenance]
- Does: DESIGNED — Writes and flushes the failure event before function return while failed startup recovery leaves N.H stopped. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Protected Startup Recovery Worker]
- Gives out: DESIGNED — The rollback-failure audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Expose rollback content or represent failure as verified completion. [V10 §25.13 / Privacy During Maintenance] [V10 §25.13 / Protected Startup Recovery Worker]
- Fails closed by: DESIGNED — Startup recovery failure leaves the worker halted and N.H stopped for full normal authorization. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: supplies its actual failure outcome. [V10 §25.13 / Protected Startup Recovery Worker]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires the named failure record to be flushed. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.13 — Session-timed-out event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_session_timed_out`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The timeout when `expires_at` is reached. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Records the session timeout under immediate write/flush timing. [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — The structural timeout audit record. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Put private change content into the timeout event. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — The timeout closes the window and revokes the token. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11.2 — Timeout relock: supplies the actual expiration occurrence. [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires write/flush before return. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.14 — Session-aborted event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_session_aborted`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The explicit-abort occurrence. [V10 §25.13 / Automatic Relocking]
- Does: DESIGNED — Writes the structural abort event and flushes before function return. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The session-abort audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Include protected content in the abort record. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — Abort immediately revokes the token and triggers rollback of a partial change. [V10 §25.13 / Automatic Relocking]

TOGETHER
- Fed by: DESIGNED — C-BGMM.11.6 — Explicit-abort relock: supplies the abort fact. [V10 §25.13 / Automatic Relocking]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: governs the immediate record. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.15 — Integrity-check-failed event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_integrity_check_failed`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — A failed startup signature or protected-file-hash verification. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Records the structural integrity failure while preventing N.H startup. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — The flushed integrity-failure security record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Start N.H despite the failure or disclose protected content in the failure event. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — Keeps N.H stopped; BGMM is the only authorized repair path. [V10 §25.13 / Signed-Manifest Trust Anchor]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5 — Startup manifest verification: supplies the actual failed integrity result. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires the event to be written and flushed before return. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.16 — Integrity-check-passed event
Stamp: DESIGNED    Source: [V10 §25.13 / Immediate Security Audit Events]

ALONE
- What it is: DESIGNED — `bgmm_integrity_check_passed`. [V10 §25.13 / Immediate Security Audit Events]
- Takes in: DESIGNED — The successful integrity-check fact. [V10 §25.13 / Immediate Security Audit Events]
- Does: DESIGNED — Writes and flushes the structural pass event before the producing function returns. [V10 §25.13 / Immediate Security Audit Events] [V10 §25.13 / Privacy During Maintenance]
- Gives out: DESIGNED — The integrity-pass audit record. [V10 §25.13 / Immediate Security Audit Events]
- Must never: DESIGNED — Include protected file content in the pass record. [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5 — Startup manifest verification: supplies the actual integrity result. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires immediate structural recording. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.15.17 — Immutable-write-blocked event
Stamp: DESIGNED    Source: [V10 §25.13 / Protected-Core Rules (Unconditional)]

ALONE
- What it is: DESIGNED — `bgmm_immutable_write_blocked`. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Takes in: DESIGNED — An attempted immutable write blocked by scope enforcement. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Does: DESIGNED — Records the blocked attempt and flushes the event before function return. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Immediate Security Audit Events]
- Gives out: DESIGNED — A structural immutable-write refusal record. [V10 §25.13 / Privacy During Maintenance]
- Must never: DESIGNED — Omit the blocked-attempt event or disclose the immutable record's private content. [V10 §25.13 / Protected-Core Rules (Unconditional)] [V10 §25.13 / Privacy During Maintenance]
- Fails closed by: DESIGNED — The attempted write remains blocked. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: DESIGNED — C-BGMM.9.3 — Immutable-write refusal: supplies the actual blocked attempt. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gated by: DESIGNED — C-BGMM.15 — Immediate security audit events: requires the event's immediate write/flush. [V10 §25.13 / Immediate Security Audit Events]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.16 — Crash, restart and offline behavior
Stamp: DESIGNED    Source: [V10 §25.13 / Crash, Restart, Offline Behavior]

ALONE
- What it is: DESIGNED — Maintenance behavior after open-session crash, rollback crash or startup integrity failure, and its offline capability. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Takes in: DESIGNED — Crash/restart state, the protected package and startup integrity results. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Does: DESIGNED — Discards volatile state on crash, loses the token through process exit, runs bounded startup rollback and records completion before N.H starts; restarts an interrupted rollback idempotently. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — Verified recovered prior state or a stopped system requiring authorized repair. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Must never: DESIGNED — Start on an integrity failure or require a network merely to operate BGMM. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — Startup integrity failure keeps N.H stopped; failed protected recovery requires full normal BGMM authorization. [V10 §25.13 / Crash, Restart, Offline Behavior] [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5 — Startup manifest verification: supplies startup integrity truth; C-BGMM.6 — Encrypted rollback package: supplies persistent prior-state restoration material. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gated by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: automatic restoration remains restricted to its verified conditions and listed scope. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.16.1 — Open-session crash | The open-session crash case. | Loses state/token authority and runs bounded rollback. | Recovery must complete before N.H starts. | [V10 §25.13 / Crash, Restart, Offline Behavior] |
| 2 · DESIGNED | C-BGMM.16.2 — Crash during rollback | The interrupted-rollback case. | Retries restoration from current files on restart. | Idempotency preserves already matching content. | [V10 §25.13 / Crash, Restart, Offline Behavior] |

SUB-PARTS: C-BGMM.16.1 — Open-session crash; C-BGMM.16.2 — Crash during rollback; C-BGMM.16.3 — Startup integrity failure; C-BGMM.16.4 — Offline maintenance

### C-BGMM.16.1 — Open-session crash
Stamp: DESIGNED    Source: [V10 §25.13 / Crash, Restart, Offline Behavior]

ALONE
- What it is: DESIGNED — Crash during an open maintenance session. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Takes in: DESIGNED — The crash and persisted rollback package. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Does: DESIGNED — Loses session state, revokes the token through OS process exit and runs startup rollback; writes `bgmm_rollback_completed` before N.H starts. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: DESIGNED — Verified restored prior state without revived maintenance authority. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Must never: DESIGNED — Reuse the lost session's write authority or start N.H before required recovery completes. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — Recovery failure keeps N.H stopped for full normal BGMM entry. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.16 — Crash, restart and offline behavior: supplies the open-session crash case. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gated by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: bounds automatic restoration. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: DESIGNED — C-BGMM.13 — Volatile maintenance session state: is lost on process crash. [V10 §25.13 / Crash, Restart, Offline Behavior]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.16.2 — Crash during rollback
Stamp: DESIGNED    Source: [V10 §25.13 / Crash, Restart, Offline Behavior]

ALONE
- What it is: DESIGNED — Interruption while rollback is in progress. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Takes in: DESIGNED — Whatever state the files are in after the rollback crash. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Does: DESIGNED — On restart, triggers rollback again from that state; matching prior files receive no repeat write. [V10 §25.13 / Crash, Restart, Offline Behavior] [V10 §25.13 / Rollback]
- Gives out: DESIGNED — Idempotent restoration toward the exact prior state. [V10 §25.13 / Rollback]
- Must never: DESIGNED — Treat interrupted rollback as completed or rewrite a file already matching prior content. [V10 §25.13 / Crash, Restart, Offline Behavior] [V10 §25.13 / Rollback]
- Fails closed by: DESIGNED — The startup worker still halts on any decrypt, verify or restore failure. [V10 §25.13 / Protected Startup Recovery Worker]

TOGETHER
- Fed by: DESIGNED — C-BGMM.16 — Crash, restart and offline behavior: supplies the interrupted rollback case. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gated by: DESIGNED — C-BGMM.7 — Protected startup recovery worker: applies the same verified recovery boundary after restart. [V10 §25.13 / Protected Startup Recovery Worker]
- Changes: DESIGNED — C-BGMM.12 — Idempotent rollback: resumes restoration from the current file state. [V10 §25.13 / Crash, Restart, Offline Behavior]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.16.3 — Startup integrity failure
Stamp: DESIGNED    Source: [V10 §25.13 / Crash, Restart, Offline Behavior]

ALONE
- What it is: DESIGNED — An integrity-check failure before N.H startup. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Takes in: DESIGNED — Failed manifest signature or protected-file hash. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Does: DESIGNED — Prevents N.H from starting and records the integrity failure. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gives out: DESIGNED — A stopped system with repair restricted to authorized BGMM entry. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Must never: DESIGNED — Bypass integrity through ordinary administrator or remote entry. [V10 §25.13 / What BGMM Is and Is Not] [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: DESIGNED — N.H stays stopped; BGMM is the only authorized repair path. [V10 §25.13 / Crash, Restart, Offline Behavior]

TOGETHER
- Fed by: DESIGNED — C-BGMM.5.5 — Startup manifest verification: supplies the failed integrity result. [V10 §25.13 / Signed-Manifest Trust Anchor]
- Gated by: DESIGNED — C-BGMM.8 — Maintenance entry sequence: repair requires the authorized maintenance path. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.16.4 — Offline maintenance
Stamp: DESIGNED    Source: [V10 §25.13 / Crash, Restart, Offline Behavior]

ALONE
- What it is: DESIGNED — BGMM's fully offline operating capability. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Takes in: NOT DECIDED
- Does: DESIGNED — Operates without requiring a network. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Make network availability a requirement for BGMM operation. [V10 §25.13 / Crash, Restart, Offline Behavior]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.17 — Unconditional protected-core rules
Stamp: DESIGNED    Source: [V10 §25.13 / Protected-Core Rules (Unconditional)]

ALONE
- What it is: DESIGNED — The protected-core limits that maintenance cannot relax. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Takes in: DESIGNED — Protected writes, ordinary PC access, maintenance authority, emergency scope and recovery values. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Does: DESIGNED — Blocks/logs immutable writes; blocks ordinary protected-file modification and resists/detects administrator tampering; keeps authorization temporary and purpose-bound; confines emergency recovery to device trust; keeps recovery-code values out of N.H storage. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Gives out: DESIGNED — Preserved protected material under bounded maintenance authority. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Must never: DESIGNED — Override immutability, allow ordinary direct writes, perpetuate maintenance authorization, grant emergency code-edit authority or store recovery values. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Fails closed by: DESIGNED — Blocks immutable writes with `bgmm_immutable_write_blocked`; ordinary users cannot modify protected material through normal paths. [V10 §25.13 / Protected-Core Rules (Unconditional)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-BGMM.9.3 — Immutable-write refusal: blocks immutable writes; C-BGMM.4 — Normal-path write prevention: enforces ordinary blocking and the qualified tamper chain; C-BGMM.11 — Immediate automatic relocking: removes temporary write authority; C-BGMM.9.2 — Emergency scope override: prevents emergency code/configuration changes; C-BGMM.3.6 — Recovery-value prohibition: keeps recovery values out of N.H storage. [V10 §25.13 / Protected-Core Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

### C-BGMM.18 — Build-time maintenance settings
Stamp: DESIGNED    Source: [V10 §25 / Build-Time Implementation Settings] [MAP C-BGMM]

ALONE
- What it is: DESIGNED — Two settled build-time implementation settings: maintenance timeout duration and the specific hardware-backed key mechanism. [V10 §25 / Build-Time Implementation Settings]
- Takes in: DESIGNED — Real observed maintenance durations and available motherbase hardware. [V10 §25 / Build-Time Implementation Settings]
- Does: DESIGNED — Leaves timeout to empirical deployment calibration and selects the key implementation according to available hardware, while mandatory hardware-backed separation remains fixed. [V10 §25 / Build-Time Implementation Settings]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Reopen either setting as an unresolved conceptual Ness decision or waive hardware-backed key separation. [V10 §25 / Build-Time Implementation Settings] [MAP C-BGMM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.18.1 — Empirical maintenance timeout | The build-time empirical-calibration assignment. | Uses observed real maintenance durations. | The timeout value remains unselected here. | [V10 §25 / Build-Time Implementation Settings] |
| 2 · DESIGNED | C-BGMM.18.2 — Hardware-backed key mechanism | The build-time hardware-selection assignment. | Selects the mechanism from available motherbase hardware. | Hardware-backed key separation stays mandatory. | [V10 §25 / Build-Time Implementation Settings] |

SUB-PARTS: C-BGMM.18.1 — Empirical maintenance timeout; C-BGMM.18.2 — Hardware-backed key mechanism

### C-BGMM.18.1 — Empirical maintenance timeout
Stamp: DESIGNED    Source: [V10 §25 / Build-Time Implementation Settings]

ALONE
- What it is: DESIGNED — The maintenance timeout duration to be calibrated empirically. [V10 §25 / Build-Time Implementation Settings]
- Takes in: DESIGNED — Observed real maintenance durations in deployment. [V10 §25 / Build-Time Implementation Settings]
- Does: DESIGNED — Calibrates the duration from those observations; the architecture supports any value, and the value remains a calibration decision. [V10 §25 / Build-Time Implementation Settings]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Treat the unset numerical duration as an unresolved conceptual authority decision. [V10 §25 / Build-Time Implementation Settings] [MAP C-BGMM]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.18 — Build-time maintenance settings: assigns this choice to empirical calibration. [V10 §25 / Build-Time Implementation Settings]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-BGMM.13.8 — Maintenance expiration time | The empirically calibrated timeout duration. | Carries the current session expiration boundary. | No numerical duration is invented. | [V10 §25 / Build-Time Implementation Settings] |

SUB-PARTS: NONE

### C-BGMM.18.2 — Hardware-backed key mechanism
Stamp: DESIGNED    Source: [V10 §25 / Build-Time Implementation Settings]

ALONE
- What it is: DESIGNED — The specific hardware-backed implementation for the manifest-signing and rollback-sealing keys. [V10 §25 / Build-Time Implementation Settings]
- Takes in: DESIGNED — Available motherbase hardware and its protected-key capabilities. [V10 §25 / Build-Time Implementation Settings]
- Does: DESIGNED — Selects at build time among TPM sealed keys, HSM, OS secure key store or equivalent, while preserving hardware-backed separation. [V10 §25 / Build-Time Implementation Settings]
- Gives out: NOT DECIDED
- Must never: DESIGNED — Collapse the separate key roles or relax hardware-backed protection because a concrete mechanism has not been selected. [V10 §25 / Build-Time Implementation Settings] [V10 §25.6]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-BGMM.18 — Build-time maintenance settings: assigns mechanism selection to available hardware at build time. [V10 §25 / Build-Time Implementation Settings]
- Gated by: DESIGNED — C-BAI.8.1 — Manifest-signing key: keeps its independent signing role; C-BAI.8.2 — Rollback-sealing key: keeps its separate non-derivable, non-exportable protection role. [V10 §25.6] [V10 §25 / Build-Time Implementation Settings]
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|


SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These continuation rows preserve the current TOGETHER relationships at their other endpoint. Earlier files are not edited. Future owners incorporate the rows when written; the register retains both exact endpoint names. Conditions and citations remain in the identified current field.

| USED BY owner | Using card | Current TOGETHER field | Exact current relationship | Disposition |
|---|---|---|---|---|
| C-BAI — Biometric Authorization Interface (§25.6) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): supplies maintenance confirmation bound to the exact session and purpose; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the trusted-phone and applicable recovery authority. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Fed by | DESIGNED — C-BAI — Biometric Authorization Interface (§25.6): supplies maintenance confirmation bound to the exact session and purpose; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the trusted-phone and applicable recovery authority. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] | Pending endpoint placement |
| C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1 — Direct, plain, one-step explanation | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.1 — Direct tone | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.2 — Plain language | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.3 — One step at a time | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.4 — Real tradeoffs | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.5 — Explanation recovery | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.5.1 — Simpler explanation | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.5.2 — Concrete worked example | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.1.5.3 — No increased abstraction | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.2 — Grounded machine-state claims | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.2.1 — Actual-state evidence | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.2.2 — Actual files over remembered descriptions | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.3 — Honest correction | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.4 — Flag and continue | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.5 — Pull Sovereignty | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.6 — Casual communication | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.7 — Understanding pace | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.8 — Shapes and steering | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.9 — Session authority | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.9.1 — Session-control boundary | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.9.2 — No session-pressure suggestions | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.10 — Latest instruction and rejected methods | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.10.1 — Latest explicit instruction | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.10.2 — Rejected-method boundary | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.10.2.1 — Stop using a rejected method | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.10.2.2 — Stop mentioning a rejected method | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.11 — Anti-loop response | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.11.1 — Abandon the current plan | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.11.2 — One-sentence deliverable restatement | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.11.3 — Direct production | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.11.4 — No repeated loops after an answer | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.12 — Actual-file delivery | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.12.1 — Actual downloadable file | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.12.2 — No unrequested delivery substitution | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13 — Version safety | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13.1 — New versioned file | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13.2 — Previous authoritative master preservation | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13.3 — Prior authority until review and adoption | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13.3.1 — Review condition | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.13.3.2 — Adoption condition | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.14 — No invented human-state explanations | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.14.1 — No human-state excuses | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.14.2 — Plain mistake account | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.14.3 — No invented emotional state | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15 — Interaction and delivery event recording | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15.1 — Interaction event recording | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15.2 — Delivery event recording | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15.3 — Interaction-record authorization | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15.3.1 — Record privacy boundary | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-2.15.3.2 — Record identity boundary | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Gated by | DESIGNED — C-2 — Ness Interaction and Artifact-Delivery Contract (§2, §2A — LOCKED): governs every maintenance interaction and artifact delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): protected content remains under its privacy and authorization rules throughout maintenance; C-SACL — Speaker Access-Control Layer (§25.4): a medium-or-higher spoofing or session-level security alert immediately closes the window. [MAP C-2] [MAP C-BGMM] [V10 §25.13 / Automatic Relocking]; DESIGNED — C-2.1 — Direct, plain, one-step explanation: maintenance explanations follow its plain-language rule; C-2.1.1 — Direct tone: communication stays direct; C-2.1.2 — Plain language: the plain version is given directly; C-2.1.3 — One step at a time: explanations present one step at a time; C-2.1.4 — Real tradeoffs: why-yes/why-no answers state actual tradeoffs; C-2.1.5 — Explanation recovery: a failed explanation becomes simpler and concrete; C-2.1.5.1 — Simpler explanation: complexity decreases when explanation fails; C-2.1.5.2 — Concrete worked example: the repair uses a concrete example; C-2.1.5.3 — No increased abstraction: explanation failure cannot be answered with greater abstraction. [V10 §2] [MAP C-2]; DESIGNED — C-2.2 — Grounded machine-state claims: actual files and state govern claims; C-2.2.1 — Actual-state evidence: machine-state claims require actual verification; C-2.2.2 — Actual files over remembered descriptions: remembered reports cannot displace the files; C-2.3 — Honest correction: errors receive honest correction; C-2.4 — Flag and continue: communication flags and continues within its settled rule; C-2.5 — Pull Sovereignty: Ness sets direction without unsolicited pressure; C-2.6 — Casual communication: casual wording is not treated as distress; C-2.7 — Understanding pace: explanations respect understanding before moving; C-2.8 — Shapes and steering: Ness retains steering. [V10 §2] [MAP C-2]; DESIGNED — C-2.9 — Session authority: Ness alone controls session boundaries; C-2.9.1 — Session-control boundary: no unilateral session ending, pausing or moving; C-2.9.2 — No session-pressure suggestions: no unrequested pressure to rest or close; C-2.10 — Latest instruction and rejected methods: the latest explicit instruction governs; C-2.10.1 — Latest explicit instruction: current instruction controls the method; C-2.10.2 — Rejected-method boundary: a rejected method stays closed unless reopened; C-2.10.2.1 — Stop using a rejected method: that method is no longer used; C-2.10.2.2 — Stop mentioning a rejected method: that method is no longer repeatedly raised. [V10 §2] [V10 §2A] [MAP C-2]; DESIGNED — C-2.11 — Anti-loop response: two corrections of the same misunderstanding trigger the settled response; C-2.11.1 — Abandon the current plan: the repeated wrong plan is abandoned; C-2.11.2 — One-sentence deliverable restatement: the exact requested deliverable is restated once; C-2.11.3 — Direct production: that deliverable is produced directly; C-2.11.4 — No repeated loops after an answer: an answered question is not repeated as a loop; C-2.12 — Actual-file delivery: a requested file is delivered as the actual file; C-2.12.1 — Actual downloadable file: the download is provided; C-2.12.2 — No unrequested delivery substitution: terminal, Cursor or manual-copy instructions cannot substitute without an explicit request. [V10 §2A] [MAP C-2]; DESIGNED — C-2.13 — Version safety: file delivery preserves prior authority; C-2.13.1 — New versioned file: a new versioned file is produced; C-2.13.2 — Previous authoritative master preservation: the prior master is not silently overwritten, renamed, deleted or replaced; C-2.13.3 — Prior authority until review and adoption: prior authority lasts until both occur; C-2.13.3.1 — Review condition: absent review, prior authority stands; C-2.13.3.2 — Adoption condition: absent adoption, prior authority stands; C-2.14 — No invented human-state explanations: mistakes receive no invented human-state explanation; C-2.14.1 — No human-state excuses: tiredness or similar excuses are not used; C-2.14.2 — Plain mistake account: the misread instruction or repeated wrong plan is stated plainly; C-2.14.3 — No invented emotional state: communication invents no emotional state. [V10 §2A] [MAP C-2]; DESIGNED — C-2.15 — Interaction and delivery event recording: maintenance interactions and file deliveries retain their records; C-2.15.1 — Interaction event recording: each interaction event is recorded; C-2.15.2 — Delivery event recording: each delivery event is recorded; C-2.15.3 — Interaction-record authorization: those records retain privacy and applicable identity/security restrictions; C-2.15.3.1 — Record privacy boundary: privacy authorization still applies; C-2.15.3.2 — Record identity boundary: applicable identity/security authorization still applies. [MAP C-2] [V10 §0B] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | Changes | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): permits only the authorized device-trust or emergency-recovery change within the declared bounded scope. [V10 §25.13 / Protected Material Boundary] [V10 §25.13 / Purpose-Specific Authorization] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BGMM.2.3 — Security-policy-change purpose | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): its thresholds may change only through the declared authorized security-policy scope. [V10 §25.13 / Protected Material Boundary] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.2.4 — Device-trust-change purpose | Changes | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): permits the specifically authorized trust-record change. [V10 §25.13 / Protected Material Boundary] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.2.5 — Emergency-recovery purpose | Changes | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies only its bounded emergency device-trust authority. [V10 §25.13 / Protected Material Boundary] | Pending endpoint placement |
| C-BAI.8.1 — Manifest-signing key | C-BGMM.5 — Signed-manifest trust anchor | Fed by | DESIGNED — C-BAI.8.1 — Manifest-signing key: signs only authorized versions with the separated hardware-backed key; C-BGMM.5.1 — Expected protected-file hashes: supplies each expected digest; C-BGMM.5.2 — Protected-file versions: supplies the corresponding versions; C-BGMM.5.3 — Pinned public verification key: supplies the hardware-anchored verification basis. [V10 §25.13 / Signed-Manifest Trust Anchor] [V10 §25.6] | Pending endpoint placement |
| C-BAI.8.2 — Rollback-sealing key | C-BGMM.6 — Encrypted rollback package | Gated by | DESIGNED — C-BAI.8.2 — Rollback-sealing key: only its separated hardware-backed rollback protection is used; C-BGMM.14 — Maintenance privacy: no protected content enters package metadata or audit fields. [V10 §25.13 / Encrypted Full-Content Rollback Packages] [V10 §25.13 / Privacy During Maintenance] | Pending endpoint placement |
| C-BAI.8.2 — Rollback-sealing key | C-BGMM.6.4 — Package sealing and integrity | Fed by | DESIGNED — C-BGMM.6 — Encrypted rollback package: supplies the full content to protect; C-BAI.8.2 — Rollback-sealing key: supplies the independent hardware-backed protection. [V10 §25.13 / Encrypted Full-Content Rollback Packages] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.8.3 — Trusted-phone confirmation | Fed by | DESIGNED — C-BGMM.8.1 — Purpose declaration: supplies the declared purpose/change; C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the trusted paired-phone identity. [V10 §25.13 / Entering Maintenance Mode] | Pending endpoint placement |
| C-BAI.3.9.4 — Maintenance confirmation purpose | C-BGMM.8.3 — Trusted-phone confirmation | Gated by | DESIGNED — C-BAI.3.9.4 — Maintenance confirmation purpose: requires the exact maintenance session/purpose binding; C-BAI.4 — One-time authorization token: the phone requires its own purpose-bound token before sending confirmation; C-BGMM.14.1 — Human-visible and phone descriptions: excludes private content from what is displayed or sent. [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance] | Pending endpoint placement |
| C-BAI.4 — One-time authorization token | C-BGMM.8.3 — Trusted-phone confirmation | Gated by | DESIGNED — C-BAI.3.9.4 — Maintenance confirmation purpose: requires the exact maintenance session/purpose binding; C-BAI.4 — One-time authorization token: the phone requires its own purpose-bound token before sending confirmation; C-BGMM.14.1 — Human-visible and phone descriptions: excludes private content from what is displayed or sent. [V10 §25.6 / Purpose Binding] [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Privacy During Maintenance] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.8.4 — Normal recovery-code verification | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies current normal recovery authority for the local check. [V10 §25.13 / Entering Maintenance Mode] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.8.5 — Emergency-factor verification | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the emergency code/sheet verification boundary; C-BGMM.8.5.1 — Physical motherbase presence: supplies the physical-access condition; C-BGMM.8.5.2 — Emergency-code verification: supplies the code factor; C-BGMM.8.5.3 — Printed-sheet verification: supplies the sheet factor. [V10 §25.13 / Entering Maintenance Mode] [V10 §25.13 / Purpose-Specific Authorization] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.8.5.2 — Emergency-code verification | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the emergency-code authority boundary. [V10 §25.13 / Entering Maintenance Mode] | Pending endpoint placement |
| C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | C-BGMM.8.5.3 — Printed-sheet verification | Fed by | DESIGNED — C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10): supplies the printed-sheet authority boundary. [V10 §25.13 / Entering Maintenance Mode] | Pending endpoint placement |
| C-BAI.8.1 — Manifest-signing key | C-BGMM.10.5 — Update and sign the manifest | Fed by | DESIGNED — C-BGMM.10.4 — Record the post-change hash: supplies `hash_after`; C-BAI.8.1 — Manifest-signing key: signs the authorized new version. [V10 §25.13 / Change Application] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BGMM.11 — Immediate automatic relocking | Fed by | DESIGNED — C-BGMM.13 — Volatile maintenance session state: supplies the active window, expiry, token and applied-change state; C-SACL — Speaker Access-Control Layer (§25.4): supplies medium-or-higher spoofing or session-level alerts. [V10 §25.13 / Automatic Relocking] [V10 §25.13 / BGMM-Owned State] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-BGMM.11.4 — Security-alert relock | Fed by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): supplies the qualifying alert; C-BGMM.11 — Immediate automatic relocking: defines its mandatory response. [V10 §25.13 / Automatic Relocking] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-BGMM.14 — Maintenance privacy | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): its protection rules remain applicable throughout maintenance. [MAP C-BGMM] | Pending endpoint placement |
| C-BAI.8.1 — Manifest-signing key | C-BGMM.18.2 — Hardware-backed key mechanism | Gated by | DESIGNED — C-BAI.8.1 — Manifest-signing key: keeps its independent signing role; C-BAI.8.2 — Rollback-sealing key: keeps its separate non-derivable, non-exportable protection role. [V10 §25.6] [V10 §25 / Build-Time Implementation Settings] | Pending endpoint placement |
| C-BAI.8.2 — Rollback-sealing key | C-BGMM.18.2 — Hardware-backed key mechanism | Gated by | DESIGNED — C-BAI.8.1 — Manifest-signing key: keeps its independent signing role; C-BAI.8.2 — Rollback-sealing key: keeps its separate non-derivable, non-exportable protection role. [V10 §25.6] [V10 §25 / Build-Time Implementation Settings] | Pending endpoint placement |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-BAI — Biometric Authorization Interface (§25.6) | 1 · DESIGNED | [V10 §25.6] | Existing TOGETHER relationship checked in earlier card |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-BAI.3.9.4 — Maintenance confirmation purpose | 2 · DESIGNED | [V10 §25.6 / Purpose Binding] | Existing TOGETHER relationship checked in earlier card |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-7P.2.6 — Strictest-rule and specialist authority boundary | 3 · ACCEPTED | [04/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md §9.1] | Existing TOGETHER relationship checked in earlier card |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10) | 5 · DESIGNED | [V10 §25.13 / Purpose-Specific Authorization] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-BGMM — Biometric-Gated Maintenance Mode (§25.13) | C-PAIR — Owner-phone pairing, recovery, replacement, emergency (§25.7–25.10), CY-I | 6 · DESIGNED | [MAP CY-I] [V10 §25.13 / Purpose-Specific Authorization] | TOGETHER continuation at using endpoint; preserve current use and its source |

## Source-to-card coverage added by CH09-f

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.13 / What BGMM Is and Is Not | C-BGMM, .1, .8: sole bounded local maintenance path; no general administrator authority. |
| V10 §25.13 / Protected Material Boundary | C-BGMM.2/.2.1–.2.5 and .3/.3.1–.3.7: five purpose/material scopes, immutable records, recovery-value prohibition, governed appends. |
| V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible) | C-BGMM.4/.4.1–.4.6: all five layers and the exact administrator/physical-attacker guarantee distinction. |
| V10 §25.13 / Signed-Manifest Trust Anchor | C-BGMM.5/.5.1–.5.5.3, .10.5, .12.5: expected hashes/versions, pinned public key, signed provenance and ordered startup/rollback verification. |
| V10 §25.13 / Encrypted Full-Content Rollback Packages | C-BGMM.6 through .6.5: all record fields, per-file fields and metadata categories; session_id reused at .13.1; canonical separated keys C-BAI.8.1/.8.2. |
| V10 §25.13 / Protected Startup Recovery Worker | C-BGMM.7/.7.1–.7.7: boot and integrity conditions, bounded exact scope, successful permanent inaccessibility and three distinct failures. |
| V10 §25.13 / Entering Maintenance Mode | C-BGMM.8/.8.1–.8.6 and .8.5.1–.8.5.3: all six entry steps; the emergency factor conditions are individually placed. |
| V10 §25.13 / Purpose-Specific Authorization | C-BGMM.2/.2.1–.2.5, .8 and .9.2: each exact factor conjunction; emergency device-trust scope; no phone required for device-trust/emergency branches. |
| V10 §25.13 / File Scope Enforcement | C-BGMM.9/.9.1–.9.3 and .13.4: exact token file list; out-of-scope and immutable refusals; emergency override. |
| V10 §25.13 / Change Application | C-BGMM.10/.10.1–.10.8: seven steps in exact source order and immediate post-touch rollback. |
| V10 §25.13 / Automatic Relocking | C-BGMM.11/.11.1–.11.7: all seven triggers, immediate token revocation/event and partial-change rollback. |
| V10 §25.13 / Rollback | C-BGMM.12/.12.1–.12.6: decryption, prior_hash check, exact bytes, signatures/metadata, prior signed manifest and no-write idempotency. |
| V10 §25.13 / BGMM-Owned State | C-BGMM.13/.13.1–.13.11.2: all eleven fields, append-only applied_changes and checkpoint file-list/hash_before references; no invented session_status enumeration. |
| V10 §25.13 / Privacy During Maintenance | C-BGMM.14/.14.1–.14.5: each content-free description/log/audit surface, protected rollback bytes and all sensitive-content classes. |
| V10 §25.13 / Immediate Security Audit Events | C-BGMM.15/.15.1–.15.17: all seventeen names, structural-only content and write/flush before producing-function return; no invented event schemas. |
| V10 §25.13 / Crash, Restart, Offline Behavior | C-BGMM.16/.16.1–.16.4: open-session crash, interrupted rollback, startup integrity failure and fully offline operation. |
| V10 §25.13 / Protected-Core Rules (Unconditional) | C-BGMM.17 reuses the atomic owners .9.3, .4, .11, .9.2 and .3.6 without new authority. |
| V10 §25 / Build-Time Implementation Settings | C-BGMM.18/.18.1/.18.2: empirical timeout and available-hardware key mechanism; values remain open build settings (Map C10), not conceptual Ness decisions. |
| V10 §§2/2A, §0B and §25.6 purpose/key boundaries | C-BGMM root preserves all fifty-one earlier C-2 maintenance-use places through named gates; .15 retains living-record boundaries; canonical BAI purpose/token/key identities are reused. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-BGMM, C-2 and CY-I | Exact root name, governed-append distinction, qualified physical-attacker guarantee, structural-only maintenance privacy, mandatory C-2 gate and the C-PAIR use in CY-I. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded security-design §13 | Source-conflict paragraph: stale package deletion versus V10 sealing/inaccessibility; no Companion deletion behavior adopted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 | C-BGMM root USED BY C-7P.2.6 reciprocates specialist protected-change authority. General action mechanics remain canonical in CH07-c. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` §§5B/6 and change-summary context | Cross-purpose token boundary checked; no maintenance-purpose token can open Personal Mode. Canonical BAI boundary remains CH09-e; complete modes remain CH09-i. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` dependency paragraph | BGMM mention is the preserved supporting source title, not added maintenance mechanics; complete enrollment remains CH09-h. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` §2.1 | Names governing BGMM law; adds no BGMM internals in the reviewed passage. Full kernel behavior/whole-file obligation remains CH10-b. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted ordinary-chat policy, frozen source status and open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted room-start policy and preserved open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` verification/closure context | Protected-file search hit is task verification, excluded under contract §1.3; no maintenance behavior added. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` §6 FR-0003 | Existing restored key-purpose rule remains C-BAI.8.3 in CH09-e; no additional archive behavior imported for this piece. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` NHD-M25 search hit | Navigation only; no behavior and no current-version authority inferred. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` NHD-M25 search hit | Accepted prior navigation index; no behavior used from its row. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` NHD-M25 search hit | Earlier candidate navigation; no behavior used. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` header and NHD-M25 row | Highest current candidate index used only for navigation; v0_6's accepted-prior standing is preserved; no architecture derived. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` BGMM discovery | The matched TSC provenance pointer adds no maintenance mechanism. V10 governs; whole-file credit is not claimed here. |
| `01_AUTHORITATIVE/cursorrules` BGMM/maintenance discovery | No new BGMM body found by scoped discovery; implementation/workflow text is not inserted into behavior. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` BGMM/maintenance discovery | No additional maintenance restoration found; no archive expansion authorized or taken. |
| Remaining owners | CH09-g full pairing/recovery material lifecycle; CH09-h full enrollment; CH09-i full modes; CH10-b full kernel; CH10-e interface packages; CH11 side paths; CH12 regenerated final registers. |

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-BGMM.1 — Narrow maintenance boundary | Gives out |
| C-BGMM.1 — Narrow maintenance boundary | Fed by |
| C-BGMM.1 — Narrow maintenance boundary | Gated by |
| C-BGMM.1 — Narrow maintenance boundary | Changes |
| C-BGMM.2 — Protected purposes and factors | Gated by |
| C-BGMM.2 — Protected purposes and factors | Changes |
| C-BGMM.2.1 — Code-change purpose | Changes |
| C-BGMM.2.2 — Configuration-change purpose | Changes |
| C-BGMM.3 — Permanently unchangeable material | Fed by |
| C-BGMM.3 — Permanently unchangeable material | Changes |
| C-BGMM.3.1 — Sealed-root protection | Fed by |
| C-BGMM.3.1 — Sealed-root protection | Changes |
| C-BGMM.3.2 — Reading and provenance protection | Fed by |
| C-BGMM.3.2 — Reading and provenance protection | Changes |
| C-BGMM.3.3 — Clash and Person-Box-link protection | Fed by |
| C-BGMM.3.3 — Clash and Person-Box-link protection | Changes |
| C-BGMM.3.4 — Audit-entry protection | Fed by |
| C-BGMM.3.4 — Audit-entry protection | Changes |
| C-BGMM.3.5 — Gold-record protection | Fed by |
| C-BGMM.3.5 — Gold-record protection | Changes |
| C-BGMM.3.6 — Recovery-value prohibition | Gives out |
| C-BGMM.3.6 — Recovery-value prohibition | Fails closed by |
| C-BGMM.3.6 — Recovery-value prohibition | Fed by |
| C-BGMM.3.6 — Recovery-value prohibition | Gated by |
| C-BGMM.3.6 — Recovery-value prohibition | Changes |
| C-BGMM.3.7 — Normal governed append boundary | Fails closed by |
| C-BGMM.3.7 — Normal governed append boundary | Fed by |
| C-BGMM.3.7 — Normal governed append boundary | Changes |
| C-BGMM.4 — Normal-path write prevention | Fed by |
| C-BGMM.4 — Normal-path write prevention | Gated by |
| C-BGMM.4 — Normal-path write prevention | Changes |
| C-BGMM.4.1 — ACL and service isolation | Gated by |
| C-BGMM.4.1 — ACL and service isolation | Changes |
| C-BGMM.4.2 — Administrator-level resistance | Fails closed by |
| C-BGMM.4.2 — Administrator-level resistance | Gated by |
| C-BGMM.4.2 — Administrator-level resistance | Changes |
| C-BGMM.4.3 — Executable code signing | Gated by |
| C-BGMM.4.3 — Executable code signing | Changes |
| C-BGMM.4.4 — Signed-manifest integrity layer | Gated by |
| C-BGMM.4.4 — Signed-manifest integrity layer | Changes |
| C-BGMM.4.5 — Change-log provenance layer | Gated by |
| C-BGMM.4.5 — Change-log provenance layer | Changes |
| C-BGMM.4.6 — Qualified tamper guarantee | Gated by |
| C-BGMM.4.6 — Qualified tamper guarantee | Changes |
| C-BGMM.5.1 — Expected protected-file hashes | Fails closed by |
| C-BGMM.5.1 — Expected protected-file hashes | Gated by |
| C-BGMM.5.1 — Expected protected-file hashes | Changes |
| C-BGMM.5.2 — Protected-file versions | Must never |
| C-BGMM.5.2 — Protected-file versions | Fails closed by |
| C-BGMM.5.2 — Protected-file versions | Fed by |
| C-BGMM.5.2 — Protected-file versions | Gated by |
| C-BGMM.5.2 — Protected-file versions | Changes |
| C-BGMM.5.3 — Pinned public verification key | Fed by |
| C-BGMM.5.3 — Pinned public verification key | Gated by |
| C-BGMM.5.3 — Pinned public verification key | Changes |
| C-BGMM.5.4 — Manifest provenance history | Fails closed by |
| C-BGMM.5.4 — Manifest provenance history | Gated by |
| C-BGMM.5.4 — Manifest provenance history | Changes |
| C-BGMM.5.5 — Startup manifest verification | Gated by |
| C-BGMM.5.5 — Startup manifest verification | Changes |
| C-BGMM.5.5.1 — Read the current manifest | Fails closed by |
| C-BGMM.5.5.1 — Read the current manifest | Gated by |
| C-BGMM.5.5.1 — Read the current manifest | Changes |
| C-BGMM.5.5.2 — Verify the manifest signature | Gated by |
| C-BGMM.5.5.2 — Verify the manifest signature | Changes |
| C-BGMM.5.5.3 — Verify every protected-file hash | Changes |
| C-BGMM.6 — Encrypted rollback package | Changes |
| C-BGMM.6.1 — Rollback change description | Fails closed by |
| C-BGMM.6.1 — Rollback change description | Changes |
| C-BGMM.6.2 — Rollback file entries | Fails closed by |
| C-BGMM.6.2 — Rollback file entries | Changes |
| C-BGMM.6.2.1 — Rollback file path | Fails closed by |
| C-BGMM.6.2.1 — Rollback file path | Fed by |
| C-BGMM.6.2.1 — Rollback file path | Changes |
| C-BGMM.6.2.2 — Exact prior file content | Fails closed by |
| C-BGMM.6.2.2 — Exact prior file content | Fed by |
| C-BGMM.6.2.2 — Exact prior file content | Changes |
| C-BGMM.6.2.3 — Prior-content hash | Gated by |
| C-BGMM.6.2.3 — Prior-content hash | Changes |
| C-BGMM.6.2.4 — Prior code signature | Must never |
| C-BGMM.6.2.4 — Prior code signature | Fails closed by |
| C-BGMM.6.2.4 — Prior code signature | Fed by |
| C-BGMM.6.2.4 — Prior code signature | Gated by |
| C-BGMM.6.2.4 — Prior code signature | Changes |
| C-BGMM.6.2.5 — Prior manifest version | Must never |
| C-BGMM.6.2.5 — Prior manifest version | Fails closed by |
| C-BGMM.6.2.5 — Prior manifest version | Gated by |
| C-BGMM.6.2.5 — Prior manifest version | Changes |
| C-BGMM.6.2.6 — File restoration metadata | Fails closed by |
| C-BGMM.6.2.6 — File restoration metadata | Gated by |
| C-BGMM.6.2.6 — File restoration metadata | Changes |
| C-BGMM.6.2.6.1 — Prior permissions | Must never |
| C-BGMM.6.2.6.1 — Prior permissions | Fails closed by |
| C-BGMM.6.2.6.1 — Prior permissions | Fed by |
| C-BGMM.6.2.6.1 — Prior permissions | Gated by |
| C-BGMM.6.2.6.1 — Prior permissions | Changes |
| C-BGMM.6.2.6.2 — Prior timestamps | Must never |
| C-BGMM.6.2.6.2 — Prior timestamps | Fails closed by |
| C-BGMM.6.2.6.2 — Prior timestamps | Fed by |
| C-BGMM.6.2.6.2 — Prior timestamps | Gated by |
| C-BGMM.6.2.6.2 — Prior timestamps | Changes |
| C-BGMM.6.2.6.3 — Prior attributes | Must never |
| C-BGMM.6.2.6.3 — Prior attributes | Fails closed by |
| C-BGMM.6.2.6.3 — Prior attributes | Fed by |
| C-BGMM.6.2.6.3 — Prior attributes | Gated by |
| C-BGMM.6.2.6.3 — Prior attributes | Changes |
| C-BGMM.6.3 — Rollback creation time | Fails closed by |
| C-BGMM.6.3 — Rollback creation time | Gated by |
| C-BGMM.6.3 — Rollback creation time | Changes |
| C-BGMM.6.4 — Package sealing and integrity | Gated by |
| C-BGMM.6.4 — Package sealing and integrity | Changes |
| C-BGMM.6.5 — Successful package closure | Changes |
| C-BGMM.7.1 — Expected measured-boot condition | Fed by |
| C-BGMM.7.1 — Expected measured-boot condition | Gated by |
| C-BGMM.7.1 — Expected measured-boot condition | Changes |
| C-BGMM.7.2 — Full package-integrity condition | Gated by |
| C-BGMM.7.2 — Full package-integrity condition | Changes |
| C-BGMM.7.3 — Exact recovery scope | Changes |
| C-BGMM.7.4 — Verified recovery completion | Changes |
| C-BGMM.7.5 — Recovery decryption failure | Changes |
| C-BGMM.7.6 — Recovery integrity failure | Changes |
| C-BGMM.7.7 — Recovery restoration failure | Changes |
| C-BGMM.8.1 — Purpose declaration | Changes |
| C-BGMM.8.2 — Motherbase thumbprint result | Changes |
| C-BGMM.8.3 — Trusted-phone confirmation | Changes |
| C-BGMM.8.4 — Normal recovery-code verification | Changes |
| C-BGMM.8.5 — Emergency-factor verification | Changes |
| C-BGMM.8.5.1 — Physical motherbase presence | Fed by |
| C-BGMM.8.5.1 — Physical motherbase presence | Gated by |
| C-BGMM.8.5.1 — Physical motherbase presence | Changes |
| C-BGMM.8.5.2 — Emergency-code verification | Changes |
| C-BGMM.8.5.3 — Printed-sheet verification | Gated by |
| C-BGMM.8.5.3 — Printed-sheet verification | Changes |
| C-BGMM.9 — Exact file-scope enforcement | Gated by |
| C-BGMM.9 — Exact file-scope enforcement | Changes |
| C-BGMM.9.1 — Out-of-scope write refusal | Gated by |
| C-BGMM.9.1 — Out-of-scope write refusal | Changes |
| C-BGMM.9.2 — Emergency scope override | Gated by |
| C-BGMM.9.2 — Emergency scope override | Changes |
| C-BGMM.9.3 — Immutable-write refusal | Gated by |
| C-BGMM.9.3 — Immutable-write refusal | Changes |
| C-BGMM.10.1 — Flush the change-log entry | Changes |
| C-BGMM.10.2 — Persist the rollback package | Changes |
| C-BGMM.10.3 — Apply the protected change | Changes |
| C-BGMM.10.4 — Record the post-change hash | Gated by |
| C-BGMM.10.4 — Record the post-change hash | Changes |
| C-BGMM.10.6 — Re-sign modified executables | Changes |
| C-BGMM.10.7 — Record the applied change | Changes |
| C-BGMM.10.8 — Post-touch failure rollback | Gated by |
| C-BGMM.11 — Immediate automatic relocking | Gated by |
| C-BGMM.11.1 — Completion relock | Gated by |
| C-BGMM.11.1 — Completion relock | Changes |
| C-BGMM.11.2 — Timeout relock | Gated by |
| C-BGMM.11.2 — Timeout relock | Changes |
| C-BGMM.11.3 — Restart or crash relock | Gated by |
| C-BGMM.11.4 — Security-alert relock | Gated by |
| C-BGMM.11.4 — Security-alert relock | Changes |
| C-BGMM.11.5 — Phone-disconnection relock | Gated by |
| C-BGMM.11.5 — Phone-disconnection relock | Changes |
| C-BGMM.11.6 — Explicit-abort relock | Gated by |
| C-BGMM.11.6 — Explicit-abort relock | Changes |
| C-BGMM.11.7 — Biometric-expiry relock | Gated by |
| C-BGMM.11.7 — Biometric-expiry relock | Changes |
| C-BGMM.12.1 — Decrypt the restoration package | Changes |
| C-BGMM.12.2 — Verify prior-content bytes | Gated by |
| C-BGMM.12.2 — Verify prior-content bytes | Changes |
| C-BGMM.12.3 — Restore prior content | Changes |
| C-BGMM.12.4 — Restore prior signature and metadata | Changes |
| C-BGMM.12.6 — Already-matching-file idempotency | Fails closed by |
| C-BGMM.12.6 — Already-matching-file idempotency | Gated by |
| C-BGMM.12.6 — Already-matching-file idempotency | Changes |
| C-BGMM.13 — Volatile maintenance session state | Changes |
| C-BGMM.13.1 — Maintenance session identifier | Must never |
| C-BGMM.13.1 — Maintenance session identifier | Fails closed by |
| C-BGMM.13.1 — Maintenance session identifier | Gated by |
| C-BGMM.13.1 — Maintenance session identifier | Changes |
| C-BGMM.13.2 — Declared maintenance purpose | Fails closed by |
| C-BGMM.13.2 — Declared maintenance purpose | Gated by |
| C-BGMM.13.2 — Declared maintenance purpose | Changes |
| C-BGMM.13.3 — Declared maintenance change | Fails closed by |
| C-BGMM.13.3 — Declared maintenance change | Changes |
| C-BGMM.13.4 — Declared file scope | Changes |
| C-BGMM.13.5 — Session authorization factors | Changes |
| C-BGMM.13.6 — Maintenance session status | Takes in |
| C-BGMM.13.6 — Maintenance session status | Gives out |
| C-BGMM.13.6 — Maintenance session status | Fails closed by |
| C-BGMM.13.6 — Maintenance session status | Gated by |
| C-BGMM.13.6 — Maintenance session status | Changes |
| C-BGMM.13.7 — Maintenance opening time | Must never |
| C-BGMM.13.7 — Maintenance opening time | Fails closed by |
| C-BGMM.13.7 — Maintenance opening time | Gated by |
| C-BGMM.13.7 — Maintenance opening time | Changes |
| C-BGMM.13.8 — Maintenance expiration time | Gated by |
| C-BGMM.13.8 — Maintenance expiration time | Changes |
| C-BGMM.13.9 — Write-token activity | Changes |
| C-BGMM.13.10 — Applied-change list | Fails closed by |
| C-BGMM.13.10 — Applied-change list | Gated by |
| C-BGMM.13.10 — Applied-change list | Changes |
| C-BGMM.13.11 — Rollback verification checkpoint | Fails closed by |
| C-BGMM.13.11 — Rollback verification checkpoint | Gated by |
| C-BGMM.13.11 — Rollback verification checkpoint | Changes |
| C-BGMM.13.11.1 — Checkpoint file list | Fails closed by |
| C-BGMM.13.11.1 — Checkpoint file list | Gated by |
| C-BGMM.13.11.1 — Checkpoint file list | Changes |
| C-BGMM.13.11.2 — Checkpoint prior hashes | Fails closed by |
| C-BGMM.13.11.2 — Checkpoint prior hashes | Gated by |
| C-BGMM.13.11.2 — Checkpoint prior hashes | Changes |
| C-BGMM.14 — Maintenance privacy | Fails closed by |
| C-BGMM.14 — Maintenance privacy | Fed by |
| C-BGMM.14 — Maintenance privacy | Changes |
| C-BGMM.14.1 — Human-visible and phone descriptions | Fails closed by |
| C-BGMM.14.1 — Human-visible and phone descriptions | Fed by |
| C-BGMM.14.1 — Human-visible and phone descriptions | Changes |
| C-BGMM.14.2 — Rollback metadata privacy | Fails closed by |
| C-BGMM.14.2 — Rollback metadata privacy | Changes |
| C-BGMM.14.3 — Structural change-log content | Fails closed by |
| C-BGMM.14.3 — Structural change-log content | Fed by |
| C-BGMM.14.3 — Structural change-log content | Changes |
| C-BGMM.14.4 — Structural security-audit content | Fails closed by |
| C-BGMM.14.4 — Structural security-audit content | Fed by |
| C-BGMM.14.4 — Structural security-audit content | Changes |
| C-BGMM.14.5 — Sensitive maintenance-content exclusion | Gives out |
| C-BGMM.14.5 — Sensitive maintenance-content exclusion | Fails closed by |
| C-BGMM.14.5 — Sensitive maintenance-content exclusion | Fed by |
| C-BGMM.14.5 — Sensitive maintenance-content exclusion | Changes |
| C-BGMM.15 — Immediate security audit events | Changes |
| C-BGMM.15.1 — Session-initiated event | Fails closed by |
| C-BGMM.15.1 — Session-initiated event | Fed by |
| C-BGMM.15.1 — Session-initiated event | Changes |
| C-BGMM.15.2 — Session-opened event | Fails closed by |
| C-BGMM.15.2 — Session-opened event | Changes |
| C-BGMM.15.3 — Write-token-granted event | Fails closed by |
| C-BGMM.15.3 — Write-token-granted event | Changes |
| C-BGMM.15.4 — Change-log-entry event | Changes |
| C-BGMM.15.5 — Change-applied event | Changes |
| C-BGMM.15.6 — Hash-registry-updated event | Takes in |
| C-BGMM.15.6 — Hash-registry-updated event | Fails closed by |
| C-BGMM.15.6 — Hash-registry-updated event | Fed by |
| C-BGMM.15.6 — Hash-registry-updated event | Changes |
| C-BGMM.15.7 — Out-of-scope-attempt event | Changes |
| C-BGMM.15.8 — Session-completed event | Fails closed by |
| C-BGMM.15.8 — Session-completed event | Changes |
| C-BGMM.15.9 — Write-token-revoked event | Changes |
| C-BGMM.15.10 — Rollback-triggered event | Fails closed by |
| C-BGMM.15.10 — Rollback-triggered event | Changes |
| C-BGMM.15.11 — Rollback-completed event | Changes |
| C-BGMM.15.12 — Rollback-failed event | Changes |
| C-BGMM.15.13 — Session-timed-out event | Changes |
| C-BGMM.15.14 — Session-aborted event | Changes |
| C-BGMM.15.15 — Integrity-check-failed event | Changes |
| C-BGMM.15.16 — Integrity-check-passed event | Fails closed by |
| C-BGMM.15.16 — Integrity-check-passed event | Changes |
| C-BGMM.15.17 — Immutable-write-blocked event | Changes |
| C-BGMM.16 — Crash, restart and offline behavior | Changes |
| C-BGMM.16.3 — Startup integrity failure | Changes |
| C-BGMM.16.4 — Offline maintenance | Takes in |
| C-BGMM.16.4 — Offline maintenance | Gives out |
| C-BGMM.16.4 — Offline maintenance | Fails closed by |
| C-BGMM.16.4 — Offline maintenance | Fed by |
| C-BGMM.16.4 — Offline maintenance | Gated by |
| C-BGMM.16.4 — Offline maintenance | Changes |
| C-BGMM.17 — Unconditional protected-core rules | Fed by |
| C-BGMM.17 — Unconditional protected-core rules | Changes |
| C-BGMM.18 — Build-time maintenance settings | Gives out |
| C-BGMM.18 — Build-time maintenance settings | Fails closed by |
| C-BGMM.18 — Build-time maintenance settings | Fed by |
| C-BGMM.18 — Build-time maintenance settings | Gated by |
| C-BGMM.18 — Build-time maintenance settings | Changes |
| C-BGMM.18.1 — Empirical maintenance timeout | Gives out |
| C-BGMM.18.1 — Empirical maintenance timeout | Fails closed by |
| C-BGMM.18.1 — Empirical maintenance timeout | Gated by |
| C-BGMM.18.1 — Empirical maintenance timeout | Changes |
| C-BGMM.18.2 — Hardware-backed key mechanism | Gives out |
| C-BGMM.18.2 — Hardware-backed key mechanism | Fails closed by |
| C-BGMM.18.2 — Hardware-backed key mechanism | Changes |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. Each positive scan hit below is retained for its named reason.

| Card / line | Flag | Reason |
|---|---|---|
| C-BGMM.1 — Narrow maintenance boundary; line 64 | empty_together | Owner boundary law, not an execution step. The word requires limits declared access; it is not an extra producer/gate. Read-only failure and direct prohibitions are explicit; actual entry gates are C-BGMM.8. |
| C-BGMM.1 — Narrow maintenance boundary; line 65 | prerequisite_review / Gated by | Owner boundary law, not an execution step. The word requires limits declared access; it is not an extra producer/gate. Read-only failure and direct prohibitions are explicit; actual entry gates are C-BGMM.8. |
| C-BGMM.2 — Protected purposes and factors; line 88 | prerequisite_review / Gated by | The classification owner states the five branches and intrinsic factor mapping. Each operative purpose card names its actual factor gates; the classifier needs no invented additional gate. |
| C-BGMM.3.6 — Recovery-value prohibition; line 377 | empty_together | A storage prohibition. No distinct producer or automatic recovery-value refusal implementation is designed; Must never states the complete law and consumers explicitly gate on it. |
| C-BGMM.4 — Normal-path write prevention; line 425 | empty_together | The five-layer design owner, not a step missing an upstream link. Its actual layers, module rejection and integrity-failure outcome are explicit; no additional source gate is invented. |
| C-BGMM.5.2 — Protected-file versions; line 642 | empty_together | A primitive manifest datum. The source names versions but no producer, encoding or gate; the manifest's use is explicit. |
| C-BGMM.5.3 — Pinned public verification key; line 665 | empty_together | The primitive hardware-anchored public trust basis. Its source defines anchoring and invariance, not another card that authorizes the key itself. |
| C-BGMM.5.5.2 — Verify the manifest signature; line 767 | prerequisite_review / Gated by | The prerequisite hit occurs in the using hash-check row: the signature check is that next step's prerequisite. This card performs the check and states its failed-start outcome; it does not need a second gate for its own intrinsic verification. |
| C-BGMM.6.2.4 — Prior code signature; line 962 | empty_together | A conditional record field, applicable where a prior code signature exists. That applicability is its own data definition, not an additional external gate. |
| C-BGMM.6.2.6.1 — Prior permissions; line 1034 | empty_together | Primitive permissions datum for exact restoration; no source names a distinct producer or separate gate. |
| C-BGMM.6.2.6.2 — Prior timestamps; line 1057 | empty_together | Primitive timestamp datum, with no source-selected format or separate producer/gate. It is used explicitly by the metadata record. |
| C-BGMM.6.2.6.3 — Prior attributes; line 1080 | empty_together | Primitive attribute datum for restoration; no independent operational step or source-designed gate is omitted. |
| C-BGMM.6.4 — Package sealing and integrity; line 1127 | prerequisite_review / Gated by | The prerequisite hit describes its consumer's need to verify package integrity. This protection card already states the pre-restoration refusal; its own inputs name the package and separated key without inventing another gate. |
| C-BGMM.6.5 — Successful package closure; line 1151 | prerequisite_review / Gated by | Its Gated by line names C-BGMM.12 (Idempotent rollback): successful final verification, or a successful rollback with its verified prior-state result, precedes this closure. The source does not define a separate general final-verification component; exact restore/completion cards retain their separate scopes. |
| C-BGMM.7.1 — Expected measured-boot condition; line 1202 | empty_together | An atomic environmental boot-state condition with no internal producer. Matching the expected measured-boot record is the condition's definition, not an extra gate; failure to match explicitly withholds restoration. |
| C-BGMM.7.1 — Expected measured-boot condition; line 1203 | prerequisite_review / Gated by | An atomic environmental boot-state condition with no internal producer. Matching the expected measured-boot record is the condition's definition, not an extra gate; failure to match explicitly withholds restoration. |
| C-BGMM.7.2 — Full package-integrity condition; line 1228 | prerequisite_review / Gated by | Package verification is the card's intrinsic test. The restoration prerequisite is explicit in Does, Must never and Fails closed by; no extra gate is inferred for the test itself. |
| C-BGMM.8.5.1 — Physical motherbase presence; line 1534 | empty_together | A physical human-presence prerequisite, not an N.H step with an omitted producer. Physical absence explicitly fails the emergency conjunction; no presence-detection implementation is invented. |
| C-BGMM.8.5.3 — Printed-sheet verification; line 1583 | prerequisite_review / Gated by | The card defines one required factor, with explicit refusal when absent/unverified. The conjunction with other emergency factors belongs to C-BGMM.8.5; no extra gate for sheet verification itself is designed. |
| C-BGMM.12.2 — Verify prior-content bytes; line 2203 | prerequisite_review / Gated by | The prerequisite scan finds the consuming content-restoration requirement. This card performs the prior-byte verification and explicitly halts failed startup recovery; it is not missing a separate authorization mechanism. |
| C-BGMM.13.2 — Declared maintenance purpose; line 2365 | prerequisite_review / Fails closed by | A declared-purpose datum that retains the already recorded pre-authorization declaration. The field is not an authorization operation; emergency scope enforcement remains C-BGMM.9.2 and purpose factors remain C-BGMM.2. |
| C-BGMM.13.2 — Declared maintenance purpose; line 2369 | prerequisite_review / Gated by | A declared-purpose datum that retains the already recorded pre-authorization declaration. The field is not an authorization operation; emergency scope enforcement remains C-BGMM.9.2 and purpose factors remain C-BGMM.2. |
| C-BGMM.14.2 — Rollback metadata privacy; line 2696 | prerequisite_review / Fails closed by | The package metadata boundary is a prohibition, with an explicit privacy gate. The source designs no separate failure implementation for a metadata-content violation; the scan's requires wording belongs to that gate. |
| C-BGMM.15.2 — Session-opened event; line 2851 | prerequisite_review / Fails closed by | An audit-event record with actual opening as input and mandatory write/flush timing. The source supplies no standalone failure routine for this event; the required timing is preserved without inventing one. |
| C-BGMM.15.3 — Write-token-granted event; line 2874 | prerequisite_review / Fails closed by | The token-grant event has a real producer and mandatory structural write/flush gate. No separate event-write failure mechanism is specified. |
| C-BGMM.15.8 — Session-completed event; line 2989 | prerequisite_review / Fails closed by | The completion-event record uses actual applied/verified/logged completion. Its mandatory flush is stated; the source does not specify a separate failure routine for this event. |
| C-BGMM.15.16 — Integrity-check-passed event; line 3173 | prerequisite_review / Fails closed by | The integrity-pass audit event has its actual result producer and flush gate. The source does not define an additional pass-event recording failure mechanism. |
| C-BGMM.16.4 — Offline maintenance; line 3315 | empty_together | A standalone offline capability boundary, not a sequence step. No source names a separate producer, gate or state mutation; network independence is explicit. |
| C-BGMM.18 — Build-time maintenance settings; line 3361 | empty_together | The owner of two build-time settings, not a runtime operation with an omitted gate. Both actual child settings are placed; numerical timeout and hardware mechanism remain unselected. |

## Coverage matrix — cumulative carried inventory



























The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F006 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F007 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F008 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F009 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A16_TSC_ARCHIVE_EVENT_NAME_ADOPTION_POLICY_v1_0_CANDIDATE.md` | Whole read in CH04-b: Event adoption §§2–7; status and source envelope. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F010 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F011 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.9 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F012 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F013 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: scoped read; exact scope and placement in the current source table. |
| F014 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F015 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F016 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F017 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F018 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker. |
| F019 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: C-ENGINE-C.7.; CH03-l: C-GOLD, C-GOLD.6.1, C-GOLD.8, C-GOLD.8.1, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.5.12. |
| F020 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_ACCEPTANCE_RECORD_v1_1.md` | Scoped reread for CH03-l; prior whole-read credit retained where previously recorded | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-l: C-GOLD.8, C-GOLD.8.5.12. |
| F021 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Read whole for CH03-l | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; CH03-l: C-GOLD.6.1, C-GOLD.8, C-GOLD.8.2, C-GOLD.8.2.1, C-GOLD.8.2.2, C-GOLD.8.3, C-GOLD.8.3.1, C-GOLD.8.3.2, C-GOLD.8.4, C-GOLD.8.5, C-GOLD.8.5.1, C-GOLD.8.5.2, C-GOLD.8.5.3, C-GOLD.8.5.4, C-GOLD.8.5.5, C-GOLD.8.5.6, C-GOLD.8.5.7, C-GOLD.8.5.8, C-GOLD.8.5.9, C-GOLD.8.5.10, C-GOLD.8.5.11, C-GOLD.8.5.12, C-GOLD.8.6, C-GOLD.8.6.1, C-GOLD.8.7, C-GOLD.8.7.1, C-GOLD.8.8, C-GOLD.8.8.1, C-GOLD.8.8.2, C-GOLD.8.9, C-GOLD.8.9.1, C-GOLD.8.9.2, C-GOLD.8.9.3, C-GOLD.8.10, C-GOLD.8.10.1, C-GOLD.8.10.2, C-GOLD.8.10.3, C-GOLD.8.11, C-GOLD.8.11.1, C-GOLD.8.11.2, C-GOLD.8.12, C-GOLD.8.12.1, C-GOLD.8.12.2, C-GOLD.8.13, C-GOLD.8.13.1, C-GOLD.8.13.2. |
| F022 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F023 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F024 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F025 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F026 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F027 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F028 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F029 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F030 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F031 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F032 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F033 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F034 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F038 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F039 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F040 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F041 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F042 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F043 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F044 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F045 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F046 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F047 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F060 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F061 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F062 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F063 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F064 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1 and cited sub-parts; C-7B.7.4.7 and cited sub-parts; C-7B.7.5.3 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F065 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3. |
| F066 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. |
| F067 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | Acceptance receipt supporting the ACCEPTED scope of the matching package; EXCLUDED: closure history and process under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F068 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Whole file in passed Chapter 2; not a new whole read in that piece | C-7B.7.1.6 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.  CH05-b: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F069 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F070 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Carried through Chapter 3-a: Not yet read; whole file newly read in Chapter 3-b | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-b: EXCLUDED: status/consolidation and workflow narrative under §1.3. Used for locating later accepted owners only; it supplies no behavior in this piece.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F071 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F072 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F073 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained. |
| F074 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-d: exact read scope and placement in the current source table; prior credits retained. |
| F075 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F076 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F077 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F078 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-c: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained.  CH05-a: exact read scope and placement in the current source table; prior credits retained.  CH05-e: exact read scope and placement in the current source table; prior credits retained. |
| F087 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F088 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Whole read in CH04-b: Two-phase authorization/promotion, continuation, C1–C10, nine coordination record types, logging, failure and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F089 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F090 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F091 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F092 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F093 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F094 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F095 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F096 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F097 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F098 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
| F099 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
| F100 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10.1.11; C-READ.10.1.12 and all firmness-policy-cited descendants: §§1–6 qualitative outcomes, evidence basis, separations, revision and no-numeric-scoring. EXCLUDED: package history/process; future policy and consumer schemas not invented.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.10. |
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
| F112 | `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Read whole for CH03-n | C-GOLD.1 identities/records/currentness in 3-e; C-GOLD.1.5 operation/execution contracts in 3-f; C-GOLD.1.6 judgment chain/conditional proof in 3-g; C-GOLD.1.7 claim lifecycle/protected recovery in 3-h; derivation, applicability and remaining dependencies NOT PLACED: later pieces; CH03-l: C-GOLD.; CH03-m: C-GOLD.1.8, C-GOLD.1.8.1, C-GOLD.1.8.1.1, C-GOLD.1.8.1.2, C-GOLD.1.8.1.2.1, C-GOLD.1.8.1.2.2, C-GOLD.1.8.1.2.3, C-GOLD.1.8.1.2.4, C-GOLD.1.8.1.2.5, C-GOLD.1.8.1.3, C-GOLD.1.8.1.3.1, C-GOLD.1.8.1.3.2, C-GOLD.1.8.1.3.3, C-GOLD.1.8.1.3.4, C-GOLD.1.8.1.3.5, C-GOLD.1.8.1.4, C-GOLD.1.8.1.4.1, C-GOLD.1.8.1.4.2, C-GOLD.1.8.1.4.3, C-GOLD.1.8.1.5, C-GOLD.1.8.1.5.1, C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.1.5.3, C-GOLD.1.8.1.6, C-GOLD.1.8.2, C-GOLD.1.8.2.1, C-GOLD.1.8.2.2, C-GOLD.1.8.2.3, C-GOLD.1.8.2.4, C-GOLD.1.8.2.4.1, C-GOLD.1.8.2.4.2, C-GOLD.1.8.2.4.3, C-GOLD.1.8.2.5, C-GOLD.1.8.2.6, C-GOLD.1.8.2.7, C-GOLD.1.8.2.8, C-GOLD.1.8.3, C-GOLD.1.8.4, C-GOLD.1.8.4.1, C-GOLD.1.8.4.2, C-GOLD.1.8.4.2.1, C-GOLD.1.8.4.2.2, C-GOLD.1.8.4.2.3, C-GOLD.1.8.4.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.3.2, C-GOLD.1.8.4.4, C-GOLD.1.8.4.5, C-GOLD.1.8.4.6, C-GOLD.1.8.4.7, C-GOLD.1.8.4.8, C-GOLD.1.8.4.9, C-GOLD.1.8.5.; CH03-n: C-GOLD.1.9, C-GOLD.1.9.1, C-GOLD.1.9.2, C-GOLD.1.9.3, C-GOLD.1.9.4, C-GOLD.1.9.5, C-GOLD.1.9.6, C-GOLD.1.9.7, C-GOLD.1.9.8, C-GOLD.1.9.9, C-GOLD.1.9.10, C-GOLD.1.9.11, C-GOLD.1.9.12, C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH05-a: exact read scope and placement in the current source table; prior credits retained. |
| F114 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F115 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read whole; NHD-B24 row searched for this correction; Chapter 3-c NHD-A2/NHD-SLF and dependency navigation searches, not a whole-file read; Chapter 3-d NHD-B16/NHD-B16EEB navigation only | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.; Chapter 3-a: Navigation only: NHD-B11 and NHD-BU1; no behavior sourced from the index; this correction: NHD-B24 navigation for C-READ.7.2 Chapter 3-c: NHD-A2/NHD-SLF navigation only. Chapter 3-d: navigation only, no behavior sourced from index. |
| F116 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F117 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_ACCEPTANCE_RECORD_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F118 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F119 | `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F120 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F121 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F122 | `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-c: whole read; exact scope and placement in the current source table. |
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
| F137 | `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Carried through Chapter 3-a: Relevant passages reopened; earlier whole-read credit retained; scoped passages/searches reopened in Chapter 3-b; earlier whole-read credit retained | C-7A.6 and cited sub-parts; C-7A.13 and cited sub-parts; C-7A.15 and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3. Chapter 3-b: C-READ.7 (excluding the ACCEPTED C-READ.7.2 guard) and C-READ.8 (FR-0125–FR-0133); C-READ.1.12.1 (FR-0123); C-READ.9 (FR-0136).  CH04-c: scoped read; exact scope and placement in the current source table. |
| F138 | `05_ACTIVE_CANDIDATE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CHAPTERS/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH00.md` | Carried through Chapter 3-a: Whole-read in Chapter 1; not reread in that piece | Naming/path continuity only; no Chapters 0–2 (carried placement) behavior sourced from this chapter. |

### V10 heading coverage

| Row | V10 heading | Placement / remaining scope |
|---|---|---|
| V10-H001 | ### This is `NH_MASTER-20_CORRECTED_v10.md`, a corrected candidate in the Master 20 lineage. It is NOT YET ADOPTED. `NH_MASTER-19_CORRECTED_v7_1.md` (SHA-256: `0e8b59e3ce8fd1b4f57367ff524fd2d467d905bb7a789745d13e7f81bd2665cf`) remains the authoritative immutable Master until Ness explicitly adopts the corrected Master 20. | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H002 | ### Historical provenance (Master 19 lineage): | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H003 | ## 0. THE PREMISE — NEVER DECIDE FACTS (NEVER CLOSE THE BOOK)  [DESIGNED — the floor under every rule] | Partial placement: C-7A and cited sub-parts; C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ interpretation remains revisable. |
| V10-H004 | ## 0A. THE TWO MACHINERIES — DUMB vs SMART (psychologics)  [DESIGNED — top-level frame] | Partial placement: C-7A and cited sub-parts; C-7B.1 and cited sub-parts; C-7B.2.5; C-7B.3.2; C-7B.3.3; C-7B.9 and cited sub-parts; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ record-carriage boundary; no new interpretation by the writer. |
| V10-H005 | ## 0B. FULL-TRANSPARENCY AND LIVING-RECORD LAW  [DESIGNED — foundational operating rule] | C-7A.16 and cited sub-parts; C-7A.17 and cited sub-parts; C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ.6 operation records and health-check operation recording.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: held-access and required audit-history boundaries. |
| V10-H006 | ## 1. WHAT N.H IS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H007 | ## 1A. THE INPUT-AGNOSTIC PRINCIPLE — ONE ENGINE, MANY FRONT DOORS  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
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
| V10-H018 | ### SCHEMA CONSTRAINTS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1 and C-READ.2.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H019 | ### PRODUCTION READINGS AUTHORIZATION | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.5 and its protections. |
| V10-H020 | ### PROTECTED FILES AND STORES | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.4/C-READ.5 destination separation; edit workflow excluded. |
| V10-H021 | ### DRY-RUN PROTOCOL | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H022 | ### §12 INCOMING — CURRENT STATUS | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H023 | ## 6B. THE ACCRETIVE STORE — SCHEMA + STATE  [BUILT & VERIFIED] | Partial placement: C-7A.8 and cited sub-parts; C-7B.2.8.4 and cited sub-parts; C-7B.10.1.3; C-7B.11 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1 twelve-field representation; C-READ.2; C-READ.3; C-READ.4.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  Chapter 3-d: governing promotion and living-record boundary comparison; B16 remains ACCEPTED, no BUILT claim.  CH04-b: C-TSC.17.8.3 reuses the existing seven-field root-schema card. |
| V10-H024 | ## 7. THE BIG DESIGN — UNIVERSAL FILTER + MEANING ENGINE  [engines A + B BUILT; §§7E–7P core-conceptually designed S17; §§7D and 7Q partially conceptually designed] | C-7A and C-7B detailed subsections follow. NOT PLACED: engine implementation behavior belongs to Group A. |
| V10-H025 | ### 7A — THE UNIVERSAL FILTER (operating rules): | C-7A and cited sub-parts; C-7B.3 and cited sub-parts; C-7B.11 and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. Chapter 3-b: C-READ reciprocal Universal Filter use; principles retained from Chapter 2. |
| V10-H026 | ### 7B — THE MEANING ENGINE (mechanism): | C-7B and cited sub-parts: operative Group 0 behavior and atomic sub-parts. EXCLUDED: session/build narrative under §1.3. |
| V10-H027 | ### 7C — THE FORCED BUILD ORDER (never re-fought): | EXCLUDED: forced build order under §1.3. NOT PLACED: engine implementations belong to Group A. |
| V10-H028 | ## 7D. THE LIVING STATE WEB — PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ grounded reading consumer relationship. |
| V10-H029 | ## 7E. CATALOG FRONT DOOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H030 | ### §7E-TSC DETAILED DESIGN  [ACCEPTED DESIGN WITH LATER CORRECTIONS — NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-b: full §§1–31 landed in C-TSC and all recursive sub-parts; §31 status evidence only. |
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F.  CH05-c: C-7F and explicit shared/deferred owners. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-b: C-7GA and explicit shared/deferred owners. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-a: C-7G and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H.  CH05-d: C-7H and explicit shared/deferred owners. |
| V10-H035 | ## 7I. VIEW LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ history/current-view use; view machinery remains with C-7I. |
| V10-H036 | ## 7J. CONTRADICTION AND CLASH HANDLING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ clash-consumer relationship; clash machinery remains with C-7J. |
| V10-H037 | ## 7K. STORY LAYER  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7A.8.3; C-7B.3.1; C-7B.3.3 and cited sub-parts; C-7B.3.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ.1.5/1.6 speaker/perspective and embedded-v1-telling boundaries; future telling identity remains for its accepted package.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H038 | ## 7L. PERSON-BOXES  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.4. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ Person-Box consumer relationship. |
| V10-H039 | ## 7M. COMPUTED VIEW  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ current-use consumer relationship. |
| V10-H040 | ## 7N. ACTION SURFACING  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H041 | ## 7O. ACTION-RESULT RETURN PATH  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H042 | ## 7P. PERMISSION AND AUTHORITY BOUNDARIES  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. |
| V10-H043 | ## 7Q. PRIVACY, DELETION, AND SENSITIVE-DATA HANDLING  [PARTIALLY CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-e: C-9A and explicit shared/deferred owners. |
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
| V10-H066 | ## 9A. IMAGE INGEST — FIRST WORKED FRONT-DOOR EXAMPLE  [DESIGNED] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H067 | ## 10. ORIGINALITY (honest calibration) | Partial placement: C-7B.9.3. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. |
| V10-H068 | ## 11. WHAT'S OPEN / NEXT (priority order) | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ foundation status and quarantine/production boundary; restored details use the decision record plus named archive, not the compressed V10 line. |
| V10-H069 | ## 11-SETTLED. (condensed) | EXCLUDED: condensed decision/session narrative under §1.3; repeated runtime rules are represented by their detailed owning sections. |
| V10-H070 | ## 12. SESSION 6 — THE DATA-RESCUE OPERATION  [recovery done; ingest FROZEN] | EXCLUDED: history, provenance or build/process narrative under contract §1.3.  CH04-e: C-9A and explicit shared/deferred owners. |
| V10-H071 | ## 13. THE LIVE LOOP  [DESIGNED — not built] | Partial placement: C-7B.9; C-7B.10.1 and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners.  CH05-e: C-CREATE and explicit shared/deferred owners. |
| V10-H073 | ## 15. SESSION 10 — BOOT HYGIENE + SIGN-IN + .CURSORRULES  [housekeeping done] | EXCLUDED: history, provenance or build/process narrative under contract §1.3. |
| V10-H074 | ## 16. THE MODEL LAYER — THE BORROWED MOUTH + THE SEARCH MODEL  [DESIGNED + partly on disk] | Partial placement: C-7B.6. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners. |
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

### Carried bridge source landing map

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

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7J / SIX CLASH TYPES | Six exact kinds and their defining differences | C-7J.1 and C-7J.1.1–C-7J.1.6 |
| V10 §7J / GENUINE CONTRADICTION VS CONTEXTUAL DIFFERENCE | Simultaneous truth under the same conditions, person, time and context; no resolution | C-7J.2 |
| V10 §7J; Bundle 3 §10 | Original clash and all eleven fields; telling pointers and source chains | C-7J.3 and C-7J.3.1–C-7J.3.11 |
| V10 §7J / TWO DETECTION MODES, SAME RECORD TYPE | Triggered comparison scope; wider scope; bounded/configurable periodic scanning; no authority by mode | C-7J.4, C-7J.4.1, C-7J.4.2 |
| Bundle 3 §10 | Conflicting-item set plus aspect; match/no-match; one commit path; crash recovery from committed records | C-7J.5 |
| Bundle 3 §10 | Detection-history event: mode, time, configuration, confidence; no duplicate or extra weight | C-7J.5.1 and C-7J.5.1.1–C-7J.5.1.4 |
| V10 §7G-A / claim validation, Step 7, checkpoint 7A, sentinels and RC-6/RC-7 | Operation key; recover before rerun; no_clash_sentinel; system failure keeps job in_progress; checkpoint handoff | C-7J.5.2; exact claim/checkpoint/sentinel fields remain the existing C-7GA cards in CH05-b |
| V10 §7J / NESS'S RESPONSE AS SEPARATE EVENT | Seven response fields; eight stated type alternatives; multiple responses; separate linked downstream actions | C-7J.6 and C-7J.6.1–C-7J.6.7 |
| Bundle 3 §8 | Recording never blocked; six downstream uses; qualified support; no clear current view; permanent clash; new linked refinements | C-7J.7, C-7J.7.1, C-7J.7.2 |
| Bundle 3 §17 | Distinct weightless reading response and clash response | C-7J.7.3; full reading-affirmation mechanics left to CH08-f |
| Bundle 3 §16 | Clash marker; detail pane; respond only; explicitly recorded named absence; plain main surface and precise side notes | C-7J.8 and C-7J.8.1–C-7J.8.3 |
| V10 §0B; Bundle 3 §19 | One real operation, one record; no recursive logging or double evidence; presentation/response log contents | C-7J.9 and C-7J.9.2 |
| A2 §§5A.1, 5A.3, 6, 10 | Canonical telling identity, semantic eligibility, blocked/skip/resume provenance; no private payload or double evidence | C-7J root, C-7J.3.3, C-7J.9.1; existing C-READ.10.10 and C-READ.10.14 reused |
| V10 §7Q; Bundle 3 §20 | Purpose-specific internal-use versus visible-output boundary; protection and identity gates | Current authorization boxes; full privacy architecture left to CH08-a |
| V10 §§7D, 7M; MAP C-7J | State evidence and current-view handoffs with conflict preserved | C-7J and cross-piece continuations; full consumers left to CH06-d/f |
| Bundle 6 mechanical §12 | Authorized clash-read result contains records and Ness responses with component provenance | C-7J USED BY C-LMAC; full query protocol left to CH08-c |
| Bundle 3 acceptance receipt; A2 package-complete receipt; Bundle 6 mechanical receipt | Exact accepted package identities/status, no new behavior | READ RECORD; receipt workflow/history excluded under §1.3 |
| Decision Defaults §§3G–3H; Companion §7J | Authority comparison and repeated conceptual clash content | No independent extra mechanism; current C-7J placement follows V10 and accepted scoped additions |
| Active decision index v0_11; A2 current-status note; September 24 recovery record and September 25 buckets | Navigation, dependency and restoration-scope checks | No behavior from the index or ledger; non-clash restored memory-health scope retained for later owners |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7K responsibilities and must-nevers; MAP C-7K | Unaltered receipt, perspective/theme/time organization, query scope, no narrative synthesis or winner | C-7K |
| V10 §7K / TELLING VS ONGOING STORY | One pass/root/perspective/moment; collection with agreements, shifts, contradictions and silences | C-7K.1 |
| V10 §7K / CONNECTIONS ACROSS TIME; A2 §8 | Five shared-attribute routes; labeled basis and root/reading pointers; temporal change distinct from contradiction | C-7K.2 |
| V10 §7K / STRUCTURED PERSPECTIVE MODEL; A2 §3 | Three required roles, optional attribution chain, five evidence relationships, unresolved attribution, separate engine lens, v1 whose compatibility | C-7K.3; shared field cards C-READ.10.1.4–C-READ.10.1.8 retained |
| A2 §§5A–6 and §8 | Immutable telling_id, Story Layer ownership, complete-set gate, zero-telling, no embedded/partial substitute, new IDs on reread | C-7K.4 and current interface fields; existing C-READ persistence/recovery atoms retained |
| V10 §7K / FIRMNESS RULE; firmness policy §§1–6 | Six qualitative outcomes with criteria, mandatory basis and hierarchy, no score, independent reading confidence, less-claiming/omission/revision rules | C-7K.5; existing C-READ.10.1.11 and C-READ.10.1.12 atoms retained |
| V10 §7K / HYBRID THEME SYSTEM | Engine proposes, only Ness confirms; indefinite unresolved status, no circularity or confirmation by repetition/time | C-7K.6 |
| Bundle 3 §11 / Theme record | Stable ID, vocabulary label, status, proposer, creation time, append-only versions | C-7K.6.1 and six field cards; two status cards under C-7K.6.1.3 |
| V10 §7K / HYBRID THEME SYSTEM | Each proposal's root IDs, telling/reading IDs, proposer, why connected, timestamp and uncertainty | C-7K.6.2 and four support atoms; proposer/time reuse C-7K.6.1.4–C-7K.6.1.5 |
| A2 §7; Bundle 3 §11 / Membership links | Non-exclusive telling_id membership and five provenance fields; no copy/move/fact; legacy unconfirmed | C-7K.6.3; existing C-READ.10.14.8 and its atoms retained |
| Bundle 3 §11 / Grouping and Aliases | Member sets, alias families, root support, no circularity, bidirectional new alias records | C-7K.6.4 and C-7K.6.5 |
| Bundle 3 §11 / Theme actions | Confirm, reject, rename, merge, split, leave unresolved; event inputs/results and preservation boundaries | C-7K.6.6 and C-7K.6.6.1–C-7K.6.6.6 |
| V10 §7K; A2 §7; Bundle 3 §11 / Influence honesty | Actual influence recorded in why-admitted retrieval provenance; no policy invented; later reading free to disagree | C-7K.6.7; full retrieval owner CH05-c and full relevance owner CH08-b |
| Bundle 6 policy §4 A3.5 | Holding through linked separate objects; Ness understanding visibly distinct; no second profile/store or fact by strength | C-7K.7; Person-Box implementation scope left to CH06-c |
| V10 §0B; MAP C-7K; Bundle 3 §§18–20 | Per-operation logging, immutable records, privacy/identity authorization, no double evidence | C-7K.8 and current gates; full protection mechanisms left to CH08-a/CH09-d |
| A17 §7; Bundle 6 mechanical §12 | Wonder possibility cannot enter stories as observed reality; LMAC returns perspective-owned tellings with clashes | C-7K boundary and USED BY interface; full Wonder remains C-7B and full LMAC remains CH08-c |
| Accepted firmness, Bundle 3, A2 and Bundle 6 receipts; A17 receipt | Exact package identities and accepted scoped status; no new behavior | READ RECORD; receipt workflow/history excluded under §1.3 |
| DD §3G; Companion §7K; Bundle 1 normalization firmness identity; active indices and A3 working record | Authority/status and dependency comparison | Current behavior follows V10 plus accepted scope; no index/working-note mechanism imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7L responsibilities, must-nevers and link types; MAP C-7L | Stable identity gather, eight source families, provenance, no profile/fact/closure and CY-A use | C-7L |
| V10 §7L link fields; Bundle 3 §§7/12 | What, why, who established, certainty, timestamp; four ordinary qualitative outcomes | C-7L.1 and field/outcome children |
| V10 §7L uncertain identity; Bundle 3 §§7/12 | Label/name, where, when, evidence, current outcome; indefinite unconfirmed anchors | C-7L.2 and five field cards |
| V10 §7L proposal-based creation; Bundle 3 §§7/12 | Stable ID; separate names/labels/roles; four search scopes with occurrence/scope recorded | C-7L.3.1–C-7L.3.3.4 |
| Bundle 3 §7 | Completely clear and definitely identifiable as the same person; automatic met-test action, pending unmet-test action, no scores or added manual approval | C-7L.3.4 and C-7L.3.5; outcome atoms under C-7L.1.4 |
| V10 §7L; Bundle 3 §§7/12/18 | Confirm, reject, rename, keep unresolved, link to existing, propose merge; preserve history | C-7L.3.6 and six response cards |
| Bundle 3 §12 | Seven append-only event kinds; candidate pair, gathered evidence, named gap; non-destructive joins and wrong-join corrections | C-7L.3.7 and event/proposal-field children |
| Bundle 3 §9 | Ness's confirmed stable ID, settled-fact provenance, clear first-person source links, ambiguous pasted-I pending, ordinary maintenance | C-7L.4 |
| V10 §7L default view; Bundle 3 §§13/15 | Seven headed sections with contents/status lines; compact and expandable records; newest usable; chronology; grouping-only responses/supersession; best-supported delegation | C-7L.5 and seven section cards; full Current/History owner CH06-e |
| Bundle 3 §15 | Five visibly active composable filters, clear-to-default, one-switch chronology, owner labels and pointer-only expansion | C-7L.5.8–C-7L.5.11 with filter atoms |
| Bundle 3 §16 | Clash marker/detail/respond, separate events; named absent item/kind, no inferred content; plain main wording and side notes | C-7L.5.4 and C-7L.5.7; shared C-7J.8/C-7J.8.3 retained |
| Bundle 3 §14 | Per-element batch identity, cross-batch identity tag, one ID view, no seal writes, ordinary tests across batches | C-7L.6 and two provenance fields |
| Bundle 6 policy §4 A3.5 | Holding through separate existing objects; Ness's understanding distinct; no fact by repetition, recency or strength | C-7L.7; existing C-7K.7 retained; exact layout still open |
| V10 §7L; Bundle 6 closeout §9; B15 §11; A16 retained archive boundary | Safe held metadata/state/blockers only; raw content excluded; sealed TSC has no inspection path | C-7L.8 and current C-7E.11 reciprocal; full archive owner C-TSC retained |
| V10 §§25.2/25.4; Bundle 6 mechanical §12 | PBR path through LMAC, seven initial categories, presence condition, version refresh and query failure to guest; separate parents and visibility | C-7L.9 and four interface cards; full PBR/access lifecycle CH09-b/d |
| V10 §25.3 voice-profile architecture and minimum linking evidence | Separate identity authority and six ordinary unknown-speaker prerequisites; empirical minima remain open | C-7L.10 and six prerequisite cards; full SIA CH09-c |
| B-INT-7 §§12A/13/14/19 | Provisional enrollment type, certainty, stable proposal ID, meaning, basis and exact reference fields; owner commit; replay lookup; six handoff outcomes | C-7L.11 and field/result children; full enrollment/SIA internals CH09-h/c |
| B-INT-8 §§12C/14/15 | Ten identity-separation rules; nine current-use checks; three proposed current-use result meanings; fail closed; route privacy and influence removal | C-7L.12 consumer boundary; full current-use records/states remain CH06-g |
| Bundle 6 mechanical §12 | Authorized box-ref query and actual certainty; PBR route; minimum authorization metadata before protected release | C-7L.13; full LMAC CH08-c |
| V10 §0B; MAP C-7L; Bundle 3 §§18–20 | One append-only record per real operation, search/evidence basis, presentation version/filters/history, no evidence inflation | C-7L.14 and current gates |
| A2 §§5A/6; A17 §7 | Complete telling-set semantic gate; first-class telling_id references; Wonder cannot become observed reality about a person | C-7L current root and telling interfaces; existing C-READ and C-7B owners retained |
| A7/B7 current-surface privacy; A26/B-INT-5 identity/access; Bundle 5 closeout | Purpose-bound privacy and visibility, per-surface hiding obligation, PBR read boundary; no imported access or privacy authority | Current gates and C-7L.5 failure boundary; complete mechanisms retain CH08-a/CH09 ownership |
| DD §3G; Companion §7L; accepted receipts; active indices/working records; September 25 Group 6 | Authority/status comparison and identity checks; restored thin-evidence query retains its existing owner | READ RECORD and source dispositions; no workflow or index text used as behavior |
| Bundle 4; Bundle 2; A19; Five Framework; operation kernel; future/intent notes | Other-owner links, derived presentation and identity-authority boundaries | Named later ownership in scope dispositions; no full package-completion claim |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-d

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7M; MAP C-7M | Internal current-picture purpose, source preservation, quiet use, deliberate inspection, honest no-clear-view, current/history and downstream direction | C-7M/C-7M.1 with existing C-7A/C-7I/C-7N relationships |
| V10 §7M seven-factor priority order | Seven ordered factors, direct support over frequency/confidence, context provenance, beside-item conflict, recency last, no collapsed score | C-7M.2 and seven factor children |
| Bundle 4 §8.1 | Nineteen conceptual profile fields, immutable versions, exact tier references, declared rules/triggers/invalidation, version/time/log history | C-7M.3 and field/rule children |
| V10 §7M update timing; Bundle 4 §8; Bundle 2 §7 | Opening, manual refresh and materially relevant event routes; six material-event kinds; no unrelated global update | C-7M.4 with trigger children; C-7M.10.7 |
| Bundle 4 §8.2 | Immutable snapshot fields, ten source-reference families, direct-root pointers, separate factors, omissions/reasons, prior/change/why, committed completeness, privacy/log references | C-7M.5 and fields; exact profile/version/derivation/time/log atoms reused from C-7M.3 |
| Bundle 4 §§8.3–8.4 | Eleven refresh-event fields; standing/staleness from latest valid applicable events only; five outcomes and their distinct consequences | C-7M.6/C-7M.7 and children; shared operation_id/created_at/log references reused |
| Bundle 4 §§8.5–8.6 and §13 | Operation plus source/version identity, at most one snapshot, event-only null/failure/incomplete, six crash/recovery cases, technical retries by reference | C-7M.8/C-7M.9 with six recovery cases; existing B9 owners retained |
| Bundle 2 §§5.1–5.2 and §7; A4 §3 | Proposed declaration identity/version, controlled purpose, target, candidate families, tier ownership and complete validity | C-7M.10.1–C-7M.10.3 and root; candidate family field reused; C-7F.6.14 validity retained |
| Bundle 2 §7 | Deterministic object-type gate, conditional declared-time gate; no universal thread/precedence gates | C-7M.10.4 and two gate children |
| Bundle 2 §§5.2–5.3 and §7 | All nine dimensions with producers, version provenance and applicability; honest missing/inapplicable outcomes | C-7M.10.5 and nine selection children; shared absence atom retained |
| Bundle 2 §§5.3/7 | Explicit none mouth authorization; future dimension-specific version/validation conditions; no precompute or continuous evaluation | C-7M.10.6/C-7M.10.7; full validation architecture remains CH08-b |
| Bundle 2 §7 Tier 2; §4 quiet-use/material-uncertainty rules | Factor 4 only, attached uncertainty/source/older-pattern labels, honest fallback, quiet internal use and downstream uncertainty disclosure | C-7M.10.8/C-7M.10.9 and consequence children |
| Bundle 2 §5.3 proposed shared uncertainty rule | Validated is interpretation; failed unused; weak unresolved/disputed clues; seven prohibited sole consequences; checks allowed; disagreement record; honest absence | C-7M.10.9.4 with existing C-7F.6.10.5.1–.5 outcome owners |
| Bundle 2 §§5.5–5.7 and §7; Bundle 4 §§11–12 | Privacy-first authorized families, no feedback into state, no self-evidence/access widening; evaluation record; no snapshot for invalid profile/declaration; unknown-purpose halt | C-7M.10.10–C-7M.10.12; full relevance record/vocabulary ownership CH08-b |
| Bundle 4 §14.1; V10 §0B; September 25 Group 10 | One connected operation log, actual evaluated/used/unused/omitted/outcome/retry/recovery/prior-use/result content, no recursive logging or extra evidence | C-7M.11/C-7M.11.1; existing C-7B.10.2/.3/.5/.8 retained |
| Bundle 4 §§9.1/13/14.1 | Domain operation keeps its physical-effect level; log append separate linked Level 2 under same identity, no merged accounting | C-7M.11.2 |
| Bundle 4 §14.2 | Initial active without exception; five active protections; absence not sufficient to cool; fixed component-owned versioned rule; future change evidence and Ness approval | C-7M.11.3.1 with five protection children; C-7M.11.3.2; existing generic rule-change atoms retained |
| Bundle 4 §14.2 | Both cooling conditions, priority-only change, exact retrieval preserved; actual-use/valid-link reactivation only; uncertain evaluation preserves prior state | C-7M.11.3.3–C-7M.11.3.5; existing C-7B.10.6 condition atoms retained |
| Bundle 4 §§14.3–14.4 | Fourteen lifecycle-event fields, active/cold only, initial previous_status empty, failed evaluation not a third status; three distinct record kinds | C-7M.11.4 fields plus shared operation/time/log atoms; C-7M.11.5 |
| Bundle 4 §§7.2/8/11–12/14 | Evidence family counts one independent event, all members individually preserved, logs no extra vote; strict state-to-view-to-action direction | C-7M.2.2/current boundaries; full evidence-family schema CH06-f |
| Bundle 6 policy §4 A13.2; mechanical §6 | Relevant provisional influence only through own operation's provisional_material_used entry; visible provisional context, exact record/status-at-use, no confirmation by repetition | C-7M.12; existing C-CREATE.8.1/.8.5 owners retained; fixed-family representation remains an explicit gap |
| V10 §7M; Bundle 2 §7; Bundle 6 closeout §9; B15/A16 archive isolation | Safe held metadata/state/blockers only; no raw influence/ranking/snapshot/output or TSC inspection | C-7M.13 and C-7M.5.5.10; C-7E.11 source reciprocal present |
| A2 §§5A/6; Bundle 3 §§8/13/16 | Complete-set telling eligibility, first-class reference use, conflicted support and requested best-supported person picture | Current root and factor/source interfaces; existing telling/clash/person atomic owners retained |
| A4; B7; B-INT-5/B-INT-7; AIC; Bundle receipts; DD/Companion; active indices; recovery ledger | Current scope and authority comparison, protected-surface/identity limits, package status, other-owner snapshot terms, ledger-only tracking | READ RECORD and scoped dispositions; no unrelated authority/session snapshot mechanism imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-e

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7I; MAP C-7I | Two views, simple/default and complete/on-demand, source preservation, newest-usable versus best-supported, output-to-Ness destination | C-7I root and Current/History cards |
| Bundle 3 §13 current usable | Acceptance passed AND not rejected AND not insufficient_context; usable is not true/final | C-7I.1.1 with three condition atoms; acceptance mechanism retains C-7G |
| Bundle 3 §13 Current grouping | Newest usable first per root and applicable person/theme grouping; three visible status kinds | C-7I.1/C-7I.1.2 and three label cards; C-7I.3 grouping scope |
| Bundle 3 §§8/13/16 | Conflict beside item, qualified/withheld weak support, exact detail and respond-only path, no winner or suppression | C-7I.1.3; existing C-7J.8.1/.8.2 retained |
| V10 §7I; Bundle 3 §13 | Best-supported or broader current-picture claim invokes seven factors, recency limited to tie-break | C-7I.1.4; current C-7M/C-7M.2 references |
| V10 §7I; Bundle 3 §13 | Complete strict chronology, always available, one switch away; optional mode grouping cannot hide history | C-7I.2/C-7I.2.1/C-7I.3 |
| Bundle 3 §§8/13/17 | Responses and changed/replaced flags alter grouping/labels only; separate weightless responses, no response means no change/block; changed judgment new event; dismissal current-use route | C-7I.4 with two input children; full B-AFFIRM event fields remain CH08-f |
| Bundle 3 §15; MAP C-7I | Shared seven-section discipline, filters visible/composable/clear-to-default, chronology and owning-layer labels, complete-on-demand pointers, no synthesis/person score | C-7I.5; existing C-7L.5 and descendants retained |
| Bundle 3 §16 | Explicit named absence and owning-layer kind only, no inferred content or proof; plain main wording and precise side notes | C-7I.6/C-7I.7; named-gap atom remains C-7J.8.3 |
| MAP C-CREATE; Bundle 6 mechanical §6 | Store-backed creation views, provisional-plus-history ideas in progress, no display-derived confirmation, unverifiable status provisional | C-7I.8; existing C-CREATE status/view owners retained |
| MAP C-7I; Bundle 3 §19; V10 §0B | One log per real view/named-gap presentation; snapshot/version, filters, History switches; no evidence inflation; access gates | C-7I.9 with three record-content fields; existing general Log atoms retained |
| Bundle 3 §20; B7 §15.4 | Privacy before surfacing, normal-inspection surface hiding, protective unverified/blocked/failed/partial withholding, visible suppression distinct from influence removal | C-7I.10 and root failure boundary; complete B7 record/lifecycle/verification/restoration owners remain CH08-a |
| B10 §5 proposed RR-PR | Post-commit view/index projection consumes a new layer, rebuildable idempotently, never gates success or owns status | C-7I root current-use boundary; C-7H.3.7 retained |
| DD §3G; Companion §7I; Bundle 3 receipt; active indices; recovery ledger; future-feature note | Status/authority comparison, acceptance identity, current scope and later intent/pending-restoration navigation | READ RECORD and source dispositions only; no history or workflow imported as behavior |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-f

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7D; MAP C-7D; DD §3G; Companion §7D | Eight structural families, grounding and independent currency, inputs/governors/downstream uses, privacy, no path choice, exact open slots | Root and C-7D.1–.8; currentness/common contract; later-owner boundaries |
| Bundle 4 §4A | Four qualitative A31 labels and less-claiming discipline | C-7D.9.5/.9.20; existing C-7G.8 labels reused |
| Bundle 4 §4B decisions NHD-A6-1/NHD-A6-2/NHD-A6-3; §5; §7 | Automatic permitted observation, direct-self-report/several-sign inference, evidence/materiality separation, routine currency without manual approval | C-7D.1/.10/.11 and their condition/transition cards |
| Bundle 4 §4B decisions NHD-A6-4/NHD-A6-5; §7 | Separate simultaneous positions, grounded tension, causal hypotheses, alternatives and separately grounded chain links | C-7D.2/.3/.6 and field children |
| Bundle 4 §4B decision NHD-A6-6; §5; §7 | Core vocabulary, automatic grounded precise description, broader category, search-before-create | C-7D.12 and three fields; C-7D.11.10 matching |
| Bundle 4 §4B decision NHD-A6-7; §7 | Needs/fears careful possibilities, several signs, stronger protected-boundary basis and protection marker, scoped practical constraints | C-7D.8.1–.8.4 and schema fields |
| Bundle 4 §4B decision NHD-A6-8; §7 | Five separate grounded/currentness capacity slots, optional supported overall summary and supporting-dimension list; no emotion/wellbeing/identity conflation | C-7D.13 and dimensional/summary fields |
| Bundle 4 §4B decision NHD-A6-9; §5; §7 | Six currency states, five aging factors, dated reasoned events, assessments, no hidden decay/time-only ending | C-7D.10 with states/events/aging factors/assessment fields |
| Bundle 4 §4B decision NHD-A6-10; §5; §7; Bundle 2 §10 | Review prompt versus inspected evidence, recorded reason, uncertain suggestion, no blanket reread, exact authorization remains open | C-7D.14/.14.1 and trigger fields; C-7D.11.4 |
| Bundle 4 §4B decision NHD-A6-11; §7; accepted A17 §7 | Automatic internal hypothetical paths, four purposes, evidence/assumptions/marker/flag, no self-evidence/action permission/history rewrite, simulation approval boundary | C-7D.7 and five fields; later simulation scope preserved |
| Bundle 4 §4B mechanical domains; §7 | Relationship/safety attribution, stable Ness identity, proposed cross-time continuity, movement separate from cause/ending/supersession | C-7D.5/.5.1/.15; transition and hypothesis structures |
| Bundle 4 §7 common contract | All common provenance/time/grounding/currency/uncertainty/history/authority/operation fields | C-7D.9.1–.9.17; C-7D.10; existing C-7M.5.2 reused |
| Bundle 4 §7 evidence family and grounding chain | Separate preserved same-event members, one independent unit per family, every chain link retained, no operational second vote | C-7D.9.18 and identifier/member/count atoms; C-7D.9.19 |
| Bundle 4 §7 state lifecycle | Creation, accumulation, review, reassessment, promotion, stale/unknown, end/supersession, new-version reactivation, linked correction, five episode-match outcomes, incomplete and omission failures | C-7D.11 and lifecycle/matching children; C-7D.9.20; C-7D.17 recovery |
| Bundle 4 §4D; §6; §7 | Layered active core/wider knowledge, nine structural distinctions, nine grouped qualifying basis kinds, multiple independent bases, world entity/condition/self↔world families | C-7D.16.1–.16.4/.16.7 and boundary/basis children |
| Bundle 4 §6; §7 membership event/lifecycle | All fifteen membership fields, two policy states, separate dimension, grounded activation, cessation plus no other basis, idempotency, precommit/missing-log/unsafe outcomes | C-7D.16.5/.16.6; existing operation/time/log fields reused |
| Bundle 2 complete §10; shared §5.1–§5.7 | Proposed RM-LS-01 v1_0, thirteen declaration fields, six candidate families, selected gates and six producers, no mouth/currentness dimension, on-demand timing, Tier 2 and three failure classes | C-7D.14.2 and children; existing A4 validity, gate and proposed T2-UNRES-SHARED atoms retained |
| Bundle 4 §§11–12; A2 §§5A/6; B3 identity/firmness interfaces; A7/B7 consumer boundary | Permitted evidence fan-in, target telling IDs and complete-set gate, governors not evidence, held-raw/TSC exclusion, internal/visible authorization and third-party rules | Root and common grounding, relation/person/telling interfaces; full privacy remains CH08-a |
| Bundle 4 §§13–14 | Stable identity/source version/idempotent commitment, startup/partial/reconciliation/retry/uncertainty, one log per operation, separate level accounting, five active protections, two cooling conditions, use/link reactivation, fourteen event fields and three record kinds | C-7D.17 and current consumer cards; existing B9 and shared C-7M log/lifecycle atoms retained |
| Accepted room-start §6; active UE5 §2.3; branch/simulation intent §3B.6; framework §§18–21 | Presentation cannot rewrite Living State; actual/history versus simulation distinction; future index/interface scope | C-7D.16.3.7 non-effect; other mechanisms left to their named later owners |
| Acceptance/closure receipts; active A2 status and decision indices; recovery ledger | Accepted package identities and older-open-slot navigation, intent status and restoration-only tracking | READ RECORD and dispositions; no workflow or recovered historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH06-g

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §24; MAP C-24; DD §3J; Companion §24 | Two responsibilities, originals separate, waiting, three bases, one-way retrieval, uncertainty, five types, pending silent investigation | C-24 and .1–.6; source-specific accepted mechanics retain their own stamps |
| B-INT-8 §§3–4 | Proposed recordkeeper scope; separate accepted record and retrieval; illustrative type list; proposed versioned type/direction contract | C-24.1/.2/.7/.8 and three contract fields with two directionality values |
| B-INT-8 §5A | Two direct-source entries; actual owner verification; exactly three outcomes and their consequences; failed-history-preserving later routes | C-24.4.1 and .1–.4; C-24.2.3; candidate/report distinction |
| B-INT-8 §5B; §7B | Exact explicit Ness choice, no implied consent, four identities, five route steps, complete precommit set and all ten forward-completion conditions | C-24.4.2; .9.2/.9.2.1 and ten condition cards; .12.3–.5 |
| B-INT-8 §5C; §7C | Existing narrow rule, ten verifiable facts, exact match, current final validation and atomic rule proof | C-24.4.3 and its rule ID/version plus remaining fields; .9.3 |
| B-INT-8 §6; §12A–B | Waiting location versus three decision values; sixteen parent states with transitions and direct bypass; five candidate states and three owner outcomes | C-24.3/.3.2; .13/.13.1/.13.2 and state cards |
| B-INT-8 §§7/7A/7D | One atomic compare-and-commit, durable proof/checkpoint, exact direct-route validation, separate rejection input/final event and suppression | C-24.9/.9.1/.9.4; crash cases and interface boundaries |
| B-INT-8 §8 | Five certainty labels, five exact source-type labels, no numeric mapping, authority/evidence/status separation and material output uncertainty | C-24.5/.6 and value cards; proposed schema consumers |
| B-INT-8 §9 | Proposed CRK minimum fields, symmetric normalization, directional distinction, separate types, racing routes, proposed authority-event key and same-proof idempotency | C-24.10/.10.1/.10.2; .8 and endpoint/authority atoms reused |
| B-INT-8 §10 | Rejected history, verified genuine delta/new ID/backlink/same key, six non-deltas, owner judgment and proposed suppression registry | C-24.11/.11.1; .3.1.3/.3.1.4; crash 17 |
| B-INT-8 §11 | All proposed endpoint, proposal, accepted, durable-input, final-decision, authority, correction, use, duplicate, parent, candidate, suppression and recovery records and slots | C-24.1.1; .3.1; .12 and field children; .10/.11/.13/.14 shared atoms |
| B-INT-8 §12C | Immutable history, backwards correction links, nine per-use resolution inputs, separate proposed state namespace, three outcomes and fail-closed, changed-geometry new version/key/both-links | C-24.14/.14.1/.14.2 and children; .12.6; retrieval/identity/output consumers |
| B-INT-8 §13A–D | Accepted use through LMAC, pending investigation marker and separation, candidate submission, complete retrieval audit additions | C-24.2.1–.2.3; .2.2.1; .12.7 with field-level audit additions |
| B-INT-8 §14; prior Bundle 3 identity rules | All ten generic-connection/identity rules, clear/unclear and definite/less-than-definite owner tests retained without duplicate identity approval; fresh current-use/privacy before handoff | C-24.15 and I8; existing C-7L.12 reused in full |
| B-INT-8 §15; B7 §16; B-INT-5 §13 | Privacy before all internal operations/commits, influence removal separate, no endpoint permission, opaque Level-1 references, shared output ceiling and no hidden signal | C-24.16; route gates and I1–I11 authorization columns |
| B-INT-8 §16 | All twenty-two crash boundaries and all nine descriptive columns: truth, recovery, key, retry, fresh action, duplicate rule, failure and audit | C-24.17.1–.17.22; common lookup-first and no-authority-reconstruction rules |
| B-INT-8 §17 | B9 by reference, same-operation technical-only retry, nine forbidden automatic retry classes and fresh decision/new evidence distinctions | C-24.18; existing C-7H.9/.10 |
| B-INT-8 §18 | All eleven interfaces and nineteen source columns including explicit n/a judgments, request/response schemas, owner truth, identity, authorization, recovery and current-use | C-24.19.1–.19.11; existing schema atoms reused |
| B-INT-8 I10; B-INT-6 §§3–5/6A | Separate stable output parent, separate request-plus-destination delivery token excluding mutable versions, per-attempt identity/facts, full output-chain ownership and honest duplicate scope | C-24.16.1–.16.3; .19.10; later full output mechanism remains CH09 |
| B-INT-8 §19 | One parent, all twenty-eight child kinds, all decision/use outcomes, no recursive/weighted logs, actual-use/valid-link cold reactivation, authorized log access | C-24.20/.20.1; existing C-7B logging/access atoms reused |
| B-INT-8 §§20–22 | All named fail-closed classes and outcomes; exact open mechanical slots and must-nevers | C-24.21 and four additional failure cards; route/status/recovery owners; gap register |
| Durable Operation Kernel §K; §T I-11; §U connection owner; scoped AF-6/AF-9 and R-33 | Generic coordination cannot replace connection claims/keys, split proof, perform/replay effects or substitute for fresh per-use resolution; connection terminals stay local | C-24.22 reference-only consumer boundary; general kernel mechanisms remain separate |
| B-INT-8 receipt; Bundle 5 closeout/receipt; active indices; recovery ledger | Exact accepted package, authority/output identity consistency and restoration-only navigation | READ RECORD; no workflow imported; Appendix B tracking carried |
| Active A19 §§13.2/13.3/16.2/16.3; future-feature intent; framework direction | Cards remain references and deliberate association does not silently accept; future unified search/index direction | Later C-19/CH10-e presentation and search owners; no invented current acceptance machinery |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7N; MAP C-7N; DD §3G; Companion §7N | Gentle question, single invitation, decline/ignore/no-response closure and personal reopening; conflicting Map new-trigger summary retained | C-7N/.1/.1.1–.1.3; header conflict |
| V10 §7N | Permission-controlled hybrid; explicit request always permitted; authorized proactive rule; settings may disable entirely | C-7N.2/.2.1–.2.3 |
| V10 §7N; B4 §10 | All three required forms and all three prohibited instruction forms, as exact source examples | C-7N.3/.3.1/.3.2 and six bottom-level form cards |
| V10 §7N; B4 §9.2; formal B2 §8 | Five possibility fields, support references, per-item labels, current-label provenance, stable record identity; separate later action; new-record L2 versus pure-read/display L1 | C-7N.4 and nine field cards; shared stage contract |
| V10 §7N; B4 §9.2 | All six states and exact consequences: separate accepted action, rejection event, modified basis, optional postponement reason, ignored exception, new alternatives pass | C-7N.5/.5.1–.5.6 |
| V10 §7N; B4 §9.1; formal B2 §8 | Weak/conflicted/stale/insufficient support, impact-based stronger review, protective/active lanes and current-support asymmetry | C-7N.6/.6.1/.6.2; prior A31 reused |
| B4 §9.2 | Five separate common stage/level fields, exact three stage values, current physical operation versus prospective level/categories and advancement requirements | C-7N.7, five field cards and three stage-value cards; later CH07-b/c consume them |
| B4 §10 | Four required display facts, approval/attempt/effect/result distinctions and all thirteen illustrative canonical forms | C-7N.8/.8.1 four facts/.8.2 distinctions/.8.3–.8.15 forms |
| B4 §§11/12 | Downstream source/picture/surfacing/normal-return wiring; privacy before SACL, governors never evidence, evidence families and less-claiming grounding | C-7N.9/.10; established C-7D/C-7M/C-7G.8/C-24.14 boundaries reused |
| B4 §13 | Stable identity and source-version key, record-level atomic commit, startup unfinished work, missing-record reconciliation, partials, technical-only B9, stage integrity and uncertain-effect freeze | C-7N.11/.11.1–.11.7; prior operation and external-effect atoms reused |
| B4 §14 | One connected operation log, content and level separation, five active protections, owned versioned rules, both cooling conditions, valid reactivation, failed-evaluation preservation and three separate record kinds | C-7N.12/.12.1–.12.3, five protection atoms, two cooling conditions; shared fourteen-field lifecycle event retained |
| Formal B2 §§4/5.1; §8 items 1–4 | Quiet automatic evaluation, proposed identity/version, tier ownership, controlled purpose, target and all candidate families | C-7N.13/.13.1–.13.4 with identity/version and target/pool atoms |
| Formal B2 §8 item 5 | Only object_type_matches is categorical; three other gates not selected; present-context label consumed from live or current positional provenance, never thread/time inferred | C-7N.13.5/.13.5.1; existing object-type and item-provenance atoms |
| Formal B2 §8 items 6–9 | Nine dimensions with embedding versus deterministic producers, state/reading-only applicability, response/clash handling, no mouth, on-demand timing/settings, no pre-computation and reason | C-7N.13.6 with nine atoms; .13.7/.13.8/.13.9 |
| Formal B2 §§5.3/5.7; §8 item 10 | Both support lanes, label ordering, weak-support fallback, empty/failure difference, clean main answer and support-kind side-drawer warning; proposed T2-UNRES-SHARED | C-7N.13.10/.13.10.1–.13.10.4; existing shared uncertainty/empty/failure atoms |
| Formal B2 §§5.5/5.6; §8 items 11–13; A4 §§2–6 | Authorized-use boundary, one Decision-12 event, Decision-11 disagreements, all support labels/provenance, questions asked/dropped and response exception; four failure classes; eight-field validity | C-7N.13.11/.13.12/.13.13 and four failure atoms; prior validity/log owners |
| B4 acceptance record §7; B2 closure; four active indices | Accepted scope, corrected current-stage level wording, proposed mechanical carriage and remaining open implementation/calibration slots | READ RECORD and source dispositions; no audit workflow imported |
| Recovery ledger scoped FR rows; Bundle 3 B-AFFIRM boundary | Restoration-only navigation and distinction between reading affirmation and possibility disposition | Appendix B carry; later CH08-f ownership, no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7O; MAP C-7O; DD §3G; Companion §7O | Two result types, normal report intake/label, detected possible link and no direct system access to reality | C-7O/.1/.1.1/.1.2 and report entry/label atoms |
| V10 §7O; B4 §9.2 | All seven proposal fields and stable action identity, without final new field serialization | C-7O.2/.2.1–.2.7 |
| V10 §7O; B4 §9.2 | Confirm, reject, modify, unresolved indefinitely; separate connection-response event; no loss from three-name B8 summary | C-7O.3/.3.1–.3.4; .9.1 |
| V10 §7O | Timing/similarity prohibitions and connection-confirmation versus causal-explanation distinction | C-7O.4/.4.1–.4.3 |
| V10 §7O; B4 §9.2 | Separate action/root/connection and event/relationship/meaning; result root referenced not copied; existing five stage fields reused | C-7O.5/.5.1–.5.6; .9.3; existing C-7N.7 |
| V10 §7O; MAP C-7O/CY-E | Conditional reread/state/open-loop/other explicitly designed use; detection may be disabled/restricted | C-7O.6/.6.1–.6.4 and .7 |
| V10 §7O | Success confirmed only by Ness versus revisable apparent consistency, separate facts and no causal proof | C-7O.8.1/.8.1.1/.8.1.2 |
| V10 §7O | Partial success confirmed versus interpreted; achieved/unmet portions separate; no automatic retry | C-7O.8.2 with four children |
| V10 §7O | Failure confirmed versus interpreted; no automatic retry/resuggestion; Ness decides next | C-7O.8.3 and two branches |
| V10 §7O | Cancellation trigger, reason, action state, actual partial effects and intended effects; authorized stop types | C-7O.8.4 and five field children |
| V10 §7O | No/unknown result, exact result-unknown marker, active uncertain state/open loop, no time-only result | C-7O.8.5 and three children |
| V10 §7O; B4 §9.2 | Wrong/contested/contradicted linkage, rejected event, corrected proposal and unchanged action/root | C-7O.8.6 and two children |
| B4 §9.2; §§10/13 | Separate B8 response and assessment records; current/prospective stage carriage; before-effect non-execution versus after-possible-effect unknown/frozen/no-retry; exact preview/authority retained | C-7O.9/.10 and both crash cases; C-7N.7/.8 and existing operation atoms; full execution owner CH07-c |
| B4 §§11/12/14 | Normal source-return path; privacy/gates never evidence; A31 and evidence family; one real-operation log, domain/log levels, B8 active/cold and fourteen-field lifecycle event | C-7O.11/.12 with canonical shared owners |
| B6 mechanical §§12/13; closeout §8 Path 4 | Outcome observations only through §7E to roots/readings; no OOP live query target; absence is not confirmation; no reconstructed capture gap | C-7O.9.4 consumer boundary; full capture/schema owners CH08 |
| B-INT-8 §12C | Fresh current-use resolution for any accepted connection, append-only correction history, no new result authority | C-7O.5.3 conditional owner gate, existing C-24.14 |
| Durable kernel §§U/V.2/W/X; framework addition §§9–11 | Reference-only coordination, component identities/terminals unchanged, no completed B-CYCLE or chosen result | C-7O.13; general kernel mechanics remain outside current scope |
| B4 receipt; active indices; recovery ledger; B15/formal B2/future-search discovery | Accepted scope and remaining open slots; navigation/restoration-only or later-owner dispositions | READ RECORD and scoped dispositions, with no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH07-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 complete §7P; Companion §7P; Map C-7P; Defaults §3G | Helper/actor boundary and all nine must-never rules | C-7P root |
| V10 §7P; B4 §9.2 | Three states with distinct authority; canonical stage values reused | C-7P.1 and .1.1–.1.3; C-7N.7.1 |
| V10 §7P; B4 §9.1 | Four levels, actual present effect, separate future level and separate Level-2 log | C-7P.2/.2.1–.2.5; C-7N.7 and .12.2 |
| B4 §9.1 | Strictest rule and specialist maintenance/privacy/promotion/TSC/identity owners; permission is not evidence | C-7P.2.6/.2.7 and existing owner cards |
| V10 §7P | Standing ability and exact moment approval; silence/previous permission/preparation never consent | C-7P.3/.3.1/.3.2 |
| V10 §7P; B4 §§9.1/9.2 | Narrow recurring object, all eight explicit scope fields plus audit/notification and pause/revocation state | C-7P.4 and ten children |
| V10 §7P; B4 §9.1 | Seven heightened categories, specific per-instance confirmation, not Level 5 or universal irreversibility | C-7P.5 and seven category children |
| V10 §7P; B4 §§9.1/9.2 | Changed/ambiguous/expired/unexpected stop conditions at every layer/level; access reduction | C-7P.6 and five stop cases |
| V10 §7P | Five immediate stop-and-surface steps; full seven event groups; known/unknown/still-changing subfields | C-7P.7, .7.1–.7.5 and full .7.3 field tree |
| V10 §7P | Correction is a new action; all real-world correction examples require approval; no assumed restoration or technical-success resolution | C-7P.8/.8.1/.8.2 |
| V10 §7P; B4 §9.2 | Five linked separate objects and additional explicit corrective-execution stage | C-7P.9/.9.1–.9.3; C-7P.7.3; existing C-7O.5.1; .11.5 |
| V10 §7P | Five simultaneous emergency predicates and every prohibited completed-world reversal example | C-7P.10 and five condition cards |
| B4 §9.2 | Prepared record’s six object fields and all shared stage/level metadata | C-7P.11.1 and six fields; C-7N.7; C-7O.2.1 |
| B4 §9.2 | Exact approval binding: prepared identity, content/version, endpoint, tool, level, categories, conditions/expiry/scope, basis/time | C-7P.11.2 and nine field cards |
| B4 §9.2 | Dated attempt under one Action ID, bound authorization and exact preview; attempt is not effect | C-7P.11.3/.11.3.1; existing Action ID and preview/authorization owners |
| B4 §9.2 | Actual authorized outside effect only, post-record of change/time/channel/authority/preview; corrective execution distinct | C-7P.11.4 and three field cards; .11.5; shared stage/identity/preview/authority |
| B4 §9.2; V10 §7P | Dated emergency record: conditions met, what stopped, what not reversed and date | C-7P.11.6 and four children |
| B4 §9.2 | Stable chain identity, no double execution, live authority, exact preview and all six invalidating changes | C-7P.12.1–.12.4 |
| B4 §§9.2/13; V10 §7O | Mandatory post-record, honest partial changed/unchanged effects, frozen unknown/no retry, cancellation, both crash positions | C-7P.12.5–.12.8; existing C-7O.10.1.1/.10.1.2 and .8.4 |
| B4 §13 | Operation ID/key, atomic record commit, no duplicate outcome, startup recovery, missing-record reconciliation, partial/technical retry/stage integrity | C-7P.13.1; shared C-7M.5.2, C-7N.11.1–.11.7 and C-7H.9/.10 |
| B4 §14; restored Group 10 operational-record laws | One operation/log, complete content/use/non-use, domain/log levels, honest stage, evidence family and three record kinds | C-7P.13.2; existing C-7B.10.2/.10.3 and Bundle 4 owners |
| B4 §14 | Initial active, five protections, owned cooling rule, two cooling conditions, actual-use/link reactivation, failure preserves prior status, fourteen-field event | C-7P.13.3 with existing C-7N.12.3/.12.3.2 and C-7M.11.4/.11.5 |
| B4 §§11/12/14 | Purpose-specific privacy, §7Q then SACL, protected/TSC/compartment/influence restrictions, no circular/double support | C-7P.13.4 with canonical A31/evidence-family and privacy owners |
| B6 mechanical complete §12 | Protected minimum-metadata §7P query obtains authority decision, no recursion/no early payload release | C-7P.14.1; full query mechanics CH08-c |
| B-INT-8 §5C/§7C/I5 | Existing exact narrow rule and authority provenance; CCR cannot create/widen rule | C-7P.14.2; existing C-24.4.3/.9.3 |
| AIC §15; kernel §§U/V.2/W | Recorded-state and reference-only coordination never own action authority | C-7P.14.3; existing C-7O.13 |
| A19 room-start §6; A22 §5 | Narrow room-start confirmation scope; full five-condition phone emergency boundary | C-7P.14.4/.14.5; full room and phone owners later |
| Accepted package/active candidate/decision discovery | Owner-preserving boundaries, navigation, restoration tracking and deliberately deferred detailed scopes | Scope dispositions and READ RECORD; no historical behavior imported |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-a

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 complete §7Q; complete Companion §7Q; Defaults §3G; Map C-7Q | Root all-stage authority and prohibitions; .1 six distinct operations, with two protection levels under sealed isolation; .2 four sensitivity categories; .3 dependency/location discovery, indirect traces, multi-root rebuilding, indexes/backups, five honest outcomes, six noncomplete-report facts, five-field history and unresolved-case block; .4 core/configurable capture exclusion, safe/unsafe separation and exclusion event; .5 third-party baseline, contextual factors, stricter controls, four-operation permission ladder, hypothetical simulation, stronger minor/vulnerable defaults and import/public limits; .6 visible eligibility, final review, mouth limitation, protective ambiguity, safe failure, minimum material, all surfaces and the privacy-decision record. | C-7Q source-ordered tree and the scope dispositions above |
| A7 full primary and full closure receipt | .7 natural-language pause/reopening, one-short-question ambiguity rule, actual-words scope, independent visible/internal controls and truthful transformation. .5 preserves compatible interpretation labels, full/detailed simulation scope and prior approval, normal longitudinal use without a new volume threshold; .6 preserves private/default and explanation-without-disclosure. No mandatory command language or implementation policy invented. | C-7Q source-ordered tree and the scope dispositions above |
| B7 full primary and full closure receipt; Bundle 5 §§3/4/5/8 scoped | .8 all thirteen proposed mechanisms: PIP, PDE, PEB, SPS, XDS, MCS, VRE, DDE, VER, BVH, IRR, PGC, PIS, plus their common enforcement-contract layer. Names remain proposed on every mention. PIP normalization vocabulary and six steps; PDE ordering/inputs; PEB minimum output; SPS identity/protection/inert credentials; detector registry and method versions; mixed capture; discovery adapters and coverage; independent verification; backup modes/restore replay; complete influence lifecycle; stricter-only person/group configuration and inspection. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §14 complete | .9 common record identity/schema/operation/time/protection/append-history discipline and all twenty-six schemas, with fields recursed. The already introduced .4.4 exclusion event and .6.9 privacy-decision record retain their first identities; §14's corresponding rows extend those records rather than duplicate them. History at .3.7 is reused by deletion_case. Record-specific identities remain distinct; references do not copy private content. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §15 complete, including bold §§15.0–15.9 | .10 shared atomic/idempotent/restart/logging/B9 spine, then nine contracts in source order: topic pause, exclusion, sealed isolation, hiding, restriction, redaction, deletion, influence removal and restoration/supersession. Preserve request/result, operation identity, key, scope, every state/transition, terminal versus protective status, checkpoint, partial recovery, retryable/terminal failure, derivative handling, verification and restoration. Six sealed-transfer steps preserve raw content before removing ordinary exposure. All thirteen hiding surfaces and ten restriction elements are explicit. | C-7Q source-ordered tree and the scope dispositions above |
| B7 §16; A26 complete §§2–4; B-INT-5 complete §§3/4/12A/12B/13 | .11 owner-preserving interfaces: all front doors; retrieval/relevance; engine/derived stores; simulations; output; TSC; backup; independently established private-mode/access facts. A26 defaults are consumed only inside the established private context. Full factor verification, mode-session/fence schemas and identity/access mechanics remain CH09-i, CH09-c/d/e. | C-7Q source-ordered tree and the scope dispositions above |
| B-INT-6 complete §§3/4/5/6B/6D/6E/7A/7B/8/13/14/15/16 | .11 exact privacy-owned payload binding, transformation loop, immediate revalidation/restriction, two stream alternatives and no-signal output. Full proposed ODC identity, claim/dispatch/attempt/receipt records, state/recovery machinery and output-channel contract remain CH09-d; CH11 assembles the whole path. Privacy never owns SACL or delivery reality. | C-7Q source-ordered tree and the scope dispositions above |
| A2 complete §5A.2/§9; prior canonical C-READ.10.11 | .11 governance discovery must find manifests, partial/blocked/integrity-failed cards, checkpoints and indexes independently of semantic eligibility. Reuse C-READ.10.11; do not make discovery semantic evidence. Protection inheritance and side-channel limits apply. | C-7Q source-ordered tree and the scope dispositions above |
| A4 complete §4; retained formal Bundle 2 and B1 scope; B6 mechanical complete §12 | .11 privacy precedes relevance, router does not re-evaluate privacy, protected minimum-metadata authorization query obtains its own decision without recursion. Full LMAC contracts are CH08-c; relevance CH08-b. | C-7Q source-ordered tree and the scope dispositions above |
| B15 complete §4; retained B-INT-4/TSC source readings; B-INT-8 whole reading retained | TSC only stores safe structural references after exclusion; no inspection/authorization token opens L1 content. Connection current-use authorization stays distinct from original acceptance, with no repeated endorsement or authority creation. Existing C-TSC/C-24 owners are reused. Full identity/token wiring remains CH09 and CH11. | C-7Q source-ordered tree and the scope dispositions above |
| B9, B10, B-HOLD, B11, B16, B24 and evaluation-evidence bridge; prior complete owner readings | Existing operation/retry/hold/promotion/model-boundary owners remain canonical. A privacy refusal is not retryable around the gate; a genuinely changed recorded authorization permits a new admission. No model validation, stored status, log or durable coordination record grants access. | C-7Q source-ordered tree and the scope dispositions above |
| AIC complete §15; durable kernel retained owner/fence sections | .11 recorded permission is descriptive; gate ownership and owner-prescribed fences remain external to coordination. No invented control-plane/kernel part identity; their full packages remain later placement. | C-7Q source-ordered tree and the scope dispositions above |
| B6 policy A30 complete; B6 mechanical §11 privacy stage; CH04-e C-9A.7.1.4 | Carry the existing marked minor-default conflict consistently; deferred WhatsApp path gains no runtime ingest authority. Full deferred intake is already CH04-e. Observation/acoustic and reaction details remain CH08-d/e/f/g. | C-7Q source-ordered tree and the scope dispositions above |
| A17, A19 room/chat/world, A22, framework additions, future-feature/dual-model/candor source topic matches | Preserve already established privacy ownership; rooms, tools, outward transfer, private surfaces and provider changes cannot grant authorization. Detailed interface/world/model/phone/future-tool bodies remain their named CH09/CH10/CH11 owners. Inactive sources remain named intents only. No historical narrative imported. | C-7Q source-ordered tree and the scope dispositions above |
| Sept25 buckets record §4 Group 11 and §6 FR-0108; authorized historical preservation file F9, read whole | .12 explicit influence-removal instruction requires scope, affected components and start time. DECIDED-2026-09-25; only this restored passage supplies behavior from the historical file. Its full pinned blob was verified before reading. No other archive catalogue content imported. | C-7Q source-ordered tree and the scope dispositions above |
| Four active indices NHD-M7Q/NHD-A7/NHD-B7/NHD-BU5 rows; recovery ledger title/status tracking | Navigation and Appendix B only. The ledger supplies no behavior. Earlier versions of packages remain superseded where accepted highest versions exist. | C-7Q source-ordered tree and the scope dispositions above |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-b

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §7R introduction and external prerequisite; A4 §4 | C-7R root: purpose-only judgment; no truth/strength/causation/authority/permission, merging, clash resolution, rewriting/reordering/suppression, privacy ownership, state writing or purpose guessing. Prior purpose-specific C-7Q authorization; held-material boundary retained. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 1 | .1: two-layer object; categorical deterministic gate excludes without grading; named value/source/method dimensions only after passing, no hidden aggregate. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 2 | .2: producer per dimension; reproducible deterministic structural/temporal/currency/count, all-MiniLM-L6-v2 semantic/thematic, declaration-limited dolphin-llama3 interpretive role; no per-call approval/self-approval; producer/version/index/prompt/value provenance. Final mouth selection remains open in accepted B2. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 3 | .3: on-demand default; optional latency-specific precomputation, no global relevance; seven field groups; exact context/validity reuse; six invalidation classes; mouth precomputation requires declaration plus independently designed validation. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 4 | .4: Tier 1 owner/validation and ten minimum declaration groups; Tier 2 consumer-local thresholds/order/weights/fallback/surfacing/unresolved fields as needed, versioned additions; no cross-tier ownership. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 5 | .5: unrestricted Ness inspection under existing record protection; direct correction, context override, consequence preview plus confirmation and new version; no veto; invalid-configuration exact-conflict explanation and preserved request; append-only all objects. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 6 | .6: six deterministic checks; Validated/Failed/Unresolved and exact meanings; optional declared validator model/config/reason/independence/provenance/disagreement handling; no model final authority or mouth gate. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 7 | .7: four exact gate names; nine exact dimensions; all link-entry fields and five explicit-link types; Ness-response entry fields; clash entry fields. Existing C-7D.10 owns six currentness statuses; C-7G owns acceptance/context status. Channel identity stays mandatory retrieval provenance. Local/shared extension path. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 8; B2 §10; B4 §5 | .8: own relevance record space; state review requires state-owned authorization; event is a trigger possibility not evidence; independent evidence, separate Ness response, relevance/currentness separation and exact forbidden feedback chain. Exact trigger authorization remains open. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 9 | .9: required controlled type and optional inert string label; all five purpose values and meanings; new type requires confirmation/versioning, new label does not. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 10 | .10: conditional Tier-2 rule identifier/version reference; present/nonempty/current validation only; consumer owns content; changed Tier 2 requires updated Tier 1 reference; no obligation for mouth-free mode. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 11 | .11: disagreement record and nine field groups, exact producer/validator pointers, three starting conflict types plus declared extension, producer model/prompt/config, validator identity/version/independence, uncertainty-rule reference, resulting state and timestamp; no copied interpretive body. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 12 | .12: completed evaluation event, all thirteen field groups; five separate candidate summary counts; conditional trigger, one pointer per judgment, disagreement flag/pointers, completion time; no event for unrun evaluation. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 13 | .13: three simultaneous pattern predicates; exact observed pattern and optional mode change, no recommendation; corrections may be contextual; open until explicit action/dismissal; dismissal suppresses unchanged pattern until new overrides/material change; no automatic configuration change. | C-7R source-ordered tree and the explicit scope dispositions |
| V10 §7R Decision 14 | .14: immediate halt, no gate/dimension/completion event; exact unknown value/vocabulary version, preserved original full configuration/context, plain explanation; confirmed mapping or versioned new type; close match not authority; separate halt event unknown/request/time. | C-7R source-ordered tree and the explicit scope dispositions |
| A4 §§1–5; B2 §§4/5 | .15: Option C shared language plus mandatory versioned declarations, all eight policy fields, invalid/missing declaration no mode; honest owner-specific stop/degraded handling; genuine empty vs system failure; no hidden relevance dialect or per-judgment clerk work. | C-7R source-ordered tree and the explicit scope dispositions |
| B2 complete §§5–10 | .16: accepted five declarations; all on demand, no precomputation, explicit mouth none, six vs nine dimension applicability, controlled purposes and canonical consumer owner references; proposed names always qualified. Proposed T2-UNRES-SHARED reuses C-7F.6.10.5 and its children, no second shared rule. Future mouth mode requires version/change/validation, not mandatory second AI. | C-7R source-ordered tree and the explicit scope dispositions |
| B2 §§5.6/5.7/11/12; B1 §5; A4 §§4/5 | .16: one-operation/one-log, evaluation/disagreement/declaration history, ordinary inspection not approval queue; B26 failure after bounded B9 stops and preserves unfinished work, no degraded continuation; genuine empty alone permits honest bare context; numeric empirical values, provider/validator choices/serialization/UI and full-cycle wiring remain open. | C-7R source-ordered tree and the explicit scope dispositions |
| B6 mechanical §12 | .17: exact relevance query Tier-1 mode id/version + purpose + candidates; uniform requester/targets/config; obtained purpose-correct privacy and authority decisions before route; own whole provenance-bearing result; router never owns rules, processors not direct targets; query identity/retry belongs CH08-c. | C-7R source-ordered tree and the explicit scope dispositions |
| Earlier delivered pieces | 37 incoming uses, one place each; C-7B.7 old USED BY root stamp is wrong and remains carried. CH02 C-7B.9.9 and .9.9.1 also incorrectly stamp C-7R ACCEPTED; add fix note, no old-byte edit. C-7R root DESIGNED. Existing root-name discrepancy, proposed qualifiers and all other earlier defects remain carried. | C-7R source-ordered tree and the explicit scope dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-c

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §26.2/§26.3/§26.5; Map C-LMAC | Root, .1–.5: whole-mechanism connection before/during/after, single interface for every call, initial relevance-guided query is first not only, no data/copy/cache/accumulated model, current-state responses including mid-pass changes, permission-preserving full reach, no filtering/relevance/privacy ownership/reduced output/caller decision. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §26.5; B6 mechanical §12 | .3 target interfaces: §7F, §7R, §7D, §7L, §7K, §7J, §7Q, §7P, §22; each exact request/result, own provenance. BOP-produced roots and pattern readings in shared memory are material reached through retrieval/relevance, not direct BOP/OOP queries. Wellbeing tier solely response calculation, never identity/access. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §26.7 | .6: response-time current behavioral readings, state/open-loop/capacity picture, wellbeing tier, authority, privacy, voice/text mode; caller computes actual response with confidence/firmness and whole picture, no stored RBCS. Exact mode-state query transport beyond the listed nine component contracts remains open. Full adaptation CH08-g. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §12 | .7 uniform request: requester, declared purpose, targets, applicable mode/configuration version; whole live result with own provenance. .8 protected Q/P control queries obtain decisions without recursive prerequisite; only minimum requester/purpose/target metadata, no protected payload before return; identity/access/purpose/logging still bind; ordinary queries apply obtained results in order. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §§3/12 | .9 query identity/log: proposed query_operation_id, one logical query/one shared routing record, five routing fields requester/target/purpose/Q authorization kind/outcome ref; transport retries reuse identity, append child details, exactly one terminal parent, new intent/context gets new identity. .10 recovery/technical retry/refusals: no private state recovery; complete interrupted terminal idempotently; component owns recovery; unknown/unauthorized purpose refused and recorded; shared B9 values reused, no semantic interpretation retry invented. | C-LMAC source-ordered tree and explicit owner dispositions |
| B6 mechanical §3/§14; V10 §0B | .11 atomic operation records, structural duplicate prevention, committed checkpoint recovery, partial completion, protective uncertainty, one-log/never log-about-logging/no log as evidence, Q/identity protection; no root-ingest mechanism invented for stateless routing. Existing operation/log/B9 owners reused. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §25.4; B24 §6.5; B-INT-6 §§4/10/11/12/14 | .12 output retrieval: SACL level/categories before retrieval, intersection with Q eligibility; generator never receives out-of-scope content or leaks its existence. SACL owns refreshed PBR cache, LMAC keeps none. proposed retrieval_intersection_record stays output-coordinator-owned and references eligibility, scope, admitted identities only. Owner current facts/epochs never restored from history; dead-epoch candidates cannot form output. Cannot honor intersection → halt/withhold. Full output fence/dispatch/delivery lifecycle CH09. | C-LMAC source-ordered tree and explicit owner dispositions |
| V10 §0B/§7G-A/§7E-TSC; B6 closeout §9; B15 §11; A16 §5; A2 §§5A.1/9; B16 §7 | .13 use boundaries: active pre-ingest/TSC blockers, safe metadata-only held references, B-HOLD no new downstream use, quarantine promotion trail, no ordinary TSC archive access or inspection, no prepared/uncommitted telling as semantic context, provisional creation status carried visibly and in canonical provisional_material_used. Sealed WhatsApp archive remains inaccessible; no decryption/promotion path created. | C-LMAC source-ordered tree and explicit owner dispositions |
| B-INT-8 §13A/I7; A25→B10 §7; kernel §V/§W | .14 owner-preserving interfaces: fresh connection current-use resolution per use and current applicable version; reread Q→F→R order regardless assignment, no narrowed context; kernel reference-only carrier cannot create parallel routing or gates. Existing C-24 and C-7H owners retain full mechanics. | C-LMAC source-ordered tree and explicit owner dispositions |
| Earlier chapters | 19 incoming relationship occurrences at 16 places, all to reciprocate one place per row. Five earlier USED BY references to this root require explicit consumption of C-7J/C-7K/C-7L.9/C-7L.13/C-7P. Do not edit earlier bytes. CH08-b root Changes cites V10 §7R for a whole-result LMAC handoff that requires B6 §12 (or V10 §26.5); carry this citation addition for the fix round and use the correct source now. | C-LMAC source-ordered tree and explicit owner dispositions |
| Discovery and status | Four index rows NHD-M26/BU6P/BU6M/BU6. B6 old open wording does not reopen accepted B7/B15/B-INT-8/B26. Final closeout receipt retains its own audit condition; accepted mechanical package is independently closed. Framework/kernel retain owners; inactive memory-fabric contributes intent only. No historical behavior imported or source pin changed. | C-LMAC source-ordered tree and explicit owner dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-d

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §25.1/26.4, Map C-BOP | Root and .1 authorization/classification: directly physical only, all authorized session signals, four source classes, confirmed sent text only; no interpretation/private store/model; OOP owns TTS stop, BOP records timestamp/position. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 event vocabulary | .2 all 22 event values in source order, their decided measurement/payload fields and exact no-interpretation limits; extended registered before first use. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 root/payload/capture identity | .3 seven BOP-specific root bindings, .4 all 19 payload fields/nested authorization/modes/methods, .5 six-input stable capture hash and durable sequence before writes. Reuse built root schema owner without claiming BOP built. participant_record and anchor_record internals genuinely unspecified. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §25.1 quality/third party/simultaneous/reconnect/DUMB/recovery | .6 quality and completeness fields/values; .7 all four third-party fields and three handling values; .8 reconstructible one-root-per-channel bundle; .9 optional anchors and ordinary later reread/retrieval; .10 complete DUMB/typing boundary; .11 failure/retry/crash. Below-threshold quality is not an authorization waiver and B11 never writes the old sealed batch. | C-BOP source-ordered tree and explicit boundary dispositions |
| A15 v1.1 §§2–6 and receipt §§3–7 | .12 optional six-field/five-name acoustic notes, scoped certainty, full provenance, downstream physical context permitted but never sufficient alone, no capture widening/schema activation; empirical choices open. Later receipt explicitly settles policy acceptance while old V10/Bundle 6 pending wording remains historical status, not active-schema authority. | C-BOP source-ordered tree and explicit boundary dispositions |
| B6 mechanical §§3/13 | .13 only Catalog→append_root/B11→reading route, atomic record/identity/commit/retry/partial recovery, held boundaries and privacy; existing B11/B9 owners reused. | C-BOP source-ordered tree and explicit boundary dispositions |
| B6 policy A12 and mechanical §13 | .14 imported-item reaction operation: exact start and four first-ending events, active/paused/post-playback segments, finite pause/post bounds, no overlap/one item/one segment, proposed reaction_window_id, duplicate opens, committed-state interruption recovery, no guessed links, capture-child link commit and exactly one parent terminal. Full raw-only facts retained; never merged/causal inference. | C-BOP source-ordered tree and explicit boundary dispositions |
| V10 §§25.6/25.11/25.12, B-INT-7 §§7/10/16/19 | .15 enrollment/biometric interfaces: B29 microphone, BOP observations; enrollment provenance not identity; BAI command seven result forms, safe two-field content; session-open single success command deterministic identity; raw voice protected, frozen set after close, capture ID end-to-end, rejected profile segments still preserved. Full enrollment process CH09. | C-BOP source-ordered tree and explicit boundary dispositions |
| Map C-BOP, V10 §0B | .16 shared logging, one operation/one record, honest failure gaps, access protection; no logs as evidence. | C-BOP source-ordered tree and explicit boundary dispositions |
| Companion BOP Third-Party Flag | Unqualified pre-output-review wording conflicts with V10's purpose-specific internal/visible authorization. Mark in header and affected gate; V10 governs. | C-BOP source-ordered tree and explicit boundary dispositions |
| Earlier chapters | Four incoming places C-7E/C-TSC/C-TSC.9/C-TSC.13.1 reciprocated separately. C-7E stamps the BOP root ACCEPTED; root is DESIGNED under contract §3, accepted wiring separately stamped. Carry earlier status fix without changing bytes. | C-BOP source-ordered tree and explicit boundary dispositions |
| Discovery | Index NHD-M25/M25-BOP-VI/A15/BU6P/BU6M navigation only. Bundle 5 A15 ownership and B6 closeout BOP row preserve owners and status. Inactive Voice/Delivery Director remains INTENT only. Defaults has no BOP-specific match. No archive behavior imported. | C-BOP source-ordered tree and explicit boundary dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-e

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §26.6 | Root and .1 definition/no owned data; .2 seven observed signal categories in source order; correction physical timing/relationship versus separate conversational content; follow-up relation mechanism genuinely unspecified, not an invented meaning classifier. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 absence discipline | .3 silence only when BOTH expected signal and observation conditions held; absence recorded as absence, never satisfaction/acceptance. No response may reflect no notice, other activity or session ending; no cause inferred. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 connectivity/routes | .4 source type outcome_observation via Catalog/engine/shared-store; .5 readings available to live query, reread, clash, state review, wellbeing tagging. Contradiction preserves original and new reading beside it. No direct configuration/rule/output route. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.6 self-improvement; §26.12 | .6 proposals through Meaning Engine/shared reading/Computed View/authority before change; all automatic changes logged/explainable/evidence-traceable/reversible; explicit protected-core approval. Full learning/threshold mechanics CH08-g. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| V10 §26.4; Map C-OOP/B29/voice-priority chain | .7 immediate TTS stop when Ness begins speaking during voice-mode function execution; BOP records timestamp and stream position. Stop control is distinct from prohibited outcome-to-behavior routing. No pipeline latency/buffering/remainder policy invented. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| B6 mechanical §§3/12/13; closeout §8 OOP row | .8 accepted one-path/no-live-query, stable capture identity, durable sequence before write, atomic state/record, per-item promotion, duplicate structural prevention, retry under existing B9, honest gaps/crash recovery, protective hold/privacy/writer and one-operation-one-log. Reuse exact B11/B9 owners. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| B6 A10/A12 and B-INT-3 | .9 existing authorized-session and imported-reaction interfaces consume C-BOP.1.1 and C-BOP.14 complete mechanics; do not duplicate a reaction window or treat it as the generic post-function window. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Map C-OOP; V10 §0B | .10 log actual post-action signal, named absence and routes to reread/clash/wellbeing; protected access, no recursive logs or evidence-weight inflation. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Earlier chapters | Three incoming places: C-7E, C-7O.9.4, C-BOP.2.6. C-7E stamps the OOP root ACCEPTED; carry fix because root remains DESIGNED, accepted mechanical scope has separate cards. Earlier action-result owner stays separate. | C-OOP source-ordered tree and explicit gap/owner dispositions |
| Discovery/status | Index M26/voice-priority/BU6 rows navigation only. Companion/Defaults have no OOP-specific match. Inactive Voice/Delivery Director is intent only. Overbroad discovery returned ledger quotation rows; they supply no behavior and no whole-read credit, and no archive was opened. | C-OOP source-ordered tree and explicit gap/owner dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.


### Source placements carried from CH08-f

| Source scope | Rules, records, fields or events | Placement |
|---|---|---|
| V10 §§0/7A/11 item23; Map C-AFFIRM | DESIGNED root: record occurrence of specific-reading accept/reject, dated and weightless in Story Layer; truth judgment stays outside engine; never block, rewrite or supply confidence/evidence/authority. Reuse C-7A.14.3 and current-use separation. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 | .1 accepted record with six fields: target reading ID(s), response accept/reject, timestamp, Ness initiator, explicit weightless marker, stable event ID. Target can plural only when one response addresses those specific readings. No invented snake_case schema fields/types. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 | .2 same response duplicate→one event/one log; .3 no response means/moves/stalls nothing, never consent or engine gate; .4 no changed reading/root/confidence/evidence/firmness/truth, rejection not opposite proof. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17 with §§13/15 | .5 only permitted presentation/current-use effects: dismissal can stop resurfacing unless valid new trigger; existing view grouping/labels owners reused; history remains. Exact new-trigger mechanics not invented. .6 changed judgment appends beside old. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §17; existing C-7J.7.3 | Root consumes canonical separate clash-response/affirmation linkage; no duplicate atom. .7 excludes general telling responses, theme actions, Person-Box events, clash responses and action dispositions, names actual owners; no widened generic feedback bus. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Bundle3 §§18/19/20; V10 §0B | .8 append-only protected living record, no recursive logging or second evidence vote, exact privacy/identity/access boundaries; no silent operation, no event as authority. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| W1 CH04-a carry; Bundle6 §13; Bundle3 §17 | .9 boundary consuming complete C-BOP.14 reaction operation and C-OOP.3 absence discipline: raw physical/link facts are not accept/reject responses. Reaction mechanics remain canonical in CH08-d, not duplicated inside AFFIRM. Writing1’s CH08-d/f carry-forward is satisfied by full d placement plus f’s narrow seam boundary. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Prior incoming C-7D; Bundle4 §§11/12 | Root reciprocal carries occurrence pointer only, never state support from accept/reject or its log. Prior C-7D generic Ness-response reference to AFFIRM needs qualification/correction: affirmative occurrence is not a general state self-report. Record fix without changing earlier bytes. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Existing cross-links | Three incoming places C-7J.7.3, C-7I.4.1, C-7D; one prior USED BY commitment C-7J.7.3 to root consumed. All individual rows. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |
| Discovery | NHD-M11-23/BU3 navigation. Companion item23/current rule list match scope; Defaults off-board principle only. Other accepted packages use generic response references, not new AFFIRM mechanics. No ledger behavior or archive used. | C-AFFIRM source-ordered tree and explicit owner/gap dispositions |

The preceding inventory is carried from the previous delivered piece. The source-to-card table above adds the current placements; its scope does not claim full placement of other components in a shared package.

### Source placements added by CH09-a

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.5: SIA responsibility | C-WIS-SEP.1; identity/audio assessment only; no mental or physical diagnosis |
| V10 §25.5: wellbeing responsibility; §22 tiers | C-WIS-SEP.2 and .2.1–.2.5; own baseline, sustained multi-session divergence, four tier consequences, ordinary availability |
| V10 §25.5: SACL responsibility | C-WIS-SEP.3; current identity/security evidence, no wellbeing tier, no acoustic inference from behavioral divergence |
| V10 §25.5: appointment records | C-WIS-SEP.4; calibration and freeze-unlock only; all three forbidden purposes |
| V10 §25.5: temporary divergence; §25.4 Option A | C-WIS-SEP.5; all listed temporary causes, imitation_risk, top_security block, recognized_ness retained; Gate-2 wording conflict marked |
| V10 §25.5: acoustic spoofing | C-WIS-SEP.6; anti_spoofing_assessment, medium/high suspicion_level, guest, relock, private alert, wellbeing uninvolved |
| V10 §25.5: two paths | C-WIS-SEP.7; no merging or conflation |
| MAP C-WIS-SEP | Root and .9; no independent I/O, named consumers, CY-H/CY-I, actual result and producing mechanism, violations, append-only records, no mandatory negative-attestation field |
| A26 §§4.4–4.6; B-INT-5 §§4/8; Bundle 6 mechanical §12 | C-WIS-SEP.8; response-only wellbeing, independent mode/access conditions, ordinary Personal Mode availability, identity-loss output stop. Full mode contracts left to CH09-i; shared query schema remains C-LMAC.3.9 in CH08-c |
| V10 §§26.6/26.11/26.12 | Existing C-OOP.5.5, C-LEARN.8.3 and C-LEARN.9.3 receive reciprocal rows in this root; no repeated learning mechanism |
| COMP §5 / Wellbeing / Identity / Security Separation Rules | Corroborates V10's complete separation section; no additional mechanism or conflict |
| B-INT-4 §7 C2; B-INT-7 source boundary | Identity confirmation is not wellbeing calibration; existing cache owner is CH04-b. Full enrollment mechanics left to CH09-h |
| V10 §25.4 remainder; §25.6; §22 remainder | Full access calculations left to CH09-d, biometric artifacts to CH09-e, calibration/unlock procedure to CH10-c. Only their separation boundaries are placed here |
| DD/CR; DR and active/accepted discovery | No additional separation mechanism imported. DD/CR workflow excluded. Ledger is navigation/Appendix B only; no restored behavior is sourced here |

### Source placements added by CH09-b

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.2 / Core Principle and Protected Rules | C-OTHER root, .1/.2/.3/.4/.5/.8: complete internal mechanism; independent disclosure; privacy and authority; no permission transfer, hidden disclosure, guest private memory, other-speaker changes or protected-core override; claims retain speakers |
| V10 §25.2 / Access Levels | C-OTHER.3 and .3.1–.3.4 carry all four values and this section's conditions. Full Gate 0–3 predicates and assessment records remain CH09-c/d |
| V10 §25.2 / Guest Mode | C-OTHER.4: general response, no Ness-personal shared-store material, no hidden-information acknowledgment |
| V10 §25.2 / Known-Person Permissions | C-OTHER.5: maintenance authority, expressed boundaries and learned evidence, all seven initial category names and open vocabulary. Canonical category field remains C-7L.9.1; PBR read interface remains C-7L.9 |
| V10 §25.2 / Separate Parent Identities | C-OTHER.6: all six independently held identity/context kinds; reuses C-7L.9.4 |
| V10 §25.2 / Parent Translation | C-OTHER.7 and .7.1–.7.5: request requirement; each of the three requests and recipients; uncertainty; no autonomous intervention; scoped adaptation; stored revisable output; authorized private context versus PBR-bounded disclosure |
| V10 §25.2 / Statements About Ness; §7H immutable reread result | C-OTHER.8 and .7.4: TSC → root → reading speaker continuity; later evidence may trigger reread; original records never changed. Full reread mechanics remain CH05-d |
| V10 §25.2 / Person-Box Visibility | C-OTHER.9: every prohibited inspection category, stored-extent and recognition secrecy. Canonical owner C-7L.9.3 |
| V10 §25.2 / Temporary Session Cache | C-OTHER.10: blocker, complete meaningful context, all session states, normal/crash distinction, indefinite waiting, no automatic transitions, separate permanent-seal authorization, no deleted state. Atomic state/transition owners remain C-TSC.12 and descendants in CH04-b |
| V10 §25.2 / Fingerprint-Authorized Batch Promotion | C-OTHER.11 and .11.1–.11.3: later thumbprint, complete relevant session as unit, unrelated caches excluded, remaining blockers respected, no second manual approval, attributed downstream route with both Map conflicts marked |
| V10 §25.2 / Continuous Speaker Security; §25.4 calculation/failure boundaries | C-OTHER.12 and .12.1–.12.3: continuous assessment, immediate recalculation, uncertainty, restart and stale/failure outcomes, medium/high versus spoofing_suspected flag, separate alert rule, imitation_risk not Gate 0, no routine voice challenge. Full failure/recovery objects remain CH09-d |
| B-INT-6 §§3/4/13; §6D consumer gate loop; §14 blocking boundary | C-OTHER.13 and .13.1–.13.3: privacy before relevance, final privacy then access, same answer on both gates, transformed answer rechecked, shared minimum, private owner-confirmed path, PBR/presence at output, no hidden material or mouth-refusal policy inference. Full coordinator identity, payload, fence, claim, dispatch, channel and recovery atoms remain CH09-d, with existing privacy atoms at C-7Q.11.3 |
| MAP C-OTHER / Logging | C-OTHER.14: every listed access/disclosure/PBR/translation/attribution operation is recorded under component privacy/security rules; no invented event names or record schema |
| A7 §§3/4.4–4.10/6; B7 §3 and §17; V10 §7Q | Existing C-7Q.5 and descendants remain canonical. Translation uses their privacy boundary. Stronger-authorization and minor/vulnerable-default conflicts retained consistently with CH08-a; no new simulation or fixed-profile mechanism |
| B-INT-4 §7 C1–C3; B-INT-5 §§4/8 | Existing session-specific token/receipt/recognition and promotion owners remain CH04-b; mode intersection/reduction belongs CH09-i. A fingerprint does not silently remove those canonical owner requirements |
| B-INT-8 §15; A22 §3 speaker attribution; B-INT-7 source boundary | No connection gives access or lets another speaker accept as Ness; complete connection operation remains CH06-g. Phone-specific intake/door policy remains CH10-d, retaining the same source attribution. Enrollment remains CH09-h |
| Bundle 5 §5 Path 9 and §8 frozen wording; COMP embedded §2 | Bundle 5 confirms the shared third-party scope and preserves its differing authority explanation; not substituted for V10. Companion full other-speaker section corroborates rules; its shorter lifecycle omits later states supplied by V10, with no alternate transition invented |
| Source discovery and receipts | Searches by C-OTHER, full other-speaker/guest/known-person name, PBR/category vocabulary, parent translation and third-party interpretation/simulation identify the packages above. No restored behavior or ledger behavior is imported. B-INT-6 receipt supplies acceptance evidence only; its remaining formal-closeout audit condition is not claimed complete |

### Source placements added by CH09-c

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 complete §25.3; MAP complete C-SIA | C-SIA root and .1–.19: complete SIA records, fields, values, cadence, identity/acoustic separation, profiles, eligibility, protection, responses, linking and compact representation. Source map fixed before drafting; no numerical threshold or algorithm added. |
| V10 §25.3 / Speaker Session State (SSS) | C-SIA.2 and .2.1–.2.7: all seven fields, exact modes/biometric values, list shape, addressed stream, timestamp/null, append-only in-session history and restart loss. |
| V10 §25.3 / Voice Stream Record | C-SIA.3 and .3.1–.3.7: all seven fields, onset root, separate identity/acoustic objects, three activity values, last timestamp and trigger. No unsupported transitions added. |
| V10 §25.3 / Speaker Assessment Object | C-SIA.4 with five outer fields; .4.1/.4.1.1 ranked candidate record, all five candidate fields, seven separate evidence dimensions; both certainty ranges, all profile values, full active-flag vocabulary and all null/separation conditions. |
| V10 §25.3 / Anti-Spoofing Assessment Object | C-SIA.5 and .5.1–.5.4: four fields, four suspicion levels, five exact acoustic bases, source reading IDs and certainty; all excluded conversational/behavioral categories retained. |
| V10 §25.3 / SIA Output Interface and Assessment Update Cadence | C-SIA.6 and three field cards; four audit-only confidence labels with no decision-input use. C-SIA.7 and eight trigger cards preserve exact trigger names and empirical window-size boundary. |
| V10 §25.3 / Diarization, Voice Profile Architecture, Natural Voice Variation | C-SIA.8/.9/.10: independent parallel streams and candidates, shared technical comparison space but independent identity authority, profile range across four named condition kinds and combined-certainty behavior. |
| A15 policy §§2–5/7 and receipt | C-SIA.10.1 consumes all six fields and five names while C-BOP.12 and descendants remain canonical record owners. All ten forbidden stand-alone conclusions, bounded context, full provenance, physical-only certainty and no-recording-authority boundary retained. V10 proposal/accepted status conflict marked. |
| V10 §25.3 / Training Eligibility Rules | C-SIA.11 and six condition cards: all six ordinary eligibility requirements, exact training_eligibility_threshold name, capture-time evidence, no appointment training and no intake/meaning bypass. |
| V10 §25.3 / The 6–10 Month Learning Period and Raw Voice Data Protection | C-SIA.12/.13: conservative thresholds, provisional ceiling, comparative weighting and gradual reduction; Layer 3 storage, protected readings, minimum access and biometric-verified Full Mode tunnel. |
| V10 §25.3 / Identity Uncertain vs. Spoofing Suspected, False Lockout Recovery, Settled Rules | C-SIA.14 plus three response cards and .15: separate uncertainty/low/medium-high responses, natural recovery, no routine challenge, silent medium/high guest/relock/private alert, independent biometric+recognition+no-spoofing requirements. Full access gates remain CH09-d. |
| V10 §25.3 / Multi-Speaker State | C-SIA.16 preserves stream set and addressed stream; SACL owns per-stream access and shared minimum. Full channel/delivery mechanics remain CH09-d and mode references CH09-i. |
| V10 §25.3 / Minimum Evidence for Person-Box Linking and Compact Profile Representation | C-SIA.17 reuses all six C-7L.10.1–.10.6 atoms without duplicating their identities. C-SIA.18 carries every derived/protected/versioned/rebuildable/non-authoritative/invalidation/inference-only property. |
| MAP C-SIA / Logging; V10 §7E-TSC §§6/7/9/29; B15 §5 items 3–7 | C-SIA.19 and root USED BY rows reciprocate existing TSC participant, attribution and event-link cards. Existing assessments are referenced without TSC calling SIA; audit authority, no root promotion, timing references and seven-field root boundary remain explicit. |
| V10 §25.11; B-INT-7 §§11–16/18/19 | C-SIA.20 plus .20.1–.20.8 carry the SIA consumer: eligible accepted readings, honest provisional confidence, one input after committed link, duplicate-free build, conservative status/ceiling/weighting, fresh assessment after restart, later evidence, post-commit enrollment event and authority limits. Existing committed-link failure atoms remain C-7L.11.13 and descendants. |
| B-INT-7 ownership remaining for CH09-h | CH09-h owns full prerequisites, bootstrap six-condition segment gate, trusted-phone/BAI opening, capture, lifecycle, proposed readiness and input-bundle records to their fields, coordinator IDs, events, crash/retry/stop mechanics and owner interfaces. Current SIA consumer lists the bundle/readiness content but creates no duplicate canonical coordination-record IDs. Activation thresholds remain unchosen in source. |
| B-INT-5 §13 and A26 §§4.1–4.3; Bundle 5 §5 Path 7 | Identity evidence never becomes private-mode or output authority. Root privacy and protection consumers use the existing owners. Full mode contracts stay CH09-i, output delivery CH09-d and enrollment CH09-h. No whole-file credit for these scoped reads. |
| Bundle 2 §5.6; Bundle 4 §9.1; Bundle 6 mechanical §§3/12; V10 §0B and component Map entries | Root USED BY continuations complete the existing declaration, authority, logging, control-query, outcome, affirmation and learning identity/security dependencies; assessment evidence does not acquire those consumers' access authority. |
| 05 NH Voice decision record v0_2 §5 | C-SIA.21 carries only the synthetic-output/identity-profile separation at CANDIDATE status. Speech engine/checkpoint/settings and language-input choices remain CH09-i/CH10-d; reported tests are evidence/history, not generalized behavior. Whole record read; one inherited whole-read obligation closed. |
| COMP complete embedded §3; kernel discovery; receipt checks | Companion SIA content corroborates the V10 record boundaries without replacing authority. Kernel matches add no SIA mechanics; whole-file obligation retained. A15 and B-INT-7 receipts are whole rereads establishing acceptance only; no independent closure audit claimed. |

### Source placements added by CH09-d

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 complete §25.4; MAP complete C-SACL; COMP complete embedded §4 | C-SACL root and .1–.17 carry the full speaker-access boundary, state, ordered gates, PBR use, output limits, background authority, failures and protected rules. Companion corroborates the same source conflict; MAP-only logging remains CANDIDATE. |
| V10 §25.4 / SACL-Owned State | C-SACL.2 with all nine session fields and .3 with all seven stream fields. Four access-level value atoms reuse C-OTHER.3 and descendants; in-progress record/material sensitivity live at .10.1/.10.1.1. No unstated schema or field encoding added. |
| V10 §25.4 / Access Level Calculation | C-SACL.4 and .4.1–.4.5 preserve exact Gate 0 → 1 → 2 → 3 → else order. Gate 0 has two alternatives; Gate 1 seven required conditions; Gate 2 five; Gate 3 six. Shared Ness-box, separation and disqualifier predicates reuse the same atoms. Three threshold names remain empirical configuration values without invented numbers. |
| V10 §25.4 / Gate 2 and Option A; §25.5 separation boundary | C-SACL.4.3/.4.3.2/.6 and the header retain the contradictory no-imitation-risk Gate 2 clause and recognized_ness-preserving Option A. Neither clause is silently removed or reconciled. Acoustic Gate 0 remains separate. |
| V10 §25.4 / Fingerprint, Three Mechanisms, Multi-Speaker Sessions | C-SACL.5–.8 and .8.1–.8.3 preserve independent biometric/identity factors, no wellbeing tier input, shared minimum, the private-unobservable exception and simultaneous dependent-stream downgrade. C-WIS-SEP owns the reused separation atoms. |
| V10 §25.4 / Permission Boundary Enforcement | C-SACL.9 and .9.1–.9.3 carry LMAC → Person-Box PBR reads, output-time category checks and refresh on version change; canonical PBR fields and presence condition remain C-7L.9/.9.1/.9.2. |
| V10 §25.4 / Access Changes, Indirect Disclosure, Output Gate, Internal Context, Background | C-SACL.10–.14 carry sensitivity comparison/immediate discard before write, retrieval-time exclusion without existence hints, final privacy then access, internal-context distinction and purpose-specific background authority. Privacy binding atoms remain C-7Q.11.3. |
| V10 §25.4 / Failure and Protected-Core Rules | C-SACL.15 and four failure children preserve restart, stale assessment, SIA failure and PBR-query failure. C-SACL.16 and seven children carry all unconditional protected rules without adding enforcement designs. |
| MAP C-SACL / Logging; V10 §0B | C-SACL.17 and four record children retain candidate access-change, disqualifier, discard and audit records. Root USED BY rows preserve all 115 distinct inspected earlier incoming consumers and their source-specific access limits; later continuations do not edit those files. |
| B-INT-6 complete §§1–5; B-INT-5 §6 and §§13–14; A26 §4 | C-SACL.18 proposed Output Delivery Coordinator and .19 ordered stages preserve independent owners. C-SACL.20 and eighteen handoff facts consume the single current mode/SACL truth, references, category limits, observability, cancellations and delivery fence. Full mode record/state/transaction ownership remains CH09-i. |
| B-INT-6 §6A | C-SACL.21 and three identity atoms keep proposed stable parent, stable request-and-destination duplicate key and per-attempt identity distinct. C-SACL.21.4 consumes seven mutable validation facts using existing owner-field atoms; none enters the stable key. |
| B-INT-6 §6B and §6D | C-SACL.22/.22.1/.22.2 and .25 preserve immutable protected payload references, seven canonical privacy bindings, eight SACL bindings and the transform → new version → privacy → SACL loop. Reused fields have no duplicate canonical identity. |
| B-INT-6 §6C | C-SACL.23 contains all sixteen proposed states; .23.16 has four explicit unknown-result transitions. Positive late confirmation records history without resend; non-delivery proof or verified same-token deduplication only permits freshly checked retry; absent safe facts leaves the parent open. Later restriction never fabricates an outcome. |
| B-INT-6 §6F, §7 and §7C; receipt §6 | C-SACL.24 plus four claim statuses and .27 plus seven dispatch steps preserve fresh immutable claim, flushed pre-contact intent, spent event, accepted handoff and channel-owned outcome. Header preserves older pre-attempt wording alongside the receipt's explicit pre-intent qualification; missing attempt event after intent never proves no contact. |
| B-INT-6 §6E, §7A and §7B | C-SACL.26 preserves owner authority in checkpoints; .28 carries all six per-write rechecks; .29 reuses the two canonical streaming alternatives C-7Q.11.3.10.1/.10.2. A checkpoint is never a substitute gate, fence or permission owner. |
| B-INT-6 §8 | C-SACL.30 reuses all twelve canonical restriction-trigger atoms, carries exact sensitivity comparison and immediate pre-write stop, restriction-before-recording and scoped background cancellation. Unknown channel history and late confirmation remain truthful. |
| B-INT-6 §9; B9 values complete §3 | C-SACL.31 consumes canonical C-7H.10 retry atoms with the actual values written inline: original plus two technical attempts, 10s/30s live or 1min/3min background minimum gaps, 7min/15min elapsed-from-first-failure ceiling, earliest bound, one careful rejection retry, real-change and early-stop rules. Unknown delivery permits at most one safe automatic retry only on proof or verified deduplication. |
| B-INT-6 §10 and §11 recovery-count wording | C-SACL.32 and sixteen crash-row cards cover rows 1–15 plus 11b, each with committed truth and recovery. Runtime restart has fresh epoch, Dry mode, guest access, dead old claims and no old formed-payload replay. The source's stale 'fifteen' count is marked, not used to omit row 11b. |
| B-INT-6 §§6A/6B/6F/7C/11/12 | C-SACL.33 has thirteen proposed coordination records and all newly owned declared field atoms; proposed payload-reference ownership remains .22.1. Existing purpose/destination/mode/privacy/access/material/identity facts are reused. No final serialization, closed code vocabulary or record field is invented. |
| B-INT-6 §12 | C-SACL.34 carries every one of the twenty-two event/logging mappings, including owner record plus coordination reference, claim-state and pre-contact dispatch-intent events, blocked duplicates and unknown outcomes. References-only logs contain no payload, hidden-existence detail or new authority. |
| B-INT-6 §§13–16 | C-SACL.35 retains all disclosure boundaries; .36 contains thirteen own failure-class cards plus canonical .23.16 unknown handling, covering all fourteen source classes; .37 contains runtime prohibitions. Source audit, implementation and adoption workflow is excluded. Open dependencies remain open. |
| B24 complete §6.5; §6.3; §6.4 opening rules and full §6.4-C4 | C-SACL.38 writes all final-output consumer facts inline: governed surfaces, final_gate_evaluation facts and terminals, access reduction invalidation and unknown-outcome honesty. Full B24 records, states, transactions, lookup-first behavior and recovery matrix belong to CH10-b. No complete B24 package claim is made here. |
| B24 §6.4-C4 versus B-INT-6 §6C | Header and C-SACL.38 preserve owner-specific terminal delivery_outcome_unknown / terminal_delivery_outcome_unknown versus proposed nonterminal delivery_unknown. No unified lifecycle mapping is invented. Independent audit/CH10-b must assess the boundary with full B24 ownership. |
| Kernel §C.1, §O DP1–DP5, §T introduction/I-10/I-12, §U, §S.2 DM-11; kernel receipt | C-SACL.39 carries distinct delivery identities, owner-decision references, retained domain states and additional duplicate prevention. Kernel never replaces privacy/SACL/mode/channel authority. Full kernel lifecycle, records and mechanical owner placement remain a later whole-source obligation, to be mapped with CH10-b's durable-operation mechanics rather than invented as a new top-level component. |
| B-INT-4 §7 C2; V10 §7E-TSC §§16/20/28/29 and §17 Phase 1 | C-SACL.40 supplies current recognized-Ness confirmation for the TSC request tuple, reuses four existing response atoms, binds confirmation_id into BAI consumption and confirmed_at into sacl_recognized_ness_confirmed_at, rejects absent/stale/conflicting/unverifiable facts and obtains fresh retry/recovery confirmation. Root rows preserve other existing TSC access consumers. |
| Bundle 5 Path 6 and §§6–8; Bundle 5 receipt | Output order, independent authority, identity separation and frozen wording are checked against C-SACL.18–.39. Receipt establishes package acceptance only; conditional independent closeout audit is not claimed performed. Other bundle paths retain later owners and the whole-file reading obligation. |
| B-INT-8 §15; B-INT-7 §§14–15 | Existing Connection output and enrollment consumers are reciprocated without importing their full owner mechanics. Enrollment remains CH09-h; Connection owners remain as already written; no recognition-to-access or output-gate bypass is added. |
| B16 complete §8 and §11 opening access bullet; B16EEB complete §13.4; AIC complete §15 | Root USED BY rows retain existing promotion, evaluation and authority-integrity consumers' current SACL boundary. The scoped source facts remain with their existing canonical owners; no whole-file reread or new promotion mechanism is claimed. |
| Bundle 2 complete §5.5; Bundle 3 complete §16; Bundle 4 complete §12 and retained §9.1; Bundle 6 retained §12 | Root USED BY rows retain existing declaration, clash, specialist, living-state, logging and control-query consumers with each place's own input/action/change. No grouped using places, added access authority or duplicate behavioral owner. |
| Canonical earlier-card inspection | All 115 earlier incoming IDs inspected. Full C-7Q.11.3 subtree, C-7L.9/.9.1/.9.2, C-LMAC.14.3, relevant C-7H.10 retry cards, C-7Q.6.4 and TSC request/response/confirmation cards checked for reuse. Earlier chapter fingerprints remain preserved; no earlier file changed. |

### Source placements added by CH09-e

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.6, complete | C-BAI and C-BAI.1–15: complete OS/pending/token/lease/state fields; purpose vocabulary; lifecycles; result/failure classes; audit split; protected-core rules. Shared field atoms are referenced, not assigned duplicate IDs. |
| V10 §7E-TSC consumer interfaces and §25.3/25.4 earlier consumers | Earlier canonical TSC/SIA/SACL cards retain ownership; 47 incoming fields across 45 named cards receive current root USED BY rows. C-BAI.10 and .16 state the producer boundary in full. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-BAI; CY-I | Official name, source-discovery scope and record-access boundary retained; CY-I use at C-SACL is one separate root USED BY row. Full cycle belongs to CH11. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded §6 | Checked against complete V10 §25.6; C-BAI.1–15. Historical/governance narrative excluded under contract §1.3. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` §4; §7 C1 | C-BAI.16.1–6: one-winner rule, live checks, ten receipt bindings, flush-before-success, no-receipt failure, post-receipt completion and BAI-only blocked-consume event. The C1 request/response atoms, receipt fields and claim/recovery mechanics remain C-TSC.16 and .29, not new BAI subparts. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Acceptance and exact standalone scope support ACCEPTED bridge lines. Formal independent closure review is not claimed. No workflow content enters behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` §5B, §6, §12 record 7, §14, §§17–18 | C-BAI.17–18: exact opening-purpose spellings, operation bindings, consumption-before-activation, dry-after-crash, current dual-owner lease/Gate1 truth, reference-only observations and fallback. Full mode records, field cards, indicator, fences and activation coordinator remain CH09-i; no completed mode-record coverage claimed here. |
| B-INT-5 §6 Reusable? lease label | Marked source-conflict paragraph and C-BAI.6 Does retain V10 repeated queries/never consumed and the differing matrix label; no silent rewriting. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Acceptance/owner guarantees checked; no claim of implementation or later independent formal closure. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` §§4–6, §18, §19 I1–I10, §§22–24; §17 identity table | C-BAI.19.1–7 carries BAI request/result, all six prerequisite facts, owner re-read, revocation, durable proof and complete minimum binding, proof/opening crash boundary, BAI-only I5C and biometric identity limit. Full proposed prerequisite/begin/binding/session/capture records and their field cards, capture lifecycle and eligibility remain CH09-h; no duplicate EC authority. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Acceptance and §6 frozen wording notes checked. C-BAI.19.5 does not close a nonexistent session; .19.6 keeps BAI the sole I5C source. Receipt's conditional formal closure is not treated as independently verified here. |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` §§7.12–7.13 | C-BAI.20.1–4 states conditional BAI producer mechanics, current six-condition check, durable receipt, no-receipt failure and all post-receipt outcomes. Canonical judgment/claim/receipt field and recovery atoms remain CH03-e–CH03-n. NHD-B16EEB-D16 remains open; no purpose or scope selected. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` §§5–6 | Supports ACCEPTED conditional architecture without closing the seventeen open decision slots. Existing C-GOLD.1.11.17 remains the authority-choice card. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` §4 Group 11 and §6 FR-0003 | C-BAI.8 and .8.3 carry restored different BAI keys for different token purposes with DECIDED-2026-09-25 and deciding-record citations on every such line. |
| `98_HISTORICAL_SOURCES_PRE_V10/sources_recovered/NH_SESSION_REFERENCE_June29_2026.md` §3D | Authorized restored-source file read whole; only FR-0003's key-separation text supplies C-BAI.8.3. All other archive behavior and narrative excluded from this piece; nothing else is restored by reading it. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` §6E and §13 | C-BAI.21 and reciprocal root rows preserve live lease ownership at output handoff/checkpoints; full output mechanics remain frozen CH09-d. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` §F.2 R31, §K.2 TSC owner row, §T I8 | C-BAI.21 preserves actual proof and owner-only audit. Full envelope, retry/recovery and owner-reference interfaces remain CH10-b; bounded rows do not earn whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` Paths 3/5/6/7; §§6–8 | Cross-checked C-BAI.16–19 owner and durability boundaries, including different TSC/mode/enrollment recovery outcomes. Complete maintenance/device paths remain CH09-f/g; full consolidation coverage remains later owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Accepted consolidation scope was read whole in CH09-d; current discovery checks only. No new independent whole-read credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` §4.1–4.4 | C-BAI.17–18 and root privacy consumer rows preserve separate mode and identity/security owners. Full relationship policy belongs to CH09-i. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Acceptance/navigation cross-check only; no new BAI mechanism or whole-file read credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 | C-7P.2.6 root reciprocal retains specialist BAI/SACL authority and strictest applicable rule. Other action classification/record mechanics remain their earlier owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` §§13–14; §9 discovery | Store-side consumer boundary remains C-TSC; C-BAI.16 does not take B15's transaction ownership. Full B15/recovery remains earlier CH04-b; no new B15 mechanism written. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` discovery | Dependency/accepted-scope check only; complete earlier TSC ownership retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` §15 | Applicable biometric authorization over protected records is preserved; canonical control-plane mechanics remain earlier owners. The control plane acquires no BAI authority. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` §31 | Existing SACL/BAI access boundaries preserved only; no new BAI mechanism. Other framework capabilities remain their named later component owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` §1 discovery | Source-list reference only; adds no BAI behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` §7 discovery | Dependency boundary only; adds no new biometric mechanism. |
| Decision-index search hits: v0_11 and older v0_10/v0_6/v0_5 | Navigation only, never behavior. Highest active version controls navigation; older versions receive no behavior citation. |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` search discovery | EXCLUDED from behavior: contract §10.9 restricts ledger use to Appendix B. FR-0003 behavior comes from the deciding record and authorized archive, never from the ledger. |
| Inherited 145 READ-file inventory plus one authorized archive file | The cumulative matrix remains intact and gains this source placement. Partial discovery does not close inherited pending whole-file reads. |
| Earlier frozen card identities and canonical ownership | No earlier piece is changed. Existing TSC receipt and interface fields, BOP event/field atoms and Gold judgment/claim mechanics retain their IDs. Current source-map deferrals name CH09-f/g/h/i, CH10-b and CH11 explicitly. |

### Source placements added by CH09-f

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.13 / What BGMM Is and Is Not | C-BGMM, .1, .8: sole bounded local maintenance path; no general administrator authority. |
| V10 §25.13 / Protected Material Boundary | C-BGMM.2/.2.1–.2.5 and .3/.3.1–.3.7: five purpose/material scopes, immutable records, recovery-value prohibition, governed appends. |
| V10 §25.13 / Normal-Path Write Prevention (Tamper-Resistant, Not Physically Impossible) | C-BGMM.4/.4.1–.4.6: all five layers and the exact administrator/physical-attacker guarantee distinction. |
| V10 §25.13 / Signed-Manifest Trust Anchor | C-BGMM.5/.5.1–.5.5.3, .10.5, .12.5: expected hashes/versions, pinned public key, signed provenance and ordered startup/rollback verification. |
| V10 §25.13 / Encrypted Full-Content Rollback Packages | C-BGMM.6 through .6.5: all record fields, per-file fields and metadata categories; session_id reused at .13.1; canonical separated keys C-BAI.8.1/.8.2. |
| V10 §25.13 / Protected Startup Recovery Worker | C-BGMM.7/.7.1–.7.7: boot and integrity conditions, bounded exact scope, successful permanent inaccessibility and three distinct failures. |
| V10 §25.13 / Entering Maintenance Mode | C-BGMM.8/.8.1–.8.6 and .8.5.1–.8.5.3: all six entry steps; the emergency factor conditions are individually placed. |
| V10 §25.13 / Purpose-Specific Authorization | C-BGMM.2/.2.1–.2.5, .8 and .9.2: each exact factor conjunction; emergency device-trust scope; no phone required for device-trust/emergency branches. |
| V10 §25.13 / File Scope Enforcement | C-BGMM.9/.9.1–.9.3 and .13.4: exact token file list; out-of-scope and immutable refusals; emergency override. |
| V10 §25.13 / Change Application | C-BGMM.10/.10.1–.10.8: seven steps in exact source order and immediate post-touch rollback. |
| V10 §25.13 / Automatic Relocking | C-BGMM.11/.11.1–.11.7: all seven triggers, immediate token revocation/event and partial-change rollback. |
| V10 §25.13 / Rollback | C-BGMM.12/.12.1–.12.6: decryption, prior_hash check, exact bytes, signatures/metadata, prior signed manifest and no-write idempotency. |
| V10 §25.13 / BGMM-Owned State | C-BGMM.13/.13.1–.13.11.2: all eleven fields, append-only applied_changes and checkpoint file-list/hash_before references; no invented session_status enumeration. |
| V10 §25.13 / Privacy During Maintenance | C-BGMM.14/.14.1–.14.5: each content-free description/log/audit surface, protected rollback bytes and all sensitive-content classes. |
| V10 §25.13 / Immediate Security Audit Events | C-BGMM.15/.15.1–.15.17: all seventeen names, structural-only content and write/flush before producing-function return; no invented event schemas. |
| V10 §25.13 / Crash, Restart, Offline Behavior | C-BGMM.16/.16.1–.16.4: open-session crash, interrupted rollback, startup integrity failure and fully offline operation. |
| V10 §25.13 / Protected-Core Rules (Unconditional) | C-BGMM.17 reuses the atomic owners .9.3, .4, .11, .9.2 and .3.6 without new authority. |
| V10 §25 / Build-Time Implementation Settings | C-BGMM.18/.18.1/.18.2: empirical timeout and available-hardware key mechanism; values remain open build settings (Map C10), not conceptual Ness decisions. |
| V10 §§2/2A, §0B and §25.6 purpose/key boundaries | C-BGMM root preserves all fifty-one earlier C-2 maintenance-use places through named gates; .15 retains living-record boundaries; canonical BAI purpose/token/key identities are reused. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-BGMM, C-2 and CY-I | Exact root name, governed-append distinction, qualified physical-attacker guarantee, structural-only maintenance privacy, mandatory C-2 gate and the C-PAIR use in CY-I. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded security-design §13 | Source-conflict paragraph: stale package deletion versus V10 sealing/inaccessibility; no Companion deletion behavior adopted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 | C-BGMM root USED BY C-7P.2.6 reciprocates specialist protected-change authority. General action mechanics remain canonical in CH07-c. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` §§5B/6 and change-summary context | Cross-purpose token boundary checked; no maintenance-purpose token can open Personal Mode. Canonical BAI boundary remains CH09-e; complete modes remain CH09-i. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` dependency paragraph | BGMM mention is the preserved supporting source title, not added maintenance mechanics; complete enrollment remains CH09-h. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` §2.1 | Names governing BGMM law; adds no BGMM internals in the reviewed passage. Full kernel behavior/whole-file obligation remains CH10-b. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted ordinary-chat policy, frozen source status and open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Search hit is protected-file verification prose, excluded from maintenance behavior. Accepted room-start policy and preserved open boundaries remain for CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` verification/closure context | Protected-file search hit is task verification, excluded under contract §1.3; no maintenance behavior added. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` §6 FR-0003 | Existing restored key-purpose rule remains C-BAI.8.3 in CH09-e; no additional archive behavior imported for this piece. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` NHD-M25 search hit | Navigation only; no behavior and no current-version authority inferred. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` NHD-M25 search hit | Accepted prior navigation index; no behavior used from its row. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` NHD-M25 search hit | Earlier candidate navigation; no behavior used. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` header and NHD-M25 row | Highest current candidate index used only for navigation; v0_6's accepted-prior standing is preserved; no architecture derived. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` BGMM discovery | The matched TSC provenance pointer adds no maintenance mechanism. V10 governs; whole-file credit is not claimed here. |
| `01_AUTHORITATIVE/cursorrules` BGMM/maintenance discovery | No new BGMM body found by scoped discovery; implementation/workflow text is not inserted into behavior. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` BGMM/maintenance discovery | No additional maintenance restoration found; no archive expansion authorized or taken. |
| Remaining owners | CH09-g full pairing/recovery material lifecycle; CH09-h full enrollment; CH09-i full modes; CH10-b full kernel; CH10-e interface packages; CH11 side paths; CH12 regenerated final registers. |

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped whole sections: §25.13; §25 Build-Time Implementation Settings; §§2/2A; §0B. Bounded §25.6 purpose vocabulary and Key Separation; partial §7Q context was inspected but not credited as a whole section. No new whole-file credit. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | C-BGMM, C-2 and CY-I entries whole; maintenance naming/wiring/build-setting/qualified-tamper boundaries. No new whole-file credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Embedded security-design §13 whole, including all old package-deletion wording; conflict comparison only. No new whole-file credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | §9.1 whole across recovered bounded reads; specialist authority reciprocal. No new whole-file credit. | `0c9a201130d5811c838fea0d5655c8a98aac909afdc60024830204a690e77f97` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | §§5B/6 whole and bounded change-summary context; cross-purpose maintenance/mode separation. No new whole-file credit. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Bounded dependency paragraph including preserved security-design source title; discovery classification, not full enrollment coverage. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | §2.1 whole; BGMM is named governing law, not a new maintenance mechanism. Full kernel remains CH10-b. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file; accepted interface scope, receipt conditions and unrelated protected-file verification hit reviewed. New whole-file credit; behavior placement remains CH10-e. | `8f22b0a1dd7b4393934af873993ef797437e8d312164b1676caecab2e240f18c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file, with the truncated tail recovered in a bounded read; scope and unrelated verification hit reviewed. New whole-file credit; behavior placement remains CH10-e. | `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Bounded verification-table/closure context around protected-file hit; project-only prose excluded; no whole-file reread claimed. | `298de053269f4a9e93e97dfd994d33b0b879d71af636b169769264e7183d9d4c` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Bounded §6 FR-0003 and adjacent row context; existing key restoration reused only through CH09-e ownership; no new whole-file credit. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | NHD-M25 search-hit discovery only; no whole-file credit and no behavior authority. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | NHD-M25 search-hit discovery only; no whole-file credit and no behavior authority. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | NHD-M25 search-hit discovery only; no whole-file credit and no behavior authority. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Header/status/authority context and NHD-M25 row; navigation only, not whole-file credit. The broad source-list output was partially truncated and receives no complete-read claim. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | BGMM/maintenance topic search and its TSC provenance pointer; scoped discovery only. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/cursorrules` | BGMM/maintenance topic search; no matched additional maintenance body. Discovery only, not whole-file credit. | `5050d08825b93acd72a79d07946e43c8cbe537e079517ccfe66bcae8e30e96e9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_2026-09-24_v0_1_CANDIDATE.md` | BGMM/maintenance topic search; no additional restoration identified. Discovery only, not whole-file credit. | `b6643a6b208a0aa6167d032769a1ea5be4f64f672289a16fc216ef23b56c2fe0` |

### Earlier chapter identities preserved

| Piece | SHA-256 |
|---|---|
| CH00 | `d01e8ec370be9c8e50fbb293c863c95ddaf6f82af5700877bf1a57276a1f4998` |
| CH01 | `f86342e90f8789a5b825fbe73f4bc42041c6537498a32a01980287ad32d47544` |
| CH02 | `22168ca6a6a54a2d142dcc7e1d068ca1ab7270b28a90e8e10c2a0106b595d19a` |
| CH03-a | `3b0ba1cb3ea3415ef71c5343702fd2c7ddcd44675aa8f0b4bf5e7aeab2aa80db` |
| CH03-b | `ba62fb68b050b3840afeabec299b2aa0baac17ba2f79869c1fc031dbc195d8b5` |
| CH03-c | `20d022f2d237cf0a29e4128eae510e0cf153505a2ffd0c64ff512fed9cb06fa6` |
| CH03-d | `9444e60b0b4cb09c1efd5d03c06579af4864f7437a10555fdeca54e50687195c` |
| CH03-e | `a33e27d89548e57f16e8c17b489ca971f3f992101e7664a0260954494f572aa2` |
| CH03-f | `567d566a000971890c22771cbaa9e6fee2669383f02975206013d440e4fb2347` |
| CH03-g | `59f8d76f64e95da500e86644e79a2a9e9cdec6dedd384b0cb5d1536ee1ca2e7f` |
| CH03-h | `af59933e649a92dc1b58dd679fbffad86fa999c2b6ffc36259eda227fea3f582` |
| CH03-i | `bb128e4e4ef9fba5889ee54b90268962d02162e51cb1ff9e5eb6a7e089e3c47f` |
| CH03-j | `0b2bb5079af523e3f101705704316b1092f4a536575eff11ff020bd1eaa13a20` |
| CH03-k | `51c6e87ed42d6bd341dc58a24ef11fb6baaf58bb2e93f7d4a435622382fd1ce3` |
| CH03-l | `b63bcb9f9b411fc79e36b84ddbeb7e87646e651d0ad7b410fbd3d0b9d268e81f` |
| CH03-m | `5354b6bd7903fa4c6e3e3632f6d09a304624da076f49b7fb14e1b1f3b837e2b2` |
| CH03-n | `0cace48ca710e471078de69f5da65c1a26728b7be07b65b15893158546218762` |
| CH03-o | `a531204f2ac54dda00f76f3434e6bd294fab0bb7908a12457f44a09fc1749f5c` |
| CH03-p | `6c43976354a4d2e897112ebd41b935c5a207c2f2f92ed64fa79b24040de6d42d` |
| CH04-a | `1d2bb9e3a3c66f08de6b3d8fb12d5dbad6ae0b1dcc70d395c26dd5e156e12769` |
| CH04-b | `2af41d1f927be32406737cdde4d8d4c3928cf91b7eaa062ffd9810fe6b033bbc` |
| CH04-c | `7176edd53af6853fc9e1e76e7f80204000527196dc2d96283eb6aed02870204b` |
| CH04-d | `901d6eb6474e79a4c14fd2ab096e07fc4e538d2a40c181b07c68ebf70cb2b736` |
| CH04-e | `b4c432cb115b379b300d21c826ce5ea80f10c843af2e13e8b28a2f6b60b88695` |
| CH05-a | `a6bf0cbce2d92e412ad3af4a27909e8cfeb8f15ad0d9b4913c5708eeeed34dd9` |
| CH05-b | `af89c86e7991cdd4c0bb821cd5861abc01e80c9750e6de954062088eaa37b8b9` |
| CH05-c | `dd7e5b17cd4e8e7dae2125d45d30ebdfdcbe349b1f80767c3a8442f5448e0e6d` |
| CH05-d | `67d59453a923647e7616898801e2dcc8ea1ff741d04617886411ad309344285d` |
| CH05-e | `e526f830db5a71a0a60c7c7e0a50ef0344f81f46bce4355e1a27480d6d0076cd` |
| CH06-a | `b604ac8293119ad8cf6f3686089f256cf5aa5fbbff1ac431edec62c2799a3571` |
| CH06-b | `fc426658bf22d37555d20eccf9a56949fb06704bf7a80fb36ee7c5cb8ce61c7d` |
| CH06-c | `05ba5405d963b66d3c75e26255f2932f146adf5f7098c4b6bf612caf539286ff` |
| CH06-d | `a79bc0af9ed246a30a4c526edf7f291b14d7b9b570c88bf94df5d7cbf9ce7dc3` |
| CH06-e | `79068327ad5315666eda0e78dda23fce1bf903f1fed0a5a84d80d3c021889692` |
| CH06-f | `da69614a03fecdf985ec8b2451849cfe282b6acadfd8257a1c7de0b4b7ecb952` |
| CH06-g | `4a8168002eac965e248d35fc761feb51232a813b0406e2df9e0851f6b42bf676` |
| CH07-a | `9ac2415acd8c58390c651a2ad4ec2ba38b16509bffae3816e68b3d5a69cfd2cd` |
| CH07-b | `7f36823b65c8523b456d93e827b0456d97dc429c9bb3ee35ff9d9fb8f778761a` |
| CH07-c | `563b84b894c3bc5022f087a356fb412a3a99eaa8a629f7cc5e26965f409055e8` |
| CH08-a | `08d9a00db55c7b18091e1942e792c8e21886525c1cf0db3dc07112dcab58838f` |
| CH08-b | `6bb46d5f30d1e67d7a27f252d656118a89b86f3a46a820542010f8599b169fa0` |
| CH08-c | `30824515b3c0d90a694118848113c4695434b1203ff1c8d5267e4dee5d456bbf` |
| CH08-d | `775c59f45dfc8fd1b8befe3e735062cfff5fab76c479afd8cfb2da34f9eaef5f` |
| CH08-e | `ac9be126cbff22a1eb34ce7fa8b881feae05aa39a2deb6510ac9de5a196bdfd5` |
| CH08-f | `d3d86da7a5e786b5449bb54a48afb476d076a9bbd9f35efd770f6368f8ed8385` |
| CH08-g | `ebf122c638aeece6e97816efc417a01e03c4140fd0d7131b18d6e80a6b8a24a3` |
| CH09-a | `22af523cc67cd0328b30cbcd7d09822d92f98e9e4b964fbd04b77bc565b08aea` |
| CH09-b | `283706c41b3d9e18751a24ee20f2406b52f9af043e675d1f838542a47aeb2f2d` |
| CH09-c | `5a61d0c9956317dc544fb818bfb8ffcd08c6ebde710cf9c264b45e38f2b41e50` |
| CH09-d | `8877df31acb4ac15c45d2687f5e82c2fb5a5541fef57fb6f475ca7694c01d338` |
| CH09-e | `370aed5b7efa49a861e39ff2bad7e1d21bed31826f001bd77cde46382cf509ad` |

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

48 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
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

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)

§1.3 no history/actions/roles/workflow in this chapter: PASS — all 140 behavior cards and their use rows were reviewed; operational maintenance actions are N.H behavior. Project receipt history remains outside the behavior. The whole-file wording scan and behavior workflow/formula scans report zero hits.

§1.4 every gap written as NOT DECIDED: PASS — 275 empty behavior fields are registered exactly once, with no filled field left in the register. Exact state encodings, session-status vocabulary, event schemas, numerical timeout and hardware implementation remain unchosen. The source-defined names and boundaries are explicit; no derivation fills an open field.

§1.5 conflicts marked, none resolved: PASS — the Companion's destructive package-disposal wording is explicitly marked against V10's sealing/inaccessibility rule. V10 behavior is retained, and the frozen Companion is not changed. The separate file_metadata/prior_metadata wording variation is preserved without adding a second field. The administrator-versus-physical-attacker qualification remains intact.

§3 exactly one stamp per line: PASS — all 1,266 field lines and 257 use rows follow the stamp rules; each named relationship uses the named card's status. There are zero BUILT lines and no new implementation claim. Empty fields retain the exact unstamped NOT DECIDED form.

§4 every behavior line cited in the exact format: PASS — all 30 distinct behavior citation locations resolve in the pinned sources. Source review covered the full maintenance body and the bounded supporting sections recorded below; no citation substitutes for the behavior. The conflict's Companion location was inspected in its complete embedded §13.

§5.4 one name per thing: PASS — exact canonical names were checked mechanically, including all 51 C-2 maintenance-use owners, the biometric purpose/token/keys and future C-PAIR. All 66 selected source names and values occur. The 17 audit event names are present; bgmm_confirmation is a purpose prefix, not an eighteenth audit event. No source-proposed name is silently adopted.

§6 all template fields present, in order, for every part: PASS — 140 complete cards, 1,266 field lines and 257 single-place USED BY rows. No duplicate ID, grouped place, multi-path row or self-listed SUB-PARTS entry remains. The full four-label header retains two trailing spaces on every label line.

§6.3 reciprocity within this chapter: PASS — all 244 internal relationships have corresponding individual use rows. The 75 outgoing relationships and 5 of the 13 external uses have 80 continuation rows identifying both ends; the other 8 external uses are answered by the using cards' own TOGETHER lines. Three inspected earlier incoming relationships are reciprocated at the root. All 51 earlier C-2 maintenance-use places have explicit root gates; prior files remain frozen. Future device-trust uses include the separate CY-I place.

§6.4 every decided detail written in, no citation used in place of content: PASS — all five purpose/material/factor branches, five protection layers, signed-manifest checks, package fields and metadata, bounded recovery and its three failures, six entry steps, three emergency conditions, seven change steps, seven relock triggers, restoration sequence, eleven session fields, checkpoint atoms, maintenance privacy surfaces, seventeen events and two build-time settings are placed. Full pairing, enrollment, modes, kernel, interface packages, side paths and registers retain their named later owners.

§6.5 sub-parts recursed to the bottom: PASS — the record fields, metadata categories, factor conditions, ordered steps, named events and failure outcomes have their atomic cards or canonical reused owners. The misfiled-box review covered all 1,266 field lines, 420 restriction/failure/gate slots and 426 actual lines in those slots, plus every use row. All 29 positive flags are named by card and line with individual reasons: 13 empty-TOGETHER flags and 16 prerequisite-review flags, across 26 cards; no plain precondition remains. No automatic enforcement is inferred where the source states only a boundary.

§9 coverage matrix rows added for every file used: PASS — 37 source-scope/remaining-owner rows accompany the cumulative inventory of 146 distinct pinned file paths; zero paths are absent. All 18 current READ RECORD fingerprints match both full SHA-256 and pinned Git blob identity/byte length. All 51 earlier chapter SHA-256 values are individually listed and unchanged. Two new whole-file reads leave 48 inherited pending whole-file obligations; discovery and partial sections receive no whole-file credit.

§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior states source-backed machine requirements, conditions and boundaries. It contains no recommendation or second-person instruction. Its references to Ness's physical acts, explicit confirmation, abort and interaction requirements are part of the source-defined machine behavior.

Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`. Both were discovered through protected-file search hits and reviewed as complete receipts; their interface behavior remains for CH10-e. All other current reading scopes are listed in READ RECORD without new whole-file credit. Contract §11.3 was reopened after writing and immediately before this check was appended. These are writer delivery checks, not the independent audit or adoption.
