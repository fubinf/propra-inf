title: Netzwerkgrundlagen mit DNS Werkzeugen
stage: alpha
timevalue: 1
difficulty: 2
assumes: apt, SSH

---

[SECTION::goal::idea]
Ich kann die Erreichbarkeit eines Rechners prüfen und kann
seine DNS-Informationen abrufen und ungefähr verstehen.
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
beitragen können.


### Werkzeuge installieren

Bevor wir mit den Werkzeugen anfangen müssen wir sie uns herunterladen.

- [EC] Aktualisieren Sie Ihr System.
- [EC] Installieren Sie das Paket `dnsutils`.

In diesem Paket sind alle Werkzeuge enthalten, die wir in dieser Aufgabe brauchen werden.

[NOTICE]
Sie werden hier 4 Werkzeuge kennenlernen.
Drei davon, `dig`, `nlookup` und `host`, haben einen sehr ähnlichen Zweck, nämlich DNS-Abfragen. 
Es ist trotzdem sinnvoll, alle drei ausprobiert zu haben, da es Ihnen passieren kann, 
dass Ihnen nur eines davon zur Verfügung steht.
[ENDNOTICE]


### Arbeiten mit [TERMREF::ping]

`ping` gibt Ihnen Rückmeldung über die Erreichbarkeit eines Systems.

Damit die Ping-Ausgabe gestoppt wird, nutzen Sie die Tastenkombination `STRG+C`.

Lesen Sie die [ping(8) manpage](https://manpages.debian.org/bookworm/iputils-ping/ping.8.en.html). 
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


### Arbeiten mit [TERMREF::dig]

`dig` wird primär genutzt, um die IP-Adresse eines Systems herauszufinden. Man kann `dig` 
explizit angeben mit welchem DNS-Server der Befehl nach IP-Adressen suchen soll.

Lesen Sie die [dig(1) manpage](https://linux.die.net/man/1/dig).
Lesen Sie insbesondere die **Description**, die **Simple Usage** und die Option **-t**.

- [EC] Nutzen Sie `dig` um Informationen über den Google DNS-Server herauszufinden.
    -   IP der Google DNS-Server: 8.8.8.8
- [EC] Nutzen Sie den Google DNS-Server um die IP-Adresse des Zielservers herauszufinden.

`dig` kann mehrere IPs von Servern herausfinden.

Lesen Sie aus dem [Beitrag](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/) 
über dig von nixcraft, die Liste der **DNS record types**.

- [EC] Finden Sie den Mailserver des Zielservers mit `dig` heraus.

Angenommen Sie erreichen den Zielserver nicht. `dig` kann die [TERMREF::Nameserver] des Zielservers 
auflösen. Durch diese Nameserver können Sie dann nachververfolgen, wie der DNS-Name rekursiv aufgelöst wird.

Wir fangen erstmal mit den root-Servern an, hier ist egal, welchen wir wählen.

- [EC] Lösen Sie mit einem root-Server die IP-Adresse des Zielservers auf: `dig <Zielserver> @a.root-servers.net`

Schauen Sie in der Authority Section nach einem weiteren Nameserver. Diese sind mit NS markiert.

- [EC] Ersetzen Sie den root-Servr aus obiger Aufgabe mit dem neuen Nameserver und führen Sie den Befehl aus.

Wenn hier schon die IP des Zielservers angezeigt wird, dann sind sie fertig, falls nicht:

- [EC] Wiederholen Sie den Prozess, bis Sie die IP des Zielservers herausgefunden haben.

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
