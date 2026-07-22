# lindseysobrinski.com

Static site built with Jekyll and served by GitHub Pages. Pushing to the default
branch triggers the build; there is no separate deploy step.

## Structure

```
_config.yml              site settings, author entity, plugins
_data/categories.yml     the 8 blog subcategories (single source of truth)
_layouts/
  default.html           <head>, Person schema, nav, footer
  lane.html              service lane: Service + Breadcrumb schema + FAQ
  post.html              blog post: auto outline, BlogPosting + Breadcrumb + FAQ
  category.html          category listing + CollectionPage schema
  page.html              plain page
_includes/
  nav.html  footer.html
  faq.html               renders visible FAQ *and* FAQPage schema from front matter
assets/css/site.css      all shared styles
_posts/                  blog posts, YYYY-MM-DD-slug.md
blog/index.html          blog home
blog/categories/*.html   one stub per category
seo-aeo-geo.md  paid-media.md  lifecycle.md  user-journey.md    the four lanes
geo.html  roas.html  scorecard.html                             standalone tools
llms.txt                 curated map for AI engines
```

## Adding a blog post

Create `_posts/YYYY-MM-DD-some-slug.md`:

```yaml
---
title: "The headline"
category: geo          # must match a slug in _data/categories.yml
tags: [optional, terms]
description: >-
  One or two sentences. Used as the meta description and the listing excerpt.
faq:
  - q: A real question a buyer would ask?
    a: >-
      A direct answer. Markdown works here.
---

Body in Markdown. Use ## and ### headings — the outline builds itself from them.
```

The outline and the FAQ are automatic. Write `##`/`###` headings and fill in
`faq:`, and the post gets its table of contents, its visible FAQ section, and
`BlogPosting` + `FAQPage` + `BreadcrumbList` schema. Set `toc: false` to skip the
outline on a short post.

## Lane page structure

Every lane renders the same four sections, in this order:

1. **Why it matters** — the Markdown body of the file.
2. **Tools** — from `tools:` in front matter. An entry with a `url` renders as a
   clickable tile; an entry without one renders as a visibly inert "In build"
   tile, so a planned tool never looks like a broken link.
3. **Further reading** — auto-populated from `blog_categories:`. Pulls the 5
   most recent posts across those categories and links to each category archive.
   Publishing a post makes it appear here with no edit to the lane page.
4. **FAQ** — from `faq:`, which drives both the visible section and the
   `FAQPage` schema. They cannot drift apart because there is one source.

```yaml
---
layout: lane
permalink: /your-lane/
title: Lane Title
eyebrow: Lane 05 — Short Label
lane_class: lane-seo      # lane-seo | lane-paid | lane-lifecycle | lane-journey
description: >-
  Meta description, also used in the Service schema.
lede: >-
  One-paragraph positioning statement under the H1.
blog_categories: [seo, aeo]
tools:
  - name: A Tool You Built
    url: /tool.html
    cta: Open it →
    blurb: What it does.
  - name: A Tool You Plan To Build
    blurb: What it will do.       # no url = renders as "In build"
faq:
  - q: A question?
    a: >-
      An answer.
---

Markdown body — this becomes the "why it matters" section.
```

The full front matter contract is also documented at the top of
`_layouts/lane.html`.

## Adding a blog category

1. Add an entry to `_data/categories.yml` (`slug`, `name`, `color`, `blurb`).
   `color` is one of `accent`, `good`, `purple`.
2. Create `blog/categories/<slug>.html` containing only:

```yaml
---
layout: category
category: <slug>
permalink: /blog/categories/<slug>/
---
```

The blog index and every category nav pick it up automatically.

## Local preview

Requires Ruby 3.x. macOS system Ruby (2.6) is too old for the `github-pages`
gem, so install a modern Ruby first (e.g. via Homebrew or rbenv), then:

```bash
bundle install
bundle exec jekyll serve
```

Preview runs at http://localhost:4000. This is optional — GitHub Pages builds
on push either way.

## Known follow-ups

- The three interactive tools (`geo.html`, `roas.html`, `scorecard.html`) are
  passthrough files with their own inline styles, so they do not show the shared
  site nav. Converting them to use `_layouts/default.html` would unify
  navigation but means untangling their self-contained `<style>` blocks.
- No OG images are set. Adding a default social share image would improve link
  previews.
