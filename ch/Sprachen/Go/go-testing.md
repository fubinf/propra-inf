title: Testen in Go
stage: draft
timevalue: 2.5
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich weiß, welche Optionen Go-Standardbibliothek für Testen anbietet.
[ENDSECTION]

[TOC]

[SECTION::background::default]
Eine der Stärken von Go ist das eingebaute Test-Framework.

In dieser Aufgabe lernen Sie, wie man Unit-Tests, Fuzzing Tests und 
Benchmarks mithilfe von der Standardbibliothek schreibt.
[ENDSECTION]

[SECTION::instructions::detailed]

[NOTICE]
In dieser Aufgabe geht es nur um das Technische, nämlich um "wie schreibe ich Tests?".

Falls Sie sich Fragen wie beispielsweise "wie schreibt man **gute** Tests?" oder 
"**was** soll man testen?" stellen, ist das Kapitel [PARTREF::Testen] genau für Sie da.
[ENDNOTICE]


### Überblick

Das Kommando `go test` hat folgende Voraussetzungen:

1. der zu testende Quellcode sowie Tests befinden sich in einem Modul 
  ([PARTREFMANUAL::go-modules::hier] gibt es eine Aufgabe, wo Sie mehr zu Modulen 
  lernen können);
2. alle Testfunktionen müssen sich in `*_test.go`-Dateien befinden;
3. alle Testfunktionen müssen mit `Test`, `Benchmark` oder `Fuzz` anfangen;
4. je nach Art des Tests muss die Testfunktion unterschiedliche Parameter annehmen:
    - `func TestSomething(t *testing.T)` für Unit-Tests*;
    - `func FuzzSomething(f *testing.F)` für Fuzz-Tests;
    - `func BenchmarkSomething(b *testing.B)` für Benchmarks.

Nach Konvention werden alle Funktionen aus `foo/foo.go` in einer Datei 
`foo/foo_test.go` getestet.

[NOTICE]
"Unit-Test" ist kein technischer Begriff, sondern eine Art von Tests, die die
Funktionalität eines in sich abgeschlossenen Moduls überprüfen.

Wir benutzen hier den Begriff "Unit-Test", um diese Funktionalität des Test-Frameworks
klar von Fuzzing-Tests und Benchmarks zu unterscheiden.

Es ist absolut möglich und normal, auch andere Arten von Tests mithilfe von `*testing.T`
zu implementieren.
[ENDNOTICE]

### Unit-Tests


So könnte ein simpler Unit-Test aussehen:

```go
func TestSomeFunction(t *testing.T) {
    input := ...
    expectedOutput := ...
    actualOutput := someFunction(input)
    
    if expectedOutput != actualOutput {
        t.Fatalf("expected %v, got %v\n".expectedOutput, actualOutput)
    }
}
```

[EQ] recherchieren Sie, was die folgenden Funktionen jeweils machen:

- `t.Log()`
- `t.Fail()`
- `t.Error()`
- `t.FailNow()`
- `t.Fatal()`


#### Run() und Parallel()

`testing.T` und `testing.B` verfügen über die Methode `Run()`.

Bei Unit-Tests ermöglicht dies strukturiertes Testen: Ein Test A darf aus den Tests 
B, C und D bestehen.
Falls einer der Tests B, C oder D nicht erfolgreich war, so gilt auch der Test A 
als nicht erfolgreich.

Benchmarks sind aber immer erfolgreich — `Run` wird ausschließlich für Lesbarkeit benutzt.

Tests können auch parallelisiert ausgeführt werden: das gewährleisten jeweils Methoden
`(*testing.T).Parallel()` und `(*testing.B).RunParallel()`.

Beispiel:

```go
func TestStuffInParallel(t *testing.T) {
    t.Run("Test 1", func(t *testing.T) {
        t.Parallel()    // registriert diesen Test für parallele Ausführung
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

func BenchmarkStuffInParallel(b *testing.B) {
    b.RunParallel(func(pb *testing.PB) {
        for pb.Next() {
            someExpensiveOperation()
        }       
    })
}
```

[NOTICE]
Im Falle von Unit-Tests fördert strukturierte Nebenläufigkeit das strukturierte Testen.
[ENDNOTICE]


#### Tabellengesteuerte Tests

Ein Sprachfeature, das sich sehr gut für tabellengesteuerte Tests eignet, sind
**anonyme Strukturen**.

Schauen Sie sich diesen 
[Artikel über tabellengesteuerte Tests](https://dave.cheney.net/2019/05/07/prefer-table-driven-tests)
an und verstehen Sie, was tabellengesteuerte Tests sind.

[ER] Definieren Sie drei Testfälle für die Funktion `Reverse()` und schreiben Sie
einen Unit-Test, der diese drei Fälle testet.

Denken Sie daran, Ihre Testfälle zu benennen (beispielsweise durch Definition in 
einer `name:case`-Map) und mittels von `t.Run()` zu organisieren, sodass die 
Ausgabe im Terminal klar und verständlich ist.

```go
[INCLUDE::snippets/go-testing-tdt-snippet.go]
```

[EC] Führen Sie den Test mit `go test -v` aus.

`-v` steht für `verbose` — so können Sie genau sehen, welche Tests ausgeführt wurden.

#### Cleanup()

Die Funktion `t.Cleanup()` wird nach jedem Test ausgeführt.
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

[EQ] Welche anderen Anwendungen von der Funktion `Cleanup()` fallen Ihnen ein?


### Fuzzing

Fuzzing ist eine Testingmethode, welche durch eine enorme Menge von zufällig 
generierten Eingaben Ausführungszweige in einer Funktion finden.
So lassen sich Randfälle finden, die beim Unit-Testing oft übersehen werden.

Diese Testingmethode ist besonders beliebt bei Testen von High Availability Systems 
und Computersicherheit.

Überfliegen Sie dieses 
[Tutorial: Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz)
.

[NOTICE]
Fun fact: Für die Funktion `Reverse(s string) string` aus dem Tutorial haben Sie unter
"Tabellengesteuerte Tests" bereits einen Unit-Test geschrieben.
[ENDNOTICE]

[EQ] Wofür wird im Tutorial getestet?
Welche gewünschten Eigenschaften der Funktion `Reverse(s string)` mussten zuerst 
identifiziert werden, um die Defekte aufzudecken?

[HINT::Eigenschaften]
Eine der Eigenschaften wäre `Reverse(Reverse(s)) == s`.

Gibt es noch welche?
[ENDHINT]

Lesen Sie diese 
[Anleitung: Go Fuzzing](https://go.dev/doc/security/fuzz/)
.

[ER] Schreiben Sie einen Fuzz-Test für die folgende Funktion.
Die Testfunktion soll `FuzzTrimSpaces` heißen. 

```go
[INCLUDE::snippets/go-testing-fuzzing-snippet.go]
```

[HINT::Eigenschaften]
Falls Sie nicht wissen, wo Sie mit dem Test anfangen sollen:

Welche Eigenschaften soll die Funktion `TrimSpaces` erfüllen?
Können Sie einen Test schreiben, der sich genau um diese Eigenschaft kümmert? 
[ENDHINT]

[EC] Führen Sie den Test aus (`go test -fuzz FuzzTrimSpaces`) und geben Sie die 
Ausgabe im Kommandoprotokoll ab.

[NOTICE]
Falls `go test` beim Fuzzing eine Eingabe findet, für die der Test nicht erfolgreich ist,
wird diese automatisch im "seed corpus" gespeichert und immer bei den darauffolgenden 
`go test -fuzz` Aufrufen benutzt.

Wenn Sie das Fuzzing komplett neu ausführen wollen, löschen Sie das Verzeichnis
`testdata/fuzz/FuzzFunctionName`.
[ENDNOTICE]

[EQ] Woran liegt das Problem?
Welche Codezeile und wie würden Sie anpassen? 


### Benchmarks

Warum würde jemand überhaupt benchmarken wollen?

Dafür gibt es mehrere Gründe:

1. Leistungsfähigkeit verschiedener Algorithmen oder Datenstrukturen vergleichen;
2. Um die Baseline beim Optimieren festzulegen — ohne sie kann man am Ende nicht
   verifizieren, dass die Leistungsfähigkeit sich tatsächlich verbessert hat.

Generell ist Benchmarking die Antwort auf die Frage "soll ich lieber X oder Y benutzen?",
sofern es keine anderen Kriterien (beispielsweise Entwicklerfreundlichkeit, 
Lesbarkeit oder Robustheit) gibt.

Falls Sie eine Funktion benchmarken wollen, muss diese Funktion in einer Schleife 
`b.N` Iterationen durchlaufen:

```go
func BenchmarkSomeFunction(b *testing.B) {
    for range b.N {
        someFunction()
    }
}
```

Wenn Sie aber `go test` ausführen, passiert nichts.
Um die Benchmark-Funktionen auszuführen, muss der Flag `-benchmark` gesetzt werden:

- `go test -benchmark .` — alle Benchmarks in dem Modul ausführen;
- `go test -bench BenchmarkSomeFunction` — eine konkrete Benchmark ausführen;
- (genereller auch `go test -bench regexp`)
- `go test -bench . -benchmem` — Benchmark mit Statistiken zur Speicherbenutzung;
- `go test -bench . -benchtime 10s` — die Dauer einer Benchmark spezifizieren;
- `go test -bench . -count 5` — die komplette Benchmark fünfmal ausführen.

In der
[Dokumentation zu Testflags](https://pkg.go.dev/cmd/go#hdr-Testing_flags)
können Sie sich weitere Flags anschauen.

Alternativ können Sie im Terminal `go help testflag` ausführen.

[NOTICE]
Wenn Ihre Funktion zusätzlich Setup/Teardown braucht und Sie diese Zeit aus der Statistik
ausschließen wollen, können Sie den Timer manuell kontrollieren:

- `b.ResetTimer()` — nach dem initialen Setup
- oder `b.StopTimer()/b.StartTimer()` für komplexere Setup/Teardown-Prozesse
- `b.ReportAllocs()` um Statistik zur Speicherbenutzung einzuschließen 
(auch wenn der Flag nicht gesetzt wurde).
[ENDNOTICE]

[ER] Implementieren Sie eine Benchmark, die Lesezugriffe auf `map[string]int` 
und `map[int]int` vergleicht.

- Implementieren Sie zwei Funktionen: `func BenchmarkIntMap(b *testing.B)` 
  und `func BenchmarkStringMap(b *testing.B)`.
  Die Funktionen sollen zuerst die jeweiligen Maps definieren und mit `amountValues`
  Schlüssel-Wert-Paaren befüllen;
- vergessen Sie nicht, `b.ResetTimer()` nach der Initialisierung und vor dem 
  tatsächlichen Benchmarking aufzurufen;
- Lesen Sie in jeder Iteration der `b.N`-Schleife **alle** Werte aus.
  Die Werte dürfen mit der `_ = val` Schreibweise ignoriert werden;
- stellen Sie sicher, dass Ihre Benchmark fair ist: 
    - Schlüssel-Zeichenketten müssen während Initialisierung kreiert werden;
    - wenn Sie `string`-Schlüssel dann in Map als `m[keys[i]]` übergeben,
     machen Sie es genauso mit `int`-Schlüsseln; ansonsten ist `map[string]int`
     benachteiligt.

[EQ] Diskutieren Sie die Ergebnisse Ihrer Benchmark.
Ab welchem Wert von `amountValues` ist der Unterschied erkennbar?
Warum ist eine Option langsamer als die andere?


[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

- [EREFQ::1] — Dokumentation lesen;
- [EREFQ::2] — ein bisschen überlegen, muss nicht unbedingt mit der Musterlösung 
  übereinstimmen;
- [EREFQ::3] — wichtig, dass man zuerst definiert, was man testet;
- [EREFQ::4] — wahrscheinlich ist das der naheliegendste Fix, aber andere Optionen 
  sind auch valide, solange sie das Kernproblem beheben;
- [EREFQ::5] — wichtige Punkte sind:
    - `string` ist langsamer als `int`;
    - das liegt am Hashing.

**Kommandoprotokoll**
[PROT::ALT:go-testing.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go/go-testing.go]

[ENDINSTRUCTOR]
