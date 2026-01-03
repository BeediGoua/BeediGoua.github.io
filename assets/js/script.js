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
     Nouveau Menu Mobile Moderne
  ----------------------- */
  function initNewMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const menuOverlay = document.querySelector('.mobile-menu-overlay');
    const navLinks = document.querySelectorAll('.mobile-menu-nav .nav-link');
    
    if (!menuBtn || !menuOverlay) return;

    // Ouvrir/fermer le menu
    const toggleMenu = () => {
      const isOpen = menuBtn.classList.contains('active');
      
      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
    };

    const openMenu = () => {
      menuBtn.classList.add('active');
      menuOverlay.classList.add('active');
      menuBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden'; // Bloquer le scroll
    };

    const closeMenu = () => {
      menuBtn.classList.remove('active');
      menuOverlay.classList.remove('active');
      menuBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = ''; // Rétablir le scroll
    };

    // Event listeners
    menuBtn.addEventListener('click', toggleMenu);
    
    // Fermer le menu en cliquant sur un lien
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        closeMenu();
      });
    });

    // Fermer le menu en cliquant en dehors (sur l'overlay)
    menuOverlay.addEventListener('click', (e) => {
      if (e.target === menuOverlay) {
        closeMenu();
      }
    });

    // Fermer avec la touche Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && menuOverlay.classList.contains('active')) {
        closeMenu();
      }
    });

    // Gestion des contrôles dans le menu mobile
    const langSwitcherMobile2 = document.getElementById('langSwitcherMobile2');
    const themeToggleMobile2 = document.getElementById('themeToggleMobile2');

    // Synchroniser le sélecteur de langue mobile avec le desktop
    if (langSwitcherMobile2) {
      langSwitcherMobile2.addEventListener('change', (e) => {
        changeLanguage(e.target.value);
      });
    }

    // Gestion du bouton thème mobile
    if (themeToggleMobile2) {
      themeToggleMobile2.addEventListener('click', () => {
        const next = document.body.classList.contains('light-theme') ? 'dark' : 'light';
        applyTheme(next);
      });
    }

    // Synchroniser les valeurs initiales
    const currentLang = localStorage.getItem('lang') || 'fr';
    if (langSwitcherMobile2) {
      langSwitcherMobile2.value = currentLang;
    }
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
          const categories = card.dataset.category.split(' ');
          const show = filter === 'all' || categories.includes(filter);
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
    initNewMobileMenu();
    initScrollSpy();
    initSmoothScroll();
    initReveal();
    initProjectFilters();
    initContactValidation();
    initContactForm();
    initAOS();
  });

})();
