import natural from 'natural';

const { TfIdf } = natural;

// Curated topic taxonomy: topic name -> keywords to match (lowercase)
const TAXONOMY = {
  'Data & Databases': [
    'data', 'database', 'databases', 'records', 'spreadsheet', 'spreadsheets',
    'statistics', 'statistical', 'sql', 'access', 'dbase', 'foxpro', 'excel',
    'tape', 'magnetic tape', 'diskette', 'dataset', 'datasets', 'data analysis',
    'data sharing', 'data journalism', 'data matching', 'database matching',
  ],
  'Investigative Methods': [
    'investigation', 'investigative', 'car', 'computer-assisted reporting',
    'computer assisted reporting', 'analysis', 'reporting', 'methodology',
    'foia', 'public records', 'records request', 'open records',
    'document analysis', 'tipsheet',
  ],
  'Crime & Justice': [
    'crime', 'criminal', 'police', 'courts', 'prison', 'jail', 'felony',
    'felons', 'murder', 'homicide', 'sentencing', 'parole', 'probation',
    'law enforcement', 'justice', 'criminal justice', 'convicted', 'arrests',
    'sex offenders', 'voter fraud', 'fraud',
  ],
  'Government & Politics': [
    'government', 'politics', 'elections', 'voter', 'voters', 'voting',
    'legislature', 'campaign', 'campaign contributions', 'political',
    'congress', 'senate', 'federal', 'state government', 'city government',
    'election', 'political analysis', 'political favors', 'lobbying',
    'transparency', 'accountability',
  ],
  'Public Safety': [
    'safety', 'faa', 'aviation', 'transportation', 'fire', 'accident',
    'accidents', 'aviation accidents', 'airline', 'highway', 'traffic',
    'bridge', 'infrastructure', 'workplace safety', 'osha', 'military',
  ],
  'Health & Environment': [
    'health', 'environment', 'pollution', 'toxic', 'water', 'air quality',
    'cancer', 'disease', 'hospital', 'hospitals', 'medical', 'healthcare',
    'pharmaceutical', 'drugs', 'contamination', 'chemical', 'epa',
    'environmental', 'public health',
  ],
  'Education': [
    'education', 'schools', 'school', 'university', 'students', 'teachers',
    'college', 'graduation', 'test scores', 'curriculum', 'student',
    'academic', 'classroom',
  ],
  'Business & Economy': [
    'business', 'economy', 'contracts', 'real estate', 'financial',
    'tax', 'taxes', 'tax loophole', 'property taxes', 'farm tax',
    'corporate', 'subsidies', 'budget', 'spending', 'economic',
    'insurance', 'banking', 'finance',
  ],
  'Journalism & Newsroom': [
    'journalism', 'newsroom', 'training', 'conference', 'editors',
    'reporter', 'reporters', 'nicar', 'ire', 'investigative reporters',
    'missouri', 'car conference', 'media', 'news', 'broadcast', 'television',
    'resources',
  ],
  'Technology': [
    'technology', 'computers', 'internet', 'software', 'hardware',
    'programming', 'gis', 'mapping', 'geographic information', 'digital',
    'online', 'web', 'network', 'mainframe', 'unix',
  ],
  'Demographics & Census': [
    'census', 'demographics', 'population', 'race', 'racial', 'racial bias',
    'poverty', 'income', 'housing', 'neighborhood', 'community',
    'geographic', 'policing',
  ],
  'Agriculture & Land': [
    'agriculture', 'farm', 'farming', 'land', 'property', 'rural',
    'livestock', 'crop', 'food inspection', 'restaurant', 'sanitation',
    'food safety', 'inspection',
  ],
};

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
