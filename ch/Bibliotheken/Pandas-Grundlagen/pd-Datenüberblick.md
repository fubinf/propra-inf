title: Überblick über Daten
stage: draft
timevalue: 0.5
difficulty: 2
requires: pd-Einführung, pd-Datenstrukturen
---

[SECTION::goal::idea]

Ich kann mir mit Überblick über ein DataFrame und seine Daten verschaffen.

Ich verstehe was `dtypes` in Zusammenhang mit Series und DataFrames bedeuten.

[ENDSECTION]

[SECTION::background::default]

Ein DataFrame enthält oft eine Menge an Informationen. Gerade wenn man noch nicht vertraut ist mit einem bestimmten DataFrame kann es Sinn machen sich erst einmal einen Überblick zu verschaffen.

[ENDSECTION]

[SECTION::instructions::loose]

[EC] Laden Sie zunächst den [Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) wie in [PARTREF::pd-Einführung] beschrieben in ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### .head() und .tail()

Bis jetzt haben Sie Einblicke in die Daten selbst nur bekommen in dem Sie zum Beispiel mit `print(erststimmen_df)` das ganze DataFrame ausgegeben. Bei großen DataFrames werden dabei aber standardmäßig nicht alle Zeilen ausgegeben sonder nur ein paar vom Anfang und vom Ende. Das ist auch erst einmal gut so: Stellen Sie sich vor Sie möchten sich ein bis zwei Beispiele für Einträge angucken und plötzlich ist Ihr Computer damit beschäftigt mehrere hunderttausend Einträge anzuzeigen.

Doch es gibt elegantere Lösungen um sich Einträge eines DataFrames anzugucken. Schauen Sie in die Dokumentation zu [DataFrame.head()](pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.head.html) und [DataFrame.tail()](pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.tail.html) und bearbeiten Sie die folgenden Aufgaben:

[EC] Geben Sie mit Hilfe der neuen Methoden die ersten 15 Zeilen des `erststimmen_df` aus.
[EQ] Was würde `sample_df.tail()` zurückgeben?
[EQ] Was würde `sample_df.tail(-3)` zurückgeben?
[EQ] Was passiert bei `sample_df.head(n)`, wenn n größer ist als die Anzahl an Reihen in `sample_df`?

Diese Funktionen sind ein schneller Weg um sich beispielhaft Daten am Anfang und Ende anzugucken.


### .info()

Eine andere Art ein DataFrame zu verstehen ist mit Hilfe von `.info()` eine Übersicht an Informationen zu bekommen.

Beantworten Sie mit Hilfe von `erststimmen_df.info()` folgende Fragen:
[EQ] Wie viele Spalten hat `erststimmen_df`?
[EQ] Was gibt der `dtype` einer Spalte an?
[EQ] Wie viele Spalten speichern Integer-Daten?
[EQ] Hat `.info()` für einen Rückgabewert?
[EQ] Welche Spalte hat die meisten leeren Felder?

Mit `.info()` haben Sie wie Sie sehen einen guten Überblick das DataFrame, seine Spalten und anderen [TERMREF::Metadaten]. Zusammen mit `.head()` und `.tail()` können Sie sich bereits einen sehr guten Eindruck des DataFrames.

### DataFrame Attribute

Indirekt lassen sich auch Zeilen und Spalten aus `.info()` ablesen, ein anderer Weg ist die `shape` ([Siehe Dokumentation](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.shape.html)) eines Objektes zu betrachten. 

[EQ] Hierbei fällt etwas auf. Während `DataFrame.info()` Klammern braucht, braucht `DataFrame.shape` keine. Recherchieren und erklären Sie den Unterschied von Methoden und Attributen einer Klasse (in dem Fall DataFrame).

[EQ] Schauen Sie in die [Dokumentation zu DataFrames](https://pandas.pydata.org/docs/dev/reference/frame.html#attributes-and-underlying-data) und finden Sie heraus in welchem Attribut die Zeileneinträge gespeichert werden.

[ENDSECTION]

[SECTION::submission::information]

[ENDSECTION]

[INSTRUCTOR::Korrektur]
.
[ENDINSTRUCTOR]
