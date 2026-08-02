# Figure queue

Every hand-drawn diagram found while transcribing gets an entry here instead of being
inlined as ASCII. TikZ is done in one dedicated pass (Phase 4.3) so it never blocks prose.

**ID scheme:** `FIG-WNN-mm` (week, running number). Appendix figures use `FIG-APA-mm`.

**Status:** `queued` → `drafted` → `done`

| ID | Source | Description | Kind | Status |
|---|---|---|---|---|
| FIG-W02-01 | Corsin Week 2, p. 3 | Nested-ovals diagram: topological ⊃ metric ⊃ normed vector ⊃ inner product spaces | Concentric labelled ellipses | queued |
| FIG-W02-02 | Corsin Week 2, p. 3 | Triangle inequality: points x, y, z with blue path x→y→z and red direct edge x→z | 2D sketch on axes | queued |
| FIG-W02-03 | Corsin Week 2, p. 5 | Manhattan / Euclidean / supremum metric in ℝ²: right triangle with d₁ red, d₂ blue, d₃ orange | 2D sketch on axes | queued |
| FIG-W02-04 | Corsin Week 2, p. 5 | Sphere S²: geodesic arc between x and y vs. straight-line Euclidean chord | 3D sphere, two views | queued |
| FIG-W02-05 | Corsin Week 2, p. 8 | Open/closed/neither in ℝ²: three squares with converging sequences xₙ, yₙ and their limits | 3 sub-panels | queued |
| FIG-W02-06 | Corsin Week 2, p. 8 | "Common misconception": ε-ball at a boundary point of [0,1]², spilling out (left) vs. clipped to the subspace (right) | 2 panels | queued |
| FIG-W02-07 | Corsin Week 2, p. 10 | The "ε-tube": curve f on [0,1] with red dotted envelopes at ±ε/3 | Plot + offset envelopes | queued |
| FIG-W02-08 | Corsin Week 2, p. 11 | Unit balls B₁(0) ⊂ ℝ²: square (supremum metric) vs. diamond (Manhattan metric) | 2 panels on axes | queued |
| FIG-W02-09 | Corsin Week 2, p. 14 | Open cover of a metric space: blob X tiled by three dotted regions U₁,U₂,U₃ | Freeform regions | queued |
| FIG-W02-10 | Corsin Week 2, p. 14 | Open cover of a **subset**: K ⊆ U₁∪U₂∪U₃ ⊆ X, the Uᵢ extending past K | Freeform regions | queued |
| FIG-W03-01 | Corsin Week 3, p. 3 | Weierstrass: continuous f on [a,b] with absolute max f(c) (red) and min f(d) (blue) — *pasted stock image, must be redrawn* | Plot | queued |
| FIG-W03-02 | Corsin Week 3, p. 4 | Disconnected (two blobs, two dashed open sets) vs. connected (one blob, "small gap" between the covering sets) | 2 panels, freeform | queued |
| FIG-W03-03 | Corsin Week 3, p. 5 | V₁ ∪ V₂ sharing x₀, enclosed in U₁; disjoint U₂ annotated "no intersection" | Freeform regions | queued |
| FIG-W03-04 | Corsin Week 3, p. 6 | Unit circle S¹ and segment [−1,1]×{0}; intersection = {(±1,0)} | 2D sketch on axes | queued |
| FIG-W03-05 | Corsin Week 3, p. 7 | Topologist's sine curve sin(1/t) on (0,0.2] | pgfplots, dense sampling | queued |
| FIG-W03-06 | Corsin Week 3, p. 8 | Same curve, annotated twice: open U around 0; the points γ(aₙ) on the crests y = 1 | pgfplots + annotations | queued |
| FIG-W03-07 | Corsin Week 3, p. 10 | Change of basis (rotation) aligning x with the horizontal axis, angle θ preserved | 2 panels + arrow | queued |
| FIG-W03-08 | Corsin Week 3, p. 11 | Projection π_v(u): u, v, angle θ, perpendicular dropped onto span(v) | 2D sketch | queued |
| FIG-W04-01 | Corsin Week 4, p. 4 | Unit circle with the point γ(π/4) and its orange tangent (velocity) arrow | 2D sketch on axes | queued |
| FIG-W05-01 | Corsin Week 5, p. 2 | Paraboloid f(x,y) over the xy-plane, purple level sets, orange gradient arrow, green minimum, red steepest-ascent arrow | 3D surface + contours | queued |
| FIG-W09-01 | Corsin Week 9, p. 2 | Parallelogram (0, x, x+y, y) with x = x₁e₁, showing area = \|det(x\|y)\| | 2D sketch on e₁/e₂ axes | queued |

*(populated during Phase 2)*

## Reference assets

`Toby Lane/geogebra/*.ggb` are interactive GeoGebra constructions covering several of the
same ideas — useful as visual references when drawing:

| File | Relates to |
|---|---|
| `gradient_contour.ggb` | FIG-W05-01 |
| `directional_derivative.ggb` … `directional_derivative4.ggb` | Week 4 (differential) |
| `extremum-quiz-1.ggb`, `extremum-quiz-2.ggb` | Week 5–6 (optimization) |
| `diff_not_allpd.ggb` | Week 4 (partials exist but not differentiable) |
