title: NumPy Array-Eigenschaften verstehen und anwenden
stage: alpha
timevalue: 1.25
difficulty: 2
requires: np-Einführung
---

[SECTION::goal::idea,experience]

- Ich kann die Achsen-Struktur von NumPy-Arrays interpretieren und besondere Attribute wie
  Real- und Imaginärteil komplexer Arrays nutzen.
- Ich kann Arrays mit vordefinierten Werten sowie Arrays mit gleicher Form wie ein bestehendes Array erzeugen.

[ENDSECTION]

[SECTION::background::default]

NumPy-Arrays haben Eigenschaften, die ihre Struktur und ihren Inhalt beschreiben. Diese Aufgabe
behandelt die wichtigsten Attribute und die grundlegenden Funktionen zum Erstellen von Arrays.

[ENDSECTION]

[SECTION::instructions::detailed]

NumPy-Arrays (`ndarray`-Objekte) haben verschiedene wichtige Eigenschaften, die uns Informationen
über die Struktur und den Inhalt der Daten geben. Die wichtigsten Eigenschaften wie `ndim`,
`shape`, `size`, `dtype` und `itemsize` sowie die konkreten NumPy-Datentypen (z.B. `int8`,
`int32`, `float32`, `float64`, `complex64`) wurden bereits in [PARTREF::np-Einführung] eingeführt;
diese Aufgabe vertieft den Umgang mit ihnen und ergänzt Funktionen zum gezielten Erstellen von
Arrays.

### Achsen verstehen: `axis`

Jede einzelne Dimension wird auch als **Achse** (englisch: axis) bezeichnet und durchnummeriert:
Achse 0 ist die erste Dimension, Achse 1 die zweite, usw. — die Zahl an Position `i` in `shape`
gibt also die Größe von Achse `i` an. Diese Nummerierung begegnet Ihnen in späteren Aufgaben
wieder, wenn Funktionen ein `axis`-Argument entgegennehmen, um festzulegen, entlang welcher
Dimension eine Operation ausgeführt werden soll.

```python
import numpy as np

c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print("shape:", c.shape)              # Ausgabe: (3, 5)
print("Achse 0 (Länge):", c.shape[0])  # Ausgabe: 3
print("Achse 1 (Länge):", c.shape[1])  # Ausgabe: 5
```

[EQ] Ein anderes Array `b` hat `b.shape` gleich `(2, 3)`. Welche Achse (0 oder 1) hat die
Länge 2, welche die Länge 3? Wie kommen Sie anhand der Position in `shape` auf diese
Zuordnung?
<!-- EQ1 -->

[ER] Erstellen Sie ein dreidimensionales Array der Form `(3, 4, 2)` mit den Werten `1` bis `24`. Geben
Sie `shape` und `ndim` aus, und listen Sie für jede der drei Achsen (0, 1, 2) auf, wie viele
Elemente sie jeweils enthält.
<!-- ER1 -->
<!-- time estimate: 15 min -->

### Real- und Imaginärteil: `.real` und `.imag`

Bei komplexen Datentypen wie `complex64` gibt es neben `size`, `dtype` und `itemsize` noch zwei
weitere nützliche Attribute: `.real` und `.imag` liefern Real- bzw. Imaginärteil als eigenes
Array.

```python
import numpy as np

c = np.array([1+2j, 3-4j], dtype=np.complex64)
print("Array:", c)
print("Realteil:", c.real)        # [1. 3.]
print("Imaginärteil:", c.imag)    # [ 2. -4.]
print("dtype von .real:", c.real.dtype)  # float32
```

[ER] Erstellen Sie Arrays mit verschiedenen Datentypen und analysieren Sie diese:

- Ein Array mit `dtype=np.int8` und Werten [10, 20, 30, 40, 50]
- Ein Array mit `dtype=np.float32` und Werten [1.5, 2.7, 3.9]
- Ein Array mit `dtype=np.complex64` und zwei komplexen Zahlen

Geben Sie für jedes Array `size`, `dtype` und `itemsize` aus. Geben Sie außerdem für das
`complex64`-Array die Attribute `.real` und `.imag` sowie deren `dtype` aus.
<!-- ER2 -->

[EQ] Sie haben in [EREFR::2] gesehen, dass ein `complex64`-Array `itemsize=8` hat, während
`.real` (`float32`) `itemsize=4` hat. Ohne es auszuprobieren: Welches `itemsize` erwarten Sie
für `.real` eines `complex128`-Arrays? Warum ist das Verhältnis zwischen einem komplexen Typ und
seinem `.real`-Typ immer exakt 2:1 und kann kein anderer Faktor sein?
<!-- EQ2 -->
<!-- time estimate: 25 min -->

### Array-Erstellung mit vordefinierten Werten

NumPy bietet verschiedene Funktionen zum Erstellen von Arrays mit vordefinierten Werten:

```python
numpy.empty(shape, dtype=None)
numpy.zeros(shape, dtype=None)
numpy.ones(shape, dtype=None)
numpy.full(shape, fill_value, dtype=None)
```

- `shape`: Ziel-Form des neuen Arrays (Tupel, z.B. `(2, 3)`)
- `dtype` (Standard `None`, was intern zu `float64` aufgelöst wird; bei `full` wird ohne
  Angabe der Typ stattdessen aus `fill_value` abgeleitet): Datentyp der Elemente
- `fill_value` (nur `full`): der Wert, mit dem alle Elemente gefüllt werden

```python
import numpy as np

# Leeres Array (uninitialisierte Werte)
empty_arr = np.empty((2, 3), dtype=int)

# Array mit Nullen
zeros_arr = np.zeros((2, 3))

# Array mit Einsen  
ones_arr = np.ones((2, 3))

# Array mit einem bestimmten Wert
full_arr = np.full((2, 3), 7)
```

[ER] Rufen Sie sowohl `np.empty((2, 3), dtype=int)` als auch `np.zeros((2, 3), dtype=int)`
jeweils zweimal in getrennten Aufrufen auf und geben Sie alle vier Ergebnisse aus.
<!-- ER3 -->

[EQ] In [EREFR::3] haben Sie `np.empty` und `np.zeros` jeweils zweimal mit identischen
Argumenten aufgerufen. Warum unterscheiden sich die beiden `np.empty`-Ergebnisse, während die
beiden `np.zeros`-Ergebnisse identisch sind?
<!-- EQ3 -->

[HINT::Was bedeutet `np.empty`?]
Schauen Sie in der [NumPy-Dokumentation zu `np.empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html)
nach der Beschreibung der Funktion.
[ENDHINT]

[ER] Verwenden Sie die verschiedenen Array-Erstellungsfunktionen:

- Erstellen Sie ein 3×4 Array mit `np.zeros` und `dtype=np.int32`
- Erstellen Sie ein 2×2×3 Array mit `np.ones` und `dtype=np.float32`
- Erstellen Sie ein 5×2 Array mit `np.full`, gefüllt mit dem Wert 3.14
- Erstellen Sie ein 4×4 Array mit `np.empty` und `dtype=np.float64`

Zeigen Sie für jedes Array seine `shape`, `dtype` und die ersten Werte an.
<!-- ER4 -->
<!-- time estimate: 15 min -->

### Arrays aus bestehenden Arrays erstellen

NumPy bietet Funktionen wie `zeros_like`, `ones_like` und `full_like`, um Arrays
mit derselben Form (und optional demselben `dtype`) wie ein bestehendes Array zu erstellen:

```python
numpy.zeros_like(a, dtype=None)
numpy.ones_like(a, dtype=None)
numpy.full_like(a, fill_value, dtype=None)
```

- `a`: das Vorlage-Array, dessen `shape` (und ohne weitere Angabe auch `dtype`) übernommen wird
- `dtype` (Standard `None`): überschreibt bei Angabe den `dtype` von `a`
- `fill_value` (nur `full_like`): der Wert, mit dem alle Elemente gefüllt werden

```python
import numpy as np

# Ursprüngliches Array
original = np.array([[1, 2, 3], [4, 5, 6]])

# Arrays mit gleicher Form erstellen
# zeros_like: gleiche shape/dtype wie original, aber mit Nullen gefüllt
zeros_similar = np.zeros_like(original)
# ones_like: gleiche shape/dtype wie original, aber mit Einsen gefüllt
ones_similar = np.ones_like(original)
# full_like: gleiche shape/dtype wie original, aber mit dem Wert 9 gefüllt
full_similar = np.full_like(original, 9)

print("Original shape:", original.shape)
print("Zeros like shape:", zeros_similar.shape)
print("Ones like shape:", ones_similar.shape)
print("Full like shape:", full_similar.shape)
```

Um zu prüfen, ob zwei Arrays exakt übereinstimmen (nicht nur `shape`, sondern auch die
Werte an jeder Position), bietet NumPy `array_equal`:

```python
numpy.array_equal(a1, a2)
```

- `a1`, `a2`: die zu vergleichenden Arrays; gibt `True` zurück, wenn beide dieselbe Form
  und an jeder Position denselben Wert haben

```python
print("full_similar gleich original?", np.array_equal(full_similar, original))  # False
print("original gleich original?", np.array_equal(original, original))  # True
```

[EQ] Sie könnten `np.zeros_like(original)` auch durch `np.zeros(original.shape, dtype=original.dtype)`
ersetzen. Welchen praktischen Vorteil bietet `zeros_like` gegenüber dieser manuellen Variante?
<!-- EQ4 -->

[ER] Erstellen Sie ein komplexes Array als Grundlage:

- Beginnen Sie mit dem Array `np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`
- Verwenden Sie `np.zeros_like()` um ein Array gleicher Form mit Nullen zu erstellen
- Verwenden Sie `np.ones_like()` um ein Array gleicher Form mit Einsen zu erstellen
- Verwenden Sie `np.full_like()` um ein Array gleicher Form zu erstellen, gefüllt mit dem Wert 5
- Wiederholen Sie `np.zeros_like()`, diesmal mit `dtype=np.float32`
- Vergleichen Sie die beiden `zeros_like`-Ergebnisse (Standard-`dtype` und `dtype=np.float32`)
  mit `np.array_equal()` — gelten sie trotz unterschiedlichem `dtype` als gleich?

Zeigen Sie alle Arrays und ihre Eigenschaften (`shape`, `dtype`) an.
<!-- ER5 -->
<!-- time estimate: 20 min -->

### Weiterführend

- [NumPy Array Attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes) – Vollständige Referenz aller ndarray-Attribute
- [Array Creation Routines](https://numpy.org/doc/stable/reference/routines.array-creation.html) – Übersicht aller Array-Erstellungsfunktionen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] Studierende ordnen allen drei Achsen des 3D-Arrays korrekt die jeweilige Länge aus
  `shape` zu (Achse 0 → 3, Achse 1 → 4, Achse 2 → 2).
- [EREFQ::2] Studierende erkennen, dass ein komplexer Typ intern aus zwei Fließkommazahlen
  gleicher Präzision (Real- und Imaginärteil) besteht, weshalb das Verhältnis immer exakt 2:1
  ist, und sagen für `complex128` korrekt `itemsize=8` für `.real` voraus (statt nur die
  gegebenen Zahlen zu wiederholen).
- [EREFQ::3] Studierende berufen sich auf die offizielle Dokumentation ("without initializing
  entries") und erkennen, dass die Werte undefiniert sind, statt zu vermuten, es gäbe einen
  Fehler oder Zufallszahlen würden gezielt erzeugt.

### Fragen und Python-Dateien
[INCLUDE::ALT:np-array.md]

[ENDINSTRUCTOR]
