title: "'requests': sehr einfach HTTP-Anfragen machen"
stage: beta
timevalue: 1.0
difficulty: 3
assumes: HTTP-GET, HTTP-POST, WebAPIs, pip, m_sys, m_json1
---

[SECTION::goal::trial]

Ich kann das Python-Paket `requests` für verschiedene Arten von HTTP-Anfragen verwenden.

[ENDSECTION]

[SECTION::background::default]

Da viele moderne Anwendungen auf externe Dienste angewiesen sind, die über [TERMREF::Web-API]
kommunizieren, ist das Beherrschen einer http-Bibliothek wichtig, mit der man solchen
externen Diensten Aufträge senden kann.
Es gibt in der Standardbibliothek dafür [http.client](https://docs.python.org/3/library/http.client.html),
aber das ist umständlich zu benutzen, weshalb die meisten Programme lieber
das _viel_ einfacher zu benutzende [`requests`](https://requests.readthedocs.io) verwenden.

[ENDSECTION]

[SECTION::instructions::loose]

Benutzen Sie bei Bedarf die [Dokumentation von `requests`](https://requests.readthedocs.io).

### Installation

- Installieren Sie `requests` mittels [PARTREF::pip].

### GET-Anfrage

[ER] Schreiben Sie in `m_requests.py` eine Routine `do_get(url: str, searchstring: str)`,
die folgendes tut:

- Einen GET-Request an den URL `url` senden und die Antwort auffangen.
- Den HTTP-Status ausgeben.
- Die Länge des Rumpfes der Antwort (und zwar gemessen in Zeichen, nicht Bytes, 
  der Rumpf also interpretiert als String, nicht als Bytefolge) 
  zusammen mit dem tatsächlich erhaltenen URL ausgeben.
  (Der ist nicht unbedingt identisch mit dem angefragten, denn `requests` folgt etwaigen Umlenkungen!)
- Die Header der Antwort ausgeben (einzeln formatiert). 
  Dabei Spezialheader (deren Name mit `'x-'` oder `'X-'` beginnt) weglassen.
- Im Rumpf nach dem `searchstring` suchen und dessen Position ermitteln (`str.find`)
  und dann 250 Zeichen ab dort vom Rumpf ausgeben. Andernfalls "((not found))" ausgeben.

[ER] Diese Routine von der Kommandozeile wie folgt aufrufbar machen:  
`python m_requests.py do_get https://requests.readthedocs.io human`

Das Ergebnis soll z.B. etwa so aussehen:
```
$ python m_requests.py do_get https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/chapter-Basis.html grundlegend
Status: 200
received 6779 characters for https://www.inf.fu-berlin.de/inst/ag-se/teaching/K-ProPra-2024-04/chapter-Basis.html
Encoding: ISO-8859-1
Headers:
   Date:        Fri, 25 Oct 2024 16:11:11 GMT
   Server:      Apache/2.4.62 (Debian)
   Last-Modified:       Wed, 14 Aug 2024 16:13:53 GMT
   ETag:        "1a7b-61fa7032eb356-gzip"
   Accept-Ranges:       bytes
   Vary:        Accept-Encoding
   Content-Encoding:    gzip
   Content-Length:      1904
   Content-Type:        text/html
   Keep-Alive:  timeout=5, max=100
   Connection:  Keep-Alive
search for 'grundlegend':
grundlegende ArbeitsfÃ¤higkeit
fÃ¼r das Programmierpraktikum herstellen:</p>
<ul>
<li>Arbeitsumgebung installieren (soweit nicht schon vorhanden):<ul>
<li>eine Unix-artige Kommandozeilen-Arbeitsumgebung</li>
<li>Python (das ist unsere Haupt-Programmi
```


### Encoding-Bestimmung

Wie man sieht, sind in der obigen Beispielausgabe die Wörter "Arbeitsfähigkeit" und "für" falsch kodiert.
Das liegt an der vom Server angenommenen Standardkodierung "ISO-8859-1";
richtig für diese Daten wäre "UTF-8".
`requests` löst das Problem meist automatisch, wenn eine Zusatzbibliothek installiert ist, wie
[in der Dokumentation bei "Encoding" beschrieben](https://requests.readthedocs.io/en/latest/user/advanced/#encodings).
Verstehen Sie das Phänomen, lesen Sie bei [pypi.org](https://pypi.org) den Zweck dieser
Bibliothek nach und installieren Sie sie bei sich nach.

Danach könnte die Ausgabe korrekt sein -- oder war es bei Ihnen ohnehin.
Oder auch beides nicht: im obigen Fall gilt nämlich die in der Dokumentation angesprochene 
Ausnahme, für die der Standard ausdrücklich "ISO-8859-1" vorschreibt und deshalb auch
die Bibliothek nicht hilft, sondern der Server müsste anders konfiguriert werden.
Das Nachinstallieren der Bibliothek ist trotzdem sinnvoll.

Explizites Nachinstallieren ist angebracht, auch wenn die Bibliothek schon vorhanden ist, 
damit sie selbständig installiert ist (nicht nur als Abhängigkeit von etwas anderem) 
und deshalb nicht irgendwann plötzlich verschwinden kann, wenn man eine andere Bibliothek deinstalliert
oder aktualisiert.

[EC] Vollziehen Sie den Aufruf des Formatbeispiels mit Ihrer eigenen Implementierung nach
und zwar für die Seite [HREF::chapter-Basis.html] in _Ihrem_ aktuellen ProPra.


### Server erkunden

Mit diesen simplen Ausgaben kann man eine Reihe interessanter Phänomene beobachten,
auch wenn man gar nicht erst versucht, alle exotischen Header zu verstehen,
sondern sich auf Gängiges konzentiert.  
Was ist jeweils das Bemerkenswerte an folgenden Fällen?:

[EQ] `python m_requests.py do_get https://community.unbounce.com unbounce`

[EQ] `python m_requests.py do_get https://amazon.de Amazon` im Gegensatz zu  
`python m_requests.py do_get https://amazon.de/laskdjfasdf Amazon` (nicht existente Seite)


### POST-Anfrage

[ER] Schreiben Sie in `m_requests.py` eine Routine `do_post(url: str, jsontext: str)`,
die folgendes tut:

- Einen POST-Request an den URL `url` senden, dabei den mit `json` geladenen `jsontext` als
  JSON-Parameter mitgeben und die Antwort auffangen.
- Den HTTP-Status ausgeben.
- Annehmen, dass die Antwort im JSON-Format kommt, dieses JSON dekodieren (das macht `requests` für Sie,
  bitte nicht selber tun) und sofort anschließend
  mit `json` in einen hübsch formatierten JSON-String serialisieren und diesen ausgeben.

[ER] Diese Routine von der Kommandozeile wie folgt aufrufbar machen:  
`python m_requests.py do_post  https://httpbin.org/anything '{"parameter1": "some value", "parameter2": 126}'`

Zum Testen können wir diesmal nicht irgendeinen Server benutzen, sondern brauchen einen,
der unseren speziellen Request auch akzeptiert.
`http.bin` ist bei obiger Aufrufform so einer, der dann die erhaltenen Daten (angereichert um andere)
geradewegs wieder zurückschickt -- und zwar im JSON-Format.

Das Ergebnis soll z.B. etwa so aussehen:
```
Status: 200
{
  "args": {},
  "data": "{\"parameter1\": \"some value\", \"parameter2\": 126}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "47",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-671bc83b-778cfd9847b00c835371ee9c"
  },
  "json": {
    "parameter1": "some value",
    "parameter2": 126
  },
  "method": "POST",
  "origin": "160.45.46.281",
  "url": "https://httpbin.org/anything"
}
```

[EC] `python m_requests.py do_post  https://httpbin.org/anything '{"a": "wer A sagt", "b": 255}'`

[ENDSECTION]

[SECTION::submission::information,snippet]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kurzer Blick auf den Code]

Wir interessieren uns nur sehr grob für die Antworten auf die Fragen
oder das Kommandoprotokoll (außer: sind die `X-...`-Header unterdrückt?)
und schauen lieber in den Code.

[EREFQ::1] Per 2024-11 setzt `community.unbounce.com` ein (allerdings kurzlebiges) Cookie,
obwohl das wegen der DSGVO eher nicht mehr erlaubt ist.

[EREFQ::2] per 2024-11 liefert `amazon.com` bei Abruf mit `requests` Status 503 (Service Unavailable),
obwohl die Seite natürlich tadellos funktioniert und auch tatsächlich korrekt ausgeliefert wird.
Das liegt am mitgeschickten Request-Header "User-Agent", der erkennen lässt, dass die Anfrage
nicht von einem Browser kommt: Amazon möchte keine Scraper und Crawler bedienen.

[PROT::ALT:m_requests.prot]

Möglicher Quellcode:

```python
[INCLUDE::ALT:m_requests.py]
```

[ENDINSTRUCTOR]
