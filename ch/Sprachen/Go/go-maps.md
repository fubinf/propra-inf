title: "Grundlagen von Go: Maps"
stage: alpha
timevalue: 1
difficulty: 2
assumes: go-basics, go-pointers, go-functions
---

[SECTION::goal::idea,experience]
Ich habe Maps in Go kennengelernt.
[ENDSECTION]

[SECTION::background::default]
Maps ermöglichen es, Daten schnell über Schlüssel zu speichern und wiederzufinden — 
wie ein eingebautes Nachschlagewerk. 
Ob Zählungen, Zuordnungen oder schnelle Suchen: Maps bieten eine elegante und effiziente 
Lösung für viele Alltagsprobleme in der Programmierung.
[ENDSECTION]

[SECTION::instructions::detailed]

### Map (Referenztyp)

Eine Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre
Schlüssel ermöglicht.

Eine Map ist ein Referenztyp.

Maps können als "map literals" erstellt werden 
(`string` ist der Typ der Schlüssel, `int` ist der Typ der Werte):
```go 
m := map[string]int{"a": 1, "b": 2, "c": 3}
```

Maps können auch mithilfe von Funktion `make` kreiert werden:
```go
m := make(map[string]int)
```

[NOTICE]
Genuso wie bei Slices, gibt `len(m)` die Länge einer Map zurück.
[ENDNOTICE]


### Lesen

Es gibt zwei Arten von Lesezugriffen auf Maps:

- `value := m[key]` gibt entweder den Wert für den Schlüssel `key` zurück — oder, 
  falls der Schlüssel nicht vorhanden ist, den Nullwert des entsprechenden Typs 
  (beispielsweise `""` für `string`, `0` für `int` usw.);
- `value, ok := m[key]`. 
  Dieses Idiom erlaubt die Unterscheidung, ob ein Schlüssel in der Map enthalten ist oder nicht.
  Ist der Schlüssel vorhanden, ist `ok` gleich `true`; andernfalls ist `ok` gleich `false`.

Ein typisches Muster für Lesezugriffe ist:
```go
if value, ok := m[key]; ok {
    // use value
}
```

[WARNING]
Die Konvention hier ist genau das Gegenteil von `err != nil`.

Der zweite Rückgabewert eines Funktionsaufrufs `val, err := someFunction()`
ist gesetzt, wenn der Aufruf fehlgeschlagen ist.

Beim Lesezugriff auf Maps hingegen ist der zweite Rückgabewert gesetzt, wenn alles
glattgelaufen ist und der Schlüssel tatsächlich in der Map existiert.

Konventionell wird der zweite Rückgabewert beim Map-Zugriff `ok` genannt.
Falls Sie ein `ok` nicht aussagekräftig finden, ersetzen Sie es durch ein `isThere` —
"value is there" liest sich natürlicher und kann den Tag retten, wenn einem die
Feinheiten mal entfallen.
[ENDWARNING]


### Schreiben

Schreibzugriffe auf Maps sind unkompliziert:

```go
m[key] = value
```

Existiert der Schlüssel `key` bereits, wird der zugehörige Wert überschrieben.
Andernfalls wird ein neues Schlüssel-Wert-Paar `key:value` angelegt.

Mit der eingebauten Funktion 
[`delete`](https://pkg.go.dev/builtin#delete)
lässt sich ein Schlüssel-Wert-Paar entfernen.
Falls der angegebene Schlüssel nicht existiert, hat der Aufruf keine Wirkung:

```go
delete(someMap, someKey)
```

[WARNING]
Man kann eine Map **deklarieren** und erst später **initialisieren**.
```go
var m map[string]int        // Deklaration
...
m = make(map[string]int)    // Initialisierung
```

Ein Schreibzugriff vor der Initialisierung führt jedoch zu einem Laufzeitfehler (Programmabsturz):
```go
m["foo"] = 42               // panic: assignment to entry in nil map
```

Deshalb raten wir davon ab, Maps nur mit `var m map[string]int` zu deklarieren, 
ohne sie direkt zu initialisieren.

Ein Lesezugriff hingegen funktioniert auch ohne vorherige Initialisierung – was leicht zu 
Missverständnissen führen kann:
```go
fmt.Println(m == nil)       // true
fmt.Println(m["foo"])       // 0
```

Die idiomatische und empfohlene Art, eine Map in Go zu initialisieren, ist:

```go
m := make(map[string]int)
```

Diese Schreibweise ist im Go-Universum klar, verständlich und weit verbreitet.
[ENDWARNING]


### Programmieren

[ER] Implementieren Sie eine Funktion `checkAnagram(w1, w2 string) bool`, die zwei Wörter als 
Argumente erhält und entscheidet, ob sie ein Anagramm-Paar bilden.

Algorithmus:

1. **Zählen der Buchstaben im ersten Wort:**
   Die Häufigkeiten der Buchstaben werden in einer Map `map[rune]int` gespeichert:
    - `for i, r := range someString` iteriert über alle Zeichen eines Strings.
    - `i` ist der Index, `r` ist der Buchstabe in Form eines `rune`-Werts (ein Alias für `int32`).
    - Beim Iterieren über Strings in Go erhält man standardmäßig `rune`-Werte 
      ([TERMREF::Unicode]-Codepoints).

2. **Verarbeiten des zweiten Wortes:** 
   Auch das zweite Wort wird Buchstabe für Buchstabe durchlaufen:
    - ist ein Buchstabe **nicht** in der Map vorhanden -> sofort `false` zurückgeben.
    - ist er vorhanden — den Zähler um 1 verringern.
      Wenn der Zähler dabei auf 0 sinkt, wird der Buchstabe aus der Map entfernt (`delete`).

3. Falls die Map am Ende leer ist, sind die Wörter ein Anagramm-Paar.

[ER] Fügen Sie folgende Testfunktion Ihrem Programm bei:

```go
[INCLUDE::include/go-maps-control-snippet.go]
```

[ER] Für ein korrektes Kommandoprotokoll muss Ihre `main`-Funktion folgendermaßen aussehen;
bitte ebenfalls zufügen:

```go
func main() {
    testMaps()
}
```

[EC] Führen Sie das Programm mittels `go run` aus.

<!-- time estimate: 30 min -->
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
`testMaps`:
diese Funktion sollte unverändert in dem abgegebenen Quellcode präsent sein,
damit das Kommandoprotokoll nicht verfälscht wird.

**Kommandoprotokoll**
[PROT::ALT:go-maps.prot]


Musterlösung der Programmieraufgabe: 
[INCLUDE::ALT:]

Oder als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-maps.go].
[ENDINSTRUCTOR]
