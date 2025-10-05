title: "Go: das Paket 'unsafe'"
stage: draft
timevalue: 1.25
difficulty: 3
assumes: go-basics, go-functions, go-structs1, go-pointers, go-arrays-and-slices
---

[SECTION::goal::idea,experience]
Ich kann das Go-Typsystem umgehen.
[ENDSECTION]

[SECTION::background::default]
In C oder C++ sind Zeiger ziemlich low-level und geben dem Programmierer viel Macht:
Ein Zeiger ist bloß eine Zahl — eine Speicheradresse.
Was man damit anfängt, ist einem überlassen, was ungeheure Möglichkeiten für Defekte eröffnet,
die sehr subtil sein können.

Im Gegensatz zu den "gefährlichen" Zeigern in C sind Zeiger in Go viel restriktiver.

In dieser Aufgabe geht es darum, wie man von high-level-Go-Zeigern zu low-level-C-Zeigern
(Zahlendarstellungen von Speicheradressen) kommt und wie das verwendet werden kann.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]
Dokumentation von `unsafe` finden Sie auf
[pkg.go.dev/unsafe](https://pkg.go.dev/unsafe).

### Reinterpretation

_Reinterpretation_ ist das Auslesen des rohen Bitmusters von Daten im Speicher,
als wären sie ein anderer Datentyp, ohne die Bytes zu konvertieren oder umzuwandeln.
(Nicht zu verwechseln mit Typumwandlung!)

Reinterpretation in C ist _relativ_ einfach — im folgenden Beispiel interpretiert
der Compiler den Speicherbereich des Werts `value` als einen Wert vom Typ `custom_type`:

```c
custom_type new_value = *((custom_type*) &value);
```

Dabei spielt es keine Rolle, ob die beiden Typen gleich groß sind oder nicht —
die Kontrolle liegt vollständig beim Entwickler.

In Go ist das nicht möglich — zumindest nicht ohne das Paket `unsafe`.


#### `uintptr` und `unsafe.Pointer`

Alle low-level-Manipulationen benutzten zwei Typen: `uintptr` und `unsafe.Pointer`.

- `uintptr` ist ein ganzzahliger Typ, der groß genug ist, um Bit-Muster aller
  Zeiger darstellen zu können.
  Wie jeder ganzzahlige Typ unterstützt `uintptr` Addition und Subtraktion.
- `unsafe.Pointer` ist ein Typ, der einen typisierten Go-Zeiger zu einem
  beliebigen/generischen konvertiert.
  `unsafe.Pointer` ist eine Art Brücke zwischen gewöhnlichen Go-Zeigern und `uintptr`-Zahlen
  mit Speicheradressen.
- (Das Lesen von
  [Dokumentation von `unsafe.Pointer`](https://pkg.go.dev/unsafe#Pointer)
  ist für diese Aufgabe nicht notwendig, aber sehr empfohlen.)

Lesen Sie nun folgende Abschnitte aus dem Artikel
[Exploring ‘unsafe’ Features in Go 1.20: A Hands-On Demo](https://medium.com/@bradford_hamilton/exploring-unsafe-features-in-go-1-20-a-hands-on-demo-7149ba82e6e1):

- **Background: The Role of ‘Unsafe’ in Go** (Kommentar, warum das Paket nur sehr
  vorsichtig zu benutzen ist)
- **Some Notes on unsafe.Pointer and uintptr** (Konvertierung zwischen `*T`, `uintptr`
  und `unsafe.Pointer`)

[EQ] Wie kann man einen Typ `X` als einen beliebigen Typ `Y` _interpretieren_?

<!-- time estimate: 10 min -->


#### Programmieren: Probenanalyse

Sie analysieren drei Erzproben von einem abgelegenen Einschlagsort, aber das
Spektralanalysegerät funktioniert nicht richtig.
Statt Ordnungszahlen gibt es `float64`-Kalibrierdaten aus.

Die Notiz Ihren Vorgesetzten lautet:
"Die Ordnungszahlen sind als Bitmuster darin gefangen.
Die `float64`-Werte sind als `int`s zu interpretieren."

Proben:

```go
type Specimen struct {
    unknownData float64
}

specimens := []Specimen{
    {1.3e-322},
    {1.4e-322},
    {3.9e-322},
}
```

[ER] Schreiben Sie eine Funktion `decode(s Specimen) Atom`, die die Proben zum Typ
`Atom{atomicNumber: int}` umwandelt und somit die Ordnungszahlen entschlüsselt.

[EQ] Welche Elemente sind das?
Was könnte ihre Kombination über die Herkunft der Proben verraten?

<!-- time estimate: 10 min -->


### Zeigerarithmetik

Eines der bekanntesten Features von Zeigern in C ist _Zeigerarithmetik_:

```c
[INCLUDE::include/go-c-pointer-arithmetics-example.c]
```

Im obigen Beispiel wurde die Variable `b` ausschließlich durch `a` und Manipulationen
an Adressen verändert.

[HINT::Ich verstehe nicht, warum es subtrahiert wird]
In C werden lokale Variablen auf dem
[Stack](https://wiki.osdev.org/Stack)
abgelegt.
Aus historischen Gründen wachsen Stacks auf den meisten heutigen Rechnerarchitekturen
__nach unten__:
Das bedeutet, dass jede neue lokale Variable eine kleinere Speicheradresse bekommt,
als die vorherige, also `&b` < `&a`.
[ENDHINT]

[HINT::Ich verstehe nicht, warum `- 1` ausreicht: müsste es für `uint32_t` nicht 4 sein?]
Der Compiler erkennt, dass es sich um einen Zeiger auf `uint32_t` handelt, und
skaliert die `1` automatisch zu `4` Bytes um.

Also bedeutet `(&a - 1)` im Prinzip __eine Speicheradresse,
die 4 Bytes (eine `uint32_t`-Größe) früher als `&a` liegt.__
[ENDHINT]

Jetzt bauen Sie die Zeigerarithmetik in Go nach.


#### Programmieren

[ER] Definieren Sie eine Struktur `Vector` mit Feldern `x int` und `y int`.

[ER] Schreiben Sie eine Funktion `getAddressDifference()`, welche zuerst die Adressen
von `Vector.x` und `Vector.y` und danach die Adressendifferenz `Vector.y - Vector.x`
als `uintptr` auf die Kommandozeile ausgibt.

[EQ] Probieren Sie die Funktion `getAddressDifference()` aus.
Basierend auf der Adressendifferenz, was können Sie über die Position
der Variablen im Speicher sagen?

[ER] Schreiben Sie eine Funktion `manipulate()`, welche:

- eine Variable `v Vector` deklariert;
- anhand der Adresse von `v.x` die Adresse von `v.y` bestimmt,
  diese zu einem Go-Zeiger konvertiert (`*int`) und den Wert von `v.y` auf 42 setzt;
  (Für die Verschiebung von `&a` bietet sich `unsafe.Sizeof()` an,
  damit keine `int`-Größen fest eingebaut werden.)
- anschließend `v` auf die Kommandozeile ausgibt.

<!-- time estimate: 15 min -->


### Praxis: Slices untersuchen

In [PARTREF::go-arrays-and-slices] haben Sie Slices kennengelernt.
Außerdem wissen Sie bereits, dass Slices ein _Mehrblocktyp_ sind.


#### Slice-Header

Der Header eines Slice sieht so aus (definiert in `go/src/runtime/slice.go`):

```go
type slice struct {
array unsafe.Pointer
len   int
cap   int
}
```

Die drei Felder sind kleingeschrieben und deswegen _privat_, also wir können auf
sie nicht direkt zugreifen.
Nicht ohne das Paket `unsafe`.

[ER] Implementieren Sie eine Funktion `myLen(s []int) int`, die `s` zum Typ
`slice` umwandelt und `slice.len` ausgibt.

[ER] Implementieren Sie eine Funktion `myCap(s []int) int`, die `s` zum Typ
`slice` umwandelt und `slice.cap` ausgibt.

[ER] Implementieren Sie eine Funktion `myPtr(s []int) int`, die `s` zum Typ
`slice` umwandelt und `slice.array` ausgibt.

[ER] Implementieren Sie eine weitere Funktion `printData(s []int)`, die alle wichtigen
Daten des Slice-Headers auf die Kommandozeile ausgibt: __die Länge__ des Slice,
__die Kapazität__ und __den Zeiger__ auf das zugrundeliegende Array.
Verwenden Sie dafür folgendes Format: `"len(s) = %2v, cap(s) = %2v, &s = %v\n"`.
Benutzen Sie außerdem die oben spezifizierten Funktionen.

<!-- time estimate: 15 min -->


#### 'append'

Hier sehen Sie sich die Funktion `append` genauer an,
indem Sie einen Slice erstellen und diesem Zahlen hinzufügen.

[ER] Implementieren Sie eine Funktion `testAppend()`, in der Sie zunächst einen
leeren `int`-Slice anlegen und dessen Informationen mit `printData(s)` auf die Kommandozeile
ausgeben lassen.
Anschließend fügen Sie dem Slice nacheinander 10 Zahlen hinzu und rufen nach jedem
Einfügen `printData(s)` auf.

[ER] Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen:

```go
func main() {
    getAddressDifference()
    manipulate()
    testAppend()
}
```

[EC] Führen Sie Ihr Programm mittels `go run` aus.

[EQ] Wann wird ein neues Array angelegt?
Wie groß ist das neue Array?
Kennen Sie eine Datenstruktur mit ähnlicher Funktionsweise?

[HINT::Woher weiß ich, dass ein neues Array erzeugt wurde?]
Das erkennen Sie an der Speicheradresse, die die Funktion `myPtr(s []int)` ausliest.

Gleiche Speicheradresse, gleiches Array.
Eine neue Adresse signalisiert, dass ein neues Array angelegt wurde.
[ENDHINT]

Eine derartige Datenstruktur ist in der Informatik als
[dynamisches Array](https://en.wikipedia.org/wiki/Dynamic_array)
bekannt.

<!-- time estimate: 10 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
[EREFQ::2]: Studierende müssen auf Fe-Ni-Au gekommen sein; der Teil über die Herkunft
der Proben ist völlig optional.

[EREFR::5] und [EREFR::6]: die eingebauten Funktionen `len()` und `cap()` dürfen __nicht__
verwendet werden.

[EREFR::9]:
ist die Ausgabe für `cap(s)` gleich, so müssen auch Adressen von `&s` übereinstimmen.

**Kommandoprotokoll**
[PROT::ALT:go-unsafe.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-unsafe.go].
[ENDINSTRUCTOR]