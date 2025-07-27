title: "Go-Kontrollfluss: defer, panic und recover"
stage: draft
timevalue: 1.5
difficulty: 2
---

https://go.dev/blog/defer-panic-and-recover
https://gobyexample.com/panic

[SECTION::goal::idea,experience]
Ich weiß, wo und wie die Go-Schlüsselwörter `defer`, `panic` und `recover` 
verwendet werden.
[ENDSECTION]

[SECTION::background::default]
Das Schlüsselwort `panic` ist Ihnen wahrscheinlich schon bekannt.

`panic` und `recover` stellen einen alternativen Kontrollfluss dar — _Panicking_.
Dieser erinnert an Exceptions aus Java oder Python, auch wenn mit einigen Unterschieden.

In dieser Aufgabe schauen wir uns diese Konstrukte genauer an und beantworten 
folgende Fragen:

* Wie funktioniert `defer`?
* Was genau ist _Panicking_?
* Wie soll `recover` benutzt werden, wenn überhaupt?
[ENDSECTION]

[SECTION::instructions::detailed]


### `defer`

Das Schlüsselwort `defer` schiebt einen Funktionsaufruf auf.

Der aufgeschobene Aufruf wird erst dann ausgeführt, wenn die umgebende Funktion
ihre Ausführung beendet — genau vor dem `return`.

Schauen Sie sich dieses Beispiel an:
['defer' on the Tour of Go](https://go.dev/tour/flowcontrol/12)
.

[EQ] Fügen Sie eine weitere `defer`-Anweisung in der interaktiven Umgebung von
"A Tour of Go".
Was können Sie über die Ausführungsreihenfolge von verschiedenen `defer`s sagen?

[FOLDOUT::größere Blöcke in einem `defer`?]
```go
defer func() {
   fmt.Println("first operation...") 
   fmt.Println("second operation...") 
   fmt.Println("third operation...") 
}()
```
[ENDFOLDOUT]

[EQ] Was wird auf die Kommandozeile ausgegeben beim Ausführen dieser Funktion? Warum?
```go
func testDefer() (s string) {
    defer fmt.Println(s)
    s = "done"
    return s
}
```

[HINT::Zurück zum "Tour of Go"...]
In dem Beispiel von "A Tour of Go" gab es diesen auf den ersten Blick kryptischen 
Kommentar:

_The deferred call's arguments are evaluated immediately, 
but the function call is not executed until the surrounding function returns._

Haben Sie nun eine Idee, was das zu bedeuten hat?
[ENDHINT]

Lesen Sie nun diesen kurzen Artikel: 
[Go by Example: defer](https://gobyexample.com/defer)
.

[EQ] Wofür wird `defer` meistens benutzt? 
Welche andere Anwendungen Fallen Ihnen ein? 


### `panic`

In [PARTREF::go-interfaces] haben Sie das Interface `error` kennengelernt.

Go-Fehlerbehandlung erfolgt nach dem Prinzip "Errors as Values" 
(beziehungsweise "Fehler als Werte"):
Alle Funktionen, wo etwas schiefgehen kann, haben nach Konvention einen 
zusätzlichen Rückgabewert vom Typ `error`.
Im glücklichen Fall ist der Wert `nil`, ansonsten der tatsächlich aufgetretene `error`:

```go
func parseInt(s string) (i int, err error) {
    ...
}
```

Ein anderer Mechanismus ist das **Panicking**:
Wenn eine `panic` in einer Funktion auftritt, wird die normale Ausführung dieser 
Funktion unterbrochen. 
Gleich im Anschluss werden alle `defer`-Anweisungen ausgeführt und die `panic` 
wird nach oben im Call-Stack propagiert.

Dies wiederholt sich, bis die `panic` irgendwo abgefangen wird oder bis alle 
Funktionen (`main`-Funktion inklusive) unterbrochen wurden — dann spricht man 
von einer vorzeitigen Beendung des Programms oder von einem _Crash_.

Überfliegen Sie diesen Artikel:
[When is it OK to panic in Go?](https://www.alexedwards.net/blog/when-is-it-ok-to-panic-in-go)
.

[NOTICE]
An sich ist `panic` nur eine Funktion, die einen beliebigen Wert annimmt:
[Dokumentation von `panic`](https://pkg.go.dev/builtin#panic)
.

Alle Funktionen, die selbst `panic()` aufrufen, sollen nach Konvention mit `must`
anfangen und müssen keinen `error` zurückgeben.
Die Idee ist, dass die Operation erfolgreich sein **muss** — wenn das schiefgeht, 
ergibt weitere Ausführung keinen Sinn und das komplette Programm darf abstürzen.
[ENDNOTICE]

[EQ] Wann würde der Autor des Artikels `panic` der normalen Fehlerbehandlung bevorzugen?

[ER] Implementieren Sie eine Funktion `mustGetInt64FromConsole() int64`.
Diese soll:

- eine ganze Zahl aus der Kommandozeile auslesen und als `int64` zurückgeben;
- `panic(err)` aufrufen, falls `res, err := strconv.ParseInt()` einen `error` zurückgibt;
- ansonsten `res` zurückgeben.

Das Ergebnis von `mustGetInt64FromConsole()` wird in der `main`-Funktion auf die 
Kommandozeile ausgegeben.

[HINT::aus der Kommandozeile auslesen...]
Schauen Sie hier nach, wie das funktioniert: 
[Reading in Console Input in Go](https://tutorialedge.net/golang/reading-console-input-golang/)
.

Es macht keinen Unterschied, ob Sie `bufio.Reader` oder `bufio.Scanner` benutzen.
[ENDHINT]

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "42" ein.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "hello" ein.


### `recover`

In der Erklärung von `panic` wurde angesprochen, dass sie abgefangen werden kann.
Wie?

`recover()` ist die Funktion dafür: 
[Dokumentation von `recover`](https://pkg.go.dev/builtin#recover)
.

Ein Aufruf von `recover()` bricht _das Panicking_ ab und stellt die normale 
Programmausführung wieder her.
Der Rückgabewert ist dann der Wert, mit dem _das Panicking_ gestartet wurde.

Hier sind die Schritte, wie das Abfangen einer `panic` abläuft:

1. `panic` ist aufgetreten
2. alle `defer`-Anweisungen werden ausgeführt
3. ein Aufruf `recover()`, um den normalen Kontrollfluss wiederherzustellen,
   den Fehler zu analysieren und die Rückgabewerte entsprechend zu modifizieren.

Schauen Sie sich 
[ein Beispiel von `recover` auf "Go by Example"](https://gobyexample.com/recover)
an. 

[NOTICE]
Ein Aufruf von `recover()` ist nur in `defer`-Anweisungen sinnvoll.

Während normaler Ausführung (nicht im `panic`-Modus) hat die Funktion nichts zu 
unterbrechen und gibt `nil` zurück.
[ENDNOTICE]

[EQ] Welcher der zwei Code-Ausschnitte fängt die `panic` ab? Warum?
```go
// Option 1
func someFunctionWithPanicInside() {
    defer recover()
    ...
}
```

```go
// Option 2
func someFunctionWithPanicInside() {
    defer func() {
        recover()        
    }()
    ...
}
```

[HINT::Zurück zum "Tour of Go"...]
Hier geht es wieder um 
[den kryptischen Kommentar](https://go.dev/tour/flowcontrol/12)
aus dem "Tour of Go":

_The deferred call's arguments are evaluated immediately, but..._
[ENDHINT]

[ER] Passen Sie die Funktion `mustGetInt64FromConsole` an:

- benennen Sie diese in `getInt64FromConsole` um;
- fügen Sie einen neuen Rückgabewert vom Typ `error` hinzu;
- fangen Sie die `panic` ab: 
    - setzen Sie den `error`-Rückgabewert auf den Rückgabewert von `recover`;
    - die Typumwandlung von `any` zu `error` überwinden Sie mittels 
      `fmt.Errorf("%v", someAny)`;
    - **benannte Rückgabewerte** helfen dabei, Rückgabewerte aus `defer`-Anweisungen
      zu modifizieren;
- Überprüfen Sie in der `main`-Funktion, ob `getInt64FromConsole` einen `error`
  zurückgegeben hat.
  Falls ja, geben Sie ihn auf die Kommandozeile aus.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "42" ein.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "hello" ein.

[ER] Passen Sie die Funktion `getInt64FromConsole` nochmal an:
Entfernen Sie den ganzen `defer`-Block und den Aufruf `panic(err)`.
Anstatt der `panic` soll an der Stelle das Paar `0, err` zurückgegeben werden.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "42" ein.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "hello" ein.

[EQ] Nun haben Sie zwei Mechanismen von Fehlerbehandlung gesehen: das Panicking 
und "Fehler als Werte".
Diskutieren Sie folgende Aspekte der zwei Ansätze:

- Lesbarkeit
- Testbarkeit
- Benutzerfreundlichkeit

Was ist Ihre Meinung zum
[Go Sprichwort](https://go-proverbs.github.io/)
"don't panic"?

[FOLDOUT::lohnt es sich überhaupt?]
Eines der Prinzipien von Go ist Simplizität.

Die in dieser Aufgabe vorgestellten `defer recover`-Ansätze sind zwar für
bestimmte Situationen angemessen, aber in den meisten Fällen unnötig.

Falls Sie sich dabei ertappen, eine solche Konstruktion zu schreiben,
überdenken Sie diese nochmals.
Befinden Sie sich wirklich in einer dieser besonderen Situationen, oder
können das System, die Schnittstelle oder die Funktion besser gestaltet werden?
[ENDFOLDOUT]

[FOLDOUT::weitere Quellen]
[The Go Blog: Defer, Panic, and Recover](https://go.dev/blog/defer-panic-and-recover)

[The Go Programming Language Specification: Defer statements](https://go.dev/ref/spec#Defer_statements)

[The Go Programming Language Specification: Handling panics](https://go.dev/ref/spec#Handling_panics)
[ENDFOLDOUT]
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

Alle Fragen in dieser Aufgabe sind als Lernfragen gedacht.
Der Zweck ist es, dass Studierende darüber nachdenken und eventuell eigene
Schlussfolgerungen ziehen.
Betonung ist hier auf **Überlegen** und **Diskutieren** gesetzt, nicht auf richtig
oder falsch (außer [EREFQ::1] und [EREFQ::2], diese müssen bitte schon stimmen).

**Kommandoprotokoll**
[PROT::ALT:go-advanced-control-flow.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-acf.go]
[ENDINSTRUCTOR]
