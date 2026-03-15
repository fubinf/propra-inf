title: git-Repository
stage: draft
timevalue: 1
difficulty: 2
explains:
assumes: git-Funktionsweise
---

[SECTION::goal::experience]
Ich lerne, was ein Git-Repository ist, wie es aufgebaut ist, und erstelle meinen ersten Commit 
in einem frischen Repository.
[ENDSECTION]

[SECTION::background::default]
In [PARTREF::Git101] haben wir gerade so das Nötigste gelernt, um unsere Aufgaben im ProPra 
abzugeben. 
Jetzt geht es darum, das Gelernte zu vertiefen und unser Wissen über die Befehle und 
die [PARTREF::git-Funktionsweise] zu festigen.

In dieser Aufgabe erstellen wir ein frisches Repository und lernen dabei,
was `git init` eigentlich tut, was sich im `.git`-Ordner verbirgt 
und wie die grundlegenden Konzepte *Repository-Verzeichnis* und *Arbeitsverzeichnis* 
zusammenhängen.
Am Ende steht unser erster Commit.
[ENDSECTION]

[SECTION::instructions::detailed]

Anders als bei den meisten Aufgaben brauchen wir diesmal ein ganz neues Repo. 
Das dient dazu, dass Sie besser verstehen, was in diesem Schritt passiert,
und die Repo-Erstellung einmal selbst durchführen, anstatt sie wie üblich 
von Tools wie GitLab erledigen zu lassen. 
Dafür erstellen Sie ein neues Verzeichnis **außerhalb Ihres bestehenden ProPra-Repositories**, 
wie wir es bereits im [TERMREF::Hilfsbereich] der ProPra-Grundlagen eingerichtet haben.
Navigieren Sie mit Ihrer Kommandozeile dort hinein und führen Sie den Befehl `git init` aus. 

[HINT::Kann ich ein neues Repository in meinem bestehenden erstellen?]
Jein. Git bietet die Möglichkeit, weitere Repos mithilfe sogenannter Submodules einzubinden. 
Submodules sind auch bei kompetenten Git-Nutzer_innen berüchtigt dafür, wie kompliziert
das Leben dann wird; also gehen wir diesen Weg hier lieber nicht,
sondern trennen unser Übungs-Repo vom ProPra-Repo.
[ENDHINT]

### Git initialisieren; Repository- und Arbeitsverzeichnis

Unser neues Repo wirkt auf den ersten Blick leer – sowohl im GUI-Dateimanager des 
Betriebssystems als auch in der Kommandozeile mit `ls`.
Warum ist das so?

Wenn Sie `git init` ausführen, legt Git den unsichtbaren Ordner `.git` an.
Führen wir `ls -a` aus oder lassen uns im Dateimanager versteckte Verzeichnisse anzeigen, 
sehen wir diesen Ordner.

Der Ordner `.git` wird auch [TERMREF::Repository-Verzeichnis] (engl. Repository Directory) genannt.
*Repository* bedeutet *Lager* oder *Speicher*. Man kann es sich wie ein Archiv vorstellen, 
in dem Git alle Informationen über unser Projekt speichert – sowohl Dateiinhalte als auch Metadaten.

Jedes Mal, wenn Sie eine Datei bzw. den Zustand einer Datei dauerhaft sichern möchten, 
übergeben Sie sie an das Repository.
Dieses Archiv teilen Sie später mit anderen Nutzern bzw. laden es auf einen Git-Server hoch.
Andere können dann jeden gespeicherten Zustand wiederherstellen oder eigene Zustände hinzufügen.

Gespeicherte Dateien lassen sich nicht ohne Weiteres ändern. Das ist wichtig zu wissen!
Haben Sie z. B. versehentlich Passwörter oder andere sensible Daten committet und auf den 
Git-Server gepusht, wird es mühsam, diese wieder zu entfernen.
Darauf gehen wir in späteren Aufgaben näher ein.

Neben dem *Repository Directory* gibt es auch das *Working Directory* (dt. Arbeitsverzeichnis), 
manchmal *Working Tree* genannt.
Das Arbeitsverzeichnis enthält den aktuellen Zustand Ihres Projekts. 
Mit diesen Dateien arbeiten Sie und können daran grundsätzlich alles ändern, 
denn alte Zustände lassen sich jederzeit aus dem Archiv wiederherstellen.

Warum eigentlich *Working __Tree__*?
Weil Git Verzeichnisse grundsätzlich als Baumstrukturen versteht.

Was haben wir bis hierhin gelernt?

* `git init` erzeugt das Repository-Verzeichnis und legt es im Ordner `.git` an.
* Im Repository-Verzeichnis befinden sich alle Informationen und Daten zu unserem Projekt.
* Wir können jederzeit zu jedem einmal abgelegten Zustand des Repositorys zurückkehren.
* Das Arbeitsverzeichnis (Working Directory) ist unsere lokale Arbeitskopie des Repos. 
  Hier können wir beliebig Änderungen vornehmen.
* Diese Änderungen sowie neu hinzugefügte Dateien und Verzeichnisse können wir dem Repository 
  zum dauerhaften Speichern übergeben.

### Wo bekomme ich nochmal Hilfe?

In [PARTREF::git-Funktionsweise] haben Sie bereits den Befehl `git help` kennengelernt.
Diesen wollen wir jetzt wieder nutzen, um zu lernen, wozu `git init` dient.

[EQ] Was macht der Befehl `git init`?
Referenzieren Sie hierbei die Git-Hilfe und vor allem die Teile, die Sie verstehen.

### Aufbau des Repository-Verzeichnisses

Besonders wichtig für uns ist der `.git`-Ordner (Repository-Verzeichnis).
Zwar müssen wir im Idealfall nie direkt in diesem Ordner arbeiten, 
aber es hilft beim Verständnis zu wissen, was sich darin befindet und wie Git ihn verwaltet.

Lesen Sie dazu den Abschnitt
[Creating a git repository](https://git-scm.com/docs/gitcore-tutorial)
im `gitcore-tutorial` und beantworten Sie dann die folgenden Fragen.

[EQ] Was wird im Verzeichnis `.git/objects` abgelegt?

[EQ] Wie werden Git-Objekte referenziert?

[EQ] Wie heißt der Default-Branch, und können Sie ihn umbenennen?

In der nächsten Aufgabe werden wir uns die Git-Objekte sehr viel genauer ansehen.
Für den Moment reicht es zu wissen, dass Git alles, was es speichert, als Objekte im 
`.git/objects`-Verzeichnis ablegt und über Hashes referenziert.

### git status

Wie wir wissen, können wir im Arbeitsverzeichnis nach Belieben Änderungen vornehmen.
Git hat jedoch eine andere Sicht auf das Arbeitsverzeichnis.
Um den Unterschied zu sehen, gibt es ein hilfreiches Kommando: `git status`.
Es zeigt an, welche Dateien Git erkennt, 
welche es verfolgt (engl. *trackt*) und ob es Änderungen seit dem letzten Commit gibt.

Führen wir `git status` in unserem neuen Repository aus, sehen wir folgende Ausgabe:

```terminaloutput
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Was bedeutet *tracken*?

*To track something* bedeutet *etwas zu verfolgen*.
Genau das macht Git hier. Für jede getrackte Datei prüft Git, 
ob seit der letzten Archivierung Änderungen vorgenommen wurden.

Mit `git add` teilen wir Git mit, welche Dateien wir tracken wollen.
Nicht getrackte Dateien kann Git zwar sehen, aber es speichert ihren Zustand nicht.

[NOTICE]
Es gibt auch eine Möglichkeit, bestimmte Dateien oder Verzeichnisse komplett zu ignorieren:
die `.gitignore`-Datei.
Git wird dann nie vorschlagen, diese Dateien zu tracken oder ihre Inhalte zu sichern.
Dazu kommen wir in einer späteren Aufgabe.
[ENDNOTICE]


### Was ist ein Commit?

Wir erinnern uns an das Archiv.
Git archiviert nur die Zustände des Repos, die wir ihm *übergeben*.
Diese Zustände nennt man *Commits*. 
Der Begriff kommt vom englischen Verb *to commit*, also „etwas übergeben" oder „überlassen".

Wir übergeben Git den aktuellen Zustand bestimmter Dateien und beauftragen es mit der Archivierung.
Dabei speichert Git nicht etwa die Änderungen, die wir vorgenommen haben, sondern ein vollständiges Abbild 
— einen sogenannten Snapshot — aller vorgemerkten Dateien. 
Was genau das bedeutet und warum das so ist, schauen wir uns in der nächsten Aufgabe an.
Git gibt uns dafür einen eindeutigen Identifikator, einen Hash.
Mit diesem Commit-Hash können wir jederzeit auf den Zustand zum Zeitpunkt dieses Commits zurückgreifen.

Wie genau das alles funktioniert, schauen wir uns in der nächsten Aufgabe im Detail an.
Für jetzt reicht es zu wissen: `git add` merkt Dateien vor, `git commit` speichert sie dauerhaft.

### Der erste Commit

Beginnen wir mit unserem kleinen Beispielprojekt – einem simplen Taschenrechner.
Erstellen Sie die Datei `calculator.py` mit folgendem Inhalt:

```python
# Ein einfacher Rechner

def addiere(a, b):
    
```

Schauen Sie sich nun den Status Ihres Repositories an.

Es erscheint weiterhin `No commits yet`, aber Git hat die neue Datei erkannt.
Sie wird als `Untracked file` aufgeführt.
Git sieht also alle Dateien im Arbeitsverzeichnis, 
kümmert sich aber erst dann aktiv um sie, wenn wir es dazu auffordern.

Fügen Sie jetzt die Datei mit `git add calculator.py` hinzu und prüfen Sie erneut den Status.

[EQ] Welche Veränderung zeigt `git status` nach dem `git add`?

Jetzt können wir unseren ersten Commit erstellen:

```bash
git commit -m "calculator.py mit Additionsfunktion angelegt"
```

[FOLDOUT::Was ist eine sinnvolle Commit-Nachricht?]
Das ist eine sehr gute Frage. 
So gut, dass es sogar 
[Studien darüber gibt.](https://dl.acm.org/doi/10.1145/3510003.3510205)
Grundsätzlich gilt: Halten Sie sich kurz und beschreiben Sie klar, was der Commit beinhaltet.
In unserem Fall z. B.: `calculator.py mit Additionsfunktion angelegt`.
Später dann vielleicht: `fix: Division fängt Division durch Null ab`.
Die Sprache ist dabei egal, aber im Code wird häufig Englisch verwendet.
Mehr Tipps dazu gibt es z. B. [hier.](https://docs.wpvip.com/guidebooks/developer-best-practices/
create-a-good-commit-message/)
[ENDFOLDOUT]

Führen Sie nach dem Commit noch einmal `git status` aus.

[EQ] Was zeigt `git status` jetzt?

### Zwischenfazit

Sie haben in dieser Aufgabe ein Repository von Grund auf erstellt und Ihren ersten Commit gemacht.
Sie kennen jetzt den Unterschied zwischen Repository-Verzeichnis (`.git`) und Arbeitsverzeichnis,
wissen, was Tracking bedeutet, und haben den grundlegenden Zyklus durchlaufen:
Datei erstellen → `git add` → `git commit`.

In der nächsten Aufgabe schauen wir uns an, was dabei *wirklich* passiert –
was Git unter der Haube mit unseren Dateien macht und warum `git add` mehr tut, 
als nur eine Datei „vorzumerken".

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhinweise]
Prüfen Sie das Protokoll auf:
- Korrekte Ausführung von `git init`, `git status`, `git add`, `git commit`

[INCLUDE::ALT:]

[ENDINSTRUCTOR]