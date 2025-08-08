title: "My Little Helpers: linkcheck --- Check hyperlinks on HTML pages"
stage: beta 
timevalue: 0.5
difficulty: 3
requires: mlh-lsnew, linkcheck-fullscreen
---

[SECTION::goal::product,experience]
Ich integriere ein Unterkommando, das _nicht_ von vornherein dafür geschrieben war.
[ENDSECTION]


[SECTION::background::default]
Der Linkprüfer aus Aufgabengruppe [PARTREF::Python-linkcheck] wird viel praktischer,
wenn wir ihn in unsere `mlh`-Werkzeugsammlung eingliedern!
[ENDSECTION]


[SECTION::instructions::loose]

### Vorarbeiten

Diese Aufgabe geht nur, wenn Sie (siehe `requires`)
die Linkcheck-Aufgaben mindestens bis [PARTREF::linkcheck-fullscreen] bearbeitet 
und vorgelegt haben.

Aber wenn Sie von den dort nachfolgenden Schritten auch noch weitere bearbeiten wollen,
sollten Sie das **zuerst** tun, und erst danach mit der hiesigen Aufgabe fortfahren.


### Aufgabe

Machen Sie eine Kopie der Datei `linkcheck.py` in ihren `mlh`-Dateibaum.

Gliedern Sie den Linkprüfer als Unterkommando `linkcheck` analog zu den übrigen
Unterkommandos in `mlh` ein.

Übernehmen Sie nun auch die Testinfrastruktur (`linkcheck_server.py` und `test_linkcheck.py`)
sinnvoll in den `mlh`-Dateibaum.

[EC] Lassen Sie den Test laufen

[EC] Lassen Sie manuell den Linkprüfer für den Testserver laufen

[EQ] Was haben Sie hier ggf. darüber gelernt, wie man beim Programmieren für spätere Um-Verwendung vorplanen sollte?


[SECTION::submission::trace,reflection,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Test reicht]
Wenn die Ausgaben der beiden Kommandos im Kommandoprotokoll richtig aussehen,
sind wir schon zufrieden.

Wer Lust hat, kann noch kurz die Reflektion in der Markdowndatei ansehen und 
ggf. aus der eigenen Erfahrung heraus kommentieren.
<!-- TODO_2: Musterlösung (Kommandoprotokoll, Quellcode, Markdown für mlh-linkcheck ergänzen -->
[ENDINSTRUCTOR]
