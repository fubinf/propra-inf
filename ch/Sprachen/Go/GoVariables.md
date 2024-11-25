title: Variablen und Datentypen
stage: draft
timevalue: 1
difficulty: 1
<!-- explains:
assumes:
requires: -->
---

[SECTION::goal::product/idea/experience/trial]
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

name := "gopher"            // oder den konkreten Datentypen herleiten lassen
```

__Note:__ falls es sich um primitive Datentypen handelt, werden nur `int`, `float64` `string` und `bool` hergeleitet:
```go
// kurze Schreibweise               // volle Schreibweise
number := 42                        var number int = 42
pi := 3.1415                        var pi float64 = 42
name := "gopher"                    var name string = "gopher"
truth := true                       var truth bool = true
```

Komplexere Datentypen werden ohne Ausnahmen hergeleitet, daher ist die kurze Schreibweise im Go-Universum bevorzugt.

### Nullwerte
Was passiert aber, wenn eine Variable __nur deklariert__ wurde? Die Variable wird automatisch mit Nullwerten definiert:
* `0` für die Typen, die eine Zahl darstellen sollen;
* `false` für boolesche Werte;
* `""` für `string`;
* zusammengesetzte Datentypen behalten dabei ihre Struktur, aber die Werte von den einzelnen Feldern werden ebenfalls mit Nullwerten definiert. 

### Konstanten
Konstanten werden mithilfe vom Schlüsselwort `const` deklariert und müssen bei Deklaration auch definiert werden. Sie dürfen außerdem nur primitive Datentypen beinhalten.
```go
const pi = 3.1415926
const pi float64 = 3.1415926

// error: Missing value in the const declaration
const pi float64
```
[SECTION::instructions::detailed/loose/tricky]

### ...

- [EC] Kommando
- [EQ] Frage
- [ER] Anforderung

### ...

[NOTICE]
[ENDNOTICE]

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[FOLDOUT::Warum gibt es ein `float64`, aber kein `int64`?]
Eigentlich, es gibt mehr Typen für Zahlen als angeführt oben. Hier ist die vollständige Liste:
* ganze Zahlen mit Vorzeichen: `int` , `int8` , `int16` , `int32` (`rune`) , `int64`;
* ganze Zahlen ohne Vorzeichen: `int` , `uint8` (`byte`), `uint16` , `uint32` , `uint64` , `uintptr`;
* Gleitkommazahlen: `float32` `float64`;
* Komplexe Zahlen: `complex64` `complex128`.

__Bitte: Keine vorzeitige Optimierung!__

Sparen Sie keine Bits Speicherplatz durch Ersetzen von allen `int` Variablen durch `int8` oder `int16`, wenn Sie keinen guten Grund dafür haben. Die meisten Funktionen aus der Standardbibliothek operieren auf `int`s, daher ist die Konvertierung zwischen den Typen in der Regel teurer als ein paar Bits von Speicherverbrauch.

[ENDFOLDOUT]

TODO_brandes: überlegen, ob wir einen Ausflug in Typisierung brauchen und falls ja, wie das aussehen soll.
<!-- [FOLDOUT::Typisierung: Was ist das?]
Aus verschiedenen Typisierungsklassifikationen gibt es zwei, die besonders oft benutzt werden.
* __Statische vs. dynamische Typisierung__
    Was eine Typisierung ist, ist eine relativ komplexe Frage. Eine vereinfachte Definition ist 
    In einer statisch typisierten Programmiersprache müssen die Datentypen von allen Variablen zur Kompilierungszeit bekannt werden, wie beispielsweise in C/C++ oder Java. Falls ein Datentyp nicht vom Compiler eindeutig bestimmt werden kann, führt das zu einem Kompilierungsfehler.

    In einer dynamisch typisierten Programmiersprache darf eine Variable während des Programmablaufs verschiedene Datentypen annehmen, wie beispielsweise in Python.
* __Starke vs. schwache Typisierung (strong/weak)__

    Bei einer starken Typisierung werden die vom Compiler/Interpreter durchgeführten Überprüfungen strikter. Beispiel: Python gibt uns einen TypeError aus, wenn eine Zahl durch eine Zeichenkette dividiert wird.
    
    Bei einer schwachen Typisierung sind diese Überprüfungen nicht so strikt und der Compiler/Interpreter versucht den Code trotzdem zum Laufen zu bringen. Um die TypeErrors umzugehen, werden oft spezielle Mechanismen eingebaut, wie beispielsweise [Type coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion) in JavaScript. 
    Gute Beispiele sind Python und JavaScript.  
* [Nominal vs. structural](https://adabeat.com/fp/introduction-to-type-systems/)
[ENDFOLDOUT] -->

[ENDSECTION]

[SECTION::submission::reflection/information/snippet/trace/program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::]
.
[ENDINSTRUCTOR]
