title: Überblick über Daten
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: pd-Datenstrukturen
requires: pd-Einführung
---

[SECTION::goal::idea]

Ich kann mir mithilfe von Methoden und Attributen einen Überblick über ein DataFrame und seine Daten verschaffen.

[ENDSECTION]

[SECTION::background::default]

Ein DataFrame enthält oft eine Menge an Informationen. Gerade wenn man noch nicht vertraut ist mit einem bestimmten DataFrame ergibt es Sinn sich erst einmal einen Überblick über das DataFrame zu verschaffen. Dafür gibt es bestimmte Methoden und Attributen die sinnvoll sind.

[ENDSECTION]

[SECTION::instructions::loose]

[EC] Laden Sie zunächst den [Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) wie in [PARTREF::pd-Einführung] beschrieben in ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Überblick über den Inhalt

Bis jetzt haben Sie Einblicke in die Daten selbst nur bekommen, indem Sie zum Beispiel mit `print(erststimmen_df)` das ganze DataFrame ausgegeben. Doch es gibt elegantere Lösungen, um sich Einträge eines DataFrames gezielt anzugucken. Schauen Sie in die Dokumentation zu [DataFrame.head()](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.head.html) und [DataFrame.tail()](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.tail.html) und bearbeiten Sie die folgenden Aufgaben:

[EQ] Beschreiben Sie was die Methoden `.head(n)` und `.tail(n)` machen.

[EC] Geben Sie mithilfe der neuen Methoden die ersten 15 Zeilen des `erststimmen_df` aus.

[EQ] Was würde `example_df.tail(-3)` zurückgeben?

[EQ] Was passiert bei `example_df.head(n)`, wenn n größer ist als die Anzahl an Reihen in `example_df`?

Diese Funktionen sind ein schneller Weg um sich beispielhaft Daten am Anfang und Ende anzugucken. Doch es gibt eine weitere Funktion, die hier sehr hilfreich ist, um zufällige Daten zu erhalten: [DataFrame.sample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample).

[EC] Geben Sie fünf zufällige Einträge des `erststimmen_df` aus.

[EC] Geben Sie ein Drittel der Daten zufällig aus. Schauen Sie dafür in die Parameter für die Funktion.

[EQ] Beschäftigen Sie sich mit dem Parameter `random_state` der `.sample()`. Welcher Wahlbezirk kommt hinaus, wenn Sie den `random_state=42` und `n=1` verwenden? Nennen Sie die Adresse.

### Metadaten des DataFrames

Eine andere Art ein DataFrame zu verstehen ist mithilfe von [DataFrame.info()](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.info.html) eine Übersicht an Informationen zu bekommen.

Beantworten Sie zu `erststimmen_df.info()` folgende Fragen:

[EQ] Wie viele Spalten hat `erststimmen_df`?

[EQ] Wie viele Spalten speichern Integer-Daten?

[NOTICE]
Der Datentyp der Daten die in einer Series gespeichert wird, wird als `dtype` bezeichnet. Siehe [Dokumentation](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dtype.html#pandas.Series.dtype) 
[ENDNOTICE]

[EQ] Was gibt `.info()` zurück (Rückgabewert)?

[EQ] Welche Spalte hat die wenigsten Einträge?

Außerdem haben DataFrames noch ein paar hilfreiche Attribute. Zum Beispiel kann man mit `erststimmen_df.info()` indirekt auf die Zeilen- und Spaltenanzahl eines DataFrames schließen, ein anderer Weg wäre das `erststimmen_df.shape`-Attribut zu benutzen.

[EQ] Schauen Sie in die [Dokumentation zu DataFrames zu Attributen](https://pandas.pydata.org/docs/dev/reference/frame.html#attributes-and-underlying-data) und finden Sie heraus in welchem Attribut die Zeileneinträge gespeichert werden.

### Ausblick

Mit `.info()` haben Sie wie Sie sehen einen guten Überblick das DataFrame, seine Spalten und anderen [TERMREF::Metadaten]. Zusammen mit `.head()`, `.tail()` und `.sample()` können Sie sich bereits einen sehr guten Eindruck über DataFrames machen.

Zur Vollständigkeit sei hier noch die `.describe()`-Methode erwähnt. Ähnlich wie `.info()` liefert sie Informationen über das DataFrame - die Daten sind dabei aber statistischer Natur. Sie können damit also Sachen wie den Durchschnitt, Minimum, Maximum und weitere Informationen über die Spalten schnell überblicken.

<!-- TODO_2_Saka: Auf Aufgabe verweisen, in der man in die analytischen Methoden eingeführt wird -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Korrektur]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
