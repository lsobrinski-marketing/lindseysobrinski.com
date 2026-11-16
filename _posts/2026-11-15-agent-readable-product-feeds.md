---
title: "Agent-readable product feeds: getting your catalog ready for AI checkout"
seo_title: "Agent-readable product feeds"
date: 2026-11-15 09:00:00 -0600
category: ecommerce-seo
hero: /assets/img/blog/agent-readable-product-feeds.png
image: /assets/img/blog/agent-readable-product-feeds.png
hero_title: "Feed the|machine"
hero_motif: nodes
hero_alt: "A product catalog on the left flowing as clean structured rows into a central shopping-graph hub, which feeds several AI shopping answer panels on the right, with one product that has incomplete rows greyed out and dropped before it reaches the hub."
tags: [AI commerce, product feed, Google Merchant Center, structured product data, AI shopping, AEO]
description: "Getting your catalog found and bought in AI starts with the feed. The Merchant Center attributes and structured data AI shopping reads, and how to prove it pays."
faq:
  - q: What product feed do AI shopping agents read?
    a: >-
      For Google's AI surfaces, the Google Merchant Center feed. AI Mode, AI
      Overviews, and Gemini build shopping answers from the Shopping Graph, and
      your Merchant Center feed is the direct input to it. Google's AI does not
      hold a separate understanding of your store, it reads the graph, so a
      complete, approved, current feed is what lets those surfaces represent and
      recommend your products at all.
  - q: Which Merchant Center attributes matter for AI shopping?
    a: >-
      The baseline is GTIN, MPN, and brand, accurate real-time price and
      availability, specific titles, the correct Google product category, and
      clean images. On top of that, Google added attributes aimed at AI surfaces,
      product highlights, structured product details, richer variant data,
      product-level questions and answers, linked documents such as manuals, and a
      popularity rank. The baseline gets you represented, the AI attributes help
      you get chosen for specific questions.
  - q: Do I need structured data on the page if I already have a feed?
    a: >-
      Yes, and it has to match. The feed is the catalog the engine queries, and
      the page markup is what an engine reads when it arrives at your product
      page. Google cross-checks the feed, the on-page Product schema, and the
      displayed page, so a price or availability that differs between them reads
      as risk and costs you the placement. One source of truth, exposed in both
      the feed and the page.
  - q: How do I measure revenue from AI shopping?
    a: >-
      Track presence and citation share per engine as the leading indicator,
      whether your products appear and whether that share is rising, then prove
      the revenue with a holdout. AI-referred traffic is small and tracked late,
      so the attributed number over-credits it. A geo or audience holdout tells
      you whether the feed work created sales or only coincided with them.
---

AI shopping agents do not browse your store, they query your catalog. Getting found and bought in AI starts with a complete, approved product feed: GTINs, accurate price and availability, specific titles, and the newer AI attributes, matched by on-page structured data. Build the feed first, then prove the revenue with a holdout. The feed is the catalog the machine reads; your pretty page is not.

## Why does the feed decide whether AI shopping finds you?

Because the engines are not reading your store the way you built it. Google's AI shopping surfaces, AI Mode, AI Overviews, and Gemini, ground their product answers in the Shopping Graph, a product-data layer Google populates from Merchant Center feeds. Google's AI does not keep a separate model of your catalog. It reads the graph, and your feed is the direct input. A feed that is incomplete, stale, disapproved, or missing identifiers leaves your products in the graph in a form the AI cannot represent, so it reaches for a competitor it can read.

This is the commerce edge of the same problem the site covers in [your JavaScript site is invisible to AI crawlers](/blog/your-javascript-site-is-invisible-to-ai-crawlers/) and [an AI agent will not recommend what it cannot verify](/blog/ai-agents-wont-recommend-what-they-cant-verify/): the facts a machine needs are present for human eyes and absent for the machine. The difference is that in commerce, the machine-readable version is a structured feed, and most brands treat it as a Google Shopping chore rather than the thing that decides AI visibility.

## What goes in an agent-readable feed?

Two layers. The baseline is non-negotiable: GTIN, MPN, and brand so the product is identifiable, accurate real-time price and availability, specific descriptive titles, the correct Google product category and product type, and clean high-resolution images. Miss these and nothing else matters, because the product is either disapproved or unreadable.

The second layer is the set of attributes Google added specifically for its AI surfaces, and it is where getting chosen is won rather than just getting listed. Product highlights, short selling-point fragments. Structured product details, specifications grouped as name-and-value pairs. Richer variant data, so the engine reads the difference between a size and a finish instead of guessing from the title. Product-level questions and answers. Linked documents, such as a crawlable manual, that the engine can use to answer a detailed question. And a popularity rank based on actual sales. These let an AI surface answer a specific shopper question with your product instead of summarizing past it. Getting the feed to this standard is the catalog outcome that the whole [AI-commerce](/seo-aeo-geo/ai-commerce/) wedge turns on.

## Why does the page have to match the feed?

Because Google cross-checks them, and a mismatch reads as doubt. The feed is the catalog the engine queries. The on-page Product schema, name, brand, price, availability, GTIN, ratings, is what an engine reads when it arrives at the page. The displayed page is what a human sees. When the price in the feed, the price in the markup, and the price on the page disagree, the engine cannot tell which is true, and an answer engine that cannot verify a fact treats it as risk and skips you. One source of truth, exposed in both the feed and the page, is the whole discipline. The delivery promise is the sharpest case: the same [date a human needs to trust](/blog/shoppers-need-a-date-they-can-trust/) is the field an agent verifies, so you build it once and it serves both, which is also what decides whether [an AI agent can actually buy from you](/blog/can-an-ai-agent-buy-from-you/) when the shopper lands to check out.

## Reviews and the trust signals an agent checks

Ratings reach AI answers through product review feeds or an approved reviews aggregator, and review volume and recency matter. The trap is that your best reviews often live on a marketplace, disconnected from your own product. Connecting them with a [GTIN so AI knows those marketplace reviews are yours](/blog/gtin-connects-your-marketplace-reviews/), and exposing ratings through [review schema](/blog/review-schema-trust-signal/), is how earned trust counts where the engine reads. A product the engine can price, confirm in stock, and see corroborated by real ratings is a product it will stand behind. A product with none of that is one it skips even when it is the better item.

## How do you prove the feed work paid?

This is where the measurement proof layer earns the trust, and it is the reason to believe any of the above. AI-referred revenue is small today and tracked late, so the attributed number in a dashboard over-credits it: a shopper the AI named may have bought you anyway. Read that number and you will congratulate the feed for demand it only witnessed, the same failure as [platform ROAS grading its own homework](/blog/platform-roas-is-grading-its-own-homework/).

The honest read is two-part. Track presence and citation share per engine as the leading indicator, whether your products appear in the answer and whether that share is rising against competitors. Then prove the revenue with [a geo or audience holdout](/blog/how-to-run-a-geo-holdout-test/), so you know the feed work created sales rather than coinciding with them. Measurement is not a separate project bolted on at the end. It is what tells you which feed changes moved money, so you keep doing those.

## The 30-day feed-readiness order

Fix the baseline first, because nothing downstream counts until the feed is approved and current: identifiers, price, availability, titles, category, images, and a clean Merchant Center with no silent disapprovals. Second, reconcile the page to the feed, so the Product schema and the displayed facts agree with the catalog. Third, add the AI attributes, highlights, details, variants, Q and A, documents, popularity rank, on your highest-revenue products. Fourth, connect the reviews. Fifth, stand up the measurement so you can read presence and prove lift. Getting named in the answer at all is the authority layer in [why your brand is not in the AI answer](/blog/why-your-brand-is-not-in-the-ai-answer/); this is the catalog layer underneath it. So the question for your next sprint is not whether your product pages look good to a shopper. It is whether an AI surface, querying your feed right now, could read, verify, and recommend your catalog, and have you proven that being there sells anything?

This post sits in the [ecommerce SEO hub](/seo-aeo-geo/ecommerce-seo/) and under the [AI-commerce page](/seo-aeo-geo/ai-commerce/).

## Sources

- Google Search Central, Introduction to Product structured data and merchant listings (identifiers, price, availability, shipping, returns): [developers.google.com](https://developers.google.com/search/docs/appearance/structured-data/product)
- PPC Land, "8 Google Merchant Center attributes your feed needs for AI Mode," 2026 (highlights, details, variants, Q and A, documents, popularity rank): [ppc.land](https://ppc.land/8-google-merchant-center-attributes-your-feed-needs-for-ai-mode/)
