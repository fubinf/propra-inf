title: Linux curl Kommando für Datenübertragung
stage: draft
timevalue: 2.0
difficulty: 2
assumes: http-GET, http-POST
---

[SECTION::goal::experience]
Ich kann das curl-Kommando für verschiedene Netzwerk-Datenübertragungen verwenden und 
verstehe die wichtigsten Optionen für HTTP-Requests, Datei-Downloads und API-Interaktionen.
[ENDSECTION]

[SECTION::background::default]
In der modernen Softwareentwicklung und Systemadministration ist die Kommunikation mit 
Webservern und APIs alltäglich geworden. 
Das curl-Kommando ist ein unverzichtbares Werkzeug für diese, 
da es eine einfache und mächtige Möglichkeit bietet, 
Daten über verschiedene Netzwerkprotokolle zu übertragen.
Von einfachen Webseiten-Abfragen bis hin zu komplexen API-Interaktionen 
ermöglicht curl präzise Kontrolle über HTTP-Requests direkt von der Kommandozeile aus.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist curl und warum ist es wichtig?

curl (Client URL) ist ein Kommandozeilen-Tool zur Datenübertragung, 
das in praktisch allen Linux-Distributionen verfügbar ist. 
Es unterstützt zahlreiche Protokolle wie HTTP, HTTPS, FTP, SFTP und viele andere.

Die Hauptvorteile von curl:

- **Vielseitigkeit**: Unterstützt fast alle gängigen Netzwerkprotokolle
- **Automatisierung**: Perfekt für Skripte und automatisierte Aufgaben geeignet
- **Präzision**: Vollständige Kontrolle über Request-Headers, Methoden und Daten
- **Plattformunabhängigkeit**: Funktioniert auf Linux, macOS und Windows

(Optional) Für eine grundlegende Einführung lesen Sie bitte:
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

[EC] Speichern Sie die Ausgabe einer Webseite in eine Datei:

```bash
curl -o myoutput.html https://httpbin.org/html
```

Überprüfen Sie anschließend den Inhalt der erstellten Datei mit `cat myoutput.html`.

### HTTP-Methoden und Request-Steuerung

curl unterstützt alle gängigen HTTP-Methoden. 
Die wichtigsten Optionen für Request-Kontrolle:

- `-X METHOD`: Spezifiziert die HTTP-Methode (GET, POST, PUT, DELETE, etc.)
- `-d "data"`: Sendet POST-Daten
- `-H "Header: Value"`: Fügt Custom-Headers hinzu
- `-G`: Konvertiert POST-Daten zu GET-Parametern

(Optional) Für detaillierte HTTP-Methoden-Referenz siehe:
[HTTP Methods with curl](https://everything.curl.dev/http/methods)

[EC] Führen Sie einen POST-Request mit Formulardaten aus:

```bash
curl -X POST -d "myname=Student&myage=25" https://httpbin.org/post
```

[EC] Senden Sie JSON-Daten mit entsprechendem Content-Type-Header:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"myname":"TestUser","myemail":"test@example.com"}' \
https://httpbin.org/post
```

### Datei-Downloads und Output-Kontrolle

curl bietet verschiedene Möglichkeiten, die Ausgabe zu steuern:

- `-o myfilename`: Speichert Output unter angegebenem Namen
- `-O`: Verwendet den ursprünglichen Dateinamen der URL
- `-s`: Stiller Modus (keine Fortschrittsanzeige)
- `-v`: Verbose-Modus (zeigt detaillierte Kommunikation)

[EC] Laden Sie eine Datei herunter und verwenden Sie den ursprünglichen Dateinamen:

```bash
curl -O https://httpbin.org/robots.txt
```

[EC] Führen Sie den gleichen Download im verbose-Modus durch, 
um die HTTP-Kommunikation zu analysieren:

```bash
curl -v -O https://httpbin.org/robots.txt
```

Dokumentieren Sie die wichtigsten Informationen aus der verbose-Ausgabe 
(Request-Headers, Response-Headers, Status-Code).

### Headers und Authentifizierung

Für erweiterte HTTP-Kommunikation sind Headers und Authentifizierung essentiell:

- `-H "Header: Value"`: Custom Headers setzen
- `-u username:password`: HTTP Basic Authentication
- `-I`: Nur Response-Headers abrufen (HEAD-Request)
- `-L`: Automatisches Folgen von Redirects

(Optional) Weitere Authentifizierungsmethoden unter:
[Authentication with curl](https://everything.curl.dev/http/auth)

[EC] Rufen Sie nur die HTTP-Headers einer Webseite ab:

```bash
curl -I https://httpbin.org/status/200
```

[EC] Testen Sie einen Request mit Custom-Headers:

```bash
curl -H "User-Agent: MyCustomAgent/1.0" \
-H "Accept: application/json" \
https://httpbin.org/headers
```

### Erweiterte Funktionen: Cookies und Sessions

curl kann Cookies verwalten und Sessions aufrechterhalten:

- `-c mycookies.txt`: Cookies in Datei speichern
- `-b mycookies.txt`: Gespeicherte Cookies verwenden
- `-b "mycookie=myvalue"`: Einzelne Cookies direkt setzen

[EC] Demonstrieren Sie Cookie-Handling:

```bash
curl -c mycookies.txt https://httpbin.org/cookies/set/mysession/abc123
curl -b mycookies.txt https://httpbin.org/cookies
```

Überprüfen Sie den Inhalt der Cookie-Datei mit `cat mycookies.txt`.

### Datei-Upload und Formulare

Für Datei-Uploads verwendet curl die multipart/form-data-Codierung:

- `-F "field=value"`: Formularfeld setzen
- `-F "file=@myfilename"`: Datei hochladen
- `--form-string "field=value"`: String-Feld ohne Interpretation

[EC] Erstellen Sie eine Testdatei und laden Sie sie hoch:

```bash
echo "Dies ist meine Testdatei für curl Upload" > mytestfile.txt
curl -F "myfile=@mytestfile.txt" -F "mydescription=Test Upload" \
https://httpbin.org/post
```

### Performance-Analyse und Debugging

curl bietet mächtige Optionen für Performance-Messungen:

- `-w "format"`: Custom Output-Format für Timing-Informationen
- `--limit-rate 100K`: Übertragungsrate begrenzen
- `--connect-timeout 30`: Verbindungs-Timeout setzen

(Optional) Umfassende Performance-Analyse-Optionen:
[Performance measurement with curl](https://everything.curl.dev/cmdline/verbose/writeout)

[EC] Messen Sie die Performance einer HTTP-Anfrage:

```bash
curl -o /dev/null -s -w "Connect: %{time_connect}s\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\nSize: %{size_download} bytes\n" \
https://httpbin.org/delay/2
```

### Fehlerbehandlung und SSL

Bei HTTPS-Verbindungen können SSL-Probleme auftreten:

- `-k`: SSL-Zertifikatsprüfung ignorieren (nur für Tests!)
- `--cacert mycert.pem`: Spezifisches CA-Zertifikat verwenden
- `--cert myclient.crt`: Client-Zertifikat für Authentifizierung

[NOTICE]
Die Option `-k` sollte niemals in Produktionsumgebungen verwendet werden, 
da sie die Sicherheit der HTTPS-Verbindung kompromittiert.
[ENDNOTICE]

[EC] Testen Sie verschiedene HTTP-Status-Codes und deren Behandlung:

```bash
curl -v https://httpbin.org/status/404
curl -v https://httpbin.org/status/500
curl -L https://httpbin.org/redirect/3
```

[EQ] Welche Informationen können Sie aus den HTTP-Status-Codes ableiten? 
Warum ist die `-L` Option bei Redirects wichtig?

### Praktische Anwendungsszenarien

[EC] API-Testing: Simulieren Sie eine typische REST-API-Interaktion:

1. GET: Daten abrufen
2. POST: Neue Daten erstellen  
3. PUT: Daten aktualisieren
4. DELETE: Daten löschen

```bash
# GET - Daten abrufen
curl https://httpbin.org/get?myid=123

# POST - Daten erstellen
curl -X POST -H "Content-Type: application/json" \
-d '{"myname":"NewUser","myemail":"new@test.com"}' \
https://httpbin.org/post

# PUT - Daten aktualisieren  
curl -X PUT -H "Content-Type: application/json" \
-d '{"myid":123,"myname":"UpdatedUser"}' \
https://httpbin.org/put

# DELETE - Daten löschen
curl -X DELETE https://httpbin.org/delete?myid=123
```

[EC] Erstellen Sie ein einfaches Bash-Skript `myapi_test.sh`, 
das mehrere API-Calls nacheinander ausführt und die Ergebnisse in separate Dateien speichert.

[EQ] In welchen Situationen würden Sie curl gegenüber einem grafischen HTTP-Client 
oder einem Browser bevorzugen? Nennen Sie mindestens drei konkrete Anwendungsfälle.

[ENDSECTION]

[SECTION::submission::program,trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
Geben Sie auch alle erstellten Dateien (myoutput.html, mytestfile.txt, mycookies.txt, myapi_test.sh) ab.

[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::curl ist vielseitig aber Details sind wichtig]

### Erwartete Dateien

Die Studierenden sollten folgende Dateien erstellen:

- `myoutput.html` - Gespeicherte HTML-Ausgabe
- `mytestfile.txt` - Testdatei für Upload
- `mycookies.txt` - Cookie-Datei  
- `myapi_test.sh` - Bash-Skript für API-Tests

### Kommandoprotokoll

Das Protokoll sollte alle curl-Befehle mit deren Ausgaben enthalten.
Besonders wichtig sind die verbose-Ausgaben (-v) zur Analyse der HTTP-Kommunikation.

### Häufige Probleme

- Vergessene Anführungszeichen bei JSON-Daten
- Falsche Content-Type-Headers
- Nicht-escaped Sonderzeichen in URLs
- Verwechslung von -o und -O Optionen

### Bewertungskriterien

- Korrekte Ausführung aller curl-Kommandos
- Verständnis der verschiedenen HTTP-Methoden
- Angemessene Verwendung von Headers und Optionen
- Qualität des API-Test-Skripts
- Reflexion über Anwendungsszenarien

[INCLUDE::ALT:curl.md]

### Kommandoprotokoll

Sollte netcat-Befehle enthalten und die entsprechenden Responses zeigen.
[PROT::ALT:curl.prot]

[ENDINSTRUCTOR]