title: Sortieren in Python
stage: alpha
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::trial]

Ich kenne die Sortiermechanismen von Python und kann sie auch dann anwenden,
wenn eine besondere Sortierordnung gefragt ist.

[ENDSECTION]
[SECTION::background::default]

Wer in normalen Anwendungen selber ein Sortierverfahren implementiert,
hat wahrscheinlich nicht mehr alle Tassen im Schrank,
denn es gibt in jeder ernstzunehmenden Sprache gute Implementierungen, 
die man wiederverwenden sollte.

Fast alle Aufgaben kann man mit den "eingebauten" Sortierverfahren gut lösen,
wenn man weiß, wie man sie richtig benutzt.

Und selbst, wenn das mal nicht geht, ist wahrscheinlich eine _andere_
Standardimplementierung die beste Alternative;
siehe z.B. die Aufgabe [PARTREF::m_subprocess2] für ein eindrucksvolles Beispiel. 

Hier lernen wir also das nötige Grundwissen über Sortieren in Python.

[ENDSECTION]
[SECTION::instructions::detailed]

### Startpunkt

- [ER] Legen Sie die Datei `sorted_and_sort.py` an und fügen Sie folgendes dort ein:
 
```
what = "Tupel von Alter, Gewicht, Körpergröße"
data = [
    (22, 69, 177,), 
    (22, 71, 172,), 
    (48, 72, 174,), 
    (38, 89, 179,), 
    (71, 59, 170,), 
]

print(what)
print(data)
print("Sortiert:")
print(...)  # Schritt 1
print("Sortiert nach Körpergröße 1:")
print(...)  # Schritt 2
print("Sortiert nach Körpergröße 2:")
print(...)  # Schritt 3
print("Sortiert nach Übergewicht:")
print(...)  # Schritt 4
print("Sortiert in Gewichtsgruppen:")
print(...)  # Schritt 5
```

Diese vier verschiedenen Sortierungen erarbeiten wir uns nun.

- Lesen Sie über die eingebaute Funktion `sorted` nach:
  [HREF::https://docs.python.org/3/library/functions.html#sorted]
- Damit kann man offensichtlich sehr einfach eine sortierte Kopie(!)
  einer Liste von Integers oder einer Liste von Strings erhalten.
- Sortiert man damit Tupel wie in unserem Fall,
  dann ist deren erstes Element das Sortierkriterium.
  Wenn das gleich ist, gilt das zweite und so weiter.
- [ER] Geben Sie bei Schritt 1 eine sortierte Kopie von `data` aus.
- [ER] Und wenn wir nach Körpergröße sortieren müssen?
  Geht auch. Dafür ist das Argument `key` geeignet.
  Wir brauchen eine Funktion, die die Körpergröße aus einem Tupel fischt.
  Schreiben Sie eine Funktion `height(mytuple: tuple[int, int, int]) -> int`, 
  die das tut, übergeben Sie sie bei `key` und geben Sie bei Schritt 2 
  die so sortierte Liste von Tupeln aus.

[HINT::Warum bekomme ich dabei immer eine Fehlermeldung?]
Sie müssen die Funktion übergeben, also `key=height`,
nicht das Ergebnis eines Aufrufs davon, wie bei `key=height()` u.ä.
[ENDHINT]

- Dieser Fall, dass die `key`-Funktion nur ein vorhandenes Element aus einem komplexen Objekt
  fischen muss, ist so häufig, dass es dafür zwei fertige Helferlein in Python gibt.
  `operator.itemgetter` (um das `k`-te Element einer Sequenz zu holen; das ist unser Fall) und 
  `operator.attrgetter` (um ein Attribut mit dem Namen `name` zu holen).  
  Lesen Sie `itemgetter` nach: 
  [HREF::https://docs.python.org/3/library/operator.html#operator.itemgetter]
- Diese beiden Funktionen liefern also bei Aufruf eine Funktion, nicht einen passiven Datenwert.
  Nur deshalb können wir einen solchen Aufruf für `key=` bei `sorted()` gebrauchen.
- [ER] Ergänzen Sie `import operator` und benutzen Sie einen Aufruf von 
  `operator.itemgetter` als Funktion, um das dritte Element jedes Tupels als Sortierschlüssel
  zu benutzen.
  Geben Sie bei Schritt 3 die so sortierte Liste von Tupeln aus.

[HINT::Warum bekomme ich dabei immer eine Fehlermeldung?]
Haben Sie daran gedacht, dass das dritte Element den Index 2 hat?
[ENDHINT]

- [ER] Nach einer einfachen Faustformel ist "Normalgewicht" die Körpergröße minus 100
  (jedenfalls für Männer, aber den Unterschied ignorieren wir hier).
  Übergewicht hat also, wer schwerer ist als dieser Wert.
  (Negative Werte sind nicht gleich Untergewicht, aber auch diese Feinheit ignorieren wir hier.)  
  Schreiben Sie eine Funktion `excess_weight(mytuple: tuple[int, int, int]) -> int`, 
  die das positive oder negative "Übergewicht" in diesem Sinne berechnet, 
  übergeben Sie sie bei `key` und geben Sie bei Schritt 4 
  die so sortierte Liste von Tupeln aus.
  Das war eine reine Fingerübung, es ist ganz analog zu Schritt 2.
- Aber dieser Ansatz mit einer `key`-Funktion hat Grenzen.
  Es gibt Sortierkriterien, die sich nicht auf einen einzelnen Datenwert reduzieren lassen,
  sondern eine Kaskade von Abfragen benötigen.
- Beispielsweise dieses: Gesucht ist eine Sortierung, die als Erstes die Gruppen 
  `klein` (bis 172cm) und `groß` (über 172cm) trennt und sodann _innerhalb_ dieser Gruppen
  nach Alter, dann bei Gleichheit nach Gewicht und erst zuletzt bei Gleichheit wieder nach
  Größe sortieren soll.
- Dafür brauchen wir eine Funktion, die direkt den Vergleich zweier Tupel beantwortet
  anstatt einen einzigen Sortierschlüssel zu liefern, der alle Kriterien abbildet.
- Auch das geht in Python und sogar relativ einfach, wenn die zu sortierenden Objekte
  zu einer Klasse gehören, die wir erweitern können.
  Bei Tupeln ist das erstmal nicht der Fall, also müssen wir die Tupel zu Klassenobjekten "aufbohren".
- [ER] Fügen Sie folgendes Ihrem Programm an geeigneter Stelle hinzu:

```
class MyTuple(tuple):
    ...
    
data2 = [MyTuple(t) for t in data]
```

- Damit sind die Tupel in `data2` gleichwertig zu denen in `data`, aber sie gehören nun
  einer Klasse an, die wir erweitern können.
- Python benutzt für die Vergleiche beim Sortieren, den "kleiner"-Operator.
  In Python kann man Operatoren überladen, also selber umdefinieren.
  Dazu haben die Operatoren einen festen Funktionsnamen.
  Wir diese Funktion als Methode in einer Klasse definiert, ist der Operator für
  Objekte dieser Klasse überladen
- Der Funktionsname für "kleiner" lautet `__lt__` ("less than").
- [ER] Schreiben sie nun also in `MyTuple` `__lt__(self, other)` im oben beschriebenen Sinn.
- Listen haben eine Methode `sort()`, die die Liste am Platze sortiert, also _ohne_ dabei eine
  Kopie anzulegen wie bei der globalen Funktion `sorted()`.
- [ER] Sortieren Sie damit `data2` am Platze (also ohne Zuweisung).
- [ER] Geben Sie dann für Schritt 5 `data2` aus, 
  das nun die mit `__lt__` definierte Sortierung widerspiegeln müsste.

[HINT::Muss mein `__lt__` wirklich so umständlich aussehen?]
Wahrscheinlich nicht. So geht es ganz hübsch:
```
    def __lt__(self, other: 'MyTuple') -> bool:
        if not self.is_big and other.is_big:
            return True
        else:
            return tuple(self) < tuple(other)
    
    @property
    def is_big(self) -> bool:
        return self[2] > 172
```
[ENDHINT]

- [EC] Lassen Sie das fertige Skript einmal laufen.

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Korrektheit und Stil prüfen]

So sieht der korrekte Output aus:
[FOLDOUT::Output von `python sorted_and_sort.py`]
```
Tupel von Alter, Gewicht, Körpergröße
[(22, 69, 177), (22, 71, 172), (48, 72, 174), (38, 89, 179), (71, 59, 170)]
Sortiert:
[(22, 69, 177), (22, 71, 172), (38, 89, 179), (48, 72, 174), (71, 59, 170)]
Sortiert nach Körpergröße 1:
[(71, 59, 170), (22, 71, 172), (48, 72, 174), (22, 69, 177), (38, 89, 179)]
Sortiert nach Körpergröße 2:
[(71, 59, 170), (22, 71, 172), (48, 72, 174), (22, 69, 177), (38, 89, 179)]
Sortiert nach Übergewicht:
[(71, 59, 170), (22, 69, 177), (48, 72, 174), (22, 71, 172), (38, 89, 179)]
Sortiert in Gewichtsgruppen:
[(22, 71, 172), (71, 59, 170), (22, 69, 177), (38, 89, 179), (48, 72, 174)]
```
[ENDFOLDOUT]
Außerdem bitte kurz gucken, ob die `__lt__`-Funktion nicht gar zu arg
kompliziert geraten ist.

[ENDINSTRUCTOR]
