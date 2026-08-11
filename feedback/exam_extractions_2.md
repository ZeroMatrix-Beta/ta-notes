# Old Exam Extractions: Lagrange Multipliers & IFT

Dieses Dokument enthält weitere LaTeX-Snippets für konzeptionelle Multiple-Choice Aufgaben aus `august2025.pdf`. Diese eignen sich hervorragend für die jeweiligen Kapitel, um das Verständnis der Studierenden zu prüfen, ohne dass sie lange Rechnungen durchführen müssen.

---

## 4. Conceptual Check: Lagrange Multipliers Trick Question
**Source:** `august2025.pdf` (Prof. Laura Kobel-Keller), Question 4.
**Target Location:** Am Ende von `content/13-lagrange/01-lagrange-multipliers.tex`

```latex
% Source: old_exams/august2025.pdf (Prof. Laura Kobel-Keller) August 2025, p. 4
% Extractor: Gemini
\begin{aiexercise}[Multiple Choice: A tricky constrained optimization problem]
\label{ex:ai_lagrange_trick_mc}
Consider a function $f(x,y,z)$ depending on three variables, of which we know that
\[ \nabla f(x,y,z) = \begin{pmatrix} e^x \\ 2y \\ 2z \end{pmatrix} \]
In addition, consider the constraint $g(x,y,z) = ay^2 + bz^2 - \pi = 0$ for some parameters $a, b \in \mathbb{R} \setminus \{0\}$. Which of the following assertions is correct?

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item Independently of the values of $a$ and $b$, the given function does not have any extremal point under the given constraint.
  \item The given constraint defines a compact set in space independently of the values of the parameters $a$ and $b$. Thus, the constrained minimum and the constrained maximum have to be achieved.
  \item In the case $a = b$, the constrained minimum is achieved.
  \item Without any further knowledge about the function $f$, it is not possible to make any further assertions about the constrained optimization problem.
\end{enumerate}
\exinfo{Adapted from the exam of August 2025 (Prof.\ Laura Kobel-Keller), Question 4.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/13-lagrange/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_lagrange_trick_mc}]
The correct answer is \textbf{(a)}.

Let's set up the Lagrange multipliers equation $\nabla f = \lambda \nabla g$. We have $\nabla g = (0, 2ay, 2bz)^T$. 
The system of equations is:
\begin{align*}
    e^x &= \lambda \cdot 0 \\
    2y &= \lambda \cdot 2ay \\
    2z &= \lambda \cdot 2bz \\
    ay^2 + bz^2 - \pi &= 0
\end{align*}
The very first equation simplifies to $e^x = 0$. Since the exponential function is strictly positive for all real numbers $x$, this equation \textbf{has no solution}. Therefore, the system of equations is inconsistent, and there can be no critical points, regardless of what $a$ and $b$ are.
\end{exercisesolution}
```

---

## 5. Conceptual Check: Inverse Function Theorem
**Source:** `august2025.pdf` (Prof. Laura Kobel-Keller), Question 5.
**Target Location:** Am Ende von `content/16-inverse-function-theorem/01-inverse-function-theorem.tex`

```latex
% Source: old_exams/august2025.pdf (Prof. Laura Kobel-Keller) August 2025, p. 5
% Extractor: Gemini
\begin{aiexercise}[Multiple Choice: Conditions for local invertibility]
\label{ex:ai_ift_conditions_mc}
We look at a function $f: \mathbb{R}^2 \to \mathbb{R}^2$ that is defined on the whole space and is twice continuously differentiable. Let $f = (f_1, f_2)^T$ and let $x, y$ be the standard coordinates on $\mathbb{R}^2$. Which of the following assertions is correct?

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item If $f$ takes values in $\mathbb{R}^n$ with $n > 2$, then locally around the origin the function is always invertible.
  \item If $f$ takes values in $\mathbb{R}^2$ and if the differential $Df$ has maximal rank at the origin, then $f$ is locally invertible around the origin.
  \item If at the origin it holds that $\frac{\partial f_1}{\partial x}(0,0) \neq 0$, then the function can be locally inverted around the origin.
  \item If at the origin it holds that $\frac{\partial f_1}{\partial y}(0,0) \neq 0$, then the function can be locally inverted around the origin.
\end{enumerate}
\exinfo{Adapted from the exam of August 2025 (Prof.\ Laura Kobel-Keller), Question 5.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/16-inverse-function-theorem/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_ift_conditions_mc}]
The correct answer is \textbf{(b)}.

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item \textbf{False.} The Inverse Function Theorem only applies when the domain and codomain have the same dimension.
  \item \textbf{True.} This is precisely the statement of the Inverse Function Theorem. For a map from $\mathbb{R}^2$ to $\mathbb{R}^2$, having maximal rank (rank 2) means the Jacobian matrix $Df$ is invertible (its determinant is non-zero).
  \item \textbf{False.} Having one non-zero partial derivative $\frac{\partial f_1}{\partial x} \neq 0$ does not imply that the $2 \times 2$ Jacobian determinant is non-zero. For example, if $f(x,y) = (x, 0)^T$, then $\frac{\partial f_1}{\partial x} = 1$, but the determinant is $0$.
  \item \textbf{False.} Same reason as (c).
\end{enumerate}
\end{exercisesolution}
```
