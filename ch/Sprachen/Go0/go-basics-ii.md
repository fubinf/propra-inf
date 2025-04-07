title: Weitere Grundlagen von Go
stage: alpha
timevalue: 3.5
difficulty: 2
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
* Funktionsname (optional);
* Runde Klammern für die Parameter: Parameter werden nacheinander als Paare `name type` aufgelistet;
* Signatur der Rückgabe:
    * leer, wenn die Funktion nichts zurückgibt;
    * `T`, wenn die Funktion einen Wert von Typ `T` zurückgibt;
    * ein Tupel `(T1, T2, ..., Tn)`, falls die Funktion mehrere Werte auf einmal zurückgibt;
* Funktionsdefinition beziehungsweise _-Body_ in geschweiften Klammern.

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

[FOLDOUT::Benannte Rückgabewerte]

Eine weitere Möglichkeit, Werte aus der Funktion zurückzugeben, sind die benannten Rückgabewerte.

```go
// Die Variablen i und err sind bereits mit entsprechenden Nullwerten initialisiert
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

[ENDFOLDOUT]

[FOLDOUT::Variadische Funktionen]

Funktionen in Go können eine dynamische Anzahl von Parametern verarbeiten, was besonders nützlich ist, wenn die genaue Anzahl der Argumente zur Kompilierungszeit nicht bekannt ist. 
Dafür gibt es eine spezielle Schreibweise, die als variadische Parameter bezeichnet wird:

```go
func receiveInts(xs ...int) {
    for i, v := range xs {
        ...
    }
}
```

Das ist äquivalent zur Verwendung eines Slices als Parameter:
```go
func receiveInts(xs []int) {
    for i, v := range xs {
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
 
[ENDFOLDOUT]

[FOLDOUT::Funktionen höherer Ordnung]

Eine Funktion kann eine andere Funktion als Parameter erhalten, wodurch sie zu einer höheren Ordnungsfunktion wird:

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

Höhere Ordnungsfunktionen sind nützlich für die Erstellung flexibler und wiederverwendbarer Codebausteine.

[ENDFOLDOUT]

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
func (p Person) PrintName() {
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
Beim Zugriff auf die Felder von Person gibt es mehrere Möglichkeiten — entweder direkt über den Namen eines Feldes oder zuerst über die eingebettete Struktur:

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
mark.Person.PrintName()
mark.PrintName()
```

### Zeiger (pointers)

Zeiger sind ein grundlegendes Konzept in der Programmierung, das es ermöglicht, auf die Speicheradresse eines Wertes zuzugreifen. 
Sie sind nützlich, um effizient mit großen Datenstrukturen zu arbeiten oder Werte durch Referenz anstatt durch Kopie zu übergeben.

Zeiger in Go ähneln denjenigen in C oder C++ mit einem wichtigen Unterschied — sie sind sicherer zu benutzen.
Sie unterstützen keine [Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm) und gehören zu einem konkreten Typ (`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).

Ein Zeiger wird mithilfe von `&` Operator erstellt. 
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` — "Adresse von `x`".

Die Umkehroperation heißt Dereferenzierung — ein Zeiger wird in den Wert "an der Adresse `x`" umgewandelt.
Dies geschieht mithilfe des Operators `*`, der sowohl zum Deklarieren eines Zeigertyps als auch zur Dereferenzierung verwendet wird.

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

In Go werden alle Argumente an Funktionen standardmäßig per Wert übergeben, also kopiert. 
Das gilt sowohl für primitive Datentypen als auch für Strukturen.

Daraus ergeben sich folgende Nachteile:

* eine Funktion kann die ursprünglichen Argumente nicht verändern (was manchmal gewünscht ist);
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

### Referenztypen

Zu den Referenztypen gehören Slices und Maps.

Zugrundeliegende Datenstruktur von Slices ist ein Array — eine Sammlung von Einträgen, wo alle Einträge zum gleichen Typ gehören und die Größe fest ist.

Arrays werden in Go selten direkt verwendet, daher konzentrieren wir uns auf Slices.

### Slice

Slices bauen immer auf Arrays auf. Ein Slice ist eine "View" bzw. eine Sicht in das zugrundeliegende Array.

Das ist die Laufzeitdarstellung eines Slices (`go/src/runtime/slice.go`):
```go
type slice struct {
    array unsafe.Pointer
    len   int
    cap   int
}
```

* `array` — das zugrundeliegende Array beziehungsweise ein Verweis auf die Speicherstelle, wo sich das Array befindet;
* `len` — die Anzahl von Elementen in dem Slice. 
  Diese Zahl ist immer zwischen 0 und der Größe des zugrundeliegenden Arrays und kann mittels der eingebauten Funktion [`len()`](https://pkg.go.dev/builtin#len) ermittelt werden;
* `cap` — die Anzahl von Elementen, die der Slice maximal beinhalten kann (Capacity/Kapazität). 
  Diese Zahl wird von der eingebauten Funktion [`cap()`](https://pkg.go.dev/builtin#cap) zurückgegeben und stellt die Anzahl von Zellen bis zum Ende des zugrundeliegenden Arrays dar.

Ein oder mehrere Elemente in einen Slice einfügen: [append.](https://pkg.go.dev/builtin#append)

Slices können entweder eigenständig erstellt werden oder als eine Sicht in ein existierendes Array:

```go
sl := make([]int, 4)            // Typ und initiale Größe eines Slices

sl := []int{0, 1, 2, 3, 4}      // direkter Slice mit Werten

arr := [5]int{0, 1, 2, 3, 4}    // existierendes Array

sl := arr[1:3]                  // der erste Index ist inklusiv, der zweite Index ist exklusiv
fmt.Println(len(sl))            // Länge: 2
fmt.Println(cap(sl))            // Kapazität: 4

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
                                // ermöglicht das Hinzufügen neuer Elemente aufgrund höherer Kapazität
sl = append(sl, 8)              // überschreibt jedoch die "3" im ursprünglichen Array!
```

### Map

Ein Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre Schlüssel ermöglicht. 

Ein Map wird mithilfe von `make()` Funktion erstellt:

```go
m := make(map[string]int)       // "string" ist der Typ der Schlüssel, "int" ist der Typ der Werte
m["one"] = 1
fmt.Println(m)                  // map[one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist, wenn kein solcher Schlüssel existiert
fmt.Println(len(m))             // 1
```

Um zu überprüfen, ob ein Schlüssel bereits vorhanden ist, verwenden Sie folgende Schreibweise:

```go
mysteriousMap := make(map[string]int)

if value, isThere := mysteriousMap["key"]; isThere {
    // do something
} else {
    // "key" does not exist in the map and the value should not be used
}
```

Sie können ein Schlüssel-Wert-Paar explizit entfernen:

```go
mysteriousMap := make(map[string]error)

mysteriousMap["foo"] = nil

if value, isThere := mysteriousMap["foo"]; isThere && value == nil {
    delete(mysteriousMap, "foo")
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
* [ER] `func RemoveElement(slice []int, at int)` — ein Element an einem Index `at` entfernen und die Größe des Slices entsprechen anpassen.
* [ER] `func AddElementIfNotThere(m map[string]int, key string, value int)` — ein Schlüssel-Wert-Paar einfügen, falls der Schlüssel noch nicht benutzt wurde.

#### Mini-Projekt: Todo-App

Hier implementieren Sie ein kleines Kommandozeilenprogramm, wo Notizen angelegt, als "erledigt" markiert und entfernt werden können.

Legen Sie dafür zwei Typen an:

```go
type Todo struct {
	msg    string
	isDone bool
}

type TodoManager struct {
	tasks []*Todo
}
```

Sie dürfen außerdem folgende Funktionen benutzen:

```go
// eine Zeile aus dem Terminal auslesen
func getLine() string {
	reader := bufio.NewReader(os.Stdin)
	inputRaw, err := reader.ReadString('\n')
	if err != nil {
		panic(err)
	}

	return strings.TrimSpace(inputRaw)
}

// formatiert die Zeichenkette: strike-through (durchgestrichen)
func strikethrough(msg string) string {
    return fmt.Sprintf("\x1b[9m%s\x1b[0m", msg)
}
```

Als ein Ausgangspunkt dürfen Sie folgende Methodensignaturen nehmen:
```go
func (tdm *TodoManager) Add(t *Todo)
func (tdm *TodoManager) ListTodos()
func (tdm *TodoManager) MarkAsDone(atIndex int)
func (tdm *TodoManager) RemoveClosedTodos()
```

Folgende Funktionalität muss Ihr Programm unterstützen:

```
commands:
  - '-n todo_message' to add a new one
  - '-d todo_index' to mark a todo as 'done'
  - '-rm' to remove all todos marked as 'done'
  - 'q' to quit the program
```

- [ER] Implementieren Sie nun das Programm.
       Sie dürfen dabei die drei Funktionen benutzen, die Sie oben definiert haben.

### Testen

[EC] starten Sie das Programm mittels `go run todo.go` und führen Sie folgende Aktionen durch:

- Hilfe ausgeben lassen: "-h";
- Todo hinzufügen: "-n feed the dog";
- Todo hinzufügen: "-n feed the cat";
- Todo hinzufügen: "-n go get groceries";
- "-rm";
- Das erste Todo als erledigt markieren: "-d 1";
- "-rm";
- Die restlichen Todos als erledigt markieren: "-d 2", "-d 1";
- "-rm";
- "-q".

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

Geben Sie Ihr Todo-Programm sowie die drei davor implementierten Funktionen (`AddElement`, `RemoveElement`, `AddElementIfNotThere`) in einer Datei ab. 

[ENDSECTION]

[INSTRUCTOR::Hinweise]

Korrektur von `AddElement`, `RemoveElement`: 
Der Punkt ist, dass Studierende Slices erstellen und modifizieren können.

Korrektur von `AddElementIfNotThere`: das `delete()` muss benutzt werden.

Korrektur von Todo-Manager: Muss funktionsfähig sein und ungefähr mit dem Kommandoprotokoll übereinstimmen.
Schöne Formatierung ist in dem Fall nur ein "nice-to-have".

[ENDINSTRUCTOR]
