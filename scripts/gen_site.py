# -*- coding: utf-8 -*-
"""Générateur de maquettes avocats à partir du template Valmont.

Usage : python scripts/gen_site.py
Génère un dossier par avocat (index.html + css palette adaptée + js copié),
en appliquant les règles de contenu : informations publiques vérifiables
uniquement, noindex, mention maquette en pied de page.
"""
import shutil, sys, io
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "template"

def esc_url(hexcolor):
    return hexcolor.replace("#", "%23")

def gen_css(dst, ink, ink2, ink3, radial):
    css = (TPL / "css" / "styles.css").read_text(encoding="utf-8")
    css = css.replace("#0B1220", ink).replace("#101A2E", ink2).replace("#16213A", ink3)
    r, g, b = int(ink[1:3], 16), int(ink[3:5], 16), int(ink[5:7], 16)
    css = css.replace("rgba(11,18,32,", f"rgba({r},{g},{b},")
    css = css.replace("rgba(30,58,138,.18)", radial)
    css = css.replace("minmax(min(24rem,100%),1fr)", "minmax(min(17rem,100%),1fr)")
    (dst / "css").mkdir(parents=True, exist_ok=True)
    (dst / "css" / "styles.css").write_text(css, encoding="utf-8")

HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>@@TITLE@@</title>
<meta name="description" content="Maquette de démonstration — @@DESC@@">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Lato:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='@@INKENC@@'/%3E%3Ctext x='32' y='@@FAVY@@' font-family='Georgia' font-size='@@FAVSIZE@@' fill='%23C0A062' text-anchor='middle'%3E@@MONO@@%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>

<div id="loader" aria-hidden="true">
  <div class="monogram">@@MONO@@</div>
  <div class="loader-line"><i></i></div>
</div>

<header id="site-header">
  <div class="container header-inner">
    <a class="brand" href="#hero" aria-label="@@BRAND@@ — retour à l'accueil">
      <span class="mark">@@MONO@@</span>
      <span class="name">@@BRAND@@<small>@@BRAND_SUB@@</small></span>
    </a>
    <nav class="desktop" aria-label="Navigation principale">
      <a href="#apropos">Le cabinet</a>
      <a href="#expertises">Expertises</a>
      <a href="#parcours">Parcours</a>
      <a href="#formation">Formation</a>
      <a href="#infos">Informations</a>
    </nav>
    <a class="btn" href="#contact">Prendre rendez-vous</a>
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div id="mobile-menu" aria-hidden="true">
  <a href="#apropos">Le cabinet</a>
  <a href="#expertises">Expertises</a>
  <a href="#parcours">Parcours</a>
  <a href="#formation">Formation</a>
  <a href="#infos">Informations</a>
  <a href="#contact">Contact</a>
</div>

<main>

<section id="hero">
  <div class="watermark" aria-hidden="true">@@WATERMARK@@</div>
  <div class="container hero-inner">
    <p class="hero-kicker">@@KICKER@@</p>
    <h1>
      <span class="line"><span>@@H1A@@</span></span>
      <span class="line"><span>@@H1B@@</span></span>
    </h1>
    <p class="hero-sub">@@HERO_SUB@@</p>
    <div class="hero-ctas">
      <a class="btn solid" href="#contact">Prendre contact</a>
      <a class="btn" href="#expertises">Découvrir les expertises</a>
    </div>
    <div class="hero-meta">
@@META@@
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">Défiler<i></i></div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
@@MARQUEE@@
  </div>
</div>

<section id="stats" aria-label="Chiffres clés">
  <div class="container stats-grid">
@@STATS@@
  </div>
</section>

<section id="apropos">
  <div class="container about-grid">
    <div class="portrait-frame reveal">
      <div class="portrait">
        <img id="portrait-img" src="@@IMG@@" alt="@@IMG_ALT@@" width="900" height="1125" loading="lazy">
        <div class="credit"><b>@@CREDIT_B@@</b>@@CREDIT_S@@</div>
      </div>
    </div>
    <div class="about-copy">
      <p class="eyebrow reveal">Le cabinet</p>
      <h2 class="section-title reveal">@@ABOUT_TITLE@@</h2>
      <p class="lead reveal">@@LEAD@@</p>
      <p class="reveal">@@P1@@</p>
      <p class="reveal">@@P2@@</p>
      <div class="about-signature reveal">
        <span class="sig">@@SIG@@</span>
        <small>@@SIG_SUB@@</small>
      </div>
    </div>
  </div>
</section>

<section id="expertises">
  <div class="container">
    <div class="expertise-head">
      <div>
        <p class="eyebrow reveal">Domaines d'intervention</p>
        <h2 class="section-title reveal">@@EXP_TITLE@@</h2>
      </div>
      <p class="reveal">@@EXP_INTRO@@</p>
    </div>
    <div class="expertise-list">
@@EXPS@@
    </div>
  </div>
</section>

<section id="parcours">
  <div class="container">
    <p class="eyebrow reveal">Parcours</p>
    <h2 class="section-title reveal">@@PARC_TITLE@@</h2>
    <div class="timeline">
      <div class="progress" aria-hidden="true"></div>
@@TIMELINE@@
    </div>
  </div>
</section>

<section id="formation">
  <div class="container">
    <p class="eyebrow reveal">@@FORM_EYEBROW@@</p>
    <h2 class="section-title reveal">@@FORM_TITLE@@</h2>
    <div class="diplomas">
@@DIPS@@
    </div>
  </div>
</section>

<section id="infos">
  <div class="container">
    <p class="eyebrow reveal">Informations pratiques</p>
    <h2 class="section-title reveal">@@INFOS_TITLE@@</h2>
    <div class="testi-grid">
@@INFOS@@
    </div>
  </div>
</section>

<section id="contact">
  <div class="container">
    <p class="eyebrow reveal">Contact</p>
    <h2 class="section-title reveal">Engageons la <em>conversation</em></h2>
    <div class="contact-grid">
      <div class="contact-info">
@@CONTACT_BLOCKS@@
      </div>
      <form class="contact-form reveal" id="contact-form" novalidate>
        <div class="field-row">
          <div class="field">
            <label for="f-nom">Nom complet <span class="req">*</span></label>
            <input id="f-nom" name="nom" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="f-email">Adresse e-mail <span class="req">*</span></label>
            <input id="f-email" name="email" type="email" autocomplete="email" required>
          </div>
        </div>
        <div class="field">
          <label for="f-objet">Objet de la consultation</label>
          <select id="f-objet" name="objet">
            <option value="">— Sélectionner —</option>
@@OPTS@@
          </select>
        </div>
        <div class="field">
          <label for="f-message">Votre message <span class="req">*</span></label>
          <textarea id="f-message" name="message" required placeholder="Décrivez brièvement votre situation…"></textarea>
        </div>
        <p class="form-note">Les informations transmises via ce formulaire sont couvertes par le secret professionnel.</p>
        <button class="btn" type="submit">Envoyer la demande</button>
        <div class="form-success" id="form-success" role="status">
          Merci — votre demande a bien été transmise. Le cabinet reviendra vers vous dans les meilleurs délais.
        </div>
      </form>
    </div>
  </div>
</section>

</main>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="name">@@FOOTER_NAME@@</div>
        <small>@@FOOTER_SUB@@</small>
      </div>
      <div class="footer-links">
        <ul>
          <li class="head">Navigation</li>
          <li><a href="#apropos">Le cabinet</a></li>
          <li><a href="#expertises">Expertises</a></li>
          <li><a href="#parcours">Parcours</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
        <ul>
          <li class="head">Informations</li>
          <li><a href="#">Mentions légales</a></li>
          <li><a href="#">Politique de confidentialité</a></li>
          <li><a href="#infos">Honoraires</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 — Tous droits réservés</span>
      <span class="demo">Maquette de démonstration non officielle, réalisée à partir d'informations publiques (@@SOURCES@@). Ce site n'est pas affilié à @@ME@@.</span>
    </div>
  </div>
</footer>

<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script src="js/main.js"></script>
</body>
</html>
"""

def build(site):
    dst = ROOT / site["slug"]
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir()
    gen_css(dst, site["ink"], site["ink2"], site["ink3"], site["radial"])
    (dst / "js").mkdir()
    shutil.copy(TPL / "js" / "main.js", dst / "js" / "main.js")

    h = HTML
    mono = site["mono"]
    favsize = "36" if len(mono) == 1 else "26"
    favy = "44" if len(mono) == 1 else "42"

    meta = "\n".join(f'      <span><b>{b}</b> — {r}</span>' for b, r in site["meta"])
    marq = "\n".join(f'    <span>{m}</span>' for m in site["marquee"] * 2)
    stats = []
    for st in site["stats"]:
        sup = f'<sup>{st["sup"]}</sup>' if st.get("sup") else ""
        if st.get("counter", True):
            num = f'<span class="counter" data-target="{st["n"]}">0</span>{sup}'
        else:
            num = f'{st["n"]}{sup}'
        stats.append(f'    <div class="stat reveal"><div class="num">{num}</div>'
                     f'<div class="label">{st["label"]}</div></div>')
    stats = "\n".join(stats)
    exps = "\n".join(
        f'      <article class="expertise-item reveal">\n'
        f'        <span class="idx">{i:02d}</span>\n'
        f'        <div><h3>{t}</h3>\n        <p>{d}</p></div>\n'
        f'      </article>'
        for i, (t, d) in enumerate(site["exps"], 1))
    tl = "\n".join(
        f'      <div class="tl-item reveal">\n'
        f'        <span class="date">{d0}</span>\n'
        f'        <h3>{t}<span>{s}</span></h3>\n'
        f'        <p>{d}</p>\n      </div>'
        for d0, t, s, d in site["tl"])
    dips = "\n".join(
        f'      <div class="diploma reveal">\n'
        f'        <div class="year">{y}</div>\n'
        f'        <h3>{t}</h3>\n        <p>{d}</p>\n'
        f'        <div class="inst">{inst}</div>\n      </div>'
        for y, t, d, inst in site["dips"])
    infos = "\n".join(
        f'      <article class="testi reveal">\n'
        f'        <p>{p}</p>\n'
        f'        <div class="who"><b>{b}</b>{s}</div>\n      </article>'
        for p, b, s in site["infos"])
    blocks = "\n".join(
        f'        <div class="info-block reveal">\n'
        f'          <div class="label">{lab}</div>\n'
        f'          {main}\n'
        f'          <small>{sub}</small>\n        </div>'
        for lab, main, sub in site["contact_blocks"])
    opts = "\n".join(f'            <option>{o}</option>' for o in site["opts"])

    repl = {
        "@@TITLE@@": site["title"], "@@DESC@@": site["desc"],
        "@@INKENC@@": esc_url(site["ink"]), "@@MONO@@": mono,
        "@@FAVSIZE@@": favsize, "@@FAVY@@": favy,
        "@@BRAND@@": site["brand"], "@@BRAND_SUB@@": site["brand_sub"],
        "@@WATERMARK@@": site["watermark"], "@@KICKER@@": site["kicker"],
        "@@H1A@@": site["h1a"], "@@H1B@@": site["h1b"],
        "@@HERO_SUB@@": site["hero_sub"], "@@META@@": meta,
        "@@MARQUEE@@": marq, "@@STATS@@": stats,
        "@@IMG@@": site["img"], "@@IMG_ALT@@": site["img_alt"],
        "@@CREDIT_B@@": site["credit_b"], "@@CREDIT_S@@": site["credit_s"],
        "@@ABOUT_TITLE@@": site["about_title"], "@@LEAD@@": site["lead"],
        "@@P1@@": site["p1"], "@@P2@@": site["p2"],
        "@@SIG@@": site["sig"], "@@SIG_SUB@@": site["sig_sub"],
        "@@EXP_TITLE@@": site["exp_title"], "@@EXP_INTRO@@": site["exp_intro"],
        "@@EXPS@@": exps, "@@PARC_TITLE@@": site["parc_title"],
        "@@TIMELINE@@": tl, "@@FORM_EYEBROW@@": site.get("form_eyebrow", "Parcours académique"),
        "@@FORM_TITLE@@": site["form_title"], "@@DIPS@@": dips,
        "@@INFOS_TITLE@@": site["infos_title"], "@@INFOS@@": infos,
        "@@CONTACT_BLOCKS@@": blocks, "@@OPTS@@": opts,
        "@@FOOTER_NAME@@": site["footer_name"], "@@FOOTER_SUB@@": site["footer_sub"],
        "@@SOURCES@@": site["sources"], "@@ME@@": site["me"],
    }
    for k, v in repl.items():
        h = h.replace(k, v)
    (dst / "index.html").write_text(h, encoding="utf-8")
    print("OK", site["slug"])

if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "scripts"))
    from sites_data import SITES
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for s in SITES:
        if only and s["slug"] not in only:
            continue
        build(s)
