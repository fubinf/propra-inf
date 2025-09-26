title: Django Views
stage: alpha
timevalue: 2
difficulty: 2
assumes: django-basics
---

[SECTION::goal::idea,experience]

- Ich verstehe die Funktionsweise von Django-Views und deren Rolle im MVT-Pattern.
- Ich kann Request-Objekte analysieren und deren wichtigste Attribute nutzen.
- Ich beherrsche verschiedene Arten von Response-Objekten (HttpResponse, render, redirect).
- Ich kann einfache View-Funktionen erstellen und HTTP-Parameter verarbeiten.

[ENDSECTION]

[SECTION::background::default]

In Django sind Views das Bindeglied zwischen den eingehenden HTTP-Requests und den 
ausgehenden HTTP-Responses. Jede View-Funktion empfängt ein Request-Objekt mit allen 
Informationen der HTTP-Anfrage und muss ein Response-Objekt zurückgeben. 
Das Verständnis dieser fundamentalen Konzepte ist essentiell für die Django-Entwicklung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Projektvorbereitung

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

### Views und das Request-Objekt verstehen

Eine View-Funktion ist das Herzstück der Django-Anwendung. Sie nimmt ein Request-Objekt 
entgegen und gibt ein Response-Objekt zurück:

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello World!")
```

Das Request-Objekt enthält alle Informationen über die HTTP-Anfrage. 
Die wichtigsten Attribute sind:

Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[Django Request Objects](https://docs.djangoproject.com/en/stable/ref/request-response/)

<!-- time estimate: 10 min -->

### Request-Attribute: GET-Parameter verarbeiten

Das `request.GET` Attribut ist ein QueryDict-Objekt, das alle GET-Parameter der URL enthält:

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` eine View-Funktion:

```python
from django.http import HttpResponse

def get_params(request):
    name = request.GET.get("name", "Unbekannt")
    age = request.GET.get("age", "Nicht angegeben")
    return HttpResponse(f"Name: {name}, Alter: {age}")
```
<!-- ER1 -->

[ER] Fügen Sie die entsprechende URL-Route in `urls.py` hinzu:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('params/', views.get_params, name='get_params'),
]
```
<!-- ER2 -->

[EQ] Testen Sie die URL mit verschiedenen GET-Parametern. Was passiert, wenn Sie 
`http://127.0.0.1:8000/params/?name=Anna&age=25` aufrufen? 
Was geschieht bei `http://127.0.0.1:8000/params/` ohne Parameter?
Wenn Sie Port 8080 verwenden, ändern Sie den Link entsprechend.
<!-- EQ1 -->

<!-- time estimate: 10 min -->

### Request-Attribute: POST-Daten verarbeiten

POST-Daten werden über `request.POST` abgerufen. Diese sind typischerweise bei 
Formular-Übertragungen relevant:

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` eine View-Funktion für POST-Requests:

```python
def post_data(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'Kein Name')
        message = request.POST.get('message', 'Keine Nachricht')
        return HttpResponse(f"Benutzer: {username}, Nachricht: {message}")
    else:
        return HttpResponse("Diese View erwartet POST-Daten")
```
<!-- ER3 -->

[ER] Fügen Sie in `meinprojekt/meinprojekt/urls.py` die URL-Route hinzu:

```python
path('post-data/', views.post_data, name='post_data'),
```
<!-- ER4 -->

[EQ] Testen Sie die POST-View unter `http://127.0.0.1:8000/post-data/` und vergleichen Sie mit der GET-Parameter-View aus [EREFQ::1]: 
Was ist der wesentliche Unterschied 
bezüglich der URL-Anzeige und Datenübertragung zwischen GET und POST?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ2 -->

<!-- time estimate: 15 min -->

### Weitere Request-Attribute erforschen

Django-Request-Objekte bieten weitere nützliche Attribute:

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` eine View-Funktion, die verschiedene Request-Attribute anzeigt:

```python
def request_info(request):
    info = f"""
    <h2>Request-Informationen</h2>
    <p><strong>HTTP-Methode:</strong> {request.method}</p>
    <p><strong>Pfad:</strong> {request.path}</p>
    <p><strong>Vollständige URL:</strong> {request.build_absolute_uri()}</p>
    <p><strong>Content-Type:</strong> {request.content_type}</p>
    <p><strong>User-Agent:</strong> {request.META.get('HTTP_USER_AGENT', 'Unbekannt')}</p>
    """
    return HttpResponse(info)
```
<!-- ER5 -->

[ER] Fügen Sie in `meinprojekt/meinprojekt/urls.py` die entsprechende URL-Route hinzu:

```python
path('request-info/', views.request_info, name='request_info'),
```
<!-- ER6 -->

[EQ] Testen Sie die Request-Info-View unter `http://127.0.0.1:8000/request-info/`:
Rufen Sie die URL auf und notieren Sie die verschiedenen Request-Informationen.
Was verrät der User-Agent über Ihren Browser und welche HTTP-Methode wird verwendet?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ3 -->

<!-- time estimate: 15 min -->

### Response-Objekte: HttpResponse

Der einfachste Response-Typ ist `HttpResponse`, der direkt Text oder HTML zurückgibt:

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` eine View mit verschiedenen HttpResponse-Beispielen:

```python
def response_examples(request):
    response_type = request.GET.get('type', 'text')
    
    if response_type == 'html':
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>HTML Response</title></head>
        <body>
            <h1>HTML-Antwort</h1>
            <p>Dies ist eine <strong>HTML-Response</strong>.</p>
        </body>
        </html>
        """
        return HttpResponse(html_content)
    
    elif response_type == 'json':
        import json
        data = {'message': 'JSON-Antwort', 'status': 'success'}
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    else:
        return HttpResponse("Einfache Text-Antwort")
```
<!-- ER7 -->

[ER] Fügen Sie in `meinprojekt/meinprojekt/urls.py` die entsprechende URL-Route hinzu:

```python
path('responses/', views.response_examples, name='response_examples'),
```
<!-- ER8 -->

[EQ] Testen Sie verschiedene Response-Typen durch Aufrufen der folgenden URLs:
1. `http://127.0.0.1:8000/responses/` (Standard-Text-Response)
2. `http://127.0.0.1:8000/responses/?type=html` (HTML-Response)
3. `http://127.0.0.1:8000/responses/?type=json` (JSON-Response)

Was ist der Unterschied in der Browser-Darstellung zwischen diesen drei Response-Typen?
Wenn Sie Port 8080 verwenden, ändern Sie die Links bitte entsprechend.
<!-- EQ4 -->

<!-- time estimate: 15 min -->

### Response-Objekte: render() verwenden

`render()` ist eine Abkürzung für das Laden von Templates:

[ER] Erstellen Sie zunächst ein Template-Verzeichnis und eine HTML-Datei.
Erstellen Sie `meinprojekt/templates/welcome.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Willkommen</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Willkommen, {{ name }}!</h1>
    <p>Du bist {{ age }} Jahre alt.</p>
    <p>Aktuelle Zeit: {{ current_time }}</p>
</body>
</html>
```
<!-- ER9 -->

[ER] Aktualisieren Sie `meinprojekt/meinprojekt/settings.py`, um das Template-Verzeichnis zu registrieren:

Suchen Sie in der Datei die `TEMPLATES`-Konfiguration und ändern Sie die `'DIRS'`-Zeile:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diese Zeile ändern
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
<!-- ER10 -->

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` eine View-Funktion mit `render()`:

```python
from django.shortcuts import render
from datetime import datetime

def welcome_template(request):
    context = {
        'name': request.GET.get('name', 'Gast'),
        'age': request.GET.get('age', 'unbekannt'),
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'welcome.html', context)
```
<!-- ER11 -->

[ER] Fügen Sie in `meinprojekt/meinprojekt/urls.py` die entsprechende URL-Route hinzu:

```python
path('welcome/', views.welcome_template, name='welcome_template'),
```
<!-- ER12 -->

[EQ] Testen Sie die Template-View unter `http://127.0.0.1:8000/welcome/?name=Max&age=30`:
Rufen Sie die URL auf und beobachten Sie, wie die Template-Engine die Variablen verarbeitet.
Was ist der wesentliche Vorteil von `render()` gegenüber `HttpResponse()` bei der HTML-Ausgabe?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ5 -->

<!-- time estimate: 25 min -->

### Response-Objekte: redirect() für Weiterleitungen

`redirect()` wird verwendet, um Benutzer auf andere URLs umzuleiten:

[ER] Erstellen Sie in `meinprojekt/meinprojekt/views.py` Views für Umleitung und Zielseite:

```python
from django.shortcuts import redirect

def redirect_example(request):
    username = request.GET.get('user')
    if username:
        return redirect(f'/profile/?name={username}')
    else:
        return redirect('/profile/?name=Anonymer_Nutzer')

def profile_page(request):
    name = request.GET.get('name', 'Unbekannt')
    return HttpResponse(f"<h1>Profil von {name}</h1><p>Hier steht das Benutzerprofil.</p>")
```
<!-- ER13 -->

[ER] Fügen Sie in `meinprojekt/meinprojekt/urls.py` beide URL-Routen hinzu:

```python
path('redirect-test/', views.redirect_example, name='redirect_test'),
path('profile/', views.profile_page, name='profile'),
```
<!-- ER14 -->

[EQ] Testen Sie die Redirect-Funktionalität durch Aufrufen von `http://127.0.0.1:8000/redirect-test/?user=Anna`:
Beobachten Sie genau: Was passiert in Ihrem Browser und wie verändert sich die URL nach dem Aufrufen?
Welche HTTP-Statuscodes werden dabei verwendet?
Wenn Sie Port 8080 verwenden, ändern Sie den Link bitte entsprechend.
<!-- EQ6 -->

<!-- time estimate: 20 min -->

[EQ] Welche der drei Response-Typen (HttpResponse, render, redirect) würden Sie 
für folgende Szenarien verwenden:

- Anzeige einer Bestätigungsnachricht nach dem Speichern
- Darstellung einer komplexen HTML-Seite mit Benutzerdaten  
- Weiterleitung nach erfolgreicher Anmeldung
<!-- EQ7 -->

<!-- time estimate: 10 min -->

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-views.md]

[ENDINSTRUCTOR]
