title: "Gilded Rose(3): Implementierung der Kundenanforderung"
stage: beta
timevalue: 0.5
difficulty: 3
requires: gildedrose_refactor
---
[SECTION::goal::experience]

Ich kann neue Funktionalität in Code einbauen, ohne die vorhandene Funktionalität zu beschädigen.

[ENDSECTION]
[SECTION::instructions::loose]

Nachdem Sie in [PARTREF::gildedrose_tests] schon ein ausführliches Testskript geschrieben 
haben und in [PARTREF::gildedrose_refactor] den Code in zwei Varianten refaktoriert haben,
müssen Sie jetzt in **beiden** Varianten die Funktionalität für die "Conjured items" 
implementieren. 
Zur Erinnerung ist hier noch einmal die [Requirements Specification](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md).  
Beginnen Sie mit Variante 1.

- Schreiben Sie in der Datei `test_gilded_rose.py` einen oder mehrere aussagekräftige Test(s), die 
  die Eigenschaften "Conjured items" beschreiben.
- [EQ] Wie viele Testfälle sind Ihrer Meinung nach nötig, um die "Conjured items" voll 
  abzudecken? Begründen Sie. 
- [EC] Lassen Sie die Testfälle laufen und überzeugen Sie sich, dass alle Testfälle **außer** den 
  Testfällen zu den "Conjured items" erfolgreich sind.
- Machen Sie einen Commit mit Ihren Ergänzungen.
- [EC] `git -P show HEAD`
- [ER] Implementieren Sie in `gilded_rose.py` die Handhabung der "Conjured items".  
  Beachten Sie dabei, dass Sie die Struktur des Codes nicht mehr ändern müssen.
- [EC] Lassen Sie die Testfälle laufen und überzeugen Sie sich, dass alle Tests erfolgreich sind.
- Machen Sie einen Commit mit Ihren Ergänzungen.
- [EC] `git -P show HEAD`

Und nun das Gleiche nochmals für Variante 2: [EC], [EC], [ER], [EC], [EC].

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Verschiedene Implementierungen]

- Durch die aus der vorherigen Aufgabe vorgegebenen Programmstrukturen sind die 
  Implementierungswege ohne viel Varianz vorgegeben.
- Die Implementierungen sind in jeweils 2-8 Zeilen Code machbar. 
  Wer deutlich mehr Code schreibt, sollte ermahnt werden; 
  wahrscheinlich wird die eingeführte Struktur verletzt.
- Eine Implementierung ohne vorherigen Test soll zurückgewiesen werden.
- Eine Implementierung mit fehlschlagenden Tests soll zurückgewiesen werden.

[ENDINSTRUCTOR]