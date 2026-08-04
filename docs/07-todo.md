# TODO — next session

## Transcription (primary, per gemini.md priority)
- [x] Corsin Week 8 — fully transcribed (pp. 1–13: quiz Q1–Q7, change of
      variables, Fubini, Feynman). Priority page + exercise statements 8.2, 8.4,
      8.5 in. **Still open:** `sec:week08_solutions` is empty — solutions to
      8.2/8.4/8.5 not yet written (Sol8_Analysis2_eng.pdf not read).
- [ ] Corsin Weeks 9–13 + ODE appendix
- [ ] `latexmk` to 0 errors after each week

## Started but not finished (from the Weeks 1–7 review, docs/08-latex-review.md)
Items where a proof/argument *exists in the document* but has a hole or is
unreadable — worth finishing, unlike items that are merely unproved:
- [ ] **C5a** `week-02.tex` — proof that `C⁰([0,1])` is closed asserts its crux:
      "if sup|f−g| < ε/3 and f jumps by ε then g jumps by ≥ ε/3" is stated, not
      shown. One line of triangle inequality; it is the only line with content.
- [ ] **C5b** `week-02.tex` — Lebesgue-number proof conflates `r := ½·sup{…}`
      with the un-halved sup. Shows `R(y) ≥ r(x) − d(x,y)`, concludes it for `r`.
      Result is true (r is even ½-Lipschitz); the written argument is not. 2 symbols.
- [ ] **C6a** `week-03.tex` — "S is connected" for the topologist's sine curve
      does not parse ("U∖{0} is also open" is true and irrelevant; the
      contradiction never appears). Rewrite at the same length.
- [ ] **C6b** `week-03.tex` — "thus aₙ → 0" is asserted; the IVT gives *some*
      aₙ, not a null sequence. **Decision: do NOT prove.** Add one clause
      ("choose aₙ smallest, so aₙ ↓ 0") and leave it — the honest fix needs a
      sup-of-the-zero-set argument that costs half a page and buys little here.
- [ ] **C7** `week-04.tex` — "a nonzero linear map cannot decay along its own
      domain" is doing too much work in one parenthesis. One clause: pick h with
      L(h) ≠ 0, then L(th)/|th| = L(h)/|h| is a nonzero constant.
- [ ] **F3** — 47 `\implies`, the subset acting as sentence connectives rather
      than joining equations (`week-05.tex:26` `\iff` + slash carrying two
      definitions; `:612`, `:625`; `week-06.tex:676`).
- [ ] **F5** — normalise the `Gemini 3.6 Flash`-marked blocks: single unbroken
      paragraphs with mid-sentence arrows, next to Sonnet-marked ones broken
      into labelled cases. No maths changes.

## Enrichment pass (same as done for Weeks 2–7)
- [ ] Per new week: missing standard defs/theorems the tutor only uses but never
      states; new subsections; transition sentences; heavy `\cref` (incl. cross-week)

## Sascha Brack — class notes: WEEKS 1–4 COMPLETE

All six files covering our Weeks 1–4 have been read and mined. **Do not re-read them.**
`Week_02_Notes_Monday_Updated.pdf`, `Week_02_Notes_Friday_Updated.pdf`,
`Week_03_Notes_Monday.pdf`, `Week_03_Notes_Friday.pdf`,
`Week_04_Notes_Monday_Updated.pdf`, `Week_04_Notes_Friday_Updated.pdf`.

Note the heavy repetition (see the merge rule in `gemini.md`): his Week 3 files are almost
entirely our Week 2 material plus a preview of our Week 4, and his Week 4 Friday is ~80% a
repeat of his own Monday. Only the *additions* were taken.

**Remaining for weeks 5–8:** `Week_05_*` (17 p), `Week_06_*` (10 p),
`Week_07_Notes_Monday.pdf` (2 p), `Week_08_*` (16 p) — 45 pages, best done fresh.

## Diego Torres Tejeda — one find logged, not yet integrated

- [ ] **`Notes - 06.03`, p. 2 — completeness is not a topological property.** An exercise:
      on $X=(0,\infty)$ compare $d_{\text{Eucl}}$ with $d(x,y) := \lvert 1/x - 1/y\rvert$.
      Show (1) $d$ is a metric, (2) $(X,d_{\text{Eucl}})$ is **not** complete, (3) $(X,d)$
      **is** complete, (4) both induce the **same topology**. This is the exact analogue of
      `rem:boundedness_not_topological` in Week 3, and would complete the trio: compactness
      **is** topological, boundedness and completeness are **not**. Would slot next to
      `rem:complete_vs_closed` in `week-02.tex`. His p. 1 also frames it well: "topological
      properties (continuity, convergence, compactness, connectedness) are the same regardless
      of the norm; however some properties are not topological, e.g. completeness."
- Diego's remaining unread files for weeks 2–4: `23.02` (10 p), `27.02` (16 p), `02.03` (13 p),
  `09.03` (8 p), `13.03` (6 p). Already mined: the Addendum, `16.03`, `30.03`.

## Sascha Brack — class-notes mining (superseded by the section above)

**Read so far:** `Week_02_Notes_Friday_Updated.pdf` (10 p), `Week_03_Notes_Monday.pdf` (7 p),
`Week_04_Notes_Monday_Updated.pdf` (11 p). `Week_02_Notes_Monday_Updated.pdf` was mined earlier
for the accumulation-point counterexample now in `week-02.tex`.

**Still to read (weeks 4–8):** `Week_03_Notes_Friday.pdf` (7 p),
`Week_04_Notes_Friday_Updated.pdf` (10 p), `Week_05_*` (17 p), `Week_06_*` (10 p),
`Week_07_Notes_Monday.pdf` (2 p), `Week_08_*` (16 p).

**Taken:** the sufficient condition for differentiability + implication chain + recipe
(`week-04.tex`, `sec:sufficient_condition_differentiability`).

**Found but NOT yet integrated** — all verified as genuine gaps by grep:
- [ ] **The open/closed/compact/complete classification table** (Week 2 Friday p. 8, repeated
      Week 3 Monday p. 3). ~11 subsets of $\mathbb{R}^n$ to classify in four columns:
      `[0,1]`, `Q`, `B_1(0)⊆R³`, `B_1(0)∩B_1(1)⊆R²`, `{0}∪{1/n}`, `⋃_n B_{1/n}(n)`,
      `(-∞,1]`, `f([0,1])`, `f⁻¹([0,1])`, `f⁻¹((0,1))`, `S=span((1,0),(3,0))`,
      `{x∈R³ : d(x,S)<1}`. Exactly the "simple but illustrative corner cases" format —
      would make an excellent `aiexercise` in Week 3 **with a solution table**.
- [ ] **Arbitrary unions / finite intersections of open sets are open** (and the dual for
      closed). Sascha's Lemmas 1.21–1.22. **Absent from `week-02.tex` entirely** — these are
      foundational and currently missing.
- [ ] **A closed subset of a compact set is compact** (his Corollary 1.37.3, with a neat proof
      adding `X∖A` to the cover). Also absent.
- [ ] **Continuity contrast pair** (Week 3 Monday p. 7): `xy/(x²+y²)` vs `x²y²/(x²+y²)` at the
      origin — the first discontinuous, the second continuous, both settled by polar
      coordinates. Our Week 4 has only the first; the pair is what shows the method
      discriminates.
- [ ] **Norm equivalence** (Week 3 Monday p. 6): Def 9.105 + Thm 9.107 "all norms on `R^n` are
      equivalent", with proof strategy. Check whether `week-03.tex` covers it.

## Second-tutor mining (only on clear hits, ~30% hit rate so far)
- [ ] Linus Lüchinger: sessions 5–9, 11, 13+ not yet checked
      (mapping: session 3 ~ Week 2, +1 session per week roughly)
- [ ] Diego Torres Tejeda: handwritten notes 06.03, 13.03, 20.03, 27.03 not yet checked
      (his typed "Addendum" file was the best find — check for other typed docs first)
- [x] Tim Fessler: confirmed no new substance, skip entirely

## TikZ figures
- [x] FIG-W06-01..07, FIG-W07-01..06 — done, in docs/05-figure-queue.md
- [ ] FIG-W08+ pre-logged as "queued" in docs/05-figure-queue.md, waiting on
      transcription of those weeks first

## Candidate spots for an original (not-from-source) TikZ, not yet drawn
- Week 3: a small picture for the Lipschitz-continuity hierarchy remark
  (Lipschitz => uniformly continuous => continuous), e.g. nested implication arrows
  or a Venn-style diagram of function classes with sqrt(x) placed in the uniform-only ring
- Week 2: the totally-bounded proof (finite ε-net construction) would benefit from
  a picture of the inductive ball-covering process
- Week 7: the "tangent vectors as velocities of curves" proposition could use a
  sketch of a curve through p with its velocity vector, next to the parametrization-basis
  picture already drawn (FIG-W07-04)

## Open / undecided
- Whether to eventually sweep the other 16 tutors systematically once all Corsin
  weeks are done, vs. staying ad-hoc (current approach)
