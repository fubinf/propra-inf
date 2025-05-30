title: Arbeiten mit dig
stage: beta
timevalue: 1.0
difficulty: 2
assumes: dnstools
---

[SECTION::goal::idea]
Ich kann verschiedene Arten von DNS-Informationen gezielt abrufen und verstehen.
[ENDSECTION]

[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
`dig` kann etwas mehr als die vorher gezeigten DNS-Werkzeuge. Einige Beispiele werden Ihnen 
hier gezeigt.
[ENDSECTION]


[SECTION::instructions::detailed]

<replacement id='dig-dnsserver'>
Zielserver = `fu-berlin.de`
</replacement>

### Fortgeschrittenes Arbeiten mit [TERMREF::dig]

`dig` wird standardmäßig wie folgt aufgerufen: `dig @server name type`
Wobei `@server` der zu nutzende DNS-Server ist, `name` die zu suchende IP-Adresse beziehungsweise 
URL ist und `type` der zu suchende DNS-Record-Type ist.
`dig` ist mächtig und hat sehr viele Optionen, von denen wir hier einige besprechen werden.
Sie haben bestimmt schon gemerkt, dass die Ausgabe von `dig` lang und ausführlich ist. Man kann die 
Ausgabe mit der Option `+short` um einiges verkürzen.

[EC] Nutzen Sie die Option `+short` um nach dem Zielserver zu suchen.


### DNS-Record-Types

Der `A-Record` wird standardmäßig, ohne Angabe des Typen, gesucht. Dieser Typ ordnet einen 
Domainnamen einer IPv4-Adresse zu.

Siehe:

```bash
condric@SIMMOB-T480-01 ~ 18:13:12  2015
$ dig fu-berlin.de

; <<>> DiG 9.18.33-1~deb12u2-Debian <<>> fu-berlin.de
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 34760
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;fu-berlin.de.                  IN      A

;; ANSWER SECTION:
fu-berlin.de.           81543   IN      A       160.45.170.10

;; Query time: 0 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Thu Mar 13 18:13:19 CET 2025
;; MSG SIZE  rcvd: 57
```

- Der erste Teil der Ausgabe gibt unter anderem die Optionen wieder, die übergeben oder aus der 
  Datei ~/.digrc gelesen wurden.
- Der zweite Teil der Ausgabe gibt die Frage wieder, also nach welchem domainname man sucht und nach 
  welchem Eintragstyp.
- Der dritte Teil der Ausgabe ist der interessante Teil, das ist die Antwort. Hier ist, in diesem Fall, 
  die IP-Adresse des Zielservers zu sehen.
- Der vierte Teil der Ausgabe liefert Einzelheiten über die DNS-Anfrage, 
  z.B. wie lange die Anfrage gebraucht hat.

Was gibt es außer `A-Records` noch für Eintragstypen?

- Der `AAAA-Record` ordnet einen Domainnamen einer IPv6-Adresse zu.
- In der [PARTREF::dnstools]-Aufgabe wurden Sie schon nach dem `MX-Record` gefragt, das gibt den
  Mailserver an, der für die Domain Email empfängt.
- Der `NS-Record` gibt die [TERMREF::Nameserver] einer Domain an.
- Der `CNAME-Record` gibt einen Alias des Domainnamens wieder. 
  Das entspricht ungefähr einem [PARTREFMANUAL::Unix-Links::symbolischen Link]:
  Dann zeigen also mehrere Namen auf denselben Server X und wenn man einen DNS-Eintrag von X ändert,
  wirkt das auch auf die anderen Namen.
  Zum Beispiel ist oft `www.mydomain.tld` das Gleiche wie `mydomain.tld`.
- Der `SOA-Record` ([TERMREF::Start of Authority]) ist ein DNS-Eintrag, 
  der grundlegende Informationen über eine DNS-Zone enthält, 
  einschließlich des primären Nameservers und der administrativen Kontaktinformationen.


[EC] Finden Sie den `AAAA-Record` des Zielservers.
(Wenn der Zielserver keinen `AAAA-Record` hat, lösen Sie die Aufgabe ersatzweise für `google.com`).

[EC] Finden Sie den `NS-Record` des Zielservers.

[EC] Finden Sie den `SOA-Record` des Zielservers.

[EC] Finden Sie den `AAAA-Record` von `google.com`. 
Nutzen Sie für die Anfrage die Public DNS Server von Google (die sie mit `dig` finden können).

[HINT::Ich verstehe nicht, wie ich die Public DNS Server von Google finde]
"DNS Server" ist ein anderes Wort für "Nameserver", siehe oben.
[ENDHINT]


### dig trace

Sie hatten mit `traceroute` schon den Pfad von Ihrem Rechner zum Server erfragt.
Auch bei DNS gibt es sozusagen Pfade, weil ein Nameserver zur Beantwortung einer Anfrage oft einen anderen
zu Rate ziehen muss.
`dig` kann sich als DNS-Server ausgeben und den so entstehenden Pfad von DNS-Abfragen wiedergeben.
Dieser Befehl kann nützlich sein, wenn Sie eine neue Webseite angemeldet haben und prüfen wollen, ob 
die Nameserver richtig eingestellt sind.
Lesen Sie die `trace`-Option aus der [dig(1) manpage](https://linux.die.net/man/1/dig).

[EC] Nutzen Sie die `trace`-Option um den DNS-Pfad des Zielservers herauszufinden.

Es sollten Ihnen mindestens die root-Server und ein weiterer Nameserver angezeigt werden, bevor der 
Zielserver angezeigt wird. Bei richtiger Konfiguration werden Sie bis zu Ihrem Zielserver weitergeleitet.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:dig.prot] 
[ENDINSTRUCTOR]