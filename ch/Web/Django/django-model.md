title: Django Modelle und Migrationen
stage: draft
timevalue: 2
difficulty: 2
requires: django-project
assumes: sql-basics, sql-SELECT, sql-UPDATE-VIEW-CASE
---

[SECTION::goal::idea,experience]

- Ich verstehe, wie ein Django-Model die Struktur einer Datenbanktabelle abbildet und wie
  Migrations Änderungen daran nachvollziehbar machen.
- Ich kann ein eigenes Model definieren und über die Admin-Oberfläche sowie die Shell verwalten.
- Ich kann grundlegende Datenoperationen (Anlegen, Lesen, Ändern, Löschen) auf einzelnen
  Objekten ausführen.

[ENDSECTION]

[SECTION::background::default]

Datenbanktabellen von Hand per SQL zu pflegen ist fehleranfällig und bindet den Code eng an
ein bestimmtes Datenbanksystem. Django bietet dafür ein Object-Relational Mapping (ORM): Eine
Python-Klasse beschreibt die Tabellenstruktur, und Django übersetzt Lese- und Schreibzugriffe
automatisch in SQL. Wie jede Abstraktion hat das seinen Preis, macht aber den alltäglichen
Umgang mit Daten deutlich einfacher.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit dem `meinprojekt`-Projekt und der App `webapp`, die Sie in
[PARTREF::django-project] angelegt haben. Alle folgenden Änderungen finden in `webapp` statt.

### Was ist ein Django-Model?

Ein **Model** ist eine Python-Klasse, die eine Datenbanktabelle beschreibt:

- Die Klasse entspricht der Tabelle.
- Jedes Klassenattribut entspricht einer Spalte.
- Jede Instanz der Klasse entspricht einer Zeile.

Django erzeugt aus dieser Klassendefinition automatisch die passenden SQL-Befehle (vgl.
[PARTREF::sql-basics] für die Tabellenkonzepte selbst).

[EQ] Erklären Sie in eigenen Worten, wie eine Model-Klasse mit einer Datenbanktabelle
zusammenhängt, und nennen Sie ein Beispiel, wie sich eine Änderung am Model (z. B. ein
neues Attribut) auf die Tabelle auswirkt.
<!-- EQ1 -->
<!-- time estimate: 10 min -->

### Ein Model definieren

Model-Klassen werden in der Datei `models.py` der jeweiligen App definiert:

[ER] Öffnen Sie `models.py` in `webapp` und definieren Sie folgendes Model:

[SNIPPET::ALT::django_model_student_basic]
<!-- ER1 -->

**Feldtypen** legen fest, welche Art von Daten eine Spalte speichert:

- `CharField(max_length=n)`: Text mit fester maximaler Länge (`max_length` ist erforderlich).
- `IntegerField()`: Ganzzahlen.
- `EmailField()`: Text mit zusätzlicher Formatvalidierung für E-Mail-Adressen.

**Feldoptionen** `null` und `blank` werden häufig verwechselt, regeln aber unterschiedliche
Ebenen: `null=True` erlaubt den Datenbankwert `NULL` (Datenbankebene), während `blank=True`
ein Feld in Formularen/Validierung als optional markiert (Eingabeebene). Ein Feld kann auch
beides gleichzeitig sein — Standard für beide ist `False`.

[HINT::Wann brauche ich null, wann blank?]
Ein Beispiel macht den Unterschied greifbar: Ein optionales Kommentarfeld vom Typ
`CharField` sollte `blank=True` bekommen (im Formular darf es leer bleiben), aber **nicht**
zwingend `null=True` — Django speichert bei `CharField` einen leeren String `""` statt
`NULL`, wenn nichts eingegeben wurde. `null=True` ist eher für Felder wie `DateField` oder
`IntegerField` relevant, bei denen es keinen sinnvollen "leeren" Wert gibt und daher
`NULL` in der Datenbank stehen muss.
[ENDHINT]
<!-- time estimate: 10 min -->

### Migrationen erstellen und anwenden

**Migrations** übersetzen Änderungen an Model-Klassen in Datenbankbefehle (vergleichbar mit
SQL `CREATE TABLE`/`ALTER TABLE`, siehe [PARTREF::sql-basics]) und machen sie nachvollziehbar.

[EC] Erstellen Sie eine Migration für das neue Model:

```bash
python manage.py makemigrations webapp
```
<!-- EC1 -->

[EC] Wenden Sie die Migration an:

```bash
python manage.py migrate
```
<!-- EC2 -->

[EC] Betrachten Sie die erzeugte Migrationsdatei:

```bash
cat webapp/migrations/0001_initial.py
```
<!-- EC3 -->

[NOTICE]
Django legt automatisch eine `id`-Spalte als Primärschlüssel an, auch wenn Sie keine
eigene definieren.
[ENDNOTICE]

[EQ] Welche Datei hat `makemigrations` erzeugt, und was genau enthält sie?
<!-- EQ2 -->
<!-- time estimate: 8 min -->

### Die `__str__()`-Methode

[ER] Öffnen Sie die Shell und legen Sie einen ersten Datensatz an:

```bash
python manage.py shell
```

```python
from webapp.models import Student
Student.objects.create(name="Anna Müller", age=22, email="anna@example.com")
print(Student.objects.all())
```
<!-- ER2 -->

Die Ausgabe zeigt vermutlich `<QuerySet [<Student: Student object (1)>]>` — nicht besonders
aussagekräftig. Der Grund: Ohne eigene Angabe stellt Django ein Objekt standardmäßig als
`Klassenname object (id)` dar. Die Methode `__str__()` legt fest, wie ein Objekt als
Text dargestellt wird — genau das lässt sich hier festlegen.

[ER] Ergänzen Sie das Model um `__str__()`:

[SNIPPET::ALT::django_model_student_str]
<!-- ER3 -->

[EQ] Verlassen Sie die Shell (`exit()`), starten Sie sie neu und rufen Sie erneut
`Student.objects.all()` auf. Was hat sich an der Ausgabe geändert, und warum war dafür
keine neue Migration nötig (anders als bei einem neuen Feld)?
<!-- EQ3 -->
<!-- time estimate: 10 min -->

### Daten anlegen (CREATE)

Ein Objekt lässt sich auf zwei Arten anlegen:

```python
# Variante 1: Objekt erzeugen, dann speichern
student = Student(name="Max Schmidt", age=24, email="max@example.com")
student.save()

# Variante 2: Erzeugen und speichern in einem Schritt
Student.objects.create(name="Lisa Weber", age=21, email="lisa@example.com")
```

[ER] Legen Sie in der Shell beide zusätzlichen Studierenden mit jeweils einer der beiden
Varianten an und lassen Sie sich danach `Student.objects.all()` ausgeben.
<!-- ER4 -->

[EQ] Beide Varianten führen zum selben Ergebnis in der Datenbank. Gibt es dennoch eine
Situation, in der Sie zwingend `Student(...)` + `save()` statt `objects.create()`
verwenden müssten (Tipp: Was passiert zwischen dem Erzeugen des Objekts und dem
Speichern)?
<!-- EQ4 -->
<!-- time estimate: 12 min -->

### Daten lesen (READ)

Lesezugriffe mit Django entsprechen SQL `SELECT`-Abfragen (vgl. [PARTREF::sql-SELECT]):

```python
Student.objects.all()                    # alle Objekte
Student.objects.get(id=1)                # genau ein Objekt anhand der ID
Student.objects.filter(name="Anna Müller")  # Objekte mit exaktem Feldwert
```

[ER] Rufen Sie in der Shell alle drei Varianten mit Ihren eigenen Daten auf.
<!-- ER5 -->

[EQ] `get()` und `filter()` liefern beide Objekte anhand eines Kriteriums zurück, aber
mit unterschiedlichem Rückgabetyp. Was passiert bei `get()`, wenn kein oder mehr als ein
Objekt zum Kriterium passt — und warum ist das bei `filter()` unproblematisch?
<!-- EQ5 -->
<!-- time estimate: 10 min -->

### Daten ändern (UPDATE)

Ändern mit Django entspricht SQL `UPDATE` (vgl. [PARTREF::sql-UPDATE-VIEW-CASE]): Ein
Objekt wird geladen, ein Attribut verändert, dann gespeichert.

[ER] Laden Sie einen Ihrer Studierenden per `get()`, ändern Sie das Attribut `age` und
speichern Sie die Änderung mit `save()`. Bestätigen Sie die Änderung mit einem erneuten
`get()`.
<!-- ER6 -->

[EQ] Was würde passieren, wenn Sie `save()` nach der Änderung vergessen? Woran würden Sie
das bemerken?
<!-- EQ6 -->
<!-- time estimate: 7 min -->

### Daten löschen (DELETE)

[ER] Laden Sie einen Ihrer Studierenden per `get()` und löschen Sie ihn mit `delete()`.
Bestätigen Sie mit `Student.objects.all()`, dass er verschwunden ist.
<!-- ER7 -->

[WARNING]
`delete()` entfernt den Datensatz sofort und endgültig, ohne Rückfrage.
[ENDWARNING]

[EQ] `Student.objects.get(id=2).delete()` und `Student.objects.get(id=2)` (ohne
`delete()`) unterscheiden sich nur durch den Methodenaufruf, führen aber zu ganz
unterschiedlichen Risiken. Welches Risiko besteht bei `delete()`, das bei einem reinen
Lesezugriff nicht besteht?
<!-- EQ7 -->
<!-- time estimate: 7 min -->

### Weitere Feldtypen

[ER] Erweitern Sie das `Student`-Model um zwei weitere Felder:

[SNIPPET::ALT::django_model_student_extended]
<!-- ER8 -->

- `BooleanField(default=True)`: Wahrheitswert, hier mit Standardwert `True`.
- `DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)`: Dezimalzahl mit
  fester Genauigkeit (hier: bis zu 3 Ziffern gesamt, davon 2 Nachkommastellen) — als
  `null=True, blank=True` definiert, weil nicht jeder Studierende bereits einen
  Notendurchschnitt hat.

[EC] Erstellen und wenden Sie die Migration für die neuen Felder an:

```bash
python manage.py makemigrations webapp
python manage.py migrate
```
<!-- EC4 -->
<!-- time estimate: 15 min -->

### Model in der Admin-Oberfläche verwalten

Django bringt eine fertige Verwaltungsoberfläche mit, in der registrierte Models über den
Browser statt über die Shell bearbeitet werden können.

[ER] Registrieren Sie `Student` in `admin.py`:

[SNIPPET::ALT::django_model_admin_register]
<!-- ER9 -->

Damit Sie sich an der Admin-Oberfläche anmelden können, benötigen Sie ein
Administrator-Konto (**Superuser**) — ein Benutzer mit vollem Zugriff auf alle
registrierten Models.

[EC] Legen Sie einen Superuser an (folgen Sie den interaktiven Eingabeaufforderungen für
Benutzername, E-Mail und Passwort):

```bash
python manage.py createsuperuser
```
<!-- EC5 -->

[ER] Starten Sie den Entwicklungsserver, öffnen Sie `http://127.0.0.1:8071/admin/`, melden
Sie sich mit Ihrem Superuser an und öffnen Sie die Übersicht Ihrer `Student`-Objekte.
<!-- ER10 -->

[EQ] Welche Studierenden werden in der Übersicht angezeigt, und woran erkennen Sie, dass
hier dieselbe `__str__()`-Darstellung verwendet wird wie zuvor in der Shell?
<!-- EQ8 -->
<!-- time estimate: 15 min -->

### Weitere Kommandos zur Datenverwaltung (Überblick)

Die folgenden Befehle werden hier nur kurz vorgestellt, ohne dass Sie sie selbst ausführen
müssen:

- `python manage.py dbshell`: öffnet eine direkte SQL-Konsole zur Datenbank — die einzige
  Möglichkeit, komplett am ORM vorbei mit der Datenbank zu arbeiten.
- `python manage.py dumpdata webapp`: exportiert die aktuellen Daten einer App als JSON.
- `python manage.py loaddata <datei>`: importiert zuvor exportierte Daten wieder.
- `python manage.py flush`: löscht alle Daten aus allen Tabellen (Tabellenstruktur bleibt
  erhalten).
<!-- time estimate: 5 min -->

### Admin-Oberfläche und ORM

[EQ] Sie haben soeben über die Shell einen Studierenden mit `.objects.create(...)`
angelegt und einen weiteren über die Admin-Oberfläche im Browser. Beide landen in
derselben Datenbanktabelle. Läuft der Weg über die Admin-Oberfläche ebenso über das ORM
wie der Weg über die Shell, oder wird das ORM dabei umgangen? Begründen Sie anhand dessen,
was ORM eigentlich bedeutet.
<!-- EQ9 -->
<!-- time estimate: 11 min -->

### Weiterführend

- [Models](https://docs.djangoproject.com/en/stable/topics/db/models/) – Umfassende
  Dokumentation zu Django-Modellen
- [Model field reference](https://docs.djangoproject.com/en/stable/ref/models/fields/) –
  Referenz zu allen verfügbaren Feldtypen und -optionen

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::3] + [EREFQ::3]: Nach Ergänzen von `__str__()` zeigt die Shell den Namen statt
  `Student object (1)`; Student erkennt, dass dafür keine Migration nötig war, weil
  `__str__()` kein Datenbankfeld ist, sondern nur die Python-seitige Darstellung betrifft.
- [EREFQ::9]: Student erkennt, dass sowohl der Shell-Weg als auch die Admin-Oberfläche
  über dasselbe ORM laufen (jeder Schreibzugriff auf ein Model geht durch die
  ORM-Übersetzungsschicht) — die Admin-Oberfläche vermeidet nur, dass man selbst
  ORM-Syntax tippt, nicht dass ORM stattfindet.
- [EREFQ::5]: Student erkennt, dass `get()` bei keinem oder mehreren Treffern einen Fehler
  auslöst (eindeutiges Einzelobjekt erwartet), während `filter()` immer ein (ggf. leeres)
  QuerySet zurückgibt.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-model.md]

### Kommandoprotokoll
[PROT::ALT:django-model.prot]

[ENDINSTRUCTOR]
