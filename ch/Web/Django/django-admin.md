title: Django django-admin Kommandozeilen-Tool
stage: draft
timevalue: 1.25
difficulty: 2
requires: django-project
---

[SECTION::goal::idea,experience]
Ich kann das `django-admin` Kommandozeilen-Tool verwenden, um Django-Projekte zu erstellen, 
zu verwalten und grundlegende Verwaltungsaufgaben durchzuführen.
[ENDSECTION]

[SECTION::background::default]
Django-Projekte bestehen aus vielen Dateien und haben eine komplexe Struktur.
Das manuelle Erstellen aller benötigten Dateien und Konfigurationen wäre zeitaufwendig 
und fehleranfällig.
Das `django-admin` Tool automatisiert diese Aufgaben und stellt eine einheitliche 
Schnittstelle für alle wichtigen Projektverwaltungsaufgaben bereit.
[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in [PARTREF::django-basics] erstellt haben.
Alle folgenden Änderungen werden Sie in diesem Projekt durchführen.

### Verfügbare Kommandos anzeigen: `help`

Das `django-admin` Tool bietet viele verschiedene Kommandos für unterschiedliche Aufgaben.
Um eine Übersicht aller verfügbaren Kommandos zu erhalten, verwenden Sie:

```bash
django-admin help
```

Für detaillierte Hilfe zu einem spezifischen Kommando:

```bash
django-admin help <kommando>
```

Die Ausgabe zeigt Ihnen alle verfügbaren Unterkommandos an:

```
Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    shell
    showmigrations
    startapp
    startproject
    test
    ...
```

### Django-Anwendung erstellen: `startapp`

Django-Projekte bestehen aus einer oder mehreren Anwendungen (Apps).
Jede App behandelt einen spezifischen Funktionsbereich.

```bash
django-admin startapp appname
```

oder innerhalb eines Projekts (empfohlen):

```bash
python manage.py startapp appname
```

Eine App-Struktur sieht folgendermaßen aus:

```
appname/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Die wichtigsten Dateien sind:

- `models.py`: Datenbankmodelle definieren
- `views.py`: Ansichts-Funktionen oder -Klassen
- `admin.py`: Konfiguration für das Admin-Interface
- `migrations/`: Datenbankmigrationen

[EC] Wechseln Sie in Ihr `meinprojekt` Projektverzeichnis und erstellen Sie eine App 
namens `produkte` mit `python manage.py startapp produkte`.
<!-- EC1 -->

<!-- time estimate: 5 min -->

### Projektkonfiguration überprüfen: `check`

Das `check` Kommando überprüft Ihr Django-Projekt auf häufige Probleme:

```bash
python manage.py check
```

Es prüft unter anderem:

- Modell-Definitionen
- URL-Konfigurationen  
- Template-Einstellungen
- Sicherheitseinstellungen

Für spezifische Checks können Sie Tags verwenden, z.B. `--tag=security` für nur die
Sicherheits-Checks.

[EC] Führen Sie `python manage.py check` in Ihrem Projekt aus und 
dokumentieren Sie das Ergebnis.

<!-- EC2 -->

[EC] Führen Sie einen Security-Check mit `python manage.py check --tag=security` durch.

<!-- EC3 -->

<!-- time estimate: 15 min -->

### Datenbankmigrationen: `makemigrations` und `migrate`

Django verwendet ein Migrationssystem zur Verwaltung von Datenbankschema-Änderungen.
`makemigrations` erstellt Migrationsdateien aus Änderungen an Ihren Modellen,
`migrate` wendet diese Migrationen auf die Datenbank an. Beide Kommandos können
auch auf eine einzelne App beschränkt werden, z.B. `python manage.py makemigrations produkte`.

[EC] Führen Sie `python manage.py makemigrations produkte` für die in [EREFC::1] erstellte
App aus. Da `produkte` noch keine Modelle enthält, erhalten Sie "No changes detected" –
das ist hier das erwartete Ergebnis. Modelle für `produkte` erstellen wir in [PARTREF::django-model].
<!-- EC4 -->

[EC] Führen Sie `python manage.py migrate` für Ihr gesamtes Projekt aus.
<!-- EC5 -->

[EC] Überprüfen Sie den Status der Migrationen mit 
`python manage.py showmigrations`.
<!-- EC6 -->

[EQ] In der Ausgabe von [EREFC::6] sind manche Migrationen mit `[X]` markiert, andere ggf. mit `[ ]`.
Was bedeutet der Unterschied, und warum sollte nach [EREFC::5] keine Migration mehr mit `[ ]` markiert sein?
<!-- EQ1 -->

<!-- time estimate: 10 min -->

### Superuser erstellen: `createsuperuser`

Für den Zugang zum Django-Admin-Interface benötigen Sie einen Superuser:

```bash
python manage.py createsuperuser
```

Das Kommando fragt interaktiv nach:

- Benutzername
- E-Mail-Adresse  
- Passwort (wird zweimal zur Bestätigung eingegeben)

[NOTICE]
Für den Login im Admin-Interface muss der Entwicklungsserver laufen.
Falls Sie ihn seit [PARTREF::django-project] beendet haben,
starten Sie ihn in einem separaten Terminal neu mit `python manage.py runserver 8071`
(oder dem von Ihnen verwendeten Port).
[ENDNOTICE]

[EC] Erstellen Sie einen Superuser für Ihr Projekt und loggen Sie sich 
unter `http://127.0.0.1:8071/admin/` (oder Ihrem Port) in das Admin-Interface ein.
<!-- EC7 -->

[EQ] Beschreiben Sie, was Sie nach dem Login unter `/admin/` im Browser sehen.
Welche Modelle werden dort bereits ohne eigenes Zutun zur Verwaltung angeboten?
<!-- EQ2 -->

<!-- time estimate: 10 min -->

### Django Shell: `shell`

Die Django Shell bietet eine interaktive Python-Umgebung mit Zugriff auf Ihr Projekt:

```bash
python manage.py shell
```

In der Shell können Sie Modelle importieren, Datenbankabfragen durchführen und
Django-Einstellungen inspizieren.

[EC] Öffnen Sie die Django Shell und führen Sie folgende Befehle aus:
<!-- EC8 -->

```python
from django.conf import settings
print(settings.DEBUG)
print(settings.DATABASES)
```

[EQ] Was geben `settings.DATABASES['default']['ENGINE']` und `settings.DATABASES['default']['NAME']`
jeweils aus, und was sagen diese beiden Werte über Ihre aktuelle Datenbank aus?
<!-- EQ3 -->

<!-- time estimate: 10 min -->

### Tests ausführen: `test`

Django bietet ein integriertes Test-Framework, das mit `python manage.py test` alle
Tests des Projekts ausführt.

[EC] Führen Sie `python manage.py test` aus und dokumentieren Sie das Ergebnis.
<!-- EC9 -->

### Statische Dateien sammeln: `collectstatic`

Für die Produktionsumgebung müssen statische Dateien gesammelt werden:

```bash
python manage.py collectstatic
```

[NOTICE]
Dieses Kommando funktioniert nur, wenn in Ihrer settings.py die Einstellung STATIC_ROOT gesetzt ist,
z. B. `STATIC_ROOT = BASE_DIR / "staticfiles"`. Wir konfigurieren das hier nicht weiter;
es genügt, `collectstatic` als Übersichtswissen zu kennen. Details finden Sie bei Bedarf
in der [Django-Dokumentation zu statischen Dateien](https://docs.djangoproject.com/en/stable/howto/static-files/).
[ENDNOTICE]

<!-- time estimate: 5 min -->

### Weitere Kommandos zur Kenntnisnahme (Übersicht)

Die folgenden Kommandos werden hier nicht praktisch geübt, sollten Ihnen aber vom Namen
her bekannt sein, falls Sie sie in der Dokumentation oder in fremdem Code antreffen:

- `dbshell`: direkter Zugang zur Datenbank-Shell
- `dumpdata`/`loaddata`: Daten als JSON exportieren bzw. importieren

### Datenbank zurücksetzen: `flush`

```bash
python manage.py flush                           # Alle Daten löschen
```

[EC] Testen Sie `python manage.py flush`, um das Zurücksetzen der Datenbank zu überprüfen.
<!-- EC10 -->

[EQ] Worin unterscheidet sich `flush` von `migrate`? Eines der beiden Kommandos verändert
das Datenbankschema, das andere den Dateninhalt – welches macht was?
<!-- EQ4 -->

<!-- time estimate: 5 min -->

### Weiterführend

- [Django Management Commands Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/) – Übersicht aller verfügbaren Kommandos
- [App-Dokumentation](https://docs.djangoproject.com/en/stable/ref/applications/) – Details zu Django-Apps
- [System Check Dokumentation](https://docs.djangoproject.com/en/stable/topics/checks/) – Weitere Informationen zu System-Checks
- [Migrations-Dokumentation](https://docs.djangoproject.com/en/stable/topics/migrations/) – Detaillierte Dokumentation zu Migrationen
- [Shell Dokumentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#shell) – Weitere Informationen zur Django Shell

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
**Knackpunkte:**

- [EREFC::5]/[EREFC::6]: `migrate` wendet die bereits aus [PARTREF::django-basics] bekannten Migrationen an (keine erneute Ausführung nötig); `showmigrations` zeigt sie als `[X]` angewendet.
- [EREFC::7]/[EREFQ::2]: Superuser erfolgreich erstellt; Student beschreibt das Admin-Interface unter `/admin/` korrekt (Login-Formular, danach Übersicht über `Users` und `Groups`).
- [EREFQ::3]: Student erklärt `ENGINE` (verwendetes Datenbank-Backend, hier sqlite3) und `NAME` (Pfad zur Datenbankdatei) korrekt.

### Kommandoprotokoll
[PROT::ALT:django-admin.prot]

### Fragen
[INCLUDE::ALT:django-admin.md]

[ENDINSTRUCTOR]