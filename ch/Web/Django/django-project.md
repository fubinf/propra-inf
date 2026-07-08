title: Django Erstes Projekt erstellen und konfigurieren
stage: alpha
timevalue: 1.0
difficulty: 2
requires: django-basics
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundstruktur eines Django-Projekts und kenne die Rolle der wichtigsten Konfigurationsdateien.
- Ich kann eine erste View-Funktion schreiben und mit einem URL verknüpfen.
- Ich kann Logik (view) und Layout (template) voneinander trennen.

[ENDSECTION]

[SECTION::background::default]

Ein Django-Projekt besteht aus mehreren Dateien und Ordnern, die zusammen eine Web-Anwendung bilden.
Das Verständnis der Projektstruktur, des URL-Routing und der Projektkonfiguration ist notwendig,
um HTTP-Anfragen zu verarbeiten und Web-Anwendungen zu entwickeln.

[ENDSECTION]

[SECTION::instructions::detailed]

### Django-Projektstruktur verstehen

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in [PARTREF::django-basics] erstellt haben.

Ein neues Django-Projekt hat folgende Struktur:
```
meinprojekt/
├── manage.py                   # Django-Kommandozeilen-Tool
├── db.sqlite3                  # (wird automatisch erstellt)
└── meinprojekt/                # Projekt-Konfigurationsordner
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

### Wichtige Konfigurationsdateien verstehen

**settings.py - Zentrale Projekteinstellungen**

Die `settings.py` enthält alle wichtigen Projekteinstellungen.
Öffnen Sie `settings.py` und betrachten Sie folgende wichtige Abschnitte:

```python
[SNIPPET::ITREE:/Web/Django/django-project-settings.py::django_project_settings]
```

[EQ] Öffnen Sie `settings.py` und beantworten Sie: 
Was ist der aktuelle Wert von `DEBUG` und warum ist dies wichtig?

**manage.py - Projekt-Verwaltungsskript**

Die `manage.py` ist ein Wrapper-Skript im Projektroot, das die richtige `DJANGO_SETTINGS_MODULE` für Ihr spezifisches Projekt setzt:

```python
[SNIPPET::ITREE:/Web/Django/django-project-manage.py::django_project_manage]
```

Damit ist `manage.py` der zentrale Zugriffspunkt für alle projektspezifischen Django-Befehle.
Weitere Details zu den verfügbaren Befehlen finden Sie in [PARTREF::django-admin].

<!-- time estimate: 15 min -->

**views.py - View-Funktionen**

Eine **View** ist eine Python-Funktion, die einen HTTP-Request empfängt und eine HTTP-Response zurückgibt.
Sie ist das Herzstück jeder Django-Anwendung.
Weitere Details zu Views finden Sie in [PARTREF::django-views].

[ER] Erstellen Sie die Datei `views.py`:

[SNIPPET::ALT::django_hello_view]

**urls.py - URL-Routing-Konfiguration**

Die `urls.py` definiert, welche URLs zu welchen Views führen.
Nach der View-Erstellung müssen Sie Ihre neue View in `urls.py` registrieren.
Die zentrale Funktion dafür ist `path()` mit drei Hauptparametern:

- `route`: der URL-Pfad (z.B. `""` für die Wurzel `/`)
- `view`: die View-Funktion, die bei einem Aufruf ausgeführt wird
- `name`: ein eindeutiger Name für die Route

Eine detaillierte Erklärung der `path()`-Funktion finden Sie in [PARTREF::django-routing].

```python
[SNIPPET::ITREE:/Web/Django/django-project-urls.py::django_project_urls]
```

[EQ] Untersuchen Sie `urls.py`. Welche Route ist standardmäßig definiert?

[ER] Modifizieren Sie `urls.py`, um Ihre neue View einzubinden:

[SNIPPET::ALT::django_project_urls2]

[HINT::Wie verbinde ich eine View mit einer URL?]
Die `urls.py` verbindet URL-Pfade mit View-Funktionen.
Sie müssen:

1. Das `views`-Modul importieren: `from . import views`
2. Eine Route mit `path()` definieren: `path("pfad", views.funktionname, name="name")`

Der leere String `""` bedeutet die Wurzel-URL (`/`).
[ENDHINT]

[NOTICE]
Der Django-Entwicklungsserver lädt Code-Änderungen automatisch neu.
Sie müssen den Server nach Code-Änderungen nicht manuell neustarten,
solange er bereits läuft.

Falls Sie den Entwicklungsserver nach [PARTREF::django-basics] beendet haben,
starten Sie ihn neu mit `python manage.py runserver 8071` (oder dem von Ihnen verwendeten Port).
Öffnen Sie dann `http://127.0.0.1:8071/` im Browser, bevor Sie die Seite aktualisieren.
[ENDNOTICE]

[EQ] Aktualisieren Sie die Browserseite. Was sehen Sie jetzt anstelle der Willkommensseite?
Erklären Sie, warum die `urls.py`-Konfiguration notwendig ist, um die View zu sehen.
<!-- time estimate: 25 min -->

### Darstellung mit Templates

**Template - HTML-Darstellung**

Ein **Template** ist eine HTML-Datei mit Platzhaltern für dynamische Inhalte.
Es trennt die Darstellung (HTML) von der Programmlogik (Python).
Weitere Details zu Templates finden Sie in [PARTREF::django-template].

Bisher gibt Ihre View-Funktion nur einen reinen Textstring zurück.
Ändern Sie die View, um ein Template zu laden.

Die Funktion `render()` lädt ein Template und übergibt Daten an es:

- `request`: das HTTP-Request-Objekt
- `template_name`: der Dateiname des Templates
- `context`: ein Dictionary mit Daten, die im Template verwendet werden

[ER] Ersetzen Sie den Inhalt von `views.py` durch
folgende Version, die ein Template verwendet:

[SNIPPET::ALT::django_project_render]

Erstellen Sie das Verzeichnis `templates/`
und legen Sie darin die Datei `hello.html` mit folgendem Inhalt an:

[SNIPPET::ALT::django_project_template]

Damit Django Ihr Template findet, ergänzen Sie in 
`settings.py` die `DIRS`-Option in der
`TEMPLATES`-Konfiguration:

[SNIPPET::ALT::django_project_settings_dirs]

[EQ] Aktualisieren Sie die Browserseite. Was hat sich gegenüber der
vorherigen Ansicht geändert? Warum ist die Trennung von Darstellung
und Logik sinnvoll?
<!-- time estimate: 20 min -->

### Weiterführend

- [Project Structure](https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project) – Mehr zur Django-Projektstruktur
- [URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/) – Detaillierte Erklärungen zu URL-Konfiguration

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2]: `urls.py` importiert `views` und enthält `path("", views.hello, name="hello")`.
- [EREFR::3]: `views.py` verwendet `render()` (nicht `HttpResponse`); `templates/hello.html` enthält `{{ message }}`; `settings.py` setzt `DIRS` auf `[BASE_DIR / 'meinprojekt' / 'templates']`.
- [EREFQ::3]: Browser zeigt „Hello World!" als HTML-Seite; Student erklärt die Rolle von `path()` als Verbindung zwischen URL und View.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-project.md]

[ENDINSTRUCTOR]