title: Weitere Grundlagen von Go
stage: alpha
timevalue: 3.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics1
---

[SECTION::goal::idea,experience]
Ich habe mich mit den weiteren Konzepten von Go auseinandergesetzt und kann nun:

- Funktionen definieren;
- Zeiger und Referenztypen effektiv benutzen;
[ENDSECTION]

[SECTION::background::default]
In dieser Aufgabe lernen Sie weitere wichtige Konstrukte in der Programmiersprache Go. 
Zusammen mit [PARTREF::go-basics1] ergibt dies eine solide Grundlage, 
mithilfe derer Sie komplexere Programme implementieren können.
Insbesondere geht es in dieser Aufgabe um Funktionen, Zeiger und die Unterscheidung zwischen Wert- und Referenztypen.
[ENDSECTION]

[SECTION::instructions::detailed]
Wie im Teil 1 gilt weiter:
Dokumentation zur Programmiersprache finden Sie in der
[Go Spec](https://go.dev/ref/spec)
für definitive (Referenz-)Information und im
[Go User Manual](https://go.dev/doc/),
wenn Sie eher Anleitungscharakter suchen.


### Funktionen

Eine Funktionsdefinition in Go besteht aus folgenden Teilen:

* `func` Schlüsselwort;
* Funktionsname (optional!);
* Runde Klammern für die Parameterliste. 
  Die Parameter werden nacheinander als Paare `name type` aufgelistet;
* Signatur der Rückgabe:
    * leer, wenn die Funktion nichts zurückgibt (Prozedur);
    * `T`, wenn die Funktion einen Wert von Typ `T` zurückgibt;
    * ein Tupel `(T1, T2, ..., Tn)`, falls die Funktion mehrere Werte auf einmal zurückgibt;
    * oder ein benanntes Tupel `(t1 T1, t2 T2, ..., tn Tn)`, falls die Rückgabewerte direkt 
      in der Funktionssignatur deklariert werden sollen;
* Funktionsrumpf in geschweiften Klammern.

Eine Funktion, die Sie bereits kennen, ist die `main`-Funktion:

```go
func main() {
    ...
}
```

Weitere Beispiele:

```go
// Rückgabetyp ist string
func convertIntToString(i int) string {
    return fmt.Sprintf("%v", i)
}

// zwei Rückgabewerte - ein int und ein error, müssen geklammert werden
func convertStringToInt(s string) (int, error) {
    return strconv.ParseInt(s, 10, 64)
}

// mehrere Parameter
func constructFullName(firstName string, lastName string) string {
    return fmt.Sprintf("%v %v", firstName, lastName)
}

// mehrere Parameter mit gleichem Typ (verkürzt)
func constructFullName(firstName, lastName string) string {
    return fmt.Sprintf("%v %v", firstName, lastName)
}

// anonyme Funktion ("lambda" Funktion), 
// die beim Aufruf definiert ist und mit zwei Zahlen aufgerufen wird
func(x int, y int) {
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

Informieren Sie sich nun selbstständig über einige weitere funktionsbezogene Konzepte:

- [Benannte Rückgabewerte](https://go.dev/tour/basics/7)
- [Variadische Funktionen](https://gobyexample.com/variadic-functions)

[EQ] Mit welchen Werten werden benannte Rückgabewerte initialisiert?

[EQ] Wann ist es Ihrer Meinung nach sinnvoll, benannte Rückgabewerte zu benutzen?

[EQ] Was ist der Unterschied zwischen einer variadischen Funktion und einer Funktion, die eine Sammlung (einen [TERMREF::Slice (Golang)]) von Parametern bekommt?

[EQ] Welche Vor- beziehungsweise Nachteile einer Schreibweise gegenüber der anderen fallen Ihnen ein?


### Funktionen höherer Ordnung

Eine Funktion kann eine andere Funktion als Parameter erhalten, 
wodurch sie zu einer Funktion höherer Ordnung wird:

```go
func apply(
    arg int, 
    operation func(int) int,
) int {
    return operation(arg)
}
```

Diese Funktion nimmt zwei Parameter an: 
ein `int` und eine Funktion, die ein `int` übergeben bekommt und ein `int` zurückgibt. 
`operation` ist der Name der Funktion, und 
`func(int) int` ist ihre Signatur.

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

Funktionen höherer Ordnung sind nützlich für die Erstellung flexibler und wiederverwendbarer Codebausteine.


[ER] Implementieren Sie eine Funktion `divide(a, b float64) (result float64, err error)`:
diese muss die erste Zahl durch die zweite dividieren.
Bei Erfolg gibt sie ein Tupel `(result, nil)` zurück; ansonsten `(0.0, fmt.Errorf("division by zero"))`.
Benutzen Sie hier benannte Rückgabewerte.

[ER] Implementieren Sie `reduce(initialValue int, operation func(int, int) int, xs ...int) int` — eine Funktion, die 
eine Funktion (`operation`) und eine beliebige Anzahl von Ganzzahlen als Parameter bekommt.
Sie wendet sukzessive `operation` auf die Ganzzahlen an:
Der erste Parameter von `operation` ist eine Akku-Variable 
(anfangs `initialValue`, danach immer das vorherige Resultat), 
der zweite der Reihe nach jedes Element der Liste `xs`.
Mit `reduce(0, func(acc, arg int) int { return acc + arg }, 1, 2, 3, 4)` kann beispielsweise 
die Summe der Ganzzahlen berechnet werden.

[ER] Fügen Sie die folgende Funktion in Ihre Quellcodedatei ein und rufen Sie diese aus der `main`-Funktion auf:

```go
func testFunctions() {
    fmt.Println(divide(5, 2))
    fmt.Println(divide(5, 0))
    fmt.Println(
        reduce(
            0,
            func(acc, arg int) int { return acc + arg * arg }, 
            2, 3, 5, 7, 11, 13, 17, 19,
        ),
    )
}
```


### Zeiger (pointers)

Zeiger sind ein grundlegendes Konzept in der Programmierung, das es ermöglicht, per Speicheradresse
auf Daten zuzugreifen. 
Sie sind nützlich, um effizient mit großen Datenstrukturen zu arbeiten oder 
Werte durch Referenz anstatt durch Kopie zu übergeben.

Zeiger in Go ähneln denjenigen in C oder C++ mit einem wichtigen Unterschied — sie sind sicherer zu benutzen.
Sie unterstützen keine 
[Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm) 
und gehören immer zu einem konkreten Typ 
(`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).

Der Nullwert aller Zeiger ist `nil`.
Ein Zeiger wird mithilfe des `&`-Operators erstellt. 
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` heißt "Adresse von `x`".

Die Umkehroperation heißt Dereferenzierung — ein Zeiger wird in den "Wert an der Adresse `x`" umgewandelt.
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

Schauen Sie sich 
[diesen Artikel](https://www.educative.io/answers/pass-by-value-vs-pass-by-reference) 
an.
Auch wenn das Beispiel dort in C++ ist, sollten Sie das richtige Gefühl für das Thema bekommen.

Schauen Sie sich außerdem
[dieses Beispiel](https://kuree.gitbooks.io/the-go-programming-language-report/content/26/text.html) 
an. 
Hier geht es um Go.

Es gibt jedoch Datentypen, die sich wie Zeiger verhalten — solche Datentypen heißen _Referenztypen_. 


### Referenz- und Werttypen

Mit _Referenztypen_ sind in der Regel die Typen gemeint, die sich wie ein Zeiger (Pointer) verhalten.
Das bedeutet unter anderem:

- der Nullwert ist `nil`
- sie enthalten intern Zeiger auf Daten
- sie bewirken "pass-by-reference"-Verhalten

_Werttypen_ sind anders: Sie stellen wirklich die Werte dar, sie sind **die Daten selbst**.
Primitive Datentypen (Zahlen, boolesche Werte und Zeichenketten) sind Werttypen.

Alle Werttypen teilen sich folgende Eigenschaften:

- der Nullwert ist nicht `nil`
- sie bewirken "pass-by-value"-Verhalten: beim Zuweisen oder Übergeben als Parameter wird eine Kopie erstellt
- Vergleichbarkeit: zwei Variablen von einem Werttyp dürfen mittels `==` sinnvoll verglichen werden

Nun betrachten wir Arrays, Slices und Maps detaillierter aus der Perspektive von Wert- und Referenztypen.


### Array

Ein Array ist ein Werttyp, der eine Sammlung von Einträgen darstellt, 
wo alle Einträge zum gleichen Typ gehören und die Größe (Anzahl von Einträgen) fest ist.

```go
var arr [5]int                      // arr == [0 0 0 0 0]
anotherArr := arr                   // eine Kopie wurde erstellt
anoterArr[0] = 42
fmt.Println(arr, anotherArr)        // [0 0 0 0 0] [42 0 0 0 0]
```

Reine Arrays werden in Go relativ selten verwendet, daher konzentrieren wir uns auf Slices.


### Slice

Slices bauen immer auf Arrays auf. 
Ein [TERMREF::Slice (Golang)] ist eine "View" bzw. eine Sicht in das zugrundeliegende Array
und ist ein Referenztyp.

Die Laufzeitdarstellung eines Slice (definiert in `go/src/runtime/slice.go`) 
sieht intern wie folgt aus:

```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

* `array`: das zugrundeliegende Array beziehungsweise ein Verweis auf die Speicherstelle, wo sich das Array befindet;
* `len`: die Anzahl von Elementen in dem Slice. 
  Diese Zahl ist immer zwischen 0 und der Größe des zugrundeliegenden Arrays und kann 
  mittels der eingebauten Funktion 
  [`len()`](https://pkg.go.dev/builtin#len)
  ermittelt werden;
* `cap`: die Anzahl von Elementen, die der Slice maximal beinhalten kann ("Capacity", Kapazität). 
  Diese Zahl wird von der eingebauten Funktion 
  [`cap()`](https://pkg.go.dev/builtin#cap)
  zurückgegeben und stellt die Anzahl von Zellen 
  bis zum Ende des zugrundeliegenden Arrays dar.

Ein oder mehrere Elemente in einen Slice einfügen: 
[append](https://pkg.go.dev/builtin#append).

Slices können entweder eigenständig erstellt werden oder als eine Sicht in ein existierendes Array:

```go
sl := make([]int, 4)            // Typ und initiale Größe eines Slice

sl := []int{0, 1, 2, 3, 4}      // direkter Slice mit Werten

arr := [5]int{0, 1, 2, 3, 4}    // existierendes Array

sl := arr[1:3]                  // der erste Index ist inklusiv, der zweite Index ist exklusiv
fmt.Println(len(sl))            // Länge: 2
fmt.Println(cap(sl))            // Kapazität: 4, denn Element 0 des Arrays ist nicht für den Slice verfügbar

fmt.Println(sl)                 // [1 2]
fmt.Println(sl[0])              // 1
fmt.Println(sl[1])              // 2
sl[0] = 8                       // das verändert das Array arr!
fmt.Println(arr)                // [0 8 2 3 4]
```

Ein weiteres Beispiel:

```go
arr := [5]int{0, 1, 2, 3, 4}

sl := arr[:]                    // kreiert einen Slice für das gesamte ursprüngliche Array (len = 5, cap = 5)
sl := arr[2:]                   // kreiert einen Slice ab Index 2 bis zum Ende des Arrays (len = 3, cap = 3)
sl := arr[:3]                   // kreiert einen Slice vom Anfang des Arrays bis zu Index 3 (exklusiv) (len = 3, cap = 5),
                                // ermöglicht also das Hinzufügen zweier weiterer Elemente
sl = append(sl, 8)              // überschreibt die "3" im ursprünglichen Array arr!
```

Wie bereits erwähnt, können Slices mithilfe der Funktion `make([]T, initialSize)` kreiert werden. 
Das zugrundeliegende Array wird dann automatisch erstellt und hat exakt die Größe von `initialSize`.

Ein solcher Slice verhält sich im Wesentlichen wie ein dynamisches Array: 
Sobald versucht wird, zum vollen Slice der Größe `initialSize` ein anderes Element hinzuzufügen, 
wird ein neues Array doppelten Größe allokiert.


### Map

Eine Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre Schlüssel ermöglicht. 

Eine Map ist ein Referenztyp und wird ebenfalls mithilfe der Funktion `make()` erstellt:

```go
m := make(map[string]int)       // "string" ist der Typ der Schlüssel, "int" ist der Typ der Werte
m["one"] = 1
fmt.Println(m)                  // map[one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist, wenn kein solcher Schlüssel existiert
fmt.Println(len(m))             // 1
```

Um zu überprüfen, ob ein Schlüssel bereits vorhanden ist, wird die folgende Schreibweise verwendet:

```go
mysteriousMap := make(map[string]int)

if value, isThere := mysteriousMap["key"]; isThere {
    // do something
} else {
    // "key" does not exist in the map and the value should not be used
}
```

Ein Schlüssel-Wert-Paar kann explizit entfernt werden:

```go
studentAges := make(map[string]int)

studentAges["Max"] = 23 

if value, isThere := studentAges["Max"]; isThere {
    delete(studentAges, "Max")
}
```

Falls es keinen solchen Schlüssel gibt, führt `delete()` keine Aktion aus.

[WARNING]
Variablen aller Referenztypen werden mit `nil` initialisiert:

```go
var s []int                     // s == nil
var m map[string]int            // m == nil
```

Das führt leicht zu Schwierigkeiten.
Es ist robuster, Slices und Maps direkt während der Deklaration mit `make()` zu initialisieren:

```go
s := make([]int, 0)
m := make(map[string]int)
```
[ENDWARNING]


### Selber programmieren

Implementieren Sie die folgenden Funktionen:

[ER] `func AddElement(slice []int, element, at int)`: 
ein Element an einem Index `at` in einen Slice einfügen;
das Element, das vorher an dieser Stelle stand, und alle nachfolgenden rücken eine Position nach rechts.

[ER] `func RemoveElement(slice []int, at int)`: 
ein Element an einem Index `at` entfernen und die Größe des Slice entsprechend anpassen.

[ER] `func AddElementIfNotThere(m map[string]int, key string, value int)`:
ein Schlüssel-Wert-Paar einfügen, falls der Schlüssel noch nicht benutzt wurde.
Ansonsten keine Aktion.

[EC] Fügen Sie die folgenden Testfunktionen Ihrem Programm bei und rufen Sie sie aus der `main`-Funktion auf:

```go
func testSlicesAndMaps() {
    fmt.Println("testing AddElement...")
    s := []int{1, 2, 3}
    for i := 0; i < len(s)+1; i++ {
        sc := make([]int, len(s))
        copy(sc, s)
        fmt.Println(AddElement(sc, 4, i))
    }

    fmt.Println("testing RemoveElement...")
    for i := 0; i < len(s)+1; i++ {
        sc := make([]int, len(s))
        copy(sc, s)
        fmt.Println(RemoveElement(sc, i))
    }

    fmt.Println("Testing AddElementIfNotThere...")

    m := make(map[string]int)
    m["hi"] = 42

    fmt.Println(AddElementIfNotThere(m, "hi", 420))
    fmt.Println(AddElementIfNotThere(m, "there", 420))
}

func testDivideAndReduce() {
    fmt.Println(divide(5, 2))
    fmt.Println(divide(5, 0))
    fmt.Println(
        reduce(
            0,
            func(acc, arg int) int { return acc + arg*arg },
            2, 3, 5, 7, 11, 13, 17, 19,
        ),
    )
}

func main() {
    testDivideAndReduce()
    testSlicesAndMaps()
}
```
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
Korrektur von `testDivideAndReduce` und `testSlicesAndMaps`:
die Funktionen sollten unverändert in dem abgegebenen Quellcode präsent sein, 
damit das Kommandoprotokoll nicht verfälscht wird.

Korrektur von `AddElement`, `RemoveElement`: 
Der Zweck ist, dass Studierende Slices erstellen und modifizieren können.

Korrektur von `AddElementIfNotThere`:
Der Zweck ist, dass Studierende überprüfen können, ob der Wert da ist.
Hier ist wichtig zu verstehen, wie man einen Nullwert von einem tatsächlich vorhandenen 
Wert unterscheiden kann — nämlich mit der Schreibweise 
`if value, isThere := studentAges["Max"]; isThere { }`.

**Kommandoprotokoll**
[PROT::ALT:go-basics2.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go0/go-basics2.go]
[ENDINSTRUCTOR]
