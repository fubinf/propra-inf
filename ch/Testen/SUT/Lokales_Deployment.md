title: Lokale Bereitstellung des System unter Test
stage: draft
timevalue: 1.0
difficulty: 1
profiles:
explains:
assumes:
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
Sollte das Verzeichnis nicht existieren, könne Sie es mir dem folgenden Befehl anlegen: `mkdir ~/ws/sut`.
Jetzt beschaffen wir uns den Quellcode mit `git clone https://github.com/fubinf/propra-inf-testobjekt.git`.
[WARNING]
Achten Sie darauf, dass Sie sich **im** Verzeichnis *sut* befinden und nach dem pullen nicht die Überraschung entdecken, dass sich
Ihr Repo auf einmal wo anders befindet.
[ENDWARNING]
- [EQ] Wie heißt das erstellte Verzeichnis unter `~/ws/sut/`?

### Requirements erfüllen

### Anwendung starten

### Anwendung aufrufen


[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::...]

.

[ENDSECTION]

[INSTRUCTOR::heading]
- [EREFC::1] Nach diesen Schitten sollte das folgende Verzeichnis `propra-inf-testobjekt` unter `~/ws/sut/` gefunden worden sein.
[ENDINSTRUCTOR]
