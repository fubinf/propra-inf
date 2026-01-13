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
  - `ch/`: Include files containing non-public, instructor-only content;
    parallels `ch/**`.
  - `itree.zip/`: Instructor tree with solution files, command protocols, source code examples;
    mostly parallels `ch/**`.
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

- `[EC]`: Render a command students should execute (which then contributes to command protocol submission)
- `[EQ]`: Question to answer (for markdown document submission)
- `[ER]`: Code requirement (for source code submission)
- `[HINT::Title]...[ENDHINT]`: Collapsible step-specific help; can (and often should) be nested for gradual help.
- `[PARTREF::TaskName]`: Link to another task/taskgroup/chapter
- `[TERMREF::Term]`: Link to glossary entry

## Task file YAML top matter

- `assumes`: names of other tasks. Students need to know the material of these and can have done the task or not.
- `requires`: names of other tasks. This task will build on top of products that students created in them.
- `difficulty`: 1: very easy; hardly ever used. 
  2: easy; guiding students through the work step-by-step. At least three quarters of
  all second-semester CS students should be able to solve the task with no major problems
  if (and often indeed only if) they read and work carefully.
  3: medium; the task steps are larger and students need to do some searching, thinking, or solving 
  without explicit instructions.
  4: difficult: suitable only for students that are highly intelligent or had much more previous
  programming practice than most.
- `timevalue`: how long (in hours) the average student should need for the task if they follow instructions
  carefully and make no major mistake. Granularity is 15 minutes up to 1.25 and 30 minutes beyond.

## Development Workflow

- All commits happen directly on `main` (no branches)
- Use `git pull --rebase` (set default: `git config pull.rebase true`)
- Task review process: Set `stage: alpha`, create GitHub issue named `Chapter/Taskgroup/Task`, assign to reviewer
- After positive review, set `stage: beta` for publication
- TODO markers in files: `TODO_1` (soon), `TODO_2` (soonish), `TODO_3` (later)

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


## How to review a task

A task can have a large variety of problems, for instance (in decreasing order of importance):

- Factual errors wrt the technical content (in which I am often not an expert)
- Unclear instructions for students or avoidable issues with terminological/conceptual clarity. 
- Unclear instructions for instructors wrt what is expected of a student solution and what is not.
  We aim to be liberal in what we expect. 
  Instructors should focus the checking on the few important bits
  that determine whether the specific learning goal of the task has likely been reached by the student.
- Task too simple or too difficult for the claimed `difficulty` and `timevalue`.
- Individual steps that are a bit harder but lack an accompanying [HINT] for reducing
  difficulty if need be, in particular for `medium` tasks.
- Redundancy (or, conversely, knowledge gaps) wrt to previous tasks (those in the `assumes` and `requires` chains)
- Submission section mentions the wrong submission types.
  (The instructions for the three standard types of submission (sum of the [EQ], [EC], [ER] steps, respectively)
  are described in task `Einreichungen`.)
- Issues with spelling, punctuation, grammar, sentence construction.

Review for these problems, but also apply programming common sense throughout.
Give me findings in two lists (major, minor), with just enough elaboration to understand the problem.


## Current development step

None.
