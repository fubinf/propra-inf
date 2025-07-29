title: Django Templates - Grundlagen und Syntax
stage: draft
timevalue: 2.0
difficulty: 2
assumes: django-admin
---

[SECTION::goal::idea,experience]
Ich kann Django-Templates erstellen und verwenden, um die Trennung von Geschäftslogik und 
Präsentationsschicht zu implementieren. Ich beherrsche Template-Variablen, -Tags, -Filter 
und grundlegende Kontrollstrukturen.
[ENDSECTION]

[SECTION::background::default]
Bisher haben wir in Django-Views direkt HTML-Code mit `HttpResponse` zurückgegeben.
Das vermischt jedoch Geschäftslogik mit der Darstellung und widerspricht dem MVT-Prinzip 
(Model-View-Template) von Django.
Templates ermöglichen eine saubere Trennung: Python-Code verarbeitet die Daten,
Templates kümmern sich um die HTML-Ausgabe.
[ENDSECTION]

[SECTION::instructions::detailed]

### Template-System verstehen

Das Django-Template-System ist eine Kernkomponente, die es ermöglicht, 
dynamische HTML-Seiten durch einfache Tags und Variablen zu generieren.
Templates sind Textdateien (meist HTML), die spezielle Django-Syntax enthalten:

- **Variablen**: `{{ variable }}` - zeigen Daten aus Views an
- **Tags**: `{% tag %}` - steuern Template-Logik (Schleifen, Bedingungen)
- **Filter**: `{{ variable|filter }}` - modifizieren Variablen vor der Ausgabe
- **Kommentare**: `{# kommentar #}` - werden nicht gerendert

Weitere Informationen zum Template-System:
[Django Templates Documentation](https://docs.djangoproject.com/en/stable/topics/templates/)

### Template-Verzeichnis und erstes Template

[ER] Erstellen Sie in Ihrem Django-Projekt (aus [PARTREF::django-admin]) 
ein Verzeichnis `templates` im Hauptprojektverzeichnis (auf derselben Ebene wie `manage.py`).

[ER] Erstellen Sie in `templates/` eine Datei `hello.html` mit folgendem Inhalt:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Django Template Test</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>Willkommen bei Django Templates!</p>
</body>
</html>
```

### Template-Konfiguration in settings.py

[ER] Öffnen Sie `settings.py` und modifizieren Sie die `TEMPLATES`-Konfiguration.
Ändern Sie die `DIRS`-Liste zu `[BASE_DIR / "templates"]`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Diese Zeile ändern
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

### View mit Template-Rendering erstellen

[ER] Erstellen Sie in `views.py` eine neue View-Funktion `hello_template`:

```python
from django.shortcuts import render

def hello_template(request):
    context = {
        'greeting': 'Hallo aus dem Template!'
    }
    return render(request, 'hello.html', context)
```

[EQ] Die `render()`-Funktion nimmt drei Parameter: das Request-Objekt, 
den Template-Namen und ein Context-Dictionary. Der Context übergibt Daten an das Template.

[ER] Fügen Sie in `urls.py` eine URL-Route für die neue View hinzu:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_template, name='hello_template'),
]
```

[ER] Starten Sie den Entwicklungsserver und besuchen Sie `http://127.0.0.1:8000/hello/`.
Dokumentieren Sie das Ergebnis.
<!-- time estimate: 30 min -->

### Template-Variablen und Datentypen

Templates können verschiedene Python-Datentypen verarbeiten:

#### Einfache Variablen verwenden

[ER] Erweitern Sie die `hello_template`-View um weitere Variablen:

```python
def hello_template(request):
    context = {
        'greeting': 'Hallo aus dem Template!',
        'username': 'Django-Nutzer',
        'current_year': 2024,
        'is_authenticated': True
    }
    return render(request, 'hello.html', context)
```

[ER] Modifizieren Sie `hello.html`, um alle Variablen anzuzeigen:

```html
<body>
    <h1>{{ greeting }}</h1>
    <p>Benutzer: {{ username }}</p>
    <p>Jahr: {{ current_year }}</p>
    <p>Angemeldet: {{ is_authenticated }}</p>
</body>
```

#### Listen in Templates verwenden

[ER] Erstellen Sie eine neue View `list_demo` mit einer Liste:

```python
def list_demo(request):
    context = {
        'fruits': ['Apfel', 'Banane', 'Orange', 'Traube'],
        'numbers': [1, 2, 3, 4, 5]
    }
    return render(request, 'list_demo.html', context)
```

[ER] Erstellen Sie `templates/list_demo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Listen Demo</title>
</head>
<body>
    <h2>Komplette Liste:</h2>
    <p>{{ fruits }}</p>
    
    <h2>Erstes Element:</h2>
    <p>{{ fruits.0 }}</p>
    
    <h2>Drittes Element:</h2>
    <p>{{ fruits.2 }}</p>
</body>
</html>
```

#### Dictionaries in Templates verarbeiten

[ER] Erstellen Sie eine View `dict_demo`:

```python
def dict_demo(request):
    context = {
        'person': {
            'name': 'Max Mustermann',
            'age': 30,
            'city': 'Berlin'
        }
    }
    return render(request, 'dict_demo.html', context)
```

[ER] Erstellen Sie `templates/dict_demo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dictionary Demo</title>
</head>
<body>
    <h2>Person-Informationen:</h2>
    <p>Komplettes Dictionary: {{ person }}</p>
    <p>Name: {{ person.name }}</p>
    <p>Alter: {{ person.age }}</p>
    <p>Stadt: {{ person.city }}</p>
</body>
</html>
```

[ER] Fügen Sie entsprechende URL-Routen für beide neuen Views hinzu.
<!-- time estimate: 25 min -->

### Template-Filter verwenden

Filter modifizieren Variablen vor der Ausgabe. Syntax: `{{ variable|filter:parameter }}`

Weitere Informationen zu Filtern:
[Django Template Filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#built-in-filter-reference)

[ER] Erstellen Sie eine View `filter_demo`:

```python
import datetime

def filter_demo(request):
    context = {
        'text': 'Django Template Filter',
        'long_text': 'Dies ist ein sehr langer Text, der gekürzt werden soll.',
        'number': 1024,
        'empty_value': '',
        'file_size': 2048576,
        'current_date': datetime.datetime.now()
    }
    return render(request, 'filter_demo.html', context)
```

[ER] Erstellen Sie `templates/filter_demo.html` mit verschiedenen Filtern:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Filter Demo</title>
</head>
<body>
    <h2>Text-Filter:</h2>
    <p>Original: {{ text }}</p>
    <p>Kleinbuchstaben: {{ text|lower }}</p>
    <p>Großbuchstaben: {{ text|upper }}</p>
    <p>Länge: {{ text|length }}</p>
    
    <h2>Truncate-Filter:</h2>
    <p>Gekürzt (10 Zeichen): {{ long_text|truncatechars:10 }}</p>
    
    <h2>Default-Filter:</h2>
    <p>Leerer Wert: {{ empty_value|default:"Kein Wert vorhanden" }}</p>
    
    <h2>Dateigröße-Filter:</h2>
    <p>Dateigröße: {{ file_size|filesizeformat }}</p>
    
    <h2>Datums-Filter:</h2>
    <p>Aktuelles Datum: {{ current_date|date:"d.m.Y" }}</p>
    <p>Mit Uhrzeit: {{ current_date|date:"d.m.Y H:i:s" }}</p>
</body>
</html>
```

[ER] Fügen Sie die URL-Route für die neue View hinzu und testen Sie die Filter-Ausgabe.
<!-- time estimate: 20 min -->

### Kontrollstrukturen: if/else-Tags

[ER] Erstellen Sie eine View `control_demo`:

```python
def control_demo(request):
    context = {
        'score': 85,
        'is_logged_in': True,
        'user_role': 'admin',
        'items': ['Item 1', 'Item 2', 'Item 3'],
        'empty_list': []
    }
    return render(request, 'control_demo.html', context)
```

[ER] Erstellen Sie `templates/control_demo.html` mit if/else-Logik:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Kontrollstrukturen Demo</title>
</head>
<body>
    <h2>If/Else-Beispiele:</h2>
    
    {% if score >= 90 %}
        <p>Ausgezeichnet! ({{ score }} Punkte)</p>
    {% elif score >= 70 %}
        <p>Gut gemacht! ({{ score }} Punkte)</p>
    {% else %}
        <p>Mehr Übung nötig. ({{ score }} Punkte)</p>
    {% endif %}
    
    <h2>Logische Operatoren:</h2>
    {% if is_logged_in and user_role == 'admin' %}
        <p>Willkommen, Administrator!</p>
    {% elif is_logged_in %}
        <p>Willkommen, Benutzer!</p>
    {% else %}
        <p>Bitte melden Sie sich an.</p>
    {% endif %}
    
    <h2>Listen-Check:</h2>
    {% if items %}
        <p>Es gibt {{ items|length }} Elemente in der Liste.</p>
    {% else %}
        <p>Die Liste ist leer.</p>
    {% endif %}
</body>
</html>
```

### Schleifen: for-Tag verwenden

[ER] Erweitern Sie `control_demo.html` um for-Schleifen:

```html
<h2>For-Schleifen:</h2>

<h3>Einfache Liste:</h3>
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

<h3>Mit Schleifenvariablen:</h3>
<ol>
{% for item in items %}
    <li>
        Element {{ forloop.counter }}: {{ item }}
        {% if forloop.first %} (Erstes Element){% endif %}
        {% if forloop.last %} (Letztes Element){% endif %}
    </li>
{% endfor %}
</ol>

<h3>Leere Liste behandeln:</h3>
{% for item in empty_list %}
    <p>{{ item }}</p>
{% empty %}
    <p>Keine Elemente vorhanden.</p>
{% endfor %}
```

[ER] Erweitern Sie die `control_demo`-View um Dictionary-Iteration:

```python
def control_demo(request):
    context = {
        'score': 85,
        'is_logged_in': True,
        'user_role': 'admin',
        'items': ['Item 1', 'Item 2', 'Item 3'],
        'empty_list': [],
        'person_data': {
            'name': 'Anna Schmidt',
            'email': 'anna@example.com',
            'phone': '0123-456789'
        }
    }
    return render(request, 'control_demo.html', context)
```

[ER] Fügen Sie Dictionary-Iteration zu `control_demo.html` hinzu:

```html
<h3>Dictionary durchlaufen:</h3>
<dl>
{% for key, value in person_data.items %}
    <dt>{{ key }}</dt>
    <dd>{{ value }}</dd>
{% endfor %}
</dl>
```
<!-- time estimate: 25 min -->

### Safe-Filter und HTML-Ausgabe

[NOTICE]
Der `safe`-Filter sollte nur bei vertrauenswürdigen Daten verwendet werden,
da er die automatische HTML-Escape-Funktion von Django umgeht.
[ENDNOTICE]

[ER] Erstellen Sie eine View `safe_demo`:

```python
def safe_demo(request):
    context = {
        'html_content': '<strong>Fetter Text</strong> und <em>kursiver Text</em>',
        'link_html': '<a href="https://www.djangoproject.com">Django Website</a>'
    }
    return render(request, 'safe_demo.html', context)
```

[ER] Erstellen Sie `templates/safe_demo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Safe Filter Demo</title>
</head>
<body>
    <h2>HTML-Ausgabe Vergleich:</h2>
    
    <h3>Ohne safe-Filter (escaped):</h3>
    <p>{{ html_content }}</p>
    
    <h3>Mit safe-Filter (unescaped):</h3>
    <p>{{ html_content|safe }}</p>
    
    <h3>Link-Beispiel:</h3>
    <p>Escaped: {{ link_html }}</p>
    <p>Safe: {{ link_html|safe }}</p>
</body>
</html>
```

### Template-Kommentare verwenden

[ER] Erstellen Sie ein Template `templates/comments_demo.html`, das verschiedene Kommentar-Arten zeigt:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Kommentare Demo</title>
</head>
<body>
    <h2>Kommentare in Templates:</h2>
    
    <p>Hier ist ein normaler Text.</p>
    
    {# Dies ist ein Kommentar, der nicht gerendert wird #}
    
    <p>Dieser Text wird angezeigt.</p>
    
    {# 
    Mehrzeiliger Kommentar
    wird ebenfalls ignoriert
    #}
    
    <p>Ende der Kommentare-Demo.</p>
</body>
</html>
```

[ER] Erstellen Sie eine entsprechende View `comments_demo` und fügen Sie alle neuen URL-Routen 
zu `urls.py` hinzu. Testen Sie alle Views.
<!-- time estimate: 15 min -->

### Include-Tag für Template-Fragmente

[ER] Erstellen Sie ein Template-Fragment `templates/navigation.html`:

```html
<nav>
    <ul>
        <li><a href="/hello/">Home</a></li>
        <li><a href="/list/">Listen</a></li>
        <li><a href="/control/">Kontrolle</a></li>
    </ul>
</nav>
```

[ER] Erweitern Sie eines Ihrer bestehenden Templates um das Include-Tag:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Include Demo</title>
</head>
<body>
    {% include "navigation.html" %}
    
    <h1>Hauptinhalt der Seite</h1>
    <p>Hier ist der eigentliche Inhalt...</p>
</body>
</html>
```

[ER] Testen Sie die Include-Funktionalität und dokumentieren Sie das Ergebnis.
<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]