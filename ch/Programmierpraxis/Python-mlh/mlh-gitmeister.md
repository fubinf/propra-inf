title: "My Little Helpers: gitmeister --- Find top contributors"
stage: beta
timevalue: 4.0
difficulty: 3
assumes: regex_einfuehrung, pip, m_subprocess, sorted-and-sort, m_pytest
requires: mlh-lsnew
---

[SECTION::goal::experience,product]

- Ich habe eine komplexe Algorithmenbibliothek eingesetzt.
- Ich habe mir ein Hilfsprogramm gebaut, um mir beim Überblicken von git-Repos zu helfen.

[ENDSECTION]
[SECTION::background::default]

Manchmal führen scheinbar simple Aufgabenstellungen zu Programmlogik, 
die man besser nicht selbst schreibt, sondern sich dafür eine Bibliothek sucht.
Das spart viel Zeit für Debugging und führt oft zu weitaus Laufzeit-effizienteren Lösungen.

[ENDSECTION]
[SECTION::instructions::loose]

### Aufgabenstellung

Git hat ein sehr nützliches Kommando, um zu verstehen, wie viele Leute wie viele Commits
zu einem Repo beigetragen haben: `git shortlog -se`.  
Dessen Ausgabe sieht z.B. so aus (bitte nicht erschrecken: über 3000 Zeilen):

[FOLDOUT::`git shortlog -se` für Django (Stand 2024-04)`]
```
[INCLUDE::include/mlh-gitmeister-django.shortlog]
```
[ENDFOLDOUT]

[ER] Diese Daten gehören zum  
[Repo](https://github.com/django/django)
von
[Django](https://django.readthedocs.io/en/stable/),
dem wichtigsten Python-Webframework.
Speichern Sie sich diese Ausgabe in die Datei `mlh/input/gitmeister-django.shortlog`.

Wenn man das sortiert (`sort -rn mlh-gitmeister-django.shortlog`),
sieht der Anfang so aus:

[FOLDOUT::`git shortlog -se|sort -rn | head` für Django`]
```
  3314  Tim Graham <timograham@gmail.com>
  2802  Adrian Holovaty <adrian@holovaty.com>
  1872  Malcolm Tredinnick <malcolm.tredinnick@gmail.com>
  1741  Russell Keith-Magee <russell@keith-magee.com>
  1713  Claude Paroz <claude@2xlibre.net>
  1519  Mariusz Felisiak <felisiak.mariusz@gmail.com>
  1377  Aymeric Augustin <aymeric.augustin@m4x.org>
   895  Jannis Leidel <jannis@leidel.info>
   893  Jacob Kaplan-Moss <jacob@jacobian.org>
   579  Simon Charette <charette.s@gmail.com>
```
[ENDFOLDOUT]

Super, oder?
Aber wer oben aufgepasst hat, hat schon das Problem bemerkt:
Manche Emailaddressen tauchen mit mehreren Namen auf (z.B. `007gzs@gmail.com` ganz am Anfang)
und manche Namen mit mehreren Emailaddressen (z.B. `Abhishek Bera` etwas weiter unten).
In den 3195 Einträgen gibt es sowas ziemlich oft:
Wenn man es bereinigt, bleiben nur noch 2803 Leute übrig (88%)
und sogar die Liste der häufigsten Committer_innen ändert sich:
In der Liste der Top 20 steigen zwei Leute auf höhere Ränge auf
und eine dritte Person erscheint überhaupt erst.

Solche Effekte gibt es in den meisten großen Repos und sie können noch
weitaus drastischer ausfallen als hier bei Django.

Dafür wollen wir uns ein Werkzeug bauen:  
**Zeige von jedem Cluster zusammengehöriger Namen-mit-gleicher-Emailadresse
und Emailadressen-mit-gleichem-Namen nur den Namen und die Emailadresse an,
auf die die meisten Commits entfallen.**

Und natürlich gliedern wir das als ein Subcommand in unsere Werkzeugsammlung
`mlh` ein.


### Erwünschte Form

So soll das am Ende aussehen:

```
usage: mlh gitmeister [-h] n [gitdir]

positional arguments:
  n           number of top committers to show
  gitdir      git directory to use (else filter input coming from 'git shortlog -se')
```

Das heißt also: 

- Entweder man gibt ein Verzeichnis an, in dem ein git-Repo liegt
  und das Programm ruft dort `git shortlog -se` auf
- oder man gibt nichts an und liefert solche `git shortlog`-Ausgaben 
  auf der Standardeingabe an, benutzt das Programm also als [TERMREF::Filter].
  (Davon werden wir hier zum Testen Gebrauch machen.)


### Wie baut man das?

- Wenn man loslegt, solchen Code zu schreiben, ist der erste Schritt klar:
  Die Eingabezeilen in die Tripel von Commitanzahl, Name und Emailaddresse zerlegen.
  Angesichts der Syntax der Zeilen geht das natürlich recht einfach mit einem
  regulären Ausdruck.
- Dann hat man lauter Name/Email-Paare, die man nun zusammenführen muss.
  Dafür könnte man z.B. eine Klasse anlegen, die ein Tripel repräsentiert
  und eine zweite, die eine Zusammenfügung solcher Tripel darstellt
  und ein Prädikat hat, um Zusammenfügbarkeit festzustellen.
- Irgendwann geht einem dann hoffentlich ein Licht auf:
  Das ist ein 
  [bipartiter Graph](https://de.wikipedia.org/wiki/Bipartiter_Graph) 
  (denn jede Kante verbindet einen Namen mit einer Emailaddresse), 
  von dem die 
  [Zusammenhangskomponenten](https://de.wikipedia.org/wiki/Zusammenhang_(Graphentheorie)) 
  gesucht sind.
- An der Stelle baut man dann eventuell seine Datenstrukturen um
  und überlegt, wie der Algorithmus für Zusammenhangskomponenten aussehen muss
- Oder -- besser! -- man denkt: Da gibt's doch bestimmt gute Bibliotheken dafür?


### Bibliothek auswählen

- Recherchieren Sie, welche populären Graphbibliotheken es für Python gibt.
- Anforderungen: 
    - Muss Kantengewichte darstellen können (Commitanzahl)
    - Braucht _nicht_ für riesige Graphen geeignet zu sein, denn wir haben
      ja maximal ein paar Tausend Kanten.
    - Muss Zusammenhangskomponenten berechnen können.
    - Sollte eine leichtverständliche Dokumentation haben,
      denn wir wollen ja nicht erst eine Woche damit zubringen,
      die Benutzung zu lernen.
- Wählen Sie eine Bibliothek aus, die Sie einsetzen würden (samt Begründung) und
  öffnen Sie _erst dann_ (oder im Falle kompletter Verzweiflung) die nachfolgende Empfehlung.

[FOLDOUT::Empfehlung einer geeigneten Graphbibliothek]
Gut geeignet ist `networkx`:
Die [Dokumentation](https://networkx.org/documentation/stable/index.html) 
(insbesondere die Einführung) ist ausgezeichnet
und man kann beliebige Objekte als Knoten benutzen, nicht nur Integers,
was uns das Leben sehr erleichtert.
[ENDFOLDOUT]


### Bauanleitung

- [ER] Legen Sie mlh.subcmds.gitmeister an und schreiben Sie dort
  `meaning`, `add_arguments()` und ein leeres `execute()`.
- [ER] Schreiben Sie `get_git_shortlog(gitdir: str) -> str`.
- [ER] Rufen Sie das in `execute()`, wenn ein `gitdir` angegeben ist
  oder lesen Sie die Standardeingabe andernfalls.
- [ER] Legen Sie eine fast leere Klasse `Committer` an, die eine Zeile
  der letztendlichen Ausgabe des Programms repräsentiert.
- [ER] Deren Konstruktor empfängt einen Graphen und eine Zusammenhangskomponente.
- [ER] Schreiben Sie auf Modulebene (also außerhalb dieser Klasse) eine Funktion
  `get_committers(shortlog: str) -> list[Committer]`, die folgendes tut:
    - Einen leeren Graphen anlegen.
    - Den Eingabestring in Zeilen zerlegen.
    - Jede Zeile in ein Tripel zerlegen.
    - Das Tripel als Kante in den Graphen einfügen.
    - Am Ende die Zusammenhangskomponenten des Graphen abfragen,
    - jede davon in einen `Committer` verwandeln
    - und die Liste dieser `Committer` als Ergebnis liefern. 
- [ER] `Committer` braucht Funktionen `top_name()` und `top_email()`,
  die den Namen und die Email finden, auf die die meisten Commits entfallen,
  sowie `commits()`, die die Gesamtanzahl an Commits für die Komponente berechnet.
- [ER] Am bequemsten implementieren Sie ferner in `Committer` die Operation `__lt__()`,
  also den "kleiner als"-Operator, dann können Sie das Sortieren einfach mit `sorted()`
  erledigen
- [ER] Sorgen Sie dafür, dass `top_name()`, `top_email()` und `commits()`
  beim Sortieren nicht immer wieder aufgerufen werden, sonst wird der Laufzeitaufwand unnötig hoch.
  Das lässt sich sehr elegant mit `functools.cached-property` bewerkstelligen.
- [ER] Implementieren Sie einen pytest-Test in `mlh/tests/test_gitmeister.py`, der sicherstellt,
  dass das Erste-12-Ergebnis für `mlh/input/gitmeister-django.shortlog` lautet wie unten.

[FOLDOUT::`python mlh gitmeister 12 <mlh/input/gitmeister-django.shortlog`]
```
 3464  Tim Graham <timograham@gmail.com>
 2802  Adrian Holovaty <adrian@holovaty.com>
 1872  Malcolm Tredinnick <malcolm.tredinnick@gmail.com>
 1741  Russell Keith-Magee <russell@keith-magee.com>
 1713  Claude Paroz <claude@2xlibre.net>
 1520  Mariusz Felisiak <felisiak.mariusz@gmail.com>
 1399  Aymeric Augustin <aymeric.augustin@m4x.org>
  895  Jannis Leidel <jannis@leidel.info>
  893  Jacob Kaplan-Moss <jacob@jacobian.org>
  646  Simon Charette <charette.s@gmail.com>
  520  Alex Gaynor <alex.gaynor@gmail.com>
  497  Luke Plant <L.Plant.98@cantab.net>
```
[ENDFOLDOUT]

[HINT::Wie bekommt man gute Testbarkeit?]
Extrahieren Sie nötigenfalls einen Teil von `execute()` in eine separate Funktion, 
damit sich eine gute Testbarkeit einstellt.
[ENDHINT]

[HINT::Wie bekommt man den Test hilfreich für die Defektsuche?]
Beim Debugging hilft es oft enorm, wenn ein solcher Test alle falschen Paare von
erhaltener Zeile und erwarteter Zeile mit deutlichen Markierungen und Nummern ausgibt,
anstatt nur zu sagen, dass es irgendwo im Output eine Abweichung gibt.
[ENDHINT]

- Zum Testen gehen Sie ins Verzeichnis `mlh` und benutzen `pytest tests/test_gitmeister.py`

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Test prüfen, Entwurfsstil prüfen]

Beispiellösung siehe [TREEREF::mlh/mlh/subcmds/gitmeister.py] und [TREEREF::mlh/tests/test_gitmeister.py].

- Enthält (oder holt sich) der Test die Testdaten?
- Ruft er sinnvoll `mlh.subcmds.gitmeister.<somefunc>` auf? (Möglichst lieber nicht `execute()`)
- Prüft er die Ausgaben gegen die Testdaten? 
  Idealerweise zeilenweise und erzeugt bei Abweichungen Debugging-Ausgaben?
- [EREFR::7] Hat `mlh/mlh/subcmds/gitmeister.py` die gewünschte Funktion `get_committers()`?
  Mit plausibler Logik (und nicht hartkodiertem Ergebnis)?
- [EREFR::6]/[EREFR::8]/[EREFR::9] Hat `mlh/mlh/subcmds/gitmeister.py` die gewünschte Klasse `Committer`?

[ENDINSTRUCTOR]
