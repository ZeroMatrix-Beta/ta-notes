# Week 10 — Geodesics, Flux & the Divergence Theorem

**Primary source:** `Corsin Nick/Class Notes/Week 10.pdf` (12 pp)
**Exercise sheet:** `exercises/Ex10_Analysis2_eng.pdf` (solutions: `Sol10_Analysis2_eng.pdf`)
**Lecture notes:** ch. 14 (Corsin pastes *Definition 14.3* on p. 6)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> ⚠️ **Cover mismatch, again.** The cover of `Week 10.pdf` reads **"Week 9"**, but the problems
> listed on it are **10.1–10.6**. As with `Week 2.pdf` (see `OQ-01`), the file name and the
> exercise numbers agree and win. See `OQ-21`.

> **Page 2 is a repeat.** It reproduces *Length of a curve* verbatim from `Week 9.pdf`, p. 8 —
> Corsin evidently carried the last page over. Transcribed once, in Week 9; **not** duplicated
> here.

> **No session split.** No `Monday`/`Friday` boxes in this file.

---

## Exercise sheet 10

*Statements quoted verbatim from `exercises/Ex10_Analysis2_eng.pdf` (assigned 24 April 2026,
due 4 May 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 10.1 | **important** | "Use spherical coordinates with $r \equiv 1$" |
| 10.2 | **important** | Gives a full torus parametrization, see below |
| 10.3 | **important** — parts 1–4; part **5 optional** | — |
| 10.4 | **semi-important** | — |
| 10.5 | **semi-important** | — |
| 10.6 | **semi-important** | — |

**Corsin's hint for 10.2 — parametrization of the surface of a torus** *(Corsin p. 1)*:
$$x = (R + r\cos\phi)\cos\theta, \qquad y = (R + r\cos\phi)\sin\theta, \qquad z = r\sin\phi$$

> **[FIG-W10-01]** *(Corsin p. 1)* Three sketches explaining the torus parametrization: (i) a
> 3D torus with red $x$/$y$/$z$ axes through its centre; (ii) a top view — two concentric blue
> circles with the major radius $R$ at angle $\theta$ and the minor radius $r$ at angle $\phi$,
> with purple braces linking to the coordinate formulas; (iii) a side view — the tube circle of
> radius $r$ at distance $R$ from the $z$-axis. → TikZ, three panels.

### 10.1 — Spherical quadrilateral *(important)*

Calculate the area of the spherical quadrilateral $S \subset \mathbb{S}^2$ bounded by the
meridians $-\pi < \phi_1 < \phi_2 < \pi$ and parallels
$-\pi/2 < \theta_1 < \theta_2 < \pi/2$.

### 10.2 — The surface area of a torus *(important)*

Let $S = \{(x,y,0)\in\mathbb{R}^3 \mid x^2+y^2 = 4\}$ and
$T = \{x\in\mathbb{R}^3 \mid d_S(x) \leq 1\}$, where $d_S(x) = \inf\{|x-y| \mid y \in S\}$ denotes
the minimal distance from $S$ to $x \in \mathbb{R}^3$. Parameterize $\partial T$ and then
calculate the area.

### 10.3 — Solids of revolution *(important; part 5 optional)*

Given $f \in C^1((a,b))\cap C([a,b])$ such that $f \geq 0$, define the **rotational body around
the $x$-axis** as
$$\Omega := \left\{(x,y,z)\in\mathbb{R}^3 \mid a < x < b,\ \sqrt{y^2+z^2} < f(x)\right\},$$
$$\partial_{\text{side}}\Omega := \left\{(x,y,z)\in\mathbb{R}^3 \mid a < x < b,\ \sqrt{y^2+z^2} = f(x)\right\}.$$

1. Say whether $\Omega$, $\partial_{\text{side}}\Omega$ are open/closed/connected subsets of
   $\mathbb{R}^3$.
2. Show that $\operatorname{vol}_3(\Omega) = \pi\int_a^b f(x)^2\,dx$.
3. Show that
   $\operatorname{vol}_2(\partial_{\text{side}}\Omega) = 2\pi\int_a^b\sqrt{1+f'(x)^2}\,f(x)\,dx$.
   *Hint: parametrise $(x,\theta)\mapsto(x, f(x)\cos\theta, f(x)\sin\theta)$.*
4. Calculate the volume and surface area of the "improper rotational body" that arises when
   $f(x) = 1/x$, $a = 1$, $b = \infty$.
5. **(\*)** Show that $\Omega$ is a bounded $C^1$ domain (as in *Definition 14.3*) if and only if
   $$f(x) > 0 \text{ in } (a,b), \quad f'(a^+) = +\infty, \quad f'(b^-) = -\infty.$$

> Part 4 is **Gabriel's horn** — finite volume, infinite surface area.

### 10.4 — Tractrix *(semi-important)*

Consider the planar curve $\sigma : (0,\pi)\to\mathbb{R}^2$ given by
$\sigma(t) := (\sin(t),\ \cos(t) + \log\tan(t/2))$.

1. Compute the length $L(\sigma|_{[\epsilon,\pi/2]})$ and study its behaviour as
   $\epsilon \to 0^+$.
2. For any $t \in (0,\pi)$ consider the segment $I_t$ tangent to $\sigma$ in $t$ and joining
   $\sigma(t)$ and the $y$-axis. Show that the length of $I_t$ is always 1, independently of $t$.
3. **(\*)** Say whether the set $\sigma((0,\pi)) \subset \mathbb{R}^2$ is a smooth manifold.
   *Hint: how would its tangent space be around the point $\sigma(\pi/2)$?*

### 10.5 — Logarithmic spiral *(semi-important)*

Consider, for $a > 0$, $b < 0$ the planar curve $\gamma : \mathbb{R}\to\mathbb{R}^2$ given by
$$\gamma(t) := (ae^{bt}\cos t,\ ae^{bt}\sin t).$$

1. Compute $L(\gamma|_{[0,T]})$ and study its behaviour as $T \to \infty$.
2. Express in polar coordinates the set $\gamma(\mathbb{R})$, and sketch it.
3. **(\*)** Say whether $\gamma(\mathbb{R})$ is a smooth submanifold of $\mathbb{R}^2$.

### 10.6 — Moment of inertia of an ellipsoid *(semi-important)*

1. Determine the Jacobi determinant of the mapping
   $$\Phi : \{(s,t) : s > 0,\ 0 < t < 2\pi\} \to \mathbb{R}^2, \qquad (s,t)\mapsto(as\cos(t),\ bs\sin(t))$$
   in terms of the parameters $a, b > 0$.
2. Calculate the polar moment of inertia
   $J_0 = \int_B x^2+y^2\,d\!\operatorname{vol}(x,y)$ of the ellipse
   $B = \{(x,y)\in\mathbb{R}^2 : x^2/a^2 + y^2/b^2 \leq 1\}$ with semi-axes $a, b > 0$.

---

## A short introduction to geodesics

*(Corsin p. 3)* — **not exam relevant**, flagged as such by Corsin in red.

We will try to find the shortest path from $0 \in \mathbb{R}^n$ to $x \in \mathbb{R}^n$. This is,
of course, the straight line, but the essentially same calculation can be used to find the
shortest path between points on a sphere or any other submanifold!

**Idea.** Apply "optimization" to the map
$$L : A \to [0,\infty), \qquad c \mapsto L(c) = \int_0^1|c'(t)|\,dt$$
$$A = \{\gamma \in C^1([0,1],\mathbb{R}^n) : \gamma(0) = 0,\ \gamma(1) = x\}.$$

**A few identities.** *(Corsin p. 3)* For $\alpha, \beta : (0,1)\to\mathbb{R}^n$ of class $C^1$:
$$\frac{d}{dt}\langle\alpha(t),\beta(t)\rangle = \langle\alpha'(t),\beta(t)\rangle + \langle\alpha(t),\beta'(t)\rangle$$
$$\frac{d}{dt}|\alpha(t)| = \frac{1}{|\alpha(t)|}\langle\alpha(t),\alpha'(t)\rangle$$

*(Corsin p. 4)* Assume that the map $c \in C^\infty([0,1],\mathbb{R}^n)$ with $c(0) = 0$,
$c(1) = x$ and $|c'(t)| \equiv \lambda$ is the optimal path we are looking for. Let
$g \in C^\infty([0,1],\mathbb{R}^n)$ such that $g(0) = g(1) = 0$ and define, for all
$\varepsilon \in \mathbb{R}$, the family of paths
$$c_\varepsilon(t) = c(t) + \varepsilon g(t)$$
where obviously $c_0 = c$.

> **[FIG-W10-02]** *(Corsin p. 4)* Two points $0$ and $x$ joined by a straight red line labelled
> $c$, surrounded by a family of green bulging curves labelled $c_\varepsilon$.
> → TikZ, straight line + family of bowed curves.

By assumption, $c$ is a minimizer of $L$. Therefore, it is a critical point, i.e.
$$\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0} L(c_\varepsilon) \overset{!}{=} 0.$$
This, of course, requires a proof, but the idea is exactly the same as that of optimization in
$\mathbb{R}^n$.

We first compute
$$\left.\frac{\partial}{\partial\varepsilon}\right|_{\varepsilon=0}c_\varepsilon(t) = \left.\frac{\partial}{\partial\varepsilon}\right|_{\varepsilon=0}\big(c(t)+\varepsilon g(t)\big) = g(t)$$
and recall that we require $|c'| = \lambda$. Then *(Corsin p. 5)*:
$$
\begin{aligned}
\left.\frac{d}{d\varepsilon}\right|_{\varepsilon=0}L(c_\varepsilon)
&= \left.\frac{d}{d\varepsilon}\int_0^1|c_\varepsilon'(t)|\,dt\right|_{\varepsilon=0}
= \int_0^1\left.\frac{\partial}{\partial\varepsilon}|c_\varepsilon'(t)|\,dt\right|_{\varepsilon=0} \\
&= \int_0^1\left.\frac{\big\langle c_\varepsilon'(t),\ \tfrac{\partial}{\partial\varepsilon}c_\varepsilon'(t)\big\rangle}{|c_\varepsilon'(t)|}\,dt\right|_{\varepsilon=0} \\
&= \frac{1}{\underbrace{\lambda}_{=\,|c_0'|}}\int_0^1\Big\langle c_0'(t),\ \left.\tfrac{\partial}{\partial\varepsilon}\right|_{\varepsilon=0}c_\varepsilon'(t)\Big\rangle\,dt \\
&= \frac{1}{\lambda}\int_0^1\left[\frac{d}{dt}\Big\langle c_0'(t), \tfrac{\partial}{\partial\varepsilon}c_0(t)\Big\rangle - \Big\langle c_0''(t), \tfrac{\partial}{\partial\varepsilon}c_0(t)\Big\rangle\right]dt \\
&= \frac{1}{\lambda}\left[\Big\langle c'(t), g(t)\Big\rangle\Big|_0^1 - \int_0^1\big\langle c''(t), g(t)\big\rangle\,dt\right] \\
&= -\frac{1}{\lambda}\int_0^1\big\langle c''(t), g(t)\big\rangle\,dt \overset{!}{=} 0
\end{aligned}
$$
(the boundary term vanishes because $g(0) = g(1) = 0$).

Since $g(t)$ is arbitrary, it follows that
$$\left.\begin{array}{l} c''(t) \equiv 0 \\ c(0) = 0,\ c(1) = x\end{array}\right\} \implies c(t) = xt, \quad \lambda = |x|.$$

> This is the **fundamental lemma of the calculus of variations** in miniature — worth a
> `remark` in the typeset version. Corsin's own flag *(not exam relevant)* should be preserved.

## Bounded $C^1$ domains

*(Corsin p. 6)* — Corsin's heading: *"Bounded $C^1$ domains and why the definition in the script
is so terrible"*.

> **Definition 14.3 (bounded $C^k$ domain)** — *quoted from the official lecture notes (2024),
> pasted into Corsin's notes on p. 6.*
>
> Given $k \geq 1$, a bounded open set $\Omega \subset \mathbb{R}^n$ is called a **bounded $C^k$
> domain** if $M := \partial\Omega$ is an $(n-1)$-dimensional submanifold of class $C^k$.

To define **flux**, we need the concept of **interior and exterior normal vectors**. For $\Omega$
as above, a normal vector $\nu \in N_p(\partial\Omega)$ is **interior** if
$$p + h\nu \in \Omega \qquad \forall h > 0 \text{ small}$$
and **exterior** if
$$p + h\nu \in \mathbb{R}^n\setminus\Omega \qquad \forall h > 0 \text{ small}.$$

A **Gauss map** is a continuous map of unit normal vectors on $\partial\Omega$. There exists a
unique interior and exterior Gauss map,
$$\nu \in C^0(\partial\Omega, S^{n-1}) \text{ such that } \nu(p) \text{ is the exterior normal}$$
— the **exterior unit normal map**.

The **Jordan–Brouwer separation theorem** asserts that if $M \subseteq \mathbb{R}^{n+1}$ is an
$n$-dimensional compact and connected submanifold, then $\mathbb{R}^{n+1}\setminus M$ has exactly
two connected components, an "inside" and an "outside".

## Flux and the divergence theorem

### Flux

*(Corsin p. 7)*

Suppose $F : U \subseteq \mathbb{R}^n\to\mathbb{R}^n$ is a $C^1$ **vector field** and
$\Omega \subseteq U$ is a $C^1$ bounded domain. The **flux** ("Fluss") of $F$ through
$\partial\Omega$ is defined as
$$
\begin{aligned}
&\int_{\partial\Omega}\langle F, \nu\rangle\,d\!\operatorname{vol}_{n-1} && \text{(Analysis notation)} \\
={} &\int_{\partial\Omega}\vec F(x)\cdot d\vec A && \text{(Physics notation)} \\
={} &\int_B \big\langle F\circ\phi(x),\ \nu\circ\phi(x)\big\rangle\sqrt{\det D\phi(x)^{\mathsf T}D\phi(x)}\,dx && \text{(explicit)}
\end{aligned}
$$
where:

- $\nu : \partial\Omega \to S^{n-1}$ is the **exterior unit normal**, i.e. $\nu(y)$ is the outward
  facing unit normal of $\partial\Omega$ at $y \in \partial\Omega$;
- $\phi : B \to \partial\Omega$ is a (local) parametrization of $\partial\Omega$. In general,
  multiple integrals in the explicit formulation may be necessary.

### Special case: $\mathbb{R}^3$

*(Corsin p. 8)*

Let $\Omega \subseteq \mathbb{R}^3$ be a bounded $C^1$ domain and $F \in C^1(\overline\Omega, \mathbb{R}^3)$
a vector field, and let $\phi : B \to \partial\Omega\setminus N$ be a parametrization of
$\partial\Omega\setminus N$, where $N \subseteq \partial\Omega$ is a null set, $B \subseteq \mathbb{R}^2$.
Then:

1. $\displaystyle \nu(x) := \frac{\partial_1\phi(x)\times\partial_2\phi(x)}{|\partial_1\phi(x)\times\partial_2\phi(x)|}$
   is an (interior or exterior) Gauss map. (More precisely, $\nu\circ\phi^{-1}$ is the Gauss map,
   i.e. $\nu(x) \in N_{\phi(x)}(\partial\Omega\setminus N)$.)
2. The Gram determinant is given by
   $$\sqrt{\det D\phi(x)^{\mathsf T}D\phi(x)} = |\partial_1\phi(x)\times\partial_2\phi(x)|.$$
3. Therefore:
   $$\boxed{\ \int_{\partial\Omega}\vec F\cdot d\vec A = \pm\int_B\big\langle F\circ\phi(x),\ \partial_1\phi(x)\times\partial_2\phi(x)\big\rangle\,dx\ }$$
   where the $\pm$ depends on whether $\nu(x)$ is interior $(-)$ or exterior $(+)$.

### Example *(Corsin pp. 9–10)*

Compute the flux of $F(x,y,z) = (xz,\ z,\ y)$ through the surface of $S^2$ with interior
$B_1(0)$.

We use spherical coordinates with $r \equiv 1$:
$$\phi : (0,2\pi)\times(0,\pi)\to\mathbb{R}^3, \qquad (\varphi,\theta)\mapsto\begin{pmatrix}\sin\theta\cos\varphi \\ \sin\theta\sin\varphi \\ \cos\theta\end{pmatrix}$$

**Compute the normal vector:**
$$\partial_\varphi\phi = \begin{pmatrix}-\sin\theta\sin\varphi \\ \sin\theta\cos\varphi \\ 0\end{pmatrix}, \qquad \partial_\theta\phi = \begin{pmatrix}\cos\theta\cos\varphi \\ \cos\theta\sin\varphi \\ -\sin\theta\end{pmatrix}$$
$$\implies \partial_\varphi\phi\times\partial_\theta\phi = \begin{pmatrix}-\sin^2\theta\cos\varphi \\ -\sin^2\theta\sin\varphi \\ -\sin\theta\cos\theta\end{pmatrix}$$

**Sanity check:** does that make sense, and is it exterior or interior?
$$\partial_\varphi\phi\times\partial_\theta\phi = -\sin\theta\,\phi(\varphi,\theta) = -\sin\theta\,(x,y,z)$$
— the exterior normal of $S^2$ is $+(x,y,z)$! *(Corsin p. 10)* So we multiply by $(-1)$ (or switch
the order in the cross product).

**Compute the integral:**
$$
\begin{aligned}
\int_{S^2}\vec F\cdot d\vec A &= \int_0^{2\pi}\int_0^\pi\begin{pmatrix}xz\\z\\y\end{pmatrix}\cdot\begin{pmatrix}\sin\theta\cos\varphi\\\sin\theta\sin\varphi\\\cos\theta\end{pmatrix}\sin\theta\,d\varphi\,d\theta \\
&= \int_0^{2\pi}d\varphi\int_0^\pi d\theta\begin{pmatrix}\sin\theta\cos\varphi\cos\theta\\\cos\theta\\\sin\theta\sin\varphi\end{pmatrix}\cdot\begin{pmatrix}\sin^2\theta\cos\varphi\\\sin^2\theta\sin\varphi\\\sin\theta\cos\theta\end{pmatrix} \\
&= \int_0^{2\pi}d\varphi\int_0^\pi d\theta\left[\sin^3\theta\cos\theta\cos^2\varphi + \sin^2\theta\cos\theta\sin\varphi + \sin^2\theta\cos\theta\sin\varphi\right] \\
&= \pi\int_0^\pi d\theta\ \sin^3\theta\cos\theta \\
&= \pi\left.\frac{\sin^4\theta}{4}\right|_0^\pi = 0
\end{aligned}
$$
(the two $\sin\varphi$ terms integrate to zero over $(0,2\pi)$, and
$\int_0^{2\pi}\cos^2\varphi\,d\varphi = \pi$).

### Gauss' theorem

*(Corsin p. 11)*

This theorem was discovered in 1762 by **Lagrange** and proven in 1828 by **Ostrogradsky**. It
states:

> Let $\Omega \subseteq \mathbb{R}^n$ be a bounded $C^1$ domain and
> $F : \overline\Omega \to \mathbb{R}^n$ a $C^1$ vector field. Then
> $$\int_\Omega \operatorname{div}F\,d\!\operatorname{vol}_n = \int_{\partial\Omega}\langle F,\nu\rangle\,d\!\operatorname{vol}_{n-1}.$$

Or in physics:
$$\int_\Omega \vec\nabla\cdot\vec F\,dx = \int_{\partial\Omega}\vec F\cdot d\vec A \qquad \text{(how cool is this!)}$$

#### Example *(Corsin p. 11)*

We compute the same flux as in the previous exercise, $\Omega = B_1(0)$ with
$\partial\Omega = S^2$, $F(x,y,z) = (xz, z, y)$:
$$
\begin{aligned}
\int_{\partial\Omega}\vec F\cdot d\vec A &= \int_\Omega \operatorname{div}F\,dx \\
&= \int_\Omega z\,dx && (z = r\cos\theta) \\
&= \int_0^1 dr\int_0^{2\pi}d\varphi\int_0^\pi d\theta\ \underbrace{\cos\theta\sin\theta}_{=\ \frac12\sin(2\theta),\ \pi\text{-periodic!}}r^3 \\
&\overset{!}{=} 0
\end{aligned}
$$

> ⚠️ **Check:** Corsin writes $\Omega = S^2$ in the example header; Gauss' theorem needs the
> **solid** ball, $\Omega = B_1(0)$ with $\partial\Omega = S^2$. The computation itself integrates
> over the ball, so only the label is loose. Corrected. See `OQ-22`.

### Why physicists care *(Corsin p. 12)*

Gauss' theorem is also a powerful tool in physics. For example, the water $V$ in a moving fluid
with velocity $\vec v$ passing through a surface element $d\vec A$ in time $\Delta t$ is:

> **[FIG-W10-03]** *(Corsin p. 12)* A blue-outlined parallelogram (the swept volume) with orange
> horizontal flow arrows $\vec v$, the angle $\theta$ marked green between $\vec v$ and the surface
> normal, a red height segment $h = |d\vec A|\cos\theta = \frac{\vec v}{|\vec v|}\cdot d\vec A$, and
> a purple base labelled $L = \Delta t|\vec v|$. → TikZ 3D-ish sketch.

$$V = \Delta t\,\vec v\cdot d\vec A\cdot\rho \qquad (\rho \text{ the density})$$

Therefore, the fluid flowing out of any bounded $C^1$ domain $\Omega$ per unit time is
$$\int_{\partial\Omega}\rho\,\vec v\cdot d\vec A = \int_\Omega \vec\nabla\cdot(\rho\vec v)\,dx.$$
Of course, since the total amount of fluid is conserved, this is also the change in the amount of
fluid in $\Omega$ in time:
$$\int_\Omega\vec\nabla\cdot(\rho\vec v)\,dx = -\frac{d}{dt}\int_\Omega\rho\,dx = -\int_\Omega\frac{\partial\rho}{\partial t}\,dx.$$
Since this is true for any $\Omega$, the **continuity equation** ("Kontinuitätsgleichung") follows:
$$\vec\nabla\cdot(\rho\vec v) + \frac{\partial\rho}{\partial t} = 0.$$

---

## German glossary contributed by this week

| English | German |
|---|---|
| geodesic | Geodäte |
| vector field | Vektorfeld |
| flux | Fluss |
| divergence | Divergenz |
| divergence theorem, Gauss' theorem | Divergenzsatz, Satz von Gauss |
| exterior / interior normal | äussere / innere Normale |
| Gauss map | Gauss-Abbildung |
| solid of revolution | Rotationskörper |
| continuity equation | Kontinuitätsgleichung |
| moment of inertia | Trägheitsmoment |
