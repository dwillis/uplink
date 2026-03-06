import { layout } from './layout.mjs';

export function renderSearchPage() {
  const content = `
<div class="page-header">
  <h1>Search Articles</h1>
</div>
<div class="search-box">
  <input
    type="search"
    id="search-input"
    placeholder="Search headlines, authors, topics…"
    autofocus
    autocomplete="off"
  >
  <span class="search-hint">Search across ${''} headlines, authors, summaries, and keywords</span>
</div>
<div id="search-results" class="search-results" aria-live="polite">
  <p class="search-placeholder">Enter a search term to find articles.</p>
</div>
<script src="/js/search.js"></script>`;

  return layout({ title: 'Search', content });
}
