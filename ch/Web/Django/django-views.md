title: Django Views
stage: draft
timevalue: 2
difficulty: 2
requires: django-project
assumes: http-GET, http-POST
---

[SECTION::goal::idea,experience]

- Ich verstehe die Funktionsweise von Django-Views und deren Zusammenspiel mit HTTP-Requests und -Responses.
- Ich kann Request-Objekte analysieren, HTTP-Parameter verarbeiten und einfache View-Funktionen erstellen.
- Ich beherrsche verschiedene Arten von Response-Objekten (HttpResponse, redirect).

[ENDSECTION]

[SECTION::background::default]

In Django sind Views das Bindeglied zwischen den eingehenden HTTP-Requests und den 
ausgehenden HTTP-Responses. Jede View-Funktion empfängt ein Request-Objekt mit allen 
Informationen der HTTP-Anfrage und muss ein Response-Objekt zurückgeben. 
Das Verständnis dieser fundamentalen Konzepte ist essentiell für die Django-Entwicklung.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit dem `meinprojekt`-Projekt, das Sie in [PARTREF::django-basics] erstellt haben.
Alle folgenden Änderungen werden Sie in diesem Projekt durchführen.

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

[EQ] Schauen Sie sich die `hello`-View aus [PARTREF::django-project] an.
Wie ist eine View-Funktion aufgebaut? Welche zwei Bestandteile sind zwingend notwendig?
<!-- EQ1 -->

<!-- time estimate: 10 min -->

### Request-Attribute: GET-Parameter verarbeiten

Das `request.GET` Attribut ist ein QueryDict-Objekt, das alle GET-Parameter der URL enthält:

[ER] Erstellen Sie in `views.py` eine View-Funktion:

[SNIPPET::ALT::django_views_get_params]
<!-- ER1 -->

[ER] Modifizieren Sie `urls.py`, um die neue View einzubinden:

[SNIPPET::ALT::django_views_urls]
<!-- ER2 -->

[EQ] Testen Sie die URL mit verschiedenen GET-Parametern. Was passiert, wenn Sie 
`http://127.0.0.1:8071/params/?name=Anna&age=25` aufrufen? 
Was geschieht bei `http://127.0.0.1:8071/params/` ohne Parameter?
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ2 -->

<!-- time estimate: 10 min -->

### Request-Attribute: POST-Daten verarbeiten

POST-Daten werden über `request.POST` abgerufen. Diese sind typischerweise bei 
Formular-Übertragungen relevant:

[ER] Erstellen Sie in `views.py` eine View-Funktion für POST-Requests:

[SNIPPET::ALT::django_views_post_data]
<!-- ER3 -->

[ER] Fügen Sie in `urls.py` die URL-Route hinzu:

[SNIPPET::ALT::django_views_urls_post]
<!-- ER4 -->

[EQ] Testen Sie die POST-View unter `http://127.0.0.1:8071/post-data/` und vergleichen Sie mit der GET-Parameter-View aus [EREFQ::2]: 
Was ist der wesentliche Unterschied 
bezüglich der URL-Anzeige und Datenübertragung zwischen GET und POST?
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ3 -->

<!-- time estimate: 15 min -->

### Weitere Request-Attribute erforschen

Django-Request-Objekte bieten weitere nützliche Attribute:

[ER] Erstellen Sie in `views.py` eine View-Funktion, die verschiedene Request-Attribute anzeigt:

[SNIPPET::ALT::django_views_request_info]
<!-- ER5 -->

[ER] Fügen Sie in `urls.py` die entsprechende URL-Route hinzu:

[SNIPPET::ALT::django_views_urls_request_info]
<!-- ER6 -->

[EQ] Testen Sie die Request-Info-View unter `http://127.0.0.1:8071/request-info/`:
Rufen Sie die URL auf und notieren Sie die verschiedenen Request-Informationen.
Was verrät der User-Agent über Ihren Browser und welche HTTP-Methode wird verwendet?
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
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

[EQ] Testen Sie die Redirect-Funktionalität durch Aufrufen von `http://127.0.0.1:8071/redirect-test/?user=Anna`:
Beobachten Sie genau: Was passiert in Ihrem Browser und wie verändert sich die URL nach dem Aufrufen?
Welche HTTP-Statuscodes werden dabei verwendet?
Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ6 -->

<!-- time estimate: 20 min -->

[NOTICE]
`render()` ist eine dritte Möglichkeit für Response-Objekte, die Django-Templates verwendet.
Sie wird in [PARTREF::django-template] eingeführt.
[ENDNOTICE]

[EQ] Welche der zwei Response-Typen (HttpResponse, redirect) würden Sie 
für folgende Szenarien verwenden:

- Anzeige einer Bestätigungsnachricht nach dem Speichern
- Weiterleitung nach erfolgreicher Anmeldung
<!-- EQ7 -->

<!-- time estimate: 10 min -->

### Weiterführend

- [Django Request Objects](https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest) – Detaillierte Dokumentation zum Request-Objekt und seinen Attributen

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::2]: `urls.py` enthält die bestehende `hello`-Route und die neue `get_params`-Route (nicht überschrieben).
- [EREFR::3]/[EREFR::9]: `post_data` prüft `request.method`; `redirect_example` gibt eine `redirect()`-Antwort zurück (kein `HttpResponse`).
- [EREFQ::6]: Student beobachtet URL-Wechsel nach Redirect und nennt HTTP 302.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-views.md]

[ENDINSTRUCTOR]
