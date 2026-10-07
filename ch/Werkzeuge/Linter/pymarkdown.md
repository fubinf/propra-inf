title: Markdown-Dateien prüfen mit PyMarkdown
stage: alpha
timevalue: 2
difficulty: 2
explains: CommonMark
assumes: Markdown, venv
---

[SECTION::goal::trial]

- Ich kann Markdown-Dateien mit `PyMarkdown` prüfen und seine Meldungen lesen.
- Ich habe erlebt, dass zwei verbreitete Markdown-Programme dasselbe Dokument unterschiedlich darstellen,
  und kann einschätzen, welche Meldungen echte Darstellungsfehler betreffen und welche nur den Stil.
- Ich kann `PyMarkdown` an die Konventionen eines Projekts anpassen
  und weiß, warum man das vor dem automatischen Korrigieren tun sollte.
- Ich weiß, was die automatische Korrektur leistet und wo sie an ihre Grenzen stößt.

[ENDSECTION]
[SECTION::background::default]

Markdown wirkt so einfach, dass man selten nachprüft, was am Ende daraus wird.
Wer schreibt, sieht den Quelltext, und der ist ja gut lesbar.
Wer liest, sieht dagegen meist die daraus erzeugte HTML-Darstellung.
Die fällt je nach Programm verschieden aus, denn Markdown hat Dialekte
(siehe den Warnhinweis in [PARTREF::Markdown]).
Der wichtigste ist [TERMREF::CommonMark]; ihm folgen z.B. GitHub, GitLab und die Markdown-Vorschau von VS Code.
Das ProPra benutzt dagegen die Bibliothek Python-Markdown, die sich an der Urfassung von Markdown orientiert.
Damit entsteht nicht nur die ProPra-Website,
sondern auch die Ansicht, in der Ihre Tutor_innen Ihre Markdown-Abgaben lesen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Vorbereitung

`PyMarkdown` ist ein in Python geschriebener [TERMREF::Linter] für Markdown.
Er kennt gut 50 Regeln.
Manche betreffen nur den Stil des Quelltexts,
andere warnen vor Stellen, die in manchen Dialekten anders dargestellt werden als gemeint.
Welche Regel zu welcher Sorte gehört, steht nirgends übersichtlich beisammen.
Das finden wir in dieser Aufgabe an einem Beispiel selbst heraus.

Legen Sie für diese Aufgabe ein frisches [PARTREF::venv] an und aktivieren Sie es.

- [EC] `pip install pymarkdownlnt markdown markdown-it-py`

Damit haben Sie drei Pakete installiert:

- `pymarkdownlnt` ist der Linter `PyMarkdown`; sein Kommando heißt `pymarkdown`.
- `markdown` ist Python-Markdown, das Markdown so in HTML umwandelt wie das ProPra.
- `markdown-it-py` wandelt Markdown nach den Regeln von CommonMark in HTML um.

[WARNING]
Verwechseln Sie die beiden ähnlich klingenden Namen nicht:
**PyMarkdown** prüft Markdown, **Python-Markdown** wandelt Markdown in HTML um.
[ENDWARNING]

Legen Sie in Ihrem [TERMREF::Hilfsbereich] ein Verzeichnis `pymarkdown_demo` an.
Führen Sie alle Kommandos dort aus, sofern nichts anderes gesagt ist.

`markdown-it-py` bringt zwar ein eigenes Kommando mit,
das kennt aber nur reines CommonMark und damit keine Tabellen.
Tabellen sind eine Erweiterung, die z.B. GitHub zusätzlich unterstützt.
Legen Sie deshalb die Datei `commonmark.py` mit folgendem Inhalt an.
Sie erzeugt einen CommonMark-Übersetzer, schaltet die Tabellen-Erweiterung ein
und gibt die übergebene Datei als HTML aus:

```python
import sys
from markdown_it import MarkdownIt

md = MarkdownIt("commonmark").enable("table")
print(md.render(open(sys.argv[1], encoding="utf-8").read()), end="")
```

Szenario: Kim aus Ihrem Semester hat ein kleines Programm zum Lernen mit Karteikarten geschrieben
und möchte es demnächst veröffentlichen.
Kim hat Sie gebeten, vorher die Beschreibung `README.md` durchzusehen;
im Editor sehe sie ordentlich aus.

Legen Sie die Datei `README.md` mit folgendem Inhalt an.
Übernehmen Sie sie genau so, wie sie ist, auch wenn Ihnen schon Fehler auffallen.

[FOLDOUT::Inhalt von `README.md`]
````markdown
# Lernkarten

Ein kleines Kommandozeilenprogramm zum Lernen mit Karteikarten.
Es fragt Karten in zufälliger Reihenfolge ab und merkt sich Ihren Lernstand.

Inhalt:
- [Installation](#installation)
- [Benutzung](#benutzung)
- [Kartendatei](#kartendatei)
- [Konfiguration](#konfiguration)

#Installation

Sie brauchen Python 3.11 oder neuer, weitere Bibliotheken sind nicht nötig.
Laden Sie das Programm herunter:
```
git clone https://example.org/kim/lernkarten.git
cd lernkarten
```

## Benutzung

Gestartet wird das Programm mit dem Namen einer Kartendatei:

    python lernkarten.py vokabeln.txt

Das Programm zeigt nacheinander die Vorderseiten der Karten. Mit <kbd>Enter</kbd> sehen Sie die Rückseite. Dann geben Sie an, ob Sie die Antwort wussten.
Mögliche Antworten:
* `j`: gewusst
* `n`: nicht gewusst
- `q`: Programm beenden
Ihr Lernstand wird in der Datei `fortschritt.json` gespeichert.

Brechen Sie das Programm ** nicht ** mit Strg+C ab,
sonst geht der Lernstand der aktuellen Runde verloren.

## Kartendatei
Die Karten stehen in einer einfachen Textdatei.

- Jede Zeile enthält genau eine Karte.
- Zwischen Vorder- und Rückseite steht ein Trennzeichen, meist ein Semikolon.
    - Leerzeichen um das Trennzeichen herum werden ignoriert.
- Leere Zeilen werden übersprungen.

**Beispiel**

```
Hund ; dog
Katze ; cat
```

#### Sonderzeichen

Soll eine Karte selbst das Trennzeichen enthalten,
schreiben Sie einen Rückwärtsstrich davor, also z.B. `\;`.

## Einstellungen

Beim Start liest das Programm die Datei `~/.lernkarten.toml`, falls es sie gibt:

| Einstellung | Bedeutung | Standardwert |
| --- | --- | --- |
| `runden` | Wie oft jede Karte richtig beantwortet werden muss | `3` |
| `mischen` | Karten in zufälliger Reihenfolge abfragen | `true` |
| `trenner` | Trennzeichen in der Kartendatei, z.B. `;` oder `|` | `;` |

## Lizenz

MIT-Lizenz, siehe https://opensource.org/license/mit

![](screenshot.png)
````
[ENDFOLDOUT]

<!-- time estimate: 10 min -->


### Zwei Darstellungen vergleichen

Bevor wir `PyMarkdown` fragen, sehen wir selbst nach, was aus der Datei wird.
Wir wandeln sie einmal nach CommonMark und einmal mit Python-Markdown in HTML um
und vergleichen die Ergebnisse.

- [EC] `python commonmark.py README.md > commonmark.html`
- [EC] `python -m markdown -o html -x fenced_code -x tables README.md > python-markdown.html`  
  (Die beiden `-x` schalten die Erweiterungen für Codeblöcke mit drei Backticks und für Tabellen ein,
  die auch das ProPra benutzt.)
- [EC] `diff commonmark.html python-markdown.html`

`diff` zeigt nur die Stellen, an denen sich die beiden Dateien unterscheiden.
Zeilen mit `<` stammen aus der ersten Datei (CommonMark), Zeilen mit `>` aus der zweiten (Python-Markdown).
Bedeutungslos sind Unterschiede in der Schreibweise oder Reihenfolge von Attributen (wie bei `<img ...>`)
oder in Zeilenumbrüchen zwischen HTML-Elementen, ebenso der Hinweis `No newline at end of file`.

[HINT::Ich kenne mich mit HTML kaum aus]
Hier genügen wenige HTML-Elemente.
Jedes beginnt mit `<name>` und endet mit `</name>`:

- `<h1>`, `<h2>`, ...: Überschrift der Ebene 1, 2, ...
- `<p>`: Absatz
- `<ul>`: Aufzählung; jeder ihrer Punkte steht in einem `<li>`
- `<pre><code>`: Codeblock; `<code>` allein: Code im Fließtext
- `<strong>`: Fettdruck
- `<a href="...">`: Link
- `<table>`, `<tr>`, `<td>`: Tabelle, Tabellenzeile, Tabellenzelle
- `<img>`: Bild; das Attribut `alt` enthält einen Ersatztext für Menschen, die das Bild nicht sehen können

Mehr dazu unter [TERMREF::HTML-Tag].
[ENDHINT]

- [EQ] Beschreiben Sie jede inhaltliche Abweichung zwischen den beiden Darstellungen:
  Was zeigt CommonMark, was zeigt Python-Markdown, und was hat Kim offensichtlich gemeint?
- [EQ] Nicht jedes Problem zeigt sich als Unterschied.
  Sehen Sie sich `commonmark.html` vollständig an, z.B. mit `less` oder in Ihrem Editor.
  Finden Sie zwei Stellen, die in _beiden_ Darstellungen anders aussehen, als Kim es gemeint hat.

[HINT::Ich finde keine solche Stelle]
Suchen Sie im Quelltext die Stellen, an denen Kim etwas hervorheben oder verlinken wollte.
Was ist im HTML daraus geworden?
[ENDHINT]

<!-- time estimate: 15 min -->


### Was meldet `PyMarkdown`?

- [EC] `pymarkdown scan README.md`

Nehmen wir als Beispiel diese Meldung:

```text
/home/.../pymarkdown_demo/README.md:12:1: MD018: No space present after the hash character on a possible Atx Heading. (no-missing-space-atx)
```

- Am Anfang stehen Datei (immer mit vollständigem Pfad), Zeile und Spalte.
- `MD018` ist die Nummer der Regel.
  Im Folgenden nennen wir Regeln nur bei ihrer Nummer.
- Danach folgen eine kurze Beschreibung, manchmal Details in eckigen Klammern,
  und am Ende in runden Klammern der Kurzname der Regel.

Jede Regel ist in der
[Regelübersicht](https://pymarkdown.readthedocs.io/en/stable/rules/)
ausführlich beschrieben, samt einer Begründung (Abschnitt "Reasoning").

- [EQ] Welche der Probleme, die Sie oben gefunden haben, meldet `PyMarkdown`, und mit welcher Regel?
  Zu welchen passt keine Meldung?

[HINT::Ich finde zu fast jedem Problem eine Meldung]
Wo ist in `commonmark.html` der Satz "Ihr Lernstand wird ..." gelandet?
Gibt es eine Meldung zu Zeile 32?
Die Meldung zu Zeile 31 betrifft die fehlende Leerzeile _über_ dem Listenpunkt.
Und gibt es irgendeine Meldung zu der Tabelle?
[ENDHINT]

[HINT::Was hat es mit MD051 auf sich?]
Ein Link auf `#konfiguration` springt zu der Überschrift, deren Sprungziel `konfiguration` heißt.
Solche Sprungziele erzeugen GitHub, die meisten Editor-Vorschauen und auch das ProPra
automatisch aus dem Text jeder Überschrift.
Unsere beiden Kommandos von oben tun das nicht; deshalb sehen Sie davon im HTML nichts.
Gibt es eine Überschrift "Konfiguration"?
Und warum meldet `PyMarkdown` auch den Link auf `#installation`?
[ENDHINT]

Nicht jede Meldung ist gleich wichtig.
Wir unterscheiden drei Kategorien:

- **Fehler**: In mindestens einer der beiden Darstellungen kommt etwas anderes heraus, als Kim gemeint hat,
  oder ein Link führt ins Leere.
- **Risiko**: In unseren beiden Darstellungen ist alles in Ordnung,
  aber in anderen Markdown-Programmen oder für manche Menschen entstehen Probleme.
- **Stil**: Die Darstellung ist überall dieselbe;
  die Regel sorgt nur für einen einheitlicheren, besser lesbaren Quelltext.

- [EQ] Ordnen Sie die Regeln MD013, MD018, MD031, MD032, MD045 und MD046 je einer der drei Kategorien zu.
  Begründen Sie bei Fehlern und Risiken in einem Satz, was schiefgeht,
  bei Fehlern auch, in welchem der beiden Dialekte.
  Bei Stil genügt die Einordnung.

[HINT::Ich weiß nicht, ob eine Regel ein Risiko ist oder nur Stil]
Lesen Sie in der Beschreibung der Regel den Abschnitt "Reasoning".
Dessen Unterabschnitte heißen z.B. "Correctness", "Accessibility", "Portability", "Readability" oder "Consistency".
Die ersten drei deuten auf einen Fehler oder ein Risiko hin.
Bei den übrigen lohnt ein zweiter Blick:
Steht dort, dass manche Markdown-Programme ("parsers") das Element sonst nicht erkennen
oder dass Screenreader ("assistive technologies") darauf angewiesen sind, ist es ein Risiko.
[ENDHINT]

<!-- time estimate: 25 min -->


### Erst konfigurieren, dann korrigieren

Manche Meldungen kann `PyMarkdown` selbst beheben.
Vorher sollten wir aber prüfen, ob die Regeln zu unserem Projekt passen,
denn die automatische Korrektur richtet sich nach ihnen.

Ein Kandidat ist MD007.
Kim hat die Unterliste im Abschnitt "Kartendatei" um 4 Leerzeichen eingerückt,
wie es auch [PARTREF::Markdown] empfiehlt.
`PyMarkdown` erwartet standardmäßig 2.
Probieren wir aus, was beides in Python-Markdown bewirkt.
`printf '%s\n'` gibt dabei jedes seiner Argumente auf einer eigenen Zeile aus;
so entsteht ohne eigene Datei ein kleines Markdown-Dokument.

- [EC] `printf '%s\n' '- a' '  - b' '- c' | python -m markdown`
- [EC] `printf '%s\n' '- a' '    - b' '- c' | python -m markdown`
- [EQ] Was würde in der Ansicht Ihrer Tutor_innen aus Kims Unterliste,
  wenn `PyMarkdown` sie nach der Standardeinstellung von MD007 korrigierte?
  Was sagt der Abschnitt "Reasoning" in der Beschreibung von
  [MD007](https://pymarkdown.readthedocs.io/en/stable/plugins/rule_md007/) dazu?

Wie `black` (siehe [PARTREF::black]) liest auch `PyMarkdown` seine Einstellungen
aus der Datei `pyproject.toml` im aktuellen Verzeichnis, und zwar aus dem Abschnitt `[tool.pymarkdown]`.
Einstellungen einer Regel schreibt man dort als `plugins.<regel>.<parameter> = <wert>`,
mit der Regelnummer in Kleinbuchstaben, also z.B. `plugins.md013.line_length = 100`.
Welche Parameter eine Regel hat, steht in ihrer Beschreibung unter "Configuration".
Kommentare beginnen in dieser Datei mit `#`.

- [ER] Legen Sie eine Datei `pyproject.toml` an, die MD007 auf eine Einrückung von 4 Leerzeichen einstellt.
  Begründen Sie die Einstellung mit einem Kommentar in der Datei.

Ein zweiter Kandidat ist MD033, die Regel gegen HTML im Markdown-Text.
Kim benutzt das HTML-Element `<kbd>`, das eine Taste der Tastatur kennzeichnet.
Es wird in beiden Dialekten richtig dargestellt, und ein Markdown-Gegenstück dazu gibt es nicht.

- [ER] Erlauben Sie in `pyproject.toml` das Element `kbd`,
  siehe den Parameter `allowed_elements` in der Beschreibung von
  [MD033](https://pymarkdown.readthedocs.io/en/stable/plugins/rule_md033/).
  Begründen Sie auch das mit einem Kommentar.

[HINT::Mein Wert für `allowed_elements` verbietet plötzlich andere Dinge]
Ihr Wert _ersetzt_ die Voreinstellung, er ergänzt sie nicht.
Sehen Sie in der Beschreibung von MD033 nach, was standardmäßig erlaubt ist,
und übernehmen Sie das in Ihre Liste.
[ENDHINT]

Ein Linter kann nicht nur zu streng eingestellt sein, sondern auch zu nachsichtig.
Zu zwei Problemen hat `PyMarkdown` oben gar nichts gemeldet:

- Für Zeilen, die ohne Einrückung an einen Listenpunkt anschließen (engl. _lazy continuation lines_),
  hat `PyMarkdown` die Regel PML102.
  Sie ist allerdings standardmäßig ausgeschaltet, weil solche Zeilen in CommonMark erlaubt sind;
  siehe die Beschreibung von
  [PML102](https://pymarkdown.readthedocs.io/en/stable/plugins/rule_pml102/).
- Tabellen gehören nicht zu CommonMark, sondern sind eine Erweiterung.
  `PyMarkdown` erkennt sie erst, wenn man seine Erweiterung `markdown-tables` einschaltet.
  Welche Erweiterungen es gibt, zeigt `pymarkdown extensions list`.

Ein- und ausschalten lassen sich Regeln mit `plugins.<regel>.enabled = true` bzw. `false`
und Erweiterungen mit `extensions.<erweiterung>.enabled = true` bzw. `false`.

- [ER] Schalten Sie in `pyproject.toml` die Regel PML102 und die Erweiterung `markdown-tables` ein,
  wieder mit Kommentaren.

Man kann eine Regel auch nur für eine einzelne Stelle abschalten,
mit einem HTML-Kommentar wie `<!-- pyml disable-next-line md033-->` auf einer eigenen Zeile davor,
ähnlich wie mit `# noqa` in [PARTREF::flake8].
Die Varianten solcher Kommentare stehen in der Beschreibung der
[Pragmas](https://pymarkdown.readthedocs.io/en/stable/extensions/pragmas/).
Ein solcher Kommentar passt für eine einzelne, begründete Ausnahme;
eine Konvention, die im ganzen Projekt gilt, gehört dagegen in `pyproject.toml`.

- [EC] `pymarkdown scan README.md`
- [EQ] Welche Meldungen sind verschwunden, welche sind neu hinzugekommen?
  Was sagt die neue Meldung zur Tabelle aus, und trifft sie den Kern des Problems?

[HINT::Meine Einstellungen wirken nicht]
Liegt `pyproject.toml` im aktuellen Verzeichnis, und heißt der Abschnitt genau `[tool.pymarkdown]`?
Mit `pymarkdown --strict-config scan README.md` meldet `PyMarkdown` fehlerhafte Einstellungen,
statt sie stillschweigend zu übergehen.
[ENDHINT]

<!-- time estimate: 20 min -->


### Automatisch korrigieren

- [EC] `cp README.md README-vorher.md`
- [EC] `pymarkdown fix README.md`
- [EC] `diff README-vorher.md README.md`
- [EC] `pymarkdown scan README.md`
- [EQ] Welche Meldungen hat `fix` beseitigt?
  Welche Meldung ist durch die Korrektur neu entstanden, und warum?

Sehen wir uns nun die Liste der möglichen Antworten in der CommonMark-Darstellung an.
`grep -A 7` zeigt die gefundene Zeile und die 7 folgenden.

- [EC] `python commonmark.py README.md | grep -A 7 'Mögliche'`
- [EQ] Ist die Liste jetzt so, wie Kim sie gemeint hat?
  Was hat `fix` daran verbessert, was nicht?
  PML102 schlägt vor, die Zeile "Ihr Lernstand ..." um 2 Leerzeichen einzurücken.
  Was würde das bewirken, und ist es das, was Kim wollte?

[HINT::Ich weiß nicht, was das Einrücken bewirken würde]
Eine Zeile, die so weit eingerückt ist wie der Text des Listenpunkts darüber,
gehört ausdrücklich zu diesem Listenpunkt.
Wo soll der Satz "Ihr Lernstand ..." nach Kims Absicht stehen?
[ENDHINT]

<!-- time estimate: 10 min -->


### Von Hand korrigieren

Den Rest müssen Sie selbst erledigen.

- [ER] Ändern Sie `README.md` so, dass `PyMarkdown` nichts mehr meldet
  und beide Darstellungen zeigen, was Kim gemeint hat.
  Wo Kims Absicht nicht eindeutig ist, entscheiden Sie selbst.

Für die überlange Zeile (MD013) gibt es zwei übliche Wege:
den Text dort umbrechen, wo die Zeile 80 Zeichen erreicht,
oder nach jedem Satz eine neue Zeile beginnen.
Nehmen Sie den zweiten Weg; auch die Quelltexte der ProPra-Aufgaben sind so geschrieben.

- [EQ] Innerhalb eines Absatzes ändert ein einzelner Zeilenumbruch nichts an der Darstellung.
  Warum ist "ein Satz pro Zeile" trotzdem praktisch, sobald die Datei mit git verwaltet wird?
  Denken Sie an `git diff`, nachdem jemand in einem langen Absatz ein einziges Wort geändert hat.

[HINT::Was mache ich mit `**Beispiel**`?]
Überlegen Sie, welche Gliederung Kim gemeint hat:
Zu welchem Abschnitt gehört "Beispiel", und welche Überschriftenebene ergibt sich daraus?
[ENDHINT]

[HINT::Welche Sprache gebe ich bei den Codeblöcken an?]
Shell-Kommandos kennzeichnet man mit `bash`, Text ohne besondere Syntax mit `text`.
[ENDHINT]

[HINT::Wie bringe ich den senkrechten Strich in die Tabelle?]
In Tabellen kann man `|` mit einem vorangestellten Rückwärtsstrich als gewöhnliches Zeichen kennzeichnen.
Prüfen Sie Ihre Lösung in beiden Darstellungen.

[HINT::In einer der beiden Darstellungen erscheint der Rückwärtsstrich mit]
Innerhalb von Backticks wirkt `\|` nur in CommonMark-Tabellen,
in Python-Markdown erscheint der Rückwärtsstrich dort mit.
Außerhalb von Backticks verstehen beide Dialekte `\|` als einfachen senkrechten Strich.
Dafür muss dieser eine Strich auf die Code-Formatierung verzichten.
Oder Sie formulieren den Text so um, dass er ohne `|` auskommt.
[ENDHINT]
[ENDHINT]

- [EC] `pymarkdown scan README.md; echo $?`

`echo $?` zeigt den Exit-Status des vorigen Kommandos:
0 heißt "keine Meldungen", 1 heißt "mindestens eine Meldung".
Daran erkennt z.B. eine [TERMREF::CI/CD]-Pipeline, ob die Prüfung bestanden ist.

Zum Schluss vergleichen wir die beiden Darstellungen noch einmal.

- [EC] `python commonmark.py README.md > commonmark.html`
- [EC] `python -m markdown -o html -x fenced_code -x tables README.md > python-markdown.html`
- [EC] `diff commonmark.html python-markdown.html`

Jetzt sollten nur noch bedeutungslose Unterschiede übrig sein.
Ein Problem, das in beiden Darstellungen gleich falsch ist, zeigt `diff` allerdings nicht an;
sehen Sie deshalb auch selbst noch einmal in `commonmark.html` nach.

<!-- time estimate: 25 min -->


### Ihre eigenen Abgaben

Nun zu Ihren eigenen Markdown-Dateien.
Wechseln Sie dazu in Ihr ProPra-Repo.
Weil `PyMarkdown` seine `pyproject.toml` nur im aktuellen Verzeichnis sucht,
geben Sie Ihre Einstellungen mit `--config` ausdrücklich an.
Damit der Pfad nicht jedes Mal getippt werden muss, legen wir ihn in einer Shellvariablen ab:

- [EC] `cfg=<pfad>/pymarkdown_demo/pyproject.toml`
  (für `<pfad>` setzen Sie den Pfad zu Ihrem Hilfsbereich ein)

Rufen Sie nun `pymarkdown --config "$cfg" scan -r .` auf; `-r` durchsucht alle Unterverzeichnisse.
Dieser Aufruf gehört nicht ins Kommandoprotokoll.

[HINT::Es erscheinen Dateien, die ich gar nicht geschrieben habe]
Vermutlich liegt ein venv innerhalb Ihres Repos,
und `PyMarkdown` untersucht auch die Markdown-Dateien der dort installierten Bibliotheken.
Schließen Sie das venv mit `--exclude` aus, und zwar mit seinem Namen ohne vorangestelltes `./`,
beispielsweise so:
`pymarkdown --config "$cfg" scan -r --exclude .venv .`  
Das gilt dann auch für den folgenden Aufruf.
(Die Kurzform `-e` vermeiden wir hier: Vor `scan` bedeutet `-e` etwas ganz anderes.)
[ENDHINT]

Bei vielen Meldungen hilft ein Überblick, welche Regeln wie oft anschlagen:

- [EC] `pymarkdown --config "$cfg" scan -r . | grep -oE '(MD|PML)[0-9]{3}' | sort | uniq -c | sort -rn`

`grep -oE` gibt von jeder Meldung nur die Regelnummer aus,
`sort | uniq -c` zählt gleiche Nummern, und `sort -rn` sortiert nach Häufigkeit.

- [EQ] Welche drei Regeln schlagen am häufigsten an?
  Sehen Sie sich zu jeder eine Stelle in Ihren Dateien an
  und ordnen Sie sie in die drei Kategorien von oben ein.
  Haben Sie einen echten Fehler gefunden,
  also eine Stelle, die Ihre Tutor_innen anders zu sehen bekommen haben, als Sie es gemeint hatten?
  (Im Zweifel prüfen Sie die Datei mit `python -m markdown` wie oben.)
- [EQ] Welche Regeln würden Sie für Ihre ProPra-Abgaben zusätzlich anders einstellen oder abschalten?
  Warum?

<!-- time estimate: 15 min -->

[ENDSECTION]
[SECTION::submission::reflection,trace,snippet]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]
(Gemeint sind `README.md` und `pyproject.toml` im Endzustand.
Kopieren Sie beide Dateien dazu aus dem Hilfsbereich in Ihr Aufgabenverzeichnis im Repo.)

Und wo Sie schon dabei sind:
Prüfen Sie vor der Abgabe auch Ihr Markdown-Dokument zu dieser Aufgabe mit `PyMarkdown`.

[ENDSECTION]
[INSTRUCTOR::Dialektunterschiede verstanden? Grenzen der Regeln und von `fix` erkannt?]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
