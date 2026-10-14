title: find - Dateien auf dem System wiederfinden
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Umgang-mit-Verzeichnissen, redirect
requires: Dateibaum-beschaffen
---

[SECTION::goal::idea]
Ich verstehe, wie `find` funktioniert, und weiß, wie ich damit Dateien finden kann.
[ENDSECTION]


[SECTION::background::default]
Das Kommando `find` durchsucht Verzeichnisbäume.
Als Suchkriterien kann man beispielsweise Namen, Dateitypen, Änderungszeiten oder Berechtigungen angeben.
Die gefundenen Dateien kann `find` bearbeiten oder (meistens) einfach ihre Pfadnamen ausgeben.
[ENDSECTION]


[SECTION::instructions::detailed]
[EC] Wechseln Sie in das Verzeichnis Ihres [TERMREF2::Hilfsbereich::-s], in dem der Dateibaum entpackt wurde.

Lesen und verstehen Sie die Synopsis der
[find(1) Manpage](https://manpages.debian.org/stable/findutils/find.1.en.html).
Nutzen Sie die Manpage als Plan B, falls in den anderen Quellen etwas nicht klar genug wird.

Lesen und verstehen Sie den Abschnitt **Name** auf der
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

[FOLDOUT::Abweichungen unter macOS]
macOS bringt ein BSD-`find` mit, nicht das GNU-`find` von Debian.
Die oben verlinkte Manpage und die ubuntuusers-Seite beschreiben das GNU-`find`.
Für diese Aufgabe reicht das BSD-`find`, aber beachten Sie zwei Unterschiede:

- Das BSD-`find` verlangt immer einen Startpfad.
  `find -name x` bricht mit `illegal option` ab.
  Schreiben Sie stattdessen `find . -name x`.
- Einige GNU-Optionen fehlen, z. B. `-printf` und `-daystart`.
  Welche Optionen es gibt, steht in `man find`.

Wer trotzdem das GNU-`find` möchte: `brew install findutils`.
Es heißt danach `gfind`.
[ENDFOLDOUT]


### `find` auf Dateien und Verzeichnisse anwenden

Sie untersuchen ein Linux-System, bei dem die Passwortregeln für Benutzerkonten angepasst werden sollen.
Ein Kollege erzählt Ihnen, dass diese Regeln nicht in `/etc/shadow` oder `/etc/login.defs` stehen,
sondern in einer Konfigurationsdatei im Verzeichnisbaum von `pam.d/`.
Er ist sich sicher, dass die Datei `common-password` heißt, weiß aber nicht mehr genau, wo sie liegt.
Statt die vielen Konfigurationsdateien in `pam.d/` einzeln durchzusehen, lassen Sie `find` suchen.

[EC] Finden Sie die Datei `common-password`.

Sie arbeiten an einem Projekt, in dessen Unterverzeichnissen viele Python-Skripte verstreut liegen.
Für eine Übersicht wollen Sie alle `.py`-Dateien finden, ohne jedes Verzeichnis einzeln zu durchsuchen.

[EC] Finden Sie alle Python-Dateien, die auf `.py` enden, im aktuellen Verzeichnis und
allen Unterverzeichnissen.

In vielen Projekten entstehen temporäre Dateien mit unterschiedlich geschriebener Endung,
z. B. `.tmp`, `.TMP` oder `.Tmp`.
Eine Suche nach exakt `.tmp` würde einen Teil davon übersehen.
Probieren Sie das Prinzip am Namen `default` aus.

[EC] Finden Sie alle Dateien, die `default` heißen, egal ob Groß- oder
Kleinschreibung.

Lesen und verstehen Sie die Unterabschnitte **Pfad** und **Typ** auf der
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Bisher hat `find` Dateien und Verzeichnisse gleichermaßen gefunden.
Oft möchte man aber nur nach dem einen oder dem anderen suchen.

Angenommen, Sie möchten in einem großen Projekt alle Konfigurationsverzeichnisse namens `config` finden,
um deren Inhalte zu überprüfen.
Sie wissen, dass es daneben auch Dateien namens `config` gibt, möglicherweise viele.
Die sollen nicht in der Ausgabe erscheinen.

[EC] Listen Sie alle `config`-Verzeichnisse auf (aber nicht Dateien namens `config`).

Dann fällt Ihnen auf, dass es genau andersherum war.
Sie brauchen die Dateien namens `config` und nicht die Verzeichnisse.

[EC] Listen Sie alle Dateien (keine Verzeichnisse, Links etc.) auf, die `config` heißen.


### `find` auf Zeitangaben und Dateigrößen anwenden

Lesen und verstehen Sie die Unterabschnitte **Größe** und **Alter** auf der
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Leere Dateien entstehen manchmal versehentlich, etwa beim Kopieren oder wenn ein Programm abbricht.
Sie stören die Übersicht.
Sie möchten deshalb prüfen, ob es in Ihrem Projekt leere Dateien gibt.

[EC] Finden Sie alle Dateien mit einer Größe von 0 Bytes.

Sie erinnern sich, dass Sie nach der letzten Änderung an `apt/sources.list` noch eine weitere
`apt`-Konfigurationsdatei geändert haben.
Die möchten Sie jetzt erneut bearbeiten, wissen aber nicht mehr, welche es war.

[EC] Finden Sie alle Dateien (nicht Verzeichnisse) im Teilbaum `apt`, die jünger sind als `apt/sources.list`.


### Aktionen auf Dateien ausführen

Lesen und verstehen Sie die **Tabelle 5** aus dem Abschnitt **Aktionen** auf der
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Im Verzeichnisbaum liegen viele Konfigurationsdateien, die von verschiedenen Diensten genutzt werden.
Oft möchte man sich einen Überblick verschaffen, welche Konfigurationsdateien existieren
und welche Eigenschaften (z. B. Größe, Änderungsdatum oder Berechtigungen) sie haben.
So können Sie leichter entscheiden, ob eine Datei überprüft, bearbeitet oder gesichert werden sollte.

[EC] Finden Sie alle `*.conf`-Dateien im aktuellen Verzeichnisbaum und zeigen Sie deren
Systeminformationen an.
Kürzen Sie die Ausgabe mit `head -10` ab.


Lesen und verstehen Sie die **Tabelle 3a** aus dem Abschnitt **Suchkriterien** auf der
[ubuntuusers find-Seite](https://wiki.ubuntuusers.de/find/).

Sie suchen unter den hunderten `*.conf`-Dateien eine, von der Sie nur noch wissen,
dass sie sehr tief verschachtelt lag; mindestens drei Ebenen tief (also auf Ebene 4,
mit 4 Schrägstrichen im relativen Dateinamen).
Sie suchen also alle diese, in der Hoffnung, dass es so wenige sind, dass Ihnen bei deren Anblick
der Name wieder einfällt.
War es irgendwas mit "session"?
Sie sind nicht sicher.

[EC] Finden Sie alle `*.conf`-Dateien, die auf Ebene 4 des Baums oder noch tiefer liegen.
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll]
[PROT::ALT:find.prot]
[ENDINSTRUCTOR]
