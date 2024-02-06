title: Lokale Bereitstellung des System unter Test
stage: draft
timevalue: 1.0
difficulty: 1
profiles: TEST
explains:
assumes: venv, pip
requires:
---
[SECTION::goal::product]

- Ich besitze erste Kenntnisse über das System unter Test
- Ich besitze die technscihen Voraussetzungemn dafür, das System unter Test lokal zu starten und zu verwenden

[ENDSECTION]
[SECTION::background::default]

### Was ist das SUT?

"System under Test" (SUT) ist ein Begriff, der in der Softwareentwicklung und im Bereich der Softwaretests verwendet wird.
Wenn wir sagen, dass ein bestimmtes System das "System under Test" ist, meinen wir, dass dieses System gerade den Fokus von
Tests und Überprüfungen bildet. Das können verschiedene Arten von Tests sein, wie zum Beispiel Funktionstests, Leistungstests
oder Sicherheitstests.

In der Praxis könnte das SUT beispielsweise eine Webanwendung, eine mobile App, ein Datenbankmanagementsystem oder ein
beliebiges Softwareprodukt sein, das entwickelt wurde und nun darauf überprüft wird, ob es den Anforderungen entspricht und
wie gut es funktioniert. In unserem Fall ist es eine einfache Webanwednung, die eigens zu diesem Zweck des Lernens im Umgang
mit der Testautomatisierung entwickelt wurde. Diese Webanwendung ist darauf ausgerichtet, nur geringe Vorbedingungen für die
Bereitstellung zu erfordern und fungiert gleichzeitig als praktisches Beispiel für eine gut testbare Webanwendung.

<replacement id=SUTCopyRepoLink>
Das SUT gibt es in mehreren Versionen, die unterschiedliche Änderungen und somit Ziele abdecken. Einen genaue Überblick gibt es
im [GitHub Repository](https://github.com/fubinf/propra-inf-testobjekt).
</replacement>

### Wann benutze ich das SUT?

Es werden Aufgaben zur Verfügung stehen, die eine besondere Grundlage benötigen, um korrekt gelöst werden zu können. Primär ist
das SUT für den Bereich TEST vorgesehen, kann auch auch für alle anderen Bereiche der Softwareentwicklung verwendet werden,
um z.B. die Webentwicklung im Front- und Backend zu erkunden, oder sich mit dem Bereitstellung von Anwendungen zu befassen.
In jedem Fall wird es ein Hinweis geben, der sich auf diese Grunlagen bezieht.

Natürlich können Sie auch jederzeit explorativ das SUT erkunden, verbessern oder erweitern. Sollten Ihnen merkwürdige Verhaltensmuster
an der Software auffallen, können Sie ebenfalls die Gelegenheit nutzen dies in GitHub als Issue kenntlich zu machen und so an der
Entwicklung teilnehmen.

### Wie benutze ich das SUT?

Im folgenden werden wir Schritt für Schritt das SUT auf Ihrem lokalen System zum Laufen bringen. Alles was Sie dafür benötigen,
ist eine Portion Motivation, Geduld und Bereitschaft zum Lernen. Vorblickend werden wir folgende Schritte durchführen:

- Den aktuellen Codestand bekommen
- Vorbedingugen erfüllen
- lokalen Dienst starten
- Webanwendung aufrufen

[ENDSECTION]
[SECTION::instructions::detailed]

### Repo pullen

Starten Sie ein eine neue Terminal Session.
Wir wollen unser SUT gleich strukturiert ablegen und navigieren in folgendes Verzeichnis: `cd ~/ws/sut`.
Sollte das Verzeichnis nicht existieren, könne Sie es mit dem folgenden Befehl anlegen: `mkdir ~/ws/sut`.
Jetzt beschaffen wir uns den Quellcode mit `git clone https://github.com/fubinf/propra-inf-testobjekt.git`.
[WARNING]
Achten Sie darauf, dass Sie sich **im** Verzeichnis *sut* befinden und nach dem pullen nicht die Überraschung entdecken, dass sich
Ihr Repo auf einmal wo anders befindet.
[ENDWARNING]

- [EQ] Wie heißt das erstellte Verzeichnis unter `~/ws/sut/`?

### Requirements erfüllen

Bevor wir die Anwendung starten können, benötigen wir die für diese Webanwendung genutzten Entwicklungsvorbedingungen. Da
dieser Webauftritt ein Python Projekt ist, wird als aller erstes Python benötigt. Sie installieren Python mit `apt-get install python`

- [EQ] Welche Pythonversion wird ihnen angezeigt?

Wenn Sie mit mehreren Pythonprojekten arbeiten, werden Sie auch auf unterschiedliche Vorbedingen oder Abhängigkeiten treffen. Daber bietet
es sich an diese Projekte in unterschiedlichen Umgebungen zu verwenden. Tiefergehende Informationen finden Sie im Kapitel **venv.md**.

- [EC] Installieren Sie in Ihrem Verzeichnis eine neue Virtuelle Python-Umgebung mit `python -m venv ./sut`
- [EC] Wechseln sie, wenn noch nicht geschehen, in diese Umgebung: `source ./sut/bin/active`
- [EQ] Wie setzt sich Ihr [TERMREF::Prompt] zusammen?

Neben der Entwicklungssprache Python werden auch weitere Open-Source Pakete / Frameworks verwendet, um diese Seite zu realisieren. Diese
Erweiterungen werden in einer einzelnen Datei dokuemtniert. Diese finden Sie standardmäßig im Stammverzeichnis unter **requirements.txt**.
Diese Datei ermöglicht es uns die Abhängigkeiten schnell und unkompliziert zu installieren.

- [ER] Zu erst wechseln wir in das vom GitHub gepullte Verzeichnis mit dem Kommando `cd`. Hier müssen Sie noch das aus [EREFQ::1] erkannte
  Verzeichnis ergänzen

Da das SUT aus unterschiedlichen Versionen besteht, müssen wir uns für eins entscheiden (bzw. wird ihnen die Version in der jeweiligen
Aufgabe nahegelegt). wechselen Sie in das vorgesehene Verzueichnis mit der angegebenen Versionsnummer (hier examplarisch v1.0.0)

- [EC] `cd v1.0.0`
- [EC] Jetzt installieren Sie einmalig die hinterlegten Abhängigkeiten mit `pip install -r requirements.txt`

### Anwendung starten

Jetzt haben wir alles, was wir zum Starten benötigen. Aber wir müssen unsere Anwendung noch zum Laufen bringen. Das realisieren wir wie folgt:

- [EC] Starten Sie die Anwendung mit `python app.py`

Jetzt läuft im Hintergrund die bereiztgestellte Webanwendung. Diese wartet auf Interaktionen auf der lokalen Schnittstelle 127.0.0.1 über
den Port 5000.

[WARNING]
In unserem Fall muss das Terminalfenster, aus dem wir unsere Anwendung gestartet haben, geöffnet bleiben, um damit arbeiten zu können.
[ENDWARNING]

[HINT::Anwednung beenden]
In Ihrer geöffneten Terminalsitzung läuft die Anwendung im Vordergrund mit. Um diese zu beenden, drücken Sie die Tastenkombination
`Control + C`, oder schließen das Terminalfenster.
[ENDHINT]

### Anwendung aufrufen

Jetzt müssen wir nur noch damit interagieren. Öffnen Sie ein Browserfenster.

- [EC] Rufen Sie im Browser die folgende Seite auf: `http://127.0.0.1:5000`

Wenn Sie jetzt eine Webseite sehen, hat alles funktioniert.

[SECTION::submission::trace]
[INCLUDE::../../_include/Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::heading]

- [EREFQ::1] Nach diesen Schitten sollte das folgende Verzeichnis `propra-inf-testobjekt` unter `~/ws/sut/` gefunden worden sein.
- [EREFQ::2] Hier soll kenntlich gemact werden, dass die venv im Prompt angezeiugt wird: **(sut)**

[ENDINSTRUCTOR]
