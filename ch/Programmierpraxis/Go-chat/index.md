title: "Chat: Nachrichtenaustausch im Terminal"
stage: alpha
---
Jeder kennt WhatsApp, Telegram, Signal und sicherlich einige weitere Anwendungen,
die uns Austausch mit anderen Benutzern ermöglichen.

In dieser Aufgabengruppe implementieren Sie selber eine (natürlich sehr simple) Chat-Anwendung 
und werden dabei viele der Fragen beantworten müssen,
die bei der Entwicklung einer solchen Anwendung entstehen:

- Wie findet der Nachrichtenaustausch statt?
- Wie loggen sich meine Benutzer ein? Wie werden sie identifiziert?
- Welche Daten sollen gespeichert werden? Wie und wo?

Dabei kommt ein großer Teil des Wissens zum Einsatz, das die Aufgabengruppen
[PARTREF2::Go::Sprachen/Go] und [PARTREF::Go-Standardbibliothek] vermitteln.

Die Anwendung besteht aus einem __Lookup-Server__ (Programm 1, Produkt von
[PARTREF::go-chat-lookup-server]) und mehreren __Peers__ (Programm 2, Produkt von
[PARTREF::go-chat-peer-registration] und [PARTREF::go-chat-peer-messaging]), die miteinander kommunizieren.

So läuft das Ganze ab:

1. Lookup-Server läuft separat und enthält eine Tabelle, wo Benutzernamen den IP-Adressen der Form
   `ip_addr:port` zugeordnet sind;
2. Alle Peers registrieren sich beim Lookup-Server (Benutzername, IP-Adresse, die automatisch
   ausgelesen wird, und Port);
3. Alle Peers starten einen Empfänger-Server auf einem bestimmten Port;
4. Sobald ein Peer nach einem Gesprächspartner sucht, fragt er beim Lookup-Server nach der
   IP-Adresse und Port des anderen Peers nach.
