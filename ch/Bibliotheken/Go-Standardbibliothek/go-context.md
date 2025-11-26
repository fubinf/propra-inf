title: "Go: das Paket 'context'"
stage: draft
timevalue: 1.5
difficulty: 2
assumes: go-channels, go-advanced-control-flow
---

[SECTION::goal::idea,experience]
Ich weiß, welche Funktionen das Paket `context` in Go zur Verwaltung von Goroutinen bietet.
[ENDSECTION]

[SECTION::background::default]
__Wie kann eine langlebige Goroutine abgebrochen werden?__

Eine Möglichkeit besteht darin, der Funktion einen Kanal wie `cancelChan` als Parameter
zu übergeben, über den signalisiert werden kann, ob die Goroutine beendet werden soll.

__Was ist, wenn eine Goroutine für ihre Aufgabe Daten benötigt?__

Diese können ebenfalls als Argumente an die Funktion übergeben werden.

__Aber was, wenn es viele solcher Goroutinen gibt?__

Deren Verwaltung wird zunehmend komplex und unübersichtlich.

Genau hier setzt das Paket `context` an — ein Modul aus der Standardbibliothek, 
das Werkzeuge zur Übertragung von Abbruchsignalen und Fristen sowie zur Weitergabe 
anfragespezifischer Werte bereitstellt.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Übersicht

Lesen Sie die Abschnitte "Introduction", "Context" und "Derived contexts" im 
[Artikel "Go Concurrency Patterns: Context" im Go Blog](https://go.dev/blog/context),
um die Fragen unten zu beantworten.

[EQ] Welche Methoden sind im Interface `context.Context` definiert und was sind 
jeweils ihre Funktionen?

[EQ] Wie wird ein Kontext erzeugt?

[EQ] Wie werden Teile eines Kontexts modifiziert?

<!-- time estimate: 15 min -->


### Übertragung von Abbruchsignalen

In diesem Abschnitt untersuchen Sie, wie sich das Abbrechen eines Kontexts auf von ihm 
abgeleitete Kontexte auswirkt.

[ER] Schreiben Sie eine Funktion `doWork(parent context.Context, cancelMsg string) string`,
die aus dem übergebenen Kontext `parent` einen eigenen Kontext erzeugt, darauf wartet, 
dass dieser abgebrochen wird, und anschließend `cancelMsg` auf der Kommandozeile ausgibt.

[ER] Implementieren Sie eine Funktion `testCancel`:

- Erzeugen Sie darin einen abbrechbaren Kontext;
- Starten Sie eine Goroutine, die eine Sekunde schläft (`time.Sleep(time.Second)`) 
  und danach den Kontext abbricht; 
- Übergeben Sie den Kontext an die Funktion `doWork()` und geben Sie deren Rückgabewert 
  auf der Kommandozeile aus;
- Übergeben Sie außerdem die Zeichenkette `"work canceled"` als `cancelMsg`.

[ER] Rufen Sie die Funktion `testCancel` in Ihrer `main`-Funktion auf. 

[EQ] Wie verhalten sich verschiedene Kontexte zueinander im Falle eines Abbruchs?
Beziehen Sie sich dabei auf das Beispiel mit `doWork`.

[EQ] Schauen Sie sich die 
[Dokumentation von `context.WithoutCancel()`](https://pkg.go.dev/context#WithoutCancel)
an und überlegen Sie, in welchen Situationen ein solcher Kontext hilfreich sein könnte.

[NOTICE]
Wird ein Kontext an eine Funktion übergeben, so steht er konventionsgemäß als erster Parameter.
[ENDNOTICE]

[HINT::Ich weiß nicht, wie ich auf das Abbruchsignal warten soll]
```go
select {
    case <-ctx.Done(): ...
}
```
[ENDHINT]

<!-- time estimate: 20 min -->


### Übertragung von Fristen

In diesem Teil lernen Sie die Methode `context.WithTimeout` praktisch kennen.

[ER] Implementieren Sie eine Funktion `testTimeout`:

- Erzeugen Sie darin einen abbrechbaren Kontext, der automatisch nach einer Sekunde abläuft 
  (abgebrochen wird);
- Übergeben Sie diesen Kontext an die Funktion `doWork()` und geben Sie deren Rückgabewert
  auf der Kommandozeile aus;
- Verwenden Sie als `cancelMsg` die Zeichenkette `"work timed out"`.

[ER] Rufen Sie die Funktion `testTimeout` in Ihrer `main`-Funktion auf.

[EQ] Was ist der Unterschied zwischen `context.WithTimeout` und `context.WithDeadline`?
Wie lässt sich die eine Funktion durch die andere ersetzen?

[HINT::Mich stört die Warnung, dass die CancelFunc ignoriert wird]
Weisen Sie die CancelFunc einer Variable zu (beispielsweise `cancel`) und rufen Sie 
sie mittels `defer` auf:

```go
ctx, cancel := ...
defer cancel()
```

Da `defer` erst beim Verlassen der Funktion ausgeführt wird — also nachdem 
der Kontext bereits abgebrochen wurde — ändert dieser Aufruf nichts an der Logik des Programms.
[ENDHINT]

<!-- time estimate: 10 min -->


### Übertragung von Schlüssel-Wert-Paaren

Jeder Kontext kann Schlüssel-Wert-Paare speichern.
Die Funktion `context.WithValue()` dient dazu, anfragebezogene Daten entlang der Aufrufkette 
weiterzugeben, ohne sie an jede Funktionssignatur anhängen zu müssen.

[EQ] Schauen Sie sich den Artikel 
["Context abuse"](https://boldlygo.tech/archive/2025-04-10-context-abuse/)
an und erläutern Sie kurz, wie man entscheiden kann, ob bestimmte Daten im Kontext 
gespeichert werden sollten oder nicht. 

[EQ] Lesen Sie den
[Artikel "Context value key collisions"](https://boldlygo.tech/archive/2025-05-23-context-value-key-collisions/)
und schildern Sie das Problem mit eigenen Worten.

[EQ] Lesen Sie zusätzlich die folgenden zwei Artikel:

  - ["Unexported context key types"](https://boldlygo.tech/archive/2025-05-27-unexported-context-key-types/)
  - ["String context keys"](https://boldlygo.tech/archive/2025-06-10-string-context-keys/)

und erläutern Sie, wie sich das zuvor beschriebene Problem vermeiden lässt.

[ER] Sie erhalten nun eine Vorlage mit sehr einfacher Logik zur Auftragsverarbeitung. 
Implementieren Sie die Funktionen `withRequestId` und `getRequestId` (denken Sie dabei an geeignete 
Schlüsseltypen) und rufen Sie die Funktion `simulateRequest` am Ende Ihrer `main`-Funktion auf.

```go
[INCLUDE::include/go-context-logging-snippet.go]
```

Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen:
```go
func main() {
    testCancel()
    testTimeout()
    simulateRequest()
}
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 25 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

<!-- @PROGRAM_TEST -->

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-context.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-context.go].
[ENDINSTRUCTOR]
