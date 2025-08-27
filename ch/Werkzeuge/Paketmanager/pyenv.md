title: "pyenv: Python-Versionsverwaltung leicht gemacht"
stage: draft
timevalue: 1.5
difficulty: 2
---

[SECTION::goal::product]

Ich kann `pyenv` verwenden, um verschiedene Python-Versionen zu installieren und zu verwalten.

[ENDSECTION]

[SECTION::background::default]

Verschiedene Python-Projekte benötigen oft unterschiedliche Python-Versionen.
Während das System-Python meist nur eine Version bereitstellt, ermöglicht `pyenv`
die Installation und Verwaltung multipler Python-Versionen nebeneinander.

`pyenv` ist besonders nützlich für:

- Testing von Code gegen verschiedene Python-Versionen
- Arbeit an Projekten mit spezifischen Python-Anforderungen
- Verwendung aktueller Python-Versionen auf älteren Systemen
- Isolation verschiedener Python-Umgebungen

Mit `pyenv` können Sie Python-Versionen pro Projekt, pro Verzeichnis oder global festlegen,
ohne das System-Python zu beeinträchtigen.
Sicherlich haben Sie auch schon `venv`kennengelernt, dass anders als `pyenv` isolierte Umgebungen
erstellt. Falls nein, nutzen Sie mit [PARTREF::venv] die Gelegenheit das nachzuholen.

[ENDSECTION]

[SECTION::instructions::detailed]

Verwenden Sie bei Bedarf die [pyenv-Dokumentation](https://github.com/pyenv/pyenv).

### pyenv installieren

1. **macOS (Homebrew)**: `brew install pyenv`
   **Linux (Git-basiert)**:

   ```bash
   curl https://pyenv.run | bash
   ```

   **Ubuntu/Debian**:

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

Das ursprüngliche `pyenv` unterstützt Windows nicht direkt. Es gibt jedoch
**pyenv-win**, einen aktiv gepflegten Windows-Port mit ähnlicher Funktionalität.
pyenv-win kann über PowerShell, Chocolatey oder pip installiert werden und
bietet dieselben Kernfunktionen wie das Unix-pyenv.

Alternativ können Sie auch die direkte Installation verschiedener Python-Versionen
oder Conda verwenden, was jedoch weniger komfortabel in der Versionsverwaltung ist.
[ENDNOTICE]

2. Fügen Sie pyenv zu Ihrer Shell-Konfiguration hinzu (`.bashrc`, `.zshrc`):

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init -)"
   ```

3. [EC] Starten Sie eine neue Shell oder führen Sie `source ~/.bashrc` aus.
   Überprüfen Sie die Installation: `pyenv --version`

### Verfügbare Python-Versionen erkunden

1. [EC] Listen Sie alle installierbaren Python-Versionen auf: `pyenv install --list`
   Die Ausgabe ist sehr lang - verwenden Sie `grep` zur Filterung:
   `pyenv install --list | grep "3\.1[01]"`
2. [EC] Zeigen Sie aktuell installierte Versionen an: `pyenv versions`

### Python-Versionen installieren

1. Installieren Sie Python 3.10 (dauert einige Minuten):
   `pyenv install 3.10.12`
2. Installieren Sie Python 3.11:
   `pyenv install 3.11.5`
3. [EC] Überprüfen Sie Ihre installierten Versionen: `pyenv versions`

### Python-Versionen verwenden

1. [EC] Zeigen Sie die aktuell aktive Python-Version: `python --version`
2. [EC] Wechseln Sie global zu Python 3.10: `pyenv global 3.10.12`
   Überprüfen Sie: `python --version`
3. [EC] Erstellen Sie ein Testverzeichnis: `mkdir ~/pyenv_test && cd ~/pyenv_test`
4. [EC] Setzen Sie für dieses Verzeichnis Python 3.11: `pyenv local 3.11.5`
   Überprüfen Sie: `python --version`
5. [EQ] Verlassen Sie das Verzeichnis (`cd ~`) und prüfen Sie `python --version`.
   Was stellen Sie fest? Warum verhält sich das so?

### Projektspezifische Python-Version

1. Erstellen Sie ein neues Projekt-Verzeichnis:

   ```bash
   mkdir ~/python_project_demo
   cd ~/python_project_demo
   ```

2. [EC] Setzen Sie Python 3.10 für dieses Projekt: `pyenv local 3.10.12`
3. [EC] Überprüfen Sie, welche Datei pyenv erstellt hat: `ls -la`
   Was steht in der `.python-version` Datei? `cat .python-version`

### Virtual Environment mit pyenv

1. pyenv kann auch virtuelle Umgebungen verwalten. Installieren Sie das Plugin:
   **macOS**: `brew install pyenv-virtualenv`
   **Linux**: Meist bereits in pyenv enthalten, falls nicht:

   ```bash
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   ```

2. Fügen Sie zu Ihrer Shell-Konfiguration hinzu:

   ```bash
   eval "$(pyenv virtualenv-init -)"
   ```

3. [EC] Starten Sie eine neue Shell und erstellen Sie ein virtuelles Environment:
   `pyenv virtualenv 3.11.5 myproject-env`
4. [EC] Listen Sie Ihre Umgebungen auf: `pyenv versions`
   Wie unterscheiden sich die virtuellen Umgebungen von den Python-Installationen?
5. [EC] Aktivieren Sie das virtuelle Environment:
   `pyenv activate myproject-env`
   Was ändert sich in Ihrem Prompt?
6. [EC] Installieren Sie ein Test-Paket: `pip install requests`
7. [EC] Deaktivieren Sie das Environment: `pyenv deactivate`
   Versuchen Sie `python -c "import requests"` - funktioniert das noch?

### pyenv mit Projekten verwenden

1. Erstellen Sie ein Demo-Projekt:

   ```bash
   mkdir ~/flask_demo
   cd ~/flask_demo
   pyenv local myproject-env
   ```

2. [EC] Überprüfen Sie die aktive Umgebung: `pyenv version`
3. Erstellen Sie eine einfache Python-Datei `app.py`:

   ```python
   import sys
   import requests
   
   print(f"Python Version: {sys.version}")
   print(f"Requests installiert: {requests.__version__}")
   print("Hello from pyenv!")
   ```

4. [EC] Führen Sie das Skript aus: `python app.py`

### Aufräumen und Best Practices

1. [EQ] Welche Vorteile hat pyenv gegenüber der manuellen Installation verschiedener Python-Versionen?
2. [EQ] Wann würden Sie `pyenv global`, `pyenv local` oder `pyenv shell` verwenden?
3. [EC] Werfen Sie einen Blick auf die möglichen Pyenv-Befehle: `pyenv commands`

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

Zeigen Sie zusätzlich folgende Informationen:

- Ausgabe von `pyenv versions` (alle installierten Versionen)
- Inhalt der `.python-version` Datei in Ihrem Demo-Projekt
- Erfolgreiche Ausführung von `app.py` in der pyenv-Umgebung

[ENDSECTION]

[INSTRUCTOR::pyenv-Installation und -Verwendung]

### Installation (Schritte 1-3):

- `pyenv --version` zeigt Versionsnummer
- PATH-Variable enthält pyenv

### Python-Versionen (Schritte 4-8):

- `pyenv install --list` funktioniert
- Mindestens 2 Python-Versionen installiert
- `pyenv versions` zeigt installierte und aktive Version mit `*` an

### Versionswechsel (Schritte 9-13):

- `pyenv global` und `pyenv local` funktionieren
- `.python-version` Datei wird erkannt

### Virtual Environments (Schritte 17-23):

- pyenv-virtualenv Plugin installiert
- Virtuelles Environment erstellt und aktiviert
- Paket-Isolation funktioniert

### Projektintegration (Schritte 24-27):

- Projektspezifische Python-Version gesetzt
- Demo-Skript läuft erfolgreich
- Import von installierten Paketen funktioniert

[ENDINSTRUCTOR]
