title: Nebenläufigkeit und Parallelität in Go
stage: draft
timevalue: 3
difficulty: 3
assumes: go-basics1, go-basics2, go-basics3
---

[SECTION::goal::idea,experience]

Ich kenne die Werkzeuge, die Go für Nebenläufigkeit und Parallelität bietet, sowie die häufigsten Fehler bei deren Verwendung.

[ENDSECTION]

[SECTION::background::default]

Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet — eine Ressource, die wir als Programmierer_innen nicht ignorieren sollten. 
Wer seine Software auf nur einem Kern laufen lässt, verschenkt wertvolle Rechenleistung und bremst die eigene Anwendung unnötig aus.
Mit den eingebauten Konzepten für Nebenläufigkeit bietet Go Werkzeuge, um das volle Potenzial heutiger Hardware auszuschöpfen und deutlich schnellere Programme zu entwickeln.

In dieser Aufgabe lernen Sie folgendes kennen:

- Goroutinen — leichtgewichtige Threads, die von der Go-Laufzeitumgebung verwaltet werden;
- Kanäle (Channels) — der Datentyp `chan`, welcher strukturierte Kommunikation zwischen Goroutinen ermöglicht; 
- Synchronisierungsmöglichkeiten — `select`, `sync.Mutex` und `sync.WaitGroup`;
- häufige Fallstricke beim Parallelisieren.

[ENDSECTION]

[SECTION::instructions::detailed]

[FOLDOUT::Was ist Nebenläufigkeit und was ist Parallelität?]

* **parallele Ausführung:** Das bedeutet, dass die einzelnen Befehle der Programme tatsächlich gleichzeitig auf mehreren CPU-Kernen ausgeführt werden. 
  Dadurch wird echte Gleichzeitigkeit erreicht.
* **nebenläufige Ausführung:** In diesem Fall werden die Programme abwechselnd auf einem CPU-Kern ausgeführt. 
  Obwohl sie nicht wirklich gleichzeitig laufen, erscheint der Ablauf dennoch "parallel", da die Umschaltung zwischen den Programmen schnell genug erfolgt, um den Eindruck von Gleichzeitigkeit zu erwecken.

[ENDFOLDOUT]


### Goroutinen

Eine Goroutine ist ein leichtgewichtiger ("grüner") Thread. 
Solche Goroutinen sind bezüglich der Laufzeiteffizienz extrem billig: Millionen von Goroutinen können nebeneinander verwaltet werden.  

Eine neue Goroutine wird mithilfe von dem Schlüsselwort `go` erzeugt.
Diese braucht keine besondere Verwaltung — sie wird automatisch von dem Scheduler zum Laufen gebracht und automatisch aufgeräumt, sobald die darin laufende Funktion ihre Aufgabe beendet hat.

[ER] Implementieren Sie eine Funktion `delayedGreeting(msg string)`, die zuerst 2 Sekunden schläft und anschließend eine Begrüßung Ihrer Wahl auf die Kommandozeile ausgibt.

[ER] Implementieren Sie auch eine andere Funktion namens `testGo()`, wo Sie zuerst `go delayedGreeting(...)` und in der nächsten Zeile `fmt.Println(...)` aufrufen.

[ER] Rufen Sie die Funktion `testGo()` aus der `main`-Funktion aus und blockieren Sie `main` mithilfe von einer Endlosschleife.
Später lernen Sie bessere Synchronisierungsmöglichkeiten, aber für jetzt reicht ein `for {}` völlig aus.

Für manche Programmierer_innen kann das ein bisschen umständlich scheinen — immer zuerst eine neue Funktion definieren zu müssen.
Zum Glück ist das nicht nötig, denn Go erlaubt das Wort `go` auch für anonyme/lambda Funktionen.

[ER] Implementieren Sie eine andere Funktion `testGoLambda()`, die prinzipiell das Gleiche tut wie `testGo()`, jedoch mit einem Unterschied — die Funktion `delayedGreeting(msg string)` soll zu einer Lambda-Funktion umgewandelt werden.

[ER] Fügen Sie `testGoLambda()` ebenfalls in Ihre `main()`-Funktion ein.

Diskutieren Sie:

[EQ] In welcher Reihenfolge werden die Funktionen (`testGo`, `testGoLambda`, `delayedGreeting` und die lambda-Funktion) gestartet?

[EQ] In welcher Reihenfolge verlassen die vier Funktionen den Geltungsbereich (beenden ihre Ausführung)? 


### Kanäle

- Ein Kanal ist im Go-Universum ein "Rohr" zwischen zwei Goroutinen.
- Daten, die durch ein solches "Rohr" gesendet und empfangen werden, behalten ihre Reihenfolge — in diesem Sinne verhalten sich Kanäle wie Warteschlangen.
- Kanäle sind typisiert und akzeptieren nur Werte von einem bestimmten Datentyp.
- Kanäle können gepuffert werden — sie bekommen eine Art Zwischenablage, wo die gesendeten Werte abgelegt werden, bis sie ausgelesen werden.
  So kann das Empfangen von dem Senden zeitlich einigermaßen entkoppelt werden.

#### Syntax-Übersicht

```go
c := make(chan int)         // einen Kanal kreieren
c := make(chan int, 4)      // einen gepufferten Kanal kreieren — Größe des Puffers ist 4
c <- 42                     // einen Wert senden
received := <-c             // einen Wert empfangen
_ = <-c                     // einen Wert empfangen und ignorieren
<-c                         // einen Wert empfangen und ignorieren
received, ok := <-c         // einen Wert empfangen und überprüfen, ob der Kanal aktiv (nicht geschlossen und nicht leer) ist
close(c)                    // einen Kanal schließen
```

Go ermöglicht es, bereits in der Funktionssignatur die Richtung eines Kanals zu spezifizieren — 
ob dieser nur zum Senden (`chan<-`), nur zum Empfangen (`<-chan`) oder bidirektional (`chan`) genutzt werden kann:

```go
// nur senden
func (c chan<- int) {}

// nur empfangen
func (c <-chan int) {}

// senden und empfangen
func (c chan int) {}
```

Für eine sequentielle Verarbeitung der aus einem Kanal empfangenen Werte gibt es die bereits bekannte `for`-Schleife:

```go
// blockiert, bis der Kanal geschlossen wird
for someValue := range intChan {
    fmt.Println(someValue)
}
```

#### Kanalaxiome ([Quelle](https://go101.org/article/channel.html))

Folgende Übersicht "Operation + Kanaltyp => Verhalten" kann beim Debuggen sehr hilfreich sein.
Besonders wichtig sind die Fälle "block forever": Oft wirkt es sehr verwirrend, wenn das Programm einfach hängt, statt eine Fehlermeldung anzuzeigen.

[NOTICE]

**Nullkanal und `panic`**

Eine Deklaration wie `var ch chan int` nennen wir hier und weiter _Nullkanal_.
Dadurch, dass Kanäle ein Referenztyp sind, verhält sich `ch` wie ein Zeiger und übernimmt den Nullwert eines Zeigers — nämlich `nil`.

`panic` ist ein Mechanismus für das Behandeln von schwerwiegenden Laufzeitfehlern. 
Das ähnelt den Exceptions in Sprachen wie Python oder Java mit dem Unterschied, dass die `panic`s wirklich kritisch sind: 
Sie stellen den "Das Programm kann/darf nicht weiter laufen"-Zustand dar.

Falls Sie ganz genau wissen möchten, was `panic` ist, könnte diese Aufgabe für Sie von Interesse sein: [PARTREF::go-advanced-control-flow].

[ENDNOTICE]

**Schließen (`close(ch)`):**

- Nullkanal -> `panic`
- ein bereits geschlossener Kanal -> `panic`
- ein existierender Kanal -> Erfolg

**Senden (`ch <-`):**

- Nullkanal -> für immer blockieren
- ein bereits geschlossener Kanal -> `panic`
- ein existierender Kanal -> blockieren oder Erfolg

**Empfangen (`<- ch`):**

- Nullkanal -> für immer blockieren
- ein bereits geschlossener Kanal -> Empfänger bekommen den Nullwert von dem Typ des Kanals
- ein existierender Kanal -> blockieren oder Erfolg


#### Kanäle ausprobieren

[ER] Implementieren Sie eine Funktion `sender(c chan<- int)`, welche Zahlen von 0 bis 5 an den Kanal `c` verschickt und danach den Kanal schließt.

[ER] Implementieren Sie eine Funktion `receiver(c <-chan int)`, welche versucht, 10 Zahlen aus dem Kanal `c` zu empfangen und auf der Kommandozeile anzuzeigen.
  Benutzen Sie dabei die `val, ok`-Schreibweise.

[ER] Implementieren Sie anschließend eine Funktion `testChannels()`, wo

* ein Kanal vom Typ `int` erstellt wird;
* `sender` und `receiver` nebenläufig aufgerufen werden.

[ER] Fügen Sie die Funktion `testChannels()` der `main`-Funktion bei.


### Synchronisationsmechanismen

### `select`

`select` ist eine Kontrollflussstruktur. 
Sie besteht aus mehreren Zweigen (cases) und führt nur denjenigen aus, der zu dem Zeitpunkt zutrifft.
Genauso wie bei einem Switch gibt es einen `default`-Zweig, welcher nur dann ausgeführt wird, wenn nichts anderes zutrifft.

Ein beliebter Anwendungsfall ist es, mehrere Kanäle unter einem `select` zu benutzen — je nachdem, welcher Kanal gerade einen Wert empfangen hat, können verschiedene Aktionen durchgeführt werden.

Beispiel:

```go
var dataChan chan []byte

// struct{} ist ein zero-byte Typ, bequem für Kommunikation der Art "guck mal hier, es ist was passiert"
var cancelChan chan struct{}

...
for {
    select {
    case data := <-dataChan:
        processData(data)
    case <-cancelChan:
        // wir interessieren uns nicht dafür, _was_ empfangen wurde
        // das Empfagen selbst ist das Signal
        return
    }
}
```

[FOLDOUT::Wo kommt der `cancelChan` her?]

Einen solchen Kanal können Sie natürlich selbstständig erzeugen und benutzen.
Meistens kommt er jedoch als Teil eines _Kontexts_.

Das Paket `context` gehört zur Standardbibliothek und bietet Werkzeuge zur Übertragung von Abbruchsignalen oder anfragespezifischen Werten.

Beispiele:

```go
// so wird ein Kontext erzeugt; in 10 Sekunden kommt ein Abbruchsignal
ctx, _ := context.WithTimeout(context.Background(), 10 * time.Second)
```

```go
func doWork(ctx context.Context, ch chan int) {
    for {
        select {
            case newInt := <- ch {
                // do work...
            }
            // ctx.Done() gibt einen Kanal zurück, der geschlossen wird, wenn die Ausführung abgebrochen werden soll
            // dieses Ereignis wird hier im select-Block abgefangen
            case <- ctx.Done() {
                return
            }
        }
    }
}
```

Mehr zum Paket `context` in dieser Aufgabe: [PARTREF::go-context].

[ENDFOLDOUT]


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
[INCLUDE::snippets/go-concurrency-broken-example.go]
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
