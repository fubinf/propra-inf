title: Django Views
stage: draft
timevalue: 2.25
difficulty: 2
requires: django-model
assumes: http-GET, http-POST, curl
---

[SECTION::goal::idea,experience]

- Ich verstehe die Funktionsweise von Django-Views und deren Zusammenspiel mit HTTP-Requests
  und -Responses.
- Ich kann Request-Daten aus verschiedenen Quellen (GET-Parameter, POST-Daten, URL-Pfad)
  verarbeiten und passende Response-Typen zurückgeben.
- Ich verstehe, warum benannte Routen und `reverse()` Code wartbarer machen als fest
  codierte URLs.

[ENDSECTION]

[SECTION::background::default]

In Django sind Views das Bindeglied zwischen den eingehenden HTTP-Requests und den
ausgehenden HTTP-Responses. Jede View-Funktion empfängt ein Request-Objekt mit allen
Informationen der HTTP-Anfrage und muss ein Response-Objekt zurückgeben. Das Verständnis
dieser fundamentalen Konzepte ist essentiell für die Django-Entwicklung.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`, die Sie in [PARTREF::django-project] angelegt und
in [PARTREF::django-model] um das `Student`-Model erweitert haben. Alle folgenden Änderungen
finden in `webapp` statt.

### Views und das Request-Objekt verstehen

Eine View-Funktion ist das Herzstück der Django-Anwendung. Sie nimmt ein Request-Objekt
entgegen und gibt ein Response-Objekt zurück:

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello World!")
```

[EQ] Schauen Sie sich die `hello`-View aus [PARTREF::django-project] an. Wie ist eine
View-Funktion aufgebaut? Welche zwei Bestandteile sind zwingend notwendig?
<!-- EQ1 -->
<!-- time estimate: 10 min -->

### Request-Attribute: GET-Parameter verarbeiten

Das `request.GET`-Attribut ist ein QueryDict-Objekt, das alle GET-Parameter der URL enthält:

[ER] Erstellen Sie in `views.py` eine View-Funktion:

[SNIPPET::ALT::django_views_get_params]
<!-- ER1 -->

[ER] Ergänzen Sie `urls.py` um die neue Route:

[SNIPPET::ALT::django_views_urls_params]
<!-- ER2 -->

[EQ] Testen Sie die URL mit verschiedenen GET-Parametern. Was passiert, wenn Sie
`http://127.0.0.1:8071/params/?name=Anna&age=25` aufrufen? Was geschieht bei
`http://127.0.0.1:8071/params/` ohne Parameter? Wenn Sie einen anderen Port verwenden,
passen Sie den Link entsprechend an.
<!-- EQ2 -->
<!-- time estimate: 10 min -->

### Request-Attribute: POST-Daten verarbeiten

POST-Daten werden über `request.POST` abgerufen. Diese sind typischerweise bei
Formular-Übertragungen relevant:

[ER] Erstellen Sie in `views.py` eine View-Funktion für POST-Requests:

[SNIPPET::ALT::django_views_post_data]
<!-- ER3 -->

[NOTICE]
Der Decorator `@csrf_exempt` schaltet Djangos CSRF-Schutz für diese View gezielt ab —
nötig, damit Sie die POST-Anfrage direkt mit `curl` testen können, ohne zuvor ein
HTML-Formular zu bauen. Was CSRF ist und warum es normalerweise wichtig ist, lernen Sie in
[PARTREF::django-form].
[ENDNOTICE]

[ER] Fügen Sie in `urls.py` die URL-Route hinzu:

[SNIPPET::ALT::django_views_urls_post]
<!-- ER4 -->

[EC] Testen Sie die POST-View mit `curl` (`-X`/`-d`, siehe [PARTREF::curl]):

```bash
curl -X POST -d "username=Max&message=Hallo" http://127.0.0.1:8071/post-data/
```

Wenn Sie einen anderen Port verwenden, passen Sie den Befehl entsprechend an.
<!-- EC1 -->

[EQ] Vergleichen Sie mit der GET-Parameter-View aus [EREFQ::2]: Was ist der wesentliche
Unterschied bezüglich der URL-Anzeige und Datenübertragung zwischen GET und POST?
<!-- EQ3 -->
<!-- time estimate: 15 min -->

### Weitere Request-Attribute erforschen

Django-Request-Objekte bieten weitere nützliche Attribute:

[ER] Erstellen Sie in `views.py` eine View-Funktion, die verschiedene Request-Attribute
anzeigt:

[SNIPPET::ALT::django_views_request_info]
<!-- ER5 -->

[ER] Fügen Sie in `urls.py` die entsprechende URL-Route hinzu:

[SNIPPET::ALT::django_views_urls_request_info]
<!-- ER6 -->

[EQ] Testen Sie die Request-Info-View unter `http://127.0.0.1:8071/request-info/`: Rufen Sie
die URL auf und notieren Sie die verschiedenen Request-Informationen. Was verrät der
User-Agent über Ihren Browser und welche HTTP-Methode wird verwendet? Wenn Sie einen anderen
Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ4 -->
<!-- time estimate: 15 min -->

### Response-Objekte: HttpResponse

Der einfachste Response-Typ ist `HttpResponse`, der direkt Text oder HTML zurückgibt:

[ER] Erstellen Sie in `views.py` eine View mit verschiedenen HttpResponse-Beispielen:

[SNIPPET::ALT::django_views_response_examples]
<!-- ER7 -->

[ER] Fügen Sie in `urls.py` die entsprechende URL-Route hinzu:

[SNIPPET::ALT::django_views_urls_responses]
<!-- ER8 -->

[EQ] Testen Sie verschiedene Response-Typen durch Aufrufen der folgenden URLs:

1. `http://127.0.0.1:8071/responses/` (Standard-Text-Response)
2. `http://127.0.0.1:8071/responses/?type=html` (HTML-Response)
3. `http://127.0.0.1:8071/responses/?type=json` (JSON-Response)

Was ist der Unterschied in der Browser-Darstellung zwischen diesen drei Response-Typen?
Wenn Sie einen anderen Port verwenden, passen Sie die Links entsprechend an.
<!-- EQ5 -->
<!-- time estimate: 15 min -->

### Response-Objekte: redirect() für Weiterleitungen

`redirect()` wird verwendet, um Benutzer auf andere URLs umzuleiten:

[ER] Erstellen Sie in `views.py` Views für Umleitung und Zielseite:

[SNIPPET::ALT::django_views_redirect]
<!-- ER9 -->

[ER] Fügen Sie in `urls.py` beide URL-Routen hinzu:

[SNIPPET::ALT::django_views_urls_redirect]
<!-- ER10 -->

[EQ] Testen Sie die Redirect-Funktionalität durch Aufrufen von
`http://127.0.0.1:8071/redirect-test/`: Beobachten Sie genau: Was passiert in Ihrem Browser
und wie verändert sich die URL nach dem Aufrufen? Welcher HTTP-Statuscode wird dabei
verwendet? Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ6 -->
<!-- time estimate: 20 min -->

[NOTICE]
`render()` ist eine dritte Möglichkeit für Response-Objekte, die Django-Templates
verwendet. Sie wird in [PARTREF::django-template] vertieft.
[ENDNOTICE]

[EQ] Welchen der beiden Response-Typen (`HttpResponse`, `redirect`) würden Sie für folgende
Szenarien verwenden?

- Anzeige einer Bestätigungsnachricht nach dem Speichern
- Weiterleitung nach erfolgreicher Anmeldung
<!-- EQ7 -->
<!-- time estimate: 10 min -->

### URL-Parameter mit Typkonvertern

Bisher waren alle Routen fest (`params/`, `post-data/`, ...). Häufig soll eine Route aber
einen Teil der URL selbst als Parameter an die View weitergeben — etwa eine ID. Dafür bietet
`path()` **Typkonverter** in spitzen Klammern:

```python
path("students/<int:student_id>/", views.student_detail, name="student_detail")
```

`<int:student_id>` extrahiert den entsprechenden URL-Teil, wandelt ihn in den angegebenen
Typ um und übergibt ihn als Funktionsargument. Die gängigsten Typkonverter:

- `str`: beliebiger Text ohne `/` (Standard, falls kein Typ angegeben wird).
- `int`: nur Ziffern, wird als Python-`int` übergeben.
- `slug`: Buchstaben, Ziffern, Bindestrich und Unterstrich (typisch für lesbare URLs).
- `uuid`: ein formatierter UUID-String.
- `path`: wie `str`, akzeptiert aber zusätzlich `/`.

[ER] Erstellen Sie eine View, die einen `Student` anhand seiner ID anzeigt (verwendet die
bereits aus [PARTREF::django-model] bekannte `.objects.get()`):

[SNIPPET::ALT::django_views_student_detail]
<!-- ER11 -->

[ER] Fügen Sie die passende Route mit `int`-Typkonverter hinzu:

[SNIPPET::ALT::django_views_urls_student_detail]
<!-- ER12 -->

[HINT::Warum `<int:student_id>` und nicht `<str:student_id>`?]
Mit `<str:student_id>` würde auch `students/abc/` auf diese Route passen — die View müsste
dann selbst prüfen und behandeln, dass `"abc"` keine gültige ID ist. Mit `<int:student_id>`
übernimmt Django diese Prüfung bereits im URL-Matching: Passt der URL-Teil nicht auf eine
Ganzzahl, greift die Route gar nicht erst, und Django probiert die nächste passende Route
(oder gibt 404 zurück). Der Typkonverter verlagert eine Validierung, die Sie sonst manuell
in der View schreiben müssten, in die URL-Konfiguration.
[ENDHINT]

[EQ] Testen Sie `http://127.0.0.1:8071/students/1/` sowie eine ID, die es nicht gibt (z. B.
`http://127.0.0.1:8071/students/999/`). Was unterscheidet sich, und woran liegt das (Tipp:
Sie kennen dieses Verhalten bereits von `.objects.get()` aus [PARTREF::django-model])? Wenn
Sie einen anderen Port verwenden, passen Sie die Links entsprechend an.
<!-- EQ8 -->
<!-- time estimate: 15 min -->

### `reverse()`: benannte Routen für Wartbarkeit

Jede Route in `urls.py` hat bereits einen `name` (z. B. `name="student_detail"`) — diese
Namen dienten bisher nur der Übersicht. Mit `reverse()` lässt sich aus einem solchen Namen
zur Laufzeit die passende URL erzeugen, statt sie fest in den Code zu schreiben:

```python
from django.urls import reverse

url = reverse("student_detail", args=[1])  # ergibt "/students/1/"
```

Der Vorteil: Ändert sich später das URL-Muster in `urls.py` (z. B. von `students/` zu
`teilnehmer/`), passt sich jeder mit `reverse()` erzeugte Link automatisch an — nur die
Route selbst muss geändert werden, nicht jede Stelle im Code, die auf sie verweist.

[ER] Erstellen Sie eine View, die mit `reverse()` zur Detailseite von Student 1
weiterleitet:

[SNIPPET::ALT::django_views_reverse_redirect]
<!-- ER13 -->

[ER] Fügen Sie die passende Route hinzu:

[SNIPPET::ALT::django_views_urls_reverse]
<!-- ER14 -->

[EQ] Testen Sie `http://127.0.0.1:8071/students/redirect/`. Wohin werden Sie
weitergeleitet, und stimmt das mit der ID überein, die Sie in der View an `reverse()`
übergeben haben? Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend
an.
<!-- EQ9 -->
<!-- time estimate: 15 min -->

### Reflexion: fest codierte Links vs. `reverse()`

[EQ] Stellen Sie sich vor, die Route für die Studierenden-Detailseite soll künftig nicht
mehr `students/<int:student_id>/`, sondern `teilnehmer/<int:student_id>/` heißen. Wie viele
Stellen im Code müssten Sie anpassen, wenn Sie überall fest codierte Links wie
`"/students/1/"` verwendet hätten? Wie viele Stellen, wenn Sie stattdessen konsequent
`reverse("student_detail", args=[1])` verwendet hätten?
<!-- EQ10 -->
<!-- time estimate: 10 min -->

### Weiterführend

- [Django Request Objects](https://docs.djangoproject.com/en/stable/ref/request-response/) – Detaillierte Dokumentation zum Request-Objekt und seinen Attributen
- [Path converters](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters) – Vollständige Liste der eingebauten Typkonverter für `path()`
- [Reverse resolution of URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/#reverse-resolution-of-urls) – Weitere Details zu `reverse()` und benannten Routen

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::4]/[EREFR::10]: `post_data` prüft `request.method`; `redirect_example` gibt eine
  `redirect()`-Antwort zurück (kein `HttpResponse`).
- [EREFQ::8]: Student erkennt, dass eine nicht existierende ID zu einem Fehler führt, weil
  `.objects.get()` (bereits aus `django-model` bekannt) ohne passenden Treffer eine
  Exception auslöst — derselbe Mechanismus, nur diesmal über eine URL statt über die Shell
  ausgelöst.
- [EREFQ::10]: Student erkennt, dass bei fest codierten Links jede einzelne Stelle im Code
  manuell angepasst werden müsste, während bei konsequenter Verwendung von `reverse()` nur
  die Route selbst in `urls.py` geändert werden muss.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-views.md]

### Kommandoprotokoll
[PROT::ALT:django-views.prot]

[ENDINSTRUCTOR]
