#!/usr/bin/env python3
"""Build ain3-starter-pack/data/world-manifest.json from ain3-starter-pack/world/*.md.

World game pipeline: participants' agents commit leaf notes into world/,
this script turns them into the graph manifest the viewer renders.
Leaf contract: flat .md, filename {namespace}-{slug}.md, frontmatter with
`namespace:`, body with [[wikilinks]]. Hubs: {namespace}-hub.md, index.md.
"""
import json, os, re, sys, math, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORLD = os.path.join(ROOT, "ain3-starter-pack", "world")
OUT = os.path.join(ROOT, "ain3-starter-pack", "data", "world-manifest.json")

NAMESPACES = ["technical", "market", "people", "concept"]
CLUSTER = {  # quadrant centers for deterministic layout
    "technical": (-420, -280), "market": (420, -280),
    "people": (-420, 280), "concept": (420, 280), "hub": (0, 0),
}
CATEGORIES = [
    {"id": "technical", "label": "артефакты", "description": "Инструменты, структуры и механики из лекций и практик."},
    {"id": "market", "label": "экономика", "description": "Бизнес-ценность, кейсы, критерии выбора процессов."},
    {"id": "people", "label": "люди", "description": "Спикеры, участники и персонажи разборов."},
    {"id": "concept", "label": "рамки", "description": "Определения и методологические рамки программы."},
    {"id": "hub", "label": "ядро", "description": "Индексные узлы кластеров."},
]

WIKILINK = re.compile(r"\[\[([^\]\|#]+)")

def parse(path):
    text = open(path, encoding="utf-8").read()
    fm = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
            for line in parts[1].splitlines():
                m = re.match(r"^(\w+):\s*(.+)$", line.strip())
                if m:
                    fm[m.group(1)] = m.group(2).strip().strip('"')
    h1 = re.search(r"^#\s+(.+)$", body, re.M)
    title = h1.group(1).strip() if h1 else os.path.basename(path)[:-3]
    prose = re.sub(r"^#.*$", "", body, flags=re.M)
    prose = re.sub(r"\[\[([^\]]+)\]\]", r"\1", prose)
    prose = re.sub(r"[*_`>#]|^- ", "", prose, flags=re.M).strip()
    first = re.split(r"(?<=[.!?])\s+", prose.replace("\n", " "))
    summary = " ".join(first[:2]).strip()[:260]
    links = [l.strip() for l in WIKILINK.findall(text)]
    return fm, title, summary, links

def main():
    files = sorted(f for f in os.listdir(WORLD) if f.endswith(".md") and f not in ("AGENTS.md", "README.md", "CLAUDE.md"))
    nodes, edges, seen_edges = [], [], set()
    by_ns = {ns: [] for ns in NAMESPACES}
    meta_nodes = {}

    for f in files:
        nid = f[:-3]
        fm, title, summary, links = parse(os.path.join(WORLD, f))
        ns = fm.get("namespace") or (nid.split("-")[0] if nid.split("-")[0] in NAMESPACES else "hub")
        if fm.get("type") == "hub" and nid != "index":
            kind = "hub"
        elif nid == "index":
            kind, ns = "index", "hub"
        else:
            kind = "leaf"
        meta_nodes[nid] = {"id": nid, "label": title, "category": ns if ns in NAMESPACES else "hub",
                           "summary": summary or title, "links": links, "kind": kind}
        if kind == "leaf" and ns in by_ns:
            by_ns[ns].append(nid)

    # layout: index center, hubs at cluster centers, leaves on rings
    for nid, n in meta_nodes.items():
        if n["kind"] == "index":
            n["x"], n["y"] = 0, 0
        elif n["kind"] == "hub":
            ns = nid.replace("-hub", "")
            cx, cy = CLUSTER.get(ns, (0, 0))
            n["x"], n["y"] = cx, cy
    for ns, ids in by_ns.items():
        cx, cy = CLUSTER[ns]
        count = max(len(ids), 1)
        for i, nid in enumerate(sorted(ids)):
            ang = 2 * math.pi * i / count - math.pi / 2
            r = 170 + 40 * (i % 2)
            meta_nodes[nid]["x"] = round(cx + r * math.cos(ang))
            meta_nodes[nid]["y"] = round(cy + r * math.sin(ang))

    ids = set(meta_nodes)
    for nid, n in meta_nodes.items():
        for target in n.pop("links"):
            if target in ids and target != nid:
                key = tuple(sorted((nid, target)))
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"source": nid, "target": target, "kind": "link"})
        n.pop("kind")
        nodes.append(n)

    manifest = {
        "meta": {
            "title": "AIN3 World Graph",
            "version": "1.0.0",
            "updated": datetime.date.today().isoformat(),
            "description": "Живой контекст-граф лабы: лекции и практики, разобранные агентами; листья коммитят участники.",
        },
        "categories": CATEGORIES,
        "nodes": nodes,
        "edges": edges,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print(f"world-manifest: {len(nodes)} nodes, {len(edges)} edges -> {os.path.relpath(OUT, ROOT)}")

if __name__ == "__main__":
    sys.exit(main())
