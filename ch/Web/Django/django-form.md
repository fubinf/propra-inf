title: Django Formularbehandlung
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: django-basics, django-project, django-admin, django-template, http-GET, http-POST
---

[SECTION::goal::idea,experience]

- Ich verstehe den Unterschied zwischen GET- und POST-Methoden in HTTP-Formularen.
- Ich kann HTML-Formulare erstellen und in Django-Views verarbeiten.
- Ich verstehe die Funktionsweise von CSRF-Token und deren Verwendung in Django.
- Ich kenne die wichtigsten Eigenschaften des HttpRequest-Objekts.
- Ich kann Formulardaten in Django empfangen, verarbeiten und zurückgeben.

[ENDSECTION]

[SECTION::background::default]

HTML-Formulare sind die klassische Methode für die Interaktivität von Websites.
Sie ermöglichen es Benutzern, Daten an den Server zu senden, die dann verarbeitet werden können.
Django bietet umfangreiche Unterstützung für die Verarbeitung von Formulardaten
sowohl über GET- als auch POST-Methoden.
In dieser Aufgabe lernen wir, wie man Formulare erstellt und deren Daten sicher verarbeitet.

[ENDSECTION]

[SECTION::instructions::detailed]

### Projekt vorbereiten

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

### HTTP-Formulare verstehen

HTTP-Protokoll arbeitet mit einem "Request-Response"-Muster.
Der Client sendet eine Anfrage mit angehängten Daten, der Server analysiert diese
und stellt basierend auf der URL spezifische Dienste bereit.

Es gibt zwei Hauptmethoden für das Senden von Formulardaten:

- **GET-Methode**: Daten werden in der URL übertragen (sichtbar und begrenzt)
- **POST-Methode**: Daten werden im Request-Body übertragen (unsichtbar und unbegrenzt)

Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[HTTP-Methoden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

### GET-Methode implementieren

[ER] Erstellen Sie die Datei `meinprojekt/meinprojekt/search.py`:

```python
from django.http import HttpResponse
from django.shortcuts import render

# Formular anzeigen
def search_form(request):
    return render(request, 'search_form.html')
 
# Anfrage verarbeiten
def search(request):  
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'Sie haben gesucht nach: ' + request.GET['q']
    else:
        message = 'Sie haben ein leeres Formular abgeschickt'
    return HttpResponse(message)
```
<!-- ER1 -->

[ER] Erstellen Sie das Verzeichnis `templates` im Projekthauptverzeichnis und 
die Datei `meinprojekt/templates/search_form.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Django Suchformular</title>
</head>
<body>
    <h1>Suchformular (GET-Methode)</h1>
    <form action="/search/" method="get">
        <label for="searchfield">Suchbegriff:</label>
        <input type="text" name="q" id="searchfield" placeholder="Geben Sie einen Suchbegriff ein">
        <input type="submit" value="Suchen">
    </form>
</body>
</html>
```
<!-- ER2 -->

[ER] Aktualisieren Sie `meinprojekt/meinprojekt/urls.py`:

```python
from django.urls import path
from . import search

urlpatterns = [
    path('search-form/', search.search_form, name='search_form'),
    path('search/', search.search, name='search'),
]
```
<!-- ER3 -->

[EQ] Starten Sie die Django-Server und testen Sie die Anwendung unter `http://127.0.0.1:8000/search-form/`.
Geben Sie verschiedene Suchbegriffe ein und beobachten Sie die URL.
Was passiert bei einem leeren Formular?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ1 -->

<!-- time estimate: 20 min -->

### POST-Methode implementieren

POST-Methoden sind sicherer für sensible Daten und werden häufiger verwendet.
Wir erweitern das System um eine POST-Variante:

[ER] Erstellen Sie `meinprojekt/templates/post_form.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Django POST-Formular</title>
</head>
<body>
    <h1>Suchformular (POST-Methode)</h1>
    <form action="/search-post/" method="post">
        {% csrf_token %}
        <label for="postfield">Suchbegriff:</label>
        <input type="text" name="q" id="postfield" placeholder="Geben Sie einen Suchbegriff ein">
        <input type="submit" value="Suchen">
    </form>
    
    {% if result %}
        <div style="margin-top: 20px; padding: 10px; background-color: #f0f0f0;">
            <h2>Ergebnis:</h2>
            <p>{{ result }}</p>
        </div>
    {% endif %}
</body>
</html>
```
<!-- ER4 -->

[ER] Erstellen Sie `meinprojekt/meinprojekt/search_post.py`:

```python
from django.shortcuts import render

def search_post(request):
    context = {}
    if request.method == 'POST':
        if 'q' in request.POST and request.POST['q']:
            context['result'] = 'Sie haben gesucht nach: ' + request.POST['q']
        else:
            context['result'] = 'Sie haben ein leeres Formular abgeschickt'
    return render(request, 'post_form.html', context)
```
<!-- ER5 -->

[ER] Erweitern Sie `meinprojekt/meinprojekt/urls.py`:

```python
from django.urls import path
from . import search, search_post

urlpatterns = [
    path('search-form/', search.search_form, name='search_form'),
    path('search/', search.search, name='search'),
    path('search-post/', search_post.search_post, name='search_post'),
]
```
<!-- ER6 -->

[EQ] Testen Sie die POST-Anwendung unter `http://127.0.0.1:8000/search-post/`.
Geben Sie verschiedene Suchbegriffe ein und beobachten Sie die Ausgabe.
Was ist der Unterschied zur GET-Methode bezüglich der URL?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ2 -->
<!-- time estimate: 10 min -->


### HttpRequest-Objekt verstehen

Jede View-Funktion erhält ein HttpRequest-Objekt als ersten Parameter.
Dieses Objekt enthält wichtige Informationen über die HTTP-Anfrage:

[ER] Erstellen Sie `meinprojekt/meinprojekt/request_info.py`:

```python
from django.http import HttpResponse

def request_info(request):
    info = f"""
    <html>
    <head>
        <title>Request-Informationen</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>HttpRequest-Objekt Informationen</h1>
        <h2>Grundlegende Eigenschaften:</h2>
        <ul>
            <li><strong>Method:</strong> {request.method}</li>
            <li><strong>Path:</strong> {request.path}</li>
            <li><strong>User:</strong> {request.user}</li>
        </ul>
        
        <h2>GET-Parameter:</h2>
        <p>{dict(request.GET)}</p>
        
        <h2>POST-Parameter:</h2>
        <p>{dict(request.POST)}</p>
        
        <h2>META-Informationen (Auswahl):</h2>
        <ul>
            <li><strong>HTTP_USER_AGENT:</strong> {request.META.get('HTTP_USER_AGENT', 'N/A')}</li>
            <li><strong>REMOTE_ADDR:</strong> {request.META.get('REMOTE_ADDR', 'N/A')}</li>
            <li><strong>SERVER_NAME:</strong> {request.META.get('SERVER_NAME', 'N/A')}</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(info)
```
<!-- ER7 -->

[ER] Fügen Sie die neue Route zu `urls.py` hinzu:

```python
from django.urls import path
from . import search, search_post, request_info

urlpatterns = [
    path('search-form/', search.search_form, name='search_form'),
    path('search/', search.search, name='search'),
    path('search-post/', search_post.search_post, name='search_post'),
    path('request-info/', request_info.request_info, name='request_info'),
]
```
<!-- ER8 -->

[EQ] Analysieren Sie das HttpRequest-Objekt mit verschiedenen Aufrufen:
1. Rufen Sie `http://127.0.0.1:8000/request-info/` ohne Parameter auf
2. Rufen Sie `http://127.0.0.1:8000/request-info/?name=Max&alter=25` mit GET-Parametern auf
Analysieren Sie die angezeigten Eigenschaften: Was bedeuten request.method, request.path, request.GET?
Welche META-Informationen sehen Sie und was sagen HTTP_USER_AGENT und REMOTE_ADDR aus?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ3 -->

<!-- time estimate: 20 min -->

### Erweiterte Formularverarbeitung

[ER] Erstellen Sie ein komplexeres Formular `meinprojekt/templates/contact_form.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Kontaktformular</title>
</head>
<body>
    <h1>Kontaktformular</h1>
    <form action="/contact/" method="post">
        {% csrf_token %}
        
        <div style="margin-bottom: 10px;">
            <label for="name">Name:</label><br>
            <input type="text" name="name" id="name" required>
        </div>
        
        <div style="margin-bottom: 10px;">
            <label for="email">E-Mail:</label><br>
            <input type="email" name="email" id="email" required>
        </div>
        
        <div style="margin-bottom: 10px;">
            <label for="subject">Betreff:</label><br>
            <select name="subject" id="subject">
                <option value="allgemein">Allgemeine Anfrage</option>
                <option value="support">Support</option>
                <option value="feedback">Feedback</option>
            </select>
        </div>
        
        <div style="margin-bottom: 10px;">
            <label for="message">Nachricht:</label><br>
            <textarea name="message" id="message" rows="5" cols="50" required></textarea>
        </div>
        
        <input type="submit" value="Nachricht senden">
    </form>
    
    {% if submitted %}
        <div style="margin-top: 20px; padding: 10px; background-color: #d4edda; border: 1px solid #c3e6cb;">
            <h2>Nachricht erhalten!</h2>
            <p><strong>Name:</strong> {{ form_data.name }}</p>
            <p><strong>E-Mail:</strong> {{ form_data.email }}</p>
            <p><strong>Betreff:</strong> {{ form_data.subject }}</p>
            <p><strong>Nachricht:</strong> {{ form_data.message }}</p>
        </div>
    {% endif %}
</body>
</html>
```
<!-- ER9 -->

[ER] Erstellen Sie `meinprojekt/meinprojekt/contact.py`:

```python
from django.shortcuts import render

def contact(request):
    context = {}
    
    if request.method == 'POST':
        # Alle Formularfelder prüfen
        required_fields = ['name', 'email', 'subject', 'message']
        form_data = {}
        
        for field in required_fields:
            if field in request.POST and request.POST[field]:
                form_data[field] = request.POST[field]
            else:
                form_data[field] = ''
        
        # Prüfen ob alle Felder ausgefüllt sind
        if all(form_data.values()):
            context['submitted'] = True
            context['form_data'] = form_data
        else:
            context['error'] = 'Bitte füllen Sie alle Felder aus.'
    
    return render(request, 'contact_form.html', context)
```
<!-- ER10 -->

[ER] Fügen Sie die Route zu `urls.py` hinzu und testen Sie das Kontaktformular:

```python
from django.urls import path
from . import search, search_post, request_info, contact

urlpatterns = [
    path('search-form/', search.search_form, name='search_form'),
    path('search/', search.search, name='search'),
    path('search-post/', search_post.search_post, name='search_post'),
    path('request-info/', request_info.request_info, name='request_info'),
    path('contact/', contact.contact, name='contact'),
]
```
<!-- ER11 -->

[EQ] Testen Sie das Kontaktformular unter `http://127.0.0.1:8000/contact/`.
Füllen Sie alle Felder aus und senden Sie das Formular ab. Testen Sie dann unvollständige Eingaben.
Was passiert bei unvollständigen Formularen? Welche HTTP-Methode wird verwendet und warum?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ4 -->
<!-- time estimate: 15 min -->

### QueryDict-Objekte verstehen

Die Attribute `request.GET` und `request.POST` sind spezielle QueryDict-Objekte:

[ER] Erstellen Sie `meinprojekt/meinprojekt/querydict_demo.py`:

```python
from django.shortcuts import render

def querydict_demo(request):
    context = {}
    
    if request.method == 'POST':
        context['post_data'] = dict(request.POST)
        context['test_value'] = request.POST.get('test')
        context['option_get'] = request.POST.get('option')
        context['option_getlist'] = request.POST.getlist('option')
        context['post_items'] = list(request.POST.items())
        context['show_results'] = True
    
    context['get_data'] = dict(request.GET)
    
    return render(request, 'querydict_demo.html', context)
```

[ER] Erstellen Sie die Template-Datei `meinprojekt/templates/querydict_demo.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>QueryDict Demo</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>QueryDict-Objekt Demonstration</h1>
    
    <h2>Test-Formular</h2>
    <form method="post">
        {% csrf_token %}
        <div style="margin-bottom: 10px;">
            <label for="test">Texteingabe:</label>
            <input type="text" name="test" id="test" placeholder="Testwert" value="beispiel">
        </div>
        <div style="margin-bottom: 10px;">
            <label>Optionen wählen:</label><br>
            <input type="checkbox" name="option" value="1" id="opt1"> 
            <label for="opt1">Option 1</label><br>
            <input type="checkbox" name="option" value="2" id="opt2"> 
            <label for="opt2">Option 2</label><br>
        </div>
        <input type="submit" value="Formular testen">
    </form>
    
    <h2>QueryDict-Eigenschaften:</h2>
    
    {% if show_results %}
        <h3>POST-Daten:</h3>
        <ul>
            <li><strong>request.POST:</strong> {{ post_data }}</li>
            <li><strong>request.POST.get('test'):</strong> {{ test_value }}</li>
        </ul>
        
        <h3>QueryDict-Methoden Vergleich:</h3>
        <ul>
            <li><strong>request.POST.get('option'):</strong> {{ option_get }}</li>
            <li><strong>request.POST.getlist('option'):</strong> {{ option_getlist }}</li>
        </ul>
        
        <h3>Weitere QueryDict-Eigenschaften:</h3>
        <ul>
            <li><strong>request.POST.items():</strong> {{ post_items }}</li>
        </ul>
    {% else %}
        <p><em>Senden Sie das Formular ab, um die QueryDict-Eigenschaften zu sehen.</em></p>
    {% endif %}
    
    <h3>GET-Daten (falls vorhanden):</h3>
    <ul>
        <li><strong>request.GET:</strong> {{ get_data }}</li>
    </ul>
</body>
</html>
```
<!-- ER12 -->

[ER] Fügen Sie die QueryDict-Demo Route zu `urls.py` hinzu:

```python
from django.urls import path
from . import search, search_post, request_info, contact, querydict_demo

urlpatterns = [
    path('search-form/', search.search_form, name='search_form'),
    path('search/', search.search, name='search'),
    path('search-post/', search_post.search_post, name='search_post'),
    path('request-info/', request_info.request_info, name='request_info'),
    path('contact/', contact.contact, name='contact'),
    path('querydict-demo/', querydict_demo.querydict_demo, name='querydict_demo'),
]
```
<!-- ER13 -->

[EQ] Testen Sie die QueryDict-Demo unter `http://127.0.0.1:8000/querydict-demo/`:
1. Ersten Test: Wählen Sie **nur Option 1** und senden Sie das Formular
2. Zweiten Test: Wählen Sie **beide Optionen (Option 1 und Option 2)** und senden Sie das Formular  
3. Vergleichen Sie in der Ausgabe: `request.POST.get('option')` vs. `request.POST.getlist('option')`
Was ist der Unterschied zwischen `.get()` und `.getlist()` bei mehreren Werten?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ5 -->

<!-- time estimate: 25 min -->

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-form.md]

[ENDINSTRUCTOR]
