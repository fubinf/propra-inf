title: Weitere Grundlagen von Go
stage: alpha
timevalue: 3.5
difficulty: 2
explains: Slice (Golang)
assumes: go-basics-i
---

[SECTION::goal::idea,experience]

Ich habe mich mit den weiteren Konzepten von Go auseinandergesetzt und kann nun:

- Funktionen definieren;
- komplexere Datenstrukturen kreieren;
- Zeiger und Referenztypen effektiv benutzen;

[ENDSECTION]

[SECTION::background::default]

In dieser Aufgabe lernen Sie weitere wichtige Konstrukte in der Programmiersprache Go. 
Zusammen mit [PARTREF::go-basics-i] ergibt dies eine solide Grundlage, mithilfe deren Sie interessantere/komplexere Programme implementieren können.
Insbesondere geht es in dieser Aufgabe um das Zusammenspiel von Funktionen und Zeiger, welches zum einen zu der Laufzeiteffizienz der Programmiersprache beiträgt 
und zum anderen mehr Kontrolle für die Entwickler_innen zur Verfügung stellt.

[ENDSECTION]

[SECTION::instructions::detailed]

### Funktionen

Jede Funktion in Go besteht aus folgenden Teilen:

* `func` Schlüsselwort;
* Funktionsname (optional!);
* Runde Klammern für die Parameter: Parameter werden nacheinander als Paare `name type` aufgelistet;
* Signatur der Rückgabe:
    * leer, wenn die Funktion nichts zurückgibt;
    * `T`, wenn die Funktion einen Wert von Typ `T` zurückgibt;
    * ein Tupel `(T1, T2, ..., Tn)`, falls die Funktion mehrere Werte auf einmal zurückgibt;
    * oder ein benanntes Tupel `(t1 T1, t2 T2, ..., tn Tn)`, falls die Rückgabewerte direkt in der Funktionssignatur deklariert werden sollen;
* Funktionsrumpf in geschweiften Klammern.

Eine Funktion, die Sie bereits kennen, ist die `main`-Funktion:

```go
func main() {
    ...
}
```

Weitere Beispiele:

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

// anonyme/"lambda" Funktion, 
// die in-place definiert ist und mit zwei Zahlen aufgerufen wird
func(x int, y int) {
    return x * y
}(4, 5)
```


#### Benannte Rückgabewerte

Eine weitere Möglichkeit, Werte aus der Funktion zurückzugeben, sind die benannten Rückgabewerte.

Benannte Rückgabewerte sind immer mit den Standard-/Default-Werten initialisiert.

```go
// Die Variablen i und err sind bereits mit (0, nil) initialisiert
func namedReturn() (i int, err error) {
    i = 42
    err = nil
    // Hier werden alle Variablen automatisch zurückgegeben, die in der Funktionssignatur initialisiert wurden
    return
}

func namedReturn() (i int, err error) {
    // Das ist auch valide 
    return 42, nil
}

func normalReturn() (int, error) {
    // Die Variablen i und err müssen hier initialisiert werden
    var (
        i   int   = 42
        err error = nil
    )
    // Und explizit zurückgegeben werden
    return i, err
}
```

Es empfiehlt sich, benannte Rückgabewerte erst dann zu benutzen, wenn die Funktion ausreichend groß ist und/oder Dokumentation benötigt.
Einerseits tragen die Parameternamen in der Rückgabesignatur zur Lesbarkeit bei; andererseits können leere `return`-Anweisungen verwirrend wirken.


#### Variadische Funktionen

Funktionen in Go können eine dynamische Anzahl von Parametern verarbeiten, was besonders nützlich ist, wenn die genaue Anzahl der Argumente zur Kompilierungszeit nicht bekannt ist. 
Dafür gibt es eine spezielle Schreibweise, die als variadische Parameter bezeichnet wird:

```go
func receiveInts(xs ...int) {
    for i, v := range xs {
        ...
    }
}
```

Das ist äquivalent zur Verwendung eines Slice als Parameter:

```go
func receiveInts(xs []int) {
    for index, value := range xs {
        ...
    }
}
```

Für den Aufrufer gibt es jedoch einen Unterschied:

```go
// Variadisch
receiveInts(0, 1, 4, 9, 16, 25, 36, 49, 64)

// Slice
receiveInts([]int{0, 1, 4, 9, 16, 25, 36, 49, 64})

```


#### Funktionen höherer Ordnung

Eine Funktion kann eine andere Funktion als Parameter erhalten, wodurch sie zu einer Funktion höherer Ordnung wird:

```go
func apply(
    arg int, 
    operation func(int) int,
) int {
    return operation(arg)
}
```

Diese Funktion nimmt zwei Parameter an: eine Zahl und eine Funktion, die ebenfalls eine Zahl übergeben bekommt und zurückgibt. 
`operation` ist der Name der Funktion, und `func(int) int` ist ihre Signatur ("sie nimmt eine Zahl an und gibt eine Zahl zurück").

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

Oder man könnte die Funktion zuerst in einer Variable speichern (das ist zwar möglich, aber eher unkonventionell):

```go
func main() {
    square := func(i int) int { return i * i }
    squared := apply(4, square)
}
```

Funktionen höherer Ordnung sind nützlich für die Erstellung flexibler und wiederverwendbarer Codebausteine.


#### Ausprobieren

- [ER] Implementieren Sie eine Funktion `divide(a, b float64) (result float64, err error)`:
  die erste Zahl durch die zweite dividieren.
  Bei Erfolg ein Tupel `(result, nil)` zurückgeben; ansonsten `(0.0, fmt.Errorf("division by zero"))`.
  Benutzen Sie hier benannte Rückgabewerte.
- [ER] Bauen Sie `reduce(initialValue int, operation func(int, int) int, xs ...int) int` — eine Funktion, die 
  eine Funktion (`operation`) und eine beliebige Anzahl von Ganzzahlen als Parameter bekommt.
  Sie wendet sukzessive `operation` auf die Ganzzahlen an:
  Der erste Parameter von `operation` ist eine Akku-Variable (anfangs `start`, am Ende das Resultat), 
  der zweite der Reihe nach jedes Element der Liste `xs`.
  Mit `reduce(0, func(acc, arg int) int { return acc + arg }, 1, 2, 3, 4)` kann beispielsweise 
  die Summe der Ganzzahlen berechnet werden.
- [ER] Fügen Sie die folgende Funktion in Ihre Quellcodedatei ein und rufen Sie diese aus der `main`-Funktion auf:

```go
func testFunctions() {
    fmt.Println(divide(5, 2))
    fmt.Println(divide(5, 0))
    fmt.Println(
        reduce(
            0,
            func(acc, arg int) int { return acc + arg * arg }, 
            2, 3, 5, 7, 11, 13, 17, 19,
        ),
    )
}
```


### Strukturen (structs)

Eine Struktur (struct) ist eine Zusammensetzung von primitiven Datentypen oder anderen Strukturen.
Da es in Go keine Klassen gibt, werden für die Kapselung Strukturen benutzt:

```go
type Person struct {
    FirstName string
    LastName  string
    Age       int
}
```

[NOTICE]

Alle Felder dieser Struktur sind großgeschrieben und deswegen öffentlich (public/exported).

[ENDNOTICE]


### Methoden

Auch ohne Klassen gibt es **Methoden** in Go. 

Methoden sind Funktionen, die einem Typ zugeordnet sind und einen zusätzlichen Parameter besitzen: den Empfänger (receiver). 
Sie ermöglichen es, Verhalten zu Strukturen hinzuzufügen.

```go
func (p Person) Print() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der Empfänger: `p` ist der Name, über welchen die Methode auf die Struktur selbst zugreifen kann.

[NOTICE]

Der Empfängertyp muss im gleichen Paket deklariert werden. 
Daher können Methoden nicht auf eingebauten Typen wie int oder string definiert werden.

[ENDNOTICE]


### Struktureinbettung (struct embedding)

Eines der Prinzipien von Go ist "Composition over Inheritance". 
Struktureinbettung ermöglicht die Komposition von Datenstrukturen und fördert die Wiederverwendbarkeit des Codes.

```go
type Student struct {
    Person
    University string
    Major      string 
}
```

In diesem Beispiel übernimmt Student alle Felder von Person. 
Beim Zugriff auf die Felder von Person gibt es mehrere Möglichkeiten — entweder direkt über den Namen eines Feldes oder
zuerst über die eingebettete Struktur:

```go
mark := Student{
    Person: Person{
        FirstName: "Mark",
        LastName:  "Mustermann",
        Age:       25,
    },
    University: "FU Berlin",
    Major:      "Computer Science",
}

fmt.Println(mark.Major)      // Computer Science
fmt.Println(mark.Person.Age) // 25
fmt.Println(mark.Age)        // 25
fmt.Println(mark.Person)     // {Mark Mustermann 25}
```

Dies erhöht die Wiederverwendbarkeit des Quellcodes und die Erweiterbarkeit der Funktionalität einer solchen Struktur. 
Im obigen Beispiel kann ein Student alles tun, was eine Person kann:

```go
// Diese Ausdrücke sind äquivalent
mark.Person.Print()
mark.Print()
```


#### Ausprobieren

- [ER] Definieren Sie eine neue Struktur: `Employee`. 
       Diese soll alle Felder und Methoden einer `Person` übernehmen und ein neues Feld definieren: `Position`.
- [ER] Implementieren Sie eine neue Methode `Print` auf `Employee`, die nicht nur 
  den vollständigen Namen auf die Kommandozeile ausgibt, sondern auch die `Position`.
- [ER] Fügen Sie die folgende Funktion in Ihre Quellcodedatei ein und rufen Sie diese aus der `main`-Funktion auf:

```go
func testStructs() {
    e := Employee{
        Person: Person{
            FirstName: "Mark",
            LastName: "Mustermann",
            Age: 25,
        },
        Position: "Accountant",
    }
    
    e.Print()
    e.Person.Print()
}
```


### Zeiger (pointers)

Zeiger sind ein grundlegendes Konzept in der Programmierung, das es ermöglicht, per Speicheradresse
auf Daten zuzugreifen. 
Sie sind nützlich, um effizient mit großen Datenstrukturen zu arbeiten oder Werte durch Referenz anstatt durch Kopie zu übergeben.

Zeiger in Go ähneln denjenigen in C oder C++ mit einem wichtigen Unterschied — sie sind sicherer zu benutzen.
Sie unterstützen keine [Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm) und gehören zu einem konkreten Typ 
(`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).

Ein Zeiger wird mithilfe des `&`-Operators erstellt. 
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` heißt "Adresse von `x`".

Die Umkehroperation heißt Dereferenzierung — ein Zeiger wird in den "Wert an der Adresse `x`" umgewandelt.
Dies geschieht mithilfe des Operators `*`, der sowohl zum Deklarieren eines Zeigertyps als auch 
zur Dereferenzierung verwendet wird.

Beispiel:

```go
content := 10               // int
box := &content             // *int

*box = 42                   // die Box "öffnen" und den Inhalt ersetzen
fmt.Println(content)        // 42
```

In diesem Beispiel zeigt `box` auf die Adresse von `content`. 
Durch Dereferenzierung kann der Wert an dieser Adresse geändert werden.


### "Pass-by-value" und "Pass-by-reference"

Wie werden Argumente in eine Funktion übergeben?

In Go werden alle Argumente an Funktionen per Wert übergeben, also kopiert. 
Das gilt sowohl für primitive Datentypen als auch für Strukturen.

Daraus ergeben sich folgende Nachteile:

* eine Funktion kann die ursprünglichen Argumente nicht verändern (was manchmal gewünscht wäre);
* jeder Funktionsaufruf kopiert alle Argumente — je größer die Argumente, desto ineffizienter wird der Aufruf. 

Lösung: Statt eine Struktur zu kopieren, übergeben wir einen Zeiger auf diese Struktur, um per Referenz zu arbeiten.

```go
// Schlecht - jeder Aufruf benötigt eine Kopie von "Person"
func printAge(p Person) {
    fmt.Println(p.Age)
}

// Gut - jeder Aufruf benutzt eine Referenz auf die Hauptstruktur
func printAge(p *Person) {
    fmt.Println(p.Age)
}
```

[NOTICE]

Eigentlich müsste der zweite Aufruf `p` dereferenzieren: `fmt.Println((*p).Age)`.

Das ist jedoch nicht nötig, da Go eine solche Umwandlung automatisch durchführt und den Zugriff auf Felder von Zeigern vereinfacht.

[ENDNOTICE]


#### Ausprobieren

- [ER] Implementieren Sie eine Methode auf `Employee` — `Promote(newPosition string)`. 
       Diese soll die ursprüngliche Struktur modifizieren und das Feld `Position` auf den neuen Wert setzen.
- [ER] Kopieren Sie die folgende Testfunktion in Ihre Datei um und rufen Sie sie ebenfalls aus der `main`-Funktion auf:

```go
func testMutation() {
    e := Employee{
        Person: Person{
            FirstName: "Mark",
            LastName: "Mustermann",
            Age: 25,
        },
        Position: "Accountant",
    }
    
    e.Print()
    e.Promote("Senior Accountant")
    e.Print()
}
```


### Referenz- und Werttypen

Mit _Referenztypen_ werden in der Regel die Typen gemeint, welche sich wie ein Zeiger (Pointer) verhalten.
Das bedeutet unter anderem:

- deren Standardwert ist `nil`
- sie enthalten intern Zeiger auf Daten
- "pass-by-reference"-Verhalten

_Werttypen_ sind anders: Sie stellen wirklich die Werte dar, sie sind **die Daten selbst**.
Primitive Datentypen (Zahlen, boolesche Werte und Zeichenketten) sind Werttypen.

Alle Werttypen teilen sich folgende Eigenschaften:

- deren Standardwert ist nicht `nil`
- "pass-by-value"-Verhalten — beim Zuweisen oder Übergeben als Parameter wird eine Kopie erstellt
- Vergleichbarkeit — zwei Variablen von einem Werttyp dürfen mittels `==` sinnvoll verglichen werden

Nun betrachten wir Arrays, Slices und Maps detaillierter aus der Perspektive von Wert- und Referenztypen.


### Array

Ein Array ist ein Werttyp, der eine Sammlung von Einträgen darstellt, wo alle Einträge zum gleichen Typ gehören und die Größe fest ist.

```go
var arr [5]int                      // arr == [0 0 0 0 0]
anotherArr := arr                   // eine Kopie wurde erstellt
anoterArr[0] = 42
fmt.Println(arr, anotherArr)        // [0 0 0 0 0] [42 0 0 0 0]
```

Reine Arrays werden in Go relativ selten verwendet, daher konzentrieren wir uns auf Slices.


### Slice

Slices bauen immer auf Arrays auf. 
Ein [TERMREF::Slice (Golang)] ist eine "View" bzw. eine Sicht in das zugrundeliegende Array, und ist somit ein Referenztyp.

Das ist die Laufzeitdarstellung eines Slice (`go/src/runtime/slice.go`):

```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

* `array` — das zugrundeliegende Array beziehungsweise ein Verweis auf die Speicherstelle, wo sich das Array befindet;
* `len` — die Anzahl von Elementen in dem Slice. 
  Diese Zahl ist immer zwischen 0 und der Größe des zugrundeliegenden Arrays und kann 
  mittels der eingebauten Funktion [`len()`](https://pkg.go.dev/builtin#len) ermittelt werden;
* `cap` — die Anzahl von Elementen, die der Slice maximal beinhalten kann (Capacity/Kapazität). 
  Diese Zahl wird von der eingebauten Funktion [`cap()`](https://pkg.go.dev/builtin#cap) zurückgegeben und stellt die Anzahl von Zellen 
  bis zum Ende des zugrundeliegenden Arrays dar.

Ein oder mehrere Elemente in einen Slice einfügen: [append.](https://pkg.go.dev/builtin#append)

Slices können entweder eigenständig erstellt werden oder als eine Sicht in ein existierendes Array:

```go
sl := make([]int, 4)            // Typ und initiale Größe eines Slice

sl := []int{0, 1, 2, 3, 4}      // direkter Slice mit Werten

arr := [5]int{0, 1, 2, 3, 4}    // existierendes Array

sl := arr[1:3]                  // der erste Index ist inklusiv, der zweite Index ist exklusiv
fmt.Println(len(sl))            // Länge: 2
fmt.Println(cap(sl))            // Kapazität: 4, denn Element 0 des Arrays ist nicht für den Slice verfügbar

fmt.Println(sl)                 // [1 2]
fmt.Println(sl[0])              // 1
fmt.Println(sl[1])              // 2
sl[0] = 8                       // das verändert das Array arr!
fmt.Println(arr)                // [0 8 2 3 4]
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

[NOTICE]

Wie bereits erwähnt, können Slices mithilfe von der Funktion `make([]T, initialSize)` kreiert werden. 
Das zugrundeliegende Array wird dann automatisch erstellt und hat exakt die Größe von `initialSize`.

Ein solcher Slice verhält sich im Wesentlichen wie ein dynamisches Array: 
Sobald es versucht wird, zu einem vollen Slice der Größe _n_ ein anderes Element hinzuzufügen, wird ein neues Array der Größe _2n_ allokiert.

[ENDNOTICE]


### Map

Eine Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre Schlüssel ermöglicht. 

Eine Map ist ein Referenztyp und wird ebenfalls mithilfe der Funktion `make()` erstellt:

```go
m := make(map[string]int)       // "string" ist der Typ der Schlüssel, "int" ist der Typ der Werte
m["one"] = 1
fmt.Println(m)                  // map[one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist, wenn kein solcher Schlüssel existiert
fmt.Println(len(m))             // 1
```

Um zu überprüfen, ob ein Schlüssel bereits vorhanden ist, wird die folgende Schreibweise verwendet:

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

Falls es keinen solchen Schlüssel gibt, führt `delete()` keine Aktion aus.

[WARNING]

Variablen von allen Referenztypen werden mit `nil` initialisiert:

```go
var s []int                     // s == nil
var m map[string]int            // m == nil
```

Es ist robuster, Slices und Maps direkt während der Deklaration mit `make()` zu initialisieren:

```go
s := make([]int, 0)
m := make(map[string]int)
```

[ENDWARNING]


### Programmieren

Implementieren Sie die folgenden Funktionen:

* [ER] `func AddElement(slice []int, element, at int)` — ein Element an einem Index `at` in einen Slice einfügen;
  das Element, das vorher an dieser Stelle stand und alle nachfolgenden rücken eine Position nach rechts;
* [ER] `func RemoveElement(slice []int, at int)` — ein Element an einem Index `at` entfernen und die Größe des Slice entsprechen anpassen.
* [ER] `func AddElementIfNotThere(m map[string]int, key string, value int)` — ein Schlüssel-Wert-Paar einfügen, falls der Schlüssel noch nicht benutzt wurde.

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]

Korrektur von `testFunctions()`, `testStructs()` und `testMutation()` — die Funktionen müssen unverändert in dem abgegebenen Quellcode präsent sein.

Korrektur von `AddElement`, `RemoveElement`: 
Der Punkt ist, dass Studierende Slices erstellen und modifizieren können.

Korrektur von `AddElementIfNotThere`: `delete()` muss benutzt werden.

[PROT::ALT:go-basics-ii.prot]

[ENDINSTRUCTOR]
