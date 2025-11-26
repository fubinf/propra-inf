title: "Grundlagen von Go: Funktionen"
stage: beta
timevalue: 1.5
difficulty: 2
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich habe mich mit weiteren Konzepten von Go auseinandergesetzt und kann nun 
Funktionen und Prozeduren definieren.
[ENDSECTION]


[SECTION::background::default]
Ein essenzieller Baustein jeder modernen Programmiersprache sind Unterprogramme —
ausgelagerte Stückchen der Funktionalität, die Wiederverwendbarkeit und Lesbarkeit
des Codes erhöhen.

In Go heißen Unterprogramme "Funktionen" und sind [TERMREF2::first-class citizen::-s].
Sie haben einige Go-spezifische Besonderheiten, die Sie in dieser Aufgabe kennenlernen werden.
[ENDSECTION]


[SECTION::instructions::detailed]

### Allgemein

Eine Funktionsdefinition in Go besteht aus folgenden Teilen:

* `func` Schlüsselwort;
* optional(!) ein Funktionsname;
* Runde Klammern für die Parameterliste.
  Die Parameter werden darin nacheinander als Paare `name type` aufgelistet;
* Signatur der Rückgabe:
    * leer, wenn die Funktion nichts zurückgibt (Prozedur);
    * `T`, wenn die Funktion einen Wert von Typ `T` zurückgibt;
    * ein Tupel `(T1, T2, ..., Tn)`, falls die Funktion mehrere Werte auf einmal zurückgibt;
    * oder ein benanntes Tupel `(t1 T1, t2 T2, ..., tn Tn)`, falls die Rückgabewerte direkt
      in der Funktionssignatur deklariert werden sollen (Erklärung folgt);
* Funktionsrumpf in geschweiften Klammern.

Eine Funktion, die Sie bereits kennen, ist die `main`-Funktion:

```go
func main() {
    ...
}
```

Die folgenden Beispiele erklären die oben unterschiedenen Fälle:

```go
// Rückgabetyp ist string
func convertIntToString(i int) string {
    return fmt.Sprintf("%v", i)
}

// zwei Rückgabewerte (hier ein int und ein error) müssen geklammert werden
func convertStringToInt(s string) (int, error) {
    return strconv.ParseInt(s, 10, 64)
}

// mehrere Parameter
func constructFullName(firstName string, lastName string) string {
    return fmt.Sprintf("%v %v", firstName, lastName)
}

// mehrere Parameter mit gleichem Typ (verkürzte Notation)
func constructFullName(firstName, lastName string) string {
    return fmt.Sprintf("%v %v", firstName, lastName)
}

// anonyme Funktion ("lambda"-Funktion), 
// die direkt in ihrem Aufruf definiert ist und mit zwei Zahlen aufgerufen wird
func (x int, y int) {
    return x * y
}(4, 5)

// benannte Tupel als Resultat
func namedReturnValues() (answer int, label string) {
    answer = 42
    label = "hello world"
    // hier würde ein leeres `return` auch automatisch alle Werte zurückgeben,
    // die in der Funktionssignatur als Rückgabewerte deklariert wurden
    return answer, label 
}
```


### Benannte Rückgabewerte und variadische Funktionen

Nutzen Sie folgende Quellen, um die nachfolgenden Fragen zu beantworten:

- [Benannte Rückgabewerte](https://go.dev/tour/basics/7)
- [Variadische Funktionen](https://gobyexample.com/variadic-functions)

[EQ] Mit welchen Werten werden benannte Rückgabewerte initialisiert?

[EQ] Wann ist es Ihrer Meinung nach sinnvoll, benannte Rückgabewerte zu benutzen?
(Dies ist keine technische Frage, sondern eine Stilfrage.)

[EQ] Was ist der Unterschied zwischen einer variadischen Funktion und einer Funktion,
die einen [TERMREF::Slice (Golang)] von Parametern bekommt?

[EQ] Welche Vor- oder Nachteile einer Schreibweise gegenüber der anderen fallen Ihnen
ein?

<!-- time estimate: 20 min -->


### Funktionen höherer Ordnung

Eine Funktion kann eine andere Funktion als Parameter erhalten,
wodurch sie zu einer Funktion höherer Ordnung wird:

```go
func apply(
    arg int,
    operation func (int) int,
) int {
    return operation(arg)
}
```

Diese Funktion nimmt zwei Parameter an:
ein `int` und eine Funktion, die ein `int` übergeben bekommt und ein `int` zurückgibt.
`operation` ist der Name der Funktion, und `func(int) int` ist ihr Typ,
zusammen bildet das die Signatur.

Der Aufruf könnte so aussehen:

```go
func square(i int) int {
    return i * i
}

func main() {
    ...
    squared := apply(4, square)
}
```

Funktionen höherer Ordnung sind nützlich für die Erstellung flexibler und wiederverwendbarer
Codebausteine.

[ER] Implementieren Sie eine Funktion `divide(a, b float64) (result float64, err error)`:
diese muss die erste Zahl durch die zweite dividieren.
Bei Erfolg gibt sie ein Tupel `(result, nil)` zurück; ansonsten
`(0.0, fmt.Errorf("division by zero"))`.
Benutzen Sie hier benannte Rückgabewerte.

[ER] Implementieren Sie `reduce(initialValue int, operation func(int, int) int, xs ...int) int` —
eine Funktion, die eine Funktion `operation` und eine beliebige Anzahl von Ganzzahlen
als Parameter bekommt.
Sie wendet sukzessive `operation` auf die Ganzzahlen an:
Der erste Parameter von `operation` ist eine Akku-Variable
(anfangs `initialValue`, danach immer das vorherige Resultat),
der zweite der Reihe nach jedes Element der Liste `xs`.
Mit `reduce(0, func(acc, arg int) int { return acc + arg }, 1, 2, 3, 4)` kann beispielsweise
die Summe der Ganzzahlen berechnet werden.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei und rufen Sie sie aus der 
`main`-Funktion auf:

```go
[INCLUDE::include/go-functions-control-snippet.go]
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 30 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
`testDivideAndReduce`:
diese beiden Funktionen sollten unverändert in dem abgegebenen Quellcode präsent sein,
damit das Kommandoprotokoll nicht verfälscht wird.

<!-- @PROGRAM_TEST -->


**Kommandoprotokoll**
[PROT::ALT:go-functions.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-functions.go].
[ENDINSTRUCTOR]
