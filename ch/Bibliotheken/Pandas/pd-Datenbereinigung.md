title: "Bereinigen von Daten"
stage: alpha
timevalue: 1.25
difficulty: 3
explains:
assumes:
requires: pd-Datenaufbereitung
---

[SECTION::goal::experience]
Ich kenne die Verfahren zur Bereinigung von Daten.

Ich kann mit falschen Datentypen und `NaN`-Werten in Pandas umgehen.
[ENDSECTION]


[SECTION::background::default]
Die Datenbereinigung ist eines der wichtigsten Konzepte im Umgang mit Daten, denn ohne eine
qualitativ gute Grundlage an Daten, können auch keine guten Analysen gemacht werden.
[ENDSECTION]


[SECTION::instructions::loose]

Fahren Sie mit dem aufbereiteten `wetter_df` aus der vorherigen Aufgabe fort.

Zur Datenbereinigung gehören verschiedene Verfahren zum Entfernen und Korrigieren 
von Daten.
Die Fehler können beispielsweise aus falschen, veralteten, redundanten, inkonsistenten oder falsch
formatierten Daten bestehen.

Am Ende möchten wir also Daten mit hoher Datenqualität:
- am besten vollständige Daten
- valide Daten: gleicher Datentyp
- einheitliche Daten: gleiche Einheit (z. B. Währung, Gewichtsangabe, Länge)
- integre Daten: Daten müssen vor absichtlicher und/oder unabsichtlicher Manipulation geschützt sein.
(dieser Punkt wird für uns erstmal weniger relevant sein)

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

[EQ] Können Sie sich eine bessere Zahl als Platzhalter vorstellen?
Begründen Sie.

### `NaN`-Werte

Bis jetzt haben wir gekonnt ignoriert, dass `pandas` auf der mathematischen Bibliothek `numpy`
aufbaut.
Doch das wird im Folgenden für Datentypen, aber auch für fehlende Werte sehr hilfreich sein.
`numpy` stellt für uns einen Platzhalter ("Not a Number") für fehlende Werte bereit: `np.nan`

Importieren Sie `numpy` mit `import numpy as np` 

[ER] Machen Sie sich mit der Methode 
[`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace)
vertraut und ersetzen Sie alle fehlenden Messungen mit `np.nan`.

[EQ] Wieso ist es wahrscheinlich besser `NaN` zu verwenden anstatt eines numerischen Wertes?

Mit fehlenden Werten umzugehen, stellt immer eine Herausforderung dar:
Ist es für spätere Analysen besser, Einträge mit fehlenden Werten ganz wegzulassen?
Oder nimmt man in Kauf, unvollständige Daten zu haben, für mehr Informationen in anderen Bereichen?
Füllt man eventuell die fehlenden Werte mit Durchschnitten oder den vorherigen Werten?

Dies und viele andere Abwägungen werden Ihnen in der Data Science immer wieder begegnen. 
Eine allgemeingültige Antwort gibt es auf diese Fragen nicht und muss je nach Einzelfall abgewogen
werden.

Wir werden in diesem Fall, alle Zeilen mit `NaN`-Werten entfernen.

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

[EQ] Warum spielt ein Datum-Datentyp so eine Rolle?
Die beiden Datumsspalten, in ihrer numerischen Form, hätte man auf größer/kleiner als ein bestimmtes
Datum prüfen können?

[ER] Greifen Sie auf die Monatswerte der `MESS_DATUM_BEGINN`-Spalte zu.
Schauen Sie sich dafür den richtigen `Accessor` der `Series` genauer an:
[Series#Accessors](https://pandas.pydata.org/docs/reference/series.html#accessors)

[HINT::Datumsangaben]
Datum-Daten liegen oft in vielen verschiedenen Formen und Varianten vor, oft auch als String.
Auf diese beiden Datumsspalten lassen sich vielleicht Vergleiche und Operationen durchführen.
Wenn aber aus anderen Datenquellen Datumsangaben in anderen Formaten kommen, ist ein einheitliches
Format notwendig.
[ENDHINT]

### Duplikaterkennung

[EQ] Das Erkennen von doppelten Einträgen ist wichtig für eine saubere Datengrundlage. 
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
entfernen, sodass nur eine der beiden Einträge übrig bleibt.
[ENDNOTICE]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
