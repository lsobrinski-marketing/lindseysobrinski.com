---
title: "You cannot prove your ads work, because no one will let you turn them off"
seo_title: "Why you cannot prove your ads work"
date: 2026-10-19 09:00:00 -0500
category: paid-media
hero: /assets/img/blog/permission-not-statistics.svg
image: /assets/img/blog/permission-not-statistics.png
tool_link: /geo-holdout-planner.html
tool_link_label: "Open the Geo-Holdout Pilot Planner →"
hero_title: "Permission,|not statistics"
hero_motif: funnel
hero_alt: "A funnel narrowing from a wide, noisy set of channels down to a single approved test, representing an incrementality test that is blocked by a budget approval rather than by statistics."
tags: [incrementality testing, geo holdout, measurement, paid media, holdout test, marketing measurement]
description: "Incrementality goes unmeasured not because the math is hard but because no one will approve pausing spend. Here is how to get the yes."
faq:
  - q: How long should a geo-holdout run?
    a: >-
      Long enough to clear weekly noise and short enough to approve. A common
      window is a four to six week test with a two-week pre-period freeze on
      promotions. The right length depends on your conversion volume. Thin
      volume needs more time or more markets to reach the power to detect a real
      effect.
  - q: How many markets do I need?
    a: >-
      Enough that the held-out and control groups each carry a stable baseline,
      and enough total conversions to detect the lift you care about. A few
      markets with low conversion counts is the most common reason a pilot
      cannot prove anything. Size it before you run it rather than after.
  - q: Do I need a vendor to run a geo-holdout?
    a: >-
      No. The design and the readout can be done with open-source tools and a
      competent analyst. A vendor buys you execution and convenience, not the
      ability to run the test. Know what a sound test looks like first, so you
      can tell whether what you are paying for is sound.
  - q: How do I get my CFO to approve turning off spend?
    a: >-
      Stop framing it as turning off a good channel. Frame it as risking a
      small, named amount in a few low-volume markets for a fixed window, with a
      readout date. Cap the revenue at risk and say the number out loud. A
      bounded cost with an end date is approvable in a way that an open-ended
      pause is not.
  - q: Geo-holdout, conversion lift, or MMM, which one?
    a: >-
      Geo-holdout when you can separate spend by geography and want a clean
      causal read without user tracking. Platform conversion lift when the
      question is one platform's value and you accept that the platform runs the
      test. MMM when you cannot turn anything off and have years of weekly data.
---

Because no one will let you turn them off. Incrementality does not go unmeasured because the statistics are hard. It goes unmeasured because pausing spend that looks like it is working requires a yes from someone who sees no reason to risk it. The fix is not a better model. It is a smaller, safer ask.

## What's in this piece

- Why the real blocker to a clean test is a person, not a p-value
- How a good last-click number guarantees a no
- What the no is actually costing you
- How to design a test small enough to get approved
- How to read the result without hiring a vendor

## The blocker is a person, not a p-value

I managed an eight-figure annual paid media budget for several years. In that entire time I was allowed to run zero incrementality tests. Not one. The method was never the hard part. The hard part was that no one would approve turning off spend that looked like it was working.

If you have never run a real holdout either, this is almost certainly why. The textbooks treat incrementality as a statistics problem. In practice it is a permission problem. The person who controls the budget sees a channel reporting a healthy return, and the request on the table is to deliberately stop some of it and watch sales for a few weeks. That request loses every time it is framed that way.

A geo-holdout is not complicated. You hold back media in a set of markets, you keep running it in a matched set, and you measure the gap. Open-source tools do the heavy math, and a competent analyst can design one in an afternoon. None of that matters if the answer is no before you finish the sentence. The constraint is not the model. It is the conversation with the person who owns the number. So the skill that actually gets a test run is not statistical. It is knowing how to make the ask small enough, and safe enough, that a cautious executive says yes.

## Why a good last-click number guarantees a no

Here is the trap. Your platforms report a strong return. Google and Meta both claim the conversions they can plausibly attribute to themselves, including the ones that would have happened with no ad at all. The reported number is high because the platform is [grading its own homework](/blog/platform-roas-is-grading-its-own-homework/).

To the person approving budgets, that high number is not a question. It is proof. You are walking in to say "let me turn off something that is returning four times its cost on paper so I can check whether it is real." You have framed your own test as a threat to a good result. Of course the answer is no.

Loss aversion does the rest. Pausing spend feels like choosing to lose sales. Keeping it on feels safe, even when no one can say what it is actually producing. The better the vanity number looks, the harder the real test is to approve. That is the opposite of how it should work, and it is exactly how most budgets run.

## What the no is actually costing you

Every dollar you cannot test is a dollar you are allocating on faith, and the research says that faith is usually misplaced. In the largest study of its kind, economists at Kellogg compared 663 randomized advertising experiments on Facebook against the observational methods most measurement relies on, and found the observational methods overstated the true, randomized lift by several times. For upper-funnel campaigns the randomized lift was 29 percent, while a standard matching method put it at 173 percent, roughly six times too high, in their paper ["Close Enough?"](https://www.kellogg.northwestern.edu/academics-research/research/detail/2023/close-enough-a-large-scale-exploration-of-non-experimental/). Even the better statistical method they tested still ran about three times the experimental truth. The number on your dashboard is not a small overstatement of reality. It is often a large one.

So without a test you do not know which of your channels are carrying the business and which are taking credit for demand you already had. The cost is not only wasted spend. It is every decision downstream. You cannot set a defensible budget, you cannot defend the one you have, and you cannot answer the one question a CFO will eventually ask, which is what happens to revenue if we cut this. Without a test, your honest answer is that you do not know. That is a weak place to run a large budget from.

## Design the test small enough to get a yes

The move is to stop asking for the perfect experiment and start asking for the smallest one that still proves something. You are not trying to measure the whole account. You are trying to get a single real read, cheaply, so the next ask is easier.

A pilot that gets approved usually has four things. It holds out a small share of markets, not the big ones, so the revenue at risk is capped and known. It names that number up front, so the executive is approving a bounded cost, not an open one. It runs for a fixed window with a fixed readout date, so it has an end. And it leaves everything else running, so the business keeps moving while you learn.

Sized that way, the ask changes shape. You are no longer proposing to turn off a good channel. You are proposing to risk a named, small amount for a few weeks to find out what the whole budget is really doing. That is a yes. The mechanics of picking the markets and the duration are a power-analysis question, not a guess, and I have [written the sizing up separately](/blog/geo-holdout-sizing-markets-and-duration/): you put in your weekly conversions, how many markets you can hold out, and the lift you need to detect, and that determines the test-cell size, the smallest effect you can actually measure, the duration, and the revenue you would be putting at risk. The point is not the math. It is handing the executive the bounded, approvable version of the ask.

{% include tool-geo-holdout.html %}

## How to read it without hiring a vendor

Do not read the result as raw before-and-after. Sales move for a hundred reasons in any given week, and a simple period-over-period comparison will fool you.

Use the matched markets as the counterfactual. Difference-in-differences or a synthetic control estimates what the held-out markets would have done if you had kept spending, based on the markets where you did. The gap between that estimate and what actually happened is your incremental lift, the [number a CFO can trust](/blog/incremental-roas-the-number-a-cfo-trusts/) rather than the attributed one. Check that the confidence interval does not straddle zero. If it does, your pilot was too small or too noisy, and the honest read is that you could not tell, not that the channel is dead.

You do not need a measurement contract to do this. You need the holdout designed correctly and enough volume to clear the noise. A vendor can run it for you, and sometimes that is the right call, but you should know what a defensible test looks like before you pay for one, so you are buying execution and not buying permission to believe a number. If you are still deciding whether to run one yourself at all, I have made [that case separately](/blog/geo-holdout-pilot-before-a-measurement-contract/), and if you are choosing between a geo-holdout and another method, [here is how to pick](/blog/which-incrementality-test-to-run/).

So before the next planning cycle locks your budget in place, which is the easier conversation to have: defending every channel on a platform-reported number you cannot verify, or walking in with a capped, two-week test and a date when you will have an answer?

## Sources

- Gordon, Moakler and Zettelmeyer, "Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement," Marketing Science, 2023 (663 Facebook experiments): [kellogg.northwestern.edu](https://www.kellogg.northwestern.edu/academics-research/research/detail/2023/close-enough-a-large-scale-exploration-of-non-experimental/)
- Gordon, Zettelmeyer, Bhargava and Chapsky, "A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook," Marketing Science, 2019: [kellogg.northwestern.edu](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/)
