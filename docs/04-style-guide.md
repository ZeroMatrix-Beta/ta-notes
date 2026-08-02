# House style — Analysis II TA notes

Derived from `gemini.md` (the prompt that worked on the Linear Algebra transcription).
LinAlg-specific rules have been dropped; Analysis II rules added.

---

## 1. Role & the two layers

You are a high-fidelity mathematical editor turning TA notes into a polished document.

**Foundational layer (fidelity).** The TA's notes are the blueprint. Follow **Corsin Nick's**
logic, wording and proof structure at ≥80% fidelity. If he explains a concept his own way,
keep his way — do **not** substitute a standard textbook proof.

**Editorial layer (style).** Translate handwritten shorthand into full academic English
prose, staying in the author's voice. If the source is minimalist, the expansion stays
minimalist in spirit.

Expand in prose: `iff` → "if and only if", `s.t.` → "such that", `w.r.t.` → "with respect to",
`w.l.o.g.` → "without loss of generality". The macros `\iff`, `\implies` remain fine **in math**.

---

## 2. Exercises

Each week opens with the official problem sheet.

- **Quote every problem statement in full**, taken verbatim from
  `exercises/ExN_Analysis2_eng.pdf` — not paraphrased. Attribute the sheet.
- Tag each problem with its **priority**, from Corsin's colour code on his
  *Recommended exercises* page:

  | Corsin's marker | Tag |
  |---|---|
  | blue ▨ | `**important**` |
  | orange ▨ | `**semi-important**` |
  | red ▨ | `**optional**` |
  | official `(*)` | `**harder**` |

- Where a second TA independently flags the same problem (Sascha Brack's `Ex Sheet Hints/`,
  Simon Kamps's `SerieNNHints.pdf`), say so — cross-TA agreement is a strong signal and
  worth surfacing to the reader.
- Corsin's hint follows the statement, attributed and page-pointed.
- The TAs' worked solutions are the ones presented. `SolN_Analysis2_eng.pdf` is used to
  **check** them, not to replace them; a genuine divergence goes in `06-open-questions.md`.

---

## 3. German mirroring

The document is English, but German technical terms are mirrored on **first introduction**
of a concept, so it can be used next to the German lecture and exercise material:

```latex
a \newterm{compact} set (\germanterm{kompakte Menge})
the \newterm{implicit function theorem} (\germanterm{Satz über implizite Funktionen})
```

`\germanterm{…}` is defined at `main.tex:174` and renders as *„…"* in the bold accent
colour. Only on first introduction — never repeatedly.

Canonical German wording comes from **Jérôme Paschoud**'s topic-named files
(*Metrische Räume*, *Banach und Kompaktheit*, *Satz über inverse Funktionen*,
*Untermannigfaltigkeiten*, *Variablenwechsel*, *Divergenzsatz*, *Wegintegrale*,
*Differentialformen*, *Picard–Lindelöf*, …). Every pair also goes into the glossary
that becomes `content/appendix-b-glossary.tex`.

In the Markdown transcripts write it as `**compact** ("kompakt")` so conversion is mechanical.

---

## 4. Mathematical notation

- **Definitional equals.** Use `:=` whenever a symbol is introduced, a set/function is
  defined, or a local assignment is made in a proof (`Let $r := \dist(x, A)$`,
  `B_r(x) := \{y \in X : d(y,x) < r\}`). Reserve `=` for equations between existing quantities.
- **Metric spaces.** `(X,d)`; open ball `B_r(x)`; closure `\overline{A}`; interior
  `\operatorname{int}(A)`; boundary `\partial A`. Note Corsin's own emphasis
  (Week 2, p. 6): the `y \in X` in `B_r(x) := \{y \in X : d(y,x) < r\}` is the
  "important subtlety" — preserve that emphasis.
- **Norms.** `\|\cdot\|` (`\lVert … \rVert`), never `||…||`. Numbered norms `\|x\|_1`,
  `\|x\|_2`, `\|x\|_\infty`; Corsin's metrics `d_1` (Manhattan), `d_2` (standard),
  `d_3` (supremum) keep his indices.
- **Derivatives.** Distinguish carefully and consistently:
  `Df(x_0)` the (total) differential as a linear map; `\Jac f(x_0)` its Jacobian matrix;
  `\nabla f(x_0)` the gradient; `\partial_i f`, `\frac{\partial f}{\partial x_i}` partials;
  `D_v f` the directional derivative; `\Hess f` the Hessian.
- **Function spaces.** `C^k(U, \mathbb{R}^m)`, `C^\infty`, `C^0([0,1], \mathbb{R})`.
- **Sets.** `\mathbb{R}^n`, `\mathbb{N}`, `\mathbb{C}`. Sphere `S^n`. Use `\subseteq` for
  inclusion (Corsin does) and `\subsetneq` when strictness matters.
- **Operators.** Use the macros, never raw `\mathrm{}`:
  `\dist`, `\diam`, `\supp`, `\vol`, `\divg`, `\curl`, `\Jac`, `\Hess`, `\grad`,
  `\rank`, `\id`, `\Img`, `\sgn`, `\Tr`, `\GL`, `\transp`.
- **Matrices.** `pmatrix` in display math; `\left(\begin{smallmatrix}…\end{smallmatrix}\right)`
  inline. Anything 3+ rows, or with column blocks, goes to display math — never inline.
- **Long displays.** Split with `align`/`split` at major `=` signs; `\nonumber` on
  intermediate lines unless referenced.
- **Delimiters.** `\left(`/`\right)` in display math; plain delimiters inline unless the
  content is genuinely tall.
- **Punctuation** goes *outside* inline math: `$x = 2$,` not `$x = 2,$`.

---

## 5. Document skeleton

One `\chapter` per teaching week, matching Corsin's file names:

```latex
\chapter{Week 2 --- Metric Spaces, Topology \& Continuity}
  \subsection*{Recommended exercises}   % the week's problem sheet
  \session{Monday}                      % -> \section{...}, see below
    \subsection{Metric spaces}
  \session{Friday}
```

**`\session`.** Corsin splits every week into a Monday and a Friday class. Rather than
hard-coding `\section{Monday}` everywhere, define one macro in the preamble so the day
headings stay a single restylable unit:

```latex
% Week N, Monday/Friday class heading.
\newcommand{\session}[1]{\section{#1}}
```

Because `\thesection` is `\thechapter.\alph{section}`, this numbers the Monday class of
Week 5 as *5.a* and the Friday class as *5.b*, and theorems inside them as `5.a.1`, `5.b.1`.
That is exactly the numbering the preamble was already built for — no override needed.
Changing the look of every day heading later is then a one-line edit.

Weeks with only one recorded session (Corsin's Week 7 and Week 10 have no Friday file) simply
omit the second `\session`.

## 6. Structure & environments

Use the environments already defined in `main.tex`:

```
numbered:    theorem  lemma  corollary  definition  proposition
unnumbered:  theorem* lemma* corollary* definition* proposition* claim*
             notation remark exercise example summary warmup question answer
             importantremark goals conclusion ainote
             proof   exercisesolution[<title>]
```

- **Sub-parts** use alphabetical labels via the environment, never hard-coded:
  `\begin{enumerate}[label=\textbf{(\alph*)}]` + plain `\item`. Never `\item[(a)]`.
  A proof of a multi-part statement mirrors the statement's `enumerate` exactly.
  Referencing a sub-part in prose keeps the bold: "by **(b)**".
- **Named lists** (properties like *definiteness*, *symmetry*, *triangle inequality* —
  Corsin labels these explicitly in Week 2, p. 3) use the `description` environment.
- **Labels** are descriptive slugs, never numbers: `\label{thm:heine_borel}`,
  `\label{def:metric_space}`. Place immediately after `\begin{…}`. Prefix by type
  (`thm:`, `lem:`, `cor:`, `def:`, `prop:`, `ex:`, `fig:`, `eq:`).
- **Cross-references** use `\cref{…}` (mid-sentence) / `\Cref{…}` (sentence-initial);
  never write "Theorem" manually. Equations use `\eqref{…}`.
- **New terminology** uses `\newterm{…}`. `\qt{…}` is for literal quotes and informal
  phrases only — e.g. Corsin's *"detours make the way longer"* gloss on the triangle
  inequality — never for a term being defined.
- **Never** put `\newterm`/`\qt`/any formatting macro inside an environment's `[...]`
  header argument.
- **Solutions** to exercises use `exercisesolution`, titled with `\cref` to the exercise.
- **Commutative diagrams**: `tikz-cd`.

---

## 7. Figure stubs — write specs, not pointers

The goal of the transcript stage is that the LaTeX stage needs **only the Markdown**. Prose
achieves that. Figures only achieve it if the stub is written as a *drawing specification*.

While the page is still on screen, capture what a TikZ author would otherwise have to reopen the
PDF for: relative positions, which objects are solid / dashed / dotted, arrow directions and what
they connect, label text and where it sits, panel layout, and roughly where curves bend or cross.
Colours are part of Corsin's convention (blue / orange / red / green / purple) — name them.

- **Pointer (forces a re-read):** "blob $X$ covered by three dotted regions $U_1$, $U_2$, $U_3$."
- **Spec (self-sufficient):** "kidney-shaped blue blob $X$; three overlapping dotted ellipses at
  roughly 10, 2 and 6 o'clock, each crossing the boundary outward; labels $U_1$–$U_3$ placed
  outside the blob next to their own ellipse; caption $U_1\cup U_2\cup U_3 = X$."

Costs nothing extra at transcription time, and removes an entire second pass over the source.

**Weeks 2–11 were written to the weaker standard.** The Group A / Group B split at the bottom of
`05-figure-queue.md` records which of those 49 figures are still self-sufficient (mathematically
determined) and which need the page in view.

## 8. Prose

- Prefer English connectives to arrows: "This implies that", "Consequently", "Hence",
  "Therefore". Avoid strings of isolated `\iff` interleaved with prose fragments.
  Never use `\implies` inside a display; break into prose between displays.
- Comma after introductory adverbs: "Clearly,", "Moreover,", "In this case,", "Hence,".
- Comma before "and therefore" where it reads well.
- Manual hyphenation hints on long technical terms:
  `finite-di\-men\-sional`, `dif\-fer\-en\-ti\-able`, `sub\-man\-i\-fold`,
  `com\-pact\-ness`, `par\-a\-met\-ri\-za\-tion`.
- Formal, structural academic tone throughout.

---

## 9. Provenance & honesty

- Every environment in `content/*.tex` traces back to a page pointer in `transcript/*.md`.
- Suspected errors in a source are **flagged, never silently corrected**:
  `\omitted{…}` / a dark-red note in the text, plus an entry in `06-open-questions.md`.
- Illegible source text: `⟨?word⟩` in the transcript + an `OQ-` entry. Never guess silently.
- Content taken from a tutor other than Corsin is attributed in the text.

---

## 10. Forbidden

- `\vspace{1em}\noindent\hrulefill\vspace{1em}` spacer blocks.
- Manual `\newpage`/`\vspace` for cosmetic tuning (the preamble handles spacing).
- Touching the theorem / `aliascnt` / `cleveref` machinery in `main.tex:334–463` — the
  comments there document real bugs already solved. Do not regress them.
- Editing anything inside the 17 tutor source folders or `exercises/`.
