# DESIGN.md — Dr Pascal Clappaz · Site vitrine

Contrat du système de design. Toute valeur (couleur, taille, espacement) utilisée dans le
code doit tracer vers un token défini ici. Synthèse des skills `ui-ux-pro-max` (palette
« Medical Clinic », polices, règles UX) et `frontend` (taste soft/minimalist, axiomes).

## 0. Research Log
- **ui-ux-pro-max — palette** : base de données `colors.csv`, entrée *Medical Clinic* (teal médical `#0891B2` + vert santé `#16A34A`) et *Healthcare App*. Retenue comme source des tokens de couleur.
- **ui-ux-pro-max — typographie** : `typography.csv`, *Premium Sans* (corps) + choix éditorial serif pour les titres (registre humain/rassurant adapté à un praticien).
- **ui-ux-pro-max — UX** : Quick Reference §1 (a11y : contraste 4.5:1, focus visibles), §4 (icônes SVG, pas d'emoji), §7 (motion 150–300 ms, transform/opacity, reduced-motion).
- **frontend skill — taste** : direction *soft / minimalist* (calme, premium, dimensionnel mais sobre). Axiomes appliqués : pas d'emoji en icône, animations GPU uniquement, motion porteuse de sens, `/visual-qa` mental à 375/768/1280.
- **Skip noté** : CLI Python des deux skills non exécutable (Python absent de la machine) → lecture directe des CSV. Références `references/design/*` du skill frontend non présentes dans le dépôt cloné → application des axiomes du routeur.

## 1. Direction
Calme, clinique, digne de confiance. Beaucoup de blanc, un teal profond comme ancre de
confiance, le vert santé strictement réservé aux confirmations/petits accents. Aucune
esbroufe : la crédibilité prime sur le « wow ». Registre humain grâce à une serif éditoriale.

## 2. Tokens couleur
| Token | Valeur | Usage |
|---|---|---|
| `--teal-600` | `#0891B2` | Primaire (CTA, liens, icônes) |
| `--teal-500` | `#22B8CE` | Hover primaire |
| `--petrol-900` | `#0c3b3f` | Fond sombre (footer, CTA), titres profonds |
| `--petrol-800` | `#134E4A` | Dégradés sombres |
| `--green-600` | `#16A34A` | Accent santé (confirmations, puces) — parcimonie |
| `--ink-900` | `#0F172A` | Titres, texte fort |
| `--ink-600` | `#475569` | Corps |
| `--ink-400` | `#64748B` | Texte secondaire / légendes |
| `--line` | `#E2ECEF` | Bordures, filets |
| `--surface` | `#FFFFFF` | Fond principal |
| `--surface-soft` | `#F3FAFB` | Fond alterné (teinte teal très légère) |
| `--teal-050` | `#E6F6F9` | Fonds d'icônes, puces |
| `--danger` | `#DC2626` | Urgence / erreurs |

Contraste : corps `--ink-600` sur blanc ≈ 8:1, secondaire `--ink-400` ≈ 4.6:1 → AA OK.
**Dette acceptée** : pas de mode sombre (vitrine grand public, mode clair attendu). Palette
sombre non définie ; à ajouter si besoin ultérieur.

## 3. Typographie
- **Titres** : `Fraunces` (serif éditoriale, opsz variable), poids 400–600, `letter-spacing:-0.01em`.
- **Corps / UI** : `Inter`, 400/500/600/700.
- `font-display: swap`. Preconnect Google Fonts.
- Échelle fluide (`clamp`) : h1 2.2→3.6rem · h2 1.6→2.4rem · h3 1.2rem · corps 16→17px.
- Interlignage corps 1.65 ; longueur de ligne ≤ 68ch.

## 4. Espacement & layout
- Rythme 4/8 px. Échelle sections : 16 / 24 / 32 / 48 / 80.
- Conteneur max 1140px, gouttières fluides `clamp(20px,5vw,48px)`.
- Rayons : sm 10 · md 16 · lg 24 · pill 999.
- Ombres douces teintées petrol, jamais dures.
- Breakpoints : 560 / 720 / 900 / 1140.

## 5. Primitives
- **btn** : `.btn` + variantes `-primary` (teal plein), `-outline`, `-ghost`, `-light` ; pill, ≥44px de haut, focus-visible anneau 3px teal.
- **card** : surface blanche, bordure `--line`, ombre sm, hover translateY(-4px)+ombre md (transform seulement).
- **badge / eyebrow** : petite étiquette teal sur `--teal-050`.
- **section-head** : eyebrow + h2 + intro centrés, max 42rem.
- **icon** : SVG inline, stroke 1.6–1.8, jeu cohérent (style Lucide). Jamais d'emoji.

## 6. Motion
- Durées 150–320 ms ; `transform`/`opacity`/`filter` uniquement (jamais layout).
- Reveal au scroll via IntersectionObserver : fade + translateY(16px), stagger 60 ms.
- Hover : uniquement sur éléments réellement interactifs (cartes cliquables, boutons, liens).
- `prefers-reduced-motion: reduce` → toutes animations/reveal désactivés, contenu visible d'emblée.

## 7. Accessibilité
- Contraste AA min. Focus-visible sur tous les interactifs. Hiérarchie h1→h3 sans saut.
- `aria-label` sur boutons/icônes seuls. Carte Google Maps avec `title`. Menu mobile avec
  `aria-expanded`/`aria-controls`. Skip-link vers le contenu principal.
- Cibles tactiles ≥44px. Zoom non désactivé.

## 8. Contenu — véracité (contrainte déontologique)
Site informatif, non promotionnel (art. R.4127-19-1 CSP). Aucune donnée inventée : diplômes,
parcours, langues et photo laissés en emplacements balisés tant que non fournis par le praticien.
Sources publiques : Ramsay Santé, Maiia, Ameli, PagesJaunes. Mention légale + disclaimer requis.
