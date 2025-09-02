title: HTTP Zustandslosigkeit und Cookies
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: http-GET
---

[SECTION::goal::idea]
Ich verstehe das Konzept der Zustandslosigkeit in HTTP und kann erklären, 
Sessions realisiert werden, um trotzdem zustandsbehaftetes Verhalten zu erlauben.
[ENDSECTION]

[SECTION::background::default]
HTTP ist von Natur aus ein zustandsloses Protokoll, das bedeutet, 
dass jede Anfrage unabhängig behandelt wird und nichts von ggf. vorangegangenen Anfragen weiß. 
Das ist zwar für die Server effizient (weil sie keinen Zustand speichern müssen),
bildet aber für viele Anwendungen keine ausreichende Grundlage.
Wie also bekommt man mittels HTTP Sitzungen mit Zustand hin?
[ENDSECTION]

[SECTION::instructions::detailed]

### Was bedeutet "zustandslos" bei Protokollen?

Ein Protokoll gilt als **zustandslos** (stateless), wenn es keine Informationen über 
den Zustand oder die Historie der Kommunikation zwischen den beteiligten Parteien speichert. 
Jede Nachricht wird unabhängig und getrennt von vorherigen oder nachfolgenden Nachrichten behandelt.

Im Gegensatz dazu ist ein Protokoll **zustandsbehaftet** (stateful), 
wenn es den Zustand oder die Historie der Kommunikation verfolgt. 
Jede Nachricht ist dann mit vorherigen oder nachfolgenden Nachrichten verbunden.

**Zustandsbehaftete Kommunikation:**

Mensch: "Hallo, ich bin user123. Mein Passwort ist pw567."  
Server: "Herzlich willkommen."  
Mensch: "Was ist in meinem Warenkorb?"
Server: "Artikel A, B und C."

**Zustandslose Kommunikation:**

Mensch: "Hallo, ich bin user123. Mein Passwort ist pw567."  
Server: "Herzlich willkommen."  
Mensch: "Was ist in meinem Warenkorb?"
Server: "Welcher Warenkorb?"

Ohne Zustand fehlt dem Server bei Anfrage 2 die Information, ob jemand angemeldet ist, oder wer.

(Optional) Zur Vertiefung lesen Sie bitte:
[HTTP als zustandsloses Protokoll](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http-is-stateless-but-not-sessionless)

<!-- time estimate: 15 min -->

### Warum ist HTTP zustandslos designed?

HTTP wurde bewusst als zustandsloses Protokoll entworfen, 
da dies verschiedene Vorteile gegenüber zustandsbehafteten Protokollen bietet:

- **Einfachheit**: Zustandslose Protokolle sind einfacher zu implementieren und zu warten, 
  da keine Informationen zwischen Anfragen gespeichert werden müssen
- **Skalierbarkeit**: Keine Synchronisation zwischen Clients und Servern erforderlich; 
  Server können mehr gleichzeitige Anfragen bearbeiten
- **Zuverlässigkeit**: Unabhängigkeit von vorherigen Nachrichten macht das System robuster 
  gegen Ausfälle und Unterbrechungen

[EQ] Recherchieren Sie und erklären Sie für folgende Anwendungsfälle,
wie die Zustandslosigkeit von HTTP entscheidend für die Skalierbarkeit ist:
Content Delivery Networks (CDNs); Lastverteilung (load balancing) bei eCommerce-Anbietern.

<!-- time estimate: 15 min -->

Na gut, aber aus Anwendungssicht braucht man oft einen Zustand.
Wie funktioniert das?



### Wie funktionieren Cookies?

Cookies sind kleine Datenstücke, die vom Server an den Browser des Benutzers gesendet 
und dort gespeichert werden. 
Bei nachfolgenden Anfragen sendet der Browser diese Cookies zurück an den Server.

Der grundlegende Ablauf sieht folgendermaßen aus:

1. Client sendet eine HTTP-Anfrage ohne Cookie
2. Server antwortet mit `Set-Cookie` Header
3. Browser speichert das Cookie
4. Bei weiteren Anfragen sendet Browser das Cookie im `Cookie` Header mit

Beispiel eines `Set-Cookie` Headers:
```http
Set-Cookie: session_id=abc123; Expires=Thu, 31 Oct 2024 07:28:00 GMT
```

Beispiel einer nachfolgenden Anfrage mit Cookie:
```http
GET /profile HTTP/1.1
Host: www.example.com
Cookie: session_id=abc123
```

(Optional) Detaillierte Informationen zu Cookie-Mechanismen unter:
[Using HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

<!-- time estimate: 10 min -->

### Sessions und Sitzungsverwaltung

Sessions sind temporäre Speicherbereiche, die auf dem Server für jeden Benutzer erstellt werden. 
Sessions enthalten Informationen über die Benutzeraktivität und den aktuellen Zustand.

Cookies und Sessions arbeiten zusammen:

- Cookie enthält eine Session-ID (eindeutiger Bezeichner)
- Server verwendet Session-ID, um Benutzerdaten aus dem Session-Speicher abzurufen
- Session-Daten bleiben auf dem Server, nur die ID wird zwischen Client und Server übertragen

Dies ermöglicht es, HTTP effektiv zustandsbehaftet zu machen, 
obwohl das Protokoll selbst zustandslos bleibt.
Der Server kann den Client durch die Session-ID identifizieren und 
entsprechend personalisierte Antworten senden.

[EQ] Erklären Sie den Unterschied zwischen Cookies und Sessions. 
Warum werden beide Mechanismen oft zusammen verwendet?

<!-- time estimate: 10 min -->

### Hauptverwendungszwecke von Cookies

Cookies werden hauptsächlich für drei Zwecke eingesetzt:

1. **Sitzungsverwaltung**: Anmeldestatus, Warenkorbinhalte, Spielstände oder andere 
   benutzerbezogene Details, die der Server sich merken muss
2. **Personalisierung**: Benutzereinstellungen wie Sprache und Design-Themes  
3. **Tracking**: Aufzeichnung und Analyse von Benutzerverhalten

Moderne Webanwendungen nutzen auch alternative Speichermechanismen wie 
`localStorage` und `sessionStorage` für clientseitige Datenspeicherung, 
da diese nicht bei jeder Anfrage übertragen werden und größere Datenmengen speichern können.

[EQ] Ein Online-Shop möchte folgende Funktionen implementieren:

- Benutzer soll angemeldet bleiben
- Warenkorbinhalte sollen gespeichert werden  
- Bevorzugte Sprache soll gesetzt werden
- Besuchsstatistiken sollen erfasst werden

Erklären Sie, welche dieser Funktionen am besten durch Cookies, Sessions oder 
alternative Speichermechanismen umgesetzt werden sollten und begründen Sie Ihre Entscheidung.

<!-- time estimate: 15 min -->

### Cookie-Attribute und Lebensdauer

Cookies können verschiedene Attribute haben, die ihr Verhalten steuern:

- **Expires/Max-Age**: Bestimmt die Lebensdauer des Cookies, `Max-Age` ist die Anzahl der Sekunden, 
  die das Cookie gültig ist
- **Domain/Path**: Bestimmt den Gültigkeitsbereich (für welche Domains/Pfade gilt das Cookie)
- **Secure**: Cookie wird nur über HTTPS übertragen
- **HttpOnly**: Cookie ist nur für HTTP-Anfragen zugänglich (nicht für JavaScript)

**Permanente Cookies** haben ein Ablaufdatum und bleiben bis zu diesem Zeitpunkt gespeichert:
```http
Set-Cookie: user_pref=dark_mode; Expires=Thu, 31 Oct 2025 07:28:00 GMT
```

**Session-Cookies** haben kein Ablaufdatum und werden beim Schließen des Browsers gelöscht:
```http
Set-Cookie: temp_data=value123
```

(Optional) Umfassende Cookie-Attribute-Referenz:
[Cookie Attributes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#attributes)

[EQ] Eine Website möchte sowohl Login-Informationen für 30 Tage speichern 
als auch temporäre Warenkorbdaten nur für die aktuelle Browsersitzung. 
Wie würden die entsprechenden `Set-Cookie` Header aussehen?

<!-- time estimate: 15 min -->

### Sicherheits- und Datenschutzaspekte

Cookies bringen wichtige Sicherheits- und Datenschutzüberlegungen mit sich:

**Sicherheitsaspekte:**

- **Session Fixation**: Angreifer können Session-IDs manipulieren oder vorhersagen
- **Session Hijacking**: Angreifer übernehmen eine bestehende Sitzung, 
indem sie gültige Session-IDs abfangen oder stehlen
- **Cross-Site Scripting (XSS)**: Malicious Scripts können Cookies auslesen und stehlen  
- **Cross-Site Request Forgery (CSRF)**: Unerwünschte Aktionen durch gefälschte Anfragen

**Datenschutzaspekte:**

- **Tracking**: Cookies ermöglichen Benutzerverfolg über mehrere Websites hinweg
- **Datenschutz**: Nutzer haben Recht auf Kontrolle über ihre Daten (DSGVO)

Moderne Browser implementieren verschiedene Schutzmaßnahmen und 
Datenschutzrichtlinien wie die DSGVO regulieren den Cookie-Einsatz.

[EQ] Erklären Sie, warum das `HttpOnly`-Attribut bei Session-Cookies wichtig für die Sicherheit ist 
und welche Angriffe dadurch verhindert werden können.

[EQ] Eine Website setzt sowohl notwendige Session-Cookies 
als auch Tracking-Cookies für Werbezwecke ein. 
Recherchieren Sie, 
welche technischen Unterschiede gibt es bei der Verwendung dieser beiden Cookie-Arten?
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
Die Studierenden sollen ein grundlegendes Verständnis für HTTP-Zustandslosigkeit entwickeln 
und verstehen, wie Cookies und Sessions diese Limitation überwinden. 
Wichtige Konzepte sind die Vor-/Nachteile der Zustandslosigkeit, 
der Unterschied zwischen Cookies und Sessions, sowie grundlegende Sicherheitsaspekte.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
```