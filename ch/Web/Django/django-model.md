title: Django Modelle und Migrationen
stage: alpha
timevalue: 2
difficulty: 2
requires: django-project
assumes: sql-basics, sql-SELECT, sql-UPDATE-VIEW-CASE
---

[SECTION::goal::idea,experience]

- Ich verstehe, wie ein Django-Model die Struktur einer Datenbanktabelle abbildet und wie
  Migrationen Änderungen daran nachvollziehbar machen.
- Ich kann ein eigenes Model definieren und über die Admin-Oberfläche sowie die Shell verwalten.
- Ich kann grundlegende Datenoperationen (Anlegen, Lesen, Ändern, Löschen) auf einzelnen
  Objekten ausführen.
[ENDSECTION]


[SECTION::background::default]
Datenbanktabellen von Hand per SQL zu pflegen ist umständlich, fehleranfällig und bindet den Code eng an
ein bestimmtes Datenbanksystem. Django bietet dafür ein Object-Relational Mapping (ORM): Eine
Python-Klasse beschreibt die Tabellenstruktur, und Django übersetzt Lese- und Schreibzugriffe
automatisch in SQL. 
Das ist nicht ganz so flexibel wie die manuelle Verwaltung mit SQL, spart aber große Mengen
Code ein und macht die Anwendung weitaus übersichtlicher und tendenziell sicherer.
[ENDSECTION]


[SECTION::instructions::detailed]
Wir arbeiten weiter mit dem `meinprojekt`-Projekt und der App `webapp`, die Sie in
[PARTREF::django-project] angelegt haben. Alle folgenden Änderungen finden in `webapp` statt.

### Was ist ein Django-Model?

Ein **Model** ist eine Python-Klasse, die eine Datenbanktabelle beschreibt:

- Die Klasse entspricht der Tabelle.
- Jedes Klassenattribut entspricht einer Spalte.
- Jede Instanz der Klasse entspricht einer Zeile.
- Jedes Attribut einer Instanz der Klasse entspricht einer Zelle.

Django erzeugt aus dieser Klassendefinition automatisch die passenden SQL-Befehle (vgl.
[PARTREF::sql-basics] für die Tabellenkonzepte selbst).

Model-Klassen werden per Konvention in der Datei `models.py` der jeweiligen App definiert.

**Feldtypen** legen fest, welche Art von Daten eine Spalte speichert:

- `CharField(max_length=n)`: Text mit fester maximaler Länge (`max_length` ist erforderlich).
- `IntegerField()`: Ganzzahlen.
- `EmailField()`: Text, aber mit zusätzlicher Formatvalidierung für E-Mail-Adressen, wenn das
  Feld in einem Formular verwendet wird (siehe Aufgabe [PARTREF::django-form]).
- Es gibt 
  [zahlreiche weitere](https://docs.djangoproject.com/en/stable/ref/models/fields/), 
  etwa für Datumsfelder oder URLs.

[ER] Öffnen Sie `models.py` in `webapp` und definieren Sie folgendes Model:

[SNIPPET::ALT::django_model_student_basic]

### Migrationen erstellen und anwenden

**Migrationen** übersetzen Änderungen an Model-Klassen in Datenbankbefehle (vergleichbar mit
SQL `CREATE TABLE`/`ALTER TABLE`, siehe [PARTREF::sql-basics]) und machen sie nachvollziehbar.

[EC] Erstellen Sie eine Migration für das neue Model:

```bash
python manage.py makemigrations webapp
```

[EC] Wenden Sie die Migration an:

```bash
python manage.py migrate
```

[NOTICE]
Django legt automatisch eine `id`-Spalte als Primärschlüssel an, wenn Sie keinen
eigenen definieren.
[ENDNOTICE]

[EQ] Öffnen Sie die Datei `webapp/migrations/0001_initial.py`. Was enthält sie? Nehmen Sie
außerdem an, Sie fügen dem Model nachträglich das Attribut
`phone = models.CharField(max_length=20)` hinzu: Was müssten Sie tun, damit sich diese
Änderung auch in der Tabelle niederschlägt?
<!-- time estimate: 15 min -->

### Daten anlegen (CREATE)

Die Tabelle existiert jetzt. Ein Objekt lässt sich direkt in der Datenbank anlegen:

```
Model.objects.create(**kwargs)
```

- `**kwargs`: die Feldwerte des neuen Objekts als Schlüsselwortargumente (z. B.
  `name=..., age=..., email=...`); erzeugt das Objekt und speichert es in einem Schritt in
  der Datenbank

[EC] Öffnen Sie die Shell und legen Sie einen ersten Datensatz an:

```bash
python manage.py shell
```

Geben Sie am Prompt (`>>>`) der interaktiven Shell folgenden Python-Code ein:

```python
from webapp.models import Student
Student.objects.create(name="Anna Müller", age=22, email="anna@example.com")
print(Student.objects.all())
```

Die Ausgabe zeigt `<QuerySet [<Student: Student object (1)>]>`. Ein **QuerySet** ist die
Liste von Objekten, die eine Datenbankabfrage zurückgibt; die Darstellung
`Student object (1)` darin ist nicht besonders aussagekräftig, weil Django ein Objekt
ohne eigene Angabe standardmäßig als `Klassenname object (id)` darstellt.
Wie ein Objekt stattdessen als Text dargestellt wird, legt die Methode `__str__()` fest,
die wir nun ergänzen wollen:

```python
def __str__(self):
    ...
```

`self` ist dabei die Model-Instanz selbst.
Die Methode muss einen `str`-Wert zurückgeben, der dann als Textdarstellung des Objekts verwendet wird.

[ER] Ergänzen Sie das Model um eine sinnvolle Fassung von `__str__()`:

[SNIPPET::ALT::django_model_student_str]

[EC] Verlassen Sie die Shell (`exit()`), starten Sie sie neu und rufen Sie erneut
`Student.objects.all()` auf:

```bash
python manage.py shell
```

```python
from webapp.models import Student
print(Student.objects.all())
```

[EQ] Was hat sich an der Ausgabe geändert, und warum war dafür keine neue Migration nötig
(anders als bei einem neuen Feld)?
<!-- time estimate: 15 min -->

Neben `objects.create()` gibt es einen zweiten Weg, ein Objekt anzulegen: es
zunächst als Python-Objekt erzeugen und danach separat speichern.

```
Model(**kwargs)
instance.save()
```

- `Model(**kwargs)`: die Feldwerte als Schlüsselwortargumente; erzeugt ein neues Objekt nur
  im Speicher, **ohne** es in der Datenbank zu speichern
- `save()`: kein Pflichtparameter für den Standardfall; schreibt die aktuellen Feldwerte des
  Objekts in die Datenbank (bei neuen Objekten als INSERT, bei bereits gespeicherten als
  UPDATE)

Damit lässt sich ein Objekt auf zwei Arten anlegen:

```python
# Variante 1: Objekt erzeugen, dann speichern
student = Student(name="Tom Fischer", age=25, email="tom@example.com")
student.save()

# Variante 2: Erzeugen und speichern in einem Schritt
Student.objects.create(name="Julia Becker", age=23, email="julia@example.com")
```

[EC] Legen Sie in der Shell Max Schmidt mit Variante 1 (`Student(...)` + `save()`) und Lisa
Weber mit Variante 2 (`objects.create()`) an und lassen Sie sich danach
`Student.objects.all()` ausgeben.

[EQ] Beide Varianten führen zum selben Ergebnis in der Datenbank. Gibt es dennoch eine
Situation, in der Sie zwingend `Student(...)` + `save()` statt `objects.create()`
verwenden müssten?

[HINT::Worauf sollte ich achten?]
Was passiert zwischen dem Erzeugen des Objekts und dem Speichern?
[ENDHINT]
<!-- time estimate: 10 min -->

### Daten lesen (READ)

Nachdem nun mehrere Studierende angelegt sind, lassen sie sich auch wieder auslesen.
Lesezugriffe mit Django entsprechen SQL `SELECT`-Abfragen (vgl. [PARTREF::sql-SELECT]):

```
Model.objects.all()
Model.objects.get(**kwargs)
Model.objects.filter(**kwargs)
```

- `all()`: keine Parameter; liefert ein QuerySet mit allen Objekten der Tabelle
- `get(**kwargs)`: Feld-Lookup-Paare (z. B. `id=1`); liefert genau ein passendes Objekt
  zurück; findet sich kein oder mehr als ein passendes Objekt, wird ein Fehler ausgelöst
- `filter(**kwargs)`: Feld-Lookup-Paare; liefert ein QuerySet mit allen passenden Objekten,
  auch wenn keins oder mehrere passen (kein Fehler)

```python
print(Student.objects.all())
print(Student.objects.get(id=42))
print(Student.objects.filter(name="Fritz Muster"))
```

[EC] Öffnen Sie die Shell und rufen Sie darin `Student.objects.all()`,
`Student.objects.get(id=1)` und `Student.objects.filter(name="Anna Müller")` auf.

[EQ] `get()` und `filter()` liefern beide Objekte anhand eines Kriteriums zurück, aber
mit unterschiedlichem Rückgabetyp. Was passiert bei `get()`, wenn kein oder mehr als ein
Objekt zum Kriterium passt, und warum ist das bei `filter()` unproblematisch?
<!-- time estimate: 10 min -->

### Daten ändern (UPDATE)

Ändern mit Django entspricht SQL `UPDATE` (vgl. [PARTREF::sql-UPDATE-VIEW-CASE]): Dabei wird
ein Objekt zunächst geladen, dann ein Attribut verändert und schließlich gespeichert.

```python
student = Student.objects.get(id=42)
student.email = "neu@example.com"
student.save()
```

[EC] Laden Sie den Studierenden mit `id=1` per `get()`, setzen Sie `age` auf `23` und
speichern Sie die Änderung mit `save()`. Bestätigen Sie die Änderung mit einem erneuten
`get(id=1)`.

[EQ] Was würde passieren, wenn Sie `save()` nach der Änderung vergessen? Woran würden Sie
das bemerken?
<!-- time estimate: 10 min -->

### Daten löschen (DELETE)

Ähnlich wie beim Ändern wird das Objekt zunächst per `get()` geladen, diesmal jedoch nicht
gespeichert, sondern gelöscht:

```
instance.delete()
```

- kein Pflichtparameter für den Standardfall; entfernt den zugehörigen Datensatz endgültig
  aus der Datenbank

```python
student = Student.objects.get(id=42)
student.delete()
```

[WARNING]
`delete()` entfernt den Datensatz sofort und endgültig, ohne Rückfrage.
[ENDWARNING]

[EC] Laden Sie den Studierenden mit `id=2` per `get()` und löschen Sie ihn mit `delete()`.
Bestätigen Sie mit `Student.objects.all()`, dass er verschwunden ist.

[EQ] Angenommen, Sie führen `Student.objects.get(id=2).delete()` versehentlich ein
zweites Mal aus. Was passiert dabei, und warum? Vergleichen Sie auch das mögliche
Risiko, das `delete()` mit sich bringt, mit einem Lesezugriff wie
`Student.objects.all()`.

[HINT::Worauf sollte ich achten?]
Was haben Sie in [EREFQ::4] über das Verhalten von `get()` gelernt, wenn kein passendes
Objekt existiert?
[ENDHINT]
<!-- time estimate: 10 min -->

### Weitere Feldtypen

Das `Student`-Model kennt bisher nur die drei einfachen Feldtypen aus dem ersten Entwurf.
Um weitere Datentypen abzudecken, lernen Sie zwei zusätzliche Feldtypen kennen:

- `BooleanField(default=True)`: Wahrheitswert, hier mit Standardwert `True`.
- `DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)`: Dezimalzahl mit
  fester Genauigkeit (hier: bis zu 3 Ziffern gesamt, davon 2 Nachkommastellen).

Das `DecimalField` ist zusätzlich mit den **Feldoptionen** `null` und `blank` definiert,
weil nicht jeder Studierende bereits einen Notendurchschnitt hat. Die beiden Optionen
werden häufig verwechselt, regeln aber unterschiedliche Ebenen: `null=True` erlaubt den
Datenbankwert `NULL` (Datenbankebene), während `blank=True` ein Feld in
Formularen/Validierung als optional markiert (Eingabeebene). Ein Feld kann auch beides
gleichzeitig sein; Standard für beide ist `False`.

[NOTICE]
**Wann brauche ich `null`, wann `blank`?**  
Ein Beispiel macht den Unterschied greifbar: Ein optionales Kommentarfeld vom Typ
`CharField` sollte `blank=True` bekommen (im Formular darf es leer bleiben), aber **nicht**
zwingend `null=True`. Django speichert bei `CharField` einen leeren String `""` statt
`NULL`, wenn nichts eingegeben wurde.  
`null=True` ist eher für Felder wie `DateField` oder
`IntegerField` relevant, bei denen es keinen sinnvollen "leeren" Wert gibt und daher
`NULL` in der Datenbank stehen muss.
[ENDNOTICE]

[ER] Erweitern Sie das `Student`-Model um zwei weitere Felder:

[SNIPPET::ALT::django_model_student_extended]

[EC] Erstellen und wenden Sie die Migration für die neuen Felder an:

```bash
python manage.py makemigrations webapp
python manage.py migrate
```
<!-- time estimate: 15 min -->

### Model in der Admin-Oberfläche verwalten

Django bringt eine fertige Verwaltungsoberfläche mit, in der registrierte Models über den
Browser statt über die Shell bearbeitet werden können.

```
admin.site.register(ModelClass)
```

- `ModelClass`: die Model-Klasse, die über die Admin-Oberfläche verwaltbar werden soll

[ER] Registrieren Sie `Student` in `webapp/admin.py`:

[SNIPPET::ALT::django_model_admin_register]

Damit Sie sich an der Admin-Oberfläche anmelden können, benötigen Sie ein
Administrator-Konto (**Superuser**), einen Benutzer mit vollem Zugriff auf alle
registrierten Models.

[EC] Legen Sie einen Superuser mit Benutzername `admin`, E-Mail `admin@example.com` und
Passwort `propraadmin` an (folgen Sie den interaktiven Eingabeaufforderungen):

```bash
python manage.py createsuperuser
```

[ER] Starten Sie den Entwicklungsserver mit `python manage.py runserver 8071`, öffnen Sie
`http://127.0.0.1:8071/admin/`, melden Sie sich mit Ihrem Superuser an und öffnen Sie die
Übersicht Ihrer `Student`-Objekte.

[EQ] Welche Studierenden werden in der Übersicht angezeigt, und woran erkennen Sie, dass
hier dieselbe `__str__()`-Darstellung verwendet wird wie zuvor in der Shell?
<!-- time estimate: 15 min -->

### Anlegen über die Admin-Oberfläche

[ER] Legen Sie über die Admin-Oberfläche einen weiteren Studierenden an: Name
`Peter Klein`, Alter `26`, E-Mail `peter@example.com`.
<!-- time estimate: 5 min -->

[EQ] Sie haben soeben über die Shell einen Studierenden mit `.objects.create(...)`
angelegt und einen weiteren über die Admin-Oberfläche im Browser. Landen beide
tatsächlich in derselben Tabelle mit derselben Struktur, oder unterscheidet sich der über
die Admin-Oberfläche angelegte Datensatz auf irgendeine Weise von dem über die Shell
angelegten? Woran könnten Sie das in der Datenbank überprüfen?
<!-- time estimate: 10 min -->

### Weiterführend

- [Models](https://docs.djangoproject.com/en/stable/topics/db/models/) – Umfassende
  Dokumentation zu Django-Modellen
- [Model field reference](https://docs.djangoproject.com/en/stable/ref/models/fields/) –
  Referenz zu allen verfügbaren Feldtypen und -optionen
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Kontrollergebnisse]
**Knackpunkte:**

- [EREFR::2] + [EREFQ::2]: Nach Ergänzen von `__str__()` zeigt die Shell den Namen statt
  `Student object (1)`; Student erkennt, dass dafür keine Migration nötig war, weil
  `__str__()` kein Datenbankfeld ist, sondern nur die Python-seitige Darstellung betrifft.
- [EREFQ::8]: Student erkennt, dass ein über die Admin-Oberfläche angelegter Datensatz
  sich in nichts von einem über die Shell angelegten unterscheidet (gleiche Tabelle,
  gleiche Struktur), und kann dies z. B. mit `filter()`/`get()` in der Shell überprüfen.
- [EREFQ::4]: Student erkennt, dass `get()` bei keinem oder mehreren Treffern einen Fehler
  auslöst (eindeutiges Einzelobjekt erwartet), während `filter()` immer ein (ggf. leeres)
  QuerySet zurückgibt.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-model.md]

### Kommandoprotokoll
[PROT::ALT:django-model.prot]
[ENDINSTRUCTOR]
