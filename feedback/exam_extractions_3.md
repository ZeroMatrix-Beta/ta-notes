# Old Exam Extractions: Topology, Submanifolds, Flux

Dieses Dokument enthält LaTeX-Snippets für die fantastischen Multiple-Choice Aufgaben aus `fs2023/Probeprfg3.pdf`. 

---

## 6. Conceptual Check: Discrete sets in compact spaces
**Source:** `fs2023/Probeprfg3.pdf` (Prof. Peter S. Jossen, Mock Exam), Question 5.
**Target Location:** `content/07-compactness/03-sequential-vs-topological.tex`, Zeile 100 (oder passend).

```latex
% Source: old_exams/fs2023/Probeprfg3.pdf (Prof. Jossen) 31 January 2023, p. 2
% Extractor: Gemini
\begin{aiexercise}[Multiple Choice: Discrete subsets of a compact space]
\label{ex:ai_discrete_compact_mc}
Let $(X, d)$ be a compact metric space. A subset $A \subseteq X$ is called \emph{discrete} if for every point $x_0 \in A$ there exists an $\varepsilon > 0$ such that $B_\varepsilon(x_0) \cap A = \{x_0\}$. Which of the following statements are always true? (More than one may be correct).

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item Every discrete subset of $X$ is finite.
  \item Every \emph{closed} discrete subset of $X$ is finite.
  \item Every locally Lipschitz continuous function $f: X \to \mathbb{R}$ is Lipschitz continuous.
  \item Every uniformly continuous function $f: X \to \mathbb{R}$ is Lipschitz continuous.
\end{enumerate}
\exinfo{Adapted from the mock exam of 31 January 2023 (Prof.\ Peter S. Jossen), Question 5.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/07-compactness/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_discrete_compact_mc}]
Statements \textbf{(b)} and \textbf{(c)} are true.

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item \textbf{False.} Consider $X = \{1, 1/2, 1/3, \dots\} \cup \{0\}$ with the standard metric. This space is compact. The subset $A = \{1, 1/2, 1/3, \dots\}$ is discrete (since every point is isolated), but it is infinite.
  \item \textbf{True.} If $A$ is closed in the compact space $X$, then $A$ itself is compact. An open cover of $A$ can be formed by taking the balls $B_\varepsilon(x)$ for each $x \in A$. Since $A$ is compact, a finite subcover exists, which implies $A$ must be finite.
  \item \textbf{True.} This is a known property: local Lipschitz continuity on a compact space implies global Lipschitz continuity (\cref{ex:locally_lipschitz_is_lipschitz}).
  \item \textbf{False.} A function can be uniformly continuous but not Lipschitz. For example, $f(x) = \sqrt{x}$ on $[0,1]$ is uniformly continuous (since $[0,1]$ is compact) but its derivative blows up near $0$, so it is not Lipschitz.
\end{enumerate}
\end{exercisesolution}
```

---

## 7. Conceptual Check: Flux and Divergence with Singularities
**Source:** `fs2023/Probeprfg3.pdf` (Prof. Peter S. Jossen, Mock Exam), Question 6.
**Target Location:** `content/23-flux-divergence/02-divergence-theorem.tex`, am Ende der Datei.

```latex
% Source: old_exams/fs2023/Probeprfg3.pdf (Prof. Jossen) 31 January 2023, p. 2
% Extractor: Gemini
\begin{aiexercise}[Multiple Choice: Flux through a sphere with a singularity]
\label{ex:ai_flux_singularity_mc}
Let $U := \mathbb{R}^3 \setminus \{0\}$ and let $F: U \to \mathbb{R}^3$ be a continuously differentiable vector field. For $r > 0$, let $I_r := \int_{\partial B_r(0)} \langle F, \mathbf{n} \rangle dA$ be the flux integral through the boundary of the ball $B_r(0)$ with respect to the outward-pointing normal. Which of the following statements are always true? (More than one may be correct).

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item If $F$ is divergence-free on $U$, then $I_r = 0$ for all $r > 0$.
  \item If $F$ is divergence-free on $U$, then the value of $I_r$ does not depend on $r$.
  \item If $F$ is curl-free on $U$, then the value of $I_r$ does not depend on $r$.
  \item If $F = \nabla \times G$ for some vector field $G$ on $U$, then $I_r = 0$ for all $r > 0$.
\end{enumerate}
\exinfo{Adapted from the mock exam of 31 January 2023 (Prof.\ Peter S. Jossen), Question 6.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/23-flux-divergence/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_flux_singularity_mc}]
Statements \textbf{(b)} and \textbf{(d)} are true.

\begin{enumerate}[label=\textbf{(\alph*)}]
  \item \textbf{False.} The vector field $F(x) = \frac{x}{\|x\|^3}$ is divergence-free on $U$, but its flux through any sphere centered at the origin is $4\pi \neq 0$.
  \item \textbf{True.} By the Divergence Theorem, the flux out of the annular region between two spheres $B_{r_1}(0)$ and $B_{r_2}(0)$ is $\int \operatorname{div}(F) dV = 0$. Thus, the flux into the region (through the inner sphere) equals the flux out (through the outer sphere), meaning $I_{r_1} = I_{r_2}$.
  \item \textbf{False.} Curl-free implies it is locally a gradient field, but it has no bearing on the flux. For example, $F(x,y,z) = (x,y,z)^T$ is curl-free, but its flux $I_r = 4\pi r^3$ depends heavily on $r$.
  \item \textbf{True.} By Stokes' Theorem, the flux of a curl field through a closed surface (like a sphere) is equal to the line integral of $G$ along the boundary of the surface. Since a sphere has no boundary ($\partial(\partial B_r(0)) = \emptyset$), the integral is strictly $0$.
\end{enumerate}
\end{exercisesolution}
```
