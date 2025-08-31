title: Weitere Grundlagen von Go — Strukturen (Teil 2)
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datentypen in Go definieren.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-structs1] haben sie bereits Strukturen kennengelernt.

In dieser Aufgabe handelt es sich um anonyme Strukturen, die leere Struktur und 
das Zusammenspiel von dem pass-by-value-Verhalten, Zeigern und Strukturen.
[ENDSECTION]


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

[ER] Implementieren Sie eine Methode `Promote` auf `Employee`, die ein Argument
`newPosition string` erwartet.
Sie soll die Struktur modifizieren und das Feld `Position` auf den neuen Wert setzen.

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

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-structs2.go]
[ENDINSTRUCTOR]
