# LaTeX review — weeks 1–7

Read-through of `content/week-01.tex` … `week-07.tex` and `main.tex`. Build is clean
(no undefined refs, no errors in `main.log`), so everything below is about *content*:
maths, figures, and flow. Ordered by how much it would hurt a student reading this cold.

---

## A. Mathematical errors that need fixing

### A1. `degenerate` is defined wrongly, and it breaks the Hessian test — `week-05.tex:292`

> *degenerate if there exists $v \neq 0$ such that $v^\top A v = 0$*

Under this definition **every indefinite matrix is degenerate** (if $v^\top Av>0$ and
$u^\top Au<0$, continuity along the segment gives a $w \neq 0$ with $w^\top Aw = 0$). So
`thm:hessian_test`'s third bullet, *"indefinite **and not degenerate** ⟹ saddle"*
(`week-05.tex:303`), is vacuous as written — it applies to no matrix at all.

The intended meaning is clearly $\det A = 0$ / $\ker A \neq \{0\}$, which is what
`ex:6.2` states in Week 6 (`week-06.tex:474`: *"If $\det M = 0$, then $M$ is degenerate"*).

Fix: define degenerate as $\exists v \neq 0$ with $Av = 0$ (equivalently $\det A = 0$,
equivalently $0$ is an eigenvalue), and drop "and not degenerate" from the saddle bullet —
indefinite alone already implies a saddle.

### A2. The "equivalent" characterization of differentiability is false — `week-04.tex:26`

$$\lim_{h\to 0}\frac{F(x_0+h)-F(x_0)}{|h|} = DF_{x_0}\!\left(\frac{h}{|h|}\right)$$

This limit does not exist in general (the right-hand side still depends on $h$), and it is
presented as *equivalent* to differentiability inside a $\Updownarrow$ chain. Directional
derivatives existing in every direction is **not** equivalent to differentiability — and the
file itself demonstrates this 60 lines later in `ex:partial_derivatives_not_continuous`
(`week-04.tex:89`), where $xy/(x^2+y^2)$ has all directional derivatives at $0$ and isn't even
continuous.

Fix: for a fixed direction $v$, write
$\lim_{s\to 0}\frac{F(x_0+sv)-F(x_0)}{s} = DF_{x_0}(v)$, and demote it from
"$\Updownarrow$" to "$\Downarrow$" — differentiability *implies* this, not conversely.
(The `importantremark` at `week-04.tex:228` already says exactly this; the display at line 26
contradicts it.)

### A3. `full rank = injective` in the regular value theorem — `week-07.tex:74`

> $\Jac F(x,y) = (2x,\ 2y)$ *has full rank (is injective as a linear map, i.e., nonzero)*

$DF_x : \mathbb{R}^2 \to \mathbb{R}$ is **surjective**, never injective — and surjectivity is
exactly what `thm:regular_value_theorem` requires eight lines above. Compare
`week-07.tex:130`, where "full rank (is injective)" *is* correct, because there the matrix is
tall ($n \times m$).

This is worth more than a fix: it's a genuinely useful tutor remark. Suggested insert after
the theorem —

> For an implicit description $F : \mathbb{R}^n \to \mathbb{R}^\ell$ the Jacobian is **wide**
> ($\ell \leq n$), so full rank means *surjective*. For a parametrization
> $f : \mathbb{R}^m \to \mathbb{R}^n$ it is **tall**, so full rank means *injective*. Same
> words, opposite condition — which one applies is decided by the shape of the matrix.

### A4. $\nabla g$ computed for the wrong $g$ — `week-05.tex:117`

The text has just set $g(x) = |x|^2-1$ (line 114), then the remark says
$\nabla g(x) = \frac{x}{|x|}$. That's $\nabla(|x|)$; for $|x|^2-1$ it is $2x$. The existing
`ainote` at `week-05.tex:227` flags the $|x|$ vs $|x|^2$ mismatch only for the exercise's
Lagrangian, not for this remark.

### A5. Broken counterexample in Week 1 — `week-01.tex:204`

> $x_k := \tfrac{3}{2} + \left(-\tfrac{1}{2}\right)^k$ *… oscillates … without settling …
> (it has two distinct subsequential limits, $\tfrac32 \pm 0$, which in fact coincide here in
> the limit, but the same construction with e.g. …)*

The sequence given **converges** to $3/2$. The parenthetical visibly notices this mid-sentence
and then patches it with a second sequence. Just lead with the one that works:
$x_k := \tfrac32 + \tfrac12(-1)^k$, accumulation points $1$ and $2$.

### A6. Wedge angle doesn't match the formula — `week-01.tex:314`

> *Remove a $30^\circ$ wedge from a disk:*
> $\{x^2+y^2\leq1\}\setminus\{|\arctan(y/x)|\leq\pi/6,\ x>0\}$

$|\arctan(y/x)|\leq\pi/6$ is $-30^\circ$ to $+30^\circ$, i.e. a **$60^\circ$** wedge. Either
say $60^\circ$ or use $\pi/12$.

### A7. Small computational slips (answers unaffected, but a student checking along will stall)

| Where | Says | Should be |
|---|---|---|
| `week-07.tex:455` | $\partial_y F_1 = 4xy^4+u^5$ | $5xy^4+u^5$ |
| `week-06.tex:632` | $\partial_y L = 2y(2-2\lambda)$ | $2y(1-\lambda)$ |
| `week-03.tex:151` | "$\delta := \varepsilon/L$ works uniformly in $x$, independently of $\varepsilon$" | independently of **$x$** |
| `week-06.tex:400–401` | domains of $x(y)$ and $y(x)$ | swapped — $x(y)$ goes $(-s,s)\to(-r,r)$ |
| `week-07.tex:482` | "$\varphi=\pm\pi$ (the *prime meridian*)" | the prime meridian is $\varphi=0$; this is the anti-meridian |
| `week-01.tex:296` | $z=\sqrt{1+x^2+y^2}$ "flattens out to slope $\approx1$" | it *steepens* to slope $1$ — it's asymptotic to the cone $z=r$ from above |

### A8. `m`-th root "metric" is not a metric — `week-02.tex:155`

> *In general, $d(x,y) := \sqrt[m]{\sum_k (x_k-y_k)^m}$ is a metric on $\mathbb{R}^n$ for any $m$.*

False as stated: needs $|x_k-y_k|^m$ (odd $m$ can give a negative radicand) **and** $m \geq 1$
(the triangle inequality fails for $m<1$ — which `week-04.tex:645` proves!). House rules say
flag rather than silently correct, so this wants an `ainote` pointing forward to
`ex:4.3` part 6.

### A9. Chained `⟺` that isn't — `week-03.tex:69`

The last step of the $\tilde d$ triangle inequality is
$$d_1 \leq d_2+d_3+2d_2d_3+d_1d_2d_3 \quad\Longleftrightarrow\quad 0 \leq 2d_2d_3+d_1d_2d_3$$
That's not an equivalence — you're *using* $d_1 \leq d_2+d_3$, not cancelling it. The
implication needed runs $\Longleftarrow$, which is fine for the proof; just say so
("$\Longleftarrow$, since $d_1 - d_2 - d_3 \leq 0$ by the triangle inequality for $d$").

---

## B. Figures that don't show what they claim — ✅ ALL FIXED

*(All items below are done and visually verified against the rendered PDF. Two further
defects of the same kind were found during that check and also fixed: the $\varepsilon$-net
figure at `week-02.tex:790` had four balls of radius $0.85$ that left the corners of $X$
uncovered — the whole point of total boundedness — now radius $1.45$ with a caption naming
the union; and the "Metric spaces" label in the nested-structures figure was
`yellow!70!black` on a `yellow!35` fill, effectively illegible, now `olive!60!black`.)*


These are the ones where a student who *trusts* the picture is worse off than one who ignores it.

### B1. The three-metrics triangle is mislabelled — `week-02.tex:146–147`

The horizontal leg is labelled $d_3 = |x_1-y_1|$ and the vertical leg $d_1 = |x_2-y_2|$.
But $d_1$ (Manhattan) is the **sum of both legs** and $d_3$ (supremum) is the **max** of them.
As drawn, the figure teaches the wrong definitions of two of the three metrics it exists to
compare.

Fix: label the legs neutrally ($|x_1-y_1|$, $|x_2-y_2|$), then annotate
$d_1 = $ *both legs together* (trace the L-path in one colour) and
$d_3 = $ *the longer leg*, with $d_2$ the hypotenuse.

### B2. The open cover doesn't cover — `week-02.tex:646–659`

Caption: $X = U_1\cup U_2\cup U_3$. From the coordinates, $U_1,U_2,U_3$ all live within
roughly $[-1.8,1.8]\times[-1.2,1.5]$, while $X$ extends to $(2.2,-0.5)$ and $(1.0,-1.5)$ — the
whole lower-right lobe of $X$ is in none of them. Compactness is *the* topic where "the union
really is everything" is the entire point.

(The companion figure at `week-02.tex:683` for $K \subseteq U_1\cup U_2\cup U_3$ looks
plausible, but is worth an eyeball at the same time.)

### B3. The convexity chord doesn't touch the curve — `week-06.tex:32–35`

Curve is $0.18(r-2.6)^2+0.4$. At $r=0.6$ and $r=4.6$ it equals $1.12$ **both times**, but the
chord is drawn from $(0.6,1.34)$ to $(4.6,0.85)$ — floating above the curve at the left end,
below the correct height at the right, and sloping when it should be horizontal. The dot
labelled "chord" sits at $(2.6,1.06)$ while the curve's vertex is at $(2.6,0.4)$.

This figure is the first thing a student sees after `def:convex_set_function`, so it should be
the cleanest one in the chapter. Suggested: endpoints on the curve at asymmetric $x$ (e.g.
$r=0.8 \to 0.983$ and $r=4.6 \to 1.12$), mark $(1-t)x+ty$ on the axis with a vertical dashed
line up to *both* the curve and the chord, and label the gap "$\leq$".

### B4. The two "tangent" lines are tangent to nothing — `week-06.tex:152–163`

Curve $g(r)=0.20(r-2.6)^2+1.0$. At $s=1.2$: $g=1.392$, $g'=-0.56$; the drawn line passes
through $(1.2,1.86)$ with slope $-0.4$. At $t=3.6$: $g=1.2$, $g'=0.4$; the drawn line passes
through $(3.6,1.39)$ with slope $0.72$. Both lines float above the curve and both slopes are
wrong.

The figure exists to make "$f'_{x,y}$ is increasing" and "the graph lies above its tangent"
visible simultaneously — right now it shows neither. Correct anchor points and slopes are
listed above; they're a two-line edit.

### B5. The marked points aren't on the sine curve — `week-03.tex:448–451`

The plot is $\sin(1/(0.1x)) = \sin(10/x)$, so peaks ($=1$) sit at
$x = 20/(\pi(1+4k))$: $1.273,\ 0.707,\ 0.490,\ 0.374,\dots$
The dots labelled $\gamma(a_n)$ are placed at $x = 2.54,\ 0.51,\ 0.28,\ 0.19$. Only one is
close. At $x=2.54$ the curve is actually at $\sin(3.94) \approx -0.71$, so the leading dot —
the one carrying the label "$\gamma(a_n) \to (0,1) \neq \gamma(0)$" — sits in empty space
roughly where the curve is at its *minimum*.

Also `week-03.tex:406`: the tick at $x=2.8$ is labelled $0.2$; with $t = x/10$ it is $0.28$.

### B6. The "rotation" changes the angle it's meant to preserve — `week-03.tex:510–531`

Left panel: $x=(1.5,0.6)$, $y=(0.8,1.8)$ → $\theta = 44.2^\circ$, $|x| = 1.62$.
Right panel (after the arrow labelled *change of basis (rotation)*): $x=(1.8,0)$,
$y=(1.2,1.6)$ → $\theta = 53.1^\circ$, $|x| = 1.8$.

A rotation preserves both lengths and angles; here neither survives. Since the whole argument
is "$\langle x,y\rangle$ is rotation-invariant, so compute in a convenient basis", the picture
undercuts the claim. Right panel should be $x=(1.62,0)$, $y \approx (1.41,1.37)$.

(Credit where due: the projection figure at `week-03.tex:556` is *exactly* right —
$\pi_v(u) = (1.6,0.4)$ computes correctly from the drawn $u,v$, and both arc angles match.
Same for the Lipschitz nested circles at `:160`, with $\sqrt{x}$ correctly placed between the
two rings.)

### B7. Orphan figure — `week-03.tex:189–207`

An unlabelled, uncaptioned, unreferenced plot of a wiggly curve with marks at $a,c,d,b$ and
$f(c), f(d)$, sitting between the Lipschitz classification exercise and the connectedness
section. It is plainly an **extreme value theorem** picture (max at $c$, min at $d$ on $[a,b]$)
and belongs 90 lines earlier, next to `item:extreme_value_theorem` in
*"Why do we care about compactness?"*. Where it currently sits it reads as a stray.

---

## C. Gaps where a first-time reader will stall

*(C1–C4 are done. C5–C7 remain: the two Week 2 proofs that assert their crux, both
topologist's-sine-curve proofs, and the uniqueness-of-the-differential parenthetical.)*

Content added alongside those fixes, as illustrative corner cases:
`aiexample` on why each metric axiom is needed (one failure each), a remark on the two
degenerate open balls ($r\leq0$ gives $\emptyset$, not $\{x\}$; discrete balls jump), an
`aiexercise` that open balls are open (with solution), an `aiexample` where *all* directional
derivatives exist yet $f$ is discontinuous, a two-panel figure for partial vs directional
derivatives, an `aiexample` where the Lagrange constraint qualification fails outright (the
cusp $y^2=x^3$), and an `aiexample` proving the coordinate cross is *not* a submanifold by
component-counting.

Not asking for full rigour — these are the spots where one or two added sentences change
the note from "record of what was said" to "usable".

### C1. **Uniform continuity is never defined.** (highest-value gap)

- `week-02.tex:848` — *"Then $f$ is uniformly continuous (`\cref{def:continuous}`)"* — that
  reference points at ordinary continuity.
- `week-03.tex:106` — introduces it with `\newterm{uniformly continuous}` (the macro reserved
  for first formal introduction) but still gives no definition, *after* Week 2 already proved
  a theorem about it.
- `week-03.tex:150` then `\cref`s `item:uniform_continuity_compact` as if it were the
  definition.

One `definition` environment in Week 2, right after `def:continuous`, fixes all three. The
contrast is the pedagogically loaded bit and worth spelling out: in `def:continuous` **(a)**,
$\delta$ may depend on $x_0$; uniform continuity demands one $\delta$ for all $x_0$ at once.

### C2. `prop:extremum_implies_critical` has no proof and the "Intuition" doesn't supply one — `week-05.tex:32–41`

The remark states $\langle\nabla f(x_0),v\rangle = 0 \iff \nabla f \perp v$, and then that
this for all $v$ forces $\nabla f = 0$ — but never says *why* the inner product vanishes at an
extremum. Two lines close it:

> Fix $v$. Then $t \mapsto f(x_0+tv)$ has an interior local extremum at $t=0$, so its
> one-variable derivative $\langle\nabla f(x_0), v\rangle$ vanishes there. As $v$ was
> arbitrary, $\nabla f(x_0)=0$.

(Also: `\mathbb{R}^2` on line 40 should be `\mathbb{R}^n`.)

### C3. The key sentence of the Lagrange section is backwards — `week-05.tex:112`

> *So $T|_{S^2}$ has a local extremum if it is **perpendicular to the surface** $S^2$.*

"it" has no referent ($\nabla T$ is meant), and the direction is wrong: perpendicularity is
**necessary**, not sufficient — which is precisely why step 5 of every Lagrange computation
(compare candidate values) exists. Suggested: *"So if $T|_{S^2}$ has a local extremum at $p$,
then $\nabla T(p)$ must be perpendicular to $S^2$ — any tangential component would let us
increase $T$ by moving along the surface. The converse fails, so perpendicularity produces
candidates, not answers."*

That last clause is already made well in the Week 6 `ainote` at `week-06.tex:648`; making the
point here first would pay off twice.

### C4. The Lagrange worked example never classifies its answers — `week-05.tex:186–225`

`ex:xyz_on_ball` asks for the *local extrema* of $xyz$ on the unit ball. The solution produces
8 boundary candidates plus the coordinate axes and stops. Nothing says which of the 8 are
maxima, which are minima, or that the axis points (where $f=0$) are not extrema at all. One
closing paragraph:

> On $S^2$, $f = \tfrac{1}{3\sqrt3}\alpha\beta\gamma$ at $\tfrac{1}{\sqrt3}(\alpha,\beta,\gamma)$,
> so the four points with $\alpha\beta\gamma=+1$ are maxima ($f = 1/(3\sqrt3)$) and the four
> with $\alpha\beta\gamma=-1$ are minima. On the coordinate axes $f \equiv 0$ and $f$ takes
> both signs arbitrarily nearby, so none of those points is an extremum.

### C5. Two Week 2 proofs assert their crux — `week-02.tex:463–471` and `week-02.tex:807`

- *$C^0([0,1])$ is closed*: the whole content is "if $\sup|f-g| < \varepsilon/3$ and $f$ jumps
  by $\varepsilon$ at $x_0$, then $g$ jumps by at least $\varepsilon/3$" — and that step is
  stated as a bare conclusion. It's one line of triangle inequality and it's the only line
  that matters.
- *$r$ is 1-Lipschitz*: with $r(x) := \tfrac12\sup\{\dots\}$, the argument shows
  $R(y) \geq r(x)-d(x,y)$ for the un-halved $R$, then concludes $r(y) \geq r(x)-d(x,y)$. The
  factor $\tfrac12$ is silently dropped. (The result is true — $r$ is even
  $\tfrac12$-Lipschitz — but as written the two symbols are conflated.)

### C6. The topologist's sine curve, both proofs — `week-03.tex:414–434`

- *Connected* (`:414`): as written this is close to unparseable — "$U\setminus\{0\}$ is also
  open" is a true but irrelevant statement, and the contradiction structure never appears.
  The clean two-liner: let $S = V_1 \sqcup V_2$ be a separation, say $(0,0) \in V_1$. The
  graph $G := S\setminus\{(0,0)\}$ is path-connected hence connected, so it lies entirely in
  one piece; it can't be $V_1$ (else $V_2 = \emptyset$), so $G \subseteq V_2$ and
  $V_1 = \{(0,0)\}$ — but every ball around the origin meets $G$, so $V_1$ isn't open.
- *Not path-connected* (`:432`): "Thus in the limit $n\to\infty$, $a_n \to 0$" is asserted.
  The IVT gives *some* $a_n$ with $x(a_n) = \frac{1}{2\pi n + \pi/2}$, not a sequence tending
  to $0$. Standard patch: let $a := \sup\{t : x(t)=0\}$, work on $[a,1]$ where $x>0$ beyond
  $a$, and pick $a_n$ as the *smallest* such parameter; then $a_n \downarrow a$ and
  $x(a_n) \to 0$ forces the contradiction.
- Also `week-03.tex:396`: $S := \{\dots\} \cup \{0\}$ — write $\{(0,0)\}$, as the figure
  caption already does.

### C7. Uniqueness of the differential — `week-04.tex:42`

*"a nonzero linear map cannot decay along its own domain"* is doing a lot of work in one
parenthesis. Replace with: *pick $h$ with $L(h) \neq 0$; then
$L(th)/|th| = L(h)/|h|$ is a nonzero constant for all $t>0$, so it cannot tend to $0$.*

---

## D. Flow and placement

1. **`week-02.tex:126` — `aiexample` on open balls in the discrete metric appears ~110 lines
   before `def:open_ball`.** It uses $B_r(x)$, "open", and "clopen", none of which have been
   defined at that point in the document. Move it to just after `def:open_ball` (`:239`) —
   where it would also set up `ex:X_empty_clopen` nicely.

2. **`week-05.tex:121` — `aiexample` on saddle points via the Hessian sits inside the Lagrange
   multiplier section**, 150 lines before `\section{The Hessian test}` and before `\Hess`,
   "indefinite", or eigenvalue criteria have appeared in this chapter. It splits the
   level-set/gradient discussion in half. Move to just after `thm:hessian_test` (`:306`),
   next to the sibling `aiexample` at `:318`.

3. **`week-02.tex:890–908` — two `aiexercise`s are wedged between an `exercisesolution` and the
   `ainote` that comments on it**, so that the `ainote`'s "*Corsin writes $n_k > k$ **above***"
   now points past two unrelated exercises. Move the `ainote` up to directly follow the
   solution at `:888`.

4. **`week-06.tex:2` — chapter title is "Week 6 — Convexity"** but two of the three sections are
   the inverse and implicit function theorems (roughly 250 of 430 content lines). The
   transition paragraph on line 5 already names all three. Suggest
   *"Week 6 — Convexity, Inverse \& Implicit Function Theorems"*, matching how weeks 3–5 title
   themselves.

5. **`week-06.tex:645–668` — exercise 6.9 is split across two `exercisesolution` environments**
   with an `ainote` in between, so part **(b)** opens a fresh "Solution" box with
   `[start=2]`. Either put the `ainote` after both parts, or nest it inside the single
   solution as is done in `week-06.tex:580`.

6. **`week-06.tex` has no `\session{}` markers**, unlike weeks 2–4. Week 5 explains its absence
   in an `ainote` (`week-05.tex:10`); Week 6 and 7 don't. One line each, or drop the
   convention from Week 5 too.

7. **Transitions.** These are genuinely good — `week-02.tex:227`, `:591`, `:618`,
   `week-03.tex:210`, `:458`, `week-04.tex:171`, `:287`, `week-06.tex:174`, `:270`,
   `week-07.tex:181` all do real work (the compactness-vs-completeness one at
   `week-02.tex:618` is the best of them, because it makes a claim rather than announcing a
   topic). Two chapters are missing one at the seam that most needs it:
   - `week-05.tex:270` — the jump from Lagrange multipliers to the Hessian test is unmarked,
     and the reader has just been doing *constrained* optimization while the Hessian test is
     about *unconstrained* critical points. One sentence would prevent the natural
     misreading that the Hessian test classifies Lagrange candidates.
   - `week-07.tex:296` — `\subsection{Normal space}` starts cold with "Suppose $F$…". A
     half-sentence ("the tangent space records the directions *along* $M$; the complementary
     directions turn out to be exactly the gradients of any implicit description") would land
     it.

---

## E. Small stuff

- **`week-05.tex:441`** — `\right\|_{t=0}` should be `\right|_{t=0}`; it currently typesets a
  double bar in Corsin's quoted hint.
- **`week-01.tex:24, 26, 121, 195, 298`** — raw ASCII `"..."` in prose typesets as `”…”`.
  Use `\qt{...}` or ` ``...'' `. (Weeks 2–7 are clean on this.)
- **`week-01.tex`** — labels `ex:1.1`…`ex:1.4` use the numbering scheme that `gemini.md`
  asks to replace with descriptive slugs; weeks 4–7 do the same for official-sheet exercises,
  so it's consistent-but-against-style. Low priority, but worth a decision rather than drift.
- **`week-04.tex:162`** — the row-of-gradients matrix should carry transposes
  ($\nabla F_1^\top$ etc.), since a gradient is a column vector. The `ainote` immediately
  below is *about* the row/column distinction, so it's a conspicuous place to be loose.
- **`week-04.tex:284`** — `\frac{d}{dt}f(x_1,\dots,x_n) := Df(x_1(t),\dots,x_n(t))` equates a
  scalar with a row vector; the `\cdot \gamma'(t)` is missing.
- **`week-04.tex:26, 28`, and throughout Week 4** — `|h|` for the Euclidean norm where
  `gemini.md` asks for `\|\cdot\|`.
- **`week-06.tex:531` / `:528`** — exercise 6.11 is titled *"Closest point on a hyperboloid"*,
  but $z = x^2-y^2$ is a hyperbolic **paraboloid** (a saddle). Retitle.
- **`week-06.tex:596–599`** — the $\mathbb{R}^2$ problem is argued with
  $x = (0,-r,0,\dots,0) \in \mathbb{R}^n$.
- **`week-06.tex:740`** — *"$\Hess f(x,y) = \operatorname{diag}(-4ax^2,-4ay^2)$ off-diagonal
  $-4axy$"* isn't a sentence; write the $2\times2$ matrix out. (The determinant claim is
  correct.)
- **`week-07.tex:324` vs `:317`** — `def:normal_space` fixes $M = F^{-1}\{0\}$, then the
  example uses $S^2 = F^{-1}\{1\}$. Use $F = x^2+y^2+z^2-1$ for consistency.
- **`week-07.tex:167`** — $f$ is reused for both $f(x,y)$ and $f(\theta)$ in the same display
  chain; rename the parametrized one ($\tilde f$ or $h$).
- **`week-02.tex:545`** — the $\varepsilon$–$\delta$ condition writes $d$ for both $d_X$ and
  $d_Y$; and `\implies` inside display math is what `gemini.md` asks to avoid.
- **`week-03.tex:277`** — `thm:continuity_preserves_connected` is stated without proof, and
  its proof is `ex:ai_connected_image` at `:651`. Worth a forward pointer at the theorem.

---

## F. Language and prose

*(F1, F4 and F6 are done. F2's two unquantified questions and the `[in $\mathbb{R}^2$]`
title are also fixed. F3 and F5 remain.)*

### F1. Sentences that don't parse — ✅ FIXED

- **`week-03.tex:55`** — *"Non-negativity, definiteness and symmetry follow from $d(x,y)$."*
  Properties don't follow from a function. → *"…are inherited directly from the corresponding
  properties of $d$, since $t \mapsto t/(1+t)$ is non-negative and vanishes only at $t=0$."*
- **`week-06.tex:574`** — a four-clause pile-up with a dangling participle:
  > *Being $(\max\{x_1,\tfrac12\})^4$ with $\max\{x_1,\tfrac12\} \geq \tfrac12 > 0$, and
  > $t \mapsto t^4$ convex and increasing on $(0,\infty)$ composed with the convex function
  > $x \mapsto \max\{x_1,\tfrac12\}$, $f$ is convex.*

  → *"$x \mapsto \max\{x_1,\tfrac12\}$ is convex, takes values in $[\tfrac12,\infty)$, and
  $t \mapsto t^4$ is convex and increasing there; a convex increasing function of a convex
  function is convex, so $f$ is convex."*
- **`week-06.tex:740`** — *"$\Hess f(x,y) = \operatorname{diag}(-4ax^2,-4ay^2)$ off-diagonal
  $-4axy$"* — no verb, no matrix. Write the $2\times2$ out.
- **`week-01.tex:298–301`** — *"…traces out four planar faces meeting at the apex $(0,0,0)$…
  reading the graph the other way…, it is the graph of the taxicab-adjacent function…"*
  A mid-sentence `...` used as punctuation, plus two clashing metaphors ("pyramid **roof**",
  then "upward-opening square **cone**") and the coinage *taxicab-adjacent*, which explains
  nothing. Pick one image and drop the ellipsis.
- **`week-04.tex:302`** — *"In practice, we never use this formula, but to shed some light on
  it:"* — trails into a colon with no main clause. → *"…but it is worth unpacking once."*
- **`week-04.tex:34`** — *"(Of course, equivalently for $U \subseteq \mathbb{R}^n$ a subset,
  $F : U \to \mathbb{R}^m$.)"* — verbless. → *"The same definition applies verbatim to
  $F : U \to \mathbb{R}^m$ for $U \subseteq \mathbb{R}^n$ open."*
- **`week-04.tex:184`** — *"And equivalently for the Jacobians."* — fragment opening with
  *And*. → *"The same identity holds for the corresponding Jacobi matrices."*
- **`week-05.tex:112`** — *"So $T|_{S^2}$ has a local extremum if **it** is perpendicular to
  the surface"* — the pronoun has no antecedent (see **C3**, which also fixes the logic).

### F2. Questions that aren't answerable as posed

- **`week-02.tex:571`** — *"Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces, where $d_Y$ is the
  discrete metric. Is $f : (X,d_X) \to (Y,d_Y)$ continuous?"* — $f$ is never quantified, so
  the question has no truth value; the answer ("No", with a counterexample) reveals the
  intent. → *"Is **every** such $f$ continuous?"* Same for `:582`.
- **`week-02.tex:361`** — `\begin{example}[in $\mathbb{R}^2$]` reads as "Example (in ℝ²)".
  The bracketed argument should be a noun phrase, as everywhere else in the document:
  `[Open, closed, and neither in $\mathbb{R}^2$]`.

### F3. Symbols used as prose glue

`gemini.md` asks for words in prose and no `\implies` inside displays. There are **47**
`\implies` across the seven files, and a good share are doing sentence work:

- `week-05.tex:26` — *"**Strict** min/max $\iff f(x) > f(x_0)$ / $f(x) < f(x_0)$"* — an `\iff`
  plus a slash carrying two definitions at once. Write it as two clauses.
- `week-05.tex:612` — *"$1 = 2\lambda x$ and $2 = 2\lambda y \implies y = 2x$"* inside a
  display.
- `week-05.tex:625`, `week-05.tex:632`, `week-06.tex:676`, `week-04.tex:195` — same pattern:
  an arrow standing in for "hence" mid-display.
- `week-05.tex:309` — *"positive $= \smile \dots$ min"* — `\dots` as glue. → *"positive
  definite: the graph curves upward ($\smile$) in every direction, so a minimum."*

Not all of these are worth touching — inside a genuine chain of algebra (`week-05.tex:213`,
transcribed from Corsin) the arrows read fine. The ones to fix are where an arrow separates
two *sentences* rather than two *equations*.

### F4. Missing commas after introductory adverbs (house rule)

`week-02.tex:761` ("So the process must terminate…"), `week-03.tex:427` ("Therefore we
find…"), `week-03.tex:432` ("Thus in the limit…"), `week-04.tex:666` ("Hence there is…"),
`week-04.tex:679` ("So connectedness of $U$ alone…"), `week-05.tex:398` ("So we have critical
points…"), `week-05.tex:625` ("Thus there are no critical points…"), `week-07.tex:175` ("So
the extrema are at…"). Eight instances, all one-character fixes.

### F5. Register — the one thing I'd deliberately *not* flatten

Two voices coexist here, and that's correct per the two-layer rule: Corsin's transcribed
material is telegraphic and exclamatory (*"Super important!"* `week-02.tex:36`, *"Important
for counterexamples!"* `:113`, *"Please never do this."* `week-04.tex:401`, *"the geometrical
meaning of this one eludes me, sorry"* `week-06.tex:303`), while the written-for-this-document
solutions are full academic prose. Keep that contrast — it's the most likeable thing about
the notes and it tells the reader instantly what came from the lecture hall.

What *does* jar is inconsistency **within** the generated material. The `aiexample` /
`aiexercise` blocks marked `% Generator: Gemini 3.6 Flash` run as single unbroken paragraphs
with arrows for connectives (`week-02.tex:930`, `week-03.tex:698`, `week-03.tex:705`,
`week-05.tex:610`, `week-05.tex:620`), while the `Claude Sonnet 5` ones are broken into
labelled cases with full sentences (`week-04.tex:650`, `week-05.tex:541`, `week-06.tex:627`).
Side by side in the same Solutions section the difference is visible. Worth one normalizing
pass over the Gemini-marked blocks: break the run-ons, replace mid-sentence `\implies` with
words. No mathematical content changes.

### F6. Terminology slip worth naming

**`week-04.tex:144`** — *"This is also called the **speed** of the curve."* $\gamma'(t)$ is
the **velocity**; the speed is $\|\gamma'(t)\|$, a scalar. Since the next display expands
$\gamma(\tfrac\pi4+h)$ using the vector, the correction matters. (If Corsin wrote "speed",
this is an `ainote` rather than a silent fix.)

---

## What's working well (so it doesn't get edited away)

- The **provenance discipline** is genuinely unusual and valuable — `% Source:`,
  `% Kept inline:`, `% Generator:` and the `ainote`-on-every-correction convention mean
  every claim is traceable. Keep it.
- The **`ainote` corrections** to Corsin's slips (rows-vs-columns `week-04.tex:164`, the
  multi-index $\partial^\alpha$ `week-04.tex:336`, the missing $\ell=0$ term
  `week-04.tex:360`, $\|x\|=R^2$ `week-03.tex:318`) are exactly right in tone: flag, explain,
  don't silently overwrite.
- The **Taylor $1/\ell!$ vs $1/\alpha!$ remark** (`week-04.tex:368`) resolves a confusion most
  textbooks skip. Slightly over-long — "they agree, but for two different reasons" undersells
  it; they agree *because* of the multinomial collapse — but the content is the best single
  paragraph in the document.
- **`ex:4.6` part 3** (`week-04.tex:671`) — the fibre-connectedness analysis is complete,
  correct, and goes past what the official hint gives.
- **`ex:6.12`** (`week-06.tex:708`) — all six sign orderings of $(a,b)$ check out against the
  Hessians. That's careful work.
- The **convexity proof** at `week-06.tex:116–124` (the $(\Leftarrow$) direction with
  $u,v$ and the two-sided estimate) is complete and airtight — no gaps at all.

---

## Suggested order of attack

1. **A1** (degenerate/Hessian test) — it makes a stated theorem vacuous.
2. **A2, A3** (differentiability characterization, full rank) — both teach the wrong idea.
3. **C1** (define uniform continuity) — one environment, unblocks three broken references.
4. **B1, B2, B3, B4, B5** — the five figures that contradict their own captions.
5. **D1, D2, D3** (three misplaced blocks) — pure cut-and-paste.
6. **F1, F4** — the eight missing commas and the six sentences that don't parse.
7. Everything else.

None of the above needs a source PDF to resolve: each one is an internal contradiction (a
figure against its own caption, a `\cref` against what it points at, a formula against the
line above it), so it is fixable from the `.tex` alone. Re-reading the tutor notes is only
worth it afterwards, and only for the places where we would want to *add* material —
realistically **C1** (a definition of uniform continuity, if we want Corsin's own phrasing
rather than a written-for-this-document one) and **A8** (whether Corsin really claimed the
$m$-th root formula for all $m$, which decides whether it gets an `ainote` or a silent
correction).
