title: "Go: das Paket 'encoding/json'"
stage: beta
timevalue: 1
difficulty: 2
assumes: go-interfaces, go-structs2, m_json
---

[SECTION::goal::idea,experience]
Ich kann Daten in Go in das JSON-Format umwandeln und wieder zurück in Go-Datenstrukturen.
[ENDSECTION]

[SECTION::background::default]
Der Datenaustausch zwischen HTTP-Servern und HTTP-Clients erfolgt häufig im JSON-Format.
[TERMREF::JSON] steht für _JavaScript Object Notation_ und hat sich im Laufe der Jahre als Standardformat für den
Datentransfer im Web etabliert.

In dieser Aufgabe lernen Sie, wie Sie Go-Datenstrukturen in JSON umwandeln und wieder daraus erzeugen können.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Darstellungsmöglichkeiten

In Go gibt es mehrere Möglichkeiten, JSON-Daten darzustellen.
Diese schauen wir uns nun anhand der folgenden Zeichenkette an:

```json
{
  "Mike": {
    "age": 30,
    "position": "accountant"
  }
}
```


#### Weg 1: Jedes Objekt als Struktur

Die sauberste Option ist es, jeden Schlüssel im JSON als Feld einer Go-Struktur zu definieren und auf diese Art und
Weise das komplette JSON zu konvertieren.
Dabei bekommt jedes JSON-Objekt eine dedizierte Struktur und die gewohnte Typsicherheit bleibt erhalten.

```go
type JSON struct {
    Mike Person
}

type Person struct {
    Age      int
    Position string
}

var mike1 = JSON{
    Mike: Person{
        Age: 30,
        Position: "accountant",
    },
}
```


#### Weg 2: Manche Objekte als anonyme Strukturen

Anonyme Strukturen gelten oft als Einweg-Strukturen:
Sie sind am besten für die Fälle geeignet, in denen die Struktur nur einmal definiert und verwendet wird.
In diesem Beispiel ist die übergeordnete Struktur anonym:

```go
var mike2 = struct{
    Mike Person
}{
    Mike: Person{
        Age: 30,
        Position: "accountant",
    },
}
```


#### Weg 3: `map[string]any`

Bei dieser Option verliert man jegliche Typsicherheit und muss die Werte immer mittels Typzusicherung zu dem erwarteten
Typen konvertieren.
Dies ist sinnvoll, wenn die JSON-Struktur erst zur Laufzeit bekannt ist.

```go
var mike3 = map[string]any{
    "Mike": map[string]any{
        "age": 30,
        "position": "accountant",
    },
}
```

Auch wenn die Definition relativ kompakt aussieht, sind es die Lesezugriffe definitiv nicht:

```go
func printMikesAge() {
    mike := mike3["Mike"]
    if mike, ok := mike.(map[string]any); ok {
        fmt.Println(mike["age"])
    }
}
```

Wir empfehlen für die folgenden Aufgaben eine Kombination aus der ersten und zweiten Option, wobei der Grad der
Anonymität je nach Anwendungsfall variiert werden kann.

[ER] Stellen Sie die folgende JSON-Zeichenkette als Go-Struktur dar, wobei die Schlüssel den Feldnamen entsprechen
(kein `map[string]any`!).
Konvertieren Sie alle kleingeschriebenen Schlüssel in großgeschriebene Namen (`"car"` -> `Car`) und wandeln Sie
`snake_case` in `PascalCase` um.
Sie dürfen sowohl anonyme Strukturen als auch eigene Typdefinitionen verwenden und die Struktur darf in einer globalen
Variable gespeichert werden.

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
<!-- time estimate: 10 min -->


### Strukturen mit Tags

Felder einer Struktur können mit zusätzlichen Annotationen versehen werden — sogenannten _Tags_.
Tags sind besonders nützlich beim _Marshalling_ (Umwandeln in JSON) und _Unmarshalling_ (Einlesen von JSON) und haben
die folgende Syntax:

```go
`key1:"value1" key2:"value2" key3:"value3" key4:...`
```
Im folgenden Beispiel bedeutet der Tag, dass das Feld `Bar` beim _Marshalling_ (Konvertierung in JSON) nicht als
`"Bar"`, sondern als `"baz"` ausgegeben wird:

```go
type Foo struct {
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
- Sie wollen das JSON ohne das Zwischenkopieren des gesamten Inhalts in Arbeitsspeicher direkt in einen Stream schreiben,
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

[HINT::Ich weiß nicht, worauf ich achten soll]
Erinnern Sie sich an [PARTREF::go-structs1]:
Wie unterscheiden sich private und öffentliche/exportierte Felder einer Struktur? 
[ENDHINT]

[ER] Schreiben Sie eine Funktion `marshal`, in der Sie die Struktur `Car` aus [EREFR::1] anhand von `json.Marshal` in
JSON-Zeichenkette umwandeln und diese auf der Kommandozeile ausgeben.

<!-- time estimate: 10 min -->


### Unmarshalling

Analog wie beim Marshalling gibt es hier zwei Möglichkeiten:

- `json.Unmarshal(data []byte, v any) error`;
- Kombination aus `json.NewDecoder(r io.Reader) *Decoder` und `(*Decoder) Decode(v any) error`.

[NOTICE]
In beiden Fällen ist `v` __ein Zeiger auf die Variable__, in der das Ergebnis gespeichert wird.
[ENDNOTICE]

[EQ] Lesen Sie den Abschnitt "Decoding" aus dem
[Artikel "JSON and Go"](https://go.dev/blog/json#decoding)
im Go Blog und erklären Sie, wie genau die Funktion `Unmarshal` die JSON-Schlüssel den Feldern einer Struktur zuordnet.

[ER] Speichern Sie das JSON von [EREFR::1] als globale Variable in Ihrem Programm und schreiben Sie eine Funktion `unmarshal`,
in der Sie es mithilfe von `json.Unmarshal` in eine Go-Struktur konvertieren und diese auf der Kommandozeile ausgeben.

[ER] Legen Sie neben Ihrem Programm eine neue Datei `car.json` an und kopieren Sie folgendes JSON in diese Datei:

```json
{
  "make": "Volkswagen",
  "model": "Golf 7",
  "color": "silver",
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
Die Datei `car.json` sollte zusammen mit `go-json.go` im Taskgroup-Verzeichnis liegen, aus dem Sie auch `go run` ausführen.
[ENDWARNING]

Vergewissern Sie sich, dass Ihre `main`-Funktion folgendermaßen aussieht:

```go
func main() {
    marshal()
    unmarshal()
    jsonFromFile()
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