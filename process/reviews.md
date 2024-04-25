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


## Priority order

We need to produce material that students can start with, quick.

- Sprachen: 
    - Some Python2 is needed, e.g. import (Python1 is not urgent)
    - Pythonpraxis looks OK
- Bibliotheken:
    - Python-Standardbibliothek: implement TODO-marked pseudo-assumes entries

## Reviews to do for Daniel Müllers



## Reviews to do for Christian Hofmann



## Reviews to do for Lutz Prechelt


- ch/Sprachen/Python1/PythonBooleans.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonStrings.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt) 
- ch/Sprachen/Python1/PythonComments.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonIntegers.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonFloats.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonTypeConversion.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonIf.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonElifElse.md (Alrwasheda->Prechelt->Alrwasheda->Prechelt)
- ch/Sprachen/Python1/PythonFunctions.md (Alrwasheda->Prechelt)


- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (Ruhe->Hofmann)
- ch/Bibliotheken/Dokumentation/changelog.md (Prechelt->Ruhe->Prechelt) Keine Anmerkungen.
- ch/Bibliotheken/Dokumentation/changelog2.md (Prechelt->Ruhe->Prechelt) Zwei Übungen ergänzt, eine
  davon auf das SUT bezigen, um nachzuvollziehen, dass ein vorhandenes Changelog schöner ist, als
  eins aus einem wenig bekannten Produkt zu extrahieren. (darauf aufbauend könnte man noch mehr in
  die Reflektion gehen, wie sinnvoll so etwas gehalten wird?)
- ch/Bibliotheken/Python-Standardbibliothek/m_hashlib.md (Wegner)


- ch/Testen/Unittests/tdd.md (Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/pytest101.md (Pietrak und Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/pytest102.md (Pietrak und Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/pytest103.md (Pietrak und Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/pytest104.md (Pietrak und Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/pytest201.md (Ruhe->Müllers->Prechelt)
- ch/Testen/Unittests/unittest201.md (Ruhe->Müllers->Alrwasheda->Prechelt):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/unittest202.md (Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/unittest301.md (Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/unittest203.md (Ruhe->Müller)
- ch/Testen/Unittests/pytest202.md (Ruhe->Müller)
- ch/Testen/Unittests/coverage.md (Pietrak und Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/mocking.md (Pietrak und Ruhe->Müllers->Alrwasheda->Prechelt)
- ch/Testen/Unittests/pytestBenchmark.md (Ruhe->Müllers)
- ch/Testen/API/index.md (Ruhe->Hofmann)
- ch/Testen/API/ResponseApi.md (Ruhe->Hofmann)
- ch/Testen/API/CRUDApi.md (Ruhe->Hofmann)
- ch/Testen/API/RestApi.md (Ruhe->Hofmann)
- ch/Testen/Testframeworks/index.md (Ruhe->Hofmann)
- ch/Testen/Testframeworks/Robot.md (Ruhe->Hofmann)
- ch/Testen/SUT/LokalesDeployment.md (Ruhe->Hofmann)

- ch/Debugging/Denkweisen/Mathematician.md (Pietrak->Hofmann)
- ch/Debugging/Denkweisen/Psychologist.md (Pietrak->Hofmann)


- ch/Bestandscode/Refactoring-Grundlagen/SOLID_principle.md (Pietrak->Alrwasheda->Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/single_responsibility_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/open_closed_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/liskov_substitution_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/interface_segregation_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoring-Grundlagen/dependency_inversion_prinzip.md (Pietrak->Prechelt)
- ch/Bestandscode/Refactoringpraxis/gildedrose_tests.md (Pietrak)  !!!
- ch/Bestandscode/Refactoringpraxis/gildedrose_refactor.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_implementation.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_reflexion.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_planning.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_implementation.md (Pietrak)
- ch/Bestandscode/SystemUnderTest/SUT_v100.md (Ruhe->Müllers)


- ch/Web/HTML/HTMLErsteSchritte.md (Müllers)


- ch/Werkzeuge/Unix-Basiswerkzeuge/04_eigenes_System.md (Condric)
- ch/Werkzeuge/Unix-Basiswerkzeuge/05_Editoren.md (Condric)
- ch/Werkzeuge/Unix-Basiswerkzeuge/06_Links.md (Condric)
- ch/Werkzeuge/Git/git-branches.md (Hüster)
- ch/Werkzeuge/Git/git-rebase.md (Hüster)
- ch/Werkzeuge/Linter/flake8.md (Ruhe->Alrwasheda->Hofmann)
- ch/Werkzeuge/Linter/black.md (Ruhe->Alrwasheda->Hofmann)
- ch/Werkzeuge/Linter/flake8_SUT.md (Ruhe->Müllers)


- ch/Werkzeuge/Benutzerverwaltung/Dateiberechtigungen.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/Gruppen.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/Nutzer.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/sudo.md (Condric)

- ch/Werkzeuge/Netzwerk/SSH.md (Condric)
- ch/Werkzeuge/Netzwerk/SSH-Tunnel.md (Condric)
- ch/Werkzeuge/Netzwerk/SSH-Reversetunnel.md (Condric)
- ch/Werkzeuge/Netzwerk/rsync.md (Condric)
- ch/Werkzeuge/Netzwerk/dnstools.md (Condric)

## Reviews to do for Hanen Alrwasheda

- ...

## Reviews to do for Ivan Condric

- ch/Werkzeuge/Paketmanager/apt.md (Condric)
- ...


## Reviews to do for Melis Atarim

- ...


## Reviews to do for Ronny Ruhe

Bitte von oben nach unten abarbeiten:

- ch/Testen/Testgrundlagen/Error.md (Ruhe->Müllers->Prechelt->Ruhe->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/ErrorExercise.md (Ruhe->Müllers->Prechelt->Ruhe->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/Testcases.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestcasesExercise.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/Testpyramide.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestDelimitations.md (Ruhe->Müllers->Prechelt->Ruhe)
- ch/Testen/Testgrundlagen/TestDelimitationsExercise.md (Ruhe->Müllers->Prechelt->Ruhe)

- ch/Testen/Unittests/unittest101.md (Ruhe->Müllers->Alrwasheda->Prechelt->Ruhe)
- ch/Testen/Unittests/unittest102.md (Ruhe->Müllers->Alrwasheda->Ruhe)
- ch/Testen/Unittests/freezegun.md (Ruhe->Müllers->Alrwasheda->Prechelt->Ruhe)
- ch/Testen/Unittests/tdd_pp.md (Ruhe->Prechelt->Ruhe)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (Ruhe->Prechelt->Ruhe)

- ch/Bibliotheken/pip-popular/requests.md (Ruhe->Müllers->Prechelt->Ruhe)

- ch/Sprachen/SQL/SQLBasic.md (Ruhe->Alrwasheda->Prechelt->Ruhe)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprachen/SQL/SQLSelect.md (Ruhe->Alrwasheda->Prechelt->Ruhe)
- ch/Sprachen/SQL/SQLJoin.md (Ruhe->Alrwasheda->Prechelt->Ruhe)
- ch/Sprachen/SQL/SQLProject.md (Ruhe->Alrwasheda->Prechelt->Ruhe)


## Reviews to do for Sven Hüster

- ch/Sprachen/RegExp/log_sanitizer (Hüster->fertiggestellt-Prechelt->Hüster)
- ch/Werkzeuge/Git/git-Fehlerbehebung.md (Hüster->Prechelt->Hüster)

- ...


## Reviews to do for Sven Wegner



## Reviews to do for Dominik Pietrak

- ch/Debugging/Debuggingtools/IDE_debugging.md (Pietrak->Prechelt->Pietrak)  
  Bitte nochmal prüfen (ich habe einiges geändert), dann auf beta setzen.

