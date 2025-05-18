title: Django Einführung
stage: alpha
timevalue: 1.5
difficulty: 2
---
[SECTION::goal::product]

- Ich kann Django installieren und ein neues Projekt starten.
- Ich kann den Unterschied zwischen MTV und MVC erklären.
- Ich kann den Unterschied zwischen Flask, Fastapi und Django erklären.
- Ich kenne typische Anwendungsfälle für den Einsatz von Django.

[ENDSECTION]

[SECTION::background::default]
### Was ist Django?
- Django ist ein High-Level Webframework in Python, das eine schnelle Entwicklung von sicheren und wartbaren Websites ermöglicht
developer.mozilla.org
- Es wurde erstmals 2005 veröffentlicht und wird seither aktiv weiterentwickelt. Django folgt dem Prinzip „Batteries included“ – viele benötigte Komponenten für Webanwendungen bringt es bereits mit. Dadurch können Entwickler Anwendungen vom Konzept bis zur Umsetzung sehr zügig realisieren
djangoproject.com
- Django kommt in vielfältigen Projekten zum Einsatz, z. B. bei Social-Media-Plattformen, E-Commerce-Seiten, Nachrichtenportalen oder Unternehmens-Websites
blog.jetbrains.com
- Große Organisationen wie Instagram oder Mozilla verwenden Django für ihre Webanwendungen (was die Reife und Skalierbarkeit des Frameworks unterstreicht). 
### MTV-Architektur von Django
- Django orientiert sich an der bekannten MVC-Architektur (Model-View-Controller), verwendet aber eine leicht abgewandelte Terminologie: das Model-Template-View (MTV) Muster
stackoverflow.com
- Die Aufgaben verteilen sich folgendermaßen:
### Model: 
- Die Datenzugriffsschicht – hier werden Datenmodelle definiert und verwaltet (typischerweise als ORM-Klassen, die mit relationalen Datenbanken wie SQLite, MySQL, PostgreSQL usw. verbunden sind). Das Model entspricht dem Model im MVC-Prinzip und stellt die Schnittstelle zur Datenbank dar
stackoverflow.com

### View: 
- Die Geschäftsschicht – hier steht die Anwendungslogik. Eine Django-View ist typischerweise eine Python-Funktion (oder Methode), die Anfragen entgegennimmt, entsprechende Daten vom Model abruft und diese an ein Template übergibt. Die View in Django übernimmt somit die Rolle des Controllers im klassischen MVC
stackoverflow.com
- Django selbst sorgt mittels URL-Routing dafür, dass die richtige View-Funktion für eine gegebene URL aufgerufen wird (d.h. einen Großteil der Controller-Aufgabe übernimmt bereits das Framework)
blog.csdn.net

### Template: 
- Die Präsentationsschicht – hier werden die Daten für die Ausgabe aufbereitet, meist als HTML-Seiten. Ein Template enthält das statische Gerüst (HTML, CSS) und Platzhalter bzw. Template-Sprachen-Konstrukte für dynamische Inhalte. Das Template entspricht dem View im MVC (also der Darstellung)
stackoverflow.com
- Django nutzt standardmäßig seine eigene Templatesprache, unterstützt aber auch alternative Template-Engines.
Zusammengefasst implementiert Django also ein MVC-ähnliches Pattern, wobei Djangos „View“ der Logik/Controller-Schicht entspricht und Templates die Darstellung übernehmen
stackoverflow.com
- Der klassische Controller wird weitgehend vom Framework abgedeckt (durch das Mapping der URLs auf View-Funktionen)
blog.csdn.net
- Dieses MTV-Muster trägt zu einer klaren Trennung von Datenmodell, Anwendungslogik und Benutzeroberfläche bei. 
### Vorteile von Django
- Django bietet zahlreiche Vorteile, die es gerade für größere Webprojekte attraktiv machen:
### Umfangreiche Ausstattung: 
- Als vollwertiges Framework bringt Django viele Funktionen out of the box mit. Zu den eingebauten Modulen gehören u. a. Authentifizierung, Verwaltung von Benutzerrechten, Sessions, Caching, Formularverarbeitung und eine Template-Engine
blog.jetbrains.com
- Django folgt dem DRY-Prinzip (Don’t Repeat Yourself), was die Entwicklung beschleunigt und Fehler reduziert. Außerdem stellt das Framework ein ORM (Object-Relational Mapping) bereit, um mit relationalen Datenbanken zu arbeiten, ohne SQL direkt schreiben zu müssen
blog.jetbrains.com


### Administrationsoberfläche: 
- Django kommt mit einem integrierten Admin-Interface. Dieses erlaubt schnelle CRUD-Operationen (Datensätze erstellen, lesen, ändern, löschen) über eine generierte Weboberfläche – und das nahezu ohne eigenen Code
salomvary.com
- Dadurch kann Django direkt als einfaches Content-Management-System dienen, was besonders bei inhaltsbasierten Anwendungen enorme Entwicklungszeit spart.
### Schnelle Entwicklung: 
- Durch den hohen Abstraktionsgrad und die mitgelieferten Komponenten kann man Django-Projekte sehr zügig aufsetzen. Für viele standardmäßige Anforderungen (Login, Formulare, Datenbankmigrationsskripte etc.) existieren sofort nutzbare Lösungen. Es eignet sich hervorragend für nahezu jede CRUD-Webanwendung, die damit in kurzer Zeit erstellt werden kann
netguru.com
- Sicherheit: Das Framework legt großen Wert auf Sicherheit und bringt Schutzmechanismen gegen häufige Web-Sicherheitslücken von Haus aus mit (z. B. gegen Cross-Site Scripting, SQL-Injection, Cross-Site Request Forgery und Clickjacking)
blog.jetbrains.com
- Als Entwickler muss man diese Aspekte nicht komplett selbst implementieren, was sicherere Anwendungen bei weniger Aufwand ermöglicht.
### Community und Erweiterbarkeit: 
- Django ist seit vielen Jahren im Einsatz und hat eine große, aktive Community. Es gibt eine Fülle von Drittanbieter-Packages (für nahezu jede erdenkliche Funktion) sowie eine exzellente Dokumentation
blog.jetbrains.com
- Bei Problemen findet man schnell Hilfe in Foren oder Communities. Die Architektur mit wiederverwendbaren Apps ermöglicht es zudem, Module einfach in neue Projekte zu integrieren oder eigene Komponenten zu schreiben.
Trotz dieser Vorteile sollte man beachten, dass Django ein “schwergewichtiges” Framework ist. Für sehr kleine oder simple Projekte kann der Overhead groß sein – hier sind Mikro-Frameworks wie Flask oft besser geeignet
blog.jetbrains.com
- Django bringt eine gewisse Lernkurve mit sich, da die Fülle an Optionen anfangs überwältigend wirken kann. Auch in puncto Performance ist Django durch seine Allgemeinheit manchmal etwas langsamer als spezialisierte Lösungen; moderne Frameworks wie FastAPI (die auf asynchrone Programmierung und reine API-Entwicklung optimiert sind) können bei reinen JSON-APIs eine höhere Geschwindigkeit erreichen
blog.jetbrains.com
- Nichtsdestotrotz lässt sich Django für große Last durch Caching, Datenbank-Optimierungen und Skalierung (z.B. horizontales Skalieren der App-Server) durchaus leistungsfähig betreiben. 

### Installation von Django
- Um Django nutzen zu können, muss zunächst Python (Empfehlung: Python 3.10 oder höher) auf dem System installiert sein. Django selbst wird bequem über pip (Python Package Installer) installiert. Die grundlegenden Schritte sind unter verschiedenen Betriebssystemen ähnlich, können sich aber in der Befehlsnotation leicht unterscheiden:
- Windows: Öffnen Sie eine Kommandozeile (Eingabeaufforderung CMD oder PowerShell) und installieren Sie Django über den Python-Launcher mit pip:
```
py -m pip install Django
```

(Der Befehl py -m pip stellt sicher, dass das richtige Python benutzt wird. Alternativ kann – falls in PATH – auch direkt pip install Django verwendet werden.)
- Linux/macOS: Öffnen Sie ein Terminal und führen Sie den Installationsbefehl mit dem entsprechenden Python-Interpreter aus, z. B.:
```
python3 -m pip install Django
```

Unter Unix-Systemen heißt der Python 3 Interpreter häufig python3 (um ihn von Python 2 zu unterscheiden). Gegebenenfalls kann auch hier pip3 install Django funktionieren, sofern es auf Python 3 verweist.
Hinweis: Der obige Befehl installiert stets die neueste stabile Django-Version. Möchte man eine bestimmte Version (etwa eine Long-Term-Support-Version) installieren, kann man dies explizit angeben, z. B. pip install Django==5.2.1 um Django 5.2.1 zu installieren
djangoproject.com
- Nach erfolgreicher Installation können Sie die Django-Version überprüfen. Geben Sie dazu im Terminal Folgendes ein:

```
python -m django --version
```

Dies sollte die installierte Django-Versionsnummer ausgeben (z. B. 4.2.1 oder 5.2.1)
tutorialspoint.com
- Falls dieser Befehl einen Fehler liefert, ist Django nicht korrekt installiert oder die PATH-Einstellungen sind falsch. In diesem Fall sollte die Installation bzw. der Aufruf von Python/Pip überprüft werden. 
### Erstes Django-Projekt erstellen
- Nach der Installation können Sie ein neues Django-Projekt anlegen. Django bringt hierfür das Tool django-admin mit, welches verschiedene Administrations-Befehle zur Verfügung stellt. Um ein neues Projekt (also eine Sammlung von Einstellungen und Grundkonfiguration für Ihre Website) zu erstellen, verwenden Sie den Befehl django-admin startproject <Projektname>. Beispiel: Erstellen eines Projekts namens mysite:

```
django-admin startproject mysite
```
- Dadurch wird ein neuer Ordner mysite in Ihrem aktuellen Verzeichnis angelegt. Dieser enthält zum einen die Datei manage.py und zum anderen ein Unterverzeichnis mysite mit den grundlegenden Projektdaten. In dieser Standard-Projektstruktur finden sich u. a.:
manage.py: Ein Skript, um das Projekt zu verwalten (Server starten, Datenbankmigrationen durchführen etc.). Sie können damit Befehle an Django senden, ähnlich wie mit django-admin, aber spezifisch für Ihr Projekt.
- Projekt-Unterordner (mysite/): Enthält den eigentlichen Projektcode als Python-Paket. Darin liegen z. B. die Einstellungsdatei (settings.py), die URL-Konfigurationsdatei (urls.py), sowie Konfigurationsdateien für den Application Server (wsgi.py für WSGI, und ab neueren Versionen auch asgi.py für ASGI-Anbindung). Außerdem ist eine leere __init__.py enthalten, die Python signalisiert, dass dieses Verzeichnis ein Paket ist.
- Diese automatisch generierten Dateien bilden das Grundgerüst Ihrer Webanwendung. Später werden Sie darin z.B. die Einstellungen anpassen oder neue Django-Apps hinzufügen. Mit dem Befehl python manage.py runserver können Sie anschließend einen Entwicklungswebserver starten, um das frische Projekt lokal zu testen – doch das ist Thema für eine spätere Übung. 
### Django vs. Flask vs. FastAPI
- Zum Abschluss ein kurzer Vergleich mit zwei anderen populären Python-Webframeworks:
### Flask: 
- Flask ist ein sog. Microframework. Im Gegensatz zu Django liefert Flask nur die minimalen Grundkomponenten (Routing, WSGI-Integration, Template-Engine) und lässt dem Entwickler viel Freiheit, weitere Bibliotheken bei Bedarf zu integrieren. Das führt zu mehr Flexibilität und weniger Overhead – man baut gewissermaßen nur das ein, was man tatsächlich braucht. Für kleine Apps oder einfache APIs kann Flask daher schlanker sein. Allerdings muss man in Flask viele Funktionen, die Django bereits mitbringt (z.B. Benutzerverwaltung, ORM), selbst nachrüsten oder implementieren. Django ist hingegen out-of-the-box einsatzbereit, was den Initialaufwand reduziert, aber dafür etwas unflexibler und „schwerer“ wirkt
blog.jetbrains.com
### FastAPI: 
- FastAPI ist ein modernes Framework, das vor allem für den Bau von Web-APIs entwickelt wurde. Es nutzt die asynchronen Features von Python (asyncio) und Typenhinweise, um sehr performante REST-APIs mit automatischer Dokumentation zu ermöglichen. Im Vergleich zu Django ist FastAPI in der Regel schneller in der Anfrageverarbeitung und sehr geeignet für Microservices oder reine JSON-API-Backends. Allerdings liefert FastAPI von Haus aus keine Komponenten wie ein Template-System oder ein Admin-Interface für Datenbanken – es ist fokussierter auf API-Endpunkte. Für klassische Webanwendungen mit Benutzeroberfläche müsste man bei FastAPI zusätzliche Tools verwenden, während Django solche Komponenten bereits integriert hat. In Summe gilt: Django für vollumfängliche Webanwendungen (besonders CMS, CRUD-Anwendungen, klassische Websites mit HTML), Flask für schnelle Prototypen oder kleinere Projekte, und FastAPI für hochperformante API-Services.
[ENDSECTION]

[SECTION::instructions::detailed]

- [EQ] Django-Grundprinzip und Architektur: Was ist Django, und welches Architekturmodell (Stichwort MTV) verwendet es? Beschreiben Sie die drei Komponenten Model, Template und View in Django und wie sie zusammenwirken. (Vergleichen Sie dabei auch kurz, wie sich dieses Modell vom klassischen MVC unterscheidet.)

- [ER] Django-Version prüfen: Wie können Sie ermitteln, welche Django-Version auf Ihrem System installiert ist? Nennen Sie den entsprechenden Befehl und geben Sie beispielhaft das Ergebnis/Format der Ausgabe an.

- [ER] Installation mit pip: Sie möchten Django installieren. Welchen Befehl verwenden Sie dazu in einer Kommandozeile unter Windows? Wie lautet der entsprechende Befehl unter Linux/macOS? (Erläutern Sie kurz, warum sich diese unterscheiden können.)

- [ER] Neues Projekt erstellen: Sie starten ein neues Django-Projekt namens “mysite”. Wie lautet der django-admin Befehl, um ein solches Projekt anzulegen? In welchem Verzeichnis wird das Projekt standardmäßig erstellt, wenn Sie keinen Zielpfad angeben?
- [EQ] Projektstruktur untersuchen: Welche Dateien und Ordner werden angelegt, wenn Sie django-admin startproject mysite ausführen? Nennen Sie mindestens zwei der wichtigsten generierten Dateien/Verzeichnisse und erläutern Sie deren Zweck.
- [EQ] MVC vs. MVT: Worin besteht der Unterschied zwischen dem MVC-Architekturmuster und Djangos MVT-Muster? (Hinweis: Betrachten Sie insbesondere die Rolle des “Controllers” bzw. dessen Entsprechung in Django.)
- [EQ] Typische Anwendungsfälle: Nennen Sie zwei typische Einsatzgebiete oder Anwendungsarten, für die Django oft genutzt wird. Begründen Sie kurz, warum Django sich dafür gut eignet.
- [EQ] Vergleich mit Flask/FastAPI: Nennen Sie einen Unterschied zwischen Django und einem Micro-Webframework wie Flask. Nennen Sie außerdem einen Unterschied zwischen Django und FastAPI. (Hinweis: Denken Sie an Aspekte wie Funktionsumfang, Performance oder Einsatzschwerpunkte.)
- [EQ] Reflexionsfrage: Warum eignet sich Django Ihrer Meinung nach besonders gut für die Umsetzung von Content-Management-Systemen (CMS) und allgemein CRUD-basierten Webanwendungen?

[SECTION::submission::information,program]
- Geben Sie hier Ihre Lösungen zu den obigen Aufgaben ein. Nutzen Sie das Information-Feld für erklärende Texte und Antworten in ganzen Sätzen. Falls Sie Code schreiben oder Befehle ausführen (z. B. um eine Version oder Struktur anzuzeigen), können Sie die relevanten Ausschnitte im Program-Bereich einfügen (z.B. Konsolenbefehle, Code-Snippets oder Dateilistings). Achten Sie auf eine klare Zuordnung Ihrer Antworten zu den jeweiligen Aufgaben. Speichern Sie bei Bedarf Ihre Python- oder Projekt-Dateien und laden Sie diese im Program-Feld hoch (falls in Ihrer Lernumgebung vorgesehen), damit die Prüfer Ihren Code einsehen können. 
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
### Lösung zu Aufgabe 1: 
Django ist ein in Python geschriebenes Webframework, das nach dem Model-Template-View-Prinzip arbeitet. Das Model bezeichnet die Datenschicht (Datenbankmodelle und ORM zur Abbildung der Datenbanktabellen). Die View in Django ist die Logikschicht – hier werden HTTP-Anfragen verarbeitet, Daten vom Model geholt und an Templates weitergegeben. Das Template schließlich ist für die Präsentation zuständig – es generiert aus den übergebenen Daten die HTML-Ausgabe für den Browser. Im Unterschied zum klassischen MVC-Muster übernimmt Django intern einen Großteil der Controller-Aufgabe (URL-Routing und Aufruf der View-Funktion). Die Komponente, die im MVC als “Controller” bezeichnet wird, entspricht in Django weitgehend der View-Funktion. Die MVC-View (Darstellung) entspricht in Django den Templates. 


### Lösung zu Aufgabe 2: 
Die installierte Django-Version kann man über ein Terminal/Kommandozeile herausfinden. Ein möglicher Befehl ist:
```
python -m django --version
```

Nach Ausführung erhält man die Versionsnummer als Ausgabe, z. B.:
4.2.1
Alternativ funktioniert auf vielen Systemen auch django-admin --version, was denselben Wert liefert. (Sollte Django nicht installiert sein, wird ein entsprechender Fehler angezeigt.) 

### Lösung zu Aufgabe 3: 
Unter Windows nutzt man oft den Python-Launcher py, um sicher das richtige Python aufzurufen. Der Installationsbefehl lautet dort zum Beispiel:
```
py -m pip install Django
```

Unter Linux oder macOS wird stattdessen meist python3 verwendet, also z. B.:
```
python3 -m pip install Django
```

Beide Befehle bewirken die Installation des Django-Pakets über pip. (Der Unterschied liegt daran, dass Windows mit dem py-Launcher arbeitet, während auf Unix-Systemen Python 3 explizit als python3 aufgerufen wird. Wichtig ist in allen Fällen, dass man Python 3 und pip installiert hat.) 

### Lösung zu Aufgabe 4: 
Der Befehl zum Anlegen eines neuen Django-Projekts namens mysite lautet:
```
django-admin startproject mysite
```

Dieser sollte in dem Verzeichnis ausgeführt werden, in dem der neue Projektordner erstellt werden soll. Ohne Angabe eines Zielpfads legt Django den Projektordner im aktuellen Arbeitsverzeichnis an. Nach Ausführen des Befehls gibt es einen neuen Ordner mysite (in dem Verzeichnis, in dem der Befehl ausgeführt wurde). 

### Lösung zu Aufgabe 5: 
Das neu erstellte Projekt mysite hat folgende Struktur: Im Wurzelverzeichnis befindet sich die Datei manage.py und der Unterordner mysite/ (gleichnamig mit dem Projekt). Die wichtigsten Inhalte sind:
manage.py: Ein Python-Skript, mit dem das Projekt verwaltet wird. Darüber können z. B. der Entwicklungsserver gestartet oder Datenbankmigrationen ausgeführt werden (python manage.py <Befehl>).
mysite/ (Projektordner): Dieser Ordner ist ein Python-Paket (er enthält u.a. eine leere __init__.py). Darin liegen zentrale Konfigurationsdateien: settings.py (Projekt-Einstellungen, z.B. Datenbank, installierte Apps), urls.py (URL-Routing der Projekt-URLs), wsgi.py (Konfiguration für WSGI-Server, zum Deployment) und asgi.py (für ASGI-Server, z.B. für Echtzeit/Async-Fähigkeit).
Diese Dateien werden von Django automatisch mit Standardinhalten gefüllt. Sie bilden das Grundgerüst der Anwendung, das man im Verlauf der Entwicklung weiter anpasst. (Hinweis: Zusätzlich erstellt man im Django-Projekt meist eine oder mehrere Apps, die weitere Dateien wie views.py, models.py etc. mitbringen – diese fehlen in der Grundstruktur direkt nach startproject, da noch keine App angelegt wurde.) 

### Lösung zu Aufgabe 6: 
Der Hauptunterschied zwischen MVC und MVT in Django liegt in der Benennung und Aufgabenteilung der Komponenten. Im MVC-Muster gibt es einen Controller, der die Eingaben verarbeitet und die passenden View/Template auswählt. Bei Django (MVT) übernimmt die View-Funktion die Rolle des Controllers – sie enthält die Logik, um eine Anfrage zu verarbeiten, auf das Model zuzugreifen und Daten aufzubereiten. Die Darstellung wird in Django vollständig vom Template übernommen (das entspricht also der View im MVC). Anders gesagt: In Django ist die „View“ nicht die Ausgabe, sondern die Logikschicht. Der Teil des Controllers, der Anfragen verteilt, wird vom Framework (über die URL-Konfiguration) automatisch erledigt. Somit müssen Entwickler sich nur um Models, Views (Logik) und Templates kümmern. Das Endergebnis ist aber vergleichbar: Beide Architekturen trennen Daten, Logik und Präsentation, Django nennt sie nur anders und automatisiert den Controller-Teil stärker. 

### Lösung zu Aufgabe 7: 
Django wird oft für datengetriebene Webanwendungen eingesetzt, insbesondere wenn ein schneller Aufbau mit Standardfunktionen gefragt ist. Zwei typische Beispiele:
Content-Management-Systeme (CMS) und Blogs: Aufgrund des eingebauten Admin-Bereichs und des ORM ist Django ideal, um Webseiten zu erstellen, bei denen Inhalte regelmäßig erstellt, bearbeitet und angezeigt werden müssen (CRUD: Create, Read, Update, Delete). Redakteure können über das Admin-Interface Inhalte verwalten, ohne dass zusätzliche Programmierung notwendig ist.
E-Commerce und komplexe Webseiten: Django eignet sich auch für Online-Shops oder Marktplätze, da es von Benutzerkonten über Bestellprozesse bis zur Bezahlung vieles mit vorhandenen Bibliotheken abdecken kann. Durch seine Skalierbarkeit und Sicherheit wird es in Enterprise-Websites, Nachrichtenportalen oder Social-Media-Plattformen verwendet, wo schnelles Entwickeln und Zuverlässigkeit wichtig sind.
Allgemein glänzt Django überall dort, wo schnell eine voll funktionsfähige Webanwendung mit Datenbank-Anbindung benötigt wird und man von den vielen mitgelieferten Features profitieren kann. 

### Lösung zu Aufgabe 8: 
Django vs Flask: Django ist ein Voll-Stack-Framework mit vielen eingebauten Features, während Flask ein minimalistisches Framework ist. Ein Unterschied besteht z.B. im Umfang: Django hat eine fest vorgegebene Projektstruktur und bringt Module für Authentifizierung, Datenbank, Templates etc. mit. Flask hingegen gibt dem Entwickler mehr Freiheit – man startet mit einer leeren Anwendung und fügt nur die Komponenten hinzu, die man braucht. Dadurch ist Flask für kleine Anwendungen leichtergewichtig (weniger Abhängigkeiten), während Django für größere Projekte vieles schon vorbereitet hat. Ein konkreter Unterschied: In Django existiert ein Admin-Interface von Haus aus, Flask hat so etwas nicht integriert (man müsste ein Plugin nutzen oder selbst programmieren). Django vs FastAPI: FastAPI ist spezialisiert auf den Bau von Web-APIs und nutzt moderne Python-Funktionen (async/await, Pydantic-Datenmodelle für Validierung). Ein Unterschied liegt in der Performance und dem Einsatzzweck: FastAPI ist in der Regel schneller bei API-Anfragen und eignet sich besonders für Microservices oder Backend-Services, die JSON-Daten liefern. Django hingegen ist etwas langsamer (durch seinen größeren Overhead), wurde aber für komplette Webanwendungen mit HTML-Rendering entwickelt. Außerdem ist Django hauptsächlich synchron (obwohl neuere Versionen auch Async unterstützen), während FastAPI von Grund auf für asynchrone Requests konzipiert ist. FastAPI hat keinen eigenen ORM oder Templates an Bord – man würde für eine vollwertige Webanwendung zusätzliche Bibliotheken benötigen. Django bietet dagegen ein Rundum-Paket (inkl. ORM, Templates, Admin), was die Entwicklung von klassischen Webapps erleichtert. 

### Lösung zu Aufgabe 9 (Reflexion): 
Django eignet sich besonders gut für CMS (Content-Management-Systeme) und CRUD-Anwendungen, weil es viele benötigte Funktionen bereits integriert hat und so „von Haus aus“ bereitstellt. Im Zentrum steht das Admin-Interface, welches Django mitbringt: Damit kann man ohne eine Zeile Code alle Datenmodelle über eine Weboberfläche bearbeiten. Für ein typisches CMS – wo Inhalte erstellt, geändert und gelöscht werden – ist dieses Feature enorm wertvoll, da Entwickler nicht jedes Frontend für Datenpflege selbst schreiben müssen. Dazu kommt Djangos ORM, mit dem sich Datenbankoperationen sehr einfach durchführen lassen, und die automatische Erstellung von Formularen und Validierungen. Kurz gesagt: Django liefert die gesamte Grundausstattung für CRUD direkt mit. Dadurch lassen sich CMS-artige Anwendungen äußerst schnell entwickeln. Sicherheit und Rechteverwaltung (wer darf Inhalte ändern, veröffentlichen etc.) sind ebenfalls schon in Django vorhanden, was genau den Anforderungen von CMS entspricht. Weil Django zudem auf Rapid Development ausgelegt ist, können CRUD-basierte Anwendungen in kurzer Zeit prototypisch umgesetzt und dann erweitert werden. Diese Kombination aus Schnelligkeit, eingebauten Tools (Admin, Auth, ORM) und Community-Unterstützung macht Django zur ersten Wahl für viele CMS und ähnliche datengetriebene Webanwendungen.

[ENDINSTRUCTOR]
