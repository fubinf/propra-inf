title: "Grundlagen von Go: Enums"
stage: alpha
timevalue: 0.75
difficulty: 2
assumes: go-structs1
---

[SECTION::goal::idea,experience]
Ich weiß, wie man in Go Aufzählungstypen (Enums) mithilfe von Konstanten und dem Bezeichner `iota`
konstruiert, und kann diese typsicher verwenden.
[ENDSECTION]

[SECTION::background::default]
In vielen Programmiersprachen (wie Java oder C++) gibt es ein explizites Schlüsselwort `enum`, um
eine feste Menge von benannten Werten zu definieren, wie beispielsweise Wochentage oder Statusmeldungen.

In Go gibt es ein solches Wort leider nicht.
Stattdessen werden Konstanten in Kombination mit einem benutzerdefinierten Typ und dem speziellen
Bezeichner `iota` verwendet, um dieses Verhalten idiomatisch nachzubilden.
[ENDSECTION]

[SECTION::instructions::detailed]

### Allgemein

Eine "Enum"-Definition in Go besteht üblicherweise aus folgenden Schritten:

- Definition eines neuen Datentyps (meist basierend auf `int`);
- Ein `const`-Block, der Werte dieses Typs definiert;
- Verwendung von `iota` zur automatischen Nummerierung.

```go
// 1. Eigenen Typ definieren
type ServerState int

// 2. Konstantenblock definieren
const (
    // 3. iota beginnt bei 0 und zählt pro Zeile hoch
    Idle      ServerState = iota // 0
    Connected                    // 1
    Error                        // 2
    Retrying                     // 3
)
```

Der Bezeichner `iota` repräsentiert den Index der aktuellen Zeile innerhalb des `const`-Blocks.
Der Ausdruck bleibt für jede Zeile des `const`-Blocks gleich; nur `iota` wird inkrementiert: 

```go
const (
    FlagA = iota * iota          // 0 * 0 = 0
    FlagB                        // implizit 1 * 1 = 1
    FlagC                        // implizit 2 * 2 = 4
)

fmt.Println(int(FlagC))          // 4
```

Lesen Sie den
[Artikel `iota` auf go.dev](https://go.dev/wiki/Iota)
und beantworten Sie anschließend die Fragen unten.

[EQ] Manchmal soll der erste Wert (`0`) ungültig sein oder übersprungen werden.
Wie erreichen Sie, dass die Aufzählung bei `1` beginnt?

[EQ] Probieren Sie aus:
Wie verhält sich `iota`, wenn es in einer Datei mehrere `const`-Blöcke gibt?

[ER] Definieren Sie einen Typ `Weekday` als `int`.
Erstellen Sie mittels `const` und `iota` folgende Aufzählungswerten: `Monday`, `Tuesday`, `Wednesday`, `Thursday`,
`Friday`, `Saturday`, `Sunday`.

<!-- time estimate: 15 min -->


### Das Interface `fmt.Stringer`

[EQ] Probieren Sie aus:
Wie sehen die Werte der Aufzählung `Weekday` auf der Kommandozeile aus?
Welches Problem fällt Ihnen ein?

Um Variablen auf der Kommandozeile darzustellen, benutzt das Paket `fmt` das Interface `Stringer`.
Oft lohnt es sich, dieses Interface für Ihre Aufzählungen zu implementieren.

[ER] Schauen Sie sich das
[Interface `Stringer` in "A Tour of Go"](https://go.dev/tour/methods/17)
an.
Implementieren Sie die Methode `String() string` für `Weekday`, sodass beim Ausdrucken der
Variablen der lesbare Name (z. B. `"Monday"` oder `"Tuesday"`) ausgegeben wird.
Sorgen Sie dafür, dass unbekannte Werte als `"Unknown"` ausgegeben werden.

(Mehr zu Interfaces lernen Sie in [PARTREF::go-interfaces].)

[ER] Implementieren Sie eine Funktion `isWeekend(d Weekday) bool`.
Diese Funktion soll `true` zurückgeben, falls `d` `Saturday` oder `Sunday` ist.

[EQ] Warum ist es sinnvoll, einen eigenen Typ (`type Weekday int`) zu definieren, anstatt einfach
`const Monday int = 0` zu verwenden?

[HINT::Ich weiß nicht]
In welchem Fall würde `isWeekend(8)` kompilieren?
Wäre das im Kontext Ihres Programms sinnvoll?
[ENDHINT]

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei und rufen Sie sie aus der `main`-Funktion auf:

```go
func testEnums() {
    days := []Weekday{Monday, Sunday, Weekday(8)}
    for _, day := range days {
        fmt.Println(day, isWeekend(day))
    }
}
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 25 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]

__Kommandoprotokoll__
[PROT::ALT:go-enums.prot]

__Lösungen__

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier: [TREEREF::/Sprachen/Go/go-enums.go].
[ENDINSTRUCTOR]