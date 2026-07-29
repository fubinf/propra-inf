title: Django View
stage: alpha
timevalue: 2.5
difficulty: 2
requires: django-model
assumes: http-GET, http-POST, curl, py-Fstrings
---

[SECTION::goal::idea,experience]

- Ich verstehe die Funktionsweise von Django-Views und deren Zusammenspiel mit HTTP-Requests
  und -Responses.
- Ich kann Request-Daten aus verschiedenen Quellen verarbeiten und passende Response-Typen
  zurückgeben.
- Ich verstehe, warum benannte Routen den Code wartbarer machen als fest codierte URLs.

[ENDSECTION]

[SECTION::background::default]

In Django ist die View das Bindeglied zwischen den eingehenden HTTP-Requests und den
ausgehenden HTTP-Responses. Jede View-Funktion empfängt ein Request-Objekt mit allen
Informationen der HTTP-Anfrage und muss ein Response-Objekt zurückgeben.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`, die Sie in [PARTREF::django-project] angelegt und
in [PARTREF::django-model] um das `Student`-Model erweitert haben. Alle folgenden Änderungen
finden in `webapp` statt; mit `views.py` und `urls.py` sind also stets `webapp/views.py` und
`webapp/urls.py` gemeint, nicht die gleichnamigen Dateien im Konfigurationsordner.

Alle `curl`-Befehle unten verwenden den Port 8071; falls Sie den Entwicklungsserver auf einem
anderen Port betreiben, passen Sie die Befehle entsprechend an. Starten Sie den Server, falls
er nicht mehr läuft, mit `python manage.py runserver 8071`.

### Die View und das Request-Objekt verstehen

Eine View-Funktion ist das Herzstück der Django-Anwendung. Django nimmt die eingehende
HTTP-Anfrage (Request und Response kennen Sie aus [PARTREF::http-GET]) und übergibt sie der
View als Python-Objekt `HttpRequest`; die View gibt ein `HttpResponse`-Objekt zurück, aus dem
Django die HTTP-Antwort erzeugt:

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello World!")
```

[EQ] Schlagen Sie in der Django-Dokumentation zu
[Writing views](https://docs.djangoproject.com/en/stable/topics/http/views/) nach: Welche
zwei Bestandteile sind laut dieser Seite bei jeder View-Funktion notwendig?
<!-- time estimate: 10 min -->

### Request-Attribute: GET-Parameter verarbeiten

Eine View liest die Eingaben einer Anfrage aus dem Request-Objekt; am häufigsten sind das die
GET-Parameter, die als Query-String in der URL stehen.
Das `request.GET`-Attribut ist ein `QueryDict`, ein wörterbuchähnliches Objekt, das alle
GET-Parameter der URL als Schlüssel-Wert-Paare enthält. Einzelne Parameter liest man daraus
wie aus einem Dictionary:

```
request.GET.get(key, default)
```

- `key`: der Name des GET-Parameters, den Sie auslesen möchten
- `default`: der Wert, der zurückgegeben wird, falls der Parameter in der URL **fehlt**; so
  lässt sich ein Zugriff auf einen nicht übergebenen Parameter ohne Fehler abfangen

Ein konkretes Beispiel:

```python
stadt = request.GET.get("stadt", "Berlin")  # "Berlin", falls "stadt" fehlt
```

[ER] Schreiben Sie in `views.py` eine View-Funktion `get_params`, die die GET-Parameter
`name` und `age` mit `request.GET.get(...)` ausliest (Standardwerte `Unbekannt` bzw.
`Nicht angegeben`, falls sie fehlen) und als `HttpResponse` den Text
`Name: <name>, Alter: <age>` zurückgibt (z. B. mit einem f-String, der die Werte per
Interpolation in den Text einsetzt, siehe [PARTREF::py-Fstrings]). Denken Sie daran,
`HttpResponse` oben in der Datei zu importieren.

Damit die View über eine URL erreichbar wird, braucht sie eine Route in `urls.py`. Zur
Erinnerung aus [PARTREF::django-project] folgt eine Route diesem Muster:

```python
path("pfad/", views.funktionsname, name="name")
```

[ER] Ergänzen Sie `urlpatterns` in `urls.py` um eine Route für die neue View: Pfad `params/`,
Ziel `get_params`, Name `get_params`.

[EC] Rufen Sie die View einmal mit und einmal ohne GET-Parameter auf (`curl`, siehe
[PARTREF::curl]):

```bash
curl "http://127.0.0.1:8071/params/?name=Anna&age=25"
curl "http://127.0.0.1:8071/params/"
```

[EQ] Beim zweiten Aufruf fehlen die Parameter, trotzdem stürzt die View nicht ab.
Warum ist das so, und welche Rolle spielt dabei das zweite Argument von `request.GET.get(...)`?
<!-- time estimate: 15 min -->

### Request-Attribute: POST-Daten verarbeiten

Während GET-Parameter sichtbar in der URL stehen, gibt es mit POST einen zweiten Weg, Daten
an eine View zu senden. POST-Daten werden über `request.POST` abgerufen und sind typischerweise
bei Formular-Übertragungen relevant. `request.POST` funktioniert wie `request.GET`: auch hier
liest man Werte mit `.get(key, default)`.

Da eine View sowohl per GET als auch per POST aufgerufen werden kann, prüft man mit
`request.method`, um welche Art von Anfrage es sich handelt:

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def beispiel_view(request):
    if request.method == "POST":
        wert = request.POST.get("feld", "kein Wert")
        return HttpResponse(f"Erhalten: {wert}")
    return HttpResponse("Bitte per POST senden.")
```

[NOTICE]
Der Decorator `@csrf_exempt` schaltet Djangos CSRF-Schutz für eine View gezielt ab; nötig ist
das, damit Sie die POST-Anfrage direkt mit `curl` testen können, ohne zuvor ein HTML-Formular
zu bauen. Was CSRF ist und warum es normalerweise wichtig ist, lernen Sie in
[PARTREF::django-form].
[ENDNOTICE]

[ER] Schreiben Sie in `views.py` eine View-Funktion `post_data`, versehen mit
`@csrf_exempt`. Sie soll `request.method` prüfen: Bei `POST` liest sie `username` und
`message` aus `request.POST` (Standardwerte `Kein Name` bzw. `Keine Nachricht`) und gibt den
Text `Empfangen von <username>: <message>` zurück; bei jeder anderen Methode gibt sie
stattdessen `Bitte per POST senden.` zurück. Importieren Sie dafür `csrf_exempt`.

[ER] Fügen Sie in `urls.py` die Route für `post_data` hinzu: Pfad `post-data/`, Name
`post_data`.

[EC] Testen Sie die POST-View mit `curl` (`-X`/`-d`, siehe [PARTREF::curl]):

```bash
curl -X POST -d "username=Max&message=Hallo" http://127.0.0.1:8071/post-data/
```

[EQ] Vergleichen Sie mit der GET-Parameter-View aus [EREFR::1]: Was ist der wesentliche
Unterschied bezüglich der URL-Anzeige und Datenübertragung zwischen GET und POST?
<!-- time estimate: 20 min -->

### Weitere Request-Attribute erforschen

Neben `request.GET` und `request.POST` bietet das Request-Objekt weitere nützliche Attribute,
etwa zur verwendeten HTTP-Methode oder zum aufgerufenen Pfad.

[ER] Schreiben Sie in `views.py` eine View-Funktion `request_info`, die zwei Angaben aus dem
Request als `HttpResponse` im Format `Methode: <...>, Pfad: <...>` zurückgibt (die
verwendete HTTP-Methode und den aufgerufenen Pfad; die passenden Attribute finden Sie im
Abschnitt "Attributes" der
[Django-Doku zu `HttpRequest`](https://docs.djangoproject.com/en/stable/ref/request-response/#attributes)).

[ER] Fügen Sie in `urls.py` die Route für `request_info` hinzu: Pfad `request-info/`, Name
`request_info`.

[EC] Rufen Sie die Request-Info-View auf:

```bash
curl http://127.0.0.1:8071/request-info/
```

[EQ] Warum ist die HTTP-Methode immer `GET`, wenn Sie eine URL direkt im Browser aufrufen?
<!-- time estimate: 15 min -->

### Response-Objekte: HttpResponse

Bisher ging es um die eingehende Seite, also den Request. Ebenso wichtig ist die ausgehende
Seite: die Response, die jede View zurückgeben muss. Der einfachste Response-Typ ist
`HttpResponse`, der direkt Text oder HTML zurückgibt. Eine View kann dabei je nach
GET-Parameter unterschiedliche Responses erzeugen, nach folgendem Schema:

```python
def beispiel_view(request):
    if request.GET.get("modus") == "x":
        return HttpResponse("Variante X")
    return HttpResponse("Variante Y")
```

[ER] Schreiben Sie in `views.py` eine View-Funktion `responses`, die abhängig vom
GET-Parameter `type` unterschiedliche `HttpResponse`-Objekte zurückgibt: bei `type=html` das
HTML-Fragment `<h1>HTML-Antwort</h1>`, bei `type=json` den JSON-String `{"status": "ok"}` mit
dem zusätzlichen Argument `content_type="application/json"`, und sonst den Text
`Text-Antwort`. Das `content_type`-Argument von `HttpResponse` ist neu; schlagen Sie es in der
[Django-Doku zu HttpResponse-Objekten](https://docs.djangoproject.com/en/stable/ref/request-response/#httpresponse-objects)
nach.

[ER] Fügen Sie in `urls.py` die Route für `responses` hinzu: Pfad `responses/`, Name
`responses`.

Den `Content-Type`-Header und die dahinterstehenden MIME-Types kennen Sie bereits aus
[PARTREF::http-GET] (siehe dort auch die
[MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types)-Übersicht): Er
entscheidet, als was der Browser eine Antwort interpretiert, unabhängig vom eigentlichen
Inhalt. Die drei Varianten von `responses` liefern unterschiedliche `content_type`-Werte;
mit `-i` werden die Header mit ausgegeben, nicht nur der Antwort-Rumpf:

[EC] Rufen Sie alle drei Response-Typen nacheinander auf:

```bash
curl -s -i "http://127.0.0.1:8071/responses/"
curl -s -i "http://127.0.0.1:8071/responses/?type=html"
curl -s -i "http://127.0.0.1:8071/responses/?type=json"
```

[EQ] Welchen `Content-Type`-Wert zeigt jede der drei Antworten in der Kopfzeile
`Content-Type: ...`? Bei welcher der drei unterscheidet er sich vom Standardwert der beiden
anderen, und an welcher Stelle im Code wurde das festgelegt?
<!-- time estimate: 20 min -->

### Response-Objekte: redirect() für Weiterleitungen

Statt selbst Inhalt zurückzugeben, kann eine View den Client auch an eine andere URL
verweisen. Dafür dient `redirect()`, das den Client auf eine andere URL umleitet:

```
redirect(to)
```

- `to`: das Umleitungsziel, also ein Routenname (der `name` aus `urls.py`), eine URL oder ein
  Objekt; Django erzeugt daraus eine Weiterleitungs-Antwort mit standardmäßig Statuscode 302

Das folgende Schema zeigt eine Zielview und eine View, die dorthin weiterleitet:

```python
from django.shortcuts import redirect

def ziel_view(request):
    return HttpResponse("Angekommen!")

def start_view(request):
    return redirect("ziel_view")  # "ziel_view" ist der Routenname aus urls.py
```

[ER] Schreiben Sie in `views.py` zwei View-Funktionen: `redirect_target`, die als
`HttpResponse` den Text `Sie wurden weitergeleitet!` zurückgibt, und `redirect_example`, die
mit `redirect("redirect_target")` dorthin weiterleitet. Importieren Sie dafür `redirect`.

[ER] Fügen Sie in `urls.py` beide Routen hinzu: Pfad `redirect-target/` mit Ziel
`redirect_target` (Name `redirect_target`) und Pfad `redirect-test/` mit Ziel
`redirect_example` (Name `redirect_example`).

[EC] Rufen Sie die Umleitung auf. Mit `-i` werden die Antwort-Header sichtbar, mit `-s`
bleibt die Ausgabe knapp:

```bash
curl -s -i http://127.0.0.1:8071/redirect-test/
```

[EQ] Die Antwort hat den Statuscode 302 und einen `Location`-Header statt eines Seiteninhalts.
Warum gibt `redirect_example` einen Redirect (302) zurück statt direkt eine `HttpResponse` mit
dem Zielinhalt? Was gewinnt man dadurch?

[NOTICE]
Neben `HttpResponse` und `redirect()` ist `render()` eine dritte Möglichkeit für
Response-Objekte, die Django-Templates verwendet. Sie wird in [PARTREF::django-template]
vertieft.
[ENDNOTICE]

[EQ] Würden Sie `HttpResponse` oder `redirect()` für folgende Szenarien verwenden?

- Direkte Anzeige einer einfachen Info-Seite mit statischem Text
- Weiterleitung nach erfolgreicher Anmeldung
<!-- time estimate: 20 min -->

### URL-Parameter mit Typkonvertern

Bisher waren alle Routen fest (`params/`, `post-data/`, ...). Häufig soll eine Route aber
einen Teil der URL selbst als Parameter an die View weitergeben, etwa eine ID. Dafür bietet
`path()` **Typkonverter** in spitzen Klammern:

```python
path("artikel/<typ:artikel_id>/", views.artikel_detail, name="artikel_detail")
```

`<typ:artikel_id>` extrahiert den entsprechenden URL-Teil, wandelt ihn in den angegebenen
Typ um und übergibt ihn als Funktionsargument; `typ` steht dabei für einen der folgenden
Bezeichner. Dies ist bereits die vollständige Liste der standardmäßig verfügbaren
Typkonverter:

- `str`: beliebiger Text ohne `/` (Standard, falls kein Typ angegeben wird).
- `int`: nur Ziffern, wird als Python-`int` übergeben.
- `slug`: Buchstaben, Ziffern, Bindestrich und Unterstrich (typisch für lesbare URLs).
- `uuid`: eine UUID im Standardformat mit Bindestrichen, wird als `uuid.UUID`-Objekt übergeben.
- `path`: wie `str`, akzeptiert aber zusätzlich `/`.

Der Typkonverter übergibt den extrahierten Wert als Funktionsargument; damit lässt sich ein
Objekt anhand der URL laden, nach folgendem Schema:

```python
from .models import MeinModel

def eintrag_view(request, eintrag_id):
    objekt = MeinModel.objects.get(id=eintrag_id)
    return HttpResponse(f"Gefunden: {objekt}")
```

[ER] Schreiben Sie in `views.py` eine View-Funktion `student_detail(request, student_id)`, die
den `Student` mit der übergebenen ID per `Student.objects.get()` (bekannt aus
[PARTREF::django-model]) lädt und seine Daten im Format `<name>, <age> Jahre, <email>` als
`HttpResponse` zurückgibt.

[ER] Fügen Sie in `urls.py` die passende Route mit `int`-Typkonverter hinzu: Pfad
`students/<int:student_id>/` mit Ziel `student_detail`, Name `student_detail`.

[HINT::Warum `<int:student_id>` und nicht `<str:student_id>`?]
Mit `<str:student_id>` würde auch `students/abc/` auf diese Route passen; die View müsste
dann selbst prüfen und behandeln, dass `"abc"` keine gültige ID ist. Mit `<int:student_id>`
übernimmt Django diese Prüfung bereits im URL-Matching: Passt der URL-Teil nicht auf eine
Ganzzahl, greift die Route gar nicht erst, und Django probiert die nächste passende Route
(oder gibt 404 zurück). Der Typkonverter verlagert eine Validierung, die Sie sonst manuell
in der View schreiben müssten, in die URL-Konfiguration.
[ENDHINT]

[EC] Rufen Sie die Detailseite einmal mit einer existierenden und einmal mit einer nicht
existierenden ID auf:

```bash
curl "http://127.0.0.1:8071/students/1/"
curl -s -i http://127.0.0.1:8071/students/999/
```

[EQ] Der zweite Aufruf endet nicht mit den Studierendendaten, sondern mit einem Fehler. Woran
liegt das, und an welcher Stelle in der View entsteht dieser Fehler?

[HINT::Puh, woher soll ich das wissen?]
Was passiert, wenn `.objects.get()` (aus [PARTREF::django-model]) keinen passenden Datensatz findet?
Und was bedeutet der erhaltene HTTP-Statuscode?
[ENDHINT]
<!-- time estimate: 20 min -->

### `urls.py` wartbar halten: `reverse()` für benannte Routen

Jede Route in `urls.py` hat bereits einen `name` (z. B. `name="student_detail"`); bisher
diente dieser Name nur als Sprungziel für `redirect()`, wie in `redirect_example` oben. Mit
`reverse()` lässt sich aus einem solchen Namen an beliebiger Stelle im Code zur Laufzeit die
passende URL erzeugen — nicht nur als Ziel eines Redirects, sondern überall dort, wo eine
URL gebraucht wird, etwa später in Templates:

```
reverse(viewname, args=[...])
```

- `viewname`: der in `urls.py` vergebene Routenname (z. B. `"student_detail"`)
- `args`: Liste der Positionsargumente für die dynamischen URL-Teile (z. B. `[1]` für die ID)

```python
from django.urls import reverse

url = reverse("student_detail", args=[2])  # ergibt "/students/2/"
```

Der Vorteil: Ändert sich später das URL-Muster in `urls.py` (z. B. von `students/` zu
`teilnehmer/`), passt sich jeder mit `reverse()` erzeugte Link automatisch an; nur die
Route selbst muss geändert werden, nicht jede Stelle im Code, die auf sie verweist. Das ist
ein zentrales Feature von Django: Eine konsequent mit benannten Routen und `reverse()`
geschriebene Anwendung lässt sich jederzeit lokal umstrukturieren, ohne dass an verstreuten
Stellen im Code oder in Templates von Hand nachgezogen werden muss.

In einer View lässt sich das erzeugte Ergebnis direkt an `redirect()` übergeben, etwa nach
diesem Schema:

```python
def einstieg_view(request):
    ziel = reverse("student_detail", args=[3])
    return redirect(ziel)
```

[ER] Schreiben Sie in `views.py` eine View-Funktion `student_redirect`, die mit `reverse()`
die URL der Detailseite von Student `1` erzeugt und den Client per `redirect()` dorthin
weiterleitet.

[ER] Fügen Sie in `urls.py` die Route für `student_redirect` hinzu: Pfad `students/redirect/`,
Name `student_redirect`.

[EC] Rufen Sie die Weiterleitung auf und achten Sie auf den `Location`-Header:

```bash
curl -s -i http://127.0.0.1:8071/students/redirect/
```

[EQ] Der `Location`-Header zeigt auf `/students/1/`. Wie hat `reverse()` aus dem Routennamen
diese URL erzeugt?
<!-- time estimate: 15 min -->

[EQ] Stellen Sie sich vor, die Route für die Studierenden-Detailseite soll künftig nicht
mehr `students/<int:student_id>/`, sondern `teilnehmer/<int:student_id>/` heißen. Wie viele
Stellen im Code müssten Sie anpassen, wenn Sie überall fest codierte Links wie
`"/students/1/"` verwendet hätten? Wie viele Stellen, wenn Sie stattdessen konsequent
`reverse("student_detail", args=[1])` verwendet hätten?
<!-- time estimate: 5 min -->

[EQ] Schauen Sie sich Ihre `urls.py` jetzt komplett an: Die Reihenfolge der Einträge folgt
bisher nur der Reihenfolge, in der die Views in dieser Aufgabe entstanden sind. Nennen Sie
mindestens zwei sinnvolle Arten, die Einträge stattdessen zu sortieren oder zu gruppieren.
<!-- time estimate: 10 min -->

### Weiterführend

- [Django Request Objects](https://docs.djangoproject.com/en/stable/ref/request-response/):
  Detaillierte Dokumentation zum Request-Objekt und seinen Attributen
- [Path converters](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters):
  Vollständige Liste der eingebauten Typkonverter für `path()`
- [Reverse resolution of URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/#reverse-resolution-of-urls):
  Weitere Details zu `reverse()` und benannten Routen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::13]/[EREFQ::9]: `student_redirect` kombiniert `reverse("student_detail", args=[1])`
  mit `redirect(...)`; ein falscher Routenname oder ein fehlendes `args` führt zu einem
  Laufzeitfehler statt zur erwarteten Weiterleitung. Student erkennt, dass `reverse()` den
  übergebenen Routennamen tatsächlich in `urls.py` nachschlägt, statt die URL nur zu raten.
- [EREFQ::8]: Student erkennt, dass eine nicht existierende ID zu einem Fehler führt, weil
  `.objects.get()` (bereits aus [PARTREF::django-model] bekannt) ohne passenden Treffer eine
  Exception auslöst; derselbe Mechanismus, nur diesmal über eine URL statt über die Shell
  ausgelöst.
- [EREFQ::10]: Student erkennt, dass bei fest codierten Links jede einzelne Stelle im Code
  manuell angepasst werden müsste, während bei konsequenter Verwendung von `reverse()` nur
  die Route selbst in `urls.py` geändert werden muss.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-view.md]

### Kommandoprotokoll
[PROT::ALT:django-view.prot]

[ENDINSTRUCTOR]
