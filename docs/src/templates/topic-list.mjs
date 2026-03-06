import { layout, escapeHtml } from './layout.mjs';

export function renderTopicList(topicIndex, topicNames, basePath = '/') {
  const cards = topicNames
    .filter(t => topicIndex[t] && topicIndex[t].length > 0)
    .sort((a, b) => (topicIndex[b] || []).length - (topicIndex[a] || []).length)
    .map(topic => {
      const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, '-');
      const count = (topicIndex[topic] || []).length;
      return `<a href="${basePath}topics/${slug}.html" class="topic-card">
  <h2>${escapeHtml(topic)}</h2>
  <span class="topic-count">${count} article${count !== 1 ? 's' : ''}</span>
</a>`;
    }).join('\n');

  const content = `
<div class="page-header">
  <h1>Browse by Topic</h1>
</div>
<div class="topic-grid">
${cards}
</div>`;

  return layout({ title: 'Topics', content, basePath });
}
