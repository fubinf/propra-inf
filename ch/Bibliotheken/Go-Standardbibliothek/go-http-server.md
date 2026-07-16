title: "Go: 'http.Server'"
stage: alpha
timevalue: 0.75
difficulty: 3
assumes: go-context, curl
---

[SECTION::goal::idea,experience]
Ich kann einen HTTP-Server in Go implementieren.
[ENDSECTION]

[SECTION::background::default]
Ein _Server_ ist ein Programm, das Anfragen von Clients (wie Webbrowsern) entgegennimmt und passende Antworten
zurücksendet.
Server bilden das Herzstück des Internets.

In dieser Aufgabe lernen Sie, eigene HTTP-Server mithilfe der Standardbibliothek zu bauen.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

Diese Aufgabe basiert auf dem Paket
[`net/http`](https://pkg.go.dev/net/http)
der Standardbibliothek.
Falls Ihnen das Thema noch völlig neu ist, bietet der
[Artikel "What is a web server?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server)
eine leicht verständliche Einführung in das Konzept eines Webservers.

Zudem erfordert diese Aufgabe ein grundlegendes Verständnis von URL-Bestandteilen wie "scheme", "domain", "port",
"path" und "parameters".
Eine Einführung hierzu liefert der
[Artikel "What is a URL?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL).


### Bestandteile eines Servers

Ein HTTP-Server in Go besteht aus folgenden Kernkomponenten:

- **Handler-Funktionen**: Funktionen mit der Signatur `func(http.ResponseWriter, *http.Request)`, die für die
  Bearbeitung von HTTP-Anfragen zuständig sind;
- **`ServeMux`**: Ein Router (Multiplexer), der eingehende HTTP-Anfragen den passenden, registrierten Handler-Funktionen
  zuordnet;
- **`http.Server`**: Eine Struktur für die erweiterte Konfiguration des Servers.


### Handler-Funktionen

Es gibt zwei Möglichkeiten, einen HTTP-Handler zu registrieren:

- `Handle(pattern string, handler http.Handler)` — `http.Handler` ist ein Interface mit der einzigen Methode
  `ServeHTTP(ResponseWriter, *Request)`.
  Passt eine HTTP-Anfrage zum `pattern`, wird die Methode `ServeHTTP` des `handler`s aufgerufen;
- `HandleFunc(pattern string, handler func(ResponseWriter, *Request))` — Die übergebene Funktion `handler` wird direkt
  aufgerufen, wenn die HTTP-Anfrage mit dem `pattern` übereinstimmt.

Eine normale Funktion lässt sich mithilfe von `http.HandlerFunc` in einen `http.Handler` umwandeln:

```go
myHandler := http.HandlerFunc(handle)
```

Dies ist in größeren Systemen besonders für den Einsatz von Middleware oder Logging nützlich.

[FOLDOUT::Wie genau passiert das?]
`http.HandlerFunc` ist ein eigener Typ, dessen zugrunde liegender Typ eine Funktion mit der Signatur
`func(ResponseWriter, *Request)` ist:

```go
type HandlerFunc func(ResponseWriter, *Request)
```

Da `HandlerFunc` ein eigener Typ ist, können auf ihm Methoden definiert werden.
Die Standardbibliothek definiert dafür die Methode `ServeHTTP`:

```go
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
	f(w, r)
}
```

Die Methode ruft schlicht die zugrunde liegende Funktion auf.

Somit implementiert `HandlerFunc` das Interface `http.Handler`.
Eine gewöhnliche Handler-Funktion kann deshalb in einen `http.Handler` konvertiert werden:

```go
func handle(w http.ResponseWriter, r *http.Request) {
	...
}

var myHandler http.Handler = http.HandlerFunc(handle)
```

Genau diese Umwandlung nimmt `http.HandlerFunc` intern automatisch vor.
[ENDFOLDOUT]


#### Was ist der Unterschied?

Die Variante mit `http.Handler` ist interfacebasiert und bietet mehr Flexibilität in größeren Projekten.
Sie eignet sich besonders dann, wenn Middleware zum Einsatz kommt, Handler einen eigenen Zustand oder weitere
Abhängigkeiten (wie eine Datenbankverbindung) besitzen oder verschiedene Komponenten miteinander kombiniert werden
sollen.

Die Funktion `http.HandleFunc` hingegen ist besser für kleinere oder simplere Server geeignet, bei denen die
Abhängigkeitsverwaltung unkompliziert ist und eine hohe Modularität keine übergeordnete Rolle spielt.

[NOTICE]
Eine spezifische URL oder Route in einer Web-Anwendung, an der Anfragen entgegengenommen und verarbeitet werden, wird
oft als **Endpunkt** (Endpoint) bezeichnet.
[ENDNOTICE]

Schauen Sie sich die Dokumentation und Beispiele zu
['HandleFunc'](https://pkg.go.dev/net/http#HandleFunc)
und
['ListenAndServe'](https://pkg.go.dev/net/http#ListenAndServe)
an und schreiben Sie ein kleines Programm, in dem Sie analog zum Beispiel folgende Endpunkte registrieren:

[ER] Eine GET-Anfrage auf `/foo` gibt `"Foo!"` zurück.

[ER] Eine GET-Anfrage auf `/users` gibt `"User list"` zurück.

[ER] Eine GET-Anfrage auf `/users/` gibt `"User subpath"` zurück.

[ER] Eine GET-Anfrage auf `/users/{id}` liest den Platzhalter `id` aus
([hier](https://pkg.go.dev/net/http#Request.PathValue)
finden Sie eine geeignete Funktion dafür) und gibt (beispielsweise für den Pfad `/users/5`) `"User with ID: 5"` zurück.

Beantworten Sie nun die unten stehenden Fragen.
Schauen Sie sich bei Bedarf die
[Dokumentation von `ServeMux`](https://pkg.go.dev/net/http#hdr-Patterns-ServeMux)
an.

[EQ] Warum gewinnt `/users/{id}` gegenüber `/users/` bei `GET /users/5`?

[EQ] Welche Routen decken jeweils `/users` und `/users/`?

[EQ] Wie würden Sie einen neuen Endpunkt registrieren, der nur auf POST-Anfragen auf `/users/{id}` reagieren soll?

<!-- time estimate: 20 min -->


### `ServeMux`

Bisher haben wir `http.HandleFunc` verwendet, was die Handler implizit im globalen `http.DefaultServeMux` registriert.
Für mehr Kontrolle, bessere Testbarkeit und die Möglichkeit mehrerer Routing-Konfigurationen erzeugen wir den
`ServeMux` nun explizit.

[ER] Passen Sie Ihr Programm an:
Erstellen Sie einen eigenen `ServeMux` und registrieren Sie die bisherigen Endpunkte dort.
Übergeben Sie diesen `ServeMux` anschließend als zweites Argument an die Funktion `http.ListenAndServe()`.

[NOTICE]
`http.ServeMux` implementiert die Methode `ServeHTTP(http.ResponseWriter, *http.Request)` und ist somit selbst ein
`http.Handler`.
[ENDNOTICE]
<!-- time estimate: 5 min -->


### `http.Server`

Die Struktur `http.Server` ermöglicht eine präzisere Konfiguration Ihres HTTP-Servers, etwa die Einrichtung von TLS
(für `https`), spezifischen Timeouts oder Kontexten, die den HTTP-Handlern für jede Anfrage zur Verfügung stehen.

[EQ] Lesen Sie die
[Dokumentation von `http.Server`](https://pkg.go.dev/net/http#Server)
und erläutern Sie den Zusammenhang zwischen der Funktion `http.ListenAndServe(addr string, handler Handler)` und der
Methode `(*http.Server) ListenAndServe()`.
Der
[Quellcode von `http.ListenAndServe`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.3:src/net/http/server.go;l=3702)
könnte Ihnen dabei helfen.

[EQ] Lesen Sie die
[Dokumentation von `(*http.Server) Close() error`](https://pkg.go.dev/net/http#Server.Close)
sowie die
[Dokumentation von `(*http.Server) Shutdown(ctx context.Context) error`](https://pkg.go.dev/net/http#Server.Shutdown).
Was ist der Unterschied zwischen diesen beiden Methoden?

[ER] Verwenden Sie
[`http.Server.BaseContext`](https://pkg.go.dev/net/http#Server.BaseContext),
um jeder Anfrage einen Kontext zu übergeben, der den Startzeitpunkt des Servers enthält.
Passen Sie Ihre Endpunkte so an, dass sie in der Antwort zusätzlich den Wert `time.Since(startTimestamp)` ausgeben.
Der Wert `startTimestamp` muss dabei aus dem Kontext ausgelesen werden.

[NOTICE]
Für größere Projekte ist es eine gute Praxis, alle Endpunkte in einer separaten Datei wie `routes.go` zu registrieren.
So bleibt die API-Oberfläche Ihres Servers stets an einer zentralen Stelle übersichtlich zusammengefasst.
[ENDNOTICE]

Starten Sie Ihren HTTP-Server und führen Sie folgende Befehle in einem anderen Terminal aus:

[EC] `curl http://localhost:8080/foo`

[EC] `curl http://localhost:8080/users`

[EC] `curl http://localhost:8080/users/`

[EC] `curl http://localhost:8080/users/23`

[EC] `curl -X POST http://localhost:8080/foo`

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-http-server.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-http-server.go].
[ENDINSTRUCTOR]