title: Netzwerkgrundlagen mit DNS Werkzeugen
stage: alpha
timevalue: 1
difficulty: 2
assumes: apt

---

[SECTION::goal::idea]
Ich verstehe Netzwerkgrundlagen, um DNS-Informationen eines Servers herauszufinden.
[ENDSECTION]

[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
[ENDSECTION]

[SECTION::instructions::detailed]
<replacement id='dnstools-dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Kolleg_innen erzählen Ihnen, dass sie keinen
Zugriff auf eine Ressource haben. Wir zeigen Ihnen hier Befehle, die zur Problemlösung
helfen können.

### Werkzeuge installieren

Bevor wir mit den Werkzeugen anfangen müssen wir sie uns herunterladen.

- [EC] Aktualsieren Sie Ihr System.
- [EC] Installieren Sie das Paket `dnsutils`.

In diesem Paket sind alle folgenden Werkzeuge enthalten, die wir in dieser Aufgabe brauchen werden.

### Anmerkung

Sie werden hier 4 Werkzeuge kennenlernen: `ping`, `dig`, `nlookup` und `host`. Außer `ping`, geben
alle Werkzeuge ähnliche Ausgaben. Es ist sinnvoll alle Werkzeuge einmal gesehen zu
haben, da es Ihnen passieren könnte, dass man keine Applikationen auf dem System
nachinstallieren darf.

### Arbeiten mit [TERMREF::ping]

Einer der ersten bekannten Befehle ist `ping`. `ping` gibt Ihnen Rückmeldung über die Erreichbarkeit
eines Systems.

Lesen Sie die [ping(8) manpage](https://manpages.debian.org/bookworm/iputils-ping/ping.8.en.html). 
Lesen Sie insbesondere die Synopsis, die **Description** und die Optionen **-c**, **-w**, **-i**.

- [EC] Pingen Sie den Server genau 5 mal an, in einem Intervall von 2 Sekunden.
- [EC] Pingen Sie den Server genau 10 Sekunden lang?

`ping` gibt Ihnen nicht nur die Erreichbarkeit des Systems an. Schauen Sie sich die Ausgaben an,
die `ping` gibt.  

Lesen Sie den Absatz **TTL Details** der [ping(8) manpage](https://manpages.debian.org/bookworm/iputils-ping/ping.8.en.html).

- [EQ] Erklären Sie den Begriff **ttl**.

### Arbeiten mit [TERMREF::dig]

`dig` wird primär genutzt, um die IP-Adresse eines Systems herauszufinden. Es hat mehr Funktionen,
auf die wir unten näher eingehen werden.

Lesen Sie die [dig(1) manpage](https://linux.die.net/man/1/dig).
Lesen Sie insbesondere die **Description**, die **Simple Usage** und die Option **-t**.

- [EC] Nutzen Sie `dig` um die IP des Zielservers herauszufinden.

`dig` kann mehrere IPs von Servern herausfinden.

Lesen Sie aus dem [Beitrag](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/) 
über dig von nixcraft, die Liste der **DNS record types**.

- [EC] Finden Sie den Mailserver des Zielservers mit `dig` heraus.

### Arbeiten mit nslookup

Lesen Sie die [nslookup(1) manpage](https://linux.die.net/man/1/nslookup).
Lesen Sie die **Synopsis**, die **Description** und die **Arguments**.

- [EC] Nutzen Sie `nslookup` um die IP des Zielservers herauszufinden.
- [EC] Finden Sie den Mailserver des Zielservers mit `nslookup` heraus.

### Arbeiten mit host

Lesen Sie die [host(1) manpage](https://manpages.debian.org/bookworm/bind9-host/host.1.en.html).
Lesen Sie insbesondere die **Synopsis** und die **Description**.

- [EC] Nutzen Sie `host` um die IP und den Mailserver des Zielservers herauszufinden.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
