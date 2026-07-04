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

[EC] Installieren Sie Django in Ihrem venv:

```bash
pip install Django
```
<!-- EC1 -->

[EC] Überprüfen Sie die Installation:

```bash
python -m django --version
```
<!-- EC2 -->
<!-- time estimate: 10 min -->

### Erstes Projekt erstellen

Sie werden Ihr erstes Django-Projekt mit `startproject` erstellen. 
Dieses Projekt namens `meinprojekt` werden Sie in allen darauffolgenden Django-Aufgaben verwenden und 
schrittweise erweitern. Erstellen Sie das Projekt im Verzeichnis `Web/Django`:

```bash
cd Web/Django  # Pfad anpassen
django-admin startproject meinprojekt
ls meinprojekt/meinprojekt
```

Wie Sie sehen, hat Django in Ihrem Verzeichnis `meinprojekt` (dem Projektverzeichnis)
ein Unterverzeichnis gleichen Namens `meinprojekt` angelegt.
Das ist ein Verzeichnis für eine "app", wie bei Django die einzelnen Bereiche größerer Projekte
genannt werden, die eine gewisse Entkopplung herstellen sollen.

Django bringt einen Entwicklungsserver mit, mit dem man probeweise seine Webanwendung
starten und ausprobieren kann. Außerdem gibt es eine Standard-Startseite, die jetzt schon existiert.
Wir starten also den Server:

[EC] `python manage.py runserver 8071`
<!-- EC3 -->

Die Nummer ist der verwendete Netzwerkport. 
Sollte der Port belegt sein (dann endet der Server mit einer entsprechenden Fehlermeldung), 
wählen Sie irgendeine andere Nummer im Bereich 8000 bis 8099.

Beachten Sie die Warnmeldung über "unapplied migrations", die Django (in rot) beim Starten ausgibt.
Sie liegt daran, dass Django ab Werk eine ganze Reihe von Funktionen mitbringt, die eine
Datenbank erfordern (z.B. für Benutzerkonten), wir aber noch kein Datenbankschema angelegt haben.

Das sollten wir also nachholen. Beenden Sie dafür den Server mit Ctrl-C und machen Sie dann:

[EC] `python manage.py migrate`
<!-- EC4 -->

Nun ist das Schema angelegt.
Mit diesem Aspekt befassen wir uns genauer in [PARTREF::django-model].

[EC] Starten Sie nun erneut den Server mit `python manage.py runserver 8071`
(die Warnmeldung bleibt nun aus)
und öffnen Sie die Homepage `http://127.0.0.1:8071/` oder welchen Port auch immer Sie benutzen.
<!-- EC5 -->

[EQ] Welche Überschrift wird auf der Homepage angezeigt?
<!-- EQ1 -->

Beenden Sie den Server mit Ctrl-C.
Das war alles: Sie haben ein Django-Projekt begonnen!

### Weiterführend

- [Django: Quick install guide](https://docs.djangoproject.com/en/stable/intro/install/) – offizielle Installationsanleitung
- [Das offizielle Django-Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) – schrittweiser Einstieg in Django

In der nächsten Aufgabe erkunden wir die Projektstruktur und schreiben unsere erste eigene
Django-basierte Webseite ("View").

<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
**Knackpunkte:**

- [EREFC::1]: Django wurde innerhalb eines venv installiert, nicht systemweit.
- [EREFC::3]/[EREFC::4]/[EREFC::5]: Migrationswarnung beim ersten Start vorhanden; nach `migrate` beim zweiten Start keine Warnung mehr.
- [EREFQ::1]: Überschrift „The install worked successfully! Congratulations!" korrekt angegeben.

### Kommandoprotokoll
[PROT::ALT:django-basics.prot]

### Fragen
[INCLUDE::ALT:django-basics.md]

[ENDINSTRUCTOR]