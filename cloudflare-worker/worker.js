// Site fetch proxy + crawl-inspection endpoint — Cloudflare Worker
// ---------------------------------------------------------------------------
// A browser cannot fetch arbitrary cross-origin pages, so the on-site tools
// need a server to fetch a target URL and hand it back with CORS headers.
//
// Two modes:
//   default        — raw pass-through of the fetched page (redirects followed).
//                    Used by geo.html. Unchanged from the original proxy, so
//                    that tool keeps working exactly as before.
//   ?mode=inspect  — does NOT follow redirects blindly; instead it walks the
//                    redirect chain hop by hop and returns JSON describing what
//                    a crawler would actually experience: the full redirect
//                    chain, the true final status, response time, and the
//                    header-level signals a browser can't see (X-Robots-Tag,
//                    Content-Type, Last-Modified), plus the final HTML body.
//                    Used by crawl-budget.html for accurate crawl-waste checks.
//
// Deploy: see README.md in this folder. Free tier covers ~100k requests/day.
//
// Protections against this becoming an open proxy someone else abuses:
//   - Only serves requests coming from the site itself (Origin / Referer check)
//   - GET only, http/https targets only
//   - Blocks localhost / private-range / cloud-metadata targets (SSRF hygiene),
//     re-checked on every redirect hop so a redirect can't smuggle in an
//     internal target
//   - Caps response size, redirect hops, and fetch time
// ---------------------------------------------------------------------------

const ALLOWED_ORIGINS = [
  'https://lindseysobrinski.com',
  'https://www.lindseysobrinski.com',
];
const MAX_BYTES = 3_000_000;      // 3 MB ceiling on a fetched page
const FETCH_TIMEOUT_MS = 20_000;  // give slow sites 20s
const MAX_HOPS = 8;               // redirect chain cap (inspect mode)

const UA = 'Mozilla/5.0 (compatible; LS-SiteTools/1.1; +https://lindseysobrinski.com/crawl-budget.html)';

// SSRF hygiene: is this host an internal / metadata target we must refuse?
function hostBlocked(host) {
  host = (host || '').toLowerCase();
  return host === 'localhost' || host.endsWith('.localhost') || host.endsWith('.internal') ||
    host === '169.254.169.254' || host === 'metadata.google.internal' ||
    host === '::1' || host === '[::1]' ||
    /^127\./.test(host) || /^10\./.test(host) || /^192\.168\./.test(host) ||
    /^169\.254\./.test(host) || /^172\.(1[6-9]|2\d|3[01])\./.test(host);
}

function validTarget(raw) {
  let u;
  try { u = new URL(raw); } catch { return { err: 'Invalid target URL' }; }
  if (u.protocol !== 'http:' && u.protocol !== 'https:')
    return { err: 'Only http/https targets allowed' };
  if (hostBlocked(u.hostname)) return { err: 'Target host not allowed' };
  return { u };
}

async function timedFetch(url, redirect, signal) {
  return fetch(url, {
    method: 'GET',
    redirect,
    signal,
    headers: { 'User-Agent': UA, 'Accept': 'text/html,text/plain,*/*' },
  });
}

export default {
  async fetch(request) {
    const origin = request.headers.get('Origin') || '';
    const referer = request.headers.get('Referer') || '';
    const allowOrigin = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];

    const cors = {
      'Access-Control-Allow-Origin': allowOrigin,
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Vary': 'Origin',
    };

    if (request.method === 'OPTIONS') return new Response(null, { headers: cors });
    if (request.method !== 'GET')
      return new Response('Method not allowed', { status: 405, headers: cors });

    // Only serve requests that originate from the site. Blocks the Worker being
    // used as a general-purpose anonymizing proxy by the rest of the internet.
    const fromSite = ALLOWED_ORIGINS.some(o => origin === o || referer.startsWith(o + '/'));
    if (!fromSite)
      return new Response('Forbidden: this proxy only serves lindseysobrinski.com',
        { status: 403, headers: cors });

    const params = new URL(request.url).searchParams;
    const target = params.get('url');
    const mode = params.get('mode') || '';
    if (!target)
      return new Response('Missing ?url= parameter', { status: 400, headers: cors });

    const v = validTarget(target);
    if (v.err) return new Response(v.err, { status: 400, headers: cors });

    // -------------------------------------------------------------------------
    // INSPECT MODE — walk the redirect chain and return JSON metadata + body.
    // -------------------------------------------------------------------------
    if (mode === 'inspect') {
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
      const chain = [];
      let current = v.u.toString();
      const started = Date.now();
      let ttfb = null;
      let resp;
      try {
        for (let hop = 0; hop <= MAX_HOPS; hop++) {
          const t0 = Date.now();
          resp = await timedFetch(current, 'manual', ctrl.signal);
          if (ttfb === null) ttfb = Date.now() - t0;   // first-response time only
          const status = resp.status;
          const isRedirect = status >= 300 && status < 400 && resp.headers.get('location');
          if (!isRedirect) break;
          const loc = resp.headers.get('location');
          let next;
          try { next = new URL(loc, current).toString(); } catch { break; }
          const nv = validTarget(next);
          chain.push({ from: current, status, location: nv.err ? null : next });
          if (nv.err) { resp = null; break; }           // refuse redirect to internal target
          current = next;
          if (hop === MAX_HOPS) { chain.push({ from: current, status: -1, location: null }); }
        }
      } catch (e) {
        clearTimeout(timer);
        const why = e && e.name === 'AbortError' ? 'timed out' : 'failed';
        return new Response(JSON.stringify({ inspect: true, error: 'fetch ' + why, requestedUrl: target }),
          { status: 200, headers: { ...cors, 'Content-Type': 'application/json' } });
      }
      clearTimeout(timer);

      let body = '';
      let finalStatus = resp ? resp.status : (chain.length ? chain[chain.length - 1].status : 0);
      let headers = {};
      if (resp) {
        const buf = await resp.arrayBuffer();
        const clipped = buf.byteLength > MAX_BYTES ? buf.slice(0, MAX_BYTES) : buf;
        body = new TextDecoder('utf-8', { fatal: false }).decode(clipped);
        headers = {
          'x-robots-tag': resp.headers.get('x-robots-tag') || '',
          'content-type': resp.headers.get('content-type') || '',
          'last-modified': resp.headers.get('last-modified') || '',
        };
      }

      const payload = {
        inspect: true,
        requestedUrl: target,
        finalUrl: current,
        redirected: chain.length > 0,
        hops: chain.length,
        chain,
        status: finalStatus,
        headers,
        responseMs: Date.now() - started,
        ttfbMs: ttfb,
        body,
      };
      return new Response(JSON.stringify(payload), {
        status: 200,
        headers: { ...cors, 'Content-Type': 'application/json', 'Cache-Control': 'no-store' },
      });
    }

    // -------------------------------------------------------------------------
    // DEFAULT MODE — raw pass-through (unchanged; geo.html depends on this).
    // -------------------------------------------------------------------------
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
    let resp;
    try {
      resp = await timedFetch(v.u.toString(), 'follow', ctrl.signal);
    } catch (e) {
      clearTimeout(timer);
      const why = e && e.name === 'AbortError' ? 'timed out' : 'failed';
      return new Response('Upstream fetch ' + why, { status: 502, headers: cors });
    }
    clearTimeout(timer);

    const buf = await resp.arrayBuffer();
    const body = buf.byteLength > MAX_BYTES ? buf.slice(0, MAX_BYTES) : buf;

    return new Response(body, {
      status: resp.status,
      headers: {
        ...cors,
        'Content-Type': resp.headers.get('Content-Type') || 'text/plain; charset=utf-8',
        'X-Proxy-Upstream-Status': String(resp.status),
      },
    });
  },
};
