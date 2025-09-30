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

### Map (Mehrblocktyp)

Eine Map ist eine Sammlung von Schlüssel-Wert-Paaren, die effizienten Zugriff auf Daten über ihre
Schlüssel ermöglicht. Maps haben einen Mehrblocktyp.

Maps können als "map literals" erstellt und gleich initialisiert werden 
(`string` ist der Typ der Schlüssel, `int` ist der Typ der Werte)
oder man legt sie leer mit `make` an:
```go 
m := map[string]int{"a": 1, "b": 2, "c": 3}
m2 := make(map[string]int)
```

Wie bei Slices gibt `len(m)` die aktuelle Anzahl von Einträgen einer Map zurück.


### Lesen

Es gibt zwei Arten des Lesezugriffs auf eine Map:

- `value := m[key]` gibt den Wert für den Schlüssel `key` zurück. 
  Falls der Schlüssel nicht vorhanden ist, liefert es den Nullwert des entsprechenden Typs 
  (beispielsweise `""` für `string`, `0` für `int` usw.).
  Einem solchen Nullwert sieht man also nicht an, ob er so eingetragen ist oder es keinen Eintrag gibt.
- `value, ok := m[key]`. 
  Dieses Idiom erlaubt die Unterscheidung, ob ein Schlüssel in der Map enthalten ist oder nicht.
  Ist der Schlüssel vorhanden, ist `ok` gleich `true`; andernfalls ist `ok` gleich `false`.

Ein typisches Idiom für Lesezugriffe ist:
```go
if value, ok := m[key]; ok {
    // use value
}
```

[WARNING]
Die Konvention hier ist genau das _Gegenteil_ von `err != nil`.

Der zweite Rückgabewert eines Funktionsaufrufs `val, err := someFunction()`
ist gesetzt, wenn der Aufruf fehlgeschlagen ist.
Beim Lesezugriff auf Maps hingegen ist der zweite Rückgabewert gesetzt, wenn alles
_glattgelaufen_ ist und der Schlüssel tatsächlich in der Map existiert.
Üblicherweise wird der zweite Rückgabewert beim Map-Zugriff `ok` genannt.
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
Das ist aber keine gute Idee, aus folgendem Grund:
```go
var m map[string]int        // Deklaration
fmt.Println(m == nil)       // true
fmt.Println(m["foo"])       // 0
m["foo"] = 42               // panic: assignment to entry in nil map
m = make(map[string]int)    // Initialisierung
```
Wie erwartet führt ein Schreibzugriff vor der Initialisierung zu einem Laufzeitfehler 
(also Programmabsturz), _aber Lesezugriffe funktionieren schon!
Das kann enorme Verwirrung stiften.

Die idiomatische und empfohlene Art, eine Map einzuführen, lautet:

```go
m := make(map[string]int)
```
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
