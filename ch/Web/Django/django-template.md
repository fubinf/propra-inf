title: Django Template System
stage: alpha
timevalue: 2.25
difficulty: 2
requires: django-view
assumes: html-erste-Schritte, html-Semantik, css-Einführung, curl
---

[SECTION::goal::idea,experience]

- Ich verstehe, wie Templates die Darstellung (HTML) von der Programmlogik (Python) trennen.
- Ich kann Daten mit Template-Variablen, Bedingungen, Schleifen und Filtern dynamisch
  darstellen.
- Ich kann mit Template-Vererbung, statischen Dateien und namensbasierten Links
  wiederverwendbare Seitenstrukturen aufbauen.

[ENDSECTION]

[SECTION::background::default]

Wenn eine View HTML direkt als Python-String zusammenbaut, vermischen sich Darstellung und
Programmlogik; das wird schnell unübersichtlich und ist schwer zu pflegen.
Das Django Template System trennt beides: Die View liefert nur die Daten, das Template
bestimmt, wie sie als HTML dargestellt werden.
So können Layout und Logik unabhängig voneinander bearbeitet werden.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`.
In [PARTREF::django-project] haben Sie bereits ein erstes Template `hello.html` angelegt, das
von der `hello`-View mit `render()` ausgeliefert wird.
Darauf bauen die folgenden Schritte auf.

Starten Sie für die folgenden Schritte den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen, damit Sie die Seiten im Browser
bzw. mit `curl` aufrufen können.
Alle URLs und Befehle unten verwenden den Port 8071; falls Sie den Entwicklungsserver auf
einem anderen Port betreiben, passen Sie sie entsprechend an.

### Aufräumen: nicht mehr benötigte Views und Routen

[PARTREF::django-view] hat mehrere Views nur zu Demonstrationszwecken eingeführt
(`get_params`, `post_data`, `request_info`, `responses`, `redirect_target`,
`redirect_example`, `student_redirect`); keine davon wird in den folgenden Aufgaben noch
gebraucht.

[ER] Entfernen Sie diese sieben Funktionen aus `views.py`, dazu die dadurch unnötig
gewordenen Importe sowie ihre Routen aus `urls.py`.
Behalten Sie `hello` und `student_detail`, die Sie weiterhin brauchen.

[HINT::Welche Importe werden jetzt nicht mehr gebraucht?]
Gehen Sie die `import`-Zeilen am Dateianfang einzeln durch und suchen Sie für jeden Namen, ob
er im verbliebenen Code überhaupt noch vorkommt.
Genau drei Namen werden nur von den entfernten Funktionen benutzt.
[ENDHINT]
<!-- time estimate: 5 min -->

### Template-Variablen und Context

Beim Aufruf von `render()` haben Sie bisher nur eine einzige Variable (`message`) an das
Template übergeben.
Wie Sie aus [PARTREF::django-project] wissen, hat `render()` die Form

```python
render(request, template_name, context)
```

Das dritte Argument, der **Context**, ist ein Dictionary, das Daten von der View an das
Template weitergibt und beliebig viele Variablen enthalten kann, nach folgendem Schema:

```python
def beispiel_view(request):
    context = {
        'farbe': 'blau',
        'anzahl': 3,
    }
    return render(request, 'beispiel.html', context)
```

[ER] Ersetzen Sie die `hello`-View in `views.py` durch eine Version, deren `context`-Dictionary
drei Variablen an `render()` übergibt: `greeting` mit dem Wert `Hallo Django Templates!`,
`user_name` mit dem Wert `Anna` und `is_logged_in` mit dem Wert `True`.

Ein Template ist eine HTML-Datei (HTML-Grundelemente wie `<h1>`, `<p>` und Listen kennen Sie
aus [PARTREF::html-erste-Schritte]), in der zusätzlich die Template-Syntax vorkommt.
Die Syntax `{{ variablenname }}` setzt an der jeweiligen Stelle den Wert aus dem Context ein,
nach folgendem Schema:

```html
<p>{{ titel }}</p>
```

Ersetzen Sie zunächst den Inhalt von `hello.html` durch die folgende Grundstruktur; sie
ergänzt die einfache Version aus [PARTREF::django-project] um `lang`-Angabe und
`<meta charset>` und trägt einen zur Aufgabe passenden Titel.
In den folgenden Schritten ändern Sie jeweils nur den `<body>`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Django Template Demo</title>
</head>
<body>
</body>
</html>
```

[ER] Fügen Sie in den `<body>` von `hello.html` `greeting` als Überschrift `<h1>` und
`user_name` darunter in einem Absatz `<p>` ein (jeweils mit der `{{ ... }}`-Syntax).

[EQ] Fügen Sie testweise irgendwo in `hello.html` die Zeile `<p>[{{ nichtvorhanden }}]</p>`
ein; `nichtvorhanden` existiert im `context` gar nicht.
Die eckigen Klammern machen sichtbar, wo der Wert stehen würde.
Rufen Sie `http://127.0.0.1:8071/` im Browser auf: Was steht zwischen den Klammern, und wie
unterscheidet sich dieses Verhalten von einem Zugriff auf einen nicht vorhandenen
Dictionary-Schlüssel in reinem Python?
Entfernen Sie die Testzeile anschließend wieder.
<!-- time estimate: 15 min -->

### Bedingte Darstellung mit `{% if %}`

Neben Variablen (`{{ ... }}`) kennt die Template-Sprache auch Tags für Logik, geschrieben mit
`{% ... %}`.
Das `{% if %}`-Tag zeigt Inhalte nur unter einer Bedingung an, mit optionalem
`{% else %}`-Zweig, nach folgendem Schema:

```html
{% if bedingung %}
    <p>Text, wenn die Bedingung zutrifft</p>
{% else %}
    <p>Text sonst</p>
{% endif %}
```

[ER] Erweitern Sie den `<body>` von `hello.html` um eine bedingte Darstellung, die von der
Variablen `is_logged_in` abhängt: Wenn sie wahr ist, zeigen Sie einen Absatz `<p>` mit dem
Text "Willkommen zurück, " gefolgt vom Wert von `user_name` und einem Ausrufezeichen;
andernfalls einen Absatz `<p>` mit dem Text "Bitte melden Sie sich an."

[EQ] Lesen Sie in der Doku zu
[Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#std-templatetag-if)
den Abschnitt zu `if` nach.
Unter welchen Bedingungen behandelt `{% if %}` einen Wert als wahr?
Setzen Sie `is_logged_in` in der View danach nacheinander auf zwei Werte, die nach dieser
Regel falsch sind, ohne `False` zu sein, und aktualisieren Sie jeweils die Seite.
Welche Werte haben Sie gewählt, und welcher Zweig erscheint?
Setzen Sie `is_logged_in` anschließend wieder auf `True`.
<!-- time estimate: 15 min -->

### Schleifen mit `{% for %}`

Neben Bedingungen kennt die Template-Sprache mit `{% for %}` auch ein Tag zum Iterieren über
Listen, ähnlich aufgebaut wie das `{% if %}`-Tag aus dem vorigen Abschnitt: ein einleitendes
Tag, dazwischen der wiederholte Inhalt, ein abschließendes Tag.
Lesen Sie in der Doku zu
[Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#std-templatetag-for)
den Abschnitt zu `for` nach, insbesondere den Zugriff auf das aktuelle Element im
Schleifenkörper und das optionale `{% empty %}`-Tag für den Fall einer leeren Liste.

[ER] Ergänzen Sie den `context` der `hello`-View um eine Liste `hobbies` mit den Werten
`Programmieren`, `Lesen`, `Sport`.
Stellen Sie `hobbies` im `<body>` von `hello.html` innerhalb des
`{% if is_logged_in %}`-Zweigs dar: eine Überschrift "Ihre Hobbys:" (`<h2>`), darunter die
Hobbys als `<ul>`-Liste mit `{% for %}` und einem `{% empty %}`-Zweig, der für eine leere
Liste "Keine Hobbys angegeben" in einem Listenelement anzeigt.

[EQ] Setzen Sie `hobbies` in der View auf eine leere Liste `[]` und aktualisieren Sie die
Seite; entfernen Sie `hobbies` danach ganz aus dem `context` und aktualisieren Sie erneut.
Was wird in den beiden Fällen angezeigt, und was haben sie mit Ihrer Beobachtung aus
[EREFQ::1] gemeinsam?

Tragen Sie `hobbies` in der View anschließend wieder mit der ursprünglichen Liste
(`['Programmieren', 'Lesen', 'Sport']`) ein, bevor Sie fortfahren.
<!-- time estimate: 15 min -->

### Echte Daten aus dem Model mit Filtern darstellen

Bisher haben Sie nur Testdaten direkt im `context` der View angegeben.
Wie Sie aus [PARTREF::django-model] wissen, liefert `Student.objects.all()` alle gespeicherten
`Student`-Objekte aus der Datenbank; im Template lässt sich das Ergebnis genauso wie eine
Liste mit `{% for %}` durchlaufen.

Um Werte beim Anzeigen aufzubereiten, bietet die Template-Sprache zusätzlich **Filter**: Ein
Filter wird mit `|` hinter einer Variablen angewendet, nach folgendem Schema:

```html
{{ variablenname|filtername }}
```

Für die Studierendenliste sind drei Filter nützlich:

- `upper`: wandelt Text durchgehend in Großbuchstaben um.
- `default:"Noch keine Note"`: zeigt einen Ersatztext, falls der Wert leer ist oder als
  falsch gilt (z. B. `None`, leerer String, `0`; `grade_average` ist laut
  [PARTREF::django-model] optional und daher oft `None`).
- `yesno:"Aktiv,Inaktiv"`: gibt je nach Wahrheitswert einen von zwei wählbaren Texten aus.

[ER] Schreiben Sie in `views.py` eine View-Funktion `students_list`, die mit `.objects.all()`
alle `Student`-Objekte lädt und sie unter dem Context-Schlüssel `students` an das Template
`students_list.html` übergibt.

[ER] Legen Sie `webapp/templates/students_list.html` an, mit derselben Grundstruktur wie
`hello.html` (`<!DOCTYPE>`, `<html lang="de">`, `<head>` mit `<meta charset>` und dem Titel
"Studierendenliste", `<body>`).
Zeigen Sie im `<body>` eine Überschrift "Alle Studierenden" (`<h1>`), darunter die
Studierenden als `<ul>`-Liste mit `{% for %}`.
Jedes Listenelement enthält den Namen (mit `upper`), gefolgt von " — Note: " und dem
Notendurchschnitt (mit `default:"Noch keine Note"`), gefolgt von " — " und dem Aktivstatus
(mit `yesno:"Aktiv,Inaktiv"`).
Ergänzen Sie einen `{% empty %}`-Zweig, der "Noch keine Studierenden registriert." in einem
Listenelement anzeigt.

[ER] Fügen Sie in `urls.py` die Route für `students_list` hinzu: Pfad `students/`, Ziel
`students_list`, Name `students_list`.

Öffnen Sie `http://127.0.0.1:8071/admin/` und melden Sie sich mit Ihrem Superuser an (siehe
[PARTREF::django-model]).
Tragen Sie dort für Anna Müller den Notendurchschnitt `2.3` und für Peter Klein `1.7` ein
(mit Punkt als Dezimaltrennzeichen, nicht mit Komma); entfernen Sie außerdem bei Peter Klein
den Haken bei `is_active`.
Lassen Sie `grade_average` bei Lisa Weber leer.

[EQ] Rufen Sie anschließend `http://127.0.0.1:8071/students/` auf.
Was erscheint bei Lisa Weber (kein Notendurchschnitt) und bei Peter Klein (nicht aktiv)
anstelle der rohen Werte, und welcher Filter ist jeweils verantwortlich?
<!-- time estimate: 25 min -->

`upper`, `default` und `yesno` sind nur drei von vielen eingebauten Filtern.

[EQ] Lesen Sie die vollständige Liste in der
[Django-Doku zu Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#built-in-filter-reference)
durch (Abschnitt "Built-in filter reference").
Welchen Filter finden Sie dort am nützlichsten oder interessantesten, und warum?
<!-- time estimate: 10 min -->

### Template-Vererbung

Sie haben jetzt zwei Seiten, `hello.html` und `students_list.html`, die beide ihren
kompletten `<head>`-Bereich einzeln ausschreiben.

[EQ] Wenn Sie diesen `<head>`-Bereich später ändern wollen, etwa um eine CSS-Datei
einzubinden: An welchen Stellen müssten Sie die Änderung vornehmen?
Überlegen Sie, welches Problem daraus entsteht, wenn weitere Seiten hinzukommen.

Template-Vererbung löst genau dieses Problem: Ein **Basis-Template** definiert die
gemeinsame Struktur und markiert mit `{% block %}` die Stellen, die einzelne Seiten füllen.
Ein **Kind-Template** übernimmt die Struktur mit `{% extends %}` und überschreibt nur die
Blöcke, nach folgendem Schema:

```html
<!-- basis.html -->
<body>{% block inhalt %}{% endblock %}</body>
```

```html
<!-- kind.html -->
{% extends "basis.html" %}
{% block inhalt %}Mein Seiteninhalt{% endblock %}
```

Das vollständige Basis-Template mit Kopf- und Fußbereich ist hier vorgegeben; es verwendet
semantische HTML-Elemente wie `<header>` und `<footer>` (siehe [PARTREF::html-Semantik]):

[ER] Erstellen Sie in `webapp/templates/` die Datei `base.html`:

[SNIPPET::ALT::django_template_base]

[ER] Wandeln Sie `hello.html` in ein Kind-Template um: Ersetzen Sie `<!DOCTYPE>`, `<html>`,
`<head>` und die `<body>`-Umschließung durch `{% extends "base.html" %}` und packen Sie
Ihren bisherigen `<body>`-Inhalt (Überschrift, Bedingungsblock mit Hobbys) in einen Block
`content`.
Stufen Sie dabei die Überschrift `<h1>{{ greeting }}</h1>` zu `<h2>{{ greeting }}</h2>`
herab: Das `<h1>` der Seite kommt jetzt aus `base.html`, ein zweites `<h1>` wäre nicht mehr
korrekt.
Stufen Sie auch die Unterüberschrift `<h2>Ihre Hobbys:</h2>` zu `<h3>Ihre Hobbys:</h3>` herab,
damit sie weiterhin der (jetzt eine Ebene tieferen) Überschrift des Inhaltsblocks
untergeordnet bleibt.

[ER] Wandeln Sie `students_list.html` auf dieselbe Weise in ein Kind-Template um: Stufen Sie
dabei ebenso die Überschrift `<h1>Alle Studierenden</h1>` zu `<h2>Alle Studierenden</h2>`
herab, und überschreiben Sie zusätzlich `{% block title %}` mit "Studierendenliste".

[HINT::Wie hängen die Blocknamen in `base.html` und den Kind-Templates zusammen?]
Ein `{% block content %}` im Kind-Template ersetzt genau den gleichnamigen
`{% block content %}` im Basis-Template; die Namen müssen also übereinstimmen.
Blöcke, die das Kind-Template nicht überschreibt (z. B. wenn Sie `{% block title %}`
weglassen), behalten den Inhalt aus `base.html` als Standard.
Sie füllen also nur die Blöcke, die sich pro Seite unterscheiden.
[ENDHINT]

[EC] Sehen Sie sich den Quelltext beider Seiten an:

```bash
curl -s http://127.0.0.1:8071/
curl -s http://127.0.0.1:8071/students/
```
<!-- time estimate: 20 min -->

### Statische Dateien einbinden

Neben der gemeinsamen Struktur gehört zum Aussehen einer Seite meist auch CSS (Syntax und
Einbindung kennen Sie aus [PARTREF::css-Einführung]).
Solche CSS-, JavaScript- und Bilddateien werden als **statische Dateien** bezeichnet.
Django findet sie automatisch im Ordner `static/` einer registrierten App, analog dazu, wie
Templates im `templates/`-Ordner gefunden werden.
Im Template bindet das `{% static %}`-Tag sie ein; dazu muss `{% load static %}` am
Dateianfang stehen, nach folgendem Schema:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'pfad/zur/datei.css' %}">
```

[ER] Erstellen Sie das Verzeichnis `webapp/static/css` und legen Sie darin `style.css` mit
folgendem CSS an:

[SNIPPET::ALT::django_template_css]

Beenden Sie danach den Entwicklungsserver mit Strg+C und starten Sie ihn neu.

[ER] Binden Sie die CSS-Datei in `base.html` ein: Setzen Sie `{% load static %}` an den
Dateianfang und fügen Sie im `<head>` ein `<link>`-Element ein, das die Datei
`css/style.css` per `{% static %}` referenziert.

[HINT::Wozu war der Neustart des Entwicklungsservers nötig?]
Django prüft nur beim Start, welche App einen `static/`-Ordner besitzt; ein danach angelegter
Ordner bleibt bis zum nächsten Start unsichtbar.
Ohne Neustart liefert der Server die Datei deshalb nicht aus, obwohl das `<link>`-Element im
HTML steht und die Seite unverändert aussieht.
Nachprüfen lässt sich das jederzeit mit
`curl -s http://127.0.0.1:8071/static/css/style.css`.
[ENDHINT]

[EQ] Rufen Sie `http://127.0.0.1:8071/students/` auf: Die Seite ist jetzt formatiert, obwohl
`students_list.html` selbst weder CSS noch ein `{% load %}` enthält.
Entfernen Sie nun versuchsweise die Zeile `{% load static %}` aus `base.html`, laden Sie die
Seite erneut und fügen Sie die Zeile danach wieder ein.
Welche Fehlermeldung erscheint, und in welcher Datei müsste ein `{% load static %}` stehen,
wenn ein Kind-Template selbst ein `{% static %}` verwenden wollte?
<!-- time estimate: 10 min -->

### Navigation mit `{% url %}`

Damit Nutzer zwischen den Seiten wechseln können, braucht `base.html` eine Navigation:
das semantische Element `<nav>` markiert einen Block mit Navigationslinks.
Für die Links verwenden Sie nicht fest codierte Pfade wie `href="/students/"`, sondern das
`{% url %}`-Tag mit dem Routennamen; das ist die Template-Seite derselben namensbasierten
Auflösung, deren Python-Seite (`reverse()`) Sie in [PARTREF::django-view] kennengelernt
haben, nach folgendem Schema:

```html
<a href="{% url 'routenname' %}">Linktext</a>
```

[ER] Erweitern Sie `base.html` um eine `<nav>` im `<header>`, die mit `{% url %}` zwei Links
setzt: einen auf die Route `hello` mit dem Text "Start" und einen auf die Route
`students_list` mit dem Text "Studierendenliste".

Auch die Detailseiten der Studierenden lassen sich so verlinken.
Deren Route `student_detail` (aus [PARTREF::django-view]) braucht allerdings ein Argument, die
`student_id`, und das obige Schema deckt nur die argumentlose Form ab.
Wie sich einem `{% url %}`-Aufruf ein Argument mitgeben lässt, finden Sie im Abschnitt zu
`url` der
[Django-Doku zu Built-in template tags](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#url).

[ER] Verlinken Sie in `students_list.html` zusätzlich jeden Studierendennamen mit `{% url %}`
auf dessen Detailseite.

[EC] Sehen Sie sich erneut den Quelltext an und achten Sie auf die `<nav>`-Links sowie die
Links zu den Detailseiten:

```bash
curl -s http://127.0.0.1:8071/students/
```

[EQ] Zu welchen Pfaden wurden die `{% url %}`-Links im Quelltext aufgelöst?
In [PARTREF::django-view] haben Sie mit `reverse()` dasselbe in einer View getan.
Warum ist es nützlich, dieselbe namensbasierte Auflösung sowohl in Python (`reverse()`) als
auch im Template (`{% url %}`) zur Verfügung zu haben?

Öffnen Sie zum Abschluss `http://127.0.0.1:8071/` im Browser und klicken Sie über die
`<nav>`-Links zwischen Startseite und Studierendenliste hin und her.
<!-- time estimate: 20 min -->

### Weiterführend

- [Templates](https://docs.djangoproject.com/en/stable/topics/templates/):
  Überblick über die Template-Sprache
- [Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/):
  Referenz zu allen Tags und Filtern
- [Managing static files](https://docs.djangoproject.com/en/stable/howto/static-files/):
  Anleitung zu statischen Dateien

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-template.md]

### Kommandoprotokoll
[PROT::ALT:django-template.prot]

[ENDINSTRUCTOR]
