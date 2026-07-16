(() => {
  'use strict';
  const hero = document.querySelector('.project-detail-hero');
  const bar = document.querySelector('.legacy-sticky-titlebar');
  const update = () => {
    if (!hero || !bar) return;
    const show = hero.getBoundingClientRect().bottom <= 8;
    bar.classList.toggle('is-visible', show);
    bar.setAttribute('aria-hidden', String(!show));
  };
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });
  document.querySelectorAll('[data-smart-back]').forEach(link => {
    link.addEventListener('click', (event) => {
      const ref = document.referrer;
      if (ref && history.length > 1) {
        event.preventDefault();
        history.back();
      }
    });
  });
  update();
})();
