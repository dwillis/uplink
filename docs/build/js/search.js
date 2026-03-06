(function () {
  'use strict';

  const basePath = window.BASE_PATH || '/';
  let searchIndex = null;
  let articles = null;
  let articleMap = null;

  const input = document.getElementById('search-input');
  const resultsEl = document.getElementById('search-results');

  if (!input || !resultsEl) return;

  // Load lunr from CDN — already included via script tag in layout
  // Load data
  Promise.all([
    fetch(basePath + 'data/search-index.json').then(r => r.json()),
    fetch(basePath + 'data/articles.json').then(r => r.json()),
  ]).then(([indexData, articlesData]) => {
    searchIndex = lunr.Index.load(indexData);
    articles = articlesData;
    articleMap = new Map(articles.map(a => [a.slug, a]));
    resultsEl.innerHTML = '<p class="search-placeholder">Enter a search term to find articles.</p>';
  }).catch(err => {
    resultsEl.innerHTML = '<p class="error">Failed to load search index.</p>';
    console.error(err);
  });

  let debounceTimer;

  input.addEventListener('input', function () {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(doSearch, 300);
  });

  function doSearch() {
    const query = input.value.trim();
    if (!query) {
      resultsEl.innerHTML = '<p class="search-placeholder">Enter a search term to find articles.</p>';
      return;
    }
    if (!searchIndex) {
      resultsEl.innerHTML = '<p class="search-placeholder">Loading search index…</p>';
      return;
    }

    let results;
    try {
      results = searchIndex.search(query + '*');
      if (results.length === 0) results = searchIndex.search(query);
    } catch (e) {
      try {
        results = searchIndex.search(query);
      } catch (e2) {
        results = [];
      }
    }

    if (results.length === 0) {
      resultsEl.innerHTML = `<p class="no-results">No articles found for "<strong>${escapeHtml(query)}</strong>".</p>`;
      return;
    }

    const html = results.map(r => {
      const article = articleMap.get(r.ref);
      if (!article) return '';
      const summary = article.summary
        ? (article.summary.length > 200 ? article.summary.slice(0, 200) + '…' : article.summary)
        : '';
      const topics = (article.topics || []).map(t => {
        const slug = t.toLowerCase().replace(/[^a-z0-9]+/g, '-');
        return `<a href="${basePath}topics/${slug}.html" class="badge">${escapeHtml(t)}</a>`;
      }).join('');

      return `<article class="article-card">
  <h2 class="article-card__title">
    <a href="${basePath}article/${escapeHtml(article.slug)}.html">${escapeHtml(article.headline)}</a>
  </h2>
  <div class="article-card__meta">
    ${article.author_name ? '<span class="author">' + escapeHtml(article.author_name) + '</span>' : ''}
    <span class="date">${escapeHtml(article.month)} ${article.year}</span>
  </div>
  ${topics}
  <p class="article-card__summary">${escapeHtml(summary)}</p>
</article>`;
    }).join('\n');

    resultsEl.innerHTML = `<p class="result-count">${results.length} result${results.length !== 1 ? 's' : ''} for "<strong>${escapeHtml(query)}</strong>"</p>${html}`;
  }

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
})();
