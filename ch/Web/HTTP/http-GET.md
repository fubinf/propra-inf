title: "HTTP GET: Abrufen von Ressourcen (request, response, status codes)" 
stage: beta
timevalue: 1.0
difficulty: 2
explains: HTTP-Statuscode
assumes: redirect
---

[SECTION::goal::idea,trial]

Ich verstehe Aufbau und Bedeutung einer GET-Anfrage und -Antwort in HTTP.

[ENDSECTION]

[SECTION::background::default]

Jede Stunde passieren Milliarden von Abrufen von Webservern.
Fast alle diese Abrufe benutzen das _Verb_ "GET".
Diese superwichtige Säule der praktischen Informatik sollte jede_r verstehen,
der technisch mit dem Web zu tun hat.

[ENDSECTION]

[SECTION::instructions::loose]

### Orientieren

- HTTP basiert auf zeilenweise strukturiertem Text und ist deshalb für Menschen leicht lesbar;
  eine sehr hilfreiche Eigenschaft.
- Es basiert ferner auf einzelnen Paaren aus Anfrage (_request_) eines Klienten (_client_)
  und zugehöriger Antwort (_response_) eines Servers.
  "Einzeln" heißt, die Paare haben miteinander aus Sicht von HTTP nichts zu tun,
  das Protokoll verwaltet also keinen Zustand einer längerlebigen Verbindung ("zustandsloses Protokoll").
  (Achtung: Mit dem _keep-alive_ Mechanismus kann "untendrunter" die für HTTP benutzte TCP-Verbindung
  sehr wohl über mehrere Requests hinweg aufrechterhalten werden, um Aufwand zu sparen.)
- Sowohl Request als auch Response bestehen aus Kopfzeilen (_headers_) und einem Rumpf (_body_).

So weit, so simpel. Allerdings gibt es dahinter jede Menge Einzelheiten:
Lesen Sie auf der
[MDN-Seite "HTTP"](https://developer.mozilla.org/en-US/docs/Web/HTTP)
die Einleitung (bis vor "HTTP Guides")
und überfliegen Sie den Rest: 
Verständliches verstehen, unverständliches als Stichwort zur Kenntnis nehmen.
Links brauchen Sie dabei auf keinen Fall zu verfolgen.

[EQ] Was hat Sie von diesem Inhalt am meisten überrascht?


### "GET": Eine Webseite abrufen

Nun arbeiten wir darauf zu, eine handgeschriebene Anfrage an einen Webserver durchzuführen, 
um HTTP gewissermaßen persönlich zu erleben.

Verfolgen Sie auf obiger Seite den Link 
[HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
lesen Sie bis zum Link 
[Request headers](https://developer.mozilla.org/en-US/docs/Glossary/Request_header),
verfolgen Sie den
und lesen Sie bis vor "See also".  
Wir merken, dass es bei den Einzelheiten schnell recht kompliziert wird.
Viele der Unterscheidungen im Protokoll, z.B. zwischen "request headers", 
"representation headers" und "simple headers"
sind in der Praxis oft nicht wichtig und werden deshalb im Sprachgebrauch oft auch nicht gemacht.

Manchmal sind sie aber doch wichtig, sodass man zumindest wissen sollte, dass man
ungenau redet und ein paar der detaillierteren Begriffe zumindest _kennen_ sollte, um
im Bedarfsfall zu merken, wenn genaueres Hinsehen nötig ist.

Lesen Sie nun auf der Seite 
[GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
den Aufbau eines HTTP-GET-Requests nach.

[EQ] Verstehen Sie die Eigenschaften "safe" und "idempotent" von GET.
Sind diese unabhängig voneinander oder impliziert eine die andere (und in welche Richtung)?

[ER] Schreiben Sie den Text für einen minimalen GET-Request auf die Seite
[HTTP/index.html]()
des ProPra in eine Datei `HTTP-GET-request.crlf`.
Ein minimaler GET-Request muss als Header einzig `Host:` enthalten.
Die Zeilen müssen (das gilt generell im Header-Bereich von HTTP-Requests und -Responses)
mit CRLF getrennt sein, nicht nur mit LF wie sonst auf Unix üblich.
CR hat Code 13 (Ctrl-M), LF had Code 10 (Ctrl-J).
Mit dem nano-Editor kann man
[Steuerzeichen mittels Alt-V eingeben](https://www.nano-editor.org/dist/v5/cheatsheet.html).

[EQ] Betrachten Sie [RFC 2616](https://www.rfc-editor.org/rfc/rfc2616),
den Standard, der HTTP 1.1 beschreibt.
Der Standard ist die definitive Quelle für alle Fragen über HTTP in der Theorie
(in der Praxis kommen regelmäßig noch ein paar Aspekte hinzu).
Finden Sie per Inhaltsverzeichnis und Link-Verfolgung die Stelle,
wo die Verbindlichkeit von `Host:` erklärt ist.
Zitieren Sie den entsprechenden Satz und nennen Sie den Abschnitt, wo er steht.

[NOTICE]
Vorsicht bei den Standards: 
RFC 2616 (von 1999) ist für unsere Anfängerzwecke in dieser Aufgabe gut geeignet,
aber er ist nicht die aktuelle Fassung des Standards zu HTTP 1.1,
denn das ist
[RFC 7230](https://www.rfc-editor.org/rfc/rfc7230) von 2014.
Ups, nein auch nicht. Sondern 
[RFC 9112](https://www.rfc-editor.org/rfc/rfc9112) von 2022.
Außerdem gibt es inzwischen auch HTTP 2 und HTTP 3;
trotzdem ist für viele Programmierzwecke weiterhin HTTP 1.1 die richtige Basis.

Um in so einem Dickicht nicht den Überblick zu verlieren, ist sehr oft
Wikipedia ein guter Ausgangspunkt: 
[HREF::https://en.wikipedia.org/wiki/HTTP]
[ENDNOTICE]

[EC] Installieren Sie nötigenfalls das apt-Paket `netcat`.  
Zeigen Sie die vorbereitete Eingabe vor (`cat HTTP-GET-request.crlf`).  
Führen Sie Ihre Anfrage aus: 
`nc name.des.webservers 80 <HTTP-GET-request.crlf`.  
`nc` sendet Eingabedaten unverändert an einen Port eines anderen Rechners
und zeigt empfangene Daten auf der Standardausgabe an.


### GET-Response Statuscode

Sie sollten also nun die HTTP-Response sehen können.
Die erste Zeile enthält den Statuscode.
Sie sollten einen der folgenden erhalten haben: 200, 301, 302, 400, 403, 404.

[Lesen Sie nach](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), was diese Codes bedeuten,
denn die sind äußerst wichtig bei der Nutzung von HTTP.
Dann erst geht es bitte hier weiter:

- Bei Statuscode 200 waren Sie erfolgreich.
- Bei 301 oder 302 befolgen Sie bitte den Hinweis aus dem Rumpf.  
  Machen Sie einen entsprechenen neuen Request.  
  Haben Sie keinen solchen Code erhalten, rufen Sie einen Shortlink auf, um das zu erleben,
  z.B. [HREF::http://tinyurl.com/myalias]; bei denen ist Umlenken der Job.
- Bei 400 war der Request in der Eingabdatei nicht wohlgeformt.  
  Korrigieren Sie das und versuchen Sie erneut (Haben Sie CRLF benutzt?)
- Bei 403 ist vermutlich ein Login nötig; das lösen wir hier nicht.  
  Rufen Sie ersatzweise irgendeine andere Webseite ab, nichts vom ProPra.
- Bei 404 ist die Adresse der Ressource in der Eingabedatei falsch.  
  Korrigieren Sie das und versuchen Sie erneut.

Diese Korrekturschritte gehören ggf. mit ins Kommandoprotokoll.


### GET-Response Content-Type

Unter dem Statuscode folgen in der Antwort die Response-Header.
Der weitaus wichtigste davon ist `Content-Type`,
der den sogenannten _media type_ oder _MIME type_ angibt.

Lesen Sie den oberen Teil der Seite 
[MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types)
bis vor "Multipart types".

[EQ] Welche MIME-Types bekommt man korrekterweise, wenn man folgende Sorten
von Ressource abruft: Eine PDF-Datei; ein JPG-Bild; eine MS-Word-Datei?

[EQ] Lesen Sie direkt im 
[HTTP-Standard RFC 2616](https://www.rfc-editor.org/rfc/rfc2616) nach,
um folgende Frage zu beantworten:
Warum gibt es die Angabe `charset` im `Content-Type`-Header
(`Content-Type: text/html; charset=utf-8`),
wenn es doch einen separaten Header `Content-Encoding` gibt?

[ENDSECTION]

[SECTION::submission::information,snippet,trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
Geben Sie auch die Datei `HTTP-GET-request.crlf` mit ab.

[ENDSECTION]

[INSTRUCTOR::HTTP scheint einfach, ist aber umfangreich und z.T. subtil]

### Eingabedatei

Die Eingabedatei sieht z.B. aus wie
[TREEREF::HTTP-GET-request.crlf].
Dabei MÜSSEN die Zeilenenden unbedingt CR LF sein!
(LF funktioniert mit einem bestimmten Server vielleicht, mit anderen aber nicht.)

Kontrolle mit `od -a HTTP-GET-request.crlf`.


### Kommandoprotokoll

Das Kommandoprotokoll kann im Detail natürlich sehr abweichen (vor allem bei Fehlversuchen), 
sieht aber im einfachen Fall ungefähr so aus:
[PROT::ALT:http-GET.prot]

### Fragen

[INCLUDE::ALT:http-GET.md]

[ENDINSTRUCTOR]
