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

Falls noch Fragen offen sind, hilft diese Ressource weiter:
[HTTP als zustandsloses Protokoll](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)

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



### Sitzungsverwaltung: URL-Rewriting und Cookies

Vorab: Zwei gängige Ansätze, um eine Sitzungskennung zwischen Client und Server zu transportieren:

- **URL-Rewriting**: Die Session-ID wird in die URL aufgenommen (Pfad oder Query), 
  z. B. `/shop;jsessionid=abc123` oder `/shop?sid=abc123`.  
- **Cookies (üblichere Variante)**: Die Session-ID wird als Cookie gespeichert und bei jeder Anfrage 
  automatisch mitgesendet.

Cookies sind kleine Datenstücke, die vom Server an den Browser gesendet 
und dort gespeichert werden. 
Bei nachfolgenden Anfragen sendet der Browser diese Cookies automatisch im `Cookie` Header zurück.

**Ablauf:**

1. Client sendet eine HTTP-Anfrage ohne Cookie  
2. Server antwortet mit `Set-Cookie` Header  
3. Browser speichert das Cookie  
4. Bei weiteren Anfragen sendet der Browser das Cookie mit  

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

**Vergleich**

- **Cookies**: Automatisch und konsistent vom Browser gehandhabt, keine sichtbare ID in der URL,
  kompatibler mit Caches und Links.  
  **Nachteile von Cookies**: Weniger transparent für Endnutzer; können für Angriffe wie CSRF 
  missbraucht werden (CSRF = Cross-Site Request Forgery, 
  dabei werden Benutzer ohne ihr Wissen zu Aktionen verleitet).
- **URL-Rewriting**: Funktioniert auch ohne Cookies, aber anfällig für Leaks und unpraktisch.  
  **Nachteile**: nicht benutzerfreundlich, sehr leicht unabsichtlich offenzulegen 
  (Copy & Paste, Bookmarks, Logs, Referer-Header), 
  erschwertes Caching, und potenziell fehleranfälliger.  

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

### Hauptverwendungszwecke und Lebensdauer von Cookies

Cookies werden im Wesentlichen für drei Zwecke eingesetzt:

- **Sitzungsverwaltung**: Anmeldestatus, Warenkorbinhalte, Spielstände oder 
  andere benutzerbezogene Details, die der Server sich merken muss.  
- **Personalisierung**: Benutzereinstellungen wie Sprache oder Design-Themes.  
- **Tracking**: Ebenfalls möglich, wird hier nur erwähnt und 
  in einer späteren Aufgabe gesondert behandelt.

Darüber hinaus spielt die Lebensdauer der Cookies eine Rolle:

- **Permanente Cookies** haben ein Ablaufdatum (z. B. über `Expires` oder `Max-Age`) 
  und bleiben bis dahin gespeichert.
```http
Set-Cookie: user_pref=dark_mode; Expires=Thu, 31 Oct 2025 07:28:00 GMT
```

- **Session-Cookies** haben kein Ablaufdatum und werden beim Schließen des Browsers gelöscht.
```http
Set-Cookie: temp_data=value123
```

Moderne Webanwendungen nutzen zudem alternative Speichermechanismen 
wie `localStorage` und `sessionStorage` für clientseitige Datenspeicherung, 
da diese nicht bei jeder Anfrage übertragen werden und größere Datenmengen speichern können.

[EQ] Ein Online-Shop möchte folgende Funktionen implementieren:

- Benutzer soll angemeldet bleiben
- Warenkorbinhalte sollen gespeichert werden  
- Bevorzugte Sprache soll gesetzt werden
- Besuchsstatistiken sollen erfasst werden

Erklären Sie, welche dieser Funktionen am besten durch Cookies, 
Sessions oder alternative Speichermechanismen umgesetzt werden sollten 
und begründen Sie Ihre Entscheidung.

[EQ] Eine Website möchte sowohl Login-Informationen für 30 Tage speichern 
als auch temporäre Warenkorbdaten nur für die aktuelle Browsersitzung. 
Wie würden die entsprechenden `Set-Cookie` Header aussehen?

<!-- time estimate: 15 min -->


[ENDSECTION]

[SECTION::submission::information]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
Die Studierenden sollen ein grundlegendes Verständnis für HTTP-Zustandslosigkeit entwickeln 
und verstehen, wie Cookies und Sessions diese Limitation überwinden. 
Wichtige Konzepte sind die Vor-/Nachteile der Zustandslosigkeit, 
der Unterschied zwischen Cookies und Sessions.

[INCLUDE::ALT:]

[ENDINSTRUCTOR]