---
title: "An AI agent will not recommend what it cannot verify"
seo_title: "An AI agent won't recommend what it can't verify"
date: 2026-10-29 09:00:00 -0500
category: ecommerce-seo
toc: false
hero: /assets/img/blog/ai-agents-wont-recommend-what-they-cant-verify.svg
image: /assets/img/blog/ai-agents-wont-recommend-what-they-cant-verify.png
hero_title: "Verify, then|recommend"
hero_motif: nodes
hero_alt: "An AI shopping agent confirming four machine-readable fields on one product, price, stock, delivery date, and returns, and recommending it, while a second product whose fields are locked in images and late-loading scripts is passed over."
tags: [AI shopping agents, structured product data, AEO, ecommerce, product schema, AI commerce]
description: "An AI shopping agent recommends what it can verify: machine-readable price, stock, delivery date, and returns. If it cannot confirm them, you are out."
faq:
  - q: What structured data do AI shopping agents read?
    a: >-
      The product and offer data exposed in your HTML and your product feed:
      price, availability, and shipping details through Product and Offer markup,
      and return terms through merchant return policy markup. These are the same
      standardized fields search engines already read, published in a form a
      machine can parse rather than buried in images or marketing copy.
  - q: Why is my product not recommended by ChatGPT or Gemini shopping even though it ranks on Google?
    a: >-
      Because ranking and being recommended are different tests. A rank means a
      page was relevant enough to list. A recommendation means an agent could
      verify your price, stock, delivery date, and return terms and was willing
      to stand behind them. If those fields are not machine-readable, you can
      rank for a human and still be unverifiable to an agent, so it recommends a
      competitor it can confirm.
  - q: Do AI agents read my product feed or my product page?
    a: >-
      Both, and they should agree. The feed is the structured catalog an agent
      can query directly; the product page carries the same facts in its markup
      for an agent that arrives there. The failure mode is a feed and a page that
      disagree, or a page whose real price and stock only appear after JavaScript
      runs, which the agent may never execute.
  - q: How do I show in-stock status and delivery date to an AI agent?
    a: >-
      Expose them as structured data in the initial HTML, not as text painted in
      by a script or baked into an image. Availability and shipping details
      belong in your Product and Offer markup and in your feed, kept current, so
      the single source of truth a human reads on the page is the same one the
      agent can verify.
---

An AI shopping agent recommends what it can verify. That means a machine-readable, current price, in-stock status, a concrete delivery date, and clear return terms, exposed as structured data in the initial HTML, not rendered later by JavaScript. If an agent cannot confirm those four, it recommends the competitor it can.

## What's in this piece

- Why an agent queries your store rather than browsing it
- The four fields an agent has to verify before it will name you
- Why most product pages fail the check
- The machine-readable layer that passes it
- The delivery promise a human and an agent both need
- How to see what an agent sees today, and the fix order

## The agent does not browse your store, it queries it

Getting cited by an AI assistant was step one. Getting an agent to complete a checkout was step two, and we covered whether [an AI agent can actually buy from you](/blog/can-an-ai-agent-buy-from-you/). This is step three, and it comes before both: whether the agent will put you on the shortlist in the first place. It will not, unless it can verify you.

Start with how an agent reads a store, because it is not how a human does. A person lands on a product page, lets the images and scripts paint in, scans the marketing copy, and infers that the item is in stock and will arrive soon. An agent does none of that. It queries your data. It pulls the structured facts from your feed and your page markup and checks them against the shopper's request. It is not reading your persuasion. It is reading your fields, and if the fields are not there in a form it can parse, as far as the agent is concerned the facts do not exist. The agent is not evaluating whether your product is good. It is evaluating whether your product is confirmable, and those are different tests.

## The four fields an agent has to verify

Before an agent will name your product, it has to confirm four things, and each one is a go or a no-go.

Price, current and exact. An agent cannot recommend a product whose price it cannot read, because price is the first thing the shopper is comparing. Availability, meaning real in-stock status. Recommending an out-of-stock item is the one mistake an agent is built hardest to avoid, so an unconfirmable stock status is treated as a risk and skipped. Delivery date, concrete rather than a vague "ships fast." If the shopper asked for something by a date, an agent needs a date it can check against that request, not a marketing phrase. Return terms, clear and parseable, because returns are part of how the agent weighs the risk of the purchase it is about to recommend.

Miss any one of the four and the agent does not lower your ranking a little. It removes you from consideration, because it cannot stand behind a recommendation it cannot verify. The bar is not "be the best option." The bar is "be a fully confirmable option," and most stores clear it for humans and fail it for machines.

## Why most product pages fail the check

The reason most pages fail is not that the information is missing. It is that the information is in a form a human can see and a machine cannot read. The price is correct, but it is painted in by a script that runs after the initial page loads. The delivery promise is right there, inside an image banner. The return policy is real, but it lives three clicks away in a paragraph of prose, not as structured data. The stock status updates live in a widget that an agent, fetching the raw HTML, never executes.

This is the same failure that makes a [JavaScript-rendered site invisible to AI crawlers](/blog/your-javascript-site-is-invisible-to-ai-crawlers/), applied to the exact fields a purchase turns on. A crawler that does not run your JavaScript sees an empty shell where your price and stock should be. An agent querying that page sees the same empty shell. The page looks complete to you because your browser does the rendering work. The agent does not do that work, so it sees a product it cannot confirm and moves on. The trust signals are all present. They are just not readable, which to a machine is the same as absent, and is another face of the [source-of-truth gap](/blog/the-source-of-truth-gap/): the answer gets built from whatever the machine can actually read.

## The machine-readable layer that passes the check

Passing the check means publishing the four fields as structured data in the initial HTML, and keeping your feed in agreement with it. These are not exotic formats. They are the same standardized product fields search engines already consume.

Price and availability belong in your Product and Offer markup, the merchant-listing structured data that Google and other engines already read, in [Google's merchant listing documentation](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing). Shipping and delivery details belong in the shipping fields of that same markup, so a delivery date is a value an agent can read rather than a phrase it has to interpret. Return terms belong in merchant return policy markup, the [MerchantReturnPolicy structured data Google documents](https://developers.google.com/search/docs/appearance/structured-data/return-policy), so the return window is a field, not a buried paragraph. The full product structured-data reference, including how these pieces fit together, is in [Google's product structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/product).

The point is not to chase a rich result in Google. It is that the machine-readable layer you build for search is the same layer an agent verifies against, and the feed is the catalog it can query directly. Build the markup and the feed once, keep them current, and make sure they agree with each other and with the page, and you have made your product confirmable to any machine that asks. Leave the facts in images and late-loading scripts, and you have built a store for human eyes that a machine has to skip.

## The delivery promise a human and an agent both need

There is one field where the human problem and the machine problem are the same problem, and solving it once serves both. Shoppers do not need the cheapest shipping. They need [a delivery date they can trust](/blog/shoppers-need-a-date-they-can-trust/), because an uncertain arrival is the thing that kills a purchase. An agent needs that identical date, as a value it can verify against the shopper's deadline.

So the delivery promise is not two projects, one for conversion-rate optimization and one for AI commerce. It is one source of truth that has to be both trustworthy to a person and readable to a machine. The brands that treat the delivery date as a real, current, structured field solve their human conversion problem and their agent-verification problem in a single move. The brands that leave it as a vague banner fail both audiences at once: the human hesitates, and the agent cannot confirm it, so neither one commits.

## How to see what an agent sees, and the fix order

You can check this today without any special tooling. Open your top product page, disable JavaScript, and reload. Whatever disappears, the price, the stock status, the delivery date, is exactly what an agent fetching your raw HTML fails to see. Then look at your product feed and confirm its price, availability, and delivery fields match what the page claims. Where the page and the feed disagree, the agent has no single truth to trust, and disagreement reads as risk.

The fix order over thirty days is short. First, get price and availability into static, machine-readable markup on your highest-revenue products, because those two fields are the hard go or no-go. Second, make the delivery date a real structured field rather than an image or a phrase. Third, expose return terms as structured data. Fourth, reconcile the feed and the pages so they tell one story. None of this is a redesign. It is moving facts you already have out of images and scripts and into the layer a machine reads. That same layer is where a [shared product identifier ties your off-site reviews back to your page](/blog/gtin-connects-your-marketplace-reviews/), so an agent can weigh your reputation, not just your facts.

So the question is not whether your store looks good to a shopper. It is whether an agent, querying your raw data right now, could confirm your price, your stock, your delivery date, and your returns. If it could not, which competitor is it recommending in your place?

## Sources

- Google Search Central, "Merchant listing (Product, Offer) structured data" (price, availability, and shipping fields): [developers.google.com](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- Google Search Central, "Merchant return policy (MerchantReturnPolicy) structured data": [developers.google.com](https://developers.google.com/search/docs/appearance/structured-data/return-policy)
- Google Search Central, "Introduction to Product structured data": [developers.google.com](https://developers.google.com/search/docs/appearance/structured-data/product)
