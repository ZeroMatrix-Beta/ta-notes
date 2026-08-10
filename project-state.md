# Project state — Analysis II TA notes

⚠️ **This is the volatile file.** It records where the project has got to and which decisions
are settled. It is expected to change often; the style and build files are not. When something
here goes stale, edit it here — do not restate project status in the other files.

⚠️ **No to-do lists in this file.** It records *decisions* and *facts*, not intentions. Earlier
revisions carried three of them ("carried-over task", "carried-over provenance task", "content
gaps not yet filled"), and every one had gone partly stale before anyone returned to it — one
listed two notes as sitting in body prose when both had been `ainote`s for some time. A task
worth doing is worth doing or dropping; it is not worth recording here. If you find work you
cannot finish, finish what you can and say so in your reply to the user.

| Companion file | What lives there |
|---|---|
| `gemini.md` | Role, fidelity policy, tool usage — read first |
| `style.md` | House style: prose, notation, environments, provenance conventions |
| `build-and-preamble.md` | Build traps, `main.tex` facts, numbering, the preamble's environments |

## Where the document stands

**Corsin Nick is fully typeset and the document builds clean at 300 pages**, with three
`Overfull \hbox` warnings; they are tabulated, with the method for attributing them correctly, in
`build-and-preamble.md`. Every week of his notes sits in the
topic chapter it belongs to. New material goes into the chapter it belongs to, never appended
to a week.

**The tracked `main.pdf` is current at 310 pages** (rebuilt 2026-08-10, on the user's
instruction, after all of the work below). It was eighteen pages behind the source before that.

⚠️ Note for the next rebuild: the first attempt hit the locked-file trap in
`build-and-preamble.md`, `latexmk` dying with *"I can't write on file `main.pdf`"* because a
viewer held it open. Once the viewer was closed, **`latexmk` still reported the same failure**
until it was re-run with `-g`: it had cached the failed state and would not retry on its own.
Reach for `-g` rather than assuming the file is still locked.

**The exercise imbalance across the second half was measured and partly corrected (2026-08-09/10).**
Chapters 2–16 averaged about seven exercises each, chapters 17–26 about two, while the worked-example
count ran the other way. The cause is not neglect: sheets 1–3 have no priority page so all 22
problems were transcribed, and from sheet 4 on only Corsin's blue and orange ones were. Rather than
reopen that decision, the gap is being closed with authored `aiexercise`s. Done so far: four in
ch. 24 (which had none at all, and now has its own `99-solutions.tex`), three in ch. 20 (a
substitution read off the integrand, an order swap that is impossible one way, and Frullani's
integral via Feynman's trick), two in ch. 23 (a divergence-theorem drill and one open surface that
has to be capped), two in ch. 18 (the fundamental lemma of the calculus of variations, and the
variation redone without the constant-speed hypothesis, both closing gaps the chapter's own
remarks admit to), two in ch. 22 (a counterexample to the script's mis-stated curl product rule,
and which of two fields is a gradient), two in ch. 25 (the pullback of the area form, and
`dx∧dy` over the two hemispheres). **Every exercise in all 26 chapters has a solution**, audited
2026-08-10; the count of `exercise` plus `aiexercise` matches the count of `exercisesolution` in
every chapter directory.

**Figure density was measured on 2026-08-10, and two of the thinnest chapters were addressed.**
Ch. 18 had one figure in 300 lines and none for the equation the chapter exists to prove; it now
has a two-panel sphere showing a great circle against a circle of latitude. Ch. 22 illustrated the
divergence and the curl but not the gradient; it now has a contour picture carrying both readings
of `\nabla f`. The other three outliers were closed the same day: **ch. 26** had nothing in its
main section while `thm:stokes_3d` stated its orientation convention in words, and now has the
right-hand-rule figure plus `rem:right_hand_rule_as_cross_product`, which reduces "the surface is
to the left" to `inward = ν × τ`; **ch. 05** defined continuity three ways with no picture and now
has the ε–δ one; **ch. 06** had only the Banach iteration and now shows `1/n` drawn twice, in
`[0,1]` and in `(0,1]`, differing only in whether the limit belongs to the space.

⚠️ **Every figure drawn in this pass was wrong on the first attempt in a way the source did not
show**, and rendering caught all of them: a normal-component arrow lying exactly on the radius
line it was drawn beside, so the two collapsed; a great circle asserting `c''` is radial with no
vector on it; three separate label collisions. This is the *Verifying figures* rule in
`build-and-preamble.md` earning its keep for the second pass running. Never commit a TikZ figure
you have not looked at.

**The 2026-08-09 prose revision is complete**, over all 26 chapters and all four appendices,
against the em-dash policy and punctuation budget in `style.md`. Zero prose em-dashes remain in
`content/`. What still matches `---` there is exactly three things, all of them deliberate:
LaTeX comments, `[11.5 --- Radial vector fields]` exercise separators and chapter/section title
separators, and table cells where `---` means "no entry".

**The 2026-08-09 pass against `lec_notes.pdf` is complete.** It did three things. It adopted the
lecture notes' norm convention document-wide (single bars Euclidean, double bars everything else;
see `style.md`, and `ainote:norm_convention` for the reader-facing statement). It checked the
remaining notation, finding our derivative and gradient conventions already in agreement and two
deliberate divergences worth keeping, both now flagged for the reader (`B_r(x)` against the
lecture's `B(x,r)`; `\Hess` against `Hf`). And it added six statements the document was missing:
equivalence of norms with its two corollaries (new section, ch. 2), the Hilbert–Schmidt length
bound, componentwise differentiability, `C^1` implies locally Lipschitz, vanishing differential
on a connected set, and compact implies closed.

⚠️ It also **falsified two claims about the course** that were sitting in the typeset text: that
the course never introduces Lipschitz continuity (Definition 9.55 does) and that it never states
the mean value theorem (Theorem 10.28 is it). Both are corrected. This is the rule in `style.md`
about not asserting what you have not opened, earning its keep a second time.

Not everything in the notes was pulled in, deliberately: `C^k` closure under sums, products and
compositions (Prop 10.36) is routine and unstated here; the entries in the *Enrich existing
sections only* table below stay skipped. Proofs were not replicated where a statement plus a
pointer does the work — the inverse function theorem is still unproved here, and now says so
accurately.

**All TikZ figures have been rendered and inspected.** That pass was worth more than expected:
in Part VII alone, four of the ten figures were wrong, three of them mathematically rather than
cosmetically, and none of the four could have been caught by reading the source. See
*Verifying figures* in `build-and-preamble.md`, which is the rule that pass produced.

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

## ⚠️ Never invent a path

A previous pass cited `Fabio Guger/Class Notes/Week_07.pdf`; that tutor's files are date-named
and there is no `Class Notes/` subdirectory. List the directory and copy the real filename, or
use `% Generator:` and no `% Source:` at all. **Never upgrade a `% Generator:` to a `% Source:`
on a hunch** — open the file first. Two blocks currently carry `% Generator:` precisely because
their source could not be verified, and that is the correct state for them to be in, not a
defect to be tidied away.

## ⚠️ Do not claim what you have not checked

"The course skips this" is a claim about a source, not a piece of prose, and it does not
belong in the document unless someone has opened that source. Where the honest statement is
about our own materials, say that instead: *"None of the transcribed notes prove this theorem"*
is checkable from `content/`, whereas *"the course does not prove this theorem"* is not.

## Settled decisions

**Appendix C holds two quizzes, and is titled accordingly (2026-08-10).** It was
*Mid-Semester Repetition Quiz*, one section, seven questions from Corsin reaching only
`ch:submanifolds`. It is now *Repetition Quizzes*: `sec:repetition_quiz` is Corsin's, unchanged,
and `sec:repetition_quiz_integration` is seven authored questions covering
`ch:jordan_measure`–`ch:stokes`, so the pair spans the document. The chapter and section labels
did not change, and the only external `\cref` into the appendix (`q:quiz_q4`, from chs. 9 and 10)
still resolves. The second quiz is authored, not transcribed: it carries `% Generator:` and says
so to the reader in its opening `ainote`, since the first section credits its questions to
Prof.\ Serra and Prof.\ Lang and the two must not be confused.

**Ch. 18 says in the document that it is not lecture material (2026-08-10, user).**
`ainote:geodesics_beyond_the_course` now states both halves of the warning: Corsin's own
"not exam relevant" marking, and the fact that the lecture notes have no counterpart. That
second claim was **checked, not assumed**, per the rule two sections above: `geodesic` occurs
exactly once in the whole of `lec_notes.pdf`, in Example 9.14 on printed p. 5, naming the
great-circle metric on the sphere without saying why that arc is shortest; the page was rendered
and read. Nothing in the course computes a geodesic and the calculus of variations does not
appear in it. The other *ahead of the script* entries listed below carry no such reader-facing
note yet.

**Two ch. 22 AI-Notes were reclassified as remarks (2026-08-10).** The source/sink and
paddle-wheel intuition blocks were `ainote`s, but both are plain mathematics with no source
commentary in them, and both contain a `\newterm`, which `style.md` names as the reliable smell
of a misfiled remark. They are `remark`s now, with titles. Neither was labelled, so no `\cref`
moved. This is Test 1 in `style.md` applied, not a new decision.

**AI-Notes are numbered and referenceable (2026-08-09).** `ainote` has a counter of its own,
reset per chapter, so `\cref` prints `AI-Note 15.1`. It is deliberately **not** aliased to the
shared theorem counter; that was tried and reverted, because 119 AI-Notes stepping it tore holes
in the theorem numbering. See `build-and-preamble.md` for the three-arrangement table.

⚠️ This changed nothing about *what belongs in one*. The tests in `style.md` still decide
`ainote` versus `remark` versus a plain `%` comment, and "I want to `\cref` it" is not
evidence of anything. Do not migrate content into AI-Notes just because it can now be pointed at.

**Two German macros, and they are not interchangeable (2026-08-09).** `\germanfor{X}` prints
`(German: „X")` and carries its own parentheses, for mirroring an English term just introduced.
`\germanterm{X}` prints a bare `„X"`, for a German word mentioned as the subject of a sentence.
Until this date only `\germanterm` existed and the 101 mirroring sites wrote `(\germanterm{X})`
by hand. Only `\germanfor` entries belong in the glossary.

**`main.pdf` is tracked (2026-08-09).** `.gitignore` un-ignores it specifically, so the built
document travels with the source. Every other root PDF stays ignored. Note the cost: each
rebuild that changes it adds a ~2 MB blob to history permanently.

**Enrich existing sections only (2026-08-06, user).** Topics the official script covers and we
have no section for do **not** get new sections:

| Script | Why skipped |
|---|---|
| §9.1.4 The reals as the completion of ℚ | Marked *extra material*; belongs to the sibling *Grundstrukturen* project. |
| ~~§11.1.5 Fundamental theorem of algebra via minimization~~ | **Reversed 2026-08-10 (user).** Now `content/12-extrema-hessian/03-fundamental-theorem-of-algebra.tex`. |
| Thm 14.22 + Ex 14.24–14.30 Jordan curve theorem | A full section's worth. We already state Jordan–Brouwer where it is needed. |
| §13.7 Partition of unity on compact submanifolds | We build partitions of unity a different, lighter way in ch. 25. |
| §15.4 Differentiability w.r.t. initial conditions | We already have the theorem in `appendix-a-odes.tex`. |
| §14.4 A glimpse into differential forms | We are *ahead* of the script here. |

Reversed **twice**. First for the completion-of-a-metric-space construction (script §9.1.3), now
`content/06-completeness/02-completion-of-a-metric-space.tex`. Then, on 2026-08-10, for the FTA
argument, which this table had itself singled out as the entry with the best value-to-length
ratio. It is now `sec:fundamental_theorem_of_algebra`, the third section of
`12-extrema-hessian/`, and the old reason for skipping it ("an application of Weierstrass rather
than Analysis II content") turned out to undersell it: Weierstrass supplies only the *first* half,
that the infimum is attained. The second half is an optimality argument at a minimiser where the
deciding term is of order `ℓ`, the first non-vanishing coefficient after `b₀`, with nothing
bounding `ℓ` in advance. That is precisely what chapters 11 and 12 cannot reach with first- and
second-order conditions, so the section belongs to this chapter rather than merely fitting in it.

**The four remaining entries above stay skipped**, and no further reversal is pending.

**Do not mine the other TAs' exercise-sheet hint files.** This applies to
`Sascha Brack/Ex Sheet Hints/` and `Simon Kamps/SerieNNHints.pdf`. It was tried once, for
sheet 8 — that material stays, but no more is added. The files are annotated copies of the
official sheet rather than independent notes, so the yield is cross-TA priority agreement plus
short margin hints, which is not worth the reading cost or the clutter next to Corsin's own
priority table. Corsin's priorities are the ones the document follows.

**Supplement coverage is not tracked in a file.** A `supplements.md` recording which of the 16
non-Corsin tutors had been mined was retired on 2026-08-09: it had gone stale, and any tutor
worth revisiting needs a fresh pass rather than a resumed one. Measure coverage by grepping
`content/` for `% Source:` / `% Supplement:` / `% Quelle:` comments naming the tutor.

## Git — never `git add -A`

Multiple sessions share one worktree. `git add -A` stages whatever is on disk, including another
session's in-flight edits. **Stage only the paths you touched**, and check `git status --short`
before every commit.

## Week numbering trap

The cover of `Corsin Nick/Class Notes/Week 2.pdf` reads *"Class notes Week 1"*.
**The file name is canonical** — it agrees with the other tutors and the exercise-sheet numbers.

## Reference documents

| File | What it settles |
|---|---|
| `lec_notes.pdf` (project root) | **The official lecture notes**, and the file to cite from now on. 239 pp, dated 27 July 2026. The authority our theorems and notation are **checked against** — not a blueprint to transcribe. |
| `exercises/ExN_Analysis2_eng.pdf` | The official problem sheets — quoted verbatim, never paraphrased. |
| `exercises/SolN_Analysis2_eng.pdf` | Official solutions, used only to **check** a solution you derived first. |

### `Analysis_II_Script_v1.pdf` is the same document under its old name

Confirmed by the user, 2026-08-09. Fifty `% Supplement: Analysis_II_Script_v1.pdf` comments across
27 files still carry the old name; they were left alone, and **they are not wrong**. Use
`lec_notes.pdf` in anything you write.

Do not assume an old citation's page number lands where you expect, though — the two names were
not always used with the same page convention, and the file itself has been revised. If a page
matters, open it.

* **Page offset: printed page = PDF page − 5.** Cite the **printed** page.
* Provenance comment: `% Supplement: lec_notes.pdf, p. 26`.
* ⚠️ The `pdftotext` warning below applies to this file. Render the page and read it.

### The lecture notes — surveyed three times

⚠️ **The third survey (2026-08-10) falsified the previous heading, which read "mined out".** A
walk down the lecture notes' own table of contents, section by section against `content/`, found
**§13.2.5 Improper integrals** (printed pp. 124–125) with no counterpart here. It is not a
skip-by-decision: no tutor covers it, Corsin never reaches it, and it was not in the
*Enrich existing sections only* table. Worse, **the document was already using the notion in four
places without defining it** — `ex:improper_integral_polar` asserted in so many words that "its
Riemann improper integral is well-defined", `ex:gaussian_integral_polar` integrated over
`ℝ²`, `ex:ai_frullani` over the half-line, and `ex:10.3` (Gabriel's horn) over `[1,∞)`. Now
`content/19-jordan-measure/02-improper-integrals.tex`: Definition 13.55 as
`def:improper_integral`, Lemma 13.56 as `lem:improper_integral_as_limit` with proof, and an
`aiexercise` running the disk and square exhaustions of the Gaussian against each other, which is
the argument `ex:gaussian_integral_polar` was making implicitly all along. It also lets the
document say why `ex:feynman_dirichlet_integral` is the odd one out: `(sin x)/x` changes sign, so
`∫₀^∞ (sin x)/x` is not an improper integral in this sense at all.

Two lessons worth keeping. **A grep for a topic name is not a survey** — "improper" *did* occur in
`content/`, four times, which is exactly why the gap survived two passes: the word was present and
the definition was not. Walk the source's table of contents instead. And **a section the document
silently depends on is worth more than a section it merely omits**; the other entries in the
skip table are genuinely optional, this one was load-bearing.

The rest of the comparison came out clean: §10.2.5 real analytic functions is
`content/11-taylor/03-analytic-functions.tex`, §14.5.1 (the divergence theorem in the language of
`k`-forms) is folded into `content/26-stokes/04-stokes-theorem.tex`, §14.2.1 partitions of unity
is `prop:partition_of_unity_finite`, and §15.2.5 Peano is in `appendix-a-odes.tex`.

*Analysis II: Several Variables*, Joaquim Serra. It continues the Analysis I numbering, so its
chapters run **9–15**, not 1–7.

**Three surveys, the first two against different revisions of the same file, which is where the
page-number caveat above comes from:**

| Date | Revision surveyed | Offset in force | Outcome |
|---|---|---|---|
| 2026-08-07 | 207 pp, as `Analysis_II_Script_v1.pdf` | printed = PDF − 4 | Every divergence, gap, exercise and example transcribed and build-verified. |
| 2026-08-09 | 239 pp, as `lec_notes.pdf`, dated 27 July 2026 | printed = PDF − 5 | Norm convention adopted, notation audited, six missing statements added. See *Where the document stands*. |
| 2026-08-10 | same 239 pp file | printed = PDF − 5 | Table of contents walked section by section against `content/`. One gap: §13.2.5 improper integrals, now ch. 19 §b. Everything else accounted for. |

The file grew by 32 pages between the two, which is why an old citation's page can miss and why
the offset changed. ⚠️ **Never quote a formula from the extracted text.** `pdftotext` eats `∂`,
`≤`, `∇`, `∈` and most Greek. Render the page and read it.

**Where we are ahead of the script — do not "fix" these by cutting them.** Differential forms
(chs. 24–25: the script has four unproved paragraphs, we have a full treatment); geodesics
(ch. 18, no counterpart); our convexity characterisations (more equivalent conditions than the
script's two); the Hessian test stated for `C²` rather than `C³`, handling the degenerate case;
Lagrange multipliers in the linear-dependence form with a constraint-qualification
counterexample, where the script gives the `λ₀`-normalised form with no qualification at all.

**Errors found in the script.** The serious two (E2, a false statement of Weierstrass; E6, a
false `rot(φF)` identity set as an exercise) are handled with `ainote`s. These are cosmetic, and
are recorded only so they are not copied if you touch the corresponding result. ⚠️ The pages
below are from the 207-page revision and were **not** re-checked against the current 239-page
one; the numbered results are what to search for, not the pages. Some may also have been fixed
upstream since.

| Where | Problem |
|---|---|
| Def 9.52(1), p. 18 | ε–δ condition ends `f(B(x,δ)) ⊆ B(f(y),ε)`; there is no `y` — should be `f(x)`. |
| Def 13.2, p. 89 | Injective map typed `a : {1,…,N} → ℤ^k` (should be `ℤⁿ`); union uses side length `2^{-k}` where the text fixes `2^{-p}`. Propagates into Lemma 13.20. |
| Ex 10.21, p. 48 | In the `∂/∂x` line, `2e^{u+v}·0` should be `2e^{u+2v}·0`. Multiplied by zero, so answers are right. |
| Thm 15.33, p. 188 | Hypothesis says `(f_k)` bounded in `C(K,ℝ)`, conclusion says `C(K,ℝᵐ)`. Ours uses `ℝᵐ` throughout. |
| Prop 11.24, p. 74 | Typed `f : C²(U)` for `f ∈ C²(U)`. |

## Exercises

Each sheet's problems sit with the material they test.

- **Quote every problem statement verbatim.** Do not paraphrase; attribute the sheet.
- **Tag each problem** with its priority from Corsin's *Recommended exercises* colour code:

  | Corsin's marker | Tag |
  |---|---|
  | blue ▨ | `**important**` |
  | orange ▨ | `**semi-important**` |
  | red ▨ | `**optional**` |
  | official `(*)` | `**harder**` |

- Corsin's hint follows the statement, attributed and page-pointed.
- TAs' worked solutions are presented; `SolN_Analysis2_eng.pdf` is used to **check**.
- **When you transcribe a new problem, add it to the table in
  `content/appendix-d-problem-sheets.tex`**, which restores the sheet view: one table per sheet,
  with Corsin's priority markings and his own comments, and a column pointing at the section
  that now hosts each problem.

## German mirroring

The document is English, but German technical terms are mirrored on **first introduction** so it
can be used alongside German lecture and exercise material:

```latex
a \newterm{compact} set \germanfor{kompakte Menge}
the \newterm{implicit function theorem} \germanfor{Satz über implizite Funktionen}
```

`\germanfor` and `\germanterm` are defined together in `main.tex`; see *Settled decisions* above
for which is which. Only on first introduction — never repeated. Canonical German wording comes
from **Jérôme Paschoud**'s topic-named files. Every pair also goes into
`content/appendix-b-glossary.tex`, whose third column is the **chapter** of first introduction
(a letter there means an appendix).

## Document skeleton — SETTLED

**Part = thematic block. Chapter = topic. Section = one file. Day and week = gone.**

The document used to be one chapter per teaching week. It is now organised by content: seven
`\part`s over 26 topic chapters, each chapter a directory, each section its own file. A week is
an accident of the timetable — compactness was split across two of them and stitched back
together with a back-pointer — whereas a chapter you can name is something a reader can look up.

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

⚠️ **Do not undo the restructure.** It was done on the user's explicit instruction, and it
changed no mathematics: within a topic the order of results, the proofs and the examples are the
tutor's; only the containers moved.

**Numbering.** Directory prefixes are ordering only; the real chapter number comes from the
`\input` order in `main.tex`. `\part` deliberately does **not** reset `\thechapter`, so chapter
numbers — and therefore theorem numbers, which are built from them — run continuously 1–26.

**Every file carries its provenance.** The first line of each is an `% Originally:` comment
naming the old week file and section it came from; the `% Source:` comments beneath are the
tutor's own, unchanged, and still cite his week-numbered PDFs. Those two kinds of comment answer
different questions — where this text used to sit in *our* document, and where it came from in
*his* notes — and both are worth keeping.

**Heading styles and suffixes:**
* **Colours:**
  - Part Title: `ThemePurple` (`PartTitleText`), number in `OliveGreen` (`PartNumberText`)
  - Section Title: `MidnightBlue` (`SecTitleColor`)
  - Subsection Title: `MidnightBlue` (`SubSecTitleColor`)
  - Subsubsection Title: `TextBoldColor` (`SubSubSecTitleColor`)
  - Green `(...)` suffix: `OliveGreen` (`SecNumberColor`)
* **Suffix format:** all numbered headings carry a green suffix:
  - `\chapter{...}` -> `Title (Chapter 7)`, and `(Appendix C)` after `\appendix`
  - `\section{...}` -> `Title (Section 7.a)`
  - `\subsection{...}` -> `Title (Subsection 7.a.1)`

**Avoid a chapter that is one section repeating the chapter's own title.** If a chapter has
exactly one section and they share a name, either split the section or let the chapter absorb it.

**Retired macros — do not reinstate.** `\session{Monday}`, `\exercisesheet{N}` and
`\continuedfrom{label}` all existed to prop up the week structure and are gone from `main.tex`.
There is no day to mark, the problem sheets are dissolved, and no topic is split across a
boundary that would need a back-pointer.

**File naming:** `content/NN-topic-slug/NN-section-slug.tex`, with `00-chapter.tex` for the stub
and `99-solutions.tex` for the solutions. There is no `transcript/` stage and no
`content/exercise-sheets/` directory — typeset straight into the section file.
