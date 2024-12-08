title: Functionen
stage: draft
timevalue: 0.5
difficulty: 1
requires: GoIDE, GoProgramStructure, GoVariablesAndPrimitives
---

[SECTION::goal::idea]
Ich verstehe, wie ich eine Funktion definieren und aufrufen kann.
[ENDSECTION]

[SECTION::background::default]
Wir betrachten zuerst die wichtigsten Bausteine einer Funktion und gehen danach auf die Nuancen ein.
[ENDSECTION]

### Anatomie einer Funktion

Jede Funktion in Go besteht aus folgenden Teilen:

* `func` Schlüsselwort;
* (optional Funktionsname)
* Runde Klammer `()` für die Parameter: Parameter werden nacheinander als Name-Typ Paare aufgelistet;
* Signatur der Rückgabe (leer, falls die Funktion nichts zurückgibt)
* Funktionsdefinition in geschweiften Klammern `{}`

Eine Funktion, die uns schon bekannt vorkommt, ist die `main`-Funktion

```go
func main() {
    ...
}
```

Weitere Beispiele
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

// mehrere Parameter (verkürzt)
func constructFullName(firstName, lastName string) string {
    return fmt.Sprintf("%v %v", firstName, lastName)
}

// anonyme/"lambda" Funktion, die mit zwei Zahlen aufgerufen wird
func(x int, y int) {
    return x * y
}(4, 5)

```

Alle Funktionen dürfen auf globale Variablen zugreifen:

```go
const Pi = 3.1415

func area(r float64) float64 {
    return Pi * r * r
}
```

### Benannte Rückgabewerte (named return values)
Eine weitere Möglichkeit, Werte aus der Funktion zurückzugeben, sind die benannten Rückgabewerte.
```go
// Variablen i und err sind bereits mit entsprechenden Nullwerten initialisiert
func testNakedReturn() (i int, err error) {
    i = 42
    err = nil
    // hier werden alle Variablen automatisch zurückgegeben, die in der Funktionssignatur initialisiert wurden.
    // Dies nennt sich "naked return"
    return
}

func testNormalReturn() (int, error) {
    // Variablen i und err müssen hier initialisiert werden
    i := 42
    var err error = nil
    // und explizit zurückgegeben werden
    return i, err
}

func testNamedReturn() (i int, err error) {
    // das ist auch valide 
    return 42, nil
}
```

Solche "naked returns" sind in der Regel zu vermeiden, es sei denn die Funktion ist sehr klein (unter 10 Codezeilen).

Wie man sich vorstellen kann, Variablennamen in der Funktionssignatur können sehr hilfreich für die Lesbarkeit und Dokumentation sein.
Andererseits gibt `return` implizit alle Variablen zurück, die in der Funktionssignatur stehen, was fehleranfällig ist.

In der Praxis kommt die bevorzugte Schreibweise darauf an, wie groß die Funktion ist. Wenn sie mehr als 3 Rückgabewerte hat, ist
es wahrscheinlich vorteilhaft, die Rückgabevariablen für Dokumentationszwecke auch in die Funktionssignatur zu schreiben:

```go
func getWeatherReport(location Location) (
    temperature float64, 
    pressure float64, 
    windSpeed float64, 
    windDirection string,
    err error,
) {
    data, err := api.getWeatherReport(location)
    if err != nil {
        return temperature, pressure, windSpeed, windDirection, err        
    }
    ...
    return temperature, pressure, windSpeed, windDirection, nil
}
```

[NOTICE]
Es ist diskutabel, ob die oben angeführte Schreibweise doch zu wiederholend ist. Orientieren Sie sich an gesunden Menschenverstand: 
Wenn es auf den ersten Blick klar ist, was die Funktion tut, sind Sie immer auf der sicheren Seite.
[ENDNOTICE]

### Funktionen höherer Ordnung

Eine Funktion darf eine andere Funktion als Parameter bekommen:

```go
func apply(
    arg int, 
    operation func(int) int,
) int {
    return operation(arg)
}
```

Diese Funktion nimmt zwei Parameter an: Eine Zahl und eine Funktion, die ebenfalls eine Zahl übergeben bekommt und zurückgibt.
`operation` ist der Name der Funktion und `func(int) int` ihre Signatur ("sie nimmt eine Zahl an und gibt eine Zahl zurück").

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

oder mit einer anonymen Funktion:
```go
func main() {
    squared := apply(4, func(i int) int { return i * i })
}
```

oder die Funktion zuerst in einer Variable speichern (das ist zwar möglich, aber eher unkonventionell):
```go
func main() {
    square := func(i int) int { return i * i }
    squared := apply(4, square)
}
```

### Variadische Funktionen

Variadische Funktion ist eine Funktion, die eine variable Anzahl an Parameter annehmen kann. 
`xs` ist in dem Fall ein Slice (das lernen Sie in der nächsten Aufgabe, für jetzt - Liste) von `int`s.

```go
func printNumbers(xs ...int) {
    ...
}
```

### `defer`

TODO_brandes: Aufgabe zu Funktionen (aber ohne Structs)
[SECTION::submission::program]
.
[ENDSECTION]

[INSTRUCTOR::Acceptance Criteria]
.
[ENDINSTRUCTOR]
