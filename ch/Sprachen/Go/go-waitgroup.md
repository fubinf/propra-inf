title: "Go: sync.WaitGroup"
stage: draft
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::idea,experience]
TODO_Brandes
[ENDSECTION]

[SECTION::background::default]
TODO_Brandes
[ENDSECTION]

[SECTION::instructions::detailed]

### sync.WaitGroup

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

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]
