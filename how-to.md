# How to write tasks for a PropPra

The target audience of this document is ProPra authors, not instructors and not students.


## Difficulty levels

Writing a task works differently for different levels of task difficulty.  
Low-difficulty tasks (levels 1 and 2) have lots of detail and guidance in the task description.  
High-difficulty tasks (level 4) in contrast rely a lot on external documentation and
the students' own thinking.  
Medium-difficulty tasks (level 3) have a mix of both.

There will be a tendency to underestimate how difficult a task is for the students,
so make sure a level-3 task feels a lot more like level-2 than like level-4.


## The role of motivation

Given the huge freedom we give students and the superficial manner in which we
check their solutions, the ProPra's success depends massively on the students'
own motivation to learn.

Therefore,

- each taskgroup (the typical case) or individual task (as needed) must carefully explain 
  why the material will be (or can be) useful for a practicing software engineer;
- we should make every attempt at implementing one of the principles described in this article:
  [12 Prinzipien zur Motivation Lernender](https://link.springer.com/chapter/10.1007/978-3-658-26990-6_1)


## Special sedrila markup

Chapter, taskgroup, and task files mostly use standard markdown syntax,
plus two types of extension: macro calls and replacement blocks.

### Macros

- Macros have names in all UPPERCASE and each have 0, 1, or 2 formal parameters.
- Sedrila supplies a fixed set of macros, discussed further down.
- Macro calls come in square brackets, parameters use a `::` as delimiter.    
  Examples: [SOMEMACRONAME], [OTHERMACRO::arg1], [YETANOTHER::arg1::arg2].
- If a macro is not defined or has a different number of parameters than supplied in the call,
  sedrila will complain.
- Some macros serve as markup for blocks of text. These macros come in `X`/`ENDX` pairs:  
  ```
  [MYBLOCK::arg1]
  body text, as many lines as needed
  [ENDMYBLOCK]
  ```
- Due to the simplistic parser used, an `X`/`ENDX` block cannot be nested in another
  `X`/`ENDX` block and both macro calls must be alone on a line by themselves.
- Non-block macro calls can be mixed with other content on a line.

### Replacement blocks

A replacement block looks like this:
```
some text <replacement id="someId">text to be replaced</replacement> some more text.
```
The idea is that the text to be replaced is somehow location-dependent
(such as the URL of a server of the local university)
and other universities using the same ProPra should be able to replace it
with their own local version in a simple manner.
Simple means they can fork the ProPra repository but need hardly ever make
any change to the actual task files, only to a single, central _replacements file_.

The replacements file is `replacements.md` in the top level of the ProPra repo.
It contains simply a list of replacement blocks:

```
<replacement id="someId">
our adapted local text (could also be on a single line instead of three)
</replacement>


<replacement id="otherId">
This is a longer replacement that can continue for multiple paragraphs.

Replacements can use _any_ **markup**, including macro calls,
only excluding other replacements.
[WARNING]
Beware of the dog!
[ENDWARNING]

## Next heading
And so on.  
</replacement>
```

Sedrila will replace the `text to be replaced` with its counterpart from the replacement file
exactly as written and will remove the `<replacement id="someId">` and `</replacement>` pseudo tags.
The `id` should start with the respective task, taskgroup, or chapter name.


## Section structure

Sections follow one after another; they cannot be nested.  
They are marked up using the `[SECTION]` block macro. Example:
```
[SECTION::goal::idea]
Understand section markup
[ENDSECTION]
```
The entire body of a task description is divided into sections; there is no extra text.  
In contrast, chapters' and taskgroups' `index.md` files can optionally use 
goal and background sections at their top, but then always
continue with section-free text for characterizing the content of the chapter or taskgroup.

### `[SECTION::goal::...]`

Short definition what is to be learned (this is the prefered type) or 
achieved (if this is mostly a stepping stone for something else). 

Either short or a bulleted list of short items.
Can be positioned first (this is the prefered structure) or 
in between two background sections or
after the entire background.

### `[SECTION::background::default]`  

Knowledge required for understanding the instructions and solving the task.

Only present if needed; typically for difficulty levels 1 and 2. Keep this short.  
If lots of background are needed, turn it into steps of the instructions.

### `[SECTION::instructions::...]`  

The main part of the task: Instructions what to do.

More strongly than for other sections, 
this section looks hugely different depending on difficulty level.
See the discussion of difficulty levels above and of instructions subtypes below.

### `[SECTION::submission::...]`  

Final part of the task: Description what to prepare for the instructor to check.

Characterizes 

- the format (eg. `.md` file or `.py` file or directory with several files),
- the content, 
- and perhaps quality criteria.


## Section subtypes

Goal:

- `[SECTION::goal::product]`:  
  A work product itself is the task's goal (because we want to have it or want to build on top of it).
  Usually difficulty 3 or 4.
- `[SECTION::goal::idea]`:  
  Understanding a concept or idea is the goal. Difficulty 1, 2, or 3.
- `[SECTION::goal::experience]`:  
  Accumulating experience from actual technical problem-solving is the task's goal.
  Difficulty 3 or 4.
- `[SECTION::goal::trial]`:  
  The task's goal is a mix of the types 'idea' (mostly) and 'experience' (smaller part). 
  Difficulty 1 to 3 (or perhaps 4).

Background:

- `[SECTION::background::default]`:  
  There is only one type of background section.

Instructions:

- `[SECTION::instructions::detailed]`:  
  The instructions are such that the student must merely follow them closely for 
  solving the task and hardly needs to do problem-solving themselves.
  These tasks are easy (difficulty 1 or 2) for the students but
  difficult for the authors, because we need to think of so many things.
- `[SECTION::instructions::loose]`:  
  The instructions are less complete; the student must fill instruction gaps of moderate size
  but we provide information where to look for the material to fill them.
  Difficulty 3 or 4.
- `[SECTION::instructions::tricky]`:  
  The instructions are of a general nature, far removed from the detail required for a solution.
  The student must not only determine many details, but must also make decisions that can
  easily go wrong, making a successful solution much harder.
  Difficulty 4.

Submission:

- `[SECTION::submission::reflection]`:  
  Students submit a text containing their thoughts about something.
- `[SECTION::submission::information]`:  
  Students submit concrete information they found in an inquiry. 
- `[SECTION::submission::snippet]`:  
  Students submit a short snippet of program text, e.g. a shell command (or a few).
- `[SECTION::submission::trace]`:  
  Students submit a log of an interactive session or the output of a program run. 
- `[SECTION::submission::program]`:  
  Students submit an entire program with many moving parts.


## Other markup and its use

- `[WARNING]`/`[ENDWARNING]`:    
  A warning of a pitfall to be avoided.
  Will render as an eye-catching text box.
- `[HINT::title text]`/`[ENDHINT]`:  
  Information, typically in the instructions section, that is helpful for solving the task
  but that students are intended to find out themselves.
  Therefore, the body text of the hint is not visible initially, only the title text is.
  Students can fold out the hint body when they recognize they need more help.
  Use this in particular for making sure a task that is intended to be
  difficulty 3 does not end up being difficulty 4.
- `[TAS::taskname]`: TA for "task", S for "short".
  Create a hyperlink to the task description file for task `taskname`.
  "short" means it looks like in the breadcrumb, essentially using the taskname as the link text.
- `[TAL::taskname]`: TA for "task", L for "long".
  Also creates a hyperlink to the task description for `taskname`.
  "long" means it uses the task's title as the link text.
- `[TAM::taskname::link text]`: TA for "task", M for "manual".
  A hyperlink to task `taskname` that uses `link text` for the link text.
- `[TGS::taskgroupname]`, `[TGL::taskgroupname]`, `[TGM::taskgroupname::link text]`:
  Like the previous three, but for task groups instead of tasks.
- `[CHS::chaptername]`, `[CHL::chaptername]`, `[CHM::chaptername::link text]`:
  Like the previous three, but for chapters instead of taskgroups.


## How we work

Suggested order of work steps towards task descriptions. 

1. Sketch a task group and its motivation.
2. List candidate tasks for the task group.
   Order them from more general (and useful for most people) to more specialized.  
   As a rule, the more general tasks should be difficulty 2, the specialized ones harder.  
   For the general tasks, split large ones (over two hours) into pieces, including
   pieces that should be "assumed" and then belong into 
   different taskgroups or even chapters. Create placeholders with todo markers for those.
3. Outline a task description by selecting the section structure, 
   in particular the section subtypes,
   and formulating the learning goal.
4. Draft the background (keep it short), instructions, and submission sections.
5. Have someone else review the description for coherence between goal and instructions/submission
   and for appropriateness of the instructions given the difficulty.