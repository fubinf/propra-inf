title: Django Template System
stage: draft
timevalue: 2
difficulty: 2
requires: django-view
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
Programmlogik — das wird schnell unübersichtlich und ist schwer zu pflegen. Das Django
Template System trennt beides: Die View liefert nur die Daten, das Template bestimmt, wie
sie als HTML dargestellt werden. So können Layout und Logik unabhängig voneinander bearbeitet
werden.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`. In [PARTREF::django-project] haben Sie bereits ein
erstes Template `hello.html` angelegt, das die `hello`-View mit `render()` anzeigt. Darauf
bauen die folgenden Schritte auf.

### Template-Variablen und Context

Der `context`-Dictionary übergibt Daten von der View an das Template. Bisher enthielt er nur
eine einzige Variable (`message`). Ein Template kann beliebig viele Variablen verwenden.

[ER] Ersetzen Sie die `hello`-View in `views.py` durch eine Version mit mehreren
Context-Variablen:

[SNIPPET::ALT::django_template_view_context]
<!-- ER1 -->

[ER] Passen Sie `hello.html` an, sodass es die neuen Variablen mit der Syntax
`{{ variablenname }}` anzeigt:

[SNIPPET::ALT::django_template_hello_context]
<!-- ER2 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/` im Browser auf. Welche Werte erscheinen anstelle
der Platzhalter `{{ greeting }}` und `{{ user_name }}`, und woher stammen diese Werte? Wenn
Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ1 -->
<!-- time estimate: 15 min -->

### Bedingte Darstellung mit `{% if %}`

Neben Variablen (`{{ ... }}`) kennt die Template-Sprache auch Tags für Logik, geschrieben mit
`{% ... %}`. Das `{% if %}`-Tag zeigt Inhalte nur unter einer Bedingung an:

[ER] Erweitern Sie `hello.html` um eine bedingte Darstellung, die von der Variablen
`is_logged_in` abhängt:

[SNIPPET::ALT::django_template_hello_if]
<!-- ER3 -->

[EQ] Ändern Sie in der View `is_logged_in` auf `False` und aktualisieren Sie die Seite. Was
wird jetzt angezeigt, und welcher Teil des Templates ist dafür verantwortlich?
<!-- EQ2 -->
<!-- time estimate: 12 min -->

### Schleifen mit `{% for %}`

Listen und andere Sammlungen lassen sich mit `{% for %}` durchlaufen. Das optionale
`{% empty %}`-Tag liefert einen Ersatzinhalt, falls die Liste leer ist.

[ER] Ergänzen Sie die `hello`-View um eine Liste `hobbies` und stellen Sie diese in
`hello.html` mit einer Schleife dar:

[SNIPPET::ALT::django_template_view_loop]

[SNIPPET::ALT::django_template_hello_for]
<!-- ER4 -->

[EQ] Setzen Sie `hobbies` in der View auf eine leere Liste `[]` und aktualisieren Sie die
Seite. Was wird angezeigt, und welches Tag ist dafür verantwortlich?
<!-- EQ3 -->
<!-- time estimate: 15 min -->

### Reflexion: Warum Wiederverwendung?

Bisher hat `hello.html` seine gesamte HTML-Struktur (`<!DOCTYPE>`, `<head>`, `<body>`)
selbst enthalten. Stellen Sie sich vor, Sie brauchen eine zweite Seite mit demselben
Kopfbereich, derselben Navigation und demselben Fußbereich.

[EQ] Angenommen, jede Seite schreibt ihren kompletten `<head>`-Bereich, eine gemeinsame
Kopfzeile und eine gemeinsame Fußzeile selbst aus (zusammen etwa 10 Zeilen). Wie viele
dieser Zeilen wären bei 2 Seiten insgesamt doppelt vorhanden, und was müssten Sie tun, wenn
sich die Fußzeile später ändert? Überlegen Sie, welches Problem dadurch entsteht.
<!-- EQ4 -->
<!-- time estimate: 12 min -->

### Template-Vererbung: eine Studierendenliste

Template-Vererbung löst genau dieses Problem: Ein **Basis-Template** definiert die
gemeinsame Struktur und markiert mit `{% block %}` die Stellen, die einzelne Seiten füllen.
Ein **Kind-Template** übernimmt die Struktur mit `{% extends %}` und überschreibt nur die
Blöcke. Als Beispiel bauen Sie eine Seite, die alle bisher registrierten Studierenden
(aus [PARTREF::django-model]/[PARTREF::django-form]) auflistet.

[ER] Erstellen Sie in `webapp/templates/` die Datei `base.html`:

[SNIPPET::ALT::django_template_base]
<!-- ER5 -->

[ER] Erstellen Sie eine View, die alle `Student`-Objekte lädt (mit der bereits aus
[PARTREF::django-model] bekannten `.objects.all()`), und ein Template
`students_list.html`, das von `base.html` erbt und die Liste mit `{% for %}` darstellt:

[SNIPPET::ALT::django_template_view_students_list]

[SNIPPET::ALT::django_template_students_list_html]
<!-- ER6 -->

Dabei kommen drei Filter zum Einsatz:

- `title`: wandelt Text in Titelschreibweise um.
- `default:"Noch keine Note"`: zeigt einen Ersatztext, falls `grade_average` `None` ist
  (das Feld ist laut [PARTREF::django-model] optional).
- `yesno:"Aktiv,Inaktiv"`: übersetzt einen Wahrheitswert in zwei wählbare Textalternativen.

[HINT::Wie hängen die Blocknamen in base.html und students_list.html zusammen?]
Ein `{% block content %}` im Kind-Template ersetzt genau den gleichnamigen
`{% block content %}` im Basis-Template — die Namen müssen also übereinstimmen. Blöcke, die
das Kind-Template nicht überschreibt (z. B. wenn Sie `{% block title %}` weglassen), behalten
den Inhalt aus `base.html` als Standard. Sie füllen also nur die Blöcke, die sich pro Seite
unterscheiden.
[ENDHINT]

[ER] Fügen Sie die passende Route in `urls.py` hinzu:

[SNIPPET::ALT::django_template_urls_students_list]
<!-- ER7 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/students/` auf. Die Kopf- und Fußzeile erscheinen,
obwohl `students_list.html` sie nicht selbst enthält — woher kommen sie? Worin liegt der
Vorteil gegenüber der in [EREFQ::4] betrachteten Wiederholung? Falls Sie noch keine
Studierenden registriert haben, sollte die Seite trotzdem fehlerfrei laden — welches Tag
sorgt dafür, dass eine leere Liste kein Problem ist? Wenn Sie einen anderen Port
verwenden, passen Sie den Link entsprechend an.
<!-- EQ5 -->
<!-- time estimate: 32 min -->

### Statische Dateien einbinden

CSS-, JavaScript- und Bilddateien werden als **statische Dateien** bezeichnet. Django
findet sie automatisch im Ordner `static/` einer registrierten App — analog dazu, wie
Templates im `templates/`-Ordner gefunden werden. Im Template bindet das `{% static %}`-Tag
sie ein; dazu muss `{% load static %}` am Dateianfang stehen.

[EC] Erstellen Sie in `webapp/` das Verzeichnis für die CSS-Datei:

```bash
mkdir -p webapp/static/css
```
<!-- EC1 -->

[ER] Legen Sie `webapp/static/css/style.css` mit etwas CSS an:

[SNIPPET::ALT::django_template_css]
<!-- ER8 -->

[ER] Binden Sie die CSS-Datei in `base.html` ein (`{% load static %}` am Anfang,
`{% static %}` im `<head>`):

[SNIPPET::ALT::django_template_base_static]
<!-- ER9 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/students/` auf. Die Seite ist jetzt formatiert, obwohl
`students_list.html` selbst kein CSS enthält. Warum genügt es, `base.html` anzupassen,
damit auch `students_list.html` das CSS erhält? Wenn Sie einen anderen Port verwenden,
passen Sie den Link entsprechend an.
<!-- EQ6 -->
<!-- time estimate: 12 min -->

### Navigation mit `{% url %}`

Damit Nutzer zwischen den Seiten wechseln können, braucht `base.html` eine Navigation. Für
die Links verwenden Sie **nicht** fest codierte Pfade wie `href="/students/"`, sondern das
`{% url %}`-Tag mit dem Routennamen — das ist die Template-Seite der Reverse Resolution,
deren Python-Seite (`reverse()`) Sie in [PARTREF::django-view] kennengelernt haben.

[ER] Erweitern Sie `base.html` um eine Navigation, die mit `{% url %}` auf die benannten
Routen `hello` und `students_list` verweist:

[SNIPPET::ALT::django_template_base_nav]
<!-- ER10 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/students/` auf und schauen Sie im Seitenquelltext
nach, zu welchen Pfaden die `{% url %}`-Links aufgelöst wurden. In [PARTREF::django-view]
haben Sie mit `reverse()` dasselbe in einer View getan. Warum ist es nützlich, dieselbe
namensbasierte Auflösung sowohl in Python (`reverse()`) als auch im Template (`{% url %}`)
zur Verfügung zu haben? Wenn Sie einen anderen Port verwenden, passen Sie den Link
entsprechend an.
<!-- EQ7 -->
<!-- time estimate: 22 min -->

### Weiterführend

- [Templates](https://docs.djangoproject.com/en/stable/topics/templates/) – Überblick über die Template-Sprache
- [Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) – Referenz zu allen Tags und Filtern
- [Managing static files](https://docs.djangoproject.com/en/stable/howto/static-files/) – Anleitung zu statischen Dateien

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::6]: `students_list.html` beginnt mit `{% extends "base.html" %}` und füllt nur den
  Block `content`; es enthält **nicht** selbst `<!DOCTYPE>`/`<head>`/`<body>` — diese kommen
  aus `base.html`. Die Liste wird mit echten `Student`-Objekten aus der Datenbank befüllt
  (`.objects.all()`), nicht mit erfundenen Testdaten.
- [EREFR::10] + [EREFQ::7]: Die Navigation nutzt `{% url 'hello' %}`/
  `{% url 'students_list' %}` (nicht fest codierte Pfade); Student erkennt, dass
  `{% url %}` und `reverse()` dieselbe namensbasierte Auflösung sind, sodass eine
  Routenänderung an beiden Stellen automatisch greift.
- [EREFQ::5]: Student erkennt, dass die gemeinsame Struktur nur einmal in `base.html` steht
  und eine Änderung dort alle erbenden Seiten betrifft (statt jede Seite einzeln zu ändern);
  außerdem, dass `{% empty %}` die leere Liste ohne Fehler abfängt.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-template.md]

### Kommandoprotokoll
[PROT::ALT:django-template.prot]

[ENDINSTRUCTOR]
