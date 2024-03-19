title: Fertige Aufgaben einreichen und angerechnet bekommen
stage: alpha
timevalue: 0.5
difficulty: 2
requires: SedrilaEinrichten
---
[SECTION::goal::idea]

Ich habe gelernt, wie ich etwas bei der Tutor_in einreiche und habe das einmal ausprobiert.

[ENDSECTION]

[SECTION::background::default]

Das ProPra ist eine ideale Gelegenheit, das ordentliche Arbeiten mit git zu lernen.

In der Softwareentwicklung hat es zahlreiche Vorteile, jeden logischen Arbeitsschritt
(nicht selten ist das eine Änderung an nur einer einzigen Zeile)
in einem separaten Commit zu verpacken.
Dann kann man mit solchen Arbeitsschritten anschließend nämlich sehr flexibel hantieren
und z.B. die gleiche Änderung (etwa eine Defektkorrektur) auf ältere Versionsstände
anwenden, die noch weitergepflegt werden. 
(Bitte vollziehen Sie diesen Gedanken unbedingt nach. 
Er hat in der modernen Softwareentwicklung eine erhebliche Bedeutung.)

Deshalb wollen wir uns eine solche Disziplin auch im ProPra angewöhnen:
Jede Aufgabe wird in einem separaten Commit (oder ggf. mehreren) eingecheckt,
niemals mehrere Aufgaben zugleich.
Dann kann man in der Commit-Nachricht die betreffende Aufgabe so markieren,
dass sich das automatisch verarbeiten lässt.

[ENDSECTION]

[SECTION::instructions::detailed]

### Übliches Abgabeformat

In der Zeiterfassungsaufgabe haben wir uns mit der Commit-Nachricht beschäftigt,
hier soll es um den Commit-Inhalt gehen.

Grundsätzlich liegt im Hauptverzeichnis Ihres Repos mindestens eine Datei pro
Aufgabe, manchmal auch ein Verzeichnis mit mehreren Dateien, die zu derselben
Aufgabe gehören.

Angenommen, es gibt eine (dort aber tatsächlich gar nicht geforderte) 
Markdown-Datei für die Aufgabe "Zeiterfassung"
sowie zwei (hier ebenfalls tatsächlich gar nicht geforderte)
Dateien `Script.py` und `Screenshot.png` für die aktuelle Aufgabe "Einreichungen", 
dann sieht Ihr Arbeitsverzeichnis vielleicht so aus:

```
Programmierpraktikum
├─README.md
├─Zeiterfassung.md
└─Einreichungen
  ├─Script.py
  └─Screenshot.png
```

### Datei-Basisnamen und -Namensendungen

Wir verwenden im gesamten Programmierpraktikum folgende Dateinamens-Konventionen
(bei einer Datei namens `hallo.xy` wird `hallo` _Basisname_ genannt und 
`xy` heißt _Endung_ oder _Suffix_):

- Die Datei-Basisnamen auf der oberen Verzeichnisebene heißen immer wie die jeweilige Aufgabe.
- Verzeichnisname auf der oberen Verzeichnisebene ebenfalls.
- Ein Verzeichnisname ist immer ohne Endung.
- Die Dateiendungen in Verzeichnissen können alles Mögliche sein, je nach Aufgabe.
- Die Dateiendungen auf der oberen Verzeichnisebene sind wie folgt:
    - Markdowndateien heißen `*.md`
    - Python-Quelltextdateien heißen `*.py`
    - Shellskripte heißen `*.sh`
    - Entsprechend auch für andere Programmiersprachen.
    - Kommandoprotokolldateien heißen `*.txt`


### Was gehört in welche Dateien?

Manchmal ist verbal beschrieben, was Sie in welchen Dateien abliefern sollen.
Manchmal (aber nur ab Schwierigkeitsgrad mittel) müssen Sie es selbst herausfinden.

Meistens ergibt es sich jedoch aus folgender Konvention: 

- Wenn Sie in der Anleitung Markierungen sehen wie [EQ], [EQ], [EQ],
  dann ist als Abgabe dazu eine Markdown-Datei gefragt und 
  Sie sollten darin die gleichen Markierungen für die zugehörigen Antworten verwenden.
- Wenn Sie in der Anleitung Markierungen sehen wie [EC], [EC], [EC],
  dann ist als Abgabe dazu ein Kommandoprotokoll gefragt.
- Wenn Sie in der Anleitung Markierungen sehen wie [ER], [ER], [ER],
  dann gehört das zugehörige Arbeitsergebnis in Quellcodedateien.

Machen Sie sich keine Sorgen, falls Sie Markdown nicht beherrschen. 
Sie dürfen ersatzweise auch unformatierten Text abgeben.
Schreiben Sie dann zu jeder Antwort einen Absatz.


### Commits nachholen

Prüfen Sie ihre Commits zu den vorherigen Aufgaben.
Benennen Sie falsch benannte Dateien um 
und checken Sie sie (ohne Zeiterfassungs-Eintrag) erneut ein.
Holen Sie ggf. fehlende Commits nach.


### Abgaben (Einreichungen) machen

Nachdem Sie einige Commits zu vorherigen Aufgaben erstellt haben, können Sie
in Ihrem Arbeitsverzeichnis folgenden Befehl ausführen:

```
sedrila student --submission
```

Sie bekommen dann eine Liste mit Aufgaben, zu denen Sie Commits angelegt
haben, zusammen mit der entsprechenden aufsummierten aufgewendeten Zeit.
Sie können darin auswählen, welche Aufgaben zur Kontrolle vorgelegt werden
sollen. Daraus wird eine Datei submission.yaml erzeugt und Ihnen weitere
Anweisungen gegeben.

Da hier nichts weiter zu tun ist, Sie aber trotzdem Zeit gutgeschrieben haben
wollen, können Sie ausnahmsweise einen Zeiterfassungscommit ohne Inhalt machen.
Hierfür verwendet man `git commit --allow-empty`.

Vergessen Sie nicht, Ihren Stand mittels `git push` verfügbar zu machen!
[ENDSECTION]

[SECTION::submission::snippet]
Die Abgabe besteht entgegen dem üblichen Format diesmal nur aus dem leeren Commit.

Zeigen Sie nun Ihre bisherigen Ergebnisse bei der Tutor_in vor wie vom Kommando
`sedrila student --submission` beschrieben.

Die Email dient dabei nur zum Übermitteln der Zugangsdaten,
für die Abnahme müssen Sie persönlich hingehen, damit die Tutor_in
Ihnen mündlich Rückmeldung geben kann.
[ENDSECTION]
