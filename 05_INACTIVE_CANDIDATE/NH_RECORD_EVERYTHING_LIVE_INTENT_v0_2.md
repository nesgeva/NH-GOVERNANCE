# NH_RECORD_EVERYTHING_LIVE_INTENT_v0_2.md — Ness's intent: everything recorded as it happens

**What this is.** Ness's intent, recorded in his words on 2026-10-05; he marked it important. **It is an intent, not a design.** It decides nothing and adds nothing to Master-21. v0_1 marked a conflict that Ness's clarification has since removed (§3). Prepared by Claude at Ness's request. Status: intent, for `05_INACTIVE_CANDIDATE/`.

**Version note (v0_2, 2026-10-05).** v0_1 (SHA-256 `2efb78014850ccd660f248c7ba2de2a30d1e7b3b52290a532fe3f1842aabfbd8`; kept) read "every letter" as letter-by-letter typing. Ness clarified it the same day, so this version adds his words (§1), replaces the conflict with his clarification (§3) and answers question 1 (§4). Nothing else changed.

## 1. Ness's words

"1 important thing that i need you to focus on is: each and every thing that i do, n.h does and happens, n.h records as it is, when it happens - not in the end of the session. there will be a log for n.h to know EVERYTHING and when I say everything i mean every click, every voice chat, text letter of the alphabet!!!!! every single click and command i do etc-..."

**His clarification:** "when i said \"every latter i type\" i mean that i want that every sentence it recieves is recorded on it's end"

## 2. What already exists (checked at `nesgeva/NH-GOVERNANCE@9645157`)

- **The recording law, V10 line 235:** "EVERYTHING IN N.H IS PERMANENTLY RECORDED, CONNECTED, AND ACTIVELY USABLE AS LIVING MEMORY. Every external input and every internal N.H operation ... must be permanently recorded ... Silent operations are prohibited."
- **What is captured:** C-BOP — Behavioral Observation Processing takes in "Available authorized voice, confirmed sent text, interface and session events, and explicitly authorized imported content" (V10 §25.1).
- **Accepted Bundle 6 policy A10:** inside a session Ness has explicitly opened, N.H "may record **all available authorized behavioral signals**", without separate permission per signal. It does not authorize capture outside an authorized session.
- **When records are written:** no rule was found that says it. "As it happens, not at the end of the session" would make that explicit.

## 3. No conflict (resolved by Ness's clarification)

- v0_1 read "every letter of the alphabet" as letter-by-letter capture while typing, which C-BOP forbids ("Must never: ... observe unfinished typing", V10 §25.1).
- Ness meant something else: **every message N.H receives is recorded on its end.** That is what C-BOP already takes in ("confirmed sent text"), so the existing rule stays as it is.

## 4. Open questions (Ness's; they join his question queue)

1. ~~Typing~~ **Answered by Ness:** every message N.H receives is recorded on its end. Unfinished typing is not recorded, so the rule is unchanged (§3).
2. **Clicks:** every click and every interface action? Interface events are captured already.
3. **Timing:** each thing recorded at the moment it happens (Ness: yes; this would become an explicit rule).
4. **Outside a session:** recording happens inside sessions Ness has opened (A10). Should that stay, or should anything be recorded outside one?
