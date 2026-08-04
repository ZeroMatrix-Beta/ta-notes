# Tutor review — weeks 1-7 (notes only, exercises excluded)

Skim pass over the 16 non-Corsin tutor folders, weeks 1-7, looking for material Corsin
doesn't already cover: useful analogies, transitions between topics, and drawings worth
adapting. Exercise-only material (hints, worked solutions) was skipped per scope.

## Worth mining for real content

- **Sascha Brack** — best find of the pass. Colour-coded theorem/definition/remark boxes.
  Explicitly **flags an error in the official lecture script**: "The script lecture had a
  version of this statement that is not fully correct" (about a sequence converging iff its
  only accumulation point — false in general; counterexample given: `x_n = 1/n` on odds,
  `x_n = n` on evens, `0` is the only accumulation point but the sequence diverges). Matches
  our `\begin{ainote}`/error-flagging convention directly. Also has a clean three-step
  "convergence via compactness" proof-strategy template, and an `arccos(x·y/‖x‖‖y‖)`
  angle-interpretation of Cauchy-Schwarz.
- **Diego Torres Tejeda** — standout supplement. "Addendum: Sequential and Topological
  Compactness" is a polished, self-contained proof of the equivalence via a Lebesgue-number
  argument, plus total boundedness and a uniform-continuity corollary. More rigorous/complete
  than typical weekly notes; a strong candidate for the compactness gap already flagged in
  `03-topic-index.md`.
- **Toby Lane** — well organized (Hypothesis/Thesis/Proof/Warning/Remark colour boxes),
  consistently ties back to Analysis I ("the Taylor expansion is just your standard Analysis I
  expansion in every coordinate"), and has a genuinely clarifying remark distinguishing the
  global `1/k!` weighting vs. the per-term `1/α!` weighting in the multivariable Taylor
  formula. Also ships GeoGebra files (directional derivative, gradient/contour) — not
  LaTeX-mineable but worth knowing about.
- **Maarten Cnoops** — has an actual `Woche 1.pdf`: builds from Analysis-I continuity up to
  the metric axioms, the bounded-metric trick `d' = d/(1+d)`, normed/Banach spaces, and an
  isometric-completion theorem. Seeded `content/week-01.tex` from this (see below) — though
  the structured-spaces hierarchy itself turned out to already be in `week-02.tex`, so only
  the genuinely new pieces (completion teaser, bounded-metric trick) were worth pulling.

## Solid but mostly redundant with Corsin

- **Adrien Martelli** — handwritten (French/German), decent geometric sketches (sphere/
  tangent-space picture for Lagrange multipliers, an alternative normalized-multiplier
  condition `λ0²+...+λk²=1`), but doesn't go beyond Corsin.
- **Lukas Krause** — explicitly "not intended to be well-formulated," but has one nice
  colour-coded Pythagorean-theorem sketch motivating the Euclidean norm. Otherwise standard.
- **Lennard Trautmann** — clean, correct, well-structured German write-up; stays close to
  standard textbook phrasing, no standout analogies found.
- **Jérôme Paschoud** — rigorous and clean but almost entirely exercise-solution transcripts
  rather than exposition.
- **Damien Lesieur** — typed, dry, but useful as a **numbering cross-check**: his theorem/
  proposition numbers (9.x = metric spaces, 10.x = differentiation, 11.x = optimization)
  line up with the official lecture-notes chapter numbers that `03-topic-index.md` still
  marks provisional.

## Low incremental value for this merge

- **Linus Lüchinger** — slides mostly logistics/"gotchas from the exercise sheet"; light on
  exposition.
- **Fabio Guger** — messy mixed German/English filenames and sessions; nothing distinctive
  found in the sample.
- **Riccardo Vanoni** — only 2 weeks of material, exercise-class framing rather than
  exposition.
- **Noah Larsson, Simon Kamps, Tim Fessler** — exercise-hints or off-topic (a physics formula
  sheet, a single unrelated file) only.
- **Toprak Erakay** — competent but plain; nothing distinctive stood out in the sample.

## Exercise placement decision

Every week currently opens `\exercisesheet{N}` immediately, before any prose
(`content/week-02.tex:4`, right after `\chapter{...}`). Decision made in-session: move
`\exercisesheet{N}` to just before `\section{Solutions}` at the end of each chapter, and add
a short intro paragraph at the top framing that week's topics instead. See git log / diffs on
`content/week-0*.tex` for the applied change.
