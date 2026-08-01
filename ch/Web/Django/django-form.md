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

Sie arbeiten weiter mit der App `webapp`. Aus den vorherigen Aufgaben stehen Ihnen dort
bereits das `Student`-Model ([PARTREF::django-model]), Views mit URL-Routing
([PARTREF::django-view]) und das Template-System ([PARTREF::django-template]) zur Verfügung.

Starten Sie für die folgenden Schritte in einer separaten Shell den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen. Alle Befehle und Links unten
verwenden den Port 8071; falls Sie den Server auf einem anderen Port betreiben, passen Sie
sie entsprechend an.

### HTTP-Formulare: GET und POST

Die Grundelemente eines HTML-Formulars (`<form>`, `<input>`, `<button type="submit">`)
kennen Sie bereits aus [PARTREF::http-POST] und [PARTREF::html-Formulare]. Ein HTML-Formular
sendet seine Daten mit einer von zwei Methoden; welche zum Einsatz kommt, legt das
`method`-Attribut von `<form>` fest (`method="get"` oder `method="post"`):

- **GET**: wirkungsfrei ("safe", siehe [PARTREF::http-GET]), verändert den Server-Zustand
  nicht. Die Daten werden sichtbar an die URL angehängt (`?q=...`), geeignet für Anfragen
  wie eine Suche, die man auch als Link teilen können soll.
- **POST**: verändert den Server-Zustand (siehe [PARTREF::http-POST]), etwa beim Anlegen
  eines Datensatzes. Die Daten werden im Request-Body übertragen und erscheinen nicht in
  der URL.

### GET-Formular: Suche

Als erstes konkretes Formular bauen Sie eine Suche nach Studierenden. Da eine Suche den
Server-Zustand nicht verändert, ist GET hier die passende Methode. In [PARTREF::django-view]
haben Sie GET-Parameter bereits mit `request.GET.get(key, default)` gelesen, dort aber per
`curl` von Hand an die URL angehängt. Bei einem `<form method="get">` übernimmt der Browser
das für Sie: Beim Absenden hängt er jedes `<input name="...">` automatisch als `?name=wert`
an die im `action` angegebene URL an, genau die Parameter, die Sie mit
`request.GET.get(...)` auslesen. Die Suche greift auf die in [PARTREF::django-model]
definierten `Student`-Objekte zu, über `Student.objects.filter(name=...)`, dieselbe exakte
Übereinstimmungssuche, die Sie dort bereits kennengelernt haben. Ein Formular mit
GET-Methode hat folgende Bestandteile:

```html
<form action="ZIEL" method="get">
    <input type="text" name="FELDNAME" value="VOREINGESTELLTER_TEXT" placeholder="HINWEISTEXT">
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `action`: die Route, an die das Formular sendet, gesetzt mit `{% url %}`
- `method="get"`: sendet die Daten als GET-Parameter an die im `action` angegebene URL
- `name`: der Schlüssel, unter dem der eingegebene Wert als GET-Parameter ankommt
- `value` (bei `<input type="text">`): der Text, der beim Anzeigen schon im Feld steht
- `placeholder`: Hinweistext, der nur angezeigt wird, solange das Feld leer ist, und beim
  Absenden nicht mitgeschickt wird

[ER] Schreiben Sie in `views.py` eine View-Funktion `search`: liest den GET-Parameter `q`
aus (Standardwert leerer String), sucht bei nichtleerem `q` mit
`Student.objects.filter(name=q)` (sonst `[]`) und rendert `search_get.html` mit `q` und
`results` im Context. Ruft man die View ganz ohne `q` auf, ist `q` leer und die Seite zeigt
schlicht das leere Formular.

[ER] Erstellen Sie `webapp/templates/search_get.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Suche`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h1>`) mit dem Text "Suchformular (GET)"
- darunter einem `<form>` mit `method="get"`, das an `{% url 'search' %}` sendet
- darin einem Text-Eingabefeld `name="q"` (Wert vorbelegt mit `{{ q }}`, Platzhaltertext
  "Suchbegriff") und einem Absende-Button mit dem Text "Suchen"
- darunter, nur wenn `q` gesetzt ist, einer `<ul>` mit `{% for %}` über `results`: je Treffer
  ein Link zur Detailseite (`{% url 'student_detail' student.id %}`) mit dem Namen
- im `{% empty %}`-Zweig dem Text `Keine Treffer für "{{ q }}"` (mit dem eingesetzten
  Suchbegriff)

[ER] Ergänzen Sie `urls.py` um die Route: Pfad `search/` auf `search` (Name `search`).

[EC] Testen Sie die GET-Suche direkt mit `curl` (der Suchbegriff ist URL-kodiert):

```bash
curl "http://127.0.0.1:8071/search/?q=Anna%20M%C3%BCller"
curl "http://127.0.0.1:8071/search/?q=Nichtvorhanden"
curl "http://127.0.0.1:8071/students/1/"
```

[EQ] Der erste `curl`-Aufruf liefert einen Link zur Detailseite von Anna Müller. Woher weiß
das Template `search_get.html`, welche ID es in `{% url 'student_detail' student.id %}`
einsetzen muss, und was bestätigt Ihnen der dritte Aufruf (`/students/1/`) über diesen Link?

[EQ] Rufen Sie zusätzlich `http://127.0.0.1:8071/search/` im Browser auf und suchen
Sie nach dem exakten Namen eines bereits vorhandenen Studierenden (aus
[PARTREF::django-model]). Wie verändert sich die URL nach dem Absenden, und wo taucht Ihr
Suchbegriff auf? Suchen Sie anschließend nach einem Namen, den es nicht gibt: was wird
angezeigt, und welches Template-Tag sorgt dafür, dass die Seite dabei nicht fehlerhaft
wird?
<!-- time estimate: 30 min -->

### POST-Formular und CSRF-Schutz

Bei einem POST-Formular verlangt Django ein zusätzliches Sicherheitsmerkmal: das
`{% csrf_token %}`-Tag. **CSRF** (Cross-Site Request Forgery) bezeichnet einen Angriff, bei
dem eine fremde Website unbemerkt eine Aktion in Ihrem Namen auslöst, während Sie
eingeloggt sind. Um das zu verhindern, weist Django jeden POST ab, der kein gültiges Token
mitschickt; eine fremde Seite kann dieses Token nicht auslesen und daher kein gültiges
Formular fälschen. Das Tag `{% csrf_token %}` ist die Gegenseite davon: Es bettet das Token
als verstecktes Feld in Ihr eigenes Formular ein, damit dessen POSTs akzeptiert werden.
Deshalb gehört `{% csrf_token %}` in **jedes** POST-Formular.

[NOTICE]
In [PARTREF::django-view] hatten Sie die `post_data`-View versuchsweise mit `@csrf_exempt`
vom CSRF-Schutz ausgenommen, um sie ohne Formular testen zu können. Ab jetzt arbeiten Sie
mit echten Formularen und verwenden daher regulär `{% csrf_token %}` statt `@csrf_exempt`.
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

[ER] Schreiben Sie in `views.py` eine View-Funktion `search_post`: Bei einem POST-Request
liest sie den POST-Parameter `q` mit `request.POST.get('q', '')` aus, sucht bei nichtleerem
`q` mit `Student.objects.filter(name=q)` (sonst `[]`) und rendert `search_post.html` mit `q`
und `results` im Context; bei jeder anderen Anfrage rendert sie `search_post.html` mit
leerem Context.

[ER] Erstellen Sie `webapp/templates/search_post.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Suche (POST)`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h1>`) mit dem Text "Suchformular (POST)"
- darunter einem `<form>` mit `method="post"`, das an `{% url 'search_post' %}` sendet
- unmittelbar nach dem öffnenden `<form>`-Tag `{% csrf_token %}`
- einem Text-Eingabefeld `name="q"` (Wert vorbelegt mit `{{ q }}`, Platzhaltertext
  "Suchbegriff") und einem Absende-Button mit dem Text "Suchen"
- darunter demselben `{% if q %}`/`{% for %}`/`{% empty %}`-Aufbau wie in `search_get.html`
  (mit demselben `Keine Treffer für "{{ q }}"`-Text)

[ER] Ergänzen Sie `urls.py` um die Route `search-post/` auf `search_post` (Name
`search_post`).

[EQ] Suchen Sie unter `http://127.0.0.1:8071/search-post/` nach demselben Namen wie in
[EREFQ::2]. Worin unterscheidet sich die URL nach dem Absenden gegenüber dem GET-Formular?

<!-- time estimate: 15 min -->

Ein `curl`-Aufruf durchläuft kein Formular und liefert daher kein gültiges CSRF-Token mit.

[EC] Senden Sie per `curl` einen POST ohne Token direkt an die View (nur der Statuscode wird
ausgegeben):

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST -d "q=Anna" http://127.0.0.1:8071/search-post/
```

Entfernen Sie nun versuchsweise `{% csrf_token %}` aus `search_post.html` und suchen Sie
danach im Browser unter `http://127.0.0.1:8071/search-post/` erneut nach einem Namen: Jetzt
wird auch dieses eigene, regulär ausgefüllte Formular abgewiesen. Lesen Sie zur
Erklärung den Abschnitt "How it works" der
[Django-Doku zu Cross Site Request Forgery protection](https://docs.djangoproject.com/en/stable/ref/csrf/#how-it-works)
nach. Fügen Sie `{% csrf_token %}` danach wieder in `search_post.html` ein.

[EQ] Welcher Statuscode kam beim `curl`-Aufruf zurück, und was ist Ihnen gerade im Browser
passiert, als `{% csrf_token %}` fehlte? Welche Komponente weist beide Aufrufe ab, und
welche Rolle spielt `{% csrf_token %}` dabei, wenn nicht die eines Türstehers?
<!-- time estimate: 15 min -->

### Registrierung mit Datenbank-Persistenz

Bisher haben die Formulare die Datenbank nur gelesen. Jetzt schreiben Sie hinein:
Ein Registrierungsformular legt über `Student.objects.create()` (aus [PARTREF::django-model])
einen neuen Datensatz an und leitet anschließend auf dessen Detailseite weiter. Da Name,
Alter und E-Mail hier echte Pflichtfelder sind, greifen Sie direkt mit `request.POST['feld']`
zu (anders als bei der optionalen Suche mit `.get()`): Fehlt das Feld komplett, wirft dieser
Zugriff einen `KeyError`, statt stillschweigend einen leeren Wert zu liefern. Eine View, die bei
POST einen Datensatz anlegt und dann weiterleitet, hat folgenden Aufbau:

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
`from django.urls import reverse`. Beide hatten Sie beim Aufräumen in
[PARTREF::django-template] entfernt, weil sie dort nicht mehr gebraucht wurden.
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
- `required`: macht das Feld zur Pflichteingabe; das prüft aber nur der Browser vor dem
  Absenden, der Server bekommt davon nichts mit

[ER] Erstellen Sie `webapp/templates/register.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Registrierung`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h1>`) mit dem Text "Studierenden-Registrierung"
- darunter einem `<form>` mit `method="post"` (inklusive `{% csrf_token %}`), das an
  `{% url 'register' %}` sendet
- drei nach diesem Schema beschrifteten und verpflichtenden Eingabefeldern (`name`: Text,
  "Name"; `age`: Zahl, "Alter"; `email`: E-Mail, "E-Mail")
- einem Absende-Button mit dem Text "Registrieren"

[ER] Ergänzen Sie `urls.py` um die Route `register/` auf `register` (Name `register`).
<!-- time estimate: 15 min -->

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/` und senden Sie das Formular ab, ohne das
Feld "Name" auszufüllen. Was passiert im Browser?

Entfernen Sie nun versuchsweise das `required`-Attribut beim Namensfeld in `register.html`
und senden Sie das Formular im Browser erneut ab, wieder ohne das Feld "Name" auszufüllen.
Rufen Sie anschließend `http://127.0.0.1:8071/students/` auf. Fügen Sie `required` danach
wieder ein.

[EQ] Was zeigt `http://127.0.0.1:8071/students/` jetzt an? Was sagt Ihnen das über die
serverseitige Prüfung von Pflichtfeldern?

Löschen Sie den dabei entstandenen Datensatz anschließend wieder, mit `delete()` oder über
die Admin-Oberfläche (beides aus [PARTREF::django-model]).

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/` und registrieren Sie einen Studierenden
mit dem Namen "Tom Fischer", Alter `20` und der E-Mail "tom@example.com". Auf welcher Seite
landen Sie danach? Rufen Sie anschließend zusätzlich `http://127.0.0.1:8071/students/` auf:
Woran erkennen Sie dort, dass Ihre Eingaben tatsächlich in der Datenbank gespeichert wurden
(und nicht nur zurückgespiegelt)? Warum ist für die Registrierung POST die richtige Methode
und nicht GET?
<!-- time estimate: 15 min -->

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

- [EREFC::2] + [EREFQ::4]: Sowohl der `curl`-Aufruf ohne Token als auch das eigene Formular
  ohne `{% csrf_token %}` werden mit Statuscode 403 abgewiesen; Student erkennt, dass die
  Abweisung von Djangos `CsrfViewMiddleware` kommt, unabhängig davon, was im Template steht,
  und dass `{% csrf_token %}` umgekehrt dafür sorgt, dass legitime Formulare gerade nicht
  abgewiesen werden.
- [EREFR::7] + [EREFQ::7]: Die `register`-View legt bei POST per `Student.objects.create()`
  einen Datensatz an und leitet mit `redirect(reverse("student_detail", args=[student.id]))`
  auf dessen Detailseite weiter; Student erkennt am zusätzlichen Aufruf von `/students/`, dass
  der neue Studierende dort tatsächlich in der Datenbank steht (nicht nur zurückgespiegelt
  wurde).
- [EREFQ::6]: Nach Entfernen von `required` legt das Formular trotz leerem Namensfeld einen
  `Student` mit leerem `name` an; Student erkennt, dass `required` reine Browser-Prüfung ist
  und die View selbst überhaupt nichts validiert.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-form.md]

### Kommandoprotokoll
[PROT::ALT:django-form.prot]

[ENDINSTRUCTOR]
