# Week 2 — Metric Spaces, Topology & Continuity

**Primary source:** `Corsin Nick/Class Notes/Week 2.pdf` (15 pp)
**Exercise sheet:** `exercises/Ex2_Analysis2_eng.pdf` (solutions: `Sol2_Analysis2_eng.pdf`)
**Lecture notes:** ch. 9 (confirmed — Corsin pastes *Definition 9.63* from the script on p. 14)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **Note on the cover.** Page 1 is a title page reading *"Class notes Week 1"*. This is
> Corsin's own initial numbering; from `Week 3.pdf` onwards the covers read "Week 3", "Week 9",
> … matching the file names. We use **Week 2** throughout — it agrees with problem set 2 and
> with every other tutor. See `OQ-01`.

> **No priority page this week.** From Week 3 onwards Corsin opens each file with a colour-coded
> *Recommended exercises* page. Week 2 has none, so the problems below carry only the official
> `(*)` difficulty marker.

---

## Exercise sheet 2

*Statements quoted verbatim from `exercises/Ex2_Analysis2_eng.pdf` (assigned 23 February 2026,
due 2 March 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

> Some of these problems have a closed-answer format, similar to what you might find on the
> final exam. "Multiple Choice" means that zero, one or more answers can be correct.
> Questions marked with (\*) are a bit more complex, you might want to skip them at the first
> read. Hints available in the last page.

### 2.1 — Examples and Non-examples of Metric spaces

Which of the following pairs are metric spaces? Prove it or provide a counterexample.

1. $(B(X), d)$, where $B(X)$ denotes the set of all bounded functions from a non-empty set $X$ to $\mathbb{R}$ and
   $$d(f,g) := \sup_{x \in X} |f(x) - g(x)|.$$
2. $(\mathbb{Q}_+, d)$, where $\mathbb{Q}_+$ are the positive rational numbers and $d(x,y) := \left|\tfrac{1}{x} - \tfrac{1}{y}\right|$.
3. $(\mathbb{R}^2, d)$, where $d(x,y) := (x_1 - y_1)^2 + |x_2 - y_2|$.
4. $(\mathbb{R}^2, d)$, where $d(x,y) := |x_1 - y_1|^{1/2} + |x_2 - y_2|$.
5. $(\mathbb{R}^{n \times n}, d)$ with $d(X,Y) := \left(\operatorname{Tr}\{(X-Y)^{\mathsf T}(X-Y)\}\right)^{1/2}$.
6. **(\*)** $(\mathbb{R}^{n \times n}, d)$ with
   $$d(X,Y) := \sup\{|v^{\mathsf T}(X-Y)v| : v \in \mathbb{R}^n, \|v\| = 1\},$$
   and $\mathbb{R}^{n\times n}$ denoting the set of square matrices.
7. **(\*)** $(\mathbb{R}^2/\mathbb{Z}^2, d)$ where the flat 2-dimensional torus $\mathbb{R}^2/\mathbb{Z}^2$ is the set of equivalence classes of pairs of real numbers under the equivalence relation
   $$x, y \in \mathbb{R}^2, \quad x \sim y \iff x_1 - y_1 \in \mathbb{Z},\ x_2 - y_2 \in \mathbb{Z},$$
   and $d([x],[y]) := \inf_{k,h \in \mathbb{Z}} \|x - y + (k,h)\|$, with $\|\cdot\|$ denoting the Euclidean distance and $[x] \in \mathbb{R}^2/\mathbb{Z}^2$ denoting the equivalence class of $x \in \mathbb{R}^2$.

*Official hints:* **2.1.3** and **2.1.4** — ignore what happens in the second variable, it is
there only to distract you. **2.1.5** — rewrite, for a general matrix $A := X - Y$, what
$\operatorname{Tr}\{A^{\mathsf T}A\}^{1/2}$ actually means; it should look familiar.
**2.1.6** — see what happens if $(X-Y)$ is anti-symmetric. **2.1.7** — convince yourself first
that the "inf" is in fact a "min".

### 2.2 — Multiple choice (closure)

Let $(X,d)$ be a metric space, and $Y_1, Y_2 \subset X$ subsets. Select all the statements below
that are necessarily true.

(a) $\overline{Y_1 \cup Y_2} = \overline{Y_1} \cup \overline{Y_2}$
(b) $\overline{Y_1} \cap \overline{Y_2} \subset \overline{Y_1 \cap Y_2}$
(c) $\overline{Y_1 \cap Y_2} \subset \overline{Y_1} \cap \overline{Y_2}$
(d) $\overline{Y_1 \cap Y_2} = \overline{Y_1} \cap \overline{Y_2}$

*Official hints:* **2.2.b** — compare with 2.1.3. **2.2.d** — play with a set of three points (a triangle).

### 2.3 — Multiple choice (distance from a set)

Let $(X,d)$ be a metric space, and $A \subset X$ a non-empty subset. We define the function
"distance from $A$" as
$$d(\cdot, A) : X \to [0,\infty), \qquad d(x,A) := \inf_{a \in A} d(x,a).$$
Select all the statements below that are necessarily true.

(a) If $A$ is closed and $x \in A^c$, then $d(x,A) > 0$.
(b) The set $M := \{x \in X : d(x,A) \geq 1\}$ is closed in $X$.
(c) For $x, y \in X$, $d(x,A) \leq d(x,y) + d(y,A)$ holds.
(d) If $A^\circ$ is non-empty and $x \in X$, then $d(x,A) = d(x, A^\circ)$.

*Official hint:* first convince yourself with a drawing that the name of this function is
appropriate; then use the characterization of open/closed sets with sequences.

### 2.4 — Boundary, Interior etc.

Determine the interior, closure, and boundary of the following subsets $Y$ of $\mathbb{R}$, for
the standard topology on $\mathbb{R}$. No need to justify the answer.

| | | | |
|---|---|---|---|
| (1) | $Y = [0,1]$ | (2) | $Y = \mathbb{Q}$ |
| (3) | $Y = \emptyset$ | (4) | $Y = (0,1)$ |
| (5) | $Y = [-1,1) \setminus \{0\}$ | (6) | $Y = [0,\infty)$ |
| (7) | $Y = \{0\}$ | (8) | $Y = \left\{\tfrac{1}{n} \mid n \in \mathbb{N}\setminus\{0\}\right\}$ |

### 2.5 — Product of metric spaces

Let $(X, d_X)$ and $(Y, d_Y)$ be a pair of metric spaces. Recall that the set of ordered pairs
$(x,y)$ with $x \in X$ and $y \in Y$ is denoted by $X \times Y$. Consider the following functions
$X \times Y \to [0,\infty)$:
$$
\begin{aligned}
d_1((x,y),(x',y')) &:= \max\{d_X(x,x'), d_Y(y,y')\} \\
d_2((x,y),(x',y')) &:= d_X(x,x') + d_Y(y,y') \\
d_3((x,y),(x',y')) &:= \sqrt{d_X(x,x')^2 + d_Y(y,y')^2}.
\end{aligned}
$$

1. Show that they are all valid distance functions on $X \times Y$.
2. Show that they are all equivalent, i.e. there is a number $C > 0$ such that
   $$d_1((x,y),(x',y')) \leq C\,d_2((x,y),(x',y')) \leq C^2 d_3((x,y),(x',y')) \leq C^3 d_1((x,y),(x',y'))$$
   for all $x, x' \in X$, $y, y' \in Y$.
3. Show that a sequence $(x_n, y_n) \to (x,y)$ with respect to $(X \times Y, d_3)$ if and only if
   $x_n \to x$ with respect to $d_X$ and $y_n \to y$ with respect to $d_Y$.

*Official hint:* don't get distracted by the abstract set-up — you already know all these things
for $\mathbb{R} \times \mathbb{R}$; start from there, then rewrite those arguments in this
general framework.

### 2.6 — Continuity of the distance

Let $(X,d)$ be a metric space, and endow $X \times X$ with the product distance
$d_2(x,y) := d(x_1,y_1) + d(x_2,y_2)$. Show that the distance function
$d : X \times X \to \mathbb{R}$ is continuous with respect to $d_2$ and, more precisely, that it
is 1-Lipschitz. Is $d$ also continuous with respect to the distance
$d_1(x,y) := \max\{d(x_1,y_1), d(x_2,y_2)\}$? Is $d$ also Lipschitz continuous with respect to
the distance $d_3(x,y) := \sqrt{d(x_1,y_1)^2 + d(x_2,y_2)^2}$?
(Notation consistent with Problem 2.5.)

### 2.7 — Continuity of the composition

Let $X, Y, Z$ be metric spaces and let $f : X \to Y$, $g : Y \to Z$ be continuous functions.
Show that $g \circ f : X \to Z$ is continuous using at least two of the three equivalent
definitions of continuity seen in class.

> **Ties into the class notes:** the three equivalent definitions are exactly the ones Corsin
> states on p. 11 (ε–δ, sequential, topological).

---

## Monday

### 1. Structured spaces

*(Corsin p. 2)*

This semester you will be introduced to certain structures that can be given to a set — also
called a **space** ("Raum") in this context — which we will denote by $X$:

- **(0. Topological spaces** — fourth semester.**)**
- **1. Metric spaces** ("metrischer Raum") $\;(X,\ d : X \times X \to \mathbb{R}_{\geq 0})$
  - Define a **distance** between points.
  - $X$ is **not** necessarily a vector space.
  - Covered in *Analysis*.
- **2. Normed metric spaces** $\;(X,\ \|\cdot\| : X \to \mathbb{R}_{\geq 0})$
  - Define the **length** of a vector.
  - Presuppose a linear structure, i.e. $X$ is a **vector space**.
  - Covered in *Linalg / Analysis*.
- **3. Inner product spaces** $\;(X,\ \langle\cdot,\cdot\rangle : X \times X \to \mathbb{R})$
  - Define **both** lengths **and** angles!
  - Super important!
  - Covered in *Linalg*, sometimes used in *Analysis*. $X$ is a vector space.

> **[FIG-W02-01]** *(Corsin p. 3)* Four concentric rounded blobs (irregular circle-like shapes,
> not perfect circles), each nested fully inside the next, largest to smallest: outermost red
> blob labelled *Topological spaces* (label near the top, inside the red band); yellow blob
> inside it labelled *Metric spaces*; green blob inside that labelled *Normed vector spaces*;
> innermost blue blob labelled *Inner product spaces*. Each label sits inside its own coloured
> band, stacked top to bottom in the same nesting order. → TikZ concentric rounded shapes.

*(Corsin p. 3)*

The precise definitions will follow later. You will see that an **inner product**
$\langle\cdot,\cdot\rangle$ induces a **norm** by the formula
$$\|x\| := \sqrt{\langle x, x\rangle}, \qquad x \in X.$$
Furthermore, a **norm** induces a **metric** by
$$d(x,y) := \|x - y\|, \qquad x, y \in X.$$

### 2. Metric spaces

*(Corsin p. 3)*

**Definition.** A **metric space** ("metrischer Raum") $(X,d)$ is any set $X$ with a
**metric** ("Metrik") $d : X \times X \to \mathbb{R}_{\geq 0}$ such that for all $x, y \in X$:

1. $d(x,y) \geq 0$, with equality if and only if $x = y$ — *(definiteness)*
   In words: "the distance is non-negative, and a point has zero distance to itself."
   > ⚠️ **Check:** Corsin's gloss reads *"the distance positive"*; the formula $d \geq 0$ is
   > correct, the gloss drops the "non-". Corrected in prose. See `OQ-02`.
2. $d(x,y) = d(y,x)$ — *(symmetry)*
   "$x$ has the same distance to $y$ as $y$ to $x$."
3. $d(x,z) \leq d(x,y) + d(y,z)$ — *(Δ-inequality, the triangle inequality)*
   "detours make the way longer"

> **[FIG-W02-02]** *(Corsin p. 3)* On a pair of coordinate axes (origin at bottom-left): point
> $x$ sits near the origin (bottom-left), $y$ sits upper-middle, $z$ sits upper-right, so the
> three points form a flattened, lever-like triangle. A blue two-segment path traces
> $x \to y \to z$ (up, then across). A red straight edge connects $x$ directly to $z$, cutting
> beneath the blue path. Below the sketch, the annotation
> $d(x,z) \le d(x,y) + d(y,z)$ in red. → TikZ 2D sketch.

#### Examples

*(Corsin p. 4)*

1. Let $X$ be a set. The **discrete metric** is given by
   $$d(x,y) = \begin{cases} 1 & \text{if } x \neq y \\ 0 & \text{if } x = y \end{cases}$$
   **Important for counterexamples!**

2. Let $X = \mathbb{R}^n$. Then we have many choices for a metric; some common ones are:

   **(a) Manhattan metric:**
   $$d_1(x,y) = |x_1 - y_1| + \dots + |x_n - y_n| = \sum_{k=1}^{n} |x_k - y_k|$$

   **(b) Standard metric:**
   $$d_2(x,y) = \sqrt{(x_1-y_1)^2 + \dots + (x_n-y_n)^2} = \sqrt{\sum_{k=1}^{n}(x_k - y_k)^2}$$

   **(c) Supremum metric:**
   $$d_3(x,y) = \sup_{k = 1,\dots,n} |x_k - y_k|$$

> **[FIG-W02-03]** *(Corsin p. 5)* Axes $x_1$ (horizontal), $x_2$ (vertical). Point $x = (x_1,x_2)$
> lower-left, point $y = (y_1,y_2)$ upper-right, each with dotted guide lines down/across to the
> axes. A right triangle is formed: the blue hypotenuse runs diagonally from $x$ straight to $y$,
> labelled $d_2$; the red vertical leg runs up the right side, at horizontal position $y_1$, from
> height $x_2$ to $y$, labelled $d_1$; the orange horizontal leg runs along the bottom, at height
> $x_2$, from $x_1$ to $y_1$, labelled $d_3$. → TikZ 2D sketch.

*(Corsin p. 5)* In general,
$$d(x,y) = \sqrt[m]{\sum_{k=1}^{n} (x_k - y_k)^m}$$
is a metric on $\mathbb{R}^n$ for any $m$.

3. $X = C^0([0,1], \mathbb{R})$, the set of continuous functions $[0,1] \to \mathbb{R}$. Then we
   can define the **supremum metric** for $f, g \in X$:
   $$d(f,g) = \sup_{x \in [0,1]} |f(x) - g(x)|$$

4. $X = S^2 := \{(x_1,x_2,x_3) \in \mathbb{R}^3 : x_1^2 + x_2^2 + x_3^2 = 1\}$. $S^n$ is called the
   **$n$-dimensional sphere**, or **$n$-sphere**. The closest path between two points on the
   sphere is an **arc of a great circle** (a *geodesic*). This defines a metric, similar to how
   straight lines define a metric on $\mathbb{R}^n$.

> **[FIG-W02-04]** *(Corsin p. 5)* Two panels, each a wireframe sphere (outline circle with a
> dashed equator ellipse for 3D shading). Left panel: point $x$ red, near the front/bottom of the
> sphere; point $y$ red, near the top; a blue arc runs over the surface between them, labelled
> $d(x,y)$. Right panel: the same sphere outline with the same two points $x$ (lower) and $y$
> (upper); the blue surface arc is drawn again (labelled "distance on sphere"), and in addition
> an orange dashed straight chord cuts directly through the sphere's interior from $x$ to $y$
> (labelled "euclidean distance"). → TikZ 3D sphere, two views.

#### Exercise *(Corsin p. 6)*

Show that the supremum metric from example 3 is a metric.

#### Solution *(Corsin p. 6)*

Symmetry and definiteness are clear. For the triangle inequality, let
$f, g, h \in C^0([0,1])$ and set $p := f - h$, $q := h - g$. Then for all $x \in [0,1]$:
$$|p(x)| \leq \sup|p| \qquad \text{and} \qquad |q(x)| \leq \sup|q|.$$
Adding the inequalities, for all $x \in [0,1]$:
$$
\begin{aligned}
|f(x) - g(x)| = |p(x) + q(x)| &\leq |p(x)| + |q(x)| \\
&\leq \sup|p| + \sup|q| \\
&= \sup|f - h| + \sup|h - g|. \qquad \square
\end{aligned}
$$

### 3. Open and closed sets

*(Corsin p. 6)*

Let $(X,d)$ be a metric space, let $x \in X$, and let $r \in \mathbb{R}$. Then we define the
**open ball** of radius $r$ as
$$B_r(x) := \{\,\boxed{y \in X}\, : d(y,x) < r\,\}$$

> **Corsin marks the boxed part in red: "important subtlety!"** — the ambient set $X$ in
> $y \in X$ is what makes openness relative to the space, and it is exactly what the
> "common misconception" on p. 8 turns on. Preserve this emphasis in the typeset version.

> ⚠️ **Check:** stated for $r \in \mathbb{R}$ rather than $r > 0$. Harmless here, but loose.
> See `OQ-03`.

Then we call a subset $U \subseteq X$ **open** ("offen") if and only if
$$\forall y \in U \ \exists \varepsilon > 0 \text{ such that } B_\varepsilon(y) \subseteq U.$$

And we call $A \subseteq X$ **closed** ("abgeschlossen") if and only if $X \setminus A$ is open.

#### Exercise *(Corsin p. 7)*

Let $(X,d)$ be a metric space. Show that $X$ and $\emptyset$ are both open and closed.

#### Solution *(Corsin p. 7)*

$X$ is open, since $B_r(x) \subseteq X$ for all $r > 0$, $x \in X$. The empty set contains no
points and is therefore vacuously open. Since $X$ and $\emptyset$ are each other's complement in
$X$, they are also closed. $\square$

### 4. Sequences and convergence

*(Corsin p. 7)*

A **sequence** $(x_n)_{n=0}^{\infty}$ in a metric space $(X,d)$ is a function $x : \mathbb{N} \to X$.

We say that $(x_n)_{n=0}^{\infty}$ **converges** to $x \in X$ if
$$\forall \varepsilon > 0 \ \exists N \in \mathbb{N} \text{ such that } d(x_n, x) < \varepsilon \quad \forall n \geq N.$$

**Proposition.** *(Corsin p. 7)*

1. $U \subseteq X$ is **open** if and only if, for every sequence in $X$ with limit in $U$, the
   sequence eventually lies in $U$.
2. $A \subseteq X$ is **closed** if and only if every convergent sequence in $A$ has its limit in $A$.

#### Examples in $\mathbb{R}^2$ *(Corsin p. 8)*

In the euclidean metric space $\mathbb{R}^2$:

1. $[0,1]^2$ is **closed**.
2. $(0,1)^2$ is **open**.
3. $[0,1] \times (0,1)$ is **neither open nor closed**.

> **[FIG-W02-05]** *(Corsin p. 8)* Three small sketches, one per case: a solid-bordered square
> with a purple sequence $x_n$ converging to a red $\times$ on the boundary; a dashed-bordered
> square with $x_n$ approaching from outside; and a square with solid left/right and dashed
> top/bottom edges carrying two sequences $x_n$, $y_n$ with limits $\times$ and $y$.
> → TikZ, three sub-panels.

**Common misconception!** *(Corsin p. 8)*

In the euclidean metric space $X = [0,1]^2$, the set $[0,1]^2$ **is open**!!!

| $[0,1]^2 \subseteq \mathbb{R}^2$ | $[0,1]^2 \subseteq [0,1]^2$ |
|---|---|
| **Not open**, since $B_\varepsilon(x)$ is not contained in $[0,1]^2$ if $x$ is on the boundary. | **Open**, since the full space is always open, as shown before. |

> **[FIG-W02-06]** *(Corsin p. 8)* Two panels side by side: left, a square with a red boundary
> point $x$ and an orange dashed ε-ball spilling outside; right, the same square where the ε-ball
> is clipped to the square. → TikZ, two panels.

#### Exercise *(Corsin p. 9)*

1. Write down the definition of convergence of a sequence $(f_n)_{n=0}^{\infty}$ to $f$ in the
   metric space $X$ of bounded functions $[0,1] \to \mathbb{R}$ with the **supremum metric**.
2. You know the resulting expression from Analysis 1. What is it called?
3. *(Optional)* Use the fact that $C^0([0,1]) \subseteq X$ is closed and the previous
   proposition on "sequentially closed" to conclude a big result from Analysis 1.

#### Solution *(Corsin pp. 9–10)*

1. $\displaystyle \forall \varepsilon > 0 \ \exists N \in \mathbb{N} : \sup_{x \in [0,1]} |f_n - f| < \varepsilon \quad \forall n \geq N$.

2. This is **uniform convergence** ("gleichmässige Konvergenz")!

3. $C^0([0,1])$ is closed in the space of bounded functions with the supremum metric.
   *Proof.* Let $f \in X \setminus C^0([0,1])$, i.e. $f : [0,1] \to \mathbb{R}$ is bounded and has
   at least one discontinuity at a point $x_0 \in [0,1]$. That is, we find $\varepsilon > 0$ such
   that for all $\delta > 0$ there exists $y \in (x_0 - \delta, x_0 + \delta)$ with
   $|f(x_0) - f(y)| \geq \varepsilon$. Then the $\tfrac{\varepsilon}{3}$-ball in $X$,
   $$B_{\varepsilon/3}(f) = \Big\{ g \in X : \sup_{x \in [0,1]} |f(x) - g(x)| < \tfrac{\varepsilon}{3} \Big\},$$
   is contained in $X \setminus C^0([0,1])$.

   Given this fact, the "sequentially closed" proposition ensures that the uniform limit $f$ of
   $(f_n)_{n=0}^{\infty}$ in $C^0([0,1])$ is also in $C^0([0,1])$, i.e. continuous, given that
   $f : [0,1] \to \mathbb{R}$ is bounded. This is the case, since $f_n$ is bounded for all
   $n \in \mathbb{N}$, and with $\varepsilon = 1$ we find $N \in \mathbb{N}$ such that
   $$\sup_{x \in [0,1]} |f_N(x) - f(x)| < 1 \implies f \text{ bounded.} \qquad \square$$

> **[FIG-W02-07]** *(Corsin p. 10)* The "ε-tube": a blue curve $f$ on $[0,1]$ flanked by two red
> dotted curves at vertical distance $\varepsilon/3$, with an orange double arrow marking
> $\varepsilon$. Caption: $B_\varepsilon(f)$ in the space of bounded functions on $[0,1]$ is the
> "ε-tube" around $f$. → TikZ plot with offset envelopes.

---

## Friday

### Warm-up question *(Corsin p. 11)*

What is the shape of $B_1(0) \subseteq \mathbb{R}^2$ with

- the **supremum metric**?
- the **Manhattan metric**?

**Answer.** Supremum: the axis-aligned **square** $[-1,1]^2$, whose edge midpoints are
$(\pm 1, 0)$ and $(0,\pm 1)$. Manhattan: the **diamond** with vertices $(\pm 1, 0)$, $(0,\pm 1)$.

> **[FIG-W02-08]** *(Corsin p. 11)* Two axis systems side by side; left, a blue dashed square
> (supremum unit ball) with $(0,1)$ and $(1,0)$ marked orange; right, a blue dashed diamond
> (Manhattan unit ball) with the same two points marked. → TikZ, two panels.

### Definition: continuous functions *(Corsin p. 11)*

For $(X, d_X)$, $(Y, d_Y)$ metric spaces, a function $f : X \to Y$ is called **continuous**
("stetig") if one of the following equivalent conditions holds:

1. **(ε–δ)**: $\forall x_0 \in X$, $\varepsilon > 0$ $\exists \delta > 0$ such that for all $x \in X$:
   $$d(x_0, x) < \delta \implies d(f(x_0), f(x)) < \varepsilon$$
   > ⚠️ **Check:** Corsin writes $d(x_0,x) < \varepsilon$ in the hypothesis, which must be
   > $\delta$ — otherwise $\delta$ is never used. A slip of the pen; corrected here and
   > logged as `OQ-05`.
2. **(sequentially continuous)**: for any sequence $(x_n)_{n=0}^{\infty}$ in $X$ with limit
   $x \in X$, $\lim_{n\to\infty} f(x_n) = f(x)$ (and the limit exists).
3. **(topological)**: for all $U \subseteq Y$ open, $f^{-1}(U) \subseteq X$ is open.

> These are exactly the "three equivalent definitions of continuity seen in class" that
> problem 2.7 asks you to use.

#### Example *(Corsin p. 12)*

Let $f : \mathbb{R} \to \mathbb{R}$, $x \mapsto x^2$. Let $a < b \in \mathbb{R}$. Then

- for $a < 0 < b$: $\quad f^{-1}((a,b)) = (-\sqrt{b}, \sqrt{b})$, open.
- for $a < b < 0$: $\quad f^{-1}((a,b)) = \emptyset$.
- for $0 < a < b$: $\quad f^{-1}((a,b)) = (-\sqrt{b}, -\sqrt{a}) \cup (\sqrt{a}, \sqrt{b})$.

**Why is it enough to check only these cases?**
*Hint:* $f^{-1}(U_1 \cup U_2) = f^{-1}(U_1) \cup f^{-1}(U_2)$.

#### Questions *(Corsin p. 12)*

2. Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces, where $d_Y$ is the **discrete metric**. Is
   $f : (X,d_X) \to (Y,d_Y)$ continuous?
3. What if $d_X$ is the discrete metric and $d_Y$ is arbitrary?

#### Answers *(Corsin p. 12)*

2. **No.** For example, take the spaces $X = Y = \mathbb{R}$, $d_X$ the standard metric, and
   $f = \operatorname{id} : X \to Y$, $z \mapsto z$. Then $\{0\} \subseteq Y$ is open, but
   $\{0\} = \operatorname{id}^{-1}\{0\}$ is not open in $(X, d_X)$.
3. **Any** subset of $X$ is open; therefore $f^{-1}(U)$ is open for any open $U \subseteq Y$.
   (So every such $f$ is continuous.)

### Definition: Cauchy sequence, complete metric space *(Corsin p. 13)*

Let $(X,d)$ be a metric space and $(x_n)_{n=0}^{\infty}$ a sequence in $X$. We say that
$(x_n)_{n=0}^{\infty}$ is **Cauchy** if
$$\forall \varepsilon > 0 \ \exists N \in \mathbb{N} \text{ such that } d(x_n, x_m) < \varepsilon \quad \forall n, m \geq N.$$

$(X,d)$ is a **complete metric space** ("vollständiger metrischer Raum") if every Cauchy sequence
in $X$ converges with respect to $d$.

**Examples.**

- The Euclidean spaces $(\mathbb{R}^n, \langle\cdot,\cdot\rangle_{\text{eucl}})$ are **complete**.
- Any **non-closed** subset $U \subseteq \mathbb{R}^n$ (standard metric) and the rationals
  $\mathbb{Q}$ are **not complete**.
- $\big(C^0([0,1]), \sup_{x \in [0,1]}|\cdot|\big)$ is **complete**. *(Zorich, p. 22)*

### Definition: Compactness *(Corsin p. 13)*

A metric space $(X,d)$ is **compact** ("kompakt") if every open cover has a finite subcover.

**Theorem.** $(X,d)$ metric space is **compact** if and only if every sequence in $X$ has a
convergent subsequence in $X$.

> **[FIG-W02-09]** *(Corsin p. 14)* Open cover of a metric space: a blue blob $X$ tiled by three
> dotted overlapping regions $U_1$ (red), $U_2$ (orange), $U_3$ (purple), annotated
> $U_1 \cup U_2 \cup U_3 = X$, $U_i \subseteq X$ open sets. → TikZ freeform regions.

*(Corsin p. 14)* A subset $K$ of a metric space $(X,d)$ is compact if the metric space
$(K, d|_{K \times K})$ is compact. This is equivalent to the definition in the script:

> **Definition 9.63 (Compactness)** — *quoted from the official lecture notes, pasted into
> Corsin's notes on p. 14.*
>
> Let $(X,d)$ be a metric space. A subset $K \subset X$ is called **compact** if one of the
> following equivalent conditions hold:
>
> 1. $K$ is **sequentially compact**: every sequence $(x_n)_{n\in\mathbb{N}}$ in $K$ has a
>    subsequence that is convergent in $K$.
> 2. $K$ is **topologically compact**: every family of open sets $\{U_i\}_{i \in I}$ that cover
>    $K$, has a finite subcover.

> **[FIG-W02-10]** *(Corsin p. 14)* Open cover of a subset: a blue blob $X$ containing a purple
> blob $K$, covered by three dotted regions $U_1$ (red), $U_2$ (purple), $U_3$ (green) that
> extend beyond $K$; annotated $K \subseteq U_1 \cup U_2 \cup U_3 \subseteq X$. → TikZ freeform regions.

#### Exercise *(Corsin p. 15)*

Let $(X,d)$ be a metric space.

1. Show that every finite subset $\{x_1, \dots, x_n\} \subseteq X$ is compact.
2. If $X$ is compact, is it complete?

#### Solution *(Corsin p. 15)*

1. Let $\{U_\alpha\}_{\alpha \in I}$ be an open cover of $\{x_1, \dots, x_n\}$. For each
   $i = 1, \dots, n$, pick $U_{\alpha_i}$ such that $x_i \in U_{\alpha_i}$. Then
   $\{U_{\alpha_i}\}_{i=1,\dots,n}$ is a finite subcover. $\square$

2. **Yes.** Let $(x_n)_{n=0}^{\infty}$ be a Cauchy sequence in $X$. Then, because $X$ is compact,
   we find a convergent subsequence, $\lim_{i \to \infty} x_{n_i} = x \in X$.

   Fix $\varepsilon > 0$. We find $N_1 \in \mathbb{N}$ such that
   $$d(x_n, x_m) < \varepsilon \quad \forall n, m > N_1$$
   and $N_2 \in \mathbb{N}$ such that
   $$d(x, x_{n_i}) < \varepsilon \quad \forall i > N_2.$$
   For $N := \max\{N_1, N_2\}$ and $k > N$:
   $$d(x, x_k) \leq d(x, x_{n_k}) + d(x_{n_k}, x_k) < 2\varepsilon$$
   where we used $n_k \geq k > N$. So any Cauchy sequence converges. $\square$

   > ⚠️ **Check:** Corsin writes $n_k > k$; for a subsequence the standing fact is
   > $n_k \geq k$. Immaterial to the argument. See `OQ-06`.

---

## German glossary contributed by this week

| English | German |
|---|---|
| space | Raum |
| metric space | metrischer Raum |
| metric | Metrik |
| open / closed set | offene / abgeschlossene Menge |
| continuity, continuous | Stetigkeit, stetig |
| uniform convergence | gleichmässige Konvergenz |
| complete metric space | vollständiger metrischer Raum |
| compact | kompakt |
| triangle inequality | Dreiecksungleichung |
