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
