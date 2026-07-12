title: "Go: 'http.Client' und Senden von HTTP-Anfragen"
stage: draft
timevalue: 0.75
difficulty: 2
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

[NOTICE]
Falls die Abkürzung "HTTP" für Sie eher neu ist, bietet sich die Aufgabengruppe [PARTREF::HTTP] als eine Einführung an.
[ENDNOTICE]

### Überblick

Senden von HTTP-Anfragen in Go benötigt drei Komponenten:

- `http.Request` — eine Struktur, die HTTP-Anfragen repräsentiert;
- `http.Client` — eine Struktur, die `http.Request`s ausführt;
- `http.Response` — eine Struktur, die das Ergebnis einer HTTP-Anfrage darstellt.

In dieser Aufgabe ziehen wir jede der drei Komponenten einzeln in Betracht und lernen die Zusammenhänge zwischen den
Komponenten kennen.


### `http.Request`

`http.Request` ist eine Struktur, die HTTP-Anfragen repräsentiert und alle relevanten Daten beinhaltet.

Schauen Sie sich die
[Dokumentation von `http.Request`](https://pkg.go.dev/net/http#Request)
an und erzeugen Sie folgende Requests.

[ER] `firstRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/get` mit einem Header`"my_header_key":"my_header_value"` und
einem Cookie `"my_cookie_name=my_cookie_value"`.

[ER] `secondRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/redirect-to?url=https://postman-echo.com/get&status_code=302`.

[ER] `thirdRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/delay/6`.

[HINT::Ich verstehe nicht, wie ein Request erzeugt wird]
Verwenden Sie dafür die Funktion
[`http.NewRequest(method, url string, body io.Reader)`](https://pkg.go.dev/net/http#NewRequest).
[ENDHINT]

[HINT::Ich weiß nicht, wie main einem Request einen Header zufügt]
Verwenden Sie dafür die Methode
[`Request.Header.Add(key, value string)`](https://pkg.go.dev/net/http#Header.Add).
[ENDHINT]

[HINT::Ich weiß nicht, wie man einem Request ein Cookie zufügt]
Das ermöglicht die Methode
[`Request.AddCookie(cookie *http.Cookie)`](https://pkg.go.dev/net/http#Request.AddCookie).
[ENDHINT]
<!-- time estimate: 20 min -->


### `http.Client`

`http.Client` ist eine Struktur, die `http.Request`s ausführt und `http.Response` liefert.

[ER] Lesen Sie die 
[Dokumentation von `http.Client`](https://pkg.go.dev/net/http#Client)
und erzeugen Sie einen `http.Client` mit dem Timeout von 5 Sekunden.
Die Funktion `CheckRedirect` soll auf der Kommandozeile `"redirect detected"` ausgeben.
Der Rückgabewert der Funktion darf `nil` sein.

[HINT::Ich verstehe nicht, wie ein `http.Client` erzeugt wird]
Hierzu gibt es keine dedizierte Funktion.
Ein `http.Client` ist eine Struktur — also wird sie wie jede normale Struktur in Go erzeugt:

```go
c := http.Client{...}
```
[ENDHINT]

[EQ] Was ist der Zusammenhang zwischen den Methoden
[`http.Client.Do()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=586),
[`http.Client.Head()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=938),
[`http.Client.Get()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=479)
und
[`http.Client.Post()`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.4:src/net/http/client.go;l=861)?

[HINT::Ich verstehe nicht, was die Antwort sein soll]
Gucken Sie das mal anders an:
Kann man einige der Methoden oben durch nur eine implementieren? 
[ENDHINT]
<!-- time estimate: 10 min -->


### `http.Response`

`http.Response` ist das Ergebnis einer HTTP-Anfrage.
Diese Struktur beinhaltet Informationen darüber, ob die Anfrage erfolgreich war (in `http.Response.Status` und
`http.Response.StatusCode`) und was das Ergebnis eigentlich ist (in `http.Response.Body`).

[EQ] Lesen Sie die
[Dokumentation von `io.ReadAll`](https://pkg.go.dev/io#ReadAll)
und erläutern Sie, wie diese Funktion verwendet werden kann, um `http.Response.Body` auf der Kommandozeile auszugeben.
Sie dürfen den Ablauf sowohl in Worten erklären als auch in einem Quellcodeabschnitt.

[HINT::Ich verstehe nicht, wie das funktionieren soll]
`io.ReadAll` liest die Daten aus einem `io.Reader` aus und gibt ein Paar `(byte[], error)` zurück.
Wie lässt sich `byte[]` zu einer lesbaren Zeichenkette konvertieren?
[ENDHINT]

[EQ] Lesen Sie die
[Dokumentation von `io.Copy`](https://pkg.go.dev/io#Copy)
und erklären Sie, wie diese Funktion das Ergebnis einer HTTP-Anfrage auf die Kommandozeile transferieren kann.
("Die Kommandozeile" ist im Go-Universum durch `os.Stdout` vom Typ `*os.File` repräsentiert.)

[HINT::Ich verstehe nicht, wie das funktionieren soll]
Der Typ `*os.File` implementiert das Interface `io.ReadWriter` und kann daher sowohl als `io.Reader` als auch als
`io.Writer` verwendet werden.
Darunter auch als `dst` in `io.Copy(dst io.Writer, src io.Reader)`.
[ENDHINT]

[ER] Schreiben Sie ein Programm, in dem Sie die oben definierten HTTP-Anfragen (`firstRequest`, `secondRequest` und
`thirdRequest`) mit dem oben definierten Client ausführen.
Benutzen Sie die Funktion `prettyPrint(r io.Reader)`, um `Response.Body` auf der Kommandozeile anzuzeigen:

```go
[SNIPPET::ITREE:go-http-client.go::pp]
```
<!-- time estimate: 15 min -->

__Im Allgemeinen gilt:__ Schlägt eine Anfrage fehl, darf sie die anderen nicht beeinträchtigen.
Soll eine HTTP-Anfrage einen Fehler zurückgeben, geben Sie statt des Inhalts von `Response.Body`
den Fehler auf der Kommandozeile aus.

[WARNING]
War die Ausführung eines Requests erfolgreich, so muss `Response.Body` nach dem Lesen geschlossen werden!

Sie können entweder manuell am Ende der Funktion `r.Body.Close()` aufrufen oder `defer r.Body.Close()` gleich nachdem es
klar ist, dass der Request erfolgreich war:

```go
resp, err := ...
if err != nil { ... }
defer resp.Body.Close()
```
[ENDWARNING]

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
[PROT::ALT:go-http-client.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-http-client.go].
[ENDINSTRUCTOR]
