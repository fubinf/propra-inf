title: NumPy Sortierung und Filterung verstehen und anwenden
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-index-slice, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Arrays sortieren und weiß, wann ich statt der sortierten Werte die Sortierungsindizes
  brauche.
- Ich kann aus zeilen- oder spaltenweisen Sortierungsindizes das sortierte Array rekonstruieren.
- Ich kann Arrays nach mehreren Kriterien mit unterschiedlicher Sortierrichtung sortieren.
- Ich kann Extremwerte lokalisieren und einen flachen Index in Zeilen- und Spaltenindex umrechnen.
- Ich kann Arrays nach einer Bedingung durchsuchen und filtern.
- Ich kann begründen, wann eine Partitionierung der vollständigen Sortierung vorzuziehen ist.

[ENDSECTION]

[SECTION::background::default]

NumPy bietet spezialisierte Funktionen zum Sortieren, Suchen und Filtern von Arrays.
Damit bringt man Datensätze nach einem oder mehreren Kriterien in eine Rangfolge, lokalisiert
Extremwerte und wählt Teilmengen nach einer Bedingung aus.
Solche Schritte stehen am Anfang fast jeder Datenauswertung, noch vor der eigentlichen Rechnung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlegende Sortierung: `sort` und `argsort`

NumPy bietet zwei grundlegende Sortierfunktionen:

```python
numpy.sort(a, axis=-1)
numpy.argsort(a, axis=-1)
```

- `a`: das zu sortierende Array
- `axis` (Standard `-1`): Achse, entlang derer sortiert wird (`-1` = letzte Achse)

```python
import numpy as np

# Einfaches 2D-Array
arr = np.array([[3, 7], [9, 1]])
print('Ursprüngliches Array:')
print(arr)
# [[3 7]
#  [9 1]]

sorted_arr = np.sort(arr)
print('Sortiert (entlang letzter Achse):')
print(sorted_arr)
# [[3 7]
#  [1 9]]

# Sortierung entlang verschiedener Achsen
print('Sortiert entlang Achse 0 (innerhalb jeder Spalte):')
print(np.sort(arr, axis=0))
# [[3 1]
#  [9 7]]

print('Sortiert entlang Achse 1 (innerhalb jeder Zeile):')
print(np.sort(arr, axis=1))
# [[3 7]
#  [1 9]]
```

Bei einem 2D-Array ist die letzte Achse genau Achse 1, der erste und der letzte Aufruf sind hier
also gleichwertig.
`np.sort` lässt `arr` dabei unverändert und liefert ein neues Array mit eigenen Daten, also eine
Kopie im Sinne von [PARTREF::np-index-slice].
Keine der Sortier-, Such- und Filterfunktionen dieser Aufgabe verändert das übergebene Array.
Die Methode `arr.sort()` dagegen sortiert an Ort und Stelle und überschreibt dabei die
Ausgangsdaten.

**Index-basierte Sortierung mit `np.argsort`**

`np.argsort` gibt nicht die sortierten Werte selbst zurück, sondern die Indizes, die die
Elemente in sortierter Reihenfolge referenzieren:

```python
import numpy as np

# np.argsort() gibt Indizes zurück, die zur Sortierung führen
x = np.array([30, 10, 20])
indices = np.argsort(x)
print('Sortierungsindizes:', indices)  # [1 2 0]
print('Sortiertes Array:', x[indices])  # [10 20 30]
```

Bei einem 2D-Array liefert `np.argsort(a, axis=1)` für jede Zeile eigene Indizes.
Einfaches Advanced Indexing (`arr[indices]`) rekonstruiert das sortierte Array daraus nicht,
denn es liest die Indizes als Zeilenindizes und wählt damit ganze Zeilen aus.
Gebraucht wird stattdessen `np.take_along_axis`, das entlang einer Achse für jede Zeile
(bzw. Spalte) die dort passenden Indizes anwendet:

```python
numpy.take_along_axis(arr, indices, axis=-1)
```

- `arr`: das Array, aus dem Werte entnommen werden
- `indices`: Array mit derselben Anzahl Dimensionen wie `arr`, das für jede Position angibt,
  welches Element aus `arr` entnommen wird.
  Entlang `axis` bestimmt es die Länge des Ergebnisses, in den übrigen Achsen muss es zu `arr`
  passen.
- `axis` (Standard `-1`): Achse, entlang derer `indices` angewendet wird

```python
import numpy as np

arr = np.array([[50, 20, 80], [10, 90, 30]])
zeilenindizes = np.argsort(arr, axis=1)
rekonstruiert = np.take_along_axis(arr, zeilenindizes, axis=1)
print('Zeilenweise sortiert über argsort-Indizes:')
print(rekonstruiert)
print('Stimmt mit np.sort überein?', np.array_equal(rekonstruiert, np.sort(arr, axis=1)))
```

[ER] Arbeiten Sie mit grundlegenden Sortierfunktionen:

- Erstellen Sie mit `np.array` ein 3×4-Array `werte` mit den Werten
  `[[80, 30, 150, 60], [120, 10, 90, 200], [40, 170, 20, 110]]`
- Verwenden Sie `np.argsort(werte, axis=1)`, um die zeilenweisen Sortierungsindizes in
  `zeilenindizes` zu erhalten
- Versuchen Sie zunächst, das sortierte Array mit `werte[zeilenindizes]` zu rekonstruieren, und
  halten Sie in einem Kommentar fest, was dabei passiert; kommentieren Sie die Zeile danach aus,
  damit das abgegebene Skript durchläuft
- Rekonstruieren Sie das zeilenweise sortierte Array mit `np.take_along_axis` und vergleichen Sie
  das Ergebnis mit `np.sort(werte, axis=1)`

[HINT::Wie vergleiche ich zwei Arrays auf Gleichheit?]
Nutzen Sie das bereits aus [PARTREF::np-array] bekannte `np.array_equal`, um die beiden
Arrays elementweise auf Übereinstimmung zu prüfen.
[ENDHINT]

[EQ] Vergleichen Sie in [EREFR::1] die `np.argsort`-Indizes mit dem sortierten Array.
Welche Information steckt in den Indizes, die im Ergebnis von `np.sort` verloren geht?
Nennen Sie eine Situation, in der Sie deshalb `np.argsort` und nicht `np.sort` brauchen.

<!-- time estimate: 20 min -->

### Lexikographische Sortierung: `lexsort`

`np.lexsort` ermöglicht die Sortierung nach mehreren Kriterien,
ähnlich der Sortierung in Tabellenkalkulationen:

```python
numpy.lexsort(keys)
```

- `keys`: Sequenz von Arrays gleicher Länge; das **letzte** Array ist das primäre
  Sortierkriterium, das vorletzte das sekundäre, und so weiter

```python
import numpy as np

# Beispiel: Studierendendaten nach Gesamtpunkten, dann nach Mathematikpunkten
namen = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
gesamtpunkte = np.array([85, 92, 85, 88])
mathepunkte = np.array([90, 85, 95, 82])

# lexsort sortiert nach dem letzten Array zuerst, dann nach dem vorletzten
# Hier: erst aufsteigend nach Gesamtpunkten, dann aufsteigend nach Mathepunkten
indices = np.lexsort((mathepunkte, gesamtpunkte))

print('Sortierung nach Gesamtpunkten, dann nach Mathepunkten:')
for i in indices:
    print(f'{namen[i]}: Gesamt={gesamtpunkte[i]}, Mathe={mathepunkte[i]}')
# Alice: Gesamt=85, Mathe=90
# Charlie: Gesamt=85, Mathe=95
# Diana: Gesamt=88, Mathe=82
# Bob: Gesamt=92, Mathe=85
```

`np.lexsort` sortiert für jedes Kriterium immer aufsteigend.
Um nach einem Kriterium absteigend zu sortieren, übergeben Sie stattdessen die **negierten**
Werte dieses Arrays — die Reihenfolge dreht sich dadurch um, ohne dass sich an den
ursprünglichen Werten etwas ändert:

```python
import numpy as np

namen = np.array(['Alice', 'Bob', 'Charlie', 'Diana'])
gesamtpunkte = np.array([85, 92, 85, 88])
mathepunkte = np.array([90, 85, 95, 82])

# Absteigend nach Gesamtpunkten, dann aufsteigend nach Mathepunkten
indices_desc = np.lexsort((mathepunkte, -gesamtpunkte))
print('Sortierung nach Gesamtpunkten (absteigend), dann nach Mathepunkten:')
for i in indices_desc:
    print(f'{namen[i]}: Gesamt={gesamtpunkte[i]}, Mathe={mathepunkte[i]}')
# Bob: Gesamt=92, Mathe=85
# Diana: Gesamt=88, Mathe=82
# Alice: Gesamt=85, Mathe=90
# Charlie: Gesamt=85, Mathe=95
```

Diese Technik setzt Zahlen voraus.
Stringarrays lassen sich nicht negieren; mit `np.lexsort` sind sie deshalb nur aufsteigend
sortierbar.

[ER] Implementieren Sie eine lexikographische Sortierung:

- Erstellen Sie mit `np.array` drei Arrays: `produkte` mit den Werten
  `['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset']`, `preise` mit den Werten
  `[1200, 25, 75, 300, 150]` und `bewertungen` mit den Werten `[4.5, 4.2, 4.5, 4.0, 4.5]`
- Sortieren Sie die Produkte mit `np.lexsort` erst nach Bewertung (absteigend), dann nach Preis
  (aufsteigend), und geben Sie in dieser Reihenfolge für jedes Produkt Name, Preis und
  Bewertung aus
- Prüfen Sie Ihr Ergebnis: An erster Stelle steht weder das billigste noch das teuerste Produkt.
  Begründen Sie in einem Kommentar, warum es trotzdem vorne steht

[HINT::In welcher Reihenfolge muss ich die Arrays an `keys` übergeben?]
Die Reihenfolge in `keys` ist leicht zu verwechseln: Das **zuletzt** übergebene Array bestimmt
die Sortierung zuerst.
Im Punktebeispiel oben steht deshalb `gesamtpunkte` als letztes Element in `keys`, weil zuerst nach
der Gesamtpunktzahl sortiert werden soll und die Mathepunktzahl nur die Reihenfolge innerhalb
gleicher Gesamtpunktzahlen festlegt.
[ENDHINT]

<!-- time estimate: 10 min -->

### Suchen von Extremwerten: `argmax` und `argmin`

Diese Funktionen finden die Indizes der größten und kleinsten Elemente:

```python
numpy.argmax(a, axis=None)
numpy.argmin(a, axis=None)
```

- `a`: das zu durchsuchende Array
- `axis` (Standard `None`): Achse, entlang derer gesucht wird; bei `None` wird das Array
  zunächst zu 1D abgeflacht und ein einzelner Index zurückgegeben

Kommt der Extremwert mehrfach vor, liefern beide Funktionen den Index seines ersten Auftretens.

```python
import numpy as np

daten = np.array([[30, 40, 70],
                  [80, 20, 10],
                  [50, 90, 60]])

print('Datenarray:')
print(daten)

# Globale Extremwerte (flaches Array)
print('Index des Maximums (flach):', np.argmax(daten))
print('Index des Minimums (flach):', np.argmin(daten))

# Extremwerte entlang Achsen
print('Maximum-Indizes pro Spalte:', np.argmax(daten, axis=0))
print('Minimum-Indizes pro Zeile:', np.argmin(daten, axis=1))
```

Die beiden Aufrufe ohne `axis` liefern für das 3×3-Array oben die flachen Indizes 7 und 5.
Einen flachen Index in Zeilen- und Spaltenindex umzurechnen, übernimmt eine fertige Funktion:

```python
numpy.unravel_index(indices, shape)
```

- `indices`: flacher Index (oder Array von Indizes)
- `shape`: Form des ursprünglichen mehrdimensionalen Arrays

```python
import numpy as np

daten = np.array([[30, 40, 70],
                  [80, 20, 10],
                  [50, 90, 60]])

flach_max = np.argmax(daten)
zeile, spalte = np.unravel_index(flach_max, daten.shape)
print(f'Maximum {daten[zeile, spalte]} an flachem Index {flach_max} = Zeile {zeile}, Spalte {spalte}')

flach_min = np.argmin(daten)
zeile, spalte = np.unravel_index(flach_min, daten.shape)
print(f'Minimum {daten[zeile, spalte]} an flachem Index {flach_min} = Zeile {zeile}, Spalte {spalte}')
```

[ER] Analysieren Sie Daten mit Extremwertfunktionen:

- Erstellen Sie mit `np.array` ein 4×5-Array `daten` mit den Werten
  `[[12, 45, 8, 67, 23], [34, 89, 3, 41, 56], [78, 63, 62, 19, 90], [27, 51, 14, 38, 6]]`
- Finden Sie Position und Wert des globalen Maximums und Minimums, sowohl über den flachen
  Index als auch mit `np.unravel_index` umgerechnet in Zeile/Spalte
- Bestimmen Sie für jede Zeile das Maximum und für jede Spalte das Minimum
- Verwenden Sie die Indizes, um die tatsächlichen Werte auszugeben

[HINT::Welche `axis` brauche ich für "pro Zeile"?]
Die Beispielaufrufe oben zeigen die jeweils andere Richtung, als hier verlangt ist, also nicht
einfach abschreiben.
Machen Sie sich die Nummerierung der Achsen aus [PARTREF::np-array] an einem kleinen 2×3-Array
klar.
Eine Reduktion entlang einer Achse lässt genau diese Achse verschwinden; an der Länge des
Ergebnisses erkennen Sie deshalb, ob pro Zeile oder pro Spalte gesucht wurde.
[ENDHINT]

[EQ] In [EREFR::3] haben Sie für Maximum und Minimum jeweils den flachen Index und das von
`np.unravel_index` gelieferte Paar aus Zeile und Spalte ausgegeben.
Formulieren Sie anhand dieser beiden Beispiele eine Rechenregel, die den flachen Index aus Zeile
und Spalte bestimmt, und prüfen Sie sie an beiden Fällen nach.
Welche Angabe über die Form des Arrays geht in die Regel ein?

<!-- time estimate: 20 min -->

### Bedingte Suche: `nonzero`, `where` und `extract`

NumPy bietet folgende Funktionen für die bedingte Suche und Filterung:

```python
numpy.nonzero(a)                # gibt die Indizes aller Nicht-Null-Elemente zurück
numpy.where(condition, x, y)    # wählt elementweise x (bei True) oder y (bei False)
numpy.extract(condition, a)     # gibt die Werte von a zurück, an denen condition True ist
```

- `a`: das zu durchsuchende bzw. zu filternde Array
- `condition`: Boolean-Array oder -Ausdruck
- `x`, `y`: Werte bzw. Arrays, aus denen elementweise ausgewählt wird, je nachdem, ob
  `condition` an der jeweiligen Position `True` oder `False` ist

Ein Boolean-Ausdruck wie `a > 50` ist selbst ein Array aus `True` und `False`, sodass
`np.nonzero(a > 50)` die Indizes aller Elemente über 50 liefert.

```python
import numpy as np

arr = np.arange(10, 100, 10).reshape(3, 3)
print('Array:')
print(arr)

# Indizes aller Elemente > 50
indices = np.nonzero(arr > 50)
print('Indizes wo arr > 50:', indices)  # (array([1, 2, 2, 2]), array([2, 0, 1, 2]))
print('Werte an diesen Positionen:', arr[indices])  # [60 70 80 90]

# where() mit drei Argumenten wählt elementweise zwischen zwei Werten
arr_1d = np.arange(-10, 11)
absolute_values = np.where(arr_1d >= 0, arr_1d, -arr_1d)
print('Betrag über where(condition, x, y):', absolute_values)

# nonzero() ohne Vergleich findet die von Null verschiedenen Elemente
sparse_arr = np.array([[10, 0, 30], [0, 25, 0], [40, 0, 50]])
print('Nicht-Null-Indizes:', np.nonzero(sparse_arr))

# extract() liefert die Werte statt der Indizes
print('Durch 30 teilbar:', np.extract(arr % 30 == 0, arr))  # [30 60 90]
```

`np.nonzero` gibt keine Liste von Positionen zurück, sondern ein Tupel mit einem Indexarray je
Achse des Arrays.
Für ein 1D-Array besteht das Tupel deshalb aus genau einem Array, das man mit `[0]` herausholt.

`np.extract(bedingung, a)` ist bei einer Boolean-Bedingung nichts anderes als die
Boolean-Maske `a[bedingung]` aus [PARTREF::np-index-slice].
`np.where(condition)` ohne `x` und `y` liefert dasselbe wie `np.nonzero(condition)`; die
NumPy-Dokumentation empfiehlt für diesen Fall aber ausdrücklich `np.nonzero`.

[ER] Verwenden Sie bedingte Suchfunktionen:

- Erzeugen Sie mit `np.arange` ein Array `arr` mit den ganzen Zahlen von -15 bis 15
- Finden Sie mit `np.nonzero` die Indizes aller positiven Werte und geben Sie auch die Werte an
  diesen Positionen aus
- Erzeugen Sie mit der Drei-Parameter-Form `np.where(condition, x, y)` ein **neues** Array
  `begrenzt`, in dem alle negativen Werte durch `0` ersetzt sind und die übrigen Werte
  unverändert bleiben; `arr` selbst bleibt dabei unangetastet
- Erstellen Sie mit `np.array` ein 3×3-Array `sparse` mit den Werten
  `[[0, 12, 0], [34, 0, 56], [0, 78, 0]]` und finden Sie darin die Nicht-Null-Elemente
- Klären Sie die Bedeutung des Rückgabewerts für dieses 2D-Array anhand der
  [Dokumentation zu `numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)
  und erklären Sie Ihre Ausgabe in einem Kommentar
- Extrahieren Sie mit `np.extract` alle Werte von -5 bis 5 aus `arr`, beide Grenzen eingeschlossen

<!-- time estimate: 20 min -->

### Partitionierung: `partition` und `argpartition`

Partitionierung ordnet ein Array so um, dass an einer gewählten Position das Element steht,
das dort auch in einem vollständig sortierten Array stünde:

```python
numpy.partition(a, kth)      # gibt eine partitionierte Kopie von a zurück
numpy.argpartition(a, kth)   # gibt die Indizes zurück, die a partitionieren würden
```

- `a`: das zu partitionierende Array
- `kth`: Index (oder Liste von Indizes), an dem das Array partitioniert wird — das Element an
  dieser Position steht am Ende genau dort, wo es auch in einem vollständig sortierten Array
  stehen würde

Garantiert ist nur diese eine Position: Vor `kth` steht kein größerer Wert, dahinter kein
kleinerer.
In welcher Reihenfolge die Werte innerhalb dieser beiden Gruppen liegen, ist offen und kann je nach
NumPy-Version anders aussehen.
Wer die k kleinsten Werte auch sortiert braucht, muss das Teilstück deshalb selbst noch sortieren.
Das folgende Beispiel prüft die Garantie mit `np.all(bedingung)`, das genau dann `True` liefert,
wenn jedes Element des Boolean-Arrays `bedingung` `True` ist.

```python
import numpy as np

# 100 absteigende Werte: 100, 99, ..., 2, 1
arr = np.arange(100, 0, -1)

# Partitionierung: 3. kleinstes Element an Index 2
partitioned = np.partition(arr, 2)
print('3. kleinstes Element:', partitioned[2])  # 3

# Nur diese Position ist garantiert
print('Alles davor ist nicht größer:', np.all(partitioned[:2] <= partitioned[2]))  # True
print('Alles danach ist nicht kleiner:', np.all(partitioned[3:] >= partitioned[2]))  # True
print('Partitioniert = sortiert?', np.array_equal(partitioned, np.sort(arr)))  # False

# Innerhalb der Gruppen herrscht keine Ordnung, wie ein Ausschnitt aus der Mitte zeigt
# (welche Werte dort stehen, ist nicht festgelegt)
print('Ausschnitt ab Index 70:', partitioned[70:80])

# argpartition liefert Indizes, die dieselbe Garantie erfüllen
indices = np.argpartition(arr, 2)
print('3. kleinstes über Indizes:', arr[indices[2]])  # 3

# Mehrere k-Werte gleichzeitig
multi_part = np.partition(arr, [2, 50])
print('Elemente an Position 2 und 50:', multi_part[2], multi_part[50])  # 3 51
```

Bei kurzen Arrays sortiert NumPy intern vollständig, sodass der Unterschied zu `np.sort` erst bei
mehr als etwa 60 Elementen sichtbar wird.

Um den Zeitunterschied zwischen zwei Operationen zu messen, bietet Pythons Standardbibliothek das
`time`-Modul: `time.perf_counter()` gibt einen Zeitpunkt in Sekunden zurück, die Differenz zweier
Aufrufe ergibt also die Laufzeit dazwischen.
Eine einzelne Messung schwankt stark, deshalb misst man mehrfach und nimmt die kürzeste Zeit.
Mit der in [PARTREF::py-Fstrings] eingeführten f-String-Formatierung mit Präzisionsangabe (`:.5f`)
lässt sich die Ausgabe auf sinnvolle Nachkommastellen begrenzen:

```python
import time

zeiten_a = []
zeiten_b = []
for lauf in range(5):
    start = time.perf_counter()
    # ... erste Operation ...
    zeiten_a.append(time.perf_counter() - start)

    start = time.perf_counter()
    # ... zweite Operation ...
    zeiten_b.append(time.perf_counter() - start)
dauer_a = min(zeiten_a)
dauer_b = min(zeiten_b)
print(f'Kürzeste Dauer der ersten Operation: {dauer_a:.5f} Sekunden')
print(f'Kürzeste Dauer der zweiten Operation: {dauer_b:.5f} Sekunden')
```

[FOLDOUT::Warum genau so gemessen wird]
`time.perf_counter()` liefert die höchste verfügbare Auflösung und ist deshalb für kurze Laufzeiten
gedacht; `time.time()` liest dagegen die verstellbare Systemuhr ab.
Von mehreren Messungen ist die kürzeste die am wenigsten gestörte, denn fremde Last auf dem Rechner
kann eine Messung nur verlängern, nicht verkürzen.
Beide verglichenen Operationen laufen in derselben Schleife mit je eigener Zeitenliste, damit
Schwankungen der Maschine beide Messungen gleichmäßig treffen.
[ENDFOLDOUT]

[ER] Implementieren Sie effiziente Partitionierung und messen Sie den Zeitunterschied selbst:

- Erzeugen Sie mit `np.arange` ein großes Array `grosses_array` mit 1 Million absteigend
  angeordneten Werten (von `1000000` bis `1`)
- Setzen Sie in das Messgerüst oben die vollständige Sortierung mit `np.sort` und die
  Partitionierung mit `np.partition` für die 10 kleinsten Werte ein, jeweils als kürzeste Zeit aus
  5 Wiederholungen
- Geben Sie beide gemessenen Zeiten aus und berechnen Sie den Geschwindigkeitsfaktor
- Verwenden Sie `np.argpartition`, um die ursprünglichen Indizes der 10 kleinsten Werte zu erhalten

[HINT::Ich habe partitioniert, aber wie komme ich an die 10 kleinsten Werte?]
Nach `np.partition(grosses_array, 9)` stehen die 10 kleinsten Werte an den Positionen 0 bis 9, also
im Slice `[:10]` — allerdings in unbestimmter Reihenfolge, sodass sich für die Ausgabe ein
zusätzliches `np.sort` auf diesem Teilstück lohnt.
Dasselbe Slice angewendet auf das Ergebnis von `np.argpartition` liefert die zugehörigen Indizes im
ursprünglichen Array.
[ENDHINT]

[EQ] In [EREFR::5] haben Sie die Laufzeit von `np.partition` und `np.sort` auf demselben großen
Array gemessen.
Erklären Sie anhand Ihrer eigenen Messwerte, warum `np.partition` schneller ist, wenn Sie nur die
k kleinsten Elemente benötigen, nicht aber das gesamte Array in sortierter Reihenfolge.

<!-- time estimate: 20 min -->

### Weiterführend

- [NumPy-Referenz: Sortier-, Such- und Zählfunktionen](https://numpy.org/doc/stable/reference/routines.sort.html)
- [NumPy-Referenz zu `numpy.lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html)
- [NumPy-Referenz: Indexierungs-Routinen](https://numpy.org/doc/stable/reference/routines.indexing.html):
  darunter `numpy.take_along_axis` und `numpy.unravel_index`

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2]: die Reihenfolge in `keys` stimmt, die Ausgabe beginnt also mit Keyboard, Headset,
  Laptop.
  Bei vertauschten `keys` entsteht eine nach Preis sortierte Liste, die mit Mouse beginnt und
  ebenfalls plausibel aussieht
- [EREFQ::2]: in der Rechenregel für den flachen Index steht die Anzahl der **Spalten**; wer die
  Anzahl der Zeilen einsetzt, erhält am nicht-quadratischen 4×5-Array falsche Werte und hat damit
  auch die Frage nach der Formangabe verfehlt
- [EREFR::4]: `begrenzt` ist ein neues Array und `arr` bleibt unverändert, sonst liefert der
  letzte Arbeitsschritt nur noch die Werte 0 bis 5 statt -5 bis 5

### Fragen und Python-Dateien
[INCLUDE::ALT:np-sort-filter.md]

[ENDINSTRUCTOR]
