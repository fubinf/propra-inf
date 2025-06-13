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

TODO_1_ruhe: Abhängigkeiten installieren.


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

TODO_1_ruhe: Erfolgreichen Testlauf machen zur Orientierung.


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

TODO_1_ruhe: Fehlschlagenden Testlauf machen als Ausgangspunkt der Aufgaben.

Ab jetzt sieht die Testausführung aus Teil 1 etwas anders aus, was von uns auch gewollt ist.

Sie, als Entwickler, haben einen Testfehlschlag als Antwort erhalten, diesen aber direkt gefixt -
so glauben Sie es zumindest.
Um das zu überprüfen, wollen Sie den Test erneut laufen lassen, aber dieses Mal die zuvor
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

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
