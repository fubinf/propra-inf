title: Django Ausblick
stage: alpha
timevalue: 0.75
difficulty: 2
requires: django-form
assumes: curl
---

[SECTION::goal::idea,experience]

- Ich kenne Djangos Bordmittel für Nutzer-Rückmeldungen und für Schutzmechanismen und habe sie
  an eigenem Code ausprobiert.
- Ich weiß grob, welche weiteren fortgeschrittenen Bausteine Django bietet.

[ENDSECTION]

[SECTION::background::default]

Eine Registrierung, die kommentarlos auf einer anderen Seite landet, ein Formular, das ohne
Schutzmechanismus jeden Absender akzeptiert, oder eine Seite, die sich anstandslos in eine
fremde Website einbetten lässt: Das sind Probleme, die in einer echten Anwendung sofort
auffallen würden, in den bisherigen Aufgaben aber nie auftraten, weil sie dort nicht im
Fokus standen. Django löst solche Probleme nicht mit Custom-Code, sondern mit eigenen,
fertigen Bordmitteln, die unabhängig von den bisher behandelten Kernkomponenten (Model,
View, Template, Formular) funktionieren.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp` aus [PARTREF::django-form].

### Bestätigungsmeldungen mit `django.contrib.messages`

Django kann Meldungen ("Registrierung erfolgreich", "Bitte anmelden" usw.) über einen
Redirect hinweg transportieren: Eine View legt eine Meldung ab, die nächste Seite, die
Meldungen anzeigt, holt sie ab und zeigt sie an, unabhängig davon, welche View dazwischen
lag.

```
messages.success(request, message)
```

- `success` ist eine von mehreren Dringlichkeitsstufen (u. a. auch `info`, `warning`,
  `error`), erkennbar am jeweiligen Funktionsnamen
- `request`: das Request-Objekt der View, in der Sie die Meldung ablegen
- `message`: der anzuzeigende Text

Konkretes Beispiel:

```python
from django.contrib import messages

messages.success(request, "Erfolgreich gespeichert")
```

[ER] Ergänzen Sie Ihre `register`-View um eine Meldung: fügen Sie oben in `views.py` den
Import wie im Beispiel hinzu. Rufen Sie in `register`, zwischen dem Anlegen des
Studierenden und der Weiterleitung, `messages.success` mit dem aktuellen Request und dem
Text "Registrierung erfolgreich" auf.

Sichtbar wird die Meldung erst, wenn ein Template sie auch anzeigt. Der `messages`-Wert
selbst ist dafür bereits automatisch in jedem Template verfügbar, ganz ohne dass eine View
ihn in den Context aufnehmen muss. Zur Anzeige dient wieder ein Filter mit Argument, wie Sie
ihn aus [PARTREF::django-template] von `default`/`yesno` kennen, diesmal allerdings ein
anderer: `|join:trennzeichen` reiht die Elemente eines iterierbaren Werts, getrennt durch das
angegebene Zeichen, zu einem einzigen Text aneinander. Konkretes Beispiel:

```
{{ zutaten|join:" + " }}
```

Bei `zutaten = ["Mehl", "Zucker", "Eier"]` ergibt das `Mehl + Zucker + Eier`; bei einer
leeren Liste bleibt die Ausgabe leer.

[ER] Fügen Sie in `base.html` unmittelbar vor der Zeile `{% block content %}` eine Zeile ein,
die `messages` mit demselben Filter und dem Trennzeichen ", " ausgibt.

Registrieren Sie über `http://127.0.0.1:8071/register/` einen Studierenden mit dem Namen
"Sophie Wagner", Alter `22` und der E-Mail "sophie@example.com". Sie landen auf der
Detailseite (Klartext, ohne die neue Zeile aus `base.html`, zeigt daher keine Meldung, und
ohne Menü zum Klicken). Rufen Sie danach im Browser
`http://127.0.0.1:8071/students/` auf.

[EQ] Auf welcher Seite taucht die Meldung "Registrierung erfolgreich" zum ersten Mal auf,
und warum nicht schon direkt auf der Detailseite? Was sagt Ihnen das über den Zeitpunkt, zu
dem eine Meldung "verbraucht" wird?
<!-- time estimate: 15 min -->

### CSRF-Middleware kurzzeitig deaktivieren

Beim zweiten Bordmittel geht es um den CSRF-Schutz selbst, den Sie aus
[PARTREF::django-form] kennen. Er wird nicht vom `{% csrf_token %}`-Tag allein
durchgesetzt, sondern von einer Middleware, die jeden
POST-Request vorab prüft. Middlewares sind in `settings.py` in einer Liste eingetragen und
wirken auf jeden Request.

[ER] Öffnen Sie `settings.py` im Konfigurationsordner `meinprojekt/meinprojekt/` und
kommentieren Sie in `MIDDLEWARE` die Zeile mit `CsrfViewMiddleware` aus.

[EC] Der Entwicklungsserver bemerkt die Änderung von selbst (sein Autoreloader beobachtet
alle `.py`-Dateien, auch `settings.py`, und startet den Prozess bei einer Änderung
automatisch neu); warten Sie kurz. Der folgende Aufruf sendet einen POST ohne CSRF-Token
an `/search-post/`, gibt aber nur den Statuscode aus und
verwirft die eigentliche Antwort:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST "http://127.0.0.1:8071/search-post/" -d "q=Anna"
```

Kommentieren Sie die Zeile danach wieder ein und senden Sie denselben Aufruf noch einmal.

[EQ] Welcher Statuscode kam mit deaktivierter Middleware zurück, und warum ist es gefährlich,
diese Middleware in einer echten Anwendung dauerhaft auszukommentieren?
<!-- time estimate: 15 min -->

### X-Frame-Options-Middleware kurzzeitig deaktivieren

Das dritte Bordmittel ist eine weitere Sicherheits-Middleware: `XFrameOptionsMiddleware`
setzt bei jeder Antwort den Header `X-Frame-Options: DENY`, der verhindert, dass Ihre
Seite in einem `<iframe>` auf einer fremden Website eingebettet wird.

[ER] Öffnen Sie `settings.py` im Konfigurationsordner `meinprojekt/meinprojekt/` und
kommentieren Sie in `MIDDLEWARE` die Zeile mit `XFrameOptionsMiddleware` aus.

[EC] Der Entwicklungsserver bemerkt die Änderung von selbst; warten Sie kurz. Senden Sie
danach den folgenden Aufruf, der nur die Header abruft (`-I`): einmal jetzt und ein
zweites Mal, nachdem Sie die Zeile wieder einkommentiert haben:

```bash
curl -sI "http://127.0.0.1:8071/"
```

[EQ] Welcher Header taucht im ersten Aufruf nicht auf, der im zweiten wieder da ist? Was
könnte eine fremde Website mit Ihrer Seite anstellen, solange dieser Header fehlt?

[HINT::Mir fällt kein konkretes Angriffsszenario ein]
Ein `<iframe>` bettet eine fremde Seite unsichtbar in die eigene Seite ein, darüber lässt
sich eine eigene, für den Nutzer sichtbare Oberfläche legen (z. B. ein verlockender
Button). Überlegen Sie, was passiert, wenn der Nutzer glaubt, auf diese Oberfläche zu
klicken, tatsächlich aber durch das unsichtbare `<iframe>` hindurch auf Ihre Seite klickt.
[ENDHINT]
<!-- time estimate: 15 min -->

### Weitere Bordmittel im Überblick

Die folgenden drei Bausteine probieren Sie nicht selbst aus. Es reicht, zu wissen, dass es
sie gibt und wofür sie sich einsetzen lassen, damit Sie bei Bedarf gezielt danach suchen
können:

- **[Class-based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)**:
  Views lassen sich statt als Funktion auch als Klasse schreiben, die für unterschiedliche
  HTTP-Methoden (GET, POST, ...) jeweils eine eigene Methode bereitstellt, statt wie bisher
  mit `if request.method == 'POST':` zu verzweigen.
- **[ModelForm](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/)**: Statt
  wie in `register` jedes Feld einzeln mit `request.POST['feld']` auszulesen und `required`
  im HTML zu prüfen, kann eine `ModelForm`-Klasse aus einem Model automatisch ein Formular
  samt serverseitiger Validierung erzeugen.
- **[Sessions und Authentifizierung](https://docs.djangoproject.com/en/stable/topics/auth/)**:
  Sie haben sich mit `createsuperuser` bereits an der Admin-Oberfläche angemeldet
  ([PARTREF::django-model]). Dasselbe System (`django.contrib.auth`) funktioniert auch
  außerhalb der Admin-Oberfläche: eigene Login-/Logout-Views, und einzelne Views lassen
  sich so absichern, dass nur angemeldete Nutzer sie aufrufen dürfen.

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
- [EREFR::3] + [EREFQ::2]: Die `CsrfViewMiddleware`-Zeile ist nach dem Test wieder
  einkommentiert; Student erkennt, dass ohne sie jeder POST ohne Token akzeptiert würde.
- [EREFR::4] + [EREFQ::3]: Die `XFrameOptionsMiddleware`-Zeile ist nach dem Test wieder
  einkommentiert; Student erkennt, dass ohne sie der `X-Frame-Options`-Header fehlt und die
  Seite dadurch in ein fremdes `<iframe>` eingebettet werden könnte.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-Ausblick.md]

### Kommandoprotokoll
[PROT::ALT:django-Ausblick.prot]

[ENDINSTRUCTOR]
