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
Die heutige Welt ist ohne HTTP-Abfragen an Webserver kaum noch vorstellbar.

In dieser Aufgabe lernen Sie, wie solche Anfragen in Go durchgeführt werden.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

[NOTICE]
Falls die Abkürzung "HTTP" für Sie eher neu ist, bietet sich die Aufgabengruppe [PARTREF::HTTP] als Einführung an.
[ENDNOTICE]

### Überblick

Für das Senden von HTTP-Anfragen in Go werden drei Kernkomponenten benötigt:

- `http.Request` — eine Struktur, die eine HTTP-Anfrage repräsentiert;
- `http.Client` — eine Struktur, die `http.Request`s ausführt;
- `http.Response` — eine Struktur, die das Ergebnis einer HTTP-Anfrage darstellt.

In dieser Aufgabe betrachten wir diese drei Komponenten im Detail und lernen ihre Zusammenhänge kennen.


### `http.Request`

`http.Request` ist eine Struktur, die eine HTTP-Anfrage sowie alle relevanten Daten repräsentiert.

Schauen Sie sich die
[Dokumentation von `http.Request`](https://pkg.go.dev/net/http#Request)
an und erzeugen Sie folgende Requests:

[ER] `firstRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/get` mit dem Header `"my_header_key":"my_header_value"` und
dem Cookie `"my_cookie_name=my_cookie_value"`.

[ER] `secondRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/redirect-to?url=https://postman-echo.com/get&status_code=302`.

[ER] `thirdRequest`:
Ein GET-`http.Request` auf `https://postman-echo.com/delay/6`.

[HINT::Ich verstehe nicht, wie ein Request erzeugt wird]
Verwenden Sie dafür die Funktion
[`http.NewRequest(method, url string, body io.Reader)`](https://pkg.go.dev/net/http#NewRequest).
[ENDHINT]

[HINT::Ich weiß nicht, wie man einem Request einen Header hinzufügt]
Verwenden Sie dafür die Methode
[`Request.Header.Add(key, value string)`](https://pkg.go.dev/net/http#Header.Add).
[ENDHINT]

[HINT::Ich weiß nicht, wie man einem Request ein Cookie hinzufügt]
Dies ermöglicht die Methode
[`Request.AddCookie(cookie *http.Cookie)`](https://pkg.go.dev/net/http#Request.AddCookie).
[ENDHINT]
<!-- time estimate: 15 min -->


### `http.Client`

`http.Client` ist eine Struktur, die `http.Request`s ausführt und eine `http.Response` zurückliefert.

[ER] Lesen Sie die
[Dokumentation von `http.Client`](https://pkg.go.dev/net/http#Client)
und erzeugen Sie einen `http.Client` mit einem Timeout von 5 Sekunden.
Die Funktion `CheckRedirect` soll auf der Kommandozeile `"redirect detected"` ausgeben und `nil` zurückgeben.

[HINT::Ich verstehe nicht, wie ein `http.Client` erzeugt wird]
Hierzu gibt es keine dedizierte Funktion.
Ein `http.Client` ist eine Struktur — sie wird also wie jede normale Struktur in Go initialisiert:

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
Betrachten Sie es aus einem anderen Blickwinkel:
Lassen sich einige dieser Methoden durch eine einzige implementieren?
[ENDHINT]
<!-- time estimate: 10 min -->


### `http.Response`

`http.Response` ist das Ergebnis einer HTTP-Anfrage.
Diese Struktur enthält Informationen über den Erfolg der Anfrage (in `http.Response.Status` und
`http.Response.StatusCode`) sowie das eigentliche Ergebnis (in `http.Response.Body`).

[EQ] Lesen Sie die
[Dokumentation von `io.ReadAll`](https://pkg.go.dev/io#ReadAll)
und erläutern Sie, wie diese Funktion verwendet werden kann, um den `http.Response.Body` auf der Kommandozeile
auszugeben.
Sie können den Ablauf in Worten erklären oder als Quellcode darstellen.

[HINT::Ich verstehe nicht, wie das funktionieren soll]
`io.ReadAll` liest die Daten aus einem `io.Reader` aus und gibt ein Paar `([]byte, error)` zurück.
Wie lässt sich ein `[]byte` in eine lesbare Zeichenkette konvertieren?
[ENDHINT]

[EQ] Lesen Sie die
[Dokumentation von `io.Copy`](https://pkg.go.dev/io#Copy)
und erklären Sie, wie diese Funktion das Ergebnis einer HTTP-Anfrage auf die Kommandozeile ausgeben kann.
("Die Kommandozeile" wird im Go-Universum durch `os.Stdout` vom Typ `*os.File` repräsentiert.)

[HINT::Ich verstehe nicht, wie das funktionieren soll]
Der Typ `*os.File` implementiert das Interface `io.ReadWriter` und kann daher sowohl als `io.Reader` als auch als
`io.Writer` verwendet werden — darunter auch als `dst` in `io.Copy(dst io.Writer, src io.Reader)`.
[ENDHINT]

[ER] Schreiben Sie ein Programm, in dem Sie die oben definierten HTTP-Anfragen (`firstRequest`, `secondRequest` und
`thirdRequest`) mit dem konfigurierten Client ausführen.
Benutzen Sie die Funktion `prettyPrint(r io.Reader)`, um den `Response.Body` auf der Kommandozeile anzuzeigen:

```go
[SNIPPET::ITREE:go-http-client.go::pp]
```

Im Allgemeinen gilt:
Schlägt eine Anfrage fehl, darf sie die anderen nicht beeinträchtigen.
Sollte eine HTTP-Anfrage einen Fehler zurückgeben, geben Sie statt des Inhalts von `Response.Body`
den Fehler auf der Kommandozeile aus.

[WARNING]
War ein Request erfolgreich, muss dessen `Response.Body` am Ende geschlossen werden!

Rufen Sie dazu entweder manuell am Ende der Funktion `r.Body.Close()` auf oder nutzen Sie `defer r.Body.Close()`, sobald
feststeht, dass der Request erfolgreich war:

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
