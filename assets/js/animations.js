// ✅ assets/js/animations.js — Version Finale PRO Compatible

// ========== PARTICLES HERO ==========
function createFloatingParticles() {
  const heroSection = document.querySelector('.hero'); // CORRIGÉ ! Doit matcher ta <section class="hero">
  if (!heroSection) return;

  const particlesContainer = document.createElement('div');
  particlesContainer.className = 'particles-container';
  heroSection.appendChild(particlesContainer);

  for (let i = 0; i < 50; i++) {
    createParticle(particlesContainer);
  }
}

function createParticle(container) {
  const particle = document.createElement('div');
  particle.className = 'particle';

  const size = Math.random() * 4 + 2;
  const x = Math.random() * window.innerWidth;
  const y = Math.random() * window.innerHeight;
  const speedX = (Math.random() - 0.5) * 0.5;
  const speedY = (Math.random() - 0.5) * 0.5;

  particle.style.cssText = `
    position: absolute;
    width: ${size}px;
    height: ${size}px;
    background: rgba(14, 165, 233, 0.3);
    border-radius: 50%;
    left: ${x}px;
    top: ${y}px;
    pointer-events: none;
  `;

  container.appendChild(particle);

  function animate() {
    let newX = x + speedX * Date.now() * 0.001;
    let newY = y + speedY * Date.now() * 0.001;
    particle.style.transform = `translate(${newX - x}px, ${newY - y}px)`;
    requestAnimationFrame(animate);
  }

  animate();
}

// ========== SCROLL SPY ==========
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const id = entry.target.getAttribute('id');
      const link = document.querySelector(`.nav-link[href="#${id}"]`);
      if (entry.isIntersecting) {
        navLinks.forEach(l => l.classList.remove('active'));
        if (link) link.classList.add('active');
      }
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));
}

// ========== PARALLAX HERO BG ==========
function initHeroParallax() {
  const heroBg = document.querySelector('.hero'); // CORRIGÉ !
  if (!heroBg) return;

  window.addEventListener('scroll', () => {
    const offset = window.pageYOffset;
    heroBg.style.backgroundPositionY = `${offset * 0.5}px`;
  });
}

// ========== SKILLS BAR ANIMATION ==========
function animateSkillBars() {
  const skills = document.querySelectorAll('.progress-bar');
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const width = bar.getAttribute('data-width');
        bar.style.width = width;
        observer.unobserve(bar);
      }
    });
  }, { threshold: 0.7 });

  skills.forEach(bar => {
    observer.observe(bar);
  });
}

// ========== HERO TYPING EFFECT ==========
function initTypingEffect() {
  const el = document.querySelector('.typed-text');
  if (!el) return;
  const roles = [
    "Data Scientist",
    "NLP Engineer",
    "RAG Specialist",
    "LLM Enthusiast"
  ];
  let i = 0, j = 0, isDeleting = false, txt = '';

  function type() {
    const current = roles[i % roles.length];
    if (isDeleting) {
      txt = current.substring(0, txt.length - 1);
    } else {
      txt = current.substring(0, txt.length + 1);
    }
    el.textContent = txt;
    let speed = isDeleting ? 60 : 120;
    if (!isDeleting && txt === current) {
      speed = 1200;
      isDeleting = true;
    } else if (isDeleting && txt === '') {
      isDeleting = false;
      i++;
      speed = 400;
    }
    setTimeout(type, speed);
  }
  type();
}

// ========== INIT GLOBAL ==========
document.addEventListener('DOMContentLoaded', () => {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReduced) {
    createFloatingParticles();
    initHeroParallax();
    initScrollSpy();
  }

  if (typeof animateCounters === 'function') animateCounters();
  if (typeof initTextRevealAnimation === 'function') initTextRevealAnimation();
  if (typeof initParallaxEffect === 'function') initParallaxEffect();
  if (typeof initShapeMorphing === 'function') initShapeMorphing();
  if (typeof initGlitchEffect === 'function') initGlitchEffect();
  if (typeof initCustomCursor === 'function') initCustomCursor();
  if (typeof initWaveAnimation === 'function') initWaveAnimation();
  if (typeof initCircularProgress === 'function') initCircularProgress();
  animateSkillBars();
  initTypingEffect();
});

// ✅ Export propre si besoin pour débogage
window.portfolioAnimations = {
  createFloatingParticles,
  initHeroParallax,
  initScrollSpy,
  animateCounters,
  initTextRevealAnimation,
  initParallaxEffect,
  initShapeMorphing,
  initGlitchEffect,
  initCustomCursor,
  initWaveAnimation,
  initCircularProgress
};

