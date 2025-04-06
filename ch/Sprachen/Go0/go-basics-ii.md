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

Weitere Beispiele
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
// Variablen i und err sind bereits mit entsprechenden Nullwerten initialisiert
func namedReturn() (i int, err error) {
    i = 42
    err = nil
    // hier werden alle Variablen automatisch zurückgegeben, die in der Funktionssignatur initialisiert wurden
    return
}

func namedReturn() (i int, err error) {
// das ist auch valide 
return 42, nil
}

func normalReturn() (int, error) {
    // Variablen i und err müssen hier initialisiert werden
    var (
        i   int   = 42
        err error = nil
    )
    // und explizit zurückgegeben werden
    return i, err
}
```

Es empfiehlt sich, die benannten Rückgabewerte erst dann zu benutzen, wenn die Funktion genügend groß ist und/oder Dokumentation braucht.
Einerseits tragen die Parameternamen in Rückgabesignatur zu der Lesbarkeit bei, andererseits können leere `return`-Anweisungen verwirrend wirken.

[ENDFOLDOUT]

[FOLDOUT::Variadische Funktionen]

Funktionen in Go dürfen eine dynamische Anzahl von Parametern bekommen.
Dafür gibt es eine besondere Schreibweise:

```go
func receiveInts(xs ...int) {
    for i, v := range xs {
        ...
    }
}
```

Das ist äquivalent zu der Slice-Schreibweise:
```go
func receiveInts(xs []int) {
    for i, v := range xs {
        ...
    }
}
```

Für den Aufrufer gibt es jedoch einen Unterschied:
```go
// variadisch
receiveInts(0, 1, 4, 9, 16, 25, 36, 49, 64)

// Slice
receiveInts([]int{0, 1, 4, 9, 16, 25, 36, 49, 64})

```
 
[ENDFOLDOUT]

[FOLDOUT::Funktionen höherer Ordnung]

Eine Funktion darf eine andere Funktion als Parameter bekommen:

```go
func apply(
    arg int, 
    operation func(int) int,
) int {
    return operation(arg)
}
```

Diese Funktion nimmt zwei Parameter an: Eine Zahl und eine Funktion, die ebenfalls eine Zahl übergeben bekommt und zurückgibt.
`operation` ist der Name der Funktion und `func(int) int` ist ihre Signatur ("sie nimmt eine Zahl an und gibt eine Zahl zurück").

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

Auch ohne Klassen gibt es **Methoden**. 

Methoden sind Funktionen, die einen zusätzlichen Parameter besitzen: den Empfänger (receiver).

```go
func (p Person) PrintName() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der Empfänger: `p` ist der Name, über welchen die Methode auf die Struktur selbst zugreifen kann.

[NOTICE]

Empfängertyp muss in dem gleichen Paket deklariert werden. Eine Methode auf `int` oder `string` ist daher nicht erlaubt.

[ENDNOTICE]

### Struktureinbettung (struct embedding)

Eins der Prinzipien von Go ist "Composition over Inheritance". 
Struktureinbettung ist die Komposition von Datenstrukturen.

```go
type Student struct {
    Person
    University string
    Major      string 
}
```

In dem Beispiel übernimmt `Student` alle Felder von `Person`.
Wenn wir auf die Felder von `Person` zugreifen wollen, gibt es mehrere Möglichkeiten — entweder direkt über den Namen eines Feldes anfragen oder zuerst über die eingebettete Struktur:

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

Dies erhöht Wiederverwendbarkeit des Quellcodes und Erweiterbarkeit der Funktionalität einer solchen Struktur: 
In dem Beispiel oben kann `Student` alles, was eine `Person` kann.

```go
// diese Ausdrücke sind äquivalent
mark.Person.PrintName()
mark.PrintName()
```


### Zeiger (pointers)

Rudimentär gesehen ist ein Zeiger die Adresse eines Wertes.

Zeiger in Go ähneln denjenigen in C oder C++ mit einem wichtigen Unterschied — sie sind sicherer zu benutzen.
Sie unterstützen keine [Zeigerarithmetik](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm) und gehören zu einem konkreten Typ (`*T`, falls der Zeiger eine Variable von Typ `T` referenziert).

Ein Zeiger wird mithilfe von `&` Operator erstellt. 
Semantisch kann dieser als "Adresse von" gelesen werden: `&x` — "Adresse von `x`".

Die Umkehroperation heißt Dereferenzierung — ein Zeiger wird zum Wert "an der Adresse `x`" umgewandelt.
Das passiert mithilfe von dem Operator `*`.

Beispiel:

```go
content := 10               // int
box := &content             // *int

*box = 42                   // die Box "öffnen" und den Inhalt ersetzen
fmt.Println(content)        // 42
```

### "Pass-by-value" und "Pass-by-reference"

Wie werden Argumente in eine Funktion übergeben?

Generell werden Argumente kopiert. 
Das gilt sowohl für primitive Datentypen als auch für Strukturen.

Daraus ergeben sich folgende Nachteile:

* eine Funktion darf keine Argumente verändern (manchmal ist das jedoch gewünscht);
* jeder Funktionsaufruf kopiert alle Argumente — je größer die Argumente, desto inperformanter. 

Lösung: Statt eine Struktur zu kopieren, übergeben wir einen Zeiger auf diese Struktur.

```go
// schlecht - jeder Aufruf braucht eine Kopie von "Person"
func printAge(p Person) {
    fmt.Println(p.Age)
}

// gut - jeder Aufruf benutzt eine Referenz auf die Hauptstruktur
func printAge(p *Person) {
    fmt.Println(p.Age)
}
```

[NOTICE]

Eigentlich müsste der zweite Aufruf `p` dereferenzieren: `fmt.Println((*p).Age)`.

Das ist jedoch nicht nötig, da Go eine solche Umwandlung automatisch durchführt.

[ENDNOTICE]

### Referenztypen

Zu den Referenztypen gehören Slices und Maps.

Zugrundeliegende Datenstruktur von Slices ist ein Array — eine Sammlung von Einträgen, wo alle Einträge zum gleichen Typ gehören und die Größe fest ist.

Arrays per se werden sehr selten benutzt, deswegen lassen wir sie hier außer Acht.

### Slice

Slices bauen immer auf Arrays auf. Ein Slice ist eine "View" bzw. eine Sicht in das zugrundeliegende Array.

Das ist die Laufzeit-Darstellung eines Slices (`go/src/runtime/slice.go`):
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

// oder
sl := []int{0, 1, 2, 3, 4}

// oder
arr := [5]int{0, 1, 2, 3, 4}

sl := arr[1:3]                  // erste Index ist inklusiv, zweite Index ist exklusiv
fmt.Println(len(sl))            // length: 2
fmt.Println(cap(sl))            // capacity: 4

fmt.Println(sl)                 // [1 2]
fmt.Println(sl[0])              // 1
fmt.Println(sl[1])              // 2
sl[0] = 8                       // wir verändern das Array arr!
fmt.Println(arr)                // [0 8 2 3 4]
```

Ein weiteres Beispiel:
```go
arr := [5]int{0, 1, 2, 3, 4}

sl := arr[:]                    // kreiert einen Slice, welcher das ganze ursprüngliche Array beinhaltet (len = 5, cap = 5)
sl := arr[2:]                   // kreiert einen Slice von Index 2 und bis zum Ende des Arrays (len = 3, cap = 3)
sl := arr[:3]                   // kreiert einen Slice von Anfang des Arrays bis zu der Index 3 (exklusiv) (len = 3, cap = 5)
                                // da cap > len ist, können wir relativ billig neue Elemente hinzufügen
sl = append(sl, 8)              // das überschreibt aber die "3" aus dem ursprünglichen Array!
```
### Map

Map ist eine Sammlung von Schlüssel-Wert-Paaren. 

Ein Map wird mithilfe von `make()` Funktion erstellt:

```go
m := make(map[string]int)       // "string" ist der Typ von Schlüsseln, "int" ist der Typ von Werten
m["one"] = 1
fmt.Println(m)                  // [one:1]
fmt.Println(m["two"])           // 0, da 0 der Nullwert von "int" ist
fmt.Println(len(m))             // 1
```

Um zu überprüfen, ob ein Schlüssel bereits da ist, gibt es die folgende Schreibweise:

```go
mysteriousMap := make(map[string]int)

if value, isThere := mysteriousMap["key"]; isThere {
    // do something
} else {
    // "key" is not used in the map and the value should not be used
}
```

Wir können ein Schlüssel-Wert-Paar explizit entfernen:

```go
mysteriousMap := make(map[string]error)

mysteriousMap["foo"] = nil

if value, isThere := mysteriousMap["foo"]; isThere && value == nil {
    delete(mysteriousMap, "foo")
}
```

Falls es keinen solchen Schlüssel gibt, macht `delete()` nichts.

[WARNING]

Variablen von allen Referenztypen werden mit `nil` initialisiert:

```go
var s []int                     // s == nil
var m map[string]int            // m == nil
```

Viel robuster ist es, Slices und Maps direkt während der Deklaration mithilfe von `make()` zu definieren:

```go
s := make([]int, 0)
m := make(map[string]int)
```

[ENDWARNING]

### Programmieren

Implementieren Sie folgende Funktionen:

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
