title: Django Erstes Projekt erstellen und konfigurieren
stage: draft
timevalue: 2.5
difficulty: 2
assumes: django-basics
---

[SECTION::goal::idea,experience]

- Ich kann ein Django-Projekt mit `django-admin` erstellen und die Grundstruktur verstehen.
- Ich verstehe die Funktionsweise von Django-Views und URL-Routing.
- Ich kann den Django-Entwicklungsserver starten und einfache Webanwendungen erstellen.
- Ich kenne die wichtigsten Django-Konfigurationsdateien und deren Zweck.

[ENDSECTION]

[SECTION::background::default]

Django ist ein High-Level Python Web-Framework, das schnelle Entwicklung und sauberes, 
pragmatisches Design ermöglicht. Es folgt dem Model-View-Template (MVT) Architekturmuster 
und bietet viele eingebaute Funktionen für typische Webentwicklungsaufgaben.
In dieser Aufgabe erstellen wir unser erstes Django-Projekt namens "HelloWorld" und lernen die Grundlagen kennen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen und Installation

Für diese Aufgabe verwenden wir Python 3.9+ und Django 4.2+.
Prüfen Sie zunächst Ihre installierten Versionen:

```bash
python3 -V
python3 -m django --version
```

Falls Django noch nicht installiert ist:
```bash
pip install django
```

Siehe auch: [Django Installation Guide](https://docs.djangoproject.com/en/4.2/intro/install/)

[ER] Führen Sie die Versionsprüfung durch und dokumentieren Sie Ihre Python- und Django-Versionen.
<!-- time estimate: 5 min -->

### Django-Verwaltungswerkzeug

Nach der Installation steht das Kommandozeilenwerkzeug `django-admin` zur Verfügung.
Es bietet verschiedene Befehle für die Projektverwaltung:

```bash
django-admin
```

Die wichtigsten Befehle:
- `startproject` - Erstellt ein neues Django-Projekt
- `startapp` - Erstellt eine neue Django-App
- `runserver` - Startet den Entwicklungsserver
- `makemigrations` - Erstellt Datenbankmigrationen
- `migrate` - Führt Datenbankmigrationen aus

[ER] Führen Sie `django-admin` ohne Parameter aus und notieren Sie sich drei weitere Befehle mit deren Zweck.
<!-- time estimate: 10 min -->

### Erstes Django-Projekt erstellen

Erstellen Sie ein neues Django-Projekt mit dem Namen "HelloWorld":

```bash
django-admin startproject HelloWorld
```

[ER] Erstellen Sie das Projekt und wechseln Sie in das Projektverzeichnis.

[ER] Untersuchen Sie die erstellte Verzeichnisstruktur mit `tree` oder `ls -la` und dokumentieren Sie diese.

Die Struktur sollte so aussehen:
```
HelloWorld/                  # Projekt-Wurzelverzeichnis
├── manage.py               # Django-Verwaltungsskript
└── HelloWorld/             # Projektkonfiguration
    ├── __init__.py         # Python-Paket-Markierung
    ├── settings.py         # Projekteinstellungen
    ├── urls.py            # URL-Konfiguration
    ├── asgi.py            # ASGI-Konfiguration (asynchron)
    └── wsgi.py            # WSGI-Konfiguration (synchron)
```
<!-- time estimate: 15 min -->

### Wichtige Konfigurationsdateien verstehen

#### settings.py - Zentrale Projekteinstellungen

Die `settings.py` enthält alle wichtigen Projekteinstellungen.
Öffnen Sie `HelloWorld/settings.py` und betrachten Sie folgende wichtige Abschnitte:

```python
# Entwicklungsmodus (NUR für Entwicklung!)
DEBUG = True

# Erlaubte Hosts (wichtig für Produktion)
ALLOWED_HOSTS = []

# Installierte Django-Apps
INSTALLED_APPS = [
    'django.contrib.admin',     # Admin-Interface
    'django.contrib.auth',      # Authentifizierung
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Sitzungsverwaltung
    'django.contrib.messages',  # Nachrichten-Framework
    'django.contrib.staticfiles', # Statische Dateien
]

# Datenbankeinstellungen (Standard: SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

[ER] Öffnen Sie `settings.py` und beantworten Sie:
- Was ist der aktuelle Wert von `DEBUG` und warum ist dies wichtig?
- Welche Datenbank wird standardmäßig verwendet?
- Wie viele Apps sind in `INSTALLED_APPS` vorkonfiguriert?

#### urls.py - URL-Routing-Konfiguration

Die `urls.py` definiert, welche URLs zu welchen Views führen:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin-Interface
]
```

[ER] Untersuchen Sie `HelloWorld/urls.py`. Welche Route ist standardmäßig definiert?
<!-- time estimate: 20 min -->

### Entwicklungsserver starten

Starten Sie den Django-Entwicklungsserver:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

Die Parameter bedeuten:
- `0.0.0.0` - Server hört auf allen Netzwerkschnittstellen
- `8000` - Port-Nummer (Standard)

[ER] Starten Sie den Server und öffnen Sie `http://127.0.0.1:8000/` im Browser.

[ER] Machen Sie einen Screenshot der Django-Willkommensseite.

Sie sollten eine Seite mit "The install worked successfully!" sehen.
<!-- time estimate: 10 min -->

### Erste View-Funktion erstellen

Jetzt erstellen wir unsere erste eigene Webseite.

[ER] Erstellen Sie die Datei `HelloWorld/HelloWorld/views.py`:

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")
```

Diese View-Funktion:
- Erhält ein `request`-Objekt mit HTTP-Anfragedaten
- Gibt ein `HttpResponse`-Objekt mit unserem Text zurück

[ER] Modifizieren Sie `HelloWorld/HelloWorld/urls.py` vollständig:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
]
```

[ER] Aktualisieren Sie die Browserseite. Was sehen Sie jetzt anstelle der Willkommensseite?
<!-- time estimate: 15 min -->

### URL-Patterns und path()-Funktion

Die `path()`-Funktion hat folgende Syntax:
```python
path(route, view, kwargs=None, name=None)
```

Parameter:
- `route` - URL-Muster als String
- `view` - View-Funktion, die aufgerufen wird  
- `kwargs` - Zusätzliche Parameter (optional)
- `name` - Eindeutiger Name für die URL (optional)

Weitere Infos: [URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/)

[ER] Ändern Sie die URL-Konfiguration, damit "Hello World" unter `/hello/` erreichbar ist:

```python
urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

[ER] Testen Sie `http://127.0.0.1:8000/hello/` im Browser.

[ER] Was passiert, wenn Sie `http://127.0.0.1:8000/` (ohne hello) aufrufen?
<!-- time estimate: 15 min -->

### Mehrere Views erstellen

[ER] Erweitern Sie `views.py` um zwei weitere Funktionen:

```python
def welcome(request):
    return HttpResponse("Willkommen bei Django!")

def about(request):
    return HttpResponse("Mein erstes Django-Projekt - HelloWorld")
```

[ER] Fügen Sie in `urls.py` entsprechende URL-Patterns hinzu:

```python
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
]
```

[ER] Testen Sie alle drei URLs im Browser.
<!-- time estimate: 20 min -->

### URL-Parameter verwenden

Django kann Parameter aus URLs extrahieren und an Views weitergeben:

[ER] Erstellen Sie eine neue View-Funktion in `views.py`:

```python
def greet(request, name):
    return HttpResponse(f"Hallo {name}! Schön, dich kennenzulernen.")
```

[ER] Fügen Sie das URL-Pattern mit Parameter hinzu:

```python
path('greet/<str:name>/', views.greet, name='greet'),
```

Die Syntax `<str:name>` bedeutet:
- `str` - Datentyp (String)
- `name` - Parametername, wird an die View weitergegeben

[ER] Testen Sie URLs wie:
- `http://127.0.0.1:8000/greet/Anna/`
- `http://127.0.0.1:8000/greet/Max/`
<!-- time estimate: 15 min -->

### HTML-Response erstellen

Views können auch HTML-Code zurückgeben:

[ER] Erstellen Sie eine neue View-Funktion:

```python
def hello_html(request):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Django Hello</title>
            <meta charset="utf-8">
        </head>
        <body>
            <h1>Hello Django!</h1>
            <p>Dies ist meine erste Django-Seite mit HTML.</p>
            <ul>
                <li><a href="/hello/">Einfacher Text</a></li>
                <li><a href="/welcome/">Willkommensseite</a></li>
                <li><a href="/about/">Über diese Seite</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html)
```

[ER] Fügen Sie das URL-Pattern hinzu und testen Sie die Seite.
<!-- time estimate: 20 min -->

### Projektstruktur dokumentieren

[ER] Erstellen Sie eine vollständige Übersicht Ihrer finalen Projektstruktur mit dem `tree`-Befehl oder manuell.

Die finale Struktur sollte etwa so aussehen:
```
HelloWorld/
├── manage.py
├── db.sqlite3              # (wird automatisch erstellt)
└── HelloWorld/
    ├── __init__.py
    ├── settings.py
    ├── urls.py             # modifiziert
    ├── views.py            # neu erstellt
    ├── asgi.py
    └── wsgi.py
```

[NOTICE]
Der Django-Entwicklungsserver lädt Code-Änderungen automatisch neu.
Sie müssen den Server nicht manuell neustarten!
[ENDNOTICE]
<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

Dokumentieren Sie:
1. Ihre Python- und Django-Versionen
2. Die Ausgabe von `django-admin` mit drei zusätzlichen Befehlen
3. Die komplette finale Projektstruktur
4. Alle erstellten View-Funktionen mit Beschreibung
5. Alle URL-Patterns mit Erklärung
6. Screenshots der funktionierenden Seiten im Browser

[INCLUDE::/_include/Submission-Quellcode.md]

Reichen Sie folgende Dateien ein:
- `HelloWorld/HelloWorld/views.py`
- `HelloWorld/HelloWorld/urls.py`

[ENDSECTION]

[INSTRUCTOR::Erwartete Ergebnisse]

Die Studierenden sollten:
- Ein funktionierendes Django-Projekt "HelloWorld" erstellt haben
- Mindestens 5 verschiedene View-Funktionen implementiert haben
- URL-Routing mit und ohne Parameter verstehen
- HTML-Responses erstellen können
- Die Projektstruktur vollständig dokumentiert haben
- Screenshots aller funktionierenden Seiten eingereicht haben

Häufige Fehler:
- Import-Statement `from . import views` vergessen
- Trailing Slashes in URL-Patterns vergessen/hinzugefügt
- Falsche Einrückung in Python-Code
- Parameter-Namen in URL und View stimmen nicht überein
- Server läuft nicht oder falsche URL aufgerufen

[INCLUDE::ALT:]
[ENDINSTRUCTOR]