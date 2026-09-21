title: "Go HTTP Chat: Lookup-Server"
stage: alpha
timevalue: 1.5
difficulty: 3
assumes: go-sync-mutex, go-http-server, go-json, go-modules, http-Status
---

[SECTION::goal::experience,product]
Ich habe einen Lookup-Server implementiert, bei dem sich Benutzer des Chats ein- und ausloggen können
und dessen nebenläufig genutzte Adresstabelle gegen gleichzeitige Zugriffe abgesichert ist.
[ENDSECTION]

[SECTION::background::default]
Der Lookup-Server behält den Überblick über alle eingeloggten Benutzer des Chats.

Jeder Peer startet einen eigenen Empfänger-Server auf einem bestimmten Port und ist damit grundsätzlich erreichbar —
nur weiß zunächst niemand, unter welcher Adresse.
Peers können sich nicht direkt finden:
Ihre IP-Adresse ändert sich je nachdem, von wo sie sich verbinden, und der Port wird bei jedem Start selbst gewählt.
Der Lookup-Server schafft hier Abhilfe, indem er unter einer festen, allen Peers bekannten Adresse erreichbar ist und
die Zuordnung von Benutzername zu IP-Adresse und Port verwaltet.

Will Alice mit Bob schreiben, so fragt Alice beim Lookup-Server nach der Adresse von Bob.
Ist Bob zu diesem Zeitpunkt im Chat eingeloggt, so bekommt Alice seine Adresse und kann ihn anschreiben.

In dieser Aufgabe implementieren Sie nur das Ein- und Ausloggen sowie das Nachschlagen.
[ENDSECTION]


[SECTION::instructions::detailed]

### Funktionalität implementieren

Legen Sie ein Modul `lookup` an.
In diesem Modul werden Sie den Lookup-Server als eigenständiges Programm implementieren.
Der Lookup-Server soll auf Port `8083` lauschen.

[NOTICE]
Für eigene, triviale Anwendungen wie diese ist es sinnvoll, sich einen zufälligen Port aus dem Bereich
`8001` bis `8099` als Standard zu wählen, statt naheliegende Ports wie `8080` oder `3000` zu verwenden.
Solche gut bekannten Ports sind auf Ihrem Rechner oft schon von anderen Tools oder Ihren eigenen Programmen
aus früheren Aufgaben belegt — ein zufälliger Port aus einem selten genutzten Bereich minimiert das Risiko
solcher Konflikte.

Aus diesem Grund legen wir in dieser Aufgabe Port `8083` fest.
[ENDNOTICE]

[ER] Implementieren Sie eine Struktur `AddressTable` mit den Feldern `mu sync.Mutex` und
`addressesByName map[string]string`.
Implementieren Sie außerdem die Konstruktorfunktion `New() *AddressTable` sowie folgende Methoden:

- `(t *AddressTable) AddIfAbsent(name, address string) (ok bool)`
    - gibt es bereits einen Benutzer mit dem Namen `name`, gibt die Methode `false` zurück;
    - gibt es keinen solchen Benutzer, speichert die Methode das Paar `name` und `address` und gibt `true` zurück.
- `(t *AddressTable) GetAddrOf(name string) (addr string, ok bool)`
    - liefert die gespeicherte Adresse des Benutzers `name`; `ok` zeigt an, ob es einen solchen Eintrag gibt.
- `(t *AddressTable) RemoveIfMatches(name, address string) (ok bool)`
    - gibt es einen Benutzer mit dem Namen `name` und der Adresse `address`, löscht die Methode den
      entsprechenden Eintrag aus `AddressTable` und gibt `true` zurück;
    - gibt es keinen Benutzer mit dem Namen `name` und der Adresse `address`, gibt die Methode `false` zurück.

Die Map `addressesByName` soll ausschließlich über diese Methoden zugreifbar sein.
Schützen Sie den Zugriff auf die Map mit dem Mutex `mu`.

Dies ist notwendig, da jede HTTP-Anfrage in einer eigenen Goroutine verarbeitet wird und die Handler dadurch
nebenläufig auf `AddressTable` zugreifen können.

**Verwenden Sie die Sichtbarkeitsregeln von Go:**
Implementieren Sie `AddressTable` und alle genannten Funktionen und Methoden im eigenen Paket `addresstable`.
Die Felder `mu` und `addressesByName` sollen nicht exportiert werden, sodass sie aus anderen Paketen nicht direkt
zugreifbar sind.

[EQ] Warum sind `AddIfAbsent` und `RemoveIfMatches` jeweils als eine einzige Methode vorgegeben, statt sie aus
`GetAddrOf` und einer separaten Schreiboperation zusammenzusetzen?
Was kann passieren, wenn sich zwei Peers gleichzeitig mit demselben Benutzernamen registrieren?

<!-- time estimate: 15 min -->

[ER] Implementieren Sie eine Struktur `NameAndPortMessage` mit den Feldern `Name string` und `Port int`.
Versehen Sie diese mit JSON-Struct-Tags: `name` für `Name` und `port` für `Port`.

[ER] Implementieren Sie für die Struktur `NameAndPortMessage` eine Methode `Validate() (err error)`,
die einen Fehler zurückgibt, wenn `Name` leer ist oder `Port` nicht im Bereich von 1 bis 65535 (jeweils einschließlich)
liegt.
Verwenden Sie für die Erzeugung der Fehler (mit einer informativen Fehlermeldung!) die Funktion
[`errors.New`](https://pkg.go.dev/errors#New).

<!-- time estimate: 10 min -->

In dieser Aufgabe implementieren Sie zwei HTTP-Handler, die fast dasselbe tun:
Beide dekodieren eine `NameAndPortMessage` aus dem JSON-Payload, validieren sie und konstruieren aus der Absenderadresse
und dem Port eine Adresse der Form `host:port`.
Der Unterschied ist nur, dass `/register` den Eintrag (Name und Adresse) speichert, während `/unregister` ihn entfernt.
Diese gemeinsame Logik sollen Sie nicht doppelt implementieren; sie gehört in eine eigenständige Funktion.

[ER] Implementieren Sie eine Funktion `extractNameAndAddress(r *http.Request) (name, addr string, err error)`.
Diese soll:

- eine `NameAndPortMessage` aus dem JSON-Payload dekodieren; schlägt das fehl, gibt die Funktion den Fehler
  `error while decoding JSON: %v` zurück, wobei `%v` durch den ursprünglichen Fehler ersetzt wird (verwenden Sie dafür
  [`fmt.Errorf`](https://pkg.go.dev/fmt#Errorf));
- die `NameAndPortMessage` validieren; schlägt das fehl, gibt die Funktion den Fehler zurück;
- aus dem Host der Absenderadresse (siehe
  [`http.Request.RemoteAddr`](https://pkg.go.dev/net/http#Request))
  und dem Port der `NameAndPortMessage` eine Adresse der Form `host:port` bilden; schlägt das fehl, gibt die Funktion
  den Fehler zurück.

Im Fehlerfall müssen `name` und `addr` konventionsgemäß leer sein.

Verwenden Sie die Funktionen
[`net.SplitHostPort`](https://pkg.go.dev/net#SplitHostPort)
(um den Host aus der Adresse auszulesen),
[`net.JoinHostPort`](https://pkg.go.dev/net#JoinHostPort)
(um Host und Port wieder zusammenzusetzen) und
[`strconv.Itoa`](https://pkg.go.dev/strconv#Itoa)
(um einen `int` in einen `string` zu konvertieren).
`net.JoinHostPort` setzt bei IPv6-Adressen automatisch die nötigen eckigen Klammern, sodass Sie nicht zwischen
IPv4 und IPv6 unterscheiden müssen.

<!-- time estimate: 10 min -->

[ER] Registrieren Sie einen POST-Endpunkt `/register`, der aus dem JSON-Payload mithilfe von `extractNameAndAddress` den
Benutzernamen und die Adresse ausliest und in `AddressTable` speichert.

Bei Erfolg ist der Statuscode `200` ("OK").
Bei einem Fehler verwenden Sie hier und auch bei den weiteren HTTP-Handlern die Funktion
[`http.Error()`](https://pkg.go.dev/net/http#Error).
Diese schreibt eine Fehlermeldung auf den `http.ResponseWriter w` und setzt den Statuscode.

Ist ein solcher Name bereits vergeben, dann gibt der Server Statuscode `409` ("Conflict") und eine informative
Fehlermeldung zurück.

Können die nötigen Daten aus dem JSON-Payload nicht ausgelesen werden oder sind die Daten ungültig
(beispielsweise eine Portnummer, die kleiner als 1 oder größer als 65535 ist),
so antwortet der Server mit `400` ("Bad Request").

(Eine Auffrischung zu Servern und JSON finden Sie in den Aufgaben [PARTREF::go-http-server] und [PARTREF::go-json]).

[HINT::Mein Server antwortet auf `/register` gar nicht mehr]
Ein möglicher Grund dafür ist ein Deadlock:
Falls Ihre Methode `AddIfAbsent` den Mutex selbst sperrt (`t.mu.Lock()`) und dann eine andere Methode von `AddressTable`
aufruft (beispielsweise `t.GetAddrOf()`), die denselben Mutex erneut zu sperren versucht, blockiert diese Goroutine für
immer.
[ENDHINT]

[FOLDOUT::Warum soll ich `http.Error()` verwenden?]
Diese Funktion ermöglicht es, mit einem Aufruf sowohl den Statuscode als auch die Fehlermeldung zu setzen.

Ohne `http.Error()` müsste man den Statuscode zunächst selbst setzen und anschließend die Fehlermeldung schreiben.
Außerdem müsste man selbst ein `\n` hinzufügen, damit die Ausgabe im Terminal schön formatiert ist.
[ENDFOLDOUT]

[FOLDOUT::Warum kommt der Port aus dem Payload und nicht aus der Anfrage?]
Man könnte auf die Idee kommen, Port und IP-Adresse beide aus `r.RemoteAddr` auszulesen — schließlich steckt dort ja
"IP:Port" drin.
Das funktioniert aber nicht:
Der Port, über den der Peer diese Registrierungsanfrage sendet, ist ein kurzlebiger, vom Betriebssystem automatisch
vergebener _ephemeral port_ (siehe
[Wikipedia: Ephemeral port](https://en.wikipedia.org/wiki/Ephemeral_port)).
Er hat nichts mit dem Port zu tun, auf dem der Peer selbst später auf eingehende Chat-Nachrichten lauscht.
Deshalb muss der Peer seinen tatsächlichen, dauerhaften Port explizit mitschicken — nur die IP-Adresse darf
unverändert aus der Anfrage übernommen werden, da sie für beide Verbindungen dieselbe ist.
[ENDFOLDOUT]

<!-- time estimate: 10 min -->

[ER] Registrieren Sie einen GET-Endpunkt `/{username}`, der entweder ein JSON zurückgibt, in dessen
Feld `addr` die Adresse von `username` steht, oder den Statuscode `404` ("Not Found"), falls es
keinen solchen Benutzer gibt.

Setzen Sie vor dem Schreiben des JSON-Payloads den Header `Content-Type: application/json`, damit alle Konsumenten des
Endpunkts wissen, worum es sich bei der Antwort handelt.
Lesen Sie in der
[Dokumentation von `http.ResponseWriter.Header`](https://pkg.go.dev/net/http#ResponseWriter.Header)
nach, wie das genau funktioniert.

<!-- time estimate: 15 min -->

[ER] Implementieren Sie abschließend noch einen POST-Endpunkt `/unregister`.
Dieser soll analog zu `/register` eine `NameAndPortMessage` aus dem JSON-Payload auslesen und den entsprechenden Eintrag
aus der Tabelle entfernen, sofern ein solches Benutzername-Adresse-Paar existiert.
Der gespeicherte Eintrag für `username` muss dabei exakt aus der IP-Adresse der aktuellen Anfrage und dem übergebenen
`port` bestehen (also derselben Berechnung wie bei `/register`).

Bei Erfolg ist der Statuscode `200` ("OK"); gibt es keinen solchen Eintrag, so ist der Statuscode `404` ("Not Found").
Können die nötigen Daten aus dem JSON-Payload nicht ausgelesen werden oder sind die Daten ungültig (beispielsweise
eine Portnummer, die kleiner als 1 oder größer als 65535 ist), so antwortet der Server mit `400` ("Bad Request").

(So kann sich niemand mit einer fremden IP-Adresse oder einem fremden Port für einen Benutzernamen ausloggen, der ihm
gar nicht gehört — deshalb wird `port` hier überhaupt im Payload gebraucht, obwohl `/unregister` streng genommen
nur den `username` bräuchte, um den passenden Tabelleneintrag zu finden.)

<!-- time estimate: 10 min -->

[HINT::Wie teste ich das?]
Die Funktionsfähigkeit des Lookup-Servers können Sie mittels [PARTREF::curl] überprüfen.

Eine POST-Anfrage mit JSON-Payload:

```bash
curl -i -X POST -d '{"username":"alice","port":8081}' http://localhost:8083/register
```

Eine GET-Anfrage:

```bash
curl -i -X GET http://localhost:8083/alice
```

Probieren Sie ein paar Kombinationen aus, um sicherzustellen, dass Ihr Lookup-Server tatsächlich
funktioniert.
[ENDHINT]


### Testen

Starten Sie Ihren Lookup-Server neu, damit die Adresstabelle leer ist,
und führen Sie in einem anderen Terminal folgende Kommandos aus:

[EC] `curl -i -X GET http://localhost:8083/alice`

[EC] `curl -i -X POST -d '{"username":"alice","port":8081}' http://localhost:8083/unregister`

[EC] `curl -i -X POST -d '{"username":"alice","port":8081}' http://localhost:8083/register`

[EC] `curl -i -X POST -d '{"username":"alice","port":8081}' http://localhost:8083/register`

[EC] `curl -i -X GET http://localhost:8083/alice`

[EC] `curl -i -X POST -d '{"username":"alice","port":8081}' http://localhost:8083/unregister`

[EC] `curl -i -X GET http://localhost:8083/alice`

[EC] `curl -i -X GET http://localhost:8083/register`

[EQ] Warum antwortet der Server auf `curl -i -X GET http://localhost:8083/register` mit Statuscode `404`,
obwohl `/register` doch ein Endpunkt dieses Servers ist?

[EC] `curl -i -X POST -d '{"username":"alice"}' http://localhost:8083/register`

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Lösungen]

**Kommandoprotokoll**
[PROT::ALT:go-chat-lookup-server.prot]

[INCLUDE::ALT:]

Quellcode als Teil des Projekts siehe unter [TREEREF::lookup].
[ENDINSTRUCTOR]
