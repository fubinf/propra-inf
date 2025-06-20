title: "Pytest: Wie bringe ich Pytest dazu das auszuführen, was ich brauche?"
stage: alpha
timevalue: 1
difficulty: 2
assumes: m_pytest, pip
---

[SECTION::goal::idea]

Ich kann beim Aufruf von `pytest` nützliche Parameter verwenden, 
um schnell nur die relevanten Tests auszuführen.

[ENDSECTION]
[SECTION::background::default]

Pytest selbst führt normalerweise alle vorhandenen Testfälle aus.
Mit Pytest-Parametern kann man gezielt steuern, welche Tests ausgeführt werden,
was besonders in großen Projekten viel Zeit spart und die Übersicht verbessert.

[ENDSECTION]
[SECTION::instructions::loose]

### Testgrundlage beschaffen

Beschaffen wir uns zunächst eine Version der bekannten `requests`-Bibliothek`.
Klonen Sie folgendes Repository in Ihren [TERMREF::Hilfsbereich]:

```shell
git clone git@github.com:psf/requests.git --tag v2.32.2
```

Wir wollen jedoch dieses Paket nicht als Entwickler in einer eigenen Anwendung verwenden, sondern
die vorhandene Testsammlung kennenlernen.
Um das machen zu können, müssen wir noch die Abhängigkeiten installieren.
Das Projekt wird glücklicher Weise mit einer `requirements.txt` bereitgestellt.
Diese Datei erlaubt es uns die Abhängigkeiten mit einem Kommando zu installieren.
Führen Sie folgendes Kommando dazu aus:

```shell
pip install -r requirements-dev.txt
```

[HINT::Installationsprpoblem]
Achten Sie darauf, dass Sie sich im Verzeichnis `requests -tagv2.32.2` befinden oder den Pfad der
`requirements-dev.txt` Datei anpassen.
Ich empfehle Ersteres.
[ENDHINT]

[INFO]
Sicherlich ist Ihnen aufgefallen, dass zuvor `requirements.txt` und später `requirements-dev.txt`
erwähnt wurde.
Hier eine kurze Erklärung:

`requirements.txt` enthält die grundlegenden Abhängigkeiten, die benötigt werden, damit das
Python-Projekt läuft.
Diese Datei wird meist für die Installation im Produktivbetrieb verwendet.

`requirements-dev.txt` enthält zusätzliche Abhängigkeiten, die speziell für die Entwicklung und das
Testen des Projekts benötigt werden,
z.B. Test-Frameworks, Linter oder Build-Tools.
Sie baut oft auf `requirements.txt` auf und erweitert diese um Entwicklungs-Tools.

[ENDINFO]

### Testsuite ausprobieren, Einlesen in die Dokumentation

Sie wissen, dass Sie mit `python -m pytest` oder einfach `pytest` alle
existierenden Pytest-Testfälle ausführen können.
Manchmal möchte man diese Ausführung erweitern, aber auch einschränken.
Lesen Sie in der Hilfeausgabe von `pytest --help` im Abschnitt "general"
grob über diese Möglichkeiten nach.

Genaueres findet man dann in der offiziellen
[Pytest-Dokumentation](https://docs.pytest.org/en/latest) 
mittels Volltextsuche nach dem Optionsnamen (z.B. "--lf").
Machen Sie diesen Schritt am besten parallel zum Lösen der jeweiligen Aufgaben unten.

Zunächst lassen Sie die vorhanden Tests durchlaufen und schauen sich das Ergebnis an.
Führen Sie mittel dem Kommando `pytest` die Tests aus.

Im folgenden nehmen wir an, dass der Test wie gewollt durchgelaufen ist.
Demnach sollten Sie folgendes sehen:

```shell
======================================================== test session starts ========================================================
platform darwin -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: /requets -tagv2.32.2
configfile: pyproject.toml
testpaths: tests
plugins: httpbin-2.1.0, cov-6.1.1
collected 608 items                                                                                                                 

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
```

Was sehen wir hier:

- pytest hat insgesamt 608 Tests gefunden und ausgeführt.
- Die Punkte (.) stehen für erfolgreich bestandene Tests.
- Ein x markiert übersprungene (skipped) Tests, meist wegen fehlender Voraussetzungen oder
  bestimmter Einstellungen.
- Ein s steht für einen Test, der explizit als "skipped" markiert wurde.
- Es gab einen Fehler mit dem Test-Server (httpbin): [SSL: TLSV1_ALERT_UNKNOWN_CA], aber pytest hat
  versucht, diesen Fehler zu ignorieren, damit der Rest der Tests weiterlaufen kann.
- Am Ende siehst du noch eine Warnungs-Zusammenfassung (warnings summary), die auf eventuelle
  Probleme oder veraltete Funktionen hinweist.

Kurz: Die meisten Tests wurden erfolgreich ausgeführt, einige wurden übersprungen oder haben
Warnungen erzeugt, aber es gab keine großen Fehler, die den Testlauf komplett gestoppt hätten.

### Für Fehlschläge sorgen

Für unsere Zwecke in dieser Aufgabe brauchen wir eine Testsuite, die fehlschlägt.
Das tut die in unserem geklonten Repo jedoch nicht.
Deshalb bauen wir nun gezielt ein Versagen ein.
Damit wir (wie im wirklichen Leben) nicht schon im Voraus wissen, was das Problem ist,
verschleiert die Aufgabe das benutzte Kommando durch eine einfache Kodierung.
Bitte führen Sie also folgendes Kommando aus, ohne es zuvor zu analysieren.
(Das kann man hier im ProPra ausnahmsweise tun, weil man den Autoren des ProPra vertraut.
In einem realen Fall wäre es bei so einer Verschleierung angezeigt, zunächst zu klären, 
was das Kommando tut, denn es könnten ja ungute Zwecke sein.) 

```shell
cd v2.32.2
echo "bXYgcmVxdWlyZW1lbnRzLWRldi50eHQgcmVxdWlyZW1lbnQtZGV2ZWxvcC50eHQ=" | base64 --decode | bash
```

### Tests auf verschiedene Weisen ausführen

Verwenden Sie erneut den Befehl `pytest`, um die selben Tests auszuführen.
Dieses Mal werden Ihnen aber fehlschläge aufgelistet.

```shell
========================================================================== test session starts ===========================================================================
platform darwin -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: /requets -tagv2.32.2
configfile: pyproject.toml
testpaths: tests
plugins: httpbin-2.1.0, cov-6.1.1
collected 608 items                                                                                                                                                      

tests/test_adapters.py .                                                                                                                                           [  0%]
tests/test_help.py ...                                                                                                                                             [  0%]
tests/test_hooks.py ...                                                                                                                                            [  1%]
tests/test_lowlevel.py ....................                                                                                                                        [  4%]
tests/test_packages.py ...                                                                                                                                         [  4%]
tests/test_requests.py ............................................................................................F..F.F.....................spytest-httpbin server hit an exception serving request: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (_ssl.c:1018)
attempting to ignore so the rest of the tests can run
................... [ 27%]
.............................................................................................x.................................................................... [ 54%]
..............................                                                                                                                                     [ 59%]
tests/test_structures.py ....................                                                                                                                      [ 62%]
tests/test_testserver.py ......s....                                                                                                                               [ 64%]
tests/test_utils.py ..s........................................................................................................................................... [ 87%]
.........................................................sssssssssss.....s                                                                                         [100%]

================================================================================ FAILURES ================================================================================
```

Neben den bekannten erfolgreichen und übersprungenen Testfällen, kamen drei weitere
Fehlschläge - markiert durch ein F - hinzu.

Ab jetzt sieht die Testausführung aus Teil 1 etwas anders aus, was von uns auch gewollt ist.

Stellen Sie sich als Entwickler vor, dass Sie den Testfehlschlag durch eine Codeanpassung
vermeindlich gefixt haben.
Angenommen, Die Testsammlung läuft mit `pytest` einige Minuten lang bis zum Ende.
Sie wollen jedoch nur erfahren, ob alle Testfälle in der zuvor fehlgeschlagenen Testdatei erfolgreich
durchlaufen und nicht jedesmal lange auf das Ergebnis warten.
Um das zu überprüfen, wollen Sie den Test erneut laufen lassen, aber dieses Mal nur die zuvor
fehlgeschlagene Testdatei.

[ER] Lesen Sie in der Dokumentation nach, wie das geht, und 
starten Sie den Test nur auf die fehlgeschlagenen Dateien.
(Ähnlich in den folgenden Schritten: Bitte jedesmal in der Dokumentation die passende Option suchen.)

Wenn viele Testfälle im Spiel sind, führt ein einzelner Defekt oft gleich zu _zahlreichen_ Versagen,
was recht verwirrend sein kann.
In diesem Fall möchte man den Test nach dem ersten Versagen oft lieber abbrechen,
um sich der Analyse dieses ersten Problems zu widmen.

[ER] Lassen Sie den Testlauf beim Auftreten des _ersten_ Fehlers abbrechen.

Nach einer Korrektur, die den Defekt potenziell bereinigt hat, interessiert uns als erstes,
ob die zuvor fehlschlagenden Testfälle (bei uns gerade nur einer) nun erfolgreich durchlaufen.

[ER] Lassen Sie nur den letzten fehlgeschlagenen Testfall wieder durchführen
(und zwar ohne vorherige Korrektur, er wird also wiederum fehlschlagen).

Klappt einfach nicht. Na gut, vergeuden wir nicht viel Zeit, prüfen wir weiter, indem wir uns einen
kleinen Checkpoint beim ersten fehlgeschlagenen Testfall setzen, der uns Zeit erspart, um weiter
zu testen.

[ER] Verwenden Sie Pytest mit einem Flag, das beim nächsten Lauf nach dem fehlgeschlagenen Test startet.

Gut, den ersten Fehlschlag kennen wir. Den wollen wir jetzt ignorieren und den Testlauf weiter durchführen.

[ER] Lassen Sie den Testlauf direkt nach dem Fehlschlag weiterlaufen.

Es soll einfach nicht sein, der Testdurchlauf wird einfach nicht problemlos grün. Sie beschließen
erst einmal aufgrund mangelnden Risikos, diesen Testfall zu überspringen, bis Sie sich mit
Gleichgesinnten austauschen können, um dieses Problem zu beheben.

[ER] Skippen Sie alle fehlgeschlagenen Testfälle beim Ausführen aller Tests.

Natürlich dürfen wir diese leichtfertige Ignoranz nicht aus den Augen verlieren und sollten uns hin
und wieder vergewissern, dass wir beim Beheben unserer Anwendung auch vorankommen und die entsprechenden
Testfälle wieder freigeben.

[ER] Verschaffen Sie sich einen Überblick über die geskippten Testfälle.

Sie haben weiterhin versucht, dieses Problem zu beheben. Nach Ihrer Änderung hat sich der Test leider
nicht zu einem Besseren bewegt. Bevor Sie weitermachen, wollen Sie jedoch noch einmal alle Tests
mit detaillierteren Informationen ausführen, um zu prüfen, ob Ihre Codeanpassung keine Seiteneffekte
beinhaltet.

[ER] Starten Sie Pytest mit detaillierter Ausgabe.

Toll, diese Übersicht bietet Ihnen die Möglichkeit, wiederum in die gezielte Ansteuerung eines
Testfalls zu gehen.

[ER] Starten Sie Pytest nur für den Testfall `test_update`.

Nachdem Sie jetzt die Gelegenheit hatten, über das Problem des Fehlschlags zu diskutieren, haben Sie
sicherlich eine Lösung gefunden, alle Testfälle erfolgreich ausführen zu lassen, ohne einen Testfall
zu überspringen. Löschen Sie, falls noch vorhanden, die Skip-Anweisung.

[ER] Beseitigen Sie den Fehler und führen Sie Pytest ohne weitere Parameter aus. Wie sieht die Ausgabe
jetzt aus?

[HINT::Weg zur Lösung des Porblems]
Betrachten Sie die am Ende einer einfachen `pytest` Ausführung ausgegebenen Informationen.
(Letzten 3 Zeilen)
[ENDHINT]

### Reflektion

Jetzt, wo Sie einige Kommandos kennengelernt und ausgeführt haben, konnten Sie unteschiedliche
Ergebnisse und Ausgaben sehen.

[EQ] Welches Kommando war aus Ihrer Sicht das am effektivsten, um die eigentliche
Problematik zu erkennen.
[EQ] Wären Sie so oder so ähnlich auch vorgegangen oder wären Ihnen alternative Ausgaben oder
Schritte lieber gewesen?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
