---
title: "The unit math that quietly kills subscription businesses"
seo_title: "The unit math that kills subscriptions"
date: 2026-07-19 09:00:00 -0500
hero: /assets/img/blog/the-unit-math-of-subscriptions.svg
image: /assets/img/blog/the-unit-math-of-subscriptions.png
category: subscriptions
tags: [cohort analysis, LTV, unit economics, contribution margin, payback period, order frequency]
description: "Your 3:1 LTV:CAC can hide an insolvent business. The model lives or dies on cohort decay and contribution margin, not headline averages."
faq:
  - q: Why are blended LTV and CAC misleading?
    a: >-
      Blended numbers average your best cohorts with your worst and your oldest with your newest. A healthy January cohort can mask a June cohort that decays to zero. Averages describe a company that doesn't exist. You underwrite growth on cohort curves, not a single blended ratio.
  - q: What's the difference between a plateau and a decay-to-zero cohort?
    a: >-
      A plateau means retention flattens at a stable percentage of members who stay indefinitely — that residual is the actual subscription. Decay-to-zero means every cohort eventually leaves; you're running a leaky funnel that has to be constantly refilled with paid acquisition. One is an asset. The other is a treadmill.
  - q: Why is payback period more important than LTV:CAC?
    a: >-
      LTV:CAC is a lifetime ratio; payback is a cash-timing constraint. A 3:1 business with a 14-month payback burns cash on every new member for over a year before breaking even. Growth accelerates the burn. Payback, not the ratio, sets how fast you can safely grow.
  - q: What should contribution margin include?
    a: >-
      Everything variable per member: COGS, payment processing fees, shipping and fulfillment, support, and the cost of the retention and dunning machine that keeps members alive. Revenue per member is vanity. Contribution margin is what actually funds CAC and overhead.
  - q: How does order frequency change the math?
    a: >-
      For consumables and replenishment, frequency is the multiplier on both revenue and variable cost. Higher frequency raises LTV but also stacks shipping, fulfillment, and processing fees. Model contribution per order and multiply by realized frequency — not the frequency you hoped for.
---
Pull up your last board deck and find the slide that says "LTV:CAC is 3:1." Now ask one question: 3:1 over what time horizon, for which cohort, on revenue or contribution? If nobody in the room can answer in under a minute, you don't know whether your subscription business is an asset or a slow-motion cash fire. Most of the ones that die had a 3:1 slide right up until the end.

## Blended numbers describe a company that does not exist

**Blended numbers describe a company that doesn't exist.** Blended LTV averages your loyal January cohort with your churn-prone June promo cohort. Blended CAC averages cheap branded search with the expensive paid social you scaled last quarter. The average is a fiction stitched from populations that behave nothing alike. It smooths exactly the signal you need to see. Every subscription business that looked healthy on blended metrics and then cratered had the same problem: the average was fine while the marginal cohort was already dead.

## Retention is a curve, not a rate

**Retention is a curve, not a rate.** A single churn percentage tells you nothing. Plot each monthly cohort as a survival curve and watch what happens after the early drop-off. There are only two shapes that matter. The first flattens to a plateau — after the tourists leave, a stable residual of members stays more or less forever. That plateau is your real business. It's an annuity you can borrow against. The second shape decays toward zero: every cohort, given enough months, fully churns out. That is not a subscription. It's a leaky funnel wearing a subscription's clothes, and it survives only as long as you keep pouring paid acquisition in the top. Same signup graph, same MRR chart, completely different company. You cannot tell them apart without cohort curves.

## Most LTV is extrapolation dressed as measurement

**Most LTV estimates are extrapolation dressed as measurement.** Someone takes months one through four, fits a retention curve, and integrates it out to infinity. If early retention is steep and the curve never actually flattens in your data, that integral inflates LTV wildly. You are booking revenue from members who will be gone before you ever collect it. The honest move is to only credit LTV you can defend from observed plateau behavior — not from a curve fit that assumes today's decay rate holds for three years. When in doubt, truncate. An LTV you can prove beats an LTV you can dream.

## Contribution margin, not revenue per member

**Revenue per member is vanity. Contribution margin is the number.** Take the revenue a member generates and subtract everything variable: COGS, payment processing, shipping and fulfillment, support tickets, returns, and — the line everyone forgets — the cost of the retention and dunning machine that keeps that member alive. The win-back emails, the retention discounts, the save offers, the tooling. That apparatus has a real per-member cost, and it comes straight out of contribution. A box that looks 40% margin on COGS alone routinely lands in the low teens once you load in the rest. You fund CAC and overhead out of contribution, not revenue. If you're computing LTV on revenue, every downstream ratio is inflated.

## Frequency multiplies in both directions

**Frequency is the multiplier — in both directions.** For consumables and replenishment, order frequency drives the whole model. More orders per member means more lifetime revenue, but it also stacks shipping, fulfillment, and processing fees on every cycle. Model contribution per order, then multiply by *realized* frequency, not the frequency in your pitch deck. And watch the interaction: a member who orders more often but churns faster can be worth less than a slow, sticky one. Frequency and retention are not independent, and the blended view hides the tradeoff completely.

## Payback is the constraint that actually binds

**Payback period is the constraint that actually binds you.** LTV:CAC is a story about the distant future. Payback is a fact about your bank account. A 3:1 business with a 14-month contribution payback is spending cash on every new member and not seeing it back for over a year. Grow faster and you dig the hole faster — growth becomes the thing that kills you. That's how a "3:1 business" ends up insolvent while the slide still reads 3:1. LTV:CAC tells you if the unit is profitable eventually. Payback tells you if you'll be alive to collect. Cash, not the ratio, sets your speed limit.

## What to do first

Segment your cohorts by acquisition month and channel — no blended anything. Plot each as a retention curve and answer the one question that matters: does it flatten to a plateau, or decay to zero? If it plateaus, size the plateau; that's your real subscription. If it decays, admit you're running a funnel and price acquisition accordingly.

Then rebuild your economics on contribution margin, fully loaded, retention machine included — not revenue. Recompute LTV only against defensible plateau retention, not an extrapolated curve. For replenishment models, express it as contribution per order times realized frequency.

Finally, put contribution payback period on the wall next to LTV:CAC and let it govern how fast you spend. If payback runs past your cash runway, you don't have a growth problem — you have a solvency problem that growth makes worse.

A subscription business is an annuity or it's a treadmill. The math tells you which one you bought — right up until it tells your investors.
