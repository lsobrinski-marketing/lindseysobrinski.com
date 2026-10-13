---
title: "Which incrementality test should you run? Geo holdout vs conversion lift vs ghost ads vs MMM"
seo_title: "Which incrementality test should you run?"
date: 2026-10-13 09:01:00 -0500
category: paid-media
hero: /assets/img/blog/which-incrementality-test-to-run.svg
image: /assets/img/blog/which-incrementality-test-to-run.png
hero_title: "Which test|should you run?"
hero_motif: nodes
tags: [incrementality testing, geo holdout, conversion lift, ghost ads, media mix modeling, measurement]
description: "Geo holdout, conversion lift, ghost ads, or MMM? The right incrementality test depends on your channel, budget, and data. A plain decision guide."
faq:
  - q: What is the difference between a geo holdout and a conversion lift test?
    a: >-
      A geo holdout randomizes whole geographic markets into treatment and
      control, so it works for channels you cannot split by individual user, and
      you run it yourself. A conversion lift test randomizes users inside a
      platform and is run by that platform. The geo test trades precision for
      independence; the conversion lift test trades independence for user-level
      precision.
  - q: Are platform-run lift tests trustworthy?
    a: >-
      They are useful, with a caveat. Conversion lift and ghost-ads tests use
      real randomization, which is a genuine strength over attribution. But the
      platform designs, runs and reports the test on its own inventory, so it is
      measuring its own work. Treat the result as evidence, not a verdict, and
      confirm the ones that drive big budget decisions with a test you control.
  - q: When should I use MMM instead of a holdout?
    a: >-
      When you need an always-on, top-down read across every channel at once,
      including ones you cannot hold out, and you have years of weekly history to
      feed it. Media mix modeling answers the portfolio question a single holdout
      cannot. It is slower, needs more data, and is correlational at its core, so
      it pairs best with experiments that calibrate it.
  - q: Can I combine incrementality methods?
    a: >-
      Yes, and you should. No single method is the whole truth. The strongest
      setups use experiments (geo or in-platform lift) to establish ground truth
      on specific channels, then use MMM to carry that read across the full
      budget, with attribution as the fast daily signal rather than the source of
      truth.
---

There is no single best incrementality test. The right one depends on your budget, your channel, and how clean your data is. Geo holdouts fit channels you cannot split by user. Platform conversion lift and ghost ads fit in-platform audiences but are run by the seller. Media mix modeling fits always-on, cross-channel budgets. Match the method to the question you are asking.

## What's in this piece

- The four tests on one table
- Geo holdouts: when you cannot randomize by user
- Platform conversion lift and ghost ads: convenient, in-platform, and conflicted
- Media mix modeling: top-down, always-on, slow, data-hungry
- A short decision tree
- Why you still triangulate

## The four tests on one table

Every method here is trying to answer the same question: what would have happened without the spend. They differ in how they build the counterfactual, and each trade-off has a cost.

| Method | What it measures | Best when | Rough cost | Main weakness |
|---|---|---|---|---|
| Geo holdout | Market-level incremental lift | You cannot split the channel by user (CTV, radio, direct mail, retail media) | Low to medium | Coarser than user-level; needs enough markets |
| Platform conversion lift | User-level incremental lift inside one platform | The channel is a big in-platform audience (Meta, Google) | Low | Designed, run and reported by the seller |
| Ghost ads | User-level lift using a clean held-out control | You want conversion lift with a better control group | Low to medium | Still in-platform; needs platform support |
| Media mix modeling | Top-down contribution across all channels | You need an always-on portfolio read with years of history | High | Correlational; slow; data-hungry |

Hold that table in mind. The rest of the piece is why each row reads the way it does.

## Geo holdouts: when you cannot randomize by user

A geo holdout randomizes geography, not people. You split non-overlapping markets at random into treatment and control, change the spend in the treatment markets, and measure the difference, a method Google's Jon Vaver and Jim Koehler [laid out in 2011](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/). Its great advantage is reach: it works for the channels you cannot split by individual user, which is most of the upper funnel. Connected TV, radio, out-of-home, direct mail, and retail media all resist user-level splitting, and geo is often the only clean experiment available for them. User-level tests cannot touch those channels at all, because there is no user-level log to split: a television ad does not drop a cookie. Geography is the only randomization available, which is why geo holdouts are the backbone of upper-funnel measurement rather than a fallback.

The trade-off is precision and independence. Markets are a coarser unit than users, so you need [enough of them, well matched, to detect a real effect](/blog/geo-holdout-sizing-markets-and-duration/). In exchange you get the one thing no in-platform test offers: a result that nobody selling the media produced. For how to run one, I have a [full how-to](/blog/how-to-run-a-geo-holdout-test/), and for whether to run one before hiring a vendor, a [separate piece on piloting it first](/blog/geo-holdout-pilot-before-a-measurement-contract/).

## Platform conversion lift and ghost ads: convenient, in-platform, and conflicted

Inside a single platform you can do better than geography. A conversion lift test randomizes users into a group that can see the ads and a group that cannot, then compares conversions. Google documents its version in its [Conversion Lift help](https://support.google.com/google-ads/answer/12003020). The method is sound, because it uses real randomization rather than attribution. Ghost ads improve on it: instead of showing the control group nothing, the system records which control users would have seen the ad, giving a cleaner, better-matched comparison, as [Johnson, Lewis and Nubbemeyer set out](https://www.kellogg.northwestern.edu/academics-research/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad/) in the research that named the technique.

Here is the catch, and it is structural, not technical. The platform designs the test, runs it on its own inventory, and reports the result. That is the seller measuring its own work, the same conflict that makes [platform-reported ROAS grade its own homework](/blog/platform-roas-is-grading-its-own-homework/). It does not mean the number is wrong. It means you should treat an in-platform lift result as evidence, not a verdict, and confirm the ones that move real budget with a test you control.

The reason to use them at all is that randomization, even run by the seller, beats attribution run by anyone. A real experiment compares buyers to comparable users who were randomized out of seeing the ad. Attribution just credits whoever the ad happened to touch on the way to a purchase they might have made regardless. An in-platform lift test is a genuine experiment with a conflict of interest. Attribution is not an experiment at all. Rank them accordingly.

## Media mix modeling: top-down, always-on, slow, data-hungry

Media mix modeling comes at the problem from the top. Instead of running an experiment, it uses years of weekly data to statistically attribute sales across every channel at once, including the ones you can never hold out. It answers the portfolio question a single test cannot: given everything running together, what is each channel contributing. The method is mainstream enough that both Google and Meta publish open-source implementations, Google's [Meridian](https://blog.google/products/ads-commerce/meridian/) and Meta's [Robyn](https://github.com/facebookexperimental/Robyn).

The weaknesses are the price of that breadth. MMM is correlational at its core, it needs a lot of clean history, and it is slow to reflect a change you made last week. On its own it can confidently assign credit to a channel that an experiment would show is doing nothing. That is why the serious practice is not MMM instead of experiments, but MMM calibrated by them.

In practice that means running geo or in-platform experiments on the channels you can test, then using those measured lifts to anchor the model so it cannot wander off and assign credit the experiments contradict. A model calibrated to real experiments is a different instrument than a model fit to history alone. One is disciplined by ground truth. The other is a confident narrator of correlations.

## A short decision tree

Pick the method from your constraints, not from fashion.

Start with the channel. If you cannot split it by user, which is most upper-funnel and offline media, a geo holdout is your experiment. If it is a large in-platform audience, a conversion lift or ghost-ads test is available and cheap, with the seller caveat attached. Then check your scope. If the question is one channel, run the experiment that fits it. If the question is the whole budget at once, and you have the history, that is the MMM question. Finally, check your stage. A single decision needs one clean test. An always-on program that re-decides budget every month needs a standing method, and usually more than one. A startup testing one new channel and a brand managing forty are not asking the same measurement question, and should not buy the same measurement system.

## Why you still triangulate

No single method is the truth. Attribution is fast and conflicted. Platform lift tests are real experiments run by an interested party. Geo holdouts are independent but coarse. MMM is comprehensive but correlational. Each one is wrong in a different direction, and knowing the direction of each error is most of the skill, which is exactly why reading them together beats trusting any one of them, and why the honest version of measurement is a [stack of methods, not a single number](/blog/attribution-incrementality-mmm-which-one/).

The practice that holds up: use experiments to establish ground truth on the channels that matter, use MMM to carry that read across the full budget, and keep attribution as the daily signal rather than the source of truth. When two of them agree, you have a decision. When they disagree, you have found the thing worth investigating, which is more useful than a [clean-looking number that was never tested](/blog/incremental-roas-the-number-a-cfo-trusts/). The goal is not the one perfect test. It is to stop being fooled, and triangulation is how you [tell a real lift from noise](/blog/a-real-lift-or-just-noise/).

## Sources

- Jon Vaver and Jim Koehler, "Measuring Ad Effectiveness Using Geo Experiments," Google, 2011: [research.google](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)
- Google Ads Help, "About Conversion Lift": [support.google.com](https://support.google.com/google-ads/answer/12003020)
- Johnson, Lewis and Nubbemeyer, "Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness," 2017: [kellogg.northwestern.edu](https://www.kellogg.northwestern.edu/academics-research/research/detail/2017/ghost-ads-improving-the-economics-of-measuring-online-ad/)
- Google, Meridian open-source marketing mix model: [blog.google](https://blog.google/products/ads-commerce/meridian/)
- Meta, Robyn open-source marketing mix model: [github.com](https://github.com/facebookexperimental/Robyn)
- Gordon, Zettelmeyer, Bhargava and Chapsky, "A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook," Marketing Science, 2019: [kellogg.northwestern.edu](https://www.kellogg.northwestern.edu/academics-research/research/detail/2019/a-comparison-of-approaches-to-advertising-measurement-evidence-from/)
