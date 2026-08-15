title: "Chat: Nachrichtenaustausch im Terminal"
stage: alpha
---
Jeder kennt WhatsApp, Telegram, Signal und sicherlich einige weitere Anwendungen,
die uns Austausch mit anderen Benutzern ermöglichen.

In dieser Aufgabengruppe implementieren Sie selber eine Chat-Anwendung (auch wenn
nicht so hübsch wie die obigen Beispiele) und werden all die Fragen beantworten müssen,
die bei der Entwicklung eines Chats entstehen:

- Wie findet der Nachrichtenaustausch statt?
- Wie loggen sich meine Benutzer ein? Wie werden sie identifiziert?
- Welche Daten sollen gespeichert werden? Wie und wo?

Die Anwendung besteht aus einem __Lookup-Server__ (Programm 1, Produkt von
[PARTREF::go-chat-lookup-server]) und mehreren __Peers__ (Programm 2, Produkt von
[PARTREF::go-chat-peer]), die miteinander kommunizieren.

So läuft das Ganze ab:

1. Lookup-Server läuft separat und enthält eine Tabelle, wo Benutzernamen den IP-Adressen der Form
   `ip_addr:port` zugeordnet sind;
2. Alle Peers registrieren sich beim Lookup-Server (Benutzername, IP-Adresse, die automatisch
   ausgelesen wird, und Port);
3. Alle Peers starten einen Empfänger-Server auf einem bestimmten Port;
4. Sobald ein Peer nach einem Gesprächspartner sucht, fragt er beim Lookup-Server nach der
   IP-Adresse und Port des anderen Peers nach.
