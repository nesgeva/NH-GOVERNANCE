# N.H Research Pipeline — Full Breakdown (Old vs New)

*Written for Ness, June 18 2026. Treats every detail as if you're seeing it fresh.*

---

## What is N.H trying to do with research?

N.H is your personal AI system running locally on your PC. One of its planned features is a **nightly research loop**: while you sleep, N.H goes out to the internet, gathers real information about topics you care about, and stores it locally. When you wake up and use N.H during the day, it already has fresh knowledge sitting on your machine — no need to be online.

The core design rule of N.H is **cognitive sovereignty**: no piece of information is allowed to become a "fact" in your system unless YOU personally approve it. Everything starts as SIMULATION (unverified), and only becomes REALITY after you review it and click Promote on the `/review` page.

---

## How the OLD system worked (what we had until today)

### The function: `deep_research(topic)`

When N.H wanted to research a topic, it called a function called `deep_research()`. Here's what happened step by step:

- **Step 1 — Three parallel AI searches.** N.H sent the topic to a model called `perplexity/sonar-deep-research` three separate times, each from a different "angle" (logical, medical/scientific, psychological/systemic). Each of these three calls was a full AI-powered research session — the model went out to the internet on its own, read websites on its own, decided what was relevant on its own, and came back with a written summary.

- **Step 2 — Verification.** N.H took those three AI-written summaries and sent them to another model (`llama-3-70b-instruct`) asking: "which facts appear in at least 2 out of 3 of these summaries?" Only facts confirmed by multiple angles were accepted.

- **Step 3 — Queue for your review.** The verified facts were written to `.nh_simulation_graph.jsonl` as SIMULATION records, waiting for you to approve or reject them on the `/review` page.

### What was wrong with this (not just cost)

- **The AI was filtering before you ever saw anything.** Each of those three `sonar-deep-research` calls didn't just fetch web pages — it *chose* which websites to read, *chose* which facts to include, *chose* how to summarize them, and *chose* what to leave out. By the time your verification step ran, it was comparing three AI opinions against each other — not three sets of raw facts.

- **You could never see or audit the original sources.** The raw web pages, the actual URLs, the original text — none of that was visible to you or stored anywhere. You only ever saw Perplexity's narrative version of what the internet said.

- **This directly conflicted with N.H's core principle.** The whole point of the SIMULATION→REALITY pipeline is that YOU are the gate, not an AI. But the AI was already acting as a hidden gate before your gate, filtering what reached you without your knowledge or control.

---

## The cost problem (real numbers)

### What one `deep_research()` call actually cost

Each call to `deep_research()` triggered:

- **3× calls to `sonar-deep-research`** (one per angle, running in parallel)
- **1× call to `llama-3-70b-instruct`** (the verification/synthesis step)

`sonar-deep-research` is one of the most expensive API models available. Its pricing stacks multiple layers on top of each other:

| Cost layer | Price |
|---|---|
| Input tokens (your prompt) | $2.00 per million tokens |
| Output tokens (its response) | $8.00 per million tokens |
| Citation tokens (source references it generates) | $2.00 per million tokens |
| Reasoning tokens (its internal thinking) | $3.00 per million tokens |
| Search queries (each web search it runs internally) | $5.00 per 1,000 searches |

A single deep research query can cost **$0.41 or more** just for one call. Your function made **three** of these per topic.

### What today's testing session cost

- You ran `deep_research()` multiple times today for testing (some completed, some got stuck and were killed mid-run)
- Total cost jumped from ~$2.31 to ~$12.57 in roughly one hour of testing
- That's approximately **$8–10 burned on test runs alone**

### What the planned nightly loop would have cost

The original plan was: run `deep_research()` continuously overnight, topic after topic, for ~8 hours.

- Each cycle takes roughly 1–4 minutes (we measured 3.5 minutes for one today)
- In 8 hours, that's roughly **120–480 cycles**
- At ~$2–3 per cycle, that's **$240–$1,440 per night**
- Even conservatively: **hundreds of dollars per night, every night**

This was not sustainable. But the cost problem led us to discover the much bigger problem: the opinion-filtering problem described above.

---

## How the NEW system will work

### The core idea: separate "fetching" from "thinking"

Instead of one expensive black-box AI call that does everything invisibly, we split the job into two clean, auditable layers:

### Layer 1 — Raw fetch (NO AI involved at all)

- N.H sends a search query to a **raw search API** (like Tavily or Brave Search API)
- The API returns exactly what a search engine would show you: page titles, URLs, and text snippets
- **No AI touches this data.** No model reads the pages, no model decides what's relevant, no model writes a summary. It's just raw internet results, exactly as they exist
- These raw results are stored locally, so you can always see and audit exactly what came back from the internet before anything else happened to it

### Layer 2 — Our own synthesis (AI involved, but ours, controlled, auditable)

- N.H takes those raw results and sends them to `llama-3-70b-instruct` (the model already in use, already paid for at normal rates)
- The prompt says: "Here are raw search results from 3 different search queries about this topic. Extract only facts that appear in at least 2 of the 3 result sets. Do not add anything that isn't in the raw data."
- The model's output goes to `.nh_simulation_graph.jsonl` as SIMULATION — same as before
- You review and approve/reject on `/review` — same as before

### What's different (and why it matters)

- **The raw internet data is preserved.** You can see exactly what websites said, exactly what URLs were returned, before any AI interpreted anything. The old system threw this away invisibly.

- **The AI's role is limited and controlled.** It only sees what the raw search returned — nothing more, nothing less. It can't secretly decide to ignore a source or add information from somewhere you didn't ask about. Its job is extraction, not exploration.

- **One AI pass instead of four.** Old system: 3× expensive AI search + 1× AI verification = 4 API calls with AI involved. New system: 3× cheap raw search + 1× AI synthesis = 1 API call with AI involved. The AI does less, which means less opportunity for opinion to creep in.

- **You can audit every step.** Raw results stored → AI synthesis stored as SIMULATION → you review. The full chain is visible. Nothing happens in a black box you can't inspect.

---

## Cost comparison (realistic)

### Raw search API pricing

| Service | Free tier | Paid rate |
|---|---|---|
| Tavily | 1,000 searches/month free | ~$0.001 per search after that |
| Brave Search API | 2,000 searches/month free | ~$0.003 per search after that |

### One research cycle: old vs new

| | OLD (sonar-deep-research) | NEW (raw search + our synthesis) |
|---|---|---|
| Search step | 3× sonar-deep-research calls (~$0.41+ each) | 3× raw search API calls (~$0.001–0.003 each) |
| Synthesis step | 1× llama-3-70b-instruct call (~$0.01–0.05) | 1× llama-3-70b-instruct call (~$0.01–0.05) |
| **Total per cycle** | **~$1.50–3.00** | **~$0.01–0.08** |
| AI opinion layers | 4 (3 search + 1 verify) | 1 (synthesis only) |
| Raw sources visible? | No | Yes |

### One night of continuous research (8 hours, ~150 cycles)

| | OLD | NEW |
|---|---|---|
| Search costs | ~$180–450 | ~$0.15–0.45 (or $0 on free tier) |
| Synthesis costs | ~$2–8 | ~$2–8 |
| **Total per night** | **~$200–450** | **~$2–8** |

### Monthly cost (running every night, 30 days)

| | OLD | NEW |
|---|---|---|
| **Monthly estimate** | **$6,000–13,500** | **$60–240** |

These are estimates based on published pricing and our real measurements today. Actual costs vary with topic complexity, response length, and how many cycles you configure per night.

---

## What stays the same (things that don't change)

- **The SIMULATION→REALITY pipeline.** Every piece of information still enters as SIMULATION, still requires your explicit approval to become REALITY. This is unchanged.

- **The `/review` page.** You still see everything in the review queue, still click Promote or Reject. No change.

- **The verification logic.** We still require facts to appear in multiple independent sources before accepting them. The method changes (raw search results instead of AI summaries), but the principle is the same.

- **The nightly schedule.** `nh_nightly.py` still runs at 3:00 AM. The internal mechanism changes, but the timing and automation concept stays.

- **Your role as the final gate.** Nothing enters REALITY without your approval. This is the most important rule in the system and it does not change.

---

## What you need to do right now

**One thing: pick a raw search API and sign up for a free account.**

Two good options:

- **Tavily** (tavily.com) — 1,000 free searches/month. Built specifically for AI applications that need raw web data. Simple API, good documentation.

- **Brave Search API** (brave.com/search/api) — 2,000 free searches/month. From the Brave browser company. Privacy-focused, also simple.

Either works. Pick whichever feels right, sign up, and grab the API key. That's the only thing needed before we can start building.

---

## Summary in one sentence

We're replacing an expensive black-box AI that secretly filtered the internet before showing it to you, with a cheap raw pipe that gives you the actual internet — and then using your own controlled AI to extract facts from what's really there.
