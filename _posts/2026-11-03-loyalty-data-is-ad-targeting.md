---
title: "Your loyalty data is now ad targeting. Price it that way."
seo_title: "Your loyalty data is now ad targeting"
date: 2026-11-03 09:00:00 -0500
category: loyalty
hero: /assets/img/blog/loyalty-data-is-ad-targeting.svg
image: /assets/img/blog/loyalty-data-is-ad-targeting.png
hero_title: "Loyalty is|ad targeting"
hero_motif: orbit
tags: [loyalty, customer match, member pricing, ai mode, incrementality, privacy]
description: "Google now shows member prices in AI Mode and requires a Customer Match list to do it. Your loyalty file just became ad targeting. Price it that way."
faq:
  - q: Can member pricing show in Google AI Mode?
    a: >-
      Yes, in the US. Google's Merchant Center help says loyalty benefits are
      eligible to show on AI Mode and Gemini Apps in the US only, and Google
      expanded loyalty benefits in listings to 14 countries in March 2026.
  - q: Do I need Customer Match to show member prices on Google?
    a: >-
      Yes, to show them to known members. Google says Customer Match lists are
      mandatory to show member shipping benefits and strikethrough member pricing
      to known members, and loyalty Customer Match is now available to all
      merchants, including non-advertisers.
  - q: Can I upload IP addresses to Customer Match?
    a: >-
      Google's help documentation now accepts IP address and interaction
      timestamp in Customer Match uploads, with timestamps requiring an IP
      address. IP matching is not supported for users in the EEA, UK or
      Switzerland.
  - q: Do loyalty programs increase spending?
    a: >-
      Less than they appear to. Members tend to be customers who already spent
      more. One study found the true effect of membership was seven times smaller
      than a naive comparison suggested, and another found heavy buyers' behavior
      did not change, while light and moderate buyers gradually bought more.
  - q: What data can I use for Customer Match?
    a: >-
      Google's policy allows only customer information collected in a first-party
      context, such as loyalty sign-ups, and requires consent for sharing where
      the law requires it. Several US state privacy laws that took effect in 2026
      include a right to opt out of targeted advertising.
---

To show a member price to a known member in Google's listings, you now need a Customer Match list. Google's Merchant Center documentation says a Customer Match list is [mandatory to show member shipping benefits and green strikethrough pricing](https://support.google.com/merchants/answer/16986038) to known members. And those listings are no longer just the blue links. Loyalty benefits are eligible to show on AI Mode and Gemini Apps, in the US only.

That is a quiet but large change. The loyalty file used to live in the CRM, read by email and the retention team. Now it is an ad audience, read by the ad system and shown at the moment of choice. Which means the member price is an ad offer, and it should be priced like one.

## How loyalty moved into the ad stack

The timeline is short. Google added member pricing and member shipping to listings, expanded loyalty benefits to 14 countries, and made them eligible on its AI surfaces back in March 2026, not this month. The October update that got attention was a [help-page revision](https://seroundtable.com/google-loyalty-customer-match-expands-42216.html) that named AI Mode and Gemini, opened loyalty Customer Match to non-advertisers, added the Merchant API, and expanded the country list. Google also says loyalty Customer Match is now [an option for all merchants, including non-advertisers](https://support.google.com/merchants/answer/12827255). Separately, Customer Match uploads now [accept IP address and interaction timestamp](https://support.google.com/google-ads/answer/7659867?hl=en) to raise match rates. None of this is exotic at scale: Kroger has said [95% of its transactions are tied to a loyalty card](https://www.digitalcommerce360.com/2026/06/18/kroger-digital-sales-q1-fy26/amp/), and its retail media business grew 20% year over year. The member file has been ad infrastructure at the biggest retailers for a while. Now it is that for everyone.

What changed is not the idea. Retailers have segmented members from non-members forever. What changed is the surface and the stakes. The member file now decides what a known customer sees at the exact moment an AI assistant answers their question, before they ever reach your site. That moves the loyalty file out of the once-a-week email cadence and into the real-time ad auction, where mistakes are more expensive and the discount is shown to whoever the list says is a member, correct or not.

## The member price is now an ad offer

Once a member price shows in an AI answer at the moment of choice, it is a discount, and it should be judged like one. For a non-member seeing it, it is an acquisition offer. For a member who was already going to buy, it is margin you handed back. Google's case for it is a click-through case: it says some retailers "have observed up to a 20% increase in click-through rates" when showing tailored offers to existing loyal customers. Read that carefully. It is a claim about clicks, not about incremental sales or margin. A discount shown at the point of decision is the same lever as the [markdown in the luxury playbook](/blog/luxury-playbook-for-the-99-dollar-dress/): it can win the click and still lose the margin, especially on the buyer who needed no convincing.

The cleanest way to see the trap is to ask who the member price actually moves. A shopper who was already loyal, already buying, already heading to the order does not need a strikethrough price to complete it; showing it to them is pure margin give-back dressed up as a benefit. The shopper it might genuinely move is the one on the fence, and that shopper is often not a member yet. So the offer is most wasted exactly where it is easiest to target, and most useful exactly where your list cannot reach.

## Members always look better. That is the problem.

The oldest trap in loyalty is selection. Members are not a random sample of your customers. They are the ones who already liked you enough to sign up, so they would have spent more with or without the card. The research on this is unambiguous. Leenheer and colleagues found the true effect of membership on share of wallet was [seven times smaller](https://repub.eur.nl/pub/9042) than a naive comparison suggests. Liu found that [heavy buyers were the most likely to claim rewards](https://www.yupingliu.com/wordpress/?p=1041) but did not change how they bought, while lighter buyers gradually bought more.

This is why self-reported loyalty numbers run so high. Bond found [73% of loyalty members say they spend more](https://bondbl.com/news/the-bond-loyalty-report-returns-with-loyalty-decoded-revealing-why-loyalty-has-never-looked-stronger/) because of membership, but that is members talking about themselves. Antavo found program owners [report an average ROI of 5.3x](https://antavo.com/?p=48058), but that is owners grading their own programs. Both are exactly the kind of figure selection bias inflates, which is the whole reason to [measure a loyalty program against a control](/blog/loyalty-program-incrementality/) rather than against a flattering before-and-after.

I have done the analytics on this directly. At a large retailer I ran growth for, I did not build the loyalty program. My part was the reporting and forecasting that made the case for loyalty-contingent promotions: offers that went to members, so the full price held for everyone else. The logic of keeping the discount inside a group only works if you have tested whether the group needed the discount at all.

That test is the whole difference between a loyalty program and an expensive habit. A program that has never been measured against a holdout cannot tell you whether it is creating loyalty or simply labeling the customers who were already loyal and paying them to keep doing what they would have done anyway. The member numbers look wonderful either way, and looking wonderful is exactly what selection bias does.

## Clean data and clear permission

Because the file is now targeting, two unglamorous things decide whether it works. The first is data quality. The list you upload decides who sees which price, so old emails, merged households and lapsed members quietly leak member discounts to the wrong people, which is its own version of the [source-of-truth problem](/blog/the-source-of-truth-gap/): the ad surface shows whatever your file says, right or wrong. The second is permission. Google's policy allows only data [collected in a first-party context](https://support.google.com/adspolicy/answer/6299717) and requires consent for sharing where the law requires it. IP matching is not supported for users in the EEA, UK or Switzerland, and three more US state privacy laws, in Indiana, Kentucky and Rhode Island, [took effect this year](https://trustarc.com/resource/new-in-2026-state-privacy-laws-in-indiana-kentucky-and-rhode-island/) with a right to opt out of targeted advertising. I am not a lawyer and this is not legal advice; whether a given upload is permitted is a question for your counsel. The practical point stands: consent and first-party collection are requirements, not nice-to-haves. The file is media now, and dirty media spends money reaching the wrong people. Here it does worse than waste impressions. It leaks your margin to shoppers who were never supposed to see the member price.

## Price the loyalty file like media

Treat the member file the way you would treat any paid audience. Four moves.

1. Hold out a member segment or a region from member pricing in ads, and compare purchases and margin against the members who still got it, using [a real holdout](/blog/how-to-run-a-geo-holdout-test/).
2. Report member offers as a cost line with an owner, not as free retention. Every member discount is spend.
3. Audit the file before each upload: recency, consent status, duplicates. The cleanest targeting in the world fails on a dirty list.
4. Watch what members acquired through the offer do next, because an offer-acquired member can behave like any other [discount-shaped cohort](/blog/cohorts-getting-worse-acquisition/).

If the member price disappeared from your ads for a month, how much would members actually buy less?
