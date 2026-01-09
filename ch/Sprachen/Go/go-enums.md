title: "Grundlagen von Go: Enums"
stage: draft
timevalue: 1.0
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

Ein klassisches Beispiel sind Wochentage:

```go
// 1. Eigener Typ erstellen
type Weekday int

// 2. Konstantenblock definieren
const (
    // 3. iota beginnt bei 0 und zählt pro Zeile hoch
    Sunday    Weekday = iota // 0
    Monday                   // 1
    Tuesday                  // 2
    Wednesday                // 3
    Thursday                 // 4
    Friday                   // 5
    Saturday                 // 6
)
```

Dank des benutzerdefinierten Typs `Weekday` verhindert der Compiler, dass Sie versehentlich eine
normale Ganzzahl an eine Funktion übergeben, die eigentlich einen `Weekday` erwartet.

Der Bezeichner `iota` repräsentiert den Index der aktuellen Zeile innerhalb des `const`-Blocks.

```go
const (
    FlagA = 1 << iota  // 1 << 0 = 1
    FlagB              // 1 << 1 = 2
    FlagC              // 1 << 2 = 4
)
```

Lesen Sie die Artikel, um die Fragen unten zu beantworten:

- [`iota` auf go.dev](https://go.dev/wiki/Iota)
- [Go by Example: Enums](https://gobyexample.com/enums)

[EQ] Was passiert mit dem internen Zähler von `iota`, wenn in einer Datei ein neuer `const`-Block beginnt?

[EQ] Manchmal soll der erste Wert (`0`) ungültig sein oder übersprungen werden.
Wie erreichen Sie, dass der erste __gültige__ Wert im `const`-Block den Wert 1 erhält?

[EQ] Warum ist es sinnvoll, einen eigenen Typ (`type Status int`) zu definieren, anstatt einfach
`const StatusRunning int = 0` zu verwenden?

<!-- time estimate: 20 min -->


### Die Stringer-Schnittstelle

Ein Nachteil dieser `int`-basierten Enums ist, dass sie bei der Konsolenausgabe standardmäßig nur
als Zahl erscheinen (z. B. `0` statt `Sunday`).

Um dies zu ändern, können Sie dem Typ eine Methode `String() string` hinzufügen.
Somit erfüllt Ihr Typ das Interface `fmt.Stringer` (mehr dazu lernen Sie in der Aufgabe [PARTREF::go-interfaces]).

Bei Konsolenausgaben wird nun die Methode `String() string` benutzt, um herauszufinden, wie die Werte
dieses Typs korrekt darzustellen sind.

```go
func (w Weekday) String() string {
    // Ein Array oder Slice mit den Namen ist oft der einfachste Weg
    names := [...]string{
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday",
    }
    // Prüfung, ob der Wert im gültigen Bereich liegt
    if w < Sunday || w > Saturday {
        return "Unknown"
    }
    return names[w]
}
```
[ER] Definieren Sie einen Typ `ServerState` als `int`.
Erstellen Sie mittels `const` und `iota` folgende Zustände: `StateIdle`, `StateConnecting`,
`StateConnected`, `StateError`.

[ER] Implementieren Sie die Methode `String() string` für `ServerState`, sodass beim Ausdrucken der
Variablen der lesbare Name (z. B. `"Idle"` oder `"Error"`) ausgegeben wird.
Sorgen Sie dafür, dass unbekannte Werte als `"Unknown State"` ausgegeben werden.

[ER] Implementieren Sie eine Funktion `transition(current ServerState) ServerState`, die einen
einfachen Zustandsautomaten simuliert (anhand von `current` den nächsten Zustand ermittelt):

- `StateIdle` wechselt zu `StateConnecting`;
- `StateConnecting` wechselt zu `StateConnected`;
- `StateConnected` wechselt zu `StateIdle` (Verbindung beendet);
- `StateError` bleibt `StateError`;
- Alle anderen Übergänge bleiben auf dem aktuellen Status.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei und rufen Sie sie aus der `main`-Funktion auf:

```go
[INCLUDE::include/go-enums-control-snippet.go]
```

[EC] Führen Sie das Programm mittels go run aus.

<!-- time estimate: 20 min -->
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