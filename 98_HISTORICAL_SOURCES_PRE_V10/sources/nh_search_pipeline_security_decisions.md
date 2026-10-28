# N.H Search Pipeline — Security & Source Decisions

*Session notes for Nes, June 18 2026. Continues directly from "N.H Research Pipeline — Full Breakdown."*

## Search API: Brave, confirmed

Chosen over Tavily specifically because Brave returns genuinely raw JSON from its own independent index (not Google/Bing underneath), with no extraction, relevance-ranking, or content-validation layer applied before the data reaches N.H. Tavily does apply that kind of processing — closer to "pre-chewed for AI" than literally untouched — which is the smaller version of the exact opinion-layer problem this whole pivot was meant to escape.

**Corrected pricing** (the original doc's numbers were stale): Brave's Search plan is $5 per 1,000 requests, with $5 free credit/month applied automatically. At full nightly-automation volume (150 cycles/night × 3 searches, 13,500/month), that's roughly $60–65/month for Brave itself, plus ~$60–240/month for the separate synthesis step (OpenRouter/llama-3-70b-instruct) — combined total around $120–300/month at full scale. Still nowhere near the old $6,000–13,500. Note: that full number only applies once the nightly autonomous scraper is actually built and running every night — cost stays near $0 (inside the free credit) during building/testing.

## Security model: malware vs. prompt injection

Traditional malware isn't really on the table here — there's no download-and-execute step, and the pipeline only ever pulls titles/URLs/snippets, not rendered pages with embedded scripts. (Stays true only if no future step renders full pages or runs JS from arbitrary URLs — if full-page text is ever needed, fetch as plain text, never execute.)

The real risk is **prompt injection**: malicious page content worded to manipulate the synthesis model reading it. The SIMULATION/REALITY gate — built for an unrelated reason — already contains this almost completely: even a successful injection only ever produces a SIMULATION record, never a direct action, never a write to REALITY. Worst case is "something misleading sits in the review queue," not anything happening on the machine.

**Two conditions required to keep that true (build defaults, not optional add-ons):**
1. Synthesis model is text-in/text-out only — no tool-calling, no file access, no ability to make its own outbound requests.
2. Synthesis system prompt states explicitly that search results are unverified raw web content to extract facts from, never instructions to follow.

Both go into the Cursor instruction for the synthesis call by default, not as something to remember to ask for separately.

## Auto-reject, not auto-delete

Decision: flagged/untrusted content routes automatically into the existing Reject bucket — no click required, doesn't block the day — but stays logged, same as any other rejected record. Explicitly **not** silent deletion: an AI with silent-delete authority over "untrustworthy" content is itself a prompt-injection target (a malicious page could try to get something legitimate flagged and erased instead of just contained), and it reintroduces the exact "things happening invisibly" failure this whole gate exists to prevent.

## Rejected-bin display rules ("look, don't touch")

For viewing flagged entries safely, once that page exists:
- URLs render as plain text strings, never `<a href>` — nothing clickable, nothing to misclick.
- No auto-fetched favicons, previews, or unfurling — viewing the bin never triggers an outbound request toward anything in it.
- Copy/select disabled on that specific view — a guardrail against accidental drag-select-and-paste, not a real security boundary (anyone could still view source). Solves the actual stated problem: not touching it by accident.
- Strip invisible/zero-width and RTL-override characters before display — closes a text-spoofing gap that survives plain-text rendering otherwise.
- Render via `textContent`-style escaping, never `innerHTML` — anything that looks like a tag displays as inert literal characters.

## Still open

Academic search source — Semantic Scholar API vs. OpenAlex vs. both. (Google Scholar has no official API and scraping it violates Google's ToS, so it's off the table either way.) Both candidates are free and slot into the same raw-fetch → synthesis → gate pipeline as a second source, no new architecture required. Decision pending — Semantic Scholar is sharper for CS/AI-leaning queries, OpenAlex is broader across all fields.
