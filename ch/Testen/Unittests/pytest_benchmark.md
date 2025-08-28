title: Pytest in Python - Anwenden des Benchmark Fixtures
stage: draft
timevalue: 0
difficulty: 3
assumes: m_pytest, pytest_fixtures, mocking
requires: LokalesDeployment
---

[SECTION::goal::idea]

Ich kann einfache Pytest-Benchmarks erstellen udn auswerten.

[ENDSECTION]
[SECTION::background::default]

Manche Unittests sind schnell und einfach in der Ausführung, einige eher teuer und dadurch langsamer.
Jetzt kann man ein Gespür für die Performance bekommen, was aber keine stabile Metrik ist. Daher
gibt es für Pytest das Fixture Benchmark, um die Geschwindigkeit messbar zu machen und dadurch
Vergleiche anzustellen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Allgemeine Anwendung

Ja, Sie haben richtig gelesen: `pytest-benchmark` stellt eine Fixture bereit, die es ermöglicht,
Leistungstests mit Pytest durchzuführen. Diese Fixture ermöglicht es, die Ausführungszeit von
Funktionen oder Codeabschnitten zu messen und zu benchmarken.

Verschaffen Sie sich einen allgemeinen Überblick über die Fixture auf der
[PyPi Seite](https://pypi.org/project/pytest-benchmark/).

- [EQ] Können Sie sich vorstellen damit im Alltag zu arbeiten? Begründen Sie.

Die benchmark-Fixture von pytest-benchmark kann in Tests verwendet werden, indem sie als Parameter
an Testfunktionen übergeben wird.

```python
def test_my_function(benchmark):
    # Hier kommt der Anteil des Unittests hin

    # Verwendung der benchmark-Fixture, um die Leistung der Funktion zu messen
    result = benchmark(my_function)
```

Dadurch können Entwickler die Ausführungszeit bestimmter Codeabschnitte messen und vergleichen,
um die Leistung ihres Codes zu optimieren.

### Praktische Anwendung am Bestandscode

Verwenden Sie das SUT, wie in der Aufgabe [PARTREF::LokalesDeployment] beschrieben. Nutzen Sie ferner
die in Aufgabe TODO erstellten Testfälle, um die Fixture anzuwenden.

Lassen Sie alle Testfälle **9-fach** durchlaufen und bilden Sie den [TERMREF::Median] jedes Testfalls.

- [EQ] Welche Werte erhalten Sie?
- [EQ] Sind Sie von den Werten überrascht? Begründen Sie.

[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
