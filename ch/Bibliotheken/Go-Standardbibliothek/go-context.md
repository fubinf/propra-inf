title: "Go: das Paket 'context'"
stage: beta
timevalue: 1
difficulty: 2
assumes: go-channels, go-advanced-control-flow
---

[SECTION::goal::idea,experience]
Ich weiß, welche Funktionen das Paket `context` in Go zur Abbruchsteuerung, Fristenkontrolle und Wertübergabe in
nebenläufigen Programmen bietet.
[ENDSECTION]


[SECTION::background::default]
__Wie kann eine langlebige Goroutine abgebrochen werden?__

Eine Möglichkeit besteht darin, der Funktion einen Kanal wie `cancelChan` als Parameter
zu übergeben, über den signalisiert werden kann, ob die Goroutine beendet werden soll.

__Was ist, wenn eine Goroutine für ihre Aufgabe Daten benötigt?__

Diese können ebenfalls als Argumente an die Funktion übergeben werden.

__Aber was, wenn es viele solcher Goroutinen gibt?__

Deren Verwaltung wird zunehmend komplex und unübersichtlich.

Genau hier setzt das Paket `context` aus der Standardbibliothek an:
Es stellt Werkzeuge zur Übertragung von Abbruchsignalen und Fristen sowie zur Weitergabe
anfragespezifischer Werte bereit.
[ENDSECTION]

[TOC]


[SECTION::instructions::detailed]

### Übersicht

Lesen Sie die Abschnitte "Introduction", "Context" und "Derived contexts" im
[Artikel "Go Concurrency Patterns: Context" im Go Blog](https://go.dev/blog/context),
um die Fragen unten zu beantworten.

[EQ] Wie wird ein Kontext erzeugt, und wie lassen sich davon abgeleitete Kontexte mit veränderten
Eigenschaften erstellen?

[EQ] Eine Funktion empfängt einen `context.Context` und möchte einen Timeout von 2 Sekunden setzen, ohne den
ursprünglichen Kontext zu verändern.
Skizzieren Sie in einem Codeausschnitt, wie das geht.

<!-- time estimate: 15 min -->


### Übertragung von Abbruchsignalen

In diesem Abschnitt untersuchen Sie, wie sich das Abbrechen eines Kontexts auf von ihm
abgeleitete Kontexte auswirkt.

[ER] Schreiben Sie eine Funktion `doWork(parent context.Context, cancelMsg string) string`, um das Verhalten
abgeleiteter Kontexte zu untersuchen.
Die Funktion soll aus dem übergebenen Kontext `parent` einen eigenen abbrechbaren Kontext erzeugen, darauf warten, dass
dieser abgebrochen wird, und anschließend `cancelMsg` zurückgeben.

[HINT::Ich weiß nicht, wie ich auf das Abbruchsignal warten soll]
```go
<-ctx.Done()
```
[ENDHINT]

[NOTICE]
Wird ein Kontext an eine Funktion übergeben, so steht er konventionsgemäß als erster Parameter.
Korrigieren Sie das, falls Sie es in `doWork` anders gemacht haben.
[ENDNOTICE]

[WARNING]
Muss ich immer die CancelFunc aufrufen? Ja!
Sogar, wenn der Kontext nach Ablauf der Frist bereits abgebrochen ist,
gibt `cancel()` die zugehörigen Ressourcen frei und sollte daher stets aufgerufen werden.

Ein idiomatisches Beispiel wäre es, die CancelFunc direkt nach dem Erzeugen des Kontexts mittels `defer` aufzurufen:

```go
ctx, cancel := ...
defer cancel()
```
[ENDWARNING]

[ER] Implementieren Sie eine Funktion `myCancel`:

- Erzeugen Sie darin einen abbrechbaren Kontext;
- Starten Sie eine Goroutine, die eine Sekunde schläft (`time.Sleep(time.Second)`)
  und danach den Kontext abbricht;
- Übergeben Sie den Kontext sowie `"work canceled"` als `cancelMsg` an die Funktion `doWork()` und geben Sie ihren
  Rückgabewert auf der Kommandozeile aus.

[EQ] Wie verhalten sich verschiedene Kontexte zueinander im Falle eines Abbruchs?
Beziehen Sie sich dabei auf das Beispiel mit `doWork`.

[EQ] Schauen Sie sich die
[Dokumentation von `context.WithoutCancel()`](https://pkg.go.dev/context#WithoutCancel)
an und überlegen Sie, in welchen Situationen ein solcher Kontext hilfreich sein könnte.

<!-- time estimate: 15 min -->


### Übertragung von Fristen

In diesem Teil lernen Sie die Funktion `context.WithTimeout` praktisch kennen.

[ER] Implementieren Sie eine Funktion `myTimeout`:

- Erzeugen Sie darin einen abbrechbaren Kontext, der automatisch nach einer Sekunde abläuft
  (abgebrochen wird);
- Übergeben Sie diesen Kontext an die Funktion `doWork()` und geben Sie deren Rückgabewert
  auf der Kommandozeile aus;
- Verwenden Sie als `cancelMsg` die Zeichenkette `"work timed out"`.

[EQ] Was ist der Unterschied zwischen `context.WithTimeout` und `context.WithDeadline`?
Wie lässt sich die eine Funktion durch die andere ersetzen?

<!-- time estimate: 10 min -->


### Übertragung von Schlüssel-Wert-Paaren

Jeder Kontext kann Schlüssel-Wert-Paare speichern.
Die Funktion `context.WithValue()` dient dazu, anfragebezogene Daten entlang der Aufrufkette
weiterzugeben, ohne sie an jede Funktionssignatur anhängen zu müssen.

[EQ] Schauen Sie sich den
[Artikel "Context abuse"](https://boldlygo.tech/archive/2025-04-10-context-abuse/)
an. 
Geben Sie ein Beispiel für "user-specific configuration" an, die man im Kontext speichern sollte.
Geben Sie ein (eigenes) Beispiel an für einen optionalen Parameter, den man nicht dort speichern sollte.

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

**Wichtig:** `requestId` muss über den Kontext übergeben werden!

```go
[INCLUDE::include/go-context-logging-snippet.go]
```

[HINT::Ich weiß nicht, wie ich die `requestId` von `any` wieder zu `string` umwandle]
Das erfolgt mittels _Typzusicherung_ (Type Assertion):

```go
someString, ok := maybeString.(string)
```

Dieses Wissen können Sie in den Aufgaben [PARTREF::go-interfaces] und [PARTREF::go-advanced-control-flow] auffrischen.
[ENDHINT]

Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen:

```go
func main() {
    myCancel()
    myTimeout()
    simulateRequest()
}
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-context.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-context.go].
[ENDINSTRUCTOR]
