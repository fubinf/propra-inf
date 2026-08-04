title: Django Ausblick
stage: alpha
timevalue: 0.75
difficulty: 2
requires: django-form
assumes: curl
---

[SECTION::goal::idea,experience]

- Ich kenne Djangos Bordmittel für Nutzer-Rückmeldungen und für Schutzmechanismen und habe
  ihre Wirkung selbst beobachtet.
- Ich weiß grob, welche weiteren fortgeschrittenen Bausteine Django bietet.

[ENDSECTION]

[SECTION::background::default]

Eine Registrierung, die kommentarlos auf einer anderen Seite landet, ein Formular, das jeden
Absender akzeptiert, oder eine Seite, die sich in eine fremde Website einbetten lässt: In
einer echten Anwendung wären das ernste Mängel.
Der erste Fall trifft auf Ihr Projekt bisher zu, denn dafür fehlt schlicht die passende
Funktion.
Die beiden anderen verhindert Django von Anfang an: Den CSRF-Schutz haben Sie in
[PARTREF::django-form] bewusst eingesetzt, den Schutz vor Einbettung nie bemerkt.
Solche Bordmittel gehören zu keiner der bisher behandelten Kernkomponenten (Model, View,
Template, Formular), sondern greifen quer dazu bei jedem Request.
In dieser Aufgabe holen Sie die fehlende Rückmeldung nach und schalten die beiden
Schutzmechanismen kurz ab, um zu sehen, was sie eigentlich leisten.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp` aus [PARTREF::django-form].

Starten Sie für die folgenden Schritte in einer separaten Shell den Entwicklungsserver mit
`python manage.py runserver 8071` und lassen Sie ihn laufen.
Alle Befehle und Links unten verwenden den Port 8071; falls Sie den Server auf einem anderen
Port betreiben, passen Sie sie entsprechend an.

### Bestätigungsmeldungen mit `django.contrib.messages`

Django kann Meldungen ("Registrierung erfolgreich", "Bitte anmelden" usw.) über einen
Redirect hinweg transportieren: Eine View legt eine Meldung ab, die nächste Seite, die
Meldungen anzeigt, holt sie ab und zeigt sie an, unabhängig davon, welche View dazwischen
lag.

```python
messages.success(request, message)
```

- `success`: eine von mehreren Dringlichkeitsstufen (u. a. `info`, `warning`, `error`), jeweils
  am Funktionsnamen erkennbar
- `request`: das Request-Objekt der View, in der Sie die Meldung ablegen
- `message`: der anzuzeigende Text

Die weiteren Stufen und den vollen Funktionsumfang beschreibt die
[Django-Doku zum Messages-Framework](https://docs.djangoproject.com/en/stable/ref/contrib/messages/).

Konkretes Beispiel:

```python
from django.contrib import messages

messages.success(request, "Erfolgreich gespeichert")
```

[ER] Ergänzen Sie Ihre `register`-View um eine Meldung: fügen Sie oben in `views.py` den
Import wie im Beispiel hinzu.
Rufen Sie in `register`, zwischen dem Anlegen des Studierenden und der Weiterleitung,
`messages.success` mit dem aktuellen Request und dem Text "Registrierung erfolgreich" auf.

Sichtbar wird die Meldung erst, wenn ein Template sie auch anzeigt.
`messages` ist dafür bereits automatisch in jedem Template verfügbar, ganz ohne dass eine View
es in den Context aufnehmen muss.
Zur Anzeige dient wieder ein Filter mit Argument, wie Sie ihn aus [PARTREF::django-template]
von `default`/`yesno` kennen, diesmal allerdings ein anderer: `|join:trennzeichen` reiht die
Elemente eines iterierbaren Werts, getrennt durch die angegebene Zeichenfolge, zu einem
einzigen Text aneinander.
Konkretes Beispiel:

```html
{{ zutaten|join:" + " }}
```

Bei `zutaten = ["Mehl", "Zucker", "Eier"]` ergibt das `Mehl + Zucker + Eier`; bei einer
leeren Liste bleibt die Ausgabe leer.
Nachschlagen lässt sich dieser Filter wie alle anderen in der Django-Doku zu
[Built-in template tags and filters](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#join).

[ER] Fügen Sie in `base.html` unmittelbar vor der Zeile `{% block content %}` eine Zeile ein,
die `messages` mit demselben Filter und dem Trennzeichen ", " ausgibt.

Registrieren Sie über `http://127.0.0.1:8071/register/` einen Studierenden mit dem Namen
"Sophie Wagner", Alter `22` und der E-Mail "sophie@example.com".
Sie landen auf der Detailseite; sie enthält keinen Link zur Studierendenliste.
Rufen Sie diese danach im Browser unter `http://127.0.0.1:8071/students/` auf.

[EQ] Auf welcher Seite taucht die Meldung "Registrierung erfolgreich" zum ersten Mal auf, und
warum nicht schon direkt auf der Detailseite?
Was sagt Ihnen das über den Zeitpunkt, zu dem eine Meldung "verbraucht" wird?
<!-- time estimate: 15 min -->

### `CsrfViewMiddleware` kurzzeitig deaktivieren

Beim zweiten Bordmittel geht es um den CSRF-Schutz selbst.
Die `CsrfViewMiddleware`, die ihn durchsetzt, haben Sie in [PARTREF::django-form] bereits
kennengelernt; hier sehen Sie nun, woher sie überhaupt kommt: Middlewares sind in
`settings.py` in einer Liste eingetragen und wirken auf jeden Request.
Was eine Middleware überhaupt ist und in welcher Reihenfolge die Liste abgearbeitet wird,
erklärt die
[Django-Doku zu Middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/).

Öffnen Sie `settings.py` im Konfigurationsordner `meinprojekt/meinprojekt/` und kommentieren
Sie in `MIDDLEWARE` die Zeile mit `CsrfViewMiddleware` aus.
Das ist nur ein Zwischenzustand für den folgenden Test: Am Ende dieses Abschnitts steht die
Zeile wieder wie im Original da.

[EC] Der Autoreloader des Entwicklungsservers erfasst auch `settings.py`, die Änderung wirkt
also ohne Neustart; warten Sie kurz.
Senden Sie danach den folgenden Aufruf, der einen POST ohne CSRF-Token an `/search-post/`
schickt und nur den Statuscode ausgibt: einmal jetzt und ein zweites Mal, nachdem Sie die
Zeile wieder einkommentiert haben:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST -d "q=Anna" http://127.0.0.1:8071/search-post/
```

[EQ] Welcher Statuscode kam mit deaktivierter Middleware zurück, und warum ist es gefährlich,
diese Middleware in einer echten Anwendung dauerhaft auszukommentieren?
<!-- time estimate: 15 min -->

### `XFrameOptionsMiddleware` kurzzeitig deaktivieren

Das dritte Bordmittel ist eine weitere Sicherheits-Middleware: `XFrameOptionsMiddleware`
setzt bei jeder Antwort den Header `X-Frame-Options: DENY`, der verhindert, dass Ihre Seite
in einem `<iframe>` auf einer fremden Website eingebettet wird.
Lesen Sie vorab den Abschnitt "An example of clickjacking" der
[Django-Doku zu Clickjacking](https://docs.djangoproject.com/en/stable/ref/clickjacking/#an-example-of-clickjacking).
Dort steht das Angriffsszenario, um das es in der Frage am Ende dieses Abschnitts geht.

Öffnen Sie `settings.py` erneut und kommentieren Sie in `MIDDLEWARE` die Zeile mit
`XFrameOptionsMiddleware` aus, wieder nur für die Dauer des Tests.

[EC] Der Entwicklungsserver bemerkt die Änderung von selbst; warten Sie kurz.
Senden Sie danach den folgenden Aufruf, der nur die Header abruft (`-I`): einmal jetzt und
ein zweites Mal, nachdem Sie die Zeile wieder einkommentiert haben:

```bash
curl -sI "http://127.0.0.1:8071/"
```

[EQ] Vergleichen Sie die beiden Ausgaben: Welche Sicherheits-Header stehen unverändert in
beiden, obwohl die `XFrameOptionsMiddleware` im ersten Aufruf fehlte?
Was könnte eine fremde Website mit Ihrer Seite anstellen, solange `X-Frame-Options` fehlt?
<!-- time estimate: 10 min -->

### Weitere Bordmittel im Überblick

Die folgenden drei Bausteine probieren Sie nicht selbst aus.
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
- **[Sessions und Authentifizierung](https://docs.djangoproject.com/en/stable/topics/auth/)**:
  Mit `createsuperuser` haben Sie bereits ein Konto angelegt und sich damit an der
  Admin-Oberfläche angemeldet ([PARTREF::django-model]).
  Dasselbe System (`django.contrib.auth`) funktioniert auch außerhalb der Admin-Oberfläche:
  Es liefert eigene Login-/Logout-Views, und einzelne Views lassen sich damit so absichern,
  dass nur angemeldete Nutzer sie aufrufen dürfen.
<!-- time estimate: 5 min -->

### Weiterführend

- [Django API-Referenz](https://docs.djangoproject.com/en/stable/ref/): Übersicht über
  alle eingebauten Django-Komponenten
- [Django Girls Tutorial](https://tutorial.djangogirls.org/): Ein weiteres vollständiges
  Projekt zum Üben, falls Sie über diese Aufgabe hinaus mit Django experimentieren möchten

[ENDSECTION]

[SECTION::submission::program]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::1] + [EREFR::2] + [EREFQ::1]: `messages.success(...)` steht in `register`
  unmittelbar vor dem `redirect(...)`, `base.html` gibt `messages` mit `|join:", "` aus;
  Student erkennt, dass die Meldung erst auf der nächsten Seite erscheint, die diese Zeile
  tatsächlich rendert (hier: `students_list.html` über `base.html`), nicht zwangsläufig auf
  der unmittelbar nächsten Seite überhaupt.
- [EREFC::1] + [EREFQ::2]: Das Protokoll enthält denselben `curl`-Aufruf zweimal, mit `200`
  bei ausgebauter und `403` bei wieder eingebauter `CsrfViewMiddleware`; Student erkennt,
  dass ohne sie jeder POST ohne Token akzeptiert würde.
- [EREFC::2] + [EREFQ::3]: Das Protokoll enthält denselben `curl -sI`-Aufruf zweimal, einmal
  ohne und einmal mit `X-Frame-Options: DENY`, während die übrigen Sicherheits-Header in
  beiden Ausgaben stehen; Student erkennt, dass ohne diesen Header die Seite in ein fremdes
  `<iframe>` eingebettet werden könnte.
- Beide Auskommentierungen waren nur Zwischenschritte: In der abgegebenen `settings.py` stehen
  `CsrfViewMiddleware` und `XFrameOptionsMiddleware` wieder aktiv in `MIDDLEWARE`.
  Das Kommandoprotokoll allein deckt das nicht ab, weil der jeweils zweite `curl`-Aufruf vor
  der Abgabe liegt und deshalb auch bei vergessener Wiederherstellung korrekt aussieht.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-Ausblick.md]

### Kommandoprotokoll
[PROT::ALT:django-Ausblick.prot]

[ENDINSTRUCTOR]
