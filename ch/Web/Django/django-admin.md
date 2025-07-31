title: Django django-admin Kommandozeilen-Tool
stage: draft
timevalue: 2.0
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

Bevor wir mit `django-admin` arbeiten können, müssen wir Django installieren.
Django ist ein Python-Web-Framework, das über `pip` installiert werden kann.

```bash
pip install django
```

Nach der Installation steht das `django-admin` Kommando zur Verfügung.
Weitere Informationen zur Installation finden Sie in der 
[Django Dokumentation](https://docs.djangoproject.com/en/stable/intro/install/).

[ER] Installieren Sie Django über `pip` und überprüfen Sie die Installation 
mit `django-admin --version`.

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

Weitere Informationen zu allen verfügbaren Kommandos finden Sie in der 
[Django Management Commands Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/).

[ER] Führen Sie `django-admin help` aus und dokumentieren Sie fünf verschiedene 
verfügbare Kommandos mit einer kurzen Beschreibung ihrer Funktion.

[ER] Verwenden Sie `django-admin help startproject`, um detaillierte Informationen 
über das `startproject` Kommando zu erhalten.
<!-- time estimate: 15 min -->

### Neues Django-Projekt erstellen: `startproject`

Das wichtigste Kommando für den Einstieg ist `startproject`, 
das die grundlegende Projektstruktur erstellt.

```bash
django-admin startproject projektname
```

Dies erstellt ein Verzeichnis mit folgender Struktur:

```
projektname/
    manage.py
    projektname/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

Die wichtigsten Dateien sind:

- `manage.py`: Projektmanagement-Skript für lokale Kommandos
- `settings.py`: Zentrale Konfigurationsdatei des Projekts
- `urls.py`: URL-Routing-Konfiguration
- `wsgi.py`: WSGI-Anwendungsentry-Point für Production-Server

Weitere Informationen zur Projektstruktur finden Sie in der 
[Django Tutorial Dokumentation](https://docs.djangoproject.com/en/stable/intro/tutorial01/).

[ER] Erstellen Sie ein neues Django-Projekt namens `meinshop` mit 
`django-admin startproject`.

[ER] Navigieren Sie in das Projektverzeichnis und listen Sie alle erstellten Dateien auf.
Beschreiben Sie kurz den Zweck von `manage.py`, `settings.py` und `urls.py`.

### Projektstruktur mit Optionen anpassen

Das `startproject` Kommando bietet verschiedene Optionen zur Anpassung:

```bash
# Projekt in spezifischem Verzeichnis erstellen
django-admin startproject projektname zielverzeichnis

# Mit benutzerdefinierten Datei-Extensions
django-admin startproject --extension=py,txt projektname

# Mit Template-URL
django-admin startproject --template=URL projektname
```

[ER] Erstellen Sie ein Projekt `testprojekt` in einem spezifischen Verzeichnis 
`/tmp/django_test` (oder einem entsprechenden Verzeichnis auf Ihrem System).
<!-- time estimate: 20 min -->

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

Weitere Details zu Django-Apps finden Sie in der 
[App-Dokumentation](https://docs.djangoproject.com/en/stable/ref/applications/).

[ER] Wechseln Sie in Ihr `meinshop` Projektverzeichnis und erstellen Sie eine App 
namens `produkte`.

[ER] Erstellen Sie eine weitere App namens `benutzer` und dokumentieren Sie 
die Unterschiede in der Verzeichnisstruktur zwischen Projekt und App.

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

[ER] Starten Sie den Entwicklungsserver für Ihr `meinshop` Projekt und 
öffnen Sie die Standard-Django-Willkommensseite im Browser.

[ER] Starten Sie den Server auf Port 8080 und testen Sie den Zugriff.
<!-- time estimate: 15 min -->

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

Weitere Informationen zu System-Checks finden Sie in der 
[System Check Dokumentation](https://docs.djangoproject.com/en/stable/topics/checks/).

[ER] Führen Sie `python manage.py check` in Ihrem Projekt aus und 
dokumentieren Sie das Ergebnis.

[ER] Führen Sie einen Security-Check mit `python manage.py check --tag=security` durch.

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

Weitere Informationen zu Migrationen finden Sie in der 
[Migrations-Dokumentation](https://docs.djangoproject.com/en/stable/topics/migrations/).

[ER] Führen Sie die initialen Migrationen für Ihr Projekt aus mit 
`python manage.py migrate`.

[ER] Überprüfen Sie den Status der Migrationen mit 
`python manage.py showmigrations`.

### Superuser erstellen: `createsuperuser`

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

[ER] Erstellen Sie einen Superuser für Ihr Projekt und loggen Sie sich 
in das Admin-Interface unter `/admin/` ein.
<!-- time estimate: 20 min -->

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

Weitere Informationen zur Django Shell finden Sie in der 
[Shell Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#shell).

[ER] Öffnen Sie die Django Shell und führen Sie folgende Befehle aus:

```python
from django.conf import settings
print(settings.DEBUG)
print(settings.DATABASES)
```

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

Weitere Informationen zum Testen finden Sie in der 
[Testing-Dokumentation](https://docs.djangoproject.com/en/stable/topics/testing/).

[ER] Führen Sie `python manage.py test` aus und dokumentieren Sie das Ergebnis.

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
Dieses Kommando funktioniert nur, wenn `STATIC_ROOT` in den Einstellungen konfiguriert ist.
[ENDNOTICE]

[ER] Konfigurieren Sie `STATIC_ROOT` in Ihrer `settings.py` 
(z.B. `STATIC_ROOT = BASE_DIR / 'staticfiles'`) und führen Sie 
`collectstatic` aus (auch wenn noch keine statischen Dateien vorhanden sind).

### Weitere nützliche Kommandos

#### Datenbankshell: `dbshell`

Direkter Zugang zur Datenbank-Shell:

```bash
python manage.py dbshell
```

#### Daten exportieren/importieren: `dumpdata` und `loaddata`

```bash
python manage.py dumpdata > backup.json         # Daten exportieren
python manage.py loaddata backup.json           # Daten importieren
```

#### Datenbank zurücksetzen: `flush`

```bash
python manage.py flush                           # Alle Daten löschen
```

[ER] Testen Sie `python manage.py dbshell` um die Datenbankverbindung zu überprüfen.

### Kommando-Übersicht und Dokumentation

[ER] Erstellen Sie eine Übersichtstabelle der wichtigsten `django-admin` Kommandos 
mit folgenden Spalten:

- **Kommando**
- **Zweck**  
- **Beispiel**
- **Wann verwendet**

Füllen Sie die Tabelle mit mindestens 10 verschiedenen Kommandos aus dieser Aufgabe.
<!-- time estimate: 30 min -->
[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]

Reichen Sie zusätzlich ein Markdown-Dokument ein, das Ihre Erfahrungen 
und Beobachtungen bei der Verwendung der verschiedenen `django-admin` Kommandos dokumentiert.

[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]

Die Studierenden sollten:

- Ein funktionsfähiges Django-Projekt erstellt haben
- Die wichtigsten `django-admin` Kommandos praktisch angewendet haben  
- Den Unterschied zwischen Projekt und App verstehen
- Grundlegende Django-Konzepte wie Migrationen und Admin-Interface kennengelernt haben
- Eine strukturierte Dokumentation ihrer Arbeit erstellt haben

Häufige Probleme:

- Django nicht korrekt installiert
- Verwechslung von `django-admin` und `manage.py`
- Fehlende Konfiguration für `collectstatic`
- Probleme beim Erstellen des Superusers
- Missverständnisse bezüglich der Projekt- versus App-Struktur

Bewertungskriterien:

- Vollständige Ausführung aller Aufgaben
- Korrekte Verwendung der Kommandos
- Verständnis der Django-Projektstruktur
- Qualität der Dokumentation
[ENDINSTRUCTOR]