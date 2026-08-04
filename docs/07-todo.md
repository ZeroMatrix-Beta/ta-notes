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
