title: "Go-Grundlagen: Arrays and Slices"
stage: alpha
timevalue: 1.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics, go-pointers, go-functions
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

#### Array (Werttyp)

Ein Array ist ein Werttyp, der eine Sammlung von Einträgen darstellt,
wo alle Einträge zum gleichen Typ gehören und die Größe (Anzahl von Einträgen) fest ist.

```go
var arr [5]int                      // arr == [0 0 0 0 0]
anotherArr := arr                   // eine Kopie wurde erstellt
anotherArr[0] = 42
fmt.Println(arr, anotherArr)        // [0 0 0 0 0] [42 0 0 0 0]
```

Reine Arrays werden in Go relativ selten verwendet, daher konzentrieren wir uns auf Slices.


#### Slice (Referenztyp)

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
  zurückgegeben und stellt die Anzahl von Zellen
  bis zum Ende des zugrundeliegenden Arrays dar.

[FOLDOUT::Was ist `unsafe.Pointer`?]
`unsafe.Pointer` ist ein Zeiger ohne Typ — ähnlich wie `void*` in C.

Solche Zeiger werden beispielsweise in Low-Level-Systemprogrammierung benutzt,
wo direkter Speicherzugriff (ohne Einschränkungen des Typsystems) von Vorteil ist.

Momentan müssen Sie sich keine Gedanken darüber machen: Einmal davon gehört
zu haben reicht völlig aus.

Wenn Sie doch mehr zum Thema wissen wollen, schauen Sie sich die
[Dokumentation](https://pkg.go.dev/unsafe#Pointer)
und den Artikel
[Exploring ‘unsafe’ Features in Go 1.20: A Hands-On Demo](https://medium.com/@bradford_hamilton/exploring-unsafe-features-in-go-1-20-a-hands-on-demo-7149ba82e6e1)
an.
[ENDFOLDOUT]

Informieren Sie sich über diese zwei Funktionen für Slices:

- [append](https://pkg.go.dev/builtin#append)
- [copy](https://pkg.go.dev/builtin#copy)

Slices können entweder eigenständig instanziiert werden oder als eine Sicht in ein existierendes Array:

```go
sl := make([]int, 4)            // Typ und initiale Größe eines Slice
sl := []int{0, 1, 2, 3, 4}      // direkter Slice mit Werten

arr := [5]int{7, 9, 11, 13, 14}    // mit Werten initialisiertes Array der Länge 5

sl := arr[1:3]                  // slice mit Werten {9, 11} (denn der zweite Index ist exklusiv)
fmt.Println(len(sl))            // Länge: 2
fmt.Println(cap(sl))            // Kapazität: 4, denn Element 0 des Arrays ist nicht für den Slice verfügbar

fmt.Println(sl)                 // [9 11]
fmt.Println(sl[0])              // 9
fmt.Println(sl[1])              // 11
sl[0] = 8                       // das verändert das Array arr!
fmt.Println(arr)                // [7 8 11 13 14]
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

[EQ] Schauen Sie sich den folgenden Quellcodeabschnitt an.
Was befindet sich am Ende in Variablen `arr`, `sl1` und `sl2`?
Was ist das zugrundeliegende Array von `sl1` und `sl2`?

```go
arr := [6]int{10, 20, 30, 40, 50, 60}
sl1 := arr[1:4]
sl2 := sl1[:cap(sl1)]  // Achtung: cap(sl1) != len(sl1)
sl2[3] = 99
```

<!-- time estimate: 10 min -->

Wie bereits erwähnt, können Slices mithilfe der Funktion `make([]T, initialSize)` kreiert werden.
Das zugrundeliegende Array wird dann automatisch erstellt und hat die Größe von `initialSize`.

Ein solcher Slice verhält sich im Wesentlichen wie ein dynamisches Array:
Sobald versucht wird, zum vollen Slice ein weiteres Element hinzuzufügen,
wird ein neues Array doppelter Größe allokiert (und damit gelingt der Versuch).

Lesen Sie nun diesen Artikel aufmerksam durch:
[Go by Example: Slices](https://gobyexample.com/slices).
(Ganz unten gibt es noch ein Kästchen, wo das vorgestellte Programm ausgeführt wird.
Leicht zu übersehen!)

[EQ] Welche Aspekte von Slices würden Sie als fehleranfällig bezeichnen?
(Nutzen Sie die Hinweise unten gerne als Inspiration.)

[HINT::Beispiel 1]
```go
arr := [5]int{4, 8, 6, 0, -1}
slice1 := arr[1:4]
slice2 := arr[1:4]
slice1[0] = 999
fmt.Println(slice2) // ???
```

Sehen Sie hier ein Problem?
Welches?
[ENDHINT]

[HINT::Beispiel 2]
```go
// Option 1
func processData(data []byte) []byte {
    // processing...
    return data[100:110]
}

// Option 2
func processData(data []byte) []byte {
    result := make([]byte, 10)
    // processing...
    copy(result, data[100:110])
    return result
}
```

In welcher der zwei Optionen kann der Garbage Collector den Slice `data` aufräumen,
wenn die Funktion `processData` beendet wird?

Wozu führt das, wenn `data` sehr groß ist?
[ENDHINT]

[HINT::Beispiel 3]
```go
func modifySlice(s []int) {
    s[0] = 999
    s = append(s, 42)
}
```

Beeinflusst die Zuweisung `s = append(s, 42)` den ursprünglichen Slice?
[ENDHINT]

Um ein besseres Verständnis zu schaffen, was Slices eigentlich sind,
lesen Sie nun diesen Artikel (es gibt Bilder!):
[The Go Blog: Go Slices — usage and internals](https://go.dev/blog/slices-intro)
.
[ENDFOLDOUT]

Implementieren Sie die folgenden Funktionen:

[ER] `func AddElement(slice []int, element, at int) []int`:
ein Element an einem Index `at` in einen Slice einfügen;
das Element, das vorher an dieser Stelle stand, und alle nachfolgenden rücken eine Position nach
rechts.
Die Funktion gibt den neuen Slice zurück.

[ER] `func RemoveElement(slice []int, at int) []int`:
ein Element an einem Index `at` entfernen und die Größe des Slice entsprechend anpassen.
Alle nachfolgenden Elemente rücken eine Position nach links.
Die Funktion gibt den neuen Slice zurück.

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

[EC] Führen Sie das Programm mittels `go run go-slices.go` aus.

<!-- time estimate: 40 min -->
[ENDSECTION]

[SECTION::submission::trace,program]
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

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-slices.go]
[ENDINSTRUCTOR]
