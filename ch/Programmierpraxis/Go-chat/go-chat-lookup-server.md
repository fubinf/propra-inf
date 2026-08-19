title: "Go HTTP Chat: Lookup-Server"
stage: alpha
timevalue: 1.25
difficulty: 3
assumes: go-http-server, go-json
---

[SECTION::goal::experience,product]
Ich habe einen Lookup-Server implementiert, bei dem sich Benutzer des Chats ein- und ausloggen können.
[ENDSECTION]

[SECTION::background::default]
Der Lookup-Server behält den Überblick über alle eingeloggten Benutzer des Chats.
Will Alice mit Bob schreiben, so fragt Alice beim Lookup-Server nach, was die Adresse von Bob ist.

Ist Bob zu diesem Zeitpunkt im Chat eingeloggt, so bekommt Alice seine Adresse und kann ihn anschreiben.

In dieser Aufgabe implementieren Sie nur das Ein- und Ausloggen sowie das Nachschlagen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Funktionalität implementieren

Legen Sie ein Modul `lookup` an.
In diesem Modul werden Sie den Lookup-Server als eigenständiges Programm implementieren.

[ER] Registrieren Sie einen POST-Endpunkt `/register`, der aus dem JSON-Payload die Felder `username`
und `port` ausliest und in einer Tabelle `addresses map[string]string` als Paare (`username`
— `ip_addr:port`) speichert.
`ip_addr` kann der Server aus dem Parameter `r *http.Request` auslesen.
Beachten Sie die Unterschiede zwischen IPv4- und IPv6-Adressen und verwenden Sie bei Bedarf die Funktionen
[`net.SplitHostPort`](https://pkg.go.dev/net#SplitHostPort),
[`net.ParseIP`](https://pkg.go.dev/net#ParseIP)
und
[`net.IP.To4`](https://pkg.go.dev/net#IP.To4).

Hat alles geklappt, so ist der Statuscode `200` und der Server antwortet mit `OK`.

Ist ein solcher Name bereits vergeben, dann gibt der Server Statuscode `420` und eine
informative Fehlermeldung zurück.

(Eine Auffrischung zu Servern und JSON finden Sie in den Aufgaben [PARTREF::go-http-server] und
[PARTREF::go-json]).

<!-- time estimate: 30 min -->

[ER] Registrieren Sie einen GET-Endpunkt `/{username}`, der entweder ein JSON zurückgibt, in dessen
Feld `addr` die Adresse von `username` steht, oder den Statuscode `404` ("Not Found"), falls es
keinen solchen Benutzer gibt.

<!-- time estimate: 15 min -->

[ER] Implementieren Sie abschließend noch einen POST-Endpunkt `/unregister`.
Dieser soll aus dem JSON-Payload die Felder `username` und `port` auslesen und den entsprechenden
Eintrag aus der Tabelle entfernen, sofern ein solches Benutzername-Adresse-Paar existiert.

Bei Erfolg gibt der Server `OK` mit Statuscode `200` zurück; gibt es keinen solchen Benutzer, so ist
der Statuscode `404`.

<!-- time estimate: 20 min -->

[HINT::Wie teste ich das?]
Die Funktionsfähigkeit des Lookup-Servers können Sie mittels [PARTREF::curl] überprüfen.

Eine POST-Anfrage mit JSON-Payload:

```bash
curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/register
```

Eine GET-Anfrage:

```bash
curl -X GET http://localhost:8083/alice
```

Probieren Sie ein paar Kombinationen aus, um sicherzustellen, dass Ihr Lookup-Server tatsächlich
funktioniert.
[ENDHINT]


### Testen

Starten Sie Ihren Lookup-Server und führen Sie in einem anderen Terminal folgende Kommandos aus:

- [EC] `curl -X GET http://localhost:8083/alice`
- [EC] `curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/unregister`
- [EC] `curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/register`
- [EC] `curl -X GET http://localhost:8083/alice`
- [EC] `curl -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/unregister`
- [EC] `curl -X GET http://localhost:8083/alice`

<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

**Kommandoprotokoll**
[PROT::ALT:go-chat-lookup-server.prot]

[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::lookup].
[ENDINSTRUCTOR]
