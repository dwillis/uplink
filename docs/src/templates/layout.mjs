export function layout({ title, content, bodyClass = '', basePath = '/' }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapeHtml(title)} — Uplink Archive</title>
  <link rel="stylesheet" href="${basePath}css/style.css">
  <script src="https://unpkg.com/lunr@2.3.9/lunr.min.js"></script>
  <script>window.BASE_PATH="${basePath}";</script>
</head>
<body class="${bodyClass}">
  <header class="site-header">
    <div class="container">
      <a href="${basePath}" class="site-title">Uplink</a>
      <p class="site-tagline">Computer-Assisted Reporting Newsletter, 1990–2007</p>
      <nav class="site-nav">
        <a href="${basePath}">Browse</a>
        <a href="${basePath}topics/">Topics</a>
        <a href="${basePath}search.html">Search</a>
      </nav>
    </div>
  </header>
  <main class="container">
    ${content}
  </main>
  <footer class="site-footer">
    <div class="container">
      <p>Uplink newsletter archive · <a href="https://github.com/dwillis/uplink">GitHub</a></p>
    </div>
  </footer>
</body>
</html>`;
}

export function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

export function topicBadges(topics, prefix = '/') {
  return (topics || []).map(t => {
    const slug = t.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    return `<a href="${prefix}topics/${slug}.html" class="badge">${escapeHtml(t)}</a>`;
  }).join('');
}
