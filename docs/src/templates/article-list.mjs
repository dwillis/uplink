import { layout, escapeHtml, topicBadges } from './layout.mjs';

function articleCard(article, depth = '') {
  const summaryPreview = article.summary
    ? (article.summary.length > 180 ? article.summary.slice(0, 180) + '…' : article.summary)
    : '';

  return `<article class="article-card" data-year="${article.year}" data-topics="${(article.topics || []).join(',')}">
  <h2 class="article-card__title">
    <a href="${depth}article/${article.slug}.html">${escapeHtml(article.headline)}</a>
  </h2>
  <div class="article-card__meta">
    <span class="author">${escapeHtml(article.author_name)}</span>
    <span class="date">${escapeHtml(article.month)} ${article.year}</span>
  </div>
  ${topicBadges(article.topics, depth)}
  <p class="article-card__summary">${escapeHtml(summaryPreview)}</p>
</article>`;
}

export function renderArticleList(articles) {
  const years = [...new Set(articles.map(a => a.year))].sort((a, b) => b - a);
  const yearOptions = years.map(y => `<option value="${y}">${y}</option>`).join('\n');

  const cards = [...articles].reverse().map(a => articleCard(a)).join('\n');

  const content = `
<div class="page-header">
  <h1>All Articles <span class="count">(${articles.length})</span></h1>
  <div class="filters">
    <label for="year-filter">Filter by year:</label>
    <select id="year-filter">
      <option value="">All years</option>
      ${yearOptions}
    </select>
    <label for="sort-order">Sort:</label>
    <select id="sort-order">
      <option value="newest">Newest first</option>
      <option value="oldest">Oldest first</option>
    </select>
  </div>
</div>
<div class="article-list" id="article-list">
${cards}
</div>
<script src="/js/app.js"></script>`;

  return layout({ title: 'Browse Articles', content });
}
