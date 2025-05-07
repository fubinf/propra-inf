title: "unittest: Das Standard-Testframework von Python"
stage: beta
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea]

Ich kann Unittests mit dem Standard-Python-Testframework `unittest` schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

Anders als viele Sprachen hat Python ein Framework für automatisierte programmatische Tests
in seiner Standardbibliothek. Das sollten wir natürlich kennen!

[ENDSECTION]
[SECTION::instructions::detailed]

`unittest` ist das von Python mitgelieferte Testframework.
Nutzen Sie die [`unittest`-Dokumentation](https://docs.python.org/3/library/unittest.html)
um die nachfolgenden Aufgaben zu lösen:

### Ein erfolgreicher Test

- Legen Sie die Datei `test_unittest.py` an.
- [ER] Schreiben Sie darin einen Test `test_addition`, der sicherstellt, dass `1+1` gleich `2` ist.
  Bilden Sie die Struktur der Testklasse wie in "Basic example" beschrieben.
- Lassen Sie den Teil mit `__name__ == '__main__'` weg, diese Struktur wird nicht benötigt.
- [EC] Lassen Sie den Test laufen wie bei "Command-Line Interface" beschrieben.
- [EQ] Was bedeutet vermutlich der Punkt in der ersten Zeile der Ausgabe?
- [EC] Machen Sie einen Commit von `test_unittest.py`.  
  `git -P show HEAD`


### Ein fehlschlagender Test

- [ER] Schreiben Sie einen zweiten Test `test_sqrt`, der sicherstellt, 
  dass `math.sqrt(10)**2` (lesen Sie ggf. nach, was das bedeutet) gleich `10` ist.  
  Dieser Test wird fehlschlagen, weil Gleitkomma-Arithmetik nicht beliebig genau ist.
- [ER] Wählen Sie einen sinnvollen Klassennamen.
- [EC] Lassen Sie beide Tests laufen wie bei "Command-Line Interface" beschrieben.
- [EQ] Was bedeutet offenbar die erste Zeile der Ausgabe?
- Verstehen Sie sorgfältig die gesamte Ausgabe. 
  Sie fällt bei realer Software (wo es eine Verschachtelung von Aufrufen des Anwendungscodes gibt)
  um einiges komplizierter aus und beschreibt recht präzise den Fehlerort und das Symptom.
- [EC] Machen Sie einen Commit von `test_unittest.py`.  
  `git -P show HEAD`
- `test_sqrt` wird ja stets fehlschlagen, was die Ausgabe verwirrend macht.
  Schauen Sie das Inhaltsverzeichnis der Dokumentation nach diesem Thema durch.
  Markieren Sie den Test mit dem passenden Dekorierer von `unittest` als hoffnungslosen Fall.
- [EC] Lassen Sie beide Tests laufen.
- [EQ] Was bedeutet offenbar die Änderung in der ersten Zeile der Ausgabe?
- [EC] Machen Sie einen Commit von `test_unittest.py`.  
  `git -P show HEAD`


### Lösung für Vergleiche bei Gleitkomma-Arithmetik

- [ER] Es gibt für Tests mit Gleitkommaarithmetik eine andere Assertion, die auf
  "fast gleich" prüft statt auf "gleich". Damit lässt sich der Test `test_sqrt` doch noch retten.  
  Bauen Sie den Test entsprechend um und aktivieren Sie ihn wieder.
  Nehmen Sie zur Kenntnis, was diese Assertion intern tut (rechte Spalte der Tabelle).
- [EC] Lassen Sie beide Tests laufen.


### Test mit erwarteter Exception
 
- [ER] Schreiben Sie einen dritten Test, der sicherstellt, dass `math.sqrt(-1)` genau die
  in dessen Dokumentation angekündigte Exception erzeugt.
  Wählen Sie einen beschreibenden Namen für den Test.
- [EC] Lassen Sie alle drei Tests laufen.
- [EC] Machen Sie einen Commit von `test_unittest.py`.  
  `git -P show HEAD`

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Kommandoprotokoll und Markdown prüfen]

- Ausführung 1: Aufruf mit `python -m unittest test_unittest.py`, nicht implizit.
- Commit 1: Aufruf `unittest.main()` sollte nicht dabei sein.
- Commit 2: Sinnvoller Klassenname ist z.B. `TestArithmetic` oder etwas Ähnliches.
- Markdown: Die Ausgaben bedeuten: `.`:Erfolgreicher Testfall. `F`:failure. `x`:expected failure.
  `s`:skipped.
- Commit 3: `@unittest.skip` ist akzeptabel, aber eigentlich ist `@unittest.expectedFailure` richtig.
- Commit 4: `with self.assertRaises(ValueError)`

[ENDINSTRUCTOR]