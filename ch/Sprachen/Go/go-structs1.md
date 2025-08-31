title: Weitere Grundlagen von Go — Strukturen (Teil 1)
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich kann komplexere Datentypen in Go definieren.
[ENDSECTION]

[SECTION::background::default]
Je größer Ihre Projekte werden, desto mehr Struktur und Organisation braucht
Ihr Quellcode.
Go ist keine objektorientierte Programmiersprache: Im Gegensatz zu Java oder Python
gibt es keine Klassen, Objekte oder Vererbung.
Stattdessen wird in Go mit __Strukturen__ (structs) gearbeitet —
mit zusammengesetzten Datentypen.

In dieser Aufgabe handelt es sich um Strukturen, Methoden und Struktureinbettung.
[ENDSECTION]


[SECTION::instructions::detailed]

### Struktur (Definition)

Eine Struktur (struct) ist eine Zusammensetzung von primitiven Datentypen oder
anderen Strukturen.

Strukturen bestehen aus _Feldern_, die jeweils einen Namen und einen festen Typ haben:

```go
type Person struct {
    FirstName string
    LastName  string
    Age       int
}
```

Lese- und Schreibzugriff auf die Felder einer Struktur erfolgt mithilfe von `.`:

```go
// volle Schreibweise
p := Person{FirstName: "Max", LastName: "Mustermann", Age: 25}

// kurze Schreibweise, Reihenfolge der Argumente bestimmt die Zuordnung
p := Person{"Max", "Mustermann", 25}

// Initialisierung mit Nullwerten: 
p := Person{}               // äquivalent zu Person{"", "", 0}

fmt.Println(p.FirstName)    // Max
p.FirstName = "Eric"
```

[NOTICE]
Alle Felder dieser Struktur sind großgeschrieben und deswegen öffentlich
(public/exported).
[ENDNOTICE]


### Methoden

Auch ohne Klassen gibt es **Methoden** in Go.

Methoden sind Funktionen, die einem Typ zugeordnet sind und einen bestimmten
ersten Parameter besitzen: den Empfänger (receiver).
Sie ermöglichen es, Verhalten zu Strukturen hinzuzufügen.

```go
func (p Person) Print() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der Empfänger: `p` ist der Name, über welchen die Methode
auf die Struktur selbst zugreifen kann.

[ER] Definieren Sie eine Struktur `Circle`, die ein Feld `radius float64` besitzt.

[ER] Implementieren Sie zwei Methoden auf `Circle`:

- `Circumference() float64` — Kreisumfang berechnen;
- `Area() float64` — Fläche berechnen;
- benutzen Sie `math.Pi` für Kreiszahl Pi.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-structs-methods-control-snippet.go]
```

<!-- time estimate: 20 min -->


### Struktureinbettung (struct embedding)

Lesen Sie diesen
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/)
.

[ER] Definieren Sie eine Struktur `Employee`.
Diese soll alle Felder und Methoden einer `Person` übernehmen und ein neues
Feld definieren: `Position string`.

[ER] Implementieren Sie eine neue Methode `Print` auf `Person`, die den
vollständigen Namen und das Alter auf die Kommandozeile ausgibt.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-structs-embedding-control-snippet.go]
```

[NOTICE]
Da `Person` in `Employee` eingebettet wurde, können Sie auf alle Felder und
Methoden von `Person` explizit über `e.Person.` zugreifen.
[ENDNOTICE]

[EQ] Stellen Sie sich vor, dass es eine neue Methode `Print` auf `Employee`
definiert wurde.
Wie ändert sich die Ausgabe von der Testfunktion?

[HINT::Verdeckung (Shadowing)]
Lesen Sie den Abschnitt "Shadowing of embedded fields" in dem
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/)
.

In dem Fall verhalten sich Methoden sehr ähnlich wie Felder.
[ENDHINT]


[ER] Stellen Sie sicher, dass Ihre `main`-Funktion genauso aussieht:

```go
func main() {
    testMethods()
    testStructs()
}
```

[EC] Führen Sie nun das Programm mittels `go run` aus.

<!-- time estimate: 20 min -->


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**
[PROT::ALT:go-structs1.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-structs1.go]
[ENDINSTRUCTOR]
