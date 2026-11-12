title: APT Paketverwaltung
stage: beta
timevalue: 1.0
difficulty: 2
assumes: apt101
---

[SECTION::goal::trial]
Ich kann `apt` zur Verwaltung von Debian-Softwarepaketen anwenden.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::apt101] haben Sie mit `sudo apt install` ein Paket installiert.
Auf einem selbstverwalteten Debian-System braucht man `apt` aber für mehr.
Man hält mit `apt` das System aktuell und wird Pakete bei Bedarf auch wieder los,
samt der Abhängigkeiten, die beim Installieren automatisch mitgekommen sind.
Auch der Wechsel auf eine komplett neue Betriebssystemversion wird von `apt` erledigt.
[ENDSECTION]

[SECTION::instructions::detailed]

[NOTICE]
Für diese Aufgabe brauchen Sie ein Debian-System, auf dem Sie Administratorrechte haben.
Auf einem Poolrechner der Uni oder auf dem Mac lässt Sie sich nicht bearbeiten.
Wie man auf dem Mac stattdessen Pakete installiert, steht in [PARTREF::apt101].
[ENDNOTICE]

Grundlage dieser Aufgabe ist der
[Beitrag über `apt`](https://wiki.ubuntuusers.de/apt/apt/)
im Wiki von ubuntuusers.
Er ist für Ubuntu geschrieben, die Befehle, die wir hier brauchen, funktionieren auf Debian aber genauso.
Lesen Sie dort zuerst den Abschnitt **Benutzung**.
Root-Rechte bekommen Sie mit `sudo`, das Sie aus [PARTREF::apt101] kennen.
Die Abschnitte **Historie anzeigen / rückgängigmachen / wiederholen und zurücksetzen**,
**sources.list editieren** und **Problembehebung** brauchen Sie nicht.
Die `history`-Befehle gibt es im `apt` von Debian 13 noch gar nicht.


### System aktualisieren

Insbesondere zum Schutz vor Sicherheitslücken sollte man die installierten Pakete
auch auf einem anscheinend gut funktionierenden System regelmäßig aktualisieren.
`apt update` kennen Sie schon aus [PARTREF::apt101]:
Es lädt nur den Paketkatalog neu und installiert nichts.

Lesen Sie im Abschnitt **Pakete verwalten** die Einträge zu `update`, `upgrade` und `full-upgrade`
und danach den Abschnitt **Vergleiche apt-get/apt**.

Aktualisieren Sie den Paketkatalog.
Dieser Aufruf gehört nicht ins Kommandoprotokoll.

[EC] Lassen Sie sich die Pakete auflisten, für die es eine neuere Version gibt:  
`apt list --upgradable`

Passt eine Ausgabe nicht auf einen Bildschirm, zeigt `apt` sie in der `less`-Ansicht an.
Blättern Sie dann mit der Leertaste bis zum Ende und verlassen Sie die Ansicht mit `q`.
Sonst fehlt der Rest der Ausgabe im Terminal und damit auch im Kommandoprotokoll.

Ist die Liste leer, ist Ihr System schon aktuell
und der nächste Schritt hat nichts zu tun.

Aktualisieren Sie die installierten Pakete.
Lesen Sie wie in [PARTREF::apt101] die Paketliste, bevor Sie mit `y` bzw. `j` bestätigen.
Auch dieser Aufruf gehört nicht ins Kommandoprotokoll, weil seine Ausgabe sehr lang ist.

[EC] Rufen Sie `apt list --upgradable` noch einmal auf.

In älteren Anleitungen finden Sie oft `apt-get dist-upgrade` statt `apt full-upgrade`.

[EQ] Was tut `apt full-upgrade` zusätzlich zu `apt upgrade`?
Was hat `apt-get dist-upgrade` damit zu tun?
Warum sollte man bei diesen beiden Kommandos die Paketliste vor dem Bestätigen besonders genau lesen?


### Pakete suchen, installieren, auflisten

Lesen Sie den Abschnitt **Suchen/Durchsuchen**.

In dieser Aufgabe nehmen wir als Beispiel den Midnight Commander.
Das ist ein textbasierter, halbgrafischer Dateimanager -- ziemlich praktisch.

[EC] Suchen Sie mit `apt` nach dem Begriff `midnight commander`.  
Blättern Sie wie oben bis zum Ende der Ausgabe.

[EC] Geben Sie die Paketinformationen des Paketes für den Midnight Commander aus.

[EC] Installieren Sie das Paket.
Achten Sie in der Ausgabe darauf, welche Pakete `apt` zusätzlich installiert.

[EC] Geben Sie die Liste aller installierten(!) Pakete aus, deren Namen mit `m` beginnen.

[HINT::Meine Liste ist leer]
Haben Sie das Suchmuster ohne Anführungszeichen geschrieben?
Dann ersetzt die Shell `m*` durch die Namen passender Dateien im aktuellen Verzeichnis, bevor `apt` startet.
Liegt dort etwa eine Datei `main.py`, sucht `apt` nach einem Paket namens `main.py` und findet keins.
Setzen Sie das Muster in Anführungszeichen, damit die Shell es unverändert an `apt` weitergibt.
[ENDHINT]

Hinter jedem Paket steht in eckigen Klammern entweder `[installed]`
oder `[installed,automatic]` (bzw. `[installiert]` und `[installiert,automatisch]`).

[EQ] Warum steht beim Paket des Midnight Commanders `installed`, beim Paket `mc-data` dagegen `installed,automatic`?


### Pakete deinstallieren

Lesen Sie im Abschnitt **Pakete verwalten** die Einträge zu `remove`, `purge` und `autoremove`.

Zum ausdrücklichen Deinstallieren gibt es zwei Kommandos: `apt remove` und `apt purge`.
Wir beginnen mit `remove`.

[EC] Deinstallieren Sie den Midnight Commander mit `apt remove`.

Unterhalb von `apt` arbeitet das Programm `dpkg`, das über jedes Paket auf dem System Buch führt.
`dpkg -l PAKETNAME` zeigt den Zustand eines Pakets.
Die ersten beiden Buchstaben der Zeile sind die wichtigen.
Der erste gibt den gewünschten Zustand an, der zweite den tatsächlichen.
In Kurzform stehen die Bedeutungen in den Kopfzeilen der Ausgabe (`Desired=...` und `Status=...`).
`dpkg -l` ruft dafür `dpkg-query` auf.
Lesen Sie deshalb in `man dpkg-query` den Eintrag **`-l, --list`**.
Ein normal installiertes Paket hat zum Beispiel `ii`:
Gewünscht ist `Install`, der Zustand ist `Installed`.

[EC] Sehen Sie sich mit `dpkg -l` den Zustand des Pakets an.

Die Pakete, die beim Installieren automatisch mitgekommen sind, liegen noch auf Ihrem System,
obwohl sie jetzt niemand mehr braucht.
Darauf hat Sie schon `apt remove` in seiner Ausgabe hingewiesen.

[EC] Entfernen Sie mit `apt autoremove` die nicht mehr benötigten Pakete.
Vergleichen Sie die Paketliste vor dem `[Y/n]` mit den Paketen,
die beim Installieren des Midnight Commanders zusätzlich installiert wurden.

[HINT::`autoremove` will auch Pakete entfernen, die ich behalten möchte]
Je nach Vorgeschichte Ihres Systems stehen in der Liste auch Pakete,
die mit dem Midnight Commander nichts zu tun haben.
Meist sind das ebenfalls überflüssige Reste wie alte Bibliotheken, die ruhig mit weg können.
Steht aber ein Programm dabei, das Sie selbst benutzen, brechen Sie mit `n` ab.
Mit `sudo apt-mark manual PAKETNAME` markieren Sie es als ausdrücklich installiert.
`autoremove` lässt es danach in Ruhe.
Rufen Sie `autoremove` dann erneut auf.
[ENDHINT]

[EC] Deinstallieren Sie den Midnight Commander jetzt mit `apt purge`.

[EC] Sehen Sie sich wieder mit `dpkg -l` den Zustand des Pakets an.

[EQ] Was bedeuten die ersten beiden Buchstaben in Ihren beiden Ausgaben von `dpkg -l`?
Erklären Sie damit den Unterschied zwischen `apt remove` und `apt purge`.

[EQ] In welcher Situation ist `apt remove` sinnvoller?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll + Markdown]
### Kommandoprotokoll
[PROT::ALT:apt.prot]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
