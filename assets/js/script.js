/* =========================================================
   PORTFOLIO — SCRIPT PRINCIPAL (propre & minimal)
   - Filtres projets
   - Reveal au scroll (IO)
   - i18n (texte + HTML)
   - Thème clair (light-mode) + migration ancien darkMode
   - Menu mobile (accessibilité, lock scroll, click-outside, ESC)
   - Scroll spy (aria-current)
   - Smooth scroll avec offset header
   - Validation instantanée du formulaire de contact
   - Loader fade-out
========================================================= */

(() => {
  'use strict';

  /* -----------------------
     Utils DOM
  ----------------------- */
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => r.querySelectorAll(s);

  /* -----------------------
     Loader fade out
  ----------------------- */
  function fadeOutLoader() {
    const loader = $('#loader');
    if (!loader) return;
    // Petite marge pour laisser respirer le rendu initial
    setTimeout(() => {
      loader.style.opacity = '0';
      setTimeout(() => { loader.style.display = 'none'; }, 500);
    }, 800);
  }

  /* -----------------------
     Système de Thème Jour/Nuit
  ----------------------- */

  // --- THEME ---
  function applyTheme(theme) {
    const isLight = theme === 'light';
    document.body.classList.toggle('light-theme', isLight);
    localStorage.setItem('theme', theme);
    // (optionnel) teinte d'UI navigateur mobile
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', getComputedStyle(document.body).getPropertyValue('--background-color').trim());
  }

  function initThemeToggle(){
    // Migration depuis l'ancien stockage, si existait
    if (localStorage.getItem('darkMode') !== null) {
      const wasDark = localStorage.getItem('darkMode') === 'true';
      localStorage.removeItem('darkMode');
      localStorage.setItem('theme', wasDark ? 'dark' : 'light');
    }

    const saved = localStorage.getItem('theme') || 'dark';
    applyTheme(saved);

    // Bouton thème desktop
    const btn = document.getElementById('themeToggle');
    if (btn) {
      btn.addEventListener('click', () => {
        const next = document.body.classList.contains('light-theme') ? 'dark' : 'light';
        applyTheme(next);
      });
    }
    
    // Bouton thème mobile intégré
    const btnMobile = document.getElementById('themeToggleMobile');
    if (btnMobile) {
      btnMobile.addEventListener('click', () => {
        const next = document.body.classList.contains('light-theme') ? 'dark' : 'light';
        applyTheme(next);
      });
    }
  }

  /* -----------------------
     i18n (texte + HTML riche)
  ----------------------- */
  async function changeLanguage(lang) {
    const main = $('main');
    if (main) main.style.opacity = 0;

    try {
      const response = await fetch(`assets/lang/${lang}.json`, { cache: 'no-store' });
      const translations = await response.json();

      // Textes simples
      $$('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[key]) el.textContent = translations[key];
      });

      // Contenus riches (listes, liens, <br/>...)
      $$('[data-i18n-html]').forEach(el => {
        const key = el.getAttribute('data-i18n-html');
        if (translations[key]) el.innerHTML = translations[key];
      });

      // Placeholders
      $$('[data-i18n-placeholder]').forEach(el => {
        const key = el.getAttribute('data-i18n-placeholder');
        if (translations[key]) el.placeholder = translations[key];
      });

      // Typing effect alimenté par i18n si présent
      if (window.portfolioAnimations?.initTypingEffect) {
        window.portfolioAnimations.initTypingEffect(
          translations.hero_roles || ["Data Scientist"]
        );
      }

      // Persistance & <html lang="..">
      localStorage.setItem('lang', lang);
      document.documentElement.lang = lang;

      // Sync sélecteurs si dispo (desktop et mobile)
      const select = $('#langSwitcher');
      const selectMobile = $('#langSwitcherMobile');
      if (select) select.value = lang;
      if (selectMobile) selectMobile.value = lang;

    } catch (e) {
      console.warn('i18n load error', e);
    } finally {
      if (main) setTimeout(() => (main.style.opacity = 1), 200);
    }
  }

  function initI18n() {
    const select = $('#langSwitcher');
    const selectMobile = $('#langSwitcherMobile');
    const defaultLang =
      localStorage.getItem('lang') ||
      document.documentElement.lang ||
      'fr';

    // Sélecteur desktop
    if (select) {
      select.value = defaultLang;
      select.addEventListener('change', (e) => {
        changeLanguage(e.target.value);
      });
    }
    
    // Sélecteur mobile intégré
    if (selectMobile) {
      selectMobile.value = defaultLang;
      selectMobile.addEventListener('change', (e) => {
        changeLanguage(e.target.value);
      });
    }
    changeLanguage(defaultLang);
  }

  /* -----------------------
     Menu mobile (access + UX)
  ----------------------- */
  function initMobileMenu() {
    const mobileToggle = $('.mobile-menu-toggle');
    const navLinks = $('.nav-links');
    const navControls = $('.nav-controls');

    if (!mobileToggle || !navLinks) return;

    // Accessibilité
    mobileToggle.setAttribute('aria-expanded', 'false');
    mobileToggle.setAttribute('aria-label', 'Ouvrir le menu');

    const openMenu = () => {
      mobileToggle.classList.add('active');
      navLinks.classList.add('active');
      navControls?.classList.add('active');
      mobileToggle.setAttribute('aria-expanded', 'true');
      mobileToggle.setAttribute('aria-label', 'Fermer le menu');
      document.body.style.overflow = 'hidden';
    };

    const closeMenu = () => {
      mobileToggle.classList.remove('active');
      navLinks.classList.remove('active');
      navControls?.classList.remove('active');
      mobileToggle.setAttribute('aria-expanded', 'false');
      mobileToggle.setAttribute('aria-label', 'Ouvrir le menu');
      document.body.style.overflow = '';
    };

    mobileToggle.addEventListener('click', () => {
      const isOpen = mobileToggle.classList.contains('active');
      isOpen ? closeMenu() : openMenu();
    });

    // Ferme au clic sur un lien
    $$('.nav-link').forEach(link => {
      link.addEventListener('click', closeMenu);
    });

    // Clic à l’extérieur
    document.addEventListener('click', (e) => {
      if (!mobileToggle.contains(e.target) && !navLinks.contains(e.target)) {
        closeMenu();
      }
    });

    // ESC pour fermer
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* -----------------------
     Scroll spy (IntersectionObserver)
  ----------------------- */
  function initScrollSpy() {
    const sections = $$('section[id]');
    const allLinks = $$('.nav-link');
    if (!sections.length || !allLinks.length) return;

    const io = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        const id = entry.target.id;
        const link = $(`.nav-link[href="#${id}"]`);
        if (!link) continue;

        if (entry.isIntersecting) {
          allLinks.forEach(l => {
            l.classList.remove('active');
            l.removeAttribute('aria-current');
          });
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
        }
      }
    }, {
      threshold: 0.5
    });

    sections.forEach(s => io.observe(s));
  }

  /* -----------------------
     Smooth scroll avec offset header
  ----------------------- */
  function initSmoothScroll() {
    const header = $('header');
    const headerOffset = () => header ? header.offsetHeight : 0;

    $$('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        const href = anchor.getAttribute('href');
        if (!href || href === '#') return;

        const target = $(href);
        if (!target) return;

        e.preventDefault();
        const y = target.getBoundingClientRect().top + window.pageYOffset - headerOffset() - 8;

        window.scrollTo({ top: y, behavior: 'smooth' });
      }, { passive: false });
    });
  }

  /* -----------------------
     Reveal au scroll (discret)
  ----------------------- */
  function initReveal() {
    const els = $$('.reveal-up');
    if (!('IntersectionObserver' in window) || !els.length) return;

    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      }
    }, { threshold: 0.12 });

    els.forEach(el => io.observe(el));
  }

  /* -----------------------
     Filtres projets
  ----------------------- */
  function initProjectFilters() {
    const buttons = $$('.filter-btn');
    const cards = $$('#projects-grid .project-item');
    if (!buttons.length || !cards.length) return;

    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.dataset.filter;
        cards.forEach(card => {
          const show = filter === 'all' || card.dataset.category === filter;
          card.style.display = show ? '' : 'none';
        });
        // Remise en contexte de la grille
        const grid = $('#projects-grid');
        if (grid) grid.style.display = 'grid';
      });
    });
  }

  /* -----------------------
     Contact: validation instantanée
  ----------------------- */
  function initContactValidation() {
    const form = $('form[data-contact]');
    if (!form) return;
    const inputs = form.querySelectorAll('input[required], textarea[required]');

    inputs.forEach(el => {
      el.addEventListener('input', () => {
        el.setCustomValidity('');
        if (!el.checkValidity()) {
          el.classList.add('is-invalid');
        } else {
          el.classList.remove('is-invalid');
        }
      });
    });
  }

  /* -----------------------
     AOS (optionnel)
  ----------------------- */
  function initAOS() {
    if (window.AOS) {
      window.AOS.init({ duration: 1000, once: true, offset: 100 });
    }
  }

  /* -----------------------
     Formulaire de contact AJAX
  ----------------------- */
  function initContactForm() {
    const form = $('#contactForm');
    const messageDiv = $('#contactMessage');
    
    if (!form) return;

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      
      // Désactiver le bouton pendant l'envoi
      submitBtn.disabled = true;
      submitBtn.textContent = 'Envoi...';
      
      try {
        const formData = new FormData(form);
        
        const response = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });
        
        if (response.ok) {
          // Réinitialiser le formulaire avant de le masquer
          form.reset();
          
          // Masquer le formulaire et afficher le message
          form.style.display = 'none';
          messageDiv.style.display = 'block';
          messageDiv.classList.remove('fade-out');
          
          // Masquer le message et réafficher le formulaire après 30 secondes
          setTimeout(() => {
            messageDiv.classList.add('fade-out');
            setTimeout(() => {
              messageDiv.style.display = 'none';
              messageDiv.classList.remove('fade-out');
              form.style.display = 'flex'; // Réafficher le formulaire
            }, 500);
          }, 30000);
          
        } else {
          throw new Error('Erreur lors de l\'envoi');
        }
        
      } catch (error) {
        alert('Erreur lors de l\'envoi du message. Veuillez réessayer.');
        console.error('Erreur:', error);
      }
      
      // Réactiver le bouton
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    });
  }

  /* -----------------------
     INIT
  ----------------------- */
  document.addEventListener('DOMContentLoaded', () => {
    fadeOutLoader();

    initThemeToggle();

    initI18n();
    initMobileMenu();
    initScrollSpy();
    initSmoothScroll();
    initReveal();
    initProjectFilters();
    initContactValidation();
    initContactForm();
    initAOS();
  });

})();
