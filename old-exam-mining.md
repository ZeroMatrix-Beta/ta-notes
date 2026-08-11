# Old-exam mining ledger

What has been taken out of `old_exams/` and what has been **rejected forever**, so that no later
pass re-reads a paper this one already worked through.

`gemini.md` holds the mining *rules* (`% Extractor:` versus `% Generator:`, never invent a path,
open the cited page and render it). This file holds only the *record*. It is an inventory, not a
status report — the deliberate absence of a project-status file still stands, and nothing here says
how far anything has got.

## ⚠️ Read this before adding a row

**These are Analysis I & II papers, not Analysis II papers.** Roughly half of every one of them is
single-variable material this document has no chapter for: integration techniques, series
convergence, power series, `l'Hôpital`, sequences of reals, the completeness of `ℝ`. That is the
largest rejection category by far and it is not itemised below, because itemising it would triple
the length of this file for no benefit. **If a problem is one-variable, it is out; do not record
it, and do not reconsider it.**

**Cite the lecturer.** The papers span at least six professors with visibly different exam styles
and syllabus emphases, so a bare date under-identifies a problem. `\exinfo` gets
`(Prof. <name>)` after the date and the phrase "Analysis I & II examination"; the `% Source:`
comment gets file, lecturer, date and page. See `style.md`.

**The file names mislead.** `HS19.pdf` is the exam of **22 January 2020**, `HS20.pdf` is
**27 January 2021**, and so on: an `HSnn` paper is sat in the January *after* `nn`. The date on the
paper itself is what goes in a citation. Note also that three pairs are byte-identical duplicates:
`FS08 = HS08`, `FS09 = HS09`, `FS15 = HS15` (verified by `md5sum`).

## Who set which paper

| Files | Lecturer | Notes |
|---|---|---|
| `FS16`, `HS16` | Prof. H. Knörrer | 4-hour paper. Distinctive "find the flaw in this proof" format, which is where its value is. |
| `FS17`, `HS17`, `FS18`, `HS18` | Prof. Manfred Einsiedler | Three-part structure: computations, applications of theory, theory from the lecture. Part 3 asks candidates to reproduce proofs from the course, so it is the richest seam for material this document states without proof. |
| `FS19`, `HS19`, `FS20`, `HS20` | Prof. Peter S. Jossen | Part A short questions, Part B five long problems of which four are attempted. The Part B problems are the best-structured multi-part exercises in the whole folder. |
| `FS13`, `HS13` | Prof. J. Teichmann | Surveyed, nothing taken. |
| `FS14`, `HS14` | Prof. E. Kowalski | Surveyed, nothing taken. |
| `FS15`, `HS15` | Prof. D. Salamon | Surveyed, nothing taken. |
| `HS00`–`HS03`, `FS04`–`FS12`, `HS04`–`HS12` | various / unidentified | Mostly *Vordiplom* papers. See the rejection notes below. |

`examHS24`, `examFS24`, `WS22_*`, `fs2023/*` and `august2025` are **not** covered by this file. They
were mined in earlier passes (Serra and Felder); `gemini.md` records their dates and the fact that
only the two Felder papers ship a solution key.

## Accepted — 2026-08-11 pass

Thirteen blocks, three lecturers, eight chapters. Each was verified by rendering the cited page
(`pdftoppm`) and reading it; `pdftotext` was used only for triage, never for a formula.

**No Knörrer, Einsiedler or Jossen paper ships a solution key.** Every solution below is an
independent derivation with nothing to check it against, which is a weaker position than the
official-sheet exercises are in. Treat them accordingly.

| # | Source | Lecturer | Lands in | Form | Why it earns its place |
|---|---|---|---|---|---|
| 1 | `FS20` Teil B A2 (c)–(e) | Jossen | `07-compactness/05` `ex:pseudocompactness_implications` | exercise | Splits Weierstrass in half: "every continuous function is bounded" ⇔ "every one attains its extrema", with no compactness anywhere. Nothing in the chapter says this. |
| 2 | `FS19` Teil B A2 (d)–(f) | Jossen | `07-compactness/05` `ex:sumset_open_closed_compact` | exercise | Sumsets `A+B`. The closed + compact case is the classic, and the counterexample for closed + closed is worth having. |
| 3 | `HS18` A9 | Einsiedler | `07-compactness/03` `ex:locally_lipschitz_is_lipschitz` | worked example | Locally Lipschitz on a compact space is Lipschitz. Second real application of the Lebesgue number, and the two-regime split is the transferable idea. |
| 4 | `FS16` A12 | Knörrer | `16-implicit/01` `ex:knoerrer_wrong_partial_derivative` | worked example | The single most common misreading of the implicit function theorem — checking `∂F/∂t` instead of `∂F/∂x` — set as "find the flaw", with a counterexample. |
| 5 | `HS18` A7 | Einsiedler | `17-submanifolds/01` `ex:immersion_locally_submanifold` | worked example | An immersion is locally a parametrization: the homeomorphism clause of `thm:local_parametrization` is free once the domain shrinks. Genuine theory the chapter lacks. |
| 6 | `HS19` Teil B A4 | Jossen | `17-submanifolds/01` `ex:orthogonal_group_submanifold` | exercise | `O₂(ℝ)`. The naive regular value theorem *fails* here; restricting the codomain to the symmetric matrices repairs it. Pairs against the existing rank-1 matrix exercise in the same `ℝ⁴`. |
| 7 | `HS20` Teil B A2 (b)–(e) | Jossen | `19-jordan-measure/01` `ex:lebesgue_null_sets_properties` | exercise | Countable unions of null sets, and the graph of a Riemann-integrable function. Part (c) is a fact this document leans on and never proves. |
| 8 | `HS18` A13 | Einsiedler | `20-change-of-variables/01` `ex:linear_substitution_elementary_matrices` | exercise | **This is the proof of `thm:jordan_measure_linear_transformation`,** which ch. 19 states without one. |
| 9 | `HS17` A13 | Einsiedler | `20-change-of-variables/01` `ex:cube_covering_lemma_substitution` | worked example | The hard geometric lemma behind `thm:change_of_variables`, which is stated without proof. Mean value inequality plus Banach fixed point. The hardest block in the pass. |
| 10 | `HS16` A3 | Knörrer | `23-flux-divergence/02` `ex:knoerrer_divergence_free_compact_support` | exercise | A compactly supported divergence-free field has zero mean. Short, and the `f(x) = x₁` trick is worth meeting. |
| 11 | `FS18` A9 | Einsiedler | `23-flux-divergence/02` `ex:flux_bounded_by_oscillation` | worked example | Flux through a closed surface is bounded by the *oscillation* of the field, because a constant field is invisible to it. A technique, not a drill. |
| 12 | `HS20` Teil B A3 | Jossen | `26-stokes/03` `ex:jossen_potential_on_disconnected_domain` | exercise | The mirror image of `ex:vortex_field_not_conservative`: a domain that is not simply connected on which the field *is* conservative. Catches "not simply connected ⟹ not conservative". |
| 13 | `FS16` A10 | Knörrer | `26-stokes/02` `ex:moving_rectangle_derivative` | worked example | `d/dt ∫_{Q_t} f = ∮_{∂Q_t} f(−dx+dy)` for a rectangle sliding along the diagonal. Reynolds transport in miniature, and it holds for merely continuous `f`, where Green's theorem cannot reach. |

### Not from the exams, but from the same pass

`content/19-jordan-measure/03-a-glimpse-of-lebesgue.tex` was written on the user's explicit
instruction after they asked whether Jordan measure and Lebesgue measure are the same thing. It is a
digression, stated without proofs, used nowhere later, with four easy `aiexercise`s. The scope
reversal that authorises it is recorded in `gemini.md`; the `aside` environment was added to
`main.tex` in the same pass and is documented in `style.md` and `build-and-preamble.md`.

## Rejected — do not reconsider

### Whole papers

| Files | Why, forever |
|---|---|
| `HS00`, `HS01`, `HS03` | *Vordiplom* papers typeset with bitmap/Type 3 fonts. `pdftotext` returns pure garbage, so every problem would have to be read from a rendered image. The content that is visible is single-variable. Not worth the rendering cost. |
| `HS02` | Is a **solution** document (`Lösung 1. Vordiplom Analysis, Herbst 2002`), not a problem set, and single-variable throughout. |
| `FS04`–`FS12`, `HS04`–`HS12` | *Vordiplom* / early *Basisprüfung* era. Surveyed by keyword census for multivariable content; the hits are routine Lagrange, routine flux and routine volume computations of kinds this document already carries several of. Nothing distinctive enough to pay for. |
| `FS13`, `HS13` (Teichmann) | Surveyed. Multivariable content is standard computation. |
| `FS14`, `HS14` (Kowalski) | Surveyed. `FS14` carries a solution key, which is tempting, but its Analysis II content duplicates material already present. |
| `FS15`, `HS15` (Salamon) | Surveyed. The first half is heavily Analysis I (Euler–Mascheroni, `arctan` series, convergence radii); the multivariable remainder is routine. |
| `FS08 = HS08`, `FS09 = HS09`, `FS15 = HS15` | Byte-identical duplicate pairs. Read one, never the other. |

### Individual problems considered and dropped

| Problem | Why |
|---|---|
| `FS17` A8 (`M = {y(y²−x) = 0}` is a submanifold away from the origin) | Good problem, but `ex:cross_not_submanifold` and `ex:lollipop_tangent_field` already teach "how to prove a set is *not* a submanifold at a bad point" twice. A third is clutter. |
| `FS17` A9 (`∫_Q f = 0` and `f ≥ 0` continuous ⟹ `f ≡ 0`) | Standard, and short enough that it adds nothing a reader could not do unprompted. |
| `FS17` A6, `FS20` Frage 2, `HS20` Frage 1 (continuous / uniformly continuous / Lipschitz implications) | `content/05-continuity/02-lipschitz-continuity.tex` already covers exactly this chain, with counterexamples. |
| `HS17` A9 (`\|f\|²` attains no maximum when `Df` is invertible) | Genuinely elegant, and a near-duplicate of material already mined from `examHS24` into `15-inverse-function-theorem`. Held back to avoid a third inverse-function-theorem exercise in one section. |
| `HS17` A5, `FS19` Teil B A3, `HS20` Frage 12, `HS16` A4, `FS16` A4 (constrained optimisation on a ball, a half-ball, a hyperboloid, a disc) | Five variants of one exercise. `13-lagrange` and `12-extrema-hessian` already carry several, including two mined from Serra papers. Volume without variety. |
| `HS18` A12 (divergence as a limit of flux over shrinking squares) | Attractive, but it is a *definition* of divergence competing with the one ch. 22 gives, and reconciling the two would cost more prose than the block is worth. |
| `HS18` A8, `FS20` Teil B A5 (continuity and ODEs for improper parameter integrals) | Overlaps `20-change-of-variables/03-feynmans-trick.tex`. `FS20` A5 is also very hard and its payoff is a complex-exponential basis argument, which is out of scope. |
| `FS19` Teil B A4 (the ellipse-area function `f(t)`, is it `C¹`?) | Strong candidate, dropped only for length: it needs a figure to make sense, and the pass was already carrying two figure-free worked examples in the same area. **Worth reconsidering** if ch. 20 ever wants a parameter-integral example with a picture. |
| `FS19` Teil B A5, `FS20` Teil B A4 (paraboloid and triangle: parametrise, normal, flux, Stokes) | Careful multi-part Stokes problems, but `26-stokes` already has the Serra ones and the mechanics are identical. |
| `HS19` Frage 6 (Hamiltonian is constant along its flow) | One line by the chain rule. Too small to number. |
| `HS19` Frage 14 (differentiate `∫₀¹ xᵅ dx` in `α` to get `∫₀¹ log(x)²x³ dx`) | This *is* Feynman's trick, and `20-change-of-variables/03-feynmans-trick.tex` is a whole section of it. |
| `HS19` Teil B A2 (open maps, closed maps, and `f(B̄) ⊆ f(B)`) | Nice, but stated for `f : ℝ → ℝ` throughout, so it is Analysis I in an Analysis II costume. |
| `HS20` Teil B A1 (`f_A(x) = dist(x,A)`, continuity, zero set is `Ā`) | Already in `03-open-and-closed-sets` in substance. |
| `FS20` Teil B A1 (mollifiers) | Requires a passage of text the exam reproduces from a book and the PDF renders as an image; and partitions of unity are handled a lighter way in ch. 25 by deliberate choice (`gemini.md`). |
| `FS20` Frage 13 (`D²f(0)(v,w)` versus `D²f(0)(w,v)`) | Schwarz's theorem, which `12-extrema-hessian` states. The bilinear-form reading is a nice angle but does not carry an exercise on its own. |
| `HS16` A11, A12, `FS16` A11 (further "what is wrong with this proof?" blocks) | The format is excellent and #4 above is the best instance of it. The others are about uniform convergence and the floor function in one variable, so they fall to the Analysis I rule. |
| `FS16` A2, `HS16` A2 (volume of `{\|z\| ≤ sin(x²+y²)}`, ball minus cylinder) | Routine cylindrical-coordinate computations. `20-change-of-variables` has several. |
| Every "state the theorem" / "give the definition" part, throughout | These test recall of the lecture, not understanding, and this document is not a flashcard deck. They are systematically dropped, and where a mined problem's first parts are of this kind the `\exinfo` says so. |
| `FS19` Frage 12, `HS19` Frage 12 (`√(i²)`, and the `1 = −1` fallacy) | Charming, and about complex square roots, which is Analysis I. Would make a fine `aside` if anyone ever wants one. |
| `FS19` Frage 15, `HS20` Frage 15 (Zorn's lemma) | Out of scope entirely. |
