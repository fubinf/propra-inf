title: Netzwerkgrundlagen mit DNS Werkzeugen
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: apt, SSH

---

[SECTION::goal::idea]
Ich kann die Erreichbarkeit eines Rechners prüfen und kann
seine DNS-Informationen abrufen und grundlegend verstehen.
[ENDSECTION]

[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
Sobald beim Umgang mit Rechnernetzen irgendwas nicht erreichbar ist oder zu sein scheint,
ist das ein häufiger Arbeitsschritt.
[ENDSECTION]

[SECTION::instructions::detailed]
<replacement id='dnstools-dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Kolleg_innen erzählen Ihnen, dass sie keinen
Zugriff auf eine Ressource haben. Wir zeigen Ihnen hier Befehle, die zur Problemlösung
beitragen können.


### Werkzeuge installieren

Bevor wir mit den Werkzeugen anfangen müssen wir sie herunterladen.

- [EC] Aktualisieren Sie Ihr System.
- [EC] Installieren Sie das Paket `dnsutils`.

In diesem Paket sind alle Werkzeuge enthalten, die wir in dieser Aufgabe brauchen werden.

[NOTICE]
Sie werden hier 4 Werkzeuge kennenlernen.
Zwei davon sind `dig`und `host`, haben einen sehr ähnlichen Zweck, nämlich [TERMREF2::DNS::--Abfragen]. 
Es ist trotzdem sinnvoll, beide ausprobiert zu haben, da es Ihnen passieren kann, 
dass Ihnen nur eines davon zur Verfügung steht.
[ENDNOTICE]


### Arbeiten mit [TERMREF::ping]

`ping` gibt Ihnen Rückmeldung über die Erreichbarkeit eines Systems. Es nutzt das 
[TERMREF::Transportprotokoll] [TERMREF::ICMP].

Damit die Ping-Ausgabe gestoppt wird, nutzen Sie die Tastenkombination `STRG+C`.

Lesen Sie die [ping(8) manpage](https://manpages.debian.org/stable/iputils-ping/ping.8.en.html). 
Lesen Sie insbesondere die Synopsis, die **Description** und die Optionen **-c**, **-w**, **-i**.

- [EC] Pingen Sie den Zielserver genau 5 mal an, in einem Intervall von 2 Sekunden.
- [EC] Pingen Sie den Zielserver genau 10 Sekunden lang an.

`ping` gibt Ihnen nicht nur die Erreichbarkeit des Systems an. Schauen Sie sich die Ausgaben an,
die `ping` gibt. 

Lesen Sie den Absatz **TTL Details** der ping manpage.

- [EQ] Unter welchen Umständen kann man einen korrekt funktionierenden Server,
  der [PARTREF::SSH] anbietet, mit `ping` erreichen, aber nicht mit `ssh`?

(Falls Sie Server finden möchten, die Sie anpingen dürfen und die "weit weg" sind,
kann [meter.net](https://www.meter.net/tools/world-ping-test/) eine hilfreiche Quelle sein,
z.B. die Seite [HREF::https://www.meter.net/test-server/102-vultr/].)

### Arbeiten mit host

Lesen Sie die [host(1) manpage](https://manpages.debian.org/stable/bind9-host/host.1.en.html).
Lesen Sie insbesondere die **Synopsis** und die **Description**.

- [EC] Nutzen Sie `host` um die [TERMREF::IP-Adresse] und den Mailserver des Zielservers herauszufinden.

### Arbeiten mit [TERMREF::dig]

Sichten Sie die [dig(1) manpage](https://linux.die.net/man/1/dig) und lesen Sie insbesondere 
die **Description**, die **Simple Usage** und die Option **-t**.

Lesen Sie im [Beitrag über dig](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/) 
von nixcraft die **DNS record types** nach.

- [EC] Nutzen Sie `dig` um die IP-Adresse des Zielservers herauszufinden.
- [EC] Finden Sie den Mailserver des Zielservers mit `dig` heraus.

### Reflektion

- [EQ] Charakterisieren Sie grob den wichtigsten Unterschied zwischen `dig` und `host` aus Aufrufersicht.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:dnstools.prot] 
[ENDINSTRUCTOR]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
