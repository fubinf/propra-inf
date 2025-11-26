title: "Go: das Paket 'encoding/json'"
stage: draft
timevalue: 1
difficulty: 2
assumes: go-interfaces, go-structs2
---

[SECTION::goal::idea,experience]
Ich kann Daten in Go in das JSON-Format umwandeln und wieder zurück in Go-Datenstrukturen.
[ENDSECTION]

[SECTION::background::default]
Der Datenaustausch zwischen HTTP-Servern und HTTP-Clients erfolgt häufig im JSON-Format.
JSON steht für _JavaScript Object Notation_ und hat sich im Laufe der Jahre als Standardformat 
für den Datentransfer im Web etabliert.

In dieser Aufgabe lernen Sie, wie Sie Go-Datenstrukturen in JSON umwandeln und wieder 
daraus erzeugen können.

(Anmerkung: 
[Protocol Buffers (Protobuf)](https://protobuf.dev/)
sind eine leistungsfähigere, aber weniger flexible Alternative.)
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Was genau ist JSON?

In JavaScript ist ein Objekt eine Sammlung von Schlüssel-Wert-Paaren — im Grunde wie eine Map.

```javascript
const car = {
    make: "Fiat", 
    model: "500", 
    color: "white"
};
```

Eine valide JSON-Zeichenkette ähnelt im Wesentlichen einem JavaScript-Objekt, mit dem Unterschied,
dass alle Schlüssel Zeichenketten (`string`) sein müssen:

```json
{
  "car": {
    "make": "Fiat",
    "model": "500",
    "color": "white"
  }
}
```

Die Werte dürfen selbst wiederum Sammlungen von Schlüssel-Wert-Paaren (JSON-Objekte),
primitive Datentypen (`int`, `float`, `string`, `bool`) oder Listen sein:

```json
{
  "car": {
    "make": "Fiat",
    "model": "500",
    "color": "white",
    "previous_owners": [
      {
        "name": "Max",
        "age": 30
      },
      {
        "name": "Annika",
        "age": 25
      }
    ]
  }
}
```

[NOTICE]
JSON-Syntax erlaubt kein abschließendes Komma (in Zeilen 5 und 10):

```json
{
  "previous_owners": [
    {
      "name": "Max",
      "age": 30,
    },
    {
      "name": "Annika",
      "age": 25
    },
  ]
}
```
[ENDNOTICE]

[ER] Stellen Sie das obige Beispiel 
`"car": {"make": ..., "model": ..., "color": ..., "previous_owners": ...}`
als Go-Struktur dar, wobei die Schlüssel den Feldnamen entsprechen (kein `map[string]any`!).
Konvertieren Sie alle kleingeschriebenen Schlüssel in großgeschriebene Namen (`"car"` -> `Car`), 
und wandeln Sie `snake_case` in `PascalCase` um.
Sie dürfen sowohl anonyme Strukturen als auch eigene Typdefinitionen verwenden.
Die Struktur darf in einer globalen Variable gespeichert werden.

<!-- time estimate: 10 min -->


### Strukturen mit Tags

Felder einer Struktur können mit zusätzlichen Annotationen versehen werden — sogenannten _Tags_.
Tags sind besonders nützlich beim _Marshalling_ (Umwandeln in JSON) und _Unmarshalling_
(Einlesen von JSON) und haben die folgende Syntax:

  `key1:"value1" key2:"value2" key3:"value3" key4:...`

Im folgenden Beispiel bedeutet der Tag, dass das Feld `Bar` beim _Marshalling_ nicht als `"Bar"`,
sondern als `"baz"` ausgegeben wird:

```go
struct Foo {
    Bar string `json:"baz"`
}
```

Beim _Unmarshalling_ gilt das Gleiche in umgekehrter Richtung:
Der JSON-Schlüssel `"baz"` wird im Feld `Bar` gespeichert.

<!-- time estimate: 5 min -->


### Marshalling

Das Paket `encoding/json` bietet zwei Möglichkeiten, eine Go-Datenstruktur in JSON umzuwandeln:

- `json.Marshal(v any) ([]byte, error)` — 
  das Argument `v` sowie der `[]byte`-Slice befinden sich im Arbeitsspeicher;
- Kombination aus `json.NewEncoder(w io.Writer) *Encoder` und `(*Encoder) Encode(v any) error` —
  das Argument `v` wird zu einer JSON-Zeichenkette umgewandelt und in den `io.Writer` `w` 
  geschrieben.

```go
err := json.NewEncoder(os.Stdin).Encode(car)
```

[HINT::Wie wandle ich einen `byte`-Slice zu `string` um?]
```go
b := []byte("hello")
hello := string(b)
```
[ENDHINT]

[EQ] Lesen Sie den Abschnitt "Encoding" aus dem 
[Artikel "JSON and Go" im Go Blog](https://go.dev/blog/json#encoding)
und erläutern Sie, warum eine solche Struktur für das Marshalling (und Unmarshalling) 
nicht geeignet ist:

```go
type Employee struct {
    position string   `json:"position"`
    age      int      `json:"age"`
    salary   float64  `json:"salary"`
}
```

[ER] Schreiben Sie eine Funktion `marshal`, in der Sie die Go-Struktur `Car` aus [EREFR::1]
in JSON-Zeichenkette umwandeln und diese auf der Kommandozeile ausgeben.

[ER] Fügen Sie der Struktur Tags hinzu, damit die JSON-Zeichenkette mit dem 
ursprünglichen Beispiel übereinstimmt.

[FOLDOUT::Wo muss ich welche der zwei Funktionen benutzen?]
Gründe für `json.Marshal()`:

- Strukturen sind relativ klein;
- Sie brauchen das JSON komplett im Speicher.

Gründe für `json.NewEncoder().Encode()`:

- Sie sind bereits in einem `Reader/Writer`-orientierten Kontext;
- Sie wollen das JSON direkt in einen Stream schreiben, etwa in eine Datei oder als HTTP-Antwort.

[ENDFOLDOUT]

<!-- time estimate: 10 min -->


### Unmarshalling

Analog wie beim Marshalling gibt es hier zwei Möglichkeiten:

- `json.Unmarshal(data []byte, v any) error`;
- Kombination aus `json.NewDecoder(r io.Reader) *Decoder` und `(*Decoder) Decode(v any) error`.
- (in beiden Fällen ist `v` __ein Zeiger auf die Variable__, in der das Ergebnis gespeichert wird.)

[EQ] Lesen Sie den Abschnitt "Decoding" aus dem 
[Artikel "JSON and Go"](https://go.dev/blog/json#decoding)
im Go Blog und erklären Sie, wie genau die Funktion `Unmarshal` die JSON-Schlüssel 
den Feldern einer Struktur zuordnet.

[ER] Schreiben Sie eine Funktion `unmarshal`, in der Sie den Wert von `"car"` aus 
dem Beispiel-JSON aus [EREFR::1] mithilfe von `json.Unmarshal` in eine Go-Struktur 
konvertieren und diese auf der Kommandozeile ausgeben.

[ER] Vergewissern Sie sich, dass Ihre `main`-Funktion folgendermaßen aussieht:

```go
func main() {
    marshal()
    unmarshal()
}
```

[EC] Führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 15 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

<!-- @PROGRAM_TEST -->

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-json.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-json.go].
[ENDINSTRUCTOR]