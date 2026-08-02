# Week 7 — Submanifolds, Tangent & Normal Spaces

**Primary source:** `Corsin Nick/Class Notes/Week 7.pdf` (10 pp)
**Exercise sheet:** `exercises/Ex7_Analysis2_eng.pdf` (solutions: `Sol7_Analysis2_eng.pdf`)
**Lecture notes:** ch. 12 (sheet 7 cites *Section 12.2.2* for the standard submanifold examples)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **No session split.** No `Monday`/`Friday` boxes in this file.

---

## Exercise sheet 7

*Statements quoted verbatim from `exercises/Ex7_Analysis2_eng.pdf` (assigned 27 March 2026,
due 13 April 2026 — the Easter break falls in between). Attribution: Prof. Joaquim Serra, D-MATH,
ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 7.1 | **important** | "First think of a diffeomorphism $(a,b) \leftrightarrow \mathbb{R}$ and adjust it such that $(a,b) = (0,1)$." |
| 7.2 | **important** | — |
| 7.3 | **semi-important** | — |
| 7.4 | **semi-important** | — |
| 7.5 | **important** | "This is a great exercise to help with understanding of IFT" |
| 7.6 | **important** | "You will need these coordinates very often over the next weeks" |
| 7.7 | **semi-important** | "In 1), only the Möbius strip should be enough" |
| 7.8 | **semi-important** | "Do 1) and 2), the others will be in the lecture" |
| 7.9 | **semi-important** | — |

### 7.1 — Diffeomorphism *(important)*

(a) Give a diffeomorphism between $\mathbb{R}^2$ and $(0,1)\times(0,1)$.
(b) Is $f(x) = x^5$, $x \in \mathbb{R}$ a diffeomorphism of $\mathbb{R}$ to itself? Motivate
rigorously your answer.

> **Ties into the class notes:** part (b) is Corsin's answer **A1** in Week 6, p. 8 with the
> exponent changed from 3 to 5 — same phenomenon, $f^{-1}$ fails to be $C^1$ at the origin.

### 7.2 — Inverse function I *(important)*

Consider the function $F : \mathbb{R}^2\to\mathbb{R}^2$ given by $F(x,y) = (x^2y,\ xy^2)$. Show
that $F$ is locally invertible around all points $(x,y)$ such that $x \neq 0$ and $y \neq 0$.
Compute the differential of the local inverse of $F$ at the point $F(2,1)$.

### 7.3 — Implicit Function I *(semi-important)*

Sketch the zero set of the following functions $f : \mathbb{R}^2\to\mathbb{R}$:

1. $f(x,y) = x^2+y^2-1$
2. $f(x,y) = y^2(1-x) - x^3$
3. $f(x,y) = y^2 - x^2(x+1)$
4. $f(x,y) = xy(x+y-1)$
5. $f(x,y) = x^2y^2 - x^2 - y^2 + 1$

You can also use software to help you. At which points $(x_0,y_0) \in \mathbb{R}^2$ does the
Implicit Function Theorem imply that the function can be locally resolved with respect to $x$ (or
with respect to $y$, with respect to both, or possibly with respect to neither variable)? Mark
these points in your sketch.

### 7.4 — Multiple choice *(semi-important)*

Mark all and only the true statements.

(a) Let $U \subset \mathbb{R}^n$ be open and $f \in C^1(U,\mathbb{R}^n)$ such that
    $\det Jf(x) > 0$ for all $x \in U$. Then the set $f(U)$ is open.
(b) Let $U \subset \mathbb{R}^n$ be open and $f \in C^1(U,\mathbb{R}^n)$ such that
    $\det Jf(x) > 0$ for all $x \in U$. Then $f$ is injective.
(c) Is there a diffeomorphism $\phi : \mathbb{R}^2\to\mathbb{R}^2$ such that $\phi(U) = V$, with
    $U := \{x^2+y^2 < 1\} \subset \mathbb{R}^2$ and $V := \{x^2+y^2 \leq 1\}\subset\mathbb{R}^2$.
(d) **(\*)** Let $T$ be a triangle and $Q$ be a square on the plane (just the boundary, not the
    interior). Is there a diffeomorphism $\phi : \mathbb{R}^2\to\mathbb{R}^2$ such that
    $\phi(T) = Q$?

> **Ties into the class notes:** (b) is exactly Corsin's **Q2/A2** in Week 6, p. 7–8 — everywhere
> invertible differential does **not** give global injectivity ($\cos$ on
> $\mathbb{R}\setminus\pi\mathbb{Z}$).

### 7.5 — Implicit function II *(important — "a great exercise to help with understanding of IFT")*

Show that the system of equations
$$\begin{cases} xy^5 + yu^5 + zv^5 = 1, \\ x^5y + y^5u + z^5v = 1, \end{cases}$$
is solvable for the variables $u$ and $v$ in a neighborhood of the point
$(x_0,y_0,z_0,u_0,v_0) = (0,1,1,1,0)$ and determine the derivatives $D_{(0,1,1)}u$ and
$D_{(0,1,1)}v$ of the implicitly defined functions $u = u(x,y,z)$ and $v = v(x,y,z)$.

### 7.6 — Spherical coordinates *(important — "you will need these coordinates very often over the next weeks")*

The mapping $\Phi : (0,\infty)\times(0,\pi)\times(-\pi,\pi)\to\mathbb{R}^3$ defined by
$$\Phi(r,\theta,\varphi) = \begin{pmatrix} r\sin\theta\cos\varphi \\ r\sin\theta\sin\varphi \\ r\cos\theta\end{pmatrix}$$
is called **spherical coordinates**.

1. Sketch the images of $r \mapsto \Phi(r,\theta_0,\varphi_0)$,
   $\theta \mapsto \Phi(r_0,\theta,\varphi_0)$ and $\varphi \mapsto \Phi(r_0,\theta_0,\varphi)$ for
   some fixed $r_0 \in (0,\infty)$, $\theta_0 \in (0,\pi)$, $\varphi_0 \in (-\pi,\pi)$.
2. What is the image of $\Phi$?
3. Show that $\det(D_{(r,\theta,\varphi)}\Phi) = r^2\sin\theta$ holds.
4. Conclude that the mapping $\Phi$ is a diffeomorphism onto its image.

### 7.7 — Parametrized surfaces *(semi-important — "only the Möbius strip should be enough")*

In Section 12.2.2 of the lecture notes we gave several examples of important submanifolds of
$\mathbb{R}^3$ (sphere $\mathbb{S}^2$, torus $\mathbb{T}^2$, Möbius strip, catenoid), in various
representations.

1. Compute the tangent spaces and normal vectors to the torus, the Möbius strip, and the catenoid
   from their given parametrizations:

   - **Torus:**
     $$x(\phi,\theta) = (R_1+R_2\cos\theta)\cos\phi, \quad y(\phi,\theta) = (R_1+R_2\cos\theta)\sin\phi, \quad z(\phi,\theta) = R_2\sin\theta,$$
     where $\phi,\theta \in [0,2\pi)$ and $R_1 > R_2 > 0$.
   - **Möbius strip:**
     $$x(u,v) = \Big(1+\tfrac{v}{2}\cos\tfrac{u}{2}\Big)\cos u, \quad y(u,v) = \Big(1+\tfrac{v}{2}\cos\tfrac{u}{2}\Big)\sin u, \quad z(u,v) = \tfrac{v}{2}\sin\tfrac{u}{2},$$
     where $u \in [0,2\pi)$ and $v \in [-1,1]$.
   - **Catenoid:**
     $$x(u,v) = \cosh(v)\cos(u), \quad y(u,v) = \cosh(v)\sin(u), \quad z(u,v) = v,$$
     where $u \in [0,2\pi)$ and $v \in \mathbb{R}$.

2. What happens to the normal vector to the Möbius strip as $u \to 2\pi$? Interpret your result
   geometrically.
3. Give a parametrisation for a general ellipsoid, defined as
   $\left\{(x,y,z)\in\mathbb{R}^3 : \tfrac{x^2}{a^2}+\tfrac{y^2}{b^2}+\tfrac{z^2}{c^2} = 1\right\}$,
   where $a,b,c > 0$.

> Part 2 is the first appearance of **non-orientability** in the course — it returns in Week 12.

### 7.8 — Graphs as parametrized surfaces *(semi-important — "do 1) and 2)")*

Let $f(x,y) : D \subset \mathbb{R}^2\to\mathbb{R}$ be a $C^1$ function, and let
$M \subset \mathbb{R}^3$ denote its graph.

1. Define a parametrization $\phi : D \to \mathbb{R}^3$ of $M$ explicitly.
2. Let $p \in M$, $p_3 = f(p_1,p_2)$. Compute a basis of the tangent space
   $T_pM \subset \mathbb{R}^3$ of $M$ at $p$ in terms of $f$.
3. Give an equation for $T_pM$.
4. Compute an expression for the normal vector $N_pM$ of $M$ at $p$, with positive vertical
   orientation, in terms of $f$. How does this relate to $\nabla f$? Can you interpret this
   geometrically?

> **Ties into the class notes:** Corsin works exactly this out for the upper hemisphere on p. 8.

### 7.9 — The IFT is only a sufficient condition *(semi-important)*

We consider the function $f(x,y) = y^2(1-x) - x^3$ from Exercise 7.3.2 in more detail.

> ⚠️ **Check:** the sheet says "from Exercise 6.3.3"; the function $y^2(1-x)-x^3$ is item **2** of
> Exercise **7.3** on this same sheet. Treated as a typo in the official sheet. See `OQ-16`.

1. Show that we cannot conclude from the implicit function theorem that $f$ is solvable for $x$ in
   a neighborhood of $(0,0)$.
2. Show, however, that the equation $f(x,y) = 0$ can be uniquely solved for $x$ everywhere.
   *Hint: analyze the mapping $x \mapsto \frac{x^3}{1-x}$ on a suitable domain.*
3. Denote by $Y(x) > 0$ the function such that $f(x,Y(x)) = 0$ around $x = 1/2$. Compute
   $Y''(1/2)$. *Hint: derive twice with respect to $x$ the identity $f(x,Y(x)) = 0$ and evaluate
   it at $x = 1/2$.*

---

## Submanifolds

*(Corsin p. 2)*

> **Recall.** A **$C^k$-diffeomorphism** is a $C^k$ bijective function whose inverse is also $C^k$.

**Definition.** $M^m \subseteq \mathbb{R}^n$ is a **$C^k$, $m$-dimensional submanifold**
("Untermannigfaltigkeit") of $\mathbb{R}^n$ if for **any** point $p \in M$ there are

- an open neighbourhood $U \subseteq \mathbb{R}^n$ of $p$, an open neighbourhood
  $V \subseteq \mathbb{R}^n$ of $0$,
- a $C^k$-diffeomorphism $\Phi : U \to V$ with $\Phi(p) = 0$ (a **submanifold chart**)

such that
$$\Phi(U\cap M) = \big(\mathbb{R}^m\times\{0\}\big)\cap V = \{x \in V : x_{m+1} = \dots = x_n = 0\}.$$

> **[FIG-W07-01]** *(Corsin p. 2)* Left panel: a blue wavy curve $M$ on axes with an orange dotted
> disc $U$ around a point $p$, and the arc $U\cap M$ marked purple. A green arrow $\Phi$ to the
> right panel: axes $\mathbb{R}^m$ (horizontal) / $\mathbb{R}^{n-m}$ (vertical) with a purple
> dotted blob $V = \Phi(U)$ straddling the horizontal axis, the image being the straight blue
> segment on that axis. → TikZ, two panels + arrow.

Finding such a chart can be very difficult. It is often easier to use one of the following
representations.

### Regular value theorem

*(Corsin p. 3)*

**Theorem (regular value theorem).** Suppose $U \subseteq \mathbb{R}^n$ open,
$F : U \to \mathbb{R}^\ell$ is $C^k$ and $y \in F(U)$. If
$$DF_x : \mathbb{R}^n \to \mathbb{R}^\ell$$
is **surjective** (i.e. $JF(x)$ has full rank) for all
$x \in F^{-1}\{y\} = \{\bar x \in U : F(\bar x) = y\}$, then $F^{-1}\{y\}$ is a $C^k$ submanifold
with dimension $n - \ell$.

#### Example *(Corsin p. 3)*

$$F : \mathbb{R}^2\to\mathbb{R}, \qquad (x,y) \mapsto x^2+y^2$$
$$JF(x,y) = (2x,\ 2y)$$
has full rank if $x \neq 0$ or $y \neq 0$, i.e. for all $(x,y) \in \mathbb{R}^2\setminus\{0\}$.
For $R > 0$, $(0,0) \notin F^{-1}\{R^2\}$, therefore
$$F^{-1}\{R^2\} = \{(x,y)\in\mathbb{R}^2 : x^2+y^2 = R^2\}$$
is a submanifold of dimension $2 - 1 = 1$.

> **[FIG-W07-02]** *(Corsin p. 3)* A purple circle of radius $R$ centred at the origin on $x$/$y$
> axes, with a red radius arrow labelled $R$. → TikZ 2D sketch.

Similarly, $\{x \in \mathbb{R}^n : |x|^2 = R^2\}$ is a submanifold of dimension $n-1$ for
$n \geq 1$ (the $n$-sphere of radius $R$).

### Recall: the Lagrangian and optimization

*(Corsin p. 4)*

We build the Lagrangian $L = f - \sum_{i=1}^{k}\lambda_ig_i$ when optimizing $f|_M$ for
$f \in C^1(\mathbb{R}^n,\mathbb{R})$, where
$$g_1,\dots,g_k : U \to \mathbb{R}, \qquad M := \{x \in \mathbb{R}^n : g_1(x) = \dots = g_k(x) = 0\}$$
and $(\nabla g_1,\dots,\nabla g_k)$ linearly independent for all $x \in M$ — ergo, $k \leq n$.

This means that for
$$g : \mathbb{R}^n\to\mathbb{R}^k, \qquad x \mapsto (g_1(x),\dots,g_k(x))$$
the Jacobian
$$Jg(x) = \begin{pmatrix} \text{---} & \nabla g_1 & \text{---} \\ & \vdots & \\ \text{---} & \nabla g_k & \text{---}\end{pmatrix}$$
has **full rank!** Therefore, $M = g^{-1}\{0\}$ is an $(n-k)$-submanifold by the regular value
theorem!

### Local parametrization

*(Corsin p. 5)*

**Theorem (local parametrization).** Let $M \subseteq \mathbb{R}^n$. If for all $p \in M$ there
exist an open neighbourhood $V$ of $p$, an open set $U \subseteq \mathbb{R}^m$ and a $C^k$ map
$f : U \to V\cap M$ such that

- $Df_x : \mathbb{R}^m\to\mathbb{R}^n$ is **injective** for all $x \in U$,
- $f$ is a **homeomorphism** (bijective, continuous, $f^{-1}$ continuous),

then $M$ is a $C^k$ submanifold with $\dim = m$.

#### Example: parabola *(Corsin p. 5)*

Let $P = \{(x,t) \in \mathbb{R}^n\times\mathbb{R} : t = |x|^2\}$ (the $n$-parabola). We could use
the regular value theorem, but let us not do that; instead, for
$$f : \mathbb{R}^n\to\mathbb{R}^n\times\mathbb{R}, \qquad x \mapsto (x, |x|^2):$$

1. $Jf(x) = \begin{pmatrix}\operatorname{Id}_{n\times n} \\ \hline 2x\end{pmatrix}$ has full rank
   (injective).
2. $f$ is bijective and continuous with inverse
   $\pi : f(U) \to \mathbb{R}^n$, $(x,t) \mapsto x$ (canonical projection), also continuous.
3. $f(U) = P$.

So $P$ is an $n$-dimensional submanifold.

> **[FIG-W07-03]** *(Corsin p. 5)* A blue upward parabola on $x$/$t$ axes. → TikZ plot.

*(Corsin p. 6)* So the **graphical representation** is a common (and equivalent) special case of a
local parametrization.

### Application: an alternative optimization technique

*(Corsin p. 6)*

$$f : \mathbb{R}^2\to\mathbb{R}, \qquad (x,y) \mapsto 2x^2+y^2-x$$

Find the extrema of $f|_{S^1}$ **without Lagrange multipliers!**, where
$S^1 = \{(x,y)\in\mathbb{R}^2 : x^2+y^2 = 1\}$.

We parametrize $S^1$ by
$$\begin{pmatrix}x(\theta) \\ y(\theta)\end{pmatrix} = \begin{pmatrix}\cos\theta \\ \sin\theta\end{pmatrix}.$$
Then:
$$f(\theta) = f(x(\theta), y(\theta)) = 2\cos^2\theta + \sin^2\theta - \cos\theta = \cos^2\theta - \cos\theta + 1$$
$$f'(\theta) = -2\cos\theta\sin\theta + \sin\theta \overset{!}{=} 0$$

1. $\sin\theta = 0 \implies \theta_1 \in \{0, \pi\}$
2. $\sin\theta \neq 0 \implies -2\cos\theta + 1 = 0 \implies \cos\theta = \tfrac{1}{2}
   \implies \theta_2 \in \{\tfrac{\pi}{3}, \tfrac{5\pi}{3}\}$

So the extrema are at:

1. $(\cos\theta_1, \sin\theta_1) = (\pm 1, 0)$
2. $(\cos\theta_2, \sin\theta_2) = \left(\tfrac{1}{2}, \pm\tfrac{\sqrt{3}}{2}\right)$

> This is problem **6.9(a)** from the previous sheet, solved by a different route — worth
> cross-referencing in the typeset version.

## Tangent and normal space

*(Corsin p. 7)*

Suppose $M^m \subseteq \mathbb{R}^n$ is a submanifold and $f : U \to f(U) \subseteq M$ a local
parametrization around some point $p \in f(U)$ with $f(q) = p$. The $n\times m$ matrix
$$Jf(q) = \left(\frac{\partial f}{\partial q_1}\ \Big|\ \cdots\ \Big|\ \frac{\partial f}{\partial q_m}\right)$$
has full rank, that is, the column vectors $\partial_i f(q)$ are **linearly independent**. They
form a basis of $T_pM$.

**Definition (tangent space).** For $M$, $f$ as above, the **tangent space** ("Tangentialraum") of
$M$ at $p \in M$ is given by
$$T_pM := \operatorname{span}\{\partial_1f(q),\dots,\partial_mf(q)\} = Df_q(\mathbb{R}^m).$$
It is independent of the choice of $f$.

> **[FIG-W07-04]** *(Corsin p. 7)* A blue curvilinear-grid patch (a surface drawn as a mesh) with
> two green tangent arrows $\frac{\partial f}{\partial x_1}$ and $\frac{\partial f}{\partial x_2}$
> from a common point. → TikZ surface mesh + two vectors.

#### Example *(Corsin p. 8)*

We parametrize the upper hemisphere
$$S^2_+ = \{(x,y,z)\in\mathbb{R}^3 : x^2+y^2+z^2 = 1,\ z > 0\}$$
graphically, i.e.
$$f(x,y) = \begin{pmatrix} x \\ y \\ \sqrt{1-x^2-y^2}\end{pmatrix}.$$
Then we determine $T_{e_3}S^2_+$, where $e_3 = (0,0,1)$:
$$\left.\frac{\partial f}{\partial x}\right|_{x=0} = \left.\begin{pmatrix} 1 \\ 0 \\ \frac{-x}{\sqrt{1-x^2-y^2}}\end{pmatrix}\right|_{x=0} = \begin{pmatrix}1\\0\\0\end{pmatrix} = e_1$$
$$\left.\frac{\partial f}{\partial y}\right|_{y=0} = \begin{pmatrix}0\\1\\0\end{pmatrix} = e_2$$
So
$$T_{e_3}S^2_+ = T_{e_3}S^2 = \operatorname{span}\{e_1,e_2\} = \mathbb{R}^2\times\{0\}.$$

> **[FIG-W07-05]** *(Corsin p. 8)* A blue sphere with a green tangent plane $T_{e_3}S^2$ resting
> on the north pole. → TikZ 3D sphere + plane.

### Why the gradients of an implicit representation are normal

*(Corsin p. 9)*

Suppose $F : U \subseteq \mathbb{R}^n \to \mathbb{R}^{n-m}$ is an **implicit representation** of
$M^m = F^{-1}\{0\}$ (regular value theorem) and $f : V \subseteq \mathbb{R}^m \to M$ is a local
parametrization, $M$ a submanifold. Then, by definition:

1. $JF(x) = \begin{pmatrix}\text{---} & \nabla F_1(x) & \text{---} \\ & \vdots & \\ \text{---} & \nabla F_{n-m}(x) & \text{---}\end{pmatrix}$
   has full rank, i.e. $\{\nabla F_i(x)\}_{i=1,\dots,n-m}$ are linearly independent.
2. $T_{f(q)}M = \operatorname{span}\{\partial_if(q)\}$ as discussed.
3. $F(f(x)) = 0$ for all $x \in V$, since $f(x) \in M = F^{-1}\{0\}$.

From (3), it follows that
$$J(F\circ f)(q) = JF(f(q))\cdot Jf(q) = \begin{pmatrix}\nabla F_1(f(q)) \\ \vdots \\ \nabla F_{n-m}(f(q))\end{pmatrix}\left(\frac{\partial f}{\partial q_1}\ \Big|\ \cdots\ \Big|\ \frac{\partial f}{\partial q_m}\right) = 0 \quad (!!!)$$

Now note that
$$\big(JF(f(q))\cdot Jf(q)\big)_{ij} = \langle \nabla F_i(f(q)),\ \partial_jf(q)\rangle = 0 \qquad \forall i = 1,\dots,n-m,\ j = 1,\dots,m.$$
So $\nabla F_i(f(q))$ are **perpendicular**, that is, **normal**, to $T_{f(q)}M$. Since by (1) we
have $n-m$ linearly independent vectors to the $m$-dimensional plane $T_{f(q)}M$, we can define:

**Definition (normal space).** *(Corsin p. 10)* Let $M^m \subseteq \mathbb{R}^n$ be a submanifold
and $F : U \to \mathbb{R}^{n-m}$ an implicit representation, $M = F^{-1}\{0\}$. Then the
**normal space** ("Normalenraum") of $M$ at $p \in M$ is
$$N_pM := \operatorname{span}\{\nabla F_1(p), \dots, \nabla F_{n-m}(p)\}.$$

#### Example *(Corsin p. 10)*

We represent $S^2$ implicitly:
$$S^2 = F^{-1}\{1\} = \{(x,y,z)\in\mathbb{R}^3 : F(x,y,z) = 1\}, \qquad F(x,y,z) = x^2+y^2+z^2.$$
We determine $N_{e_3}S^2$:
$$\nabla F(0,0,1) = (2x,\ 2y,\ 2z)\big|_{(x,y,z) = (0,0,1)} = 2e_3.$$
So
$$N_{e_3}S^2 = \operatorname{span}\{e_3\} = \{0\}\times\mathbb{R}.$$

> **[FIG-W07-06]** *(Corsin p. 10)* A blue sphere with a vertical orange line through the poles,
> labelled $N_{e_3}S^2$. → TikZ 3D sphere + axis line.

> **Note on the level.** The definition above uses the level set $F^{-1}\{0\}$; the example uses
> $F^{-1}\{1\}$. Both are covered by the regular value theorem (any regular value works), and the
> gradient argument is unchanged. Worth a one-line remark in the typeset version rather than a
> correction.

---

## German glossary contributed by this week

| English | German |
|---|---|
| submanifold | Untermannigfaltigkeit |
| chart | Karte |
| regular value theorem | Satz vom regulären Wert |
| parametrization | Parametrisierung |
| tangent space | Tangentialraum |
| normal space | Normalenraum |
| spherical coordinates | Kugelkoordinaten |
| surface | Fläche |
