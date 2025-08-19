title: "Daten bearbeiten"
stage: alpha
timevalue: 1.5
difficulty: 2
explains:
assumes:
requires: pd-Datenselektion
---

[SECTION::goal::idea]
Ich verstehe, wie man Daten in Pandas korrekt bearbeitet.

Ich kenne den Unterschied zwischen `View` und `Copy` und weiß sauber damit zu arbeiten.
[ENDSECTION]


[SECTION::background::default]
Pandas-Methoden weisen einen sehr unintuitives Verhalten dabei auf, ob man mit Ihnen das eigentliche
Datenobjekt bearbeitet oder eine Kopie des Datenobjekts erstellt und dann bearbeitet.
Diese Aufgabe lehrt das nötige Verständnis, um ungewollte Nebeneffekte zu vermeiden 
und Daten sauber zu bearbeiten.
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


### Daten bearbeiten

Das Bearbeiten von Daten ist oberflächlich gesehen recht intuitiv:

`erststimmen_df.loc[0,"Bezirksname"] = "Bearbeitet"` 

Wie bei einer herkömmlichen Liste können wir hier den Bereich den wir bearbeiten wollen 
per Index überschreiben.
Wenn Sie nun das `erststimmen_df` betrachten, sehen Sie die Änderung im ersten Eintrag.

[ER] Setzen Sie mithilfe von `loc` die ganze Spalte "Stimmart" auf "Bearbeitet".

[ER] Setzen Sie mithilfe von Indexierung (`erststimmen_df[...]`) die ganze Spalte "Stimmart" auf "Bearbeitet2".

# `Copy` und `View`

Auch wenn dies erstmal recht simpel erscheint, gibt es noch einige Stolperfallen, denn
beim Selektieren von Daten verhält sich Pandas nicht immer nachvollziehbar.

Manchmal werden nur Ansichten (`View`) auf die Originaldaten zurückgegeben. 
Das bedeutet wenn Sie diese Ansicht bearbeiten, werden auch die Originaldaten bearbeitet.
In anderen Fällen wird jedoch eine Kopie (`Copy`) erstellt werden.
Beim Bearbeiten vonn Kopien werden die Originaldaten nicht mitbearbeitet.
Ob eine Operation eine `View` oder eine `Copy` zurückgibt, 
hängt von der Operation _und den Daten_ ab.
Um das genauer zu verstehen, schauen Sie sich die folgende Beispiele an:

```python
subset1 = erststimmen_df[erststimmen_df["Bezirksname"] == "Mitte"]
subset1["Bezirksnummer"] = -1

subset2 = erststimmen_df.iloc[:50]
subset2.loc[:, "Wahlbezirk"] = -1
``` 

[EQ] Beide Beispiele nehmen eine Teilmenge des originalen `DataFrame` und bearbeiten diese.
Übernehmen Sie diese beiden Beispiele und betrachten Sie `ertstimmen_df`.
Bei welcher Teilmenge handelt es sich um eine wahre Kopie und bei welchem um eine `View`?

Mit großer Wahrscheinlichkeit ist es für Sie nicht gerade ersichtlich wieso sich die beiden
Beispiele unterschiedlich verhalten.
Und tatsächlich lässt sich das auch schwer vorraussagen.

[ER] Wenn Sie sicher gehen wollen, dass ein neues `DataFrame` erstellt wird, können Sie die Methode 
[`copy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy) 
verwenden.
Ändern Sie das Beispiel, welches zuvor eine `View` war, mit dieser Methode so ab, 
dass das originale `DataFrame` nicht mitbearbeitet wird.

[EQ] In der Dokumentation von `copy()`, werden `Shallow Copy` und `Deep Copy` erwähnt.
Erklären Sie den Unterschied zwischen diesen beiden Arten einer `Copy`.

[EQ] Wieso denken Sie gibt es überhaupt `View`s in Pandas, 
wenn es zu so einem unvorhersehbaren Verhalten mit Nebeneffekten führt?

# `SettingWithCopyWarning`

Nun wäre es allerdings recht aufwending, bei jeder Operation ein `copy()` ranzuhängen,
nur um sicher zu gehen, dass keine Nebeneffekte entstehen.
Hier soll die `SettingWithCopyWarning` Abhilfe schaffen. 
Es ist eine Warnung von Pandas, dass eine Zuweisung auf einem potenziellen `View` gemacht wurde –
wodurch nicht klar ist, ob das Original verändert wird oder nicht.

Wenn Sie eine solche Warnung bekommen, sollten Sie Ihre Ausdrücke dementsprechend umformulieren bzw.
`copy()` verwenden wenn nicht anders möglich.

[ER] `erststimmen_df["Bezirksname"][0] = "Mitte Neu"` formulieren Sie diesen Ausdruck so um, dass
Sie in der Konsole keine `SettingWithCopyWarning` kriegen.

[ER] `erststimmen_df[erststimmen_df["Bezirksname"] == "Mitte"]["Bezirksnummer"] = 999` formulieren
Sie auch diesen Ausdruck um, sodass er keine `SettingWithCopyWarning` wirft.

Besonders oft kommt es durch "Chained Assignments" also die Aneinanderreihung von Indexaufrufen beim
Bearbeiten zu solchen Fällen. Vermeiden Sie also wenn möglich Schreibweisen wie `df[][] = ...`.

# Copy-On-Write

Seit Pandas 2.0 gibt es ein neues Verhalten, das man einstellen kann, 
welches viele der oben genannten Probleme lösen soll: Copy-on-Write (CoW).

Das beduetet: Wenn Sie eine Teilmenge (z. B. per `df["col"]` oder `df.loc[...]`) erzeugen, 
dann wird zwar nicht direkt eine Kopie gemacht,
aber beim ersten Schreibzugriff auf diese Teilmenge wird automatisch eine Kopie angelegt.
Das hat den Vorteil, dass möglichst viel Performance erhalten bleibt und nicht bei jeder Operation
kopiert wird und dass keine Nebeneffekte auf das originale `DataFrame` entstehen. 
Das Original bleibt dadurch unverändert, auch wenn es technisch zunächst dieselben Daten nutzt.

[ER] Schauen Sie in die 
[Dokumentation zu Copy-On-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#migrating-to-copy-on-write). 
Aktivieren Sie Copy-On-Write. 
Falls Sie alles richtig gemacht haben, sollte weder `subset1` noch `subset2` das 
`erststimmen_df` verändern.

# Takeaways: So bearbeiten Sie Daten korrekt mit Pandas

- Besser `loc()` oder `iloc()` verwenden, um verkettete Zuweisungen wie `df[][] = ...`, zu vermeiden.
- Verwenden Sie `copy()` explizit, wenn Sie sicher sein wollen, eine unabhängige Kopie zu erhalten.
- Achten Sie auf die `SettingWithCopyWarning`. 
Sie signalisiert potenziell fehleranfällige Operationen.

- Mit aktiviertem Copy-on-Write (CoW), bleiben Originaldaten bei Bearbeitungen sicher unangetastet.

[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::`Copy` und `View` verstanden?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
