title: "Grundlagen von Go: Strukturen (Teil 2)"
stage: beta
timevalue: 1.25
difficulty: 2
assumes: go-pointers, go-structs1
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datentypen in Go definieren.
[ENDSECTION]


[SECTION::background::default]
In [PARTREF::go-structs1] haben Sie bereits Strukturen kennengelernt.

In dieser Aufgabe geht es um anonyme Strukturen, leere Strukturen und 
die Steuerung des Speicherlayouts.
[ENDSECTION]


[TOC]


[SECTION::instructions::detailed]

### Anonyme Strukturen

Lesen Sie den Artikel
[What Are Golang's Anonymous Structs?](https://blog.boot.dev/golang/anonymous-structs-golang/),
um zu erfahren, was anonyme Strukturen sind.

[EQ] Welche Anwendungen von anonymen Strukturen erwähnt der Autor?

[EQ] Wie würden Sie einen Slice mit drei anonymen Strukturen instanziieren, die nur
die Felder `price`, `language` und `author` besitzen?
Geben Sie den Codeabschnitt in Ihrer Markdown-Datei ab.

(Die konkreten Werte für die drei Felder dürfen Sie sich beliebig ausdenken.)

<!-- time estimate: 15 min -->


### Leere Strukturen

Eine leere Struktur ist ein Typ ohne Felder und mit Größe 0 Byte.

Dieses Konstrukt wird in den Situationen benutzt, wo Ab- oder Anwesenheit
eines Wertes wichtiger ist als der Wert selbst.

```go
type emptyStruct struct{}
es := emptyStruct{}

// anonyme Schreibweise
es := struct{}{}
```

[FOLDOUT::0 Bytes groß? Wie?]
Der Trick ist, dass alle Instanzen aller leeren Strukturen sich eine vom
Compiler festgelegte Speicheradresse teilen: `zerobase`.

Der Compiler erkennt, dass so eine Struktur keinen Speicherplatz braucht und spart sich das Allokieren.

Falls Sie sich mehr an diesen etwas seltsamen Gedanken gewöhnen möchten:

- [Dave Cheney: The empty struct](https://dave.cheney.net/2014/03/25/the-empty-struct)
- [Decrypt Go: empty struct](https://dev.to/huizhou92/decrypt-go-empty-struct-5i4)
[ENDFOLDOUT]

[ER] Implementieren Sie eine Funktion namens `testEmptyStruct`, welche 3 Instanzen
der obigen leeren Struktur erzeugt und deren Adressen auf die Kommandozeile ausgibt.

[EQ] Was fällt Ihnen während der Ausführung auf?

[ER] Stellen Sie sicher, dass Ihre `main`-Funktion genau so aussieht:

```go
[SNIPPET::ITREE:go-structs2.go::main]
```

[EC] Führen Sie nun das Programm mittels `go run` aus.

[HINT::Ich weiß nicht, wie ich die Adresse einer Variable ausgeben kann]
Siehe [PARTREF::go-basics] über `fmt.printf`-Formatangaben.

[HINT::Ich weiß nicht, wie ich die Adresse einer Variable ermitteln kann]
Siehe [PARTREF::go-pointers] über den Operator `&`.

`&variable` gibt die Adresse der Variable zurück.
[ENDHINT]
[ENDHINT]

<!-- time estimate: 10 min -->


### "Pass-by-value" und "Pass-by-reference"

In [PARTREF::go-pointers] haben Sie bereits gelernt, dass Funktionsargumente
beim Übergeben immer kopiert werden.

[EQ] Was wäre Ihrer Meinung nach ein guter Grund, eine Struktur per Zeiger statt
per Wert zu übergeben?
Und was wäre ein weniger überzeugender Grund?

[EQ] Wie würden Sie vorgehen, wenn die Struktur sehr groß ist, aber nicht verändert werden darf?

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

<!-- time estimate: 10 min -->


### Speicherlayout (Alignment und Padding)

Es gibt Situationen, in denen die Reihenfolge der Felder innerhalb einer Struktur
tatsächlich einen Unterschied macht.

Ein wichtiger Begriff, den Sie an dieser Stelle kennenlernen sollten, ist das sogenannte
_Alignment_.

Lesen Sie den
[Abschnitt "Type Alignment Guarantees in Go" im Artikel "go101: Memory Layouts"](https://go101.org/article/memory-layout.html),
um ein besseres Verständnis dafür zu bekommen, was genau mit Alignment gemeint ist.

[HINT::Ich finde den Abschnitt zu technisch]
Um eine effiziente Datenverarbeitung durch die CPU zu gewährleisten, müssen alle Werte eines
Typs auf Speicheradressen liegen, die ein Vielfaches einer bestimmten Zahl _N_ sind.

Diese Zahl _N_ bezeichnet man als das _Alignment_ des jeweiligen Typs.

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

[EQ] Laut den spezifizierten Alignments, welche dargestellten Speicherzellen dürfen einen `bool`-Wert
adressieren?
Welche einen `int32`-Wert?

Jetzt probieren Sie ein paar Anordnungen aus, um ein Bauchgefühl zu entwickeln,
wie Speicherplatz tatsächlich benutzt wird.

Belegen Sie den Speicher von links nach rechts mit den Feldern der jeweiligen Struktur:
das erste Feld kommt zuerst, dann das zweite und so weiter.

Die Antwort soll folgendermaßen aussehen: `a[0-3]b[4]c[5-12]`, wo die Zahlen in
eckigen Klammern den Start- und den Endindex beinhalten (beide inklusive).
Unbenutzte Bytes werden nicht erwähnt.

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

[EQ] Was ist die minimal erforderliche Größe, um zwei `bool`- und zwei `int32`-Felder
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

**Kommandoprotokoll**
[PROT::ALT:go-structs2.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier:
[TREEREF::/Sprachen/Go/go-structs2.go].
[ENDINSTRUCTOR]
