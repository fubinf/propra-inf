# Reviewing process

## Rules

We will modify these rules over time when others appear more useful. 

- When an author finds a task as far developed as they can sensibly do,
  they put it in `stage: alpha` and send it into review.
- A task goes through one or possibly two stages of review:
  - Normal case: Hand it to Lutz Prechelt (who will finish it or hand it back to you with feedback).
  - If you are afraid your task may not be ready for this, hand it to Christian Hofmann first.
  - Tasks come into review with `stage: alpha` and leave with `alpha` or `beta`, or `draft`.
    `beta` is assigned by Lutz Prechelt only.
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


## Reviews to do for Lutz Prechelt


- ch/Sprachen/Python1/PythonIntegers.md (Alrwasheda->LP->HA->LP)
- ch/Sprachen/Python1/PythonFloats.md (Alrwasheda->LP->HA->LP)
- ch/Sprachen/Python1/PythonTypeConversion.md (Alrwasheda->LP->HA->LP)
- ch/Sprachen/Python1/PythonIf.md (Alrwasheda->LP->HA->LP)
- ch/Sprachen/Python1/PythonElifElse.md (Alrwasheda->LP->HA->LP)
- ch/Sprachen/Python1/PythonFunctions.md (Alrwasheda->LP)


- ch/Bibliotheken/Dokumentation/changelog.md (Prechelt->RR->LP) Keine Anmerkungen.
- ch/Bibliotheken/Dokumentation/changelog2.md (Prechelt->RR->LP) Zwei Übungen ergänzt, eine
  davon auf das SUT bezigen, um nachzuvollziehen, dass ein vorhandenes Changelog schöner ist, als
  eins aus einem wenig bekannten Produkt zu extrahieren. (darauf aufbauend könnte man noch mehr in
  die Reflektion gehen, wie sinnvoll so etwas gehalten wird?)

- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (Ruhe->CH)


- ch/Testen/Unittests/tdd.md (Ruhe->DM->LP)
- ch/Testen/Unittests/pytest101.md (Pietrak und Ruhe->DM->LP)
- ch/Testen/Unittests/pytest102.md (Pietrak und Ruhe->DM->LP)
- ch/Testen/Unittests/pytest103.md (Pietrak und Ruhe->DM->LP)
- ch/Testen/Unittests/pytest104.md (Pietrak und Ruhe->DM->LP)
- ch/Testen/Unittests/pytest201.md (Ruhe->DM->LP)
- ch/Testen/Unittests/unittest201.md (Ruhe->DM->HA->LP):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/unittest202.md (Ruhe->DM->HA->LP)
- ch/Testen/Unittests/unittest301.md (Ruhe->DM->HA->LP)
- ch/Testen/Unittests/unittest203.md (Ruhe->Müller)
- ch/Testen/Unittests/pytest202.md (Ruhe->Müller)
- ch/Testen/Unittests/coverage.md (Pietrak und Ruhe->DM->HA->LP)
- ch/Testen/Unittests/mocking.md (Pietrak und Ruhe->DM->HA->LP)
- ch/Testen/Unittests/pytestBenchmark.md (Ruhe->DM)
- ch/Testen/API/index.md (Ruhe->CH)
- ch/Testen/API/ResponseApi.md (Ruhe->CH)
- ch/Testen/API/CRUDApi.md (Ruhe->CH)
- ch/Testen/API/RestApi.md (Ruhe->CH)
- ch/Testen/Testframeworks/index.md (Ruhe->CH)
- ch/Testen/Testframeworks/Robot.md (Ruhe->CH)
- ch/Testen/SUT/LokalesDeployment.md (Ruhe->CH)


- ch/Debugging/Denkweisen/Mathematician.md (Pietrak->CH)


- ch/Bestandscode/Refactoring-Grundlagen/SOLID_principle.md (Pietrak->HA->DP->LP)
- ch/Bestandscode/Refactoring-Grundlagen/single_responsibility_prinzip.md (Pietrak->LP)
- ch/Bestandscode/Refactoring-Grundlagen/open_closed_prinzip.md (Pietrak->LP)
- ch/Bestandscode/Refactoring-Grundlagen/liskov_substitution_prinzip.md (Pietrak->LP)
- ch/Bestandscode/Refactoring-Grundlagen/interface_segregation_prinzip.md (Pietrak->LP)
- ch/Bestandscode/Refactoring-Grundlagen/dependency_inversion_prinzip.md (Pietrak->LP)
- ch/Bestandscode/Refactoringpraxis/gildedrose_tests.md (Pietrak)  !!!
- ch/Bestandscode/Refactoringpraxis/gildedrose_refactor.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_implementation.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/gildedrose_reflexion.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_planning.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_implementation.md (Pietrak)
- ch/Bestandscode/SystemUnderTest/SUT_v100.md (Ruhe->DM)


- ch/Werkzeuge/Unix-Basiswerkzeuge/Informationensammlung.md (Condric)
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Editoren.md (Condric)
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Links.md (Condric)

- ch/Werkzeuge/Git/git-branches.md (Hüster)
- ch/Werkzeuge/Git/git-rebase.md (Hüster)

- ch/Werkzeuge/Linter/flake8.md (Ruhe->HA->CH)
- ch/Werkzeuge/Linter/black.md (Ruhe->HA->CH)
- ch/Werkzeuge/Linter/flake8_SUT.md (Ruhe->DM)

- ch/Werkzeuge/Benutzerverwaltung/Dateiberechtigungen.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/Gruppen.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/Nutzer.md (Condric)
- ch/Werkzeuge/Benutzerverwaltung/sudo.md (Condric)

- ch/Werkzeuge/Netzwerk/SSH-Tunnel.md (Condric)
- ch/Werkzeuge/Netzwerk/SSH-Reversetunnel.md (Condric)
- ch/Werkzeuge/Netzwerk/rsync.md (Condric)
- ch/Werkzeuge/Netzwerk/dnstools.md (Condric)

- ch/Werkzeuge/Paketmanager/apt.md (Condric)


## Reviews to do for Hanen Alrwasheda

- ch/Sprachen/Python1/PythonComments.md (Alrwasheda->LP->HA->LP->HA)
- ch/Sprachen/Python1/PythonBooleans.md (Alrwasheda->LP->HA->LP->HA)
- ch/Sprachen/Python1/PythonStrings.md (Alrwasheda->LP->HA->LP->HA) 
- ch/Sprachen/Python2/Python-import.md (Alrwasheda->P->A)
- ...


## Reviews to do for Ivan Condric

- ch/Werkzeuge/Netzwerk/SSH.md (Condric)
- ...


## Reviews to do for Christian Hofmann



## Reviews to do for Sven Hüster

- ch/Sprachen/RegExp/log_sanitizer (Hüster->fertiggestellt-Prechelt->SH)
- ch/Werkzeuge/Git/git-Fehlerbehebung.md (Hüster->LP->SH)

- ...


## Reviews to do for Daniel Müllers

- ch/Web/HTML/HTMLErsteSchritte.md (Müllers->LP->DM)


## Reviews to do for Dominik Pietrak

- ch/Debugging/Debuggingtools/IDE_debugging.md (Pietrak->LP->DP)  
  Bitte nochmal prüfen (ich habe einiges geändert), dann auf beta setzen.


## Reviews to do for Ronny Ruhe

Bitte von oben nach unten abarbeiten:

- ch/Testen/Testgrundlagen/Error.md (Ruhe->DM->LP->RR->LP->RR)
- ch/Testen/Testgrundlagen/ErrorExercise.md (Ruhe->DM->LP->RR->LP->RR)
- ch/Testen/Testgrundlagen/Testcases.md (Ruhe->DM->LP->RR)
- ch/Testen/Testgrundlagen/TestcasesExercise.md (Ruhe->DM->LP->RR)
- ch/Testen/Testgrundlagen/Testpyramide.md (Ruhe->DM->LP->RR)
- ch/Testen/Testgrundlagen/TestDelimitations.md (Ruhe->DM->LP->RR)
- ch/Testen/Testgrundlagen/TestDelimitationsExercise.md (Ruhe->DM->LP->RR)

- ch/Testen/Unittests/unittest101.md (Ruhe->DM->HA->LP->RR)
- ch/Testen/Unittests/unittest102.md (Ruhe->DM->HA->RR)
- ch/Testen/Unittests/freezegun.md (Ruhe->DM->HA->LP->RR)
- ch/Testen/Unittests/tdd_pp.md (Ruhe->LP->RR)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (Ruhe->LP->RR)

- ch/Bibliotheken/pip-popular/requests.md (Ruhe->DM->LP->RR)

- ch/Sprachen/SQL/SQLBasic.md (Ruhe->HA->LP->RR)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprachen/SQL/SQLSelect.md (Ruhe->HA->LP->RR)
- ch/Sprachen/SQL/SQLJoin.md (Ruhe->HA->LP->RR)
- ch/Sprachen/SQL/SQLProject.md (Ruhe->HA->LP->RR)


## Reviews to do for Sven Wegner

- ch/Bibliotheken/Python-Standardbibliothek/m_hashlib.md (Wegner->LP->SW):  
  Die Aufgabe ist in vieler Hinsicht super, aber Sie haben sie abermals nicht selber
  durchgeführt. Das funktioniert nicht!
  Bitte holen Sie das jetzt nach und prüfen Sie, ob ich alle ihre Fehler erwischt habe;
  ich habe es nämlich auch nur teilweise praktisch durchgeturnt.

- ...

