title: "Mit mehreren Datensätzen arbeiten"
stage: beta
timevalue: 1.5
difficulty: 3
assumes: pd-Datenbereinigung, pd-Transformationen
---

[SECTION::goal::idea]
Ich verstehe, wie ich unterschiedliche Datensätze aneinander angleichen kann, sodass
ich mit beiden auf die gleiche Weise weiterarbeiten kann.
[ENDSECTION]


[SECTION::background::default]
Oft muss man mit Daten aus mehreren Quellen arbeiten oder sie vergleichen.
Solche Daten liegen oft nicht in gleicher Struktur vor, weshalb man sie zuerst anpassen muss.
[ENDSECTION]


[SECTION::instructions::detailed]
Für diese Aufgabe verwenden Sie sowohl die Daten der Wetterstation Dahlem als auch die Daten
der österreichischen Wetterstation "Aigen im Ennstal".

Wetterstation Dahlem: Wie in [PARTREF::pd-Datenaufbereitung] beschrieben.  
Wetterstation Aigen:
<!-- @LINK_SPEC: status=405 -->
[Download der ausgewählten Monatsdaten](https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1m?parameters=vv_mittel%2Cvv_mittel_flag%2Ctlmax%2Ctlmin%2Ctl_mittel%2Ctlmax_mittel%2Ctlmin_mittel&start=1963-01-01T00%3A53%3A00.000Z&end=2024-12-01T00%3A00%3A00.000Z&station_ids=2&output_format=csv&filename=AigenEnnstal_196301_202412).
Die Daten stammen von
[GeoSphere Austria](https://dataset.api.hub.geosphere.at/app/frontend/station/historical/klima-v2-1m).
Die Bedeutung der Spalten steht in der
<!-- @LINK_SPEC: status=405 -->
[Metadatenbeschreibung](https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1m/metadata/parameters?filename=Messstationen+Monatsdaten+v2+Parameter-Metadaten).

Laden Sie die beiden Datensätze wie folgt aus Ihrem [TERMREF::Hilfsbereich]:
```python
wetter_df_dahlem = pd.read_table("pfad/zur/dahlem.txt", sep=';', encoding='latin')
wetter_df_aigen = pd.read_csv("pfad/zur/aigen.csv", encoding='latin')
```

Unser Ziel ist es, die Lufttemperaturen über die Zeit zu vergleichen.
Machen Sie sich daher zuerst mit der Beschreibung der bereitgestellten Felder in der CSV-Datei
vertraut.
<!-- time estimate: 10 min -->


### Fehlende Daten

[EQ] Schauen Sie sich die CSV-Datei an.
Wie werden fehlende Daten im Gegensatz zu den Dahlem-Daten dargestellt?

[HINT::Ich finde in der CSV-Datei keine fehlenden Daten]
Davon gibt es nur sehr wenige.
Sehen Sie sich im Editor die Zeile für März 1964 an.
[ENDHINT]

[EQ] Schauen Sie sich nun an, wie diese Darstellung im `wetter_df_aigen` interpretiert wird.
Sind noch weitere Umformungen nötig, um fehlende Daten im `DataFrame` als `NaN` darzustellen?

[ER] Ersetzen Sie wie in [PARTREF::pd-Datenbereinigung] die fehlenden Daten durch `NaN`,
in `wetter_df_dahlem` und falls nötig auch in `wetter_df_aigen`.
Entfernen Sie dabei keine Zeilen (also kein `dropna()`), sonst passen die beiden Datensätze später
nicht mehr zusammen.
<!-- time estimate: 15 min -->


### Datumswerte

[ER] Wandeln Sie in beiden Datensätzen die Spalte, die den Beginn des Messzeitraums angibt,
in eine `datetime`-Spalte um: `MESS_DATUM_BEGINN` bzw. `time`.
Prüfen Sie das Ergebnis: Der erste Wert in `wetter_df_dahlem` muss im Januar 1719 liegen.

[HINT::Meine Dahlem-Daten liegen alle im Jahr 1970]
Die Spalte enthält ganze Zahlen wie `17190101`.
Ohne weitere Angabe liest `to_datetime()` solche Zahlen als Nanosekunden seit dem 1.1.1970.
Den nötigen Parameter kennen Sie aus [PARTREF::pd-Datenbereinigung].
[ENDHINT]

Wenn Sie nun aber mit dem Attribut `dtype` den Typ der beiden Spalten vergleichen, werden Sie
feststellen, dass diese nicht gleich sind:
```
datetime64[us]
datetime64[us, UTC]
```

Das liegt daran, dass die eine Spalte "timezone-naive", also ohne Zeitzone, arbeitet
und die andere "timezone-aware", also mit Zeitzone.
Eine der Stolperfallen bei der Arbeit mit `datetime`!

[EQ] Schauen Sie in die Dokumentation von
[`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime)
und nennen Sie den Parameter, mit dem Sie dafür sorgen können, dass beide Spalten die Zeitzone UTC haben.

[ER] Wandeln Sie beide Spalten mit diesem Parameter um.
Prüfen Sie mit `dtype`, dass sie jetzt denselben Typ haben.
<!-- time estimate: 20 min -->


### Vergleichbare Spalten

[EQ] Beide Datensätze enthalten mehrere Spalten zur Lufttemperatur in 2m Höhe.
Doch welche davon sind jetzt wirklich miteinander vergleichbar?
Zählen Sie diese auf.

[HINT::Ich weiß nicht, welche Spalten ich vergleichen soll]
In `wetter_df_dahlem` kommen `MO_TT`, `MO_TN`, `MO_TX`, `MX_TN` und `MX_TX` infrage.
Vergleichen Sie deren Beschreibung in der Datensatzbeschreibung des DWD mit der
Metadatenbeschreibung der Spalten von `wetter_df_aigen`.
[ENDHINT]

[ER] Entfernen Sie mit 
[`drop()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)
alle Spalten aus `wetter_df_aigen`, die nicht für unseren Temperaturvergleich relevant sind.

[ER] Benennen Sie die restlichen Spalten so um, dass sie den gleichen Namen haben wie die 
vergleichbaren Spalten in `wetter_df_dahlem`.

[NOTICE]
Sie können dafür
[`rename()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename)
benutzen.
[ENDNOTICE]
<!-- time estimate: 15 min -->


### Vergleichbare Zeiträume 

Jetzt gibt es jedoch noch ein Problem:
`wetter_df_dahlem` enthält einen deutlich längeren Zeitraum der Messungen.

[ER] Passen Sie `wetter_df_dahlem` so an, 
dass es nur Daten aus dem gleichen Zeitraum enthält wie `wetter_df_aigen`.

[EQ] Bilden Sie nun die Differenz der beiden `MO_TT`-Spalten und sehen Sie sich das Ergebnis an.
Was fällt Ihnen auf?
Erklären Sie das Ergebnis mithilfe des Abschnitts über
[Rechnen mit `Series` und die Ausrichtung nach Index-Labels](https://pandas.pydata.org/docs/user_guide/dsintro.html#vectorized-operations-and-label-alignment-with-series).

[ER] Sorgen Sie mit
[`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html)
dafür, dass `wetter_df_dahlem` den gleichen Index hat wie `wetter_df_aigen`.
Der alte Index soll dabei nicht als neue Spalte erhalten bleiben;
den passenden Parameter finden Sie in der Dokumentation.

[ER] Der neue Index paart die Zeilen jetzt einfach nach ihrer Position.
Das ist nur richtig, wenn beide Datensätze dieselben Monate in derselben Reihenfolge enthalten.
Prüfen Sie das mit einem Vergleich der beiden `MESS_DATUM_BEGINN`-Spalten, der genau einen bool-Wert liefert.

[HINT::Wie mache ich aus dem zeilenweisen Vergleich einen einzigen Wert?]
`==` liefert für zwei `Series` wieder eine `Series` mit bool-Werten.
Die lässt sich mit
[`all()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html)
zusammenfassen.
[ENDHINT]
<!-- time estimate: 15 min -->


### Vergleiche

[ER] Schreiben Sie den Code, der die Werte für die folgenden drei Fragen berechnet.

[EQ] Bei welcher der zwei Stationen war es durchschnittlich kälter (`MO_TT`)?

[EQ] Gibt es Monate, in denen es an einer Station im Monatsmittel (`MO_TT`) um mindestens 10 Grad Celsius
kälter oder wärmer war als an der anderen?
Benennen Sie diese.

[EQ] An welcher Station wurde die höchste Temperatur (im Monatsmittel) gemessen und wie viel Grad
waren das?
<!-- time estimate: 10 min -->


### Einheiten anpassen

[ER] Mal angenommen, die Spalte `MO_TT` wäre in `wetter_df_aigen` nicht in Celsius,
sondern in Fahrenheit angegeben.
Rechnen Sie sie mit `apply()` und der Formel `T_C = 5/9 * (T_F - 32)` nach Celsius um.
Speichern Sie das Ergebnis in einer neuen Variable `mo_tt_celsius`,
denn in Wirklichkeit ist die Spalte schon in Celsius und muss so bleiben.

[EQ] Die gleiche Umrechnung geht auch ohne `apply()`.
Wie?
Warum ist das hier die bessere Lösung?
<!-- time estimate: 5 min -->
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]