title: Einführung in Pandas
stage: alpha
timevalue: 0.5
difficulty: 1
assumes: pip
---

[SECTION::goal::idea]

Ich habe die Datenstrukturen von Pandas grundlegend verstanden und kann DataFrames aus eigenen oder externen Daten erstellen.

[ENDSECTION]

[SECTION::background::default]

Der Umgang mit Daten – sie zu sammeln, zu bearbeiten und zu analysieren – ist ein essenzieller Bestandteil in vielen Bereichen unserer heutigen Welt. Pandas ist dafür ein mächtiges Werkzeug und stellt eine Reihe an Datenstrukturen und Methoden bereit, um Daten in Python bearbeiten und analysieren zu können.

Diese Aufgabe führt Sie in die grundlegende Funktionsweise von Pandas ein: wie man einen Datensatz mit Pandas erstellt oder importiert und wie diese Daten strukturiert sind.

[ENDSECTION]

[SECTION::instructions::loose]

### Setup

Installieren Sie `pandas` mittels [PARTREF::pip].

Nach Konvention wird `pandas` mit dem Alias `pd` abgekürzt. Der Import in einer Python-Umgebung sieht standardmäßig also wie folgt aus: `import pandas as pd`.

### Datenstrukturen in Pandas

Um nun die breite Palette an Pandas-Werkzeugen nutzen zu können, brauchen Sie erst einmal ein Verständnis wie Daten in Pandas strukturiert sind und Daten mit denen Sie arbeiten können. Dazu können entweder Daten direkt mit Python erstellt werden, oder aus einem externen Datensatz (z.B. in Form einer Datei) geladen werden.

Es gibt zwei Datenstrukturen in Pandas:

- `pd.Series`, eine eindimensionale, listenartige Datenstruktur
- `pd.DataFrame`, eine zweidimensionale, tabellenartige Datenstruktur

#### pd.Series
Eine Series ist eine eindimensionale Datenstruktur in Pandas, die man sich als Array mit beschrifteten Achsen (Index) vorstellen kann.

- [ER] Erstellen Sie zunächst aus dem Array `[3.78,1.91,0.69]` eine Pandas-Series `einwohner_in_mio` und lassen Sie sich die Series ausgeben.

[NOTICE]
In die [Dokumentation von Pandas](https://pandas.pydata.org/docs/dev/index.html) zu schauen kann oft sehr hilfreich sein, um Methoden oder Eigenschaften besser zu verstehen!
[ENDNOTICE]

Die Series sollte wie folgt aussehen:
```
0    3.78
1    1.91
2    0.69
dtype: float64
```
Hier sieht man, dass jeder Wert in einer Series einen Index hat. Die Indizes sind standardmäßig Integer es können aber auch andere Datentypen genutzt werden.

- [ER] Erstellen Sie aus dem Array `[3.78,1.91,0.69]` eine Series `einwohner_in_mio_2` mit dem Index `["Berlin","Hamburg","Bremen"]`

Der Output sollte wie folgt aussehen:
```
Berlin     3.78
Hamburg    1.91
Bremen     0.69
dtype: float64
```

Wer mit der Datenstruktur [TERMREF::Dictionary] vertraut ist, dem fallen Parallelen zwischen Series und Dictionaries auf: Beide arbeiten mit Indizes, deren Datentyp beliebig sein kann. Tatsächlich kann man aus einem Dictionary auch direkt eine Series erstellen (und umgekehrt).

```
flaeche_km2_dict = {
    "Berlin": 891.8,
    "Hamburg": 755.2,
    "Bremen": 325.4
}
```

- [ER] Erstellen Sie mit dem `flaeche_km2_dict` eine weitere Series `flaeche_in_km2`.

#### pd.DataFrame

Ein DataFrame ist wohl die am meisten genutzte Datenstruktur in Pandas. Wenn man sich zum Beispiel eine Series als eine Spalte vorstellt, dann wäre das DataFrame eine Reihe an Spalten bzw. eine Tabelle.
Deshalb kann man sich DataFrames auch wie Dictionaries vorstellen und nach der [Dokumentation von Pandas zu DataFrames](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.html) ein Dictionary benutzen, um ein DataFrame zu erstellen: 
```
tabellen_dict = {
    "Index von Spalte 1": series1,
    "Index von Spalte 2": series2
}
```

- [ER] Erstellen Sie ein DataFrame aus den vorherigen beiden Series `einwohner_in_mio_2` und `flaeche_in_km2`. Erstellen Sie dafür zunächst ein Dictionary. Die Spaltenindizes sollten "Einwohner in Millionen" und "Fläche in Quadratkilometer" sein.

- [EQ] Wie viele Zeilen hat Ihr DataFrame, wenn Sie die Series `einwohner_in_mio` statt `einwohner_in_mio_2` benutzen? Wie entsteht die Änderung?

### DataFrame aus einer Datei laden

Es gibt eine Vielzahl von Quellen aus denen man Datensätze kriegen kann. Eine davon ist [GovData](https://govdata.de), eine Sammlung von Datensätze, veröffentlicht von staatlichen Institutionen.

Laden Sie die .csv Datei der [Erststimmen der Bundestagswahl 2025 - Berlin](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) runter.

- [ER] Mit dem Befehl `pd.read_csv("Pfad/zu/der/Datei.csv, sep=';')` können Sie diese Daten als ein DataFrame laden. Tuen Sie dies für die heruntergeladene CSV-Datei und lassen Sie sich das neue DataFrame ausgeben.

[NOTICE]
CSV-Dateien trennen Spalten standardmäßig mit einem Komma. In diesem Fall ist der Seperator aber kein Komma, sondern ein Semikolon weshalb wir `sep=';'` explizit mit angeben müssen.
[ENDNOTICE]

Jetzt können Sie DataFrames und Series erstellen und externe Datensätze laden. In den nächsten Aufgaben werden Sie die hilfreichen Methoden kennenlernen und benutzen, die Pandas zu so einer vielgenutzten Bibliothek machen.

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]