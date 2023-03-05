title: GitLab-Repo anlegen und klonen 
description: |
  Basis-Umgang mit GitLab
timevalue: 1.0
difficulty: 1
---
<!-- Problem: Wenn ich erst GitLab, dann Git101 erkläre, dann weiß der User noch nicht, wie man die Dateien hochläd. Wenn ich erst Git101, dann GitLab erkläre, dann hat der User noch kein Repo zum hochpushen.
Lösung 1: Git101 splitten in Git101 - lokal und Git101 - RepoStuff, GitLab dazwischensetzen
Lösung 2: Abgabe für GitLab über den Editor von GitLab einfügen -->
GitLab ist, genauso wie GitHub, "eine Webanwendung zur Versionsverwaltung für Softwareprojekte auf
Git-Basis" (Quelle: [Wikipedia](https://de.wikipedia.org/wiki/GitLab)). Über solche Webanwendungen
kann man unter anderem

- mehrere Repos verwalten,
- Code-Reviews durchführen,
- den eigenen Code öffentlich (oder auch nur bestimmten Nutzern) verfügbar machen,
- Continuous Integragion und Continuous Delivery (CI/CD) einrichten und durchführen,

In dieser Aufgabe liegt der Fokus auf dem Login auf der GitLab-Instanz des
<!--dept-->Fachbereichs Mathematik und Informatik der freien Universität Berlin, das
Erstellen des ersten Repos und wie man dann damit auf dem eigenen Rechner arbeitet.

## GitLab-Repo anlegen

Rufen Sie die Webseite der [GitLab-Instanz](https://git.imp.fu-berlin.de/) des
<!--dept-->Fachbereichs Mathematik und Informatik der Freien Universität Berlin auf und
melden Sie sich mit ihren ZEDAT-Zugangsdaten an.

<!-- TODO: Warum ist das ein Hint? Warum nicht eine Info? -->
[HINT::Ein erster Blick aufs User Interface]
In der Mitte der Webseite sehen Sie eine Auflistung ihrer Projekte, das _Dashboard_. 
Wenn Sie sich zum ersten Mal hier einloggen, ist die Liste vermutlich noch leer.

Oben links finden Sie drei Elemente, von links nach rechts: 
1. Das GitLab-Logo bringt Sie jederzeit zum Dashboard zurück. 
2. Das Icon daneben erlaubt es Ihnen, schnell zwischen Projekten, Gruppen und weiteren
    Funktionen von GitLab zu wechseln.
3. Das letzte Element ist eine Suche, mit der Sie Benutzer, Projekte oder auch Ihnen
    zugewiesene Aufgaben wie "Issues" oder "Merge Requests" suchen können.

<!-- TODO: Bin kein Fan, die Symbole nach Reihenfolge zu benennen. Besser wären mindestens Symbole -->
Oben rechts finden Sie sechs weitere Elemente, wieder von links nach rechts: 
1. Das Plus-Symbol erlaubt es Ihnen, schnell neue Projekte oder Gruppen zu eröffnen.
2. Als zweites finden Sie alle Ihnen zugewiesenen Issues.
3. Als drittes finden Sie alle Merge Requests, die mit Ihnen in Verbindung stehen.
4. Als viertes finden Sie eine To-Do-List.
5. Das fünfte Element führt zu den Hilfe-Elementen von GitLab.
6. Das letzte Element führt Sie zu Ihren Account-Einstellungen.
[ENDHINT]

Klicken Sie im Dashboard auf "New Project", danach auf "Create blank project".
Der "Project name" soll für dieses Programmierpraktikum ein bestimmtes Format haben.
Achten Sie darauf, dass Sie das Semester richtig angeben, beispielsweise "propra-sose2028"
für das SoSe 2028 bzw. "propra-wise2028" für das WiSe 2028/2029. 
Bei "Project URL" wählen Sie unter "Pick a group or namespace" Ihren Benutzernamen aus, den
"Project slug" lassen Sie unverändert.
Das "Visibility Level" muss "Private" sein.
Entfernen Sie zuletzt den Haken bei "Initialize repository with a README" und erstellen Sie
dann das Projekt. <!-- TODO: Warum ohne? -->

Wenn Sie den Schritten genau gefolgt sind, haben Sie jetzt Ihr leeres GitLab-Projekt vor sich.
Eine Einstellung fehlt für das Programmierpraktikum noch.
Damit die Tutor\_innen später Ihre Abgaben bewerten können, benötigen diese noch Schreibrechte.
Klicken Sie auf "Invite members" und fügen Sie alle Tutor\_innen mit der Rolle "Maintainer" hinzu.
Sie finden in der Datei [sedrila.yaml](sedrila.yaml) die Namen und Accountnamen der Tutor\_innen
dieses Kurses unter dem Eintrag "instructors". 

## `git clone`

Damit Sie lokal auf Ihrem Rechner in Ihrem GitLab-Projekt arbeiten können, müssen Sie jetzt das
Projekt _klonen_.
Dabei laden Sie eine exakte Kopie des Repos herunter. 
Zwar liegen aktuell keine Dateien in ihren Repo, allerdings weiß Git so direkt, wo das
GitLab im Internet zu erreichen ist.

Klonen Sie mit dem folgenden Befehl das Git-Repo. Achten Sie darauf, bei `USERNAME` ihren
GitLab-Nutzernamen und bei `PROJECTNAME` den Namen ihres GitLab-Projektes anzugeben:

    ```bash
       git clone https://git.imp.fu-berlin.de/USERNAME/PROJECTNAME.git
    ```

Sie werden nun nach Ihrem Benutzernamen und daraufhin nach Ihrem Passwort gefragt. Das liegt daran,
dass das Projekt den Visibility Level "Private" hat. 
Wenn Sie bis hierhin alles richtig gemacht haben, wird Ihnen in ihrem Terminal eine Warnung
angezeigt: "warning: You appear to have cloned an empty repository."


<!-- TODO: Warum ist das ein Hint? -->
[HINT::Anmeldung mit `ssh`-Schlüssel statt User Credentials]
TODO: Verweis auf andere Aufgabe setzen.
[ENDHINT]

!!! submission "Abgabe"
    Kopieren Sie die Ausgaben des Terminals nach dem Klonen Ihres Repos und nach `git remote -v` inklusive der Befehle.

    Laden Sie diese Markdown-Datei auf ihr hier erstelltes GitLab-Repo hoch.

- (clone erklären)
- `clone`
- `git remote -v`

!!! instructor
    - Sichtbarkeit "privat" prüfen
    - Schreibrechte aller Tutor\_innen prüfen
