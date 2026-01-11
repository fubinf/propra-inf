title: "Grundlagen von Go: Strukturen (Teil 1)"
stage: beta
timevalue: 1
difficulty: 2
assumes: go-functions
---

[SECTION::goal::idea,experience]
Ich kann zusammengesetzte Datentypen in Go definieren.
[ENDSECTION]


[SECTION::background::default]
Go ist keine objektorientierte Programmiersprache: Es gibt keine Vererbung.
Sehr wohl gibt es aber so etwas wie Klassen und Methoden, allerdings sind die Bezeichnungen
und die Notation anders:
In Go wird mit __Strukturen__ (structs) gearbeitet, also mit zusammengesetzten Datentypen.
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
Alle Felder dieser Struktur haben Namen, die mit Großbuchstaben beginnen.
Solche Felder sind öffentlich (public/exported).

Felder mit Kleinbuchstaben sind hingegen privat, also nur im selben Paket zugreifbar.
<!-- TODO_Brandes: go-modules referenzieren, sobald die Aufgabe in beta ist -->
[ENDNOTICE]


### Methoden

Methoden sind Funktionen, die einem Typ zugeordnet sind;
meist (aber nicht immer) einem `struct`-Typ.
Ihre Deklaration erfolgt nicht im `struct`, sondern außerhalb.
Die Syntax ist eine erweiterte Form der Syntax für Funktionen:

```go
func (p Person) Print() {
    fmt.Println(p.FirstName, p.LastName)
}
```

Hier ist `(p Person)` der sogenannte Empfänger (receiver) und
`p` ist der Name, über welchen die Methode auf die Struktur zugreifen kann.
In Python lautet dieser Name konventionellerweise stets `self`, 
in Go wird meist der Anfangsbuchstabe des Typnamens benutzt
(oder ein anderer, sehr kurzer Name, der sich an den Typnamen anlehnt).

[ER] Definieren Sie eine Struktur `Circle`, die ein Feld `radius float64` besitzt.

[ER] Implementieren Sie zwei Methoden auf `Circle`:

- `Circumference() float64` — Kreisumfang berechnen;
- `Area() float64` — Fläche berechnen;
- benutzen Sie `math.Pi` für die Kreiszahl Pi.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-structs-methods-control-snippet.go]
```

<!-- time estimate: 10 min -->


### Struktureinbettung (struct embedding)

Holen Sie sich aus diesem
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/)
das Wissen, um die nachfolgenden Implementierungsschritte zu lösen.

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

[EQ] Stellen Sie sich vor, dass eine neue Methode `Print` auf `Employee`
definiert wurde.
Wie ändert sich die Ausgabe der Testfunktion?

[HINT::Ich bin verwirrt]
Lesen Sie den Abschnitt "Shadowing of embedded fields" in dem
[Artikel über Struktureinbettung](https://eli.thegreenplace.net/2020/embedding-in-go-part-1-structs-in-structs/).  
Das gilt für Methoden ganz ähnlich wie für Felder.
[ENDHINT]


[ER] Stellen Sie sicher, dass Ihre `main`-Funktion genau so aussieht:

```go
func main() {
    testMethods()
    testEmbedding()
}
```

[EC] Führen Sie nun das Programm mittels `go run` aus.

<!-- time estimate: 15 min -->
[ENDSECTION]


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

Musterlösung der Programmieraufgabe als ausführbare Datei hier: 
[TREEREF::/Sprachen/Go/go-structs1.go].
[ENDINSTRUCTOR]
