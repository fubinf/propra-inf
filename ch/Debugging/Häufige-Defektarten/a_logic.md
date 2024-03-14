title: Algorithmisches - Logische Defekte
stage: alpha
timevalue: 1
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, welche Form logische Defekte in Code annehmen können und habe einen solchen Defekt
in fremdem Code erfolgreich gefunden.

[ENDSECTION]

[SECTION::background::default]

Logische Defekte können zu Fehlfunktionen, Sicherheitslücken und einer beeinträchtigten Benutzererfahrung führen.
Entwickler sollten diese Defekte verstehen, um präventive Maßnahmen zu ergreifen,
effizientes Debugging zu ermöglichen und qualitativ hochwertigen Code zu schreiben.
Dies fördert nicht nur die Effizienz und Sicherheit von Software,
sondern erleichtert auch die Zusammenarbeit in Teams.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an logische Defekte

Computer sind präzise in der Ausführung von Anweisungen, aber oft unfähig, Absichten zu
antizipieren, was zu logischen Defekten führt, oft basierend auf schlechten Annahmen über Daten.
Sehen Sie sich hierfür das folgende Code-Beispiel in Python an.
Hier wird versucht mittels Wissen über die Repräsentation von ASCII-Zeichen
einen String in eine kleingeschriebene Variante umzuwandeln.
`ord()` wandelt dabei ein Zeichen in seinen numerischen ASCII-Wert um, während `chr()` das
Gegenteil macht.

```python
s = "TESt"
lower = ""
for k in range(0, len(s)):
    lower += chr(ord(s[k]) - ord("A") + ord("a"))
```

Versuchen Sie für sich den Code mittels einer
[ASCII-Tabelle](https://www.asciitable.com/) nachzuvollziehen.
Der Code funktioniert... solange `s[k]` ein Großbuchstabe ist.
Bei Kleinbuchstaben, Satzzeichen und Leerzeichen würde der Code nicht das gewünschte Resultat liefern.

Gerade Schleifen können sehr anfällig für logische Defekte sein.
Vor allem bei der Überlegung, wie man die Schleife beendet können Denkfehler auftreten.
Als Beispiel dient diese Initialisierung einer `for`-Schleife in C.
Sehen Sie schon das Problem?

```C
for (j = 1; j != 100; j = j + 2)
```

[HINT::Der Index der Schleife...]
...fängt bei 1 an, wird bei jeder Iteration um 2 erhöht
und die Schleife läuft, solange der Index den Wert 100 nicht annimmt.
Dies kann niemals der Fall sein, sofern `j` nicht innerhalb der Schleife manipuliert wird,
also wird die Schleife niemals terminieren.
[ENDHINT]

Genauso kann durch ein falsch gesetztes oder vergessenes `break`
der richtige Zeitpunkt zum Austritt aus der Schleife verpasst werden,
wie z. B. in diesem Python-Code.

```python
def end_of_line():
    ... # some code defining the end of a line

def cleanup():
    ... # some code cleaning up the processing pipeline

while True:
    if end_of_line():
        cleanup()
        # probably missing a break statement here
    # some code processing
```

Am Ende der Zeile (`end_of_line()`) wird eine Aufräum-Funktion (`cleanup()`) aufgerufen.
Es wird aber verpasst danach aus der while-Schleife auszubrechen, wodurch es folgend zum 
Programmabsturz kommen kann.

Die bisherigen Beispiele für Defekte sind durch kleine Änderungen behebbar gewesen.
Dass das nicht immer der Fall sein muss, soll das folgende Beispiel zeigen.

```python
a = [...] # list with unsorted ints
biggest = 0 
for k in range(len(a)-1):
    distance = abs(a[k] - a[k+1])
    if distance > biggest:
        biggest = distance
```

Hier wird versucht den Abstand zwischen den zwei Zahlen in `a` zu finden, die am weitesten 
voneinander entfernt sind. 
Dieser Code tut genau das, was der Programmierer vorhat, der Algorithmus ist aber falsch.
Es wird davon ausgegangen, dass die zwei am weitesten voneinander entfernten Zahlen 
nebeneinander liegen. 
Eine kleine Änderung wird bei diesem logischen Defekt nicht helfen; der gesamte Algorithmus muss 
überarbeitet werden. 

### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein logischer Defekt vorliegt.
Diese Funktion teilt Personen fürs Weihnachtswichteln ihren Partnern zu.
Hierfür erhält die Funktion eine Liste von Namen und gibt ein Dictionary zurück, 
in dem die Schlüssel die Schenker und die Werte die Beschenkten darstellen.
Das ist gar nicht so trivial: Die Funktion muss die Situation verhindern, 
in der die ersten N-1 Personen unter sich selbst Geschenke verteilen und 
die letzte Person nur noch sich selbst beschenken könnte.
Im folgenden Python-Code kann in einigen Iterationen bei der Handhabung dieses Falls
ein Defekt auftreten, durch den eine Person doppelt beschenkt wird:

```python
[INCLUDE::a_logic.py]
```

Hier sind einige Vorschläge, um an den Code heranzutreten:

1. Es werden zwei Listen (`input_list` und `receivers_list`) und ein Dictionary (`return_dict`) 
   benutzt.  
   Benennen Sie, was das Ziel dieser Datenstrukturen in diesem Code ist und
   notieren Sie, wo und wie diese verändert werden.
2. In Zeile 43 wird die Funktion `index()` benutzt, um eine Person in `receivers_list` zu finden.
   Das impliziert, dass diese Person in `receivers_list` sein muss.  
   Gibt es eine Garantie, dass das der Fall sein muss?
3. Es existiert eine Invariante zwischen `return_dict` und `receivers_list`,
   in welcher ein Element in einer der Listen ist, aber nicht in der anderen.
   Prüfen Sie, die entsprechenden Zeilen Code, die sicherstellen, dass diese Invariante immer
   wahr ist.
4. Was ist das Ziel des Codes in den Zeilen 41 bis 46?  
   Wie viele Pfade kann man in diesem Code zu durchlaufen?

[HINT::Lösungshinweis 1]
Durchlaufen Sie eine Iteration des Codes mit der unter `test_input` angegebenen Liste.

[HINT::Lösungshinweis 2]
Nehmen Sie noch einmal die Eingabe aus `test_input`.
Stellen Sie sich vor, dass die zweite Iteration läuft, also `person` gleich `Joe` ist und 
die `receivers_list` aus `["Tom", "Donna", "Susan", "Paul"]` besteht.

[HINT::Lösungshinweis 3]
Bedenken Sie eine vierte Iteration, in der `person` aus `"Susan"` besteht und
nehmen Sie an, dass die `receivers_list` jetzt aus `["Donna, "Paul"]` besteht.
[ENDHINT]

[ENDHINT]

[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `a_logic.py` korrigieren.
- Machen sie einen Commit `a_logic.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git show --color=always HEAD | cat`

[ENDSECTION]
[SECTION::submission::snippet]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]