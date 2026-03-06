import natural from 'natural';

const { TfIdf } = natural;

function cosineSimilarity(vecA, vecB) {
  // vecA and vecB are Maps of term -> tfidf score
  let dot = 0;
  let normA = 0;
  let normB = 0;

  for (const [term, scoreA] of vecA) {
    normA += scoreA * scoreA;
    const scoreB = vecB.get(term) || 0;
    dot += scoreA * scoreB;
  }
  for (const [, scoreB] of vecB) {
    normB += scoreB * scoreB;
  }

  if (normA === 0 || normB === 0) return 0;
  return dot / (Math.sqrt(normA) * Math.sqrt(normB));
}

export function computeSimilarity(articles, topN = 5) {
  const tfidf = new TfIdf();

  // Build document for each article from headline + summary + keywords
  for (const article of articles) {
    const doc = [
      article.headline,
      article.summary || '',
      (article.keywords || []).join(' '),
    ].join(' ');
    tfidf.addDocument(doc);
  }

  // Build TF-IDF vectors for each document
  const vectors = articles.map((_, docIndex) => {
    const vec = new Map();
    tfidf.listTerms(docIndex).forEach(({ term, tfidf: score }) => {
      vec.set(term, score);
    });
    return vec;
  });

  console.log(`Computing similarity for ${articles.length} articles...`);

  // Compute pairwise cosine similarity and store top-N per article
  for (let i = 0; i < articles.length; i++) {
    const scores = [];
    for (let j = 0; j < articles.length; j++) {
      if (i === j) continue;
      const score = cosineSimilarity(vectors[i], vectors[j]);
      if (score > 0) {
        scores.push({ slug: articles[j].slug, score: Math.round(score * 1000) / 1000 });
      }
    }
    scores.sort((a, b) => b.score - a.score);
    articles[i].similar = scores.slice(0, topN);
  }

  console.log('Similarity computation complete.');
  return articles;
}
