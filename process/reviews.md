# Reviewing process

## Rules

We will modify these rules over time when others appear more useful. 

- When an author finds a task as far developed as they can sensibly do,
  they put it in `stage: alpha` and send it into review.
- A task typically goes through two or three (usually sequential) stages of review:
  - Review by Daniel Müllers for possibly more or better didactical ideas
    for the task.
    Use your own judgment whether or when this is useful.
    Do it at least when you do not find your task very convincing.  
    Tasks come with `stage: alpha` and leave with `alpha` or `draft`.
  - Holistic review by Christian Hofmann or Hanen Alrwasheda.
    Tasks come with `stage: alpha` and leave with `alpha`, `beta`, or `draft`.
  - Review for release by Lutz Prechelt.
    Tasks come with `stage: alpha` or `beta` and should leave with `beta`, or `done`.
  - Review by anybody else for specific topic reasons as needed.
- Authors assign a task to a reviewer by writing a line of the following form
  in the reviewer's section below:  
  `ch/chaptername/taskgroupname/taskname.md (authorname)`
- Reviewers make simple changes (typos, hard-to-understand formulations, formatting stuff, etc.)
  themselves and defer complex changes to the author.
  They should leave simple changes to the author as well if they believe the author
  will learn from making them.
- Reviewers may add feedback in the task file 
  (a paragraph or itemized list starting with a TODO_1_someauthor marker; default case)
  or write them in the Discord if they believe everybody should see them.
- Reviewers then move the review task assignment line to the section (in `review.md`)
  of the next person that needs to consider the given task:
  They either hand the task back to the author (if the author needs to make changes or should
  look at changes the reviewer made) or forward it to the next reviewer.
- Authors, after reworking a task, hand over the improved task either to the next reviewer
  or to the same one again when appropriate.
  If the task appears to be finished, they assign `stage: beta` (or perhaps even no stage at all)
  and hand over to no one. 


## Reviews to do for Daniel Müllers

- ch/Testen/Basiswissen/index.md (Ronny Ruhe)
- ch/Testen/Basiswissen/error.md (Ronny Ruhe)
- ch/Testen/Basiswissen/errorExercise1.md (Ronny Ruhe)
- ch/Testen/Basiswissen/testcases.md (Ronny Ruhe)
- ch/Testen/Basiswissen/testcasesExercvise1.md (Ronny Ruhe)
- ch/Testen/Basiswissen/testDelimitations.md (Ronny Ruhe)
- ch/Testen/Basiswissen/testDelimitationsExercvise1.md (Ronny Ruhe)
- ch/Testen/Basiswissen/testpyramide.md (Ronny Ruhe)

- ch/Testen/Unittests/index.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/unittest101.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/unittest102.md (Ronny Ruhe)
- ch/Testen/Unittests/unittest201.md (Ronny Ruhe)
- ch/Testen/Unittests/unittest202.md (Ronny Ruhe)
- ch/Testen/Unittests/unittest301.md (Ronny Ruhe)
- ch/Testen/Unittests/pytest101.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/pytest102.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/pytest103.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/pytest104.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/pytest201.md (Ronny Ruhe)
- ch/Testen/Unittests/coverage.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/freezegun.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/mocking.md (Dominik Pietrak und Ronny Ruhe)
- ch/Testen/Unittests/tdd.md (Ronny Ruhe)
- ch/Debugging/Debugging-Praxis/Einkaufsliste-04.md (Dominik Pietrak)

- ch/Bibliotheken/stdlib/datetime.md (Sven Wegner)

- ch/Werkzeuge/Linter/flake8.md (Ronny Ruhe)
- ch/Testen/Linter/flake8_SUT.md (Ronny Ruhe)
- ch/Werkzeuge/Linter/black.md (Ronny Ruhe)

- ch/Sprachen/grundkenntnisse/PythonComments.md (Hanen Alrwasheda)
- ch/Sprachen/grundkenntnisse/PythonStrings.md (Hanen Alrwasheda)
- ch/Sprachen/grundkenntnisse/PythonIntegers.md (Hanen Alrwasheda)
- ch/Sprachen/grundkenntnisse/PythonFloats.md (Hanen Alrwasheda)


## Reviews to do for Christian Hofmann

- ch/Debugging/Debugging-Praxis/Einkaufsliste-02.md (Dominik Pietrak)
- ch/Debugging/Debugging-Praxis/Einkaufsliste-03.md (Dominik Pietrak)

- ch/Debugging/Denkweisen/Mathematician.md (Dominik Pietrak)
- ch/Debugging/Denkweisen/Professor-Solomon.md (Dominik Pietrak)
- ch/Debugging/Denkweisen/Psychologist.md (Dominik Pietrak)
- ch/Debugging/Denkweisen/Sherlock-Holmes.md (Dominik Pietrak)

- ch/Debugging/Häufige-Defektarten/a_logic.md (Dominik Pietrak)
- ch/Debugging/Häufige-Defektarten/b_expression.md (Dominik Pietrak)
- ch/Debugging/Häufige-Defektarten/b_variable.md (Dominik Pietrak)
- ch/Debugging/Häufige-Defektarten/d_indexing.md (Dominik Pietrak)
- ch/Debugging/Häufige-Defektarten/f_location.md (Dominik Pietrak)

- ch/Bibliotheken/stdlib/m_subprocess2.md (Lutz Prechelt)

- ch/Testen/SUT/LokalesDeployment.md (Ronny Ruhe)
- ch/Bibliotheken/stdlib/jsonBasic.md (Ronny Ruhe)
- ch/Bibliotheken/stdlib/jsonExercise.md (Ronny Ruhe)
- ch/Bibliotheken/stdlib/jsonPerformance.md (Ronny Ruhe)
- ch/Basis/Repo/SedrilaEinrichten.md (Christian Hofmann)
- ch/Basis/Repo/Einreichungen.md (Lutz Prechelt)

- ch/Bestandscode/Refactoringpraxis/01gildedrose_tests.md (Dominik Pietrak)
- ch/Bestandscode/Refactoringpraxis/02gildedrose_refactor.md (Dominik Pietrak)
- ch/Bestandscode/Refactoringpraxis/03gildedrose_implementation.md (Dominik Pietrak)
- ch/Bestandscode/Refactoringpraxis/04gildedrose_reflexion.md (Dominik Pietrak)

- ch/Testen/API/index.md (Ronny Ruhe)
- ch/Testen/API/responseApi.md (Ronny Ruhe)
- ch/Testen/API/CRUDApi.md (Ronny Ruhe)


## Reviews to do for Lutz Prechelt

- ch/Debugging/debuggingtools/gitbisect.md (Dominik Pietrak, reviewed by Hanen Alrwasheda)
- ...


## Reviews to do for Hanen Alrwasheda

- ...


## Reviews to do for Ivan Condric

- ch/Sprachen/pythonpraxis/mlh-rename (Lutz Prechelt)
- ...


## Reviews to do for Melis Atarim

- ch/Sprachen/pythonpraxis/mlh-pseudonymize2.md (Lutz Prechelt)
- ...


## Reviews to do for Ronny Ruhe

- ch/Testen/Testframeworks/index.md (Ronny Ruhe)
- ch/Testen/Testframeworks/Robot.md (Ronny Ruhe)
- ch/Testen/API/restApi.md (Ronny Ruhe)
- ch/Testen/Betriebsumgebung/index.md:
  Komplett neugeschrieben.
- ch/Testen/Betriebsumgebung/GitHubDeployment.md (Ronny Ruhe, zurück von Lutz Prechelt):
  Ich habe recht massive Änderungen gemacht, bitte vollziehen Sie nach, warum.
  Kann jetzt von mir aus so bleiben, wenn Sie keine Fehler entdecken.


## Reviews to do for Sven Hüster

- ch/Sprachen/pythonpraxis/mlh-gitac (Lutz Prechelt)
- ch/Sprachen/regex/log_sanitizer (Sven Hüster, fertiggestellt von Lutz Prechelt)
- ...


## Reviews to do for Sven Wegner

- ch/Werkzeuge/Paketmanager/venv.md (Lutz Prechelt)
- ch/Werkzeuge/Paketmanager/pip.md (Lutz Prechelt)
- ch/Bibliotheken/Frameworks/argparse-subcommand.md (Lutz Prechelt)


## Reviews to do for Dominik Pietrak

- ch/Basis/Repo/Markdown101.md (Dominik Pietrak, reviewed by Hanen Alrwasheda)