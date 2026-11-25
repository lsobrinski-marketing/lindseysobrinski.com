---
layout: leader
published: false        # <-- flip to true (or delete this line) when the contributor says yes and approves
name: "First Last"
slug: first-last        # <-- must match the `author:` value in their guest post's front matter
role: "Their title, e.g. Head of SEO at Example"
headshot: /assets/img/leaders/first-last.jpg   # <-- add their approved portrait here
image: /assets/img/leaders/first-last.jpg   # social-share (og:image); point at the headshot above
linkedin: https://www.linkedin.com/in/their-handle
website: https://theirsite.com                 # optional; becomes Person.url if present
featured: true          # <-- the newest yes takes the spotlight slot on /leaders/
joined: 2026-11-19      # <-- date they went live; orders the spotlight by newest
bio_short: "One-line credential in their voice, ~25 words. Used in the byline box on their post."
same_as:
  - https://www.linkedin.com/in/their-handle
  - https://theirsite.com
  # - https://x.com/their-handle        # add every corroborating profile; each strengthens entity resolution
knows_about:
  - Topic one
  - Topic two
  - Topic three
---

Two or three short paragraphs of bio, in or approved by the contributor, written as prose.
Lead with what they are known for and the credential that makes their read worth citing, then
what they contributed here. Keep it factual: no invented titles, employers, or numbers.

HOW TO ADD A CONTRIBUTOR (delete this section in the real file):
1. Copy this file to _leaders/their-slug.md and fill every field above.
2. Drop their approved headshot in assets/img/leaders/their-slug.jpg.
3. In their guest post's front matter, add:  author: their-slug
   That rewires the post's byline, the author box, and the schema author to this page.
4. Set published: true here. They appear on /leaders/ and take the spotlight if featured: true.
