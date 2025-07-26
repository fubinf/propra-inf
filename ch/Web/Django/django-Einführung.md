title: Django Einführung
stage: alpha
timevalue: 1.5
difficulty: 2
---
[SECTION::goal::idea,experience]
Ich kann Django installieren und ein neues Projekt starten sowie 
die MTV-Architektur verstehen und von MVC abgrenzen.
Ich kann Django mit anderen Python-Webframeworks (Flask, FastAPI) vergleichen und 
typische Anwendungsfälle für Django benennen.
[ENDSECTION]

[SECTION::background::default]
Webentwicklung mit reinem Python ist für einfache Skripte oft ausreichend.
Bei komplexeren Webanwendungen mit Datenbanken, Benutzerauthentifizierung und 
dynamischen Inhalten stoßen wir schnell an Grenzen.
Hier bieten Web-Frameworks wie Django standardisierte Lösungen und 
bewährte Architekturprinzipien.
[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist Django? 

`Django` ist ein High-Level Webframework in Python, das schnelle Entwicklung von 
sicheren und wartbaren Websites ermöglicht. Es wurde 2005 veröffentlicht und folgt 
dem "Batteries included"-Prinzip – viele benötigte Komponenten für Webanwendungen 
sind bereits integriert.

Große Organisationen wie Instagram oder Mozilla verwenden `Django` für ihre 
Webanwendungen, was die Reife und Skalierbarkeit des Frameworks unterstreicht.

`Django` eignet sich besonders für datengetriebene Webanwendungen wie 
Content-Management-Systeme, E-Commerce-Plattformen oder Social-Media-Anwendungen.

### Integrierte Funktionen und Kernmerkmale

`Django` bietet zahlreiche vorkonfigurierte Komponenten für typische Webanwendungen:

`Django` verfügt über ein `Admin-Backend` mit automatisch generierter Verwaltungsoberfläche ohne manuelle CRUD-Implementierung, ein `ORM` (Object-Relational Mapping) zur Manipulation von Datenbanken mit Python-Klassen statt SQL-Befehlen, eine integrierte `Formularbehandlung` mit Validierung und CSRF-Schutz (Cross-Site Request Forgery), fertige `Benutzerverwaltung` für Anmeldung, Registrierung und Berechtigungen (`django.contrib.auth`), ein flexibles `Routing-System` mit Unterstützung für reguläre Ausdrücke sowie `Cache-Mechanismen` für verschiedene Backends wie `Memcached` oder `Redis`.

[EQ] Erklären Sie, was das "Batteries included"-Prinzip von Django bedeutet und welche Vorteile es für Entwickler bietet.

`Django` zeichnet sich durch folgende Kernmerkmale aus:

`Django` ermöglicht `Schnelle Entwicklung` durch vorgefertigte Komponenten, die den Fokus auf Geschäftslogik erlauben, bietet hohe `Sicherheit` mit integriertem Schutz gegen gängige Angriffe wie SQL-Injection, XSS und CSRF, garantiert `Skalierbarkeit`, da das Framework für hohe Lasten konzipiert wurde und mit dem Projekt mitwächst, fördert durch das `DRY-Prinzip` (Don't Repeat Yourself) die Code-Wiederverwendung und klare Strukturen und unterstützt `Erweiterbarkeit` durch eine große Auswahl an Drittanbieter-Paketen wie `Django REST framework` oder `Django CMS`.

[ER] Beschreiben Sie, warum die Kombination aus Admin-Interface und ORM Django besonders 
produktiv für datengetriebene Anwendungen macht. Nennen Sie mindestens zwei konkrete Vorteile.

Weitere Informationen finden Sie in der [Django 5.2](https://docs.djangoproject.com/en/5.2/)

<!-- time estimate: 10 min -->


### MTV-Architektur: `Model`, `Template`, `View`

`Django` orientiert sich an der bekannten `MVC`-Architektur, verwendet aber eine 
abgewandelte Terminologie: das Model-Template-View (`MTV`) Muster.

**Model:** Die Datenschicht definiert Datenmodelle als `ORM`-Klassen und stellt 
die Schnittstelle zur Datenbank dar (SQLite, MySQL, PostgreSQL).

**View:** Die Geschäftslogik verarbeitet HTTP-Anfragen, ruft Daten vom Model ab 
und übergibt sie an Templates. Entspricht dem Controller im klassischen `MVC`.

**Template:** Die Präsentationsschicht bereitet Daten für die HTML-Ausgabe auf 
und enthält das statische Gerüst mit Platzhaltern für dynamische Inhalte.

Weitere Details zur [Architektur](https://docs.djangoproject.com/en/5.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template
-how-come-you-don-t-use-standard-names)

[EQ] Der klassische Controller wird in `Django` weitgehend vom Framework selbst 
abgedeckt durch das URL-Routing und die Zuordnung zu View-Funktionen.

[ER] Erklären Sie den Unterschied zwischen `MVC` und `MTV` in `Django`. 
Welche Komponente übernimmt die Rolle des Controllers?
<!-- time estimate: 15 min -->


### Django-Installation: `pip install Django`

Um `Django` nutzen zu können, muss zunächst Python (Empfehlung: Python 3.10 oder höher) 
installiert sein. `Django` wird über `pip` (Python Package Installer) installiert.

**Windows:** Öffnen Sie eine Kommandozeile und installieren Sie `Django`:
```
py -m pip install Django
```

**Linux/macOS:** Verwenden Sie den entsprechenden Python-Interpreter:
```
python3 -m pip install Django
```

Der Befehl `py -m pip` stellt unter Windows sicher, dass das richtige Python 
verwendet wird. Unter Unix-Systemen heißt der Python 3 Interpreter meist `python3`.

Nach erfolgreicher Installation können Sie die `Django`-Version überprüfen:
```
python -m django --version
```

Dies gibt die installierte Versionsnummer aus (z.B. 4.2.1 oder 5.2.1).
Weitere Installationsdetails: [HREF::https://docs.djangoproject.com/en/5.1/topics/install/]

[ER] Installieren Sie `Django` auf Ihrem System und überprüfen Sie die Version. 
Welchen Befehl verwenden Sie jeweils unter Windows und Linux/macOS?

[ER] Was bedeutet der Parameter `-m` in `python -m django --version`?
<!-- time estimate: 20 min -->


### Erstes Django-Projekt: `django-admin startproject`

Nach der Installation können Sie ein neues `Django`-Projekt anlegen. `Django` 
bringt das Tool `django-admin` mit, das verschiedene Administrations-Befehle 
zur Verfügung stellt.

Um ein neues Projekt zu erstellen, verwenden Sie:
```
django-admin startproject mysite
```

Dadurch wird ein neuer Ordner `mysite` in Ihrem aktuellen Verzeichnis angelegt 
mit folgender Struktur:

- `manage.py`: Skript zur Projektverwaltung (Server starten, Migrationen etc.)
- `mysite/`: Python-Paket mit den Projektdateien
  - `settings.py`: Einstellungsdatei für das Projekt
  - `urls.py`: URL-Konfigurationsdatei 
  - `wsgi.py`: Konfiguration für WSGI-Server
  - `asgi.py`: Konfiguration für ASGI-Server
  - `__init__.py`: Python-Paket-Markierung

Mit `python manage.py runserver` können Sie den Entwicklungswebserver starten.
Weitere Projektdetails: [HREF::https://docs.djangoproject.com/en/5.1/intro/tutorial01/]

[ER] Erstellen Sie ein `Django`-Projekt namens "mysite" und beschreiben Sie 
die wichtigsten generierten Dateien und deren Zweck.

[ER] Was ist der Unterschied zwischen `django-admin` und `manage.py`?
<!-- time estimate: 25 min -->


### Framework-Vergleich: `Django` vs. `Flask` vs. `FastAPI`

**Django:** Vollständiges Framework mit integrierter `ORM`, Admin-Interface, 
Authentifizierung und Template-System. Ideal für komplette Webanwendungen 
mit Datenbank-Anbindung.

**Flask:** Microframework mit minimalen Grundkomponenten (Routing, Templates). 
Bietet mehr Flexibilität, erfordert aber zusätzliche Bibliotheken für 
erweiterte Funktionen wie `ORM` oder Authentifizierung.

**FastAPI:** Modernes Framework für Web-APIs mit asynchronen Features und 
automatischer Dokumentation. Optimiert für JSON-APIs und Microservices, 
aber ohne Template-System oder Admin-Interface.

Übersicht der Unterschiede: 
[HREF::https://testdriven.io/blog/fastapi-vs-flask/]

[EQ] `Django` ist "batteries included", `Flask` ist minimal und erweiterbar, 
`FastAPI` ist API-fokussiert und hochperformant.

[ER] Nennen Sie je einen Vorteil von `Django`, `Flask` und `FastAPI`. 
Für welche Art von Projekt würden Sie welches Framework wählen?

[ER] Warum eignet sich `Django` besonders gut für Content-Management-Systeme?
<!-- time estimate: 20 min -->
[ENDSECTION]


[SECTION::submission::information,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
