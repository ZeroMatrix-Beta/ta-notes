# Topic index — the merge key

**Why this file exists.** The tutors do not teach the same material in the same week. Corsin
covers optimization in his Week 5; Adrien's optimization notes are dated 20.03 and 23.03;
Jérôme splits it over *Woche 5.2* and *Woche 6.1*. Merging by calendar week would scramble
the document.

So: **supplements attach to a topic, never to a date.** This table is the only mapping that
matters.

## Status

**The provisional map (derived from Jérôme Paschoud's German file names) was wrong in several
places** — Corsin runs roughly a week ahead of it from Week 4 onwards.

⚠️ **The Skeleton table below carried that provisional map, uncorrected, until Weeks 1–8 were
typeset.** Six rows were off by one week (Taylor, Lagrange, the Hessian test, the implicit
function theorem, tangent spaces, change of variables) — i.e. the correction table immediately
below was never propagated into the table people actually use. Rows verified against
`content/week-0N.tex` are now marked in **bold**. Weeks 9–10 are now typeset and verified.
Weeks 11–13 remain provisional and should be treated as unverified until those chapters are
typeset.

**The authority is `content/week-NN.tex` itself** — grep for the section label, e.g.
`grep -l 'label{sec:lagrange_multipliers}' content/*.tex`. (Earlier revisions of this file named
`transcript/week-*.md` as the authority; that directory does not exist — the project typesets
directly into `content/`, see `docs/01-file-structure.md`.)

| Provisional (from file names) | Actual (from Corsin's notes) |
|---|---|
| Week 4: norms, differential, chain rule | Week 4: differential, chain rule, **and Taylor** |
| Week 5: Taylor, optimization | Week 5: optimization, **Lagrange, Hessian test** (no Taylor) |
| Week 6: optimization II, inverse function thm | Week 6: convexity, inverse **and implicit** function thms |
| Week 7: implicit function thm, submanifolds | Week 7: submanifolds, **tangent & normal spaces** |
| Week 8: tangent spaces, Jordan measure, Riemann | Week 8: **repetition quiz**, change of variables, Fubini, **Feynman's trick** |
| Week 9: change of variables, d-volume | Week 9: **determinants & volume, Gram determinant**, d-volume, curve length |
| Week 10: integrals over submanifolds, divergence thm | Week 10: **geodesics, C¹ domains, flux, Gauss' theorem** |
| Week 11: divergence thm, Green, line integrals | Week 11: Gauss revisited, **alternating forms, wedge product, differential forms, exterior derivative** |

Notably, **line integrals and Green's theorem do not appear in Corsin's notes at all** — a genuine
gap, and the first strong candidate for a Phase 3 supplement.

## Skeleton (from Corsin's week structure; filled in as transcription proceeds)

| Topic | Owning week/section | Lecture notes § | Sheet | Supplements |
|---|---|---|---|---|
| Structured spaces (topological/metric/normed/inner-product) | Week 2 · Monday | ch. 9 | — | |
| Metric spaces, the three axioms | Week 2 · Monday | ch. 9 | 2 | |
| Examples of metrics (discrete, `d₁`, `d₂`, `d₃`, `C⁰`, `S²`) | Week 2 · Monday | ch. 9 | 2 | |
| Open and closed sets, open balls | Week 2 · Monday | ch. 9 | 2 | |
| Topology and continuity | Week 2 · Friday | ch. 9 | 2 | |
| Compactness, Heine–Borel | Week 3 · Monday | ch. 9 | 3 | |
| Banach fixed point theorem | Week 3 | ch. 9 | 3 | |
| Connectedness, path-connectedness | Week 3 · Friday | ch. 9 | 3 | |
| Norm equivalence on ℝⁿ | Week 3–4 | ch. 9 | 3 | |
| The differential, partial derivatives | Week 4 | ch. 10 | 4 | |
| Chain rule, mean value theorem | Week 4 | ch. 10 | 4 | |
| Taylor expansion | **Week 4** | ch. 10 | 4 | |
| Optimization: critical points, gradient | Week 5 | ch. 11 | 5 | |
| Lagrange multipliers | **Week 5** | ch. 11 | 5 | |
| Hessian test, extremal points | **Week 5** | ch. 11 | 5 | |
| Convexity | Week 6 | ch. 11 | 6 | |
| Inverse function theorem | Week 6 | ch. 12 | 6 | |
| Implicit function theorem | **Week 6** | ch. 12 | 6 | |
| Submanifolds, parametrizations | Week 7 | ch. 12 | 7 | |
| Tangent & normal spaces | **Week 7** | ch. 12 | 7 | |
| Repetition quiz (mid-semester, Weeks 2–7) | **Week 8** | — | — | |
| Change of variables / substitution | **Week 8** | ch. 13 | 8 | |
| Fubini's theorem | **Week 8** | ch. 13 | 8 | |
| Feynman's trick (differentiation under $\int$) | **Week 8** | ch. 13 | 8 | |
| Jordan measure | *not covered by Corsin* | ch. 13 | 8 | ⚠ used in Week 8 without being defined — gap |
| Riemann integral (several variables) | *not covered by Corsin* | ch. 13 | 8 | ⚠ gap |
| Length, area, volume; determinant & volume | Week 9 | ch. 13 | 9 | |
| d-volume, improper integrals | Week 9 | ch. 13 | 9 | |
| Integrals over submanifolds | Week 10 | ch. 13 | 10 | |
| Divergence theorem | Week 10–11 | ch. 14 | 10–11 | |
| Green's theorem | Week 11 | ch. 14 | 11 | |
| Line integrals, 1-forms | Week 11 | ch. 14 | 11 | |
| Differential forms, k-forms | Week 12 | ch. 14 | 12 | |
| Orientability | Week 12 | ch. 14 | 12 | |
| Stokes' theorem | Week 13 | ch. 14 | 13 | |
| ODEs, Picard–Lindelöf | Week 13 + Appendix A | — | 13 | |

Chapter numbers were provisional (inferred from Adrien Martelli's chapter-tagged file names).
**Ch. 9 is now confirmed** against Damien Lesieur's `TA_notes_analysis_2.pdf`, which mirrors the
official lecture numbering directly (his `Definition 9.3` = metric space, `Theorem 9.69`/`9.74`
= the three faces of compactness / Heine–Borel, `Proposition 9.83` = continuous image of
connected, etc.) — all metric-space/topology/compactness/connectedness content (Weeks 2–3) is
ch. 9. Chapters 10 (differentiation) and 11 (optimization) are consistent with Damien's file
structure (his notes continue past compactness into differentiation next) but were not checked
page-by-page against `exercises/lec_notes.pdf` here; still worth a full pin-down in a later pass.

## How to add a supplement

1. Find the row the content belongs to — by **topic**, ignoring the source's date.
2. Add `Tutor, file, p. N — one-line description of what it adds` to the *Supplements* cell.
3. Only add it if it is a genuine **gap**: something Corsin does not cover, a materially
   clearer explanation, or an independent worked solution. Not a restatement.
