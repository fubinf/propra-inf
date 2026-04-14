title: "Grundlagen von Go: Kanäle (Channels)"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: go-goroutines, go-arrays-and-slices
---

[SECTION::goal::idea,experience]
Ich weiß, was Kanäle in Go sind und wie sie verwendet werden.
[ENDSECTION]

[SECTION::background::default]
Sie kennen bereits [PARTREF2::go-goroutines::Goroutinen] — leichtgewichtige 
Ausführungspfade, die parallel beziehungsweise nebenläufig auf verschiedenen Prozessorkernen 
oder Betriebssystem-Threads laufen können.

Das ist zwar praktisch, aber wie kommunizieren Goroutinen eigentlich miteinander?
Eine Möglichkeit wäre, gemeinsam genutzte Daten mit Mutexen zu schützen, um kritische Abschnitte
abzusichern.

Doch Go bietet dafür eine elegantere Lösung: **Kanäle**.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Übersicht

Ein Kanal ist eine typisierte (optional: gepufferte) "Rohrleitung" zwischen Goroutinen.
Kanäle gehören zu den _Mehrblocktypen_.

Schauen Sie sich die folgenden zwei Themen in "A Tour Of Go" an:

- ['Channels'](https://go.dev/tour/concurrency/2)
- ['Buffered Channels'](https://go.dev/tour/concurrency/3)

Vollziehen Sie die Beispielprogramme nach und machen Sie selber Änderungen, 
um die folgenden Fragen zu beantworten. Geben Sie jeweils kommentarlos ein Beispiel an:

[EQ] Wie wird ein `int`-Kanal **deklariert**?

[EQ] Wie wird ein `int`-Kanal **initialisiert**?

[EQ] Wie wird ein `int`-Kanal mit einem Puffer von Größe 2 **definiert**?

[EQ] Was ist der Nullwert eines Kanals?

[EQ] Wie wird ein Wert aus einem Kanal **empfangen**?

[EQ] Wie wird ein Wert in einen Kanal **gesendet**?

[EQ] Wie lässt sich mit einem Kanal eine Verklemmung (Deadlock) erzeugen?

[HINT::Ich weiß nicht, was ein Deadlock ist und wie ein Deadlock entsteht]
Ein Deadlock entsteht, wenn eine Goroutine auf etwas wartet, das niemals eintreten wird.
Unter welchen Bedingungen blockiert ein Kanal beim Senden oder Empfangen?
[ENDHINT]

[NOTICE]
Wie bei Slices lassen sich auch bei Kanälen mit `cap` und `len` Informationen abfragen:

- `cap(ch)` gibt die Größe des Puffers an;
- `len(ch)` gibt die Anzahl der aktuell im Puffer befindlichen Elemente zurück.
[ENDNOTICE]

[WARNING]
Stellen Sie sicher, dass jeder Kanal nur an genau einer Stelle ausgelesen wird.
Wenn mehrere Goroutinen denselben Kanal konsumieren, entsteht leicht **nicht-deterministisches Verhalten** — 
also eine Situation, in der nicht vorhersehbar ist, welche Goroutine den gesendeten Wert erhält, was zu schwer
nachvollziehbaren Logikfehlern führen kann.

Für den Anfang empfiehlt sich ein Leser pro Kanal.
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
    // c kann hier nur zum Empfangen verwendet werden
}
```

[EQ] Würden Sie eine "gerichtete" Deklaration in der `main`-Funktion benutzen?
Begründen Sie.

[HINT::Ich bin verwirrt]
Überlegen Sie, welche Operationen auf einem Kanal möglich sind, der auf der obersten Ebene
explizit als `chan<- int` oder `<-chan int` deklariert ist.
[ENDHINT]

<!-- time estimate: 5 min -->


### `range` und `close`

Lesen Sie das
[Thema 'Range and Close' in "A Tour of Go"](https://go.dev/tour/concurrency/4).

[EQ] Warum kann ein Kanal geschlossen werden?

[EQ] Wie lässt sich überprüfen, ob ein Kanal geschlossen ist?

[EQ] Wie empfängt man mehrere Werte nacheinander aus einem Kanal?

[EQ] Was passiert, wenn in einen geschlossenen Kanal gesendet wird?

[EQ] Was passiert, wenn aus einem geschlossenen Kanal empfangen wird?

[HINT::Ich bin mir nicht sicher]
Für die letzten zwei Fragen bietet es sich an, ein kleines Programmchen zu schreiben und
die beschriebenen Aktionen auszuprobieren.
[ENDHINT]

[WARNING]
Senden an sowie Empfangen von einem `nil`-Kanal blockiert immer.

Das Schließen eines bereits geschlossenen oder eines `nil`-Kanals führt zu `panic`.
[ENDWARNING]

<!-- time estimate: 10 min -->


### `select`

`select` ist ein Sprachkonstrukt zur Koordination von Kanälen.
Es besteht aus mehreren Zweigen (`case`-Anweisungen) und führt davon immer einen aus,
der nicht blockiert, also zu diesem Zeitpunkt ausgeführt werden kann.
Optional kann ein `default`-Zweig angegeben werden, der nur dann ausgeführt wird,
wenn alle anderen Zweige blockieren würden.

Sehen Sie sich das 
[Thema 'Select' in "A Tour of Go"](https://go.dev/tour/concurrency/5)
an und führen Sie das Beispiel aus.

[EQ] Was passiert, wenn Sie dem `select` im Beispiel einen `default`-Zweig mit 
`fmt.Println("default")` hinzufügen?
Warum?

<!-- time estimate: 10 min -->


### Programmieren

[ER] Implementieren Sie eine Funktion `sender(c chan<- int, done chan<- bool)`, welche Zahlen von 0 bis 4
in einen Kanal `c` sendet, den Kanal `c` schließt und über den Kanal `done` Bescheid gibt, dass das Senden
beendet wurde.

[HINT::Was bedeutet hier "Bescheid geben"?]
Am Ende der Funktion soll ein Wert in den Kanal gesendet werden, beispielsweise `done <- true`.
Das ermöglicht dem Aufrufer die Synchronisation: Die Zeile `<-senderDone` in der Funktion `testChannels` würde
die Ausführung so lange blockieren, bis die Funktion `sender` fertig ist.
[ENDHINT]

[ER] Implementieren Sie eine Funktion `receiver(c <-chan int, done chan<- bool)`, die Werte aus `c` empfängt
und diese auf der Kommandozeile ausgibt.
Verwenden Sie dabei die Schreibweise, mit der überprüft wird, ob der Kanal noch geöffnet ist —
nur die validen Werte dürfen ausgegeben werden.
Sobald der Kanal `c` geschlossen wurde, soll die Funktion über den Kanal `done` Bescheid geben, dass sie ihre
Ausführung beendet.

[HINT::Ich weiß nicht, wie ich prüfe, ob der Kanal noch geöffnet ist]
Ein Empfang aus einem Kanal kann zwei Werte zurückgeben: den empfangenen
Wert und einen bool, der angibt, ob der Kanal noch offen ist: `v, ok := <-c`.
[ENDHINT]

[ER] Implementieren Sie anschließend eine Funktion `testChannels()`, wo

* ein Kanal vom Typ `int` erstellt wird;
* Kanäle `senderDone` und `receiverDone` vom Typ `bool` erstellt werden;
* `sender` und `receiver` nebenläufig aufgerufen werden;
* auf die Werte aus `senderDone` und `receiverDone` gewartet wird.

[EC] Fügen Sie die Funktion `testChannels()` der `main`-Funktion hinzu und führen Sie
das Programm mittels `go run` aus.

[NOTICE]
Wie verwendet man Kanäle zum Signalisieren **richtig**?

Kanäle wie `senderDone` und `receiverDone` dienen ausschließlich dazu, das Eintreten eines Ereignisses
zu signalisieren — die dabei übertragenen Daten sind irrelevant.
Für solche Fälle eignen sich Kanäle vom Typ `struct{}`, die leere Strukturen übertragen.
Da eine leere Struktur in Go keinen Speicherplatz belegt (0 Bytes), ist sie ideal für reines Signalisieren.
Mehr dazu in der Aufgabe [PARTREF::go-structs2].
[ENDNOTICE]

<!-- time estimate: 15 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

- [EREFQ::1] — [EREFQ::6] sind reine Syntax-Fragen, die ziemlich oberflächlich geprüft werden können.
- [EREFQ::7] — hier ist wichtig, dass die Studierenden verstehen, dass viele von Kanal-bezogenen Operationen blockieren.
- [EREFQ::8] — eine kleine Verständnisfrage, dass das Typsystem manchmal zu restriktiv sein kann.
- [EREFQ::9] — eher wichtig, da es um die Kommunikation zwischen Sender und Receiver geht.
  Diese zwei Rollen tauchen in Go ziemlich oft auf, besonders wenn die Rede von Kanälen ist.
- [EREFQ::10] und [EREFQ::11] — noch mehr Syntax-Fragen, keine strenge Kontrolle nötig.
- [EREFQ::12] und [EREFQ::13] — hier sollten die Studierenden einfach selber ausprobieren, ebenfalls
keine strenge Kontrolle nötig.
- [EREFQ::14] — die Studierenden müssen darauf gekommen sein, dass der `default`-Zweig nicht blockiert
  und deswegen so oft ausgeführt wird.

[EREFR::1], [EREFR::2] und [EREFR::3] dürfen ein bisschen von der Musterlösung abweichen, solange
die Ausgabe von [EREFC::1] mit dem Kommandoprotokoll übereinstimmt.

**Kommandoprotokoll**
[PROT::ALT:go-channels.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-channels.go].
[ENDINSTRUCTOR]