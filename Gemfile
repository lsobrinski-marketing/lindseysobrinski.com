source "https://rubygems.org"

# Matches what GitHub Pages runs in production, so local preview and the live
# build stay in sync. Do not add plugins GitHub Pages does not whitelist.
gem "github-pages", group: :jekyll_plugins

gem "webrick", "~> 1.8"   # Ruby 3+ no longer bundles this; jekyll serve needs it

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end
