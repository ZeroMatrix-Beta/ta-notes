# Week 11 — Gauss' Theorem Revisited, Alternating Forms & Differential Forms

**Primary source:** `Corsin Nick/Class Notes/Week 11.pdf` (15 pp)
**Exercise sheet:** `exercises/Ex11_Analysis2_eng.pdf` (solutions: `Sol11_Analysis2_eng.pdf`)
**Lecture notes:** ch. 14
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **The longest and most theoretical week.** Corsin builds differential forms from scratch:
> motivation (reparametrization invariance) → antisymmetric $k$-linear forms → the wedge product
> → the basis expansion → differential forms → the exterior derivative, ending by recovering
> $\operatorname{curl}$ from $d$ on a 1-form in $\mathbb{R}^3$.

> **No session split.** No `Monday`/`Friday` boxes in this file.

---

## Exercise sheet 11

*Statements quoted verbatim from `exercises/Ex11_Analysis2_eng.pdf` (assigned 1 May 2026,
due 11 May 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

This week the page carries only the colour code, no written notes.

| Problem | Priority |
|---|---|
| 11.1 | **important** |
| 11.2 | **semi-important** |
| 11.3 | **semi-important** |
| 11.4 | **semi-important** |
| 11.5 | **important** |
| 11.6 | **optional** |
| 11.7 | **optional** |
| 11.8 | **important** |
| 11.9 | **important** |

### 11.1 — Flow of vector field *(important)*

Compute the flow of the vector field
$$V : (x,y,z)\mapsto(x,\ y,\ z-x^2-y^2)$$
through the upper hemisphere $S = \{(x,y,z)\in\mathbb{R}^3 : x^2+y^2+z^2 = 1,\ z \geq 0\}$ from
"inside" to "outside". That is the number $\int_S V(x)\cdot\nu(x)\,d\!\operatorname{vol}_2$.

### 11.2 — Closed answer *(semi-important)*

For each of the following improper integrals, say whether they have a well-defined *finite* value
or not.

(a) $\int_{B_1}|x|^{-n}\,dx$ with $B_1 \subset \mathbb{R}^n$
(b) $\int_{B_1}|x|^{-n+\epsilon}\,dx$ with $B_1\subset\mathbb{R}^n$, $\epsilon > 0$
(c) $\int_{\mathbb{R}^n\setminus B_1}|x|^{-n+\epsilon}\,dx$ with $B_1\subset\mathbb{R}^n$, $\epsilon>0$
(d) $\int_{\mathbb{R}^n\setminus B_1}|x|^{-n-\epsilon}\,dx$ with $B_1\subset\mathbb{R}^n$
(e) $\int_{B_1}|x|^{-n}e^{-1/|x|}\,dx$ with $B_1\subset\mathbb{R}^n$
(f) $\int_{\mathbb{R}^3}\frac{e^{-z^2}}{x^2+y^2}\,dx\,dy\,dz$
(g) $\int_{\mathbb{R}^3}\frac{e^{-x^2-y^2-z^2}}{x^2+y^2}\,dx\,dy\,dz$
(h) $\int_{A_0}\frac{dx\,dy}{x^2y^2}$ with $A_0 := \{(x,y)\in\mathbb{R}^2 : x^2+y^2 > 1,\ x>0,\ y>0\}$
(i) $\int_{A_\epsilon}\frac{dx\,dy}{x^2y^2}$ with
    $A_\epsilon := \{(x,y)\in\mathbb{R}^2 : x^2+y^2>1,\ x>\epsilon y>0,\ y>\epsilon x>0\}$ and $\epsilon>0$

### 11.3 — Standard computation *(semi-important)*

Let $F : \mathbb{R}^3\to\mathbb{R}^3$ be given by
$F(x,y,z) = (x\cos^2 z,\ y\sin^2 z,\ z\sqrt{x^2+y^2})$ and let
$B = \{(x,y,z)\in\mathbb{R}^3 \mid 0 \leq z \leq 1-\sqrt{x^2+y^2}\}$. Calculate the flux integral
$\int_{\partial B}F\cdot\nu\,d\!\operatorname{vol}_{n-1}$.

### 11.4 — Fluxes, divergences etc. *(semi-important)*

Let $Z \subset \mathbb{R}^3$ be the area bounded by the surfaces
$$M = \{(x,y,z)\in\mathbb{R}^3 \mid x^2+y^2 = 4\}, \quad G_1 = \{(x,y,-1)\in\mathbb{R}^3\}, \quad G_2 = \{(x,y,1)\in\mathbb{R}^3\}.$$

1. Draw the set $Z$.
2. Find parameterizations of the three submanifolds $M$, $G_1$, $G_2$, such that the corresponding
   normal vectors point outward.
3. Let $F : \mathbb{R}^3\to\mathbb{R}^3$ be the vector field $F(x,y,z) = (z,y,x)$. Compute
   $\int_{\partial Z}F\cdot\nu\,d\!\operatorname{vol}_{n-1}$.
4. Compute the 2-volume of $\partial Z$.
5. Compute the 3-volume of $Z$.

### 11.5 — Radial vector fields *(important)*

For $\alpha \in \mathbb{R}$ consider the vector field
$V_\alpha(x) = |x|^\alpha x$, $x \in \mathbb{R}^n\setminus\{0\}$, where $|x|$ is the usual
Euclidean norm.

1. Compute $\operatorname{div}V_\alpha(x)$ for all $x \neq 0$, and show that it vanishes
   identically for $\alpha = -n$.
2. Using the divergence theorem on $V_0$, show the following relation between the $n$-volume of a
   sphere and the $(n-1)$-volume of its boundary:
   $$r\operatorname{vol}_{n-1}(\partial B_r) = n\operatorname{vol}_n(B_r), \qquad \forall r > 0.$$
3. Show that
   $$\int_{\partial B_1}V_{-n}\cdot\nu\,d\!\operatorname{vol}_{n-1} > 0, \qquad \int_{B_1}\operatorname{div}V_{-n}(x)\,dx = 0.$$
   Why doesn't this contradict the divergence theorem?

### 11.6 — The heat kernel *(optional)*

A function $u \in C^2((0,\infty)\times\mathbb{R}^n)$ solves the **heat equation** if and only if
$$\frac{\partial u}{\partial t} = \frac{\partial^2u}{\partial x_1^2} + \frac{\partial^2u}{\partial x_2^2} + \dots + \frac{\partial^2u}{\partial x_n^2}, \qquad \text{for all } x\in\mathbb{R}^n,\ t>0. \tag{1}$$
In the physical interpretation, $u = u(x,t)$ represents the temperature at position $x$ and time
$t > 0$. You will see more of this in Analysis IV. For now we just want to verify a formula that
gives $u(x,t)$ in terms of the initial temperature $u(x,0^+) =: f(x)$.

The **heat kernel**, denoted by $H(x,t)$, is the rescaled Gaussian function
$$H(x,t) = \frac{1}{(4\pi t)^{n/2}}e^{-\frac{|x|^2}{4t}}, \qquad x\in\mathbb{R}^n,\ t>0.$$

1. Prove that $H(x,t)$ solves (1) and $\int_{\mathbb{R}^n}H(z,t)\,dz = 1$ for all $t > 0$.
2. Prove that for every $f \in C(\mathbb{R}^n)$ compactly supported, the function
   $u(x,t) := \int_{\mathbb{R}^n}H(x-y,t)f(y)\,dy$, $x\in\mathbb{R}^n$, $t>0$, solves (1).
   (Notice that this is *not* an improper integral.)
3. **(\*)** Assume further that $f$ is Lipschitz continuous. Prove that, for each fixed
   $x \in \mathbb{R}^n$, $u(x,t)\to f(x)$ as $t\to 0^+$.
   *Sketch: write $f(x) = \int_{\mathbb{R}^n}H(x-y,t)f(x)\,dy$ and try to bound $|u(x,t)-f(x)|$.
   In the resulting integral change the variables replacing $y = x+\sqrt t z$. Use the compact
   support of $f$ (and its uniform continuity) to prove that the integral goes to 0 as $t\to0$.*

### 11.7 — Reality check *(optional)*

Verify the divergence theorem, i.e.
$\int_B\operatorname{div}F(x)\,dx = \int_{\partial B}F\cdot\nu\,d\!\operatorname{vol}_{n-1}$, for
the following domains and vector fields:

1. Let $a,b,c>0$, $F(x,y,z) = (x^2,y^2,z^2)$ and $B = [0,a]\times[0,b]\times[0,c]$.
2. Let $F(x,y,z) = (2xy,\ 3xy,\ ze^{x+y})$ and $B = [0,1]^3$.
3. Let $F(x,y,z) = (x,2y,3z)$ and
   $B = \{(x,y,z)\in\mathbb{R}^3 \mid 0\leq x\leq 1,\ 0\leq y\leq x,\ 0\leq z\leq x+y\}$.

### 11.8 — Multiple choice *(important)*

Say whether the following statements are always true or might be false. Let
$\Omega\subset\mathbb{R}^n$ be any open set.

(a) If $f \in C^0(\Omega)$ has compact support (in $\Omega$), then $f$ is uniformly continuous.
(b) If $f \in C^0(\Omega)$ has compact support (in $\Omega$), and is locally Lipschitz continuous
    (in $\Omega$), then $f$ is Lipschitz continuous (in $\Omega$).
(c) If $f \in C^1(\Omega)$ has compact support (in $\Omega$), then it is Lipschitz continuous
    (in $\Omega$).
(d) If $f \in C^1(\Omega)$, then it is Lipschitz continuous (in $\Omega$).

### 11.9 — Differential forms *(important)*

Compute the differentials of the following differential forms in $\mathbb{R}^3$:

(a) $\omega = y\,dx + z\,dy + \cos(x+y)\,dz$
(b) $\omega = x^2\,dy + yz\,dx + e^z\,dz$
(c) $\omega = (e^x+2y)\,dy\wedge dz + x\sin(y)\,dz\wedge dx$
(d) $\omega = (x+y+z)\,dx\wedge dy + xyz\,dx\wedge dz$
(e) $\omega = \cos(\ln(x^2+3) - \sin(y)z^5)\,dy\wedge dx\wedge dz$

> **Ties into the class notes:** everything needed for 11.9 is on pp. 13–15 — the exterior
> derivative rules and the worked $\mathbb{R}^3$ 1-form example.

---

## Intuition and final words on Gauss' theorem

*(Corsin p. 2)*

**Gauss' theorem.** $B \subseteq \mathbb{R}^n$ a bounded $C^1$-domain and
$F : \overline B\to\mathbb{R}^n$ a $C^1$ vector field. Then
$$\int_B \operatorname{div}(F)\,d\!\operatorname{vol}_n = \int_{\partial B}\langle F,\nu\rangle\,d\!\operatorname{vol}_{n-1}$$
where $\nu : \partial B \to S^{n-1}$ is the exterior unit normal.

### Special case $n = 1$: the fundamental theorem of calculus

*(Corsin p. 2)*

$f : [a,b]\to\mathbb{R}$ of class $C^1$ (this **is** a vector field!). Then Gauss' formula becomes
$$
\begin{aligned}
\int_a^b\frac{\partial f}{\partial x}\,dx &= \int_{[a,b]}\operatorname{div}f\,d\!\operatorname{vol}_1 \\
&= \int_{\partial[a,b]}\langle f,\nu\rangle\,d\!\operatorname{vol}_0 \\
&= f(b) - f(a) \qquad \text{(FTC) (almost)}
\end{aligned}
$$

There are several problems with this argument, for example what a 0-dimensional Jordan measure or
0-dimensional submanifold is. But the definitions from the lecture can be extended to include this
case.

### Vice versa: FTC proves a special case of Gauss' theorem

*(Corsin p. 3)*

Suppose $F : [0,1]^2\to\mathbb{R}^2$ is a $C^1$ vector field. Then Gauss' theorem holds on
$B = (0,1)^2$.

> **[FIG-W11-01]** *(Corsin p. 3)* The unit square with corners $(0,0)$, $(1,0)$, $(1,1)$,
> $(0,1)$ labelled, and the four outward unit normals $-e_1$, $e_1$, $-e_2$, $e_2$ drawn on the
> corresponding edges. → TikZ 2D sketch.

**Proof.**
$$
\begin{aligned}
\int_{\partial B}\langle F,\nu\rangle\,d\!\operatorname{vol}_1 ={}& \int_0^1\langle F(0,t), -e_1\rangle\,dt + \int_0^1\langle F(1,t), e_1\rangle\,dt \\
&+ \int_0^1\langle F(t,0), -e_2\rangle\,dt + \int_0^1\langle F(t,1), e_2\rangle\,dt \\
={}& \int_0^1\big[F_1(1,t) - F_1(0,t)\big]dt + \int_0^1\big[F_2(t,1) - F_2(t,0)\big]dt \\
\overset{\text{FTC}}{=}{}& \int_0^1\left(\int_0^1\partial_1F_1(s,t)\,ds\right)dt + \int_0^1\left(\int_0^1\partial_2F_2(t,s)\,ds\right)dt \\
\overset{\text{Fubini}}{=}{}& \int_B\partial_1F_1\,d\!\operatorname{vol}_2 + \int_B\partial_2F_2\,d\!\operatorname{vol}_2 \\
={}& \int_B\operatorname{div}F\,d\!\operatorname{vol}_2 \qquad \square
\end{aligned}
$$

## Differential forms

### Motivation

*(Corsin p. 4)*

Suppose you study a submanifold $M \subseteq \mathbb{R}^n$, and you find a parametrization
$\phi : D \to M$. You compute the integral of some quantity over $M$ (for example, the Gauss
curvature — see **Gauss–Bonnet** if you are interested) and you want to know: **is this number a
property of $\phi$, or is it a property of $M$?** If it is invariant under reparametrization, then
it must be the latter! **Differential forms satisfy exactly this property.**

> **[FIG-W11-02]** *(Corsin p. 4)* Commutative triangle: $D \xrightarrow{\ \phi\ } M$ along the
> top, $V$ at bottom-left with $\Psi : V \to D$ upward (annotated "diffeo, $\det D\Psi > 0$") and
> $\phi\circ\Psi : V \to M$ along the diagonal. → `tikz-cd`.

$$
\begin{aligned}
\int_M\omega &= \int_D\omega_{\phi(x)}(D\phi_x)\,dx \\
&\overset{\substack{\text{change of variable}\\(\text{reparam.})}}{=} \int_V\omega_{\phi\circ\Psi(y)}(D\phi_{\Psi(y)})\,|\det D\Psi_y|\,dy \\
&\overset{!}{=} \int_V\omega_{\phi\circ\Psi(y)}\big(D(\phi\circ\Psi)_y\big)\,dy = \int_M\omega
\end{aligned}
$$

### Antisymmetric $k$-linear forms

*(Corsin p. 5)*

Let $V$ be an $n$-dimensional real vector space and let $L : V^k\to\mathbb{R}$ satisfy:

- $L$ is **$k$-linear**, i.e. it is linear in every entry:
  $$L(v_1, v_2, \dots, \alpha v_i + \beta w_i, \dots, v_k) = \alpha L(v_1,\dots,v_i,\dots,v_k) + \beta L(v_1,\dots,w_i,\dots,v_k)$$
- $L$ is **anti-symmetric**, i.e.
  $$L(v_1,\dots,v_i,\dots,v_j,\dots,v_k) = -L(v_1,\dots,v_j,\dots,v_i,\dots,v_k)$$

**Remark.** For $k = n$, $V = \mathbb{R}^n$, $L(e_1,\dots,e_n) = 1$: there exists a **unique** such
$L$, namely $L = \det$.

**Notation.** For $v \in V$ and a fixed basis $(e_1,\dots,e_n)$ of $V$, we will write
$$v = \sum_{i=1}^n v^ie_i = (v^1, v^2, \dots, v^n)$$
to distinguish the **components of a vector** from a **list of vectors** $v_1,\dots,v_k \in V$.

We will now set $V = \mathbb{R}^n$ with the standard basis.

#### Examples *(Corsin p. 6)*

**1.** Fix $A \in \operatorname{Mat}_{k\times n}$, and note that
$V = (v_1\mid v_2\mid\cdots\mid v_k) = (v^i_j)_{\substack{i=1,\dots,n\\ j=1,\dots,k}}$ is an
$n\times k$ matrix. Then $L := \det(AV)$ satisfies the requirements.

**2.** For $k = 1$, $L : \mathbb{R}^n\to\mathbb{R}$ is a **covector**, $L \in (\mathbb{R}^n)^*$.
The standard basis of $(\mathbb{R}^n)^*$, $(e_1^*,\dots,e_n^*)$ satisfying
$e_i^*(e_j) = \delta_{ij}$, are **1-forms**. In particular, $e_i^*(v) = v^i$.

#### Equivalence with the lecture's condition *(Corsin pp. 6–7)*

In the lecture, instead of anti-symmetry, you have seen the condition: for
$V := (v_1,\dots,v_k) \in \operatorname{Mat}_{n\times k}$ and
$A = \begin{pmatrix}a_{11}&\cdots&a_{1k}\\ \vdots&\ddots&\vdots\\ a_{k1}&\cdots&a_{kk}\end{pmatrix} \in \operatorname{Mat}_{k\times k}$,
$$L(VA) = L(V)\det(A).$$
These two conditions are equivalent. We will show the special case $n = 3$, $k = 2$, i.e. for
$$V = \begin{pmatrix}v^1 & w^1\\ v^2 & w^2\\ v^3 & w^3\end{pmatrix} = (v_1\mid v_2), \qquad A = \begin{pmatrix}a&b\\c&d\end{pmatrix}.$$

*(Corsin p. 7)* First, we rewrite $L(VA)$ as $L(x_1,x_2)$, that is, in multilinear form. Note:
$$VA = (v, w)\begin{pmatrix}a&b\\c&d\end{pmatrix} = (av+cw,\ bv+dw)$$
so:
$$
\begin{aligned}
L(VA) &= L(av+cw,\ bv+dw) \\
&= aL(v,\ bv+dw) + cL(w,\ bv+dw) \\
&= ab\underbrace{L(v,v)}_{0} + ad\,L(v,w) + cb\,L(w,v) + cd\underbrace{L(w,w)}_{0} \\
&= L(v,w)(ad-bc) \\
&= L(V)\det(A)
\end{aligned}
$$
where we used $L(v,v) = -L(v,v) \implies L(v,v) = 0$.

### The wedge product

*(Corsin p. 7)*

There is a closed form for the wedge product that is not terribly important for our purposes: for
$\alpha$ a $k$-form and $\beta$ an $m$-form,
$$\alpha\wedge\beta(v_1,\dots,v_k,v_{k+1},\dots,v_{k+m}) = \sum_{\sigma\in S_{k,m}}\operatorname{sgn}(\sigma)\,\alpha(v_{\sigma(1)},\dots,v_{\sigma(k)})\,\beta(v_{\sigma(k+1)},\dots,v_{\sigma(k+m)})$$
*(Corsin p. 8)* where $S_{k,m}$ are all the permutations $\sigma$ of $\{1,\dots,k+m\}$ such that
$\sigma(1) < \dots < \sigma(k)$ and $\sigma(k+1) < \dots < \sigma(k+m)$.

**The following properties are important for us:**

1. $\wedge$ is bilinear.
2. For $\alpha$ a $k$-form, $\beta$ an $m$-form, $\alpha\wedge\beta$ is a $(k+m)$-form.
3. $(\alpha\wedge\beta)\wedge\gamma = \alpha\wedge(\beta\wedge\gamma) = \alpha\wedge\beta\wedge\gamma$
   (associative).
4. For 1-forms $L_1, L_2, \dots, L_k$ and vectors $v_1,\dots,v_k\in\mathbb{R}^n$:
   $$L_1\wedge L_2\wedge\dots\wedge L_k(v_1,\dots,v_k) = \det\big(L_i(v_j)\big).$$
5. For $\alpha(T) := \det(AT)$, $\beta(S) := \det(BS)$ we have
   $$\alpha\wedge\beta(X) = \det\left(\left[\frac{A}{B}\right]X\right).$$

**Example.** *(Corsin pp. 8–9)* From (4) follows:
$$e_{i_1}^*\wedge e_{i_2}^*\wedge\dots\wedge e_{i_k}^*(v_1,\dots,v_k) = \det\begin{pmatrix}v_1^{i_1}&\cdots&v_k^{i_1}\\ \vdots&\ddots&\vdots\\ v_1^{i_k}&\cdots&v_k^{i_k}\end{pmatrix}$$
So:
$$e_{i_1}^*\wedge\dots\wedge e_{i_k}^*(v_1,\dots,v_k) = \det\left(\begin{bmatrix}e_{i_1}^{\mathsf T}\\ \vdots\\ e_{i_k}^{\mathsf T}\end{bmatrix}\big[v_1\ \cdots\ v_k\big]\right)$$

### Every $k$-form is a combination of wedge products of $e_i^*$

*(Corsin pp. 9–10)*

We now want to show that any linear $k$-form on $\mathbb{R}^n$ can be written as
$$L = \sum_{1\leq i_1 < \dots < i_k \leq n}\ell_{i_1\dots i_k}\,e_{i_1}^*\wedge\dots\wedge e_{i_k}^*.$$
To do this, we simply expand $L(v_1,\dots,v_k)$ with $v_i = \sum_{m=1}^n v_i^me_m$ and use
antisymmetry:
$$
\begin{aligned}
L(v_1,\dots,v_k) &= L\left(\sum_{i_1=1}^n v_1^{i_1}e_{i_1},\ \dots,\ \sum_{i_k=1}^n v_k^{i_k}e_{i_k}\right) \\
&= \sum_{1\leq i_1, i_2, \dots, i_k \leq n} L(e_{i_1},\dots,e_{i_k})\,v_1^{i_1}\cdots v_k^{i_k}
\end{aligned}
$$
By antisymmetry, $L(e_{i_1},\dots,e_{i_k}) = 0$ if $e_{i_j} = e_{i_m}$ for some entries
$e_{i_j}$, $e_{i_m}$. Therefore
$$
\begin{aligned}
&= \sum_{\substack{1\leq i_1,i_2,\dots,i_k\leq n \\ i_1\neq\dots\neq i_k}} L(e_{i_1},\dots,e_{i_k})\,v_1^{i_1}\cdots v_k^{i_k} \\
&= \sum_{1\leq i_1<\dots<i_k\leq n}\ \sum_{\sigma\in S_k} L(e_{i_{\sigma(1)}},\dots,e_{i_{\sigma(k)}})\,v_1^{i_{\sigma(1)}}\cdots v_k^{i_{\sigma(k)}} \\
&= \sum_{1\leq i_1<\dots<i_k\leq n}\underbrace{L(e_{i_1},\dots,e_{i_k})}_{=:\ \ell_{i_1\dots i_k}}\underbrace{\sum_{\sigma\in S_k}\operatorname{sgn}(\sigma)\,v_1^{i_{\sigma(1)}}\cdots v_k^{i_{\sigma(k)}}}_{=\ \det\left(\begin{smallmatrix}v_1^{i_1}&\cdots&v_k^{i_1}\\ \vdots&&\vdots\\ v_1^{i_k}&\cdots&v_k^{i_k}\end{smallmatrix}\right)} \\
&= \sum_{1\leq i_1<\dots<i_k\leq n}\ell_{i_1\dots i_k}\,e_{i_1}^*\wedge\dots\wedge e_{i_k}^*(v_1,\dots,v_k)
\end{aligned}
$$

### Differential forms proper

*(Corsin p. 10)*

**Definition.** A **differential $p$-form** ("Differentialform") $\omega$ is defined in a domain
$D \subseteq \mathbb{R}^n$ if for all $x \in D$,
$$\omega(x) = \omega_x : \mathbb{R}^n\to\mathbb{R}$$
is an **antisymmetric, $n$-linear** map.

> ⚠️ **Check:** for a $p$-form the map must be $p$-linear on $(\mathbb{R}^n)^p$, not $n$-linear on
> $\mathbb{R}^n$; the displayed signature is loose on both counts. The expansion immediately below
> uses $p$ indices, confirming the intent. Corrected to
> $\omega_x : (\mathbb{R}^n)^p \to \mathbb{R}$, antisymmetric and $p$-linear. See `OQ-23`.

As seen above, if $(e_1(x),\dots,e_n(x))$ is a basis of $\mathbb{R}^n$ for any $x \in D$, then we
can write
$$\omega(x) = \sum_{1\leq i_1<\dots<i_p\leq n}\omega_{i_1\dots i_p}(x)\,e_{i_1}^*(x)\wedge\dots\wedge e_{i_p}^*(x)$$
where $\omega_{i_1\dots i_p} : \mathbb{R}^n\to\mathbb{R}$ are functions.

**Notation.** *(Corsin p. 11)*

- We often write $e_{i_1}^*\wedge\dots\wedge e_{i_p}^* = e_I^*$.
- We denote the set of $p$-forms on $D \subseteq \mathbb{R}^n$ by $\Omega^p(U)$.
- By convention, $\Omega^0(U) = C^\infty(U)$.

#### Examples *(Corsin pp. 11–12)*

Let $U \subseteq \mathbb{R}^n$.

**1.** $f \in C^\infty(U)$ is a **0-form**.

**2.** A vector field $F : U \to \mathbb{R}^n$ has an associated **1-form** defined as
$$\omega_F(x) : \mathbb{R}^n\to\mathbb{R}, \qquad v \mapsto \langle F(x), v\rangle$$
i.e.
$$\omega_F(x)(v) = \sum_{i=1}^n F^i(x)v^i = \sum_{i=1}^n F^i(x)\,e_i^*(x)(v_i) \implies \boxed{\ \omega_F = \sum_{i=1}^n F^ie_i^*\ }$$

**3.** $F : U \to \mathbb{R}^n$ also naturally induces an **$(n-1)$-form** by
$$\omega_F^{n-1}(x) : (\mathbb{R}^n)^{n-1}\to\mathbb{R}, \qquad (v_1,\dots,v_{n-1})\mapsto\det\big(F(x)\mid v_1\mid\cdots\mid v_{n-1}\big).$$
If we develop the determinant over the first column, we get
$$\omega_F^{n-1}(x)(v_1,\dots,v_{n-1}) = \sum_{i=1}^n(-1)^{i-1}F^i(x)\underbrace{\begin{vmatrix}v_1^1&\cdots&v_{n-1}^1\\ \vdots&&\vdots\\ v_1^{i-1}&\cdots&v_{n-1}^{i-1}\\ v_1^{i+1}&\cdots&v_{n-1}^{i+1}\\ \vdots&&\vdots\\ v_1^n&\cdots&v_{n-1}^n\end{vmatrix}}_{e_1^*\wedge\dots\wedge e_{i-1}^*\wedge e_{i+1}^*\wedge\dots\wedge e_n^*(v_1,\dots,v_{n-1})}$$
Thus:
$$\omega_F^{n-1} = \sum_{i=1}^n(-1)^{i-1}F^i\,e_1^*\wedge\dots\wedge\widehat{e_i^*}\wedge\dots\wedge e_n^*$$
where $\widehat{\phantom{x}}$ denotes an **omitted** factor.

**4.** In particular, for $F : \mathbb{R}^3\to\mathbb{R}^3$, we have
$$\omega_F^2(x)(v_1,v_2) = \langle F(x),\ v_1\times v_2\rangle = \det\big(F(x)\mid v_1\mid v_2\big).$$

### The exterior derivative

*(Corsin p. 13)*

You have seen in the lecture that there exists a **linear operator**
$d : \Omega^k(U)\to\Omega^{k+1}(U)$ satisfying:

1. For $f \in C^\infty(U) = \Omega^0(U)$: $\;df = Df$, the standard differential.
2. $\omega \in \Omega^k(U)$, $\theta \in \Omega^s(U)$, then
   $d(\omega\wedge\theta) = d\omega\wedge\theta + (-1)^k\omega\wedge d\theta$.
3. $d\circ d\,\omega = d^2\omega = 0$.

In particular, we denote by $dx^i$ the differential of $x \mapsto x^i$ in a moving frame
$(e_1(x),\dots,e_n(x))$, that is, $dx^i = e_i^*(x)$. Hence, any $p$-form $\omega$ on
$U \subseteq \mathbb{R}^n$ takes the shape
$$\omega = \sum_{1\leq i_1<\dots<i_p\leq n}\underbrace{\omega_{i_1\dots i_p}}_{\in\ C^\infty(U)}dx^{i_1}\wedge\dots\wedge dx^{i_p} = \sum_I \omega_I\,dx^I$$
with **exterior derivative** ("äussere Ableitung"):
$$d\omega = \sum_I d\omega_I\wedge dx^I.$$

#### Examples *(Corsin pp. 14–15)*

**0.** $f \in C^\infty(\mathbb{R}^n) = \Omega^0(\mathbb{R}^n)$:
$$
\begin{aligned}
df_x(v) &= \left(\frac{\partial f}{\partial x^1}\ \Big|\ \cdots\ \Big|\ \frac{\partial f}{\partial x^n}\right)\begin{pmatrix}v^1\\\vdots\\v^n\end{pmatrix} \\
&= \frac{\partial f}{\partial x^1}v^1 + \dots + \frac{\partial f}{\partial x^n}v^n \\
&= \frac{\partial f}{\partial x^1}dx^1(v) + \dots + \frac{\partial f}{\partial x^n}dx^n(v)
\end{aligned}
$$
so:
$$df = \frac{\partial f}{\partial x^1}dx^1 + \dots + \frac{\partial f}{\partial x^n}dx^n = \langle\nabla f,\ \cdot\rangle \qquad \text{(Stokes} \implies \text{FTC)}$$

**1.** Define a 1-form on $U \subseteq \mathbb{R}^3$:
$$\omega(x,y,z) = \langle F(x,y,z),\ \cdot\rangle = F^1\,dx + F^2\,dy + F^3\,dz$$
then:
$$
\begin{aligned}
d\omega ={}& dF^1\wedge dx + dF^2\wedge dy + dF^3\wedge dz \\
={}& (\partial_xF^1\,dx + \partial_yF^1\,dy + \partial_zF^1\,dz)\wedge dx \\
&+ (\partial_xF^2\,dx + \partial_yF^2\,dy + \partial_zF^2\,dz)\wedge dy \\
&+ (\partial_xF^3\,dx + \partial_yF^3\,dy + \partial_zF^3\,dz)\wedge dz
\end{aligned}
$$
*(Corsin p. 15)*
$$
\begin{aligned}
={}& \partial_yF^1\,dy\wedge dx + \partial_zF^1\,dz\wedge dx \\
&+ \partial_xF^2\,dx\wedge dy + \partial_zF^2\,dz\wedge dy \\
&+ \partial_xF^3\,dx\wedge dz + \partial_yF^3\,dy\wedge dz \\
={}& \left(\frac{\partial F^3}{\partial y} - \frac{\partial F^2}{\partial z}\right)dy\wedge dz + \left(\frac{\partial F^1}{\partial z} - \frac{\partial F^3}{\partial x}\right)dz\wedge dx + \left(\frac{\partial F^2}{\partial x} - \frac{\partial F^1}{\partial y}\right)dx\wedge dy \\
={}& \langle\nabla\times F,\ \cdot\times\cdot\rangle \\
={}& \det\big(\nabla\times F\mid\cdot\mid\cdot\big)
\end{aligned}
$$

> **The punchline.** $d$ on a 0-form is the **gradient**; $d$ on a 1-form in $\mathbb{R}^3$ is the
> **curl**; and (next week) $d$ on the $(n-1)$-form $\omega_F^{n-1}$ is the **divergence**. All
> three classical operators are the same operator in different degrees — which is why Stokes'
> theorem subsumes FTC, Green and Gauss. Worth a `summary` environment in the typeset version.

---

## German glossary contributed by this week

| English | German |
|---|---|
| differential form | Differentialform |
| alternating / antisymmetric | alternierend / antisymmetrisch |
| multilinear | multilinear |
| wedge product | Dachprodukt, äusseres Produkt |
| covector | Kovektor |
| exterior derivative | äussere Ableitung |
| curl | Rotation |
| reparametrization | Umparametrisierung |
| heat equation | Wärmeleitungsgleichung |
