gsap.registerPlugin(ScrollTrigger);

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- Header ---------- */
const header = document.getElementById("site-header");
ScrollTrigger.create({
  start: 80,
  onEnter: () => header.classList.add("scrolled"),
  onLeaveBack: () => header.classList.remove("scrolled")
});

/* ---------- Menu mobile ---------- */
const burger = document.getElementById("burger");
const mobileMenu = document.getElementById("mobile-menu");
function toggleMenu(force){
  const open = force !== undefined ? force : !mobileMenu.classList.contains("open");
  mobileMenu.classList.toggle("open", open);
  burger.classList.toggle("open", open);
  burger.setAttribute("aria-expanded", open);
  mobileMenu.setAttribute("aria-hidden", !open);
  document.body.style.overflow = open ? "hidden" : "";
}
burger.addEventListener("click", () => toggleMenu());
mobileMenu.querySelectorAll("a").forEach(a => a.addEventListener("click", () => toggleMenu(false)));

/* ---------- Formulaire (démo) ---------- */
document.getElementById("contact-form").addEventListener("submit", e => {
  e.preventDefault();
  const form = e.target;
  if (!form.checkValidity()) { form.reportValidity(); return; }
  document.getElementById("form-success").classList.add("visible");
  form.querySelector("button[type=submit]").disabled = true;
});

/* ---------- Animations ---------- */
if (reduceMotion) {
  // Tout visible immédiatement, pas d'animations.
  document.getElementById("loader").style.display = "none";
  gsap.set(".reveal", { opacity: 1, y: 0 });
  document.querySelector(".timeline .progress").style.transform = "scaleY(1)";
} else {
  /* Loader + intro hero */
  const intro = gsap.timeline();
  intro
    .to("#loader .loader-line i", { scaleX: 1, duration: .9, ease: "power2.inOut" })
    .to("#loader", { autoAlpha: 0, duration: .6, ease: "power2.out" }, "+=.15")
    .set("#loader", { display: "none" })
    .from("#hero h1 .line > span", {
      yPercent: 110, duration: 1.1, ease: "power4.out", stagger: .12
    }, "-=.35")
    .from(".hero-kicker, .hero-sub, .hero-ctas, .hero-meta", {
      opacity: 0, y: 24, duration: .8, ease: "power2.out", stagger: .1
    }, "-=.6")
    .from(".scroll-cue", { opacity: 0, duration: .8 }, "-=.3");

  /* Reveal générique au scroll */
  ScrollTrigger.batch(".reveal", {
    start: "top 86%",
    once: true,
    onEnter: els => gsap.to(els, {
      opacity: 1, y: 0, duration: .9, ease: "power3.out", stagger: .09, overwrite: true
    })
  });

  /* Compteurs */
  document.querySelectorAll(".counter").forEach(el => {
    const target = +el.dataset.target;
    ScrollTrigger.create({
      trigger: el, start: "top 88%", once: true,
      onEnter: () => gsap.to(el, {
        innerText: target, duration: 1.8, ease: "power2.out", snap: { innerText: 1 }
      })
    });
  });

  /* Parallaxe portrait */
  gsap.to("#portrait-img", {
    yPercent: -14, ease: "none",
    scrollTrigger: { trigger: ".portrait-frame", start: "top bottom", end: "bottom top", scrub: 1 }
  });

  /* Watermark hero — dérive douce */
  gsap.to("#hero .watermark", {
    yPercent: 18, ease: "none",
    scrollTrigger: { trigger: "#hero", start: "top top", end: "bottom top", scrub: 1 }
  });

  /* Ligne de progression de la timeline */
  gsap.to(".timeline .progress", {
    scaleY: 1, ease: "none",
    scrollTrigger: { trigger: ".timeline", start: "top 75%", end: "bottom 60%", scrub: .6 }
  });
}
