# Week 5 — Optimization, Lagrange Multipliers & the Hessian Test

**Primary source:** `Corsin Nick/Class Notes/Week 5.pdf` (11 pp)
**Exercise sheet:** `exercises/Ex5_Analysis2_eng.pdf` (solutions: `Sol5_Analysis2_eng.pdf`)
**Lecture notes:** ch. 11 (sheet 5 cites *Theorem 10.16*, *Proposition 10.14*, *Corollary 10.45*)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **No session split this week.** Unlike Weeks 2–4, Corsin marks no `Monday` / `Friday` boxes in
> this file; the material runs continuously from optimization through Lagrange multipliers to the
> Hessian test. Typeset as a single sequence of `\subsection`s with no `\session` heading.

---

## Exercise sheet 5

*Statements quoted verbatim from `exercises/Ex5_Analysis2_eng.pdf` (assigned 16 March 2026,
due 23 March 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 5.1 | **important** | "Recall the linearity of the differential and that $C^1 \Rightarrow$ differentiable" |
| 5.2 | **important** | "Compare with the example from the script and recall that continuous functions on compact sets attain their extrema." |
| 5.3 | **important** | "There is no difference between $x \to 0$ and $|x| \to 0$." |
| 5.4 | **semi-important** | "Use the definition of directional derivative, $\partial_v f(x) = \left.\frac{\partial}{\partial t}\right\|_{t=0} f(x+tv)$. Solve a few of these, but not all." |
| 5.5 | **optional** | — |
| 5.6 | **optional** | "Interesting, but irrelevant for the course" |
| 5.7 | **optional** | "Interesting for physicists, will be covered in classical mechanics." |

### 5.1 — Derivatives *(important)*

(a) Consider $f(x,y) := xy^2e^{-x^2-y^2}$ for $(x,y) \in \mathbb{R}^2$. Find all the critical
points of $f$, that is all the points where the gradient of $f$ vanishes. (The point will be
given if and only if all the numerical values you find are correct… so check your computations
twice.)

(b) We want to find a function $g \in C^1(\mathbb{R}^2)$ with the following directional
derivative:
$$\partial_v g(x,y) = 2\cos(x^2y)xv_2 + \cos(x^2y)v_1^2y \quad \text{for all } (x,y) \text{ and } (v_1,v_2) \in \mathbb{R}^2.$$
Give an explicit example of such a function $g$ or prove that a function with these properties
cannot exist.

> Corsin's hint — *recall the linearity of the differential* — is the whole of part (b): a
> directional derivative must be **linear** in $v$, and $v_1^2$ is not.

### 5.2 — Lagrange multipliers *(important)*

Consider the ball $U := \{(x,y,z) : x^2+y^2+z^2 < 1\}$ and the function
$$f(x,y,z) := 1 - x^2 - y^2 + 4x.$$

1. Motivate rigorously why $f$ attains its absolute maximum and minimum in $\overline{U}$.
2. Find all the critical points of $f$ which lie in the interior of $U$. Say whether
   $\sup_U f$ (or $\inf_U f$) is attained at some point in $U$.
3. Say whether $\max_{\partial U} f$ and $\min_{\partial U}$ exist.
4. With the method of Lagrange multipliers, find the possible critical points for the constrained
   problem $\max\{f(x,y,z) : (x,y,z) \in \partial U\}$, and same for min.
5. Among all the points you have found, clarify at which points the maximum/minimum of $f$ is
   attained.

### 5.3 — Multiple choice (Landau notation) *(important)*

Mark all and only the statements which are true.

(a) As $|x| \to 0$, if $f(x) = x_2x_1^2 + O(x_1^2)$, then $f(x) = O(|x|^2)$.
(b) As $x \to 0$, if $f(x) = x_2x_1^2 + O(x_1^3)$, then $f(x) = O(x_1^3)$.
(c) As $|x| \to 0$, if $f(x) = x_2x_1 + O(|x|^2)$, then $f$ is differentiable at $x = 0$.
(d) As $x \to 0$, if $f(x) = x_2x_1 + O(|x|^2)$, then $f$ is twice differentiable around $x = 0$.
(e) As $|x| \to 0$, if $f(x) = x_2x_1 + O(|x|^3)$, then $f$ is twice differentiable around
    $x = 0$ and $\partial_{11}f(0) = 0$.

*Official hint:* revise *Corollary 10.45*.

### 5.4 — Computation of derivatives *(semi-important)*

For each of the following functions compute the directional derivative in the general direction
$v$ at a general point $x$, that is $\partial_v f(x)$, where applicable.

1. $x_1/x_2$, $e^{-x_1/x_2}$ for $x \in \mathbb{R}^2\setminus\{x_2 = 0\}$. (Also: can they be
   extended continuously or differentiably across $\{x_2 = 0\}$?)
2. $e^{x_1x_2}\sin(x_1+x_2^2)$, $\dfrac{x_1^2}{x_1^2+x_2^2}$, $\dfrac{x_1^2x_2}{x_1^2+x_2^2}$,
   $\dfrac{x_1^2x_2}{x_1^2+x_2^4}$ for $x \in \mathbb{R}^2\setminus\{0\}$. (Also: can they be
   extended continuously or differentiably across the origin?)
3. $|x|$, $|x|^\alpha$, $x/|x|$, $g(|x|)$, $x\cdot e$, $g(x\cdot e)$, for $\alpha \in \mathbb{R}$,
   $e \in \mathbb{R}^n$ and $g \in C^1(\mathbb{R})$.
4. $ax$, $x^{\mathsf T}$, $\operatorname{Tr}(x)$, $x^2$, $x^3$, $\operatorname{Tr}(x^2)$ for
   $x, a \in \mathbb{R}^{n\times n}$.
5. **(\*)** $x^{-1}$, $x^{-2}$ for $x \in \mathbb{R}^{n\times n}$ with $\det x \neq 0$.

*Official hints:* to prove that a function **is** differentiable at 0 you have two tools — the
definition of differentiability, and the sufficient condition of *Theorem 10.16*. To prove that a
function **is not** differentiable at 0 you have two tools — show that the necessary condition of
*Proposition 10.14* does not hold, or show that for some $C^1$ curve
$\gamma : (-\delta,\delta)\to\mathbb{R}^n$ the function $(f\circ\gamma)(t)$ is **not**
differentiable at $t = 0$ (simpler, as you study a function of one variable).
**5.4.3** — these functions are $C^\infty$, so compute them on $x+tv$ and find an expansion in
powers of $t$; by *Corollary 10.45* it must be the Taylor polynomial, from which the derivatives
can be read off. For example
$(x+tv)^2 = x^2 + (xv+vx)t + O(t^2)$.

### 5.5 — Multiple choice (cost of a Taylor expansion) *(optional)*

Assume $g \in C^\infty(\mathbb{R})$ and $f \in C^\infty(\mathbb{R}^n)$ is such that
$$f(x) = x_1 + x_2x_1 + O(|x|^4) \quad \text{as } x \to 0.$$
We want to compute the Taylor expansion of $(g\circ f)$ at $x = 0$ of the highest possible order
with the information we have. We can ask for the value $g^{(k)}(t)$ for arbitrary
$k \in \mathbb{N}$, $t \in \mathbb{R}$, but we have to pay 5 CHF each time.

For a general $g$, which is the degree of the best (i.e. highest-order) Taylor polynomial we can
compute? How expensive will it be to compute it?

(a) degree 3 and 20 CHF (b) degree 2 and 15 CHF (c) degree 2 and 10 CHF (d) degree 3 and 15 CHF

### 5.6 — Polynomials *(optional — "interesting, but irrelevant for the course")*

Let $P, Q \in \mathbb{R}[x_1,\dots,x_n]$ be polynomials of $n$ variables; assume that there are
positive numbers $M, \sigma$ such that
$$|P(x) - Q(x)| \leq M|x|^\sigma \quad \text{for all } |x| \leq 1.$$
Show that $P$ and $Q$ have the same coefficients of order smaller than $\sigma$. That is, if we
write $P(X) = \sum_{\alpha\in\mathbb{N}^n} a_\alpha X^\alpha$,
$Q(X) = \sum_{\alpha\in\mathbb{N}^n} b_\alpha X^\alpha$, then $a_\alpha = b_\alpha$ for all
$|\alpha| < \sigma$.

### 5.7 — Chain rule for a curve, or: a car on Earth *(optional — "interesting for physicists")*

Let $R > 0$ and $\omega \in \mathbb{R}$ be constants. Let
$\sigma : I \subset \mathbb{R}\to\mathbb{R}^2$, $\sigma(t) = (a(t), b(t))$, which we interpret as
a curve in a "map" representing the longitude and latitude of a car at time $t$.

Define the "rotating" spherical coordinates $F : \mathbb{R}^2\times\mathbb{R}\to\mathbb{R}^3$,
$$F((x,y),t) = \big(R\cos y\cos(\omega t + x),\ R\cos y\sin(\omega t + x),\ R\sin y\big),$$
representing what a point on the map looks like on Earth from a satellite at time $t$ (we consider
the Earth as a rotating sphere with speed $\omega$, and forget about translation around the Sun).

Consider $r : \mathbb{R}\to\mathbb{R}^3$, $r(t) = F(\sigma(t), t)$, the position of the car at
time $t$.

1. Compute the acceleration $r''(t)$ using the chain rule.
2. Assume that the acceleration is always proportional to the radial vector $r(t)$, i.e.
   $r''(t) = \lambda(t)\,r(t)$ for some scalar function $\lambda(t)$. Show that $a$ and $b$ satisfy
   $$b'' + \sin b\cos b\,(\omega+a')^2 = 0, \qquad \cos b\,a'' - 2\sin b\,(\omega+a')b' = 0.$$
   Equivalently, away from the poles ($\cos b \neq 0$),
   $$a'' - 2\tan b\,(\omega+a')\,b' = 0.$$

---

## Optimization

*(Corsin p. 2)*

- **Local minimum** of $f : U \subseteq \mathbb{R}^n \to \mathbb{R}$: $f$ has a **local minimum**
  ("lokales Minimum") at $x_0 \in U$ if
  $$\exists\,\varepsilon > 0 \text{ such that } \forall x \in B_\varepsilon(x_0)\cap U : f(x) \geq f(x_0).$$
- **Local maxima** are defined analogously with $f(x) \leq f(x_0)$.
- **Strict** min/max $\iff f(x) > f(x_0)$ / $f(x) < f(x_0)$.
- A **critical point** ("kritischer Punkt") of $f \in C^1(U,\mathbb{R})$, $U \subseteq \mathbb{R}^n$
  open, is a point $x_0 \in U$ where $\nabla f(x_0) = 0$.

**Proposition.** *Local extremum $\Rightarrow$ critical point.* If $f \in C^1(U,\mathbb{R})$ and
$x_0 \in \operatorname{int}(U)$ is a local extremum, then $\nabla f(x_0) = 0$.

**Intuition.** *(Corsin p. 2)*

> **[FIG-W05-01]** *(Corsin p. 2)* A blue paraboloid-like surface $f(x,y)$ over an $xy$-grid;
> purple level sets projected onto the plane, an orange gradient arrow, a green marked minimum,
> and a red "steepest ascent" arrow on the surface. → TikZ 3D surface + contours.
> *(Reference asset: `Toby Lane/geogebra/gradient_contour.ggb`.)*

$$\langle\nabla f(x_0), v\rangle = 0 \iff \nabla f(x_0) \perp v,$$
$$\text{and this for all } v \in \mathbb{R}^2 \iff \nabla f(x_0) = 0.$$

## Lagrange multipliers

*(Corsin p. 3)*

Suppose we want to find the hottest place on the surface of the earth. In theory, temperature is
defined everywhere, giving some function
$$T \in C^\infty(\mathbb{R}^3, (0,\infty)) \qquad \text{(absolute zero is not attainable ☺)}$$

If we model the earth as $S^2 := \{x \in \mathbb{R}^3 : |x| = 1\}$, then we want to find the local
maxima of $T|_{S^2}$, which **are not necessarily critical points of $T$!**

> **[FIG-W05-02]** *(Corsin p. 3)* A blue sphere $S^2$. At a point $q$ near the top, a red arrow
> $\nabla T(q)$ points radially outward, annotated "local extremum of $T|_{S^2}$". At a point $p$
> lower down, an orange arrow $\nabla T(p)$ points obliquely, annotated: "has a component pointing
> along the tangent, **not** a local extremum of $T|_{S^2}$, since $T$ increases along a direction
> on $S^2$." → TikZ 3D sphere with two gradient arrows.

So $T|_{S^2}$ has a local extremum if it is **perpendicular to the surface** $S^2$. Note that
$S^2$ is the **level set** $g(x) = 0$ for $g(x) = |x| - 1$, or $S^2 = g^{-1}\{0\}$.

**Note.** $\nabla g(x) = \dfrac{x}{|x|}$ is perpendicular to $S^2$. In general, **the gradient is
perpendicular to the level sets.**

*(Corsin p. 4)* This intuition is made rigorous in the following.

**Proposition (constrained optimization problems).** Suppose $f : U \to \mathbb{R}$,
$g : U \to \mathbb{R}^k$ are $C^1$ and $U \subseteq \mathbb{R}^n$ is open, and write
$g = (g_1,\dots,g_k)$. If $f|_{g^{-1}\{0\}}$ has a local extremum at $x_0 \in g^{-1}\{0\}$, then
$$\{\nabla f(x_0), \nabla g_1(x_0), \dots, \nabla g_k(x_0)\} \text{ are linearly dependent.}$$

For $k = 1$, this corresponds to our intuition above of $\nabla f(x_0)$ **parallel to**
$\nabla g(x_0)$.

*In practice*, we assume $(\nabla g_1, \dots, \nabla g_k)$ nowhere linearly dependent, since
otherwise $\lambda_0 = 0$ is possible, which does not give us anything. We then eliminate the
perpendicular part of $\nabla f(x_0)$ by forming the **Lagrangian** ("Lagrange-Funktion"):
$$
\begin{aligned}
L : U \times \mathbb{R}^k &\to \mathbb{R} \\
(x,\lambda) &\mapsto f(x) - \lambda\cdot g(x) = f(x) - \lambda_1g_1(x) - \dots - \lambda_kg_k(x)
\end{aligned}
$$
We then find local extrema by forcing $\nabla L(x,\lambda) = 0$, i.e.
$$\underbrace{\frac{\partial L}{\partial x_i} = 0 \ \ \forall i = 1,\dots,n}_{\nabla f(x) - \lambda\cdot\nabla g(x) = 0} \qquad \text{and} \qquad \underbrace{\frac{\partial L}{\partial \lambda_j} = 0 \ \ \forall j = 1,\dots,k}_{g_j(x) = 0}$$

### Exercise *(Corsin p. 5)*

Find the local extrema of
$$f : K \to \mathbb{R}, \quad (x,y,z) \mapsto xyz, \qquad K = \{(x,y,z) \in \mathbb{R}^3 : x^2+y^2+z^2 \leq 1\}.$$

### Solution *(Corsin pp. 5–6)*

We first find the **interior critical points**:
$$\nabla f(x,y,z) = (yz,\ xz,\ xy) \overset{!}{=} 0 \implies x = y = 0 \ \text{ or } \ x = z = 0 \ \text{ or } \ y = z = 0.$$

Then we look for local extrema **on the boundary**. We need to find the local extrema of
$f|_{g^{-1}\{0\}}$, where $g : \mathbb{R}^3\to\mathbb{R}$ is given by $g(x) = |x|^2 - 1$.

> ⚠️ **Check:** Corsin writes $g(x) = |x| - 1$ here, but the Lagrangian on the next line uses
> $x^2+y^2+z^2-1$, i.e. $|x|^2-1$. Both cut out the same sphere; the squared version is the one
> actually differentiated, so it is used throughout. See `OQ-12`.

The Lagrangian is
$$L(x,y,z,\lambda) = f(x,y,z) - \lambda g(x,y,z) = xyz - \lambda(x^2+y^2+z^2-1),$$
giving the system of equations
$$
\begin{aligned}
\frac{\partial L}{\partial x} &= yz - 2\lambda x = 0, & \frac{\partial L}{\partial \lambda} &= 1 - (x^2+y^2+z^2) = 0. \\
\frac{\partial L}{\partial y} &= xz - 2\lambda y = 0, \\
\frac{\partial L}{\partial z} &= xy - 2\lambda z = 0,
\end{aligned}
$$

*(Corsin p. 6)* We then have
$$2\lambda = \frac{yz}{x} = \frac{xz}{y} = \frac{xy}{z} \tag{$*$}$$
$$\implies \underbrace{y^2z^2 = x^2z^2}_{y^2 = x^2} = \underbrace{x^2y^2}_{y^2 = z^2} \qquad \text{(if any coordinate is 0, so are the others)}$$
$$\implies x^2 = y^2 = z^2.$$
Then $x^2+y^2+z^2 = 1 \implies 3x^2 = 1 \implies x = \pm\frac{1}{\sqrt{3}}$, giving **8 solutions**:
$$(x,y,z) \in \left\{\tfrac{1}{\sqrt{3}}(\alpha,\beta,\gamma) : \alpha,\beta,\gamma \in \{\pm 1\}\right\}$$
plus the solutions $\{(x_1,x_2,x_3) \in K : x_i = x_j = 0,\ i \neq j\}$.

> **[FIG-W05-03]** *(Corsin p. 6)* A blue sphere with the three green coordinate axes through the
> centre; the eight points $\tfrac{1}{\sqrt3}(\pm1,\pm1,\pm1)$ marked in red, connected by red
> dotted lines forming an inscribed cube. → TikZ 3D sphere + inscribed cube.

**To justify division by $z$, $x$ or $y$ in $(*)$:** if $z = 0$, then
$-\lambda x = -\lambda y = xy = 0$, giving $x = 0$ or $y = 0$, and $\lambda = 0$, since
$x = y = z = 0$ does not satisfy $x^2+y^2+z^2 = 1$. Then, since $\lambda = 0$,
$\nabla f(x,y,z) = 0$ and we have already found that point in the first step. Similarly for
$y = 0$ or $x = 0$.

## The Hessian test

*(Corsin p. 7)*

The **Hessian** of $f \in C^2(U,\mathbb{R})$, $U \subseteq \mathbb{R}^n$, is given by
$$\mathcal{H}f(x) = (\partial_i\partial_j f)_{i,j=1,\dots,n}$$
with respect to the standard basis of $\mathbb{R}^n$. By **Schwarz's lemma**
("Satz von Schwarz"), $\mathcal{H}f(x)$ is symmetric.

**Definition (sign of a symmetric matrix).** A symmetric matrix $A \in \mathbb{R}^{n\times n}$ is:

- **positive definite** if $v^{\mathsf T}Av > 0$ for all $v \in \mathbb{R}^n\setminus\{0\}$;
- **negative definite** if $v^{\mathsf T}Av < 0$ for all $v \in \mathbb{R}^n\setminus\{0\}$;
- **indefinite** if there exist $v, u \in \mathbb{R}^n\setminus\{0\}$ such that
  $v^{\mathsf T}Av > 0$ and $u^{\mathsf T}Au < 0$;
- **degenerate** if there exists $v \in \mathbb{R}^n\setminus\{0\}$ such that $v^{\mathsf T}Av = 0$.

If $f \in C^3(U,\mathbb{R})$ has a critical point $x_0 \in \operatorname{int}(U)$, then:

- $\mathcal{H}f(x_0)$ **positive definite** $\Rightarrow$ local **min** at $x_0$;
- $\mathcal{H}f(x_0)$ **negative definite** $\Rightarrow$ local **max** at $x_0$;
- $\mathcal{H}f(x_0)$ **indefinite and not degenerate** $\Rightarrow$ **saddle point** at $x_0$.

Mnemonic *(Corsin p. 7)*: positive $= \smile \dots$ min; negative $= \frown \dots$ max;
indefinite $= $ saddle.

> ⚠️ **Check:** the regularity is stated as $C^3$; the test needs only $C^2$ (which is what the
> Hessian's definition above assumes). See `OQ-13`.

### How do I determine positive/negative definiteness?

*(Corsin p. 8)*

Let $A \in \mathbb{R}^{n\times n}$ be symmetric with eigenvalues $\lambda_1,\dots,\lambda_n$.
Note: $\det(A) = \lambda_1\cdots\lambda_n$ and $\operatorname{Tr}(A) = \lambda_1+\dots+\lambda_n$.

**For $n = 2$:**

- $\det(A) = \lambda_1\lambda_2 < 0 \implies$ **indefinite**
- $\det(A) > 0$, $\operatorname{Tr}(A) > 0 \implies$ **positive definite**
- $\det(A) > 0$, $\operatorname{Tr}(A) < 0 \implies$ **negative definite**

**For $n \geq 3$:**

- Solve the characteristic equation $\det(A - \lambda\operatorname{Id}) = 0$ for $\lambda$ and
  check all eigenvalues.

  > ⚠️ **Check:** Corsin writes "$A - \lambda\operatorname{Id} = 0$"; the determinant is missing.
  > Corrected. See `OQ-14`.

- **Hurwitz criterion** ("Hurwitz-Kriterium"): for
  $$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & \ddots & & \vdots \\ \vdots & & \ddots & \\ a_{n1} & \cdots & & a_{nn}\end{pmatrix}$$
  define the leading principal minors
  $$A_1 = \det(a_{11}), \quad A_2 = \det\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}, \quad \dots, \quad A_n = \det(A).$$
  Then *(Corsin p. 9)*:
  - $A_1 > 0$, $A_2 > 0$, $A_3 > 0$, … $\iff$ **positive definite**
  - $A_1 < 0$, $A_2 > 0$, $A_3 < 0$, … $\iff$ **negative definite**
  - **indefinite** if neither $A_1 \geq 0, A_2 \geq 0, \dots$ nor $A_1 \leq 0, A_2 \geq 0, A_3 \leq 0, \dots$

#### Examples *(Corsin p. 9)*

| Matrix | Computation | Conclusion |
|---|---|---|
| $\begin{pmatrix}2&2\\2&5\end{pmatrix}$ | $\det = 6 > 0$, $\operatorname{Tr} = 7 > 0$ | positive definite |
| $\begin{pmatrix}-4&2\\2&-4\end{pmatrix}$ | $\det = 12 > 0$, $\operatorname{Tr} = -8 < 0$ | negative definite |
| $\begin{pmatrix}4&2\\2&-4\end{pmatrix}$ | $\det = -20 < 0$ | indefinite |
| $\begin{pmatrix}-5&0&0\\0&-4&-2\\0&-2&-4\end{pmatrix}$ | $A_1 = -5 < 0$, $A_2 = 20 > 0$, $A_3 = -60 < 0$ | negative definite |
| $\begin{pmatrix}-1&0&-4\\0&2&-2\\-4&-2&22\end{pmatrix}$ | $A_1 = -1 < 0$, $A_2 = -2 < 0$, $A_3 = -72 < 0$ | indefinite |

### Exercise *(Corsin p. 10)*

Find the critical values of
$$f_\alpha : \mathbb{R}^2 \to \mathbb{R}, \qquad (x,y) \mapsto x^3 - y^3 + 3\alpha xy$$
for $\alpha \in \mathbb{R}\setminus\{0\}$ and determine min/max/saddle points.

### Solution *(Corsin pp. 10–11)*

$$
\begin{aligned}
\frac{\partial f_\alpha}{\partial x} &= 3x^2 + 3\alpha y \overset{!}{=} 0 &&\implies y = -\frac{x^2}{\alpha} \\
\frac{\partial f_\alpha}{\partial y} &= -3y^2 + 3\alpha x \overset{!}{=} 0 &&\implies -\frac{x^4}{\alpha^2} + \alpha x = 0
\end{aligned}
$$

1. $x = y = 0$
2. $x \neq 0 \implies x^3 = \alpha^3 \implies x = \alpha$, $y = -\alpha$

So we have critical points $(0,0)$ and $(\alpha, -\alpha)$.

Compute the Hessian:
$$\begin{pmatrix} \partial_x^2 f & \partial_x\partial_y f \\ \partial_x\partial_y f & \partial_y^2 f\end{pmatrix} = \begin{pmatrix} 6x & 3\alpha \\ 3\alpha & -6y \end{pmatrix} = \mathcal{H}f(x,y)$$

$$\mathcal{H}f(0,0) = \begin{pmatrix} 0 & 3\alpha \\ 3\alpha & 0\end{pmatrix}, \qquad \det = -9\alpha^2 < 0 \implies \text{indefinite}$$

$$\mathcal{H}f(\alpha,-\alpha) = \begin{pmatrix} 6\alpha & 3\alpha \\ 3\alpha & 6\alpha\end{pmatrix} = 3\alpha\begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}, \qquad \det = 27\alpha^2 > 0, \quad \operatorname{Tr} = 12\alpha$$

For $\alpha > 0$ this is positive definite; for $\alpha < 0$ it is negative definite. So:

- $(0,0) \longrightarrow$ **saddle point**
- $(\alpha,-\alpha) \longrightarrow$ **local minimum** for $\alpha > 0$; **local maximum** for $\alpha < 0$

---

## German glossary contributed by this week

| English | German |
|---|---|
| local minimum / maximum | lokales Minimum / Maximum |
| critical point | kritischer Punkt |
| level set | Niveaumenge |
| constraint | Nebenbedingung |
| Lagrange multiplier | Lagrange-Multiplikator |
| Lagrangian | Lagrange-Funktion |
| Schwarz's lemma | Satz von Schwarz |
| positive / negative definite | positiv / negativ definit |
| saddle point | Sattelpunkt |
| Hurwitz criterion | Hurwitz-Kriterium |
