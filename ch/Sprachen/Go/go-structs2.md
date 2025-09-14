title: Weitere Grundlagen von Go — Strukturen (Teil 2)
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: go-basics, go-functions, go-pointers, go-structs1
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datentypen in Go definieren.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-structs1] haben sie bereits Strukturen kennengelernt.

In dieser Aufgabe handelt es sich um anonyme Strukturen, die leere Struktur und 
das Zusammenspiel von dem pass-by-value-Verhalten, Zeigern und Strukturen.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]


### Anonyme Strukturen

Lesen Sie die folgende
[Erklärung, was anonyme Strukturen sind](https://blog.boot.dev/golang/anonymous-structs-golang/)
.

[EQ] Welche Anwendungen von anonymen Strukturen erwähnt der Autor?

[EQ] Wie würden Sie einen Slice mit drei anonymen Strukturen instanziieren, die nur
die Felder `price`, `language` und `author` besitzen? 
Geben Sie den Codeabschnitt in Ihrer Markdown-Datei.

(Die konkreten Werte für die drei Felder dürfen Sie ausdenken.)

<!-- time estimate: 15 min -->


### Die leere Struktur

Die leere Struktur stellt einen Typ dar, dessen Größe 0 Byte beträgt.

Dieses Konstrukt wird in den Situationen benutzt, wo Ab- oder Anwesenheit
eines Wertes wichtiger ist als der Wert selbst.

```go
type emptyStruct struct{}
es := emptyStruct{}

// "anonyme" Schreibweise
es := struct{}{}
```

[FOLDOUT::0 Bytes groß? Wie?]
Der Trick ist, dass alle Instanzen von der leeren Struktur sich eine von dem
Compiler festgelegte Speicheradresse teilen — `zerobase`.

Go Compiler erkennt, dass so eine Struktur keine Felder besitzt und
dementsprechend keinen Speicherplatz braucht, und spart sich das Allokieren.

Falls Sie mehr zum Thema wissen wollen (könnte auch dann von Interesse sein, wenn 
Sie noch relativ frisch im Go-Universum sind):

- [Dave Cheney: The empty struct](https://dave.cheney.net/2014/03/25/the-empty-struct)
- [Decrypt Go: empty struct](https://dev.to/huizhou92/decrypt-go-empty-struct-5i4)
[ENDFOLDOUT]

[ER] Implementieren Sie eine Funktion namens `testEmptyStruct`, welche 3 Instanzen
von der leeren Struktur erzeugt und deren Adressen auf die Kommandozeile ausgibt.
Was fällt Ihnen auf?

[HINT::Die Adresse einer Variable ausgeben lassen]
Benutzen Sie die Funktion `fmt.Printf` mit dem `%p` Platzhalter — `p` steht für
"Pointer" und sorgt dafür, dass es tatsächlich die Speicheradresse angezeigt wird.

[HINT::Die Adresse einer Variable ermitteln]
Das _Referenzieren_ ermöglicht uns der Operator `&`.

`&variable` gibt die Adresse der Variable zurück.
[ENDHINT]
[ENDHINT]

<!-- time estimate: 10 min -->


### "Pass-by-value" und "Pass-by-reference"

In [PARTREF::go-pointers] haben Sie bereits gelernt, dass Funktionsargumente
beim Übergeben immer kopiert werden.

Daraus ergeben sich folgende Nachteile:

- eine Funktion kann die ursprünglichen Argumente nicht verändern (was manchmal
  gewünscht wäre);
- jeder Funktionsaufruf kopiert alle Argumente — ineffizient für große Strukturen.

```go
// Option 1
func processPerson(p Person) {
    ...
}

// Option 2
func processPerson(p *Person) {
    ...
}
```
Schauen Sie sich diese
[pass-by-value vs pass-by-reference Benchmark](https://blog.boot.dev/golang/pointers-faster-than-values/)
an.

[EQ] Was wäre ein guter Grund, Option 2 (übergabe per Zeiger) gegenüber
Option 1 (übergabe per Wert) zu bevorzugen?
Was wäre ein nicht so guter Grund?

[HINT::Hilfsfragen]

- Muss die Funktion etwas an Person ändern?
- Wie groß ist die Struktur `Person`?
[ENDHINT]

[FOLDOUT::Gibt es einen Punkt, ab dem die Laufzeiteffizienz deutlich beeinflusst wird?]
Kurze Antwort — ja, wenn die Struktur größer als 10MB ist.

Eine etwas längere Antwort finden Sie in dem Artikel:
[Go Benchmarks: Does Pass by Pointer Really Make a Difference?](https://dev.to/anubhav023/go-benchmarks-does-pass-by-pointer-really-make-a-difference-1540)
.
[ENDFOLDOUT]

[NOTICE]
**Automatisches Dereferenzieren**

Unabhängig davon, ob es sich um eine Struktur oder um einen Zeiger auf eine
Struktur handelt, darf man auf die Felder mit der `.`-Syntax zugreifen:

```go
p := Person{}
pptr := &Person{}

fmt.Println(p.Age) // 0
fmt.Println(pptr.Age) // 0
fmt.Println((*pptr).Age) // explizit (aber unnötig)
```
[ENDNOTICE]

[ER] Übernehmen Sie die Strukturen `Person` und `Employee` aus [PARTREF::go-structs1]. 
Implementieren Sie eine Methode `Promote` auf `Employee`, die ein Argument
`newPosition string` erwartet.
Sie soll die Struktur modifizieren und das Feld `Position` auf den neuen Wert setzen.

[ER] Implementieren Sie außerdem eine Methode `(e Employee) Print()`, die die Struktur 
im folgenden Format darstellt:
```go
fmt.Printf("%v %v, %v (%v)\n", e.FirstName, e.LastName, e.Age, e.Position)
```

[ER] Fügen Sie folgende Testfunktion in Ihre Datei ein:

```go
[INCLUDE::include/go-structs-mutation-control-snippet.go]
```

[ER] Stellen Sie sicher, dass Ihre `main`-Funktion genauso aussieht:

```go
func main() {
    testEmptyStruct()
    testMutation()
}
```

[EC] Führen Sie nun das Programm mittels `go run` aus.

<!-- time estimate: 20 min -->


### Speicherlayout (Alignment und Padding)

Es gibt Situationen, wo Reihenfolge der Felder einer Struktur tatsächlich einen Unterschied macht.

Ein wichtiger Begriff, den Sie nun kennenlernen müssen, ist _Alignment_.
Lesen Sie zunächst den
[Abschnitt: Type Alignment Guarantees in Go](https://go101.org/article/memory-layout.html)
.

[HINT::Zusammenfassung]
Um eine effiziente Datenverarbeitung durch die CPU zu gewährleisten, müssen sich alle Werte eines
Typs auf Speicheradressen befinden, die ein Vielfaches einer bestimmten Zahl _N_ sind.

Diese Zahl _N_ bezeichnet man als _Alignment_ dieses Typs.

Mit anderen Worten: Alle Speicheradressen, an denen Werte dieses Typs gespeichert werden,
müssen durch das Alignment teilbar sein.
[ENDHINT]

Betrachten Sie das folgende "Speicherstück", wo die Zahlen in der unteren Reihe
"Speicheradressen" sind.
Hier sind 16 Bytes dargestellt.

    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬────┬────┬────┬────┬────┬────┐
    │   │   │   │   │   │   │   │   │   │   │    │    │    │    │    │    │
    ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼────┼────┼────┼────┼────┼────┤
    │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 │ 13 │ 14 │ 15 │
    └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴────┴────┴────┴────┴────┴────┘

Für die Aufgabe konzentrieren wir uns auf zwei primitiven Datentypen:

- `bool` — 1 Byte groß, Alignment 1
- `int32` — 4 Byte groß, Alignment 4

[EQ] Laut den spezifizierten Alignments, welche Speicherzellen dürfen einen `bool`-Wert
adressieren?
Einen `int32`-Wert?

Jetzt probieren Sie ein paar Anordnungen aus, um ein Bauchgefühl zu entwickeln,
wie Speicherplatz tatsächlich benutzt wird.

Belegen Sie den Speicher von links nach rechts mit den Feldern der jeweiligen Struktur:
das erste Feld kommt zuerst, dann das zweite und so weiter.

Die Antwort soll folgendermaßen aussehen: `a[0-3]b[4]c[5-12]`, wo die Zahlen in
eckigen Klammern den Start- und den Endindex beinhalten (beide inklusive).

[EQ]
```go
type A struct {
    a bool
    b int32
    c bool
    d int32
}
```
[EQ]
```go
type B struct {
    a bool
    b bool
    c int32
    d int32
}
```
[EQ]
```go
type C struct {
    a bool
    b int32
    c int32
    d bool
}
```
[EQ]
```go
type D struct {
    a int32
    b int32
    c bool
    d bool
}
```

[EQ] Was ist die minimal erforderliche Größe, um diese vier Felder (zwei `bool` und zwei `int32`)
speichern zu können?

Überprüfen Sie nun Ihre Größeneinschätzung mithilfe von der Funktion `unsafe.Sizeof()`.
Stimmt das Ergebnis mit Ihrer Einschätzung überein?

[FOLDOUT::Die Strukturen selbst besitzen auch ein Alignment!]
Wahrscheinlich haben Sie angenommen, dass die kleinstmögliche Struktur 10 Bytes groß ist.

Die Funktion `unsafe.Sizeof()` gibt jedoch für die Struktur `D` eine Größe von 12 Bytes an.

Warum?

Wie bereits erwähnt: Strukturen besitzen ebenfalls ein Alignment.
In der Regel entspricht dieses dem größten Alignment ihrer Felder — in diesem Fall 4.

Stellen Sie sich nun ein Array `[2]D` vor, in dem zwei Strukturen `D` direkt nebeneinander
im Speicher liegen.
Da `D` ein Alignment von 4 hat, darf jede Instanz nur an Adressen beginnen, die ein Vielfaches
von 4 sind: also 0, 4, 8, 12, 16, 20, ...

Wenn die erste Struktur die Speicherzellen 0 bis 9 belegt, darf die zweite erst
bei Adresse 12 beginnen.
Die Speicherzellen 10 und 11 bleiben dabei ungenutzt, gehören aber logisch zur ersten
Struktur — und werden deshalb von `unsafe.Sizeof()` mitgezählt.

Diese beiden zusätzlichen Bytes nennt man _Padding_.
[ENDFOLDOUT]

<!-- time estimate: 30 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

- `testEmptyStruct` — die Speicheradresse im abgegebenen Kommandoprotokoll muss
  nicht mit dieser in der Musterlösung übereinstimmen.
  Der Punkt ist, dass es dreimal dieselbe Adresse ist.

**Kommandoprotokoll**
[PROT::ALT:go-structs2.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier: 
[TREEREF::/Sprachen/Go/go-structs2.go]
.
[ENDINSTRUCTOR]
