(() => {
  'use strict';

  const root = document.documentElement;
  const body = document.body;

  const safeStorage = {
    get(key, fallback) {
      try { return localStorage.getItem(key) || fallback; }
      catch (_) { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); }
      catch (_) { /* file:// and privacy modes may block storage */ }
    }
  };

  const setLanguage = (lang) => {
    const next = lang === 'en' ? 'en' : 'fr';
    root.dataset.expLang = next;
    root.lang = next;
    safeStorage.set('portfolioLanguage', next); safeStorage.set('lang', next);

    const title = document.querySelector('title');
    const translatedTitle = title?.getAttribute(`data-page-title-${next}`);
    if (translatedTitle) document.title = translatedTitle;

    document.querySelectorAll('[data-set-lang]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.setLang === next));
    });
  };

  const applyTheme = (theme) => {
    const next = theme === 'light' ? 'light' : 'dark';
    body.classList.toggle('light-theme', next === 'light');
    safeStorage.set('theme', next);
  };

  const setupCompactTitle = () => {
    const hero = document.querySelector('.exp-hero');
    const stickyTitle = document.querySelector('.exp-sticky-titlebar');
    if (!hero || !stickyTitle) return;

    let ticking = false;
    const update = () => {
      const shouldShow = hero.getBoundingClientRect().bottom <= 0;
      stickyTitle.classList.toggle('is-visible', shouldShow);
      stickyTitle.setAttribute('aria-hidden', String(!shouldShow));
      ticking = false;
    };

    const onScroll = () => {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();
  };

  const revealContent = () => {
    const elements = [...document.querySelectorAll('.reveal-up')];
    if (!elements.length) return;

    // Content must remain visible even when IntersectionObserver is unavailable
    // or the page is opened directly from the local filesystem.
    if (!('IntersectionObserver' in window)) {
      elements.forEach((element) => element.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.08,
      rootMargin: '0px 0px -4% 0px'
    });

    elements.forEach((element) => observer.observe(element));

    // Safety fallback: never leave content hidden because of browser quirks.
    window.setTimeout(() => {
      elements.forEach((element) => element.classList.add('is-visible'));
    }, 700);
  };

  setLanguage(safeStorage.get('portfolioLanguage', safeStorage.get('lang', 'fr')));
  applyTheme(safeStorage.get('theme', 'dark'));

  document.querySelectorAll('[data-set-lang]').forEach((button) => {
    button.addEventListener('click', () => setLanguage(button.dataset.setLang));
  });

  document.querySelectorAll('[data-theme-toggle]').forEach((button) => {
    button.addEventListener('click', () => {
      applyTheme(body.classList.contains('light-theme') ? 'dark' : 'light');
    });
  });


  document.querySelectorAll('[data-smart-back]').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (document.referrer && history.length > 1) {
        event.preventDefault();
        history.back();
      }
    });
  });

  revealContent();
  setupCompactTitle();
})();
