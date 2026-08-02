# File structure & conventions

## Layout

```
ta-notes/
├── main.tex                     the document root (preamble + \input list)
├── CLAUDE.md                    entry point for AI sessions -> points here
├── gemini.md                    historical: style prompt from the LinAlg project
│
├── docs/                        project documentation (this folder)
│   ├── 00-implementation-plan.md
│   ├── 01-file-structure.md     <- you are here
│   ├── 02-source-inventory.md   every tutor, every file, verdict
│   ├── 03-topic-index.md        topic -> owning week (the merge key)
│   ├── 04-style-guide.md        house style for prose, math and LaTeX
│   ├── 05-figure-queue.md       diagrams awaiting TikZ
│   └── 06-open-questions.md     illegible passages, suspected errors
│
├── transcript/                  STAGE 1 output: plaintext, source-annotated
│   ├── week-02.md … week-13.md
│   ├── appendix-a-odes.md
│   └── supplements/
│       ├── toby-lane.md
│       ├── lukas-krause.md
│       ├── damien-lesieur.md
│       ├── toprak-erakay.md
│       └── sascha-brack.md
│
├── content/                     STAGE 2 output: the actual LaTeX
│   ├── week-02.tex … week-13.tex
│   ├── appendix-a-odes.tex
│   └── appendix-b-glossary.tex
│
├── exercise-sheets/             (optional) official Serie01–13 problem statements
│
└── <17 tutor folders>/          SOURCE MATERIAL — never modified
```

## Naming

| Thing | Convention | Example |
|---|---|---|
| Transcript file | `week-NN.md`, zero-padded, week = **file name** of Corsin's PDF | `week-02.md` |
| LaTeX file | same stem, `.tex` | `content/week-02.tex` |
| Figure ID | `FIG-WNN-mm` | `FIG-W05-01` |
| Open question ID | `OQ-NN` (running) | `OQ-07` |
| LaTeX label | descriptive slug, never a number | `\label{thm:heine_borel}` |

⚠️ **Week numbering.** The cover page of `Corsin Nick/Class Notes/Week 2.pdf` reads
*"Class notes Week 1"*, but `Week 3.pdf` and `Week 9.pdf` read *"Week 3"* / *"Week 9"*.
**The file name wins** — it agrees with every other tutor's week/date indexing and with
the exercise-sheet numbers. Never renumber to follow the Week-2 cover.

## Two-stage pipeline

```
PDF  ──read──>  transcript/week-NN.md  ──convert──>  content/week-NN.tex  ──latexmk──>  main.pdf
                (plaintext, page pointers)            (house style applied)
```

The transcript stage exists so that nothing is lost and every claim in the final PDF can be
traced back to a tutor, a file and a page. Never edit `content/*.tex` for a *content*
change — fix the transcript and re-derive.

## Build

```bash
cd "C:/Users/miche/latex/ta-notes" && latexmk -pdf -interaction=nonstopmode main.tex
```

MiKTeX is installed at `C:\Users\miche\AppData\Local\Programs\MiKTeX\miktex\bin\x64`
(`pdflatex`, `lualatex`, `latexmk`). Clean up with `latexmk -c`.

## Source material is read-only

The 17 tutor folders are inputs. Nothing is written into them, nothing is renamed, nothing
is deleted. All output goes to `docs/`, `transcript/` and `content/`.
