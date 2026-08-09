# Project state — Analysis II TA notes

⚠️ **This is the volatile file.** It records where the project has got to and which decisions
are settled. It is expected to change often; the style and build files are not. When something
here goes stale, edit it here — do not restate project status in the other files.

| Companion file | What lives there |
|---|---|
| `gemini.md` | Role, fidelity policy, tool usage — read first |
| `style.md` | House style: prose, notation, environments, provenance conventions |
| `build-and-preamble.md` | Build traps, `main.tex` facts, numbering, the preamble's environments |

## ⚠️ Priority — read first

**Get *Corsin Nick* all the way to a compiling PDF. Do not touch the other 16 tutors until
that exists.** Corsin alone is the deliverable; supplements are a bonus and come last.

Correct work order:

| # | Step | Reads PDFs? |
|---|---|---|
| 1 | Typeset Corsin — all 13 weeks + ODE appendix, into the topic chapter each belongs to | **yes, heavily** |
| 2 | Build & Verify: `latexmk` until `main.pdf` compiles clean | no |
| 3 | TikZ figures | only for a figure traced from a source page; invented ones, no |
| 4 | *Optional:* supplements from other tutors | yes — **not before step 2** |

Steps 1 and 2 are **done**: every week of Corsin's notes has been typeset and the document
compiles clean. New material now gets pasted into the topic chapter it belongs to, not appended
to a week.

## ⚠️ Settled 2026-08-09: AI-Notes are numbered and referenceable

On the user's instruction, `ainote` stopped being `\newtheorem*` and now has **a counter of its
own**, reset per chapter, so `\cref` prints `AI-Note 15.1`. It is deliberately **not** aliased to
the shared theorem counter, because that arrangement had already been tried and reverted (119
AI-Notes stepping it tore holes in the theorem numbering). See `build-and-preamble.md` for the
three-arrangement table.

⚠️ **This changed nothing about what belongs in one.** The two tests in `style.md` still decide
`ainote` versus `remark` versus a plain `%` comment, and \qt{I want to `\cref` it} is no longer
evidence of anything. Do not migrate content into AI-Notes just because it can now be pointed at.

## ⚠️ In progress: the 2026-08-09 prose revision

A full prose revision is under way, against four new rules now in `style.md` (strict em-dash
policy with the measured punctuation-budget table, the two-stage `ainote` test, the spoiler rule,
and the prose-architecture section). **Read those before continuing it.**

**Done:** `main.tex`'s seven `\part` paragraphs, and **Parts I and II (chapters 1--8)** in full.

| Measure | Before | ch. 1--8 after |
|---|---|---|
| Prose em-dashes | ~250 | **0** (25 `[N --- Title]` separators kept by design) |
| `ainote`s | 41 | 25 |

**Part III (chapters 9--11) is also done** as of the same pass: 2 prose em-dashes left (both
inside quoted script text, deliberately untouched), build clean at 281 pp.

**Part IV (chapters 12--14) is done** as of 2026-08-09: **0** prose em-dashes left (the only `---`
remaining in those three directories are LaTeX comments and `[6.2 --- Title]` exercise
separators), `ainote`s 8 → 7, build clean at 283 pp with the same 4 pre-existing `Overfull \hbox`
warnings and no new ones. What that pass also turned up, all four being the *same* kind of fault
worth hunting in 15--26 --- leftovers of the week → topic restructure:

* Two forward transitions pointing at the chapter the **old week order** placed next, not the one
  that follows now (`12-.../01-optimization.tex` announced Lagrange where the Hessian test now
  follows; `14-.../01-convexity.tex` announced the inverse function theorem, which is Part V's
  opener's job). Both rewritten.
* The inscribed-cube figure in `13-lagrange/` sat ~180 lines below the exercise whose eight
  candidates it draws (`ex:xyz_on_ball`), with two unrelated exercises in between. Moved up.
* A figure asserting something its coordinates contradicted, exactly as the *Verifying figures*
  note in `build-and-preamble.md` warns: the paraboloid/level-set picture in
  `12-.../01-optimization.tex` labelled a point **on a level circle** \qt{minimum} and drew the
  gradient there in the $-x$ direction rather than radially. Minimum moved to the centre, gradient
  made radial, re-rendered and inspected.
* One `ainote` gone stale on the restructure (`14-.../01-convexity.tex` said
  `def:sign_symmetric_matrix` comes \qt{later}; it is now in chapter 12, i.e. earlier). It was
  editor-facing anyway and is now a `%` comment.

Also in that pass: `13-lagrange/01-lagrange-multipliers.tex` was 600+ lines with no subsections
and now has two (`Second-order conditions on the constraint set`, `An application: the spectral
theorem`), each with a short lead-in; a nested `ainote` inside `rem:why_the_lagrangian` duplicated
`rem:lagrange_multiplier_sensitivity`'s shadow-price story and was replaced by a cross-reference,
with `\newterm{shadow price}` moved to the surviving remark (the glossary entry already points at
chapter 13, so nothing to change there).

**Part V (chapters 15--18) is done** as of 2026-08-09: **0** prose em-dashes left, build clean at
285 pp (283 before the additions below) with the same 4 pre-existing `Overfull \hbox` warnings.
The same restructure leftovers as in Part IV turned up again, which is now three parts running:

* Another transition aimed at the chapter the **old week order** placed next
  (`15-.../01-inverse-function-theorem.tex` announced the implicit function theorem from the
  middle of its own chapter, in nearly the words of ch. 16's stub). Cut.
* Another figure ~150 lines from what it illustrates: the $\cos$ sketch in ch. 15 sat *below*
  FIG-W06-03, while the prose under FIG-W06-03 calls that one the \qt{second} sketch. Moved up.
* Another stale cross-reference: `17-.../01-submanifolds.tex` said the cuspidal cubic was seen
  \qt{one chapter earlier}, which was true of the week order and is four chapters out now.
* An `ainote` carrying a `\label` (`15-.../01-...`), which was impossible to reference at the
  time and is mathematics anyway. Now `rem:inverse_function_theorem_intuition`.

**Content added** (the user's standing \qt{feel free to add stuff}):

* `18-geodesics/02-geodesics-on-submanifolds.tex`, a **new section**. \Cref{sec:geodesics} opened
  by promising that the same calculation works \qt{on a sphere or any other submanifold} and then
  never did it. The new section states and sketches the geodesic equation $c'' \perp T_{c(t)}M$,
  gives great circles versus circles of latitude on $S^2$, and sets an `aiexercise` on the
  cylinder with its solution in the chapter's **new** `99-solutions.tex`. This is also what the
  chapter was moved next to \cref{ch:submanifolds} for.
* A remark in ch. 18 on why constant speed is assumed and why it costs nothing, since the
  hypothesis is used twice in the computation and never commented on.
* An `ainote` in ch. 15 connecting `lem:lipschitz_perturbation_identity` to the theorem it
  exists to prove. **The lemma was stated, proved, and then never referred to again anywhere in
  the document.**

**Part VI (chapters 19--21) is done** as of 2026-08-09: **0** prose em-dashes left, build clean
at 285 pp with the same 4 pre-existing `Overfull \hbox` warnings. What it turned up:

* ⚠️ **A `\label` inside an `exercisesolution`, which `\cref` was rendering as \qt{Section 21.e}.**
  `exercisesolution` wraps `proof`, which has no counter, so this is exactly the silent
  misattribution `build-and-preamble.md` warns about, and it looked plausible enough to survive
  several passes. Now referenced with `\cpageref` (\qt{the solution on Page 221}), per the
  documented workaround. A regex sweep of `content/` found **only this one**, so it is not
  systemic --- but it is worth re-running the sweep after adding any labelled solution:
  `\\begin\{exercisesolution\}(\[[^\]]*\])?\s*\n\s*\\label` in multiline mode.
* **A spoiler above an exercise**, the third found so far: an `ainote` under \cref{ex:8.5} gave
  away the transformed domain for part 3 and the curved constraint for part 2, i.e.\ two of the
  three answers. Moved into `99-solutions.tex`, where the surviving half turned out to duplicate
  an `ainote` already sitting beside the solution.
* **Three stale chapter numbers in file headers** (chapters 19, 20 and 21 each announced
  themselves as the previous number, left over from the restructure). These are comments only,
  so nothing typeset was wrong.
* Two AI-Notes that were production logistics by Test 2 (one recording that answers were
  cross-checked against `Sol9_Analysis2_eng.pdf` and matched) are now `%` comments.

**First real use of the new AI-Note numbering.** A solution in ch. 21 read \qt{see the
\texttt{ainote} above}, leaking a LaTeX environment name into the typeset text because there was
no way to reference one. It now reads \qt{(\cref{note:9.1_coordinates_mislabelled})}, printing
\qt{AI-Note 21.5}. That is the shape of case the change was worth making for; it is not licence
to start labelling AI-Notes generally.

**Not yet done: chapters 22--26 and the four appendices.** Work chapter by chapter; do not
batch-substitute, for the reasons in `style.md`.

**Done out of order (user request): the dyadic step-function figure.** FIG-19-01 now sits inside
`def:riemann_integral_rn` in `content/19-jordan-measure/01-jordan-measure.tex`: two panels at mesh
$2^{-1}$ and $2^{-2}$, lower step function in blue, the $h-g$ gap in orange, over an increasing
$f$ so that the per-interval extrema are just the endpoint values. Arithmetic is checked in a
comment above the figure; the gap area halves from $0.350$ to $0.175$. Rendered and inspected.
The surrounding prose in that definition was revised with it; **the rest of chapter 19 was not**.

Two ordering faults of the kind worth hunting for in the remaining chapters, both found in
1--8: `07-compactness/00-chapter.tex` and `01-open-covers.tex` opened with the *same paragraph*
near-verbatim, and two notes disclosed exercise answers above the exercise
(`01-prerequisites/01-from-analysis-i.tex`, `03-visualizing-sets.tex`).

**How to work a chapter.** In this order, one chapter at a time, building between chapters:

1. Strict em-dash repair. **Prefer a full stop plus a connective** (`Therefore,` `Consequently,`
   `Hence,` `Note that`) over a semicolon or colon; the punctuation table in `style.md` shows both
   of those are already over budget against the reference project, so moving dashes onto them
   makes the prose worse, not better.
2. `ainote` triage by the two-stage test.
3. Spoiler relocation into that chapter's `99-solutions.tex`.
4. Chapter-opener prose, only where it earns its place.
5. Re-break overlong displays into `align` / `split`.

⚠️ **After any batch that converts an `ainote` into a `remark`, grep for prose that still says
\qt{an ainote} or \qt{an AI-Note}.** That cross-reference goes stale silently and the build stays
clean. It bit once already, in `06-completeness/01-completeness.tex`, pointing at a block that had
been reclassified earlier in the same pass.

⚠️ **Build to a jobname you are not currently viewing.** `-jobname=check` is the documented escape
from a locked `main.pdf`, but `check.pdf` gets locked in turn by `pdftoppm` while inspecting
figures, and `latexmk` then dies with *"I can't write on file"*. Use `-jobname=chk2` (or any fresh
name) when that happens.

**Also added: FIG-06-01, cobweb diagrams for the fixed point iteration**
(`06-completeness/03-contraction-mappings.tex`, after the uniqueness proof). Chapter 6 previously
had **no figure at all**, despite the Banach proof being a construction whose content is entirely
visual in one variable. Two panels: a genuine contraction ($L=0.45$) staircasing to $x^*$, and
$f(x)=x+0.12$ with slope exactly $1$, whose graph is parallel to the diagonal so no fixed point
exists. Arithmetic checked in a comment; rendered and inspected.

**Content gaps found by audit in chapters 1--11, not yet filled** (ranked):

| Gap | Where |
|---|---|
| The British Rail metric's topology remark *describes a picture in words* (every non-zero point isolated, the origin normal) with no figure. Same fault as the flat-torus one already fixed. | `02-.../02-metric-spaces.tex`, `ex:british_rail_metric` |
| Chapters **1, 4, 5 and 11** have **zero** `aiexample` and **zero** `aiexercise` between them. Ch. 11 (Taylor) is the sorest: a drill computing an expansion by 1D substitution would earn its place. | those four chapters |
| Chapter 5 has one figure only, and none for the Lipschitz $\Rightarrow$ uniform $\Rightarrow$ continuous hierarchy. | `05-continuity/` |

Two things found and deliberately left for that pass:

* Four pre-existing `Overfull \hbox` warnings, none of them in chapters 1--11:
  `24-differential-forms/02-exterior-derivative.tex` (the `dx \wedge \dots` chain, 101pt over),
  `26-stokes/02-greens-theorem-conservative-fields.tex`, `26-stokes/04-stokes-theorem.tex` and
  `appendix-a-odes.tex`.
* `\operatorname{span}` is written out 22 times with no macro. Worth a
  `\DeclareMathOperator{\spn}{span}` in the preamble plus a sweep, but that touches chapters
  outside the current pass, so it was not started.

## The five things that matter

1. **Corsin Nick is the blueprint.** His notes define which results appear and how they are
   proved. Everyone else is mined for gaps only. (They no longer define the document's
   *structure* — chapters are topics now — but they remain the mathematical blueprint.)
2. **Merge by topic, never by date — and never by the other tutor's week number either.**
   The ultimate authority for topic→chapter is `content/` itself: grep for the section label,
   or read the chapter list in `main.tex`.

   The trap is subtler than dates, and the restructure removed only half of it. Week numbers no
   longer name our files, but a tutor's own file names still carry them, and **a file named
   `Week_03_...pdf` is not about our third chapter, or about any one chapter.** Tutors run their
   own schedule, repeat material across sessions, and split topics differently from Corsin.
   Observed directly:
   - Sascha Brack's `Week_03_Notes_Monday.pdf` and `Week_03_Notes_Friday.pdf` both consist of
     material belonging to **our Week 2** (compactness corollaries, Heine–Borel, connectedness,
     normed and inner-product spaces) plus a preview of **our Week 4** (differentiability, the
     implication diagram, the checking recipe). Almost none of it is our Week 3.
   - His `Week_02_Notes_Friday_Updated.pdf` already reaches compactness and Heine–Borel, i.e.
     our Week 3.
   - His `Week_04_Notes_Friday_Updated.pdf` is ~80% a repeat of his own Monday file; the only
     new content is the chain-rule variable graph.
   - Diego Torres Tejeda's files are named by **date**, and route by topic to scattered weeks:
     `16.03` supplied our Week 3, `30.03` our Week 7.

   Two consequences. **(a)** Open a supplementary file expecting to find *some* topic, not a
   particular week's topic, and file each piece where the topic lives. **(b)** Heavy repetition
   between a tutor's own files is normal — do not assume a file is new material because it
   carries a different week number. Skim for what is *added*.
3. **Direct LaTeX with Fine Provenance.** Typeset directly into the right section file under
   `content/NN-topic/`, with precise `% Source: Corsin Nick/Class Notes/Week N.pdf, p. M`
   comments on every section. Source comments still name the tutor's week — that is where the
   material came from, and it does not change because our chapters were reorganised.
4. **Never silently correct a source.** Flag it inline with `\begin{ainote}`, at the spot it
   concerns. That is the entire mechanism — there is no open-questions file to update.
5. **Source folders are read-only.** The 17 tutor folders and `exercises/`
   are inputs. Output goes to `content/`.

## Git — never `git add -A`

Multiple sessions share one worktree. `git add -A` stages whatever is on disk,
including another session's in-flight edits. **Stage only the paths you touched:**

```bash
git add -A                                          # no
```

Check `git status --short` before every commit.

## Week numbering trap

The cover of `Corsin Nick/Class Notes/Week 2.pdf` reads *“Class notes Week 1”*.
**The file name is canonical** — it agrees with the other tutors and the
exercise-sheet numbers.

## Reference documents

| File | What it settles |
|---|---|
| `Analysis_II_Script_v1.pdf` (project root) | The official course script. The authority our theorems are **checked against** — not a blueprint to transcribe. See *The official script* below. |
| `exercises/ExN_Analysis2_eng.pdf` | The official problem sheets — quoted verbatim, never paraphrased. |
| `exercises/SolN_Analysis2_eng.pdf` | Official solutions, used only to **check** a solution you derived first. |

**Supplement coverage is not tracked in a file.** A `supplements.md` recording which of the 16
non-Corsin tutors had been mined was retired on 2026-08-09: it had gone stale, and any tutor
worth revisiting needs a fresh pass rather than a resumed one. Measure coverage by grepping
`content/` for `% Source:` / `% Supplement:` / `% Quelle:` comments naming the tutor.

## The official script — surveyed and mined out

*Analysis II: Several Variables*, Joaquim Serra, ETH FS 2024, 207 pp. It continues the
Analysis I numbering, so its chapters run **9–15**, not 1–7.

**Status: complete.** A full survey plus five enrichment sessions finished 2026-08-07. Every
divergence, gap, exercise and example the survey identified has been transcribed into
`content/`, checked against a rendered page, and build-verified. **There is no outstanding work
here** — the detailed session log was retired with `script-coverage.md`. What survives is below,
because it is the part that stays useful.

**If you ever go back to the script:**

* **Page offset: printed page = PDF page − 4.** Cite the **printed** page, since that is what
  the text's own numbering refers to.
* Provenance comment: `% Supplement: Analysis_II_Script_v1.pdf, p. 27`.
* ⚠️ **Never quote a formula from the extracted text.** `pdftotext` eats `∂`, `≤`, `∇`, `∈` and
  most Greek. Render the page and read it.

**Standing decision (2026-08-06, user): enrich existing sections only.** Topics the script
covers and we have no section for do **not** get new sections. Recorded here so the choice stays
visible and reversible:

| Script | Why skipped |
|---|---|
| §9.1.4 The reals as the completion of ℚ | The script marks it *extra material*; belongs to the sibling *Grundstrukturen* project. |
| §11.5 Fundamental theorem of algebra via minimization | An application of Weierstrass rather than Analysis II content; needs its own section. |
| Thm 14.22 + Ex 14.24–14.30 Jordan curve theorem | A full section's worth. We already state Jordan–Brouwer where it is needed. |
| §13.7 Partition of unity on compact submanifolds | We build partitions of unity a different, lighter way in ch. 25. |
| §15.4 Differentiability w.r.t. initial conditions | We already have the theorem in `appendix-a-odes.tex`. |
| §14.4 A glimpse into differential forms | We are *ahead* of the script here. |

Reversed once, for the completion-of-a-metric-space construction (script §9.1.3), now
`content/06-completeness/02-completion-of-a-metric-space.tex`. The §9.1.4 ℝ-from-ℚ
specialisation is still out of scope. **If any other entry is later wanted**, the FTA argument
(§11.5) has the best value-to-length ratio: about a page, and it sits naturally at the end of
`12-extrema-hessian/`.

**Where we are ahead of the script — do not "fix" these by cutting them.** Differential forms
(chs. 24–25: the script has four unproved paragraphs, we have a full treatment); geodesics
(ch. 18, no counterpart); our convexity characterisations (more equivalent conditions than the
script's two); the Hessian test stated for `C²` rather than `C³`, handling the degenerate case;
Lagrange multipliers in the linear-dependence form with a constraint-qualification
counterexample, where the script gives the `λ₀`-normalised form with no qualification at all.

**Errors found in the script and not yet flagged anywhere.** The serious two (E2, a false
statement of Weierstrass; E6, a false `rot(φF)` identity set as an exercise) are already handled
with `ainote`s. These remain unflagged, being cosmetic — worth not copying if you touch the
corresponding result:

| Where | Problem |
|---|---|
| Def 9.52(1), p. 18 | ε–δ condition ends `f(B(x,δ)) ⊆ B(f(y),ε)`; there is no `y` — should be `f(x)`. |
| Def 13.2, p. 89 | Injective map typed `a : {1,…,N} → ℤ^k` (should be `ℤⁿ`); union uses side length `2^{-k}` where the text fixes `2^{-p}`. Propagates into Lemma 13.20. |
| Ex 10.21, p. 48 | In the `∂/∂x` line, `2e^{u+v}·0` should be `2e^{u+2v}·0`. Multiplied by zero, so answers are right. |
| Thm 15.33, p. 188 | Hypothesis says `(f_k)` bounded in `C(K,ℝ)`, conclusion says `C(K,ℝᵐ)`. Ours uses `ℝᵐ` throughout and is consistent. |
| Prop 11.24, p. 74 | Typed `f : C²(U)` for `f ∈ C²(U)`. |

## Carried-over task: unproved results to check against the sources

Opened 2026-08-09, on the user's point that \qt{the course skips this} is a claim, not prose, and
should not be written until someone has opened the source. **Nothing here has been checked yet.**
For each, open Corsin's PDF and `Analysis_II_Script_v1.pdf`; if a proof is there, transcribe it
and cut the note down to a pointer.

| Result | Where | What the text currently claims |
|---|---|---|
| Inverse function theorem | `15-.../01-inverse-function-theorem.tex`, `ainote` after `lem:lipschitz_perturbation_identity` | only that it is stated **in this document** without proof, which is what was verified. The `%` comment above it names the files to open. |
| Ascoli--Arzelà | `07-.../06-ascoli-arzela.tex`, l. 121 | \qt{The course does not prove this theorem} --- asserted in **body prose**, unverified, and on both counts what the new `style.md` rule forbids. |
| Sequential $=$ topological compactness | `07-.../03-sequential-vs-topological.tex`, l. 9 | \qt{The course states this equivalence but never proves it} --- same two faults. |

The two chapter-7 entries were found by grep during the Part V pass and deliberately **not**
fixed then, to avoid reopening a signed-off chapter mid-pass. They are small: move each into an
`ainote` and soften it to what has actually been verified.

## Carried-over provenance task

Two blocks carry `% Generator:` only because their source could not be verified. If you find the
real source while mining, upgrade the comment to a `% Source:` with a page number — **verify by
opening the file, never upgrade on a hunch:**

* the Lagrange sensitivity remark in `content/13-lagrange/01-lagrange-multipliers.tex`
  (possibly Toby Lane, `class-document.pdf`);
* the graph arc-length proposition and astroid example in
  `content/21-gram-determinant/03-length-of-a-curve.tex`
  (possibly Linus Lüchinger, `Slides-04-30.pdf`, p. 3).

⚠️ **Never invent a path.** A previous pass cited `Fabio Guger/Class Notes/Week_07.pdf`; that
tutor's files are date-named and there is no `Class Notes/` subdirectory. List the directory and
copy the real filename, or use `% Generator:` and no `% Source:` at all.

## Exercises

Each week opens with the official problem sheet (`exercises/ExN_Analysis2_eng.pdf`).

- **Quote every problem statement verbatim.** Do not paraphrase; attribute the sheet.
- **Tag each problem** with its priority from Corsin's *Recommended exercises* colour code:

  | Corsin’s marker | Tag |
  |---|---|
  | blue ▨ | `**important**` |
  | orange ▨ | `**semi-important**` |
  | red ▨ | `**optional**` |
  | official `(*)` | `**harder**` |

- ⚠️ **Standing decision: do NOT mine the other TAs' exercise-sheet hint files.** This applies
  to `Sascha Brack/Ex Sheet Hints/` and `Simon Kamps/SerieNNHints.pdf`. It was tried once, for
  sheet 8 (see `content/19-jordan-measure/` and `content/appendix-d-problem-sheets.tex`, and
  the two per-exercise hints) — that material stays, but **do not add more of it**. The files
  are annotated copies of the official sheet rather than independent notes, so the yield is
  cross-TA priority agreement plus short margin hints, which is not worth the reading cost or
  the clutter next to Corsin's own priority table. Corsin's priorities are the ones the document
  follows.
- Corsin’s hint follows the statement, attributed and page-pointed.
- TAs’ worked solutions are presented; `SolN_Analysis2_eng.pdf` is used to **check**

## German mirroring

The document is English, but German technical terms are mirrored on **first introduction**
so it can be used alongside German lecture and exercise material:

```latex
a \newterm{compact} set (\germanterm{kompakte Menge})
the \newterm{implicit function theorem} (\germanterm{Satz über implizite Funktionen})
```

`\germanterm{...}` is defined at `main.tex:189`. Only on first introduction — never
repeated. Canonical German wording comes from **Jérôme Paschoud**’s topic-named files.
Every term pair also goes into `content/appendix-b-glossary.tex`, whose third column is the
**chapter** of first introduction (a letter there means an appendix).
(An earlier two-stage pipeline wrote these into Markdown transcripts first; that stage was
dropped -- there is no `transcript/` directory. Write the LaTeX form directly.)

## Document skeleton — SETTLED (restructured; this replaces the week-based skeleton)

**Part = thematic block. Chapter = topic. Section = one file. Day and week = gone.**

The document used to be one chapter per teaching week. It is now organised by content: seven
`\part`s over 26 topic chapters, each chapter a directory, each section its own file. The point
of the change was that a week is an accident of the timetable — compactness was split across two
of them and stitched back together with a back-pointer — whereas a chapter you can name is
something a reader can look up.

```
content/
  07-compactness/
    00-chapter.tex      <- \chapter + \label + a short intro + nothing but \input lines
    01-open-covers.tex
    02-compact-subsets.tex
    03-sequential-vs-topological.tex
    04-heine-borel.tex
    05-why-compactness-matters.tex
    99-solutions.tex    <- the chapter's single \section{Solutions}
```

`main.tex` holds the `\part` lines and one `\input` of each `00-chapter.tex`, in order. **To add
a chapter:** make the directory, write `00-chapter.tex`, add the `\input`. **To add material to
an existing chapter:** drop a new `NN-*.tex` beside its siblings and add one `\input` line to
that chapter's stub. Nothing else has to be touched — that is the whole reason for the layout.

**Numbering.** Directory prefixes are ordering only; the real chapter number comes from the
`\input` order in `main.tex`. `\part` deliberately does **not** reset `\thechapter`, so chapter
numbers — and therefore theorem numbers, which are built from them — run continuously 1–26.

**Every file carries its provenance.** The first line of each is an `% Originally:` comment
naming the old week file and section it came from; the `% Source:` comments beneath are the
tutor's own, unchanged, and still cite his week-numbered PDFs. Those two kinds of comment answer
different questions — where this text used to sit in *our* document, and where it came from in
*his* notes — and both are worth keeping.

**Heading Styles & Suffixes:**
* **Colors:**
  - Part Title: `ThemePurple` (`PartTitleText`), number in `OliveGreen` (`PartNumberText`)
  - Section Title: `MidnightBlue` (`SecTitleColor`)
  - Subsection Title: `MidnightBlue` (`SubSecTitleColor`)
  - Subsubsection Title: `TextBoldColor` (`SubSubSecTitleColor`)
  - Green `(...)` Suffix: `OliveGreen` (`SecNumberColor`)
* **Suffix Format:** All numbered headings carry a green suffix:
  - `\chapter{...}` -> `Title (Chapter 7)`, and `(Appendix C)` after `\appendix`
  - `\section{...}` -> `Title (Section 7.a)`
  - `\subsection{...}` -> `Title (Subsection 7.a.1)`

**Avoid a chapter that is one section repeating the chapter's own title.** If a chapter has
exactly one section and they share a name, either split the section or let the chapter absorb it.

**Retired macros — do not reinstate.** `\session{Monday}`, `\exercisesheet{N}` and
`\continuedfrom{label}` all existed to prop up the week structure and are gone from `main.tex`.
There is no day to mark, the problem sheets are dissolved, and no topic is split across a
boundary that would need a back-pointer.

**Problem sheets are dissolved.** Each problem sits with the material it tests, so a single
sheet's problems can be spread over several chapters, and its solution is in that chapter's
`99-solutions.tex`. `content/appendix-d-problem-sheets.tex` restores the sheet view: one table
per sheet, with Corsin's priority markings and his own comments, and a column pointing at the
section that now hosts each problem. **When you transcribe a new problem, add it to that table.**

**File naming:** `content/NN-topic-slug/NN-section-slug.tex`, with `00-chapter.tex` for the stub
and `99-solutions.tex` for the solutions. There is no `transcript/` stage and no
`content/exercise-sheets/` directory -- typeset straight into the section file.
