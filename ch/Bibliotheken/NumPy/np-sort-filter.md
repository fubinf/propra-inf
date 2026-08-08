title: NumPy Sortierung und Filterung verstehen und anwenden
stage: alpha
timevalue: 2
difficulty: 2
assumes: np-Einführung, np-array, np-array2, np-index-slice, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich kann Arrays sortieren und weiß, wann ich statt der sortierten Werte die Sortierungsindizes
  brauche.
- Ich kann aus zeilen- oder spaltenweisen Sortierungsindizes das sortierte Array rekonstruieren.
- Ich kann Arrays nach mehreren Kriterien mit unterschiedlicher Sortierrichtung sortieren.
- Ich kann Extremwerte lokalisieren und weiß, wie flacher Index und Zeilen-/Spaltenindex
  zusammenhängen.
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

### Grundlegende Sortierung: `sort`

Die grundlegende Sortierfunktion sortiert entlang einer wählbaren Achse:

```python
numpy.sort(a, axis=-1)
```

- `a`: das zu sortierende Array
- `axis` (Standard `-1`): Achse, entlang derer sortiert wird (`-1` = letzte Achse)

```python
import numpy as np

# Einfaches 2D-Array
arr = np.array([[30, 70], [90, 10]])
print('Ursprüngliches Array:')
print(arr)
# [[30 70]
#  [90 10]]

sorted_arr = np.sort(arr)
print('Sortiert (entlang letzter Achse):')
print(sorted_arr)
# [[30 70]
#  [10 90]]

# Sortierung entlang verschiedener Achsen
print('Sortiert entlang Achse 0 (innerhalb jeder Spalte):')
print(np.sort(arr, axis=0))
# [[30 10]
#  [90 70]]

print('Sortiert entlang Achse 1 (innerhalb jeder Zeile):')
print(np.sort(arr, axis=1))
# [[30 70]
#  [10 90]]
```

Bei einem 2D-Array ist die letzte Achse genau Achse 1, der erste und der letzte Aufruf sind hier
also gleichwertig.
`np.sort` lässt `arr` dabei unverändert und liefert ein neues Array mit eigenen Daten, also keine
View im Sinne von [PARTREF::np-index-slice].
Keine der Sortier-, Such- und Filterfunktionen dieser Aufgabe verändert das übergebene Array.
Die Methode `arr.sort()` dagegen sortiert an Ort und Stelle und überschreibt dabei die
Ausgangsdaten.

[EQ] Zwei Schreibweisen sollen für `arr = np.array([[30, 70], [90, 10]])` dieselbe zweite Zeile des
sortierten Arrays liefern, nämlich `np.sort(arr)[1]` und `arr.sort()[1]`.
Probieren Sie beide aus und übernehmen Sie die dabei auftretende Fehlermeldung in Ihre Antwort.
Geben Sie außerdem aus, was `arr.sort()` selbst zurückliefert und was danach in `arr` steht.
Erklären Sie damit, warum die eine Schreibweise abbricht.
Nennen Sie schließlich eine Situation, in der `arr.sort()` trotzdem der passendere Aufruf ist als
`np.sort(arr)`.

<!-- time estimate: 10 min -->

### Sortierungsindizes: `argsort` und `take_along_axis`

`np.argsort(a, axis=-1)` hat dieselben Parameter wie `np.sort`, gibt aber nicht die sortierten
Werte selbst zurück, sondern die Indizes, die die Elemente in sortierter Reihenfolge referenzieren:

```python
import numpy as np

# np.argsort() gibt Indizes zurück, die zur Sortierung führen
x = np.array([30, 10, 20])
indices = np.argsort(x)
print('Sortierungsindizes:', indices)  # [1 2 0]
print('Sortiertes Array:', x[indices])  # [10 20 30]
```

Bei einem 2D-Array liefert `np.argsort(a, axis=1)` für jede Zeile eigene Indizes.
Die Integer-Array-Indexierung `arr[indices]` aus [PARTREF::np-index-slice] rekonstruiert das
sortierte Array daraus nicht; je nach Form des Arrays liefert sie ein falsches Ergebnis oder bricht
mit einem `IndexError` ab.
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
  `zeilenindizes` zu erhalten, und geben Sie sie aus
- Versuchen Sie zunächst, das sortierte Array mit `werte[zeilenindizes]` zu rekonstruieren, und
  halten Sie in einem Kommentar fest, was dabei passiert und warum.
  Kommentieren Sie die Zeile danach aus, damit das abgegebene Skript durchläuft
- Rekonstruieren Sie das zeilenweise sortierte Array mit `np.take_along_axis`, geben Sie es aus und
  vergleichen Sie das Ergebnis mit `np.sort(werte, axis=1)`
- Ermitteln Sie ebenso die spaltenweisen Sortierungsindizes in `spaltenindizes`, rekonstruieren Sie
  daraus das spaltenweise sortierte Array und vergleichen Sie es mit `np.sort(werte, axis=0)`

[HINT::Wie vergleiche ich zwei Arrays auf Gleichheit?]
Nutzen Sie das bereits aus [PARTREF::np-array] bekannte `np.array_equal`, um die beiden
Arrays elementweise auf Übereinstimmung zu prüfen.
[ENDHINT]

[EQ] In [EREFR::1] haben Sie die `np.argsort`-Indizes und das zeilenweise sortierte Array
nebeneinander ausgegeben.
Welche Information steckt in den Indizes, die im Ergebnis von `np.sort` verloren geht?
Nennen Sie eine Situation, in der Sie deshalb `np.argsort` und nicht `np.sort` brauchen.

<!-- time estimate: 20 min -->

### Lexikographische Sortierung: `lexsort`

`np.lexsort` ermöglicht die Sortierung nach mehreren Kriterien,
ähnlich dem mehrstufigen Sortieren in Tabellenkalkulationen:

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
String-Arrays lassen sich nicht negieren; auf diesem Weg sind sie deshalb nur aufsteigend
sortierbar.

[ER] Sortieren Sie einen Datensatz lexikographisch nach zwei Kriterien:

- Erstellen Sie mit `np.array` drei Arrays: `produkte` mit den Werten
  `['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset']`, `preise` mit den Werten
  `[1200, 25, 75, 300, 150]` und `bewertungen` mit den Werten `[4.5, 4.2, 4.5, 4.0, 4.5]`
- Sortieren Sie die Produkte mit `np.lexsort` erst nach Bewertung (absteigend), dann nach Preis
  (aufsteigend), und geben Sie in dieser Reihenfolge für jedes Produkt Name, Preis und
  Bewertung aus
- Prüfen Sie Ihr Ergebnis: An erster Stelle steht weder das billigste noch das teuerste Produkt.
  Begründen Sie in einem Kommentar, warum dieses Produkt trotzdem vorne steht

[HINT::In welcher Reihenfolge muss ich die Arrays an `keys` übergeben?]
Die Reihenfolge in `keys` ist leicht zu verwechseln: Das **zuletzt** übergebene Array bestimmt
die Sortierung zuerst.
Im Punktebeispiel oben steht deshalb `gesamtpunkte` als letztes Element in `keys`, weil zuerst nach
der Gesamtpunktzahl sortiert werden soll und die Mathepunktzahl nur die Reihenfolge innerhalb
gleicher Gesamtpunktzahlen festlegt.
[ENDHINT]

<!-- time estimate: 20 min -->

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
Das Umrechnen eines flachen Index in Zeilen- und Spaltenindex übernimmt eine fertige Funktion:

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
- Bestimmen Sie die Indizes der Maxima jeder Zeile in `zeilen_max_indizes` und die der Minima jeder
  Spalte in `spalten_min_indizes`
- Verwenden Sie diese Indizes, um die tatsächlichen Werte auszugeben
- Aus den beiden Positionen des globalen Maximums und Minimums lässt sich eine Rechenregel
  vermuten, die den flachen Index aus Zeile und Spalte bestimmt.
  Sagen Sie mit dieser Regel den flachen Index des Maximums der letzten Zeile voraus, das bei
  Zeile 3, Spalte 1 liegt, und prüfen Sie die Vorhersage mit `np.unravel_index` nach

[HINT::Welche `axis` brauche ich für "pro Zeile"?]
Die Beispielaufrufe oben zeigen jeweils die andere Richtung als die hier verlangte; wer die
dortigen `axis`-Werte übernimmt, erhält das falsche Ergebnis.
Machen Sie sich die Nummerierung der Achsen aus [PARTREF::np-array] an einem kleinen 2×3-Array
klar.
Eine Reduktion entlang einer Achse lässt genau diese Achse verschwinden; an der Länge des
Ergebnisses erkennen Sie deshalb, ob pro Zeile oder pro Spalte gesucht wurde.
[ENDHINT]

[HINT::Wie komme ich von den achsenweisen Indizes zu den Werten?]
`np.argmax(daten, axis=1)` liefert pro Zeile nur die Spaltennummer; die zugehörige Zeilennummer ist
die Position innerhalb des Ergebnisses.
Für den Zugriff auf einen Wert werden beide Zahlen gebraucht: `daten[zeilennummer, spaltennummer]`.
Ein Zugriff mit nur einer davon wie `daten[zeilen_max_indizes]` liest diese als Zeilennummern und
liefert ganze Zeilen statt einzelner Werte, im Spaltenfall sogar ohne Fehlermeldung.
Am bequemsten ist eine Schleife über das Indexarray, die mit `enumerate` die Position mitführt.
[ENDHINT]

[EQ] In [EREFR::3] haben Sie aus den Positionen von Maximum und Minimum eine Rechenregel für den
flachen Index abgeleitet und an einer dritten Position nachgeprüft.
Geben Sie diese Regel an und nennen Sie, welche Angabe über die Form des Arrays in sie eingeht.
Die beiden ersten Positionen liegen allerdings so, dass auch andere Regeln zu ihnen passen.
Erklären Sie anhand Ihrer dritten Position, warum die Probe deshalb nötig war.

Die zeilenweise Anordnung, die dieser Regel zugrunde liegt, heißt C-Ordnung und ist in
[PARTREF::np-array2] bei `nditer` schon als Iterationsreihenfolge `order='C'` vorgekommen.

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

Ein Boolean-Ausdruck wie `a > 50` ist selbst ein Array aus `True` und `False`.
Da `True` als von Null verschieden zählt, liefert `np.nonzero(a > 50)` die Indizes aller Elemente
über 50.

```python
import numpy as np

arr = np.arange(10, 100, 10).reshape(3, 3)
print('Array:')
print(arr)

# Indizes aller Elemente > 50
indices = np.nonzero(arr > 50)
print('Indizes mit arr > 50:', indices)  # (array([1, 2, 2, 2]), array([2, 0, 1, 2]))
print('Werte an diesen Positionen:', arr[indices])  # [60 70 80 90]

# where() mit drei Argumenten wählt elementweise zwischen zwei Werten
arr_1d = np.arange(-10, 11)
absolute_values = np.where(arr_1d >= 0, arr_1d, -arr_1d)
print('Betrag über where(condition, x, y):', absolute_values)

# nonzero() ohne Vergleich findet die von Null verschiedenen Elemente
arr_mit_nullen = np.array([[10, 0, 30], [0, 25, 0], [40, 0, 50]])
print('Nicht-Null-Indizes:', np.nonzero(arr_mit_nullen))

# extract() liefert die Werte statt der Indizes
print('Durch 30 teilbar:', np.extract(arr % 30 == 0, arr))  # [30 60 90]
```

`np.nonzero` gibt keine Liste von Positionen zurück, sondern ein Tupel mit einem Indexarray je
Achse des Arrays.
Für ein 1D-Array besteht das Tupel deshalb aus genau einem Array, das man mit `[0]` herausholt.

Der Unterschied zur Boolean-Maske aus [PARTREF::np-index-slice] liegt darin, was man zurückbekommt:
`np.nonzero` liefert die Positionen, an denen die Bedingung zutrifft, die Auswahl über die Maske
dagegen die Werte.
Wann man die Positionen statt der Werte braucht, ist dabei dieselbe Frage wie die nach `np.sort`
gegenüber `np.argsort` aus [EREFQ::2].

`np.extract(condition, a)` ist bei einer Boolean-Bedingung dagegen nichts anderes als die
Boolean-Maske `a[condition]`.
Als eigene Funktion taucht sie trotzdem in fremdem Code und in der NumPy-Dokumentation auf,
weshalb man sie wiedererkennen können sollte.
`np.where(condition)` ohne `x` und `y` liefert dasselbe wie `np.nonzero(condition)`; die
NumPy-Dokumentation empfiehlt für diesen Fall aber ausdrücklich `np.nonzero`.

[ER] Verwenden Sie bedingte Suchfunktionen:

- Erzeugen Sie mit `np.arange` ein Array `arr` mit den ganzen Zahlen von -15 bis 15
- Finden Sie mit `np.nonzero` die Indizes aller positiven Werte und geben Sie auch die Werte an
  diesen Positionen aus
- Erzeugen Sie mit der Drei-Argument-Form `np.where(condition, x, y)` ein **neues** Array
  `begrenzt`, in dem alle negativen Werte durch `0` ersetzt sind und die übrigen Werte
  unverändert bleiben; `arr` selbst bleibt dabei unangetastet
- Erstellen Sie mit `np.array` ein 3×3-Array `mit_nullen` mit den Werten
  `[[0, 12, 0], [34, 0, 56], [0, 78, 0]]` und finden Sie darin die Nicht-Null-Elemente
- Klären Sie die Bedeutung des Rückgabewerts für dieses 2D-Array anhand der
  [Dokumentation zu `numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html)
  und erklären Sie Ihre Ausgabe in einem Kommentar
- Holen Sie alle Werte von -5 bis 5 aus `arr`, beide Grenzen eingeschlossen, auf zwei Wegen:
  einmal mit `np.extract` und einmal mit der Boolean-Maske aus [PARTREF::np-index-slice].
  Halten Sie in einem Kommentar fest, ob beide Wege dasselbe liefern

[HINT::Wie kombiniere ich zwei Bedingungen zu einer?]
Der letzte Arbeitsschritt braucht eine untere **und** eine obere Grenze.
Wie sich zwei Vergleiche zu einer einzigen Bedingung verbinden lassen und warum dabei die Klammern
nicht fehlen dürfen, steht in [PARTREF::np-index-slice].
[ENDHINT]

<!-- time estimate: 25 min -->

### Partitionierung: `partition` und `argpartition`

Partitionierung ordnet ein Array so um, dass an einer gewählten Position das Element steht,
das dort auch in einem vollständig sortierten Array stünde:

```python
numpy.partition(a, kth)      # gibt eine partitionierte Kopie von a zurück
numpy.argpartition(a, kth)   # gibt die Indizes zurück, die a partitionieren würden
```

- `a`: das zu partitionierende Array
- `kth`: Index (oder Liste von Indizes), an dem partitioniert wird

Garantiert ist nur diese eine Position: Vor `kth` steht kein größerer Wert, dahinter kein
kleinerer.
In welcher Reihenfolge die Werte innerhalb dieser beiden Gruppen liegen, ist offen und kann je nach
NumPy-Version anders aussehen.
Wer die `k` kleinsten Werte zusätzlich in sortierter Reihenfolge braucht, muss das Teilstück
deshalb selbst noch sortieren.
Das folgende Beispiel prüft die Garantie mit `np.all(condition)`, das genau dann `True` liefert,
wenn jedes Element des Boolean-Arrays `condition` `True` ist.

```python
import numpy as np

# 1000 absteigende Werte: 1000, 999, ..., 2, 1
arr = np.arange(1000, 0, -1)

# Partitionierung: 3. kleinstes Element an Index 2
partitioned = np.partition(arr, 2)
print('3. kleinstes Element:', partitioned[2])  # 3

# Nur diese Position ist garantiert
print('Alles davor ist nicht größer:', np.all(partitioned[:2] <= partitioned[2]))  # True
print('Alles danach ist nicht kleiner:', np.all(partitioned[3:] >= partitioned[2]))  # True
print('Partitioniert = sortiert?', np.array_equal(partitioned, np.sort(arr)))  # False

# Innerhalb der beiden Gruppen herrscht dagegen keine Ordnung
print('Hinterer Teil sortiert?', np.array_equal(partitioned[3:], np.sort(partitioned[3:])))  # False

# argpartition liefert Indizes, die dieselbe Garantie erfüllen
indices = np.argpartition(arr, 2)
print('3. kleinstes über Indizes:', arr[indices[2]])  # 3

# Mehrere Ranggrenzen in einem Durchgang festlegen
multi_part = np.partition(arr, [2, 50])
print('Elemente an Position 2 und 50:', multi_part[2], multi_part[50])  # 3 51
```

Bei kurzen Arrays sortiert NumPy intern ohnehin vollständig durch, sodass sich das Ergebnis dort
nicht von `np.sort` unterscheidet.
Ab welcher Länge der Unterschied auftritt, hängt vom internen Auswahlverfahren und von den Daten ab
und ist nicht zugesichert.

[INCLUDE::_include/Zeitmessung.md]

[ER] Vergleichen Sie Partitionierung und vollständige Sortierung anhand einer eigenen Zeitmessung:

- Erzeugen Sie mit `np.arange` ein großes Array `grosses_array` mit 1 Million absteigend
  angeordneten Werten (von `1000000` bis `1`)
- Setzen Sie in das Messgerüst oben die vollständige Sortierung mit `np.sort` und die
  Partitionierung mit `np.partition` für die 10 kleinsten Werte ein, jeweils als kürzeste Zeit aus
  5 Wiederholungen
- Geben Sie beide gemessenen Zeiten (5 Nachkommastellen, `:.5f`) aus und berechnen Sie daraus den
  Geschwindigkeitsfaktor (1 Nachkommastelle, `:.1f`).
  Zu erwarten ist ein einstelliger Faktor, keine Zehnerpotenz; der genaue Wert hängt von der
  Maschine ab
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
Belegen Sie mit Ihren eigenen Messwerten, dass `np.partition` schneller ist, und erklären Sie,
woher dieser Unterschied kommt, wenn nur die `k` kleinsten Elemente gebraucht werden und nicht das
gesamte Array in sortierter Reihenfolge.

<!-- time estimate: 25 min -->

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

### Fragen und Python-Dateien
[INCLUDE::ALT:np-sort-filter.md]

[ENDINSTRUCTOR]
