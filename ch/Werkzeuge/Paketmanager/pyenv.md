title: "pyenv: Mehrere Python-Versionen nebeneinander benutzen"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: venv, curl
---

[SECTION::goal::product]
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

### pyenv installieren

`sudo apt update && sudo apt install pyenv`

[EC] Überprüfen Sie die Installation: `pyenv --version`

### Verfügbare Python-Versionen erkunden

1. [EC] Listen Sie alle installierbaren Python-Versionen auf: `pyenv install --list`
   Die Ausgabe ist sehr lang.
   Filtern Sie mit `grep` nach den Versionen 3.10 und 3.11:
   `pyenv install --list | grep "  3\.10\.\|  3\.11\."`

[HINT::Was bedeutet das grep-Muster?]
Das Muster `"  3\.10\.\|  3\.11\."` sucht nach Zeilen, die eine Versionsangabe
der Form `3.10.*` oder `3.11.*` enthalten (mit zwei führenden Leerzeichen).
Der Punkt im Versionsmuster ist durch `\.` als Literalpunkt maskiert
(sonst würde er für beliebige Zeichen stehen).
`\|` ist in grep das „oder“-Symbol.
Die zwei führenden Leerzeichen verhindern, dass Anaconda- oder PyPy-Einträge mit angezeigt werden.
[ENDHINT]

2. [EC] Zeigen Sie aktuell installierte Versionen an: `pyenv versions`
   Zu Beginn sehen Sie dort nur `system` (Ihr vorhandenes System-Python).
<!-- time estimate: 5 min -->

### Python-Versionen installieren

Suchen Sie sich aus der `pyenv install --list`-Ausgabe jeweils die neueste Patchversion von Python 3.10
und 3.11 heraus (also z. B. `3.10.17` und `3.11.12`) und installieren Sie beide
(jede Installation dauert einige Minuten):

1. [EC] `pyenv install 3.10.17`  _(Patchnummer ggf. anpassen)_
2. [EC] `pyenv install 3.11.12`  _(Patchnummer ggf. anpassen)_
3. [EC] Überprüfen Sie Ihre installierten Versionen: `pyenv versions`
<!-- time estimate: 15 min -->

### Python-Versionen verwenden

`pyenv` kennt drei Ebenen für die aktive Python-Version:

- `pyenv global <version>` – gilt systemweit als Standard
- `pyenv local <version>` – gilt im aktuellen Verzeichnis (und allen Unterverzeichnissen),
  gespeichert in einer Datei `.python-version` im Verzeichnis
- `pyenv shell <version>` – gilt nur in der aktuellen Shell-Sitzung, temporär ohne Datei

1. [EC] Zeigen Sie die aktuell aktive Python-Version: `python --version`
2. [EC] Wechseln Sie global zu Python 3.10: `pyenv global 3.10.17`  _(Patchnummer anpassen)_
   Überprüfen Sie: `python --version`
3. [EC] Erstellen Sie ein Testverzeichnis und wechseln Sie hinein:
   `mkdir ~/pyenv_test && cd ~/pyenv_test`
4. [EC] Setzen Sie für dieses Verzeichnis Python 3.11: `pyenv local 3.11.12`  _(Patchnummer anpassen)_
   Überprüfen Sie: `python --version`
5. [EC] Schauen Sie nach, welche Datei pyenv angelegt hat: `cat .python-version`
6. [EQ] Verlassen Sie das Verzeichnis mit `cd ~` und prüfen Sie `python --version`.
   Welche Version ist nun aktiv und warum?
<!-- time estimate: 15 min -->

### Überblick und Reflexion

1. [EQ] Sie haben soeben `pyenv global` und `pyenv local` ausprobiert.
   Wann im Entwicklungsalltag würden Sie welches verwenden?
   Wozu dient `pyenv shell` im Vergleich dazu?
2. [EQ] Werfen Sie einen Blick auf alle verfügbaren pyenv-Befehle: `pyenv commands`
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
