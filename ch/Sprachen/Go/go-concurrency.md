title: Nebenläufigkeit und Parallelität in Go
stage: draft
timevalue: 2.5
difficulty: 3
---

[SECTION::goal::idea,experience]

Ich kenne die Werkzeuge, die Go für Nebenläufigkeit und Parallelität bietet, sowie die häufigsten Fehler bei deren Verwendung.

[ENDSECTION]

[SECTION::background::default]

Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet — eine Ressource, die wir als Programmierer_innen nicht ignorieren sollten. 
Wer seine Software auf nur einem Kern laufen lässt, verschenkt wertvolle Rechenleistung und bremst die eigene Anwendung unnötig aus.
Mit den eingebauten Konzepten für Nebenläufigkeit bietet Go Werkzeuge, um das volle Potenzial heutiger Hardware auszuschöpfen und deutlich schnellere Programme zu entwickeln.

In dieser Aufgabe lernen Sie folgendes kennen:

- Kanäle (Channels) — der Datentyp `chan`, welcher strukturierte Kommunikation zwischen Goroutinen ermöglicht; 
- Synchronisierungsmöglichkeiten — `select`, `sync.Mutex` und `sync.WaitGroup`;
- häufige Fallstricke beim Parallelisieren.

[ENDSECTION]

[SECTION::instructions::detailed]

### Synchronisationsmechanismen


### sync.Mutex

Das Wort "Mutex" stammt von "mutual exclusion" — "gegenseitiger Ausschluss".

Vereinfacht ist ein Mutex eine Lock-Variable, die den unkoordinierten Zugriff auf die gemeinsamen Datenstrukturen von verschiedenen Threads verhindert.

Mutexe sind eine Lösung von dem Problem des kritischen Abschnitts — eines Quellcodeabschnitts, welcher nur von einem Prozess/Thread zur selben Zeit ausgeführt werden darf.

[Hier](https://stackoverflow.com/questions/34524/what-is-a-mutex) finden Sie eine ziemlich gute und anschauliche Erklärung, was ein Mutex ist.

Beispiel:

```go
var mu sync.Mutex

...

mu.Lock()
counter++
someCriticalSectionMap["newKey"] = newValue
mu.Unlock()
```

[FOLDOUT::Eine Alternative dem lock-increment-unlock-Zyklus: `atomic`]

Für einen Zähler scheint das etwas umständlich — einen Mutex initialisieren, sperren, freigeben...
Wenn es sich ausschließlich um Variablenmanipulationen handelt, ist das Paket `atomic` sehr hilfreich.

Ein Zähler mit Mutexen und ohne `atomic`:

```go
counter := 0
var mu sync.Mutex

// kritischer Abschnitt Start
mu.Lock()
counter++
mu.Unlock()
// kritischer Abschnitt Ende
```

Ein Zähler ohne Mutexe und mit `atomic`:

```go
var counter atomic.Int32        // counter == 0, weil das der Nullwert von int32 ist

// kritischer Abschnitt Start
counter.Add(1)
// kritischer Abschnitt Ende
```

[ENDFOLDOUT]

[FOLDOUT::mehr Granularität]

Zusätzlich zum `sync.Mutex` gibt es noch den `sync.RWMutex` (Read-Write-Mutex).

Dieser ist zu bevorzugen, wenn Leseoperationen viel öfter stattfinden als die Schreiboperationen.
Hier ist eine Übersicht von möglichen Abwägungen:

* Idee 1: kein Mutex beim Lesen, Mutex beim Schreiben.
    - fehlerhaft, wenn eine Goroutine die Daten ausliest, während die andere die Daten modifiziert — Korrektheit kann nicht garantiert werden (**Race Condition**).
* Idee 2: Mutex sowohl beim Lesen als auch beim Schreiben.
    - unnötiger Leistungsverlust — es kann nur eine Goroutine zur selben Zeit die Daten auslesen, auch wenn mehrere parallele Leseoperationen in Ordnung wären.
* Lösung: `sync.RWMutex` — `Lock()`/`Unlock()` beim Schreiben und `RLock()`/`RUnlock()` beim Lesen.
    - erlaubt nebenläufige Lesezugriffe, solange die Daten unverändert bleiben.
      ein `.RLock()`-Aufruf blockiert die anderen `.RLock()`-Aufrufe nicht; ein `.Lock()`-Aufruf blockiert die anderen `.Lock()`- und `.RLock()`-Aufrufe.  

[ENDFOLDOUT]


#### sync.WaitGroup

`sync.WaitGroup` ist ein weiterer Synchronisationsmechanismus, der mehrere Goroutinen untereinander synchronisiert.
Hier bedeutet das: Die Programmausführung darf erst dann fortgesetzt werden, wenn alle _n_ Goroutinen beendet wurden.

Intern besitzt jede `WaitGroup` einen Zähler — dieser gibt an, auf wie viele Goroutinen es gewartet werden soll.
Der Zähler wird mit 0 initialisiert (es muss auf nichts gewartet werden).

`wg.Add(delta int)` addiert `delta` zum Wert des internen Zählers, `wg.Done()` subtrahiert 1.

`wg.Wait()` blockiert, solange der interne Zähler größer als 0 ist. 

Grobe Vorgehensweise:

- jede Goroutine bei einer `WaitGroup` anmelden: `wg.Add(1)`;
- Goroutine starten;
- wenn eine Goroutine mit ihrer Aufgabe fertig ist, ruft sie `wg.Done()` auf;
- `wg.Wait()` blockiert, bis alle Goroutinen `wg.Done()` aufgerufen haben.

[WARNING]

`wg.Add(1)` muss immer **vor dem Start** der entsprechenden Goroutine aufgerufen werden.

Vergleichen Sie die folgenden Beispiele:

```go
// Beispiel 1
wg := sync.WaitGroup{}

wg.Add(1)
go func() {
    defer wg.Done()
    // do work
}()

wg.Wait()
```

```go
// Beispiel 2
wg := sync.WaitGroup{}

go func() {
    wg.Add(1)
    defer wg.Done()
    // do work
}()

wg.Wait()
```

Im zweiten Beispiel ist es nicht garantiert, dass `wg.Wait()` nach dem `wg.Add(1)` aufgerufen wird. 
Sollte das nicht der Fall sein, so endet das Programm noch bevor die Goroutine ihre Aufgabe erledigt hat. 

[ENDWARNING]


#### Synchronisierung ausprobieren

[ER] Implementieren Sie eine Funktion namens `testCounter`. 
Diese soll folgendes tun:

- einen Zähler mit 0 initialisieren und in einer `for`-Schleife eine Million Goroutinen starten, welche den Zähler jeweils um 1 inkrementieren.
  Die Goroutinen müssen mittels einer `WaitGroup` synchronisiert werden, sonst wird die Funktion `testCounter` zu früh beendet;
- die totale Ausführungszeit messen (`time.Now()` und `time.Since()` helfen Ihnen dabei);
- den Zähler sowie die Ausführungszeit auf die Kommandozeile ausgeben.
  Das Format soll folgendermaßen aussehen: `"function_name - counter: %Wert%, achieved in %Wert%\n"`.

[ER] Implementieren Sie eine Funktion namens `testCounterMutex`.
In dieser Variante muss der kritische Abschnitt mithilfe von einem Mutex geschützt werden. 
An allen anderen Stellen darf die Funktion genauso bleiben wie die `testCounter`. Passen Sie die Ausgabe auf die Kommandozeile entsprechend an (`function_name = testCounterMutex`).

[ER] Implementieren Sie nun eine Funktion `testCounterChannels`.
Diese Version unterscheidet sich von den vorherigen zwei Varianten dadurch, dass der kritische Abschnitt mittels eines Kanals geschützt wird.

- Erstellen Sie einen Kanal des Typen `int` und starten Sie eine Goroutine, welche in einer Endlosschleife die Werte aus dem Kanal empfängt und zum `counter` addiert;
- Die Million Goroutinen greifen nicht mehr direkt auf den Zähler zu; stattdessen senden sie jeweils eine 1 über den Kanal an die empfangende Goroutine;
- (optional) wenn Sie die empfangende Goroutine auch ordentlich beendet wollen:
    - benutzen Sie die Schreibweise `value, ok := <- channel` und brechen Sie die Endlosschleife ab, sobald der Kanal geschlossen ist;
    - schließen Sie den Kanal, sobald die Million Goroutinen fertig sind.


Diskutieren Sie die Ergebnisse:

[EQ] Welche Implementierungen haben das richtige Ergebnis geliefert? Welche nicht?

[EQ] Was ist die schnellste Implementierung? Was ist die langsamste? Warum?
 

### Oft begangene Fehler

#### Wettlaufsituation (Race Condition)

Eine Race Condition ist ein Fehlertyp, bei dem das Ergebnis von der Ausführungsreihenfolge von nebenläufigen Operationen abhängt.
Diesen Fehlertyp haben Sie bereits anhand von `testCounter` kennengelernt.

Ein anderes Beispiel finden Sie in der Warnung oben, im Abschnitt zu `sync.WaitGroup`.

#### Mutexe per Wert übergeben

```go
// diese Struktur zählt, wie oft ein Wort vorkommt
type Counter struct {
    mu    sync.Mutex
    words map[string]int
}

// c ist ein neuer Zähler — eine Kopie, weil Strukturen per Wert übergeben werden
func worker(c Counter, wg *sync.WaitGroup) {
    defer wg.Done()
    // Textverarbeitung hier...
    
    c.mu.Lock()         // c.mu ist ein komplett anderer Mutex
    words[nextWord]++   // gefährlich, wenn es mehrere 'worker's gibt
    c.mu.Unlock()
    
    // Textverarbeitung geht weiter...
}
```

#### Kanalbezogene Fehler

```go
func channelWithoutDirection(ch chan int) {
    // Kann sowohl lesen als auch schreiben — verwirrend
    ch <- 42
    val := <-ch
}

func deadlock() {
    ch := make(chan int)
    ch <- 42 // blockiert für immer 
    fmt.Println("Never reached")
}

func sendOnClosed() {
    ch := make(chan int)
    close(ch)
    ch <- 42 // auf geschlossenen Kanal schreiben — Panik
}
```

### Fehlerjagd

[EQ] Betrachten Sie das folgende (fehlerhafte) Programm.
Welche Zeile enthält den Fehler und wie muss diese Zeile aussehen, damit das Programm wieder funktioniert?

```go
[INCLUDE::include/go-concurrency-broken-example.go]
```

[FOLDOUT::Wie funktioniert der Go-Scheduler?]

* [Kurze Version](https://medium.com/@hatronix/inside-the-go-scheduler-a-step-by-step-look-at-goroutine-management-1a8cbe9d5dbd)
* [Lange Version](https://medium.com/@sanilkhurana7/understanding-the-go-scheduler-and-looking-at-how-it-works-e431a6daacf)

[ENDFOLDOUT]

[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
