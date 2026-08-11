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
| `august2025` | Prof. Laura Kobel-Keller | ✅ **Mined 2026-08-11, front to back.** Analysis II alone (`Analysis II: mehrere Variablen`), bilingual German/English. All 19 questions read from rendered pages. See the accepted table below and *What is left in `august2025`*. |

`examHS24`, `examFS24`, `WS22_Prüfung` and `fs2023/Prüfung` were mined in earlier passes (Serra and
Felder); `gemini.md` records their dates and the fact that only the two Felder papers ship a
solution key.

⚠️ **The three `Probeprfg` mock exams have still never been mined.** `august2025.pdf` had not been
either until 2026-08-11; an earlier revision of this file asserted otherwise, which was wrong. See
*Where to mine next*, immediately below.

## Loose official material (not exams, not numbered sheets)

| File | What it is | State |
|---|---|---|
| `exercises_2024/` | **The FS 2024 edition of this same course** — 401-1262-07L, Prof. Joaquim Serra, sheets written by Federico Franceschini. Thirteen sheets with full official solutions in English *and* German, a 180-minute mock exam with a key, and `exam1.pdf`. | ⚠️ **Mostly a duplicate of `exercises/`. See the warning below before opening it.** |
| `DiffComp.pdf` (project root) | **Prof. Joaquim Serra**, *Some differential form computations 1*, Analysis II FS 2026, issued 13 May 2026, ungraded. 4 pp: six problems computing `ω = df ∧ λ` on `ℝ³`, then his own full worked solutions. | ✅ **Mined 2026-08-11, in full.** All six are `ex:serra_df_wedge_lambda` in `content/24-differential-forms/02-exterior-derivative.tex`, solutions in that chapter's `99-solutions.tex`. Nothing left in it. |

### ⚠️ `exercises_2024/` is the same sheets, renumbered by nothing at all

**Established 2026-08-11 by reading the two side by side, not inferred.** The FS 2026 problem
sheets in `exercises/` are a re-issue of the FS 2024 sheets in `exercises_2024/`. Problem `N.M` of
one is problem `N.M` of the other, word for word, differing only where the sheet cites a numbered
definition from the script (the script was renumbered between the two years).

**The trap this sets.** The FS 2024 sheets label their problem `N.1` **`BONUS PROBLEM`**, and the
FS 2026 sheets do not. A pass told to "mine all the bonus problems" will therefore find ten
problems that look new and are not: seven of the ten were already transcribed years ago under
`exercises/ExN_Analysis2_eng.pdf` provenance. They are `3.1`, `4.1`, `5.1`, `7.1`, `9.1`, `10.1`
and `11.1`. **Check `content/` for the exercise before transcribing anything out of this folder.**

Of the remaining three, `8.1` and `12.1` were mined on 2026-08-11 — appendix D had already listed
both as *not transcribed*, so they were documented gaps rather than finds — and `6.1` was
considered and **rejected**, because both of its parts are already in ch. 14
(`ex:convexity_characterizations` part (c), and `ex:convex_function_unattained_infimum`, which uses
exactly the `e^{x₁+x₂}` the problem asks for). That decision is recorded in appendix D too.

**What the folder is still good for**, and it is not nothing:

* **Official solutions to every sheet, in English and German.** `exercises/` ships these too, but a
  second independent write-up is worth having when a solution here was derived rather than checked.
* **`mock.pdf` + `mocksol.pdf`** — a 180-minute Analysis II mock exam with a key.
  ✅ **Mined 2026-08-11, front to back.** See *`mock.pdf` is the August 2024 exam with the numbers
  changed* below, which is the finding that matters, and the accepted table further down.
* **The priority markers differ from Corsin's.** Franceschini marks his own recommended problems
  with a heart, `(♡)`, and `(*)` for the harder ones. Where a problem carries a heart, tag it
  `\textnormal{(important)}` exactly as for Corsin's blue marker.

### ⚠️ `mock.pdf` is the August 2024 exam with the numbers changed

**Established 2026-08-11 by reading the two side by side.** This is the same trap as the one above,
one level up: `exercises_2024/mock.pdf` and `old_exams/examFS24.pdf` (21 August 2024, Serra, already
mined) are the same paper, question for question, with the data altered. Its **Exercise 1 is
`examFS24`'s Aufgabe 1 verbatim** — same annulus `U`, same `f(x,y) = sin(xy) − y⁴`, same six parts —
and it has been `ex:annulus_continuous_image` in `07-compactness/05` since long before this pass.

The rest of the correspondence, with the mock's numbering first:

| mock | `examFS24` | Verdict |
|---|---|---|
| Ex 1 (annulus, `sin(xy) − y⁴`) | Aufgabe 1 | **Identical.** Already `ex:annulus_continuous_image`. |
| Ex 3 (Banach hypotheses, three pairs) | Aufgabe 2 (`X=[0,1]`, `x²`) | Same drill; `ex:banach_hypotheses_true_false` and `ex:bfpt_applicability_table` already carry it twice. Rejected. |
| Ex 5 (`xy²/(x²+y²+z²)` on `ℝ³`) | Aufgabe 4 (`xy²/(x²+y²)` on `ℝ²`) | Near-duplicate of `ex:regularity_ladder_xy2`. Rejected. |
| Ex 6 (Taylor, `x₁²+x₃⁴+o(\|x\|⁵)`) | Aufgabe 5 (`10x₂+x₁²+x₂²+o(\|x\|²)`) | Near-duplicate of `ex:expansion_five_verdicts`. Rejected. |
| Ex 9 (`F : ℝ³→ℝ²`, level set) | Aufgabe 6 (`Φ : ℝ²→ℝ²`) | **Taken.** Wide Jacobian, not square: a different theorem does the work. |
| Ex 10 (`sin(xy)/(x²+y²)`, `(x+1)log`) | Aufgabe 10 (`cos(xy)/(x²+y²)²`) | Near-duplicate of `ex:improper_cos_over_r4`. Rejected. |
| Ex 11 (`Φ` non-injective; `Ψ : ℝ²→ℝ³`) | Aufgabe 7 (affine `ℝ³→ℝ³`) | **Taken.** Gram determinant with `m > n`, which the square case cannot reach. |
| Ex 12 (`∫e^{−x²−y²−α\|z\|}`) | Aufgabe 9 (`∫e^{−α\|x\|}` in the plane) | **Taken.** Product splitting rather than polar coordinates. |
| Ex 13 (three fields `X`, `Y`, `Z`) | Aufgabe 11 (two fields, two circles) | Near-duplicate of `ex:two_fields_two_circles`. Rejected. |
| Box 15–22 | Kästchenaufgaben 1–4 | Same *form* (answer-only box questions), different problems. **Four taken.** |
| Ex 23 (`(x²+y²)e^{αx}` on the disc) | Kurzproblem 1 (`eˣ(x²+αy²)`) | Near-duplicate, **and** it falls under the standing constrained-optimisation rejection at the foot of this file. Rejected twice over. |
| Ex 25 (paraboloid `U`/`M`, flux of `E` and of a curl) | Kurzproblem 2 (paraboloid `U`/`M`, flux of `E` and of `curl A`) | Near-duplicate. Rejected; see the note below on its part 2. |

**The lesson to carry forward is the one this file already learned about `exercises_2024/`: check
`content/` for the exercise before transcribing anything.** Six of the fourteen multiple-choice
blocks were already in the document, and the resemblance is close enough that a pass working from
the mock alone would have added all six as new material.

**What is left in `mock.pdf`, and why.** Ten blocks were taken (see the accepted table). Of the
rest, the near-duplicates above account for most; five further ones were considered on their
merits and dropped:

| Problem | Why |
|---|---|
| Ex 2 (`X ⊆ ℝ²`: not open ⟹ closed? convex ⟹ connected? bounded ⟹ compact? complete ⟹ closed?) | Four standard implications, each already covered: `03-open-and-closed-sets` for the first, `08-connectedness` for the second, `rem:boundedness_not_topological` and `ex:kobel_compactness_characterisation` for the third and fourth. |
| Ex 7 (a Hessian with a parameter `α`, and `∇f` as a diffeomorphism) | The Hessian half is the rejected routine-classification kind and ch. 12 carries six already. Its one distinctive part, that `det Hf ≠ 0` makes `∇f` a local diffeomorphism, **is** `ex:hessian_gradient_diffeomorphism` in ch. 15. |
| Ex 14 (four concrete `F` for Picard–Lindelöf) | `ex:kobel_picard_lindeloef_single_choice` in `appendix-a-odes.tex` makes the same point (Lipschitz in the state variable, not the independent one) and its part (3), `y + √\|x\|`, is exactly this block's part (3). |
| Ex 24 (`y'' − y' = f`, then `z' = Az` with a parameter) | The appendix already carries `ex:three_linear_odes`, `ex:ode_inhomogeneous` and `ex:ode_matrix_exponential`. The one part worth having is the boundedness question (all solutions bounded as `t → +∞` exactly for `α ≤ 0`), which is a stability question the course does not develop. |
| Problem 26 (mollifiers: an explicit bump function `η(t) = e^{−tan²t}/cos²t`, and smoothing a solution of `Lu = f`) | 20 points and five parts, and it needs convolution, which this document does not have. Its one gem is that `∫η = √π` falls out of `s = tan t` in a line. **Reconsider only if a section on convolution is ever written**; the standing rejection of `FS20` Teil B A1 (mollifiers) is the same call made once already. |

⚠️ **One part of Ex 25 is worth reconsidering on its own.** Part 2 asks the reader to *construct* a
vector potential `A` with `B = curl A`, with a hint at the shape to try. Every existing block in
`23-flux-divergence` and `26-stokes` goes the other way, from a given `A` to a flux, and
`examFS24`'s Kurzproblem 2 hands `A` over. If ch. 26 ever wants a construct-the-potential exercise
to sit beside `ex:ai_which_fields_are_gradients`, this is the one.

`exam1.pdf` is the exam of **21 August 2024** — the same paper as `old_exams/examFS24.pdf`, already
mined. Same lecturer, same date, same course number, same 12 pages. It is **not** the same *file*:
the two have different `md5sum`s and differ in size by a factor of nearly two (614 kB against
357 kB), so they are two renderings of one document. Do not read it twice, and do not "correct"
this row to say the files are identical — that was checked and they are not.

Two things about `DiffComp.pdf` worth carrying forward. It is the **only** source mined so far that
is by this course's own lecturer *and* ships worked solutions, so its solution block is marked
`% Extractor:`, not `% Generator:` — the mathematics is Serra's. And all six of his boxed answers
were re-derived here independently and are correct, so there is no erratum to inherit.

## Where to mine next

**Start here. In this order.** The 2026-08-11 pass worked the `HS*`/`FS*` block and `DiffComp.pdf`
and stopped; the three targets below are untouched, and the first two are worth more than
everything that block had left in it.

### 1. ~~`old_exams/august2025.pdf`~~ — done 2026-08-11

**Prof. Laura Kobel-Keller, August 2025, 21 pages.** Mined front to back; see the accepted table.
It was the best target in the folder for four reasons, all of which held up: it is *Analysis II
alone* (title *Analysis II: mehrere Variablen*), so nothing had to be filtered out as
single-variable; it is **bilingual**, so every statement was quoted from the examiner's own English
rather than translated; it is the most recent paper here by roughly four years; and its
single-choice and multiple-choice sections convert directly into the true/false `exercise` style
already used in chapters 19 and 20.

**What is left in it, and why.** Twelve of the nineteen questions were taken. The other seven:

| Question | Verdict |
|---|---|
| Frage 11 (a sequence converging in one norm on `ℝⁿ`; can it diverge, or be unbounded, in the Euclidean norm?) | Both options are false because all norms on `ℝⁿ` are equivalent, which `02-metric-normed-inner-product/04-equivalence-of-norms.tex` is an entire section about, with `ex:3.9` already asking for the proof. |
| Aufgabe 12 (critical points of `x³/3 − y − x + y⁵/5`) | Routine Hessian classification. Chapter 12 carries six of these already, including two with a parameter. |
| Aufgabe 14 (swap the order in `∫₀² ∫_{y²}^{2√(2y)} f dx dy`) | **Already in the document.** It is `ex:change_order_integration`, transcribed from Sascha Brack's notes long before this pass. The exercise now carries an `\exinfo` recording that the exam sets the identical region, and the pass added the two-panel figure instead. |
| Aufgabe 15 b), c) (the sup-norm is a norm on `B(U,Y)`; a uniform limit of continuous maps is continuous) | Standard, and both are in chapter 2 and chapter 7 in substance. Only part a) was distinctive; it is `ex:kobel_local_banach_fixed_point`. |
| Aufgabe 18 (prove Fubini) | A "reproduce the lecture's proof" part; see the standing rejection at the foot of this file. |
| Aufgabe 19 (prove the Hessian test) | Same category, and we are **ahead** of it: the exam assumes `f ∈ C³`, our `thm:hessian_test` assumes `C²`. |

### 2. The three `Probeprfg` mock exams, two of which ship solution keys

None of these is cited in `content/`, and **the keys are the point**: of the papers mined on
2026-08-11, only `exercises_2024/mock.pdf` had a solution to check against, so every other solution
in the tables below rests on independent derivation alone.

| Problems | Key | Pages |
|---|---|---|
| `old_exams/fs2023/Probeprfg3.pdf` | `old_exams/fs2023/Probeprfg3_Lsg.pdf` | 4 + 6 |
| `old_exams/fs2023/2022/Probeprfg2.pdf` | `old_exams/fs2023/2022/Probeprfg2_Lsg.pdf` | 4 + 7 |
| `old_exams/fs2023/Probeprfg1.pdf` | none | 3 |
| ~~`exercises_2024/mock.pdf`~~ | `exercises_2024/mocksol.pdf` | ✅ **done 2026-08-11** |

Note the trap that the rest of this file warns about applies here too: `Probeprfg2` sits in
`fs2023/2022/`, not beside its siblings. Copy the path, do not reconstruct it.

**What the mock pass established, and what it costs the three above.** `exercises_2024/mock.pdf`
was expected to be the best of the four, and in one respect it was: it is the only source mined so
far that ships a key, and checking against one turned out to be worth more than expected, since it
surfaced two errors *in the official answers* rather than in ours (see the accepted table). But
roughly half of it was already in the document under `examFS24` provenance. The three `Probeprfg`
papers are Analysis I & II and by a different lecturer, so they carry no such risk of duplication —
which now makes them, on balance, the better targets. **Derive first, open the key second**, as
`style.md` requires: on the mock that rule is what made the two errata visible instead of
inherited.

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

## Accepted — 2026-08-11 pass, `august2025.pdf` (Prof. Laura Kobel-Keller)

Twelve blocks, ten chapters. Every question was read from a rendered page; `pdftotext` was used for
triage only. **This paper ships no solution key either**, so every solution below is an independent
derivation, exactly as for the block above.

| # | Question | Lands in | Form | Why it earns its place |
|---|---|---|---|---|
| 1 | Frage 1 | `06-completeness/01` `ex:kobel_cauchy_single_choice` | single choice | Option (b), *"has a limit if `X` is closed"*, is the sharpest form of the closed-relative-to-what confusion, and the chapter had nothing testing it. |
| 2 | Aufgabe 15 a) | `06-completeness/03` `ex:kobel_local_banach_fixed_point` | exercise | A genuine refinement of Banach: no complete domain, no self-map, replaced by one inequality on the first step. It is how the theorem is *actually* used in the proof of the inverse function theorem. |
| 3 | Frage 10 | `07-compactness/04` `ex:kobel_compactness_characterisation` | true/false | Puts "closed and bounded" against "complete and totally bounded" in one block, which `rem:boundedness_not_topological` argues for at length and nothing tested. |
| 4 | Frage 3 | `09-differential/02` `ex:kobel_differentiable_single_choice` | single choice | Option (b) drops *linearity* from the definition of the differential, which is the one word carrying its content. Option (c) is a stronger-than-needed error term. |
| 5 | Frage 4 | `13-lagrange/01` `ex:kobel_lagrange_single_choice` | single choice | The Lagrange system is inconsistent (`eˣ = 0`), so the problem is settled without ever knowing `f`. An inconsistent system as a legitimate outcome is not represented elsewhere. |
| 6 | Aufgabe 13 | `13-lagrange/01` `ex:kobel_sphere_meets_cylinder` | exercise | Sphere ∩ cylinder. Not the rejected routine-Lagrange kind: the two constraints eliminate two variables outright, and the lesson is to try solving the constraints *before* reaching for multipliers. |
| 7 | Frage 5 | `15-inverse-function-theorem/01` `ex:kobel_ift_single_choice` | single choice | Separates "some derivative is non-zero" from "the derivative is invertible", and rules out the mismatched-dimensions case in (a). |
| 8 | Aufgabe 17 | `16-implicit-function-theorem/01` `ex:kobel_conic_implicit_maximal_interval` | exercise | Local theorem, global answer: the implicit function theorem gives *some* interval, and solving the quadratic gives all of `ℝ`. The official hint says outright that no theorem is needed for the last part. |
| 9 | Frage 6 | `19-jordan-measure/01` `ex:kobel_diffeomorphic_jordan_measure` | single choice | A diffeomorphism preserves compactness, hence finiteness of measure, and nothing else. Three of the four options assert it preserves size. |
| 10 | Frage 7 | `19-jordan-measure/01` `ex:kobel_layer_cake` | single choice | **The layer-cake formula**, which computes an integral by slicing the range. It is the move that separates Lebesgue from Riemann, and `03-a-glimpse-of-lebesgue.tex` had no concrete instance of it. |
| 11 | Aufgabe 16 | `19-jordan-measure/01` `ex:kobel_ball_minus_lattice` | exercise | A ball in `ℝ⁴` minus the lattice points. The whole problem is noticing the removed set is *finite* after intersecting; everything else is assembling standard facts. |
| 12 | Frage 8, Frage 9 | `26-stokes/02` `ex:kobel_line_integral_yz_circle`, `26-stokes/03` `ex:kobel_irrotational_single_choice` | single choice ×2 | The first has a non-conservative field with zero work around one loop, which catches "curl ≠ 0 ⟹ non-zero answer". The second's true option is the weakest one, *"it may be that a potential exists"* — its distractors are the two standard over-readings of `curl V = 0`. |
| — | Frage 2 | `appendix-a-odes.tex` `ex:kobel_picard_lindeloef_single_choice` | single choice | Lipschitz **in the state variable**, not in the independent one. Options (b) and (c) differ only in which variable, and the appendix had nothing making that distinction explicit. |

### Not from the exams, but from the same pass

`content/19-jordan-measure/03-a-glimpse-of-lebesgue.tex` was written on the user's explicit
instruction after they asked whether Jordan measure and Lebesgue measure are the same thing. It is a
digression, stated without proofs, used nowhere later, with four easy `aiexercise`s. The scope
reversal that authorises it is recorded in `gemini.md`; the `aside` environment was added to
`main.tex` in the same pass and is documented in `style.md` and `build-and-preamble.md`.

## Accepted — 2026-08-11 pass, `exercises_2024/mock.pdf`

Ten blocks, eight chapters. Every problem was read from a rendered page (`pdftoppm`);
`pdftotext` was used for triage only. **This is the first source mined with a solution key**, and
every verdict below was derived first and compared afterwards, per `style.md`. All nine agree with
`mocksol.pdf` except where a divergence is recorded in an `ainote`, and there are two of those, both
against the key.

| # | Problem | Lands in | Form | Why it earns its place |
|---|---|---|---|---|
| 1 | Box 16 | `07-compactness/05` `ex:box_preimage_of_compact_not_compact` | box question | The section's three headline facts all run in the image direction. This is the one line showing the preimage direction is not among them, and it is what `ex:box_proper_map_not_diffeomorphism` needs to lean on. |
| 2 | Box 19 | `08-connectedness/01` `ex:box_intersection_disconnected_union_connected` | box question + figure | `cor:union_connected_common_point` makes unions easy and the chapter says nothing about intersections. An annulus crossed by a strip is why. Drawn as FIG-MOCK-19. |
| 3 | Box 17 | `15-inverse-function-theorem/01` `ex:box_smooth_bijection_rough_inverse` | box question | `x ↦ x³`: bijective, `C^∞`, inverse not differentiable at one point. Global good behaviour does not substitute for `g'(x₀) ≠ 0`. |
| 4 | Box 18 | `15-inverse-function-theorem/01` `ex:box_proper_map_not_diffeomorphism` | box question | The multivariable form of the one above, and the chapter's only *construct it* problem. Introduces properness, which nothing else in the document names. |
| 5 | Ex 8 | `16-implicit-function-theorem/01` `ex:graph_over_which_variable` | true/false | `∂G/∂x` never vanishes on `V = {y⁴+y² = x³+x}`, so one direction is free everywhere and all the content sits in the other. Part (d) is the rare case where the theorem fails **and** the answer is genuinely no, provable by hand. |
| 6 | Ex 9 | `17-submanifolds/02` `ex:level_set_of_a_wide_jacobian` | true/false | Six parts, six distinct ideas: a curve through the point that is not in `M`, the dimension count `3−2`, tangent versus normal, solving for two variables, and the open-mapping conclusion. The `ℝ³→ℝ²` counterpart of `ex:local_diffeo_parameter_alpha`. |
| 7 | Box 21 | `17-submanifolds/03` `ex:box_normal_to_a_graph_in_r4` | box question | The unit normal to a graph, set one dimension past the picture where it can no longer be read off a drawing. **The official key's first display is wrong** and its second is right; the `ainote` says which. |
| 8 | Ex 12 | `20-change-of-variables/02` `ex:gaussian_slab_alpha_asymptotics` | true/false | A product integrand split by Fubini into three one-dimensional pieces. Part (a) is the trap: at `α = 0` the `z`-integral diverges, and the printed value `√π` is what one Gaussian factor contributes. |
| 9 | Ex 11 | `21-gram-determinant/02` `ex:area_formula_two_maps` | true/false + `ainote` | **The best block in the pass.** The chapter defines the Gram determinant and never applies it to a map given by a formula; here `Ψ : ℝ²→ℝ³` is exactly the `m > n` case it was built for. And the exam's own formula sheet states the area formula with **no injectivity hypothesis**, which makes its part (a) false as printed — `Φ` is two-to-one. See below. |
| 10 | Ex 4 | `22-vector-calculus/02` `ex:differential_identities_true_false` | true/false | Part (d) is the product rule for the divergence, `div(u∇u) = \|∇u\|² + uΔu`, which the chapter never states and which is Green's first identity waiting to be integrated. The printed version puts the Hessian *matrix* where a scalar belongs. |

### Two errors found in the official key

Both were caught because the solutions here were derived before the key was opened, which is the
entire justification for that rule.

* **`Φ : (x,y) ↦ (xy, x²−y²)` and the area formula (Ex 11, part 1).** The key marks it **true**,
  and it is what the paper's own formula sheet gives. It is false: `Φ(−p) = Φ(p)`, so `Φ` is
  two-to-one, and for `E` the closed unit disc the image is the ellipse `4u²+v² ≤ 1` of area `π/2`
  while the integral returns `π`. The factor is exactly the number of preimages. Recorded as
  `note:area_formula_needs_injectivity` in `21-gram-determinant/99-solutions.tex`, which keeps both
  verdicts and says which is which.
* **The normal to a graph in `ℝ⁴` (Box 21).** The key prints two displays. The second is correct.
  The first lists a component `−∂₄φ(x)` and normalises by a sum including `∂₄φ(x)²`, but `φ` is a
  function of *three* variables, so there is no `∂₄φ` and the vector would have five entries.

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
