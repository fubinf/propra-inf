title: Prompt und Navigation

#Prompt

Als Prompt (deutsch "Eingabeaufforderung") werden die Zeilen bezeichnet, die dem Benutzer der Shell signalisieren, dass er eine Eingabe tätigen kann. Üblicherweise handelt es sich hierbei um eine einzelne Zeile mit einer Reihe an Informationen, gefolgt von einem (ggf. blinkenden) Text-Cursor.

Informationen, die man in Prompts häufig findet, sind:

* Name des Benutzers
* Name des Computers
* Aktueller Pfad (`pwd` - present working dir)
* Superuser-Indikator

Selbst bei Shells, die standardmäßig auf nahezu alle Informationen im Prompt verzichten, existiert der Superuser-Indikator. Dieser ist das letzte Symbol vor dem Beginn der Benutzereingabe (außer gegebenenfalls Leerzeichen). Es gibt hier das `$` oder `%`, das bedeutet, dass man aktuell keine Superuser-Rechte hat, und das `#`, das Superuser-Rechte symbolisiert.

Das ist besonders wichtig, da man bei Anleitungen, die Shell-Befehle beinhalten, häufig diesen Indikator sehen kann. Findet man hier Befehle, die mit einem Indikator anfangen, sollte man zunächst einmal wissen, dass dieser nicht Teil des Befehls ist und daher auch nicht eingegeben/kopiert werden sollte, und außerdem, dass Befehle, denen ein `#` vorangestellt sind, nicht oder nicht vollständig funktionieren werden, wenn man nicht selbst Superuser-Rechte besitzt.

Es gibt je nach Shell noch eine Vielzahl an zusäztlich darstellbaren Informationen. Geläufig sind beispielsweise Informationen zu git oder einen Indikator darüber, ob der vorherige Befehl erfolgreich war oder nicht.

#Shellbenutzung

Es gibt Funktionen von Shells, die sehr nützlich sind, aber oft nicht bekannt sind oder selten benutzt werden.

* Tab Completion

    Ähnlich wie viele Programmierumgebungen bieten auch Shells die Möglichkeit, Vorschläge dafür zu liefern, was man eintippen möchte. Hierfür beginnt man, etwas zu zu schreiben, und drückt die Tab-Taste, um eine Vervollständigung oder Vorschläge für selbige zu erhalten.

    Üblich ist die Vervollständigung von Befehlen in beispielsweise `ec<tab>` aber auch von Dateien und Verzeichnissen in `ls /ho<tab>`.

    Weniger verbreitet und bekannt ist die Fähigkeit, auch Dinge wie SSH-Hosts oder Programm-Parameter zu vervollständigen. Die Shell `fish` ist hierfür in der Standardkonfiguration besonders weiträumig ausgestattet.

* Expansion

    Insbesondere bei der Handhabung von Datei- und Verzeichnispfaden kann es oft vorkommen, dass mehrere ähnliche Argumente für eine Anwendung gebraucht werden. Man kann sich hier sparen, diese immer wieder neu einzugeben, indem man mehrere unterschiedliche Wortteile durch Komma getrennt in geschweiften Klammern angibt.

    So ist beispielweise `echo 1{,2,34}5` äquivalent zu `echo 15 125 1345`. Mehrere Gruppen sind auch möglich und bilden ein Kreuzprodukt.

* History

    Shells verwalten üblicherweise eine Liste der eingegebenen Befehle, um auf diese später einfacher zugreifen zu können.

    Geläufig ist, dass man durch die Einträge dieser Liste einfach mit den Pfeiltasten hoch/runter navigieren kann. Es gibt Shells, die hierbei kontextabhängig agieren können. Das heißt, dass beispielsweise `cat <hoch>` nur Einträge aus der History anzeigt, die mit `cat` anfangen.

    Es gibt außerdem den Befehl `history`, der die Einträge dieser Liste durchnumeriert anzeigt. Was dieser Befehl sonst anbietet, ist abhängig von der jeweiligen Shell.

#Dateiverwaltung

Beim Starten einer Shell ist man häufig im Home-Verzeichnis des jeweiligen Benutzers, üblicherweise `/home/<Benutzername>`, auch zu finden in der Variable `$HOME` und dem Kürzel `~`. Ähnlich dazu gibt es beispielsweise auch `$PWD`, das das aktuelle Verzeichnis beinhaltet.

Zu den häufigen Befehlen der Dateiverwaltung zählen:

* `cd` (change directory) zum Wechseln des aktuellen Verzeichnisses
* `ls` (list) zur Anzeige des Inhalts eines Verzeichnisses
* `find` zum Suchen nach Dateien und Verzeichnissen
* `mkdir` (make directory) zum Erzeugen von Verzeichnissen
* `rmdir` (remove directory) zum Löschen von leeren(!) Verzeichnissen
* `touch` zum Erzeugen von Dateien (und Anpassen des letzten Bearbeitungszeitpunktes)
* `rm` (remove) zum Entfernen von Dateien oder Verzeichnissen
* `mv` (move) zum Verschieben von Dateien und Verzeichnissen
* `cp` (copy) zum Kopieren von Dateien und Verzeichnissen
* `cat` (concatenate) gibt den Inhalt von Dateien aus
* `less` (Nachfolger von more) zeigt den Inhalt einer Datei in einer interaktiven Anwendung an
* `echo` gibt einen Text aus

Es gibt einige Anwendungen, die Dateiverwaltung komfortabler gestalten können, darunter u.A. `z`, den Midnight Commander und Ranger.

Für Informationen zu den jeweiligen Befehlen, kann man man in der jeweiligen sogenannten Manpage nachschauen. Zu finden üblicherweise mit dem Befehl `man <Befehl>`.

!resources
