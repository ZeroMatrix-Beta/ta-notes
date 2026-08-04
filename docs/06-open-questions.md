# Open questions

Anything that must not be silently resolved: illegible handwriting, suspected mathematical
errors in a source, divergences between a TA and the official solution, and judgement calls
worth a second opinion.

**ID scheme:** `OQ-NN`, running. **Status:** `open` → `resolved` / `accepted-open`.

| ID | Where | Issue | Status |
|---|---|---|---|
| OQ-01 | `Corsin Nick/Class Notes/Week 2.pdf`, cover | Cover reads *"Class notes Week 1"* while `Week 3.pdf`/`Week 9.pdf` read *"Week 3"*/*"Week 9"*. | **resolved** — file name is canonical; it agrees with all other tutors and with the exercise-sheet numbering. |
| OQ-02 | Corsin Week 2, p. 3 | Metric axiom 1 is stated as `d(x,y) ≥ 0, with equality iff x = y`, and glossed *"the distance positive"*. The gloss omits "non-"; the formula is correct. | **resolved** — transcribe the formula, correct the gloss to "the distance is non-negative". |
| OQ-03 | Corsin Week 2, p. 6 | `B_r(x)` is defined for `r ∈ ℝ` rather than `r > 0`. Harmless in context but technically loose. | open — flag as a remark, do not alter. |
| OQ-04 | Corsin Week 3, p. 1 | Exercise 3 asks to show `ℕ ⊆ X` is closed, bounded, non-compact for `d(x,y) = |x−y|/(1+|x−y|)` on `X = ℝⁿ`. With `X = ℝⁿ` and `n > 1`, `ℕ ⊆ ℝⁿ` needs an embedding; Corsin presumably means `n = 1`. | open — flag, ask before "fixing". |
| OQ-05 | Corsin Week 2, p. 11 | The ε–δ definition of continuity is written `d(x₀,x) < ε ⟹ d(f(x₀),f(x)) < ε` — the hypothesis must use `δ`, otherwise the quantified `δ` never appears. | **resolved** — a slip of the pen; typeset with `δ` in the hypothesis. Unambiguous from context. |
| OQ-06 | Corsin Week 2, p. 15 | Solution 2 says "where we used `n_k > k > N`". For a subsequence the standing fact is `n_k ≥ k`. | **resolved** — immaterial to the argument (`k > N` is what is used); typeset as `n_k ≥ k > N`. |
| OQ-07 | Corsin Week 3, p. 6 | Counterexample writes `V = S¹ = {x ∈ ℝ² : ‖x‖ = R²}`. | **resolved** — must be `‖x‖ = 1`; the stated intersection `{(±1,0)}` confirms it. Corrected. |
| OQ-08 | Corsin Week 3, p. 2 | In the triangle-inequality expansion for `d̃ = d/(1+d)`, one term reads `d₂d₁d₂` where the expansion gives `d₂d₁d₃`. | **resolved** — a transcription slip in the source; the cancelled terms and the conclusion `0 ≤ 2d₂d₃ + d₁d₂d₃` are correct. Re-derive the line cleanly when typesetting. |
| OQ-09 | Corsin Week 4, p. 5 | "The **columns** of the Jacobian are the gradients" — the displayed matrix stacks ∇F₁…∇F_m as **rows**. | **resolved** — rows is correct (and consistent with `Jf = (∇f)ᵀ` directly above). Corrected to "rows". |
| OQ-10 | Corsin Week 4, p. 10 | Multi-index recall written `∂^α = ∂_{α₁}∂_{α₂}⋯∂_{α_n}`, e.g. `∂^(2,1) = ∂₂∂₁`. | **resolved** — a multi-index counts applications, so `∂^(2,1) = ∂₁²∂₂`. His own expansion uses `∂₁²∂₂`, confirming intent. Corrected. |
| OQ-11 | Corsin Week 4, p. 11 | Both compact Taylor formulas are written `Σ_{ℓ=1}^k`, omitting the `ℓ=0` term `f(x̄)`. | **resolved** — must be `Σ_{ℓ=0}^k`; the explicit expansion on p. 10 includes `f(x̄)`. Corrected. |
| OQ-12 | Corsin Week 5, p. 5 | Constraint written `g(x) = |x| − 1`, but the Lagrangian differentiates `x²+y²+z²−1 = |x|²−1`. | **resolved** — both cut out the same sphere; the squared version is the one used. Typeset with `|x|²−1` throughout. |
| OQ-13 | Corsin Week 5, p. 7 | The Hessian test is stated for `f ∈ C³`. | **resolved** — `C²` suffices and is what the Hessian's own definition assumes. Relaxed to `C²`. |
| OQ-14 | Corsin Week 5, p. 8 | Characteristic equation written `A − λId = 0` (determinant missing). | **resolved** — must be `det(A − λId) = 0`. Corrected. |
| OQ-15 | Corsin Week 6, p. 11 | The two implicit functions `x(y)` and `y(x)` are given swapped domains relative to his own IFT setup (`r` around `x₀`, `s` around `y₀`). | **resolved** — swapped back: `x(y) : (−s,s)→(−r,r)`, `y(x) : (−r,r)→(−s,s)`. |
| OQ-16 | `exercises/Ex7_Analysis2_eng.pdf`, 7.9 | Refers to "Exercise 6.3.3"; the function `y²(1−x)−x³` is item 2 of Exercise **7.3** on the same sheet. | **resolved** — typo in the official sheet. Cross-referenced to 7.3.2. |
| OQ-17 | Corsin Week 8, p. 13 | In the final integration the α-term is written `(π/2)·α/(1+α²)` and integrates to `(π/4)log(1+α²)` — both a factor 2 off from `I'(α)`, whose α-term is `απ/4`. | **resolved** — corrected to `(π/4)·α/(1+α²)` and `(π/8)log(1+α²)`, which makes his two bracket terms genuinely equal. **Final answer `π log 2/8` is correct** and matches the known value. |
| OQ-18 | Corsin Week 8, p. 4 | Quiz bullet says "for `α ≠ √2`, ∇f is a local diffeo"; `det Hf(0) = 2−α²` also vanishes at `α = −√2`. | **resolved** — should read `α ≠ ±√2`. Same oversight the next bullet exploits. Corrected with a note. |
| OQ-19 | Corsin Week 8, p. 8 | Fubini example 1 writes `∫dx∫dy` but takes the inner antiderivative in `x`. | **resolved** — differentials swapped relative to the computation; result correct. Order fixed. |
| OQ-20 | Corsin Week 9, p. 1 | Hint for 9.1 labels `(r sinθ cosφ, r sinθ sinφ, r cosθ)` as **cylindrical** coordinates; that is the **spherical** formula. Range also given as `θ ∈ (−π/2, π/2)` rather than `(0,π)`. | **resolved** — relabelled *spherical* and the range corrected; the formula (not the label) is what is useful here. The official sheet's own hint does say "cylindrical". |
| OQ-21 | `Corsin Nick/Class Notes/Week 10.pdf`, cover | Cover reads "Week 9" while the problems listed are 10.1–10.6. | **resolved** — same class of slip as `OQ-01`; file name + exercise numbers win. |
| OQ-22 | Corsin Week 10, p. 11 | Gauss example header says `Ω = S²`; the theorem needs the solid ball. | **resolved** — the computation does integrate over `B₁(0)`; only the label was loose. Corrected. |
| OQ-23 | Corsin Week 11, p. 10 | Differential `p`-form defined via `ω_x : ℝⁿ → ℝ` "antisymmetric, `n`-linear". | **resolved** — must be `ω_x : (ℝⁿ)^p → ℝ`, antisymmetric and `p`-linear; his own expansion uses `p` indices. Corrected. |
| OQ-24 | Corsin Week 5, p. 7 | `degenerate` defined as "∃ `v ≠ 0` with `vᵀAv = 0`". This is far weaker than intended: for indefinite `A`, `t ↦ (tv+(1−t)u)ᵀA(tv+(1−t)u)` changes sign and so vanishes somewhere, making **every** indefinite matrix degenerate — and the Hessian test's "indefinite **and not degenerate** ⟹ saddle" vacuous. | **resolved** — intended notion is a nontrivial kernel (`det A = 0`), which is also what Ex. 6.2 states. Corrected; the redundant "and not degenerate" dropped from the saddle case, and the genuinely inconclusive case (semidefinite *and* degenerate) stated instead. |
| OQ-25 | Corsin Week 4, p. 2 | Middle line of the differentiability chain reads `lim_{h→0} (F(x₀+h)−F(x₀))/|h| = DF_{x₀}(h/|h|)`, inside a chain of `⇕`. The limit does not exist (`h → 0` on the left, `h` still on the right) and the equivalence is false — all directional derivatives existing does not give differentiability. | **resolved** — restated as: fix `v`, then `lim_{s→0}(F(x₀+sv)−F(x₀))/s = DF_{x₀}(v)`, and demoted `⇕` to `⇓`. His own *important remark* on p. 6 already says the converse fails, and `xy/(x²+y²)` on p. 3 is the counterexample. |
| OQ-26 | Corsin Week 7, pp. 2–3 | Regular value theorem requires `DF_x` **surjective**, but the worked example glosses full rank of `(2x, 2y)` as "is injective as a linear map". A `1×2` matrix is never injective. | **resolved** — full rank means *surjective* for a wide (implicit) Jacobian and *injective* for a tall (parametrization) one; his later use of "full rank (is injective)" for `Jac f` **is** correct. Both glosses kept and disambiguated by shape in a new *important remark*. |

| OQ-27 | Corsin Week 4, p. 4 | `γ'(π/4)` called "the **speed** of the curve". | **resolved** — `γ'(t)` is the *velocity* (a vector); the *speed* is the scalar `\|γ'(t)\|`. The display immediately below uses the vector, so the distinction matters. Corrected with a note. |

| OQ-28 | Corsin Week 5, p. 3 | Remark gives `∇g(x) = x/\|x\|` for the `g` just fixed as `g(x) = \|x\|² − 1`, whose gradient is `2x`. `x/\|x\|` is `∇(\|x\|)`. | **resolved** — same `\|x\|` vs `\|x\|²` confusion as `OQ-12`, one page earlier. The two gradients are positive multiples of each other so the geometry (perpendicular to the level set) is unaffected, but the Lagrangian below differentiates the squared version. Corrected to `2x` with a note. |

*(weeks 12–13 and the ODE appendix still to come)*

## Conventions

- An entry is **never** removed, only re-statused, so the reasoning stays auditable.
- `resolved` entries record *what was decided and why*, not just that it was decided.
- Divergences from `exercises/SolN_Analysis2_eng.pdf` are always logged, even when the TA
  turns out to be right — the disagreement itself is useful to the reader.
