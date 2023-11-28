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


