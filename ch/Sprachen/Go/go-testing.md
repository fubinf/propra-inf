title: Testen in Go
stage: draft
timevalue: 2
difficulty: 3
assumes: go-arrays-and-slices, go-structs2
---

[SECTION::goal::idea,experience]
Ich weiß, welche Optionen Go-Standardbibliothek für Testen anbietet.
[ENDSECTION]

[TOC]

[SECTION::background::default]
Eine der Stärken von Go ist das eingebaute Test-Framework.

In dieser Aufgabe lernen Sie, wie man Unit-Tests, Fuzz-Tests und Benchmarks mithilfe der Standardbibliothek schreibt.
[ENDSECTION]

[SECTION::instructions::detailed]

[NOTICE]
In dieser Aufgabe geht es hauptsächlich um das Technische, nämlich um "wie schreibe ich Tests?".

Fragen wie beispielsweise "wie schreibt man **gute** Tests?" oder "**was** soll man testen?" werden im Kapitel
[PARTREF::Testen] beantwortet.
[ENDNOTICE]


### Überblick

Das Kommando `go test` hat folgende Voraussetzungen:

1. der zu testende Quellcode sowie Tests befinden sich in einem Modul; <!-- TODO_2_Brandes: 
   add a reference to go-modules once it's live -->
2. alle Testfunktionen müssen sich in `*_test.go`-Dateien befinden;
3. alle Testfunktionen müssen mit `Test`, `Benchmark` oder `Fuzz` anfangen;
4. je nach Art des Tests muss die Testfunktion unterschiedliche Parameter annehmen:
    - `func TestSomething(t *testing.T)` für Unit-Tests;
    - `func FuzzSomething(f *testing.F)` für Fuzz-Tests;
    - `func BenchmarkSomething(b *testing.B)` für Benchmarks.

Nach Konvention werden alle Funktionen aus `foo/foo.go` in einer Datei `foo/foo_test.go` getestet.

[NOTICE]
"Unit-Test" ist kein technischer Begriff, sondern eine Art von Tests, die die Funktionalität eines in sich
abgeschlossenen Moduls überprüfen.

Wir benutzen hier den Begriff "Unit-Test", um diese Funktionalität des Test-Frameworks klar von Fuzz-Tests und
Benchmarks zu unterscheiden.

Mithilfe von `*testing.T` können Sie auch andere Arten von Tests implementieren.
[ENDNOTICE]

<!-- time estimate: 5 min -->


### Unit-Tests

So könnte ein simpler Unit-Test aussehen:

```go
func TestSomeFunction(t *testing.T) {
    input := ...
    expectedOutput := ...
    actualOutput := someFunction(input)
    
    if expectedOutput != actualOutput {
        t.Fatalf("expected %v, got %v\n", expectedOutput, actualOutput)
    }
}
```

[EQ] Lesen Sie die [Dokumentation](https://pkg.go.dev/testing) und gruppieren Sie Methoden `t.Fail()`, `t.Error()`,
`t.FailNow()` und `t.Fatal()` in zwei Kategorien:

- Methoden, die einen Test sofort abbrechen;
- Methoden, die einen Test als fehlgeschlagen markieren, aber die Ausführung fortsetzen.

[EQ] Überlegen Sie:
In welchen Situationen kann es sinnvoll sein, einen Test nach einem Fehlschlag weiterlaufen zu lassen, statt ihn sofort
abzubrechen?

<!-- time estimate: 15 min -->


#### Cleanup()

Die Methode `t.Cleanup()` wird nach jedem Test ausgeführt.
Diese soll für das Aufräumen benutzt werden, beispielsweise so:

```go
func TestSomethingWithFiles(t *testing.T) {
    file, err := os.CreateTemp("", "test-*.txt")
    if err != nil {
        t.Fatal(err)
    }
    
    // aufräumen
    t.Cleanup(func() {
        os.Remove(file.Name())
    })
    
    // Tests durchführen
}
```

[EQ] Welche anderen Anwendungen der Methode `Cleanup()` fallen Ihnen ein?

<!-- time estimate: 5 min -->


#### Run() und Parallel()

`testing.T` verfügt über Methoden `Run()` und `Parallel()`.

Bei Unit-Tests ermöglicht die Methode `Run()` strukturiertes Testen:
Ein Test A darf aus den Tests B, C und D bestehen.
Schlägt einer der Tests B, C oder D fehl, so gilt auch der Test A als fehlgeschlagen.

Die Methode `Parallel()` wird zusammen mit der Methode `Run()` verwendet und registriert einen Test für parallele
Ausführung:

```go
func TestStuffInParallel(t *testing.T) {
    t.Run("Test 1", func(t *testing.T) {
        t.Parallel()
        ...
    })
    t.Run("Test 2", func(t *testing.T) {
        t.Parallel()        
        ...
    })
    t.Run("Test 3", func(t *testing.T) {
        t.Parallel()
        ...
    })
}
```

So können Sie die gesamte Ausführungszeit Ihrer Testsuite deutlich reduzieren.

<!-- time estimate: 5 min -->


#### Tabellengesteuerte Tests

Ein Sprachkonstrukt, das sich sehr gut für tabellengesteuerte Tests eignet, sind **anonyme Strukturen**.

Schauen Sie sich diesen 
[Artikel über tabellengesteuerte Tests](https://dave.cheney.net/2019/05/07/prefer-table-driven-tests)
an und verstehen Sie, was tabellengesteuerte Tests sind.

[ER] Definieren Sie drei Testfälle für die Funktion `Reverse()` und schreiben Sie einen Unit-Test, der diese drei Fälle
testet.
Denken Sie daran, Ihre Testfälle zu benennen (beispielsweise durch Definition in einer `name:case`-Map) und mittels
`t.Run()` zu organisieren, sodass die Ausgabe im Terminal klar und verständlich ist.

```go
[INCLUDE::include/go-testing-tdt-snippet.go]
```

[EC] Führen Sie den Test mit `go test -v` aus.
`-v` steht für `verbose` — so können Sie genau sehen, welche Tests ausgeführt wurden.

<!-- time estimate: 20 min -->


### Fuzzing

Fuzzing ist eine Testingmethode, welche durch eine enorme Menge von zufällig generierten Eingaben Ausführungszweige in
einer Funktion finden.
So lassen sich Randfälle finden, die beim Unit-Testing oft übersehen werden.

Diese Testingmethode ist besonders beliebt bei Testen von High Availability Systems und Computersicherheit.

Überfliegen Sie dieses 
[Tutorial: Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz)
und beantworten Sie die Fragen unten.

[EQ] Wofür wird im Tutorial getestet?
Welche gewünschten Eigenschaften der Funktion `Reverse(s string)` mussten zuerst identifiziert werden, um die Defekte
aufzudecken?

[HINT::Ich verstehe nicht, was für "Eigenschaften" gemeint sind]
Eine der Eigenschaften wäre `Reverse(Reverse(s)) == s`.

Gibt es noch welche?
[ENDHINT]

[ER] Lesen Sie diese
[Anleitung: Go Fuzzing](https://go.dev/doc/security/fuzz/)
und Schreiben Sie einen Fuzz-Test für die folgende Funktion, die Leerzeichen aus einer Zeichenkette vorne und hinten
entfernt (aus `"   some test string  "` wird `"some test string"`).
Die Testfunktion soll `FuzzTrimSpaces` heißen.

```go
[INCLUDE::include/go-testing-fuzzing-snippet.go]
```

[EC] Führen Sie den Test aus (`go test -fuzz FuzzTrimSpaces`) und geben Sie die Ausgabe im Kommandoprotokoll ab.
(Geben Sie die Ausgabe ab, die einen Defekt entdeckt! Wiederholen Sie den Test bei Bedarf.)

[NOTICE]
Falls `go test` beim Fuzzing eine Eingabe findet, für die der Test nicht erfolgreich ist, wird diese automatisch im
"seed corpus" gespeichert und immer bei den darauffolgenden Aufrufen von `go test` verwendet.

Solche Eingaben befinden sich im Verzeichnis `testdata/fuzz/FuzzFunctionName` (beispielsweise in
`testdata/fuzz/FuzzTrimSpaces/b0118fa98fb2891d`), das nach dem Test in Ihrem Modul erscheint.
Um die Tests komplett neu auszuführen, können Sie dieses Verzeichnis löschen.
[ENDNOTICE]

[EQ] Woran liegt das Problem?
Welche Codezeile und wie würden Sie anpassen?

<!-- time estimate: 30 min -->


### Benchmarking

Benchmarks sind Funktionen, die im Wesentlichen den folgenden zwei Zwecken dienen:

1. Die Leistungsfähigkeit verschiedener Algorithmen oder Datenstrukturen zu vergleichen;
2. Eine Baseline beim Optimieren festzulegen — ohne sie kann man am Ende nicht verifizieren, dass sich die
   Leistungsfähigkeit tatsächlich verbessert hat.

Generell liefert Benchmarking eine Antwort auf die Frage "soll ich lieber X oder Y benutzen?", sofern es keine
anderen Kriterien (beispielsweise Entwicklerfreundlichkeit, Lesbarkeit oder Robustheit) gibt.


#### Praxis

Falls Sie eine Funktion benchmarken wollen, muss diese Funktion in einer Schleife `b.N` Iterationen durchlaufen:

```go
func BenchmarkSomeFunction(b *testing.B) {
    for range b.N {
        someFunction()
    }
}
```

Benchmarks können auch parallel ausgeführt werden:

```go
func BenchmarkStuffInParallel(b *testing.B) {
    b.RunParallel(func(pb *testing.PB) {
        for pb.Next() {
            someExpensiveOperation()
        }
    })
}
```

Dabei werden `b.N` Iterationen automatisch über mehrere Goroutinen verteilt.

Um die Benchmark-Funktionen auszuführen, muss der Flag `-bench` gesetzt werden.
Hier ist eine kleine Auflistung von oft verwendeten Flags:

- `go test -bench .` — alle Benchmarks in dem Modul ausführen;
- `go test -bench BenchmarkSomeFunction` — eine konkrete Benchmark ausführen;
- (genereller auch `go test -bench regexp`, mehr zu regulären Ausdrücken in [PARTREF::RegExp])
- `go test -bench . -benchmem` — Benchmark mit Statistiken zur Speicherbenutzung (diese können Sie auch mit dem Aufruf
   `b.ReportAllocs()` anzeigen lassen);
- `go test -bench . -benchtime 10s` — die Dauer einer Benchmark spezifizieren;
- `go test -bench . -count 5` — die komplette Benchmark fünfmal ausführen.

(Weitere Flags lernen Sie in der
[Dokumentation zu Testflags](https://pkg.go.dev/cmd/go#hdr-Testing_flags)
oder im Terminal über `go help testflag` kennen.)

[NOTICE]
Wenn Ihre Funktion zusätzlich Setup/Teardown braucht und Sie diese Zeit aus der Statistik ausschließen wollen, können
Sie den Timer manuell kontrollieren:

- `b.ResetTimer()` — nach dem Setup;
- oder `b.StopTimer()/b.StartTimer()` für komplexere Setup/Teardown-Prozesse;
- `b.ReportAllocs()` um Statistik zur Speicherbenutzung einzuschließen (auch wenn der Flag nicht gesetzt wurde).
[ENDNOTICE]

[ER] Implementieren Sie eine Benchmark, die Lesezugriffe auf `map[string]int` und `map[int]int` vergleicht.

- Implementieren Sie zwei Funktionen: `func BenchmarkIntMap(b *testing.B)` und `func BenchmarkStringMap(b *testing.B)`.
  Die Funktionen sollen zuerst die jeweiligen Maps definieren und mit `amountValues` Schlüssel-Wert-Paaren befüllen;
- vergessen Sie nicht, `b.ResetTimer()` nach der Initialisierung und vor dem tatsächlichen Benchmarking aufzurufen;
- Lesen Sie in jeder Iteration **alle** Werte aus.
  Die Werte dürfen mit der `_ = val` Schreibweise ignoriert werden;
- stellen Sie sicher, dass Ihre Benchmark fair ist: 
    - Schlüssel-Zeichenketten müssen während Initialisierung kreiert werden;
    - wenn Sie `string`-Schlüssel dann in Map als `m[keys[i]]` übergeben, machen Sie es genauso mit `int`-Schlüsseln;
      ansonsten ist `map[string]int` benachteiligt.

[HINT::Wie erkenne ich, welche Option schneller ist?]
Die Standardausgabe einer Benchmark sieht folgendermaßen aus:

```bash
goos: darwin       # Betriebssystem
goarch: arm64      # CPU-Architektur
pkg: tests         # das Modul, wo die Tests ausgeführt wurden
cpu: Apple M1 Pro  # die konkrete CPU
# Funktionsname-Anzahl_CPU_Kerne     Anzahl Iterationen        Nanosekunden pro eine Iteration
BenchmarkIntMap-10                   24481357                  49.33 ns/op
```

Uns interessiert, wie viele Nanosekunden eine Operation/Iteration gedauert hat, also `49.33` im obigen Beispiel.
[ENDHINT]

[EC] Führen Sie die Benchmark mittels `go test -bench .` aus.

[EQ] Diskutieren Sie die Ergebnisse.
Welche Option ist schneller und warum?

<!-- time estimate: 30 min -->

[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

**Kommandoprotokoll**
[PROT::ALT:go-testing.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-testing.go].

[ENDINSTRUCTOR]
