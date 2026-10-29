---
title: "Migration SEO shows up 90 days later, in the crawl logs"
seo_title: "Migration SEO: Why Damage Surfaces 90 Days Later"
date: 2026-08-25 09:00:00 -0500
category: technical-seo
toc: false
hero: /assets/img/blog/migration-seo-90-days-later.png
image: /assets/img/blog/migration-seo-90-days-later.png
tags: [site migration, replatforming, 301 redirects, technical seo, redirect chains, crawl budget]
description: "A replatform rarely tanks traffic on launch day. Redirect chains, orphaned subdomains, and TTFB regressions surface in the crawl logs about 90 days later."
faq:
  - q: How long does an SEO migration take to recover?
    a: >-
      Plan for a full quarter. A clean migration can hold rankings from day one,
      but most sites see a dip that deepens for six to twelve weeks as Google
      recrawls and reprocesses the new structure, then recovers over the next
      one to three months once the signals settle. A migration that is still
      losing ground after 90 days has an unresolved problem, not a slow
      recovery, and that is the point to audit redirects, templates, and server
      response rather than wait.
  - q: What is the most common SEO mistake in a replatform?
    a: >-
      Redirect chains. A templated path change, such as moving every post from
      one directory to another, can turn a single intended 301 into a chain of
      two, three, or more hops, and it can do that across thousands of URLs at
      once. Each extra hop bleeds a little equity and slows the crawler. The old
      URL should land on the new one in a single hop, every time.
  - q: Do I need to keep old URLs after migrating?
    a: >-
      You need to keep the mapping, not the pages. Every old URL that had
      traffic, links, or rankings must 301 to its closest live equivalent and
      stay that way. Dropping a redirect because the old page is gone is how you
      hand back the equity that URL earned. Retire the content, keep the
      redirect.
  - q: Should I submit a new sitemap after a site migration?
    a: >-
      Yes, and submit it the day you launch. A fresh XML sitemap with only the
      new live URLs, no redirected or dead ones, is how you tell Google what the
      site looks like now and speed up the recrawl. Keep an eye on the index
      coverage report afterward, because that is where the lag and the leaks
      show up first.
---

A replatform rarely tanks traffic on launch day. The damage shows up 90 days later, after Google has recrawled the site and reprocessed the redirects and new templates. Sites that hold rankings map every old URL to a single 301 with no chains, preserve titles, H1s, and internal links, and keep the sitemap and canonical signals intact from day one.

I watched this play out on an enterprise ecommerce site that moved its blog from one path to another. The launch looked clean. The pages loaded, the checklist was green, and everyone moved on. The crawl logs told a different story a quarter later: 383 redirect chains, roughly 3,264 redirect links, a decommissioned mobile subdomain throwing a DNS error, and a server that answered 36% slower than it used to. None of that was visible on launch day. All of it was already there.

## What's in this piece

- Why migration damage shows up 90 days late
- Redirect chains: 383 of them, from one path change
- The subdomains a migration leaves behind
- A slower server means a slower crawl
- The migration checklist that protects rankings
- How to watch the 90-day window

## Why migration damage shows up 90 days late

Two scoreboards are running during a replatform, and they do not agree. The first is the launch scoreboard: does the new site work, do pages render, does checkout complete. That one goes green on day one, and it is the one the whole project is organized around. The second is the SEO scoreboard: has Google recrawled the new structure, reprocessed the redirects, re-evaluated the templates, and recomputed where each page ranks. That one is measured in crawl stats, and it does not move on your schedule. It moves on Google's.

The lag is mechanical. Google does not recrawl an entire site the moment you flip it. It works through the URLs over weeks, prioritizing what it already considers important and getting to the long tail slowly. Every redirect it hits has to be followed and resolved. Every new template has to be fetched, rendered, and assessed. A large catalog can take a full quarter for the crawler to work through, which means a structural problem introduced at launch does not surface in rankings until Google has crawled enough of the site to notice it. The site that looks fine in week two is often the same site that slides in week ten.

That delay is why migrations get misdiagnosed. By the time organic traffic drops, the launch is old news, the team has moved on, and the decline gets blamed on seasonality or an algorithm update. The real cause was shipped three months earlier.

## Redirect chains: 383 of them, from one path change

The single largest problem on that site came from one decision: moving the blog from one directory to another. That is a reasonable thing to do in a replatform. Executed through templates, it manufactured redirect chains at scale. The audit found 383 chains and roughly 3,264 redirect links behind them.

A chain is what happens when an old URL does not land on the final live URL in one hop. It redirects to an intermediate URL, which redirects again, and sometimes again. Each hop is a place for equity to leak and for the crawler to spend budget it could have spent elsewhere. Google will usually follow a short chain, but it is slower, it passes along less, and long chains or loops can simply be dropped. One templated rule, applied across thousands of URLs, is all it takes to turn a clean cutover into thousands of multi-hop redirects. I have written before about how [a single line in a header template produced 92% of a site's redirect chains](/blog/one-line-in-a-header-template-was-92-percent-of-our-redirect-chains/); the pattern repeats because templates are efficient at being wrong at scale.

The fix is a rule, not a cleanup project: every old URL redirects to its final live destination in exactly one hop. Not to a category page, not to an intermediate path, not to the homepage. To the page that replaced it. Build the full old-to-new URL map before launch, flatten any redirect that points at another redirect, and test the map against the live redirects after cutover rather than trusting that the rules did what you intended.

## The subdomains a migration leaves behind

Redirects get attention. Subdomains get forgotten, and they are where two quieter problems hid on this site.

The first was a mobile subdomain, the old `m.` host, that had been decommissioned but was still throwing a DNS error. On a mobile-first-indexing site, the host Google associates with your mobile experience returning an error is not a cosmetic issue. It is a signal problem on the exact surface Google uses to index you. The subdomain was supposed to be gone. It was gone in the sense that nobody used it, and present in the sense that it still resolved to an error the crawler could find.

The second was a duplicate order-tracking subdomain that leaned on canonical tags instead of redirects. A canonical is a hint. A 301 is an instruction. When you have fully retired a host and want its equity to move, the canonical is the wrong tool, because Google can and does ignore canonicals when other signals disagree. I have seen [Google overrule canonical tags](/blog/google-is-ignoring-your-canonical-tags/) often enough that I treat them as a suggestion, not a guarantee. If a URL should no longer exist as a destination, redirect it. Reserve the canonical for genuine duplicates you intend to keep serving.

## A slower server means a slower crawl

The last finding was the easiest to miss and the most self-reinforcing. Time to first byte regressed 36%, from about 330ms to about 448ms. On its own that reads like a minor performance note. In a migration it is a crawl problem.

Google throttles crawl rate on slow servers. When responses get slower, the crawler backs off to avoid overloading the site, which means it crawls fewer URLs per day. Right at the moment you most need Google to recrawl the whole site quickly, to pick up the new structure and resolve all those redirects, a slower server stretches that process out. The crawl budget you depend on to recover shrinks exactly when the demand on it is highest. Slow server, slower crawl, longer lag before recovery. That is the loop, and it compounds with the chain problem, because chains already cost extra crawl. For the fuller mechanics of how a constrained crawl starves new and updated pages, see [crawl budget is a real constraint](/blog/crawl-budget-is-a-real-constraint/). The regression also carries a conversion cost of its own, the same tax described in [a 10-second LCP is a ranking decision](/blog/lcp-is-a-ranking-decision/).

## The migration checklist that protects rankings

The sites that hold rankings through a replatform do the same unglamorous things. This is the list worth saving.

Before launch, build the complete old-to-new URL map for every URL that has traffic, links, or rankings, and flatten it so no entry points at another redirect. Preserve the on-page equity Google already assigned: keep the titles, the H1s, and the body copy as close to the originals as the new design allows, because a page that changes its title and heading at the same time it changes its URL is asking to be re-evaluated from scratch. Preserve the internal links, so the new pages inherit the link structure that was passing authority around the old site, rather than orphaning pages the navigation no longer reaches.

At launch, put every redirect in as a single-hop 301, retire duplicate hosts with redirects rather than canonicals, and reserve canonicals for real duplicates you still serve. Publish a fresh XML sitemap containing only live URLs, and submit it in Search Console the same day. Confirm the robots file and any noindex rules carried over correctly, because a stray noindex from a staging environment is a common and silent way to lose a template's worth of pages.

## How to watch the 90-day window

A migration is not finished at launch. It is finished when the crawl stats say it is. For the first 90 days, treat crawl data as your early-warning system rather than waiting for the traffic chart to tell you something is wrong, because by the time traffic moves, the cause is months old.

Watch the index coverage report for a rising count of redirect, crawled-not-indexed, or discovered-not-indexed URLs, which is where chains and orphans announce themselves first. Watch crawl stats for response time and crawl volume, so a server regression shows up as a number rather than a mystery. Re-run a crawl of the live site a few weeks after launch and diff it against your redirect map to catch chains the templates created on their own. The point of the 90-day window is not to wait it out. It is to catch the slide while it is still a crawl-log entry and not yet a revenue line.

If you are planning a replatform or trying to explain a drop that started a quarter after one, a [technical audit](/seo-aeo-geo/technical-seo/) will tell you which of these is actually happening on your site. What does your crawl data look like 90 days after your last migration?
