title: Django django-admin Kommandozeilen-Tool
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: django-basics, django-project
---

[SECTION::goal::idea,experience]
Ich kann das `django-admin` Kommandozeilen-Tool verwenden, um Django-Projekte zu erstellen, 
zu verwalten und grundlegende Verwaltungsaufgaben durchzuführen.
[ENDSECTION]

[SECTION::background::default]
Django-Projekte bestehen aus vielen Dateien und haben eine komplexe Struktur.
Das manuelle Erstellen aller benötigten Dateien und Konfigurationen wäre zeitaufwendig 
und fehleranfällig.
Das `django-admin` Tool automatisiert diese Aufgaben und stellt eine einheitliche 
Schnittstelle für alle wichtigen Projektverwaltungsaufgaben bereit.
[ENDSECTION]

[SECTION::instructions::detailed]

### Django Installation und erste Schritte

Bitte lesen Sie zunächst [PARTREF::django-basics] und folgen Sie den dort beschriebenen 
Schritten, um Django in einer virtuellen Umgebung erfolgreich zu installieren. 
Damit verfügen Sie über eine saubere Arbeitsumgebung für die folgenden Aufgaben.  

[EC] Überprüfen Sie die Installation mit `django-admin --version`.
<!-- EC1 -->

### Verfügbare Kommandos anzeigen: `help`

Das `django-admin` Tool bietet viele verschiedene Kommandos für unterschiedliche Aufgaben.
Um eine Übersicht aller verfügbaren Kommandos zu erhalten, verwenden Sie:

```bash
django-admin help
```

Für detaillierte Hilfe zu einem spezifischen Kommando:

```bash
django-admin help <kommando>
```

Die Ausgabe zeigt Ihnen alle verfügbaren Unterkommandos an:

```
Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    shell
    showmigrations
    startapp
    startproject
    test
    ...
```

Optional: weitere Informationen zu allen verfügbaren Kommandos finden Sie in der 
[Django Management Commands Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/).

<!-- time estimate: 15 min -->

### Neues Django-Projekt erstellen: `startproject`

Das wichtigste Kommando für den Einstieg ist `startproject`, 
das die grundlegende Projektstruktur erstellt.

```bash
django-admin startproject projektname
```

Erstellen Sie ein Projekt namens **meinprojekt**, indem Sie zunächst [PARTREF::django-project] 
lesen und den dort beschriebenen Schritten folgen, 
um in einer virtuellen Umgebung erfolgreich ein neues Django-Projekt anzulegen.  

[EC] Erstellen Sie ein neues Django-Projekt namens `meinshop` mit 
`django-admin startproject`.
<!-- EC2 -->

<!-- time estimate: 5 min -->

### Django-Anwendung erstellen: `startapp`

Django-Projekte bestehen aus einer oder mehreren Anwendungen (Apps).
Jede App behandelt einen spezifischen Funktionsbereich.

```bash
django-admin startapp appname
```

oder innerhalb eines Projekts (empfohlen):

```bash
python manage.py startapp appname
```

Eine App-Struktur sieht folgendermaßen aus:

```
appname/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Die wichtigsten Dateien sind:

- `models.py`: Datenbankmodelle definieren
- `views.py`: Ansichts-Funktionen oder -Klassen
- `admin.py`: Konfiguration für das Admin-Interface
- `migrations/`: Datenbankmigrationen

Optional: weitere Details zu Django-Apps finden Sie in der 
[App-Dokumentation](https://docs.djangoproject.com/en/stable/ref/applications/).

[EC] Wechseln Sie in Ihr `meinshop` Projektverzeichnis und erstellen Sie eine App 
namens `produkte`.
<!-- time estimate: 5 min -->

<!-- EC3 -->

### Entwicklungsserver starten: `runserver`

Um das Django-Projekt zu testen, können Sie den integrierten Entwicklungsserver starten:

```bash
python manage.py runserver
```

Standardmäßig läuft der Server auf `http://127.0.0.1:8000/`.
Sie können Port und IP-Adresse anpassen:

```bash
python manage.py runserver 0.0.0.0:8080  # IP und Port
python manage.py runserver 8080           # nur Port ändern
```

Zusätzliche Optionen:

```bash
python manage.py runserver --noreload     # ohne automatisches Neuladen
python manage.py runserver --insecure     # statische Dateien in DEBUG=False
```

[NOTICE]
Der Entwicklungsserver ist nur für die Entwicklung gedacht und sollte 
niemals in einer Produktionsumgebung verwendet werden.
[ENDNOTICE]


### Projektkonfiguration überprüfen: `check`

Das `check` Kommando überprüft Ihr Django-Projekt auf häufige Probleme:

```bash
python manage.py check
```

Es prüft unter anderem:

- Modell-Definitionen
- URL-Konfigurationen  
- Template-Einstellungen
- Sicherheitseinstellungen

Für spezifische Checks können Sie Tags verwenden:

```bash
python manage.py check --tag=models      # nur Modell-Checks
python manage.py check --tag=security    # nur Sicherheits-Checks
python manage.py check --tag=urls        # nur URL-Checks
```

Optional: weitere Informationen zu System-Checks finden Sie in der 
[System Check Dokumentation](https://docs.djangoproject.com/en/stable/topics/checks/).

[EC] Führen Sie `python manage.py check` in Ihrem Projekt aus und 
dokumentieren Sie das Ergebnis.

<!-- EC4 -->

[EC] Führen Sie einen Security-Check mit `python manage.py check --tag=security` durch.

<!-- EC5 -->

<!-- time estimate: 15 min -->

### Datenbankmigrationen: `makemigrations` und `migrate`

Django verwendet ein Migrationssystem zur Verwaltung von Datenbankschema-Änderungen.

```bash
python manage.py makemigrations          # Erstellt Migrationsdateien
python manage.py migrate                 # Wendet Migrationen an
```

Für spezifische Apps:

```bash
python manage.py makemigrations appname  # nur für eine App
python manage.py migrate appname         # nur für eine App
python manage.py migrate appname 0002    # zu spezifischer Migration
```

Weitere Optionen:

```bash
python manage.py migrate --fake          # Migration als angewendet markieren
python manage.py migrate --fake-initial  # nur bei existierenden Tabellen
```

Optional: weitere Informationen zu Migrationen finden Sie in der 
[Migrations-Dokumentation](https://docs.djangoproject.com/en/stable/topics/migrations/).

[EC] Führen Sie die initialen Migrationen für Ihr Projekt aus mit 
`python manage.py migrate`.

<!-- EC6 -->


[EC] Überprüfen Sie den Status der Migrationen mit 
`python manage.py showmigrations`.

<!-- EC7 -->

<!-- time estimate: 10 min -->

### Superuser erstellen: `createsuperuser`

**Migrationen anwenden** (wenn Sie eine Warnung über nicht angewendete Migrationen sehen)
```bash
python manage.py migrate  # Wendet alle ausstehenden Datenbankmigrationen an
```

Für den Zugang zum Django-Admin-Interface benötigen Sie einen Superuser:

```bash
python manage.py createsuperuser
```

Das Kommando fragt interaktiv nach:

- Benutzername
- E-Mail-Adresse  
- Passwort (wird zweimal zur Bestätigung eingegeben)

Alternativ können Sie Parameter direkt übergeben:

```bash
python manage.py createsuperuser --username=admin --email=admin@example.com
```

[EC] Erstellen Sie einen Superuser für Ihr Projekt und loggen Sie sich 
in das Admin-Interface unter `/admin/` ein.

<!-- time estimate: 5 min -->

<!-- EC8 -->

### Django Shell: `shell`

Die Django Shell bietet eine interaktive Python-Umgebung mit Zugriff auf Ihr Projekt:

```bash
python manage.py shell
```

In der Shell können Sie:

- Modelle importieren und verwenden
- Datenbankabfragen durchführen
- Django-Einstellungen testen

```python
# Beispiel in der Django Shell
from django.contrib.auth.models import User
users = User.objects.all()
print(users)
```

Für verschiedene Shell-Interpreter:

```bash
python manage.py shell --interface=ipython  # IPython verwenden
python manage.py shell --interface=bpython  # BPython verwenden
```

Optional: weitere Informationen zur Django Shell finden Sie in der 
[Shell Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#shell).

[EC] Öffnen Sie die Django Shell und führen Sie folgende Befehle aus:

<!-- EC9 -->

```python
from django.conf import settings
print(settings.DEBUG)
print(settings.DATABASES)
```

<!-- time estimate: 10 min -->

### Tests ausführen: `test`

Django bietet ein integriertes Test-Framework:

```bash
python manage.py test                           # Alle Tests
python manage.py test appname                   # Tests einer App
python manage.py test appname.tests.TestClass   # Spezifische Testklasse
```

Weitere Test-Optionen:

```bash
python manage.py test --verbosity=2             # Ausführliche Ausgabe
python manage.py test --keepdb                  # Test-Datenbank behalten
python manage.py test --parallel                # Parallele Ausführung
```

[EC] Führen Sie `python manage.py test` aus und dokumentieren Sie das Ergebnis.


<!-- EC10 -->

### Statische Dateien sammeln: `collectstatic`

Für die Produktionsumgebung müssen statische Dateien gesammelt werden:

```bash
python manage.py collectstatic
```

Weitere Optionen:

```bash
python manage.py collectstatic --noinput        # ohne Bestätigung
python manage.py collectstatic --clear          # Zielverzeichnis leeren
python manage.py collectstatic --dry-run        # Testlauf ohne Änderungen
```

[NOTICE]
Dieses Kommando funktioniert nur, wenn in Ihrer settings.py die Einstellung STATIC_ROOT gesetzt ist,
z. B.:
```py
STATIC_ROOT = BASE_DIR / "staticfiles"
```
Dadurch werden alle statischen Dateien beim Befehl collectstatic in das Verzeichnis staticfiles/ kopiert.
[ENDNOTICE]

<!-- time estimate: 10 min -->

### Weitere nützliche Kommandos

**Datenbankshell: `dbshell`**

Direkter Zugang zur Datenbank-Shell:

```bash
python manage.py dbshell
```

**Daten exportieren/importieren: `dumpdata` und `loaddata`**

```bash
python manage.py dumpdata > backup.json         # Daten exportieren
python manage.py loaddata backup.json           # Daten importieren
```

**Datenbank zurücksetzen: `flush`**

```bash
python manage.py flush                           # Alle Daten löschen
```

[EC] Testen Sie `python manage.py flush`, um das Zurücksetzen der Datenbank zu überprüfen.
<!-- EC11 -->

<!-- time estimate: 5 min -->


[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll
[PROT::ALT:django-admin.prot]

[ENDINSTRUCTOR]