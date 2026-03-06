import { layout, escapeHtml, topicBadges } from './layout.mjs';

function similarArticleItem(sim, articleMap) {
  const a = articleMap.get(sim.slug);
  if (!a) return '';
  return `<li class="similar-item">
  <a href="/article/${escapeHtml(a.slug)}.html">${escapeHtml(a.headline)}</a>
  <span class="similar-meta">${escapeHtml(a.month)} ${a.year}</span>
</li>`;
}

function formatFullText(text) {
  if (!text) return '<p><em>Full text not available.</em></p>';
  // Split into paragraphs on double newlines or single newlines
  const paragraphs = text
    .split(/\n\n+/)
    .map(p => p.replace(/\n/g, ' ').trim())
    .filter(p => p.length > 0);

  if (paragraphs.length <= 1) {
    // Single block — try to split on sentence boundaries for readability
    const sentences = text.replace(/([.!?])\s+/g, '$1\n').split('\n');
    const chunks = [];
    let chunk = [];
    for (const s of sentences) {
      chunk.push(s);
      if (chunk.join(' ').length > 400) {
        chunks.push(chunk.join(' '));
        chunk = [];
      }
    }
    if (chunk.length) chunks.push(chunk.join(' '));
    return chunks.map(c => `<p>${escapeHtml(c.trim())}</p>`).join('\n');
  }

  return paragraphs.map(p => `<p>${escapeHtml(p)}</p>`).join('\n');
}

export function renderArticleDetail(article, allArticles) {
  const articleMap = new Map(allArticles.map(a => [a.slug, a]));
  const idx = allArticles.findIndex(a => a.slug === article.slug);
  const prev = idx > 0 ? allArticles[idx - 1] : null;
  const next = idx < allArticles.length - 1 ? allArticles[idx + 1] : null;

  const similarHtml = (article.similar || []).length > 0
    ? `<aside class="similar-articles">
  <h3>Similar Articles</h3>
  <ul class="similar-list">
    ${article.similar.map(s => similarArticleItem(s, articleMap)).join('\n')}
  </ul>
</aside>`
    : '';

  const prevNext = `<nav class="article-nav">
  ${prev ? `<a href="/article/${prev.slug}.html" class="article-nav__prev">← ${escapeHtml(prev.headline)}</a>` : '<span></span>'}
  ${next ? `<a href="/article/${next.slug}.html" class="article-nav__next">${escapeHtml(next.headline)} →</a>` : ''}
</nav>`;

  const content = `
<article class="article-detail">
  <header class="article-header">
    <h1>${escapeHtml(article.headline)}</h1>
    <div class="article-byline">
      ${article.author_name ? `<span class="author">${escapeHtml(article.author_name)}</span>` : ''}
      ${article.author_title ? `<span class="author-title">${escapeHtml(article.author_title)}</span>` : ''}
      <span class="date">${escapeHtml(article.month)} ${article.year}</span>
    </div>
    <div class="article-topics">${topicBadges(article.topics, '/')}</div>
  </header>

  ${article.summary ? `<div class="article-summary"><p>${escapeHtml(article.summary)}</p></div>` : ''}

  <div class="article-body">
    ${formatFullText(article.full_text)}
  </div>
</article>

${similarHtml}
${prevNext}`;

  return layout({
    title: article.headline,
    content,
    bodyClass: 'article-page',
  });
}
