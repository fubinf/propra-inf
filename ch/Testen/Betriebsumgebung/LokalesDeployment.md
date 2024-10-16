title: Lokale Bereitstellung des System unter Test
stage: alpha
timevalue: 1
difficulty: 1
explains: SUT
assumes: venv, pip, Shell-Grundlagen, Git101, apt
---

[SECTION::goal::idea]

- Ich kann das SUT lokal starten und verwenden.

[ENDSECTION]
[SECTION::background::default]

Das SUT ist eine einfache Webanwendung, die eigens zu dem Zweck des ProPra für die
Testautomatisierung entwickelt wurde. Diese Webanwendung ist darauf ausgerichtet, nur geringe
Vorbedingungen für die Bereitstellung zu erfordern und fungiert gleichzeitig als praktisches
Beispiel für eine gut zu testende Webanwendung.

[ENDSECTION]
[SECTION::instructions::detailed]

### Warum benutze ich das SUT?

Es werden Aufgaben zur Verfügung stehen, die eine besondere Grundlage benötigen, um korrekt gelöst
werden zu können. Primär ist das SUT für den Bereich TEST vorgesehen, kann auch auch für alle
anderen Bereiche der Softwareentwicklung verwendet werden, um z.B. die Webentwicklung im Front- und
Backend zu erkunden, oder sich mit der Bereitstellung (Deployment) von Anwendungen zu befassen.
In jedem Fall wird es ein Hinweis geben, der sich auf diese Grundlagen bezieht.

Natürlich können Sie auch jederzeit explorativ das SUT erkunden, verbessern oder erweitern. Sollten
Ihnen merkwürdige Verhaltensmuster an der Software auffallen, können Sie ebenfalls die Gelegenheit
nutzen dies in GitHub als Issue kenntlich zu machen und so an der Entwicklung teilnehmen.

<replacement id=SUTCopyRepoLink>
Verschaffen Sie sich einen Überblick über den Entwicklungsstand, welchen Sie im
[GitHub Repository](https://github.com/fubinf/propra-inf-testobjekt) finden.
</replacement>

- [EQ] Welche Versionen befinden sich im Repository?

### Repository pullen

Starten Sie ein eine neue Terminal Session. Wir wollen unser SUT gleich strukturiert ablegen.

- Legen Sie dazu ein neues Verzeichnis an: `mkdir ~/ws/sut`.
- Navigieren Sie anschließend in dieses Verzeichnis: `cd ~/ws/sut`.
- Jetzt beschaffen wir uns den Quellcode mit `git clone https://github.com/fubinf/propra-inf-testobjekt.git`.

- [EQ] Wie heißt das erstellte Verzeichnis unter `~/ws/sut/`?

[WARNING]
Achten Sie darauf, dass Sie sich **im** Verzeichnis *sut* befinden und nach dem pullen nicht die
Überraschung entdecken, dass sich Ihr Repo auf einmal wo anders befindet.
[ENDWARNING]

### Anforderungen erfüllen

Bevor wir die Anwendung starten können, benötigen wir die für diese Webanwendung genutzten
Entwicklungsvorbedingungen. Da dieser Webauftritt ein Python Projekt ist, wird als aller erstes
Python benötigt.

- [EC] Aktualisieren Sie, falls notwendig, auf Python Version 3.11

Wenn Sie mit mehreren Python Projekten arbeiten, werden Sie auch auf unterschiedliche Vorbedingen
oder Abhängigkeiten treffen. Daher bietet es sich an diese Projekte in unterschiedlichen Umgebungen
mit Hilfe von [TERMREF::venv] zu verwenden. Tiefer gehende Informationen finden Sie im Kapitel
[PARTREF::venv].

- [EQ] Wie setzt sich Ihr [TERMREF::Prompt] zusammen?

[HINT:: VENV einrichten]

- Zu erst wechseln wir in das vom GitHub gepullte Verzeichnis mit dem Kommando `cd`. Hier
  müssen Sie noch das aus [EREFQ::1] erkannte Verzeichnis ergänzen.
- Installieren Sie in Ihrem Verzeichnis eine neue Virtuelle Umgebung mit: `python -m venv ./sut`
- Wechseln sie in diese Virtuelle Umgebung: `source ./sut/bin/active`

[ENDHINT]

Neben der Entwicklungssprache Python werden auch weitere [TERMREF::Framework]s verwendet, um diese
Seite zu realisieren. Diese Erweiterungen werden in einer einzelnen Datei dokumentiert. Diese
finden Sie standardmäßig im Stammverzeichnis unter `requirements.txt`. Mit dieser Datei haben Sie
die Möglichkeit Abhängigkeiten schnell und unkompliziert zu installieren.

Da das SUT aus unterschiedlichen Versionen besteht, müssen wir uns für eins entscheiden (bzw. wird
ihnen die Version in der jeweiligen Aufgabe nahegelegt).

- [EC] Wechseln Sie in das vorgesehene Verzeichnis mit der angegebenen Versionsnummer (hier
  exemplarisch v1.0.0)
- [EC] Anschließend installieren Sie einmalig die hinterlegten Abhängigkeiten über die Datei
  `requirements.txt`

[WARNING]
Da Sie die Virtuelle Umgebung `sut` verwenden, sind die installierten Abhängigkeiten nur für diese
Umgebung gültig. Wechseln Sie in eine andere Umgebung, die diese Abhängigkeiten nicht installiert
hat, wird beim folgenden Ausführen eine Fehlermeldung auftauchen.
[ENDWARNING]

### Anwendung starten

Jetzt haben wir alles, was wir zum Starten benötigen. Jedoch wir müssen unsere Anwendung noch zum
Laufen bringen. Das realisieren wir mit dem folgenden Kommando:

- [EC] Starten Sie die Anwendung mit Python, indem Sie die Hauptdatei aufrufen.

[HINT::Datei nicht gefunden]
Sollte die Datei nicht gefunden werden, müssen die den Pfad anpassen oder ins Verzeichnis der
vorgeschriebenen Version wechseln.
[ENDHINT]

Jetzt läuft im Hintergrund die bereitgestellte Webanwendung. Diese wartet auf Interaktionen auf der
lokalen Schnittstelle 127.0.0.1 über den Port 5000.

[WARNING]
In unserem Fall muss das Terminalfenster, aus dem wir unsere Anwendung gestartet haben, geöffnet
bleiben, um damit arbeiten zu können.
[ENDWARNING]

[HINT::Anwendung beenden]
In Ihrer geöffneten Terminalsitzung läuft die Anwendung im Vordergrund mit. Um diese zu beenden,
drücken Sie die Tastenkombination `Control + C`, oder schließen das Terminalfenster.
[ENDHINT]

### Anwendung aufrufen

Um mit der Webanwednung zu interagieren zu können, benötigen Sie ein Browserfenster.

- Rufen Sie im Browser die folgende Seite auf: `http://127.0.0.1:5000`

Wenn Sie jetzt eine Webseite sehen, hat alles funktioniert.

Natürlich werden Sie in die Versuchung kommen, Änderungen am Code vorzunehmen, indem Sie Anpassungen
vornehmen, Dinge Löschen oder Hinzufügen.

- [EQ] Welche Auswirkung hat eine Änderung auf das GitHub Repository?

Win diesem Task geht es darum, das SUT lokal zu starten und eine Änderung nicht online zur Verfügung
zu stellen. Doch ..

- [EQ] Warum arbeiten wir lokal und nicht permanent mit eine online bereitgestellten Version?

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::heading]

- [EREFQ::1] Versionen v1.0.0, v1.1.0 und v3.0.0, wobei v1.0.0 Code enthält.
- [EREFQ::2] Nach diesen Schritten sollte das folgende Verzeichnis `propra-inf-testobjekt` unter
  `~/ws/sut/` gefunden worden sein.
- [EREFC::1] `apt install python3.11` könnte eine Lösung sein.
- [EREFQ::3] Hier soll kenntlich gemacht werden, dass die venv im Prompt angezeigt wird. Wenn
  der Hinweis befolgt wird, sollte folgendes erscheinen: **(sut)**
- [EREFC::2] `cd v1.0.0`
- [EREFC::3] `pip install -r requirements.txt`
- [EREFC::4] `python3 app.py`
- [EREFQ::4] Gar keine, da alle Änderungen lediglich lokal geschehen und GitHub gar nichts davon
  mitbekommt, so fern man keine Commits pushed.
- [EREFQ::5] Die wesentlichsten Vorteile sind:
  - Schneller Zugriff auf ein laufendes SUT
  - Debugging Möglichkeit
  - Zum Testen immer ein SUT mit ein und dem selben Zustand (Testdaten)
  - unabhängig und flexibel mit der Anwendung

[ENDINSTRUCTOR]
