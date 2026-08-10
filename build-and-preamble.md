# Build traps and preamble facts

Everything tied to *this* `main.tex`: how numbering is derived, which environments exist, the
traps that have each broken a build at least once, and how to compile. **Line numbers in this
file are checked against `main.tex` and go stale when it grows** — if one does not point where
it claims, fix it here rather than working around it.

| Companion file | What lives there |
|---|---|
| `gemini.md` | Role, fidelity policy, tool usage — read first |
| `style.md` | House style: prose, notation, environments, provenance conventions |
| `gemini.md` | Also holds the sources: blueprint tutor, reference documents, scope against the script |

## Document layout — SETTLED

**Part = thematic block. Chapter = topic. Section = one file. Day and week = gone.**

Seven `\part`s over 26 topic chapters, each chapter a directory, each section its own file.

```
content/
  07-compactness/
    00-chapter.tex      <- \chapter + \label + a short intro + nothing but \input lines
    01-open-covers.tex
    ...
    99-solutions.tex    <- the chapter's single \section{Solutions}
```

`main.tex` holds the `\part` lines and one `\input` of each `00-chapter.tex`, in order. **To add a
chapter:** make the directory, write `00-chapter.tex`, add the `\input`. **To add material to an
existing chapter:** drop a new `NN-*.tex` beside its siblings and add one `\input` line to that
chapter's stub. Nothing else has to be touched — that is the whole reason for the layout.

⚠️ **Do not undo the restructure** from one-chapter-per-teaching-week to topic chapters. It was
done on the user's explicit instruction, and it changed no mathematics: within a topic the order of
results, the proofs and the examples are the tutor's; only the containers moved.

**Every file carries its provenance.** The first line of each is an `% Originally:` comment naming
the old week file it came from; the `% Source:` comments beneath are the tutor's own, unchanged.
Those two answer different questions — where the text used to sit in *our* document, and where it
came from in *his* notes — and both are worth keeping.

**File naming:** `content/NN-topic-slug/NN-section-slug.tex`, with `00-chapter.tex` for the stub and
`99-solutions.tex` for the solutions. There is no `transcript/` stage and no
`content/exercise-sheets/` directory — typeset straight into the section file.

**Avoid a chapter that is one section repeating the chapter's own title.** If a chapter has exactly
one section and they share a name, either split the section or let the chapter absorb it.

**Heading suffixes and colours.** All numbered headings carry a green `(...)` suffix in `OliveGreen`
(`SecNumberColor`): `\chapter{...}` → `Title (Chapter 7)`, and `(Appendix C)` after `\appendix`;
`\section{...}` → `Title (Section 7.a)`; `\subsection{...}` → `Title (Subsection 7.a.1)`. Part
titles are `ThemePurple` (`PartTitleText`) with the number in `OliveGreen` (`PartNumberText`);
section and subsection titles are `MidnightBlue`; subsubsection is `TextBoldColor`.

**Retired macros — do not reinstate.** `\session{Monday}`, `\exercisesheet{N}` and
`\continuedfrom{label}` all existed to prop up the week structure and are gone from `main.tex`.

## Numbering is automatic — do not configure it

* **Theorem Numbering — do NOT set it per file in this project.** The scheme is
  `Chapter.SectionLetter.TheoremNumber` (e.g. 2.b.1), and `main.tex:415` already derives it
  automatically from `\thechapter` and the section counter, resetting per chapter. **No
  `content/*.tex` file overrides `\thetheorem`, and none should.**

  > ⚠️ Older revisions of this file instructed writing
  > `\renewcommand{\thetheorem}{23.a.\arabic{theorem}}` at the top of each part's file. That is
  > imported from a different repository (a linear-algebra project whose source parts did not
  > map one-to-one onto sections — the leftover comment naming "Prof. Biran" at `main.tex:406`
  > is from the same import). Following it here would hard-code a wrong chapter number into
  > every week and desynchronise the numbering from the actual chapter. Ignore it.
* **Exercises are already numbered — nothing to configure.** `main.tex:493` declares
  `exercise` via `\newaliascnt{exercise}{theorem}`, so every `\begin{exercise}` is numbered and
  `\cref{ex:...}` resolves to a clickable reference out of the box. Do **not** declare a local
  counter, and do not look for an `exercise*` variant — there isn't one. Give every exercise a
  descriptive label (`\label{ex:heine_borel_fails}`, or `\label{ex:4.3}` for a problem quoted
  from the official sheet) and reference it with `\cref`.
* **Multi-Pass Compilation for Cross-References:** When adding or modifying labels, `\cref` references, or `lastpage` counters, always run full multi-pass compilation (e.g. `latexmk`) until `.aux` files stabilize and all cross-reference warnings resolve.

## Build traps in this preamble (each has cost a broken build at least once)

* **Float specifier `[h]` warnings:** Never use `[h]` alone for floats (like `table` or `figure`), as LaTeX will warn (`LaTeX: 'h' float specifier changed to 'ht'`) and change it. Always use `[ht]` or `[htbp]` to give LaTeX enough flexibility.
* **`\end{ainote>` — closing an environment with `>` instead of `}`.** Every model working on
  this file has made this one, repeatedly, and it is the single most common break. The error
  message does not point at it; you get *"Paragraph ended before \end was complete"* plus
  *"`\begin{ainote}` on input line N ended by `\end{document}`"*, with a line number pointing at
  the **opening** brace, often hundreds of lines earlier. It also cascades into hundreds of
  bogus "undefined reference" warnings, which look alarming and are not the problem.

  * **BAD:** `\end{ainote>`  `\end{remark>`  `\end{aiexample>`
  * **GOOD:** `\end{ainote}`  `\end{remark}`  `\end{aiexample}`

  Cheap detector, worth running after any batch of edits:
  use the search tool in regex mode on `\\(begin|end)\{[a-z*]+[>)\]]` to find malformed closers.
  If you suspect unmatched `ainote` environments, search for `begin{ainote}` and `end{ainote}` and
  compare the counts for the file you edited. Do this **before** reading the log.
* **`\textbf{...}` inside `$$...$$` errors** with *"Command \sffamily invalid in math mode"*.
  The sans-serif theorem fonts leak into math mode. Use `\text{\textbf{(1)}}` (mathtools is
  loaded) or `\mathbf`.
* **`question` and `answer` take NO optional argument.** `\begin{question}[Some title]` fails
  with the same `\sffamily` error. Put the title in the body text instead.
* **`ainote` has its own counter and may be `\label`ed and `\cref`ed** (changed 2026-08-09; it
  was `\newtheorem*` and unreferenceable before). It is declared
  `\newtheorem{ainote}{AI-Note}[chapter]`, so it does **not** alias the shared theorem counter
  and `\cref` prints `AI-Note 15.1`. Do not "fix" this back to `\newaliascnt{ainote}{theorem}`:
  that variant was tried and reverted, because 119 AI-Notes stepping the shared counter tore
  holes in the theorem numbering (a Lemma 2.f.43 followed by a Definition 2.f.46). The
  independent counter is what avoids both that and the unnumbered-`\label` hazard.

  Being referenceable is **not** a licence to file content in an `ainote` — the two tests in
  `style.md` still decide `ainote` versus `remark` versus a plain `%` comment.
* **Never bulk-edit `.tex` with `perl -pi -e 's/.../.../'` containing backslashes.** In the
  replacement, `\\qt` collapses to `qt`, and in the *pattern* `\d`, `\p`, `\l`, `\C` are read as
  regex classes, not literal `\dots`, `\pi`, `\leq`, `\Crefname`. This has silently corrupted
  nine `\qt{}` and one `\leq` into `qt{}` and `eq` — which **typeset without erroring**, so a
  clean build does not prove the edit was safe. Use the edit tool. If you must use perl,
  verify afterwards with the search tool in regex mode on `(^|[^\\])qt\{` and similar.
* ⚠️ **Do not route `.tex` content, or backslash patterns, through the Bash tool at all.**
  The shell layer consumes one level of backslash *before the command runs*, so this corrupts
  writes **and** silently breaks the greps you would use to check them. It is the perl hazard
  above arriving by a route that does not look like a substitution.

  **On the way in.** Appending with a heredoc collapsed every `\\` to a single `\`:

  ```latex
  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}     % written
  \begin{pmatrix} 0 & 1 \  1 & 0 \end{pmatrix}     % landed on disk
  ```

  Quoting the delimiter did **not** prevent it — `<<'EOF'` was used and the collapse happened
  anyway — and it is not specific to `cat`: a `python - <<'PY'` heredoc written to *repair* the
  damage was mangled identically on its own way in, `\b` becoming a literal backspace so that
  `\begin` arrived as `␈egin`, and the repair script failed its own assertion.

  **On the way out.** The same layer eats the pattern, so verification quietly lies. Checking
  the repair with

  ```bash
  grep -cF '\\' 99-solutions.tex      # intended: count lines holding a row separator
  ```

  reported **59** on a file containing exactly **4** — because `'\\'` reached `grep` as a single
  backslash and matched every line with any control sequence at all. A detector that fails open
  is worse than none.

  **Why it bites here specifically.** Only backslash-doubled sequences are touched, so
  ninety-nine lines in a hundred survive and the diff looks clean at a glance. But `\\` is
  exactly what `pmatrix` rows, `align` breaks and `tabular` rows are built from, so the damage
  lands squarely on display math and tables. Nor is it reliably loud: in a `pmatrix` it raised
  *"Undefined control sequence"* and was caught in one build, but inside a `tabular` a collapsed
  `\\` merely **merges two rows** and typesets without erroring — the same "a clean build does
  not prove the edit was safe" trap the perl entry describes.

  **What to do instead.** Write with the edit tool, which writes bytes literally, and verify with
  the search tool, whose pattern is passed as a parameter and never sees a shell. On the file
  above, the search tool with pattern `\\\\` correctly returns the four matrix-row lines that
  `grep -cF` could not find.
* ⚠️ **Never put a commit message on the command line — write it to a file and use
  `git commit -F`.** This is the shell-quoting hazard above arriving by a third door, and it bites
  in PowerShell as readily as in Bash.

  `git commit -m @'...'@` with a here-string looks safe, and usually is. It broke on 2026-08-10
  with

  ```
  error: unknown switch `A'
  ```

  because the message contained double-quoted phrases. PowerShell re-quotes a multi-line string
  when handing it to a **native** executable, and the embedded `"` characters split the one
  argument into several, so the words `git add -A` sitting in the middle of the prose arrived at
  `git` as a flag.

  **What makes it dangerous is that it is intermittent.** A longer message committed minutes
  earlier through the identical here-string worked perfectly — it simply happened to contain no
  `"`. So the form appears reliable right up until a message quotes something, and the failure
  then points at a word in the prose rather than at the quoting.

  Write the message with the edit tool, to the scratchpad, and pass the path:

  ```bash
  git commit -F /path/to/commitmsg.txt
  ```

  Nothing then crosses the shell boundary. The same reasoning applies to any prose argument long
  enough to contain punctuation: `-F`, `--file`, or a heredoc-free equivalent beats `-m`.
* **A literal `[` or `]` inside a `[...]` environment title closes the argument early.** An
  exercise titled `[$\mathbb{R}[x]$ is infinite-dimensional]` broke LaTeX's optional-argument
  bracket matching — the `[x]` ended the `\begin{exercise}[...]` argument, and the error surfaces
  nowhere near the title. Brace-protect it: `$\mathbb{R}{[}x{]}$`. Applies to any theorem-like
  environment title containing a bracket in math.
* **`main.pdf` is often locked** by an open viewer; `latexmk` then dies with
  *"I can't write on file"*. Build with `-jobname=check` to a throwaway name instead.

  ⚠️ **Closing the viewer is not enough on its own.** After the lock is released, `latexmk`
  reports the *same* failure on the next run, because it has cached the failed state and will not
  retry. This looks exactly like the file still being locked, and it is not: test with a shell
  append, and if the file is writable, re-run with `-g` (force) to get a real build. Observed
  2026-08-10, where two ordinary re-runs both exited 12 against a demonstrably writable
  `main.pdf` and `-g` then produced all 310 pages first time.
* **`hyperref` warnings about `Token not allowed in a PDF string`**.
  This happens when math commands (like superscripts `^`, subscripts `_`, or specific symbols) appear in chapter or section titles, which hyperref tries to use for PDF bookmarks. Fix this by wrapping the math in `\texorpdfstring{math}{text}`. For example, `\texorpdfstring{$\mathbb{R}^n$}{Rn}` instead of `\texorpdfstring{$\mathbb{R}^n$}{R^n}`. The second argument must be plain ASCII text without any math formatting.

## Verifying figures

Do **not** trust TikZ source. Build, render the page (`pdftoppm -png -r 95 -f N -l N`), and
*look*. Several figures in this document asserted things their own coordinates contradicted: a
chord whose endpoints were not on the curve, "tangent" lines tangent to nothing, an open cover
that did not cover, marked points sitting where the curve was at its minimum. Where a figure
encodes a computation, check the arithmetic in a comment above it (see FIG-W06-03, now in
`content/14-convexity/`, for the pattern).

The 2026-08-09 figure pass is the strongest evidence for this rule. In Part VII alone, four of
the ten figures were wrong, and three of those were wrong *mathematically* rather than
cosmetically: a frame drawn as a rotation where the accompanying note asserted a reflection
(so it illustrated the case an orientable atlas **allows**); a point labelled $p \in \partial M$
sitting half a unit inside the interior, with the tangent vector pointing across the region and
the domain drawn on the wrong side of its own half-space boundary; and both shared-edge arrows
in the Green's theorem cell picture reversed relative to their own cells. Not one of the four
was visible in the source. The reversed arrows had survived several passes precisely because
the pair still *looked* like it cancelled — cancellation was the conclusion, but which arrow
belonged to which cell was the reason for it, and that was the part that was backwards.

## `Overfull \hbox` warnings: the baseline is now ZERO

**A clean build emits none. Zero is the baseline: if a build reports one, it is yours.**

This section used to tabulate three standing warnings as acceptable — 101.24pt in
`24-differential-forms/02-exterior-derivative.tex` (the `dx \wedge \dots` chain), 10.61pt in
`26-stokes/04-stokes-theorem.tex`, and 4.62pt in `14-convexity/01-convexity.tex`. All three are
gone, incidentally rather than deliberately: the prose revision and the norm-convention pass
rewrote the surrounding lines, and the widest of them was finally split into an `align*`.
Verified 2026-08-10 against a full 315-page build.

That makes the check sharper than it was, so use it: `Overfull` should return nothing at all.

```powershell
(Select-String -Path check.log -Pattern "Overfull" -SimpleMatch | Measure-Object).Count
```

⚠️ Do not read a small line count in `check.log` as a truncated log. MiKTeX writes very long
lines here, so a complete 315-page run is only about 1700 lines and reaches `page.2` within the
first thousand. Confirm completeness from the **tail** — a finished run ends with
`Output written on check.pdf` followed by `PDF statistics:`.

It was **four** until 2026-08-09. The fourth, 1.20pt in `appendix-a-odes.tex`, disappeared on its
own during the norm-convention pass: replacing `\lVert x_2-x_3\rVert` by `|x_2-x_3|` on the
Picard–Lindelöf Lipschitz line shortened it enough to fit. Page numbers are deliberately no
longer tabulated here, because they move whenever anything upstream is added; find the warning's
nearest `[NNN]` marker in the `.log` instead.

⚠️ **Attribute these by page, not by guesswork.** A list kept elsewhere had named
`26-stokes/02` and omitted `14-convexity` entirely, and it went unchallenged for some time
because the counts matched. The reliable method: find the `[NNN]` page marker nearest the
warning in the `.log`, then read that page of the PDF. The bracketed file nesting in the log is
not trustworthy on its own, because parentheses in ordinary text confuse the obvious parse.

## The preamble's environments and macros

* Don't use

```latex
\vspace{1em}
\noindent\hrulefill
\vspace{1em}
```

* Make use of the following environments:

```latex
% --- NUMBERED ENVIRONMENTS ---
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{proposition}[theorem]{Proposition}

% !! The block below is the GENERIC TEMPLATE and is NOT what this repo does. !!
% In this project every one of these is NUMBERED via \newaliascnt{name}{theorem},
% except `ainote`. See "This project's override" below, and main.tex:410-640,
% which is authoritative. Reproduced here only to show the available names:
%   remark, exercise, example, summary, warmup, question, answer,
%   importantremark, goals, conclusion, notation, ainote, aiexample, aiexercise
%   theorem, lemma, corollary, definition, proposition, claim*
\newtheorem{ainote}{AI-Note}[chapter]   % <- the ONE with a counter of its own
\newenvironment{exercisesolution}[1][Solution]{%
  \begin{proof}[#1]%
}{%
  \end{proof}%
}
% Trailing notes on an exercise/example (added 2026-08-10; main.tex, just below
% exercisesolution, carries the full comment). Both hang off the END of a statement,
% inside the environment, and share one geometry via \exnoteopen: a centred block
% indented \exnoteindent on each side, small italic, in a muted colour.
%   \exinfo{...}          \faTag, TextMetaNote gray -- where the problem came from
%   \exhint[Label]{...}   \faLightbulb[regular], HintTint -- how to start it
% Deliberately UNNUMBERED, the one case the rule below does not reach: they are
% formatting blocks inside an already-numbered environment and are never \cref
% targets, so no \label ever goes inside one. See style.md for when to use each.
% \hint{...} is RETIRED and no longer defined -- \exhint replaced it.
\newenvironment{exerciseinfo}{\exnoteopen{TextMetaNote}{\faTag}{Info}}{\exnoteclose}
\newenvironment{exercisehint}[1][Hint]{\exnoteopen{HintTint}{\faLightbulb[regular]}{#1}}{\exnoteclose}
% \newterm  -> ENGLISH quotes (main.tex:188). \germanterm (main.tex:189) is the
% \glqq...\grqq one. They are deliberately different -- the German-mirroring
% convention in style.md depends on it. Do not collapse them.
\newcommand{\newterm}[1]{\textcolor{BrickRed}{``}\textcolor{TextBoldColor}{\textit{#1}}\textcolor{BrickRed}{''}}
\newcommand{\germanterm}[1]{\textcolor{BrickRed}{\glqq}\textcolor{TextBoldColor}{\textit{#1}}\textcolor{BrickRed}{\grqq}}
\newcommand{\qt}[1]{\textit{\textcolor{BrickRed}{``}#1\textcolor{BrickRed}{''}}}

% --- MATH OPERATORS (the common core; a project's preamble is authoritative
%     for its own full list, e.g. this repo's main.tex also defines \Jac, \Hess,
%     \dist, \diam, \supp, \vol, \divg, \curl, \grad, \Img, \Orth, \Unit, ...) ---
\DeclareMathOperator{\Tr}{Tr}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\sgn}{sgn}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\id}{id}
\DeclareMathOperator{\GL}{GL}
```

* **This project's override — everything is numbered, with exactly one exception.** The generic
  template above uses `\newtheorem*` (asterisked, unnumbered) for `remark`/`example`/`exercise`/
  etc. **This repository's `main.tex` does not** — they are all numbered via the same
  `\newaliascnt{name}{theorem}` pattern as `lemma`/`corollary`/`definition`/`proposition`,
  because an unnumbered environment has no counter, so a `\label` placed inside it is silently
  misattributed by `cleveref` to whatever ambient counter (e.g. the enclosing subsection) was
  last stepped — producing wrong `\cref` output that still looks plausible.

  **The one exception is `ainote`, which has a counter of its very own** rather than an alias of
  the theorem counter: `\newtheorem{ainote}{AI-Note}[chapter]`. That is the third of three
  arrangements this environment has had, and the only one with neither failure mode:

  | Arrangement | What broke |
  |---|---|
  | `\newaliascnt{ainote}{theorem}` | 119 AI-Notes stepped the shared counter, so theorem numbers jumped (Lemma 2.f.43 → Definition 2.f.46). Reverted. |
  | `\newtheorem*{ainote}` (unnumbered) | No counter, so a `\label` inside it was misattributed to the last-stepped ambient counter, and `\cref` printed a plausible-looking wrong number. Reverted 2026-08-09. |
  | `\newtheorem{ainote}{AI-Note}[chapter]` | Current. Own counter, so `\label`/`\cref` work (`AI-Note 15.1`) and theorem numbers do not move. |

  `\theainote` is `\thechapter.\arabic{ainote}`, already unique document-wide, so **no
  `\theHainote` entry is needed** — the `\theH...` block exists only for the environments that
  *share* the theorem counter. There is a `\crefname`/`\Crefname` pair.

  See `main.tex`'s theorem/`aliascnt`/`cleveref` block (roughly lines 410–640) for the current
  list of environments and their `\crefname`s.

* **Math Operators**: Use the macros already declared in the project's preamble, never raw
  `\mathrm{}` or `\text{}` for an operator name. If a needed operator has no macro yet, propose
  one (`\DeclareMathOperator`) rather than writing it out ad hoc.
* **Suggestions welcome**: You are encouraged to suggest more math operators or environments on the fly if you believe they will improve document consistency. Moreover, any suggestion on how to extend the instructions above are just as welcome.

## Build

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

**`main.pdf` is tracked.** `.gitignore` un-ignores it specifically, so the built document travels
with the source; every other root PDF stays ignored. The cost is that each rebuild which changes it
adds a ~2 MB blob to history permanently. Rebuild it in the same commit as the source change, so
the two never disagree.

MiKTeX at `C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`.
**Be careful with** the theorem / `aliascnt` / `cleveref` block at roughly `main.tex:410–640` —
its comments document real bugs already solved (duplicate hyperref anchors, `cleveref` printing
the wrong environment name for aliased counters). If you extend it, follow the existing pattern
exactly: every environment in this project is numbered, and every one of them except `ainote`
takes its number from the shared theorem counter. **Never leave a new environment unnumbered**,
because an unnumbered environment has no counter, so a `\label` placed inside it gets silently
misattributed to the last-stepped ambient counter, e.g. `\cref` printing "Section 2.d.4" instead
of "AI-Exercise 2.d.26". `ainote` is the exception in the other direction: it has a counter, just
not the shared one.
Adding a new environment means: `\newaliascnt{name}{theorem}`,
`\newtheorem{name}[name]{Display Name}`, `\aliascntresetthe{name}`, a `\theHname` entry in the
`\AtBeginDocument` block, and a `\crefname`/`\Crefname` pair — mirroring `lemma`/`corollary`/etc.

**The rule reaches theorem-like environments only.** `exerciseinfo` and `exercisehint` (added
2026-08-10) are plain `\newenvironment` formatting blocks with no counter and no `\crefname`,
and that is correct: the hazard above needs a `\label` to bite, and these always sit *inside* an
already-numbered `exercise` or `example`, which is what a reader cites. Do not "fix" them by
giving them counters. If you ever want to `\cref` one, that is the signal it should have been a
`remark` — the same test as `ainote`.

