# Blog hero images

**Rule: every blog post gets a hero image.** Heroes are branded 1200×630 SVGs in
the site's house style (light gradient, category-colored left bar + pill, a 2-line
title, the "Lindsey Sobrinski / Growth that survives the measurement." wordmark, and
a concept graphic on the right). See any file in `assets/img/blog/*.svg`.

## Add a hero to a new post

After writing a post in `_posts/`, run from the site root:

```bash
python3 scripts/generate_hero.py _posts/2026-09-10-my-new-post.md
```

That writes `assets/img/blog/<slug>.svg` (the on-page hero) and `<slug>.png`
(the og:image social card), and inserts `hero:` and `image:` into the post's
front matter automatically.

### Make the title read well
The script derives the 2-line title from the post, but the cleanest result comes
from setting a short one in front matter:

```yaml
hero_title: "Two words|second line"   # "|" splits the two lines
hero_motif: funnel                     # optional: nodes | arcs | bars | funnel | orbit
```

Or pass them on the command line:

```bash
python3 scripts/generate_hero.py _posts/... --title "Two|words" --motif funnel --force
```

### Hand-drawn illustration instead of an abstract motif
Some posts deserve a bespoke diagram (see the existing heroes — the redirect fan,
the funnel with a leak, etc.). To supply one, save an SVG fragment at
`assets/img/blog/<slug>.diagram.svg` with elements positioned in the right region
(x 590–1110, y 160–500, using the category color, `#c0392b` red for the "problem"
accent, `#51607a` muted labels, `#dde7ee` guide lines). If that file exists the
script uses it verbatim instead of a generated motif.

## Requirements
- Python 3.
- ImageMagick (`convert`) for the PNG og:image. The SVG hero works without it;
  if `convert` is missing the script just skips the PNG and only sets `hero:`.

## Colors (kept in sync with `assets/css/site.css`)
ink `#1a2333` · muted `#51607a` · guide `#dde7ee` · problem-red `#c0392b`
Category colors: accent/blue `#1D6FA3` · good/green `#1e8e5a` · purple `#7a5ea8`
(pulled per-category from `_data/categories.yml`).
