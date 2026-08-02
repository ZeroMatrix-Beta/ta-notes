# Analysis II — TA Notes → Typeset Document

> ## ⚠️ PHASE ORDER CORRECTION — supersedes the numbering below
>
> The phases below number **supplement-mining as Phase 3, ahead of the LaTeX build**. That is
> wrong for this project's actual priority and must not be followed.
>
> The user's standing instruction is that **Corsin Nick alone is the deliverable**: *"If
> everything from Corsin Nick is transcribed nicely and you just have a look at the others,
> that's fine for me."* So the other 16 tutors are touched **only after a PDF compiles**.
>
> **Correct order:** scaffolding → transcribe Corsin (weeks 2–13 + ODEs) → retarget `main.tex`
> and convert to LaTeX → **build until it compiles** → TikZ figures → *then, optionally,*
> supplements.
>
> Read the phase descriptions below for their *content*; take the *ordering* from the table in
> `CLAUDE.md`. Everything from "Phase 3 — Topic index & curated supplements" onwards is
> renumbered accordingly: it is now the last step, and it is optional.

> **Amendments after approval (2026-08-02).** Two additions from the user:
>
> 4. **Official course material acquired.** The whole of
>    <https://metaphor.ethz.ch/x/2026/fs/401-1262-07L/> is public. Downloaded into
>    `exercises/`: problem sets `Ex1–13` and solutions `Sol1–13` (**English**),
>    `lec_notes.pdf` (the official lecture notes — the authority for chapter and theorem
>    numbering), `DiffComp.pdf`, and the two past exams. This closes the biggest gap in the
>    original plan: Corsin's *Recommended exercises* pages reference problems by number
>    only (`9.3 ▨`), which was untranscribable without the statements.
> 5. **Exercises are quoted in full.** Each week opens with the complete problem sheet,
>    verbatim from the official English PDF, each problem tagged with Corsin's colour-coded
>    priority — with cross-TA agreement surfaced where Sascha Brack or Simon Kamps
>    independently flag the same problem. Details in `04-style-guide.md §2`.
>
> Both are reflected in `02-source-inventory.md` and `04-style-guide.md`.

## Context

`C:\Users\miche\latex\ta-notes` holds the exercise-class notes of **17 teaching assistants**
for **ETH D-MATH, Analysis II: Several Variables (Prof. J. Serra, FS 2026)** — roughly
1500 PDF pages in every conceivable format (digital handwriting, photo scans, typeset
LaTeX, Beamer, PowerPoint; English and German).

The goal is one polished LaTeX document. Two root files already exist and are the
starting point:

- `main.tex` — a fully developed preamble (purple/olive theme, aliascnt theorem setup,
  cleveref, fancyhdr, titlepage with an AI-disclaimer box). Currently targets a
  *Linear Algebra I/II* project and `\input`s 32 non-existent `content/*.tex` files.
- `gemini.md` — a house-style prompt that worked well on a previous
  handwritten→LaTeX transcription. Its LaTeX/prose rules carry over; its LinAlg-specific
  notation rules do not.

**Decisions taken** (user, this session):

1. **Structure: by week.** Corsin Nick's weekly notes are the blueprint. Caveat the user
   raised explicitly: *other tutors do not teach the same material in the same week*, so
   merging is **not** week-aligned — supplements must be matched by **topic**, not by date.
2. **Scope: Corsin fully + curated supplements.** All ~137 pages of Corsin Nick get
   transcribed. A shortlist of other tutors is mined only for content Corsin lacks.
3. **Language: English throughout** — but German technical terms are mirrored where they
   add value. On the first introduction of a concept, give the German term alongside the
   English one using the `\germanterm{…}` macro that `main.tex:174` already defines
   (renders as *„…"* in the bold accent colour), e.g. *a __compact__ set (\germanterm{kompakte Menge})*,
   *the __implicit function theorem__ (\germanterm{Satz über implizite Funktionen})*. This makes the
   document usable next to the German lecture/exercise material. In the Markdown transcripts
   the same thing is written `**compact** ("kompakt")` so the conversion is mechanical.
   Jérôme Paschoud's topic-named German files are the source for the canonical German wording.

**Deliverable order (user's explicit request):** plaintext/Markdown transcription *first*,
with a source pointer (tutor / file / page) on every block, so nothing gets lost; LaTeX
conversion only afterwards.

---

## Why Corsin Nick is the right blueprint

Verified by sampling `Week 2/3/5/9.pdf`: digital handwriting, very legible, English,
consistently structured — cover page → *Recommended exercises* (hints for that week's
problem sheet, with an important/semi-important/optional colour code) → `Monday` /
`Friday` session headings → topic headings → `Thm:` / `Def` / `Exercise:` / `Solution:`
blocks, plus hand-drawn diagrams. 13 files, ~137 pages:

| File | Pages | Topic (cross-checked against Jérôme Paschoud's topic-named files) |
|---|---|---|
| Week 2 | 15 | Structured spaces, metric spaces, open/closed sets, topology, continuity |
| Week 3 | 12 | Compactness, Heine–Borel, Banach fixed point, connectedness |
| Week 4 | 13 | Norms, the differential, chain rule |
| Week 5 | 11 | Taylor, optimization (critical points, gradient) |
| Week 6 | 12 | Optimization II, inverse function theorem |
| Week 7 | 10 | Implicit function theorem, submanifolds |
| Week 8 | 13 | Tangent spaces, Jordan measure, Riemann integral |
| Week 9 | 8 | Change of variables, length/area/volume, d-volume |
| Week 10 | 12 | Integrals over submanifolds, divergence theorem |
| Week 11 | 15 | Divergence theorem & Green, line integrals |
| Week 12 | 7 | Differential forms |
| Week 13 | 9 | Stokes, ODEs |
| Analysis 1 lesson on ODEs | 13 | ODE recap → appendix |

⚠️ **Numbering trap:** the cover of `Week 2.pdf` reads *"Class notes Week 1"*, while
`Week 3.pdf` and `Week 9.pdf` read *"Week 3"* / *"Week 9"*. **The file name is canonical**
(it matches every other tutor's week/date indexing). Do not follow the Week-2 cover.

---

## Target file structure

Everything new lives under `C:\Users\miche\latex\ta-notes`. Source PDF folders are never
modified.

```
ta-notes/
├── main.tex                     ← retargeted (see Phase 4)
├── CLAUDE.md                    ← new: points at docs/, so future sessions load the style guide
├── gemini.md                    ← left untouched (historical reference)
├── docs/
│   ├── 00-implementation-plan.md   ← this plan, checked into the project
│   ├── 01-file-structure.md        ← layout + naming conventions + build instructions
│   ├── 02-source-inventory.md      ← all 17 tutors: files, pages, format, language, verdict
│   ├── 03-topic-index.md           ← topic → Corsin week + supplement pointers (the merge key)
│   ├── 04-style-guide.md           ← gemini.md rewritten for Analysis II
│   ├── 05-figure-queue.md          ← every diagram to be redrawn in TikZ, with an ID
│   └── 06-open-questions.md        ← illegible passages, suspected errors, judgement calls
├── transcript/                     ← PHASE 2/3 OUTPUT: plaintext, source-annotated
│   ├── week-02.md … week-13.md
│   ├── appendix-a-odes.md
│   └── supplements/
│       ├── toby-lane.md, lukas-krause.md, toprak-erakay.md,
│       └── sascha-brack.md, damien-lesieur.md
└── content/                        ← PHASE 4 OUTPUT: the actual LaTeX
    ├── week-02.tex … week-13.tex
    ├── appendix-a-odes.tex
    └── appendix-b-glossary.tex   ← English↔German term glossary
```

---

## Transcript format (the core convention)

One Markdown file per week. Every content block carries its provenance; nothing is written
without a page pointer. Header of each file:

```markdown
# Week 5 — Taylor & Optimization

**Primary source:** `Corsin Nick/Class Notes/Week 5.pdf` (11 pp)
**Lecture chapters:** 10–11
**Status:** transcribed ☐ · figures logged ☐ · supplements merged ☐ · LaTeX ☐
```

Body conventions:

- Session headings `## Monday` / `## Friday` exactly as Corsin marks them.
- Topic headings `### Optimization` verbatim from the notes.
- Every block ends with a page pointer: `*(Corsin p. 4)*`. Multi-page blocks: `*(Corsin pp. 4–5)*`.
- Math in `$…$` / `$$…$$` — already valid LaTeX, so Phase 4 is mostly mechanical.
- Diagrams are **not** transcribed as ASCII. They get a stub that is also logged in
  `docs/05-figure-queue.md`:
  `> **[FIG-W05-01]** *(Corsin p. 2)* Paraboloid over the xy-plane, level sets in purple, gradient arrow at the minimum. → TikZ (3D surface + contours).`
- Uncertain readings: `⟨?word⟩`, and a line in `docs/06-open-questions.md`.
- Suspected mathematical errors in the source: `> ⚠️ **Check:** …` inline **and** in
  `06-open-questions.md` — never silently "fixed".
- Supplements from other tutors: `> **[SUPP]** *(Lukas Krause, Week 6, p. 12)* …`,
  inserted at the topic where it belongs, regardless of which calendar week that tutor taught it.

---

## Phases

### Phase 1 — Scaffolding (no PDF reading)

Create `docs/` with all six files. Contents that are already known:

- `02-source-inventory.md`: the full 17-tutor survey (files, page counts, format,
  language, legibility, verdict) — data already gathered this session, including the note
  that `ANALYSIS II MICHAELS.pdf`, `Analysis_II_2024.pdf` / `Lecture_2024.pdf` and Corsin's
  `Books/` are third-party/official material, **excluded** from transcription and cited only.
- `04-style-guide.md`: port from `gemini.md` — keep the LaTeX/environment/prose rules
  (`\newterm`, `\qt`, `:=` for definitions, descriptive `\label` slugs, `\cref`,
  display-math splitting, "iff"→"if and only if", commas after introductory adverbs,
  `tikz-cd`, alphabetical sub-part labels via `enumerate[label=\textbf{(\alph*)}]`);
  drop the LinAlg-only rules (representation matrices, EROs, Fibonacci, `\ColS`/`\RowS`);
  add Analysis II conventions: `(X,d)` metric spaces, `B_r(x)`, `\overline{A}`,
  `\partial A`, `\mathrm{int}(A)`, `Df(x_0)` vs `\nabla f`, `\|\cdot\|`, `C^k(U,\mathbb{R}^m)`,
  new operators `\dist`, `\diam`, `\supp`, `\vol`, `\divg`, `\curl`, `\Jac`; and the German-mirroring
  rule (`\germanterm{…}` on first introduction, Decision 3) plus a running English↔German
  glossary table that grows during Phase 2 and ends up as an appendix.
- `01-file-structure.md`: layout above + the build command.
- Empty stubs for `03`, `05`, `06` and for `transcript/week-*.md`.

Fully creatable without opening a single PDF.

### Phase 2 — Transcribe Corsin Nick (the bulk of the work)

Week by week, `Week 2.pdf` → `Week 13.pdf`, then `Analysis 1 lesson on ODEs.pdf` →
`appendix-a-odes.md`. Per week: read the PDF in batches of ≤6 pages (`Read` with `pages`),
write `transcript/week-NN.md` in one pass, append figures to `05-figure-queue.md` and
oddities to `06-open-questions.md`, then tick the status line.

Fidelity rule inherited from `gemini.md`: **stay ≥80% faithful to Corsin's logic, wording
and proof structure**; expand shorthand (`s.t.`, `w.r.t.`, `iff`) into full academic prose,
but never substitute a textbook proof for his.

12 weeks + appendix ≈ 137 pages. This is the long pole and should be checkpointed after
every week (each week's file is independently useful).

### Phase 3 — Topic index & curated supplements

1. Build `docs/03-topic-index.md` from the finished transcripts: one row per topic →
   the Corsin week/section that owns it. This is the merge key that resolves the
   week-misalignment problem — supplements attach to a **topic**, never to a date.
2. Mine the shortlist, in this order, **only for gaps**:
   - **Toby Lane** — `class-document.pdf`, 100 pp typeset English course companion, has a
     TOC; plus 8 GeoGebra files (unique visual assets, worth referencing/redrawing).
   - **Lukas Krause** — 144 pp typeset English textbook-style notes, weeks 2–13 (week 8 missing).
   - **Damien Lesieur** — 21 pp typeset, lemma numbers matching the lecture (`9.19`, …):
     the cheapest way to pin our statements to official lecture numbering.
   - **Toprak Erakay** — 322 pp, very legible handwriting, detailed worked exercise solutions.
   - **Sascha Brack** — 187 pp class notes (Mon+Fri) + 8 annotated exercise-sheet hint PDFs.

   The three typeset sources are text-extractable (`pdftotext`), so they cost almost nothing —
   do those first and only fall back to image reading for Toprak/Sascha where a real gap remains.
3. Everything else is **skipped**, and `02-source-inventory.md` records *why* (German +
   poor legibility: Maarten Cnoops; slide shells with little derivation: Tim Fessler;
   5 pages: Riccardo Vanoni; duplicates of Corsin's coverage: the rest).

### Phase 4 — LaTeX

1. **Retarget `main.tex`** — it is otherwise sound and should be preserved:
   - Title block: `Linear Algebra I/II` → `Analysis II: Several Variables`;
     `Prof. Dr. Paul Biran` → `Prof. Dr. Joaquim Serra`; subtitle → "Exercise-Class Notes";
     add a credit line naming Corsin Nick as primary author of the transcribed notes and
     the supplement tutors. Keep the AI-disclaimer `tcolorbox` verbatim — it applies here too.
   - Replace the 32 LinAlg `\input` lines with `content/week-02.tex … week-13.tex` +
     `\appendix` + `content/appendix-a-odes.tex` + `content/appendix-b-glossary.tex`.
   - Drop the LinAlg-only operators (`\ColS`, `\RowS`, `\Fib`, `\Orth`/`\Unit`/`\SOrth`/`\SUnit`,
     `\transp` may stay — it is used for Jacobians); add the Analysis II operators listed in Phase 1.
   - Keep the existing theorem/`aliascnt`/`cleveref` machinery **unchanged** — the comments in
     `main.tex:344–415` document real bugs that were already solved there; do not regress them.
   - Theorem numbering: the preamble prints `Chapter.SectionLetter.Number`. With weeks as
     chapters that yields e.g. `5.b.3`, which is fine and needs no override.
2. Convert `transcript/week-NN.md` → `content/week-NN.tex`, one week at a time, applying
   `docs/04-style-guide.md`. Corsin's `Exercise:` / `Solution:` pairs map onto the existing
   `exercise` and `exercisesolution` environments; his *Recommended exercises* cover page
   becomes an opening `\subsection*{Recommended exercises}` per week.
3. Work the `05-figure-queue.md` in a dedicated pass — TikZ is the slowest part and must
   not block the prose.

### Phase 5 — Build & proofread

Compile, fix over/underfull boxes and any `cleveref`/label collisions, sanity-check that
every `\label` slug is unique and every figure stub has been resolved.

---

## Verification

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

MiKTeX is installed (`pdflatex`, `lualatex`, `latexmk` all present at
`C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`). Checks:

- Document compiles with zero errors; `main.log` free of undefined references/citations.
- TOC lists 12 week chapters + the ODE appendix, in order.
- Spot-check three transcribed pages against their PDF originals (one per format class:
  a definition-heavy page, a proof page, a figure page).
- `docs/05-figure-queue.md` and `docs/06-open-questions.md` are both fully triaged — no
  `TODO` left un-triaged, remaining items explicitly marked as accepted-open.
- Page-pointer audit: every `\begin{theorem}`-class environment in `content/` traces back
  to a page pointer in the matching `transcript/` file.

## Out of scope

- The four books under `Corsin Nick/Books/` and the copies of the official lecture notes
  (`ANALYSIS II MICHAELS.pdf`, `Analysis_II_2024.pdf`, `Lecture_2024.pdf`) — cited, never transcribed.
- `Buch_Analysis_1_Michaels.pdf` (Analysis I), `Physik_II_Formelsammlung.pdf`,
  `Codes_Datenanalyse_Pruefung_Noah.ipynb` — different courses.
- The 12 German/low-legibility/low-density tutors listed in Phase 3.3.
