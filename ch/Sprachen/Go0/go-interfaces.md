title: Go Interfaces
stage: alpha
timevalue: 3.5
difficulty: 2
assumes: go-basics1, go-basics2, go-basics3
---

[SECTION::goal::idea,experience]

Ich verstehe, was Interfaces in Go sind, welchem Zweck sie dienen, wie sie implementiert und angewendet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist ein Interface?

In Golang ist ein Interface eine Menge an Funktionssignaturen. 
Ein Typ **implementiert** ein Interface, wenn dieser Typ
Methoden hat, die den vorausgesetzten Signaturen entsprechen.

Alle Interfaces in Go sind **implizit**: Sobald die nötigen Methoden implementiert sind, ist auch das ganze Interface
implementiert. 
Das Interface muss nicht namentlich erwähnt werden und es wird kein `implements`-Schlüsselwort vorausgesetzt.


### Beispiel
 
Wir definieren hier ein Interface `Speaker`, der aus einer Methode besteht: `Speak() string`:

```go
type Speaker interface {
    Speak() string
}
```

Und nun ein paar Haustiere: Strukturen `Cat` und `Dog`. 
Diese zwei Typen sollen die `Speak()` Methode implementieren und werden dadurch automatisch zu `Speaker`n.
Dann ist anschließend folgendes möglich:

```go
speakers := []Speaker{Cat{}, Dog{}}

for _, speaker := range speakers {
    fmt.Println(speaker.Speak())
}

```

Ausgabe:

```
Meow!
Woof!
```

[ER] Definieren Sie zwei Strukturen, `Cat` und `Dog`.
Implementieren Sie für jede Struktur das Interface `Speaker`, sodass der Programmausschnitt oben die erwartete Ausgabe produziert.


### Wichtige Standard-Interfaces

#### Stringer

Das eingebaute `Stringer`-Interface sorgt dafür, dass ein Typ korrekt als `string` dargestellt wird. 
Das Interface verlangt nur eine Methode `String() string` .

[ER] Implementieren Sie das Interface `Stringer` für einen neuen Typ `MyString`: 

1. Definieren Sie eine Struktur `MyString` (nicht zu verwechseln mit dem eingebauten Datentyp `string`) 
   mit zwei Feldern: `value string` und `lastByteRead int`.
2. Definieren Sie eine Konstruktor-Methode `NewString() *MyString`.
3. Implementieren Sie das `Stringer`-Interface, sodass Funktionen wie `fmt.Println()` nicht die ganze Struktur im 
   Terminal ausgeben, sondern nur das `value`.

Ein weiteres Beispiel können Sie sich hier anschauen: [A Tour Of Go](https://go.dev/tour/methods/17).

Die [Dokumentation](https://pkg.go.dev/fmt#Stringer) kann ebenfalls hilfreich sein.


#### Reader

Das eingebaute Interface `Reader` besteht aus einer einzigen Methode: `Read(p []byte) (n int, err error)`. 
Diese muss den Inhalt der implementierenden Struktur in den bereitgestellten Puffer/Slice `p` auslesen 
und gibt zwei Werte zurück: 
Die Anzahl der in diesem Aufruf von `Read` ausgelesenen Bytes und einen `error`, 
falls das Auslesen nicht weiter möglich ist.

[ER] Implementieren Sie das Interface `Reader` für `MyString`:

1. Implementieren Sie die `Read` Methode auf der `MyString` Struktur.
    - solange es etwas auszulesen gibt, wird dies ausgelesen;
    - sobald das Ende erreicht wurde, ein `(n, fmt.Errorf("EOF"))` Paar zurückgeben.
2. Testen Sie Ihre Implementierung mittels des klassischen gepufferten Auslesens:
    - einen Puffer definieren (beispielsweise der Größe 4);
    - in einer Endlosschleife die `Read(buf)` Methode aufrufen und nach jeder Iteration den Inhalt im Terminal ausgeben,
      bis ein `error` auftaucht.

Ein Referenzbeispiel: [A Tour Of Go](https://go.dev/tour/methods/21).

Die [Dokumentation](https://pkg.go.dev/io#Reader) von `io.Reader` könnte für die Implementierung von `Read()` nützlich sein. 


#### Writer

Das Interface `Writer` besteht ebenfalls aus einer Methode: `Write(p []byte) (n int, err error)`. Diese ermöglicht das
Schreiben aus dem Slice `p` in die Struktur und gibt die Anzahl von den geschriebenen Bytes und den Fehler zurück, falls etwas schiefgegangen
ist.

[ER] Implementieren Sie auch das `Writer`-Interface.

1. Implementieren Sie die `Write` Methode auf der `MyString` Struktur. Diese soll den übergebenen Puffer als `string` an
   die bereits vorhandene Zeichenkette (`value`) aufhängen.
2. Testen Sie Ihre Implementierung, indem Sie einen `MyString` erzeugen und eine beliebige Nachricht per `Write`
   in diesen `MyString` schreiben.

`io.Writer`: [Dokumentation](https://pkg.go.dev/io#Writer)

[NOTICE]

**Was ist der Zweck?**

Die Implementierung der `Reader`- und `Writer`-Methoden mag auf den ersten Blick wie eine reine Übungsaufgabe wirken — in der Tat legt sie aber das Fundament für fortgeschrittene Go-Programmierung.

In späteren Aufgaben werden Sie intensiv mit Dateisystem und Netzwerkkommunikation arbeiten, wo die `Reader`- und `Writer`-Interfaces eine zentrale Rolle spielen. 
Durch die Erstellung eigener `Reader`-`Writer`-Strukturen erwerben Sie zwei entscheidende Fähigkeiten:

- ein deutlich besseres Verständnis von der I/O-Methoden der Standardbibliothek, da Sie deren zugrundeliegende Mechanismen selbst implementiert haben;
- Sie können I/O-Operationen eleganter abstrahieren — das führt zu kompakterem Code und erhöht gleichzeitig die Lesbarkeit Ihrer Programme.
   
[ENDNOTICE]


#### Error

Das Interface `Error` verlangt nur die `Error() string` Methode. Wie können wir das ausnutzen?

Stellen Sie sich vor, Sie wollen eine Menge von verschiedenen `Error`-Strukturen haben, die jeweils gewisse nützliche 
Daten beinhalten: 
Beispielsweise hat ein `HTTPError` einen `statusCode`, 
ein `FileError` einen `reason`, warum die Operation fehlgeschlagen ist (Zugriff nicht gestattet / Datei existiert nicht / etc). 
Dieses Spektrum können wir mithilfe des `Error`-Interfaces abbilden.

[WARNING]

Dieses Beispiel ist nur für Lernzwecke ausgedacht. 
Es darf kein echtes Szenario geben, wo `FileError`s neben `HTTPError`s behandelt werden sollen.

[ENDWARNING]

[ER] Das Interface `Error` zweimal implementieren:

1. Definieren Sie eine Struktur `HTTPError` mit einem Feld `statusCode int`.
2. Implementieren Sie das `Error`-Interface. Der `statusCode` muss in der Fehlermeldung erwähnt werden.
3. Definieren Sie eine Struktur `FileError` mit einem Feld `reason string`.
4. Implementieren Sie das `Error`-Interface. Der `reason` muss in der Fehlermeldung erwähnt werden.

Referenzen:

- Ein Beispiel in [A Tour Of Go](https://go.dev/tour/methods/19)
- Eine ausführlichere Erklärung, was ein `error` ist und wie er benutzt wird: [Exercism](https://exercism.org/tracks/go/concepts/errors)


### Interfaceeinbettung

Genauso wie Strukturen dürfen Interfaces miteinander kombiniert werden.

```go
type Car interface {
    Accelerate()
    Decelerate()
}

type ElectricCar interface {
    Car
    Charge()
}
```

Dementsprechend muss ein `ElectricCar` ebenfalls Methoden `Accelerate()` und `Decelerate()` implementieren.

[Hier](https://eli.thegreenplace.net/2020/embedding-in-go-part-2-interfaces-in-interfaces/) finden Sie ein paar weitere Beispiele.


### Das leere Interface

Was ist, wenn der Typ einer Variable erst zur Laufzeit bestimmt werden kann?
An dieser Stelle kommt das leere Interface ins Spiel.

Schauen Sie sich folgende Funktion an:

```go
func HandleSomething(v interface{}) {
    switch v := v.(type) {
    case int: fmt.Println("it's an int", v)
    case bool: fmt.Println("it's a bool", v)
    case string: fmt.Println("it's a string", v)
    default: fmt.Printf("it's a %T\n", v)         // %T gibt den automatisch bestimmten Typ von 'v' aus
    }
}
```

Diese Funktion erhält einen Parameter vom Typ `interface{}` und bestimmt in einem [Type Switch](https://go.dev/doc/effective_go#type_switch) dynamisch den konkreten Typ. 
Aber warum funktioniert das überhaupt?

Das leere Interface definiert keine Methoden-Anforderungen. 
Da jeder Typ in Go automatisch Null Methoden erfüllt, wird dieses Interface von jedem Typ implementiert. 
Das ist Gos Antwort auf `Object` in Java oder `void*` in C.

Das leere Interface: [A Tour Of Go](https://go.dev/tour/methods/14).

[ER] Informieren Sie sich über Type Switch und Type Assertion: [Effective Go](https://go.dev/doc/effective_go#interface_conversions).

[ER] Implementieren Sie eine Funktion `HandleSpeaker(s Speaker)`.
Diese soll einen Parameter vom Typ `Speaker` annehmen und mithilfe von Type Switch oder Type Assertion erkennen, ob der `Speaker` ein `Cat` oder ein `Dog` ist.
Je nachdem, was für ein `Speaker` erkannt wurde, soll die Funktion eine informative Meldung auf die Kommandozeile ausgeben.

[SECTION::submission::trace,program]

Geben Sie den Quellcode in einer ausführbaren Datei `interfaces.go` ab. 
Diese muss folgendes beinhalten:

* `type Speaker interface`
* `type Cat struct`
    * `(c Cat) Speak() string`
* `type Dog struct`
    * `(d Dog) Speak() string`
* `type MyString struct`
* `NewString() *MyString`
* `(s *MyString) Read(p []byte) (n int, err error)`
* `(s *MyString) Write(p []byte) (n int, err error)`
* `(s *MyString) String() string`
* `type FileError struct` 
    * `(e FileError) Error() string`
* `type HTTPError struct` mit `Error()`
    * `(e HTTPError) Error() string`
* `HandleSpeaker(s Speaker)`

[ER] Fügen Sie den folgenden Codeausschnitt ihrem Programm hinzu.
Falls Sie die Funktion `main` bereits benutzt haben, ersetzten Sie den Inhalt durch diesen aus dem Ausschnitt.
Den folgenden Code dürfen Sie nicht ändern!

```go
[INCLUDE::snippets/go-interfaces-control-snippet.go]
```

[EC] `go run interfaces.go`

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Korrekturhinweise]

1. Die Test-Methoden müssen in der abgegebenen Quellcode-Datei unverändert bleiben;
2. Sanity-Check, ob die Funktionen in der Tat das tun, was sie tun sollen und nicht nur das abdecken, was getestet wird.

Quellcode siehe unter [TREEREF::go-interfaces.go]

Kommandoprotokoll: [PROT::ALT:go-interfaces.prot]

[ENDINSTRUCTOR]
