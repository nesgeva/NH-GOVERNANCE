# Chapter 9-b — Group G: C-OTHER

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-b.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece contains the other-speaker architecture: permitted disclosure, guest and known-person use, separate parent identities, requested translation, speaker attribution, the third-party cache boundary and continuous security. Existing Person-Box, privacy and TSC atoms retain their canonical owners. Complete identity assessment belongs to CH09-c, SACL state and delivery coordination to CH09-d, biometric authorization to CH09-e, mode wiring to CH09-i, phone policies to CH10-d, and side paths to CH11.

[SOURCE CONFLICT: V10 §25.2 / Fingerprint-Authorized Batch Promotion names a sealed-store append destination. MAP C-OTHER instead names the B11 active writable batch and excludes a sealed batch. V10's own sealed-root refusal also remains binding. Both route descriptions are recorded; no permission to reopen a seal is inferred.]

[SOURCE CONFLICT: V10 §25.2 / Fingerprint-Authorized Batch Promotion orders readings → §7J → §7M → §7L proposals. MAP C-OTHER instead fans readings out to §7J/§7K/§7L/§7D under their rules, then assembles §7M from permitted sources. The differing path descriptions remain explicit.]

[SOURCE CONFLICT: V10 §7Q requires increasingly stronger authorization for later third-party operations and stronger default restrictions for minors/highly vulnerable people. A7 §§4.5–4.7/6 and B7 §3 permit ordinary bounded interpretation without separate permission and remove automatic category restrictions; Bundle 5 §8 calls the V10 wording frozen pre-decision text. V10 governs this candidate under the build contract. Existing CH08-a conflicts remain open.]

[SOURCE CONFLICT: V10 §25.4 Gate 2 lists disqualifying imitation-risk flags, while its Option A and §25.5 preserve recognized_ness when imitation_risk blocks top_security. This piece does not reconcile the wording; the full calculation belongs to CH09-d.]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.

<!-- BEGIN BEHAVIOR -->

### C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2)
Stamp: DESIGNED    Source: [V10 §25.2] [MAP C-OTHER]

ALONE
- What it is: DESIGNED — The architecture for speaking with people other than Ness while retaining the complete internal mechanism and limiting what each current speaker may receive. [V10 §25.2 / Core Principle]
- Takes in: DESIGNED — Speaker assessments, the current access level, person-specific permission boundaries and attributed third-party session material. [V10 §25.2] [MAP C-OTHER]
- Does: DESIGNED — Keeps internal understanding separate from disclosure; applies guest or known-person limits, preserves separate identities and speaker attribution, and handles parent translation only within Ness's request. [V10 §25.2]
- Gives out: DESIGNED — Permitted responses for the addressed speaker, private translation assistance for Ness, and attributed material held or processed through the authorized cache path. [V10 §25.2]
- Must never: DESIGNED — Expose private Ness memory to a guest, transfer one person's permissions to another, acknowledge hidden information indirectly, turn a third-party claim into a fact about Ness, or let another speaker change permissions, memory, security, system authority or behavior. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: DESIGNED — Uncertainty reduces access; medium-or-higher spoofing immediately reduces access to guest and queues a private Ness alert. [V10 §25.2 / Continuous Speaker Security]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and suspicion assessments; C-TSC — Temporary Session Cache (§7E-TSC): third-party material retains session context and speaker attribution; C-7L.9 — Person-Box permission-boundary read interface: the active person's PBR reference. [V10 §25.2] [MAP C-OTHER]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current speaker level and category limits bound disclosure; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal use and visible disclosure need their own privacy authority; C-7P — Permission & Authority Boundaries (§7P): permissions cannot override the protected core. [V10 §25.2] [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): requested retrieval remains inside current access and privacy limits; C-7L — Person-Boxes (§7L): authorized third-party readings may support person proposals without collapsing attribution into truth. [MAP C-OTHER] [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | The current speaker and person-specific boundaries. | Determines what may be revealed or done while the full mechanism remains internally active. | Only speaker-permitted disclosure reaches the output path. | [V10 §25.2] [MAP C-OTHER] |
| 2 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | Third-party session material with its complete context. | Holds it outside Meaning Engine visibility pending session authorization. | No automatic long-term promotion follows from conversation. | [V10 §25.2 / Temporary Session Cache] |
| 3 · DESIGNED | C-OTHER.7 — Request-driven parent translation | A parent conversation and Ness's request. | Uses the complete mechanism within the requested scope and permitted disclosure. | Understanding creates no authority to reveal private context. | [V10 §25.2 / Parent Translation] |

SUB-PARTS: C-OTHER.1 — Internal understanding and external disclosure; C-OTHER.2 — Protected authority for other-speaker use; C-OTHER.3 — Four access levels; C-OTHER.4 — Guest conversational response; C-OTHER.5 — Known-person permission boundaries; C-OTHER.6 — Separate parent records; C-OTHER.7 — Request-driven parent translation; C-OTHER.8 — Statements about Ness retain their speaker; C-OTHER.9 — Person-Box visibility for other speakers; C-OTHER.10 — Third-party cache boundary; C-OTHER.11 — Completed-session batch authorization; C-OTHER.12 — Continuous speaker security; C-OTHER.13 — Current disclosure limits; C-OTHER.14 — Other-speaker operational records

### C-OTHER.1 — Internal understanding and external disclosure
Stamp: DESIGNED    Source: [V10 §25.2 / Core Principle]

ALONE
- What it is: DESIGNED — The permanent distinction between internal processing and disclosure to the current speaker. [V10 §25.2 / Core Principle]
- Takes in: DESIGNED — Information available to the mechanism and the current purpose, privacy authority and speaker access. [V10 §25.2 / Protected Rules (Unconditional)]
- Does: DESIGNED — Keeps the whole mechanism active at every access level; speaker access limits surfacing while internal use remains subject to privacy and authority rules. [V10 §25.2 / Core Principle] [V10 §25.2 / Protected Rules (Unconditional)]
- Gives out: DESIGNED — Internal understanding and a separately bounded disclosure decision. [V10 §25.2 / Core Principle]
- Must never: DESIGNED — Treat internal understanding as permission to reveal or treat an active internal mechanism as permission to bypass privacy. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal information use requires its own authorized purpose; C-7P — Permission & Authority Boundaries (§7P): processing stays within the applicable authority. [V10 §25.2 / Protected Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Internal results and current access. | Restricts what may be surfaced without reducing the whole mechanism to a guest mechanism. | Access governs disclosure, not the existence of protected context. | [V10 §25.2 / Core Principle] |

SUB-PARTS: NONE

### C-OTHER.2 — Protected authority for other-speaker use
Stamp: DESIGNED    Source: [V10 §25.2 / Protected Rules (Unconditional)]

ALONE
- What it is: DESIGNED — The unoverrideable authority limits that apply during other-speaker interaction. [V10 §25.2 / Protected Rules (Unconditional)]
- Takes in: DESIGNED — A speaker's request and the permissions belonging to that person. [V10 §25.2 / Protected Rules (Unconditional)]
- Does: DESIGNED — Keeps each person's permission separate; keeps memory, permissions, security rules, system authority and N.H's behavior outside other people's change authority. [V10 §25.2 / Protected Rules (Unconditional)]
- Gives out: DESIGNED — Interaction within the existing protected authority boundary. [V10 §25.2 / Protected Rules (Unconditional)]
- Must never: DESIGNED — Transfer permissions between people; allow another person to change permissions, memories, security rules, system authority or behavior; or permit even Ness to override the architectural core, immutable roots, provenance or non-negotiable safeguards. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): protected authority remains binding on the interaction and PBR maintenance. [V10 §25.2 / Known-Person Permissions] [V10 §25.2 / Protected Rules (Unconditional)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | A speaker request subject to current authority. | Enforces access without granting permission to rewrite the security or architectural rules. | No speaker-level grant overrides the protected core. | [V10 §25.2 / Protected Rules (Unconditional)] |

SUB-PARTS: NONE

### C-OTHER.3 — Four access levels
Stamp: DESIGNED    Source: [V10 §25.2 / Access Levels]

ALONE
- What it is: DESIGNED — The four-level disclosure vocabulary determined by SACL from SIA output. [V10 §25.2 / Access Levels]
- Takes in: DESIGNED — Current SIA identity evidence, biometric status where required, suspicion and the active person's PBR. [V10 §25.2 / Access Levels]
- Does: DESIGNED — Distinguishes `top_security`, `recognized_ness`, `known_person` and `guest`; the whole mechanism stays active under each. [V10 §25.2 / Access Levels]
- Gives out: DESIGNED — The current speaker's disclosure level. [V10 §25.2 / Access Levels]
- Must never: DESIGNED — Let uncertainty expand access or let voice alone unlock top-security. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: DESIGNED — Conditions not qualifying for a higher level receive `guest`. [V10 §25.2 / Access Levels]

TOGETHER
- Fed by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the calculated current level, based on SIA evidence and the applicable gates. [V10 §25.2 / Access Levels]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.3.1 — Top-security level | The four-level vocabulary. | Recognizes the highest level only under its combined factors. | Voice by itself never supplies that level. | [V10 §25.2 / Access Levels] |
| 2 · DESIGNED | C-OTHER.3.2 — Recognized-Ness level | The four-level vocabulary. | Distinguishes ordinary recognized access from top-security. | A biometric is not required for this level. | [V10 §25.2 / Access Levels] |
| 3 · DESIGNED | C-OTHER.3.3 — Known-person level | The four-level vocabulary. | Requires a confirmed non-Ness identity and active PBR. | Permission remains person-specific. | [V10 §25.2 / Access Levels] |
| 4 · DESIGNED | C-OTHER.3.4 — Guest level | The four-level vocabulary. | Handles conditions not qualifying for a higher level. | Disclosure stays at guest. | [V10 §25.2 / Access Levels] |

SUB-PARTS: C-OTHER.3.1 — Top-security level; C-OTHER.3.2 — Recognized-Ness level; C-OTHER.3.3 — Known-person level; C-OTHER.3.4 — Guest level

### C-OTHER.3.1 — Top-security level
Stamp: DESIGNED    Source: [V10 §25.2 / Access Levels]

ALONE
- What it is: DESIGNED — The `top_security` access level. [V10 §25.2 / Access Levels]
- Takes in: DESIGNED — Verified biometric and independently sufficient active-speaker recognition of Ness at high certainty, with no disqualifying suspicion. [V10 §25.2 / Protected Rules (Unconditional)]
- Does: DESIGNED — Requires both factors; absence of spoofing suspicion is part of this level's definition. [V10 §25.2 / Access Levels]
- Gives out: DESIGNED — Top-security disclosure authority only when its combined conditions hold. [V10 §25.2 / Access Levels]
- Must never: DESIGNED — Unlock top-security from voice alone or treat fingerprint verification as sufficient without independent speaker certainty. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: DESIGNED — Top-security remains locked if the active speaker is uncertain or suspicious after fingerprint success. [V10 §25.4 / Fingerprint as One Independent Factor]

TOGETHER
- Fed by: DESIGNED — C-OTHER.3 — Four access levels: the level vocabulary distinguishes the combined-factor level. [V10 §25.2 / Access Levels]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): Gate 1 requires the independent biometric and speaker factors rather than either alone. [V10 §25.4 / Fingerprint as One Independent Factor]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Biometric and speaker evidence. | Applies the combined-factor top-security condition. | Uncertain recognition cannot be repaired by fingerprint alone. | [V10 §25.4 / Fingerprint as One Independent Factor] |

SUB-PARTS: NONE

### C-OTHER.3.2 — Recognized-Ness level
Stamp: DESIGNED    Source: [V10 §25.2 / Access Levels]

ALONE
- What it is: DESIGNED — The `recognized_ness` level. [V10 §25.2 / Access Levels]
- Takes in: DESIGNED — Recognition of Ness at threshold certainty without disqualifying suspicion. [V10 §25.2 / Access Levels]
- Does: DESIGNED — Provides recognized access without requiring biometric verification. [V10 §25.2 / Access Levels]
- Gives out: DESIGNED — Ordinary recognized access; the separation rule retains it when behavioral `imitation_risk` blocks top-security. [V10 §25.5] [SOURCE CONFLICT: V10 §25.4 / Access Level Calculation, Gate 2, also names disqualifying imitation-risk flags.]
- Must never: DESIGNED — Turn this level into biometric-free top-security or use wellbeing tier to erase recognition. [V10 §25.2 / Protected Rules (Unconditional)] [V10 §25.5]
- Fails closed by: DESIGNED — Speaker uncertainty reduces permitted access rather than increasing it. [V10 §25.2 / Continuous Speaker Security]

TOGETHER
- Fed by: DESIGNED — C-OTHER.3 — Four access levels: the recognized-access classification is separate from the combined-factor top level. [V10 §25.2 / Access Levels]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current identity/security calculation determines the level; wellbeing tier is not access evidence. [V10 §25.2 / Access Levels] [V10 §25.5]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Ness recognition and current suspicion. | Distinguishes recognized access from top-security. | No biometric requirement is added to ordinary recognized access. | [V10 §25.2 / Access Levels] |

SUB-PARTS: NONE

### C-OTHER.3.3 — Known-person level
Stamp: DESIGNED    Source: [V10 §25.2 / Access Levels]

ALONE
- What it is: DESIGNED — The `known_person` access level for a confirmed non-Ness identity. [V10 §25.2 / Access Levels]
- Takes in: DESIGNED — A confirmed non-Ness Person-Box recognized at threshold and a valid active PBR. [V10 §25.2 / Access Levels]
- Does: DESIGNED — Associates the recognized speaker with that person's permission boundary. [V10 §25.2 / Access Levels]
- Gives out: DESIGNED — Known-person access bounded by the active PBR. [V10 §25.2 / Known-Person Permissions]
- Must never: DESIGNED — Transfer another person's permissions or treat a confirmed identity as unlimited disclosure authority. [V10 §25.2 / Protected Rules (Unconditional)] [V10 §25.2 / Known-Person Permissions]
- Fails closed by: DESIGNED — A failed PBR query closes Gate 3 and reduces the stream to guest. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]

TOGETHER
- Fed by: DESIGNED — C-OTHER.3 — Four access levels: the confirmed non-Ness classification; C-7L.9 — Person-Box permission-boundary read interface: the active person's permission record. [V10 §25.2 / Access Levels] [V10 §25.4 / Permission Boundary Enforcement]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): recognized non-Ness identity and a valid active PBR must satisfy the known-person gate. [V10 §25.4 / Access Level Calculation]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The confirmed person and their PBR. | Applies the known-person conditions and category limits. | A failed PBR read grants no elevation. | [V10 §25.4 / Access Level Calculation] [V10 §25.4 / Permission Boundary Enforcement] |

SUB-PARTS: NONE

### C-OTHER.3.4 — Guest level
Stamp: DESIGNED    Source: [V10 §25.2 / Access Levels]

ALONE
- What it is: DESIGNED — The `guest` level for all other conditions. [V10 §25.2 / Access Levels]
- Takes in: DESIGNED — A speaker who does not meet the applicable higher-level conditions. [V10 §25.2 / Access Levels]
- Does: DESIGNED — Limits disclosure to guest-permitted material while keeping the whole mechanism active. [V10 §25.2 / Access Levels]
- Gives out: DESIGNED — Guest access. [V10 §25.2 / Access Levels]
- Must never: DESIGNED — Expose private Ness memory or imply hidden information exists. [V10 §25.2 / Guest Mode]
- Fails closed by: DESIGNED — Guest is the fallback when higher access is not established. [V10 §25.2 / Access Levels]

TOGETHER
- Fed by: DESIGNED — C-OTHER.3 — Four access levels: the fallback classification. [V10 §25.2 / Access Levels]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.4 — Guest conversational response | The guest result. | Responds naturally from permitted general material. | Private Ness content remains inaccessible to the speaker. | [V10 §25.2 / Guest Mode] |

SUB-PARTS: NONE

### C-OTHER.4 — Guest conversational response
Stamp: DESIGNED    Source: [V10 §25.2 / Guest Mode]

ALONE
- What it is: DESIGNED — General conversational capability under guest disclosure limits. [V10 §25.2 / Guest Mode]
- Takes in: DESIGNED — The guest's interaction and available permitted content. [V10 §25.2 / Guest Mode]
- Does: DESIGNED — Forms a natural response from available content, without accessing shared-store Ness-personal material for the guest. [V10 §25.2 / Guest Mode]
- Gives out: DESIGNED — A response that carries no signal of hidden private material. [V10 §25.2 / Guest Mode]
- Must never: DESIGNED — Say “I cannot tell you” to acknowledge hidden material, disclose private Ness memory or expose that more is stored. [V10 §25.2 / Guest Mode]
- Fails closed by: DESIGNED — Material beyond permitted access is withheld; the response uses permitted content only and signals no hidden remainder. [V10 §25.4 / Output Gate (Two Factors, Sequential)]

TOGETHER
- Fed by: DESIGNED — C-OTHER.3.4 — Guest level: the current guest classification. [V10 §25.2 / Guest Mode]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): guest-level limits remain binding at output; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the privacy gate must pass first. [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-OTHER.13 — Current disclosure limits | The guest response formed from permitted material. | Keeps it within the privacy-first, access-second output boundary. | No private-memory signal is exposed at delivery. | [V10 §25.2 / Guest Mode] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-OTHER.5 — Known-person permission boundaries
Stamp: DESIGNED    Source: [V10 §25.2 / Known-Person Permissions]

ALONE
- What it is: DESIGNED — The PBR-based boundary for disclosure to each known person. [V10 §25.2 / Known-Person Permissions]
- Takes in: DESIGNED — Ness's expressed boundaries, learned evidence and the active PBR's `permission_categories`. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Does: DESIGNED — Maintains PBRs under protected authority; the initial open-ended category vocabulary is `family_information`, `health_information`, `nh_project_information`, `creative_projects`, `current_plans`, `shared_memories`, `practical_information`. [V10 §25.2 / Known-Person Permissions]
- Gives out: DESIGNED — The person's active permission categories for checking at output time. [V10 §25.4 / Permission Boundary Enforcement]
- Must never: DESIGNED — Give another person authority over PBRs, let Ness's expressed boundary override the protected core, or grant every listed category merely because it exists in the vocabulary. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Fails closed by: DESIGNED — Content outside the active PBR's permitted categories is not surfaced. [V10 §25.4 / Permission Boundary Enforcement]

TOGETHER
- Fed by: DESIGNED — C-7L.9.1 — Person-Box permission categories: the person's actual permitted category values; C-7L.9 — Person-Box permission-boundary read interface: the active version is obtained through LMAC. [V10 §25.4 / Permission Boundary Enforcement]
- Gated by: DESIGNED — C-7P — Permission & Authority Boundaries (§7P): PBR maintenance is constrained by protected authority; C-SACL — Speaker Access-Control Layer (§25.4): each output must pass the active category check. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The active PBR categories. | Checks the current output against them. | Out-of-category material is not disclosed. | [V10 §25.4 / Permission Boundary Enforcement] |

SUB-PARTS: NONE

### C-OTHER.6 — Separate parent records
Stamp: DESIGNED    Source: [V10 §25.2 / Separate Parent Identities]

ALONE
- What it is: DESIGNED — The separate identity context used for each parent. [V10 §25.2 / Separate Parent Identities]
- Takes in: DESIGNED — Each parent's own Person-Box, voice profile, behavioral pattern readings, PBR, relationship context in the Living State Web and translation behavior history. [V10 §25.2 / Separate Parent Identities]
- Does: DESIGNED — Preserves separation across all six kinds of record and context. [V10 §25.2 / Separate Parent Identities]
- Gives out: DESIGNED — Individually scoped parent context and permission boundaries. [V10 §25.2 / Separate Parent Identities]
- Must never: DESIGNED — Treat the parents as one combined person. [V10 §25.2 / Separate Parent Identities]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-7L.9.4 — Separate parent Person-Box identities: the canonical independently scoped parent identities and associated records. [V10 §25.2 / Separate Parent Identities]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.7 — Request-driven parent translation | The particular parent's context and translation history. | Interprets or adapts wording for that individual. | The other parent's identity or permissions are not substituted. | [V10 §25.2 / Separate Parent Identities] [V10 §25.2 / Parent Translation] |

SUB-PARTS: NONE

### C-OTHER.7 — Request-driven parent translation
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — Translation assistance initiated by Ness for a particular parent interaction. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — Ness's request to understand a parent's statement, prepare wording for that parent or deliver specified content to that parent. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Selects the requested kind of assistance; preserves the particular parent's context and keeps interpretation, private wording assistance and actual speech to the parent distinct. [V10 §25.2 / Parent Translation] [V10 §25.2 / Separate Parent Identities]
- Gives out: DESIGNED — A private uncertain interpretation, private candidate wordings, or the requested content delivered with in-scope tone and wording adaptation. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Autonomously join, intervene in or redirect a family conversation; speak to a parent when only private wording assistance was requested. [V10 §25.2 / Parent Translation]
- Fails closed by: DESIGNED — Does not begin parent translation without Ness's request. [V10 §25.2 / Parent Translation]

TOGETHER
- Fed by: DESIGNED — C-OTHER.6 — Separate parent records: the requested parent's distinct context and translation history. [V10 §25.2 / Separate Parent Identities]
- Gated by: DESIGNED — C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2): the recipient's disclosure boundary must permit the requested delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorized internal use and permitted visible purpose remain separate. [V10 §25.2 / Parent Translation] [V10 §25.2 / Protected Rules (Unconditional)]
- Gated by: DESIGNED — Ness's request is required; the request authorizes its stated assistance scope, not autonomous intervention. [V10 §25.2 / Parent Translation]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.7.1 — Interpret a parent's statement for Ness | A request to understand the parent's meaning. | Gives Ness an uncertain interpretation privately. | The parent is not addressed. | [V10 §25.2 / Parent Translation] |
| 2 · DESIGNED | C-OTHER.7.2 — Prepare private candidate wordings | A request for wording to use with the parent. | Offers candidates to Ness privately. | No speech to the parent is authorized by this branch. | [V10 §25.2 / Parent Translation] |
| 3 · DESIGNED | C-OTHER.7.3 — Deliver requested content to a parent | Ness's request that N.H speak to the parent. | Delivers the specified content with in-scope adaptation. | Only the explicitly requested intervention occurs. | [V10 §25.2 / Parent Translation] |
| 4 · DESIGNED | C-OTHER.7.4 — Translation reading and revision | The translation output. | Keeps it as a revisable reading. | Interpretation does not become immutable truth about the parent. | [V10 §25.2 / Parent Translation] |
| 5 · DESIGNED | C-OTHER.7.5 — Private translation context and bounded disclosure | Private context relevant to requested translation. | Separates internal understanding from what the parent may receive. | Private context creates no broader disclosure grant. | [V10 §25.2 / Parent Translation] |

SUB-PARTS: C-OTHER.7.1 — Interpret a parent's statement for Ness; C-OTHER.7.2 — Prepare private candidate wordings; C-OTHER.7.3 — Deliver requested content to a parent; C-OTHER.7.4 — Translation reading and revision; C-OTHER.7.5 — Private translation context and bounded disclosure

### C-OTHER.7.1 — Interpret a parent's statement for Ness
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — The “What did [parent] mean?” translation branch. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — The parent's statement and Ness's request to understand it. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Obtains a Meaning Engine reading and presents it as N.H's interpretation with uncertainty. [V10 §25.2 / Parent Translation]
- Gives out: DESIGNED — The interpretation delivered to Ness only. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Present the reading as the parent's established inner state or deliver this private interpretation to the parent. [V10 §25.2 / Parent Translation] [V10 §7Q]
- Fails closed by: DESIGNED — Waits for the translation request and applicable third-party authorization. [V10 §25.2 / Parent Translation] [V10 §7Q]

TOGETHER
- Fed by: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading of the parent's statement. [V10 §25.2 / Parent Translation]
- Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.7.4 — Translation reading and revision | The uncertain interpretation. | Preserves its reading identity and revision route. | A later reread can reconsider the interpretation. | [V10 §25.2 / Parent Translation] |

SUB-PARTS: NONE

### C-OTHER.7.2 — Prepare private candidate wordings
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — The “How should I say X to [parent]?” branch. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — The content Ness wants to convey and the request for candidate wordings. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Prepares possible wordings for Ness to use. [V10 §25.2 / Parent Translation]
- Gives out: DESIGNED — Candidates delivered privately to Ness. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Speak to the parent as a consequence of this wording-assistance request. [V10 §25.2 / Parent Translation]
- Fails closed by: DESIGNED — Does not convert a private preparation request into outward speech. [V10 §25.2 / Parent Translation]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness's request must select private wording assistance, and delivery remains private. [V10 §25.2 / Parent Translation]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.7.4 — Translation reading and revision | The private wording-assistance output. | Retains translation output as a revisable reading. | The output does not authorize speaking to the parent. | [V10 §25.2 / Parent Translation] |

SUB-PARTS: NONE

### C-OTHER.7.3 — Deliver requested content to a parent
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — The branch in which Ness explicitly asks N.H to speak to the parent. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — Ness's requested content and its intended parent recipient. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Delivers that content with automatic tone and wording adaptation limited to the request scope. [V10 §25.2 / Parent Translation]
- Gives out: DESIGNED — The requested parent-facing communication within the parent's permitted categories. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Expand the request into autonomous intervention or reveal private Ness context outside the parent's PBR. [V10 §25.2 / Parent Translation]
- Fails closed by: DESIGNED — Withholds content outside the current privacy or access boundary. [V10 §25.4 / Output Gate (Two Factors, Sequential)]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must explicitly request speech to the parent; C-SACL — Speaker Access-Control Layer (§25.4): the parent-facing content must pass current PBR limits; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization must pass before the access gate. [V10 §25.2 / Parent Translation] [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.7.4 — Translation reading and revision | The requested translation output. | Keeps its reading and revision identity. | Later interpretation does not rewrite the original output. | [V10 §25.2 / Parent Translation] [V10 §7H] |

SUB-PARTS: NONE

### C-OTHER.7.4 — Translation reading and revision
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — The stored-reading status of translation output. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — Translation output from the requested assistance branch. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Keeps translation output as a reading in the shared store, revisable through the reread lifecycle. [V10 §25.2 / Parent Translation]
- Gives out: DESIGNED — A reading available for later permitted reconsideration. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Present an interpretation as a final fact or rewrite the original reading when later evidence changes the understanding. [V10 §25.2 / Statements About Ness] [V10 §7H]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-OTHER.7 — Request-driven parent translation: the authorized translation output; C-OTHER.7.1 — Interpret a parent's statement for Ness: the uncertain interpretation; C-OTHER.7.2 — Prepare private candidate wordings: private wording candidates; C-OTHER.7.3 — Deliver requested content to a parent: the requested communication. [V10 §25.2 / Parent Translation]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-7H — Reread Lifecycle (§7H): the translation reading remains eligible for source-governed revision through rereading. [V10 §25.2 / Parent Translation]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7H — Reread Lifecycle (§7H), CY-F | A translation reading and later relevant evidence. | Reconsiders meaning through the reread route. | The original reading remains preserved. | [V10 §25.2 / Parent Translation] [V10 §7H] |

SUB-PARTS: NONE

### C-OTHER.7.5 — Private translation context and bounded disclosure
Stamp: DESIGNED    Source: [V10 §25.2 / Parent Translation]

ALONE
- What it is: DESIGNED — The separation between private translation context and the parent's disclosure permission. [V10 §25.2 / Parent Translation]
- Takes in: DESIGNED — Private Ness context relevant to understanding the requested interaction and the parent's active PBR categories. [V10 §25.2 / Parent Translation]
- Does: DESIGNED — Allows privacy-authorized internal understanding to use private context while limiting what reaches the parent to their permitted categories. [V10 §25.2 / Parent Translation] [V10 §25.2 / Protected Rules (Unconditional)]
- Gives out: DESIGNED — Context-informed translation without a transfer of private-memory access. [V10 §25.2 / Parent Translation]
- Must never: DESIGNED — Expose internal private context merely because it helped form the response. [V10 §25.2 / Parent Translation]
- Fails closed by: DESIGNED — Content outside privacy or access permission is withheld without acknowledging a hidden remainder. [V10 §25.4 / Output Gate (Two Factors, Sequential)]

TOGETHER
- Fed by: DESIGNED — C-OTHER.7 — Request-driven parent translation: the requested use and recipient; C-7L.9.1 — Person-Box permission categories: the parent's permitted categories. [V10 §25.2 / Parent Translation]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the internal purpose must be authorized; C-SACL — Speaker Access-Control Layer (§25.4): external disclosure is bounded independently at output. [V10 §25.2 / Protected Rules (Unconditional)] [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The proposed parent-facing output and active PBR. | Limits disclosure regardless of richer internal context. | No private context is exposed by inference or acknowledgment. | [V10 §25.2 / Parent Translation] [V10 §25.4 / Avoiding Indirect Disclosure] |

SUB-PARTS: NONE

### C-OTHER.8 — Statements about Ness retain their speaker
Stamp: DESIGNED    Source: [V10 §25.2 / Statements About Ness]

ALONE
- What it is: DESIGNED — The continuous source-attribution boundary for another person's statement about Ness. [V10 §25.2 / Statements About Ness]
- Takes in: DESIGNED — A third-party statement, its speaker and the session context. [V10 §25.2 / Statements About Ness]
- Does: DESIGNED — Carries that speaker through the TSC, promoted root and Meaning Engine reading. Later evidence may trigger rereading; the original root and reading remain unaltered. [V10 §25.2 / Statements About Ness]
- Gives out: DESIGNED — An attributed statement and any later attributed interpretation, rather than an unqualified fact about Ness. [V10 §25.2 / Statements About Ness]
- Must never: DESIGNED — Silently convert a third-party claim into a fact about Ness, strip the speaker or rewrite the original root or reading. [V10 §25.2 / Statements About Ness]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): the attributed statement and complete context persist through authorized promotion. [V10 §25.2 / Statements About Ness] [V10 §25.2 / Temporary Session Cache]
- Gated by: DESIGNED — C-7Q.5 — Third-party data baseline: actual words, Ness's interpretation and N.H's interpretation remain distinguishable; inference is not fact. [V10 §7Q]
- Changes: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading keeps the original speaker attribution; C-7H — Reread Lifecycle (§7H): later evidence may cause a new reading without altering the earlier records. [V10 §25.2 / Statements About Ness]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | Another person's statement about Ness. | Preserves the speaker and meaningful surrounding context. | The statement is not reassigned to Ness. | [V10 §25.2 / Statements About Ness] |
| 2 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | The attributed promoted root. | Reads it as a claim from that speaker. | Its reading does not silently establish a fact about Ness. | [V10 §25.2 / Statements About Ness] |
| 3 · DESIGNED | C-7H — Reread Lifecycle (§7H), CY-F | Later evidence concerning the statement. | May reread the original material. | Original root and reading remain unchanged. | [V10 §25.2 / Statements About Ness] |

SUB-PARTS: NONE

### C-OTHER.9 — Person-Box visibility for other speakers
Stamp: DESIGNED    Source: [V10 §25.2 / Person-Box Visibility]

ALONE
- What it is: DESIGNED — The other speaker's restricted view of person-related information. [V10 §25.2 / Person-Box Visibility]
- Takes in: DESIGNED — The person's request and current speaker access level. [V10 §25.2 / Person-Box Visibility]
- Does: DESIGNED — Answers from only what the current level permits. [V10 §25.2 / Person-Box Visibility]
- Gives out: DESIGNED — A permitted answer that does not expose the extent or mechanics of recognition and storage. [V10 §25.2 / Person-Box Visibility]
- Must never: DESIGNED — Allow another person to inspect their full Person-Box, hidden readings, private observations, internal relationship models or stored security information; reveal how much is stored or how recognition works. [V10 §25.2 / Person-Box Visibility]
- Fails closed by: DESIGNED — Withholds material outside current access without signaling hidden content. [V10 §25.2 / Person-Box Visibility] [V10 §25.2 / Protected Rules (Unconditional)]

TOGETHER
- Fed by: DESIGNED — C-7L.9.3 — Person-Box visibility restriction: the canonical person-information disclosure boundary. [V10 §25.2 / Person-Box Visibility]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): current speaker access limits the answer. [V10 §25.2 / Person-Box Visibility]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | A proposed answer concerning a person's records. | Applies the current permission boundary without full-box access. | Stored extent and recognition mechanics remain undisclosed. | [V10 §25.2 / Person-Box Visibility] |

SUB-PARTS: NONE

### C-OTHER.10 — Third-party cache boundary
Stamp: DESIGNED    Source: [V10 §25.2 / Temporary Session Cache]

ALONE
- What it is: DESIGNED — The holding boundary for third-party session material before authorized long-term processing. [V10 §25.2 / Temporary Session Cache]
- Takes in: DESIGNED — The complete third-party session context, including Ness's words where they give meaning to another person's statements. [V10 §25.2 / Temporary Session Cache]
- Does: DESIGNED — Uses the Catalog pre-ingest holding area with `pending_fingerprint_authorization`; held material is invisible to the Meaning Engine. Normal closure moves `active` to `sealed`; a crash moves it to separately sealed `interrupted`. Both wait indefinitely. Authorization permits `authorized` → `promoting` → `promoted` or `promotion_failed`; successful retained-archive creation moves `promoted` to `archived`. Separate authorization alone may move `archived` to `permanently_sealed`. [V10 §25.2 / Temporary Session Cache]
- Gives out: DESIGNED — Held session material or authorized promotion results with their lifecycle state preserved. [V10 §25.2 / Temporary Session Cache]
- Must never: DESIGNED — Auto-expire, auto-delete or auto-promote a waiting cache; silently discard context needed for attribution; permanently seal automatically; introduce a `deleted` lifecycle state. [V10 §25.2 / Temporary Session Cache]
- Fails closed by: DESIGNED — Without session authorization, the sealed or interrupted cache remains held and unavailable to Meaning Engine processing. [V10 §25.2 / Temporary Session Cache]

TOGETHER
- Fed by: DESIGNED — C-TSC.12 — Session and item lifecycles: the existing state and transition atoms retain the session's actual lifecycle. [V10 §25.2 / Temporary Session Cache]
- Gated by: DESIGNED — C-TSC.16 — Session authorization: the relevant completed session must be authorized before promotion; C-TSC.23 — Retained archive: permanent sealing requires its separate authorization. [V10 §25.2 / Temporary Session Cache]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.11 — Completed-session batch authorization | The complete pending cache from the relevant completed session. | Uses the session as the authorization unit. | Unrelated caches are not included. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |

SUB-PARTS: NONE

### C-OTHER.11 — Completed-session batch authorization
Stamp: DESIGNED    Source: [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

ALONE
- What it is: DESIGNED — Authorization of the complete pending TSC belonging to one relevant completed session. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Takes in: DESIGNED — That completed session's pending cache and Ness's thumbprint in a later session. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Does: DESIGNED — Authorizes the session as a unit; items with no remaining blockers then proceed under the existing evidence rules without additional manual Ness approval. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gives out: DESIGNED — A session-authorized batch whose individually unblocked items may proceed. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Must never: DESIGNED — Select individual people, memories or items as the authorization unit; automatically include unrelated sealed caches; or treat fingerprint success as removal of every other blocker. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Fails closed by: DESIGNED — Waiting material does not promote before authorization, and remaining blockers continue to hold affected items. [V10 §25.2 / Temporary Session Cache] [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

TOGETHER
- Fed by: DESIGNED — C-OTHER.10 — Third-party cache boundary: the complete held cache from the relevant completed session. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gated by: DESIGNED — C-TSC.16 — Session authorization: the session's fingerprint authorization is required; C-TSC.11 — Blockers and resolution history: every remaining blocker must be clear for the affected item to proceed. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Changes: DESIGNED — C-TSC.17 — Ordered promotion: the authorized, unblocked material is eligible for the established promotion route. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.11.1 — Session-sized permission | The relevant completed session's authorization. | Preserves the complete cache as the permission unit. | No unrelated session is included. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |
| 2 · DESIGNED | C-OTHER.11.2 — Unblocked items proceed automatically | The authorized batch. | Lets only items without remaining blockers continue. | No second manual approval is added. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |
| 3 · DESIGNED | C-OTHER.11.3 — Attributed promotion route | The authorized unblocked items. | Carries their attribution into downstream reading. | The source's two differing downstream-route descriptions remain visible. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [MAP C-OTHER] |

SUB-PARTS: C-OTHER.11.1 — Session-sized permission; C-OTHER.11.2 — Unblocked items proceed automatically; C-OTHER.11.3 — Attributed promotion route

### C-OTHER.11.1 — Session-sized permission
Stamp: DESIGNED    Source: [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

ALONE
- What it is: DESIGNED — The scope of the later thumbprint authorization. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Takes in: DESIGNED — The complete pending cache of the relevant completed session. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Does: DESIGNED — Keeps the session, rather than a person, memory or selected item, as the authorization unit. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gives out: DESIGNED — Permission scoped to that completed session alone. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Must never: DESIGNED — Automatically promote an unrelated sealed cache or fragment the session into individual authorization choices. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Fails closed by: DESIGNED — Other sessions retain their own authorization requirement. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

TOGETHER
- Fed by: DESIGNED — C-OTHER.11 — Completed-session batch authorization: the current session authorization and its cache scope. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-TSC.16 — Session authorization | The relevant completed session. | Binds authorization to that cache as a whole. | Other caches do not inherit the permission. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |

SUB-PARTS: NONE

### C-OTHER.11.2 — Unblocked items proceed automatically
Stamp: DESIGNED    Source: [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

ALONE
- What it is: DESIGNED — Post-authorization processing of items without remaining blockers. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Takes in: DESIGNED — Authorized cache items and each item's unresolved blockers. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Does: DESIGNED — Sends unblocked items through the established evidence-processing route without another manual Ness approval. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gives out: DESIGNED — Eligible promoted material; items with blockers remain held. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Must never: DESIGNED — Bypass a remaining blocker or require additional manual approval merely because the authorized material is from another speaker. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Fails closed by: DESIGNED — An item does not proceed while any remaining blocker applies. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

TOGETHER
- Fed by: DESIGNED — C-OTHER.11 — Completed-session batch authorization: the authorized session batch. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gated by: DESIGNED — C-TSC.11 — Blockers and resolution history: all remaining blockers for the item must be clear. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Changes: DESIGNED — C-TSC.17 — Ordered promotion: eligible items enter the existing ordered processing operation. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-TSC.17 — Ordered promotion | Session-authorized items with no remaining blockers. | Processes them under the settled evidence rules. | No further manual approval is inserted. | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |

SUB-PARTS: NONE

### C-OTHER.11.3 — Attributed promotion route
Stamp: DESIGNED    Source: [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [MAP C-OTHER]

ALONE
- What it is: DESIGNED — The source-described downstream route for session-authorized third-party material. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Takes in: DESIGNED — Authorized items with no remaining blockers and their original speaker attribution. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [V10 §25.2 / Statements About Ness]
- Does: DESIGNED — Routes authorized material through Catalog → sealed store → Meaning Engine → readings → Clash Handling → Computed View → Person-Box proposals. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [SOURCE CONFLICT: MAP C-OTHER instead uses append_root() into the B11 active writable batch, never a sealed batch, then fans readings to §7J/§7K/§7L/§7D under their rules before §7M assembles permitted sources. V10's seal refusal is not relaxed.]
- Gives out: DESIGNED — Attributed roots/readings and source-governed downstream proposals, without converting a speaker's statement into a fact about Ness. [V10 §25.2 / Statements About Ness] [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Must never: DESIGNED — Lose speaker attribution or infer permission to append to an existing sealed store from the route wording. [V10 §25.2 / Statements About Ness] [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Fails closed by: BUILT — Existing seal protection refuses `append_root()` while `.nh_roots.sealed` is present. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]

TOGETHER
- Fed by: DESIGNED — C-OTHER.11 — Completed-session batch authorization: the complete authorized session, with only unblocked items proceeding. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]
- Gated by: DESIGNED — C-TSC.17 — Ordered promotion: existing promotion requirements apply; the conflicting route shorthand supplies no alternate operation. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [V10 §25.2 / Temporary Session Cache]
- Gated by: BUILT — C-STORE — Accretive store & sealed roots (§6B): `.nh_roots.sealed` blocks `append_root()`; the promotion route does not lift the seal. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER]
- Changes: DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): receives attributed promoted material for reading. [V10 §25.2 / Fingerprint-Authorized Batch Promotion]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G), CY-D | Authorized, attributed promoted roots. | Produces readings retaining the source speaker. | A third-party claim is not silently turned into a fact about Ness. | [V10 §25.2 / Statements About Ness] [V10 §25.2 / Fingerprint-Authorized Batch Promotion] |

SUB-PARTS: NONE

### C-OTHER.12 — Continuous speaker security
Stamp: DESIGNED    Source: [V10 §25.2 / Continuous Speaker Security]

ALONE
- What it is: DESIGNED — Continuous identity/security assessment during an interaction. [V10 §25.2 / Continuous Speaker Security]
- Takes in: DESIGNED — SIA assessments, speaker changes and acoustic suspicion. [V10 §25.2 / Continuous Speaker Security]
- Does: DESIGNED — Recalculates access immediately when the speaker changes, reduces access when uncertain, and applies the acoustic-spoofing guest/alert rule. [V10 §25.2 / Continuous Speaker Security]
- Gives out: DESIGNED — Current speaker-bounded access throughout the session. [V10 §25.2 / Continuous Speaker Security]
- Must never: DESIGNED — Expand access under uncertainty or issue routine live voice challenges. [V10 §25.2 / Continuous Speaker Security]
- Fails closed by: DESIGNED — SACL restart returns all streams to guest and discards in-progress operations; PBR query failure closes Gate 3. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]

TOGETHER
- Fed by: DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and acoustic-security evidence. [V10 §25.2 / Continuous Speaker Security]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): current assessments determine the access ceiling and fail-closed outcome. [V10 §25.2 / Continuous Speaker Security]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-OTHER.12.1 — Uncertainty lowers access | Current uncertain speaker evidence. | Applies the restrictive access direction. | No uncertainty-derived elevation occurs. | [V10 §25.2 / Continuous Speaker Security] |
| 2 · DESIGNED | C-OTHER.12.2 — Speaker-change recalculation | A changed active speaker. | Recalculates access immediately. | The previous speaker's permission is not inherited. | [V10 §25.2 / Continuous Speaker Security] |
| 3 · DESIGNED | C-OTHER.12.3 — Acoustic-suspicion guest outcome | Acoustic suspicion or the spoofing flag. | Applies Gate 0 and its separate alert condition. | Guest access and any required private alert follow. | [V10 §25.4 / Access Level Calculation] |

SUB-PARTS: C-OTHER.12.1 — Uncertainty lowers access; C-OTHER.12.2 — Speaker-change recalculation; C-OTHER.12.3 — Acoustic-suspicion guest outcome

### C-OTHER.12.1 — Uncertainty lowers access
Stamp: DESIGNED    Source: [V10 §25.2 / Continuous Speaker Security]

ALONE
- What it is: DESIGNED — The restrictive direction of uncertain speaker evidence. [V10 §25.2 / Continuous Speaker Security]
- Takes in: DESIGNED — Current identity uncertainty, stale assessment or SIA failure. [V10 §25.2 / Continuous Speaker Security] [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]
- Does: DESIGNED — Reduces access instead of expanding it; stale assessments downgrade streams above guest, add `assessment_stale` and keep SACL at guest until fresh output. SIA failure sends all streams to guest and immediately writes an audit event. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]
- Gives out: DESIGNED — Restricted access pending fresh sufficient evidence. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]
- Must never: DESIGNED — Treat uncertainty or missing fresh evidence as an access grant. [V10 §25.2 / Continuous Speaker Security]
- Fails closed by: DESIGNED — Stale or failed assessment leaves guest access rather than preserving higher access. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]

TOGETHER
- Fed by: DESIGNED — C-OTHER.12 — Continuous speaker security: current evidence and assessment availability. [V10 §25.2 / Continuous Speaker Security]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): uncertain, stale or failed evidence reduces the current access level. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Stale or failed SIA evidence. | Downgrades rather than extrapolating authorization. | Guest access remains until fresh evidence supports more. | [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] |

SUB-PARTS: NONE

### C-OTHER.12.2 — Speaker-change recalculation
Stamp: DESIGNED    Source: [V10 §25.2 / Continuous Speaker Security]

ALONE
- What it is: DESIGNED — The immediate access response to a changed speaker. [V10 §25.2 / Continuous Speaker Security]
- Takes in: DESIGNED — A speaker change during the session. [V10 §25.2 / Continuous Speaker Security]
- Does: DESIGNED — Recalculates access immediately from the current speaker evidence. [V10 §25.2 / Continuous Speaker Security]
- Gives out: DESIGNED — Access belonging to the current speaker rather than the previous speaker. [V10 §25.2 / Continuous Speaker Security]
- Must never: DESIGNED — Transfer the previous speaker's permissions to the new speaker. [V10 §25.2 / Protected Rules (Unconditional)]
- Fails closed by: DESIGNED — Any resulting uncertainty reduces access. [V10 §25.2 / Continuous Speaker Security]

TOGETHER
- Fed by: DESIGNED — C-OTHER.12 — Continuous speaker security: the changed-speaker evidence. [V10 §25.2 / Continuous Speaker Security]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the access calculation is refreshed immediately. [V10 §25.2 / Continuous Speaker Security]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | A changed current speaker. | Recalculates the applicable access. | Previous-speaker authority does not carry over. | [V10 §25.2 / Continuous Speaker Security] |

SUB-PARTS: NONE

### C-OTHER.12.3 — Acoustic-suspicion guest outcome
Stamp: DESIGNED    Source: [V10 §25.4 / Access Level Calculation]

ALONE
- What it is: DESIGNED — Gate 0's acoustic-security outcome for an affected stream. [V10 §25.4 / Access Level Calculation]
- Takes in: DESIGNED — `anti_spoofing.suspicion_level` equal to `medium` or `high`, or `active_flags` containing `spoofing_suspected`. [V10 §25.4 / Access Level Calculation]
- Does: DESIGNED — Sets `stream_access_level` to `guest` and stops the gate calculation; medium-or-higher suspicion additionally queues a private Ness alert. A low-suspicion spoofing flag can therefore reduce access without that alert. [V10 §25.4 / Access Level Calculation] [MAP C-OTHER]
- Gives out: DESIGNED — Guest access and, only for medium/high suspicion, the required private alert. [V10 §25.4 / Access Level Calculation]
- Must never: DESIGNED — Use `imitation_risk` as a Gate 0 trigger or conflate behavioral divergence with acoustic spoofing. [V10 §25.4 / Access Level Calculation] [V10 §25.5]
- Fails closed by: DESIGNED — The trigger sends the affected stream to guest immediately. [V10 §25.4 / Access Level Calculation]

TOGETHER
- Fed by: DESIGNED — C-OTHER.12 — Continuous speaker security: the current acoustic suspicion and flags. [V10 §25.2 / Continuous Speaker Security]
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 terminates the access calculation at guest and queues the alert under its distinct condition. [V10 §25.4 / Access Level Calculation]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | The current acoustic-security trigger. | Applies Gate 0 without consulting wellbeing state. | Guest access and the conditional private alert result. | [V10 §25.4 / Access Level Calculation] [V10 §25.5] |

SUB-PARTS: NONE

### C-OTHER.13 — Current disclosure limits
Stamp: ACCEPTED    Source: [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The other-speaker output boundary enforced by the existing privacy-first, access-second delivery chain. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The response made from permitted material, current stream access, active PBR and the output path's observability. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Uses the shared minimum on shared/observable output, an individual level only on an owner-confirmed private unobservable path, and current PBR categories and presence requirements at output time. Privacy precedes relevance; the final privacy gate precedes final SACL. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — Output permitted by both final gates for the actual current path. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3]
- Must never: ACCEPTED — Let Personal Mode make a shared path private, reverse gate order, treat one pass as the other, or reveal hidden content through wording, structural gaps or implied omission. A mouth-provider refusal is recorded separately as a mouth limitation; it is neither an N.H privacy rule nor evidence that the material is forbidden. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — PBR failure or uncertainty closes disclosure; missing, stale or unverifiable PBRs, unmet Ness-presence, unavailable authority or incompatible current owner facts block the output. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §14]

TOGETHER
- Fed by: DESIGNED — C-OTHER.4 — Guest conversational response: the guest response contains only permitted content; C-SACL — Speaker Access-Control Layer (§25.4): current access and PBR limits. [V10 §25.2 / Guest Mode] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gated by: ACCEPTED — C-7Q.11.3 — Exact-payload privacy and output revalidation: the exact output must satisfy the current privacy and revalidation boundary. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the final current access/PBR gate must pass after privacy. [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-OTHER.13.1 — Shared and private output ceilings | Current active streams and path observability. | Selects the correct shared or individual ceiling. | A shared path cannot inherit a private ceiling. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |
| 2 · ACCEPTED | C-OTHER.13.2 — PBR and Ness-presence revalidation | Current PBR categories and required Ness presence. | Checks them at output time. | Failure or presence loss restricts disclosure immediately. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |
| 3 · ACCEPTED | C-OTHER.13.3 — Two sequential disclosure gates | The current exact answer. | Requires privacy first and access second. | No one-gate shortcut delivers. | [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3] |

SUB-PARTS: C-OTHER.13.1 — Shared and private output ceilings; C-OTHER.13.2 — PBR and Ness-presence revalidation; C-OTHER.13.3 — Two sequential disclosure gates

### C-OTHER.13.1 — Shared and private output ceilings
Stamp: ACCEPTED    Source: [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The current-path ceiling for shared versus genuinely private output. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — `shared_output_level`, individual stream access and owner-confirmed path observability. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Uses the minimum access level across active streams for shared/observable output; an individual level is usable only on a private and unobservable path confirmed by its owner. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — The permitted level for the actual output path. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Treat Personal Mode or a private intention as a change to the path's actual observability. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — Without owner-confirmed private unobservability, an individual stream's higher level cannot be used for shared output. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-OTHER.13 — Current disclosure limits: the current stream and path facts. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Current streams and the actual private/shared path. | Supplies the corresponding permitted output ceiling. | Shared output uses the minimum across streams. | [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-OTHER.13.2 — PBR and Ness-presence revalidation
Stamp: ACCEPTED    Source: [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — Output-time enforcement of the active known-person PBR and any Ness-presence requirement. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Takes in: ACCEPTED — The active PBR categories and whether the required Ness stream still has qualifying access. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Does: ACCEPTED — Checks the active categories for every output; where `ness_presence_required = true`, elevated known-person access lasts only while a Ness stream remains at `recognized_ness` or above. [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gives out: ACCEPTED — A currently valid category/presence result. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Must never: ACCEPTED — Preserve the known person's elevated access after required Ness presence is lost, or treat PBR uncertainty as permission. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Fails closed by: ACCEPTED — When Ness's qualifying stream drops below the required level, the known-person stream drops to guest simultaneously; PBR failure or uncertainty fails closed. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]

TOGETHER
- Fed by: ACCEPTED — C-OTHER.13 — Current disclosure limits: the active output's PBR and stream facts. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13]
- Gated by: DESIGNED — C-7L.9.2 — Person-Box Ness-presence permission condition: the PBR's required Ness presence must still hold. [V10 §25.4 / Multi-Speaker Sessions]
- Changes: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): required-presence loss reduces the known-person stream to guest at the same time. [V10 §25.4 / Multi-Speaker Sessions]

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The current PBR and required Ness-stream condition. | Enforces both for the actual output. | The known-person path loses elevation immediately on required-presence loss. | [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] |

SUB-PARTS: NONE

### C-OTHER.13.3 — Two sequential disclosure gates
Stamp: ACCEPTED    Source: [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The two-factor final delivery order for other-speaker output. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3]
- Takes in: ACCEPTED — The exact formed answer and the current privacy/access facts. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]
- Does: ACCEPTED — Applies final privacy review first, then current SACL access and PBR review. Both must approve the same output; changed or transformed content returns through both gates. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6D]
- Gives out: ACCEPTED — A currently permitted answer for the single existing delivery chain. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]
- Must never: ACCEPTED — Reverse or merge the gates, allow either gate to widen the other, deliver first and check later, or create a second output path around the restrictions. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §14]
- Fails closed by: ACCEPTED — Failure of either authorization prevents the affected output; a safer transformed answer must pass both checks anew. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §6D]

TOGETHER
- Fed by: ACCEPTED — C-OTHER.13 — Current disclosure limits: the actual response and current recipient/path context. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy review must pass first; C-SACL — Speaker Access-Control Layer (§25.4): final access and PBR review must then pass for the same answer. [V10 §25.4 / Output Gate (Two Factors, Sequential)]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | The privacy-approved exact answer and current access/PBR state. | Acts as the second final gate. | A privacy pass does not substitute for access permission. | [V10 §25.4 / Output Gate (Two Factors, Sequential)] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3] |

SUB-PARTS: NONE

### C-OTHER.14 — Other-speaker operational records
Stamp: CANDIDATE    Source: [MAP C-OTHER]

ALONE
- What it is: CANDIDATE — The producing mechanisms' operational record of other-speaker access and use. [MAP C-OTHER]
- Takes in: CANDIDATE — An access determination, permitted or withheld disclosure, PBR category check, translation request/delivery or third-party attribution carried through the path. [MAP C-OTHER]
- Does: CANDIDATE — Records each of those actual operations under the shared operational logging rule. [MAP C-OTHER]
- Gives out: CANDIDATE — Operational records subject to privacy and identity/security authorization. [MAP C-OTHER]
- Must never: CANDIDATE — Let record existence bypass the producing component's privacy or security access rules. [MAP C-OTHER]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to the records remains privacy-authorized; C-SACL — Speaker Access-Control Layer (§25.4): identity/security authorization remains required. [MAP C-OTHER] [V10 §0B]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-SACL — Speaker Access-Control Layer (§25.4) | Its actual access determination and category check. | Records the result and permitted/withheld disclosure. | No new permission is created by logging. | [MAP C-OTHER] [V10 §0B] |
| 2 · DESIGNED | C-TSC — Temporary Session Cache (§7E-TSC) | Third-party attribution along the held/promoted path. | Records the attribution actually carried. | Speaker provenance remains traceable. | [MAP C-OTHER] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

These continuation rows preserve the current TOGETHER relationships at their other endpoint. Earlier files are not edited. Future owners incorporate the rows when written; the register retains both exact endpoint names. Conditions and citations remain in the identified current field.

| USED BY owner | Using card | Current TOGETHER field | Exact current relationship | Disposition |
|---|---|---|---|---|
| C-SIA — Speaker Identity Assessment (§25.3) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and suspicion assessments; C-TSC — Temporary Session Cache (§7E-TSC): third-party material retains session context and speaker attribution; C-7L.9 — Person-Box permission-boundary read interface: the active person's PBR reference. [V10 §25.2] [MAP C-OTHER] | Pending endpoint placement |
| C-TSC — Temporary Session Cache (§7E-TSC) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and suspicion assessments; C-TSC — Temporary Session Cache (§7E-TSC): third-party material retains session context and speaker attribution; C-7L.9 — Person-Box permission-boundary read interface: the active person's PBR reference. [V10 §25.2] [MAP C-OTHER] | Pending endpoint placement |
| C-7L.9 — Person-Box permission-boundary read interface | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and suspicion assessments; C-TSC — Temporary Session Cache (§7E-TSC): third-party material retains session context and speaker attribution; C-7L.9 — Person-Box permission-boundary read interface: the active person's PBR reference. [V10 §25.2] [MAP C-OTHER] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current speaker level and category limits bound disclosure; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal use and visible disclosure need their own privacy authority; C-7P — Permission & Authority Boundaries (§7P): permissions cannot override the protected core. [V10 §25.2] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current speaker level and category limits bound disclosure; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal use and visible disclosure need their own privacy authority; C-7P — Permission & Authority Boundaries (§7P): permissions cannot override the protected core. [V10 §25.2] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7P — Permission & Authority Boundaries (§7P) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current speaker level and category limits bound disclosure; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal use and visible disclosure need their own privacy authority; C-7P — Permission & Authority Boundaries (§7P): permissions cannot override the protected core. [V10 §25.2] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-LMAC — Live Mechanism Access Coordinator (§26) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Changes | DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): requested retrieval remains inside current access and privacy limits; C-7L — Person-Boxes (§7L): authorized third-party readings may support person proposals without collapsing attribution into truth. [MAP C-OTHER] [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-7L — Person-Boxes (§7L) | C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | Changes | DESIGNED — C-LMAC — Live Mechanism Access Coordinator (§26): requested retrieval remains inside current access and privacy limits; C-7L — Person-Boxes (§7L): authorized third-party readings may support person proposals without collapsing attribution into truth. [MAP C-OTHER] [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.1 — Internal understanding and external disclosure | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal information use requires its own authorized purpose; C-7P — Permission & Authority Boundaries (§7P): processing stays within the applicable authority. [V10 §25.2 / Protected Rules (Unconditional)] | Pending endpoint placement |
| C-7P — Permission & Authority Boundaries (§7P) | C-OTHER.1 — Internal understanding and external disclosure | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): internal information use requires its own authorized purpose; C-7P — Permission & Authority Boundaries (§7P): processing stays within the applicable authority. [V10 §25.2 / Protected Rules (Unconditional)] | Pending endpoint placement |
| C-7P — Permission & Authority Boundaries (§7P) | C-OTHER.2 — Protected authority for other-speaker use | Gated by | DESIGNED — C-7P — Permission & Authority Boundaries (§7P): protected authority remains binding on the interaction and PBR maintenance. [V10 §25.2 / Known-Person Permissions] [V10 §25.2 / Protected Rules (Unconditional)] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.3 — Four access levels | Fed by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the calculated current level, based on SIA evidence and the applicable gates. [V10 §25.2 / Access Levels] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.3.1 — Top-security level | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): Gate 1 requires the independent biometric and speaker factors rather than either alone. [V10 §25.4 / Fingerprint as One Independent Factor] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.3.2 — Recognized-Ness level | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the current identity/security calculation determines the level; wellbeing tier is not access evidence. [V10 §25.2 / Access Levels] [V10 §25.5] | Pending endpoint placement |
| C-7L.9 — Person-Box permission-boundary read interface | C-OTHER.3.3 — Known-person level | Fed by | DESIGNED — C-OTHER.3 — Four access levels: the confirmed non-Ness classification; C-7L.9 — Person-Box permission-boundary read interface: the active person's permission record. [V10 §25.2 / Access Levels] [V10 §25.4 / Permission Boundary Enforcement] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.3.3 — Known-person level | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): recognized non-Ness identity and a valid active PBR must satisfy the known-person gate. [V10 §25.4 / Access Level Calculation] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.4 — Guest conversational response | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): guest-level limits remain binding at output; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the privacy gate must pass first. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.4 — Guest conversational response | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): guest-level limits remain binding at output; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the privacy gate must pass first. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7L.9.1 — Person-Box permission categories | C-OTHER.5 — Known-person permission boundaries | Fed by | DESIGNED — C-7L.9.1 — Person-Box permission categories: the person's actual permitted category values; C-7L.9 — Person-Box permission-boundary read interface: the active version is obtained through LMAC. [V10 §25.4 / Permission Boundary Enforcement] | Pending endpoint placement |
| C-7L.9 — Person-Box permission-boundary read interface | C-OTHER.5 — Known-person permission boundaries | Fed by | DESIGNED — C-7L.9.1 — Person-Box permission categories: the person's actual permitted category values; C-7L.9 — Person-Box permission-boundary read interface: the active version is obtained through LMAC. [V10 §25.4 / Permission Boundary Enforcement] | Pending endpoint placement |
| C-7P — Permission & Authority Boundaries (§7P) | C-OTHER.5 — Known-person permission boundaries | Gated by | DESIGNED — C-7P — Permission & Authority Boundaries (§7P): PBR maintenance is constrained by protected authority; C-SACL — Speaker Access-Control Layer (§25.4): each output must pass the active category check. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.5 — Known-person permission boundaries | Gated by | DESIGNED — C-7P — Permission & Authority Boundaries (§7P): PBR maintenance is constrained by protected authority; C-SACL — Speaker Access-Control Layer (§25.4): each output must pass the active category check. [V10 §25.2 / Known-Person Permissions] [V10 §25.4 / Permission Boundary Enforcement] | Pending endpoint placement |
| C-7L.9.4 — Separate parent Person-Box identities | C-OTHER.6 — Separate parent records | Fed by | DESIGNED — C-7L.9.4 — Separate parent Person-Box identities: the canonical independently scoped parent identities and associated records. [V10 §25.2 / Separate Parent Identities] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.7 — Request-driven parent translation | Gated by | DESIGNED — C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2): the recipient's disclosure boundary must permit the requested delivery; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): authorized internal use and permitted visible purpose remain separate. [V10 §25.2 / Parent Translation] [V10 §25.2 / Protected Rules (Unconditional)]; DESIGNED — Ness's request is required; the request authorizes its stated assistance scope, not autonomous intervention. [V10 §25.2 / Parent Translation] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-OTHER.7.1 — Interpret a parent's statement for Ness | Fed by | DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading of the parent's statement. [V10 §25.2 / Parent Translation] | Pending endpoint placement |
| C-7Q.5.3 — Four-operation third-party authorization ladder | C-OTHER.7.1 — Interpret a parent's statement for Ness | Gated by | DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must request this branch; C-7Q.5.3 — Four-operation third-party authorization ladder: V10's stronger-authorization requirement applies to interpretation. [V10 §25.2 / Parent Translation] [V10 §7Q] [SOURCE CONFLICT: A7 §§4.5/6.1 and B7 §3 allow ordinary bounded interpretation without separate permission.] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.7.3 — Deliver requested content to a parent | Gated by | DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must explicitly request speech to the parent; C-SACL — Speaker Access-Control Layer (§25.4): the parent-facing content must pass current PBR limits; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization must pass before the access gate. [V10 §25.2 / Parent Translation] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.7.3 — Deliver requested content to a parent | Gated by | DESIGNED — C-OTHER.7 — Request-driven parent translation: Ness must explicitly request speech to the parent; C-SACL — Speaker Access-Control Layer (§25.4): the parent-facing content must pass current PBR limits; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy authorization must pass before the access gate. [V10 §25.2 / Parent Translation] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7H — Reread Lifecycle (§7H) | C-OTHER.7.4 — Translation reading and revision | Changes | DESIGNED — C-7H — Reread Lifecycle (§7H): the translation reading remains eligible for source-governed revision through rereading. [V10 §25.2 / Parent Translation] | Pending endpoint placement |
| C-7L.9.1 — Person-Box permission categories | C-OTHER.7.5 — Private translation context and bounded disclosure | Fed by | DESIGNED — C-OTHER.7 — Request-driven parent translation: the requested use and recipient; C-7L.9.1 — Person-Box permission categories: the parent's permitted categories. [V10 §25.2 / Parent Translation] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.7.5 — Private translation context and bounded disclosure | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the internal purpose must be authorized; C-SACL — Speaker Access-Control Layer (§25.4): external disclosure is bounded independently at output. [V10 §25.2 / Protected Rules (Unconditional)] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.7.5 — Private translation context and bounded disclosure | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the internal purpose must be authorized; C-SACL — Speaker Access-Control Layer (§25.4): external disclosure is bounded independently at output. [V10 §25.2 / Protected Rules (Unconditional)] [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-TSC — Temporary Session Cache (§7E-TSC) | C-OTHER.8 — Statements about Ness retain their speaker | Fed by | DESIGNED — C-TSC — Temporary Session Cache (§7E-TSC): the attributed statement and complete context persist through authorized promotion. [V10 §25.2 / Statements About Ness] [V10 §25.2 / Temporary Session Cache] | Pending endpoint placement |
| C-7Q.5 — Third-party data baseline | C-OTHER.8 — Statements about Ness retain their speaker | Gated by | DESIGNED — C-7Q.5 — Third-party data baseline: actual words, Ness's interpretation and N.H's interpretation remain distinguishable; inference is not fact. [V10 §7Q] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-OTHER.8 — Statements about Ness retain their speaker | Changes | DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading keeps the original speaker attribution; C-7H — Reread Lifecycle (§7H): later evidence may cause a new reading without altering the earlier records. [V10 §25.2 / Statements About Ness] | Pending endpoint placement |
| C-7H — Reread Lifecycle (§7H) | C-OTHER.8 — Statements about Ness retain their speaker | Changes | DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): the reading keeps the original speaker attribution; C-7H — Reread Lifecycle (§7H): later evidence may cause a new reading without altering the earlier records. [V10 §25.2 / Statements About Ness] | Pending endpoint placement |
| C-7L.9.3 — Person-Box visibility restriction | C-OTHER.9 — Person-Box visibility for other speakers | Fed by | DESIGNED — C-7L.9.3 — Person-Box visibility restriction: the canonical person-information disclosure boundary. [V10 §25.2 / Person-Box Visibility] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.9 — Person-Box visibility for other speakers | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): current speaker access limits the answer. [V10 §25.2 / Person-Box Visibility] | Pending endpoint placement |
| C-TSC.12 — Session and item lifecycles | C-OTHER.10 — Third-party cache boundary | Fed by | DESIGNED — C-TSC.12 — Session and item lifecycles: the existing state and transition atoms retain the session's actual lifecycle. [V10 §25.2 / Temporary Session Cache] | Pending endpoint placement |
| C-TSC.16 — Session authorization | C-OTHER.10 — Third-party cache boundary | Gated by | DESIGNED — C-TSC.16 — Session authorization: the relevant completed session must be authorized before promotion; C-TSC.23 — Retained archive: permanent sealing requires its separate authorization. [V10 §25.2 / Temporary Session Cache] | Pending endpoint placement |
| C-TSC.23 — Retained archive | C-OTHER.10 — Third-party cache boundary | Gated by | DESIGNED — C-TSC.16 — Session authorization: the relevant completed session must be authorized before promotion; C-TSC.23 — Retained archive: permanent sealing requires its separate authorization. [V10 §25.2 / Temporary Session Cache] | Pending endpoint placement |
| C-TSC.16 — Session authorization | C-OTHER.11 — Completed-session batch authorization | Gated by | DESIGNED — C-TSC.16 — Session authorization: the session's fingerprint authorization is required; C-TSC.11 — Blockers and resolution history: every remaining blocker must be clear for the affected item to proceed. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-TSC.11 — Blockers and resolution history | C-OTHER.11 — Completed-session batch authorization | Gated by | DESIGNED — C-TSC.16 — Session authorization: the session's fingerprint authorization is required; C-TSC.11 — Blockers and resolution history: every remaining blocker must be clear for the affected item to proceed. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-TSC.17 — Ordered promotion | C-OTHER.11 — Completed-session batch authorization | Changes | DESIGNED — C-TSC.17 — Ordered promotion: the authorized, unblocked material is eligible for the established promotion route. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-TSC.11 — Blockers and resolution history | C-OTHER.11.2 — Unblocked items proceed automatically | Gated by | DESIGNED — C-TSC.11 — Blockers and resolution history: all remaining blockers for the item must be clear. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-TSC.17 — Ordered promotion | C-OTHER.11.2 — Unblocked items proceed automatically | Changes | DESIGNED — C-TSC.17 — Ordered promotion: eligible items enter the existing ordered processing operation. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-TSC.17 — Ordered promotion | C-OTHER.11.3 — Attributed promotion route | Gated by | DESIGNED — C-TSC.17 — Ordered promotion: existing promotion requirements apply; the conflicting route shorthand supplies no alternate operation. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [V10 §25.2 / Temporary Session Cache]; BUILT — C-STORE — Accretive store & sealed roots (§6B): `.nh_roots.sealed` blocks `append_root()`; the promotion route does not lift the seal. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] | Pending endpoint placement |
| C-STORE — Accretive store & sealed roots (§6B) | C-OTHER.11.3 — Attributed promotion route | Gated by | DESIGNED — C-TSC.17 — Ordered promotion: existing promotion requirements apply; the conflicting route shorthand supplies no alternate operation. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] [V10 §25.2 / Temporary Session Cache]; BUILT — C-STORE — Accretive store & sealed roots (§6B): `.nh_roots.sealed` blocks `append_root()`; the promotion route does not lift the seal. [V10 §6A / SOVEREIGNTY BOUNDARIES BY LAYER] | Pending endpoint placement |
| C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | C-OTHER.11.3 — Attributed promotion route | Changes | DESIGNED — C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G): receives attributed promoted material for reading. [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | Pending endpoint placement |
| C-SIA — Speaker Identity Assessment (§25.3) | C-OTHER.12 — Continuous speaker security | Fed by | DESIGNED — C-SIA — Speaker Identity Assessment (§25.3): continuous identity and acoustic-security evidence. [V10 §25.2 / Continuous Speaker Security] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.12 — Continuous speaker security | Gated by | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): current assessments determine the access ceiling and fail-closed outcome. [V10 §25.2 / Continuous Speaker Security] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.12.1 — Uncertainty lowers access | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): uncertain, stale or failed evidence reduces the current access level. [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.12.2 — Speaker-change recalculation | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the access calculation is refreshed immediately. [V10 §25.2 / Continuous Speaker Security] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.12.3 — Acoustic-suspicion guest outcome | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): Gate 0 terminates the access calculation at guest and queues the alert under its distinct condition. [V10 §25.4 / Access Level Calculation] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.13 — Current disclosure limits | Fed by | DESIGNED — C-OTHER.4 — Guest conversational response: the guest response contains only permitted content; C-SACL — Speaker Access-Control Layer (§25.4): current access and PBR limits. [V10 §25.2 / Guest Mode] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] | Pending endpoint placement |
| C-7Q.11.3 — Exact-payload privacy and output revalidation | C-OTHER.13 — Current disclosure limits | Gated by | ACCEPTED — C-7Q.11.3 — Exact-payload privacy and output revalidation: the exact output must satisfy the current privacy and revalidation boundary. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]; DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the final current access/PBR gate must pass after privacy. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.13 — Current disclosure limits | Gated by | ACCEPTED — C-7Q.11.3 — Exact-payload privacy and output revalidation: the exact output must satisfy the current privacy and revalidation boundary. [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §4]; DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): the final current access/PBR gate must pass after privacy. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7L.9.2 — Person-Box Ness-presence permission condition | C-OTHER.13.2 — PBR and Ness-presence revalidation | Gated by | DESIGNED — C-7L.9.2 — Person-Box Ness-presence permission condition: the PBR's required Ness presence must still hold. [V10 §25.4 / Multi-Speaker Sessions] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.13.2 — PBR and Ness-presence revalidation | Changes | DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): required-presence loss reduces the known-person stream to guest at the same time. [V10 §25.4 / Multi-Speaker Sessions] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.13.3 — Two sequential disclosure gates | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy review must pass first; C-SACL — Speaker Access-Control Layer (§25.4): final access and PBR review must then pass for the same answer. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.13.3 — Two sequential disclosure gates | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): final privacy review must pass first; C-SACL — Speaker Access-Control Layer (§25.4): final access and PBR review must then pass for the same answer. [V10 §25.4 / Output Gate (Two Factors, Sequential)] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-OTHER.14 — Other-speaker operational records | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to the records remains privacy-authorized; C-SACL — Speaker Access-Control Layer (§25.4): identity/security authorization remains required. [MAP C-OTHER] [V10 §0B] | Pending endpoint placement |
| C-SACL — Speaker Access-Control Layer (§25.4) | C-OTHER.14 — Other-speaker operational records | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to the records remains privacy-authorized; C-SACL — Speaker Access-Control Layer (§25.4): identity/security authorization remains required. [MAP C-OTHER] [V10 §0B] | Pending endpoint placement |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | 1 · DESIGNED | [V10 §25.2] [MAP C-OTHER] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER — Other-Speaker / Guest / Known-Person Architecture (§25.2) | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | 2 · DESIGNED | [V10 §25.2 / Temporary Session Cache] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.1 — Internal understanding and external disclosure | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Core Principle] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.2 — Protected authority for other-speaker use | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Protected Rules (Unconditional)] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.3.1 — Top-security level | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Fingerprint as One Independent Factor] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.3.2 — Recognized-Ness level | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Access Levels] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.3.3 — Known-person level | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Access Level Calculation] [V10 §25.4 / Permission Boundary Enforcement] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.5 — Known-person permission boundaries | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Permission Boundary Enforcement] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.7.4 — Translation reading and revision | C-7H — Reread Lifecycle (§7H), CY-F | 1 · DESIGNED | [V10 §25.2 / Parent Translation] [V10 §7H] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.7.5 — Private translation context and bounded disclosure | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Parent Translation] [V10 §25.4 / Avoiding Indirect Disclosure] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.8 — Statements about Ness retain their speaker | C-TSC — Temporary Session Cache (§7E-TSC), CY-D | 1 · DESIGNED | [V10 §25.2 / Statements About Ness] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.8 — Statements about Ness retain their speaker | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G) | 2 · DESIGNED | [V10 §25.2 / Statements About Ness] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.8 — Statements about Ness retain their speaker | C-7H — Reread Lifecycle (§7H), CY-F | 3 · DESIGNED | [V10 §25.2 / Statements About Ness] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.9 — Person-Box visibility for other speakers | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Person-Box Visibility] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.11.1 — Session-sized permission | C-TSC.16 — Session authorization | 1 · DESIGNED | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.11.2 — Unblocked items proceed automatically | C-TSC.17 — Ordered promotion | 1 · DESIGNED | [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.11.3 — Attributed promotion route | C-7G — Meaning Engine Interior + Acceptance Check + Creation-aware mode (§7G), CY-D | 1 · DESIGNED | [V10 §25.2 / Statements About Ness] [V10 §25.2 / Fingerprint-Authorized Batch Promotion] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.12.1 — Uncertainty lowers access | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Failure, Stale Assessments, Fail-Closed] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.12.2 — Speaker-change recalculation | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.2 / Continuous Speaker Security] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.12.3 — Acoustic-suspicion guest outcome | C-SACL — Speaker Access-Control Layer (§25.4), CY-I | 1 · DESIGNED | [V10 §25.4 / Access Level Calculation] [V10 §25.5] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.13.1 — Shared and private output ceilings | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.13.2 — PBR and Ness-presence revalidation | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Multi-Speaker Sessions] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §13] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.13.3 — Two sequential disclosure gates | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [V10 §25.4 / Output Gate (Two Factors, Sequential)] [04/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md §3] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.14 — Other-speaker operational records | C-SACL — Speaker Access-Control Layer (§25.4) | 1 · DESIGNED | [MAP C-OTHER] [V10 §0B] | TOGETHER continuation at using endpoint; preserve current use and its source |
| C-OTHER.14 — Other-speaker operational records | C-TSC — Temporary Session Cache (§7E-TSC) | 2 · DESIGNED | [MAP C-OTHER] | TOGETHER continuation at using endpoint; preserve current use and its source |

## Source-to-card coverage added by CH09-b

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

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-OTHER.1 — Internal understanding and external disclosure | Fails closed by |
| C-OTHER.1 — Internal understanding and external disclosure | Fed by |
| C-OTHER.1 — Internal understanding and external disclosure | Changes |
| C-OTHER.2 — Protected authority for other-speaker use | Fails closed by |
| C-OTHER.2 — Protected authority for other-speaker use | Fed by |
| C-OTHER.2 — Protected authority for other-speaker use | Changes |
| C-OTHER.3 — Four access levels | Gated by |
| C-OTHER.3 — Four access levels | Changes |
| C-OTHER.3.1 — Top-security level | Changes |
| C-OTHER.3.2 — Recognized-Ness level | Changes |
| C-OTHER.3.3 — Known-person level | Changes |
| C-OTHER.3.4 — Guest level | Gated by |
| C-OTHER.3.4 — Guest level | Changes |
| C-OTHER.4 — Guest conversational response | Changes |
| C-OTHER.5 — Known-person permission boundaries | Changes |
| C-OTHER.6 — Separate parent records | Fails closed by |
| C-OTHER.6 — Separate parent records | Gated by |
| C-OTHER.6 — Separate parent records | Changes |
| C-OTHER.7 — Request-driven parent translation | Changes |
| C-OTHER.7.1 — Interpret a parent's statement for Ness | Changes |
| C-OTHER.7.2 — Prepare private candidate wordings | Fed by |
| C-OTHER.7.2 — Prepare private candidate wordings | Changes |
| C-OTHER.7.3 — Deliver requested content to a parent | Fed by |
| C-OTHER.7.3 — Deliver requested content to a parent | Changes |
| C-OTHER.7.4 — Translation reading and revision | Fails closed by |
| C-OTHER.7.4 — Translation reading and revision | Gated by |
| C-OTHER.7.5 — Private translation context and bounded disclosure | Changes |
| C-OTHER.8 — Statements about Ness retain their speaker | Fails closed by |
| C-OTHER.9 — Person-Box visibility for other speakers | Changes |
| C-OTHER.10 — Third-party cache boundary | Changes |
| C-OTHER.11.1 — Session-sized permission | Gated by |
| C-OTHER.11.1 — Session-sized permission | Changes |
| C-OTHER.12 — Continuous speaker security | Changes |
| C-OTHER.12.1 — Uncertainty lowers access | Gated by |
| C-OTHER.12.2 — Speaker-change recalculation | Gated by |
| C-OTHER.12.3 — Acoustic-suspicion guest outcome | Gated by |
| C-OTHER.13 — Current disclosure limits | Changes |
| C-OTHER.13.1 — Shared and private output ceilings | Gated by |
| C-OTHER.13.1 — Shared and private output ceilings | Changes |
| C-OTHER.13.3 — Two sequential disclosure gates | Changes |
| C-OTHER.14 — Other-speaker operational records | Fails closed by |
| C-OTHER.14 — Other-speaker operational records | Fed by |
| C-OTHER.14 — Other-speaker operational records | Changes |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. The following positive scan hits are retained for the stated reason; they are not unreviewed exceptions. Tier action cards have explicit producer links. No source states a separate enforcement mechanism for a pure boundary law.

| Card / line | Flag | Reason |
|---|---|---|
| C-OTHER.1 — Internal understanding and external disclosure; line 56 | prerequisite_review / Fails closed by | The prerequisite hit comes from the explicit privacy/authority gate already filled. The source gives the separation invariant, not an additional independent failure procedure for this boundary card; Fails closed by remains undecided without weakening Gated by. |
| C-OTHER.3 — Four access levels; line 106 | prerequisite_review / Gated by | The phrase 'requires a confirmed non-Ness identity and active PBR' defines one of the four classifications. It is not a separate external gate on the vocabulary card. SACL supplies the computed level, and the classified conditions and fallback are explicit in its children and Fails closed by. |
| C-OTHER.7 — Request-driven parent translation; line 293 | plain_together / Gated by | The plain Gated by line is Ness's request, a genuine human precondition with no separate card. It is allowed by lessons 3.3; the recipient and privacy gates are separately named. |

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

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: complete §25.2; §25.4 from its opening through Access Level Calculation/Fingerprint as One Independent Factor, plus complete Multi-Speaker Sessions, Permission Boundary Enforcement, Avoiding Indirect Disclosure, Output Gate and Failure/Stale Assessments/Fail-Closed; §25.5 separation retained from CH09-a; complete §7H; full §7Q Third-party Data Rules; §6A Sovereignty Boundaries by Layer and the status-table root/seal rows. No whole-file credit. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: complete C-OTHER paragraph and fan-in correction discovery. Current paths CY-D/CY-I retain their prior canonical identities; full side-path construction remains CH11. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped: complete embedded §2 Other-Speaker / Guest / Known-Person Architecture. No whole-file credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Scoped: complete §§3/4/6D/13/14/15/16; consumer disclosure and transformation boundaries only placed here. Full delivery records and crash boundaries reserved for CH09-d. | `4edaaadc57854b711e7f750ed897e6f4a6eaa0c0ae3734b4614167e6c58afe48` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole receipt read. Acceptance and frozen wording evidence only. No claim that the receipt's conditional formal closure audit has occurred. | `9a26dcdbb442b3ed8900deb4015865f6744c81f4e3b42fe978c9c6d8dfd919f8` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Scoped: complete §3; §§4.4–4.10; §6. Existing privacy atoms and marked V10 conflicts reused, no new whole credit. | `3deacafbd7fb840404d59f05b0f314199467889735dcb9f6243f7ef14078d6f5` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: acceptance/status statements in §§1/3/4/5. Earlier complete receipt credit retained; not a new whole read. | `f89fa7b1603dd64c8000a084b539bd8596fc15c8662cba3a04ba3d4262ae7281` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_v1_3_CANDIDATE.md` | Scoped: complete §§3 and 17; third-party restrictions and the explicit differing A7 policy. Existing privacy mechanism owns the underlying records. | `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped: §5 Path 9 in full, adjacent connection/logging context, and §8 frozen-wording items 1–5. No new whole credit; remaining scope stays pending. | `b20d4ee944d5a575b307d70485e5c074c4b298f43a3082ddd760159aa61d924d` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Scoped: §7 introduction and complete C1–C3; canonical token, recognition and durable-receipt requirements remain with CH04-b owners. | `f722ac9599c8c88bb019220764266985aac2fe820068e20f5368dbcc9c229ef8` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Scoped: complete §§4/8; independent mode/access intersection and lower-ceiling behavior. Full mode mechanics remain CH09-i. | `c449728139f732d5aefe5efd7ca1a0d251937c64bd73504ff8527cc3ec01b305` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Scoped source-boundary discovery; no enrollment behavior imported. CH09-h owns the full package. | `184a63cf7dfbefdd73ea84c02506e3478374a48df2d9a2e174ed9a38305cacb6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md` | Scoped: complete §15 and the preceding §7L-handoff boundary. Existing connection owners remain CH06-g. | `6a3b7cf71546ed237507b34b1a24a759d34ca683216b255c91ac4add679b1bfd` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Scoped: §3 transfer and speaker-attribution paragraphs; phone capture policy remains CH10-d, not a new route in this chapter. | `187ef4ce4c24b09ad81d246053b88cf39c60f84550ce2ee2fdccba73a4a2b231` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Discovery only among Stage-2 rows, no behavior used and no whole-file credit. Pending restoration register remains CH12-b. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |

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

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

54 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
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
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — all 33 behavior cards reviewed; 0 behavior-workflow hits. Project records are outside behavior.
§1.4 every gap written as NOT DECIDED: PASS — 43 empty fields exactly match 43 current register rows; filled fields are not registered.
§1.5 conflicts marked, none resolved: PASS — sealed-store destination, downstream promotion order, third-party authorization/category policy and imitation-risk wording remain explicitly marked. Existing source-conflict treatment is preserved; no seal reopening or policy reconciliation is invented.
§3 exactly one stamp per line: PASS — 33 headers, 257 populated field lines and 51 USED BY rows checked. The 2 BUILT lines are C-OTHER.11.3's existing seal refusal and its C-STORE gate; both match V10's built-and-verified seal status. No other-speaker machinery is called built.
§4 every behavior line cited in the exact format: PASS — 31 distinct citation locations resolve at the pin; subheadings resolve within their named parent sections. The source-to-claim review, including the reused-owner scopes, was performed separately from location resolution.
§5.4 one name per thing: PASS — current headings, named TOGETHER targets, USED BY places and continuation endpoints match the canonical or newly declared names. No prior card is recreated under a new identity.
§6 all template fields present, in order, for every part: PASS — 33 templates and 300 field lines; repeated field lines separate source statuses or the genuine human gate. All 51 USED BY rows name one place with no more than one path. No card occurs in its own SUB-PARTS.
§6.3 reciprocity within this chapter: PASS — all 26 internal relationship occurrences have their reciprocal; 63 outgoing relationships and 25 external uses have 88 continuation rows naming both ends. No earlier incoming C-OTHER field relationship was found in the frozen behavior blocks. Future or earlier endpoint continuations remain explicit rather than being represented as edits.
§6.4 every decided detail written in, no citation used in place of content: PASS — 18 source-scope/placement rows reviewed; all 34 selected exact source-name literals present. The complete §25.2 content is carried. Shared TSC lifecycle and Person-Box field atoms retain their established identities; full SIA, SACL and delivery records have named later owners.
§6.5 sub-parts recursed to the bottom: PASS — all four access levels, three request branches, translation record/context boundaries, authorization unit, unblocked-item route, continuous-security outcomes and shared/private/PBR/gate limits are explicit. There are 0 empty-TOGETHER cards. Previously complete lifecycle/category structures are consumed through their canonical cards rather than recreated.
§9 coverage matrix rows added for every file used: PASS — 145 inherited READ-folder paths resolve at the pin; all current placements and 15 full source fingerprints are recorded. Earlier identities are listed and verified for 47 chapters. The 54 remaining whole-file reading obligations remain visible.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior and all use rows were reviewed. The source's “How should I say X to [parent]?” is an example request handled by the machine, not a recommendation from this document. The whole-file wording scan returns 0 hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

### Computed self-check results

Writer checks are not an independent audit or adoption. The 3 positive flags are individually named above: two prerequisite-review hits whose actual conditions are already placed, and the plain human-request gate. All 300 behavior field lines and all 51 use rows were reviewed for misfiled content; the restriction/failure/gate review covers 99 named slots expressed in 102 field lines. No DECIDED-stamped line needs a deciding-record check in this piece. No unresolved current-file validator error remains.

| Check | Count |
|---|---|
| cards | 33 |
| field_lines | 300 |
| used_by_rows | 51 |
| empty_fields | 43 |
| internal_edges | 26 |
| outgoing_edges | 63 |
| external_uses | 25 |
| citations | 31 |
| resolved_citation_headings | 31 |
| built_lines | 2 |
| formula_hits | 0 |
| workflow_hits | 0 |
| wording_hits | 0 |
| errors | 0 |
| review_flags | 3 |
| registered_empty_fields | 43 |
| continuation_rows | 88 |
| source_literals_checked | 34 |
| source_literals_missing | 0 |
| preserved_earlier_hashes | 47 |
| read_fingerprints_checked | 15 |
| coverage_file_paths | 145 |
| coverage_paths_missing_at_pin | 0 |
| pending_whole_files | 54 |
| source_map_rows | 18 |
| named_review_dispositions | 3 |
| misfiled_box_fields_scanned | 300 |
| restriction_failure_gate_slots_reviewed | 99 |
| restriction_failure_gate_lines_reviewed | 102 |
