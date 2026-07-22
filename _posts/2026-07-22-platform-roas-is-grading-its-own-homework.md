---
title: "Platform ROAS is grading its own homework"
category: paid-media
tags: [incrementality, ROAS, media mix modeling, attribution]
description: >-
  Every ad platform reports on the conversions it can see and stays silent about
  the counterfactual. Here is how to tell how much of your reported return is
  real, and what to run first if you suspect it is not.
faq:
  - q: What is the difference between reported ROAS and incremental ROAS?
    a: >-
      Reported ROAS is revenue a platform could associate with an ad it served,
      divided by spend. Incremental ROAS is the return on revenue that would not
      have occurred without the spend. The first is observational and always
      flattering; the second requires a comparison group and is frequently
      lower, sometimes by a large multiple.
  - q: How much lower is incremental ROAS usually?
    a: >-
      It varies enormously by channel and business, which is exactly why it has
      to be measured rather than assumed. The pattern that repeats is directional
      rather than numeric: channels that intercept existing demand, like
      retargeting and branded search, tend to overstate the most, while
      upper-funnel channels tend to be undercredited. Anyone quoting you a
      universal discount factor is guessing.
  - q: What is the cheapest way to start testing incrementality?
    a: >-
      An audience suppression test on retargeting. It requires no geographic
      infrastructure, runs inside a single platform, and targets the channel
      where reported and incremental returns most often diverge. A geo holdout
      is the stronger design and the right next step, but suppression is the
      lowest-friction way to get a first real answer.
  - q: Do I still need attribution if I run incrementality tests?
    a: >-
      Yes, for a different job. Attribution is a fast directional signal for
      in-flight optimization — which creative, which audience, which day. It
      should not be the basis of a budget reallocation. Tests establish causal
      truth periodically; a mix model turns that into continuous allocation;
      attribution handles the daily tactical read.
  - q: How long should an incrementality test run?
    a: >-
      Long enough to clear your purchase consideration cycle plus the reporting
      lag, which for most businesses means several weeks rather than several
      days. Ending a test early because the result looks clear is the single
      most common way these studies produce confident wrong answers.
---

There is a diagnostic that takes about ten minutes and tells you most of what
you need to know about your measurement. Pull the revenue each ad platform
reported last quarter. Add it up. Compare it to what the company actually
booked.

If the platforms claim more revenue than the business earned, you are not
looking at a reporting bug. You are looking at the structural condition of
platform attribution, and every budget decision made on those numbers inherited
it.

## Why the numbers overlap

An ad platform can only observe conversions it can associate with an impression
or click it served. That is a reasonable thing for it to report and an
unreasonable thing to run a business on, for three reasons.

**It cannot see the counterfactual.** The platform has no view of what the buyer
would have done without the ad. A customer who was going to purchase anyway, saw
a retargeting ad on the way, and converted is counted as a full win.

**It cannot see the other platforms.** Two channels touching the same buyer will
both claim the conversion. Neither is lying by its own rules. The rules just do
not compose.

**It is optimizing toward what it can see.** Delivery systems find the users
most likely to convert, which frequently means the users already intending to.
The system then reports the resulting conversions as evidence it worked.

The net effect is a bias toward whichever channels are best at *observing*
conversions — usually branded search and retargeting — and away from the
channels that generated the demand those channels intercepted.

## What incrementality actually asks

Incremental ROAS asks a narrower and harder question: what is the return on
revenue that would not have happened otherwise?

Answering it requires a comparison group. There is no way around that, and no
amount of modeling on observational data substitutes for one.

### Geo holdouts

Split markets into test and control, suppress spend in control, and read the
difference in total business outcomes. Cleanest option for channels without
clean user-level tracking, and the only honest way to evaluate CTV, audio, and
out-of-home.

### Audience suppression

Withhold a randomized share of an addressable audience. Well suited to
retargeting and lifecycle, which is fortunate, because those are the channels
where inflated reporting is most common.

### Platform lift studies

Cheapest to run and worth using, with the caveat that you are asking a party to
grade itself under rules it wrote. Useful directionally, weak as sole evidence
for a major reallocation.

## The result is usually uncomfortable

The common finding is that retargeting and branded search are substantially less
incremental than reported, and that upper-funnel channels are doing more than
they were credited for. This is uncomfortable because it inverts the internal
scoreboard, and the channels that look worst under scrutiny are typically the
ones someone has been reporting as wins for years.

It is also the finding that unlocks growth, because it means there is
underexploited capacity in channels the current measurement was systematically
undervaluing.

## What to do first

Start with one test on the channel carrying the most spend with the weakest
causal evidence. That is almost always retargeting or branded search. Size it so
the result is unambiguous, run it long enough to clear the purchase cycle, and
agree in advance what result would change the budget — before anyone has seen
the outcome and started negotiating with it.

Then calibrate. Tests give you causal truth about a narrow window; a mix model
gives you continuous allocation across everything. Using the first to anchor the
second is the structure that holds up over time.

The goal is not to prove any channel wrong. It is to be able to answer, in a
room with a CFO, how you know.
