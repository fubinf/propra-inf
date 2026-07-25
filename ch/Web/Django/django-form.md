title: Django Formularbehandlung
stage: alpha
timevalue: 1.5
difficulty: 2
requires: django-template
assumes: http-GET, http-POST, html-Formulare, curl
---

[SECTION::goal::idea,experience]

- Ich verstehe den Unterschied zwischen GET und POST beim Absenden von Formularen.
- Ich kann HTML-Formulare erstellen, ihre Daten in einer View verarbeiten und dauerhaft
  in der Datenbank speichern.
- Ich verstehe die Rolle des CSRF-Schutzes im Formular-Workflow.

[ENDSECTION]

[SECTION::background::default]

HTML-Formulare sind der klassische Weg, über den Nutzer Daten an eine Web-Anwendung senden,
von der Suchanfrage bis zur Registrierung. Diese Aufgabe führt die bisher getrennt
behandelten Ebenen zusammen: Ein Formular wird in einem Template dargestellt, seine Daten in
einer View verarbeitet und über ein Model in der Datenbank gespeichert.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`. Aus den vorherigen Aufgaben stehen Ihnen bereits
das `Student`-Model ([PARTREF::django-model]), Views mit URL-Routing ([PARTREF::django-view])
und das Template-System ([PARTREF::django-template]) zur Verfügung. Alle Änderungen finden in
`webapp` statt.

### HTTP-Formulare: GET und POST

Die Grundelemente eines HTML-Formulars (`<form>`, `<input>`, Checkboxen,
`<button type="submit">`) kennen Sie bereits aus [PARTREF::http-POST] und
[PARTREF::html-Formulare]. Welche der beiden Methoden zum Einsatz kommt, legt das
`method`-Attribut von `<form>` fest: `method="get"` oder `method="post"`. Ein HTML-Formular
sendet seine Daten mit einer von zwei Methoden:

- **GET**: wirkungsfrei ("safe", siehe [PARTREF::http-GET]), verändert den Server-Zustand
  nicht. Die Daten werden sichtbar an die URL angehängt (`?q=...`), geeignet für Anfragen
  wie eine Suche, die man auch als Link teilen können soll.
- **POST**: verändert den Server-Zustand (siehe [PARTREF::http-POST]), etwa beim Anlegen
  eines Datensatzes. Die Daten werden im Request-Body übertragen und erscheinen nicht in
  der URL.

### GET-Formular: Suche

Mit diesem Unterschied im Hinterkopf bauen Sie jetzt ein erstes konkretes Formular: eine
Suche nach Studierenden. Da eine Suche den Server-Zustand nicht verändert, ist GET hier
die passende Methode. In [PARTREF::django-view] haben Sie GET-Parameter bereits mit
`request.GET.get(key, default)` gelesen, dort aber per `curl` von Hand an die URL
angehängt. Bei einem `<form method="get">` übernimmt der Browser das für Sie: Beim Absenden
hängt er jedes `<input name="...">` automatisch als `?name=wert` an die im `action`
angegebene URL an, genau die Parameter, die Sie mit `request.GET.get(...)` auslesen. Die
Suche greift auf die in [PARTREF::django-model] definierten `Student`-Objekte zu, über
`Student.objects.filter(name=...)`, dieselbe exakte Übereinstimmungssuche, die Sie dort
bereits kennengelernt haben. Ein Formular mit GET-Methode hat folgende Bestandteile:

```html
<form action="ZIEL" method="get">
    <input type="text" name="FELDNAME" value="VOREINGESTELLTER_TEXT" placeholder="HINWEISTEXT">
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `action`: die Route, an die das Formular sendet, gesetzt mit `{% url %}`
- `method="get"`: sendet die Daten als GET-Parameter an die im `action` angegebene URL
- `name`: der Schlüssel, unter dem der eingegebene Wert als GET-Parameter ankommt
- `value` (bei `<input type="text">`): der Text, der schon im Feld steht, anders als bei
  einer Checkbox, wo `value` den beim Ankreuzen gesendeten Wert bestimmt
- `placeholder`: Hinweistext, der nur angezeigt wird, solange das Feld leer ist, und beim
  Absenden nicht mitgeschickt wird

Konkretes Beispiel:

```html
<form action="{% url 'routenname' %}" method="get">
    <input type="text" name="feld" value="{{ variable }}" placeholder="Ihre Eingabe">
    <button type="submit">Absenden</button>
</form>
```

[ER] Schreiben Sie in `views.py` zwei View-Funktionen: `search_form`
rendert nur `search_form.html` ohne Context; `search` liest den GET-Parameter `q` aus
(Standardwert leerer String), sucht bei nichtleerem `q` mit `objects.filter`
(sonst `[]`) und rendert `search_form.html` mit `q` und `results` im Context.

Erstellen Sie `search_form.html` mit folgender Grundstruktur, den `<body>` füllen Sie im
nächsten Schritt:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Suche</title>
</head>
<body>
</body>
</html>
```

[ER] Füllen Sie den `<body>` von `search_form.html`: eine Überschrift (`<h1>`) mit dem Text
"Suchformular (GET)", darunter ein `<form>` mit `method="get"`, das an `{% url 'search' %}`
sendet, mit einem Text-Eingabefeld `name="q"` (Wert vorbelegt mit `{{ q }}`, Platzhaltertext
"Suchbegriff") und einem Absende-Button mit dem Text "Suchen". Zeigen Sie darunter, nur wenn
`q` gesetzt ist, eine `<ul>` mit `{% for %}`
über `results`: je Treffer ein Link zur Detailseite (`{% url 'student_detail' student.id
%}`) mit dem Namen; im `{% empty %}`-Zweig den Text `Keine Treffer für "{{ q }}"` (mit dem
eingesetzten Suchbegriff).

[ER] Ergänzen Sie `urls.py` um zwei Routen: Pfad `search-form/` auf `search_form` (Name
`search_form`), Pfad `search/` auf `search` (Name `search`).

[EC] Starten Sie den Entwicklungsserver und lassen Sie ihn laufen. Testen Sie die
GET-Suche direkt mit `curl` (der Suchbegriff ist URL-kodiert):

```bash
python manage.py runserver 8071
curl "http://127.0.0.1:8071/search/?q=Anna%20M%C3%BCller"
curl "http://127.0.0.1:8071/search/?q=Nichtvorhanden"
curl "http://127.0.0.1:8071/students/1/"
```

Wenn Sie einen anderen Port verwenden, passen Sie die Befehle entsprechend an.

[EQ] Der erste `curl`-Aufruf liefert einen Link zur Detailseite von Anna Müller. Woher weiß
das Template `search_form.html`, welche ID es in `{% url 'student_detail' student.id %}`
einsetzen muss, und was bestätigt Ihnen der dritte Aufruf (`/students/1/`) über diesen Link?

[EQ] Rufen Sie zusätzlich `http://127.0.0.1:8071/search-form/` im Browser auf und suchen
Sie nach dem exakten Namen eines bereits vorhandenen Studierenden (aus
[PARTREF::django-model]). Wie verändert sich die URL nach dem Absenden, und wo taucht Ihr
Suchbegriff auf? Suchen Sie anschließend nach einem Namen, den es nicht gibt: was wird
angezeigt, und welches Template-Tag sorgt dafür, dass die Seite dabei nicht fehlerhaft
wird? Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- time estimate: 30 min -->

### POST-Formular und CSRF-Schutz

Bei einem POST-Formular verlangt Django ein zusätzliches Sicherheitsmerkmal: das
`{% csrf_token %}`-Tag. **CSRF** (Cross-Site Request Forgery) bezeichnet einen Angriff, bei
dem eine fremde Website unbemerkt eine Aktion in Ihrem Namen auslöst, während Sie
eingeloggt sind. Um das zu verhindern, bettet Django in jedes Formular ein verstecktes,
einmaliges Token ein (`{% csrf_token %}`) und akzeptiert einen POST nur, wenn dieses Token
mitgeschickt wird, so kann eine fremde Seite kein gültiges Formular fälschen. Deshalb
gehört `{% csrf_token %}` in **jedes** POST-Formular.

[NOTICE]
In [PARTREF::django-view] hatten Sie eine POST-View versuchsweise mit `@csrf_exempt` vom
CSRF-Schutz ausgenommen, um sie ohne Formular testen zu können. Ab jetzt arbeiten Sie mit
echten Formularen und verwenden daher regulär `{% csrf_token %}` statt `@csrf_exempt`.
[ENDNOTICE]

Ein Formular mit POST-Methode hat dieselben Bestandteile wie eben, mit zwei Unterschieden:

```html
<form action="ZIEL" method="post">
    {% csrf_token %}
    <input type="text" name="FELDNAME">
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `method="post"`: sendet die Daten im Request-Body statt als GET-Parameter in der URL
- `{% csrf_token %}`: unmittelbar nach dem öffnenden `<form>`-Tag, bettet das oben
  beschriebene CSRF-Token ein

Konkretes Beispiel:

```html
<form action="{% url 'routenname' %}" method="post">
    {% csrf_token %}
    <input type="text" name="feld">
    <button type="submit">Absenden</button>
</form>
```

[ER] Schreiben Sie in `views.py` eine View-Funktion `search_post`: Bei einem POST-Request
liest sie den POST-Parameter `q` aus (Schlüssel `q`), sucht bei nichtleerem `q` mit
`Student.objects.filter(name=q)` (sonst `[]`) und rendert `search_post.html` mit `q` und
`results` im Context; bei jeder anderen Anfrage rendert sie `search_post.html` mit leerem
Context.

Erstellen Sie `search_post.html` mit derselben Grundstruktur wie `search_form.html` (Titel
`Suche (POST)`), den `<body>` füllen Sie im nächsten Schritt.

[ER] Füllen Sie den `<body>` von `search_post.html`: eine Überschrift (`<h1>`) mit dem Text
"Suchformular (POST)", darunter ein `<form>` mit `method="post"`, unmittelbar nach dem
öffnenden `<form>`-Tag `{% csrf_token %}`, ein Text-Eingabefeld `name="q"` (Platzhaltertext
"Suchbegriff") und ein Absende-Button mit dem Text "Suchen", gesendet an
`{% url 'search_post' %}`. Darunter denselben
`{% if q %}`/`{% for %}`/`{% empty %}`-Aufbau wie in `search_form.html` (mit demselben
`Keine Treffer für "{{ q }}"`-Text).

[ER] Ergänzen Sie `urls.py` um die Route `search-post/` auf `search_post` (Name
`search_post`).

[EQ] Suchen Sie unter `http://127.0.0.1:8071/search-post/` nach demselben Namen wie in
[EREFQ::2]. Worin unterscheidet sich die URL nach dem Absenden gegenüber dem GET-Formular,
und was würde passieren, wenn Sie `{% csrf_token %}` aus dem Formular entfernen? Wenn Sie
einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- time estimate: 30 min -->

### Registrierung mit Datenbank-Persistenz

Bisher wurden die Formulardaten nur zurückgespiegelt. Jetzt speichern Sie sie dauerhaft:
Ein Registrierungsformular legt über `Student.objects.create()` (aus [PARTREF::django-model])
einen neuen Datensatz an und leitet anschließend auf dessen Detailseite weiter. Da Name,
Alter und E-Mail hier echte Pflichtfelder sind, greifen Sie direkt mit `request.POST['feld']`
zu (anders als bei der optionalen Suche vorhin
mit `.get()`): Fehlt das Feld, wirft dieser Zugriff einen `KeyError`, statt stillschweigend
einen leeren Wert zu liefern. Eine View, die bei POST einen Datensatz anlegt und dann
weiterleitet, hat folgenden Aufbau:

```python
def beispiel_view(request):
    if request.method == 'POST':
        objekt = MeinModel.objects.create(feld=request.POST['feld'])
        return redirect(reverse('detail_route', args=[objekt.id]))
    return render(request, 'formular.html')
```

- `MeinModel.objects.create(...)`: legt den Datensatz an und gibt das neu erzeugte Objekt
  zurück (aus [PARTREF::django-model])
- `objekt.id`: die von der Datenbank vergebene ID des neuen Objekts
- `redirect(reverse(...))`: erzeugt aus dem Routennamen die Detail-URL und leitet dorthin
  weiter (aus [PARTREF::django-view])
- Bei jeder anderen Anfrage (kein POST) wird stattdessen das leere Formular gerendert

[NOTICE]
`request.POST` enthält nur die Formulardaten, die der Nutzer eingegeben hat (Name, Alter,
E-Mail); die ID vergibt die Datenbank erst beim Anlegen und steht dort nicht drin. Deshalb
kann `objekt.id` erst **nach** dem Aufruf von `Student.objects.create(...)` verwendet werden
(am zurückgegebenen Objekt), nicht aus `request.POST` selbst.
[ENDNOTICE]

[ER] Schreiben Sie in `views.py` eine View-Funktion `register` nach diesem Schema: Bei einem
POST-Request legt sie mit `Student.objects.create()` einen neuen `Student` aus
`request.POST['name']`, `request.POST['age']` und `request.POST['email']` an und leitet auf
dessen Detailseite (Route `student_detail`) weiter; bei jeder anderen Anfrage rendert sie
`register.html` ohne Context.

[HINT::Was muss ich zusätzlich importieren?]
Für diese View brauchen Sie zwei Imports: `from django.shortcuts import redirect` und
`from django.urls import reverse`. Falls Sie beim Aufräumen in [PARTREF::django-template]
auch den `redirect`-Import mit entfernt haben, müssen Sie ihn hier wieder ergänzen.
[ENDHINT]

Ein Formular mit mehreren Feldern hat folgende Bestandteile (aus [PARTREF::http-POST]):

```html
<form action="ZIEL" method="post">
    {% csrf_token %}
    <label>BESCHRIFTUNG: <input type="TYP" name="FELDNAME" required></label><br>
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `<label>Text: <input ...></label>`: verbindet die Beschriftung mit dem Feld
- `required`: macht das Feld zur Pflichteingabe, der Browser prüft das vor dem Absenden

Konkretes Beispiel mit zwei Feldern:

```html
<form action="{% url 'routenname' %}" method="post">
    {% csrf_token %}
    <label>Beschriftung 1: <input type="text" name="feld1" required></label><br>
    <label>Beschriftung 2: <input type="text" name="feld2" required></label><br>
    <button type="submit">Absenden</button>
</form>
```

[ER] Erstellen Sie das Template `register.html`: eine Überschrift (`<h1>`) mit dem Text
"Studierenden-Registrierung", darunter ein `<form>` mit `method="post"` (inklusive
`{% csrf_token %}`), das an `{% url 'register' %}` sendet, mit drei nach diesem Schema
beschrifteten und verpflichtenden Eingabefeldern (`name`: Text, "Name"; `age`: Zahl,
"Alter"; `email`: E-Mail, "E-Mail") und einem Absende-Button mit dem Text "Registrieren".

[ER] Ergänzen Sie `urls.py` um die Route `register/` auf `register` (Name `register`).

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/` und senden Sie das Formular ab, ohne das
Feld "Name" auszufüllen. Was passiert, und welches Attribut ist dafür verantwortlich?
<!-- time estimate: 8 min -->

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/` und registrieren Sie einen Studierenden
mit dem Namen "Tom Fischer", Alter `20` und der E-Mail "tom@example.com". Auf welcher Seite
landen Sie danach, und woran erkennen Sie, dass Ihre Eingaben tatsächlich in der Datenbank
gespeichert wurden (und nicht nur zurückgespiegelt)? Warum ist für diese Aktion POST die
richtige Methode und nicht GET? Wenn Sie einen anderen Port verwenden, passen Sie den Link
entsprechend an.
<!-- time estimate: 30 min -->

### Weiterführend

- [Working with forms](https://docs.djangoproject.com/en/stable/topics/forms/):
  Überblick über die Formularverarbeitung in Django
- [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/stable/ref/csrf/):
  Details zum CSRF-Schutz

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFQ::2]: Die `search`-View verwendet `Student.objects.filter(name=...)`
  statt `.get(...)`, eine Suche ohne Treffer liefert dadurch eine leere, aber gültige
  Liste (abgefangen mit `{% empty %}`) statt eines Absturzes; Student erkennt diesen
  bewussten Unterschied zur `get()`-Verwendung aus [PARTREF::django-model].
- [EREFR::7] + [EREFQ::5]: Die `register`-View legt bei POST per `Student.objects.create()`
  einen Datensatz an und leitet mit `redirect(reverse("student_detail", args=[student.id]))`
  auf dessen Detailseite weiter; Student erkennt an der angezeigten Detailseite, dass die
  Daten tatsächlich gespeichert (nicht nur zurückgespiegelt) wurden.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-form.md]

### Kommandoprotokoll
[PROT::ALT:django-form.prot]

[ENDINSTRUCTOR]
