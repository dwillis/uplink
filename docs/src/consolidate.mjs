import { readFileSync, readdirSync } from 'fs';
import { join } from 'path';
import slugify from 'slugify';

const MONTH_ORDER = {
  january: 1, february: 2, march: 3, april: 4, may: 5, june: 6,
  july: 7, august: 8, september: 9, october: 10, november: 11, december: 12
};

const MONTH_NAMES = [
  'january','february','march','april','may','june',
  'july','august','september','october','november','december'
];

export function makeSlug(year, month, headline) {
  const base = `${year}-${month}-${headline}`;
  return slugify(base, { lower: true, strict: true });
}

function normalizeMonth(month) {
  const s = String(month).toLowerCase().trim();
  const num = parseInt(s, 10);
  if (!isNaN(num) && num >= 1 && num <= 12) return MONTH_NAMES[num - 1];
  const match = s.match(/^([a-z]+)/);
  return match ? match[1] : s;
}

export function consolidate(repoRoot) {
  const issuesDir = join(repoRoot, 'issues');

  const consolidated = [];
  const slugCounts = new Map();

  for (const file of readdirSync(issuesDir).sort()) {
    if (!file.endsWith('.json')) continue;
    const filePath = join(issuesDir, file);
    const raw = readFileSync(filePath, 'utf8').trim();
    if (!raw) continue;
    const issue = JSON.parse(raw);
    const articles = issue.articles || [];

    for (const a of articles) {
      if (!a.headline || !a.full_text) continue;

      const year = issue.year || 0;
      const month = issue.month || '';
      const monthNum = MONTH_ORDER[normalizeMonth(month)] || 0;

      // Generic recurring headlines ("Tipsheets", "Web Links", "Bits &
      // Bytes") can collide within the same issue/month now that far more
      // short items are captured -- disambiguate so pages don't silently
      // overwrite each other.
      let slug = a.id || makeSlug(year, month, a.headline);
      const seen = slugCounts.get(slug) || 0;
      slugCounts.set(slug, seen + 1);
      if (seen > 0) slug = `${slug}-${seen + 1}`;

      consolidated.push({
        id: a.id || slug,
        slug,
        year,
        month,
        monthNum,
        headline: a.headline,
        kicker: a.kicker || '',
        author_name: a.author_name || '',
        author_title: a.author_title || '',
        affiliation: a.affiliation || '',
        summary: a.summary || '',
        keywords: a.keywords || [],
        full_text: a.full_text,
        topics: a.topics || [],
        technologies: a.technologies || [],
        provenance: a.provenance || null,
        similar: [],
      });
    }
  }

  // Sort chronologically
  consolidated.sort((a, b) => {
    if (a.year !== b.year) return a.year - b.year;
    return a.monthNum - b.monthNum;
  });

  console.log(`Consolidated: ${consolidated.length} articles from ${readdirSync(issuesDir).filter(f => f.endsWith('.json')).length} issue files`);
  return consolidated;
}
