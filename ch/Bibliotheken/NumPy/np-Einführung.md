title: np-Einführung
stage: draft
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea,experience]

- Ich verstehe die Bedeutung und Anwendungsgebiete von NumPy in der wissenschaftlichen Datenverarbeitung.
- Ich kann NumPy erfolgreich installieren und die Installation verifizieren.
- Ich verstehe die Grundlagen des ndarray-Objekts und seine Eigenschaften.
- Ich kenne die wichtigsten NumPy-Datentypen und deren Verwendung.
- Ich kann einfache NumPy-Arrays erstellen und grundlegende Operationen durchführen.

[ENDSECTION]

[SECTION::background::default]

NumPy (Numerical Python) ist eine fundamentale Bibliothek für wissenschaftliches Rechnen in Python. 
Sie stellt leistungsstarke N-dimensionale Array-Objekte zur Verfügung und ist die Grundlage für viele 
andere wissenschaftliche Python-Bibliotheken wie SciPy und Matplotlib. 
In dieser Aufgabe lernen wir die Grundlagen von NumPy kennen und machen erste praktische Erfahrungen 
mit der Erstellung und Manipulation von Arrays.

[ENDSECTION]

[SECTION::instructions::detailed]

### NumPy und sein Ökosystem verstehen

NumPy bildet das Fundament des wissenschaftlichen Python-Ökosystems. Es wird häufig zusammen mit 
anderen Bibliotheken verwendet:

- **SciPy** (Scientific Python): Erweitert NumPy um Algorithmen für Optimierung, lineare Algebra, 
  Integration, Interpolation und andere wissenschaftliche Berechnungen
- **Matplotlib**: Ermöglicht die Visualisierung von Daten und erstellt Diagramme und Grafiken
- **Pandas**: Bietet Datenstrukturen und Analysewerkzeuge für strukturierte Daten

Diese Kombination stellt eine mächtige Alternative zu MATLAB dar und ermöglicht umfassende 
Datenanalyse und maschinelles Lernen in Python.

Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[NumPy User Guide](https://numpy.org/doc/stable/user/index.html)

[EQ] Nennen Sie drei wichtige Bibliotheken, die auf NumPy aufbauen, und beschreiben Sie 
deren Hauptanwendungsgebiete.
<!-- EQ1 -->

### NumPy Installation und Verifikation

NumPy ist nicht in der Standard-Python-Installation enthalten und muss separat installiert werden.

**Installation mit pip:**
```python
pip3 install numpy
```

**Installation mit conda (bei Anaconda/Miniconda):**
```python
conda install numpy
```

**Installation mit verbesserter Performance:**
```python
pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

[NOTICE]
Die conda-Installation bringt oft optimierte mathematische Bibliotheken (wie Intel MKL) mit, 
die die Performance erheblich verbessern können.
[ENDNOTICE]

**Verifikation der Installation:**
```python
import numpy as np
print(np.__version__)
```

[ER] Schreiben Sie ein Python-Programm, das NumPy importiert, die Version ausgibt und 
überprüft, ob die Installation erfolgreich war. Geben Sie eine entsprechende Erfolgsmeldung aus.
<!-- ER1 -->

<!-- time estimate: 10 min -->

### Das ndarray-Objekt verstehen

Das wichtigste Element von NumPy ist das N-dimensionale Array-Objekt (`ndarray`). Es unterscheidet 
sich wesentlich von Python-Listen:

**Wichtige Eigenschaften des ndarray:**
- Homogene Datentypen: Alle Elemente haben den gleichen Datentyp
- Feste Größe: Die Größe wird bei der Erstellung festgelegt
- Effizienter Speicher: Zusammenhängender Speicherbereich
- Schnelle Operationen: Optimierte mathematische Berechnungen

**Interne Struktur eines ndarray:**
- Zeiger auf Daten im Speicher
- Datentyp-Beschreibung (dtype) 
- Shape-Tupel für Dimensionen
- Stride-Tupel für Speicher-Navigation

Unklar? Dann bitte hier nochmal in anderer Form nachlesen:
[NumPy ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)

[EQ] Erklären Sie drei wesentliche Unterschiede zwischen einem NumPy ndarray und einer Python-Liste.
<!-- EQ2 -->

### Arrays erstellen mit numpy.array()

Die grundlegende Funktion zur Array-Erstellung ist `numpy.array()`:

```python
numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
```

**Parameter-Bedeutung:**
- `object`: Array oder verschachtelte Sequenz
- `dtype`: Datentyp der Array-Elemente (optional)
- `copy`: Ob eine Kopie erstellt werden soll (optional)
- `order`: Speicher-Layout ('C' für zeilenweise, 'F' für spaltenweise)
- `ndmin`: Minimale Anzahl der Dimensionen

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
1. Ein 1D-Array mit den Zahlen 10, 20, 30, 40, 50
2. Ein 2D-Array (3x2) mit den Werten [[1, 2], [3, 4], [5, 6]]
3. Ein Array mit mindestens 2 Dimensionen aus der Liste [7, 8, 9] (verwenden Sie ndmin)
<!-- ER2 -->

<!-- time estimate: 15 min -->

### NumPy-Datentypen verstehen

NumPy unterstützt viel mehr Datentypen als Standard-Python und orientiert sich an C-Datentypen:

**Wichtige NumPy-Datentypen:**
- `bool_`: Boolesche Werte (True/False)
- `int8`, `int16`, `int32`, `int64`: Vorzeichenbehaftete Ganzzahlen verschiedener Größen
- `uint8`, `uint16`, `uint32`, `uint64`: Vorzeichenlose Ganzzahlen
- `float16`, `float32`, `float64`: Gleitkommazahlen verschiedener Präzision
- `complex64`, `complex128`: Komplexe Zahlen

**Beispiel für explizite Datentyp-Angabe:**
```python
# Array mit komplexen Zahlen
c = np.array([1, 2, 3], dtype=complex)
print(c)  # [1.+0.j 2.+0.j 3.+0.j]
```

Zur Vertiefung: Weitere Informationen finden Sie hier:
[NumPy Data Types](https://numpy.org/doc/stable/user/basics.types.html)

[ER] Erstellen Sie Arrays mit verschiedenen Datentypen:
1. Ein Array [100, 200, 300] vom Typ `int16`
2. Ein Array [1.5, 2.7, 3.14] vom Typ `float32`  
3. Ein Array [1, 2, 3] vom Typ `complex64`
Geben Sie jeweils das Array und seinen dtype aus.
<!-- ER3 -->

### dtype-Objekte verwenden

Das `dtype`-Objekt beschreibt die Interpretation der Bytes im Array-Speicher:

```python
# dtype aus String erstellen
dt1 = np.dtype('i4')  # 32-bit Integer
print(dt1)  # int32

# dtype aus Typ erstellen  
dt2 = np.dtype(np.int32)
print(dt2)  # int32

# Byte-Reihenfolge spezifizieren
dt3 = np.dtype('<i4')  # Little-endian 32-bit Integer
print(dt3)  # int32
```

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
- 'matrikelnr': 32-bit Integer
- 'name': String mit maximal 15 Zeichen  
- 'note': 32-bit Float
Fügen Sie drei Beispiel-Studenten hinzu und geben Sie nur die Namen aus.
<!-- ER4 -->

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
<!-- EQ3 -->

[ER] Erstellen Sie ein 3D-Array der Form (2, 3, 4) mit beliebigen Integer-Werten und 
geben Sie folgende Eigenschaften aus:
- shape, ndim, size, dtype, itemsize
<!-- ER5 -->

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
1. Addition der beiden Arrays
2. Multiplikation des ersten Arrays mit 3
3. Umformung des Ergebnisses aus (1) in ein 2x2-Array
<!-- ER6 -->

<!-- time estimate: 15 min -->

### Zusammenfassung und Ausblick

NumPy ist die Grundlage für wissenschaftliches Rechnen in Python. Die wichtigsten Konzepte sind:

- **ndarray**: Effiziente N-dimensionale Arrays mit homogenen Datentypen
- **dtype**: Flexible Datentyp-Definition für verschiedene Anwendungen
- **Array-Operationen**: Schnelle element-weise mathematische Berechnungen

Diese Grundlagen ermöglichen komplexere Datenanalysen mit Bibliotheken wie Pandas, 
maschinelles Lernen mit scikit-learn und Visualisierungen mit Matplotlib.

Falls noch Fragen offen sind, hilft diese Ressource weiter:
[NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)

[EQ] Fassen Sie in eigenen Worten zusammen, warum NumPy für die wissenschaftliche 
Datenverarbeitung in Python so wichtig ist. Nennen Sie mindestens drei Gründe.
<!-- EQ4 -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:np-Einführung.md]

[ENDINSTRUCTOR]
