title: Arrays, Slices, Maps
stage: draft
timevalue: 1
difficulty: 2
requires: GoIDE, GoProgramStructure, GoVariablesAndPrimitives, GoFunctions
---

[SECTION::goal::idea]
Ich verstehe, was ein Array, ein Slice und ein Map sind und wo ich sie anwenden kann.
[ENDSECTION]

## Array

Ein Array ist eine Sammlung von Elementen des gleichen Typs, welche eine feste Größe besitzt.

Der wichtigste Punkt ist hier "feste Größe". Arrays können nicht dynamisch vergrößert/verkleinert werden.
```go
// die Größe des Arrays muss eine Konstante sein
var arr [5]int
fmt.Println(arr)                // [0 0 0 0 0]

arr = [5]int{1, 2, 3, 4, 5}
fmt.Println(arr)                // [1 2 3 4 5]
```

Aus Python-Sicht sind Arrays sehr unbequem: Was ist ihr Nutzen, wenn man kein Element hinzufügen/entfernen darf?
Der Vorteil von Arrays ist Leistung. Sie sind in einem zusammenhängenden Speicherblock gespeichert, was Iteration
viel schneller macht als Pointer-Lookup einer verketteten Liste.

Zugriff auf die einzelnen Elemente geschieht genauso wie bei Python-Listen:
```go
var arr [5] int
arr[3] = 4
fmt.Println(arr)                // [0 0 0 4 0]
fmt.Println(arr[3])             // 4
```

Indizes eines Arrays starten immer bei 0.

## Slice

Slices bauen immer auf Arrays auf. Ein Slice ist eine "View" bzw. eine Sicht in das zugrundeliegende Array.

Das ist die Laufzeit-Darstellung eines Slices (`go/src/runtime/slice.go`):
```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

* `array` ist das zugrundeliegende Array. Zeiger (`Pointer`) wird später ausführlicher erklärt. Für jetzt - Speicheradresse, wo sich das Array befindet;
* `len` "Größe/Länge" ist die Anzahl von Elementen in dem Slice. Diese Zahl ist immer zwischen 0 und der Größe des Arrays und kann mithilfe der eingebauten Funktion `len()` ermittelt werden;
* `cap` "Kapazität" ist die Anzahl von Elementen, die der Slice maximal beinhalten kann. Diese Zahl wird von der eingebauten Funktion `cap()` zurückgegeben und stellt
Anzahl von "Zellen" bis zum Ende des zugrundeliegenden Arrays dar.

Slices können entweder eigenständig erstellt werden oder als die "Sicht" in ein existierendes Array:
```go
sl := []int{0, 1, 2, 3, 4}

// oder
arr := [5]int{0, 1, 2, 3, 4}

sl := arr[1:3]                   // erste Index ist inklusiv, zweite Index ist exklusiv
fmt.Println(len(sl))            // 2
fmt.Println(cap(sl))            // 4

fmt.Println(sl)                 // [1 2]
fmt.Println(sl[0])              // 1
fmt.Println(sl[1])              // 2
sl[0] = 8                       // wir verändern das Array arr!
fmt.Println(arr)                // [0 8 2 3 4]
```

Andere Schreibweisen:
```go
arr := [5]int{0, 1, 2, 3, 4}

sl := arr[:]        // kreiert einen Slice, welcher das ganze ursprüngliche Array beinhaltet (len = 5, cap = 5)
sl := arr[2:]       // kreiert einen Slice von Index 2 und bis zum Ende des Arrays (len = 3, cap = 3)
sl := arr[:3]       // kreiert einen Slice von Anfang des Arrays bis zu der Index 3 (exklusiv) (len = 3, cap = 5)
                    // da cap > len ist, können wir relativ billig neue Elemente hinzufügen
sl = append(sl, 8)  // das überschreibt aber die "3" aus dem ursprünglichen Array!
```

[NOTICE]
Neue Elemente werden in einen Slice mittels der `append()` Funktion hinzugefügt. 
Ein eigenständiger Slice verhält sich wie ein dynamisches Array - wenn es keinen Platz mehr gibt,
wird ein neues Array kreiert, der i. d. R. zweimal größer ist als das ursprüngliche, 
und alle vorhandenen Elemente werden in das neue Array kopiert.
[ENDNOTICE]

[WARNING]
Slices werden mit `nil` initialisiert:
```go
var x []int     // x == nil
```
[ENDWARNING]

## Map

Map ist eine Sammlung von Schlüssel-Wert Paaren (key-value).
Map ist sehr ähnlich wie `dict` in Python, ist jedoch statisch typisiert - 
alle Schlüssel und alle Werte müssen jeweils von dem gleichen Typen sein.

Ein Map wird mithilfe von `make()` Funktion erstellt:
```go
m := make(map[string]int)       // "string" ist der Typ von Schlüsseln, "int" ist der Typ von Werten
m["one"] = 1
fmt.Println(m)                  // [one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist
fmt.Println(len(m))             // 1
```

[WARNING]
Maps werden mit `nil` initialisiert.
```go
var m map[string]int
m["one"] = 1            // panic: assignment to entry in nil map 
```
[ENDWARNING]

Weitere Infos können [hier](https://go.dev/blog/maps) nachgelesen werden.

[SECTION::submission::program]
Implementieren Sie eine Funktion, die ein Element aus dem Slice entfernt.
[ENDSECTION]

[INSTRUCTOR::Acceptance Criteria]
.
[ENDINSTRUCTOR]
