# Old-exam mining ledger

What has been taken out of `old_exams/` and what has been **rejected forever**, so that no later
pass re-reads a paper this one already worked through.

⚠️ **Despite the file name, this ledger also covers loose official material that is not an exam
and not a numbered problem sheet** — currently `DiffComp.pdf` in the project root. Such files have
no home in `content/appendix-d-problem-sheets.tex` either, which is an inventory of the numbered
sheets only, so without a row here they are invisible and get mined twice or never. **If you find
another stray official PDF, add it to the table below rather than inventing a third register.**

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
| `august2025` | Prof. Laura Kobel-Keller | **Not yet mined.** Unlike every file above, this one is *Analysis II alone* (`Analysis II: mehrere Variablen`), and it is bilingual German/English. See below. |

`examHS24`, `examFS24`, `WS22_Prüfung` and `fs2023/Prüfung` were mined in earlier passes (Serra and
Felder); `gemini.md` records their dates and the fact that only the two Felder papers ship a
solution key.

⚠️ **`august2025.pdf` and the three `Probeprfg` mock exams have never been mined by anybody.** An
earlier revision of this file asserted that they had been, which was wrong: `grep` over `content/`
returns no citation of either. See *Where to mine next*, immediately below, which is where that
correction leads.

## Loose official material (not exams, not numbered sheets)

| File | What it is | State |
|---|---|---|
| `DiffComp.pdf` (project root) | **Prof. Joaquim Serra**, *Some differential form computations 1*, Analysis II FS 2026, issued 13 May 2026, ungraded. 4 pp: six problems computing `ω = df ∧ λ` on `ℝ³`, then his own full worked solutions. | ✅ **Mined 2026-08-11, in full.** All six are `ex:serra_df_wedge_lambda` in `content/24-differential-forms/02-exterior-derivative.tex`, solutions in that chapter's `99-solutions.tex`. Nothing left in it. |

Two things about `DiffComp.pdf` worth carrying forward. It is the **only** source mined so far that
is by this course's own lecturer *and* ships worked solutions, so its solution block is marked
`% Extractor:`, not `% Generator:` — the mathematics is Serra's. And all six of his boxed answers
were re-derived here independently and are correct, so there is no erratum to inherit.

## Where to mine next

**Start here. In this order.** The 2026-08-11 pass worked the `HS*`/`FS*` block and `DiffComp.pdf`
and stopped; the three targets below are untouched, and the first two are worth more than
everything that block had left in it.

### 1. `old_exams/august2025.pdf` — do this one first

**Prof. Laura Kobel-Keller, August 2025, 21 pages.** Never mined: no `% Source:` anywhere in
`content/` names it. It is the single best target in the folder, for four independent reasons.

* **It is Analysis II alone.** Its title is *Analysis II: mehrere Variablen*. Every `HS*`/`FS*`
  paper is a combined Analysis I & II exam whose first half has to be discarded, and that filtering
  was the main cost of the last pass. Here there is nothing to filter.
* **It is bilingual.** Every question is printed in German and then in English. The English is the
  examiner's own, so a statement can be quoted rather than translated, which removes the one place
  the last pass had to exercise judgement silently.
* **It is the most recent exam in the folder**, by roughly four years, so its scope and emphasis
  are the closest of anything here to the course this document actually serves.
* **It opens with a single-choice section** (`Bei den folgenden Fragen gibt es jeweils genau eine
  richtige Antwort`), which converts into `exercise` blocks in the true/false style already used
  throughout chapters 19 and 20.

Question 1 is a Cauchy-sequence question aimed at chapter 6, so the paper starts inside our scope
on page 1. Work it front to back.

### 2. The three mock exams, two of which ship solution keys

None of these is cited in `content/`, and **the keys are the point**: not one paper mined on
2026-08-11 had a solution to check against, so every solution in the table below rests on
independent derivation alone. These four files are the only chance in the whole folder to mine
problems *and* verify the answers.

| Problems | Key | Pages |
|---|---|---|
| `old_exams/fs2023/Probeprfg3.pdf` | `old_exams/fs2023/Probeprfg3_Lsg.pdf` | 4 + 6 |
| `old_exams/fs2023/2022/Probeprfg2.pdf` | `old_exams/fs2023/2022/Probeprfg2_Lsg.pdf` | 4 + 7 |
| `old_exams/fs2023/Probeprfg1.pdf` | none | 3 |

Note the trap that the rest of this file warns about applies here too: `Probeprfg2` sits in
`fs2023/2022/`, not beside its siblings. Copy the path, do not reconstruct it.

⚠️ **Derive first, open the key second.** This is the `SolN_Analysis2_eng.pdf` rule in `style.md`,
and it exists because reading a solution first steers your method even when you do not copy it.
The keys are for checking, not for drafting.

### 3. One deferred problem from the last pass

`FS19` Teil B Aufgabe 4 (Jossen): the area `f(t)` of the region cut off by a moving ellipse, and
whether `f` is `C¹`. It was dropped only for length, since it needs a figure. Pick it up if
chapter 20 ever wants a parameter-integral example with a picture.

### 4. Look for a second Serra example sheet

`DiffComp.pdf` is titled *Some differential form computations **1***, and its problems are numbered
`1.1`–`1.6` under a section heading `1.`. Both strongly suggest a sheet 2 exists. It is not in the
repository as of 2026-08-11. If one appears, it goes straight to the top of this list: same
lecturer, same course, same semester, worked solutions included.

### What is genuinely exhausted

The `HS*`/`FS*` block. Every one of those 37 files has been surveyed and its verdict recorded
below, either in the accepted table or in the rejection tables. **Do not re-read them.** The one
category deliberately left unharvested is constrained-optimisation problems, of which the folder
holds at least five near-identical variants; the reasoning is in the rejection table and it has not
changed.

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
