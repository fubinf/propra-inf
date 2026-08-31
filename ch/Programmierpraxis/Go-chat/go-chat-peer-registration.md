title: "Go HTTP Chat: Peer — Registrierung und Gesprächspartner"
stage: alpha
timevalue: 2.25
difficulty: 3
assumes: go-http-client, go-json
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
  registration/   // An- und Abmelden
  setup/          // alles um die Initialisierung
  types/
  go.mod
  main.go
```

[ER] Implementieren Sie im Paket `setup` eine Funktion `MustGetLookupUrl() string`, welche die Kommandozeilenargumente
nach einem Eintrag der Form `lookup=192.168.178.76:8083` durchsucht (siehe
[Go by Example: Command-Line Arguments](https://gobyexample.com/command-line-arguments)),
die Lookup-Url zusammenstellt und zurückgibt (beispielsweise `"http://192.168.178.76:8083"`).
Fehlt das Argument, so soll die Funktion mit `panic` abbrechen — ohne Lookup-Server-Adresse kann der Peer nichts tun.

<!-- time estimate: 10 min -->

[ER] Implementieren Sie im Paket `setup` noch eine Funktion `MustGetFreeListener() net.Listener`, welche einen
TCP-Listener auf `"0.0.0.0:0"` mithilfe von
[`net.Listen()`](https://pkg.go.dev/net#Listen)
öffnet und zurückgibt (der Port `0` lässt das Betriebssystem einen freien Port zuweisen).
Schlägt das fehl, wird der Fehler protokolliert und das Programm mittels
[`log.Fatalf`](https://pkg.go.dev/log#Fatalf)
beendet.

<!-- time estimate: 10 min -->


### Eine Konfiguration, die mehrere Goroutinen überleben wird

Auch wenn Sie in dieser Aufgabe noch keine eigenen Goroutinen starten:
Der `Config`-Typ wird in der nächsten Aufgabe aus mehreren Goroutinen gleichzeitig gelesen und geschrieben.
Bauen Sie ihn deshalb von Anfang an thread-sicher.

[ER] Legen Sie eine Struktur `Peer` im Paket `types` an.
Diese soll folgendermaßen aussehen:

```go
type Peer struct {
	Username string
	Address  string     // URL-Adresse, an welcher der Peer Nachrichten empfängt, z. B. http://192.168.178.49:50547
}
```

[ER] Definieren Sie im Paket `config` eine Struktur `Config` mit (mindestens) folgenden unexportierten Feldern:
`lookupUrl`, `username string`, `peer *Peer` (der aktuelle Gesprächspartner) und `listener net.Listener`
(für eingehende Anfragen), geschützt durch einen `mu sync.Mutex`.
Fügen Sie außerdem ein exportiertes Feld `Client *http.Client` (für ausgehende Anfragen) hinzu, das sich alle
HTTP-Aufrufe teilen.

Für jedes unexportierte Feld brauchen Sie einen Getter (z. B. `Username() string`) und einen Setter
(z. B. `SetUsername(string)`), die beide den Mutex sperren.

Verwenden Sie für die Konstruktion das **Functional-Options-Muster**:

```go
type Option func(*Config)

func New(options ...Option) *Config {
    config := &Config{Client: &http.Client{}}
    for _, option := range options {
        option(config)
    }
    return config
}
```

So lässt sich `Config` später bequem konfigurieren:

```go
cfg := config.New(func(c *config.Config) {
    c.SetLookupUrl(setup.MustGetLookupUrl())
})
```

<!-- time estimate: 20 min -->

[ER] Fügen Sie der Struktur `Config` eine Methode `Port() int` hinzu, welche die Portnummer bei jedem Aufruf aus dem
vorhandenen `net.Listener` ausliest.
Da `net.Listener.Addr()` nur den generischen Typ `net.Addr` zurückgibt, benötigen Sie eine Typzusicherung auf den
konkreten Typ `*net.TCPAddr`, um an dessen Feld `Port` zu gelangen.

<!-- time estimate: 5 min -->


### Registrieren (Login)

[ER] Implementieren Sie in einem neuen Paket `registration` die Funktion
`Login(ctx context.Context, cfg *config.Config, path string, onExit func()) (name string, err error)`, welche: 

- den Benutzernamen in einer Schleife abfragt (`"What's your username?: "`).
  Diese Schleife kann mit `:q` abgebrochen werden;
- einen `POST` an `cfg.LookupUrl()+path` mit JSON-Payload `{"username": ..., "port": ... }` schickt
  (hier muss `port` eine Zeichenkette sein!)
- den Benutzernamen zurückgibt, falls die Registrierung erfolgreich war (Statuscode `200`);
- die Fehlermeldung des Servers ausgibt und erneut nach einem Benutzernamen fragt, falls die Registrierung fehlschlägt;
- die Funktion `onExit()` aufruft und einen leeren String zurückgibt, sobald der Benutzer `:q` eingegeben hat;
- sofort abbricht, sobald `ctx` abgebrochen wurde.
- gibt bei Erfolg `nil` als Fehler zurück; bei `:q` oder Abbruch des Kontexts einen Fehler Ihrer Wahl.

[HINT::Wie kombiniere ich Terminal-Eingabe mit `ctx.Done()`?]
Lesen Sie die Eingabe in einer eigenen Goroutine und schicken Sie das Ergebnis über einen Kanal.
So können Sie mit `select` sowohl auf die Eingabe als auch auf den Kontext reagieren:

```go
input := make(chan string)
go func() {
    line, _ := reader.ReadString('\n')
    input <- strings.TrimRight(line, "\n")
}()

select {
case <-ctx.Done():
    // abbrechen
case username := <-input:
    // weiterverarbeiten
}
```
[ENDHINT]

<!-- time estimate: 25 min -->

[ER] Richten Sie in `main` einen Kontext ein, der bei `Ctrl+C` abbricht, und reichen Sie ihn an `Login` durch:

```go
ctx, _ := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
```

(Eine vollständige nebenläufige Ablaufsteuerung mit mehreren Goroutinen folgt erst in der nächsten Aufgabe —
hier reicht dieser Kontext aus.)

<!-- time estimate: 5 min -->


### Abmelden (Logout)

[ER] Implementieren Sie die Funktion `Logout(cfg *types.Config, path string) error`:

- Schickt einen `POST` an `cfg.LookupUrl()+path` mit demselben JSON-Payload wie beim Einloggen.
- Gibt bei Erfolg `nil` zurück, sonst einen Fehler mit einer informativen Meldung (Statuscode + Server-Antwort).

[ER] Login und Logout verschicken denselben JSON-Payload.
Fassen Sie ihn im Paket `types` als gemeinsame Struktur `NameAndPortMessage` zusammen, die die Felder `Name string` und
`Port string` mit den JSON-Tags `username` und `port` entsprechend beinhaltet.

<!-- time estimate: 20 min -->


### Gesprächspartner suchen

[ER] Implementieren Sie im Paket `setup` die Funktion
`GetPeer(ctx context.Context, config *types.Config, onGoBack func()) (peer types.Peer, err error)`,
welche sich im Wesentlichen der Funktion `Login` ähnelt und folgendes tut:

- fragt `"Who do you want to chat with?: "` in einer Schleife ab;
- ruft `onGoBack()` auf und gibt einen Fehler zurück, falls der Benutzer `:q` eingegeben hat;
- schickt eine GET-Anfrage an `config.LookupUrl()+"/"+username` und dekodiert die Antwort (`{"addr": "..."}`), wenn der
  Benutzer etwas eingegeben hat (`username`);
- zeigt eine informative Fehlermeldung an und fragt erneut nach einem Benutzernamen, wenn der Server mit einem Fehler
  antwortet oder die empfangene Adresse `addr` leer ist;
- Bricht ab, sobald `ctx` abgebrochen wurde.

<!-- time estimate: 20 min -->


### Alles zusammenstecken

[ER] Schreiben Sie eine Funktion `testScenario(ctx context.Context)`, die

1. die Lookup-URL ausliest, einen freien TCP-Listener findet und eine `Config` erstellt,
2. `Login` aufruft,
3. nach erfolgreichem Einloggen eine Meldung ausgibt (beispielsweise `Logged in as Alice`) und `username` in `Config`
   aktualisiert,
4. bei Erfolg `GetPeer` aufruft und die gefundene Adresse ausgibt (z. B. `"Bob is at 192.168.178.42:62013"`),
5. beim Beenden `Logout` aufruft,
6. nach erfolgreichem Ausloggen eine Meldung ausgibt (beispielsweise `Alice logged out`);
7. den TCP-Listener wieder schließt (`cfg.Listener().Close()`).

Rufen Sie die Funktion `testScenario` in Ihrer `main`-Funktion auf.

Denken Sie daran, `Logout()` und `Listener().Close()` auch dann aufzurufen, wenn das Programm mittels `Ctrl+C`
beendet wird (`defer`).

<!-- time estimate: 10 min -->


### Testen

Starten Sie den Lookup-Server aus der vorigen Aufgabe und in zwei weiteren Terminals je eine Instanz Ihres
Peer-Programms (`go run . lookup=localhost:8083`).

1. Melden Sie sich im ersten Terminal als `alice` an, im zweiten als `bob`;
2. Suchen Sie in Alices Terminal nach `bob` (`alice` beendet sich dann automatisch);
3. Suchen Sie in Bobs Terminal nach `alice` (die zu dem Zeitpunkt nicht mehr existiert);
4. Beenden Sie Bobs Peer mit `Ctrl+C`.

[EC] (Terminal-Trace Alice)

[EC] (Terminal-Trace Bob)

<!-- time estimate: 10 min -->

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
