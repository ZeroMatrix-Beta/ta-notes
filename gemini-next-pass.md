# Prompt for Gemini's next pass — mining only

Paste the block below. Written 2026-08-06, after a prose-editing pass had to be reverted
wholesale (see the note at the end of this file, and `scratch/gemini-pass-2026-08-06.patch`).

---

```
You are working on the Analysis II TA-notes repo at C:\Users\miche\latex\ta-notes.
Read gemini.md in full first; it is authoritative and it has changed since your last pass.

SCOPE — THIS PASS IS MINING ONLY.

Your job is to read tutor PDFs that have never been read and typeset what is NEW into the
right chapter under content/. That is the whole job.

Do NOT, under any circumstances:
  - rewrite, expand, reword, or "improve" any prose that is already in content/. Not one
    sentence. If existing text looks clumsy to you, leave it and note it in an ainote.
  - run any search-and-replace, regex, or scripted edit across files. Edit occurrences one at
    a time, reading each sentence. A previous pass ran a Python re.sub over every .tex file
    and had to be reverted wholesale (scratch/gemini-pass-2026-08-06.patch).
  - touch LaTeX comments (% ...) or TikZ node text for style reasons. They are out of scope.
  - paraphrase text quoted from an official problem sheet. It is verbatim, always.
  - delete a % Generator: comment, or any tracked file.

BEFORE YOU TYPESET ANY EXAMPLE, GREP FOR IT

Search content/ for a distinctive fragment of the formula, not the title. The last pass added
x^2y/(x^4+y^2) as a new counterexample when it was already in the document one section earlier,
with correct arithmetic and better prose. "grep -rn 'x^4' content/" would have caught it.

WHERE TO START

supplements.md holds a coverage table and a suggested order. Start with Jérôme Paschoud's
Notizen/ folder (24 topic-named German files, never opened). He is the canonical source for
German terminology per gemini.md, so mine content AND collect \germanterm pairs into
content/appendix-b-glossary.tex as you go. Then Toprak Erakay (12 files), then Tim Fessler (20).

Do not mine Simon Kamps — SerieNNHints.pdf are exercise-sheet hints, excluded by standing
decision in gemini.md.

PROVENANCE — VERIFY, DO NOT GUESS

Before writing any % Source: or % Supplement: comment, list the directory and copy the real
filename. A previous pass invented "Fabio Guger/Class Notes/Week_07.pdf"; that tutor's files
are date-named and there is no Class Notes/ subdirectory. If you cannot cite a real path and
page, use % Generator: Gemini <version> (<effort>) and no % Source: at all.

Re-cite the source below every block you insert — a provenance comment claims everything under
it until the next one. This is the rule broken most often.

BEFORE YOU REPORT DONE

  latexmk -pdf -interaction=nonstopmode -jobname=check main.tex
must exit 0 with zero errors and zero undefined references. Check the log, not your impression
of the log. Then run the malformed-closer grep from gemini.md.

ONE SPECIFIC TASK CARRIED OVER

Several blocks added in commit 567632b are marked % Generator: because their source could not
be verified. If while mining you find the actual source, upgrade the comment to a real
% Source: with page number. Candidates:
  - the Lagrange sensitivity remark in content/13-lagrange/01-lagrange-multipliers.tex
    (possibly Toby Lane, class-document.pdf)
  - the graph arc-length proposition and astroid example in
    content/21-gram-determinant/03-length-of-a-curve.tex
    (possibly Linus Lüchinger, Slides-04-30.pdf, p. 3)
Verify by opening the file. Do not upgrade on a hunch.
```

---

## Why this pass is scoped to mining

The August 2026 pass split cleanly: everything it got right was *adding* mathematics,
everything it got wrong was *editing existing text*. Scoping to mining removes the failure
surface and points at the real remaining work — nine of sixteen tutors have never been opened.

What went wrong, for the record:

| Failure | Example |
|---|---|
| Scripted regex over every `.tex` | broke a math span across a line break, `\tfrac` in text mode, build dead |
| Prose inflation in transcribed sections | Young's inequality proof 6 lines → 40 |
| Problem-sheet text paraphrased | exercise 1.1 gained clauses not on the sheet |
| Fabricated provenance | `Fabio Guger/Class Notes/Week_07.pdf` does not exist |
| Mandatory comments deleted | four `% Generator:` lines dropped |
| Tracked file deleted | `supplements.md` removed outright |
| Wrong mathematics in new content | claimed all directional derivatives of `x^2y/(x^4+y^2)` are 0 |
| Duplicated content already in the document | that same example was already `ex:all_directional_derivatives_exist`, one section earlier, correct |

What went right, and was kept (commit `567632b`): eight new results — Euler's homogeneous
function theorem, the spectral theorem via Rayleigh-quotient Lagrange, Courant–Fischer,
multiplier sensitivity, a convex function with unattained infimum, the complex exponential,
gradient-normal-to-level-sets, Peano existence, graph arc length — plus four genuine gaps
filled in existing proofs.
