title: Django Template System
stage: alpha
timevalue: 2
difficulty: 2
requires: django-view
assumes: html-erste-Schritte, html-Semantik, css-Einführung, curl
---

[SECTION::goal::idea,experience]

- Ich verstehe, wie Templates die Darstellung (HTML) von der Programmlogik (Python) trennen.
- Ich kann Daten mit Template-Variablen, Bedingungen, Schleifen und Filtern dynamisch
  darstellen.
- Ich kann mit Template-Vererbung und statischen Dateien wiederverwendbare Seitenstrukturen
  aufbauen.

[ENDSECTION]

[SECTION::background::default]

Wenn eine View HTML direkt als Python-String zusammenbaut, vermischen sich Darstellung und
Programmlogik; das wird schnell unübersichtlich und ist schwer zu pflegen. Das Django
Template System trennt beides: Die View liefert nur die Daten, das Template bestimmt, wie
sie als HTML dargestellt werden. So können Layout und Logik unabhängig voneinander bearbeitet
werden.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`. In [PARTREF::django-project] haben Sie bereits ein
erstes Template `hello.html` angelegt, das die `hello`-View mit `render()` anzeigt. Darauf
bauen die folgenden Schritte auf.

Starten Sie für die folgenden Schritte den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen, damit Sie die Seiten im Browser
bzw. mit `curl` aufrufen können.

### Aufräumen: nicht mehr benötigte Views

[PARTREF::django-view] hat mehrere Views nur zu Demonstrationszwecken eingeführt
(`get_params`, `post_data`, `request_info`, `responses`, `redirect_target`,
`redirect_example`, `student_redirect`); keine davon wird in den folgenden Aufgaben noch
gebraucht.

Entfernen Sie diese sieben Funktionen aus `views.py` sowie ihre Routen aus `urls.py`.
Behalten Sie `hello` und `student_detail`, die brauchen Sie weiterhin.

### Template-Variablen und Context

Beim Aufruf von `render()` haben Sie bisher nur eine einzige Variable (`message`) an das
Template übergeben. Zur Erinnerung aus [PARTREF::django-project] hat `render()` die Form

```
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
aus [PARTREF::html-erste-Schritte]), in der zusätzlich die Template-Syntax vorkommt. Die
Syntax `{{ variablenname }}` setzt an der jeweiligen Stelle den Wert aus dem Context ein, nach
folgendem Schema:

```html
<p>{{ titel }}</p>
```

Ersetzen Sie zunächst den Inhalt von `hello.html` durch die folgende Grundstruktur (gegenüber
der einfachen Version aus [PARTREF::django-project] mit `lang`-Angabe, `<meta charset>` und
passendem Titel). In den folgenden Schritten ändern Sie jeweils nur den `<body>`:

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

[EQ] Rufen Sie `http://127.0.0.1:8071/` im Browser auf. Welche Werte erscheinen anstelle
der Platzhalter `{{ greeting }}` und `{{ user_name }}`, und woher stammen diese Werte? Wenn
Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- time estimate: 15 min -->

### Bedingte Darstellung mit `{% if %}`

Neben Variablen (`{{ ... }}`) kennt die Template-Sprache auch Tags für Logik, geschrieben mit
`{% ... %}`. Das `{% if %}`-Tag zeigt Inhalte nur unter einer Bedingung an, mit optionalem
`{% else %}`-Zweig, nach folgendem Schema:

```html
{% if bedingung %}
    <p>Text, wenn die Bedingung zutrifft</p>
{% else %}
    <p>Text sonst</p>
{% endif %}
```

[ER] Erweitern Sie den `<body>` von `hello.html` um eine bedingte Darstellung, die von der
Variablen `is_logged_in` abhängt: Wenn sie zutrifft, zeigen Sie einen Absatz `<p>` mit dem
Text "Willkommen zurück, " gefolgt vom Wert von `user_name` und einem Ausrufezeichen;
andernfalls einen Absatz `<p>` mit dem Text "Bitte melden Sie sich an.".

[EQ] Ändern Sie in der View `is_logged_in` auf `False` und aktualisieren Sie die Seite. Was
wird jetzt angezeigt, und welcher Teil des Templates ist dafür verantwortlich?
<!-- time estimate: 10 min -->

### Schleifen mit `{% for %}`

Neben Bedingungen kennt die Template-Sprache mit `{% for %}` auch ein Tag zum Iterieren über
Listen, ähnlich aufgebaut wie das `{% if %}`-Tag aus dem vorigen Abschnitt: ein einleitendes
Tag, dazwischen der wiederholte Inhalt, ein abschließendes Tag. Lesen Sie in der Doku zu
[Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#std-templatetag-for)
den Abschnitt zu `for` nach, insbesondere den Zugriff auf das aktuelle Element im
Schleifenkörper und das optionale `{% empty %}`-Tag für den Fall einer leeren Liste.

[ER] Setzen Sie `is_logged_in` in der View wieder auf `True` und ergänzen Sie den `context`
um eine Liste `hobbies` mit den Werten `Programmieren`, `Lesen`, `Sport`. Stellen Sie
`hobbies` im `<body>` von `hello.html` innerhalb des `{% if is_logged_in %}`-Zweigs dar: eine
Überschrift `Ihre Hobbies:` (`<h2>`), darunter die Hobbies als `<ul>`-Liste mit `{% for %}`
und einem `{% empty %}`-Zweig, der als Ersatztext für den Fall einer leeren Liste den Satz
"Keine Hobbies angegeben" in einem Listenelement anzeigt.

[EQ] Setzen Sie `hobbies` in der View auf eine leere Liste `[]` und aktualisieren Sie die
Seite. Was wird angezeigt, und welches Tag ist dafür verantwortlich?
<!-- time estimate: 15 min -->

Setzen Sie `hobbies` in der View wieder auf die ursprüngliche Liste
(`['Programmieren', 'Lesen', 'Sport']`), bevor Sie fortfahren.

### Echte Daten aus dem Model darstellen

Bisher haben Sie nur Testdaten direkt im `context` der View angegeben. Wie Sie aus
[PARTREF::django-model] wissen, liefert `Student.objects.all()` alle gespeicherten
`Student`-Objekte aus der Datenbank; diese lassen sich genauso wie jede andere Liste mit
`{% for %}` darstellen.

Um Werte beim Anzeigen aufzubereiten, bietet die Template-Sprache zusätzlich **Filter**: Ein
Filter wird mit `|` hinter einer Variablen angewendet, nach folgendem Schema:

```html
{{ variablenname|filtername }}
```

Für die Studierendenliste sind drei Filter nützlich:

- `title`: wandelt Text in Titelschreibweise um.
- `default:"Noch keine Note"`: zeigt einen Ersatztext, falls der Wert `None` ist
  (`grade_average` ist laut [PARTREF::django-model] optional).
- `yesno:"Aktiv,Inaktiv"`: übersetzt einen Wahrheitswert in zwei wählbare Textalternativen.

[ER] Schreiben Sie in `views.py` eine View-Funktion `students_list`, die mit `.objects.all()`
alle `Student`-Objekte lädt und sie unter dem Context-Schlüssel `students` an das Template
`students_list.html` übergibt.

[ER] Legen Sie `webapp/templates/students_list.html` an, mit derselben Grundstruktur wie
`hello.html` (`<!DOCTYPE>`, `<html lang="de">`, `<head>` mit `<meta charset>` und Titel,
`<body>`). Zeigen Sie im `<body>` eine Überschrift `Alle Studierenden` (`<h2>`), darunter die
Studierenden als `<ul>`-Liste mit `{% for %}`: je Studierendem den Namen (mit `title`),
gefolgt von " — Note: " und dem Notendurchschnitt (mit `default:"Noch keine Note"`), gefolgt
von " — " und dem Aktivstatus (mit `yesno:"Aktiv,Inaktiv"`).

[ER] Fügen Sie in `urls.py` die Route für `students_list` hinzu: Pfad `students/`, Name
`students_list`.

Öffnen Sie `http://127.0.0.1:8071/admin/` und melden Sie sich mit Ihrem Superuser an (siehe
[PARTREF::django-model]). Tragen Sie dort für Anna Müller den Notendurchschnitt `2.3` und für
Peter Klein `1.7` ein (mit Punkt als Dezimaltrennzeichen, nicht mit Komma); setzen Sie
außerdem bei Peter Klein `is_active` auf deaktiviert. Lassen Sie `grade_average` bei Lisa
Weber leer.

[EQ] Rufen Sie anschließend `http://127.0.0.1:8071/students/` auf. Was erscheint für diese
beiden Studierenden anstelle der rohen Werte, und welcher Filter ist jeweils verantwortlich?
<!-- time estimate: 20 min -->

### Template-Vererbung

Sie haben jetzt zwei Seiten, `hello.html` und `students_list.html`, die beide ihren
kompletten `<head>`-Bereich sowie eine gemeinsame Kopf- und Fußzeile selbst ausschreiben
müssten.

[EQ] Wenn Sie eine gemeinsame Kopf- oder Fußzeile für beide Seiten einführen und diese
später ändern: An welchen Stellen müssten Sie die Änderung vornehmen? Überlegen Sie, welches
Problem dadurch entsteht.

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
Ihren bisherigen `<body>`-Inhalt (Überschrift, Bedingungsblock mit Hobbies) in einen Block
`content`.

[ER] Wandeln Sie `students_list.html` auf dieselbe Weise in ein Kind-Template um.

[HINT::Wie hängen die Blocknamen in base.html und den Kind-Templates zusammen?]
Ein `{% block content %}` im Kind-Template ersetzt genau den gleichnamigen
`{% block content %}` im Basis-Template; die Namen müssen also übereinstimmen. Blöcke, die
das Kind-Template nicht überschreibt (z. B. wenn Sie `{% block title %}` weglassen), behalten
den Inhalt aus `base.html` als Standard. Sie füllen also nur die Blöcke, die sich pro Seite
unterscheiden.
[ENDHINT]

[EC] Sehen Sie sich den Quelltext beider Seiten an:

```bash
curl -s http://127.0.0.1:8071/
curl -s http://127.0.0.1:8071/students/
```

Wenn Sie einen anderen Port verwenden, passen Sie die Befehle entsprechend an.
<!-- time estimate: 20 min -->

### Statische Dateien einbinden

Neben der gemeinsamen Struktur gehört zum Aussehen einer Seite meist auch CSS (Syntax und
Einbindung kennen Sie aus [PARTREF::css-Einführung]). Solche CSS-, JavaScript- und
Bilddateien werden als **statische Dateien** bezeichnet. Django
findet sie automatisch im Ordner `static/` einer registrierten App, analog dazu, wie
Templates im `templates/`-Ordner gefunden werden. Im Template bindet das `{% static %}`-Tag
sie ein; dazu muss `{% load static %}` am Dateianfang stehen, nach folgendem Schema:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'pfad/zur/datei.css' %}">
```

[ER] Erstellen Sie das Verzeichnis `webapp/static/css` und legen Sie darin `style.css` mit
folgendem CSS an:

[SNIPPET::ALT::django_template_css]

[ER] Binden Sie die CSS-Datei in `base.html` ein: Setzen Sie `{% load static %}` an den
Dateianfang und fügen Sie im `<head>` ein `<link>`-Element ein, das die Datei
`css/style.css` per `{% static %}` referenziert.

[HINT::Warum ändert sich die Darstellung manchmal nicht?]
Falls die Seite nach diesem Schritt unverändert aussieht, prüfen Sie mit
`curl -s http://127.0.0.1:8071/static/css/style.css`, ob die Datei überhaupt ausgeliefert
wird. War der Entwicklungsserver schon gestartet, bevor Sie `webapp/static/css/` angelegt
haben, kann es sein, dass er das neue Verzeichnis noch nicht kennt: Beenden Sie ihn mit
Strg+C und starten Sie ihn neu.
[ENDHINT]

[EQ] Rufen Sie `http://127.0.0.1:8071/students/` auf. Die Seite ist jetzt formatiert, obwohl
`students_list.html` selbst kein CSS enthält. Warum genügt es, `base.html` anzupassen,
damit auch `students_list.html` das CSS erhält? Wenn Sie einen anderen Port verwenden,
passen Sie den Link entsprechend an.
<!-- time estimate: 20 min -->

### Navigation mit `{% url %}`

Damit Nutzer zwischen den Seiten wechseln können, braucht `base.html` eine Navigation:
das semantische Element `<nav>` markiert einen Block mit Navigationslinks. Für die Links
verwenden Sie nicht fest codierte Pfade wie `href="/students/"`, sondern das
`{% url %}`-Tag mit dem Routennamen; das ist die Template-Seite der Reverse Resolution,
deren Python-Seite (`reverse()`) Sie in [PARTREF::django-view] kennengelernt haben, nach
folgendem Schema:

```html
<a href="{% url 'routenname' %}">Linktext</a>
```

[ER] Erweitern Sie `base.html` um eine `<nav>` im `<header>`, die mit `{% url %}` zwei Links
setzt: einen auf die Route `hello` mit dem Text "Start" und einen auf die Route
`students_list` mit dem Text "Studierendenliste".

[ER] Verlinken Sie in `students_list.html` zusätzlich jeden Studierendennamen mit `{% url %}`
auf dessen Detailseite: Die Route `student_detail` (aus [PARTREF::django-view]) erwartet
dabei die `student_id` als Argument.

[EC] Sehen Sie sich erneut den Quelltext an und achten Sie auf die `<nav>`-Links sowie die
Links zu den Detailseiten:

```bash
curl -s http://127.0.0.1:8071/students/
```

Wenn Sie einen anderen Port verwenden, passen Sie den Befehl entsprechend an.

[EQ] Zu welchen Pfaden wurden die `{% url %}`-Links im Quelltext aufgelöst? In
[PARTREF::django-view] haben Sie mit `reverse()` dasselbe in einer View getan. Warum ist es
nützlich, dieselbe namensbasierte Auflösung sowohl in Python (`reverse()`) als auch im
Template (`{% url %}`) zur Verfügung zu haben?
<!-- time estimate: 20 min -->

Öffnen Sie zum Abschluss `http://127.0.0.1:8071/` im Browser und klicken Sie über die
`<nav>`-Links zwischen Startseite und Studierendenliste hin und her. Gut gemacht!

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

**Knackpunkte:**

- [EREFR::5] + [EREFR::6]: `students_list` lädt echte `Student`-Objekte aus der Datenbank
  (`.objects.all()`), nicht erfundene Testdaten; `students_list.html` wendet die drei
  Filter korrekt auf die passenden Felder an.
- [EREFR::10]: `students_list.html` beginnt nach der Umwandlung mit
  `{% extends "base.html" %}` und füllt nur den Block `content`; es enthält **nicht** mehr
  selbst `<!DOCTYPE>`/`<head>`/`<body>`; diese kommen aus `base.html`.
- [EREFR::13] + [EREFQ::7]: Die Navigation nutzt `{% url 'hello' %}`/
  `{% url 'students_list' %}` (nicht fest codierte Pfade); Student erkennt, dass
  `{% url %}` und `reverse()` dieselbe namensbasierte Auflösung sind, sodass eine
  Routenänderung an beiden Stellen automatisch greift.
- [EREFR::14]: Der Link je Studierendem nutzt `{% url 'student_detail' student.id %}` mit
  `student.id` als Argument (nicht ein fest codierter Pfad wie `/students/1/`).

### Fragen und Python-Dateien
[INCLUDE::ALT:django-template.md]

### Kommandoprotokoll
[PROT::ALT:django-template.prot]

[ENDINSTRUCTOR]
