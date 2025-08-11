/* =========================================================
   PORTFOLIO — ANIMATIONS (Hero & UI light)
   - Typing effect (multilingue, piloté par i18n)
   - Particules flottantes (légères, respect reduced-motion)
   - Parallax discret du Hero (désactivé mobile/reduced-motion)
   - Progress bars (IntersectionObserver)
   - Aucune duplication du scroll-spy (laissé à script.js)
========================================================= */

(() => {
  'use strict';

  // ------- Helpers -------
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => r.querySelectorAll(s);
  const prefersReduced = () => window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isMobile = () => window.matchMedia && window.matchMedia('(max-width: 768px)').matches;

  // ------- State interne (pour clean-up idempotent) -------
  const state = {
    typing: { timer: null },
    particles: { raf: null, container: null, items: [] },
    parallax: { raf: null, enabled: false },
    skillBars: { io: null }
  };

  /* =======================================================
     1) TYPING EFFECT (multilingue)
     - Appelée par script.js après chargement i18n :
       window.portfolioAnimations.initTypingEffect(translations.hero_roles || ["Data Scientist"])
  ======================================================= */
  function initTypingEffect(roles) {
    const el = $('.typed-text');
    if (!el || !roles || !roles.length) return;

    // stop précédent si relancé par un changement de langue
    if (state.typing.timer) {
      clearTimeout(state.typing.timer);
      state.typing.timer = null;
    }

    let i = 0, txt = '', del = false;

    (function type() {
      const cur = roles[i % roles.length];
      txt = del ? cur.substring(0, txt.length - 1) : cur.substring(0, txt.length + 1);
      el.textContent = txt;

      let speed = del ? 60 : 120;
      if (!del && txt === cur) { del = true; speed = 900; }
      else if (del && !txt)   { del = false; i++; speed = 400; }

      state.typing.timer = setTimeout(type, speed);
    })();
  }

  function destroyTypingEffect() {
    if (state.typing.timer) {
      clearTimeout(state.typing.timer);
      state.typing.timer = null;
    }
  }

  /* =======================================================
     2) PARTICULES FLOTTANTES (héros)
     - très légères : ~16–40 particules selon viewport
     - rAF unique + deltaTime
     - clean-up complet via stopParticles()
  ======================================================= */
  function startParticles() {
    if (prefersReduced()) return;              // respect user
    const hero = $('.hero');
    if (!hero || state.particles.raf) return;  // déjà en cours

    const container = document.createElement('div');
    container.className = 'particles-container';
    Object.assign(container.style, {
      position: 'absolute',
      inset: 0,
      overflow: 'hidden',
      pointerEvents: 'none',
      zIndex: 0
    });
    hero.appendChild(container);
    state.particles.container = container;

    const count = isMobile() ? 16 : (window.innerWidth < 1100 ? 28 : 40);
    const items = [];
    const rnd = (min, max) => Math.random() * (max - min) + min;

    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      const size = rnd(2, 5);
      Object.assign(p.style, {
        position: 'absolute',
        width: `${size}px`,
        height: `${size}px`,
        left: `${rnd(0, container.clientWidth)}px`,
        top: `${rnd(0, container.clientHeight)}px`,
        background: 'rgba(74, 144, 226, 0.28)',
        borderRadius: '50%',
        transform: 'translate3d(0,0,0)'
      });
      container.appendChild(p);

      items.push({
        el: p,
        x: parseFloat(p.style.left),
        y: parseFloat(p.style.top),
        vx: rnd(-0.06, 0.06),
        vy: rnd(-0.06, 0.06)
      });
    }
    state.particles.items = items;

    let last = performance.now();
    const loop = (now) => {
      const dt = Math.min(64, now - last); // clamp dt pour stabilité
      last = now;

      const w = container.clientWidth;
      const h = container.clientHeight;

      for (const it of items) {
        it.x += it.vx * dt;
        it.y += it.vy * dt;

        // wrap edges
        if (it.x < -10) it.x = w + 10;
        if (it.x > w + 10) it.x = -10;
        if (it.y < -10) it.y = h + 10;
        if (it.y > h + 10) it.y = -10;

        it.el.style.transform = `translate3d(${Math.round(it.x)}px, ${Math.round(it.y)}px, 0)`;
      }

      state.particles.raf = requestAnimationFrame(loop);
    };
    state.particles.raf = requestAnimationFrame(loop);

    // Recalcule sur resize (léger)
    const onResize = () => {
      // on ne recalcule que le conteneur; les particules se wrappent d'elles-mêmes
      // (pas besoin de tout re-créer)
    };
    window.addEventListener('resize', onResize, { passive: true });
    state.particles._onResize = onResize;
  }

  function stopParticles() {
    if (state.particles.raf) {
      cancelAnimationFrame(state.particles.raf);
      state.particles.raf = null;
    }
    if (state.particles._onResize) {
      window.removeEventListener('resize', state.particles._onResize);
      state.particles._onResize = null;
    }
    if (state.particles.container) {
      state.particles.container.remove();
      state.particles.container = null;
    }
    state.particles.items = [];
  }

  /* =======================================================
     3) PARALLAX (discret)
     - évite les set scroll trop fréquents via rAF
     - désactivé sur mobile & reduced-motion
  ======================================================= */
  function startHeroParallax() {
    if (prefersReduced() || isMobile() || state.parallax.raf) return;
    const hero = $('.hero');
    if (!hero) return;

    state.parallax.enabled = true;
    let ticking = false;

    const update = () => {
      if (!state.parallax.enabled) return;
      const y = window.pageYOffset * 0.2; // intensité douce
      // background-position déclenche un repaint, mais la surface est limitée à .hero
      hero.style.backgroundPosition = `center calc(50% + ${y}px)`;
      state.parallax.raf = requestAnimationFrame(() => { ticking = false; });
    };

    const onScroll = () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    state.parallax._onScroll = onScroll;
  }

  function stopHeroParallax() {
    state.parallax.enabled = false;
    if (state.parallax.raf) {
      cancelAnimationFrame(state.parallax.raf);
      state.parallax.raf = null;
    }
    if (state.parallax._onScroll) {
      window.removeEventListener('scroll', state.parallax._onScroll);
      state.parallax._onScroll = null;
    }
  }

  /* =======================================================
     4) SKILL BARS
     - Remplit la largeur à l’entrée en viewport
  ======================================================= */
  function animateSkillBars() {
    const bars = $$('.progress-bar');
    if (!bars.length) return;

    // Reset safe (si revisit)
    bars.forEach(b => { b.style.width = '0px'; });

    const io = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        const bar = entry.target;
        const target = bar.getAttribute('data-width') || bar.dataset.width || '100%';
        // micro delay pour laisser la transition s'appliquer
        requestAnimationFrame(() => { bar.style.width = target; });
        io.unobserve(bar);
      }
    }, { threshold: 0.6 });

    bars.forEach(b => io.observe(b));
    state.skillBars.io = io;
  }

  function stopSkillBars() {
    if (state.skillBars.io) {
      state.skillBars.io.disconnect();
      state.skillBars.io = null;
    }
  }

  /* =======================================================
     5) API "reduceMotion"
     - utile si tu veux couper des effets sur mobile via script.js
  ======================================================= */
  function reduceMotion() {
    stopParticles();
    stopHeroParallax();
    // le typing reste (léger). Si besoin: destroyTypingEffect();
  }

  /* =======================================================
     INIT au chargement
  ======================================================= */
  document.addEventListener('DOMContentLoaded', () => {
    // Particules & parallax seulement si non réduit
    if (!prefersReduced()) {
      startParticles();
      startHeroParallax();
    }
    animateSkillBars();

    // Typing par défaut si script.js ne l'appelle pas (fallback)
    if (!$('.typed-text')) return;
    if (!(window.__i18n && Array.isArray(window.__i18n.hero_roles))) {
      initTypingEffect(["Data Scientist"]);
    }
  });

  /* =======================================================
     Expose propre pour script.js (i18n, toggles, etc.)
  ======================================================= */
  window.portfolioAnimations = Object.assign({}, window.portfolioAnimations, {
    initTypingEffect,
    destroyTypingEffect,
    startParticles,
    stopParticles,
    startHeroParallax,
    stopHeroParallax,
    animateSkillBars,
    stopSkillBars,
    reduceMotion
  });

})();
