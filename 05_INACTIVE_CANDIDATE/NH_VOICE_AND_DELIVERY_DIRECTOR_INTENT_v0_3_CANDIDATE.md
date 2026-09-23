# NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md

## Status

- **Class:** Intent capture — INACTIVE CANDIDATE. Not a design. Not adopted.
  Decides nothing new. Authorizes no implementation. Selects no model for
  N.H. Records Ness's decisions, changes to earlier choices, and an isolated
  experimental build snapshot.
- **Package:** `NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT`, version 0.3.
- **Version note (v0_3, 2026-09-24):** v0_2 (SHA-256
  `95a7877808edb481463f1ba15540e9c29f9a313b2b034794382b9e6396643dd8`,
  32,473 bytes, 505 lines) plus **four bounded documentation corrections**
  under ChatGPT's correction instruction of 2026-09-24: (1) consistent
  evidence labels in §4 and §8 — supplied-but-unverified scripts separated
  from run-verified files; (2) the blanket "no checkpoint, stats file, or
  trained weights exist" replaced by the supported statement; (3) the
  anti-clipping workaround connected to the unchanged content-preservation
  rule and marked an experimental limitation; (4) §2 item 10 moved out of
  the confirmed-decision list with its source stated. One evidence update
  added in §8 (English conversion result now on screen), flagged in §10.
  No decision, historical material, reported progress, or open dependency
  was removed. v0_1 remains embedded byte-identical in §A; v0_1 and v0_2
  are untouched.
- **Concept and decision owner:** Ness (Register A). No numbered Register-A
  item and no new controlled package ID is created by this file.
- **Existing mechanical Register ID touched:** **B29 — voice pipeline,
  Bundle 7** — only to record early speech-output work done ahead of its
  bundle. **B29 remains open.**
- **Origin:** Stated by Ness during the 2026-09-23 evening session (direct
  build loop, Claude as worker); v0_2 drafted by Claude under ChatGPT's exact
  task-entry instruction of 2026-09-23; v0_3 drafted by Claude on 2026-09-24
  under ChatGPT's bounded correction instruction. No independent ChatGPT
  audit of v0_3 has occurred.
- **Intended folder:** `05_INACTIVE_CANDIDATE/`
- **Authority:** Subordinate to `01_AUTHORITATIVE/NH_MASTER-20_CORRECTED_v10.md`
  and the full authority order (Master V10 → `NH_DECISION_DEFAULTS-S19_v2_2.md`
  → `cursorrules` → `NH_PROJECT_COMPANION_GOVERNANCE_AND_ARCHIVE_v1.md`).
  Nothing here overrides, reopens, or modifies any accepted design, seal,
  store, or decision.
- **Relation to v0_1:** v0_1 is preserved **verbatim and unabridged** in
  §A (historical baseline) below. Everything outside §A is the v0.2 addendum
  as corrected in v0.3.
  Nothing in v0_1 is corrected, shortened, replaced, or deleted. Statements
  in v0_1 such as "none chosen" or "not decided, not designed, not built"
  describe the 2026-09-23 **daytime** snapshot; the addendum updates only the
  specific choices and experimental facts listed in §1–§4.
- **Recording a decision does not un-decide it.** Ness's decisions listed in
  §2 are his decisions; this file records them. The file itself remains
  unadopted.

## 0. Reading record (what was actually read)

- Repository: `nesgeva/NH-GOVERNANCE`, branch `main`, commit
  `280f20ab98aa887d71ec7f55f557ece9dc98b17c` (2026-09-23 23:24 +03:00,
  "Record B24 rejection-category decision (P8-U10) v0_1"), cloned fresh for
  this task.
- Baseline: `05_INACTIVE_CANDIDATE/NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`
  — read in full; Git blob `91a0439f1457e1bb6fca320f0143bff779a53da8`;
  SHA-256 `361e8f6904c852777d8d670179cd825d21e70ac58aa0b596b3f73e6bab05c858`;
  114 lines; 6,036 bytes. Matches the baseline Ness supplied (commit
  `07505fb`).
- Navigation: `05_ACTIVE_CANDIDATE/NH_DECISION_INDEX_PROPOSAL_v0_10_CANDIDATE.md`
  (SHA-256 prefix `aafc7abe6522`) — Part F (voice interruption settled vs
  new), F.2 V-NEW-1…7 (`assistant_summary` / `assistant_proposal`, not
  Ness-recorded decisions), NHD-M26-VP, NHD-M25-BOP-VI, NHD-BINT7.
- Map: `02_WORKING_MAP/NH_COMPLETE_DESIGN_AND_WIRING_MAP_v1_6_CANDIDATE.md`
  (`33af648d9a1e`) — C-9 (voice I/O; voice pipeline → B29; A21 not chosen
  there), C-BOP and C-OOP voice-priority entries, Register B29, A21.
- Plan: `03_WORKFLOW/NH_REPLACEMENT_EIGHT_BUNDLE_DEPENDENCY_PLAN_v1_0_CANDIDATE.md`
  (`2d6483d133bb`) — Bundle 5 (B-INT-7), Bundle 7 (A21, B29), global
  execution rules 4, 6, 7, 10, 11, 12.
- Workflow: `03_WORKFLOW/NH_FULL_DESIGN_COMPLETION_WORKFLOW_v1_0.md` §§10–12.
- Instructions: `06_OPERATIONAL_INSTRUCTIONS/NH_CLAUDE_PROJECT_INSTRUCTIONS_v1_4_CANDIDATE.md`
  (`0bce604860cc`) — task-entry requirement, its [v1.4] scope note, evidence
  discipline, direct-build-loop section.
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_LIVE_DUAL_MODEL_HANDOFF_v1.md` —
  §§1–4 (Ness-approved standalone concept decision; not integrated into
  Master V10 or the Map).
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_LIVE_DUAL_MODEL_HANDOFF_BUNDLE_PLACEMENT_AND_DEPENDENCY_RECORD_v1_1_CANDIDATE.md`
  §4 and its `…_ACCEPTANCE_RECORD_v1_0.md` (Ness: "accepted", July 13, 2026).
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B_INT_7_INITIAL_NESS_VOICE_PROFILE_ENROLLMENT_BOOTSTRAP_WIRING_v1_1_CANDIDATE.md`
  §§7, 24, 25 and its `…_PACKAGE_COMPLETE_CLOSURE_RECORD_v1_0.md` §7 —
  B29 is interfaced, not completed.
- `04_ACCEPTED_STANDALONE_DESIGNS/NH_B24_VALIDATOR_FIRST_MODEL_BOUNDARY_AND_BENCHMARK_v7_CANDIDATE.md`
  — §5A warm live-conversation path, §6.5 output gates, messenger
  wording/warmth-only rule.
- `05_ACTIVE_CANDIDATE/NH_DECISION_PACKAGE_MODEL_CANDOR_AND_HONESTY_STACK_v1_CANDIDATE.md`
  (`05969d795b8b`) — status **CANDIDATE, not adopted**; §1.2 warmth is
  delivery-only; §4 Layer C language-model fine-tuning is an OPEN SLOT.
- Master V10 lines 5145–5147 (voice priority rule) read directly.
- Session evidence: Ness's 2026-09-23 evening-session statements;
  `NH_VOICE_PROJECT_FULL_RECORD_2026-09-23.md` (daytime session record);
  PowerShell transcripts from `C:\Users\user\voice_test` pasted by Ness
  during the evening session (disk evidence for §4).

Folder placement, the word "candidate" in a filename, and frozen status
paragraphs do not by themselves establish acceptance; the acceptance
evidence named above was followed.

## 1. Change table — 2026-09-23, evening session

| # | Earlier position (source) | Today's decision or new evidence | Scope of change | What remains unchanged |
|---|---|---|---|---|
| 1 | Hebrew must sound native Israeli (v0_1 Part 1 §3). | **A foreign accent in Hebrew is acceptable** (Ness, evening). | Relaxes v0_1 Part 1 §3 for the reference-voice choice. | Hebrew pronunciation itself must still be correct; one voice identity across both languages. |
| 2 | English accent: British, "not too strong but noticeable" (Ness's daytime session account — **not** stated in v0_1, which says nothing about English accent). | **American** (Ness, evening, after listening to British and American reference voices locally). | Replaces the daytime British preference. | One voice identity across both languages. |
| 3 | Voice source: Option A (Ness's own voice) or Option B (consenting friend/family); no actor, YouTuber, or product voice (v0_1 Part 3, "none chosen"). | Ness: **not his own voice, not someone he knows, not a paid speaker.** Reference chosen for this private experiment: ElevenLabs free-tier library voice **"Ryan - Product Reviewer."** Private, non-commercial use. | Selects a reference source for the isolated experiment, departing from v0_1 Part 3's exclusion. Ness was told of the terms concern once by Claude and made the choice himself. **This choice is not evidence of licensing permission or speaker consent**, and is recorded as Ness's decision with that provenance. | The clip is a *reference* for a local model; N.H runtime remains offline; no cloud speech during operation (v0_1 Part 1 §4, Boundaries). |
| 4 | Voice age/identity: normal 20–24-year-old man (v0_1 Part 1 §1). Daytime widening: a deeper voice is fine if not too calm and slow. | Unchanged as a goal. | — | Continues. |
| 5 | Delivery wants: warmth, good tone per sentence, liveliness (v0_1 Part 1 §5). | Unchanged; evening listening found the local model's delivery reads as "robotic / like an AI" in both languages (Ness's ears). | Adds a finding, not a decision. | The wants stand; the director idea (v0_1 Part 4) stands. |
| 6 | "Any real test starts from the newest explicitly licensed version"; V3 exists (v0_1 Part 2 note). | BlueV3 check **not done**. Local experiment uses the v2 ONNX bundle (`notmax123/blue-onnx-v2`) for cloning and the author's `blue-v2` PyTorch weights for the fine-tune start point. | Records the state; **no upgrade selected**. | v0_1's version note stands. |
| 7 | No training of any kind existed (v0_1 "Not decided, not designed, not built"). | Ness chose to **fine-tune BlueTTS** on real human speech in an isolated folder, to obtain conversational rather than read/synthetic delivery. Data chosen: **SASPEECH gold** (Hebrew) + **Emilia-YODAS EN chunk 0** (English). Preparation is in progress; training **not yet run**. | Adds an experiment and its data choices. | This does **not** adopt BlueTTS into N.H, does **not** choose the heavy or light language model (A21), and does **not** decide the candor package's separate language-model fine-tuning slot (Layer C). |
| 8 | ivrit.ai podcast corpus considered as training data (daytime session record §9). | **Shelved** by Ness after listening to samples ("too noisy and too stating"); not selected for renewed work. | Records the shelving. | The corpus and its license note remain in the daytime record. |
| 9 | Placement of the voice layer "not decided here" (v0_1 Status). | Placement already exists in accepted sources: the voice pipeline's mechanical owner is **B29**, listed under **Bundle 7** in the accepted eight-bundle plan; A21 (Interactive Translator model) is also Bundle 7. | v0_1's "not decided here" was correct for v0_1's scope; this row only points at the accepted placement. No placement is decided by this file. | B29 open; Bundle 7 not closed; bundle order unchanged. |

## 2. Ness's decisions — 2026-09-23, evening session (Register A; his, recorded)

1. **English accent: American.** Replaces the daytime British preference.
2. **Hebrew: a foreign accent is acceptable.** Relaxes v0_1 Part 1 §3.
3. **Continuing goal preserved:** a normal young adult male voice,
   approximately 20–24, with **one voice identity across English and
   Hebrew**.
4. **The reference voice is not Ness's voice, not someone he knows, and
   not a paid speaker.**
5. **Reference source for this private experiment:** ElevenLabs free-tier
   library voice **"Ryan - Product Reviewer"** (file on disk:
   `ElevenLabs_2026-09-23T19_30_57_Ryan - Product Reviewer_pvc_s50_m2.mp3`,
   in `voice_test\incoming\`).
6. **Intended use: private and non-commercial.**
7. **Provenance of decision 5:** Claude stated the terms-of-service concern
   once (a library voice licensed to the vendor is not the same as a
   consenting speaker; the vendor's terms restrict using outputs to build
   other voice models). Ness made the choice. The choice is recorded as
   his; it is **not** described here as proof of licensing permission or
   speaker consent. Ness is not asked to decide this again.
8. **Training data selected:** **SASPEECH gold** — Hebrew, approximately
   four hours, single speaker (Shaul Amsterdamski, who volunteered his
   voice), studio 44.1 kHz, manually corrected transcripts; described by
   its README and OpenSLR page as **non-commercial use only**, copyright
   IPBC. **Emilia-YODAS EN chunk 0** — English, in-the-wild speech,
   approximately four hours selected from 25,482 clips by the dataset's
   own quality score; described on its Hugging Face page as **CC-BY 4.0**.
   These license descriptions are attributed to the datasets' own pages
   as read during the session; **no independent legal verification was
   performed or is claimed.**
9. **Purpose of the fine-tuning experiment:** more conversational speech
   instead of the observed read/synthetic delivery style.
**Claude-reported, outside the confirmed-decision list (not in the evening
handoff instruction; not independently verified):** a working-style
statement — Ness schedules, Claude supplies facts and steps. Source:
`NH_VOICE_PROJECT_FULL_RECORD_2026-09-23.md` (daytime session record,
Claude-written, uploaded by Ness to the Claude project), §1 items 10–11,
which quote Ness: "I do not like it when you tell me what to do." That
record is not in the NH-GOVERNANCE repository. The statement is preserved
here as reported; Ness is not asked to restate it, and nothing here claims
it was not said.

**Scope of these decisions.** They concern the isolated speech experiment in
`voice_test`. They do not adopt BlueTTS into N.H, do not select the heavy or
light language model (A21 remains Ness's), and do not settle the candor
package's separate language-model fine-tuning question (Layer C, open slot).
The **offline-runtime requirement remains**: acquiring a reference clip from
an online library does not authorize any cloud speech call during N.H
operation.

## 3. Findings and listening observations (not decisions)

- **Reported diagnosis — why the model sounds like reading.** The BlueTTS
  repository's `training/docs/datasets.md` (read from the shallow clone in
  `voice_test\BlueTTS_repo`) states that its Hebrew training set,
  SententicDataTTS, is "audio generated with Chatterbox" and "audio generated
  with MamreTTS," resampled to 44.1 kHz and time-stretched (slowed); English
  came from LibriTTS audiobooks. The session identified this as the cause of
  the calm, read-like delivery heard in both languages. **Evidence:** the
  author's own dataset note supports the *training-data fact*; the
  *causal link* to the heard delivery is the session's reported diagnosis,
  not independently established causation.
- **Ear tests (Ness's judgment; Claude measured files but cannot hear).**
  ElevenLabs "James - Professional British Male" cloned locally: Hebrew
  "very good"; English did not come out British ("the British accent in the
  English is not shown"); higher `cfg_scale` (7, 9) made it loud and angry;
  lower (3, 4) made it weak or "less conversational"; a quieter reference
  level made it "a bit robotic." Ness then chose an American voice, and later
  "Ryan - Product Reviewer" as "the perfect one" on the vendor's site. Ness's
  standing observation of every local output: "it sounds a bit robotic, like
  a general AI" in both languages.
- **Session observation on `cfg_scale`:** in this setup, 4 sounded weak and 5
  forceful, and no satisfactory middle was found or reported. **This is an
  observation about this reference clip and this bundle; it is not
  generalized into a universal limitation of the model.**
- **Wording drives delivery:** with calmer, lighter sentences the same voice
  read as less "depressed" on the vendor's site; the test sentences are
  written in N.H's voice (helper, honest, no pressure) and are kept in the
  scripts on disk.
- **Accent leak, re-observed:** a clip in one language carries its accent
  into the other language's output (already noted in v0_1 Part 3). With
  today's decisions this leak is acceptable to Ness rather than a defect.

## 4. Experimental build snapshot — 2026-09-23, evening session

**Location:** `C:\Users\user\voice_test` (outside the engine repository).
**Classification:** *Early, isolated B29 / Bundle 7 speech-output foundation
work; unadopted and not integrated into N.H.*

Facts marked **[disk]** were seen in PowerShell output pasted by Ness during
the session; facts marked **[reported]** are the session's account.

- No engine-repository files were touched; all voice work is isolated in
  `voice_test`. **[reported; consistent with every pasted transcript]**
- BlueTTS v2 ONNX zero-shot cloning works from a ten-second reference clip
  via `blue_onnx.style.style_from_wav`. **[disk: `clone.py`, `final.py`,
  `sweep.py` runs printing `saved he` / `saved en` / `done`]**
- Settings for the chosen voice. **Verified by run [disk]:** `final.py`
  produced `cfg4.0_*`, `cfg4.5_*`, `cfg5.0_*` files (`total_step=16`,
  `speed=1.0`), and Ness judged 5.0 the usable one. **Intended by supplied
  code, unverified:** `cfg_scale=5.0`, `speed=1.0`, output volume `0.55`,
  bass `+5 dB @ 160 Hz` (ffmpeg `bass=g=5:f=160:w=0.7`) are the values
  written into the `say.py` code supplied to Ness; their operation was not
  demonstrated by any pasted run.
- `say.py` — **code supplied to Ness as a paste block; file creation and
  execution unverified [supplied, unverified].** As supplied, it is intended
  to give one-command synthesis in the selected voice
  (`.\blue_env\Scripts\python say.py "<sentence>"`), detect the language
  from the text, and — for Hebrew — **append the throwaway sentence "וזהו."
  to the synthesis input** as a workaround for end-of-sentence clipping.
  **Content-preservation boundary (unchanged rule; see §5):** approved words
  may not be added to or removed from. The supplied code appends a word to
  the input and, as written, plays the whole output file — so **if that
  addition reaches playback it changes the approved words and is
  incompatible with final N.H speech delivery.** Existing evidence does not
  show removal of the tail before playback; the supplied code contains no
  such removal. **Recorded as an experimental limitation of the
  `voice_test` scripts, not an authorized exception.** Its replacement is
  not designed or implemented here.
- Training environment `train_env`: Python 3.13, `torch 2.11.0+cu128`,
  `cuda True`, **NVIDIA GeForce RTX 2060, 12 GB**, driver 591.86; `bluecodec`
  from GitHub; `phonemizer`, `espeakng-loader`, `pyarrow`; **`pandas<3`
  pinned** for the author's `combine_datasets.py`. **[disk]**
- Author's PyTorch weights (`notmax123/blue-v2`: `blue_codec.safetensors`
  233.8 MB, `vf_estimetor.safetensors` 166.4 MB, `duration_predictor_final`,
  `stats_multilingual`) in `pt_models\`. **[disk]**
- Data on disk: `saspeech\saspeech_gold_standard\` (2,986 WAV, `metadata.csv`
  pipe-separated, README, terms PDF); `emilia\en0\` (25,482 MP3+JSON);
  `emilia\wavs\` (1,698 WAV, 44.1 kHz mono, filenames stamped
  `s<speaker_id>_…`); `emilia\metadata_spk.csv`; `train_config.json`
  (two datasets: SASPEECH speaker 1, `he`; Emilia 268 speakers via filename
  splits, `en`). **[disk]**
- Training table, as of drafting:
  - `train_data\combined.csv` — **4,684 rows: 2,986 Hebrew + 1,698 English,
    269 speakers** (1 Hebrew + 268 English). **[disk]**
  - `train_data\combined_raw.csv` — copy of the above before Hebrew
    conversion. **[disk]**
  - Hebrew rows converted to IPA with **the same RenikudPlus G2P the
    inference path uses** (`blue_onnx.TextProcessor(...).phonemize(text,
    lang="he")` + `strip_lang_tags_from_phoneme_string`), with the
    `datastore=None` workaround because `datastore.json` is missing upstream;
    2,986 lines converted; sample `ʃalˈom, tslˈil ʔavʁahˈam.` **[disk]**
  - Author's cleaner (`combine_datasets.py --skip-combine`) then kept
    **4,615 rows** (2,977 Hebrew + 1,638 English; 60 English rows and 9
    Hebrew rows dropped for characters outside the model's IPA vocabulary).
    **[disk]**
  - English conversion: the author's espeak step **failed twice** in this
    environment (first a regex incompatibility with pandas 3, fixed by the
    pin; then a batch/line-count mismatch). A per-sentence conversion with
    the author's espeak settings (`en-us`, `preserve_punctuation`,
    `with_stress`, `language_switch="remove-flags"`) and the author's
    `normalize_text` was written (`en_phonemize.py`) and launched; **its
    result was not yet in evidence when this file was drafted.** See §8.
- **Not yet run (as of the evening session):** `compute_latent_stats` → DP
  training → T2L training with `--finetune`. **No newly generated training
  outputs of this experiment were evidenced** in any pasted transcript.
  (Absence of output is not proof of absence on disk.) The *downloaded
  pretrained* artifacts in `pt_models\` — including the author's
  `stats_multilingual.safetensors` — are inventoried above and are distinct
  from the not-yet-evidenced `runs\nh1\stats_multilingual.pt` that the
  first training step would produce.
- Scripts (all under `voice_test`, none in the engine), by evidence class:
  - **Run-verified [disk — creation and a completed run seen in pasted
    output]:** `clone.py`, `cfgtest.py`, `calm.py`, `gentle.py`, `sweep.py`,
    `final.py`, `taste.py`, `listemilia.py`, `emilia_prep.py`,
    `make_config.py`, `diag.py`, `he_phonemize.py`, `en_phonemize.py`.
  - **Supplied to Ness, creation and execution unverified [supplied,
    unverified]:** `bass.py`, `jamesavg.py`, `jamessoft.py`, `avg.py`,
    `check.py`, `say.py`. Their described behavior is the intent of the
    supplied code, not demonstrated operation.
  - Daytime scripts (`hear.py` … `shows.py`) are listed in the daytime
    record with its own evidence status.
- Removed today by Ness (dead ends): `transcripts\`, `voxforge-he\`,
  `cv-corpus-…\`, `crowd\`, `samples\`, `listen\`, and the two unpacked
  archives. **[disk]**

**Not claimed:** the full voice pipeline is not implemented; training is not
finished; the quality problem is not solved; fully offline operation of the
clone/synthesis path is not independently proved (the RenikudPlus weights are
fetched from the Hugging Face cache; a cold start with no network was not
tested). No hardware, latency, memory, or simultaneous-model performance is
inferred beyond the pasted evidence.

## 5. Placement, boundaries, and dependencies that remain open

**B29 remains open. B-INT-7 belongs to Bundle 5 and interfaces B29; it does
not complete B29. This record neither changes the accepted bundle order nor
closes Bundle 7.**

Preserved boundaries (from accepted sources; nothing here reopens them):

- Heavy model = background analysis; light model = the single visible
  conversational carrier; **N.H validates the relevant outputs** (handoff
  package §§1–4; placement record §4; B24 v7 §5A and §6.5 output gates).
- **Speech and delivery styling must not become a separate source of words,
  conclusions, certainty, or meaning.** The messenger may change wording,
  warmth, structure, language, presentation only — never meaning (handoff
  §3; B24 §1686 table).
- **v0_1's director constraint stands:** directions may change *how* the
  approved words are spoken, never add or remove words.
- Existing privacy and output authorization stand: **§7Q first, then SACL**,
  authorization rechecked before output (B-INT-6; Map I.0).
- **Ness speaking stops N.H's TTS immediately** (Master V10 lines 5145–5147;
  enforced by OOP; recorded by BOP as `voice_interrupt_of_nh` with timestamp
  and position — NHD-M26-VP, NHD-M25-BOP-VI). Recording that physical
  interruption **does not prove what Ness heard or understood.**
- Decision-index **F.2 V-NEW-1…7 remain `assistant_summary` /
  `assistant_proposal`.** This file does **not** decide full-answer buffering,
  streaming, or the handling and retention of an unplayed remainder.
- The delivery director's model, owner, interface, and actual control support
  remain undecided or unverified. (The evening session showed, as fact, which
  synthesis knobs exist — `cfg_scale`, `speed`, `silence_duration`,
  `text_is_phonemes` with IPA stress marks — which is *evidence of available
  controls*, not a director design.)
- The candor package is a **candidate, not adopted**; its §1.2 "warmth is
  delivery-only" is cited as the line this intent already follows; its §4
  Layer C language-model fine-tuning slot is **untouched** by the TTS
  fine-tune experiment.

B29's remaining mechanics stay open where not settled by accepted sources:
capture, cleanup, transcription, sensor/front-door handoff, TTS interruption
realization, latency handling, error/fallback, operation identity, §0B
logging, duplicate prevention, and crash recovery. **This record adds no
schema, store, event type, retry limit, fallback rule, or runtime interface.**

## 6. Open items

**Technical (voice experiment):**
1. RenikudPlus `datastore.json` — reported missing upstream (404 at
   `notmax123/RenikudPlus`; the newer page is login-gated). Local Hebrew
   stress/punctuation quality is a little below the public demo's.
2. End-of-sentence clipping in synthesis — the only workaround in use is a
   trailing throwaway sentence, which **adds a word to the input** and is
   therefore not usable for final N.H delivery (§4, §8); a proper fix is
   not found and is not designed here.
3. Remaining data preparation (English IPA result to confirm; §8) and the
   training sequence not yet run (`compute_latent_stats` → DP → T2L
   `--finetune`).
4. Whether the resulting model actually improves conversational delivery —
   unknown; Ness's ears decide.
5. BlueV3 check — not done; v0_1's version note preserved; no upgrade
   selected.
6. ivrit.ai podcast route — **shelved**, not selected for renewed work.
7. From v0_1, still outstanding unless evidence above resolves them:
   bilingual identity across a full listening set (only partly heard);
   mixed-language speech in one sentence (untested locally); dates, times,
   prices, numbers with gender (untested locally); latency and memory
   alongside the language models (untested); fully offline cold start
   without network attempts (untested).
8. The legacy cloud-TTS function in the engine (`nh_jarvis_core.py`) — still
   on the fix list for its audit part; untouched.

**Design (governance):**
9. B29 complete design — open (Bundle 7).
10. A21 — Interactive Translator model and Hebrew interim — open (Bundle 7;
    Ness).
11. Delivery director — model, owner, interface, control support — open.
12. F.2 V-NEW-1…7 — await Ness's own words.

## 7. Tone-listener note (recorded only; not raised, not placed)

**Unraised Register-A question for Ness. Interpreting tone, emotion, intent,
or meaning would be SMART-side interpretation, not BOP observation. No
specific component owner or placement has been decided.**

Ness asked in the evening how N.H could "understand how to reply to my
sounds and tones." This file records that the question exists. It assigns
it to no bundle, package, numbered Register item, model, component, or
implementation stage; it does not merge it with the output delivery
director; and it does not put the question to Ness.

## 8. Discrepancies and honest gaps, stated plainly

- **Row counts.** ChatGPT's instruction says the table is "in progress:
  4,684 rows — 2,986 Hebrew and 1,698 English — across 269 speakers." That
  is the *combined* table before cleaning and is on disk. After the author's
  cleaner the *cleaned* table on disk has **4,615 rows (2,977 he + 1,638
  en), 265 speakers**. Both numbers are recorded in §4; neither replaces the
  other.
- **English conversion path.** The v0_2 instruction says English conversion
  "uses espeak through the author's `combine_datasets.py`." In this
  environment that step failed (regex/pandas 3; then a batch length
  mismatch). The conversion was re-run per sentence with the author's own
  espeak settings and normalizer in a helper script (`en_phonemize.py`).
  The author's file was **not edited**. **Update, 2026-09-24 (v0_3) [disk]:**
  the helper's run was pasted after v0_2 was delivered — `english done:
  1638 converted, 0 empty dropped, 4615 rows total`, `{'en': 1638, 'he':
  2977} speakers: 265`, sample `nˈuːtɹɑːn ɪmˈɪʃən ɪz ɐ mˈoʊd …`. The
  cleaned table is therefore complete in both languages. This discrepancy
  is closed; the v0_2 row-count note above stands as history.
- **`say.py` and the other supplied-but-unverified scripts** (`bass.py`,
  `jamesavg.py`, `jamessoft.py`, `avg.py`, `check.py`, `say.py`): code was
  delivered as paste blocks; no pasted run shows their creation or
  execution. Recorded as supplied code with intended behavior, not as
  verified files. Any claim in this file about what they *do* is a claim
  about the code as supplied.
- **Anti-clipping tail.** The `say.py` workaround appends "וזהו." to Hebrew
  synthesis input. No evidence shows the tail removed before playback; the
  supplied code does not remove it. Incompatible with final N.H delivery
  under the content-preservation rule; experimental limitation only (§4).
- **v0_1 baseline encoding.** v0_1 is UTF-8 with LF line endings; it is
  embedded below byte-for-byte from the repository file. This candidate is
  also UTF-8/LF.

## 9. Self-audit (drafting checks)

- **Source check:** all named sources present at commit `280f20ab`; v0_1
  blob hash matches Ness's baseline; no source reconstructed.
- **Preservation check:** v0_1 embedded verbatim in §A; a byte comparison of
  the extracted §A body against the repository file was run before delivery
  (result reported with the delivery).
- **Decision check:** §2 items map one-to-one to Ness's evening statements
  ("i decided to go with american", "it's ok" on the American-tagged voice,
  "i do not want to use people who i know", "i don't want a stranger which
  is someone i paid for", "it is only for me", "option 1" → later "no, i
  will not wait for meta… find better or different places" → Emilia; "i
  want to do it now" on training). Observations, measured facts, reported
  diagnoses, planned steps, and unknowns are separated in §3, §4, §6.
- **Scope check:** B29 open (§5); B-INT-7 not confused with speech-output
  completion (§5); no tone-listener placement (§7); no accepted rule
  reopened; no V-NEW item promoted; no model adopted; no schema or runtime
  mechanism added; no concept decided by Claude.
- **Arithmetic:** 2,986 + 1,698 = 4,684; 1 + 268 = 269; 2,977 + 1,638 =
  4,615; 4,684 − 4,615 = 69 = 60 en + 9 he.
- **No existing source edited; no build work run for this task; no
  acceptance or adoption decision made; nothing committed or pushed.**

## 10. v0_3 correction record (2026-09-24)

| # | Correction (ChatGPT instruction item) | Where applied |
|---|---|---|
| 1 | Evidence labels made consistent; `say.py` and five other scripts relabeled **supplied, unverified**; settings split into run-verified vs intended-by-code; scripts list split by evidence class. | §4 (settings line, `say.py` line, scripts list), §8 |
| 2 | Blanket "No checkpoint, stats file, or trained weights exist" replaced with: listed stages not run as of the session; no newly generated outputs evidenced; downloaded pretrained inventory (incl. author's `stats_multilingual.safetensors`) preserved and distinguished. | §4 |
| 3 | Anti-clipping workaround tied to the content-preservation rule; playback removal marked not evidenced; recorded as experimental limitation, not an exception; no replacement designed. | §4, §6 item 2, §8 |
| 4 | §2 item 10 (working style) moved out of the confirmed-decision list; source given (daytime record §1 items 10–11, quoting Ness); kept as Claude-reported, not independently verified. | §2 |
| + | **Beyond the four items, flagged for the auditor:** §8's English-conversion discrepancy updated with the pasted result (1,638 converted, 0 dropped, 4,615 rows). Added because it is existing pasted evidence that resolves a discrepancy §8 had left open; strike if judged out of scope. | §8 |

v0_3 checks: v0_2 compared line-by-line for unintended loss (only the
passages above changed); embedded v0_1 byte comparison repeated (result
reported with delivery); every `[disk]` label re-read against a pasted
transcript; every `[supplied, unverified]` label applied where no run was
pasted. No runtime test, training, code change, installation, engine change,
or repository commit was made for this correction.

---

## A. Historical baseline — `NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md`, verbatim

Everything between the two marker lines is the original v0_1 file, byte for
byte (Git blob `91a0439f1457e1bb6fca320f0143bff779a53da8`). Its status lines,
"none chosen," and "not decided, not designed, not built" describe the
2026-09-23 daytime snapshot and are superseded only where §1–§2 above say so.

<!-- BEGIN v0_1 VERBATIM -->
# NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_1.md

## Status

- **Class:** Intent capture — INACTIVE CANDIDATE. Not a design. Not adopted.
  Decides nothing. Authorizes no implementation. Selects no model.
- **Owner of the concept:** Ness (Register A). This file records Ness's own
  decisions and ideas in preserved form so they cannot be lost; all meaning,
  policy, model choice, and acceptance authority remain with Ness.
- **Origin:** Stated by Ness during the 2026-09-23 session, after a ChatGPT
  research pass (GPT-6 Astra Ultra, web search + GitHub connector) on offline
  bilingual Hebrew/English text-to-speech, and after a first listening test
  (Claude-assisted capture, same route as `NH_ISSUE_CHANNEL_INTENT_v0_1.md`).
- **Intended folder:** `05_INACTIVE_CANDIDATE/`
- **Authority:** Subordinate to NH_MASTER-20_CORRECTED_v10.md and the full
  authority order. Nothing here overrides, reopens, or modifies any accepted
  design, seal, store, or decision. Where the voice layer sits in the design
  is not decided here.
- **Build order:** not scheduled. The voice matters only once live chat exists
  and the conversational models are chosen; nothing in Bundle 1 depends on it.

## Part 1 — The voice (Ness's decision, 2026-09-23)

1. N.H's spoken voice is **a normal 20–24-year-old man**.
2. **The same voice in English and in Hebrew.** One person, two languages —
   not two voices.
3. In Hebrew it must sound **native Israeli**, not like a foreigner reading
   Hebrew.
4. Like everything in N.H, it must run **locally and offline**. No cloud
   speech. (A legacy function in the engine, `nh_jarvis_core.py`, calls
   OpenAI cloud TTS; it is excluded and goes on the fix list when its audit
   part is reached.)
5. Ness likes, from voices he has heard elsewhere: **warmth**, **good choice
   of tone per sentence**, and **liveliness / energy**. These are wants about
   delivery, not about the words.

## Part 2 — First listening test (2026-09-23, Ness's ears)

- Tool: the public BlueTTS demo (Hebrew-first, MIT, ONNX/CPU path; by an
  Israeli developer; same author as the Hebrew pronunciation tools RenikudPlus
  / Phonikud). Preset voices only, no cloning, browser demo, not a local run.
- Text: the first three sentences of the listening set (greeting; the two
  meanings of ספר — barber and book; numbers with gender).
- **Result, in Ness's words: "it read it in perfect Hebrew."** Native, not
  foreign. The preset voices sounded **too slow** (a speed slider) and **too
  old** (the preset voice, not the model).
- Not yet tested: a young male voice (needs a reference clip), English from
  the same voice, mixed Hebrew–English in one sentence, dates/prices, delay
  and memory on Ness's PC next to the language models, and a fully offline
  cold start with no network attempts.
- Note: BlueTTS has moved past the version the research pass ranked (a V3
  exists). Any real test starts from the newest explicitly licensed version.

## Part 3 — Where the voice comes from (Ness's options, none chosen)

A model like this speaks in whatever voice it is given a few seconds of.
There is no "younger" setting; the age is in the clip.

- Option A: **Ness's own voice** (fastest test; no consent question).
- Option B: **a consenting friend or family member of the right age**, who
  agrees to both languages and to Ness keeping the recording and voice
  profile.
- Not an option: any actor, YouTuber, or product voice who did not agree,
  including cloning a commercial assistant's voice (not Ness's to use, and an
  English clip would leak an American accent into the Hebrew).

## Part 4 — The delivery director (Ness's idea, 2026-09-23)

Ness asked: *is there a way to build a system for the voice that instructs
it and tells it what to do?* Captured as follows, in the shape stated in chat
and not objected to:

- **Two tracks, not one.**
  - Track 1 — **what** N.H says: the final, validated words. Untouchable.
  - Track 2 — **how** to say it: per-sentence directions such as slower,
    gentle, lively, stress this word. A small "director" that reads the
    meaning and writes stage directions for the voice.
- **The one hard rule:** the director may add *how*, never *what*. It puts no
  words in and takes no words out. Otherwise it would be a second mouth that
  can drift from the validated answer.
- This is the same line the candor package already draws: **warmth is
  delivery-only** and never softens what N.H actually says.
- Consequences for model choice (a selection criterion, not a decision): the
  voice model must accept directions (per-sentence style, speed, emphasis,
  or emotion tags). Whether BlueTTS does is unchecked. This matters more than
  the accent test already passed.
- Who runs the director is open (the light model of the accepted dual-model
  handoff is one candidate because it already sits at the delivery end).
  Ness decides.

## What already exists nearby (for whoever designs this later)

- Master V10 requires speech to stop immediately when Ness speaks; generated
  text, played audio, and what Ness actually heard are different facts.
- Decision index F.2 **V-NEW-1**: "complete final answer generated before
  speaking; speech = playback of existing text" is compatible with, but not
  decided by, the dual-model handoff package. Open.
- The accepted output chain (privacy first, SACL second, authorization
  rechecked before output) applies to whatever the voice plays.
- The ChatGPT research report (2026-09-23, in Ness's ChatGPT N.H master
  project) lists candidates and a listening set; every claim in it is
  unverified until heard on Ness's PC.

## Boundaries stated now

- Offline only; nothing leaves the PC at runtime.
- One voice identity across both languages.
- Directions never change words.
- No model, no speaker, no placement, no playback timing decided here.

## Not decided, not designed, not built

Everything above is intent and a test result. No mechanics, schema, wiring,
or scheduling exists. Reopening this is Ness's act.
<!-- END v0_1 VERBATIM -->

*End of NH_VOICE_AND_DELIVERY_DIRECTOR_INTENT_v0_3_CANDIDATE.md — inactive candidate; unadopted; B29 remains open.*
