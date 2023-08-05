title: Gilded Rose 02 - Refactoring von Legacy Code
description: |
  Üben Sie hier das Refaktorieren von Programmen
timevalue: 1
difficulty: 3
requires: 01gildedrose_tests
---
!!! goal
    Beim Refactoring von Legacy Code kann es sein, dass Sie nur begrenzte Möglichkeiten zur 
    Änderung des Codes haben.
    Ziel dieser Aufgabe ist es den vorhandenen Code soweit zu refaktorieren, dass er 
    sowohl einfacher zu warten, als auch einfacher zu erweitern ist.

Beim Betrachten des Codes des [Gilded Rose-Kata](https://github.
com/emilybache/GildedRose-Refactoring-Kata/tree/main) sollte Ihnen auffallen, dass die benutzte 
Logik viel Komplexität in Anspruch nimmt.
Setzen Sie sich mit dem Code auseinander und refaktorieren Sie das Programm.
Beachten Sie dabei, welche Änderungen Sie laut der GildedRoseRequirements.txt durchführen dürfen 
und welche nicht.
Nutzen Sie ihre in der vorherigen Aufgabe geschriebenen Tests um sicherzustellen, dass das 
Programm weiterhin funktioniert.

[HINT::Tipps, wenn Sie auf dem Schlauch stehen]
  Achten Sie auf Logik, die sich häufig wiederholt: Lässt sie sich anders formulieren und so kürzen?
  Erinnern Sie sich an die de-morganschen Regeln, wenn Sie sich die Logik anschauen.
  Sie dürfen weitere Funktionen schreiben, wenn es hilfreich ist und diese benutzen.
[ENDHINT]

!!! submission
    Die Abgabe besteht aus dem refaktorierten Programm und einer Beschreibung, welche Schritte 
    Sie zur Refaktorierung angewandt haben.
    
!!! instructor
    Mit genügend Zeit und Aufwand lässt sich das Programm sehr stark kürzen und vereinfachen.
    Wichtig ist hier, dass die Funktionstüchtigkeit des Programms weiterbesteht und die Regeln 
    aus GildedRoseRequirements.txt eingehalten werden.
    Wichtigster Punkt hierzu: Die Klasse `Item` darf **nicht** geändert werden.