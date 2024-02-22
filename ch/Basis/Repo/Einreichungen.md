title: Fertige Aufgaben einreichen und angerechnet bekommen
stage: draft
timevalue: 0.5
difficulty: 2
requires: Sedrila einrichten
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

## Übliches Abgabeformat

In der Zeiterfassungsaufgabe haben wir uns mit der Commit-Nachricht beschäftigt,
hier soll es um den Commit-Inhalt gehen.

Grundsätzlich liegt im Hauptverzeichnis eures Repos idealerweise eine Datei pro
Aufgabe oder alternativ ein Verzeichnis bei mehreren Dateien, die zu derselben
Aufgabe gehören.

Angenommen, es gibt eine (nicht geforderte) Datei für die Aufgabe "Zeiterfassung"
sowie zwei Dateien --- `Script.py` und `Screenshot.png` --- für diese Aufgabe, dann
sieht das Verzeichnis etwa so aus:

```
Programmierpraktikum
├─README.md
├─Zeiterfassung.md
└─Einreichung
  ├─Script.py
  └─Screenshot.png
```

Die Endung der Einzeldateien ist hierbei unerheblich und richtet sich nach der
geforderten Abgabeform. Für Code wird die Endung beispielsweise eher .py sein,
während sie für Text wie eine Reflexion eher .md (Markdown) sein wird.

Machen Sie sich keine Sorgen, falls Sie Markdown nicht beherrschen. Es ist
völlig in Ordnung, einfach unformatierten Text abzugeben. Bemühen Sie sich
bitte dennoch um eine sinnvolle Struktur mit Einrückung und Absätzen.

[SECTION::instructions::detailed]
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

Vergessen Sie nicht, Ihren Stand mittels `git push` auch verfügbar zu machen!
[ENDSECTION]
[SECTION::submission::snippet]
Die Abgabe besteht entgegen dem Format diesmal nur aus dem leeren Commit.

Sie sind allerdings dazu angehalten, auch schon eine submission-Datei zu
erzeugen und zur Bewertung abzugeben! Es ist wichtig, sich der korrekten
Verwdendung dieses Ablaufs zu versichern.
[ENDSECTION]
