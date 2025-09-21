title: Django Modelle und ORM
stage: draft
timevalue: 2.5
difficulty: 2
assumes: django-project
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept von Django ORM und dessen Vor- und Nachteile.
- Ich kann Django-Modelle definieren und Datenbankmigrationen durchführen.
- Ich kann grundlegende CRUD-Operationen (Create, Read, Update, Delete) mit Django-Modellen ausführen.
- Ich verstehe die Beziehung zwischen Django-Modellen und Datenbanktabellen.

[ENDSECTION]

[SECTION::background::default]

Django bietet ein mächtiges Object-Relational Mapping (ORM) System, das es ermöglicht, 
mit Datenbanken zu arbeiten, ohne direkt SQL schreiben zu müssen. 
Das ORM fungiert als Brücke zwischen Python-Objekten und Datenbankstrukturen und 
unterstützt verschiedene Datenbanksysteme wie SQLite, PostgreSQL, MySQL und Oracle.

In dieser Aufgabe lernen wir, wie man Modelle definiert und grundlegende Datenbankoperationen durchführt.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist Django ORM?

Object-Relational Mapping (ORM) ist eine Technik, die es ermöglicht, 
zwischen objektorientierten Programmiersprachen und relationalen Datenbanken zu übersetzen.

**Vorteile von ORM:**

- Höhere Entwicklungseffizienz
- Datenbankwechsel ohne Code-Änderungen möglich
- Schutz vor SQL-Injection-Angriffen
- Automatische Validierung und Typsicherheit

**Nachteile von ORM:**

- Performance-Overhead bei der SQL-Generierung
- Weniger Kontrolle über komplexe Abfragen
- Kann SQL-Kenntnisse vernachlässigen lassen

**ORM-Entsprechungen:**

- Python-Klasse ↔ Datenbanktabelle
- Klassenattribut ↔ Tabellenspalte
- Klasseninstanz ↔ Tabellenzeile

Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[Django Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)

[EQ] Erklären Sie in eigenen Worten, was ORM bedeutet und welche Hauptvorteile es bietet.  
<!-- EQ1 -->  
<!-- time estimate: 15 min -->

### Django-App für Modelle erstellen

Django-Modelle müssen in einer App definiert werden.  
Erstellen Sie eine neue App für unsere Datenbankexperimente:

[EC] Erstellen Sie eine neue Django-App namens `mymodels`:

```bash
python manage.py startapp mymodels
```
<!-- EC1 -->

[ER] Registrieren Sie die neue App in `settings.py`:  

Fügen Sie `'mymodels'` zur `INSTALLED_APPS`-Liste hinzu:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mymodels',  # Neue App hinzufügen
]
```
<!-- ER1 -->  
<!-- time estimate: 10 min -->

### Erstes Django-Modell definieren

[ER] Erstellen Sie in `mymodels/models.py` ein einfaches Modell:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```
<!-- ER2 -->

**Wichtige Feldtypen:**
- `CharField(max_length=n)` - Textfeld mit maximaler Länge
- `IntegerField()` - Ganzzahlen
- `EmailField()` - E-Mail-Adressen (mit Validierung)
- `DateTimeField()` - Datum und Zeit
- `auto_now_add=True` - Automatisch beim Erstellen setzen

Die `__str__`-Methode definiert, wie das Objekt als String dargestellt wird.

Neugierig geworden? Dann lesen Sie hier weiter:
[Model field reference](https://docs.djangoproject.com/en/4.2/ref/models/fields/)

[EQ] Was bewirkt der Parameter `auto_now_add=True` bei einem `DateTimeField`?  
<!-- EQ2 -->  
<!-- time estimate: 15 min -->

### Datenbankmigrationen erstellen und anwenden

Django verwendet Migrationen, um Änderungen am Datenbankschema zu verwalten:

[EC] Erstellen Sie eine Migration für das neue Modell:

```bash
python manage.py makemigrations mymodels
```
<!-- EC2 -->

[EC] Wenden Sie die Migration an:

```bash
python manage.py migrate
```
<!-- EC3 -->

[NOTICE]  
Django erstellt automatisch eine `id`-Spalte als Primärschlüssel,  
auch wenn Sie keinen explizit definieren.  
[ENDNOTICE]

[EC] Überprüfen Sie die erstellte Migrationsdatei:

```bash
cat mymodels/migrations/0001_initial.py
```
<!-- EC4 -->

[EQ] Welche Datei wurde durch `makemigrations` erstellt und was enthält sie?  
<!-- EQ3 -->  
<!-- time estimate: 15 min -->

### Django Shell für Datenbankoperationen

Die Django Shell ermöglicht interaktive Datenbankoperationen:

[EC] Starten Sie die Django Shell:

```bash
python manage.py shell
```
<!-- EC5 -->

### Daten erstellen (CREATE)

[ER] Führen Sie in der Django Shell folgende Operationen aus:

```python
# Modell importieren
from mymodels.models import Student

# Ersten Studenten erstellen
student1 = Student(name="Anna Müller", age=22, email="anna@example.com")
student1.save()

# Zweiten Studenten erstellen (alternative Methode)
student2 = Student.objects.create(
    name="Max Schmidt", 
    age=24, 
    email="max@example.com"
)

# Dritten Studenten erstellen
student3 = Student.objects.create(
    name="Lisa Weber", 
    age=21, 
    email="lisa@example.com"
)

print("Studenten erstellt!")
```
<!-- ER3 -->

[EQ] Was ist der Unterschied zwischen `Student()` + `save()` und `Student.objects.create()`?  
<!-- EQ4 -->  
<!-- time estimate: 20 min -->

### Daten abfragen (READ)

[ER] Führen Sie verschiedene Abfragen aus:

```python
# Alle Studenten abrufen
all_students = Student.objects.all()
print("Alle Studenten:", all_students)

# Einzelnen Studenten nach ID abrufen
student = Student.objects.get(id=1)
print("Student mit ID 1:", student)

# Studenten nach Name filtern
anna = Student.objects.filter(name="Anna Müller")
print("Anna:", anna)

# Studenten nach Alter filtern
young_students = Student.objects.filter(age__lt=23)  # Alter < 23
print("Junge Studenten:", young_students)

# Anzahl der Studenten
count = Student.objects.count()
print("Anzahl Studenten:", count)

# Studenten sortieren
sorted_students = Student.objects.order_by('age')
print("Nach Alter sortiert:", sorted_students)
```
<!-- ER4 -->

**Wichtige QuerySet-Methoden:**
- `all()` - Alle Objekte
- `get()` - Ein spezifisches Objekt (wirft Fehler wenn nicht eindeutig)
- `filter()` - Objekte nach Bedingungen filtern
- `count()` - Anzahl der Objekte
- `order_by()` - Sortierung

Hier gibt es ein kompaktes Tutorial zum Thema:
[Making queries](https://docs.djangoproject.com/en/4.2/topics/db/queries/)

[EQ] Was passiert, wenn `get()` kein Objekt oder mehrere Objekte findet?  
<!-- EQ5 -->  
<!-- time estimate: 25 min -->

### Daten aktualisieren (UPDATE)

[ER] Aktualisieren Sie Studentendaten:

```python
# Einzelnen Studenten aktualisieren
student = Student.objects.get(id=1)
student.age = 23
student.save()
print("Anna's Alter aktualisiert")

# Mehrere Studenten gleichzeitig aktualisieren
Student.objects.filter(age__gte=23).update(age=25)
print("Ältere Studenten aktualisiert")

# Überprüfung
updated_students = Student.objects.all()
for s in updated_students:
    print(f"{s.name}: {s.age} Jahre")
```
<!-- ER5 -->

[EQ] Was ist der Unterschied zwischen `save()` und `update()` bei der Datenaktualisierung?  
<!-- EQ6 -->  
<!-- time estimate: 15 min -->

### Daten löschen (DELETE)

[ER] Löschen Sie Studentendaten:

```python
# Einzelnen Studenten löschen
student_to_delete = Student.objects.get(id=2)
student_to_delete.delete()
print("Max Schmidt gelöscht")

# Mehrere Studenten nach Bedingung löschen
Student.objects.filter(age=25).delete()
print("Studenten mit Alter 25 gelöscht")

# Verbleibende Studenten anzeigen
remaining = Student.objects.all()
print("Verbleibende Studenten:", remaining)
```
<!-- ER6 -->

[WARNING]  
`delete()` löscht Daten permanent ohne Rückfrage!  
Seien Sie besonders vorsichtig mit `objects.all().delete()`.  
[ENDWARNING]

[EC] Verlassen Sie die Django Shell:

```python
exit()
```
<!-- EC6 -->  
<!-- time estimate: 15 min -->

### Erweiterte Modellfelder

[ER] Erweitern Sie das Student-Modell um weitere Felder:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    grade_average = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.age})"
```
<!-- ER7 -->

**Neue Feldtypen:**
- `auto_now=True` - Automatisch bei jeder Änderung aktualisieren
- `BooleanField()` - True/False-Werte
- `DecimalField()` - Dezimalzahlen mit fester Präzision
- `null=True` - NULL-Werte in der Datenbank erlaubt
- `blank=True` - Leere Werte in Formularen erlaubt

[EC] Erstellen und anwenden Sie die Migration:

```bash
python manage.py makemigrations mymodels
python manage.py migrate
```
<!-- EC7 -->  
<!-- time estimate: 20 min -->

### View für Datenbankoperationen erstellen

[ER] Erstellen Sie in `mymodels/views.py` eine View für Datenbankoperationen:

```python
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by('name')
    
    html = "<h1>Studentenliste</h1><ul>"
    for student in students:
        html += f"<li>{student.name} - {student.age} Jahre - {student.email}</li>"
    html += "</ul>"
    
    # Statistiken hinzufügen
    total_count = Student.objects.count()
    avg_age = Student.objects.aggregate(Avg('age'))['age__avg']
    
    html += f"<p>Gesamt: {total_count} Studenten</p>"
    if avg_age is not None:
        html += f"<p>Durchschnittsalter: {avg_age:.1f} Jahre</p>"
    
    return HttpResponse(html)

def add_sample_data(request):
    # Beispieldaten hinzufügen
    students_data = [
        {"name": "Tom Fischer", "age": 20, "email": "tom@example.com"},
        {"name": "Sarah Klein", "age": 22, "email": "sarah@example.com"},
        {"name": "David Braun", "age": 19, "email": "david@example.com"},
    ]
    
    for data in students_data:
        Student.objects.get_or_create(**data)
    
    return HttpResponse("Beispieldaten hinzugefügt! <a href='/students/'>Zur Liste</a>")
```
<!-- ER8 -->

[ER] Erstellen Sie `mymodels/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add-sample/', views.add_sample_data, name='add_sample'),
]
```
<!-- ER9 -->

[ER] Aktualisieren Sie die Haupt-`urls.py`:

```python
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('greet/<str:name>/', views.greet, name='greet'),
    path('hello-html/', views.hello_html, name='hello_html'),
    path('students/', include('mymodels.urls')),
]
```
<!-- ER10 -->

[EC] Testen Sie die neuen URLs:  
- `http://127.0.0.1:8000/students/add-sample/` - Beispieldaten hinzufügen  
- `http://127.0.0.1:8000/students/` - Studentenliste anzeigen  
<!-- EC8 -->

[EQ] Was bewirkt die Methode `get_or_create()` und warum ist sie nützlich?  
<!-- EQ7 -->  
<!-- time estimate: 25 min -->

### Datenbankabfragen mit Lookup-Feldern

[ER] Erweitern Sie `student_list` um erweiterte Filteroptionen:

```python
def student_list(request):
    # URL-Parameter für Filterung
    min_age = request.GET.get('min_age')
    max_age = request.GET.get('max_age')
    name_contains = request.GET.get('name')
    
    # Basis-QuerySet
    students = Student.objects.all()
    
    # Filter anwenden
    if min_age:
        students = students.filter(age__gte=min_age)
    
    if max_age:
        students = students.filter(age__lte=max_age)
    
    if name_contains:
        students = students.filter(name__icontains=name_contains)
    
    html = "<h1>Studentenliste</h1><ul>"
    for student in students:
        html += f"<li>{student.name} - {student.age} Jahre - {student.email}</li>"
    html += "</ul>"
    
    return HttpResponse(html)
```
<!-- ER11 -->

[EQ] Wie können Sie die Filteroptionen in der URL anpassen, um spezifische Ergebnisse zu erhalten?  
(Beispiel: `/students/?min_age=20&max_age=25&name=Tom`)  
<!-- EQ8 -->  
<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]  
[INCLUDE::/_include/Submission-Quellcode.md]  
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien  
[INCLUDE::ALT:django-model.md]

### Kommandoprotokoll  
[PROT::ALT:django-model.prot]

[ENDINSTRUCTOR]
```