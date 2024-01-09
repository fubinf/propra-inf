title: Gilded Rose 01 - Fixieren von Funktionalität
stage: alpha
timevalue: 1
difficulty: 3
profiles:
assumes: refactoring
requires:
---
[SECTION::goal::experience]

- Ich kann Funktionalität auf bestimmte Code-Bereiche zurückführen.
- Ich kann Code, den ich refaktorieren möchte, mittels Tests fixieren.

[ENDSECTION]

[SECTION::instructions::loose]
Das [Gilded Rose-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main) ist 
eine Aufgabe, bei der Ihnen ein funktionierender Code gegeben wird mit der Bitte eine 
Anforderungsspezifikation zu erfüllen.  
Diese Spezifikation beinhaltet zum einen die Beschreibung des funktionierenden Codes, aber auch 
die Beschreibung von gewünschter Funktionalität. 
Lesen Sie sich die Aufgabe genau durch und wählen Sie eine Programmiersprache, in der Sie die 
Aufgabe bewältigen wollen.
Der Einfachheit halber ist das Kata im Programmierpraktikum in mehrere Aufgaben aufgeteilt.
Schreiben Sie in dieser Aufgabe die Tests, die alle aktuellen Funktionen des Programms fixieren.
Auch wenn die Quelle z. B. bei der Nutzung von Python vom Testframework `unittest` ausgeht, ist 
Ihnen die Wahl des Testframeworks überlassen.
Wenn Sie hierzu Unterstützung benötigen, finden Sie in der Aufgabengruppe [PARTREFTITLE::testframeworks]
weitere Informationen.

Die geforderte Implementierung der Regeln für "Conjured Items" ist hier noch nicht gefragt. 
[ENDSECTION]

[SECTION::submission::program]
Die Abgabe besteht aus dem kommentierten Testskript.
Beschreiben Sie zu jedem Test (oder jeder Testklasse), welche Fälle abgedeckt werden und warum.
[ENDSECTION]

[INSTRUCTOR::Testentwurf]
Anhand des Testentwurfs kann darüber geurteilt werden, wie gut das Programm verstanden 
worden ist.
Eine mögliche Herangehensweise ist es die Tests kategorisiert nach der Handhabung der 
Qualitätsänderung zu gestalten. 
So sollten bis zu 15 Tests entstehen.
[ENDINSTRUCTOR]