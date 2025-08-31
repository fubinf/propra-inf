title: "Go-Grundlagen: Maps"
stage: alpha
timevalue: 3.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich habe Maps in Go kennengelernt.
[ENDSECTION]

[SECTION::background::default]
TODO
[ENDSECTION]

[SECTION::instructions::detailed]

Zur Erinnerung: [PARTREFMANUAL::go-reference-and-value-types::hier] finden Sie eine
Erklärung, was Referenz- und Werttypen sind.


#### Map (Referenztyp)

Eine Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre
Schlüssel ermöglicht.

Eine Map ist ein Referenztyp und wird ebenfalls mithilfe der Funktion `make()` erstellt:

```go
m := make(map[string]int)       // "string" ist der Typ der Schlüssel, "int" ist der Typ der Werte
m["one"] = 1
fmt.Println(m)                  // map[one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist, wenn kein solcher Schlüssel existiert
fmt.Println(len(m))             // 1
```

Für die Fallunterscheidung, ob ein Schlüssel bereits vorhanden ist oder nicht,
dient folgendes Idiom:

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

[WARNING]
Die Konvention hier ist genau das Gegenteil von `err != nil`.

Der zweite Rückgabewert eines Funktionsaufrufs `val, err := someFunction()`
ist gesetzt, wenn der Aufruf fehlgeschlagen ist.

Beim Lesezugriff auf Maps hingegen ist der zweite Rückgabewert gesetzt, wenn alles
glattgelaufen ist und der Schlüssel tatsächlich in der Map existiert.

Konventionell wird der zweite Rückgabewert beim Map-Zugriff `ok` genannt.
Wir empfehlen jedoch das Paar `value, isThere` für Maps: Selbst wenn einem die Feinheiten
mal entfallen, kann eine aussagekräftige Benennung der Variablen den Tag retten.
[ENDWARNING]

Falls es keinen solchen Schlüssel gibt, führt `delete()` keine Aktion aus.

[ER] Implementieren Sie eine Funktion
`func AddElementIfNotThere(m map[string]int, key string, value int)`:
ein Schlüssel-Wert-Paar einfügen, falls der Schlüssel noch nicht benutzt wurde.
Ansonsten keine Aktion.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-maps-control-snippet.go]
```

[ER] Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen;
bitte ebenfalls zufügen:

```go
func main() {
    testMaps()
}
```

[EC] Führen Sie das Programm mittels `go run go-maps.go` aus.

<!-- time estimate: 10 min -->

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
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
`testMaps`:
diese Funktion sollte unverändert in dem abgegebenen Quellcode präsent sein,
damit das Kommandoprotokoll nicht verfälscht wird.

Korrektur von `AddElementIfNotThere`:
Der Zweck ist, dass Studierende überprüfen können, ob der Wert da ist.
Hier ist wichtig zu verstehen, wie man einen Nullwert von einem tatsächlich vorhandenen
Wert unterscheiden kann — nämlich mit der Schreibweise
`if value, isThere := studentAges["Max"]; isThere { }`.

**Kommandoprotokoll**
[PROT::ALT:go-maps.prot]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-maps.go]
[ENDINSTRUCTOR]
