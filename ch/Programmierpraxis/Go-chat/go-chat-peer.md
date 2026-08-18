title: "HTTP Chat: Peer"
stage: draft
timevalue: 2
difficulty: 3
assumes: go-http-client, go-http-server, go-json
requires: go-chat-lookup-server
---

[SECTION::goal::experience,product]
TODO
[ENDSECTION]

[SECTION::background::default]
TODO
[ENDSECTION]

[TOC]

[SECTION::instructions::loose]

In dieser Aufgabe gehen wir das Peer-Programm genauer an.

### Architektur

Wir unterteilen den Programmablauf in drei Stufen:

1. `Login` — wo der Benutzername eingegeben wird;
2. `Choose Partner` — wo der Name des Gesprächspartners eingegeben wird;
3. `Chat` — wo der Nachrichtenaustausch stattfindet.
4. (`Exit` — wo der Benutzer die Anwendung beenden will.)

Dabei darf der Benutzer jederzeit mittels `:q` (oder einer anderen Nachricht Ihrer Wahl) zur einen
niedrigere Stufe springen, wie beispielsweise von `Chat` zu `Choose Partner`.

[ER] Legen Sie ein


### Initialisierung

Jeder Peer braucht die IP-Adresse des Lookup-Servers — diese darf beim Starten als
Kommandozeilenargument übergeben werden.

[ER] Implementieren Sie im Peer-Programm eine Funktion `MustGetLookupUrl`, welches beim Start die
Kommandozeilenargumente ausliest und nach einem Argument der Form `lookup=192.168.178.76:8083` sucht.
Schauen Sie in dem
[Artikel "Go by Example: Command-Line Arguments"](https://gobyexample.com/command-line-arguments)
nach, wie das abläuft.
Danach gibt die Funktion eine URL wie `http://192.168.178.76:8083` zurück.

[ER] Implementieren Sie eine Funktion `MustLogin` nach folgender Spezifikation:

- Als Erstes wird eine Begrüßung ausgegeben, wie beispielsweise `Welcome! What's your name?: `
- Sobald der Benutzer etwas eingegeben hat (und `Enter` gedrückt) soll die Funktion den Benutzer
beim Lookup-Server registrieren (mit dem Port `8080`);
- Ist die Registrierung erfolgreich, soll eine entsprechende Meldung ausgegeben werden; anderenfalls
wird eine informative Fehlermeldung ausgegeben und die Funktion startet von vorne wieder;
- Die Funktion soll einen `ctx context.Context` als Parameter bekommen und den Login-Vorgang sofort
abbrechen, falls der Kontext abgebrochen wurde.
(Lösungsvorschlag: Ein Kanal `input` für Benutzereingaben und ein `select` über `ctx.Done()` und
`input`.)

[ER] Implementieren Sie noch eine Funktion `Logout`.
Diese soll den Benutzer beim Lookup-Server abmelden (über den Endpunkt `/unregister`).

[ER] Verwenden Sie das folgende Konstrukt, um das Schließen von `ctx.Done()` auszulösen, sobald die
Anwendung mittels `Ctrl+C` beendet wird:

```go
ctx, cancel := signal.NotifyContext(ctx, os.Interrupt)
```

(der Kanal `ctx.Done()` wird geschlossen, sobald es ein Signal `os.Interrupt` kommt.)

[ER] Nachdem die Anmeldung erfolgreich abgeschlossen wurde, soll der Benutzer einen Gesprächspartner
wählen können.
Implementieren Sie eine Funktion `GetConversationPartner`, welche:

- einen Benutzernamen von der Kommandozeile einliest;
- beim Lookup-Server die Adresse des anderen Benutzers nachschlägt (Endpunkt `GET /{username}`);
- eine informative Fehlermeldung ausgibt, falls etwas schiefgeht;
- eine Meldung Ihrer Wahl ausgibt, falls ein solcher Benutzer existiert.

[ER] Aktuell sieht der Flow folgendermaßen aus:

```
Login -> Gesprächspartner auswählen -> Chat
```

Wir wollen aber dem Benutzer Ausloggen ermöglichen.
Dies sollte durch Eingabe von `:q` im Schritt "Gesprächspartner auswählen" stattfinden.


#### Benutzereingaben bearbeiten

Wie in der Mehrheit von Chat-Anwendungen soll Benutzereingabe immer ganz unten bleiben.
Neue Nachrichten erscheinen dann direkt darüber.

Um die Ausgaben auf der Kommandozeile zu manipulieren, gibt es die sogenannten
[ANSI Escape Codes](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797).
Folgende Funktion fügt den `text` oberhalb der letzten Zeile im Terminal hinzu:

```go
func insertAboveInput(text string, promptLength int) {
	fmt.Printf("\u001B[1A\r%v\r\033[%vC", text, promptLength)
}
```

(`promptLength` ist die Länge vom Prompt — wir benutzen `[Me]: ` als Prompt, also ist die Länge 6.)

[ER] Überlegen Sie sich woraus eine `Message` besteht.

[ER] Implementieren Sie eine Funktion `observeInput(outgoing chan<- Message)`, die Terminal-Eingaben
in Strukturen von Typ `Message` umwickelt und in den Kanal `outgoing` sendet.
Diese Funktion ist außerdem für den Prompt `[Me]: ` zuständig und läuft in einer eigenen Goroutine.

[ER] Implementieren Sie eine weitere Funktion `display(messages <-chan Message)`, die Nachrichten
aus dem Kanal `messages` empfängt und auf der Kommandozeile mithilfe von `insertAboveInput` ausgibt.
Stammt eine Nachricht von dem Benutzer selbst, so wird anstatt vom Benutzernamen `Me` ausgegeben.
Diese Funktion läuft auch in einer separaten Goroutine.

So sollen die Zwischenzustände aussehen:

__Warten auf Benutzereingaben__
```terminaloutput
[Me]:
```

__Benutzer gibt die Nachricht ein__
```terminaloutput
[Me]: Hi ther
```

__Benutzer hat `Enter` bzw `Eingabe` gedrückt__
```terminaloutput
[Me at 15:04] Hi there!
[Me]:
```


#### Nachrichten senden

#### Nachrichten empfangen


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

In erster Linie orientieren wir uns auf korrekte Funktionsweise.

Den Code lesen, insbesondere Fehlerbehandlung.
Ein `if err != nil { panic(err) / return err }` reicht oft aus, aber spezifischere Fehlermeldungen
sind an manchen Stellen sehr vorteilhaft.
Wir wollen das Bedenken sehen, "was tut mein Code, wenn XYZ schiefgeht?"
[ENDINSTRUCTOR]
