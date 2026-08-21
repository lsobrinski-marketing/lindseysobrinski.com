# Site fetch proxy + crawl-inspection Worker (Cloudflare)

`geo.html` and `crawl-budget.html` need a server to fetch other people's pages on
their behalf (a browser can't do that cross-origin). This Worker is that server.
It replaces the free public CORS proxies, which are unreliable, all of them were
down simultaneously on 2026-07-23, which took the analyzer offline.

Free tier covers ~100,000 requests/day, far more than these tools will ever use.
**Nothing to purchase**, the free plan is all this needs.

## Two modes

- **Default** (`?url=…`), raw pass-through of the fetched page. Used by
  `geo.html`. Unchanged, so that tool keeps working exactly as before.
- **Inspect** (`?url=…&mode=inspect`), walks the redirect chain hop-by-hop and
  returns JSON: the full redirect chain, true final status, response time, and
  the header-level signals a browser can't see (`X-Robots-Tag`, `Content-Type`,
  `Last-Modified`), plus the final HTML. Used by `crawl-budget.html` for accurate
  crawl-waste detection. **This is the accuracy upgrade**, the crawl-budget tool
  still runs without it (falling back to public proxies), just with less detail.

## Upgrading / redeploying (2 minutes, no command line)

If you already deployed the older version for `geo.html`, this is a paste-over:

1. Go to **https://dash.cloudflare.com** → **Workers & Pages** → open your
   existing Worker (e.g. `geo-proxy`).
2. Click **Edit code**. Select all, delete, and paste the entire current
   contents of [`worker.js`](worker.js). Click **Deploy**.
3. Done. The URL doesn't change, so both tools keep pointing at it. `geo.html` is
   unaffected (default mode is identical); `crawl-budget.html` now runs at full
   accuracy.

First-time deploy instead? Follow the numbered steps below.

## Deploy, no command line needed

1. Go to **https://dash.cloudflare.com** and sign in (create a free account if
   you don't have one).
2. Left sidebar: **Workers & Pages** → **Create application** → **Create Worker**.
3. Give it a name, e.g. `geo-proxy`. The name becomes part of the URL. Click
   **Deploy** (it deploys a placeholder first; that's fine).
4. Click **Edit code**. Select all the placeholder code and delete it. Paste the
   entire contents of [`worker.js`](worker.js). Click **Deploy** (top right).
5. Copy the Worker URL shown at the top, it looks like
   `https://geo-proxy.<your-subdomain>.workers.dev`.
6. Send that URL to Claude Code. It gets wired into `geo.html` as the primary
   fetch path (the free proxies stay as a fallback), then pushed live.

## Test it after deploying

The Worker intentionally refuses requests that don't come from the site, so a
plain browser visit returns "Forbidden", that's correct. To test it the way the
site does, run this (replace the URL with yours):

```bash
curl -s -H "Origin: https://lindseysobrinski.com" \
  "https://geo-proxy.YOUR-SUBDOMAIN.workers.dev/?url=https://example.com" | head
```

You should get back the HTML of example.com.

To confirm the **inspect upgrade** is live, hit a URL that redirects and check for
JSON with a `chain` field (this one 301-redirects to `https://`):

```bash
curl -s -H "Origin: https://lindseysobrinski.com" \
  "https://geo-proxy.YOUR-SUBDOMAIN.workers.dev/?mode=inspect&url=http://github.com" | head -c 400
```

You should get JSON like `{"inspect":true,...,"redirected":true,"chain":[...]}`.
If instead you get raw HTML, the Worker still has the old code, redeploy it.

## If you ever change your domain

Update `ALLOWED_ORIGINS` at the top of `worker.js`, paste the new code into the
Worker, and Deploy again.
