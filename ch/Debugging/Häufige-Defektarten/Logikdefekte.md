title: Logikdefekte
stage: beta
timevalue: 1
difficulty: 2
---
[SECTION::goal::idea]

Ich verstehe, welche Form logische Defekte in Code annehmen können und habe einen solchen Defekt
in fremdem Code erfolgreich gefunden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Eine Heranführung an logische Defekte

Computer sind präzise in der Ausführung von Anweisungen, aber unfähig, Absichten zu
antizipieren, was zu logischen Defekten führt, oft basierend auf schlechten Annahmen über Daten.
Sehen Sie sich hierfür das folgende Code-Beispiel in Python an.
Hier wird versucht, mittels Wissen über die Repräsentation von [TERMREF::ASCII]-Zeichen
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
Der Code funktioniert, wenn `s[k]` ein Großbuchstabe ist.
Bei Kleinbuchstaben, Satzzeichen und Leerzeichen liefert er aber nicht das gewünschte Resultat.
Der Grund hierfür ist, dass man die Logik der ASCII-Tabelle ignoriert hat.
Hier haben Klein- und Großbuchstaben verschiedene Codierungen.

Ein weiteres Beispiel findet man bei der Initialisierung von Schleifen.
Pythons `for`-Schleife ist hier sehr robust, deshalb behelfen wir uns der Syntax einer 
`for`-Schleife in C.
Vor allem bei der Überlegung, wie man die Schleife beendet, können Denkfehler auftreten.
In C-Syntax besteht die Initialisierung einer `for`-Schleife aus drei Teilen:

- Zuerst wird eine Laufvariable, auch Index genannt, initialisiert.
- Danach wird eine Abbruchbedingung gestellt und die `for`-Schleife läuft, solange diese 
  Bedingung nicht erfüllt ist.
  In der Regel benutzt man den Index zur Definition der Abbruchbedingung.
- Letztlich wird noch definiert wie der Index innerhalb der Schleife inkrementiert wird.

Sehen Sie schon das Problem?

```C
for (j = 1; j != 100; j = j + 2)
```

[HINT::Der Index der Schleife...]
...fängt bei 1 an, wird bei jeder Iteration um 2 erhöht (ist also immer ungerade)
und die Schleife läuft, solange der Index den Wert 100 nicht annimmt.
Das Abbruchkriterium kann also allenfalls erfüllt werden, wenn der Schleifenrumpf weitere
Änderungen an `j` macht;
andernfalls wird die Schleife niemals anhalten.

Hier wäre vermutlich die Bedingung `j < 100` sinnvoller. Um genau diese Art von Fehler
zu vermeiden, ist der idiomatische Weg in Python auch `for j in range(1, 100, 2)`.
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
Es wird aber verpasst, danach aus der while-Schleife auszubrechen, wodurch es folgend zum 
Versagen kommen kann.

Die bisherigen Beispiele für Defekte sind durch kleine Änderungen behebbar gewesen.
Dass das nicht immer der Fall sein muss, soll das folgende Beispiel zeigen.
Im folgenden Python-Code wird versucht den Abstand zwischen den zwei Zahlen in der Liste `a` zu 
finden, die am weitesten voneinander entfernt sind.
In der Liste `a = [2, 1, 10, 100]` sollte also das Ergebnis 99 lauten, denn die beiden am weitesten 
voneinander entfernten Zahlen lauten 1 und 100.

```python
a = [2, 1, 10, 100] # list with unsorted ints
biggest = 0 
for k in range(len(a)-1):
    distance = abs(a[k] - a[k+1])
    if distance > biggest:
        biggest = distance

print(biggest) # 90
```

Dieser Code tut genau das, was der Programmierer vorhat und berechnet den Abstand zwischen zwei 
Zahlen aus der Liste `a`.
Der Algorithmus ist aber falsch, da er davon ausgeht, dass die zwei am weitesten voneinander 
entfernten Zahlen nebeneinander liegen.
Eine kleine Änderung wird bei diesem logischen Defekt nicht helfen; der gesamte Algorithmus muss 
überarbeitet werden.


### Ihre Aufgabe

Im Folgenden sollen Sie eine Funktion debuggen, in der ein logischer Defekt vorliegt.
Diese Funktion teilt Personen fürs Weihnachtswichteln ihren Partnern zu.
Hierfür erhält die Funktion eine Liste von Namen und gibt ein [TERMREF::Dictionary] zurück, 
in dem die Schlüssel die Schenker und die Werte die Beschenkten darstellen.
Das ist gar nicht so trivial: Die Funktion muss die Situation verhindern, 
in der die ersten N-1 Personen unter sich selbst Geschenke verteilen und 
die letzte Person nur noch sich selbst beschenken könnte.
Im folgenden Python-Code kann in einigen Iterationen bei der Handhabung dieses Falls
ein Defekt auftreten, durch den eine Person doppelt beschenkt wird:

```python
[INCLUDE::Logikdefekte.py]
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
   Über wie viele Pfade kann man in diesen Code durchlaufen?

[HINT::Lösungshinweis 1]
Durchlaufen Sie eine Iteration des Codes mit der unter `test_input` angegebenen Liste.

[HINT::Lösungshinweis 2]
Nehmen Sie noch einmal die Eingabe aus `test_input`.
Stellen Sie sich vor, dass die zweite Iteration läuft, also `person` gleich `Joe` ist und 
die `receivers_list` aus `["Tom", "Donna", "Susan", "Paul"]` besteht.

[HINT::Lösungshinweis 3]
Bedenken Sie eine vierte Iteration, in der `person` aus `"Susan"` besteht und
nehmen Sie an, dass die `receivers_list` jetzt aus `["Donna, "Paul"]` besteht.  
Welche Zuteilungen sind hier noch möglich?
[ENDHINT]

[ENDHINT]

[ENDHINT]

- Defekt gefunden? Prima. Dann jetzt bitte in `Logikdefekte.py` korrigieren.
- Machen sie einen Commit `Logikdefekte.py corrected`, der nur genau diese modifizierte Datei enthält.
- [EC] `git -P show HEAD`

[ENDSECTION]
[SECTION::submission::snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Lösungsansatz]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]