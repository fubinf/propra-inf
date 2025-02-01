title: "HTTP Chat"
stage: alpha
timevalue: 4
difficulty: 3
---

[SECTION::goal::experience,product]

- Ich habe mich mit HTTP Requests und Servern auseinandergesetzt.
- Ich weiß, wie ich Daten im JSON-Format sende und empfange.
- Ich habe mir ein Chat-Programm im Terminal gebaut, welches Nachrichtenaustausch 
  zwischen mehreren Benutzer_innen über ermöglicht. 

[ENDSECTION]

[SECTION::background::default]

Messengers sind ein wesentlicher Teil unseres Lebens geworden. Wie kompliziert ist es denn, die grundlegende 
Funktionalität zu implementieren?

Die Anwendung, die Sie im Laufe der Aufgabe bauen, ist ein gutes Beispiel und/oder Ausgangspunkt für Erweiterungen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Einleitung

Unsere Anwendung besteht aus einem __Server-Programm__ und mehreren __Client-Programmen.__
Clients dürfen sich bei dem Server anmelden und erhalten bei Erfolg einen __Token__, mithilfe dessen
sie von dem Server wiedererkannt werden können.
In dieser Version sparen wir uns alle komplizierteren Authentifizierungsverfahren. 

### Anforderungen

- Benutzer_innen können sich einloggen 
(und zwar genau einmal; mehrere Sitzungen für einen Benutzer müssen nicht unterstützt werden);
- Benutzer_innen können den Gesprächspartner frei wählen, behalten aber die Möglichkeit, 
alle einkommende Nachrichten zu sehen;
- falls etwas nicht klappt, müssen die Benutzer_innen eine informative Fehlermeldung sehen.

### 0. Bevor Sie mit Programmieren loslegen...
- fangen Sie mit einer Whiteboarding-Session an: Überlegen Sie sich, welche Rollen es in Ihrer Anwendung geben wird 
und wie die Verantwortung verteilt wird. Wie sehen die Schnittstellen aus? Was müssen die Module voneinander wissen? 
Welche Funktionalität kann zwischen den Modulen geteilt werden?
- machen Sie sich Gedanken über die Projektstruktur. Eine (von uns empfohlene) Option wäre es, mehrere Module unter 
einer `go.work` Datei 
zu behalten. Das wäre besonders vorteilhaft, wenn Sie beispielsweise die Datentypen zwischen dem Client und dem Server 
sowie verschiedene Hilfsmethoden wiederverwenden wollen. `client` und `server` sind hier zwei komplett voneinander
getrennte Module.
- __nie__ einen Schlüssel in git committen! Bewahren Sie alle nötigen Schlüssel in einer `.env` Datei auf. Vergessen Sie 
nicht diese in `.gitignore` hinzuzufügen (oder in .git/info/exclude).

### 1. Einen HTTP-Server hochfahren

* Führen Sie in dem `server` Verzeichnis `go mod init server` aus. So wird automatisch eine `go.mod` Datei angelegt, 
welche dieses Modul sowie seine Abhängigkeiten deklariert.
* Legen Sie nun eine `main.go` Datei an. Das ist der Einstiegspunkt von dem Server-Prozess.
* Der Server soll auf der Adresse `"0.0.0.0:port"` lauschen - so können andere Rechner den Server über eine IP-Adresse 
finden.
* Lesen Sie die Dokumentation: [Server](https://pkg.go.dev/net/http#Server) und 
[ServeMux](https://pkg.go.dev/net/http#ServeMux) (Router). ServeMux ist eine präferierte Option, da dieser Typ eine gute 
Trennung und Skalierbarkeit von URL-Pfaden ermöglicht.
* Legen Sie nun ein weiteres Modul an: `chattypes` (`go mod init ...`, `chattypes.go`). Hier können wir alle Typen 
definieren, die sowohl im Server als auch im Client benutzt werden. Um Sie dann aus den anderen Modulen benutzen können, 
Sie im Root-Verzeichnis folgendes Kommando aus: `go work init ./server ./client ./chattypes`.
* Definieren sie einen Typen `Message`. Der soll einem JSON-Objekt entsprechen, welches __mindestens__ das Feld `Data`
enthält. Stellen Sie sicher, dass Ihr Typ (`struct`) von der `encoding/json` Bibliothek richtig erkannt wird
([Dokumentation](https://pkg.go.dev/encoding/json)).
* Registrieren Sie nun einen Handler für einen `POST`-Endpunkt (beispielsweise `/login`), damit Sie die grundlegende 
Funktionalität überprüfen können(beispielsweise mit `curl` oder [Postman](https://www.postman.com/)). Dieser soll eine 
`Message` aus dem Request Body auslesen und im Terminal anzeigen. Falls Sie sich fragen, wie das geschehen soll, können 
Sie [hier](https://stackoverflow.com/questions/15672556/handling-json-post-request-in-go) und 
[hier](https://pkg.go.dev/encoding/json#NewDecoder) nützliche Information finden.

Starten Sie nun den Server und führen Sie in einem anderen Terminalfenster folgende Testbefehle aus:

- [EC] `curl -X POST -d '{"data": "hi there"}' http://127.0.0.1:3000/login`
- [EC] `curl -X POST -d '{"other_data": "hi there"}' http://127.0.0.1:3000/login`
- [EC] `curl -X POST -d '{"other_data": "hi there"' http://127.0.0.1:3000/login`

[FOLDOUT::wie gebe ich externe Abhängigkeiten in eine Handler-Funktion über?]
Frage: Wie Sie wahrscheinlich schon gelesen haben, muss eine Handler-Funktion einer ganz spezifischen Signatur 
entsprechen: `func(http.ResponseWriter, *http.Request)`. 
Was tun, wenn eine Handler-Funktion zusätzliche Parameter braucht?

Antwort: Decorator Entwurfsmuster implementiert durch Closures.

```go
// so muss eine Handler-Funktion aussehen (Standardbibliothek)
type HandlerFunc func(http.ResponseWriter, *http.Request)

// Deklaration/Definition - eine Funktion, die eine http.HandlerFunc zurückgibt
func decoratedHandler(a, b, c string) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        // tue etwas mit a, b und/oder c     
    } 
}

// Benutzung
router.HandleFunc("GET /stuff", decoratedHandler("a", "b", "c"))
```

[ENDFOLDOUT]

[FOLDOUT::Kein Fehler, auch wenn JSON-Struktur dem erwarteten Struct nicht entspricht?]

Im Testfall mit `{"other_data": "hi there"}` hat unser Server weder die Daten ausgelesen noch einen Error geschmissen.
Es ist einfach **nichts** passiert.

Selbst wenn das auf den ersten Blick schön scheint - ist es wirklich so? Man kann sich sehr leicht vertippen und es 
fällt einem erst viel später auf, dass JSON an dieser Stelle nicht richtig empfangen und dekodiert wird.

Es gibt Bibliotheken, die eine solche Validierung bereitstellen - beispielsweise 
[go-playground/validator](https://github.com/go-playground/validator). Eine solche Validierung selbst zu implementieren
wäre auch eine gute Übung, ist jedoch nicht das Thema dieser Aufgabe.

[ENDFOLDOUT]

### 2. Client: Benutzereingaben und Anbindung zum Server

Der Client kümmert sich im Wesentlichen um die Benutzereingaben. Zu diesen gehören Benutzername/Passwort und die 
darauffolgenden Nachrichten, die an einen anderen Client verschickt werden.

* initialisieren Sie ein Modul namens `client` in dem `client` Verzeichnis (`go mod init ...` und `main.go`).
* implementieren sie das Anmeldeverfahren (unter anderem
[Passworteingabe ohne "echo"](https://pkg.go.dev/golang.org/x/term#ReadPassword), `go get golang.org/x/term`, 
`go mod tidy`): Benutzer gibt den Namen im Terminal ein, dann das Passwort, und bekommt anschließend eine freundliche 
Begrüßung Ihrer Wahl.
* Für Testzwecke können Sie zuerst Benutzername und Passwort in einem [POST-Request](https://pkg.go.dev/net/http#Post)
(bzw. 
[hier](https://www.practical-go-lessons.com/post/go-how-to-send-post-http-requests-with-a-json-body-cbhvuqa220ds70kp2lkg
))
an den Server verschicken. Legen Sie hierfür einen anderen Datentypen `AuthMessage` mit `Username` und `Password` 
Feldern und passen Sie die Handler-Methode auf der Serverseite so an, dass sie jetzt eine `AuthMessage` erwartet.

Starten Sie nun den Server und den Client. Melden Sie sich im Client an.

- [EC] Wie sieht das im Client-Terminal aus? (Trace)
- [EC] Wie sieht das im Server-Terminal aus? (Trace)

### 3. Auth Token

Der Server darf keine Passwörter behalten, daher kreieren wir anhand von dem Benutzernamen und dem Passwort einen Token
(beziehungsweise `Hash`).

- generieren Sie einen Schlüssel (beispielsweise eine zufällige Zeichenkette mit 64 Zeichen) und legen Sie diesen in der 
- Datei `.env` in dem `server` Modul ab (beispielsweise als `key=...`).
- implementieren Sie nun eine Funktion, welche `username` und `password` als Parameter bekommt und ein Tupel 
(`token`, `error`) ausgibt. Dies sind die einzelnen Schritte:
    * den Schlüssel aus der Datei auslesen;
    * die Parameter auf eine gewisse Art und Weise zu einer Zeichenkette zusammenfügen;
    * einen Hash-Wert [erstellen](https://pkg.go.dev/crypto/hmac#New) und mithilfe dessen eine Bytefolge produzieren;
    * diese Bytefolge als Base64 (`base64.URLEncoding`) kodieren und somit eine Zeichenkette kreieren, die unser 
    Authentifizierungstoken wird.
- packen Sie nun den Token in eine oben definierte `Message` ein und verschicken Sie diese als Response auf den Request.
Passen Sie den Handler im Client so an, dass der empfangene Token im Terminal angezeigt wird.

[HINT::Wie soll das bitte funktionieren?]

`http.ResponseWriter` implementiert die `Write([]byte) (int, error)` Methode und somit auch das
`io.Writer` Interface. Das ermöglicht Kodierung von `struct`s als JSON-Objekte direkt in den `Writer`:
```go
json.NewEncoder(w).Encode(Message{Data: "hi there"})
```

Achten Sie aber darauf, dass die Headers richtig gesetzt sind und die andere Seite ein JSON-Objekt als Response
erwartet.

[ENDHINT]

Versuchen Sie sich nun einzuloggen! Aber als verschiedene Benutzer:

- [EC] Benutzername: "Alice", Passwort: "alice_password". (Trace)
- [EC] Benutzername: "Bob", Passwort: "bob_password". (Trace)
- [EC] Benutzername: "Alice", Passwort: "alice_password". (Trace)

### 4. Nachrichten empfangen können

Wie sollen unsere Clients die Nachrichten von dem Server oder den anderen Clients empfangen? Um dies zu ermöglichen, 
müssen sie einen Endpunkt bereitstellen. Hier müssen Sie ein URL-Schema festlegen. Eine Möglichkeit wäre
`http://0.0.0.0:port/username`. Was brauchen wir dafür?

* ein freier Port. Ein hilfreicher Trick ist es, vom Betriebssystem eine Portnummer `:0` anzufragen. Sie dürfen 
[diese Funktion](https://gist.github.com/sevkin/96bdae9274465b2d09191384f86ef39d) benutzen (lesen und verstehen ist 
aber auch sehr willkommen).
* ein Endpunkt von der Clientseite, welcher `POST`-Anfragen zu oben definierten URL entgegennimmt (hier können Sie die
Schritte aus Punkt 1. nochmal üben).
* Der zentrale Server muss diesen Endpunkt auch kennen. Stellen Sie sicher, dass der Server den "Pfad" zusammen mit 
Benutzernamen und Passwort bekommt. Alternativ könnte Client die Portnummer mitschicken, die für Anfragen offen wird, 
und der Server stellt die komplette Adresse selber zusammen.

**curl** Testing. Gehen Sie die Anweisungen durch und geben dann zwei Terminal-Traces
ab: für den Server und für den Client.

1. Starten Sie den Server und den Client (eine Nachricht wie "receiving messages at http://#.#.#.#:#/#
wäre sehr hilfreich).
2. Loggen Sie sich im Client ein.
3. Beenden Sie den Serverprozess (Ctrl+C) und schicken stattdessen eine Nachricht an den Client via **curl**:
   `curl -X POST -d '{"data":"Hello there!"}' http://#.#.#.#:#/#`

- [EC] (Server-Terminal Trace)
- [EC] (Client-Terminal Trace)

[NOTICE]

Warum können wir nicht die ganze Adresse mit übergeben?

Das würde auch funktionieren. Wir müssten aber die IP-Adresse des Rechners von dem Betriebssystem abfragen und dann
sicherstellen, dass es wirklich die Adresse ist, die für den Server sichtbar ist. Stattdessen schauen wir uns den
Request genauer an - dieser enthält bereits die IP-Adresse (`r.RemoteAddr`).

[ENDNOTICE]

### 5. "Input loop"

Das wird in unserem Fall eine Funktion sein, die in einer separaten _Goroutine_ gestartet wird und in einer 
Endlosschleife Benutzerabgaben von `os.Stdin` abliest und an den Server verschickt.

Anforderungen:

* Die Funktion hat zwei Parameter: `serverAddr string` und `errorChan chan<- error`.
* Die Funktion hat eine hübsche Prompt-Nachricht (Sie dürfen hier "hübsch" relativ frei interpretieren).
* Die Funktion bricht ab, falls "-q" abgelesen wurde. Danach darf der Server ausgeschaltet werden.
* Ansonsten packt sie die Eingabe in eine `Message` ein und verschickt sie in einem `POST` Request an die `serverAddr`.
* alle Fehler werden in `errorChan` geschrieben, die Funktion läuft weiter.

Testing. Hier geht es wieder um zwei Traces.

1. Starten Sie den Server und den Client, loggen Sie sich ein.
2. Schicken Sie ein paar Nachrichten an den Server.
3. Beenden Sie den Client, indem Sie `-q` eingeben.

- [EC] (Server-Terminal Trace)
- [EC] (Client-Terminal Trace)

### 6. Einen Client finden

Wie findet die Nachricht von einem Client ihren Empfänger? Intuitiv hat man hier zwei Optionen:

1. Die Nachricht selbst enthält ein Feld `To`. Dann muss der Server einmal die Nachricht geparst haben, bis die 
Nachricht weitergeleitet wird.
2. Wir fügen einen Header `To` ein. Das spart uns eine Decode-Encode Runde und eignet sich für den Fall besser, wenn der 
komplette Inhalt verschlüsselt wäre. Wir empfehlen diese Lösung. 

Welche Daten braucht der Server, um einen Client finden zu können? Eigentlich nur seine Adresse.

[WARNING]

Legen Sie jetzt ein Packet (Verzeichnis) unter `server` an und nennen Sie diesen `connmgr` (ConnectionManager). Dort
definieren Sie eine Einheit (`type ConnectionManager struct {...}`), welche für die Datenverwaltung zuständig wird.
Definieren Sie außerdem eine "Konstruktor"-Methode `New()` und die nötigen thread-sicheren get/set-Methoden. Das soll
ungefähr so aussehen:

```go
type ConnectionManager struct {
    users   map[string]strng
    usersMu sync.RWMutex
}

func (c *ConnectionManager) AddUser(username, addr string) {
    c.usersMu.Lock()
    defer c.usersMu.Unlock()
    users[username] = addr
}

...

cm := connmgr.New()
```

Das eliminiert auf einmal eine Menge von "ich habe das übersehen"-Fehler und macht Ihren Code verständlicher für die
anderen Go-Entwickler.

[ENDWARNING]

* legen Sie ein Map `map[string]string` an, um die Benutzeradressen mithilfe von Benutzernamen wieder finden können 
(Maps sind nicht Thread-sicher: falls Sie ein Map in mehreren Goroutinen benutzen, müssen alle Zugriffsoperationen über
einen `sync.RWMutex` geschehen).
* Passen Sie die "input loop" so an, dass man zuerst den Gesprächspartner wählt und den gewählten Namen in 
Prompt-Nachricht sieht. 
* fügen Sie einen Handler für die Nachrichten an (Server Seite). Dieser muss zuerst überprüfen, ob es einen Header mit 
`Authorization: /authToken/` gibt und ob ein Client mit diesem Token tatsächlich registriert wurde (Vorschlag: 
`map[string]string`, token-username Paare). Weiterhin muss ein Header `To` ausgelesen werden. Falls
dieser existiert - leiten Sie die Nachricht einfach weiter an den Empfänger.
* Fügen Sie in `Message` zusätzlich Felder `Time` und `From` ein. Zeitstempel darf Stunden, Minuten und Sekunden 
anzeigen (16:27:03). Machen Sie diese Informationen für den Benutzer sichtbar.
* Passen Sie die "-q" Option so, dass sie nur den letzten Chat schließt und nicht die ganze App. Folgendes soll möglich
sein: Benutzer A anschreiben - "-q" - Benutzer B anschreiben. 

Funktionalität prüfen:

1. Starten Sie den Server und **drei** Clients: beispielsweise "Alice", "Bob" und "Eva".
2. Schicken Sie ein paar Nachrichten: von Alice zu Bob, von Bob zu Alice.
3. Schreiben Sie als Eva Bob an.
4. Schließen Sie als Bob das Gespräch mit Alice und antworten Sie auf Evas Nachricht.

- [EC] (Terminal Trace Alice)
- [EC] (Terminal Trace Bob)
- [EC] (Terminal Trace Eva)

Im Wesentlichen - das war's! Wie am Anfang erwähnt, fühlen Sie sich frei die Funktionalität selber verbessern und 
erweitern.

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Korrektheit, Entwurfsstruktur]

Quellcode siehe [TREEREF::go_chat/server/main.go].

In erster Linie orientieren wir uns auf korrekte Funktionsweise.

Den Code lesen, insbesondere Fehlerbehandlung. `if err != nil { panic(err) / return err }` reicht oft aus, aber 
eigene Fehlermeldungen sind an manchen Stellen sehr vorteilhaft. Wir wollen das Bedenken sehen, "was tut mein Code, 
wenn XYZ schiefgeht?"

Modularität ist an dieser Stelle noch nicht gefragt: Sinnvolle Unterteilung von Funktionalität in einzelne Funktionen
ist genug.

[ENDINSTRUCTOR]
