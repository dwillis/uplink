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

const ARTICLE_ARRAY_KEYS = ['articles', 'stories', 'news_stories', 'newsletter', 'content', 'data'];

function normalizeArticles(data) {
  if (Array.isArray(data)) return data;
  for (const key of ARTICLE_ARRAY_KEYS) {
    if (data[key] && Array.isArray(data[key])) return data[key];
  }
  return [data];
}

const MONTH_NAMES = [
  'january','february','march','april','may','june',
  'july','august','september','october','november','december'
];

function normalizeMonth(month) {
  const s = String(month).toLowerCase().trim();
  // Handle numeric months: "3" → "march"
  const num = parseInt(s, 10);
  if (!isNaN(num) && num >= 1 && num <= 12) return MONTH_NAMES[num - 1];
  // Extract just the first month name from compound formats like
  // "March-April", "July/August", "November/December", "January-February"
  const match = s.match(/^([a-z]+)/);
  return match ? match[1] : s;
}

function matchKey(year, month, headline) {
  return `${year}|${normalizeMonth(month)}|${headline.toLowerCase().trim()}`;
}

/**
 * Extract a readable summary from raw OCR full text.
 * Finds complete sentences that form a coherent opening, targeting ~200 chars.
 */
function extractSummary(fullText) {
  // Normalize whitespace, strip leading junk (page numbers, headers, etc.)
  let text = fullText.replace(/\s+/g, ' ').trim();

  // Skip past short leading fragments that look like headers/bylines (< 40 chars before first period)
  const firstPeriod = text.indexOf('.');
  if (firstPeriod > 0 && firstPeriod < 40) {
    // Check if there's a sentence after this short fragment
    const rest = text.slice(firstPeriod + 1).trim();
    if (rest.length > 100) {
      text = rest;
    }
  }

  // Split into sentences (period/exclamation/question followed by space+uppercase or end)
  const sentences = text.match(/[^.!?]*[.!?]+/g);
  if (!sentences || sentences.length === 0) {
    // No sentence boundaries found — fall back to word-boundary truncation
    if (text.length <= 250) return text;
    const cut = text.lastIndexOf(' ', 250);
    return text.slice(0, cut > 100 ? cut : 250) + '...';
  }

  // Accumulate complete sentences up to ~250 chars
  let summary = '';
  for (const sentence of sentences) {
    const trimmed = sentence.trim();
    if (!trimmed) continue;
    if (summary.length + trimmed.length > 300 && summary.length > 80) break;
    summary += (summary ? ' ' : '') + trimmed;
    if (summary.length >= 150) break;
  }

  if (!summary) {
    summary = sentences[0].trim();
  }

  return summary;
}

export function consolidate(repoRoot) {
  const dataDir = join(repoRoot, 'data');
  const origDir = join(repoRoot, 'articles', 'original');

  // Step 1: load all full-text articles grouped by file
  const fullTextByFile = new Map(); // filename -> [{article}, ...]
  const allFullText = [];
  for (const file of readdirSync(origDir).sort()) {
    if (!file.endsWith('.json')) continue;
    const filePath = join(origDir, file);
    const raw = readFileSync(filePath, 'utf8').trim();
    if (!raw) continue;
    const data = JSON.parse(raw);
    const articles = normalizeArticles(data);
    const fileArticles = [];
    for (const a of articles) {
      if (!a.headline || !a.full_text) continue;
      const article = {
        year: parseInt(a.year, 10),
        month: a.month,
        headline: a.headline,
        author_name: a.author_name && a.author_name !== 'null' ? a.author_name : '',
        author_title: a.author_title && a.author_title !== 'null' ? a.author_title : '',
        full_text: a.full_text,
        sourceFile: file,
      };
      fileArticles.push(article);
      allFullText.push(article);
    }
    if (fileArticles.length > 0) {
      fullTextByFile.set(file, fileArticles);
    }
  }

  // Step 2: load all summaries — both as a matchKey map and grouped by file
  const summaryMap = new Map();
  const summaryByFile = new Map(); // filename -> [{summary}, ...]
  for (const file of readdirSync(dataDir).sort()) {
    if (!file.endsWith('.json')) continue;
    const filePath = join(dataDir, file);
    const raw = readFileSync(filePath, 'utf8').trim();
    if (!raw) continue;
    const data = JSON.parse(raw);
    const articles = normalizeArticles(data);
    const fileSummaries = [];
    for (const a of articles) {
      if (!a.headline) continue;
      const key = matchKey(a.year, a.month, a.headline);
      const summaryObj = {
        headline: a.headline,
        summary: a.summary || null,
        keywords: a.keywords || null,
        matched: false,
      };
      summaryMap.set(key, summaryObj);
      fileSummaries.push(summaryObj);
    }
    if (fileSummaries.length > 0) {
      summaryByFile.set(file, fileSummaries);
    }
  }

  // Step 3: two-pass matching
  let matchedExact = 0;
  let matchedPositional = 0;
  let unmatched = 0;

  // Map from article to its resolved summary
  const articleSummaries = new Map();

  // Pass 1: exact headline match
  for (const article of allFullText) {
    const key = matchKey(article.year, article.month, article.headline);
    const summary = summaryMap.get(key);
    if (summary && !summary.matched) {
      articleSummaries.set(article, summary);
      summary.matched = true;
      matchedExact++;
    }
  }

  // Pass 2: positional match within same file for unmatched articles
  for (const [file, fileArticles] of fullTextByFile) {
    const fileSummaries = summaryByFile.get(file);
    if (!fileSummaries) continue;

    // Get unmatched articles and summaries for this file
    const unmatchedArticles = fileArticles.filter(a => !articleSummaries.has(a));
    const unmatchedSummaries = fileSummaries.filter(s => !s.matched);

    if (unmatchedArticles.length === 0 || unmatchedSummaries.length === 0) continue;

    // Match by position: article N pairs with summary N
    const limit = Math.min(unmatchedArticles.length, unmatchedSummaries.length);
    for (let i = 0; i < limit; i++) {
      articleSummaries.set(unmatchedArticles[i], unmatchedSummaries[i]);
      unmatchedSummaries[i].matched = true;
      matchedPositional++;
    }
  }

  // Step 4: build consolidated array
  const consolidated = [];

  for (const article of allFullText) {
    const summary = articleSummaries.get(article);

    let finalSummary;
    let finalKeywords;

    if (summary) {
      finalSummary = summary.summary;
      finalKeywords = summary.keywords;
    } else {
      finalSummary = extractSummary(article.full_text);
      finalKeywords = [];
      unmatched++;
    }

    const slug = makeSlug(article.year, article.month, article.headline);
    const monthNum = MONTH_ORDER[normalizeMonth(article.month)] || 0;

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

  const totalMatched = matchedExact + matchedPositional;
  console.log(`Consolidated: ${consolidated.length} articles (${totalMatched} matched: ${matchedExact} exact + ${matchedPositional} positional, ${unmatched} unmatched)`);
  return consolidated;
}
