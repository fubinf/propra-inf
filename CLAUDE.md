# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **propra-inf** (Programmierpraktikum Informatik), a self-driven lab course for bachelor-level Informatics students at FU Berlin. The course content is written in German.

The project uses **sedrila** as its build tool to generate a course website from Markdown task files.

## Build Commands

```bash
# Install sedrila (one-time setup)
pipx install sedrila

# Build the course website
sedrila author --config sedrila.yaml --include_stage beta out

# Build with custom config (recommended for actual courses)
cp sedrila.yaml my-sedrila.yaml
sedrila author --config my-sedrila.yaml --include_stage beta out
```

The generated website appears in `out/` (student version) and `out/instructor/` (instructor version).

## Repository Structure

- **ch/**: Main content directory containing chapters, taskgroups, and tasks
  - Each chapter is a subdirectory (Basis, Sprachen, Bibliotheken, Testen, Debugging, Bestandscode, Web, Werkzeuge, Programmierpraxis, Feedback)
  - Taskgroups are subdirectories within chapters
  - Tasks are individual `.md` files following the template structure
- **altdir/**: Alternative content directory (git submodule) containing:
  - `ch/`: Alternative task versions
  - `itree.zip/`: Instructor tree with solution files, command protocols, source code examples
- **baseresources/**: Base resources for the website (CSS, etc.)
- **process/**: Development documentation
  - `how-to.md`: Comprehensive guide for authors and instructors
  - `todo.md`: Work coordination and open issues
  - `aufgabenideen.md`: Ideas for new tasks
- **sedrila.yaml**: Course configuration file

## Task File Format

Tasks use YAML front matter plus sedrila macros. Use `ch/template.md` as a starting point:

```markdown
title: "Task Name"
stage: draft|alpha|beta
timevalue: 1.5
difficulty: 1|2|3|4
explains: glossary-term
assumes: OtherTask
requires: PrerequisiteTask
---

[SECTION::goal::product|idea|experience|trial]
Learning objectives
[ENDSECTION]

[SECTION::background::default]
Motivation
[ENDSECTION]

[SECTION::instructions::detailed|loose|tricky]
Task instructions with [EC], [EQ], [ER] markers
[ENDSECTION]

[SECTION::submission::reflection|information|snippet|trace|program]
[INCLUDE::/_include/Submission-*.md]
[ENDSECTION]

[INSTRUCTOR::ReviewPriority]
Instructor hints and sample solutions
[ENDINSTRUCTOR]
```

## Key Macros

- `[EC]`: Command to execute (generates command protocol submission)
- `[EQ]`: Question to answer (generates markdown document submission)
- `[ER]`: Code requirement (generates source code submission)
- `[HINT::Title]...[ENDHINT]`: Collapsible help
- `[PARTREF::TaskName]`: Link to another task/taskgroup/chapter
- `[TERMREF::Term]`: Link to glossary entry

## Development Workflow

- All commits happen directly on `main` (no branches)
- Use `git pull --rebase` (set default: `git config pull.rebase true`)
- Task review process: Set `stage: alpha`, create GitHub issue named `Chapter/Taskgroup/Task`, assign to reviewer
- After positive review, set `stage: beta` for publication
- TODO markers in files: `TODO_1` (urgent), `TODO_2` (soon), `TODO_3` (later)

## Working with the altdir Submodule

After `git pull`, the submodule is in "detached HEAD" state. To make changes:

```bash
cd altdir
git switch main
git pull
# Now make your changes and commit
```

If conflicts occur during pull:
```bash
git pull --rebase --no-recurse-submodules
git submodule update --recursive
```

## Language Conventions (German)

- "Verzeichnis" not "Ordner" (directory)
- "Defekt" for software defects (vs. "Fehler" for errors)
- "beispielsweise" not "z.B." in flowing text
- "Repo" as abbreviation for "Repository"
- "Git" for the software name, "git" in commands
