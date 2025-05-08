title: Go Interfaces
stage: alpha
timevalue: 2.5
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich verstehe, was Interfaces in Go sind, wie sie implementiert und angewendet werden.

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

Und ein paar Haustiere: Strukturen `Cat` und `Dog`. 
Dadurch, dass diese zwei Typen die `Speak()` Methode implementieren, werden sie automatisch zu `Speaker`n.

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

Das `Stringer`-Interface sorgt dafür, dass ein Typ korrekt als `string` dargestellt wird. 
Das Interface verlangt nur eine Methode `String() string` .

[ER] Implementieren Sie das Interface `Stringer`: 

1. Definieren Sie eine Struktur `String` (nicht verwechseln mit dem eingebauten Datentyp `string`) mit zwei Feldern: `value string` und `lastByteRead int`.
2. Definieren Sie eine Konstruktor-Methode `NewString() *String`.
3. Implementieren Sie das `Stringer`-Interface, sodass Funktionen wie `fmt.Println()` nicht die ganze Struktur im 
   Terminal ausgeben, sondern nur das `value`.

#### Reader

Das Interface `Reader` besteht aus einer einzigen Methode: `Read(p []byte) (n int, err error)`. 
Diese muss den Inhalt in den bereitgestellten Puffer/Slice `p` auslesen und gibt zwei Werte zurück: 
Die Anzahl der in diesem Aufruf von `Read` ausgelesenen Bytes und einen `error`, 
falls das Auslesen nicht weiter möglich ist.

[ER] Implementieren Sie das Interface `Reader`:

1. Implementieren Sie die `Read` Methode auf der `String` Struktur.
    - solange es etwas auszulesen gibt, wird dies ausgelesen;
    - sobald das Ende erreicht wurde, ein `0, error` Paar zurückgeben.
2. Testen Sie Ihre Implementierung mittels des klassischen gepufferten Auslesens:
    - einen Puffer definieren (beispielsweise der Größe 4);
    - in einer Endlosschleife die `Read(buf)` Methode aufrufen und nach jeder Iteration den Inhalt im Terminal ausgeben,
      bis ein `error` auftaucht oder keine Bytes mehr ausgelesen werden.


#### Writer

`Writer` Interface besteht ebenfalls aus einer Methode: `Write(p []byte) (n int, err error)`. Diese ermöglicht das
Schreiben in die Struktur und gibt die Anzahl von geschriebenen Bytes und den Fehler zurück, falls etwas schiefgegangen
ist.

[ER] Implementieren Sie auch das `Writer`-Interface.

1. Implementieren Sie die `Write` Methode auf der `String` Struktur. Diese soll den übergebenen Puffer als `string` an
   die bereits vorhandene Zeichenkette (`value`) aufhängen.
2. Testen Sie Ihre Implementierung, indem Sie einen `String` kreieren und eine beliebige Nachricht über `Write` Methode
   in diesen `String` schreiben.

#### Error

Das Interface `Error` verlangt nur die `Error() string` Methode. Wie können wir das ausnutzen?

Stellen Sie sich vor, Sie wollen eine Menge von verschiedenen `Error`-Strukturen haben, die jeweils gewisse nützliche 
Daten beinhalten: 
Beispielsweise hat ein `HTTPError` einen `statusCode`, 
ein `FileError` einen `reason`, warum die Operation fehlgeschlagen ist (Zugriff nicht gestattet / Datei existiert nicht / etc). 
Diesen Fehlerraum können wir 
mithilfe von `Error`-Interface abbilden.

[WARNING]

Dieses Beispiel ist nur für Lernzwecke ausgedacht. Es darf kein echtes Szenario geben, wo `FileError`s neben 
`HTTPError`s behandelt werden sollen.

[ENDWARNING]

[ER] Das Interface `Error` implementieren:

1. Definieren Sie eine Struktur `HTTPError` mit einem Feld `statusCode int`.
2. Implementieren Sie das `Error`-Interface. Der `statusCode` muss in der Fehlermeldung erwähnt werden.
3. Definieren Sie eine Struktur `FileError` mit einem Feld `reason string`.
4. Implementieren Sie das `Error`-Interface. Der `reason` muss in der Fehlermeldung auch erwähnt werden.

#### Interfaceeinbettung

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

Beispiel: [ReadWriter](https://pkg.go.dev/io#ReadWriter)

#### Leeres Interface

Leeres Interface (`interface{}`) ist ein Interface, welches keine Methoden verlangt. Das bedeutet, dass alle Typen 
dieses eine Interface automatisch implementieren. Das ist das Go-Äquivalent von `Object` in Java oder `void*` in C.

So mächtig wie dieses Konstrukt auch ist, spielt es ein bisschen gegen die typ-sichere Natur von Go und impliziert mehr 
Typ-Checks zur Laufzeit, was zum einen direkt die Leistungsfähigkeit beeinflusst (mehr zu tun für das Programm), und zum 
anderen manche Compiler-Optimierungen unmöglich macht. 

Falls Sie den Hinweis oben noch nicht aufgeklappt haben, machen Sie das. Auf diese Art und Weise können Sie zur Laufzeit
bestimmen, was genau sich unter diesem `interface{}` versteckt, und entsprechend agieren.

[ER] Schreiben Sie eine Funktion `HandleSomething(v interface{}) string`, die folgende Datentypen erkennt und jeweils
verschiedene Zeichenketten zurückgibt:

- `string`;
- `int`;
- `bool`;
- für die anderen Typen dürfen Sie `fmt.Sprintf("%T\n", x)` zurückgeben (automatische Typerkennung).

[HINT::switch...]

Den unterliegenden Typ können Sie aus einem Interface mithilfe von dynamischem Casting bestimmen:

```go
switch e := err.(type) {
case A: // do stuff with A
case B: // do stuff with B
default: // do something
}
```

[ENDHINT]

[SECTION::submission::trace,program]

Geben Sie den Quellcode in einer `interfaces.go` Datei ab, welche mit `package interfaces` anfängt. Diese muss folgendes 
beinhalten:

* `type String`
* `NewString() *String`
* `(s *String) Read(p []byte) (n int, err error)`
* `(s *String) Write(p []byte) (n int, err error)`
* `(s *String) String() string`
* `type FileError` mit `Error()` 
* `type HTTPError` mit `Error()`
* `HandleSomething()`

Fügen Sie den folgenden Codeausschnitt ihrem Programm hinzu und führen Sie das Programm aus.
Falls Sie die Funktion `main` bereits benutzt haben, ersetzten Sie den Inhalt durch diesen aus dem Ausschnitt.
Den folgenden Code dürfen Sie nicht ändern!

```go
[INCLUDE::snippets/go-interfaces-control-snippet.go]
```

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Korrekturhinweise]

1. Die Test-Methoden müssen in der abgegebenen Quellcode-Datei unverändert bleiben;
2. Sanity-Check, ob die Funktionen in der Tat das tun, was sie tun sollen und nicht nur das abdecken, was getestet wird.

Quellcode siehe unter [TREEREF::go-interfaces.go]

Kommandoprotokoll:
[PROT::ALT:go-interfaces.prot]

[ENDINSTRUCTOR]
