title: Sicherheitslücken finden mit bandit
stage: alpha
timevalue: 2
difficulty: 2
explains: SQL Injection, Command Injection, Fehlalarm
assumes: venv, flake8, sql-SELECT
---

[SECTION::goal::trial]

- Ich kann Python-Code mit `bandit` auf typische Sicherheitslücken prüfen
  und seine Meldungen lesen.
- Ich habe an einem Beispiel selbst ausprobiert, wie sich solche Lücken ausnutzen lassen,
  und kann sie beheben.
- Ich kann echte Lücken von Fehlalarmen unterscheiden und Fehlalarme gezielt stummschalten.
- Ich weiß, warum `No issues identified` nicht bedeutet, dass ein Programm sicher ist.

[ENDSECTION]
[SECTION::background::default]

Die meisten Sicherheitslücken entstehen nicht durch raffinierte Tricks,
sondern durch ganz gewöhnlichen, bequemen Code:
ein schnell zusammengesetzter SQL-Befehl, ein Aufruf der Shell,
eine Zufallszahl aus dem falschen Modul.
Solcher Code funktioniert meist tadellos und ist oft sogar `flake8`-sauber.
Zum Problem wird er erst, wenn jemand gezielt nach seinen Schwächen sucht.

`bandit` ist ein [TERMREF::Linter], der gezielt nach solchen Stellen sucht.
`bandit` kennt eine Liste typischer Gefahrenmuster in Python-Code
und meldet jede Stelle, auf die eines davon passt.
Ob dort wirklich eine Lücke steckt, muss man allerdings selbst beurteilen.
Genau das üben wir in dieser Aufgabe.

[ENDSECTION]
[SECTION::instructions::detailed]

### Das Beispielprogramm

Legen Sie für diese Aufgabe ein frisches [PARTREF::venv] an und aktivieren Sie es.

- [EC] `pip install bandit flake8`

Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein Verzeichnis `bandit_demo` an.
Führen Sie alle Kommandos dort aus, sofern nichts anderes gesagt ist.

Der Ruderclub "Spree 1923" verwaltet seine Mitglieder mit einem kleinen Kommandozeilenprogramm,
das ein Vereinsmitglied an einem Wochenende geschrieben hat.
Das Programm speichert die Mitglieder in einer SQLite-Datenbank
und vergibt jedem neuen Mitglied einen Zugangscode für das Codeschloss am Bootshaus.
Es kennt fünf Kommandos:

- `add NAME` nimmt ein Mitglied auf und zeigt dessen Zugangscode an.
- `show NAME` zeigt, seit wann jemand Mitglied ist.
  Das darf jeder abfragen.
- `delete NAME PASSWORT` löscht ein Mitglied.
  Das darf nur der Vorstand.
- `backup DATEI` kopiert die Datenbank in eine Sicherungsdatei.
- `cox` lost aus, wer heute steuert (engl. _cox_: Steuerperson im Ruderboot).

Legen Sie die Datei `mitglieder.py` mit folgendem Inhalt an.
Sie müssen den Code jetzt noch nicht im Detail verstehen;
wir sehen uns die wichtigen Stellen später gezielt an.

[FOLDOUT::Inhalt von `mitglieder.py`]
```python
"""Mitgliederverwaltung des Ruderclubs "Spree 1923"."""
import argparse
import random
import sqlite3
import string
import subprocess
from datetime import date

DB_FILE = "mitglieder.db"
ADMIN_PASSWORD = "Spree1923!"


def connect():
    con = sqlite3.connect(DB_FILE)
    con.execute("CREATE TABLE IF NOT EXISTS member "
                "(name TEXT, since TEXT, door_code TEXT)")
    return con


def new_door_code():
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(8))


def add(con, name):
    since = date.today().isoformat()
    code = new_door_code()
    con.execute(f"INSERT INTO member VALUES ('{name}', '{since}', '{code}')")
    con.commit()
    print(f"{name} aufgenommen. Zugangscode fürs Bootshaus: {code}")


def show(con, name):
    sql = "SELECT name, since FROM member WHERE name = '" + name + "'"
    for row in con.execute(sql):
        print(*row)


def delete(con, name, password):
    assert password == ADMIN_PASSWORD, "Nur der Vorstand darf löschen."
    con.execute("DELETE FROM member WHERE name = ?", (name,))
    con.commit()
    print(f"{name} gelöscht.")


def backup(target):
    subprocess.run(f"cp {DB_FILE} {target}", shell=True)
    print(f"Sicherung nach {target} geschrieben.")


def cox(con):
    names = [row[0] for row in con.execute("SELECT name FROM member")]
    print("Steuert heute:", random.choice(names))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command",
                        choices=["add", "show", "delete", "backup", "cox"])
    parser.add_argument("args", nargs="*")
    args = parser.parse_args()
    con = connect()
    if args.command == "add":
        add(con, args.args[0])
    elif args.command == "show":
        show(con, args.args[0])
    elif args.command == "delete":
        delete(con, args.args[0], args.args[1])
    elif args.command == "backup":
        backup(args.args[0])
    elif args.command == "cox":
        cox(con)


if __name__ == "__main__":
    main()
```
[ENDFOLDOUT]

Probieren Sie das Programm aus:

- [EC] `for name in Anna Ben Carla; do python mitglieder.py add $name; done`
- [EC] `python mitglieder.py show Ben`
- [EC] `flake8 mitglieder.py`

`flake8` hat nichts auszusetzen, stilistisch ist der Code also in Ordnung.
Mal sehen, was `bandit` dazu sagt.

<!-- time estimate: 10 min -->


### Was meldet `bandit`?

- [EC] `bandit mitglieder.py`

Jede Meldung (`Issue`) besteht aus mehreren Teilen:

- Die **Test-ID**, beispielsweise `B602`, bezeichnet die Regel, die angeschlagen hat.
  Dahinter steht eine kurze Beschreibung.
- **Severity** ist die Einschätzung von `bandit`, wie schwer der Schaden wäre,
  falls an der Stelle wirklich eine Lücke ist.
- **Confidence** ist die Einschätzung von `bandit`, wie sicher es ist,
  dass an der Stelle wirklich eine Lücke ist.
- **CWE** verweist auf einen Eintrag in der _Common Weakness Enumeration_,
  einem öffentlichen Katalog von Schwachstellentypen:
  [HREF::https://cwe.mitre.org/]
- **More Info** führt zur Beschreibung der Regel in der `bandit`-Dokumentation.
- **Location** nennt Datei, Zeile und Spalte; darunter folgt der betroffene Codeausschnitt.

Lesen Sie die Meldungen in Ruhe durch und sehen Sie sich jeweils die genannte Codestelle an.

- [EQ] Bevor wir genauer hinsehen, eine spontane Einschätzung:
  Welche Meldung halten Sie für die gefährlichste, welche für überflüssig? Warum?
  (Hier gibt es kein Richtig oder Falsch; wir kommen später darauf zurück.)

<!-- time estimate: 10 min -->


### Angriffe ausprobieren

Solange nur die Person, die das Programm geschrieben hat, es auf ihrem eigenen Rechner aufruft,
ist wenig zu befürchten:
Wer ohnehin an der Shell sitzt, kann dort auch so beliebige Kommandos ausführen.
Gefährlich wird es, sobald die Eingaben von anderen kommen.
Stellen Sie sich vor, der Verein bindet das Programm später an seine Webseite an,
sodass sich alle Kommandos auch dort aufrufen lassen,
etwa `show`, damit Interessierte nachsehen können, ob jemand schon Mitglied ist.
Genau so entstehen viele echte Lücken:
Code wird für einen harmlosen Zweck geschrieben und später in einem anderen Zusammenhang benutzt.

Wir probieren nun aus, ob sich die Meldungen tatsächlich ausnutzen lassen.
Alle Angriffe sind harmlos und betreffen nur Ihr Verzeichnis `bandit_demo`.

Zuerst eine ganz unschuldige Eingabe:

- [EC] `python mitglieder.py add "Jan O'Neill"`
- [EQ] Warum stürzt das Programm ab?
  Schreiben Sie den SQL-Befehl auf, den `add` hier an die Datenbank schickt.

Was durch ein Versehen kaputtgeht, lässt sich auch absichtlich ausnutzen:

- [EC] `python mitglieder.py show "x' UNION SELECT name, door_code FROM member --"`
- [EQ] Was ist passiert?
  Schreiben Sie den SQL-Befehl auf, den `show` hier an die Datenbank schickt,
  und erklären Sie, welche Rolle das `'` und das `--` darin spielen.
  Diese Angriffsart heißt [TERMREF::SQL Injection].

[HINT::Ich verstehe den SQL-Befehl nicht]
Setzen Sie die Eingabe von Hand in die Zeichenkette in `show` ein.
Achten Sie darauf, wo im entstehenden SQL-Befehl eine Zeichenkette beginnt und wo sie endet.
`UNION` hängt an das Ergebnis einer Abfrage das Ergebnis einer zweiten Abfrage an;
beide müssen gleich viele Spalten liefern.
`--` leitet in SQL einen Kommentar bis zum Zeilenende ein.
[ENDHINT]

- [EC] `python mitglieder.py backup "kopie.db; echo GEHACKT"`
- [EQ] Warum erscheint `GEHACKT`?
  Was könnte jemand anstelle von `echo GEHACKT` einsetzen?
  Diese Angriffsart heißt [TERMREF::Command Injection].

[HINT::Ich weiß nicht, warum `GEHACKT` erscheint]
Wegen `shell=True` übergibt `subprocess.run` die ganze Zeichenkette einer Shell,
genau so, als hätten Sie sie selbst an der Kommandozeile eingetippt.
Setzen Sie die Eingabe in die Zeichenkette in `backup` ein.
Was macht die Shell mit einem `;`?
[ENDHINT]

Zuletzt der Passwortschutz von `delete`:

- [EC] `python mitglieder.py delete Anna falsch`
- [EC] `python -O mitglieder.py delete Anna falsch`
- [EQ] Was bewirkt die Option `-O`?
  Warum ist `assert` deshalb ungeeignet, um ein Passwort zu prüfen,
  und wofür ist es eigentlich gedacht?
  Lesen Sie dazu die Beschreibung von
  [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
  und die der
  [`assert`-Anweisung](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement).

Anders als bei den Angriffen oben braucht es hier niemanden mit böser Absicht:
Manche starten Programme mit `-O` nur in der Hoffnung, dass sie schneller laufen,
oder auf einem Server ist die gleichwertige [TERMREF::Umgebungsvariable] `PYTHONOPTIMIZE`
für alle Python-Programme voreingestellt.
Wer das Programm geschrieben hat, hat darauf keinen Einfluss.
Läuft das Programm dann hinter der Webseite, kann dort jede Person Mitglieder löschen.

<!-- time estimate: 20 min -->


### Meldungen beurteilen

Nicht jede Meldung bedeutet eine Lücke.
Wir unterscheiden drei Kategorien:

- **Lücke**: ein echtes Sicherheitsproblem in diesem Programm.
- **Fehlalarm** (engl. _false positive_): Die Stelle passt auf ein Gefahrenmuster von `bandit`,
  ist hier aber ungefährlich.
- **Hinweis**: Die Stelle ist für sich genommen kein Problem,
  sondern nur ein Anlass, den Code in ihrer Umgebung genauer anzusehen.

Vier Meldungen haben Sie oben schon ausprobiert.
Für die übrigen helfen die aufklappbaren Hilfen unter der folgenden Frage.

- [EQ] Legen Sie eine Tabelle mit einer Zeile pro `bandit`-Meldung an,
  mit den Spalten Zeile, Test-ID, Severity, Confidence, Kategorie und Begründung (ein Satz).
  Vergleichen Sie die Tabelle anschließend mit Ihrer spontanen Einschätzung von vorhin:
  Welche Meldung hatten Sie unter- oder überschätzt?

[HINT::Wie beurteile ich die beiden `B311`-Meldungen?]
Lesen Sie die Warnung am Anfang der Dokumentation des Moduls
[`random`](https://docs.python.org/3/library/random.html)
(siehe auch [PARTREF::m_random]).
Fragen Sie sich dann für jede der beiden Stellen einzeln:
Was hätte jemand davon, das Ergebnis vorhersagen zu können?
[ENDHINT]

[HINT::Wie beurteile ich `B105`?]
Überlegen Sie, wo dieser Quellcode überall landet:
im Git-Repo des Vereins, vielleicht öffentlich auf GitHub, in Sicherungskopien,
auf den Rechnern aller, die am Programm mitarbeiten.
Und was müsste geschehen, wenn der Vorstand das Passwort ändern will?
[ENDHINT]

[HINT::Wie beurteile ich `B404`?]
Ist es an sich gefährlich, ein Modul zu importieren?
Wozu könnte die Meldung trotzdem nützlich sein, wenn man fremden Code durchsieht?
[ENDHINT]

In größeren Projekten liefert `bandit` schnell Dutzende Meldungen.
Da ist es verlockend, sich nur die "wichtigen" anzusehen,
und `bandit` kann tatsächlich nach Severity und Confidence filtern.
Wir probieren aus, was dabei herauskäme.
Die ausführliche Ausgabe ist zum Verstehen gut, zum Vergleichen aber zu lang.
Mit `-q` (keine Statuszeilen), `-f custom` und `--msg-template` erhalten wir eine Zeile pro Meldung.
Damit wir die Formatangabe nicht jedes Mal tippen müssen, legen wir sie in einer Shellvariablen ab.

- [EC] `fmt="{line}: {test_id} {severity}/{confidence}"`
- [EC] `bandit -q -f custom --msg-template "$fmt" --severity-level medium mitglieder.py`
- [EC] `bandit -q -f custom --msg-template "$fmt" --confidence-level medium mitglieder.py`
- [EQ] Welche Lücken aus Ihrer Tabelle wären mit dem jeweiligen Filter unbemerkt geblieben?
  Was folgt daraus für den Einsatz dieser Filter?

<!-- time estimate: 20 min -->


### Lücken schließen

Nun beheben wir die Lücken, eine nach der anderen.
Rufen Sie nach jedem Schritt `bandit -q -f custom --msg-template "$fmt" mitglieder.py` auf
und beobachten Sie, welche Meldung verschwindet.
Diese Zwischenaufrufe gehören nicht ins Kommandoprotokoll.

- [ER] Ändern Sie `add` und `show` so, dass die Werte nicht mehr in die Zeichenkette
  des SQL-Befehls eingebaut, sondern über Platzhalter übergeben werden.
  Wie das geht, steht im Abschnitt
  [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
  der `sqlite3`-Dokumentation (siehe auch [PARTREF::m_sqlite3]).
  Ein Vorbild finden Sie sogar im Programm selbst.
- [ER] Ändern Sie `backup` so, dass keine Shell mehr beteiligt ist.
  Am einfachsten startet man dafür gar kein fremdes Programm,
  denn Python kann Dateien selbst kopieren:
  Benutzen Sie
  [`shutil.copy`](https://docs.python.org/3/library/shutil.html#shutil.copy)
  (siehe auch [PARTREF::m_shutil]).
  Entfernen Sie anschließend den nicht mehr benötigten Import von `subprocess`.

Muss man doch einmal ein externes Programm starten, übergibt man das Kommando als Liste,
also etwa `subprocess.run(["cp", DB_FILE, target])`, und lässt `shell=True` weg.
Dann wird keine Shell gestartet, und `;` hat keine besondere Bedeutung mehr.
Mehr dazu steht im Abschnitt
[Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)
der `subprocess`-Dokumentation.

- [ER] Erzeugen Sie die Zugangscodes mit dem Modul
  [`secrets`](https://docs.python.org/3/library/secrets.html)
  statt mit `random`.
  `cox` lassen Sie vorerst unverändert.
- [ER] Ersetzen Sie das `assert` in `delete` durch eine `if`-Anweisung,
  die das Programm im Fehlerfall mit `sys.exit("Nur der Vorstand darf löschen.")` beendet.
- [ER] Entfernen Sie die Konstante `ADMIN_PASSWORD`.
  `delete` soll das eingegebene Passwort stattdessen mit dem Wert der
  [TERMREF::Umgebungsvariable] `ADMIN_PASSWORD` vergleichen,
  den Sie mit `os.environ.get("ADMIN_PASSWORD")` erhalten.
  Geben Sie `get` dabei keinen Ersatzwert mit:
  Mit `os.environ.get("ADMIN_PASSWORD", "Spree1923!")` stünde das Passwort wieder im Code,
  und `bandit` würde es nicht einmal bemerken.

[HINT::Was passiert, wenn die Umgebungsvariable gar nicht gesetzt ist?]
Dann liefert `os.environ.get` den Wert `None`.
Kein eingegebenes Passwort ist gleich `None`, also kann dann niemand löschen.
Das ist das richtige Verhalten:
Bei einer Fehlkonfiguration soll die Tür zubleiben, statt offen zu stehen.
[ENDHINT]

Übrig ist jetzt nur noch die `B311`-Meldung in `cox`.
Dort ist der Code in Ordnung, also bringen wir stattdessen `bandit` zum Schweigen,
ähnlich wie mit den `# noqa`-Kommentaren von `flake8` aus [PARTREF::flake8]
(siehe
[In-line Ignoring Errors](https://flake8.pycqa.org/en/stable/user/violations.html#in-line-ignoring-errors)).

- Lesen Sie im Abschnitt
  [Exclusions](https://bandit.readthedocs.io/en/latest/config.html#exclusions)
  der `bandit`-Dokumentation nach, wie das mit einem `# nosec`-Kommentar geht.
- [ER] Schalten Sie in `cox` genau diese eine Meldung stumm,
  und zwar so, dass eine andere Meldung, die später in derselben Zeile hinzukäme,
  weiterhin erscheinen würde.
  Schreiben Sie in die Zeile darüber einen kurzen Kommentar,
  warum die Meldung hier ein [TERMREF::Fehlalarm] ist.
  Das empfiehlt auch der Abschnitt
  [Suppressing Individual Lines](https://bandit.readthedocs.io/en/latest/config.html#suppressing-individual-lines).

[HINT::Ich weiß nicht, wie ich nur eine einzige Meldung stummschalte]
Im Abschnitt Exclusions gibt es ein Beispiel, in dem hinter `# nosec` noch etwas steht.
Was bewirkt dieser Zusatz?
[ENDHINT]

- [EC] `bandit mitglieder.py; echo $?`

Jetzt sollte `bandit` `No issues identified.` melden.
In der Zusammenfassung sollte die stummgeschaltete Meldung bei
`Total potential issues skipped due to specifically being disabled` mitgezählt sein.
Steht die 1 stattdessen bei `Total lines skipped (#nosec)`,
haben Sie die ganze Zeile stummgeschaltet statt nur dieser einen Meldung.
`echo $?` zeigt den Exit-Status von `bandit`:
0 heißt "keine Meldungen", 1 heißt "mindestens eine Meldung".
Daran erkennt beispielsweise eine [TERMREF::CI/CD]-Pipeline, ob die Prüfung bestanden ist.

Ein stilles `bandit` beweist aber noch nicht, dass die Korrekturen wirken.
Prüfen Sie deshalb, dass die Angriffe von vorhin scheitern
und das Programm trotzdem noch tut, was es soll:

- [EC] `python mitglieder.py add "Jan O'Neill"`
- [EC] `python mitglieder.py show "x' UNION SELECT name, door_code FROM member --"`
- [EC] `python mitglieder.py backup "kopie.db; echo GEHACKT"`
- [EC] `ADMIN_PASSWORD=Steuerbord python -O mitglieder.py delete Ben falsch`
  (So setzt man eine Umgebungsvariable nur für diesen einen Aufruf.)
- [EC] `ADMIN_PASSWORD=Steuerbord python -O mitglieder.py delete Ben Steuerbord`
- [EQ] Was geschieht jetzt bei `show` und bei `backup` mit den Eingaben des Angriffs?
  Sehen Sie für `backup` mit `ls` in Ihrem Verzeichnis nach.
- Räumen Sie anschließend auf: `rm "kopie.db; echo GEHACKT"`

<!-- time estimate: 35 min -->


### Was `bandit` nicht sieht

Legen Sie eine Datei `grenzen.py` mit folgendem Inhalt an:

```python
ADMIN_PASSWORD = "Spree1923!"
ADMIN_PASSWORT = "Spree1923!"


def show_a(con, name):
    return con.execute("SELECT name FROM member WHERE name = '%s'" % name)


def show_b(con, name):
    sql = "SELECT name FROM member WHERE name = '%s'"
    return con.execute(sql % name)
```

Der Ausdruck `"... %s ..." % name` setzt den Wert von `name` an der Stelle von `%s`
in die Zeichenkette ein, ähnlich wie ein f-String (sogenannte %-Formatierung).

Die Zeilen 1 und 2 enthalten dasselbe Problem,
und die beiden Funktionen enthalten dieselbe Lücke.

- [EC] `bandit -q -f custom --msg-template "$fmt" grenzen.py`
  (Falls Sie inzwischen eine neue Shell geöffnet haben, legen Sie `fmt` vorher erneut an.)
- [EQ] Welche der vier Stellen meldet `bandit`, welche nicht?
  Was schließen Sie daraus, wie `bandit` nach Lücken sucht?

[HINT::Ich weiß nicht, wie `bandit` vorgeht]
Die
[Startseite der `bandit`-Dokumentation](https://bandit.readthedocs.io/en/latest/)
beschreibt das in einem Satz:
`bandit` zerlegt jede Datei in einen abstrakten Syntaxbaum (engl. _abstract syntax tree_, AST)
und prüft dessen Knoten mit seinen Regeln.
In diesem Baum ist jede Anweisung und jeder Ausdruck ein eigener Knoten:
Die Anweisung `y = x + 1` etwa hat die Teilknoten `y` und `x + 1`,
und `x + 1` hat wiederum die Teilknoten `x` und `1`.
Überlegen Sie: Woran kann `bandit` erkennen, dass eine Variable ein Passwort enthält?
Und was weiß es beim Ausdruck `sql % name` in `show_b` darüber, was in `sql` steht?
[ENDHINT]

Zurück zu `mitglieder.py`: Dort ist `bandit` inzwischen still.

- [EQ] Ist das Programm damit sicher?
  Sehen Sie sich an, welche Kommandos ein Passwort verlangen und welche nicht,
  und denken Sie an die geplante Webseite.

[HINT::Ich finde kein Problem mehr]
Was braucht man, um ins Bootshaus zu kommen?
Und wie bekommt man das?
[ENDHINT]

<!-- time estimate: 15 min -->


### `bandit` und Ihr eigener Code

- [EC] Rufen Sie `bandit -q -r` für den größten zusammenhängenden Satz von Python-Dateien auf,
  den Sie im Rahmen des ProPra geschrieben haben.
  (`-r` durchsucht ein Verzeichnis rekursiv.)

[HINT::Die Ausgabe ist riesig und nennt Dateien, die ich gar nicht geschrieben habe]
Vermutlich liegt ein venv innerhalb des Verzeichnisses,
und `bandit` untersucht auch alle dort installierten Bibliotheken.
Schließen Sie es mit `-x` aus, beispielsweise so:
`bandit -q -r meinprojekt -x meinprojekt/.venv`  
Der Pfad bei `-x` sollte dabei so beginnen wie der bei `-r`.
Wenn Sie im Projektverzeichnis selbst stehen, heißt es also `bandit -q -r . -x ./.venv`;
ein bloßes `-x .venv` schließt nichts aus.
[ENDHINT]

- [EQ] Ordnen Sie bis zu drei der Meldungen in die drei Kategorien von oben ein
  und begründen Sie Ihre Einordnung kurz.
  Falls `bandit` bei Ihnen nichts findet: Woran liegt das vermutlich?

[HINT::Ich bekomme viele `B101`-Meldungen aus meinen Tests]
Überlegen Sie, ob das, was Sie bei `delete` über `assert` gelernt haben, auch für Testcode gilt:
Schützt ein `assert` in einem Test irgendetwas?
Und wer würde Tests mit `-O` ausführen?
[ENDHINT]

- [EQ] Würden Sie `bandit` in einem eigenen Projekt regelmäßig einsetzen,
  beispielsweise automatisch in einer CI-Pipeline?
  Was spricht dafür, was dagegen?

<!-- time estimate: 10 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint ist `mitglieder.py` im Endzustand.
Kopieren Sie die Datei dazu aus dem Hilfsbereich in Ihr Aufgabenverzeichnis im Repo.)

[ENDSECTION]
[INSTRUCTOR::Zwei `B311`-Meldungen verschieden beurteilt? Grenzen von `bandit` erkannt?]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:bandit.prot]

[ENDINSTRUCTOR]
