#!/usr/bin/env python3
"""
indexnow_ping.py - submit new/changed URLs to IndexNow after a Pages build.

Reads the freshly built live sitemap, diffs <loc>/<lastmod> against a committed
snapshot of what was submitted last time, verifies each changed URL is live
(HTTP 200), and POSTs the changed set to IndexNow (Bing + the shared network).
On the first run (no snapshot) it submits the full list. It then writes an
updated snapshot so the next build diffs against it.

Config via environment (all optional; defaults target lindseysobrinski.com):
  INDEXNOW_SITE          https://lindseysobrinski.com
  INDEXNOW_HOST          lindseysobrinski.com
  INDEXNOW_KEY           32-char hex key (matches /<key>.txt at the site root)
  INDEXNOW_KEY_LOCATION  https://lindseysobrinski.com/<key>.txt
  INDEXNOW_ENDPOINT      https://api.indexnow.org/indexnow
  INDEXNOW_PREV          path to the previous snapshot (may not exist yet)
  INDEXNOW_OUT           path to write the new snapshot
  INDEXNOW_DRY_RUN       set to 1 to skip the POST (prints what it would send)

A snapshot line is "<loc>\t<lastmod>". Success is HTTP 200 or 202; only
successfully submitted URLs advance in the snapshot, so a URL that is not yet
live (or a failed POST) is retried on the next build. The key is public by
design (it is served at its .txt location); it is not a secret.
"""
import os, sys, json, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET

SITE = os.environ.get("INDEXNOW_SITE", "https://lindseysobrinski.com").rstrip("/")
HOST = os.environ.get("INDEXNOW_HOST", "lindseysobrinski.com")
KEY = os.environ.get("INDEXNOW_KEY", "7af2a91ba35a8a52d8259ca68034c21d")
KEY_LOCATION = os.environ.get("INDEXNOW_KEY_LOCATION", f"{SITE}/{KEY}.txt")
ENDPOINT = os.environ.get("INDEXNOW_ENDPOINT", "https://api.indexnow.org/indexnow")
PREV = os.environ.get("INDEXNOW_PREV", "")
OUT = os.environ.get("INDEXNOW_OUT", "submitted.tsv")
DRY = os.environ.get("INDEXNOW_DRY_RUN", "") not in ("", "0", "false", "False")
MAX_URLS = 10000
UA = "indexnow-ping/1.0 (+https://lindseysobrinski.com)"
SM_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def _bust(url):
    return f"{url}{'&' if '?' in url else '?'}nocache={int(time.time()*1000)}"


def _get(url, timeout=30):
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    return urllib.request.urlopen(req, timeout=timeout)


def get_sitemap():
    # Cache-bust: the CDN caches sitemap.xml, so a plain fetch can be stale
    # right after a build and miss the post that just published.
    with _get(_bust(f"{SITE}/sitemap.xml")) as r:
        data = r.read()
    root = ET.fromstring(data)
    out = {}
    for u in root.findall("sm:url", SM_NS):
        loc = (u.findtext("sm:loc", default="", namespaces=SM_NS) or "").strip()
        lm = (u.findtext("sm:lastmod", default="", namespaces=SM_NS) or "").strip()
        if loc:
            out[loc] = _effective_lastmod(loc, lm)
    return out


def _effective_lastmod(loc, lm):
    # The standalone tool pages (roas.html, geo.html, ...) are pure static HTML
    # with no front-matter date, so jekyll-sitemap stamps their <lastmod> with
    # the build time, which changes on every rebuild. Treating that as a real
    # change would re-ping them on every build forever. Ignore the lastmod for
    # .html pages (they ping once, when first added); keep real content-derived
    # lastmods for blog posts so a genuine edit still re-pings.
    if loc.endswith(".html"):
        return ""
    return lm


def load_prev(path):
    prev = {}
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                parts = line.split("\t")
                prev[parts[0]] = parts[1] if len(parts) > 1 else ""
    return prev


def is_live_200(url):
    try:
        with _get(_bust(url)) as r:
            return 200 <= getattr(r, "status", r.getcode()) < 300
    except Exception as e:
        print(f"  check failed for {url}: {e}")
        return False


def submit(urls):
    body = json.dumps({
        "host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.getcode(), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def main():
    current = get_sitemap()
    print(f"sitemap: {len(current)} URL(s)")
    if not current:
        print("empty/unreadable sitemap; aborting without changes")
        return 0

    prev = load_prev(PREV)
    first_run = not prev
    changed = sorted(
        loc for loc, lm in current.items()
        if loc not in prev or prev.get(loc) != lm)
    print(f"{'first run (full submit)' if first_run else 'delta'}: "
          f"{len(changed)} changed URL(s)")

    ok_changed = []
    for loc in changed:
        if is_live_200(loc):
            ok_changed.append(loc)
        else:
            print(f"  skip (not 200 live, will retry next build): {loc}")

    submitted_ok = set()
    if not ok_changed:
        print("nothing to submit")
    elif DRY:
        print("DRY RUN - would submit:")
        for u in ok_changed:
            print("   ", u)
    else:
        for i in range(0, len(ok_changed), MAX_URLS):
            batch = ok_changed[i:i + MAX_URLS]
            code, resp = submit(batch)
            print(f"IndexNow POST {len(batch)} url(s) -> HTTP {code}")
            for u in batch:
                print("  submitted:", u)
            if code in (200, 202):
                submitted_ok.update(batch)
            else:
                print(f"  WARNING non-2xx body: {resp[:500]}")

    # Build the next snapshot. Unchanged URLs carry forward; successfully
    # submitted URLs advance to the new lastmod; changed URLs we could not
    # confirm/submit keep their old value (or stay absent) so they retry.
    changed_set = set(changed)
    new = {}
    for loc, lm in current.items():
        if loc not in changed_set:
            new[loc] = lm
        elif loc in submitted_ok:
            new[loc] = lm
        elif loc in prev:
            new[loc] = prev[loc]
        # else: brand-new and not submitted -> omit so it is re-detected

    with open(OUT, "w", encoding="utf-8") as f:
        for loc in sorted(new):
            f.write(f"{loc}\t{new[loc]}\n")
    print(f"wrote snapshot: {OUT} ({len(new)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
