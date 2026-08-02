# Week 8 — Mid-Semester Repetition, Multivariate Integration & Feynman's Trick

**Primary source:** `Corsin Nick/Class Notes/Week 8.pdf` (13 pp)
**Exercise sheet:** `exercises/Ex8_Analysis2_eng.pdf` (solutions: `Sol8_Analysis2_eng.pdf`)
**Lecture notes:** ch. 13 (sheet 8 cites *Definition 13.10* for $\mu_{\text{out}}$ and *Definition 13.18* for Jordan-null sets)
**Status:** transcribed ☑ · figures logged ☑ · supplements merged ☐ · LaTeX ☐

> Conventions: `docs/04-style-guide.md`. Every block carries a page pointer
> `*(Corsin p. N)*`. Figures are stubs logged in `docs/05-figure-queue.md`.
> Uncertain readings `⟨?word⟩` + an entry in `docs/06-open-questions.md`.

> **Structure of this week.** Half the file is a **mid-semester repetition quiz** (pp. 2–6), run
> as a Kahoot, credited by Corsin to *Prof. Serra* and *Prof. Lang*. Colour code on the page:
> green ▧ = correct, red ▨ = incorrect. The second half (pp. 7–13) starts multivariate
> integration and ends with **Feynman's trick**, which is not on any problem sheet — it is
> Corsin's own addition and one of the highlights of his notes.
>
> Kahoot link as given on p. 2:
> <https://create.kahoot.it/share/mid-semester-repetition-ana2/a3ad53cb-deae-4aab-8d76-d9fdd08a0616>

> **No session split.** No `Monday`/`Friday` boxes in this file.

---

## Exercise sheet 8

*Statements quoted verbatim from `exercises/Ex8_Analysis2_eng.pdf` (assigned 10 April 2026,
due 20 April 2026). Attribution: Prof. Joaquim Serra, D-MATH, ETH Zürich.*

### Corsin's recommendations *(Corsin p. 1)*

| Problem | Priority | Corsin's note |
|---|---|---|
| 8.1 | **semi-important** | — |
| 8.2 | **important** | — |
| 8.3 | **semi-important** | — |
| 8.4 | **important** | — |
| 8.5 | **important** | "If you don't have much time, try to definitely do this exercise!" |
| 8.6 | **optional** | — |

### 8.1 — Jordan-null set *(semi-important)*

Let $X \subset \mathbb{R}$ be a Jordan-null set (as in *Definition 13.18*).

(a) Show rigorously that $X \times X \subset \mathbb{R}^2$ is also Jordan-null.
(b) Show rigorously that $X \times [0,1] \subset \mathbb{R}^2$ is also Jordan-null.

### 8.2 — True or False *(important)*

1. A bounded countable set is always Jordan-null.
2. A countable set is always Lebesgue-null.
3. Let $D \subset [0,1]$ be a dense set (i.e. $\overline{D} = [0,1]$). Then $\mu_{\text{out}}(D) = 1$.
   ($\mu_{\text{out}}$ was defined in *Definition 13.10*.)
4. Let $X, Y \subset [0,1]$ Jordan measurable sets such that $\mu(X) > 1/2$ and $\mu(Y) > 1/2$.
   Then $X \cap Y \neq \emptyset$.
5. Let $X, Y \subset [0,1]$ such that $\mu_{\text{out}}(X) > 1/2$ and $\mu_{\text{out}}(Y) > 1/2$.
   Then $X \cap Y \neq \emptyset$.

*Official hint:* **8.2.5** — $\mu_{\text{out}}$ can be positive and large on very sparse sets.

### 8.3 — Fat boundary *(semi-important)*

Construct an open subset $U \subset \mathbb{R}$ for which the boundary $\partial U$ is **not** a
null set.

*Official hint:* any open subset of $\mathbb{R}$ is a union of disjoint open intervals. Try to
achieve that $U$ has a very small "total volume", but still contains all rational numbers in
$[0,1]$.

### 8.4 — Multiple choice *(important)*

Let $U \subset \mathbb{R}^n$ be a nonempty, open subset, $f : U \to \mathbb{R}^m$ a function, and
$N \subset U$ a Jordan null set. In which of the following cases is the image
$f(N) \subset \mathbb{R}^m$ necessarily a null set? **Attention: only one answer is correct!**

1. If $f$ is uniformly continuous.
2. If $f$ is uniformly continuous and $m \geq n$.
3. If $f$ is locally Lipschitz continuous.
4. If $f$ is locally Lipschitz continuous and $m \geq n$.

### 8.5 — Change of variables and Jacobians *(important — "if you don't have much time, definitely do this one")*

For each of the following domains and change of variables find the Jacobian and the appropriate
transformed domain. There is no need to actually compute the integrals!

1. $A := \{(x_1,x_2)\in\mathbb{R}^2 : x_1 > 0,\ x_2 < x_1,\ 1 < x_1^2+x_2^2 < 4\}$ and
   $x_1 = r\cos\theta$, $x_2 = r\sin\theta$. Complete the dots:
   $$\int_A x_1^2\sin(x_2)\,dx_1dx_2 = \int_{\dots}\dots\,dr\,d\theta$$
2. $B := \{(x,y)\in\mathbb{R}^2 \mid 1 < xy < 2,\ x^2 < y < 2x^2\}$ and $u := xy$, $v := x^2$.
   Complete the dots:
   $$\int_B y^2e^{-xy}\,dx\,dy = \int_{\dots}\dots\,du\,dv$$
3. $C := \{(x,y,z)\in\mathbb{R}^3 \mid 1 < z-2y < 2,\ 0 < z < 1,\ -2 < 3x+y+z < 0\}$ and $u := z$,
   $v := z-2y$, $w := 3x+y+z$. Complete the dots:
   $$\int_C xyz\,dx\,dy = \int_{\dots}\dots\,du\,dv\,dw$$

> **Ties into the class notes:** Corsin's worked example on pp. 8–10 is problem **2** in disguise
> — same trick, different exponents.

### 8.6 — The Cantor set **(\*)** *(optional)*

Let $X \subset [0,1]$ be the set of all real numbers whose decimal expansion does not contain the
digit 8.¹ Show that:

1. $X$ is a Lebesgue null set,
2. $X$ is uncountable,
3. $X \times X \subset [0,1]^2$ is a Lebesgue null set,
4. $X$ is compact (the choice made in the footnote matters!).

*¹ Footnote in the original sheet: the decimal expansion is not always unique — for example
$0.8 = 0.7999\dots$. Whenever $x$ has at least one decimal expansion not containing 8, we rule
that $x$ **belongs** to $X$; so for example $0.3257\overline{9} \in X$, $0.3258\overline{9} \in X$.*

---

## Mid-semester repetition

*(Corsin pp. 2–6)* — quiz questions credited to Prof. Serra and Prof. Lang.
Green = correct statement, red = incorrect statement.

### Question 1 *(Corsin p. 2)*

Let $U := \{(x,y)\in\mathbb{R}^2 : 1 \leq x^2+y^2 \leq 4\}$ and $f(x,y) = \sin(xy) - y^4$.

- ✅ **Then $f(U) = [a,b]$ for some $a < b$.**
  $U$ is compact and connected, $f$ is continuous, so $f(U) \subseteq \mathbb{R}$ is compact and
  connected $\implies [a,b]$.
- ❌ $f(U)$ is disconnected and closed with two connected components.

### Question 2 *(Corsin p. 2)*

Let $X \subseteq \mathbb{R}^2$ with $X \neq \mathbb{R}^2$, $X \neq \emptyset$. If $X$ is complete,
then it is closed.

✅ **True.** Let $(a_n)_{n=0}^{\infty}$ be a convergent sequence with elements in $X$. Then
$(a_n)$ is Cauchy and by completeness has a limit point in $X$. So $X$ is sequentially closed.

### Question 3 *(Corsin p. 3)*

Let $X \subseteq \mathbb{R}^2$ as above. If $X$ is not open, then it is closed.

❌ **False.**

### Question 4 *(Corsin p. 3)*

Let $f(x,y,z) = \dfrac{xy^2}{x^2+y^2+z^2}$ for $(x,y,z) \neq 0$ and $f(0,0,0) = 0$. Then
$f \in C^1(\mathbb{R}^3)$.

❌ **False.** We compute
$$\partial_x f = \frac{y^2}{x^2+y^2+z^2} - 2\frac{x^2y^2}{(x^2+y^2+z^2)^2}.$$
In polar coordinates:
$$\partial_x f = \sin^2\theta\sin^2\varphi - 2\sin^4\theta\cos^2\varphi\sin^2\varphi.$$
The limit $\lim_{r\to 0}\partial_x f(r,\theta,\varphi)$ is therefore ill-defined and
$\partial_x f$ is not sequentially continuous.

### Question 5 *(Corsin pp. 3–4)*

Let $f \in C^\infty(\mathbb{R}^3)$ and $\alpha \in \mathbb{R}$ such that
$$\nabla f(0) = (0,0,0), \qquad \mathcal{H}f(0) = \begin{pmatrix}1 & \alpha & 0 \\ \alpha & 2 & 0 \\ 0 & 0 & 1\end{pmatrix}.$$
**Which of the following is FALSE?** *(the correct answer to the quiz is marked green)*

- ❌ *(true statement)* For all $\alpha \in \mathbb{R}$, $0$ is **not** a local maximum point for
  $f$. — True, since clearly $1 > 0$ is an eigenvalue of $\mathcal{H}f(0)$ for any choice of
  $\alpha$.
- ❌ *(true statement)* For $\alpha > \sqrt{2}$, $0$ is a saddle point. — Let
  $\lambda_1,\lambda_2,\lambda_3 = 1$ be the eigenvalues of $\mathcal{H}f(0)$. Then
  $$\lambda_1\lambda_2 = \det(\mathcal{H}f(0)) = 2-\alpha^2 < 0 \quad \text{for } \alpha > \sqrt2,$$
  so $\mathcal{H}f(0)$ has both positive and negative eigenvalues $\implies 0$ is a saddle point.
- ❌ *(true statement)* For $\alpha \neq \sqrt2$, $\nabla f : \mathbb{R}^3\to\mathbb{R}^3$ is a
  local diffeomorphism around $0$. — For these values $\det(\mathcal{H}f(0)) \neq 0$ and therefore
  the **inverse function theorem** applies. Note that $\mathcal{H}f(0) = D(\nabla f)_0$.
- ✅ **THE FALSE ONE:** For $\alpha < \sqrt2$, $0$ is a local minimum point of $f$. — This
  statement is false because the same reasoning as above gives that for
  $\alpha < -\sqrt2 < \sqrt2$, $0$ is a saddle point of $f$.

> ⚠️ **Check:** the third bullet should read $\alpha \neq \pm\sqrt2$ — $\det \mathcal{H}f(0) = 2-\alpha^2$
> also vanishes at $\alpha = -\sqrt2$. Same oversight the fourth bullet then exploits.
> See `OQ-18`.

### Question 6 *(Corsin p. 5)*

Let $V = \{(x,y)\in\mathbb{R}^2 : y^4+y^2 = x^3+x\}$. Then…

- ✅ **$V$ is a graph over $y$ in a neighbourhood of $(0,0)$.**
  Notice that $V = f^{-1}\{0\}$ for $f(x,y) = y^4+y^2-x^3-x$. Then
  $$Jf(x,y) = (\partial_xf,\ \partial_yf) = (-3x^2-1,\ 4y^3+2y)$$
  and so $Jf(0,0) = (-1, 0)$. By the implicit function theorem, in a neighbourhood of $(0,0)$ it
  holds that
  $$(x,y) \in V \iff f(x,y) = 0 \iff x \equiv x(y).$$
  The theorem however does **not** apply for $y$.
- ❌ $V$ is a graph over $x$ in a neighbourhood of $(0,0)$. — We solve for $y^2$:
  $$y^2 = -\tfrac{1}{2} + \sqrt{\tfrac{1}{4} + x^3 + x}$$
  which has no solution for $x \in (-\varepsilon, 0)$.

### Question 7 *(Corsin p. 6)*

Let $\gamma : I \to \mathbb{R}^2$ be injective and smooth, $I$ an open interval. Then $\gamma(I)$
is a smooth submanifold of $\mathbb{R}^2$.

❌ **False.** Consider
$$\gamma : (0,2\pi) \to \mathbb{R}^2, \qquad t \mapsto (\sin t,\ \sin 2t).$$
There is no graphical representation of $\operatorname{Im}(\gamma)$ around $(0,0)$.

> **[FIG-W08-01]** *(Corsin p. 6)* The figure-eight (lemniscate-like) curve
> $t\mapsto(\sin t, \sin 2t)$ on $[-1,1]^2$ axes, with a red dashed circle around the
> self-intersection at the origin annotated "problems!". → pgfplots parametric plot + annotation.

> This is exactly why the local-parametrization theorem (Week 7, p. 5) requires $f$ to be a
> **homeomorphism** onto its image, not merely injective — the inverse fails to be continuous at
> the crossing point.

---

## Multivariate integration

### Change of variables

*(Corsin p. 7)*

Suppose $U, V \subseteq \mathbb{R}^n$ are open sets, $\Phi : U \to V$ is a $C^1$-diffeomorphism.
If $A \subseteq U$ is **Jordan measurable** ("Jordan-messbar") with $\overline{A} \subseteq U$,
and $f : A \to \mathbb{R}$ is continuous, then
$$\int_A f(x)\,dx = \int_{\Phi(A)} \frac{f\circ\Phi^{-1}(y)}{\big|\det J\Phi(\Phi^{-1}(y))\big|}\,dy.$$

### Fubini's theorem

*(Corsin p. 7)*

Let $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$ be intervals ("boxes"). Let
$f : X\times Y \to \mathbb{R}$, $(x,y)\mapsto f(x,y)$ be continuous. Then
$$\int_{X\times Y} f(x,y)\,dx\,dy = \int_X\left(\int_Y f(x,y)\,dy\right)dx = \int_Y\left(\int_X f(x,y)\,dx\right)dy,$$
where we look at the expression in brackets as a function, e.g.
$x \mapsto \int_Y f(x,y)\,dy$.

#### Examples *(Corsin p. 8)*

**1.**
$$
\begin{aligned}
\int_{[0,1]^2} x^{y+1}\,dx\,dy &= \int_0^1 dy \int_0^1 dx\ x^{y+1} \\
&= \int_0^1 dy\left[\frac{x^{y+2}}{y+2}\right]_0^1 \\
&= \int_0^1 dy\ \frac{1}{y+2} \\
&= \log|y+2|\Big|_0^1 \\
&= \log\!\left(\tfrac{3}{2}\right)
\end{aligned}
$$

> ⚠️ **Check:** the first line writes $\int_0^1 dx\int_0^1 dy\ x^{y+1}$, but the inner
> antiderivative taken is with respect to $x$. The order of the differentials is swapped
> relative to the computation; the result is correct. See `OQ-19`.

**2.**
$$\int_A \frac{y}{\sqrt{x}}\,dy\,dx, \qquad A = \left\{(x,y)\in\mathbb{R}^2 : \begin{array}{l} x,y > 0 \\ 1 \leq \frac{y}{\sqrt{x}} \leq 2 \\ 1 \leq xy \leq 2\end{array}\right\}$$

This is not easily integrated with Fubini alone. But we can apply a transformation of variables to
simplify the integration domain $A$:

*(Corsin p. 9)*
$$\Phi : U \to V, \qquad \begin{pmatrix}x\\y\end{pmatrix} \mapsto \begin{pmatrix}u(x,y)\\v(x,y)\end{pmatrix} = \begin{pmatrix}\frac{y}{\sqrt{x}}\\ xy\end{pmatrix}$$
*(with $V$ to be determined; it must be open.)*

**Check injectivity.** For $x, y > 0$, suppose
$$\text{(1) } \frac{y}{\sqrt{x}} = \frac{y'}{\sqrt{x'}}, \qquad \text{(2) } xy = x'y'.$$
Then from (2): $\dfrac{x}{x'} = \dfrac{y'}{y}$. Inserting into (1):
$$\frac{1}{\sqrt{x}} = \frac{y'}{y}\frac{1}{\sqrt{x'}} = \frac{x}{x'}\frac{1}{\sqrt{x'}} \implies x^{3/2} = (x')^{3/2} \implies x = x' \implies \frac{y'}{y} = \frac{x}{x'} = 1.$$
So for $U = (0,\infty)^2$, $V = \Phi(U)$, $\Phi$ is a bijection between open sets.

We calculate the functional determinant $|\det J\Phi|$. If it is strictly positive, we can proceed
with a change of variables, since $\Phi$ is then a local diffeomorphism and a bijection, thus a
diffeomorphism. *(Corsin p. 10)*
$$J\Phi(x,y) = \begin{pmatrix} -\dfrac{y}{2\sqrt{x}^3} & \dfrac{1}{\sqrt{x}} \\[2ex] y & x\end{pmatrix}$$
such that
$$\big|\det J\Phi(x,y)\big| = \left|-\frac{3}{2}\frac{y}{\sqrt{x}}\right| = \frac{3}{2}\frac{y}{\sqrt{x}} = \frac{3}{2}u(x,y).$$
So $\Phi$ is a diffeomorphism and $du\,dv = \tfrac{3}{2}u\,dx\,dy$. Furthermore, by design,
$$\Phi(A) = (1,2)^2.$$
So with change of variables:
$$\int_A \frac{y}{\sqrt{x}}\,dy\,dx = \int_{(1,2)^2} u\,\frac{1}{\tfrac{3}{2}u}\,du\,dv \overset{\text{Fubini}}{=} \frac{2}{3}\int_1^2 dv\int_1^2 du = \frac{2}{3}.$$

*(Corsin p. 10)* We now want to look at a powerful new integration technique using **ODEs**.

## Feynman's trick

*(Corsin p. 11)*

Let $U \subseteq \mathbb{R}^n\times\mathbb{R}$ be open, $f \in C^1(U)$ and $K \subseteq \mathbb{R}^n$
compact such that $K \times [a,b] \subseteq U$. Then the function
$$(a,b) \to \mathbb{R}, \qquad y \mapsto \int_K f(x,y)\,dx$$
is **continuously differentiable** and
$$\frac{d}{dy}\int_K f(x,y)\,dx = \int_K \frac{\partial}{\partial y}f(x,y)\,dx$$
for all $y \in (a,b)$.

### Example *(Corsin pp. 11–13)*

We want to compute the integral
$$I(1) = \int_0^1 \frac{\log(1+x)}{1+x^2}\,dx.$$
By introducing a parameter $\alpha \in (-1,1)$:
$$I(\alpha) = \int_0^1 \frac{\log(1+\alpha x)}{1+x^2}\,dx.$$
Note that the integrand is a $C^1$ function on
$U := \big(-\tfrac{1}{1+\varepsilon}, \tfrac{1}{\varepsilon}\big)_x \times (-\varepsilon, 1+\varepsilon)_\alpha$
and $K = [0,1]\times[0,1] \subseteq U$ for $0 < \varepsilon < 1$ (pay attention to the logarithm!),
so we may **differentiate under the integral**!

*(Corsin p. 12)* We obtain an ordinary differential equation:
$$
\begin{aligned}
I'(\alpha) &= \frac{d}{d\alpha}\int_0^1 \frac{\log(1+\alpha x)}{1+x^2}\,dx \\
&= \int_0^1 \frac{x}{(1+\alpha x)(1+x^2)}\,dx \\
&= \left(\int_0^1 \frac{-\alpha}{1+\alpha x} + \frac{x+\alpha}{1+x^2}\right)\frac{1}{1+\alpha^2}
\end{aligned}
$$

*Partial fractions.* From $A + Ax^2 + Bx + B\alpha x^2 + C + C\alpha x = x$:
$$-A = C, \qquad -\tfrac{A}{\alpha} = B, \qquad B + C\alpha = 1 \implies -\tfrac{A}{\alpha} - A\alpha = 1$$
$$\implies A = -\frac{\alpha}{1+\alpha^2}, \qquad B = \frac{1}{1+\alpha^2}, \qquad C = \frac{\alpha}{1+\alpha^2}$$

$$
\begin{aligned}
I'(\alpha) &= \frac{1}{1+\alpha^2}\Big[-\log(1+\alpha x) + \tfrac{1}{2}\log(1+x^2) + \alpha\arctan(x)\Big]_0^1 \\
&= \frac{1}{1+\alpha^2}\Big[\log\sqrt{2} + \frac{\alpha\pi}{4} - \log(1+\alpha)\Big]
\end{aligned}
$$

*(Corsin p. 13)* With initial value
$$I(0) = \int_0^1 \frac{\log(1)}{1+x^2}\,dx = 0,$$
we obtain from the fundamental theorem of calculus:
$$
\begin{aligned}
\int_0^1 \frac{\log(1+x)}{1+x^2}\,dx = I(1) &= I(1) - I(0) \\
&= \int_0^1\left(\frac{\log\sqrt2}{1+\alpha^2} + \frac{\pi}{4}\frac{\alpha}{1+\alpha^2} - \underbrace{\frac{\log(1+\alpha)}{1+\alpha^2}}_{\text{integrates to } I(1)}\right)d\alpha
\end{aligned}
$$
so that $2I(1) = \int_0^1\left(\frac{\log\sqrt2}{1+\alpha^2} + \frac{\pi}{4}\frac{\alpha}{1+\alpha^2}\right)d\alpha$, hence
$$
\begin{aligned}
I(1) &= \frac{1}{2}\Big[\log\sqrt2\,\arctan(\alpha) + \frac{\pi}{8}\log(1+\alpha^2)\Big]_0^1 \\
&= \frac{1}{2}\left(\frac{\pi\log\sqrt2}{4} + \frac{\pi\log\sqrt2}{4}\right) \\
&= \boxed{\ \frac{\pi\log\sqrt2}{4} = \frac{\pi\log 2}{8}\ }
\end{aligned}
$$

> ⚠️ **Check:** the source writes $\frac{\pi}{2}\frac{\alpha}{1+\alpha^2}$ in the integrand and
> $\frac{\pi}{4}\log(1+\alpha^2)$ after integrating — both off by a factor 2 relative to
> $I'(\alpha)$, whose $\alpha$-term is $\frac{\alpha\pi}{4}$. The two slips are consistent with
> each other but not with the line above, and the **final answer is correct** (and matches the
> known value $\tfrac{\pi\log2}{8}$). Corrected to $\frac{\pi}{4}\frac{\alpha}{1+\alpha^2}$ and
> $\frac{\pi}{8}\log(1+\alpha^2)$, which makes the two bracket terms genuinely equal as he claims.
> See `OQ-17`.

> **Not on any problem sheet.** Feynman's trick is Corsin's own addition. Worth marking as such
> in the typeset version — perhaps with a `remark` environment noting it is enrichment rather
> than examinable material.

---

## German glossary contributed by this week

| English | German |
|---|---|
| Jordan measurable | Jordan-messbar |
| Jordan measure | Jordan-Maß |
| null set | Nullmenge |
| change of variables | Variablenwechsel, Substitution |
| functional determinant | Funktionaldeterminante |
| Fubini's theorem | Satz von Fubini |
| differentiation under the integral sign | Differentiation unter dem Integral |
| fundamental theorem of calculus | Hauptsatz der Differential- und Integralrechnung |
