title: "BugsInPy: echte Defekte nachstellen und Regressionstests schreiben"
stage: alpha
timevalue: 2.0
difficulty: 2
explains: Regressionstest, Defektaufdeckender Test
assumes: m_pytest, venv, pip, Git101, Fehler-Defekt-Versagen, flake8, FastAPI-GET
---

[SECTION::goal::trial]

- Ich kann einen realen, dokumentierten Defekt aus der Sammlung BugsInPy nachstellen
  und mit Testläufen zeigen, welcher Test ihn aufdeckt.
- Ich kann für einen realen Defekt einen Regressionstest schreiben,
  der auf der defekten Version fehlschlägt und auf der korrigierten besteht.
- Ich kann begründen, warum eine Testsuite einen Defekt übersehen hat.

[ENDSECTION]

[SECTION::background::default]
Die Defekte in Übungsaufgaben sind meist ausgedacht und liegen dort, wo man sie sucht.
Echte Defekte stecken in fremdem Code, sind oft unscheinbar
und sind an der Testsuite ihres Projekts unbemerkt vorbeigekommen.

BugsInPy ist eine Sammlung von rund 500 solchen Defekten
aus 17 bekannten Python-Projekten wie pandas, black oder FastAPI.
Zu jedem Defekt ist festgehalten, in welchem Commit er steckt, mit welchem Commit er behoben wurde
und welcher Test ihn sichtbar macht.
Gesammelt wurden die Defekte für die Forschung,
etwa um Werkzeuge zur automatischen Defektsuche an echten Fällen zu erproben.
Für Sie ist die Sammlung ein Übungsgelände:
Sie stellen echte Defekte nach, sehen, wie sie behoben wurden,
und schreiben selbst einen Test, der dafür sorgt, dass ein Defekt nicht unbemerkt wiederkommt.
[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitung

- Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein `venv` für diese Aufgabe an und aktivieren Sie es
  (siehe [PARTREF::venv]):
  `python -m venv venv_bugsinpy` und `source venv_bugsinpy/bin/activate`.
  Alle folgenden Kommandos führen Sie in diesem `venv` aus.
  Ihr übliches `venv` eignet sich dafür nicht:
  Sie installieren hier alte Paketversionen wie Pydantic 1,
  die dort andere Aufgaben stören würden.
- Klonen Sie BugsInPy in Ihren Hilfsbereich und wechseln Sie in das neue Verzeichnis:
  `git clone https://github.com/soarsmu/BugsInPy.git` und `cd BugsInPy`.

<!-- time estimate: 5 min -->

### Ein Eintrag in BugsInPy

Jeder Defekt hat in BugsInPy ein eigenes Verzeichnis `projects/<Projekt>/bugs/<Nummer>`.
Wir beginnen mit Defekt Nr. 3 des Projekts PySnooper.
PySnooper ist ein kleines Debugging-Werkzeug:
Wer eine Funktion mit `@pysnooper.snoop()` [TERMREF2::Decorator::dekoriert],
bekommt bei jedem Aufruf ein Protokoll aller ausgeführten Zeilen und aller geänderten Variablen.
Mit `@pysnooper.snoop('/pfad/zur/datei.log')` landet dieses Protokoll in einer Datei
statt auf dem Bildschirm.

Sehen Sie sich mit `ls` an, welche Dateien im Verzeichnis `projects/PySnooper/bugs/3` liegen,
und lesen Sie die beiden wichtigsten:

[EC] `cat projects/PySnooper/bugs/3/bug.info projects/PySnooper/bugs/3/run_test.sh`

Lesen Sie auch `requirements.txt` und `setup.sh`.
Nur `bug_patch.txt` heben Sie sich noch auf:
Darin steht die Korrektur, und den Defekt sollen Sie zunächst selbst finden.

[NOTICE]
BugsInPy bringt eigene Skripte mit, die die folgenden Schritte automatisieren
(`bugsinpy-checkout`, `bugsinpy-compile`, `bugsinpy-test`).
Wir gehen die Schritte hier von Hand durch.
Das ist lehrreicher, und die Skripte laufen nicht überall
(sie brauchen beispielsweise `bash` ab Version 4 und `dos2unix`).
[ENDNOTICE]

<!-- time estimate: 5 min -->

### Den Defekt nachstellen

Klonen Sie PySnooper in Ihren Hilfsbereich, also neben das Verzeichnis `BugsInPy` und nicht hinein,
und wechseln Sie in das neue Verzeichnis:
`git clone https://github.com/cool-RR/PySnooper.git` und `cd PySnooper`.

Wechseln Sie nun auf den defekten Stand (`buggy_commit_id`).
Git genügen dafür die ersten sieben Zeichen der Commit-ID:

[EC] `git checkout 6e3d797`

Die lange Meldung zu _detached HEAD_ besagt nur, dass Sie gerade auf keinem Branch arbeiten,
sondern sich einen alten Stand ansehen.
Das ist hier genau richtig.

#### Abhängigkeiten von PySnooper bereitstellen

Installieren Sie die Pakete, die PySnooper in diesem Stand für sich selbst
und für seine Tests braucht.
Sie stehen in den Dateien `requirements.txt` und `test_requirements.txt` von PySnooper:
`pip install -r requirements.txt -r test_requirements.txt`.

Die gleichnamige Datei `requirements.txt` im BugsInPy-Eintrag ist bei diesem Defekt leer;
bei vielen anderen Defekten legt sie die Versionen aller Pakete genau fest.
`setup.sh` installiert PySnooper samt seinen Abhängigkeiten
mit dem veralteten `python setup.py install`; das brauchen wir hier nicht.

#### Tests ausführen

Führen Sie nun den Test aus `run_test.sh` aus.
Wir rufen `pytest` dabei als `python -m pytest` auf;
so findet Python das Paket `pysnooper` im aktuellen Verzeichnis,
ohne dass Sie es installieren müssen.
`tests/test_pysnooper.py::test_file_output` wählt aus der Datei nur die eine Testfunktion aus.
`-q` (_quiet_) kürzt die Ausgabe.
Die Option `-s` lassen wir weg:
Sie zeigt Ausgaben der Tests sofort an, statt sie abzufangen; das brauchen wir hier nicht.

[EC] `python -m pytest -q tests/test_pysnooper.py::test_file_output`

`pytest` findet den Test nicht, denn im defekten Stand gibt es ihn noch gar nicht:
Er entstand erst zusammen mit der Korrektur.
Deshalb kombiniert BugsInPy beim Nachstellen beide Stände:
den Code aus dem defekten Commit und die in `test_file` genannte Testdatei aus dem korrigierten.
Holen Sie sich diese eine Datei aus dem korrigierten Commit (`fixed_commit_id`);
alles andere bleibt auf dem defekten Stand:
`git checkout 15555ed -- tests/test_pysnooper.py`.

[EC] `python -m pytest -q tests/test_pysnooper.py::test_file_output`

[EQ] Beschreiben Sie das [TERMREF::Versagen]:
Was erlebt jemand, der PySnooper so benutzt wie dieser Test?
Bestimmen Sie anhand der Ausgabe von `pytest` den [TERMREF::Defekt]:
In welcher Datei und Zeile steckt er, und was ist dort falsch?

[HINT::Die Ausgabe von `pytest` ist mir zu lang]
Lesen Sie sie von unten nach oben.
Die Zeile, die mit `E` beginnt, nennt die Ausnahme;
kurz darunter steht, in welcher Datei und Zeile sie auftrat.
Die Abschnitte darüber zeigen, über welche Aufrufe der Test dorthin gelangt ist.
[ENDHINT]

Vergleichen Sie Ihre Antwort erst jetzt mit `bug_patch.txt` im BugsInPy-Eintrag.

[EQ] Verallgemeinern Sie Ihr Vorgehen:
Mit welchen Kommandos stellt man einen beliebigen Defekt aus BugsInPy nach
und lässt den Test aus `run_test.sh` laufen,
wenn das Repo des Projekts schon geklont ist und alle Pakete installiert sind?
Schreiben Sie Platzhalter wie `<buggy_commit_id>` überall dort,
wo eine Angabe aus dem Eintrag einfließt,
und nennen Sie zu jedem Platzhalter die Datei, aus der die Angabe stammt.

<!-- time estimate: 25 min -->

### Welcher Test zeigt den Defekt?

Bisher haben Sie nur den einen Test ausgeführt, den BugsInPy nennt.
Lassen Sie jetzt die ganze Testsuite laufen.
`--tb=no` unterdrückt die langen Tracebacks; die Zusammenfassung am Ende genügt.

[EC] `python -m pytest -q --tb=no tests`

Außer `test_file_output` schlägt noch ein zweiter Test fehl.
Ob auch er etwas mit dem Defekt zu tun hat, zeigt ein Vergleich mit dem korrigierten Stand.
Wechseln Sie dorthin und wiederholen Sie den Testlauf.
Die Testdatei, die Sie vorhin geholt haben, stimmt mit der des korrigierten Stands überein,
deshalb lässt Git Sie ohne Weiteres wechseln.

[EC] `git checkout 15555ed`

[EC] `python -m pytest -q --tb=no tests`

[EQ] Welcher der beiden fehlgeschlagenen Tests zeigt Defekt Nr. 3, welcher nicht?
Begründen Sie Ihre Antwort mit den beiden Testläufen.
Formulieren Sie daraus eine allgemeine Regel:
Woran erkennt man, ob ein fehlschlagender Test einen bestimmten Defekt zeigt?

<!-- time estimate: 10 min -->

### Warum hat das niemand bemerkt?

Mit diesem Defekt konnte PySnooper sein Protokoll in keine einzige Datei schreiben.
Trotzdem hat keiner der Tests, die es vor der Korrektur gab, etwas davon gemerkt.

[EQ] Woran lag das?
Sehen Sie sich dazu in `tests/test_pysnooper.py` an,
womit die übrigen Tests `pysnooper.snoop(...)` aufrufen.
Und warum meldet Python den Defekt nicht schon beim `import pysnooper`?

Ein Werkzeug, das ganz ohne Tests auskommt, hätte diesen Defekt sofort gemeldet:
ein [TERMREF::Linter] wie `flake8`, den Sie aus [PARTREF::flake8] kennen.
Probieren Sie das aus.
Wechseln Sie dafür noch einmal auf den defekten Stand (`git checkout 6e3d797`)
und installieren Sie `flake8` in Ihr `venv` (`pip install flake8`).

[EC] `flake8 --select=F pysnooper/pysnooper.py`

[HINT::Ich weiß nicht, was `--select=F` bewirkt]
Mit `--select=F` beschränken Sie `flake8` auf die Meldungen mit `F`-Code;
sie stammen von pyflakes und weisen auf mögliche Programmierfehler hin statt auf Stilfragen.
[ENDHINT]

[EQ] Welche der Meldungen zeigt den Defekt, und was besagen die übrigen?
Wie kann `flake8` den Defekt finden, ohne den Code auszuführen?

[HINT::Ich verstehe die Meldungscodes nicht]
Die Bedeutung der `F`-Codes steht in der
[Liste der Meldungscodes von flake8](https://flake8.pycqa.org/en/stable/user/error-codes.html).
[ENDHINT]

[NOTICE]
Hineingeraten war der Defekt übrigens einen Tag vor seiner Korrektur, bei einem Umbau des Codes:
Die Zeile, die `output_path` definierte, fiel dabei weg;
die Zeile, die es benutzte, wurde umgeschrieben und blieb.
[ENDNOTICE]

<!-- time estimate: 15 min -->

### Ein zweiter Defekt: Diesmal schreiben Sie den Test

Einen Test wie `test_file_output`, der auf dem defekten Stand fehlschlägt
und auf dem korrigierten besteht, nennt man
[TERMREF2::Defektaufdeckender Test::defektaufdeckend]
(engl. meist _fail-to-pass test_ oder _triggering test_).
Genau solche Tests nennt BugsInPy in `run_test.sh`.
Beim ersten Defekt hatten die Entwickler den defektaufdeckenden Test schon geschrieben.
Beim zweiten schreiben Sie ihn selbst, bevor Sie sich die Korrektur ansehen.

Es geht um Defekt Nr. 5 des Projekts fastapi,
also um das Web-Framework, das Sie aus [PARTREF::FastAPI-GET] kennen.
Den BugsInPy-Eintrag dazu sehen Sie sich diesmal erst am Ende an,
denn schon die Dateinamen darin verraten zu viel.

Klonen Sie FastAPI in Ihren Hilfsbereich, also neben `BugsInPy` und `PySnooper`
(das Repo ist knapp 100 MB groß), und wechseln Sie in das neue Verzeichnis:
`git clone https://github.com/fastapi/fastapi.git` und `cd fastapi`.
Wechseln Sie dann auf den defekten Stand:

[EC] `git checkout 7cea84b`

#### Abhängigkeiten von FastAPI bereitstellen

Welche Pakete FastAPI in diesem Stand braucht, steht in `pyproject.toml`
im Abschnitt `[tool.flit.metadata]` unter `requires`:
Starlette, das Web-Framework, auf dem FastAPI aufbaut, in genau der Version 0.12.9,
und Pydantic in einer Version vor 2.
Für den Testclient, den Sie gleich kennenlernen, kommt `requests` hinzu:
`pip install "starlette==0.12.9" "pydantic<2" requests`.

Die `requirements.txt` im BugsInPy-Eintrag installieren Sie auch diesmal nicht.
Sie legt zahlreiche Pakete genau auf ihren Stand von 2020 fest, passend zu Python 3.8.
Mit Python 3.13 etwa scheitert ihre Installation an `orjson==3.0.2`,
für das es dort kein fertiges Paket gibt.


#### Was `response_model` leisten soll

In [PARTREF::FastAPI-GET] haben Sie das Antwortmodell eines Endpunkts
als Rückgabetyp der Funktion angegeben, etwa `-> Greetings`.
Gleichwertig ist der Parameter `response_model` des Decorators:

```python
@app.get("/user", response_model=User)
def read_user():
    ...
```

Im defekten Stand (FastAPI 0.47) funktioniert nur diese Schreibweise;
den Rückgabetyp wertet FastAPI erst seit Version 0.89 aus.
Ein Endpunkt, der sein Antwortmodell nur als Rückgabetyp angibt, filtert hier also gar nichts,
weder im defekten noch im korrigierten Stand.
Geben Sie das Antwortmodell in dieser Aufgabe deshalb immer mit `response_model=` an.

FastAPI wandelt den Rückgabewert in das `response_model` um
und gibt nur die Felder aus, die das Modell deklariert.
Das ist vor allem für die Sicherheit wichtig:
Ein Endpunkt darf intern ein Objekt mit Passwort zurückgeben,
und das `response_model` sorgt dafür, dass das Passwort nicht in der Antwort landet.
Das gilt ausdrücklich auch dann, wenn die Klasse des Objekts von der des `response_model` erbt.
Nachlesen können Sie das in der FastAPI-Dokumentation unter
[Response Model](https://fastapi.tiangolo.com/tutorial/response-model/),
Abschnitt „FastAPI Data Filtering“.

Eine Anwendung verwendet dafür diese beiden Modelle:

```python
class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str
```

Intern hält die Anwendung Benutzer als `UserInDB`.
Nach außen sollen alle Endpunkte nur die Felder von `User` zeigen.
Stellen Sie sich dazu folgenden Problembericht vor:

> Obwohl kein `response_model` unserer Anwendung ein Feld `hashed_password` enthält,
> taucht es in manchen Antworten auf.

#### Endpunkte testen, ohne einen Server zu starten

Um einen Endpunkt zu testen, brauchen Sie keinen laufenden Server.
Ein `TestClient` schickt Anfragen direkt an Ihre Anwendung und liefert die Antwort zurück.
Ein Test sieht zum Beispiel so aus:

```python
from fastapi import FastAPI
from starlette.testclient import TestClient

app = FastAPI()


@app.get("/hello")
def hello():
    return {"hello": "World"}


client = TestClient(app)


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"hello": "World"}
```

Heutige FastAPI-Versionen bieten denselben Testclient auch als `fastapi.testclient` an
(siehe [Testing](https://fastapi.tiangolo.com/tutorial/testing/)).
Im defekten Stand gibt es diesen Namen noch nicht,
deshalb importieren Sie den Testclient hier direkt aus Starlette.

Speichern Sie das Beispiel im FastAPI-Repo als `tests/test_hello.py` und führen Sie es aus.
Besteht der Test, sind alle nötigen Pakete installiert.

[EC] `python -m pytest -q tests/test_hello.py`

Warnungen vom Typ `DeprecationWarning` aus dem Code von Starlette oder FastAPI
rühren daher, dass alter Code auf neuem Python läuft, und sind hier harmlos.

#### Den Regressionstest schreiben

Ein [TERMREF::Regressionstest] soll sicherstellen, dass etwas, das einmal funktioniert hat,
nach späteren Änderungen weiterhin funktioniert.
Eine wichtige Art von Regressionstest entsteht zusammen mit der Korrektur eines Defekts:
Er bleibt fortan in der Testsuite und läuft bei jeder späteren Änderung mit,
sodass der Defekt nicht unbemerkt zurückkehren kann.
Einen solchen schreiben Sie jetzt.

[ER] Legen Sie im FastAPI-Repo die Datei `tests/test_response_model_regression.py` an.
Bauen Sie darin mit den beiden Modellen oben eine kleine FastAPI-Anwendung,
deren Endpunkte intern `UserInDB`-Objekte verwenden,
per `response_model` nach außen aber nur die Felder von `User` zeigen sollen.
Schreiben Sie Testfunktionen, die mit einem `TestClient` prüfen, was in den Antworten steht.
Leiten Sie die erwarteten Antworten aus der Beschreibung oben ab, nicht aus dem Code von FastAPI.
Mindestens ein Test soll den Defekt aus dem Problembericht aufdecken.

[EC] `python -m pytest -q tests/test_response_model_regression.py`

[HINT::Alle meine Tests bestehen schon auf dem defekten Stand]
Grün ist hier ausnahmsweise eine schlechte Nachricht:
Dann trifft noch keiner Ihrer Tests den Defekt.
Der Problembericht spricht von _manchen_ Antworten.
Auf welche Weise kann ein Benutzer in einer Antwort stecken,
außer als unmittelbarer Rückgabewert eines Endpunkts?

[HINT::Ich finde den fehlenden Fall trotzdem nicht]
Bauen Sie ein Modell, das einen `User` als Feld enthält,
etwa ein Profil mit den Feldern `bio: str` und `user: User`.
Geben Sie in einem Endpunkt mit diesem `response_model` ein Profil zurück,
dessen `user` ein `UserInDB`-Objekt ist.

[ENDHINT]

[ENDHINT]

Sobald einer Ihrer Tests fehlschlägt, wechseln Sie auf den korrigierten Stand.
Ihre Testdatei gehört zu keinem der beiden Commits;
Git lässt sie deshalb beim Wechsel unverändert stehen.

[EC] `git checkout 75a07f2`

[EC] `python -m pytest -q tests/test_response_model_regression.py`

Jetzt sollten alle Ihre Tests bestehen.
Schlägt noch einer fehl, prüfen Sie, ob seine Erwartung wirklich aus der Beschreibung folgt,
und korrigieren Sie gegebenenfalls den Test.
Haben Sie dabei die Testdatei geändert, wiederholen Sie beide Läufe:
zuerst auf dem defekten Stand (`git checkout 7cea84b`),
dann auf dem korrigierten (`git checkout 75a07f2`).
Nur so zeigt Ihr Kommandoprotokoll, dass die abgegebene Fassung auf dem defekten Stand fehlschlägt
und auf dem korrigierten besteht.

Die Korrektur ändert in `fastapi/utils.py` eine einzige Zeile von `create_cloned_field()`:
Aus `use_type.__fields__[f.name] = f`
wurde `use_type.__fields__[f.name] = create_cloned_field(f)`.

#### Mit den Tests der Entwickler vergleichen

Die Entwickler haben mit der Korrektur die Datei `tests/test_filter_pydantic_sub_model.py`
angelegt; lesen Sie sie.
Der Endpunkt darin holt sich sein `ModelC`-Objekt per `Depends`
(siehe [PARTREF::FastAPI-Dependency-Injection]);
für diese Aufgabe genügt es zu wissen, dass `model_c` ein `ModelC`-Objekt samt Passwort ist.
Welche ihrer Testfunktionen den Defekt aufdeckt, zeigt derselbe Trick wie bei BugsInPy:
defekter Code, aber die Tests aus dem korrigierten Stand.
Außer der neuen Testdatei hat die Korrektur nur `fastapi/utils.py` geändert;
holen Sie sich diese eine Datei aus dem defekten Commit:
`git checkout 7cea84b -- fastapi/utils.py`.
`-rA` listet am Ende jeden Test mit seinem Ergebnis auf.

[EC] `python -m pytest -q -rA --tb=no tests/test_filter_pydantic_sub_model.py`

Stellen Sie danach den korrigierten Stand wieder her: `git checkout 75a07f2 -- fastapi/utils.py`.

Erst jetzt sehen Sie sich den BugsInPy-Eintrag zu diesem Defekt an.
Wechseln Sie dafür zurück in das Verzeichnis `BugsInPy`.

[EC] `cat projects/fastapi/bugs/5/bug.info projects/fastapi/bugs/5/run_test.sh`

[EQ] Die Entwickler haben zwei Testfunktionen geschrieben, `run_test.sh` nennt nur eine davon.
Warum deckt die andere den Defekt nicht auf, obwohl sie dieselbe Anwendung testet?
Was folgt daraus für das Schreiben von Regressionstests?

Kopieren Sie Ihre Datei `test_response_model_regression.py` zur Abgabe
in Ihren [TERMREF::Arbeitsbereich].

<!-- time estimate: 50 min -->

### Reflexion

[EQ] Hätte `flake8` auch den Defekt in `create_cloned_field()` gemeldet?
Begründen Sie Ihre Antwort.
Was folgt aus Ihren beiden Defekten für die Arbeitsteilung zwischen Linter und Tests?

<!-- time estimate: 5 min -->

[ENDSECTION]

[SECTION::submission::reflection,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]
[INCLUDE::ALT:]
[PROT::ALT:pytest_bugsinpy.prot]
[ENDINSTRUCTOR]
