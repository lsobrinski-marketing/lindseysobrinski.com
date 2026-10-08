---
title: "When the ruler moves, your dashboard calls it performance"
seo_title: "When the ruler moves: keep a metric-change log"
date: 2026-10-20 09:00:00 -0500
category: paid-media
hero: /assets/img/blog/when-the-ruler-moves.svg
image: /assets/img/blog/when-the-ruler-moves.png
hero_title: "The ruler|moved"
hero_motif: bars
tags: [paid media, measurement, attribution, analytics, reporting, shopify]
description: "Shopify, Search Console, Meta and Google all changed how they count in the last year. None of it was performance. Here is the log every team should keep."
faq:
  - q: Why did my Shopify conversion rate change in September 2026?
    a: >-
      Shopify changed how it measures sessions between September 21 and 23, 2026:
      sessions no longer reset at midnight UTC, some sessions without a pageview
      are counted, and identified bot sessions are filtered out by default.
      Shopify says orders, sales and customer counts are not affected and
      recommends treating post-update data as a new baseline.
  - q: Were Google Search Console impressions wrong?
    a: >-
      For a period, yes. Google says a logging error prevented Search Console
      from accurately reporting impressions from May 13, 2025 until April 27,
      2026. Impressions, CTR and average position were affected; clicks were not.
  - q: What counts as a view in Google Demand Gen?
    a: >-
      Google's help page says a view is counted when at least 1 pixel of an ad is
      on screen for any time. That is looser than the previous Active View
      standard, which required at least 50% of the ad to be visible for one
      continuous second, so reported view-through conversions can rise without any
      change in performance.
  - q: What changed in Meta's attribution in 2026?
    a: >-
      Meta removed the 7-day and 28-day view windows from the Ads Insights API on
      January 12, 2026. In March 2026 it was reported that click-through
      attribution now counts link clicks only, with other engagement moved to a
      separate engage-through attribution, and that the video engaged-view
      threshold fell from 10 seconds to 5.
  - q: How do I avoid misreading a metric change?
    a: >-
      Keep a dated log of every platform definition change, annotate dashboards
      on the change date, restate baselines instead of comparing across the
      break, and anchor reporting on business numbers the platforms do not
      define, such as orders, new customers and contribution margin.
---

In late September, conversion rates moved overnight for a lot of Shopify stores. The [session measurement rollout](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/session-measurement-update) ran from September 21 to 23, 2026, and it changed how sessions are counted: they are based on continued activity instead of ending at midnight UTC, some sessions without a pageview now count, and identified bot sessions are filtered out by default. Divide the same orders by a different session number and the conversion rate changes.

Orders did not change. Shopify said so plainly: "Your orders, sales, and customer counts aren't affected by this update," and told merchants to treat it as a measurement change and use the new data as the baseline. That sentence is the whole discipline this post is about. Every dashboard depends on a definition someone else controls, and when the definition moves, the number moves with it, and that is not news about your business.

## Four rulers moved in a year

Shopify was one of four this year. Its change actually makes some numbers more accurate, because filtering bots removes traffic that was never going to buy, and bot classification applies only to sessions from October 7, 2025 and after. Accuracy and comparability are different things, though, and the break still has to be marked.

Search Console disclosed a bigger one. Google says a [logging error](https://support.google.com/webmasters/answer/6211453?hl=en) prevented it from accurately reporting impressions from May 13, 2025 until April 27, 2026, affecting impressions, click-through rate and average position, though not clicks. On the same page, Google noted that as of May 7, 2026, FAQ rich results no longer appear in Search, which removes a surface a lot of pages were counting on.

Meta narrowed what it counts. It removed the [7-day and 28-day view windows](https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/) from the Ads Insights API on January 12, 2026. And in March it was [reported](https://www.socialmediatoday.com/news/meta-updates-ad-metrics-to-align-with-other-platforms/813712/) that click-through attribution now counts link clicks only, with likes, shares and saves moved to a renamed engage-through attribution, and that the video engaged-view threshold dropped from 10 seconds to 5.

Google is loosening one in the other direction. Its help page says a Demand Gen [view is counted](https://support.google.com/google-ads/answer/16399666?hl=en) when at least 1 pixel of an ad is on screen for any time, where the previous Active View standard required at least 50% of the ad to show for one continuous second. Demand Gen display ads are [moving to that looser definition](https://searchengineland.com/google-changes-view-through-conversion-reporting-for-demand-gen-display-ads-493504) for view-through attribution, rolling out over the coming weeks. Going from half the ad for a second to one pixel for any instant will make view-through conversions look better with nothing changing in the market.

## Why teams read definition changes as performance

The reason this fools people is structural. A dashboard shows the number, not the definition behind it. Nobody owns reading the release notes. And good news gets explained faster than bad news, so a jump gets a victory lap and a drop gets an investigation, when both might be the same ruler moving. This is the same reason it is hard to [tell a real lift from noise](/blog/a-real-lift-or-just-noise/): without a controlled read, you are interpreting a number whose meaning may have shifted underneath you.

It is not new. Meta's 2021 move to a [7-day click, 1-day view default](https://developers.facebook.com/blog/post/2021/01/19/actions-partners-mobile-web-advertisers/) warned it "may result in a decrease in the number of reported conversions," and the GA4 transition changed what a [session and a bounce even meant](https://support.google.com/analytics/answer/11986666?hl=en) before Universal Analytics stopped processing on July 1, 2023. Site changes do this too: a replatform can shift a metric in ways that only [surface a quarter later](/blog/migration-seo-90-days-later/), long after anyone connects the change to the number.

The tell is timing. A real change in the business shows up gradually and across related numbers: orders, sessions and revenue moving together. A definition change shows up all at once, on one metric, on the date of a release you can look up. When a single number jumps overnight while everything around it stays flat, the ruler moved. That is not a hunch. It is the first thing to rule out, and it takes five minutes if someone kept the log.

## Some rulers move toward the platform

Not every change is neutral in whose favor it cuts. When a platform widens what counts as a view or narrows what counts as a click, it changes how much credit it can claim for itself. That is the quiet version of the problem where [platform reporting grades its own homework](/blog/platform-roas-is-grading-its-own-homework/). To be fair, not all of these moves favor the platform. Meta's click change narrows the credit it can take. But every one of them changes the scoreboard, and a scoreboard change is not a score change. A buyer who does not track these changes will, over a year, slowly inherit a better-looking story than the business earned, one definition at a time. Nobody decides to do that. It happens by default, because the numbers arrive already changed and the release notes arrive in an inbox nobody reads. One more reason to discount impression-based credit: a served impression was never the same thing as a seen ad, and Omnicom found [65% of US consumers avoid advertising to some degree](https://digiday.com/media-buying/omnicom-media-digs-into-the-reasons-people-avoid-ads-and-offers-solutions-for-clients/), with 41% paying for subscriptions to avoid it.

## Zero-click made this personal

Search reporting has moved more in the last year than in the five before it, and it happened while AI answers started taking the clicks that used to arrive. The num=100 results parameter going away in mid-September 2025 is a good example of how much a counting change can distort: in [one analysis of 319 properties](https://searchengineland.com/google-num100-impact-data-462231), 87.7% saw impressions decline and 77.6% lost unique ranking terms, with no change in what they actually ranked for. Read the impression line alone and you would think the sky fell.

I have been on the right side of that trap. At a large retailer I ran growth for, AI answers started absorbing the click. I reported answer-layer visibility as visibility, not as traffic, and built the framing leadership used to judge zero-click value. If we had read the traffic line alone, we would have called it a decline. The fix was to name the surface, not just count the clicks, which is the whole point of [winning the answer box](/blog/winning-the-answer-box/) rather than the link.

## Keep a ruler log

The defense is cheap and almost nobody runs it: a dated log of every definition change. Start with this and keep adding rows.

| Date | Platform | What changed | Metrics affected | Not affected | Source | Annotated? |
|---|---|---|---|---|---|---|
| Sep 21-23, 2026 | Shopify | Session counting rules | Sessions, conversion rate | Orders, sales, customers | Help center | |
| Through Apr 27, 2026 | Search Console | Impression logging error fixed | Impressions, CTR, position | Clicks | Help center | |
| May 7, 2026 | Search Console | FAQ rich results removed | Impressions, CTR | Clicks | Help center | |
| Rolling out | Google Demand Gen | View = 1 pixel, any time | View-through conversions | Clicks | Help center | |
| Mar 2026 | Meta | Click = link clicks only; view threshold 10s to 5s | Click-through, engaged views | Spend | Social Media Today | |
| Jan 12, 2026 | Meta | 7-day and 28-day view windows removed | View-attributed conversions | Click conversions | Meta for Developers | |

Three moves make it work. First, one owner reads release notes and help-page change logs weekly; this is a half-hour job that nobody is assigned. Second, annotate every dashboard on the date of a change, and restate the baseline rather than comparing across the break. Third, anchor reporting on the numbers the platforms do not define: orders, revenue, new customers, contribution margin, read through [the right mix of attribution, incrementality and modeling](/blog/attribution-incrementality-mmm-which-one/).

The last time a metric in your weekly report jumped, did anyone check whether the definition changed first?
