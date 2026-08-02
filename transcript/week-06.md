# Week 6 — Convexity, the Inverse & Implicit Function Theorems

**Primary source:** `Corsin Nick/Class Notes/Week 6.pdf` (12 pp)
**Exercise sheet:** `exercises/Ex6_Analysis2_eng.pdf` (solutions: `Sol6_Analysis2_eng.pdf`)
**Lecture notes:** ch. 11–12
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **Title note.** Corsin reaches the **implicit** function theorem already this week (pp. 9–12),
> a week earlier than the provisional map. `docs/03-topic-index.md` corrected.

> **No session split.** As in Week 5, this file carries no `Monday` / `Friday` boxes. His note on
> problem 6.2 — *"This is what we covered on Friday"*, referring to the $2\times 2$ signature rule
> from Week 5 — confirms Week 5 did span both sessions even though it is unmarked.

---

## Exercise sheet 6

*Statements quoted verbatim from `exercises/Ex6_Analysis2_eng.pdf` (assigned 20 March 2026,
due 30 March 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 6.1 | **important** | — |
| 6.2 | **important** | "This is what we covered on Friday. Find a lemma in your linear algebra notes which relates the determinant and trace to the eigenvalues." |
| 6.3 | **semi-important** | "By using $\alpha+\beta+\gamma = \pi$ for the angles, you can express this as an optimization problem in two variables." |
| 6.4 | **semi-important** | — |
| 6.5 | **optional** | "See *data analysis*" |
| 6.6 | **optional** | "Do two or three, not all of them" |
| 6.7 | **important** | — |
| 6.8 | **important** | — |
| 6.9 | **important** | — |
| 6.10–6.12 | **optional** | "These are good exercises, but how many optimization problems do you really need?" |

### 6.1 — Convex function *(important)*

Let $f \in C^2(\mathbb{R}^n)$ be a convex function.

(a) Show that $z \in \mathbb{R}^n$ is a critical point of $f$ if and only if $z$ is a global
minimizer.
(b) Provide an example of such an $f$ in some $\mathbb{R}^n$ with $n > 1$, which is always
nonnegative, but does not have a minimum point. That is to say
$f(x) > \inf_{\mathbb{R}^n} f \geq 0$ for all $x \in \mathbb{R}^n$.

> **Ties into the class notes:** part (a) is exactly Corsin's Exercise part 3 on p. 3, which he
> proves in full on p. 6.

### 6.2 — The signature of a $2\times2$ matrix *(important)*

Despite the definition, it is not necessary to compute the eigenvalues of a matrix to find its
signature.¹ Prove that for a symmetric $2\times2$ matrix $M$ we have the following simple rule to
determine the signature in terms of $\det M$ and $\operatorname{Tr}M$:

- If $\det M > 0$, $\operatorname{Tr}M > 0$ then $M$ is positive definite,
- If $\det M > 0$, $\operatorname{Tr}M < 0$ then $M$ is negative definite,
- If $\det M < 0$ then $M$ is indefinite,
- If $\det M = 0$, then $M$ is degenerate.

*¹ Footnote in the original sheet: "Ask ChatGPT about the Principal Minor Theorem".*

*Official hint:* use the spectral theorem and the properties
$\det(AB) = \det(A)\det(B)$, $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$.

> **Ties into the class notes:** this is the $n=2$ rule Corsin states in Week 5, p. 8.

### 6.3 — Isoperimetric triangles *(semi-important)*

Among all the triangles with perimeter equal to 2, find the ones with the largest area. You may
give for granted Heron's formula, which gives the area of a triangle in terms of the length of its
sides $x, y, z$:
$$A = \sqrt{p(p-x)(p-y)(p-z)}, \qquad \text{with } 2p := x+y+z,$$
so that in our case $p = 1$.

*Official hint:* minimize $A^2$ instead of $A$. You can use the method of Lagrange multipliers.

### 6.4 — Barycenter *(semi-important)*

Let $y_1,\dots,y_k \in \mathbb{R}^n$ be given. Show that there is exactly one point for which
$$f(x) = \|x-y_1\|^2 + \dots + \|x-y_k\|^2, \qquad x \in \mathbb{R}^n$$
is minimal, and determine this point.

### 6.5 — Linear regression I *(optional)*

You study the house market in Zürich over a year in which $N$ houses are sold. You keep track of
the size of the houses $x_1,\dots,x_N$ and the respective sale prices $y_1,\dots,y_N$. Now you
would like to find "the" function $f : \mathbb{R}\to\mathbb{R}$ that gives
$$\text{sale price} = f(\text{size of the house}),$$
and you make the (not unreasonable) assumption that $f$ is affine, i.e. $f_{a,b}(x) = ax+b$ for
some coefficients $a, b \in \mathbb{R}$. Among all such functions find (in terms of the data you
collected) the value of the parameters $a, b$ that minimizes the average quadratic error
$$E(a,b) := \sum_{i=1}^{N}\big(y_i - f_{a,b}(x_i)\big)^2, \qquad a,b\in\mathbb{R}.$$

*Official hint:* do not get distracted by the setting — after all you have to minimize a quadratic
polynomial of $a, b$.

### 6.6 — Convex functions *(optional — "do two or three, not all of them")*

Decide whether the following functions $f_i$ are convex in the convex domain
$U_i \subset \mathbb{R}^n$. Try to find, in each case, the simplest argument; you can almost always
avoid lengthy computations.

1. $f_1(x,y) = x^2+y^2-4y$ in $U_1 = \mathbb{R}^2$
2. $f_2(x,y) = x^2+y^2-y^4$ in $U_2 = \{(x,y)\in\mathbb{R}^2 : x^2+y^2 < \tfrac{1}{10000}\}$
3. $f_3(x,y) = x^2+y^2-4xy$ in $U_3 = \mathbb{R}^2$
4. $f_4(x,y) = x^2+y^2-4xy$ in $U_4 = \{(x,y)\in\mathbb{R}^2 : 0 < \tfrac{1}{10}x < y\}$
5. $f_5(x) = \varphi(g(x))$, $x \in U_5$, where $g \in C^2(U_5)$ is any convex function in
   $U_5 \subset \mathbb{R}^n$ and $\varphi \in C^2(\mathbb{R})$ is any convex and increasing function
6. $f_6(x,y) = (1+x^2+y^2)^{1/2}$ in $U_6 = \mathbb{R}^2$
7. $f_7(x,y) = -(1+x^2+y^2)^{-1/2}$ in $U_7 = \mathbb{R}^2$
8. $f_8(x) = \sum_{i=1}^{n}|x_i|^p$ in $U_8 = \mathbb{R}^n$, where $p \geq 1$ is a fixed exponent
9. $f_9(x) = \max\{\varphi(x), \psi(x)\}$ where $\varphi,\psi \in C(U_9)$ are any pair of convex
   functions defined in some open set $U_9 \subset \mathbb{R}^n$
10. $f_{10}(x) = |x|$ in $U_{10} = \mathbb{R}^n$
11. $f_{11}(x) = \varphi(|x|)$ in $U_{11} = B_1 \subset \mathbb{R}^n$, where
    $\varphi \in C(\mathbb{R})$ is any convex function

### 6.7 — Multiple choice (convex functions) *(important)*

Among the following statements about convex functions mark those (and only those) which are always
true.

(a) If $f \in C^1(U)$ is convex in some open convex set $U \subset \mathbb{R}^n$ and $f$ has a
    local maximum at $z \in U$, then $\nabla f \equiv 0$ in $U$.
(b) If $f \in C^1(U)$ is convex in some open convex set $U \subset \mathbb{R}^n$ and $f$ has a
    global maximum at $z \in U$, then $\nabla f \equiv 0$ in $U$.
(c) Assume $f_n \in C^2(\mathbb{R})$ is a sequence of convex functions that converge pointwise to
    some $f : \mathbb{R}\to\mathbb{R}$. Is $f$ necessarily convex?
(d) There exists a convex function $f \in C^\infty(\mathbb{R}^2)$ such that
    $f(x) = 1 - 2x_1 + x_2^3 + O(|x|^4)$ as $|x| \to 0$.
(e) There exists a convex function $f \in C^\infty(\mathbb{R}^2)$ such that
    $f(x) = 1 - 2x_1 + x_2^4 + O(|x|^4)$ as $|x| \to 0$.
(f) A convex set is not necessarily connected.

### 6.8 — Multiple choice (positive semidefinite Hessian) *(important)*

The Hessian matrix of $f \in C^2(\mathbb{R}^n)$ is positive semidefinite at a critical point $x_0$
of $f$, i.e. $\langle v, Hf(x_0)v\rangle \geq 0$ for all $v \in \mathbb{R}^n$. Which of the
following statements necessarily hold? (There may be more than one.)

(a) $x_0$ is a strict local minimum of $f$.
(b) $x_0$ is a local minimum of $f$.
(c) $x_0$ is not a local maximum of $f$.
(d) None of the above statements.

### 6.9 — Minimization *(important)*

The function $f : \mathbb{R}^2\to\mathbb{R}$ is given by $f(x,y) = 2x^2+y^2-x$. Determine the
extrema of $f$ on…

(a) …the unit circle $\mathbb{S}^1 = \{(x,y)\in\mathbb{R}^2 \mid x^2+y^2 = 1\}$;
(b) …the closed unit disk $\mathbb{D} = \{(x,y)\in\mathbb{R}^2 \mid x^2+y^2 \leq 1\}$.

### 6.10 — Lagrange multipliers *(optional)*

Consider the function $f(x,y,z) = 3x-y+2z$ and the set
$$M = \{(x,y,z)\in\mathbb{R}^3 \mid x^2+y^2+z^2 = 1,\ x+y = 0\}.$$
Determine the extrema of $f$ on $M$ and their nature.

### 6.11 — Closest point on a hyperboloid *(optional)*

Find the points on the submanifold $M = \{(x,y,z)\in\mathbb{R}^3 : z = x^2-y^2\}$ that are closest
to the point $(0,0,1)$.

### 6.12 — Critical points *(optional)*

Let $f : \mathbb{R}^2\to\mathbb{R}$ be the function $f(x,y) = (ax^2+by^2)e^{-x^2-y^2}$ with real
parameters $a, b \in \mathbb{R}$. Find all critical points and determine their nature with the
Hessian test, depending on $a, b$.

---

## Convexity

*(Corsin p. 2)*

A subset $A \subseteq \mathbb{R}^n$ is **convex** ("konvex") if for all $x, y \in A$ and any
$t \in [0,1]$, the point $p = (1-t)x + ty$ is an element of $A$, $p \in A$.

A function $f : A \to \mathbb{R}$ is **convex** if $A$ is convex and for all $x,y \in A$,
$t \in [0,1]$:
$$f\big((1-t)x + ty\big) \leq (1-t)f(x) + tf(y).$$

**Proposition.** *(Corsin p. 2)* Let $U \subseteq \mathbb{R}^n$ be open and convex,
$f \in C^2(U)$. Then
$$f \text{ convex} \iff \mathcal{H}f(x) \text{ nonnegative definite } \forall x \in U$$
$$\iff f(y) - f(x) \geq Df_x(y-x) \quad \forall x,y \in U.$$

**Example.** *(Corsin p. 2)* The parabola is convex:
$$p : \mathbb{R}^n\to\mathbb{R}, \qquad x \mapsto |x|^2 = \sum_{i=1}^{n}x_i^2.$$
Then $\partial_i\partial_j p(x) = 2\delta_{ij}$, so $\mathcal{H}p(x) = 2\operatorname{Id}_n$.
Every eigenvalue is $2 > 0$, hence convex.

### Exercise *(Corsin p. 3)*

1. Show that $f : U \to \mathbb{R}$ is convex if and only if the functions
   $$f_{x,y} : [0,1]\to\mathbb{R}, \qquad s \mapsto f\big(x + s(y-x)\big)$$
   are convex for all $x, y \in U$.
2. Show that
   $$f \text{ convex} \iff f(y) - f(x) \geq Df_x(y-x) \quad \forall x,y\in U$$
   also holds for $f \in C^1(U)$, $U \subseteq \mathbb{R}^n$ open and convex.
3. Conclude that if $f \in C^1(U)$ convex has a critical point at $x_0 \in U$, then it has a
   minimum at $x_0$.

### Solution *(Corsin pp. 3–6)*

**1.** $f_{x,y}$ convex
$$\iff f_{x,y}\big((1-t)s_0 + ts_1\big) \leq (1-t)f_{x,y}(s_0) + tf_{x,y}(s_1) \quad \forall s_0, s_1, t \in [0,1]$$
$$\iff f\Big(x + \big[(1-t)s_0 + ts_1\big](y-x)\Big) \leq (1-t)f\big(x+s_0(y-x)\big) + tf\big(x+s_1(y-x)\big)$$
$$\iff f\Big((1-t)\big(x+s_0(y-x)\big) + t\big(x+s_1(y-x)\big)\Big) \leq (1-t)f\big(x+s_0(y-x)\big) + tf\big(x+s_1(y-x)\big)$$

If we now set $s_0 = 0$, $s_1 = 1$, we get convexity of $f$ if the above holds for all
$x,y \in U$.

Vice versa, if $f$ is convex, then convexity of $f_{x,y}$ follows by applying convexity of $f$ to
the points $x + s_i(y-x)$, $i = 0,1$, for any $x,y \in U$, $s_0, s_1 \in [0,1]$.

**2.** *(Corsin p. 4)* Recall that $g \in C^1(I)$, $I \subseteq \mathbb{R}$ an interval, is convex
if and only if $g'$ is increasing. Therefore:
$$f \text{ convex} \iff f_{x,y}' \text{ increasing } \forall x,y \in U.$$
Compute with the chain rule, for $t \in [0,1]$:
$$f_{x,y}'(t) = Df_{x+t(y-x)}(y-x).$$
By the **mean value theorem**, there exists $s \in (0,1)$ such that
$$f(y) - f(x) = f_{x,y}(1) - f_{x,y}(0) = f_{x,y}'(s) = Df_{x+s(y-x)}(y-x).$$

*(Corsin p. 5)* So if $f$ is convex, then $f_{x,y}$ is convex by **(1)**, therefore $f_{x,y}'$ is
increasing and in particular
$$f_{x,y}'(s) \geq f_{x,y}'(0) \implies f(y) - f(x) \geq Df_x(y-x).$$

If vice versa $f(y) - f(x) \geq Df_x(y-x)$ for all $x,y \in U$, then we must show
$$0 \leq s < t \leq 1 \implies f_{x,y}'(s) \leq f_{x,y}'(t).$$

> **[FIG-W06-01]** *(Corsin p. 5)* A green convex curve $f_{x,y}(r)$ over $r \in [0,1]$ with two
> supporting lines: an orange line $Df_u(r(y-x)) + \text{const.}$ tangent at $r = s$ (negative
> slope) and a purple line $Df_v(r(y-x)) + \text{const.}$ tangent at $r = t$ (positive slope);
> dotted verticals at $0, s, t, 1$. → TikZ plot with two tangent lines.

Let $u = x + s(y-x)$, $v = x + t(y-x)$. Note that $u - v = (s-t)(y-x)$ and
$$Df_u(v-u) \leq f(v) - f(u), \qquad Df_v(u-v) \leq f(u) - f(v).$$
Therefore *(Corsin p. 6)*:
$$
\begin{aligned}
(t-s)f_{x,y}'(s) &= Df_u(v-u) \\
&\leq f(v) - f(u) \\
&\leq -Df_v(u-v) \\
&= Df_v(v-u) \\
&= (t-s)f_{x,y}'(t)
\end{aligned}
$$
And since $(t-s) > 0$, $f_{x,y}'$ is increasing and hence $f_{x,y}$ convex. $\square$

**3.** *(Corsin p. 6)* Since $f$ is convex and $x_0 \in U$ a critical point,
$$0 = Df_{x_0}(y-x_0) \leq f(y) - f(x_0) \quad \forall y \in U.$$
So $f$ is minimal at $x_0$.

## Inverse function theorem

*(Corsin p. 7)*

Let $U \subseteq \mathbb{R}^n$ be open and $f \in C^k(U, \mathbb{R}^n)$, and let $x_0 \in U$ such
that $Df_{x_0}$ is **invertible**. Then there exists an open **neighbourhood** of $x_0$,
$U_0 \subseteq U$, such that
$$f|_{U_0} : U_0 \to f(U_0)$$
is a **$C^k$-diffeomorphism** ("$C^k$-Diffeomorphismus") and
$$D\big(f|_{U_0}^{-1}\big)_{f(x)} = D\big(f|_{U_0}\big)_x^{-1} \qquad \forall x \in U_0.$$

**Q1.** *(Corsin p. 7)* If $f : \mathbb{R}^n\to\mathbb{R}^n$ is $C^k$ and a **homeomorphism**
(bijective with continuous inverse), is it necessarily a $C^k$-diffeomorphism?

**Q2.** If $f \in C^\infty(U,\mathbb{R}^n)$ has an everywhere invertible differential, $Df_x$
invertible for all $x \in U$, $U \subseteq \mathbb{R}^n$ open, then $f$ is a
$C^\infty$-diffeomorphism onto its image. True or false?

**A1.** *(Corsin p. 8)* **False.** Consider $f : \mathbb{R}\to\mathbb{R}$, $x \mapsto x^3$. Then
$f^{-1} : \mathbb{R}\to\mathbb{R}$, $x \mapsto \sqrt[3]{x}$ is not continuously differentiable at
$0 \in \mathbb{R}$.

**A2.** **False.** Consider
$$\cos|_{\mathbb{R}\setminus\pi\mathbb{Z}} : \mathbb{R}\setminus\pi\mathbb{Z} \to (-1,1), \qquad x \mapsto \cos(x).$$
For any $x \in \mathbb{R}\setminus\pi\mathbb{Z}$, $\cos'(x) = -\sin(x) \neq 0$. But the cosine is
not bijective.

> **[FIG-W06-02]** *(Corsin p. 8)* A cosine curve on axes with $\pi/2$, $\pi$, $3\pi/2$, $2\pi$
> marked in green, and a red dashed horizontal line crossing it repeatedly, annotated "not
> injective". → TikZ/pgfplots.

> **[FIG-W06-03]** *(Corsin p. 8)* A wiggly blue curve with two red dashed horizontal levels: the
> upper one at a local maximum annotated "not invertible", the lower one on a flat-ish stretch
> annotated "invertible, but not diffeo"; a green dashed tangent on the steep descending branch
> annotated "diffeo by IFT". → TikZ freehand-style plot with annotations.

## Implicit function theorem

*(Corsin p. 9)*

**Setup (IF).** With $n > n-d \geq 1$:

- $f \in C^k(\mathbb{R}^d\times\mathbb{R}^{n-d}, \mathbb{R}^{n-d})$ (or an open subset of
  $\mathbb{R}^d\times\mathbb{R}^{n-d}$),
- $f(x_0,y_0) = 0$ for some $(x_0,y_0) \in \mathbb{R}^d\times\mathbb{R}^{n-d}$,
- $D_y f_{(x_0,y_0)}$, the differential of $y \mapsto f(x_0,y)$ at $y_0$, is **bijective** (so
  $J_y f(x_0,y_0)$ is invertible).

> **[FIG-W06-04]** *(Corsin p. 9)* Axes $x \in \mathbb{R}^d$ (green, horizontal) and
> $y \in \mathbb{R}^{n-d}$ (orange, vertical); the point $(x_0,y_0)$ marked; a purple arrow
> $D_yf(x_0,y_0)$ from a vertical $\partial y$ tick to a $\partial f$ tick on a separate blue
> $\mathbb{R}^{n-d}$ axis, and a blue arrow $f$ from $(x_0,y_0)$ to $0 = f(x_0,y_0)$ on that axis.
> → TikZ, two coordinate systems + arrows.

**Consequence: THEN** there exist $B_r(x_0) \subseteq \mathbb{R}^d$ and
$B_s(y_0) \subseteq \mathbb{R}^{n-d}$ and $g \in C^k(B_r(x_0), B_s(y_0))$ such that for all
$(x,y) \in B_r(x_0)\times B_s(y_0)$:
$$f(x,y) = 0 \iff y = g(x).$$

In our picture, this means that the **level set** $\{f(x,y) = 0\}$ can locally be expressed as a
**graph over $x$**.

> **[FIG-W06-05]** *(Corsin p. 10)* Same axes; a green box $B_r(x_0)\times B_s(y_0)$ containing a
> purple S-shaped curve through $(x, g(x))$; a purple arrow labelled $f$ mapping it to
> $0 = f(x, g(x))$ on the blue axis. → TikZ, box + graph + arrow.

Furthermore,
$$Jg(x) = -\big(J_yf(x, g(x))\big)^{-1}J_xf(x,g(x)).$$

> *(Corsin's aside, p. 10: "The geometrical meaning of this one eludes me, sorry ☺")* — keep this
> remark; it is characteristic of his voice.

### Examples *(Corsin pp. 10–12)*

**1. Circle $S^1$.** $S^1 = \{(x,y)\in\mathbb{R}^2 : x^2+y^2-1 = 0\}$ is the level set to
$0 \in \mathbb{R}$ for $F(x,y) = x^2+y^2-1$:
$$S^1 = F^{-1}\{0\} = \{(x,y)\in\mathbb{R}^2 : F(x,y) = 0\}.$$

> **[FIG-W06-06]** *(Corsin p. 10)* A green circle on axes; a blue dotted interval around $x_0$ on
> the $x$-axis lifting to the upper arc labelled $y = \sqrt{1-x^2}$; at $\bar x = 1$ a red dotted
> mark annotated "not possible around $y = 0$"; a green arrow $F$ to a separate $\mathbb{R}$ axis
> with $0$ marked. → TikZ, circle + graph-over-$x$ annotation.

*(Corsin p. 11)* Locally, we have explicit functions
$$x \mapsto \pm\sqrt{1-x^2} = y(x)$$
which we can define on open intervals around $x_0$ whenever $y(x_0) \neq 0$. And indeed,
$$D_yF(x,y) = \frac{\partial F}{\partial y} = 2y$$
is bijective whenever $y \neq 0$, so the implicit function theorem holds.

**2.** Suppose $G(x,y) = y^5+y^3+y+x$. Consider the level set
$$G^{-1}\{0\} = \{(x,y)\in\mathbb{R}^2 : G(x,y) = 0\}.$$
Clearly $(0,0) \in G^{-1}\{0\}$, i.e. $G(0,0) = 0^5+0^3+0+0 = 0$.

Now both:
$$\partial_x G(0,0) = 1 \neq 0, \qquad \partial_y G(0,0) = \big[5y^4+3y^2+1\big]_{y=0} = 1 \neq 0.$$

So by the implicit function theorem, there are open intervals (balls) $(-r,r)$, $(-s,s)$ and
functions
$$(-s,s) \to (-r,r), \quad y \mapsto x(y) = -y^5-y^3-y, \qquad (-r,r)\to(-s,s), \quad x \mapsto y(x) = \ ?$$

> ⚠️ **Check:** Corsin writes the two domains the other way round — $x(y)$ on $(-r,r)\to(-s,s)$
> and $y(x)$ on $(-s,s)\to(-r,r)$. Since $r$ is the radius around $x_0$ and $s$ the radius around
> $y_0$ (his own setup on p. 9), the assignments must be swapped. Corrected. See `OQ-15`.

*(Corsin p. 12)* satisfying
$$y^5+y^3+y+x(y) = 0, \qquad y(x)^5+y(x)^3+y(x)+x = 0.$$

**Galois, Abel: for $y(x)$, no formula exists!** Nevertheless, we know that $y(x)$ exists by the
implicit function theorem. And we can graph it with a computer!

> **[FIG-W06-07]** *(Corsin p. 12)* Plot of the implicitly defined $y(x)$ solving
> $y^5+y^3+y+x = 0$ for $x \in [-10,10]$: a decreasing curve from $y \approx 1.4$ to
> $y \approx -1.4$, steepest at the origin. → pgfplots (solve numerically, or plot the inverse
> $x = -y^5-y^3-y$ with axes swapped — the latter is exact and trivial).

---

## German glossary contributed by this week

| English | German |
|---|---|
| convex | konvex |
| convex set | konvexe Menge |
| mean value theorem | Mittelwertsatz |
| neighbourhood | Umgebung |
| diffeomorphism | Diffeomorphismus |
| homeomorphism | Homöomorphismus |
| inverse function theorem | Satz über inverse Funktionen |
| implicit function theorem | Satz über implizite Funktionen |
| graph (of a function) | Graph |
