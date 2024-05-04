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
Mit DNS-Werkzeugen finden Sie Probleme mit den Namensauflösung und der Kommunikation zwischen 
Ressourcen.
[ENDSECTION]

[SECTION::instructions::detailed]
<replacement id='dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Ihre Kollegen erzählen Ihnen, dass sie keinen 
Zugriff auf eine Ressource haben. Wir zeigen Ihnen hier ein paar Befehle, die zur Problemlösung
helfen können.

### [TERMREF::Ping]

Einer der ersten bekannten Befehle ist `ping`. Es gibt Ihnen Rückmeldung über die Erreichbarkeit 
eines Systems.
 
Lesen Sie die den [Beitrag](https://wiki.ubuntuusers.de/ping/) über `ping` von ubuntuusers.
Lesen Sie insbesondere die **Benutzung** und die Optionen **-c**, **-w** und **-I**.

- [EC] Pingen Sie den Server genau 5 mal an.

`ping` gibt Ihnen nicht nur die Erreichbarkeit des Systems an. Schauen Sie sich die Ausgaben an, 
die `ping` gibt.  
Lesen Sie den Abschnitt **Optionen** des oberen [Beitrags](https://wiki.ubuntuusers.de/ping/).

- [EQ] Welche Informationen werden Ihnen neben der Erreichbarkeit noch gezeigt?


### [TERMREF::Dig]

`dig` wird primär genutzt, um die IP-Adresse eines Systems herauszufinden. Es hat mehr Funktionen 
auf die wir unten näher eingehen werden.

Lesen Sie die dig(1) [manpage](https://linux.die.net/man/1/dig).
Lesen Sie insbesondere die **Description** und die **Simple Usage**.

- [EC] Nutzen Sie `dig` um die IP des Zielservers herauszufinden.
- [EC] Erklären Sie kurz die verschiedenen Abschnitte des Ergebnisses.

Wie Sie im oberen Beitrag gelesen haben, können Sie mehrere dns query types eines Zielservers 
herausfinden.

Lesen Sie aus dem 
[Beitrag](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/).  
über dig von nixcraft, die Liste der **DNS record types**.

- [EC] Finden Sie den Mailserver des Zielservers heraus.


### [TERMREF::Traceroute]

`traceroute` zeigt den Pfad an, den Datenpakete von Ihrem Gerät zum Zielserver im Internet nehmen.
Angenommen, Sie haben kein Zugriff auf eine Ressource. Durch den traceroute finden Sie heraus,
ob das Problem an Ihrem lokalen Netz oder im Internet liegt.

Lesen Sie den [Beitrag](https://www.cyberciti.biz/faq/traceroute-tracepath-unix-linux-command/) 
über traceroute von nixcraft.
Lesen Sie insbesondere die **Benutzung** und den **Output**.

- [EC] Finden Sie heraus, über welche Hops der Zielserver erreicht wird.
- [EQ] Erklären Sie die einzelnen Spalten des Ergebnisses.
- [EQ] Warum werden bei einigen der Hops drei Sterne angezeigt?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]