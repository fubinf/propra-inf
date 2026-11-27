title: Arbeiten mit dig
stage: beta
timevalue: 1.0
difficulty: 2
assumes: dnstools
---

[SECTION::goal::idea]
Ich kann verschiedene Arten von DNS-Informationen gezielt abrufen und verstehen.
Ich verstehe, warum eine geänderte DNS-Antwort nicht sofort überall ankommt.
[ENDSECTION]


[SECTION::background::default]
Mit DNS-Werkzeugen finden Sie Probleme mit der Namensauflösung und der Kommunikation zwischen
Rechnern.
`dig` kann etwas mehr als die vorher gezeigten DNS-Werkzeuge.
Einige Beispiele werden Ihnen hier gezeigt.
[ENDSECTION]


[SECTION::instructions::detailed]
<replacement id='dig-dnsserver'>
Zieldomain = `fu-berlin.de`
</replacement>


### Fortgeschrittenes Arbeiten mit [TERMREF::dig]

`dig` wird standardmäßig wie folgt aufgerufen: `dig @server name type`,
wobei `@server` der zu nutzende DNS-Server ist, `name` der zu suchende Domainname
und `type` der zu suchende DNS-Record-Type.
`dig` ist mächtig und hat sehr viele Optionen, von denen wir hier einige besprechen werden.
Sie haben bestimmt schon gemerkt, dass die Ausgabe von `dig` lang und ausführlich ist.
Man kann die Ausgabe mit der Option `+short` um einiges verkürzen.

[EC] Nutzen Sie die Option `+short` um nach der Zieldomain zu suchen.


### DNS-Record-Types

Der `A-Record` wird standardmäßig, ohne Angabe des Typen, gesucht.
Dieser Typ ordnet einen Domainnamen einer IPv4-Adresse zu.

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
  Datei `~/.digrc` gelesen wurden.
- Der zweite Teil der Ausgabe gibt die Frage wieder, also nach welchem Domainnamen man sucht
  und nach welchem Eintragstyp.
- Der dritte Teil der Ausgabe ist der interessante Teil, das ist die Antwort.
  Hier ist, in diesem Fall, die IP-Adresse der Zieldomain zu sehen.
- Der vierte Teil der Ausgabe liefert Einzelheiten über die DNS-Anfrage,
  beispielsweise wie lange die Anfrage gebraucht hat.

Was gibt es außer `A-Records` noch für Eintragstypen?

- Der `AAAA-Record` ordnet einen Domainnamen einer IPv6-Adresse zu.
- In der [PARTREF::dnstools]-Aufgabe wurden Sie schon nach dem `MX-Record` gefragt, das gibt den
  Mailserver an, der für die Domain Email empfängt.
- Der `NS-Record` gibt die [TERMREF::Nameserver] einer Domain an.
- Der `CNAME-Record` gibt einen Alias des Domainnamens wieder.
  Das entspricht ungefähr einem [PARTREF2::Unix-Links::symbolischen Link]:
  Dann zeigen also mehrere Namen auf denselben Server X und wenn man einen DNS-Eintrag von X ändert,
  wirkt das auch auf die anderen Namen.
  Zum Beispiel ist oft `www.mydomain.tld` das Gleiche wie `mydomain.tld`.
- Der `SOA-Record` ([TERMREF::Start of Authority]) ist ein DNS-Eintrag,
  der grundlegende Informationen über eine DNS-Zone enthält,
  einschließlich des primären Nameservers und der administrativen Kontaktinformationen.

[EC] Finden Sie den `AAAA-Record` der Zieldomain.
(Wenn die Zieldomain keinen `AAAA-Record` hat, lösen Sie die Aufgabe ersatzweise für `google.com`).

[EC] Finden Sie den `NS-Record` der Zieldomain.

[EC] Finden Sie den `SOA-Record` der Zieldomain.

Google betreibt einen öffentlichen DNS-Server, den jeder für seine Anfragen nutzen darf.
Er heißt Google Public DNS und ist unter dem Domainnamen `dns.google` erreichbar.
Er ist nicht dasselbe wie die Nameserver aus dem `NS-Record` von `google.com`:
Diese sind nur für die Domain `google.com` zuständig.

[EC] Finden Sie die IPv4-Adressen von `dns.google`.

[EC] Finden Sie den `AAAA-Record` von `google.com`.
Nutzen Sie für die Anfrage eine der eben gefundenen Adressen von Google Public DNS.


### DNS-Pfad verfolgen mit `+trace`

Sie hatten mit `traceroute` schon den Pfad von Ihrem Rechner zum Server erfragt.
Auch bei DNS gibt es sozusagen Pfade,
weil ein Nameserver zur Beantwortung einer Anfrage oft einen anderen zu Rate ziehen muss.
Mit der `trace`-Option geht `dig` diesen Pfad selbst Schritt für Schritt ab,
beginnend bei den [TERMREF2::Root-Nameserver::-n], und zeigt die Antwort jeder Station an.
Dieser Befehl kann nützlich sein, wenn Sie eine neue Domain angemeldet haben und prüfen wollen,
ob die Nameserver richtig eingestellt sind.
Lesen Sie in der
[dig(1) manpage](https://manpages.debian.org/stable/bind9-dnsutils/dig.1.en.html)
den Eintrag zu `+trace, +notrace`.

[EC] Nutzen Sie die `trace`-Option um den DNS-Pfad der Zieldomain herauszufinden.

Es sollten Ihnen mindestens die Root-Nameserver und die Nameserver der [TERMREF::Top-Level-Domain]
angezeigt werden, bevor die Antwort für die Zieldomain kommt.
Bei richtiger Konfiguration endet der Pfad bei einem der zuständigen Nameserver der Zieldomain,
der dann den `A-Record` liefert.


### Reflexion: Wie alt ist die Antwort?

[EC] Fragen Sie den `A-Record` der Zieldomain bei einem ihrer Nameserver ab
(die kennen Sie aus dem `NS-Record`).

[EC] Fragen Sie denselben `A-Record` bei `8.8.8.8` ab.

[EC] Wiederholen Sie die Abfrage bei `8.8.8.8` nach etwa einer Minute.

Vergleichen Sie jeweils die Zahl in der zweiten Spalte der `ANSWER SECTION`.

Lesen Sie in
[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034#section-3.6)
den Abschnitt **3.6. Resource Records** bis einschließlich des Eintrags `TTL`.
Die dort beschriebenen Felder finden Sie als Spalten der `ANSWER SECTION` wieder.

[EQ] Was bedeutet die Zahl in der zweiten Spalte, und warum ist sie bei `8.8.8.8` kleiner
als beim Nameserver der Zieldomain?

[HINT::Ist das dieselbe TTL wie bei `ping`?]
Der Name ist derselbe, die Einheit nicht.
Bei `ping` in [PARTREF::dnstools] zählt die TTL Router,
hier steht laut RFC 1034 eine Zeit in Sekunden.
[ENDHINT]

[HINT::Ich verstehe nicht, warum die Zahl bei `8.8.8.8` kleiner ist]
`8.8.8.8` ist nicht für die Zieldomain zuständig.
Woher hat er die Antwort, und was sagt Abschnitt 3.6 darüber, wie lange er sie aufbewahren darf?
[ENDHINT]

[HINT::Bei der zweiten Abfrage ist die Zahl größer geworden]
Hinter `8.8.8.8` stehen viele Server, jeder mit eigenem Cache.
Sie landen nicht bei jeder Abfrage beim selben.
[ENDHINT]

[EQ] Angenommen, der Betreiber der Zieldomain ändert morgen die IP-Adresse in ihrem `A-Record`.
Wie lange könnten Nutzer von `8.8.8.8` höchstens noch die alte Adresse bekommen?
Wie prüfen Sie als Admin, ob die Änderung beim zuständigen Nameserver schon angekommen ist?
[ENDSECTION]


[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll + Markdowndokument]
[PROT::ALT:dig.prot]


### Markdowndokument

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
