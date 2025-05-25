title: Datenstrukturen und Indizes in Pandas
stage: alpha
timevalue: 1
difficulty: 2
assumes: Pandas-Einführung
---

[SECTION::goal::idea]

Ich kann Series aus Listen erstellen.
Ich kann DataFrames aus Dictionaries erstellen.
Ich verstehe was ein Index ist, wie ich ihn ändern kann und wie ich mithilfe des Indexes auf spezifische Elemente aus einem DataFrame oder einer Series zugreife.

[ENDSECTION]
[SECTION::background::default]

Um gekonnt mit Daten in Pandas umzugehen, muss man wissen wie die Pandas-Datenstrukturen aufgebaut sind und auch wie man auf einzelne Datenpunkte zugreifen kann.

[ENDSECTION]
[SECTION::instructions::loose]

In der Pandas-Einführung haben Sie bereits tabellarische Daten kennengelernt und dass diese in Pandas durch Series und DataFrames dargestellt werden.

### pd.Series

Eine Series enthält 1-dimensionale Daten. Sie ist in der Hinsicht also sehr ähnlich zu einem Array, besitzt aber noch ein paar mehr Eigenschaften wie Sie nach und nach lernen werden. Sie können tatsächlich auch aus einem Array eine Series erstellen. 

- Erstellen Sie die Series `buecher_namen_series` mit folgendem Code:
```python
buecher_namen_array = ["Harry Potter und der Stein der Weisen", "Der kleine Prinz", "Die unendliche Geschichte"]
buecher_namen_series = pd.Series(buecher_namen_array)
print(buecher_namen_series)
```

[NOTICE]
Um zu verstehen, wie man eine `pd.Series` erstellt und was ihre Eingabeparameter sind können Sie sich die [Dokumentation von Pandas zu Series](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.html) anschauen.
[ENDNOTICE]

Betrachten Sie den Output. Links neben den Büchernamen sollten Sie jeweils eine Nummer sehen (0,1,...). Das ist der standardmäßige [TERMREF::Index] für eine Series. Genauso wie bei einem herkömmlichen Array (`array[Index]`) kann der Index bei einer Series genutzt werden, um auf bestimmte Elemente innerhalb der Datenstruktur zuzugreifen. Er ist quasi wie eine Adresse um einen Datenpunkt wiederzufinden.

- [ER] Wählen Sie das dritte Element aus der Series aus, indem Sie den Index benutzen. Der Syntax ist wie bei einem Array: `series[Index]`

Bisher sieht man keine großen Unterschiede zu einem herkömmlichen Array. Doch ein Vorteil von Series ist, dass der Index bei Series-Objekten keine Integer sein müssen. Es können beliebige Datentypen und beliebige Werte sein und nicht nur eine starre Aufzählung 0,1,2,...:

- Überschreiben Sie `buecher_namen_series` mit dem folgenden neuen Index:
```python
buecher_namen_series = pd.Series(buecher_namen_array, 
    index=["3-551-32011-X", "3-7920-0024-5", "3-522-20202-3"] # ISBN der Bücher
)
```

- [ER] Wählen Sie das Buch "Die unendliche Geschichte" mithilfe des neuen Index aus.

- [EQ] Welche Vorteile hat es einen eigenen Index verwenden zu können gegenüber dem Standard-Index (0,1,2,3,...)?

[HINT::Anregungen]
Stellen Sie sich vor, Sie arbeiten in einem Bücherladen. Würden Sie es bevorzugen Ihre Bücher anhand der ISBN zu suchen oder daran der wievielte Eintrag dieses Buch in Ihrer Liste war? 
Und was ist, wenn Sie eine zweite Datenquelle für Bücher anschließen wollen?
[ENDHINT]

- Erstellen Sie wie folgt eine zweite Series `buecher_preis_series`:
```python
buecher_preis_series = pd.Series([12.99, 5.99, 5.9],
    index=["3-522-20202-3", "3-551-32011-X", "3-7920-0024-5"]
)
print(buecher_preis_series)
```

Wenn Sie nun zu einem Buch den Namen und den Preis haben wollen können Sie die Daten anhand der ISBN aus beiden Series holen:
```python
isbn = "3-522-20202-3"
print(buecher_namen_series[isbn])
print(buecher_preis_series[isbn])
```

### pd.DataFrame

Bis jetzt haben Sie zwei Series zu dem gleichen Thema erstellt. Es wäre praktisch, wenn man diese Daten aber nicht aus jeder einzelnen Series abfragen muss sondern eine Art 2-dimensionale Datenstruktur hat, wie in einer Art Tabelle, wo alle Informationen liegen. An dieser Stelle kann ein DataFrame weiterhelfen.

- Zuerst erstellen wir ein Dictionary in dem wir alle Series (und ihre Namen) auflisten. Dieses übergeben wir dann an den `pd.DataFrame`-Konstruktor.
```python
buecher_dict = {
    "Buchname": buecher_namen_series,
    "Preis in €": buecher_preis_series
}

buecher_df = pd.DataFrame(buecher_dict)
print(buecher_df)
```

Der Output dürfte wie folgt aussehen:
```
                                            Buchname  Preis in €
3-522-20202-3              Die unendliche Geschichte       12.99
3-551-32011-X  Harry Potter und der Stein der Weisen        5.99
3-7920-0024-5                       Der kleine Prinz        5.90
```

[NOTICE]
Es gibt noch viele weitere Arten wie man mit Series ein DataFrame erstellen könnte, die Sie in den [Beispielen der Dokumentation zu DataFrames](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.html) nachlesen können. Die Erstellung aus einem Dictionary ist aber eine sehr gängige.
[ENDNOTICE]

Nun haben Sie ein DataFrame erstellt, bei dem jede Spalte eine der Series darstellt. Die Preise und Namen der Bücher wurden anhand des Index (die ISBN) korrekt zugeordnet.
So eine zwei-dimensionale Datenstruktur benötigt dementsprechend auch zwei Indizes: Eine für die Spalten und eine für die Zeilen.
Während Sie bei einer Series mit `series[zeilen_index]` auf ein einzelnes Element zugreifen konnten, können Sie bei einem DataFrame mit `dataframe[spalten_index]` auf eine ganze Spalte des DataFrame zugreifen.

[NOTICE]
In Pandas wird der Zeilenindex als `index` bezeichnet und der Spaltenindex als `columns`.
Mit `dataframe.index` kriegen Sie alle Zeilenindizes und mit `dataframe.columns` alle Spaltenindizes.
[ENDNOTICE]

- [ER] Wählen Sie mithilfe des Spaltenindex die Kostenspalte des DataFrames `buecher_df` aus.

Bei diesen Spalten handelt es sich um Series-Objekte. Das kann man z.B. mit der `type()`-Funktion herausfinden. Eine Spalte eines DataFrames kann man sich also als eine Series vorstellen. Jede Operation die man auf Series machen kann, kann man also auch auf Spalten machen.

- [EQ] Wenn `dataframe[spalten_index]` eine Series zurückgibt und `series[zeilen_index]` ein Element einer Series zurückgibt: Wie können Sie dann mit Hilfe des `spalten_index` und `zeilen_index` ein einzelnes Element aus einem `dataframe` zurückgeben?

- [ER] Wählen Sie den Buchnamen "Die unendliche Geschichte" aus dem dataframe `buecher_df` aus indem Sie zuerst die Spalte und dann die Zeile auswählen.


[ENDSECTION]
[SECTION::submission::information]

Geben Sie den Quellcode zu den Anforderungen [EREFR::1], [EREFR::2], ... ab.

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Verständnis für Indizes]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]