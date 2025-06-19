title: Weitere Grundlagen von Go
stage: draft
timevalue: 3.5
difficulty: 2
assumes: go-basics1, go-basics2
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datenstrukturen in Go definieren.
[ENDSECTION]

[SECTION::background::default]
TODO_Brandes
[ENDSECTION]

[SECTION::instructions::detailed]
Wie im Teil 1 und 2 gilt weiter:
Dokumentation zur Programmiersprache finden Sie in der
[Go Spec](https://go.dev/ref/spec)
für definitive (Referenz-)Information und im
[Go User Manual](https://go.dev/doc/),
wenn Sie eher Anleitungscharakter suchen.


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

Methoden sind Funktionen, die einem Typ zugeordnet sind und einen bestimmten ersten Parameter besitzen:
den Empfänger (receiver).
Sie ermöglichen es, Verhalten zu Strukturen hinzuzufügen.

```go
func (p Person) Print() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der Empfänger: `p` ist der Name, über welchen die Methode auf die Struktur selbst zugreifen kann.

Der Empfängertyp muss im gleichen Paket deklariert werden.
Daher können Methoden nicht auf eingebauten Typen wie int oder string definiert werden.


### Struktureinbettung (struct embedding)

TODO_Brandes: Studis selber nachlesen schicken

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


[ER] Definieren Sie eine neue Struktur: `Employee`.
Diese soll alle Felder und Methoden einer `Person` übernehmen und ein neues Feld definieren: `Position`.

[ER] Implementieren Sie eine neue Methode `Print` auf `Employee`, die nicht nur
den vollständigen Namen auf die Kommandozeile ausgibt, sondern auch die `Position`.

[ER] Fügen Sie die folgende Funktion in Ihre Quellcodedatei ein und rufen Sie diese aus der `main`-Funktion auf:

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

TODO_Brandes: etwas zu Structs-pointers Interaktion, wahrscheinlich unter "Methoden" oder Ergänzung zur pass-by-reference

### "Pass-by-value" und "Pass-by-reference"

TODO_Brandes: betonen, dass es erst ab ~10mb großen Structs einen Unterschied macht

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

Eigentlich müsste der zweite Aufruf `p` dereferenzieren: `fmt.Println((*p).Age)`, aber
Go führt diese Umwandlung automatisch durch und vereinfacht damit den Zugriff auf Felder von Zeigern.

[ER] Implementieren Sie eine Methode `Promote` auf `Employee`, die ein Argument `newPosition string`
erwartet.
Sie soll die Struktur modifizieren und das Feld `Position` auf den neuen Wert setzen.

[ER] Kopieren Sie die folgende Testfunktion in Ihre Datei um und rufen Sie sie ebenfalls aus der `main`-Funktion auf:

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


[SECTION::submission::information,trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

[ENDINSTRUCTOR]
