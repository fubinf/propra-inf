title: "HTTP Chat - Schutz"
stage: alpha
timevalue: 3
difficulty: 3
requires: go-http-chat-core
---

[SECTION::goal::experience,idea]

- Ich habe mich mit Verschlüsselung auseinandergesetzt (RSA und Diffie-Hellman-Schlüsselaustausch).
- Ich habe Ende-zu-Ende-Verschlüsselung (E2EE, "end-to-end-encryption") implementiert.

[ENDSECTION]

[SECTION::background::default]

Zurzeit ist der Chat nicht besonders vor möglichen man-in-the-middle-Angriffen geschützt: Wir verschicken Passwörter im
sowie alle Nachrichten als unverschlüsselten JSON-Text. In dieser Aufgabe implementieren Sie die oben angesprochenen
Schutzmaßnahmen.

[ENDSECTION]

[SECTION::instructions::detailed]

Die erste Schwachstelle ist das Anmeldeverfahren. Diese lässt sich durch ein Handshake und RSA-Verschlüsselung beheben.

### Lösungsvorschlag

- Client spricht den Server an, "ich möchte mich bitte anmelden. Schick mir deinen öffentlichen RSA Schlüssel".
- Nach dem Empfang des Schlüssels wird dieser benutzt, um die Anmeldedaten (Benutzername und Passwort) zu 
verschlüsseln.
- Der Server entschlüsselt die Daten und kann wie bereits implementiert fortfahren (Auth Token erstellen usw).

Nun geht es mit dem Programmieren los!

### Öffentlichen Schlüssel dem Client kommunizieren

- Informieren Sie sich, wie man ein RSA Schlüsselpaar [erzeugt](https://pkg.go.dev/crypto/rsa#GenerateKey). Dieser darf 
für verschiedene Clients gleich bleiben.
- Registrieren Sie beim Server noch einen HTTP-Handler. Dieser nimmt eine `GET`-Anfrage entgegen und antwortet mit
einer JSON-Darstellung einer `GenericMessage` mit einem Feld `Data`, welches den öffentlichen Schlüssel des Servers 
enthält. Vergessen Sie nicht die `base64` Kodierung! [Diese](https://pkg.go.dev/crypto/x509#MarshalPKIXPublicKey) und
[diese](https://pkg.go.dev/encoding/pem#EncodeToMemory) Funktionen helfen Ihnen dabei.
- Empfangen Sie nun auf der Clientseite den Schlüssel. Für Testzwecke lohnt es sich, diesen einfach im Terminal 
anzuzeigen - sowohl auf der Server- als auch auf der Clientseite.

Probieren Sie jetzt das Ganze aus - loggen Sie sich als Client ein. Neben den gewöhnlichen Meldungen sollen Sie nun den 
öffentlichen Schlüssel des Servers sehen. Dieser soll innerhalb einer Server-Sitzung gleich bleiben.

- [EC] (Trace Alice)
- [EC] (Trace Bob)

### Anmeldedaten verschlüsseln und an den Server senden

Hier müssen sich Client und Server auf eine gewisse Verschlüsselungsreihenfolge einigen. Wir schlagen vor, zuerst die 
`AuthMessage` zu serialisieren, zu verschlüsseln und als `GenericMessage.Data` zu senden.

- Wandeln Sie die Textdarstellung des Schlüssels in `*rsa.PublicKey` um. Die Umwandlung besteht aus drei Schritten:
    * Konvertieren von einer Base64 Zeichenkette zurück zu `[]byte`.
    * Erstellen eines `pem.Block{}` aus der Bytefolge `[]byte` ([Hilfe](https://pkg.go.dev/encoding/pem#Decode)).
    * Den Schlüssel aus den `block.Bytes` zu [parsen](https://pkg.go.dev/crypto/x509#ParsePKIXPublicKey) und als 
    `*rsa.PublicKey` zu casten.
- Serialisieren Sie die `AuthMessage` (`json.Marshal`).
- Verschlüsseln Sie die Byte-Darstellung von `AuthMessage` mithilfe von 
   [dieser Funktion](https://pkg.go.dev/crypto/rsa#EncryptOAEP).
- Kodieren Sie die verschlüsselten Daten wieder als Base64 und verschicken Sie diese als `GenericMessage.Data` an den
   Server.

### Kommt der Server mit den neuen Daten klar?

Der Server muss natürlich die Daten wieder entschlüsseln. Daher:

- Passen Sie den Endpunkt so, dass er nun eine `GenericMessage` erwartet.
- `GenericMessage.Data` wird von base64 dekodiert und mit dem privaten Schlüssel des Servers 
   [entschlüsselt](https://pkg.go.dev/crypto/rsa#DecryptOAEP).
- Die entschlüsselten Daten als `AuthMessage` werden nun weiter für die Erzeugung des Auth Tokens benutzt.

Jetzt testen! 

Fügen Sie zwei `fmt.Println` Befehle kurz vor dem Entschlüsseln und nach dem Entschlüsseln der Daten im Server ein.
Dies dient jetzt dem Testen und der Veranschaulichung, dass die Daten tatsächlich verschlüsselt transportiert werden.

Überprüfen Sie nun die Chat-Funktionalität: Loggen Sie sich ein als Alice, als Bob und schicken Sie ein paar 
Nachrichten.

- [EC] (Trace Server)
- [EC] (Trace Alice)
- [EC] (Trace Bob)

### Code organisieren

Jetzt sind wir zu dem Zeitpunkt gekommen, wo unser Projekt ein bisschen mehr Struktur braucht. Wir haben beispielsweise 
zwei Funktionen, die sich um die Umwandlung zwischen Base64 und `*rsa.PublicKey` / `*rsa.PrivateKey` kümmern. Wäre es
nicht schöner, diese Funktionen in einem separaten Modul zu haben?

Aufgabe: lagern Sie die mehrmals auftauchende Code-Abschnitte in einzelne Funktionen aus, wo nötig/möglich - in separate
Module. Zu denen gehören u. a. dateisystembezogene Funktionen, Authentifizierung, Terminal Ein- und Ausgabe.

[NOTICE]

Das Problem von "Passwörtern-im-Klartext" ist dadurch behoben. Weiter geht es mit Ende-zu-Ende-Verschlüsselung (E2EE).

[ENDNOTICE]

### Diffie-Hellman-Schlüsselaustausch

Ende-zu-Ende-Verschlüsselung, die wir in dieser Aufgabe implementieren, basiert auf dem 
Diffie-Hellman-Schlüsselaustausch (Elliptic Curve Diffie-Hellman). Sie müssen das Verfahren nicht selber implementieren:
Zum Glück hat Go-Standardbibliothek alle nötigen Pakete bereits implementiert. Schauen Sie sich die kurze 
[Dokumentation](https://pkg.go.dev/crypto/ecdh) an.

#### Algorithmus:
- Wir einigen uns auf X25519-Kurve. Alle Schlüsselpaare von Clients werden mithilfe von dieser Kurve erzeugt.
- Server speichert öffentliche Schlüssel von eingeloggten Benutzern zusammen mit der Adresse. Sie können an dieser 
Stelle einen Typen `User` definieren.
- Erweitern Sie die `AuthMessage` um den öffentlichen Schlüssel (als Zeichenkette). Stellen Sie sicher, dass dieser 
a) korrekt an den Server gesendet wird und b) korrekt von dem Server empfangen wird.
- Stellen Sie sicher, dass ein Client den öffentlichen Schlüssel des Gesprächspartners rechtzeitig bekommt. Ein 
passender Zeitpunkt dafür wäre gleich nach dem "Mit wem willst du schreiben?". Das muss ein neuer Endpunkt auf der 
Serverseite sein. Das könnte hilfreich sein: 
[Dynamische Routen](https://stackoverflow.com/questions/64408209/net-http-simple-dynamic-routes).  
- Legen Sie eine Struktur an, die für E2EE zuständig ist. Diese könnte `EncryptionManager` heißen und soll die Namen 
von Gesprächspartner_innen zusammen mit ihren öffentlichen Schlüsseln speichern. Außerdem soll hier das Ver- und 
Entschlüsseln stattfinden. Von außen sichtbare Funktionen sind also:
    * `func Encrypt(msg []byte, to string) ([]byte, error)` 
   ([Dokumentation/Beispiel](https://pkg.go.dev/crypto/cipher#example-NewGCM-Encrypt)).
    * `func Decrypt(msg []byte, from string) ([]byte, error)`
     ([Dokumentation/Beispiel](https://pkg.go.dev/crypto/cipher#example-NewGCM-Decrypt)).
    * (Einen 32-Byte "Secret" aus einem `secret []byte` bekommen Sie anhand von `sha256.Sum256(secret)`)
- Achten Sie auf die Reihenfolge von Operationen: beim Senden empfehlen wir:
    * `Message` erstellen
    * `Message` serialisieren
    * `Message` verschlüsseln
    * `Message` als Base64 kodieren
    * als Teil von `GenericMessage` nochmal serialisieren
   
    Folglich sollen beim Empfangen alle Operationen rückwärts stattfinden:

    * `GenericMessage` empfangen
    * `GenericMessage.Data` von Base64 dekodieren
    * entschlüsseln
    * zu `Message` deserialisieren
   
    Passen Sie nun alle nötigen Stellen so an, dass die Nachrichten verschlüsselt transportiert werden. 
    Eine technische Einschränkung ist es, dass wir nun explizit kommunizieren müssen, von wem die Nachricht kommt 
    (beispielsweise als ein Header-Feld) - ansonsten weiß der Empfänger nicht, welcher öffentliche Schlüssel benutzt 
    werden soll. 
    
- Fügen Sie ein `fmt.Println` Kommando irgendwo im Server ein, um zu überprüfen, wie die verschlüsselten Nachrichten 
   aussehen.

Nun los mit Testen! Starten Sie den Server und zwei Clients, Alice und Bob. Schicken Sie ein paar Nachrichten und geben 
Sie anschließend die Traces ab.

[NOTICE]

**Wie kann man sich die Pakete anschauen?**

Dafür gibt es ein Tool - [Wireshark](https://www.wireshark.org/). Anhand des Tools können Sie alle Requests sehen, die
Ihr Rechner sendet und entgegennimmt und welche Daten sich jeweils in den Paketen befinden. Das Tool ist auch für das 
Testing von dieser Aufgabe sehr gut geeignet: Versetzen Sie sich in die Angreifer-Rolle hinein und probieren Sie aus, 
die Nachrichten von Bob zu Alice zu lesen.

[ENDNOTICE]

- [EC] (Trace Server)
- [EC] (Trace Alice)
- [EC] (Trace Bob)
- [EQ] Ist der Chat nun vollständig geschützt, oder gibt es immer noch Schwachstellen? Vor welchen Angriffen? 
Diskutieren Sie, welche Daten trotz unserer Schutzmaßnahmen immer noch zugänglich für die Angreifer bleiben. Wie lassen 
sich diese Daten schützen? 

[ENDSECTION]

[SECTION::submission::trace,reflection,program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Korrektheit, Codestruktur, Fehlerbehandlung]

Quellcode siehe [TREEREF::go_chat/client/encmgr/encryption_manager.go].

Korrektheit: Was schon in `go-http-chat-core` funktioniert hat, muss weiterhin funktionieren.

Codestruktur: Wir erwarten eine sinnvolle Kapselung von Funktionalität (beispielsweise in `ConnectionManager` oder 
`EncryptionManager`).

Fehlerbehandlung: Die Fehlermeldungen sollen (1) da sein und (2) verständlich sein.

[EREFQ::1] - alle plausiblen Antworten zählen als richtig. Das Einzige, was eindeutig falsch ist - "nein, unser Chat ist 
schon 100% geschützt, fertig".

Falls die Studierenden die in der Musterlösung erwähnten Schwachstellen schon selber behoben haben, müssen sie diese 
hier nicht mehr diskutieren. 

[ENDINSTRUCTOR]
