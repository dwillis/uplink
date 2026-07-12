import { writeFileSync, mkdirSync } from 'fs';
import { join } from 'path';
import { BASE_PATH } from './templates/layout.mjs';

const SITE_ORIGIN = 'https://dwillis.github.io';

function exportRecord(a) {
  return {
    id: a.id,
    slug: a.slug,
    url: `${SITE_ORIGIN}${BASE_PATH}/article/${a.slug}.html`,
    year: a.year,
    month: a.month,
    monthNum: a.monthNum,
    headline: a.headline,
    kicker: a.kicker,
    author_name: a.author_name,
    author_title: a.author_title,
    affiliation: a.affiliation,
    summary: a.summary,
    keywords: a.keywords,
    topics: a.topics,
    technologies: a.technologies,
    full_text: a.full_text,
    provenance: a.provenance,
  };
}

export function writeExports(articles, buildDir) {
  const corpus = {
    name: 'Uplink newsletter archive',
    description:
      'All articles from Uplink, the newsletter of the National Institute ' +
      'for Computer-Assisted Reporting (NICAR), October 1990 - March 2007.',
    publisher: 'National Institute for Computer-Assisted Reporting (NICAR)',
    source: 'https://github.com/dwillis/uplink',
    documentation: `${SITE_ORIGIN}${BASE_PATH}/data.html`,
    generated_at: new Date().toISOString(),
    count: articles.length,
    articles: articles.map(exportRecord),
  };
  writeFileSync(
    join(buildDir, 'data', 'uplink-articles.json'),
    JSON.stringify(corpus),
    'utf8'
  );
  console.log(`Written: data/uplink-articles.json (${articles.length} articles)`);

  const articleDir = join(buildDir, 'article');
  mkdirSync(articleDir, { recursive: true });
  for (const a of articles) {
    const record = {
      ...exportRecord(a),
      similar: (a.similar || []).map(s => ({ slug: s.slug, score: s.score })),
      html_url: `${SITE_ORIGIN}${BASE_PATH}/article/${a.slug}.html`,
      json_url: `${SITE_ORIGIN}${BASE_PATH}/article/${a.slug}.json`,
    };
    writeFileSync(
      join(articleDir, `${a.slug}.json`),
      JSON.stringify(record, null, 2),
      'utf8'
    );
  }
  console.log(`Written: ${articles.length} per-article JSON files`);
}
