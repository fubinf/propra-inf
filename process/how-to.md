# 1. For course teachers: How to use the ProPra

The target audience of this part of the document is course leads of ProPra courses.
These use `sedrila`'s `author` command for building the course website,
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

# 2. For course authors: How to write tasks for a ProPra

The target audience of this part of the document is ProPra authors, not instructors and not students.

## 2.1 Principles

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


## 2.2 Prior knowledge we assume students to have

We assume the students taking the propra-inf to have the following knowledge and skills:
- Boolean logic
- Programming:
  - procedural programming with variables and state and common control flow constructs:
    if-then-else, for, while
  - programming with parameterized subroutines
  - basic object-oriented programming: classes, methods, inheritance
  - functional programming style
- Corresponding syntax, semantics, and handling of Python,
  including basic use of lists, dictionaries, a small subset of `builtins`, but 
  hardly anything from the standard library.

We do _not_ assume a good understanding of algorithms, data structures, 
or software design, especially modularization, at least for tasks at difficulty level 2 (easy).


## 2.3 Learning to write ProPra task content

### 2.3.1 Learn `sedrila`

First, learn about `sedrila` in the
[README.md](https://github.com/fubinf/sedrila/blob/main/README.md) and
[authors.md](https://github.com/fubinf/sedrila/blob/main/doc/authors.md) parts of its documentation.


### 2.3.2 Use the task file template

When you start a new task description file, 
copy [ch/template.md](../ch/template.md) 
and use it as a template to have a clean up-to-date starting point.


### 2.3.3 Design for difficulty level

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


### 2.3.4 The role of motivation

Given the huge freedom we give students and the superficial manner in which we
check their solutions, the ProPra's success depends massively on the students'
own motivation to learn.

Therefore,

- each taskgroup (the typical case) or individual task (as needed) should explain 
  why the material will be (or can be) useful for a practicing software engineer;
- we should make every attempt at implementing one of the principles described in this article:
  [12 Prinzipien zur Motivation Lernender](https://link.springer.com/chapter/10.1007/978-3-658-26990-6_1)


### 2.3.5 Strive to re-use known didactic methods

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


### 2.3.6 Work steps towards a task description 

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


### 2.3.7 `[SECTION::goal::...]`

The goal section

- is always rather short
- usually formulates one goal or two, not many
- aims at giving a quick idea what can be learned in this task to help students select tasks


### 2.3.8 `[SECTION::background::default]`

The background section

- is the only one that can be missing (but is usually present)
- should typically be short
- is _not_ used for providing background information that is part of the technical content
- is used only for _motivation_: Why or how it can be useful to have learned what can be learned here. 


### 2.3.9 `[SECTION::instructions::type]`

The instruction section

- is the main part of the task
- can be rather long
- Instructions of type `detailed` at difficulty 2 (easy) 
  carefully guide students through detailed, separate steps,
  that require understanding but little inventing (Bloom taxonomy level 3: apply),
  and use `[HINT]`s to help with the remaining inventing.
  The task should be easy for an average student working on it concentratedly.
  If there are many `[HINT]`s, students who'd prefer a more difficult task can make it
  more difficult for them by ignoring all the `[HINT]`s. 
  Therefore, turning some understanding step into an inventive step and providing a `[HINT]` for it
  can be a useful task design technique.
- Instructions of type `loose` at difficulty 3 (medium) 
  require much larger invention steps (Bloom taxonomy levels 4+5)
  but provide `[HINT]`s to make the task feasible for many more people.
  For difficult topics, difficulty 3 tasks sometimes use `detailed` instructions.
- Instructions of type `loose` or `tricky` at difficulty 4 (difficult) 
  require still larger invention steps and much more self-steered
  work for the understanding parts as well (Bloom taxonomy levels 4+5).
  They provide few `[HINT]`s (for `tricky`) or none.
- At any difficulty level, the instructions can and should provide `[EQ]` reflection questions where
  students make up their minds what they think are advantages/disadvantages of something,
  what they like/dislike (and why) etc. (Bloom taxonomy level 6).
  (At difficulty 2, we will accept almost any response, 
  at levels 3+4, the responses should be sensible.)

For the authors, tasks at difficulty 2 (easy) are much more work and also harder to get right 
than those at difficulties 3 or 4.
However, the majority of our tasks needs to have difficulty 2 in order to address the majority
of our audience adequately.


### 2.3.10 [SECTION::submission::subtype1,subtype2]

The submission section

- usually contains only calls to one or more of the boilerplate blocks  
  ´[INCLUDE::/_include/Submission-Kommandoprotokoll.md]` (if `[EC]` is present anywhere in the task)  
  `[INCLUDE::/_include/Submission-Quellcode.md]` (if `[ER]` is present)  
  `[INCLUDE::/_include/Submission-Markdowndokument.md]` (if `[EQ]` is present)  
  in a suitable order
- sometimes contains additional text, e.g. about what is or is not to be considered part of the source code
  or from what perspective to answer the `[EQ]` questions
- describes the character of the task via the submission subtypes:
    - `reflection`: There are `[EQ]` reflection questions
    - `information`: There are `[EQ]` fact-finding questions
    - `snippet`: The source code is to be viewed as a piecemeal collection of snippets 
       or there are `[EQ]` questions to be answered with a bit of source code
    - `program`: The source code is an entire program, largely written by the student
    - `trace`: There are `[EC]` command instructions
- The idea of having these subtypes is that they help designing the task if you decide
  on the subtypes _before_ deciding on the details of the task.


### 2.3.11 [SECTION::instructor::GistOfPriorities]

The instructor section

- will announce in its title what the instructors should consider most important
  (usually: what indicates whether the student has learned the main teachings of the task)
- will reflect that priority in the order of information in the section body:
  important stuff first!
- will use terms "must" and "should" for indicating reasons for rejecting a task
  vs. points for mere feedback comments from the instructor to the student
- will include concrete example answers for all `[EQ]` questions (with discussion if needed)
- will include a concrete command protocol for all `[EC]` items
- will (if there are `[ER]` items) either include an example solution source code
  via an `[INCLUDE::ALT:sourcefile.xyz]` (embedded in triple backquotes for formatting)
  or point to it via `[TREEREF::/Chapter/Group/File]`


### 2.3.12 Language use (in German because we use German)

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
Generell beugen wir Fremdwörter nach deutscher Rechtschreibung,
aber bevorzugen deutsche Begriffe, soweit die zumindest einigermaßen geläufig sind.

Wenn wir uns auf einen Teil der Universität beziehen, nennen wir sie beim vollen Namen
und benutzen `<replacement id="...">...</replacement>` Tags, um die Angabe änderbar zu machen.


## 2.4 Technical development process


### 2.4.1 Development flow in general

- We are not using branches, all commits happen on `main` directly.
  We are a closed group and trust each other to work carefully.
- Integrate your local commits via 'git pull --rebase', not via 'merge'.
  Call `git config pull.rebase true` once to make this the default.
- Our staging happens via the `stage:` attribute of each task (see 
  ["YAML top matter"](https://sedrila.readthedocs.io/en/latest/authors/#15-task-files-yaml-top-matter)).
  Changing this attribute replaces the pull request workflow typical in other open source projects.
- Tasks should be set to `stage: beta` only after a positive review by Lutz Prechelt.
  To start a review, create an issue named `MyChapter/MyTaskgroup/MyTask` and assign it to `prechelt`.  


### 2.4.2 Task review flow

- If the reviewing takes more than one round, Lutz Prechelt will unassign himself from the issue each time
  he hands back the task to you.
  Remember to assign him again once your rework is done or nothing will happen. 
- When submitting a task, consider whether you should mention special properties, design consideration, etc.
  If so, place them in the issue description. 
  Otherwise, just put "nothing special" there.
- In the review dialog, each partner may introduce identifiers `T1`, `T2`, etc. for giving
  arbitrary review "topics" a name within the review.
  Refer to these when you respond and introduce additional ones (just keep counting) as needed.
  (`T3` is often a better identifier than `F3`/`A4`/`K5` from the task text, because the latter are
  not stable when steps are added or removed.)
- Always respond to such topics.
- Once a task has reached review, finishing it and getting it published should usually take
  priority over work on other tasks, so that we produce value for the students earlier.


### 2.4.3 Task text layout conventions

- Line length: Restrict lines to 100 characters, prefer 80 where easily possible.
  Start each sentence on a new line.
  These two rules make the `diff` for later changes much more readable.
- Empty lines: Place two empty lines before each SECTION and before each heading.  
  Place one empty line before each blockmacro start line and after each blockmacro end line,
  but none after the start line (unless needed to repair a broken itemized list) 
  or before the end line. See `ch/template_md`.
- Put hyperlinks on a separate line.

`[SECTION::instructions::...]`
- uses `###` subheadings for explaining task structure and supporting skimming
- puts each `[EQ]`, `[ER]`, `[EC]` in a separate paragraph (or sometimes list item)
- puts subsequent short preparatory steps (that do not need a `[EQ]`, `[ER]`, `[EC]` marker)
  into unnumbered list items
- prefers medium-long paragraphs otherwise


### 2.4.4 Working with the `altdir` submodule

Unfortunately, working with submodules in git is a bit tricky.

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

