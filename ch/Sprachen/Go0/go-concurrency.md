title: Nebenläufigkeit und Parallelität in Go
stage: draft
timevalue: 3
difficulty: 3
assumes: go-basics-i, go-basics-ii
---

[SECTION::goal::idea,experience]

Ich weiß, wie Parallelität und Nebenläufigkeit in Go aussehen, und kann Programme so gestalten und implementieren, dass alle CPU-Kerne für die Aufgabe eingesetzt werden.

[ENDSECTION]

[SECTION::background::default]

Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet — eine Ressource, die wir als Programmierer_innen nicht ignorieren sollten. 
Wer seine Software auf nur einem Kern laufen lässt, verschenkt wertvolle Rechenleistung und bremst die eigene Anwendung unnötig aus. 
Go bietet mit seinen eingebauten Konzepten für Nebenläufigkeit Werkzeuge, um das volle Potenzial heutiger Hardware auszuschöpfen und deutlich schnellere Programme zu entwickeln.

In dieser Aufgabe lernen Sie folgendes kennen:

- Goroutinen — leichtgewichtige Threads, die von der Go-Laufzeitumgebung verwaltet werden;
- Kanäle (Channels) — der Datentyp `chan`, welcher strukturierte Kommunikation zwischen Goroutinen ermöglicht; 
- Synchronisierungsmöglichkeiten — `select`, `sync.Mutex` und `sync.WaitGroup`;
- `context`-Paket;
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
 - Kanäle können gepuffert werden — so kann das Empfangen von dem Senden zeitlich einigermaßen entkoppelt werden.

Syntax-Übersicht:

```go
c := make(chan int)         // einen Kanal kreieren
c := make(chan int, 4)      // einen gepufferten Kanal kreieren
c <- 42                     // einen Wert senden
received := <-c             // einen Wert empfangen
received, ok := <-c         // einen Wert empfangen und überprüfen, ob der Kanal aktiv (nicht geschlossen und nicht leer) ist
close(c)                    // einen Kanal schließen
```

[WARNING]

Ein Senden ist nur dann erfolgreich, wenn der Wert auf der anderen Seite ausgelesen wird oder wenn es noch Platz im Puffer gibt.
Sonst ist diese Operation blockierend.

Das Gleiche gilt für das Empfangen: Diese Operation blockiert, falls es nichts auszulesen gibt.

[ENDWARNING]


#### Kanalaxiome

Die folgende Tabelle kann beim Debuggen sehr hilfreich sein.
Besonders wichtig sind die Fälle "block forever": Oft wirkt es sehr verwirrend, wenn das Programm einfach hängt, statt eine Fehlermeldung anzuzeigen.

|    Operation     |  Nil Channel  | Closed Channel | Not-Closed Non-Nil Channel |
|:----------------:|:-------------:|:--------------:|:--------------------------:|
|    **Close**     |     panic     |     panic      |          succeed           |
|   **Send To**    | block forever |     panic      |      block or succeed      |
| **Receive From** | block forever |  never block   |      block or succeed      |

[Quelle](https://go101.org/article/channel.html)


#### Kanäle ausprobieren

- [ER] Implementieren Sie eine Funktion `sender(c chan int)`, welche Zahlen von 0 bis 5 an den Kanal `c` verschickt und danach den Kanal schließt.
- [ER] Implementieren Sie eine Funktion `receiver(c chan int)`, welche versucht, 10 Zahlen aus dem Kanal `c` zu empfangen und auf der Kommandozeile anzuzeigen.
  Benutzen Sie dabei die `val, ok`-Schreibweise.
- [ER] Implementieren Sie anschließend eine Funktion `testChannels()`, wo
    * ein Kanal vom Typ `int` erstellt wird;
    * `sender` und `receiver` nebenläufig aufgerufen werden.
- [ER] Fügen Sie die Funktion `testChannels()` der `main`-Funktion bei.


### Synchronisationsmechanismen

### `select`

`select` ist eine Kontrollflussstruktur. 
Sie besteht aus mehreren Fällen (cases) und führt nur denjenigen aus, der zu dem Zeitpunkt zutrifft.
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
        return
    } 
}
```


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

[FOLDOUT::lock-increment-unlock]

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
var counter atomic.Int32        // counter == 0, weil das der Standardwert von int32 ist

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
* Lösung: `sync.RWMutex` — `Lock()`/`Unlock()` für Schreiben und `RLock()`/`RUnlock()` für Lesen.
    - erlaubt nebenläufige Lesezugriffe, solange die Daten unverändert bleiben.
      ein `.RLock()`-Aufruf blockiert die anderen `.RLock()`-Aufrufe nicht; ein `.Lock()`-Aufruf blockiert die anderen `.Lock()`- und `.RLock()`-Aufrufe.  

[ENDFOLDOUT]

#### sync.WaitGroup

`sync.WaitGroup` ist ein weiterer Synchronisationsmechanismus, der mehrere Goroutinen untereinander synchronisiert.

Eine `WaitGroup` stellt einen **Semaphor** dar, auch wenn mit einigen Unterschieden.

[NOTICE]

**Semaphor**

Ein Semaphor lässt mehrere (aber nicht alle) Akteure gleichzeitig den kritischen Abschnitt betreten und signalisiert den anderen, sobald es im kritischen Abschnitt eine "freie Stelle" gibt.

Intern gibt es einen Zähler, der mit der Anzahl von "verfügbaren Plätzen" initialisiert wird.

Ein Thread dekrementiert den Zähler beim Erwerb der Ressource und inkrementiert ihn erst dann, wenn die Ressource wieder freigegeben wird.

Alle Threads, die bei einem nichtpositiven Zähler die Ressource anfragen, werden blockiert.

[Dem Foliensatz](https://www.inf.fu-berlin.de/inst/ag-se/teaching/V-NSEQ-2023/08_Semaphor_Monitor.pdf) 
können Sie weitere Informationen entnehmen, falls Sie mehr theoretischen Hintergrund zum Thema haben möchten (Nichtsequentielle und verteilte Programmierung, Barry Linnert).


[ENDNOTICE]

Der Initialwert des internen Zählers von einer `WaitGroup` ist 0.

Methoden:

- `Add(delta int)` — inkrementiert den internen Zähler um `delta`.
  In der Regel bedeutet das den Start einer Goroutine oder das Betreten des kritischen Abschnitts.
- `Done()` — dekrementiert den internen Zähler um 1.
  Das signalisiert, dass eine Goroutine nun fertig ist und ihre Aufgabe erledigt hat — der kritische Abschnitt wird verlassen.
- `Wait()` — blockiert die Ausführung, wenn/solange der interne Zähler ungleich 0 ist.

### `context`

### Frequently begangene Fehler

// ab hier wahrscheinlich concurrency-advanced, wenn überhaupt

### Programmieren

#### a) Game of Life

#### b) File Processing

#### c) Primzahlen

#### d) Dateisystem traversieren

[FOLDOUT::Wie funktioniert eigentlich der Scheduler?]

* [Kurze Version](https://medium.com/@hatronix/inside-the-go-scheduler-a-step-by-step-look-at-goroutine-management-1a8cbe9d5dbd)
* [Lange Version](https://medium.com/@sanilkhurana7/understanding-the-go-scheduler-and-looking-at-how-it-works-e431a6daacf)

[ENDFOLDOUT]
#### 



[ENDSECTION]