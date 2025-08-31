title: "pandas: Daten ändern"
stage: alpha
timevalue: 1.5
difficulty: 2
requires: pd-Datenselektion
---

[SECTION::goal::idea]
Ich verstehe, wie man Daten in Pandas korrekt verändert.

Ich verstehe, welches Verhalten man von Pandas in Hinblick auf die Kopien (`Copy`) und Sichten
(`View`) erwarten würde und wie Pandas von diesem mentalen Modell abweichen.
[ENDSECTION]

[SECTION::background::default]
Pandas-Methoden weisen ein sehr unintuitives Verhalten auf, wenn man Daten ändert,
denn beim vorherigen Selektieren bekommt man manchmal eine _Sicht_ auf den darunter liegenden
Dataframe und manchmal eine _Kopie_ der jeweiligen Teile des Dataframes.
Wenn man den Dataframe ändern wollte, wird der zweite Fall also ein Fehlschlag. 
Diese Aufgabe lehrt das nötige Verständnis, um Daten erfolgreich zu bearbeiten.
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

Das Ändern eines Dataframes scheint zunächst einfach:

`erststimmen_df.loc[0,"Bezirksname"] = "Bearbeitet"`

Wie bei einer herkömmlichen Liste können wir hier den Bereich, den wir bearbeiten wollen 
per Index selektieren und überschreiben.
Wenn Sie nun `erststimmen_df` betrachten, sehen Sie die Änderung im ersten Eintrag.

[ER] Setzen Sie mithilfe von `loc()` die ganze Spalte "Stimmart" überall auf "Bearbeitet".

[ER] Ändern Sie mithilfe von Indexierung (`erststimmen_df[...]`) die ganze Spalte "Stimmart" auf "Bearbeitet2".

### Mentales Modell

Bei einer Liste ist das Auswählen und Schreiben ähnlich:
`liste[3] = "Neuer Wert"`
Jede dieser Selektionen (`loc()`, Indexierung, etc.) kann man sich als eine Art "Fenster" 
(Sicht, `View`) auf den `DataFrame` selbst vorstellen.
Wenn Sie so einer Sicht Daten zuweisen, dann werden die Daten vom originalen
`DataFrame` selbst überschrieben.

#### Subsets

[EQ] Wenn jede Selektion eine Sicht auf den `DataFrame` ist, würde man erwarten, dass folgender Code
`df` bearbeitet?

```python
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
subset = df["a"]
subset[0] = 999
```

[HINT::`subset` eigenständiger `DataFrame`?]
`subset` speichert nur die Sicht auf `df` und sollte nach unserem Verständnis kein eigenständiger
`DataFrame` sein.
Wenn also was in `subset` geändert wird, wird es auch in `df` geändert.
[ENDHINT]

[ER] Trotzdem möchte man als Programmierer die Möglichkeit haben, explizit Kopien eines `DataFrame`
zu erstellen.
Dazu können Sie die Methode
[`copy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy) 
verwenden.
Ändern Sie das vorherige Beispiel so ab, dass `subset` eine echte Kopie von `df` ist.

#### Verkettete Indexierung

Wenn jede Selektion eine Sicht ist, dann sollte man auch Verkettungen schreiben können, wie:
`df["Spalte B"][df["Spalte A"] == 1] = 99`
Denn letztendlich wird die Sicht auf die Daten einfach nur immer weiter eingeschränkt.

[EQ] Warum würde dieser Ausdruck nicht `df` bearbeiten, wenn jede Selektion eine Kopie zurückgibt
statt einer Sicht?

### Reales Verhalten von Pandas

Doch tatsächlich weicht Pandas von diesem Ideal, jede Selektion sei eine Sicht auf Daten, ab.
Und das ist der Kernpunkt für die meisten Verwirrungen, die im Umgang mit Pandas entstehen.
Pandas garantieren nämlich nicht, dass jede Selektion eine Sicht ist:
Manchmal, und leider auch sehr unvorhersehbar, _können_ Kopien zurückgegeben werden statt Sichten (`Views`).

```python
subset1 = erststimmen_df[erststimmen_df["Bezirksname"] == "Mitte"]
subset1["Bezirksnummer"] = -1

subset2 = erststimmen_df.iloc[:50]
subset2.loc[:, "Wahlbezirk"] = -1
``` 

[EQ] Beide Beispiele nehmen eine Teilmenge des originalen `DataFrame` und bearbeiten diese.
Übernehmen Sie diese beiden Beispiele und betrachten Sie `ertstimmen_df`.
Bei welcher Teilmenge handelt es sich um eine Kopie und bei welcher um eine Sicht?

[NOTICE]
Änderungen auf der Kopie werden im originalen `DataFrame` nicht übernommen,
Änderungen auf der Sicht schon.
[ENDNOTICE]

[ER] Ändern Sie das Beispiel, welches zuvor eine `View` war, mit `copy()` so ab, 
dass der originale `DataFrame` nicht mitbearbeitet wird.

[EQ] Lesen Sie sich die Dokumentation zu 
[Returning a view vs copy](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy)
und 
[Why does assignment fail when using chained indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#why-does-assignment-fail-when-using-chained-indexing)
durch und erklären Sie, welche Probleme es mit "Chained Indexing" (verketteter Indexierung) gibt.

[NOTICE]
Solche ungewünschten Schreibweisen wie "Chained Indexing", die zu nicht vorhersehbarem Verhalten
führen, werden oftmals mithilfe der `SettingWithCoypWarning` von Pandas in der Konsole sichtbar
gemacht.
[ENDNOTICE]

Schauen Sie in die Dokumentation, um herauszufinden, wie sie "Chained Indexing" sauber umformulieren
können und bearbeiten Sie folgende Aufgaben.

[ER] `erststimmen_df["Bezirksname"][0] = "Mitte Neu"` formulieren Sie diesen Ausdruck so um, dass
Sie in der Konsole keine `SettingWithCopyWarning` kriegen.

[ER] `erststimmen_df[erststimmen_df["Bezirksname"] == "Mitte"]["Bezirksnummer"] = 999` formulieren
Sie auch diesen Ausdruck um, sodass er keine `SettingWithCopyWarning` wirft.

# Copy-On-Write

Seit Pandas 2.0 gibt es ein neues Verhalten, das man einstellen kann, 
welches viele der oben genannten Probleme lösen soll: Copy-on-Write (CoW).

Das bedeutet: Wenn Sie eine Teilmenge (z. B. per `df["col"]` oder `df.loc[...]`) auswählen, wird
jedes Mal eine Kopie gemacht.
Intern wird das Ganze zwar noch optimiert, aber für Sie als Programmierer heißt das, dass jede
Operation eine Kopie statt einer Sicht zurückgibt.
Somit ist jedenfalls ein deterministisches Verhalten möglich, es weicht aber stark vom mentalen
Modell ab.
Außerdem müssen Sie ein `DataFrame` beim Kopieren nicht mehr explizit mit `copy()` kopieren, aus
leserlichen Gründen ist dies ggf. trotzdem sinnvoll.

[ER] Schauen Sie in die 
[Dokumentation zu Copy-On-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#migrating-to-copy-on-write). 
Aktivieren Sie Copy-On-Write.
Falls Sie alles richtig gemacht haben, sollte weder `subset1` noch `subset2` das 
`erststimmen_df` verändern.

```python
subset1 = erststimmen_df[erststimmen_df["Bezirksname"] == "Mitte"]
subset1["Bezirksnummer"] = -1

subset2 = erststimmen_df.iloc[:50]
subset2.loc[:, "Wahlbezirk"] = -1
``` 

# Takeaways: So bearbeiten Sie Daten korrekt mit Pandas

- Besser `loc()` oder `iloc()` verwenden, um verkettete Indexierung wie `df[][] = ...`, zu vermeiden.
- Verwenden Sie `copy()` explizit, wenn Sie sicher sein wollen, eine unabhängige Kopie zu erhalten.
- Achten Sie auf die `SettingWithCopyWarning`. 
  Sie signalisiert potenziell fehleranfällige Operationen.
- Mit aktiviertem Copy-on-Write (CoW) bleiben Originaldaten bei Bearbeitungen sicher unangetastet.
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Pandas-Verhalten bei Datenselektion und -schreiben verstanden?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
