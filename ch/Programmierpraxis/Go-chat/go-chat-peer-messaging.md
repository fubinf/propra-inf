title: "Go HTTP Chat: Peer — Nachrichtenaustausch"
stage: draft
timevalue: 2
difficulty: 3
assumes: go-goroutines, go-channels, go-http-client, go-http-server
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

Außerdem wollen wir, dass Benutzer_innen jederzeit mit `:q` eine Stufe zurückspringen können (beispielsweise vom Chat
zurück zur Partnerwahl).
Dafür bauen wir den Programmablauf selbst als kleine Zustandsmaschine.
[ENDSECTION]


[TOC]


[SECTION::instructions::detailed]

### Nachrichtentyp

[ER] Definieren Sie im Paket `types` einen Typ `Message` mit den Feldern `Sender`, `Receiver`, `Content`
(vom Typ `string`) und `CreatedAt` (`time.Time`).
Fügen Sie den Feldern entsprechende JSON-Tags hinzu.


### Empfänger-Server (Receiver)

Jeder Peer verfügt über einen HTTP-Server, an dem er eingehende Nachrichten entgegennimmt.
Einen Teil davon haben Sie bereits — die in [PARTREF::go-chat-peer-registration] implementierte Funktion
`MustGetFreeListener` gibt einen `net.Listener` zurück, den Sie für den Server verwenden können.

[ER] Verwenden Sie die Methode
[`http.Server.Serve()`](https://pkg.go.dev/net/http#Server.Serve)
und implementieren Sie in einem neuen Paket `receiver` die Funktion
`Receiver(ctx context.Context, cfg *config.Config, messages chan<- types.Message)`:

- mit dem in `Config` vorhandenen `net.Listener` einen Server startet;
- einen Endpunkt `"/"+config.Username()` registriert, der eingehende `POST`-Requests als `types.Message` dekodiert
  und auf den Channel `messages` schreibt.
- Fährt den Server mittels
  [`server.Shutdown(ctx)`](https://pkg.go.dev/net/http#Server.Shutdown)
  sauber herunter, sobald `ctx` abgebrochen wird.

Sie können den Receiver nun testen, indem Sie diese Funktion in `main` aufrufen und eine HTTP-Anfrage mit
`curl -i -X POST -d '{"sender":"bob", "content": "hi there"}' http://localhost:51373/alice;` senden —
die Portnummer und den Pfad müssen Sie so anpassen, wie Ihr Empfänger-Server es erwartet.

[HINT::Wie starte ich den Server und warte gleichzeitig auf Shutdown?]
`http.Server.Serve` blockiert, `Shutdown` muss aber aus einer anderen Goroutine aufgerufen werden.
Eine mögliche Lösung:

```go
go func() {
    if err := server.Serve(cfg.Listener()); err != nil && !errors.Is(err, http.ErrServerClosed) {
        fmt.Println(err)
    }
}()

<-ctx.Done()
...
// shutdown
```
[ENDHINT]


### Sender

[ER] Implementieren Sie eine Methode `(p Peer) FullAddress() string`, die aus `Peer.Address` und `Peer.Username`
eine vollständige URL der Form `http://address/username` zusammenstellt (beispielsweise `http://127.0.0.1:51043/alice`).

<!-- time estimate: 5 min -->

[ER] Implementieren Sie in einem neuen Paket `sender` die Funktion
`Sender(ctx context.Context, cfg *config.Config, messages <-chan types.Message)`, welche:

- Nachrichten vom Channel `messages` liest und jede per `POST` an `cfg.Peer().FullAddress()` schickt;
- Schlägt das Verschicken fehl, wird der Fehler geloggt (beispielsweise mit `fmt.Println()`), das Programm läuft
  aber weiter;
- sich beendet, sobald `ctx` abgebrochen wird.

<!-- time estimate: 20 min -->


### Der Ablauf als Zustandsmaschine

Bisher war Ihr Programmablauf linear.
Jetzt wollen wir zwischen drei Stufen wechseln können — `login`, `choosePartner` und `chat` — und dabei jederzeit mit
`:q` eine Stufe zurückspringen (und aus jeder Stufe mit `Ctrl+C` ganz aussteigen).

[ER] Definieren Sie einen Aufzählungstyp `stage int` mit den Aufzählungswerten `login`, `choosePartner`,
`chat` und `exit`.

<!-- time estimate: 5 min -->

[ER] Definieren Sie eine Funktion
`act(ctx context.Context, cfg *config.Config, currentStage stage, setNewStage func(stage))`, welche je nach
`currentStage` in einem `switch`-Block entscheidet, was passieren soll:

- `login`
   - einloggen;
   - beim Erfolg den Benutzernamen in der `Config` speichern und weiter zu `choosePartner` gehen;
   - beim Fehlschlagen nochmal versuchen, bis der Benutzer die Anwendung verlässt oder das Anmelden funktioniert;
- `choosePartner`
   - einen Peer aussuchen;
   - beim Erfolg den Peer in der `Config` speichern und weiter zu `chat` gehen;
   - beim Fehlschlagen den Benutzer abmelden und zurück zur Stufe `login` gehen;
- `chat`
   - zwei Kanäle für die eingehenden und ausgehenden Nachrichten anlegen (`incoming, outgoing chan types.Message`);
   - einen abbrechbaren Kontext erzeugen und mit diesem nebenläufig Sender und Receiver starten.
     Die Abbruchsfunktion verwenden Sie später im `onGoBack`-Callback-Parameter von der Funktion `processChat`;
   - eine Funktion `processChat()` aufrufen, die Sie im nächsten Schritt implementieren.

<!-- time estimate: 20 min -->


[ER] Legen Sie in `main` einen Kanal `stageChan chan stage` und eine zentrale Schleife an, die unter einem `select`
auf Kanäle `stageChan` und `ctx.Done()` hört.

- Beim Abbrechen soll der Benutzer abgemeldet werden und das Programm endet;
- Beim Empfangen von `exit` aus `stagesChan` wird das Programm beendet;
  ansonsten wird nebenläufig die Funktion `act` aufgerufen.

<!-- time estimate: 10 min -->


### Chat-Stufe: Eingabe und Anzeige

Wie in den meisten Chat-Programmen soll die Eingabezeile immer ganz unten stehen, neue Nachrichten
erscheinen direkt darüber.
Dafür nutzen wir einen ANSI-Escape-Trick:

```go
func insertAboveInput(text string, promptLength int, senderIsSelf bool) {
    if senderIsSelf {
        fmt.Printf("\033[1A\r%v\033[%vC", text, promptLength)
    } else {
        fmt.Printf("\033[1L\r%v\033[%vC", text, promptLength)
    }
}
```

[FOLDOUT::Was bedeuten diese Zeichen?]
Jede Zeichenkette ist nur eine Folge von Ansi-Escape-Codes.

`\033[1A` bewegt den Textcursor eine Zeile nach oben, `\r` bewegt ihn zum Anfang der Zeile, `\033[%vC` bewegt ihn um
`%v` Stellen nach rechts.

`\033[1L` fügt eine leere Zeile oberhalb der aktuellen Zeile ein (sie wird nach unten geschoben), `\r` bewegt den
Textcursor zum Anfang der Zeile, `\033[%vC` bewegt ihn um `%v` Stellen nach rechts.

Sie dürfen die oben vorgestellte Funktion beliebig modifizieren; sie dient nur als ein Ausgangspunkt.
[ENDFOLDOUT]

[ER] Implementieren Sie die Funktion
`observeInput(ctx context.Context, cfg *config.Config, prompt string, outgoing chan<- types.Message, onGoBack func())`,
die Folgendes tut:

- liest Zeilen von `os.Stdin` in einer separaten Goroutine ein;
- Verpackt jede nichtleere Zeile in eine `Message` und schickt sie auf `outgoing`;
- Zeigt vor jeder Eingabe den Prompt `"[Me to <peerName>]: "` an;
- Beendet bei `:q` die Eingabeschleife und ruft `onGoBack()` auf (zurück zur Partnerwahl).

<!-- time estimate: 15 min -->

[ER] Implementieren Sie die Funktion
`displayMessages(cfg *config.Config, prompt string, incoming <-chan types.Message)`, welche:

- Liest Nachrichten vom Channel `incoming` und gibt sie über `insertAboveInput` aus;
- Nachrichten von einem selbst werden anders formatiert als Nachrichten vom Gesprächspartner
  (beispielsweise `"[Me (alice) to bob at 15:04:03]: ..."` vs. `"[bob to Me (alice) at 15:04:05]: ..."`).

<!-- time estimate: 10 min -->

[ER] Implementieren Sie die Funktion
`processChat` mit Parametern `ctx context.Context`, `cfg *config.Config`, `incoming <-chan types.Message`,
`outgoing chan<- types.Message` und `onGoBack func()`, die folgendes tut:

- `observeInput` in einer Goroutine startet; jede eingegebene Nachricht muss **zwei** Ziele erreichen:
  den `Sender` (damit sie tatsächlich verschickt wird) und die lokale Anzeige (damit man seine eigene Nachricht auch
  sieht);
- `displayMessages` für die eigenen (soeben gesendeten) und für die eingehenden Nachrichten jeweils in einer eigenen
  Goroutine startet.

[FOLDOUT::Ein Wert, zwei Abnehmer]
Ein Kanal hat pro Nachricht immer nur einen Empfänger.
Wollen Sie dieselbe Nachricht sowohl verschicken als auch lokal anzeigen, brauchen Sie entweder zwei separate
Sende-Operationen auf zwei verschiedene Kanäle, oder eine kleine Verteiler-Goroutine, die von einem Eingabekanal
liest und auf zwei Ausgabekanäle weiterreicht.
[ENDFOLDOUT]

<!-- time estimate: 10 min -->


### Alles starten

Erweitern Sie `main` (manche Schritte haben Sie bereits implementiert — dies ist nur eine Checkliste):

1. Erzeugen Sie einen Kontext, der beim Empfangen von `syscall.SIGTERM` abbricht;
2. Erzeugen Sie eine `Config`, verwenden Sie dabei die Funktionen `setup.MustGetFreeListener` und
   `setup.MustGetLookupUrl`;
3. Stoßen Sie die Ausführung an, indem Sie in einer separaten Goroutine `login` auf den Kanal `stagesChan` senden;
4. In einer Schleife unter `select` auf `ctx.Done()` und `stagesChan` hören und die nächste Stufe an die Funktion
   `act()` weitergeben.

Nun ist es Ihnen überlassen, die Funktionsweise der Anwendung zu überprüfen und nachzubessern.

<!-- time estimate: 5 min -->


### Testen

Starten Sie den Lookup-Server und zwei Peer-Instanzen (`alice`, `bob`).

1. Beide melden sich an, Alice sucht nach Bob.
2. Alice schreibt Bob zwei Nachrichten, Bob antwortet einmal.
3. Bob verlässt den Chat mit `:q`, sucht stattdessen nach einer nicht existierenden `carol`, dann
   erneut nach `alice` und schreibt weiter.
4. Alice beendet ihr Programm mit `Ctrl+C`, während Bob noch eine Nachricht schickt.

- [EC] (Terminal-Trace Alice)
- [EC] (Terminal-Trace Bob)
- [EC] (Terminal-Trace Lookup-Server)

<!-- time estimate: 10 min -->
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
