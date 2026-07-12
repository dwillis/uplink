import { layout, BASE_PATH } from './layout.mjs';

const SITE_ORIGIN = 'https://dwillis.github.io';

const FIELDS = [
  ['id', 'string', 'Permanent identifier, minted once into the corpus. Never changes, even if the headline is later corrected.'],
  ['slug', 'string', 'URL slug derived from year, month, and headline. Currently identical to id, but regenerated at build time — use id for longitudinal work.'],
  ['url', 'string', 'Canonical URL of the article page on this site.'],
  ['year / month / monthNum', 'number / string / number', 'Issue date. monthNum is 1–12 for sorting; some issues cover two months (e.g. "July/August"), in which case monthNum reflects the first.'],
  ['headline', 'string', 'Article title as printed.'],
  ['kicker', 'string', 'Section label or eyebrow above the headline (e.g. "ENERGY"). Often empty.'],
  ['author_name', 'string', 'Byline name. Empty for unsigned items (about a third of the corpus — many short listings ran without bylines).'],
  ['author_title', 'string', 'The author’s job title only.'],
  ['affiliation', 'string', 'The author’s publication or organization.'],
  ['summary', 'string', 'One-paragraph abstract, generated during archival processing.'],
  ['keywords', 'string[]', 'Free-text tags assigned during archival processing.'],
  ['topics', 'string[]', 'One to three entries from a controlled 12-topic taxonomy (see data/taxonomy.json in the repository).'],
  ['technologies', 'string[]', 'Software, hardware, formats, and services mentioned in the article, normalized against a controlled vocabulary (data/technologies.json) and alias map (data/technology_aliases.json). Useful for tracing tool adoption over time.'],
  ['full_text', 'string', 'Complete article text, OCR-extracted from the original scanned PDFs. Occasional OCR artifacts remain.'],
  ['provenance', 'object', 'How the record was produced: extracted_by (extraction model or "pre-v2" for legacy records), extracted_at, and verified (whether the extraction passed anchor checks against the source text).'],
  ['similar', '{slug, score}[]', 'Per-article JSON only: top five related articles by TF-IDF cosine similarity, computed at build time.'],
];

export function renderDataPage(count) {
  const corpusUrl = `${SITE_ORIGIN}${BASE_PATH}/data/uplink-articles.json`;
  const exampleArticleUrl = `${SITE_ORIGIN}${BASE_PATH}/article/1990-october-ghostbusting-in-east-st-louis.json`;

  const rows = FIELDS.map(([name, type, desc]) => `    <tr>
      <td><code>${name}</code></td>
      <td><code>${type}</code></td>
      <td>${desc}</td>
    </tr>`).join('\n');

  const content = `
<div class="data-page">
  <h1>Data</h1>
  <p>The full Uplink archive — ${count.toLocaleString('en-US')} articles from 145 issues,
  October 1990 through March 2007 — is available as JSON. It documents how
  computer-assisted reporting was actually practiced as it evolved: the tools,
  the data sources, and the stories, issue by issue for sixteen years.</p>

  <h2>Downloads</h2>
  <ul>
    <li><a href="${corpusUrl}"><code>data/uplink-articles.json</code></a> —
      the complete corpus in one file, including full text (~8&nbsp;MB).
      Wrapped as <code>{name, description, publisher, source, generated_at, count, articles: [...]}</code>.</li>
    <li><code>article/&lt;slug&gt;.json</code> — one JSON file per article,
      alongside its HTML page, with related-article links added
      (<a href="${exampleArticleUrl}">example</a>). Every article page links to
      its JSON version.</li>
  </ul>

  <h2>Field dictionary</h2>
  <div class="table-wrap">
  <table class="field-table">
    <thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead>
    <tbody>
${rows}
    </tbody>
  </table>
  </div>

  <h2>Example</h2>
  <p>Count technology mentions by year with <code>curl</code> and <code>jq</code>:</p>
  <pre><code>curl -s ${corpusUrl} \\
  | jq -r '.articles[] | .year as \$y | .technologies[] | "\\(\$y) \\(.)"' \\
  | sort | uniq -c | sort -rn | head</code></pre>

  <h2>Notes for researchers</h2>
  <ul>
    <li>Use <code>id</code> as the stable key when tracking articles across
      corpus revisions.</li>
    <li><code>topics</code> and <code>technologies</code> are controlled
      vocabularies; <code>keywords</code> are free text.</li>
    <li>The underlying per-issue source files, extraction pipeline, and
      data-quality report live in the
      <a href="https://github.com/dwillis/uplink">GitHub repository</a>.
      Original publication: NICAR (National Institute for Computer-Assisted
      Reporting).</li>
  </ul>
</div>`;

  return layout({
    title: 'Data',
    content,
    bodyClass: 'data-page-body',
  });
}
