// ---------------------------
// assets/js/script.js
// ---------------------------

// ✅ Variables globales
let currentLang = localStorage.getItem('lang') || 'fr';
let isDarkMode = localStorage.getItem('darkMode') === 'true';

document.addEventListener('DOMContentLoaded', () => {

  // ✅ 1) Loader fade out
  setTimeout(() => {
    const loader = document.getElementById('loader');
    loader.style.opacity = '0';
    setTimeout(() => loader.style.display = 'none', 500);
  }, 1000);

  // ✅ 2) Mode sombre
  if (isDarkMode) document.body.classList.add('dark-mode');

  // ✅ 3) Langue par défaut
  changeLanguage(currentLang);

  // ✅ 4) AOS animations
  if (window.AOS) {
    AOS.init({ duration: 1000, once: true, offset: 100 });
  }

  // ✅ 5) Ecouteurs
  initEventListeners();

  // ✅ 6) Scroll Spy modern
  initScrollSpy();

  // ✅ 7) Smooth scroll interne
  initSmoothScroll();

});

// ---------------------------
// 📌 Changer la langue
// ---------------------------
async function changeLanguage(lang) {
  const main = document.querySelector('main');
  main.style.opacity = 0;

  try {
    const response = await fetch(`assets/lang/${lang}.json`);
    const translations = await response.json();

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (translations[key]) el.textContent = translations[key];
    });

    document.documentElement.lang = lang;
    localStorage.setItem('lang', lang);
    currentLang = lang;

  } catch (error) {
    console.error('[JSON ERROR]', error);
  } finally {
    setTimeout(() => main.style.opacity = 1, 200);
  }
}

// ---------------------------
// 🌙 Toggle Dark Mode
// ---------------------------
function initEventListeners() {
  const darkModeBtn = document.getElementById('darkModeToggle');
  if (darkModeBtn) {
    darkModeBtn.addEventListener('click', () => {
      isDarkMode = !isDarkMode;
      document.body.classList.toggle('dark-mode');
      localStorage.setItem('darkMode', isDarkMode);
    });
  }
}

// ---------------------------
// 🧭 Scroll Spy (Intersection Observer)
// ---------------------------
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const id = entry.target.id;
      const link = document.querySelector(`.nav-link[href="#${id}"]`);
      if (entry.isIntersecting) {
        navLinks.forEach(l => l.classList.remove('active'));
        if (link) link.classList.add('active');
      }
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));
}

// ---------------------------
// 📌 Smooth scroll interne
// ---------------------------
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 60,
          behavior: 'smooth'
        });
      }
    });
  });
}
