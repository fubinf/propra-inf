title: "HTTP Chat - Persistierung"
stage: draft
timevalue: 4
difficulty: 3
requires: go-http-chat-core
---

[SECTION::goal::experience,product]

- Ich habe eine lokale Datenbank für die Chat-Anwendung in Go angelegt, mithilfe dessen ich die Funktionalität erweitern 
konnte.

[ENDSECTION]

[SECTION::background::default]

Der HTTP-Chat, den Sie in [PARTREF::go-http-chat-core] implementiert haben, ist aktuell nur noch Laufzeit-Chat - alle 
Ereignisse "leben" nur im Arbeitsspeicher. Sobald der Prozess beendet ist, gehen die Daten verloren. Das wollen wir in 
dieser Aufgabe verbessern.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorwort

Es gibt eine Menge von Datenbank-Technologien - zu den beliebtesten gehören u. a. PostgreSQL, MySQL, MongoDB und SQLite.
Wir fokussieren uns auf SQLite, da diese Datenbank dank der dateiorientierten Funktionsweise sehr simpel und performant 
ist. Dies erlaubt außerdem für ein schnelles Entwickeln und ist für ein extensives Testen geeignet.

Um die Anwendung plattformunabhängig zu halten, verzichten wir auf jegliche Abhängigkeiten zu C. Ein beliebter SQLite
Treiber für Go ist [modernc.org/sqlite](https://pkg.go.dev/modernc.org/sqlite?utm_source=godoc).

Wir schreiben aber keine SQL-Anfragen selber: Das macht für uns ein ORM (Object-Relational Mapping). Wenn Sie 
zukünftig mit Go arbeiten werden, haben Sie eine größere Chance auf ein solches ORM zu stoßen als auf die reine SQL.
ORM unserer Wahl ist [GORM](https://gorm.io/) - dies ist ein beliebtes Tool, welches relativ einfach zu benutzen ist 
und eine Menge von Features anbietet. 

### Arbeitsplan

In dieser Aufgabe implementieren Sie eine lokale Datenbank für den Client und eine für den Server.

#### Was soll gespeichert werden?

- Server
    * Benutzernamen und Auth Tokens (1) beziehungsweise Passwörter (2) von den Clients (kommt darauf an, ob Sie die 
[PARTREF::go-http-chat-security] Aufgabe bereits abgeschlossen haben);
    * Einloggen-Ereignisse;
    * Wer mit wem kommuniziert hat.
- Client
    * Chat-Verläufe mit verschiedenen anderen Benutzer_innen;
    * Nachrichten, die nicht gesendet werden konnten;

#### Wie werden diese Daten benutzt?

- Server
    * "einloggen" statt "registrieren" - der Benutzer wird nur dann eingeloggt, wenn das Passwort bzw. der Token für den 
    Benutzernamen mit dem Passwort/Token aus der Datenbank übereinstimmt;
    * Live Logging von allen Ereignissen - Ein- und Ausloggen sowie 
    "es wurde eine Nachricht von X an Y gesendet"-Ereignisse werden in einer Datenbank gespeichert.
- Client
    * Chat-Verlauf ist nun sichtbar;
    * Reihenfolge von Gesprächspartnern, basierend auf dem Zeitpunkt des Empfangs bzw. Absendens der letzten Nachricht;
    * Textsuche über dem Chat-Verlauf;
    * Nachrichtensuche basierend auf dem Zeitstempel.

Wir fangen mit dem Server an.

### Neue Funktionalität: Server

#### Datenbank einrichten

1. Legen Sie unter `server` ein neues Verzeichnis `database` an mit einer `database.go` Datei und einem weiteren 
   Verzeichnis `model`. Definieren Sie Strukturen für `User`, `Login` und `Message`. `User` enthält Information über 
   Benutzer, `Login` - über Einloggen-Ereignisse und `Message` - über gesendete Nachrichten. Benutzen Sie dabei 
   [gorm.Model](https://pkg.go.dev/gorm.io/gorm@v1.25.12#Model) und Struct Embedding.
2. Deklarieren Sie in der Datei `database.go` eine Struktur `DB` und eine Funktion `Init() *DB`. Falls Sie schon
   einige Erfahrungen mit objektorientierter Programmierung gemacht haben, können Sie diese Funktion als Konstruktor 
   betrachten. [Hier](https://gorm.io/docs/) können Sie nachschlagen, wie man eine Datenbank einrichtet.  

#### Einloggen statt registrieren

1. Implementieren Sie eine simple API, die mit `User` Tabelle interagiert. Das sind prinzipiell Methoden auf 
   `DB`, wie beispielsweise `func (db *DB) InsertUser(user model.User) error` und 
   `func (db *DB) GetUserByName(name string) *model.User`. Sie dürfen selber entscheiden, welche Getter-Methoden Sie 
    brauchen.
    Passen Sie auf den Unterschied zwischen `.First()` und `.Find()`: Falls keine Einträge gefunden wurden, können Sie 
    unter `.First().Error` herausfinden, warum. `.Find().Error` bleibt aber `nil`. Wir bevorzugen hier alles Explizite 
    allem Impliziten und empfehlen ausschließlich mit `.First()` zu arbeiten, wenn Sie genau einen Rückgabewert 
    erwarten.
2. Passen Sie nun die Anmelde-Logik an: Falls der Benutzername schon in der Datenbank ist, muss auch das Passwort / der 
   Token übereinstimmen. Sonst fügen Sie einen Benutzer in die Datenbank ein. (Bonus: eine aussagekräftige Fehlermeldung 
   an Client senden)

#### Logging

1. Implementieren Sie eine create/retrieve API für `Login` Ereignis.
[ENDSECTION]