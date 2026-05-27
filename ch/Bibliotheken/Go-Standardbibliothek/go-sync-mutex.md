title: "Go: sync.Mutex"
stage: beta
timevalue: 1.25
difficulty: 3
assumes: go-sync-waitgroup
---

[SECTION::goal::idea,experience]
Ich kenne `sync.Mutex` und atomare Variablen in Go und kann einschätzen, wann welcher Mechanismus geeignet ist. 
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
der jeweils nur von einer Goroutine gleichzeitig ausgeführt werden darf.

Solange eine Goroutine den Mutex hält, darf keine andere Goroutine den kritischen 
Abschnitt betreten.

Sehen Sie sich das 
[Beispiel "Go by Example: Mutexes"](https://gobyexample.com/mutexes)
an und beantworten Sie die Fragen unten.

[EQ] Was ist der Nullwert eines `sync.Mutex`?

[EQ] Warum steht `defer c.mu.Unlock()` direkt hinter `c.mu.Lock()` im Beispiel? 
Was wäre die Folge, wenn man das Unlock erst am Funktionsende ohne `defer` schreibt und in der Mitte
eine _Panik_ auftritt?

[EQ] Wie und warum würde sich die Funktionsweise des Beispielprogramms ändern, wenn `Container`
in `inc` per Wert übergeben worden wäre?
(`(c Container) inc(name string)` anstatt von `(c *Container) inc(name string)`)

<!-- time estimate: 10 min -->


### `sync.RWMutex`

Die Go-Standardbibliothek stellt mit `sync.RWMutex` eine Variante bereit, die zwischen Lese- und Schreibzugriffen
unterscheidet und dadurch mehrere gleichzeitige Lesezugriffe erlaubt.

Diese Variante bietet _zwei_ Paare von Zugriffsmethoden:

- Für Lesezugriffe: `RLock()` und `RUnlock()`;
- Für Schreibzugriffe: `Lock()` und `Unlock()`.

[EQ] Lesen Sie diese
[Antwort auf Stack Overflow](https://stackoverflow.com/questions/19148809/how-to-use-rwmutex/19168242#19168242) 
aufmerksam durch und erklären Sie selbst:
Welches Problem löst `sync.RWMutex`?

[ER] Implementieren Sie eine Struktur `Config` mit den Feldern `mu sync.Mutex` und `data map[string]string` sowie
einer Methode `(c *Config) Read(key string) string`, die den Mutex sperrt (und am Ende freigibt!), den Wert für `key`
aus `data` ausliest und zurückgibt.
Fügen Sie unmittelbar vor dem `return` ein `time.Sleep(100 * time.Millisecond)` ein, um einen teuren Lesezugriff
zu simulieren.

[ER] Implementieren Sie eine Funktion `myMutex`, die eine Instanz von `Config` mit
`map[string]string{"theme": "dark"}` initialisiert, 5 Goroutinen startet, die gleichzeitig `c.Read("theme")` aufrufen,
und die Gesamtausführungszeit mit `time.Now()` und `time.Since()` misst und ausgibt.
Verwenden Sie eine [PARTREF2::go-sync-waitgroup::sync.WaitGroup] für die Synchronisierung der Goroutinen.

[EQ] Rufen Sie `myMutex` auf und notieren Sie die Ausführungszeit.
Was beobachten Sie, wenn Sie `sync.Mutex` durch `sync.RWMutex` und `Lock`/`Unlock`
entsprechend durch `RLock` und `RUnlock` austauschen?
Warum?

<!-- time estimate: 25 min -->


### `sync/atomic`

Für einfache Lese-, Schreib- und Update-Operationen auf einzelnen Variablen eignen sich _atomare Variablen_,
die von der Go-Standardbibliothek im Paket `sync/atomic` bereitgestellt werden.

Schauen Sie sich das
[Beispiel "Go by Example: Atomic Counters"](https://gobyexample.com/atomic-counters)
an und beantworten Sie die Fragen unten.

[EQ] Wie verwendet man eine _atomare Variable_?
Zeigen Sie anhand eines kurzen Codeausschnitts, wie man eine solche Variable deklariert und
wie Lese- und Schreibzugriffe aussehen.

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
- Synchronisieren Sie die Goroutinen mittels einer `sync.WaitGroup`.

[ER] Implementieren Sie eine Funktion mit dem Namen `testCounterMutex`.
Diese soll im Wesentlichen dasselbe tun wie `testCounter`, allerdings muss in dieser Variante 
der kritische Abschnitt (Inkrementieren des Zählers) durch einen `sync.Mutex` geschützt werden.
Passen Sie die Ausgabe auf die Kommandozeile entsprechend an 
(`"testCounterMutex - counter: %v, achieved in %v\n"`).

[ER] Implementieren Sie anschließend eine Funktion `testCounterAtomic`.
Hier implementieren Sie dieselbe Funktionalität mithilfe einer `atomic.Int64`-Variable.
Passen Sie die Ausgabe auf die Kommandozeile an
(`"testCounterAtomic - counter: %v, achieved in %v\n"`).

[EC] Rufen Sie die drei Funktionen in Ihrer `main`-Funktion auf und führen Sie 
das Programm mittels `go run` aus.

[EQ] Welche Implementierung liefert ein falsches Ergebnis und warum?

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
[PROT::ALT:go-sync-mutex.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-sync-mutex.go].
[ENDINSTRUCTOR]
