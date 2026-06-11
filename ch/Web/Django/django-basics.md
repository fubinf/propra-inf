title: Django installieren und erstes Projekt starten
stage: alpha
timevalue: 0.5
difficulty: 2
---

[SECTION::goal::experience]
Ich kann Django in einer virtuellen Umgebung installieren, ein erstes Django-Projekt erstellen 
und im Browser die Django-Willkommensseite aufrufen.
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

### Django installieren

Bevor Sie Django installieren, müssen Sie Python auf Ihrem System verfügbar haben. 
Django unterstützt Python 3.8 oder höher. Nutzen Sie eine virtuelle Umgebung, 
um Ihre Entwicklungsabhängigkeiten isoliert zu halten.

**Schritt 1: Virtuelle Umgebung erstellen und aktivieren**:
```bash
python3 -m venv django_lern_env
source django_lern_env/bin/activate    # Linux/Mac
django_lern_env\Scripts\activate       # Windows
```

**Schritt 2: Django im venv installieren**:
```bash
pip install Django
```

**Schritt 3: Installation überprüfen**:
```bash
python -m django --version
```

[EC] Installieren Sie Django in einer virtuellen Umgebung auf Ihrem System und dokumentieren Sie die Befehle.

[EC] Überprüfen Sie die Installation und dokumentieren Sie die Ausgabe von `python -m django --version`.

<!-- time estimate: 15 min -->

### Erstes Projekt erstellen

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

[EC] Erstellen Sie ein Django-Projekt namens `meinprojekt`, starten Sie den Server und öffnen Sie die Willkommensseite im Browser.

### Weiterführend

- [Django: Quick install guide](https://docs.djangoproject.com/en/stable/topics/install/) – offizielle Installationsanleitung
- [Das offizielle Django-Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) – schrittweiser Einstieg in Django

Im nächsten Schritt erkunden Sie die Projektstruktur und schreiben Ihren ersten View:
[PARTREF::django-project]

<!-- time estimate: 15 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
Reichen Sie Ihre Installations- und Startbefehle ein.

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Kommandoprotokoll
[PROT::ALT:django-basics.prot]

Knackpunkte:

- Django wurde innerhalb eines venv installiert, nicht systemweit.
- `django-admin startproject` und `runserver` wurden erfolgreich ausgeführt.
- Die Django-Willkommensseite ist im Browser unter http://127.0.0.1:8000/ sichtbar.

[ENDINSTRUCTOR]