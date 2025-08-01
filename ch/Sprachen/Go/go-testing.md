title: Testen in Go
stage: draft
timevalue: 2
difficulty: 2
---

https://blog.jetbrains.com/go/2022/11/22/comprehensive-guide-to-testing-in-go/

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


### Überblick

Das Kommando `go test` hat folgende Voraussetzungen:

1. es muss ein Modul geben;
2. alle Test-Funktionen müssen sich in `*_test.go`-Dateien befinden;
3. alle Test-Funktionen müssen mit `Test`, `Benchmark` oder `Fuzz` anfangen.

Nach Konvention werden alle Funktionen aus `foo/foo.go` in einer Datei 
`foo/foo_test.go` getestet.


#### Cleanup

#### Parallel


### Benchmarks


### Fuzzing


[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
[ENDINSTRUCTOR]
