title: Wie man fertige Aufgaben einreicht und angerechnet bekommt
description: |
  Wir legen die Beschreibungsdatei an, legen das Repo der Tutor_in vor
  und schauen uns anschließend die Ergebnisse an.
timevalue: 1.0
difficulty: 1
requires: Zeiterfassung
---
---
[TOC]

TODO 2: einreichungen.md

Grob gesagt:

- sedrila erzeugt Einreichungsdatei `submission.yaml` mit einem Eintrag für jede Aufgabe, 
  zu der es Commits gibt, die aber noch nicht angerechnet ist.
- Studi löscht Einträge, die ersie noch nicht einreichen will (z.B. weil unfertig).
- commit, push
- Tutor_in per Email verständigen und Repo-URL angeben.
- Tutor_in prüft, erklärt ggf. gefundene Probleme mündlich, trägt Stichwörter dazu in
  `submission.yaml` ein, trägt OKs für akzeptierte Aufgaben in `submission.yaml` ein.
- Wenn alle geprüften Aufgaben akzeptiert wurden, werden die restlichen ungeprüften
  ebenfalls mit angerechnet.
  Andernfalls werden nur die akzeptierten Aufgaben angerechnet;
  die abgelehnten gelten als einmal abgelehnt; 
  die ungeprüften gelten als diesmal nicht vorgelegt.
- Tutorin checkt `submission.yaml` ein (signierter Commit) und pusht.
- Studi pullt, schaut `submission.yaml` an, um die Probleme zu analysieren,
  und ruft evtl. sedrila, um den Kontostand auszurechnen.

!!! instructor 
    Wenn eine wohlgeformte und sinnvolle `submission.yaml` im commit liegt, sind wir schon zufrieden.
---
---
---
---
