title: GitLab-Repo anlegen und klonen 
description: |
  Wir legen das Repo auf dem Server an, vergeben Rechte und koppeln es mit einer
  Kopie auf dem eigenen Rechner.
timevalue: 1.0
difficulty: 1
---
<!-- Problem: Wenn ich erst GitLab, dann Git101 erkläre, dann weiß der User noch nicht, wie man die Dateien hochläd. Wenn ich erst Git101, dann GitLab erkläre, dann hat der User noch kein Repo zum hochpushen.
Lösung 1: Git101 splitten in Git101 - lokal und Git101 - RepoStuff, GitLab dazwischensetzen
Lösung 2: Abgabe für GitLab über den Editor von GitLab einfügen -->
GitLab ist, genauso wie GitHub, "eine Webanwendung zur Versionsverwaltung für Softwareprojekte auf
Git-Basis" (Quelle: [Wikipedia](https://de.wikipedia.org/wiki/GitLab)). Über solche Webanwendungen
kann 

- mehrere `git` Repositories verwalten,
- Code Reviews durchführen,
- bei Bedarf den eigenen Code öffentlich (oder auch nur bestimmten Nutzern) verfügbar machen,
- Continuous Integragion und Continuous Delivery (CI/CD) einrichten und durchführen,

und vieles mehr.
In dieser Aufgabe dreht sich erstmal alles um den ersten Login auf der GitLab-Instanz des
Fachbereichs Mathematik und Informatik, das Erstellen des ersten Repositories und wie man dann damit
auf dem eigenen Rechner arbeitet.

## GitLab-Repo anlegen

Rufen Sie die Webseite der [GitLab-Instanz](https://git.imp.fu-berlin.de/) des Fachbereichs auf und
melden Sie sich mit ihren ZEDAT-Accountdaten an.

[HINT::Ein erster Blick aufs User Interface]
In der Mitte der Webseite sehen Sie eine Auflistung ihrer Projekte, das _Dashboard_. 
Wenn Sie sich zum ersten mal hier einloggen, stehen die Chancen gut, dass die Liste noch leer ist.

Oben links finden Sie drei Elemente, von links nach rechts: 
Das GitLab-Logo bringt Sie jederzeit zum Dashboard zurück. 
Das Icon daneben erlaubt es Ihnen schnell zwischen Projekten und Gruppen und weiteren Funktionen von
GitLab zu wechseln.  
Das letzte Element ist eine Suche, mit der Sie Benutzer, Projekte  oder auch Ihnen zugewiesene
Aufgaben wie Issues oder Merge Requests suchen können.

Oben rechts finden Sie sechs weitere Elemente, wieder von links nach rechts: 

Das Plus-Symbol erlaubt es Ihnen schnell neue Projekte oder Gruppen zu eröffnen.
Als zweites finden Sie alle Ihnen zugewiesenen Issues.
Als drittes finden Sie alle Merge Requests, die mit Ihnen in Verbindung stehen.
Als viertes finden Sie eine To-Do-List.
Das fünfte Element führt zu den Hilfe-Elementen von GitLab. Hilfe, Support, Keyboard Shortcuts,...
Das letzte Element führt Sie zu Ihren Account-Einstellungen. Hier können Sie Ihr Profil und Ihre Einstellungen ändern.
[ENDHINT]

Klicken Sie im Dashboard auf `New Project`, danach auf `Create blank project`.
Der _Project name_ soll für dieses Programmierpraktikum ein bestimmtes Format haben.
Achten Sie darauf, dass Sie das Semester richtig angeben, z. B. `propra-sose2028` für das SoSe 2028
bzw. `propra-wise2028` für das WiSe 2028/2029. 
Bei _Project URL_ wählen Sie unter `Pick a group or namespace` ihren Benutzernamen aus, den _Project
slug_ lassen Sie unverändert.
Das _Visibility Level_ muss `Private` sein.
Entfernen Sie zuletzt den Haken bei `Initialize repository with a README` und erstellen Sie dann das
Projekt. 

Wenn Sie den Schritten genau gefolgt sind, werden Sie jetzt von ihrem leeren GitLab-Projekt begrüßt.
Eine Einstellung fehlt für das Programmierpraktikum noch.
Damit die Tutor\_innen später Ihre Abgaben bewerten können, benötigen diese noch Schreibrechte.
Klicken Sie auf `Invite members` und fügen Sie alle Tutor\_innen mit der Rolle `Maintainer` hinzu.
Sie finden in der Datei [_sedrila.yaml](_sedrila.yaml) die Namen und Accountnamen der Tutor\_innen
dieses Kurses unter dem Eintrag `instructors`. 

## `git clone`

Damit Sie lokal auf ihrem Rechner in Ihrem GitLab-Projekt arbeiten können, müssen Sie jetzt das
Projekt _klonen_.
Dabei laden Sie eine exakte Kopie des Repositories herunter. 
Zwar liegen aktuell keine Dateien in ihren Repository, allerdings weiß `git` so direkt, wo das
GitLab im Internet zu erreichen ist.

Klonen Sie mit dem folgenden Befehl das `git`-Repository. Achten Sie darauf, bei `USERNAME` ihren
GitLab-Nutzernamen und bei `PROJECTNAME` den Namen ihres GitLab-Projektes anzugeben:

    ```bash
       git clone https://git.imp.fu-berlin.de/USERNAME/PROJECTNAME.git
    ```

Sie werden nun nach Ihrem Benutzernamen und daraufhin nach Ihrem Passwort gefragt. Das liegt daran,
dass das Projekt den Visibility Level `Private` hat. 
Wenn Sie bis hierhin alles richtig gemacht haben, wird Ihnen in ihrem Terminal eine Warnung
angezeigt: `warning: You appear to have cloned an empty repository.`


[HINT::Anmeldung mit `ssh`-Schlüssel statt User Credentials]
TODO: Verweis auf andere Aufgabe setzen.
[ENDHINT]

!!! submission "Abgabe"
    Kopieren Sie die Ausgaben des Terminals nach dem Klonen Ihres Repositories und nach `git remote -v` inkl. der Befehle, speichern Sie diese in einer Markdown-Datei.

    Laden Sie diese Markdown-Datei auf ihr hier erstelltes GitLab-Repository hoch.

- (clone erklären)
- `clone`
- `git remote -v`

!!! instructor
    - Sichtbarkeit "privat" prüfen
    - Schreibrechte aller Tutor_innen prüfen
