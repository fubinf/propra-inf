title: "Go HTTP Chat: Lookup-Server"
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: go-http-server, go-json, go-modules, http-Status
---

[SECTION::goal::experience,product]
Ich habe einen Lookup-Server implementiert, bei dem sich Benutzer des Chats ein- und ausloggen können.
[ENDSECTION]

[SECTION::background::default]
Der Lookup-Server behält den Überblick über alle eingeloggten Benutzer des Chats.

Jeder Peer startet einen eigenen Empfänger-Server auf einem bestimmten Port und ist damit grundsätzlich erreichbar —
nur weiß zunächst niemand, unter welcher Adresse.
Peers können sich nicht direkt finden:
Ihre IP-Adresse ändert sich je nachdem, von wo sie sich verbinden, und der Port wird bei jedem Start selbst gewählt.
Der Lookup-Server schafft hier Abhilfe, indem er unter einer festen, allen Peers bekannten Adresse erreichbar ist und
die Zuordnung von Benutzername zu IP-Adresse und Port verwaltet.

Will Alice mit Bob schreiben, so fragt Alice beim Lookup-Server nach, was die Adresse von Bob ist.
Ist Bob zu diesem Zeitpunkt im Chat eingeloggt, so bekommt Alice seine Adresse und kann ihn anschreiben.

In dieser Aufgabe implementieren Sie nur das Ein- und Ausloggen sowie das Nachschlagen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Funktionalität implementieren

Legen Sie ein Modul `lookup` an.
In diesem Modul werden Sie den Lookup-Server als eigenständiges Programm implementieren.
Der Lookup-Server soll auf Port `8083` lauschen.

[NOTICE]
Für eigene, triviale Anwendungen wie diese ist es sinnvoll, sich einen zufälligen Port aus dem Bereich `8001`—`8099`
als Standard zu wählen, statt naheliegende Ports wie `8080` oder `3000` zu verwenden.
Solche gut bekannten Ports sind auf Ihrem Rechner oft schon von anderen Tools oder Ihren eigenen Programmen aus früheren
Aufgaben belegt — ein zufälliger Port aus einem selten genutzten Bereich minimiert das Risiko solcher Konflikte.
[ENDNOTICE]

[ER] Implementieren Sie eine Struktur `AddressTable` mit den Feldern `mu sync.Mutex` und
`addressesByName map[string]string`.
Implementieren Sie außerdem die Konstruktorfunktion `New() *AddressTable` sowie folgende Methoden:

- `(t *AddressTable) Add(name, address string)`
- `(t *AddressTable) GetAddrOf(name string) (addr string, ok bool)`
- `(t *AddressTable) RemoveAddrOf(name string)`

Die Map `addressesByName` soll ausschließlich über diese Methoden zugreifbar sein.
Schützen Sie den Zugriff auf die Map mit dem Mutex `mu`.

**Verwenden Sie die Sichtbarkeitsregeln von Go:**
Implementieren Sie `AddressTable` und alle genannten Funktionen und Methoden im eigenen Paket `addresstable`.
Die Felder `mu` und `addressesByName` sollen nicht exportiert werden, sodass sie aus anderen Paketen nicht direkt
zugreifbar sind.

<!-- time estimate: 15 min -->

[ER] Registrieren Sie einen POST-Endpunkt `/register`, der aus dem JSON-Payload die Felder `username`
und `port` ausliest und in `AddressTable` speichert.
Der Parameter `name` ist der Benutzername;
Der Parameter `address` wird aus der IP-Adresse und dem Port gebildet, getrennt durch einen Doppelpunkt
(`ip_addr:port`).
`ip_addr` kann der Server dem Feld
[`RemoteAddr`](https://pkg.go.dev/net/http#Request)
des Parameters `r *http.Request` entnehmen.
Beachten Sie die Unterschiede zwischen IPv4- und IPv6-Adressen (bei IPv4-Adressen soll das Format `ip_addr:port`
verwendet werden; bei IPv6-Adressen das Format `[ip_addr]:port`) und verwenden Sie bei Bedarf die Funktionen
[`net.SplitHostPort`](https://pkg.go.dev/net#SplitHostPort),
[`net.ParseIP`](https://pkg.go.dev/net#ParseIP)
und
[`net.IP.To4`](https://pkg.go.dev/net#IP.To4).

Hat alles geklappt, so ist der Statuscode `200` und der Server antwortet mit `OK`.
Lesen Sie selbst nach in der Dokumentation von `net/http`, wie man in Go bei einem `http.ResponseWriter`
den Statuscode setzt.

Ist ein solcher Name bereits vergeben, dann gibt der Server Statuscode `409` ("Conflict") und eine informative
Fehlermeldung zurück.

(Eine Auffrischung zu Servern und JSON finden Sie in den Aufgaben [PARTREF::go-http-server] und [PARTREF::go-json]).

[FOLDOUT::Warum kommt der Port aus dem Payload und nicht aus der Anfrage?]
Man könnte auf die Idee kommen, Port und IP-Adresse beide aus `r.RemoteAddr` auszulesen — schließlich steckt dort ja
"IP:Port" drin.
Das funktioniert aber nicht:
Der Port, über den der Peer diese Registrierungsanfrage sendet, ist ein kurzlebiger, vom Betriebssystem automatisch
vergebener _ephemeral port_ (siehe
[Wikipedia: Ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port)).
Er hat nichts mit dem Port zu tun, auf dem der Peer selbst später auf eingehende Chat-Nachrichten lauscht.
Deshalb muss der Peer seinen tatsächlichen, dauerhaften Port explizit mitschicken — nur die IP-Adresse darf unverändert
aus der Anfrage übernommen werden, da sie sich zwischen Ephemeral- und dauerhaftem Port nicht unterscheidet.
[ENDFOLDOUT]

<!-- time estimate: 30 min -->

[ER] Registrieren Sie einen GET-Endpunkt `/{username}`, der entweder ein JSON zurückgibt, in dessen
Feld `addr` die Adresse von `username` steht, oder den Statuscode `404` ("Not Found"), falls es
keinen solchen Benutzer gibt.

<!-- time estimate: 15 min -->

[ER] Implementieren Sie abschließend noch einen POST-Endpunkt `/unregister`.
Dieser soll aus dem JSON-Payload die Felder `username` und `port` auslesen und den entsprechenden Eintrag aus der
Tabelle entfernen, sofern ein solches Benutzername-Adresse-Paar existiert.
Der gespeicherte Eintrag für `username` muss dabei exakt aus der IP-Adresse der aktuellen Anfrage und dem übergebenen
`port` bestehen (also derselben Berechnung wie bei `/register`).

Bei Erfolg gibt der Server `OK` mit Statuscode `200` zurück; gibt es keinen solchen Benutzer, so ist der Statuscode
`404` ("Not Found").

(So kann sich niemand mit einer fremden IP-Adresse oder einem fremden Port für einen Benutzernamen ausloggen, der ihm
gar nicht gehört — deshalb wird `port` hier überhaupt im Payload gebraucht, obwohl `/unregister` streng genommen
nur den `username` bräuchte, um den passenden Tabelleneintrag zu finden.)

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

[EC] `curl -i -X GET http://localhost:8083/alice`

[EC] `curl -i -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/unregister`

[EC] `curl -i -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/register`

[EC] `curl -i -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/register`

[EC] `curl -i -X GET http://localhost:8083/alice`

[EC] `curl -i -X POST -d '{"username":"alice","port":"8081"}' http://localhost:8083/unregister`

[EC] `curl -i -X GET http://localhost:8083/alice`

[EQ] Warum antwortet der Server mit "user not found" auf `curl -X GET http://localhost:8083/register`?

<!-- time estimate: 15 min -->

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
