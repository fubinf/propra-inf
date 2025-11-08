title: "Go: 'http.Client' und Senden von HTTP-Anfragen"
stage: draft
timevalue: 1
difficulty: 3
assumes: go-interfaces
---

[SECTION::goal::idea,experience]
Ich kann HTTP-Anfragen in Go senden.
[ENDSECTION]

[SECTION::background::default]
Es ist schwierig, die heutige Welt ohne HTTP-Abrufen von Webservern vorzustellen.

In dieser Aufgaben lernen Sie, wie solche Anfragen in Go durchgeführt werden.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Überblick

Senden von HTTP-Anfragen in Go benötigt drei Komponenten:

- `http.Request` — eine Struktur, die HTTP-Anfragen repräsentiert;
- `http.Client` — eine Struktur, die `http.Request`s ausführt;
- `http.Response` — eine Struktur, die das Ergebnis einer HTTP-Anfrage darstellt.

In dieser Aufgabe ziehen wir jede der drei Komponenten einzeln in Betracht und lernen die
Zusammenhänge zwischen den Komponenten kennen.


### `http.Request`

`http.Request` ist eine Struktur, die HTTP-Anfragen repräsentiert und alle relevanten Daten
beinhaltet.

Schauen Sie sich die 
[Dokumentation von `http.Request`](https://pkg.go.dev/net/http#Request)
an und beantworten Sie die Fragen unten.

[EQ] Wie wird ein `http.Request` erzeugt?

[EQ] Welche Argumente werden für das Erzeugen benötigt?

[EQ] Wo findet man im `http.Request` die IP-Adresse, von der die HTTP-Anfrage gekommen ist?

<!-- time estimate: 10 min -->


### `http.Client`

`http.Client` ist eine Struktur, die `http.Request`s ausführt und `http.Response` liefert.

Lesen Sie die 
[Dokumentation von `http.Client`](https://pkg.go.dev/net/http#Client)
und beantworten Sie die folgenden Fragen.

[EQ] Wie wird ein `http.Client` erzeugt?

[EQ] Was ist der Zusammenhang zwischen den Methoden
[`http.Client.Do()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=586),
[`http.Client.Head()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=938),
[`http.Client.Get()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=479)
und 
[`http.Client.Post()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=861)?

[EQ] Was ist der Unterschied zwischen:

- `http.Client.Head()` und
  [`http.Head()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=922)?
- `http.Client.Get()` und 
  [`http.Get()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=452)?
- `http.Client.Post()` und 
  [`http.Post()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=843)?

(Die Links führen zum Quellcode der jeweiligen Funktionen.
Das könnte beim Beantworten der Frage helfen.)

<!-- time estimate: 15 min -->


### `http.Response`

`http.Response` ist das Ergebnis einer HTTP-Anfrage.

Schauen Sie sich die 
[Dokumentation von `http.Response`](https://pkg.go.dev/net/http#Response)
an, um die Fragen unten zu beantworten.

[EQ] Was ist der Typ von `http.Response.Body`?
Was bedeutet das?

[EQ] Wer muss `http.Response.Body` schließen?

[EQ] Lesen Sie die 
[Dokumentation von `io.ReadAll`](https://pkg.go.dev/io#ReadAll)
und erläutern Sie, wie diese Funktion verwendet werden kann, um Ergebnis einer HTTP-Anfrage
auf der Kommandozeile auszugeben.

[EQ] Lesen Sie die
[Dokumentation von `io.Copy`](https://pkg.go.dev/io#Copy)
und erklären Sie, wie diese Funktion dabei hilft, die Ausgabe eines `io.Reader` auf 
der Kommandozeile (`os.Stdout`) anzuzeigen.
Was ist der grundsätzliche Unterschied zwischen dieser Funktion und `io.ReadAll`?

[HINT::Ich verstehe nicht, wie das funktionieren soll]
"Auf der Kommandozeile ausgeben" bedeutet letztlich, in eine Datei zu schreiben, 
nämlich nach `/dev/stdout`.
In Go ist diese Datei über die Variable `os.Stdout` vom Typ `*os.File` zugänglich.

Der Typ `*os.File` implementiert das Interface `io.ReadWriter` und kann daher sowohl als `io.Reader`
als auch als `io.Writer` verwendet werden.
[ENDHINT]

[ER] Erzeugen Sie einen `http.Client` und konfigurieren Sie ihn wie folgt:

- Timeout: 5 Sekunden;
- Die Funktion `CheckRedirect` soll auf der Kommandozeile `"redirect detected"` ausgeben,
  der Rückgabewert der Funktion darf `nil` sein.

[ER] Schreiben Sie ein Programm, in dem Sie die folgenden HTTP-Anfragen wie angegeben ausführen 
(benutzen Sie den oben konfigurierten `http.Client`):

- Eine `GET`-Anfrage an `https://postman-echo.com/get`
    * Setzen Sie einen Header `"custom_header_key":"custom_header_value"` 
     (mithilfe von `Request.Header.Add(key, value string)`);
    * Setzten Sie ein Cookie `"custom_cookie_name=custom_cookie_value"`
     (mithilfe von `Request.AddCookie(cookie *http.Cookie)`).
- Eine `GET`-Anfrage an 
  `https://postman-echo.com/redirect-to?url=https://postman-echo.com/get&status_code=302`
- Eine `GET`-Anfrage an `https://postman-echo.com/delay/6`

Benutzen Sie die Funktion `prettyPrint(r io.Reader)`, um `Response.Body` auf der Kommandozeile 
anzuzeigen:

```go
func prettyPrint(r io.Reader) {
    var buf bytes.Buffer
    data, err := io.ReadAll(r)
    if err != nil {
        fmt.Println(err)
        return
    }
    if err = json.Indent(&buf, data, "", "  "); err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println(buf.String())
}
```

__Im Allgemeinen gilt:__ Schlägt eine Anfrage fehl, darf sie die anderen nicht beeinträchtigen.
Soll eine HTTP-Anfrage einen Fehler zurückgeben, geben Sie statt des Inhalts von `Response.Body`
den Fehler auf der Kommandozeile aus.

Denken Sie daran, `Response.Body` nach dem Lesen zu schließen! 

[EC] Führen Sie Ihr Programm mittels `go run` aus.

<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-http-client.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Sprachen/Go/go-http-client.go].
[ENDINSTRUCTOR]
