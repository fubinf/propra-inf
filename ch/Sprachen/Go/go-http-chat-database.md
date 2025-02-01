title: "HTTP Chat - Persistierung"
stage: draft
timevalue: 4
difficulty: 3
requires: go-http-chat-core
---

[SECTION::goal::experience,product]

- Ich habe eine lokale Datenbank für die Chat-Anwendung angelegt, mithilfe dessen ich die Funktionalität erweitern 
konnte.

[ENDSECTION]

[SECTION::background::default]

Der HTTP-Chat, den Sie in [PARTREF::go-http-chat-core] implementiert haben, ist aktuell nur noch Laufzeit-Chat - alle Ereignisse
"leben" nur im Arbeitsspeicher. Sobald der Prozess beendet ist, gehen die Daten verloren. Das wollen wir in dieser 
Aufgabe verbessern.

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

Im Rahmen dieser Aufgabe implementieren Sie eine lokale Datenbank, um folgende Daten zu speichern:

- Server
    * Benutzernamen und Auth Tokens (1) beziehungsweise Passwörter (2) von den Clients (kommt darauf an, ob Sie die 
[PARTREF::go-http-chat-security] Aufgabe bereits abgeschlossen haben)
    * Einloggen-Ereignisse
- Client
    * Chat-Verläufe mit verschiedenen anderen Benutzer_innen
    * Nachrichten, die nicht gesendet werden konnten

Dies ermöglicht neue Funktionalität, wie beispielsweise:
- Chat-Verlauf geht nicht verloren (offensichtlich)
- Gesprächspartner-Reihenfolge basierend auf dem Zeitpunkt des Empfangs bzw. Absendens der letzten Nachricht
- Textsuche im Chat
- Finde-Alle-an-dem-Tag-XYZ-gesendeten-Nachrichten
- und vieles weitere ...

[ENDSECTION]