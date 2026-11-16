---
title: "Reactivation costs less than acquisition, but only if it is incremental"
seo_title: "Reactivation vs acquisition cost"
date: 2026-11-10 09:30:00 -0600
category: lifecycle
hero: /assets/img/blog/reactivation-vs-acquisition.png
image: /assets/img/blog/reactivation-vs-acquisition.png
hero_title: "Cheaper,|only if real"
hero_motif: bars
hero_alt: "Two cost columns side by side, one labeled acquisition and one reactivation, with only the small top slice of the reactivation column highlighted in warm gold to mark the incremental part, the rest shaded as returns that would have happened anyway."
tags: [lifecycle, reactivation, win-back, incrementality, retention, acquisition cost]
description: "Reactivation looks cheaper than acquisition per order, but much of it is not incremental. Measure the incremental cost with a holdout before you shift budget."
faq:
  - q: Is it cheaper to win back a customer or acquire a new one?
    a: >-
      Often cheaper to win back, but not by as much as the dashboard says, and
      sometimes not at all. A win-back campaign reaches people who already know
      you, so the cost per order looks low, but a share of those customers were
      going to return on their own. The only fair comparison is incremental cost
      per reactivated customer against acquisition cost, and you get the
      incremental number from a holdout, not from the attributed total.
  - q: How do you measure incremental reactivation?
    a: >-
      Withhold the win-back campaign from a random slice of the eligible lapsed
      audience, run it to everyone else, and compare return rates over the same
      window. The gap between the two groups is the incremental reactivation, the
      customers the campaign actually brought back. Divide the campaign cost,
      including the discount margin, by that incremental count to get the honest
      cost per reactivated customer.
  - q: What is a win-back holdout?
    a: >-
      A control group inside your lapsed list that is deliberately not sent the
      win-back flow. You split the eligible audience at random, send to most,
      hold back the rest, and read the difference in returns. It is the lifecycle
      version of a geo holdout, and it is the only read that separates the
      reactivations you caused from the ones that were coming anyway.
  - q: Does a discount-driven win-back train customers to wait?
    a: >-
      It can. If customers learn that lapsing triggers a discount, you teach your
      base to stop buying until the offer arrives, which raises the cost of every
      future order. A holdout helps here too, because it shows whether the
      discount is buying incremental returns or just subsidizing returns you
      already had and conditioning the rest of the list to wait.
toc: false
---

Reactivation looks cheaper than acquisition on a cost-per-order basis, and that comparison is a trap. Much of what a win-back campaign claims is not incremental: customers who were going to return anyway. The honest number is incremental cost per reactivated customer, measured with a holdout. Measured that way, reactivation is often cheaper, and sometimes it is not.

## What's in this piece

- Why reactivation looks cheaper than it is
- The would-have-returned-anyway problem
- How to measure incremental reactivation
- When reactivation actually beats acquisition, and when it does not
- What to do with the finding

## Why does reactivation look cheaper than it is?

Open any win-back report and the math is flattering. You email a lapsed segment, some of them buy, and the cost per order comes in far below your blended acquisition cost. The conclusion writes itself: stop spending so hard on new customers and pour it into winning back the old ones.

The reason the number looks good is the reason it is wrong. A lapsed list is not a cold audience. It is people who already chose you once, kept the account, maybe still get the emails. Reaching them is cheap because you are not paying to find them again. But a low cost to reach is not the same as a low cost to cause a purchase, and the report only measures the first one. It credits the campaign with every return that followed a send, with no way to know which of those returns needed the send at all.

## What is the would-have-returned-anyway problem?

A lapsed customer is rarely gone. Many are simply between purchases, on a longer or more irregular cycle than your definition of lapsed assumes. A share of them were always going to come back, discount or no discount, email or no email. When the win-back flow sends to the whole segment, it collects the returns from those people alongside the returns it actually created, and the report cannot tell the two apart.

This is the same selection effect that inflates loyalty numbers and retargeting returns, and it is the core finding in Lewis and Rao's work on how hard advertising returns are to measure: the response you are trying to detect is small next to the behavior that was going to happen anyway. A win-back email is a marketing touch like any other. The thing that looks like a strong effect is mostly demand already in motion. The site covers the lifecycle version of this in [win-back campaigns mostly reactivate people who would have returned anyway](/blog/winback-incrementality/), and the fix is the same discipline every time: stop asking who bought after the send, and start asking what would have happened without it.

## How do you measure incremental reactivation?

With a holdout, and for lifecycle email it is cheaper to run than almost any other experiment, because the audience is already defined and the send is already automated. Withhold the win-back flow from a random slice of the eligible lapsed audience, send it to everyone else, and observe both groups over the same window. The treated group returns at one rate. The held-out group returns at some rate with no campaign at all. The incremental reactivation is the gap, and only the gap.

The design has a few non-negotiables. Split at random, so the held-out group mirrors the treated one instead of being your least valuable lapsed customers. Hold out a slice large enough that the difference can clear the noise. Use a window long enough to capture the natural return behavior, because a window that is too short misses the organic returns coming a few weeks later and overstates the lift. Fix the metric and the window before you start. This is the same logic as [a geo holdout](/blog/how-to-run-a-geo-holdout-test/), applied to an email list. Then divide the full cost of the flow, including the margin you gave away in the discount, by the incremental count. That is your cost per reactivated customer, and it is the only version of the number that belongs next to acquisition cost.

## When does reactivation actually beat acquisition?

Once you have the real lift, the comparison becomes honest, and it usually still favors reactivation, just by less than the gross implied. A lapsed customer who needed the nudge and came back is cheaper to move than a stranger who has never heard of you, because you are not paying for discovery or first trust. That is a real structural advantage and it does not disappear when you measure correctly.

Where reactivation loses is at the edges. If the held-out group returns on its own at a high rate, the incremental cost per reactivation can climb above acquisition cost, which means you are paying a discount to pull forward or confirm returns you already had. And a reactivation only pays if it leads to another order, which is why [the second purchase is the real conversion](/blog/the-second-purchase-is-the-real-conversion/) and why the number to watch is [what a reactivated customer is worth over time](/blog/cohort-payback-period/), not the single order the report celebrates. Acquisition and reactivation are two incremental-cost curves, and the right split is wherever the next incremental dollar buys more.

## What do you do with the finding?

The result rarely says kill the flow. A win-back program with a real, positive incremental lift against its cost is worth keeping and scaling, now that the number is honest. A flow whose lift is near zero once you subtract organic returns is not earning its discount, and the move is to cut the giveaway, not necessarily the email: a lighter reminder with no markdown may capture the same organic returns without paying for them. Often the right answer is to re-time, pushing the flow later or reserving the discount for the segment that truly does not come back on its own, which is how you keep the incremental part and stop paying for the rest. The segments matter here the same way they do in [any honest look at churn](/blog/four-kinds-of-churn/): the customer who needs the nudge and the customer who was always coming back should not get the same offer, and the only way to tell them apart is the test. So before your next plan books reactivation as cheaper than acquisition, have you measured the lift, or are you comparing a real acquisition cost to a reactivation cost that is mostly borrowed?

## Sources

- Randall A. Lewis and Justin M. Rao, "The Unfavorable Economics of Measuring the Returns to Advertising," Quarterly Journal of Economics, 2015 (why ad response is hard to detect against baseline behavior): [ideas.repec.org](https://ideas.repec.org/r/oup/qjecon/v130y2015i4p1941-1973.html)
- Blake, Nosko and Tadelis, "Consumer Heterogeneity and Paid Search Effectiveness" (the eBay holdout; attributed revenue that was not incremental), 2015: [nber.org](https://www.nber.org/papers/w20171)
