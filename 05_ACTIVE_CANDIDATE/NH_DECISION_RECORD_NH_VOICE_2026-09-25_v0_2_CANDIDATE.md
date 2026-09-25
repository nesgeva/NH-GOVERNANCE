CANDIDATE — decision record — not a design — no integration, no implementation.

# NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md

## 0. Identity and three statuses, kept apart

- **File:** `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md`
- **Version note:** v0_2 is a bounded correction of v0_1 (SHA-256 `068516d72c650b969b0fdfcefc128d3f30eec6f40d691e61e4cfb53f789be147`, 12,032 bytes, 96 lines, preserved unchanged), made 2026-09-25 on ChatGPT's audit instruction. Two substantive changes only, both in §5: (1) the B29 bullet's closing "All remain open" is replaced by a bounded statement of what stays open and what this record does not settle; (2) the first preserved-boundary bullet's blanket "has no role" statement is replaced by a statement of distinctness that names what the voice selection does not change. All decisions, values, findings, source attribution, history, and remaining boundaries are unchanged.
- **Repository:** `nesgeva/NH-GOVERNANCE`, branch `main`. **Commit inspected:** `80f7573de5ca9adc24e5d7b1652b4240e06cda78` (HEAD at the time of writing; no later commit).
- **The decision:** made by **Ness on 2026-09-25**, through listening tests on his own machine. Its wording and the reported tests come from **Ness's direct statement of 2026-09-25, supplied in the ChatGPT-prepared task instruction of the same date**. No transcript, quotation, timestamp, test log, recording, artifact hash, or independent reproduction exists in this repository for those tests, and none is invented here.
- **This document:** a candidate decision record, created by Claude from that instruction. **Awaiting ChatGPT's independent audit.** Not audited, not accepted, not adopted, not package-complete.
- **Integration and build status inside N.H:** none. This record performs no Master or Map integration and claims no implementation, installation, export, synthesis, or configuration inside N.H.

Ness's choices below are his; they are not assistant proposals and he is not asked to decide them again.

## 1. Authority and sources read

**Authority order (unchanged):**
1. `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
2. `01_AUTHORITATIVE/NH_DECISION_DEFAULTS-S19_v2_2.md`
3. `01_AUTHORITATIVE/cursorrules`
4. `01_AUTHORITATIVE/NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`
5. `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`, subordinate.

Master V10 governs conflicts. Older Master references preserved inside the Defaults or the Companion do not replace V10. Only Ness decides acceptance, adoption, and permission to build.

**Read first, as navigation only (not edited; unrelated status discrepancies not resolved):** `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md` — rows NHD-A15 and NHD-BINT7 located; no row records a spoken-voice selection for N.H; no later record in `04`/`05` at the inspected commit records this decision.

**Passages read and cited below:**
- Master V10 §0 (the premise), §0B (full-transparency and living-record law), §2 (how to work with Ness); §9 "Recovered voice input/output pipeline" (line "Confirmed elements … Missing …"); §16 (local-first decision); §25 (voice security and identity system, `voice_interrupt_of_nh`); §26 ("Voice priority rule").
- Map: C-9 card; A21 entry; B29 entry.
- `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md` — §2 (Ness's decisions of 2026-09-23, incl. the scope paragraph), §3, §5, and its preserved v0_1 baseline (Part 1). **An inactive intent record is not an adopted design;** it is cited here only for what it records.
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` (the approved concept) and `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md` §1, §4 with its acceptance receipt `…_ACCEPTANCE_RECORD_v1_0.md`.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_A15_BOP_ACOUSTIC_CONDITION_NOTES_AMENDMENT_POLICY_v1_1_CANDIDATE.md` with closure record v1_0; `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md` with closure record v1_0 — read for their boundaries, which this record leaves intact.

No governance source is cited as evidence for any listening result (§4): governance documents set boundaries; they did not perform or establish these tests.

## 2. The decision — N.H's speech-output setup (Ness, 2026-09-25)

Recorded exactly as stated; every filename, spelling, and value preserved.

1. **Speech engine and checkpoint.** BlueTTS, repository `github.com/notmax123/BlueTTS`. The author's **untouched** text-to-latent checkpoint **`vf_estimetor.safetensors`**, exported to ONNX using the repository's `exports/export_onnx.py`. Reported local export folder: `onnx_author`. This identifies the chosen setup; it instructs no export.
2. **Spoken voice.** The shipped style file **`voices/daniel.json`**, used as **one voice for both Hebrew and English**.
3. **Synthesis settings.** **`total_step=32`**, **`cfg_scale=2.0`**. Separately recorded, as Ness's listening observation: 8 steps with `cfg_scale=4.0` produced audible distortion.
4. **Hebrew text input.** **`renikud-plus` pinned to `0.3.0`.** Reported compatibility reason: version `0.5.0` expects a `datastore.json` absent from the author's Hugging Face repository in the tested setup.
5. **English text input.** **`espeak-ng`** installed in the tested setup, with **`PHONEMIZER_ESPEAK_LIBRARY`** set to its `libespeak-ng.dll`. No absolute path and no installation version are recorded here.

## 3. Standing constraints preserved (earlier records + Ness's restatement of 2026-09-25)

| constraint | earlier record | Ness's restatement, 2026-09-25 |
|---|---|---|
| The same young-male voice in Hebrew and English | v0_1 baseline Part 1 §1–§2 ("a normal 20–24-year-old man"; "the same voice in English and in Hebrew"); v0_3 §2 item 3 ("a normal young adult male voice … one voice identity across English and Hebrew") | restated |
| Not Ness's own voice | v0_3 §2 item 4 ("not Ness's voice, not someone he knows, and not a paid speaker") | restated |
| No emotional pull | not found in the earlier voice records as such; recorded here on Ness's restatement only | restated |
| Local/offline runtime | v0_1 baseline Part 1 §4 ("run locally and offline. No cloud speech"); v0_3 §2 scope paragraph ("The offline-runtime requirement remains"); consistent with V10 §16 ("THE DECISION — LOCAL-FIRST. Sovereign, offline, private…") | carried; the chosen setup is a local ONNX export |

No new accent, age, delivery, or emotional-expression rule is added. The earlier accent and delivery decisions recorded in v0_3 §2 are neither restated nor changed here. The earlier reference-voice route recorded in v0_3 §2 items 5–9 (a library reference clip and a fine-tuning experiment) is **historical evidence**, not erased and not rewritten; for the chosen setup, the voice is now `voices/daniel.json` (§2 item 2). v0_3 as a whole is **not** blanket-superseded: its delivery-director intent, findings, open items, and tone-listener note stand as recorded.

## 4. Findings — evidence, not rules (Ness's tests and account of 2026-09-25)

- A fine-tune of the checkpoint on **4,605 clips** — **2,977 Hebrew clips from SASPEECH gold** and **1,638 English clips** — at learning rate **`2.5e-4` for 20,000 steps** degraded intelligibility and prosody in Ness's tests.
- The base model already speaks Hebrew via universal IPA, as reported in the test account.
- Fine-tuning is not needed for the chosen voice.
- If fine-tuning is ever revisited, the recorded direction is a **far gentler recipe, judged by ear at each checkpoint**. This authorizes no experiment and specifies no recipe.
- The distortion observation (§2 item 3) and the dependency-compatibility report (§2 item 4) are likewise Ness's tests and account of 2026-09-25.

These findings are not generalized: they do not establish a permanent prohibition on fine-tuning, a universal model limitation, or a proven causal diagnosis. Neither Claude nor ChatGPT heard, reproduced, or verified any of these results.

## 5. Scope, boundaries, and dependencies left unchanged

**What this record does:** records N.H's selected speech-output setup (§2) and the constraints it satisfies (§3).

**What it does not do:**
- It does not complete **B29** — the voice-pipeline mechanical owner. V10 §9 lists the confirmed elements (microphone capture; audio cleanup; transcription; sensor/front-door handoff; Hebrew speech output; English speech output) and the missing ones (exact pipeline architecture, model selection, latency requirements, error handling); the Map's B29 entry lists the undesigned mechanics (capture → cleanup → transcription → handoff → Hebrew-and-English speech output → TTS interruption → latency → error/fallback, with operation identity, logging, crash behavior, duplicate prevention). The remaining pipeline mechanics stay open where not already settled by accepted sources. This record captures the speech-output choices in §2; it does not settle A21's separate language-model choices or complete B29.
- It does not settle **A21** — the final Interactive Translator model, which V10 §9 marks UNDECIDED and the Map's A21 entry reserves — nor the heavy/light language-model choices, which the accepted placement-and-dependency record §4 leaves open ("no model is selected, made eligible, installed, or adopted by this record"; "A21 and B29 remain the relevant Bundle 7 owners"). Selecting a speech synthesizer is not selecting a language model.
- It does not complete the **delivery director** (v0_3 §5: model, owner, interface and control support remain open) and does not close **Bundle 7 or Bundle 8** work.
- It does not change **V10 §9 voice I/O** or any accepted package. **A15** (BOP acoustic condition-notes amendment policy) and **B-INT-7** (initial Ness voice-profile enrollment bootstrap wiring) keep their boundaries exactly; v0_3 §5 already records that B-INT-7 belongs to Bundle 5 and interfaces B29 without completing it.

**Boundaries preserved:**
- **N.H's synthetic speaking voice is distinct from Ness's identity or enrollment voice profile.** Selecting `voices/daniel.json` does not change speaker identity assessment, access control, B-INT-7 enrollment, A15 acoustic-condition notes, or the existing rules governing physical observation of N.H's output (V10 §25).
- **Voice priority stands:** "When Ness speaks, N.H TTS stops immediately," enforced by OOP and recorded as `voice_interrupt_of_nh` when it occurs (V10 §26; V10 §25; Map B29). The chosen synthesizer is subject to that rule; nothing here relaxes it.
- Privacy, authorization, and meaning-preservation boundaries (V10 §0, §0B; the approved live dual-model handoff concept and its accepted placement record) are unchanged. The chosen setup runs locally; it introduces no cloud speech call (§3, offline row).

**Prohibited work not performed:** no design, mechanism, architecture, schema, wiring, fallback, latency target, scheduling, playback-timing rule, or training plan; no code or commands for building, installation, export, synthesis, fine-tuning, configuration, or tests; no edits to existing files (authority files, accepted packages, the Map, the decision index, earlier voice records, Master-21 material); no new or renamed controlled IDs, receipts, manifests, or companion files; no production-store, seal, gate, credential, legacy-layer, or live N.H changes.

## 6. No-loss and verification statement

- Destination checked before writing: `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_1_CANDIDATE.md` did not exist at commit `80f7573de5ca9adc24e5d7b1652b4240e06cda78`; no collision.
- This task adds exactly one file. No existing file is edited, overwritten, moved, renamed, reformatted, or deleted; all pre-existing files and unrelated working-tree changes are preserved.
- All five choices (§2) and every finding (§4) are present with unchanged values and spellings, including `vf_estimetor.safetensors`, `onnx_author`, `voices/daniel.json`, `total_step=32`, `cfg_scale=2.0`, `renikud-plus` `0.3.0` / `0.5.0`, `datastore.json`, `espeak-ng`, `PHONEMIZER_ESPEAK_LIBRARY`, `libespeak-ng.dll`, 4,605 / 2,977 / 1,638, `2.5e-4`, 20,000.
- Decision (Ness, 2026-09-25), reported evidence (Ness's tests and account), document status (candidate, awaiting audit), and N.H implementation status (none) are stated separately (§0, §4).
- Citations were checked against the cited passages at the inspected commit; "no emotional pull" is deliberately not attributed to any earlier record (§3).
- No invented decision, implementation claim, or dependency-closure claim. Not committed, not pushed.

**Status: DELIVERED — AWAITING CHATGPT INDEPENDENT AUDIT.**

*End of record v0_2.*
