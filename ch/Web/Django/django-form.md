title: Django Formularbehandlung
stage: beta
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
von der Suchanfrage bis zur Registrierung.
Diese Aufgabe führt die bisher getrennt behandelten Ebenen zusammen: Ein Formular wird in
einem Template dargestellt, seine Daten in einer View verarbeitet und über ein Model in der
Datenbank gespeichert.
[ENDSECTION]


[SECTION::instructions::detailed]
Sie arbeiten weiter mit der App `webapp`.
Aus den vorherigen Aufgaben stehen Ihnen dort bereits das `Student`-Model
([PARTREF::django-model]), Views mit URL-Routing ([PARTREF::django-view]) und das
Template-System ([PARTREF::django-template]) zur Verfügung.

Starten Sie für die folgenden Schritte in einer separaten Shell den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen.
Alle Befehle und Links unten verwenden den Port 8071; falls Sie den Server auf einem anderen
Port betreiben, passen Sie sie entsprechend an.

### HTML-Formulare: GET und POST

Die Grundelemente eines HTML-Formulars (`<form>`, `<input>`, `<button type="submit">`)
kennen Sie bereits aus [PARTREF::http-POST] und [PARTREF::html-Formulare], den Unterschied
zwischen den beiden Methoden GET und POST aus [PARTREF::http-GET] und [PARTREF::http-POST].
Das `method`-Attribut von `<form>`, mit dem ein Formular sich für eine der beiden entscheidet,
kennen Sie aus [PARTREF::http-POST] bereits als `method="POST"`; die unten durchgehend
verwendete Kleinschreibung `method="post"` ist gleichwertig, neu ist nur der Wert `get`.
Welche der beiden für ein bestimmtes Formular die richtige ist, beobachten Sie in dieser
Aufgabe an drei Beispielen selbst.

### GET-Formular: Suche

Als erstes konkretes Formular bauen Sie eine Suche nach Studierenden.
Da eine Suche den Server-Zustand nicht verändert, ist GET hier die passende Methode.
In [PARTREF::django-view] haben Sie GET-Parameter bereits mit `request.GET.get(key, default)`
gelesen, dort aber per `curl` von Hand angehängt.
Bei einem `<form method="get">` übernimmt der Browser das: Beim Absenden verpackt er jedes
`<input name="...">` als GET-Parameter, den Sie dann mit `request.GET.get(...)` auslesen.
Die Suche greift mit `Student.objects.filter(name=...)` auf die in [PARTREF::django-model]
definierten `Student`-Objekte zu, also mit derselben exakten Übereinstimmungssuche, die Sie
dort bereits kennengelernt haben.
Ein Formular mit GET-Methode hat folgende Bestandteile:

```html
<form action="ZIEL" method="get">
    <input type="text" name="FELDNAME" value="VOREINGESTELLTER_TEXT" placeholder="HINWEISTEXT">
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `action`: die URL, an die das Formular sendet, gesetzt mit `{% url %}`
- `method="get"`: sendet die Daten als GET-Parameter an die im `action`-Attribut angegebene URL
- `name`: der Schlüssel, unter dem der eingegebene Wert als GET-Parameter ankommt
- `value` (bei `<input type="text">`): der Text, der beim Anzeigen schon im Feld steht
- `placeholder`: Hinweistext, der nur angezeigt wird, solange das Feld leer ist, und beim
  Absenden nicht mitgeschickt wird

[ER] Schreiben Sie in `views.py` eine View-Funktion `search_get`, die den GET-Parameter `q`
ausliest (Standardwert leerer String), bei nichtleerem `q` mit
`Student.objects.filter(name=q)` sucht (sonst `[]`) und `search_get.html` mit `q` und
`results` im Context rendert.
Ruft man die View ganz ohne `q` auf, ist `q` leer und die Seite zeigt schlicht das leere
Formular.

[ER] Erstellen Sie `webapp/templates/search_get.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Suche`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h2>`) mit dem Text "Suchformular (GET)"
- darunter einem `<form>` mit `method="get"`, das an `{% url 'search_get' %}` sendet
- darin einem Text-Eingabefeld `name="q"` (Wert vorbelegt mit `{{ q }}`, Platzhaltertext
  "Suchbegriff") und einem Absende-Button mit dem Text "Suchen"
- darunter, nur wenn `q` gesetzt ist, einer `<ul>` mit `{% for %}` über `results`: je Treffer
  ein Link zur Detailseite (`{% url 'student_detail' student.id %}`) mit dem Namen
- im `{% empty %}`-Zweig dem Text `Keine Treffer für "{{ q }}"` (mit dem eingesetzten
  Suchbegriff)

[ER] Ergänzen Sie `urls.py` um die Route `search-get/` auf `search_get` (Name `search_get`).

[EC] Testen Sie die GET-Suche direkt mit `curl` und rufen Sie anschließend die Detailseite
des Treffers auf (der Suchbegriff ist URL-kodiert):

```bash
curl "http://127.0.0.1:8071/search-get/?q=Anna%20M%C3%BCller"
curl "http://127.0.0.1:8071/search-get/?q=Nichtvorhanden"
curl "http://127.0.0.1:8071/students/1/"
```

[EQ] Der erste `curl`-Aufruf liefert einen Link zur Detailseite von Anna Müller.
Woher weiß das Template `search_get.html`, welche ID es in
`{% url 'student_detail' student.id %}` einsetzen muss, und was bestätigt Ihnen der dritte
Aufruf (`/students/1/`) über diesen Link?

[EQ] Rufen Sie zusätzlich `http://127.0.0.1:8071/search-get/` im Browser auf und suchen Sie nach
dem exakten Namen eines bereits vorhandenen Studierenden (aus [PARTREF::django-model]).
Wie verändert sich die URL nach dem Absenden, und wo taucht Ihr Suchbegriff auf?
Suchen Sie anschließend nach einem Namen, den es nicht gibt: was wird angezeigt, warum führt
die erfolglose Suche nicht zu einem Fehler, und welches Template-Tag erzeugt die Meldung?
<!-- time estimate: 30 min -->

### POST-Formular und CSRF-Schutz

Bei einem POST-Formular verlangt Django ein zusätzliches Sicherheitsmerkmal: ein CSRF-Token.
**CSRF** (Cross-Site Request Forgery) bezeichnet einen Angriff, bei dem eine fremde Website
unbemerkt eine Aktion in Ihrem Namen auslöst, während Sie eingeloggt sind.
Um das zu verhindern, weist Django jeden POST ab, der kein gültiges Token mitschickt; eine
fremde Seite kann dieses Token nicht auslesen und daher kein gültiges Formular fälschen.
Das Tag `{% csrf_token %}` ist die Gegenseite davon: Es bettet das Token als verstecktes Feld
in Ihr eigenes Formular ein, damit dessen POSTs akzeptiert werden.
Deshalb gehört `{% csrf_token %}` in **jedes** POST-Formular.

[NOTICE]
In [PARTREF::django-view] hatten Sie die `post_data`-View versuchsweise mit `@csrf_exempt`
vom CSRF-Schutz ausgenommen, um sie ohne Formular testen zu können.
Ab jetzt arbeiten Sie mit echten Formularen und verwenden daher regulär `{% csrf_token %}`
statt `@csrf_exempt`.
[ENDNOTICE]

Ein Formular mit POST-Methode hat dieselben Bestandteile wie das GET-Formular, mit zwei
Unterschieden:

```html
<form action="ZIEL" method="post">
    {% csrf_token %}
    <input type="text" name="FELDNAME" value="VOREINGESTELLTER_TEXT" placeholder="HINWEISTEXT">
    <button type="submit">BESCHRIFTUNG</button>
</form>
```

- `method="post"`: sendet die Daten mit der HTTP-Methode POST statt als GET-Parameter; sie
  sind dann über `request.POST` statt über `request.GET` zugänglich
- `{% csrf_token %}`: steht unmittelbar nach dem öffnenden `<form>`-Tag und bettet das oben
  beschriebene CSRF-Token ein

[ER] Schreiben Sie in `views.py` eine View-Funktion `search_post`: Bei einem POST-Request
liest sie den POST-Parameter `q` mit `request.POST.get('q', '')` aus, sucht bei nichtleerem
`q` mit `Student.objects.filter(name=q)` (sonst `[]`) und rendert `search_post.html` mit `q`
und `results` im Context; bei jeder anderen Anfrage rendert sie `search_post.html` mit leerem
Context.

Die Fallunterscheidung nach `request.method` ist das übliche Django-Muster für Views, die ein
POST-Formular verarbeiten; bei `register` weiter unten brauchen Sie es erneut.

[ER] Erstellen Sie `webapp/templates/search_post.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Suche (POST)`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h2>`) mit dem Text "Suchformular (POST)"
- darunter einem `<form>` mit `method="post"`, das an `{% url 'search_post' %}` sendet
- unmittelbar nach dem öffnenden `<form>`-Tag `{% csrf_token %}`
- einem Text-Eingabefeld `name="q"` (Wert vorbelegt mit `{{ q }}`, Platzhaltertext
  "Suchbegriff") und einem Absende-Button mit dem Text "Suchen"
- darunter demselben `{% if q %}`/`{% for %}`/`{% empty %}`-Aufbau wie in `search_get.html`
  (mit demselben `Keine Treffer für "{{ q }}"`-Text)

[ER] Ergänzen Sie `urls.py` um die Route `search-post/` auf `search_post` (Name
`search_post`).

[EQ] Suchen Sie unter `http://127.0.0.1:8071/search-post/` nach demselben Namen wie in [EREFQ::2].
Worin unterscheidet sich die URL nach dem Absenden gegenüber dem GET-Formular?
<!-- time estimate: 15 min -->

Ein `curl`-Aufruf durchläuft kein Formular und bringt daher weder das CSRF-Cookie noch das
versteckte Feld mit, die Django zusammen erwartet.

[EC] Senden Sie per `curl` einen POST ohne Token direkt an die View.
Der erste Aufruf zeigt nur den Statuscode: `-o /dev/null` verwirft die Antwortseite,
`-w "%{http_code}\n"` gibt stattdessen den Statuscode aus.
Der zweite Aufruf wiederholt den POST und holt aus der Antwortseite die Begründung heraus,
die Django dort angibt:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST -d "q=Anna" http://127.0.0.1:8071/search-post/
curl -s -X POST -d "q=Anna" http://127.0.0.1:8071/search-post/ | grep -A2 "Reason given"
```

Entfernen Sie nun versuchsweise `{% csrf_token %}` aus `search_post.html` und laden Sie
`http://127.0.0.1:8071/search-post/` im Browser neu, damit das Formular ohne das Tag neu
aufgebaut wird; suchen Sie dann erneut nach einem Namen.
Achten Sie darauf, was die Seite meldet und welche Begründung sie angibt.
Lesen Sie zur Erklärung den Abschnitt "How it works" der
[Django-Doku zu Cross Site Request Forgery protection](https://docs.djangoproject.com/en/stable/ref/csrf/#how-it-works)
nach.
Fügen Sie `{% csrf_token %}` danach wieder in `search_post.html` ein.

[EQ] Welcher Statuscode kam beim `curl`-Aufruf zurück, und was ist Ihnen gerade im Browser
passiert, als `{% csrf_token %}` fehlte?
Django nennt in beiden Fällen eine Begründung, aber nicht dieselbe: woran liegt das?
Welche Komponente weist beide Aufrufe ab, und welche Rolle spielt `{% csrf_token %}` dabei?
<!-- time estimate: 15 min -->

### Registrierung mit Datenbank-Persistenz

Bisher haben die Formulare die Datenbank nur gelesen.
Jetzt schreiben Sie hinein: Ein Registrierungsformular legt über `Student.objects.create()`
(aus [PARTREF::django-model]) einen neuen Datensatz an und leitet anschließend auf dessen
Detailseite weiter.
Für die drei Formularfelder greifen Sie mit `request.POST['name']` (usw.) zu, also mit
eckigen Klammern statt mit `.get()` wie bei der Suche: Ein Feld, das im Request gar nicht
vorkommt, bricht die View dann mit einem `MultiValueDictKeyError` ab, statt still zu einem
leeren Wert zu werden.
Eine View, die bei POST einen Datensatz anlegt und dann weiterleitet, hat folgenden Aufbau:

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
E-Mail); die ID vergibt die Datenbank erst beim Anlegen und steht dort nicht drin.
Deshalb kann `objekt.id` erst **nach** dem Aufruf von `Student.objects.create(...)` verwendet
werden (am zurückgegebenen Objekt), nicht aus `request.POST` selbst.
[ENDNOTICE]

[ER] Schreiben Sie in `views.py` eine View-Funktion `register` nach diesem Schema: Bei einem
POST-Request legt sie mit `Student.objects.create()` einen neuen `Student` aus
`request.POST['name']`, `request.POST['age']` und `request.POST['email']` an und leitet auf
dessen Detailseite (Route `student_detail`) weiter; bei jeder anderen Anfrage rendert sie
`register.html` ohne Context.

[HINT::Was muss ich zusätzlich importieren?]
Für diese View brauchen Sie zwei Imports: `from django.shortcuts import redirect` und
`from django.urls import reverse`.
Beide hatten Sie beim Aufräumen in [PARTREF::django-template] entfernt, weil sie dort nicht
mehr gebraucht wurden.
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
- `required`: macht das Feld zur Pflichteingabe

[ER] Erstellen Sie `webapp/templates/register.html` als Kind-Template von `base.html`
(`{% extends "base.html" %}`, Titel `Registrierung`, Inhalt in `{% block content %}`) mit:

- einer Überschrift (`<h2>`) mit dem Text "Studierenden-Registrierung"
- darunter einem `<form>` mit `method="post"` (inklusive `{% csrf_token %}`), das an
  `{% url 'register' %}` sendet
- drei nach diesem Schema beschrifteten und verpflichtenden Eingabefeldern (`name`: Text,
  "Name"; `age`: Zahl, "Alter"; `email`: E-Mail, "E-Mail")
- einem Absende-Button mit dem Text "Registrieren"

[ER] Ergänzen Sie `urls.py` um die Route `register/` auf `register` (Name `register`).
<!-- time estimate: 15 min -->

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/` und registrieren Sie einen Studierenden mit
dem Namen "Tom Fischer", Alter `20` und der E-Mail "tom@example.com".
Auf welcher Seite landen Sie danach?
Rufen Sie anschließend zusätzlich `http://127.0.0.1:8071/students/` auf: Woran erkennen Sie
dort, dass Ihre Eingaben tatsächlich in der Datenbank gespeichert wurden (und nicht nur
zurückgespiegelt)?
Warum ist für die Registrierung POST die richtige Methode und nicht GET?

Führen Sie nun zwei weitere Absendeversuche durch, bei denen Sie das Feld "Name" jeweils leer
lassen: einen mit dem `required`-Attribut am Namensfeld, so wie es jetzt dasteht, und einen,
nachdem Sie das Attribut in `register.html` entfernt und die Seite neu geladen haben.
Alter und E-Mail füllen Sie dabei beide Male normal aus, denn dort steht `required` weiterhin.
Rufen Sie nach dem zweiten Versuch `http://127.0.0.1:8071/students/` auf.
Fügen Sie `required` danach wieder ein.

[EQ] Wie hat der Browser auf die beiden Absendeversuche jeweils reagiert?
Was zeigt `http://127.0.0.1:8071/students/` danach an, und was sagt Ihnen das darüber, wo die
Prüfung von `required` stattfindet?

[NOTICE]
Bei diesem Versuch ist ein `Student` mit leerem Namen in der Datenbank gelandet.
Löschen Sie diesen Datensatz jetzt wieder, mit `delete()` oder über die Admin-Oberfläche
(beides aus [PARTREF::django-model]), sonst steht er Ihnen im weiteren Verlauf dauerhaft in
der Studierendenliste.
[ENDNOTICE]

Dass ungültige Eingaben in der Datenbank landen, lässt sich nur durch serverseitige
Validierung verhindern, etwa mit Django-Forms (siehe "Working with forms" unter
Weiterführend).
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
### Fragen und Python-Dateien
[INCLUDE::ALT:django-form.md]

### Kommandoprotokoll
[PROT::ALT:django-form.prot]
[ENDINSTRUCTOR]
