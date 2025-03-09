title: Variablen und primitive Datentypen
stage: draft
timevalue: 1
difficulty: 1
requires: go-ide, go-program-structure
---

[SECTION::goal::idea]
Ich verstehe, wie man Variablen deklarieren und definieren kann. Ich kenne mich mit den primitiven Datentypen aus.

[ENDSECTION]

[SECTION::background::default]
Go ist eine statisch typisierte Programmiersprache. Die Typen von allen Variablen werden entweder explizit angegeben oder von dem Compiler hergeleitet.
[ENDSECTION]

### Primitive Datentypen

Es gibt 5 wichtigste primitive Datentypen:

* `int`: eine ganze Zahl mit Vorzeichen (signed)
* `float64`: eine Gleitkommazahl
* `byte`: 8 Bits von Information (wichtig im Kontext von Dateioperationen oder Netzwerken benutzt)
* `string`: Zeichenkette
* `bool`: Ein boolescher Wert, `true` oder `false`

### Eine Variable deklarieren/definieren
```go
var name string             // deklarieren

name = "gopher"             // definieren

var name string = "gopher"  // beide Aktionen kombiniert

name := "gopher"            // oder den konkreten Datentypen
var name = "gopher"         // herleiten lassen

width, height := 1920, 1080 // mehrere Variablen auf einmal
```

__Note:__ falls es sich um primitive Datentypen handelt, werden nur `int`, `float64` `string` und `bool` hergeleitet:
```go
// kurze Schreibweise               // volle Schreibweise
number := 42                        var number int = 42
pi := 3.1415                        var pi float64 = 42
name := "gopher"                    var name string = "gopher"
truth := true                       var truth bool = true
```

[FOLDOUT::Warum gibt es ein `float64`, aber kein `int64`?]
Doch. Es gibt mehr Typen für Zahlen als oben angeführt sind. Hier ist die vollständige Liste:

* ganze Zahlen mit Vorzeichen: `int` , `int8` , `int16` , `int32` (`rune`) , `int64`;
* ganze Zahlen ohne Vorzeichen: `int` , `uint8` (`byte`), `uint16` , `uint32` , `uint64` , `uintptr`;
* Gleitkommazahlen: `float32` `float64`;
* Komplexe Zahlen: `complex64` `complex128`.

__Bitte: Keine vorzeitige Optimierung!__

Sparen Sie keine Bits Speicherplatz durch Ersetzen von allen `int` Variablen durch `int8` oder `int16`, wenn Sie keinen guten Grund dafür haben. Die meisten Funktionen aus der Standardbibliothek operieren auf `int`s, daher ist die Konvertierung zwischen den Typen in der Regel teurer als ein paar Bits von Speicherverbrauch.

[ENDFOLDOUT]

[//]: # (Komplexere Datentypen werden ohne Ausnahmen hergeleitet, daher ist die kurze Schreibweise im Go-Universum bevorzugt.)

### Nullwerte
Was passiert aber, wenn eine Variable __nur deklariert__ wurde? Die Variable wird automatisch mit Nullwerten definiert:

* `0` für die Typen, die eine Zahl darstellen sollen;
* `false` für boolesche Werte;
* `""` für `string`.

[//]: # (* zusammengesetzte Datentypen behalten dabei ihre Struktur, aber die Werte von den einzelnen Feldern werden ebenfalls mit Nullwerten definiert. )

### Konstanten
Konstanten werden mithilfe vom Schlüsselwort `const` deklariert und müssen bei Deklaration auch definiert werden. Sie dürfen außerdem nur primitive Datentypen beinhalten.
```go
const pi = 3.1415926
const pi float64 = 3.1415926

// error: Missing value in the const declaration
const pi float64
```

[NOTICE]
Konstanten können nur global definiert werden (außerhalb von allen Funktionen). Es ist eine gute Praxis diese ganz oben in der Datei zu deklarieren, damit die anderen sofort sehen, welche Konstanten in dem Programm benutzt werden. Es gibt jedoch keine besonderen Namenskonventionen: einfach kleingeschrieben und _camelCase_, falls Sie mehrere Wörter benutzen.
[ENDNOTICE]

### Als Block deklarieren
Die Block-Schreibweise haben wir schon bei dem Wort `import` kennengelernt. `const` und `var` können genauso benutzt werden:
```go
const (
    pi  = 3.1415
    e   = 2.7183
    
    // da pi und e beide konstant sind, ist ihr Produkt ebenso konstant
    product = pi * e
)

var (
    name    = "Max"
    surname = "Mustermann"
)
```

[FOLDOUT::groß- oder kleingeschrieben: Was ist der Unterschied?]
Groß- und Kleinschreibung wird in Go als Sichtbarkeitsindikator benutzt. Zukünftig werden wir unsere Programme in mehrere Pakete zerlegen. Ab dem Punkt wird die Sichtbarkeit wichtig. Alle Variablen/Funktionen, deren Name großgeschrieben ist, gelten als __öffentliche/exportierte__ (exported/public) und werden aus anderen Paketen sichtbar. Ist der Name einer Variable/Funktion kleingeschrieben, so ist diese __privat__ (private) und kann nur in dem Paket benutzt werden, wo sie deklariert wurde.

Beispiel - hier deklarieren wir zwei Konstanten
```go
package A

const Pi = 3.1415
const e  = 2.7183
```

Beispiel - hier versuchen wir auf sie zuzugreifen
```go
package B

import (
    "fmt"
    "%projekt_name%/A"
)

func foo() {
    fmt.Println(A.Pi)       // funktioniert, weil Pi "exported" ist
    fmt.Println(A.e)        // funktioniert nicht, weil e privat ist
}
```

Selbst die Funktion `fmt.Println()` ist großgeschrieben - weil sie im `"fmt"`-Paket öffentlich/exportiert ist.
[ENDFOLDOUT]

[SECTION::submission::program]
Sie bekommen einen Code-Abschnitt, welcher einen Text im Terminal printen soll. Dort fehlen jedoch einige Wörter. Ihre Aufgabe besteht darin, diesen Text zu ergänzen, indem Sie die im Text benutzten Variablen definieren. Es gibt auch kleine Hinweise: `%s` Platzhalter signalisiert eine Zeichenkette, `%d` - eine ganze Zahl und `%.4f` - eine Gleitkommazahl, die mit nur 4 Nachkommastellen angezeigt wird.

Folgende Konstrukte soll es in Ihrer Lösung geben:

* eine Konstante;
* eine mittels kurzer Schreibweise definierte Variable;
* eine mittels voller Schreibweise definierte Variable;
* einen Block, wo mehrere Variablen definiert sind;
* eine mehrfache Zuweisung (wo mehrere Variablen mit einem "="-Zeichen definiert werden).

Speichern Sie anschließend Ihre Datei als `variables_abgabe.go` und geben Sie diese ab.

```go
[INCLUDE::snippets/variables_source.go]
```

[ENDSECTION]

[INSTRUCTOR::Acceptance Criteria]
Der Punkt ist, die Variablen auf verschiedene Art und Weise zu definieren und dabei die Datentypen beachten. Was für Wörter/Zahlen Studierende dort eingeben, sollte komplett irrelevant sein. Kreativität ist hier nicht vorausgesetzt, aber sehr wünschenswert.

Beispiellösung:
```go
[INCLUDE::ALT:variables_abgabe.go]
```
[ENDINSTRUCTOR]
