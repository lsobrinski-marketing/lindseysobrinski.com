// GEO Analyzer fetch proxy — Cloudflare Worker
// ---------------------------------------------------------------------------
// A browser cannot fetch arbitrary cross-origin pages, so the GEO analyzer
// (geo.html) needs a server to fetch a target URL and hand it back with CORS
// headers. This replaces the free public proxies, which are unreliable and
// were all down at once on 2026-07-23, taking the tool with them.
//
// Deploy: see README.md in this folder. Free tier covers ~100k requests/day.
//
// Protections against this becoming an open proxy someone else abuses:
//   - Only serves requests coming from the site itself (Origin / Referer check)
//   - GET only, http/https targets only
//   - Blocks localhost / private-range / cloud-metadata targets (SSRF hygiene)
//   - Caps response size and fetch time
// ---------------------------------------------------------------------------

const ALLOWED_ORIGINS = [
  'https://lindseysobrinski.com',
  'https://www.lindseysobrinski.com',
];
const MAX_BYTES = 3_000_000;      // 3 MB ceiling on a fetched page
const FETCH_TIMEOUT_MS = 20_000;  // give slow sites 20s

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

    const target = new URL(request.url).searchParams.get('url');
    if (!target)
      return new Response('Missing ?url= parameter', { status: 400, headers: cors });

    let u;
    try { u = new URL(target); } catch {
      return new Response('Invalid target URL', { status: 400, headers: cors });
    }
    if (u.protocol !== 'http:' && u.protocol !== 'https:')
      return new Response('Only http/https targets allowed', { status: 400, headers: cors });

    // SSRF hygiene: refuse internal / metadata hosts.
    const host = u.hostname.toLowerCase();
    const blocked =
      host === 'localhost' || host.endsWith('.localhost') || host.endsWith('.internal') ||
      host === '169.254.169.254' || host === 'metadata.google.internal' ||
      host === '::1' || host === '[::1]' ||
      /^127\./.test(host) || /^10\./.test(host) || /^192\.168\./.test(host) ||
      /^169\.254\./.test(host) || /^172\.(1[6-9]|2\d|3[01])\./.test(host);
    if (blocked)
      return new Response('Target host not allowed', { status: 400, headers: cors });

    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), FETCH_TIMEOUT_MS);
    let resp;
    try {
      resp = await fetch(u.toString(), {
        method: 'GET',
        redirect: 'follow',
        signal: ctrl.signal,
        headers: {
          // Present as a normal browser so sites don't serve a bot-block page.
          'User-Agent': 'Mozilla/5.0 (compatible; GEO-Analyzer/1.0; +https://lindseysobrinski.com/geo.html)',
          'Accept': 'text/html,text/plain,*/*',
        },
      });
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
