# Week 4 — The Differential, the Chain Rule & Taylor Expansions

**Primary source:** `Corsin Nick/Class Notes/Week 4.pdf` (13 pp)
**Exercise sheet:** `exercises/Ex4_Analysis2_eng.pdf` (solutions: `Sol4_Analysis2_eng.pdf`)
**Lecture notes:** ch. 10
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **Title note.** Corsin covers **Taylor expansions** already on Friday of Week 4, one week
> earlier than the provisional topic map predicted. His Week 5 then opens directly with
> optimization. `docs/03-topic-index.md` has been corrected accordingly.

> **First priority page.** Week 4 is where Corsin's colour-coded *Recommended exercises* page
> begins. It recurs in every later file.

---

## Exercise sheet 4

*Statements quoted verbatim from `exercises/Ex4_Analysis2_eng.pdf` (assigned 9 March 2026,
due 16 March 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

Colour key, as given on the page: **blue ▨ = important**, **orange ▨ = semi-important**,
**red ▨ = optional**.

| Problem | Priority | Corsin's note |
|---|---|---|
| 4.1 | **important** | "Use the chain rule" |
| 4.2 | **important** | "Recall that path connected ⟹ connected" |
| 4.3 | **semi-important** — parts 1, 2, 3, 5; parts **4 and 6 important** | "For 3., use Cauchy–Schwarz in $\mathbb{R}^n$ applied to convenient vectors." |
| 4.4 | **optional** | — |
| 4.5 | **optional** | — |
| 4.6 | **important** — parts 1, 2, 3 | — |

> Contact given on the page: `conick@ethz.ch`.

### 4.1 — Derivative computation *(important)*

Consider the function $u : (x,y) \mapsto x^{\sin(y)}$, defined for
$(x,y) \in (0,\infty)\times\mathbb{R} \subset \mathbb{R}^2$. Compute $\partial_x u$ and
$\partial_y u$.

### 4.2 — Connected graphs *(important)*

Let $U \subset \mathbb{R}^n$ be open and connected and let $f \in C^1(U, \mathbb{R}^m)$. Show that
its graph
$$\Gamma_f := \{(x, f(x)) : x \in U\}$$
is a connected subset of $\mathbb{R}^n \times \mathbb{R}^m$.

### 4.3 — $p$-norms *(semi-important; parts 4 and 6 important)*

For $p \geq 1$ and $x \in \mathbb{R}^n$ define the **$p$-norm** of $x$ as
$$|x|_p := \Big(\sum_{i=1}^{n} |x_i|^p\Big)^{1/p}.$$

1. For $n = 2$ and $p = 1, 2, 10$ sketch the sets $\{x \in \mathbb{R}^2 : |x|_p \leq 1\}$.
2. For a given $x \in \mathbb{R}^n$, compute the limit $|x|_\infty := \lim_{p\to\infty}|x|_p$.
3. Using an appropriate inequality that you have seen in class, prove that
   $$\Big(\sum_{i=1}^{n} a_i^{p-1}b_i\Big)^2 \leq \Big(\sum_{i=1}^{n}a_i^p\Big)\Big(\sum_{i=1}^{n}a_i^{p-2}b_i^2\Big),$$
   whenever $a_i, b_i$ are $n$-tuples of positive numbers.
4. Fix $x, y \in \mathbb{R}^n$ and consider the function $f : [0,1] \to \mathbb{R}$ defined as
   $$f(t) := |tx + (1-t)y|_p = \Big(\sum_{i=1}^{n}|tx_i + (1-t)y_i|^p\Big)^{1/p}. \tag{1}$$
   Show that $f$ is convex. You may assume that the coordinates of $x$ and $y$ are all strictly
   positive and use the inequality of the previous point.
5. Deduce from the previous point that the triangular inequality holds, i.e.
   $|x+y|_p \leq |x|_p + |y|_p$ for all $x,y \in \mathbb{R}^n$.
6. What happens for $p \in (0,1)$?

*Official hints:* **4.3.3** — use Cauchy–Schwarz and the fact that
$a_i^{p-1}b_i = a_i^{p/2}\cdot a_i^{(p-2)/2}b_i$. **4.3.4** — show that $f''(t) \geq 0$; it is not
the simplest derivative, but if you get it right the inequality in 4.3.3 will be just what you
need. **4.3.5** — write the convexity inequality between $x$, $y$ and the middle point
$(x+y)/2$. To get the general case from the one with positive coordinates, observe that for
$x \in \mathbb{R}^n$, denoting $\hat x := (|x_1|,\dots,|x_n|)$, we have
$|x+y|_p \leq |\hat x + \hat y|_p$ and $|\hat x|_p = |x|_p$ for all $x,y \in \mathbb{R}^n$.

### 4.4 — $p$-means *(optional)*

For $x \in \mathbb{R}^n$ with positive coordinates and $p \neq 0$ define the **$p$-mean** as
$$\mu_p(x) := \left(\frac{x_1^p + \dots + x_n^p}{n}\right)^{1/p}.$$

1. Compute the limits $p \to \pm\infty$, $p \to 0$ and define accordingly $\mu_{-\infty}(x)$,
   $\mu_0(x)$, $\mu_{+\infty}(x)$.
2. For any $n$-tuple of numbers $a_i > 0$ show that
   $$\sum_{i=1}^{n} \frac{a_i\log(a_i)}{a_1 + \dots + a_n} \geq \log\left(\frac{a_1 \dots + a_n}{n}\right).$$
3. For a fixed $x$, show that the function $f : \mathbb{R}\to\mathbb{R}$, given by
   $f(t) := \mu_t(x)$, is continuous and increasing.
4. Prove the Arithmetic–Geometric inequality and Arithmetic–Quadratic inequality:
   $$n(x_1x_2\cdots x_n)^{1/n} \leq x_1 + \dots + x_n, \qquad (x_1+\dots+x_n)^2 \leq n(x_1^2+\dots+x_n^2).$$
5. **(\*)** Is $f$ continuously differentiable in the whole $\mathbb{R}$?

*Official hints:* **4.4.2** — combine the concavity of $\log(\cdot)$ and the Cauchy–Schwarz
inequality; use the generalisation of the concavity inequality: for any concave
$f : \mathbb{R}\to\mathbb{R}$,
$f(\lambda_1x_1 + \dots + \lambda_nx_n) \geq \lambda_1f(x_1)+\dots+\lambda_nf(x_n)$ for all
$x_i \in \mathbb{R}$, $0 \leq \lambda_i \leq 1$ with $\lambda_1+\dots+\lambda_n = 1$.
**4.4.3** — it might be more convenient to work with $\log f(t)$.

### 4.5 — Mean value for vector-valued functions *(optional)*

Let $f \in C^1(\mathbb{R},\mathbb{R}^m)$ for $m > 1$. Is it true that there is $t \in [0,1]$ such
that
$$f(1) - f(0) = Df_t(1) = \begin{pmatrix} f_1'(t) \\ \vdots \\ f_m'(t) \end{pmatrix}?$$
Prove it or provide a counterexample.

*Official hint:* try $f(t) = (\sin(2\pi t), \cos(2\pi t))$.

### 4.6 — A directional derivative vanishes *(important)*

Let $u \in C^1(\mathbb{R}^n)$ and $\nu \in \mathbb{R}^n$. Show that

1. If $\partial_1 u \equiv 0$ then "$u$ does not depend on $x_1$"; more rigorously: there exists a
   unique function $v \in C^1(\mathbb{R}^{n-1})$ such that
   $$u(x_1,\dots,x_n) = v(x_2,\dots,x_n) \quad \text{for all } x \in \mathbb{R}^n. \tag{2}$$
2. If $\partial_\nu u \equiv 0$ and $\nu\cdot e_1 \neq 0$ then "$u$ is a function of $n-1$
   variables"; more rigorously: there exists a unique function $w \in C^1(\mathbb{R}^{n-1})$ such
   that
   $$u(x_1,\dots,x_n) = w\!\left(x_2 - \frac{x_1\nu_2}{\nu_1}, \dots, x_n - \frac{x_1\nu_n}{\nu_1}\right) \quad \text{for all } x \in \mathbb{R}^n.$$
3. **(\*)** What can we conclude if we assume only that $\partial_1 u = 0$ in an open connected
   subset $U \subset \mathbb{R}^n$?

*Official hints:* **4.6.2** — apply the mean value theorem to $u(x + t\nu)$. **4.6.3** — consider
the domain $U := \{(x,y) : x^2 < y < x^2+1\}$ and the function
$$u(x,y) := \begin{cases} \max\{0, y-2\}^2 & \text{if } x \geq 0, \\ 0 & \text{if } x \leq 0.\end{cases}$$

---

## Monday

### The differential

*(Corsin p. 2)*

**For $f : \mathbb{R}\to\mathbb{R}$ differentiable at $x_0 \in \mathbb{R}$:**
$$f(x_0+h) = f(x_0) + f'(x_0)h + o(h)$$
$$\Updownarrow$$
$$\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h} = f'(x_0)$$
$$\Updownarrow$$
$$\lim_{h\to 0}\left|\frac{f(x_0+h)-f(x_0)-f'(x_0)h}{h}\right| = 0$$

**For $F : \mathbb{R}^n \to \mathbb{R}^m$ differentiable at $x_0 \in \mathbb{R}^n$:**
$$F(x_0+h) = F(x_0) + \underbrace{DF_{x_0}(h)}_{\text{linear map}} + o(|h|)$$
$$\Updownarrow$$
$$\lim_{h\to 0}\frac{F(x_0+h)-F(x_0)}{|h|} = DF_{x_0}\!\left(\frac{h}{|h|}\right) = \partial_{\frac{h}{|h|}}F(x_0) \quad \text{(directional derivative in direction } h)$$
$$\Updownarrow$$
$$\lim_{h\to 0}\frac{|F(x_0+h)-F(x_0)-DF_{x_0}(h)|}{|h|} = 0$$

We say that $F : \mathbb{R}^n \to \mathbb{R}^m$ is **differentiable** ("differenzierbar") at $x_0$
if a linear map $DF_{x_0}$ as above exists, where $x_0, h \in \mathbb{R}^n$.

(Of course, equivalently for $U \subseteq \mathbb{R}^n$ a subset, $F : U \to \mathbb{R}^m$.)

### The Jacobi matrix

*(Corsin p. 3)*

Since $DF_{x_0} : \mathbb{R}^n \to \mathbb{R}^m$ is a linear map, there is a **1–1 correspondence
with a matrix once a basis is fixed!** In the standard basis of $\mathbb{R}^n$,
$(e_1,\dots,e_n)$, this is the **Jacobi matrix** ("Jacobi-Matrix"):
$$DF_x \;\cong\; JF(x) = \begin{pmatrix} \dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\[1ex] \vdots & \ddots & \vdots \\[1ex] \dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n}\end{pmatrix}$$
($m$ rows, $n$ columns), where we wrote $F(x) = (F_1, \dots, F_m)^{\mathsf T}$ and
$$\frac{\partial F}{\partial x_i} =: \partial_i F(x)$$
is the **$i$-th partial derivative** ("partielle Ableitung") at $x$:
$$\partial_i F(x) = \lim_{s\to 0}\frac{F(x+se_i)-F(x)}{s}.$$
This defines a function $\partial_i F : U \to \mathbb{R}^m$. If $F$ is differentiable, then
$$\partial_i F(x) = DF_x(e_i).$$

> ⚠️ **The partial derivatives can exist even if $F : U \to \mathbb{R}^m$ is not
> differentiable!** *(Corsin p. 3, flagged with warning signs on both margins)*

#### Examples *(Corsin p. 4)*

**1. Curve.**
$$\gamma : \mathbb{R}\to\mathbb{R}^2, \qquad t \mapsto \begin{pmatrix}\cos t \\ \sin t\end{pmatrix}$$
What is $\gamma'(\tfrac{\pi}{4}) := D\gamma_{\pi/4}$?
$$\gamma'\!\left(\tfrac{\pi}{4}\right) = \begin{pmatrix}\partial_t\gamma_1(\pi/4) \\ \partial_t\gamma_2(\pi/4)\end{pmatrix} = \begin{pmatrix}-1/\sqrt{2} \\ 1/\sqrt{2}\end{pmatrix}$$

> **[FIG-W04-01]** *(Corsin p. 4)* Unit circle on axes; the point $\gamma(\pi/4)$ marked with an
> orange tangent arrow pointing up-left, and a dotted radius to the point. → TikZ 2D sketch.

This is also called the **speed of the curve**. We get that
$$\gamma\!\left(\tfrac{\pi}{4}+h\right) = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} + \frac{h}{\sqrt{2}}\begin{pmatrix}-1\\1\end{pmatrix} + o(|h|).$$

From this example, we see that the **column** vectors of the Jacobian are the partial derivatives:
$$JF(x) = \left(\frac{\partial F}{\partial x_1}\ \Big|\ \cdots\ \Big|\ \frac{\partial F}{\partial x_n}\right)$$
and therefore, in the canonical basis, with $v = (v_1,\dots,v_n)^{\mathsf T}$:
$$\partial_v F(x) = DF_x(v) = JF(x)\,v = \sum_{i=1}^{n} v_i\,\frac{\partial F}{\partial x_i}.$$

**2. Scalar field.** *(Corsin p. 5)*
$$f : \mathbb{R}^3\to\mathbb{R}, \qquad (x,y,z) \mapsto 2x^2 + y^2 + 3z^2 - 2xyz$$
What is $Jf(x,y,z)$?
$$Jf(x,y,z) = (4x - 2yz,\ 2y - 2xz,\ 6z - 2xy) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right) = (\nabla f)^{\mathsf T}$$

From this, we see that the **rows** of the Jacobian are the gradients:
$$JF(x) = \begin{pmatrix} \nabla F_1 \\ \hline \vdots \\ \hline \nabla F_m \end{pmatrix}$$

> ⚠️ **Check:** Corsin's sentence reads "the **columns** of the Jacobian are the gradients", but
> the displayed matrix stacks $\nabla F_1, \dots, \nabla F_m$ as **rows** — which is the correct
> statement, and consistent with $(\nabla f)^{\mathsf T}$ just above. Corrected to "rows".
> See `OQ-09`.

### Chain rule

*(Corsin p. 5)*

For $f : U \subseteq \mathbb{R}^n \to \mathbb{R}^m$, $g : V \subseteq \mathbb{R}^m \to \mathbb{R}^d$
differentiable, it holds:
$$D(g\circ f)(x) = Dg(f(x))\,Df(x)$$
And equivalently for the Jacobians.

#### Exercise *(Corsin p. 5)*

Compute $J(g\circ f)$ for
$$f : \mathbb{R}^3\to\mathbb{R}^2,\ x \mapsto (x_1x_2,\ x_2+x_3), \qquad g : \mathbb{R}^2\to\mathbb{R}^2,\ x \mapsto (e^{x_1},\ x_1x_2).$$

#### Solution *(Corsin p. 6)*

We have
$$Jf(x) = \begin{pmatrix} x_2 & x_1 & 0 \\ 0 & 1 & 1\end{pmatrix}, \qquad Jg(x) = \begin{pmatrix} e^{x_1} & 0 \\ x_2 & x_1 \end{pmatrix}.$$
So:
$$
\begin{aligned}
J(g\circ f) &= \begin{pmatrix} e^{x_1x_2} & 0 \\ x_2+x_3 & x_1x_2\end{pmatrix}\begin{pmatrix} x_2 & x_1 & 0 \\ 0 & 1 & 1\end{pmatrix} \\
&= \begin{pmatrix} x_2e^{x_1x_2} & x_1e^{x_1x_2} & 0 \\ x_2^2 + x_2x_3 & 2x_1x_2 + x_1x_3 & x_1x_2 \end{pmatrix}
\end{aligned}
$$

*(Corsin p. 6)* Sometimes the differential is not easily expressed as a Jacobian. Then it can be
convenient to use the formula for **directional derivatives**:
$$DF_{x_0}(v) = \partial_v F(x_0) = \left.\frac{d}{ds}\right|_{s=0} F(x_0 + sv) \tag{$*$}$$

> ⚠️ The directional derivative $\partial_v F(x_0)$ can exist (depending on $v$ and $x_0$) even if
> $F$ is not differentiable at $x_0$, i.e. $DF_{x_0}$ does not exist. However, if $DF_{x_0}$
> exists, the formula $(*)$ holds. *(Corsin p. 6, flagged with a warning sign)*

#### Exercise *(Corsin p. 7)*

We identify the inner product space of real-valued matrices $\mathbb{R}^{n\times n}$ with inner
product
$$\langle A, B\rangle = \sum_{i,j=1}^{n} A_{ij}B_{ij} = \operatorname{Tr}(A^{\mathsf T}B)$$
for $A, B \in \mathbb{R}^{n\times n}$, with the euclidean space
$\mathbb{R}^{n^2}\cong\mathbb{R}^{n\times n}$, with the standard inner product. Then, consider the
function
$$F : \mathbb{R}^{n\times n}\to\mathbb{R}^{n\times n}, \qquad A \mapsto A^{\mathsf T}A.$$
Compute the differential at the identity matrix $\operatorname{Id}\in\mathbb{R}^{n\times n}$
applied to $X \in \mathbb{R}^{n\times n}$:
$$DF_{\operatorname{Id}}(X) = \partial_X F(\operatorname{Id}).$$

#### Solution *(Corsin p. 7)*

We use $(*)$:
$$
\begin{aligned}
DF_{\operatorname{Id}}(X) &= \left.\frac{d}{ds}\right|_{s=0} F(\operatorname{Id}+sX) \\
&= \left.\frac{d}{ds}\,(\operatorname{Id}+sX)^{\mathsf T}(\operatorname{Id}+sX)\right|_{s=0} \\
&= \left.\frac{d}{ds}\left[\operatorname{Id} + s(X^{\mathsf T}+X) + s^2X^{\mathsf T}X\right]\right|_{s=0} \\
&= X^{\mathsf T} + X
\end{aligned}
$$

---

## Friday

### The chain rule along a path

*(Corsin p. 8)*

An important special case of the chain rule is that of a **composition of a scalar field with a
path**. Suppose $f : \mathbb{R}^n \supseteq U \to \mathbb{R}$ and $\gamma : [0,1]\to\mathbb{R}^n$
are a $C^1$ scalar field and path, respectively. Then
$$
\begin{aligned}
D(f\circ\gamma)(t) &= Df(\gamma(t))\cdot D\gamma(t) \\
&= \langle \nabla f(\gamma(t)),\ \gamma'(t)\rangle \\
&= \sum_{i=1}^{n} \frac{\partial f}{\partial \gamma_i}\frac{\partial \gamma_i}{\partial t}
\end{aligned}
$$
where $\gamma = (\gamma_1,\dots,\gamma_n)$ and
$\dfrac{\partial f}{\partial \gamma_i} := \partial_i f(\gamma(t))$.

This operation is so common in physics that it has its own notation: for $f$ as above, we look at
each coordinate as a function of **time** and differentiate:
$$\frac{d}{dt}f(x_1,\dots,x_n) := Df(x_1(t),\dots,x_n(t)) = \sum_{i=1}^{n}\frac{\partial f}{\partial x_i}\frac{\partial x_i}{\partial t}.$$

### Taylor expansions

*(Corsin p. 9)*

In the lecture, you have seen the following formula. For
$f \in C^k(U \subseteq \mathbb{R}^n, \mathbb{R})$, $\bar x \in U$:
$$f(\bar x + h) = \sum_{|\alpha| = 0}^{k} \partial^\alpha f(\bar x)\,\frac{h^\alpha}{\alpha!} + o(|h|^k)$$
where $\alpha$ is a **multi-index** ("Multiindex") in $\mathbb{N}^n$.

In practice, we never use this formula, but to shed some light on it:

#### Exercise *(Corsin p. 9)*

Let $f \in C^3(\mathbb{R}^2,\mathbb{R})$. Write out the maximal Taylor approximation.

#### Solution *(Corsin pp. 9–10)*

The multi-indices are:

- $|\alpha| = 0$: $\alpha = (0,0)$
- $|\beta| = 1$: $\beta_1 = (1,0)$, $\beta_2 = (0,1)$
- $|\gamma| = 2$: $\gamma_1 = (1,1)$, $\gamma_2 = (2,0)$, $\gamma_3 = (0,2)$
- $|\delta| = 3$: $\delta_1 = (3,0)$, $\delta_2 = (2,1)$, $\delta_3 = (1,2)$, $\delta_4 = (0,3)$

Recall that
$$\partial^\alpha = \partial_1^{\alpha_1}\partial_2^{\alpha_2}\cdots\partial_n^{\alpha_n}, \qquad \text{e.g. } \partial^{\delta_2} = \partial^{(2,1)} = \partial_1^2\partial_2,$$
and
$$\alpha! = \alpha_1!\cdots\alpha_n!, \qquad \text{e.g. } \gamma_2! = (2,0)! = 2\cdot 1 = 2.$$

> ⚠️ **Check:** Corsin writes the recall line as $\partial^\alpha = \partial_{\alpha_1}\partial_{\alpha_2}\cdots\partial_{\alpha_n}$
> with the example $\partial^{(2,1)} = \partial_2\partial_1$. Read literally that is the wrong
> object — a multi-index $\alpha$ records *how many times* each $\partial_i$ is applied, so
> $\partial^{(2,1)} = \partial_1^2\partial_2$. His own expansion below uses
> $\partial_1^2\partial_2 f(\bar x)\,\tfrac{h_1^2h_2}{2}$ for $\delta_2$, confirming the
> intended meaning. Corrected. See `OQ-10`.

So:
$$
\begin{aligned}
f(\bar x + h) = &\ f(\bar x) && (\alpha) \\
&+ \partial_1 f(\bar x)h_1 + \partial_2 f(\bar x)h_2 && (\beta_1, \beta_2)\\
&+ \partial_1\partial_2 f(\bar x)h_1h_2 + \partial_1^2 f(\bar x)\frac{h_1^2}{2} + \partial_2^2 f(\bar x)\frac{h_2^2}{2} && (\gamma_1, \gamma_2, \gamma_3)\\
&+ \partial_1^3 f(\bar x)\frac{h_1^3}{6} + \partial_1^2\partial_2 f(\bar x)\frac{h_1^2h_2}{2} && (\delta_1, \delta_2)\\
&+ \partial_1\partial_2^2 f(\bar x)\frac{h_1h_2^2}{2} + \partial_2^3 f(\bar x)\frac{h_2^3}{6} && (\delta_3, \delta_4)\\
&+ o(|h|^3)
\end{aligned}
$$

*(Corsin p. 11)* We can rewrite this as
$$f(\bar x + h) = \sum_{\ell=0}^{k}\frac{1}{\ell!}\big(h_1\partial_1 + h_2\partial_2\big)^\ell f(\bar x).$$

> **Taylor, "working formula"** *(Corsin p. 11, boxed in red)*
> For $f \in C^k(U \subseteq \mathbb{R}^n, \mathbb{R})$ with $\bar x + th \in U$ for all
> $t \in [0,1]$:
> $$f(\bar x + h) = \sum_{\ell=0}^{k}\frac{1}{\ell!}\left(\sum_{m=1}^{n} h_m\partial_m\right)^{\!\ell} f(\bar x) + o(|h|^k)$$

> ⚠️ **Check:** both sums are written with lower limit $\ell = 1$ in the source. The $\ell = 0$
> term is $f(\bar x)$ itself, which the explicit expansion above does include, so the lower limit
> must be $0$. Corrected. See `OQ-11`.

#### Exercise *(Corsin p. 11)*

Compute the Taylor expansion of
$$f : \mathbb{R}^2\to\mathbb{R}, \qquad (x,y) \mapsto (x+y^2)e^{-x^2-y^2}$$
around $(0,0)$ up to third order.

#### Cumbersome solution *(Corsin p. 11)*

Calculate all partial derivatives up to third order and use the definition. *(Please never do
this.)*

#### The easy solution *(Corsin pp. 11–12)*

The substitution and multiplication rules we used in Analysis 1 still apply:
$$
\begin{aligned}
(x+y^2)e^{-x^2-y^2} &= (x+y^2)\left(1 - x^2 - y^2 + o(|x^2+y^2|)\right) \\
&= x + y^2 - x^3 - xy^2 + o\!\left(|(x,y)|^3\right)
\end{aligned}
$$

#### Remark *(Corsin p. 12)*

The second-order Taylor approximation of $f \in C^2(\mathbb{R}^n,\mathbb{R})$ around
$x_0 \in \mathbb{R}^n$ can be expressed compactly as
$$f(x_0+x) = f(x_0) + \nabla f(x_0)\cdot x + \tfrac{1}{2}x^{\mathsf T}\cdot \mathcal{H}f(x_0)\cdot x + o(|x|^2)$$
where
$$\mathcal{H}f(x_0) = \big(\partial_i\partial_j f(x_0)\big)_{i,j=1,\dots,n}$$
is the **Hessian matrix** ("Hesse-Matrix") of $f$.

#### Question *(Corsin p. 12)*

For $f \in C^k(U, \mathbb{R})$, do the Taylor expansions of $t \mapsto f(x_0+th)$ in $t$ and of
$(th) \mapsto f(x_0+th)$ in $(th)$ around $0$ coincide?

#### Answer *(Corsin p. 12)*

**Yes.** This is, in fact, how we prove the multi-dimensional Taylor approximation, and why we
need the assumption $x_0 + th \in U$ for all $t \in [0,1]$.

#### Exercise *(Corsin p. 13)*

Prove the formula from above:
$$f(x_0+h) = f(x_0) + \nabla f(x_0)h + \tfrac{1}{2}h^{\mathsf T}\mathcal{H}f(x_0)h + \dots$$
for $f \in C^k(U,\mathbb{R})$ with $x_0 + th \in U$ for all $t \in [0,1]$.

#### Solution *(Corsin p. 13)*

We expand $t \mapsto f(x_0+th)$ in $t$:
$$
\begin{aligned}
f(x_0+th) &= f(x_0) + t\left.\frac{d}{dt}\right|_{t=0}f(x_0+th) + \frac{t^2}{2}\left.\frac{d^2}{dt^2}\right|_{t=0}f(x_0+th) + o(|th|^2) \\
&= f(x_0) + t\sum_{i=1}^{n}\partial_i f(x_0)h_i + \frac{t^2}{2}\frac{d}{dt}\left.\sum_{i=1}^{n}\partial_i f(x_0+th)h_i\right|_{t=0} + o(|h|^2) \\
&= f(x_0) + t\nabla f(x_0)h + \frac{t^2}{2}\sum_{i,j=1}^{n}\partial_i\partial_j f(x_0)h_ih_j + o(|th|^2) \\
&= f(x_0) + t\nabla f(x_0)h + \frac{t^2}{2}h^{\mathsf T}\mathcal{H}f(x_0)h + o(|th|^2)
\end{aligned}
$$
Setting $t = 1$ gives the result.

---

## German glossary contributed by this week

| English | German |
|---|---|
| differentiable | differenzierbar |
| the differential | das Differential |
| Jacobi matrix | Jacobi-Matrix |
| partial derivative | partielle Ableitung |
| directional derivative | Richtungsableitung |
| chain rule | Kettenregel |
| gradient | Gradient |
| multi-index | Multiindex |
| Hessian matrix | Hesse-Matrix |
| scalar field | Skalarfeld |
