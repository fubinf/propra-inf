title: "Grundlagen von Go: Goroutinen"
stage: alpha
timevalue: 1
difficulty: 2
assumes: go-functions
---

[SECTION::goal::idea,experience]
Ich habe Goroutinen kennengelernt und mein erstes nichtsequentielles Programm in Go geschrieben.
[ENDSECTION]


[SECTION::background::default]
Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet — eine Ressource, die wir als
Programmierer_innen nicht ungenutzt lassen sollten.
Wer seine Software nur auf einem Kern ausführt, verschenkt wertvolle Rechenleistung und bremst die 
Anwendung unnötig.

Nicht-sequentielle Programmierung erfolgt in Go mithilfe von __Goroutinen__ — unabhängigen
Ausführungspfaden, die jeweils eigene Aufgaben übernehmen. 
In dieser Aufgabe lernen Sie Goroutinen kennen.

__Anmerkung:__ Goroutinen allein reichen nicht aus, um effektive nebenläufige Programme in Go zu
schreiben. 
Sie sind jedoch der erste Schritt, um die nicht-sequentielle Denkweise zu erlangen.

<!-- TODO_2_Brandes: add teasers to go-channels, go-sync-mutex and go-sync-waitgroup once all four tasks are live -->
[ENDSECTION]


[SECTION::instructions::detailed]

### Nebenläufigkeit vs. Parallelität

In der Programmierung werden häufig die Begriffe „nebenläufig“ und „parallel“ verwendet.
Beide Konzepte sind zentral, daher werden sie im Folgenden erläutert und voneinander abgegrenzt:

- __Sequentielle Ausführung:__ Alle Befehle eines Programms werden strikt nacheinander auf einem
  CPU-Kern ausgeführt.
- __Nebenläufige Ausführung:__ Aufgaben werden nicht sequentiell ausgeführt.
  Ein typisches Beispiel sind mehrere Threads (siehe [TERMREF::Thread] im Glossar), die abwechselnd 
  auf einem CPU-Kern laufen.
- __Parallele Ausführung:__ Einzelne Befehle oder Aufgaben werden gleichzeitig auf mehreren
  CPU-Kernen ausgeführt.
  Parallelität ist ein Spezialfall der Nebenläufigkeit.

[EQ] Geben Sie ein paar Beispiele aus dem Alltag, bei denen Sie Threads statt sequentiellem Code
verwenden würden.

Welche der folgenden Aussagen sind richtig?
Begründen Sie.

[EQ] _"Nebenläufige Ausführung setzt mehrere CPU-Kerne voraus."_

[EQ] _"Parallel ist immer nebenläufig."_

[EQ] _"Nebenläufig ist immer parallel."_

[EQ] _"Es ist unmöglich, die Leistung eines Programms auf einem CPU-Kern durch Threads zu
verbessern."_

<!-- time estimate: 10 min -->


### Thread-Taxonomie

Welche Threads gibt es?

Je nach Situation werden typischerweise folgende Arten von Threads erwähnt:

- __Hardware-Threads:__ Logische Kerne der CPU.
  Auch wenn die CPU nur 8 Kerne besitzt, kann es 16 Hardware-Threads geben (mehr dazu im
  [Wikipedia-Artikel „Simultaneous Multithreading“](https://de.wikipedia.org/wiki/Simultaneous_Multithreading)).
- __Kernel- bzw. OS-Threads:__ „Echte“ Threads, die vom Betriebssystem verwaltet werden.
  Sie werden den verfügbaren Hardware-Threads zugeordnet und ermöglichen echte Parallelität.
- __User-Threads:__ Threads, die von einem Programm oder einer Bibliothek im Benutzerraum verwaltet
  werden.
  Das Betriebssystem kennt sie nicht, daher ist echte Parallelität nicht möglich.
  Im Gegensatz zu OS-Threads ist Erzeugung und Kontextwechsel bei User-Threads viel billiger.

Auf einer feineren Ebene wird die Begrifflichkeit etwas inkonsistent: Man hört zusätzlich von
[_Green-Threads_](https://en.wikipedia.org/wiki/Green_thread)
und
[_virtuellen Threads_](https://en.wikipedia.org/wiki/Virtual_thread),
wobei die Abgrenzung immer schwieriger wird.

Das haben die Entwickler von Go rechtzeitig erkannt und als Folge den Begriff „Goroutine“
eingeführt.


### Goroutinen

Eine Goroutine ist ein leichtgewichtiger („grüner/virtueller“) [TERMREF::Thread].

Lesen Sie den
[Abschnitt „Goroutines“ auf der Webseite „Effective Go“](https://go.dev/doc/effective_go#goroutines)
und beantworten Sie die folgenden Fragen.

[EQ] Wie wird eine Funktion in einer neuen Goroutine ausgeführt?

[EQ] Was ist die Beziehung zwischen Goroutinen und OS-Threads?

[FOLDOUT::Wie werden Goroutinen verwaltet?]
Jede ausführbare Binärdatei, die vom Go-Compiler produziert wird, enthält neben dem Programm selbst
noch Komponenten der Laufzeitumgebung, beispielsweise Garbage Collector und _den Scheduler_.

Der Scheduler entscheidet:

- welche Goroutine wann ausgeführt wird,
- auf welchem OS-Thread dies geschieht,
- und wie die Last über alle CPU-Kerne verteilt wird.

Artikel
["Understanding the Go Scheduler: How Goroutines Are Managed"](https://rickkoch.github.io/posts/go-scheduler/)
und
["Go's work-stealing scheduler"](https://rakyll.org/scheduler/)
helfen Ihnen, das Scheduling genau zu verstehen.
[ENDHINT]

[ER] Implementieren Sie die Funktion `delayedGreeting(msg string)`, die zunächst 2 Sekunden wartet
und anschließend eine Zeichenkette auf die Kommandozeile ausgibt.

[ER] Implementieren Sie außerdem die Funktion `testGo()`, die
`go delayedGreeting("Hello world delayed!")` aufruft und in der nächsten Zeile
`fmt.Println("Hello world!")` ausgibt.

[ER] Rufen Sie `testGo()` aus der `main`-Funktion auf und blockieren Sie `main` mit einer
Endlosschleife. Für den Moment reicht ein `for {}` aus.

Für manche kann das umständlich wirken — immer zuerst eine neue Funktion definieren zu müssen. Zum
Glück ist das nicht nötig, denn Go erlaubt das Schlüsselwort `go` auch für anonyme (Lambda-)
Funktionen.

[ER] Implementieren Sie die Funktion `testGoLambda()`, die dasselbe tut wie `testGo()`, jedoch
`delayedGreeting` als anonyme Funktion definiert. Die auszugebende Zeichenkette bleibt
`"Hello world delayed!"`.

[ER] Fügen Sie `testGoLambda()` ebenfalls in Ihre `main()`-Funktion ein.

[EC] Führen Sie Ihr Programm aus, warten Sie, bis alle Funktionen beendet wurden, und unterbrechen
Sie die Endlosschleife per `Ctrl+C`.

Diskutieren Sie:

[EQ] In welcher Reihenfolge werden die Funktionen (`testGo`, `testGoLambda`, `delayedGreeting` und
die Lambda-Funktion) gestartet?

[EQ] In welcher Reihenfolge verlassen die vier Funktionen den Geltungsbereich (beenden ihre
Ausführung)?

<!-- time estimate: 30 min -->

[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


<!-- @program_test_skip: reason="Infinite loop program, requires manual interruption" manual_test_required=true -->

[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**
[PROT::ALT:go-goroutines.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier:
[TREEREF::/Sprachen/Go/go-goroutines.go].
[ENDINSTRUCTOR]
