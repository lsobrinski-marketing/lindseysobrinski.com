---
layout: post
permalink: /blog/the-budget-mix-test-is-a-plan-c/
title: "The budget mix test is a Plan C, not a verdict"
seo_title: "The Budget Mix Test Is a Plan C, Not a Verdict"
date: 2026-11-25 09:00:00 -0600
category: paid-media
author: eric-brinker
noindex: true
sitemap: false
hero: /assets/img/blog/eric-brinker-mix-test-vs-holdout.jpg
image: /assets/img/blog/eric-brinker-mix-test-vs-holdout.jpg
hero_title: "Big swing,|or noise"
hero_motif: nodes
hero_alt: "A single large dial for one ad channel's budget turned hard to the right, and a whole-business sales line behind it lifting by the same proportion, while a second tiny dial barely moves and its line stays flat inside a band of daily noise."
tags: [incrementality, holdout testing, mmm, attribution, lift test, guest]
description: "Eric Brinker on the no-history lift test: why it only works on a big swing, where it breaks, and when a brand should graduate to a real holdout."
faq:
  - q: What is a budget mix test in marketing measurement?
    a: >-
      It is a lift test for a brand with no measurement history. You change one channel's share of total
      spend hard, up or down, and watch whether total business results move with it. If a channel is a
      large part of the budget, a big swing shows up on the bottom line even when much of its true impact
      is untracked. Eric Brinker calls it a Plan C, useful when you cannot yet run a clean holdout.
  - q: Why does a budget mix test only work on a big swing?
    a: >-
      Because your daily sales already move around on their own. To be sure a change in results came from
      the budget move and not a random good day, the move has to clear that normal noise. That threshold
      is the minimum detectable effect. Eric's rule of thumb is that a shift smaller than about 20 percent
      of your whole paid budget is probably too small to read on total results.
  - q: When should a brand switch from a mix test to a real holdout?
    a: >-
      When it has roughly 30 to 90 days of history, enough to pick comparison and holdout groups whose
      sales correlate and whose daily volumes are similar. A holdout always finds savings: either it proves
      a channel is not working and pausing it saves money, or it proves the channel is incremental and
      worth funding.
  - q: Does AI search make incrementality tests less reliable?
    a: >-
      Not on its own. A geo-holdout does not care whether the customer journey is tracked, so AI research
      in the path does not break it. The real risk is test duration. If you misjudge the consideration
      cycle and the test runs too short, it misses customers who buy later. Size the window to the real
      buying cycle, not a calculator's default.
---

You do not need a year of clean data to learn whether a channel is working. If a large share of your sales shows up untracked, you can swing one channel's budget hard and watch what the whole business does. Eric Brinker ran that test for a game studio on its first day of paid spend, when 60 percent of the results came through with no tracking at all. The catch, and the reason this is a Plan C and not a verdict, is that the swing has to be big, roughly a fifth of your entire paid budget, or the signal drowns in the noise. Below is where the method breaks and when a brand should graduate to a real holdout, in Eric's own words.

Eric is the founder of [Brinker Analytics](https://brinkeranalytics.com) and has run more than 70 incrementality tests. He picked this topic himself, because it is the question he gets most after people try the mix-shift approach. I sent him eight questions. His answers are below, lightly edited and his own.

## Stop calling them attributed conversions. Call them observed.

**You judge a channel on blended cost per result, total spend divided by total results, not only the conversions that kept their tracking. What does that change about a decision a founder would otherwise make straight from the platform dashboards?**

Platform dashboards show attributed conversions. I think "attributed" conversions should be called "observed" conversions. When you call them "observed" conversions, you quickly start asking: What is doing the observing? Is it good at observing? What does it not observe? Does observing the sale mean causing a sale? When a founder makes a decision only on platform dashboards, it is a faith assumption that the dashboards are good at observing all sales that interacted with the ad, and that those sales were caused by interacting with the ad. Unfortunately for many businesses, neither of those statements is true. Some sales come from people who saw but did not click your ad. And some sales from people who clicked your ad were people who had been to the website 7 other times this month, and those sales might have happened anyway. That is why, for some businesses on some channels, it is not even mostly true that attributed conversions are the whole picture.

If a founder starts thinking, "platform conversions can only see some sales, and only some of those sales are caused by the ad; there are also sales the platform is not recording but that are caused by the ad," the founder very quickly starts comparing platform-recorded sales to whole-business results. There are steps you can take to sharpen this comparison, like geo testing or marketing mix modeling. But using numbers besides the ones reported in the platform is a great way to keep the larger customer journey in mind, so you can truly drive the channels that push your whole business forward.

<blockquote class="pullquote">"Attributed conversions should be called observed conversions."</blockquote>

## How big does the move have to be?

**You write that a small bump will not tell you much. How do you decide how big the channel move needs to be, and what do you tell a brand that cannot afford a big move?**

How big does a channel move need to be? With a little bit of math, your LLM can analyze your previous sales to figure out how stable versus how "noisy" your daily numbers are. The wilder your daily numbers, the bigger the channel move needs to be to rise above the normal noise, just to prove that a pop in sales was not simply a random good day. This is called the "minimum detectable effect" (MDE): a sales increase that says "your previous days were high sometimes, but they were not this high for this long. You must be doing something right." If a brand cannot afford a big move, you can (A) play with the numbers until you are simulating a big move in a smaller sandbox, or (B) try a holdout test. A holdout test always finds savings. Either you prove a channel was not working, and pausing that channel in a fraction of the country saved you money, or you prove a channel absolutely must be on to help your business, and you prove that spending money makes you money.

<blockquote class="pullquote">"A holdout test always finds savings."</blockquote>

## Where the mix test starts to break

**Where does the mix test start to break, and what are the first signs the read is no longer one you would trust?**

A mix test is what small brands can do in a pinch when they do not have historical data robust enough to set the baselines they need to run a good holdout or new-channel test. The young brand I was working with, Pandamander Games, was on Day 1 of paid traffic, ever. And only on Facebook. 60 percent of their results were NOT tagged as Facebook in their internal analytics. So they assumed, "It must be all those YouTube reviews we are getting from creators." We simply increased Facebook spend and found that all results increased at the same ratio. We decreased Facebook spend, and all results decreased at the same ratio.

This worked because, as a percentage, changes to the Facebook budget were enormously visible to the portfolio. After all, it was the entire budget. This would not have worked if we doubled a new channel from 1 percent of all spend to 2 percent of all spend. It also worked because the effect of the Facebook budget change had an undeniable effect on the bottom line. A simple budget mix shift will stop working pretty quickly unless you are making radical changes, and for businesses of any serious size, that is too risky, understandably. This is not hard math, but my gut is that a budget mix shift of less than 20 percent change to your whole paid budget might be too small a change to sniff out on the bottom line.

## The share of results nobody can claim

**Your table shows a share of results nobody can claim. How do you think about that part?**

Pandamander Games saw 60 percent of their internal results come through with no tracking. For a new brand with no organic demand or prior paid traffic footprint, this is pretty high. My guess is that most brands launching with only Facebook ads should expect only 20 to 30 percent of their results at most to come with no tracking. For Pandamander, some of this was technology. Wishlisting on Steam is often done in the Steam app, which for Steam players can load directly from the Facebook ad and immediately drop tracking.

But also, this audience is extremely savvy about self-exploration, both in Google and on Steam, and extremely wary about paid advertising. These are all reasons why a legitimately caused result from a Facebook ad would NOT have Facebook tracking printed on that result in the brand's internal analytics. That is why we played around with spend levels, to confirm Facebook was affecting the overall blended business result and not just the last-click tracking with which the internal system credited Facebook.

## The bar the evidence has to clear

**You treat a close match between spend and total results as a strong read but not proof. Before you would act on it, say cut or scale a channel, what is the bar the evidence has to clear?**

There are steps a brand can take to close this confidence gap some, but in advertising there will always be a confidence gap. And that is because of customers and their windy journeys. Without an omniscient understanding of every person's mind and every variable in the universe, there will always be people who buy from a brand because of an ad that a browser cookie failed to capture.

Here is some of the evidence I would look for, if I was going to cut or scale a channel:

- Does a channel's daily or weekly spend correlate with its own last-click results?
- Is there evidence of a halo? Does it correlate with organic results, direct results, paid search results, whole-business results?
- From its last-click results, are the majority of customers new customers?
- From its analytics, are the majority of its clicks new visitors?
- Is the 30-day ROAS higher than the 1-day ROAS? And is this relative increase a bigger relative increase than other channels?

These questions can help paint a story about whether a channel converts now or later, whether it prospects or re-engages. If a channel, for example, has a sharp increase from 1-day ROAS to 30-day ROAS, brings in a healthy amount of new visitors and new customers, and correlates well with whole-business results, it may be a demand generator.

Helpful channels may have a wide variety of yeses and nos to these questions. There is no one-size-fits-all channel. Often, though, a string of nos makes it tough for a channel to remain positively impactful. But the answers can help you design the lift test you want, to prove a channel's ultimate impact on the business.

## When to graduate to a real holdout

**When does a brand have enough history to move from the mix test to a real holdout, and what should they collect now so that first holdout goes well?**

Answers vary depending on the brand's daily sales volume. This is pretty easily handled with a few different math equations that your LLM can walk you through. Broadly, though, I would look for at least 30 to 90 days of data. This can help you choose places to compare and which places to hold out. You will want to see that the groups you choose correlate with each other's sales, and also do not stray too far from each other's daily sales volume, even if you have to scale one of the groups to pretend they are the same size.

## When a mix test has pointed the wrong way

**Has a mix test ever pointed you the wrong way? What happened?**

Absolutely. A mix test is a Plan C if you cannot run a high-fidelity holdout test. A marketing mix model is really a series of mix tests. For example, I worked with a brand that dabbled in podcast sales at 1 percent of their budget, then doubled to 2 percent of their budget on the same days that their business doubled in sales. A mix test would falsely attribute the business's rising tide of sales to a tiny increase in podcasts. But this brand knew to take the mix test in context. They knew better than to assign an incredible month to a few more dollars spent on podcasts.

A mix test can be helpful if you take a wild swing, let's say you double your largest channel, and see a wild change in your business. But like all business measurement, and ultimately all business action, it still leaves some gaps and risks.

## Is AI search changing how you measure?

**When someone hears about a brand in ChatGPT and buys a week later, where does that show up for you?**

The jury is out on this one, because the answer is no, possibly, and sometimes.

No: AI search being a fresh technology does not by itself mean that geo tests are less effective. AI search might mean that paid search gets fewer clicks, but that by itself does not change how well a geo test can measure. That is the beauty of a geo test. It does not care how windy or even invisible the customer journey is, or how a user may have blocked every cookie or changed their email address. It just points out areas where you spend more and compares that to what you sold in those areas.

However, your second question, about whether consideration delays can affect tests: ABSOLUTELY. If a test does not run long enough, it will not capture customers who take longer to decide to buy. It is as simple as that. When some "how long should I run my test" calculators push up their glasses and say, "well, based on the data, looks like 3.9 weeks," but they do not stop to ask, "Are you testing something that changes customers' minds in 3.9 weeks or less, or are you doing upper-funnel brand media on a $1000 AOV product that comes with a 6-to-12-month consideration cycle," those calculators and their 3.9-week suggested windows may be setting up your test for failure.

But if AI shortens someone's consideration cycle, it might actually help sharpen geo tests. And if AI moves people to buy your product who are in treatment geos but who did not see your upper-funnel TV advertising, this could show up as a false positive in your upper-funnel advertising geo test. Hopefully that will wash out over a large enough sample size. That is why the jury is out on AI. It may help in some measurement areas, it may not matter in others.

{% include author-banner.html %}

## Where to go next

Eric's thread runs straight through the measurement argument this site keeps making. If platform dashboards only show you observed conversions, start with [why platform ROAS is grading its own homework](/blog/platform-roas-is-grading-its-own-homework/). On reading a swing against the daily noise, see [a real lift or just noise](/blog/a-real-lift-or-just-noise/). When you are ready to graduate from the mix test, here is [how to run a geo-holdout test](/blog/how-to-run-a-geo-holdout-test/), [which incrementality test to run](/blog/which-incrementality-test-to-run/), and [how to size the markets and duration](/blog/geo-holdout-sizing-markets-and-duration/) so the consideration cycle Eric warns about does not sink the read. On the AI-search question, here is the companion piece on [how AI is doing the selling while paid search takes the credit](/blog/ai-does-the-selling-paid-search-takes-the-credit/).
