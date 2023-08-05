title: Gilded Rose 01 - Fixieren von Funktionalität
description: |
  Üben Sie hier das Erkunden von Legacy Code und Fixieren von Funktionalität mittels Test
timevalue: 1
difficulty: 3
assumes: refactoring
---
!!! goal
    Wenn Sie mitten im Lebenszyklus einer Software zu einem Projekt hinzustoßen, müssen Sie mit 
    Code umgehen, der zwar funktioniert, aber möglicherweise schlecht wartbar oder erweiterbar
    ist.
    Üben Sie hier die Funktionalität des Programms mittels Tests zu fixieren.

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

Die geforderte Implementierung der Regeln für "Conjured Items" ist hier noch nicht gefragt. 

!!! submission
    Beschreiben Sie kurz ihren Testentwurf für das Programm und beschreiben Sie, welche Fälle 
    sie gewählt haben und warum.
    Die Abgabe kann entweder aus dem kommentierten Testskript bestehen oder aus einer separaten 
    Markdown-Datei, die ihr Testskript beschreibt.

!!! instructor
    Anhand des Testentwurfs kann darüber geurteilt werden, wie gut das Programm verstanden 
    worden ist.
    Eine mögliche Herangehensweise ist es die Tests kategorisiert nach der Handhabung der 
    Qualitätsänderung zu gestalten. 
    So sollten bis zu 15 Tests entstehen.