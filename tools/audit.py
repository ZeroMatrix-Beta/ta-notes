#!/usr/bin/env python3
"""
Structural audit of the Analysis II TA notes.

    python tools/audit.py            # run every check
    python tools/audit.py --quiet    # findings only, no informational sections

Exits non-zero if any check finds something, so it can gate a commit.

WHAT THIS IS FOR
----------------
Every check here mechanises a rule that `gemini.md`, `style.md` or
`build-and-preamble.md` states in prose and that nothing else enforces. It opens
no source PDF: each check compares the repository against itself, which is what
makes it cheap enough to run on every commit. Verifying an `\\exinfo` against the
paper it cites is a separate, expensive job and is deliberately out of scope --
but note that a citation can be *internally* wrong (disagreeing with the
`% Source:` comment beside it, or with `% Originally:`), and those cases are
caught here for free.

WHY IT EXISTS
-------------
Three of the defects it checks for were live in the tree on 2026-08-23 and none
had been noticed: a tikz picture referencing a colour the document never defines
(pgfkeys ignores an unknown key and builds on, so the PDF looked fine), sixty
numeric `ex:N.M` labels the rule files had banned, and six exercise titles naming
only the question format. A rule that is written down but not checked is a rule
that drifts. See also the note in `gemini.md`: a summary of a pass is not
evidence the pass happened -- so every claim this script makes is one you can
re-derive by running it.
"""
import re, sys, json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
MAIN = ROOT / "main.tex"
QUIET = "--quiet" in sys.argv

FILES = sorted(CONTENT.rglob("*.tex"))
TEXT = {f: f.read_text(encoding="utf-8", errors="replace") for f in FILES}
def rel(f): return str(f.relative_to(CONTENT)).replace("\\", "/")

# Scan typeset content, not commentary. A `% Correction:` note that quotes the
# label it removed must not read as a live \label -- which is exactly what this
# script did to its own first finding.
COMMENT = re.compile(r"(?<!\\)%.*$")
def code(line): return COMMENT.sub("", line)

findings = []
def report(title, rows, cap=25, informational=False):
    if informational and QUIET:
        return
    if not informational:
        findings.extend(rows)
    flag = "  (informational)" if informational else ""
    print(f"\n=== {title}: {len(rows)}{flag} ===")
    for r in rows[:cap]:
        print("  " + r)
    if len(rows) > cap:
        print(f"  ... and {len(rows) - cap} more")

# ----------------------------------------------------------------- gather ---
ENV_LIKE = ("exercise", "aiexercise", "example", "aiexample")
TITLED = ENV_LIKE + ("theorem", "proposition", "lemma", "corollary", "definition")

labels = collections.defaultdict(list)
refs = collections.defaultdict(list)
exsol = collections.defaultdict(list)

for f in FILES:
    for i, raw in enumerate(TEXT[f].split("\n"), 1):
        line = code(raw)
        for m in re.finditer(r"\\label\{([^}]*)\}", line):
            labels[m.group(1)].append(f"{rel(f)}:{i}")
        for m in re.finditer(r"\\[cC]?ref\{([^}]*)\}|\\cpageref\{([^}]*)\}"
                             r"|\\hyperref\[([^\]]*)\]", line):
            for name in (m.group(1) or m.group(2) or m.group(3)).split(","):
                refs[name.strip()].append(f"{rel(f)}:{i}")
        for m in re.finditer(r"\\exsol(?:\[[^\]]*\])?\{([^}]*)\}", line):
            exsol[m.group(1)].append(f"{rel(f)}:{i}")

BLOCK = re.compile(r"\\begin\{(" + "|".join(ENV_LIKE) + r")\}(\[(?P<title>.*?)\])?"
                   r"\s*\n(?P<body>.*?)\\end\{\1\}", re.S)
blocks = []
for f in FILES:
    lines = TEXT[f].split("\n")
    for m in BLOCK.finditer(TEXT[f]):
        start = TEXT[f][:m.start()].count("\n")
        above, i = [], start - 1
        while i >= 0 and (lines[i].startswith("%") or not lines[i].strip()):
            if lines[i].startswith("%"):
                above.append(lines[i])
            i -= 1
        body = m.group("body")
        exinfo = None
        k = body.find("\\exinfo{")
        if k != -1:
            depth = 0
            for j in range(k + len("\\exinfo"), len(body)):
                if body[j] == "{": depth += 1
                elif body[j] == "}":
                    depth -= 1
                    if depth == 0: break
            exinfo = " ".join(body[k + len("\\exinfo") + 1:j].split())
        blocks.append(dict(file=rel(f), line=start + 1, env=m.group(1),
                           title=m.group("title"), exinfo=exinfo,
                           comments=list(reversed(above)), body=body))

print(f"files {len(FILES)} | labels {len(labels)} | blocks {len(blocks)} "
      f"| \\exsol {sum(len(v) for v in exsol.values())}")

# ------------------------------------------------------- A. label integrity --
report("duplicate \\label",
       [f"{k}  at  {', '.join(v)}" for k, v in sorted(labels.items()) if len(v) > 1])

report("reference to a label that does not exist",
       [f"{k}  from  {', '.join(v[:3])}" for k, v in sorted(refs.items())
        if k not in labels])

report("\\exsol pointing at a label that does not exist",
       [f"{k}  from  {', '.join(v)}" for k, v in sorted(exsol.items())
        if k not in labels])

# The rule is descriptive slugs, never the source's numbering (gemini.md). Match a
# N.M anywhere in the slug: the 2026-08-23 sweep matched only digits straight after
# the colon and left `ex:solution_9.1` and `note:9.1_...` behind.
report("label carrying a source number instead of a descriptive slug",
       [f"{k}  ({v[0]})" for k, v in sorted(labels.items())
        if re.search(r"\d+\.\d+", k)])

report("sol: anchor with nothing pointing at it",
       [f"{k}  ({v[0]})" for k, v in sorted(labels.items())
        if k.startswith("sol:") and k not in exsol and k not in refs])

PREFIX_OK = {
    "thm": {"theorem"}, "prop": {"proposition"}, "lem": {"lemma"},
    "cor": {"corollary"}, "def": {"definition", "notation"},
    "ex": set(ENV_LIKE), "sol": {"exercisesolution", "proof"},
    "rem": {"remark", "importantremark", "aside"},
    "ainote": {"ainote"}, "note": {"ainote", "remark", "aside"},
    "not": {"notation"}, "q": {"question", "quiz"},
}
SKIP_ENV = {"center", "enumerate", "itemize", "align", "equation", "figure", "table"}
mismatch = []
for f in FILES:
    cur = None
    for i, raw in enumerate(TEXT[f].split("\n"), 1):
        line = code(raw)
        m = re.search(r"\\begin\{([a-zA-Z]+)\}", line)
        if m: cur = m.group(1)
        lm = re.search(r"\\label\{([a-z]+):([^}]*)\}", line)
        if lm and cur and lm.group(1) in PREFIX_OK:
            if cur not in PREFIX_OK[lm.group(1)] and cur not in SKIP_ENV:
                mismatch.append(f"{rel(f)}:{i}  \\label{{{lm.group(1)}:...}} on a "
                                f"`{cur}`  ({lm.group(2)[:40]})")
report("label prefix does not match the environment it labels", mismatch)

# ------------------------------------------------ B. provenance, internal ----
P_SHEET = re.compile(r"Problem\s+(\d+)\.(\d+)\s+of\s+Problem\s+Sheet\s+(\d+)")
P_ORIG = re.compile(r"\\exercisesheet\{(\d+)\}\s*,\s*problem\s+(\d+)\.(\d+)")
P_SRC = re.compile(r"exercises/Ex(\d+)_Analysis2")
P_DATE = re.compile(r"examination of[^,.]*\d{4}")
P_LECT = re.compile(r"\((?:Prof\.|Dr\.)[^)]*\)|names no lecturer")

noun, vs_orig, vs_src, self_odd = [], [], [], []
cited = collections.defaultdict(list)
for b in blocks:
    if not b["exinfo"]:
        continue
    is_ex = b["env"] in ("exercise", "aiexercise")
    if is_ex and re.match(r"\s*This example\b", b["exinfo"]):
        noun.append(f'{b["file"]}:{b["line"]}  {b["env"]} says "This example..."')
    if not is_ex and re.match(r"\s*This exercise\b", b["exinfo"]):
        noun.append(f'{b["file"]}:{b["line"]}  {b["env"]} says "This exercise..."')
    m = P_SHEET.search(b["exinfo"])
    if not m:
        continue
    cited[(m.group(3), m.group(1), m.group(2))].append(f'{b["file"]}:{b["line"]}')
    if m.group(1) != m.group(3):
        self_odd.append(f'{b["file"]}:{b["line"]}  "Problem {m.group(1)}.{m.group(2)} of '
                        f'Problem Sheet {m.group(3)}" -- sheet numbers disagree')
    for c in b["comments"]:
        o = P_ORIG.search(c)
        if o and (m.group(1), m.group(2), m.group(3)) != (o.group(2), o.group(3), o.group(1)):
            vs_orig.append(f'{b["file"]}:{b["line"]}  exinfo Problem {m.group(1)}.{m.group(2)}'
                           f'/Sheet {m.group(3)} vs % Originally: sheet {o.group(1)}, '
                           f'problem {o.group(2)}.{o.group(3)}')
            break
    for c in b["comments"]:
        s = P_SRC.search(c)
        if s:
            if s.group(1) != m.group(3):
                vs_src.append(f'{b["file"]}:{b["line"]}  exinfo says Sheet {m.group(3)} '
                              f'but % Source: is Ex{s.group(1)}_Analysis2')
            break

report("exinfo noun does not match its environment", noun)
report("exinfo problem number disagrees with % Originally:", vs_orig)
report("exinfo sheet disagrees with the % Source: filename", vs_src)
report("the exinfo's own problem/sheet numbers disagree", self_odd)
report("one sheet problem cited by two different blocks",
       [f'Sheet {k[0]} problem {k[1]}.{k[2]}: {", ".join(v)}'
        for k, v in sorted(cited.items()) if len(v) > 1])
report("% Extractor: with no % Source: beside it",
       [f'{b["file"]}:{b["line"]}  {str(b["title"])[:55]}' for b in blocks
        if any(c.strip().startswith("% Extractor:") for c in b["comments"])
        and not any(c.strip().startswith(("% Source:", "% Quelle:")) for c in b["comments"])])
report("old-exam citation naming no lecturer",
       [f'{b["file"]}:{b["line"]}  {b["exinfo"][:95]}' for b in blocks
        if b["exinfo"] and P_DATE.search(b["exinfo"]) and not P_LECT.search(b["exinfo"])])

# ------------------------------------------------------------- C. titles ----
untitled = []
for f in FILES:
    for i, line in enumerate(TEXT[f].split("\n"), 1):
        if re.match(r"\s*\\begin\{(" + "|".join(TITLED) + r")\}\s*$", line):
            untitled.append(f"{rel(f)}:{i}  {line.strip()}")
report("environment with no title", untitled)

titles = collections.defaultdict(list)
for b in blocks:
    if b["title"]:
        titles[b["title"]].append(f'{b["file"]}:{b["line"]}')
report("two blocks sharing one title",
       [f'"{k}"  at  {", ".join(v)}' for k, v in sorted(titles.items()) if len(v) > 1])

# A title must say what the problem is about, not what shape it is (gemini.md).
FORMAT_ONLY = re.compile(r"^(True or False|Multiple [Cc]hoice)\s*"
                         r"(\\textnormal\{\((important|semi-important|optional)\)\})?\s*$")
report("title names only the question format, not the subject",
       [f'{v[0]}  "{k}"' for k, v in sorted(titles.items()) if FORMAT_ONLY.match(k)])

report("title still carrying a sheet-number prefix",
       [f'{v[0]}  "{k}"' for k, v in sorted(titles.items())
        if re.match(r"^\d+\.\d+\s*-", k)])

# --------------------------------------------------------- D. build traps ---
traps = []
for f in FILES:
    for i, raw in enumerate(TEXT[f].split("\n"), 1):
        line = code(raw)
        for m in re.finditer(r"\\cpageref\{([^}]*)\}", line):
            if "," in m.group(1):
                traps.append(f"{rel(f)}:{i}  \\cpageref given a list -- breaks the build")
        if re.search(r"(^|[^\\])\bqt\{", line):
            traps.append(f"{rel(f)}:{i}  bare 'qt{{' -- a lost backslash")
        if re.search(r"\\rot\b", line):
            traps.append(f"{rel(f)}:{i}  \\rot is undefined -- use \\curl")
report("documented build traps", traps)

# CamelCase colour names used in tikz options but never defined. This is the
# ThemeRed class of bug: pgfkeys ignores the unknown key, prints an error into the
# log and carries on, so the picture silently loses its colour.
defined = set(re.findall(r"\\(?:definecolor|colorlet)\{([A-Za-z]+)\}",
                         MAIN.read_text(encoding="utf-8", errors="replace")))
# xcolor's dvipsnames, which main.tex loads and the figures use freely.
DVIPS = set("""Apricot Aquamarine Bittersweet Black Blue BlueGreen BlueViolet
BrickRed Brown BurntOrange CadetBlue CarnationPink Cerulean CornflowerBlue Cyan
Dandelion DarkOrchid Emerald ForestGreen Fuchsia Goldenrod Gray Green GreenYellow
JungleGreen Lavender LimeGreen Magenta Mahogany Maroon Melon MidnightBlue Mulberry
NavyBlue OliveGreen Orange OrangeRed Orchid Peach Periwinkle PineGreen Plum
ProcessBlue Purple RawSienna Red RedOrange RedViolet Rhodamine RoyalBlue
RoyalPurple RubineRed Salmon SeaGreen Sepia SkyBlue SpringGreen Tan TealBlue
Thistle Turquoise Violet VioletRed White WildStrawberry Yellow YellowGreen
YellowOrange""".split())
# arrow tips and other CamelCase pgf keys that are not colours
KNOWN_KEYS = {"Latex", "Straight", "Circle", "Stealth", "Bar", "To", "Square",
              "Triangle", "Rectangle", "Kite", "Parenthesis", "Computer",
              "Implies", "Hooks", "Butt", "Round", "Arc", "Glyph"}
unknown = []
for f in FILES:
    for i, raw in enumerate(TEXT[f].split("\n"), 1):
        line = code(raw)
        if "\\draw" not in line and "\\fill" not in line and "\\node" not in line \
           and "\\path" not in line:
            continue
        for m in re.finditer(r"[\[,]\s*([A-Z][A-Za-z]{2,})\s*[,\]]", line):
            name = m.group(1)
            if name not in defined and name not in DVIPS and name not in KNOWN_KEYS:
                unknown.append(f"{rel(f)}:{i}  '{name}' is not a colour this document defines")
report("tikz option naming a colour that does not exist", unknown)

# ---------------------------------------------------------- E. build log ----
for logname in ("check.log", "main.log"):
    log = ROOT / logname
    if not log.exists():
        continue
    lt = log.read_text(encoding="utf-8", errors="replace")
    errs = re.findall(r"^! .*$", lt, re.M)
    undef = re.findall(r"^LaTeX Warning: (?:Reference|Citation) .*$", lt, re.M)
    over = re.findall(r"Overfull \\hbox \(([0-9.]+)pt", lt)
    report(f"{logname}: errors", errs)
    report(f"{logname}: undefined references", undef)
    report(f"{logname}: overfull hboxes",
           [f"{p}pt too wide" for p in sorted(over, key=float, reverse=True)],
           informational=True)
    break

# ------------------------------------------------------------- verdict ------
print("\n" + "-" * 62)
if findings:
    print(f"{len(findings)} finding(s).")
    sys.exit(1)
print("Clean.")
