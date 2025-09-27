title: Django
---

[TERMREF::Django] ist ein in Python geschriebenes, hochentwickeltes Webframework, das die schnelle und sichere Entwicklung moderner Webanwendungen ermöglicht. Es folgt dem sogenannten **MTV-Architekturmuster** (Model-Template-View), das eng mit dem bekannten MVC-Prinzip verwandt ist.

Mit Django lassen sich komplexe Webanwendungen mit **wenig Code** und **klarer Struktur** erstellen. Dank seiner zahlreichen integrierten Komponenten wie einem **Object-Relational Mapper (ORM)**, einem **automatisch generierten Admin-Interface**, einem **flexiblen URL-Routing-System** und integrierter **Formularverarbeitung** ist Django besonders gut für datengetriebene Anwendungen geeignet.

Typische Anwendungsbereiche sind:

- Content-Management-Systeme (z. B. Blogs, Nachrichtenseiten)
- Soziale Netzwerke und Plattformen mit Benutzerverwaltung
- E-Commerce-Systeme mit Warenkorb und Bezahlfunktion
- REST-APIs in Kombination mit Django REST framework

Django legt großen Wert auf **Sicherheit**: Es schützt standardmäßig vor SQL-Injection, Cross-Site-Scripting (XSS), Cross-Site-Request-Forgery (CSRF) und anderen häufigen Web-Angriffen. Zudem verfolgt es die Philosophie **„Don’t Repeat Yourself“ (DRY)** und **„Konvention vor Konfiguration“**, was zu effizientem und wartbarem Code führt.

Die Installation von Django erfolgt meist über `pip`:

```bash
python -m pip install Django
```

Gute Quellen für Django:

- [Offizielle Dokumentation](https://docs.djangoproject.com/)

- [Django Girls Tutorial](https://tutorial.djangogirls.org/)

- [Mozilla Developer Network](https://developer.mozilla.org/de/docs/Learn_web_development/Extensions/Server-side/Django)

Django ist „batteries included": Viele Funktionen, die bei anderen Frameworks nachinstalliert werden müssen, sind bereits enthalten. Es ist damit ideal für Entwickler:innen, die schnell produktive Webanwendungen erstellen möchten – ohne auf Flexibilität oder Erweiterbarkeit zu verzichten.

---

## Diese Aufgabengruppe: Lernpfad und Aufgabenübersicht

Die Django-Aufgaben in diesem Kapitel bauen systematisch aufeinander auf und folgen dem MTV-Architekturmuster:

### 1. Grundlagen (Einstieg)

- **[django-basics](django-basics.html)**: Installation und Konzepte (1.5h)
    - Django installieren und konfigurieren
    - MTV-Architektur verstehen
    - Django-Philosophie und Anwendungsbereiche
    - Entwicklungsumgebung einrichten

- **[django-project](django-project.html)**: Erstes Projekt erstellen (2.0h)
    - `django-admin startproject` verwenden
    - Projektstruktur verstehen (`settings.py`, `urls.py`, `manage.py`)
    - Entwicklungsserver starten
    - Erste View-Funktionen und URL-Routing

### 2. Kernkomponenten

- **[django-admin](django-admin.html)**: Kommandozeilen-Tool beherrschen (1.25h)
    - `django-admin` und `manage.py` Befehle
    - Apps erstellen mit `startapp`
    - Datenbankmigrationen durchführen
    - Superuser erstellen und Admin-Interface nutzen

- **[django-views](django-views.html)**: Request/Response-Verarbeitung (2.0h)
    - View-Funktionen erstellen
    - Request-Objekt analysieren (GET/POST-Daten)
    - Response-Objekte: `HttpResponse`, `render()`, `redirect()`
    - HTTP-Parameter verarbeiten

- **[django-routing](django-routing.html)**: URL-Konfiguration (1.5h)
    - URL-Patterns mit `path()` und `re_path()`
    - Reguläre Ausdrücke in URLs
    - URL-Konfiguration mit `include()` aufteilen
    - Reverse Resolution und Namespaces

### 3. Datenschicht und Präsentation

- **[django-model](django-model.html)**: Datenmodellierung mit ORM (2.25h)
    - Django-Modelle definieren
    - Datenbankmigrationen erstellen und anwenden
    - CRUD-Operationen (Create, Read, Update, Delete)
    - Model-Beziehungen und Queries

- **[django-template](django-template.html)**: Frontend-Entwicklung (2.0h)
    - Template-System verstehen
    - Template-Variablen und -Tags verwenden
    - Template-Vererbung für wiederverwendbare Layouts
    - Statische Dateien einbinden

### 4. Erweiterte Funktionen

- **[django-form](django-form.html)**: Formularverarbeitung (1.5h)
    - HTML-Formulare erstellen und verarbeiten
    - GET vs. POST-Methoden verstehen
    - CSRF-Schutz implementieren
    - Formulardaten validieren und speichern

**Empfohlene Reihenfolge**: Die Aufgaben sollten in der angegebenen Reihenfolge bearbeitet werden, da sie aufeinander aufbauen. Jede Aufgabe erweitert das Verständnis des MTV-Musters um eine weitere Komponente.

**Tipp**: Halten Sie Ihr Django-Projekt während aller Aufgaben aktiv und erweitern Sie es schrittweise. So entsteht am Ende eine vollständige Webanwendung, die alle gelernten Konzepte integriert!