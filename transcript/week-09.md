# Week 9 — Determinants and Volume, the Gram Determinant, $d$-Volume

**Primary source:** `Corsin Nick/Class Notes/Week 9.pdf` (8 pp)
**Exercise sheet:** `exercises/Ex9_Analysis2_eng.pdf` (solutions: `Sol9_Analysis2_eng.pdf`)
**Lecture notes:** ch. 13 (Corsin pastes *Definition 13.68* on p. 5)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **No session split.** No `Monday`/`Friday` boxes in this file.

---

## Exercise sheet 9

*Statements quoted verbatim from `exercises/Ex9_Analysis2_eng.pdf` (assigned 20 April 2026,
due 27 April 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 9.1 | **important** | Gives the coordinate formula, see below |
| 9.2 | **important** | "You can parametrize the triangle in 2) as $D = \{(x,y)\in\mathbb{R}^2 : 0 \leq x \leq y \leq \pi\}$" |
| 9.3 | **semi-important** | — |
| 9.4 | **semi-important** | — |
| 9.5 | **optional** | — |
| 9.6 | **semi-important** | "This may become important in later courses. $\langle\cdot,\cdot\rangle$ is the standard inner product." |
| 9.7 | **optional** | — |

Corsin's coordinate hint for 9.1, as written:
$$\begin{pmatrix}x\\y\\z\end{pmatrix} = \begin{pmatrix}r\sin\theta\cos\varphi\\ r\sin\theta\sin\varphi\\ r\cos\theta\end{pmatrix}, \qquad (r,\theta,\varphi) \in (0,\infty)\times\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)\times(0,2\pi)$$

> ⚠️ **Check:** he labels these **cylindrical** coordinates, but the formula is **spherical**
> (cylindrical would be $(r\cos\varphi,\ r\sin\varphi,\ z)$). The official hint on the sheet does
> say "use cylindrical coordinates". Either the label or the formula is wrong; the formula is the
> more useful of the two here, so it is kept and relabelled *spherical*, with the discrepancy
> flagged. Note also that the standard polar-angle range is $\theta \in (0,\pi)$, not
> $(-\tfrac\pi2,\tfrac\pi2)$. See `OQ-20`.

### 9.1 — Volume *(important)*

Calculate the volume of the region $B \subset \mathbb{R}^3$ enclosed by the surfaces
$x^2+y^2+z^2 = 8$ and $2z = x^2+y^2$. *Official hint: use cylindrical coordinates.*

### 9.2 — Multiple integrals *(important)*

1. Let $D = [0,2]\times[0,1]$. Calculate $\displaystyle\iint_D (x^3+3x^2y+y^3)\,dx\,dy$.
2. Let $D \subset \mathbb{R}^2$ be the interior of the triangle with vertices $(0,0)$, $(0,\pi)$,
   and $(\pi,\pi)$. Calculate $\displaystyle\iint_D x\cos(x+y)\,dx\,dy$.
3. Let $D = \{(x,y)\in\mathbb{R}^2 \mid x > 1,\ y > 1,\ x+y < 3\}$. Calculate
   $\displaystyle\iint_D \frac{1}{(x+y)^3}\,dx\,dy$.

### 9.3 — Fubini theorem *(semi-important)*

Compute the integrals
$$\int_0^{\sqrt\pi}\int_x^{\sqrt\pi}\sin(y^2)\,dy\,dx, \qquad \int_{-1}^{1}\int_{|y|}^{1}(x+y)^2\,dx\,dy.$$

### 9.4 — Counterexample to Fubini *(semi-important)*

Let $f : [0,\infty)^2\to\mathbb{R}$, defined by
$$f(x) = \begin{cases} e^{y-x} & x > y \geq 0, \\ -e^{x-y}, & 0 \leq x \leq y.\end{cases}$$
Compute the iterated integrals
$$\int_0^\infty\left\{\int_0^\infty f(x,y)\,dx\right\}dy, \qquad \int_0^\infty\left\{\int_0^\infty f(x,y)\,dy\right\}dx,$$
and show that they have different values. Explain why this does not contradict Fubini's theorem.

### 9.5 — Volume of the cone over a set *(optional)*

Let $\Omega \subset \mathbb{R}^n$ be a bounded measurable set, $n \geq 1$. Consider the
"cone over $\Omega$"
$$C\Omega := \{(x,t)\in\mathbb{R}^n\times\mathbb{R} : 0 \leq t \leq 1,\ x \in (1-t)\Omega\}.$$
Using Fubini's theorem and homogeneity of $\mu_n$ show that
$$\mu_{n+1}(C\Omega) = \frac{\mu_n(\Omega)}{n+1}.$$
Use this result to compute the $n$-volume of the $n$-simplex:
$$\mu_n(T_n) := \mu_n\big(\{a_1e_1+\dots+a_ne_n : 0 \leq a_i \leq 1,\ a_1+\dots+a_n \leq 1\}\big) = \frac{1}{n!},$$
where $e_1,\dots,e_n$ denotes an orthonormal frame of $\mathbb{R}^n$.
*Official hint: show $(n+1)T_{n+1} = T_n$.*

### 9.6 — Gaussian integrals *(semi-important — "may become important in later courses")*

Let $n \in \mathbb{N}$ and $A \in \operatorname{Mat}_{n,n}(\mathbb{R})$ be a symmetric positive
definite matrix. Show that
$$\int_{\mathbb{R}^n} e^{-\langle Ax,x\rangle}\,dx = \frac{\pi^{n/2}}{\sqrt{\det(A)}}.$$
*Official hint: start with the case where $A$ is a diagonal matrix, then use the spectral theorem
for the general case. You can also use that $\int_{\mathbb{R}}\exp(-x^2)\,dx = \sqrt\pi$.*

### 9.7 — Layer-cake formula **(\*)** *(optional)*

Let $f : \mathbb{R}^n\to[0,\infty)$ be a continuous function which vanishes identically outside a
compact set, and let $p \geq 1$. Using Fubini's theorem show the **layer-cake formula**
$$\int_{\mathbb{R}} f(x)^p\,dx = p\int_0^\infty t^{p-1}\mu_n(\{x\in\mathbb{R}^n : f(x) > t\})\,dt.$$
Find a similar formula for the integral of
$$\int_{\mathbb{R}}\Phi(f(x))\,dx = \int_0^\infty \dots\ \mu_n(\{x\in\mathbb{R}^n : f(x) > t\})\,dt,$$
where $\Phi \in C^1(\mathbb{R})$ is any function such that $\Phi(0) = 0$.
*Official hint: $f(x) = \int_0^{f(x)}dt$.*

---

## Length, area, and volume

*(Corsin p. 2)*

The relationship between the **determinant** and **volume** is a key concept in this part of the
lecture. We want to illustrate the special case of $\mathbb{R}^2$.

Let $x, y \in \mathbb{R}^2$ be vectors. What is the area of the parallelogram $(0, x, x+y, y)$?
Assume without loss of generality $x = x_1e_1$.

> **[FIG-W09-01]** *(Corsin p. 2)* Parallelogram on $e_1$/$e_2$ axes: blue base vector
> $x = x_1e_1$ along the horizontal axis, orange vector $y$, green dashed drop-lines marking $y_1$
> and $y_2$, purple dotted lines completing the parallelogram. → TikZ 2D sketch.

The area is given by
$$A = |x_1y_2| = \left|\det\begin{pmatrix}x_1 & y_1 \\ 0 & y_2\end{pmatrix}\right|.$$
And for any rotation of $x, y$ by $R \in O(2)$:
$$A = \big|\det(Rx \mid Ry)\big| = \big|\det(R)\det(x\mid y)\big| = \big|\det(x\mid y)\big|.$$
So the "without loss of generality" above was justified.

## The Gram determinant

*(Corsin p. 3)*

A key realization is that for $M \in \operatorname{Mat}_{n\times n}(\mathbb{R})$:
$$|\det(M)| = \sqrt{\det(M)\det(M)} = \sqrt{\det(M^{\mathsf T})\det(M)} = \sqrt{\det(M^{\mathsf T}M)},$$
the **Gram determinant** ("Gramsche Determinante") of $M$. So the volume of an $n$-parallelotope in
$\mathbb{R}^n$ is given by the Gram determinant, in analogy to our previous discussion of the
determinant.

But note that the expression $\sqrt{\det(M^{\mathsf T}M)}$ makes sense for
$M \in \operatorname{Mat}_{n\times m}(\mathbb{R})$, while $\det(M)$ does not. We postulate that:

> For $m$ $n$-dimensional vectors $v_1,\dots,v_m \in \mathbb{R}^n$, the **area / length / volume**
> of the parallelotope spanned by them is given by
> $$\sqrt{\det\big(\langle v_i, v_j\rangle\big)} = \sqrt{\det(V^{\mathsf T}V)}$$
> where $V = (v_1 \mid v_2 \mid \cdots \mid v_m) \in \operatorname{Mat}_{n\times m}(\mathbb{R})$.

### Examples *(Corsin pp. 3–4)*

**For $m = 1$** (length), we have
$$\sqrt{\det(v_1^{\mathsf T}v_1)} = \sqrt{\langle v_1, v_1\rangle} = \|v_1\|.$$

**For $m = 2$, $n = 3$** (area), we hope that the Gram determinant of
$$M = \begin{pmatrix}x_1 & y_1 \\ x_2 & y_2 \\ x_3 & y_3\end{pmatrix}$$
gives us the area of the parallelogram spanned by $x$ and $y$ in $\mathbb{R}^3$. If $\theta$ is
the angle between $x$ and $y$, this should be
$$A = \|x\|\,\|y\|\,|\sin\theta|.$$
And indeed:
$$
\begin{aligned}
\sqrt{\det(M^{\mathsf T}M)} &= \sqrt{\det\begin{pmatrix}\langle x,x\rangle & \langle x,y\rangle \\ \langle x,y\rangle & \langle y,y\rangle\end{pmatrix}} \\
&= \sqrt{\langle x,x\rangle\langle y,y\rangle - \langle x,y\rangle^2} \\
&= \sqrt{\|x\|^2\|y\|^2 - \|x\|^2\|y\|^2\cos^2\theta} \\
&= \|x\|\,\|y\|\,|\sin\theta| \qquad (= |x \times y|)
\end{aligned}
$$

> **[FIG-W09-02]** *(Corsin p. 4)* A 3D parallelogram: blue vector $x$ and orange vector $y$ from
> the origin with the angle $\theta$ marked green, a red dashed height segment labelled
> $\|x\|\sin\theta$, and blue/orange/purple dotted lines completing the parallelogram in space.
> → TikZ 3D sketch.

## Volume of embedded surfaces

*(Corsin p. 5)*

> **Definition 13.68 ($d$-volume on a parametrized $d$-submanifold)** — *quoted from the official
> lecture notes, pasted into Corsin's notes on p. 5.*
>
> Let $V \subset \mathbb{R}^d$ be open, and let $\phi : V \to \mathbb{R}^n$ be a parametrized
> submanifold. Given a Jordan measurable set $E \subset V$ with $\overline{E} \subset V$, we
> define the **$d$-volume** of $\phi(E)$ by
> $$\operatorname{vol}_d(\phi(E)) := \int_E \sqrt{\det\big(D\phi(x)^{\mathsf T}D\phi(x)\big)}\,dx.$$

Here the Gram determinant in the integrand is the volume of the parallelotope spanned by the
vectors $\partial_1\phi(x), \partial_2\phi(x), \dots, \partial_d\phi(x)$, which by assumption (see
parametrized submanifold) are **linearly independent** (i.e. $D\phi(x)$ has full rank), so the
volume is strictly positive.

> **[FIG-W09-03]** *(Corsin p. 5)* A black curved surface sketch; from a point $\phi(x)$ two green
> tangent vectors $\partial_1\phi(x)$, $\partial_2\phi(x)$ span a green hatched parallelogram
> labelled $\sqrt{D\phi(x)^{\mathsf T}D\phi(x)}$. → TikZ surface + spanned parallelogram.

This factor gives a measure for the **stretching** of $E$ as it is "glued" to the surface. If
$$\sqrt{D\phi(x)^{\mathsf T}D\phi(x)} \equiv 1$$
then $\phi$ is an **isometry**. A special case is the length of a curve.

### Example *(Corsin pp. 6–7)*

Compute the area of the surface
$$F = \left\{(x,y,z)\in\mathbb{R}^3 : \begin{array}{l} x^2+4y^2 < 8 \\ z = \tfrac{1}{2}(x^2+2y^2)\end{array}\right\}$$

"$z = \tfrac12(x^2+2y^2)$" means we can conveniently write $F$ as the image of the parametrization
$$\phi : A \to F, \quad (x,y) \mapsto \left(x,\ y,\ \tfrac12(x^2+2y^2)\right), \qquad A = \{(x,y)\in\mathbb{R}^2 : x^2+4y^2 < 8\}.$$

**Compute the Gram determinant:**
$$D\phi(x) = \begin{pmatrix}1 & 0 \\ 0 & 1 \\ x & 2y\end{pmatrix} \implies D\phi(x)^{\mathsf T}D\phi(x) = \begin{pmatrix}1+x^2 & 2xy \\ 2xy & 1+4y^2\end{pmatrix}$$
$$\therefore \sqrt{\det D\phi(x)^{\mathsf T}D\phi(x)} = \sqrt{(1+x^2)(1+4y^2) - 4x^2y^2} = \sqrt{1+x^2+4y^2}$$

**Compute the integral:**
$$\operatorname{vol}_2(F) = \int_A \sqrt{1+x^2+4y^2}\,dx\,dy, \qquad A = \{(x,y)\in\mathbb{R}^2 : x^2+4y^2 < 8\}$$

We should choose more convenient coordinates. Polar coordinates come to mind, but then we still
have problems, since $A$ is not radially symmetric.

*(Corsin p. 7)* We want to write $A = \Phi\big((0,R)\times(0,2\pi)\big)$ (up to a difference of
measure zero). Note that for $y = 0$, $|x| < \sqrt8 = 2\sqrt2$, and for $x = 0$, $|y| < \sqrt2$.
Choose $R = \sqrt2$ and weigh $x, y$ accordingly:
$$\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}2r\cos\theta \\ r\sin\theta\end{pmatrix} = \Phi(r,\theta)$$

**Change of variable:**
$$
\begin{aligned}
dx\,dy &= \big|\det D\Phi(r,\theta)\big|\,dr\,d\theta \\
&= \left\|\begin{matrix}2\cos\theta & -2r\sin\theta \\ \sin\theta & r\cos\theta\end{matrix}\right\|\,dr\,d\theta \\
&= 2r\,dr\,d\theta
\end{aligned}
$$
Giving:
$$
\begin{aligned}
\operatorname{vol}_2(F) &= \int_A \sqrt{1+x^2+4y^2}\,dx\,dy \\
&= \int_0^{\sqrt2}dr\int_0^{2\pi}d\theta\ 2r\sqrt{1+4r^2} \\
&= 4\pi\int_0^{\sqrt2}dr\ r\,(1+4r^2)^{1/2} \\
&= \frac{\pi}{2}\int_0^{\sqrt2}dr\ 8r\,(1+4r^2)^{1/2} \\
&= \frac{\pi}{2}\left[(1+4r^2)^{3/2}\cdot\frac{2}{3}\right]_0^{\sqrt2} \\
&= \frac{\pi}{3}(27-1) = \frac{26\pi}{3}
\end{aligned}
$$

## Length of a curve

*(Corsin p. 8)*

The **length** ("Länge") of a curve — or path — $\gamma \in C^1([a,b], \mathbb{R}^n)$ is given by
$$L(\gamma) = \int_a^b |\gamma'(t)|\,dt.$$

For a $C^0$-curve $c \in C^0([a,b],\mathbb{R}^n)$, it is defined as
$$L(c) = \sup\left\{\sum_{i=1}^{n-1}\big|c(t_{i+1}) - c(t_i)\big| : a = t_1 < \dots < t_n = b\right\}.$$

> **[FIG-W09-04]** *(Corsin p. 8)* A black wiggly curve $\operatorname{Im}(c)$ with a blue
> inscribed polygon through the sample points $c(t_1), \dots, c(t_7)$ — the polygonal
> approximation whose supremum defines the length. → TikZ freehand curve + polyline.

For a $C^1$ curve, the definitions agree. Notice that
$$|\gamma'(t)| = \sqrt{J\gamma(t)^{\mathsf T}\cdot J\gamma(t)}$$
is the Gram determinant of $J\gamma(t)$.

---

## German glossary contributed by this week

| English | German |
|---|---|
| Gram determinant | Gramsche Determinante |
| parallelotope | Parallelotop |
| volume | Volumen |
| surface area | Flächeninhalt |
| length (of a curve) | Länge |
| isometry | Isometrie |
| spherical coordinates | Kugelkoordinaten |
| cylindrical coordinates | Zylinderkoordinaten |
| polar coordinates | Polarkoordinaten |
