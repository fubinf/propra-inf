title: "Grundlagen von Go: Zeiger"
stage: beta
timevalue: 0.5
difficulty: 2
assumes: go-functions
---

[SECTION::goal::idea,experience]
Ich verstehe, was Zeiger in Go sind und kann sie effektiv benutzen.
[ENDSECTION]

[SECTION::background::default]
Zeiger sind ein grundlegendes Konzept in der Programmierung, das es ermöglicht, per Speicheradresse
auf Daten zuzugreifen.
Sie sind nützlich, um effizient mit großen Datenstrukturen zu arbeiten oder
Werte durch Referenz anstatt durch Kopie zu übergeben.

Wer Zeiger versteht, schreibt nicht nur besseren Go-Code, sondern versteht auch besser, 
wie Programme "unter der Haube" funktionieren.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist ein Zeiger?

Ein Zeiger ist **ein Ausdruck, der die Speicheradresse eines Objekts repräsentiert.**

Ein Zeiger wird mithilfe des `&`-Operators erstellt.
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` heißt also "Adresse von `x`"
und liefert einen Zeiger, der auf `x` zeigt.

Die Umkehroperation heißt _Dereferenzierung_: 
aus dem Zeiger wird der "Wert an der Adresse" ermittelt.
Dies geschieht mithilfe des Operators `*`, der sowohl zum Deklarieren eines Zeigertyps als auch
zur Dereferenzierung verwendet wird.

Eine Variable des Typs `*T` deklariert einen Zeiger auf einen Wert vom Typ `T`.

Beispiel:

```go
content := 10               // int
var box *int
box = &content              // *int

*box = 42                   // die Box "öffnen" und den Inhalt ersetzen
fmt.Println(content)        // 42
```

In diesem Beispiel zeigt `box` auf die Adresse von `content`.
Durch Dereferenzierung kann der Wert an dieser Adresse gelesen oder geändert werden.

Schauen Sie sich das
[Thema 'Zeiger' in "A Tour of Go"](https://go.dev/tour/moretypes/1)
an und vollziehen Sie das Beispielprogramm nach (selber Änderungen machen!).

[NOTICE]
Der Nullwert aller Zeiger ist `nil`.
[ENDNOTICE]

[ER] Schreiben Sie eine Funktion `inc`, die einen Zeiger `*int` übergeben bekommt und
die Zahl um eins inkrementiert.

[EQ] Was passiert, wenn die Funktion `nil` als Parameter bekommt?

<!-- time estimate: 10 min -->


### Mehr Beispiele

[EQ] Beschreiben Sie mit eigenen Worten, warum `a` im folgenden Beispiel nicht verändert wird,
`b` aber sehr wohl.

```go
func change(x int) {
	x = 42
}

func changePointer(x *int) {
    *x = 42
}

func main() {
	a := 0
	b := 0
	change(a)
    changePointer(&b)
	fmt.Println(a)
	fmt.Println(b)
}
```

[EQ] Was wird im folgenden Beispiel auf die Kommandozeile ausgegeben?
Warum?

```go
func setToNil(p *int) {
    p = nil
}

func main() {
    x := 5
    xptr := &x
    setToNil(xptr)
    fmt.Println(xptr)
}
```

<!-- time estimate: 15 min -->
<!-- TODO_2_Brandes: add a teaser about unsafe when task 'go-unsafe' is ready --> 
[ENDSECTION]

[SECTION::submission::information,snippet]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Lösungen**

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
