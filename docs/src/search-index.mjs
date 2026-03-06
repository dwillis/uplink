import lunr from 'lunr';

export function buildSearchIndex(articles) {
  const idx = lunr(function () {
    this.ref('slug');
    this.field('headline', { boost: 10 });
    this.field('author_name', { boost: 5 });
    this.field('keywords', { boost: 5 });
    this.field('summary', { boost: 3 });

    for (const article of articles) {
      this.add({
        slug: article.slug,
        headline: article.headline,
        author_name: article.author_name,
        keywords: (article.keywords || []).join(' '),
        summary: article.summary || '',
      });
    }
  });

  console.log(`Search index built for ${articles.length} articles.`);
  return idx;
}
