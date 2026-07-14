title: "Blockchain verketten"
stage: alpha
timevalue: 3.0
difficulty: 3
assumes: git-Rebase, m_json, m_hashlib
---

[SECTION::goal::product]
Ich kann Blöcke mithilfe von SHA256-Hashs kryptografisch verketten, sodass
Änderungen die Kette ungültig machen.
[ENDSECTION]


[SECTION::background::default]
Eine Blockchain ist eine Möglichkeit, Daten zu speichern und die Gültigkeit der Daten
ohne zentrale Vertrauensstelle zu überprüfen.
Innerhalb einer Blockchain gibt es definierte Regeln, so dass die Gültigkeit
der Daten, durch die Daten selbst bestätigt werden kann.
[ENDSECTION]


[SECTION::instructions::loose]


### Programmiersprache auswählen

In diesem Programmierprojekt ist die Programmiersprache freiwählbar.
Im Rahmen dieses Projekts müssen JSON-Daten verarbeitet, im Dateisystem gespeichert
und eine REST-API bereitgestellt werden.
Hierbei sollte eine Sprache genutzt werden, in der Sie diese Anforderungen umsetzen können.
Das ProPra bietet ausreichend Ressourcen, um dieses Projekt in Python zu implementieren.

[EQ] Erläutern Sie kurz, warum Sie sich für die gewählte Programmiersprache entschieden haben.


### Daten verketten

In einer Blockchain werden Daten in sogenannten Blöcken gespeichert.
In jedem Block gibt es eine Referenz auf den vorherigen Block.
Diese Referenz wird in der Regel durch eine [TERMREF::kryptografische Hashfunktion]
über den Block erstellt: den *Block-Hash*.

Wenn nun der erste Block geändert wird, muss sich der zweite ändern.
In einer Blockchain ist es nicht möglich, einen Block zu verändern, ohne
**alle** Blöcke danach zu verändern.

[ER] Wechseln Sie in Ihr Hilfsverzeichnis.
Erstellen Sie dort (also _nicht_ in Ihrem normalen Repo) einen neuen Ordner `blockchain_example`.
Initialisieren Sie in dem Ordner ein neues Git-Repo und erstellen Sie dort eine Datei
`Block1.txt` mit beliebigem Inhalt.
Erzeugen Sie anschließend ein Commit mit der Nachricht `Block1`.
Wiederholen Sie dies analog mit der Datei `Block2.txt` und den Commit `Block2`.

[EC] Geben Sie nun Ihre Git-History einzeilig aus.

[HINT::Wie gebe ich die Git-History aus?]
Die Git-History können Sie mit dem `git log` Kommando ausgeben.
[git-log Dokumentation](https://git-scm.com/docs/git-log).

[HINT::Wie kann ich nur eine Zeile pro Commit ausgeben?]
Wenn Sie nur eine Zeile ausgeben wollen, können Sie die Flag `--oneline`
dem Kommando hinzufügen.
[ENDHINT]

[ENDHINT]

[HINT::Die Ausgabe wird nicht in die Shell gedruckt.]
Standardmäßig wird die Ausgabe von `git` in einen sogenannten *Pager* übergeben.
Ein Pager wird in Unix-Systemen genutzt, um lange Dateien im Terminal zu lesen und scrollen zu können.
Sie können dies mit
[der Flag `--no-pager`](https://git-scm.com/docs/git#Documentation/git.txt---no-pager)
verhindern, um die Ausgabe direkt in das Terminal zu drucken.

```
git --no-pager log --oneline

```
[ENDHINT]

[ER] Nutzen Sie 
[git-rebase](https://git-scm.com/docs/git-rebase),
um im ersten Commit (`Block1`) die Datei `Block1.txt` zu verändern.
Der zweite Commit `Block2` soll unverändert übernommen werden.

[EC] Geben Sie die einzeilige Git-History aus.

Sie können sehen, dass sich beide Commit-Hashes verändert haben, obwohl Sie lediglich
den ersten Commit bearbeitet haben.
Dies begründet sich am oben beschriebenen Prinzip.
Git verknüpft die Commits über die Commit-Hashes miteinander.
Wenn ein Commit bearbeitet wird, ändern sich alle Hashes der nachfolgenden Commits.
Die Daten selbst bilden keine Blockchain, sondern die Commit-Hashes.

Das Verzeichnis sieht nach dem Rebase genauso aus wie vorher,
es existieren beide Dateien mit Inhalt.
Durch die veränderten Commit-Hashes kann erkannt werden, dass die Dateien verändert wurden.

Dass diese Manipulation in Git so einfach möglich ist, ist an dieser Stelle gewollt.
In kryptografischen Blockchains allerdings nicht.
Hier soll eine Manipulation so aufwendig sein, dass sie praktisch nicht möglich ist.
Inwiefern und auf welche Art das in Bitcoin und Sedricoin geschützt wird,
wird in einer späteren Aufgabe erläutert.


### Programmaufbau

Sowohl Bitcoin, als auch Git sind als verteilte Systeme entworfen.
Sedricoin soll vereinfacht als Client-Server-Architektur entwickelt werden.
Die Peer-to-Peer-Funktionalität wird erst später ergänzt werden.

[ER] Legen Sie ein Verzeichnis `Sedricoin` in Ihrem Arbeitsverzeichnis an.
Nutzen Sie dieses Verzeichnis für Ihre Sedricoin-Implementation.
Sie müssen für die folgenden Aufgaben daher lediglich *Dateilisten-Dateien* abgeben.

[NOTICE]
Durch die freie Wahl der Programmiersprache gibt es keine Vorgaben zur
Benennung der Dateien, Variablen oder Funktionen.
Halten Sie sich an die Namenskonvention Ihrer Sprache, beispielsweise in Python
an die Verwendung von Snake-Case (`foo_bar`, nicht `fooBar`).
Benennen Sie Ihre einzelnen Module/Teile sinnvoll, sodass ersichtlich ist,
ob es sich hierbei um den Server, den Client oder andere Hilfsfunktionen handelt.
[ENDNOTICE]


### Server-Grundlagen

Bevor Sie selbst beginnen, die Sedricoin-Blockchain zu implementieren, müssen
hierfür Standards festgelegt werden.

Die Sedricoin-Blockchain soll als JSON-Datei im Dateisystem gespeichert werden.
Achten Sie darauf, diese Dateien nicht im Arbeitsverzeichnis, sondern im Hilfsverzeichnis
zu schreiben, damit sie nicht in Ihrem Git-Repo liegen.

Einstellungen werden über Umgebungsvariablen eingelesen.
Die angegebenen Variablen überschreiben immer die Standardwerte, falls Sie diese anlegen.
Ihre Implementierung soll diese Umgebungsvariablen akzeptieren:

```env
COIN_STORAGE_PATH="/pfad/zu/den/sedricoin/blöcken/"
```

Außerdem muss die zu speichernde JSON-Datei (das Modell) definiert werden.
Im Verlauf dieses Projekts werden die Modelle immer wieder erweitert, bis die
ganze Funktionalität abgebildet ist.
Ein `Block` besteht aus dem `BlockHeader` und den Transaktionsdaten.
Die Daten werden vorerst weggelassen.
Der `BlockHeader` beschreibt den `Block` und beinhaltet aktuell die Felder:

- `previous_hash`: `String` (Hex-Repräsentation des vorherigen Block-Hash; nur *lower-case*)
- `timestamp`: `unsigned Integer` (Unix-Timestamp in Sekunden)

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

Jeder Block hat einen Block-Hash.
Dieser wird nicht explizit gespeichert, sondern kann nach folgenden Regeln berechnet werden:

1. Die Werte der Felder mit `;` getrennt zu einem `String` aneinanderreihen.
   Die Reihenfolge der Werte muss der im JSON oben entsprechen.
2. Alle Zeichen in `lower-case` umwandeln.
3. Leerzeichen und alle anderen `Whitespace`-Zeichen entfernen.
4. Den doppelten `SHA256`-Hash berechnen; also `SHA256(SHA256(x))`.
   Dabei muss der String im inneren Hash mit `UTF-8` enkodiert werden.
   Der äußere Hash wird über die Bytes des ersten Hashs gebildet.
5. Der Block-Hash ist die Hex-Repräsentation des Ergebnisses.

Der gegebene Block hat also den Block-Hash
`807eee99f5758108077c7be5ca7c2ef37c8b5b3f3046260ed9867b4eb08f7e3b`.

[HINT::Ich berechne einen anderen Block-Hash]
Der Block-Hash berechnet sich nur über die aneinandergereihten Werte.
Er muss über den String
`"0000000000000000000000000000000000000000000000000000000000000000;1783428541"`
berechnet werden.

Außerdem muss der String in `UTF-8` enkodiert werden, und der Hash über die
Bytes berechnet werden.

[HINT::Musterlösung in Python]

In Python muss der Hash wie folgt berechnet werden:

```py
from hashlib import sha256

values = "0000000000000000000000000000000000000000000000000000000000000000;1783428541".lower()

block_hash = sha256(sha256(values.encode("utf-8")).digest()).hexdigest()
print(block_hash)
```
[ENDHINT]

[ENDHINT]

[ER] Implementieren Sie nun die ersten Grundlagen für Ihren Sedricoin-Server,
der die folgende Funktionalität umfasst:

- Ein `Block` kann aus einer JSON-Datei geladen und als solche im Dateisystem gespeichert werden.
- Der Block-Hash kann korrekt berechnet werden.
- Nutzen Sie als ersten `Block` den oben genannten.
  Wenn der erste `Block` noch nicht existiert, soll er erstellt werden.
  Er muss, analog zu Bitcoin, fest in den Code geschrieben werden.
- Beim Starten werden die angegebenen Umgebungsvariablen geladen.
  Der Server beachtet diese als Konfiguration.
- Beim Starten wird die aktuelle Blockchain auf der Konsole ausgegeben.
  Pro Block jeweils eine Zeile `<Blockhöhe> <Block-Hash>`.
  Die Blockhöhe ist der Index des Blocks in der Blockchain.
- Wenn der Server ausgeführt wird, wird ein neuer `Block` mit dem aktuellen
  Zeitstempel, der Höhe und dem vorherigen Block-Hash berechnet, in der Blockchain gespeichert
  und auf der Konsole ausgegeben.
  Danach endet das Programm.
- Falls beim Laden die Blockchain ungültig ist, wird auf der Konsole ausgegeben,
  an welcher Stelle die Kette ungültig ist und es wird kein neuer `Block` berechnet.

[NOTICE]
Ihre Implementierung darf mehrere Dateien umfassen.
So ist es beispielsweise üblich, Datenmodelle in eigene Dateien zu schreiben.
Sie werden in diesem Projekt keine Vorgaben über die genaue Softwarearchitektur erhalten.
Überlegen Sie sich eine sinnvolle Struktur und passen Sie diese, falls nötig, an.
[ENDNOTICE]


### Projektbeschreibung

Zur Korrektur ist es notwendig, dass die Tutor_innen wissen, wie sie Ihre
Programme aufrufen können.

[ER] Legen Sie dafür in Ihrem `Sedricoin`-Ordner die folgende, ausgefüllte `README.md`
Datei an und pflegen Sie diese im Verlauf dieses Projekts.
Ihre Programme müssen aus dem Basisverzeichnis aufgerufen werden können.

````md
# Sedricoin

Zuletzt bearbeitete Aufgabe: coin-chain

## Umgebungsvariablen

```
STORAGE_PATH=/home/adrian/sedricoin
```

## Server

Sprache: `Python 3.14`
Dependencies installieren:

```
pip install "fastapi[standard]"
```

Server aufrufen:

```
python3 server.py
```

## Client

*Noch nicht implementiert*

Sprache: `Python 3.14`
Dependencies:

```
pip install requests
```

Client starten:

```
python3 client.py
```
````

[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
