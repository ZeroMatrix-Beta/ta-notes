# Source inventory

Course: **ETH D-MATH, 401-1262-07L — Analysis II: Several Variables**, Prof. Joaquim Serra, FS 2026.
Course page: <https://metaphor.ethz.ch/x/2026/fs/401-1262-07L/>

Everything below is **read-only input**. Page counts are from PDF object counting.

---

## 0. Official course material (`exercises/`, downloaded 2026-08-02)

| File | Pages | Note |
|---|---|---|
| `Ex1_Analysis2_eng.pdf` … `Ex13_Analysis2_eng.pdf` | ~2 each | Official problem sets, **English**. Typeset LaTeX. |
| `Sol1_Analysis2_eng.pdf` … `Sol13_Analysis2_eng.pdf` | ~4–8 each | Official solutions, English. |
| `lec_notes.pdf` | — | **Official lecture notes.** The authority for chapter/theorem numbering (`9.19`, `10.4`, …). |
| `DiffComp.pdf` | — | Differential-forms worked examples. |
| `examFS24.pdf`, `examHS24.pdf` | — | Past exams. |

Text extracts cleanly with `pdftotext -layout`, but **math glyphs are mangled**
(`∫ → �`, `⊂ → ` , `× → �`). Use `pdftotext` for structure and read the page image to get
formulas right.

**Usage policy.** Exercise *statements* are quoted in full in the transcript and the final
document (see `04-style-guide.md`), with attribution to the official sheet. Official
*solutions* are used only to check the TAs' work — the document presents the **TAs'**
solutions, not ETH's. The title page already carries an unofficial-document disclaimer.

---

## 1. Primary source — transcribed in full

### Corsin Nick — `Corsin Nick/Class Notes/` — 137 pp

Digital handwriting, English, very legible. The **structural blueprint** for this document.

Per file: cover page → *Recommended exercises* (that week's problem sheet, colour-coded
▨ important / ▨ semi-important / ▨ optional, with hints) → `Monday` / `Friday` session
headings → topic headings → `Thm:` / `Def` / `Exercise:` / `Solution:` blocks → hand-drawn
diagrams.

| File | Pages | Topics |
|---|---|---|
| `Week 2.pdf` | 15 | Structured spaces, metric spaces, open/closed sets, topology, continuity |
| `Week 3.pdf` | 12 | Compactness, Heine–Borel, Banach fixed point, connectedness |
| `Week 4.pdf` | 13 | Norms, the differential, chain rule |
| `Week 5.pdf` | 11 | Taylor, optimization (critical points, gradient) |
| `Week 6.pdf` | 12 | Optimization II, inverse function theorem |
| `Week 7.pdf` | 10 | Implicit function theorem, submanifolds |
| `Week 8.pdf` | 13 | Tangent spaces, Jordan measure, Riemann integral |
| `Week 9.pdf` | 8 | Change of variables, length/area/volume, d-volume |
| `Week 10.pdf` | 12 | Integrals over submanifolds, divergence theorem |
| `Week 11.pdf` | 15 | Divergence theorem & Green, line integrals |
| `Week 12.pdf` | 7 | Differential forms |
| `Week 13.pdf` | 9 | Stokes, ODEs |
| `Analysis 1 lesson on ODEs.pdf` | 13 | ODE recap → Appendix A |

⚠️ The cover of `Week 2.pdf` reads *"Class notes Week 1"*; `Week 3.pdf` / `Week 9.pdf` read
*"Week 3"* / *"Week 9"*. **File name is canonical.**

`Corsin Nick/Books/` (Michaels Analysis 1 & 2, Serra script 2024, Zorich) — third-party
books. **Excluded**; cited only.

---

## 2. Curated supplements — mined for gaps only

Ordered by cost-effectiveness. The first three are typeset and text-extractable, so they
are nearly free.

| Tutor | Files | Pages | Format | Lang | Content | Why it earns a place |
|---|---|---|---|---|---|---|
| **Toby Lane** | `class-document.pdf` + 8 `.ggb` | 100 | Typeset LaTeX, has TOC | EN | Full course companion | Only source with interactive GeoGebra assets (`gradient_contour`, `directional_derivative1–4`, `extremum-quiz-1/2`, `diff_not_allpd`) — ideal TikZ references |
| **Lukas Krause** | 11 PDFs | 144 | Typeset LaTeX | EN | Textbook-style class notes, weeks 2–13 (**week 8 missing**) | Cleanest independent English restatement; good tie-breaker where Corsin is terse |
| **Damien Lesieur** | 2 PDFs | 21 | Typeset LaTeX | EN | Theory summary + Q&A | Numbers its lemmas to match the lecture (`9.19`, …) — cheapest way to pin our statements to `lec_notes.pdf` |
| **Toprak Erakay** | 12 PDFs | 322 | Digital handwriting, large & clean | EN | Detailed worked exercise solutions | Largest, most legible handwritten solution corpus |
| **Sascha Brack** | 22 + 8 + 3 | 187 / 27 / 47 | Digital handwriting | EN | Mon+Fri class notes; annotated official sheets; Jordan-measure thesis; Kahoot | Two sessions per week like Corsin; his `Ex Sheet Hints/` give a second TA's importance ranking |

---

## 3. Skipped — and why

| Tutor | Pages | Reason |
|---|---|---|
| **Adrien Martelli** | 121 | Good notes, but topic coverage fully duplicated by Corsin + Lukas. Revisit only if a gap survives Phase 3. |
| **Diego Torres Tejeda** | 161 | Photo-scanned pen handwriting; solutions duplicated by Toprak at better legibility. |
| **Jérôme Paschoud** | 98 | German. **Kept as the authority for German technical terms** (his file names are topic-named: *Metrische Räume*, *Satz über implizite Funktionen*, …) feeding the glossary — but not transcribed. |
| **Lennard Trautmann** | 37 | German, terse sheet solutions; superseded by the official `Sol*.pdf`. |
| **Linus Lüchinger** | ~700 frames | Beamer with heavy overlay duplication; low content density per frame. |
| **Fabio Guger** | 87 | Very small dense script; content duplicated. |
| **Maarten Cnoops** | 73 | German **and** poor legibility (cursive photo scans). |
| **Noah Larsson** | 146 | German. Excellent quality — the best German source. Reconsider only if the document ever goes bilingual. |
| **Riccardo Vanoni** | 5 | Too small to matter (p-norm equivalence, connectedness). |
| **Simon Kamps** | 18 | Annotated copies of official sheets we now have directly. Kept as an *importance signal* only. |
| **Tim Fessler** | 326 frames | German PowerPoint; formulas are embedded objects, exercise texts are pasted images — little derivable text. |

### Out of scope entirely

- `Adrien Martelli/Extra material/ANALYSIS II MICHAELS.pdf` (386 pp) ≈
  `Jérôme Paschoud/Sonstiges/ANALYSIS II MICHAELS-1.pdf` — third-party book.
- `Analysis_II_2024.pdf` = `Lecture_2024.pdf` (207 pp) — last year's official notes,
  superseded by `exercises/lec_notes.pdf`.
- `Buch_Analysis_1_Michaels.pdf` (528 pp) — Analysis **I**.
- `Noah Larsson/Extra Material/Physik_II_Formelsammlung.pdf`,
  `Codes_Datenanalyse_Pruefung_Noah.ipynb` — different courses.
