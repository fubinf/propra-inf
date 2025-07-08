title: "Pytest: Wie bringe ich Pytest dazu das auszuführen, was ich brauche?"
stage: beta
timevalue: 1
difficulty: 2
assumes: m_pytest, pip, venv, Umgang-mit-Verzeichnissen
---

[SECTION::goal::idea]

Ich kann beim Aufruf von `pytest` nützliche Parameter verwenden, 
um schnell nur die relevanten Tests auszuführen.

[ENDSECTION]
[SECTION::background::default]

Pytest führt normalerweise alle vorhandenen Testfälle aus.
Das kann lange dauern und/oder zu unübersichtlich langen Ausgaben führen.
Mit Pytest-Parametern kann man flexibel steuern, welche Teilmenge von Tests ausgeführt wird,
was besonders in großen Projekten viel Zeit spart und die Übersicht verbessert.

[ENDSECTION]
[SECTION::instructions::loose]

### Testgrundlage beschaffen

Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein `venv` an (das wir nur für diese eine Aufgabe brauchen)
und aktivieren Sie es.

Beschaffen Sie den Projektbaum, an dem wir hier üben wollen.
Klonen Sie folgendes Repository in Ihren [TERMREF::Hilfsbereich] und wechseln Sie zur Version 2.32.2,
auf der unsere Aufgabe hoffentlilch wie geplant funktioniert:

```shell
git clone git@github.com:psf/requests.git
cd requests
git checkout v2.32.2
```

Wir sind nun also im Arbeitsverzeichnis des Repos.
Alle weiteren Schritte finden dort statt.
Installieren Sie als Erstes die Abhängigkeiten von `requests` in Ihr `venv`
und zwar in der Fassung für Entwicklung (die z.B. `pytest` mit einschließt):

```shell
pip install -r requirements-dev.txt
```


### Testsuite ausprobieren, Einlesen in die Dokumentation

Sie wissen, dass Sie mit `python -m pytest` oder einfach `pytest` alle
existierenden Pytest-Testfälle ausführen können.
Oft möchte man diese Ausführung aber einschränken (und weniger Testfälle laufen lassen)
oder die Betriebsweise modifizieren.
Lesen Sie in der Hilfeausgabe von `pytest --help` im Abschnitt "general"
grob über diese Möglichkeiten nach.

Genaueres zu jeder Option finden Sie bei Bedarf in der offiziellen
[Pytest-Dokumentation](https://docs.pytest.org/en/latest) 
z.B. auf den Seiten
[How to invoke...](https://docs.pytest.org/en/stable/how-to/usage.html)
oder
[How to re-run...](https://docs.pytest.org/en/stable/how-to/cache.html).
Lesen Sie am besten parallel zum Lösen der jeweiligen Aufgaben nach.
Kennt man sich nach einer Weile halbwegs aus, reicht einem aber `pytest --help` recht oft.

Zunächst lassen wir alle vorhandenen Tests durchlaufen und schauen uns das Ergebnis an:
```shell
pytest
```

Wenn alles wie gewollt durchgelaufen ist, sollten Sie _ungefähr_ so etwas sehen
(`[...]` markiert Auslassungen gegenüber der vollen Ausgabe):

```shell
======================================================== test session starts ========================================================
[...]
configfile: pyproject.toml
testpaths: tests
plugins: httpbin-2.1.0, cov-6.1.1
collected 606 items                                                                                                                 

tests/test_adapters.py .                                                                                                      [  0%]
tests/test_help.py ...                                                                                                        [  0%]
tests/test_hooks.py ...                                                                                                       [  1%]
tests/test_lowlevel.py ....................                                                                                   [  4%]
tests/test_packages.py ...                                                                                                    [  4%]
tests/test_requests.py ...................................................................................................... [ 21%]
.................spytest-httpbin server hit an exception serving request: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (_ssl.c:1018)
attempting to ignore so the rest of the tests can run
........................................................................................................... [ 42%]
.....x..................................................................................................                      [ 59%]
tests/test_structures.py ....................                                                                                 [ 62%]
tests/test_testserver.py ......s....                                                                                          [ 64%]
tests/test_utils.py ..s...................................................................................................... [ 81%]
..............................................................................................sssssssssss.....s               [100%]

========================================================= warnings summary ==========================================================
[...]
==================================== 590 passed, 15 skipped, 1 xfailed, 18 warnings in 82.55s (0:01:22) =============================
```

Was sehen wir hier? Bitte vollziehen Sie jeden der folgenden Punkte nach: 

- pytest hat insgesamt 606 Tests gefunden und ausgeführt.
- Die Punkte (.) stehen für erfolgreich bestandene Tests.
- Ein x markiert fehlgeschlagene Tests, die in der Testsuite markiert sind als
  "wir wissen, dass dieser Test fehlschlagen wird" (expected to fail: "xfail")
- Ein s steht für einen Test, der nicht ausgeführt wurde, weil er explizit als 
  "zu überspringen" ("skipped") markiert ist.
- Es gab Versagen des intern verwendeten Test-Servers (httpbin), 
  aber die Testsuite hat dies vor `pytest` versteckt, damit der Rest der Tests weiterlaufen kann.
- Hätte es Testversagen gegeben, würde nun der ausführliche Bericht darüber folgen.
- Danach folgt eine Warnungs-Zusammenfassung (warnings summary), die auf eventuelle
  Probleme oder veraltete Funktionen hinweist.
- Ganz am Ende kommt die Zusammenfassung des Testergebnisses.
  Ein Eintrag "failed" ist nicht dabei (der wäre rot), die Testsuite ist also 
  ohne Testversagen durchgelaufen.


### Für Fehlschläge sorgen

Für unsere Zwecke in dieser Aufgabe brauchen wir eine Testsuite, die fehlschlägt.
Das tut die in unserem geklonten Repo jedoch nicht.
Deshalb bauen wir nun gezielt ein Versagen ein.
Damit wir (wie im wirklichen Leben) nicht schon im Voraus wissen, was das Problem ist,
verschleiert die Aufgabe das benutzte Kommando durch eine einfache Kodierung.
Bitte führen Sie also folgendes Kommando einfach aus, ohne es zuvor zu analysieren.
(Das kann man hier im ProPra ausnahmsweise tun, weil man den Autoren des ProPra vertraut.
In einem realen Fall wäre es bei so einer Verschleierung angezeigt, zunächst zu klären, 
was das Kommando tut, denn es könnten ja ungute Zwecke sein.) 

```shell
echo "bXYgcmVxdWlyZW1lbnRzLWRldi50eHQgcmVxdWlyZW1lbnQtZGV2ZWxvcC50eHQ=" | base64 --decode | bash
```

### Gedachter Anwendungsfall

Verwenden Sie erneut den Befehl `pytest`, um dieselben Tests auszuführen.
Dieses Mal gibt es Fehlschläge:

```shell
========================================================================== test session starts =============================================================
[...]
tests/test_lowlevel.py ....................                                                                                                                        [  4%]
tests/test_packages.py ...                                                                                                                                         [  4%]
tests/test_requests.py ............................................................................................F..F.F.....................spytest-httpbin server hit an exception serving request: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (_ssl.c:1018)
attempting to ignore so the rest of the tests can run
[...]
FAILED tests/test_requests.py::TestRequests::test_POSTBIN_GET_POST_FILES - FileNotFoundError: [Errno 2] No such file or directory: 'requirements-dev.txt'
FAILED tests/test_requests.py::TestRequests::test_POSTBIN_GET_POST_FILES_WITH_DATA - FileNotFoundError: [Errno 2] No such file or directory: 'requirements-dev.txt'
FAILED tests/test_requests.py::TestRequests::test_conflicting_post_params - FileNotFoundError: [Errno 2] No such file or directory: 'requirements-dev.txt'
======================================= 3 failed, 587 passed, 15 skipped, 1 xfailed, 18 warnings in 82.53s (0:01:22) =======================================
```

Stellen Sie sich vor, Sie hätten eine Codeanpassung gemacht, von der Sie hoffen, dass sie
mindestens eines der Versagen löst, wollen aber nicht auf den Durchlauf der ganzen Testsuite warten,
weil Sie nicht erwarten, durch Ihre Korrektur "ganz woanders" etwas kaputt gemacht zu haben.


### Teilmengen von Tests ausführen

Sie wollen deshalb nur wissen, welche Testfälle in der (einzigen) zuvor fehlschlagenden Testdatei 
jetzt erfolgreich durchlaufen.
Um das zu überprüfen, wollen Sie den Test erneut laufen lassen, aber dieses Mal nur die zuvor
fehlgeschlagene Testdatei.

[ER] Lesen Sie in der Dokumentation nach, wie das geht, und 
starten Sie den Test nur für die Datei, die die drei Versagen hervorgebracht hatte.
(Ähnlich in den folgenden Schritten: Bitte jedesmal in der Dokumentation die passende Option suchen.)

In unserer Übung gibt es natürlich _doch_ wieder drei Versagen, weil wir ja gar keine Korrektur
gemacht haben. Aber diesmal ging der Test schon deutlich schneller!

Wenn viele Testfälle im Spiel sind, führt ein einzelner Defekt oft gleich zu _zahlreichen_ Versagen,
was recht verwirrend sein kann.
In diesem Fall möchte man eventuell den Test lieber schon nach dem ersten Versagen abbrechen,
um sich in Ruhe der Analyse dieses ersten Problems zu widmen.

[ER] Lassen Sie den Testlauf beim Auftreten des _ersten_ Fehlers abbrechen.

[EQ] Welchen Nachteil kann es (je nach Testsuite) haben, nur das erste Versagen zu sehen?

Obiges Verfahren reduziert zwar den Output, dauert aber bei der Testausführung eventuell
trotzdem noch recht lange, denn das erste Versagen kann ja sehr spät passieren.
Das kann man vermeiden, indem man nur die Testfälle nochmal ausführt, die zuletzt fehlgeschlagen waren.

[ER] Lassen Sie mittels der passenden Option nur die zuvor fehlgeschlagenen Testfälle wieder durchführen.

Whoa, das geht jetzt schön schnell!
Genau deshalb ist dies eine sehr gern eingesetzte Form des Aufrufs während einer Debugging-Phase.

Wenn viele Testfälle fehlschlagen, wird der Output von `pytest` schnell überwältigend lang.
Deshalb wäre es hilfreich, wenn man sich von einem Versagen zum nächsten hangeln könnte,
um also bei jedem Testlauf nur (maximal) ein Versagen zu sehen.

Genau dies zu erreichen, geht mit den Bordmitteln von `pytest` nicht, aber eine gute
Annäherung, bei der man maximal zwei Versagen pro Lauf sieht.
Lesen Sie die (nicht toll beschriebenen) Optionen `--stepwise` und `--stepwise-skip` nach.
Probieren Sie sie so lange aus, bis Sie die beste Annäherung an obiges Ideal herausgefunden haben.

[NOTICE]
Das führt am Ende zu vier Testläufen mit den Versagen 1, 1+2, 2+3, 3.  
Damit das ganze nicht zu lange dauert, geben Sie zusätzlich jeweils die Datei mit an wie bei
Schritt [EREFR::1].  
Sie dürfen gern auch die Kurznamen `--sw` und `--sw-skip` benutzen.  
Wenn Sie sich verfranst haben, brauchen Sie zum Rücksetzen in einen wohldefinierten Zustand
entweder `--sw-reset` oder einen Lauf ganz ohne `--sw`-Option.
[ENDNOTICE]

[ER] Zeigen Sie die Kommandos für diese vier Testläufe.


### Tests vorübergehend deaktivieren

In unserem Fall haben alle drei Versagen den gleichen Grund und der ist sehr einfach zu
verstehen. 
Aber angenommen, das wäre nicht so, sondern Sie geben das Debugging irgendwann entnervt auf:
Dann wäre von jetzt an die Testsuite nie mehr erfolgreich, was es schwer macht, 
andere, neue Versagen zu bemerken.

Deshalb deaktiviert man solche Testfälle in diesem Moment häufig für eine (hoffentlich!) begrenzte
Zeit, bis man sich ihnen mit frischer Energie wieder widmen kann.

Lesen Sie die Verwendung von `@pytest.mark.skip` nach.
Ändern Sie den Quellcode der Testsuite und deaktivieren Sie damit die drei fehlschlagenden Testfälle.
Geben Sie als Grund etwas Informatives an, z.B. den Kern der vom Test erhaltenen Fehlermeldung. 

[EC] `git diff`

Im wahren Leben ist die Kunst bei der Verwendung von `@pytest.mark.skip`
(oder seinem Vetter `@pytest.mark.xfail`), sich nach nicht allzulanger Zeit
erneut auf die Suche zu machen und diese Testprobleme sauber zu lösen.
Manchmal ist der richtige Weg, die entsprechenden Testfälle einfach zu löschen,
meistens sollte man sie aber reparieren.

Lassen Sie die Tests mit verkürzter Ausgabe (`-q`, `--quiet`) nochmal laufen:  
`pytest -q tests/test_requests.py`  
und überzeugen Sie sich, dass die drei Versagen verschwunden sind.
Sie müssten jetzt etwas mit  
`324 passed, 4 skipped, 1 xfailed`  
als Ergebnis bekommen.


### Überblick über Testsuite gewinnen

Stellen wir uns vor, ein Neuzugang in unserem Team bekommt die Aufgabe,
diese drei Versagen zu lösen und die deaktivierten Testfälle wieder zu aktivieren. 
Er oder sie hat keine Ahnung, wie die Testsuite aufgebaut ist.

Um eine unbekannte Testsuite kennenzulernen, kann man sie mit `-v` (für "verbose", also "geschwätzig")
oder sogar `-vv` ausführen, um mehr Information zu erhalten.
(Der Handlichkeit halber beschränken wir uns hier wieder auf die eine relevante Testdatei.)

Außerdem kann man mit `-r` (für "report") einen Extrabericht über bestimmte Sorten von
Testfällen erhalten, z.B. mit `-r s` über deaktivierte ("skipped") Testfälle.

[ER] Spielen Sie Neuzugang und verschaffen Sie sich mit beiden Optionen zusammen einen Überblick 
über die Testsuite.

Dabei lernen Sie beispielsweise, welche Testfälle es überhaupt gibt (Namen) und welche davon
besonders lange dauern.
Die Zusammenfassung der geskippten Fälle gibt einen Überblick über die Gründe:
bei uns z.B. dreimal der Gleiche.


### Eine maßgeschneiderte Gruppe von Testfällen bilden

Entfernen Sie die drei oben zugefügten `@pytest.mark.skip`
und geben Sie den betreffenden Tests stattdessen eine passende Bezeichnung,
z.B. `@pytest.mark.fixme`.
Dabei ist `fixme` ein weitgehend frei zu wählender Name;
man kann mit solchen Markierungen beliebige Gruppen von Testfällen bilden
(z.B. für besonders langsame Testfälle, um die dann manchmal auszuschließen).

Wir haben nun eine Gruppe genau für unseren Debugging-Zweck.
Lesen Sie nach, wie man mit `-m` (für "marked") die Testausführung auf solche Gruppen 
beschränken kann.


### Die Versagen lösen

Jetzt machen wir uns ernsthaft an die Arbeit mit dem Debugging der Versagensfälle.

[ER] Starten Sie Pytest nur für die `fixme`-Testfälle.

Hui! Das ging flott! So eine Testfallgruppe ist ein super Arbeitsmittel.

[ER] Diagnostizieren Sie nun das Problem, benennen Sie die betroffene Datei wieder passend
zurück um und starten Sie `pytest` nochmals in der gleichen Weise.

Nun sollten alle drei Tests erfolgreich gewesen sein.
Aber haben wir vielleicht dabei einen anderen Test kaputtgemacht?

[ER] Starten Sie nochmals die gesamte Testsuite und überzeugen Sie sich,
dass jetzt alle Testfälle erfolgreich sind.


### Reflektion

Versetzen Sie sich gedanklich nochmals an den Punkt, wo der Ablauf der gesamten Testsuite
_erstmals_ zu den drei Versagen geführt hat.
Sie starten als Nächstes also eine Debugging-Episode.

[EQ] Arbeiten Sie zum Debugging direkt mit dem Output des Komplett-Laufs oder 
beschaffen Sie sich mit einem zweiten Lauf zuvor einen kürzeren Output? Warum? 
Falls zweiter Lauf: Welches Kommando setzen Sie ein?

[EQ] Welche Option von `pytest` finden Sie allgemein besonders clever? Warum?
[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Quellcode.md]
Gefragt ist also überwiegend _nicht_ ein Kommandoprotokoll, sondern nur ein Shellskript `pytest_call.sh`
mit den Kommandos darin.
Notieren Sie darin vor jedem Kommando als Kommentar dessen Nummer.

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Nur auf korrekte Optionen prüfen]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
