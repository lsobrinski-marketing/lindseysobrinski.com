---
title: "Churn is four problems added together, and you're fixing the wrong one"
seo_title: "The four kinds of churn, and why the mix decides the fix"
date: 2026-09-03 09:00:00 -0500
category: churn
hero: /assets/img/blog/four-kinds-of-churn.svg
hero_title: "Four kinds|of churn"
hero_motif: bars
tags: [churn decomposition, involuntary churn, activation, win-back, lifecycle marketing, retention]
description: "A failed credit card and a disappointed customer both show up as a cancellation. Splitting churn into involuntary, never-activated, completed, and dissatisfied is what turns a rate into a plan."
faq:
  - q: What are the different types of customer churn?
    a: >-
      Four that behave differently enough to need separate work. Involuntary
      churn is a payment failure, not a decision. Never-activated churn is a
      customer who bought and never reached the value they bought for. Completed
      churn is a customer whose need genuinely ended. Dissatisfied churn is a
      customer who got the value and judged it not worth the price. They have
      different owners, different fixes, and very different recoverable value,
      which is why a single churn rate cannot tell you what to do.
  - q: How do I find out what kind of churn I have?
    a: >-
      Involuntary is the easiest: it lives in your billing system as declines
      and failed retries, not in your cancellation reasons. Never-activated
      shows up as churn concentrated in the first cycle or two among customers
      who never hit whatever your first-value milestone is. Completed churn is
      visible in tenure and consumption patterns, customers who reached a
      natural end. Dissatisfied is what remains, and it is the group where
      qualitative work, cancellation surveys, and support history actually earn
      their keep.
  - q: Which type of churn should I work on first?
    a: >-
      Usually involuntary, because it needs nobody to be persuaded of anything
      and is typically the largest recoverable pool in the business. After that,
      the activation window, because a customer who never reached value is lost
      regardless of what you send them later. Win-back for the dissatisfied and
      the drifted comes last, not because it does not matter, but because it is
      the most expensive intervention with the lowest ceiling.
  - q: Is completed churn a problem?
    a: >-
      Not usually, and treating it as one is how brands end up running win-back
      campaigns at people with no remaining need. A customer whose project
      ended, whose child outgrew the size, or who finished the course did not
      fail and neither did you. The useful responses are a genuinely different
      offer, an adjacent need, or an honest acceptance that this cohort has a
      natural life and the acquisition math has to work within it.
  - q: Why does a single churn rate not tell you enough?
    a: >-
      Because it is a symptom presented as a diagnosis. The rate reports that
      customers left. It cannot say whether they left because a card expired,
      because they never got started, because they were finished, or because the
      thing was not worth the money. Those four are owned by four different
      teams, and handing the combined number to whoever runs email is how most
      retention programs end up aimed at the smallest of the four.
---

Every churn conversation starts with a single number, and the single number is why the conversation goes nowhere. Some percentage of customers left. That figure cannot tell you whether a credit card expired, whether the customer never figured out what they bought, whether they finished what they came for, or whether the thing simply was not worth the money.

Those are four different business problems with four different owners, and they arrive added together in one percentage that gets handed to whoever runs email.

## The four, and who actually owns each one

**Involuntary.** The payment failed. The card expired, the charge declined, a fraud rule fired, the billing address went stale. These customers did not decide anything, and on most subscription businesses they are a fifth to two fifths of total churn. The fix is dunning logic, card-updater coverage, retry timing, and pre-expiration outreach. That belongs to payments operations, and in most orgs it belongs to nobody at all, which is exactly why it stays broken.

**Never activated.** They bought, and then never reached the value they bought for. The box arrived and stayed unopened. The account was created and never configured. The second order never happened. This group churns early and gets reported as a marketing failure while almost always being an onboarding one.

**Completed.** They got exactly what they came for. The project ended, the child outgrew the size, the course finished. This is not a failure at all, and treating it as one produces win-back campaigns aimed at people with no remaining need. The honest responses are an adjacent offer or an acceptance that this cohort has a natural life the acquisition math has to work within.

**Dissatisfied.** They experienced the value and returned a verdict: not worth the price. The product, the service, or the price is the problem, and the only genuinely useful thing marketing can do is report that accurately to the people who can change it. A discount aimed at this group buys silence, not retention.

## Why the mix decides everything

Two businesses can report the same churn rate and need completely opposite programs.

The first is 40% involuntary. Its highest-return work is a billing project: better retry schedules, card-updater coverage, an email before the card expires rather than after it fails. No persuasion required, no margin given away, and the recovered subscriber is worth their full remaining contribution at essentially zero acquisition cost.

The second is 40% never-activated. Its billing is fine. Its problem is that four in ten customers never got to the thing they paid for, and every dollar it spends downstream is spent on people who never started. A dunning project here would return almost nothing, and a loyalty program would spend margin on the customers who were already fine.

Same rate. Opposite plans. The rate cannot distinguish them, which is why the decomposition has to come before the intervention rather than after the first program underperforms.

## The decomposition is easier than it sounds

You do not need a warehouse project to get a usable split.

Start with the billing system, not the cancellation reasons. Involuntary churn does not appear as a cancellation; it appears as failed charges and exhausted retries. Pull it directly and you usually find a number nobody in marketing had seen.

Then look at where churn sits on the tenure axis. Churn concentrated in the first cycle or two, among customers who never hit your first-value milestone, is never-activated. Pick the milestone honestly: second order, first successful use, whatever actually predicts survival in your data rather than whatever is easiest to query.

Completed churn shows up in consumption and tenure, customers who reached a natural end point rather than an abrupt one. And dissatisfied is what remains, which is the one group where cancellation surveys, support history, and actual conversations earn their keep. Do not start with the survey. Start with the three groups you can size from behavior, and let the survey explain the residual.

The [Churn Decomposition Model](/churn-decomposition.html) does the arithmetic if you want to see what the mix is worth before you go get the exact numbers. Rough and directional beats precise and absent, because the ranking is what changes the plan and the ranking is robust to being ten points wrong.

## Price each pool, then rank

Once the four are sized, convert them to money: customers in each group multiplied by the remaining contribution a saved customer would generate. Then apply an honest recovery rate, because you cannot save all of any group.

The ordering that comes out of this is nearly always the same in businesses that have never done it, and nearly always different from what the team was working on. Involuntary sits at the top because its recovery rate is high and its cost is operational. Activation sits second because the window is short and the effect is permanent. Win-back sits last, because it intervenes after the decision has been made and its only remaining tool is usually price.

That is the whole argument for decomposing before intervening. The rate tells you the patient has a temperature. The mix tells you what to treat.

## One caution about the recovery rates

Every recovery number in that ranking is a hypothesis until it survives a holdout. A share of lapsed customers return without being asked, a share of failed payments recover on the next natural retry, and a program with no control group will report all of them as saves.

This is the same discipline that separates incremental return from [self-reported credit in paid media](/blog/platform-roas-is-grading-its-own-homework/), and there is no principled reason retention should be exempt from it. Hold out a slice of every intervention, permanently, and read the difference rather than the absolute.

More on how this fits together: [churn reduction](/lifecycle/churn/) covers the cohort curves and the risk window, and [subscription economics](/lifecycle/subscriptions/) sets what a saved customer is actually worth.

So before the next retention program gets scoped: do you know which of the four you are funding, or are you funding the average?
