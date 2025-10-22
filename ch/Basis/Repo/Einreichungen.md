title: Fertige Aufgaben einreichen und angerechnet bekommen
stage: beta
timevalue: 0.5
difficulty: 2
assumes: Markdown
requires: Sedrila-einrichten
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
dass sich das automatisch verarbeiten lässt -- und das macht `sedrila` sich zunutze.

[ENDSECTION]

[SECTION::instructions::loose]

### Übliches Abgabeformat

In der Zeiterfassungsaufgabe haben wir uns mit der Commit-Nachricht beschäftigt,
hier soll es um den Commit-Inhalt gehen.

Grundsätzlich liegen Ihre Dateien fast immer in einem Pfad,
der dem Pfad der Aufgabe im ProPra-Website-Inhaltsverzeichnis entspricht.
Das Verzeichnis für die Aufgabe selbst kann man je nach Geschmack auch einsparen, 
wenn alle abzugebenden Dateien Namen haben, die mit dem Aufgabennamen anfangen.
(Das müssen dann allerdings beide Mitglieder jedes gemeinsam abgebenden Paars überall
gleich handhaben!)

Beispiel:
Angenommen, es gäbe eine (dort aber tatsächlich gar nicht geforderte) 
Markdown-Datei für die Aufgabe "Zeiterfassung"
sowie zwei (hier ebenfalls tatsächlich gar nicht geforderte)
Dateien `Script.py` und `Bild.png` für die aktuelle Aufgabe "Einreichungen", 
dann sähe Ihr Arbeitsverzeichnis vielleicht so aus:

```
Programmierpraktikum
├─README.md
└─Basis
  └─Repo
    ├─Zeiterfassung.md
    └─Einreichungen
      ├─Bild.png
      └─Script.py
```
Als flache Dateiliste und alphabetisch sortiert sieht das Gleiche also so aus:

```
Programmierpraktikum/Basis/Repo/Einreichungen/Bild.png
Programmierpraktikum/Basis/Repo/Einreichungen/Script.py
Programmierpraktikum/Basis/Repo/Zeiterfassung.md
Programmierpraktikum/README.md
```

Die einzelnen Abgabedateien haben im Normalfall entweder den Aufgabennamen als Basisname oder Namenspräfix
oder sie liegen in einem Verzeichnis, das wie die Aufgabe heißt.

Genauer gesagt, ist es so:


### Datei-Basisnamen und -Namensendungen

Wir verwenden im gesamten Programmierpraktikum folgende Dateinamens-Konventionen
(bei einer Datei namens `hallo.xy` wird `hallo` _Basisname_ genannt und 
`xy` heißt _Endung_ oder _Suffix_):

- Ein Verzeichnisname hat in der Regel keine Endung.
- Die Dateiendungen in Verzeichnissen können alles Mögliche sein, je nach Aufgabe.
- Die Dateiendungen sind wie folgt:
    - Markdowndateien heißen `*.md`
    - Python-Quelltextdateien heißen `*.py`
    - Shellskripte heißen `*.sh`
    - Entsprechend auch für andere Programmiersprachen.
    - Kommandoprotokolldateien heißen `*.prot`


### Was gehört in welche Dateien?

Manchmal ist verbal beschrieben, was Sie in welchen Dateien abliefern sollen.
Manchmal (aber nur ab Schwierigkeitsgrad mittel) müssen Sie es teilweise selbst herausfinden.

Meistens ergibt es sich jedoch aus folgender Konvention: 

- Wenn Sie in der Anleitung Markierungen sehen wie [EQ], [EQ], [EQ],
  dann ist als Abgabe dazu eine [PARTREF::Markdown]-Datei gefragt und 
  Sie sollten darin die gleichen Markierungen (nur ohne Farbe) für die zugehörigen Antworten 
  verwenden (und genug von der Frage wiederholen, das Ihre Tutor_in sich schnell zurecht findet).
- Wenn Sie in der Anleitung Markierungen sehen wie [EC], [EC], [EC],
  dann ist als Abgabe dazu ein Kommandoprotokoll gefragt.
- Wenn Sie in der Anleitung Markierungen sehen wie [ER], [ER], [ER],
  dann gehört das zugehörige Arbeitsergebnis in Quellcodedateien.
- **F** steht für Frage, **K** für Kommando und **A** für Anforderung.


### Dateien außerhalb des üblichen Verzeichnisses

Bei manchen Aufgaben kommt es vor, dass mehrere verschiedene Aufgaben an denselben Dateien 
oder jedenfalls in einem gemeinsamen Dateibaum arbeiten, sodass der Pfad
`Programmierpraktikum/Kapitelname/Gruppenname/Aufgabenname/*` nicht immer funktionieren kann.
Damit das `sedrila`-Werkzeug auch in diesem Fall die Tutor_in gut dabei unterstützen kann,
alle relevanten Dateien zügig zu sichten, müssen Sie in diesem Fall eine Dateilisten-Datei
abgeben, die diese Dateien aufführt. Wie sieht das aus?
Dateilisten-Dateien sind Textdateien, haben einen Namen der Form `*.files` und 
enthalten einen relativen Pfadnamen pro Zeile.

Beispiel:
Angenommen, die Dateien
```
Programmierpraktikum/Basis/Repo/Task99/Bild.png
Programmierpraktikum/Basis/Repo/Task99/Script.py
```
sind auch noch für Aufgaben aus anderen Gruppen oder sogar anderen Kapiteln relevant.
Dann schreibt die Aufgabe `Task99` vielleicht vor:
_"Packen Sie die Dateien in den Pfad `MitBild` auf oberster Ebene"_
und Sie machen nach dieser Anweisung automatisch eine Abgabedatei
```
Programmierpraktikum/Basis/Repo/Task99.files
```
in der steht
```
../../MitBild/Bild.png
../../MitBild/Script.py
```
Warum diese Pfade?
Weil die Angaben relativ zu dem Ort sind, an dem die Listendatei liegt, also `Repo`.
Von dort aus muss man zwei Ebenen aufsteigen, damit `MitBild` dort ein Unterverzeichnis ist.


### Commits nachholen

Prüfen Sie ihre Commits zu den vorherigen Aufgaben.

- Benennen Sie ggf. unpassend benannte Dateien um 
  und checken Sie sie (_ohne_ Zeiterfassungs-Eintrag) erneut ein.
- Holen Sie ggf. fehlende Commits nach.
- Falls [PARTREFMANUAL::Zeiterfassung::Zeiterfassungs-Einträge] fehlen, holen Sie diese 
  mit geschätzten Zeiten ebenfalls nach.


### Abgaben (Einreichungen) machen

Nachdem Sie einige Commits zu vorherigen Aufgaben erstellt haben, können Sie
in Ihrem Arbeitsverzeichnis folgenden Befehl ausführen:

```
sedrila student
```

Mit 'w' ("webapp") können Sie im Webbrowser auswählen, welche Aufgaben eingereicht
werden sollen (und welche vielleicht lieber noch nicht).

Haben Sie das Format der [PARTREF::Zeiterfassung] nicht eingehalten, müssen Sie `submission.yaml` von Hand
anlegen. Die Datei besteht aus Zeilen der Form  
`taskname: CHECK`  
also beispielsweise  
```
Zeiterfassung: CHECK
Einreichungen: CHECK
```
Mit c ("commit") checken Sie die so entstandene `submission.yaml` mit der genau passenden
Commit-Nachricht ein;
mit p ("push") geben Sie diesen Commit frei.
Abschließend zeigt das Kommando an, wie es weitergeht: Email an eine Tutor_in.

Da bei der hiesigen Aufgabe nichts weiter zu tun ist, 
Sie aber trotzdem Zeit gutgeschrieben bekommen sollen, 
können Sie ausnahmsweise einen [PARTREFMANUAL::Zeiterfassung::Zeiterfassungscommit] ohne Inhalt machen.
Hierfür verwendet man `git commit --allow-empty -m"..."`.

Vergessen Sie nicht, Ihren Stand mittels `git push` verfügbar zu machen!
[ENDSECTION]

[SECTION::submission::snippet]
Die Abgabe besteht entgegen dem üblichen Format diesmal nur aus dem leeren Commit.

Zeigen Sie nun Ihre bisherigen Ergebnisse bei der Tutor_in vor wie im Schritt 'push' von Kommando
`sedrila student` beschrieben.

Die Email dient dabei nur zum Übermitteln der Zugangsdaten,
für die Abnahme gelten die Verfahrensweisen, die die 
Veranstalter_innen dafür bekannt gegeben haben.

[WARNING]
Bedenken Sie gegen Ende des Kurszeitraums, dass Sie vor Ihrer nächsten Abgabe zuerst
die Rückmeldung zur vorherigen abwarten müssen.
Achten Sie darauf, dass bis zum Schlusstermin genügend Luft bleibt, um auch Ihre letzte
Abgabe sauber abwickeln zu können!
[ENDWARNING]
[ENDSECTION]

[INSTRUCTOR::Nichts zu prüfen]
Wer geschafft hat, eine sinnvolle `submission.yaml` einzureichen, 
hat diese Aufgabe schon erledigt.
[ENDINSTRUCTOR]