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

*(populated during Phase 2)*

## Conventions

- An entry is **never** removed, only re-statused, so the reasoning stays auditable.
- `resolved` entries record *what was decided and why*, not just that it was decided.
- Divergences from `exercises/SolN_Analysis2_eng.pdf` are always logged, even when the TA
  turns out to be right — the disagreement itself is useful to the reader.
