# Chapter 4-e — Group B: C-9A

**Document:** `NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH04-e.md`  
**Status:** CANDIDATE  
**Source repository:** `nesgeva/NH-GOVERNANCE`  
**Source commit:** `6a7160ba688ba4e433a31899162815df7e2bab17`

This piece covers C-9A — Image ingest front door (§9A), with all its sub-parts. It leaves every path except P-MAIN to CH11, and the appendices to CH12.

Citation keys: V10 = `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`; DD = `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`; CR = `01_AUTHORITATIVE/cursorrules`; COMP = `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`; MAP = `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`; `04/` = `04_ACCEPTED_STANDALONE_DESIGNS/`; `05/` = `05_ACTIVE_CANDIDATE/`; `98/` = `98_HISTORICAL_SOURCES_PRE_V10/`. Every citation resolves at the pinned commit.

<!-- BEGIN BEHAVIOR -->

### C-9A — Image ingest front door (§9A)
Stamp: DESIGNED    Source: [V10 §9A] [MAP C-9A] [V10 §1A]

ALONE
- What it is: DESIGNED — The first worked non-text front door into the one input-agnostic Meaning Engine. [V10 §9A] [MAP C-9A] [V10 §1A]
- Takes in: DESIGNED — An image capture and its actual source metadata. [V10 §9A] [MAP C-9A] [V10 §1A]
- Does: DESIGNED — Runs metadata → plain description → context-meaning proposal → Ness confirmation, then the Catalog route to an eligible root. Uses the same engine as text, video and audio; a new input type adds a front door. [V10 §9A] [MAP C-9A] [V10 §1A]
- Gives out: DESIGNED — Captured image material, explicit proposals and a confirmation outcome entering the ordinary Catalog boundary. [V10 §9A] [MAP C-9A] [V10 §1A]
- Must never: DESIGNED — Treat a machine description as fact without confirmation, or create a separate meaning engine merely for images. [V10 §9A] [MAP C-9A] [V10 §1A]
- Fails closed by: DESIGNED — Uses Catalog's capture-error and holding lifecycle; an unconfirmed context-meaning remains a proposal. [V10 §9A] [MAP C-9A] [V10 §1A]

TOGETHER
- Fed by: DESIGNED — C-9A.1 — Image metadata: supplies source and deterministic metadata at the first stage. [MAP C-9A]
- Fed by: DESIGNED — C-9A.2 — Proposed plain description: supplies the plain-description proposal. [MAP C-9A]
- Fed by: DESIGNED — C-9A.3 — Context-meaning proposal: supplies contextual meaning as a proposal. [MAP C-9A]
- Fed by: DESIGNED — C-9A.6 — Image operation records: provides the required image-operation records. [MAP C-9A]
- Fed by: ACCEPTED — C-9A.7 — B22 — Deferred WhatsApp ingest: supplies applicable media only through the future authorized frozen-archive route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [MAP C-9A]
- Gated by: DESIGNED — C-9A.4 — Image confirmation boundary: Ness must confirm before contextual meaning receives more than proposal status. [MAP C-9A]
- Gated by: DESIGNED — C-9A.5 — Image Catalog handoff: the common capture envelope and Catalog eligibility must hold. [MAP C-9A] [MAP C-7E]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A.1 — Image metadata | Image capture and actual metadata. | Preserves facts and deterministic derivations. | Later proposals remain distinct from source metadata. | [MAP C-9A] |
| 2 · DESIGNED | C-9A.4 — Image confirmation boundary | The image proposal and actual response. | Records confirmation or rejection and preserves that boundary. | Unconfirmed interpretation remains provisional. | [MAP C-9A] |
| 3 · ACCEPTED | C-9A.7.1.3 — WhatsApp image stage | The independently captured media image. | Uses the same image front door. | WhatsApp media gets no special semantic bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [MAP C-9A] |
| 4 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E) | An image capture and its common intake envelope. | Receives and resolves the image capture under the Catalog lifecycle. | Image material reaches root eligibility only through the shared front door boundary. | [MAP C-7E] [MAP C-9A] |
| 5 · DESIGNED | C-7E — Catalog Front Door + pre-ingest holding (§7E); P-MAIN step 1 | An image at the front door. | Runs the image proposal/confirmation sequence and common Catalog intake. | Eligible image material enters the main root path; the frozen WhatsApp branch remains disabled. | [V10 §1A] [MAP C-9A] |

SUB-PARTS: C-9A.1 — Image metadata; C-9A.2 — Proposed plain description; C-9A.3 — Context-meaning proposal; C-9A.4 — Image confirmation boundary; C-9A.5 — Image Catalog handoff; C-9A.6 — Image operation records; C-9A.7 — B22 — Deferred WhatsApp ingest

### C-9A.1 — Image metadata
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The first stage of image intake. [MAP C-9A]
- Takes in: DESIGNED — The image and metadata actually supplied by its source. [MAP C-9A]
- Does: DESIGNED — Preserves source metadata and distinguishes any deterministic metadata derivation from a machine-proposed description. [MAP C-9A]
- Gives out: DESIGNED — Source-carried or deterministically derived metadata with its capture provenance. [MAP C-9A]
- Must never: DESIGNED — Present a proposed description as a source-carried metadata fact. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A — Image ingest front door (§9A): supplies the capture and the rule placing metadata first. [MAP C-9A]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | The image metadata. | Begins the image sequence with its source facts. | Description has a provenance-bearing input. | [MAP C-9A] |
| 2 · DESIGNED | C-9A.2 — Proposed plain description | Captured image metadata. | Forms the plain-description proposal after metadata. | The sequence retains its first handoff. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.2 — Proposed plain description
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The plain-description stage following metadata. [MAP C-9A]
- Takes in: DESIGNED — Captured image material and its metadata. [MAP C-9A]
- Does: DESIGNED — Produces a proposed plain description and records that proposal. [MAP C-9A]
- Does: DECIDED-2026-09-25 — Uses detection or segmentation rather than a narrating vision-language model: flat labels, boxes and confidence within a vocabulary ceiling: the detector knows only its trained labels and will miss or force-fit unfamiliar objects, with scene understanding beyond OCR. The named candidates are YOLO, Segment-Anything, osam, PaddleOCR-VL, SmolVLM and the Ollama route; no tool is selected or installed. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 3] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §5] [98/sources/NH_MASTER-8.md §9A]
- Gives out: DESIGNED — A machine description awaiting confirmation rather than an established fact. [MAP C-9A]
- Must never: DESIGNED — Treat the machine description as fact without Ness's confirmation. [MAP C-9A]
- Fails closed by: DESIGNED — Leaves the unconfirmed description as a proposal. [MAP C-9A]

TOGETHER
- Fed by: DESIGNED — C-9A.1 — Image metadata: supplies the preceding metadata stage. [MAP C-9A]
- Gated by: DESIGNED — C-9A.4 — Image confirmation boundary: factual treatment requires Ness's confirmation. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | A proposed plain description. | Carries it toward contextual interpretation and confirmation. | The description retains proposal status. | [MAP C-9A] |
| 2 · DESIGNED | C-9A.3 — Context-meaning proposal | A plain-description proposal. | Forms the contextual proposal in sequence. | Interpretation remains a separate proposal stage. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.3 — Context-meaning proposal
Stamp: DESIGNED    Source: [V10 §9A] [MAP C-9A]

ALONE
- What it is: DESIGNED — The contextual interpretation stage of the image sequence. [V10 §9A] [MAP C-9A]
- Takes in: DESIGNED — The image, metadata and plain-description proposal. [V10 §9A] [MAP C-9A]
- Takes in: DECIDED-2026-09-25 — The plain description, read against Ness's life; the context never reads the photo directly. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 3] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §5] [98/sources/NH_MASTER-8.md §9A]
- Does: DESIGNED — Carries a context-meaning proposal forward to Ness's confirmation boundary. [V10 §9A] [MAP C-9A]
- Gives out: DESIGNED — Proposed meaning whose status remains unsettled until confirmation. [V10 §9A] [MAP C-9A]
- Must never: DESIGNED — Treat context-meaning as anything more than a proposal before Ness confirms. [V10 §9A] [MAP C-9A]
- Fails closed by: DESIGNED — Retains proposal status when confirmation is absent. [V10 §9A] [MAP C-9A]

TOGETHER
- Fed by: DESIGNED — C-9A.2 — Proposed plain description: supplies the proposed plain description. [MAP C-9A]
- Gated by: DESIGNED — C-9A.4 — Image confirmation boundary: confirmation is required before treating context-meaning as more than a proposal. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | The image's context-meaning proposal. | Routes it to the confirmation boundary. | Meaning is not silently settled. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.4 — Image confirmation boundary
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — Ness's confirmation or rejection of the image proposal. [MAP C-9A]
- Takes in: DESIGNED — The proposed description and context-meaning, and Ness's response. [MAP C-9A]
- Does: DESIGNED — Records the confirmation or rejection; permits context-meaning to be treated as more than a proposal only after confirmation. [MAP C-9A]
- Gives out: DESIGNED — A recorded response with the corresponding proposal boundary preserved. [MAP C-9A]
- Must never: DESIGNED — Infer confirmation from the existence of a machine description or bypass Ness's confirmation. [MAP C-9A]
- Fails closed by: DESIGNED — Without confirmation, withholds factual treatment of the machine description and keeps context-meaning provisional. [MAP C-9A]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-9A — Image ingest front door (§9A): Ness's confirmation is required to treat the interpretation as more than a proposal. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | Ness's actual confirmation or rejection. | Applies the image confirmation boundary. | Unconfirmed descriptions remain proposals. | [MAP C-9A] |
| 2 · DESIGNED | C-9A.2 — Proposed plain description | The recorded response to the description. | Retains proposal status until confirmation. | Machine description cannot silently become fact. | [MAP C-9A] |
| 3 · DESIGNED | C-9A.3 — Context-meaning proposal | Ness's response. | Preserves the proposal boundary. | No unconfirmed contextual fact is asserted. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.5 — Image Catalog handoff
Stamp: DESIGNED    Source: [MAP C-9A] [MAP C-7E]

ALONE
- What it is: DESIGNED — The common capture and root-eligibility boundary for images. [MAP C-9A] [MAP C-7E]
- Takes in: DESIGNED — Stable unique `capture_id`, exact raw payload or stable immutable reference, capture timestamp, front-door/source type, payload format/media type, source-provided metadata without reinterpretation, and traceable capture provenance. [MAP C-9A] [MAP C-7E]
- Does: DESIGNED — Hands the image to Catalog's separate raw-capture and root-ingestion gates. Preserves source-carried speaker and real source thread identity; uses non-semantic capture-session or singleton placeholders for established untitled grouping, and holds uncertain grouping. Uses the existing held → ready → promoting → promoted lifecycle, with rejected, excluded and error outcomes; promotion is atomic and idempotent, and the pre-ingest record remains as provenance. [MAP C-9A] [MAP C-7E]
- Gives out: DESIGNED — An eligible root through Catalog, or an honest held/excluded/error disposition with preserved material. [MAP C-9A] [MAP C-7E]
- Must never: DESIGNED — Guess envelope values or speakers, use a topic as `source_title`, drop a malformed capture silently, expose held raw content to downstream semantic analysis, or bypass exclusion handling. [MAP C-9A] [MAP C-7E]
- Fails closed by: DESIGNED — Sends malformed input to capture-error; unresolved required fields hold ingestion. Excluded raw material goes to protected storage with only safe remainder and non-reconstructive metadata in ordinary records. [MAP C-9A] [MAP C-7E]

TOGETHER
- Fed by: DESIGNED — C-7E.2 — Minimum intake envelope: supplies the complete seven-element minimum envelope contract. [MAP C-7E]
- Gated by: DESIGNED — C-7E — Catalog Front Door + pre-ingest holding (§7E): capture completeness, source attribution, exclusion and root eligibility are Catalog's existing conditions. [MAP C-7E] [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | The image intake envelope and resolution state. | Uses the shared capture and promotion boundary. | Eligible input proceeds; malformed or unresolved input is handled honestly. | [MAP C-9A] [MAP C-7E] |

SUB-PARTS: NONE

### C-9A.6 — Image operation records
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The four image-front-door event classes required by the operation log. [MAP C-9A]
- Takes in: DESIGNED — Image captures, deterministic metadata derivations, proposed descriptions, and Ness's confirmation or rejection. [MAP C-9A]
- Does: DESIGNED — Records each event in its own applicable operation context; applies privacy access and applicable identity/security authorization to those records. [MAP C-9A]
- Gives out: DESIGNED — Traceable image handling and proposal-response records. [MAP C-9A]
- Must never: DESIGNED — Expose the records through an unauthorized access path. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A.6.1 — Image capture record: supplies capture events. [MAP C-9A]
- Fed by: DESIGNED — C-9A.6.2 — Metadata derivation record: supplies deterministic derivation events. [MAP C-9A]
- Fed by: DESIGNED — C-9A.6.3 — Plain-description proposal record: supplies description-proposal events. [MAP C-9A]
- Fed by: DESIGNED — C-9A.6.4 — Image response record: supplies actual confirmation/rejection events. [MAP C-9A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): image records remain subject to privacy access authorization. [MAP C-9A]
- Gated by: DESIGNED — C-SACL — Speaker Access-Control Layer (§25.4): applicable identity/security authorization must permit access to the records. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | Capture, derivation, proposal and response events. | Retains the trace of image handling. | Image operations remain accountable. | [MAP C-9A] |
| 2 · DESIGNED | C-9A.6.1 — Image capture record | An actual capture event. | Records it in the image operation context. | The required event is retained. | [MAP C-9A] |
| 3 · DESIGNED | C-9A.6.2 — Metadata derivation record | A deterministic metadata operation. | Records its occurrence. | The derivation is traceable. | [MAP C-9A] |
| 4 · DESIGNED | C-9A.6.3 — Plain-description proposal record | A proposed plain description. | Records it as a proposal. | Proposal status is preserved in the trace. | [MAP C-9A] |
| 5 · DESIGNED | C-9A.6.4 — Image response record | An actual confirmation or rejection. | Records the response. | No fictitious confirmation is introduced. | [MAP C-9A] |

SUB-PARTS: C-9A.6.1 — Image capture record; C-9A.6.2 — Metadata derivation record; C-9A.6.3 — Plain-description proposal record; C-9A.6.4 — Image response record

### C-9A.6.1 — Image capture record
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The record of an image capture. [MAP C-9A]
- Takes in: DESIGNED — Each actual image capture. [MAP C-9A]
- Does: DESIGNED — Records the capture. [MAP C-9A]
- Gives out: DESIGNED — Capture-operation evidence subject to record-access rules. [MAP C-9A]
- Must never: DESIGNED — Omit a real image capture from the required operation record. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A.6 — Image operation records: supplies the capture-event recording rule. [MAP C-9A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): capture-record access requires the applicable privacy authorization. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A.6 — Image operation records | Each image capture. | Includes the capture record. | Capture is traceable. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.6.2 — Metadata derivation record
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The record of deterministic metadata derivation. [MAP C-9A]
- Takes in: DESIGNED — Each deterministic derivation performed on the captured image metadata. [MAP C-9A]
- Does: DESIGNED — Records that derivation as deterministic metadata work. [MAP C-9A]
- Gives out: DESIGNED — A trace of the derived metadata's production. [MAP C-9A]
- Must never: DESIGNED — Mislabel a proposed description as a deterministic derivation. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A.6 — Image operation records: supplies the derivation-event recording rule. [MAP C-9A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): derivation-record access requires the applicable privacy authorization. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A.6 — Image operation records | Each metadata derivation. | Includes its derivation record. | Source and derived metadata remain distinguishable. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.6.3 — Plain-description proposal record
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The record of a proposed plain description. [MAP C-9A]
- Takes in: DESIGNED — Each machine-proposed image description. [MAP C-9A]
- Does: DESIGNED — Records the description as a proposal. [MAP C-9A]
- Gives out: DESIGNED — Traceable proposal production. [MAP C-9A]
- Must never: DESIGNED — Record an unconfirmed description as established fact. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A.6 — Image operation records: supplies the proposal-event recording rule. [MAP C-9A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): proposal-record access requires the applicable privacy authorization. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A.6 — Image operation records | Each proposed description. | Records proposal production. | No proposal is relabeled as fact. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.6.4 — Image response record
Stamp: DESIGNED    Source: [MAP C-9A]

ALONE
- What it is: DESIGNED — The record of Ness's image confirmation or rejection. [MAP C-9A]
- Takes in: DESIGNED — Ness's actual response to the proposal. [MAP C-9A]
- Does: DESIGNED — Records whether Ness confirmed or rejected it. [MAP C-9A]
- Gives out: DESIGNED — The response record associated with the image proposal. [MAP C-9A]
- Must never: DESIGNED — Manufacture a confirmation or omit a rejection. [MAP C-9A]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: DESIGNED — C-9A.6 — Image operation records: supplies the response-event recording rule. [MAP C-9A]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): response-record access requires the applicable privacy authorization. [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A.6 — Image operation records | Ness's response. | Records its actual disposition. | The image proposal has a response trace. | [MAP C-9A] |

SUB-PARTS: NONE

### C-9A.7 — B22 — Deferred WhatsApp ingest
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]

ALONE
- What it is: ACCEPTED — The accepted design of the deferred WhatsApp pipeline, with the archive still frozen. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]
- Takes in: ACCEPTED — A future authorized archive-ingest request, the engine, and the approved protected ingest path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]
- Does: ACCEPTED — Defines five separate operation classes and their protected, recoverable handoffs. Keeps the path disabled until its required protected mechanics are accepted and integrated and Ness authorizes its use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]
- Gives out: ACCEPTED — A design-bound future route through decryption, SQLite extraction, image handling where applicable, privacy handling, and engine-plus-Catalog ingestion. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]
- Must never: ACCEPTED — Decrypt or ingest merely because this design exists, bypass the engine or Catalog, or turn accepted design status into runtime authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]
- Fails closed by: ACCEPTED — Refuses an unauthorized frozen-path invocation and records its frozen status honestly. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §12]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.1 — Five-stage WhatsApp pipeline: supplies the five separate operation classes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.4 — Independent durable work items: supplies independent durable work identities and checkpoints. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5 — WhatsApp work recovery: supplies the bounded recovery outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies one-operation/one-log records including frozen refusal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: protected handling must exist before any key or plaintext stage runs. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.3 — Media and attachment ordering: both exact durable endpoints are required before an attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.7 — Consumed Bundle 6 operation contract: shared atomicity, identity, privacy, retry and B11 conditions bind every operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · DESIGNED | C-9A — Image ingest front door (§9A) | An independently identified media capture. | Applies the unchanged image sequence within that route. | Archive design does not itself enable image ingestion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [MAP C-9A] |
| 2 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | The archive path's established authorization. | Admits stage execution only when permitted. | A design alone cannot start decryption. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.2.7 — Protected-mechanics prerequisite | Required mechanics and integration state. | Maintains the prerequisite independently from authorization. | Design acceptance cannot be mistaken for execution readiness. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.1 — Five-stage WhatsApp pipeline; C-9A.7.2 — Protected key and plaintext lifecycle; C-9A.7.3 — Media and attachment ordering; C-9A.7.4 — Independent durable work items; C-9A.7.5 — WhatsApp work recovery; C-9A.7.6 — WhatsApp operation records; C-9A.7.7 — Consumed Bundle 6 operation contract

### C-9A.7.1 — Five-stage WhatsApp pipeline
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The ordered decomposition of the deferred pipeline. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — An authorized future archive job under the protected-stage boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Runs decrypt → SQLite front door → image front door where applicable → ordinary privacy/third-party handling → ingest only through the engine and Catalog. Gives each stage its own operation class; exact access and purpose checks precede every stage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Independently identified stage operations and governed downstream handoffs. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat stage completion as authorization for the next stage or postpone privacy checks until after exposure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — A stage without its required authorization or protected boundary does not begin. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.1.1 — Decrypt stage: supplies integrity-verified protected decrypt output. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.1.2 — SQLite extraction stage: supplies separate source-faithful captures. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.1.3 — WhatsApp image stage: supplies the unchanged image proposal path where applicable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.1.5 — Engine and Catalog ingest stage: supplies the sole engine-and-Catalog root route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7 — B22 — Deferred WhatsApp ingest: the frozen path requires its future prerequisites and Ness's authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.1.4 — WhatsApp privacy stage: ordinary privacy, evidence and simulation rules remain applicable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | The ordered stage design. | Routes future authorized work across the five stages. | No stage becomes an ingest bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.1.2 — SQLite extraction stage | Source database and media. | Extracts each source item independently. | The five-stage route retains its SQLite boundary. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.1.1 — Decrypt stage; C-9A.7.1.2 — SQLite extraction stage; C-9A.7.1.3 — WhatsApp image stage; C-9A.7.1.4 — WhatsApp privacy stage; C-9A.7.1.5 — Engine and Catalog ingest stage

### C-9A.7.1.1 — Decrypt stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The archive decryption operation class. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The encrypted archive and authorized key extraction inside the protected boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Uses the named `wa-crypt-tools` tool family for the deferred design, with one operation identity per decrypt run; verifies output integrity. No command or key-handling implementation is specified. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A readable message database and media set held entirely outside ordinary memory in protected staging. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Expose the key or plaintext to ordinary memory, or accept output whose integrity is doubtful. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Halts on any integrity doubt. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: keys and plaintext require the protected lifecycle before decryption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | Readable database and media held outside ordinary memory. | Advances to source extraction within the protected route. | The archive output remains protected. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.1.2 — SQLite extraction stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]

ALONE
- What it is: ACCEPTED — Per-message extraction into the common intake envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Takes in: ACCEPTED — Source messages, sender metadata, media items and exact source timestamp fields. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Does: DECIDED-2026-09-25 — Sets `subject` to the honest provenance placeholder `seed:whatsapp_a13` and maps the chat or contact name to `source_title`, never to `subject`. [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §4 / Group 11] [05/NH_DECISION_RECORD_PRE_V10_RECOVERY_BUCKETS_2026-09-25_v0_2_CANDIDATE.md §5] [98/sources/NH_MASTER-9_2.md §12D]
- Does: ACCEPTED — Keeps each message and each media item as its own unchanged Origin; connects related Origins without merging them. Derives message `capture_id` deterministically from the stable WhatsApp message identity. Carries the sender from source without guessing. Populates typed `source_times` with `source_time_kind` (`sent` for message send time, `recorded` or `created` for media where supplied), exact-field `provenance_ref`, `timezone_state` and `reliability_status`. Only `known_reliable` source times may be the main date; unknown source time has zero main date. Keeps original, imported and record-created times distinct; import or record time never substitutes for the original. Writes an attachment relationship separately only after both endpoints durably exist. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Gives out: ACCEPTED — Separate capture work items with faithful source identity and time provenance. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Must never: ACCEPTED — Merge a message and photograph into one Origin, guess the sender or a timestamp, substitute an import date, or commit a dangling attachment link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Fails closed by: ACCEPTED — An unsatisfied intake envelope produces a capture-error; an unreliable original time remains explicitly unknown with no main date. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.1 — Five-stage WhatsApp pipeline: supplies the ordered extraction rule after protected decryption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-STORE.5.5.4 — source_times: supplies the typed source-time representation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Fed by: ACCEPTED — C-STORE.5.5.5 — imported_at: supplies the distinct import-time field. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Fed by: ACCEPTED — C-STORE.5.5.6 — record_created_at: supplies the distinct record-creation time. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3]
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: all seven intake elements must be present without guessing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | Message and media Origins with their source metadata. | Routes applicable media to the image stage. | Source granularity and time provenance survive extraction. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.1.3 — WhatsApp image stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Application of the ordinary image front door to applicable media. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — An extracted image item with its own capture identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Uses metadata → plain description → context-meaning proposal without changing the ordinary image confirmation rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — An image proposal routed through the common confirmation and Catalog boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat a machine description as fact without Ness's confirmation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — An unconfirmed machine interpretation stays a proposal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-9A — Image ingest front door (§9A): the normal image sequence and Ness-confirmation boundary apply unchanged. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [MAP C-9A]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | An image stage result. | Carries the result with its confirmation boundary. | Machine description is not silently promoted. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.1.4 — WhatsApp privacy stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]

ALONE
- What it is: ACCEPTED — The accepted A30 ordinary privacy and third-party handling target, with the governing age-default disagreement explicitly retained. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Takes in: ACCEPTED — Third-party material, including material about a child, minor, disabled, distressed, dependent or otherwise vulnerable person. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Does: ACCEPTED — Preserves source and speaker separation, evidence and uncertainty labeling, privacy and compartments, authenticated private use versus restricted external use, prohibition of unsupported claims and illegal or harmful use, explicit approval for full simulation, and person/group rules that become stricter only when Ness chooses. A30 adds no automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. [SOURCE CONFLICT: V10 §7Q prescribes stronger default restrictions for minors and highly vulnerable people] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Gives out: ACCEPTED — Material subject to all ordinary protections, with no claim that the opposing age-default rules have been integrated or reconciled. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Must never: ACCEPTED — Weaken an ordinary privacy, evidence, external-use, harm, legality or simulation rule, or treat A30 as permission to ingest the archive. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]
- Fails closed by: ACCEPTED — The frozen archive remains unavailable for ingest until the engine and approved path exist; a missing applicable authorization blocks the stage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): privacy, compartment and external-use authorization must hold; the V10 age-default conflict remains explicit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §7Q / THIRD-PARTY DATA RULES]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | Third-party handling requirements. | Preserves the applicable privacy boundary and explicit source disagreement. | No age-policy reconciliation is silently invented. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] |

SUB-PARTS: NONE

### C-9A.7.1.5 — Engine and Catalog ingest stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The sole root-producing stage of the deferred pipeline. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Eligible captured material after the applicable image and privacy boundaries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Routes through the one engine and Catalog into the B11 active writable batch, with exclusion precedence at capture and the consumed B11 write contract. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — Governed active-batch roots and corresponding promotion outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Write directly to a store, use a side channel, or reopen, unseal or append to the sealed 5,521-root batch. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Refuses promotion when Catalog eligibility, privacy, coverage or B11 write conditions do not hold. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-7E.12 — Accepted root-write handoff: the accepted root-write handoff and active-batch write conditions must hold. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.1 — Five-stage WhatsApp pipeline | Eligible material at the final stage. | Completes only through the active writable batch. | The pipeline has no direct store branch. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2 — Protected key and plaintext lifecycle
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Protection requirements binding on every WhatsApp stage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Keys, decrypted plaintext, staging artifacts and any durable decrypted derivatives. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Keeps credentials inside Level-1 execution, plaintext inside operation-scoped protected staging, artifacts accounted for, and access authorized before each stage. Seals interrupted staging and resumes only through the same protected path. Required B7 mechanics must be accepted and integrated before this path is runnable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Protected handling with no ordinary key or staging-content exposure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Postpone privacy until after exposure, leave untracked staging copies, or silently retain durable plaintext derivatives. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Keeps the path disabled when its required protected mechanics are unavailable or unintegrated; interruption seals staging against access. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.2.1 — Key confinement: supplies the key-confinement rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.2.2 — Protected plaintext staging: supplies the operation-scoped plaintext boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.2.3 — Staging artifact accounting: supplies full staging-artifact accounting. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.2.5 — Interrupted staging recovery: supplies sealed interrupted-state recovery. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.2.6 — Durable decrypted derivatives: supplies the durable-derivative preservation rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.2.4 — Authorization before each stage: exact authorization and purpose must be checked before every stage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.2.7 — Protected-mechanics prerequisite: required B7 mechanics must be accepted and integrated. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | Protected-boundary readiness and authorization. | Keeps the deferred path disabled when prerequisites are absent. | Sensitive material is not exposed by a premature invocation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.1.1 — Decrypt stage | Stage authorization and protected staging. | Decrypts only within the allowed boundary and verifies integrity. | Ordinary memory receives no raw decrypt output. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.2.2 — Protected plaintext staging | Decrypted plaintext. | Keeps it outside ordinary retrieval and model context. | Only the protected path can access it. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-9A.7.2.3 — Staging artifact accounting | Stage files, previews, copies, exports, caches and backups. | Registers each to the operation. | Artifact persistence is accountable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-9A.7.2.5 — Interrupted staging recovery | Interrupted staging state. | Seals, records and resumes only within that boundary. | Restart preserves containment. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-9A.7.2.6 — Durable decrypted derivatives | A derivative that must persist. | Records and protects it. | No decrypted derivative is silently retained. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.2.1 — Key confinement; C-9A.7.2.2 — Protected plaintext staging; C-9A.7.2.3 — Staging artifact accounting; C-9A.7.2.4 — Authorization before each stage; C-9A.7.2.5 — Interrupted staging recovery; C-9A.7.2.6 — Durable decrypted derivatives; C-9A.7.2.7 — Protected-mechanics prerequisite

### C-9A.7.2.1 — Key confinement
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Level-1 containment of decryption keys and credentials. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Raw cryptographic keys or credentials required by the authorized function. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Uses raw keys only within the protected execution boundary and references them outside by opaque identity only. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — The permitted operation result without ordinary raw-key exposure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Place raw keys in ordinary logs, prompts, memory, screenshots, error text or model context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Withholds the stage when the required protected execution boundary is unavailable. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-9A.7.2.7 — Protected-mechanics prerequisite: the required protected execution mechanics must be available and integrated. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | Keys needed by the authorized function. | Keeps them in Level-1 execution. | Raw keys stay outside ordinary channels. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.2 — Protected plaintext staging
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The operation-scoped holding area for decrypted plaintext. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Readable database and media outputs of the authorized decrypt operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Holds plaintext in protected staging unavailable to ordinary retrieval, reasoning or model context. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Operation-scoped protected plaintext available only through its authorized path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Let ordinary retrieval, reasoning or model context read staging plaintext. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Prevents ordinary access to the staging content. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: supplies the operation-scoped protected-staging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.2.4 — Authorization before each stage: only the exact authorized protected-stage purpose may access plaintext. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | Decrypted database and media. | Holds them in protected staging. | Ordinary reasoning cannot read staging content. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.3 — Staging artifact accounting
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Registration and close-time accounting of every staging artifact. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Temporary files, previews, copies, exports, caches and backups created in the staging operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Registers every such artifact to the operation and accounts for it at close. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A complete operation-bound artifact accounting. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Create an untracked temporary file, preview, copy, export, cache or backup. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: supplies the requirement to register every artifact and account at close. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | All stage-created artifacts. | Accounts for each at close. | No untracked copy is silently left behind. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.4 — Authorization before each stage
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The exact-purpose access boundary preceding stage execution. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The next stage, requested access and exact authorized purpose. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Runs the authorization and purpose checks before the stage begins; evaluates privacy at or before the protected staging boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A stage allowed only within its established protected purpose. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Check privacy only after sensitive plaintext has entered an unprotected place. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Does not begin an unauthorized stage. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): the exact requested access and purpose must be authorized before stage execution. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | The next operation and its purpose. | Applies the pre-stage boundary. | Privacy is not deferred beyond exposure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.2.2 — Protected plaintext staging | Established purpose authorization. | Keeps staging inside the allowed boundary. | Ordinary access stays unavailable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.2.5 — Interrupted staging recovery | Recovery purpose and access authorization. | Resumes only through protected staging. | The interrupted area stays sealed otherwise. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.5 — Interrupted staging recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The protected recovery action after a staging crash. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The interrupted staging state and durable operation record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Seals staging against access, records its interrupted state and resumes only through the same protected path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A sealed, recorded interruption or an authorized protected resumption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Expose plaintext or guess missing state during recovery. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Leaves staging closed against access until the protected recovery path can proceed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: supplies the interruption rule and protected recovery boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.2.4 — Authorization before each stage: resumption must use the same authorized protected path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | An interrupted staging operation. | Closes access and records the state. | Restart cannot expose or reconstruct plaintext. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.6 — Durable decrypted derivatives
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Preservation and visibility handling for a decrypted derivative that must persist. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — A required durable derivative of decrypted material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the derivative and protects it at the correct level under ordinary preservation and visibility laws. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — An honestly recorded, appropriately protected derivative. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Retain a decrypted derivative silently or exempt it from protection because it came from staging. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-9A.7.2 — Protected key and plaintext lifecycle: supplies preservation and visibility requirements for persistent derivatives. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | Plaintext derivatives that must persist. | Records and protects each at the correct level. | Persistence is explicit and governed. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.2.7 — Protected-mechanics prerequisite
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The prerequisite for enabling the deferred WhatsApp path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Accepted protected-execution and sealed-storage mechanics and their version-safe integration state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Requires both acceptance and integration of the necessary B7 mechanics before the path can be runnable; independent ingest authorization remains required. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A disabled path until all those prerequisites are established. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat the existence of an accepted B7 document alone as integration, implementation or permission to decrypt. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Keeps the path disabled and non-runnable while its required integration is absent. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7 — B22 — Deferred WhatsApp ingest: supplies the disabled-until-ready condition for the deferred path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): required B7 protected mechanics must be accepted and integrated before runtime use. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.2 — Protected key and plaintext lifecycle | Their established integration state. | Keeps the path disabled until ready. | Acceptance alone does not enable runtime handling. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.2.1 — Key confinement | Protected-boundary readiness. | Allows only contained key use. | No ordinary substitute path is accepted. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.3 — Media and attachment ordering
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The ordering rule that prevents broken message-to-media links. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Separately durable message and media Origins and their directly recorded attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Commits a separate append-only `origin_relationship_record` [proposed] only after both exact endpoint identities durably exist, under its own operation identity and structural duplicate key. A message whose media extraction fails stands alone with an honest failure record; later recovery may append the relationship after both endpoints verify. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A valid standalone message or a verified append-only attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Create a broken, dangling or misleading relationship, or rewrite an Origin or pre-ingest record to repair the link. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Refuses the relationship when either durable endpoint is missing or cannot be verified. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-STORE.5.5.7 — origin_relationship_record [proposed]: both exact endpoint identities must durably exist before the separate relationship commit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | Message and media completion evidence. | Preserves link safety across the pipeline. | No dangling relationship is admitted. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.5.3 — Missing-relationship resumption | Verified endpoint identities. | Appends the relationship idempotently. | Missing or uncertain endpoints block the link. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.6.4 — Relationship-creation record | The verified creation result. | Records that operation's truthful outcome. | No dangling link is reported as created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.4 — Independent durable work items
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Separate recovery units for messages, media and attachment relationships. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Each message, each media item and each attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Gives every item its own stable identity and durable checkpoint. Retains completed items while unfinished items remain discoverable independently. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Three independently tracked work-item classes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Infer media completion from message completion or mark a whole unit complete merely because a crash occurred. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Leaves incomplete items incomplete and available to the recovery scan. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.4.1 — Message work identity: supplies the deterministic message identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.4.2 — Media work identity: supplies the deterministic media identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.4.3 — Relationship work identity: supplies the proposed relationship operation identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | Message, media and relationship work items. | Tracks their completion independently. | A parent capture cannot conceal missing media work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.4.1 — Message work identity | The stable source message identity. | Derives and reuses its deterministic capture identity. | Reruns identify the same message work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.4.2 — Media work identity | The stable source media identity. | Derives and reuses its own capture identity. | Parent message completion cannot erase media work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-9A.7.4.3 — Relationship work identity | Its own stable operation identity. | Keeps relationship recovery separate from capture completion. | The link receives its own terminal result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-9A.7.5.1 — Incomplete-item scan and exact lookup | The independent message, media or relationship identity. | Finds the actual unfinished operation. | A different item's state cannot stand in for this one. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.4.1 — Message work identity; C-9A.7.4.2 — Media work identity; C-9A.7.4.3 — Relationship work identity

### C-9A.7.4.1 — Message work identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable identity of a message extraction work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The stable WhatsApp message identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Derives a deterministic message `capture_id` and reuses it for retries and recovery lookup. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — One durable message work-item identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Mint a fresh message capture identity on rerun to evade duplicate detection. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Structural duplicate prevention recognizes the existing capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.4 — Independent durable work items: supplies the independent message identity and checkpoint rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4 — Independent durable work items | Stable message capture identity. | Tracks message work independently. | Message retries keep the same identity. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.4.2 — Media work identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable identity of a media extraction work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The stable WhatsApp media identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Derives a deterministic media `capture_id`, independently of the parent message's completion, and reuses it on retries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — One durable media work-item identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Duplicate media on rerun or let a committed parent message suppress the unfinished media item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Structural duplicate prevention recognizes the existing media capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.4 — Independent durable work items: supplies the independent media identity and checkpoint rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4 — Independent durable work items | Stable media capture identity. | Tracks media work independently. | Parent completion cannot hide missing media. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.4.3 — Relationship work identity
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The stable proposed `relationship_operation_id` for an attachment relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The relationship work item and its exact endpoint, kind and provenance identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Retains its own stable operation identity across retries and recovery, alongside a structural duplicate key independent of the message and media capture identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A separately recoverable relationship operation with its own terminal operational record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat the message's terminal record as completion of the relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Reuses the exact existing identity rather than duplicating the operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.4.3.1 — Relationship structural duplicate key: supplies exact endpoint-plus-kind-plus-provenance duplicate identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.4 — Independent durable work items: supplies the independent relationship work-item rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.4.3.2 — Directional relationship ordering: directional kinds must retain source-to-target direction. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.4.3.3 — Symmetric relationship ordering: symmetric kinds must use canonical endpoint ordering. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4 — Independent durable work items | Stable relationship identity and checkpoint. | Tracks relationship completion independently. | Link recovery has its own terminal result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.4.3.1 — Relationship structural duplicate key | Exact endpoints, kind and source provenance. | Forms the required duplicate identity. | Retry cannot duplicate the relationship. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.4.3.1 — Relationship structural duplicate key; C-9A.7.4.3.2 — Directional relationship ordering; C-9A.7.4.3.3 — Symmetric relationship ordering

### C-9A.7.4.3.1 — Relationship structural duplicate key
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The duplicate identity of a directly recorded relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The two exact endpoint identities, relationship kind and source-provenance identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Forms the structural key from all four elements and applies the relationship kind's endpoint-ordering rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A structural relationship identity that survives retry and restart. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Omit source provenance or an endpoint from duplicate identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Prevents a second relationship with the same structural identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.4.3 — Relationship work identity: supplies the structural identity rule for relationship work. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4.3 — Relationship work identity | The relationship's structural key. | Recognizes replay independently of message completion. | Duplicate relationships are prevented. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.6.6 — Relationship duplicate-prevention record | Matching endpoint, kind and provenance identity. | Skips and records the recognized duplicate. | A novel relationship is not mislabeled as a replay. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.4.3.2 — Directional relationship ordering
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Endpoint ordering for a directional relationship kind. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The relationship's source and target endpoint identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Preserves endpoint direction in the duplicate key. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A key retaining the actual directed relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Canonicalize away direction for a directional kind. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4.3 — Relationship work identity | The directional kind and ordered endpoints. | Uses a direction-preserving key. | Direction is not erased. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.4.3.3 — Symmetric relationship ordering
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Endpoint ordering for a symmetric relationship kind. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The two endpoint identities of a symmetric kind. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Uses canonical endpoint ordering so reversing the endpoints cannot create a second relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A single structural identity for either endpoint order. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Accept a reversed-endpoint duplicate of a symmetric relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Recognizes the canonical key and prevents the duplicate. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.4.3 — Relationship work identity | The symmetric kind and endpoint pair. | Uses one canonical key. | Reversing endpoints cannot duplicate the link. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5 — WhatsApp work recovery
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Recovery of the independent durable WhatsApp work items. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Committed checkpoints and all incomplete message, media and relationship work. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Looks up each exact identity before work, scans every incomplete item, and resumes its missing operation under bounded retry. Keeps completed results, records failures honestly and never reconstructs or rewrites source records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — Resumed missing work, idempotently completed relationships or explicit terminal failures. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Scan only messages lacking pre-ingest records or silently lose an attachment because its parent committed first. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Halts terminal work items and retains honest failure records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.5.1 — Incomplete-item scan and exact lookup: supplies complete discovery and exact-identity lookup. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5.2 — Missing-media resumption: supplies the missing-media recovery action. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5.3 — Missing-relationship resumption: supplies missing-relationship recovery. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5.4 — Terminal media failure: supplies the honest terminal-media outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5.6 — Terminal work-item halt: supplies terminal work-item failure handling. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.5.7 — WhatsApp capture-error outcome: supplies malformed-message capture-error handling. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.5.5 — WhatsApp bounded technical retry: technical attempts and elapsed time must both remain within the accepted bounds. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | Incomplete work and terminal results. | Resumes only the actual unfinished operations. | Recovery preserves completed work and honest failures. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.5.1 — Incomplete-item scan and exact lookup | Durable item identities and checkpoints. | Looks up the exact operation before work. | Recovery is tied to committed state. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: C-9A.7.5.1 — Incomplete-item scan and exact lookup; C-9A.7.5.2 — Missing-media resumption; C-9A.7.5.3 — Missing-relationship resumption; C-9A.7.5.4 — Terminal media failure; C-9A.7.5.5 — WhatsApp bounded technical retry; C-9A.7.5.6 — Terminal work-item halt; C-9A.7.5.7 — WhatsApp capture-error outcome

### C-9A.7.5.1 — Incomplete-item scan and exact lookup
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Discovery of all unfinished durable work after interruption. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — All incomplete work items and their applicable stable identities. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Scans messages, media and relationships independently and looks up the exact work-item identity before doing any work. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — The actual unfinished operation associated with its existing checkpoint. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Limit discovery to messages without committed pre-ingest records or start work before identity lookup. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Does not infer completion from a different item's committed state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.5 — WhatsApp work recovery: supplies the rule to scan all incomplete work before resuming. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.4 — Independent durable work items: work may resume only after looking up that item's exact stable identity and checkpoint. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | All incomplete work items. | Finds the actual unfinished work. | No child is lost behind a completed parent. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.2 — Missing-media resumption
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Recovery when a message Origin exists but its media Origin is missing. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The committed message and the exact unfinished media extraction identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Resumes that exact media extraction operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Continued media work without rewriting or duplicating the message. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Mark the media complete solely because the message committed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Keeps the message valid while the media remains incomplete or terminally failed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | Committed message and missing media. | Resumes the exact media operation. | Message completion is preserved. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.3 — Missing-relationship resumption
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Recovery when both Origins committed but their relationship did not. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Both exact durable endpoint identities and the unfinished relationship work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Verifies both endpoints and appends the relationship idempotently using its own stable identity and duplicate key. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — One verified attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Rewrite an Origin or pre-ingest record, or append before endpoint verification. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Refuses an unverifiable relationship and records the outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-9A.7.3 — Media and attachment ordering: both exact Origins must verify durably before the missing relationship is appended. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | Two committed Origins and an absent link. | Verifies endpoints and appends idempotently. | The attachment can complete without rewriting Origins. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.4 — Terminal media failure
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The outcome of media extraction that has terminally failed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The valid message Origin and the failed media work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Leaves the message valid and standalone, records the media-extraction failure honestly and creates no relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A preserved message plus a truthful media-failure record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Invent an attachment, create a dangling link or silently hide the media failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Halts the failed media work item with no relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | Failed media and valid message. | Leaves the message standalone. | No false attachment is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.5 — WhatsApp bounded technical retry
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The consumed background/nightly B9 retry limits for this deferred path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — A retryable technical failure and the same durable work-item identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Permits 3 total attempts, with minimum gaps of 1 minute then 3 minutes, within a 15-minute elapsed maximum. Applies both attempt and elapsed gates; stops at whichever closes first, and may stop earlier if retry is useless or unsafe. Further continuation requires a recorded real change. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — A bounded retry under the same message, media or relationship identity, or an honest stopped result. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Reset identity or retry counters through repetition, continue past either bound, or treat repetition alone as a real change. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Stops when either bound closes or the failure is terminal; records the outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-STORE.5.2.11 — Bounded retry: retryability, attempt and elapsed limits, safety and real-change rules must hold. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | Retry classification, attempt count and elapsed time. | Permits only bounded same-identity retry. | Exhaustion or unsafe retry stops work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.6 — Terminal work-item halt
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Terminal failure handling for an individual pipeline work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — A message, media or relationship failure classified as terminal. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Halts that work item and records the failure honestly, preserving already completed independent work. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A terminal result that does not imply unrelated items failed or completed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Claim successful completion or silently discard the terminal failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Stops the affected work item with its failure record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | An actual terminal failure. | Halts only the affected work item honestly. | Completed independent work stands. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.5.7 — WhatsApp capture-error outcome
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — Failure of an extracted message to satisfy the intake envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — An extracted message with missing or invalid required capture information. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Routes it to the explicit capture-error outcome under Catalog's preservation boundary. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — An honest capture error rather than a fabricated eligible root. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Silently drop the message or force a guess to satisfy the envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Withholds root ingestion and records the capture error. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: DESIGNED — C-7E.2 — Minimum intake envelope: an extracted message must satisfy the complete intake envelope. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.5 — WhatsApp work recovery | An unsatisfied envelope. | Preserves an honest failure instead of a forced root. | Invalid input cannot slip into memory. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6 — WhatsApp operation records
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — Operation logging for the deferred WhatsApp path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Decrypt runs, message and media captures, relationship outcomes, privacy-decision references, promotions and refused frozen invocations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Gives each real operation exactly one operational record; relationship operations receive their own terminal record. Keeps records append-only, access-controlled and free of recursive logging or extra evidential weight. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — The required per-operation records with preserved privacy boundaries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Expose raw keys or protected plaintext through logging, recursively log the logging act, or let a log prove its own subject. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — An unauthorized frozen invocation is refused and recorded; terminal failures retain honest outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6.1 — Decrypt-run record: supplies the decrypt-run outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.2 — Message-capture record: supplies message-capture outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.3 — Media-capture record: supplies media-capture outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.4 — Relationship-creation record: supplies relationship-creation outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.5 — Relationship-refusal record: supplies relationship-refusal outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.6 — Relationship duplicate-prevention record: supplies relationship duplicate-prevention outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.7 — Relationship-failure record: supplies relationship-failure outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.8 — Privacy-decision reference record: supplies privacy-decision references. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.9 — WhatsApp promotion record: supplies actual promotion outcomes. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fed by: ACCEPTED — C-9A.7.6.10 — Frozen-invocation refusal record: supplies the refused frozen-path invocation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.7 — Consumed Bundle 6 operation contract: one-operation/one-log, access control and protected-content restrictions apply to every record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | Actual pipeline operations. | Retains their required outcomes. | Invocation and completion remain auditable. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 2 · ACCEPTED | C-9A.7.6.1 — Decrypt-run record | One real decrypt operation. | Writes its operational result without key material. | The run retains one record. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 3 · ACCEPTED | C-9A.7.6.2 — Message-capture record | The message operation. | Records only its actual completion. | Media completion remains independent. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 4 · ACCEPTED | C-9A.7.6.3 — Media-capture record | The media operation. | Records its own capture result. | Parent message logs cannot substitute for it. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 5 · ACCEPTED | C-9A.7.6.4 — Relationship-creation record | The relationship creation operation. | Records its result once. | No second terminal truth is introduced. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 6 · ACCEPTED | C-9A.7.6.5 — Relationship-refusal record | An actual refusal. | Retains the refusal outcome. | Refused work is not presented as creation. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 7 · ACCEPTED | C-9A.7.6.6 — Relationship duplicate-prevention record | A structurally identified duplicate. | Records duplicate prevention. | No duplicate link or evidence increment results. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 8 · ACCEPTED | C-9A.7.6.7 — Relationship-failure record | The actual failed relationship operation. | Records its own failure. | The failure remains distinguishable from message success. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 9 · ACCEPTED | C-9A.7.6.8 — Privacy-decision reference record | The applicable privacy decision. | Records its safe reference. | Authorization remains traceable without sensitive payload. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| 10 · ACCEPTED | C-9A.7.6.9 — WhatsApp promotion record | The actual Catalog promotion. | Records its proper operation outcome. | There is no second parent terminal log. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: C-9A.7.6.1 — Decrypt-run record; C-9A.7.6.2 — Message-capture record; C-9A.7.6.3 — Media-capture record; C-9A.7.6.4 — Relationship-creation record; C-9A.7.6.5 — Relationship-refusal record; C-9A.7.6.6 — Relationship duplicate-prevention record; C-9A.7.6.7 — Relationship-failure record; C-9A.7.6.8 — Privacy-decision reference record; C-9A.7.6.9 — WhatsApp promotion record; C-9A.7.6.10 — Frozen-invocation refusal record

### C-9A.7.6.1 — Decrypt-run record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The one operational record for a decrypt run. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The decrypt operation identity and its actual outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records that run once under its own identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A traceable decrypt result without raw keys or unprotected plaintext. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Put key material in the log or emit duplicate terminal records for the same run. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — The operation's state and record commit together; under uncertainty no entry, activation or completion is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the decrypt-run logging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): decrypt-record access is subject to privacy authorization and key confinement. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | Each decrypt run. | Includes its one record. | Decryption is traceable without keys in the log. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.2 — Message-capture record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The record of an extracted message capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The extracted message operation and deterministic message `capture_id`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the capture independently of its media and attachment operations. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A truthful message-capture result. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Treat this record as proof that media or relationships completed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — The operation's state and record commit together; under uncertainty no entry, activation or completion is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the independent message-capture logging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): message-capture records require the applicable access authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | Each extracted message capture. | Records its own result. | Parent completion stays separate from media completion. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.3 — Media-capture record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The record of a media capture. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The media operation and deterministic media `capture_id`. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the media capture under its own operation identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A separate media-capture result. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Hide a missing media operation behind the parent message record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — The operation's state and record commit together; under uncertainty no entry, activation or completion is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the independent media logging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): media-capture records require the applicable access authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | Each media capture. | Records it independently. | Missing media cannot disappear behind a message log. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.4 — Relationship-creation record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The operational outcome of creating an attachment relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The relationship's own operation identity and verified durable endpoints. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the relationship creation as that operation's outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — Its own one-operation/one-log terminal record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Add a second terminal truth for the same relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Without verified endpoints and an actual commit, no creation is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the relationship's one-terminal-record rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: ACCEPTED — C-9A.7.3 — Media and attachment ordering: a creation outcome requires verified durable endpoints and the actual relationship commit. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | A verified relationship creation. | Retains its own terminal record. | The link's operation has one truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.5 — Relationship-refusal record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The recorded refusal of a relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — A relationship request that cannot proceed under its conditions. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the refusal honestly under the relationship operation identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A refusal result without a fabricated relationship. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Conceal the refusal or record creation when no relationship was admitted. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — The refused relationship is not created. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the relationship-refusal recording rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): refusal-record access must remain within its authorized purpose. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | A refused relationship request. | Records refusal without a link. | The absence is honest. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.6 — Relationship duplicate-prevention record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The record that a duplicate relationship was recognized and prevented. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — A replay recognized by the structural relationship identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Skips the duplicate and records duplicate prevention without creating a second relationship or second terminal truth for the original operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — An explicit duplicate-prevention outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Append the duplicate relationship or count a prevented duplicate as new evidence. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Prevents the duplicate structurally. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the replay-skip-and-record rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-9A.7.4.3.1 — Relationship structural duplicate key: the structural key must identify an existing relationship before duplicate prevention is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | A structurally recognized duplicate. | Records prevention without duplicate creation. | Idempotency is visible in the operation result. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.7 — Relationship-failure record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The failure outcome of a relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — Its actual failure and stable operation identity. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the failure honestly as the relationship operation's own outcome. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A traceable failed relationship operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Substitute a message completion record for the relationship failure. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Terminal failure halts the relationship work item. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the relationship-failure logging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | A failed relationship operation. | Records its own failure. | Message success does not conceal link failure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.8 — Privacy-decision reference record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The operation's reference to an applicable privacy decision. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — The privacy-decision reference governing the stage or material. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Records the reference while preserving protected-content and opaque-key boundaries. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A traceable authorization/privacy basis for the operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Copy raw secrets into an ordinary record as a privacy explanation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: NOT DECIDED

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the privacy-reference logging rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): access to the privacy-decision reference is authorized for its current purpose. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | The applicable decision reference. | Retains the operation's privacy basis safely. | Logging does not reproduce secrets. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.9 — WhatsApp promotion record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The record of a Catalog promotion from the deferred pipeline. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — The actual promotion operation and its B11-governed result. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Records the promotion with the shared parent/child one-operation/one-log separation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — A truthful promotion outcome in the active-batch route. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Record a direct sealed-store write as an authorized promotion or turn child logs into extra parent terminal records. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — Without verified endpoints and an actual commit, no creation is claimed. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: ACCEPTED — C-9A.7.6 — WhatsApp operation records: supplies the promotion logging and parent/child separation rule. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: DESIGNED — C-7Q — Privacy, Deletion, Sensitive-data (§7Q): promotion-record access requires the applicable privacy authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | The Catalog promotion result. | Includes the governed active-batch result. | Child records do not duplicate parent terminal truth. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.6.10 — Frozen-invocation refusal record
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

ALONE
- What it is: ACCEPTED — The recorded refusal when the frozen path is invoked without authorization. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Takes in: ACCEPTED — An unauthorized request to use the deferred archive path. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Does: ACCEPTED — Refuses execution and records the frozen status honestly. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Gives out: ACCEPTED — A refusal record with no decryption or ingest. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Must never: ACCEPTED — Begin decryption or ingest before recording the path's actual authorization state. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]
- Fails closed by: ACCEPTED — Performs no decryption or ingest and retains the refusal record. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: NOT DECIDED
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | An unauthorized archive request. | Records that no execution occurred. | Frozen status remains explicit. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

SUB-PARTS: NONE

### C-9A.7.7 — Consumed Bundle 6 operation contract
Stamp: ACCEPTED    Source: [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

ALONE
- What it is: ACCEPTED — The shared operation protections applied to each WhatsApp operation. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Takes in: ACCEPTED — Stable operation identity, deterministic duplicate key, durable checkpoints, purpose authorization and root-write eligibility where relevant. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Does: ACCEPTED — Commits each state change atomically with its append-only record; enforces structural uniqueness and idempotent replay; recovers only committed checkpoints and records each recovery operation; retains completed per-item results. Technical retry uses 3 total attempts, minimum gaps of 10 then 30 seconds live or 1 then 3 minutes background/nightly, and elapsed maxima of 7 or 15 minutes respectively. A bad, unsafe or unsupported proposal gets exactly 1 careful retry after its durable rejection. Either retry gate closing stops work; useless or unsafe retry may stop early; further continuation requires a recorded real change. Uses one operation/one log for retrieval, use, evaluated-but-unused candidates, acceptance, rejection, omission and failure. Root writes consume B11 batch selection, global claim, WB1 ownership generation/reservation/root-ID binding, WB2 durable `commit_fenced` generation and matching ownership at commit, WB3 exactly one terminal parent record, historical coverage before writes, and B11 recovery/refusals. Privacy precedes relevance; held and sealed boundaries remain in force. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gives out: ACCEPTED — Durable, bounded and auditable operations through the shared accepted contracts. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Must never: ACCEPTED — Reconstruct missing state, let logging recurse or add evidence weight, bypass Catalog, reopen the sealed batch, write without historical coverage, or count a child log as a second parent log. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Fails closed by: ACCEPTED — On uncertainty admits nothing to memory, activates nothing and claims nothing complete; terminal failures halt honestly. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]

TOGETHER
- Fed by: NOT DECIDED
- Gated by: ACCEPTED — C-STORE.5.2 — Bundle 6 operation protections: the full shared operation-protection conditions bind this caller. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Gated by: ACCEPTED — C-7E.12 — Accepted root-write handoff: any root write must satisfy the accepted active-batch handoff. [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3]
- Changes: NOT DECIDED

USED BY
| # | Used in (part ID, and path ID if the use is path-specific) | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| 1 · ACCEPTED | C-9A.7 — B22 — Deferred WhatsApp ingest | The applicable shared operation conditions. | Applies them throughout the deferred path. | No local stage bypasses the accepted common contract. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| 2 · ACCEPTED | C-9A.7.6 — WhatsApp operation records | Actual operation and authorized record content. | Retains one truthful operational result. | Logs create neither recursive operations nor evidence weight. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

SUB-PARTS: NONE

<!-- END BEHAVIOR -->

## Cross-piece USED BY continuations

| Owner whose USED BY is continued | Used in | Takes in there | Does there | Changes there | Source |
|---|---|---|---|---|---|
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | DESIGNED — C-9A.5 — Image Catalog handoff | Image capture and source-carried metadata. | Applies the common capture lifecycle. | Images enter by the same governed front door contract. | [MAP C-7E] [MAP C-9A] |
| C-7E.2 — Minimum intake envelope | DESIGNED — C-9A.5 — Image Catalog handoff | The seven required capture elements. | Carries them without guessing. | The image capture is traceable and identifiable. | [MAP C-7E] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-9A.6 — Image operation records | The record-access purpose. | Restricts access to authorized uses. | Logging does not create an exposure bypass. | [MAP C-9A] |
| C-SACL — Speaker Access-Control Layer (§25.4) | DESIGNED — C-9A.6 — Image operation records | Current record-access authority. | Applies the relevant security boundary. | Only authorized record access proceeds. | [MAP C-9A] |
| C-STORE.5.5.4 — source_times | ACCEPTED — C-9A.7.1.2 — SQLite extraction stage | Actual timestamp values, kinds, provenance, reliability and timezone. | Preserves reliable main-date selection and explicit unknown time. | Import and record times cannot replace the source date. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3] |
| C-STORE.5.5.5 — imported_at | ACCEPTED — C-9A.7.1.2 — SQLite extraction stage | When N.H received or imported the item. | Retains it separately from source time. | The original date is not overwritten by receipt time. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3] |
| C-STORE.5.5.6 — record_created_at | ACCEPTED — C-9A.7.1.2 — SQLite extraction stage | When N.H created its record. | Keeps it separate from original and import times. | Three time families retain their meanings. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A3] |
| C-7E.2 — Minimum intake envelope | ACCEPTED — C-9A.7.1.2 — SQLite extraction stage | Each message's capture envelope. | Admits or reports capture-error. | Malformed messages cannot become forced roots. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.1.4 — WhatsApp privacy stage | The current purpose and applicable third-party rules. | Applies privacy before use. | Accepted design does not silently override governing V10. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md §4 / A30] [V10 §7Q / THIRD-PARTY DATA RULES] |
| C-7E.12 — Accepted root-write handoff | ACCEPTED — C-9A.7.1.5 — Engine and Catalog ingest stage | Catalog-eligible capture and write authority. | Promotes only through the B11 route. | No direct or sealed-batch write occurs. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.2.4 — Authorization before each stage | Stage purpose and proposed access. | Checks authorization at the staging boundary. | Unauthorized stages do not begin. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| C-STORE.5.5.7 — origin_relationship_record [proposed] | ACCEPTED — C-9A.7.3 — Media and attachment ordering | Source and target Origin identities, kind and provenance. | Uses the shared append-only relationship contract. | Recovery cannot create a dangling or rewritten link. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| C-STORE.5.2.11 — Bounded retry | ACCEPTED — C-9A.7.5.5 — WhatsApp bounded technical retry | Failure classification and retry history. | Applies the consumed B9 background bounds. | Retry cannot continue by changing identity or repeating unchanged work. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7E.2 — Minimum intake envelope | ACCEPTED — C-9A.7.5.7 — WhatsApp capture-error outcome | The actual capture information. | Reports capture-error when the envelope cannot be satisfied. | No guessed eligible root is emitted. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| C-STORE.5.2 — Bundle 6 operation protections | ACCEPTED — C-9A.7.7 — Consumed Bundle 6 operation contract | Stable identity, checkpoints, privacy and retry state. | Consumes the already defined shared atoms. | No new local exception is created. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7E.12 — Accepted root-write handoff | ACCEPTED — C-9A.7.7 — Consumed Bundle 6 operation contract | Catalog-eligible item and B11 ownership/coverage state. | Applies the shared write fence and terminal-record boundary. | The sealed historical batch stays untouched. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-9A.6.1 — Image capture record | The requested record use. | Preserves the capture trace under its access rules. | Logging does not authorize disclosure. | [MAP C-9A] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-9A.6.2 — Metadata derivation record | The requested metadata-record use. | Applies the record's privacy boundary. | Only authorized access proceeds. | [MAP C-9A] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-9A.6.3 — Plain-description proposal record | The requested description-record use. | Keeps the proposal trace within its purpose. | Description logging creates no exposure permission. | [MAP C-9A] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | DESIGNED — C-9A.6.4 — Image response record | The requested confirmation/rejection record use. | Applies its privacy rules. | The response remains protected. | [MAP C-9A] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.2.7 — Protected-mechanics prerequisite | Protected-execution and sealed-storage readiness. | Maintains the disabled-path prerequisite. | Standalone acceptance alone cannot enable the path. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.1 — Decrypt-run record | The record-access purpose. | Exposes only permitted operation metadata. | Raw keys and staging content stay protected. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.2 — Message-capture record | The requested record use. | Applies privacy to the operation trace. | Capture logging grants no broader access. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.3 — Media-capture record | The requested media-record use. | Restricts access to the authorized purpose. | Media provenance is not an exposure bypass. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.5 — Relationship-refusal record | The requested refusal-record use. | Retains the safe refusal trace. | Sensitive details are not exposed through refusal logging. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.8 — Privacy-decision reference record | The requested decision-record use. | Preserves safe traceability. | Ordinary records expose no secrets. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |
| C-7Q — Privacy, Deletion, Sensitive-data (§7Q) | ACCEPTED — C-9A.7.6.9 — WhatsApp promotion record | The requested promotion trace. | Applies its access boundary. | A promotion record cannot authorize disclosure. | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §3] |

## Scope and path placement

C-9A is the image front-door branch entering **P-MAIN — End-to-end main path** through C-7E. Every local descendant supplies that same front door or its deferred WhatsApp design; the hierarchy carries that path placement. This adds no new path ID and does not complete the missing live-response synchronization. C-7E's existing incoming image use is reciprocated below.

The ordinary image sequence is DESIGNED. B22, A30 and A3.2/A3.3 are ACCEPTED standalone design, with status established by their separate receipts. Neither status proves implementation. The frozen WhatsApp source is described solely to preserve the future design and its restrictions. No archive, key or plaintext has been opened, and no ingest is performed.

The common envelope, typed time fields and append-only Origin relationship fields retain their existing C-STORE.5.5 / C-7E identities. Their fields and values are reused as shared atoms, not assigned second competing schemas. The proposed `relationship_operation_id` remains proposed; the source supplies its role and duplicate identity, not an encoding.


## Cross-piece TOGETHER continuations for incoming uses

| Using card | Field | Current owner | Condition / handoff | Source |
|---|---|---|---|---|
| C-7E — Catalog Front Door + pre-ingest holding (§7E) | Fed by | C-9A — Image ingest front door (§9A) | DESIGNED — supplies image captures with the same minimum envelope. | [MAP C-7E] [MAP C-9A] |



## Source conflicts and explicit source-scope differences

| Kind | Sources and opposing content | Treatment |
|---|---|---|
| [SOURCE CONFLICT] | V10 §7Q / THIRD-PARTY DATA RULES requires stronger default restriction for minors and highly vulnerable people. Bundle 6 policy §4 A30 and mechanical §11 B22 prohibit automatic stronger restriction, block, weakened analysis or special simulation prohibition solely for age or vulnerability. | V10 remains governing. The accepted opposing target is preserved explicitly in C-9A.7.1.4; no reconciliation or hidden integration is chosen. |
| [SOURCE CONFLICT] | Bundle 6 mechanical §11 says no accepted B7 package exists and Bundle 5 is paused. The pinned B7 closure receipt §§2,4–6 establishes acceptance of B7 v1_3 at SHA-256 `7fda28e994336a7ea0d17e217025cb71c116ec42ce3ecde3d8c9110783b52aad`. | Preserve the stale status statement as a source disagreement. Do not repeat it as the current repository state. The receipt still authorizes no integration or implementation; the required integrated protected path and separate ingest authorization remain prerequisites. |
| Scope distinction | The Map lists B22/A30 as formerly open mechanics/policy while also marking them resolved in its design-complete sentence; the accepted receipts establish their standalone design scope. | This chapter includes the accepted content. Acceptance does not unfreeze the archive. |
| Scope distinction | The B7 receipt itself says delivered, awaiting independent audit; formal receipt closure depends on that audit. Its explicit source acceptance is separately recorded. | Do not equate source acceptance with a passed receipt audit, formal closure, runtime readiness or integration. |

## Explicit remaining scope

- **CH08-a — C-7Q** owns the full A7/B7 privacy architecture, records, execution boundary, protected stores, detection, separation, derivative discovery, verification and all other privacy operations. The B22 requirements consumed here are complete for this caller; the architecture is not asserted absent merely because this chapter does not duplicate it.
- **CH05-a — C-7G** and **CH05-d — C-7H** own complete generic retry architecture and orchestration. The accepted B9 numerical bounds and shared behavior used by B22 are already included here and in C-STORE.5.2.
- **CH03-a — C-STORE.5.5** owns the complete B21 typed time and relationship schemas, including `timestamp_value`, `is_main_real_life_date`, `known_reliable`, `known_unreliable`, `unknown`, `imported_at`, `record_created_at`, and the relationship's source/target/kind/provenance fields. C-9A consumes them without altering their identities. **CH04-a — C-7E** owns speaker/title resolution, holding and root handoff.
- **CH05-a/c** own A3.4's full no-surroundings reading rule and retrieval behavior; **CH06-c** owns A3.5's Person-Box holding; **CH03-a / CH05-a** own A3.1's Keeper/meaning boundary. Only A3.2/A3.3 are current policy placement.
- **CH11** owns connected side-path assembly. The stage order here is the complete decided B22 order, not a newly invented WhatsApp path ID. **CH12** will regenerate the gap, source-conflict and coverage appendices.
- The source's historical archive dates, file-size snapshot, backup location and project acceptance workflow are excluded from behavior under contract §1.3. The receipts supply acceptance and source identity only.

## Additional undecided implementation slots

| Slot | Owner | Value | Source |
|---|---|---|---|
| Image metadata extraction algorithm and exact image-description/context-meaning record schemas | C-9A.1–4 | NOT DECIDED | [V10 §9A] [MAP C-9A] |
| Separate image confirmation/rejection event schema and handling beyond the stated proposal boundary | C-9A.4 / C-9A.6.4 | NOT DECIDED | [MAP C-9A] |
| Exact image operation event identifiers and encodings | C-9A.6 | NOT DECIDED | [MAP C-9A] |
| Decryption command, script and actual key-handling implementation | C-9A.7.1.1 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| Concrete WhatsApp deterministic capture-ID derivations and work-item serialization | C-9A.7.4 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| Encoding of proposed relationship_operation_id and canonical endpoint comparator | C-9A.7.4.3 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |
| Exact B22 staging-artifact registry schema and operation-specific state labels | C-9A.7.2 | NOT DECIDED | [04/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md §11] |

## Review of plain gates and empty boxes

All populated TOGETHER lines name their governing or supplying cards. Stage execution, confirmation, endpoint durability, privacy and retry limits are actual prerequisites. Carrying a field or writing a required log is not by itself a newly invented runtime gate. Event cards retain empty failure boxes where the source decides no separate log-storage failure procedure; their shared operation rules and access boundaries remain present. Record encodings and algorithms have not been invented from the named conceptual fields.

## Appendix A carry-forward — this piece

| Part | Field or cell | Value |
|---|---|---|
| C-9A | Changes | NOT DECIDED |
| C-9A.1 | Fails closed by | NOT DECIDED |
| C-9A.1 | Gated by | NOT DECIDED |
| C-9A.1 | Changes | NOT DECIDED |
| C-9A.2 | Changes | NOT DECIDED |
| C-9A.3 | Changes | NOT DECIDED |
| C-9A.4 | Fed by | NOT DECIDED |
| C-9A.4 | Changes | NOT DECIDED |
| C-9A.5 | Changes | NOT DECIDED |
| C-9A.6 | Fails closed by | NOT DECIDED |
| C-9A.6 | Changes | NOT DECIDED |
| C-9A.6.1 | Fails closed by | NOT DECIDED |
| C-9A.6.1 | Changes | NOT DECIDED |
| C-9A.6.2 | Fails closed by | NOT DECIDED |
| C-9A.6.2 | Changes | NOT DECIDED |
| C-9A.6.3 | Fails closed by | NOT DECIDED |
| C-9A.6.3 | Changes | NOT DECIDED |
| C-9A.6.4 | Fails closed by | NOT DECIDED |
| C-9A.6.4 | Changes | NOT DECIDED |
| C-9A.7 | Changes | NOT DECIDED |
| C-9A.7.1 | Changes | NOT DECIDED |
| C-9A.7.1.1 | Fed by | NOT DECIDED |
| C-9A.7.1.1 | Changes | NOT DECIDED |
| C-9A.7.1.2 | Changes | NOT DECIDED |
| C-9A.7.1.3 | Fed by | NOT DECIDED |
| C-9A.7.1.3 | Changes | NOT DECIDED |
| C-9A.7.1.4 | Fed by | NOT DECIDED |
| C-9A.7.1.4 | Changes | NOT DECIDED |
| C-9A.7.1.5 | Fed by | NOT DECIDED |
| C-9A.7.1.5 | Changes | NOT DECIDED |
| C-9A.7.2 | Changes | NOT DECIDED |
| C-9A.7.2.1 | Fed by | NOT DECIDED |
| C-9A.7.2.1 | Changes | NOT DECIDED |
| C-9A.7.2.2 | Changes | NOT DECIDED |
| C-9A.7.2.3 | Fails closed by | NOT DECIDED |
| C-9A.7.2.3 | Gated by | NOT DECIDED |
| C-9A.7.2.3 | Changes | NOT DECIDED |
| C-9A.7.2.4 | Fed by | NOT DECIDED |
| C-9A.7.2.4 | Changes | NOT DECIDED |
| C-9A.7.2.5 | Changes | NOT DECIDED |
| C-9A.7.2.6 | Fails closed by | NOT DECIDED |
| C-9A.7.2.6 | Gated by | NOT DECIDED |
| C-9A.7.2.6 | Changes | NOT DECIDED |
| C-9A.7.2.7 | Changes | NOT DECIDED |
| C-9A.7.3 | Fed by | NOT DECIDED |
| C-9A.7.3 | Changes | NOT DECIDED |
| C-9A.7.4 | Gated by | NOT DECIDED |
| C-9A.7.4 | Changes | NOT DECIDED |
| C-9A.7.4.1 | Gated by | NOT DECIDED |
| C-9A.7.4.1 | Changes | NOT DECIDED |
| C-9A.7.4.2 | Gated by | NOT DECIDED |
| C-9A.7.4.2 | Changes | NOT DECIDED |
| C-9A.7.4.3 | Changes | NOT DECIDED |
| C-9A.7.4.3.1 | Gated by | NOT DECIDED |
| C-9A.7.4.3.1 | Changes | NOT DECIDED |
| C-9A.7.4.3.2 | Fails closed by | NOT DECIDED |
| C-9A.7.4.3.2 | Fed by | NOT DECIDED |
| C-9A.7.4.3.2 | Changes | NOT DECIDED |
| C-9A.7.4.3.2 | Gated by | NOT DECIDED |
| C-9A.7.4.3.3 | Fed by | NOT DECIDED |
| C-9A.7.4.3.3 | Changes | NOT DECIDED |
| C-9A.7.4.3.3 | Gated by | NOT DECIDED |
| C-9A.7.5 | Changes | NOT DECIDED |
| C-9A.7.5.1 | Changes | NOT DECIDED |
| C-9A.7.5.2 | Fed by | NOT DECIDED |
| C-9A.7.5.2 | Changes | NOT DECIDED |
| C-9A.7.5.2 | Gated by | NOT DECIDED |
| C-9A.7.5.3 | Fed by | NOT DECIDED |
| C-9A.7.5.3 | Changes | NOT DECIDED |
| C-9A.7.5.4 | Fed by | NOT DECIDED |
| C-9A.7.5.4 | Changes | NOT DECIDED |
| C-9A.7.5.4 | Gated by | NOT DECIDED |
| C-9A.7.5.5 | Fed by | NOT DECIDED |
| C-9A.7.5.5 | Changes | NOT DECIDED |
| C-9A.7.5.6 | Fed by | NOT DECIDED |
| C-9A.7.5.6 | Changes | NOT DECIDED |
| C-9A.7.5.6 | Gated by | NOT DECIDED |
| C-9A.7.5.7 | Fed by | NOT DECIDED |
| C-9A.7.5.7 | Changes | NOT DECIDED |
| C-9A.7.6 | Changes | NOT DECIDED |
| C-9A.7.6.1 | Changes | NOT DECIDED |
| C-9A.7.6.2 | Changes | NOT DECIDED |
| C-9A.7.6.3 | Changes | NOT DECIDED |
| C-9A.7.6.4 | Changes | NOT DECIDED |
| C-9A.7.6.5 | Changes | NOT DECIDED |
| C-9A.7.6.6 | Changes | NOT DECIDED |
| C-9A.7.6.7 | Changes | NOT DECIDED |
| C-9A.7.6.7 | Gated by | NOT DECIDED |
| C-9A.7.6.8 | Fails closed by | NOT DECIDED |
| C-9A.7.6.8 | Changes | NOT DECIDED |
| C-9A.7.6.9 | Changes | NOT DECIDED |
| C-9A.7.6.10 | Fed by | NOT DECIDED |
| C-9A.7.6.10 | Changes | NOT DECIDED |
| C-9A.7.6.10 | Gated by | NOT DECIDED |
| C-9A.7.7 | Fed by | NOT DECIDED |
| C-9A.7.7 | Changes | NOT DECIDED |

## Retained plain-gate inventory

All populated TOGETHER lines name an owning or connected card; no plain gate remains.

## Source coverage added by CH04-e

| Source | Scope read | Landing / exclusion |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §1A, §9A and §12 whole; §7Q whole, placing only current image/privacy boundaries and the age-default conflict. | C-9A and C-9A.1–5; frozen path in C-9A.7; privacy conflict retained; remaining §7Q owned by CH08-a. |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: C-9A and C-7E in full; C-9A image and deferred-archive placement. | C-9A.1–6; C-7E incoming continuation and P-MAIN image branch. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §3 shared mechanical spine and §11 B22 in full. | C-9A.7 with all five stages, protected handling, independent recovery and event classes; shared atoms reused. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: §4 A3 and A30 in full; current placement A3.2/A3.3 and A30, with other A3 policies assigned to their named owners. | C-9A.7.1.2 source granularity/times and C-9A.7.1.4 A30; other A3 content assigned to named owners. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: §§1–4 in full: source identity, audit, explicit acceptance and standalone scope. | Receipt identity/status evidence; project workflow excluded and implementation not asserted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: §§1–4 in full: source identity, audit, explicit acceptance and standalone scope. | Receipt identity/status evidence; project workflow excluded and implementation not asserted. |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Acceptance/status evidence only; no B7 mechanisms adopted from receipt summaries and no formal receipt PASS assumed. | Receipt identity/status evidence; project workflow excluded and implementation not asserted. |

## Coverage matrix — cumulative carried inventory





The following inventory retains the preceding pieces’ placements and read status. This piece’s additional placements and deferrals are in the source-scope table above; inherited notes are not fresh whole-read claims.
### File coverage

| Row | Source | Read scope | Placement |
|---|---|---|---|
| F001 | `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped read in CH04-b: §0B; §6A SCHEMA CONSTRAINTS; §6B schema/status boundary; full §7E-TSC §§1–31. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.1; C-STORE.2; C-STORE.3; CY-A Chapter 3-b: C-READ and its v1 record, validator, writer, quarantine, production-boundary and operation-record sub-parts; CY-A/CY-F reading-write interfaces. Chapter 3-c: governing checks for C-READ.10; A2/firmness additions stay ACCEPTED, never BUILT. Chapter 3-d: source-status and no-production-write boundaries; governing operational living-memory rule at C-READ.11.9.4.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.3, C-ENGINE-C.3.1, C-ENGINE-C.3.2, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.11.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1, C-ENGINE-AB.1.1, C-ENGINE-AB.1.2, C-ENGINE-AB.1.3, C-ENGINE-AB.2, C-ENGINE-AB.2.1, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.1, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.2.4, C-ENGINE-AB.3, C-ENGINE-AB.4, C-ENGINE-AB.5, C-ENGINE-AB.6, C-ENGINE-AB.8, C-ENGINE-AB.9.; CH03-k: C-INDEX, C-INDEX.1, C-INDEX.1.1, C-INDEX.1.2, C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.1, C-INDEX.4.2, C-INDEX.4.3, C-INDEX.4.4, C-INDEX.4.5, C-INDEX.4.7, C-INDEX.4.8, C-INDEX.5, C-INDEX.6.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.2, C-GOLD.6.3, C-GOLD.7, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.1, C-INGEST.2, C-INGEST.3, C-INGEST.4, C-INGEST.4.1, C-INGEST.4.2, C-INGEST.4.3, C-INGEST.4.4, C-INGEST.4.5, C-INGEST.4.6, C-INGEST.4.7, C-INGEST.4.8, C-INGEST.4.8.1, C-INGEST.4.8.2, C-INGEST.4.8.3, C-INGEST.4.8.4, C-INGEST.4.9, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.2, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.5, C-DETECT.3.6, C-DETECT.4.1.; CH04-a: C-7E, C-7E.1, C-7E.1.1, C-7E.1.2, C-7E.2, C-7E.3, C-7E.4, C-7E.5, C-7E.5.1, C-7E.5.2, C-7E.5.3, C-7E.5.4, C-7E.5.5, C-7E.5.6, C-7E.6, C-7E.6.1, C-7E.6.2, C-7E.6.3, C-7E.6.4, C-7E.6.5, C-7E.6.6, C-7E.6.7, C-7E.7, C-7E.8, C-7E.8.1, C-7E.8.2, C-7E.8.3, C-7E.8.4, C-7E.9, C-7E.9.1, C-7E.9.2, C-7E.9.2.1, C-7E.9.2.2, C-7E.9.2.3, C-7E.9.2.4, C-7E.9.3, C-7E.9.3.1, C-7E.9.3.2, C-7E.9.3.3, C-7E.9.3.4, C-7E.9.3.5, C-7E.9.3.6, C-7E.9.4, C-7E.10, C-7E.10.1, C-7E.10.2, C-7E.11, C-7E.12, C-7E.13, C-7E.13.1, C-7E.13.4, C-7E.13.5, C-7E.13.6. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F002 | `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md` | Scoped read in CH04-b: §3N; inspection conflict. Prior read credits retained. | EXCLUDED: interaction/workflow guidance under §1.3 and §2.4. NOT PLACED: remaining behavior belongs to other component groups.; Chapter 3-a: C-STORE.2.3 Chapter 3-b: C-READ.1 confidence semantics and C-READ.2 uncertainty-preserving shape gate; remaining scope retained. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.2, C-ENGINE-AB.2.2, C-ENGINE-AB.2.2.2, C-ENGINE-AB.2.3, C-ENGINE-AB.8.; CH03-l: C-GOLD, C-GOLD.2, C-GOLD.2.1, C-GOLD.3, C-GOLD.3.1, C-GOLD.4, C-GOLD.4.1, C-GOLD.4.2, C-GOLD.4.3, C-GOLD.4.4, C-GOLD.4.5, C-GOLD.4.6, C-GOLD.5, C-GOLD.6, C-GOLD.6.1, C-GOLD.6.3, C-GOLD.8.3, C-GOLD.8.5.10, C-GOLD.8.5.11.; CH04-a: C-7E, C-7E.1.2, C-7E.5.2, C-7E.6.1, C-7E.6.2, C-7E.7, C-7E.8.4, C-7E.13.3. CH04-b: see the exact source-scope and landing table above. |
| F003 | `01_AUTHORITATIVE/cursorrules` | Scoped reread for CH03-o; prior whole-read credit retained where previously recorded | EXCLUDED: coding-process rules under §1.3. NOT PLACED: built-code boundaries belong to store, reader and code-boundary groups. Chapter 3-b: C-READ.1.12 per-store/global-key conflict and C-READ.3 shared write boundary; workflow remains excluded. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet.; CH03-i: C-ENGINE-AB.5.; CH03-k: C-INDEX.2, C-INDEX.2.1, C-INDEX.3, C-INDEX.3.1, C-INDEX.3.2, C-INDEX.3.3, C-INDEX.4, C-INDEX.4.6.; CH03-l: C-GOLD, C-GOLD.9.; CH03-o: C-INGEST, C-INGEST.4, C-INGEST.4.7, C-INGEST.6. |
| F004 | `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md` | Scoped read in CH04-b: Embedded TSC §§15–16; conflicting inspection and failed-authorization text. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. Chapter 3-c: governing-boundary check only; no new behavior attributed to a search snippet. CH04-b: see the exact source-scope and landing table above. |
| F005 | `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped read in CH04-b: C-TSC and CY-D; component naming and path ownership. Prior read credits retained. | C-7A and cited sub-parts; C-7B and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; Chapter 3-a: C-STORE; C-STORE.3.4; CY-A Chapter 3-b: C-READ component name, operation logging and consumer/caller relationships; CY-A/CY-F interfaces. Chapter 3-c: component ownership/names and Group A/D boundary; accepted A2 supplies behavior. Chapter 3-d: names, Group A ownership and per-reading seam versus full CY-G boundary.; CH03-j: C-ENGINE-C, C-ENGINE-C.1, C-ENGINE-C.2.1, C-ENGINE-C.2.2, C-ENGINE-C.4, C-ENGINE-C.6, C-ENGINE-C.7, C-ENGINE-C.8, C-ENGINE-C.9.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.1.1, C-ENGINE-AB.1.3, C-ENGINE-AB.2.1, C-ENGINE-AB.2.4, C-ENGINE-AB.4, C-ENGINE-AB.6, C-ENGINE-AB.6.1.; CH03-k: C-INDEX, C-INDEX.2, C-INDEX.3, C-INDEX.5, C-INDEX.6, C-INDEX.6.1, C-INDEX.6.2, C-INDEX.6.3, C-INDEX.6.4, C-INDEX.6.5, C-INDEX.6.6.; CH03-l: C-GOLD, C-GOLD.4, C-GOLD.4.6, C-GOLD.6, C-GOLD.6.2, C-GOLD.7, C-GOLD.7.1, C-GOLD.7.2, C-GOLD.7.3, C-GOLD.7.4.; CH03-o: C-INGEST, C-INGEST.4.4, C-INGEST.4.7, C-INGEST.5, C-INGEST.5.1, C-INGEST.5.2, C-INGEST.5.3, C-INGEST.5.4, C-INGEST.6.; CH03-p: C-DETECT, C-DETECT.1, C-DETECT.1.1, C-DETECT.1.2, C-DETECT.1.3, C-DETECT.2, C-DETECT.2.1, C-DETECT.2.2, C-DETECT.2.3, C-DETECT.2.4, C-DETECT.2.5, C-DETECT.3, C-DETECT.3.1, C-DETECT.3.3, C-DETECT.3.4, C-DETECT.3.6, C-DETECT.4, C-DETECT.4.1, C-DETECT.4.1.1, C-DETECT.4.1.2, C-DETECT.4.2.; CH04-a: C-7E, C-7E.3, C-7E.4, C-7E.5, C-7E.5.2, C-7E.6.1, C-7E.6.4, C-7E.7, C-7E.8, C-7E.11, C-7E.13, C-7E.13.1, C-7E.13.2, C-7E.13.3, C-7E.13.4, C-7E.13.5, C-7E.13.6, C-7E.13.7. CH04-b: see the exact source-scope and landing table above.  CH04-c: scoped read; exact scope and placement in the current source table.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
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
| F035 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A29_HOLD_UNTIL_ENOUGH_POLICY_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | C-7B.7 and cited sub-parts. Remaining source scope NOT PLACED: belongs to other component groups; history/process excluded under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F036 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_CANDIDATE.md` | Scoped reread for CH03-j; prior whole-read credit retained where previously recorded | C-READ.10 and all A2-cited descendants: §§1–10 identity, card/preparation/event ownership, acceptance/correspondence, commit/recovery, legacy mapping, lifecycle, semantic/safety boundaries, references/rereading and logging. EXCLUDED: source revision history, acts of acceptance, implementation workflow and self-audit claims under §1.3. Other consumer mechanics remain with their owning groups.  Correction 1: all 352 cards checked for placement of decided prohibitions, failure handling and gates; the nine sequence steps are linked to their defining cards.; CH03-j: C-ENGINE-C, C-ENGINE-C.3.3, C-ENGINE-C.4, C-ENGINE-C.5, C-ENGINE-C.6, C-ENGINE-C.9, C-ENGINE-C.11. |
| F037 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_A2_TELLING_OBJECT_IDENTITY_PACKAGE_v1_8_PACKAGE_COMPLETE_RECORD_v1_0.md` | Read whole for CH03-j | Acceptance/status and exact source-identity verification only. EXCLUDED from behavior: receipt history, acceptance narrative and process under §1.3; no mechanism sourced from the receipt.; CH03-j: Status/provenance only; no behavior from this receipt or historical blocker. |
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
| F048 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for C-STORE.4; receipt narrative excluded under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker. |
| F049 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B11_ACTIVE_WRITABLE_BATCH_ARCHITECTURE_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §13 TSC caller boundary. Prior read credits retained. | Chapter 3-a: C-STORE.4 and all descendants. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: §10 cross-batch reading reread for boundary check; no new B11 behavior written here, Chapter 3-a placement retained.; CH04-a: C-7E, C-7E.1.2, C-7E.5.6, C-7E.6.3, C-7E.6.4, C-7E.12. CH04-b: see the exact source-scope and landing table above. |
| F050 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole read in CH04-b: Acceptance/status evidence only. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F051 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B15_TSC_TRANSACTIONAL_STORE_ARCHITECTURE_v1_4_CANDIDATE.md` | Whole read in CH04-b: Structural store, exact tables, constraints, transactions, recovery, archive, logging and open implementation choices. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F052 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_PROMOTION_EVALUATION_EVIDENCE_BRIDGE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH03-n | Status/identity checked for NHD-B16EEB; globally unique slot identifiers retained; acceptance narrative EXCLUDED by §1.3; CH03-l: Status/provenance only; no behavior from this receipt or historical blocker.; CH03-m: C-GOLD.1.8.1.5.1.; CH03-n: C-GOLD.1.10, C-GOLD.1.11, C-GOLD.1.11.1, C-GOLD.1.11.2, C-GOLD.1.11.3, C-GOLD.1.11.4, C-GOLD.1.11.5, C-GOLD.1.11.6, C-GOLD.1.11.7, C-GOLD.1.11.8, C-GOLD.1.11.9, C-GOLD.1.11.10, C-GOLD.1.11.11, C-GOLD.1.11.12, C-GOLD.1.11.13, C-GOLD.1.11.14, C-GOLD.1.11.15, C-GOLD.1.11.16, C-GOLD.1.11.17, C-GOLD.1.12, C-GOLD.1.12.1, C-GOLD.1.12.2, C-GOLD.1.12.3, C-GOLD.1.12.4, C-GOLD.1.12.5. |
| F053 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | §§2–6 establish exact accepted standalone scope and source identity. EXCLUDED from behavior: receipt history/roles/process; no mechanism sourced from receipt. |
| F054 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B16_QUARANTINE_PROMOTION_EVIDENCE_ARCHITECTURE_v1_0_CANDIDATE.md` | Read whole for Chapter 3-d; pinned Git blob and SHA-256 verified | C-READ.11 and every descendant: complete §§1–11 seam; §13 traces checked against the same rules. §12 external ownership and unspecified details recorded separately. EXCLUDED under §1.3: source status/history/process, self-audit and delivery narrative (§§14–15). |
| F055 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F056 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F057 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md` | Scoped reread for CH03-m; prior whole-read credit retained where previously recorded | C-READ.7.2 and its reciprocal C-READ.7 link: ACCEPTED guard from §1.2 (NHD-B24), matching FR-0608 CARRIED. Remaining B24 behavior NOT PLACED: belongs to later owning templates; no other B24 mechanism added here. Chapter 3-c C-READ.10.3.8.8 and source-conflict register: structural-disposition difference retained against A2; no new retry policy.; CH03-m: C-GOLD.1.8.1.5.2, C-GOLD.1.8.1.5.2.1, C-GOLD.1.8.1.5.2.2, C-GOLD.1.8.1.5.2.3, C-GOLD.1.8.4.3.1, C-GOLD.1.8.4.5, C-GOLD.1.8.4.8. |
| F058 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_PACKAGE_COMPLETE_RECORD_v1_0.md` | Newly read whole for this correction, all 132 lines; pinned Git blob verified | §§2–3, 5 and 12 establish the accepted standalone status and exact v7 identity used for C-READ.7.2; no behavior sourced from this receipt. EXCLUDED: closure history/process under §1.3; no implementation or integration claimed. |
| F059 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
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
| F079 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_1.md` | Scoped read in CH04-b: §5 paths 3–4; authority owner/limit cross-check. Prior read credits retained. | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. CH04-b: see the exact source-scope and landing table above. |
| F080 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_5_PRIVACY_SECURITY_ACCESS_AND_TSC_AUTHORITY_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
| F081 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_CANDIDATE_v1_2.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F082 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_INGEST_PROVENANCE_RESEARCH_CREATION_AND_PERSONAL_LEARNING_FINAL_CONSOLIDATION_AND_CLOSEOUT_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_1.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check.  CH04-d: exact read scope and placement in the current source table; prior credits retained. |
| F083 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Bundle 6 mechanics; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F084 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped read in CH04-b: §3 held/sealed restrictions and privacy precedence. Prior read credits retained. | Chapter 3-a: C-STORE.5 / operation protections, B17, B20, B21; other component scopes NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: C-7E, C-7E.2, C-7E.8, C-7E.9.1, C-7E.11, C-7E.12. CH04-b: see the exact source-scope and landing table above.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F085 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Read whole for CH04-a | Chapter 3-a: ACCEPTED status evidence for Origin policy; receipt narrative EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3.; CH04-a: Status/provenance only; no behavior from this receipt or historical blocker.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
| F086 | `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped reread for CH04-a; prior whole-read credit retained where previously recorded | Chapter 3-a: C-STORE.5 / Origin preservation policy; A3.4–A3.5 and other components NOT PLACED: later owning groups; history/workflow EXCLUDED under §1.3. EXCLUDED: source history/workflow under §1.3. Chapter 3-b: Navigation excerpt only; no new behavior sourced in this piece.; CH03-i: C-ENGINE-AB, C-ENGINE-AB.7, C-ENGINE-AB.8.; CH04-a: C-7E.12.  CH04-d: exact read scope and placement in the current source table; prior credits retained.  CH04-e: exact read scope and placement in the current source table; prior credits retained. |
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
| F113 | `05_ACTIVE_CANDIDATE/NH_B24_REJECTION_CATEGORY_DECISION_2026-09-23_v0_1_CANDIDATE.md` | Carried through Chapter 3-a: Not yet read | NOT PLACED: no Chapters 0–2 (carried placement) behavior is sourced from this file; remaining content belongs to later owning groups or appendices, subject to its read and version check. |
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
| V10-H031 | ## 7F. CONTEXT RETRIEVAL  [CONCEPTUALLY DESIGNED, NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading. Chapter 3-b: C-READ.1.9 retrieval audit and genuine no-context audit; retrieval machinery remains with C-7F. |
| V10-H032 | ## 7G. MEANING ENGINE INTERIOR  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ acceptance/shape distinction and caller relationship; C-READ.3 new-root write handoff also cites the nested §7G-A subsection.  Chapter 3-c: governing comparison for C-READ.10; accepted A2/firmness adds no build claim. |
| V10-H033 | ### §7G CREATION-AWARE MODE  [SETTLED CONCEPT — NOT BUILT] | Partial placement: C-7B.2.8.4 and cited sub-parts; C-7B.11.2. Remaining detail NOT PLACED: its owning components or paths are outside Group 0.  CH04-d: C-14 and explicit shared/deferred owners. |
| V10-H034 | ## 7H. REREAD LIFECYCLE  [CONCEPTUALLY DESIGNED, NOT BUILT] | Partial placement: C-7B and cited sub-parts. Remaining detail NOT PLACED: its owning components or paths are outside Group 0. Chapter 3-b: C-READ reread output relationship; detailed orchestration remains with C-7H. |
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
| V10-H072 | ## 14. THE CHAT FRONT DOOR  [PARTIALLY SETTLED, PARTIALLY OPEN — NOT BUILT] | NOT PLACED: section belongs to another component group or a later path/appendix; no Chapters 0–2 (carried placement) behavior sourced from this heading.  CH04-c: live-loop surface and model boundary in C-13; remaining chat/model internals retain their later owners.  CH04-d: C-14 and explicit shared/deferred owners. |
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













## READ RECORD

Each current source identity was checked against its pinned Git blob. Whole-file credit is limited to rows marked Whole; all other reading is scoped. Contract §§5–11 and the complete lessons were reopened before writing; §11.3 is reopened after writing.

| Source file | Reading credit | SHA-256 |
|---|---|---|
| `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md` | Scoped: §1A, §9A and §12 whole; §7Q whole, placing only current image/privacy boundaries and the age-default conflict. | `2d9ed4c606286c3af024d760a2855be85988553925d80b816627da2cc14aa32c` |
| `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md` | Scoped: C-9A and C-7E in full; C-9A image and deferred-archive placement. | `33af648d9a1e821aa90f166ae441c7b082170c315d050b6d8c2fa5c0c3d11865` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_v1_4_CANDIDATE.md` | Scoped: §3 shared mechanical spine and §11 B22 in full. | `bc1095955525fcea56cb4d16057c93bfb15eec42a83a1b644baf0e87a473f64e` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_v1_0_CANDIDATE.md` | Scoped: §4 A3 and A30 in full; current placement A3.2/A3.3 and A30, with other A3 policies assigned to their named owners. | `b37f965a343dbf86130f96591d58de9288ad0a746a68e8ae8fdd7b66208a63da` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_MECHANICAL_DESIGN_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: §§1–4 in full: source identity, audit, explicit acceptance and standalone scope. | `c5e379f508f3d2c498dfcecfe567db20db4362872de4feff4c7da57d4ff7de79` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_BUNDLE_6_POLICY_DECISIONS_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Scoped: §§1–4 in full: source identity, audit, explicit acceptance and standalone scope. | `4b37668ea3a95463e49bc27ada107be78cd807e3cbf8455a06b912901b4346f6` |
| `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` | Whole: Acceptance/status evidence only; no B7 mechanisms adopted from receipt summaries and no formal receipt PASS assumed. | `6179207c8d472ed81df208ceede832976f209e88e443ed7121a428d07a8b1a3d` |

Instruction fingerprints:

- Contract v1_0: `e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1`.
- Writer lessons v0_1: `635be95b861c181efb3b7bc1b2a8405ab706f864068a0b88f31fb91971adf3e6`.
- Run instructions v0_2: `93431167c0fb03fe1216ebbc12655ac640d71bcb7a59659cd123f51e72a54611`.

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

### READ-folder files not yet read whole

83 inherited pending files remain. Scoped reads do not remove whole-file obligations; previous read credits and source placements remain.

- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_CHAT_INTERFACE_POLICY_PACKAGE_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_ROOM_START_POLICY_PACKAGE_v1_2_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A19_UNREAL_ENGINE_5_RUNTIME_DIRECTION_ACCEPTANCE_RECORD_v1_1.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_ACCEPTANCE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B1_CONTEXT_RETRIEVAL_PARAMETER_ARCHITECTURE_v1_0_CANDIDATE.md`
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
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_5_IDENTITY_AND_PERSONAL_MODE_ACCESS_WIRING_v1_5_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_8_CONNECTION_CAPABILITY_WAITING_AND_ACCEPTANCE_ROUTES_WIRING_v1_2_CANDIDATE.md`
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
- `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`

## CONTRACT CHECK

CONTRACT CHECK (against the cloned contract, SHA-256 e78c7a8c8a448ff20966002465c8d6a330000900802c0b19a48e8a124e5ceba1)
§1.3 no history/actions/roles/workflow in this chapter: PASS — 54 behavior cards reviewed; 0 project/workflow hits. Source-status and scope notes are outside the behavior cards.
§1.4 every gap written as NOT DECIDED: PASS — 96 empty fields/cells exactly match the register; 7 additional implementation slots are explicit.
§1.5 conflicts marked, none resolved: PASS — 2 explicit conflict-register rows. The governing V10 age-default restriction and accepted A30 target remain opposed explicitly. The stale B22 assertion that B7 is unaccepted is recorded against the actual acceptance receipt, without treating acceptance as integration, implementation or authorization.
§3 exactly one stamp per line: PASS — 54 headers, 438 populated fields and 96 USED BY rows checked; 0 BUILT field lines. Relationship stamps follow the named card.
§4 every behavior line cited in the exact format: PASS — 15 distinct current citations resolve at the pin; all populated fields and relationship rows are cited. Claims were reviewed against the mapped source sections.
§5.4 one name per thing: PASS — 54 current IDs checked for duplicates, prior collisions and exact official names; shared atoms retain their previous names.
§6 all template fields present, in order, for every part: PASS — 54 templates and 534 field lines checked.
§6.3 reciprocity within this chapter: PASS — 94 internal lines cover 94 reciprocal pairs; 27 external-use continuations and 1 incoming continuations name both endpoints.
§6.4 every decided detail written in, no citation used in place of content: PASS — The image sequence, factual-treatment confirmation boundary, common seven-element intake and lifecycle, four image event classes, all five B22 stages, separate Origins and three time families, exact typed source-time use, key and plaintext protections, artifact accounting, per-stage authorization, interrupted staging recovery, durable derivative handling, independent message/media/relationship work identities, proposed relationship_operation_id, endpoint-kind-provenance duplicate identity, directional and symmetric ordering, all incomplete-work recovery branches, numerical retry bounds, capture-error and terminal outcomes, ten WhatsApp event classes and the shared B11/operation contract are present. The full already-defined B21 fields and later B7/generic retry owners are named explicitly.
§6.5 sub-parts recursed to the bottom: PASS — 53 declared child/shared references and 54 owned cards checked; 38 explicit steps have 0 empty TOGETHER cases. Image stages and records, B22 stages, protected-lifecycle requirements, work-item identity kinds, relationship key ordering, recovery cases and operation-event classes have separate cards. Existing envelope, typed-time and relationship schema atoms retain their earlier identities rather than being redefined.
§9 coverage matrix rows added for every file used: PASS — 7 current source identities, 145 READ-folder inventory rows and 107 V10 heading rows checked; 145 named source paths exist at the pin. Earlier credits and placements remain cumulative.
§10.11 no recommendation, no sentence addressed to Ness: PASS — the behavior was reviewed as system operation and boundaries; 0 formula phrases and 0 project/workflow hits.
Files read whole for this chapter: `04_ACCEPTED_STANDALONE_DESIGNS/NH_B7_PRIVACY_ENFORCEMENT_AND_PROTECTED_HANDLING_ARCHITECTURE_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md`.

Computed self-check output:

| Check | Count |
|---|---|
| cards | 54 |
| field_lines | 534 |
| populated_fields | 438 |
| not_decided_boxes | 96 |
| not_decided_fields_and_cells | 96 |
| used_by_rows | 96 |
| relationships | 121 |
| internal_relationships | 94 |
| external_relationships | 27 |
| internal_use_pairs | 94 |
| external_use_pairs | 27 |
| used_by_continuation_rows | 27 |
| incoming_continuation_rows | 1 |
| plain_gates | 0 |
| step_cards_with_empty_together | 0 |
| explicit_step_cards_checked | 38 |
| unique_citations | 15 |
| resolved_citations | 15 |
| named_source_paths_checked | 145 |
| source_identities | 7 |
| whole_read_files | 1 |
| earlier_identities | 23 |
| pending_source_paths | 83 |
| built_field_lines | 0 |
| misfiled_scan_fields | 534 |
| misfiled_scan_used_by_cells | 288 |
| empty_restriction_failure_gate_boxes | 24 |
| formula_hits | 0 |
| wording_hits | 2 |
| wording_verbatim_exceptions | 2 |
| wording_actionable_hits | 0 |
| project_workflow_hits | 0 |
| path_use_rows | 1 |
| path_covered_cards | 54 |
| subpart_references_checked | 53 |
| v10_heading_rows_checked | 107 |
| read_folder_files_covered | 145 |
| source_names_checked | 17 |
| errors | 0 |
| additional_undecided_slots | 7 |
| explicit_source_conflict_records | 2 |

The complete cards and all relationship cells were reviewed against the source map, including every empty restriction, failure and gate box. Actual confirmation, authorization, integration, endpoint verification, kind selection and retry conditions appear as gates. Identity derivation, staging recovery and record steps name their rules. Empty log-storage failure boxes do not invent an unspecified write-failure mechanism. No plain TOGETHER gate remains. Source identifiers, the proposed relationship_operation_id qualifier, frozen status, exact retry values and the two explicit disagreements were checked.

Two source-verbatim wording exceptions remain in inherited coverage: the A29 closure filename has a space before its extension, and V10 heading 15 contains the literal dot-prefixed cursorrules name. No actionable wording flags remain.

All 23 earlier completed fingerprints were rechecked and are listed in full. The final count table is compared against a recount after this block is appended. No earlier chapter, repository source or runtime code is changed.
