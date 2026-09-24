title: "pyenv: Mehrere Python-Versionen nebeneinander benutzen"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: venv
---

[SECTION::goal::experience]
Ich kann `pyenv` verwenden, um verschiedene Python-Versionen zu installieren und zu verwalten.
[ENDSECTION]


[SECTION::background::default]
Verschiedene Python-Projekte benötigen manchmal unterschiedliche Python-Versionen.
Wenn man selbst eine Bibliothek veröffentlichen möchte, sollte man deren Kompatibilität mit
möglichst vielen Python-Versionen durch entsprechende Tests sicherstellen.
Aber in Debian ist normalerweise immer nur eine einzige Python-Version verfügbar.
Also wie löst man das?
`pyenv` ermöglicht die Installation und Verwaltung mehrerer Python-Versionen nebeneinander.

Im Gegensatz zu `venv`, das Sie aus [PARTREF::venv] kennen, verwaltet `pyenv` nicht
getrennte Paketumgebungen zur gleichen Python-Version, sondern die Python-Version selbst.

Es stehen Hunderte von Versionen zur Verfügung, nicht nur von der Standardimplementierung CPython,
sondern auch von anderen wie
PyPy (mit Just-in-Time-Compiler) oder
MicroPython (für Mikrocontroller).
[ENDSECTION]


[SECTION::instructions::detailed]
Verwenden Sie bei Bedarf die
[pyenv Command Reference](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md).

### `pyenv` installieren und einrichten

`sudo apt update && sudo apt install pyenv`

[EC] Überprüfen Sie die Installation: `pyenv --version`

`pyenv` arbeitet mit sogenannten _Shims_: kleinen Platzhalterprogrammen namens `python`, `python3`, `pip` usw.
im Verzeichnis `~/.pyenv/shims`.
Steht dieses Verzeichnis im `PATH` vor dem System-Python, landet jeder Aufruf von `python` beim Shim,
und der ruft die gerade gewählte Python-Version auf.

Außerdem braucht `pyenv` eine Shellfunktion gleichen Namens:
`pyenv shell` und `pyenv rehash` müssen den Zustand der laufenden Shell verändern
(Umgebungsvariablen bzw. den Befehls-Cache).
Das kann das Programm `pyenv` nicht, denn als Kindprozess kann es die Umgebung seiner Shell nicht ändern.

Beides richtet `pyenv init` ein.
Es gibt die nötigen Shell-Befehle aus, und `eval` führt sie in der aktuellen Shell aus.

[EC] Tragen Sie den Aufruf in Ihre `~/.bashrc` ein und laden Sie sie neu:
`echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc && source ~/.bashrc`

[HINT::Ich benutze `zsh` statt `bash`]
Verwenden Sie `~/.zshrc` statt `~/.bashrc` und `pyenv init - zsh` statt `pyenv init - bash`.
[ENDHINT]

[EC] Prüfen Sie die Einrichtung: `type pyenv` sollte melden, dass `pyenv` eine Shellfunktion ist,
und `echo $PATH` sollte `~/.pyenv/shims` ganz vorn enthalten.
<!-- time estimate: 10 min -->

### Verfügbare Python-Versionen erkunden

Lesen Sie in der Command Reference die Abschnitte zu
[`pyenv install`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-install),
[`pyenv versions`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-versions) und
[`pyenv latest`](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-latest).

1. [EC] Lassen Sie sich alle installierbaren Versionen von CPython 3.10 und 3.11 anzeigen.

[HINT::Die Liste ist viel zu lang]
Filtern Sie die Ausgabe mit `grep`.

[HINT::Welches `grep`-Muster brauche ich?]
`pyenv install --list | grep "  3\.10\.\|  3\.11\."`

Der Punkt ist durch `\.` als Literalpunkt maskiert (sonst stünde er für ein beliebiges Zeichen).
`\|` ist in `grep` das „oder“-Symbol.
Die zwei führenden Leerzeichen verhindern, dass Anaconda- oder PyPy-Einträge mit angezeigt werden.
[ENDHINT]
[ENDHINT]

2. [EC] Ermitteln Sie mit einem einzigen Befehl die neueste bekannte Patchversion von Python 3.10
   und ebenso von 3.11.
3. [EC] Zeigen Sie die aktuell installierten Versionen an.
   Zu Beginn sehen Sie dort nur `system` (Ihr vorhandenes System-Python).
<!-- time estimate: 10 min -->

### Python-Versionen installieren

1. [EC] Installieren Sie die neuesten Patchversionen von Python 3.10 und 3.11
   (jede Installation dauert einige Minuten, weil Python dabei aus dem Quellcode übersetzt wird).
2. [EC] Überprüfen Sie Ihre installierten Versionen.

[HINT::Muss ich die volle Versionsnummer angeben?]
Nein. Lesen Sie im Abschnitt zu `pyenv install` nach, was bei Angabe eines Präfixes wie `3.10` passiert.
[ENDHINT]
<!-- time estimate: 15 min -->

### Python-Versionen verwenden

`pyenv` kennt drei Ebenen für die aktive Python-Version:

- `pyenv global <version>` – gilt als Standard für Ihren Benutzer
- `pyenv local <version>` – gilt im aktuellen Verzeichnis (und allen Unterverzeichnissen),
  gespeichert in einer Datei `.python-version` im Verzeichnis
- `pyenv shell <version>` – gilt nur in der aktuellen Shell-Sitzung, temporär ohne Datei

Geben Sie dabei jeweils die volle Versionsnummer an, wie `pyenv versions` sie anzeigt.

1. [EC] Zeigen Sie die Version Ihres System-Pythons: `python3 --version`
2. [EC] Probieren Sie nun `python --version`.
   Debian liefert kein Kommando `python` (nur `python3`), aber Ihre `pyenv`-Versionen tun es.
   Die Meldung des Shims sagt Ihnen, wo es `python` gibt.
3. [EC] Stellen Sie Python 3.10 als globale Version ein und prüfen Sie mit `python --version`.
4. [EC] Erstellen Sie ein Testverzeichnis `~/pyenv_test` und wechseln Sie hinein.
5. [EC] Stellen Sie für dieses Verzeichnis Python 3.11 ein und prüfen Sie mit `python --version`.
6. [EC] Schauen Sie nach, welche Datei `pyenv` angelegt hat und was darin steht.
7. [EQ] Verlassen Sie das Verzeichnis mit `cd ~` und prüfen Sie `python --version`.
   Welche Version ist nun aktiv und warum?
8. [EC] Stellen Sie (weiterhin in `~`) nur für die aktuelle Shell Python 3.11 ein
   und prüfen Sie mit `python --version`.
9. [EC] Öffnen Sie ein neues Terminalfenster und prüfen Sie dort erneut `python --version`.
<!-- time estimate: 20 min -->

### Überblick und Reflexion

1. [EQ] Sie haben soeben `pyenv global`, `pyenv local` und `pyenv shell` ausprobiert.
   Wann im Entwicklungsalltag würden Sie welches verwenden?
2. [EQ] Werfen Sie einen Blick auf alle verfügbaren `pyenv`-Befehle: `pyenv commands`
   Welchen Befehl finden Sie warum hilfreich?

<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::trace,reflection]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::pyenv-Installation und -Verwendung]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
