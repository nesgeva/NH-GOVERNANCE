# NH_READ_ALOUD_START_POINT_INTENT_v0_2.md — Ness's intent: choose where N.H starts reading aloud, and ask it to repeat

**What this is.** Ness's new feature idea, recorded in his words on 2026-10-05, so that it is not lost. **It is an intent, not a design.** It decides nothing, adds nothing to Master-21, and is designed later through the normal route, after Ness decides its open questions. Prepared by Claude at Ness's request. Status: CANDIDATE (intent), for `05_INACTIVE_CANDIDATE/`.

**Version note (v0_2, 2026-10-05).** v0_1 (SHA-256 `6de4a62b67727b135dc14cab6c457fec1f31f4a75a7c7b70b76853877683d6c1`; kept) recorded the start-point idea. Ness then added "repeat" (§1, §3 question 4). Nothing else changed.

## 1. Ness's words

- "whether ... there is a rule/feature that says that i will be able to choose from where n.h will begin reading, rather than only read from start to finish (read aloud)"
- "we need to add it tho... it's a small feature tho"
- "in the read aloud, i could ask N.H to repeat a phrase or wording or all of the sentence again with and without writing it again in chat. by saying \"repeat\""

## 2. What Master-21 already has (checked at `nesgeva/NH-GOVERNANCE@9645157`)

- **No rule lets Ness choose where reading aloud starts.** The phrase "read aloud" does not occur in the book.
- **N.H speaks (TTS) and stops at once when Ness starts speaking:** C-OOP.7 — Immediate voice-priority TTS stop; MAP C-9.
- **The interruption is recorded with a timestamp and the position in N.H's output stream:** C-BOP's `voice_interrupt_of_nh` event, book lines 211523–211541.
- **No rule uses that recorded position** to resume or to choose a start point.

## 3. Open questions (Ness's to decide; they join his question queue, route note v0_8 §9.9)

The examples below only help him think; they are not options anyone has chosen.

1. **What can N.H read aloud?** For example: its own replies, any text on screen, documents and files Ness gives it, or all of these.
2. **How does Ness choose where it starts?** For example: pointing at a line or paragraph on screen, saying it ("start from the second paragraph"), or both.
3. **After an interruption, should N.H offer to continue from where it stopped?** The stop position is already recorded.
4. **"Repeat":** what does "repeat" alone repeat (for example the last sentence), and how does Ness pick a phrase or a single wording instead? Which way is the default: repeated aloud only, or also written again in chat? Ness wants both to be possible.

## 4. What stays fixed whatever the answers

The existing rules hold, and this intent does not reopen them:
- N.H stops speaking at once when Ness speaks (C-OOP.7);
- anything read aloud is visible output, so it passes the output gates in their fixed order: privacy (§7Q) first, then speaker access (SACL).
