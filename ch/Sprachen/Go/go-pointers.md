title: "Go-Grundlagen: Zeiger"
stage: alpha
timevalue: 1
difficulty: 2
explains: Slice (Golang)
assumes: go-basics, go-functions
---

[SECTION::goal::idea,experience]
Ich habe mich mit den weiteren Konzepten von Go auseinandergesetzt und kann nun
Zeiger effektiv benutzen.
[ENDSECTION]

[SECTION::background::default]
Zeiger in Go ermöglichen es, direkt mit Speicher zu arbeiten — effizienter und flexibler. 
Mithilfe von Zeigern lassen sich Werte über Funktionen hinweg ändern, Daten sparen 
und komplexe Strukturen wie Listen oder Bäume bauen.

Wer Zeiger versteht, schreibt nicht nur besseren Go-Code, sondern versteht auch besser, 
wie Programme "unter der Haube" funktionieren.
[ENDSECTION]

[SECTION::instructions::detailed]


### Zeiger (pointers)

Zeiger sind ein grundlegendes Konzept in der Programmierung, das es ermöglicht, per Speicheradresse
auf Daten zuzugreifen.
Sie sind nützlich, um effizient mit großen Datenstrukturen zu arbeiten oder
Werte durch Referenz anstatt durch Kopie zu übergeben.

Zeiger in Go ähneln denjenigen in C oder C++ mit einem wichtigen Unterschied — sie sind sicherer zu
benutzen.
Sie unterstützen keine
[Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm)
und gehören immer zu einem konkreten Typ
(`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).

Der Nullwert aller Zeiger ist `nil`.
Ein Zeiger wird mithilfe des `&`-Operators erstellt.
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` heißt also "Adresse von `x`"
und liefert einen Zeiger, der auf `x` zeigt.

Die Umkehroperation heißt Dereferenzierung — ein Zeiger wird in den "Wert an der Adresse von `x`"
umgewandelt.
Dies geschieht mithilfe des Operators `*`, der sowohl zum Deklarieren eines Zeigertyps als auch
zur Dereferenzierung verwendet wird.

Beispiel:

```go
content := 10               // int
box := &content             // *int

*box = 42                   // die Box "öffnen" und den Inhalt ersetzen
fmt.Println(content)        // 42
```

In diesem Beispiel zeigt `box` auf die Adresse von `content`.
Durch Dereferenzierung kann der Wert an dieser Adresse gelesen oder geändert werden.

[ER] Schauen Sie sich 
[Zeiger auf "A Tour of Go"](https://go.dev/tour/moretypes/1)
an.

[EQ] Schreiben Sie eine Funktion `inc`, die einen Zeiger `*int` übergeben bekommt und
die Zahl um eins inkrementiert. 
Geben Sie den Code in Ihrer Markdown-Datei.

[EQ] Was passiert, wenn die Funktion `nil` als Parameter bekommt?

<!-- time estimate: 5 min -->


### "Pass-by-value" und "Pass-by-reference"

Schauen Sie sich diesen Artikel an:
[Pass-by-value vs. Pass-by-reference](https://www.educative.io/answers/pass-by-value-vs-pass-by-reference).
Obwohl das Beispiel dort in C++ ist, sollten Sie das richtige Gefühl für das Thema bekommen.

Betrachten Sie diese zwei Codeabschnitte:
```go
func change(x int) {
	x = 42
}

func main() {
	a := 0
	change(a)
	fmt.Println(a) // Gibt 42 aus — a wurde NICHT verändert
}
```

```go
func changePointer(x *int) {
    *x = 42
}

func main() {
    a := 0
    changePointer(&a)
    fmt.Println(a) // Gibt 42 aus — a wurde verändert
    }
```

[EQ] Beschreiben Sie mit eigenen Worten, warum `a` im ersten Beispiel nicht verändert wurde, 
im zweiten Beispiel aber schon.

[EQ] Warum wird Go als "pass-by-value"-Sprache betrachtet, auch wenn Zeiger als Funktionsparameter 
übergeben werden?

[EQ] Was wird im folgenden Beispiel auf die Kommandozeile ausgegeben?
Warum?

```go
func setToNil(p *int) {
    p = nil
}

func main() {
    x := 5
    setToNil(&x)
    fmt.Println(x)
}
```

<!-- time estimate: 20 min -->

### Referenztypen

Mit _Referenztypen_ sind in der Regel die Typen gemeint, die sich wie ein Zeiger (Pointer)
verhalten.
Das bedeutet unter anderem:

- der Nullwert ist `nil`
- sie enthalten intern Zeiger auf Daten
- sie zeigen "pass-by-reference"-Verhalten

Zu den Referenztypen gehören unter anderem Maps, Slices und Zeiger.

[EQ] Welche Beispiele für Referenztypen aus Python fallen Ihnen ein?


### Werttypen

_Werttypen_ sind anders: Sie stellen wirklich die Werte dar, sie sind **die Daten selbst**.
Primitive Datentypen (Zahlen, boolesche Werte und Zeichenketten) sind Werttypen.

Alle Werttypen teilen sich folgende Eigenschaften:

- der Nullwert ist nicht `nil`
- sie zeigen "pass-by-value"-Verhalten: beim Zuweisen oder Übergeben als Parameter wird eine Kopie
  erstellt
- Vergleichbarkeit: zwei Variablen von einem Werttyp dürfen mittels `==` sinnvoll verglichen werden

[EQ] Welche Beispiele für Werttypen aus Python fallen Ihnen ein?

[EQ] Welche Nachteile oder Programmierfehler können Sie sich beim Benutzen von
Referenztypen vorstellen?

Damit sind Sie nun gut vorbereitet für die nächsten Themen:

- [PARTREF::go-arrays-and-slices]
- [PARTREF::go-maps]
[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

**Lösungen**

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
