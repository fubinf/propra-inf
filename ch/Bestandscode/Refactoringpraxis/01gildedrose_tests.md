title: "Gilded Rose: Festhalten der Funktionalität"
stage: alpha
timevalue: 1
difficulty: 3
assumes: unittest101, pytest104
---
[SECTION::goal::experience]
Ich kann mich für Code, den ich refaktorieren möchte, dagegen versichern,
das Verhalten versehentlich zu ändern.
[ENDSECTION]

[SECTION::background::default]
"Gilded Rose" ist eine tolle Übungsaufgabe für den Umgang mit Bestandscode:
Obwohl das Programm winzig klein ist (und die Übungen deshalb kurz), kann man
alle wichtigen Teilaufgaben daran üben.

In dieser Aufgabe machen wir die erste, nachfolgende bauen darauf auf.
[ENDSECTION]


[SECTION::instructions::loose]
- Einlesen in die Domäne:
  Lesen Sie grob die Anforderungsbeschreibung (nur lesen, noch nichts machen) von
  "Gilded Rose": 
  [Requirements Specification](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md).  
  (Es gibt auch eine 
  [deutsche Fassung](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements_de.md),
  aber da die Software auf Englisch ist, geht die Arbeit mit der englischen besser.)
- Software beschaffen:
  Kopieren Sie (einfach per Copy/Paste) den Quellcode von 
  `[gilded_rose.py](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/python/gilded_rose.py)`
  in die Datei `gildedrose/gilded_rose.py` in Ihrem ProPra-Verzeichnis.
- Testbasis beschaffen:
  Kopieren Sie (einfach per Copy/Paste) den Quellcode von 
  `[test_gilded_rose.py](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/python/test_gilded_rose.py)`
  in die Datei `gildedrose/test_gilded_rose.py` in Ihrem ProPra-Verzeichnis.
- Machen Sie einen Commit mit den beiden Dateien `gildedrose/*`.
- `test_gilded_rose.py` enthält genau einen Test.
  Führen Sie die Datei aus: Der Test schlägt fehl.
  Lesen, verstehen und reparieren Sie den Test.
- Machen Sie einen Commit mit der reparierten Datei `test_guilded_rose.py`.
- [EC] `git show --color=always HEAD | cat`
  (Achtung: Starten Sie `script` diesmal in einer zweiten Shell, sonst werden Sie viel zu
  bereinigen haben.)
- Sie können mit dieser Testsuite weiterarbeiten, die `unittest` benutzt.
  Praktischer ist aber, Sie verwenden `pytest` mit tabellengesteuerten Tests,
  wie aus Aufgabe [PARTREF::pytest104] bekannt.
  Wir empfehlen _dringend_, den Test jetzt diese Form umzuarbeiten.
  Gestalten Sie Test und Tabelle so, wie es zum Hinschreiben der Testfälle am praktischsten ist.
- Arbeiten Sie nun die Anforderungen durch und schreiben Sie, wo nötig, jeweils
  eine oder mehrere Testeingaben mit einer immer gleichen beliebigen Testausgabe.
  (Die Anforderung zu "conjured items" ist dabei natürlich auszulassen, denn die ist ja noch
  gar nicht umgesetzt, sondern ist der Anlass für das ganze Softwareprojekt.)
- Lassen Sie die Testfälle laufen und ergänzen Sie die erhaltene Testausgabe zu jedem Testfall.
- [EC] Lassen Sie die Testfälle laufen und überzeugen Sie sich, dass alle Tests erfolgreich sind.
- Machen Sie einen Commit mit Ihren Ergänzungen.
- [EC] `git show --color=always HEAD | cat`
- [EQ] Betrachten Sie nun die Tabelle bzw. die Klasse mit Ihren Testfällen.
  Ist sie übersichtlich? Gut verständlich? 
  Könnte man z.B. ggf. einen duplizierten Testfall leicht erkennen?
- [EQ] Falls nicht, reflektieren Sie darüber, warum Ihnen das unterwegs nicht aufgefallen ist
  bzw. warum Sie nichts dagegen unternommen haben.
- [EQ] Halten Sie Ihre Testfallmenge eher für 
  übervorsichtig (sehr viele Tests, vermutlich mehr als nötig) oder für
  hoffnungsvoll (eher wenige Tests: "Wird schon klappen") oder für 
  genau passend? Warum?
[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Testentwurf]
- Der ursprüngliche Test sollte erhalten bleiben oder in den tabellengesteuerten integriert werden.
- Wer `unittest` benutzt hat und jeden Testfall einzeln handkodiert, bitte zurückweisen:
  das ist unprofessionell.
- Wer `unittest` benutzt und sich selbst eine tabellengesteuerte Testlogik gebaut hat,
  kann wahrscheinlich pro Testlauf nur 1 Versagen sehen, nicht mehrere.
  Auf die Vorzüge von `pytest` hinweisen, wo das ohne Mehraufwand besser geht.
- Wenn die Sulfuras-Regel, dass sich `selL_in` nicht verändert, nicht überprüft wird,
  die Tests zurückweisen.  
  Ob man das hingegen in der Tabelle widerspiegelt oder in der Testlogik separat abfragt,
  ist Geschmackssache.
- Wenn jemand noch mehr Regeln mit Testlogik abgebildet hat anstatt über Daten,
  bitte ermahnen: Das würde einem im wirklichen Leben schnell über den Kopf wachsen.
  Für Charakterisierungstests sind Testtabellen die Methode der Wahl.
[ENDINSTRUCTOR]