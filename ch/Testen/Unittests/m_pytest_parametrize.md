title: "@pytest.mark.parametrize: Testfälle per Eingabe-Tabelle parametrisieren"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: m_pytest
---

[SECTION::goal::idea]

Ich kann mit pytest tabellengesteuerte Testfälle gestalten.

[ENDSECTION]
[SECTION::background::default]

Es gibt häufig Tests, bei denen die gleiche Testlogik mit vielen verschiedenen Eingabeparametern 
benutzt werden sollte (und natürlich zugehörigen Erwartungen für die Ausgabe),
um relevant verschiedene Fälle abzudecken.

Der naive Weg hierzu wäre, die Testlogik in eine Hilfsfunktion `mytest` mit entsprechend vielen Parametern zu stecken
und dann in jedem Testfall nur genau einen Aufruf von `mytest` zu schreiben.
Bei 17 Testfällen braucht man so also 18 Funktionen.
Aber mit `pytest` geht es viel schlanker und eleganter, mit nur einer einzigen Funktion und
einer Datentabelle.

[ENDSECTION]
[SECTION::instructions::detailed]

- [ER] Legen Sie die Datei `pytests/test_pytest_parametrize.py` an.
- [ER] Implementieren Sie darin eine Funktion  
  `smallest_letter_and_digit(input: str) -> tuple[str | None, int | None]`  
  mit folgender Semantik:
    - Die Funktion ignoriert alle Zeichen in `input`, die keine Kleinbuchstaben sind 
      (nur solche im Bereich `a` bis `z`, keine Umlaute o.ä.) 
      und auch keine Ziffern sind (im Bereich `0` bis `9`).
    - Sie liefert ein Tupel aus dem alphabetisch kleinsten Kleinbuchstaben (als `str`)
      und der numerisch kleinsten Ziffer (als `int`, nicht `str`).
    - Sollte es in `input` keinen Kleinbuchstaben geben, wird stattdessen `None` geliefert.
    - Sollte es in `input` keine Ziffer geben, wird stattderer `None` geliefert.

- [ER] Implementieren Sie eine Testfunktion  
  `def test_smallest_letter_and_digit(input, letter, digit)`  
  die prüft, ob `smallest_letter_and_digit` die Eingabe `input` in die Ausgabe `(letter, digit)` überführt.
- Lesen Sie auf ["How to parametrize"](https://docs.pytest.org/en/stable/how-to/parametrize.html) nach,
  wie man diese Funktion mit einer Tabelle von Testdaten versorgen kann.
- [ER] Schreiben Sie eine solche Versorgung hin.
  Sie benötigen in Ihrer Tabelle 6 grundlegend verschiedene Testfälle:
  4 für alle nötigen Kombinationen von `None` und Nicht-`None`,
  2 weitere für grundlegend verschiedene Inputs für 2 dieser Fälle, wo die Logik intern anders funktioniert.
- Falls Sie gleich alles richtig gemacht haben: Probieren Sie auch aus, wie die Ausgabe im
  Versagensfall aussieht; studieren Sie das in Ruhe, denn es ist im Ernstfall sehr nützlich.
- [EC] `pytest pytests/test_pytest_parametrize.py`
- [EQ] Welchen Nachteil hätte es, wenn man nicht `pytest.mark.parametrize` benutzen würde,
  sondern in der Testfunktion eine Schleife macht, um deren Einträge zu durchlaufen? 
- [EQ] Kann man eine solche `pytest.mark.parametrize`-Tabelle aus einer Datei einlesen?
  Wie würde so ein Konstrukt gebaut?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Alle Teile prüfen]

Dies ist ein wichtiges Thema, deshalb prüfen wir hier mal gründlich:

- Die Testfälle müssen abdecken: Kleinstes zuerst, kleinstes später, gibtsnicht.
  Und das für Buchstabe und für Ziffer. Einmal mit und einmal ohne sonstige Zeichen.
  Ferner die leere Eingabe.
- Das Protokoll muss die gleiche Zahl von Testfällen anzeigen.
- Nachteil mit Schleife wäre, dass die Fälle nach dem ggf. ersten Versagen gar nicht mehr geprüft werden,
  und das man die Datenwerte bei Versagen nicht angezeigt bekommt.
- Der zweite Parameter von `pytest.mark.parametrize` kann natürlich ein Funktionsaufruf sein,
  der die Daten auf jede erdenkliche Weise beschaffen kann.
  Es muss lediglich ein Iterable von Tupeln dabei herauskommen.

[ENDINSTRUCTOR]