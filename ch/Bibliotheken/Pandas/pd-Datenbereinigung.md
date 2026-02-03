title: "Bereinigen von Daten"
stage: alpha
timevalue: 1.25
difficulty: 3
explains:
assumes:
requires: pd-Datenaufbereitung
---

[SECTION::goal::experience]
Ich kenne Verfahren zur Bereinigung von Daten.

Ich kann mit falschen Datentypen und `NaN`-Werten in Pandas umgehen.
[ENDSECTION]


[SECTION::background::default]
Daten sehen nur selten gleich so aus, wie es für die Verarbeitung nötig oder sinnvoll ist.
In [PARTREF::pd-Datenaufbereitung] haben wir schon strukturelle Anpassungen gemacht.
Oft braucht man aber zusätzlich auch inhaltliche; um die geht es hier.
[ENDSECTION]


[SECTION::instructions::loose]
Fahren Sie mit dem aufbereiteten `wetter_df` aus [PARTREF::pd-Datenaufbereitung] fort.

Zur Datenbereinigung gehören verschiedene Verfahren zum Entfernen und Korrigieren 
von Daten, die falsch, veraltet, redundant, inkonsistent oder ungünstig formatiert sind.

Am Ende möchten Daten mit hoher Datenqualität haben, z.B.:
- möglichst vollständige Daten
- homogene Daten: gleicher Datentyp, gleiche Maßeinheit
- konsistente Daten, die bekannte Randbedingungen erfüllen wie `A > B` oder `A*K+B = C`.


### Unvollständige Daten

[EQ] Woran erkennen Sie im `wetter_df` unvollständige Daten?

[EQ] Was halten Sie von dieser Art, fehlende Arten darzustellen?
Nennen Sie einen Vorteil und einen Nachteil.

[HINT::Vor- und Nachteil an Darstellung fehlender Daten]
Jeder fehlende Wert wird als `-999` dargestellt. 
Zu verwechseln ist sie mit richtigen Messwerten daher nicht 
(z.B. wird Temperatur nie -999 Grad Celsius sein). 

Was aber passiert, wenn Sie z.B. die Durchschnittstemperatur über einen Zeitraum berechnen wollen?
Was für einen Effekt haben dann die fehlenden Werte?
[ENDHINT]

[EQ] Gibt es eine andere Zahl, die einen besseren Platzhalter darstellt?
Begründen Sie.


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

[EQ] Wieso ist es besser `np.nan` zu verwenden anstatt eines numerischen Wertes?

Mit fehlenden Werten umzugehen, stellt immer eine Herausforderung dar:
Ist es für spätere Analysen besser, Einträge mit fehlenden Werten ganz wegzulassen?
Oder nimmt man in Kauf, unvollständige Daten zu haben, für mehr Informationen in anderen Bereichen?
Füllt man eventuell die fehlenden Werte mit Durchschnitten oder den vorherigen Werten?

Diese und ähnliche Abwägungen werden Ihnen in der Data Science immer wieder begegnen. 
Eine allgemeingültige Antwort gibt es nicht, sondern es muss je nach Einzelfall abgewogen
werden.

Wir werden nun alle Zeilen mit NaN-Werten entfernen.

[ER] Auch dafür bietet Pandas eine Methode:
[`dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna)
Geben Sie explizit die `axis` und `how` Parameter an.


### Datums-Werte

Sie haben schon kurz den `dtype` kennengelernt, den Datentyp, den die Werte in einer Spalte haben.

[EQ] Welchen Datentyp haben `MESS_DATUM_BEGINN` und `MESS_DATUM_ENDE`?

[HINT::`dtype` herausfinden]
Jede `Series` besitzt das Attribut `dtype`.
Alternativ können Sie den `dtype` aller Spalten mit `info()` überblicken.
[ENDHINT]

[ER] Es gibt einen Datentyp, der für Datumswerte gedacht ist. Nutzen Sie
[`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime),
um die beiden Datumsspalten zu diesem Typen zu konvertieren. 
Der `format`-Parameter spielt für die Konvertierung eine entscheidende Rolle.

[EQ] Warum brauchen wir einen Datum-Datentyp und nutzen nicht einfach Strings?

[HINT::Wie sähen Datumsstrings aus?]
Wie schreibt man ein Datum in Deutschland? Wie in USA?
[ENDHINT]

[ER] Greifen Sie auf die Monatswerte der `MESS_DATUM_BEGINN`-Spalte zu.
Schauen Sie sich dafür den richtigen `Accessor` der `Series` genauer an:
[Series#Accessors](https://pandas.pydata.org/docs/reference/series.html#accessors)


### Duplikaterkennung

[EQ] Das Erkennen von doppelten Einträgen ist wichtig für eine saubere Datengrundlage,
denn in vielen Situationen ergeben doppelte Einträge keinen Sinn, sondern stellen Fehler dar. 
In Pandas funktioniert das sehr einfach mit
[`duplicated()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated).
Finden Sie heraus, wie viele Duplikate enthalten sind.

[ER] `duplicated()` prüft, ob alle Werte eines Eintrages gleich sind.
Für uns sollte es aber schon als Duplikat zählen, falls es für einen Monat mehrfache Einträge gibt.
Erweitern Sie den Ausdruck, sodass geprüft wird, ob für "MESS_DATUM_BEGINN" und "MESS_DATUM_ENDE"
Duplikate gibt.

[NOTICE]
Sie können duplizierte Einträge, falls vorhanden, mit
[`drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates)
entfernen, sodass nur einer davon übrig bleibt.
[ENDNOTICE]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
