title: "Grundlagen von Go: Arrays and Slices"
stage: alpha
timevalue: 2
difficulty: 2
explains: Slice (Golang)
assumes: go-basics, go-pointers, go-functions, go-structs1
---

[SECTION::goal::idea,experience]
Ich habe Arrays und Slices in Go kennengelernt.
[ENDSECTION]


[SECTION::background::default]
Ob bei Zeichenkettenmanipulationen, HTTP-Anfragen oder Ein- und Ausgabeoperationen — 
an Slices führt kein Weg vorbei.

Sie sind zugleich eine der Stellen, an denen Go deutliche Leistungsgewinne erzielt:
Statt Arrays zu kopieren, werden diese bei Bedarf mehrfach referenziert — als Slices.
[ENDSECTION]


[SECTION::instructions::detailed]

#### Array

Ein Array ist ein _Einblocktyp_, der eine Sammlung von Einträgen darstellt,
wo alle Einträge zum gleichen Typ gehören und die Größe (Anzahl von Einträgen) fest ist.

```go
var arr [5]int                      // arr == [0 0 0 0 0]
anotherArr := arr                   // eine Kopie wurde erstellt
anotherArr[0] = 42
fmt.Println(arr, anotherArr)        // [0 0 0 0 0] [42 0 0 0 0]
```

[NOTICE]
Die Größe des Arrays ist in seinem Typ festgelegt: `[5]int` und `[4]int` sind 
zwei verschiedene Datentypen.
[ENDNOTICE]

Reine Arrays werden in Go relativ selten verwendet, daher konzentrieren wir uns auf Slices.


#### Slice

Slices bauen immer auf Arrays auf.
Ein [TERMREF::Slice (Golang)] ist eine "View" bzw. eine Sicht in das zugrundeliegende Array
und ist ein _Mehrblocktyp_.

Die Laufzeitdarstellung eines Slice (definiert in `go/src/runtime/slice.go`)
sieht intern wie folgt aus:

```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

* `array`: das zugrundeliegende Array beziehungsweise ein Verweis auf die Speicherstelle, wo sich
  das Array befindet;
* `len`: die Anzahl von Elementen in dem Slice.
  Diese Zahl ist immer zwischen 0 und der Größe des zugrundeliegenden Arrays und kann
  mittels der eingebauten Funktion
  [`len()`](https://pkg.go.dev/builtin#len)
  ermittelt werden;
* `cap`: die Anzahl von Elementen, die der Slice maximal beinhalten kann ("Capacity", Kapazität).
  Diese Zahl wird von der eingebauten Funktion
  [`cap()`](https://pkg.go.dev/builtin#cap)
  zurückgegeben und stellt die Anzahl von Zellen bis zum Ende des zugrundeliegenden Arrays dar.
  Wird es zu einem Slice mit `cap = 0` ein weiteres Element hinzugefügt, so wird ein neues zugrunde
  liegendes Array doppelter Größe allokiert.

Slices können entweder eigenständig instanziiert werden oder als eine Sicht in ein
existierendes Array:

```go
sl := make([]int, 4)                // Typ und initiale Größe eines Slice
sl := make([]int, 4, 10)            // Typ, initiale Größe und initiale Kapazität eines Slice

sl := []int{0, 1, 2, 3, 4}          // direkter Slice mit Werten

arr := [5]int{7, 9, 11, 13, 14}     // mit Werten initialisiertes Array der Länge 5
sl := arr[1:3]                      // slice mit Werten {9, 11} (denn der zweite Index ist exklusiv)
```

Um ein besseres Verständnis zu schaffen, was Slices eigentlich sind,
lesen Sie nun diesen Artikel (es gibt Bilder!):
[The Go Blog: Go Slices — usage and internals](https://go.dev/blog/slices-intro).

Informieren Sie sich über diese zwei Funktionen für Slices:

- [append](https://pkg.go.dev/builtin#append)
- [copy](https://pkg.go.dev/builtin#copy)

Schauen Sie sich die folgenden Beispiele _genau_ an; denken Sie mit.

Versuchen Sie zunächst selbst nachzuvollziehen, was in jeder Zeile passiert, 
_bevor_ Sie die Kommentare lesen.

```go
// Beispiel 1
arr := [5]int{7, 9, 11, 13, 14}     // mit Werten initialisiertes Array der Länge 5
sl := arr[1:3]                      // slice mit Werten {9, 11} (denn der zweite Index ist exklusiv)

fmt.Println(len(sl))                // Länge: 2
fmt.Println(cap(sl))                // Kapazität: 4, denn Element 0 des Arrays ist nicht für den Slice verfügbar

fmt.Println(sl)                     // [9 11]
fmt.Println(sl[0])                  // 9
fmt.Println(sl[1])                  // 11
sl[0] = 8                           // das verändert das Array arr!
fmt.Println(arr)                    // [7 8 11 13 14]


// Beispiel 2
arr := [5]int{7, 9, 11, 13, 14}

sl := arr[:]                        // kreiert einen Slice für das gesamte ursprüngliche Array (len = 5, cap = 5)
sl := arr[2:]                       // kreiert einen Slice ab Index 2 bis zum Ende des Arrays (len = 3, cap = 3)
sl := arr[:3]                       // kreiert einen Slice vom Anfang des Arrays bis zu Index 3 (exklusiv) (len = 3, cap = 5),
                                    // ermöglicht also das Hinzufügen zweier weiterer Elemente
sl = append(sl, 8)                  // überschreibt die "13" im ursprünglichen Array arr!
```

<!-- time estimate: 10 min -->

[NOTICE]
Es gibt eine andere Schreibweise, die die Kapazität eines Slice beschränkt: `s[start:end:max]`.
`max` ist die obere Grenze (lies: exklusiv) von Indizes, die vom Slice angefasst werden dürfen.
Ist `max = 4`, so darf der Slice höchstens Index 3 anfassen.

Dies beschränkt die Kapazität automatisch auf `(max - start)`.
[ENDNOTICE]

```go
// Beispiel 3
arr := [5]int{7, 9, 11, 13, 14}
sl := [0:2:2]                       // kreiert einen Slice ab Index 0 bis zu Index 2 (exklusiv) (len = 2, cap = 2)
sl = append(sl, 8)
fmt.Println(arr)                    // [7 9 11 13 14]
fmt.Println(sl)                     // [7 9 8]
sl[0] = 42
fmt.Println(arr)                    // [42 9 11 13 14] 
```
<!-- time estimate: 10 min -->

[EQ] Schauen Sie sich den folgenden Quellcodeabschnitt an.
Was befindet sich am Ende in Variablen `arr`, `sl1` und `sl2`?
Was ist das zugrundeliegende Array von `sl1` und `sl2`?

```go
arr := [6]int{10, 20, 30, 40, 50, 60}
sl1 := arr[1:4]
sl2 := sl1[:cap(sl1)]  // Achtung: cap(sl1) != len(sl1)
sl2[3] = 99
```

<!-- time estimate: 5 min -->

Lesen Sie diesen Artikel aufmerksam durch:
[Go by Example: Slices](https://gobyexample.com/slices).
(Ganz unten gibt es noch ein Kästchen, wo das vorgestellte Programm ausgeführt wird.
Leicht zu übersehen!)

[EQ] Schauen Sie sich die Quellcodeabschnitte unten an, identifizieren Sie jeweils 
Probleme und schlagen Sie eine Lösung vor.

__Problematisches Beispiel 1:__

```go
arr := [5]int{4, 8, 6, 0, -1}
slice1 := arr[1:4]
slice2 := arr[1:5]
slice1 = append(slice1, 42)
fmt.Println(slice2) // ???
```

__Problematisches Beispiel 2:__

```go
arr := [5]int{4, 8, 6, 0, -1}
slice1 := arr[1:4]
slice2 := arr[1:4]
slice1[0] = 999
fmt.Println(slice2) // ???
```

__Problematisches Beispiel 3:__

```go
func modifySlice(s []int) {
    s = append(s, 42)
}
```

<!-- time estimate: 10 min -->

Implementieren Sie die folgenden Funktionen:

[ER] `AddElement(slice []int, element, at int) []int`:
ein Element an einem Index `at` in einen Slice einfügen;
das Element, das vorher an dieser Stelle stand, und alle nachfolgenden rücken eine Position nach
rechts.
Die Funktion gibt den neuen Slice zurück.

[ER] `RemoveElement(slice []int, at int) []int`:
ein Element an einem Index `at` entfernen und die Größe des Slice entsprechend anpassen.
Alle nachfolgenden Elemente rücken eine Position nach links.
Die Funktion gibt den neuen Slice zurück.
Wenn `at` kleiner als 0 oder größer als der letzte Index von `slice` ist, soll entsprechend 
das erste oder das letzte Element entfernt werden. 

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:
```go
[INCLUDE::include/go-slices-control-snippet.go]
```

[ER] Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen;
bitte ebenfalls zufügen:

```go
func main() {
    testSlices()
}
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 15 min -->
[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Hinweise]
`testSlices`:
diese Funktion sollte unverändert in dem abgegebenen Quellcode präsent sein,
damit das Kommandoprotokoll nicht verfälscht wird.

`AddElement`, `RemoveElement`:
Der Zweck ist, dass Studierende Slices erstellen und modifizieren können.

**Kommandoprotokoll**
[PROT::ALT:go-arrays-and-slices.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier: 
[TREEREF::/Sprachen/Go/go-slices.go].
[ENDINSTRUCTOR]
