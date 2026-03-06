import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';
import slugify from 'slugify';
import { renderArticleList } from './templates/article-list.mjs';
import { renderArticleDetail } from './templates/article-detail.mjs';
import { renderTopicList } from './templates/topic-list.mjs';
import { renderTopicDetail } from './templates/topic-detail.mjs';
import { renderSearchPage } from './templates/search-page.mjs';

function write(filePath, content) {
  mkdirSync(filePath.replace(/\/[^/]+$/, ''), { recursive: true });
  writeFileSync(filePath, content, 'utf8');
}

export function render(articles, topicIndex, topicNames, buildDir, basePath = '/') {
  // index.html
  write(join(buildDir, 'index.html'), renderArticleList(articles, basePath));
  console.log('Written: index.html');

  // article/{slug}.html
  const articleDir = join(buildDir, 'article');
  mkdirSync(articleDir, { recursive: true });
  for (const article of articles) {
    write(join(articleDir, `${article.slug}.html`), renderArticleDetail(article, articles, basePath));
  }
  console.log(`Written: ${articles.length} article pages`);

  // topics/index.html
  const topicsDir = join(buildDir, 'topics');
  mkdirSync(topicsDir, { recursive: true });
  write(join(topicsDir, 'index.html'), renderTopicList(topicIndex, topicNames, basePath));
  console.log('Written: topics/index.html');

  // topics/{slug}.html
  for (const topic of topicNames) {
    if (!topicIndex[topic] || topicIndex[topic].length === 0) continue;
    const topicSlug = topic.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    const topicArticles = topicIndex[topic]
      .map(slug => articles.find(a => a.slug === slug))
      .filter(Boolean);
    write(join(topicsDir, `${topicSlug}.html`), renderTopicDetail(topic, topicArticles, basePath));
  }
  console.log(`Written: ${topicNames.length} topic pages`);

  // search.html
  write(join(buildDir, 'search.html'), renderSearchPage(basePath));
  console.log('Written: search.html');
}
