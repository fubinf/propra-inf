title: "pandas: Daten gruppieren"
stage: alpha
timevalue: 2
difficulty: 2
requires:
assumes: pd-Datenselektion2, pd-Transformationen
---

[SECTION::goal::idea]
Ich verstehe was kategorische Daten sind und wie ich sie benutzen kann.

Ich kann Daten nach Gemeinsamkeiten gruppieren.

Ich kann mit hierarchischen Indizes umgehen.
[ENDSECTION]


[SECTION::background::default]
Datenpunkte haben oft Gemeinsamkeiten bzw. Unterschiede nach denen man die Daten aufteilen möchte.
Diese Aufgabe behandelt wie das geht und was man mit den gruppierten Daten machen kann.
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

Kategorische Daten sind Daten, deren Werte einzelne Namen darstellen ("Nominalskala").
Das können Aufzählungstypen sein (mit einem festen, meist recht kleinen Wertebereich,
z.B. Geschlecht: "männlich", "weiblich", "divers")
oder offene Benennungen (z.B. Straßennamen, Familiennamen).
Auch geordnete Daten ("Ordinalskala", z.B. Größe: "S", "M", "L", "XL") kann man als kategorische Daten ansehen,
wenn sie keiner numerischen Ordnung folgen.
Allgemeine Strings, die man ja alphabetisch sortieren kann, würde man eher nicht als
kategorisch ansehen, wenn sie "zu viele" verschiedene Werte annehmen, denn in der Statistik
ist die Rolle kategorischer Daten oft, Datensätze in relevante Gruppen zu unterteilen.
Eine scharfe Grenze dafür gibt es aber nicht.

[EQ] Listen Sie 5 Spalten aus dem `erststimmen_df` auf, die kategorische Daten enthalten.

[EQ] Die Spalte "Bezirksnummer" enthält numerische Daten. 
Handelt es sich hierbei trotzdem um kategorische Daten oder nicht?
Begründen Sie.


### Gruppieren mit `groupby()`

Kategorische Daten kann man sich als Gruppenbezeichnungen vorstellen.
Oft kann es interessant sein, zu sehen, in welchen anderen Eigenschaften sich diese Gruppen
unterscheiden.
Die Methode
[`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
stellt eine entsprechende Gruppierung her.

[ER] Schauen Sie sich die Dokumentation zu `groupby()` an und gruppieren Sie `erststimmen_df`
nach den Bezirksnamen in die Variable `bezirks_gruppierung`.

Dabei ist `bezirks_gruppierung` ein `DataFrameGroupBy` also kein normales `DataFrame`.

Das klingt erstmal kompliziert, bedeutet aber nur,
dass es sich um einen _Gruppendeskriptor_ handelt.
Es speichert also Informationen darüber, welche Zeile zu welcher Gruppe gehört, welche Spalten
gruppiert wurden und wie die Gruppierung generell intern organisiert ist.

Wenn man versucht, sich `bezirks_gruppierung` anzusehen, 
dann handelt es sich auch nicht um ein simples DataFrame.
Das liegt daran, dass wir zwar die Daten gruppiert haben, `pandas` aber nicht weiß,
welche Informationen über die Gruppen wir gerne hätten.

[EQ] Beschreiben Sie, was `bezirks_gruppierung.max()` zurückgibt und in welcher Struktur.

Im gleichen Stil lassen sich auch andere Funktionen wie z.b. `min()` oder `mean()` anwenden.
Bei solchen Funktionen handelt es sich um 
[Aggregationsfunktionen](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#aggregation),
die Daten aus den Gruppen auf bestimmte Weisen aggregieren, in Ihrer Dimension also reduzieren.

Wenden Sie eine anonyme Funktion wie `apply(lambda x: x)` auf `bezirks_gruppierung` an,
um die Daten in einer aggregierten Form betrachten zu können
(siehe [PARTREF::pd-Transformationen] für mehr zu `apply()`).
Kurz gesagt weiß `pandas` durch Aggregationen Bescheid, 
welche Informationen Sie über die Gruppen haben wollen.

[ER] Gruppieren Sie nach "Wahlbezirksart" und berechnen Sie die 
durchschnittliche Anzahl gültiger Stimmen.

[ER] `groupby()` lässt aber nicht nur auf eine kategorische Variable filtern. 
Gruppieren Sie `erststimmen_df` nach "Bezirksname" und "Wahlbezirksart" und
betrachten Sie das Ergebnis mit `apply(lambda x: x)`.
Speichern Sie diesen in der Variable `wahlart_df`.

Wenn Sie das Ergebnis betrachten, fällt Ihnen bestimmt der eigenartige Index für die Zeilen auf.
Dadurch, dass Sie nun mehrere Gruppierungskriterien angegeben haben, brauchen wir Gruppen in
den Gruppen.
Der Index hat jetzt quasi mehrere Stufen (_Level_) und wird auch hierarchischer Index oder
[`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex)
genannt mit "Bezirksname" auf der einen Stufe und "Wahlbezirksart" auf der anderen.
So lassen sich auch feingranulare Analysen durchführen, z. B. wie sich Wahlergebnisse je nach
Bezirk und Wahlform unterscheiden.

[EQ] Wie können Sie im Code überprüfen, ob es sich beim Index eines `DataFrame` 
um einen `MultiIndex` oder einen "normalen" Index handelt?

[ER] Wenn Sie auf ein bestimmtes Level zugreifen möchten, dann geben Sie nun statt `loc[IndexWert]`
das Level mit an in einem Tupel `loc[(Level1Wert, Level2Wert)]`.
Geben Sie den Wert für `Friedrichshain-Kreuzberg` auf dem ersten Level und `W` auf dem zweiten Level
aus (von `wahlart_df`).

[ER] Konvertieren Sie den `MultiIndex` mittels 
[`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)
zu einem `Index`.


### `agg()`

[ER] Schauen Sie sich die Dokumentation zu 
[`agg()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html)
an und formulieren Sie `bezirks_gruppierung.max()` so um, dass es `agg()` nutzt.

[ER] Mit `agg()` lassen sich die Gruppierungen noch flexibler nutzen.
Sie können auch mehrere Funktionen gleichzeitig auf die Gruppen anwenden.
Wenden Sie sowohl `min()` als auch `max()` mit `agg()` an.

Nun handelt es sich bei den Spalten um einen `MultiIndex`.

Das `agg()` sehr flexibel ist, sieht man auch daran, dass man Dictionaries übergeben kann,
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

[ER] Man kann offensichtlich auch heterogen aggregieren:
Gruppieren Sie nach "Bezirksname" und "OstWest". 
Aggregieren Sie die Summe der Stimmen für die AfD, das Maximum für die Grünen, 
sowie die durchschnittliche Anzahl an ungültigen Stimmen.

[EQ] Können Sie `reset_index()` auch nutzen, um den _Spaltenindex_ von `MultiIndex` zu einem 
einfachen Index zu konvertieren?


### Gruppieren mit Bedingungen

Ähnlich wie bei [PARTREF::pd-Datenselektion2], kann man auch bei `groupby()` nicht nur Spalten
angeben, sondern auch logische Ausdrücke:
```python
grouped = df.groupby(df['Punkte'] >= 50)  # Beispiel
```

[ER] Gruppieren Sie `erststimmen_df` nach Einträgen, bei denen die AfD mehr Stimmen hatte 
als die Linke.

[EQ] Beschreiben Sie die Struktur des Zeilenindex sprachlich.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::`groupby()` und `agg()` im Wesentlichen verstanden]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
