title: Django Erstes Projekt erstellen und konfigurieren
stage: alpha
timevalue: 1
difficulty: 2
requires: django-basics
---

[SECTION::goal::idea,experience]

- Ich verstehe die Grundstruktur eines Django-Projekts, die Rolle der wichtigsten
  Konfigurationsdateien, und den Unterschied zwischen Project und App.
- Ich kann eine erste View-Funktion in einer App schreiben und mit einem URL verknüpfen.
- Ich kann Logik (view) und Layout (template) voneinander trennen.

[ENDSECTION]

[SECTION::background::default]

Ein Django-Projekt besteht aus mehreren Dateien und Ordnern, die zusammen eine Web-Anwendung bilden.
Das Verständnis der Projektstruktur, des URL-Routing und der Projektkonfiguration ist notwendig,
um HTTP-Anfragen zu verarbeiten und Web-Anwendungen zu entwickeln. Django unterscheidet dabei
zwischen dem Project (Gesamtkonfiguration) und Apps (Module für konkrete Funktionsbereiche):
Komponenten wie View, Template und Routing gehören deshalb in eine App: Die Aufteilung der
Geschäftslogik in Apps hält das Projekt wartbar, statt alles im Konfigurationsordner zu bündeln.

[ENDSECTION]

[SECTION::instructions::detailed]

### Django-Projektstruktur verstehen

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in
[PARTREF::django-basics] erstellt haben.

Ein neues Django-Projekt hat folgende Struktur:
```
meinprojekt/
├── manage.py                   # Django-Kommandozeilen-Tool
├── db.sqlite3                  # (wird automatisch erstellt)
└── meinprojekt/                # Projekt-Konfigurationsordner
    ├── __init__.py             # Python-Paket-Marker (leer)
    ├── settings.py             # Zentrale Projektkonfiguration
    ├── urls.py                 # URL-Routing-Konfiguration
    ├── wsgi.py                 # WSGI-Deployment-Konfiguration
    └── asgi.py                 # ASGI-Konfiguration für async/WebSockets
```

### Eine App erstellen

Ein Django-**Project** enthält die Gesamtkonfiguration einer Website. Konkrete Funktionsbereiche
(z. B. eine Blog-Funktion oder ein Kontaktformular) werden dagegen in einer **App** untergebracht —
einem eigenständigen Python-Paket innerhalb des Projekts. Ein Project kann mehrere Apps enthalten.
View, Template, Routing und Form gehören deshalb in eine App, nicht in den
Projekt-Konfigurationsordner `meinprojekt/`.

Erzeugen Sie eine neue App mit `startapp`:

```bash
python manage.py startapp webapp
```

```
meinprojekt/
├── meinprojekt/                # Projekt-Konfigurationsordner (siehe oben)
└── webapp/                     # neuer App-Ordner
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

Damit Django die App erkennt, muss sie zusätzlich in `settings.py` unter `INSTALLED_APPS`
eingetragen werden:

```python
INSTALLED_APPS = [
    ...
    'webapp',
]
```

[ER] Tragen Sie `'webapp'` in `INSTALLED_APPS` in `settings.py` ein.

[EQ] `startapp` legt den `webapp`-Ordner unabhängig von `INSTALLED_APPS` an — der Ordner
existiert also auch ohne den Eintrag. Warum schlägt `python manage.py startapp` trotzdem nicht
fehl, wenn Sie den Eintrag vergessen, obwohl Django die App dann nicht als installiert
betrachtet?

<!-- time estimate: 10 min -->

### Wichtige Konfigurationsdateien verstehen

**settings.py - Zentrale Projekteinstellungen**

Die `settings.py` enthält alle wichtigen Projekteinstellungen.
Öffnen Sie `settings.py` (in `meinprojekt/`) und betrachten Sie folgende wichtige
Abschnitte:

```python
[SNIPPET::ITREE:/Web/Django/django-project-settings.py::django_project_settings]
```

[EQ] Öffnen Sie `settings.py` und beantworten Sie: 
Was ist der aktuelle Wert von `DEBUG` und warum ist dies wichtig?

**manage.py - Projekt-Verwaltungsskript**

Die `manage.py` ist ein Wrapper-Skript im Projektroot, das die richtige
`DJANGO_SETTINGS_MODULE` für Ihr spezifisches Projekt setzt:

```python
[SNIPPET::ITREE:/Web/Django/django-project-manage.py::django_project_manage]
```

Damit ist `manage.py` der zentrale Zugriffspunkt für alle projektspezifischen Django-Befehle.
Welche Befehle das im Einzelnen sind, lernen Sie nach Bedarf in den folgenden Aufgaben kennen.

**views.py - View-Funktionen**

Eine **View** ist eine Python-Funktion, die einen HTTP-Request empfängt und eine
HTTP-Response zurückgibt.
Sie ist das Herzstück jeder Django-Anwendung. Technisch ließe sich eine View auch direkt im
Projekt-Konfigurationsordner ablegen, doch die App-Modularisierung erleichtert die Verwaltung
größerer Projekte erheblich — deshalb implementieren wir Views (und die übrigen Komponenten)
grundsätzlich innerhalb einer App.
Weitere Details zu Views finden Sie in [PARTREF::django-views].

[ER] `startapp` hat `views.py` bereits leer angelegt. Füllen Sie sie in Ihrer App `webapp`
mit folgendem Inhalt:

[SNIPPET::ALT::django_hello_view]

**urls.py - URL-Routing-Konfiguration**

Die `urls.py` definiert, welche URLs zu welchen Views führen. Jede App bekommt dafür eine eigene
`urls.py`, die das Projekt über `include()` einbindet — so bleibt das Routing der App bei der App,
und der Projekt-Konfigurationsordner sammelt nur die Verweise auf die Apps. Die zentrale Funktion
dafür ist `path()` mit drei Hauptparametern:

- `route`: der URL-Pfad (z.B. `""` für die Wurzel `/`)
- `view`: die View-Funktion, die bei einem Aufruf ausgeführt wird
- `name`: ein eindeutiger Name für die Route

Eine detaillierte Erklärung der `path()`-Funktion finden Sie in [PARTREF::django-views].

```python
[SNIPPET::ITREE:/Web/Django/django-project-urls.py::django_project_urls]
```

[EQ] Untersuchen Sie die bisherige Projekt-`urls.py` (in `meinprojekt/`). Welche Route ist
standardmäßig definiert, und warum existiert diese Route bereits, obwohl Sie sie nicht selbst
mit `path()` angelegt haben?

[ER] Erstellen Sie eine `urls.py` in der App `webapp` mit einer Route für Ihre neue View:

[SNIPPET::ALT::django_webapp_urls]

Binden Sie diese App-`urls.py` in der Projekt-`urls.py` mit `include()` ein:

[SNIPPET::ALT::django_project_urls2]

[HINT::Wie verbinde ich eine View mit einer URL?]
Zwei Schritte:

1. In der App-`urls.py`: `views`-Modul importieren (`from . import views`) und eine Route mit
   `path()` definieren: `path("pfad", views.funktionname, name="name")`.
2. In der Projekt-`urls.py`: die App-`urls.py` über
   `path("", include("webapp.urls"))` einbinden (`include` aus `django.urls` importieren).

Der leere String `""` bedeutet jeweils die Wurzel-URL (`/`).
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

[ER] Ersetzen Sie den Inhalt der `views.py` in Ihrer App `webapp` durch
folgende Version, die ein Template verwendet:

[SNIPPET::ALT::django_project_render]

Erstellen Sie in `webapp/` das Verzeichnis `templates/`
und legen Sie darin die Datei `hello.html` mit folgendem Inhalt an:

[SNIPPET::ALT::django_project_template]

In der `TEMPLATES`-Konfiguration von `settings.py` ist `APP_DIRS` bereits standardmäßig `True`.

[NOTICE]
Falls die Browserseite jetzt mit `TemplateDoesNotExist: hello.html` abstürzt, obwohl die Datei
existiert: Der Entwicklungsserver hatte beim Registrieren der App in `INSTALLED_APPS` bereits
einen veralteten Stand geladen. Beenden Sie ihn mit Strg+C und starten Sie ihn neu mit
`python manage.py runserver 8071` (oder Ihrem Port).
[ENDNOTICE]

[EQ] Aktualisieren Sie die Browserseite. Was hat sich gegenüber der
vorherigen Ansicht geändert? Warum ist die Trennung von Darstellung
und Logik sinnvoll?

[EQ] Anders als beim Erstellen der App (wo Sie `webapp` manuell in `INSTALLED_APPS` eintragen
mussten) mussten Sie `settings.py` diesmal nicht anfassen, damit Django Ihr Template findet.
Warum reicht hier die Ordnerstruktur allein aus?
<!-- time estimate: 20 min -->

### Weiterführend

- [Project Structure](https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project) – Mehr zur Django-Projektstruktur
- [URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/) – Detaillierte Erklärungen zu URL-Konfiguration
- [Applications](https://docs.djangoproject.com/en/stable/ref/applications/) – Details zum App-Konzept in Django

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFQ::1]: `'webapp'` ist in `INSTALLED_APPS` eingetragen; Student erkennt, dass
  `startapp` und die `INSTALLED_APPS`-Eintragung zwei unabhängige Schritte sind (Dateien anlegen
  vs. Django mitteilen, dass die App installiert ist), weshalb ein vergessener Eintrag nicht zu
  einem Fehler führt.
- [EREFR::3]: Die App-`urls.py` importiert `views` und enthält
  `path("", views.hello, name="hello")`; die Projekt-`urls.py` bindet sie mit
  `path("", include("webapp.urls"))` ein (`include` importiert).
- [EREFQ::3]: Student erkennt, dass die `admin/`-Route nicht selbst angelegt wurde, sondern von
  einer App stammt, die bereits ab Projekterstellung in `INSTALLED_APPS` eingetragen ist, genauso
  wie soeben `'webapp'`.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-project.md]

[ENDINSTRUCTOR]