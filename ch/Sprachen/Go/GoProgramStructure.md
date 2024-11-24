title: Programmstruktur
stage: draft
timevalue: 0.5
difficulty: 1
---

[SECTION::goal::idea]
Ich verstehe, was die Schlüsselwörter `package`, `import` bedeuten und wie ein Go-Programm auszuführen ist.
[ENDSECTION]

[SECTION::background::default]
In der ersten Aufgabe haben wir IDE für Go Entwicklung eingerichtet und unser erstes Programm ausgeführt. Nun ist es Zeit, sich dieses Programm und die einzelnen Bauteile etwas genauer anzuschauen.
[ENDSECTION]

[SECTION::instructions::detailed]

Quellcode von "Hello World!":
```go
[INCLUDE::hello_world.go]
```

### 1. `package`
Ersetzen Sie nun `main` durch ein anderes Wort und führen Sie das Programm nochmal aus. Hat das immer noch funktioniert? Warum?

Falls Sie schon eine eigene Hypothese haben, dürfen Sie die Erklärung aufklappen.

[FOLDOUT::Erklärung]
In Go müssen alle Quellcodedateien zu einem _Paket_ (Package)  gehören. `package main` ist dabei ganz besonders - so versteht der Compiler, das dies ein ausführbares Programm ist. Demzufolge dürfen nur Dateien mit `package main` die tatsächliche `main()` Methode definieren, welche der Einstiegspunkt von dem Programm ist.

Alle anderen Pakete werden als Bibliotheken interpretiert, die in einem `main` Paket importiert und benutzt werden können. Solche Bibliotheken können nicht selbständig ausgeführt werden.
[ENDFOLDOUT]

### 2. `import`
So importiert man in einer Go Quellcodedatei andere Pakete. In dem Beispiel haben wir "fmt" Paket importiert, welches zur Go-Standardbibliothek gehört und uns Textausgabe ermöglicht. Falls mehrere Pakete importiert werden müssen, schreibt man sie in Klammern untereinander:

```go 
import (
    "fmt"
    "net/http"
    "log"
    ...
)
``` 

### 3. `func main()` 
Diese Funktion ist der Einstiegspunkt. Es darf nur eine `main()`Funktion geben, un diese muss sich in dem `main` Paket befinden.

`func` ist ein Schlüsselwort, welches eine Funktion deklariert (`def` in Python).

[ENDSECTION]


[SECTION::submission::program]
Schreiben Sie nun ein kleines Programm, das beim Ausführen eine zufällige ganze Zahl im Terminal ausgibt. Speichern Sie diese anschließend als `rand_int.go` und geben Sie diese Quellcodedatei ab. Sie dürfen als Ausgangspunkt das Beispiel von "Hello World" benutzen.

[HINT::Eine passende Funktion könnte im Paket `math` liegen...]

[ENDSECTION]

[INSTRUCTOR::Gedankengang prüfen]
Diese Aufgabe hat im Wesentlichen drei Schritte:

* die richtige Funktion (`Int()` aus `math/rand` bzw. `math/rand/v2`) zu importieren und dabei Klammer-Schreibweise zu benutzen;
* herauszufinden, dass `fmt.Println()` nicht nur Zeichenketten ausgeben kann, sondern beliebige Datentypen;
* nochmal das Ausführen im Terminal zu üben (`go run rand_int.go`).

Lösung:
```go
[INCLUDE::ALT:rand_int.go]
```
[ENDINSTRUCTOR]
