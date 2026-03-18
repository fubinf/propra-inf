title: "pyenv: Python-Versionsverwaltung leicht gemacht"
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: venv
---

[SECTION::goal::product]

Ich kann `pyenv` verwenden, um verschiedene Python-Versionen zu installieren und zu verwalten.

[ENDSECTION]

[SECTION::background::default]

Verschiedene Python-Projekte benötigen oft unterschiedliche Python-Versionen.
Während das System-Python meist nur eine Version bereitstellt, ermöglicht `pyenv`
die Installation und Verwaltung multipler Python-Versionen nebeneinander.

`pyenv` ist besonders nützlich für:

- Testen von Code gegen verschiedene Python-Versionen
- Arbeit an Projekten mit spezifischen Python-Anforderungen
- Verwendung aktueller Python-Versionen auf älteren Systemen

Mit `pyenv` können Sie Python-Versionen pro Projekt, pro Verzeichnis oder global festlegen,
ohne das System-Python zu beeinträchtigen.
Im Gegensatz zu `venv`, das Sie aus [PARTREF::venv] kennen, verwaltet `pyenv` nicht
Paketumgebungen, sondern die Python-Version selbst.

[ENDSECTION]

[SECTION::instructions::detailed]

Verwenden Sie bei Bedarf die
[pyenv Command Reference](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md).

### pyenv installieren

1. Installieren Sie `pyenv` passend zu Ihrem Betriebssystem:

   **macOS (Homebrew)**: `brew install pyenv`

   **Linux (alle Distributionen)**:

   ```bash
   curl https://pyenv.run | bash
   ```

   **Ubuntu/Debian (Alternative mit Systemabhängigkeiten)**:

   ```bash
   sudo apt update
   sudo apt install -y make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
   libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
   liblzma-dev python3-openssl git
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   ```

[NOTICE]
**Und was ist mit Windows?**

Das ursprüngliche `pyenv` unterstützt Windows nicht direkt.
Es gibt jedoch `pyenv-win`, einen aktiv gepflegten Windows-Port mit ähnlicher Funktionalität.
`pyenv-win` kann über PowerShell, Chocolatey oder pip installiert werden und
bietet dieselben Kernfunktionen wie das originale `pyenv`.
[ENDNOTICE]

2. Fügen Sie `pyenv` zu Ihrer Shell-Konfiguration hinzu.
   Finden Sie zunächst heraus, welche Shell Sie verwenden: `echo $SHELL`

   Öffnen Sie dann die passende Konfigurationsdatei in einem Texteditor:
   - Bei **bash**: `~/.bashrc`
   - Bei **zsh**: `~/.zshrc`

   Fügen Sie am Ende der Datei folgende drei Zeilen ein:

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init -)"
   ```

3. [EC] Laden Sie die Konfiguration neu – entweder durch Öffnen einer neuen Shell oder durch:
   - bash: `source ~/.bashrc`
   - zsh: `source ~/.zshrc`

   Überprüfen Sie die Installation: `pyenv --version`

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
`\|` ist in grep das „oder"-Symbol.
Die zwei führenden Leerzeichen verhindern, dass Anaconda- oder PyPy-Einträge mitangezeigt werden.
[ENDHINT]

1. [EC] Zeigen Sie aktuell installierte Versionen an: `pyenv versions`
   Zu Beginn sehen Sie dort nur `system` (Ihr vorhandenes System-Python).

### Python-Versionen installieren

Suchen Sie sich aus der `pyenv install --list`-Ausgabe jeweils die neueste Patchversion von Python 3.10
und 3.11 heraus (also z. B. `3.10.17` und `3.11.12`) und installieren Sie beide
(jede Installation dauert einige Minuten):

1. [EC] `pyenv install 3.10.17`  _(Patchnummer ggf. anpassen)_
2. [EC] `pyenv install 3.11.12`  _(Patchnummer ggf. anpassen)_
3. [EC] Überprüfen Sie Ihre installierten Versionen: `pyenv versions`

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

### Überblick und Reflexion

1. [EQ] Sie haben soeben `pyenv global` und `pyenv local` ausprobiert.
   Wann im Entwicklungsalltag würden Sie welches verwenden?
   Wozu dient `pyenv shell` im Vergleich dazu?
2. [EC] Werfen Sie einen Blick auf alle verfügbaren pyenv-Befehle: `pyenv commands`

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::pyenv-Installation und -Verwendung]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
