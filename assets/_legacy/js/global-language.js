(() => {
  'use strict';

  const STORAGE_KEY = 'portfolioLanguage';
  const LEGACY_KEY = 'lang';
  const SUPPORTED = new Set(['fr', 'en']);
  const root = document.documentElement;
  const dictionaries = window.PORTFOLIO_TRANSLATIONS || { fr: {}, en: {} };
  let currentLanguage = null;
  let observer = null;

  const safeGet = (key) => {
    try { return localStorage.getItem(key); } catch (_) { return null; }
  };
  const safeSet = (key, value) => {
    try { localStorage.setItem(key, value); } catch (_) {}
  };

  const queryLanguage = () => {
    try {
      const value = new URL(window.location.href).searchParams.get('lang');
      return SUPPORTED.has(value) ? value : null;
    } catch (_) { return null; }
  };

  const inferredLanguage = () => {
    const file = (window.location.pathname.split('/').pop() || '').toLowerCase();
    if (file === 'index-en.html') return 'en';
    const declared = (root.getAttribute('lang') || '').toLowerCase().slice(0, 2);
    return SUPPORTED.has(declared) ? declared : 'fr';
  };

  const getLanguage = () => {
    const candidate = queryLanguage() || safeGet(STORAGE_KEY) || safeGet(LEGACY_KEY) || inferredLanguage();
    return SUPPORTED.has(candidate) ? candidate : 'fr';
  };

  const isHomePage = () => {
    const file = (window.location.pathname.split('/').pop() || '').toLowerCase();
    return file === '' || file === 'index.html' || file === 'index-en.html';
  };

  const homeFile = (lang) => lang === 'en' ? 'index-en.html' : 'index.html';

  const persist = (lang) => {
    safeSet(STORAGE_KEY, lang);
    safeSet(LEGACY_KEY, lang);
  };

  const translateElement = (element, lang) => {
    const table = dictionaries[lang] || {};

    const textKey = element.getAttribute('data-i18n');
    if (textKey && Object.prototype.hasOwnProperty.call(table, textKey)) {
      element.textContent = table[textKey];
    }

    const htmlKey = element.getAttribute('data-i18n-html');
    if (htmlKey && Object.prototype.hasOwnProperty.call(table, htmlKey)) {
      element.innerHTML = table[htmlKey];
    }

    const placeholderKey = element.getAttribute('data-i18n-placeholder');
    if (placeholderKey && Object.prototype.hasOwnProperty.call(table, placeholderKey)) {
      element.setAttribute('placeholder', table[placeholderKey]);
    }

    const titleKey = element.getAttribute('data-i18n-title');
    if (titleKey && Object.prototype.hasOwnProperty.call(table, titleKey)) {
      element.setAttribute('title', table[titleKey]);
    }

    const ariaKey = element.getAttribute('data-i18n-aria-label');
    if (ariaKey && Object.prototype.hasOwnProperty.call(table, ariaKey)) {
      element.setAttribute('aria-label', table[ariaKey]);
    }
  };

  const applyLanguageToSubtree = (scope, lang) => {
    if (!scope || scope.nodeType !== 1) return;

    const languageNodes = scope.matches?.('[data-lang]') ? [scope] : [];
    scope.querySelectorAll?.('[data-lang]').forEach((node) => languageNodes.push(node));
    languageNodes.forEach((element) => {
      const visible = element.getAttribute('data-lang') === lang;
      element.hidden = !visible;
      element.setAttribute('aria-hidden', String(!visible));
    });

    const translatedNodes = scope.matches?.('[data-i18n],[data-i18n-html],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria-label]') ? [scope] : [];
    scope.querySelectorAll?.('[data-i18n],[data-i18n-html],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria-label]').forEach((node) => translatedNodes.push(node));
    translatedNodes.forEach((element) => translateElement(element, lang));
  };

  const syncControls = (lang) => {
    document.querySelectorAll('[data-set-lang], .lang-chip').forEach((control) => {
      let value = control.getAttribute('data-set-lang');
      if (!value) {
        const text = (control.textContent || '').trim().toLowerCase();
        value = text.startsWith('en') ? 'en' : 'fr';
      }
      const active = value === lang;
      control.setAttribute('aria-pressed', String(active));
      control.classList.toggle('is-active', active);
      if (active) control.setAttribute('aria-current', 'true');
      else control.removeAttribute('aria-current');
    });

    document.querySelectorAll('select[id*="lang" i], select[data-language-switch]').forEach((select) => {
      if ([...select.options].some((option) => option.value === lang)) select.value = lang;
    });
  };

  const updateDocumentTitle = (lang) => {
    const title = document.querySelector('title');
    if (!title) return;
    const translated = title.getAttribute(`data-page-title-${lang}`);
    if (translated) document.title = translated;
  };

  const languageAwareHref = (rawHref, lang) => {
    if (!rawHref || /^(https?:|mailto:|tel:|javascript:)/i.test(rawHref) || rawHref.startsWith('#')) return rawHref;
    try {
      const url = new URL(rawHref, window.location.href);
      if (url.protocol !== 'file:' && url.origin !== window.location.origin) return rawHref;
      const file = (url.pathname.split('/').pop() || '').toLowerCase();
      if (file === 'index.html' || file === 'index-en.html' || file === '') {
        url.pathname = url.pathname.replace(/(?:index(?:-en)?\.html)?$/, homeFile(lang));
      }
      if (/\.html$/i.test(url.pathname)) url.searchParams.set('lang', lang);
      return url.href;
    } catch (_) { return rawHref; }
  };

  const rewriteInternalLinks = (lang) => {
    document.querySelectorAll('a[href]').forEach((link) => {
      const original = link.getAttribute('data-lang-original-href') || link.getAttribute('href');
      if (!link.hasAttribute('data-lang-original-href')) link.setAttribute('data-lang-original-href', original || '');
      const next = languageAwareHref(original, lang);
      if (next) link.setAttribute('href', next);
    });

    document.querySelectorAll('a[href*="CV_GouaHenri_"]').forEach((link) => {
      const current = link.getAttribute('href') || '';
      link.setAttribute('href', current.replace(/CV_GouaHenri_(?:FR|EN)\.pdf/i, `CV_GouaHenri_${lang === 'en' ? 'EN' : 'FR'}.pdf`));
    });
  };

  const updateQueryWithoutReload = (lang) => {
    try {
      const url = new URL(window.location.href);
      url.searchParams.set('lang', lang);
      history.replaceState(history.state, '', url.href);
    } catch (_) {}
  };

  const navigateHomeVariant = (lang) => {
    if (!isHomePage()) return false;
    const currentFile = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
    const targetFile = homeFile(lang);
    if (currentFile === targetFile) return false;
    const target = new URL(targetFile, window.location.href);
    target.searchParams.set('lang', lang);
    target.hash = window.location.hash;
    window.location.replace(target.href);
    return true;
  };

  const notifyDependentComponents = (lang) => {
    window.dispatchEvent(new CustomEvent('portfolio:languagechange', { detail: { language: lang } }));
  };

  const applyLanguage = (lang) => {
    currentLanguage = lang;
    root.lang = lang;
    root.dataset.siteLang = lang;
    root.dataset.expLang = lang;
    root.dataset.projLang = lang;

    applyLanguageToSubtree(document.body, lang);
    syncControls(lang);
    updateDocumentTitle(lang);
    rewriteInternalLinks(lang);
    updateQueryWithoutReload(lang);
    notifyDependentComponents(lang);
  };

  const setLanguage = (lang, options = {}) => {
    const next = SUPPORTED.has(lang) ? lang : 'fr';
    persist(next);
    if (options.navigateHome !== false && navigateHomeVariant(next)) return;
    applyLanguage(next);
  };

  const ensureSwitcher = () => {
    const hasSwitcher = document.querySelector('[data-set-lang], .lang-chip, select[id*="lang" i], select[data-language-switch]');
    if (hasSwitcher) return;
    const wrapper = document.createElement('div');
    wrapper.className = 'global-lang-switch';
    wrapper.setAttribute('aria-label', 'Language switcher');
    wrapper.innerHTML = '<button type="button" data-set-lang="fr">FR</button><button type="button" data-set-lang="en">EN</button>';
    document.body.appendChild(wrapper);
  };

  const bindControls = () => {
    document.addEventListener('click', (event) => {
      const control = event.target.closest('[data-set-lang], .lang-chip');
      if (!control) return;
      let lang = control.getAttribute('data-set-lang');
      if (!lang) {
        const text = (control.textContent || '').trim().toLowerCase();
        lang = text.startsWith('en') ? 'en' : 'fr';
      }
      if (!SUPPORTED.has(lang)) return;
      event.preventDefault();
      event.stopImmediatePropagation();
      setLanguage(lang);
    }, true);

    document.addEventListener('change', (event) => {
      const select = event.target.closest('select[id*="lang" i], select[data-language-switch]');
      if (!select || !SUPPORTED.has(select.value)) return;
      event.stopImmediatePropagation();
      setLanguage(select.value);
    }, true);
  };

  const observeDynamicContent = () => {
    if (!('MutationObserver' in window) || observer) return;
    observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
          if (node.nodeType === 1) applyLanguageToSubtree(node, currentLanguage || getLanguage());
        });
      });
      syncControls(currentLanguage || getLanguage());
      rewriteInternalLinks(currentLanguage || getLanguage());
    });
    observer.observe(document.body, { childList: true, subtree: true });
  };

  const initial = getLanguage();
  persist(initial);

  if (isHomePage() && navigateHomeVariant(initial)) return;

  const boot = () => {
    ensureSwitcher();
    bindControls();
    applyLanguage(initial);
    observeDynamicContent();
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
  else boot();

  window.PortfolioLanguage = {
    get: () => currentLanguage || getLanguage(),
    set: setLanguage,
    apply: () => applyLanguage(currentLanguage || getLanguage())
  };
})();
