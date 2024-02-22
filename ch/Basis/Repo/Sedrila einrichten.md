title: SeDriLa lauffähig machen für die Verwendung der Teilnehmer
stage: draft
timevalue: 0.25
difficulty: 2
requires: Zeiterfassung
---
[SECTION::goal::idea]
Ich kann `sedrila` aufrufen und habe meinen Übungspartner und mein Semester
für die Tutor\_innen festgehalten.
[ENDSECTION]
[SECTION::background::default]
Das Programmierpraktikum basiert auf der Anwendung SeDriLa (Self-Driven Lab).
Das dient Ihnen grundlegend für folgende Dinge:

1. Einhaltung einer einheitliche Abgabeform, damit Ihre Tutor\_innen weniger
   unnötigen Verwaltungsaufwand bei der Bewertungen haben und Ihnen damit
   schneller Rückmeldung geben können.
2. Einen Überblick über den eigenen Fortschritt schaffen.

Unterschätzen Sie diese Punkte nicht! Zur Verwaltung zählt beispielsweise
auch, die Zuordnung des Übungspartners und des Semesters festzuhalten. Das
gewährt Ihnen grundsätzlich die Freiheit, das Modul in ihrem eigenen Tempo
zu einer späteren Zeit abzuschließen als das Semester, in dem Sie begonnen
haben.

Auch der Überblick kann schnell verloren gehen, insbesondere darüber, welche
Aufgaben bereits bearbeitet, aber noch nicht bewertet oder gar abgelehnt
wurden.
[ENDSECTION]
[SECTION::instructions::detailed]

Zunächst müssen Sie SeDriLa installieren. Führen Sie hierzu folgenden Befehl aus:

```
pip install sedrila
```

In Ihrem ProPra-Verzeichnis führen Sie anschließend folgenden Befehl aus:

```
sedrila student --init
```

Sie werden aufgefordert, die URL dieses Kurses anzugeben, zusammen mit einigen
Daten über sich und ihren Übungspartner.
Diese Daten werden in einer Datei namens student.yaml festgehalten.

Sie sollten anschließend in der Lage sein, `sedrila student` auszuführen und
eine Tabelle mit den bisher bearbeiteten Aufgaben sehen. Diese kann noch
leer sein. In diesem Fall erstellen Sie Commits ihrer bisher bearbeiteten
Aufgaben (einschließlich dieser hier) in dem Format, das in
[PARTREF::Zeiterfassung] beschrieben wurde.

Lassen Sie sich nicht von dem Timevalue TOTAL abschrecken. Das beinhaltet nur
bereits akzeptierte Abgaben und entspricht daher nicht der geleisteten Arbeit.

[ENDSECTION]
[SECTION::submission::snippet]
Die Abgabe besteht aus der generierten Datei student.yaml.
[ENDSECTION]
