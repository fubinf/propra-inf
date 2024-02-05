# How to write tasks for a PropPra

The target audience of this document is ProPra authors, not instructors and not students.


## Sedrila

First, learn about sedrila in the
[README.md](https://github.com/fubinf/sedrila/blob/main/README.md) and
[authors.md](https://github.com/fubinf/sedrila/blob/main/doc/authors.md) parts of its documentation.


## Task file template

When you start a new task description file, 
copy [ch/template_md](../ch/template_md) 
and use it as a template to have a clean up-to-date starting point.


## Difficulty levels

Writing a task works differently for different levels of task difficulty.  

Low-difficulty tasks (levels 1 and 2) have lots of detail and guidance in the task description.  
We do not assume these students can easily discriminate relevant from irrelevant information.
This means they have a hard time finding suitable pieces in a large documentation
and they need to be explained the significance of important information.
This, in turn, means we have to guide them to relevant information by pointing out
specific sources, sections in sources, names of commands/flags/classes/methods etc. they can use,
or sometimes providing exact pieces of code they need directly.

High-difficulty tasks (level 4) in contrast rely a lot on external documentation and
the students' own thinking.  

Medium-difficulty tasks (level 3) either have a mix of both or 
are simple cases of what might otherwise be level 4.

There will be a tendency to underestimate how difficult a task is for the students,
so make sure a level-3 task leans more towards level-2 than towards level-4.
See macro `[HINT]` below.


## The role of motivation

Given the huge freedom we give students and the superficial manner in which we
check their solutions, the ProPra's success depends massively on the students'
own motivation to learn.

Therefore,

- each taskgroup (the typical case) or individual task (as needed) must carefully explain 
  why the material will be (or can be) useful for a practicing software engineer;
- we should make every attempt at implementing one of the principles described in this article:
  [12 Prinzipien zur Motivation Lernender](https://link.springer.com/chapter/10.1007/978-3-658-26990-6_1)


## Didactic methods

When designing a set of tasks, many difficult didactic decisions must be made:
What to cover at all? In which depth? In which order?
Using which scenarios/examples/instructions/problems?

For answering these, there are two approaches:
- Find sources (in your specific topic area) that do it visibly well
  and copy many of their ideas or solutions
- Develop your decisions from well-tried general teaching methods.

For the latter, find a list of possible models (mostly geared to interactive teaching
in schools) here:
[Liste der Unterrichtsmethoden (Wikipedia)](https://de.wikipedia.org/wiki/Liste_der_Unterrichtsmethoden)


## Language use (in German because we use German)

Zur Vermeidung inkonsistenter Sprache sollten wir einheitliche Begriffe für gleiche oder im
Kontext äquivalente Begriffe verwenden.

- "Anwendung" statt Programm/Software oder auch Paket (wo sinnvoll)
- "Verzeichnis" statt Ordner
- "Defekt" in der Verwendung von Softwaretechnik, insbesondere in Abgrenzung zu "Fehler"
- "beispielsweise" statt "z.B." in Fließtext

Bei der Einführung neuer Begriffe verwenden wir erstmals Anführungszeichen. Wollen wir sie
anschließend betont verwenden, machen wir sie *italic*. Bei der Einführung von deutschen
Fachbegriffen erwähnen wir die korrekte englische Vokabel in Klammern.

Die Verwendung von Blocktext ist für Code oder Codeteile oder technische Bezeichner gedacht.

Wir kürzen "Repository" mit "Repo" ab. Wir schreiben "Git", wenn wir die Software in einer
Art benennen, die kein Kommando ist. In Kommandos schreiben wir "git".

Wir vermeiden die Pluralisierung englischer Wörter, die auf y enden.
Generell beugen wir Fremdwörter nach deutscher Rechtschreibung.

Wenn wir uns auf einen Teil der Universität beziehen, nennen wir sie beim vollen Namen
und benutzen `<replacement id="...">...</replacement>` Tags, um die Angabe änderbar zu machen.


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