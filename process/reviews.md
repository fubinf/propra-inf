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

- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (RR->CH)
- ch/Bibliotheken/Python-Standardbibliothek/os_path.md (Wegner)

- ch/Testen/Testgrundlagen/Testcases-Testsuites-Testplans.md (RR->LP) (Merge aus Testcases und TestcasesExercise)
- ch/Testen/Testgrundlagen/Testpyramide.md (RR->LP)
- ch/Testen/Testgrundlagen/Testabgrenzung.md (RR->LP) (Merge aus TestDelimitations und TestDelimitationsExercise)
- ch/Testen/Unittets/m_unittest_fixtures.md (RR->LP)
- ch/Testen/Unittests/m_pytest_fixtures.md (RR->LP)
- ch/Testen/Unittests/m_pytest_benchmark.md (RR->DM->LP)
- ch/Testen/Unittests/m_unittest_mocking.md (RR->DM->HA->LP)
- ch/Testen/Unittests/m_unittest_github.md (RR->LP)

- ch/Werkzeuge/Linter/flake8.md (RR->HA->CH)
- ch/Werkzeuge/Linter/black.md (RR->HA->CH)
- ch/Werkzeuge/Linter/flake8_SUT.md (RR->DM)

- ch/Bestandscode/SystemUnderTest/SUT_v100.md (RR->DM)

- ch/Debugging/Denkweisen/Mathematician.md (Pietrak->CH->LP)

- ch/Bestandscode/Refactoringpraxis/refactor_movierental_planning.md (Pietrak)
- ch/Bestandscode/Refactoringpraxis/refactor_movierental_implementation.md (Pietrak)

- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Editoren.md (Condric)
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Links.md (Condric)

- ch/Werkzeuge/Linter/flake8.md (Ruhe->HA->CH)
- ch/Werkzeuge/Linter/black.md (Ruhe->HA->CH)
- ch/Werkzeuge/Linter/flake8_SUT.md (Ruhe->DM)

- ch/Werkzeuge/Netzwerk/SSH.md (Condric)
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

- ch/Werkzeuge/Unix-Basiswerkzeuge/Informationensammlung.md (Condric->LP->IC)  
  Hübsch!  
  Bitte in `altdir` eine Musterlösung ablegen.  
  Was hat es mit dem "exclude"-Hinweis auf sich? Den verstehe ich nicht.  
  Für htop braucht man Markdown, nicht Kommandoprotokoll, oder?
- ch/Werkzeuge/Benutzerverwaltung/sudo.md (Condric->LP->IC)  
  ch/Werkzeuge/Benutzerverwaltung/Accounts.md (Condric->LP->IC)  
  ch/Werkzeuge/Benutzerverwaltung/Dateiberechtigungen.md (Condric->LP->IC)  
  Gefallen mir inhaltlich gut, im Detail habe ich aber doch eine Menge Änderungswünsche gehabt
  und großenteils gleich umgesetzt. 
  Bitte vollziehen Sie das anhand der Commits oder des Endresultats nach.  
  Ich habe alle drei schon mal auf beta gesetzt, aber die brauchen bitte alle noch eine
  **Musterlösung**.
  Welchen Sinn hat das **`-R`** bei `chmod/chgrp`? Wenn da kein Hintergedanke steckt, bitte entfernen.
- ...


## Reviews to do for Christian Hofmann



## Reviews to do for Sven Hüster

- ch/Werkzeuge/Git/Git-Fehlerbehebung.md (Hüster->LP->SH->LP->SH)
- ch/Werkzeuge/Git/Git-Branches.md (Hüster->LP->SH)
- ch/Werkzeuge/Git/Git-Rebase.md (Hüster)
- ch/Sprachen/RegExp/log_sanitizer (Hüster->fertiggestellt-Prechelt->SH)
- ...


## Reviews to do for Daniel Müllers

- ch/Web/HTML/HTMLErsteSchritte.md (Müllers->LP->DM)


## Reviews to do for Dominik Pietrak

- ch/Debugging/Debuggingtools/IDE_debugging.md (Pietrak->LP->DP)  
  Bitte nochmal prüfen (ich habe einiges geändert), dann auf beta setzen.

- ch/Bestandscode/Refactoring-Grundlagen/SOLID_principle.md (Pietrak->HA->DP->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/single_responsibility_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/open_closed_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/liskov_substitution_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/interface_segregation_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/dependency_inversion_prinzip.md (Pietrak->LP->DP)


## Reviews to do for Ronny Ruhe

- ch/Testen/Unittests/m_testcoverage.md (RR->LP)
- ch/Testen/Unittests/mocking.md (Pietrak und RR->DM->HA->LP)
- ch/Testen/Unittests/unittest102.md (RR->DM->HA->RR)
- ch/Testen/Unittests/tdd_pp.md (RR->LP->RR)
- ch/Testen/Unittests/freezegun.md (RR->DM->HA->LP->RR_LP)
- ch/Testen/Unittests/tdd.md (RR->DM->LP)
- ch/Testen/Unittests/pytest103.md (Pietrak und RR->DM->LP)
- ch/Testen/Unittests/pytest201.md (RR->DM->LP)
- ch/Testen/Unittests/unittest201.md (RR->DM->HA->LP):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/unittest203.md (RR->Müller)
- ch/Testen/Unittests/pytest202.md (RR->Müller)
- ch/Testen/API/ResponseApi.md (RR->CH)
- ch/Testen/API/CRUDApi.md (RR->CH)
- ch/Testen/API/RestApi.md (RR->CH)
- ch/Testen/Testframeworks/index.md (RR->CH)
- ch/Testen/Testframeworks/Robot.md (RR->CH)
- ch/Testen/SUT/LokalesDeployment.md (RR->CH)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (RR->LP->RR)

- ch/Bibliotheken/pip-popular/requests.md (RR->DM->LP->RR)

- ch/Sprachen/SQL/SQLBasic.md (RR->HA->LP->RR)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprachen/SQL/SQLSelect.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLJoin.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLProject.md (RR->HA->LP->RR)


## Reviews to do for Sven Wegner

