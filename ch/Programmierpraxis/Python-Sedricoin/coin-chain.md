title: "Blockchain verketten"
stage: alpha
timevalue: 3.0
difficulty: 3
assumes: git-Repository, git-Rebase, m_json, m_hashlib, m_pydantic, m_pytest
---

[SECTION::goal::product]
Ich kann Blöcke mithilfe von SHA256-Hashes kryptografisch verketten, sodass
Änderungen die Kette ungültig machen.
[ENDSECTION]


[SECTION::background::default]
Eine Blockchain ist eine Möglichkeit, Daten zu speichern und die Gültigkeit der Daten
ohne zentrale Vertrauensstelle zu überprüfen.
Innerhalb einer Blockchain gibt es definierte Regeln, sodass die Gültigkeit
der Daten durch die Daten selbst bestätigt werden kann.
[ENDSECTION]


[SECTION::instructions::loose]


### Programmiersprache auswählen
<!-- time estimate: 10 min -->

In diesem Programmierprojekt ist die Programmiersprache frei wählbar.
Im Rahmen dieses Projekts müssen JSON-Daten verarbeitet, im Dateisystem gespeichert
und eine REST-API bereitgestellt werden.
Hierbei sollte eine Sprache genutzt werden, in der Sie diese Anforderungen umsetzen können.
Die Hinweise und Code-Beispiele gehen davon aus, dass Sie das Projekt in Python implementieren.
Wenn Sie eine andere Sprache wählen, erhöht sich der Schwierigkeitsgrad und
Sie müssen Probleme selbständig lösen.

[EQ] Erläutern Sie kurz, warum Sie sich für die gewählte Programmiersprache entschieden haben.


### Daten verketten
<!-- time estimate: 30 min -->

In einer Blockchain werden Daten in sogenannten Blöcken gespeichert.
In jedem Block gibt es eine Referenz auf den vorherigen Block.
Diese Referenz wird in der Regel durch eine [TERMREF::kryptografische Hashfunktion]
über den Block erstellt: den *Block-Hash*.

Wenn nun der erste Block geändert wird, muss sich der zweite ändern.
In einer Blockchain ist es nicht möglich, einen Block zu verändern, ohne
**alle** Blöcke danach zu verändern.

Wechseln Sie in Ihr Hilfsverzeichnis.
Erstellen Sie dort (also _nicht_ in Ihrem normalen Repo) ein neues
Verzeichnis `blockchain_example`.
Initialisieren Sie in diesem Verzeichnis ein neues Git-Repo und erstellen Sie dort
eine Datei `Block1.txt` mit beliebigem Inhalt.
Erzeugen Sie anschließend einen Commit mit der Nachricht `Block1`.
Wiederholen Sie dies analog mit der Datei `Block2.txt` und dem Commit `Block2`.

[HINT::Neues Git-Repo erstellen]
Ein Git-Repo können Sie mit dem Kommando `git init` erstellen, siehe
[git-init-Dokumentation](https://git-scm.com/docs/git-init).
[ENDHINT]

[EC] Geben Sie nun Ihre Git-History einzeilig aus.

[HINT::Wie gebe ich die Git-History aus?]
Die Git-History können Sie mit dem Kommando `git log` ausgeben, siehe
[git-log-Dokumentation](https://git-scm.com/docs/git-log).

[HINT::Wie kann ich nur eine Zeile pro Commit ausgeben?]
Wenn Sie nur eine Zeile ausgeben wollen, können Sie die Flag `--oneline`
dem Kommando hinzufügen.
[ENDHINT]

[ENDHINT]

[HINT::Die Ausgabe wird nicht in die Shell gedruckt.]
Standardmäßig wird die Ausgabe von `git` an einen sogenannten *Pager* übergeben.
Ein Pager wird in Unix-Systemen genutzt, um lange Dateien im Terminal zu lesen
und scrollen zu können.
Sie können dies mit
[der Flag `--no-pager`](https://git-scm.com/docs/git#Documentation/git.txt---no-pager)
verhindern, um die Ausgabe direkt in das Terminal zu drucken.

```
git --no-pager log --oneline
```
[ENDHINT]

Nutzen Sie
[git-rebase](https://git-scm.com/docs/git-rebase),
um im ersten Commit (`Block1`) die Datei `Block1.txt` zu verändern.
Der zweite Commit `Block2` soll unverändert übernommen werden.

[EC] Geben Sie die einzeilige Git-History aus.

Sie können sehen, dass sich beide Commit-Hashes verändert haben, obwohl Sie lediglich
den ersten Commit bearbeitet haben.
Dies ist durch das oben beschriebene Prinzip begründet.
Git verknüpft die Commits über die Commit-Hashes miteinander.
Wenn ein Commit bearbeitet wird, ändern sich alle Hashes der nachfolgenden Commits.
Nicht die Dateiinhalte bilden also die Kette, sondern die über die Commit-Hashes
verknüpften Commits.
In Sedricoin wird diese Idee nachgebaut:
Jeder Block verweist über seinen Hash auf seinen Vorgänger.

Das Verzeichnis sieht nach dem Rebase genauso aus wie vorher,
es existieren beide Dateien mit Inhalt.
Durch die veränderten Commit-Hashes kann erkannt werden, dass die Dateien verändert wurden.

Dass diese Manipulation in Git so einfach möglich ist, ist an dieser Stelle gewollt.
In einer Kryptowährungs-Blockchain ist sie dagegen unerwünscht:
Dort soll eine Manipulation so aufwendig sein, dass sie praktisch nicht möglich ist.
Inwiefern und auf welche Art das in Bitcoin und Sedricoin geschützt wird,
wird in einer späteren Aufgabe erläutert.


### Programmaufbau
<!-- time estimate: 5 min -->

[ER] Legen Sie ein Verzeichnis `Sedricoin` in Ihrem Arbeitsverzeichnis an.
Nutzen Sie dieses Verzeichnis für Ihre Sedricoin-Implementierung.

Die Anforderungen in dieser Aufgabengruppe beschreiben vor allem,
was Ihre Anwendung erfüllen soll.
Wie genau, müssen Sie selbst herausfinden.
In den Hinweisen folgen Tipps, wie Sie eine Anforderung erfüllen können.
Wichtige Dependencies werden explizit erwähnt, grundsätzlich dürfen Sie
die Standardbibliothek Ihrer Sprache verwenden.
Ihre Implementierung darf mehrere Dateien umfassen.
Sie werden in diesem Projekt keine Vorgaben über die genaue Softwarearchitektur erhalten.
Überlegen Sie sich eine sinnvolle Struktur und passen Sie diese, falls nötig, an.

[NOTICE]
Durch die freie Wahl der Programmiersprache gibt es keine Vorgaben zur
Benennung der Dateien, Variablen oder Funktionen.
Halten Sie sich an die Namenskonvention Ihrer Sprache, beispielsweise in Python
an die Verwendung von Snake-Case (`foo_bar`, nicht `fooBar`).
Benennen Sie Ihre einzelnen Module sinnvoll, sodass ersichtlich ist,
um welchen Teil der Anwendung es sich handelt.
[ENDNOTICE]


### Einstellungen über Umgebungsvariablen
<!-- time estimate: 20 min -->

[ER] Beim Starten soll der Server die Umgebungsvariablen einlesen.
Darüber können Einstellungen für das Programm gesetzt werden.
Alle Umgebungsvariablen bekommen das Präfix `SEDRICOIN_`.
Vorerst soll nur die Variable `SEDRICOIN_STORAGE_PATH` unterstützt werden.
Diese gibt den Speicherort der Blockchain an.
Sie müssen hier einen Pfad angeben, der im _Hilfsbereich_ ist, damit die Daten
nicht Teil Ihres Repos sind.
Wenn das angegebene Verzeichnis beim Start der Anwendung nicht existiert, soll es erstellt werden.
Scheitert dies, bricht die Anwendung ab.

[HINT::Umgebungsvariablen in Python einlesen]
Umgebungsvariablen können Sie mit der Funktion `getenv()` des Moduls
[`os`](https://docs.python.org/3/library/os.html#os.getenv)
der Python-Standardbibliothek auslesen.

Wollen Sie sehen, welche Umgebungsvariablen aktuell in Ihrer Shell gesetzt sind,
können Sie das Kommando `env` im Terminal ausführen.
[ENDHINT]

[HINT::Umgebungsvariablen im Terminal setzen]
Umgebungsvariablen können im Terminal mit dem Befehl `export` gesetzt werden.
Variablen, die auf diese Weise gesetzt werden, sind nur temporär
(bis Sie die Shell schließen) verfügbar.

```sh
export SEDRICOIN_STORAGE_PATH="/pfad/zum/sedricoin/blockchain/Verzeichnis"
```

Wollen Sie nun testen, ob die Variable korrekt gesetzt wurde, können Sie diese
wie folgt ausgeben:

```sh
echo $SEDRICOIN_STORAGE_PATH
```
[ENDHINT]

[WARNING]
Ihre Anwendung darf keine Umgebungsvariablen überschreiben.
Es dürfen höchstens Standardwerte verwendet werden, falls die entsprechende
Umgebungsvariable nicht gesetzt wurde.
[ENDWARNING]


### `Block`-Modell
<!-- time estimate: 30 min -->

Die Sedricoin-Blockchain soll als JSON-Dateien im Dateisystem gespeichert werden.
Pro Block soll im Verzeichnis eine Datei existieren.
Das Verzeichnis wird über die Umgebungsvariable gesetzt.

Ein `Block` besteht aus dem `BlockHeader` und den Transaktionsdaten.
Die Daten werden vorerst weggelassen.
Der `BlockHeader` beschreibt den `Block` und beinhaltet aktuell die Felder:

- `previous_hash`: `String` (Hex-Repräsentation des vorherigen Block-Hashes; nur *lower-case*)
- `timestamp`: `unsigned Integer` (Unix-Timestamp in Sekunden)

Im Verlauf dieses Projekts werden die Modelle immer wieder erweitert, bis die
ganze Funktionalität abgebildet ist.

So sieht das `Block`-Modell aktuell aus:

```json
{
  "header": {
    "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp": 1783428541
  }
}
```

[WARNING]
Achten Sie darauf, dass Ihre Implementierung die Feldnamen exakt übernimmt:
`previous_hash != previous_Hash` oder `previous_hash != previousHash`.
[ENDWARNING]

Da der erste Block noch keinen Vorgänger hat, wird dieser Null-Hash eingetragen.

[ER] Implementieren Sie das `Block`-Modell.
Dieses soll aus einer JSON-Datei gelesen und als solche im Dateisystem gespeichert werden können.
Außerdem muss das Modell auch intern in der Anwendung verwendbar sein.
Wenn Sie das Projekt in Python implementieren, nutzen Sie dafür die [PARTREF::m_pydantic]-Bibliothek.

[HINT::Wie kann ich Daten mit Pydantic modellieren?]
Legen Sie ein neues Modul `models.py` an, in dem Sie Ihre Datenmodelle implementieren.
Teilen Sie dabei den `Block` in mehrere Modelle auf: `Block` und `BlockHeader`.
Erstellen Sie im `Block` das Attribut `header: BlockHeader`, um die Modelle zu verschachteln.

In einer späteren Aufgabe werden dem `Block` auch noch Transaktionsdaten hinzugefügt.

Falls Sie eine andere Sprache nutzen, müssen Sie sich ggf. selbst eine Funktion
schreiben, die den `Block` in gültiges JSON umwandelt.
[ENDHINT]

Jeder Block hat einen Block-Hash.
Dieser wird nicht explizit gespeichert, sondern kann nach folgenden Regeln berechnet werden:

1. Die Werte der Felder mit `;` getrennt zu einem `String` aneinanderreihen.
   Die Reihenfolge der Werte muss dem gegebenen JSON-Modell entsprechen.
   Zukünftige Erweiterungen werden immer hinten angefügt.
2. Alle Werte, die nicht `String` sind, müssen in einen `String` umgewandelt werden.
3. Alle Zeichen in `lower-case` umwandeln.
4. Leerzeichen entfernen.
5. Den doppelten `SHA256`-Hash berechnen; also `SHA256(SHA256(x))`.
   Dabei muss der `String` im inneren Hash mit `UTF-8` enkodiert werden.
   Der äußere Hash wird über die Bytes des ersten Hashs gebildet.
6. Der Block-Hash ist die Hex-Repräsentation des Ergebnisses.

<!-- time estimate: 20 min -->
[ER] Implementieren Sie eine Funktion mit der der Block-Hash berechnet werden kann.
Der gegebene Block hat also den Block-Hash
`807eee99f5758108077c7be5ca7c2ef37c8b5b3f3046260ed9867b4eb08f7e3b`.

[HINT::Ich berechne einen anderen Block-Hash]
Der Block-Hash berechnet sich nur über die aneinandergereihten Werte.
Er muss über den `String`
`"0000000000000000000000000000000000000000000000000000000000000000;1783428541"`
berechnet werden.

Außerdem muss der `String` in `UTF-8` enkodiert werden, und der Hash über die
Bytes berechnet werden.

[HINT::Musterlösung in Python]

In Python muss der Hash wie folgt berechnet werden:

```py
from hashlib import sha256

values = "0000000000000000000000000000000000000000000000000000000000000000;1783428541"
normalized_values = values.replace(" ", "").lower().encode("utf-8")

block_hash = sha256(sha256(normalized_values).digest()).hexdigest()
print(block_hash)
```
[ENDHINT]
[ENDHINT]

<!-- time estimate: 25 min -->
[ER] Die Funktion zur Berechnung des Block-Hashes ist zentral für die Blockchain.
Schreiben Sie daher einen [TERMREF::Unittest], um sicherzustellen, dass die
Funktion korrekt funktioniert.
Nutzen Sie im Test die vorgegebenen Testfälle.
In Python können Sie dafür das [PARTREF::m_pytest]-Framework nutzen.

[FOLDOUT::Testfälle Block-Hash]
1. Genesis-Block-Test

```json
{
  "header": {
    "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp": 1783428541
  }
}
```

Block-Hash:
`807eee99f5758108077c7be5ca7c2ef37c8b5b3f3046260ed9867b4eb08f7e3b`

2. Lower-Case-Test

```json
{
  "header": {
    "previous_hash": "807EEE99F5758108077C7BE5CA7C2EF37C8B5B3F3046260ED9867B4EB08F7E3B",
    "timestamp": 1783428541
  }
}
```

Block-Hash:
`2093d1fa0b62abb409954fc97030e8c0bf4a4af499def428685a2c3617ee0c1f`

3. Leerzeichen-Test

```json
{
  "header": {
    "previous_hash": "807eee99f5758108077c7be5ca 7c2ef37c8b5b3f3046260ed9867b4eb08f7e3b ",
    "timestamp": 1783428541
  }
}
```

Block-Hash:
`2093d1fa0b62abb409954fc97030e8c0bf4a4af499def428685a2c3617ee0c1f`

[ENDFOLDOUT]


### Server aufrufen
<!-- time estimate: 30 min -->

Erst in den folgenden Aufgaben implementieren Sie die REST-API.
Allerdings müssen beim Starten, wie oben schon implementiert, die Umgebungsvariablen
eingelesen werden und der *Genesis-Block* (wie folgt) erzeugt werden.
Auch wenn das Programm in dieser Aufgabe noch nicht dauerhaft weiterläuft,
wird hier bereits von *Server* gesprochen.

[ER] Wenn der Server ausgeführt wird, soll ein neuer `Block` mit dem aktuellen Unix-Timestamp
berechnet und der Blockchain hinzugefügt werden.
Falls die Blockchain noch nicht existiert, wird im angegebenen Verzeichnis der *Genesis-Block*
als erste Datei angelegt.
Dieser Genesis-Block entspricht genau dem oben angegebenen JSON-Block.
Jede Sedricoin-Implementierung verwendet denselben Genesis-Block.
Benennen Sie die Block-Dateien nach der Block-Höhe.
Die Block-Höhe ist der Index des Blocks in der Blockchain.
Dieser wird nur berechnet, aber nicht im `Block` gespeichert.
Der Genesis-Block hat die Block-Höhe `0`.

[ER] Beim Ausführen der Anwendung soll die aktuelle Blockchain auf der Konsole ausgegeben werden.
Pro Zeile soll ein Block ausgegeben werden, im Format `<Block-Höhe>: <Block-Hash>`
bzw. `New Block <Block-Höhe>: <Block-Hash>`.
Falls beim Laden die Blockchain ungültig ist, wird auf der Konsole ausgegeben,
an welcher Stelle die Kette ungültig ist (`Blockchain Error at Block <Block-Höhe>.`),
und es wird kein neuer `Block` berechnet.
Für die Gültigkeit müssen aktuell die folgenden Kriterien erfüllt sein:

- Der `previous_hash` entspricht dem Block-Hash des Vorgängers.
  Achten Sie darauf, diesen selbst zu berechnen und nicht blind den Dateien zu vertrauen.
- Der `timestamp` muss größer als der des Vorgängers sein.

[NOTICE]
Zur Validierung sind vorerst keine Tests erforderlich, diese Tests werden in einer
späteren Aufgabe ausführlicher beschrieben.
[ENDNOTICE]

[EC] Rufen Sie Ihren Server zweimal auf.
Ändern Sie anschließend den `timestamp` im `Block` mit der Block-Höhe `1` und rufen
Sie den Server erneut auf.


### Projektbeschreibung
<!-- time estimate: 10 min -->

Zur Korrektur ist es notwendig, dass die Tutor_innen wissen, wie sie Ihre
Anwendung verwenden können.

[ER] Legen Sie dafür in Ihrem Verzeichnis `Sedricoin` die folgende, ausgefüllte `README.md`-Datei
an und pflegen Sie diese Dokumentation Ihrer Anwendung im Verlauf dieses Projekts.
Erklären Sie darin:

- welche Umgebungsvariablen eingelesen werden können.
- welche Programmiersprache verwendet wird.
- welche zusätzlichen Bibliotheken installiert werden müssen und wie dies geht.
- wie die Anwendung gestartet werden kann.
- wie die Tests ausgeführt werden können.


[FOLDOUT::Vorlage `README.md`]
````md
# Sedricoin

Zuletzt bearbeitete Aufgabe: coin-chain

## Umgebungsvariablen

```
SEDRICOIN_STORAGE_PATH=/home/adrian/sedricoin
```

## Server

Sprache: `<Ihre gewählte Programmiersprache eintragen>`
Dependencies installieren:

```
<Befehl zum Installieren der Dependencies einfügen>
```

Server aufrufen:

```
<Befehl zum Server aufrufen einfügen>
```

Tests ausführen:

```
<Befehl zum Tests ausführen einfügen>
```

````
[ENDFOLDOUT]

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode-files.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
