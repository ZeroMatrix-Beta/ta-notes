# Analysis II — TA Notes → Typeset Document

> ## ⚠️ PRIMARY DIRECTIVE: CORSIN NICK FIRST
>
> **Corsin Nick is the sole architectural blueprint for this project.**
>
> The standing user instruction is: **Get Corsin Nick's notes completely typeset and compiling to `main.pdf` first.** Corsin alone is the core deliverable. The other 16 tutors are touched **only after** all Corsin chapters (weeks 2–13 + ODE appendix) compile cleanly and are fully formatted.
>
> **Execution Order:**
> 1. Scaffolding (`docs/`)
> 2. Typeset Corsin — weeks 2–13 + ODE appendix directly into `content/*.tex` with fine-grained page provenance comments (`% Source: Corsin Nick/Class Notes/Week N.pdf, p. M`)
> 3. Build & Verify: `latexmk` until `main.pdf` compiles with 0 errors
> 4. Native TikZ figures (`docs/05-figure-queue.md`)
> 5. *Optional:* Mine supplements from other tutors for content gaps **only after step 3**

## Context

`C:\Users\miche\latex\ta-notes` holds the exercise-class notes of **17 teaching assistants** for **ETH D-MATH, Analysis II: Several Variables (Prof. J. Serra, FS 2026)**.

The goal is one polished LaTeX document based on Corsin Nick's notes:

- `main.tex` — the document root (purple/olive theme, aliascnt theorem setup, cleveref, fancyhdr, titlepage).
- `gemini.md` — the single source of truth for all guidelines, formatting rules, and Analysis II specifics.

## Why Corsin Nick is the Blueprint

Digital handwriting, very legible, English, consistently structured:

| File | Pages | Topic |
|---|---|---|
| Week 2 | 15 | Structured spaces, metric spaces, open/closed sets, topology, continuity |
| Week 3 | 12 | Compactness, Heine–Borel, Banach fixed point, connectedness |
| Week 4 | 13 | The differential, chain rule, Taylor expansions |
| Week 5 | 11 | Optimization, Lagrange multipliers, Hessian test |
| Week 6 | 12 | Optimization II, inverse function theorem |
| Week 7 | 10 | Implicit function theorem, submanifolds |
| Week 8 | 13 | Tangent spaces, Jordan measure, Riemann integral |
| Week 9 | 8 | Change of variables, length/area/volume, d-volume |
| Week 10 | 12 | Integrals over submanifolds, divergence theorem |
| Week 11 | 15 | Divergence theorem & Green, line integrals |
| Week 12 | 7 | Differential forms |
| Week 13 | 9 | Stokes, ODEs |
| Analysis 1 lesson on ODEs | 13 | ODE recap → appendix |

⚠️ **Numbering note:** The file name of Corsin's PDF is canonical (`Week 2.pdf` = Chapter 1 = Week 2).
