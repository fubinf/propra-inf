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

In der heutigen Zeit sind selbst Smartphones mit leistungsstarken Mehrkernprozessoren ausgestattet.

Als Programmierer_innen sollten wir stets die modernen Leistungsstandards im Blick behalten und die Möglichkeiten der aktuellen Hardware gezielt nutzen, wo es sinnvoll ist.

Natürlich eignet sich nicht jede Aufgabe zur Aufteilung in mehrere parallel ausführbare Teile. 
Doch wenn dies möglich ist, warum nicht die Vorteile der Parallelisierung nutzen?

In dieser Aufgabe lernen Sie Folgendes kennen:

- Goroutinen — leichtgewichtige Threads, die von der Go-Laufzeitumgebung verwaltet werden;
- Kanäle (Channels) — der Datentyp `chan`, welcher strukturierte Kommunikation zwischen Goroutinen ermöglicht; 
- Synchronisierungsmöglichkeiten — `select`, `sync.Mutex` und `sync.WaitGroup`;
- `context`-Paket;
- häufige Fallstricke beim Parallelisieren.

[ENDSECTION]

[SECTION::instructions::detailed]

[FOLDOUT::Was ist Nebenläufigkeit und was ist Parallelität?]

Zwei Programme können auf verschiedene Weise ausgeführt werden:

* **parallel:** Dies bedeutet, dass die einzelnen Befehle der Programme tatsächlich gleichzeitig auf mehreren CPU-Kernen ausgeführt werden. 
  Dadurch wird echte Gleichzeitigkeit erreicht.
* **nebenläufig:** In diesem Fall werden die Programme abwechselnd auf einem einzigen CPU-Kern ausgeführt. 
  Obwohl sie nicht wirklich gleichzeitig laufen, erscheint der Ablauf dennoch "parallel", da die Umschaltung zwischen den Programmen schnell genug erfolgt, um den Eindruck von Gleichzeitigkeit zu erwecken.

[ENDFOLDOUT]

### Goroutinen

Eine Goroutine ist ein leichtgewichtiger ("grüner") Thread. 
Solche Goroutinen sind bezüglich der Laufzeiteffizienz extrem billig: Millionen von Goroutinen können nebeneinander verwaltet werden.  

Eine neue Goroutine wird mithilfe von dem Schlüsselwort `go` erzeugt.
Diese braucht keine besondere Verwaltung — sie wird automatisch von dem Scheduler zum Laufen gebracht und automatisch aufgeräumt, sobald die darin laufende Funktion ihre Aufgabe beendet hat.

- [ER] Implementieren Sie eine Funktion `delayedGreeting(msg string)`, die zuerst 2 Sekunden schläft und anschließend eine Begrüßung Ihrer Wahl auf die Kommandozeile ausgibt.
- [ER] Implementieren Sie auch eine andere Funktion namens `testGo()`, wo Sie zuerst `go delayedGreeting(...)` und in der nächsten Zeile `fmt.Println(...)` aufrufen.
- [ER] Blockieren Sie die `main`-Funktion mithilfe von einer Endlosschleife. 
       Später lernen Sie bessere Synchronisierungsmöglichkeiten, aber für jetzt reicht ein `for {}` völlig aus.

Für manche Programmierer_innen kann das ein bisschen umständlich scheinen — immer zuerst eine neue Funktion definieren zu müssen.
Zum Glück ist das nicht nötig, da Go das Wort `go` für alle Funktionsaufrufe erlaubt — auch für die anonymen/lambda Funktionen.

- [ER] Implementieren Sie eine andere Funktion `testGoLambda()`, die prinzipiell das Gleiche tut wie `testGo()`, jedoch mit einem Unterschied — die Funktion `delayedGreeting(msg string)` soll in situ definiert und aufgerufen werden.
- [ER] Fügen Sie die beiden Funktionen in Ihre `main()`-Funktion ein.

### Kanäle

Ein Kanal ist im Go-Universum ein Rohr / eine Warteschlange zwischen zwei Goroutinen.
Diese Warteschlange erlaubt nur Werte von einem bestimmten Datentyp und kann gepuffert werden. 
Die Goroutinen, die eine Referenz auf den Kanal besitzen, dürfen darüber die Werte von einem festen Typ verschicken (send) und empfangen (receive).

Syntax-Übersicht:

```go
c := make(chan int)         // einen Kanal kreieren
c := make(chan int, 4)      // einen gepufferten Kanal kreieren
c <- 42                     // einen Wert senden
received := <-c             // einen Wert empfangen
close(c)                    // einen Kanal schließen
```

[WARNING]

Ein Verschicken ist nur dann erfolgreich, wenn der Wert auf der anderen Seite ausgelesen wird oder wenn es noch Platz im Puffer gibt.
Sonst ist diese Operation blockierend.

Das Gleiche gilt für das Empfangen: Diese Operation blockiert, falls es nichts auszulesen gibt.

[ENDWARNING]

[FOLDOUT::Kanalaxiome]

Das ist eine Tabelle, die sehr hilfreich beim Debuggen sein könnte.
Besonders wichtig sind die Fälle "block forever": Oft wirkt es sehr verwirrend, wenn das Programm, statt eine Fehlermeldung anzuzeigen, einfach nichts tut.

|             Operation              |  A Nil Channel   | A Closed Channel |  A Not-Closed Non-Nil Channel  |
|:----------------------------------:|:----------------:|:----------------:|:------------------------------:|
|             **Close**              |      panic       |      panic       |        succeed to close        |
|         **Send Value To**          |  block forever   |      panic       |    block or succeed to send    |
|       **Receive Value From**       |  block forever   |   never block    |  block or succeed to receive   |

[Quelle](https://go101.org/article/channel.html)

[ENDFOLDOUT]

### Synchronisierungsmöglichkeiten

#### `select`

`select` ist eine Kontrollflussstruktur. 
Sie besteht aus mehreren Fällen (cases) und führt nur diesen aus, der zu dem Zeitpunkt zutrifft.
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

#### sync.Mutex

#### sync.WaitGroup

### `context`

### Frequently begangene Fehler

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