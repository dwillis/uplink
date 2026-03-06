import { writeFileSync, mkdirSync, copyFileSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

import { consolidate } from './src/consolidate.mjs';
import { assignAllTopics } from './src/topics.mjs';
import { computeSimilarity } from './src/similarity.mjs';
import { buildSearchIndex } from './src/search-index.mjs';
import { render } from './src/render.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, '..');
const buildDir = join(__dirname, 'build');

mkdirSync(join(buildDir, 'data'), { recursive: true });
mkdirSync(join(buildDir, 'css'), { recursive: true });
mkdirSync(join(buildDir, 'js'), { recursive: true });

console.log('\n=== Step 1: Consolidating articles ===');
let articles = consolidate(repoRoot);

console.log('\n=== Step 2: Assigning topics ===');
const { articles: articlesWithTopics, topicIndex, topicNames } = assignAllTopics(articles);
articles = articlesWithTopics;

console.log('\n=== Step 3: Computing similarity ===');
articles = computeSimilarity(articles);

console.log('\n=== Step 4: Building search index ===');
const searchIdx = buildSearchIndex(articles);
writeFileSync(
  join(buildDir, 'data', 'search-index.json'),
  JSON.stringify(searchIdx),
  'utf8'
);
console.log('Written: data/search-index.json');

// Write articles.json (without full_text for search/listing)
const articlesLight = articles.map(({ full_text, ...rest }) => rest);
writeFileSync(
  join(buildDir, 'data', 'articles.json'),
  JSON.stringify(articlesLight),
  'utf8'
);
console.log(`Written: data/articles.json (${articlesLight.length} articles)`);

console.log('\n=== Step 5: Rendering HTML ===');
render(articles, topicIndex, topicNames, buildDir);

console.log('\n✓ Build complete! Output in docs/build/');
console.log(`  Total articles: ${articles.length}`);
console.log(`  Total topics: ${topicNames.length}`);
