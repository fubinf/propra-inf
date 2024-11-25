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

-------------------------------------------------------------------------------------------

## Reviews to do for Lutz Prechelt

**Ich reviewe pro Kapitel die Einträge von oben nach unten. 
Bitte also neues unten anhängen oder ggf. selbst sinnvolle andere Reihenfolge entscheiden.**

### Basis
- ch/Basis/IDE/IDEFirstSteps.md (SW)

### Sprachen
- ch/Sprachen/Python2/Python-OOP-Intro.md (HA->LP)
- ch/Sprachen/Python2/Python-OOP-Methods.md (HA->LP)
- ch/Sprachen/Python2/Python-OOP-Inheritance.md (HA-LP)

### Bibliotheken
- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (RR->CH->LP)

### Bestandscode
- ch/Bestandscode/SystemUnderTest/SUT_v100.md (RR->LP)


### Testen
- ch/Testen/Unittests/m_pytest_plugin_linter_flake8.md (RR-LP)
- ch/Testen/Betriebsumgebung/LokalesDeployment.md (RR -> LP) Grundlage für weitere Task

### Web

### Werkzeuge
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Editoren.md (Condric->LP->IC->LP->IC-LP)
  Ich bin mir hier unsicher, was in den Instructor-Teil soll. Es gibt ja keine falschen 
  Antworten für die Reflektion. 
- ch/Werkzeuge/Unix-Basiswerkzeuge/Unix-Links.md (Condric->LP->IC->LP->IC->LP)
- ch/Werkzeuge/Netzwerk/rsync.md (IC->LP)

-------------------------------------------------------------------------------------------

## Reviews to do for Hanen Alrwasheda

- Python1/ Inhalt wird am Ende ausgearbeitet.

- ch/Sprachen/Python2/Python-Context-Managers.md (HA->LP->HA)
- ch/Sprachen/Python2/Python-Function-Arguments-Advanced.md (HA->LP->HA)
- ch/Sprachen/Python2/Python-import.md (HA->LP->HA->LP->HA)

## Reviews to do for Ivan Condric
- ch/Werkzeuge/Netzwerk/traceroute.md: (kommt noch)  
  LP: "Den traceroute-Teil finde ich sehr anspruchsvoll. Wenn ich die Ähnlichkeiten und Unterschiede von
  `traceroute -T fu-berlin.de` und `traceroute fu-berlin.de` erklären sollte, würde ich ins
  Schleudern kommen. Oder warum im internen Netz manchmal bei fast jedem Hop ein Fehlschlag dabei ist.
  Und beim nächsten Mal wieder keiner. oderoderoder.  
  Kriegen wir das besser eingehegt?  
  Beispielsweise hatte ich mich gefragt, ob eine Route zur Uni Luxemburg wohl über Frankreich
  oder Belgien führt, um dann erstaunt zu lernen, dass sie bevorzugt über Polen plus Tschechien führt
  und alternativ über Niederlande plus Belgien. Staun.  https://network.geant.org/gn4-3n/  
  Nötigenfalls Schwierigkeit "mittel" nehmen und/oder traceroute abspalten."
- ch/Werkzeuge/Netzwerk/dnstools.md (Condric->LP->IC->LP->IC->LP->IC->LP->IC)


## Reviews to do for Christian Hofmann



## Reviews to do for Sven Hüster

- ch/Debugging/Debuggingtools/python-profiling.md (Hüster->LP->SH)  
  Siehe in der Datei.
- ch/Sprachen/RegExp/log_sanitizer (Hüster->fertiggestellt-Prechelt->SH)
- ch/Werkzeuge/Git/Git-Anpassen.md (Hüster)
- ch/Werkzeuge/Git/Git-Branches.md (Hüster->LP->SH->LP->SH)
- ch/Werkzeuge/Git/Git-Fehlerbehebung.md (Hüster->LP->SH->LP->SH->LP->SH):
  Musterlösung anpassen!
- ch/Werkzeuge/Git/Git-Rebase.md (Hüster->LP->SH)
- ...


## Reviews to do for Daniel Müllers

- ch/Web/CSS/CSSEinfuehrung.md (Müllers->LP->DM)  
  Ich finde a) dass der Theorieteil am Anfang reichlich lang ist, bis was Hübsches passiert, und
  b) dass man gern etwas mehr Fun-Faktor haben könnte, z.B. mit supergroßem Titel.  
  Ist aber jetzt schon mal beta.
- ch/Web/CSS/CSSSelektorenKlassen.md (DM->LP->DM)



## Reviews to do for Ronny Ruhe

- ch/Bibliotheken/pip-popular/requests.md (RR->DM->LP->RR->LP)  
  Nee, sorry, aber die Aufgabengruppe HTTP ist noch nicht brauchbar und auf der muss man
  gezielt aufbauen. Da steht nur uralter, viel zu schwieriger Kram drin.

- ch/Testen/API/ResponseApi.md (RR->CH->LP->RR)
- ch/Testen/API/CRUDApi.md (RR->CH->LP->RR)
- ch/Testen/API/RestApi.md (RR->CH->LP->RR)

- ch/Testen/Betriebsumgebung/GitHubDeployment.md (RR->LP->RR)
- ch/Testen/Betriebsumgebung/Github-Build2.md (RR->LP->RR)  
  Bitte erst die requires-Voraussetzung GitHubDeployment fertig machen.

- ch/Testen/Testframeworks/index.md (RR->CH->LP->RR)
- ch/Testen/Testframeworks/Robot.md (RR->CH->LP->RR->LP->RR)

- ch/Testen/Testgrundlagen/Testabgrenzung.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testcases-Testsuites-Testplans.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testpyramide.md (RR->LP->RR)
- Hmm, die Gruppe "Testgrundlagen" wird immer leerer.  
  Ist aber auch logisch: Das ist alles Theorie, passt also nicht von allein ins ProPra.
  Sondern nur, wenn man gute Reflektionsaufgaben findet oder einen empirischen "Forschungsteil" konstruiert.

- ch/Testen/SUT/LokalesDeployment.md (RR->CH->LP->RR)

- ch/Testen/Unittests/freezegun.md (RR->DM->HA->LP->RR->LP->RR)
- ch/Testen/Unittests/m_pytest_call (RR->LP->RR)
- ch/Testen/Unittests/m_pytest_plugin_testcoverage.md (RR->LP->RR)
- ch/Testen/Unittests/m_pytest_fixtures.md (RR->LP->RR)
- ch/Testen/Unittests/m_testcoverage.md (RR->LP->RR)
- ch/Testen/Unittests/m_unittest_fixtures.md (RR->LP->RR)
- ch/Testen/Unittests/mocking.md (Pietrak und RR->DM->HA->LP->RR)
- ch/Testen/Unittests/pytest103.md (Pietrak und RR->DM->LP->RR)
- ch/Testen/Unittests/pytest201.md (RR->DM->LP->RR)
- ch/Testen/Unittests/pytest202.md (RR->Müller->LP->RR)
- ch/Testen/Unittests/tdd.md (RR->DM->LP->RR)
- ch/Testen/Unittests/tdd_pp.md (RR->LP->RR)
- ch/Testen/Unittests/unittest102.md (RR->DM->HA->RR)
- ch/Testen/Unittests/unittest201.md (RR->DM->HA->LP->RR):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/m_unittest_mocking.md (RR->DM->HA->LP->RR) siehe Hinweise in der Datei
- ch/Testen/Unittests/unittest203.md (RR->Müller->LP->RR)
- ch/Testen/Unittests/m_pytest_benchmark.md (RR->DM)

- ch/Sprachen/Pythonpraxis/Passwortgenerator.md (RR->LP->RR)

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

