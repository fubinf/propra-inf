title: Weitere Grundlagen von Go — Strukturen
stage: alpha
timevalue: 3
difficulty: 2
assumes: go-basics1, go-basics2
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datentypen in Go definieren.
[ENDSECTION]

[SECTION::background::default]
Je größer Ihre Projekte werden, desto mehr Struktur und Organisation braucht
Ihr Quellcode.
Go ist keine objektorientierte Programmiersprache: Im Gegensatz zu Java oder Python
gibt es keine Klassen, Objekte oder Vererbung.
Stattdessen wird in Go mit __Strukturen__ (structs) gearbeitet —
mit zusammengesetzten Datentypen.

In dieser Aufgabe handelt es sich um Strukturen, Methoden, Struktureinbettung
und das Zusammenspiel von dem pass-by-value-Verhalten, Zeigern und Strukturen.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]
Wie im Teil 1 und 2 gilt weiter:
Dokumentation zur Programmiersprache finden Sie in der
[Go Spec](https://go.dev/ref/spec)
für definitive (Referenz-)Information und im
[Go User Manual](https://go.dev/doc/),
wenn Sie eher Anleitungscharakter suchen.


### Definition

Eine Struktur (struct) ist eine Zusammensetzung von primitiven Datentypen oder
anderen Strukturen.

Strukturen bestehen aus _Feldern_, die jeweils einen Namen und einen festen Typ haben:

```go
type Person struct {
    FirstName string
    LastName  string
    Age       int
}
```

Lese- und Schreibzugriff auf die Felder einer Struktur erfolgt mithilfe von `.`:

```go
// volle Schreibweise
p := Person{FirstName: "Max", LastName: "Mustermann", Age: 25}

// kurze Schreibweise, Reihenfolge der Argumente bestimmt die Zuordnung
p := Person{"Max", "Mustermann", 25}

// Initialisierung mit Nullwerten: 
p := Person{}               // äquivalent zu Person{"", "", 0}

fmt.Println(p.FirstName)    // Max
p.FirstName = "Eric"
```

[NOTICE]
Alle Felder dieser Struktur sind großgeschrieben und deswegen öffentlich
(public/exported).
[ENDNOTICE]


### Methoden

Auch ohne Klassen gibt es **Methoden** in Go.

Methoden sind Funktionen, die einem Typ zugeordnet sind und einen bestimmten
ersten Parameter besitzen: den Empfänger (receiver).
Sie ermöglichen es, Verhalten zu Strukturen hinzuzufügen.

```go
func (p Person) Print() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der Empfänger: `p` ist der Name, über welchen die Methode
auf die Struktur selbst zugreifen kann.

[ER] Definieren Sie eine Struktur `Circle`, die ein Feld `radius float64` besitzt.

[ER] Implementieren Sie zwei Methoden auf `Circle`:

- `Circumference() float64` — Kreisumfang berechnen;
- `Area() float64` — Fläche berechnen;
- benutzen Sie `math.Pi` für Kreiszahl Pi.

[ER] Fügen Sie die Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-basics3-control-snippet-methods.go]
```

### Struktureinbettung (struct embedding)

Lesen Sie diesen
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/)
.

[ER] Definieren Sie eine Struktur `Employee`.
Diese soll alle Felder und Methoden einer `Person` übernehmen und ein neues
Feld definieren: `Position string`.

[ER] Implementieren Sie eine neue Methode `Print` auf `Person`, die den
vollständigen Namen und das Alter auf die Kommandozeile ausgibt.

[ER] Fügen Sie die Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-basics3-control-snippet-structs.go]
```

[NOTICE]
Da `Person` in `Employee` eingebettet wurde, können Sie auf alle Felder und
Methoden von `Person` explizit über `e.Person.` zugreifen.
[ENDNOTICE]

[EQ] Stellen Sie sich vor, dass es eine neue Methode `Print` auf `Employee`
definiert wurde.
Wie ändert sich die Ausgabe von der Testfunktion?

[HINT::Verdeckung (Shadowing)]
Lesen Sie den Abschnitt "Shadowing of embedded fields" in dem
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/)
.

In dem Fall verhalten sich Methoden sehr ähnlich wie Felder.
[ENDHINT]


### Anonyme Strukturen

Lesen Sie die folgende
[Erklärung, was anonyme Strukturen sind](https://blog.boot.dev/golang/anonymous-structs-golang/)
.

[EQ] Welche Anwendungen von anonymen Strukturen erwähnt der Autor?


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

Quellen für Nachlesen (könnte auch dann von Interesse sein, wenn Sie noch
relativ frisch im Go-Universum sind):

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


### "Pass-by-value" und "Pass-by-reference"

In [PARTREF::go-basics2] haben Sie bereits gelernt, dass Funktionsargumente
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

[ER] Implementieren Sie eine Methode `Promote` auf `Employee`, die ein Argument
`newPosition string` erwartet.
Sie soll die Struktur modifizieren und das Feld `Position` auf den neuen Wert setzen.

[ER] Fügen Sie die Testfunktion in Ihre Datei ein:

```go
[INCLUDE::include/go-basics3-control-snippet-mutation.go]
```

[ER] Stellen Sie sicher, dass Ihre `main`-Funktion genauso aussieht:

```go
func main() {
    testMethods()
    testStructs()
    testEmptyStruct()
    testMutation()
}
```

[EC] Führen Sie nun das Programm mittels `go run` aus.

[FOLDOUT::Glückwunsch!]
Wenn Sie es zum Ende des dritten Teils von `go-basics` geschafft haben,
können Sie sich sicher sein, dass Sie ein fundiertes Verständnis für die
wichtigsten Konzepte der Programmiersprache Go entwickelt haben.

Lassen Sie sich nicht vom Begriff `basics` täuschen — Übergabe per Wert/Zeiger,
Struktureinbettung, Methoden und Slices sind keineswegs triviale Themen.
`basics` bedeutet nur, dass dieses Wissen in den weiteren Aufgaben vorausgesetzt wird.

Im `basics`-Kapitel fehlt nur noch der letzte Schliff — [PARTREF::go-interfaces].
Interfaces sind ein weiteres Konzept, das in Go anders funktioniert als in
beispielsweise Java.
Also: Viel Erfolg!
[ENDFOLDOUT]

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
[PROT::ALT:go-basics3.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go0/go-basics3.go]
[ENDINSTRUCTOR]
