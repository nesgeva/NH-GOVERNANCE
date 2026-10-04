# Chapter 10-d — Group H: C-23

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH10-d.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`  

This piece covers the three-mode mobile companion, its independent local memory, two deliberate connection doors, sync and authentication boundaries, mobile logging and unresolved A20/B30 mechanics. CH09-i remains the canonical owner of A22 phone-control policy and restored phone names; this piece supplies their mobile interfaces. CH10-e carries interface/World design, CH11 the connected mobile path, and CH12 the registers. No tunnel implementation, platform choice, transfer scope or cross-layer migration is inferred.

[SOURCE CONFLICT] Map C-23 says Manual Sync requires biometric confirmation. V10 §23 and DD §3L expressly allow fingerprint, Face ID or PIN. The V10 alternatives are retained without silently changing the Map's narrower wording. The separate protected-voice-material rule still requires biometric verification through Full Mode. [MAP C-23] [V10 §23] [DD §3L] [V10 §25.3 / Raw Voice Data Protection]

[SOURCE CONFLICT] Map C-23 ends with “A20 settled” while its own open-slots list, V10 §23 and the accepted A22 receipt still leave the on-device model, local memory format, background-platform feasibility and Manual-Sync content scope open. Those choices remain unfilled. [MAP C-23] [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md §5]

[SOURCE CONFLICT] V10 §9 and Map C-9 retain five recovered phone-side names. Accepted A22 removes Breathing Reminder and Night Lockout and adds Cloudflare Tunnel Off. The earlier C-9.3 inventory and accepted policy are preserved at their own status; this mobile interface creates no removed feature or replacement wellbeing restriction. [V10 §9] [MAP C-9] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1]

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`.

<!-- BEGIN BEHAVIOR -->

### C-23 — Mobile App, three modes (§23)
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — A mobile companion with an on-demand real-N.H Full Mode and one independent local AI in online/offline states. [V10 §23]
- Takes in: DESIGNED — Ness's deliberate requests, locally accumulated phone material and available connectivity. [V10 §23]
- Does: DESIGNED — Keeps Mode 1 separate from Modes 2/3; lets the local AI answer online or from its existing offline memory; bridges to real N.H only through deliberate Manual Sync or Full Mode. [V10 §23]
- Gives out: DESIGNED — Live desktop access during an authorized Full Mode window, independent local answers and deliberately transferred phone material subject to review. [V10 §23]
- Must never: DESIGNED — Auto-connect to real N.H, leave a passive tunnel, give phone data a shortcut to REALITY, execute raw OS commands from phone input or store local data unencrypted. [V10 §23]
- Fails closed by: DESIGNED — With no usable local memory offline, stores Ness's words without a reply and waits for connectivity. [V10 §23]

TOGETHER
- Fed by: DESIGNED — C-9.3 — Phone-side feature scope: provides the accepted phone controls without creating another connection door. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: requires deliberate Ness action for both real-N.H bridges. [V10 §23]
- Changes: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): receives eligible mobile captures through the ordinary front door. [MAP C-7E]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.1 — Two deliberate connection doors | A deliberate Ness request to connect or send material. [V10 §23] | Permits only the two named doors; keeps local AI operation independent otherwise. [V10 §23] | A deliberate connection route without an automatic background channel. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.2 — Mode 1 — Full Mode | Ness's explicit fingerprint, Face ID or PIN action and real authentication. [V10 §23] | Opens a Cloudflare tunnel for direct full-memory/full-engine live access during a window Ness deliberately creates and ends. [V10 §23] | A live remote Full Mode session. [V10 §23] | [V10 §23] |
| 3 · DESIGNED | C-23.2.1 — Deliberate Full Mode opening | A deliberate fingerprint, Face ID or PIN action by Ness. [V10 §23] | Starts the Full Mode window only through actual authentication. [V10 §23] | A deliberately initiated connection window. [V10 §23] | [V10 §23] |
| 4 · DESIGNED | C-23.2.2 — Deliberate Full Mode closure | Ness's decision to close the tunnel when done. [V10 §23] | Ends the deliberately created connection window. [V10 §23] | No passively continuing Full Mode tunnel. [V10 §23] | [V10 §23] |
| 5 · DESIGNED | C-23.3 — Independent local AI and memory | Phone interactions, its local memory and online API results when available. [V10 §23] | Operates independently of the real N.H REALITY/SIMULATION store; online/offline are two states of this same local AI. [V10 §23] | Local answers and retained independent phone memory. [V10 §23] | [V10 §23] |
| 6 · DESIGNED | C-23.3.1 — Separate encrypted local memory | Material retained by the local AI. [V10 §23] | Keeps local memory on the phone and encrypted at rest across all modes. [V10 §23] | Independent encrypted local data. [V10 §23] | [V10 §23] |
| 7 · DESIGNED | C-23.4.1 — Mode 3 — Local AI offline | What Mode 2 already taught the local AI and what its local memory can supply. [V10 §23] | Runs from existing local knowledge, with no new API calls or online learning. [V10 §23] | Offline local answers where usable local memory exists. [V10 §23] | [V10 §23] |
| 8 · DESIGNED | C-23.5 — Manual Sync | Ness's explicit sync request, confirmation and local memory material. [V10 §23] | Requires fingerprint, Face ID or PIN confirmation before sending; routes arriving material through the same SIMULATION review gate as other unverified material. [V10 §23] | Phone-originated material awaiting the ordinary reviewed entry path. [V10 §23] | [V10 §23] |
| 9 · DESIGNED | C-23.5.2 — Same review gate for phone material | Material deliberately sent from the phone. [V10 §23] | Treats it by the same review standard as a research finding or sandbox-scored thought; while Layer 2 remains active, its authorized promotion path remains protected. [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Reviewed material only through the existing authorized gate. [V10 §23] | [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 10 · DESIGNED | C-23.6 — Mobile security requirements | Full Mode access, phone-originated content and all locally stored data. [V10 §23] | Keeps those five requirements applicable across mobile modes. [V10 §23] | Deliberately bounded remote access and protected local/transfer behavior. [V10 §23] | [V10 §23] |
| 11 · ACCEPTED | C-23.8 — Accepted phone-control interfaces | Ness's deliberate control activations and their existing policy conditions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] | Keeps private phone capture distinct from transfer, and ordinary disconnection distinct from emergency desktop stopping. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] | Only the four accepted control effects, each within the two-door boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] |
| 12 · ACCEPTED | C-23.8.1 — Emergency recording phone boundary | Ness's deliberately started recording and the single after-call choice. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Keeps the recording private on the phone; exactly once after the call offers Keep private, Send whole call or Choose parts. Only deliberately selected excerpts are sent under Choose parts, visibly marked as part of a longer call. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Private phone material or a deliberately selected whole/excerpt transfer toward real N.H. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 13 · DESIGNED | C-23.9 — Mobile operational history | Actual Full Mode opens/closes, Manual Sync events and gate outcomes, and local-AI learning updates. [MAP C-23] | Records each event with the clear boundary that local records never silently enter real N.H; access remains subject to privacy and applicable identity/security authorization. [MAP C-23] | Traceable mobile operational records. [MAP C-23] | [MAP C-23] |
| 14 · ACCEPTED | C-23.10 — Layer-2 mobile coexistence | Mobile operations crossing or approaching the real-N.H boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] | Keeps Layer 2 active and protected until Ness explicitly authorizes decommissioning; A24/B-INT-10 retain the cross-layer handoff scope. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] | Mobile transfers within the existing protected layer boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] |
| 15 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Captures from every front door, each with the minimum intake envelope and any reliable source-derived catalog facts already known. | Captures and normalizes identifiable material, evaluates catalog completeness, manages resolution and holding, then promotes only eligible material without duplicate roots. | Nothing at this status; see the companion row. | [V10 §7E / MINIMUM INTAKE ENVELOPE] [MAP C-7E] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / PRE-INGEST HOLDING AREA] |
| 16 · ACCEPTED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | Nothing at this status; see the companion row. | Nothing at this status; see the companion row. | Prepared root payloads and committed upstream evidence references through the B11 active-writable-batch seam, receiving its durable caller outcome and owning `batch_id` [proposed]. | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 17 · DESIGNED | C-9 — Access/authentication model + voice I/O + phone modes (§9) | Deliberate access requests, ordinary and stronger authentication results, voice input and requests for speech output. [V10 §9] | Separates personal-data access in code, keeps voice a soft factor, handles the confirmed microphone/cleanup/transcription/front-door/speech stages and stops TTS immediately when Ness speaks. [V10 §9] [MAP C-9] | Mode-limited data access, Hebrew and English speech, access-transition and step-up records and voice-stage events. [V10 §9] [MAP C-9] | [V10 §9] [MAP C-9] |
| 18 · ACCEPTED | C-9.3 — Phone-side feature scope | Deliberate phone-control actions within A22's separately accepted four-control policy. | Provides Emergency Record, Stealth Toggle, Cloudflare Tunnel Off and the Full Mode Kill Switch; Breathing Reminder and Night Lockout are removed from A22. | Private phone capture choices, ordinary remote disconnect or bounded emergency stop according to the selected control. | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] |
| 19 · ACCEPTED | C-9.3.1 — Emergency Record | The active call and Ness's deliberate start. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Records the call, keeps it private on the phone and asks exactly once after the call what to do with it. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Exactly three choices: Keep private, Send whole call, Choose parts. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 20 · ACCEPTED | C-9.3.3 — Stealth Toggle | Ness's activation and the surrounding live audio. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Keeps recording and any local understanding private on the phone; may understand the situation locally and show silent screen text; offers the three choices when Ness stops it. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Keep private, Send whole recording or Choose parts, with selected parts visibly marked as excerpts. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] |
| 21 · ACCEPTED | C-9.3.5 — Full Mode Kill Switch | Ness's Kill Switch activation while the bounded emergency-stop conditions hold. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Immediately ends phone Full Mode access, closes the tunnel, invalidates/rejects the current session, stops and locks desktop N.H software and active services, and prevents unfinished phone-operation steps where stopping safely prevents further effects. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Stopped/locked desktop N.H and terminated Full Mode access, while Windows stays powered on and the independent phone companion's memory stays separate. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] |
| 22 · ACCEPTED | C-9.3.6 — Cloudflare Tunnel Off | Ness activating Tunnel Off. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Closes the current Cloudflare Tunnel, invalidates and ends the current remote Full Mode phone session and ends its access to real N.H. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | An ended remote phone session while real N.H keeps running locally on the desktop. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] |
| 23 · ACCEPTED | C-9.3.7 — Phone recording transfer boundary | Ness's deliberate send choice, the chosen material and current identity/authorization/privacy/provenance/intake facts. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Uses only Manual Sync or Full Mode; carries source and speaker; uses the §7E envelope and B11 active writable batch, never the sealed 5,521-root batch. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Material submitted through the existing authorized intake door; a send action is not a final-memory entry. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 24 · ACCEPTED | C-9.3.9 — Unspecified phone-control mechanics | NOT DECIDED | NOT DECIDED | NOT DECIDED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §6] |
| 25 · DESIGNED | C-SIA.13 — Protected raw voice and readings | Raw acoustic roots in the sealed root store, Layer 3 Full Protected, and profile readings in the readings store under the same protection rules. [V10 §25.3 / Raw Voice Data Protection] | Requires at least `recognized_ness` for access; permits transmission outside the local device only through the Full Mode tunnel under biometric-verified conditions. [V10 §25.3 / Raw Voice Data Protection] | Access and permitted transmission within those protection limits. [V10 §25.3 / Raw Voice Data Protection] | [V10 §25.3 / Raw Voice Data Protection] |

SUB-PARTS: C-23.1 — Two deliberate connection doors; C-23.2 — Mode 1 — Full Mode; C-23.3 — Independent local AI and memory; C-23.4 — Mode 2 — Local AI online; C-23.5 — Manual Sync; C-23.6 — Mobile security requirements; C-23.7 — Protected voice-material transmission; C-23.8 — Accepted phone-control interfaces; C-23.9 — Mobile operational history; C-23.10 — Layer-2 mobile coexistence; C-23.11 — Mobile policy choices still open; C-23.12 — Full Mode mechanical design still open

### C-23.1 — Two deliberate connection doors
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The exclusive phone-to-real-N.H boundary: Manual Sync and Full Mode. [V10 §23]
- Takes in: DESIGNED — A deliberate Ness request to connect or send material. [V10 §23]
- Does: DESIGNED — Permits only the two named doors; keeps local AI operation independent otherwise. [V10 §23]
- Gives out: DESIGNED — A deliberate connection route without an automatic background channel. [V10 §23]
- Must never: DESIGNED — Open automatically, on a schedule or silently, or treat a deliberate action as permission to invent a third door. [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Fails closed by: DESIGNED — Without the deliberate trigger, neither door opens. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness deliberately triggers Manual Sync or Full Mode. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): defines the only permitted connection boundary. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23 — Mobile App, three modes (§23) | Ness's deliberate requests, locally accumulated phone material and available connectivity. [V10 §23] | Keeps Mode 1 separate from Modes 2/3; lets the local AI answer online or from its existing offline memory; bridges to real N.H only through deliberate Manual Sync or Full Mode. [V10 §23] | Live desktop access during an authorized Full Mode window, independent local answers and deliberately transferred phone material subject to review. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.2 — Mode 1 — Full Mode | Ness's explicit fingerprint, Face ID or PIN action and real authentication. [V10 §23] | Opens a Cloudflare tunnel for direct full-memory/full-engine live access during a window Ness deliberately creates and ends. [V10 §23] | A live remote Full Mode session. [V10 §23] | [V10 §23] |
| 3 · DESIGNED | C-23.3 — Independent local AI and memory | Phone interactions, its local memory and online API results when available. [V10 §23] | Operates independently of the real N.H REALITY/SIMULATION store; online/offline are two states of this same local AI. [V10 §23] | Local answers and retained independent phone memory. [V10 §23] | [V10 §23] |
| 4 · DESIGNED | C-23.4 — Mode 2 — Local AI online | Questions, local memory and available internet APIs, with OpenRouter named as an example. [V10 §23] | Uses APIs to answer and grow or improve its own local memory; each online interaction can add to what it knows. [V10 §23] | Online local answers and local learning. [V10 §23] | [V10 §23] |
| 5 · DESIGNED | C-23.4.1 — Mode 3 — Local AI offline | What Mode 2 already taught the local AI and what its local memory can supply. [V10 §23] | Runs from existing local knowledge, with no new API calls or online learning. [V10 §23] | Offline local answers where usable local memory exists. [V10 §23] | [V10 §23] |
| 6 · DESIGNED | C-23.5 — Manual Sync | Ness's explicit sync request, confirmation and local memory material. [V10 §23] | Requires fingerprint, Face ID or PIN confirmation before sending; routes arriving material through the same SIMULATION review gate as other unverified material. [V10 §23] | Phone-originated material awaiting the ordinary reviewed entry path. [V10 §23] | [V10 §23] |
| 7 · DESIGNED | C-23.5.2 — Same review gate for phone material | Material deliberately sent from the phone. [V10 §23] | Treats it by the same review standard as a research finding or sandbox-scored thought; while Layer 2 remains active, its authorized promotion path remains protected. [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Reviewed material only through the existing authorized gate. [V10 §23] | [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 8 · DESIGNED | C-23.6 — Mobile security requirements | Full Mode access, phone-originated content and all locally stored data. [V10 §23] | Keeps those five requirements applicable across mobile modes. [V10 §23] | Deliberately bounded remote access and protected local/transfer behavior. [V10 §23] | [V10 §23] |
| 9 · ACCEPTED | C-23.8 — Accepted phone-control interfaces | Ness's deliberate control activations and their existing policy conditions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Keeps private phone capture distinct from transfer, and ordinary disconnection distinct from emergency desktop stopping. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] | Only the four accepted control effects, each within the two-door boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] |
| 10 · ACCEPTED | C-23.8.3 — Ordinary remote-session disconnection | Ness's Tunnel Off activation. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Closes the current tunnel, invalidates/ends the remote phone session and ends access through it; desktop N.H continues locally. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Ended remote access with desktop operation and independent phone memory preserved. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] |

SUB-PARTS: NONE

### C-23.2 — Mode 1 — Full Mode
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — An on-demand live tunnel from the phone to the real desktop N.H. [V10 §23]
- Takes in: DESIGNED — Ness's explicit fingerprint, Face ID or PIN action and real authentication. [V10 §23]
- Does: DESIGNED — Opens a Cloudflare tunnel for direct full-memory/full-engine live access during a window Ness deliberately creates and ends. [V10 §23]
- Gives out: DESIGNED — A live remote Full Mode session. [V10 §23]
- Must never: DESIGNED — Open automatically, silently or on a schedule, or keep the tunnel passively open. [V10 §23]
- Fails closed by: DESIGNED — No deliberate authenticated action means no Full Mode opening. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: requires the explicit trigger; C-23.6.1 — Real tunnel authentication: requires actual nh_auth.py PIN/token wiring. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): enables the temporary direct desktop connection. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.2.2 — Deliberate Full Mode closure | Ness's decision to close the tunnel when done. [V10 §23] | Ends the deliberately created connection window. [V10 §23] | No passively continuing Full Mode tunnel. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.6.1 — Real tunnel authentication | A deliberate opening request and the real authentication result. [V10 §23] | Requires the tunnel itself to be gated by that authentication mechanism. [V10 §23] | An authenticated Full Mode boundary, with exact wiring still unspecified. [V10 §23] | [V10 §23] |
| 3 · DESIGNED | C-23.7 — Protected voice-material transmission | Protected identity/voice material under its local store protections. [V10 §25.3 / Raw Voice Data Protection] | Allows external transmission only through Full Mode under biometric-verified conditions; access requires at least recognized_ness. [V10 §25.3 / Raw Voice Data Protection] | A constrained protected-material path within Full Mode. [V10 §25.3 / Raw Voice Data Protection] | [V10 §25.3 / Raw Voice Data Protection] |
| 4 · ACCEPTED | C-23.8.3 — Ordinary remote-session disconnection | Ness's Tunnel Off activation. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Closes the current tunnel, invalidates/ends the remote phone session and ends access through it; desktop N.H continues locally. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Ended remote access with desktop operation and independent phone memory preserved. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] |
| 5 · ACCEPTED | C-23.8.4 — Emergency Full Mode stop interface | The explicit emergency activation and all five simultaneously applicable §7P stop conditions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Immediately ends phone access, closes the tunnel, rejects/invalidates the session, stops/locks desktop N.H and its active services, and prevents unfinished phone-originated steps where a bounded stop safely prevents additional effects. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Stopped and locked desktop N.H with Windows powered on and independent local phone memory unchanged. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] |
| 6 · DESIGNED | C-23.9.1 — Tunnel-open event | An actual deliberately opened tunnel. [MAP C-23] | Records the opening event under the mobile operational boundary. [MAP C-23] | A Full Mode opening record. [MAP C-23] | [MAP C-23] |

SUB-PARTS: C-23.2.1 — Deliberate Full Mode opening; C-23.2.2 — Deliberate Full Mode closure

### C-23.2.1 — Deliberate Full Mode opening
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The explicit-action trigger for the real-N.H tunnel. [V10 §23]
- Takes in: DESIGNED — A deliberate fingerprint, Face ID or PIN action by Ness. [V10 §23]
- Does: DESIGNED — Starts the Full Mode window only through actual authentication. [V10 §23]
- Gives out: DESIGNED — A deliberately initiated connection window. [V10 §23]
- Must never: DESIGNED — Infer opening permission from elapsed time, scheduling, background activity or a password existing elsewhere. [V10 §23]
- Fails closed by: DESIGNED — Opening cannot occur without the explicit authenticated action. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): starts the requested real-N.H connection. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.6.1 — Real tunnel authentication | A deliberate opening request and the real authentication result. [V10 §23] | Requires the tunnel itself to be gated by that authentication mechanism. [V10 §23] | An authenticated Full Mode boundary, with exact wiring still unspecified. [V10 §23] | [V10 §23] |

SUB-PARTS: NONE

### C-23.2.2 — Deliberate Full Mode closure
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — Ness's explicit end to the temporary Full Mode window. [V10 §23]
- Takes in: DESIGNED — Ness's decision to close the tunnel when done. [V10 §23]
- Does: DESIGNED — Ends the deliberately created connection window. [V10 §23]
- Gives out: DESIGNED — No passively continuing Full Mode tunnel. [V10 §23]
- Must never: DESIGNED — Leave the tunnel open as an always-on connection. [V10 §23]
- Fails closed by: ACCEPTED — A later Full Mode session requires a new deliberate action. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-9.3.6 — Cloudflare Tunnel Off: supplies the ordinary disconnect control. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Gated by: DESIGNED — C-23.2 — Mode 1 — Full Mode: bounds the tunnel to Ness's created and ended window. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): ends ordinary remote access. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.9.2 — Tunnel-close event | An actual tunnel close. [MAP C-23] | Records the closed connection window. [MAP C-23] | A Full Mode closure record. [MAP C-23] | [MAP C-23] |

SUB-PARTS: NONE

### C-23.3 — Independent local AI and memory
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — One small on-phone model with its own memory, used in both online and offline states. [V10 §23]
- Takes in: DESIGNED — Phone interactions, its local memory and online API results when available. [V10 §23]
- Does: DESIGNED — Operates independently of the real N.H REALITY/SIMULATION store; online/offline are two states of this same local AI. [V10 §23]
- Gives out: DESIGNED — Local answers and retained independent phone memory. [V10 §23]
- Must never: DESIGNED — Auto-connect, merge its memory into real N.H, or treat phone learning as a desktop-memory write. [V10 §23]
- Fails closed by: DESIGNED — The only connection bridges remain deliberate Manual Sync and Full Mode. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: prevents independent local operation from becoming a hidden connection. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): supplies the same local companion in Modes 2 and 3. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.3.1 — Separate encrypted local memory | Material retained by the local AI. [V10 §23] | Keeps local memory on the phone and encrypted at rest across all modes. [V10 §23] | Independent encrypted local data. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.4 — Mode 2 — Local AI online | Questions, local memory and available internet APIs, with OpenRouter named as an example. [V10 §23] | Uses APIs to answer and grow or improve its own local memory; each online interaction can add to what it knows. [V10 §23] | Online local answers and local learning. [V10 §23] | [V10 §23] |
| 3 · DESIGNED | C-23.4.1 — Mode 3 — Local AI offline | What Mode 2 already taught the local AI and what its local memory can supply. [V10 §23] | Runs from existing local knowledge, with no new API calls or online learning. [V10 §23] | Offline local answers where usable local memory exists. [V10 §23] | [V10 §23] |
| 4 · ACCEPTED | C-23.8.2 — Stealth phone boundary | Ness's activation, local recording/understanding and the choice when Stealth stops. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Keeps recording and understanding private; may understand locally and show silent text, with no spoken/audible response. On stopping offers Keep private, Send whole recording or Choose parts; sent parts stay marked as excerpts. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Private local material or a deliberate whole/excerpt transfer under the existing protections. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] |

SUB-PARTS: C-23.3.1 — Separate encrypted local memory

### C-23.3.1 — Separate encrypted local memory
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The phone companion's own memory, separate from REALITY/SIMULATION. [V10 §23]
- Takes in: DESIGNED — Material retained by the local AI. [V10 §23]
- Does: DESIGNED — Keeps local memory on the phone and encrypted at rest across all modes. [V10 §23]
- Gives out: DESIGNED — Independent encrypted local data. [V10 §23]
- Must never: DESIGNED — Store local data unencrypted or silently cross the boundary into the real store. [V10 §23]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.3 — Independent local AI and memory: preserves the separate-store boundary. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): retains the local knowledge available in either connectivity state. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.4 — Mode 2 — Local AI online | Questions, local memory and available internet APIs, with OpenRouter named as an example. [V10 §23] | Uses APIs to answer and grow or improve its own local memory; each online interaction can add to what it knows. [V10 §23] | Online local answers and local learning. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.4.1.1 — Offline with no usable local memory | Ness's words while disconnected and without usable local knowledge. [V10 §23] | Stores what Ness says silently and waits for a connection. [V10 §23] | Retained phone input without a fabricated reply. [V10 §23] | [V10 §23] |
| 3 · DESIGNED | C-23.5 — Manual Sync | Ness's explicit sync request, confirmation and local memory material. [V10 §23] | Requires fingerprint, Face ID or PIN confirmation before sending; routes arriving material through the same SIMULATION review gate as other unverified material. [V10 §23] | Phone-originated material awaiting the ordinary reviewed entry path. [V10 §23] | [V10 §23] |

SUB-PARTS: NONE

### C-23.4 — Mode 2 — Local AI online
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The independent local AI with internet API access. [V10 §23]
- Takes in: DESIGNED — Questions, local memory and available internet APIs, with OpenRouter named as an example. [V10 §23]
- Does: DESIGNED — Uses APIs to answer and grow or improve its own local memory; each online interaction can add to what it knows. [V10 §23]
- Gives out: DESIGNED — Online local answers and local learning. [V10 §23]
- Must never: DESIGNED — Treat online connectivity as authorization to connect to real N.H. [V10 §23]
- Fails closed by: DESIGNED — Real-N.H access still requires a separate deliberate door action. [V10 §23]

TOGETHER
- Fed by: DESIGNED — C-23.3 — Independent local AI and memory: supplies the on-phone model and independent store. [V10 §23]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: keeps internet learning distinct from real-N.H connection. [V10 §23]
- Changes: DESIGNED — C-23.3.1 — Separate encrypted local memory: retains the local learning from online use. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.9.4 — Local learning-update event | An actual learning update in the independent phone companion. [MAP C-23] | Records the local update without moving that material into the real store. [MAP C-23] | A local learning-update record. [MAP C-23] | [MAP C-23] |

SUB-PARTS: C-23.4.1 — Mode 3 — Local AI offline

### C-23.4.1 — Mode 3 — Local AI offline
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The same phone model and memory without internet access. [V10 §23]
- Takes in: DESIGNED — What Mode 2 already taught the local AI and what its local memory can supply. [V10 §23]
- Does: DESIGNED — Runs from existing local knowledge, with no new API calls or online learning. [V10 §23]
- Gives out: DESIGNED — Offline local answers where usable local memory exists. [V10 §23]
- Must never: DESIGNED — Invent an answer when no usable local memory exists or imply that an unavailable API was called. [V10 §23]
- Fails closed by: DESIGNED — The no-memory case stores Ness's words silently with no reply until connectivity returns. [V10 §23]

TOGETHER
- Fed by: DESIGNED — C-23.3 — Independent local AI and memory: preserves the same model and store across the connectivity change. [V10 §23]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: forbids automatic fallback to the real desktop system. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): keeps existing local capability available offline. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.4.1.1 — Offline with no usable local memory | Ness's words while disconnected and without usable local knowledge. [V10 §23] | Stores what Ness says silently and waits for a connection. [V10 §23] | Retained phone input without a fabricated reply. [V10 §23] | [V10 §23] |

SUB-PARTS: C-23.4.1.1 — Offline with no usable local memory

### C-23.4.1.1 — Offline with no usable local memory
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The explicit no-answer branch for an offline local AI without usable memory. [V10 §23]
- Takes in: DESIGNED — Ness's words while disconnected and without usable local knowledge. [V10 §23]
- Does: DESIGNED — Stores what Ness says silently and waits for a connection. [V10 §23]
- Gives out: DESIGNED — Retained phone input without a fabricated reply. [V10 §23]
- Must never: DESIGNED — Pretend to answer, invent missing knowledge or auto-connect to the real system. [V10 §23]
- Fails closed by: DESIGNED — Gives no reply until the connection returns. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.4.1 — Mode 3 — Local AI offline: supplies the offline/no-memory condition. [V10 §23]
- Changes: DESIGNED — C-23.3.1 — Separate encrypted local memory: retains the phone-side input under local storage protection. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.5 — Manual Sync
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — A deliberate transfer of accumulated local-AI material toward desktop N.H. [V10 §23]
- Takes in: DESIGNED — Ness's explicit sync request, confirmation and local memory material. [V10 §23]
- Does: DESIGNED — Requires fingerprint, Face ID or PIN confirmation before sending; routes arriving material through the same SIMULATION review gate as other unverified material. [V10 §23]
- Gives out: DESIGNED — Phone-originated material awaiting the ordinary reviewed entry path. [V10 §23]
- Must never: DESIGNED — Run background sync, bypass review or promote phone data directly to REALITY. [V10 §23]
- Fails closed by: DESIGNED — No confirmation means no send; no review means no direct REALITY entry. [V10 §23]

TOGETHER
- Fed by: DESIGNED — C-23.3.1 — Separate encrypted local memory: supplies the accumulated phone material. [V10 §23]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: requires Ness's deliberate sync trigger. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): provides the explicit phone-to-desktop transfer door. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.5.1 — Pre-send confirmation | Ness's requested sync and explicit confirming factor. [V10 §23] | Keeps the send behind that confirmation. [V10 §23] | A confirmed transfer request. [V10 §23] | [V10 §23] |
| 2 · DESIGNED | C-23.5.2 — Same review gate for phone material | Material deliberately sent from the phone. [V10 §23] | Treats it by the same review standard as a research finding or sandbox-scored thought; while Layer 2 remains active, its authorized promotion path remains protected. [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Reviewed material only through the existing authorized gate. [V10 §23] | [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] |
| 3 · ACCEPTED | C-23.5.3 — Mobile root-entry caller contract | Seven-field root payload, eligibility/authorization/blocker-clearance references, stable ingest-identity basis per sync item, and source provenance labels. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] | Supplies that caller contract through the Catalog path; B11 mechanically checks shape against schema_compat_ref [proposed], evidence-reference existence, identity/idempotency and target state. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] | The B11 outcome, root identity and owning batch_id [proposed], while mobile retains sync-scope policy. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] | [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] |
| 4 · DESIGNED | C-23.9.3 — Sync event and gate outcome | An actual sync and the associated gate result. [MAP C-23] | Keeps the transfer event and gate outcome attributable. [MAP C-23] | A sync record with the actual gate outcome. [MAP C-23] | [MAP C-23] |

SUB-PARTS: C-23.5.1 — Pre-send confirmation; C-23.5.2 — Same review gate for phone material; C-23.5.3 — Mobile root-entry caller contract

### C-23.5.1 — Pre-send confirmation
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The fingerprint, Face ID or PIN confirmation required before Manual Sync sends anything. [V10 §23]
- Takes in: DESIGNED — Ness's requested sync and explicit confirming factor. [V10 §23]
- Does: DESIGNED — Keeps the send behind that confirmation. [V10 §23]
- Gives out: DESIGNED — A confirmed transfer request. [V10 §23]
- Must never: DESIGNED — Send before confirmation or replace it with an automatic background trigger. [V10 §23]
- Fails closed by: DESIGNED — Unconfirmed material stays unsent. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness explicitly confirms with fingerprint, Face ID or PIN before anything is sent. [V10 §23]
- Changes: DESIGNED — C-23.5 — Manual Sync: supplies the required pre-send act. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.5.2 — Same review gate for phone material
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The ordinary SIMULATION review requirement for arriving phone data. [V10 §23]
- Takes in: DESIGNED — Material deliberately sent from the phone. [V10 §23]
- Does: DESIGNED — Treats it by the same review standard as a research finding or sandbox-scored thought; while Layer 2 remains active, its authorized promotion path, `promote_to_memory()`, remains protected. [V10 §23] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Gives out: DESIGNED — Reviewed material only through the existing authorized gate. [V10 §23]
- Must never: DESIGNED — Give phone-sourced material an exception or direct route into REALITY. [V10 §23]
- Fails closed by: DESIGNED — Unreviewed material does not promote directly into REALITY. [V10 §23]

TOGETHER
- Fed by: DESIGNED — C-23.5 — Manual Sync: supplies deliberately transferred local material. [V10 §23]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: forbids any third transfer path. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): preserves the existing Layer-2 intake boundary. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.5.3 — Mobile root-entry caller contract
Stamp: ACCEPTED    Source: [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]

ALONE
- What it is: ACCEPTED — The per-sync-item caller seam into the shared Catalog/B11 root writer. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Takes in: ACCEPTED — Seven-field root payload, eligibility/authorization/blocker-clearance references, stable ingest-identity basis per sync item, and source provenance labels. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Does: ACCEPTED — Supplies that caller contract through the Catalog path; B11, through the shared `append_root()` boundary, mechanically checks shape against schema_compat_ref [proposed], evidence-reference existence, identity/idempotency and target state. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Gives out: ACCEPTED — The B11 outcome, root identity and owning batch_id [proposed], while mobile retains sync-scope policy. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]
- Must never: ACCEPTED — Write directly to root files, bypass the shared Catalog/B11 seam, append to the sealed 5,521-root batch, or treat sending as final-memory entry. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Fails closed by: ACCEPTED — Entry must satisfy existing identity, privacy/capture-exclusion, provenance and intake protections; deliberate sending alone is insufficient. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]

TOGETHER
- Fed by: DESIGNED — C-23.5 — Manual Sync: supplies the deliberately transferred sync item. [V10 §23]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): owns the sole ordinary intake envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): retains privacy and capture-exclusion precedence. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Changes: ACCEPTED — C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: receives the caller's normal root-writing request. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.6 — Mobile security requirements
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The five non-negotiable mobile boundaries: real authentication, no raw phone commands, encrypted local data, reviewed phone entry and no automatic real-N.H connection. [V10 §23]
- Takes in: DESIGNED — Full Mode access, phone-originated content and all locally stored data. [V10 §23]
- Does: DESIGNED — Keeps those five requirements applicable across mobile modes. [V10 §23]
- Gives out: DESIGNED — Deliberately bounded remote access and protected local/transfer behavior. [V10 §23]
- Must never: DESIGNED — Assume a password somewhere gates the tunnel, execute raw OS commands, store local data unencrypted, bypass SIMULATION review or auto-connect the local AI. [V10 §23]
- Fails closed by: DESIGNED — Full Mode requires real authentication; phone data cannot bypass review and the two deliberate doors. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: excludes every automatic real-N.H bridge. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): constrains every mode and transfer. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.6.2 — Raw phone-command prohibition | Phone-originated command input. [V10 §23] | Excludes nh_pc_agent.py's run: trigger and direct os.system() execution from the mobile design. [V10 §23] | No permitted raw-OS-command path from the phone. [V10 §23] | [V10 §23] |

SUB-PARTS: C-23.6.1 — Real tunnel authentication; C-23.6.2 — Raw phone-command prohibition

### C-23.6.1 — Real tunnel authentication
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — Actual wiring of Full Mode through nh_auth.py's existing PIN/token mechanism. [V10 §23]
- Takes in: DESIGNED — A deliberate opening request and the real authentication result. [V10 §23]
- Does: DESIGNED — Requires the tunnel itself to be gated by that authentication mechanism. [V10 §23]
- Gives out: DESIGNED — An authenticated Full Mode boundary, with exact wiring still unspecified. [V10 §23]
- Must never: DESIGNED — Assume the tunnel is safe merely because a password exists elsewhere. [V10 §23]
- Fails closed by: DESIGNED — The tunnel cannot be treated as authenticated without the real wiring. [V10 §23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.2.1 — Deliberate Full Mode opening: supplies the explicit user-triggered opening condition. [V10 §23]
- Changes: DESIGNED — C-23.2 — Mode 1 — Full Mode: constrains actual tunnel opening. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.2 — Mode 1 — Full Mode | Ness's explicit fingerprint, Face ID or PIN action and real authentication. [V10 §23] | Opens a Cloudflare tunnel for direct full-memory/full-engine live access during a window Ness deliberately creates and ends. [V10 §23] | A live remote Full Mode session. [V10 §23] | [V10 §23] |

SUB-PARTS: NONE

### C-23.6.2 — Raw phone-command prohibition
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The exclusion of raw OS command execution from phone input. [V10 §23]
- Takes in: DESIGNED — Phone-originated command input. [V10 §23]
- Does: DESIGNED — Excludes nh_pc_agent.py's run: trigger and direct os.system() execution from the mobile design. [V10 §23]
- Gives out: DESIGNED — No permitted raw-OS-command path from the phone. [V10 §23]
- Must never: DESIGNED — Extend, reuse or retain the raw run: trigger as the mobile command route. [V10 §23]
- Fails closed by: DESIGNED — Mobile/Full Mode go-live waits for outright removal and verified removal of the dangerous path. [MAP C-23]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — The run: trigger and its direct os.system() phone-input path must be removed and that removal verified before mobile/Full Mode go-live. [MAP C-23]
- Changes: DESIGNED — C-23.6 — Mobile security requirements: preserves the C11 pre-go-live boundary. [V10 §23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-23.12 — Full Mode mechanical design still open | NOT DECIDED. | Proceeds only when the C11 removal and verification is complete before go-live. | Nothing in this card. | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §6] |

SUB-PARTS: NONE

### C-23.7 — Protected voice-material transmission
Stamp: DESIGNED    Source: [V10 §25.3 / Raw Voice Data Protection]

ALONE
- What it is: DESIGNED — The artifact-specific transmission boundary for voice profile readings, acoustic roots and anti-spoofing readings. [V10 §25.3 / Raw Voice Data Protection]
- Takes in: DESIGNED — Protected identity/voice material under its local store protections. [V10 §25.3 / Raw Voice Data Protection]
- Does: DESIGNED — Allows external transmission only through Full Mode under biometric-verified conditions; access requires at least recognized_ness. [V10 §25.3 / Raw Voice Data Protection]
- Gives out: DESIGNED — A constrained protected-material path within Full Mode. [V10 §25.3 / Raw Voice Data Protection]
- Must never: DESIGNED — Expose the material below recognized_ness or transmit it outside the local device through another route. [V10 §25.3 / Raw Voice Data Protection]
- Fails closed by: DESIGNED — Without the required access level, biometric verification and Full Mode path, external transmission is unavailable. [V10 §25.3 / Raw Voice Data Protection]

TOGETHER
- Fed by: DESIGNED — C-SIA.13 — Protected raw voice and readings: supplies the protected-material boundary. [V10 §25.3 / Raw Voice Data Protection]
- Gated by: DESIGNED — C-SIA.13 — Protected raw voice and readings: requires recognized_ness and biometric-verified Full Mode transmission. [V10 §25.3 / Raw Voice Data Protection]
- Changes: DESIGNED — C-23.2 — Mode 1 — Full Mode: carries only transmissions satisfying the artifact's additional protections. [V10 §25.3 / Raw Voice Data Protection]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.8 — Accepted phone-control interfaces
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1]

ALONE
- What it is: ACCEPTED — The four accepted controls acting at the mobile boundary: Emergency Record, Stealth Toggle, Cloudflare Tunnel Off and Full Mode Kill Switch. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1]
- Takes in: ACCEPTED — Ness's deliberate control activations and their existing policy conditions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Keeps private phone capture distinct from transfer, and ordinary disconnection distinct from emergency desktop stopping. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Only the four accepted control effects, each within the two-door boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Recreate Breathing Reminder or Night Lockout as paused, renamed or deferred A22 features, or add replacement breathing, bedtime, focus, wellbeing or phone-usage restrictions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1]
- Fails closed by: ACCEPTED — No control creates a third connection door or an automatic connection. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]

TOGETHER
- Fed by: DESIGNED — C-9.3 — Phone-side feature scope: supplies the canonical accepted control policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: restricts every control's real-N.H connection. [V10 §23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): applies the controls at their mobile interfaces. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: C-23.8.1 — Emergency recording phone boundary; C-23.8.2 — Stealth phone boundary; C-23.8.3 — Ordinary remote-session disconnection; C-23.8.4 — Emergency Full Mode stop interface

### C-23.8.1 — Emergency recording phone boundary
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]

ALONE
- What it is: ACCEPTED — The mobile boundary of deliberate active-call recording. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Takes in: ACCEPTED — Ness's deliberately started recording and the single after-call choice. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Does: ACCEPTED — Keeps the recording private on the phone; exactly once after the call offers Keep private, Send whole call or Choose parts. Only deliberately selected excerpts are sent under Choose parts, visibly marked as part of a longer call. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Gives out: ACCEPTED — Private phone material or a deliberately selected whole/excerpt transfer toward real N.H. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Must never: ACCEPTED — Start automatically or silently, equate phone presence with N.H entry, or send through an A22-specific third door. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Fails closed by: ACCEPTED — Sending remains subject to existing identity, authorization, privacy/capture-exclusion, provenance and intake protections. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]

TOGETHER
- Fed by: ACCEPTED — C-9.3.1 — Emergency Record: owns deliberate recording and the three choices. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Gated by: ACCEPTED — C-9.3.7 — Phone recording transfer boundary: retains protected deliberate transfer through one of the two doors. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): keeps capture private until an authorized transfer. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.8.2 — Stealth phone boundary
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The mobile boundary of deliberately activated surrounding-voice/sound capture. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Takes in: ACCEPTED — Ness's activation, local recording/understanding and the choice when Stealth stops. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Does: ACCEPTED — Keeps recording and understanding private; may understand locally and show silent text, with no spoken/audible response. On stopping offers Keep private, Send whole recording or Choose parts; sent parts stay marked as excerpts. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Gives out: ACCEPTED — Private local material or a deliberate whole/excerpt transfer under the existing protections. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Must never: ACCEPTED — Activate automatically, speak/chime, let real N.H remember/use the material merely because Stealth ran, guess speakers or silently turn another person's statements into facts about Ness. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Material reaches real N.H only through deliberate sending and the existing protected two-door intake path. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9.3.3 — Stealth Toggle: supplies the canonical quiet-capture policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-9.3.7 — Phone recording transfer boundary: preserves attribution, privacy and ordinary intake. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]
- Changes: DESIGNED — C-23.3 — Independent local AI and memory: keeps local capture/understanding independent until permitted transfer. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.8.3 — Ordinary remote-session disconnection
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]

ALONE
- What it is: ACCEPTED — The mobile effect of Cloudflare Tunnel Off, an ordinary Full Mode session end. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Takes in: ACCEPTED — Ness's Tunnel Off activation. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Does: ACCEPTED — Closes the current tunnel, invalidates/ends the remote phone session and ends access through it; desktop N.H continues locally. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Gives out: ACCEPTED — Ended remote access with desktop operation and independent phone memory preserved. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Must never: ACCEPTED — Let anyone other than Ness activate it, shut down desktop N.H or Windows, stop/erase the local companion, alter memory/roots/readings/logs/records or reconnect automatically. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Fails closed by: ACCEPTED — New Full Mode access requires a new deliberate Ness action. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]

TOGETHER
- Fed by: ACCEPTED — C-9.3.6 — Cloudflare Tunnel Off: supplies the ordinary disconnect policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]
- Gated by: DESIGNED — C-23.1 — Two deliberate connection doors: requires deliberate reopening for any later session. [V10 §23]
- Changes: DESIGNED — C-23.2 — Mode 1 — Full Mode: ends the present remote connection window. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.8.4 — Emergency Full Mode stop interface
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]

ALONE
- What it is: ACCEPTED — The mobile effect of Ness's deliberate Full Mode Kill Switch. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Takes in: ACCEPTED — The explicit emergency activation and all five simultaneously applicable §7P stop conditions. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Does: ACCEPTED — Immediately ends phone access, closes the tunnel, rejects/invalidates the session, stops/locks desktop N.H and its active services, and prevents unfinished phone-originated steps where a bounded stop safely prevents additional effects. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Gives out: ACCEPTED — Stopped and locked desktop N.H with Windows powered on and independent local phone memory unchanged. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Must never: ACCEPTED — Power off Windows, delete or rewrite records/history, undo or claim to undo completed actions, send corrective messages/apologies/reversals/restorations/compensation, auto-restart/reconnect or weaken existing identity/access/privacy/gates/Layer-2 protections. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Fails closed by: ACCEPTED — Restart/reconnection requires new deliberate Ness action; completed-world correction is a separate action needing separate approval. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]

TOGETHER
- Fed by: ACCEPTED — C-9.3.5 — Full Mode Kill Switch: owns the emergency control and its protected outcomes. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Gated by: DESIGNED — C-7P.10 — Narrow pre-authorized emergency stop: requires ongoing action, prevention of further rather than completed effects, bounded previously authorized stopping, no reasonably larger consequence than continuing, and immediate recording/surfacing of the stop and authority basis. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]
- Changes: DESIGNED — C-23.2 — Mode 1 — Full Mode: ends active remote access without silently restoring it. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.9 — Mobile operational history
Stamp: DESIGNED    Source: [MAP C-23]

ALONE
- What it is: DESIGNED — The §0B record of tunnel, sync and local-learning activity. [MAP C-23]
- Takes in: DESIGNED — Actual Full Mode opens/closes, Manual Sync events and gate outcomes, and local-AI learning updates. [MAP C-23]
- Does: DESIGNED — Records each event with the clear boundary that local records never silently enter real N.H; access remains subject to privacy and applicable identity/security authorization. [MAP C-23]
- Gives out: DESIGNED — Traceable mobile operational records. [MAP C-23]
- Must never: DESIGNED — Treat recording an event as permission to send local material or access protected records. [MAP C-23]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): governs use/access of these records. [MAP C-23]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): preserves the history of actual mobile activity. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-23.9.1 — Tunnel-open event | An actual deliberately opened tunnel. [MAP C-23] | Records the opening event under the mobile operational boundary. [MAP C-23] | A Full Mode opening record. [MAP C-23] | [MAP C-23] |
| 2 · DESIGNED | C-23.9.2 — Tunnel-close event | An actual tunnel close. [MAP C-23] | Records the closed connection window. [MAP C-23] | A Full Mode closure record. [MAP C-23] | [MAP C-23] |
| 3 · DESIGNED | C-23.9.3 — Sync event and gate outcome | An actual sync and the associated gate result. [MAP C-23] | Keeps the transfer event and gate outcome attributable. [MAP C-23] | A sync record with the actual gate outcome. [MAP C-23] | [MAP C-23] |
| 4 · DESIGNED | C-23.9.4 — Local learning-update event | An actual learning update in the independent phone companion. [MAP C-23] | Records the local update without moving that material into the real store. [MAP C-23] | A local learning-update record. [MAP C-23] | [MAP C-23] |

SUB-PARTS: C-23.9.1 — Tunnel-open event; C-23.9.2 — Tunnel-close event; C-23.9.3 — Sync event and gate outcome; C-23.9.4 — Local learning-update event

### C-23.9.1 — Tunnel-open event
Stamp: DESIGNED    Source: [MAP C-23]

ALONE
- What it is: DESIGNED — The record of each Full Mode tunnel opening. [MAP C-23]
- Takes in: DESIGNED — An actual deliberately opened tunnel. [MAP C-23]
- Does: DESIGNED — Records the opening event under the mobile operational boundary. [MAP C-23]
- Gives out: DESIGNED — A Full Mode opening record. [MAP C-23]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.9 — Mobile operational history: supplies event-record and access rules. [MAP C-23]
- Changes: DESIGNED — C-23.2 — Mode 1 — Full Mode: makes its actual opening traceable. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.9.2 — Tunnel-close event
Stamp: DESIGNED    Source: [MAP C-23]

ALONE
- What it is: DESIGNED — The record of each Full Mode tunnel closure. [MAP C-23]
- Takes in: DESIGNED — An actual tunnel close. [MAP C-23]
- Does: DESIGNED — Records the closed connection window. [MAP C-23]
- Gives out: DESIGNED — A Full Mode closure record. [MAP C-23]
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.9 — Mobile operational history: retains the record under access rules. [MAP C-23]
- Changes: DESIGNED — C-23.2.2 — Deliberate Full Mode closure: preserves its actual closure event. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.9.3 — Sync event and gate outcome
Stamp: DESIGNED    Source: [MAP C-23]

ALONE
- What it is: DESIGNED — The record of each Manual Sync event and its gate outcome. [MAP C-23]
- Takes in: DESIGNED — An actual sync and the associated gate result. [MAP C-23]
- Does: DESIGNED — Keeps the transfer event and gate outcome attributable. [MAP C-23]
- Gives out: DESIGNED — A sync record with the actual gate outcome. [MAP C-23]
- Must never: DESIGNED — Equate transfer with successful memory entry. [MAP C-23]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.9 — Mobile operational history: preserves the local-to-real boundary in the record. [MAP C-23]
- Changes: DESIGNED — C-23.5 — Manual Sync: makes its transfer and review result traceable. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.9.4 — Local learning-update event
Stamp: DESIGNED    Source: [MAP C-23]

ALONE
- What it is: DESIGNED — The record of each local-AI learning update. [MAP C-23]
- Takes in: DESIGNED — An actual learning update in the independent phone companion. [MAP C-23]
- Does: DESIGNED — Records the local update without moving that material into the real store. [MAP C-23]
- Gives out: DESIGNED — A local learning-update record. [MAP C-23]
- Must never: DESIGNED — Use logging as a hidden sync or desktop-memory write. [MAP C-23]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-23.9 — Mobile operational history: protects the local-record boundary. [MAP C-23]
- Changes: DESIGNED — C-23.4 — Mode 2 — Local AI online: retains its actual local-learning history. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.10 — Layer-2 mobile coexistence
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]

ALONE
- What it is: ACCEPTED — Preservation of the active Layer-2 REALITY/SIMULATION gate while mobile and later layer designs coexist. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Takes in: ACCEPTED — Mobile operations crossing or approaching the real-N.H boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Does: ACCEPTED — Keeps Layer 2 active and protected until Ness explicitly authorizes decommissioning; A24/B-INT-10 retain the cross-layer handoff scope. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Gives out: ACCEPTED — Mobile transfers within the existing protected layer boundary. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Must never: ACCEPTED — Assume migration, weaken Layer 2 or turn component design into a completed cross-layer sync cycle. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Fails closed by: ACCEPTED — No phone material bypasses the active Layer-2 promotion gate. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — Ness must separately and explicitly authorize Layer-2 decommissioning. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7]
- Changes: DESIGNED — C-23 — Mobile App, three modes (§23): preserves current layer ownership during coexistence. [MAP C-23]

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.11 — Mobile policy choices still open
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The unselected on-device model, local memory format, background-platform feasibility and Manual-Sync content scope. [V10 §23]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: C-23.11.1 — On-device model choice; C-23.11.2 — Local memory format; C-23.11.3 — Mobile background-platform feasibility; C-23.11.4 — Manual-Sync content scope

### C-23.11.1 — On-device model choice
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The small phone-model choice remains open, including the size/quality tradeoff for phone hardware. [V10 §23]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.11.2 — Local memory format
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The exact format and structure of local AI memory on the phone remain unspecified. [V10 §23]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.11.3 — Mobile background-platform feasibility
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — The iOS-versus-Android differences for continuously running the local model in the background remain open. [V10 §23]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.11.4 — Manual-Sync content scope
Stamp: DESIGNED    Source: [V10 §23]

ALONE
- What it is: DESIGNED — Whether Manual Sync sends the whole local memory or only new entries since the previous sync remains open under A20. [V10 §23]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY (one row per place; the same part may appear in several paths)
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|

SUB-PARTS: NONE

### C-23.12 — Full Mode mechanical design still open
Stamp: ACCEPTED    Source: [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §6]

ALONE
- What it is: ACCEPTED — B30's exact authentication, secure commands, failing/frozen/unreachable tunnel behavior, tunnel lifecycle, session invalidation, service-stop order, unfinished-operation handling, accidental activation, button/label/icon/placement choices, identities, append-only logs, idempotency, duplicate prevention, timeouts/failures, crash/partial-stop recovery, actual-stop verification, how the no-larger-consequence emergency-stop condition is tested/thresholded/detected/enforced, and deliberate restart/reconnection mechanics remain unspecified. C11 removal and verified removal of the raw phone run: path remains a pre-go-live dependency. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §6]
- Takes in: NOT DECIDED
- Does: NOT DECIDED
- Gives out: NOT DECIDED
- Must never: NOT DECIDED
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-23.6.2 — Raw phone-command prohibition: the C11 removal and verification is complete before go-live. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §6]
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
| C-9.3 — Phone-side feature scope | C-23 — Mobile App, three modes (§23) | Fed by | DESIGNED — C-9.3 — Phone-side feature scope: provides the accepted phone controls without creating another connection door. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §7] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-23 — Mobile App, three modes (§23) | Changes | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): receives eligible mobile captures through the ordinary front door. [MAP C-7E] | Pending endpoint placement |
| C-9.3.6 — Cloudflare Tunnel Off | C-23.2.2 — Deliberate Full Mode closure | Fed by | ACCEPTED — C-9.3.6 — Cloudflare Tunnel Off: supplies the ordinary disconnect control. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | C-23.5.3 — Mobile root-entry caller contract | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): owns the sole ordinary intake envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): retains privacy and capture-exclusion precedence. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-23.5.3 — Mobile root-entry caller contract | Gated by | DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): owns the sole ordinary intake envelope; C-7Q — Privacy, Deletion, Sensitive-data (§7Q): retains privacy and capture-exclusion precedence. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Pending endpoint placement |
| C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture | C-23.5.3 — Mobile root-entry caller contract | Changes | ACCEPTED — C-STORE.4 — B11 — Active Writable-Batch / Sealed Multi-Box Architecture: receives the caller's normal root-writing request. [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] | Pending endpoint placement |
| C-SIA.13 — Protected raw voice and readings | C-23.7 — Protected voice-material transmission | Fed by | DESIGNED — C-SIA.13 — Protected raw voice and readings: supplies the protected-material boundary. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-SIA.13 — Protected raw voice and readings | C-23.7 — Protected voice-material transmission | Gated by | DESIGNED — C-SIA.13 — Protected raw voice and readings: requires recognized_ness and biometric-verified Full Mode transmission. [V10 §25.3 / Raw Voice Data Protection] | Pending endpoint placement |
| C-9.3 — Phone-side feature scope | C-23.8 — Accepted phone-control interfaces | Fed by | DESIGNED — C-9.3 — Phone-side feature scope: supplies the canonical accepted control policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] | Pending endpoint placement |
| C-9.3.1 — Emergency Record | C-23.8.1 — Emergency recording phone boundary | Fed by | ACCEPTED — C-9.3.1 — Emergency Record: owns deliberate recording and the three choices. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Pending endpoint placement |
| C-9.3.7 — Phone recording transfer boundary | C-23.8.1 — Emergency recording phone boundary | Gated by | ACCEPTED — C-9.3.7 — Phone recording transfer boundary: retains protected deliberate transfer through one of the two doors. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Pending endpoint placement |
| C-9.3.3 — Stealth Toggle | C-23.8.2 — Stealth phone boundary | Fed by | ACCEPTED — C-9.3.3 — Stealth Toggle: supplies the canonical quiet-capture policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Pending endpoint placement |
| C-9.3.7 — Phone recording transfer boundary | C-23.8.2 — Stealth phone boundary | Gated by | ACCEPTED — C-9.3.7 — Phone recording transfer boundary: preserves attribution, privacy and ordinary intake. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Pending endpoint placement |
| C-9.3.6 — Cloudflare Tunnel Off | C-23.8.3 — Ordinary remote-session disconnection | Fed by | ACCEPTED — C-9.3.6 — Cloudflare Tunnel Off: supplies the ordinary disconnect policy. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Pending endpoint placement |
| C-9.3.5 — Full Mode Kill Switch | C-23.8.4 — Emergency Full Mode stop interface | Fed by | ACCEPTED — C-9.3.5 — Full Mode Kill Switch: owns the emergency control and its protected outcomes. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-7P.10 — Narrow pre-authorized emergency stop | C-23.8.4 — Emergency Full Mode stop interface | Gated by | DESIGNED — C-7P.10 — Narrow pre-authorized emergency stop: requires ongoing action, prevention of further rather than completed effects, bounded previously authorized stopping, no reasonably larger consequence than continuing, and immediate recording/surfacing of the stop and authority basis. [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Pending endpoint placement |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | C-23.9 — Mobile operational history | Gated by | DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): governs use/access of these records. [MAP C-23] | Pending endpoint placement |

## Cross-piece TOGETHER continuations for current uses

Each row identifies one current USED BY place. Existing reciprocal fields are credited only where inspected; other rows remain explicit continuation obligations, without inventing the future card’s box.

| Current USED BY owner | Using endpoint / path | Current use row | Source | Disposition |
|---|---|---|---|---|
| C-23 — Mobile App, three modes (§23) | C-7E — Catalog Front Door + pre-ingest holding (§7E) | 15 · DESIGNED | [V10 §7E / MINIMUM INTAKE ENVELOPE] [MAP C-7E] [V10 §7E / DESIGN BOUNDARY] [V10 §7E / PRE-INGEST HOLDING AREA] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §7.1] [04/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md §13] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9 — Access/authentication model + voice I/O + phone modes (§9) | 16 · DESIGNED | [V10 §9] [MAP C-9] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3 — Phone-side feature scope | 17 · DESIGNED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §1] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.1 — Emergency Record | 18 · ACCEPTED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.3 — Stealth Toggle | 19 · ACCEPTED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §3] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.5 — Full Mode Kill Switch | 20 · ACCEPTED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §5] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.6 — Cloudflare Tunnel Off | 21 · ACCEPTED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §4] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.7 — Phone recording transfer boundary | 22 · ACCEPTED | [04/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md §2] | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-9.3.9 — Unspecified phone-control mechanics | 23 · ACCEPTED |  | Existing TOGETHER relationship checked in earlier card |
| C-23 — Mobile App, three modes (§23) | C-SIA.13 — Protected raw voice and readings | 24 · DESIGNED | [V10 §25.3 / Raw Voice Data Protection] | Existing TOGETHER relationship checked in earlier card |

## Source-to-card coverage added by CH10-d

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §23, DD §3L, Companion embedded §23, Map C-23 | C-23 root; two-door boundary; Mode 1 live tunnel and deliberate opening/closure; one independent local AI with online/offline states; no-memory offline branch; Manual Sync; all five non-negotiable security requirements and exact open choices. |
| V10 §25.3 Raw Voice Data Protection | C-23.7 protected acoustic/voice/anti-spoofing material transmission seam; only Full Mode and biometric verification, with at least recognized_ness; keep this artifact-specific restriction separate from generic phone content. |
| Accepted A22 v1_1 and its receipt, both WHOLE | Consume existing C-9.3 through four mobile interface cards, retaining private capture, no third door, ordinary disconnect versus emergency hard stop, complete must-not boundaries and separate restart. C-9 owns all menus, provenance and five emergency-stop conditions already written. Source policy remains ACCEPTED despite frozen candidate header; formal receipt closure wording not silently promoted. |
| B11 §13 caller matrix, accepted A22 §2/§3 | Mobile sync-item caller supplies seven-field payload, eligibility/authorization/blocker-clearance references, stable identity basis and provenance; receives outcome/root/batch identities. Existing Catalog and B11 own actual intake and write mechanics. Full cross-layer CY-H remains CH11, not inferred. |
| Map A20/B30/C11/A24/B-INT-10 and A22 §6/§7 | Named mobile open-policy and mechanical slots; verified raw run-path removal prerequisite; Layer-2 gate remains protected; no handoff or source-operation timeout invented. |
| Map C-23 §0B | Tunnel opening/closure, Manual Sync event and gate outcome, local learning-update records and no silent local→real crossing; exact schemas still open. |
| Source conflicts | Map biometric-only Manual-Sync wording versus V10/DD PIN alternative; Map A20-settled status versus still-open specific choices; inherited five phone-name inventory versus accepted A22 removals/addition. Preserve all, no reconciliation. |
| Earlier endpoints | Ten incoming fields across ten places; no existing C-23 USED BY rows. New relationships receive exact-name reciprocal rows and cross-piece continuations. |
| Twenty discovery matches | Accepted interface/room policies leave mobile integration open for CH10-e; AIC/kernel/framework packages leave mobile policy unchanged; decision indexes navigate; ledger only Appendix B; prior restored personality/power-switch names remain canonical C-9.3.8. No new runtime from historical or future idea notes. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | §13 caller/callee matrix and §7.1 boundary read in scope; canonical B11 retains schema/write ownership. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Exclusion of mobile/voice construction inspected; no mobile implementation inferred. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Mobile relation/open-question paragraphs inspected; unaccepted VR ideas supply no mobile mechanics. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Discovery-only matching titles/classifications; ledger feeds Appendix B, not behavior; no whole-file reread credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Recovery boundary/group scopes inspected; restored phone names retain canonical C-9.3.8 placement. No new archive restoration. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |

## Appendix A carry-forward — this piece

| Part | Field |
|---|---|
| C-23.1 — Two deliberate connection doors | Fed by |
| C-23.2 — Mode 1 — Full Mode | Fed by |
| C-23.2.1 — Deliberate Full Mode opening | Fed by |
| C-23.2.1 — Deliberate Full Mode opening | Gated by |
| C-23.3 — Independent local AI and memory | Fed by |
| C-23.3.1 — Separate encrypted local memory | Fails closed by |
| C-23.3.1 — Separate encrypted local memory | Fed by |
| C-23.4.1.1 — Offline with no usable local memory | Fed by |
| C-23.5.1 — Pre-send confirmation | Fed by |
| C-23.6 — Mobile security requirements | Fed by |
| C-23.6.1 — Real tunnel authentication | Fed by |
| C-23.6.2 — Raw phone-command prohibition | Fed by |
| C-23.9 — Mobile operational history | Fails closed by |
| C-23.9 — Mobile operational history | Fed by |
| C-23.9.1 — Tunnel-open event | Must never |
| C-23.9.1 — Tunnel-open event | Fails closed by |
| C-23.9.1 — Tunnel-open event | Fed by |
| C-23.9.2 — Tunnel-close event | Must never |
| C-23.9.2 — Tunnel-close event | Fails closed by |
| C-23.9.2 — Tunnel-close event | Fed by |
| C-23.9.3 — Sync event and gate outcome | Fails closed by |
| C-23.9.3 — Sync event and gate outcome | Fed by |
| C-23.9.4 — Local learning-update event | Fails closed by |
| C-23.9.4 — Local learning-update event | Fed by |
| C-23.10 — Layer-2 mobile coexistence | Fed by |
| C-23.11 — Mobile policy choices still open | Takes in |
| C-23.11 — Mobile policy choices still open | Does |
| C-23.11 — Mobile policy choices still open | Gives out |
| C-23.11 — Mobile policy choices still open | Must never |
| C-23.11 — Mobile policy choices still open | Fails closed by |
| C-23.11 — Mobile policy choices still open | Fed by |
| C-23.11 — Mobile policy choices still open | Gated by |
| C-23.11 — Mobile policy choices still open | Changes |
| C-23.11.1 — On-device model choice | Takes in |
| C-23.11.1 — On-device model choice | Does |
| C-23.11.1 — On-device model choice | Gives out |
| C-23.11.1 — On-device model choice | Must never |
| C-23.11.1 — On-device model choice | Fails closed by |
| C-23.11.1 — On-device model choice | Fed by |
| C-23.11.1 — On-device model choice | Gated by |
| C-23.11.1 — On-device model choice | Changes |
| C-23.11.2 — Local memory format | Takes in |
| C-23.11.2 — Local memory format | Does |
| C-23.11.2 — Local memory format | Gives out |
| C-23.11.2 — Local memory format | Must never |
| C-23.11.2 — Local memory format | Fails closed by |
| C-23.11.2 — Local memory format | Fed by |
| C-23.11.2 — Local memory format | Gated by |
| C-23.11.2 — Local memory format | Changes |
| C-23.11.3 — Mobile background-platform feasibility | Takes in |
| C-23.11.3 — Mobile background-platform feasibility | Does |
| C-23.11.3 — Mobile background-platform feasibility | Gives out |
| C-23.11.3 — Mobile background-platform feasibility | Must never |
| C-23.11.3 — Mobile background-platform feasibility | Fails closed by |
| C-23.11.3 — Mobile background-platform feasibility | Fed by |
| C-23.11.3 — Mobile background-platform feasibility | Gated by |
| C-23.11.3 — Mobile background-platform feasibility | Changes |
| C-23.11.4 — Manual-Sync content scope | Takes in |
| C-23.11.4 — Manual-Sync content scope | Does |
| C-23.11.4 — Manual-Sync content scope | Gives out |
| C-23.11.4 — Manual-Sync content scope | Must never |
| C-23.11.4 — Manual-Sync content scope | Fails closed by |
| C-23.11.4 — Manual-Sync content scope | Fed by |
| C-23.11.4 — Manual-Sync content scope | Gated by |
| C-23.11.4 — Manual-Sync content scope | Changes |
| C-23.12 — Full Mode mechanical design still open | Takes in |
| C-23.12 — Full Mode mechanical design still open | Does |
| C-23.12 — Full Mode mechanical design still open | Gives out |
| C-23.12 — Full Mode mechanical design still open | Must never |
| C-23.12 — Full Mode mechanical design still open | Fails closed by |
| C-23.12 — Full Mode mechanical design still open | Fed by |
| C-23.12 — Full Mode mechanical design still open | Changes |

## Named review dispositions

The complete behavior was reviewed for misfiled restrictions, failure outcomes and gates, including every USED BY row. Each positive scan hit below is retained for its named reason.

| Card / line | Flag | Reason |
|---|---|---|
| C-23.1 — Two deliberate connection doors; line 80 | plain_together / Gated by | Plain gate is Ness's deliberate personal connection act; no component owns that act. The two-door rule remains in the card's own Does field. |
| C-23.5.1 — Pre-send confirmation; line 331 | plain_together / Gated by | Plain gate is the explicit fingerprint/Face ID/PIN confirmation before sending, a personal act rather than a new component. |
| C-23.6.2 — Raw phone-command prohibition; line 443 | plain_together / Gated by | Plain gate is the source's verified raw-run-path removal prerequisite before go-live; no enforcement or removal implementation is invented. |
| C-23.10 — Layer-2 mobile coexistence; line 712 | plain_together / Gated by | Plain gate is Ness's separate express Layer-2 decommissioning authority, not an inferred migration mechanism. |
| C-23.11 — Mobile policy choices still open; line 733 | empty_together | Named open policy slots, not executable steps; source supplies no selected values or runtime relations. |
| C-23.11.1 — On-device model choice; line 755 | empty_together | Unselected on-device model slot, not an executable step; no model choice is invented. |
| C-23.11.2 — Local memory format; line 777 | empty_together | Unspecified local-memory representation slot, not an executable step; no schema is invented. |
| C-23.11.3 — Mobile background-platform feasibility; line 799 | empty_together | Unresolved platform feasibility slot, not an executable step; no platform capability is asserted. |
| C-23.11.4 — Manual-Sync content scope; line 821 | empty_together | Unselected transfer scope slot, not an executable step; whole-memory versus new-entry choice remains open. |
| C-23.12 — Full Mode mechanical design still open; line 844 | prerequisite_review / Gated by | Its Gated by line names C-23.6.2 (raw phone-command prohibition): the C11 removal and verification is complete before go-live, so its TOGETHER boxes are not empty. B30's mechanical scope stays expressly open; no transitions, enforcement, recovery, timeout or UI mechanics are invented. |

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

### Source placements added by CH09-g

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` §25.7 / Four States | C-PAIR.1 through .1.6: four exact states, every transition/condition, 90-second initial QR, state-2 permanent inertness/sealing, hardware binding, state-3 failure/timeout retry, state-4 four-condition finalization, final trust and permanent closure. |
| V10 §25.7 / What becomes permanently inert when | C-PAIR.1.2.1 signed QR; .1.2.2 temporary secret; .1.4.1 trust upgrade; .2.3.5 recovery-code local copy. The source's four artifact/time rows are all placed. |
| V10 §25.8 / First Recovery Code Creation | C-PAIR.2.1 through .2.1.5: immediate first creation, desktop encryption to phone key, phone-only biometric-approved decryption, phone-only display, no desktop/clipboard exposure, confirmation/10min30s hiding and clipboard clearing, old-valid/new-inactive timeout outcome. |
| V10 §25.8 / Save Verification | C-PAIR.2.2 through .2.2.5: Saved in Bitwarden trigger, exactly four unique random positions, requested order and exact case, three attempts, new positions after failure, local verification, all three unpersisted classes, terminal new-code inertness/old-code preservation/restart. |
| V10 §25.8 / Activation Handover | C-PAIR.2.3 through .2.3.6: all six steps in source order; four individual local-test prohibitions .2.3.2.1–.2.3.2.4; test-before-activation; new-active-before-old-invalid; immediate local-copy inaccessibility/sealing; Bitwarden as sole intended long-term store. |
| V10 §25.8 / Recovery Code Rotation | C-PAIR.2.4 and .3: every successful pairing/re-pairing triggers the same complete handover; old code stays valid until saving, verification, local test and activation all succeed. |
| V10 §25.9 | C-PAIR.3 through .3.4: both normal recovery factors, replacement by default, full pairing/verification before automatic prior-phone revocation, complete re-entry flow for a revoked phone, mandatory normal-code rotation. |
| V10 §25.10 / Required Factors | C-PAIR.4.1 through .4.1.3: four simultaneous factors, emergency code outside Bitwarden, printed sheet physically secure, unconditional remote prohibition. Existing BGMM physical-presence/thumbprint/code/sheet owners are reused by exact name. |
| V10 §25.10 / Intermediate State (Provisional Only) | C-PAIR.4.2 through .4.2.6: all six source invariants separately placed; new trust provisional; every old phone/code/sheet remains valid; no partial revocation. |
| V10 §25.10 / Required Steps Before Final Commit | C-PAIR.4.3 and .4.3.1–.4.3.3: normal code saved/four-character-verified/tested, emergency code saved/verified, printed sheet confirmed saved/verified. Normal-code testing is reused; activation is not pulled forward into preparation. |
| V10 §25.10 / Atomic Final Commit | C-PAIR.4.4 and .4.4.1–.4.4.7: sole new-phone permanent trust, all old phones revoked, each old code/sheet invalidated, simultaneous new-material activation and bai_emergency_reset_finalized in one atomic commit. |
| V10 §25.10 / If Any Step Fails Before Final Commit | C-PAIR.4.5 through .4.5.4.2: safe abort, all new material sealed/inert, provisional pairing cancelled, complete prior-authority preservation, bai_emergency_reset_aborted, failed-step and reason details without invented field names. |
| V10 §25.11 / Prerequisites (All Six Must Be True); §7L Integration | C-PAIR root enrollment use and .1.6: four pairing-owned prerequisites; exact bai_initial_setup_finalized owner-phone trust reference in the provisional link basis. Full enrollment mechanism remains CH09-h; C-7L.11.5 remains the existing provisional-link basis owner. |
| V10 §25.6 / Purpose Binding | C-PAIR.1.2.3 reuses C-BAI.3.8 app_session_key_ref; hardware-backed keystore trust, no OS device-ID substitution. Canonical biometric artifacts remain CH09-e. |
| V10 §25.13 / Protected Material Boundary; Entering Maintenance Mode; Purpose-Specific Authorization | C-PAIR root, .3.1 and .4.1 reuse the exact existing BGMM authorities/factors. Eleven incoming fields from ten earlier cards are reciprocated. Device-trust/emergency authority never extends to emergency code/configuration writes. |
| V10 §§2/2A and §0B | C-PAIR root gates all 51 distinct C-2 interaction/delivery owners; .6 preserves connected permanent operation recording, one-operation-one-log, no double evidence and Level-1 secrecy/access limits. No project workflow is imported. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` C-PAIR | Exact root name and full handover/replacement/emergency wiring; .6/.6.1–.6.4 place every named audit-operation category and its authorization limits. |
| Map C-2 and CY-I | Root C-2 gate and its 50 subcard reciprocity obligations; ordinary and CY-I BGMM uses are preserved. Complete side-path assembly remains CH11. |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` embedded security-design §§7–10 | Conflict header preserves stale destruction/erasure versus V10 sealing/inertness/inaccessibility at QR pairing, failed save check, activated local copy and aborted provisional emergency material. No older destructive behavior is adopted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` §§3–5 | C-PAIR.5/.5.1 preserve pairing-owner authority, four prerequisite facts, hardware identity, outer trust versus inner approval, live-owner revalidation and changed-prerequisite refusal/revocation. Full enrollment_prerequisite_snapshot [proposed], its fields and all six-owner coordination remain CH09-h. |
| B-INT-7 v1.1 §9 | C-PAIR.5.2: loss/replacement/revocation, invalid recovery/setup and QR/secret contradiction are actual owner events; enrollment stops before logging, preserves committed observations, excludes affected segments and never silently resumes. Full consumer protection mechanics remain CH09-h. |
| B-INT-7 v1.1 §13 | C-PAIR root USED BY C-7L.11.5 and .1.6 event basis: owner-phone trust is evidence for declared enrollment provenance, never confirmed voice identity. Existing Person-Box link ownership remains CH06-c. |
| B-INT-7 v1.1 §19 I1/I2; bounded §6A/§6D context | C-PAIR.5.1 states operation_ref and per-prerequisite owner_ref/owner_version/satisfied reference-only seam and owner re-reads. Complete I1/I2 schema atoms, snapshot and capture-start consumer records/mechanics remain CH09-h; no pairing owner acquires capture or coordinator authority. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` whole | Acceptance/version provenance checked; candidate filename and [proposed] labels retained. Frozen three wording notes and open implementation/threshold boundaries remain carried, with full enrollment treatment in CH09-h. Receipt prose is not system behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` B-INT-7 consolidation paragraph | Confirms trusted-phone enrollment wiring without adding pairing mechanics; full enrollment B-INT-7 ownership remains CH09-h. No unrelated consolidation scope claimed here. |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` and `01_AUTHORITATIVE/cursorrules` pairing-topic discovery | No additional pairing/recovery mechanism found in scoped topic discovery. No new whole-file read credit; project workflow excluded. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` §9.1 specialist-authority paragraph | Discovery hit retains BGMM for device-trust changes and §25 safeguards; these existing boundaries are consumed through canonical BGMM ownership, not a new pairing mechanism. Full permission/action ownership remains CH07-c. |
| All 04/05 files, by C-PAIR/full-name/pairing/recovery-code/trusted-phone/device-trust/Bitwarden discovery | B-INT-7, Bundle 4 and Bundle 5 consolidation match these scoped topics; no separate later pairing package or recovery decision found. Discovery is not whole-file reading; the restoration ledger is excluded from behavior discovery. |
| Remaining owners | Full enrollment coordinator and schema atoms CH09-h; full modes CH09-i; full durable-operation kernel CH10-b; side-path assembly CH11; script-regenerated final registers CH12. No unstated code format, emergency-check algorithm, QR-expiry regeneration route or crash implementation is selected. |

### Source placements added by CH09-h

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §25.11; Map C-ENROLL | C-ENROLL retains the exact Map name and DESIGNED status. Full initial enrollment flow is placed through .1–.16; specialist authorities remain separate. All 22 earlier incoming fields across 19 places are reciprocated; all 13 inspected earlier uses receive root relationships. |
| V10 §25.11 / Prerequisites; B-INT-7 v1.1 §4 | C-ENROLL.2 and .2.1–.2.6 place all six conditions. Pairing facts reuse C-PAIR.1.2.1/.1.2.2/.1.4.1/.1.4.2/.1.6/.2.3/.5.1; SIA/SACL own spoofing and Gate 0; C-7L.4 owns confirmed Ness-box truth. |
| B-INT-7 §4 snapshot and §19 I2 | C-ENROLL.2.7 and its children: snapshot_id, snapshot_version, six per-owner entries, owner_ref, owner_version/current event identity, satisfied, taken_at and boolean all_six_satisfied. C-ENROLL.2.8 owns the operation_ref request seam. No snapshot becomes authority; failed initial checks prevent the BAI call. |
| B-INT-7 §3 | C-ENROLL.1 owns coordination only. Phone, recovery, QR, spoofing, box, biometric session, identity/access, privacy, root, queue and profile authority remain at their actual owners; outer trusted-phone binding and inner biometric approval are not named identity. |
| B-INT-7 §5 steps 1–3; §17; §19 I1 | C-ENROLL.3/.3.1–.3.5: dedicated trusted-phone flow, explicit_begin_event_ref, trusted_phone_binding_ref, stable proposed parent and prospective session identities, proposed begin claim, no authority from reservation, anti-double-tap identity and refusal/recovery outcomes. |
| B-INT-7 §5 steps 4–10; §19 I3/I4 | C-ENROLL.4/.4.1/.4.2/.4.4: full ordered request, BAI-only pending/prompt/token, immediately fresh owner recheck, revocation without consumption on change, verified flushed proof then opening then capture. Exact purpose/requester/operation_ref/session_ref and pending_id/refusal/token_ref/failure forms are present. Existing C-BAI.19.1–.19.4 remain canonical authorization/proof owners. |
| B-INT-7 §6A | C-ENROLL.4.3 and eleven field cards carry the complete durable chain and binding: proposed operation/session IDs; separate token/pending refs; exact purpose; app_session_key_ref; snapshot ref; BAI trusted-local timestamps; requester; audit schema/version; integrity reference. The proposed append-only companion references the BAI event and is referenced by that event or opening. No secrets or new biometric authority. |
| B-INT-7 §6B | C-ENROLL.4.5 and eight children place every duplicate barrier: one begin/two sessions, two proofs/one session, one proof/two sessions, old unmatched result, changed prerequisite, absent flushed proof, stale snapshot and concurrent BAI pending. |
| B-INT-7 §6C; receipt §6 wording note 2 | C-ENROLL.4.6/.4.7 and .6.14 preserve no-session spent-proof abort versus an actually opened session with confirmed zero capture. The former uses the proposed abort event, never a fictitious session-close event; both prohibit silent microphone activation. |
| B-INT-7 §6D; §19 I5A | C-ENROLL.5/.5.1–.5.5: current opening/privacy/security/no-stop conjunction; flushed proposed intent before request; seven reference-only request classes, each placed; exact started/confirmed_not_started/unknown results, separately placed; B29-sourced proposed start fact. Intent, start and observations remain distinct, with every stated crash outcome and no inferred non-start. |
| B-INT-7 §7; V10 §25.11 BOP Integration; §25.12; §19 I5B/I5C | C-ENROLL.5.3.5/.5.6/.5.7 consume canonical C-BOP.15 and C-BAI.19.6. role=ness is declared; source_title=enrollment:ness:<session_id>; session_authorization.authorization_type=enrollment_declared is formally adopted. Exactly one BAI-sourced biometric:result:success observation with session ID and trusted-local timestamp; deterministic capture_id from session/opening/command. Canonical C-BOP.15.3.1/.15.3.2 retain the two fields; forbidden purpose/token/biometric/authorization/identity payloads remain absent. |
| B-INT-7 §7 A15 boundary | C-ENROLL.5.6 names C-BOP.12, the already placed six-field/five-name acoustic-condition amendment owner. Those atoms remain there; h preserves physical context only and all ten prohibited conclusions: identity, speaker change, spoofing, imitation risk, emotion, intent, meaning, importance, behavioral pattern and causation. |
| B-INT-7 §8 | C-ENROLL.6.1–.6.27 place all 27 exact proposed state labels, splitting both combined table pairs. Every entry fact, actual owner and outcome is written. The combined closing/closed source condition is preserved without inventing an intermediate commit rule. |
| B-INT-7 §8A/§8B | C-ENROLL.6.28/.6.29: separate capture-session/parent lifecycles; valid unaffected material can continue after closure/interruption; only legal nonterminal transitions; no regression of committed observations/roots/readings/eligibility/link/profile; absorbing parent terminals; at most one winner; no state inferred from coordination. The source's abort shorthand is bounded by §6C and the receipt. |
| B-INT-7 §9 | C-ENROLL.7/.7.1–.7.8 place all eight owner-event groups, explicitly retaining loss/replacement/revocation, recovery/setup and QR/secret alternatives. Stop precedes logging; only committed observations are preserved; no reconstruction or affected-segment training; honest closure/interruption; no same-session resumption; no TSC lifecycle/database/archive authority reuse. |
| B-INT-7 §10; §19 I6–I9 | C-ENROLL.8/.8.1–.8.4 carry all ten close/freeze/Catalog/B11/append/duplicate/root_id/queue/quarantine steps. I6 actual observations to immutable set; I7 frozen capture_ids+provenance and accepted/rejected/blocked; I8 capture_id-derived identity+validated root fields+ingest_operation_id and root_id/append_duplicate_absorbed/rejected/indeterminate; I9 root_id/enqueued. Canonical C-BOP.13.1, C-STORE.3.5/.4.6.2.1/.4.6.2.3, C-7E, C-7GA and C-READ.11 retain their existing schema/fence/queue atoms. No duplicate writer or queue is introduced. |
| B-INT-7 §11; §19 I10 | C-ENROLL.9/.9.1–.9.6 carry all six checks; .9.6.1–.9.6.5 carry every stream-integrity condition, including threshold over the FULL segment. Authorization requires enrollment_declared plus session_id linked to confirmed durable bai_token_consumed. overall_completeness is exactly complete or partial. Stream consistency never establishes who spoke. |
| B-INT-7 §§11/17/20 | C-ENROLL.9.7/.9.8 and field children place proposed immutable segment and eligibility-decision identities, one outcome per segment, accepted/rejected event mirroring, reason and source references without audio. Replay recovers the prior decision; rejection preserves roots and prevents training. |
| B-INT-7 §12; §19 I11 | C-ENROLL.10/.10.1–.10.4: accepted quarantine readings only; counted_reading_refs set keyed by reading identity; each eligibility-decision ref; readiness outcome; unavailable-rule, unverifiable-set and missing-decision failures; no numbers/durations/thresholds/algorithms; no rejected-as-valid or invented insufficient_context reading; no A29 substitution; no link/profile if not ready. |
| B-INT-7 §12A; §17 | C-ENROLL.10.5 and five permitted input classes: exact eligible accepted reading refs, eligibility decisions, operation/session refs, prerequisite/authorization evidence, readiness ref. One proposed immutable bundle per readiness outcome; recover the same bundle on replay. Coordination only, no profile/store/identity evidence. |
| B-INT-7 §13; §19 I12; V10 §25.12 | C-ENROLL.11/.11.1 use all canonical C-7L.11 field owners by exact name: link_type=enrollment_material_provisional, certainty=enrollment_provisional, proposed stable proposal ID, provenance-only meaning, three-part basis, bundle/confirmed box/operation/session/readings/eligibility/prerequisite references. Proposal recorded is separate from committed/refused/pending outcome; current committed link required; refused/pending/stale/contradictory/unverifiable outcomes remain individually owned in C-7L.11.13.1–.13.6. |
| B-INT-7 §14; §17; §19 I13 | C-ENROLL.11.2/.11.3 and canonical C-SIA.20 retain the proposed idempotent build identity keyed to committed link+linked reading set, SIA-owned commitment before creation event, enrollment_provisional status, recognized_ness ceiling without grant, five dimensions weighted above acoustic until enrollment_active, ordinary later training and unknown/guest restart. C-ENROLL.6.25 requires both commits and both enrollment events for completion. |
| B-INT-7 §§15/16; §19 I14; B-INT-5 §5B | C-ENROLL.12 reuses C-SIA.20.8/C-BOP.15.6 and names privacy/SACL/mode gates. All enrollment-alone authority prohibitions are written; privacy precedes capture; minimum protected raw-voice boundary; references/structural facts only; no ordinary-component sensitive payload merely for rejection; no indirect disclosure or reconstructive logs; final privacy-first/access-second/fence-revalidated output. Enrollment purpose never opens Personal Mode. |
| B-INT-7 §17, all 17 identity rows | Proposed parent/session/begin claim .3; BAI pending/token C-BAI.19.1; snapshot .2.7; proposed segment and decision .9.7/.9.8; BOP capture_id and B11 ingest_operation_id .8.3 with canonical owners; queue/read refs .8.4; proposed readiness .10; proposed bundle .10.5; proposed proposal ID .11.1; proposed build identity .11.2; capture-control/intent/start .5; proposed recovery identity .13.3.1. One-parent/many-children/no-extra-weight rule .13. |
| B-INT-7 §18 | C-ENROLL.14 and nine event children preserve every exact settled enrollment event. Additional proposed abort/intent/B29-start names remain separate at .4.6/.5.2/.5.5, not mislabeled settled events. BAI and every other owner keep their events. Required write/flush precedes owner success; .16.3 handles failure. |
| B-INT-7 §20, all 13 proposed record kinds | Intent .5.2; bundle .10.5; parent operation .13.1 with identity/state/terminal reason/audit-ref atoms; stage event .13.2; begin claim .3.4; snapshot .2.7; authorization binding .4.3; capture set .8.1; segment .9.7; eligibility decision .9.8; readiness .10; recovery event .13.3 with identity/boundary atoms; duplicate absorbed .13.4. All are append-only reference-only non-authorities with no evidence weight. |
| B-INT-7 §21, every crash row | C-ENROLL.15.1–.15.7 map source rows 1–7; .15.8 maps inserted row 7b; .15.9–.15.21 map rows 8–20. Every committed-truth and exact recovery action is written. The table has 21 rows despite §20/§26 saying twenty; no row is omitted. I5C preserves BAI as sole recovered biometric-observation source. |
| B-INT-7 §22 | C-ENROLL.16/.16.1/.16.2: same-parent technical retry only when no fresh explicit action and no recreated security authority; all seven prohibited reuse classes; five fresh-session requirements; accepted B9 values consumed by reference with none invented. |
| B-INT-7 §23, all 16 failure groups | Bad prerequisite .2; pending conflict .4.5.8; unmatched result .4.5.4; unflushed proof .4.5.6; unverifiable binding .4.3; changed prerequisite .4.2; absent/current opening .5.1/.5.3.3; unsafe BOP capture .5.3.6/.5.6; privacy exclusion .7.7; Catalog nonacceptance .8.2; unverified append .8.3; unavailable eligibility owner .9; readiness failure .10.4; unavailable Person-Box/SIA .11; owner contradiction .15.21; required audit failure .16.3. Each outcome is explicit in the owning card; .16 retains the complete named list. |
| B-INT-7 §§0–2/24–26 and closure receipt whole | Authority/version/dependency and drafting/implementation instructions are provenance or excluded project workflow. System boundaries from §24 are placed in .1/.5/.8/.9/.11/.12/.13; still-open mechanics in §25 are explicitly assigned to CH09-i or remain unchosen. Receipt's three frozen minor notes and the actual 1066-line count are preserved in delivery records; no source is edited and no independent audit is claimed. |
| Full Bundle 5 consolidation v1.1 | Its enrollment scope and cross-package authority table support explicit begin plus BAI token, actual specialist owners, one-reference recordkeeping and no substituted authority. Other consolidated policy/mechanical details retain canonical earlier C-7Q/C-24/C-TSC/C-SACL/C-BAI/C-PAIR owners; full Personal Mode remains CH09-i. Receipt/history/closeout prose is excluded from behavior. |
| Companion embedded security §§11–12 | Header conflict retains V10 permanent QR/secret inertness instead of Companion destruction. Formally adopted enrollment_declared and enrollment_material_provisional vocabulary is placed through canonical BOP/Person-Box owners, without a second schema or older destructive behavior. |
| 04/05 discovery by C-ENROLL, full name, enrollment and bootstrap topics | All 15 matched paths classified. B-INT-7 and Bundle 5 read whole. B11 bootstrap hits describe historical sealed-batch registration, not enrollment; its root path is consumed through earlier canonical owners. Kernel dependency-list hit adds no new enrollment rule; full kernel CH10-b. Highest decision index v0_11 is navigation; v0_5/v0_6/v0_10 hits are superseded navigation. |
| Active decision/candidate matches | Synthetic-voice decision v0_2 reread whole: selected output voice is distinct from identity/enrollment; speech choices land CH09-i. Recovery buckets Group 6 is bootstrap reading and memory health, not voice capture, with no new archive use here. B16 EEB v1_7 §2.10 cites enrollment as an authority example and changes no enrollment policy; promotion/judgment rules retain earlier ownership. |
| Remaining owners and holes | Complete modes and still-open B29 mechanics CH09-i; full model/B24/kernel CH10-b; side-path assembly CH11; final script-generated registers CH12. No new prompt wording, sample/duration/quality/diarization/spoofing/readiness/activation value, hardware, channel, cleanup algorithm or serialization is selected. Gaps in this piece remain exact NOT DECIDED. |

### Authorized archive inventory additions — CH09-i

| Source | Read scope | Placement |
|---|---|---|
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER-5.md` | WHOLE authorized archive; exact permitted scope only | C-9.2.12 and C-9.3.8 restored candidate/tool and phone words under buckets Groups4/8; all other historical behavior excluded |
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER_CONTEXT.md` | WHOLE authorized archive; exact permitted scope only | C-9.2.12 and C-9.3.8 restored candidate/tool and phone words under buckets Groups4/8; all other historical behavior excluded |

### Source placements added by CH09-i

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §9; Map C-9 | C-9 and C-9.1 retain the exact Map name and DESIGNED root. Dry, Personal and graduated step-up, raw/derived separation, exact-original-words exception, authorized applications, zero-copy and actual code-level data separation are individually placed. |
| A26 §§2–4; B-INT-5 §§3–4 | C-9.5/.5.1/.5.2 place both cooperating authorities, all six policy clauses and the four-way restrictive intersection. Private-default exceptions reuse C-7Q.1.2.2/.6.1/.11.2. Recognition neither opens Personal Mode nor becomes an unconditional opening prerequisite. |
| B-INT-5 §6 | C-9.1.4 and its eight children place every factor-matrix row. Intent, PIN/fingerprint ordinary proof, SIA/SACL identity and safety, trusted-origin binding, sensitive-operation recheck, BAI lease and stronger verification remain distinct. The header retains lease-reuse conflict; PIN-only opening is not blocked by unrelated BAI outage. |
| B-INT-5 §§5/5A | C-9.6/.6.1–.6.12 place every opening step: intent and reservation, factor, atomic snapshot, binding, preparation flush, owner recheck, closed-fence activation, reserved-target opened-event flush, actual commit, release, indication and first private retrieval. C-9.6.14 preserves restriction before logging. |
| B-INT-5 §5B; canonical C-BAI.17 | C-9.6.13 places the eight-step fingerprint consumer path and every validation dimension. Exact purpose placeholders are retained by source context, including personal_mode_open_operation_id, open_operation_id and logging id variants; no cross-purpose token reuse or post-consumption crash reopening. |
| B-INT-5 §§7/7A | C-9.7/.7.1–.7.8 place proposed PMA, six state labels, fresh nonreused runtime epoch, monotonically increasing generation family, all stage-qualified identities and stale mismatch rules. Proposed qualifier is retained for every proposed name. |
| B-INT-5 §7B | C-9.7.9 and ten transition children place every transition row. C-9.7.8 owns sole allocation, reservation versus commit, current-base check and restrictive precedence; all five access-change kinds and forbidden transitions are explicit. The receipt's three frozen shorthands remain recorded outside behavior; exact opening sequence controls placement. |
| B-INT-5 §8 | C-9.8/.8.1–.8.4 and their children place all reduction actions, three safe lower-ceiling cases, six Ness-private safety-loss classes and future-only restoration exclusions. Canonical C-SACL owns operation sensitivity; no old answer or cancelled operation is resurrected. |
| B-INT-5 §§9/9A | C-9.9/.9.1/.9.2 place explicit close, idempotency, no durable destruction, exact dependency-scoped cancellation, independent background ownership and fresh delivery checks. Closing interactive mode grants no independent restart-survival promise. |
| B-INT-5 §10 | C-9.10/.10.1–.10.14 cover every row 1,2,3,4a–4e,5–10. Fresh Dry epoch, committed truth, restrictive recovery, spent-proof handling and exact failed/restart_interrupted/crash_interrupted proposed values are explicit; interrupted is not invented as a terminal state. |
| B-INT-5 §11 | C-9.11/.11.1–.11.3 place boundary/epoch singleton scope, same-key replay, different-key race, stage-specific fence and duplicate indication, plus all restrictive-wins cases. A new session ID is not a new singleton boundary. |
| B-INT-5 §12 preamble | C-9.12 separates authority from history, requires proposed schema_version, excludes all six protected/raw classes, and permits reference-linked corrections without in-place rewriting. Final serialization remains open. |
| B-INT-5 §12 record 1 | C-9.12.1 and field cards place all ten session fields with exact meanings and proposed names. The current-effective-access reference is null only in opening/no-personal-access, and shared boundary/epoch fields have single canonical definitions. |
| B-INT-5 §12 record 2 | C-9.12.2 and fields place parent identity/idempotency, six operation types, five conditional access-change kinds, current and reserved generations, trusted-origin/device references, seven states, named terminal reasons and audit references. Requiredness remains specific to this record. |
| B-INT-5 §12 record 3 | C-9.12.3 places all ten transition-event fields. The opened event truthfully records activation under a reserved target before operation commit; it allocates and commits no generation. Unspecified requiredness is not invented for transition_event_id, mode_session_ref or at. |
| B-INT-5 §12 record 4 | C-9.12.4 places every binding field and the full intent/proof/snapshot identity conjunction. Gate kind permits only pin or fingerprint; BAI purpose/proof fields are conditional; exact origin/device, freshness and timestamp fields remain distinct. |
| B-INT-5 §12 record 5 | C-9.12.5 places session/boundary/epoch/reserved-generation identity, mode permission, atomic SACL reference/version, both event IDs, stream-set identity and all seven per-stream fields; addressed/Ness/shared/PBR references, all four owner-held observability references, optional stronger-owner set, required effective_ceiling and computed_at. No blanket requiredness is added to computation time. |
| B-INT-5 §12 record 5 invalidation | C-9.12.5 invalidation card preserves every named assessment/freshness/level/disqualifier/stream/speaker/addressed/shared/PBR/presence/Gate0–3/channel/classification/observability/step-up change. Access changes or unsafe fences require a new generation; cached levels and cross-epoch references never suffice. |
| B-INT-5 §12 record 6 | C-9.12.6 and fields preserve complete prior/new epoch-generation pairs, all fourteen crash-boundary values, committed truth, three action values and reference-only history. Source expressions action_taken = closed_for_restart and operation_type = access_change are represented by separately qualified field and value names, without changing their meaning. |
| B-INT-5 §12 record 7; §14 | C-9.12.7 and C-9.14 place the reference-only stronger-authority link, required top-security BAI lease and Gate1 pair, event references, five observed states and permitted non-top-security reference set. No generic authority_ref or mode-owned step_up_active bit substitutes for actual owners. |
| B-INT-5 §12 record 8 | C-9.12.8 places all activation-ready fields, exact activation_ready result, one-per-operation identity and successful flush before activation. History creates no permission; binding, SACL, observability and effective snapshot references are current together. |
| B-INT-5 §12 record 9 | C-9.12.9 places dependency identity, dependent parent/owner/purpose, required boolean, conditional session/boundary/epoch/generation/snapshot, optional cancellation/correction references, delivery path, four states and time. The committed-generation field has no concrete source name and stays explicitly unnamed. |
| B-INT-5 §12A | C-9.12.10 reuses shared identities and places eight unique delivery-fence fields, closed/released vocabulary, monotonic version, scoped idempotency, conditional release/restrictive-close refs and latest authoritative event. Owner reset, repeated release, restrictive precedence and logging failure rules are explicit. |
| B-INT-5 §12B | C-9.12.11 and five seam cards place each owner-version revalidation requirement, actual owner pair and restrictive result on changed or unverifiable truth. |
| B-INT-5 §13; B-INT-6 §§3–5/6E/7A–7B/8/10/14 | C-9.13 produces the current mode/fence handoff and reuses canonical C-SACL.20 consumers. All eighteen consumer atoms are connected; privacy-first then access, exact payload, owner versions and every-write checks remain with their canonical owners. |
| B-INT-5 §15 | C-9.15 and seven indicator children place committed semantic states, separately verified stronger authority, secrecy and accurate restriction/restart indication. Exact display/UI wording remains open. |
| B-INT-5 §16 | C-9.16 and twenty-five mapping children place every operation/audit row, real parent, stages, recovery, replay and reference-only provenance. The source's elliptical effective-access-snapshot abbreviation denotes the full proposed personal_mode_effective_access_snapshot, not a new field. |
| B-INT-5 §§17–19 | C-9.17 and twenty-four failure children place each named class and safe outcome; source prohibitions are distributed to actual owners. C-9.18 preserves unchosen PIN/fingerprint/trusted-app implementation, durations, retries, UI and serialization as explicit gaps. Closure/build workflow is excluded. |
| V10 §9 voice; B-INT-7 §6D/§7/I5A–I5B | C-9.2 and six stages place microphone, cleanup, transcription, sensor/front-door handoff, Hebrew and English output. C-9.2.7–.2.10 place immediate TTS stop, B29 capture's seven reference classes/three outcomes, protected raw boundary and operation recording; C-ENROLL.5 and C-BOP.15 atoms remain canonical. B29 hardware/latency/algorithm mechanics remain open. |
| Speech-output decision §§2/3/5 | C-9.2.11 and eight setup children place BlueTTS, untouched vf_estimetor.safetensors, exports/export_onnx.py, onnx_author, voices/daniel.json, total_step=32, cfg_scale=2.0, renikud-plus 0.3.0, espeak-ng and PHONEMIZER_ESPEAK_LIBRARY/libespeak-ng.dll. Four constraint children preserve bilingual young male, not Ness, no emotional pull, local/offline. Candidate status is retained; experimental listening reports are excluded. |
| Buckets Group4 and Group8; authorized archive headings | C-9.2.12 and five children restore only Whisper/Piper/Coqui/noisereduce/librosa candidate names. C-9.3.8 and four children restore only research/emotional/strategic/power switch words. Every DECIDED-2026-09-25 line cites the deciding record and authorized archive; no historical mechanism is imported or phone power switch equated with A22. |
| V10 §9 phone names; A22 §§1–5/7 and receipt | C-9.3/.3.1–.3.7 preserve V10's five-name inventory and marked A22 scope difference. All four accepted controls, deliberate starts, private phone retention, exact once/stop menus, full/excerpt marking, existing two-door/privacy/provenance/intake rules, Tunnel Off and Kill Switch effects/prohibitions are placed. C-7P.10 retains all five emergency conditions; removed A22 names acquire no deferred mechanisms. |
| A22 §6; V10 §23; Defaults3L; Map CY-H | C-9.3.9 names all seventeen still-open B30 mechanical areas. Full mobile three-mode architecture remains CH10-d; CY-H remains CH11. No automatic connection or third door is introduced; project-side removal workflow is excluded. |
| V10 §9 rehearsal | C-9.4/.4.1–.4.4 place all fixed-profile, real-person presentation, silent profiling and privacy/evidence/Person-Box/simulation boundaries. Exact A23 rehearsal mechanism remains undecided. |
| Dual-model placement §§1–6; B24 model/open rows | Voice consumes the single light-model voice, validator-first handoff and meaning-preservation boundary. Full model/kernel/benchmark and replacement rules remain CH10-b; connected path remains CH11; speech-synthesizer selection does not choose the language models. |
| B7/A7 private context; B-INT-8 current-authority interfaces; kernel identity/I9/recovery32 | C-7Q/C-24 and current mode references retain separate owners. Kernel coordination never replaces mode epoch/generation/fence or restores personal access. Other complete owner schemas remain earlier cards or CH10-b. |
| Other scoped 04/05 discovery matches | A15/A16/B15/B-INT-4 packages and receipts retain C-BOP/C-TSC ownership. A17 and A19 use current access without new authority; full interface remains CH10-e. All index versions are navigation only, with v0_11 authoritative for full identifiers. Bundle5 accepted ownership is retained; acceptance/closure narrative is excluded. |
| Earlier chapter relationships | All fifty-seven inspected incoming fields across fifty-five distinct places receive reciprocal root rows. All eight earlier uses receive exact current root relationships. Forty-nine canonical specialist cards retain names/status/ownership. Every new external relation has a both-endpoints continuation; no earlier file is edited. |

### Authorized archive inventory additions — CH10-a

| Source | Read scope | Placement |
|---|---|---|
| `98_HISTORICAL_SOURCES_PRE_V10/sources/nh_research_architecture_explained.md` | WHOLE authorized archive; only buckets Group7 restored scope | C-8.19/.19.1/.19.4; no old pipeline implementation, pricing or advice restored |

### Source placements added by CH10-a

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §8; Map C-8/CY-C | C-8 root and C-8.1 retain the exact root name, DESIGNED status and raw→single synthesis→create-space/gate→review→authorized entry route. Memory grows as readings; the mouth never trains. B11/engine/Catalog/privacy/access owners are explicit, with continuations. |
| V10 §8 WHY BRAVE and threat model | C-8.2/.3/.3.1/.3.2 separate raw independent-index JSON, one synthesis, text-only execution and unverified-data instruction containment. Brave and OpenRouter keys remain distinct. Current pricing, test-session history and running-code claims are excluded. |
| V10 §8 rejected-bin rules; Bundle 6 closeout §9(d) | C-8.4/.5/.5.1–.5.6 place retained auto-rejection, every inert-display rule and the explicit distinction between deliberate review and forbidden silent ordinary influence. No copy/select security claim or review-authorized memory/reasoning/retrieval/ranking use. |
| V10 §8 cap, academics and responsibilities | C-8.6 states the mandatory code-level counter/cap without inventing its value or enforcement. C-8.7 and its two children retain both academic sources and exclude Google Scholar. C-8.8 and two children preserve new gathering versus currency assessment and all four outcome words. |
| V10 §8 source preservation and separate capture | C-8.9 and seven artifact/metadata children preserve plain text, frozen PNG, inactive URL, provenance, timestamp, research-reading ID and integrity hash. C-8.10 keeps capture isolation distinct from synthesis isolation. No executable page state, screenshot reasoning or embeddings. Exact capture technology and field encodings remain open. |
| V10 §8 approved rechecks and fallback; Bundle 6 mechanics §5 | C-8.11 records the genuine personal approval gate. C-8.12 and five source-named causes retain every text/metadata item, failure reason and SOURCE PRESERVATION INCOMPLETE. Screenshot absence alone causes no auto-discard, confidence downgrade or automatic corroboration; actual verification failure remains closed. |
| Bundle 6 mechanics §5 isolation | C-8.13 and three context cards cover sole outbound fetch, separate capture, text-only synthesis, create-space/gate, sole review exit and absence of every direct production-write path. Authorized entry consumes normal engine, Catalog and B11. |
| Bundle 6 mechanics §5 identities | C-8.14/.14.1–.14.5 and locator/hash/method/content children place all five identities and their exact composition/exclusions. research_operation_id retains [proposed] at every use. Dated snapshots are not stable duplicate identity. No serialization or hash algorithm is invented. |
| Bundle 6 mechanics §5 duplicate and version rules | C-8.14.6/.14.7/.14.8 cover identical-output reevaluation linked to one candidate, materially changed output as a new linked version with difference/provenance, preserved older versions and exactly one concurrent winner with a recorded duplicate hit. |
| Bundle 6 mechanics §5 checkpoints | C-8.15 and six stage cards place fetched→preserved→synthesized→gated→queued or rejected, separate commits, committed-stage resumption and preserved-but-unsynthesized waiting. No failed-stage content or preservation is fabricated. |
| Bundle 6 mechanics §§3/5; canonical C-STORE.5.2, C-7H.9/.10, C-7G.9, C-STORE.4 | C-8.16 consumes exact B9 attempt/wait/elapsed/substantive-retry/early-stop/real-change rules and committed-state/partial recovery. Root and operation cards consume atomic commits, deterministic replay and structural duplicates from their canonical owner. Full B11 registry/selection, global claim, WB1 binding, WB2 commit fence, WB3 single terminal parent record, historical-coverage-before-writes and recovery remain canonical C-STORE.4; the C-8.1 caller seam includes payload, evidence references, stable ingest identity, outcome/root/batch ownership. |
| Bundle 6 mechanics §5 failure classes | C-8.17 and seven children distinguish failed fetch, failed synthesis, unverifiable context boundary, preservation integrity, text, metadata and provenance failure. Honest retryable/terminal treatment, outside-queue recorded/reported uncertainty and no progress toward memory are explicit. |
| Bundle 6 mechanics §§3/5 operation records | C-8.18 and seven event-kind children cover fetch, preservation success/INCOMPLETE, synthesis call, gate decision, queue entry, retained rejection and currency re-check. One real operation/one log, append-only, no recursion/evidence weight, applicable privacy/access and genuine failures remain explicit. |
| Buckets §4 Group 7; authorized NH_MASTER-5 §8, NH_MASTER_CONTEXT restored headings, research architecture Layer2/What stays the same | C-8.19 and four children place only FR-0081/0122/0142/0155: two-of-three differently angled raw result sets as the scoped rule; exact historical model/service, 150 cycles/night with 3 raw searches/cycle and 3:00 AM only as values-at-the-time. Every DECIDED line cites the deciding record and authorized archive. No old gate implementation, pricing, extra model vote or present-day scheduling permission is restored. |
| Bundle 6 closeout §§8/10; Map CY-C | C-8.20 registers eight unknown full-cycle fields. B13 component completion does not settle B-CYCLE-2 identity, transactions, idempotency, duplicate prevention, crash/retry/partial recovery or fail-closed end-to-end wiring. The connected path remains CH11. |
| Bundle 4 §§4D/6/7.4; canonical C-7D.16 | C-8.21 retains wider research knowledge outside the active core absent an evidence-linked qualifying basis. Membership stays separate from currentness/grounding/relevance/ranking; the full lifecycle and nine qualifying bases remain C-7D.16. Deactivation never rewrites research material. |
| A26 §4.6; canonical C-WIS-SEP | C-8 keeps research availability independent of wellbeing tiers while real privacy/security gates remain. Full wellbeing and its source constraints remain CH10-c. |
| Defaults §§3I/5; Companion embedded §8; cursorrules §5 | Header marks the older academic-open and screenshot-confidence/corroboration/inert-role drift; V10 precedence is preserved. Cursorrules dual-pipeline warning is old implementation inventory, not new research behavior or a current running-state claim. |
| Earlier C-7B/C-7B.6/C-7B.8 and C-7E endpoints | Two incoming named C-8 fields receive two single-place root use rows. Three earlier C-8 uses, including C-7B at CY-C and CY-J, receive explicit root Fed-by conditions. The inherited V10 §2/§7B conflict remains marked for named-gap handling; no earlier file is edited. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A17_WONDER_TO_MEMORY_POLICY_PACKAGE_v1_0_CANDIDATE.md` | Scoped §11 source inventory only; no C-8 behavior from the inventory. Wonder ownership remains its existing/later path scope. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md` | Scoped §9: only runtime direction §§1/49 accepted, supporting research inventory is not Knowledge Catcher behavior. Full interface coverage remains CH10-e. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Scoped §4.6: C-8 availability boundary, full canonical mode/wellbeing scope retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Scoped source-preservation-method context around lines768–778 is evidence packaging, not research source preservation. Full authority-control-plane mechanics remain CH10-b. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped §13 caller contract read whole; C-8.1 carries research caller seam. Full storage mechanics remain canonical C-STORE.4. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Scoped §4D, §6 and §7.4 membership passages read; C-8.21 consumes canonical world-model boundary, not new membership mechanics. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Whole current consolidation read; C-8 protected review and cycle boundaries placed. Other ingest/provenance/creation/learning owners retain their earlier cards. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Whole closure receipt reread for accepted status and scope only; no implementation or independent audit claimed. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole closure receipt reread; confirms accepted mechanics scope, not new behavior. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped §§3/5/14/15 read whole, prior full-file credit inherited; all C-8 component mechanics placed with canonical shared dependencies. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole policy closure receipt reread for policy status and boundaries only. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped §7 B13 planned-governed policy passage; later accepted mechanics supply C-8.13–.18, not a fabricated implementation. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Scoped cross-component dependency context lines101–111; C-8 owns component identities and seam. Full kernel mechanics remain CH10-b. |
| `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_0.md` | Scoped matched nightly-organization context only; superseded checkpoint is not an added behavior source. Latest v1_2 belongs CH10-e. |
| `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_1.md` | Scoped matched nightly-organization context only; superseded checkpoint is not an added behavior source. Latest v1_2 belongs CH10-e. |
| `05_ACTIVE_CANDIDATE/NH_A19_HUMAN_EXPERIENCE_DECISIONS_CHECKPOINT_v1_2.md` | Scoped nightly-organization intention context only; interface ownership remains CH10-e, no research mechanism inferred. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped matched discovery/navigation rows read only; v0_11 is current navigation and prior index versions supply no added behavior. No whole-file credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped matched discovery/navigation rows read only; v0_11 is current navigation and prior index versions supply no added behavior. No whole-file credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped matched discovery/navigation rows read only; v0_11 is current navigation and prior index versions supply no added behavior. No whole-file credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped matched discovery/navigation rows read only; v0_11 is current navigation and prior index versions supply no added behavior. No whole-file credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Scoped §3 and §46 supporting engineering-research inventory; not Knowledge Catcher behavior. Full direction/interface scope remains CH10-e. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Whole file read; C-8 retains component isolation/identity and does not confer ungated conversation control. Full framework-direction/dependency coverage remains CH10-b. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Scoped §5 research-model boundary; research supplies background material, never ungated conversation control. Full handoff scope remains CH10-b. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Scoped §§1–4 Groups1–8 and exact Group7 FR rows273/294/314/327; only four authorized research restorations used here. |
| `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | Scoped §§5.2/5.8 research-output and project examples; artifact/interface and future intent scope remains CH10-e/appendices. No C-8 mechanics derived. |

### Source placements added by CH10-b

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10§16,§7R Decision6; MapC-16,A21,B24; DD§3D/E/F; CR§6A; Companion§16 | C-16 root and .1–.7: frozen borrowed mouth, memory growth, search-before-wording, local-first, low-restriction stack, recorded mouth limitations, test-model status, final adoption gate and exact candidate/verification requirements. On-disk statement is source-time status; no current inventory claim. Engine A/B and C-GOLD behavior remains in its earlier owner. |
| Live dual-model concept WHOLE and accepted placement/dependency v1_1+receipt WHOLE | C-16.8: heavy analyst, single visible light messenger, governing authority, twelve-step conceptual sequence, continuation and no-distortion rules, new-input continuing/supplementing/restarting branch; exact models, run frequency, resource/latency/overlap policy remain open where later accepted mechanics do not close them. Full connected CY-B remains CH11. Concept status supported by accepted placement receipt; no adoption or runtime claim. |
| B24v7+receipt WHOLE | C-16.9–.23: producer envelope, facts/possibilities/unknowns/clarifications/direction, captured contribution and routing records; sanitized messenger payload and evidence view; multilingual lane presentation; post-messenger checks and exact rejection labels; pending output and heavy failure paths; parent/child hierarchy; remaining transaction/idempotency/recovery/delivery/supplement rules; parent/child terminal schemas and logs/cooling; all benchmark rules/families/measurements/severity and remaining opens. Every source-proposed name remains marked on every use. |
| B24§B/1,§2.9/2.10/2.12,§3,T3–T7,§7.5 validation operations | Consume existing C-7G.10–.14 in CH05-a: evidence/input boundary, exact validation/insufficiency/compatibility records, deterministic and semantic checks, provider independence, adjudication, rejection vocabulary, committed validation transactions and their log events. Do not redeclare those canonical schemas or turn references into invented closure. Explicit cross-piece continuations connect the remaining B24 producer/messenger boundary to these owners. |
| B9values§3/4/7/13; B9architecture and receipts scoped; normalization§6/8; A29,A31 scoped | C-16 retry/fallback seam consumes C-7H canonical B9 cards with exact 3 total attempts,10/30s live,1/3min background,7/15min deadlines,one careful retry AFTER durable rejection,real-change continuation,early-stop and truthful unfinished outcome. Only eligible proposal after consumed-and-rejected careful retry reaches governed insufficiency assessment; no technical/authorization/hold/indeterminate/validation-boundary relabeling. Accepted A31 dual lanes preserve possibility basis and externally adjudicated insufficiency. |
| Accepted B16bridgev1_7§4,§8.4,§16–18/20 scoped + receipt scoped; existing C-GOLD bridge cards | C-16 benchmark-consumption boundary references existing bridge canonical E12 and coverage owners. E12 is not a B16 input. Eight families,three scopes,fourteen actual measurements,both sealed sets,all runs,current heads,gold-rule-first scoring remain; M-C4 is reported not budgeted. NHD-B16EEB-D1/2/3/4/5/9/15/16 remain open; no model eligible merely because the architecture exists. No bare D IDs outside source quotations. |
| Candor package WHOLE | C-16.24: CANDIDATE truthful disposition, delivery-only warmth, production-time heavy candor, four honesty layers, four benchmark families, fine-tuning authorization and policy values open. No assertion of cited external research findings needed for runtime behavior. Conflict noted for unconditional absence-of-evidence→not-in-memory wording against accepted evidence-linked possibilities/external insufficiency adjudication; canonical accepted boundary not overwritten. |
| B24categorydecisionv0_1 WHOLE | C-16.25: CANDIDATE three reason-to-existing-category table corrections; LANE_CONTAMINATION category deferred, underlying violation still substantive, any-critical rule unchanged; no change to CH05-a literal category set or B9 decisions. Schema-write question stays open. |
| AICv1_10+closure WHOLE | New C-NEW-AIC — Authority Integrity Control Plane: DUMB authority proof, seven example classes,13ledger requirements,14distinct proposed identities/claim/attachment references; establishment-before-observation/sharedclaim; atomic complete basis sealing and generation;6stages/AIC0–5; current reproof and immutable outcomes;B9class/retry seam;17idempotency points,24recoveryrows,23failclosedrows,19logfamilies and18open groups. Content writes only own ledger; no new policy or permission. Receipt controls stale header only. |
| Kernelv1_9+closure WHOLE | New C-NEW-UDOK — Unified Durable Operation Kernel:26envelopeelements,30typedidentitykinds,13semanticfacts,UDOK0–8/6C/R boundaries,CP1–9,lookupfirst recovery and full matrix,13ownerinterfaces,7waits,owner-only claims/effects,one parent terminal+ack,per-generation membership head/closure race,contradiction positions A/B/C and owner resolution,11duplicate points,42+1a failclosed rows,11partialcompletion,13dualsupport rows,logs and explicit opens. AIC Layer1 at every applicable generation before work; Layer2 just-in-time owner authorization. B24 delivery_outcome_unknown terminal distinct from B-INT-6 delivery_unknown nonterminal. |
| FiveFrameworkAdditions WHOLE | Existing accepted AIC/kernel mechanics above; remaining directions as CANDIDATE new C-NEW-FABRIC — Provenance-First Multi-Index Memory Fabric (8channels,11retrievalplan requirements,source-owned rebuild/degradation), C-NEW-LAB — Bounded Self-Healing Execution Laboratory (bounded loop,17contract requirements,9trajectory types,8completion conditions,must-nevers), C-NEW-TOOLS — Governed Capability Registry and Sandboxed Tool Forge (20contract requirements,noncallable candidate and10example lifecycle stages). Inactive fabric mechanical file never imported. Final schemas/owners/values remain open. Project writing/design roles §§34/35 excluded; actual runtime acceptance/permission remains. |
| Contract§5.3 and frozenCH00§0.4 | First-use delivery includes Chapter0§0.4 naming-table continuation naming the five source-existing new top-level parts with primary citations. These documentary C-NEW IDs assign no controlled component/Register IDs and alter no frozen CH00 bytes. Track continuation for later assembly. |
| 75 matching 04/05 paths in CH10-b-discovery.json | Primary whole reads above. Other accepted package hits read as scoped dependency/status/boundary contexts, preserving their existing owners; UE5 kernel-name alignment belongs CH10-e. Decision-index matches reviewed as navigation/status evidence, not behavior; older index versions do not control acceptance. Source-map inventory names every discovery file without falsely claiming whole-file reads. Additional partial index output truncation is recorded as partial navigation-only review, not a whole-read credit. |
| Earlier card endpoints | Ten incoming fields across nine places recorded in CH10-b-incoming.json; no existing C-16 USED BY rows. Existing owner names/statuses from cards-index.json; deduplicate incoming root use per place, preserve separate fields in continuation. Every new outgoing cross-piece edge gets both endpoints in one row. Source-owned privacy/access/provenance/relevance rules stay with earlier cards. |
| AIC §10 and §14 matrix coverage | Seventeen duplicate-prevention points and twenty-three fail-closed conditions are placed across C-NEW-AIC.2 identities/claims, .3 transaction boundaries, .4 current re-proof, .5 outcome/retry classes and .6 recovery cases. No separate permissive route or duplicate owner schema is inferred. |
| UDOK §C.4, §F.2, §Q | Thirteen lifecycle-fact cards plus twenty-four transition cards; full recovery cases including R-19A–D in C-NEW-UDOK.9 and later owner-resolution positions; all forty-three FC conditions including FC-1a in C-NEW-UDOK.18.1–.43. |
| B24 §7.3/§7.5/§7.6 | C-16.21 contains parent/child terminals, forty-four exact event labels, link/state/cooling record fields and active/cold/reactivation conditions. Source-proposed tokens remain qualified; old canonical endpoint names are preserved. |
| B24 §9 and candor §6 | C-16.26 and .26.1–.11 retain named policy/implementation gaps; C-16.24.6 retains all candor mechanical opens. No B9 value is reopened and no operation timeout is invented. |
| Kernel §J.3 versus B9 values §7/§14 | R0/R1 source-boundary wording conflict marked in header; owner admission is carried by reference without renaming either source boundary. |
| Earlier canonical name C-7G.10.4 | Exact frozen name claim_scope retained in the two relationship endpoints. Its missing proposed qualifier is a candidate for the fix-round audit, not a silent rename. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_GOLD_CASES_MISSING_SOURCE_BLOCKER_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_DESIGN_CLOSURE_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A1_ENGINE_C_REPLACEMENT_STORY_BEARING_GOLD_SET_UNPINNED_CONTENT_v1_3_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_v1_2_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_2_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0 .md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A31_GROUNDED_ENOUGH_THRESHOLD_POLICY_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_ACCEPTANCE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A4_RELEVANCE_MODE_DECLARATION_POLICY_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A7_PRIVACY_INFLUENCE_AND_THIRD_PARTY_USE_POLICY_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_STATE_ARCHITECTURE_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B9_RETRY_VALUES_WIRING_INTO_B9_B10_BHOLD_B24_v1_4_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BHOLD_HOLD_UNTIL_ENOUGH_LIFECYCLE_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE1_B9_B10_BHOLD_COORDINATION_NOTE_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_CANDIDATE_v1_4.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_FORMAL_RELEVANCE_DECLARATIONS_AND_COMPLETION_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_2_RELEVANCE_AND_RETRIEVAL_FOUNDATION_COMPLETION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_3_STORY_LAYER_PERSON_BOXES_THEMES_AND_CLASHES_COMPLETION_v1_2_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_ACCEPTANCE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_STORY_LAYER_FIRMNESS_SCALE_POLICY_v1_0_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_A2_CURRENT_STATUS_v1_1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_v1_7_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_A19_UNREAL_ENGINE_5_LOCAL_WORLD_WONDER_RUNTIME_v1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Primary source placed above where applicable; otherwise scoped dependency/status or navigation context only, retaining the already written component owner and later CH10-e/CH11 integration ownership. No whole-read credit from discovery. |

### Authorized archive inventory additions — CH10-c

| Source | Read scope | Placement |
|---|---|---|
| `98_HISTORICAL_SOURCES_PRE_V10/sources/NH_MASTER_FILE_COMPLETE__1_.md` | Authorized Other modules / FR-0082 scope only; verified pin | C-22.13 and its three children; other module descriptions excluded from runtime restoration |

### Source placements added by CH10-c

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §22 WHAT THIS IS / CORE PHILOSOPHY / WHY NESS CAN'T BE THE VALIDATOR | C-22 root and .1: one data-integrity/wellbeing mechanism, personal demonstrated baseline, no external clinical standard, self-consistency across time and no current-opinion veto. |
| V10 §22 passive building / data sources | C-22.2, four source cards and three session-metadata elements: every promotion/rejection, conversation pattern, question type and cross-session decision; demonstrated rather than declared values; exact Layer-2 files preserved. |
| V10 §22 Periodic surface | C-22.3 and correction condition: monthly short summary, only edge refinements consistent with wider pattern; accumulation over time is the design rationale, not a claimed measured accuracy rate. |
| V10 §22 triggers | C-22.4 physical binary visible threshold direction and open values; C-22.5 five specific mental/behavioral patterns, single-session noise versus sustained cross-context signal, unchosen thresholds. |
| V10 §22 four tiers / unlock | C-22.6 four tier cards and open transition logic; C-22.7 appointment document, timestamp and unlocking; no invented threshold, verification algorithm, tier transition record schema or unlock transaction. |
| V10 §22 limitation / architecture / build gate; DD §3K; CR §12D | C-22.8 limitation, C-22.9 build prerequisites and protected-file boundary. Preserve advisory/no-diagnosis/no-prescription/no-autonomous-action and no silent writes; exclude coding-workflow confirmation rituals. Mark the advisory-versus-promotion-control wording tension without resolving it. |
| V10 §25.5; accepted A26 §4.6; B-INT-5 §4 separation; B-INT-4 C2 | Root explicit canonical C-WIS-SEP and C-SACL.7 references; tier and calibration effects never become identity/access authority. Earlier imitation-risk source conflict remains carried. |
| Map C-22 §0B; V10 §26.6/§26.7/§26.11; Bundle6 mechanics §12 | C-22.10 four log events and access protections; C-22.11 current-tier query for response calculation; incoming OOP observations stay tagged consideration, never direct response configuration. C-22.12 Layer-2 scope retained. |
| Buckets §3/§4 Group2/Group11 and FR-0082; authorized archive Other modules | C-22.13 clinical PDF and chart forms at DECIDED-2026-09-25 only. Exact historical module identifiers are provenance, not restored implementation. Content schema, generation, access/export workflow and scheduling remain open. No other archive behavior imported. |
| Other Future Feature Intent Excerpts §10 | Explicitly not promoted suggestions; no new wellbeing mechanisms. Preserve for CH12 inventory only. A22 removed breathing/night-lockout modes belong CH10-d, with no wellbeing replacement. |
| Fifteen accepted/active discovery matches | Component boundary matches retained in existing owners; index matches navigation only; kernel FC-22 matches are lexical false positives; recovery ledger feeds Appendix B only. No whole-read credit from discovery. |
| Earlier endpoint inventory | Seven incoming fields and eleven earlier use places recorded; provide exact-name reciprocal rows/continuations while leaving all finished files unchanged. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | §3 removal boundary inspected; breathing/night-lockout removal belongs CH10-d and creates no replacement wellbeing feature. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_4_TSC_AUTHORIZATION_PROMOTION_AND_INTERRUPTED_CONTINUATION_WIRING_v1_3_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A26_IDENTITY_AND_PERSONAL_MODE_RELATIONSHIP_POLICY_v1_1_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Relevant separation/dependency context read; current component owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Discovery FC-22 and correction-table matches classified as lexical false positives for C-22; no wellbeing mechanism drawn. Whole-file credit inherited from CH10-b. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Scoped NHD-M22 navigation row inspected only; no behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Scoped NHD-M22 navigation row inspected only; no behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/Other_Future_Feature_Intent_Excerpts.md` | §10 read whole: all eight proposed ideas are explicitly not promoted; no mechanics written and no whole-file credit. |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | FR-0082 discovery/index context only; ledger feeds Appendix B and supplies no runtime behavior. Earlier whole-read credit unchanged. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Scoped NHD-M22 navigation row inspected only; no behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | §3 and §4 Groups2/11 plus coverage row FR-0082 read; restoration narrowed to clinical PDF/chart output only. Prior whole credit inherited. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Scoped NHD-M22 navigation row inspected only; no behavior or whole-file credit from index. |

### Source placements added by CH10-d

| Source scope / inventory | Placement or explicit remaining owner |
|---|---|
| V10 §23, DD §3L, Companion embedded §23, Map C-23 | C-23 root; two-door boundary; Mode 1 live tunnel and deliberate opening/closure; one independent local AI with online/offline states; no-memory offline branch; Manual Sync; all five non-negotiable security requirements and exact open choices. |
| V10 §25.3 Raw Voice Data Protection | C-23.7 protected acoustic/voice/anti-spoofing material transmission seam; only Full Mode and biometric verification, with at least recognized_ness; keep this artifact-specific restriction separate from generic phone content. |
| Accepted A22 v1_1 and its receipt, both WHOLE | Consume existing C-9.3 through four mobile interface cards, retaining private capture, no third door, ordinary disconnect versus emergency hard stop, complete must-not boundaries and separate restart. C-9 owns all menus, provenance and five emergency-stop conditions already written. Source policy remains ACCEPTED despite frozen candidate header; formal receipt closure wording not silently promoted. |
| B11 §13 caller matrix, accepted A22 §2/§3 | Mobile sync-item caller supplies seven-field payload, eligibility/authorization/blocker-clearance references, stable identity basis and provenance; receives outcome/root/batch identities. Existing Catalog and B11 own actual intake and write mechanics. Full cross-layer CY-H remains CH11, not inferred. |
| Map A20/B30/C11/A24/B-INT-10 and A22 §6/§7 | Named mobile open-policy and mechanical slots; verified raw run-path removal prerequisite; Layer-2 gate remains protected; no handoff or source-operation timeout invented. |
| Map C-23 §0B | Tunnel opening/closure, Manual Sync event and gate outcome, local learning-update records and no silent local→real crossing; exact schemas still open. |
| Source conflicts | Map biometric-only Manual-Sync wording versus V10/DD PIN alternative; Map A20-settled status versus still-open specific choices; inherited five phone-name inventory versus accepted A22 removals/addition. Preserve all, no reconciliation. |
| Earlier endpoints | Ten incoming fields across ten places; no existing C-23 USED BY rows. New relationships receive exact-name reciprocal rows and cross-piece continuations. |
| Twenty discovery matches | Accepted interface/room policies leave mobile integration open for CH10-e; AIC/kernel/framework packages leave mobile policy unchanged; decision indexes navigate; ledger only Appendix B; prior restored personality/power-switch names remain canonical C-9.3.8. No new runtime from historical or future idea notes. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | §13 caller/callee matrix and §7.1 boundary read in scope; canonical B11 retains schema/write ownership. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Exclusion of mobile/voice construction inspected; no mobile implementation inferred. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |
| `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Mobile relation/open-question paragraphs inspected; unaccepted VR ideas supply no mobile mechanics. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Discovery-only matching titles/classifications; ledger feeds Appendix B, not behavior; no whole-file reread credit. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Recovery boundary/group scopes inspected; restored phone names retain canonical C-9.3.8 placement. No new archive restoration. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. |

## READ RECORD

Contract §§5–11 and lessons §§1–11 reopened for this piece; contract §11.3 reopened after writing. Bounded source reads do not receive whole-file credit. The following scopes describe actual reading; downloaded files are not treated as read. Earlier whole-read credits are inherited without claiming to have repeated them.

| Source file | Reading scope / whole-file credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | §23 read whole; §25.3 Raw Voice Data Protection read in scope; §7E and §12 interface boundaries checked. No whole-file reread credit. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | §3L read whole; fingerprint/Face ID/PIN and independent companion boundaries checked. No whole-file reread credit. | `6cd09329e12ba9de78b96d02347a765b65191ec6f7050f62f71d4a831baee696` |
| `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Embedded §23 read whole; no whole-file reread credit. | `cdcc6134e273014472ad288dc349ce0c7c525638a73929f7dede52d30d040aeb` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | C-23, A20/B30/C11 and A24/B-INT-10 scopes read; no whole-file reread credit. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. | `187ef4ce4c24b09ad81d246053b88cf39c60f84550ce2ee2fdccba73a4a2b231` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. | `8f22b0a1dd7b4393934af873993ef797437e8d312164b1676caecab2e240f18c` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | §13 caller/callee matrix and §7.1 boundary read in scope; canonical B11 retains schema/write ownership. | `baca06e562027a080dab4384943bfb87947c6f598b36776f1016fa8472384a87` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. | `de70bc8132c93a1530bafc7f5dec9884def9c8870200313abcfbc194c841d92e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_AUTHORITY_INTEGRITY_CONTROL_PLANE_MECHANICAL_DESIGN_v1_10_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. | `b39654a60744982d0e2f16c2bc3cd7a33f6ae47ff55b63b5b1dfffada719d709` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. | `7bb426d211685ba9f96b2194163bcbb6750365ed689ef19b0614f5b217288451` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_ACCEPTANCE_RECORD_v1_0.md` | Exclusion of mobile/voice construction inspected; no mobile implementation inferred. | `ef561aa5037068e1a225157e0382f7155cb91c1948df4347e5236f3a535fbd01` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. | `91c52869fb1616f25a5193a5eeca7e70ba0bf0fa755c8ce5648719efae8f9b11` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md` | Relevant mobile/open-interface paragraphs inspected; full human-experience component belongs CH10-e. No new whole-file credit. | `fa42d8ff4295c08df0634978107e555d6244f7e4c033d5f8bc4a7588deac3af0` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | WHOLE file reread; accepted four-control policy and exact receipt identity checked; earlier whole-file credit retained. | `1c788736a58c3b8836765b64690d25d90ef4f0be8fe2e36fa144c4a3863f9e50` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. | `5998098c86875721feb99bab7e3bb14435770e0d74be6541eab828aa9efee26e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_UNIFIED_DURABLE_OPERATION_KERNEL_MECHANICAL_DESIGN_v1_9_CANDIDATE.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. | `1f9ea714f1a182c0857e80399850a3aeebcf4a50a32d5a200fce57a5d5f47ae3` |
| `05_ACTIVE_CANDIDATE/NH_PERSONAL_IDEA_NOTE_A19_VR_WORLD_ROOMS_OFFLINE_CREATION_v1.md` | Mobile relation/open-question paragraphs inspected; unaccepted VR ideas supply no mobile mechanics. | `0839e5dcfcff1fd41b65fd44403a2ad18408869fea38111300852a2074ce20f3` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. | `aad8d1aeee9a331ad6f4d9ddbcfa9c42eae2a94e1ef1bccde7484079181ff7b4` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_5_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. | `457c6f43562a92cd82076640af44a58ea412335284c0e61da3c38f3ba63f24b9` |
| `05_ACTIVE_CANDIDATE/NH_PRE_V10_HISTORY_VS_V10_FEATURE_RECOVERY_LEDGER_v0_1_CANDIDATE.md` | Discovery-only matching titles/classifications; ledger feeds Appendix B, not behavior; no whole-file reread credit. | `fc014bbab36c87495d534ade8bb78f8de4197efa9408f5abb908743601a21522` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. | `aafc7abe6522f4c7ece23f40560e648866188e1b5401ed6cd298809d15ed0f7b` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md` | Recovery boundary/group scopes inspected; restored phone names retain canonical C-9.3.8 placement. No new archive restoration. | `9f6f9cac1e07ab14f0c6f3ed834b8260265dac6f6a430fa12be5c6e4c3f0b59f` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_6_CANDIDATE.md` | Navigation matches inspected only; no runtime behavior or whole-file credit from index. | `3f1b95da77f620597e9ba862568f4247d1eb4d50f73c620888637dfcde03e3c9` |
| `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_FIVE_FRAMEWORK_CAPABILITY_ADDITIONS_v1.md` | Mobile dependency/open-scope context read; existing owner retained; no whole-file reread credit. | `1386091a0977ac79588f22a9f85213579203637e493dbb2d75be3d893326aa28` |

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
| CH09-f | `0b06b8fc0a819d6844c8e1a638afa615e24bc59663daab8cb3d19434f8fd69b7` |
| CH09-g | `93002da16c0c48625e63d808f07e2c7a8414e349c56e98476a6ff867f3c9d8d1` |
| CH09-h | `f207851ff1069c61d4649a62b66ba2207510c7765abff4db0061c2a98e0865c7` |
| CH09-i | `fc06db5d0aacc159c58f8005cf0056382e5b28a831c3efe105b4796b2b6daec7` |
| CH10-a | `6ea2d8c834c801353e78adcd6d72450b47fca76932597b81d129bf80b15d9e2d` |
| CH10-b | `1fa96f9009889eaf9c9628dea0f7aeebce38ad838d912d5dcd45bb7c7c3210d6` |
| CH10-c | `334fd69ad34ff9e1a9cb26df6e9f055951b0b38b8bd2cbc9e9676eada1843ed8` |

### Instruction and carry-forward identities

| Artifact | SHA-256 |
|---|---|
| Build contract v1_0 | `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1` |
| Lessons v0_4 | `e60b950df06fd4ac62961b194e416d2fba682ab02436c2ade131a8cd6f3f7bf8` |
| Run instructions v0_5 | `f0d9c411ee1bceda4c3527e58b1b1c60631304200a802fdb246edba31ded77d3` |
| Route v0_4 | `a83d9c1451d25bed3da95e7dcb83aa399abbed600d79d9da0c0e910275ffa97d` |
| Writing 2 manifest | `5f435a441ed31a3f14c05c2ae1c58d904e8ea7a5a680fcc433308b1196511160` |

### READ-folder files not yet read whole

38 inherited pending files remain after the explicitly credited whole reads. Scoped discovery does not close these obligations.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_B10_MANUAL_REREAD_COMPATIBILITY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_REREAD_MODE_ASSIGNMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_0_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A25_TO_B10_REREAD_MODE_CONNECTION_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B10_REREAD_OPERATION_IDENTITY_AND_RECOVERY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_1_MEMORY_READING_FOUNDATION_NORMALIZATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_4_LIVING_STATE_COMPUTED_VIEW_ACTION_AND_WORLD_MODEL_COMPLETION_v1_3_CANDIDATE.md`
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
§1.3 no history/actions/roles/workflow in this chapter: PASS — behavior region scanned: 0 workflow hits; project records remain outside behavior.  
§1.4 every gap written as NOT DECIDED: PASS — 72 empty fields; 72 matching Appendix A rows; zero mixed gaps.  
§1.5 conflicts marked, none resolved: PASS — 3 header conflict paragraphs; inherited conflicts remain in the manifest.  
§3 exactly one stamp per line: PASS — 315 template field lines; 63 using-place rows; populated lines use permitted stamps and empty fields use the required gap form.  
§4 every behavior line cited in the exact format: PASS — 20 distinct citation locations; 20 resolve at the pin. Statement support reviewed against the scoped sources; heading resolution alone is not a semantic-support claim.  
§5.4 one name per thing: PASS — 35 unique cards; zero duplicate IDs, wrong endpoint names or wrong target stamps.  
§6 all template fields present, in order, for every part: PASS — 35 cards and 315 field lines; no missing or reordered field sequence.  
§6.3 reciprocity within this chapter: PASS — 52 internal TOGETHER relationships have reciprocal places; 63 single-place USED BY rows; 27 cross-piece continuation rows name both endpoints.  
§6.4 every decided detail written in, no citation used in place of content: PASS — direct source-to-card review recorded in 29 coverage rows; 20 selected exact source labels checked, 0 missing. This label count is a check inventory, not a claim to count every source fact.  
§6.5 sub-parts recursed to the bottom: PASS — every SUB-PARTS list checked for owned children and exclusion of self; record, state, transition, failure, event and gate content mapped above.  
§9 coverage matrix rows added for every file used: PASS — 150 cumulative source paths, 0 absent at the pin; 24 current read fingerprints; 38 inherited files still without whole-read credit.  
§10.11 no recommendation, no sentence addressed to Ness: PASS — behavior reviewed as system description; quoted source utterances, where present, remain system output examples.  

Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_v1_1_CANDIDATE.md`; `04_ACCEPTED_STANDALONE_DESIGNS/NH_A22_PHONE_SIDE_MODES_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`

Writer self-check: 315 field lines and 189 USED BY behavior cells reviewed; restriction/failure/gate slots: 105. Prerequisite wording is assessed against each card's own fields; each reciprocal use retains the directly authored using-card text, whose requirements were reviewed at that owner. All 10 positive flags have named card/line/reason dispositions above. No flag is hidden in an ordinary total. Formula hits: 0; wording hits: 0; blank stamped content: 0; errors: 0. Earlier identities checked and unchanged: 58. BUILT lines: 0; these retain only the V10-built embedding/index endpoint, not a new implementation claim. The DECIDED-citation check applies wherever a DECIDED stamp occurs.

Computed validator output:

```json
{
  "cards": 35,
  "field_lines": 315,
  "used_by_rows": 63,
  "empty_fields": 72,
  "internal_edges": 52,
  "outgoing_edges": 17,
  "external_uses": 11,
  "citations": 20,
  "resolved_citation_headings": 20,
  "built_lines": 0,
  "formula_hits": 0,
  "workflow_hits": 0,
  "wording_hits": 0,
  "errors": 0,
  "review_flags": 10,
  "registered_empty_fields": 72,
  "continuation_rows": 27,
  "source_literals_checked": 20,
  "source_literals_missing": 0,
  "preserved_earlier_hashes": 58,
  "read_fingerprints_checked": 24,
  "coverage_file_paths": 150,
  "coverage_paths_missing_at_pin": 0,
  "pending_whole_files": 38,
  "source_map_rows": 29,
  "named_review_dispositions": 10,
  "misfiled_box_fields_scanned": 315,
  "restriction_failure_gate_slots_reviewed": 105,
  "restriction_failure_gate_lines_reviewed": 105
}
```
