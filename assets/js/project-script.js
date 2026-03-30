/* =========================================================
   PROJECT PAGES SCRIPT
   - Synchronisation de la langue & thème
   - Back button dans le sticky header au scroll
========================================================= */

(() => {
    'use strict';

    /* -----------------------
       Utils DOM
    ----------------------- */
    const $ = (s, r = document) => r.querySelector(s);
    const $$ = (s, r = document) => r.querySelectorAll(s);

    function safeFeatherReplace() {
        if (typeof feather !== 'undefined' && typeof feather.replace === 'function') {
            feather.replace();
        }
    }

    /* -----------------------
       Système de Thème
    ----------------------- */
    function applyTheme(theme) {
        const isLight = theme === 'light';
        document.body.classList.toggle('light-theme', isLight);
        localStorage.setItem('theme', theme);
        const meta = document.querySelector('meta[name="theme-color"]');
        if (meta) meta.setAttribute('content', getComputedStyle(document.body).getPropertyValue('--background-color').trim());
    }

    function initTheme() {
        if (localStorage.getItem('darkMode') !== null) {
            const wasDark = localStorage.getItem('darkMode') === 'true';
            localStorage.removeItem('darkMode');
            localStorage.setItem('theme', wasDark ? 'dark' : 'light');
        }
        const saved = localStorage.getItem('theme') || 'dark';
        applyTheme(saved);
    }

    /* -----------------------
       i18n (traductions)
    ----------------------- */
    async function changeLanguage(lang) {
        try {
            const response = await fetch(`../assets/lang/${lang}.json`, { cache: 'no-store' });
            const translations = await response.json();

            // Textes simples
            $$('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (translations[key]) el.textContent = translations[key];
            });

            // Contenus riches
            $$('[data-i18n-html]').forEach(el => {
                const key = el.getAttribute('data-i18n-html');
                if (translations[key]) el.innerHTML = translations[key];
            });

            localStorage.setItem('lang', lang);
        } catch (err) {
            console.error('Erreur chargement langue:', err);
        }
    }

    function initLanguage() {
        const defaultLang = localStorage.getItem('lang') || 'en';
        changeLanguage(defaultLang);
    }

    /* -----------------------
       Sticky Back Button
    ----------------------- */
    function initStickyBackButton() {
        const hero = $('.project-detail-hero');
        const headerContainer = $('.project-header-container');
        const backNav = $('.back-nav');

        if (!hero || !headerContainer || !backNav) return;

        // Créer une copie du back button pour le sticky header
        const backButton = $('.back-link');
        if (!backButton) return;

        let stickyBackButton = null;
        const scrollThreshold = 100;

        window.addEventListener('scroll', () => {
            const isScrolled = window.scrollY > scrollThreshold;

            hero.classList.toggle('is-sticky', isScrolled);

            if (isScrolled && !stickyBackButton) {
                // Créer et afficher le bouton dans le sticky header
                stickyBackButton = document.createElement('div');
                stickyBackButton.className = 'sticky-back-button';
                stickyBackButton.innerHTML = `
          <a href="../index.html#projects" class="back-link">
            <i data-feather="arrow-left" style="width: 18px; color: var(--primary-color);"></i>
            <span data-i18n="btn_back_projects">Back to Projects</span>
          </a>
        `;
                headerContainer.insertBefore(stickyBackButton, headerContainer.firstChild);

                // Réappliquer feather icons et traductions
                safeFeatherReplace();
                const span = stickyBackButton.querySelector('[data-i18n="btn_back_projects"]');
                const savedLang = localStorage.getItem('lang') || 'en';

                fetch(`../assets/lang/${savedLang}.json`)
                    .then(r => r.json())
                    .then(t => {
                        if (t['btn_back_projects']) {
                            span.textContent = t['btn_back_projects'];
                        }
                    });
            } else if (!isScrolled && stickyBackButton) {
                // Retirer le bouton quand on remonte
                stickyBackButton.remove();
                stickyBackButton = null;
            }
        });
    }

    /* -----------------------
       Reveal au scroll
    ----------------------- */
    function initReveal() {
        const io = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('is-visible');
                }
            });
        }, { threshold: 0.1 });

        $$('.reveal-up').forEach(el => io.observe(el));
    }

    /* -----------------------
       Init
    ----------------------- */
    function init() {
        safeFeatherReplace();
        initTheme();
        initLanguage();
        initReveal();
        initStickyBackButton();
    }

    if (document.readyState === 'loading') {
        window.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
