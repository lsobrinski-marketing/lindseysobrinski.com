#!/usr/bin/env python3
"""
generate_hero.py — make a branded 1200x630 hero image for a blog post and wire
its front matter. Matches the house style used across the site's blog heroes.

USAGE
    python3 scripts/generate_hero.py _posts/2026-09-10-my-new-post.md

    # optional overrides
    python3 scripts/generate_hero.py _posts/... --title "Two|words" --motif funnel --force

WHAT IT DOES
    1. Reads the post's front matter (title / seo_title / category, plus optional
       `hero_title` and `hero_motif`).
    2. Writes  assets/img/blog/<slug>.svg   (the on-page hero; browsers use real fonts)
       and    assets/img/blog/<slug>.png   (the og:image social card; needs ImageMagick `convert`).
    3. Inserts `hero:` and `image:` into the post front matter if not already present.

HOUSE STYLE (kept in sync with assets/css/site.css)
    1200x630, diagonal light gradient bg, 10px left bar in the category color,
    a category pill, a 2-line title, the "Lindsey Sobrinski / Growth that survives
    the measurement." wordmark, and an abstract concept motif on the right.

BESPOKE DIAGRAMS
    For a hand-authored illustration instead of an abstract motif, drop an SVG
    fragment at assets/img/blog/<slug>.diagram.svg (elements positioned in the
    right region, x 590-1110, y 160-500). If that file exists it is used verbatim.

REQUIREMENTS
    Python 3. ImageMagick `convert` for the PNG (the SVG hero works without it).
    Run from the site root (the folder containing _posts/ and _data/).
"""
import os, re, sys, argparse, subprocess, hashlib

FONT = "'Segoe UI', system-ui, -apple-system, Helvetica, Arial, sans-serif"
INK="#1a2333"; MUTED="#51607a"; GUIDE="#dde7ee"; RED="#c0392b"; WHITE="#ffffff"; PILL="#eef4f8"
# category color-name -> hex (from site.css)
HEX={"accent":"#1D6FA3","good":"#1e8e5a","purple":"#7a5ea8"}
# fallback slug -> (Name, color-name) if _data/categories.yml can't be read
FALLBACK={
 "seo":("SEO","accent"),"aeo":("AEO","accent"),"geo":("GEO","purple"),
 "paid-media":("Paid Media","good"),"lifecycle":("Lifecycle","good"),
 "subscriptions":("Subscriptions","good"),"user-journey":("User Journey","purple"),
 "conversion-optimization":("Conversion Optimization","accent"),
 "technical-seo":("Technical SEO","accent"),"ecommerce-seo":("Ecommerce SEO","good"),
 "content-seo":("Content SEO","purple"),"local-seo":("Local SEO","good"),"ai":("AI","purple"),
}

def load_categories():
    path="_data/categories.yml"
    cats=dict(FALLBACK)
    if os.path.exists(path):
        try:
            import yaml
            for c in yaml.safe_load(open(path,encoding="utf-8")) or []:
                if c.get("slug"): cats[c["slug"]]=(c.get("name",c["slug"]).upper() if False else c.get("name",c["slug"]), c.get("color","accent"))
        except Exception:
            # tiny regex fallback
            slug=name=color=None
            for ln in open(path,encoding="utf-8"):
                m=re.match(r"\s*-\s*slug:\s*(\S+)",ln)
                if m: slug=m.group(1); continue
                m=re.match(r"\s*name:\s*(.+)",ln)
                if m and slug: name=m.group(1).strip()
                m=re.match(r"\s*color:\s*(\S+)",ln)
                if m and slug: cats[slug]=(name or slug, m.group(1).strip())
    return cats

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def T(x,y,s,size=15,weight="700",fill=MUTED,anchor="start",ls=None):
    l=f' letter-spacing="{ls}"' if ls is not None else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}"{l}>{esc(s)}</text>'

def fit_size(line, maxw=486, base=46):
    # approximate width of 800-weight text ~0.60*size per char; scale down long lines
    if not line: return base
    est=len(line)*0.60
    return max(24, min(base, int(maxw/est)))

def title_lines(raw):
    # raw may contain "|" to force the split; else wrap to two short lines
    if "|" in raw:
        a,b=raw.split("|",1); return a.strip(), b.strip()
    words=raw.split()
    l1=[]; n=0
    for w in words:
        if n and n+len(w)+1>15: break
        l1.append(w); n+=len(w)+1
    l2=words[len(l1):]
    return " ".join(l1), " ".join(l2)

# ---------- abstract motifs (right region x 590-1110, y 160-500) ----------
def m_nodes(c):
    pts=[(660,240),(820,200),(1000,250),(760,360),(950,400),(620,410)]
    s=[f'<line x1="{pts[a][0]}" y1="{pts[a][1]}" x2="{pts[b][0]}" y2="{pts[b][1]}" stroke="{GUIDE}" stroke-width="3"/>'
       for a,b in [(0,1),(1,2),(0,3),(3,4),(2,4),(3,5),(0,5)]]
    for i,(x,y) in enumerate(pts):
        col=RED if i==2 else c
        s.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{WHITE}" stroke="{col}" stroke-width="4"/>')
    return "\n".join(s)

def m_arcs(c):
    s=[f'<circle cx="850" cy="315" r="{r}" fill="none" stroke="{GUIDE}" stroke-width="14"/>' for r in (60,110,160)]
    s.append(f'<path d="M 850 155 A 160 160 0 0 1 1000 260" fill="none" stroke="{c}" stroke-width="14" stroke-linecap="round"/>')
    s.append(f'<circle cx="850" cy="315" r="16" fill="{RED}"/>')
    return "\n".join(s)

def m_bars(c):
    s=[f'<line x1="620" y1="430" x2="1080" y2="430" stroke="{GUIDE}" stroke-width="3"/>']
    for i,h in enumerate((120,180,150,240)):
        x=660+i*100; y=430-h
        s.append(f'<rect x="{x}" y="{y}" width="66" height="{h}" rx="4" fill="{c}"/>')
    s.append(f'<line x1="640" y1="210" x2="1060" y2="210" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7 7"/>')
    return "\n".join(s)

def m_funnel(c):
    return (f'<path d="M 650 200 L 1050 200 L 955 285 L 745 285 Z" fill="{c}" opacity="0.30"/>'
            f'<path d="M 745 295 L 955 295 L 890 380 L 810 380 Z" fill="{c}" opacity="0.58"/>'
            f'<path d="M 810 390 L 890 390 L 858 470 L 842 470 Z" fill="{c}"/>')

def m_orbit(c):
    import math
    s=[f'<circle cx="850" cy="315" r="120" fill="none" stroke="{GUIDE}" stroke-width="3"/>',
       f'<circle cx="850" cy="315" r="34" fill="{c}"/>']
    for i,a in enumerate((20,140,255)):
        x=850+120*math.cos(math.radians(a)); y=315+120*math.sin(math.radians(a))
        col=RED if i==2 else c
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" fill="{WHITE}" stroke="{col}" stroke-width="4"/>')
    return "\n".join(s)

MOTIFS={"nodes":m_nodes,"arcs":m_arcs,"bars":m_bars,"funnel":m_funnel,"orbit":m_orbit}

def pick_motif(slug, override):
    if override and override in MOTIFS: return override
    keys=sorted(MOTIFS)
    h=int(hashlib.md5(slug.encode()).hexdigest(),16)
    return keys[h % len(keys)]

def build_svg(label, color, t1, t2, diagram):
    pw=round(len(label)*12.2+40); pcx=72+pw/2
    s1=fit_size(t1); s2=fit_size(t2); size=min(s1,s2)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7fafc"/><stop offset="1" stop-color="#e8f0f6"/></linearGradient></defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect x="0" y="0" width="10" height="630" fill="{color}"/>
  <rect x="72" y="70" rx="20" ry="20" width="{pw}" height="40" fill="{PILL}"/>
  {T(pcx,96,label,18,"800",color,"middle",1.5)}
  {T(72,176,t1,size,"800",INK,"start",-0.5)}
  {T(72,176+58,t2,size,"800",INK,"start",-0.5)}
  {T(72,540,"Lindsey Sobrinski",26,"800",INK,"start",-0.3)}
  {T(72,568,"Growth that survives the measurement.",17,"600",MUTED)}
  {diagram}
</svg>'''

def read_front_matter(text):
    m=re.match(r"^---\n(.*?)\n---\n",text,re.S)
    fm=m.group(1) if m else ""
    def g(key):
        mm=re.search(rf"^{key}:\s*(.+)$",fm,re.M)
        if not mm: return None
        v=mm.group(1).strip().strip('"').strip("'")
        return v
    return fm, g

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("post")
    ap.add_argument("--title", help='override title, "line1|line2"')
    ap.add_argument("--motif", help="nodes|arcs|bars|funnel|orbit")
    ap.add_argument("--force", action="store_true", help="overwrite existing hero front matter/images")
    a=ap.parse_args()

    if not os.path.exists(a.post): sys.exit(f"post not found: {a.post}")
    text=open(a.post,encoding="utf-8").read()
    fm,g=read_front_matter(text)
    slug=re.sub(r"^\d{4}-\d{2}-\d{2}-","",os.path.basename(a.post))[:-3]
    cat=g("category")
    if not cat: sys.exit("post has no `category:` in front matter")
    cats=load_categories()
    label,colorname=cats.get(cat,(cat.replace("-"," ").upper(),"accent"))
    label=label.upper(); color=HEX.get(colorname,HEX["accent"])

    raw_title=a.title or g("hero_title") or g("seo_title") or g("title") or slug
    t1,t2=title_lines(raw_title)

    diagram_file=f"assets/img/blog/{slug}.diagram.svg"
    if os.path.exists(diagram_file):
        diagram=open(diagram_file,encoding="utf-8").read()
    else:
        motif=pick_motif(slug, a.motif or g("hero_motif"))
        diagram=MOTIFS[motif](color)

    os.makedirs("assets/img/blog",exist_ok=True)
    svg_path=f"assets/img/blog/{slug}.svg"; png_path=f"assets/img/blog/{slug}.png"
    open(svg_path,"w",encoding="utf-8").write(build_svg(label,color,t1,t2,diagram))
    print("wrote",svg_path)

    # PNG for og:image (best effort)
    try:
        subprocess.run(["convert","-background","white","-density","144",svg_path,"-resize","1200x630",png_path],
                       check=True, capture_output=True)
        print("wrote",png_path)
        have_png=os.path.exists(png_path) and os.path.getsize(png_path)>3000
    except Exception as e:
        have_png=False; print("PNG skipped (ImageMagick `convert` not available):",e)

    # inject front matter after the category line, if missing
    if "hero:" in fm and not a.force:
        print("front matter already has hero: — leaving as is")
        return
    lines=text.split("\n"); out=[]; done=False
    for ln in lines:
        if re.match(r"^hero:\s",ln) or re.match(r"^image:\s",ln):  # drop existing on --force
            continue
        out.append(ln)
        if not done and re.match(r"^category:\s*\S+",ln):
            out.append(f"hero: /{svg_path}")
            if have_png: out.append(f"image: /{png_path}")
            done=True
    if done:
        open(a.post,"w",encoding="utf-8").write("\n".join(out)); print("updated front matter in",a.post)
    else:
        print("WARNING: no `category:` line found to anchor front-matter insert")

if __name__=="__main__":
    main()
