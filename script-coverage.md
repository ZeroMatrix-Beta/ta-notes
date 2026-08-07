# Mining `Analysis_II_Script_v1.pdf` — coverage survey

The **official course script**: *Analysis II: Several Variables*, Joaquim Serra, ETH,
Spring Semester 2024, 207 pp., dated 10 July 2024. It continues the Analysis I numbering, so
its chapters run **9–15**, not 1–7. Lineage stated in its own preface: German originals by
Manfred Einsiedler and Andreas Wieser (2016/17), revised by Peter Jossen (2019/20), rewritten
in English by Serra for 2023/24.

This is a *different kind of source* from the 17 tutor folders. It is not a blueprint to
transcribe — Corsin Nick remains that — it is the **authority to check our theorems against**,
plus a well-stocked reservoir of exercises and examples.

**Status: thin survey pass complete, no `.tex` written yet.** This file is the output. It
records the theorem-by-theorem comparison and shortlists what is worth taking, so the actual
enrichment can be done chapter by chapter without re-reading 207 pages.

**Decision taken 2026-08-06 (user):** *enrich existing sections only*. Topics the script
covers and we have no section for do **not** get new sections — see
[§6](#6-script-only-topics-deliberately-not-given-sections).

## Practical notes

* **Page offset:** printed page = PDF page − 4. (PDF 168 = printed 164.) Cite the **printed**
  page in `% Supplement:` comments, since that is what the numbering in the text refers to.
* **Provenance comment to use:**
  `% Supplement: Analysis_II_Script_v1.pdf, p. 27` (the file sits at the project root).
  Remember the SCOPE rule in `gemini.md` — re-cite the surrounding tutor source below any
  block inserted into transcribed material.
* **Extracted text** is at `scratch/script.txt` (full, `pdftotext -layout`) and
  `scratch/script-statements.txt` (statements and exercises only, proof bodies stripped —
  ~4000 lines instead of 10 700). Regenerate the latter with
  `scratchpad/extract.py` if needed. ⚠️ The extraction eats `∂`, `≤`, `∇`, `∈` and most Greek.
  **Never quote a formula from the `.txt` — render the page and read it.**

---

## 1. Section map

| Script | Printed pp. | Our chapters |
|---|---|---|
| 9.1 Basics of metric spaces | 3–13 | 2, 4, 6 |
| 9.2 Topology of metric spaces | 14–30 | 3, 5, 6, 7, 8 |
| 9.3 Normed vector spaces | 31–37 | 2, 3 |
| 10.1 The differential | 39–51 | 9, 10, 11 |
| 10.2 Higher derivatives | 52–61 | 11 |
| 11 Optimization, convexity | 62–75 | 12, 13, 14 |
| 12 Inverse/implicit, submanifolds | 76–87 | 15, 16, 17 |
| 13 Multidimensional integration | 88–133 | 19, 20, 21 |
| 14 Global integral theorems | 134–168 | 22, 23, 24, 25, 26 |
| 15 Ordinary differential equations | 169–202 | `appendix-a-odes.tex` |

The mapping is clean. No script section splits awkwardly across our chapters, and no chapter
of ours draws on two distant script sections.

---

## 2. Theorem-by-theorem verdict

Short answer to *"are our theorems more or less the same?"* — **yes, and closer than expected.**
Of ~120 numbered results in script chapters 9–14 that fall inside our scope, our document
carries a matching statement for about 100. Corsin evidently follows the script closely, so
the two agree not just in content but usually in *formulation*. Four genuine divergences and a
handful of gaps are listed below; everything not listed matches.

### Matches worth noting for how *exactly* they line up

* **The "three faces" pattern.** Script Prop 9.53 (continuity) → our
  `05-continuity/01-continuity.tex:29` *"The three definitions of continuity agree"*;
  script Thm 9.69 (compactness) → our `07-compactness/03-sequential-vs-topological.tex:83`.
  Same three conditions, same equivalence, independently arrived at.
* **Cauchy–Schwarz with the equality case** (Prop 9.100) → `02-.../03-cauchy-schwarz.tex:123`.
* **Sufficient condition for differentiability** (Thm 10.12) →
  `10-chain-rule/03-criteria-for-differentiability.tex:15`.
* **Euler's identity for homogeneous functions** — script has it as *Exercise* 10.22, we
  promoted it to a theorem (`10-chain-rule/01-chain-rule.tex:81`). Ours is the better call.
* **Spectral theorem via constrained minimization** (Thm 11.9 + Lemma 11.11) →
  `13-lagrange/01-lagrange-multipliers.tex:373`, including the Rayleigh-quotient corollary
  (`cor:courant_fischer_extreme`), which is script Exercise 11.21(iii).
* **Analytic estimates ⟹ Taylor series converges** (Def 10.39, Thm 10.40) →
  `11-taylor/03-analytic-functions.tex:8,15`. The estimate `sup|∂^α f| ≤ C α! ρ^{-|α|}` is
  identical.
* **Jordan measurability ⟺ boundary is null** (Prop 13.12) →
  `19-jordan-measure/01-jordan-measure.tex:117`, and our
  `lem:compact_jordan_vs_lebesgue_null` (line 122) is exactly the lemma that makes the
  script's Lebesgue-null phrasing legitimate.
* **Change of variables** (Thm 13.35) → `20-change-of-variables/01-change-of-variables.tex:6`.
  We state the `∫_A f(φ(y))|det Jφ(y)|dy` form; the script states the inverse form and gives
  ours as Exercise 13.36. Both are correct — no action needed.
* **Integrability conditions + Poincaré Lemma** (Lemma 14.38, Thm 14.44, Lemma 14.45) →
  `26-stokes/02-...tex:121` and `26-stokes/03-poincare-lemma.tex:6,13`.
* **Ascoli–Arzelà** (Thm 15.33) → `07-compactness/06-ascoli-arzela.tex:108`, added in the
  most recent commit. Same hypotheses.

### Divergences — candidates for `ainote`s

| # | Where | What diverges |
|---|---|---|
| **D1** | `07-compactness/02-compact-subsets.tex:8` | We quote the definition as **"9.63"**. In the script, compactness is **Definition 9.62**; *9.63* is the unnumbered remark explaining why condition (2) is called "topological". We also quote only **two** of the script's **three** equivalent conditions — the third, *"complete and totally bounded"*, is dropped. We do have totally-boundedness (`03-sequential-vs-topological.tex:36,43`) and we do prove the three-way equivalence at line 83, so nothing is missing mathematically; the *definition* just under-quotes its own cited source. Fix the number and add the third bullet. |
| **D2** | `12-extrema-hessian/02-hessian-test.tex:118` | We require **`f ∈ C²`**; script Prop 11.15 requires **`f ∈ C³`**. Ours is right (Taylor to second order with a `o(\|h\|²)` remainder needs only `C²`), and ours is also the standard statement. Worth an `ainote` saying so, since students comparing against the script will notice. Note this compounds an existing `ainote` at line 132 about Corsin's *"indefinite and not degenerate"* — the script has the same redundant hypothesis, so that note can now cite the script too. |
| **D3** | `21-gram-determinant/01-area-and-the-gram-determinant.tex:66` | We call **`det(MᵀM)`** the Gram determinant. Script Def 13.55 calls **`√det(LᵀL)`** the Gram determinant. Standard usage is ours; the square root is the *volume*. Every downstream formula agrees, so this is terminology only — but it is exactly the kind of thing that costs a mark in an exam, so it deserves a note. (The script's own statement of this definition is internally inconsistent — see E4.) |
| **D4** | `02-.../01-structured-spaces.tex` | **Notation.** Script remark 9.94 declares that from p. 31 onward the *Euclidean* norm is written `\|x\|` and `‖·‖` is reserved for non-standard norms. We use `‖·‖` throughout, per `gemini.md`. Keep ours; one `ainote` in ch. 2 so readers of the script are not tripped up, especially in chs. 13–14 where the script's `\|·\|` convention is dense. |

### Gaps — in the script, valuable, not in ours

Ordered by value. All go into an **existing** file.

| Script | What | Target |
|---|---|---|
| **Cor 10.41** | **Unique continuation principle** for real-analytic functions: two analytic functions on a connected open set agreeing to all orders at one point agree everywhere; in particular agreeing on a nonempty open subset forces agreement throughout. Four lines, and it is the payoff that makes `03-analytic-functions.tex` feel finished rather than truncated. | `11-taylor/03-analytic-functions.tex` |
| **Lemma 15.13** | **Grönwall's inequality.** `u' ≤ β(t)u ⟹ u(t) ≤ u(a)exp(∫β)`. Absent from our document entirely. It is the tool behind ODE uniqueness, and script Ex 15.45 makes uniqueness a corollary of it. | `appendix-a-odes.tex` |
| **Prop 11.26** | **Jensen's inequality** for convex `f` on a convex open set. We *use* Jensen in `02-.../99-solutions.tex:380,434` without ever having stated it. | `14-convexity/01-convexity.tex` |
| **Cor 9.50** | Two metrics on the same set have **the same convergent sequences iff they generate the same topology** (with Prop 9.49, convergence stated purely topologically). Clean, short, and it is the precise sense in which "the metric doesn't matter, the topology does". | `04-sequences/01-sequences-and-convergence.tex` |
| **Lemma 9.70** | **Nesting principle** — the finite-intersection-property characterisation of topological compactness. We have neither the statement nor the name. | `07-compactness/01-open-covers.tex` |
| **Def 9.15** | The **"eventually"** vocabulary, defined once and then used to compress every `∃N ∀n≥N` in the chapter. A notational device, not a theorem, but it makes chs. 4–7 noticeably lighter to read. Would be a `notation` environment. | `04-sequences/01-sequences-and-convergence.tex` |
| **Ex 14.16** | **Archimedes' principle** from the divergence theorem — buoyant force `= ρgV`. Half a page, genuinely memorable, and our ch. 23 has no physical application at all. | `23-flux-divergence/02-flux-and-the-divergence-theorem.tex` |

### Where *we* are ahead of the script

Worth recording so no one "fixes" these by cutting them.

* **Differential forms.** Script §14.4 is four paragraphs titled *"A glimpse into differential
  forms"* with `∫_M dω = ∫_∂M ω` stated and not proved, no numbered statements at all. Our
  chs. 24–25 (wedge products, exterior derivative, pullbacks, orientability, submanifolds with
  boundary) are a full treatment the script does not attempt.
* **Geodesics** (ch. 18) has no counterpart in the script.
* **Convexity** — our `prop:characterizations_of_convexity` collects more equivalent conditions
  than script Prop 11.24's two.
* **The Hessian test** is stated correctly for `C²` (see D2) and handles the degenerate case
  explicitly, which the script does not.
* **Lagrange multipliers** — the script gives the `λ₀`-normalised form (Prop 11.5,
  `λ₀∇f + Σλⱼ∇gⱼ = 0`, `Σλ² = 1`) with no constraint qualification; we give the
  linear-dependence form plus `aiexample` `ex:constraint_qualification_fails` (the cuspidal
  cubic) showing what breaks without it. The two statements are equivalent; ours is better
  taught.

---

## 3. Exercise shortlist

Criteria applied: valuable, **not too hard**, and not already in our document. The script's
exercises are unmarked for difficulty, so the ratings are mine. Every one of these would be an
`exercise` (transcribed, not `aiexercise`) with a `% Supplement:` comment, and needs an
`exercisesolution` per `gemini.md`.

### Take first — high value, genuinely easy

| Script | p. | Statement | Target chapter |
|---|---|---|---|
| **Ex 9.56** | 19 | For `∅ ≠ E ⊆ X`, `f_E(x) := inf{d(x,z) : z ∈ E}` is 1-Lipschitz, and `E` is closed iff `E = {f_E = 0}`. | 5 (continuity) |
| **Ex 9.76** | 25 | An open `U ⊆ ℝⁿ` is complete iff `U = ℝⁿ` or `U = ∅`. | 6 (completeness) |
| **Ex 9.60** | 20 | Find (a) a contraction on a non-complete space with no fixed point, (b) an isometry of a complete space with no fixed point. Shows both Banach hypotheses are sharp. | 6 (contraction mappings) |
| **Ex 9.46** | 16 | In `ℝⁿ`, `closure B(x,r) = {d(x,y) ≤ r}` and `∂B(x,r) = {d(x,y) = r}`. Worth pairing with the discrete-metric counterexample where this *fails*. | 3 (open/closed) |
| **Ex 9.26** | 10 | Three facts about Cauchy sequences: bounded; convergent ⟹ Cauchy; Cauchy with a convergent subsequence converges. | 6 |
| **Ex 9.81** | 28 | Two connected sets with a common point have connected union; generalise to arbitrary unions; use it to define the connected component of a point. | 8 |
| **Ex 9.68** | 22 | Totally bounded ⟹ bounded, and a bounded metric space that is not totally bounded. | 7 |
| **Ex 10.13** | 44 | `xy/(x²+y²)`: both partials exist everywhere, not differentiable at `0`. ⚠️ **Check `10-chain-rule/02-directional-derivatives.tex` first** — we already carry `x²y/(x⁴+y²)` and a near-miss duplicate of this kind was caught once before (see `supplements.md`). | 10 |
| **Ex 11.18** | 71 | Critical points of `f(x,y) = x³ − y³ + 3αxy`, classified. Standard, clean, parameter-dependent. | 12 |
| **Ex 14.56** | 163 | `rot(grad f) = 0` and `div(rot F) = 0`. Two lines each, and the pair is the whole content of `d² = 0`. | 22 |
| **Ex 9.103** | 35 | `ℝ[x]` is infinite-dimensional; exhibit a basis. Motivates why norm-equivalence needs finite dimension. | 2 |

### Take second — valuable, medium

| Script | p. | Statement | Target |
|---|---|---|---|
| **Ex 9.5** | 5 | Polygon inequality `d(x₁,x_N) ≤ Σd(xᵢ,xᵢ₊₁)` by induction. | 2 |
| **Ex 9.8** + **9.18** | 6, 8 | `φ∘d` is a metric for concave increasing `φ` with `φ(0)=0`, and it has the same convergent sequences. **We already have the first half as a proposition** (`02-.../02-metric-spaces.tex:154`) — take only Ex 9.18, the convergence half, which is the interesting one. | 2 or 4 |
| **Ex 9.85** | 29 | IVT on any connected space, not just an interval. | 8 |
| **Ex 10.36** | 60 | Quadratic Taylor polynomials of `sin(xy)`, `√(1+x+y²)`, `exp(arctan(x−y))`, `1/√(1−x²−y²)` — *"Don't use the general formula!"* Excellent drill for the substitution technique. | 11 |
| **Ex 11.14** | 70 | Polarisation: `d²/dt²|₀ f(te) = eᵀ Hf(0) e` recovers all second derivatives. | 12 |
| **Ex 11.22** | 73 | Two points of `S^{n−1}` are at maximal distance iff antipodal — via Lagrange on `S^{n−1}×S^{n−1}`. | 13 |
| **Ex 11.25** | 75 | The gradient inequality `f(y) − f(x) ≥ Df_x(y−x)` characterises convexity for `C¹` `f`; deduce every critical point is a global minimum. | 14 |
| **Ex 13.6** | 92 | Inclusion–exclusion for the measure of a union of dyadic sets. | 19 |
| **Ex 14.46** | 156 | For which `α` is `F(x,y) = (αx e^y, (y+1+x²)e^y)` conservative? Find the potential. Short and exam-shaped. | 26 |
| **Ex 14.58** | 164 | Choose `α,β,γ` making a given field irrotational, then find a potential. | 26 |
| **Ex 14.57**, **14.59** | 163–164 | Two flux computations done twice — directly, and by Stokes (14.59 also by Gauss). The point is that the answers agree. | 26 |
| **Ex 15.17** | 178 | Three concrete linear ODEs, including one wanting an integrating factor (with hint). | appendix A |
| **Ex 15.37** | 194 | `F` with continuous `∂_{x_k}F` is locally Lipschitz — the bridge from the usual hypothesis to Picard–Lindelöf's. | appendix A |

### Deliberately skipped

* ~~**Ex 9.33–9.35** (completion of a metric space) — depends on §9.1.4, which we have no
  section for. See §6.~~ **Reversed 2026-08-07 (user).** Taken after all — see §8. The
  dependency was on §9.1.3 (Def 9.32, the general completion construction), not §9.1.4 (the
  ℝ-from-ℚ specialisation, still skipped); the general construction is itself marked \qt{extra
  material} by the script but is now transcribed as
  `content/06-completeness/02-completion-of-a-metric-space.tex`.
* **Ex 14.24–14.30** (rotation number, Jordan curve theorem) — a six-exercise chain building to
  a proof of the Jordan curve theorem. Individually meaningless, collectively a whole section.
  We already state Jordan–Brouwer at `22-vector-calculus/01-bounded-c1-domains.tex:29`. See §6.
* **Ex 15.40** (marked *Challenge* in the script), **Ex 15.42–15.43** (attractors, limit
  cycles) — beyond "not too hard".
* **Ex 10.32**, **Ex 10.37** (multinomial identity; Taylor expansion of `det(I+tX)`) —
  combinatorial rather than illuminating, and 10.37 is harder than it looks.

---

## 4. Example shortlist

| Script | p. | What | Target |
|---|---|---|---|
| **Ex 9.13** | 7 | The sphere carries **two** natural metrics: the restricted Euclidean chord distance and the geodesic arc `d₁(x,y) = R·arccos(⟨x,y⟩/R²)`. The best possible motivation for "a subset inherits a metric, but not necessarily the one you want". | 2 |
| **Ex 9.11** | 6 | The Manhattan metric, with the actual street-grid explanation. We have `d₁` (per `gemini.md`, keeping Corsin's indices) — **check whether the motivating story is there**; if not, the prose is worth lifting. | 2 |
| **9.38** | 14 | `X = (0,1) ∪ (2,3)` has clopen sets other than `∅` and `X`, previewing connectedness. Two sentences, and it makes "clopen" concrete before ch. 8 needs it. | 3 |
| **Ex 9.65** | 22 | `ℚ ∩ [0,2]` is not compact, via the cover `(ℚ∩[0,√2)) ∪ ⋃_{p∈ℚ,p>√2}(ℚ∩(p,2])` (corrected 2026-08-07 — verified on the rendered page; the set is `[0,2]`, not `[0,√2]`, and the union runs to `2`, not `√2`). The irrationality of `√2` is doing the work — a much better example than `(0,1]`. | 7 |
| **Ex 10.21** | 48 | *"How to use the chain rule in practice"*: rename `g`'s variables `u,v`, tabulate the partials, substitute back. A three-step recipe, and the script ends by admitting the chain rule is not more economical here than differentiating directly — honest, and pedagogically the right note. | 10 |
| **Ex 10.35** | 59 | Degree-2 Taylor of `√(1+x−y²)` by substituting `t = x−y²` into the known 1-D series, then discarding `O(r³)` terms. The worked companion to Ex 10.36. | 11 |
| **Ex 11.17** | 71 | `f(x,y) = x sin(y) + ax² + by²` with `det H = 4ab−1`: a two-parameter family running through all four Hessian cases. | 12 |
| **Ex 11.16** | 71 | `ax⁴ + by⁴` — Hessian is the zero matrix regardless of `a,b`, yet the behaviour at `0` changes with them. The sharpest statement of "degenerate ⟹ no information". Pairs directly with our `ainote` at `02-hessian-test.tex:132`. | 12 |
| **Ex 14.16** | 145 | Archimedes' principle (also listed as a gap in §2). | 23 |
| **Ex 14.36** | 152 | `F(x,y) = (−y,x)` integrated along three different paths from `(0,0)` to `(1,1)`, giving `0`, `1`, `−1`. Path-dependence made unmissable before the potential theory starts. | 26 |
| **Ex 14.39** | 153 | `F = (−y,x)/(x²+y²)` on `ℝ²∖{0}`: satisfies the integrability conditions everywhere, still not conservative (`∮ = 2π`). The standard witness that Poincaré needs simple connectedness. **Check `26-stokes/02-...tex` first** — we may already have it. | 26 |
| **Ex 15.15** | 176 | Pure resonance of a pumped harmonic oscillator, `y'' + ky = sin(ωt)`, and what happens as `ω² → k`. | appendix A |
| **Ex 15.27–15.29** | 182–185 | Three autonomous 2-D systems: rotation, spiral, and a nonlinear one whose polar form `r' = r − r³` gives a limit cycle. The first two are easy and are the standard pictures. | appendix A |

Also worth a look when ch. 20 is next touched: the script's **spherical and cylindrical
coordinate boxes** (pp. 113–114) tabulate both Jacobians explicitly, with `det J = r² sinθ`
and `det J = r`. We compute these in several places; a single reference table would save the
repetition.

---

## 5. Errors and slips in the script

Found during this pass. Each is a candidate for an `ainote` wherever we state the
corresponding result — per `gemini.md`, flag, never silently follow.

| # | Where | Problem |
|---|---|---|
| **E1** | Def 9.52(1), p. 18 | The ε–δ condition ends `f(B(x,δ)) ⊆ B(f(y),ε)`. There is no `y` in the statement; it must be `B(f(x),ε)`. |
| **E2** | Cor 9.79 (Weierstrass), p. 27 | *"there exist `x̄ ∈ X` such that `f(x̄) = sup_K f`"* — must be **`x̄ ∈ K`**; on `X` the claim is false as soon as `f` is unbounded off `K`. The proof repeats the slip, writing `f^{-1}(sup f(X))` where it means `sup f(K)`. |
| **E3** | Def 13.2, p. 89 | Two index slips in one definition: the injective map is typed `a : {1,…,N} → ℤ^k` (should be `ℤⁿ`), and the displayed union uses side length `2^{-k}` where the surrounding text fixes `2^{-p}`. The stray `k` propagates into the proof of Lemma 13.20 (p. 96). Harmless but confusing on first read. |
| **E4** | Def 13.55 (Gram determinant), p. 119 | *"the square root of the determinant of the `d × d` matrix `LLᵀ`, that is: `√det(LᵀL)`"*. Three problems: `d` is never introduced (it should be `m`); prose says `LLᵀ` while the formula says `LᵀL`, and for `L : ℝᵐ → ℝⁿ` with `m < n` only `LᵀL` is `m × m` and invertible — `LLᵀ` is `n × n` and singular; and naming the *square root* "the Gram determinant" is nonstandard (cf. D3). The formula is the correct one; the prose around it is wrong. |
| **E5** | Remark 14.52, p. 158 | The unit normal to an immersed disk is given as `ν(x) := ∂₁φ(x) × ∂₁φ(x) / \|∂₁φ(x) × ∂₁φ(x)\|`. A vector crossed with itself is `0`, so this reads `0/0`. Must be `∂₁φ × ∂₂φ`. Both occurrences are wrong, so it is a typo repeated, not an OCR artifact — **verified on the rendered page**. |
| **E6** | Ex 14.61, p. 164 | Asks to prove `rot(φf) = (grad φ) × F`. **The identity as stated is false** — the correct one is `rot(φF) = φ·rot(F) + (∇φ) × F`; the first term is missing. Also `f` and `F` are used for the same object in one line, and the Laplace-operator preamble is unrelated to what is asked. **Verified on the rendered page** (PDF p. 168). If this exercise is taken, state the correct identity and flag the discrepancy. |
| **E7** | Ex 10.21, p. 48 | In the `∂/∂x` line, `2e^{u+v}·0` should be `2e^{u+2v}·0`. The term is multiplied by zero so both final answers are correct — cosmetic only, but worth not copying. |
| **E8** | Thm 15.33 (Ascoli–Arzelà), p. 188 | Hypothesis says `(f_k)` bounded in `C(K,ℝ)`; conclusion says the limit lies in `C(K,ℝᵐ)`. One of the two is a typo. Our `07-compactness/06-ascoli-arzela.tex` uses `ℝᵐ` throughout and is consistent. |
| **E9** | Prop 11.24, p. 74 | Typed `f : C²(U)` for `f ∈ C²(U)`. Cosmetic. |

Nothing found rises to a mathematical error that would mislead someone who understands the
material, except **E6**, which is a false identity set as an exercise, and **E2**, which is a
false statement of Weierstrass. Those two are the ones to flag if we touch the corresponding
sections.

---

## 6. Script-only topics deliberately not given sections

Per the 2026-08-06 decision. Recorded here so the choice is visible and reversible, not lost.

| Script | pp. | Why skipped |
|---|---|---|
| §9.1.4 The reals as the completion of ℚ | 12–13 | The script itself marks it `*extra material; cf. Grundstrukturen`. Belongs to the sibling project. |
| §11.5 Fundamental theorem of algebra via minimization | 72–73 | Self-contained and pretty, but it is an *application* of Weierstrass rather than Analysis II content, and needs a section of its own to make sense. |
| Thm 14.22 + Ex 14.24–14.30 Jordan curve theorem via rotation number | 148–150 | A full section's worth. We already state Jordan–Brouwer where it is needed (`22-vector-calculus/01-bounded-c1-domains.tex:29`). |
| §13.7 partition of unity on compact submanifolds | 128–133 | We have partitions of unity (`25-pullbacks-orientability/02-integration-of-forms.tex:122`) in the form our ch. 25 needs. The script's graphical-cover machinery (Defs 13.71–13.75) is a different, heavier construction serving a definition of `∫_M f dvol_m` that we build another way. |
| §15.4 Differentiability w.r.t. initial conditions | 197–202 | We have the theorem (`appendix-a-odes.tex:339`); the script's development is one exercise plus proof. |
| §14.4 A glimpse into differential forms | 165–168 | We are *ahead* of the script here — see §2. |

**If any of these is later wanted**, the FTA-via-minimization argument (§11.5) is the one with
the best value-to-length ratio: about a page, uses only Weierstrass plus a clever local
estimate, and would sit naturally at the end of `12-extrema-hessian/`.

---

## 7. Suggested order for the enrichment passes

Highest value first. Each is one session, and each is self-contained.

1. **Chapters 2–8** (script §9, printed pp. 3–37). The largest single block of takeable
   exercises — 8 of the 11 "take first" items live here — plus divergence **D1** to fix and
   gaps **Cor 9.50**, **Lemma 9.70**, **Def 9.15**.
   **Done in full, 2026-08-07 — see §8.**
2. **Chapters 11–14** (script §§10.2–11). Gaps `Cor 10.41` (unique continuation) and
   `Prop 11.26` (Jensen), divergences **D2** and **D3**, and the strongest examples in the
   script (11.16, 11.17, 10.35). **Done in full, 2026-08-07 — see §8.**
3. **`appendix-a-odes.tex`** (script §15). Grönwall is a real gap; the three autonomous
   systems and the resonance example are the best-drawn examples in the whole script.
4. **Chapters 22–26** (script §14). Archimedes, the three-paths example, and the Stokes/Gauss
   double-computation exercises — plus errors **E5** and **E6** to flag.
5. **Chapters 19–21** (script §13). Lowest yield: our measure-theory chapters already track the
   script closely, and most of what remains is machinery we deliberately build differently.

---

## 8. Progress log

Kept so a future session (or a future pass in this one) can resume without re-deriving what's
already done. Update this section, don't just delete finished lines — the "not yet started"
list at the bottom is the actual todo.

### Done — 2026-08-07

* **D4** (script's `|x|`-for-Euclidean / `‖·‖`-for-non-standard convention, Remark 9.94 p. 31,
  verified on the rendered page) — `ainote` in
  [`02-metric-normed-inner-product/01-structured-spaces.tex`](content/02-metric-normed-inner-product/01-structured-spaces.tex),
  right after `def:norm`.
* **Ex 9.33–9.35 skip reason** (user-requested, not originally in this file's own todo) —
  `ainote` in
  [`06-completeness/01-completeness.tex`](content/06-completeness/01-completeness.tex), right
  after `def:complete_metric_space`, explaining the dependency on script §9.1.4 and pointing at
  §6 above.
* **Chapter 2 (`02-metric-normed-inner-product/`) — done in full:**
  Ex 9.5 (polygon inequality, `ex:polygon_inequality`), Ex 9.18 (convergence survives concave
  reshaping, `ex:reshaping_same_convergence`, companion to the already-present
  `prop:concave_reshaping_metric` = Ex 9.8), Ex 9.11 (Manhattan street-grid story, as a
  `remark`), Ex 9.13 (the sphere's chord metric $d_0$ vs.\ geodesic metric $d_1$ made explicit,
  `rem:sphere_two_metrics`), Ex 9.103 ($\mathbb{R}[x]$ infinite-dimensional,
  `ex:polynomials_infinite_dimensional`, placed next to `ex:3.9`/norm equivalence). All four
  exercises have solutions in the chapter's `99-solutions.tex`, in document order.
* **Chapter 3 (`03-open-and-closed-sets/`) — done in full:**
  Example 9.38 (clopen sets other than $X,\emptyset$ on $(0,1)\cup(2,3)$,
  `ex:clopen_nontrivial`, forward-references `ch:connectedness`) and Ex 9.46 (closure/boundary
  of a general ball in $\mathbb{R}^n$, `ex:closure_boundary_of_ball`, generalising the $r=1$
  case already in `ex:interior_closure_boundary_more`\textbf{(b)}), with the latter's solution
  in `99-solutions.tex`.
* **D1** fixed — `07-compactness/02-compact-subsets.tex`: retitled `[9.63, ...]` to
  `[Definition 9.62, ...]` and restored the missing third \qt{complete + totally bounded}
  condition, with an `ainote` explaining the discrepancy.
* **Lemma 9.70** (nesting principle) — added as `lem:nesting_principle` in
  `07-compactness/01-open-covers.tex`, with the script's proof (both directions) and a remark
  connecting it to `def:compact_metric_space` via De Morgan.
* **New section, reversing the 2026-08-06 \qt{enrich existing sections only} decision for this
  one topic (user instruction, 2026-08-07):** completion of a metric space (script Def 9.32,
  Ex 9.33–9.35), transcribed in full as a new
  `content/06-completeness/02-completion-of-a-metric-space.tex`, with all three exercises
  solved in `99-solutions.tex`. `content/06-completeness/03-contraction-mappings.tex` is the
  old `02-contraction-mappings.tex`, renumbered to make room (git-tracked rename, no content
  change). The chapter-level `ainote` explaining the skip (in `01-completeness.tex`) is updated
  accordingly. The script's own $\mathbb{R}$-from-$\mathbb{Q}$ specialisation (§9.1.4) is
  \emph{still} not built — it remains explicitly out of scope, pointing at the sibling
  \emph{Grundstrukturen} project, per the unchanged §6 entry above.
* Build verified clean (`latexmk -jobname=check`, 255 pages, no errors) after every change
  above. One real bug was caught and fixed in the process: an exercise title
  `[$\mathbb{R}[x]$ is infinite-dimensional]` broke LaTeX's optional-argument bracket matching
  (the literal `[x]` inside closed the `\begin{exercise}[...]` argument early) — fixed by
  brace-protecting to `\mathbb{R}{[}x{]}`. Worth remembering for any future title containing a
  literal `[` or `]` in math.

### Session 1 (chapters 2–8) — DONE, 2026-08-07

All items finished. Cor 9.50 (`cor:same_topology_same_convergence`, ch 4, with a supporting
`lem:convergence_is_topological`) and Def 9.15 "eventually" (`not:eventually`, ch 4). E2 ainote
added next to `item:extreme_value_theorem` in ch 7. Ex 9.56 landed as
`cor:closed_iff_zero_of_distance` in ch 5 (kept short — it mostly restates already-transcribed
`ex:2.3` and `ex:distance_to_point_continuous`, adding only the missing \qt{iff} direction, to
avoid the kind of duplication `supplements.md` warns about). Ex 9.76 turned out to duplicate
`ex:3.4`\textbf{(b)} (already in ch 7) in substance; resolved by cross-referencing from ch 6
instead of re-proving, with the script's more elementary segment-based proof added as a bonus
`ainote` on `ex:3.4`'s solution. Ex 9.60 (`ex:banach_hypotheses_sharp`, ch 6) and Ex 9.26
(`ex:cauchy_elementary_facts`, ch 6) taken directly. Ex 9.68
(`ex:totally_bounded_implies_bounded`, ch 7) and Ex 9.65 (`ex:rationals_not_compact`, ch 7,
using the corrected $\mathbb{Q}\cap[0,2]$ set noted in §3 above) taken directly. Ex 9.81 generalised
beyond the pairwise case already present as `ex:connectedness_tf`\textbf{(a)}: added
`cor:union_connected_common_point` (arbitrary unions) and `def:connected_component` (ch 8). Ex
9.85 added as `cor:ivt_general_connected` (ch 8), the connected-space generalisation of the
already-present interval-only IVT.

Build verified clean throughout (latest: 263 pages, no errors, no undefined references).

### Session 2 (chapters 11–14) — DONE, 2026-08-07

Cor 10.41 (`cor:unique_continuation`, ch 11, with the bump-function remark on why analyticity —
not just $C^\infty$ — is needed) and Prop 11.26 (`prop:jensen_inequality`, ch 14, cross-linked
to the silent use of Jensen already in ch 2's `ex:4.4` solution). D2 and D3 both turned out to
already have partial `ainote`s in place (D2 at `02-hessian-test.tex` on the $C^3$-vs-$C^2$
regularity, D3 implicitly in the Gram-determinant section) — both enriched with the script
citation and, for D3, the E4 write-up of the script's own inconsistency (undefined $d$, $LL\transp$
vs $L\transp L$). Ex 10.36 landed as two new sub-exercises (`exp(arctan(x-y))`,
`1/(1-x^2-y^2)`) completing an already-present partial match (`sin(xy)` and
`sqrt(1+x+y^2)` were already there) rather than duplicating it. Ex 11.14 (polarisation formula,
`ex:polarisation_formula`) and Ex 11.22 (antipodal points maximise sphere distance,
`ex:antipodal_max_distance`) taken directly. Ex 11.16 turned out to already be present in
substance (`x^4+y^4` vs `x^4-y^4`); enriched with a remark generalising to the script's
`ax^4+by^4` family. Ex 11.17 (two-parameter family through all four Hessian cases) taken
directly. Ex 11.18 and Ex 11.25 were **already fully present** — Ex 11.18 is verbatim
`ex:cubic_saddle_family` (Corsin's own exercise happens to be the same one the script sets), and
Ex 11.25 is exactly parts (b) and (c) of the already-transcribed `ex:convexity_characterizations`
— no new content needed for either.

Build verified clean: 268 pages, no errors, no undefined references.

* **Session 3** (`appendix-a-odes.tex`): entirely open — see §7 item 3.
* **Session 3** (`appendix-a-odes.tex`): entirely open — see §7 item 3.
* **Session 4** (chapters 22–26): entirely open — see §7 item 4.
* **Session 5** (chapters 19–21): entirely open — see §7 item 5.
