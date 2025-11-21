title: "Go: 'http.Server'"
stage: draft
timevalue: 1
difficulty: 3
assumes: go-context, go-pointers
---

[SECTION::goal::idea,experience]
Ich kann einen HTTP-Server in Go implementieren.
[ENDSECTION]

[SECTION::background::default]
Ein _Server_ ist ein Programm, das Anfragen von Clients wie Webbrowsern entgegennimmt 
und passende Antworten zurücksendet. 
Er bildet das Herzstück des Internets.

In dieser Aufgabe lernen Sie, eigene HTTP-Server zu bauen — schnell, effizient und mit 
minimalem Code dank der starken Standardbibliothek.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

Diese Aufgabe basiert auf dem Paket 
[`net/http`](https://pkg.go.dev/net/http)
aus der Standardbibliothek.
Falls Ihnen das Thema noch völlig neu ist, finden Sie eine leicht verständliche Einführung 
in das Konzept eines Webservers im
[Artikel "What is a web server?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server).


### Bestandteile eines Servers

Ein HTTP-Server in Go besteht aus folgenden Teilen:

- `ServeMux` — ordnet eingehende HTTP-Anfragen den registrierten Handler-Funktionen zu;
- Handler-Funktionen — sind jeweils für Bearbeitung einer HTTP-Anfrage zuständig.
  Sie bekommen eine Anfrage (`http.Request`) und schreiben mittels `http.ResponseWriter` 
  eine HTTP-Antwort;
- `http.Server` — optional für zusätzliche Konfigurationen.


### `ServeMux`

Lesen Sie den
[Abschnitt über 'ServeMux' in der Dokumentation von `net/http`](https://pkg.go.dev/net/http#ServeMux),
um ein Gefühl dafür zu bekommen, wie die Zuordnung von Anfragen den Handlern abläuft.

[HINT::Die URL-Begrifflichkeit ist mir neu und unverständlich]
Für diese Aufgabe genügt ein grobes Verständnis der Begriffe "scheme", "domain", "port", 
"path" und "parameters".

Eine verständliche Einführung dazu finden Sie im
[Artikel "What is a URL?" auf developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL).
[ENDHINT]

[EQ] Wie wird ein `ServeMux` erzeugt?

[EQ] Was passiert, wenn mehrere Muster auf eine Anfrage passen? 
Wie entscheidet der `ServeMux`, welchen Handler er aufruft?

[EQ] Wie unterscheiden sich Muster `/users` und `/users/`? 
Welche Anfragen werden welchem Muster zugeordnet?

[EQ] Wie kann man explizit angeben, welche HTTP-Methode für ein bestimmtes Muster erlaubt ist?

<!-- time estimate: 10 min -->


### Handler-Funktionen

Die Standardbibliothek bietet zwei Funktionen zur Registrierung eines HTTP-Handlers:

- `Handle(pattern string, handler http.Handler)` — `http.Handler` ist ein Interface 
  mit einer einzigen Methode `ServeHTTP(ResponseWriter, *Request)`. 
  Stimmt die HTTP-Anfrage mit dem `pattern` überein, wird die Methode `ServeHTTP` 
  des übergebenen Handlers aufgerufen;
- `HandleFunc(pattern string, handler func(ResponseWriter, *Request))` — die Funktion `handler` 
  wird aufgerufen, falls die HTTP-Anfrage mit dem `pattern` übereinstimmt.

[NOTICE]

- Die Funktion `http.HandlerFunc(f func(http.ResponseWriter, *http.Request)) http.Handler`
ermöglicht Konvertierung einer Funktion `f` zu einem `http.Handler`, der die Funktion `f` aufruft.
- `http.ServeMux` implementiert die Methode `ServeHTTP(http.ResponseWriter, *http.Request)` und ist
  somit selbst ein `http.Handler`. 
[ENDNOTICE]

__Was ist der Unterschied?__

Die Option mit `http.Handler` ist interface-basiert und bietet mehr Flexibilität in größeren 
Projekten. 
Sie eignet sich besonders dann, wenn Middleware eingesetzt wird, Handler eigenen Zustand oder 
weitere Abhängigkeiten (beispielsweise eine Datenbankverbindung) besitzen oder verschiedene 
Komponenten miteinander kombiniert werden sollen.

Die Funktion `HandleFunc` dagegen ist besser geeignet für kleinere beziehungsweise einfachere 
Server, bei denen die Verwaltung von Abhängigkeiten unkompliziert ist und eine höhe Modularität 
des Codes keine wichtige Rolle spielt.

[NOTICE]
Eine spezifische URL/Route in einer Web-Anwendung, wo Anfragen entgegengenommen und
verarbeitet werden, wird oft ein __Endpunkt__ genannt.
[ENDNOTICE]

[EQ] Lesen Sie Dokumentation und Beispiele zu 
['HandleFunc'](https://pkg.go.dev/net/http#HandleFunc)
und
['ListenAndServe'](https://pkg.go.dev/net/http#ListenAndServe).
Wie wird ein HTTP-Server gestartet?
Wie teilt man dem Paket `http` mit, dass die Endpunkte aus einem konkreten `ServeMux`
verwendet werden sollen?

[ER] Schreiben Sie einen HTTP-Server, der HTTP-Anfragen auf Port `:8080` entgegennimmt.
Benutzen Sie einen expliziten `ServeMux` und registrieren Sie einen Endpunkt `"/hello"`, 
wo die Antwort `"Hello, World!"` lautet.
Die Antwort kann mittels `responseWriter.Write([]byte)` geschrieben werden.

[NOTICE]
Manche Browser fügen am Ende der URL automatisch ein `/` hinzu, wodurch es so wirken kann,
als würde Ihr Endpunkt nicht funktionieren.

Um solche Inkonsistenzen zu vermeiden, verwenden wir `curl` zum Testen.
Das folgende Kommando sendet eine HTTP-Anfrage an den Endpunkt `/your_path` auf Port `8080`:

    curl -X GET http://localhost:8080/your_path
[ENDNOTICE]

[ER] Registrieren Sie einen weiteren Endpunkt `"/echo/"`, der den Pfad (path) der
ursprünglichen URL als Antwort zurückgibt.

[FOLDOUT::`DefaultServeMux`]
Wird der Funktion `http.ListenAndServe` kein `ServeMux` übergeben, so benutzt
das Paket `http` einen `DefaultServeMux`.

Funktionen `http.Handle(pattern string, handler http.Handler)` und
`http.HandleFunc(pattern string, handler func(w http.ResponseWriter, r *http.Request))` sind nur 
Wrapper-Funktionen, die intern entsprechende Methoden von `DefaultServeMux` benutzen.
[ENDFOLDOUT]

<!-- time estimate: 20 min -->


### `http.Server`

Die Struktur `http.Server` ermöglicht eine präzisere Konfiguration Ihres HTTP-Servers, etwa die 
Einrichtung von TLS (für `https`), verschiedenen Timeouts, einem optionalen Logger (für 
Laufzeitfehler) sowie die Übergabe von Kontexten, die den HTTP-Handlern für jede Anfrage
zur Verfügung stehen.

[EQ] Lesen Sie die 
[Dokumentation von `http.Server`](https://pkg.go.dev/net/http#Server)
und erläutern Sie den Zusammenhang zwischen der Funktion 
`http.ListenAndServe(addr string, handler Handler)`
und der Methode `(*http.Server) ListenAndServe()`.
Schauen Sie sich den 
[Quellcode von `http.ListenAndServe`](https://cs.opensource.google/go/go/+/refs/tags/go1.25.3:src/net/http/server.go;l=3702)
an, wenn nötig.

[EQ] Lesen Sie die 
[Dokumentation von `(*http.Server) Close() error`](https://pkg.go.dev/net/http#Server.Close)
sowie die
[Dokumentation von `(*http.Server) Shutdown(ctx context.Context) error`](https://pkg.go.dev/net/http#Server.Shutdown).
Was ist der Unterschied zwischen den zwei Funktionen?

[ER] Verwenden Sie das Feld `http.Server.BaseContext`, um jeder Anfrage einen Kontext zu übergeben,
der den Startzeitpunkt des Servers enthält.
Passen Sie Ihre Endpunkte so an, dass sie in der Antwort zusätzlich den Wert 
`time.Since(startTimestamp)` zurückgeben, wobei `startTimestamp` __aus dem Kontext__ 
ausgelesen werden muss.

[NOTICE]
Für größere Projekte ist es eine gute Praxis, alle Endpunkte in einer Datei 
`routes.go` zu registrieren.
So bleibt die API-Oberfläche Ihres Servers stets an einer zentralen Stelle klar und übersichtlich.
[ENDNOTICE]

Starten Sie Ihren HTTP-Server und führen Sie folgende Befehle in einem anderen Terminal aus:

- [EC] `curl -X GET http://localhost:8080/hello`
- [EC] `curl -X GET http://localhost:8080/hello/`
- [EC] `curl -X GET http://localhost:8080/echo/`
- [EC] `curl -X GET http://localhost:8080/echo/test`

<!-- time estimate: 20 min -->
[ENDSECTION]

[SECTION::submission::information,snippet,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

<!-- @PROGRAM_TEST_SKIP: reason="Infinite loop program, requires manual interruption" manual_test_required=true -->

[INSTRUCTOR::Lösungen]
**Kommandoprotokoll**
[PROT::ALT:go-http-server.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe als ausführbare Datei hier:
[TREEREF::/Bibliotheken/Go-Standardbibliothek/go-http-server.go].
[ENDINSTRUCTOR]
