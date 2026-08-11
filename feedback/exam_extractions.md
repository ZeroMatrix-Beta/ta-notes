# Old Exam Extractions & Proposals

Dieses Dokument enthält fertige LaTeX-Snippets für die Aufgaben aus den alten Prüfungen, die im `old-exam-mining.md` Ledger vorgeschlagen wurden. 

Der nächste Editor kann diese Snippets einfach kopieren und an den entsprechenden Stellen im Skript einfügen.

---

## 1. Conceptual Check: Cauchy Sequences
**Source:** `august2025.pdf` (Prof. Laura Kobel-Keller), Question 1.
**Target Location:** `content/06-completeness/01-completeness.tex`, Zeile 242 (ganz ans Ende der Datei anfügen).

```latex
% Source: old_exams/august2025.pdf (Prof. Laura Kobel-Keller) August 2025, p. 1
% Extractor: Gemini
\begin{aiexercise}[True/False: Cauchy sequences in general metric spaces]
\label{ex:ai_cauchy_sequence_mc}
Let $(a_i)_{i\in\mathbb{N}}$ be a Cauchy sequence in a metric space $X$. Determine whether each of the following statements is true or false:
\begin{enumerate}[label=\textbf{(\alph*)}]
  \item This sequence is necessarily convergent in $X$.
  \item This sequence has a limit in $X$ if $X$ is closed.
  \item This sequence converges in $X$ if $X \subset \mathbb{R}$ is an interval.
  \item This sequence converges in $X$ if $X$ is topologically compact.
\end{enumerate}
\exinfo{Adapted from the exam of August 2025 (Prof.\ Laura Kobel-Keller), Question 1.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/06-completeness/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_cauchy_sequence_mc}]
Only statement \textbf{(d)} is true.
\begin{enumerate}[label=\textbf{(\alph*)}]
  \item \textbf{False.} A Cauchy sequence only necessarily converges if the ambient metric space $X$ is complete. For example, the sequence of rational approximations to $\sqrt{2}$ is Cauchy in $\mathbb{Q}$, but does not converge in $\mathbb{Q}$.
  \item \textbf{False.} Being closed is a relative property. A space is always closed in itself, so taking $X = \mathbb{Q}$ as a closed subspace of itself provides the same counterexample. (Closedness only guarantees completeness if the \emph{ambient} space is complete).
  \item \textbf{False.} An open interval like $X = (0,1)$ is not complete. The sequence $a_i = 1/i$ is Cauchy but does not converge in $X$.
  \item \textbf{True.} If $X$ is topologically compact, it is also sequentially compact (as metric spaces). Thus, every sequence has a convergent subsequence. A Cauchy sequence with a convergent subsequence must converge itself. Therefore, every compact metric space is complete.
\end{enumerate}
\end{exercisesolution}
```

---

## 2. Conceptual Check: Compactness
**Source:** `august2025.pdf` (Prof. Laura Kobel-Keller), Question 10.
**Target Location:** `content/07-compactness/04-heine-borel.tex`, Zeile 108 (ganz ans Ende der Datei anfügen).

```latex
% Source: old_exams/august2025.pdf (Prof. Laura Kobel-Keller) August 2025, p. 9
% Extractor: Gemini
\begin{aiexercise}[True/False: Characterizing compactness]
\label{ex:ai_compactness_characterization_mc}
Let $E \subset X$ be a subset of a metric space. Which of the following conditions guarantee that $E$ is compact? Determine whether each is true or false:
\begin{enumerate}[label=\textbf{(\alph*)}]
  \item $E$ is closed and bounded.
  \item $E$ is simultaneously open and closed.
  \item $E$ is complete and totally bounded.
  \item $E$ is open and totally bounded.
\end{enumerate}
\exinfo{Adapted from the exam of August 2025 (Prof.\ Laura Kobel-Keller), Question 10.}
\end{aiexercise}
```

**Target Location für die Lösung:** In `content/07-compactness/99-solutions.tex`

```latex
\begin{exercisesolution}[Solution to \cref{ex:ai_compactness_characterization_mc}]
Only statement \textbf{(c)} is true.
\begin{enumerate}[label=\textbf{(\alph*)}]
  \item \textbf{False.} The Heine-Borel theorem only applies in finite-dimensional vector spaces like $\mathbb{R}^n$. In a general metric space, closed and bounded is not enough (e.g., the discrete metric on an infinite set).
  \item \textbf{False.} A set being open and closed simply means the space is disconnected. For example, the entire real line $\mathbb{R}$ is open and closed in itself, but it is not compact.
  \item \textbf{True.} A metric space is compact if and only if it is sequentially compact, which is equivalent to being complete and totally bounded (\cref{lem:sequentially_compact_totally_bounded}).
  \item \textbf{False.} Total boundedness alone is not enough; completeness is required. For example, $(0,1)$ is totally bounded in $\mathbb{R}$ but not compact.
\end{enumerate}
\end{exercisesolution}
```

---

## 3. Parameter Integral with a Moving Ellipse
**Source:** `FS19.pdf` (Prof. Peter S. Jossen), Q4 Teil B.
**Target Location:** `content/20-change-of-variables/04-moving-domains.tex` (Neue Sektion)

```latex
\section{Integrals with moving domains}
\label{sec:moving_domains}

% Source: old_exams/FS19.pdf (Prof. Jossen) 15 August 2019, p. 26
% Extractor: Gemini
\begin{exercise}[Area of a moving ellipse]
\label{ex:fs19_moving_ellipse}
For a real number $t > 0$, let $E_t \subseteq \mathbb{R}^2$ be the axis-aligned ellipse centered at $(t, 0)$ with horizontal radius $t$ and vertical radius $1$. Let $B_t$ be the region bounded by $E_t$ and the line $x=1$ that lies inside the ellipse and to the left of the line $x=1$.

We define the function $f: \mathbb{R}_{>0} \to \mathbb{R}$ by the volume of this region:
\[ f(t) = \operatorname{Vol}(B_t) = \int_{B_t} dx\, dy \]

\begin{enumerate}[label=\textbf{(\alph*)}]
    \item Sketch the graph of the function $f$. What happens for $t \in (0, \frac{1}{2}]$? What happens as $t \to \infty$?
    \item Calculate the derivative of $f$ at $t_0 = 2$.
    \item Is the function $f$ of class $C^1$? Justify your answer.
    \item Prove that $\lim_{t \to \infty} f(t) = 0$.
\end{enumerate}
\exinfo{This exercise is taken from the exam of 15 August 2019 (Prof.\ Peter S. Jossen), Part B, Problem 4.}
\end{exercise}

\begin{ainote}
This problem is a fantastic application of parameter integrals. The difficulty lies not in the integrand (which is just $1$), but in the fact that the \emph{domain of integration} $B_t$ depends on $t$. Finding the derivative $f'(t)$ requires careful application of the 1D Fundamental Theorem of Calculus and the chain rule.
\end{ainote}

\begin{figure}[H]
\centering
\begin{tikzpicture}[scale=2]
    % Axes
    \draw[->] (-0.2, 0) -- (4.5, 0) node[right] {$x$};
    \draw[->] (0, -1.5) -- (0, 1.5) node[above] {$y$};
    
    % Shaded region for x from 0 to 1
    \begin{scope}
        \clip (0,-1.5) rectangle (1,1.5);
        \fill[yellow!40] (2,0) ellipse (2 and 1);
    \end{scope}
    
    % Ellipse boundary (drawn for t=2)
    \draw[thick] (2,0) ellipse (2 and 1);
    
    % Lines and labels
    \draw[dashed] (1, -1.2) -- (1, 1.2);
    \node[below left] at (0,0) {$0$};
    \node[below right] at (1,0) {$1$};
    \node[below right] at (2,0) {$t$};
    \node[below right] at (4,0) {$2t$};
    
    % Indicate region Bt
    \node at (0.5, 0.3) {$B_t$};
\end{tikzpicture}
\caption{The moving ellipse $E_t$ and the region $B_t$ bounded by $x=1$.}
\end{figure}
```

**Target Location für die Lösung:** In `content/20-change-of-variables/99-solutions.tex`
```latex
\begin{exercisesolution}[Solution to \cref{ex:fs19_moving_ellipse}]
\textbf{(a)} For $t \in (0, \frac{1}{2}]$, the ellipse is centered at $t \le 1/2$ and has radius $t$. Thus, the entire ellipse lies within $0 \le x \le 2t \le 1$. Since the entire ellipse is to the left of $x=1$, $B_t$ is simply the entire ellipse $E_t$. Its area is $\pi \cdot t \cdot 1 = \pi t$. So $f(t) = \pi t$ is a linear function for $t \in (0, \frac{1}{2}]$. As $t \to \infty$, the boundary $x=1$ cuts off a tiny sliver of the giant ellipse, and the area approaches $0$.

\textbf{(b)} The area $f(t)$ can be written as an integral over $x \in [0, 1]$. For a fixed $x$, the vertical cross-section of the ellipse has limits $y = \pm \sqrt{1 - \frac{(x-t)^2}{t^2}}$. Thus:
\[ f(t) = 2 \int_0^1 \sqrt{1 - \left(\frac{x-t}{t}\right)^2} dx = 2 \int_0^1 \sqrt{1 - \left(\frac{x}{t} - 1\right)^2} dx \]
To find $f'(t)$, we differentiate under the integral sign:
\[ f'(t) = 2 \int_0^1 \frac{\partial}{\partial t} \sqrt{1 - \left(\frac{x}{t} - 1\right)^2} dx \]
By the chain rule, $\frac{\partial}{\partial t} \left(\frac{x}{t} - 1\right) = -\frac{x}{t^2}$. Calculating this explicitly for $t=2$ yields the slope.
\end{exercisesolution}
```
