title: "Auswahl von Datensatz-Teilen in Pandas"
stage: beta
timevalue: 1.5
difficulty: 2
assumes: pd-Datenstrukturen
explains: Slicing (Python)
---

[SECTION::goal::idea]
Ich kann gezielt Teilbereiche eines `DataFrame` auswählen.

Ich verstehe, was Slices sind und wie ihre Notation aussieht.
[ENDSECTION]


[SECTION::background::default]
In der Praxis führt man selten Analysen oder Transformationen auf allen Daten eines Datensatzes
durch. 
Oft möchte man nur Teilbereiche auswählen, bearbeiten oder analysieren. 
Hierzu bietet Pandas verschiedene Methoden an.
[ENDSECTION]


[SECTION::instructions::loose]
Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis)
wie in
[PARTREF::pd-Einführung] beschrieben in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```

### Spaltenzugriff: `dataframe[[spaltenindex, spaltenindex]]`

Stellen Sie sich vor, Sie wollen die Stimmen für die CDU mit der Anzahl der gültigen Stimmen 
in jedem Wahlbezirk vergleichen. 
In diesem Fall interessieren sie sich für zwei oder drei der 41 Spalten. 
Es wäre sehr praktisch, wenn man diese Spalten exakt auswählen könnte.

Um auf eine Spalte aus einem `DataFrame` zuzugreifen, haben Sie bereits gelernt, dass Sie per Label
der Spalten (also per Index) darauf zugreifen können: `dataframe["spaltenname"]`.
Hierbei nutzen Sie den Index-Operator `[]`.
Sie können aber auch eine Liste an Spaltennamen an diesen Operator übergeben, 
für die Spalten, die Sie auswählen möchten: `dataframe[["spaltenname 1", "spaltenname 2"]]`

[ER] Wählen Sie den Wahlbezirk, die gültigen Stimmen und die Stimmen der CDU mit
dieser Methode aus und geben Sie sie aus.

[EQ] Eine andere Schreibweise für `dataframe["spaltenname"]` ist der Syntax `dataframe.spaltenname`.
Dieser Syntax wird jedoch beim sauberen Programmieren vermieden. 
Überlegen Sie, welche Probleme es mit diesem Syntax geben könnte.

[HINT::Syntax-Probleme] 
Überlegen Sie die Probleme am Beispiel der vorherigen Aufgabe:

- Könnten Sie die Spalte "Gültige Stimmen" auf diese Weise ansprechen?
- Können Sie auf diese Weise auch mehrere Spalten ansprechen?
- Was passiert, wenn eine Spalte einen Namen hat, der die gleiche Schreibweise hat wie ein Attribut
  oder eine Methode des `DataFrame`, zum Beispiel eine Spalte mit dem Namen "columns"?
[ENDHINT]


### Zeilenzugriff und Slicing: `dataframe[zeilenindex:zeilenindex]`

Mit dem gleichen Index-Operator `[]` auf einem `DataFrame` lassen sich statt Spalten auch Zeilen
auswählen.
Das geht aber nur mit sogenanntem [TERMREF::Slicing (Python)].

Mit Slicing kann man durch die Angabe von Startindex, Endindex und einer Schrittlänge einen
bestimmten Bereich auf Sequenz-Datenstrukturen auswählen: `dataframe[start:end:step]`
Sie haben Slicing eventuell schon im Kontext von Python-Listen gesehen, wie zum Beispiel: 
`liste[0:5]` oder `liste[::2]`.
Das erste Beispiel hätte hier alle Elemente von Index 0 bis Index 5 ausgewählt,
das zweite Beispiel hätte jedes zweite Element ausgewählt.

Wenden Sie dieses Slicing jedoch auf ein DataFrame an, 
_dann werden nicht wie erwartet die Spalten, sondern die Zeilen angesprochen!_
Während bei Listen Slicing und Indexing immer dieselbe (einzige) Dimension betroffen ist,
unterscheidet Pandas bei einem `DataFrame` also je nach Zugriffsmethode zwischen Zeilen und Spalten.
Dieses Verhalten kann anfangs verwirrend sein; bitte behalten Sie folgendes im Kopf:

- `dataframe[index_a]` wählt eine Spalte aus
- `dataframe[[index_a,index_b]]` wählt mehrere Spalten aus
- `dataframe[index_a:index_b]` wählt einen Bereich von Zeilen aus

[ER] Wählen Sie die Zeilen von Index 0 bis Index 10 des `erststimmen_df` aus.

[EQ] Enthält `0:n`, auf ein `DataFrame` angewendet, das Element mit dem Index `n` 
oder geht es nur bis `n-1`?
Sie können dazu das Ergebnis der vorherigen Aufgabe betrachten.

[ER] Wählen Sie jede dritte Zeile der ersten 50 Zeilen aus, angefangen bei 0.

[EQ] Was passiert, wenn sie versuchen, statt der Zeilenindizes Slicing auf den Spaltenindizes zu
betreiben?


### Kombinieren von Zeilen- und Spaltenzugriff: `dataframe[index][index]`

Nun handelt es sich bei einem `DataFrame` um eine zweidimensionale Datenstruktur, bei der man
eventuell einen Teilbereich von Zeilen und einen Teilbereich von Spalten auswählen möchte.

[EQ] In [PARTREF::pd-Datenstrukturen] haben Sie hierzu bereits die Schreibweise 
`dataframe[spaltenindex][zeilenindex]` kennengelernt.
Wieso funktioniert das nicht genauso für eine Liste an Spaltenindizes, zum Beispiel: 
`erststimmen_df[["Wahlbezirk", "Gültige Stimmen"]][5]`?

[HINT::Wann Spaltenindex und wann Zeilenindex?]
Auf einem `DataFrame` spricht man mit der Schreibweise `data[index]` die Spalten des `DataFrame` an.
Auf einer `Series` spricht man mit der Schreibweise `data[index]` die Zeilen des `DataFrame` an.

Dadurch, dass `dataframe[spaltenindex]` eine `Series` zurückgibt, kann man auf dieser die Zeilen
ansprechen `dataframe[spaltenindex][zeilenindex]`.

Was ist der Rückgabetyp von `dataframe[[spaltenindex1, spaltenindex2, ...]]`?
[ENDHINT]

[ER] Formulieren Sie das Beispiel `erststimmen_df[["Wahlbezirk", "Gültige Stimmen"]][5]` so um, dass
es mit Hilfe von Slicing funktioniert.

[ER] Formulieren Sie ihr Ergebnis aus der vorherigen Aufgabe so um, dass zuerst die Zeile ausgewählt
wird und dann die Spalten.


### Zugriff auf einzelne Felder: `at[]`

`dataframe[spaltenindex][zeilenindex]` ist also nur eine Verkettung von Ausdrücken, die uns zum
richtigen Feld führt.
Etwas eleganter ist die Notation
[`at[zeilenindex, spaltenindex]`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html).
Damit kann man direkt auf ein *einzelnes* Feld zugreifen, indem man den Zeilenindex und dann den
Spaltenindex angibt.

Wie Sie an den eckigen Klammern sehen, ist `at` keine Methode, sondern ein Attribut. 
`dataframe.at` ist ein Hilfsobjekt, auf dem man Indexierung anwenden kann.
<!-- TODO_3_Saka: Python Klassen-Attribute als assumes-->


[ER] Geben Sie mit `at` den Wert von CDU in der ersten Zeile des `erststimmen_df` aus.


### Zugriff auf Bereiche: `loc[]`

Nun möchte man oft nicht nur ein Feld betrachten, sondern ein oder mehrere Zeilen bzw. Teilbereiche
dieser Zeilen. 
Hierfür gibt es die Notation
[loc[zeilenbereiche, spaltenbereiche]](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html),
die den gleichen technischen Kniff anwendet wie `at` und sehr flexibel ist für die Auswahl von Teilbereichen.

Bereiche können Sie zum Beispiel mit Listen angeben: 
`dataframe.loc[[zeilindex1, zeilenindex2], [spaltenindex1, spaltenindex2]]`

[ER] Schauen Sie in die Dokumentation von `loc` und machen Sie sich mit den Parametern vertraut.
Geben Sie den Wert von CDU in der ersten Zeile des `erststimmen_df` mithilfe von `loc` aus.

[ER] Geben Sie mithilfe von `loc` den Wert von CDU sowie die gültigen Stimmen in der ersten und
dritten Zeile aus.

Bereiche kann man neben Listen hier auch mit Slicing angeben.

[EQ] Welchen Bereich gibt `erststimmen_df.loc[0:3]` zurück?

[EQ] Welchen Bereich gibt `erststimmen_df.loc[:3, "Erststimmen"]` zurück?

[EQ] Welchen Bereich gibt `erststimmen_df.loc[:]` zurück?

[ER] Slicing lässt sich nicht nur auf numerische Indizes anwenden. 
Geben Sie mithilfe von `loc` und dem `:`-Operator die ersten 5 Zeilen zurück mit den Spalten von
"Adresse" bis "Wahlbezirk".

[EQ] Wie bereits erwähnt lassen sich per Slicing auch Schrittgrößen angeben. 
Was tut der folgende Ausdruck: `erststimmen_df.loc[0:49:10]`

[EQ] Was bedeutet `erststimmen_df.loc[::10, "Adresse":"Bezirksnummer"]`

Mit `loc` können Sie also flexibel Bereiche des ganzen `DataFrame` auf Grundlage der Indizes
ansprechen. 
Mit `at` lässt sich das nur auf einzelnen Einträgen machen. 

[NOTICE]
Wieso sollte man `at[]` einsetzen, wenn man auch `loc[]` für einzelne Felder benutzen kann? 
Weil `at[]` schneller ist; es kann bei großen `DataFrames` für spürbar 
schnelleren Gesamtablauf sorgen.
[ENDNOTICE]


### Zugriff per Position: `iat[]` und `iloc[]`

`at` und `loc` arbeiten mit den Indizes des `DataFrame`. 
Beide besitzen auch ein Gegenstück, mit dem man rein per Position und nicht per Index arbeiten kann: 
[iat](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html) 
und 
[iloc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

Aus `at[zeilenindex, spaltenindex]` wird also `iat[zeilenposition, spaltenposition]` und ebenso
mit `loc` und `iloc`.

In unserem Beispiel des `erststimmen_df` sind der Zeilenindex und die Zeilenposition zwar gleich,
aber das gilt nur, weil dieser `DataFrame` keinen eigenen Zeilenindex hat (was allerdings häufig vorkommt).
Die Spalten hingegen haben fast immer einen Index, nämlich individuelle Spaltennamen.

[ER] Formulieren Sie `erststimmen_df.at[0,"Adresse"]` zu `iat` um.
Überlegen Sie sich hierzu, welche Spaltenposition "Adresse" hat.

[ER] Formulieren Sie `erststimmen_df.loc[10:50,"Stimmart":"Wahlbezirk"]` zu `iloc` um. 

[NOTICE]
`loc[]` und `iloc[]` unterscheiden sich, wie bereits erwähnt, 
in der Zugriffsart (Index und Position), doch es gibt einen weiteren wichtigen Unterschied:

`0:9` wird bei `loc[]` inklusiv behandelt, `0..9` sind die erhaltenen Einträge.
Das Ende `9` wird also mit einbezogen.
Das ist nötig, weil hier ja auch z.B. Strings stehen könnten, wo ein weglassen
des letzten sehr seltsam wäre.

`0:9` wird bei `iloc[]` exklusiv behandelt, `0..8` sind die erhaltenen Einträge.
Das Ende, `9`, wird nicht mit einbezogen, genau wie bei slices in Python.
[ENDNOTICE]


### Wann kann man welche Funktion nutzen?

Wenn man per Index auswählen möchte:

- Spalten auswählen: `dataframe[spaltenindex]` bzw. `dataframe[[spaltenindex1, ...]]`
- Zeilen auswählen: `dataframe[start:end:step]`
- Spalten auswählen: `dataframe.loc[:, spalten]`
- Zeilen auswählen: `dataframe.loc[zeilen]`
- Zeile und Spalten auswählen: `dataframe.loc[zeilen, spalten]`
- Effizient einzelne Felder auswählen: `dataframe.at[zeile, spalte]`

Wenn man per Position auswählen möchte:

- Zeilen auswählen: `dataframe.iloc[zeilenpositionen]`
- Zeile und Spalten auswählen: `dataframe.iloc[zeilenpositionen, spaltenpositionen]`
- Effizient einzelne Felder auswählen: `dataframe.iat[zeilenposition, spaltenposition]`

Letztendlich gibt es keine festen Regeln, welche dieser Arten der Datenauswahl man benutzen sollte.
Empfehlenswert ist es, standardmäßig mit `loc[]` zu arbeiten, für positionsbasierte Fälle `iloc[]` 
und für Fälle, in denen man stets auf ein einzelnes Feld zugreifen möchte, `at[]` bzw. `iat[]` zu
verwenden. 

Beim Bearbeiten von Datenbereichen gibt es weitere Best Practices, die hilfreich sein können.
Schauen Sie sich hierzu die Aufgabe zu Copy und Views in Pandas an: [PARTREF::pd-Datenveränderung]
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Antworten im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]

