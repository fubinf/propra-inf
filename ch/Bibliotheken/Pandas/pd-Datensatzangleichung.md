title: "Mit mehreren Datensätzen arbeiten"
stage: draft
timevalue: 1.5
difficulty: 2
requires: pd-Datenbereinigung
---

[SECTION::goal::idea]
Ich verstehe, wie ich unterschiedliche Datensätze aneinander angleichen kann, sodass
ich mit beiden weiterarbeiten kann.
[ENDSECTION]


[SECTION::background::default]
Oft muss man mit Daten aus mehreren Quellen arbeiten oder sie vergleichen.
Solche Daten sind liegen oft nicht in gleicher Struktur vor, wehsalb man sie zuerst anpassen muss.
[ENDSECTION]


[SECTION::instructions::detailed]
Für diese Aufgabe werden Sie sowohl die Daten der Wetterstation Dahlem als auch die Daten
der österreichischen Wetterstation "Aigen im Ennstal" verwenden.

Wetterstation Dahlem: Wie in [PARTREF::pd-Datenaufbereitung] beschrieben.  
Wetterstation Aigen: Finden Sie [hier](https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1m?parameters=vv_mittel%2Cvv_mittel_flag%2Ctlmax%2Ctlmin%2Ctl_mittel%2Ctlmax_mittel%2Ctlmin_mittel&start=1963-01-01T00%3A53%3A00.000Z&end=2024-12-01T00%3A00%3A00.000Z&station_ids=2&output_format=csv&filename=AigenEnnstal_196301_202412).
Dies ist der Download für die ausgewählten Daten, die Website die das bereitstellt ist 
[GeoSphere Austria](https://dataset.api.hub.geosphere.at/app/frontend/station/historical/klima-v2-1m).
Die Metadatenbeschreibung finden Sie 
[hier](https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1m/metadata/parameters?filename=Messstationen+Monatsdaten+v2+Parameter-Metadaten).

Laden Sie die beiden Datensätze wie folgt in Ihre Umgebung:
```python
wetter_dahlem_df = pd.read_table("pfad/zur/dahlem.txt", sep=';', encoding='latin')
wetter_aigen_df = pd.read_csv("pfad/zur/aigen.csv", encoding='latin')
```

Unser Ziel ist es, die Lufttemperaturen über die Zeit zu vergleichen.
Machen Sie sich daher zuerst mit der Beschreibung der bereitgestellten Felder in der CSV-Datei
vetraut.

### Fehlende Daten

[EQ] Schauen Sie sich die CSV-Datei an.
Wie werden fehlende Daten im Gegensatz zu den Dahlem-Daten dargestellt?

[EQ] Schauen Sie sich nun an, wie diese Darstellung im `wetter_aigen_df` interpretiert wird.
Brauchen Sie noch weitere Umformungen zu machen, um fehlende Daten im `DataFrame` als `NaN`
darzustellen?

Stellen Sie wie in [PARTREF::pd-Datenbereinigung] fehlende Daten durch `NaN` dar, sowohl in
`wetter_dahlem_df` als auch in `wetter_aigen_df` falls nötig.


### Datumswerte

[ER] Wandeln Sie in beiden `DataFrames` die Spalten, die den Messzeitraum angeben in `datetime`-
Spalten um.

Wenn Sie nun aber die beiden mit `type()` den Typ der beiden Spalten vergleichen, werden Sie
feststellen, dass diese nicht gleich sind:
```
dtype: datetime64[ns]
dtype: datetime64[ns, UTC]
```

Das liegt daran, dass die eine Spalte "timezone-naive" also ohne
Zeitzone arbeiten und die andere "timezone-aware" also mit Zeitzone arbeitet.
Eine der Stolperfallen bei der Arbeit mit `datetime`!

[EQ] Schauen Sie in die Dokumentation von
[`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
und nennen Sie wie und mit welchem Parameter Sie dafür sorgen können, dass beide Spalten im
UTC-Format sind.

### Vergleichbare Spalten

[EQ] Beide `DataFrames` enthalten mehrere Spalten zur Lufttemperatur in 2m Höhe.
Doch welche davon sind jetzt wirklich miteinander vergleichbar?
Zählen Sie diese auf.

[HINT::Relevante Spalten]
Schauen Sie sich die Metadatenbeschreibung zu diesen Spalten genauer an und vergleichen Sie die
mit den Spaltenbeschreibungen aus `wetter_aigen_df`:
"MO_TT", "MO_TN", "MO_TX", "MX_TN", "MX_TX"
[ENDHINT]

[ER] Entferne mit 
[`drop()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)
alle Spalten aus `wetter_aigen_df`, die nicht für unseren Temperaturvergleich relevant sind.

[ER] Bennenen Sie die restlichen Spalten so um, dass sie den gleichen Namen haben, wie die 
vergleichbaren Spalten in `wetter_dahlem_df`.

[NOTICE]
Sie können dafür
[`rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename)
benutzen.
[ENDNOTICE]

### Vergleichbare Zeiträume 

Jetzt gibt es jedoch noch ein Problem:
Das `wetter_dahlem_df` enthält einen deutlich längeren Zeitraum der Messungen.

[ER] Passe das `wetter_dahlem_df` so an, dass es nur Daten aus dem gleichen Zeitraum enthält, wie
`wetter_aigen_df`.
Vergessen Sie nicht die Indizes auch anzugleichen (`reset_index()`)!

### Vergleiche

[EQ] Bei welchen der zwei Stationen war es durchschnittlich kälter?

[EQ] Berechnen Sie die Differenz der mittleren Temperaturen.
Gibt es Monate, in denen es an einer Station durchschnittlich 10 Grad Celsius kälter oder wärmer
war als an der anderen?
Benennen Sie diese.

[EQ] An welcher Station wurde die höchste Temperatur (im Monatsmitttel) gemessen und wie viel Grad
waren das?

### Einheiten Anpassen

[ER] Mal angenommen das Monatsmittel der Tagesmittel wäre in  `wetter_aigen_df`
nicht in Celsius, sondern in Fahrenheit angegeben.
Wie könnten Sie diese mittels `apply()` angleichen?
Die Umrechnungsformel lautet: `T_C = 5/9 * (T_F - 32)`
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]