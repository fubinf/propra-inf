title: Erweiterte Datentypen
stage: draft
timevalue: 1
difficulty: 2
assumes: go-ide, go-variables-and-primitives, go-functions, go-collections
---

[SECTION::goal::idea]
Ich kann Strukturen definieren und weiß, wie ich sie lesbar für die anderen halte.

[ENDSECTION]

[SECTION::background::default]
Früher oder später reichen die primitiven Datentypen nicht mehr aus. In dieser Aufgabe gehen wir auf die benutzerdefinierten Datentypen ein.

Zuerst werden Sie mit einer Menge nützlicher Information präsentiert und anschließend vereinfachen Sie einen Code-Abschnitt.
[ENDSECTION]

### Was ist eine Struktur?

Eine Struktur (__structure__ beziehungsweise `struct`) ist eine strukturierte Zusammensetzung von mehreren Feldern/Datentypen. Dies lässt sich sehr gut anhand eines Beispiels erklären und verstehen.

Sagen wir, wir brauchen eine Struktur, um eine/n Studierende/n darzustellen. Diese würde wahrscheinlich aus Namen, Matrikelnummer und E-Mail bestehen (es können noch weitere Informationen gespeichert werden, ist aber momentan irrelevant). In Go wird diese Struktur folgendermaßen deklariert:

```go
type Student struct {
    name            string
    matrikelnummer  string
    email           string
}
```

Diese Struktur beinhaltet drei Felder, jeweils von dem Datentypen `string`. 

### Wie wird eine Struktur benutzt?
```go
// kreiert eine leere Struktur, wo Felder mit Nullwerten definiert werden
emptyStudent := Student{}

// vollständig initialisierte Struktur
student := Student{"Max Mustermann", "0123456", "max.mustermann@fakemail.com"}

// vollständig initialisierte Struktur mit Feldernamen
fullyNamedStudent := Student{
    name: "Max Mustermann",
    matrikelnummer: "0123456", 
    email: "max.mustermann@fakemail.com",
}

// partiell initialisierte Struktur
// "matrikelnummer" und "email" sind aktuell leere Zeichenketten, ""
NamedStudent := Student{
    name: "Max Mustermann",
}
```

Wie greift man auf die einzelnen Felder zu? Das geschieht mittels der sogenannten dot-Syntax:
```go
fmt.Println(student.name)
student.name = "Max Mustermännchen"
```

[FOLDOUT::Beste Praxis]
Benutzen Sie immer die Feldernamen, wenn Sie eine Struktur initialisieren! Bei simpleren Strukturen kommt man wahrscheinlich auch ohne zurecht, aber das spart Ihnen das schmerzhafte Debugging in Zukunft. In größeren Strukturen verbessert dies enorm die Lesbarkeit. 

Beispiel:
```go
type User struct {
    ID        int
    Username  string
    Email     string
    Age       int
    IsActive  bool
    IsAdmin   bool
}
```

Ohne Feldernamen gegen mit Feldernamen:
```go
user := User{
    ID:        1,
    Username:  "johndoe",
    Email:     "john@example.com",
    Age:       25,
    IsActive:  true,
    IsAdmin:   false,
}

user := User{
    1,
    "johndoe",
    "john@example.com",
    25,
    true,
    false,
}

```
[ENDFOLDOUT]

### Einbettung einer Struktur (Struct embedding)

Struktureinbettung ist ein Konzept, welches uns die Komposition von Datentypen ermöglicht. Außerdem können wir so einige Datentypen wiederverwenden.

Stellen Sie sich vor, Sie modellieren ein Unternehmen. Dafür brauchen Sie einige Datenstrukturen, um Arbeitnehmer darstellen zu können (beispielsweise `Person`, `Employee`, und `Manager`). So würde die naive Lösung aussehen:

```go
type Person struct {
    name    string
    age     int
}

type Employee struct {
    name        string
    age         int
    jobTitle    string
    company     string
    salary      float64
}

type Manager struct {
    name        string
    age         int
    jobTitle    string
    company     string
    salary      float64
    team        string
    department  string
}
```

Ist das schön? Nein. Einbettung ist genau das, was uns das ständige Wiederholen spart:

```go
type Person struct {
    name    string
    age     int    
}

type Employee struct {
    Person              // alle Felder von "Person" werden in "Employee" übernommen
    jobTitle    string
    company     string
    salary      float64
}

type Manager struct {
    Employee            // alle Felder von "Employee" werden in "Manager" übernommen
    department  string
}
```

Dabei befinden sich die Felder auf derselben Tiefe in Hierarchie (ein `Manager` besitzt Felder `department`, `salary`, `age` usw).
```go
manager := Manager{
    Employee: Employee{
        Person: Person{
            name: "Max Mustermann",
            age:  25,
        },
        jobTitle: "manager",
        company:  "basf",
        salary:   1000,
    },
    department: "research",
}

fmt.Println(manager.name)           // gibt der Name des Managers aus
fmt.Println(manager.Employee.name)  // gibt der Name des Managers über "Employee" aus
fmt.Println(manager.Person.name)    // gibt der Name des Managers über "Person" aus
```

Aus diesem Beispiel könnte man die Schlüssfolgerung ziehen, dass `Employee` und `Person` als Felder von `Manager` gespeichert werden. Das ist falsch.

`Employee` und `Person` erlauben uns die Felder, die aus der entsprechenden Struktur eingebettet wurden, als eine Instanz dieser Struktur zu interpretieren. Dies trägt ebenfalls der Wiederverwendbarkeit bei.

### Methoden

Go unterstützt keine Klassen und Vererbung und ist in dem Sinne keine objektorientierte Sprache. Was man stattdessen nutzen kann, sind __Methoden__ -
Funktionen mit einem Empfänger-Argument (receiver argument). Dieser kann zwischen dem `func` Schlüsselwort und dem Funktionsnamen stehen:

```go
type Vector struct {
    x, y float64
}

func (v Vector) abs() float64 {
    return math.Sqrt(v.x*v.x + v.y*v.y)
}

...

v := Vector{x: 3, y: 4}
fmt.Println(v.abs())        // 5
```

`v` in der Funktionssignatur ist ähnlich wie `self` Schlüsselwort in Python.

[SECTION::submission::snippet]
### Aufgabe 1. Refactoring

Go ist eine geeignete Sprache, um verschiedene Services zu implementieren (später werden wir von Microservices reden). Das sind kleine Akteure, die jeweils für eine Aufgabe zuständig sind. Wir (als Entwickler) wollen jederzeit sicher sein, dass unser Service nach wie vor funktioniert und seine Aufgaben erledigt. So sehen unsere Strukturen aus:
```go
import "time"

type LoggingService struct {
    Name        string
    CreatedAt   time.Time
    IsRunning   bool
    LogLevel    string
    LogFilePath string
}

type TestService struct {
    Name        string
    CreatedAt   time.Time
    IsRunning   bool
    TestData    string
}

type MonitoredService struct {
    Name            string
    CreatedAt       time.Time
    IsRunning       bool
    LogLevel        string
    LogFilePath     string
    HealthCheckURL  string
    Metrics         map[string]float64
}
```

Überlegen Sie sich, wie man diese Struktur-Konstellation vereinfachen kann. Erstellen Sie sich dafür eine Datei namens `structs_abgabe.go` und kopieren Sie den oben angeführten Abschnitt in diese Datei. Geben Sie dann diese Datei ab, wenn Sie der Meinung sind, es kann nichts mehr verbessert werden.

[NOTICE]
Es kann am Ende mehr Strukturen geben als am Anfang.
[ENDNOTICE]

### Aufgabe 2. Geometrie
Stellen Sie folgende Figuren als Strukturen (structs) dar und implementieren Sie jeweils Methoden, die die Fläche und das Perimeter der Figur berechnen:

* Kreis
* Dreieck
* Rechteck

[ENDSECTION]

- [EQ] In welchen Situationen kann die Struktureinbettung nützlich sein?
- [EQ] Gibt es ähnliche Konzepte in anderer Programmiersprachen, die Sie kennen?

[INSTRUCTOR::Lösungen]
Strukturen vereinfachen:
```go
[INCLUDE::ALT:structs_abgabe.go]
```

Fragen:

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
