---
title: "Entities, not keywords: architecting a site search engines can actually model"
seo_title: "Entities, not keywords: architect for search"
date: 2026-07-11 09:00:00 -0500
hero: /assets/img/blog/entities-not-keywords.svg
image: /assets/img/blog/entities-not-keywords.png
category: seo
tags: [entity seo, topical authority, internal linking, structured data, pillar cluster, disambiguation]
description: "Search ranks entities and topics, not keyword strings. Most sites are a pile of unrelated pages. How to build one an engine can actually model."
faq:
  - q: What is the difference between a keyword and an entity?
    a: >-
      A keyword is a literal string a user types. An entity is a distinct thing — a person, product, concept, or place — that search engines track in a knowledge graph independent of how it's phrased. Ranking systems resolve queries to entities, then evaluate which pages best cover that entity and its relationships. Optimizing for strings gives you pages; optimizing for entities gives you coverage.
  - q: How do pillar and cluster pages actually help rankings?
    a: >-
      A pillar defines a topic broadly and links to focused cluster pages that each cover a subtopic in depth; the clusters link back. This structure tells an engine the pages are related and that your site treats the topic as a coherent whole, which consolidates authority instead of splitting it. It also prevents the thin, near-duplicate pages that keyword-by-keyword content produces.
  - q: Does structured data improve rankings on its own?
    a: >-
      Not directly, and anyone promising a ranking boost from schema alone is overselling it. Structured data is machine-readable confirmation of what a page is about and how its entities relate. It reduces ambiguity, qualifies pages for rich results, and makes your entity claims explicit rather than inferred. Treat it as evidence, not as a lever.
  - q: How do I know if my site has a keyword-cannibalization problem?
    a: >-
      Pull your Search Console query report and group pages by the queries they receive impressions for. Where two or more URLs trade impressions and clicks for the same query, and neither holds a stable position, you have cannibalization. Consolidate them into one authoritative page and redirect the rest.
  - q: Where should I start if my site is a pile of unrelated pages?
    a: >-
      Map your existing content to topics first, not keywords. Identify which entities you can credibly own given your evidence and expertise, then build the internal link graph so every page connects to the pillar that defines its topic. Fix the architecture before you publish anything new.
---
Open your top twenty organic landing pages. For each, write one sentence naming the single entity it is about. If you cannot, or if three of them name the same entity, you do not have a content problem. You have an architecture problem.

Most sites are not knowledge graphs. They are piles of pages, each written to catch a keyword string, stacked next to each other with no declared relationship. Search engines stopped rewarding that arrangement years ago. They resolve a query to an entity, consult what they already know about that entity, and then ask which site models the topic well enough to be trusted with the answer.

**A keyword is a string. An entity is a thing.** "Running shoes for flat feet," "best sneakers for overpronation," and "stability trainers" are three strings and one entity. If you built a separate page for each, you did not triple your coverage. You split one page's authority into thirds and asked the engine to choose between three weaker candidates. It usually picks none of them cleanly, and your own pages compete for the same impressions. That is cannibalization, and it is self-inflicted.

## Model the topic, not the query

Think of your site as a graph the engine has to reconstruct. Nodes are entities. Edges are the relationships you assert between them. The engine's job is to figure out what your site is *about* and whether it covers the territory. Your job is to make that reconstruction trivial.

The workhorse structure is the pillar and its clusters. A pillar page defines a topic broadly and honestly — what it is, what it involves, what questions surround it. Each cluster page takes one subtopic and goes deep. The pillar links down to every cluster; every cluster links back up. That reciprocal linking is not decoration. It is the signal that these pages are one body of work, and it consolidates authority onto the pillar instead of scattering it across near-duplicates.

**Internal linking is how you tell the engine what you're about.** External links are votes you don't fully control. Internal links are the votes you cast, and their anchor text and placement declare which pages you consider central. If your most important entity page has three internal links pointing at it and your privacy policy has forty, you have told the engine your privacy policy is the more important node. It believed you.

## Disambiguation is the tax you owe

Entities collide. "Mercury" is a planet, a metal, a car brand, and a Roman god. "Java" is a language, an island, and coffee. If your page does not make clear which entity it means, the engine has to guess, and a guess is a downgrade.

You disambiguate the way people do — with context. Co-occurring terms, named related entities, unambiguous headings, and links to and from other pages about the same subject. A page about the programming language that mentions the JVM, garbage collection, and Kotlin has told the engine which Java it means without ever saying "not the island." The test is simple: strip your title tag and read the body. If a reader could not tell which entity you mean, neither can the machine.

**Structured data is the confirmation, not the claim.** Schema.org markup lets you state, in a format machines parse without inference, that this page is about a specific product, that it has these attributes, that it relates to these other entities. Done well, it turns your implicit entity claims into explicit ones and qualifies you for rich results. Done as a bolt-on, it confirms nothing your content didn't already say. It is evidence you file, not a lever you pull — and if your markup and your visible content disagree, the markup loses.

The reason keyword-first content fails is structural, not tactical. Chasing individual queries produces one thin page per phrase, each covering a sliver, each competing with its siblings, none demonstrating the topical depth that earns trust. Chasing entities produces fewer, deeper pages that reinforce each other. The first approach rents position and re-rents it every algorithm update. The second earns it and compounds.

## What to do first

Do these in order, and don't publish anything new until the architecture is fixed.

**Map your topics.** Cluster every existing page by the entity it covers, not the keyword it targets. Where multiple pages cover one entity, mark them for consolidation.

**Pick the entities you can credibly own.** You cannot model a topic you have no evidence or expertise in. Choose the three to five entities where your firsthand authority is real, and concede the rest for now.

**Build the internal link graph deliberately.** For each owned entity, designate one pillar and wire every related page to it with descriptive anchor text. Redirect the cannibalizing duplicates into the pillar so their authority consolidates instead of competing.

Then add schema that confirms what the page already proves, and verify in Search Console that each entity now has one clear winner drawing its impressions.

Stop building pages for strings a user might type. Build a graph a machine can read, and the strings take care of themselves.
