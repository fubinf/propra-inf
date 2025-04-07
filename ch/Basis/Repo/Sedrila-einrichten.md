title: "'sedrila'-Werkzeug zur Kursunterstützung einrichten"
stage: beta
timevalue: 0.5
difficulty: 2
requires: Zeiterfassung
---

[SECTION::goal::idea]
Ich kann `sedrila` aufrufen und habe meinen Übungspartner und mein Semester
für die Tutor\_innen festgehalten.
[ENDSECTION]

[SECTION::background::default]
Das Programmierpraktikum basiert auf der Anwendung `sedrila`
([Dokumentation](https://sedrila.readthedocs.io/en/latest/)).
sedrila dient Ihnen für zwei Zwecke:

1. Halbautomatische Erstellung einer einheitlichen Beschreibungsdatei `submission.yaml`
   für jede Abgabe, damit Ihre Tutor\_innen weniger
   Verwaltungsaufwand bei den Bewertungen haben und Ihnen damit
   schneller Rückmeldung geben können.
2. Überblick über Ihren Fortschritt bekommen.

Unterschätzen Sie diese Punkte nicht!
Die Erleichterung für die Tutoren vermeidet Missverständnisse und spart damit auch Ihnen Zeit.
Auch der Überblick kann schnell verloren gehen, insbesondere darüber, welche
Aufgaben bereits bearbeitet, aber noch nicht bewertet wurden.
[ENDSECTION]

[SECTION::instructions::detailed]

Zunächst müssen Sie `sedrila` installieren, davor seine Infrastruktur 
[`pipx`](https://pipx.pypa.io/) und
[`gnupg`](https://gnupg.org):

```
sudo apt install pipx gnupg
pipx install sedrila
```

In Ihrem ProPra-Verzeichnis (git-Arbeitsverzeichnis) führen Sie anschließend folgenden Befehl aus:

```
sedrila student --init
```

Sie werden aufgefordert, folgende Daten anzugeben, die Sie zuvor bereithalten sollten:

<replacement id="SedrilaEinrichtenPromptlist">
- die URL der Homepage des ProPras
- Ihren vollen Namen
- Ihre Matrikelnummer
- Ihren git-Benutzernamen (Accountnamen)
- git-Benutzernamen (Accountnamen) Ihrer Paar-Partner_in 
  (oder leer lassen, falls Sie allein arbeiten werden)
</replacement>

Diese Daten werden in einer Datei namens `student.yaml` festgehalten.
(Dort können Sie nötigenfalls mit einem Texteditor auch später Änderungen vornehmen
und in Git einchecken, wenn sich ausnahmsweise etwas ändern sollte.
Keinesfalls ändern sollten Sie hingegen den URL, jedenfalls sobald Sie erstmalig eine Aufgabe
erfolgreich bei der Tutor_in eingereicht haben, denn dadurch würde Ihr bis dahin angesammeltes
Stundenkonto ungültig.)

Sie sollten anschließend in der Lage sein, `sedrila student` auszuführen und
können dann in der webapp eine Tabelle mit den bisher bearbeiteten Aufgaben sehen.
Darin stehen zwei Sorten von Aufgaben:
Erstens die, die Sie schon mal eingereicht haben.
Zweitens die, für die Sie einen Commit, in dem Format gemacht haben,
das in [PARTREF::Zeiterfassung] beschrieben wurde.
Uneingereichtes ohne einen solchen Commit fehlt in der Tabelle, denn darüber kann sedrila nichts
Nützliches sagen. Holen Sie ggf. solche Commits wie dort beschrieben nach.

"Timevalue TOTAL" ist bislang 0, denn das umfasst nur bereits eingereichte und akzeptierte Abgaben.
Wie man Einreichungen macht, lernen Sie in der nächsten Aufgabe.

[ENDSECTION]

[SECTION::submission::snippet]
Die Abgabe besteht aus der von `sedrila student --init`
generierten Datei `student.yaml`.
[ENDSECTION]

[INSTRUCTOR::Kann man kaum falschmachen]
Wenn für diese Aufgabe eine Einreichung ankommt,
ist sie damit normalerweise automatisch auch akzeptabel.
Kuriose Ausnahmen sind natürlich denkbar.
[ENDINSTRUCTOR]
