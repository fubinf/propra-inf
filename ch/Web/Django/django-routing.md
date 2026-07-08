title: Django URL-Routing und Pfadkonfiguration
stage: draft
timevalue: 1.5
difficulty: 2
requires: django-template
assumes: http-GET, http-POST
---

[SECTION::goal::idea,experience]

- Ich verstehe das Konzept des URL-Routings und kann Pfad-zu-View-Zuordnungen mit `path()` sowie regulären Ausdrücken (`re_path()`, benannte und unbenannte Gruppen) konfigurieren.
- Ich kann URL-Konfigurationen mit `include()` auf mehrere Module verteilen und mittels Namespaces organisieren.
- Ich verstehe das Konzept der Reverse Resolution und kann URL-Namen in Views und Templates verwenden.

[ENDSECTION]

[SECTION::background::default]

Django-Routing ist das System, das eingehende URL-Anfragen mit den entsprechenden View-Funktionen verknüpft. 
Es ermöglicht Entwicklern, saubere und strukturierte URLs zu erstellen, die sowohl benutzerfreundlich als auch 
wartbar sind. In komplexeren Projekten mit mehreren Apps wird eine durchdachte URL-Struktur besonders wichtig 
für die Codeorganisation und -wartung.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in [PARTREF::django-basics] erstellt haben.
Alle folgenden Änderungen werden Sie in diesem Projekt durchführen.

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


[EQ] Erklären Sie in eigenen Worten: Was ist URL-Routing und warum ist es in Webentwicklung wichtig?
<!-- EQ1 -->
<!-- time estimate: 10 min -->

### URL-Parameter mit `path()` verwenden

Die `path()`-Funktion akzeptiert mehrere Parameter, die jeweils eine wichtige Rolle spielen:

**Syntax der `path()`-Funktion:**
```python
path(route, view, kwargs=None, name=None)
```

**Parameter:**

- `route` - Ein String, das URL-Muster definiert (z.B. `'artikel/<int:id>/'`)
- `view` - Die View-Funktion, die aufgerufen wird, wenn die URL passt
- `kwargs` - Ein Wörterbuch mit zusätzlichen Argumenten (optional)
- `name` - Ein eindeutiger Name für die URL, um sie später in Views/Templates zu referenzieren (optional)

**Einfache Parameter mit `path()`:**
```python
path('artikel/<int:id>/', views.artikel_detail, name='artikel')
path('benutzer/<str:username>/', views.profil, name='profil')
```

Die Syntax `<typ:name>` bedeutet:
- `typ` - Der Datentyp (z.B. `str`, `int`, `uuid`)
- `name` - Der Parametername, wird an die View-Funktion übergeben

[ER] Sie arbeiten weiter mit dem `meinprojekt`-Projekt aus [PARTREF::django-basics].
Erstellen Sie in `views.py` eine neue View-Funktion mit Parametern:

```python
def greet(request, name):
    return HttpResponse(f"Hallo {name}! Schön, dich kennenzulernen.")
```
<!-- ER1 -->

[ER] Aktualisieren Sie `urls.py` und fügen Sie ein URL-Pattern mit einem `<str:name>` Parameter hinzu:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),  # Das hello Pattern aus django-project
    path('greet/<str:name>/', views.greet, name='greet'),
]
```
<!-- ER2 -->

[EC] Testen Sie die neue Route im Browser:
- `http://127.0.0.1:8071/greet/Anna/`
- `http://127.0.0.1:8071/greet/Max/`

Wenn Sie einen anderen Port verwenden, passen Sie die Links entsprechend an.
<!-- EC1 -->

[EQ] Welche Datentypen können Sie in `<...>` verwenden und wie werden sie validiert?
<!-- EQ2 -->
<!-- time estimate: 15 min -->

### URL-Patterns mit Parametern: Reguläre Ausdrücke

Django bietet verschiedene Möglichkeiten, Parameter aus URLs zu extrahieren und an View-Funktionen weiterzugeben.

**Reguläre Ausdrücke mit `re_path()`:**
```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^artikel/([0-9]{4})/$', views.artikel_jahr),
]
```

Größere Projekte gliedern ihre Views und URLs oft in mehrere Module. Wir simulieren das hier,
indem wir für einen Blog-Bereich eigene Dateien `blog_views.py` und `blog_urls.py` anlegen
(die eigentliche App-Struktur mit `startapp` lernen Sie in [PARTREF::django-admin] kennen).

[ER] Erstellen Sie eine neue Datei `blog_views.py` mit folgenden View-Funktionen:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Blog Hauptseite")

def artikel_detail(request, artikel_id):
    return HttpResponse(f"Artikel Details für ID: {artikel_id}")

def kategorie(request, kategorie_name):
    return HttpResponse(f"Artikel in Kategorie: {kategorie_name}")
```
<!-- ER3 -->
<!-- time estimate: 10 min -->

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

[ER] Erweitern Sie `blog_views.py` um eine View-Funktion für unbenannte Gruppen:

```python
def artikel_datum(request, jahr, monat):
    return HttpResponse(f"Artikel aus {monat}/{jahr}")
```
<!-- ER4 -->

[ER] Erstellen Sie `blog_urls.py` und konfigurieren Sie URL-Patterns mit unbenannten Gruppen.
Da `blog_urls.py` neben `blog_views.py` in Ihrem Projektverzeichnis liegt (nicht in einer eigenen App),
importieren Sie das Modul unter einem Alias, um es von `urls.py` zu unterscheiden:

```python
from django.urls import path, re_path
from . import blog_views as views

urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum),
]
```
<!-- ER5 -->

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


[ER] Erweitern Sie `blog_urls.py` um URL-Patterns mit benannten Gruppen:

```python
urlpatterns = [
    path('', views.index, name='blog_index'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum),
    re_path(r'^artikel/(?P<artikel_id>[0-9]+)/$', views.artikel_detail),
    re_path(r'^kategorie/(?P<kategorie_name>[a-zA-Z]+)/$', views.kategorie),
]
```
<!-- ER6 -->

[EQ] Was ist der Unterschied zwischen benannten und unbenannten Gruppen in Django URL-Patterns? 
Welche Vor- und Nachteile haben sie jeweils?
<!-- EQ3 -->
<!-- time estimate: 20 min -->

### URL-Konfiguration aufteilen: `include()`

Bei größeren Projekten mit mehreren Bereichen wird es unübersichtlich, alle URLs in der Haupt-`urls.py` 
zu verwalten. Django bietet `include()`, um `urlpatterns`-Listen aus anderen Modulen einzubinden –
das funktioniert mit jedem Modul, das eine `urlpatterns`-Liste definiert, nicht nur mit Apps.

**Problem:** Alle URLs in einer Datei führen zu:
- Unübersichtlichkeit
- Namenskonflikten
- Schwieriger Wartung

**Lösung:** URL-Verteilung mit `include()`

[ER] Modifizieren Sie die Haupt-`urls.py`, um `blog_urls.py` einzubinden:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('meinprojekt.blog_urls')),
]
```
<!-- ER7 -->

[EC] Testen Sie die URL-Struktur, indem Sie verschiedene URLs aufrufen:
```bash
curl http://127.0.0.1:8071/blog/
```
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EC2 -->

[ER] Implementieren Sie analog zu `blog_views.py`/`blog_urls.py` einen zweiten Bereich
`portfolio_views.py`/`portfolio_urls.py`:
```python
# portfolio_views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Portfolio Hauptseite")

def projekt(request, projekt_id):
    return HttpResponse(f"Projekt ID: {projekt_id}")
```

```python
# portfolio_urls.py
from django.urls import path, re_path
from . import portfolio_views as views

urlpatterns = [
    path('', views.index, name='portfolio_index'),
    re_path(r'^projekt/(?P<projekt_id>[0-9]+)/$', views.projekt),
]
```
<!-- ER8 -->

[ER] Erweitern Sie die Haupt-`urls.py` um den Portfolio-Bereich:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('meinprojekt.blog_urls')),
    path('portfolio/', include('meinprojekt.portfolio_urls')),
]
```
<!-- ER9 -->

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


[ER] Erweitern Sie `blog_views.py` um eine View mit Reverse Resolution:

```python
from django.urls import reverse
from django.shortcuts import redirect

def weiterleitung(request):
    # Weiterleitung zur Hauptseite
    return redirect(reverse('blog_index'))
```
<!-- ER10 -->

[ER] Aktualisieren Sie `blog_urls.py` um die neue View und stellen Sie sicher, 
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
<!-- ER11 -->

[EQ] Testen Sie `http://127.0.0.1:8071/blog/weiterleitung/` im Browser. 
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
Beschreiben Sie, was passiert und warum dies nützlich für die Webentwicklung ist.
<!-- EQ4 -->
<!-- time estimate: 25 min -->

### Namespaces: URL-Namen organisieren

Namespaces verhindern Namenskonflikte zwischen verschiedenen URL-Modulen, die ähnliche URL-Namen verwenden.

**Problem:** Zwei Module mit demselben URL-Namen `'index'` führen zu Konflikten.

**Lösung:** Namespaces definieren

[ER] Fügen Sie Namespaces zu Ihren URL-Modulen hinzu. 

Aktualisieren Sie `blog_urls.py`:
```python
from django.urls import path, re_path
from . import blog_views as views

app_name = 'blog'  # Namespace definieren

urlpatterns = [
    path('', views.index, name='index'),
    path('weiterleitung/', views.weiterleitung, name='redirect'),
    re_path(r'^artikel/([0-9]{4})/([0-9]{2})/$', views.artikel_datum, name='artikel_datum'),
    re_path(r'^artikel/(?P<artikel_id>[0-9]+)/$', views.artikel_detail, name='artikel_detail'),
    re_path(r'^kategorie/(?P<kategorie_name>[a-zA-Z]+)/$', views.kategorie, name='kategorie'),
]
```
<!-- ER12 -->

[ER] Aktualisieren Sie `portfolio_urls.py` entsprechend:
```python
from django.urls import path, re_path
from . import portfolio_views as views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^projekt/(?P<projekt_id>[0-9]+)/$', views.projekt, name='projekt'),
]
```
<!-- ER13 -->

[ER] Modifizieren Sie `blog_views.py`, um Namespaces in Reverse Resolution zu verwenden:

```python
def weiterleitung(request):
    return redirect(reverse('blog:index'))  # Namespace verwenden
```
<!-- ER14 -->

**Verwendung von Namespaces:**
- In Views: `reverse('blog:index')`
- In Templates: `{% url 'blog:index' %}`
- Mit Parametern: `reverse('blog:artikel_detail', kwargs={'artikel_id': 123})`

[EQ] Testen Sie `http://127.0.0.1:8071/blog/weiterleitung/` im Browser nach der Namespace-Implementierung.
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
Erklären Sie, warum Namespaces in größeren Django-Projekten wichtig sind. 
Geben Sie ein konkretes Beispiel für einen möglichen Namenskonflikt an.
<!-- EQ5 -->
<!-- time estimate: 15 min -->

### Integration und Testing

[ER] Erstellen Sie eine einfache HTML-Vorlage, um die Navigation zwischen den Bereichen zu testen:

Erstellen Sie `templates/base.html`:
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
<!-- ER15 -->

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
<!-- ER16 -->

[EC] Testen Sie alle implementierten URLs systematisch mit curl oder dem Browser:
```bash
curl http://127.0.0.1:8071/blog/artikel/2024/03/
```
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EC3 -->

[EQ] Welche URL-Pattern würde am besten zu folgenden Anforderungen passen:
- Benutzerprofile abrufen: `/benutzer/max_mustermann/`
- Artikel mit Datum filtern: `/blog/2024/03/15/`
- API-Endpunkt für Produktdetails: `/api/produkte/12345/`

Geben Sie für jeden Fall das passende Django URL-Pattern an.
<!-- EQ6 -->
<!-- time estimate: 15 min -->

### Weiterführend

- [Django URL dispatcher](https://docs.djangoproject.com/en/4.2/topics/http/urls/) – Umfassende Dokumentation zum URL-Routing-System in Django
- [URL patterns mit regulären Ausdrücken](https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path) – Detaillierte Dokumentation zu re_path und regulären Ausdrücken
- [URL names und reverse resolution](https://docs.djangoproject.com/en/4.2/topics/http/urls/#reverse-resolution-of-urls) – Weitere Informationen zur Reverse Resolution von URLs

[ENDSECTION]

[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]
**Knackpunkte:**

- [EREFR::5]/[EREFR::7]: `blog_urls.py` importiert `blog_views` unter dem Alias `views` (nicht `from . import views`, das würde mit der Haupt-`views.py` kollidieren); Haupt-`urls.py` bindet es korrekt mit `include('meinprojekt.blog_urls')` ein.
- [EREFR::12]/[EREFR::13]: Beide URL-Module setzen `app_name`; [EREFR::14] verwendet `reverse('blog:index')` mit Namespace-Präfix statt des einfachen Namens.
- [EREFQ::5]: Student nennt ein konkretes Namenskonflikt-Beispiel (z.B. zwei Module mit `name='index'`) und erklärt, warum Namespaces es lösen.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-routing.md]

### Kommandoprotokoll
[PROT::ALT:django-routing.prot]

[ENDINSTRUCTOR]
