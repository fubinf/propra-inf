# Aufgabenideen

## Aufgabenbereich Basis

- Ist schon geklärt, wie das ganze Projekt bootstrapped wird?
- Hat jemand den vollständigen Weg für ein System einmal durchgespielt?
  Wenn es hier scheitert, ist die Frustrationsgrenze schnell erreicht.
- 

## Aufgabenbereich Programmiersprache

- WebAPIs-Aufgabe um GraphQL erweitern oder dazu eine separate Aufgabe gestalten?

## Aufgabenbereich Bibliotheken

- Rechercheaufgabe: Bibliothek für bestimmten Zweck suchen
  - Wo findet man Bibliotheken?
  - Nach welchen Merkmalen wählt man eine Bibliothek aus?

## Aufgabenbereich Testen

- Vorgegebene Testklasse einfach ausführen
- Tests korrigieren
- Test-Coverage bestimmen?
- SetUp und TearDown bei repetitiven Tests oder teurem Setup
- Wie groß ist ein Test/eine Testklasse?

## Aufgabenbereich Bestandscode

- ...

## Aufgabenbereich Werkzeuge

Hier muss explizit mehr vermittelt werden, als im Grundlagenbereich.

### Terminal-Tools

- bash
  - Bash Scripting?
  - Loops?
  - Warum sieht so ein Skript gruselig aus? Andere Mittel führen lesbarer zum Ziel.
- Git
  - Logs
  - Merge vs Rebase
  - Ein Repo, mehrere Origins
  - Signing
  - Squashing
  - bisect
  - cherry-pick
- ssh
- grep, awk, sed
  - Was kann grep? awk? sed? Wahrscheinlich unnötig separate Aufgaben zu gestalten.
  - Wie verbindet man die Funktionalitäten der Tools?
- Alternative Shells
  - Schmökeraufgabe, dürfte nicht mehr als eine Aufgabe sein. zsh existiert und ist super 
    anpassbar, ksh "existiert", fish bietet Sane Scripting. Wenn bash Programmierungsaufgaben 
    existieren, lassen sich diese hier in fish nachimplementieren.


### Außerhalb des Terminals

- RegEx
- IDE
  - Unterschied IDE und Editor
  - Projekterstellung
  - Code-Ausführung in der IDE
  - Debugging
  - Refactoring
  - git-Integration
  - Integriertes Terminal
- Paketmanager
  - Welche stehen in meiner Sprache zur Verfügung? Gibt es überhaupt welche?
  - Welche Funktionen bietet ein Paketmanager?
  - Wie finde ich Pakete?
  - Fallbeispiel über Probleme mit Paketmanagern
    - Eine der unzähligen Probleme mit npm heraussuchen, vielleicht mit einem Post Mortem. 
      Aufgabe ist es herauszuarbeiten, was das Problem genau ist, ob es dauerhaft gefixt ist 
      oder ob es überhaupt fixbar ist. 
      Nicht als Draufprügeln für npm, sondern für das Verstehen, dass die Nutzung von Fremdcode 
      unter der Hand explodieren kann. 
- Arbeitsplatzergonomie
  - _Persönlich_ finde ich wichtig, dass die Studierenden nicht nur ihre Arbeitsumgebung im PC, 
    sondern auch um ihren PC herum einrichten können.
    Meistens denkt man da erst dran, wenn es zu spät ist.
    Maximal eine Aufgabe, darf nicht zu viel Platz beanspruchen.
- Postman
  - APIs testen und planen, relevant fürs Debugging und Bauen eigener APIs. 
    Gehört ins Portfolio des Profils "Webentwickler". In Kombination mit WebAPIs-Aufgabe möglich.
- docker
  - Wenn es Aufgaben zu docker gibt, dann erst sehr spät.

## Aufgabenideen ohne Heimat

- Lektion: Kämpfe nicht gegen den Compiler an.
  - Sucht nach einer Umsetzung. 
    Eine eigene Implementierung vs eine Implementierung der Standardbibliothek zu dekompilieren 
    führt nicht zum Ziel, Python optimiert recht wenig. 
