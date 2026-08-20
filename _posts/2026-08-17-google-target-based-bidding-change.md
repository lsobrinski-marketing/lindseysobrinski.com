---
title: "Your campaigns were beating their targets. Google just ended that."
seo_title: "Google's target-based bidding change (Aug 2026)"
date: 2026-08-17 07:00:00 -0500
category: paid-media
hero: /assets/img/blog/google-target-based-bidding-change.png
image: /assets/img/blog/google-target-based-bidding-change.png
tags: [google ads, target cpa, target roas, smart bidding, marketing measurement, incrementality]
description: "Google's Aug 17 bidding change pulls budget-limited Target CPA/ROAS campaigns toward their target instead of beating it. That outperformance was your margin. Here's what to do."
faq:
  - q: What changed in Google's target-based bidding in August 2026?
    a: >-
      Starting August 17, 2026, budget-limited campaigns using Target CPA, Target
      ROAS (or Target CPC in Demand Gen) will optimize consistently toward the
      target you set instead of potentially outperforming it. A campaign that was
      quietly beating its target — hitting a $5 CPA against a $10 target — will
      drift up toward the $10 you configured. It applies across Search, Shopping,
      Performance Max, Demand Gen, and Travel.
  - q: Will my CPA go up after the August 17 Google Ads update?
    a: >-
      It can, if your campaigns were budget-limited and running better than their
      stated target — which is common, because most advertisers set targets with
      padding. The algorithm will now spend the slack up to the target you gave
      it. If your target was set loosely or by habit, reset it to the number that
      reflects your real economics before the platform spends to the old ceiling.
  - q: What is the Bid Target Adjustment Tool?
    a: >-
      A tool Google released July 6, 2026 so advertisers could review and adjust
      targets before the August 17 rollout. It offers four paths: keep your
      current target, lower it to match recent actual performance, set a custom
      target in between, or switch to Maximize Conversions / Maximize Conversion
      Value. Nothing changes automatically — you have to make the call.
  - q: Does hitting my target CPA mean my ads are working?
    a: >-
      Not necessarily. Target CPA and Target ROAS are reported, platform-measured
      proxies — they tell you the cost the platform associated with a conversion,
      not whether the ad caused it. A campaign can hit its target CPA while buying
      conversions that would have happened anyway. Hitting the target is a
      budgeting fact; incremental lift is the business fact, and only a holdout
      shows it.
  - q: Which campaigns are affected by the change?
    a: >-
      Budget-limited Search, Shopping, Performance Max, Demand Gen, and Travel
      campaigns using target-based bidding (Display and Hotel already behaved this
      way). App, Video reach, and Video view campaigns are not affected. It rolls
      out across Google Ads, Search Ads 360, Display & Video 360, the Editor, and
      the API.
---

Starting today, Google changed how target-based bidding works: budget-limited campaigns using Target CPA or Target ROAS will stop beating their targets and start drifting toward them. If a campaign was quietly delivering a $5 CPA against a $10 target, it'll now spend up toward the $10 you configured. Google calls that "predictability." It's also a transfer of the margin you didn't know you had.

This is not a settings bug or a scary algorithm mystery. It's a clean measurement story, and the lesson is one I keep coming back to: the number you hand an optimizer becomes the number you get — no better.

## What actually changed

As of August 17, budget-constrained campaigns on Target CPA, Target ROAS, and Target CPC (Demand Gen only) will optimize consistently toward their configured target rather than outperforming it. Previously, a campaign hemmed in by budget could deliver results *better* than its stated target. After the rollout, Google puts it plainly: a campaign that used to outperform its target "will see its performance move toward the configured target rather than its historical level."

It applies across Search, Shopping, Performance Max, Demand Gen, and Travel (Display and Hotel already worked this way), everywhere from the main interface to Search Ads 360, DV360, the Editor, and the API. App and Video campaigns are exempt. Google gave a runway: the Bid Target Adjustment Tool has been available since July 6 so you could review and reset targets before today.

## Your "outperformance" was margin — and that's what's moving

Here's the part to sit with. If your budget-limited campaign was hitting a $5 CPA against a $10 target, that $5 gap was real efficiency. It was money you weren't spending, conversions you were getting under your own ceiling. Most advertisers never optimized for it because it showed up as a pleasant surprise, not a lever.

That surprise is what's going away. When the algorithm stops beating the target and moves toward it, it spends the slack. Your effective CPA rises to meet the number you set, or your ROAS sags to it. Nothing about the market changed. The auction didn't get more expensive. The optimizer simply stopped leaving money on the table on your behalf and started using the full permission you gave it.

Which raises the uncomfortable question the change forces: was your target ever a real number, or was it a padded guess you set once and never revisited?

## The target just became the target — literally

I've written before about [the AI that gamed its own scorecard](/blog/the-ai-gamed-its-own-scorecard/): point a capable optimizer at a proxy and it will move the proxy exactly, no more and no less. This is the tame, sanctioned version. "When a measure becomes a target, it ceases to be a good measure" — and Google just made your bid target the literal outcome. The measure and the result are now the same thing by design.

That's fine *if* your target reflects the truth of your business. It's expensive if your target was aspirational, or arbitrary, or set to a round number in a hurry two quarters ago. The optimizer was covering for a loose target by outperforming it. Now the loose target is binding, and the looseness is billable.

## "Predictable" — for whom?

Google's stated reason is predictability: tighter alignment between the target you set and the performance you get makes campaigns "easier to scale." That's true, and it's genuinely useful — you can raise budgets with more confidence about where you'll land.

But notice where the surplus goes. The outperformance that used to accrue to you — cheaper conversions than you asked for — becomes inventory Google can now sell up to your ceiling. Predictable-to-target means the platform captures the gap between what you were willing to pay and what you were actually paying. This isn't a conspiracy; it's the incentive structure working as designed. The platform optimizes the metric you gave it, and it has no reason to keep beating a target you told it was acceptable. Same dynamic as [reported ROAS grading its own homework](/blog/platform-roas-is-grading-its-own-homework/): the system moves the number you rewarded, in the direction that suits it.

## Hitting the target was never the same as working

The deeper trap is treating "we hit our target CPA" as proof the spend is doing something. Target CPA and Target ROAS are reported, platform-attributed proxies. They measure the cost the platform *associates* with a conversion — not whether the ad *caused* it. A campaign can sit dead on its target while buying conversions that would have happened without it, harvesting demand that already existed.

So the honest reading of this update isn't just "my CPA might rise." It's that the number now pinned to your target was always a budgeting fact, not a business fact. The business fact is incremental lift — the revenue that wouldn't have existed without the spend — and that's established by a comparison the platform doesn't control, [a geo holdout or a matched-market test](/blog/how-to-run-a-geo-holdout-test/), not by whether a target was met. If you don't know your incremental CPA, this change is a good prompt to go find it, because you're about to pay closer to your full target for the same underlying demand.

## What to actually do this week

Don't panic-lower every target, and don't just accept the drift. Work it deliberately.

Pull the campaigns that were budget-limited at any point in the last twelve months and were running meaningfully better than their targets — those are the ones exposed. For each, decide what the target should actually be, from your real unit economics: contribution margin, true payback, the CPA at which the customer is worth acquiring. If your old target already reflects that, keep it and let the change do nothing. If your old target was padded and the algorithm's *actual* performance was closer to the truth, reset the target down to reality with the Bid Target Adjustment Tool so you don't hand back the efficiency. And where a target was always arbitrary — a number you never really believed — consider Maximize Conversions or Maximize Conversion Value instead, and control spend with budget rather than a fictional target.

The point is to make the target mean something before the platform starts spending exactly up to it. It ties to the same principle as running [one demand engine on one honest scoreboard](/blog/one-demand-engine-measured-one-way/): the number you manage to should be the number that reflects real value, not a habit.

## The takeaway

Google didn't take anything from you that it promised to keep. It stopped subsidizing a target you set too loosely and started honoring it exactly. That's the whole lesson of optimization in one release: a capable system will give you precisely what you asked for, so you'd better ask for the right thing.

So before the rollout finishes reshaping your accounts: is every Target CPA and Target ROAS in your account a real number tied to what a customer is worth — or a padded guess the algorithm was quietly rescuing you from until today?
