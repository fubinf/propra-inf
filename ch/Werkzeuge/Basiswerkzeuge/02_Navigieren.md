title: Navigieren in der Kommandozeile
stage: beta
timevalue: 1.0
difficulty: 2
assumes: 00_manpages
---

TODO_1: assume Shell-Wildcards und andere Shell-Grundlagen wie TAB.

[SECTION::goal::idea]
Ich weiß wie ich mit Befehlen auf der Kommandozeile navigieren kann.
[ENDSECTION]

[SECTION::background::default]
Ein Linux-Administrator bewegt sich hauptsächlich auf der Kommandozeile.
Das geht ganz anders als aus grafischen Oberflächen gewöhnt, aber für viele Zwecke
weitaus besser.
Wir machen hier die allerersten Gehversuche.
[ENDSECTION]

[SECTION::instructions::detailed]

### Grundlagen: Umgang mit Dateien

Lesen Sie in dieser
[Kommandoübersicht](https://bytescout.com/blog/most-used-linux-commands.html)
mindestens folgende Einträge: 
`cd, ls, man, cat, mkdir, rmdir, touch, rm, mv, echo, free, head, history, alias, df`.

Wenn Ihnen etwas seltsam vorkommt (und dafür gibt es eine Menge Anlass),
klären Sie es mit der passenden [PARTREFMANUAL::00_manpages::manpage] auf
und überfliegen Sie auch, welche [TERMREF2::Option::-en] es gibt.
Diese Webseite ist ein gutes Beispiel dafür, dass solche Fundstücke im Web
zwar oft recht praktisch, aber nicht immer auch zuverlässig sind.

Nicht wundern, nicht alle diese Kommandos (wohl aber alle der oben genannten) sind auf jedem
Unixsystem auch wirklich installiert.


### Ausprobieren!

- [EC] Listen Sie die Dateien in Ihrem `home`-Ordner.
- [EC] Geben Sie Ihre Dateien aus Ihrem `home`-Ordner in einer Listenansicht aus.
- [EC] Erstellen Sie nun einen Ordner namens `mydir`.
- [EC] Wechseln Sie in das oben erstellte Verzeichnis.
- [EC] Erstellen Sie in dem Verzeichnis eine leere Datei namens `myfile1`.
- [EC] Kopieren Sie die Datei `myfile1` ins `home`-Verzeichnis
- [EC] Benennen Sie die Datei `myfile1` im `mydir`-Ordner nach `myfile2` um.
- [EC] Wechseln Sie zurück in ihr `home`-Verzeichnis und erstellen Sie einen neuen Ordner namens `mydir2`. 
  Verschieben Sie alle Dateien (auch wenn da mehrere wären) aus `mydir` in den Ordner `mydir2`.
- [EC] Löschen Sie den Ordner `mydir`.
- [EC] Löschen sie den Ordner `mydir2`.

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
