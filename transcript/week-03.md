# Week 3 — Compactness, Connectedness & Cauchy–Schwarz

**Primary source:** `Corsin Nick/Class Notes/Week 3.pdf` (12 pp)
**Exercise sheet:** `exercises/Ex3_Analysis2_eng.pdf` (solutions: `Sol3_Analysis2_eng.pdf`)
**Lecture notes:** ch. 9 (sheet 3 cites *Definition 9.89* for norms and *Definition 9.96* for the Hilbert–Schmidt norm)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **Title note.** The chapter is titled *Compactness, Connectedness & Cauchy–Schwarz* rather
> than the provisional "Banach Fixed Point" — Corsin covers the fixed-point material only
> through the exercise sheet (3.1, 3.5); his Friday class goes to path-connectedness and
> Cauchy–Schwarz instead.

> **No priority page this week.** Corsin's colour-coded *Recommended exercises* page starts
> later in the semester; Week 3 opens directly with the Monday class. Problems carry only the
> official `(*)` marker.

---

## Exercise sheet 3

*Statements quoted verbatim from `exercises/Ex3_Analysis2_eng.pdf` (assigned 2 March 2026,
due 9 March 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### 3.1 — Lipschitz or not

Give an example of:

(a) A $\tfrac{1}{2}$-Lipschitz function $f : [0,1) \to [0,1)$ that has no fixed point.
(b) A map $f : \mathbb{R}^2 \to \mathbb{R}^2$ that has no fixed point, but is an isometry, i.e.
$\|f(x) - f(x')\| = \|x - x'\|$ for all $x, x' \in \mathbb{R}^2$.

### 3.2 — Problems at the origin

Show that there is no continuous function $f : \mathbb{R}^2 \to \mathbb{R}$ such that
$f(x,y) = xy/(x^2+y^2)$ for all $(x,y) \neq (0,0)$. On the other hand, show that there is
exactly one continuous function $g : \mathbb{R}^2 \to \mathbb{R}$ such that
$g(x,y) = xy/\sqrt{x^2+y^2}$ for all $(x,y) \neq (0,0)$.

*Official hint:* if a function is continuous at $0$ and $x_k \to 0$ and $y_k \to 0$, then
$f(x_k)$ and $f(y_k)$ must converge to the same value.

### 3.3 — Open, closed, complete and compact

For each of the following subsets of $\mathbb{R}^N$ say whether they are
open / closed / none / compact (with respect to the standard Euclidean structure). Try to prove
your assertions "efficiently".

1. $E_1 := \{x \in \mathbb{R}^3 : 0 < x_2 \leq 2\}$
2. $E_2 := \{x \in \mathbb{R}^n : \sin(\|x\|) \geq \tfrac{1}{4}\}$
3. $E_3 := \bigcup_{n \geq 1}\{x \in \mathbb{R}^3 : x_1^4 - \tfrac{1}{n}x_3^2 - x_2^2 > \tfrac{1}{n},\ x_1 + x_2 < 6\}$
4. $E_4 := \{(x,y) \in (\mathbb{R}^n \times \mathbb{R}^n) : x \cdot y > \tfrac{1}{2}\|x\|\|y\|\}$
5. $E_5 := \{X \in \mathbb{R}^{n\times n} : \text{the matrix } X \text{ is invertible}\}$
6. $E_6 := \{X \in \mathbb{R}^{n\times n} : \text{the matrix } X \text{ is symmetric}\}$
7. $E_7 := \{X \in \mathbb{R}^{n\times n} : \text{the entries of } X \text{ are either } 0 \text{ or } 1\}$
8. $E_8 := \{x \in \mathbb{R}^n : |x_i| \leq 6 \text{ for all } 1 \leq i \leq n\}$
9. $E_9 := E_8 \times E_3 \subset \mathbb{R}^{n+3}$
10. $E_{10} := E_2 \cap E_8 \subset \mathbb{R}^n$

### 3.4 — Multiple choice (open, complete, compact)

Select all the statements below that are true.

(a) A nonempty open strict subset of $\mathbb{R}^n$ cannot be compact.
(b) A nonempty open strict subset of $\mathbb{R}^n$ cannot be complete.
(c) A complete subset of $\mathbb{R}^n$ contains all its accumulation points.
(d) Countable union of complete subsets of $\mathbb{R}^n$ is complete.
(e) A subset is closed in $\mathbb{R}^n$ if and only if it is complete as a metric space itself
    (with the distance inherited from $\mathbb{R}^n$).

### 3.5 — Multiple choice (fixed points)

Select all the statements below that are true.

(a) If you spread a map of Zurich on your desk, then one point of the desk will coincide with its
    representation on the map (in an ideal world).
(b) If $f : [0,1] \to [0,2]$ is $\tfrac{1}{2}$-Lipschitz, then $f$ has a fixed point.
(c) If $f : [0,2] \to [0,1]$ is $\tfrac{1}{2}$-Lipschitz, then $f$ has a fixed point.
(d) If $f : [0,1] \cup [2,3] \to [0,1] \cup [2,3]$ is continuously differentiable with
    $|f'(x)| < 1$ for all $x \in [0,1]\cup[2,3]$, then it has a fixed point.
(e) **(\*)** If $f : [0,1] \to [0,1]$ is differentiable with $|f'(x)| < 1$ for all
    $x \in (0,1)$, then it has a fixed point.

### 3.6 — Multiple choice (uniform continuity)

Select all the statements below that are true.

(a) The function $(x,y) \mapsto x+y$ is uniformly continuous in $\mathbb{R}^2$.
(b) The function $(x,y) \mapsto xy$ is uniformly continuous in $\mathbb{R}^2$.
(c) The function $(x,y) \mapsto x+y$ is uniformly continuous in $[0,1]^2$.
(d) The function $(x,y) \mapsto xy$ is uniformly continuous in $[0,1]^2$.

> **Ties into the class notes:** Corsin's third reason to care about compactness (p. 3) is
> precisely that a continuous function on a compact space is uniformly continuous — which
> settles (c) and (d) at once.

### 3.7 — Cauchy–Schwarz

Let $V$ be a vector space over $\mathbb{R}$, let $\langle\cdot,\cdot\rangle$ be an inner product
on $V$, and let $\|\cdot\| : V \to \mathbb{R}$ be given by $\|v\| = \sqrt{\langle v,v\rangle}$.
Then the inequality
$$|\langle v,w\rangle| \leq \|v\|\|w\| \tag{1}$$
holds for all $v, w \in V$. Furthermore, equality in (1) holds if and only if $v$ and $w$ are
linearly dependent.

> **Ties into the class notes:** Corsin devotes the whole second half of Friday (pp. 9–12) to
> this problem, including the geometric reading and an explicit proof hint.

### 3.8 — Inner product and norm

Let $V$ be a vector space over $\mathbb{R}$, let $\langle -,-\rangle$ be an inner product on $V$.
The map defined by
$$\|\cdot\| : V \to \mathbb{R}, \qquad \|v\| = \sqrt{\langle v,v\rangle}$$
satisfies the triangular inequality and is a norm.

### 3.9 — All norms are equivalent in $\mathbb{R}^n$

Let $|\cdot|$ denote the standard Euclidean norm in $\mathbb{R}^n$ and let
$f : \mathbb{R}^n \to [0,\infty)$ be another norm (that is, a function satisfying the properties
of *Definition 9.89*).

1. Expressing $x$ in a basis and using the "abstract" properties that $f$ must have, show that
   there is a constant $C_1 > 0$ such that $f(x) \leq C_1|x|$ for all $x \in \mathbb{R}^n$.
2. Show that $f$ is continuous in $\mathbb{R}^n$ (with respect to the standard distance of
   $\mathbb{R}^n$!).
3. Show that there is a number $c_2 > 0$ such that $f(x) \geq c_2$ for all $|x| = 1$.
4. Conclude that $f(x) \geq c_2|x|$ for all $x \in \mathbb{R}^n$.
5. Show that if $\tilde f$ is yet another norm, then there is $C > 0$ such that
   $C^{-1}f(x) \leq \tilde f(x) \leq Cf(x)$ for all $x \in \mathbb{R}^n$.

*Official hints:* **3.9.2** — recall that from the definition it follows that
$|f(x) - f(y)| \leq f(x-y)$, and that Lipschitz functions are always continuous.
**3.9.3** — apply the Weierstrass theorem to $f$ on $S := \{x \in \mathbb{R}^n : |x| = 1\}$ and
use that $f$, being a norm, is nondegenerate. **3.9.5** — if $f$ is equivalent to $|\cdot|$ and
$\tilde f$ is equivalent to $|\cdot|$, it follows by transitivity that $f$ is equivalent to
$\tilde f$.

> **Ties into the class notes:** hint 3.9.3 is exactly Corsin's reason #2 for caring about
> compactness (p. 3) — the Weierstrass/extreme value theorem on the compact unit sphere.

### 3.10 — Hilbert–Schmidt norm of the composition

Take two linear functions $\varphi : \mathbb{R}^d \to \mathbb{R}^n$ and
$\psi : \mathbb{R}^n \to \mathbb{R}^m$, and denote with $\Phi$, $\Psi$ the matrices that
represent them in the canonical bases. Recall that the linear map
$\psi \circ \varphi : \mathbb{R}^d \to \mathbb{R}^m$ is represented in these bases by the matrix
$\Psi \cdot \Phi$. Show that
$$\|\Psi \cdot \Phi\| \leq \|\Psi\|\|\Phi\|,$$
where $\|\cdot\|$ is the Hilbert–Schmidt norm of a matrix (see *Definition 9.96* in the notes).

*Official hint:* recall that $\|M\|^2$ is the sum of the squares of the entries of $M$. Notice
that $(\Psi\cdot\Phi)^i_j$ ($i$-th row, $j$-th column) is the scalar product of $\Psi^i$ and
$\Phi_j$, which are vectors of $\mathbb{R}^n$. Apply Cauchy–Schwarz to each of them.

### 3.11 — (\*) Uniform continuity and moduli of continuity

Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces and let $f : X \to Y$.

A **modulus of continuity** is a function $\omega : [0,\infty) \to [0,\infty]$ such that
$$\omega(0) = 0, \qquad \omega \text{ is nondecreasing}, \qquad \lim_{t \downarrow 0}\omega(t) = 0.$$
(Here $[0,\infty]$ means we also allow the value $+\infty$.)

We say that $f$ **has modulus of continuity** $\omega$ if
$$d_Y\big(f(x), f(y)\big) \leq \omega\big(d_X(x,y)\big) \qquad \forall x,y \in X.$$

1. Prove that $f$ is uniformly continuous on $X$ if and only if $f$ has a modulus of continuity.
2. *(Bonus 1)* Assume $X \subset \mathbb{R}$ is an interval with the usual distance
   $d_X(x,y) = |x-y|$. Show that the modulus constructed in (1) can be chosen **subadditive**, i.e.
   $\omega(t_1+t_2) \leq \omega(t_1) + \omega(t_2)$ for all $t_1, t_2 \geq 0$.
3. *(Bonus 2)* Assume $X \subset \mathbb{R}^n$ is **convex**, meaning: for all $x_1, x_2 \in X$
   and all $\lambda \in [0,1]$, $(1-\lambda)x_1 + \lambda x_2 \in X$. With
   $d_X(x,y) = \|x-y\|$ (Euclidean distance), show again that the modulus from (1) can be chosen
   subadditive.

*Remark (official).* In general metric spaces a modulus of continuity may have infinite value for
finite $t > 0$. Example: $X = \mathbb{Z}$ with the usual distance, $Y = \mathbb{R}$,
$f(n) = n^2$. This $f$ is uniformly continuous on $\mathbb{Z}$ (because points closer than 1 must
be equal), but no finite $\omega(1)$ can bound $|f(n+1) - f(n)| = 2n+1$ for all $n$. Allowing the
value $+\infty$ avoids this issue, and in many familiar settings (e.g. intervals/convex sets in
$\mathbb{R}^n$) the resulting $\omega_f(t)$ is finite for all $t$.

*Official hints:* **3.11.1** — define the "worst oscillation at scale $t$"
$\omega_f(t) := \sup\{d_Y(f(x),f(y)) : d_X(x,y) \leq t\}$. **3.11.2 / 3.11.3** — if
$d_X(x,y) \leq t_1 + t_2$, choose an intermediate point $z$ on the segment from $x$ to $y$ so
that $d_X(x,z) \leq t_1$ and $d_X(z,y) \leq t_2$, then use the triangle inequality in $Y$.

---

## Monday

### Compactness (continued)

*(Corsin p. 1)*

**Theorem (Heine–Borel).** A subset $K \subseteq \mathbb{R}^n$ equipped with the **standard
metric** is **compact** if and only if it is **closed** and **bounded**.

This captures our intuition of a "compact" set. We will briefly show that Heine–Borel is **false**
for $\mathbb{R}^n$ with an **arbitrary metric**.

#### Exercise *(Corsin p. 1)*

Let $(X,d)$ be a metric space.

1. Show that $\tilde d(x,y) := \dfrac{d(x,y)}{1 + d(x,y)}$ is a metric on $X$. *(Optional)*
2. Show that, if $U \subseteq X$ is open with respect to $d$, then $U$ is open with respect to
   $\tilde d$.
3. Show that, for $X = \mathbb{R}^n$, $d(x,y) = \dfrac{|x-y|}{1+|x-y|}$,
   $\mathbb{N} \subseteq X$ is closed and bounded but not compact.

> ⚠️ **Check:** part 3 sets $X = \mathbb{R}^n$ but then works with $\mathbb{N} \subseteq X$ and
> $|x-y|$, which only parses for $n = 1$. See `OQ-04`.

#### Solution *(Corsin pp. 2–3)*

**1.** Non-negativity, definiteness and symmetry follow from $d(x,y)$.

*Triangle inequality.* We want to show
$$\frac{d(x,y)}{1+d(x,y)} \leq \frac{d(x,z)}{1+d(x,z)} + \frac{d(z,y)}{1+d(z,y)}.$$
Denote $d(x,y) = d_1$, $d(x,z) = d_2$, $d(z,y) = d_3$ and multiply out:
$$
\begin{aligned}
&d_1(1+d_2)(1+d_3) \leq d_2(1+d_1)(1+d_3) + d_3(1+d_1)(1+d_2) \\
\iff\ & (d_1 + d_1d_2)(1+d_3) \leq (d_2 + d_2d_1)(1+d_3) + (d_3 + d_1d_3)(1+d_2) \\
\iff\ & d_1 + \underline{d_1d_3} + d_1d_2d_3 + \underline{d_1d_2} \leq d_2 + d_3d_2 + d_2d_1d_2 + \underline{d_2d_1} \\
& \qquad\qquad\qquad\qquad\qquad\quad + d_3 + d_3d_2 + \underline{d_1d_3} + d_1d_3d_2 \\
\iff\ & d_1 \leq d_2 + 2d_2d_3 + d_3 + d_1d_2d_3 \\
\iff\ & 0 \leq 2d_2d_3 + d_1d_2d_3 \qquad \text{(subtract the triangle inequality } d_1 \leq d_2 + d_3\text{)}
\end{aligned}
$$
which is true by non-negativity. $\square$

> ⚠️ **Check:** the underlined cancellation on the third line contains a stray $d_2d_1d_2$ where
> the expansion gives $d_2d_1d_3$. The conclusion is unaffected — the cancelled terms are the
> underlined ones — but the intermediate line should be re-derived cleanly when typesetting.
> See `OQ-08`.

**2.** Let $U \subseteq X$ be open. Then, given $x \in U$, we find $r > 0$ such that
$B_r(x) = \{y \in X : d(x,y) < r\} \subseteq U$. Let $\varepsilon := \dfrac{r}{1+r}$. Then
$\tilde B_\varepsilon(x) \subseteq B_r(x) \subseteq U$, where
$\tilde B_\varepsilon(x) := \{y \in X : \tilde d(x,y) < \varepsilon\}$. $\square$

**3.** Note that for all $x, y \in \mathbb{R}$, $\dfrac{|x-y|}{1+|x-y|} < 1$. So
$\mathbb{N} \subseteq B_1(0)$, thus it is **bounded** with respect to this metric. Also,
$\mathbb{N}$ is **closed**, as follows from (2). But $x_n = n$ defines a sequence in $\mathbb{N}$
with no convergent subsequence, thus $\mathbb{N}$ is **not compact**.

### Why do we care about compactness?

*(Corsin p. 3)*

1. **Preserved by continuous functions.** $X$, $Y$ metric spaces, $K \subseteq X$ compact,
   $f : X \to Y$ continuous. Then $f(K) \subseteq Y$ is compact.

2. **Weierstrass theorem / Extreme value theorem.** $X$ metric space, $K \subseteq X$ compact,
   $f : K \to \mathbb{R}$ continuous. Then $f$ attains its maximum and minimum in $K$. In
   particular, $f$ is bounded.

3. **Uniform continuity.** $X$, $Y$ metric spaces, $f : X \to Y$ continuous. If $X$ is compact,
   then $f$ is **uniformly continuous** ("gleichmässig stetig").

> **[FIG-W03-01]** *(Corsin p. 3)* Pasted illustration: a continuous function $f(x)$ on a closed
> interval $[a,b]$, with the absolute maximum $f(c)$ marked red and the absolute minimum $f(d)$
> marked blue, with dashed guide lines to the axes. → TikZ plot; redraw rather than embed.

### Connectedness

*(Corsin p. 4)*

**Definition (connected metric space / subset).** A metric space $(X,d)$ is **disconnected**
("unzusammenhängend") if there exist $U_1, U_2 \subseteq X$ subsets which are

1. **open**,
2. **non-empty**, $U_1 \neq \emptyset \neq U_2$,
3. **disjoint**, $U_1 \cap U_2 = \emptyset$,

such that $X = U_1 \cup U_2$. Similarly, for a subset $A \subseteq X$, it is **disconnected** if
it is disconnected as a metric space with the induced metric $d|_{A \times A}$.
**Connected** ("zusammenhängend") is the negation of disconnected.

Typically, proving that a set or metric space is connected is done **by contradiction**, which is
why one should remember the definition of *disconnected*. Intuitively, connected means:

> "The space can not be separated by open sets."

> **[FIG-W03-02]** *(Corsin p. 4)* Two panels. Left, *disconnected*: two separate black blobs,
> each enclosed by its own blue dashed open set $U_1$, $U_2$. Right, *connected*: a single black
> blob with two blue dashed sets $U_1$, $U_2$ whose boundary curves leave a "small gap" (orange
> annotation) — plus a detached purple dashed set annotated "no intersection".
> → TikZ freeform regions, two panels.

**Theorem.** *(Corsin p. 5)* **Continuous functions preserve connected sets.** Let $X$, $Y$ be
metric spaces, $f : X \to Y$ continuous. If $A \subseteq X$ is connected, then $f(A)$ is connected.

#### Exercise *(Corsin p. 5)*

Are the following true or false?

1. The union of connected subsets with a common point is connected.
2. The intersection of connected subsets is connected.
3. The closure of a connected subset is connected.

#### Solution *(Corsin pp. 5–6)*

**1. True.** *Proof.* Let $X$ be a metric space, $V_1, V_2 \subseteq X$ connected, and
$x_0 \in V_1 \cap V_2$. Suppose $V_1 \cup V_2 \subseteq U_1 \cup U_2$ with $U_1, U_2 \subseteq X$
open and disjoint. Assume without loss of generality $x_0 \in U_1$. Then
$U_1 \cap V_1 \neq \emptyset$ and $U_1 \cap V_2 \neq \emptyset$. So, since $V_1, V_2$ are
connected, $V_1 \cap U_2 = V_2 \cap U_2 = \emptyset$. Therefore
$(V_1 \cup V_2) \cap U_2 = \emptyset$ and $V_1 \cup V_2$ is connected. $\square$

> **[FIG-W03-03]** *(Corsin p. 5)* Two overlapping orange blobs $V_1$, $V_2$ sharing the purple
> point $x_0$, both enclosed in a red dotted region $U_1$; a separate red dotted region $U_2$ to
> the right, annotated "no intersection". → TikZ freeform regions.

**2. False.** *Counterexample:*
$$X = \mathbb{R}^2, \quad U = [-1,1] \times \{0\}, \quad V = S^1 = \{x \in \mathbb{R}^2 : \|x\| = 1\},$$
$$U \cap V = \{(-1,0), (1,0)\}.$$

> ⚠️ **Check:** Corsin writes $\|x\| = R^2$ in the definition of $S^1$; it must be $\|x\| = 1$,
> as the stated intersection $\{(\pm 1, 0)\}$ confirms. Corrected here. See `OQ-07`.

> **[FIG-W03-04]** *(Corsin p. 6)* Axes with a red unit circle $S^1$ and an orange horizontal
> segment $[-1,1]\times\{0\}$ through the origin; the two intersection points $(\pm 1, 0)$ marked.
> → TikZ 2D sketch.

**3. True.** Suppose $X$ is a metric space, $A \subseteq X$ a subset with closure $\overline{A}$.
Suppose $U_1, U_2 \subseteq X$ are disjoint open sets covering $\overline{A}$, and assume without
loss of generality $\overline{A} \cap U_1 \neq \emptyset$. Then, since $U_1$ is open,
$A \cap U_1 \neq \emptyset$. By connectedness of $A$, $U_2 \cap A = \emptyset$, and since $U_2$ is
open, also $U_2 \cap \overline{A} = \emptyset$.

---

## Friday

### Path connectedness

*(Corsin p. 6)*

**Definition (paths).** Let $(X,d)$ be a metric space. A continuous function
$\gamma : [0,1] \to X$, where $[0,1]$ carries the standard metric, is called a **path** ("Weg").
More generally, we can replace $[0,1]$ by $[a,b]$ for $a < b$.

**Definition (path-connected).** *(Corsin p. 7)* A metric space $X$ (or subset thereof) is
**path-connected** ("wegzusammenhängend") if for all $x, y \in X$ there exists a path
$\gamma : [0,1] \to X$ with $\gamma(0) = x$, $\gamma(1) = y$.

**Lemma (path connected is connected).** Let $X$ be a metric space. Then $X$ path-connected
implies $X$ connected.

**Proposition.** *For open euclidean subsets, connected is path-connected.* Let
$U \subseteq \mathbb{R}^n$ be open. Then
$$U \text{ path-connected} \iff U \text{ connected}.$$

> ⚠️ **Only for open subsets!** *(Corsin p. 7, marked with a red warning sign)*

**Counterexample: the topologist's sine curve.**
$$S := \left\{\left(t, \sin\left(\tfrac{1}{t}\right)\right) : t > 0\right\} \cup \{0\} \subseteq \mathbb{R}^2$$
$S$ is **connected** but **not path-connected**!

> **[FIG-W03-05]** *(Corsin p. 7)* Plot of $\sin(1/t)$ for $t \in (0, 0.2]$, oscillating ever
> faster and filling a solid blue band as $t \to 0$; vertical range $[-1,1]$.
> → TikZ/pgfplots, sampled densely near 0.

#### $S$ is connected *(Corsin p. 8)*

Any open set $U$ with $0 \in U$ will also contain elements from $S \setminus \{0\}$, which is
path-connected. Since path-connected implies connected and $U \setminus \{0\}$ is also open,
"$S$ disconnected" gives a contradiction.

#### $S$ is not path-connected *(Corsin p. 8)*

Assume by contradiction there is a path from $(0,0)$ to $(\tfrac{1}{\pi}, 0)$,
$$\gamma : [0,1] \to [0, \tfrac{1}{\pi}] \times [-1,1], \qquad t \mapsto (x(t), y(t)).$$
Since $\gamma$ is continuous, $x$ and $y$ must also be continuous. By the **intermediate value
theorem**, $x : [0,1] \to [0,\tfrac{1}{\pi}]$ attains every value in $[0,\tfrac{1}{\pi}]$, since
$x(0) = 0$, $x(1) = \tfrac{1}{\pi}$. Therefore we find a sequence $(a_n)_{n=0}^{\infty}$ such that
$$x(a_n) = \frac{1}{2\pi n + \tfrac{\pi}{2}}.$$
Note that $y(a_n) = 1$ for all $n \in \mathbb{N}$. Thus in the limit $n \to \infty$,
$a_n \to 0$, but $\gamma(a_n) \to (0,1) \neq \gamma(0)$.

**Contradiction to sequential continuity!**

> **[FIG-W03-06]** *(Corsin p. 8)* Two annotated copies of the sine-curve plot. Top: a small
> orange dashed circle labelled $U$ around the origin. Bottom: red dots marking the points
> $\gamma(a_n)$ along the crests $y = 1$, with $\gamma(a_n)$ labelled on the rightmost crest and
> $\gamma(0)$ labelled at the origin. → TikZ/pgfplots with annotations.

### Cauchy–Schwarz

*(Corsin p. 9)*

**Definition (inner product / scalar product).** Let $V$ be a **vector space** over $\mathbb{R}$.
An **inner product** ("Skalarprodukt") on $V$ is a map
$$\langle\cdot,\cdot\rangle : V \times V \to \mathbb{R}$$
satisfying, for all $u, v, w \in V$ and $\alpha, \beta \in \mathbb{R}$:

1. **Bilinearity:** $\langle \alpha u + \beta v, w\rangle = \alpha\langle u,w\rangle + \beta\langle v,w\rangle$,
   and equivalently in the second variable.
2. **Symmetry:** $\langle u,v\rangle = \langle v,u\rangle$.
3. **Definiteness:** $\langle u,u\rangle \geq 0$, and $\langle u,u\rangle = 0 \iff u = 0$.

**Definition (norm).** *(Corsin p. 9)* Let $V$ be a **real** vector space. A **norm** ("Norm") on
$V$ is a map $\|\cdot\| : V \to [0,\infty)$ satisfying, for all $u, v \in V$ and
$\alpha \in \mathbb{R}$:

1. **Definiteness:** $\|v\| \geq 0$, and $\|v\| = 0 \iff v = 0$.
2. **Homogeneity:** $\|\alpha v\| = |\alpha|\|v\|$.
3. **Δ-inequality:** $\|u+v\| \leq \|u\| + \|v\|$.

*(Corsin p. 10)*

- $\|v\| := \sqrt{\langle v,v\rangle}$ defines a norm.
- $d(x,y) := \|x-y\|$ defines a metric.

#### Geometric meaning of the inner product *(Corsin p. 10)*

In $\mathbb{R}^2$, the following identity holds:
$$\langle x,y\rangle := x_1y_1 + x_2y_2 := \|x\|\|y\|\cos\theta$$
where $\theta$ is the angle between $x, y \in \mathbb{R}^2$.

To see this, conveniently choose our basis vectors such that $x = (x_1, 0)$, $y = (y_1, y_2)$.

> **[FIG-W03-07]** *(Corsin p. 10)* Two axis systems joined by a curved arrow labelled "change of
> basis (rotation)". Left: vectors $x$ (blue) and $y$ (orange) at angle $\theta$, both off-axis.
> Right: the same pair rotated so that $x$ lies along the positive horizontal axis, with a dotted
> drop-line from $y$. → TikZ, two panels + arrow.

Then
$$\langle x,y\rangle = x_1y_1 = x_1\|y\|\cos\theta = \|x\|\|y\|\cos\theta.$$

For more rigour, you will show in Linalg that the rotations in $\mathbb{R}^2$ are given by
matrices $R$ satisfying $\langle Rx, Ry\rangle = \langle x,y\rangle$.

*(Corsin p. 11)* In a general inner product space $V$, this becomes the **definition** of the
angle $\theta$. It then makes sense to define the **projection onto $v$**, $\pi_v$:
$$\pi_v(u) = \frac{\langle u,v\rangle}{\|v\|^2}\,v = \|u\|\cos\theta\,\frac{v}{\|v\|}.$$

> **[FIG-W03-08]** *(Corsin p. 11)* A blue vector $u$ and an orange vector $v$ from a common
> origin, angle $\theta$ marked in green; a purple dashed perpendicular from the tip of $u$ onto
> the line spanned by $v$, with the foot labelled $\pi_v(u)$ and a right-angle marker.
> → TikZ 2D sketch.

In words, $\pi_v(u)$ is the part of $u$ which points along $v$. In particular,
$$\|\pi_v(u)\| = \|u\|\,|\cos\theta| = \frac{|\langle u,v\rangle|}{\|v\|}.$$

In this sense, Cauchy–Schwarz says something very obvious — see the picture above:
$$\frac{|\langle u,v\rangle|}{\|v\|} \leq \|u\| \iff \|\pi_v(u)\| \leq \|u\| \iff \|u\|\,|\cos\theta| \leq \|u\|.$$

#### Hint for the proof of Cauchy–Schwarz *(Corsin p. 12)*

Use definiteness and expand the term
$$\langle u - \pi_v(u),\ u - \pi_v(u)\rangle = \dots$$
where $u - \pi_v(u)$ is the **perpendicular part** of $u$ to $v$.

---

## German glossary contributed by this week

| English | German |
|---|---|
| uniformly continuous | gleichmässig stetig |
| connected / disconnected | zusammenhängend / unzusammenhängend |
| path | Weg |
| path-connected | wegzusammenhängend |
| inner product, scalar product | Skalarprodukt |
| norm | Norm |
| closure | Abschluss |
| bounded | beschränkt |
