title: "Go HTTP Chat: Peer — Nachrichtenaustausch"
stage: draft
timevalue: 2.25
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


### Empfänger-Server (Receiver)

Jeder Peer verfügt über einen HTTP-Server, an dem er eingehende Nachrichten entgegennimmt.
Ein Teil davon ist bereits vorhanden — die in [PARTREF::go-chat-peer-registration] implementierte Funktion
`MustGetFreeListener` liefert einen `net.Listener`, den Sie für den Server nutzen können.

[ER] Verwenden Sie die Methode
[`http.Server.Serve()`](https://pkg.go.dev/net/http#Server.Serve)
und implementieren Sie in einem neuen Paket `receiver` die Funktion
`Receiver(ctx context.Context, cfg *config.Config, messages chan<- types.Message)`, die Folgendes tut:

- startet mit dem in `Config` hinterlegten `net.Listener` einen Server;
- registriert den Endpunkt `"/"+config.Username()` und dekodiert eingehende `POST`-Requests als `types.Message`,
  die er auf den Channel `messages` schreibt;
- fährt den Server über `server.Shutdown(ctx)` sauber herunter, sobald `ctx` abgebrochen wird.

Testen Sie den Receiver, indem Sie die Funktion in `main` aufrufen und eine HTTP-Anfrage mit

```bash
curl -i -X POST -d '{"sender":"bob", "receiver":"alice", "content":"hi there"}' http://localhost:51373/alice
```

senden — passen Sie Port, Pfad und `receiver` an die Konfiguration Ihres Empfänger-Servers an.

[HINT::Wie starte ich den Server und warte gleichzeitig auf Shutdown?]
`http.Server.Serve` blockiert, `Shutdown` muss aus einer anderen Goroutine aufgerufen werden.
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
[ENDHINT]

<!-- time estimate: 15 min -->


### Sender

[ER] Implementieren Sie eine Methode `(p Peer) FullAddress() string`, die aus `Peer.Address` und `Peer.Username`
die vollständige URL `http://address/username` erzeugt (beispielsweise `http://127.0.0.1:51043/alice`).

<!-- time estimate: 5 min -->

[ER] Implementieren Sie in einem neuen Paket `sender` die Funktion
`Sender(ctx context.Context, cfg *config.Config, messages <-chan types.Message)`, welche:

- Nachrichten vom Channel `messages` liest;
- jede Nachricht per `POST` an `cfg.Peer().FullAddress()` sendet;
- Fehler protokolliert (beispielsweise mit `fmt.Println()`), das Programm aber weiterlaufen lässt;
- sich beendet, sobald `ctx` abgebrochen wird.

<!-- time estimate: 20 min -->


### Der Ablauf als Zustandsmaschine

Bisher war Ihr Programmablauf linear.
Nun wollen wir zwischen drei Stufen wechseln — `login`, `choosePartner` und `chat` — und jederzeit mit `:q` eine Stufe
zurückspringen sowie mit `Ctrl+C` das Programm beenden.

[ER] Definieren Sie einen Aufzählungstyp `stage int` mit den Werten `login`, `choosePartner`, `chat` und `exit`.

<!-- time estimate: 5 min -->

[ER] Definieren Sie die Funktion
`act(ctx context.Context, cfg *config.Config, currentStage stage, setNewStage func(stage))`
und lassen Sie sie in einem `switch`-Block je nach `currentStage` folgendes ausführen:

- **login**
    - einloggen,
    - bei Erfolg den Benutzernamen in `Config` speichern und zu `choosePartner` wechseln,
    - bei Fehlschlag erneut versuchen, bis der Benutzer die Anwendung verlässt oder die Anmeldung klappt.
- **choosePartner**
    - einen Peer auswählen,
    - bei Erfolg den Peer in `Config` speichern und zu `chat` wechseln,
    - bei Fehlschlag abmelden und zurück zu `login`.
- **chat**
    - zwei Kanäle für eingehende und ausgehende Nachrichten anlegen (`incoming, outgoing chan types.Message`),
    - einen abbrechbaren Kontext erzeugen und damit nebenläufig Sender und Receiver starten (die Abbruchfunktion
      verwenden Sie später im `onGoBack`-Callback von `processChat`),
    - die Funktion `processChat()` aufrufen (siehe nächster Schritt).

<!-- time estimate: 20 min -->

[ER] Legen Sie in `main` einen Kanal `stageChan chan stage` an und bauen Sie eine zentrale Schleife, die mit
`select` auf `stageChan` und `ctx.Done()` wartet:

- Beim Abbruch wird der Benutzer abgemeldet und das Programm endet.
- Beim Empfang von `exit` aus `stageChan` beendet das Programm ebenfalls; sonst startet `act` nebenläufig.

<!-- time estimate: 10 min -->


### Chat-Stufe: Eingabe und Anzeige

Wir wollen, dass die Eingabezeile immer ganz unten steht und neue Nachrichten direkt darüber erscheinen.
Dazu nutzen wir folgenden ANSI-Escape-Trick:

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
`\033[1A` — bewegt den Textcursor eine Zeile nach oben.

`\r` — setzt den Textcursor an den Zeilenanfang.

`\033[%vC` — bewegt den Textursor `%v` Stellen nach rechts.

`\033[1L` — fügt eine leere Zeile oberhalb der aktuellen Zeile ein.

Sie dürfen die Funktion beliebig modifizieren; sie dient nur als Ausgangspunkt.

[In diesem Artikel von Wikipedia](https://en.wikipedia.org/wiki/ANSI_escape_code)
können Sie nachlesen, was die ANSI Escape Codes überhaupt sind; falls Sie wissen möchten, welche anderen Codes es gibt,
wäre die
[Seite "ANSI Escape Codes" auf GitHub Gist](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)
eine gute Quelle.
[ENDFOLDOUT]

[ER] Implementieren Sie die Funktion
`observeInput(ctx context.Context, cfg *config.Config, prompt string, outgoing chan<- types.Message, onGoBack func())`,
welche:

- Zeilen von `os.Stdin` in einer separaten Goroutine liest;
- jede nichtleere Zeile in eine `Message` verpackt und sie auf `outgoing` schickt;
- vor jeder Eingabe den Prompt `"[Me to <peerName>]: "` anzeigt;
- bei `:q` die Eingabeschleife beendet und `onGoBack()` aufruft (zurück zur Partnerwahl).

<!-- time estimate: 15 min -->

[ER] Implementieren Sie die Funktion
`displayMessages(cfg *config.Config, prompt string, incoming <-chan types.Message)`, welche:

- Nachrichten vom Channel `incoming` liest;
- sie mit `insertAboveInput` ausgibt;
- eigene Nachrichten anders formatiert als Nachrichten des Gesprächspartners, zum Beispiel
  `"[Me (alice) to bob at 15:04:03]: ..."`(ausgehend) und `"[bob to Me (alice) at 15:04:05]: ..."` (eingehend).

<!-- time estimate: 10 min -->

[ER] Implementieren Sie die Funktion `processChat` mit den Parametern
`ctx context.Context`, `cfg *config.Config`, `incoming <-chan types.Message`, `outgoing chan<- types.Message`,
`onGoBack func()`, welche:

- `observeInput` in einer Goroutine startet; jede eingegebene Nachricht muss **zwei** Ziele erreichen:
den `Sender` (damit sie verschickt wird) und die lokale Anzeige (damit man die eigene Nachricht sieht);
- `displayMessages` für eigene und eingehende Nachrichten jeweils in einer eigenen Goroutine startet.

[FOLDOUT::Ein Wert, zwei Abnehmer]
Ein Kanal hat pro Nachricht nur einen Empfänger.
Um dieselbe Nachricht sowohl zu verschicken als auch lokal anzuzeigen, benötigen Sie entweder zwei separate
Sende-Operationen auf verschiedene Kanäle oder eine kleine Verteiler-Goroutine, die von einem Eingabekanal liest
und die Nachricht auf zwei Ausgabekanäle verteilt.
[ENDFOLDOUT]

<!-- time estimate: 10 min -->


### Alles starten

Erweitern Sie `main` (einige Schritte haben Sie bereits erledigt – dies ist nur eine Checkliste):

1. Erzeugen Sie einen Kontext, der bei `syscall.SIGTERM` abbricht.
2. Erzeugen Sie eine `Config` und nutzen Sie dabei `setup.MustGetFreeListener` sowie `setup.MustGetLookupUrl`.
3. Starten Sie die Ausführung, indem Sie in einer separaten Goroutine `login` auf den Kanal `stageChan` senden.
4. Bauen Sie eine Schleife mit `select`, die auf `ctx.Done()` und `stageChan` wartet und die nächste Stufe an `act()`
   weitergibt.

Nun können Sie die Funktionsweise der Anwendung prüfen und nachbessern.

<!-- time estimate: 5 min -->


### Testen

Starten Sie den Lookup-Server und zwei Peer-Instanzen (`Alice`, `Bob`).

1. Beide melden sich an;
2. Beide geben den Namen des Gesprächspartners ein (Alice gibt "Bob" ein, Bob gibt "Alice" ein);
3. Alice schreibt Bob zwei Nachrichten, Bob antwortet einmal;
4. Bob verlässt den Chat mit `:q`, sucht nach einer nicht existierenden `carol`, dann erneut nach `alice` und schreibt
   Alice noch eine Nachricht;
5. Alice beendet ihr Programm mit `Ctrl+C`;
6. Bob versucht noch eine Nachricht an Alice zu schicken;
7. Bob verlässt den Chat mit `:q` und sucht erneut nach Alice;
8. Bob verlässt die Anwendung mit `:q` (wird mehrmals eingegeben).

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
[PROT::ALT:go-chat-peer-messaging.prot]

[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::peer].

[ENDINSTRUCTOR]