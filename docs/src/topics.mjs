import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import natural from 'natural';

const { TfIdf } = natural;

const __dirname = dirname(fileURLToPath(import.meta.url));

// Curated topic taxonomy: topic name -> keywords to match (lowercase).
// Single source of truth is data/taxonomy.json (also read by
// src/extract_metadata.py) so the Python and Node sides can't drift.
const TAXONOMY = JSON.parse(
  readFileSync(join(__dirname, '..', '..', 'data', 'taxonomy.json'), 'utf8')
);
const TAXONOMY_TOPICS = new Set([...Object.keys(TAXONOMY), 'Other']);

function extractTfIdfKeywords(fullText, topN = 3) {
  const tfidf = new TfIdf();
  tfidf.addDocument(fullText);
  const terms = [];
  tfidf.listTerms(0).slice(0, topN * 3).forEach(item => {
    if (item.term.length > 3 && !/^\d+$/.test(item.term)) {
      terms.push(item.term);
    }
  });
  return terms.slice(0, topN);
}

function assignTopics(article) {
  // Prefer topics already assigned by the LLM metadata pass
  // (src/extract_metadata.py) over keyword/TF-IDF guessing.
  if (Array.isArray(article.topics) && article.topics.length > 0) {
    const valid = article.topics.filter(t => TAXONOMY_TOPICS.has(t));
    if (valid.length > 0) return valid.slice(0, 3);
  }

  const keywords = (article.keywords || []).map(k => k.toLowerCase());
  const assignedTopics = new Set();

  for (const [topic, topicKeywords] of Object.entries(TAXONOMY)) {
    for (const kw of keywords) {
      if (topicKeywords.some(tk => kw.includes(tk) || tk.includes(kw))) {
        assignedTopics.add(topic);
        break;
      }
    }
  }

  // If no topics assigned and article has full_text, extract keywords via TF-IDF
  if (assignedTopics.size === 0 && article.full_text) {
    const extracted = extractTfIdfKeywords(article.full_text, 5);
    for (const kw of extracted) {
      for (const [topic, topicKeywords] of Object.entries(TAXONOMY)) {
        if (topicKeywords.some(tk => kw.includes(tk) || tk.includes(kw))) {
          assignedTopics.add(topic);
        }
      }
    }
    // If article had no keywords, add the extracted ones
    if (!article.keywords || article.keywords.length === 0) {
      article.keywords = extracted;
    }
  }

  if (assignedTopics.size === 0) {
    assignedTopics.add('Other');
  }

  return Array.from(assignedTopics).slice(0, 3);
}

export function assignAllTopics(articles) {
  for (const article of articles) {
    article.topics = assignTopics(article);
  }

  // Build topic index
  const topicIndex = {};
  for (const article of articles) {
    for (const topic of article.topics) {
      if (!topicIndex[topic]) topicIndex[topic] = [];
      topicIndex[topic].push(article.slug);
    }
  }

  const topicNames = Object.keys(TAXONOMY).concat(['Other'])
    .filter(t => topicIndex[t] && topicIndex[t].length > 0);

  console.log('Topic distribution:');
  for (const t of topicNames) {
    console.log(`  ${t}: ${(topicIndex[t] || []).length} articles`);
  }

  return { articles, topicIndex, topicNames };
}
