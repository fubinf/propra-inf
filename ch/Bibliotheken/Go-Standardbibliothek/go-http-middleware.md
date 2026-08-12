title: "Go: Adapter-Pattern im Kontext von HTTP-Middleware"
stage: beta
timevalue: 1
difficulty: 3
assumes: go-interfaces, go-http-server
---

[SECTION::goal::idea,experience]
Ich kann das Adapter-Pattern im Kontext von HTTP-Middleware in Go anwenden.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-http-server] haben Sie gelernt, dass `http.Handle` flexibler ist als `http.HandleFunc`.
Doch was bedeutet das genau?

Mit `http.Handle` lässt sich das Adapter-Pattern anwenden — in Go oft als [TERMREF::Middleware] bekannt.

Dank der interfacebasierten Struktur können wir an jeder Stelle der Verarbeitungskette
zusätzliche Funktionalität einfügen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Daten aus `http.Request` auslesen

Stellen Sie sich vor, dass es auf Ihrer Webseite einen Bereich `api` mit den Pfaden `"/api/dashboard"`,
`"/api/healthcheck"` und `"/api/usage"` gibt.

Nun wollen Sie für den Bereich Logging einbauen, jedoch völlig transparent (unsichtbar)
für die existierenden Handler.

[ER] Implementieren Sie einen HTTP-Server auf Port `8080`, der die obigen Endpunkte in einem `ServeMux` namens `mainMux`
registriert.
Die Endpunkte sollen jeweils ihren Namen zurückgeben (also `dashboard`, `healthcheck` und `usage`).

[ER] Lesen Sie die
[Dokumentation zu `http.StripPrefix(prefix string, h http.Handler) http.Handler`](https://pkg.go.dev/net/http#StripPrefix)
und passen Sie das Routing so an, dass `mainMux` nur Anfragen mit dem Präfix `/api/` abfängt und sie an einen `apiMux`
weiterleitet.
Der `apiMux` selbst soll nichts vom `/api`-Präfix wissen und lediglich die Routen `/dashboard`, `/healthcheck` und
`/usage` behandeln.

[HINT::Ich verstehe nicht, wie die Weiterleitung stattfinden soll]
Zuerst brauchen Sie einen Endpunkt, der alle Anfragen unter `/api/` entgegennimmt:

```go
mainMux.Handle("/api/", ...)
```

Anschließend wird die passende Route an den Handler weitergegeben, allerdings ohne das `/api`-Präfix
(Vorsicht: nur mit einem Schrägstrich!):

```go
http.StripPrefix("/api", apiMux)
```
[ENDHINT]

[EQ] Lesen Sie den
[Abschnitt "The adapter pattern for middleware" im Artikel "How I write HTTP services in Go after 13 years"](https://grafana.com/blog/2024/02/09/how-i-write-http-services-in-go-after-13-years/#the-adapter-pattern-for-middleware)
und erläutern Sie, wie eine solche Schicht integriert werden kann.

[EQ] Der Beispielcode im Artikel lässt sich in dieser Form nicht kompilieren.
Identifizieren Sie die fehlerhafte Zeile, erklären Sie, warum der Compiler an dieser Stelle einen Fehler wirft, und
geben Sie den korrekten Aufruf an.

[ER] Fügen Sie — analog zum Beispiel `adminOnly` — den `api`-Endpunkten Logging hinzu.
Die Logik muss sich in einer Funktion `withLogging(next http.Handler) http.Handler` befinden.
Dabei sollen die HTTP-Methode der Anfrage (`GET`, `POST`, und so weiter), der Pfad und der Wert von
`time.Now().Format(time.RFC3339)` auf der Kommandozeile ausgegeben werden.
Verwenden Sie das Format `("[%v] [%v] %v\n", currentTime, method, path)`.

<!-- time estimate: 30 min -->


### Schreibzugriffe auf `http.ResponseWriter` abfangen

Was ist, wenn die Antwort auch geloggt werden muss?

Da jede Antwort über das Interface `http.ResponseWriter` geschrieben wird, müssen Sie einen eigenen
`http.ResponseWriter` implementieren und dort die Methoden _überdecken_, die für das Schreiben verwendet werden.
In dem Fall ist
[Interfaceeinbettung in Strukturen](https://eli.thegreenplace.net/2020/embedding-in-go-part-3-interfaces-in-structs/)
hilfreich:

```go
type LoggingWriter struct {
    http.ResponseWriter
}
```

Mithilfe dieser Wrapper-Struktur können Sie alle Methoden eines "echten" `http.ResponseWriter` überdecken.
Beachten Sie hier die Begrifflichkeit: In Go sprechen wir nicht vom Überschreiben, sondern vom Überdecken.
Anders als bei der klassischen Vererbung, wo Methoden dynamisch überschrieben werden, handelt es sich in Go um ein
statisches Überdecken (_Shadowing of embedded fields_, wie in [PARTREF::go-structs1] eingeführt) basierend auf der
Einbettungstiefe.

[HINT::Ich verstehe nicht, was diese Deklaration bedeutet]
Hier wird ein Interface in eine Struktur eingebettet.

Das bedeutet:

1. Die Struktur `LoggingWriter` bekommt bei der Initialisierung einen Wert übergeben, der das Interface
   `http.ResponseWriter` implementiert;
2. Die Struktur `LoggingWriter` implementiert selbst das Interface `http.ResponseWriter`.
   Dabei werden die Methoden des übergebenen Werts aufgerufen.

Effektiv ist diese Deklaration äquivalent zu:

```go
type LoggingWriter struct {
    w http.ResponseWriter
}

func (lw LoggingWriter) Header() http.Header {
    return lw.w.Header()
}

func (lw LoggingWriter) Write(b []byte) (int, error) {
    return lw.w.Write(b)
}

func (lw LoggingWriter) WriteHeader(statusCode int) {
    lw.w.WriteHeader(statusCode)
}
```
[ENDHINT]

[ER] Kopieren Sie die Struktur `LoggingWriter` in Ihr Programm.
Damit Ihr `LoggingWriter` flexibel bleibt, fügen Sie der Struktur `LoggingWriter` ein Feld `log func([]byte)` hinzu.
Dieses Feld wird beim Erstellen der Struktur mit einer Funktion initialisiert, die das tatsächliche Logging ausführt.

[HINT::Ich verstehe nicht, was hier gewollt ist]
Der Ziel-Zustand sieht ungefähr so aus:

```go
func (lw LoggingWriter) someMethod(b []byte) {
    ...
    lw.log(b)
}
```
[ENDHINT]

[ER] Überdecken Sie die Methode `Write(b []byte) (int, error)`, indem Sie zuerst `log(b)`
aufrufen und dann die Ausführung an die "echte" Methode `Write` des eingebetteten `http.ResponseWriter` weiterleiten.

[ER] Verwenden Sie den `LoggingWriter` in der Funktion `withLogging`:
Erstellen Sie dort eine Instanz von `LoggingWriter` und übergeben Sie diese an `next.ServeHTTP`
anstelle des ursprünglichen `http.ResponseWriter`.
Die Funktion `log` soll die Antwort-Bytefolge zu einer Zeichenkette umwandeln und diese im Format `"response: %v\n"` auf
der Kommandozeile ausgeben.

[EC] Starten Sie Ihren HTTP-Server mittels `go run` und führen Sie in einem anderen Terminal folgende Befehle aus:

- `curl http://localhost:8080/api/dashboard`
- `curl -X POST http://localhost:8080/api/usage`
- `curl http://localhost:8080/api/healthcheck`

**Wichtig:** Geben Sie nur die Ausgaben von der Server-Sitzung ab!
Die `curl`-Befehle sind nur der Auslöser und gehören nicht ins Kommandoprotokoll.

[EQ] Wie und warum ändert sich das Logging, wenn Sie die Zeile
`mainMux.Handle("/api/", withLogging(http.StripPrefix("/api", apiMux)))` durch die Zeile
`mainMux.Handle("/api/", http.StripPrefix("/api", withLogging(apiMux)))` ersetzen?

<!-- time estimate: 30 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-http-middleware.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-http-middleware.go].
[ENDINSTRUCTOR]
