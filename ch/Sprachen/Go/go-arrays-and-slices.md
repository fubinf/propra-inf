title: "Go-Grundlagen: Arrays and Slices"
stage: alpha
timevalue: 2.5
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

#### Array (Werttyp)

Ein Array ist ein Werttyp, der eine Sammlung von Einträgen darstellt,
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

Slices können entweder eigenständig instanziiert werden oder als eine Sicht in ein
existierendes Array:

```go
sl := make([]int, 4)                // Typ und initiale Größe eines Slice
sl := make([]int, 4, 10)            // Typ, initiale Größe und initiale Kapazität eines Slice

sl := []int{0, 1, 2, 3, 4}          // direkter Slice mit Werten

arr := [5]int{7, 9, 11, 13, 14}     // mit Werten initialisiertes Array der Länge 5
sl := arr[1:3]                      // slice mit Werten {9, 11} (denn der zweite Index ist exklusiv)
```

[ER] In [PARTREF::go-pointers] haben Sie bereits (wahrscheinlich) das Paket `unsafe` kennengelernt.
Nun wollen Sie sich drei kleine Hilfsfunktionen schreiben:

1. `myLen(s []int) int` — funktioniert wie `len()`, aber ohne `len()` aufzurufen;
2. `myCap(s []int) int` — funktioniert wie `cap()`, aber ohne `cap()` aufzurufen;
3. `myPtr(s []int) unsafe.Pointer` — gibt den Zeiger `array` aus dem Slice-Header zurück.

Ihr Gedankengang:

- Information über einen Slice liegt in seinem Header (oben unter "Die Laufzeitdarstellung 
  eines Slice...").
  Einen Zeiger auf den Header vom Slice `s` bekommen Sie mittels `&s`;
- Ein Zugriff wie `(&s).len` ist leider nicht erlaubt.
  Sie wissen aber, dass `&s` genau auf so eine Struktur von Typ `slice` zeigt.
  Wenn Sie nur eine Möglichkeit hätten, das Go-Typsystem zu umgehen...
- Es gibt doch `unsafe.Pointer`! 
  Sicherlich können Sie `&s` zuerst in einen `unsafe.Pointer` umwandeln und dann in einen
  Zeiger des Typs `*slice`.
  An der Stelle spielt das Typsystem mit und erlaubt alle Zugriffe auf 
  `(*slice).len`, `(*slice).cap` und `(*slice).array`.
- Für die Umwandlung in einen `slice` müssen Sie die Struktur `slice` in Ihrem 
  eigenen Programm noch einmal definieren.
  Wichtig ist dabei nur, dass die Reihenfolge und die Typen der Felder genau mit 
  denen aus dem Header übereinstimmen.
  Die Namen der Felder spielen dabei keine Rolle.

<!-- time estimate: 15 min -->

[NOTICE]
Um ein besseres Verständnis zu schaffen, was Slices eigentlich sind,
lesen Sie nun diesen Artikel (es gibt Bilder!):
[The Go Blog: Go Slices — usage and internals](https://go.dev/blog/slices-intro).
[ENDNOTICE]

[ER] Schauen Sie sich die folgenden zwei Beispiele ganz genau an und denken Sie mit.
Versuchen Sie zunächst selbst nachzuvollziehen, was in jeder Zeile passiert, 
bevor Sie die Kommentare lesen.

```go
// Beispiel 1:

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

arr := [5]int{0, 1, 2, 3, 4}

sl := arr[:]                        // kreiert einen Slice für das gesamte ursprüngliche Array (len = 5, cap = 5)
sl := arr[2:]                       // kreiert einen Slice ab Index 2 bis zum Ende des Arrays (len = 3, cap = 3)
sl := arr[:3]                       // kreiert einen Slice vom Anfang des Arrays bis zu Index 3 (exklusiv) (len = 3, cap = 5),
                                    // ermöglicht also das Hinzufügen zweier weiterer Elemente
sl = append(sl, 8)                  // überschreibt die "3" im ursprünglichen Array arr!
```

<!-- time estimate: 10 min -->

Informieren Sie sich über diese zwei Funktionen für Slices:

- [append](https://pkg.go.dev/builtin#append)
- [copy](https://pkg.go.dev/builtin#copy)

[ER] Nun schauen Sie sich die Funktion `append` ganz genau an,
indem Sie einen Slice erstellen und mehrmals eine Zahl hinzufügen.

1. Schreiben Sie eine kleine Funktion `printData(s []int)`, welche alle wichtigen
   Daten aus dem Slice-Header auf die Kommandozeile ausgeben soll: die Länge des Slice,
   die Kapazität und den Zeiger auf das zugrundeliegende Array.
   Ganz bequem haben Sie kurz davor drei kleine Funktionen implementiert, die genau 
   die richtigen Informationen liefern.
   Benutzen Sie außerdem dieses Format: `"len(s) = %2v, cap(s) = %2v, &s = %v\n"`.
2. Schreiben Sie eine andere Funktion `testAppend()`, wo Sie zuerst einen leeren `int`-Slice 
   kreieren und seine Information auf die Kommandozeile ausgeben lassen (mittels `printData(s)`).
   Danach fügen Sie 10 Zahlen nacheinander in den Slice ein und rufen Sie nach jedem Einfügen
   `printData(s)` auf.

[EQ] Wann wird ein neues Array kreiert?
Wie groß ist das neue Array?
Kennen Sie eine Datenstruktur mit ähnlicher Funktionsweise?

[HINT::Woher weiß ich, dass ein neues Array kreiert wurde?]
Das erkennen Sie an der Speicheradresse, die die Funktion `myPtr(s []int)` ausliest.

Gleiche Speicheradresse — gleiches Array.
Eine neue Adresse signalisiert, dass ein neues Array angelegt wurde.
[ENDHINT]

[HINT::Datenstrukturen...]
Eine derartige Datenstruktur ist in Informatik als 
[dynamisches Array](https://en.wikipedia.org/wiki/Dynamic_array) 
bekannt.
[ENDHINT]

[EQ] Schauen Sie sich den folgenden Quellcodeabschnitt an.
Was befindet sich am Ende in Variablen `arr`, `sl1` und `sl2`?
Was ist das zugrundeliegende Array von `sl1` und `sl2`?

```go
arr := [6]int{10, 20, 30, 40, 50, 60}
sl1 := arr[1:4]
sl2 := sl1[:cap(sl1)]  // Achtung: cap(sl1) != len(sl1)
sl2[3] = 99
```

<!-- time estimate: 20 min -->

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

<!-- time estimate: 15 min -->

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

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:
```go
[INCLUDE::include/go-slices-control-snippet.go]
```

[ER] Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen;
bitte ebenfalls zufügen:

```go
func main() {
    testAppend()
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
`testAppend`:
ist die Ausgabe für `cap(s)` gleich, so müssen auch Adressen von `&s` übereinstimmen.

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
