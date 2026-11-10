title: "Go HTTP Chat: Peer — Nachrichtenaustausch"
stage: alpha
timevalue: 2.5
difficulty: 3
assumes: go-goroutines, go-channels, go-context, go-enums, go-http-client, go-http-server
requires: go-chat-lookup-server, go-chat-peer-registration
---

[SECTION::goal::experience,product]
Ich habe Senden und Empfangen von Nachrichten zwischen Peers implementiert.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::go-chat-peer-registration] kann Ihr Peer sich bereits an- und abmelden und die Adresse eines
Gesprächspartners nachschlagen.
Jetzt fehlt nur noch das eigentliche Verschicken und Empfangen von Nachrichten.

Unser Chat hat keinen zentralen Relay-Server — Nachrichten gehen direkt von Peer zu Peer.
Jeder Peer ist gleichzeitig **HTTP-Client** (zum Verschicken) und **HTTP-Server** (zum Empfangen).
Beide müssen nebenläufig laufen, während gleichzeitig die Terminal-Eingabe verarbeitet wird.

Außerdem soll es jederzeit möglich sein, mit `:q` eine Stufe zurückzuspringen
(beispielsweise vom Chat zurück zur Partnerwahl).
Dazu bauen wir den Programmablauf als kleine Zustandsmaschine.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]

### Nachrichtentyp

[ER] Definieren Sie im Paket `types` einen Typ `Message` mit den Feldern `Sender`, `Receiver`, `Content`
(vom Typ `string`) und `CreatedAt` (`time.Time`).
Fügen Sie den Feldern passende JSON-Tags hinzu.

<!-- time estimate: 5 min -->


### Das Protokoll

Bevor Sie programmieren, legen wir fest, wer mit wem worüber redet, wer auf wen wartet und wer am Ende aufräumt.
Eine solche Festlegung nennt man ein **Protokoll**.
Bei nebenläufigen und verteilten Programmen stecken die schwierigsten Fehler selten in einer einzelnen Funktion,
sondern im Zusammenspiel: Eine Goroutine wartet auf eine Nachricht, die nie kommt; jemand schreibt in einen Kanal,
den ein anderer schon geschlossen hat; ein Server nimmt Nachrichten an, obwohl niemand mehr zuhört.
Solche Fehler findet man kaum durch Testen, weil sie nur bei ungünstigem Timing auftreten.
Man vermeidet sie, indem man das Protokoll **vor** der Implementierung aufschreibt und sich dann daran hält.
Das gilt weit über Go hinaus.

Lesen Sie diesen Abschnitt deshalb sorgfältig; die Anforderungen weiter unten setzen ihn um.

#### Zwischen zwei Peers (HTTP)

- Jeder Peer betreibt ab Programmstart für seine gesamte Laufzeit **einen** Empfänger-Server, und zwar auf dem Port,
  den er beim Lookup-Server angemeldet hat;
- Eine Nachricht wird als `POST /{username}` mit einer `Message` als JSON-Body verschickt;
  `{username}` ist der Name des Empfängers.
- Der Empfänger antwortet so:
    - `200 OK`: Nachricht angenommen;
    - `400 Bad Request`: Der Body ist keine gültige `Message`;
    - `404 Not Found`: Unter diesem Namen ist auf diesem Peer niemand angemeldet;
    - `409 Conflict`: Der Empfänger chattet gerade nicht mit dem Absender (er ist beispielsweise in der Partnerwahl
      oder chattet mit jemand anderem);
    - `503 Service Unavailable`: Der Empfänger kommt mit dem Anzeigen nicht hinterher;
- Bei jedem Status außer `200` zeigt der Absender eine Fehlermeldung an;
  die Nachricht ist dann verloren.


#### Innerhalb eines Peers (Kanäle)

Ein _Chat_ beginnt mit der Wahl eines Partners und endet mit `:q`, dem Ende der Eingabe oder `Ctrl+C`.
Manche Kanäle leben nur während eines Chats, andere während des ganzen Programms.

Für Kanäle gelten drei Regeln:

1. **Wer schreibt, schließt.** Ein Leser schließt einen Kanal nie.
2. **Hat ein Kanal mehrere Schreiber, wird er gar nicht geschlossen.**
   Seine Leser müssen auf anderem Weg erfahren, wann sie aufhören sollen.
3. **Darf ein Schreiber nicht warten, schreibt er mit `select` und `default`.**
   Ist gerade kein Platz im Kanal, verwirft er den Wert und meldet das, statt zu blockieren.

Daraus ergibt sich für unsere Kanäle:

- **`incoming`** lebt während des ganzen Programms.
  Schreiber sind die Handler des Receivers (einer pro Anfrage),
  Leser ist `displayMessages` des jeweils laufenden Chats.
  Weil es mehrere Schreiber gibt, wird der Kanal nie geschlossen (Regel 2).
- **`outgoing`** lebt einen Chat lang.
  `observeInput` schreibt, `Sender` liest; `observeInput` schließt.
- **`localDisplay`** lebt einen Chat lang.
  `observeInput` schreibt, `displayMessages` liest; `observeInput` schließt.
- **`errorChan`** lebt einen Chat lang.
  `Sender` schreibt, `displayMessages` liest; `Sender` schließt, sobald `outgoing` geschlossen ist.

Ein Chat endet in genau dieser Reihenfolge:

1. `observeInput` endet bei `:q`, Ende der Eingabe oder `Ctrl+C` und schließt `outgoing` und `localDisplay`.
   Sofort danach wird der Partner in `Config` auf `nil` gesetzt; ab jetzt lehnt der Receiver Nachrichten mit `409` ab.
2. Der `Sender` verschickt, was noch aussteht, und schließt dann `errorChan`.
3. `displayMessages` endet, sobald `localDisplay` und `errorChan` geschlossen sind.

Schritte 2 und 3 laufen in eigenen Goroutinen und können noch kurz weiterlaufen,
während das Programm schon zur Partnerwahl zurückgekehrt ist.

Zwischen zwei Chats liest niemand aus `incoming`.
Damit der Receiver dann nicht hängen bleibt, ist `incoming` gepuffert, und der Receiver schreibt nach Regel 3:
Ist der Puffer voll, antwortet er mit `503`.
Bleibt vom Ende eines Chats eine Nachricht im Puffer liegen, verwirft die Anzeige des nächsten Chats sie,
sofern sie von einem anderen Absender stammt.

<!-- time estimate: 15 min -->


### Empfänger-Server (Receiver)

[ER] Verwenden Sie die Methode
[`http.Server.Serve()`](https://pkg.go.dev/net/http#Server.Serve)
und implementieren Sie in einem neuen Paket `receiver` die Funktion
`Receiver(ctx context.Context, cfg *config.Config, messages chan<- types.Message)`, die Folgendes tut:

- startet mit dem in `Config` hinterlegten `net.Listener` einen Server;
- registriert den Endpunkt `"POST /{username}"` und beantwortet Anfragen wie im Protokoll festgelegt.
  Den Namen aus dem Pfad liefert
  [`r.PathValue("username")`](https://pkg.go.dev/net/http#Request.PathValue);
  verglichen wird er bei jeder Anfrage neu mit `cfg.Username()`, genauso wie der Absender mit `cfg.Peer()`;
- schreibt angenommene Nachrichten nach Regel 3 auf den Kanal `messages`:
  mit `select` und `default`, und im `default`-Fall antwortet er mit `503`;
- fährt den Server über `server.Shutdown(...)` sauber herunter, sobald `ctx` abgebrochen wird;
- schließt `messages` **nicht** (Regel 2).

[HINT::Wie starte ich den Server und warte gleichzeitig auf Shutdown?]
`http.Server.Serve` blockiert, also muss `Shutdown` aus einer anderen Goroutine aufgerufen werden.
Eine mögliche Lösung:

```go
go func() {
    if err := server.Serve(cfg.Listener()); err != nil && !errors.Is(err, http.ErrServerClosed) {
        fmt.Println(err)
    }
}()

<-ctx.Done()
... // shutdown
```

`ctx` ist an dieser Stelle schon abgebrochen.
Übergeben Sie ihn an `Shutdown`, gibt `Shutdown` sofort auf, statt laufende Anfragen abzuwarten.
Nehmen Sie stattdessen einen frischen Kontext mit Frist:
`context.WithTimeout(context.Background(), time.Second)`.
[ENDHINT]

Testen Sie den Receiver, bevor der Rest des Peers fertig ist.
Ersetzen Sie dazu in `main` vorübergehend den Aufruf von `testScenario` durch Testcode, der

- mit `cfg.SetUsername("alice")` und `cfg.SetPeer(&types.Peer{Username: "bob"})` einen Benutzer und
  einen Partner einträgt (ohne Lookup-Server);
- einen Kanal anlegt und den Receiver mit `go` startet;
- in einer Schleife die Nachrichten aus dem Kanal ausgibt.

Dieser Testcode wird später durch die Zustandsmaschine ersetzt.
Schicken Sie dem Receiver dann mit `curl` Anfragen, zum Beispiel:

```bash
curl -i -X POST -d '{"sender":"bob", "receiver":"alice", "content":"hi there"}' http://localhost:51373/alice
```

Passen Sie den Port an Ihren Listener an (diesen können Sie beim Start eines Peers mit `cfg.Port()` ausgeben lassen).

Prüfen Sie die Statuscodes aus dem Protokoll:
Was antwortet der Receiver, wenn Sie den Pfad `/carol` verwenden?
Wenn `carol` als Absender schreibt?
Wenn die Nachricht keine gültige `types.Message` ist?

<!-- time estimate: 20 min -->


### Sender

[ER] Implementieren Sie eine Methode `(p Peer) FullAddress() string`, die aus `Peer.Address` und `Peer.Username`
die vollständige URL `http://address/username` erzeugt (beispielsweise `http://127.0.0.1:51043/alice`).

<!-- time estimate: 5 min -->

[ER] Implementieren Sie in einem neuen Paket `sender` die Funktion
`Sender(client *http.Client, url string, messages <-chan types.Message, errorChan chan<- error)`, welche:

- Nachrichten vom Kanal `messages` mit `range` liest, bis dieser geschlossen wird;
- jede Nachricht mit `httpjson.PostJSON` aus [PARTREF::go-chat-peer-registration] an `url` schickt;
- jeden Fehler auf `errorChan` schickt, statt ihn selbst auszugeben;
- `errorChan` schließt, sobald `messages` geschlossen ist (Regel 1).

<!-- time estimate: 10 min -->


### Chat: Eingabe und Anzeige

In diesem Abschnitt bauen Sie die beiden Funktionen, aus denen ein Chat besteht.
Zusammengesetzt werden sie weiter unten in `doChat`.

Wir wollen, dass die Eingabezeile immer ganz unten steht und neue Nachrichten direkt darüber erscheinen.
Dazu nutzen wir folgenden ANSI-Escape-Trick:

```go
func insertAboveInput(text, prompt string, senderIsSelf bool) {
    if senderIsSelf {
        fmt.Print("\033[1A") // eine Zeile hoch, zur gerade getippten Zeile
    }
    fmt.Printf("\r\033[K%v%v", text, prompt)
}
```

[FOLDOUT::Was bedeuten diese Zeichen, und warum zwei Fälle?]
`\033[1A` — bewegt den Textcursor eine Zeile nach oben.

`\r` — setzt den Textcursor an den Zeilenanfang.

`\033[K` — löscht die Zeile vom Textcursor bis zum Zeilenende.

Eigene und fremde Nachrichten brauchen unterschiedliche Behandlung:

- **Eigene Nachricht:** Was Sie getippt haben, steht schon auf dem Bildschirm, weil das Terminal Ihre
  Eingabe anzeigt, und nach `Enter` steht der Cursor in einer neuen, leeren Zeile.
  Die Funktion springt eine Zeile hoch, überschreibt die getippte Zeile mit der formatierten Nachricht
  und gibt darunter einen neuen Prompt aus.
  Ohne das Überschreiben würde die Nachricht doppelt da stehen.
- **Fremde Nachricht:** Der Cursor steht in der Eingabezeile hinter dem Prompt.
  Die Funktion überschreibt diese Zeile mit der Nachricht und gibt darunter einen neuen Prompt aus.

`text` muss in beiden Fällen mit `\n` enden, damit der Prompt in der Zeile darunter steht.

**Wichtig:** Den neuen Prompt nach einer Nachricht gibt **nur** `insertAboveInput` aus.
Würde zusätzlich `observeInput` ihn ausgeben, liefen zwei Goroutinen unkoordiniert durch dieselbe Zeile,
und je nach Timing würde der Prompt verschoben im Terminal stehen.

Sie dürfen die Funktion beliebig verbessern; sie dient nur als Ausgangspunkt.
(Beispielsweise verschwindet halb getippter Text vom Bildschirm, wenn genau dann eine fremde Nachricht eintrifft;
mit `Enter` wird er trotzdem verschickt.)

[In diesem Artikel von Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)
können Sie nachlesen, was die ANSI Escape Codes überhaupt sind;
falls Sie wissen möchten, welche anderen Codes es gibt, wäre die
[Seite "ANSI Escape Codes" auf GitHub Gist](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)
eine gute Quelle.
[ENDFOLDOUT]

[ER] Implementieren Sie die Funktion
`observeInput(ctx context.Context, self, partner, prompt string, outgoing, localDisplay chan<- types.Message)`,
welche:

- zu Beginn einmal den Prompt ausgibt;
- Zeilen mit `input.ReadLine(ctx)` aus [PARTREF::go-chat-peer-registration] liest;
- bei `:q`, Ende der Eingabe oder Abbruch von `ctx` endet;
- bei einer leeren Zeile nur den Prompt erneut ausgibt;
- jede andere Zeile in eine `Message` von `self` an `partner` verpackt (`CreatedAt` ist `time.Now()`)
  und sie erst auf `outgoing` und dann auf `localDisplay` schickt;
- beim Beenden `outgoing` und `localDisplay` schließt, weil sie deren einziger Schreiber ist (Regel 1).

[FOLDOUT::Warum zwei Kanäle für dieselbe Nachricht?]
Ein Kanal hat pro Nachricht nur einen Empfänger.
Jede eingegebene Nachricht muss aber **zwei** Ziele erreichen:
den `Sender` (damit sie verschickt wird) und die Anzeige (damit man die eigene Nachricht sieht).
Deshalb schreibt `observeInput` sie einfach nacheinander in zwei Kanäle.
[ENDFOLDOUT]

<!-- time estimate: 15 min -->

[ER] Implementieren Sie die Funktion
`displayMessages(self, partner, prompt string, incoming, own <-chan types.Message, errorChan <-chan error)`,
welche:

- mit `select` gleichzeitig auf alle drei Kanäle wartet;
- eigene Nachrichten aus `own` und Nachrichten des Partners aus `incoming` unterschiedlich formatiert, zum Beispiel
  `[Me (alice) to bob at 15:04:03]: ...` (ausgehend) und `[bob to Me (alice) at 15:04:05]: ...` (eingehend);
- Fehler aus `errorChan` als `error: ...` anzeigt;
- alles mit `insertAboveInput` ausgibt;
- Nachrichten aus `incoming` von allen anderen Absendern als `partner` verwirft
  (das sind Reste aus einem früheren Chat);
- endet, sobald `own` und `errorChan` beide geschlossen sind.
  `incoming` wird nie geschlossen und spielt für das Ende keine Rolle.

[HINT::Wie warte ich darauf, dass zwei Kanäle geschlossen sind?]
Ein Empfang von einem geschlossenen Kanal gelingt sofort.
Ist einer der beiden Kanäle schon geschlossen, würde `select` deshalb immer wieder diesen Fall wählen.
Setzen Sie die Variable des geschlossenen Kanals auf `nil`:
Ein Empfang von einem `nil`-Kanal blockiert für immer, und `select` beachtet diesen Fall nicht mehr.
Die Schleife läuft dann, solange einer der beiden Kanäle noch nicht `nil` ist:

```go
for own != nil || errorChan != nil {
    select {
    case msg, ok := <-own:
        if !ok {
            own = nil
            continue
        }
        ...
    ...
    }
}
```
[ENDHINT]

<!-- time estimate: 20 min -->


### Der Ablauf als Zustandsmaschine

Bisher war Ihr Programmablauf linear.
Nun wollen wir zwischen drei Stufen wechseln — `login`, `choosePartner` und `chat` — und jederzeit mit `:q` eine Stufe
zurückspringen sowie mit `Ctrl+C` das Programm beenden.
Dazu bekommt jede Stufe eine eigene Funktion, die die Stufe ausführt und die nächste Stufe zurückgibt.

[ER] Definieren Sie einen Aufzählungstyp `stage int` mit den Werten `login`, `choosePartner`, `chat` und `exit`.

<!-- time estimate: 5 min -->

[ER] Implementieren Sie eine Funktion `doLogin(ctx context.Context, cfg *config.Config) stage`, welche
`registration.Login` aufruft.
Bei Erfolg speichert sie den Benutzernamen in `Config` und gibt `choosePartner` zurück, sonst `exit`.

<!-- time estimate: 5 min -->

[ER] Implementieren Sie eine Funktion `doChoosePartner(ctx context.Context, cfg *config.Config) stage`,
welche `setup.GetPeer` aufruft und folgende Anforderungen erfüllt:

- Wurde `ctx` abgebrochen, gibt sie `exit` zurück;
- bei `:q` oder Ende der Eingabe meldet sie den Benutzer ab, leert den Benutzernamen in `Config`
  und gibt `login` zurück;
- bei Erfolg speichert sie den Partner in `Config` und gibt `chat` zurück.

[HINT::Wie unterscheide ich `:q` von `Ctrl+C`?]
`GetPeer` gibt in beiden Fällen einen Fehler zurück.
`ctx.Err()` ist aber nur dann nicht `nil`, wenn der Kontext abgebrochen wurde, also bei `Ctrl+C`.
[ENDHINT]

<!-- time estimate: 10 min -->

[ER] Implementieren Sie die Funktion
`doChat(ctx context.Context, cfg *config.Config, incoming <-chan types.Message) stage`, welche:

- den Benutzernamen und den Partner einmal aus `Config` liest;
- die Kanäle `outgoing`, `localDisplay` und `errorChan` anlegt und den Prompt `"[Me to <partner>]: "` baut;
- den `Sender` (mit `partner.FullAddress()` als URL) und `displayMessages` als Goroutinen startet;
- `observeInput` direkt aufruft (ohne `go`). So wartet `doChat`, bis der Chat endet;
- danach den Partner in `Config` auf `nil` setzt;
- `exit` zurückgibt, wenn `ctx` abgebrochen wurde, sonst `choosePartner`.

<!-- time estimate: 15 min -->

[ER] Bauen Sie die `main`-Funktion so auf (sie ersetzt den Aufruf von `testScenario` aus
[PARTREF::go-chat-peer-registration] und Ihren Testcode für den Receiver):

1. Erzeugen Sie wie in [PARTREF::go-chat-peer-registration] einen Kontext, der bei `Ctrl+C` abbricht,
   und eine `Config`.
2. Legen Sie einen gepufferten Kanal `incoming` an (beispielsweise mit Kapazität 10) und starten Sie den `Receiver`
   nebenläufig, und zwar **einmal** für die gesamte Laufzeit.
3. Bauen Sie eine Schleife, die bei `login` beginnt und je nach Stufe die passende Funktion aufruft,
   bis die Stufe `exit` ist:

```go
for next := login; next != exit; {
    switch next {
    case login:
        next = doLogin(ctx, cfg)
    ...
    }
}
```

4. Melden Sie den Benutzer nach der Schleife ab, falls ein Benutzername noch in `Config` steht.

<!-- time estimate: 10 min -->


### Testen

Starten Sie den Lookup-Server in einem eigenen Terminal.
Für den Test brauchen Sie zwei weitere Terminals: eines für Alice und eines für Bob.
Das Kommandoprotokoll besteht nur aus den Abschnitten dieser beiden Terminals;
das Terminal vom Lookup-Server gehört nicht hinein.

[EC] Terminal Alice: `go run . lookup=localhost:8083`

[EC] Terminal Bob: `go run . lookup=localhost:8083`

Gehen Sie dann in genau dieser Reihenfolge vor:

1. Melden Sie sich in Alices Terminal als `alice` an, in Bobs Terminal als `bob`.
2. Wählen Sie in Alices Terminal `bob` als Partner, in Bobs Terminal `alice`.
3. Alice schreibt Bob zwei Nachrichten, Bob antwortet einmal.
4. Bob verlässt den Chat mit `:q`.
5. Alice schreibt Bob noch eine Nachricht.
   Sie muss mit `409` abgelehnt werden, weil Bob in der Partnerwahl ist.
6. Bob sucht nach `carol` (die es nicht gibt), dann wieder nach `alice`, und schreibt ihr eine Nachricht.
7. Alice antwortet.
   Beenden Sie danach Alices Peer mit `Ctrl+C`.
8. Bob schreibt Alice noch eine Nachricht (das muss scheitern), verlässt den Chat mit `:q` und sucht erneut nach
   `alice`.
9. Bob verlässt die Anwendung mit `:q` (zweimal: Partnerwahl, dann Anmeldung).

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
[PROT::ALT:go-chat-peer-messaging.prot]

[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::peer].

[ENDINSTRUCTOR]