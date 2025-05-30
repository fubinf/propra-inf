# How to use the ProPra

The target audience of this part of the document is course leads of ProPra courses.
These use the `author` command for building the course website,
then the `instructor` command during the course.

1. Make sure you have a platform with an up-to-date Python (you need not know Python yourself).
   The ProPra itself assumes Debian/Ubuntu, but other variants of Linux (including on Windows WSL)
   will work just as well. Mac OS is not tested well, it may or may not work.   
   You need to know how to work with `git`.
2. Clone the present repo (see https://github.com/fubinf) and `cd propra-inf`.
3. Install the `pipx` Linux package.
4. Perform `pipx sedrila` to install the sedrila tool.  
   It serves as the build tool for the ProPra website (using its `author` command),
   as the tool for course participants (who use the `student` commmand) for submitting tasks and for 
   reviewing their completion status, and
   as the tool for course instructors during the course (who use the `instructor` command)
   for reviewing student submissions and recording acceptance/rejection per task.
5. `cp sedrila.yaml my-sedrila.yaml`. Review and adapt the contents of `my-sedrila.yaml`.
   Consult the respective section of the [sedrila docs](https://sedrila.readthedocs.io/en/latest/authors)
   for what the entries mean.
   For the moment, no changes are needed.
   For running an actual course later, make the following changes:
    - you need to change `instructors`
    - you will want to change `title` and `name`
    - perhaps you want to remove some taskgroups; simply delete the respective line
    - if the course will be served by an Apache webserver, adapt `htaccess_template`.  
      Then you can simply copy the entire generated tree (containing both the student
      version and the instructor version of the website) into a publicly visible directory.
      The `htaccess_template` will result in an `.htaccess` file that grants visibility of the
      instructor part to instructors only.  
      If you are using a different webserver, you need to solve this problem yourself.
6. Perform `sedrila author --config my-sedrila.yaml --include_stage beta out`.
   This builds the ProPra student website in directory `out` and 
   the ProPra instructor website in directory `out/instructor`.
7. Point your webbrowser to `out/index.html` to review the student version of
   the website; start at the homepage.  
   Then point it to `out/instructor/index.html` and read the instructor instructions on the homepage
   to understand what other preparations are required: Each instructor needs to create a GPG keypair
   and the public keys must be recorded in `my-sedrila.yaml`.
8. Copy the tree below `out` to a directory that will be served by your webserver.
   Tell your students the URL. Start your ProPra course. That's it.

If you want to modify some aspects of the ProPra content, read the "Customization" part
of the [sedrila `author` documentation](https://sedrila.readthedocs.io/en/latest/authors)
for the technical aspects.
Once you understood those, read on below for some content aspects.

----------------------
----------------------

# How to write tasks for a ProPra

The target audience of this part of the document is ProPra authors, not instructors and not students.

## Principles

During the development of propra-inf, we have discovered the following principles
for its structure and attempt to obey them throughout:

- **SeDriLa template:** 
  We use [sedrila](https://github.com/fubinf/sedrila) and follow its conventions
  (as described in [doc/authors.md](https://github.com/fubinf/sedrila/blob/main/doc/authors.md)).
- **regular structure:**
  All tasks are arranged into a simple chapter/taskgroup/task hierarchy.
  All tasks follow the same simple goal/background/instructions/submission section structure.
  There are [naming conventions](https://sedrila.readthedocs.io/en/latest/authors/#114-naming-conventions).
- **motivation focus:**
  Landing pages of chapters and taskgroups, goal sections of tasks
  greet students with a very short text that explains why they might be interested in this
  material.
- **all audiences:**
  We have tasks at different levels of difficulty.
  Most are aimed at "average" students, but others cater for stronger ones or (rarely) very weak ones.
- **fine granularity:**
  Our tasks are small, most in the 1.0...1.5 hour range (smaller if needed), with a 4 hours maximum.
- **independent tasks**:
  We strive to avoid strong dependencies between tasks, so students can pick what they want as much as possible.
- **heavy cross referencing:**
  Our tasks cross-reference each other a lot to show their interconnectedness and to support
  the fine granularity. 
  There are standard types of cross-reference (`assumes`, `requires`, `explains`)
  and free-form ones (`[PARTREF]`).
- **glossary as glue:**
  A glossary entry lists all tasks referencing it and so serves as powerful glue in the 
  cross-referencing structure.
- **simple reviewing:**
  The requirements for what students submit are geared towards making it simple and quick
  for instructors to review them, in particular by means of shell command protocols:
  [Kommandoprotokolle](ch/_include/Kommandoprotokolle.md).
- **avoid academic material:**
  We avoid duplicating (or even refering to) academic material known from lectures
  and prefer tasks that feel practical, real-worldly and that can be understood
  mostly with common sense.

Most of these principles serve the same purpose:
Maximizing the students' motivation to learn and try out things
because they find them interesting and relevant, find the tasks are fun to do,
and can observe their progress well. 


## Specific assumptions

We assume the students taking the propra-inf to have the following knowledge and skills:
- Boolean logic
- Programming:
  - procedural programming with variables and state and common control flow constructs:
    if-then-else, for, while
  - programming with parameterized subroutines
  - object-oriented programming with classes, methods, inheritance
  - functional programming style
- Corresponding syntax, semantics and handling of Python,
  including basic use of lists, dictionaries, a small subset of `builtins`, and 
  hardly anything from the standard library.
- A second-semester course on algorithms and data structures

We do _not_ assume a good understanding of software design, especially modularization.
In parallel to this course, the students ought to take a big (9 ECTS) introductory
software engineering course, but some of them may do this earlier, later, or never (non-CS majors).


## Learning to write ProPra tasks

### 1. Learn `sedrila`

First, learn about `sedrila` in the
[README.md](https://github.com/fubinf/sedrila/blob/main/README.md) and
[authors.md](https://github.com/fubinf/sedrila/blob/main/doc/authors.md) parts of its documentation.


### 2. Use the task file template

When you start a new task description file, 
copy [ch/template.md](../ch/template.md) 
and use it as a template to have a clean up-to-date starting point.


### 3. Design for difficulty level

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


### 4. The role of motivation

Given the huge freedom we give students and the superficial manner in which we
check their solutions, the ProPra's success depends massively on the students'
own motivation to learn.

Therefore,

- each taskgroup (the typical case) or individual task (as needed) should explain 
  why the material will be (or can be) useful for a practicing software engineer;
- we should make every attempt at implementing one of the principles described in this article:
  [12 Prinzipien zur Motivation Lernender](https://link.springer.com/chapter/10.1007/978-3-658-26990-6_1)


### 5. Strive to re-use known didactic methods

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


### 6. Work steps towards a task description 

Suggested procedure:

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
   Background is for motivation only, not for delivering required information. 
5. Have someone else review the description for coherence between goal and instructions/submission
   and for appropriateness of the instructions given the difficulty.


## Language use (in German because we use German)

Zur Vermeidung inkonsistenter Sprache sollten wir einheitliche Begriffe für gleiche oder im
Kontext äquivalente Begriffe verwenden.
TODO_3: In dieser Hinsicht (einheitliche Sprache und Begrifflichkeiten) gibt es noch viel zu tun.

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


## Tech stuff

### Development flow in general

- We are not using branches, all commits happen on `main` directly.
  We are a closed group and trust each other to work carefully.
- Integrate your local commits via 'git pull --rebase', not via 'merge'.
- Our staging happens via the `stage:` attribute of each task (see 
  ["YAML top matter"](https://sedrila.readthedocs.io/en/latest/authors/#15-task-files-yaml-top-matter)).
  Changing this attribute replaces the pull request workflow typical in other open source projects.

### Working with the `altdir` submodule

- **After `git pull`**, the submodule is always in the **"detached HEAD"** state,  
  because the super-repo references a specific commit ID and that commit is now checked out.  
  This is usually the most recent commit and identical to `origin/main`, but that is not guaranteed.
- If you want to make changes in the submodule (which is often the case), 
  you may need to **clean it up**:
    - `(cd altdir; git log)` should show that `HEAD` and `origin/main` are aligned.
    - `(cd altdir; git switch main; git pull)` then brings the local `main` branch to that state.
- If in the check above `HEAD` and `origin/main` do _not_ match, someone messed up.  
  On 2024-07-02, for example, I found a branch `origin/detached` at `HEAD`, 
  which was one commit ahead of `origin/main`.  
  After the cleanup described above, this commit was still missing.  
  It could be restored with `(cd altdir; git reset --hard origin/detached)`; alternatively, you could use  
  `git cherry-pick <commit-id>` — but you should treat `git reset --hard` with proper caution.
- Until the next `git pull`, you can now **make commits** in the submodule.
- If you **forgot to clean up** and have already made local changes, you must  
  temporarily put them aside so they don't get wiped out during `git switch`:
    - `(cd altdir; git add myfile.xyz ...; git stash push -m myfile.xyz -- myfile.xyz ...)`  
      (`add` is only needed if `myfile.xyz` isn’t versioned yet.)
    - Then perform the cleanup and restore the file(s) with `(cd altdir; git stash pop)`.
    - If you committed such local changes despite all of git’s warnings:  
      Those commits will be lost during cleanup because they’re not connected to a proper branch.  
      Solution:  
      Remember the commit ID; perform cleanup as usual; reapply the commit using `cherry-pick`;  
      learn from this incident and take git's warnings more seriously next time.
- In the main repo, after changes, you may get the message  
  "fatal: cannot rebase with locally recorded submodule modifications" during `git pull`.  
  The reason and solution are described at  
  https://stackoverflow.com/questions/54215983/git-pull-error-fatal-cannot-rebase-with-locally-recorded-submodule-modificati  
  in the answer by Prechelt. The solution is usually:  
  `git pull --rebase --no-recurse-submodules`  
  `git submodule update --recursive`
- If you use a good IDE (such as PyCharm) for making your submodule changes,
  it will usually do much of the above for you automatically and life is a lot simpler.
  For keeping it simple, make sure you `pull` before you make changes, and
  `commit` and `push` those changes ASAP.
  The shorter your change episodes, the fewer git problems.