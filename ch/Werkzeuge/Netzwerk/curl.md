title: Datenübertragung mit curl
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: http-GET, http-POST, http-State
---

[SECTION::goal::experience]
Ich kann das curl-Kommando für verschiedene Netzwerk-Datenübertragungen verwenden und 
verstehe die wichtigsten Optionen für HTTP-Requests, Datei-Downloads und API-Interaktionen.
[ENDSECTION]


[SECTION::background::default]
In der modernen Softwareentwicklung und Systemadministration ist die Kommunikation mit 
Webservern per HTTP alltäglich geworden. 
Das curl-Kommando ist eine Art Schweizer Messer dafür.
Man bekommt damit von einfachen Abrufen bis zu recht komplexen maßgeschneiderten Requests
verblüffend viele Dinge ohne Programmierung hin, direkt auf der Kommandozeile.
[ENDSECTION]


[SECTION::instructions::detailed]

### Was ist curl und warum ist es wichtig?

curl (Client URL) ist ein Kommandozeilen-Tool zur Datenübertragung, 
das in praktisch allen Linux-Distributionen (und anderen Plattformen) verfügbar ist. 
Es unterstützt zahlreiche Protokolle wie HTTP, HTTPS, FTP, SFTP und andere und bietet
genaue Kontrolle über Request-Headers, Methoden und Daten.

### Grundlegende Syntax und erste Schritte

Die Basissyntax von curl ist einfach strukturiert:

```bash
curl [optionen] [URL...]
```

[EC] Führen Sie einen GET-Request aus und inspizieren Sie die JSON-Antwort:

```bash
curl https://httpbin.org/get
```

Die Antwort sollte JSON-Daten mit Ihren Request-Details enthalten (z.B. Ihre IP, User-Agent, Headers).
<!-- EC1 -->

<!-- time estimate: 10 min -->


### HTTP-Methoden und Request-Steuerung

curl unterstützt alle gängigen HTTP-Methoden. 
Die wichtigsten Optionen für Request-Kontrolle:

- `-X METHOD`: Spezifiziert die HTTP-Methode (GET, POST, PUT, DELETE, etc.)
- `-d "param=value"`: Sendet ein Name/Wert-Paar als POST-Daten
- `-H "Header: Value"`: Fügt Custom-Headers hinzu

[EC] Führen Sie einen POST-Request mit Formulardaten `myname=Student` und `myage=25` an `https://httpbin.org/post` aus:

[HINT::Wie kombiniere ich mehrere Parameter?]
curl ermöglicht die Kombination mehrerer Parameter.
Sie können z.B. zwei Parameter gleichzeitig verwenden, um einen Request durchzuführen.

Die Syntax für einen POST-Request mit Formulardaten ist:
```bash
curl -X POST -d "param1=wert1&param2=wert2" <URL>
```

Das `-X POST` ist hier optional, da `-d` die HTTP-Methode automatisch auf POST setzt.
[ENDHINT]
<!-- EC2 -->

[EC] Senden Sie JSON-Daten `myname=Student` und `myage=25` 
mit entsprechendem Content-Type-Header:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"myname":"Student","myage":25}' https://httpbin.org/post
```
<!-- EC3 -->

[EQ] Vergleichen Sie die Antworten von [EREFC::2] und [EREFC::3]:
In welchem Feld der JSON-Antwort erscheinen die Daten jeweils?
<!-- EQ1 -->


### Datei-Downloads und Output-Kontrolle

curl bietet verschiedene Möglichkeiten, die Ausgabe zu steuern:

- `-o myfilename`: Speichert den Rumpf der Antwort unter angegebenem Namen 
  (statt ihn auf der Standardausgabe auszugeben)
- `-O`: Verwendet die letzte Komponente der URL als Dateiname
- `-v`: Verbose-Modus (zeigt detailliert die Kommunikation)

[EC] Laden Sie die Datei `https://httpbin.org/robots.txt` herunter 
und verwenden Sie den ursprünglichen Dateinamen für das Speichern der Antwort.
<!-- EC4 -->

[EC] Führen Sie den gleichen Download im verbose-Modus durch, 
um die HTTP-Kommunikation zu analysieren:
<!-- EC5 -->

<!-- time estimate: 20 min -->


### Headers und Authentifizierung

Für erweiterte HTTP-Kommunikation sind oft Headers und Authentifizierung relevant:

- `-H "Header: Value"`: Custom Headers setzen
- `-I`: Nur Response-Headers abrufen (`HEAD`-Request)

[EC] Rufen Sie nur die HTTP-Headers einer Webseite `https://httpbin.org/status/200` ab.
<!-- EC6 -->

[EC] Senden Sie einen Request mit Custom-Headers (`Accept: application/json` und `User-Agent: MyCustomAgent/1.0`) an `https://httpbin.org/headers`. 
Überprüfen Sie in der Antwort, dass Ihre Custom-Headers korrekt übertragen wurden.
<!-- EC7 -->


### Erweiterte Funktionen: Cookies und Sessions

curl kann Cookies verwalten und Sessions aufrechterhalten:

- `-c mycookies.txt`: Cookies in Datei speichern
- `-b mycookies.txt`: Gespeicherte Cookies verwenden
- `-b "mycookie=myvalue"`: Einzelne Cookies direkt setzen

[EC] Speichern Sie das Cookie `mysession=abc123` in der Datei `mycookies.txt`. 
Verwenden Sie dazu den Endpunkt `/cookies/set/mysession/abc123` von `https://httpbin.org`.

[NOTICE]
Sie können die URL-Basis und den Endpunkt direkt zusammenfügen:
`<URL-Basis><Endpunkt>` = `https://.../<endpunkt>`
[ENDNOTICE]
<!-- EC8 -->

[EC] Senden Sie das gespeicherte Cookie aus `mycookies.txt` an `https://httpbin.org/cookies`.  
<!-- EC9 -->

<!-- time estimate: 15 min -->


### Datei-Upload und mehrteilige Anfragen

Manchmal möchten Sie nicht nur eine Datei hochladen, sondern gleichzeitig auch zusätzliche Informationen dazu senden (z.B. eine Beschreibung oder Metadaten).
Die `-F`-Option ermöglicht genau das, indem sie mehrere Felder in einer einzigen Anfrage verpackt:

- `-F "fieldname=value"`: Sendet ein Text-Feld mit einem einfachen Wert
- `-F "file=@filename"`: Sendet den Inhalt einer Datei

Jeder `-F`-Parameter ist ein separates Feld in der Anfrage.
Wenn Sie mehrere `-F`-Parameter verwenden, werden alle Felder zusammen mit `multipart/form-data`-Codierung in einer Anfrage versendet.
So können Sie z.B. gleichzeitig eine Beschreibung (Text) und eine Datei übertragen.

[EC] Erstellen Sie eine Datei `mytestfile.txt` mit dem Text `Testdatei für curl Upload`.
Laden Sie die Datei zusammen mit dem Text-Feld `mydescription=Test Upload` nach `https://httpbin.org/post` hoch.
Verwenden Sie die `-F`-Option mit `myfile=@mytestfile.txt` für das Dateifeld und `mydescription=Test Upload` für das Text-Feld.

Überprüfen Sie in der Antwort, dass beide Felder korrekt übertragen wurden 
(schauen Sie in der JSON-Antwort nach den Keys `files` und `form`).
<!-- EC10 -->

[EQ] In welchen Situationen würden Sie curl gegenüber einem grafischen HTTP-Client 
oder einem Browser bevorzugen? Nennen Sie zwei Fälle.
<!-- EQ2 -->

<!-- time estimate: 15 min -->

### Weiterführend

- [curl Tutorial Basics](https://curl.se/docs/tutorial.html) – Grundlegende Einführung in curl
- [HTTP Methods with curl](https://everything.curl.dev/http/index.html) – Detaillierte Referenz zu HTTP-Methoden
- [Authentication with curl](https://everything.curl.dev/http/auth) – Weitere Authentifizierungsmethoden

[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]

Knackpunkte:

- [EREFC::2]: Response enthält `form`-Feld mit `myname` und `myage`.
- [EREFC::3]: Response enthält `json`-Feld mit `myname` und `myage`.
- [EREFC::10]: Response enthält `files`-Feld (Datei) und `form`-Feld (Textfeld).

### Kommandoprotokoll

[PROT::ALT:curl.prot]

### Markdown

[INCLUDE::ALT:curl.md]
[ENDINSTRUCTOR]