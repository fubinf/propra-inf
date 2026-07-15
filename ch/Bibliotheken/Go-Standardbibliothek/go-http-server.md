title: "Go: 'http.Server'"
stage: draft
timevalue: 1
difficulty: 3
assumes: go-context, curl
---

[SECTION::goal::idea,experience]
Ich kann einen HTTP-Server in Go implementieren.
[ENDSECTION]

[SECTION::background::default]
Ein _Server_ ist ein Programm, das Anfragen von Clients wie Webbrowsern entgegennimmt und passende Antworten
zurücksendet. 
Er bildet das Herzstück des Internets.

In dieser Aufgabe lernen Sie, eigene HTTP-Server mithilfe der Standardbibliothek zu bauen.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

Diese Aufgabe basiert auf dem Paket 
[`net/http`](https://pkg.go.dev/net/http)
aus der Standardbibliothek.
Falls Ihnen das Thema noch völlig neu ist, finden Sie eine leicht verständliche Einführung in das Konzept eines
Webservers im
[Artikel "What is a web server?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server).

Außerdem benötigt diese Aufgabe ein grobes Verständnis der URL-Begrifflichkeit, wie beispielsweise "scheme", "domain",
"port", "path" und "parameters".
Eine Einführung dazu finden Sie im
[Artikel "What is a URL?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL).


### Bestandteile eines Servers

Ein HTTP-Server in Go besteht aus folgenden Teilen:

- Handler-Funktionen — Funktionen mit der Signatur `func(http.ResponseWriter, *http.Request)`, die für die Bearbeitung
  von HTTP-Anfragen zuständig sind;
- `ServeMux` — ein Teil, der eingehende HTTP-Anfragen den registrierten Handler-Funktionen zuordnet;
- `http.Server` — eine Struktur für zusätzliche Konfiguration.


### Handler-Funktionen

Es gibt zwei Methoden zur Registrierung eines HTTP-Handlers:

- `Handle(pattern string, handler http.Handler)` — `http.Handler` ist ein Interface mit einer einzigen Methode
  `ServeHTTP(ResponseWriter, *Request)`.
  Trifft eine HTTP-Anfrage auf ein `pattern` zu, wird die Methode `ServeHTTP` vom `handler` aufgerufen;
- `HandleFunc(pattern string, handler func(ResponseWriter, *Request))` — die Funktion `handler`
  wird aufgerufen, falls die HTTP-Anfrage mit dem `pattern` übereinstimmt.

Eine Umwandlung zwischen `handle func(http.ResponseWriter, r *http.Request)` und `http.Handler` ist mithilfe von
`http.HandlerFunc` möglich:

```go
myHandler := http.HandlerFunc(handle)
```

Dies könnte in größeren Systemen für Middleware oder Logging nützlich sein. 

[FOLDOUT::Wie genau passiert das?]
`http.HandlerFunc` ist ein eigener Typ, dessen zugrunde liegender Typ eine Funktion mit der Signatur
`func(ResponseWriter, *Request)` ist:

```go
type HandlerFunc func(ResponseWriter, *Request)
```

Da `HandlerFunc` ein eigener Typ ist, können auf ihm Methoden definiert werden.
Die Standardbibliothek definiert darauf die Methode `ServeHTTP`:

```go
func (f HandlerFunc) ServeHTTP(w ResponseWriter, r *Request) {
	f(w, r)
}
```

Die Methode ruft einfach die zugrunde liegende Funktion auf.

Dadurch implementiert `HandlerFunc` das Interface `http.Handler`.
Eine gewöhnliche Handler-Funktion kann deshalb in einen `http.Handler` umgewandelt werden:

```go
func handle(w http.ResponseWriter, r *http.Request) {
	...
}

var myHandler http.Handler = http.HandlerFunc(handle)
```

Genau diese Umwandlung übernimmt `HandleFunc` intern automatisch.
[ENDFOLDOUT]

#### Was ist der Unterschied?

Die Option mit `http.Handler` ist interfacebasiert und bietet mehr Flexibilität in größeren Projekten.
Sie eignet sich besonders dann, wenn Middleware eingesetzt wird, Handler eigenen Zustand oder weitere Abhängigkeiten
(beispielsweise eine Datenbankverbindung) besitzen oder verschiedene Komponenten miteinander kombiniert werden.

Die Funktion `http.HandleFunc` hingegen ist besser für kleinere oder einfachere Server geeignet, bei welchen die
Verwaltung von Abhängigkeiten unkompliziert ist und eine höhe Modularität keine wichtige Rolle spielt.

[NOTICE]
Eine spezifische URL/Route in einer Web-Anwendung, an der Anfragen entgegengenommen und verarbeitet werden, wird oft ein
__Endpunkt__ genannt.
[ENDNOTICE]

Schauen Sie sich die Dokumentation und Beispiele zu
['HandleFunc'](https://pkg.go.dev/net/http#HandleFunc)
und
['ListenAndServe'](https://pkg.go.dev/net/http#ListenAndServe)
an und schreiben Sie ein kleines Programm, wo Sie analog zum Beispiel folgende Endpunkte registrieren:

[ER] eine GET-Anfrage auf `/foo` gibt `"Foo!"` zurück;

[ER] eine Anfrage auf `/users` gibt `"User list"` zurück;

[ER] eine Anfrage auf `/users/` gibt `"User subpath"` zurück;

[ER] eine GET-Anfrage auf `users/{id}` liest den Platzhalter `id` aus
([hier](https://pkg.go.dev/net/http#Request.PathValue)
finden Sie eine geeignete Funktion dafür) und gibt `"User with ID: 5"` zurück, falls der ursprüngliche Pfad `users/5`
ist.

Beantworten Sie nun die Fragen unten.
Schauen Sie sich bei Bedarf die
[Dokumentation von `ServeMux`](https://pkg.go.dev/net/http#hdr-Patterns-ServeMux)
an.

[EQ] Warum gewinnt `/users/{id}` gegenüber `/users/` bei `GET /users/5`?

[EQ] Was passiert bei `GET /users` im Vergleich zu `GET /users/`?

[EQ] Wie würden Sie einen neuen Endpunkt registrieren, der nur auf POST-Anfragen auf `/users` reagieren soll?


### `ServeMux`

Bisher haben wir `http.HandleFunc` verwendet — das registriert Handler unbemerkt im globalen `http.DefaultServeMux`.
Für mehr Kontrolle, bessere Testbarkeit und um mehrere Routing-Konfigurationen zu ermöglichen, erzeugen wir den
`ServeMux` nun explizit.

[ER] Passen Sie Ihr Programm an, indem Sie nun einen eigenen `ServeMux` erzeugen und die existierenden Endpunkte dort
registrieren.
Übergeben Sie Ihren `ServeMux` anschließend als das zweite Argument an die Funktion `http.ListenAndServe()`.

[NOTICE]
`http.ServeMux` implementiert die Methode `ServeHTTP(http.ResponseWriter, *http.Request)` und ist somit selbst ein
`http.Handler`.
[ENDNOTICE]
<!-- time estimate: 10 min -->


### `http.Server`

Die Struktur `http.Server` ermöglicht eine präzisere Konfiguration Ihres HTTP-Servers, etwa die Einrichtung von TLS
(für `https`), verschiedenen Timeouts und Kontexten, die den HTTP-Handlern für jede Anfrage zur Verfügung stehen.

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
Was ist der Unterschied zwischen den zwei Funktionen?

[ER] Verwenden Sie
[`http.Server.BaseContext`](https://pkg.go.dev/net/http#Server.BaseContext),
um jeder Anfrage einen Kontext zu übergeben, der den Startzeitpunkt des Servers enthält.
Passen Sie Ihre Endpunkte so an, dass sie in der Antwort zusätzlich den Wert `time.Since(startTimestamp)` zurückgeben,
wobei `startTimestamp` __aus dem Kontext__ ausgelesen werden muss.

[NOTICE]
Für größere Projekte ist es eine gute Praxis, alle Endpunkte in einer Datei `routes.go` zu registrieren.
So bleibt die API-Oberfläche Ihres Servers stets an einer zentralen Stelle klar und übersichtlich.
[ENDNOTICE]

Starten Sie Ihren HTTP-Server und führen Sie folgende Befehle in einem anderen Terminal aus:

- [EC] `curl -X GET http://localhost:8080/foo`
- [EC] `curl -X GET http://localhost:8080/users`
- [EC] `curl -X GET http://localhost:8080/users/`
- [EC] `curl -X GET http://localhost:8080/users/23`

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
