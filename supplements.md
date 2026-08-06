# Supplement coverage

Which of the 16 non-Corsin tutors' notes have been read and mined into `content/`.
Corsin Nick is the blueprint, transcribed chapter-by-chapter, so he is not tracked here.

Route any supplement by **topic**, never by the tutor's own week number or file date — their
weeks do not line up with ours. See the merge rule in `gemini.md`.

## Sascha Brack — weeks 1–4 COVERED

All six files read and mined. **Do not re-read them:**
`Week_02_Notes_Monday_Updated`, `Week_02_Notes_Friday_Updated`, `Week_03_Notes_Monday`,
`Week_03_Notes_Friday`, `Week_04_Notes_Monday_Updated`, `Week_04_Notes_Friday_Updated`.

Taken: the open/closed/compact/complete classification table (→ Wk 3); the union/intersection
lemmas and "a closed subset of a compact set is compact" (→ Wk 2); ℝⁿ completeness with proof
(→ Wk 2); the sufficient condition for differentiability with its implication chain and
checking recipe (→ Wk 4); the `xy/(x²+y²)` vs `x²y²/(x²+y²)` contrast pair (→ Wk 4); the chain
rule as a sum over paths (→ Wk 4).

Expect heavy repetition: his Week 3 files are mostly our Week 2 material plus a preview of our
Week 4, and his Week 4 Friday is ~80% a repeat of his own Monday.

**Not read:** `Week_05_*`, `Week_06_*`, `Week_07_Notes_Monday`, `Week_08_*` (≈45 p).

**`Ex Sheet Hints/` — deliberately not mined further.** They are annotated copies of the
official sheet; the sheet-8 pass already in `week-08.tex` is where that stops.

## Diego Torres Tejeda — weeks 1–4 partly covered

Mined: the typed `Addendum` (compactness equivalence proof → Wk 2); `16.03` (preservation table
→ Wk 3); `30.03` (tangent vectors as velocities → Wk 7); `06.03` (completeness is not
topological → Wk 2); `02.03` (local-to-global framing → Wk 3); `09.03` (mean value theorem and
its failure for vector-valued `f` → Wk 4).

**Not read:** `23.02` (10 p), `27.02` (16 p), `13.03` (6 p).

⚠️ **Found and deliberately not taken.** `09.03` pp. 6–8 give the counterexample
`xy/√(x²+y²)` — continuous at the origin, all directional derivatives exist, still not
differentiable. Sharper than either example we have. But he uses the one-sided convention
`∂_v f = lim_{s→0⁺}`; under our two-sided definition the quotient is `sgn(s)·v_x·v_y/|v|`, so
the limit does not exist and his claim is false as we state things. Fix the convention or
replace the example — verify before adding.

## Everyone else

Coverage as of 2026-08-06, measured by counting `% Source:` / `% Supplement:` / `% Quelle:`
comments in `content/`:

| Tutor | Citations in `content/` | PDFs | Status |
|---|---|---|---|
| Sascha Brack | 51 | 32 | weeks 1–4 mined, see above |
| Diego Torres Tejeda | 9 | 20 | partly mined, see above |
| Linus Lüchinger | 2 | 24 | barely touched |
| Toby Lane | 1 | 1 | one section used |
| Lukas Krause | 1 | 11 | barely touched |
| Adrien Martelli | 1 | 29 | barely touched |
| **Fabio Guger** | 0 | 19 | **never opened** |
| **Jérôme Paschoud** | 0 | 26 | **never opened** |
| **Tim Fessler** | 0 | 20 | **never opened** |
| **Toprak Erakay** | 0 | 12 | **never opened** |
| **Maarten Cnoops** | 0 | 12 | **never opened** |
| **Lennard Trautmann** | 0 | 14 | **never opened** |
| **Damien Lesieur** | 0 | 2 | **never opened** |
| **Noah Larsson** | 0 | 2 | **never opened** |
| **Riccardo Vanoni** | 0 | 2 | **never opened** |
| Simon Kamps | 0 | 5 | **excluded on purpose** — `SerieNNHints.pdf` are exercise-sheet hints, covered by the standing decision in `gemini.md` not to mine hint files |

### `scratch/` is a map of unfinished work — do not delete it

`scratch/` holds ~470 page renders (`pdftoppm` output) from earlier sessions. They are **not**
leftovers from completed passes. Comparing renders against citations in `content/`:

| Prefix | Pages rendered | Citations in `content/` | Reading |
|---|---|---|---|
| `linus_*` | 228 | 4 | **read but almost entirely unmined** |
| `diego_*` | 106 | 22 | partly mined |
| `lukas_*` | 64 | 10 | partly mined |
| `sascha_*` | 47 | 51 | mined, consistent with the note above |
| `toprak_*` | 10 | 0 | **rendered, nothing mined** |
| `toby_*` | 5 | 1 | the file is 5 pages; roughly done |
| `official_*` | 10 | — | official sheet/solution pages |

Two things follow. First, `linus_0518`, `linus_0521`, `linus_0504`, `linus_0507` and friends
represent a large block of pages that were prepared for reading and then never mined — that is
probably the cheapest content in the repo to pick up, since the extraction is already done.
Second, renders exist for Diego's `23.02`, `27.02` and `13.03`, which the note above lists as
*not read* — so a render is evidence that a file was opened, not that it was mined. Trust the
citation count, not the presence of PNGs.

Regenerating any of these is one `pdftoppm` call, so they are safe to delete if the directory
gets in the way; but while they are there they are the fastest way to see what is half-done.

### Suggested order

1. **Jérôme Paschoud** — `Notizen/` is 24 topic-named German files (`Woche 2.1 Metrische
   Räume`, `Woche 7.1 Satz über implizite Funktionen`, …). `gemini.md` already names him as the
   canonical source for German terminology, and `content/appendix-b-glossary.tex` is built from
   those pairs, so this folder pays for itself twice: German terms plus content. Highest value
   per page in the whole set.
2. **Toprak Erakay** — 12 files, one per week, cleanly named. Easy to route by topic.
3. **Tim Fessler** — 20 files in `Woche N/` subdirectories, weeks 2–14.
4. **Fabio Guger** — 19 files, named by date (`Mo. 02.03.26.pdf`, `Fr 20.03.25.pdf`), so route
   strictly by topic; the dates do not map to our chapters. ⚠️ A previous pass invented the
   path `Fabio Guger/Class Notes/Week_07.pdf` for this tutor. There is no `Class Notes/`
   subdirectory and no week-numbered file. Read the real filenames before citing.
5. **Maarten Cnoops** (12, `Woche N.pdf`), **Lennard Trautmann** (14, date-named).
6. Small folders, likely quick: **Damien Lesieur** (2, incl. `TA_questions_answered.pdf`),
   **Riccardo Vanoni** (2), **Noah Larsson** (2, one is a physics formula sheet — probably skip).
7. Finish the partly-mined ones: Linus Lüchinger's remaining slides, Adrien Martelli, Lukas
   Krause, and Sascha's unread `Week_05`–`Week_08`.

### Check for duplicates before adding anything

A pass in August 2026 added `x^2y/(x^4+y^2)` to `content/10-chain-rule/03-...tex` as a fresh
counterexample. It was already in the document one section earlier, as
`ex:all_directional_derivatives_exist` in `02-directional-derivatives.tex`, with better prose
and correct arithmetic. The duplicate survived a clean build and two reviews before a page
render caught it.

So: before typesetting anything that feels like a standard example, grep `content/` for a
distinctive fragment of it — the formula, not the title. `grep -rn "x^4" content/` would have
taken two seconds and saved the round trip.
