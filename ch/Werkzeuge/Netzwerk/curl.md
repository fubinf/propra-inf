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

Optional: Für eine grundlegende Einführung lesen Sie bitte:
[curl Tutorial Basics](https://curl.se/docs/tutorial.html)


### Grundlegende Syntax und erste Schritte

Die Basissyntax von curl ist einfach strukturiert:

```bash
curl [optionen] [URL...]
```

[EC] Testen Sie curl mit einem einfachen GET-Request. 
Führen Sie folgenden Befehl aus und dokumentieren Sie die Ausgabe:

```bash
curl https://httpbin.org/get
```
<!-- time estimate: 15 min -->


### HTTP-Methoden und Request-Steuerung

curl unterstützt alle gängigen HTTP-Methoden. 
Die wichtigsten Optionen für Request-Kontrolle:

- `-X METHOD`: Spezifiziert die HTTP-Methode (GET, POST, PUT, DELETE, etc.)
- `-d "param=value"`: Sendet ein Name/Wert-Paar als POST-Daten
- `-d "data"`: Sendet POST-Daten in einem anderen Format
- `-H "Header: Value"`: Fügt Custom-Headers hinzu
- `-G`: Konvertiert POST-Daten zu GET-Parametern

Optional: Für detaillierte HTTP-Methoden-Referenz siehe:
[HTTP Methods with curl](https://everything.curl.dev/http/index.html)

[EC] Führen Sie einen POST-Request mit Formulardaten `myname=Student` und `myage=25` aus:  

[EC] Senden Sie JSON-Daten `myname=Student` und `myage=25` 
mit entsprechendem Content-Type-Header:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"myname":"TestUser","myage":"999"}' https://httpbin.org/post
```


### Datei-Downloads und Output-Kontrolle

curl bietet verschiedene Möglichkeiten, die Ausgabe zu steuern:

- `-o myfilename`: Speichert den Rumpf der Antwort unter angegebenem Namen 
  (statt ihn auf der Standardausgabe auszugeben)
- `-O`: Verwendet die letzte Komponente der URL als Dateiname
- `-s`: Stiller Modus (keine Fortschrittsanzeige)
- `-v`: Verbose-Modus (zeigt detailliert die Kommunikation)

[EC] Laden Sie die Datei `https://httpbin.org/robots.txt` herunter 
und verwenden Sie den ursprünglichen Dateinamen für das Speichern der Antwort.

[EC] Führen Sie den gleichen Download im verbose-Modus durch, 
um die HTTP-Kommunikation zu analysieren:

<!-- time estimate: 20 min -->


### Headers und Authentifizierung

Für erweiterte HTTP-Kommunikation sind oft Headers und Authentifizierung relevant:

- `-H "Header: Value"`: Custom Headers setzen
- `-u username:password`: HTTP Basic Authentication
- `-I`: Nur Response-Headers abrufen (`HEAD`-Request)
- `-L`: Automatisches Verfolgen von Redirects

Optional: Weitere Authentifizierungsmethoden unter:
[Authentication with curl](https://everything.curl.dev/http/auth)

[EC] Rufen Sie nur die HTTP-Headers einer Webseite `https://httpbin.org/status/200` ab.

[EC] Testen Sie einen Request mit Custom-Headers `Accept: application/json` 
und `User-Agent: MyCustomAgent/1.0`.


### Erweiterte Funktionen: Cookies und Sessions

curl kann Cookies verwalten und Sessions aufrechterhalten:

- `-c mycookies.txt`: Cookies in Datei speichern
- `-b mycookies.txt`: Gespeicherte Cookies verwenden
- `-b "mycookie=myvalue"`: Einzelne Cookies direkt setzen

[EC] Speichern Sie das Cookie `mysession=abc123` in der Datei `mycookies.txt`. 
Verwenden Sie dazu den Endpunkt `/cookies/set/mysession/abc123` von `https://httpbin.org`.

[EC] Senden Sie das gespeicherte Cookie aus `mycookies.txt` an `https://httpbin.org/cookies`.  

<!-- time estimate: 15 min -->


### Datei-Upload und Formulare

Für Datei-Uploads verwendet curl die Codierung `multipart/form-data`:

- `-F "field=value"`: Formularfeld setzen
- `-F "file=@myfilename"`: Datei hochladen
- `--form-string "field=value"`: String-Feld ohne Interpretation

[EC] Erstellen Sie eine Datei `mytestfile.txt` mit einem kurzen Text `Testdatei für curl Upload`
und laden Sie sie anschließend mit curl sowie dem Feld `mydescription=Test Upload` 
nach `https://httpbin.org/post` hoch.

[EQ] In welchen Situationen würden Sie curl gegenüber einem grafischen HTTP-Client 
oder einem Browser bevorzugen? Nennen Sie zwei Fälle.

<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::program,trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll

[PROT::ALT:curl.prot]

### Markdown

[INCLUDE::ALT:curl.md]
[ENDINSTRUCTOR]