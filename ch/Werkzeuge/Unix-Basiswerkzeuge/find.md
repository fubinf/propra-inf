title: find - Dateien auf dem System wiederfinden
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
requires: Dateibaum-beschaffen
---

[SECTION::goal::idea]
Ich verstehe wie `find` funktioniert und weiß wie ich damit Dateien finden kann.
[ENDSECTION]


[SECTION::background::default]
Das Kommando `find` ist ein vielseitiges Werkzeug, um Verzeichnisbäume zu durchsuchen. 
Es erlaubt, Suchkriterien wie Namen, Dateitypen, Änderungszeiten oder Berechtigungen anzugeben
und die so gefundenen Dateien zu bearbeiten oder (meistens) ihre Pfadnamen auszugeben.
[ENDSECTION]


[SECTION::instructions::detailed]
[EC] Wechseln Sie in den Ordner Ihres [TERMREF2::Hilfsbereich::-s], wo der Dateibaum entpackt wurde.

Lesen und verstehen Sie die Synopsis der 
[find(1) manpage](https://manpages.debian.org/stable/findutils/find.1.en.html).
Nutzen Sie die manpage als Plan B, falls in den anderen Quellen etwas nicht klar genug wird.

Lesen und verstehen Sie den Abschnitt **Name** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).


### `find` auf Dateien und Verzeichnisse anwenden

Sie untersuchen ein Linux-System, bei dem die Passwortregeln für Benutzerkonten angepasst werden sollen.
Ein Kollege erzählt Ihnen, dass die Einstellungen für Passwort-Policies nicht direkt in `/etc/shadow` oder
`/etc/login.defs` stehen, sondern in einer Konfigurationsdatei im Verzeichnisbaum von `pam.d/`.
Er ist sich sicher, dass die Datei `common-password` heißt, weiß aber nicht mehr genau, wo sie liegt.

Da der `/etc/pam.d/`-Ordner viele verschiedene Konfigurationsdateien für Authentifizierung und Login
enthält, wäre es mühsam, jede Datei einzeln zu öffnen. Mit `find` können Sie den Verzeichnisbaum
automatisch durchsuchen und die Datei schnell lokalisieren.

[EC] Finden Sie die Datei `common-password`.

Sie arbeiten an einem Projekt mit vielen Unterordnern und haben zahlreiche Python-Skripte
angelegt. Jetzt möchten Sie herausfinden, welche `.py`-Dateien sich überall im Projekt
befinden, um z. B. alle Skripte zu überprüfen, Tests auszuführen oder eine Übersicht
zu erstellen. Die Dateien können in unterschiedlichen Unterverzeichnissen liegen, und
manuelles Durchsuchen wäre zu zeitaufwendig.

`find` kann den gesamten Verzeichnisbaum durchsuchen und gezielt auch nach Dateiendungen
suchen. So bekommen Sie schnell einen vollständigen Überblick über alle relevanten
Dateien.

[EC] Finden Sie alle Python-Dateien, die auf `.py` enden, im aktuellen Verzeichnis und
allen Unterverzeichnissen.  

In vielen Projekten entstehen temporäre Dateien, die unterschiedlich geschrieben sein
können, z. B. `.tmp`, `.TMP` oder `.Tmp`. Wenn Sie solche Dateien löschen oder prüfen
möchten, reicht eine einfache Suche nach exakt `.tmp` nicht aus – Sie könnten viele
Dateien übersehen.

Um das Prinzip zu veranschaulichen, machen wir ein Beispiel mit dem Wort `default`.

[EC] Finden Sie alle Dateien, die `default` heißen, egal ob Groß- oder
Kleinschreibung.

Lesen und verstehen Sie die Unterabschnitte **Pfad** und **Typ** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie haben gerade gelernt, wie man mit `find` sowohl Dateien als auch Verzeichnisse
finden kann. Oft ist es aber hilfreich, gezielt nur nach dem einen _oder_ dem anderen zu
suchen.  

Stellen Sie sich vor, Sie haben ein großes Projekt und möchten alle Konfigurationsordner `config`
ausfindig machen, um deren Inhalte zu überprüfen oder Skripte darauf anzuwenden – ohne
jeden Pfad einzeln kennen zu müssen.
Sie ahnen oder wissen, dass es zugleich auch einzelne Dateien mit dem Namen `config`
gibt; potentiell viele. Die möchten Sie also aus der Suche ausschließen.

[EC] Listen Sie alle `config`-Verzeichnisse auf (aber nicht Dateien namens `config`).

Nun fällt Ihnen ein "Nein, das war ja genau falschrum.".
Tatsächlich müssen Sie die _Dateien_ namens `config` finden und die Ordner unterdrücken.

[EC] Listen Sie alle Dateien (keine Verzeichnisse, Links etc.) auf, die `config` heißen.


### `find` auf Zeitangaben und Dateiengrößen anwenden

Lesen und verstehen Sie die Unterabschnitte **Groesse** und **Alter** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Manchmal entstehen in Projekten leere Dateien – etwa versehentlich beim Kopieren oder
durch Programme, die unvollständig beendet wurden. Solche Dateien brauchen oft nur
unnötig Platz und können die Übersicht stören. Sie möchten deshalb prüfen, ob in Ihrem
Projekt leere Dateien existieren, um diese gezielt zu löschen oder zu überprüfen.  

[EC] Finden Sie alle Dateien mit einer Größe von 0 Bytes.

In Projekten ist es oft wichtig, den Überblick über aktuelle Änderungen zu behalten. 
Vielleicht wollen Sie die neuesten Dateien sichern, Änderungen überprüfen oder nach einem 
Fehler nachvollziehen, welche Dateien zuletzt verändert wurden.  
Zum Beispiel erinnern Sie sich, dass Sie irgendeine `apt`-Konfiguration nach der letzten
Änderung an `apt/sources.list` modifiziert hatten, die Sie jetzt erneut ändern möchten.
Aber welche war es?

[EC] Finden Sie alle Dateien (nicht Verzeichnisse) im Teilbaum `apt`, die jünger sind als `apt/sources.list`.


### Aktionen auf Dateien ausführen

Lesen und verstehen Sie die **Tabelle 5** aus dem Abschnitt **Aktionen** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Im Verzeichnisbaum liegen viele Konfigurationsdateien, die von verschiedenen 
Diensten genutzt werden. Oft möchte man sich einen Überblick verschaffen, welche 
Konfigurationsdateien existieren und welche Eigenschaften (z. B. Größe, Änderungsdatum 
oder Berechtigungen) sie haben. So können Sie leichter entscheiden, ob eine Datei 
überprüft, bearbeitet oder gesichert werden sollte.  

[EC] Finden Sie alle `*.conf`-Dateien im aktuellen Verzeichnisbaum und zeigen Sie deren 
Systeminformationen an. Kürzen Sie die Ausgabe mit `head -10` ab.


Leseen und verstehen Sie die **Tabelle 3a** aus dem Abschnitt **Suchkriterien** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie suchen unter den hunderten `*.conf`-Dateien eine, von der Sie nur noch wissen,
dass sie sehr tief verschachtelt lag; mindestens drei Ebenen tief (also auf Ebene 4,
mit 4 Schrägstrichen im relativen Dateinamen).
Sie suchen also alle diese, in der Hoffnung, dass es so wenige sind, dass Ihnen bei deren Anblick
der Name wieder einfällt. War es irgendwas mit "session"? Sie sind nicht sicher.

[EC] Finden Sie alle `*.conf`-Dateien, die auf Ebene 4 des Baums oder noch tiefer liegen.
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:find.prot]
[ENDINSTRUCTOR]

