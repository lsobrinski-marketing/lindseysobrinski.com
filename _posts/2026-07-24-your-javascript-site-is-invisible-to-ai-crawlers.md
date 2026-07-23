---
title: "Your JavaScript site is invisible to AI crawlers"
seo_title: "Is your JavaScript site invisible to AI crawlers?"
date: 2026-07-24 09:00:00 -0500
category: technical-seo
tags: [javascript seo, rendering, ai crawlers, gptbot, generative engine optimization, prerendering]
description: "Most AI crawlers don't run JavaScript. If your product content only appears after JS executes, the engines answering your buyers' questions can't see it. Here's the 30-second way to prove it — and the fix."
faq:
  - q: Do AI crawlers like GPTBot and PerplexityBot execute JavaScript?
    a: >-
      No. The major AI crawlers — GPTBot and OAI-SearchBot (ChatGPT), ClaudeBot,
      and PerplexityBot — do not render JavaScript. They fetch the raw HTML and
      read what's in it. Googlebot renders JavaScript, but on a delay and
      imperfectly. So if your content only appears after JavaScript runs in the
      browser, the AI engines that increasingly answer your buyers' questions
      see an empty page.
  - q: How do I check whether my site is visible without JavaScript?
    a: >-
      Two 30-second tests. First, disable JavaScript in Chrome (DevTools →
      Settings → Debugger → Disable JavaScript) and reload a product or category
      page; if it goes blank or shows only a nav shell, that's what most crawlers
      see. Second, right-click and View Source (not Inspect) on the same page and
      search for your product name or price — if it isn't in the raw HTML, it
      isn't there for a crawler that doesn't render JS.
  - q: What's the fix for a client-rendered site that AI crawlers can't read?
    a: >-
      Serve real HTML to crawlers. The options, fastest to most permanent: a
      prerender layer (middleware that detects bots and hands them a cached, fully
      rendered HTML version) can go live in days with no front-end changes;
      static generation (SSG) pre-builds pages to HTML; and server-side rendering
      (SSR) renders every page on the server by default. Prerendering is the
      quickest way to become visible; native SSR is the durable end state.
  - q: If Google renders JavaScript, why does this still matter for SEO?
    a: >-
      Because Google renders on a delay and AI engines don't render at all, and
      the answer layer is where a growing share of discovery now happens. Even for
      Google, render-dependent content gets crawled and indexed more slowly, which
      hurts on a large site with a crawl-budget problem. And when ChatGPT or
      Perplexity assembles an answer about your category, a page it can't read
      simply doesn't exist to it — so it uses whatever it can read instead, which
      is usually someone else.
---

Open a product page on your site. Now disable JavaScript in your browser and reload it.

If the page goes blank — or leaves you with a bare navigation shell and no product, no price, no description — you've just seen your site the way most of the machines reading it right now do. That includes every major AI crawler. And it means the engines your buyers increasingly ask before they ever reach you are answering questions about your products from a page they cannot see.

This is the most consequential technical problem I find on large ecommerce sites, and almost no one is looking at it, because on a normal browser everything renders perfectly. The gap only shows up when you look the way a crawler looks.

## Most crawlers don't run your JavaScript

There's a quiet assumption baked into modern front-end architecture: that the client will execute the JavaScript, so the server can ship a near-empty HTML shell and let the browser build the page. For human visitors, fine. For crawlers, it's the difference between a full page and a blank one.

Googlebot renders JavaScript, but on a delay and imperfectly — render-dependent content gets discovered and indexed more slowly, which matters enormously on a large site already fighting for crawl budget. The AI crawlers don't render it at all. GPTBot and OAI-SearchBot (ChatGPT), ClaudeBot, and PerplexityBot fetch your raw HTML and read what's in it. One analysis of hundreds of millions of GPTBot fetches found no evidence of JavaScript execution whatsoever. If your content isn't in the HTML, it isn't in their world.

On one enterprise retail site I looked at, the core templates — product listing pages, product detail pages, even the main navigation — returned essentially nothing without JavaScript. The raw HTML was a loader and a bundle of scripts. Every crawler that doesn't render JS was arriving, fetching that shell, and leaving with nothing to index or cite.

## The 30-second proof

You don't need a crawler or a tool to check this. You need thirty seconds and two clicks.

**Test one — turn JavaScript off.** In Chrome, open DevTools, go to Settings, and check "Disable JavaScript." Reload a product or category page. What's left is roughly what a non-rendering crawler sees. If the products vanished, so did your visibility to them.

**Test two — read the raw source.** Right-click the same page and choose View Source — not Inspect. Inspect shows the rendered DOM after JavaScript has run; View Source shows the actual HTML that was delivered. Search it for a product name or a price. If it's not in there, a crawler that doesn't render JavaScript never saw it.

Do those two things on your highest-value pages before you read another word about AI search strategy. Everything downstream depends on the answer.

## Why this is a discovery problem, not a rendering nicety

Here is the part that turns a technical detail into a revenue issue. When someone asks ChatGPT or Perplexity a question about your category, the engine assembles an answer from what it can read. If it can't read your product pages, it doesn't wait for you — it fills the gap with what it *can* read: third-party roundups, reviews, forum threads, competitors. Your brand gets described secondhand, from stale and incomplete sources, in an answer you had no part in shaping.

So the brand ends up narrated by everyone except itself. The catalog is current, the prices are live, the reviews are real — and none of it reaches the engine, because all of it lives on the far side of a JavaScript execution the crawler never performs. Meanwhile a competitor with server-rendered HTML gets read directly, cited accurately, and recommended.

You cannot be the source of truth about your own products if the systems doing the answering can't open the page.

## The fix, fastest to most permanent

The goal is simple to state: serve real HTML to crawlers. There are three ways there, and they're not mutually exclusive.

**A prerender layer** is the fastest. Middleware detects a bot request and serves it a cached, fully rendered HTML version of the page — products, prices, reviews, structured data, all visible — while human visitors keep getting the existing experience. It requires no front-end rewrite and can be live in days. It's the quickest route from invisible to readable.

**Static generation** pre-builds pages to HTML at deploy time, so the content exists in the markup for everyone, crawler or not.

**Server-side rendering** is the durable end state: every page renders full HTML on the server by default, with JavaScript enhancing rather than creating the content. It's more work and usually a phased migration, but it removes the problem at the root.

Start with prerendering to stop the bleeding, plan the move to native rendering on your own timeline. The sequencing matters less than the principle: JavaScript may enhance the page, but it must not be the thing that makes the content exist.

## How to know you fixed it

Measure it the way the crawlers experience it. Baseline first — crawl your key templates as a non-rendering bot, or just run the two tests above, and document which page types come back empty. After the fix, confirm that GPTBot, ClaudeBot, and PerplexityBot receive full HTML with products and prices in it, and watch whether your pages start showing up — accurately — when you ask the engines about your category.

The test that started this piece is also the one that ends it. Disable JavaScript, view the source, and look for your products. When they're there in the raw HTML, so are you.
