title: "Kontrollfluss in Go: defer, panic und recover"
stage: draft
timevalue: 1.25
difficulty: 2
assumes: go-interfaces
---

[SECTION::goal::idea,experience]
Ich weiß, wo und wie die Go-Schlüsselwörter `defer`, `panic` und `recover` 
verwendet werden.
[ENDSECTION]

[TOC]

[SECTION::background::default]
Das Schlüsselwort `panic` ist Ihnen möglicherweise bereits bekannt.

`panic` und `recover` stellen einen alternativen Kontrollflussmechanismus dar — 
das sogenannte _Panicking_.
Dieses Verhalten erinnert an Ausnahmen (Exceptions) in Sprachen wie Java oder Python, 
weist jedoch einige wichtige Unterschiede auf.

In dieser Aufgabe schauen wir uns diese Konzepte im Detail an und klären folgende Fragen:

* Wie funktioniert `defer` genau?
* Was bedeutet _Panicking_ konkret?
* Wie (und wann) sollte `recover` verwendet werden — wenn überhaupt?
[ENDSECTION]

[SECTION::instructions::detailed]

### `defer`

Das Schlüsselwort `defer` verzögert die Ausführung eines Funktionsaufrufs.

Ein `defer`-Aufruf wird erst dann ausgeführt, wenn die umgebende Funktion 
(oder generell: Geltungsbereich) ihre Ausführung beendet — unmittelbar _vor_ dem `return`.

Schauen Sie sich das
[Thema 'defer' in "A Tour of Go"](https://go.dev/tour/flowcontrol/12)
an.

[EQ] Fügen Sie dem Beispielprogramm dort eine weitere `defer`-Anweisung hinzu — beispielsweise
`defer fmt.Println("!")` in Zeile 7.
Was können Sie über die Ausführungsreihenfolge von mehreren `defer`s sagen?

<!-- time estimate: 5 min -->


#### Auswerten von Argumenten

Im 
[Beitrag 'Defer, Panic, and Recover' im Go Blog](https://go.dev/blog/defer-panic-and-recover)
findet sich eine interessante Aussage über das Verhalten von `defer`:

    Die Argumente einer aufgeschobenen Funktion werden zum Zeitpunkt der Ausführung der `defer`-Anweisung ausgewertet.

Doch was bedeutet das genau?

Konzeptionell gibt es zwei gängige Arten, `defer` zu verwenden:

__1. Mit einem direkten Funktionsaufruf:__
```go
defer fmt.Println(s)
```

__2. Mit einer anonymen Funktion:__
```go
defer func(t string) { 
    fmt.Println(t)
    fmt.Println(v) // v stammt aus dem äußeren Geltungsbereich 
}(t)
```

Im ersten Fall werden alle Argumente der Funktion — hier also `s` — sofort beim 
Erfassen der `defer`-Anweisung ausgewertet.

Im zweiten Fall wird nur das explizit übergebene Argument (`t`) direkt ausgewertet.
Andere innerhalb der anonymen Funktion verwendete Variablen wie `v` werden erst beim 
tatsächlichen Ausführen der aufgeschobenen Funktion ausgewertet.

[EQ] Was wird beim Ausführen dieser Funktion auf der Kommandozeile ausgegeben?
Warum?

```go
func testDefer() (s string) {
    defer fmt.Println(s)
    s = "done"
    return s
}
```

[EQ] Was wird beim Ausführen dieser Funktion auf der Kommandozeile ausgegeben?
Warum?

```go
func testDefer() (s string) {
    defer func() { fmt.Println(s) }()
    s = "done"
    return s
}
```

[EQ] Welche Anwendungen von `defer` werden im
[Artikel 'defer' in "Go by Example"](https://gobyexample.com/defer)
erwähnt?
Welche andere Anwendungen fallen Ihnen ein?

<!-- time estimate: 15 min -->


### `panic`


#### Fehler als Werte

In [PARTREF::go-interfaces] haben Sie das Interface `error` kennengelernt.

Die Fehlerbehandlung in Go folgt dem Prinzip _"Errors as Values"_ 
(beziehungsweise _"Fehler als Werte"_):
Funktionen, bei denen etwas schiefgehen kann, geben nach Konvention einen 
zusätzlichen Rückgabewert vom Typ `error` zurück.

Im Erfolgsfall ist dieser Wert `nil`, andernfalls enthält er den aufgetretenen `error`:

```go
func parseInt(s string) (i int, err error) {
    ...
}
```


#### Panicking

Ein alternativer Mechanismus ist das sogenannte _Panicking_.

[EQ] Schauen Sie sich den 
[Beitrag "Go by Example: Panic"](https://gobyexample.com/panic)
an.
Wie wird das _Panicking_ gestartet?

Tritt in einer Funktion eine `panic` auf, wird ihre normale Ausführung sofort abgebrochen.
Anschließend werden alle aufgeschobenen (`defer`) Anweisungen ausgeführt, und die `panic` wird
entlang des Call-Stacks nach oben weitergereicht.

Dieser Vorgang wiederholt sich, bis die `panic` entweder abgefangen wird oder das Programm
die oberste Ebene erreicht (einschließlich der `main`-Funktion).
In letzterem Fall spricht man von einem Programmabbruch oder einem _Crash_.

[NOTICE]
Alle Funktionen, die intern `panic()` aufrufen, sollen nach Konvention mit `must`
anfangen und dürfen keinen `error` zurückgeben.
Die Idee ist, dass die Operation erfolgreich sein **muss** — wenn das schiefgeht, 
ergibt weitere Ausführung keinen Sinn und das komplette Programm darf abstürzen.
[ENDNOTICE]

[EQ] Lesen Sie den Abschnitt __"When is panicking appropriate?"__ im 
[Artikel "When is it OK to panic in Go?"](https://www.alexedwards.net/blog/when-is-it-ok-to-panic-in-go) 
und beantworten Sie die Frage:
Wann würde der Autor des Artikels _Panicking_ der normalen Fehlerbehandlung vorziehen?

[ER] Implementieren Sie eine Funktion `mustGetInt64FromConsole() int64`, die 
folgende Aufgaben erfüllt:

- Liest eine Ganzzahl von der Kommandozeile ein und gibt sie als `int64` zurück;
- Ruft `panic(err)` auf, falls `strconv.ParseInt()` einen `error` liefert;
- Gibt andernfalls das Ergebnis `res` zurück.

[ER] Rufen Sie die Funktion `mustGetInt64FromConsole()` in der `main`-Funktion auf und 
geben Sie das Ergebnis auf die Kommandozeile aus.

[HINT::ich weiß nicht, wie eine Zahl von der Kommandozeile eingelesen wird]
Schauen Sie hier nach, wie das funktioniert: 
[Reading in Console Input in Go](https://tutorialedge.net/golang/reading-console-input-golang/).

Es macht keinen Unterschied, ob Sie `bufio.Reader` oder `bufio.Scanner` benutzen.
[ENDHINT]

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "42" ein.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "hello" ein.

<!-- time estimate: 20 min -->


### `recover`

In der Erklärung von `panic` wurde angesprochen, dass sie abgefangen werden kann.

Wie?

Durch einen Aufruf von `recover()` in der __aufgeschobenen anonymen Funktion:__

```go
func notPanickingFunction() (s string) {
    defer func() {
        recover()
        // hier darf s modifiziert werden
    }()
}
```

Ein Aufruf von `recover()` unterbricht das _Panicking_ und stellt den normalen 
Programmfluss wieder her.
Als Rückgabewert erhält man den Wert, mit dem das _Panicking_ ausgelöst wurde.

Der Ablauf beim Abfangen einer `panic` sieht folgendermaßen aus:

1. Eine `panic` tritt auf;
2. Alle aufgeschobenen (`defer`) Funktionen werden ausgeführt — in umgekehrter Reihenfolge;
3. In einer dieser Funktionen wird `recover()` aufgerufen, um:
    - den Kontrollfluss wiederherzustellen;
    - den Fehler auszuwerten;
    - ggf. die Rückgabewerte der Funktion anzupassen.

[NOTICE]
Sie können Rückgabewerte innerhalb eines `defer`-Blocks verändern — vorausgesetzt, 
es handelt sich um _benannte Rückgabewerte_.
[ENDNOTICE]

Schauen Sie sich 
[ein Beispiel von `recover` auf "Go by Example"](https://gobyexample.com/recover)
an.

[ER] Schreiben Sie eine Wrapper-Funktion `getInt64FromConsole() (i int64, err error)`, die
intern die Funktion `mustGetInt64FromConsole` aufruft und ihre `panic` abfängt.
Setzen Sie den Rückgabewert `err` auf das Ergebnis von `recover()` und `i = 0`, 
wenn es einen `error` gibt.
(die Typumwandlung von `any` zu `error` überwinden Sie mittels `fmt.Errorf("%v", someAny)`.)

[ER] Ersetzen Sie `mustGetInt64FromConsole` in der `main`-Funktion durch `getInt64FromConsole`.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "42" ein.

[EC] Rufen Sie das Programm mittels `go run` aus und geben Sie "hello" ein.

[EQ] Nun kennen Sie zwei Mechanismen zur Fehlerbehandlung in Go: _Panicking_ 
und _"Fehler als Werte"_.
Mit diesem Wissen im Hinterkopf, was halten Sie vom 
[Go-Sprichwort](https://go-proverbs.github.io/)
_"don't panic"_?

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

[EREFQ::4], [EREFQ::6], [EREFQ::7] sind als Lernfragen gedacht.
Ihr Zweck besteht darin, dass Studierende darüber nachdenken und gegebenenfalls eigene
Schlussfolgerungen ziehen. 
Der Fokus liegt hierbei auf dem Reflektieren und Diskutieren, nicht auf richtig oder falsch.

**Kommandoprotokoll**
[PROT::ALT:go-advanced-control-flow.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier: 
[TREEREF::/Sprachen/Go/go-acf.go].
[ENDINSTRUCTOR]
