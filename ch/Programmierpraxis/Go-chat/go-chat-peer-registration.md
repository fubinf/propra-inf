title: "Go HTTP Chat: Peer — Registrierung und Gesprächspartner"
stage: alpha
timevalue: 2.5
difficulty: 3
assumes: go-http-client, go-json, go-sync-mutex, go-goroutines, go-channels, go-context
requires: go-chat-lookup-server
---

[SECTION::goal::experience,product]
Mein Peer-Programm kann sich beim Lookup-Server an- und abmelden und die Adresse eines Gesprächspartners nachschlagen.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-chat-lookup-server] haben Sie den Server gebaut, der weiß, wer gerade online ist.
Jetzt bauen Sie die Gegenseite: das Peer-Programm, mit dem sich Benutzer_innen tatsächlich anmelden und einen
Gesprächspartner finden.

Zwei Peers können erst dann miteinander chatten, wenn jeder die Adresse des anderen kennt.
Bevor es also ans eigentliche Nachrichtenschreiben geht, muss ein Peer sich beim Lookup-Server anmelden (`register`),
sich wieder abmelden können (`unregister`) und die Adresse eines anderen Benutzers nachschlagen können
(`GET /{username}`).
[ENDSECTION]


[TOC]


[SECTION::instructions::detailed]

### Projekt-Setup

Legen Sie ein Modul `peer` an.
Empfohlene Struktur:

```
peer/
  config/         // Konfigurationsobjekt des Peers
  httpjson/       // Hilfsfunktionen für JSON
  input/          // unser Wrapper für die Terminaleingaben
  registration/   // An- und Abmelden
  setup/          // alles um die Initialisierung
  types/
  go.mod
  main.go
```

[ER] Implementieren Sie im Paket `setup` eine Funktion `MustGetLookupUrl() string`, welche die Kommandozeilenargumente
nach einem Eintrag der Form `lookup=192.168.178.76:8083` durchsucht (siehe
[Go by Example: Command-Line Arguments](https://gobyexample.com/command-line-arguments)),
die Lookup-URL zusammenstellt und zurückgibt (beispielsweise `"http://192.168.178.76:8083"`).
Fehlt das Argument, so soll die Funktion mit `panic` abbrechen — ohne Lookup-Server-Adresse kann der Peer nichts tun.

<!-- time estimate: 10 min -->

[ER] Implementieren Sie im Paket `setup` noch eine Funktion `MustGetFreeListener() net.Listener`, welche einen
TCP-Listener auf `"0.0.0.0:0"` mithilfe von
[`net.Listen()`](https://pkg.go.dev/net#Listen)
öffnet und zurückgibt (der Port `0` lässt das Betriebssystem einen freien Port zuweisen).
Schlägt das fehl, bricht die Funktion mit `panic` ab.

<!-- time estimate: 10 min -->


### Eine Konfiguration, die mehrere Goroutinen überleben wird

Der `Config`-Typ wird in [PARTREF::go-chat-peer-messaging] aus mehreren Goroutinen gleichzeitig gelesen
und geschrieben.
Bauen Sie ihn deshalb von Anfang an thread-sicher.

[ER] Legen Sie eine Struktur `Peer` im Paket `types` an.
Diese soll folgendermaßen aussehen:

```go
type Peer struct {
	Username string
	Address  string     // Adresse (host:port), an welcher der Peer Nachrichten empfängt, z. B. 192.168.178.49:50547
}
```

[ER] Definieren Sie im Paket `config` eine Struktur `Config` mit folgenden unexportierten Feldern:
`lookupUrl string`, `username string`, `peer *types.Peer` (der aktuelle Gesprächspartner) und `listener net.Listener`
(für eingehende Anfragen), geschützt durch einen `mu sync.Mutex`.
Fügen Sie außerdem ein exportiertes Feld `Client *http.Client` (für ausgehende Anfragen) hinzu, das sich alle
HTTP-Aufrufe teilen.

Implementieren Sie für `username` und `peer` einen Getter (z. B. `Username() string`) und einen Setter
(z. B. `SetUsername(string)`), die beide den Mutex sperren.
Für `lookupUrl` und `listener` genügt jeweils ein Getter.

Für die Konstruktion verwenden wir das **Functional-Options-Muster**.

Lesen Sie den
[Artikel "Functional options for friendly APIs" von Dave Cheney](https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis),
um zu verstehen, wie und aus welchen Gründen Programmierer zu diesem Muster gekommen sind.

[FOLDOUT::Eine Zusammenfassung, falls Sie den brillanten Artikel nicht lesen wollen]
Go kennt weder Default-Werte für Parameter noch überladene Konstruktoren.
Ein Konstruktor `New(lookupUrl string, listener net.Listener, ...)` müsste deshalb bei jedem neuen Feld seine Signatur
ändern, und alle Aufrufer müssten mitziehen.
Beim Functional-Options-Muster nimmt der Konstruktor stattdessen beliebig viele *Optionen* entgegen.
Eine Option ist eine Funktion, die die gerade entstehende Struktur verändert.
Was nicht als Option übergeben wird, behält seinen Default-Wert.
So kann man im Laufe der Entwicklung immer neue Optionen hinzufügen, ohne die Signatur des Konstruktors anpassen zu
müssen.
[ENDFOLDOUT]

Der Konstruktor sieht dann so aus:

```go
type Option func(*Config)

func New(options ...Option) *Config {
    config := &Config{Client: &http.Client{Timeout: 5 * time.Second}}
    for _, option := range options {
        option(config)
    }
    return config
}
```

<!-- time estimate: 20 min -->

Lesbar wird das Muster erst durch benannte Optionen.

[ER] Schreiben Sie im Paket `config` zwei Funktionen `WithLookupUrl(url string) Option` und
`WithListener(listener net.Listener) Option`, die jeweils eine Option zurückgeben, welche das entsprechende
Feld setzt, und verwenden Sie sie wie folgt:

```go
cfg := config.New(
    config.WithLookupUrl(setup.MustGetLookupUrl()),
    config.WithListener(setup.MustGetFreeListener()),
)
```

<!-- time estimate: 5 min -->

[ER] Fügen Sie der Struktur `Config` eine Methode `Port() int` hinzu, welche die Portnummer bei jedem Aufruf aus dem
vorhandenen `net.Listener` ausliest.
Da `net.Listener.Addr()` nur den generischen Typ `net.Addr` zurückgibt, benötigen Sie eine Typzusicherung auf den
konkreten Typ `*net.TCPAddr`, um an dessen Feld `Port` zu gelangen.

<!-- time estimate: 5 min -->


### Terminaleingaben lesen

Der Peer liest an mehreren Stellen Zeilen vom Terminal: beim Login, bei der Partnersuche und in
[PARTREF::go-chat-peer-messaging] im Chat.

Das Lesen vom Terminal blockiert, bis eine Zeile kommt; währenddessen kann das Programm nicht auf `Ctrl+C` reagieren.
Deshalb findet es in einer separaten Goroutine statt.
Wenn aber jeder dieser drei Teile eine eigene Leser-Goroutine starten würde, könnten sie sich gegenseitig
Zeilen wegnehmen, und zwar zufällig.
Stattdessen implementieren Sie in Ihrem Chat eine zentrale Goroutine, die von `os.Stdin` liest und die Zeilen
in einen Kanal schreibt.
Der Rest des Programms holt sich diese Zeilen über die Funktion `ReadLine` und weiß weder etwas vom Kanal
noch von `os.Stdin`.

[ER] Legen Sie im Paket `input` zwei unexportierte Variablen an: einen mit `make` erzeugten Kanal
`stdInputs chan string` und `once sync.Once`.
[`sync.Once`](https://pkg.go.dev/sync#Once)
verwenden Sie hier, um die Lese-Goroutine genau einmal zu starten.

[ER] Implementieren Sie eine unexportierte Funktion `readStdin()`, die mit einem
[`bufio.Scanner`](https://pkg.go.dev/bufio#Scanner)
Zeile für Zeile von `os.Stdin` liest, Leerzeichen und Zeilenumbrüche am Anfang und Ende der Zeile entfernt
und sie anschließend in den Kanal `stdInputs` schickt.
Am Ende der Eingabe schließt sie den Kanal.

[ER] Implementieren Sie eine Funktion `ReadLine(ctx context.Context) (line string, ok bool)`, die beim
ersten Aufruf `readStdin` als Goroutine startet und dann mit `select` auf `ctx.Done()` und die nächste
Zeile aus dem Kanal `stdInputs` wartet.
Sie gibt die Zeile mit `ok == true` zurück, bei Abbruch von `ctx` oder Ende der Eingabe `ok == false`.

[HINT::Ich verstehe nicht, wie man die Goroutine nur beim ersten Aufruf startet]
Dafür gibt es eine Methode
[`sync.Once.Do`](https://pkg.go.dev/sync#Once.Do).
`once.Do(f)` führt `f` beim ersten Aufruf aus und tut bei allen weiteren Aufrufen nichts.
[ENDHINT]

[HINT::Wie erkenne ich das Ende der Eingabe?]
Ein Empfang von einem geschlossenen Kanal gelingt sofort und liefert den Nullwert.
Mit der Form `line, ok := <-kanal` können Sie überprüfen, ob der Kanal geschlossen ist (`ok == false`).
Dieses `ok` können Sie direkt zurückgeben.
[ENDHINT]

<!-- time estimate: 20 min -->


### Registrieren (Login)

[ER] Beim An- und beim Abmelden schickt der Peer denselben JSON-Payload `{"username": ..., "port": ... }`
an den Lookup-Server.
Legen Sie dafür im Paket `types` eine Struktur `NameAndPortMessage` an, die die Felder `Name string` und
`Port int` mit den JSON-Tags `username` und `port` entsprechend beinhaltet.

<!-- time estimate: 5 min -->

Login, Logout und später das Senden von Chat-Nachrichten schicken jeweils JSON per POST und müssen die
Antwort gleich auswerten.
Damit Sie diesen Code nur einmal schreiben, lagern Sie ihn in eine Hilfsfunktion aus.

[ER] Implementieren Sie im Paket `httpjson` eine Funktion
`PostJSON(client *http.Client, url string, payload any) error`, welche einen beliebigen `payload` als
JSON per POST an die `url` schickt.
Wenn die Konvertierung in JSON oder die Anfrage fehlschlägt, gibt sie diesen Fehler zurück.
Antwortet der Server nicht mit `200`, gibt sie einen Fehler aus Status und Antworttext zurück, beispielsweise
`409 Conflict: this username is already taken`.
Entfernen Sie dabei Leerzeichen und Zeilenumbrüche am Anfang und Ende mittels der Funktion `strings.TrimSpace()`.
`PostJSON` gibt selbst nichts aus, sondern überlässt das den Aufrufern.

<!-- time estimate: 10 min -->

[ER] Implementieren Sie im Paket `registration` eine Funktion
`Login(ctx context.Context, cfg *config.Config, path string) (string, error)`, welche:

- den Benutzernamen in einer Schleife abfragt (`"What's your username?: "`) und dafür `input.ReadLine(ctx)` verwendet.
  Diese Schleife kann mit `:q` abgebrochen werden;
- eine `NameAndPortMessage` mittels `httpjson.PostJSON()` an `cfg.LookupUrl()+path` schickt.
  `path` ist dabei der Pfad, unter dem Ihr Lookup-Server Registrierungen entgegennimmt;
- den Benutzernamen zurückgibt, falls `httpjson.PostJSON()` keinen Fehler liefert;
- die Fehlermeldung von `httpjson.PostJSON()` ausgibt und erneut nach einem Benutzernamen fragt, falls
  die Registrierung fehlschlägt;
- bei Erfolg `nil` als Fehler zurückgibt, bei `:q`, Ende der Eingabe oder Abbruch des Kontexts
  (`ReadLine` liefert in diesem Fall `ok == false`) einen Fehler mit der Nachricht `canceled`.

[HINT::Welchen Wert übergebe ich für `path`?]
Schauen Sie in [PARTREF::go-chat-lookup-server] nach, unter welchen Pfaden Ihr Lookup-Server seine Handler
registriert hat.
Login und Logout bekommen ihren Pfad als Parameter, damit diese Pfade nur an einer Stelle im Peer stehen,
am besten als Konstanten in `main.go`.

[HINT::Ich komme trotzdem nicht drauf]
`Login` bekommt `"/register"`, `Logout` bekommt `"/unregister"`.
[ENDHINT]
[ENDHINT]

<!-- time estimate: 10 min -->

[ER] Richten Sie in `main` mittels
[`signal.NotifyContext()`](https://pkg.go.dev/os/signal#NotifyContext)
einen Kontext ein, der bei `Ctrl+C` abbricht, und reichen Sie ihn später über `testScenario` an `Login`
und `GetPeer` durch:

```go
ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
defer stop()
```

`stop` spielt hier dieselbe Rolle wie die `CancelFunc` aus [PARTREF::go-context]:
Sie gibt die Signalbehandlung wieder frei und muss deshalb aufgerufen werden.

<!-- time estimate: 5 min -->


### Abmelden (Logout)

[ER] Implementieren Sie im Paket `registration` die Funktion `Logout(cfg *config.Config, path string) error`:

- schickt eine `NameAndPortMessage` mittels `httpjson.PostJSON()` an `cfg.LookupUrl()+path`;
- gibt bei Erfolg `nil` zurück, sonst den Fehler von `httpjson.PostJSON()`.

<!-- time estimate: 5 min -->


### Gesprächspartner suchen

[ER] Implementieren Sie im Paket `setup` die Funktion
`GetPeer(ctx context.Context, cfg *config.Config) (types.Peer, error)`,
die im Wesentlichen der Funktion `Login` ähnelt und Folgendes tut:

- fragt `"Who do you want to chat with?: "` in einer Schleife mit `input.ReadLine(ctx)` ab;
- gibt bei `:q`, Ende der Eingabe oder Abbruch von `ctx` einen Fehler mit der Nachricht `canceled` zurück;
- gibt `you cannot chat with yourself` aus und fragt erneut, falls der Benutzer seinen eigenen Namen
  (`cfg.Username()`) eingegeben hat;
- schickt eine GET-Anfrage an `cfg.LookupUrl()+"/"+username` und dekodiert die Antwort (`{"addr": "..."}`), wenn der
  Benutzer etwas eingegeben hat (`username`);
- zeigt eine informative Fehlermeldung an und fragt erneut nach einem Benutzernamen, wenn der Server mit einem Fehler
  antwortet oder die empfangene Adresse `addr` leer ist.

<!-- time estimate: 20 min -->


### Alles zusammenstecken

[ER] Schreiben Sie eine Funktion `testScenario(ctx context.Context)`, die

1. die Lookup-URL ausliest, einen freien TCP-Listener findet und eine `Config` erstellt,
2. `Login` mit dem Registrierungspfad aufruft,
3. nach erfolgreichem Einloggen eine Meldung `Logged in as <name>` ausgibt und `username` in `Config` aktualisiert,
4. bei Erfolg `GetPeer` aufruft und `<partner> is at <host:port>` ausgibt (z. B. `bob is at 192.168.178.42:62013`),
5. beim Beenden `Logout` mit dem Abmeldepfad aufruft,
6. nach erfolgreichem Ausloggen eine Meldung `<name> logged out` ausgibt.

(Bei `bob` sind die Meldungen entsprechend `Logged in as bob`, `alice is at xyz` und `bob logged out`.)

Rufen Sie die Funktion `testScenario` in Ihrer `main`-Funktion auf.
Denken Sie daran, `Logout()` auch dann aufzurufen, wenn das Programm mittels `Ctrl+C` beendet wird (`defer`).

<!-- time estimate: 10 min -->


### Testen

Starten Sie den Lookup-Server aus der vorigen Aufgabe in einem eigenen Terminal.
Für den Test brauchen Sie zwei weitere Terminals: eines für Alice und eines für Bob.
Das Kommandoprotokoll besteht nur aus den Abschnitten dieser beiden Terminals; das Terminal vom Lookup-Server gehört
nicht hinein.

[EC] Terminal Alice: `go run . lookup=localhost:8083`

[EC] Terminal Bob: `go run . lookup=localhost:8083`

Gehen Sie dann in genau dieser Reihenfolge vor:

1. Melden Sie sich in Alices Terminal als `alice` an.
2. Versuchen Sie in Bobs Terminal, sich ebenfalls als `alice` anzumelden.
   Ihr Peer sollte die Fehlermeldung des Servers ausgeben und erneut nach einem Benutzernamen fragen.
   Melden Sie sich nun als `bob` an.
3. Suchen Sie in Alices Terminal nach `bob`. Alices Peer beendet sich dann von selbst.
4. Suchen Sie in Bobs Terminal nach `alice`. Alice ist zu diesem Zeitpunkt nicht mehr angemeldet.
5. Beenden Sie Bobs Peer mit `Ctrl+C`.

[EC] Terminal Bob: Starten Sie Bobs Peer noch einmal mit `go run . lookup=localhost:8083`
und brechen Sie die Anmeldung mit `:q` ab.

Übertragen Sie die beiden Abschnitte wie in [PARTREF::Kommandoprotokolle] beschrieben in Ihre Protokolldatei:
**zuerst den kompletten Inhalt von Alices Terminal, direkt dahinter den kompletten Inhalt von Bobs Terminal.**
Jeder Abschnitt beginnt mit seinem eigenen Prompt und `go run`-Kommando.

<!-- time estimate: 15 min -->

[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Lösungen]

**Kommandoprotokoll**
[PROT::ALT:go-chat-peer-registration.prot]

[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::peer].
[ENDINSTRUCTOR]
