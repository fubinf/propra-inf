title: "Grundlagen von Go: Arrays and Slices"
stage: beta
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

[TOC]

[SECTION::instructions::detailed]

### Zwei Kategorien von Typen

In Go gibt es zwei Kategorien von Typen: _Einblocktypen_ und _Mehrblocktypen_.
Ein gutes Verständnis ihrer Eigenschaften sowie ihres Verhaltens als Funktionsparameter 
ist für das weitere Programmieren in Go unerlässlich.

[EQ] Benutzen Sie den Abschnitt "Two Categories of Go Types" im
[Artikel go101: Value Parts](https://go101.org/article/value-part.html)
um die Frage zu beantworten, was _Einblocktypen_ und _Mehrblocktypen_ sind.

[NOTICE]
Go ist eine _Pass-by-Value_-Programmiersprache — das bedeutet, dass Funktionsargumente
stets kopiert werden.

Bei den _Einblocktypen_ ist dieses Verhalten leicht nachvollziehbar: Der (einzige) Speicherblock
wird vollständig kopiert.

Bei den _Mehrblocktypen_ hingegen wird nur der direkte Teil (_direct part_) kopiert;
die _underlying parts_ gibt es hingegen weiterhin nur einmal und sie werden zwischen
dem Original des Werts und der Kopie geteilt.
Wenn man an diesen Daten etwas ändert, scheinen sich also sowohl das Original
als auch die Kopie zu ändern.
[ENDNOTICE]

<!-- time estimate: 10 min -->


### Array

Ein Array ist ein _Einblocktyp_, der eine Sammlung von Einträgen darstellt,
wo alle Einträge zum gleichen Typ gehören und die Größe (Anzahl von Einträgen) fest ist.

In Go wird eine __nullbasierte Nummerierung__ verwendet: Das erste Element
eines Arrays oder Slices hat den Index `0`, das zweite den Index `1` und so weiter. 

Schauen Sie sich das 
[Thema 'Arrays' in "A Tour of Go"](https://go.dev/tour/moretypes/6)
an und beantworten Sie die Fragen unten:

[EQ] Wie wird ein `int`-Array der Länge 5 __deklariert__?

[EQ] Wie wird ein `int`-Array der Länge 5 __definiert__ (also mit Werten befüllt)?

[EQ] Wie greift man per Index auf ein bestimmtes Element eines Arrays zu?

[EQ] Kann man in einer Variable vom Typ `[5]int` ein Array wie `{7, 8, 9, 10}` speichern?
_Begründen Sie Ihre Antwort._

[EQ] Was ist der Nullwert eines Arrays?

[EQ] Was passiert, wenn man ein bestehendes Array einer anderen Variable zuweist?
Entstehen dadurch zwei eigenständige Arrays oder eine gemeinsame Referenz?

[HINT::Ich weiß nicht, wie ich das überprüfen kann]
Fügen Sie nach Zeile 12 im A-Tour-of-Go-Beispiel folgende Zeile ein:

    primes2 := primes

Ändern Sie anschließend etwas an `primes`.

Wenn diese Änderung sich nicht in `primes2` widerspiegelt, handelt es sich um zwei eigenständige 
Arrays.
[ENDHINT]

[FOLDOUT::Die Anzahl der Elemente kann automatisch abgeleitet werden]
Dazu verwendet man die folgende Schreibweise:

```go
a := [...]int{0, 1, 2, 4, 5}
```

Der Compiler ermittelt die Anzahl der Elemente automatisch anhand der Initialisierung,
sodass keine manuelle Größenangabe erforderlich ist.
[ENDFOLDOUT]

<!-- time estimate: 15 min -->

### Slice

Ein [TERMREF::Slice (Golang)] ist eine flexible "View" bzw. eine Sicht in das zugrundeliegende 
Array und ist ein _Mehrblocktyp_.

Es gibt drei Möglichkeiten, einen Slice zu kreieren:

- als ein _Slice-Literal_;
- durch Deklaration;
- durch _Slicing_;
- mittels der eingebauten Funktion `make`.


#### Slice-Literal

Ein 
[Literal](https://de.wikipedia.org/wiki/Literal) 
bezeichnet allgemein einen festen Wert, der direkt im Quellcode geschrieben wird — also 
nicht berechnet oder aus einer Variable entnommen wird.

Schauen Sie sich dazu das 
[Thema 'Slice literals' in "A Tour of Go"](https://go.dev/tour/moretypes/9)
an.

[ER] Erstellen Sie einen `string`-Slice mit den Namen `Alice`, `Bob` und `Eva`.
Benutzen Sie die Literal-Schreibweise.

<!-- time estimate: 5 min -->


#### Deklaration

Der Nullwert eines Slices ist ebenfalls ein gültiger Slice — allerdings ohne das
zugrundeliegende Array:

```go
var s []int
fmt.Println(s)          // []
fmt.Println(s == nil)   // true
s = append(s, 42)
fmt.Println(s)          // [42]
```


#### Slicing

Ein Slice kann auch als eine "View" in ein vorhandenes Array erstellt werden.

Finden Sie in den folgenden verlinkten Abschnitten von "A Tour of Go" die entsprechenden 
Informationen:

- Wie ein Slice auf diese Weise initialisiert wird — siehe 
  [Thema "Slices"](https://go.dev/tour/moretypes/7);
- Was man bei der Slicing-Notation weglassen darf — siehe 
  [Thema "Slice defaults"](https://go.dev/tour/moretypes/10);
- Wie sich Änderungen am Slice auf das zugrundeliegende Array auswirken — siehe
  [Thema "Slices are like references to arrays"](https://go.dev/tour/moretypes/8);

[ER] Legen Sie ein Array `evenNumbers` mit 6 geraden Zahlen an.
Erzeugen Sie anschließend einen Slice `evenNumbersSlice`, der die ersten 4 Zahlen aus 
`evenNumbers` enthält.
Verwenden Sie dafür die Slicing-Notation.

[ER] Können Sie die Zuweisung `evenNumbersSlice := ...` noch kürzer schreiben?
(Selbst ein Zeichen weniger zählt!)

[EQ] Was passiert mit dem Array `evenNumbers`, wenn Sie ein Element in `evenNumbersSlice`
auf `42` setzen?

<!-- time estimate: 10 min -->


#### 'make'

Eine weitere Möglichkeit, einen Slice zu kreieren, ist die Funktion `make`:
`func make(t Type, size ...IntegerType) Type`.

[ER] Schauen Sie sich das 
[Thema 'Creating a slice with make' in "A Tour of Go"](https://go.dev/tour/moretypes/13)
an und erstellen Sie einen `int`-Slice mit initialer Größe 5.
Benutzen Sie dabei die Funktion `make`.
Befüllen Sie den Slice in einer `for`-Schleife mit ganzen Zahlen
von 0 bis 4 (inklusive).

<!-- time estimate: 5 min -->


#### Länge und Kapazität

Zwei sehr wichtige Attribute eines Slice sind seine _Länge_ und _Kapazität_.

Sie können mithilfe der eingebauten Funktionen 
[len()](https://pkg.go.dev/builtin#len)
und 
[cap()](https://pkg.go.dev/builtin#cap) 
entsprechend ermittelt werden.

Die __Länge__ eines Slice ist die Anzahl von Elementen in dem Slice.

Die __Kapazität__ eines Slice ist die Anzahl von "Speicherzellen" von Anfang des Slice 
bis zum Ende des zugrundeliegenden Arrays.

Lesen Sie den 
[Abschnitt 'Slice Internals'](https://go.dev/blog/slices-intro#slice-internals)
im Artikel "Go Slices: usage and internals" und vollziehen Sie nach, was der Zusammenhang 
zwischen der Länge, der Kapazität und dem zugrundeliegenden Array ist.

Sehen Sie sich ein praktisches Beispiel auf "A Tour of Go" an:
[Slice length and capacity](https://go.dev/tour/moretypes/11).
Achten Sie besonders darauf, wie sich die Länge eines Slice dynamisch verändern lässt.

[EQ] Ändern Sie die Zeile 14 im A-Tour-Of-Go-Beispiel zu

```go
s = s[:14]
```

Führen Sie das Programm aus.
Was ist passiert?
Warum?
Worauf muss man bei einer solchen Größenänderung achten?

[EQ] Was ist die _Kapazität_ des Slice `s`?

```go
arr := [5]int{7, 8, 9, 13, 14}
s := arr[2:]
```

[EQ] Was ist die _Kapazität_ des Slice `s`?
Was ist seine _Länge_?

```go
arr := [10]int{0, 4, 5, 3, 2, 7, 8, 9, 13, 14}
s := arr[2:6]
```

[EQ] Was ist die _Kapazität_ des Slice `s2`?
Was ist seine _Länge_?

```go
arr := [10]int{0, 4, 5, 3, 2, 7, 8, 9, 13, 14}
s := arr[2:6]
s2 := s[:0]
```

<!-- time estimate: 15 min -->

[NOTICE]
Es gibt eine besondere Schreibweise, mit der sich die Kapazität eines Slice 
explizit begrenzen lässt:

```go
s[start:end:max]
```

Dabei gibt `max` die obere (exklusive) Grenze der Indizes an, die der Slice intern nutzen darf.
Wenn `max = 4`, darf der Slice also nur bis einschließlich Index 3 reichen.

Die Kapazität des Slice beträgt in diesem Fall automatisch:

```go
cap(s) = max - start
```
[ENDNOTICE]


#### 'copy' und 'append'

Zwei weitere eingebaute Funktionen sind:

- `copy(dst, src []T) int` — kopiert Inhalte von `src` nach `dst` und gibt die Anzahl
  von erfolgreich kopierten Elementen zurück (immer `min(len(dst), len(src))`);
- `append(s []T, elems ...T) []T` — fügt die `elems` zum Slice `s` hinzu und gibt den neuen
  Slice zurück.

Ein gängiger Trick zum Zusammenfügen zweier Slices nutzt die sogenannte Variadic-Syntax 
(auch „Spread-Operator“ genannt):

```go
s1 := append(s1, s2...)
```

Der Ausdruck `s2...` bedeutet: Alle Elemente von `s2` werden __einzeln__ als Argumente 
an `append` übergeben — nicht als ein einzelner Slice.

[ER] Erstellen Sie einen Slice `primes` mit den ersten 5 Primzahlen.
Legen Sie einen zweiten Slice `primesCopy` mit Größe 10 an.
Kopieren Sie `primes` in `primesCopy`.
Wo landen die Werte im Ziel-Slice, wenn dieser mehr Platz hat als nötig?

<!-- time estimate: 5 min -->


#### Mehr Beispiele

Schauen Sie sich die zwei Beispiele _genau_ an; denken Sie mit.

Versuchen Sie zunächst selbst nachzuvollziehen, was in jeder Zeile passiert,
_bevor_ Sie die Kommentare lesen.

```go
// Beispiel 1
arr := [5]int{7, 9, 11, 13, 14}     // mit Werten initialisiertes Array der Länge 5
sl := arr[1:3]                      // slice mit Werten {9, 11} (denn der zweite Index ist exklusiv)

fmt.Println(len(sl))                // Länge: 2
fmt.Println(cap(sl))                // Kapazität: 4, denn Element 0 des Arrays ist nicht für den Slice verfügbar

fmt.Println(sl)                     // [9 11]
sl[0] = 8                           // das verändert das Array arr!
fmt.Println(arr)                    // [7 8 11 13 14]


// Beispiel 2
arr := [5]int{7, 9, 11, 13, 14}
sl := arr[:3]
sl = append(sl, 8)                  // das überschreibt die "13" im ursprünglichen Array arr!
fmt.Println(arr)                    // [7 9 11 8 14]
```

[EQ] Was geben die zwei `fmt.Println()`-Anweisungen jeweils aus?

```go
arr := [5]int{7, 9, 11, 13, 14}
sl := arr[0:2:2]
sl[0] = 42
sl = append(sl, 8)
fmt.Println(sl)
fmt.Println(arr)
```

[EQ] Was befindet sich am Ende in Variablen `arr`, `sl1` und `sl2`?
Was ist das zugrundeliegende Array von `sl1` und `sl2`?

```go
arr := [6]int{10, 20, 30, 40, 50, 60}
sl1 := arr[1:4]
sl2 := sl1[:cap(sl1)]
sl2[3] = 99
```

<!-- time estimate: 15 min -->


### Programmieren

Implementieren Sie die folgenden Funktionen:

[ER] `AddElement(slice []int, element, at int) []int`:
ein Element an einem Index `at` in einen Slice einfügen;
das Element, das vorher an dieser Stelle stand, und alle nachfolgenden rücken eine Position nach
rechts.
Wenn `at` kleiner als 0 ist, soll das Element am Anfang eingefügt werden.
Wenn `at` größer als der letzte Index von `slice` ist, soll das Element am Ende eingefügt werden.
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

<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::information,trace,snippet,program]
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
