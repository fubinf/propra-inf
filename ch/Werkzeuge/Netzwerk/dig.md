title: Arbeiten mit dig
stage: alpha
timevalue: 0.5
difficulty: 3
assumes: dnstools
---

[SECTION::goal::idea]
Ich kann DNS-Informationen abrufen und grundlegend verstehen.
[ENDSECTION]

[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
Sobald beim Umgang mit Rechnernetzen irgendwas nicht erreichbar ist oder zu sein scheint,
ist das ein häufiger Arbeitsschritt.
[ENDSECTION]


[SECTION::instructions::detailed]

<replacement id='dig-dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

Angenommen Sie sind ein Netzwerkadministrator und Kolleg_innen erzählen Ihnen, dass sie keinen
Zugriff auf eine Ressource haben. Wir zeigen Ihnen hier dig, das zur Problemlösung
beitragen könnte.

### Werkzeuge installieren

Bevor wir mit den Werkzeugen anfangen müssen wir sie uns herunterladen.

- [EC] Aktualisieren Sie Ihr System.
- [EC] Installieren Sie das Paket `dnsutils`.

In diesem Paket ist dig enthalten, das wir in dieser Aufgabe brauchen werden.

### Fortgeschrittenes Arbeiten mit [TERMREF::dig]

`dig` wird primär genutzt, um die IP-Adresse eines Systems herauszufinden, kann aber viel mehr:

- [EC] Nutzen Sie `dig` um Informationen über den Google DNS-Server herauszufinden.
  Die IP-Adresse der Google DNS-Server lautet 8.8.8.8.
- [EC] Nutzen Sie den Google DNS-Server um die IP-Adresse des Zielservers herauszufinden.

Angenommen Sie erreichen den Zielserver nicht. `dig` kann die [TERMREF::Nameserver] des Zielservers 
auflösen. Durch diese Nameserver können Sie dann nachververfolgen, wie der DNS-Name rekursiv aufgelöst wird.

Wir fangen erstmal mit den [TERMREF2::Root-Nameserver::-n] an, hier ist egal, welchen wir wählen.

- [EC] Lösen Sie mit einem Root-Nameserver die IP-Adresse des Zielservers auf: `dig <Zielserver> @a.root-servers.net`

Schauen Sie in der Authority Section nach einem weiteren Nameserver. Diese sind mit NS markiert.

- [EC] Ersetzen Sie den Root-Nameserver aus obiger Aufgabe mit dem neuen Nameserver und führen Sie den Befehl aus.

Wenn hier nur noch die IP-Adresse des Zielservers angezeigt wird, dann sind Sie fertig, falls nicht:

- [EC] Wiederholen Sie den Prozess, bis Sie die IP-Adresse des Zielservers herausgefunden haben.


[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:dig.prot] 
[ENDINSTRUCTOR]