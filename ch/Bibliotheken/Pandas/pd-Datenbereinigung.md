title: "Bereinigen von Daten"
stage: beta
timevalue: 1.5
difficulty: 3
explains:
assumes: pd-Gruppierung
requires: pd-Datenaufbereitung
---

[SECTION::goal::experience]
Ich kenne Verfahren zur Bereinigung von Daten.

Ich kann mit falschen Datentypen und `NaN`-Werten in Pandas umgehen.

Ich kann fehlende Werte auffüllen und beurteilen, wann das die Ergebnisse verfälscht.
[ENDSECTION]


[SECTION::background::default]
Daten sehen nur selten gleich so aus, wie es für die Verarbeitung nötig oder sinnvoll ist.
In [PARTREF::pd-Datenaufbereitung] haben wir schon strukturelle Anpassungen gemacht.
Oft braucht man aber zusätzlich auch inhaltliche; um die geht es hier.
Mit den bereinigten Daten nehmen wir am Ende die langfristige Temperaturentwicklung in Dahlem unter die Lupe.
[ENDSECTION]


[SECTION::instructions::loose]
Fahren Sie mit dem aufbereiteten `wetter_df` aus [PARTREF::pd-Datenaufbereitung] fort.
Die Spalten nennen wir hier beim ursprünglichen Namen ("die `MO_TT`-Spalte");
benutzen Sie in Ihrem Code Ihre eigenen Spaltennamen.

Zur Datenbereinigung gehören verschiedene Verfahren zum Entfernen und Korrigieren 
von Daten, die falsch, veraltet, redundant, inkonsistent oder ungünstig formatiert sind.

Am Ende möchten wir Daten mit hoher Datenqualität haben, z.B.:

- möglichst vollständige Daten
- homogene Daten: gleicher Datentyp, gleiche Maßeinheit
- konsistente Daten, die bekannte Randbedingungen erfüllen wie `A > B` oder `A*K+B = C`.


### Unvollständige Daten

In [PARTREF::pd-Datenaufbereitung] haben Sie gesehen, dass `-999` im `wetter_df` für fehlende Werte steht.

[EQ] Was halten Sie von dieser Art, fehlende Werte darzustellen?
Nennen Sie einen Vorteil und einen Nachteil.

[EQ] Gibt es eine andere Zahl, die einen besseren Platzhalter darstellt?
Begründen Sie.
<!-- time estimate: 5 min -->


### `NaN`-Werte

Die Verwendung eines festen Zahlenwerts zur Darstellung fehlender Werte ist eine altmodische
und eigentlich seit Jahrzehnten überholte Vorgehensweise.
Wie fast alle modernen Programmiersprachen hat Python einen symbolischen Wert dafür: `math.nan`
(für "[not a number](https://docs.python.org/3/library/math.html#math.nan)", meist abgekürzt "NaN").

Das Gleiche gibt es auch in `numpy`: `np.nan`.
Da Pandas auf NumPy aufbaut, benutzt man üblicherweise den.

Importieren Sie `numpy` mit `import numpy as np`. 

[ER] Machen Sie sich mit der Methode 
[`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace)
vertraut und ersetzen Sie alle fehlenden Messungen mit `np.nan`.

[EQ] Wieso ist es besser, `np.nan` zu verwenden anstatt einer gewöhnlichen Zahl?

[HINT::Mir fehlt ein konkretes Argument]
Vergleichen Sie `mean()` der `MO_RR`-Spalte vor und nach dem Ersetzen.
[ENDHINT]

Mit fehlenden Werten umzugehen, stellt immer eine Herausforderung dar:
Ist es für spätere Analysen besser, Einträge mit fehlenden Werten ganz wegzulassen?
Oder nimmt man in Kauf, unvollständige Daten zu haben, für mehr Informationen in anderen Bereichen?
Füllt man eventuell die fehlenden Werte mit Durchschnitten oder den vorherigen Werten?

Diese und ähnliche Abwägungen werden Ihnen in der Data Science immer wieder begegnen. 
Eine allgemeingültige Antwort gibt es nicht, sondern es muss je nach Einzelfall abgewogen
werden.

Probieren wir zuerst das Weglassen aus.

[ER] Auch dafür bietet Pandas eine Methode:
[`dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna).
Entfernen Sie alle Zeilen mit `NaN`-Werten und speichern Sie das Ergebnis als `wetter_vollst_df`.
Geben Sie explizit die Parameter `axis` und `how` an.

[EQ] Wie viele Zeilen enthält `wetter_vollst_df` noch und mit welchem Monat beginnt es?
Welche Spalte ist hauptsächlich dafür verantwortlich? (`wetter_df.isna().sum()` hilft.)
Wozu wäre `wetter_vollst_df` deshalb unbrauchbar?

Arbeiten Sie im Folgenden mit dem vollständigen `wetter_df` weiter.
<!-- time estimate: 15 min -->


### Datums-Werte

Sie haben schon kurz den `dtype` kennengelernt, den Datentyp, den die Werte in einer Spalte haben.

[EQ] Welchen Datentyp haben `MESS_DATUM_BEGINN` und `MESS_DATUM_ENDE`?

[HINT::Wie finde ich den `dtype` heraus?]
Jede `Series` besitzt das Attribut `dtype`.
Alternativ können Sie den `dtype` aller Spalten mit `info()` überblicken.
[ENDHINT]

[ER] Es gibt einen Datentyp, der für Datumswerte gedacht ist.
Nutzen Sie
[`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime),
um die beiden Datumsspalten zu diesem Typ zu konvertieren. 
Der `format`-Parameter spielt für die Konvertierung eine entscheidende Rolle.
Prüfen Sie das Ergebnis: Der erste Wert von `MESS_DATUM_BEGINN` muss im Januar 1719 liegen.

[EQ] Warum brauchen wir einen Datum-Datentyp und lassen die Werte nicht einfach als Zahlen oder Strings?

[HINT::Mir fällt kein Grund ein]
Wie viele Tage liegen zwischen dem 31.1.1719 und dem 1.2.1719?
Was ergibt `17190201 - 17190131`?
Und wie würden Sie aus `17190201` den Monat gewinnen?
[ENDHINT]

Der neue Datentyp macht zum Beispiel den mittleren Jahresgang leicht berechenbar,
also die Durchschnittstemperatur jedes Kalendermonats über alle Jahre.
Wir brauchen ihn nachher als Vergleichswert.

[ER] Ermitteln Sie aus der `MESS_DATUM_BEGINN`-Spalte den Monat mit dem passenden
[Accessor der `Series`](https://pandas.pydata.org/docs/reference/series.html#accessors).
Gruppieren Sie `wetter_df` damit und berechnen Sie den Mittelwert der `MO_TT`-Spalte je Monat.
Speichern Sie das Ergebnis als `jahresgang`.
Zur Kontrolle: Der Juli liegt bei rund 18,7 °C, der Januar bei rund -0,6 °C.
<!-- time estimate: 15 min -->


### Duplikaterkennung

Das Erkennen von doppelten Einträgen ist wichtig für eine saubere Datengrundlage,
denn in vielen Situationen ergeben doppelte Einträge keinen Sinn, sondern stellen Fehler dar. 
In Pandas funktioniert das sehr einfach mit
[`duplicated()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated).

[EQ] Wie viele Duplikate enthält `wetter_df`?

[ER] `duplicated()` prüft, ob alle Werte eines Eintrages gleich sind.
Für uns sollte es aber schon als Duplikat zählen, falls es für einen Monat mehrfache Einträge gibt.
Erweitern Sie den Ausdruck, sodass geprüft wird, ob es für `MESS_DATUM_BEGINN` und `MESS_DATUM_ENDE`
Duplikate gibt.

Da `wetter_df` keine Duplikate enthält, sehen Sie hier noch keinen Unterschied.
Der folgende `test_df` enthält einen Monat zweimal, aber mit einem abweichenden Wert:
```python
test_df = wetter_df.iloc[[0, 1, 1, 2]].copy()
test_df.iloc[2, -1] = 0
```

[ER] Wenden Sie beide Ausdrücke auf `test_df` an.
Der erste muss 0 Duplikate finden, der zweite 1.

[NOTICE]
Sie können duplizierte Einträge, falls vorhanden, mit
[`drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates)
entfernen, sodass nur einer davon übrig bleibt.
[ENDNOTICE]
<!-- time estimate: 10 min -->


### Fehlende Werte auffüllen

Statt Zeilen wegzulassen, kann man fehlende Werte auch durch Schätzwerte ersetzen.
Das nennt man _Imputation_.
In der `MO_TT`-Spalte fehlt seit 1719 nur ein einziger Wert: März 2025.

[ER] Erzeugen Sie zwei aufgefüllte Fassungen der `MO_TT`-Spalte:
`mo_tt_mittel` mit
[`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html)
und dem Mittelwert der Spalte sowie `mo_tt_interpoliert` mit
[`interpolate()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html).
Geben Sie in beiden den Wert für März 2025 aus.

[EQ] Welcher der beiden Werte ist plausibler?
Vergleichen Sie mit dem März in `jahresgang` und mit den Märzwerten der Jahre 2015 bis 2024.
Woran liegt der Unterschied zwischen den beiden Verfahren?

[ER] Weisen Sie `mo_tt_interpoliert` der `MO_TT`-Spalte von `wetter_df` zu.
<!-- time estimate: 15 min -->


### Die Temperaturentwicklung seit 1719

Monatswerte schwanken jahreszeitlich viel zu stark, um darin einen langfristigen Trend zu erkennen.
Deshalb bildet man Jahresmittel und glättet diese über 30 Jahre, die in der Klimatologie übliche Zeitspanne.

Für Jahresmittel muss ein Jahr aber vollständig sein, und das ist nicht immer der Fall:
Manche Monate fehlen in der Datei ganz, also ohne `-999` und ohne `NaN`, die Jahre 1722 bis 1727 zum Beispiel.

[ER] Gruppieren Sie die `MO_TT`-Spalte nach dem Jahr und berechnen Sie mit `mean()` die Jahresmittel
und mit `count()` die Anzahl der Monatswerte pro Jahr.

[EQ] Welche Jahre haben weniger als 12 Monatswerte?
Was stimmt deshalb am Jahresmittel von 1729 nicht?

[ER] Schreiben Sie eine Funktion `klimareihe(spalte)`, die für eine übergebene `Series`
die Jahresmittel aller vollständigen Jahre bildet und deren gleitenden 30-Jahre-Durchschnitt liefert.
Dieser entsteht aus den Jahresmitteln mit
[`rolling(30)`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html)`.mean()`:
Jeder Wert ist der Mittelwert des jeweiligen Jahres und der 29 vorherigen Zeilen,
und für die ersten 29 Zeilen ergibt sich `NaN`.
Speichern Sie das Ergebnis für die `MO_TT`-Spalte als `klima_tt` und geben Sie es für diese Jahre aus:
```python
jahre = [1775, 1800, 1825, 1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025]
print(klima_tt.loc[jahre])
```
Zur Kontrolle: Der Wert für 2025 liegt bei rund 10,1 °C.

[HINT::Wie wähle ich nur die vollständigen Jahre aus?]
Die Ergebnisse von `mean()` und `count()` haben denselben Index.
Bilden Sie aus `count()` einen logischen Ausdruck und selektieren Sie damit die Jahresmittel.
[ENDHINT]

[EQ] Beschreiben Sie den Verlauf von `klima_tt`.
Um wie viel Grad ist der Wert von 1975 bis 2025 gestiegen?
Welche Einschränkung hat eine Aussage, die auf nur einer Wetterstation beruht?
<!-- time estimate: 20 min -->


### Auffüllen im großen Stil

Für die Minimumtemperatur (`MO_TN`) sieht die Lage schlechter aus: Vor 1830 fehlen alle Werte.
Wir wollen aber auch diese Spalte über den ganzen Zeitraum auswerten.
Füllen wir die Lücken also wieder mit dem Mittelwert auf, der bleibt dabei ja immerhin unverändert.

[ER] Erzeugen Sie so `mo_tn_gefuellt` und geben Sie `klimareihe(mo_tn_gefuellt)` für die obigen Jahre aus.
Zählen Sie außerdem die Zeilen, in denen die Minimumtemperatur über der mittleren Temperatur (`MO_TT`) liegt,
einmal mit `mo_tn_gefuellt` und einmal mit der unveränderten `MO_TN`-Spalte.

[EQ] Warum ist dieses Auffüllen hier Unfug?
Nennen Sie mindestens zwei Beobachtungen aus Ihren Ergebnissen.
Was wäre der bessere Umgang mit diesen Lücken?
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
