# GEO Analyzer fetch proxy (Cloudflare Worker)

`geo.html` needs a server to fetch other people's pages on its behalf (a browser
can't do that cross-origin). This Worker is that server. It replaces the free
public CORS proxies, which are unreliable — all of them were down simultaneously
on 2026-07-23, which took the analyzer offline.

Free tier covers ~100,000 requests/day, far more than this tool will ever use.

## Deploy — no command line needed

1. Go to **https://dash.cloudflare.com** and sign in (create a free account if
   you don't have one).
2. Left sidebar: **Workers & Pages** → **Create application** → **Create Worker**.
3. Give it a name — e.g. `geo-proxy`. The name becomes part of the URL. Click
   **Deploy** (it deploys a placeholder first; that's fine).
4. Click **Edit code**. Select all the placeholder code and delete it. Paste the
   entire contents of [`worker.js`](worker.js). Click **Deploy** (top right).
5. Copy the Worker URL shown at the top — it looks like
   `https://geo-proxy.<your-subdomain>.workers.dev`.
6. Send that URL to Claude Code. It gets wired into `geo.html` as the primary
   fetch path (the free proxies stay as a fallback), then pushed live.

## Test it after deploying

The Worker intentionally refuses requests that don't come from the site, so a
plain browser visit returns "Forbidden" — that's correct. To test it the way the
site does, run this (replace the URL with yours):

```bash
curl -s -H "Origin: https://lindseysobrinski.com" \
  "https://geo-proxy.YOUR-SUBDOMAIN.workers.dev/?url=https://example.com" | head
```

You should get back the HTML of example.com.

## If you ever change your domain

Update `ALLOWED_ORIGINS` at the top of `worker.js`, paste the new code into the
Worker, and Deploy again.
