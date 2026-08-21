---
title: "Attribution, incrementality, MMM: stop asking which one is right"
seo_title: "Attribution vs incrementality vs MMM"
date: 2026-07-21 09:00:00 -0500
category: paid-media
hero: /assets/img/blog/attribution-incrementality-mmm-which-one.svg
image: /assets/img/blog/attribution-incrementality-mmm-which-one.png
tags: [media mix modeling, mmm, attribution, incrementality, measurement, paid media]
description: "Teams argue about attribution vs incrementality vs media mix modeling as if they have to pick one. They answer different questions and work best layered, tests calibrate the model, the model allocates, attribution steers."
faq:
  - q: What is the difference between attribution, incrementality, and media mix modeling?
    a: >-
      They answer different questions. Attribution assigns credit for observed
      conversions across the touchpoints that preceded them, it's fast and
      granular but inherits the platforms' observation bias. Incrementality
      testing uses controlled experiments (holdouts, geo tests) to measure the
      causal lift of a specific channel over a specific window. Media mix
      modeling is a top-down statistical model that estimates each channel's
      contribution across the whole plan, including channels with no click at
      all. One steers, one proves, one allocates.
  - q: Should I use attribution or incrementality?
    a: >-
      Both, for different jobs. Attribution is a fine tool for day-to-day
      steering, which creative is fatiguing, which campaign is drifting, where
      speed matters more than causal precision. Incrementality is what you use
      before a budget decision, because it measures what the spend actually
      caused rather than what a platform observed. Using attribution to steer
      and incrementality to decide is the split that keeps you fast without
      being fooled.
  - q: What is media mix modeling good for?
    a: >-
      Allocating budget across the entire plan, including the channels
      attribution can't see, CTV, out-of-home, audio, print. MMM uses
      historical spend and outcome data to estimate each channel's contribution
      and diminishing returns, so you can model how shifting budget changes
      total results. Its weakness is that it's correlational and coarse, which
      is exactly why you calibrate it against incrementality experiments rather
      than trusting it on its own.
  - q: How do the three measurement methods work together?
    a: >-
      In a loop. Incrementality tests produce causal ground-truth reads on
      specific channels. Those reads calibrate the media mix model so its
      contribution estimates match reality instead of drifting on correlation.
      The calibrated model allocates budget across everything, including the
      un-clickable channels. Attribution then steers the day-to-day execution
      inside that allocation. Tests prove, the model allocates, attribution
      steers, and the tests re-run periodically to keep the model honest.
  - q: Is attribution dead?
    a: >-
      No, but its job got smaller. Signal loss, privacy changes, and the
      structural bias of platforms grading their own homework mean attribution
      can no longer be the basis of a budget decision. It's still useful as a
      fast, directional steering instrument for in-flight optimization. The
      mistake isn't using attribution, it's using it to answer the causal
      question it was never able to answer.
---

There's a recurring argument in measurement circles that goes nowhere: attribution versus incrementality versus media mix modeling, as if you have to crown one and retire the others. It's the wrong frame. They answer three different questions, and a serious measurement program uses all three, each for the job it's actually good at.

## Three questions, three tools

**Attribution answers: which touchpoints preceded the conversions I can see?** It assigns credit across the clicks and impressions leading up to an observed sale. It's fast, granular, and available in every dashboard, and it inherits every bit of the platforms' observation bias, because it can only reason about conversions that were tracked. Attribution is a steering instrument.

**Incrementality answers: what did this spend actually cause?** It builds a controlled comparison, a holdout, a geo test, an audience suppression, and measures the lift between an exposed group and an unexposed one. It's slower and narrower, covering one channel over one window, but it's causal. Incrementality is ground truth.

**Media mix modeling answers: how should I allocate across everything, including what I can't click?** It's a top-down statistical model relating historical spend to outcomes across the whole plan, CTV, out-of-home, audio, and the trackable channels together. It's coarse and correlational, but it's the only one that can see the un-clickable channels. MMM is the allocator.

Steer, prove, allocate. Different questions. No winner.

## Why picking one always fails

Each tool, used alone, fails in a predictable way.

Attribution alone hands your budget to whichever channel is best at *observing* conversions, branded search, retargeting, and starves the demand-generation channels that don't get tracked. You optimize toward a mirror.

Incrementality alone is too slow and too narrow to run the whole plan. You can't hold out every channel every week; tests are expensive and cover one thing at a time. Ground truth, but not a steering wheel.

MMM alone is correlational and easy to fool. Without experimental calibration it drifts, confidently attributing to a channel whatever happened to move alongside it. A pretty model, unmoored from cause.

The failures are complementary, which is the tell that the tools are meant to be layered.

> Attribution is a speedometer, incrementality is a scale, MMM is a map. Nobody argues about which instrument is "right." You'd never fly with just one.

## How they actually stack

The working structure is a loop, not a hierarchy.

Incrementality tests produce causal reads on specific channels, the true lift of retargeting, of branded search, of a CTV campaign. Those reads *calibrate* the media mix model, anchoring its contribution estimates to experimental reality instead of letting them float on correlation. The calibrated model then *allocates* budget across the entire plan, including the channels attribution never sees. And attribution *steers* the day-to-day execution inside that allocation, which creative, which audience, which campaign needs attention this week.

Then you re-run the tests periodically, because channels and markets drift, and a model calibrated a year ago is a model quietly going wrong. Tests prove, the model allocates, attribution steers, and the tests refresh the whole thing on a cadence.

## Where this fits

This is the machinery underneath the [Measurement lane](/paid-media/measurement/): not a single magic metric, but three instruments doing three jobs. It's also how the [demand-generation vs demand-capture](/blog/demand-generation-vs-demand-capture/) argument finally gets settled, attribution will always flatter capture, so you need incrementality to prove what generation created and MMM to allocate between them.

Stop looking for the one true measurement method. Build the layered system: fast steering from attribution, causal truth from incrementality, whole-plan allocation from a model the tests keep honest. The teams that win the measurement conversation aren't the ones with the best single tool. They're the ones who stopped treating it as a single-tool problem.
