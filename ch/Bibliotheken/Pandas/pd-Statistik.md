title: "Deskriptive Statistik in Pandas"
stage: alpha
timevalue: 1
difficulty: 2
requires: pd-Datenselektion
assumes: pd-Datenüberblick
---

[SECTION::goal::idea]
Ich kann verschiedene deskriptive Kennzahlen in Pandas berechnen und interpretieren.
Ich verstehe die Unterschiede zwischen Lagemaßen und Streuungsmaßen und wann welche Kennzahlen
sinnvoll eingesetzt werden.
[ENDSECTION]


[SECTION::background::default]
Die deskriptive Statistik hilft uns, große Datenmengen durch aussagekräftige Kennzahlen
zur Verteilung zu charakterisieren. Man unterscheidet dabei vor allem zwischen:    
- Lagemaßen (Mittelwert, Median, Modus), die die Mitte einer Verteilung beschreiben           
- Streuungsmaßen (Varianz, Standardabweichung), die die Variation der Daten um die Mitte angeben       
[ENDSECTION]


[SECTION::instructions::loose]
Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) 
wie gewohnt in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

In [PARTREF::pd-Datenüberblick] haben Sie mit `describe()` eine Übersicht über die wichtigsten
statistischen Kennzahlen eines DataFrames kennengelernt. Doch was bedeuten diese Werte
eigentlich, und wann sind sie aussagekräftig?

### Lagemaße verstehen und anwenden (`mean()`, `median()`, `mode()`)

Lagemaße helfen uns, die "typischen" Werte in einem Datensatz zu identifizieren.
Das bekannteste Lagemaß ist der Mittelwert (Durchschnitt), aber er ist nicht immer
das aussagekräftigste Maß.

[EQ] Mit 
[`mean()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html) (Durchschnitt)
[`median()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html) (Median) 
und [`mode()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html) (Modus)
können Sie diese Kennzahlen für `Series` berechnen.
Lesen Sie Dokumentation und probieren Sie diese aus, falls nötig, um zu verstehen, wie sich diese
Kennzahlen ergeben.
Beschreiben Sie bei jeder kurz, wie sich diese ergibt.

[EQ] Wieso wird der Median oft als aussagekräftiger bezeichnet als der Durchschnitt?

[EQ] Sie können diese Methoden nicht nur auf eine `Series` sondern auch auf 
ein `DataFrame` anwenden.
Testen Sie dies mit `erststimmmen_df`. Was wird zurückgegeben?

[NOTICE]
Diese Methoden können nur auf numerische Spalten angewendet werden.
Beim Benutzen auf das ganze `erststimmen_df` muss deshalb `numeric_only=True` in den Parametern 
gesetzt werden, um nichtnumerische Spalten auszuschließen.
[ENDNOTICE]

[EQ] Finden Sie den Modus der Bezirksnummern.
Was sagt das über die Wahlbezirke aus?

### Streuungsmaße interpretieren (`std()`, `var()`)

Lagemaße allein geben kein vollständiges Bild. 
Zwei Datensätze können denselben Mittelwert haben, sich aber stark darin unterscheiden, 
wie stark die Werte um diesen Mittelwert streuen. 
Deshalb ist es wichtig, die *Streuungsmaße* zu betrachten.

[EQ] Beschreiben Sie knapp, was die Varianz 
([`var()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html))
misst bzw. was man daran ablesen kann.
[HREF::https://de.wikipedia.org/wiki/Varianz]

Die Standardabweichung ist definiert als die Wurzel aus der Varianz.
Die Varianz hat quadrierte Einheiten, was schwer zu interpretieren ist.
Die Standardabweichung hingegen hat die gleichen Einheiten wie die Originaldaten, 
was sie intuitiver macht.

[ER] Berechnen Sie die Standardabweichung der SPD-Stimmen mit 
[`std()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html) und 
geben Sie diese an.

[EQ] Betrachten Sie zusätzlich zur Standardabweichung den Median der SPD-Stimmen.
Nennen Sie diese und begründen Sie, ob Sie denken, dass die Werte stark streuen, gemessen
an den beiden Kennzahlen.

### Extremwerte und ihre Position (`min()`,`idxmin()`,`max()`,`idxmax()`)

Oft interessieren uns nicht nur die Durchschnittswerte, sondern auch die Extremwerte
und wo sie auftreten.
Dabei sollte Ihnen Minimum 
[`min()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html)
und Maximum 
[`max()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html)
ein Begriff sein.

Mit 
[`idxmin()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html)
und 
[`idxmax()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
können Sie die *Positionen* dieser Minimal- und Maximalwerte finden.

[ER] Finden Sie die Zeilenindizes der Wahlbezirke mit den geringsten und meisten
Grünen-Stimmen.

[ER] Kombinieren Sie `idxmax()` mit `loc[]`, um die gesamte Zeile mit den meisten
Grünen-Stimmen auszugeben. 

Deskriptive Statistiken sind der erste Schritt in jeder Datenanalyse. Sie helfen,
Muster und Besonderheiten in den Daten zu erkennen, die dann mit komplexeren
statistischen Methoden weiter untersucht werden können.
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]