title: Django URL-Routing und Pfadkonfiguration
stage: draft
timevalue: 2.5
difficulty: 2
assumes: django-project
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des URL-Routings in Django und kann Pfad-zu-View-Zuordnungen konfigurieren.
- Ich kann reguläre Ausdrücke in Django-URLs verwenden, sowohl mit benannten als auch unbenannten Gruppen.
- Ich kann URL-Konfigurationen mithilfe von `include()` auf verschiedene Apps verteilen.
- Ich verstehe das Konzept der Reverse Resolution und kann URL-Namen in Views und Templates verwenden.
- Ich kann Namespaces für URL-Konfigurationen einrichten und verwenden.

[ENDSECTION]

[SECTION::background::default]

Django-Routing ist das System, das eingehende URL-Anfragen mit den entsprechenden View-Funktionen verknüpft. 
Es ermöglicht Entwicklern, saubere und strukturierte URLs zu erstellen, die sowohl benutzerfreundlich als auch 
wartbar sind. In komplexeren Projekten mit mehreren Apps wird eine durchdachte URL-Struktur besonders wichtig 
für die Codeorganisation und -wartung.

[ENDSECTION]

[SECTION::instructions::detailed]

### Voraussetzungen und Projektsetup

Bitte lesen Sie zunächst [PARTREF::django-project] und folgen Sie den dort beschriebenen 
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

### Grundlagen des Django URL-Routings

Das Django URL-System arbeitet mit Mustern (Patterns), die eingehende URLs mit View-Funktionen verbinden.
Das Routing wird hauptsächlich in `urls.py`-Dateien konfiguriert, wobei jedes Muster aus einer URL 
und einer zugehörigen View-Funktion besteht.

**Grundstruktur einer URL-Konfiguration:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('route/', views.view_function, name='url_name'),
]
```

**Weitere Informationen zum URL-System:**
[Django URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/)

[EQ] Erklären Sie in eigenen Worten: Was ist URL-Routing und warum ist es in Webentwicklung wichtig?
<!-- EQ1 -->

### URL-Patterns mit Parametern: Reguläre Ausdrücke

Django bietet verschiedene Möglichkeiten, Parameter aus URLs zu extrahieren und an View-Funktionen weiterzugeben.

**Einfache Parameter mit `path()`:**
```python
path('artikel/<int:id>/', views.artikel_detail, name='artikel')
path('benutzer/<str:username>/', views.profil, name='profil')
```

**Reguläre Ausdrücke mit `re_path()`:**
```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^artikel/([0-9]{4})/$', views.artikel_jahr),
]
```

[ER] Erstellen Sie eine neue Django-App namens `blog` in Ihrem Projekt:
```bash
python manage.py startapp blog
```
<!-- ER1 -->

[ER] Erstellen Sie in `blog/views.py` folgende View-Funktionen:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Blog Hauptseite")

def artikel_detail(request, artikel_id):
    return HttpResponse(f"Artikel Details für ID: {artikel_id}")

def kategorie(request, kategorie_name):
    return HttpResponse(f"Artikel in Kategorie: {kategorie_name}")
```
<!-- ER2 -->

### Unbenannte Gruppen in regulären Ausdrücken

Unbenannte Gruppen werden durch runde Klammern `()` definiert und die erfassten Werte werden in der 
Reihenfolge ihres Auftretens als Positionsargumente an die View-Funktion übergeben.

**Syntax für unbenannte Gruppen:**
```python
re_path(r'^artikel/([0-9]{4})/$', views.artikel_jahr)
```

Die View-Funktion muss entsprechende Parameter akzeptieren:
```python
def artikel_jahr(request, jahr):
    return HttpResponse(f"Artikel aus dem Jahr: {jahr}")
```

[ER] Erweitern Sie `blog/views.py` um eine View-Funktion für unbenannte Gruppen:

```python
def artikel_datum(request, jahr, monat):
    return HttpResponse(f"Artikel aus {monat}/{jahr}")
```
<!-- ER3 -->

[ER] Erstellen Sie `blog/urls.py` und konfigurieren Sie URL-Patterns mit unbenannten Gruppen:

```python
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum),
]
```
<!-- ER4 -->

### Benannte Gruppen in regulären Ausdrücken

Benannte Gruppen verwenden die Syntax `(?P<gruppenname>muster)` und übergeben die erfassten Werte 
als Schlüsselwortargumente an die View-Funktion.

**Syntax für benannte Gruppen:**
```python
re_path(r'^artikel/(?P<jahr>[0-9]{4})/(?P<monat>[0-9]{2})/$', views.artikel_datum)
```

Die View-Funktion erhält benannte Parameter:
```python
def artikel_datum(request, jahr, monat):
    return HttpResponse(f"Artikel aus {monat}/{jahr}")
```

Wenn noch Fragen offen sind, hilft diese Ressource weiter:
[URL patterns mit regulären Ausdrücken](https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path)

[ER] Erweitern Sie `blog/urls.py` um URL-Patterns mit benannten Gruppen:

```python
urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum),
    re_path(r'^artikel/(?P<artikel_id>[0-9]+)/$', views.artikel_detail),
    re_path(r'^kategorie/(?P<kategorie_name>[a-zA-Z]+)/$', views.kategorie),
]
```
<!-- ER5 -->

[EQ] Was ist der Unterschied zwischen benannten und unbenannten Gruppen in Django URL-Patterns? 
Welche Vor- und Nachteile haben sie jeweils?
<!-- EQ2 -->

### URL-Konfiguration aufteilen: `include()`

Bei größeren Projekten mit mehreren Apps wird es unübersichtlich, alle URLs in der Haupt-`urls.py` 
zu verwalten. Django bietet `include()`, um URL-Konfigurationen auf verschiedene Apps zu verteilen.

**Problem:** Alle URLs in einer Datei führen zu:
- Unübersichtlichkeit
- Namenskonflikten
- Schwieriger Wartung

**Lösung:** URL-Verteilung mit `include()`

[ER] Modifizieren Sie die Haupt-`urls.py` (`meinprojekt/urls.py`):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```
<!-- ER6 -->

[EC] Testen Sie die URL-Struktur, indem Sie verschiedene URLs aufrufen:
```bash
curl http://127.0.0.1:8000/blog/
```
<!-- EC1 -->

[ER] Erstellen Sie eine zweite App namens `portfolio` und implementieren Sie ähnliche URL-Patterns:
<!-- ER7 -->

```python
# portfolio/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Portfolio Hauptseite")

def projekt(request, projekt_id):
    return HttpResponse(f"Projekt ID: {projekt_id}")
```

```python
# portfolio/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio_index'),
    re_path(r'^projekt/(?P<projekt_id>[0-9]+)/$', views.projekt),
]
```

[ER] Erweitern Sie die Haupt-`urls.py` um die Portfolio-App:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
]
```
<!-- ER8 -->

### Reverse Resolution: URL-Namen verwenden

Reverse Resolution ermöglicht es, URLs dynamisch anhand ihrer Namen zu generieren, anstatt 
Pfade fest zu codieren. Dies macht Anwendungen wartbarer und flexibler.

**In Views:**
```python
from django.urls import reverse
from django.shortcuts import redirect

def meine_view(request):
    url = reverse('blog_index')
    return redirect(url)
```

**In Templates:**
```html
<a href="{% url 'blog_index' %}">Zum Blog</a>
<a href="{% url 'artikel_detail' artikel_id=123 %}">Artikel lesen</a>
```

Zur Vertiefung: Weitere Erklärungen finden Sie hier:
[URL names und reverse resolution](https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls)

[ER] Erweitern Sie `blog/views.py` um eine View mit Reverse Resolution:

```python
from django.urls import reverse
from django.shortcuts import redirect

def weiterleitung(request):
    # Weiterleitung zur Hauptseite
    return redirect(reverse('blog_index'))
```
<!-- ER9 -->

[ER] Aktualisieren Sie `blog/urls.py` um die neue View und stellen Sie sicher, 
dass alle URLs benannte Patterns haben:

```python
urlpatterns = [
    path('', views.index, name='blog_index'),
    path('weiterleitung/', views.weiterleitung, name='blog_redirect'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum, name='artikel_datum'),
    re_path(r'^artikel/(?P<artikel_id>[0-9]+)/$', views.artikel_detail, name='artikel_detail'),
    re_path(r'^kategorie/(?P<kategorie_name>[a-zA-Z]+)/$', views.kategorie, name='kategorie'),
]
```
<!-- ER10 -->

[EQ] Testen Sie `http://127.0.0.1:8000/blog/weiterleitung/` im Browser. 
Beschreiben Sie, was passiert und warum dies nützlich für die Webentwicklung ist.
<!-- EQ3 -->

### Namespaces: URL-Namen organisieren

Namespaces verhindern Namenskonflikte zwischen verschiedenen Apps, die ähnliche URL-Namen verwenden.

**Problem:** Zwei Apps mit demselben URL-Namen `'index'` führen zu Konflikten.

**Lösung:** Namespaces definieren

[ER] Fügen Sie Namespaces zu Ihren App-URLs hinzu. 

Aktualisieren Sie `blog/urls.py`:
```python
from django.urls import path, re_path
from . import views

app_name = 'blog'  # Namespace definieren

urlpatterns = [
    path('', views.index, name='index'),
    path('weiterleitung/', views.weiterleitung, name='redirect'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum, name='artikel_datum'),
    re_path(r'^artikel/(?P<artikel_id>[0-9]+)/$', views.artikel_detail, name='artikel_detail'),
    re_path(r'^kategorie/(?P<kategorie_name>[a-zA-Z]+)/$', views.kategorie, name='kategorie'),
]
```
<!-- ER11 -->

[ER] Aktualisieren Sie `portfolio/urls.py` entsprechend:
```python
from django.urls import path, re_path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^projekt/(?P<projekt_id>[0-9]+)/$', views.projekt, name='projekt'),
]
```
<!-- ER12 -->

[ER] Modifizieren Sie `blog/views.py`, um Namespaces in Reverse Resolution zu verwenden:

```python
def weiterleitung(request):
    return redirect(reverse('blog:index'))  # Namespace verwenden
```
<!-- ER13 -->

**Verwendung von Namespaces:**
- In Views: `reverse('blog:index')`
- In Templates: `{% url 'blog:index' %}`
- Mit Parametern: `reverse('blog:artikel_detail', kwargs={'artikel_id': 123})`

[EQ] Erklären Sie, warum Namespaces in größeren Django-Projekten wichtig sind. 
Geben Sie ein konkretes Beispiel für einen möglichen Namenskonflikt an.
<!-- EQ4 -->

### Integration und Testing

[ER] Erstellen Sie eine einfache HTML-Vorlage, um die Navigation zwischen den Apps zu testen:

Erstellen Sie `meinprojekt/templates/base.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Routing Demo</title>
    <meta charset="utf-8">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{% url 'blog:index' %}">Blog</a></li>
            <li><a href="{% url 'portfolio:index' %}">Portfolio</a></li>
            <li><a href="{% url 'blog:artikel_detail' artikel_id=1 %}">Beispiel Artikel</a></li>
            <li><a href="{% url 'portfolio:projekt' projekt_id=1 %}">Beispiel Projekt</a></li>
        </ul>
    </nav>
    <main>
        {{ content }}
    </main>
</body>
</html>
```
<!-- ER14 -->

[ER] Aktualisieren Sie `settings.py`, um das Templates-Verzeichnis hinzuzufügen:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diese Zeile hinzufügen
        'APP_DIRS': True,
        'OPTIONS': {
            # ...
        },
    },
]
```
<!-- ER15 -->

[EC] Testen Sie alle implementierten URLs systematisch mit curl oder dem Browser:
```bash
curl http://127.0.0.1:8000/blog/artikel/2024/03/
```
<!-- EC2 -->

[EQ] Welche URL-Pattern würde am besten zu folgenden Anforderungen passen:
- Benutzerprofile abrufen: `/benutzer/max_mustermann/`
- Artikel mit Datum filtern: `/blog/2024/03/15/`
- API-Endpunkt für Produktdetails: `/api/produkte/12345/`

Geben Sie für jeden Fall das passende Django URL-Pattern an.
<!-- EQ5 -->

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-routing.md]

### Kommandoprotokoll
[PROT::ALT:django-routing.prot]

[ENDINSTRUCTOR]
