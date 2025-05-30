title: Netzwerkgrundlagen und DNS Werkzeuge
stage: beta
timevalue: 1.0
difficulty: 2
assumes: ssh
---

[SECTION::goal::idea]
Ich kann die Erreichbarkeit eines Rechners prüfen und kann
seine DNS-Informationen abrufen und grundlegend verstehen.
[ENDSECTION]

[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
Sobald beim Umgang mit Rechnernetzen irgendwas nicht erreichbar zu sein scheint,
ist das ein häufiger Arbeitsschritt.
[ENDSECTION]

[SECTION::instructions::detailed]
<replacement id='dnstools-dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Kolleg_innen erzählen Ihnen, dass sie keinen
Netzzugriff auf einen bestimmten Rechner haben. 
Wir zeigen Ihnen hier Befehle zur Analyse solch eines Problems.


### Werkzeuge installieren

Die hier besprochenen Werkzeuge gehören meist nicht zum Basisumfang des Systems, also:

[EC] `sudo apt update && sudo apt upgrade`

[EC] `sudo apt install dnsutils`


[NOTICE]
Sie werden hier 4 Werkzeuge kennenlernen.
Zwei davon (`dig`und `host`) haben einen sehr ähnlichen Zweck, nämlich [TERMREF2::DNS::--Abfragen]. 
Es ist trotzdem sinnvoll, _beide_ ausprobiert zu haben, da Ihnen auf manchen Systemen 
nur eines davon zur Verfügung steht.
[ENDNOTICE]


### Arbeiten mit `[TERMREF::ping]`

`ping` gibt Ihnen Rückmeldung über die Erreichbarkeit eines Systems. Es nutzt das 
[TERMREF::Transportprotokoll] [TERMREF::ICMP].
`ping` läuft auf vielen (nicht allen!) Systemen standardmäßig endlos weiter.
Zum Abbrechen nutzen Sie die Tastenkombination `STRG+C`.

Lesen Sie die [ping(8) manpage](https://manpages.debian.org/stable/iputils-ping/ping.8.en.html). 
Lesen Sie insbesondere die Synopsis, die **Description** und die Optionen **-c**, **-w**, **-i**.

[EC] Pingen Sie den Zielserver genau 5 mal an, in einem Intervall von 2 Sekunden.

[EC] Pingen Sie den Zielserver genau 10 Sekunden lang an.

`ping` gibt Ihnen nicht nur die Erreichbarkeit des Systems an. Schauen Sie sich die Ausgaben an,
die `ping` gibt. 
Lesen Sie den Absatz **TTL Details** der ping manpage.

[EQ] Unter welchen Umständen kann man einen korrekt funktionierenden Server,
der [PARTREF::ssh] anbietet, mit `ping` erreichen, aber nicht mit `ssh`?
Plappern Sie nicht die Manpage nach, sondern formulieren Sie selbst.
(Das Durchlaufen eines Routers wird auch "hop" genannt, also Sprung oder Hüpfer.)

(Falls Sie Server finden möchten, die Sie anpingen dürfen und die "weit weg" sind,
kann [meter.net](https://www.meter.net/tools/world-ping-test/) eine hilfreiche Quelle sein,
z.B. die Seite [HREF::https://www.meter.net/test-server/102-vultr/].)


### Arbeiten mit `host`

Lesen Sie die [host(1) manpage](https://manpages.debian.org/stable/bind9-host/host.1.en.html).
Lesen Sie insbesondere die **Synopsis** und die **Description**.

[EC] Nutzen Sie `host` um die [TERMREF::IP-Adresse] und den Mailserver des Zielservers herauszufinden.


### Arbeiten mit `[TERMREF::dig]`

Sichten Sie die [dig(1) manpage](https://linux.die.net/man/1/dig) und lesen Sie insbesondere 
die **Description**, die **Simple Usage** und die Option **-t**.

Lesen Sie im [Beitrag über dig](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/) 
von nixcraft die **DNS record types** nach.

[EC] Nutzen Sie `dig` um die IP-Adresse des Zielservers herauszufinden.

[EC] Finden Sie den Mailserver des Zielservers mit `dig` heraus.

[EQ] Charakterisieren Sie grob den wichtigsten Unterschied zwischen `dig` und `host` aus Aufrufersicht.


### `traceroute`

`[TERMREF::traceroute]` ist ein Befehl, der den Netzwerkpfad (die Route) von der Quelle zum Ziel angibt.

Dieser Befehl ist nützlich, um nachvollziehen zu können, wo die Pakete hängen bleiben, 
falls das Ziel nicht erreicht werden kann, oder warum eine Latenzzeit größer ist als erwartet.
Lesen Sie die [traceroute(1) manpage](https://manpages.debian.org/bookworm/traceroute/traceroute.1.en.html). 
Lesen Sie insbesondere die Synopsis, die **Description** und die Option **-I**.

[EC] Suchen Sie nach dem Pfad von Ihrem Rechner zum Zielserver mit `traceroute`.

Falls der Pfad nicht komplett aufgelöst werden konnte, ist das in Ordnung.
`traceroute` arbeitet im default-Modus mit UDP Paketen, die beim ersten Hop an den Port 33434 
gehen und bei jedem weiteren Hop wird die Portnummer um 1 erhöht. 
Falls bei einem Server der entsprechende Port geschlossen ist, schlägt das Verfahren fehl.
Deshalb gibt es eine neuere Methode, mit der man ICMP-Pakete für die Verfolgung nutzt:

[EC] Suchen Sie nach dem Pfad von Ihrem Rechner zum Zielserver mit ICMP-Paketen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
Die folgenden Ausgaben müssen heute nicht mehr genau so stimmen, nur der Art nach.
[PROT::ALT:dnstools.prot] 
[ENDINSTRUCTOR]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
