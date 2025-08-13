title: Django Grundlagen und Installation
stage: alpha
timevalue: 2.0
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich verstehe die Grundkonzepte von Django, kann Django installieren und kenne die 
MTV-Architektur sowie die wichtigsten Anwendungsszenarien.
[ENDSECTION]

[SECTION::background::default]
Webentwicklung mit reinem Python ist möglich, aber mühsam: Man muss HTTP-Requests parsen, 
HTML generieren, Datenbanken anbinden und Sicherheitslücken vermeiden. 
Web-Frameworks wie Django nehmen einem diese Arbeit ab und bieten bewährte Lösungen 
für wiederkehrende Aufgaben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist Django?

Django ist ein in Python geschriebenes Open-Source-Web-Framework, das die schnelle 
Entwicklung von vollständigen Webanwendungen ermöglicht. 
Mit Django können Python-Entwickler mit wenig Code professionelle Websites erstellen, 
die alle wichtigen Funktionen einer modernen Webanwendung bieten.

Django folgt der Philosophie **"Don't Repeat Yourself" (DRY)** und bietet viele 
eingebaute Funktionen, die Entwicklern helfen, sich auf die Geschäftslogik zu konzentrieren, 
anstatt Grundfunktionen neu zu implementieren.

(Optional) Weitere Informationen finden Sie in der offiziellen Dokumentation: 
[Django Overview](https://docs.djangoproject.com/en/stable/intro/overview/)

[EQ] Nennen Sie drei große Websites, die Django verwenden. 
Nutzen Sie dafür die Django-Website oder andere Quellen.
<!-- time estimate: 15 min -->

### Django-Philosophie und Kernprinzipien

Django basiert auf mehreren wichtigen Designprinzipien:

**DRY (Don't Repeat Yourself)**: Vermeidung von Code-Duplikation durch Wiederverwendung 
von Komponenten wie Templates, Modellen und Views.

**Convention over Configuration**: Django bietet sinnvolle Standardkonfigurationen 
(z.B. automatisch generierte Admin-Oberfläche), um Entscheidungsaufwand zu reduzieren.

**Rapid Development**: Schnelle Entwicklung von Prototypen bis hin zu produktionsreifen 
Anwendungen.

(Optional) Mehr Details zu Django's Design-Philosophie: 
[Django Design Philosophy](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)

[EQ] Erklären Sie in eigenen Worten, was "Convention over Configuration" bedeutet.
<!-- time estimate: 10 min -->

### MTV-Architektur vs. MVC

Django verwendet das **MTV (Model-Template-View)**-Muster, eine Variante des bekannten 
**MVC (Model-View-Controller)**-Musters:

**Model**: Verwaltet Daten und Geschäftslogik, kommuniziert mit der Datenbank.

**Template**: Zuständig für die Darstellung, generiert HTML-Ausgabe.

**View**: Fungiert als Controller, verarbeitet Requests und koordiniert Model und Template.

**Ablauf in Django**:

- URL-Request wird an entsprechende View weitergeleitet (`urls.py`)
- View verarbeitet Request und ruft Model-Daten ab
- View übergibt Daten an Template
- Template rendert HTML und sendet Response zurück

(Optional) Vergleichen Sie mit der traditionellen MVC-Architektur: 
[MVC vs MTV](https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/)


### Django's eingebaute Funktionen

Django bietet zahlreiche eingebaute Features:

| Funktion | Beschreibung |
|----------|--------------|
| **Admin Backend** | Automatisch generierte Verwaltungsoberfläche |
| **ORM** | Object-Relational Mapping für Datenbankoperationen |
| **Formular-Handling** | Eingebaute Validierung und CSRF-Schutz |
| **Benutzer-Authentifizierung** | Login, Registrierung, Rechteverwaltung |
| **URL-Routing** | Flexible URL-Zuordnung mit Regex-Unterstützung |
| **Caching** | Unterstützung für Memcached, Redis etc. |

(Optional) Detaillierte Übersicht der Features: 
[Django Features](https://www.djangoproject.com/start/overview/)

[EQ] Recherchieren Sie für **Admin Backend**, **ORM**, **Formular-Handling** jeweils 
ein konkretes Anwendungsbeispiel.
<!-- time estimate: 25 min -->

### Anwendungsszenarien für Django

**Geeignet für Django**:

- Content Management Systeme (CMS)
- Social Media Plattformen
- E-Commerce Websites
- API-Backends (mit Django REST Framework)
- Datengetriebene Webanwendungen

**Weniger geeignet**:

- Hochperformante Echtzeitsysteme
- Sehr leichtgewichtige Microservices
- Anwendungen mit extremen Performance-Anforderungen

**Django vs. andere Frameworks**:

- **Flask**: Leichtgewichtiger, mehr Flexibilität, weniger eingebaute Features
- **FastAPI**: Fokus auf APIs, asynchrone Unterstützung, moderne Python-Features
- **Ruby on Rails**: Ähnliche Philosophie, aber in Ruby

[EQ] Bewerten Sie, ob Django für folgende Projekte geeignet wäre und begründen Sie:

1. Ein Online-Shop mit 10.000 Produkten
2. Eine Chat-Anwendung mit Echtzeit-Messaging
3. Ein Blog mit 50 Artikeln
4. Eine REST-API für eine Mobile App
<!-- time estimate: 20 min -->


### Entwicklungsumgebung einrichten und  Django Installation

**Empfohlene Entwicklungstools**:

- **VS Code** mit Python-Extension
- **PyCharm**
- **Sublime Text** mit Python-Paketen

Bevor Sie Django installieren können, muss Python auf Ihrem System verfügbar sein. 
Django unterstützt Python 3.8 oder höher.

**Installation mit pip**:
```bash
pip install Django
```

**Spezifische Version installieren (hier z.B. 5.2.5)**:
```bash
pip install Django==5.2.5
```

**Installation mit Paketmanager (Linux)**:
```bash
# Ubuntu/Debian
sudo apt-get install python3-django

# CentOS/RHEL
sudo yum install python3-django
```

(Optional) Weitere Installationsanleitung: 
[Django Installation Guide](https://www.w3schools.com/django/django_install_django.php)

**Virtuelle Umgebung erstellen** (empfohlen):
```bash
python -m venv django_env
python3 -m venv django_env      # python3 unter Linux ist manchmal notwendig

source django_env/bin/activate  # Linux/Mac
django_env\Scripts\activate     # Windows

pip install Django
```

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

[EC] Installieren Sie Django in einer virtuellen Umgebung mit Name `django_lern_env` auf Ihrem System und dokumentieren Sie die verwendeten Befehle.

[EC] Überprüfen Sie die Installation mit folgendem Befehl und notieren Sie die Ausgabe:
```bash
python -m django --version
```
[EC] Erstellen Sie ein Django-Projekt namens `testprojekt` und starten Sie den 
Entwicklungsserver. 

<!-- time estimate: 30 min -->

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

(Optional) Mehr zur 
[Project Structure](https://docs.djangoproject.com/en/stable/intro/tutorial01/#creating-a-project)

[EC] Erkunden Sie die Projektstruktur und listen Sie alle erstellten Dateien und 
Ordner. Benutzen Sie dazu den `tree`-Befehl oder ähnliche Tools:
```bash
sudo apt update
sudo apt install tree
tree meinprojekt
```

<!-- time estimate: 15 min -->
[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
Reichen Sie Ihre Installationsbefehle und Projektstruktur ein.

[INCLUDE::/_include/Submission-Markdowndokument.md]
Dokumentieren Sie Ihre Antworten zu den Recherche- und Analyseaufgaben.
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
Die Studierenden sollten:

- Django erfolgreich installiert haben
- Die MTV-Architektur verstehen
- Ein funktionsfähiges Django-Projekt erstellt haben
- Die Grundlagen der Django-Philosophie erklären können
- Anwendungsszenarien bewerten können

Typische Stolpersteine:

- Python-Version-Kompatibilität
- Virtuelle Umgebungen nicht verwendet
- Firewall-Probleme beim Entwicklungsserver

### Fragen
[INCLUDE::ALT:django-basics.md]

### Kommandoprotokoll
[PROT::ALT:django-basics.prot]

[ENDINSTRUCTOR]