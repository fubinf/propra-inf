title: "Transformationen"
stage: alpha
timevalue: 1
difficulty: 2
explains:
assumes:
requires: pd-Datenveränderung
---

[SECTION::goal::product]
Ich verstehe, wie ich arithmetische Operationen und benutzerdefinierte Funktionen auf
Datenstrukturen in Pandas anwenden kann.
[ENDSECTION]


[SECTION::background::default]
Nicht immer lassen sich Transformationen (Veränderungen) der Daten mit eingebauten Pandas-Methoden
umsetzen.
Doch mit arithmetischen Operationen oder der Methode `apply()` in Kombination mit einer gewöhnlichen
Python-Funktion lassen sich auch solch sehr individuellen Transformationen umsetzen.
[ENDSECTION]


[SECTION::instructions::loose]
Laden Sie zunächst den 
[Datensatz der Erststimmen Bundestagswahl 2025](https://www.govdata.de/suche/daten/bundestagswahl-2025-in-berlin-nach-wahlbezirken-endgultiges-ergebnis) 
wie gewohnt in Ihre Python-Umgebung:
```python
import pandas as pd
erststimmen_df = pd.read_csv("Pfad/zur/Berlin_BT25_W1.csv", sep=';')
```


### Arithmetische Operationen (`+`,`-`,`/`,`*`,...)

Genauso wie Sie `Series` mit Boolean-Vergleichen (`<`,`=`,...) benutzen können, können Sie
auch arithmetische Operationen darauf anwenden.

Grundlegende arithmetische Operationen sind Folgende:     
- Addition: `s + 5` oder `s1 + s2`      
- Subtraktion: `s - 3` oder `s1 - s2`   
- Multiplikation: `s * 10` oder `s1 * s2`   
- Division: `s / 2` oder `s1 / s2`  
- Ganzzahldivision: `s // 2` oder `s1 // s2`    
- Modulo: `s % 2` oder `s1 % s2`    
- Potenz: `s ** 2` oder `s1 ** s2`      

[ER] Erstellen Sie eine neue Spalte `"SPD_pro_Waehlende"`, in der Sie die Stimmen der `"SPD"` durch
die Anzahl der `"Wählende"` Spalte teilen und abspeichern. 


### `apply()`

Die arithmetischen Operationen sind für sehr einfache Fälle von Nutzen. 
Wenn es aber um bedingte Abläufe oder Verzweigungen geht, dann ist das nicht mehr so einfach umzusetzen.
Idealerweise hätten Sie dann gerne, dass Sie eine *Funktion* mit der gewünschten Logik definieren und auf ein oder mehrere Spalten anwenden können.

Ein essenzielles Tool dafür ist
[`apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply).
Mit dieser Methode können Sie genau das machen und eingebaute oder selbstdefinierte Funktionen auf
Pandas-Datenstrukturen anwenden.

[ER] Verwenden Sie `apply()` mit der eingebauten Python-Funktion `len`, um die Länge aller Einträge der Spalte `"Bezirksname"` zu berechnen.

[ER] Definieren Sie eine Funktion, um die Stimmzahlen zu verdoppeln, 
falls die Stimmzahlen ungerade sind und wenden Sie diese mit `apply()` auf die "SPD" an.

Manchmal ist es praktisch, Funktion die man eh nur einmal verwendet, 
direkt an dem Ort zu definieren, an dem man sie benutzt.
So eine temporäre Funktion nennt man [TERMREF::Anonyme Funktion].

[ER] Setzen Sie die vorherige Aufgabe mittels einer anonymen Funktion in `apply()` um.

[EQ] Können Sie `max()` auf eine Spalte mittels `apply()` anwenden?
Begründen Sie.
Versuchen Sie, dafür die Funktionsweise von `apply()` mittels der Dokumentation besser zu verstehen.

[EQ] Wenden Sie `max()` mittels `apply()` auf das ganze `erststimmen_df` an.
Was passiert, wenn Sie `apply()` auf ein `DataFrame` statt auf eine `Series` anwenden.
Beschreiben Sie die Rückgabe.

[EQ] Wieso funktioniert `max()` im folgenden Beispiel?
Wie genau ist `x` in dem Fall aufgebaut?

```python
max_series = erststimmen_df[["SPD","CDU","AfD"]].apply(lambda x: max(x), axis=1)
```


### Mapping mittels `apply()` und `map()`

[ER] Wenden Sie mittels `apply()` dieses Dictionary auf die Spalte "Bezirksname" an.
Am Ende sollte somit jeder Eintrag in "Bezirksname" durch seinen entsprechenden Wert aus dem
Dictionary ersetzt sein.

```python
bezirke_dict = {
    "Mitte": "MI",
    "Charlottenburg-Wilmersdorf": "CW",
    "Friedrichshain-Kreuzberg": "FK",
    "Pankow": "PA",
    "Spandau": "SP",
    "Steglitz-Zehlendorf": "SZ",
    "Tempelhof-Schöneberg": "TS",
    "Neukölln": "NE",
    "Treptow-Köpenick": "TK",
    "Marzahn-Hellersdorf": "MH",
    "Lichtenberg": "LI",
    "Reinickendorf": "RE"
}
```

Für solche Mapping-Vorgänge können Sie die Methode
[`map()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map)
anwenden anstelle von `apply()`.

[ER] Nutzen Sie das Dictionary mit `map()`, um das gleiche Ergebnis wie mit `apply()` zu erhalten.

[EQ] Erklären Sie den Unterschied zwischen `map()` und `apply()` in Bezug auf ihre typische Verwendung.  
Wann ist `map()` ausreichend, wann braucht man `apply()`?
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::`apply()` verstanden]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
