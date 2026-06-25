title: Django Erstes Projekt erstellen und konfigurieren
stage: alpha
timevalue: 1.0
difficulty: 2
requires: django-basics
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundstruktur eines Django-Projekts.
- Ich kenne die Rollen der wichtigsten Konfigurationsdateien.
- Ich kann den Django-Entwicklungsserver starten.

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

[EC] Erkunden Sie die Projektstruktur und listen Sie alle erstellten Dateien und 
Ordner. Benutzen Sie dazu den `tree`-Befehl:
```bash
sudo apt update
sudo apt install tree
tree meinprojekt
```
<!-- EC1 -->
<!-- time estimate: 10 min -->

### Wichtige Konfigurationsdateien verstehen

**settings.py - Zentrale Projekteinstellungen**

Die `settings.py` enthält alle wichtigen Projekteinstellungen.
Öffnen Sie `meinprojekt/settings.py` und betrachten Sie folgende wichtige Abschnitte:

```python
[SNIPPET::ITREE:/Web/Django/django-project-settings.py::django_project_settings]
```

[EQ] Öffnen Sie `settings.py` und beantworten Sie: 
Was ist der aktuelle Wert von `DEBUG` und warum ist dies wichtig?
Welche Datenbank wird standardmäßig verwendet?
Wie viele Apps sind in `INSTALLED_APPS` vorkonfiguriert?
<!-- EQ1 -->

**manage.py - Projekt-Verwaltungsskript**

Die `manage.py` ist ein Wrapper-Skript im Projektroot, das die richtige `DJANGO_SETTINGS_MODULE` für Ihr spezifisches Projekt setzt:

```python
[SNIPPET::ITREE:/Web/Django/django-project-manage.py::django_project_manage]
```

Damit ist `manage.py` der zentrale Zugriffspunkt für alle projektspezifischen Django-Befehle.
Weitere Details zu den verfügbaren Befehlen finden Sie in [PARTREF::django-admin].

<!-- time estimate: 20 min -->

**views.py - View-Funktionen**

Eine **View** ist eine Python-Funktion, die ein HTTP-Request empfängt und eine HTTP-Response zurückgibt.
Sie ist das Herzstück jeder Django-Anwendung.
Weitere Details zu Views finden Sie in [PARTREF::django-views].

[ER] Erstellen Sie die Datei `meinprojekt/meinprojekt/views.py`:
<!-- ER1 -->

[SNIPPET::ALT::django_hello_view]

**urls.py - URL-Routing-Konfiguration**

Die `urls.py` definiert, welche URLs zu welchen Views führen.
Nach der View-Erstellung müssen Sie Ihre neue View in `urls.py` registrieren:

```python
[SNIPPET::ITREE:/Web/Django/django-project-urls.py::django_project_urls]
```

[EQ] Untersuchen Sie `meinprojekt/urls.py`. Welche Route ist standardmäßig definiert?
<!-- EQ2 -->

[ER] Modifizieren Sie `meinprojekt/meinprojekt/urls.py`, um Ihre neue View einzubinden:
<!-- ER2 -->

```python
[SNIPPET::ITREE:/Web/Django/django-project-urls2.py::django_project_urls2]
```

[HINT::Wie verbinde ich eine View mit einer URL?]
Die `urls.py` verbindet URL-Pfade mit View-Funktionen.
Sie müssen:

1. Das `views`-Modul importieren: `from . import views`
2. Eine Route mit `path()` definieren: `path("pfad", views.funktionname, name="name")`

Der leere String `""` bedeutet die Wurzel-URL (`/`).
[ENDHINT]

[NOTICE]
Der Django-Entwicklungsserver lädt Code-Änderungen automatisch neu.
Sie müssen den Server nicht manuell neustarten!
[ENDNOTICE]

[EQ] Aktualisieren Sie die Browserseite. Was sehen Sie jetzt anstelle der Willkommensseite?
Erklären Sie, warum die `urls.py`-Konfiguration notwendig ist, um die View zu sehen.
<!-- time estimate: 20 min -->
<!-- EQ3 -->

### Projektstruktur dokumentieren

[EC] Erstellen Sie eine vollständige Übersicht Ihrer finalen Projektstruktur 
mit dem `tree`-Befehl.
<!-- EC2 -->

<!-- time estimate: 5 min -->

### Weiterführend

- [Project Structure](https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project) – Mehr zur Django-Projektstruktur
- [URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/) – Detaillierte Erklärungen zu URL-Konfiguration

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

Knackpunkte:

- views.py: Die Datei muss eine Funktion enthalten, die ein `request`-Parameter akzeptiert und ein `HttpResponse`-Objekt zurückgibt.
- urls.py: Die Datei muss das `views`-Modul importieren und einen `path()` mit dem neuen View in `urlpatterns` registrieren.
- Funktionalität: Die URL-Route muss auf die View-Funktion verweisen und "Hello World!" zurückgeben.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-project.md]

### Kommandoprotokoll
[PROT::ALT:django-project.prot]

[ENDINSTRUCTOR]