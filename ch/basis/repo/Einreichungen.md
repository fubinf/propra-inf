title: Wie man fertige Aufgaben einreicht und angerechnet bekommt
description: |
  Wir legen die Beschreibungsdatei an, legen das Repo der Tutori\_in vor
  und schauen uns anschließend die Ergebnisse an.
timevalue: 1.0
difficulty: 1
requires: Zeiterfassung
---
Zu jeder Aufgabe ist mindestens ein Commit anzufertigen. Commits über mehrere Aufgaben hinweg
sind zu vermeiden, mehrere Commits zu einer Aufgabe sind akzeptiert und sinnvoll. Es mag auch
Aufgaben geben, in denen mehrere Commits _notwendig_ sind.

Zu einer Aufgabe sollte die Abgabe entweder vollumfänglich in einer Markdown-Datei mit Namen
der Aufgabe stehen oder komplett in einem Verzeichnis liegen, das gleichnamig zur Aufgabe ist.
Um Unklarheiten vorzubeugen, haben Aufgaben oft eine Box, die möglichst genau beschreibt,
was in der Abgabe einer Aufgabe erwartet wird.

Zur Anrechnung von erledigten Aufgaben kann mit sedrila eine Liste aller Aufgaben erzeugt
werden, für die bereits Commits vorliegen, aber noch keine Anrechnung vorliegt. Aus dieser
Liste können dann Einträge entfernt werden, die noch nicht kontrolliert werden sollen, weil
sie beispielsweise noch nicht vollständig bearbeitet sind.

Diese angepasste Liste wird dann in einem eigenen Commit zum Repository hinzugefügt.
Anschließend wird der/die Tutor\_in mit der URL des Repos darüber informiert, dass Aufgaben
zur Kontrolle vorliegen. Dieser trägt Feedback in diese Datei ein und markiert akzeptierte
Aufgaben. Das wird als **signierter** Commit in das Repository hinzugefügt. Für die
Abschlussbewertung zählen ausschließlich diese Commits.
<!-- Es gab hier mal die Idee, auch nicht angesehene Aufgaben zu bewerten.
Grundlegend gar keine schlechte Idee, aber ich würde das vermutlich einfach derart
handhaben, dass Tutor\_innen einfach 3 Feedback-Möglichkeiten haben.
Sowas wie "fehlerhaft", "okay" und "akzeptiert" oder sowas.
Ich sehe allerdings ein Problem darin, dass ohne klare Ansage, wann das gestattet ist und
in welchem Umfang, die Tutoren eher ein "Okay" geben würde, ohne die Aufgabe zu prüfen. -->

Sedrila kann dann den Kontostand auf Studierendenseite aktualisieren.

[TOC]

!!! instructor 
    Wenn eine wohlgeformte und sinnvolle `submission.yaml` im commit liegt, sind wir schon zufrieden.
