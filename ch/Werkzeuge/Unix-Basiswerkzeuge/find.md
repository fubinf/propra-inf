title: find - Dateien auf dem System finden
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
requires: Dateibaum-beschaffen
---

[SECTION::goal::idea]
Ich verstehe wie find funktioniert und weiß wie ich damit Dateien finden kann.
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

`find` kann den gesamten Verzeichnisbaum durchsuchen und gezielt nach Dateiendungen
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

Lesen und verstehen Sie den Abschnitt **Pfadteile** und **Typ** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie haben gerade gelernt, wie man mit `find` sowohl Dateien als auch Verzeichnisse
finden kann. Oft ist es aber hilfreich, gezielt nur nach dem einen oder dem anderen zu
suchen.  

Stellen Sie sich vor, Sie haben ein großes Projekt und möchten alle Konfigurationsordner
ausfindig machen, um deren Inhalte zu überprüfen oder Skripte darauf anzuwenden – ohne
jeden Pfad einzeln kennen zu müssen.  

[EC] Listen Sie alle `config`-Verzeichnisse auf.  

Oder nehmen wir den Fall, dass Sie nur ganz bestimmte Dateien suchen möchten. Angenommen,
Sie wollen genau die Dateien finden, die `config` heißen, und dabei keine Verzeichnisse
oder Links berücksichtigen.  

[EC] Listen Sie alle Dateien (keine Verzeichnisse, Links etc.) auf, die `config` heißen.


### `find` auf Zeitangaben und Dateiengrößen anwenden

Lesen und verstehen Sie den Abschnitt **Groesse** und **Alter** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Manchmal entstehen in Projekten leere Dateien – etwa versehentlich beim Kopieren oder
durch Programme, die unvollständig beendet wurden. Solche Dateien brauchen oft nur
unnötig Platz und können die Übersicht stören. Sie möchten deshalb prüfen, ob in Ihrem
Projekt leere Dateien existieren, um diese gezielt zu löschen oder zu überprüfen.  

[EC] Finden Sie alle Dateien mit einer Größe von 0 Bytes.

In Projekten ist es oft wichtig, den Überblick über aktuelle Änderungen zu behalten. 
Vielleicht wollen Sie die neuesten Dateien sichern, Änderungen überprüfen oder nach einem 
Fehler nachvollziehen, welche Dateien zuletzt verändert wurden.  

[EC] Finden Sie alle Dateien, die innerhalb der letzten 24 Stunden geändert wurden.

Es ist in Ordnung wenn sie hier keine Ergebnisse bekommen, da die Daten schon etwas älter sind.

### Aktionen auf Dateien ausführen

Lesen und verstehen Sie die **Tabelle 5** aus dem Abschnitt **Aktionen** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Im Verzeichnisbaum liegen viele Konfigurationsdateien, die von verschiedenen 
Diensten genutzt werden. Oft möchte man sich einen Überblick verschaffen, welche 
Konfigurationsdateien existieren und welche Eigenschaften (z. B. Größe, Änderungsdatum 
oder Berechtigungen) sie haben. So können Sie leichter entscheiden, ob eine Datei 
überprüft, bearbeitet oder gesichert werden sollte.  

[EC] Finden Sie alle `.conf`-Dateien im aktuellen Verzeichnisbaum und zeigen Sie deren 
Systeminformationen an. Kürzen Sie die Ausgabe mit `head -10` ab.


Leseen und verstehen Sie die **Tabelle 3a** aus dem Abschnitt **Suchkriterien** von der 
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Im Verzeichnisbaum gibt es den Ordner `security`, in dem wichtige Konfigurationsdateien 
für Zugriffsrechte und Sicherheitsrichtlinien liegen. Sie möchten gezielt nur diese Dateien prüfen, 
ohne versehentlich Konfigurationen in tieferliegenden Unterordnern zu ändern.  

[EC] Finden Sie alle `.conf`-Dateien im Verzeichnis `security`, aber nicht in Unterverzeichnissen.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:find.prot]
[ENDINSTRUCTOR]

