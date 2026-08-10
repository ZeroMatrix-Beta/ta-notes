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
| **`gemini.md`** (this file) | Role, the two layers, fidelity, tool usage | rarely |
| **`style.md`** | Prose, notation, environments, lists, figures, provenance conventions | when a style decision changes |
| **`build-and-preamble.md`** | Build traps, `main.tex` facts and line numbers, numbering, the environment set | when `main.tex` changes |
| **`project-state.md`** | Blueprint tutor, what is done, document skeleton, standing decisions | often |

Read this file plus the one covering what you are about to do. **Put each new rule in the file
matching its lifetime** — a `main.tex` line number never belongs in `style.md`, and project
status never belongs anywhere but `project-state.md`. Mixing the three is what produced the
contradictions this layout exists to prevent.

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

Two habits worth keeping, because they cost nothing and preserve the audit trail:

* mark new content you write with `% Generator: <model> (<effort>)`;
* when you correct an outright mathematical error in transcribed material, say so in an `ainote`
  right there, so the divergence from the tutor's PDF stays visible.

> **The week → topic restructure.** This document was reorganised once, on the user's explicit
> instruction, from one chapter per teaching week into topic chapters (see *Document skeleton*
> in `project-state.md`). What the restructure did *not* do is change mathematics: within a topic the order of
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

