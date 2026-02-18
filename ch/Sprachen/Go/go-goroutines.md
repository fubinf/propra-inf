title: "Grundlagen von Go: Goroutinen"
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: go-functions
---

[SECTION::goal::idea,experience]
Ich habe meine ersten Goroutinen gestartet und verstanden, wie sich die Programmausführung ändert,
wenn Code nicht mehr streng sequenziell abläuft.
[ENDSECTION]


[SECTION::background::default]
Fast alle modernen Rechner sind mit Mehrkernprozessoren ausgestattet und bieten Möglichkeiten,
die wir als Programmierer_innen nutzen wollen.
Nicht-sequenzielle Programmierung erfolgt in Go mithilfe von __Goroutinen__ — unabhängigen Ausführungspfaden,
die jeweils eigene Aufgaben übernehmen.

__Anmerkung:__ Goroutinen allein reichen nicht aus, um echte nebenläufige Programme in Go zu schreiben;
sie leisten weder Kommunikation noch Synchronisation.
Sie sind jedoch der erste Schritt.
[ENDSECTION]


[TOC]


[SECTION::instructions::detailed]

### Teil 1: Die Praxis

Wir wollen simulieren, dass eine Aufgabe Zeit kostet und nicht sofort fertig ist.

[ER] Implementieren Sie eine Funktion `delayedGreeting(msg string)`, die zuerst 2 Sekunden wartet
(`time.Sleep(2 * time.Second)` und das benötigt `import time`) und danach die Zeichenkette `msg`
auf der Konsole ausgibt.

[ER] Schreiben Sie eine Funktion `testGo()`. Diese soll:

- `delayedGreeting("Hello world delayed!")` aufrufen.
  Setzen Sie das Schlüsselwort `go` vor diesen Aufruf.
- Direkt in der nächsten Zeile `fmt.Println("Hello world!")` aufrufen (ohne `go`).

[EQ] Rufen Sie `testGo()` in Ihrer `main`-Funktion auf.
Was beobachten Sie?

[FOLDOUT::Erklärung]
Das beobachtete Verhalten liegt daran, dass das Hauptprogramm (`main`) sich beendet, ohne auf die
nebenläufig gestartete Goroutine zu warten, die Sie durch den Aufruf
`go delayedGreeting("Hello world delayed!")` gestartet haben.
[ENDFOLDOUT]

[ER] Ergänzen Sie Ihre `main`-Funktion am Ende um eine Endlosschleife, damit das Programm nicht sofort beendet wird.
Später müssen Sie das Programm manuell mit `Strg+C` abbrechen.

Man muss nicht immer eine extra Funktion definieren, denn Go erlaubt das Starten von Goroutinen auch direkt mit anonymen
Funktionen (Lambdas).

[ER] Implementieren Sie eine Funktion `testGoLambda()`.
Starten Sie darin eine Goroutine mit einer anonymen Funktion: `go func() { ... }()`, wo zuerst zwei
Sekunden gewartet und danach `"Hello world delayed!"` auf der Kommandozeile ausgegeben wird.
Geben Sie außerdem `"Hello world!"` am Ende von `testGoLambda` aus.
Fügen Sie die Funktion `testGoLambda()` Ihrer `main`-Funktion hinzu:

```go
func main() {
    testGo()
    testGoLambda()
    ...
}
```

[EC] Führen Sie das Programm aus.
Warten Sie auf die Ausgaben und beenden Sie es dann manuell.

[EQ] In welcher Reihenfolge werden die Funktionen (`testGo`, `testGoLambda`, `delayedGreeting` und
die Lambda-Funktion) gestartet?

[EQ] In welcher Reihenfolge verlassen die vier Funktionen den Geltungsbereich (beenden ihre
Ausführung)?

<!-- time estimate: 30 min -->


### Teil 2: Was ist eine Goroutine genau?

Alle Go-Programme bestehen aus einer oder mehreren _Goroutinen_ — `main` läuft ebenfalls in einer Goroutine.
Der Aufruf `go someFunc()` startet die Funktion `someFunc` in einer neuen Goroutine und blockiert die
übergeordnete Goroutine nicht.

[NOTICE]
Oben mussten Sie `main` mit einer Endlosschleife blockieren, da die Beendung von `main` das Ende des
Programms bedeutet und alle laufenden Goroutinen automatisch abgebrochen werden.
[ENDNOTICE]


#### Sequentiell vs. Nebenläufig

__Sequentiell__: Ein Schritt nach dem anderen.
Wäre `delayedGreeting` ohne `go` aufgerufen worden, hätte das ganze Programm 2 Sekunden blockiert,
bevor `"Hello World"` ausgegeben worden wäre.

__Nebenläufig__: Durch das Schlüsselwort `go` wurde `delayedGreeting` in eine eigene Goroutine ausgelagert.
Das Hauptprogramm lief sofort weiter.

Intern führen Goroutinen ihren Code _sequentiell_ aus.
In Relation zueinander sind Goroutinen _nebenläufig_.

[NOTICE]
Parallelität ist ein Spezialfall von Nebenläufigkeit.
[ENDNOTICE]

[EQ] Nennen Sie ein Beispiel aus dem Alltag (außerhalb der IT), bei dem Aufgaben sequentiell
abgearbeitet werden müssen, und eines, bei dem Nebenläufigkeit sinnvoller ist.

<!-- time estimate: 10 min -->


#### Kernbegriffe

Für ein gutes Verständnis, was eine Goroutine ist, müssen Sie zuerst die folgenden Begriffe kennenlernen.
Stellen Sie sicher, dass Sie ein Bauchgefühl für die Bedeutung der Wörter haben, und springen Sie zurück
zu dieser Liste, falls Sie bei der weiteren Erklärung etwas nicht verstehen.

- __Thread__: Die kleinste Einheit der Programmausführung, die sich unabhängig verwalten lässt.
- __(Betriebssystem-)Kernel__: Das Herz eines Betriebssystems;
  hier werden Ressourcen wie Arbeitsspeicher und CPU verwaltet.
- __Kernelraum__: Der privilegierte Speicherbereich, in dem der Kernel läuft.
- __Benutzerraum__: Speicherbereich, in dem alle „normalen“ Benutzeranwendungen laufen.
- __Scheduler__: Ein Programm, das die Verwaltung von Threads übernimmt.
- __kooperativ__: Ein Thread kommt erst dann zur Ausführung, wenn ein anderer Thread seine Ausführung selbst pausiert.
- __präemptiv__: Der aktuell laufende Thread wird in gewissen Zeitabständen vom Scheduler unterbrochen, um anderen
  Threads Ausführung zu ermöglichen.
- __Stack__: Hier: ein „privater“ Speicherbereich eines Threads.

<!-- time estimate: 10 min -->


#### Goroutinen vs. Threads

Hier sammeln wir nun einige weitere Begriffe, die im Kontext von Nebenläufigkeit wichtig sind.

1. __Hardware-Threads__: Die logischen Kerne Ihrer CPU — die echten „Arbeiter“.
2. __OS-Threads__: Threads, die im _Kernel_ verwaltet werden.
   Sie sind relativ „teuer“ im Speicherverbrauch (Stacks zwischen 512 KB und 8 MB) und ihr Wechsel kostet Zeit,
   weil die Threads im _Benutzerraum_ laufen.
   Das Betriebssystem ordnet OS-Threads den Hardware-Threads zu.
3. __User Threads__: 
   Threads, die von einem _Scheduler_ im _Benutzerraum_ verwaltet werden — von einem externen Programm.
   Sie sind für das Betriebssystem komplett unsichtbar und leichter als OS-Threads, weil ihre Erzeugung
   und ihr Kontextwechsel keinen Sprung zwischen Kernel- und Benutzerraum benötigen.

In der Praxis begegnet man noch anderen Bezeichnungen für Threads, die keine OS-Threads sind.
Diese werden heute oft synonym verwendet und sind im Grunde verschiedene Sorten von _User Threads_:

- __Green Threads__:
  Eine Implementierung von User Threads in der Standardbibliothek von Java 1.1, die mit Java 1.3 abgeschafft wurde.
  Sie teilten sich einen OS-Thread und waren größtenteils _kooperativ_.
- __Virtual Threads__: Eine modernere Implementierung von User Threads (Java 21).
  Virtual Threads benutzen das __M:N Mapping__:
  Die Laufzeit verteilt _M_ virtuelle Threads dynamisch auf _N_ OS-Threads.
  Im Gegensatz zu Green Threads ist das Scheduling hier (fast) __präemptiv__ — der Scheduler unterbricht die Ausführung
  eines Threads bei blockierenden Ein- und Ausgabeoperationen.
- __Goroutinen__: Eine komplett _präemptive_ Implementierung von Virtual Threads in Go.
  Eine Endlosschleife in einem Virtual Thread in Java würde den darunterliegenden OS-Thread komplett blockieren,
  in Go nicht.
  Außerdem sind die Stacks von Goroutinen zu Beginn sehr klein — nur 2 KB.

[FOLDOUT::Tiefenwissen: Scheduler Details]
Wenn Sie genau wissen wollen, wie der Go-Scheduler die Last verteilt („Work Stealing“), empfehlen wir die Artikel:
["Understanding the Go Scheduler"](https://rickkoch.github.io/posts/go-scheduler/)
oder
["Go's work-stealing scheduler"](https://rakyll.org/scheduler/).
Für unsere Aufgaben hier sind diese Quellen nicht nötig.
[ENDFOLDOUT]

<!-- time estimate: 15 min -->


### Verständnis-Check

Sie haben jetzt viel über Threads und Goroutinen gelesen.
Prüfen Sie kurz, ob das Konzept sitzt:

[EQ] __Szenario 1__:
Stellen Sie sich vor, Sie schreiben einen Chat-Server, der eine Million Nutzer gleichzeitig bedienen muss.
Für jeden Nutzer brauchen Sie einen eigenen „Arbeiter“ (Thread).
Warum würde Ihr Server wahrscheinlich abstürzen, wenn Sie dafür eine Million OS-Threads starten,
während er mit einer Million Goroutinen stabil läuft?

[HINT::Ich weiß nicht]
Wägen Sie die Situation in Bezug auf den Speicherverbrauch ab.
Wie viel Arbeitsspeicher benötigen OS-Threads im Gegensatz zu Goroutinen?
[ENDHINT]

[EQ] __Szenario 2__: In Ihrem Code oben haben Sie eine Goroutine gestartet, die nur wartet.
Angenommen, Sie schreiben stattdessen eine Goroutine, die ununterbrochen rechnet (`for { i++ }`).
Warum friert das Hauptprogramm dabei trotzdem nicht komplett ein?

[HINT::Ich weiß nicht]
Betrachten Sie noch einmal den Unterschied zwischen _kooperativ_ und _präemptiv_.
[ENDHINT]

<!-- time estimate: 15 min -->


### Zusammenfassung & Ausblick

Sie haben gelernt, dass `go func()` einen neuen Ausführungsstrang startet.
Sie haben aber auch das größte Problem der Nebenläufigkeit entdeckt: __Synchronisation__.

Wir mussten eine „dumme“ Endlosschleife (`for {}`) nutzen, damit `main` nicht zu früh beendet wird.
In echten Programmen verwenden wir dafür:

1. WaitGroups (um zu warten, bis Aufgaben fertig sind).
2. Channels (um Daten sicher zwischen Goroutinen auszutauschen).
3. Mutex (um gemeinsamen Speicher zu schützen).

Das lernen Sie in den nächsten Aufgaben.

<!-- TODO_2_Brandes: add teasers to go-channels, go-sync-mutex and go-sync-waitgroup once all four tasks are live -->
[ENDSECTION]


[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**
[PROT::ALT:go-goroutines.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei siehe hier:
[TREEREF::/Sprachen/Go/go-goroutines.go].
[ENDINSTRUCTOR]
