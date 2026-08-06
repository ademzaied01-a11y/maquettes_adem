// ---------- Menu mobile ----------
const toggle = document.querySelector('.nav-toggle');
const navList = document.getElementById('nav-list');

if (toggle && navList) {
  toggle.addEventListener('click', () => {
    const open = navList.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  });

  // Ferme le menu après un clic sur un lien (mobile)
  navList.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navList.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// ---------- Reveal au scroll (motion porteuse de sens, cf. DESIGN.md §6) ----------
const reveals = document.querySelectorAll('[data-reveal]');
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReduced || !('IntersectionObserver' in window)) {
  // Reduced motion ou navigateur ancien : contenu visible immédiatement
  reveals.forEach((el) => el.classList.add('is-visible'));
} else {
  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // léger stagger pour les groupes proches
          entry.target.style.transitionDelay = Math.min(i * 60, 180) + 'ms';
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -8% 0px' }
  );
  reveals.forEach((el) => observer.observe(el));
}

// ---------- Année dynamique ----------
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();
