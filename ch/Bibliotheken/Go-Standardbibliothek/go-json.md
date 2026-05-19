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
JSON steht für _JavaScript Object Notation_ und hat sich im Laufe der Jahre als Standardformat für den Datentransfer
im Web etabliert.

In dieser Aufgabe lernen Sie, wie Sie Go-Datenstrukturen in JSON umwandeln und wieder daraus erzeugen können.
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

Eine valide JSON-Zeichenkette ähnelt im Wesentlichen einem JavaScript-Objekt, mit dem Unterschied, dass alle Schlüssel
Zeichenketten (`string`) sein müssen:

```json
{
  "car": {
    "make": "Fiat",
    "model": "500",
    "color": "white"
  }
}
```

Die Werte dürfen selbst wiederum Sammlungen von Schlüssel-Wert-Paaren (JSON-Objekte), primitive Datentypen
(`int`, `float`, `string`, `bool`) oder Listen sein:

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

[ER] Stellen Sie das obige Beispiel `"car": {"make": ..., "model": ..., "color": ..., "previous_owners": ...}` als
Go-Struktur dar, wobei die Schlüssel den Feldnamen entsprechen (kein `map[string]any`!).
Konvertieren Sie alle kleingeschriebenen Schlüssel in großgeschriebene Namen (`"car"` -> `Car`) und wandeln Sie
`snake_case` in `PascalCase` um.
Sie dürfen sowohl anonyme Strukturen als auch eigene Typdefinitionen verwenden.
Die Struktur darf in einer globalen Variable gespeichert werden.

<!-- time estimate: 10 min -->


### Strukturen mit Tags

Felder einer Struktur können mit zusätzlichen Annotationen versehen werden — sogenannten _Tags_.
Tags sind besonders nützlich beim _Marshalling_ (Umwandeln in JSON) und _Unmarshalling_ (Einlesen von JSON) und haben
die folgende Syntax:

  `key1:"value1" key2:"value2" key3:"value3" key4:...`

Im folgenden Beispiel bedeutet der Tag, dass das Feld `Bar` beim _Marshalling_ (Konvertierung in JSON) nicht als
`"Bar"`, sondern als `"baz"` ausgegeben wird:

```go
struct Foo {
    Bar string `json:"baz"`
}
```

Beim _Unmarshalling_ gilt das Gleiche in umgekehrter Richtung:
Der JSON-Schlüssel `"baz"` wird im Feld `Bar` gespeichert.

[ER] Fügen Sie der Struktur `Car` Tags hinzu, damit die Umwandlung in JSON dieselben Feldnamen produziert wie im
ursprünglichen Beispiel.

<!-- time estimate: 5 min -->


### Marshalling

Das Paket `encoding/json` bietet zwei Möglichkeiten, eine Go-Datenstruktur in JSON umzuwandeln:

- `json.Marshal(v any) ([]byte, error)` — das Argument `v` sowie der `[]byte`-Slice befinden sich im Arbeitsspeicher;
- Kombination aus `json.NewEncoder(w io.Writer) *Encoder` und `(*Encoder) Encode(v any) error` — das Argument `v` wird
  zu einer JSON-Zeichenkette umgewandelt und in den `io.Writer` `w` geschrieben.
  Diese Version eignet sich für kontinuierliche Datenströme, die oft die Interfaces `io.Reader` und `io.Writer`
  implementieren.

[FOLDOUT::Wo soll ich welche der zwei Funktionen benutzen?]
Gründe für `json.Marshal()`:

- Strukturen sind relativ klein;
- Sie brauchen das JSON komplett im Arbeitsspeicher.

Gründe für `json.NewEncoder().Encode()`:

- Sie sind bereits in einem `Reader/Writer`-orientierten Kontext;
- Sie wollen das JSON ohne das Zwischenkopieren des gesamten Inhalts in Arbeitspeicher direkt in einen Stream schreiben,
  etwa in eine Datei oder als HTTP-Antwort.

[ENDFOLDOUT]

Das folgende Beispiel konvertiert die Struktur `car` nach JSON und schreibt es auf die Kommandozeile (`os.Stdout`):

```go
err := json.NewEncoder(os.Stdout).Encode(car)
```

[HINT::Wie wandle ich einen `byte`-Slice zu `string` um?]
```go
b := []byte("hello")
hello := string(b)
```
[ENDHINT]

[EQ] Lesen Sie den Abschnitt "Encoding" aus dem 
[Artikel "JSON and Go" im Go Blog](https://go.dev/blog/json#encoding)
und erläutern Sie, warum eine solche Struktur für das Marshalling (und Unmarshalling) **nicht** geeignet ist:

```go
type Employee struct {
    position string   `json:"position"`
    age      int      `json:"age"`
    salary   float64  `json:"salary"`
}
```

[ER] Schreiben Sie eine Funktion `marshal`, in der Sie die Struktur `Car` aus [EREFR::1] anhand von `json.Marshal` in
JSON-Zeichenkette umwandeln und diese auf der Kommandozeile ausgeben.

<!-- time estimate: 10 min -->


### Unmarshalling

Analog wie beim Marshalling gibt es hier zwei Möglichkeiten:

- `json.Unmarshal(data []byte, v any) error`;
- Kombination aus `json.NewDecoder(r io.Reader) *Decoder` und `(*Decoder) Decode(v any) error`.
- (in beiden Fällen ist `v` __ein Zeiger auf die Variable__, in der das Ergebnis gespeichert wird.)

[EQ] Lesen Sie den Abschnitt "Decoding" aus dem 
[Artikel "JSON and Go"](https://go.dev/blog/json#decoding)
im Go Blog und erklären Sie, wie genau die Funktion `Unmarshal` die JSON-Schlüssel den Feldern einer Struktur zuordnet.

[ER] Speichern Sie das Beispiel-JSON als globale Variable in Ihrem Programm und schreiben Sie eine Funktion `unmarshal`,
in der Sie es mithilfe von `json.Unmarshal` in eine Go-Struktur konvertieren und diese auf der Kommandozeile ausgeben.

[ER] Legen Sie neben Ihrem Programm eine neue Datei `car.json` an und kopieren Sie folgendes JSON in diese Datei um:

```json
{
  "make": "Volkswagen",
  "model": "Golf 7",
  "color": "silber",
  "previous_owners": [
    {
      "name": "Dave",
      "age": 25
    }
  ]
}
```

Ergänzen Sie anschließend diese Funktion:

```go
func jsonFromFile() {
    f, err := os.Open("car.json")
    if err != nil {
        panic(err)
	}
    defer f.Close()

    // verwenden Sie hier json.NewDecoder, 
    // um JSON aus car.json in Car umzuwandeln und auf der Kommandozeile auszugeben.
}
```

[WARNING]
Die Datei `car.json` muss in dem Verzeichnis liegen, aus dem Sie `go run` ausführen.

So muss das Verzeichnis aussehen, wenn Sie das Programm mittels `go run go-json.go` ausführen:

```
foo/
├── go-json.go
└── car.json
```

Benutzen Sie stattdessen `go run foo/go-json.go`, so ist das die gewünschte Struktur:

```
bar/
├── car.json
└── foo/
    └── go-json.go
```

[ENDWARNING]

Vergewissern Sie sich, dass Ihre `main`-Funktion folgendermaßen aussieht:

```go
func main() {
    marshal()
    unmarshal()
}
```

[EC] Führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-json.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-json.go].
[ENDINSTRUCTOR]