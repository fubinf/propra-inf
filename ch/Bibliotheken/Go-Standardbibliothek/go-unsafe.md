title: "Go: das Paket 'unsafe'"
stage: alpha
timevalue: 1
difficulty: 3
assumes: go-structs1, go-arrays-and-slices
---

[SECTION::goal::idea,experience]
Ich weiß, wie man das Typsystem in Go umgeht.
[ENDSECTION]


[SECTION::background::default]
In C oder C++ geben Zeiger ziemlich dem Programmierer viel Macht:
Ein Zeiger ist bloß eine Zahl — eine Speicheradresse.
Was man damit anfängt, ist einem überlassen, was ungeheure Möglichkeiten für Defekte eröffnet, die sehr subtil sein
können.

Im Gegensatz zu den "gefährlichen" Zeigern in C sind Zeiger in Go viel restriktiver.

In dieser Aufgabe geht es darum, wie man von high-level-Go-Zeigern zu low-level-C-Zeigern (Zahlendarstellungen von
Speicheradressen) kommt und wie das verwendet werden kann.
[ENDSECTION]


[TOC]


[SECTION::instructions::detailed]

### Reinterpretation

_Reinterpretation_ ist das Auslesen des rohen Bitmusters von Daten im Speicher, als wären sie ein anderer Datentyp, ohne
die Bytes zu konvertieren oder umzuwandeln.
(Nicht zu verwechseln mit Typumwandlung!)

Reinterpretation in C ist _relativ_ einfach — im folgenden Beispiel interpretiert der Compiler den Speicherbereich der
Variable `value` als eine Variable vom Typ `custom_type`:

```c
custom_type new_value = *((custom_type*) &value);
```

Dabei spielt es keine Rolle, ob die beiden Typen gleich groß sind oder nicht — die Kontrolle liegt vollständig beim
Entwickler.

In Go ist das nicht möglich — zumindest nicht ohne das Paket `unsafe`.


#### `uintptr` und `unsafe.Pointer`

Alle low-level-Manipulationen benutzten zwei Typen: `uintptr` und `unsafe.Pointer`.

- `uintptr` ist ein ganzzahliger Typ, der groß genug ist, um Bit-Muster aller Zeiger darstellen zu können.
  Wie jeder ganzzahlige Typ unterstützt `uintptr` Addition und Subtraktion.
- `unsafe.Pointer` ist ein Typ, der einen typisierten Go-Zeiger zu einem beliebigen/generischen konvertiert.
  `unsafe.Pointer` ist eine "Brücke" zwischen gewöhnlichen Go-Zeigern und `uintptr`-Variablen mit rohen
  Speicheradressen.

<!-- @LINK_SPEC: status=403 -->
Lesen Sie nun folgende Abschnitte aus dem Artikel
[Exploring ‘unsafe’ Features in Go 1.20: A Hands-On Demo](https://medium.com/@bradford_hamilton/exploring-unsafe-features-in-go-1-20-a-hands-on-demo-7149ba82e6e1):

- "Background: The Role of ‘Unsafe’ in Go" (Kommentar, warum das Paket nur sehr vorsichtig zu benutzen ist)
- "Some Notes on unsafe.Pointer and uintptr" (Konvertierung zwischen `*T`, `uintptr` und `unsafe.Pointer`)

[EQ] Wie kann man einen Typ `X` als einen beliebigen Typ `Y` _interpretieren_?
Erklären Sie mit Worten und/oder geben Sie einen Codeausschnitt als Beispiel an.

<!-- time estimate: 20 min -->


#### Programmieren: Probenanalyse

Sie analysieren drei Erzproben von einem abgelegenen Einschlagsort, aber das Spektralanalysegerät funktioniert nicht
richtig.
Statt Ordnungszahlen gibt es `float64`-Kalibrierdaten aus.

Die Notiz Ihres Vorgesetzten lautet:
"Die Ordnungszahlen sind als Bitmuster darin gefangen.
Die `float64`-Werte sind als `int`s zu interpretieren."

Proben:

```go
type Specimen struct {
    unknownData float64
}

var specimens = []Specimen{
    {1.3e-322},
    {1.4e-322},
    {3.9e-322},
}
```

[ER] Schreiben Sie eine Funktion `decode(s Specimen) Atom`, die die Proben zum Typ`Atom{atomicNumber: int}` umwandelt
und somit die Ordnungszahlen entschlüsselt.

[EQ] Welche Elemente sind das?

<!-- time estimate: 10 min -->


### Zeigerarithmetik

Eines der bekanntesten Features von Zeigern in C ist _Zeigerarithmetik_:

```c
[INCLUDE::include/go-c-pointer-arithmetics-example.c]
```

Im obigen Beispiel wurde die Variable `b` ausschließlich durch `a` und Manipulationen an Adressen verändert.

[FOLDOUT::Ich verstehe nicht, warum es subtrahiert wird]
<!-- @LINK_SPEC: status=403 -->
In C werden lokale Variablen auf dem
[Stack](https://wiki.osdev.org/Stack)
abgelegt.
Aus historischen Gründen wachsen Stacks auf den meisten heutigen Rechnerarchitekturen **nach unten**:
Das bedeutet, dass jede neue lokale Variable eine kleinere Speicheradresse bekommt, als die vorherige, also gilt
`&b` < `&a`.
[ENDFOLDOUT]

[FOLDOUT::Ich verstehe nicht, warum `-1` ausreicht: müsste es für `uint32_t` nicht 4 sein?]
Der Compiler erkennt, dass es sich um einen Zeiger auf `uint32_t` handelt, und skaliert die `1` automatisch zu `4` Bytes
um.

Also bedeutet `(&a - 1)` im Prinzip **eine Speicheradresse auf dem Stack, die 4 Bytes (eine `uint32_t`-Größe) weiter
unten als `&a` liegt.**
[ENDFOLDOUT]

Nun untersuchen Sie Adressen von Feldern einer Struktur in Go und bauen Sie die Zeigerarithmetik nach.

[ER] Definieren Sie eine Struktur `Vector` mit Feldern `x int` und `y int`.

[ER] Schreiben Sie eine Funktion `getAddressDifference()`, welche die Adressen von `Vector.x` und `Vector.y` sowie die
Adressendifferenz `Vector.y - Vector.x` als `uintptr` auf die Kommandozeile ausgibt.

[EQ] Probieren Sie die Funktion `getAddressDifference()` aus.
Basierend auf der Adressendifferenz, was können Sie über die Position der Variablen im Speicher sagen?

[ER] Schreiben Sie eine Funktion `manipulate()`, welche:

- eine Variable `v Vector` deklariert;
- anhand der Adresse von `v.x` die Adresse von `v.y` bestimmt, diese zu einem Go-Zeiger konvertiert (`*int`) und
  den Wert von `v.y` auf 42 setzt;
  (Für die Verschiebung von `&v.x` bietet sich `unsafe.Sizeof()` an, damit keine `int`-Größen fest eingebaut werden.)
- anschließend `v` auf die Kommandozeile ausgibt.

Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen:

```go
func main() {
    getAddressDifference()
    manipulate()
}
```

[EC] Führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Lösungen]

**Kommandoprotokoll**
[PROT::ALT:go-unsafe.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-unsafe.go].
[ENDINSTRUCTOR]