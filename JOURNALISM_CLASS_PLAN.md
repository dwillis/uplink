# Journalism Class Plan: Exploring the Uplink Newsletter Collection

## Project Overview

This curriculum guides students through exploring, organizing, and enhancing a historical collection of **Uplink newsletters** (1990-2007) - publications that documented the early days of computer-assisted reporting and data journalism. Students will use Python and LLM libraries to analyze this collection and build a public website showcasing these foundational texts.

**Collection Stats:**
- ~150 newsletter issues spanning 1990-2007
- ~148 PDF source documents
- Pre-processed JSON files with extracted articles
- Topics: Early database journalism, FOIA data requests, investigative techniques

---

## Learning Objectives

By the end of this project, students will:
1. Understand the history and evolution of data journalism
2. Use Python LLM libraries (OpenAI, Anthropic Claude, Google Gemini, or local models)
3. Perform content analysis, categorization, and enhancement using AI
4. Structure and organize large text collections
5. Build a searchable, public-facing website
6. Practice ethical considerations in AI-assisted journalism

---

## Prerequisites

- Basic Python knowledge (variables, loops, functions)
- Familiarity with command line/terminal
- Text editor or IDE (VS Code recommended)
- Git basics (optional but helpful)

---

## Phase 1: Setup & Exploration (Weeks 1-2)

### Week 1: Environment Setup

**Goals:**
- Set up Python environment
- Explore the existing collection
- Understand the data structure

**Activities:**

1. **Install Python Dependencies**
   ```bash
   # Install uv (modern Python package manager)
   pip install uv

   # Install required packages
   uv pip install openai anthropic google-generativeai python-dotenv pandas
   ```

2. **Explore the Collection Structure**
   - Review the existing JSON files in `/articles/`
   - Examine a sample article structure
   - Count total articles and date ranges
   - Identify common themes and authors

3. **Assignment: Collection Inventory**
   - Write a Python script to:
     - Count total articles
     - List all unique authors
     - Create a timeline of publications
     - Identify the most common keywords

### Week 2: Understanding LLM APIs

**Goals:**
- Learn to interact with LLM APIs
- Understand prompting techniques
- Compare different models

**Activities:**

1. **Choose Your LLM Provider**
   Options:
   - **OpenAI** (GPT-4o, GPT-4o-mini) - Already used in processor.py
   - **Anthropic Claude** (Claude 3.5 Sonnet, Haiku) - Excellent for analysis
   - **Google Gemini** (Gemini 2.0 Flash) - Fast and cost-effective
   - **Local Models** (via Ollama) - Free, privacy-focused

2. **First LLM Script**
   Create `explore_article.py` to:
   - Load a single article from JSON
   - Send it to an LLM with a simple prompt
   - Ask the LLM to summarize the article's main points
   - Extract the historical significance

3. **Assignment: Prompting Comparison**
   - Test the same article with different prompts
   - Compare outputs from different models (if access available)
   - Document which prompts work best for different tasks

---

## Phase 2: Content Analysis & Enhancement (Weeks 3-5)

### Week 3: Batch Processing & Classification

**Goals:**
- Process all articles programmatically
- Create consistent categorizations
- Extract additional metadata

**Activities:**

1. **Build a Classification System**
   Create categories for articles:
   - **Topics**: FOIA/Access, Database Analysis, Tools & Technology, Case Studies, Tips & Techniques
   - **Difficulty Level**: Beginner, Intermediate, Advanced
   - **Data Types Used**: Databases, Public Records, Court Records, etc.

2. **Create `classify_articles.py`**
   ```python
   # Pseudo-code structure
   for each article:
       - Send to LLM with classification prompt
       - Extract: topics, difficulty, data types, technologies mentioned
       - Add new fields to JSON structure
       - Save enhanced version
   ```

3. **Assignment: Category Analysis**
   - Run classification on full collection
   - Create visualizations showing:
     - Topic distribution over time
     - Evolution of technologies mentioned
     - Geographical distribution of stories

### Week 4: Generating Summaries & Enhancements

**Goals:**
- Create reader-friendly summaries
- Extract teaching moments
- Identify connections between articles

**Activities:**

1. **Multi-Length Summaries**
   For each article, generate:
   - **One-liner** (tweet-length, <280 chars)
   - **Abstract** (2-3 sentences)
   - **Extended summary** (one paragraph)

2. **Extract "Lessons Learned"**
   Use LLM to identify:
   - Key reporting techniques used
   - Technical skills required
   - Obstacles overcome
   - Modern relevance/comparison

3. **Create `enhance_articles.py`**
   - Process articles in batches
   - Add rate limiting (avoid API limits)
   - Save progress incrementally
   - Handle errors gracefully

4. **Assignment: Historical Context**
   - Select 5 articles from different time periods
   - Use LLM to research historical context
   - Add "What was happening in journalism/technology" notes

### Week 5: Relationship Mapping

**Goals:**
- Identify related articles
- Build citation networks
- Create reading pathways

**Activities:**

1. **Similarity Analysis**
   - Use LLM embeddings to find similar articles
   - Cluster articles by theme
   - Identify article "series" or related pieces

2. **Create Reading Paths**
   Design curated pathways:
   - "Introduction to Computer-Assisted Reporting"
   - "Evolution of FOIA Data Access"
   - "Database Analysis Techniques"
   - "Tools & Technology Timeline"

3. **Assignment: Interactive Timeline**
   - Create a JSON file mapping articles to historical events
   - Connect technical developments to reporting innovations

---

## Phase 3: Organization & Data Modeling (Week 6)

### Week 6: Database Design

**Goals:**
- Design optimal data structure for website
- Create search indices
- Prepare for front-end display

**Activities:**

1. **Design Final Data Schema**
   ```json
   {
     "id": "unique-article-id",
     "headline": "original headline",
     "slug": "url-friendly-slug",
     "year": 1990,
     "month": "October",
     "date": "1990-10",
     "author": {
       "name": "Author Name",
       "title": "Title/Affiliation"
     },
     "full_text": "complete article text",
     "summaries": {
       "one_liner": "...",
       "abstract": "...",
       "extended": "..."
     },
     "metadata": {
       "topics": ["FOIA", "Databases"],
       "difficulty": "Intermediate",
       "data_types": ["Court Records"],
       "technologies": ["dBASE", "mainframe"],
       "keywords": ["voter fraud", "death records"]
     },
     "enhancements": {
       "lessons_learned": "...",
       "modern_relevance": "...",
       "historical_context": "..."
     },
     "relationships": {
       "related_articles": ["id1", "id2"],
       "reading_path": ["beginner-path"]
     }
   }
   ```

2. **Create Master Dataset**
   - Consolidate all enhanced data
   - Generate unique IDs
   - Create search index (using tools like `whoosh` or prepare for Elasticsearch)

3. **Assignment: Data Quality Check**
   - Validate all articles have required fields
   - Check for duplicates
   - Ensure text formatting is clean

---

## Phase 4: Website Development (Weeks 7-10)

### Week 7: Static Site Planning

**Goals:**
- Choose website technology
- Design user experience
- Plan site structure

**Technology Options:**

1. **Static Site Generators (Recommended for beginners)**
   - **Eleventy (11ty)** - JavaScript-based, flexible
   - **Hugo** - Fast, simple
   - **Jekyll** - Ruby-based, GitHub Pages friendly

2. **Modern Frameworks**
   - **Next.js** - React-based, excellent for search
   - **SvelteKit** - Lightweight, fast
   - **Astro** - Perfect for content-focused sites

**Site Structure:**
```
Homepage
├── About the Collection
├── Timeline View
├── Browse by Topic
├── Browse by Year
├── Search
└── Reading Paths
    ├── Beginner's Guide
    ├── FOIA & Access
    ├── Database Techniques
    └── Tools & Technology

Article Page
├── Headline & Metadata
├── Summaries (collapsible)
├── Full Text
├── Lessons Learned
├── Historical Context
├── Related Articles
└── Share/Citation
```

**Assignment: Site Mockups**
- Create wireframes for 3-5 key pages
- Plan navigation structure
- Design article display format

### Week 8: Building Core Pages

**Goals:**
- Set up static site generator
- Create page templates
- Import article data

**Activities:**

1. **Initialize Project**
   ```bash
   # Example with Eleventy
   npm install -g @11ty/eleventy
   eleventy --input=src --output=dist
   ```

2. **Create Templates**
   - Homepage with featured articles
   - Article detail page
   - Browse/archive pages
   - About page

3. **Data Integration**
   - Import JSON files
   - Create data pipelines
   - Build page generation logic

4. **Assignment: First Deploy**
   - Deploy basic site to GitHub Pages or Netlify
   - Share link for peer review

### Week 9: Search & Discovery Features

**Goals:**
- Implement search functionality
- Add filtering and sorting
- Create interactive timeline

**Activities:**

1. **Search Implementation**
   Options:
   - **Client-side**: Lunr.js, Fuse.js
   - **Service**: Algolia, Meilisearch
   - **Build-time**: Pagefind

2. **Filter & Sort**
   - By topic, year, author
   - By difficulty level
   - By technology mentioned

3. **Interactive Elements**
   - Timeline visualization (D3.js or Timeline.js)
   - Topic network graph
   - Related articles suggestions

4. **Assignment: User Testing**
   - Test search with classmates
   - Gather feedback on discoverability
   - Iterate on design

### Week 10: Polish & Enhancement

**Goals:**
- Improve design and accessibility
- Add final features
- Optimize performance

**Activities:**

1. **Design Refinement**
   - Typography and readability
   - Responsive design
   - Color scheme and branding

2. **Accessibility**
   - Semantic HTML
   - ARIA labels
   - Keyboard navigation
   - Screen reader testing

3. **SEO & Performance**
   - Meta tags and descriptions
   - Image optimization
   - Loading performance
   - Social media previews

4. **Final Features**
   - Citation generator
   - Print-friendly view
   - RSS feed
   - Download original PDFs option

**Assignment: Final Presentation**
- 5-minute presentation on process and findings
- Demo the website
- Reflect on what you learned

---

## Phase 5: Reflection & Publication (Week 11-12)

### Week 11: Documentation & Methodology

**Goals:**
- Document your process
- Reflect on AI ethics
- Create reproducible workflow

**Activities:**

1. **Write Methodology Documentation**
   - How articles were processed
   - What LLM prompts were used
   - How classifications were made
   - Limitations and biases

2. **Create User Guide**
   - How to navigate the site
   - How to cite articles
   - How to contribute corrections

3. **Ethical Reflection Paper**
   Topics to address:
   - Accuracy of LLM-generated summaries
   - Bias in categorization
   - Transparency in AI use
   - Attribution and authorship

4. **Assignment: Process Blog Post**
   - Write about your experience
   - Share interesting discoveries
   - Discuss challenges and solutions

### Week 12: Launch & Promotion

**Goals:**
- Public launch of website
- Share with journalism community
- Plan for maintenance

**Activities:**

1. **Final Review**
   - Content accuracy check
   - Link testing
   - Cross-browser testing
   - Performance audit

2. **Launch Plan**
   - Announce on social media
   - Share with journalism educators
   - Contact IRE (Investigative Reporters & Editors)
   - Reach out to original authors

3. **Create Submission Plan**
   - Submit to journalism archives
   - Add to relevant directories
   - Consider academic publication

4. **Maintenance Plan**
   - How to add new articles (if found)
   - How to accept corrections
   - Sustainability strategy

**Final Assignment: Reflection Essay**
- What did you learn about data journalism history?
- How has AI changed your understanding of journalism?
- What surprised you most about the collection?
- How would you apply these skills to future reporting?

---

## Technical Skills Checklist

By project completion, students will have practiced:

**Python:**
- [ ] File I/O and JSON manipulation
- [ ] API interactions and rate limiting
- [ ] Batch processing and error handling
- [ ] Data transformation and cleaning
- [ ] Creating reusable scripts

**LLM & AI:**
- [ ] Prompt engineering
- [ ] API usage (OpenAI, Claude, or Gemini)
- [ ] Text classification and summarization
- [ ] Embeddings and similarity search
- [ ] Understanding AI limitations

**Web Development:**
- [ ] Static site generation
- [ ] HTML/CSS/JavaScript basics
- [ ] Search implementation
- [ ] Responsive design
- [ ] Deployment and hosting

**Journalism:**
- [ ] Historical research
- [ ] Source verification
- [ ] Metadata creation
- [ ] Information architecture
- [ ] Public presentation

---

## Sample Code Snippets

### 1. Basic Article Processing Script

```python
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def enhance_article(article):
    """Generate enhancements for a single article"""

    prompt = f"""
    Analyze this 1990s computer-assisted reporting article:

    Headline: {article['headline']}
    Author: {article['author_name']}
    Year: {article['year']}

    Text: {article['full_text'][:2000]}...

    Provide:
    1. One-line summary (max 280 chars)
    2. Three main topics/tags
    3. Difficulty level (Beginner/Intermediate/Advanced)
    4. Key lesson learned
    5. Modern relevance

    Return as JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

# Process all articles
for filename in os.listdir("articles"):
    if filename.endswith(".json"):
        with open(f"articles/{filename}", 'r') as f:
            data = json.load(f)

        for article in data['articles']:
            enhancement = enhance_article(article)
            article['enhancement'] = enhancement

        # Save enhanced version
        with open(f"enhanced/{filename}", 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Processed {filename}")
```

### 2. Find Similar Articles (Using Embeddings)

```python
from openai import OpenAI
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI()

def get_embedding(text):
    """Get embedding vector for text"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text[:8000]  # Truncate if needed
    )
    return response.data[0].embedding

def find_similar_articles(target_article, all_articles, top_n=5):
    """Find most similar articles using embeddings"""

    # Get embedding for target
    target_embedding = get_embedding(target_article['full_text'])

    # Get embeddings for all articles
    similarities = []
    for article in all_articles:
        if article['headline'] == target_article['headline']:
            continue

        article_embedding = get_embedding(article['full_text'])
        similarity = cosine_similarity(
            [target_embedding],
            [article_embedding]
        )[0][0]

        similarities.append({
            'article': article,
            'similarity': similarity
        })

    # Sort and return top N
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    return similarities[:top_n]
```

### 3. Build Timeline Data

```python
import json
from collections import defaultdict
from datetime import datetime

def build_timeline():
    """Create timeline data structure for visualization"""

    timeline = defaultdict(list)

    for filename in os.listdir("enhanced"):
        if filename.endswith(".json"):
            with open(f"enhanced/{filename}", 'r') as f:
                data = json.load(f)

            for article in data['articles']:
                date_key = f"{article['year']}-{article['month']}"

                timeline[date_key].append({
                    'headline': article['headline'],
                    'summary': article['enhancement']['one_line'],
                    'topics': article['enhancement']['topics'],
                    'author': article['author_name']
                })

    # Convert to sorted list for frontend
    timeline_list = []
    for date, articles in sorted(timeline.items()):
        timeline_list.append({
            'date': date,
            'count': len(articles),
            'articles': articles
        })

    # Save for website
    with open('site/data/timeline.json', 'w') as f:
        json.dump(timeline_list, f, indent=2)

    return timeline_list
```

---

## Assessment Rubric

### Technical Execution (40%)
- Code quality and organization
- Successful LLM integration
- Data processing completeness
- Website functionality

### Content & Analysis (30%)
- Accuracy of enhancements
- Quality of categorization
- Depth of historical research
- Insightful connections

### Design & UX (20%)
- Website usability
- Visual design
- Accessibility compliance
- Search effectiveness

### Reflection & Documentation (10%)
- Methodology transparency
- Ethical considerations
- Process documentation
- Learning reflection

---

## Resources & References

### LLM APIs & Documentation
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude API](https://docs.anthropic.com)
- [Google Gemini API](https://ai.google.dev/docs)
- [Ollama (Local Models)](https://ollama.ai)

### Data Journalism History
- [IRE (Investigative Reporters & Editors)](https://www.ire.org)
- [NICAR (National Institute for Computer-Assisted Reporting)](https://www.ire.org/nicar/)
- [Data Journalism Handbook](https://datajournalism.com)

### Web Development
- [Eleventy Documentation](https://www.11ty.dev)
- [MDN Web Docs](https://developer.mozilla.org)
- [Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

### Python Libraries
- `openai` - OpenAI API client
- `anthropic` - Claude API client
- `google-generativeai` - Gemini API
- `pandas` - Data manipulation
- `python-dotenv` - Environment variables
- `lunr` - Client-side search

---

## Extension Ideas

For advanced students or continued work:

1. **Oral Histories**: Interview original authors about the early days
2. **Comparative Analysis**: Compare 1990s techniques to modern tools
3. **Interactive Tutorials**: Create lessons teaching techniques from articles
4. **API Development**: Build an API for the collection
5. **Machine Translation**: Translate collection to other languages
6. **Podcast Series**: Create audio versions with commentary
7. **Academic Paper**: Analyze evolution of data journalism
8. **Tool Recreation**: Rebuild vintage tools with modern equivalents
9. **Contribution Platform**: Allow community corrections/additions
10. **Educational Curriculum**: Create lesson plans for high schools

---

## Project Success Criteria

This project will be successful if:

- ✅ All articles are processed and enhanced with LLM-generated metadata
- ✅ A public website makes the collection searchable and browsable
- ✅ Students can articulate the history of computer-assisted reporting
- ✅ The methodology is transparent and reproducible
- ✅ The website is accessible and user-friendly
- ✅ Students demonstrate ethical awareness in AI use
- ✅ The collection is preserved and made available to journalism community

---

## Contact & Contribution

This project preserves an important part of journalism history. We welcome:
- Corrections and additions
- Memories from original readers/authors
- Additional Uplink issues we may have missed
- Technical improvements to the website

---

*Last Updated: November 2025*
*This curriculum is designed for a 12-week semester course but can be adapted for shorter workshops or self-paced learning.*
