title: "Grundlagen von Go: Kanäle (Channels)"
stage: alpha
timevalue: 1.25
difficulty: 2
assumes: go-goroutines, go-arrays-and-slices
---

[SECTION::goal::idea,experience]
Ich weiß, was Kanäle in Go sind und wie sie verwendet werden.
[ENDSECTION]

[SECTION::background::default]
Sie kennen bereits [PARTREFMANUAL::go-goroutines::Goroutinen] — leichtgewichtige 
Ausführungspfade, die parallel beziehungsweise nebenläufig auf verschiedenen Prozessorkernen 
oder Betriebssystem-Threads laufen können.

Das ist zwar praktisch, aber wie kommunizieren Goroutinen eigentlich miteinander?
Eine Möglichkeit wäre, gemeinsam genutzte Daten mit Mutexen zu schützen, um kritische Abschnitte
abzusichern.

Doch Go bietet dafür eine elegantere Lösung: __Kanäle__.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Übersicht

Ein Kanal ist eine typisierte (optional: gepufferte) Rohrleitung zwischen zwei Goroutinen.
Kanäle gehören zu _Mehrblocktypen_.

Schauen Sie sich die folgenden zwei Themen in "A Tour Of Go" an:

- ['Channels'](https://go.dev/tour/concurrency/2)
- ['Buffered Channels'](https://go.dev/tour/concurrency/3)

Vollziehen Sie die Beispielprogramme nach und machen Sie selber Änderungen, 
um die Fragen unten zu beantworten:

[EQ] Wie wird ein `int`-Kanal __deklariert__?

[EQ] Wie wird ein `int`-Kanal __definiert__?

[EQ] Wie wird ein `int`-Kanal mit einem Puffer von Größe 2 __definiert__?

[EQ] Was ist der Nullwert eines Kanals?

[EQ] Wie wird ein Wert aus einem Kanal __empfangen__?

[EQ] Wie wird ein Wert in einen Kanal __gesendet__?

[EQ] Wie lässt sich mit einem Kanal eine Verklemmung (Deadlock) erzeugen?

[NOTICE]
Wie bei Slices lassen sich auch bei Kanälen mit `cap` und `len` Informationen abfragen:

- `cap(ch)` gibt die Größe des Puffers an;
- `len(ch)` gibt die Anzahl der aktuell im Puffer befindlichen Elemente zurück.
[ENDNOTICE]

[WARNING]
Stellen Sie sicher, dass jeder Kanal nur an genau einer Stelle ausgelesen wird.
Wenn mehrere Goroutinen denselben Kanal konsumieren, entsteht leicht eine _Wettlaufsituation_ 
(Race Condition) — also eine Situation, in der der Programmablauf davon abhängt, welche Goroutine 
den gesendeten Wert erhält.
[ENDWARNING]

<!-- time estimate: 15 min -->


### Gerichtete Kanäle

Die Richtung eines Kanals kann bereits bei seiner Deklaration angegeben werden:

```go
var foo chan<- int          // nur senden
var bar <-chan int          // nur empfangen
var baz chan int            // senden und empfangen
```

Diese Spezifikation ist besonders in Funktionssignaturen nützlich, da sie die
Verantwortlichkeiten klar zwischen den Komponenten eines Systems trennt:

```go
func foo(c <-chan int) {
    // c kann hier nur zum Empfangen verwenden werden
}
```

[EQ] Würden Sie eine "gerichtete" Deklaration in der `main`-Funktion benutzen?
Begründen Sie.

<!-- time estimate: 5 min -->


### `range` und `close`

Lesen Sie das
[Thema 'Range and Close' in "A Tour fo Go"](https://go.dev/tour/concurrency/4).

[EQ] Warum kann ein Kanal geschlossen werden?

[EQ] Wie lässt sich überprüfen, ob ein Kanal geschlossen ist?

[EQ] Wie empfängt man mehrere Werte nacheinander aus einem Kanal?

[EQ] Was passiert, wenn in einen geschlossenen Kanal gesendet wird?

[EQ] Was passiert, wenn aus einem geschlossenen Kanal empfangen wird?

[WARNING]
Senden an sowie Empfangen von einem `nil`-Kanal blockiert immer.

Das Schließen eines bereits geschlossenen oder eines `nil`-Kanals führt zu `panic`.  
[ENDWARNING]

<!-- time estimate: 10 min -->


### `select`

`select` ist ein Sprachkonstrukt zur Koordination von Kanälen.

Im Kontext nebenläufiger Programmierung wirkt `select` wie eine _Barriere_:
Es besteht aus mehreren Zweigen (`case`-Anweisungen) und führt genau denjenigen aus,
der nicht blockiert, also zu diesem Zeitpunkt ausgeführt werden kann.

Optional kann ein `default`-Zweig angegeben werden, der nur dann ausgeführt wird,
wenn alle anderen Zweige blockieren würden.

Typischerweise wird `select` zur Synchronisation und Koordination von Kanälen verwendet.

Sehen Sie sich das 
[Thema 'Select' in "A Tour of Go"](https://go.dev/tour/concurrency/5)
an und führen Sie das Beispiel aus.

[EQ] Was passiert, wenn Sie dem `select` im Beispiel einen `default`-Zweig mit 
`fmt.Println("default")` hinzufügen?
Warum?

<!-- time estimate: 10 min -->


### Programmieren

[ER] Implementieren Sie eine Funktion `sender(c chan<- int)`, welche Zahlen von 0 bis 5 
in einen Kanal `c` sendet und danach den Kanal schließt.

[ER] Implementieren Sie eine Funktion `receiver(c <-chan int)`, die Werte aus `c` empfängt
und diese auf der Kommandozeile ausgibt.
Verwenden Sie dabei die Schreibweise, mit der überprüft wird, ob der Kanal noch geöffnet ist —
nur die validen Werte dürfen ausgegeben werden.

[ER] Implementieren Sie anschließend eine Funktion `testChannels()`, wo

* ein Kanal vom Typ `int` erstellt wird;
* `sender` und `receiver` nebenläufig aufgerufen werden;
* die `main`-Funktion für zwei Sekunden blockiert wird (`time.Sleep`).

[EC] Fügen Sie die Funktion `testChannels()` der `main`-Funktion hinzu und führen Sie
das Programm mittels `go run` aus.

<!-- time estimate: 15 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-channels.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-channels.go].
[ENDINSTRUCTOR]