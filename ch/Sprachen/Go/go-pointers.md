title: "Go-Grundlagen: Zeiger"
stage: alpha
timevalue: 3.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich habe mich mit den weiteren Konzepten von Go auseinandergesetzt und kann nun
Zeiger effektiv benutzen.
[ENDSECTION]

[SECTION::background::default]
TODO
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


### "Pass-by-value" und "Pass-by-reference"

Schauen Sie sich diesen Artikel an:
[Pass-by-value vs. Pass-by-reference](https://www.educative.io/answers/pass-by-value-vs-pass-by-reference).
Obwohl das Beispiel dort in C++ ist, sollten Sie das richtige Gefühl für das Thema bekommen.

Schauen Sie sich außerdem diesen Beitrag an:
[The Go Programming Language Report: Pass by value or Pass by reference](
https://kuree.gitbooks.io/the-go-programming-language-report/content/26/text.html).
Hier geht es um Go.

Auch wenn Go alle Werte per Wert übergibt, gibt es Datentypen, die das `pass-by-reference`-Verhalten
zeigen — solche Datentypen heißen _Referenztypen_.
[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**

TODO

**Lösungen**

TODO

Musterlösung der Programmieraufgabe siehe hier: TODO
[ENDINSTRUCTOR]
