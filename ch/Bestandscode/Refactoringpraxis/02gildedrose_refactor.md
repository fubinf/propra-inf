title: "Gilded Rose: Struktur verbessern"
stage: alpha
timevalue: 1
difficulty: 3
assumes: Refactoring-Grundlagen
requires: 01gildedrose_tests
---
[SECTION::goal::experience]

- Ich kann Code refaktorieren, ohne die Funktionalität zu ändern.
- Ich kann Code refaktorieren, um die Wartbarkeit und das Verständnis des Codes zu verbessern.

[ENDSECTION]

[SECTION::instructions::loose]
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
[ENDSECTION]

[SECTION::submission::program]
Die Abgabe besteht aus dem refaktorierten Programm und einer Markdown-Datei mit der 
Beschreibung, welche Schritte Sie zur Refaktorierung angewandt haben.
[ENDSECTION]
    
[INSTRUCTOR::Tipps zur Korrektur]
Mit genügend Zeit und Aufwand lässt sich das Programm sehr stark kürzen und vereinfachen.
Wichtig ist hier, dass die Funktionstüchtigkeit des Programms weiterbesteht und die Regeln 
aus GildedRoseRequirements.txt eingehalten werden.
Wichtigster Punkt hierzu: Die Klasse `Item` darf **nicht** geändert werden.
[ENDINSTRUCTOR]