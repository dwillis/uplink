(function () {
  'use strict';

  const list = document.getElementById('article-list');
  const yearFilter = document.getElementById('year-filter');
  const sortOrder = document.getElementById('sort-order');

  if (!list) return;

  const cards = Array.from(list.querySelectorAll('.article-card'));

  function applyFilters() {
    const year = yearFilter ? yearFilter.value : '';
    const sort = sortOrder ? sortOrder.value : 'newest';

    let visible = cards.filter(card => {
      if (year && card.dataset.year !== year) return false;
      return true;
    });

    if (sort === 'oldest') {
      visible = visible.slice().reverse();
    }

    // Hide all, then show filtered in order
    cards.forEach(c => (c.style.display = 'none'));
    visible.forEach(c => {
      c.style.display = '';
      list.appendChild(c);
    });

    const count = document.querySelector('.count');
    if (count) count.textContent = `(${visible.length})`;
  }

  if (yearFilter) yearFilter.addEventListener('change', applyFilters);
  if (sortOrder) sortOrder.addEventListener('change', applyFilters);
})();
