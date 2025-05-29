title: Structured Query Language (SQL)
stage: draft
---
Sobald man bei der Verwaltung von Daten die ACID-Eigenschaften braucht,
ist fast immer ein relationales Datenbank-Managementsystem (RDBMS) das Mittel der Wahl.

ACID steht für _atomic, consistent, isolated, durable_ und bedeutet grob gesagt,
dass die Daten auch nach Programmende dauerhaft ("persistent", _durable_) gespeichert sein sollen,
dass Gruppen von Änderungen an den Daten ganz abgearbeitet werden müssen oder gar nicht (_atomic_),
dass das RDBMS gewisse (in einem Datenbankschema beschriebene) Eigenschaften der Daten und 
Beziehungen zwischen ihnen auch dann sicherstellen soll, 
wenn der Programmcode falsch ist und diese Eigenschaften verletzten würde (_consistent_) und
dass sogar mehrere Programme gleichzeitig Änderungen am selben Datenbestand machen können,
ohne das die obigen Eigenschaften verletzt werden (_isolated_).

SQL ist die Sprache, in der man in der Regel die Operationen ausdrückt, die ein RDBMS auf den
Daten vornehmen soll: Schema definieren, Daten zufügen, löschen, ändern, finden.

SQL gehört zu den Dauerbrennern unter den Programmiersprachen: 
es ist schon seit den 1970er Jahren für seinen Zweck führend.

SQL ist eine deklarative Sprache. Man beschreibt also, was getan werden soll, aber nicht
die Art und Weise, wie das passiert.
Das erlaubt dem RDBMS mehr Optimierungen, als bei einer prozeduralen Sprache möglich wäre.
