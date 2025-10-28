title: Überblick über Daten
stage: beta
timevalue: 0.5
difficulty: 2
assumes: pd-Datenstrukturen
requires: pd-Einführung
---

[SECTION::goal::idea]
Ich kann mir mithilfe von Methoden und Attributen einen Überblick über ein `DataFrame` und seine Daten
verschaffen.
[ENDSECTION]

[SECTION::background::default]
Ein umfangreicher `DataFrame` kann überwältigend sein, wenn man nicht weiß,
wie man ihn sich erschließt.
[ENDSECTION]

[SECTION::instructions::loose]
Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) 
wie in [PARTREF::pd-Einführung] beschrieben in ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Inhalt gezielt betrachten

Bis jetzt haben Sie Einblicke in die Daten selbst nur bekommen, indem Sie zum Beispiel mit 
`print(erststimmen_df)` den ganzen `DataFrame` ausgegeben haben. 
Doch es gibt elegantere Lösungen, um sich Einträge eines `DataFrame` gezielt anzugucken. 
Schauen Sie in die Dokumentation zu 
[DataFrame.head()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) und 
[DataFrame.tail()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html) 
und bearbeiten Sie die folgenden Aufgaben:

[EQ] Beschreiben Sie, was die Methoden `head(n)` und `tail(n)` machen.

[ER] Geben Sie mithilfe der neuen Methoden die ersten 15 Zeilen des `erststimmen_df` aus.

[EQ] Was würde `example_df.tail(-3)` zurückgeben?

[EQ] Was passiert bei `example_df.head(n)`, wenn n größer ist als die Anzahl an Zeilen in
`example_df`?

Diese Funktionen sind ein schneller Weg, um sich beispielhaft Daten am Anfang und Ende anzugucken.
Mit einer weiteren hilfreichen Funktion kann man _zufällig_ ausgewählte Datensätze erhalten:
[DataFrame.sample()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample).

[ER] Geben Sie fünf zufällige Einträge des `erststimmen_df` aus.

[ER] Geben Sie ein Drittel der Daten zufällig aus. Schauen Sie dafür in die Parameter für die
Funktion.

[EQ] Beschäftigen Sie sich mit dem Parameter `random_state` von `sample()`. 
Welcher Wahlbezirk kommt hinaus, wenn Sie den `random_state=42` und `n=1` verwenden? 
Nennen Sie die Adresse.

[EQ] Wieso kann man mit `sample()` eventuell informativere Einblicke in die Datensätze kriegen 
als mit `head()` und `tail()`?

[HINT::Mehr Informationen durch `sample()`]
Betrachten Sie die Spalte "Adresse" in `erststimmen_df.head()`.
Hätte es sich für Sie allein aus diesen Werten erschlossen, 
dass "06B3F" ein gültiger Wert für eine Adresse ist?
[ENDHINT]

### Metadaten des `DataFrame`

Eine andere Art, ein `DataFrame` zu verstehen, ist, mithilfe von 
[DataFrame.info()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html) 
eine Übersicht an Informationen zu
bekommen.

Beantworten Sie mithilfe von `erststimmen_df.info()` folgende Fragen:

[EQ] Wie viele Spalten hat `erststimmen_df`?

[EQ] Wie viele Spalten speichern Integer-Daten?

[NOTICE]
Der Datentyp der Daten, die in einer Series gespeichert werden, wird als `dtype` bezeichnet. Siehe
[Dokumentation](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype) 
[ENDNOTICE]

[EQ] Was ist der *Rückgabewert* von `info()`?

[EQ] Welche Spalte hat die wenigsten Einträge?

Auch wenn `info()` eine gute Übersicht an Informationen bietet, liegen diese nur zur Ansicht vor.
Wenn man mit den Informationen weiterarbeiten möchte, ist `info()` ungeeignet, aber natürlich
gibt es Alternativen. 
Zum Beispiel kann man mit dem Attribut `erststimmen_df.shape` 
die Zeilen- und Spaltenanzahl eines `DataFrame` ermitteln.

[EQ] Schauen Sie in die 
[Dokumentation zu DataFrame-Attributen](https://pandas.pydata.org/docs/reference/frame.html#attributes-and-underlying-data)
und finden Sie heraus, in welchem Attribut die Zeileneinträge gespeichert werden.


### Statistische Metadaten

Mit `info()` haben Sie einen guten Überblick über den `DataFrame`, seine Spalten und andere
[TERMREF::Metadaten]. 
Zusammen mit `head()`, `tail()` und `sample()` können Sie sich bereits
einen guten Eindruck auch über einen großen `DataFrame` verschaffen.

Zur Vollständigkeit sei hier aber noch die Methode `describe()` aufgeführt. 
Ähnlich wie `info()` liefert sie Informationen über den `DataFrame` -- die Daten sind 
dabei aber statistischer Natur.

[EQ] Schauen Sie sich die 
[Dokumentation zu describe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe) 
an und benutzen Sie `describe()` auf dem `erststimmen_df`. 
Zu welcher Art von Spalten werden hier Daten aufgeführt? 
Und wieso nicht zu den anderen Spalten?

[EQ] Was ist die maximale Anzahl an Stimmen, die die SPD in einem Wahlbezirk bekommen hat?

[EQ] Was ist die minimale Anzahl an Stimmen, die die CDU in einem Wahlbezirk bekommen hat?

[EQ] Wie viele Stimmen hat die FDP im Durchschnitt bekommen?

Mit `describe()` lassen sich, wie Sie sehen, viele statistische Metadaten schnell präsentieren.
Neben dem Minimum, Maximum und Durchschnitt gibt es noch weitere interessante Metriken, 
die Sie in späteren Aufgaben ([PARTREF::pd-Statistik]) kennenlernen werden.
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
