title: "Daten gruppieren"
stage: draft
timevalue: 2
difficulty: 2
explains:
assumes:
requires: pd-Datenselektion2
---

[SECTION::goal::idea]
Ich verstehe was kategorische Daten sind und wie ich sie benutzen kann.

Ich kann Daten nach Gemeinsamkeiten gruppieren.

Ich kann mit hierarchischen Indizes umgehen.
[ENDSECTION]


[SECTION::background::default]
Datenpunkte haben oft Gemeinsamkeiten bzw. Unterschiede nach denen man die Daten aufteilen möchte.
Wie das geht
[ENDSECTION]


[SECTION::instructions::detailed]
Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis)
wie in
[PARTREF::pd-Einführung] beschrieben in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Kategorische Daten

Kategorische Daten sind Daten, die Werte in Form von Gruppen oder Kategorien annehmen, 
ohne eine natürliche Reihenfolge oder numerische Bedeutung zu haben.

Wenn wir einen Datensatz über Personen hätten, dann sind z. B. das Geschlecht mit `männlich` oder
`weiblich` kategorische Daten oder die Augenfarbe (`blau`,`grün`,`braun`,etc.).

[EQ] Listen Sie 5 Spalten aus dem `erststimmen_df` auf, die kategorische Daten enthalten.

[EQ] Die Spalte "Bezirksnummer" enthält numerische Daten. 
Handelt es sich hierbei trotzdem um kategorische Daten oder nicht?
Begründen Sie.

### Gruppieren mit `groupby()`

Kategorische Daten kann man sich quasi als Gruppen vorstellen.
Oft kann es interessant sein zu sehen, in welchen anderen Eigenschaften sich diese Gruppen
unterscheiden.
Wenn Sie z. B. zwischen `männlich` und `weiblich` unterscheiden, kann es interessant sein sich
anzugucken, wie die durchschnittliche Lebensdauer sich zwischen diesen beiden Gruppen verhält.
Die Methode
[`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
ist ideal, um solche kategorischen Daten zu gruppieren.

[ER] Schauen Sie sich die Dokumenation zu `groupby()` an und gruppieren Sie `erststimmen_df`
nach den Bezirksnamen in `bezirks_gruppierung`.

[EQ] Was für einen Datentyp ist `bezirks_gruppierung`?

Wie Sie merken, handelt es sich hierbei um ein etwas undruchsichtigeres Konstrukt.
Zwar wissen wir, dass die Daten nun gruppiert sind, aber wie das genau aussehen soll ist nicht
ganz ersichtlich.
Wenn man `bezirks_gruppierung` ansieht, dann handelt es sich auch nicht um ein simples DataFrame.
Das liegt daran das wir zwar die Daten gruppiert haben, `pandas` weiß aber nicht welche
Informationen über die Gruppen wir gerne hätten. 

[EQ] Beschreiben Sie was `bezirks_gruppierung.max()` zurückgibt und in welcher Struktur.

Im gleichen Stil lassen sich auch andere Funktionen wie z.b. `min()` oder `mean()` anwenden.
Und noch viel besser zum Betrachten der Daten: 
Wenden Sie einfach ein anonyme Funktion wie `apply(lambda x: x)` auf `bezirks_gruppierung` an,
um die Daten in Ihrer rohen Form betrachten zu können. 
Mit Funktionen weiß `pandas` also Bescheid, welche Informationen Sie über die Gruppen haben wollen.
<!-- TODO_2_Saka: Verweis auf apply Aufgabe -->

[ER] Gruppieren Sie nach "Wahlbezirksart" und berechnen Sie die 
durchschnittliche Anzahl gültiger Stimmen.

[ER] `groupby()` lässt aber nicht nur auf eine kategorische Variable filtern. 
Gruppieren Sie `erststimmen_df` nach "Bezirksname" und "Wahlbezirksart".

Wenn Sie das Ergebnis betrachten, fällt Ihnen bestimmt der eigenartige Index auf, für die Zeilen.
Dadurch, dass Sie nun mehrer Gruppierungskriterien angegeben haben, brauchen wir Gruppierungen in
Gruppen.
Der Index hat jetzt quasi mehrere _Level_ und wird auch hierarchischer Index oder
[MultiIndex](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex)
genannt.
So lassen sich z. B. feingranulare Analysen durchführen, z. B. wie sich Wahlergebnisse je nach
Bezirk und Wahlform unterscheiden.

[EC] Wie können Sie im Code überprüfen, ob es sich beim Index um einen MultIndex oder einen
"normalen" Index handelt?

[EC] Wenn Sie auf ein bestimmtes Level zugreifen möchten, dann geben Sie nun statt `loc[IndexWert]`
das Level mit an in einem Tupel `loc[(Level1Wert, Level2Wert)]`.
Geben Sie den Wert für `Friedrichshain-Kreuzberg` auf dem ersten Level und `O` auf dem zweiten Level
aus.

[EC] Konvertieren Sie den MultiIndex mittels 
[`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)
zu einem einfachen Index.

### `agg()`

[EQ] Schauen Sie sich die Dokumentation zu 
[`agg()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)
an und formulieren Sie `bezirks_gruppierung.max()` so um, dass es `agg()` nutzt.

[EC] Mit `agg()` lassen sich die Gruppierungen noch flexibler nutzen.
Sie können z. B. mehrere Funktionen gleichzeitig auf die Gruppen anwenden.
Wenden Sie sowohl `min()` als auch `max()` mit `agg()` an.

[EQ] Das `agg()` sehr flexibel ist, sieht man auch daran, dass man Dictionaries übergeben kann,
um noch gezielter Informationen zu bekommen.

```python
partei_stats = erststimmen_df.groupby('Bezirksname').agg({
    'SPD': ['sum', 'mean'],
    'CDU': ['sum', 'mean'],
    'Die Linke': ['sum', 'mean'],
    'GRÜNE': ['sum', 'mean'],
    'AfD': ['sum', 'mean']
})
```

[EC] Gruppieren Sie nach "Bezirkname" und "OstWest". Aggreggieren Sie die Summe der
Summe der Stimmen für die AfD, das Maximum für die Grünen, sowie die durchschnittliche Anzahl an 
ungültigen Stimmen.

[EQ] Können Sie `reset_index()` auch nutzen, um den Spalteindex von Multiindex zu einem einfachen
Index zu konvertieren?

### Gruppieren mit Bedingungen

Ähnlich wie bei [TASKREF::pd-Datenselektion2], kann man auch bei `groupby()` nicht nur Spalten
angeben, sondern auch logische Ausdrücke:
```python
grouped = df.groupby(df['Punkte'] >= 50) # Beispiel
```

[EC] Gruppieren Sie `erststimmen_df` nach Einträgen, bei denen die AfD mehr Stimmen hatte 
als die Linke.

[EQ] Beschreiben Sie den Zeilenindex.

[ENDSECTION]


[SECTION::submission::reflection/information/snippet/trace/program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::]
Hinweise an die Tutoren zur Aufgabenkorrektur
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
