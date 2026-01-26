title: "Sedricoin Start"
stage: draft
timevalue: 0.0
difficulty: 3
assumes: m_hashlib, FastAPI-CRUD
---

[SECTION::goal::idea]

* Ich verstehe, wie Daten in einer Blockchain miteinander verknüpft werden.
* Ich implementiere einen Server, der eine minimale Blockchain speichert und eine
  REST-API zur Manipulation bereitstellt.

[ENDSECTION]


[SECTION::background::default]
Eine Blockchain ist eine Möglichkeit, Daten zu speichern und die Gültigkeit der Daten
ohne zentrale Vertrauensstelle zu überprüfen.

FastAPI bietet eine simple Möglichkeit, einen REST-API-Server zu implementieren,
der es erlaubt neue Blöcke zu erstellen und die vorhandenen Blöcke abzufragen.
Durch FastAPI wird während der Entwicklung automatisch die OpenAPI Spezifikation
erzeugt und zusätzlich ein Frontend bereitgestellt, um mit den Endpunkten
während der Entwicklung interagieren zu können.
[ENDSECTION]


[SECTION::instructions::loose]

### Daten zu einer Blockchain verketten

Bevor Sie beginnen den Server zu implementieren, machen Sie sich mit der Idee einer
Blockchain vertraut:
In einer Blockchain werden Daten in sogenannten Blöcken gespeichert.
In jedem Block gibt es eine Referenz auf den vorherigen Block.
Diese Referenz wird in der Regel durch eine [TERMREF::kryptografische Hashfunktion]
über den Block erstellt.

Wenn nun der erste Block (oder Daten im Block) geändert wird, ändert sich automatisch
auch der zweite Block.
In einer Blockchain ist es nicht möglich, Daten in einem Block zu verändern, ohne
**alle** Blöcke danach zu verändern.

[ER] Wechseln Sie in ihr Arbeitsverzeichnis und erstellen Sie dort einen neuen Ordner
`blockchain_example`.
*Die Dateien sind nicht für die Abgabe relevant.*

[ER] Initialisieren Sie ein neues git Repo und erstellen Sie eine Datei `Block1.txt`
mit beliebigem Inhalt. Erstellen Sie einen Commit mit der Nachricht `Block1`.

[ER] Wiederholen Sie dies mit einer zweiten Datei `Block2.txt` und erzeugen
Sie erneut einen Commit mit der Nachricht `Block1`.

[EC] Geben Sie das Ergebnis von `git --no-pager log --oneline` aus.
Sie sehen nun zwei Commits und die dazugehörigen Hashwerte.

[ER] Nutzen Sie `git rebase -i --root`, um im ersten Commit `Block1` etwas Neues
in die Datei zu schreiben.
Der zweite Commit `Block2` soll unverändert übernommen werden.

[EC] Geben Sie das Ergebnis von `git --no-pager log --oneline` erneut aus.

Sie können nun sehen, dass sich beide Commit-Hashs verändert haben, obwohl Sie nur
den ersten Commit bearbeitet haben.
Dies liegt an dem oben beschriebenen Prinzip.
Git verknüpft die Commits miteinander.
Wenn ein Commit bearbeitet wird, ändern sich alle Nachfolger auch.


### Programmaufbau

Obwohl Bitcoin und auch git als verteilte Systeme angelegt wurden, wird Sedricoin
zuerst als Client-Server-Architektur entwickeln.

[ER] Legen Sie ein neues Python Package `sedricoin` mit den Modulen `miner`, `models` und `server`
auf oberster Ebene in Ihrem Arbeitsverzeichnis an.
Sie werden innerhalb dieses Projekts die einzelnen Module weiterentwickeln.
Sie müssen für die folgenden Aufgaben daher nur *Dateilisten-Dateien* abgeben.

Das Modul `server` wird die gesamte Server Logik enthalten.
Das Modul `models` wird die einzelnen Datenklassen/Datenmodelle enthalten.
Dadurch können diese sowohl vom Client als auch vom Server verwendet werden.
Das Modul `miner` wird die Client Logik enthalten.


### Sedricoin Server

[ER] Erstellen Sie eine neue FastAPI Anwendung im Modul `server`, die die gegebene
OpenAPI Spezifikation implementiert.
Als Funktionskörper der Endpunkte können Sie vorerst `pass` angeben.
Die Logik in den einzelnen Endpunkte wird später ergänzt.
**Achten Sie bei den Modellen auf die korrekte Reihenfolge der Attribute.**


[FOLDOUT::OpenAPI Spezifikation für `Sedricoin-Start`]
Sie können beispielsweise den [Swagger-Editor](https://editor.swagger.io/) nutzen,
um die Spezifikation in der gewohnten Oberfläche zu lesen.
```
[INCLUDE::_include/openapi-sedricoin-start.json]
```
[ENDFOLDOUT]

[NOTICE]
Das Schema `Block` taucht in der OpenAPI Dokumentation zweimal auf, da es als Rückgabewert
eines GET Endpunkts und als Input für den `POST` Endpunkt verwendet wird.
Sie müssen im Code nur ein Modell anlegen und können dieses für Beides verwenden.
[ENDNOTICE]

Genau wie in Bitcoin wird auch in Sedricoin ein Block aus einem Block-Header und Daten
zusammengesetzt.
Vorerst fehlen die Daten, diese werden erst in der nächsten Aufgabe ergänzt.
Der Block-Hash muss nur über den Block-Header erzeugt werden.

[ER] Ergänzen Sie daher in ihrer `BlockHeader` Klasse die Methode `get_hash() -> str`.
Diese soll nur die **Werte** der Attribute aneinanderreihen und darüber
den `SHA256` Hash berechnen.
Schreiben Sie die Funktion so, dass sie ohne Änderungen funktioniert,
wenn später noch weitere Attribute der Klasse hinzugefügt werden.

Außerdem muss ein persistenter Speicher eingerichtet werden, damit die Blockchain
Neustarts des Servers überlebt.
Die Blockchain soll dabei in Ihrem Dateisystem gespeichert werden.
Die einzelnen Blöcke werden als JSON-Datei gespeichert.
Das Verzeichnis (im Code nur noch `repo` genannt) soll dabei die folgende Struktur haben:

```txt
blockchain/
└── block/
    ├── 0.json
    └── 1.json
```

Der 0-te Block, der sogenannte `Genesis-Block`, ist der erste Block in einer Blockchain.
Dieser ist insofern besonders, da er keinen Vorgänger hat, auf den referenziert werden kann.
In Bitcoin und vielen anderen Blockchains wird er deswegen explizit in den Code geschrieben
und nicht generiert.

Setzen Sie dies nun in Sedricoin um.
Nutzen Sie daher diesen Genesis Block an der notwendigen Stelle.

```json
{
  "header": {
    "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
    "timestamp": 1762265364,
  },
}
```

[ER] Kopieren Sie den folgenden Code Block in Ihr `server` Modul und implementieren
Sie die Funktion der Hilfsfunktionen, wie im Kommentar jeweils beschrieben wird.

[NOTICE]
Die Funktionen werden in dieser Reihenfolge implementiert, da sie sich untereinander
aufrufen.
Dementsprechend wird `init_repo()` zuletzt implementiert.
[ENDNOTICE]

```python
import os
from pathlib import Path


REPO: Path = Path(os.path.dirname(__file__)) / "blockchain"
block_head: int = 0 # index zum neuesten block der blockchain

def get_block_path(index: int) -> Path:
    """
    Gibt den korrekten Datei Pfad zum Block Index zurück.
    Der Pfad soll lediglich zusammengesetzt werden, es wird nicht geprüft, ob
    die Datei existiert.
    """

def get_block(index: int) -> Block | None:
    """
    Prüft, ob die entsprechende Block Datei im repo existiert,
    parsed die Datei und gibt das Block Model zurück.
    Wenn der Block nicht existiert, soll None zurückgegeben werden, ohne dass ein
    Fehler geworfen wird.
    """
 
def write_block(data: Block) -> None:
    """
    Schreibt einen neuen Block an das Ende der Blockchain im repo.
    Dadurch ändert sich die globale Variable block_head.
    Der Block ist bereits gültig.
    """

def init_repo() -> None:
    """
    Prüft, ob das Repo im Dateisystem bereits existiert.
    Falls nicht, werden die Ordner entsprechend angelegt und der Genesis-Block wird geschrieben.
    Außerdem wird hier der block_head aktualisiert.
    Am Ende der Funktion soll weiterhin das vorhandene print-Statement stehen.
    """

    print(f"repo initialisiert HEAD: {block_head}")
```

[ER] Lesen Sie in der
[FastAPI Dokumentation](https://fastapi.tiangolo.com/advanced/events/#lifespan)
den Abschnitt `Lifespan`, und ergänzen Sie Ihren Server, sodass `init_repo()` aufgerufen wird,
bevor die API gestartet wird.


[ER] Ergänzen Sie nun die Funktionskörper der einzelnen Endpunkte, sodass die Endpunkte
die in der Spezifikation beschriebene Funktion erfüllen.


### Sedricoin Client

[ER] Implementieren Sie in Ihrem Modul `miner.py` die folgende Client Logik.

```python
API_UR = "http://localhost:8000"

def fetch_newest_block() -> Block:
    """
    Lädt den neuesten Block von der API herunter.
    """

def create_new_block() -> Block:
    """
    Erstellt einen neuen Nachfolger zum neuesten Block und lädt diesen in der API hoch.
    """

if __name__ == "__main__":
    create_new_block()
```



[EC] Starten Sie Ihren Server Ihren Server vollständig neu und geben Sie am Ende
das Log des Servers ab.
Führen Sie nun in einer weiteren Konsole Ihr `client.py` Modul genau ein Mal aus.

[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Codedurchsicht]


[ENDINSTRUCTOR]
