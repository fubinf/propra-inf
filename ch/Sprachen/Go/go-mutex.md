title: "Go: sync.Mutex"
stage: draft
timevalue: 1
difficulty: 2
assumes: go-waitgroup
---

[SECTION::goal::idea,experience]
Ich weiß, was ein Mutex ist und wie Mutexe in Go verwendet werden. 
[ENDSECTION]

[SECTION::background::default]
Eine Möglichkeit zur Synchronisation sind _Mutexe_ — Sperrvariablen,
die dafür sorgen, dass immer nur eine Goroutine gleichzeitig auf bestimmte geteilte Daten
zugreifen kann.

In dieser Aufgabe geht es um Mutexe in Go: 
Welche Arten es gibt, wie und wo sie eingesetzt werden und welche Alternativen zur Verfügung stehen.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### `sync.Mutex`

Das Wort "Mutex" stammt von "mutual exclusion" — "gegenseitiger Ausschluss".

Ein Mutex dient dem Schutz des sogenannten _kritischen Abschnitts_ — eines Quellcodebereichs,
der jeweils nur von einem Prozess oder Thread gleichzeitig ausgeführt werden darf.

Solange eine Goroutine den Mutex hält, darf keine andere Goroutine den kritischen 
Abschnitt betreten.

Sehen Sie sich das 
[Beispiel "Go by Example: Mutexes"](https://gobyexample.com/mutexes)
an und beantworten Sie die Fragen unten.

[EQ] Welche Methoden von `sync.Mutex` werden im Beispiel verwendet, und wozu dienen sie?

[EQ] Was ist der Nullwert eines `sync.Mutex`?

[EQ] Wie würde sich die Funktionsweise des Beispielprogramms ändern, wenn `Container`
in `inc` per Wert übergeben worden wäre?
(`(c Container) inc(name string)` anstatt von `(c *Container) inc(name string)`)

<!-- time estimate: 10 min -->


### `sync.RWMutex`

Die Go-Standardbibliothek stellt mit `sync.RWMutex` eine feingranulare Alternative zum 
gewöhnlichen `sync.Mutex` bereit.

Diese Variante unterscheidet zwischen Lese- und Schreibzugriffen und bietet vier 
zentrale Methoden:

- Für Lesezugriffe: `RLock()` und `RUnlock()`;
- Für Schreibzugriffe: `Lock()` und `Unlock()`.

[EQ] Lesen Sie diese
[Antwort auf Stack Overflow](https://stackoverflow.com/questions/19148809/how-to-use-rwmutex/19168242#19168242) 
aufmerksam durch und erklären Sie selbst:
Welches Problem löst `sync.RWMutex`?

<!-- time estimate: 10 min -->


### `sync/atomic`

Eine Alternative zum Lock-Increment-Unlock-Zyklus ist das Paket `sync/atomic`.

Schauen Sie sich das
[Beispiel "Go by Example: Atomic Counters"](https://gobyexample.com/atomic-counters)
an und beantworten Sie die Fragen unten.

[EQ] Wie verwendet man eine _atomare Variable_?
Wie laufen die Lese- und Schreibzugriffe ab? 

[EQ] Wann würden Sie diese Option den Mutexen bevorzugen?

[HINT::Ich verstehe nicht, was "atomar" in diesem Kontext bedeutet]
Eine gute Erklärung finden Sie im
[Artikel "Atomare Operation" auf Wikipedia](https://de.wikipedia.org/wiki/Atomare_Operation).
[ENDHINT]

<!-- time estimate: 10 min -->


### Programmieren

[ER] Implementieren Sie eine Funktion namens `testCounter`.
Diese soll folgendes tun:

- einen Zähler mit 0 initialisieren und in einer `for`-Schleife eine Million Goroutinen starten, 
  welche den Zähler jeweils um 1 inkrementieren;
- die totale Ausführungszeit messen (`time.Now()` und `time.Since()` helfen Ihnen dabei);
- den Zähler sowie die Ausführungszeit auf die Kommandozeile ausgeben.
  Das Format soll folgendermaßen aussehen: `"testCounter - counter: %v, achieved in %v\n"`;
- Synchronisieren Sie die Goroutine mittels einer `sync.WaitGroup`.

[ER] Implementieren Sie eine Funktion mit dem Namen `testCounterMutex`.
Diese soll im Wesentlichen dasselbe tun, wie `testCounter`, allerdings muss in dieser Variante 
der kritische Abschnitt (Inkrementieren des Zählers) durch einen `sync.Mutex` geschützt werden.
Passen Sie die Ausgabe auf die Kommandozeile entsprechend an 
(`"testCounterMutex - counter: %v, achieved in %v\n"`).

[ER] Implementieren Sie anschließend eine Funktion `testCounterAtomic`.
Hier implementieren Sie dieselbe Funktionalität mithilfe einer `atomic.Int64`-Variable.
Passen Sie die Ausgabe auf die Kommandozeile an
(`"testCounterAtomic - counter: %v, achieved in %v\n"`).

[EC] Fügen Sie die drei Funktionen Ihrer `main`-Funktion hinzu und führen Sie 
das Programm mittels `go run` aus.

[EQ] Welche Implementierungen haben das richtige Ergebnis geliefert?

[EQ] Diskutieren Sie die Laufzeiteffizienz der drei Varianten.
Was ist die schnellste Implementierung und warum?
Was ist die schnellste _korrekte_ Implementierung?

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-mutex.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-mutex.go].
[ENDINSTRUCTOR]
