title: "Grundlagen von Go: Goroutinen"
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: go-functions
---

[SECTION::goal::idea,experience]
Ich habe Goroutinen kennengelernt und mein erstes nichtsequentielles Programm 
in Go geschrieben.
[ENDSECTION]

[SECTION::background::default]
Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet — eine Ressource, 
die wir als Programmierer_innen nicht ungenutzt lassen sollten.
Wer seine Software auf nur einem Kern ausführt, verschenkt wertvolle Rechenleistung 
und bremst die eigene Anwendung unnötig aus.

Nicht-sequentielle Programmierung erfolgt in Go mithilfe von __Goroutinen__ — 
unabhängigen Ausführungspfaden, die jeweils eigene Aufgaben übernehmen.
In dieser Aufgabe lernen Sie die Goroutinen kennen.
[ENDSECTION]

[SECTION::instructions::detailed]

[FOLDOUT::Was ist Nebenläufigkeit und was ist Parallelität?]
**Parallele Ausführung:** Das bedeutet, dass die einzelnen Befehle der Programme 
tatsächlich gleichzeitig auf mehreren CPU-Kernen ausgeführt werden. 
Dadurch wird echte Gleichzeitigkeit erreicht.

**Nebenläufige Ausführung:** In diesem Fall werden die Programme abwechselnd auf 
einem CPU-Kern ausgeführt.
Obwohl sie nicht wirklich gleichzeitig laufen, erscheint der Ablauf dennoch 
"parallel", da die Umschaltung zwischen den Programmen schnell genug erfolgt, um 
den Eindruck von Gleichzeitigkeit zu erwecken.
[ENDFOLDOUT]

### Goroutinen

Eine Goroutine ist ein leichtgewichtiger ("grüner") Thread.
Solche Goroutinen sind bezüglich der Laufzeiteffizienz extrem billig: 
Millionen von Goroutinen können nebeneinander ausgeführt werden.

Eine neue Goroutine wird mit dem Schlüsselwort `go` erzeugt.
Diese braucht keine besondere Verwaltung — sie wird automatisch von dem 
Scheduler zum Laufen gebracht und automatisch aufgeräumt, sobald die darin 
laufende Funktion ihre Aufgabe beendet hat.

[ER] Implementieren Sie eine Funktion `delayedGreeting(msg string)`, die zuerst 
2 Sekunden schläft und anschließend eine Zeichenkette auf die Kommandozeile ausgibt.

[ER] Implementieren Sie auch eine andere Funktion namens `testGo()`, wo Sie zuerst 
`go delayedGreeting("Hello world delayed!")` und in der nächsten Zeile 
`fmt.Println("Hello world!")` aufrufen.

[ER] Rufen Sie die Funktion `testGo()` aus der `main`-Funktion auf und blockieren 
Sie `main` mittels einer Endlosschleife.
Später lernen Sie bessere Synchronisierungsmöglichkeiten, aber für jetzt reicht 
ein `for {}` völlig aus.

<!-- time estimate: 5 min -->

Für manche kann das ein bisschen umständlich scheinen — 
immer zuerst eine neue Funktion definieren zu müssen.
Zum Glück ist das nicht nötig, denn Go erlaubt das Wort `go` auch für 
"lambda"-Funktionen.

[ER] Implementieren Sie eine andere Funktion `testGoLambda()`, die prinzipiell 
das Gleiche tut wie `testGo()`, jedoch mit einem Unterschied — die Funktion 
`delayedGreeting(msg string)` soll zu einer Lambda-Funktion umgewandelt werden.
Die auszugebende Zeichenkette bleibt gleich — `"Hello world delayed!"`. 

[ER] Fügen Sie `testGoLambda()` ebenfalls in Ihre `main()`-Funktion ein.

[EC] Führen Sie Ihr Programm aus, warten Sie ab, bis alle Funktionen beendet wurden,
und unterbrechen Sie die Endlosschleife per `Ctrl+C`.

<!-- time estimate: 5 min -->

Diskutieren Sie:

[EQ] In welcher Reihenfolge werden die Funktionen (`testGo`, `testGoLambda`, 
`delayedGreeting` und die lambda-Funktion) gestartet?

[EQ] In welcher Reihenfolge verlassen die vier Funktionen den Geltungsbereich 
(beenden ihre Ausführung)?

<!-- time estimate: 10 min -->

[FOLDOUT::Wie werden Goroutinen verwaltet?]
__Diese Information liegt vollständig außerhalb des Umfangs dieser Aufgabe.__

Falls Sie sich jedoch besonders für Go interessieren und genauer verstehen möchten,
wie Goroutinen intern funktionieren, gibt es zwei empfehlenswerte Quellen
(betreten auf eigene Gefahr!):

* <!-- LINK_CHECK: status=403 -->
  [Kurze Version](https://medium.com/@hatronix/inside-the-go-scheduler-a-step-by-step-look-at-goroutine-management-1a8cbe9d5dbd)
* <!-- LINK_CHECK: status=403 -->
  [Lange Version](https://medium.com/@sanilkhurana7/understanding-the-go-scheduler-and-looking-at-how-it-works-e431a6daacf)
[ENDFOLDOUT]
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

<!-- @PROGRAM_TEST_SKIP: reason="Infinite loop program, requires manual interruption" manual_test_required=true -->

[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**
[PROT::ALT:go-goroutines.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier:
[TREEREF::/Sprachen/Go/go-goroutines.go].
[ENDINSTRUCTOR]

