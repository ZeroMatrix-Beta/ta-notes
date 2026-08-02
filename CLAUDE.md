# Analysis II — TA notes → typeset document

Turning the exercise-class notes of 17 ETH teaching assistants into one polished LaTeX
document. Course: **401-1262-07L, Analysis II: Several Variables**, Prof. Joaquim Serra,
FS 2026.

## Read these first

| File | What it settles |
|---|---|
| `docs/00-implementation-plan.md` | The whole plan, the phases, and every decision taken |
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
