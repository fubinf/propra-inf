title: Importe automatisch ordnen mit isort
stage: alpha
timevalue: 1.25
difficulty: 2
assumes: venv, flake8, black
---

[SECTION::goal::trial]

- Ich kann die Importe einer Python-Datei mit `isort` ordnen lassen und vorab prüfen, was es ändern würde.
- Ich weiß, welche Import-Regeln aus PEP 8 `isort` umsetzt und was es `flake8` überlässt.
- Ich weiß, woran `isort` erkennt, ob ein Import zum eigenen Projekt gehört,
  und warum dafür eine Konfigurationsdatei wichtig ist.
- Ich kann `isort` so konfigurieren, dass es mit `black` zusammenarbeitet.

[ENDSECTION]
[SECTION::background::default]

In gewachsenem Python-Code stehen die `import`-Anweisungen oft in der Reihenfolge,
in der sie jemandem eingefallen sind.
Dann sieht man schlecht, wovon eine Datei abhängt.
Außerdem hängen bei Teamarbeit oft zwei Personen ihre neuen Importe an derselben Stelle an,
was unnötige Merge-Konflikte erzeugt.

`isort` ist ein [TERMREF::Codeformatierer] speziell für Importe:
Es gruppiert und sortiert sie nach festen Regeln und bringt sie in eine einheitliche Form.
Die Aufgabe knüpft an [PARTREF::flake8] und [PARTREF::black] an.

[ENDSECTION]
[SECTION::instructions::detailed]

### Testprojekt anlegen

Legen Sie für diese Aufgabe ein frisches [PARTREF::venv] an und aktivieren Sie es.

- [EC] `pip install isort black flake8`

Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein Verzeichnis `isort_demo` an.
Führen Sie alle Kommandos dort aus, sofern nichts anderes gesagt ist.

Legen Sie darin die Datei `textstats.py` an, eine kleine Bibliothek für Textstatistiken.
Ihren Inhalt müssen Sie nicht lesen, nur übernehmen:

[FOLDOUT::Inhalt von `textstats.py`]
```python
from collections import Counter


def count_words(text):
    return len(text.split())


def unique_words(text):
    return len(set(text.lower().split()))


def longest_word(text):
    return max(text.split(), key=len)


def average_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words)


def most_common_words(text, n):
    return Counter(text.lower().split()).most_common(n)
```
[ENDFOLDOUT]

Legen Sie außerdem das Programm `report.py` an, das diese Bibliothek benutzt.
Es ist über längere Zeit gewachsen; seine Importe stehen in der Reihenfolge, in der sie dazugekommen sind:

[FOLDOUT::Inhalt von `report.py`]
```python
import sys
from textstats import most_common_words
import os, json
import requests
from pathlib import Path
from textstats import longest_word, unique_words
from datetime import date
from textstats import count_words
import argparse
from collections import defaultdict
from textstats import average_word_length


def read_text(source):
    if source.startswith("http"):
        return requests.get(source).text
    return Path(source).read_text()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    args = parser.parse_args()
    text = read_text(args.source)
    result = {
        "date": str(date.today()),
        "words": count_words(text),
        "unique": unique_words(text),
        "longest": longest_word(text),
        "average": round(average_word_length(text), 2),
        "top": most_common_words(text, 3),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```
[ENDFOLDOUT]

Ausführen müssen Sie `report.py` nicht.
Installieren Sie die Bibliothek `requests` deshalb bitte auch _nicht_.

<!-- time estimate: 10 min -->


### Was `flake8` zu den Importen sagt

- [EC] `flake8 report.py`
- Lesen Sie in [TERMREF::PEP8] den Abschnitt
  [Imports](https://peps.python.org/pep-0008/#imports).
- [EQ] Gegen welche Regeln aus diesem Abschnitt verstößt `report.py`?
  Welche dieser Verstöße meldet `flake8`, welche nicht?

<!-- time estimate: 10 min -->


### Importe ordnen

- [EC] `isort --diff report.py`
  (Mit `--diff` zeigt `isort` nur an, was es ändern würde, und lässt die Datei unverändert.)
- [EQ] Nach welchen Regeln ordnet `isort` die Importe?
  Achten Sie auf die Gruppen, auf die Reihenfolge innerhalb einer Gruppe
  und darauf, was mit den Importen aus `textstats` geschieht.
  Welche dieser Regeln verlangt PEP 8, welche sind Zusatzregeln von `isort`?
- [EC] `isort report.py`
- [EC] `flake8 report.py`
- [EQ] Welche `flake8`-Meldungen hat `isort` beseitigt, welche nicht?
  Warum entfernt `isort` ungenutzte Importe nicht einfach mit?

[HINT::Ich weiß nicht, warum `isort` ungenutzte Importe stehen lässt]

Überlegen Sie, welchen Teil der Datei `isort` untersuchen müsste, um festzustellen, ob ein Import benutzt wird.
Und: Beim ersten Import eines Moduls wird dessen Code ausgeführt.
Kann es also sein, dass ein Import gebraucht wird, obwohl der importierte Name nirgends vorkommt?

[ENDHINT]

- [ER] Entfernen Sie die ungenutzten Importe von Hand aus `report.py`.
- [EC] `flake8 report.py`
  (Jetzt sollte keine Meldung mehr erscheinen.)

Beim ersten Import eines Moduls wird dessen Code ausgeführt.
Deshalb kann in seltenen Fällen auch die _Reihenfolge_ der Importe eine Rolle spielen,
etwa wenn ein Modul beim Import ein anderes umkonfiguriert.
`isort` geht davon aus, dass die Reihenfolge keine Rolle spielt, und das stimmt fast immer.
Für die Ausnahmen kann man `isort` mit Kommentaren wie `# isort: skip` stellenweise abschalten, siehe
[Action Comments](https://isort.readthedocs.io/en/latest/configuration/action_comments.html).

<!-- time estimate: 15 min -->


### Woher weiß `isort`, was zum Projekt gehört?

`isort` hat `requests` als Fremdbibliothek (`THIRDPARTY`) eingeordnet,
obwohl es in Ihrem venv gar nicht installiert ist,
und `textstats` als Teil Ihres Projekts (`FIRSTPARTY`).
Wir sehen uns an, wie diese Einordnung zustande kommt.

- Wechseln Sie mit `cd ..` in das übergeordnete Verzeichnis.
- [EC] `isort --diff isort_demo/report.py`
- `isort --show-config` zeigt alle Einstellungen, die `isort` für eine Datei verwendet.
  Uns interessiert davon nur `src_paths`.
- [EC] `isort --show-config isort_demo/report.py | grep -A3 '^    "src_paths"'`
  (Der Eintrag `"src_paths"` kommt in der Ausgabe zweimal vor;
  `^` und genau vier Leerzeichen wählen den äußeren aus, `-A3` zeigt die drei folgenden Zeilen mit.)
- Lesen Sie die Beschreibungen der Optionen
  [`src_paths`](https://isort.readthedocs.io/en/latest/configuration/options.html#src-paths)
  und
  [`default_section`](https://isort.readthedocs.io/en/latest/configuration/options.html#default-section).
- [EQ] Warum ordnet `isort` `textstats` jetzt anders ein als vorhin?
  Warum landet `requests` in beiden Fällen bei den Fremdbibliotheken?
  Welches Problem entsteht daraus in einem Team, in dem nicht alle `isort` aus demselben Verzeichnis aufrufen?

[HINT::Laut Dokumentation ist `src_paths` leer, aber die Ausgabe zeigt zwei Pfade]

Ist `src_paths` nicht gesetzt, verwendet `isort` ersatzweise ein Basisverzeichnis und dessen Unterverzeichnis `src`.
Welches Basisverzeichnis das hier ist, sehen Sie in der Ausgabe.
Vergleichen Sie es mit dem Ort, an dem `textstats.py` liegt.

[ENDHINT]

- Wechseln Sie mit `cd isort_demo` zurück.

<!-- time estimate: 15 min -->


### `isort` und `black` zusammen einsetzen

In der Praxis setzt man `isort` meist zusammen mit `black` ein.
Probieren wir das aus.

- [EC] `black report.py`
- [EC] `isort --check-only --diff report.py; echo $?`

[NOTICE]
`--check-only` ändert die Datei nicht, sondern prüft nur.
  `echo $?` zeigt den Exit-Status des vorigen Kommandos:
  0 heißt "nichts zu ändern", 1 heißt "die Datei würde geändert".
  An diesem Status erkennt z.B. eine [TERMREF::CI/CD]-Pipeline, ob eine Prüfung bestanden ist.
[ENDNOTICE]

- [EQ] Was hat `black` an den Importen geändert, und was würde `isort` daraus wieder machen?
  Was würde in einer Pipeline passieren, die nacheinander `isort --check-only` und `black --check` ausführt?

[HINT::Ich weiß nicht, was in der Pipeline passieren würde]

Die Pipeline prüft den Code, den jemand eingecheckt hat.
Spielen Sie durch, was passiert, wenn diese Person vorher erst `isort` und dann `black` auf die Datei
angewendet hat, und was, wenn sie es in umgekehrter Reihenfolge getan hat.

[ENDHINT]

Wie man das Problem löst, beschreibt die `isort`-Dokumentation unter
[Compatibility with black](https://isort.readthedocs.io/en/latest/configuration/black_compatibility.html).
Wie `black` kann auch `isort` seine Einstellungen aus der Datei `pyproject.toml` lesen,
und zwar aus dem Abschnitt `[tool.isort]`.

- [ER] Legen Sie in `isort_demo` eine Datei `pyproject.toml` an, die `isort` auf `black` einstellt.
- [EC] `isort --check-only --diff report.py; echo $?`
- [EC] `black --check report.py`
- [EQ] Welche Einstellungen des Profils `black` sorgen dafür, dass `isort` den `textstats`-Import
  jetzt genauso umbricht wie `black`?
  Die Einstellungen des Profils finden Sie unter
  [Built-in profiles](https://isort.readthedocs.io/en/latest/configuration/profiles.html)
  im Abschnitt `black`, die Bedeutung der Zahlenwerte unter
  [Multi line output modes](https://isort.readthedocs.io/en/latest/configuration/multi_line_output_modes.html).

Zu den Einstellungen des Profils gehört auch `line_length = 88`, die Standard-Zeilenlänge von `black`.
Wenn Sie `black` in einem Projekt wie in [PARTREF::black] auf 79 Zeichen einstellen,
müssen Sie dort in `[tool.isort]` deshalb zusätzlich `line_length = 79` setzen.
Sonst lässt `isort` Importzeilen mit 80 bis 88 Zeichen stehen, und `black --check` beanstandet sie.
In `isort_demo` ist das nicht nötig, weil `black` dort mit seiner Standardlänge arbeitet.

<!-- time estimate: 20 min -->


### Noch einmal vom übergeordneten Verzeichnis aus

Die neue `pyproject.toml` hat noch eine zweite, weniger offensichtliche Wirkung.

- Wechseln Sie mit `cd ..` erneut in das übergeordnete Verzeichnis.
- [EC] `isort --check-only --diff isort_demo/report.py; echo $?`
- [EC] `isort --show-config isort_demo/report.py | grep -A3 '^    "src_paths"'`
- [EQ] Warum ordnet `isort` `textstats` jetzt auch von hier aus als Teil des Projekts ein?
  Lesen Sie dazu unter
  [Supported config files](https://isort.readthedocs.io/en/latest/configuration/config_files.html)
  nach, wo `isort` seine Konfigurationsdatei sucht.

<!-- time estimate: 5 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint sind `report.py` und `pyproject.toml` im Endzustand.
Kopieren Sie beide Dateien dazu aus dem Hilfsbereich in Ihr Aufgabenverzeichnis im Repo.)

[ENDSECTION]
[INSTRUCTOR::Einordnung nach Verzeichnis und Konflikt mit black verstanden?]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
