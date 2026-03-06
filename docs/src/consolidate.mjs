import { readFileSync, readdirSync } from 'fs';
import { join, basename } from 'path';
import slugify from 'slugify';

const MONTH_ORDER = {
  january: 1, february: 2, march: 3, april: 4, may: 5, june: 6,
  july: 7, august: 8, september: 9, october: 10, november: 11, december: 12
};

function makeSlug(year, month, headline) {
  const base = `${year}-${month}-${headline}`;
  return slugify(base, { lower: true, strict: true });
}

const ARTICLE_ARRAY_KEYS = ['articles', 'stories', 'news_stories', 'newsletter'];

function normalizeArticles(data) {
  if (Array.isArray(data)) return data;
  for (const key of ARTICLE_ARRAY_KEYS) {
    if (data[key] && Array.isArray(data[key])) return data[key];
  }
  return [data];
}

function matchKey(year, month, headline) {
  return `${year}|${String(month).toLowerCase()}|${headline.toLowerCase().trim()}`;
}

export function consolidate(repoRoot) {
  const dataDir = join(repoRoot, 'data');
  const origDir = join(repoRoot, 'articles', 'original');

  // Step 1: load all full-text articles (authoritative list)
  const fullTextArticles = [];
  for (const file of readdirSync(origDir).sort()) {
    if (!file.endsWith('.json')) continue;
    const filePath = join(origDir, file);
    const raw = readFileSync(filePath, 'utf8').trim();
    if (!raw) continue; // skip empty files
    const data = JSON.parse(raw);
    const articles = normalizeArticles(data);
    for (const a of articles) {
      if (!a.headline || !a.full_text) continue;
      fullTextArticles.push({
        year: parseInt(a.year, 10),
        month: a.month,
        headline: a.headline,
        author_name: a.author_name || '',
        author_title: a.author_title || '',
        full_text: a.full_text,
        summary: null,
        keywords: null,
      });
    }
  }

  // Step 2: load all summaries and index by matchKey
  const summaryMap = new Map();
  for (const file of readdirSync(dataDir).sort()) {
    if (!file.endsWith('.json')) continue;
    const filePath = join(dataDir, file);
    const raw = readFileSync(filePath, 'utf8').trim();
    if (!raw) continue;
    const data = JSON.parse(raw);
    const articles = normalizeArticles(data);
    for (const a of articles) {
      if (!a.headline) continue;
      const key = matchKey(a.year, a.month, a.headline);
      summaryMap.set(key, {
        summary: a.summary || null,
        keywords: a.keywords || null,
      });
    }
  }

  // Step 3: match and merge
  let matched = 0;
  let unmatched = 0;
  const consolidated = [];

  for (const article of fullTextArticles) {
    const key = matchKey(article.year, article.month, article.headline);
    const summary = summaryMap.get(key);

    let finalSummary = article.summary;
    let finalKeywords = article.keywords;

    if (summary) {
      finalSummary = summary.summary;
      finalKeywords = summary.keywords;
      matched++;
    } else {
      // fallback: first 200 chars of full_text
      const text = article.full_text.replace(/\s+/g, ' ').trim();
      finalSummary = text.length > 200 ? text.slice(0, 200) + '...' : text;
      finalKeywords = []; // will be filled by topics.mjs via TF-IDF
      unmatched++;
    }

    const slug = makeSlug(article.year, article.month, article.headline);
    const monthNum = MONTH_ORDER[article.month.toLowerCase()] || 0;

    consolidated.push({
      slug,
      year: article.year,
      month: article.month,
      monthNum,
      headline: article.headline,
      author_name: article.author_name,
      author_title: article.author_title,
      summary: finalSummary,
      keywords: finalKeywords || [],
      full_text: article.full_text,
      topics: [],
      similar: [],
    });
  }

  // Sort chronologically
  consolidated.sort((a, b) => {
    if (a.year !== b.year) return a.year - b.year;
    return a.monthNum - b.monthNum;
  });

  console.log(`Consolidated: ${consolidated.length} articles (${matched} matched, ${unmatched} unmatched)`);
  return consolidated;
}
