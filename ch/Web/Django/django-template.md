title: Django Template System - Trennung von Daten und Darstellung
stage: alpha
timevalue: 2
difficulty: 2
assumes: django-basics, django-project, django-admin
---

[SECTION::goal::idea,experience]

- Ich verstehe das Model-View-Template (MVT) Muster in Django und die Vorteile der Trennung von Geschäftslogik und Darstellung.
- Ich kann Django-Templates erstellen und mit Template-Variablen arbeiten.
- Ich kann Template-Tags für bedingte Darstellung und Schleifen verwenden.
- Ich kann Template-Vererbung einsetzen, um wiederverwendbare HTML-Strukturen zu erstellen.
- Ich kann statische Dateien in Templates einbinden und konfigurieren.

[ENDSECTION]

[SECTION::background::default]

Das Django Template System ist eine zentrale Komponente für die Trennung von Geschäftslogik und Darstellung. 
Während Views die Datenverarbeitung übernehmen, sind Templates ausschließlich für die Präsentation der Daten zuständig. 
Dies folgt dem Model-View-Template (MVT) Architekturmuster und ermöglicht eine saubere Codestruktur, 
bessere Wartbarkeit und die Zusammenarbeit zwischen Entwicklern und Designern.

[ENDSECTION]

[SECTION::instructions::detailed]

### Django-Projekt vorbereiten

Bitte lesen Sie zunächst [PARTREF::django-basics] und folgen Sie den dort beschriebenen 
Schritten, um Django in einer virtuellen Umgebung erfolgreich zu installieren.

Erstellen Sie ein Projekt namens **meinprojekt**, indem Sie zunächst [PARTREF::django-project] 
lesen und den dort beschriebenen Schritten folgen, 
um in einer virtuellen Umgebung erfolgreich ein neues Django-Projekt anzulegen.

**Django-Server starten**:
```bash
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

[EC] Stellen Sie sicher, dass Ihr Django-Projekt läuft und zeigen Sie die erfolgreiche 
Server-Anzeige mit `python manage.py runserver` und dann beenden Sie den Server beispielsweise 
mit `Strg + C` (unter macOS ebenfalls `control + C`).
<!-- EC1 -->
<!-- time estimate: 5 min -->

### Template-Verzeichnis konfigurieren

Django Templates werden in speziellen Verzeichnissen gespeichert. 
Zunächst müssen wir die Template-Konfiguration in den Projekteinstellungen anpassen.

[ER] Erstellen Sie ein `templates`-Verzeichnis im Hauptprojektordner 
und öffnen Sie `meinprojekt/settings.py` und modifizieren Sie die `TEMPLATES`-Konfiguration:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Hier anpassen
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
<!-- ER1 -->

### Erstes Template erstellen

Templates sind HTML-Dateien mit spezieller Django-Syntax für dynamische Inhalte.

[ER] Erstellen Sie die Datei `templates/hello.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Django Template Demo</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>Willkommen bei Django Templates!</p>
</body>
</html>
```
<!-- ER2 -->

Die doppelten geschweiften Klammern `{{ greeting }}` sind Template-Variablen, 
die von der View mit Daten gefüllt werden.

[ER] Erstellen Sie eine neue View-Funktion in `meinprojekt/views.py`:

```python
from django.shortcuts import render

def hello_template(request):
    context = {
        'greeting': 'Hallo Django Templates!'
    }
    return render(request, 'hello.html', context)
```
<!-- ER3 -->

[ER] Fügen Sie die neue Route in `meinprojekt/urls.py` hinzu:

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-template/', views.hello_template, name='hello_template'),
]
```
<!-- ER4 -->

[EQ] Testen Sie die URL `http://127.0.0.1:8000/hello-template/` im Browser. 
Was wird anstelle von `{{ greeting }}` angezeigt und warum? 
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ1 -->
<!-- time estimate: 20 min -->

### Template-Variablen und Context

Der `context`-Dictionary übergibt Daten von der View an das Template.

[ER] Erweitern Sie die View `hello_template` um mehr Variablen:

```python
def hello_template(request):
    context = {
        'greeting': 'Hallo Django Templates!',
        'user_name': 'Anna',
        'current_year': 2024,
        'is_logged_in': True
    }
    return render(request, 'hello.html', context)
```
<!-- ER5 -->

[ER] Erweitern Sie `templates/hello.html` um die neuen Variablen:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Django Template Demo</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>Willkommen {{ user_name }}!</p>
    <p>Jahr: {{ current_year }}</p>
    <p>Angemeldet: {{ is_logged_in }}</p>
</body>
</html>
```
<!-- ER6 -->

[EQ] Aktualisieren Sie die Seite `http://127.0.0.1:8000/hello-template/` im Browser. 
Welche neuen Informationen werden jetzt angezeigt? Listen Sie alle sichtbaren Template-Variablen auf.
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ2 -->

Wenn Sie mehr über Template-Variablen erfahren möchten:
[Django Template Variables](https://docs.djangoproject.com/en/4.2/topics/templates/#variables)

<!-- time estimate: 10 min -->

### Template-Tags: Bedingte Darstellung

Template-Tags verwenden geschweifte Klammern mit Prozentzeichen `{% %}` für Logik.

[ER] Erweitern Sie `templates/hello.html` um bedingte Darstellung:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Django Template Demo</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    
    {% if is_logged_in %}
        <p>Willkommen zurück, {{ user_name }}!</p>
        <p>Sie sind erfolgreich angemeldet.</p>
    {% else %}
        <p>Bitte melden Sie sich an.</p>
    {% endif %}
    
    <p>Jahr: {{ current_year }}</p>
</body>
</html>
```
<!-- ER7 -->

[EQ] Aktualisieren Sie die Seite `http://127.0.0.1:8000/hello-template/` im Browser. 
Ändern Sie in der View `is_logged_in` auf `False`. Was passiert mit der Anzeige?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ3 -->

<!-- time estimate: 10 min -->

### Template-Tags: Schleifen

Listen und andere Sammlungen können mit `{% for %}` durchlaufen werden.

[ER] Erweitern Sie die View um eine Liste:

```python
def hello_template(request):
    context = {
        'greeting': 'Hallo Django Templates!',
        'user_name': 'Anna',
        'current_year': 2024,
        'is_logged_in': True,
        'hobbies': ['Programmieren', 'Lesen', 'Sport', 'Musik']
    }
    return render(request, 'hello.html', context)
```
<!-- ER8 -->

[ER] Erweitern Sie das Template um die Hobby-Liste:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Django Template Demo</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    
    {% if is_logged_in %}
        <p>Willkommen zurück, {{ user_name }}!</p>
        
        <h2>Ihre Hobbies:</h2>
        <ul>
        {% for hobby in hobbies %}
            <li>{{ hobby }}</li>
        {% empty %}
            <li>Keine Hobbies angegeben</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Bitte melden Sie sich an.</p>
    {% endif %}
    
    <p>Jahr: {{ current_year }}</p>
</body>
</html>
```
<!-- ER9 -->

Das `{% empty %}` Tag zeigt alternative Inhalte, wenn die Liste leer ist.

[EQ] Aktualisieren Sie die Seite `http://127.0.0.1:8000/hello-template/` im Browser. 
Ändern Sie dann in der View die `hobbies`-Liste zu einer leeren Liste `[]`. 
Was wird angezeigt und welcher Django-Tag ist dafür verantwortlich?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ4 -->

Mehr Details zu Template-Tags finden Sie hier:
[Django Template Tags](https://docs.djangoproject.com/en/4.2/topics/templates/#tags)
<!-- time estimate: 15 min -->

### Template-Vererbung: Base Template

Template-Vererbung vermeidet Code-Duplikation durch wiederverwendbare HTML-Strukturen.

[ER] Erstellen Sie `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django Template System{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        header { background: #333; color: white; padding: 10px; margin-bottom: 20px; }
        footer { margin-top: 40px; text-align: center; color: #666; }
    </style>
</head>
<body>
    <header>
        <h1>Django Template Demo</h1>
    </header>
    
    <main>
        {% block content %}
        <!-- Hier wird der Inhalt der Child-Templates eingefügt -->
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Django Template System</p>
    </footer>
</body>
</html>
```
<!-- ER10 -->

[ER] Erstellen Sie `templates/welcome.html` mit Template-Vererbung:

```html
{% extends "base.html" %}

{% block title %}Willkommen - Django Templates{% endblock %}

{% block content %}
    <h2>{{ greeting }}</h2>
    
    {% if is_logged_in %}
        <div style="border: 1px solid green; padding: 15px; background: #f0f8f0;">
            <p>Willkommen zurück, <strong>{{ user_name }}</strong>!</p>
            
            <h3>Ihre Hobbies:</h3>
            <ul>
            {% for hobby in hobbies %}
                <li>{{ hobby }}</li>
            {% empty %}
                <li>Keine Hobbies angegeben</li>
            {% endfor %}
            </ul>
        </div>
    {% else %}
        <div style="border: 1px solid red; padding: 15px; background: #f8f0f0;">
            <p>Bitte melden Sie sich an.</p>
        </div>
    {% endif %}
{% endblock %}
```
<!-- ER11 -->

[ER] Erstellen Sie eine neue View für das Welcome-Template:

```python
def welcome(request):
    context = {
        'greeting': 'Willkommen auf unserer Seite!',
        'user_name': 'Maria',
        'current_year': 2024,
        'is_logged_in': True,
        'hobbies': ['Fotografie', 'Reisen', 'Kochen']
    }
    return render(request, 'welcome.html', context)
```
<!-- ER12 -->

[ER] Fügen Sie die Route in `urls.py`hinzu:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-template/', views.hello_template, name='hello_template'),
    path('welcome/', views.welcome, name='welcome'),
]
```
<!-- ER13 -->

[EQ] Testen Sie beide URLs: `http://127.0.0.1:8000/hello-template/` und `http://127.0.0.1:8000/welcome/`. 
Was ist der Vorteil der Template-Vererbung gegenüber der Wiederholung von HTML-Code?
Wenn Sie Port 8080 verwenden, ändern Sie die Links bitte entsprechend.
<!-- EQ5 -->
<!-- time estimate: 20 min -->

### Statische Dateien einbinden

Statische Dateien wie CSS, JavaScript und Bilder werden über das `{% static %}` Tag eingebunden.

[EC] Erstellen Sie Verzeichnisse für statische Dateien im Hauptprojektordner:
```bash
cd meinprojekt
mkdir -p static/css static/js static/images
```
<!-- EC2 -->

[ER] Erstellen Sie `static/css/style.css`:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    margin-bottom: 30px;
    border-radius: 8px;
}

.hobby-list {
    background: #e8f4fd;
    padding: 15px;
    border-radius: 5px;
    border-left: 4px solid #2196F3;
}

footer {
    margin-top: 40px;
    text-align: center;
    color: #666;
    font-size: 0.9em;
}
```
<!-- ER14 -->

[ER] Aktualisieren Sie `settings.py` für statische Dateien:

```python
# Am Ende der Datei hinzufügen
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
<!-- ER15 -->

[ER] Aktualisieren Sie `templates/base.html` mit statischen Dateien:

```html
{% load static %}
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django Template System{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <header>
            <h1>Django Template Demo</h1>
        </header>
        
        <main>
            {% block content %}
            <!-- Hier wird der Inhalt der Child-Templates eingefügt -->
            {% endblock %}
        </main>
        
        <footer>
            <p>&copy; 2024 Django Template System</p>
        </footer>
    </div>
</body>
</html>
```
<!-- ER16 -->

[ER] Aktualisieren Sie `templates/welcome.html` mit CSS-Klassen:

```html
{% extends "base.html" %}

{% block title %}Willkommen - Django Templates{% endblock %}

{% block content %}
    <h2>{{ greeting }}</h2>
    
    {% if is_logged_in %}
        <div class="hobby-list">
            <p>Willkommen zurück, <strong>{{ user_name }}</strong>!</p>
            
            <h3>Ihre Hobbies:</h3>
            <ul>
            {% for hobby in hobbies %}
                <li>{{ hobby }}</li>
            {% empty %}
                <li>Keine Hobbies angegeben</li>
            {% endfor %}
            </ul>
        </div>
    {% else %}
        <div style="border: 1px solid red; padding: 15px; background: #f8f0f0;">
            <p>Bitte melden Sie sich an.</p>
        </div>
    {% endif %}
{% endblock %}
```
<!-- ER17 -->

Falls noch Fragen offen sind, hilft diese Ressource weiter:
[Django Static Files](https://docs.djangoproject.com/en/4.2/howto/static-files/)
<!-- time estimate: 10 min -->

### Template-Filter verwenden

Template-Filter modifizieren Variablenwerte bei der Anzeige.

[ER] Erstellen Sie eine neue View mit verschiedenen Datentypen:

```python
from datetime import datetime

def filter_demo(request):
    context = {
        'current_year': 2024,
        'long_text': 'Dies ist ein sehr langer Text, der demonstriert, wie Template-Filter funktionieren.',
        'user_name': 'anna müller',
        'price': 29.99,
        'creation_date': datetime.now(),
        'description': '<p>Dies ist <strong>HTML-Text</strong> mit Tags.</p>'
    }
    return render(request, 'filter_demo.html', context)
```
<!-- ER18 -->

[ER] Erstellen Sie `templates/filter_demo.html`:

```html
{% extends "base.html" %}

{% block title %}Template-Filter Demo{% endblock %}

{% block content %}
    <h2>Template-Filter Demonstration</h2>
    
    <div class="hobby-list">
        <h3>String-Filter:</h3>
        <p>Original: {{ user_name }}</p>
        <p>Großbuchstaben: {{ user_name|upper }}</p>
        <p>Titel-Format: {{ user_name|title }}</p>
        <p>Erstes Zeichen: {{ user_name|first }}</p>
        
        <h3>Text-Filter:</h3>
        <p>Gekürzt (30 Zeichen): {{ long_text|truncatechars:30 }}</p>
        <p>Gekürzt (5 Wörter): {{ long_text|truncatewords:5 }}</p>
        
        <h3>Zahlen-Filter:</h3>
        <p>Preis: {{ price|floatformat:2 }}€</p>
        
        <h3>Datum-Filter:</h3>
        <p>Datum formatiert: {{ creation_date|date:"d.m.Y H:i" }}</p>
        
        <h3>HTML-Filter:</h3>
        <p>Escaped: {{ description }}</p>
        <p>Safe HTML: {{ description|safe }}</p>
        
        <h3>Standard-Werte:</h3>
        <p>Leer oder Standardwert: {{ empty_var|default:"Kein Wert vorhanden" }}</p>
    </div>
{% endblock %}
```
<!-- ER19 -->

[ER] Fügen Sie die Route in `urls.py` hinzu:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-template/', views.hello_template, name='hello_template'),
    path('welcome/', views.welcome, name='welcome'),
    path('filter-demo/', views.filter_demo, name='filter_demo'),
]
```
<!-- ER20 -->

Hier gibt es ein kompaktes Tutorial zum Thema:
[Django Template Filters](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#built-in-filter-reference)

<!-- time estimate: 10 min -->

### Template-Navigation erstellen

[ER] Erweitern Sie `templates/base.html` um Navigation:

```html
{% load static %}
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Django Template System{% endblock %}</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <header>
            <h1>Django Template Demo</h1>
            <nav style="margin-top: 15px;">
                <a href="{% url 'hello_template' %}" style="color: white; margin-right: 15px;">Hello Template</a>
                <a href="{% url 'welcome' %}" style="color: white; margin-right: 15px;">Welcome</a>
                <a href="{% url 'filter_demo' %}" style="color: white;">Filter Demo</a>
            </nav>
        </header>
        
        <main>
            {% block content %}
            <!-- Hier wird der Inhalt der Child-Templates eingefügt -->
            {% endblock %}
        </main>
        
        <footer>
            <p>&copy; 2024 Django Template System</p>
        </footer>
    </div>
</body>
</html>
```
<!-- ER21 -->

[EQ] Testen Sie alle drei Seiten über die Navigation: `http://127.0.0.1:8000/hello-template/`, 
`http://127.0.0.1:8000/welcome/` und `http://127.0.0.1:8000/filter-demo/`. 
Vergleichen Sie die visuellen Unterschiede zwischen den Seiten und erklären Sie den Vorteil 
der `{% url %}` Tags gegenüber fest programmierten Links.
Wenn Sie Port 8080 verwenden, ändern Sie die Links bitte entsprechend.
<!-- EQ6 -->

<!-- time estimate: 20 min -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-template.md]

### Kommandoprotokoll
[PROT::ALT:django-template.prot]

[ENDINSTRUCTOR]