# House style — authoring rules

Durable rules for *how* the LaTeX is written: prose, notation, environments, and the
provenance conventions that go with transcribed material. Nothing in this file depends on a
`main.tex` line number or on how far the project has got, so it should need editing only when
a style decision actually changes.

| Companion file | What lives there |
|---|---|
| `gemini.md` | Role, fidelity policy, tool usage — read first |
| `build-and-preamble.md` | Build traps, `main.tex` facts, numbering, the preamble's environments |
| `project-state.md` | Which tutor is the blueprint, what is done, standing decisions |

## Expansion rules — shorthand into prose

* Transform lecture shorthand like "iff" into the full phrase "if and only if" in prose.
* Expand "s.t." to "such that" and "w.r.t." to "with respect to".
* **`i.e.` and `e.g.` follow the bracket rule — they are NOT on the expansion list above.**
  Inside parentheses or brackets, keep the abbreviation: a parenthetical is already an aside,
  and `(i.e.\ ...)` / `(e.g.\ ...)` keep it short instead of nesting a second clause inside the
  first. In running prose outside brackets, write it out ("that is,", "for example,",
  "for instance,") — or better, recast the sentence so no gloss is needed.

  * **GOOD:** `contracted to a point within $U$ (i.e.\ any two paths with the same endpoints are homotopic)`
  * **GOOD:** `a dense set (i.e.\ $\overline D = [0,1]$)`
  * **BAD:** `a dense set (that is, $\overline D = [0,1]$)`
  * **GOOD:** `Symmetry: $d(x,y) = d(y,x)$, that is, $x$ has the same distance to $y$ as $y$ to $x$.`
  * **BAD:** `Symmetry: $d(x,y) = d(y,x)$, i.e., $x$ has the same distance to $y$ as $y$ to $x$.`

  Note the spacing: inside brackets use `i.e.\ ` (backslash-space) before text, or `i.e., `
  before a clause — never a bare `i.e. `, whose period TeX reads as end-of-sentence and
  over-spaces.

  This rule applies to **typeset text only**. LaTeX comments (`% ...`) and TikZ node labels are
  out of scope: comments are never typeset, and figure labels need the shortest form that fits.
  Leave both exactly as they are.
* ⚠️ **Never apply any of these expansions with a blind search-and-replace over `content/`.**
  A pass on 2026-08-06 ran a Python `re.sub` across every `.tex` file and had to be reverted
  wholesale (the diff is kept at `scratch/gemini-pass-2026-08-06.patch`).
  It rewrote LaTeX comments and TikZ node text, produced `that is,:` and `no such $d$ exists, so`
  where the surrounding punctuation no longer fit, and split a math span across a line break
  (`--- e.g.\ $\tan :` became `--- for example, $\tan :$`), which put `\tfrac` in text mode and
  broke the build. This is the same hazard the perl warning under *Build traps* describes; the
  language does not matter. Edit the occurrences individually, reading each sentence.

## MATHEMATICAL NOTATION (THE HOUSE STYLE)

* **Definitional Equal Sign (`:=`):** Always use `:=` (colon-equal) when introducing a new symbol, defining a set/function/subspace, or making a local assignment in proofs and definitions (e.g., `Let $r := \rank(A)$`, `Let $Q := \begin{pmatrix} ... \end{pmatrix}$`, `\operatorname{Im}(T) := \{T(v) \mid v \in V\}`, `\langle \cdot, \cdot \rangle' := \langle \cdot, \cdot \rangle_A`). Reserve standard `=` strictly for mathematical equations, identities, and calculations between existing quantities.

  The test is **"am I naming something, or claiming something?"** Naming takes `:=`; claiming
  takes `=`. The distinction is easy to get wrong in both directions:

  | | Correct | Why |
  |---|---|---|
  | naming | `Let $X := \mathbb{R}^n$.` | $X$ did not exist a moment ago |
  | naming | `the Lagrangian $L := f - \lambda g$` | introduces $L$ |
  | naming | `with $g(x) := \lvert x\rvert^2-1$` | fixes what $g$ means |
  | **claiming** | `so $X = \bigcup_k B_\varepsilon(x_k)$` | an assertion to be proved, not a definition |
  | **claiming** | `$\dim M = m$` | a fact about $M$ |
  | **claiming** | `$\det = 27\alpha^2 > 0$` | the outcome of a computation |
  | **claiming** | `(with $\lambda = 1$)` | a value that was solved for, not chosen |

  Two standing exceptions. **(1)** Text quoted verbatim from an official problem sheet is never
  re-punctuated — leave its `=` alone even where the sheet is defining something. **(2)** In a
  chain like `$L(x,\lambda) := f(x) - \lambda g(x) = xyz - \lambda(\dots)$`, only the *first*
  sign is definitional; the rest is computation.
* **Matrices & Long Display Equations:** Use `\begin{pmatrix}` for displayed block equations `\[ ... \]` and `\left(\begin{smallmatrix} ... \end{smallmatrix}\right)` for 2D matrices in inline math `$ ... $`. **Tall / Block Matrices:** Large matrices or multi-row block representations (such as column-block matrices $\begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix}$ or matrices with 3+ rows) must NEVER be written inline inside `$ ... $`; always elevate them to display math `\[ ... \]`.
  * **Multi-line Equation Splitting:** Never let wide display equations with large matrix blocks overflow page boundaries. Split them using `align` or `split` at major equal signs or logical steps. Suppress intermediate equation numbers using `\nonumber` unless specifically referenced.
    * **BAD Example (Single-line overflow):**

      ```latex
      \begin{equation}
      \label{eq:unitary_matrix_product}
          A^* A = \begin{pmatrix} \text{---} & \overline{v_1}\transp & \text{---} \\ & \vdots & \\ \text{---} & \overline{v_n}\transp & \text{---} \end{pmatrix} \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} = \left( \overline{v_i}\transp \cdot v_j \right)_{1 \leq i \leq n, 1 \leq j \leq n} = \left( \langle v_j, v_i \rangle \right)_{1 \leq i \leq n, 1 \leq j \leq n}.
      \end{equation}
      ```

    * **GOOD Example (Structured multi-line alignment):**

      ```latex
      \begin{align}
      \label{eq:unitary_matrix_product}
          A^* A &= \begin{pmatrix} \text{---} & \overline{v_1}\transp & \text{---} \\ & \vdots & \\ \text{---} & \overline{v_n}\transp & \text{---} \end{pmatrix} \begin{pmatrix} | & & | \\ v_1 & \dots & v_n \\ | & & | \end{pmatrix} \nonumber \\
          &= \left( \overline{v_i}\transp \cdot v_j \right)_{1 \leq i, j \leq n} \nonumber \\
          &= \left( \langle v_j, v_i \rangle \right)_{1 \leq i, j \leq n}.
      \end{align}
      ```

  * **Overfull `\hbox` / Too Long Formulas:** Never let long formulas overflow the page margins (producing `Overfull \hbox` warnings). Break long equations using `align` (or `align*`) or `split` inside `equation`. Align multiline equations on logical relations (like `=`) or mathematical operators (like `+` or `-`).
    * **BAD Example (Single-line overflow):**

      ```latex
      \begin{equation}
          \int_A f(x,y,z) \,dx\,dy\,dz = \int_0^1 \int_0^{1-x} \int_0^{1-x-y} (x^2 + y^2 + z^2 + 2xy + 2xz + 2yz) \,dz\,dy\,dx = \frac{1}{20}
      \end{equation}
      ```

    * **GOOD Example (Structured multi-line alignment):**

      ```latex
      \begin{align}
          \int_A f(x,y,z) \,dx\,dy\,dz &= \int_0^1 \int_0^{1-x} \int_0^{1-x-y} (x^2 + y^2 + z^2 \nonumber \\
          &\qquad + 2xy + 2xz + 2yz) \,dz\,dy\,dx \nonumber \\
          &= \frac{1}{20}.
      \end{align}
      ```

    * **Inline Fractions:** Prefer the slash form `x/y` to `\frac{x}{y}` inside inline math
      `$ ... $` — a stacked fraction stretches the line height and invites `Overfull \hbox` or
      `Underfull \hbox`. This is about the *fraction*, not the delimiters around it: where an
      inline `\frac` is genuinely unavoidable, it is "exceptionally tall" content in the sense of
      the **Delimiters** rule below, so size the brackets around it with `\left ... \right`
      rather than forcing standard-size braces onto tall content.
    * **TikZ Pictures:** If a `\begin{tikzpicture}` overflows the page width (producing an `Overfull \hbox`), check the `xshift` of scopes or manually scale it down, rather than ignoring the warning.

* **Delimiters — this rule governs inline bracket sizing.** Use `\left(` and `\right)` (and other
  auto-sizing delimiters like `\left[` / `\right]`) freely in displayed equations `\[ ... \]`, so
  that delimiters match the height of their content. In inline math `$ ... $`, standard delimiters
  are preferred, to keep the line height even — **unless the content is exceptionally tall**, in
  which case auto-sizing wins. The two tall inline cases that actually arise in this project are a
  `smallmatrix` and an unavoidable `\frac`; both take `\left ... \right`. Where *Matrices* above
  prescribes `\left(\begin{smallmatrix}...\end{smallmatrix}\right)`, that is this exception being
  applied, not a competing rule.
* **General Linear Group:** Always use the macro `\GL` for the general linear group (e.g., `\GL_n(K)` or `\GL(n, K)`). This renders as `\operatorname{GL}`.
* **Curl / Rotation:** Always use the macro `\curl` for the curl/rotation of a vector field. Do NOT use `\rot`, as it is not defined and will break compilation.
* **Sub-part Labels:** Always use alphabetical numbering for sub-parts, items, and cases (e.g., `\textbf{(a)}`, `\textbf{(b)}`). Do NOT use numerical labels like `(1), 2)`. This applies to proof sections, lists, and TikZ nodes. **Important:** Do NOT hardcode custom labels using `\item[...]` — this applies to **both** `itemize` and `enumerate`, with no exceptions. Instead, set `\begin{enumerate}[label=\textbf{(\alph*)}]` on the environment itself and use plain `\item`; for `itemize`, use plain `\item` and put any name/label as `\textbf{name:}` at the start of the item's text. **Proof Sub-parts:** Do NOT write `Proof of (a):` or use `\item[...]`. Write sub-part proof headers using `\begin{enumerate}[label=\textbf{(\alph*)}]` with plain `\item`, or write `\textbf{(a)}` directly in prose. When referencing a specific sub-part or custom enumerate label in prose, maintain the bold formatting (e.g., "statement \textbf{(d)}", "from \textbf{(K4)}"). If a theorem/proposition statement uses an `enumerate` environment to list sub-claims/points, any proof that proves those individual points must also structure its proof using an identical `enumerate` environment matching those points.
* **Labels:** Use descriptive, human-readable slugs for labels instead of numbering schemes. For example, use `\label{prop:unique_solution_criterion}` instead of `\label{prop:17.d.4}`. If possible (i.e. available), always place the original handwritten note label as a comment directly above the new descriptive label (e.g., `% prop:17.d.4`). This avoids duplicates and makes the LaTeX source much easier to navigate. **Placement:** Always place the `\label{...}` immediately after the `\begin{...}` statement (e.g., right after `\begin{theorem}`), rather than at the end of the environment.
* **Cross-Referencing:** Use `\cref{...}` (from the `cleveref` package) for referencing sections, theorems, propositions, lemmas, and definitions. `\cref` automatically adds the appropriate label (like "Theorem 1"), so do not add manual prefixes. **Important:** If a sentence starts with a reference, use `\Cref{...}` instead so that the word is properly capitalized (e.g., "Theorem 1"). Use `\eqref{...}` exclusively for referencing equations (this automatically adds parentheses around the number).
* **Lists with Descriptions — the `description` environment is FORBIDDEN.** For lists where
  each item has a specific name or title (e.g., "Associativity", "Distributivity"), use `itemize`
  (or `enumerate` if order matters) instead, with the name bolded inline at the start of the
  item's text: `\item \textbf{Associativity:} ...`. Do not use `description` for any purpose. For
  standard numbered lists, use `enumerate` but do not hard-code labels; rely on the global style
  defined in the preamble.
* **New Terminology & Quotes:** Use `\newterm{...}` for introducing newly defined mathematical terms (the first definition or formal introduction of a concept). Use `\qt{...}` strictly for quoting text, literal quotes, colloquial terms, or informal emphasis—never use `\qt{...}` where a term is being formally defined or introduced for the first time.
* **Raw ASCII double quotes `"..."` are FORBIDDEN in typeset text.** They render as `”…”` —
  two *closing* quotes — because TeX has no notion of an opening `"`. Always use `\qt{...}`
  instead (or, where `\qt`'s italics are unwanted, the explicit ``` ``...'' ```).

  * **BAD:** `statements like "every bounded sequence has a convergent subsequence" need new proofs`
  * **GOOD:** `statements like \qt{every bounded sequence has a convergent subsequence} need new proofs`

  This applies to scare quotes, quoted phrases, colloquialisms, and quoted source strings alike.
  It does **not** apply inside LaTeX comments (`% ...`), which are never typeset. Note that
  grepping for `"` produces false positives from umlaut escapes (`\"a`, `\"o`, `\"u`); filter
  those out before assuming a hit is real.

* **Custom bracketed names on theorem environments are encouraged.** All theorem-like
  environments (`theorem`, `lemma`, `definition`, `proposition`, `corollary`, `claim*`,
  `example`, `remark`, `exercise`, etc.) **should** carry a descriptive `[...]` name/title where
  a natural one exists. Examples: `\begin{theorem}[Heine--Borel]`,
  `\begin{definition}[Metric space]`, `\begin{lemma}[Gronwall's inequality]`. This applies
  retroactively; adding names to existing environments is encouraged when revisiting a file.
  * **Not every environment needs one.** A short `ainote` correcting a slip, or a one-line
    `remark`, reads better untitled than with a laboured title. Roughly 1 in 6 `ainote`s in
    Weeks 1–7 carry a title, and that ratio is about right: title it when the title *names*
    something ("Lebesgue's covering lemma", "Corsin's recommendations"), not when it merely
    restates the first sentence.
  * **`question` and `answer` take NO optional argument** — see the build traps in
    `build-and-preamble.md`.
  * **Sole exception — `proof` immediately after its parent environment:** A `proof`
    environment that directly and immediately follows the theorem/proposition/lemma it belongs
    to does **not** need a `[Proof of \cref{...}]` label — the adjacency already makes the
    connection clear. Add a `[Proof of \cref{...}]` title only when the proof is separated
    from its statement (e.g., deferred to a solution section or a later page).
  * **Macro restrictions inside `[...]` still apply:** NEVER use `\qt{...}`, `\newterm{...}`,
    or other formatting macros inside the bracketed header argument — plain text and math are
    safe, macros with fragile arguments are not. `\cref{...}` is safe inside
    `exercisesolution[...]` and deferred `proof[...]` headers.

## GRAMMAR AND PROSE STYLE

* ⚠️ **Em-dashes (`---`) are a last resort.** A pass on 2026-08-09 counted **1006** of them in
  `content/`, against **6** in the whole of the sibling `en-linalg-biran-gemini` project. That
  ratio is the problem: a mark that is meant to signal a rupture had become this document's
  default connector, so nothing it marked read as a rupture any more.

  **The rule is not a quota, it is a test.** Before keeping an em-dash, ask: *does a comma, a
  colon, a semicolon, a pair of parentheses, or a full stop carry this?* If any of them does,
  use it. An em-dash survives only where the sentence genuinely breaks off and no other mark
  reproduces the break. Expect that to be rare — of the order of one per two or three pages.

  Most occurrences fall into five patterns, each with a standard repair:

  | Pattern | Repair |
  |---|---|
  | Paired parenthetical: `the set --- also called a space --- which we denote $X$` | commas, or real parentheses |
  | Standing in for a colon: `\textbf{No} --- the triangle inequality fails` | `\textbf{No:} the triangle inequality fails` |
  | Standing in for a semicolon: `something very obvious --- see the picture above` | `something very obvious; see the picture above` |
  | Hint/label separator: `\textbf{3.9.2} --- recall that...` | `\textbf{3.9.2:} recall that...` |
  | Tacked-on afterthought: `..., not merely a candidate --- which still needs checking` | make it its own sentence, or cut it |

  **Legitimate survivors** are the cases where the break *is* the point: a self-interruption
  that reverses direction (`the obvious guess --- and it is wrong --- is that ...`), or a final
  sharpening that must not read as a smooth continuation. If in doubt, repunctuate.

  * **BAD** (two paired parentheticals in one paragraph, neither a rupture):
    ```latex
    Each induces the next --- $\|v\| := \sqrt{\langle v,v\rangle}$ and $d(x,y) := \|x-y\|$ ---
    and neither implication reverses.
    ```
  * **GOOD:**
    ```latex
    Each induces the next, via $\|v\| := \sqrt{\langle v,v\rangle}$ and $d(x,y) := \|x-y\|$,
    and neither implication reverses.
    ```

  **Scope.** This governs typeset text only. LaTeX comments (`% Generator: ... --- ...`) are
  never typeset and are out of scope, as are en-dashes (`Cauchy--Schwarz`, `pp. 13--14`), which
  are a different mark doing a different job. **Never repair these with a global
  search-and-replace** — the ban a few sections above applies with full force, because the
  correct repair differs per sentence and roughly one occurrence in five is inside a comment.

  ⚠️ **Do not simply move the tic** — and note that the two obvious places to move it to are
  already full. Counting both documents per 1000 lines of prose (comments excluded) on 2026-08-09:

  | | `en-linalg-biran-gemini` | this document |
  |---|---|---|
  | `;` | 55 | **96** |
  | `:` | 202 | **295** |
  | `Therefore,` `Thus,` `Hence,` `Consequently,` | **19.3** | 2.1 |
  | `, which implies` | 4.0 | ~0 |
  | `Note that` / `Recall that` | 6.7 | 1.7 |

  Read the bottom three rows against the top two and the actual difference in flow becomes
  legible. **The reference joins sentences with words; this document joins clauses with
  punctuation.** The em-dash count is the most visible symptom of that habit, not the disease.

  **Therefore the default repair is a full stop plus a connective, not a smaller mark.** Reach for
  `Therefore,` / `Consequently,` / `Hence,` / `Thus,` / `Note that` / `Recall that` before
  reaching for a semicolon, and treat every repair that adds a `;` or a `:` as spending from a
  budget that is already overdrawn.

  * **BAD** (dash → semicolon: the sentence is still doing two jobs):
    ```latex
    The determinant is non-zero; the matrix is therefore invertible.
    ```
  * **GOOD** (two sentences, joined by a word):
    ```latex
    The determinant is non-zero. Consequently, the matrix is invertible.
    ```

* **Logical Arrows:** The default for prose should be natural words (e.g., This implies that, Consequently, Therefore, Hence, Thus, if and only if). Handwritten shorthand like "iff" must be expanded to "if and only if" in prose text, but the macro `\iff` is fully permitted in math. Avoid overusing isolated `\iff` arrows interspersed with prose (e.g., alternating between inline `\iff`, prose fragments, and `\iff` again); choose full English phrasing like "if and only if" whenever it makes the sentence sound more natural. Avoid using `\implies` inside displayed equations (`\[ ... \]`); write out logical implications using full prose (e.g., ", which implies that", "Consequently,") between separate display equations instead. `\implies` should still be used sparingly.

  The line to draw: an arrow may **join two equations**; it may not **replace a verb**.

  * **BAD** (arrow standing in for "hence", inside a display):
    ```latex
    $$\nabla f(x,y) = (y,x)\transp = (0,0)\transp \implies (x,y) = (0,0)$$
    ```
  * **GOOD** (the deduction is prose, the display holds only mathematics):
    ```latex
    The critical points satisfy $\nabla f(x,y) = (y,x)\transp = (0,0)\transp$, and therefore
    $(x,y) = (0,0)$.
    ```
  * **BAD** (an `\iff` plus a slash carrying two definitions at once):
    ```latex
    \item \textbf{Strict} min/max $\iff f(x) > f(x_0)$ / $f(x) < f(x_0)$.
    ```
  * **GOOD:**
    ```latex
    \item The extremum is \textbf{strict} if the inequality is strict: $f(x) > f(x_0)$ for a
      strict minimum, $f(x) < f(x_0)$ for a strict maximum.
    ```

  Arrows are fine inside a genuine chain of algebra (`$x^{3/2} = (x')^{3/2} \implies x = x'$`),
  where both sides really are equations and no English is being displaced.
* **`Fix ...` is house-preferred for introducing a variable** (`Fix $t > 0$`, `Fix $x \in X$ and
  let $\varepsilon > 0$`). It is idiomatic, it signals that the variable is arbitrary but held
  constant for the argument, and it should not be edited away in favour of `Let` or `Consider`.
  The one case where it is genuinely wrong is fixing a variable and then defining a *function*
  of that same letter (`Fix $t>0$ and define $g(t) := \dots$`, which fixes $t$ and then quantifies
  over it). There, fix the parameters and define the function properly:
  `Fix conjugate exponents $p,q>1$, and define $g : (0,\infty) \to \mathbb{R}$ by $g(t) := \dots$`.
* **Sophisticated Academic Prose:** Maintain a formal, structural tone.
* **Introductory Phrases:** Always place a comma after introductory adverbs (e.g., Clearly, So, Moreover, In this case, Hence, Thus, Next).
* **Conjunctions:** Where grammatically sound, use commas around transition phrases like ", and therefore," (e.g., The determinant is non-zero, and therefore, the matrix is invertible.).
* **Structural Flow:** Use commas to separate conditional clauses (If... , then...), but avoid grammatically incorrect commas before "that" or between verbs and objects. Use commas in front of "and therefore" if appropriate.
* **Syllabication:** To assist LaTeX with professional justification and avoid margin overflows, use manual hyphenation hints for long technical terms. For example, always use `finite-di\-men\-sional` instead of the plain version.
* **Punctuation and Math Mode:** Always place standard punctuation (like commas or periods) *outside* of inline math mode (e.g., `$x=2$,` instead of `$x=2,$`) to ensure proper spacing.

## PROSE ARCHITECTURE — where text goes, and how much of it

Three rules about *placement and quantity* of prose, as opposed to its wording. All three were
added 2026-08-09 after a read-through found the document generous with prose in the places it
does not help and thin in the places it does.

* ⚠️ **Nothing may spoil an exercise before the reader has attempted it.** A note about the
  common mistakes on a problem, a warning about the trap in part 4, a summary of what most
  students got wrong: all of these are useful, and all of them are useless *above* the exercise,
  because a reader who has been told the answer cannot then find it.

  **Placement:** a genuine *hint* (of the kind the official sheet prints) may sit directly under
  the statement, clearly marked as a hint. Anything that reveals the answer or names the wrong
  answer goes into the chapter's `99-solutions.tex`, next to the solution it concerns.

  * **BAD** — sitting above `\cref{ex:1.1}`, disclosing parts 2 and 4:
    ```latex
    Two mistakes are worth flagging before attempting \cref{ex:1.1}: on part 2, most students
    first guessed $f(x) = \log|x| + c$ for a single constant $c$ --- wrong, since ...
    ```
  * **GOOD** — the same text, moved into the solution section, where it is a post-mortem
    rather than a giveaway.

  The same applies to an `ainote` that says which method the solution will use, and to a
  `remark` placed above an exercise that quietly states the exercise's own conclusion.

* **The register to write in, stated concretely.** "Write like `en-linalg-biran-gemini`" is not
  actionable on its own. What that document actually does, measured against this one:

  | It does | Rather than |
  |---|---|
  | Short declarative sentences, one clause each | Long sentences held together by dashes and semicolons |
  | Says the thing, then qualifies it in a new sentence | Qualifies mid-sentence inside a parenthetical |
  | Uses a **question** as a transition: *"What about over $\mathbb{C}$?"*, *"Is the converse true?"* | Announces the next topic administratively |
  | Plain connectives: *Consequently*, *Therefore*, *Now assume*, *We wish to* | Elaborate hedged connectives |
  | Addresses the reader as *we* doing mathematics together | Describes the document's own structure |
  | Lets a definition follow a one-sentence motivation, then stops | Prefaces every definition with a paragraph |

  The single most transferable habit is the third: at a genuine change of direction, ask the
  question the reader is about to ask, then answer it. It costs one short line and does the work
  that a paragraph of framing usually fails to do.

* **Framing prose: add it only where a reader would otherwise be lost.** The register to aim for
  is the sibling `en-linalg-biran-gemini` project: prose is sparse, and every sentence of it is
  load-bearing. A short paragraph earns its place if it answers one of

  - *what is this chapter for, and what does it need from the previous one?*
  - *why are we suddenly doing this?* (at a genuine change of subject inside a chapter)
  - *what just happened?* (after a long proof or a run of definitions, where the payoff is not
    self-evident)

  and does not earn it if it merely announces the table of contents ("In this section we define
  X, then prove Y, then give examples"). **A chapter stub with no intro is better than a chapter
  stub with a paragraph of throat-clearing.** Two to four sentences is the working range; if a
  fifth is needed, the material probably wants a `remark` next to the mathematics instead.

* **`\part` prose is the exception that should be fuller.** A part opener is the only place a
  reader meets a thematic block as a whole, and it is read once, deliberately. Four to six
  sentences: what unifies the chapters, what earlier machinery they consume, and what the block
  buys that the previous one could not do. Do not list the chapter titles; the table of contents
  already does.

## TYPOGRAPHY & SPACING RULES

* **Paragraph Spacing & Indentation:** Paragraph indentation is set globally to `\setlength{\parindent}{0pt}` with `\setlength{\parskip}{3pt plus 1.5pt minus 0.5pt}`. Paragraphs must NEVER have indentation — whether preceded by `\section`, `\subsection`, or `\subsubsection`, or followed/preceded by `itemize` or `enumerate`.
* **List Spacing:** Top-level and nested `itemize`/`enumerate` environments use compact zero-spacing (`topsep=0pt`, `itemsep=0pt`, `parsep=0.5\customparskip`).
* **Theorem Environment Spacing:** All theorem-like environments use `\customenvspace` (`2.0ex plus 0.5ex minus 0.2ex`) for above and below spacing.
* **Line Spread:** Line spread is configured to `\linespread{1.05}` across the entire document.

* **Commutative Diagrams:** Always use the `tikz-cd` package for commutative diagrams.
* **Coordinate Calculations:** In TikZ `\draw` and `\node` coordinates, unbraced math expressions containing commas or operations will fail to parse (e.g., `at (2.6, 1.0 + 0.3*sin(...))`). Always enclose coordinate math expressions in curly braces `{}` (e.g., `at (2.6, {1.0 + 0.3*sin(...)})`) or pre-calculate the numeric coordinate (e.g., `at (2.6, 1.06)`).
* **Multi-line Node Text:** `\node[align=center] {Line 1\\Line 2}` is fine and is what this
  project uses throughout — no `text width` is required, provided the node text is non-empty and
  contains an explicit `\\`. The *"A node must have a label text"* error comes from an
  **empty or absent** node body (e.g. a stray `node {}` left on a `plot`), not from `align`
  itself; look for that instead. `\shortstack{...}` also works but nests badly inside `tabular`
  and is not needed here.
* **Function Plot Domains & Overflow:** When plotting functions with singular or rapidly growing terms near $0$ (such as $\sin(1/t)$ for the topologist's sine curve), bound the plot domain strictly away from zero (e.g., `domain=0.08:2.8`) to avoid PGF math `! Dimension too large` errors.
* **TikZ `cos`/`sin` read their argument in DEGREES, not radians.** A phase-portrait spiral
  written as if the plot parameter were radians overflowed PGF's dimension limit — the growth
  rate has to be recalibrated per degree. If a parametric plot blows up with `Dimension too
  large` and the domain is already sane, check this before anything else.
* **Scope Syntax:** Always terminate `\end{scope}` cleanly with a closing brace `}`, never a trailing semicolon (e.g., avoid `\end{scope};`).
* **Rotation and Transformation Syntax:** In TikZ scope transformations, always use spaces in rotation keys (e.g., `rotate around x=65`) or define explicit 3D coordinate system vectors (e.g., `x={(0.866cm,-0.3cm)}, y={(0.5cm,0.4cm)}`). Never write unspaced key strings like `rotatearound x`, which cause PGF key parsing errors.
* **Environment Centering:** Wrap inline TikZ figures in standard `\begin{center} ... \end{center}` environments or floating `figure` environments.
* **Figure Stubs — write specs, not pointers.** When a diagram cannot be drawn immediately,
  the stub must be a self-sufficient *drawing specification* so that no one needs to reopen the
  source PDF to reconstruct it. Capture: relative positions of all objects, which lines are
  solid / dashed / dotted, arrow directions and what they connect, label text and placement,
  panel layout, and roughly where curves bend or cross. Name any colours used by the author.

  - **Pointer (forces a re-read):** "blob $X$ covered by three dotted regions."
  - **Spec (self-sufficient):** "kidney-shaped blob $X$; three overlapping dotted ellipses at
    roughly 10, 2 and 6 o'clock, each crossing the boundary outward; labels $U_1$–$U_3$
    outside the blob next to their ellipse; caption $U_1\cup U_2\cup U_3=X$."

  A good spec costs nothing extra when the source is on screen and removes an entire
  second pass over it later.

## OPERATIONAL DIRECTIVES

* **Inline Edits:** When performing inline edits, prioritize keeping the surrounding LaTeX syntax intact.
* **Logic Checks:** If a proof seems circular or a matrix calculation is visibly incorrect, flag
  it in an `ainote` while applying the stylistic edits, and mention it to the user in your reply.
* **Commit Messages:** When asked to generate a commit message, be specific about the mathematical or stylistic changes made.
* ⚠️ **Flagging errors — `ainote` is the whole system.** If a source appears to contain an error,
  say so in an `ainote` at that spot, stating what the source says, what it should say, and
  whether you changed it. Do **not** silently substitute a corrected version.

  There is no separate register to update: **this project has no open-questions file, and no
  OQ numbering.** Earlier revisions of this file referred to both, and to flagging errors with
  `\omitted{...}` or "a dark-red note" — all three are dead. `\omitted` is still defined in the
  preamble, marked *"kept for future use if needed"*, but is used nowhere in `content/`; do not
  reach for it. One mechanism, in one place, next to the mathematics it concerns.
* **Illegible source text:** Mark as `⟨?word⟩` inline in the `.tex` and add an `ainote` saying
  what is unreadable and where. Never guess silently.
* **Custom Sections:** You are allowed and encouraged to inject custom `\section`, `\subsection`,
  and `\subsubsection` headings wherever they improve readability or navigation — do not feel
  constrained by the existing structure. Adding logical subdivisions that are not present in the
  handwritten source is an editorial decision you are empowered to make.
* **Source Provenance Comments:** At the top of each section (or logical block of content) in
  every `content/*.tex` file, insert a LaTeX comment recording where that content comes from:

  ```latex
  % Source: Corsin Nick/Class Notes/Week 5.pdf, pp. 1--3
  \section{Compactness}
  ```

  Use a **relative path** from the project root (e.g., `Corsin Nick/Class Notes/Week 5.pdf`)
  and a **page range** (`pp. N--M`; use `p. N` for a single page). The tutor's name is already
  visible from the path, so no additional attribution prose is required inside the comment.
  *Granularity:* one comment per section (or sub-section if a single section spans material
  from multiple pages or tutors) is sufficient — do **not** add a provenance comment per
  theorem or definition, as this would inflate token cost without proportionate benefit.
  When a supplement from a second tutor is merged in, add a second comment line:

  ```latex
  % Source: Corsin Nick/Class Notes/Week 5.pdf, pp. 1--3
  % Supplement: Sascha Brack/Ex Sheet Hints/Serie05Hints.pdf, p. 2
  \section{Compactness}
  ```

* ⚠️ **Provenance comments have SCOPE — this is the rule broken most often.**
  A `% Source:` / `% Quelle:` / `% Supplement:` comment is not a decoration attached to the one
  line beneath it. **It claims everything below it until the next provenance comment.** Stated
  that way the rule below is obvious; stated any other way it keeps getting forgotten, because
  it never feels like it applies to whatever you happen to be inserting.

  **Consequence: any block you insert into transcribed material steals that material's
  attribution.** It does not matter what the block is --- a remark, an example, an exercise, a
  figure, an `ainote`, a transition. If transcribed content resumes below your insertion, you
  must repeat the comment above it.

  ```latex
  % Source: Corsin Nick/Class Notes/Week 4.pdf, p. 4
  \begin{example}[Derivative of a curve]...\end{example}

  \begin{ainote}...\end{ainote}                        % <- your insertion

  % Source: Corsin Nick/Class Notes/Week 4.pdf, p. 4    % <- MUST be repeated
  From this example, we see that the columns of the Jacobian are ...
  ```

  The second failure mode is the same principle running the other way: **never let your own
  `% Supplement:` comment come to rest directly above someone else's content.**

  ```latex
  % BAD -- now reads as though problem 8.2 came from Sascha's file
  % Supplement: Sascha Brack/Ex Sheet Hints/Ex8_Analysis2_hints.pdf
  \begin{ainote}...his priorities...\end{ainote}
  \begin{exercise}[8.2 --- True or False]

  % GOOD
  % Supplement: Sascha Brack/Ex Sheet Hints/Ex8_Analysis2_hints.pdf
  \begin{ainote}...his priorities...\end{ainote}
  % Source: exercises/Ex8_Analysis2_eng.pdf, p. 1
  \begin{exercise}[8.2 --- True or False]
  ```

  **Verify afterwards; do not rely on remembering.** After inserting, scroll *down* to the next
  transcribed block and ask whether the nearest provenance comment above it is still the right
  one. To see every claim boundary in a chapter at once, run the search tool in regex mode over
  that chapter's directory (e.g. `content/10-chain-rule/`) with the pattern

  ```
  ^% (Source|Quelle|Supplement|Generator|Transition|Originally):
  ```

  Read the result as a list of ranges: every transcribed block must sit inside a range naming
  *its own* source. (Use the search tool, not a terminal `grep` — see *Tool Usage*.)

* **Exercise Solutions — mirror the source, and record the decision in-line.** Where a solution
  lives in the LaTeX depends on how the *original tutor's own handwritten notes* present it for
  that specific exercise — check the source PDF, don't default blindly:
  * **If the tutor solves the exercise immediately in their own notes** (e.g. a handwritten
    "Exercise: ... Solution: ..." block, solved right there on the page), **keep the solution
    inline** in the LaTeX too, directly after the `exercise` environment, exactly mirroring the
    source's structure. Immediately above that `exercisesolution`, add a one-line comment
    recording *why* it is inline and citing the precise source page, e.g.
    ```latex
    % Kept inline: solved directly in Corsin Nick/Class Notes/Week 2.pdf, p. 6.
    \begin{exercisesolution}[...]
    ...
    \end{exercisesolution}
    ```
    This makes the placement decision traceable in the source itself, not just in an edit
    summary. This applies to **every** tutor's notes as they get merged in, not only Corsin's.
  * **If there is no source solution to mirror** — e.g. the exercise is quoted verbatim from the
    official problem sheet and the tutor only gives a hint/priority marker rather than a worked
    solution, or the exercise is an `aiexercise`/`aiexample` invented for these notes — collect
    its solution into the chapter's `99-solutions.tex`, which holds a single
    `\section{Solutions}` at the **end of the chapter**, after all other content, ordered to
    match the order the exercises first appear in the chapter. A solution always lives in the
    chapter that hosts its exercise — never in a different one.
  * **Every `exercise` in a chapter must have a corresponding `exercisesolution`** somewhere
    (inline or in the end-of-chapter section per the rule above) — this includes exercises
    quoted verbatim from the official problem sheet. When the tutor left no worked solution and
    you must write one yourself, mark it with `% Generator: <model name> (<effort>)` directly
    inside the `exercisesolution`, matching the `aiexercise`/`aiexample` convention.
    **Derive your own solution first, and only open `SolN_Analysis2_eng.pdf` afterwards, to
    check it.** Reading the official solution before attempting the problem lets it steer your
    method and phrasing even when you don't copy it outright, which defeats the point of an
    independent check — you end up confirming your own anchoring bias, not verifying correctness.
    Work the problem cold, then compare. Cross-check your solution against the official
    `SolN_Analysis2_eng.pdf` where one exists; if your reasoning or final answer genuinely
    diverges from it, flag the divergence in an `ainote` right there — never silently prefer
    your own answer over the official solution without saying so. Even when your solution agrees with the official one, feel free
    to add an `ainote` for anything genuinely worth flagging about the master solution or the
    exercise itself — a subtlety it skates past, a non-obvious step, a result that looks
    surprising at first, or a detail (like a critical point being only a *local*, non-global
    extremum) that's easy to miss. This is about noteworthy observations, not routine restating
    of the solution.
  * **Never delete a tutor's original worked solution.** If you are unsure whether a solution
    already existed before an edit, check the source PDF before assuming it should be
    reconstructed — but if it turns out the tutor's own solution was removed by mistake,
    transcribe it back in (citing its page, as above) and keep any AI-authored alternative as a
    clearly separate, additional `exercisesolution` rather than overwriting it.
  * When an exercise is tied to a specific numbered environment, use `\cref` to reference it in
    the solution title, preferring the word "Proof" if it is a proof (e.g.,
    `\begin{exercisesolution}[Proof of \cref{prop:properties_adjoint_matrix}]`). To reference
    specific subitems (e.g., part (c) of a Lemma), combine `\cref` with the bolded letter
    manually (e.g., `\begin{exercisesolution}[Proof of \cref{lem:properties_adjoint_map}
    \textbf{(c)}]`). If the exercise is tied to an *unnumbered* environment (like a `claim*`),
    you must add a label to that environment and reference its page number in the solution title
    using `\cpageref` along with a highly descriptive name. For example:
    `\begin{exercisesolution}[Proof of Linearity of $\varphi_u$ (on
    \cpageref{claim:linearity_phi_u})]`.

* **Editorial transitions between spliced source content — tag them, as a reflex, not a
  process.** When you write a short bridging sentence or paragraph to smooth the join between
  two blocks of transcribed/quoted content (rather than transcribing it from any source), mark it
  with a brief comment naming the model that wrote it, e.g. `% Transition: Claude Sonnet 5` (this
  project's sessions have also used the equivalent shorthand `% Sonnet 5 (Medium)` — either is
  fine, pick one and be consistent within a file). **If transcribed content resumes below your
  insertion, re-cite its source comment above it** — see the *Provenance comments have SCOPE*
  rule earlier in this section, which applies to every kind of insertion, not only transitions.
  Keep this lightweight — a one-line comment each time, not a ceremony.
* **Integrating a second tutor's supplementary material** (not the primary blueprint tutor) into
  an already-transcribed section: cite it with a `% Quelle: <relative path>` (or `% Source: ...`)
  comment naming the exact file, and where relevant the page/section, e.g.
  `% Quelle: Diego Torres Tejeda/Addendum - Sequential and Topological Compactness.pdf`. State in
  an `ainote` *why* the primary tutor's notes don't already cover it (skipped, stated without
  proof, etc.) before presenting the supplement, and reformulate rather than copying verbatim.

## ENVIRONMENT SEMANTICS — WHAT GOES WHERE

Each environment has a precise semantic role. Using the wrong one is a style error.

* **`remark`** — for mathematical or pedagogical remarks that are directly about the
  mathematical content: a subtlety of a definition, a common pitfall, a clarifying observation.
  Do **not** use `remark` to make meta-comments about a tutor's notation style, about your own
  AI limitations, or about the typesetting process.
  * **Settled: didactic content goes here — do NOT add a separate environment for it.** The
    sibling project `eth-grundstrukturen-fs2026-ki-transkription` has a `didactic-insight`
    tcolorbox, and it works well there (36 uses, on par with its 34 `remark`s). It was
    considered for this project and **rejected**: its content splits into history/philosophy
    (Hilbert, the Wiener Kreis, Cantor) plus three categories — why a hypothesis is essential,
    proof ideas, appreciation of a technique — that are ordinary `remark`s. Only the first is
    genuinely homeless, and Grundstrukturen is full of it because logic and set theory *are*
    philosophical. Analysis II has almost none (the Galois/Abel note in `content/14-convexity/` is about
    the only instance in eight weeks), so the box would stand near-empty and the other three
    categories would drift into it. Use a **titled** remark instead —
    `\begin{remark}[Why this hypothesis is there]` — which buys the same skimmability with no
    new semantics and no twelfth colour-coded box competing with `importantremark`.
* **`notation`** — strictly for introducing or summarising notation conventions used by the
  author in their notes. Do **not** use `notation` to comment on the fact that a particular
  tutor uses unusual notation — that is an `ainote`.
* **`ainote`** (AI-Note) — for **all** meta, editorial, and AI-generated observations that
  are not part of the mathematical content itself. Use it for:
  - Comments about the typesetting process, transcription choices, or source ambiguity.
  - Observations about a tutor's idiosyncratic notation that differ from standard usage.
  - Flagging suspected or confirmed errors in a source (see *Flagging errors* above — the
    `ainote` is the flag; there is no separate register).
  - Any remark where you are injecting knowledge that goes beyond what the source says.
  Example:
  ```latex
  \begin{ainote}
    The author writes $\|\cdot\|_*$ for the operator norm, which is non-standard
    in this course; most texts use $\|\cdot\|_{\mathrm{op}}$. The author's
    notation is preserved here.
  \end{ainote}
  ```
  An `ainote` is the **only** place for AI self-reference or editorial intervention. Never
  smuggle such content into a `remark`, `notation`, or any semantic mathematical environment.

  **Two tests, applied in order.** The first sorts mathematics from commentary; the second, added
  2026-08-09, sorts commentary the *reader* needs from commentary only a future *editor* needs.
  Applying only the first is what let 146 AI-Notes accumulate, many of them production logistics
  addressed to nobody who will ever read the PDF.

  **Test 1 — "would this text exist if the notes had been written from scratch, by a human, with
  no source PDFs at all?"** If yes, it is mathematics: use `remark` (or `example` / `aiexample` /
  `aiexercise` as the content dictates). If no, it is commentary; go to Test 2. This is not a
  nicety: 20 blocks in Weeks 1–7 were originally filed as AI-Notes when they were plain
  mathematics, which buried real content under an editorial label.

  **Test 2 — "does a reader of the PDF need this, or only someone editing the source?"**

  | Needs it | Belongs in |
  |---|---|
  | A reader, who would otherwise be misled or left wondering | `ainote` |
  | Only an editor, mining a source or auditing provenance | a `%` comment |

  Reader-facing, and therefore a genuine `ainote`: a **flagged error in a source** and what was
  done about it; a **notation divergence** the reader will meet in the lecture or the script; a
  **divergence from the official solution**; **why an expected proof is absent** ("the course
  states this without proof").

  Editor-facing, and therefore a `%` comment: how a section was assembled, which tutors were
  sampled, whether anyone left a worked solution, that a solution was cross-checked against
  `SolN_Analysis2_eng.pdf`. None of that changes how the mathematics is read.

  * **BAD** — production logistics typeset into the document:
    ```latex
    \begin{ainote}
    None of the tutors sampled for the first problem sheet left a full worked solution to
    transcribe; the solutions below are written for this document and cross-checked against
    the official \texttt{exercises/Sol1\_Analysis2\_eng.pdf}.
    \end{ainote}
    ```
  * **GOOD** — same information, addressed to the person who actually wants it:
    ```latex
    % No tutor sampled for sheet 1 left a worked solution; the solutions below are written for
    % this document and cross-checked against exercises/Sol1_Analysis2_eng.pdf.
    ```

  The earlier revision of this file said the opposite, listing *"no priority page this week"* and
  *"only the important exercises are reproduced below"* as model `ainote`s. They are `%` comments.
  The one member of that old list that survives is **"the course does not prove this here"**,
  which is reader-facing: it tells the reader why they are about to see a proof the lecture
  skipped.

  * **`ainote` (fails the test — exists only because there is a source):**
    ```latex
    \begin{ainote}
    Corsin writes $\partial^{(2,1)} = \partial_2\partial_1$; a multi-index counts how many
    times each $\partial_i$ is applied, so this must be $\partial_1^2\partial_2$. His own
    expansion below confirms the intent. Corrected here.
    \end{ainote}
    ```
  * **`remark` (passes the test — this is just mathematics):**
    ```latex
    \begin{remark}[Lebesgue's covering lemma]
    The proof above shows more than was stated: on a compact metric space \emph{every} open
    cover has a Lebesgue number. This is known as \newterm{Lebesgue's covering lemma}.
    \end{remark}
    ```

  A reliable smell that an `ainote` is really a `remark` is that it contains a `\newterm{...}`:
  you are formally introducing terminology, and that is content. A note that states a theorem,
  gives a counterexample, or explains a concept is a `remark`, however it came to be written.

  ⚠️ **"I want to `\cref` it" is no longer one of those smells.** It used to be, because
  AI-Notes were unnumbered. Since 2026-08-09 they carry their own per-chapter counter and
  `\cref` prints `AI-Note 15.1` (see `build-and-preamble.md`). **Referenceability decides
  nothing about which environment to use** — apply Test 1 and Test 2 exactly as before, and do
  not move content into an `ainote` merely because you now can point at it.

  Conversely, do not over-correct in the other direction either. An `ainote` that flags a real
  error, or warns that a tutor's $\|\cdot\|_*$ means the operator norm, earns its box: deleting
  it loses information the reader needs. Test 2 removes *logistics*, not *warnings*.
* ⚠️ **"The course does not prove this" belongs in an `ainote`, and only after you have looked.**
  Added 2026-08-09 on the user's instruction. Two separate rules, and the second is the one that
  bites:

  **(1) Not body prose.** A sentence in the running text announcing what the lecture skipped
  reads oddly, because it is about the course rather than about the mathematics, and the reader
  meets it in the middle of an argument. Put it in an `ainote` next to the result. That is the
  one category of "why is there no proof here" the two tests keep as reader-facing.

  **(2) Do not assert it from your own document.** Grepping `content/` proves only that
  *this document* has no proof. It proves nothing about Corsin's PDFs or
  `Analysis_II_Script_v1.pdf`, and the script in particular does prove a great many results we
  merely state. Either open the source and check, or write only the claim you actually verified.

  * **BAD** (unverified, and it reads as fact): `Neither the course nor this document proves the
    inverse function theorem.`
  * **GOOD** (verified, and says exactly as much as was checked): `\Cref{thm:inverse_function_theorem}
    is stated above without proof`, plus a `% ⚠️ TO CHECK AGAINST THE SOURCES` comment naming the
    files someone should open, and a line in `project-state.md` so the check is tracked rather
    than forgotten.

* ⚠️ **The `ai*` prefix means "invented here", NOT "typeset by an AI".** Everything in this
  document is typeset by an AI, so that reading would make the prefix meaningless. What
  `aiexample` / `aiexercise` mark is **provenance**: the item does not exist in any source.
  This is the same authored-here-versus-transcribed line as `remark` versus `ainote`.

  The mistake to avoid is reaching for `aiexercise` whenever *you* are the one adding the block.
  An exercise lifted from a tutor's notes is a plain `exercise` with a `% Source:` /
  `% Supplement:` comment, however much reformatting it took — the exercise is theirs.

  * **BAD** — Sascha Brack's classification table, transcribed from his notes:
    ```latex
    \begin{aiexercise}[Classify these sets]   % wrong: it is his exercise, not ours
    ```
  * **GOOD:**
    ```latex
    % Supplement: Sascha Brack/Class Notes/Week_02_Notes_Friday_Updated.pdf, p. 8
    \begin{exercise}[Classify these sets]
    ```

  **A transcribed exercise with an authored solution is the normal case**, and it is not a
  contradiction: the `exercise` is transcribed, and the `exercisesolution` carries
  `% Generator: <model> (<effort>)` because the tutor left the answer blank. Label slugs should
  match — use `ex:classification_table`, not `ex:ai_classification_table`, when the exercise is
  not ours.
* **`aiexample`** (AI-Example) — for AI-generated illustrative mathematical examples that clarify a definition, theorem, or technique.
  - **Generator Comment:** Must contain a LaTeX comment naming the model that wrote it, `% Generator: <model> (<effort>)` -- e.g. `% Generator: Gemini 3.6 Flash (Medium)` or `% Generator: Claude Opus 5 (Medium)` -- directly inside the environment.
  - Rendered in GoldOrange style (`EnvAINote`).
* **`aiexercise`** (AI-Exercise) — for AI-generated practice problems created to reinforce the surrounding material.
  - **Difficulty:** Maximum **medium difficulty** (pedagogical, clarifying core concepts).
  - **Generator Comment:** Must contain a LaTeX comment naming the model that wrote it, `% Generator: <model> (<effort>)` -- e.g. `% Generator: Gemini 3.6 Flash (Medium)` or `% Generator: Claude Opus 5 (Medium)` -- directly inside the environment.
  - **Mandatory Solution:** Every `aiexercise` MUST have a corresponding complete worked solution in the chapter's `99-solutions.tex`.

## Mathematical notation — Analysis II specifics

All generic rules in this file apply. Additional project-specific conventions:

- **Metric spaces.** `(X,d)`; open ball `B_r(x)`; closure `\overline{A}`;
  interior `\operatorname{int}(A)`; boundary `\partial A`. Preserve Corsin’s
  emphasis (Week 2, p. 6) that `y \in X` in `B_r(x) := \{y \in X : d(y,x) < r\}`
  is the “important subtlety”.
- **Norms.** `\|\cdot\|` (`\lVert...\rVert`), never `||...||`. Corsin’s metrics
  `d_1` (Manhattan), `d_2` (standard Euclidean), `d_3` (supremum) — keep his
  indices exactly.
- **Derivatives.** `Df(x_0)` = total differential (linear map);
  `\Jac f(x_0)` = Jacobian matrix; `\nabla f(x_0)` = gradient;
  `\partial_i f` or `\frac{\partial f}{\partial x_i}` = partials;
  `D_v f` = directional derivative; `\Hess f` = Hessian.
- **Function spaces.** `C^k(U, \mathbb{R}^m)`, `C^\infty`, `C^0([0,1], \mathbb{R})`.
- **Sets.** Use `\subseteq` for inclusion and `\subsetneq` when strictness matters.
- **Operators.** Use the declared macros, never raw `\mathrm{}`:
  `\dist`, `\diam`, `\supp`, `\vol`, `\divg`, `\curl`, `\Jac`, `\Hess`,
  `\grad`, `\rank`, `\id`, `\Img`, `\sgn`, `\Tr`, `\GL`, `\transp`.

