# Reviewing process

See process description in how-to.md.
These are the remainders of the previous process.
Do not add new entries here.

## Reviews to do for Lutz Prechelt

**Ich reviewe pro Kapitel die Einträge von oben nach unten. 
Bitte also neues unten anhängen oder ggf. selbst sinnvolle andere Reihenfolge entscheiden.**

### Testen
- ch/Testen/Unittests/pytest_mocking.md (RR->DM->HA->LP->RR->LP->RR->LP)
- ch/Testen/Unittests/pytest_mocking_freezegun.md (RR->DM->HA->LP->RR->LP->RR->LP) - leichte Überarbeitung
- ch/Testen/Betriebsumgebung/GitHub-Build.md (RR->LP->RR->LP)
- ch/Testen/Betriebsumgebung/Github-Build2.md (RR->LP->RR->LP)


### Werkzeuge
- ch/Werkzeuge/Netzwerk/X11-Weiterleitung.md (IC->LP)
- ch/Werkzeuge/Netzwerk/rsync.md (IC->LP->IC->LP)

### Sprachen
- ch/Sprachen/SQL/sql-SELECT.md (YL -> LP)
- ch/Sprachen/SQL/sql-JOIN.md (YL -> LP)

### (on hold)
- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (RR->CH->LP)
- ch/Bestandscode/SystemUnderTest/SUT_v100.md (RR->LP)
- ch/Testen/Unittests/pytest_plugin_linter_flake8.md (RR-LP)
- ch/Testen/Betriebsumgebung/LokalesDeployment.md (RR -> LP) Grundlage für weitere Task

-------------------------------------------------------------------------------------------

## Rework to do for Hanen Alrwasheda

- Python0/ Inhalt wird am Ende ausgearbeitet.

- ch/Sprachen/Python/py-OOP-Intro.md (HA->LP->HA)
- ch/Sprachen/Python/py-OOP-Methods.md (HA->LP->HA)
- ch/Sprachen/Python/py-OOP-Inheritance.md (HA-LP->HA)
- ch/Sprachen/Python/py-OOP-Praxis.md: (HA-LP->HA)
- ch/Sprachen/Python/py-Context-Managers.md (HA->LP->HA)
- ch/Sprachen/Python/py-Function-Arguments-Advanced.md (HA->LP->HA)
- ch/Sprachen/Python/py-import.md (HA->LP->HA->LP->HA)


## Rework to do for Ihar Brandes

- ch/Sprachen/Go0/go-ide.md (IB->LP->IB)


## Rework to do for Ivan Condric

- ch/Werkzeuge/Unix-Diverses/0x_cron.md


## Rework to do for Kilian Hofmann

- ch/Sprachen/C/c-preprocessor.md (KH->LP->KH)


## Rework to do for Sven Hüster

- ch/Debugging/Debuggingtools/python-profiling.md (Hüster->LP->SH)  
  Siehe in der Datei.
- ch/Sprachen/RegExp/log_sanitizer (Hüster->fertiggestellt-Prechelt->SH)
- ch/Werkzeuge/Git/Git-Anpassen.md (Hüster)
- ch/Werkzeuge/Git/Git-Branches.md (Hüster->LP->SH->LP->SH)
- ch/Werkzeuge/Git/Git-Fehlerbehebung.md (Hüster->LP->SH->LP->SH->LP->SH):
  Musterlösung anpassen!
- ch/Werkzeuge/Git/Git-Rebase.md (Hüster->LP->SH)
- ...


## Rework to do for Yixiang Li
- ch/Sprachen/SQL/sql-user-admin.md (YL)
- ch/Sprachen/SQL/SQL-project.md (YL)


## Rework to do for Daniel Müllers

- ch/Web/CSS/CSSEinfuehrung.md (Müllers->LP->DM)  
  Ich finde a) dass der Theorieteil am Anfang reichlich lang ist, bis was Hübsches passiert, und
  b) dass man gern etwas mehr Fun-Faktor haben könnte, z.B. mit supergroßem Titel.  
  Ist aber jetzt schon mal beta.


## Rework to do for Ronny Ruhe

Ich schlage (nur aus dem Gedächtnis, das kann also teilweise unpassend sein)
seeehr grob folgende Vorgehensweise und Arbeitsreihenfolge vor.
Die Teile heißen inzwischen teils ganz anders, mein Vorschlag ist nach ungefähren Themenkreisen
gedacht:

### Zuerst diese konsolidieren (Reihenfolge ist alphabetisch gemeint)
Unittest-Frameworks: `unittest` (nur elementare Nutzung),
`pytest` (und die wichtigsten Bells and Whistles).  
Außerdem Methodik des Testfallentwurfs für Modultests mit Äquivalenzklassen, Randfällen,
Fehlerfällen, Whitebox/Strukturtest.  
Einsatzfälle für Mocking: Fehlerfälle induzieren, schwergewichtige Kollaborateure loswerden.

- ch/Testen/Unittests/pytest-Methodik-Whitebox.md (RR->LP->RR)
- ch/Testen/Unittests/testcoverage.md (RR->LP->RR) Streichen, relevante Reste pytest_plugin_testcoverage.md
  aufnehmen
- ch/Testen/Unittests/pytest_plugin_testcoverage.md (RR->LP->RR) Auf die Testmethoden und pytest_call
  beziehen und weiterführen

- ch/Testen/Unittests/pytest_fixtures.md (RR->LP->RR->LP->RR)
- ch/Testen/Unittests/pytest103.md (Pietrak und RR->DM->LP->RR)
- ch/Testen/Unittests/pytest201.md (RR->DM->LP->RR)
- ch/Testen/Unittests/pytest202.md (RR->Müller->LP->RR)
- ch/Testen/Unittests/tdd.md (RR->DM->LP->RR)
- ch/Testen/Unittests/tdd_pp.md (RR->LP->RR)

### Welle 2
Weitere Unittest-Frameworks kurz antippen: `nosetest`, `doctest`, `robot`.  
Weitere nette pytest-Plugins.  
Typische Sorten von Tests: REST-APIs, Charakterisierungstests, ...

- ch/Testen/Testframeworks/index.md (RR->CH->LP->RR)
- ch/Testen/Testframeworks/Robot.md (RR->CH->LP->RR->LP->RR)
- ch/Testen/Unittests/pytest_benchmark.md (RR->DM)
- ch/Testen/Unittests/pytest_plugin_linter_flake8.md (RR-LP)
- ch/Testen/API/ResponseApi.md (RR->CH->LP->RR)
- ch/Testen/API/CRUDApi.md (RR->CH->LP->RR)
- ch/Testen/API/RestApi.md (RR->CH->LP->RR)
- ch/Werkzeuge/Linter/black.md (Ruhe->HA->CH->LP->RR)  
  siehe in der Datei

### Welle 3 oder sobald nötig
- ch/Bestandscode/SystemUnderTest/SUT_v100.md (RR->LP)
- ch/Testen/Betriebsumgebung/LokalesDeployment.md (RR -> LP) Grundlage für weitere Task
- ch/Bibliotheken/Python-Standardbibliothek/jsonPerformance.md (RR->CH->LP)
- ch/Sprachen/SQL/SQLBasic.md (RR->HA->LP->RR)  
  Bitte verfrachten Sie den allgemeinen Teil von Background ins Glossar.
  Ein Eintrag für SQL, einer für DBMS/RDBMS, die aufeinander verweisen.
  Es bleibt nur der Hinweis auf SQlite in der Aufgabe stehen.
- ch/Sprachen/SQL/SQLSelect.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLJoin.md (RR->HA->LP->RR)
- ch/Sprachen/SQL/SQLProject.md (RR->HA->LP->RR)

### vermutlich eher wegwerfen?
Methodisches passt ins ProPra nur, wenn es in praktische Aufgaben gekleidet daherkommt.
Von `unittest` behandeln wir nur die Grundlagen und ziehen dann `pytest` stets vor.

- ch/Testen/Testgrundlagen/Testabgrenzung.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testcases-Testsuites-Testplans.md (RR->LP->RR)
- ch/Testen/Testgrundlagen/Testpyramide.md (RR->LP->RR)
- Hmm, die Gruppe "Testgrundlagen" wird immer leerer.  
  Ist aber auch logisch: Das ist alles Theorie, passt also nicht von allein ins ProPra.
  Sondern nur, wenn man gute Reflektionsaufgaben findet oder einen empirischen "Forschungsteil" konstruiert.
- ch/Testen/Unittests/unittest102.md (RR->DM->HA->RR)
- ch/Testen/Unittests/unittest201.md (RR->DM->HA->LP->RR):
  Hier habe ich vor allem die Abgabe anders fromuliert. Auf Matrikelnummer im Namen der Abgabedatei
  kann verzichtet werden. Bitte überprüfen.
  Schwierigkeit und timevalue habe ich auch entsprechend erhöht.
- ch/Testen/Unittests/unittest203.md (RR->Müller->LP->RR)
- ch/Testen/Unittests/m_unittest_fixtures.md (RR->LP->RR)
- ch/Testen/Unittests/mocking.md (Pietrak und RR->DM->HA->LP->RR)
