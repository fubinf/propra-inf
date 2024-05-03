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
Ein Linux-Administrator sollte wissen, ob seine Ressourcen erreichbar sind.  
Hier werden wir einige dieser Befehle näher beleuchten.
[ENDSECTION]

[SECTION::instructions::detailed]
<replacement id='dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Ihre Kollegen erzählen Ihnen, dass sie Probleme 
haben Zugriff auf eine Ressource zu bekommen. Damit Sie wissen, wie Sie eine Lösung zu der 
Erreichbarkeit der Ressource finden können, behandeln wir hier Befehle, die dabei helfen.

### [TERMREF::Ping]
Lesen Sie sich den [Beitrag](https://wiki.ubuntuusers.de/ping/) über ping von ubuntuusers durch.

- [EC] Pingen Sie den Server genau 10 mal an. Nutzen Sie eine [TERMREF::Option] dafür.
- [EQ] Erkären Sie die einzelnen Spalten Ihres Ergebnisses.

### [TERMREF::Dig]
Lesen Sie sich den [Beitrag](https://www.cyberciti.biz/faq/linux-unix-dig-command-examples-usage-syntax/) 
über dig von nixcraft durch.

- [EC] Nutzen Sie nun `dig` um die IP des Zielservers herauszufinden.
- [EC] Erklären Sie kurz die verschiedenen Abschnitte des Ergebnisses.
- [EC] Finden Sie den Mailserver des Zielservers heraus.


### [TERMREF::Traceroute]
Lesen Sie sich den [Beitrag](https://www.cyberciti.biz/faq/traceroute-tracepath-unix-linux-command/) 
über traceroute von nixcraft durch.

- [EC] Finden Sie heraus, über welche Hops Sie den Zielserver erreichen.
- [EQ] Erklären Sie die einzelnen Spalten ihres Ergebnisses.
- [EQ] Warum werden bei einigen der Hops drei Sterne angezeigt?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
