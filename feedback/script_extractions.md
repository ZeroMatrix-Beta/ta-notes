# Official Script Extractions

Auf deinen ausdrücklichen Wunsch hin habe ich die Regel, keine neuen Themenbereiche aus dem Skript anzulegen, aus dem Regelwerk entfernt. Hier sind die versprochenen LaTeX-Snippets für die drei genialen Beispiele aus dem Skript (`lec_notes.pdf`), die das Projekt massiv bereichern werden!

---

## 1. Epicycloid Area via Divergence Theorem
**Source:** `lec_notes.pdf`, Example 14.22 (Page 161).
**Target Location:** In `content/23-flux-divergence/02-divergence-theorem.tex` als wunderschönes Anwendungsbeispiel.

```latex
% Source: lec_notes.pdf, Example 14.22, p. 161
% Extractor: Gemini
\begin{aiexample}[Area of an Epicycloid via the Divergence Theorem]
\label{ex:ai_epicycloid_area}
Consider the region $B \subset \mathbb{R}^2$ inside an epicycloid (the curve traced by a point on a circle rolling around the outside of another circle). For an integer $m \ge 1$, let the inner circle have radius $1$ and the rolling circle have radius $1/m$. The boundary curve $\gamma: [0, 2\pi] \to \mathbb{R}^2$ is given by:
\[ \gamma(t) = \frac{m+1}{m} \begin{pmatrix} \cos(t) \\ \sin(t) \end{pmatrix} + \frac{1}{m} \begin{pmatrix} \cos((m+1)t) \\ \sin((m+1)t) \end{pmatrix}. \]
Using the smooth vector field $F(x) = x$, we have $\operatorname{div}(F) = 2$. By the Divergence Theorem, the area is:
\[ 2 \operatorname{vol}(B) = \int_B \operatorname{div}(F) dx = \int_{\partial B} F \cdot \nu \, dL = \int_0^{2\pi} \langle \gamma(t), \nu(\gamma(t)) \rangle dt. \]
The outward normal $n_\gamma(t)$ is
\[ n_\gamma(t) = \frac{m+1}{m} \begin{pmatrix} \cos(t) \\ \sin(t) \end{pmatrix} + \frac{m+1}{m} \begin{pmatrix} \cos((m+1)t) \\ \sin((m+1)t) \end{pmatrix}. \]
Computing the scalar product $\langle \gamma(t), n_\gamma(t) \rangle$ and integrating over $[0, 2\pi]$ (noting that the cross terms integrate to zero) yields:
\[ \operatorname{vol}(B) = \frac{1}{2} \int_0^{2\pi} \langle \gamma(t), n_\gamma(t) \rangle dt = \pi \frac{(m+1)(m+2)}{m^2}. \]
For $m=1$ (the cardioid), the area is $6\pi$.
\end{aiexample}
```

---

## 2. The Courant-Fischer Theorem
**Source:** `lec_notes.pdf`, Exercise 11.22 (Page 72).
**Target Location:** In `content/13-lagrange/01-lagrange-multipliers.tex`. Es verbindet Lagrange direkt mit der Linearen Algebra!

```latex
% Source: lec_notes.pdf, Exercise 11.22, p. 72
% Extractor: Gemini
\begin{aiexercise}[The Courant-Fischer Theorem via Lagrange Multipliers]
\label{ex:ai_courant_fischer_lagrange}
Let $A \in \operatorname{Mat}_{n,n}(\mathbb{R})$ be a symmetric matrix. Show using the method of Lagrange multipliers that the minimum and maximum eigenvalues of $A$ correspond exactly to the global minimum and maximum of the quadratic form $f(x) = x^T A x$ on the unit sphere $\mathbb{S}^{n-1} = \{ x \in \mathbb{R}^n \mid x^T x = 1 \}$.
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/13-lagrange/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_courant_fischer_lagrange}]
We want to find the extrema of $f(x) = x^T A x$ subject to the constraint $g(x) = x^T x - 1 = 0$. Since $\mathbb{S}^{n-1}$ is compact and $f$ is continuous, global extrema must exist.
The gradients are $\nabla f(x) = 2Ax$ (since $A$ is symmetric) and $\nabla g(x) = 2x$.
The Lagrange multiplier condition $\nabla f(x) = \lambda \nabla g(x)$ becomes:
\[ 2Ax = \lambda 2x \implies Ax = \lambda x. \]
This is exactly the eigenvalue equation! Thus, the critical points of this constrained optimization problem are precisely the unit eigenvectors of $A$, and the Lagrange multipliers $\lambda$ are the eigenvalues.
Evaluating the objective function at a critical point $v$ gives $f(v) = v^T A v = v^T (\lambda v) = \lambda \|v\|^2 = \lambda$.
Thus, the global maximum of $f$ on the sphere is the largest eigenvalue, and the global minimum is the smallest eigenvalue.
\end{exercisesolution}
```

---

## 3. The Catenoid (Katenoid)
**Source:** `lec_notes.pdf`, Page 91.
**Target Location:** In `content/21-gram-determinant/02-volume-of-embedded-surfaces.tex`. (Ergänzend zum Torus und Möbiusband).

```latex
% Source: lec_notes.pdf, p. 91
% Extractor: Gemini
\begin{aiexample}[The Catenoid]
\label{ex:ai_catenoid_parametrization}
The catenoid is a classic example of a minimal surface in $\mathbb{R}^3$. It is the surface of revolution obtained by rotating a catenary curve (the shape of a hanging chain) around the $z$-axis. It can be parametrized by:
\begin{align*}
    x(u, v) &= \cosh(v) \cos(u), \\
    y(u, v) &= \cosh(v) \sin(u), \\
    z(u, v) &= v,
\end{align*}
where $u \in [0, 2\pi)$ and $v \in \mathbb{R}$. 
The Jacobian matrix of this parametrization is:
\[ J(u,v) = \begin{pmatrix} -\sin(u) \cosh(v) & \cos(u) \sinh(v) \\ \cos(u) \cosh(v) & \sin(u) \sinh(v) \\ 0 & 1 \end{pmatrix}. \]
This matrix has maximal rank (rank 2) everywhere, confirming that the catenoid is a regular surface (a 2-dimensional submanifold) everywhere.
\end{aiexample}
```
