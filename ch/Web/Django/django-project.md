title: Django Erstes Projekt erstellen und konfigurieren
stage: alpha
timevalue: 2.0
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
In dieser Aufgabe erstellen wir unser erstes Django-Projekt namens "meinprojekt" und lernen die Grundlagen kennen.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen und Installation

Bitte lesen Sie zunächst [PARTREF::django-basics] und folgen Sie den dort beschriebenen 
Schritten, um Django in einer virtuellen Umgebung erfolgreich zu installieren. 
Damit verfügen Sie über eine saubere Arbeitsumgebung für die folgenden Aufgaben.  

Während dieses Prozesses können unter anderem folgende Befehle hilfreich sein:

```bash
python3 -m venv django_env        # Virtuelle Umgebung erstellen
source django_env/bin/activate    # Virtuelle Umgebung aktivieren (Linux/Mac)
django_env\Scripts\activate       # Virtuelle Umgebung aktivieren (Windows)
pip install django                # Django in der virtuellen Umgebung installieren
python -m django --version        # Installierte Django-Version prüfen
```
[EC] Dokumentieren Sie, dass Sie Django erfolgreich in einer virtuellen Umgebung
installiert haben, indem Sie die Ausgabe von python -m django --version angeben.
<!-- EC1 -->

<!-- time estimate: 5 min -->

### Erstes Django-Projekt erstellen

Sie können Ihr erstes Django-Projekt mit `startproject` erstellen:

**Erstes Django-Projekt erstellen**:
```bash
django-admin startproject meinprojekt
cd meinprojekt
python manage.py runserver
```

**Häufige Probleme beim Starten des Servers**:

**Migrationen anwenden** (wenn Sie eine Warnung über nicht angewendete Migrationen sehen)
```bash
python manage.py migrate  # Wendet alle ausstehenden Datenbankmigrationen an
```

**Port-Konflikt lösen** (wenn Port 8000 bereits verwendet wird)
```bash
python manage.py runserver 8080  # Server auf einem alternativen Port starten
```

Nach dem Start sollte unter `http://127.0.0.1:8000/` 
oder `http://127.0.0.1:8080/` die Django-Willkommensseite erscheinen.

[EC] Erstellen Sie ein Django-Projekt namens `testprojekt` und starten Sie den 
Entwicklungsserver. 
<!-- EC2 -->

### Django-Projektstruktur verstehen

Ein neues Django-Projekt hat folgende Struktur:
```
meinprojekt/
├── manage.py                   # Django-Kommandozeilen-Tool
└── testprojekt/                # Projekt-Konfigurationsordner
    ├── __init__.py             # Python-Paket-Marker (leer)
    ├── settings.py             # Zentrale Projektkonfiguration
    ├── urls.py                 # Haupt-URL-Routing
    ├── wsgi.py                 # WSGI-Deployment-Konfiguration
    └── asgi.py                 # ASGI-Konfiguration für async/WebSockets
```

**Wichtige Dateien**:

- `manage.py`: Kommandozeilen-Tool für Projektverwaltung
- `settings.py`: Konfigurationsdatei des Projekts
- `urls.py`: URL-Routing-Konfiguration
- `wsgi.py`/`asgi.py`: Deployment-Konfiguration für Webserver

Optional: Möchten Sie mehr erfahren? Mehr zur 
[Project Structure](https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project)

[EC] Erkunden Sie die Projektstruktur und listen Sie alle erstellten Dateien und 
Ordner. Benutzen Sie dazu den `tree`-Befehl oder ähnliche Tools:
```bash
sudo apt update
sudo apt install tree
tree meinprojekt
```
<!-- EC3 -->
<!-- time estimate: 15 min -->

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


### Wichtige Konfigurationsdateien verstehen

**settings.py - Zentrale Projekteinstellungen**

Die `settings.py` enthält alle wichtigen Projekteinstellungen.
Öffnen Sie `meinprojekt/settings.py` und betrachten Sie folgende wichtige Abschnitte:

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

[EQ] Öffnen Sie `settings.py` und beantworten Sie: 
Was ist der aktuelle Wert von `DEBUG` und warum ist dies wichtig?
Welche Datenbank wird standardmäßig verwendet?
Wie viele Apps sind in `INSTALLED_APPS` vorkonfiguriert?
<!-- EQ1 -->

**urls.py - URL-Routing-Konfiguration**

Die `urls.py` definiert, welche URLs zu welchen Views führen:

```python
[SNIPPET::ITREE:/Web/Django/snippet-test.py::snippet_test]
```
<!-- [SNIPPET::ITREE:Web/Django/snippet-test.py::snippet_test] -->
<!-- [SNIPPET::ITREE:snippet-test.py::snippet_test] -->

[EQ] Untersuchen Sie `meinprojekt/urls.py`. Welche Route ist standardmäßig definiert?
<!-- EQ2 -->
<!-- time estimate: 20 min -->

### Erste View-Funktion erstellen

Jetzt erstellen wir unsere erste eigene Webseite.

[ER] Erstellen Sie die Datei `meinprojekt/meinprojekt/views.py`:
<!-- ER1 -->

[SNIPPET::ALT::django_hello_view]

Diese View-Funktion:

- Erhält ein `request`-Objekt mit HTTP-Anfragedaten
- Gibt ein `HttpResponse`-Objekt mit unserem Text zurück

[ER] Modifizieren Sie `meinprojekt/meinprojekt/urls.py` vollständig:
<!-- ER2 -->

[SNIPPET::ALT::django_hello_urls]
[NOTICE]
Der Django-Entwicklungsserver lädt Code-Änderungen automatisch neu.
Sie müssen den Server nicht manuell neustarten!
[ENDNOTICE]

[EQ] Aktualisieren Sie die Browserseite. Was sehen Sie jetzt anstelle der Willkommensseite?
<!-- time estimate: 10 min -->
<!-- EQ3 -->

### URL-Patterns und path()-Funktion

Die `path()`-Funktion hat folgende Syntax:
```python
[SNIPPET::/Web/Django/include/snippet-test.py::snippet_test_path]
```
<!-- [SNIPPET::/Web/Django/include/snippet-test.py::snippet_test_path] -->
<!-- [SNIPPET::include/snippet-test.py::snippet_test_path] -->
Parameter:

- `route` - URL-Muster als String
- `view` - View-Funktion, die aufgerufen wird  
- `kwargs` - Zusätzliche Parameter (optional)
- `name` - Eindeutiger Name für die URL (optional)

Optional: Weitere Erklärungen finden Sie hier: 
[URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/)

[ER] Ändern Sie die URL-Konfiguration, damit "Hello World" unter `/hello/` erreichbar ist:
<!-- ER3 -->

<!-- Korrekte Referenz. Zum Testen kann sie geändert werden in: wrong_snippet_id -->
[SNIPPET::ALT::django_hello_route]


[EQ] Testen Sie `http://127.0.0.1:8000/hello/` im Browser. 
Was passiert, wenn Sie `http://127.0.0.1:8000/` (ohne hello) aufrufen?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.

<!-- EQ4 -->

<!-- time estimate: 20 min -->

### Mehrere Views erstellen

[ER] Erweitern Sie `views.py` um zwei weitere Funktionen:

```python
def welcome(request):
    return HttpResponse("Willkommen bei Django!")

def about(request):
    return HttpResponse("Mein erstes Django-Projekt - meinprojekt")
```
<!-- ER4 -->

[ER] Fügen Sie in `urls.py` entsprechende URL-Patterns hinzu:

```python
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
]
```
<!-- ER5 -->

[ER] Testen Sie alle drei URLs im Browser mit `http://127.0.0.1:8000/hello/`, 
`http://127.0.0.1:8000/welcome/`, `http://127.0.0.1:8000/about/`. 
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- ER6 -->

<!-- time estimate: 15 min -->

### URL-Parameter verwenden

Django kann Parameter aus URLs extrahieren und an Views weitergeben:

[ER] Erstellen Sie eine neue View-Funktion in `views.py`:

```python
def greet(request, name):
    return HttpResponse(f"Hallo {name}! Schön, dich kennenzulernen.")
```
<!-- ER7 -->

[ER] Fügen Sie das URL-Pattern mit Parameter hinzu:

```python
path('greet/<str:name>/', views.greet, name='greet'),
```
<!-- ER8 -->

Die Syntax `<str:name>` bedeutet:
- `str` - Datentyp (String)
- `name` - Parametername, wird an die View weitergegeben

[ER] Testen Sie URLs: `http://127.0.0.1:8000/greet/Anna/`, `http://127.0.0.1:8000/greet/Max/`
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.

<!-- ER9 -->

<!-- time estimate: 15 min -->

### HTML-Response erstellen

Views können auch HTML-Code zurückgeben:

[ER] Erstellen Sie eine neue View-Funktion:
<!-- ER10 -->

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
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- ER11 -->
[HINT::Route]
Schreiben Sie den Eintrag so wie bei den Routen `hello`, `welcome` und `about`
[ENDHINT]
<!-- time estimate: 15 min -->

### Projektstruktur dokumentieren

Drücken Sie **Strg + C** (Linux/macOS) bzw. **Ctrl + C** (Windows), um den Server zu beenden.

[EC] Erstellen Sie eine vollständige Übersicht Ihrer finalen Projektstruktur 
mit dem `tree`-Befehl oder manuell.
<!-- EC4 -->

Die finale Struktur sollte etwa so aussehen:
```
meinprojekt/
├── manage.py
├── db.sqlite3              # (wird automatisch erstellt)
└── meinprojekt/
    ├── __init__.py
    ├── settings.py
    ├── urls.py             # modifiziert
    ├── views.py            # neu erstellt
    ├── asgi.py
    └── wsgi.py
```

<!-- time estimate: 5 min -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-project.md]

### Kommandoprotokoll
[PROT::ALT:django-project.prot]

[ENDINSTRUCTOR]