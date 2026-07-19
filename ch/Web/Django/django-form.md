title: Django Formularbehandlung
stage: draft
timevalue: 1.5
difficulty: 2
requires: django-template
assumes: http-GET, http-POST
---

[SECTION::goal::idea,experience]

- Ich verstehe den Unterschied zwischen GET und POST beim Absenden von Formularen.
- Ich kann HTML-Formulare erstellen, ihre Daten in einer View verarbeiten und dauerhaft
  in der Datenbank speichern.
- Ich verstehe die Rolle des CSRF-Schutzes im Formular-Workflow.

[ENDSECTION]

[SECTION::background::default]

HTML-Formulare sind der klassische Weg, über den Nutzer Daten an eine Web-Anwendung senden —
von der Suchanfrage bis zur Registrierung. Diese Aufgabe führt die bisher getrennt
behandelten Ebenen zusammen: Ein Formular wird in einem Template dargestellt, seine Daten in
einer View verarbeitet und über ein Model in der Datenbank gespeichert.

[ENDSECTION]

[SECTION::instructions::detailed]

Sie arbeiten weiter mit der App `webapp`. Aus den vorherigen Aufgaben stehen Ihnen bereits
das `Student`-Model ([PARTREF::django-model]), Views mit URL-Routing ([PARTREF::django-views])
und das Template-System ([PARTREF::django-template]) zur Verfügung. Alle Änderungen finden in
`webapp` statt.

### HTTP-Formulare: GET und POST

Ein HTML-Formular sendet seine Daten mit einer von zwei Methoden:

- **GET**: Die Daten werden sichtbar an die URL angehängt (`?q=...`). Geeignet für Anfragen,
  die nichts verändern (z. B. eine Suche), und die man als Link teilen können soll.
- **POST**: Die Daten werden im Request-Body übertragen und erscheinen nicht in der URL.
  Geeignet für Aktionen, die etwas verändern (z. B. einen Datensatz anlegen).

### GET-Formular: Suche

[ER] Erstellen Sie in `views.py` zwei View-Funktionen — eine zeigt das Suchformular an, die
andere verarbeitet die Suchanfrage:

[SNIPPET::ALT::django_form_search_views]
<!-- ER1 -->

[ER] Erstellen Sie das Template `search_form.html` mit einem Formular, das die
GET-Methode verwendet:

[SNIPPET::ALT::django_form_search_html]
<!-- ER2 -->

[ER] Ergänzen Sie `urls.py` um die beiden Routen:

[SNIPPET::ALT::django_form_urls_search]
<!-- ER3 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/search-form/` auf, geben Sie einen Suchbegriff ein und
senden Sie ab. Wie verändert sich die URL nach dem Absenden, und wo taucht Ihr Suchbegriff
auf? Wenn Sie einen anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ1 -->
<!-- time estimate: 20 min -->

### POST-Formular und CSRF-Schutz

Bei einem POST-Formular verlangt Django ein zusätzliches Sicherheitsmerkmal: das
`{% csrf_token %}`-Tag. **CSRF** (Cross-Site Request Forgery) bezeichnet einen Angriff, bei
dem eine fremde Website unbemerkt eine Aktion in Ihrem Namen auslöst, während Sie
eingeloggt sind. Um das zu verhindern, bettet Django in jedes Formular ein verstecktes,
einmaliges Token ein (`{% csrf_token %}`) und akzeptiert einen POST nur, wenn dieses Token
mitgeschickt wird — so kann eine fremde Seite kein gültiges Formular fälschen. Deshalb
gehört `{% csrf_token %}` in **jedes** POST-Formular.

[NOTICE]
In [PARTREF::django-views] hatten Sie eine POST-View versuchsweise mit `@csrf_exempt` vom
CSRF-Schutz ausgenommen, um sie ohne Formular testen zu können. Ab jetzt arbeiten Sie mit
echten Formularen und verwenden daher regulär `{% csrf_token %}` statt `@csrf_exempt`.
[ENDNOTICE]

[ER] Erstellen Sie in `views.py` eine View, die dieselbe Suche per POST verarbeitet:

[SNIPPET::ALT::django_form_searchpost_view]
<!-- ER4 -->

[ER] Erstellen Sie das Template `search_post.html` mit einem POST-Formular (inklusive
`{% csrf_token %}`):

[SNIPPET::ALT::django_form_searchpost_html]
<!-- ER5 -->

[ER] Ergänzen Sie `urls.py` um die neue Route:

[SNIPPET::ALT::django_form_urls_searchpost]
<!-- ER6 -->

[EQ] Suchen Sie unter `http://127.0.0.1:8071/search-post/` nach einem Begriff. Worin
unterscheidet sich die URL nach dem Absenden gegenüber dem GET-Formular aus [EREFQ::1], und
was würde passieren, wenn Sie `{% csrf_token %}` aus dem Formular entfernen? Wenn Sie einen
anderen Port verwenden, passen Sie den Link entsprechend an.
<!-- EQ2 -->
<!-- time estimate: 20 min -->

### Registrierung mit Datenbank-Persistenz

Bisher wurden die Formulardaten nur zurückgespiegelt. Jetzt speichern Sie sie dauerhaft:
Ein Registrierungsformular legt über `Student.objects.create()` (aus [PARTREF::django-model])
einen neuen Datensatz an und leitet anschließend auf dessen Detailseite (aus
[PARTREF::django-views]) weiter.

[ER] Erstellen Sie in `views.py` eine `register`-View, die bei einem POST einen neuen
`Student` anlegt und danach auf dessen Detailseite weiterleitet:

[SNIPPET::ALT::django_form_register_view]
<!-- ER7 -->

[HINT::Wie leite ich nach dem Speichern auf die Detailseite weiter?]
`Student.objects.create(...)` gibt das neu angelegte Objekt zurück. Weisen Sie es einer
Variablen zu (`student = Student.objects.create(...)`), dann steht Ihnen über `student.id`
die vom Datenbank vergebene ID zur Verfügung. Diese ID übergeben Sie an `reverse()`, um die
passende Detail-URL zu erzeugen: `redirect(reverse("student_detail", args=[student.id]))`.
[ENDHINT]

[ER] Erstellen Sie das Template `register.html` mit einem POST-Formular für Name, Alter und
E-Mail:

[SNIPPET::ALT::django_form_register_html]
<!-- ER8 -->

[ER] Ergänzen Sie `urls.py` um die Registrierungs-Route:

[SNIPPET::ALT::django_form_urls_register]
<!-- ER9 -->

[EQ] Öffnen Sie `http://127.0.0.1:8071/register/`, füllen Sie das Formular aus und senden
Sie es ab. Auf welcher Seite landen Sie danach, und woran erkennen Sie, dass Ihre Eingaben
tatsächlich in der Datenbank gespeichert wurden (und nicht nur zurückgespiegelt)? Warum ist
für diese Aktion POST die richtige Methode und nicht GET? Wenn Sie einen anderen Port
verwenden, passen Sie den Link entsprechend an.
<!-- EQ3 -->
<!-- time estimate: 25 min -->

### QueryDict: mehrere Werte pro Feld

`request.POST` ist ein QueryDict — ein Dictionary, das pro Schlüssel mehrere Werte halten
kann. Das ist relevant, wenn ein Formularfeld mehrfach vorkommt, etwa bei Checkboxen mit
demselben `name`. Zwei Methoden greifen unterschiedlich darauf zu:

- `request.POST.get("feld")`: liefert nur **einen** Wert (den letzten).
- `request.POST.getlist("feld")`: liefert **alle** Werte als Liste.

[ER] Erstellen Sie in `views.py` eine `survey`-View, die beide Zugriffe demonstriert:

[SNIPPET::ALT::django_form_survey_view]
<!-- ER10 -->

[ER] Erstellen Sie das Template `survey.html` mit mehreren Checkboxen, die denselben
`name` verwenden:

[SNIPPET::ALT::django_form_survey_html]
<!-- ER11 -->

[ER] Ergänzen Sie `urls.py` um die Umfrage-Route:

[SNIPPET::ALT::django_form_urls_survey]
<!-- ER12 -->

[EQ] Rufen Sie `http://127.0.0.1:8071/survey/` auf, kreuzen Sie **beide** Checkboxen an und
senden Sie ab. Welchen Wert zeigt `get("sprache")` und welchen `getlist("sprache")`? In
welcher Situation brauchen Sie zwingend `getlist()`? Wenn Sie einen anderen Port verwenden,
passen Sie den Link entsprechend an.
<!-- EQ4 -->
<!-- time estimate: 25 min -->

### Weiterführend

- [Working with forms](https://docs.djangoproject.com/en/stable/topics/forms/) – Überblick über die Formularverarbeitung in Django
- [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/stable/ref/csrf/) – Details zum CSRF-Schutz
- [QueryDict](https://docs.djangoproject.com/en/stable/ref/request-response/#querydict-objects) – Referenz zu QueryDict und seinen Methoden

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Kontrollergebnisse]

**Knackpunkte:**

- [EREFR::7] + [EREFQ::3]: Die `register`-View legt bei POST per `Student.objects.create()`
  einen Datensatz an und leitet mit `redirect(reverse("student_detail", args=[student.id]))`
  auf dessen Detailseite weiter; Student erkennt an der angezeigten Detailseite, dass die
  Daten tatsächlich gespeichert (nicht nur zurückgespiegelt) wurden.
- [EREFR::5]: Das POST-Formular enthält `{% csrf_token %}`; ohne dieses Token weist Django
  den POST mit einem 403-Fehler ab.
- [EREFQ::4]: Student erkennt, dass `get()` bei mehrfach vorkommendem Feld nur einen Wert
  liefert, `getlist()` dagegen alle — Letzteres ist bei Mehrfachauswahl (Checkboxen) nötig.

### Fragen und Python-Dateien
[INCLUDE::ALT:django-form.md]

### Kommandoprotokoll
[PROT::ALT:django-form.prot]

[ENDINSTRUCTOR]
