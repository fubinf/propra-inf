title: "Go: Adapter-Pattern im Kontext von HTTP-Middleware"
stage: draft
timevalue: 1
difficulty: 3
assumes: go-http-server, go-interfaces
---

[SECTION::goal::idea,experience]
Ich kann das Adapter-Pattern im Kontext von HTTP-Middleware in Go anzuwenden.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-http-server] haben Sie gelernt, dass einer der Vorteile von 
`http.Handle` die __größere Flexibilität__ ist.
Doch was bedeutet das genau?

Sie besteht in der Möglichkeit, das Adapter-Pattern (in Go oft als "Middleware" bekannt) anzuwenden.

Dank der interface-basierten Struktur können wir HTTP-Anfragen gezielt abfangen und zusätzliche
Funktionalität in jeden Schritt der eigentlichen Verarbeitung hinzufügen.
[ENDSECTION]

[SECTION::instructions::detailed]

### Daten aus `http.Request` auslesen

Stellen Sie sich vor, dass es auf Ihrer Webseite einen Bereich
`api` mit Pfaden `"/api/dashboard"`, `"/api/healthcheck"` und `"/api/usage"` gibt.

Nun wollen Sie für den Bereich Logging einbauen, jedoch völlig transparent (unsichtbar) 
für die existierenden HTTP-Handler.

Doch wie geht das?

[ER] Implementieren Sie einen HTTP-Server auf Port `8080`, der die obigen Endpunkte in einem 
`ServeMux` namens `mainMux` registriert.
Die Antwort darf der Name des jeweiligen Endpunkts sein
(beispielweise `dashboard`, `healthcheck` und `usage`).

[ER] Lesen Sie die
[Dokumentation zu `http.StripPrefix(prefix string, h http.Handler) http.Handler`](https://pkg.go.dev/net/http#StripPrefix)
und passen Sie das Routing so an, dass `mainMux` nur Anfragen mit dem Präfix `/api/` abfängt und
sie an einen `apiMux` weiterleitet.
Der `apiMux` selbst soll nichts vom `/api`-Präfix wissen und lediglich die Routen
`/dashboard`, `/healthcheck` und `/usage` behandeln.

[HINT::Ich verstehe nicht, wie das passieren soll]
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

Jetzt brauchen Sie nur noch eine Logging-Schicht zwischen `mainMux` und `apiMux`.

[EQ] Lesen Sie den
[Abschnitt "The adapter pattern for middleware" im Artikel "How I write HTTP services in Go after 13 years"](https://grafana.com/blog/2024/02/09/how-i-write-http-services-in-go-after-13-years/#the-adapter-pattern-for-middleware)
und erläutern Sie, wie eine solche Schicht integriert werden kann.

[WARNING]
Der Aufruf `h(w, r)` in dem Beispiel ist natürlich falsch, da `h` ein Handler ist
und keine Funktion.
Was der Autor stattdessen meinte, ist `h.ServeHTTP(w, r)`.
[ENDWARNING]

[ER] Fügen Sie — analog zum Beispiel mit Authentifizierung — den `api`-Endpunkten Logging hinzu.
Die Logik muss sich in einer Funktion `withLogging` befinden.
Dabei sollen die HTTP-Methode der Anfrage (`GET`, `POST`, und so weiter), der Pfad und
der Wert von `time.Now().Format(time.RFC3339)` auf der Kommandozeile ausgegeben werden.
Benutzen Sie das Format `("[%v] [%v] %v\n", currentTime, method, path)`.

<!-- time estimate: 25 min -->


### Daten aus `http.ResponseWriter` auslesen

Was ist, wenn die Antwort auch geloggt werden muss?

Da jede Antwort über die Methode `http.ResponseWriter.Write(b byte[]) (int, error)` geschrieben
wird, müssen Sie einen eigenen `http.ResponseWriter` implementieren und dort die entsprechende
Methode überschreiben.
In dem Fall ist
[Interfaceeinbettung in Strukturen](https://eli.thegreenplace.net/2020/embedding-in-go-part-3-interfaces-in-structs/)
hilfreich:

```go
type LoggingWriter struct {
    http.ResponseWriter
}
```

Mithilfe von dieser Wrapper-Struktur können Sie alle Methoden eines "echten" `http.ResponseWriter`s
überschreiben.

[NOTICE]
Ein `LoggingWriter` benötigt bei der Initialisierung immer einen konkreten `http.ResponseWriter` 
als Argument.

Auf diese Weise können Sie jederzeit die Methoden des konkreten `http.ResponseWriter`über den 
`LoggingWriter` aufrufen:

```go
func (lw LoggingWriter) someMethod() {
    lw.ResponseWriter.someMethod()
}
```
[ENDNOTICE]

[HINT::Ich verstehe nicht, was diese Deklaration bedeutet]
Hier wird ein Interface in eine Struktur eingebettet.

Das bedeutet:

1. Die Struktur `LoggingWriter` bekommt während Initialisierung eine andere Struktur übergeben, die
   das Interface `http.ResponseWriter` implementiert;
2. Die Struktur `LoggingWriter` implementiert selbst das Interface `http.ResponseWriter`.
   Dabei werden Methoden von der übergebenen Struktur aufgerufen.

Effektiv ist diese Deklaration äquivalent zu:

```go
type LoggingWriter struct {
    w http.ResponseWriter
}

func (lw LoggingWriter) Header() http.Header {
    return lw.w.Header()
}

func (lw LoggingWriter) Write(b byte[]) (int, error) {
    return lw.w.Write(b)
}

func (lw LoggingWriter) WriteHeader(statusCode int) {
    return lw.w.WriteHeader(statusCode)
}
```
[ENDHINT]

[ER] Kopieren Sie die Struktur `LoggingWriter` in Ihr Programm.
Damit Ihr `LoggingWriter` flexibel bleibt, fügen Sie der Struktur `LoggingWriter`
ein Feld `log func([]byte)` hinzu.
Dieses Feld wird beim Erstellen der Struktur mit einer Funktion initialisiert, die das
tatsächliche Logging ausführt.

[HINT::Ich verstehe nicht, was hier gewollt ist]
Der Ziel-Zustand sieht ungefähr so aus:

```go
func (lw LoggingWriter) someFunc(b byte[]) {
    ...
    lw.log(b)
}
```

Das könnte heißen, dass `log` entweder ein Feld oder eine Methode von `LoggingWriter` ist.
Eine Methode wäre in dem Fall ungünstig, da sie nicht flexibel genug ist — ist die Methode
definiert, so bleibt sie für alle Strukturen des Typs gleich.

Deswegen entscheiden wir uns für ein Feld `log func(byte[])`.
[ENDHINT]

[ER] Überschreiben Sie die Methode `Write(b byte[]) (int, error)`, indem Sie zuerst `log(b)`
aufrufen und dann die Ausführung an die "echte" Methode `Write` der internen Struktur weiterleiten.

[ER] Benutzen Sie den `LoggingWriter` in der Funktion `withLogging`: 
Erstellen Sie dort eine Instanz von `LoggingWriter` und übergeben Sie diese anstatt vom 
ursprünglichen `ResponseWriter` `w` an `h.ServeHTTP`.
Die Funktion `log` soll die Antwort-Bytefolge zu einer Zeichenkette umwandeln und diese im Format 
`"response: %v\n"` auf der Kommandozeile ausgeben.

[EC] Starten Sie Ihren HTTP-Server und führen Sie in einem anderen Terminal folgende Befehle aus:

- `curl -X GET http://localhost:8080/api/dashboard`
- `curl -X GET http://localhost:8080/api/usage`
- `curl -X GET http://localhost:8080/api/status`

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
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
