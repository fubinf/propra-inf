title: Typumwandlung
stage: draft
timevalue: 0.5
difficulty: 1
requires: GoIDE, GoProgramStructure, GoVariablesAndPrimitives
---

[SECTION::goal::idea]
Ich verstehe, wie ich einen Typen zu einem anderen umwandeln kann.

[ENDSECTION]

[SECTION::background::default]
Diese Aufgabe soll unter anderem als Spickzettel zur Typumwandlung dienen. Wir gehen hier auf die häufigsten Typumwandlungen ein. 
[ENDSECTION]

### Was ist eine Typumwandlung (typecast)?

Typumwandlung ist eine Operation, die der Typ einer Variable ändert. Dabei ändert sich oft der Inhalt.

Generell lässt sich diese Prozedur folgendermaßen beschreiben: _T(v)_ konvertiert den Wert _v_ zum Typen _T_.

Nach diesem Schema können `int`- oder `float`-Typen zueinander konvertiert werden:
```go
i64 := 150
i8 := int8(i64)

f64 := 1 << 500     // bitshift Operation, entspricht 2^500
f32 := float32(f64) 
```

### Typumwandlung zu einer Zeichenkette (`string()`) (Recherche)
[EQ] Mit ganzzahligen Argumenten gibt es jedoch keinen Fehler, obwohl die Umwandlung nicht funktioniert. Warum?

Eine generelle Vorgehensweise ist folgende:
```go
f := 10.5
s := fmt.Sprintf("%v", f)
```

Zwei wichtigste Funktionen aus `fmt` Paket sind `fmt.Println()` (für die Fehlersuche und Logging) und `fmt.Sprintf()`, welche eine Zeichenkette zurückgibt. 
Die Platzhaltersyntax ähnelt sich der Syntax von `printf` Funktion in C. `%v` steht dort für "value": Die ganze Zeile lautet also "erstelle eine Zeichenkette, die den Wert von `f` darstellt".

### Typumwandlung von einer Zeichenkette
An dieser Stelle lernen wir ein nützliches Paket aus der Go-Standardbibliothek kennen, welches `strconv` heißt. In diesem Paket liegen Funktionen wie `parseT()`, wo _T_ ein primitiver Datentyp ist.
Diese Funktionen geben jeweils zwei Werte zurück: einen Wert von dem gewünschten Typen und einen `error`, welcher `nil` ist, wenn die Umwandlung erfolgreich war:
```go
i, err := strconv.ParseInt("10")            // i = 10, err = nil
i, err := strconv.ParseInt("something")     // i = 0, err = strconv.ParseInt: parsing "something": invalid syntax
```

[FOLDOUT::Kleiner Ausflüg ins `error`-Land]
Sie haben gerade zwei neue Konzepte getroffen: `nil` und `error`. `nil` ist ähnlich wie `null` in Java oder `None` in Python,
mit dem Unterschied, dass Arrays (haben wir zwar noch nicht kennengelernt, aber kommt gleich), Strukturen und primitive Datentypen diesen Wert __nicht__ annehmen dürfen (wir wissen schon, dass sie ihre eigenen Nullwerte haben).

Was ist `error`? Das ist ein Interface. Jede Struktur darf ein Error sein, solange sie die `Error()`-Methode implementiert:
```go
type Foo struct { ... }

func (f Foo) Error() string {
    ...
}
```

Wir müssen nicht alle unseren Errors vordefinieren - es gibt eine Funktion `fmt.Errorf()`, die eine Zeichenkette übergeben bekommt und
einen Error mit der Zeichenkette zurückgibt. Solche Errors sind sehr hilfreich, wenn wir unsere eigenen Randfälle abfangen möchten.
[ENDFOLDOUT]


[SECTION::submission::program]
Probieren Sie die Typumwandlung aus! Starten Sie mit `var i int64 = 150` und `var f float64 = 1 << 500`,
wandeln Sie diese bis zu `int8` bzw. `float32` und zurück zu `int` und `float64` um. Beschreiben Sie Ihre Beobachtungen 
und erklären Sie diese als Kommentare im Quellcode (einzeilige Kommentare fangen mit `//` an, mehrzeilige sehen aus wie `/* Kommentar */`). 
Speichern Sie Ihr Programm unter `casting_abgabe.go` und geben Sie diese Datei ab.
[ENDSECTION]

[INSTRUCTOR::Acceptance Criteria]
`string(int)` Erklärung
[INCLUDE::ALT:]

Der Hauptpunkt ist darauf hinzuweisen, dass Go keinen Fehler schmeißt, selbst wenn ein Über- oder Unterlauf stattgefunden hat.

Ein Lösungsvorschlag:

```go
[INCLUDE::ALT:casting_abgabe.go]
```
[ENDINSTRUCTOR]
