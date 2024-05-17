title: "pytest: Das Profi-Testframework"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: m_unittest, pip
---

[SECTION::goal::idea]

Ich kann Unittests mit dem Profi-Python-Testframework `pytest` schreiben und ausführen.

[ENDSECTION]
[SECTION::background::default]

Für die meisten ernsthaften Anwendungen ist `pytest` das Testframework der Wahl:
Es ist zugleich wesentlich leistungsfähiger als `unittest` und trotzdem handlicher zu benutzen;
eine selten günstige Kombination!

Mit seinen Hunderten von Erweiterungen kann `pytest` auch sehr spezielle Anforderungen abdecken.

[ENDSECTION]
[SECTION::instructions::detailed]

Arbeiten Sie sich mittels der 
[Dokumentation von pytest](https://docs.pytest.org) 
und bei Bedarf weiteren Quellen mittels
der folgenden Aufgaben in das Framework ein.


### `ptest` als Ersatz für `unittest`

- [EC] Installieren Sie `pytest` mittels `pip install pytest`.
- [ER] Legen Sie die Datei `pytests/test_pytest.py` an als exakte Kopie der Datei `unittests/test_unittest.py`.
- [EC] Rufen Sie `pytest pytests/test_pytest.py` auf.
- [EQ] Aha, offenbar kann `pytest` als direkter Ersatz von `unittest` agieren.
  Welcher Output gefällt Ihnen besser? Warum?


### Schlankere Notation für Tests

- Lesen Sie auf der Homepage der `pytest`-Dokumentation die Abschnitte "A quick example" und
  "Features".
- [ER] Übertragen Sie per Analogieschluss den Code in `pytests/test_pytest.py` 
  von `unittest`-Stil nach `pytest`-Stil:
  Testklasse wegwerfen; 
  Testmethoden zu einfachen Funktionen machen (ohne Parameter);
  `self.assert...` ersetzen durch `assert`.   
  (Für den dritten Test müssen Sie die Dokumentation etwas weiter durchforsten.
   `assertAlmostEqual` realisiert man in `pytest` von Hand, wie in der Doku von `unittest` angegeben.)
- [EC] Machen Sie einen Commit von `pytests/test_pytest.py`.  
  `git -P show HEAD`
- [EC] Rufen Sie `pytest pytests/test_pytest.py` auf.
- [ER] Auch in `pytest` gibt es natürlich eine Lösung für das, was zuvor `@unittest.expectedFailure` hieß.
  Finden Sie sie und probieren Sie sie aus.

[HINT::Wie markiert man expected failures?]
`@pytest.mark.xfail`
[ENDHINT]

- [EC] Machen Sie einen Commit von `pytests/test_pytest.py`.  
  `git -P show HEAD`
- [EC] Rufen Sie `pytest pytests/test_pytest.py` auf.
- [EC] Rufen Sie `pytest -v pytests/test_pytest.py` auf.


### Tests mit Hilfsausgaben

Eine Eigenschaft von `pytest` ist extrem hilfreich, sobald es etwas komplizierter wird:
`pytest` verschluckt zunächst alle Bildschirmausgaben, die in Test macht und spuckt sie
nur dann aus, wenn der Test fehlschlägt.

Dadurch kann man seine Tests so konzipieren, dass sie allerlei Informationen, die für die
Diagnose eines Fehlschlags hilfreich sein könnten, routinemäßig ausgeben.
Wenn dann ein [TERMREF::Versagen] auftritt, hat man es im Nu verstanden.
Das ist für [TERMREF2::Modultest::-s] meist nicht nötig, 
aber für komplexe [TERMREF2::Integrationstest::-s] unbezahlbar.

Ergänzen Sie folgende beiden Tests und verstehen Sie sie:

```
def test_failure1():
    print("lots\nof\nstuff")
    assert False

def test_failure2(self):
    print("still\nmore\nstuff")
    assert False
```

- [EC] Lassen Sie die Tests laufen.
- [ER] Nun übertragen Sie die beiden Tests in `unittest`-Manier nach `unittests/test_unittest.py`.
- [EC] `python -m unittest unittests/test_unittest.py`
- [EQ] Vergleichen Sie die Ausgaben der beiden Kommandos.
  Was ist Ihr Eindruck?
  Fallen Ihnen noch wichtige Gründe ein, `unittest` zu benutzen?

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
