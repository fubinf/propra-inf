title: Einführung von NumPy
stage: alpha
timevalue: 1.5
difficulty: 1
---

[SECTION::goal::idea,experience]

- Ich kann NumPy installieren und grundlegende Arrays erstellen.
- Ich kenne die wichtigsten NumPy-Datentypen und deren grundlegende Verwendung.
- Ich kann grundlegende Array-Eigenschaften auslesen und einfache Operationen durchführen.
[ENDSECTION]


[SECTION::background::default]
NumPy (Numerical Python) ist eine fundamentale Bibliothek für wissenschaftliches Rechnen in Python. 
Sie stellt leistungsstarke N-dimensionale Array-Objekte zur Verfügung und ist die Grundlage für viele 
andere wissenschaftliche Python-Bibliotheken wie 
[PARTREF::Pandas], [PARTREF::SciPy] und [PARTREF::Matplotlib]. 
[ENDSECTION]


[SECTION::instructions::detailed]

### NumPy installieren

NumPy ist nicht in der Standard-Python-Installation enthalten und muss separat installiert werden.

[EC] Installieren Sie NumPy mit pip:
```bash
pip3 install numpy
```

<!-- time estimate: 5 min -->

### Das ndarray-Objekt verstehen

Das wichtigste Element von NumPy ist das N-dimensionale Array-Objekt (`ndarray`). Es unterscheidet 
sich wesentlich von Python-Listen:

**Wichtige Eigenschaften des ndarray:**

- Homogene Datentypen: Alle Elemente haben den gleichen Datentyp
- Feste Größe: Die Größe wird bei der Erstellung festgelegt
- Vektorisierte Operationen: Mathematische Berechnungen werden elementweise auf das gesamte Array angewendet, ohne explizite Schleifen

[EQ] Erklären Sie drei wesentliche Unterschiede zwischen einem NumPy ndarray und einer Python-Liste.

### Arrays erstellen mit numpy.array()

Die grundlegende Funktion zur Array-Erstellung ist `numpy.array()`. Die für uns relevanten Parameter sind:

```python
numpy.array(object, dtype=None, ndmin=0)
```

**Parameter-Bedeutung:**

- `object`: Array oder verschachtelte Sequenz
- `dtype` (Standard `None`): Datentyp der Array-Elemente; bei `None` wird er automatisch aus den Daten abgeleitet
- `ndmin` (Standard `0`): erzwungene Mindestanzahl an Dimensionen. Ohne Angabe hat z.B. `np.array([7, 8, 9])` 1 Dimension;
  mit `ndmin=2` wird das Array künstlich auf 2 Dimensionen "aufgefüllt", `.shape` wird dann z.B. `(1, 3)` statt `(3,)`

Es gibt weitere optionale Parameter (`copy`, `order`, `subok`) für Spezialfälle, die wir hier nicht brauchen;
Details dazu finden Sie in der [offiziellen Dokumentation](https://numpy.org/doc/stable/reference/generated/numpy.array.html).

**Beispiele für Array-Erstellung:**

**1D-Array:**
```python
import numpy as np
a = np.array([1, 2, 3])
print(a)  # [1 2 3]
```

**2D-Array:**
```python
b = np.array([[1, 2], [3, 4]])
print(b)  
# [[1 2]
#  [3 4]]
```

[ER] Erstellen Sie die folgenden Arrays und geben Sie sie aus:

- Ein 1D-Array mit den Zahlen 10, 20, 30, 40, 50
- Ein 2D-Array (3x2) mit den Werten [[1, 2], [3, 4], [5, 6]]
- Ein Array mit mindestens 2 Dimensionen aus der Liste [7, 8, 9] (verwenden Sie ndmin)

<!-- time estimate: 25 min -->

### NumPy-Datentypen verstehen

NumPy unterstützt viel mehr Datentypen als Standard-Python und orientiert sich an C-Datentypen:

**Wichtige NumPy-Datentypen:**

- `bool_`: Boolesche Werte (True/False)
- `int8`, `int16`, `int32`, `int64`: Ganzzahlen verschiedener Größen (in Bits)
- `float16`, `float32`, `float64`: Gleitkommazahlen
- `complex64`, `complex128`: Komplexe Zahlen

**Beispiel für explizite Datentyp-Angabe:**
```python
# Array mit komplexen Zahlen
c = np.array([1, 2, 3], dtype=np.complex128)
print(c)  # [1.+0.j 2.+0.j 3.+0.j]
```

Sie können auch den eingebauten Python-Typ `complex` schreiben (`dtype=complex`) —
NumPy wandelt ihn automatisch in `np.complex128` um.

[ER] Erstellen Sie Arrays mit verschiedenen Datentypen:

- Ein Array [100, 200, 300] vom Typ `int16`
- Ein Array [1.5, 2.7, 3.14] vom Typ `float32`  
- Ein Array [1, 2, 3] vom Typ `complex64`
Geben Sie jeweils das Array und seinen dtype aus.
<!-- time estimate: 15 min -->

### dtype-Objekte verwenden

Das `dtype`-Objekt beschreibt, welchen Datentyp die Elemente eines Arrays haben und wie viel Speicherplatz sie belegen:

```python
# dtype aus Typ erstellen (üblicher, pythonischer Stil)
dt2 = np.dtype(np.int32)
print(dt2)  # int32

# dtype aus String erstellen (kompakte Kurzschreibweise)
dt1 = np.dtype('i4')  # 32-bit Integer
print(dt1)  # int32
```

Die Kurzschreibweise (`'i4'`, `'f4'`, `'U20'`, ...) stammt aus der C-nahen Array-Protokoll-Konvention
von NumPy und ist kein typischer Python-Stil (der Buchstabe steht für den Typ – `i` für Integer,
`f` für Float, `U` für Unicode-String –, die Zahl für die Größe in Bytes bzw. bei `U` für die
Zeichenanzahl). Für eigenen Code ist `np.int32` üblicher und lesbarer; die Kurzschreibweise begegnet
Ihnen aber häufig bei strukturierten Datentypen (siehe unten) und in fremdem Code, weshalb Sie sie
erkennen können sollten.

**Strukturierte Datentypen:**
```python
# Strukturierter dtype definieren
person_dtype = np.dtype([('name', 'U20'), ('age', 'i1'), ('height', 'f4')])
print(person_dtype)

# Array mit strukturiertem dtype
people = np.array([('Alice', 30, 165.5), ('Bob', 25, 180.0)], dtype=person_dtype)
print(people['name'])  # ['Alice' 'Bob']
```

[ER] Erstellen Sie ein strukturiertes Array für "Studenten" mit folgenden Feldern:

- `matrikelnr`: 32-bit Integer
- `name`: String mit maximal 15 Zeichen  
- `note`: 32-bit Float
Fügen Sie drei Beispiel-Studenten hinzu und geben Sie nur die Namen aus.

<!-- time estimate: 20 min -->

### Array-Eigenschaften erkunden

NumPy-Arrays haben wichtige Eigenschaften, die bei der Datenverarbeitung nützlich sind:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)    # (2, 3) - Dimensionen
print(arr.ndim)     # 2 - Anzahl Dimensionen  
print(arr.size)     # 6 - Gesamtanzahl Elemente
print(arr.dtype)    # int64 - Datentyp
print(arr.itemsize) # 8 - Bytes pro Element
```

[EQ] Ein Array hat die Form (4, 5, 3). Wie viele Dimensionen hat es, wie viele Elemente 
insgesamt, und welche Bedeutung haben die einzelnen Zahlen in der Form-Angabe?

[ER] Erstellen Sie ein 3D-Array der Form (2, 3, 4) mit beliebigen Integer-Werten und 
geben Sie folgende Eigenschaften aus:
- shape, ndim, size, dtype, itemsize
<!-- time estimate: 20 min -->

### Praktische Array-Operationen

**Einfache mathematische Operationen:**
```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# Element-weise Operationen
print(arr1 + arr2)   # [11 22 33 44]
print(arr1 * 2)      # [2 4 6 8]
print(arr2 / arr1)   # [10. 10. 10. 10.]
```

**Array-Umformung:**
```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
# [[1 2 3]
#  [4 5 6]]
```

[ER] Erstellen Sie zwei 1D-Arrays mit je 4 Elementen und führen Sie folgende Operationen durch:

- Addition der beiden Arrays
- Multiplikation des ersten Arrays mit 3
- Umformung des Ergebnisses aus (1) in ein 2x2-Array

<!-- time estimate: 10 min -->

### Weiterführend

- [NumPy ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) – Detaillierte Referenz zum `ndarray`-Objekt
- [NumPy Data Types](https://numpy.org/doc/stable/user/basics.types.html) – Übersicht aller NumPy-Datentypen

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
**Knackpunkte:**

- [EREFR::1]: Das dritte Array (`ndmin=2` auf `[7, 8, 9]`) hat die Shape `(1, 3)`, nicht `(3,)` – zeigt, ob `ndmin` wirklich verstanden wurde.
- [EREFR::3]: Der strukturierte dtype ist korrekt mit drei benannten Feldern definiert, und `students['name']` liefert nur die Namen (nicht das gesamte Tupel).
- [EREFQ::1]: Student nennt tatsächlich technische Unterschiede (z.B. homogene Datentypen, feste Größe, vektorisierte Operationen) statt nur allgemeiner Vorteile von NumPy.

### Kommandoprotokoll
[PROT::ALT:np-Einführung.prot]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-Einführung.md]

[ENDINSTRUCTOR]
