# Build traps and preamble facts

Everything tied to *this* `main.tex`: how numbering is derived, which environments exist, the
traps that have each broken a build at least once, and how to compile. **Line numbers in this
file are checked against `main.tex` and go stale when it grows** — if one does not point where
it claims, fix it here rather than working around it.

| Companion file | What lives there |
|---|---|
| `gemini.md` | Role, fidelity policy, tool usage — read first |
| `style.md` | House style: prose, notation, environments, provenance conventions |
| `project-state.md` | Which tutor is the blueprint, what is done, standing decisions |

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
* **`ainote` is unnumbered (`\newtheorem*`) and must never carry a `\label`.** If you find
  yourself wanting to `\cref` one, it is content, not commentary — make it a `remark`. See the
  comment at its `\newtheorem*` in `main.tex`.
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
* **A literal `[` or `]` inside a `[...]` environment title closes the argument early.** An
  exercise titled `[$\mathbb{R}[x]$ is infinite-dimensional]` broke LaTeX's optional-argument
  bracket matching — the `[x]` ended the `\begin{exercise}[...]` argument, and the error surfaces
  nowhere near the title. Brace-protect it: `$\mathbb{R}{[}x{]}$`. Applies to any theorem-like
  environment title containing a bracket in math.
* **`main.pdf` is often locked** by an open viewer; `latexmk` then dies with
  *"I can't write on file"*. Build with `-jobname=check` to a throwaway name instead.
* **`hyperref` warnings about `Token not allowed in a PDF string`**.
  This happens when math commands (like superscripts `^`, subscripts `_`, or specific symbols) appear in chapter or section titles, which hyperref tries to use for PDF bookmarks. Fix this by wrapping the math in `\texorpdfstring{math}{text}`. For example, `\texorpdfstring{$\mathbb{R}^n$}{Rn}` instead of `\texorpdfstring{$\mathbb{R}^n$}{R^n}`. The second argument must be plain ASCII text without any math formatting.

## Verifying figures

Do **not** trust TikZ source. Build, render the page (`pdftoppm -png -r 95 -f N -l N`), and
*look*. Several figures in this document asserted things their own coordinates contradicted: a
chord whose endpoints were not on the curve, "tangent" lines tangent to nothing, an open cover
that did not cover, marked points sitting where the curve was at its minimum. Where a figure
encodes a computation, check the arithmetic in a comment above it (see FIG-W06-03, now in
`content/14-convexity/`, for the pattern).

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
\newtheorem*{ainote}{AI-Note}   % <- the ONE genuinely unnumbered environment
\newenvironment{exercisesolution}[1][Solution]{%
  \begin{proof}[#1]%
}{%
  \end{proof}%
}
% \newterm  -> ENGLISH quotes (main.tex:188). \germanterm (main.tex:189) is the
% \glqq...\grqq one. They are deliberately different -- the German-mirroring
% convention in project-state.md depends on it. Do not collapse them.
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

  **The one exception is `ainote`, which IS `\newtheorem*` and unnumbered** (`main.tex:570`).
  The hazard above needs a `\label` to bite, and an AI-Note never carries one: it is editorial
  commentary about the transcription, not a result anyone cites. Numbering them only inflated
  the shared theorem counter, so that a Lemma 2.f.43 was followed by a Definition 2.f.46 with
  two AI-Notes in between. There is therefore no `\theHainote` entry and no `\crefname` for it
  either.

  **Corollary of that exception:** if you find yourself wanting to `\label` an `ainote`, that is
  the signal it is *content*, not commentary — convert it to a `remark` (see the semantics
  semantics section of `style.md`). See `main.tex`'s theorem/`aliascnt`/`cleveref` block (roughly
  lines 410–640) for the current list of environments and their `\crefname`s.

* **Math Operators**: Use the macros already declared in the project's preamble, never raw
  `\mathrm{}` or `\text{}` for an operator name. If a needed operator has no macro yet, propose
  one (`\DeclareMathOperator`) rather than writing it out ad hoc.
* **Suggestions welcome**: You are encouraged to suggest more math operators or environments on the fly if you believe they will improve document consistency. Moreover, any suggestion on how to extend the instructions above are just as welcome.

## Build

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

MiKTeX at `C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`.
**Be careful with** the theorem / `aliascnt` / `cleveref` block at roughly `main.tex:410–640` —
its comments document real bugs already solved (duplicate hyperref anchors, `cleveref` printing
the wrong environment name for aliased counters). If you extend it, follow the existing pattern
exactly: every environment in this project is numbered **except `ainote`** (an unnumbered
environment has no counter, so a `\label` placed inside it gets silently misattributed to the
last-stepped ambient counter, e.g. `\cref` printing "Section 2.d.4" instead of
"AI-Exercise 2.d.26" — `ainote` is safe only because it never carries a `\label`).
Adding a new environment means: `\newaliascnt{name}{theorem}`,
`\newtheorem{name}[name]{Display Name}`, `\aliascntresetthe{name}`, a `\theHname` entry in the
`\AtBeginDocument` block, and a `\crefname`/`\Crefname` pair — mirroring `lemma`/`corollary`/etc.

