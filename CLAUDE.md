# Analysis II — TA notes → typeset document

Turning the exercise-class notes of 17 ETH teaching assistants into one polished LaTeX
document. Course: **401-1262-07L, Analysis II: Several Variables**, Prof. Joaquim Serra,
FS 2026.

## ⚠️ THE PRIORITY — read before anything else

**Get *Corsin Nick* all the way to a compiling PDF. Do not touch the other 16 tutors until
that exists.**

The user's instruction from the outset: *"If everything from Corsin Nick is transcribed nicely
and you just have a look at the others, that's fine for me."* Corsin alone is the deliverable;
supplements are a bonus, and they are **last**.

Do **not** follow the phase numbers in `docs/00-implementation-plan.md` — that document numbers
supplement-mining as Phase 3, ahead of the LaTeX build. That ordering is superseded. Correct
order:

| # | Step | Reads PDFs? | Status |
|---|---|---|---|
| 1 | Scaffolding (`docs/`, `transcript/`) | no | ✅ **done** |
| 2 | Transcribe Corsin — weeks 2–13 + ODE appendix | **yes, heavily** | 🔶 weeks 2–11 done; **12, 13, ODEs remain** |
| 3 | Retarget `main.tex`, convert `transcript/*.md` → `content/*.tex` | no | ⬜ not started |
| 4 | Build: `latexmk` until it compiles clean → **a real PDF exists here** | no | ⬜ not started |
| 5 | TikZ figures (`05-figure-queue.md`) | Group B only | ⬜ not started |
| 6 | *Optional:* supplements from other tutors | yes | ⬜ **do not start before step 4** |

Steps 3–5 improve a document that already builds. Step 6 is the only one that opens another
tutor's folder, and the project is a legitimate deliverable without it.

## Where the work stands

Corsin Nick's weeks **2–11 are fully transcribed** (~3,970 lines); weeks **12, 13 and the ODE
appendix remain** (~29 pp).

To resume: `transcript/week-12.md` is the next file. Read
`Corsin Nick/Class Notes/Week 12.pdf` (7 pp) and `exercises/Ex12_Analysis2_eng.pdf`, then follow
the format of any finished week (`week-11.md` is the richest example).

⚠️ **`main.tex` does not compile yet** — it still carries the Linear Algebra title block and
`\input`s 32 files that do not exist. That is step 3, untouched by design.

### Do steps 2 and 3 as separate sessions — they have opposite cost profiles

1. **Finish transcription** — weeks 12, 13, `Analysis 1 lesson on ODEs.pdf` (~29 pp).
   Reads PDF page images, so it is context-hungry. Stay in Markdown for these three: switching
   to direct-LaTeX for the last 23% would buy little and cost consistency.
2. **LaTeX conversion + `main.tex` retarget** — **opens no PDFs at all.** Pure text→text over
   `transcript/`, so it is cheap and can run in a session that never touches the source folders.

*Retrospective, for whoever plans the next project like this:* the Markdown→LaTeX two-stage
pipeline was a judgement call that cost a second pass over every week. Writing `content/*.tex`
directly, with `% Corsin Week 5, p. 4` comments carrying the provenance, would have achieved the
same traceability in one pass. The transcripts' math is already LaTeX, so stage 2 is mostly
wrapping prose in environments. Not worth reversing now — 10 of 13 weeks are already through
stage 1.

## Read these first

| File | What it settles |
|---|---|
| `docs/00-implementation-plan.md` | The whole plan and every decision taken. ⚠️ **Its phase *numbering* is superseded** by the priority table above — supplements are last, not third |
| `docs/01-file-structure.md` | Layout, naming, the two-stage pipeline, build command |
| `docs/02-source-inventory.md` | Every tutor and file: what is transcribed, what is skipped, why |
| `docs/03-topic-index.md` | Topic → owning week. **The merge key** — read before adding any supplement |
| `docs/04-style-guide.md` | House style for prose, math, LaTeX. Follow it exactly |
| `docs/05-figure-queue.md` | Diagrams awaiting TikZ |
| `docs/06-open-questions.md` | Illegible passages, suspected errors, unresolved calls |

`gemini.md` is the *previous* project's style prompt, kept for reference only.
`docs/04-style-guide.md` supersedes it.

## The five things that matter

1. **Corsin Nick is the blueprint.** `Corsin Nick/Class Notes/Week 2–13.pdf` is transcribed
   in full and defines the document's structure (one chapter per week, Monday/Friday
   sessions). Everyone else is mined for gaps only.
2. **Merge by topic, never by date.** Tutors do not teach the same material in the same
   week. `docs/03-topic-index.md` is the only valid mapping.
3. **Transcript before LaTeX.** `transcript/week-NN.md` first, with a page pointer on every
   block; `content/week-NN.tex` derived from it. Content fixes go in the transcript.
4. **Never silently correct a source.** Flag it inline and log it in `06-open-questions.md`.
5. **Source folders are read-only.** The 17 tutor folders and `exercises/` are inputs.
   Output goes to `docs/`, `transcript/`, `content/`.

## Week numbering trap

The cover of `Corsin Nick/Class Notes/Week 2.pdf` reads *"Class notes Week 1"*, but
`Week 3.pdf` and `Week 9.pdf` read *"Week 3"* / *"Week 9"*. **The file name is canonical** —
it agrees with the other tutors and with the exercise-sheet numbers.

## Build

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

MiKTeX at `C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`.
Do not touch the theorem / `aliascnt` / `cleveref` block in `main.tex:334–463` — its
comments document real bugs already solved there.
