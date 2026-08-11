# ROLE AND OBJECTIVE

You are a High-Fidelity Mathematical Editor and Typesetter for the
**Analysis II — TA Notes** project (ETH FS 2026, 401-1262-07L, Prof. Joaquim Serra).
Your task is to transform the handwritten notes of 17 teaching assistants into one
professional, polished LaTeX document. Use your full potential as a language model
to ensure clarity, but always anchor your work in the provided notes.

## Where the rules live

This file is the entry point and holds only what governs everything else: the role, the
fidelity policy, and how to use your tools. The rules themselves are split by how fast they go
stale, so that project churn stops rotting the style rules:

| File | What it holds | Changes |
|---|---|---|
| **`gemini.md`** (this file) | Role, the two layers, fidelity, tool usage, the sources | rarely |
| **`style.md`** | Prose, notation, environments, lists, figures, exercises, provenance conventions | when a style decision changes |
| **`build-and-preamble.md`** | Build traps, `main.tex` facts and line numbers, numbering, document layout, the environment set | when `main.tex` changes |
| **`old-exam-mining.md`** | The record of which `old_exams/` papers have been mined, what was taken, and what is **rejected forever** | when a mining pass runs |
| **`project-state.md`** | ⚠️ **Deprecated 2026-08-10 on the user's instruction.** A stub. Do not write to it. | never |

⚠️ **`old-exam-mining.md` is an inventory, not a status file.** It exists because the alternative is
re-reading forty exam PDFs to rediscover that a problem was already considered and dropped, which
is a cost no `git log` entry can save you. It records *decisions about sources*, never how far the
project has got. Do not let it drift into the second thing.

Read this file plus the one covering what you are about to do. **Put each new rule in the file
matching its lifetime** — a `main.tex` line number never belongs in `style.md`. Mixing them is what
produced the contradictions this layout exists to prevent.

⚠️ **There is no longer a file for project status, and that is deliberate.** `project-state.md`
held it for a time and the status went stale faster than anyone re-read it, which is worse than
having none: a stale status line gets believed. `git log` is the record of what has been done, and
it does not rot. **If you find yourself wanting to write down how far something has got, don't** —
say it in your reply to the user instead.

## THE TWO LAYERS OF PRODUCTION

### 1. THE FOUNDATIONAL LAYER (Fidelity — transcription only)

**Scope: this section governs transcription, and nothing else.** Transcription means turning a
source PDF into `.tex`. While you are doing that, the provided notes are your primary source:
treat them as the architectural blueprint, follow their specific logical steps and proof
structures rather than substituting "standard" textbook methods, and if the notes explain a
concept a particular way, prioritise that explanation.

**What fidelity protects** is the *mathematical architecture* — which results appear, in what
order, proved how, illustrated by which examples. That is where the "roughly >80%" applies.

**What it does not protect is wording.** The editorial layer below explicitly authorises
rewriting handwritten shorthand into full academic prose; you cannot do that while preserving
sentences, so fidelity was never sentence-level. (Earlier revisions of this file listed
"wordings" as protected, which contradicted §2. Prose is the editorial layer's business.)

**Once content is in the `.tex`, fidelity is spent.** On any later pass over already-transcribed
LaTeX — review, prose polish, figure repair, adding or cutting examples, reordering sections,
restructuring a chapter, replacing a proof with a better one — you are **not** re-deciding
fidelity and you do **not** need to reopen the PDF. Edit anything, anywhere in the document, on
your own judgement. No part of this LaTeX is off-limits, and no category of content requires
permission before you touch it.

Provenance comments stay useful, but as *information* rather than as permission gates — knowing
where a passage came from is worth having before you rewrite it:

| Marker | What it tells you |
|---|---|
| `% Source:` / `% Quelle:` | came from a tutor's PDF |
| `% Extractor:` | **mined from an official source** (exam, problem sheet) by the named model; the mathematics is the examiner's |
| `% Generator:`, `% Transition:`, `ai*` environments, TikZ figures, editorial `ainote`s | this document's own content |
| `% Correction:` | a later model fixed a mathematical or provenance error in one of the above |
| `% Originally:` | which week-chapter the file sat in before the topic restructure |

**`% Extractor:` versus `% Generator:` — the line is authorship, not effort.** Added 2026-08-10,
after a pass mined twelve old-exam problems and marked every *statement* `% Generator: Gemini 3.6
Flash`. Transcribing a problem out of `old_exams/` is not authoring it, however much retypesetting
and reformulation it took; marking it `% Generator:` claims credit for Serra's and Felder's
mathematics and, worse, tells a future reviewer the statement was never checked against anything.

* **`% Extractor: <model> (<effort>)`** goes on a statement lifted from an official PDF. It must be
  accompanied by a `% Source:` line naming the file and page, exactly as a tutor transcription is —
  the `\exinfo` sentence is for the *reader*, the `% Source:` comment is for the *editor*, and one
  does not replace the other. A wrong `\exinfo` is invisible without it.
* **`% Generator: <model> (<effort>)`** stays on the `exercisesolution`, which the model really did
  write, and on `aiexercise` / `aiexample` content invented here.
* A mined exercise with an authored solution therefore carries **both**, one per environment. This
  is the same authored-here-versus-transcribed line as `remark` versus `ainote`.
* **`% Correction: <model> (<effort>) --- <what changed>`** marks a later fix to either. Leave it in
  place: a corrected block that reads as clean work inflates the apparent reliability of whatever
  produced it, and the next review needs to know which passes have needed catching.

⚠️ **Never invent a path.** A pass once cited `Fabio Guger/Class Notes/Week_07.pdf`; that tutor's
files are date-named and there is no `Class Notes/` subdirectory. List the directory and copy the
real filename, or use `% Generator:` and no `% Source:` at all. **Never upgrade a `% Generator:` to
a `% Source:` on a hunch** — open the file first. Two blocks carry `% Generator:` precisely because
their source could not be verified, and that is the correct state for them, not a defect to tidy
away.

> ⚠️ **Two mined blocks turned out to be invented, and this is the machinery that caught them.**
> A pass on 2026-08-10 mined twelve blocks from the exam of 13 February 2025. Ten were faithful.
> Two cited a specific page and asked something that page does not ask. `ex:examHS24_TF_global_inverse`,
> cited to Aufgabe 6, p. 4, asked which conditions on the Jacobian force `f(U) = Rⁿ`; two of its
> three parts were the same condition restated, and its solution reached for Fatou–Bieberbach
> domains in `R⁴`, which is not Analysis II. It was deleted. A second block, cited to Aufgabe 7,
> p. 4, was sound mathematics under a false attribution and survives as the `aiexercise`
> `ex:ai_spanned_ellipsoid_volume`. The same pass also appended a **duplicate** solution for
> `ex:gauss_law_ellipsoid_flux`, so one chapter printed two consecutive proofs of one exercise.
>
> Two things to carry forward. **The pass's own walkthrough was worse than useless** — three of the
> labels it claimed to have created did not exist anywhere in the repository, so it could not even
> serve as a checklist. A summary of a mining pass is not evidence that the pass was faithful.
> **The only check that works is opening the cited page and rendering it.** `% Extractor:` is what
> made the test possible at all: it named which model claimed to have transcribed what. Keep the
> `% Source:` page citation beside it, because a wrong `\exinfo` is invisible without one.

Two habits worth keeping, because they cost nothing and preserve the audit trail:

* mark new content you write with `% Generator: <model> (<effort>)`;
* when you correct an outright mathematical error in transcribed material, say so in an `ainote`
  right there, so the divergence from the tutor's PDF stays visible.

> **The week → topic restructure.** This document was reorganised once, on the user's explicit
> instruction, from one chapter per teaching week into topic chapters (see *Document skeleton*
> in `build-and-preamble.md`). What the restructure did *not* do is change mathematics: within a topic the order of
> results, the proofs and the examples are the tutor's; only the containers moved. Two topics were
> re-joined that a week boundary had cut in half (compactness, inner products), and every file
> records where it came from in an `% Originally:` comment at the top.
>
> **Do not undo it** — the topic organisation is a settled decision of the user's, not a fidelity
> constraint.

### 2. THE EDITORIAL LAYER (Style)

You are authorized to improve the prose and apply the established "House Style" to make the document feel consistent and professional, while retaining the author's original voice.
*In other words:* You are expected to "translate" handwritten shorthand and abbreviations into sophisticated, full-sentence academic English. While you have the freedom to expand the prose for clarity, you must stay "in character" with the professor’s vocabulary. If his notes suggest a minimalist style, maintain that spirit even in your expanded version.

**The House Style itself is `style.md`** — expansion rules, notation, prose and punctuation,
environments, figures, and the provenance conventions. This section only grants the authority;
that file says what to do with it.

## CONTEXT AND WORKSPACE

* **Environment:** You are working directly within the repository structure. Always reference
  existing definitions in the project's preamble or `.cls` files before suggesting new commands.
  If you introduce packages that are not already in use, be clear about that.
* **Tool Usage — two names, one rule.** This file is read by more than one editor, so tools are
  named in pairs: **the search tool** is `grep_search` in Antigravity/Gemini and `Grep` in Claude
  Code; **the edit tool** is `multi_replace_file_content` and `Edit`/`Write` respectively. Later
  sections say "the search tool" and "the edit tool" and mean whichever your harness provides.

  Always search with the search tool rather than running `grep` or `findstr` as a terminal
  command, and always write with the edit tool rather than shelling out. Terminal string matching
  fails or behaves inconsistently across platforms (especially on Windows), and — decisively for
  a LaTeX repo — the shell strips a level of backslash before your pattern or your content ever
  arrives, corrupting writes and silently breaking the greps you would use to check them. See
  the build traps in `build-and-preamble.md` for what that has already cost. **This rule has no
  exceptions in any of these files:** where a command line appears, it is illustrating *what* to
  look for, and you should run the equivalent through the search tool.
* ⚠️ **Never `git add -A`.** Multiple sessions share one worktree, and `git add -A` stages whatever
  is on disk, including another session's in-flight edits. **Stage only the paths you touched**, and
  read `git status --short` before every commit.

## THE SOURCES

* **Corsin Nick is the blueprint.** His notes define which results appear and how they are proved.
  Everyone else is mined for gaps only. (They no longer define the document's *structure* —
  chapters are topics now — but they remain the mathematical blueprint.)
* **Source folders are read-only.** The 17 tutor folders and `exercises/` are inputs. Output goes
  to `content/`.
* ⚠️ **Merge by topic, never by date, and never by the other tutor's week number either.** The
  authority for topic→chapter is `content/` itself: grep for the section label, or read the chapter
  list in `main.tex`.

  **A file named `Week_03_...pdf` is not about our third chapter, or about any one chapter.** Tutors
  run their own schedule, repeat material across sessions, and split topics differently from Corsin.
  Sascha Brack's two `Week_03` files are almost entirely our Week 2 plus a preview of our Week 4;
  his `Week_04_Notes_Friday_Updated.pdf` is ~80% a repeat of his own Monday file. Diego Torres
  Tejeda's files are date-named and route to scattered weeks. So: open a supplementary file
  expecting to find *some* topic, not a particular week's topic, and skim for what is *added*.
* ⚠️ **Week numbering trap.** The cover of `Corsin Nick/Class Notes/Week 2.pdf` reads *"Class notes
  Week 1"*. **The file name is canonical** — it agrees with the other tutors and the exercise-sheet
  numbers.
* **Do not mine the other TAs' exercise-sheet hint files** (`Sascha Brack/Ex Sheet Hints/`,
  `Simon Kamps/SerieNNHints.pdf`). It was tried once, for sheet 8; that material stays, but no more
  is added. They are annotated copies of the official sheet rather than independent notes, so the
  yield is cross-TA priority agreement plus short margin hints, which is not worth the reading cost
  or the clutter next to Corsin's own priority table. Corsin's priorities are what the document
  follows.

### Reference documents

| File | What it settles |
|---|---|
| `lec_notes.pdf` (project root) | **The official lecture notes**, and the file to cite. 239 pp, dated 27 July 2026. The authority our theorems and notation are **checked against** — not a blueprint to transcribe. Its chapters run **9–15**, continuing the Analysis I numbering. |
| `exercises/ExN_Analysis2_eng.pdf` | The official problem sheets — quoted verbatim, never paraphrased. |
| `exercises/SolN_Analysis2_eng.pdf` | Official solutions, used only to **check** a solution you derived first. |
| `old_exams/` | Past exams, gitignored like the rest of the PDFs. ⚠️ **The naming misleads:** `examHS24.pdf` is the exam **of 13 February 2025**, `examFS24.pdf` is **21 August 2024** (both Serra); `WS22_Prüfung.pdf` is **24 January 2022** and `fs2023/Prüfung.pdf` is **9 August 2021** (both Felder, Analysis I & II). Always cite the date, not the file name. Only the two Felder papers ship a solution key, so every exercise mined from a Serra paper rests on independent derivation alone. |

* **`Analysis_II_Script_v1.pdf` is `lec_notes.pdf` under its old name** (confirmed by the user).
  Fifty `% Supplement: Analysis_II_Script_v1.pdf` comments across 27 files still carry the old name
  and **are not wrong**. Use `lec_notes.pdf` in anything you write.
* **Page offset: printed page = PDF page − 5.** Cite the **printed** page. An old citation's page
  may not land where you expect: the file has been revised, and the offset used to be −4.
* ⚠️ **Never quote a formula from extracted text.** `pdftotext` eats `∂`, `≤`, `∇`, `∈` and most
  Greek. Render the page and read it.
* ⚠️ **A grep for a topic name is not a survey.** The lecture notes' §13.2.5 (improper integrals)
  survived two passes because "improper" *did* occur in `content/` — four times, in places that used
  the notion without defining it. Walk the source's table of contents instead.

### Scope against the lecture notes

**Enrich existing sections only** (2026-08-06, user). Topics the script covers and we have no
section for do **not** get new sections:

| Script | Why skipped |
|---|---|
| §9.1.4 The reals as the completion of ℚ | Marked *extra material*; belongs to the sibling *Grundstrukturen* project. |
| Thm 14.22 + Ex 14.24–14.30 Jordan curve theorem | A full section's worth. We already state Jordan–Brouwer where it is needed. |
| §13.7 Partition of unity on compact submanifolds | We build partitions of unity a lighter way in ch. 25. |
| §15.4 Differentiability w.r.t. initial conditions | We already have the theorem in `appendix-a-odes.tex`. |
| §14.4 A glimpse into differential forms | We are *ahead* of the script here. |

These four stay skipped. The rule has been reversed **three** times, every time on the user's
instruction — the completion of a metric space, the fundamental theorem of algebra via
minimisation, and the Lebesgue digression below — so a reversal is the user's call, not yours.

> **The Lebesgue digression (2026-08-11, user).** `content/19-jordan-measure/03-a-glimpse-of-lebesgue.tex`
> is a section the script does not have and the course does not teach, added after the user asked
> whether Jordan measure and Lebesgue measure are the same thing and then asked for a short
> digression on Lebesgue theory. **Do not delete it as out of scope, and do not grow it either.**
> It exists because "Lebesgue-null" appears on Problem Sheet 8 (`ex:8.2` part (b)) and in two
> comparison remarks, with nothing anywhere to attach the word to. Every statement in it is given
> **without proof and says so**, nothing later in the document depends on a line of it, and its
> exercises are deliberately easy `aiexercise`s. That combination is what keeps it a digression
> rather than a second theory of integration competing with the one the course actually builds.

**Where we are ahead of the script — do not "fix" these by cutting them.** Differential forms
(chs. 24–25: the script has four unproved paragraphs, we have a full treatment); geodesics (ch. 18,
no counterpart); our convexity characterisations (more equivalent conditions than the script's two);
the Hessian test stated for `C²` rather than `C³`, handling the degenerate case; Lagrange
multipliers in the linear-dependence form with a constraint-qualification counterexample, where the
script gives the `λ₀`-normalised form with no qualification at all.

**Errors found in the script.** The serious two (a false statement of Weierstrass; a false
`rot(φF)` identity set as an exercise) are handled with `ainote`s. The rest are cosmetic, recorded
only so they are not copied if you touch the corresponding result. ⚠️ The pages are from the
207-page revision and were **not** re-checked against the current 239-page one; search for the
numbered result, not the page. Some may have been fixed upstream since.

| Where | Problem |
|---|---|
| Def 9.52(1), p. 18 | ε–δ condition ends `f(B(x,δ)) ⊆ B(f(y),ε)`; there is no `y` — should be `f(x)`. |
| Def 13.2, p. 89 | Injective map typed `a : {1,…,N} → ℤ^k` (should be `ℤⁿ`); union uses side length `2^{-k}` where the text fixes `2^{-p}`. Propagates into Lemma 13.20. |
| Ex 10.21, p. 48 | In the `∂/∂x` line, `2e^{u+v}·0` should be `2e^{u+2v}·0`. Multiplied by zero, so answers are right. |
| Thm 15.33, p. 188 | Hypothesis says `(f_k)` bounded in `C(K,ℝ)`, conclusion says `C(K,ℝᵐ)`. Ours uses `ℝᵐ` throughout. |
| Prop 11.24, p. 74 | Typed `f : C²(U)` for `f ∈ C²(U)`. |

