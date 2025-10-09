title: "Go: sync.Mutex"
stage: draft
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich weiß, was ein Mutex ist und wie Mutexe in Go verwendet werden. 
[ENDSECTION]

[SECTION::background::default]
Eine der Synchronisierungsmöglichkeiten sind Mutexe — Schlossvariablen,
die kontrollieren, wer auf bestimmte geteilte Daten zu einem bestimmten Zeitpunkt 
zugreifen darf und wer nicht.

In dieser Aufgabe geht es um Mutexe in Go: Welche es gibt, wo und wie sie zu verwenden sind,
und welche Alternativen es gibt.
[ENDSECTION]

[SECTION::instructions::detailed]

### sync.Mutex

Das Wort "Mutex" stammt von "mutual exclusion" — "gegenseitiger Ausschluss".

Vereinfacht ist ein Mutex eine Lock-Variable, die den unkoordinierten Zugriff auf 
die gemeinsamen Datenstrukturen von verschiedenen Threads verhindert.

Mutexe sind eine Lösung von dem Problem des kritischen Abschnitts — eines Quellcodeabschnitts, 
welcher nur von einem Prozess/Thread zur selben Zeit ausgeführt werden darf.

In diesem 
[StackOverflow-Beitrag](https://stackoverflow.com/questions/34524/what-is-a-mutex)
finden Sie eine ziemlich gute Erklärung, was ein Mutex ist.

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


### Programmieren

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


### Oft begangene Fehler

#### Wettlaufsituation (Race Condition)

Eine Race Condition ist ein Fehlertyp, bei dem das Ergebnis von der Ausführungsreihenfolge von nebenläufigen Operationen abhängt.
Diesen Fehlertyp haben Sie bereits anhand von `testCounter` kennengelernt.

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

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]
