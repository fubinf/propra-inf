title: Django django-admin Kommandozeilen-Tool
stage: draft
timevalue: 1.25
difficulty: 2
requires: django-project
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

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in [PARTREF::django-basics] erstellt haben.
Alle folgenden Änderungen werden Sie in diesem Projekt durchführen.

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

[EC] Wechseln Sie in Ihr `meinprojekt` Projektverzeichnis und erstellen Sie eine App 
namens `produkte` mit `python manage.py startapp produkte`.
<!-- time estimate: 5 min -->

<!-- EC1 -->

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

[EC] Führen Sie `python manage.py check` in Ihrem Projekt aus und 
dokumentieren Sie das Ergebnis.

<!-- EC2 -->

[EC] Führen Sie einen Security-Check mit `python manage.py check --tag=security` durch.

<!-- EC3 -->

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

[EC] Führen Sie die initialen Migrationen für Ihr Projekt aus mit 
`python manage.py migrate`.

<!-- EC4 -->


[EC] Überprüfen Sie den Status der Migrationen mit 
`python manage.py showmigrations`.

<!-- EC5 -->

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

<!-- EC6 -->

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

[EC] Öffnen Sie die Django Shell und führen Sie folgende Befehle aus:

<!-- EC7 -->

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


<!-- EC8 -->

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
<!-- EC9 -->

<!-- time estimate: 5 min -->

### Weiterführend

- [Django Management Commands Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/) – Übersicht aller verfügbaren Kommandos
- [App-Dokumentation](https://docs.djangoproject.com/en/stable/ref/applications/) – Details zu Django-Apps
- [System Check Dokumentation](https://docs.djangoproject.com/en/stable/topics/checks/) – Weitere Informationen zu System-Checks
- [Migrations-Dokumentation](https://docs.djangoproject.com/en/stable/topics/migrations/) – Detaillierte Dokumentation zu Migrationen
- [Shell Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#shell) – Weitere Informationen zur Django Shell

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll
[PROT::ALT:django-admin.prot]

[ENDINSTRUCTOR]