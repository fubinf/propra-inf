title: Pandas Datenstrukturen
stage: alpha
timevalue: 1
difficulty: 2
assumes: pd-Einführung
---

[SECTION::goal::idea]
Ich kann `Series` und `DataFrames` erstellen.

Ich verstehe, was ein Index ist, wie ich ihn ändern kann und wie ich mithilfe der Indexwerte auf
spezifische Elemente aus einem `DataFrame` oder einer `Series` zugreife.
[ENDSECTION]

[SECTION::background::default]
Daten und Datensätze können nicht nur aus externen Dateien kommen. 
Oft möchte man auch eigene Daten, die in Variablen im Code gespeichert sind, verwenden. 
Um mit diesen Daten und Daten in Pandas-Objekten komptetent hantieren zu können, 
ist es wichtig, ein gutes mentales Modell der Daten zu haben.
[ENDSECTION]

[SECTION::instructions::loose]
In der Pandas-Einführung haben Sie bereits tabellarische Daten kennengelernt und dass diese in
Pandas durch `Series` und `DataFrame` dargestellt werden.

### pd.Series

Eine `Series` enthält 1-dimensionale Daten. 
Sie ist in der Hinsicht also sehr ähnlich zu einem Array, 
besitzt aber noch ein paar mehr Eigenschaften, wie Sie nach und nach lernen werden. 
Sie können tatsächlich auch aus einem Array direkt eine `Series` erstellen.

- Erstellen Sie die `Series` namens `buecher_namen_series` mit folgendem Code:
```python
buecher_namen_array = ["Harry Potter und der Stein der Weisen", "Der kleine Prinz", "Die unendliche Geschichte"]
buecher_namen_series = pd.Series(buecher_namen_array)
print(buecher_namen_series)
```
[EQ] Schauen Sie sich die 
[Dokumentation von Pandas zu Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) 
an.
Welche von den Parametern aus der Dokumentation haben wir bei der Erstellung der `Series` übergeben?
Was für einen Effekt hatten die übergebenen Parameter?

Betrachten Sie den Output. 
Links neben den Büchernamen sollten Sie jeweils eine Nummer sehen (0, 1, ...). 
Das ist der standardmäßige [TERMREF::Index] für eine `Series`. 
Genauso wie bei einem herkömmlichen Array (`array[Indexwert]`) kann der Index bei einer `Series` 
genutzt werden, um auf bestimmte Elemente innerhalb der Datenstruktur zuzugreifen. 
Ein Indexwert ist quasi wie eine Adresse, um einen Datenpunkt wiederzufinden.

[ER] Wählen Sie das dritte Element aus der `Series` aus, indem Sie den richtigen Indexwert benutzen. 
Der Syntax ist wie bei einem Array: `series[Indexwert]`

Bisher sieht man keine großen Unterschiede zu einem herkömmlichen Array. 
Doch ein Vorteil von `Series` ist, dass die Indexwerte bei `Series`-Objekten keine Integer sein
müssen, auch wenn das standardmäßig der Fall ist.
Es können beliebige Datentypen und beliebige Werte sein 
und nicht nur eine starre Aufzählung 0, 1, 2, ...:

Überschreiben Sie `buecher_namen_series` mit dem folgenden neuen Index:
```python
buecher_namen_series = pd.Series(buecher_namen_array, 
    index=["3-551-32011-X", "3-7920-0024-5", "3-522-20202-3"] # ISBN der Bücher
)
```

[ER] Wählen Sie das Buch "Die unendliche Geschichte" mithilfe des neuen Indexwert aus.

Erstellen Sie wie folgt eine zweite `Series` namens `buecher_preis_series`:
```python
buecher_preis_dict = {
    "3-522-20202-3": 12.99,
    "3-551-32011-X": 5.99,
    "3-7920-0024-5": 5.90
}
buecher_preis_series = pd.Series(buecher_preis_dict)
print(buecher_preis_series)
```
Diesmal haben Sie kein Array, sondern ein [TERMREF::Dictionary] übergeben. 
Wie Sie in der 
[Dokumentation von Pandas](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
sehen ist dies auch ein valider Eingabe-Typ für den Parameter: 
`array-like, Iterable, dict, or scalar value`. 

Nicht nur das: 
Während wir bei einem einfachen Array den Index selber hätten angeben müssen, 
werden hier die Keys des Dictionary als Index interpretiert.

[ER] Erstellen Sie nun ein eigenes Dictionary, das zu jedem Buch eine beliebige Bewertung (1-10)
speichert. 
Nutzen Sie dieses Dictionary, um Ihre eigene `Series` namens `buecher_bewertung_series` zu erstellen.

Wenn Sie nun zu einem Buch den Namen und den Preis wollen, können Sie die Daten 
anhand der ISBN aus den `Series` holen:
```python
isbn = "3-522-20202-3"
print(buecher_namen_series[isbn])
print(buecher_preis_series[isbn])
print(buecher_bewertung_series[isbn])
```

### pd.DataFrame

Bis jetzt haben Sie drei `Series` zu dem gleichen Thema erstellt, wobei die Indexwerte angeben,
welche Informationen zusammengehören.
Es wäre praktisch, wenn man diese Daten aber nicht aus jeder einzelnen `Series` abfragen muss,
sondern eine Art Tabelle (2-dimensionale Datenstruktur) hat, wo alle Informationen liegen. 
An dieser Stelle kann ein `DataFrame` weiterhelfen.

Zuerst erstellen Sie ein Dictionary, in dem Sie alle `Series` (und ihre Namen) auflisten. 
Dieses übergeben wir dann an den `pd.DataFrame`-Konstruktor.
```python
buecher_dict = {
    "Buchname": buecher_namen_series,
    "Preis in €": buecher_preis_series,
    "Bewertung": buecher_bewertung_series
}

buecher_df = pd.DataFrame(buecher_dict)
print(buecher_df)
```

Der Output dürfte wie folgt aussehen:
```
                                            Buchname  Preis in €  Bewertung
3-522-20202-3              Die unendliche Geschichte       12.99          7
3-551-32011-X  Harry Potter und der Stein der Weisen        5.99          8
3-7920-0024-5                       Der kleine Prinz        5.90          9
```

[NOTICE]
Es gibt noch weitere Arten, wie man mit einer `Series` ein `DataFrame` erstellen könnte, 
die Sie in den
[Beispielen der Dokumentation zu DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
nachlesen können. 
Die Erstellung aus einem Dictionary ist aber eine sehr gängige.
[ENDNOTICE]

[EQ] Welchen Vorteil kann der benutzerdefinierte Index bei der Erstellung eines `DataFrame`
bieten?

Nun haben Sie ein `DataFrame` erstellt, bei dem jede Spalte eine der `Series` darstellt.
So eine zwei-dimensionale Datenstruktur benötigt dementsprechend auch zwei Indizes: 
einen für die Spalten und einen für die Zeilen.
Während Sie bei einer `Series` mit `series[zeilen_index_wert]` auf ein einzelnes Element zugreifen konnten,
können Sie bei einem `DataFrame` mit `dataframe[spalten_index_wert]` auf eine ganze Spalte des
`DataFrame` zugreifen.

[NOTICE]
In Pandas wird der Zeilenindex eines `DataFrame` als `index` bezeichnet 
und der Spaltenindex als `columns`.
Mit `dataframe.index` kriegen Sie die Indexwerte des Zeilenindex und mit `dataframe.columns` die Indexwerte des Spaltenindex.
[ENDNOTICE]

[ER] Wählen Sie mithilfe des Spaltenindex die Kostenspalte von `buecher_df` aus.

Bei diesen Spalten handelt es sich um `Series`-Objekte. 
Das kann man z. B. mit der Methode `type()` herausfinden. 
Eine Spalte eines `DataFrame` kann man sich also als eine `Series` vorstellen. 
Jede Operation, die man auf `Series` machen kann, kann man also auch auf Spalten machen.

[EQ] Wenn `dataframe[spalten_index_wert]` eine `Series` ist und `series[zeilen_index_wert]` ein
Element einer `Series` zurückgibt: 
Wie können Sie dann mit Hilfe des `spalten_index_wert` und `zeilen_index_wert` ein
einzelnes Element aus einem `dataframe` zurückgeben? 
Erstellen Sie keine Hilfsvariablen.

[ER] Wählen Sie den Buchnamen "Die unendliche Geschichte" mit Hilfe des Spalten- und Zeilenindex
aus dem `buecher_df` aus.
[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Verstehen die Studierenden mit Indizes umzugehen]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]