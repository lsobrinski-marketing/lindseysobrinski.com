---
title: "Run a geo-holdout pilot before you sign a measurement vendor"
seo_title: "Run a geo-holdout pilot before a measurement vendor"
date: 2026-10-13 09:02:00 -0500
category: paid-media
hero: /assets/img/blog/geo-holdout-pilot-before-a-measurement-contract.svg
image: /assets/img/blog/geo-holdout-pilot-before-a-measurement-contract.png
hero_title: "Pilot before|the contract"
hero_motif: arcs
hero_alt: "A single highlighted test region on a stylized map measured against a set of matched control regions, with a caliper comparing the two, representing one geo-holdout pilot run before committing to an ongoing measurement contract."
tags: [geo holdout, incrementality testing, measurement, paid media, holdout test, marketing measurement]
description: "You can pilot a geo-holdout yourself for a fraction of a measurement contract. One test tells you if a channel is incremental before you sign."
faq:
  - q: Do I need an incrementality vendor, or can I run the tests myself?
    a: >-
      You can run the first test yourself. A geo-holdout uses a published,
      decades-old method and the media you were already going to spend, so a
      single pilot is well within reach for most in-house teams. A vendor is
      worth paying for when you need the test run continuously, across many
      channels, at a scale or cadence an in-house team cannot sustain. Run the
      pilot first, then decide.
  - q: How much does a geo-holdout pilot cost?
    a: >-
      Less than people expect, because the main cost is not a fee. It is the
      media you reallocate or withhold in the test markets, which you were
      already spending, plus the analyst time to design and read the test.
      There is no platform license for a one-off pilot. Weighed against an annual
      measurement contract, a single pilot is a small, bounded cost that tells
      you whether the contract is worth signing.
  - q: What is the difference between a one-off pilot and ongoing measurement?
    a: >-
      A pilot is a snapshot. It answers whether one channel is incremental in one
      window, which is enough to make a budget decision. Ongoing measurement
      keeps that answer current as spend, creative, seasonality and channel mix
      change, and extends it across more channels than a single test can cover.
      The pilot tells you if the question is worth answering repeatedly. Only
      then does ongoing monitoring earn its cost.
  - q: How do I know if a measurement contract is worth it?
    a: >-
      Run the pilot, then ask how fast your spend changes. If your budget is
      stable and concentrated in a few channels, one pilot can hold for a long
      time and a contract may be premature. If you are scaling quickly across
      many channels, the answer decays and the value of always-on monitoring
      rises. The contract is worth it when last quarter's answer goes stale
      before you can act on it.
---

Yes. You can and should pilot a geo-holdout yourself before you sign a measurement vendor. One well-designed test, holding spend out of a random set of matched markets and comparing outcomes, tells you whether a channel is actually incremental, for a fraction of a yearly contract. Use that result to decide whether ongoing measurement is worth paying for.

## What's in this piece

- What a geo-holdout pilot actually proves, and what it does not
- Why to run the pilot before you sign anything
- Designing a credible one-off pilot
- Reading the result: incremental lift, not platform-reported ROAS
- When the pilot says pay for the vendor, and when it says you already have your answer
- What an ongoing vendor adds on top of a one-off pilot
- The COO question: what you are really buying with ongoing monitoring

## What a geo-holdout pilot actually proves, and what it does not

A geo-holdout answers one question. If you turn a channel off in a set of markets, does the business change. You hold spend out of a random set of matched markets, keep it running in the rest, and compare outcomes. The difference is the incremental effect: the sales that would not have happened without the spend. That is the number almost no platform report gives you, because a platform counts the conversions that were going to happen anyway.

The clearest proof of that gap comes from eBay. In a large field experiment, its economists turned off brand-keyword search ads and found [no measurable short-term benefit](https://www.nber.org/papers/w20171) from them, even though the platform had been crediting those ads with real revenue. A holdout caught what attribution could not, which is the same reason [branded search so often looks incremental when it is not](/blog/is-branded-search-incremental/): the person was already going to buy.

What a pilot does not prove is just as important. It does not measure every channel at once, it does not run forever, and it does not hand you a weekly dashboard. A single pilot is a snapshot of one channel in one window. That is enough to make a budget decision. It is not a monitoring system, which is the distinction that decides whether you need a vendor at all.

## Why to run the pilot before you sign anything

Because the pilot answers the exact question the contract is supposed to answer, and it answers it for far less money. Measuring advertising returns is hard, and the research says so plainly. Lewis and Rao showed that the returns to advertising are so noisy relative to total sales that most observational methods cannot measure them reliably at all, in [work published in the Quarterly Journal of Economics](https://ideas.repec.org/r/oup/qjecon/v130y2015i4p1941-1973.html). Gordon and colleagues, comparing observational models against fifteen randomized experiments at Facebook, concluded that those methods ["often fail to accurately measure the true effect of advertising"](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/).

The lesson from both is the same. If you want to know whether a channel works, you run an experiment. A measurement vendor sells you experiments on a subscription. You can run the first one yourself, and you should, because the alternative is to trust the platform's own report, which is the seller [grading its own homework](/blog/platform-roas-is-grading-its-own-homework/). Pay for the subscription only after a test has shown you there is something worth subscribing to.

## Designing a credible one-off pilot

The method is published and old enough to be boring. Google's Jon Vaver and Jim Koehler laid out geo experiments in 2011: split non-overlapping geographic regions at random into treatment and control, change the ad spend in the treatment markets, and measure the difference against control, in [their geo experiments paper](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/). The craft is in the matching and the sizing. Pick markets that moved together before the test. Hold spend out of a random subset. Leave the rest running as the control. Give it enough time for the effect to clear the week-to-week noise, which usually means a few weeks, and longer when the lift you expect to find is small.

The most common way a pilot fails is under-holding: cutting too little spend, in too few markets, for too short a window, so the test cannot detect an effect that is really there. I am not going to repeat the full mechanics here, because I have [written the step-by-step how-to separately](/blog/how-to-run-a-geo-holdout-test/). The point for this decision is narrower. The design is known, the method is documented, and nothing about running one pilot requires a vendor's platform.

## Reading the result: incremental lift, not platform-reported ROAS

Read the test on incremental lift, not on attributed conversions. Establish what the treatment markets would have done without the change, using their pre-test relationship to the control, then measure the gap between that baseline and what actually happened. Divide incremental revenue by incremental spend and you have incremental ROAS, the [number a CFO can trust](/blog/incremental-roas-the-number-a-cfo-trusts/), rather than the platform-reported ROAS that counts demand you already had.

At a large retailer I ran growth for, every channel was read three ways: the platform's report, a post-purchase survey, and incrementality tests. When the three disagreed, the platform's number was almost always the optimistic one. The holdout was the tiebreaker, because it was the only one of the three that nobody selling media had produced.

## When the pilot says pay for the vendor, and when it says you already have your answer

A pilot resolves into one of two situations. In the first, the answer is large and clear. The channel is strongly incremental, or it clearly is not, and the result is big enough to act on without a second opinion. At a subscription wellness brand, I cut DSP spend that could not show it was adding customers. One clean read settled it, and no ongoing contract would have changed the decision.

In the second, the answer is close to the noise, or you can see it drifting as you scale, or you have a dozen channels and have only tested one. That is where a one-off pilot runs out of road. You do not need a vendor to tell you a channel is dead. You might need one to keep telling you the truth about ten live channels as all of them move.

## What an ongoing vendor adds on top of a one-off pilot

A vendor is buying you repetition and breadth, not a different kind of truth. Three things specifically. First, always-on testing: geo experiments can be run continuously rather than as a single shot, using the kind of [time-based framework Google published](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/) for exactly that. Second, in-platform methods a geo holdout cannot run, such as [conversion lift](https://support.google.com/google-ads/answer/12003020), which measures at the user level inside a platform, with the caveat that it is run by the seller. Third, triangulation: no single method is the whole answer, and keeping [attribution, incrementality and media mix modeling](/blog/attribution-incrementality-mmm-which-one/) in agreement is real, ongoing work. What a vendor does not add is a more valid version of the one test you can already run.

## The COO question: what you are really buying with ongoing monitoring

So reframe the purchase. You are not paying a vendor to find out whether a channel is incremental. The pilot answered that. You are paying for the guarantee that the answer stays current as spend, creative, seasonality and channel mix all change underneath it. That is a real thing to buy, and for some businesses it is clearly worth it.

The real question is not whether measurement is worth it. It is whether your spend changes fast enough that last quarter's answer is already stale. Run the pilot first. If the answer holds still, you have saved yourself a contract. If it will not hold still, you now know exactly what the contract is for. When did you last confirm, with a test rather than a dashboard, that your biggest channel is actually incremental?

## Sources

- Jon Vaver and Jim Koehler, "Measuring Ad Effectiveness Using Geo Experiments," Google, 2011: [research.google](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)
- Google, "Estimating Ad Effectiveness using Geo Experiments in a Time-Based Regression Framework" (continuous geo testing): [research.google](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/)
- Gordon, Zettelmeyer, Bhargava and Chapsky, "A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook," Marketing Science, 2019: [kellogg.northwestern.edu](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/)
- Randall A. Lewis and Justin M. Rao, "The Unfavorable Economics of Measuring the Returns to Advertising," Quarterly Journal of Economics, 2015: [ideas.repec.org](https://ideas.repec.org/r/oup/qjecon/v130y2015i4p1941-1973.html)
- Blake, Nosko and Tadelis, "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment" (the eBay study), 2015: [nber.org](https://www.nber.org/papers/w20171)
- Google Ads Help, "About Conversion Lift": [support.google.com](https://support.google.com/google-ads/answer/12003020)
