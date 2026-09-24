# N.H Interactive Architecture Canvas — Design Spec
*Captured June 19 2026, from a live design session with Nes. Standalone test pages were built to find the right feel; this spec captures the full vision for building it into N.H proper.*

---

## The core idea

A spatial canvas where N.H's architecture (and eventually its live data) is represented as **interactive illustrated icons** — not abstract labeled boxes. You recognize each piece by its shape, operate it by touching it, and the canvas itself signals what kind of thinking you're doing through its background. This fits how Nes thinks: spatially, by interacting with things, not by reading text.

---

## Two modes (background = mental mode)

The background isn't decoration — it tells you (and anyone watching) which kind of work you're doing.

- **Architecture mode → pure black** + faint red blueprint grid. Stark, clean, for *structuring* the system — laying out modules and connections.
- **Solution/thinking mode → dark metallic blue** (brushed-metal sheen and depth, not flat). For *working through problems*.

The mode-switch idea connects directly to the earlier "live-changing background depending on mode" thought from the mobile-app session — the interface showing its own state through color.

---

## The icons

- **Illustrated, not boxes.** Each component type looks like the actual thing: a vault for a memory store, a gate for a gate, a glowing core for the engine, a sandbox for the sandbox, etc.
- **Art style: chosen as "C2 + D2 combined"** — warm inner glow-fill (D2) plus sci-fi HUD detailing (C2: dashed scanner outline, antenna dot, small monospace labels). Reference file: `nh_icon_combined.html`.
- **Color-coded by type:** red = core module, orange = gate (approval enforced), purple = physical store. (Carried from the canvas color legend.)
- **Swappable** — Nes can pick/change which icon a node uses.
- **Interactive as live controls** — this is the key part. Icons aren't pictures, they're operable:
  - Click the vault/store → see the records inside it
  - Click the gate → review what's pending approval
  - Click the core → see engine state
  - Each icon reacts visually when touched (pulse/flare — first version built in `nh_icon_combined.html`).

The endpoint: the architecture map doesn't just *describe* N.H — it becomes a way to *operate* N.H.

---

## The grid

Faint red grid lines on the black background — signals "this is the blueprint/design surface." Stays for architecture mode. Keep it.

---

## Generation: /generateincanvas (backend, build LAST)

The canvas should be able to **pull real topics/content that already exist** and generate them onto the canvas automatically — either:
- from **all sources at once** (scan files + memory + modules, lay them out), or
- by a **specific command** like `/generateincanvas <topic>` that pulls just that topic.

**Critical build-order note:** this part CANNOT be a standalone test page. It requires the canvas to talk to N.H's real backend — read files, query the vector index, hit the engine. That means a real backend route in N.H proper (Cursor work, touching the actual system), not a sandboxed HTML file. Build the canvas + icons + interactivity FIRST as the visual surface; wire generation in LAST.

---

## Build order (the right sequence)

1. **The canvas surface** — pure-black grid, draggable nodes, drawable connections. (Standalone prototype already built: `nh_architecture_canvas.html`.)
2. **The illustrated icon set** — full set in the chosen C2+D2 style, replacing the plain boxes. (Style proven on 3 sample icons: `nh_icon_combined.html`.)
3. **Icon interactivity** — each icon as a live control (click vault → records, click gate → pending, etc.). Visual reaction on touch already prototyped.
4. **The metallic-blue solution mode** — same canvas, reskinned.
5. **`/generateincanvas` backend** — the real N.H route that populates the canvas from actual sources. Built into N.H proper, LAST.

---

## Prototype files built this session (standalone, safe, no backend)

- `nh_canvas_test.html` — interactive red particle field (first "touchable background" test)
- `nh_architecture_canvas.html` — draggable module canvas on pure-black grid, N.H modules pre-loaded
- `nh_icon_styles.html` — four art-direction options for icons (A neon / B solid / C sci-fi HUD / D glow-fill)
- `nh_icon_combined.html` — the chosen C2+D2 combined style, 3 sample icons, click-to-react

---

## Honest notes

- This is pure frontend — zero risk to N.H's backend, memory, or gates — until step 5 (generation), which is the only part that touches the real system.
- This whole canvas is a genuine sub-project, not a quick tweak. It came out of a tired late-night session and will build better fresh, one piece at a time — same discipline that's worked all along.
- The security/audit work this session is separate and already done; this canvas is a new creative direction, not a fix.
