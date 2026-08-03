# House style — Analysis II TA notes

`gemini.md` is our guideline — the base style prompt this project's house style is built on.
This document adds Analysis-II-specific rules and settled decisions on top of it; it does not
replace it. Where this document is silent, `gemini.md` governs.

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

## 5. Document skeleton — SETTLED

**Chapter = week (container). Section = topic (the navigable level). Day = a marker, not a
sectioning level.**

```latex
\chapter{Week 2 --- Metric Spaces, Topology \& Continuity}   % chapter no. = week no.

\exercisesheet{2}            % \section*, but does appear in the TOC
\session{Monday}             % styled rule in the body; NOT a sectioning command
\section{Structured spaces}          % -> 2.a
\section{Metric spaces}              % -> 2.b
  \subsection{Examples}              % unnumbered (secnumdepth = 1)
\section{Open and closed sets}       % -> 2.c
\session{Friday}
\section{Continuity}                 % -> 2.d
```

### Why day is not a sectioning level

Only **weeks 2, 3 and 4** carry Monday/Friday markers in Corsin's notes; weeks 5–11 have none
(each transcript records "no session split"). Making day a `\section` would leave nine chapters
with a single section or none, and would push topics down to `\subsection`, which is unnumbered
under `secnumdepth = 1` — so theorems would lose their topic anchor. Topic-as-section also matches
the sibling project `en-ta-notes-analysis2-sb`, which sections purely by topic.

### What this buys

`\thesection` is already `\thechapter.\alph{section}` and theorems already number
`Chapter.SectionLetter.Number`, so with no preamble override:

- chapter number **equals** the week number — Week 7 is Chapter 7;
- sections read *2.a Structured spaces*, *2.b Metric spaces*, … — a TOC you can navigate by topic;
- theorems land as `2.c.1`, anchored to a **topic**, not to a weekday;
- `\cref{sec:metric_spaces}` resolves to something meaningful.

### Macros to add to the preamble

```latex
% Monday/Friday class marker. Deliberately NOT a sectioning command: it must not
% consume a section letter, disturb theorem numbering, or enter the TOC.
\newcommand{\session}[1]{%
  \par\addvspace{2.5ex}%
  \noindent{\sffamily\bfseries\color{ThemeWeekNumber}#1}%
  \hspace{0.75em}\textcolor{HeaderFooterLine}{\leaders\hrule height 0.5pt\hfill}%
  \par\addvspace{1.2ex}\noindent\ignorespaces}

% The week's problem sheet. Unnumbered so it does not consume a section letter
% (theorem numbers stay tied to topics), but listed in the TOC so it is findable.
\newcommand{\exercisesheet}[1]{%
  \section*{Exercise sheet #1}%
  \addcontentsline{toc}{section}{Exercise sheet #1}%
  \markright{Exercise sheet #1}}

% A topic carried over from the previous week.
\newcommand{\continuedfrom}[1]{%
  \par\noindent{\small\itshape\color{TextMetaNote}Continued from \cref{#1}.}\par\addvspace{1ex}}
```

### Topics that span weeks

Corsin himself writes *"Compactness (continued)"* at the top of Week 3. Mirror that:

```latex
\section{Compactness --- continued}
\label{sec:compactness_continued}
\continuedfrom{sec:compactness}
```

The `---` form is the house convention for any carried-over topic. Always add
`\continuedfrom{...}` so the reader can jump back.

### Finding a topic across weeks

Because chapters are weeks, a topic split over two weeks appears twice. The fix is **not** to
restructure but to add **Appendix C — Thematic index**: lecture chapters 9–14 → the week/section
that covers them, generated from `docs/03-topic-index.md`. Readers who think in lecture chapters
use that; readers who think in weeks use the TOC.

### File naming

`content/week-02.tex` etc., one file per week — matching `transcript/week-02.md` one-to-one, so
the two stages stay in lockstep. (The sibling `-sb` project splits one file per topic; that suits
a single-week pilot, not 12 weeks.)

## 6. Structure & environments

Use the environments already defined in `main.tex`:

```
numbered:    theorem  lemma  corollary  definition  proposition
unnumbered:  theorem* lemma* corollary* definition* proposition* claim*
             notation remark exercise example summary warmup question answer
             importantremark goals conclusion ainote
             proof   exercisesolution[<title>]
```

- **Named theorem environments.** All theorem-like environments should carry a `[Name]`
  bracket where a natural name exists:
  `\begin{theorem}[Heine--Borel]`, `\begin{definition}[Metric space]`,
  `\begin{lemma}[Gronwall's inequality]`. This is now the **preferred** style.
  See `gemini.md` for the `proof`-adjacency exception and macro restrictions.
- **Sub-parts** use alphabetical labels via the environment, never hard-coded:
  `\begin{enumerate}[label=\textbf{(\alph*)}]` + plain `\item`. Never `\item[(a)]`.
  A proof of a multi-part statement mirrors the statement's `enumerate` exactly.
  Referencing a sub-part in prose keeps the bold: "by **(b)**".
- **Named lists** (properties like *definiteness*, *symmetry*, *triangle inequality* —
  Corsin labels these explicitly in Week 2, p. 3) use `itemize` or `enumerate`, never
  `description` (forbidden, see section 10) — bold the name inline with `\textbf{name}`
  rather than putting it in a `description` item label:
  `\item \textbf{definiteness:} $d(x,y) \geq 0$, ...`.
- **Labels** are descriptive slugs, never numbers: `\label{thm:heine_borel}`,
  `\label{def:metric_space}`. Place immediately after `\begin{\ldots}`. Prefix by type
  (`thm:`, `lem:`, `cor:`, `def:`, `prop:`, `ex:`, `fig:`, `eq:`).
- **Cross-references** use `\cref{\ldots}` (mid-sentence) / `\Cref{\ldots}` (sentence-initial);
  never write "Theorem" manually. Equations use `\eqref{\ldots}`.
- **New terminology** uses `\newterm{\ldots}`. `\qt{\ldots}` is for literal quotes and informal
  phrases only — e.g. Corsin's *"detours make the way longer"* gloss on the triangle
  inequality — never for a term being defined.
- **Never** put `\newterm`/`\qt`/any formatting macro inside an environment's `[...]`
  header argument.
- **Exercises — prefer numbered.** Use a numbered `exercise` counter so `\cref{ex:...}` works.
  The preamble's `\newtheorem*{exercise}` (unnumbered) is available for truly standalone
  exercises; for everything else, numbered is preferred. Always reference exercises with
  `\cref{ex:...}` or, if unnumbered, `\cpageref{ex:...}`.
- **Solutions** to exercises use `exercisesolution`, titled with `\cref` to the exercise.
- **Commutative diagrams**: `tikz-cd`.
- **Environment semantics.** See `gemini.md § ENVIRONMENT SEMANTICS` for the authoritative
  rules on when to use `remark` vs. `notation` vs. `ainote`. Short version:
  - `ainote` is the **only** home for AI/editorial/meta remarks.
  - `notation` is purely for introducing source notation; not for commentary on the notation.
  - `remark` is for mathematical observations only.

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
`05-figure-queue.md` records which of those 45 figures are still self-sufficient (mathematically
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
- **Source provenance comments in LaTeX.** At the top of each `\section` (or `\subsection`
  if a section spans material from multiple sources), insert:
  ```latex
  % Source: Corsin Nick/Class Notes/Week 5.pdf, pp. 1--3
  \section{Compactness}
  ```
  Use a relative path from the project root and a page range. When merging a second tutor's
  material, add a `% Supplement:` line beneath it. Do **not** add per-theorem or per-definition
  comments — section-level granularity is sufficient and keeps token cost manageable.
- Suspected errors in a source are **flagged, never silently corrected**:
  `\omitted{\ldots}` / a dark-red note in the text, plus an entry in `06-open-questions.md`.
- Illegible source text: `⟨?word⟩` in the transcript + an `OQ-` entry. Never guess silently.
- Content taken from a tutor other than Corsin is attributed in the text.
- **Custom sections are allowed.** You may inject `\section`, `\subsection`, and
  `\subsubsection` headings that are not in the handwritten source whenever they improve
  readability or navigation. This is an editorial decision within your authority.

---

## 10. Forbidden

- `\vspace{1em}\noindent\hrulefill\vspace{1em}` spacer blocks.
- Manual `\newpage`/`\vspace` for cosmetic tuning (the preamble handles spacing).
- Touching the theorem / `aliascnt` / `cleveref` machinery in `main.tex:334--463` — the
  comments there document real bugs already solved. Do not regress them.
- Editing anything inside the 17 tutor source folders or `exercises/`.
- The `description` environment, for any purpose. Use `itemize`/`enumerate` instead.
- Using `remark`, `notation`, or any semantic mathematical environment for AI/editorial
  meta-remarks — use `ainote` exclusively for those. See `gemini.md § ENVIRONMENT SEMANTICS`.
