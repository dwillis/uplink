import { layout, escapeHtml, topicBadges } from './layout.mjs';

function articleCard(article) {
  const summaryPreview = article.summary
    ? (article.summary.length > 180 ? article.summary.slice(0, 180) + '…' : article.summary)
    : '';

  return `<article class="article-card">
  <h2 class="article-card__title">
    <a href="/article/${article.slug}.html">${escapeHtml(article.headline)}</a>
  </h2>
  <div class="article-card__meta">
    ${article.author_name ? `<span class="author">${escapeHtml(article.author_name)}</span>` : ''}
    <span class="date">${escapeHtml(article.month)} ${article.year}</span>
  </div>
  ${topicBadges(article.topics, '/')}
  <p class="article-card__summary">${escapeHtml(summaryPreview)}</p>
</article>`;
}

export function renderTopicDetail(topic, topicArticles) {
  const cards = [...topicArticles].reverse().map(a => articleCard(a)).join('\n');

  const content = `
<div class="page-header">
  <h1>${escapeHtml(topic)} <span class="count">(${topicArticles.length})</span></h1>
  <a href="/topics/" class="back-link">← All topics</a>
</div>
<div class="article-list">
${cards}
</div>`;

  return layout({ title: topic, content });
}
