"""
nh_log.py - the read-only HTML log / "mirror" of the accretive store (N.H §7B Part 7)
=====================================================================================
The standalone clickable surface that replaces nh_peek.py for actually reading the
store. Same read discipline as nh_peek: uses ONLY the public read function
nh_accretive_store.read_all(); never parses the .jsonl directly; never writes to the
store. The ONLY thing it writes is a single self-contained file, nh_log.html, in the
current folder.

  python nh_log.py            ->  builds nh_log.html, then open it in a browser

What the page does:
  - groups every record by subject (provenance for now; real subjects arrive with the engine)
  - shows the SHAPE of the store at a glance (each group's bar = its real size)
  - expand a group -> read its records, content first, Hebrew/RTL rendered correctly
  - search content across the whole store
  - read-only: nothing on the page can edit the store; it is a mirror, not a console

Offline by design: no external fonts, no CDN, no network. One file, opens anywhere.
Throwaway like nh_peek -- discard if/when a live engine-backed log supersedes it.
"""

from __future__ import annotations

import json
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

from nh_accretive_store import read_all

OUT_FILE = Path(__file__).parent / "nh_log.html"


def _build_payload() -> dict:
    records = read_all()

    groups: "OrderedDict[str, list]" = OrderedDict()
    for r in records:
        subject = r.get("subject") or "(no subject)"
        groups.setdefault(subject, []).append({
            "id": r.get("id", ""),
            "content": r.get("content", ""),
            "source_title": r.get("source_title"),
            "re_reads": r.get("re_reads", []),
            "timestamp": r.get("timestamp", ""),
        })

    group_list = [
        {"subject": subject, "count": len(recs), "records": recs}
        for subject, recs in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ]

    return {
        "total": len(records),
        "group_count": len(group_list),
        "generated": datetime.now().isoformat(timespec="seconds"),
        "groups": group_list,
    }


def _render_html(payload: dict) -> str:
    # Embed as JSON in a data island; escape "</" so content can never close the script tag.
    data_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return _TEMPLATE.replace("/*__DATA__*/", data_json)


_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>N.H - The Log</title>
<style>
  :root{
    --ink:#0c0c11;
    --surface:#14141b;
    --surface-2:#1b1b25;
    --line:#272733;
    --line-soft:#1f1f2a;
    --text:#e9e7f1;
    --muted:#8b8799;
    --muted-2:#5f5c6e;
    --violet:#a78bda;
    --violet-dim:#6b5a9e;
    --violet-bg:#1c1730;
    --root:#5a8f86;
  }
  *{box-sizing:border-box;}
  html,body{margin:0;padding:0;}
  body{
    background:var(--ink);
    color:var(--text);
    font-family:"Segoe UI", system-ui, -apple-system, sans-serif;
    line-height:1.7;
    -webkit-font-smoothing:antialiased;
  }
  .mono{font-family:"Cascadia Code","Consolas",ui-monospace,monospace;}

  .wrap{max-width:920px;margin:0 auto;padding:0 22px 120px;}

  /* ---- header ---- */
  header{padding:54px 0 26px;border-bottom:1px solid var(--line);}
  .eyebrow{
    font-family:"Cascadia Code","Consolas",ui-monospace,monospace;
    font-size:11px;letter-spacing:.34em;text-transform:uppercase;
    color:var(--violet);margin:0 0 14px;
  }
  h1{
    margin:0;font-size:30px;font-weight:600;letter-spacing:-.01em;color:var(--text);
  }
  .sub{margin:12px 0 0;color:var(--muted);font-size:15px;max-width:60ch;}
  .note{
    margin:16px 0 0;color:var(--muted-2);font-size:13px;
    border-left:2px solid var(--line);padding-left:12px;max-width:60ch;
  }
  .stat-row{
    display:flex;gap:28px;margin-top:26px;flex-wrap:wrap;
    font-family:"Cascadia Code","Consolas",ui-monospace,monospace;font-size:12px;
  }
  .stat b{color:var(--text);font-size:18px;font-weight:600;display:block;letter-spacing:0;}
  .stat span{color:var(--muted-2);letter-spacing:.08em;text-transform:uppercase;font-size:10px;}
  .ro{
    float:right;font-family:"Cascadia Code","Consolas",ui-monospace,monospace;
    font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-2);
    border:1px solid var(--line);border-radius:3px;padding:4px 9px;
  }

  /* ---- search ---- */
  .search{position:sticky;top:0;background:var(--ink);padding:18px 0 14px;z-index:5;
          border-bottom:1px solid var(--line-soft);margin-bottom:10px;}
  .search input{
    width:100%;background:var(--surface);border:1px solid var(--line);
    color:var(--text);font-size:14px;padding:11px 14px;border-radius:7px;outline:none;
    font-family:inherit;
  }
  .search input:focus{border-color:var(--violet-dim);}
  .search input::placeholder{color:var(--muted-2);}
  .searchmeta{margin-top:9px;font-size:12px;color:var(--muted);min-height:16px;
              font-family:"Cascadia Code","Consolas",ui-monospace,monospace;}

  /* ---- group seams (the strata signature) ---- */
  .group{border-bottom:1px solid var(--line-soft);}
  .seam{
    display:grid;grid-template-columns:1fr auto;align-items:baseline;gap:14px;
    padding:16px 4px 8px;cursor:pointer;user-select:none;
  }
  .seam:hover .subject{color:var(--violet);}
  .subject{font-size:15px;color:var(--text);transition:color .15s;
           word-break:break-word;}
  .subject .car{display:inline-block;width:1.1em;color:var(--muted-2);
                transition:transform .18s, color .15s;}
  .group.open .car{transform:rotate(90deg);color:var(--violet);}
  .count{font-family:"Cascadia Code","Consolas",ui-monospace,monospace;
         font-size:12px;color:var(--muted);white-space:nowrap;}
  .bar{grid-column:1 / -1;height:3px;background:var(--line-soft);border-radius:2px;
       overflow:hidden;margin-bottom:14px;}
  .bar > i{display:block;height:100%;background:linear-gradient(90deg,var(--violet-dim),var(--violet));
           opacity:.85;border-radius:2px;}

  /* ---- records ---- */
  .records{display:none;padding:2px 4px 22px;}
  .group.open .records{display:block;}
  .card{
    background:var(--surface);border:1px solid var(--line-soft);border-radius:9px;
    padding:16px 18px;margin:0 0 12px;
  }
  .card .content > div{margin:0;}
  .card .content{font-size:15px;color:var(--text);white-space:pre-wrap;word-break:break-word;}
  .card .content div{unicode-bidi:plaintext;}
  .meta{
    display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;
    margin-top:13px;padding-top:11px;border-top:1px solid var(--line-soft);
    font-family:"Cascadia Code","Consolas",ui-monospace,monospace;font-size:11px;
    color:var(--muted-2);
  }
  .meta .k{color:var(--muted-2);}
  .meta .v{color:var(--muted);}
  .tag{border:1px solid var(--line);border-radius:3px;padding:2px 7px;color:var(--muted);}
  .tag.root{color:var(--root);border-color:#264a44;}
  .tag.title{color:var(--violet);border-color:var(--violet-dim);max-width:42ch;
             overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
  .chip{cursor:pointer;color:var(--violet);border:1px solid var(--violet-dim);
        border-radius:3px;padding:2px 7px;}
  .chip:hover{background:var(--violet-bg);}
  .more{
    display:block;width:100%;text-align:center;background:var(--surface-2);
    border:1px dashed var(--line);color:var(--muted);border-radius:7px;
    padding:10px;cursor:pointer;font-family:"Cascadia Code","Consolas",ui-monospace,monospace;
    font-size:12px;margin-top:4px;
  }
  .more:hover{border-color:var(--violet-dim);color:var(--violet);}
  .flatsub{font-family:"Cascadia Code","Consolas",ui-monospace,monospace;font-size:11px;
           color:var(--violet);letter-spacing:.06em;margin:0 0 6px;}
  .empty{color:var(--muted);padding:40px 4px;font-size:14px;}
  mark{background:var(--violet-bg);color:var(--violet);border-radius:2px;padding:0 1px;}
  :focus-visible{outline:2px solid var(--violet-dim);outline-offset:2px;}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="ro">read-only</span>
    <p class="eyebrow">N.H — The Log</p>
    <h1>The mirror</h1>
    <p class="sub">Every piece kept, grouped by where it came from. Each seam's width is its real size — the shape of the store at a glance. Nothing on this page can edit anything.</p>
    <p class="note">Groups are provenance for now. Real subjects arrive with the engine; until then this reads the store as it stands.</p>
    <div class="stat-row">
      <div class="stat"><b id="s-total">0</b><span>records</span></div>
      <div class="stat"><b id="s-groups">0</b><span>groups</span></div>
      <div class="stat"><b id="s-gen" style="font-size:12px;line-height:2.6;">—</b><span>generated</span></div>
    </div>
  </header>

  <div class="search">
    <input id="q" type="text" placeholder="Search content across the whole store…" autocomplete="off" spellcheck="false">
    <div class="searchmeta" id="qmeta"></div>
  </div>

  <main id="main"></main>
</div>

<script type="application/json" id="data">/*__DATA__*/</script>
<script>
(function(){
  "use strict";
  const DATA = JSON.parse(document.getElementById("data").textContent);
  const main = document.getElementById("main");
  const PAGE = 200;

  document.getElementById("s-total").textContent  = DATA.total.toLocaleString();
  document.getElementById("s-groups").textContent = DATA.group_count.toLocaleString();
  document.getElementById("s-gen").textContent    = (DATA.generated || "—").replace("T", "  ");

  const maxCount = DATA.groups.reduce((m,g)=>Math.max(m,g.count), 1);

  // index by id for point-back resolution (latent until re_reads exist)
  const byId = new Map();
  DATA.groups.forEach(g => g.records.forEach(r => byId.set(r.id, {rec:r, subject:g.subject})));

  function shortId(id){ return id ? id.slice(0,8) : "—"; }

  function contentEl(text){
    const c = document.createElement("div");
    c.className = "content";
    const lines = String(text).split("\n");
    lines.forEach(line => {
      const d = document.createElement("div");
      d.setAttribute("dir","auto");
      d.textContent = line.length ? line : "\u00a0";
      c.appendChild(d);
    });
    return c;
  }

  function metaEl(rec){
    const m = document.createElement("div");
    m.className = "meta";

    if (rec.source_title){
      const t = document.createElement("span");
      t.className = "tag title";
      t.setAttribute("dir","auto");
      t.title = rec.source_title;
      t.textContent = rec.source_title;
      m.appendChild(t);
    }

    if (Array.isArray(rec.re_reads) && rec.re_reads.length){
      const k = document.createElement("span"); k.className="k"; k.textContent="re-reads"; m.appendChild(k);
      rec.re_reads.forEach(rid => {
        const chip = document.createElement("span");
        chip.className = "chip mono";
        chip.textContent = shortId(rid);
        chip.title = "jump to " + rid;
        chip.addEventListener("click", e => { e.stopPropagation(); locate(rid); });
        m.appendChild(chip);
      });
    } else {
      const root = document.createElement("span");
      root.className = "tag root";
      root.textContent = "root";
      m.appendChild(root);
    }

    const ts = document.createElement("span");
    ts.className = "v"; ts.textContent = rec.timestamp || "—";
    m.appendChild(ts);

    const id = document.createElement("span");
    id.className = "v"; id.title = rec.id; id.textContent = shortId(rec.id);
    m.appendChild(id);

    return m;
  }

  function cardEl(rec, highlight){
    const card = document.createElement("article");
    card.className = "card";
    card.id = "rec-" + rec.id;
    const c = contentEl(rec.content);
    if (highlight) markInside(c, highlight);
    card.appendChild(c);
    card.appendChild(metaEl(rec));
    return card;
  }

  // ---- group browse view ----
  function renderGroups(){
    main.innerHTML = "";
    if (!DATA.groups.length){
      const e = document.createElement("p"); e.className="empty";
      e.textContent = "The store is empty."; main.appendChild(e); return;
    }
    DATA.groups.forEach(g => main.appendChild(groupEl(g)));
  }

  function groupEl(g){
    const wrap = document.createElement("section");
    wrap.className = "group";

    const seam = document.createElement("div");
    seam.className = "seam";
    const subj = document.createElement("div");
    subj.className = "subject";
    subj.innerHTML = '<span class="car">▸</span>';
    const label = document.createElement("span");
    label.setAttribute("dir","auto");
    label.textContent = g.subject;
    subj.appendChild(label);
    const cnt = document.createElement("div");
    cnt.className = "count";
    cnt.textContent = g.count.toLocaleString() + (g.count === 1 ? " entry" : " entries");
    seam.appendChild(subj); seam.appendChild(cnt);

    const bar = document.createElement("div");
    bar.className = "bar";
    const fill = document.createElement("i");
    fill.style.width = Math.max(2, (g.count / maxCount) * 100) + "%";
    bar.appendChild(fill);

    const recs = document.createElement("div");
    recs.className = "records";
    let shown = 0;

    function paint(){
      const slice = g.records.slice(shown, shown + PAGE);
      slice.forEach(r => recs.appendChild(cardEl(r, null)));
      shown += slice.length;
      const old = recs.querySelector(".more");
      if (old) old.remove();
      if (shown < g.records.length){
        const more = document.createElement("button");
        more.className = "more";
        more.textContent = "Show more — " + (g.records.length - shown).toLocaleString() + " remaining";
        more.addEventListener("click", paint);
        recs.appendChild(more);
      }
    }

    seam.addEventListener("click", () => {
      const opening = !wrap.classList.contains("open");
      wrap.classList.toggle("open");
      if (opening && shown === 0) paint();
    });

    wrap.appendChild(seam); wrap.appendChild(bar); wrap.appendChild(recs);
    return wrap;
  }

  // ---- search view ----
  function renderSearch(term){
    const t = term.toLowerCase();
    const hits = [];
    for (const g of DATA.groups){
      for (const r of g.records){
        if ((r.content || "").toLowerCase().includes(t)){
          hits.push({rec:r, subject:g.subject});
          if (hits.length > 2000) break;
        }
      }
      if (hits.length > 2000) break;
    }
    document.getElementById("qmeta").textContent =
      hits.length ? (hits.length > 2000 ? "2000+ matches (showing first 2000)" : hits.length.toLocaleString() + " match" + (hits.length===1?"":"es"))
                  : "no matches";
    main.innerHTML = "";
    if (!hits.length){
      const e = document.createElement("p"); e.className="empty";
      e.textContent = "Nothing in the store contains that."; main.appendChild(e); return;
    }
    let shown = 0;
    function paint(){
      const slice = hits.slice(shown, shown + PAGE);
      slice.forEach(h => {
        const sub = document.createElement("p"); sub.className="flatsub";
        sub.setAttribute("dir","auto"); sub.textContent = h.subject;
        main.appendChild(sub);
        main.appendChild(cardEl(h.rec, term));
      });
      shown += slice.length;
      const old = main.querySelector(".more");
      if (old) old.remove();
      if (shown < hits.length){
        const more = document.createElement("button");
        more.className = "more";
        more.textContent = "Show more — " + (hits.length - shown).toLocaleString() + " remaining";
        more.addEventListener("click", paint);
        main.appendChild(more);
      }
    }
    paint();
  }

  function markInside(container, term){
    const t = term.toLowerCase();
    container.querySelectorAll("div").forEach(d => {
      const txt = d.textContent;
      const i = txt.toLowerCase().indexOf(t);
      if (i < 0) return;
      d.textContent = "";
      d.appendChild(document.createTextNode(txt.slice(0, i)));
      const m = document.createElement("mark");
      m.textContent = txt.slice(i, i + term.length);
      d.appendChild(m);
      d.appendChild(document.createTextNode(txt.slice(i + term.length)));
    });
  }

  function locate(id){
    const found = byId.get(id);
    if (!found){ alert("That id isn't in the store."); return; }
    document.getElementById("q").value = "";
    renderGroups();
    // open the group containing it, then scroll
    const sections = main.querySelectorAll(".group");
    DATA.groups.forEach((g, idx) => {
      if (g.subject === found.subject){
        const sec = sections[idx];
        sec.querySelector(".seam").click();
        setTimeout(() => {
          const card = document.getElementById("rec-" + id);
          if (card){ card.scrollIntoView({behavior:"smooth", block:"center"});
                     card.style.borderColor = "var(--violet-dim)"; }
        }, 60);
      }
    });
  }

  let timer = null;
  const q = document.getElementById("q");
  q.addEventListener("input", () => {
    clearTimeout(timer);
    const v = q.value.trim();
    timer = setTimeout(() => {
      if (v.length === 0){ document.getElementById("qmeta").textContent=""; renderGroups(); }
      else if (v.length >= 2){ renderSearch(v); }
    }, 160);
  });

  renderGroups();
})();
</script>
</body>
</html>
"""


def main() -> None:
    payload = _build_payload()
    html = _render_html(payload)
    OUT_FILE.write_text(html, encoding="utf-8")
    size_mb = OUT_FILE.stat().st_size / (1024 * 1024)
    print(f"nh_log.html written: {OUT_FILE}")
    print(f"  {payload['total']:,} records across {payload['group_count']} groups  ·  {size_mb:.1f} MB")
    print(f"  open it in a browser to read the store.")


if __name__ == "__main__":
    main()
