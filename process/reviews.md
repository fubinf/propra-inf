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
- Reviewers may add long feedback in the task file 
  (a paragraph or itemized list starting with a TODO_1_someauthor marker)
  or shorter feedback in reviews.md
  or write feedback in the Discord if they believe everybody should see it.
- Reviewers then move the review task assignment line to the section (in `review.md`)
  of the next person that needs to consider the given task (author or reviewer) or
  delete it if the task has arrived in `beta` and needs no further change or check.


## Reviews to do for Lutz Prechelt

**Kapitel bitte in Reihenfolge des Inhaltsverzeichnisses, alles darunter in alphabetischer, Leerzeile pro Gruppe**

### Sprachen


### Bibliotheken
- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (RR->CH->LP)


### Bestandscode

- ch/Bestandscode/SystemUnderTest/SUT_v100.md (RR->DM)


### Debugging


### Testen

- ch/Testen/Unittests/m_pytest_fixtures.md (RR->LP->RR)
- ch/Testen/Unittests/m_pytest_benchmark.md (RR->DM->LP)
- ch/Testen/Unittests/m_unittest_mocking.md (RR->DM->HA->LP)
- ch/Testen/Unittests/m_unittest_github.md (RR->LP)
- ch/Testen/Unittests/m_testcoverage.md (RR->LP)


### Werkzeuge
- ch/Werkzeuge/Benutzerverwaltung/ACL.md
  Ich bin mir noch unsicher wie lange es sein soll und welche Schwierigkeit die Aufgabe haben soll
- ch/Werkzeuge/Benutzerverwaltung/Gruppen.md (Condric->LP->IC->LP)  

- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Editoren.md (Condric->LP)
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Links.md (Condric->LP)


## Reviews to do for Hanen Alrwasheda

- ch/Sprachen/Python1/PythonComments.md (Alrwasheda->LP->HA->LP->HA)
- ch/Sprachen/Python1/PythonBooleans.md (Alrwasheda->LP->HA->LP->HA)
- ch/Sprachen/Python1/PythonStrings.md (Alrwasheda->LP->HA->LP->HA)
- ch/Sprachen/Python2/Python-import.md (Alrwasheda->P->A)
- ...


## Reviews to do for Ivan Condric

- ch/Werkzeuge/Netzwerk/dnstools.md (Condric->LP->IC)  
  dig muss erst installiert werden. Wir sollten uns nicht auf eine "so kannste das installieren"-Meldung
  a la Debian verlassen.  
  Den traceroute-Teil finde ich sehr anspruchsvoll. Wenn ich die Ähnlichkeiten und Unterschiede von
  `traceroute -T fu-berlin.de` und `traceroute fu-berlin.de` erklären sollte, würde ich ins
  Schleudern kommen. Oder warum im internen Netz manchmal bei fast jedem Hop ein Fehlschlag dabei ist.
  Und beim nächsten Mal wieder keiner. oderoderoder.
  Kriegen wir das besser eingehegt?  
  Beispielsweise hatte ich mich gefragt, ob eine Route zur Uni Luxemburg wohl über Frankreich
  oder Belgien führt, um dann erstaunt zu lernen, dass sie bevorzugt über Polen plus Tschechien führt
  und alternativ über Niederlande plus Belgien. Staun.  https://network.geant.org/gn4-3n/  
  Nötigenfalls Schwierigkeit "mittel" nehmen und/oder traceroute abspalten.


- ch/Werkzeuge/Netzwerk/SSH.md (Condric->LP->IC)  
  Siehe Notizen in der Datei. Schwierig!

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

- ch/Bestandscode/Refactoring-Grundlagen/SOLID_principle.md (Pietrak->HA->DP->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/single_responsibility_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/open_closed_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/liskov_substitution_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/interface_segregation_prinzip.md (Pietrak->LP->DP)
- ch/Bestandscode/Refactoring-Grundlagen/dependency_inversion_prinzip.md (Pietrak->LP->DP)

- ch/Bestandscode/Refactoringpraxis/refactor_movierental_planning.md (Pietrak->LP)  
  ch/Bestandscode/Refactoringpraxis/refactor_movierental_implementation.md (Pietrak->LP)  
  Auf beta gesetzt, aber bitte die Musterlösung noch konkretisieren.
  Zu jedem Item brauchen die Tutoren Anhaltspunkte.
  Bei _implementation darf das gern Bezug auf _planning nehmen.

- ch/Debugging/Denkweisen/Mathematician.md (Pietrak->CH->LP->DP)  
  Für die ganze Taskgruppe bitte jeweils Korrekturhilfen in altdir zufügen.
  Z.B. könnten die für jede Frage beispielhaft je einen Gesichtspunkt für zwei gegensätzliche
  denkbare (akzeptable) Positionen der Studis benennen, um den Rahmen abzustecken,
  in dem die Antworten ungefähr erwartet werden.
  Vielleicht manchmal auch unakzeptable erläutern.
- ch/Debugging/Debuggingtools/IDE_debugging.md (Pietrak->LP->DP)  
  Bitte nochmal prüfen (ich habe einiges geändert), ggf. korrigieren, Eintrag hier löschen.


## Reviews to do for Ronny Ruhe

- ch/Testen/API/ResponseApi.md (RR->CH->LP->RR)
- ch/Testen/API/CRUDApi.md (RR->CH->LP->RR)
- ch/Testen/API/RestApi.md (RR->CH->LP->RR)

- ch/Testen/Testframeworks/index.md (RR->CH->LP->RR)
- ch/Testen/Testframeworks/Robot.md (RR->CH->LP->RR)

- ch/Testen/Testgrundlagen/Testabgrenzung.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testcases-Testsuites-Testplans.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testpyramide.md (RR->LP->RR)
- Hmm, die Gruppe "Testgrundlagen" wird immer leerer.  
  Ist aber auch logisch: Das ist alles Theorie, passt also nicht von allein ins ProPra.
  Sondern nur, wenn man gute Reflektionsaufgaben findet oder einen empirischen "Forschungsteil" konstruiert.

- ch/Testen/SUT/LokalesDeployment.md (RR->CH->LP->RR)

- ch/Testen/Unittests/m_unittest_fixtures.md (RR->LP->RR)
- ch/Testen/Unittests/mocking.md (Pietrak und RR->DM->HA->LP->RR)
- ch/Testen/Unittests/unittest102.md (RR->DM->HA->RR)
- ch/Testen/Unittests/tdd_pp.md (RR->LP->RR)
- ch/Testen/Unittests/freezegun.md (RR->DM->HA->LP->RR->LP->RR)
- ch/Testen/Unittests/tdd.md (RR->DM->LP->RR)
- ch/Testen/Unittests/pytest103.md (Pietrak und RR->DM->LP->RR)
- ch/Testen/Unittests/pytest201.md (RR->DM->LP->RR)
- ch/Testen/Unittests/unittest201.md (RR->DM->HA->LP->RR):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/unittest203.md (RR->Müller->LP->RR)
- ch/Testen/Unittests/pytest202.md (RR->Müller->LP->RR)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (RR->LP->RR)

- ch/Bibliotheken/pip-popular/requests.md (RR->DM->LP->RR)

- ch/Sprachen/SQL/SQLBasic.md (RR->HA->LP->RR)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprachen/SQL/SQLSelect.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLJoin.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLProject.md (RR->HA->LP->RR)

- ch/Werkzeuge/Linter/black.md (Ruhe->HA->CH->LP->RR)  
  siehe in der Datei

## Reviews to do for Sven Wegner

- ch/Bibliotheken/Python-Standardbibliothek/m_os.path.md (Wegner->LP->SW)  
  Musterlösung ergänzen (siehe TODO), meine Änderungen prüfen. Ist schon beta.
