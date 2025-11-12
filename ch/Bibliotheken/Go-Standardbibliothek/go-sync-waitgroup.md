title: "Go: sync.WaitGroup"
stage: draft
timevalue: 0.5
difficulty: 2
assumes: go-goroutines, go-advanced-control-flow
---

[SECTION::goal::idea,experience]
Ich kann mehrere Goroutinen mit einer `sync.WaitGroup` synchronisieren.
[ENDSECTION]

[SECTION::background::default]
Ist es Ihnen schon einmal passiert, dass Sie in der `main`-Funktion mehrere Goroutinen
gestartet haben, das Programm aber sofort beendet wurde, ohne etwas Sinnvolles auf der
Kommandozeile auszugeben?

Oft liegt das daran, dass die `main`-Funktion beendet wird, bevor die Goroutinen ihre
Arbeit abgeschlossen haben.
In solchen Fällen muss die `main`-Funktion blockiert werden.

Doch wie lange?

Ein `time.Sleep()` ist in den seltensten Fällen die richtige Lösung.

Genau dafür gibt es die `sync.WaitGroup`.
[ENDSECTION]

[SECTION::instructions::detailed]

### `sync.WaitGroup`

`sync.WaitGroup` ist ein weiterer Mechanismus zur Synchronisation, mit dem sich mehrere
Goroutinen koordinieren lassen.

In diesem Fall bedeutet das:
Die Programmausführung soll erst dann fortgesetzt werden, wenn alle Goroutinen abgeschlossen sind.


### Funktionsweise

Intern verwaltet jede `WaitGroup` einen Zähler, der angibt, auf wie viele Goroutinen noch
gewartet werden muss.
Zu Beginn ist dieser Zähler auf 0 gesetzt — es muss also auf nichts gewartet werden.

Mit `wg.Add(delta int)` wird der Zähler um `delta` erhöht (beispielsweise beim Start
neuer Goroutinen).
Ein Aufruf von `wg.Done()` verringert ihn um 1 (wenn eine Goroutine fertig ist).

`wg.Wait()` blockiert, solange der interne Zähler größer als 0 ist.

[EQ] Was passiert, wenn der interne Zähler einer `sync.WaitGroup` negativ wird?

[EQ] Schauen Sie sich das erste Beispiel im
[Artikel "Golang sync.WaitGroup: Powerful, but tricky"](https://wundergraph.com/blog/golang-wait-groups)
an und skizzieren Sie, wie man eine `sync.WaitGroup` verwendet.

[EQ] In der Version 1.25 wurde eine neue Methode hinzugefügt: `WaitGroup.Go()`.
Schauen Sie sich die 
[Dokumentation](https://pkg.go.dev/sync#WaitGroup.Go)
und/oder den 
[Quellcode](https://cs.opensource.google/go/go/+/refs/tags/go1.25.2:src/sync/waitgroup.go;l=235)
der neuen Methode und erklären Sie, was diese tut.


### Programmieren

[ER] Schreiben Sie ein Programm, das 5 Goroutinen startet.
Jede Goroutine soll `"Worker X done"` (mit X = 0 bis 4) ausgeben.
Verwenden Sie eine `sync.WaitGroup`, um sicherzustellen, dass das Hauptprogramm erst
`"All done"` ausgibt, wenn alle Goroutinen abgeschlossen sind.

[EC] Führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 20 min -->

[WARNING]
`wg.Add(1)` muss immer **vor dem Start** der entsprechenden Goroutine aufgerufen werden.

Wird es erst danach oder gleichzeitig aufgerufen, kann es passieren, dass der Aufruf nebenläufig
zum `wg.Wait()` erfolgt — möglicherweise sogar erst _nach_ dem `wg.Wait()`.
In diesem Fall würde auf die Goroutine nicht gewartet werden.
[ENDWARNING]
[ENDSECTION]

[SECTION::submission::information,snippet,trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

<!-- @PROGRAM_TEST_SKIP: reason="Concurrent execution order is non-deterministic" manual_test_required=true -->

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-sync-waitgroup.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-sync-waitgroup.go].
[ENDINSTRUCTOR]
