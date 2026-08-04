# File structure & conventions

## Layout

```
ta-notes/
├── main.tex                     the document root (preamble + \input list)
├── CLAUDE.md                    entry point for AI sessions -> points to gemini.md
├── gemini.md                    authoritative source of truth for guidelines & style
│
├── docs/                        project documentation (this folder)
│   ├── 00-implementation-plan.md
│   ├── 01-file-structure.md     <- you are here
│   ├── 02-source-inventory.md   every tutor, every file, verdict
│   ├── 03-topic-index.md        topic -> owning week (the merge key)
│   ├── 04-style-guide.md        redirect to gemini.md
│   ├── 05-figure-queue.md       diagrams awaiting TikZ
│   ├── 06-open-questions.md     illegible passages, suspected errors
│   ├── 07-todo.md               next-session handover
│   ├── 07-tutor-review.md       skim of the 16 non-Corsin tutors
│   └── 08-latex-review.md       maths/figure/prose review of Weeks 1–7
│
├── content/                     the actual LaTeX files
│   ├── week-01.tex … week-08.tex        (09–13 not yet written)
│   ├── exercise-sheets/                 full sheets: week-02 … week-05 only
│   ├── appendix-a-odes.tex              PLANNED — does not exist yet
│   └── appendix-b-glossary.tex          PLANNED — does not exist yet
│
├── exercises/                   official ExN_/SolN_Analysis2_eng.pdf sheets
│
└── <17 tutor folders>/          SOURCE MATERIAL — never modified
```

⚠️ Two paths above are easy to get wrong. The transcribed problem sheets live in
`content/exercise-sheets/`, **not** at the top level; the top-level `exercises/` folder holds
the official PDFs and is read-only. And there is **no `transcript/` directory** — the two-stage
transcript pipeline was dropped in favour of the direct workflow below.

## Naming

| Thing | Convention | Example |
|---|---|---|
| LaTeX file | `week-NN.tex`, zero-padded, week = **file name** of Corsin's PDF | `content/week-02.tex` |
| Figure ID | `FIG-WNN-mm` | `FIG-W05-01` |
| Open question ID | `OQ-NN` (running) | `OQ-07` |
| LaTeX label | descriptive slug, never a number | `\label{thm:heine_borel}` |

⚠️ **Week numbering.** The cover page of `Corsin Nick/Class Notes/Week 2.pdf` reads
*"Class notes Week 1"*, but `Week 3.pdf` and `Week 9.pdf` read *"Week 3"* / *"Week 9"*.
**The file name wins** — it agrees with every other tutor's week/date indexing and with
the exercise-sheet numbers. Never renumber to follow the Week-2 cover.

## Direct LaTeX Workflow

```
PDF  ──read & typeset──>  content/week-NN.tex  ──latexmk──>  main.pdf
                           (fine provenance % comments, house style)
```

Content is typeset directly into `content/*.tex` with section-level source provenance comments (e.g. `% Source: Corsin Nick/Class Notes/Week 5.pdf, pp. 1--3`).

## Build

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

MiKTeX is installed at `C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`
(`pdflatex`, `lualatex`, `latexmk`). Clean up with `latexmk -c`.

## Source material is read-only

The 17 tutor folders are inputs. Nothing is written into them, nothing is renamed, nothing
is deleted. All output goes to `docs/` and `content/`.
