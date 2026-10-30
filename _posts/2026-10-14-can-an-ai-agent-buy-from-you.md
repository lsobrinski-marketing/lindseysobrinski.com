---
title: "Getting cited was step one. Can an AI agent actually buy from you?"
seo_title: "Can an AI agent actually buy from you?"
date: 2026-10-14 09:00:00 -0500
category: ecommerce-seo
hero: /assets/img/blog/can-an-ai-agent-buy-from-you.svg
image: /assets/img/blog/can-an-ai-agent-buy-from-you.png
hero_title: "Cited. Now|can it buy?"
hero_motif: nodes
tags: [ecommerce seo, ai agents, agentic commerce, product feed, structured data, holiday]
description: "Google and Shopify opened checkout to AI agents in September. Being cited is no longer the finish line. Here is what an agent has to read to buy from you."
faq:
  - q: What is Google's Universal Commerce Protocol hub?
    a: >-
      A section of Merchant Center where US merchants can configure, test and
      launch UCP-powered features on Google, starting with cart transfer and
      expanding to native checkout and account linking. Google says Australia and
      Canada will follow early next year.
  - q: Is native checkout in Google AI Mode turned on for my Shopify store?
    a: >-
      Google emailed merchants on September 22, 2026 that Shopify stores matched
      to Merchant Center were enabled for native checkout on AI Mode and Gemini.
      Merchants can turn it off in the Shopify admin under Sales channels,
      Agentic.
  - q: Can AI agents complete a Shopify checkout?
    a: >-
      Yes. On September 28, 2026 Shopify released WebMCP tools that let browser
      agents read, update and complete checkouts. Shopify's documentation
      requires the agent to show the buyer the order and total and get permission
      before placing it.
  - q: How ready are retailers for AI shopping agents?
    a: >-
      Not very. A PYMNTS Intelligence and Visa study rated 11% of small and
      mid-sized businesses as agent ready, against 19% of large merchants, and
      Adobe reported retail product pages average 66% machine readable.
  - q: Does llms.txt help AI agents buy from my site?
    a: >-
      Not much on current evidence. Google's John Mueller said of llms.txt that
      "the hope is bigger than the reality." Accurate product feeds, structured
      data and server-rendered pages matter more.
---

In September the finish line moved. Google matched Shopify stores to Merchant Center and switched on native checkout in Google AI Mode and Gemini, and [emailed merchants on September 22](https://www.seroundtable.com/google-native-checkout-emails-42140.html) that their store was "matched to your Merchant Center, enabling native checkout on Google AI Mode and Gemini." Days later Shopify announced that [browser agents can now read and update Shopify checkouts](https://shopify.dev/changelog/webmcp-support-for-checkout) using its WebMCP tools.

Every AI search post I have written, and there are a lot of them on this site, has been about getting cited. Being crawled, being mentioned, being recommended. That is now step one. The new question is whether an agent can finish the purchase without getting something wrong.

## What changed in September

Google opened a Universal Commerce Protocol hub in Merchant Center, [described](https://business.google.com/us/accelerate/announcements/ucp-integration-hub-in-merchant-center/) as "your central hub to configure, test, and launch new UCP-powered features," where merchants can "start lightweight with Cart Transfer, or expand into Native Checkout and Account Linking." It is US first, with [Australia and Canada](https://developers.google.com/merchant/ucp/guides/tools/merchant-center/overview) to follow early next year. Shopify, for its part, is auto-enrolling eligible stores in new agentic channels; products [went to Meta by default](https://www.searchenginejournal.com/shopify-now-enrolls-your-store-in-every-new-ai-shopping-channel/591049/) on September 8.

Shopify is also making the agent path fast. In its own test, reported by [TechCrunch](https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/), WebMCP completed 60 of 60 attempts against 56 of 60 for ordinary browser automation, at 10.3 seconds per attempt versus 27.4. Shopify's Gil Greenberg put the goal plainly: "Shopping with an agent shouldn't feel like watching paint dry."

The other direction is just as real. OpenAI said its [Instant Checkout is moving to Apps](https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/), with buyers finishing on the merchant's own site. Walmart reported that purchases inside ChatGPT [converted at about one third the rate](https://martech.org/walmart-says-chatgpt-checkout-converted-3x-worse-than-its-own-website/) of shoppers who clicked out to Walmart's site, a result its EVP called "unsatisfying." And the same TechCrunch report, citing Bloomberg, noted Amazon is blocking AI agents from making purchases. The landscape is unsettled. The requirement underneath it is not.

## An agent believes whatever it reads first

An agent does not shop the way a person does. It pulls price, stock, variant, shipping date and return terms from one of three places: your product feed, your structured data, or the rendered page. If those three disagree, it does not stop to ask which one is right. It acts on whatever it read. A wrong price in the feed becomes a wrong price in the cart.

Most sites are not ready for that. Adobe, [as reported](https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable), scores retail product pages at 66% machine readable, with homepages lower at 61% and returns pages higher at 82%. A PYMNTS Intelligence and Visa [study](https://www.pymnts.com/?p=4214915) rated only 11% of small and mid-sized businesses as agent ready against 19% of large merchants, and found 15% of merchants have structured product data. How often agents get a purchase wrong from a price or stock mismatch is not public yet. The exposure is.

This is the practical cost of two things I have written about before. If your product details only appear after JavaScript runs, [AI crawlers see an empty shell](/blog/your-javascript-site-is-invisible-to-ai-crawlers/), because they do not execute it. And when the model cannot read you cleanly, it fills the gap from wherever it can, which is the whole [source-of-truth problem](/blog/the-source-of-truth-gap/): the agent trusts the source it can parse, not the one you would choose.

I have paid for that gap. At a large retailer I ran growth for, the site's front end could not render schema markup to crawlers, and the fix sat on the IT roadmap for about 18 months. So we stood up a separate content property on infrastructure we controlled, with the structured data built in. Brand audience grew 4.3x and earned mentions 3.6x, and the brand was cited across ChatGPT, Perplexity, Google AI Overviews and Claude. The citations came from the property we could control, not from waiting on the roadmap.

The reason the three sources drift apart is that different teams own them. Merchandising sets the price on the page, a feed tool refreshes the feed on its own schedule, and a developer wrote the structured data once and moved on. For a shopper that drift is invisible, because a person only ever sees the page. For an agent the drift is the whole risk, because it may read the feed or the markup and never load the page a human would. The work is not glamorous. It is making three systems that were never designed to agree report the same number at the same moment. The same discipline extends to identity: publishing [one matching product identifier everywhere](/blog/gtin-connects-your-marketplace-reviews/) is how an engine knows your product is the one reviewed on a marketplace.

## The feed is now a storefront

The product feed used to be a paid-media artifact. It is now the record an agent reads to decide what you sell and for how much. Google's own onboarding reflects that: Merchant Center [will alert you](https://support.google.com/merchants/answer/16992327?hl=en) if any actions are needed to update your feed attributes, returns, or account configuration as you turn UCP features on.

I also learned that Merchant Center is not just a paid tool. The feed is how a product enters the Shopping Graph and AI Mode. That reframes two old technical jobs. A feed that breaks takes your free listings down with the paid ones, because [they run on the same source](/blog/free-shopping-listings-break-on-a-shared-feed/). And variants are where an agent is most likely to choose the wrong size or color, which is exactly the case for giving [high-demand variants their own clean, indexable identity](/blog/product-variant-seo/) rather than collapsing them into one ambiguous product.

A feed that was tuned to win a Shopping auction is not automatically a feed an agent can transact against. The auction forgives a missing return window or a stale delivery estimate. An agent completing a purchase does not, because those fields are the ones it shows the buyer before it places the order.

## Trust has to be machine readable too

Before a person buys, they check the reviews, the return window and the delivery date. An agent needs those same signals, but as data it can parse, not as a badge in an image or a line in a tab it never opens. Ratings only help the agent if they are [marked up where a machine can read them](/blog/review-schema-trust-signal/), and the brand reputation an engine assembles about you is its own [background check](/blog/ai-background-check/) that you do not control but do influence.

A review count rendered as an image, a return policy written only as prose, a delivery promise that appears after a script runs: all of it is invisible to the thing now doing the buying. If a signal is not in the feed or the HTML as data, then for an agent it does not exist.

This matters more because of where the decision still sits. Shopify's documentation requires that, before the agent calls complete, it [show the buyer the order and total](https://shopify.dev/docs/agents/carts-and-checkout/checkout-webmcp) and get permission to place it. The human still approves. Which means the details the agent surfaces have to be right, because a buyer shown the wrong total or the wrong delivery date will cancel at the last step.

## The pre-holiday agent readiness check

The timing is not academic. Adobe forecasts AI traffic to US retail sites up 130% year over year this holiday season, Thanksgiving up 159%, with online sales of $275.1 billion, up 6.7%, in its [September forecast](https://news.adobe.com/news/2026/09/adobe-us-holiday-shopping-season-to-hit-record). Agentic traffic arrives on the same calendar as everything else, which means the window to fix it is the [same shrinking seasonal window](/blog/content-has-a-shelf-life-seasonal-seo/) as the rest of your holiday prep.

Run this check on your top products before peak.

| Item | Where it must match | How to check |
|---|---|---|
| Price and sale price | Feed, structured data, rendered page | Pull all three for one SKU and compare |
| Stock status | Feed, page | Confirm out-of-stock propagates to the feed |
| Variant IDs and attributes | Feed, structured data | Size and color map to the right item |
| Shipping cost and delivery date | Feed, page | The date shown is one you can keep |
| Return window and cost | Returns policy, feed attributes | Stated in days and dollars, not prose |
| Review data | Structured data | AggregateRating present and valid |
| Product identifiers (GTIN, MPN) | Feed | Present and correct for matching |

Three moves make it stick. First, decide on purpose whether you want each agentic channel on; both Google's native checkout and Shopify's auto-enrollment are defaults you can review rather than inherit. Second, run the feed, the structured data and the rendered page for your best sellers side by side and fix every mismatch. Third, do not lean on llms.txt to carry this; Google's John Mueller said of it that [the hope is bigger than the reality](https://www.searchenginejournal.com/googles-mueller-says-ai-crawlers-access-sitemaps-rss-in-his-logs/592012/). Rely on the feed and the HTML.

Getting cited was the work of the last two years. Completing the sale is the work of this one. If an agent bought your best seller today, which detail would it most likely get wrong?
