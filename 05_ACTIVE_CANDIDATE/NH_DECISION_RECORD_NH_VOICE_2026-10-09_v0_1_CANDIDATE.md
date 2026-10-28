# N.H voice — VoxCPM2 selection and local listening results

**Filename:** `NH_DECISION_RECORD_NH_VOICE_2026-10-09_v0_1_CANDIDATE.md`  
**Intended repository path:** `05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-10-09_v0_1_CANDIDATE.md`  
**Date:** 2026-10-09, Asia/Jerusalem  
**Owner of the choice:** Ness  
**Prepared by:** ChatGPT, at Ness's request  
**Document status:** CANDIDATE — decision and evidence record; not a completed speech-system design, not independently audited, not an accepted package, not Master/Map integration, and not authorization to build N.H.

## 1. What this record is for

Ness has now heard a local VoxCPM2 reader in English and Hebrew and wants that voice in N.H. This file preserves that choice, the tested setup and the remaining work, so the later N.H design can use the actual successful result.

The choice and this document's status are separate: Ness made the voice choice in the conversation; this is a candidate record of it. Review of this file checks whether that choice and the evidence were recorded faithfully. It does not ask Ness to choose the voice again.

A **decision record** is more fitting than an undecided feature intent because Ness has already selected a concrete speaking setup after listening. The existing placement precedent is the 2026-09-25 voice decision record in `05_ACTIVE_CANDIDATE/`. The wider delivery-director and read-aloud ideas remain in their existing intent files. Folder placement by itself confers no acceptance or authority. [R3–R6]

**Design stage preserved.** Ness clarified: “I don't build it until I'm done with designing everything.” The standalone reader used for listening is an experiment outside N.H. Its existence proves neither that N.H has been built nor that this record authorizes building it.

## 2. Repository and authority check

Repository inspected: `nesgeva/NH-GOVERNANCE`, branch `main`, commit **`f422465af0635ca3909581102a232b401cb7db1d`**. The branch head was rechecked for this task. Its complete returned tree was not truncated. The proposed destination filename does not exist at that commit; a repository search for `VoxCPM` returned no results.

The repository separates authoritative material (`01_AUTHORITATIVE/`), the subordinate working Map (`02_WORKING_MAP/`), workflow records (`03_WORKFLOW/`), accepted standalone designs (`04_ACCEPTED_STANDALONE_DESIGNS/`), active candidates (`05_ACTIVE_CANDIDATE/`), inactive intents (`05_INACTIVE_CANDIDATE/`), operational instructions, tools and preserved historical material. This record belongs with the active voice decision record, not among the authoritative or accepted files.

**Current authority is Master-21.** Its adoption record explicitly makes it the authoritative Master in place of V10, despite preserved `CANDIDATE` wording inside the adopted book and chapters. The order is Master-21 → adopted Decision Defaults S19 v2_2 → `cursorrules` → Companion v1; the Working Map remains subordinate and the decision index is navigation. Older V10 authority statements in the voice record, Map, route and project instructions are historical wording, not a reversal of Master-21's adoption. [R1]

Master-21 adoption leaves `NOT DECIDED` entries unresolved and does not authorize building. The recorded route remains gap decisions → finished system description → separately authorized building. This file supplies evidence and a later Ness choice for that route; it does not become a second gap-decisions register. [R1, R7]

The review was focused on repository structure, authority, voice selection, speech-output cards, related intents and connected output boundaries. It was **not** a complete audit of every Master-21 chapter or of the entire N.H design.

## 3. Ness's choice and listening evidence

### 3.1 The choice to carry into N.H's design

Use **VoxCPM2 with the reference recording and language-specific settings identified in §4** as the selected speaking setup for N.H's future English and Hebrew output. Preserve this successful baseline for comparison during later speed and integration work.

This records the voice and speech-engine choice. It does not select N.H's heavy or light conversational language model, design its microphone/transcription system, or settle its final hardware allocation.

### 3.2 Ness's words on 2026-10-09

| Subject | Evidence from this conversation |
|---|---|
| Local English result | “the rythem is perfect, the sound is perfect.” |
| Local Hebrew result | “The Hebrew is perfect, the same sound. It sound the same, somehow with a different voice, but it's very close.” |
| Intended use | Ness asked for this voice in his personal app, supplied the N.H repository, and said: “I want this voice to be in it.” |
| Build stage | “I don't build it until I'm done with designing everything.” |
| This deliverable | Ness asked for one file to place in the appropriate repository location, after examining GitHub's structure, and allowed the fitting record type to be selected. |

These are **Ness's listening judgments and instructions**, not ChatGPT's independent auditory findings. The Hebrew statement deliberately retains his qualification that the voice is slightly different but very close. It must not be rewritten as a measured, exact identity match between languages.

The English and Hebrew demo trials preceded the local reader trial. The selection here rests on Ness subsequently hearing **both languages locally**. The source record is this conversation and its supplied setup output/screenshot; those materials have not been added to GitHub by this task.

### 3.3 What the available evidence establishes

- Ness's pasted setup output reports successful installation, a completed model download, successful imports and decoding of the original MP3 at about 10.9 seconds, followed by `Ready`.
- The reader screenshot shows `Generating English, part 1/1` at **2:31 elapsed**. This establishes a substantial generation delay during that run. It is not a completed-run timing, a loading-time measurement or a real-time performance benchmark.
- Ness then reported the successful local English and Hebrew listening results quoted above.
- The distributed reader's source and the original reference bytes were inspected for this record. The setup transcript supplies the installed source version and downloaded model revision in §4.
- The successful local output WAVs and their accompanying per-reading JSON files have **not** been supplied to ChatGPT. Their exact filenames, hashes, random seeds, final generation times and waveform measurements are therefore not invented here.

## 4. Exact baseline to preserve

This section identifies the **distributed reader configuration used for the reported tests**. ChatGPT has not directly inspected the installed files on Ness's PC or independently reproduced its speech. These values preserve the known baseline; they are not a permanent N.H hardware, scheduling or runtime-interface design.

### 4.1 Engine and reference identity

| Item | Recorded identity and evidence |
|---|---|
| Speech model | `openbmb/VoxCPM2` |
| Downloaded model revision | `32279effe8c19989596f05d353d1447f51d9e915` — printed in Ness's successful setup output |
| Official source | `OpenBMB/VoxCPM`, commit `cce58a5b59303c9bd63d12f23afe6a49a4a80c59` |
| Installed package reported by setup | `voxcpm-2.0.3.post43+gcce58a5b5` |
| Original reference upload | `2026-10-09 17-35-35.mp3`, **176,283 bytes** |
| Reference in the reader | `reference_original.mp3` — byte-identical to that upload; full recording, including its original silence, not a trimmed or softened derivative |
| Reference SHA-256 | `0798ca3e4f9f0ae5bf3a3162b0e887d17cb38fd367c1148931f9f8251d66b51b` |
| Reader package | `VoxCPM2_Reader_v1.zip`, **174,358 bytes** |
| Reader ZIP SHA-256 | `0054655dd3b72fa3742581c1f848c62580bdcf7576b08735e9e18dbae1bb473c` |
| Test installation | Windows, private Python 3.12 environment; setup reports PyTorch and torchaudio `2.8.0+cpu` |
| CPU precision in the supplied setup | Private local model configuration set to `float32`; original downloaded configuration preserved separately; model weights not fine-tuned |

The reference is identified by its exact bytes. Its transcript is not proof of a speaker's legal identity, and the file must not be relabeled as the earlier Ryan reference simply because that recording appears in older voice history.

The voice package and audio remain separate artifacts; this Markdown file contains their identities, not their bytes. They are not claimed to be stored in NH-GOVERNANCE. The reader package preserves the supplied code and reference; the successful WAVs on Ness's PC are the listening comparison material. A fresh setup can fetch a later model revision, so later work must use the recorded revision when reproducing this baseline.

### 4.2 Language-specific synthesis settings

“Ultimate Cloning” is the online demo's label. The local reader implements the corresponding argument combinations below; it does not call the online demo.

| Setting | English | Hebrew |
|---|---|---|
| Ultimate Cloning equivalent | On | Off |
| `reference_wav_path` | `reference_original.mp3` | The same `reference_original.mp3` |
| `prompt_wav_path` | The same reference file | Omitted |
| `prompt_text` | Reference transcript below | Omitted |
| `cfg_value` | `2.0` | `2.0` |
| `inference_timesteps` | `10` | `10` |
| `normalize` | `False` | `False` |
| `denoise` | `False` | `False` |
| Control/style instruction | None | None |

The English transcript shipped in `reference_transcript.txt` is:

> Today I'm Tom, this is a quick sample of my voice, easygoing, warm and perfect for natural conversations.

It was copied from the demo's automatic transcription. It has **not** been independently verified word for word. The reader lets Ness edit it; no edit was reported in this conversation. Hebrew uses no transcript. The reference transcript is conditioning material, not extra text to add to N.H's answer.

The supplied worker loads local model files with `device="cpu"`, `local_files_only=True`, `load_denoiser=False` and `optimize=False`. It sets Hugging Face and Transformers offline flags. Model/library acquisition used the internet; the local generation path contains no cloud speech-service call. An air-gapped cold-start/network-isolation test was not performed, so this is not an independent offline-certification claim.

No fixed random seed is selected by the reader. The worker uses the engine's ordinary retry defaults; those are not adopted N.H failure/retry policy. The local engine's ten inference steps must not be confused with the old BlueTTS setting of 32 steps. The online demo's backend step count was not established.

No pitch, pace or voice filter is added. The reader writes PCM-16 WAV at the model's reported sample rate; its code reduces level only if the peak exceeds 1.0, using a gain of `0.98 / peak`. Whether that reduction occurred in either successful reading is unknown without the corresponding output JSON. Changing runtime precision, reference bytes or synthesis settings later may change the sound and needs comparison with the successful baseline.

### 4.3 Supplied short listening texts

The reader's test buttons contain these texts. The completed output files have not been collected to independently verify each spoken word.

**English:** Good evening. This is a short test of the voice in English, with a longer sentence so we can hear the rhythm.

**Hebrew:** שלום, טוב לשמוע ממך. איך עבר עליך היום? בוא נעבור על הדברים יחד, צעד אחר צעד.

## 5. Relationship to the earlier choice and to Master-21

The September record selected BlueTTS, `voices/daniel.json`, its ONNX checkpoint and its associated synthesis and text-input dependencies. Today's selection carries **VoxCPM2 plus the current reference** forward instead. It does not transplant BlueTTS's 32-step parameter, `renikud-plus` or `espeak-ng` requirements into VoxCPM2. The old choice and all earlier test findings remain history; the old files are neither overwritten nor erased. [R3]

The change is bounded to the speaking setup. It does not blanket-supersede the older record's standing constraints, the delivery-director intent, or unrelated decisions. Earlier records retain the young adult male / one bilingual voice goal, private non-commercial use, offline-runtime direction, American-English preference and acceptance of a foreign accent in Hebrew, the recorded reference-voice constraints and the no-emotional-pull constraint. This file reports Ness's approval of the new listening result without claiming that every general constraint has received an independent technical verification. [R3, R4]

| Existing location | Connection to this record | Effect now |
|---|---|---|
| Master-21 **C-9.2.11 — Recorded speech-output setup** | Existing home for the synthesizer/voice selection | This record provides a later Ness choice for the normal design-consolidation route; the adopted chapter is not edited. |
| **C-9.2.11.1–C-9.2.11.6** | Engine/checkpoint, shared voice, synthesis values and language-specific inputs | Later consolidation must carry the VoxCPM2 baseline into these subjects and explicitly reconcile the old BlueTTS-specific details. This file renames no controlled IDs and writes no replacement cards. |
| **C-9.2.11.7–C-9.2.11.8** | Standing voice constraints; separation of speech from language-model choice | Preserve their boundaries. Choosing a synthesizer does not choose the Interactive Translator or heavy/light language models. |
| **C-9.2.5 / C-9.2.6** | Hebrew and English speech output | Both are consumers of the selected voice setup; their output gates and interruption obligations still apply. |
| **C-9.2.13 / B29** | Remaining voice-pipeline work | The selection supplies a tested speech-output starting point. It does not close architecture, latency, error/fallback, operation records or recovery work. |
| **C-OOP.7** | Immediate stop when Ness begins speaking | Remains a requirement on the eventual N.H connection. A manual Stop button in the test reader does not implement it. |

These are links to existing owners, not newly invented components. [R2, R8]

## 6. Boundaries for later design work

1. **Use N.H's existing output path.** Hebrew and English speech remain subject to the ordered privacy-first, SACL-second checks on the same immutable output version, with current authorization/fence revalidation. The selected synthesizer supplies no independent permission to speak and creates no second route around that chain. [R2, R9]
2. **Preserve the approved words and meaning.** Voice styling is delivery, not a new source of assertions or a second answer writer. The existing delivery-director intent's “how, never what” boundary is preserved; this record does not claim that its controller, interface or expressive controls have been designed or tested. [R4, R10]
3. **Keep interruption and observation distinct.** Ness beginning to speak must stop active N.H TTS immediately. Its physical interruption event is separate from a claim about what Ness heard or understood. The exact adapter, buffering, cancellation and recovery mechanics are not supplied here. [R8]
4. **Keep speaking voice separate from identity.** N.H's generated voice is not Ness's identity/enrollment profile and does not change SIA, SACL, BAI, B-INT-7 or A15 authority. The existing distinction already appears in the earlier speech-selection record. [R3 §5]
5. **Carry related feature intents forward in their own scope.** The existing read-aloud record captures choosing a start point, repeating according to Ness's meaning, and visible text in a side voice box. The multi-chat and voice-command records retain their own open design questions. Selecting this voice neither implements them nor resolves the still-open “when to offer to continue” behavior. [R5, R6]
6. **Do not adopt the test reader's incidental behavior as N.H design.** Clipboard input, automatic language detection, 360-character grouping, generating and playing parts sequentially, saving WAV/text JSON files, replaying the last part, and unloading the model on Stop are test-program choices. They do not settle N.H's interface, storage/retention, speech scheduling, language switching, full-answer buffering, streaming or unplayed-remainder policy. Existing undecided/proposed matters retain their actual status. [R7, R11]

## 7. What is still unfinished

| Subject | Current evidence / state | What later work needs |
|---|---|---|
| Voice quality | Ness approved the local English result and the local Hebrew result, with the Hebrew qualification preserved in §3. | Preserve the reference/settings and compare any changed setup against the successful samples. This is not a claim of universal pronunciation accuracy. |
| Generation speed | The CPU screenshot was still generating at 2:31; Ness found the delay too long. | Measure a practical local runtime alongside the other N.H models. No latency target or successful acceleration is established by this record. |
| GPU/resource allocation | No GPU version of this reader was installed or tested in this session; requested GPU diagnostics were not supplied before the design-record task. | Decide the allocation through the existing resource/design work using measurements. This file commits neither NVIDIA nor Intel Arc to speech and requires no purchase. |
| Real N.H connection | The standalone reader ran; N.H remains in design. | Complete the relevant B29/output-channel design and later perform the separately authorized build. No code, service interface or runtime transport is selected here. |
| Automatic interruption | The test program has manual Stop; no microphone-triggered N.H interruption was demonstrated. | Connect the existing C-OOP.7 requirement through the actual speech/output owners when that work is authorized. |
| Broader speech behavior | Two local language samples were judged; no comprehensive mixed-language, long-text or numerical-pronunciation evaluation is claimed. | Check the actual use cases needed by the eventual design, without treating this record as a passed full-system test. |
| Playback, remainder and repeat | Existing rules and intent answers coexist with remaining open mechanics. | Follow the existing cumulative decision route; do not infer final policy from how this temporary reader plays or saves files. |

No numerical “fast enough” target, automatic cloud fallback, new retry rule, storage policy, delivery-director mechanism, microphone design or N.H model-adoption gate is decided by this file. B29 and the wider speech system are not declared complete.

## 8. Placement and later incorporation

Place this single new file at the intended path in the header. Preserve the earlier dated voice record and all intent files in their current locations; this task does not instruct a move or deletion.

During the normal N.H design work, use this record as the source for Ness's later voice choice and its listening evidence, linked to the existing C-9.2.11 family. Any incorporation into the cumulative gap-decisions record, a future Master or Map version, or the decision index remains a separate versioned action under the established route. This file is not itself that incorporation and allocates no new NHD, FR, component or path identifier. [R1, R7, R11]

**Work performed for this deliverable:** read-only GitHub inspection, inspection/hashing of the existing local test materials, and creation/checking of this one Markdown deliverable. No repository write or commit, N.H source change, Master/Map edit, model installation, synthesis run, new speech code or production-store operation was performed for this task. No independent audit or formal acceptance of this new record is claimed.

## 9. Source references and evidence limits

Repository links below are pinned to the inspected commit. Internal historical headers in source files retain their original wording; current authority comes from R1. The source coverage was targeted to the sections named here.

- **R1 — Current authority and build stage:** [Master-21 adoption record, §§1–5](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/01_AUTHORITATIVE/NH_MASTER-21_ADOPTION_RECORD_v1_0.md). It records the adopted joined book SHA-256 as `8d7c929c5715bb8138644f2a0a7513a89e4f98d98c6f0f05e068284f4cc5ed0d`; that full book was not independently re-hashed for this task.
- **R2 — Existing speech-output locations:** [Adopted Master-21, CH09-i](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH09-i.md), especially C-9.2, C-9.2.5–7, C-9.2.11 and its child cards, C-9.2.13. The relevant cards were inspected; this is not a claim to have audited every card in the chapter.
- **R3 — Prior voice selection and placement precedent:** [2026-09-25 voice decision record v0_2, §§0–5](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_ACTIVE_CANDIDATE/NH_DECISION_RECORD_NH_VOICE_2026-09-25_v0_2_CANDIDATE.md). Its candidate/awaiting-audit status is preserved; this task grants it no new acceptance.
- **R4 — Earlier preferences and delivery-director scope:** [Voice and Delivery Director intent v0_3, §§2–5 and preserved baseline Part 4](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md). This remains an intent record, not an adopted director design.
- **R5 — Read-aloud choices:** [Read-Aloud Start-Point intent v0_3, §§1–5](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_INACTIVE_CANDIDATE/NH_READ_ALOUD_START_POINT_INTENT_v0_3.md), including the recorded 2026-10-05 answers and still-open continuation condition.
- **R6 — Related interface/command intents:** [Multi-Chat Interface intent v0_1](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_INACTIVE_CANDIDATE/NH_MULTI_CHAT_INTERFACE_INTENT_v0_1.md) and [Voice Commands intent v0_2](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_INACTIVE_CANDIDATE/NH_VOICE_COMMANDS_INTENT_v0_2.md). Their related ideas and unresolved questions are not converted into completed design here.
- **R7 — Recording/consolidation route:** [Master-21 to Finished System Description route v0_2, §§2–4](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/03_WORKFLOW/NH_MASTER-21_TO_FINAL_SYSTEM_DESCRIPTION_ROUTE_v0_2_CANDIDATE.md), read with R1's later adoption record; and the attached decision-triage rule v0_3, whose adoption is recorded by R1. No new gap answer was derived or batch-approved by this task.
- **R8 — Voice interruption and mechanical owner:** [Adopted Master-21, CH08-e, C-OOP.7](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/01_AUTHORITATIVE/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1/NH_MASTER-21_SYSTEM_BEHAVIOR_v0_1_CANDIDATE__CH08-e.md); [Working Map v1_6, C-9 and B29](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md). The Map remains subordinate.
- **R9 — Existing output gates:** [B-INT-6 wiring v1_3, §4](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_v1_3_CANDIDATE.md), with its [receipt, §§2–7](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_6_PRIVACY_FIRST_SACL_SECOND_OUTPUT_CHAIN_WIRING_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md). The receipt records Ness's source acceptance and distinguishes it from its own pending formal-closure audit. This record makes no new closure ruling.
- **R10 — Language-model/meaning boundary:** the attached `NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md`, §§1–3 and §§6–8. Its approved concept is distinct from speech synthesis and leaves hardware/resource mechanics and model choices to their own work.
- **R11 — Navigation only:** [Decision index v0_11, F.2 V-NEW-1–7](https://github.com/nesgeva/NH-GOVERNANCE/blob/f422465af0635ca3909581102a232b401cb7db1d/05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_11_CANDIDATE.md). The voice ideas are kept at their recorded proposal/summary status; later direct answers in R5 are preserved rather than erased by older index wording.

Operational instructions and the relevant authority, version-safety and file-protection passages of the Defaults, `cursorrules` and Companion were checked for scope. No unrelated discrepancy was resolved.

**Local evidence inspected:** the delivered `VoxCPM2_Reader_v1.zip` and its `reader_common.py`, `setup_reader.py`, `voice_worker.py`, `reader.py` and `reference_transcript.txt`; the original reference MP3; Ness's supplied `Pasted text(20261009-154722).txt` setup output; and the earlier inspected `image(20261009-155211).png` generation screenshot. The reference and ZIP hashes in §4 were recalculated for this record. The user reports, source configuration, installer output and screenshot are different kinds of evidence and are not presented as interchangeable.

*End of candidate record. Ness's selected voice is recorded; N.H design completion, formal incorporation, performance validation and building remain separate.*
