title: "Systemtests mit Playwright: Eine Webanwendung im Browser prüfen"
stage: alpha
timevalue: 2.0
difficulty: 2
explains: Systemtest, Flaky Test
assumes: m_pytest, venv, css-Selektoren
---

[SECTION::goal::trial]

- Ich kann mit Playwright und pytest [TERMREF2::Systemtest::-s] schreiben,
  die eine Webanwendung im Browser bedienen und das Ergebnis prüfen.
- Ich kann erklären, warum Playwright vor Aktionen und bei Prüfungen automatisch wartet
  und warum Tests dadurch zuverlässiger werden.
- Ich kann Elemente einer Webseite so auswählen, dass ein Test einen Umbau der Seite übersteht,
  und diese Wahl begründen.

[ENDSECTION]


[SECTION::background::default]

Unittests prüfen einzelne Funktionen.
Ob man etwa in einer Aufgabenliste im Browser tatsächlich einen Eintrag anlegen, abhaken und löschen kann,
zeigen sie nicht, denn dabei arbeiten HTML, CSS, JavaScript und Browser zusammen.
Ohne Werkzeug bleibt nur, sich vor jeder neuen Version von Hand durch die Anwendung zu klicken:
mühsam, langsam und so eintönig, dass man leicht etwas übersieht.

Playwright steuert einen echten Browser per Programm:
Es öffnet Seiten, tippt, klickt und prüft, was angezeigt wird.
Mit dem Plugin `pytest-playwright` schreiben Sie solche Tests als ganz normale pytest-Tests.
Tests, die die ganze Anwendung über ihre Bedienoberfläche prüfen, heißen
[TERMREF2::Systemtest::-s];
die Playwright-Dokumentation nennt sie "end-to-end tests".
Systemtests haben den Ruf, langsam zu sein und bei jeder Änderung der Oberfläche kaputtzugehen.
In dieser Aufgabe sehen Sie, woran das liegt und wie man es zumindest teilweise vermeidet.

[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Legen Sie für diese Aufgabe ein frisches [PARTREF::venv] an und aktivieren Sie es.
Installieren Sie dann Playwright samt pytest-Plugin
und einen Browser, den Playwright fernsteuern kann:

- `pip install pytest-playwright`
- `playwright install chromium`

Der zweite Befehl lädt einige hundert MB herunter.
Der Browser landet nicht im venv, sondern in einem Cache-Verzeichnis unterhalb Ihres
Home-Verzeichnisses.
Falls Playwright später meldet, dass dem Browser Systembibliotheken fehlen
(das kann unter Linux und WSL passieren),
installieren Sie diese mit `playwright install-deps chromium`;
der Befehl fragt nach Ihrem sudo-Passwort.

- [EC] `playwright --version`

Unser Testgegenstand ist eine Aufgabenliste, die das Playwright-Team zum Üben bereitstellt:
[HREF::https://demo.playwright.dev/todomvc]
Öffnen Sie die Seite in Ihrem gewohnten Browser und probieren Sie sie aus:
Legen Sie zwei Einträge an (Text eingeben, <kbd>Enter</kbd> drücken),
haken Sie einen davon ab, wechseln Sie zwischen den Filtern "All", "Active" und "Completed"
und löschen Sie schließlich einen Eintrag.
Achten Sie dabei auf den Zähler links unten.
Merken Sie sich, was Sie zum Löschen tun mussten; das wird später wichtig.

[HINT::Ich finde keine Möglichkeit zum Löschen]
Fahren Sie mit der Maus über einen Eintrag.
Rechts erscheint dann ein ×.
[ENDHINT]

<!-- time estimate: 15 min -->


### Ein erster Test

Lesen Sie auf der Seite "Writing tests" der Playwright-Dokumentation die Abschnitte
"First test", "Actions" und "Assertions":
[HREF::https://playwright.dev/python/docs/writing-tests]

Legen Sie ein Verzeichnis für diese Aufgabe an und darin die Datei `test_todo.py`:

```python
from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc"


def eintragen(page: Page, text: str):
    eingabe = page.get_by_placeholder("What needs to be done?")
    eingabe.fill(text)
    eingabe.press("Enter")


def test_neuer_eintrag(page: Page):
    page.goto(URL)
    eintragen(page, "Milch kaufen")
    expect(page.get_by_test_id("todo-title")).to_have_text("Milch kaufen")
```

Dazu einige Erläuterungen:

- `page` ist eine [TERMREF::Fixture], die `pytest-playwright` jedem Test bereitstellt,
  der einen Parameter mit diesem Namen hat.
  Sie steht für einen Browser-Tab in einer frischen Browserumgebung,
  ähnlich einem neuen privaten Fenster.
  Jeder Test beginnt also mit einer leeren Aufgabenliste.
- `get_by_placeholder` findet das Eingabefeld über seinen Platzhaltertext,
  also den grauen Hinweis im leeren Feld.
- `get_by_test_id` findet ein Element über sein Attribut `data-testid`.
  Solche Attribute bauen Entwickler eigens für Tests in ihre Seiten ein.
  Sie sehen sie, wenn Sie im Browser mit der rechten Maustaste auf ein Element klicken
  und "Untersuchen" wählen.
- `expect(...).to_have_text(...)` prüft, ob das Element genau diesen Text zeigt.

- [ER] Ergänzen Sie `test_neuer_eintrag` um eine Prüfung, dass der Zähler `1 item left` anzeigt.
  Verwenden Sie auch dafür `get_by_test_id`.

[HINT::Wie heißt die Test-ID des Zählers?]
Legen Sie im Browser einen Eintrag an, klicken Sie mit der rechten Maustaste auf
"1 item left" und wählen Sie "Untersuchen".
Im HTML sehen Sie dann das Element des Zählers mit seinem Attribut `data-testid`.
[ENDHINT]

- [EC] `pytest test_todo.py`

Einen Browser sehen Sie dabei nicht,
denn Playwright startet ihn normalerweise ohne Fenster (engl. _headless_).
Mit `pytest --headed --slowmo 500 test_todo.py` können Sie zusehen:
`--headed` öffnet ein Fenster und `--slowmo 500` verlangsamt jeden Schritt um 500 Millisekunden.
Falls das bei Ihnen (etwa unter WSL) nicht klappt, lassen Sie diesen Schritt aus.

<!-- time estimate: 20 min -->


### Den richtigen Eintrag finden

Die Objekte, die `page.get_by_placeholder(...)` und ähnliche Methoden liefern, heißen bei Playwright "Locator":
Sie beschreiben, wie man ein Element auf der Seite findet.
Lesen Sie auf der Seite "Locators" die Einleitung samt "Quick Guide"
und den Abschnitt "Locate by role":
[HREF::https://playwright.dev/python/docs/locators]

Playwright empfiehlt vor allem `get_by_role`.
Damit finden Sie Elemente über ihre Rolle
(Schaltfläche `button`, Checkbox `checkbox`, Link `link`, Listeneintrag `listitem` usw.)
und ihren Namen, also über das, was auch ein Screenreader einer blinden Person vorlesen würde.
Der Name stammt meist aus dem sichtbaren Text des Elements oder aus seinem Attribut `aria-label`.

- [ER] Schreiben Sie einen Test `test_erledigt`, der
    - die Einträge "Milch kaufen", "Brot backen" und "Käse reiben" anlegt,
    - "Milch kaufen" abhakt,
    - prüft, dass der Zähler `2 items left` anzeigt,
    - auf den Filter "Active" klickt und
    - prüft, dass "Brot backen" und "Käse reiben" zu sehen sind, "Milch kaufen" aber nicht.

  Verwenden Sie in diesem Test außer `eintragen` nur `get_by_role` und `get_by_text`;
  warum, sehen Sie im Teil "Gleiches Verhalten, anderes HTML".
  Passende Prüfungen sind `to_be_visible()` und `not_to_be_visible()`.

Zum Abhaken liegt `page.get_by_role("checkbox", name="Toggle Todo").check()` nahe,
denn so heißen die Checkboxen laut ihrem `aria-label`.
Schreiben Sie es zunächst so und lassen Sie den Test laufen.
Mit `pytest -k erledigt test_todo.py` laufen nur die Tests, deren Name `erledigt` enthält.

- [EQ] Was bemängelt Playwright?
  Warum ist es sinnvoll, dass Playwright hier abbricht,
  statt einfach die erste passende Checkbox anzuklicken?

Die Fehlermeldung schlägt auch gleich passende Locatoren vor.
Diese benutzen aber `get_by_label`; bleiben Sie trotzdem bei `get_by_role` und `get_by_text`.
Lesen Sie auf der Locators-Seite den Abschnitt "Filter by text"
und bauen Sie Ihren Test damit so um, dass er die richtige Checkbox abhakt und besteht.

[HINT::Wie finde ich die Checkbox im richtigen Eintrag?]
`page.get_by_role("listitem").filter(has_text="Milch kaufen")` findet den Listeneintrag,
der "Milch kaufen" enthält.

[HINT::Und wie komme ich von dort zur Checkbox?]
Rufen Sie auf diesem Locator erneut `get_by_role` auf;
dann sucht Playwright nur innerhalb dieses Eintrags.
Weil jeder Eintrag nur eine einzige Checkbox enthält, brauchen Sie dort keinen Namen anzugeben.
[ENDHINT]
[ENDHINT]

<!-- time estimate: 25 min -->


### Warten wie ein Mensch

- [ER] Schreiben Sie einen Test `test_loeschen`, der "Milch kaufen" anlegt,
  den Eintrag über das × löscht und prüft, dass "Milch kaufen" nicht mehr zu sehen ist.
  Das × ist eine Schaltfläche mit `aria-label="Delete"`;
  Sie finden sie also mit `page.get_by_role("button", name="Delete")`.

Lassen Sie den Test mit `pytest -k loeschen test_todo.py` laufen und haben Sie etwas Geduld.

- [EQ] Warum findet Playwright die Schaltfläche nicht, obwohl sie im HTML der Seite steht?
  Was hat Playwright während der Wartezeit getan?
  Für den zweiten Teil hilft die Einleitung der Seite "Auto-waiting":
  [HREF::https://playwright.dev/python/docs/actionability]

Ergänzen Sie den Test nun so, dass er besteht.
Tun Sie dazu dasselbe, was auch ein Mensch tun müsste.

[HINT::Was muss ein Mensch denn tun?]
Er muss mit der Maus über den Eintrag fahren.
Bei Playwright heißt das `hover()`.
[ENDHINT]

Auch `expect` wartet.
Ändern Sie in `test_neuer_eintrag` vorübergehend den erwarteten Zählerstand auf `2 items left`
und lassen Sie den Test mit `pytest -k neuer test_todo.py` laufen.
Achten Sie auf die Laufzeit und auf das "Call log" in der Fehlermeldung.
Ersetzen Sie die Prüfung dann durch dieses gewöhnliche `assert`
und lassen Sie den Test erneut laufen:

```python
assert page.get_by_test_id("todo-count").inner_text() == "2 items left"
```

Stellen Sie danach die ursprüngliche Prüfung mit `1 item left` wieder her.

- [EQ] Was tut `expect` anders als `assert`?
  Belegen Sie Ihre Antwort mit Ihren Beobachtungen zum "Call log" und zur Laufzeit.
- [EQ] Viele Webanwendungen zeigen das Ergebnis einer Aktion erst an,
  wenn die Antwort des Servers da ist, an einem schlechten Tag vielleicht eine Sekunde später.
  Wie würde sich in diesem Fall ein Test mit `assert` verhalten, wie einer mit `expect`?
  Warum wäre es keine gute Lösung, vor dem `assert` einfach `time.sleep(2)` einzufügen?

[HINT::Was ist an `time.sleep(2)` so schlecht?]
Denken Sie an zwei Fälle:
Der Server ist ausnahmsweise noch langsamer.
Und: Die Testsuite enthält 500 solcher Tests.
[ENDHINT]

Tests, die ohne jede Änderung am Code mal bestehen und mal fehlschlagen,
nennt man [TERMREF2::Flaky Test::-s] (engl. _flaky_: unzuverlässig).
Sie sind sehr lästig, weil man jedem Fehlschlag nachgehen muss
und sich schnell angewöhnt, Fehlschläge zu ignorieren.
Das automatische Warten von Playwright entschärft eine ihrer häufigsten Ursachen.

<!-- time estimate: 25 min -->


### Gleiches Verhalten, anderes HTML

Auf
[HREF::https://todomvc.com]
gibt es dieselbe Aufgabenliste in vielen Fassungen, gebaut mit verschiedenen Web-Frameworks.
Sie bieten dieselben Funktionen, unterscheiden sich aber im HTML und in manchen Details.
Für einen Test ist der Wechsel zu einer anderen Fassung wie ein großer Umbau der Oberfläche,
bei dem alle Funktionen erhalten bleiben.
Ein guter Systemtest sollte so etwas überstehen, solange sich das, was er prüft, nicht ändert.

Zum Vergleich brauchen wir noch einen Test, der ein Element über seine Position im HTML findet,
wie man es mit CSS-Selektoren tun kann.
Der Selektor `.todo-list li:nth-child(1) .toggle` bedeutet:
im Element mit der Klasse `todo-list` dasjenige `li`, das das erste Kind seines Elternelements ist,
und darin das Element mit der Klasse `toggle`.
Kurz: die Checkbox im ersten Eintrag der Liste.

- [ER] Kopieren Sie `test_erledigt` als `test_erledigt_css`
  und ändern Sie darin nur die Zeile zum Abhaken in
  `page.locator(".todo-list li:nth-child(1) .toggle").check()`.
- [EC] `pytest test_todo.py`

Alle vier Tests sollten bestehen.
Ändern Sie nun `URL` auf die Fassung, die mit reinem JavaScript ohne Framework gebaut ist:
`https://todomvc.com/examples/javascript-es6/dist/`.
Lassen Sie dann alle Tests erneut laufen.
Die Option `--tb=line` kürzt die Fehlermeldungen etwas; der Lauf dauert knapp eine Minute.

- [EC] `pytest --tb=line test_todo.py`

Setzen Sie `URL` danach wieder auf die Demo-Seite zurück.

- [EQ] Welche Tests schlagen fehl, und an welchem Locator liegt es jeweils?
  Vergleichen Sie dazu im Browser mit "Untersuchen" das HTML der beiden Fassungen.
- [EQ] `test_erledigt_css` scheitert nicht in der Zeile mit dem CSS-Selektor, sondern später.
  Was ist tatsächlich passiert?
  Warum ist das tückischer als ein Locator, der gar kein Element findet?

[HINT::Ich verstehe nicht, was in `test_erledigt_css` passiert ist]
Legen Sie in der neuen Fassung von Hand drei Einträge an und achten Sie auf ihre Reihenfolge.
[ENDHINT]

- [EQ] Welche Arten von Locatoren haben den Wechsel überstanden, welche nicht?
  Formulieren Sie daraus eine Faustregel für die Wahl von Locatoren.
  Wann ist es dagegen richtig, dass ein Systemtest nach einer Änderung der Oberfläche scheitert?

<!-- time estimate: 25 min -->


### Einordnen

- [EQ] Wie lange haben Ihre vier Tests auf der Demo-Seite zusammen gebraucht
  (siehe [EREFC::3])?
  Vergleichen Sie das mit Unittests, wie Sie sie aus [PARTREF::m_pytest] kennen.
  Wofür würden Sie in einem Projekt wie dieser Aufgabenliste Systemtests schreiben,
  wofür lieber Unittests?

<!-- time estimate: 10 min -->

[ENDSECTION]


[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
Der fehlschlagende Lauf [EREFC::4] gehört ausdrücklich in das Protokoll.

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint ist `test_todo.py` im Endzustand, mit der URL der Demo-Seite.)

[ENDSECTION]


[INSTRUCTOR::Warten und Robustheit von Locatoren verstanden?]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:Playwright.prot]

[ENDINSTRUCTOR]
