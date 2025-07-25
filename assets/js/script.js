// Variables globales
let currentLang = localStorage.getItem('lang') || 'fr';
let isDarkMode = localStorage.getItem('darkMode') === 'true';

document.addEventListener('DOMContentLoaded', () => {

  // Loader fade out
  setTimeout(() => {
    const loader = document.getElementById('loader');
    loader.style.opacity = '0';
    setTimeout(() => loader.style.display = 'none', 500);
  }, 1000);

  // Mode sombre
  if (isDarkMode) document.body.classList.add('dark-mode');

  // Langue par défaut ou sauvegardée
  const langSwitcher = document.getElementById('langSwitcher');
  if (langSwitcher) {
    langSwitcher.value = currentLang; 
    changeLanguage(currentLang);      

    langSwitcher.addEventListener('change', (e) => {
      const selectedLang = e.target.value;
      localStorage.setItem('lang', selectedLang); 
      changeLanguage(selectedLang);
    });
  } else {
    changeLanguage(currentLang);
  }

  // AOS animations
  if (window.AOS) {
    AOS.init({ duration: 1000, once: true, offset: 100 });
  }

  // Ecouteurs généraux
  initEventListeners();

  // Menu mobile
  initMobileMenu();

  // Scroll Spy modern
  initScrollSpy();

  // Smooth scroll interne
  initSmoothScroll();

});

// Changer la langue dynamiquement

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
    currentLang = lang;

  } catch (error) {
    console.error('[JSON ERROR]', error);
  } finally {
    setTimeout(() => main.style.opacity = 1, 200);
  }
}

// Toggle Dark Mode

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

// Menu Mobile

function initMobileMenu() {
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  const navControls = document.querySelector('.nav-controls');
  const navLinkItems = document.querySelectorAll('.nav-link');

  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', () => {
      mobileToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
      navControls.classList.toggle('active');
      
      // Empêche le scroll du body quand le menu est ouvert
      document.body.style.overflow = mobileToggle.classList.contains('active') ? 'hidden' : '';
    });

    // Ferme le menu quand on clique sur un lien
    navLinkItems.forEach(link => {
      link.addEventListener('click', () => {
        mobileToggle.classList.remove('active');
        navLinks.classList.remove('active');
        navControls.classList.remove('active');
        document.body.style.overflow = '';
      });
    });

    // Ferme le menu si on clique en dehors
    document.addEventListener('click', (e) => {
      if (!mobileToggle.contains(e.target) && !navLinks.contains(e.target)) {
        mobileToggle.classList.remove('active');
        navLinks.classList.remove('active');
        navControls.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }
}

// Scroll Spy (Intersection Observer)

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

// Smooth scroll interne

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
