title: "Grundlagen von Go: Zeiger"
stage: alpha
timevalue: 2
difficulty: 2
assumes: go-basics, go-functions, go-structs1
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

In C oder C++ sind Zeiger ziemlich low-level und geben dem Programmierer viel mehr Macht:
Ein Zeiger ist bloß eine Zahl — eine Speicheradresse.
Was man damit anfängt, ist einem überlassen, was ungeheure Möglichkeiten für Defekte eröffnet,
die sehr subtil sein können.

Im Gegensatz zu den "gefährlichen" Zeigern in C sind Go-Zeiger restriktiver.
Sie unterstützen keine
[Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm)
und gehören immer zu einem konkreten Typ
(`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).
In C sind Zeiger ebenfalls typisiert, allerdings kann man einen Zeiger in jeden anderen Typ
umdeuten und das wird auch tatsächlich häufig genutzt.


### Wie funktionieren Zeiger in Go?

Der Nullwert aller Zeiger ist `nil`.
Ein Zeiger wird mithilfe des `&`-Operators erstellt.
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` heißt also "Adresse von `x`"
und liefert einen Zeiger, der auf `x` zeigt.

Die Umkehroperation heißt _Dereferenzierung_: 
aus dem Zeiger wird der "Wert an der Adresse" ermittelt.
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

Schauen Sie sich das
[Thema 'Zeiger' in "A Tour of Go"](https://go.dev/tour/moretypes/1)
an und vollziehen Sie das Beispielprogramm nach (selber Änderungen machen!).

[ER] Schreiben Sie eine Funktion `inc`, die einen Zeiger `*int` übergeben bekommt und
die Zahl um eins inkrementiert. 
Geben Sie den Code in Ihrer Markdown-Datei ab.

[EQ] Was passiert, wenn die Funktion `nil` als Parameter bekommt?

<!-- time estimate: 10 min -->


### "Pass-by-value" und "Pass-by-reference"

Schauen Sie sich diesen Artikel an:
[Pass-by-value vs. Pass-by-reference](https://www.educative.io/answers/pass-by-value-vs-pass-by-reference).
Obwohl das Beispiel dort in C++ ist, sollten Sie damit ein Verständnis für das Thema bekommen.

Betrachten Sie diese zwei Codeabschnitte:
```go
func change(x int) {
	x = 42
}

func main() {
	a := 0
	change(a)
	fmt.Println(a) // Gibt 0 aus — a wurde NICHT verändert
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

[EQ] Beschreiben Sie mit eigenen Worten, warum `a` im ersten Beispiel nicht verändert 
wurde, im zweiten Beispiel aber schon.

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

<!-- time estimate: 5 min -->


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

<!-- time estimate: 10 min -->


### 'unsafe'

Am Anfang der Aufgabe haben Sie gelernt, dass Zeiger in Go keine Zeigerarithmetik 
unterstützen.
Das ist nicht 100% korrekt, da es das Paket `unsafe` gibt, welches solche "gefährlichen"
low-level Operationen ermöglicht, wie beispielsweise _Zeigerarithmetik_.

In diesem Teil lernen Sie noch zwei Datentypen kennen und spielen selbst mit
den low-level Zeigern.

Der erste Typ ist `uintptr` — das ist ein Integer-Typ, der groß genug ist, um 
Bit-Muster aller Zeiger darstellen zu können.
Prinzipiell ist es nur eine ganze Zahl — kann also addiert und subtrahiert werden.

Der zweite Typ ist `unsafe.Pointer` — er konvertiert einen typisierten Go-Zeiger 
zu einem beliebigen/generischen.
`unsafe.Pointer` ist eine Art Brücke zwischen gewöhnlichen Go-Zeigern 
und `uintptr`-Zahlen mit Speicheradressen.

Das Lesen von 
[Dokumentation von `unsafe.Pointer`](https://pkg.go.dev/unsafe#Pointer)
ist für diese Aufgabe nicht notwendig, aber sehr empfohlen.

Lesen Sie nun folgende Abschnitte aus dem Artikel
[Exploring ‘unsafe’ Features in Go 1.20: A Hands-On Demo](https://medium.com/@bradford_hamilton/exploring-unsafe-features-in-go-1-20-a-hands-on-demo-7149ba82e6e1):

- **Background: The Role of ‘Unsafe’ in Go** (Kommentar, warum das Paket nur sehr 
  vorsichtig zu benutzen ist)
- **Some Notes on unsafe.Pointer and uintptr** (Konvertierung zwischen `*T`, `uintptr` 
  und `unsafe.Pointer`)

[ER] Definieren Sie eine Struktur `Vector` mit Feldern `x byte` und `y byte`.

[ER] Schreiben Sie eine Funktion `getAddressDifference()`, welche:

- eine Variable `v Vector` deklariert;
- die Speicheradressen von `v.x` und `v.y` zu `uintptr` konvertiert;
- Diese als `addrX` und `addrY` übereinander auf die Kommandozeile ausgibt (benutzen Sie das 
  Format `"addrX: %x\n"` beziehungsweise `"addrY: %x\n"`);
- Die Differenz `addrY - addrX` ebenfalls auf die Kommandozeile ausgibt.

[EQ] Basierend auf der Differenz der Adressen, was können Sie über die Position 
der Variablen im Speicher sagen?

[ER] Schreiben Sie eine Funktion `manipulate()`, welche:

- eine Variable `v Vector` deklariert;
- anhand der Adresse von `v.x` die Adresse von `v.y` bestimmt (muss ja gleich die
  nächste Speicherzelle sein? — entweder `+ 1` oder `+ unsafe.Sizeof(v.x)`), 
  diese zu einem Go-Zeiger konvertiert (`*byte`) und den Wert von `v.y` auf 42 setzt;
- anschließend `v` auf die Kommandozeile ausgibt.

[EC] Rufen Sie die Funktionen `getAddressDifference()` und `manipulate()` aus der
`main`-Funktion auf und führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-pointers.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-pointers.go].
[ENDINSTRUCTOR]
