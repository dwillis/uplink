// Mint a permanent `id` for every article in issues/*.json.
//
// The id is the slug the site already publishes (see consolidate.mjs), frozen
// into the corpus so it survives future headline corrections or re-extraction.
// Run once (idempotent -- existing ids are never touched):
//
//   node docs/src/mint-ids.mjs
import { readFileSync, readdirSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { makeSlug } from './consolidate.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const repoRoot = join(__dirname, '..', '..');
const issuesDir = join(repoRoot, 'issues');

// Byte-match python's json.dumps(data, indent=2) + "\n" (ensure_ascii=True),
// which wrote these files, so the git diff shows only the added "id" lines.
function serialize(data) {
  const json = JSON.stringify(data, null, 2).replace(
    /[\u0080-\uffff]/g,
    (c) => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0')
  );
  return json + '\n';
}

const slugCounts = new Map();
const usedIds = new Set();
let minted = 0;
let kept = 0;

for (const file of readdirSync(issuesDir).sort()) {
  if (!file.endsWith('.json')) continue;
  const filePath = join(issuesDir, file);
  const raw = readFileSync(filePath, 'utf8');
  if (!raw.trim()) continue;
  const issue = JSON.parse(raw);

  // Refuse to touch a file our serializer can't reproduce byte-for-byte --
  // adding ids must be the only change a rewrite introduces.
  if (serialize(issue) !== raw) {
    throw new Error(`${file}: round-trip serialization mismatch, aborting`);
  }

  let changed = false;
  issue.articles = (issue.articles || []).map((a) => {
    // consolidate.mjs skips these, so they never get a slug/page either.
    if (!a.headline || !a.full_text) return a;

    // Mirror consolidate.mjs collision handling exactly: count on the base
    // key (existing id or derived slug), suffix -2/-3 for repeats, so minted
    // ids equal the slugs (URLs) the site already publishes.
    const base = a.id || makeSlug(issue.year || 0, issue.month || '', a.headline);
    const seen = slugCounts.get(base) || 0;
    slugCounts.set(base, seen + 1);

    if (a.id) {
      if (usedIds.has(a.id)) {
        console.warn(`WARNING ${file}: duplicate existing id "${a.id}" left as-is`);
      }
      usedIds.add(a.id);
      kept += 1;
      return a;
    }

    let slug = seen > 0 ? `${base}-${seen + 1}` : base;
    let bump = seen + 1;
    while (usedIds.has(slug)) {
      // A suffixed slug can collide with a natural one (headline ending in a
      // number); not in today's corpus, but minting must stay safe.
      bump += 1;
      const next = `${base}-${bump}`;
      console.warn(`WARNING ${file}: id "${slug}" already used, bumping to "${next}"`);
      slug = next;
    }
    usedIds.add(slug);
    minted += 1;
    changed = true;
    return { id: slug, ...a };
  });

  if (changed) writeFileSync(filePath, serialize(issue), 'utf8');
}

console.log(`Minted ${minted} id(s), kept ${kept} existing, ${usedIds.size} total unique.`);
