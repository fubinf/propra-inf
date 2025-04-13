title: "Pytest: Wie bringe ich Pytest dazu das auszuführen, was ich brauche?"
stage: alpha
timevalue: 1
difficulty: 2
assumes: m_pytest, pip
---

[SECTION::goal::idea]

- Ich kann nützliche Pytest Parameter verwenden, um effektiver meine Tests auszuführen.

[ENDSECTION]
[SECTION::background::default]

Pytest selbst führt normalerweise alle vorhandenen Testfälle aus.
Mit Pytest-Parametern kann man gezielt steuern, welche Tests ausgeführt werden,
was besonders in großen Projekten viel Zeit spart und die Übersicht verbessert.

[ENDSECTION]
[SECTION::instructions::loose]

### Testgrundlage beschaffen

Bedienen wir uns zunächst einer frei zugänglichen Repository-Version von einer hilfreichen
Python-Tool-Sammlung.
Klonen Sie folgendes Repository in Ihren [TERMREF::Hilfsbereich]:

```shell
git clone git@github.com:psf/requests.git --tag v2.32.2
```

### Tests ausführen - Teil 1

Sie wissen sicherlich bereits, dass wir mit `python -m pytest` oder einfach `pytest` alle
existierenden Pytest-Testfälle ausführen können.
Manchmal möchte man diese Ausführung erweitern, aber auch einschränken.
Wie wir das umsetzen können, lesen Sie bitte auf der offiziellen
[Pytest-Seite](https://docs.pytest.org/en/6.2.x/usage.html) nach.
Anschließend - gerne auch parallel dazu - erstellen Sie folgende Befehle und dokumentieren das
jeweilige Ergebnis.

Sollten Sie direkt schon einmal `pytest` ausgeführt haben, wird Ihnen mit hoher Wahrscheinlichkeit
der Testlauf nicht so gefallen.
Das Modul `requests` besitzt einige Abhängigkeiten, die ebenfalls installiert werden müssen.
Installieren Sie die Abhängigkeiten. Sollten Sie eine Auffrischung benötigen, besuchen Sie die Übung
[PARTREF::pip].

Wenn Sie Pytest anschließend erneut ohne weitere Informationen ausführen, sollte Ihnen direkt etwas
am Ergebnis aufgefallen sein.
Diesen Zustand werden wir im Folgenden manipulieren, dann wieder mit viel Gewissenhaftigkeit und
Fleiß herstellen.

#### Testgrundlage schaffen

Eine neue Version x.y.z wird in der Regel dann bereitgestellt, wenn diese Version auch aus Sicht der
Entwickler stabil ist.
Leider hilft uns eine stabile Version vorerst nicht weiter, weshalb wir ein klein wenig
nachhelfen müssen, um ein Problem zu erzeugen.
Um die Spannung nicht vorwegzunehmen, wurde diese Manipulation verschleiert.
Diese Art der Änderung nennt sich auch [TERMREF::Mutationstests].

Stellen Sie sicher, dass Sie sich im geklonten Unterverzeichnis `v2.32.2` des Verzeichnisses `requests`
befinden.
Bitte führen Sie folgenden Befehl aus:

```shell
echo "bXYgcmVxdWlyZW1lbnRzLWRldi50eHQgcmVxdWlyZW1lbnQtZGV2ZWxvcC50eHQ=" | base64 --decode | bash
```

### Tests ausführen - Teil 2

Ab jetzt sieht die Testausführung aus Teil 1 etwas anders aus, was von uns auch gewollt ist.

Sie, als Entwickler, haben einen Testfehlschlag als Antwort erhalten, diesen aber direkt gefixt -
so glauben Sie es zumindest.
Um das zu überprüfen, wollen Sie den Test erneut laufen lassen, aber dieses Mal die zuvor
fehlgeschlagene Testdatei.

[ER] Starten Sie den Test nur auf die fehlgeschlagenen Dateien.

Wenn sehr viele Testfälle im Spiel sind, könnten bestimmte Fehler auch Effekte auf andere Testfälle
haben.
In diesem Fall möchte man den Test nach einem Fehler gar nicht erst weiterlaufen lassen, sondern
abbrechen.

[ER] Lassen Sie den Testlauf beim Auftreten des _ersten_ Fehlers abbrechen.

Manchmal kann ein Fehlschlag auch nur durch eine zeitliche Abhängigkeit auftreten, wie zum Beispiel
beim Abfragen eines [TERMREF::TOTP], der beim Verwenden seine Gültigkeit verloren hat. In diesem
Fall bietet es sich an, einen Testfall erneut auszuführen.

[ER] Lassen Sie nur den letzten fehlgeschlagenen Testfall wiederholt durchführen.

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
