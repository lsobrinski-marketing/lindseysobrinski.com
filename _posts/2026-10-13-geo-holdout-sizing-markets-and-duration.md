---
title: "How many markets and how long does a geo-holdout actually need?"
seo_title: "How many markets and how long for a geo holdout?"
date: 2026-10-13 09:00:00 -0500
category: paid-media
hero: /assets/img/blog/geo-holdout-sizing-markets-and-duration.svg
image: /assets/img/blog/geo-holdout-sizing-markets-and-duration.png
hero_title: "How many|markets?"
hero_motif: bars
tags: [geo holdout, sample size, minimum detectable effect, test duration, matched markets, measurement]
description: "Market count and duration come from a power analysis, not a rule of thumb. How minimum detectable effect and spend size a geo-holdout test."
faq:
  - q: How many markets do I need for a geo holdout?
    a: >-
      As many as your power analysis requires to detect the smallest lift you
      care about. There is no universal count. The number rises as your expected
      effect shrinks, your spend falls, or your markets are noisier and less
      alike. A handful of mismatched markets will not detect anything reliable;
      the point is to size for the effect you need to see, not to a fixed number.
  - q: How long should a geo holdout run?
    a: >-
      Long enough to clear the week-to-week noise and to capture the channel's
      lag to effect, but not so long that seasonality and drift contaminate it.
      Upper-funnel channels whose impact builds over time need longer windows
      than direct-response channels. Set the duration, like the market count,
      from a power analysis against your expected effect, and define it before
      the test starts.
  - q: What is minimum detectable effect?
    a: >-
      The smallest true lift your test is designed to detect reliably. You set it
      first, before anything else, because it drives both how many markets you
      need and how long you run. A smaller minimum detectable effect, say a 3%
      lift rather than a 10% lift, demands far more markets and more time. If you
      cannot specify it, you cannot size the test.
  - q: What happens if my geo test is too small?
    a: >-
      It fails quietly. An underpowered test returns a result that looks like
      "no effect," when the truth may be that the effect was real but too small
      for the test to see. You then cut a channel that was working, or keep one
      that was not, with false confidence. An underpowered test is worse than no
      test, because it produces a wrong answer that looks like data.
---

The real answer is that there is no fixed number. A geo-holdout needs enough matched markets, and enough time, to detect the smallest lift you care about. That minimum detectable effect, set against your spend and your baseline noise, decides both the market count and the duration. Size it with a power analysis, not a rule of thumb.

## What's in this piece

- Why sizing decides whether the test can detect anything at all
- Minimum detectable effect: the number you set first
- How many markets you actually need, and why matched pairs matter
- How long to run it
- How much to hold out, and why under-holding quietly kills the test
- A pre-test checklist before you spend a dollar

## Why sizing decides whether the test can detect anything at all

Most failed geo-holdouts do not fail because the channel did nothing. They fail because the test was never built to detect what the channel did. A geo experiment compares outcomes in treatment markets against what the control predicts they would have done, and the signal you are trying to read is small relative to the ordinary week-to-week swing in sales. If the test is too small, that signal is buried in the noise, and the result comes back as a flat line that you misread as "no effect."

This is the whole game, and it is a statistical-power problem before it is a marketing one. The same discipline that separates [a real lift from noise](/blog/a-real-lift-or-just-noise/) governs whether your geo-holdout can see anything at all. Google's geo-experiment methodology, from Vaver and Koehler, is built around exactly this: randomize non-overlapping regions, and estimate the effect against a modeled baseline with a known level of precision, in [their 2011 paper](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/). Precision is not a detail you check at the end. It is the thing you design for at the start.

## Minimum detectable effect: the number you set first

Before markets, before duration, before spend, you set the minimum detectable effect. That is the smallest true lift you want the test to catch reliably. It is a business decision, not a statistical one: how small a result would still change what you do. If a 3% lift would make you keep the channel and a 2% lift would make you cut it, your minimum detectable effect is around there, and you must build a test that can resolve it.

The reason this comes first is that everything else scales off it. A test built to detect a 10% lift is far cheaper than one built to detect a 3% lift, because the smaller effect is harder to distinguish from noise, so it needs more markets and more time. Teams that skip this step and ask "how many markets" first have the order backward. They are picking a sample size for a target they never defined. If you cannot state your minimum detectable effect, you are not ready to size the test.

## How many markets you actually need, and why matched pairs matter

Once the minimum detectable effect is set, the market count follows from it, and from how well your markets match. The number rises as the effect you want to detect shrinks, as the spend behind the test falls, and as your markets get noisier and less alike. There is no universal figure, which is why any blanket "you need N markets" claim should make you suspicious.

Matching is where the leverage is. Two markets that moved together before the test, in sales trend, seasonality, and size, make a far more precise comparison than two that did not, because the control predicts the treatment market more accurately. Good matching effectively buys you statistical power: well-matched markets detect a smaller effect with the same count. This is why practitioners build matched pairs or synthetic controls rather than splitting markets at random with no regard to history. The quality of the match does as much work as the number of markets.

## How long to run it

Duration is the second output of the same power analysis, and it answers a different question than "how many weeks feels right." You need enough time for three things. First, the channel's lag to effect: upper-funnel media builds over weeks, so a window that fits a direct-response channel will understate it. Second, enough measurement periods to average out the week-to-week noise, which is the same precision logic as the market count. Third, a clean pre-period, so the model knows how the markets relate before you changed anything. Google's work on [running geo experiments continuously](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/) formalizes this time dimension, estimating effects within a regression framework over defined test periods.

The failure mode at both ends is real. Too short, and the effect has not accumulated and the noise has not averaged out. Too long, and seasonality, promotions, and drift contaminate the comparison. The answer is to set the window from your expected effect and your channel's lag, and to fix it before you start, so you are not tempted to extend the test until it finally shows the result you wanted.

## How much to hold out, and why under-holding quietly kills the test

Under-holding is the most common way a well-intentioned test produces nothing. If you hold only a little spend out of only a few markets, the change you are trying to measure is tiny, and a tiny change cannot clear the noise. The instinct to protect revenue by keeping most of the spend on is exactly what guarantees the test cannot see anything, and you spend the budget and the weeks and learn nothing.

A credible test needs a large enough contrast between treatment and control to move the outcome measurably. That usually means holding out a meaningful share of spend in a meaningful number of markets, sized to your minimum detectable effect, not the smallest cut you are comfortable with. The short-term revenue you forgo in the held-out markets is the price of the answer, and it is almost always smaller than the cost of running the wrong budget for a year on a number you never tested. If the result tells you the channel is incremental, you have validated spend that earns its place. If it does not, you have found budget to move, which is the same reason to read the test on [incremental lift rather than attributed ROAS](/blog/incremental-roas-the-number-a-cfo-trusts/).

## A pre-test checklist before you spend a dollar

Before the test goes live, confirm these in order.

First, state the minimum detectable effect, the smallest lift that would change your decision. Second, run the power analysis that turns that effect, your spend, and your market variance into a market count and a duration. Third, build matched treatment and control markets from pre-period history, not from a random split. Fourth, decide the hold-out share, large enough to create a measurable contrast. Fifth, fix the window and the primary metric in writing before launch, so the test cannot be quietly extended or re-cut to a friendlier answer. Sixth, write down what each outcome will make you do, so the result drives a decision rather than a debate.

The deeper mechanics of running the test live in the [how-to](/blog/how-to-run-a-geo-holdout-test/), and the question of whether to run one yourself at all is covered in the [pilot-before-a-vendor piece](/blog/geo-holdout-pilot-before-a-measurement-contract/). If you are still choosing between a geo-holdout and another method entirely, start with [which incrementality test to run](/blog/which-incrementality-test-to-run/). But the sizing is the part that decides whether any of it works. A geo-holdout that is too small does not give you a cautious answer. It gives you a confident wrong one.

## Sources

- Jon Vaver and Jim Koehler, "Measuring Ad Effectiveness Using Geo Experiments," Google, 2011: [research.google](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)
- Google, "Estimating Ad Effectiveness using Geo Experiments in a Time-Based Regression Framework": [research.google](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/)
