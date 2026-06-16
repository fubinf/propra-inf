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

# 2. For course authors: How to write tasks for ProPra

See [CONTRIBUTING.md](CONTRIBUTING.md).

----------------------

# 3. For course lead: Review process for alpha tasks

non-portable; using example values

- `git pull`
- `claude_review`
- `/review-task ch/Testen/Unittests/pytest_fixtures https://github.com/fubinf/propra-inf/issues/68`
- Annotate `.claude/draft-reviews/r-pytest_fixtures.md`,
  perhaps make manual changes to `pytest_fixtures.md`.
- If task needs further work: Paste `r-pytest_fixtures.md` into issue #68
- If task is ready: `stage: beta`, make entry in `changes.md`, build, publish
- Make commit
- `git push`
- Make announcement in Discord
