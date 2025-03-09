title: Go Interfaces
stage: alpha
timevalue: 1.5
difficulty: 2
requires: go-ide, go-variables-and-primitives, go-functions, go-structs
assumes: go-type-casting
---

[SECTION::goal::idea,experience]
Ich verstehe, was Interfaces in Go sind, wie sie implementiert und angewendet werden.

[ENDSECTION]

### Was ist ein Interface?

In Golang, ein Interface ist eine Menge an Funktionssignaturen. Ein Typ **implementiert** ein Interface, wenn dieser Typ
Methoden hat, die den vorausgesetzten Signaturen entsprechen.

Anders gesehen ist ein Interface eine Art Vereinbarung: Ein Typ "entsperrt" eine neue Funktionalität, indem er ein 
Interface implementiert.

Alle Interfaces in Go sind **implizit**: Sobald die nötigen Methoden implementiert sind, ist auch das ganze Interface
implementiert. Es wird kein `implements`-Schlüsselwort vorausgesetzt.

### Beispiel
 
Wir definieren hier ein Interface `Speaker`, der aus einer Methode besteht: `Speak() string`:

```go
type Speaker interface {
    Speak() string
}
```

Und ein paar Haustiere, die dieses Interface jeweils implementieren:

```go
type Dog struct {}

func (d Dog) Speak() string {
    return fmt.Sprintf("Woof!")
}

type Cat struct {}

func (c Cat) Speak() string {
    return fmt.Sprintf("Meow!")
}
```

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

### Wichtigsten Interfaces

#### Stringer

`Stringer` Interface sorgt dafür, dass ein Typ korrekt als `string` dargestellt wird. Das Interface verlangt nur eine
`String() string` Methode.

1. Definieren Sie eine Struktur `String` mit zwei Feldern: `value string` und `lastByteRead int`.
2. Definieren Sie eine Konstruktor-Methode `NewString() *String`.
3. Implementieren Sie das `Stringer`-Interface, sodass Funktionen wie `fmt.Println()` nicht die ganze Struktur im 
   Terminal ausgeben, sondern nur das `value`.

#### Reader

`Reader` Interface besteht aus einer einzigen Methode: `Read(p []byte) (n int, err error)`. Diese muss den Inhalt in den
bereitgestellten Puffer/Slice `p` auslesen und gibt zwei Werte zurück: Anzahl von den in diesem Aufruf von `Read`
ausgelesenen Bytes und einen `error`, falls das Auslesen nicht weiter möglich ist.

Implementieren Sie nun dieses Interface!

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

Implementieren Sie auch das `Writer` Interface.

1. Implementieren Sie die `Write` Methode auf der `String` Struktur. Diese soll den übergebenen Puffer als `string` an
   die bereits vorhandene Zeichenkette (`value`) aufhängen.
2. Testen Sie Ihre Implementierung, indem Sie einen `String` kreieren und eine beliebige Nachricht über `Write` Methode
   in diesen `String` schreiben.

#### Error

`Error` Interface verlangt nur die `Error() string` Methode. Wie können wir das ausnutzen?

Stellen Sie sich vor, Sie wollen eine Menge von verschiedenen `Error` Strukturen haben, die jeweils gewisse nützlichen 
Daten beinhalten: Beispielsweise hat ein `HTTPError` ein `statusCode`, ein `FileError` einen `reason`, warum die 
Operation fehlgeschlagen hat (Zugriff nicht gestattet / Datei existiert nicht / etc). Diesen Fehlerraum können wir 
mithilfe von `Error`-Interface abbilden.

[WARNING]

Dieses Beispiel ist nur für Lernzwecke ausgedacht. Es darf kein echtes Szenario geben, wo `FileError`s neben 
`HTTPError`s behandelt werden sollen.

[ENDWARNING]


1. Definieren Sie eine Struktur `HTTPError` mit einem Feld `statusCode int`.
2. Implementieren Sie das `Error`-Interface.
3. Definieren Sie eine Struktur `FileError` mit einem Feld `reason string`.
4. Implementieren Sie das `Error`-Interface.
5. Implementieren Sie eine Funktion `handleError(err error)`, die den unterliegenden Typ von dem `error` bestimmt und
   je nach Typ unterschiedliche Meldungen im Terminal ausgibt.

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

#### Leeres Interface

Leeres Interface (`interface{}`) ist ein Interface, welches keine Methoden verlangt. Das bedeutet, dass alle Typen 
dieses eine Interface automatisch implementieren. Das ist das Go-Äquivalent von `Object` in Java oder `void*` in C.

So mächtig wie dieses Konstrukt auch ist, spielt es ein bisschen gegen die typ-sichere Natur von Go und impliziert mehr 
Typ-Checks zur Laufzeit, was zum einen direkt die Leistungsfähigkeit beeinflusst (mehr zu tun für das Programm), und zum 
anderen manche Compiler-Optimierungen unmöglich macht. 

Falls Sie den Hinweis oben noch nicht aufgeklappt haben, machen Sie das. Auf diese Art und Weise können Sie zur Laufzeit
bestimmen, was genau sich unter diesem `interface{}` versteckt, und entsprechend agieren.

- [EQ] Wo ist Ihrer Meinung nach das Nutzen von `interface{}` sinnvoll?

Schreiben Sie eine Funktion `HandleSomething(v interface{}) string`, die folgende Datentypen erkennt und jeweils
verschiedene Zeichenketten zurückgibt:

- `string`;
- `int`;
- `bool`;
- alles andere soll zusammengefügt werden.

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Markdowndokument.md]

Geben Sie den Quellcode in einer `interfaces.go` Datei ab, welche mit `package interfaces` anfängt. Diese muss folgendes 
beinhalten:

* `type String`
* `NewString()`
* `Read()`
* `Write()`
* `String()`
* `type FileError` mit `Error()` 
* `type HTTPError` mit `Error()`
* `HandleError()`
* `HandleSomething()`

[ENDSECTION]

[INSTRUCTOR::Korrekturhinweise]

Es gibt einen Satz von Unit-Tests [TREEREF::interfaces_test/interfaces_test.go]. Das setzt natürlich voraus, dass Sie Go 
auf Ihrem System installiert haben.

Kopieren Sie das ganze `interfaces_test` Verzeichnis auf Ihren Rechner und legen Sie die Abgabe unter 
`interfaces_test/interfaces/interfaces.go` ab. Aus dem Root-Verzeichnis (`interfaces_test`) führen Sie nun `go test` 
aus.

Quellcode siehe unter [TREEREF::interfaces.go]


[ENDINSTRUCTOR]
