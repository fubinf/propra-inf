# Reviewing process

## Rules

We will modify these rules over time when others appear more useful. 

- When an author finds a task as far developed as they can sensibly do,
  they put it in `stage: alpha` and send it into review.
- A task goes through one or possibly two stages of review:
  - Normal case: Hand it to Lutz Prechelt (who will finish it or hand it back to you with feedback).
  - If you are afraid your task may not be ready for this, hand it to Christian Hofmann first.
  - Tasks come into review with `stage: alpha` and leave with `alpha` or `beta`, or `draft`.
  - In special cases, send your task into review by anybody else as needed.
- Authors assign a task to a reviewer by writing a line of the following form
  in the reviewer's section below:  
  `ch/chaptername/taskgroupname/taskname.md (authorname)`
- Reviewers make simple changes themselves and defer complex changes to the author.
  They should leave simple changes to the author as well if they believe the author
  will learn from making them.
- Reviewers may add feedback in the task file 
  (a paragraph or itemized list starting with a TODO_1_someauthor marker; default case)
  or write them in the Discord if they believe everybody should see them.
- Reviewers then move the review task assignment line to the section (in `review.md`)
  of the next person that needs to consider the given task (author or reviewer) or
  delete it if the task has arrived in `beta`.


## Reviews to do for Daniel Müllers



## Reviews to do for Christian Hofmann



## Reviews to do for Lutz Prechelt

- ch/Testen/SUT/LokalesDeployment.md (Ruhe->Hofmann)
- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (Ruhe->Hofmann)

- ch/Bestandscode/Refactoringpraxis/gildedrose_tests.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_refactor.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_implementation.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_reflexion.md (Pietrak)

- ch/Testen/API/index.md (Ruhe->Hofmann)
- ch/Testen/API/ResponseApi.md (Ruhe->Hofmann)
- ch/Testen/API/CRUDApi.md (Ruhe->Hofmann)
- ch/Testen/API/RestApi.md (Ruhe->Hofmann)

- ch/Testen/Testframeworks/index.md (Ruhe->Hofmann)
- ch/Testen/Testframeworks/Robot.md (Ruhe->Hofmann)

- ch/Werkzeuge/Linter/flake8.md (Ruhe->Alrwasheda->Hofmann)
- ch/Werkzeuge/Linter/black.md (Ruhe->Alrwasheda->Hofmann)

- ch/Bestandscode/Refactoringpraxis/refactor_movierental_planning.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_implementation.md (Pietrak)

- ch/Werkzeuge/Linter/flake8_SUT.md (Ruhe->Müllers)

- ch/Testen/Unittests/tdd_pp.md (Ruhe->Müllers)
- ch/Testen/Unittests/pytestBenchmark.md (Ruhe->Müllers)

- ch/Bestandscode/SystemUnderTest/SUT_v100.md (Ruhe->Müllers)

- ch/Bibliotheken/pip-popular/requests.md (Ruhe->Müllers)

- ch/Testen/Unittests/unittest203.md (Ruhe->Müller)
- ch/Testen/Unittests/pytest202.md (Ruhe->Müller)
 
- ch/Debugging/Debugging-Praxis/einkaufsliste-versagen.md (Pietrak->Hofmann)
- ch/Debugging/Debugging-Praxis/einkaufsliste-conditional.md (Pietrak->Hofmann)

- ch/Debugging/Denkweisen/Mathematician.md (Pietrak->Hofmann)
- ch/Debugging/Denkweisen/Professor-Solomon.md (Pietrak->Hofmann)
- ch/Debugging/Denkweisen/Psychologist.md (Pietrak->Hofmann)
- ch/Debugging/Denkweisen/Sherlock-Holmes.md (Pietrak->Hofmann)

- ch/Debugging/Häufige-Defektarten/a_logic.md (Pietrak->Hofmann)
- ch/Debugging/Häufige-Defektarten/b_expression.md (Pietrak->Hofmann)
- ch/Debugging/Häufige-Defektarten/b_variable.md (Pietrak->Hofmann)
- ch/Debugging/Häufige-Defektarten/d_indexing.md (Pietrak->Hofmann)
- ch/Debugging/Häufige-Defektarten/f_location.md (Pietrak->Hofmann)

- ch/Testen/Unittests/coverage.md (Pietrak und Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/mocking.md (Pietrak und Ruhe->Müllers->Alrwasheda->Prechelt)

- ch/Testen/Unittests/unittest201.md (Ruhe->Müllers->Alrwasheda->Prechelt):
Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
kann verzichtet werden. Bitte überprüfen.
Schwierigkeit und timevalue habe ich auch entsprechend erhöht.

- ch/Testen/Unittests/unittest202.md (Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/unittest301.md (Ruhe->Müllers->Alrwasheda->Prechelt)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (Ruhe->Prechelt)

- ch/Debugging/Debugging-Praxis/einkaufsliste-postmortem.md (Pietrak->Müllers->Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/SOLID_principle.md (Pietrak->Alrwasheda->Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/single_responsibility_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/open_closed_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/liskov_substitution_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/interface_segregation_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/dependency_inversion_prinzip.md (Pietrak->Prechelt)

- ch/Bibliotheken/Dokumentation/changelog.md (Prechelt->Ruhe->Prechelt) Keine Anmerkungen.
- ch/Bibliotheken/Dokumentation/changelog2.md (Prechelt->Ruhe->Prechelt) Zwei Übungen ergänzt, eine
  davon auf das SUT bezigen, um nachzuvollziehen, dass ein vorhandenes Changelog schöner ist, als
  eins aus einem wenig bekannten Produkt zu extrahieren. (darauf aufbauend könnte man noch mehr in
  die Reflektion gehen, wie sinnvoll so etwas gehalten wird?)

- ch/Testen/Testgrundlagen/Error.md (Ruhe->Müllers->Prechelt->Ruhe->Prechelt)
- ch/Testen/Testgrundlagen/ErrorExercise.md (Ruhe->Müllers->Prechelt->Ruhe->Prechelt)

- ch/Sprachen/Python1/PythonBooleans.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)

## Reviews to do for Hanen Alrwasheda

- ch/Sprachen/Python1/PythonStrings.md (Alrwasheda->Prechelt->Alrwasheda) 
- ch/Sprachen/Python1/PythonComments.md (Alrwasheda->Prechelt->Alrwasheda)
  Über PythonBooleans und PythonStrings sprechen wir mal.
  PythonComments habe ich auch angeschaut und kommentiert.
  Alle übrigen gebe ich auf Verdacht zurück, weil manche der Kommentare vmtl. auch dort
  irgendwo relevant sind.
- ch/Sprachen/Python1/PythonIntegers.md (Alrwasheda->Prechelt->Alrwasheda)
- ch/Sprachen/Python1/PythonFloats.md (Alrwasheda->Prechelt->Alrwasheda)
- ch/Sprachen/Python1/PythonCasting.md (Alrwasheda->Prechelt->Alrwasheda)
- ch/Sprachen/Python1/PythonIf.md (Alrwasheda->Prechelt->Alrwasheda)
- ch/Sprachen/Python1/PythonElifElse.md (Alrwasheda->Prechelt->Alrwasheda)

- ch/Testen/Unittests/index.md (Pietrak und Ruhe->Müllers->Alrwasheda)

- ch/Testen/Unittests/tdd.md (Ruhe->Müllers->Alrwasheda)
- ch/Testen/Unittests/pytest101.md (Pietrak und Ruhe->Müllers->Alrwasheda)
- ch/Testen/Unittests/pytest102.md (Pietrak und Ruhe->Müllers->Alrwasheda)
- ch/Testen/Unittests/pytest103.md (Pietrak und Ruhe->Müllers->Alrwasheda)
- ch/Testen/Unittests/pytest104.md (Pietrak und Ruhe->Müllers->Alrwasheda)
- ch/Testen/Unittests/pytest201.md (Ruhe->Müllers->Alrwasheda)


## Reviews to do for Ivan Condric

- ch/Sprachen/Pythonpraxis/mlh-rename (Prechelt)
- ...


## Reviews to do for Melis Atarim

- ...


## Reviews to do for Ronny Ruhe

- ch/Testen/Testgrundlagen/Testcases.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestcasesExercise.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/Testpyramide.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestDelimitations.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestDelimitationsExercise.md (Ruhe->Müllers->Prechelt->Ruhe)

- ch/Testen/Unittests/unittest101.md (Ruhe->Müllers->Alrwasheda->Prechelt->Ruhe)
- ch/Testen/Unittests/unittest102.md (Ruhe->Müllers->Alrwasheda->Ruhe)
- ch/Testen/Unittests/freezegun.md (Ruhe->Müllers->Alrwasheda->Prechelt->Ruhe)

- ch/Sprachen/SQL/SQLBasic.md (Ruhe->Alrwasheda->Prechelt->Ruhe)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprache/SQL/SQLSelect.md (Ruhe->Alrwasheda->Prechelt->Ruhe)
- ch/Sprache/SQL/SQLJoin.md (Ruhe->Alrwasheda->Prechelt->Ruhe)
- ch/Sprache/SQL/SQLProject.md (Ruhe->Alrwasheda->Prechelt->Ruhe)


## Reviews to do for Sven Hüster

- ch/Sprachen/Pythonpraxis/mlh-gitac (Prechelt)
- ch/Sprachen/RegExp/log_sanitizer (Hüster, fertiggestellt von Prechelt)
- ...


## Reviews to do for Sven Wegner

- ch/Bibliotheken/Python-Standardbibliothek/m_subprocess2.md (Prechelt)
- ch/Bibliotheken/Python-Standardbibliothek/sorted_and_sort.md (Prechelt)

- ch/Bibliotheken/Frameworks/argparse_subcommand.md (Prechelt)


## Reviews to do for Dominik Pietrak

- ch/Debugging/debuggingtools/gitbisect.md (Pietrak->Prechelt->Pietrak):
  Habe die Einleitung ganz neu geschrieben, hoffentlich klarer.
  Die dient zur Motivation, gehört also nach [SECTION::Background].
- ch/Sprachen/Pythonpraxis/mlh-pseudonymize2.md (Prechelt)

- ch/Testen/Unittests/freezegun.md (Pietrak und Ruhe->Müllers->Alrwasheda->Prechelt->Pietrak und Ruhe)
