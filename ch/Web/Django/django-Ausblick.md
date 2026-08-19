title: Django Ausblick
stage: alpha
timevalue: 1.0
difficulty: 2
requires: django-form
assumes: curl, http-State
explains: Middleware
---

[SECTION::goal::idea,experience]

- Ich kenne Djangos Bordmittel für Nutzer-Rückmeldungen und für den Schutz vor typischen
  Angriffen und habe ihre Wirkung selbst beobachtet.
- Ich weiß, was eine Middleware ist und warum Aktionen, die für jeden Request getan werden müssen,
  dort eingebaut werden.
- Ich weiß grob, welche weiteren fortgeschrittenen Bausteine Django bietet.
[ENDSECTION]


[SECTION::background::default]
Wenn etwas in jeder View passieren muss, selbst wenn man davon hunderte hat,
ist es schön, wenn man das einmal an einer zentralen Stelle realisieren kann,
anstatt in jeder View daran denken zu müssen.
Django hat diverse Bordmittel von dieser Art und man kann leicht eigene ergänzen.
Sie heißen [TERMREF::Middleware].
[ENDSECTION]


[SECTION::instructions::detailed]
Sie arbeiten weiter mit der App `webapp` aus [PARTREF::django-project].

Starten Sie für die folgenden Schritte in einer separaten Shell den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen.
Alle Befehle und Links unten verwenden den Port 8071; falls Sie den Server auf einem anderen
Port betreiben, passen Sie sie entsprechend an.

### Bestätigungsmeldungen mit `django.contrib.messages`

Django kann Meldungen ("Registrierung erfolgreich", "Bitte anmelden" usw.) von einer View aus
weitergeben: Die View legt die Meldung ab, die anschließend angezeigte Seite zeigt sie an,
und zwar egal, welche Folgeseite dies ist.

```python
messages.success(request, message)
```

- `success`: eine von mehreren Meldungsstufen; zu jeder gibt es eine gleichnamige Funktion
  (u. a. `info`, `warning`, `error`)
- `request`: das Request-Objekt der View, in der Sie die Meldung ablegen
- `message`: der anzuzeigende Text

Die weiteren Stufen und den vollen Funktionsumfang beschreibt die
[Django-Doku zum Messages-Framework](https://docs.djangoproject.com/en/stable/ref/contrib/messages/).

Nicht offensichtlich ist dabei nur, woher `messages` kommt:

```python
from django.contrib import messages
```

[ER] Ergänzen Sie Ihre `register`-View um eine Meldung: fügen Sie oben in `views.py` diesen
Import hinzu.
Rufen Sie in `register`, zwischen dem Anlegen des Studierenden und der Weiterleitung,
`messages.success` mit dem aktuellen Request und dem Text "Registrierung erfolgreich" auf.

Sichtbar wird die Meldung aber nur, wenn das Template der Folgeseite sie auch anzeigt.
Ein Objekt `messages` ist dafür bereits in jedem Template verfügbar, ganz ohne dass eine View diese
Variable in den Context aufnehmen muss; dafür sorgt der Eintrag
`django.contrib.messages.context_processors.messages` in `settings.py` unter
`TEMPLATES` → `OPTIONS` → `context_processors`.
Ein solcher Context-Prozessor ist eine Funktion, die den Context jedes mit `render()`
erzeugten Templates automatisch um weitere Variablen ergänzt.

`messages` verhält sich wie eine Liste, denn es könnten mehrere Meldungen zugleich relevant sein.
Man durchläuft sie wie jede andere Liste mit einer `{% for %}`-Schleife aus
[PARTREF::django-template].
Jedes Element ist dabei ein Meldungsobjekt, nennen wir es `message`:
`{{ message }}` liefert den Text und
`{{ message.tags }}` liefert die Stufe, unter der die Meldung abgelegt wurde;
oben war das `success`.
Ein Beispiel für einen solchen Block zeigt der Abschnitt "Displaying messages" der oben
verlinkten Doku zum Messages-Framework.

[ER] Fügen Sie in `base.html` eine `{% for %}`-Schleife über `messages` ein, die jede Meldung
als eigenen Absatz (`<p>`) in der Form `<stufe>: <text>` ausgibt.
Platzieren Sie sie so, dass jedes Kind-Template die Ausgabe übernimmt.

Registrieren Sie über `http://127.0.0.1:8071/register/` einen Studierenden mit dem Namen
"Sophie Wagner", Alter `22` und der E-Mail "sophie@example.com".
Sie landen auf der Detailseite.
Rufen Sie die Studierendenliste danach im Browser unter `http://127.0.0.1:8071/students/` auf.
Laden Sie dieselbe Seite anschließend noch ein zweites Mal.

[EQ] Auf welcher Seite taucht die Meldung "Registrierung erfolgreich" zum ersten Mal auf, und
warum nicht schon direkt auf der Detailseite?
Was sagen Ihnen die beiden Aufrufe der Studierendenliste über den Zeitpunkt, zu dem eine
Meldung "verbraucht" wird?

[HINT::Ich sehe die Meldung auf keiner einzigen Seite]
Prüfen Sie zuerst `base.html`: Steht Ihr neuer `{% for %}`-Block _außerhalb_ von
`{% block content %}`?
Denn innerhalb gilt: Jedes Kind-Template ersetzt den Inhalt dieses Blocks durch seinen eigenen;
die Schleife käme dann nie zur Ausgabe.
Prüfen Sie danach, ob `messages.success` in `register` _vor_ dem `redirect` steht.
[ENDHINT]

[HINT::Ich verstehe nicht, warum ausgerechnet die Detailseite nichts anzeigt]
Sehen Sie sich an, was `student_detail` aus [PARTREF::django-view] zurückgibt und was daran
anders ist als bei den übrigen Views.
[ENDHINT]

Damit erscheint die Meldung also nicht dort, wo sie hingehört: auf der Detailseite.

Zwischen dem Ablegen in der einen View und dem Anzeigen auf der nächsten Seite muss die Meldung
irgendwo überdauern: Django speichert sie beim Erzeugen der Response wieder ab, standardmäßig in
einem Cookie `messages`, das signiert und damit gegen Veränderung geschützt ist (Cookies kennen
Sie aus [PARTREF::http-State]).
<!-- time estimate: 20 min -->

### `CsrfViewMiddleware` kurzzeitig deaktivieren

Beim zweiten Bordmittel geht es um den CSRF-Schutz selbst.
Seine Wirkung kennen Sie aus [PARTREF::django-form]: Ein POST ohne gültiges Token wurde dort
mit Statuscode 403 abgewiesen.
Zuständig dafür ist eine weitere **Middleware**: eine Komponente,
die jeder Request auf dem Weg zur View und jede Response auf dem Rückweg durchläuft und die
dabei eingreifen kann.
Das ist die Ausprägung, die der allgemeine Begriff aus dem Glossar in einem Web-Framework
annimmt; außerhalb davon bezeichnet er auch ganz andere Infrastruktur-Software.
Welche Middlewares ein Projekt verwendet, steht als Liste `MIDDLEWARE` in `settings.py`; für
den CSRF-Schutz ist der Eintrag `CsrfViewMiddleware` verantwortlich.
Auch das Messages-Framework aus dem vorigen Abschnitt hängt an einem Eintrag dieser Liste.
In welcher Reihenfolge die Liste abgearbeitet wird und was eine Middleware sonst noch leisten
kann, erklärt die
[Django-Doku zu Middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/).
Welche Middlewares Django mitbringt und was jede davon tut, listet die
[Django-Doku zu den eingebauten Middlewares](https://docs.djangoproject.com/en/stable/ref/middleware/).

Öffnen Sie `settings.py` im Konfigurationsordner `meinprojekt/meinprojekt/` und kommentieren
Sie in `MIDDLEWARE` die Zeile mit `CsrfViewMiddleware` aus.
Das ist nur ein Zwischenzustand für den folgenden Test; am Ende dieses Abschnitts muss die
Zeile wieder dastehen wie zu Beginn.

[EC] Senden Sie den gleichen Aufruf wie in [PARTREF::django-form], der einen POST ohne
CSRF-Token an `/search-post/` schickt und nur den Statuscode ausgibt:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST -d "q=Anna" http://127.0.0.1:8071/search-post/
```

[EC] Kommentieren Sie die Zeile wieder ein und senden Sie denselben Aufruf ein zweites Mal.

[HINT::Ich bekomme nicht die richtigen Statuscodes]
Dann hatte der Entwicklungsserver Ihre geänderte `settings.py` noch nicht fertig eingelesen.
Im Serverfenster erscheint nach jeder Änderung eine Zeile, die auf
`settings.py changed, reloading.` endet; warten Sie diese ab und wiederholen Sie den Aufruf.
[ENDHINT]

[EQ] Verändert haben Sie keine einzige View, sondern nur eine Zeile in `settings.py`, und
trotzdem ändert sich das Verhalten von `/search-post/`.
Welche Ihrer übrigen Views wären von derselben Zeile ebenfalls betroffen, welche nicht?
Für welche Zwecke ist so etwas sinnvoll?

[HINT::Ich weiß nicht, welche meiner Views überhaupt betroffen sein können]
Sehen Sie in [PARTREF::django-form] nach, bei welcher Art von Anfrage Django ein gültiges Token
verlangt.
Gehen Sie danach Ihre `urls.py` durch und prüfen Sie für jede eingetragene View, ob sie solche
Anfragen überhaupt entgegennimmt.
[ENDHINT]
<!-- time estimate: 15 min -->

### `XFrameOptionsMiddleware` kurzzeitig deaktivieren

Das dritte Bordmittel ist eine weitere Sicherheits-Middleware: `XFrameOptionsMiddleware`
setzt bei jeder Antwort den Header `X-Frame-Options`, standardmäßig mit dem Wert `DENY`, der
jede Einbettung Ihrer Seite in einen `<iframe>` verhindert, gleich von welcher Website aus.
Lesen Sie vorab den Abschnitt "An example of clickjacking" der
[Django-Doku zu Clickjacking](https://docs.djangoproject.com/en/stable/ref/clickjacking/#an-example-of-clickjacking).
Dort steht das Angriffsszenario, um das es in der Frage am Ende dieses Abschnitts geht.

Öffnen Sie `settings.py` erneut und kommentieren Sie in `MIDDLEWARE` die Zeile mit
`XFrameOptionsMiddleware` aus, wieder nur für die Dauer des Tests.

Der Entwicklungsserver bemerkt die Änderung wieder von selbst; warten Sie kurz.

[EC] Senden Sie den folgenden Aufruf, der nur die Header abruft (`-I`):

```bash
curl -sI "http://127.0.0.1:8071/"
```

[EC] Kommentieren Sie die Zeile wieder ein und senden Sie denselben Aufruf ein zweites Mal.

[EQ] Vergleichen Sie die beiden Ausgaben: Welche Sicherheits-Header stehen unverändert in
beiden, obwohl die `XFrameOptionsMiddleware` im ersten Aufruf fehlte, und welcher andere
Eintrag der `MIDDLEWARE`-Liste kommt als Urheber dieser Header in Frage?
Was könnte eine fremde Website mit Ihrer Seite anstellen, solange `X-Frame-Options` fehlt?
Für die erste Frage hilft die im vorigen Abschnitt verlinkte Übersicht der eingebauten
Middlewares.

In diesem und dem vorigen Abschnitt war `settings.py` die einzige Datei, die Sie angefasst
haben; nehmen Sie sie neben `views.py` und `base.html` aus Abschnitt 1 mit in Ihre
`*.files`-Datei auf, damit sich der wiederhergestellte Zustand der beiden Middleware-Zeilen
prüfen lässt.
<!-- time estimate: 15 min -->

### Weitere Bausteine im Überblick

Die folgenden drei Bausteine probieren wir nicht selbst aus.
Es reicht, zu wissen, dass es sie gibt und wofür sie sich einsetzen lassen, damit Sie bei
Bedarf gezielt danach suchen können:

- **[Class-based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)**:
  Views lassen sich statt als Funktion auch als Klasse schreiben, die für unterschiedliche
  HTTP-Methoden (GET, POST, ...) jeweils eine eigene Methode bereitstellt, statt wie bisher
  mit `if request.method == 'POST':` zu verzweigen.
- **[ModelForm](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/)**: Statt
  wie in `register` jedes Feld einzeln mit `request.POST['feld']` auszulesen und sich für die
  Pflichtfeldprüfung auf `required` im HTML zu verlassen, kann eine `ModelForm`-Klasse aus
  einem Model automatisch ein Formular samt serverseitiger Validierung erzeugen.
- **[Authentifizierung](https://docs.djangoproject.com/en/stable/topics/auth/)**:
  Mit `createsuperuser` haben Sie bereits ein Konto angelegt und sich damit an der
  Admin-Oberfläche angemeldet ([PARTREF::django-model]).
  Dasselbe System (`django.contrib.auth`) funktioniert auch außerhalb der Admin-Oberfläche:
  Es liefert eigene Login-/Logout-Views, und einzelne Views lassen sich damit so absichern,
  dass nur angemeldete Nutzer sie aufrufen dürfen.

[EQ] Welcher dieser drei Bausteine hätte Ihnen in [PARTREF::django-form] am meisten geholfen,
an welcher konkreten Stelle, und was hätte er dort besser gemacht?
<!-- time estimate: 10 min -->

### Weiterführend

- [Django API-Referenz](https://docs.djangoproject.com/en/stable/ref/): Übersicht über
  alle eingebauten Django-Komponenten
- [MDN-Tutorial "Django Web Framework"](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django):
  Ein vollständiges Projekt, in dem die drei oben nur erwähnten Bausteine tatsächlich zum
  Einsatz kommen

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

### Fragen und Python-Dateien
[INCLUDE::ALT:django-Ausblick.md]

### Kommandoprotokoll
[PROT::ALT:django-Ausblick.prot]

[ENDINSTRUCTOR]
