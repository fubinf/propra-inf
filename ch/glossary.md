title: Begriffsverzeichnis
---

Auf dieser Seite werden wichtige Begriffe erläutert; 
insbesondere solche, die für mehr als eine Aufgabe relevant sind.

Die Erläuterungen verweisen zurück auf die Aufgaben, in denen sie erwähnt werden,
sowie ggf. auf Aufgaben, die weitere Erläuterungen dazu enthalten. 


## A

[TERM::Akzeptanzkriterien]
Akzeptanzkriterien sind spezifische, messbare Bedingungen, die definieren, wann eine User Story oder eine Funktion als abgeschlossen und akzeptiert betrachtet wird. Sie legen die Erwartungen und Anforderungen fest, die erfüllt sein müssen, damit das Produkt oder die Funktion als erfolgreich betrachtet wird. Akzeptanzkriterien dienen dazu, Missverständnisse zu vermeiden, indem sie klare Richtlinien für die Entwicklung und das Testen geben.
[ENDTERM]

[TERM::apt|apt-get|Debian-Paketmanager]
Das Hilfsprogramm bei Debian (und von Debian abgeleiteten Systemen wie Ubuntu oder Mint),
das die Paketinstallationen auf einem Debian-System durchführt und überwacht.

Es kennt die Abhängigkeiten zwischen Paketen und sorgt automatisch dafür, dass
bei Installation von Paket A auch die davon benötigten Pakete B und C installiert werden,
sowie die von B benötigten Pakete B1, B2, B3 usw.

Beim Deinstallieren von A werden alle diese auch wieder mit abgeräumt -- es sei denn,
z.B. B2 würde auch noch von einem anderen installierten Paket benötigt
oder sei manuell installiert worden: dann bleibt es da.
[ENDTERM]

[TERM::Argument]
Der konkrete Wert, den man an einen [TERMREF::Parameter] übergibt, 
z.B. in Form einer konkreten Variable.
[ENDTERM]

[TERM::API]
Eine API (Application Programming Interface) ist eine Schnittstelle,
die es verschiedenen Softwareanwendungen ermöglicht, miteinander zu kommunizieren und
Daten auszutauschen. Sie definiert die Regeln und Protokolle, nach denen Programme
miteinander interagieren können.
[ENDTERM]


## B

[TERM::Bash|.bashrc]
Die meistbenutzte [TERMREF::Shell] auf Linux-Systemen.

Kommandos zur Initialisierung der Shell stehen in der Datei `.bashrc` im HOME-Verzeichnis
(das stimmt nur ungefähr, etwas genauer steht es in 
https://linuxize.com/post/bashrc-vs-bash-profile/).
Richtig genau steht es in der Dokumentation von Bash.
[ENDTERM]

[TERM::BDD]
Behavior Driven Development (BDD) ist eine agile Softwareentwicklungsmethode, die sich auf die Zusammenarbeit
zwischen Entwicklern, Testern und nicht-technischen Stakeholdern konzentriert. In BDD werden Anforderungen
in verständlichen, natürlichsprachlichen Szenarien formuliert, die als "Gherkin"-Syntax bekannt sind. 

https://docs.robotframework.org/docs/testcase_styles/bdd#what-is-bdd
https://www.codecentric.de/wissens-hub/blog/givenwhenthen-and-example-tables-using-the-robot-framework
[ENDTERM]

[TERM::Bibliothek|Library]
Eine Sammlung von Programmelementen (z.B. Klassen, Funktionen, Datentypen, Module, Pakete)
ohne Hauptprogramm; 
dazu bestimmt, von anderen Programmen oder anderen Bibliotheken benutzt zu werden.

Bibliotheken erlauben es, Programme weitgehend aus vorhandenen Bausteinen zusammenzusetzen
und nur noch wenig Code selbst schreiben zu müssen.
Sie sind das wirksamste Mittel für hohe Produktivität bei der Softwareentwicklung.
[ENDTERM]


## C


## D

[TERM::Default|Defaultwert|Default-Argument]
Ein [TERMREF::Argument] zur Übergabe an einen [TERMREF::Parameter],
das implizit benutzt wird, wenn man nicht selbst explizit ein Argument übergibt. 
[ENDTERM]

[TERM::Defekt|Defect|Fault]
Ein Defekt (engl. _defect, fault_) verursacht ein Versagen.
Häufig wird das Wort Bug synonym benutzt.
Dies ist eine strukturelle Eigenschaft des Codes und kann damit auch nur in diesem behoben werden.
[ENDTERM]

[TERM::DSL]
Eine DSL (domänenspezifische Sprache) ist eine speziell auf eine bestimmte Problemstellung
oder Domäne zugeschnittene Sprache. Im Gegensatz zu allgemeinen Programmiersprachen, die
für eine Vielzahl von Anwendungen geeignet sind, ist eine DSL darauf ausgerichtet, spezifische
Aufgaben oder Anforderungen in einem begrenzten Kontext zu adressieren.
[ENDTERM]

[TERM::Dynamische analytische Qualitätssicherung]
Die dynamische analytische Qualitätssicherung bezieht sich auf den Prozess der Überprüfung der Softwarequalität durch das Testen der Software während ihrer Ausführung. Dies umfasst verschiedene Testmethoden wie unit tests, Integrationstests, Systemtests und Leistungstests, um sicherzustellen, dass die Software die erwarteten Anforderungen erfüllt und ordnungsgemäß funktioniert. 
[ENDTERM]

## E

[TERM::Executable|ausführbare Datei]
Eine Datei, deren "executable"-Bit gesetzt ist (mit dem Kommando `chmod`)
und die entweder Maschinencode enthält
oder mit einer [TERMREF::Shebang-Zeile] beginnt.
[ENDTERM]

## F

[TERM::Fehler|Error]
Ein Fehler (engl. _error_) führt zum Defekt. 
Es liegt ein falsches Verhalten (engl. _commission_) oder ein Versäumnis (engl. _omission_) vor.
Damit entsteht ein Fehler immer während der Entwicklung, entweder im Code, bei den 
Anforderungen oder beim Entwurf.
[ENDTERM]

[TERM::Rahmenwerk|Framework]
Ein Rahmenwerk (Framework) ist eine [TERMREF::Bibliothek]
(oder ein direkt lauffähiges Programm),
die nicht hauptsächlich von der Benutzer_in aufgerufen wird,
sondern bei der die Benutzer_in eigene Programmteile registriert,
die dann anschließend durch das Rahmenwerk aufgerufen werden.

Dieses Funktionsprinzip ist bekannt als Kontrollumkehr (inversion of control)
oder Hollywood-Prinzip: _"Don't call us, we'll call you"_.
[ENDTERM]


## G

[TERM::Globbing]
Globbing bezeichnet die Expansion von Dateinamensmustern in eine Liste von Dateinamen.
Dabei wird insbesondere das Zeichen `*` als Platzhalter für irgendeinen Dateinamens-Teil interpretiert,
sodass sich z.B. mittels `*.txt` alle Dateien mit dem Suffix `.txt` (im selben Verzeichnis)
zugleich ansprechen lassen.

Globbing ist insbesondere in allen gängigen [TERMREF2::Shell::-s] implementiert.

Kurzerläuterung: [https://tldp.org/LDP/abs/html/globbingref.html](https://tldp.org/LDP/abs/html/globbingref.html)
[ENDTERM]


## H

[TERM::HTTP]
HTTP steht für "Hypertext Transfer Protocol" und ist ein Protokoll, das für die
Übertragung von Daten über das World Wide Web verwendet wird. Es bildet die Grundlage
für den Datenaustausch zwischen Webbrowsern und Webservern. HTTP ermöglicht die Kommunikation
zwischen Client-Anwendungen (zum Beispiel Webbrowsern) und Servern, auf denen Webseiten und
andere Ressourcen gehostet werden.
[ENDTERM]

## I
## J

[TERM::JSON]
JSON (JavaScript Object Notation) ist ein leichtgewichtiges Datenaustauschformat,
das für den menschenlesbaren und einfachen Datenaustausch zwischen verschiedenen
Programmiersprachen konzipiert ist. Es basiert auf einer Untermenge der
JavaScript-Programmiersprache, jedoch kann JSON von vielen anderen Sprachen
unterstützt und interpretiert werden.
[ENDTERM]

## K

[TERM::Kommandozeilenparameter]
Ein [TERMREF::Parameter] für ein ausführbares Programm, das per 
[TERMREF::Shell]-Kommando aufgerufen wird, 
oder für ein eingebautes Shell-Kommando 
[ENDTERM]

[TERM::KDT]
Schlüsselwortgetriebenes Testen (Keyword-Driven Testing; Schlüsselwortgetriebenes Testen)
ist eine Testautomatisierungsmethode, bei der Tests mithilfe von Schlüsselwörtern oder
Aktionen beschrieben werden, die von einem Testframework interpretiert und ausgeführt werden. 

https://de.wikipedia.org/wiki/Keyword-Driven_Testing
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates
[ENDTERM]


## L

[TERM::Linux|GNU/Linux]
Eine Familie von Open-Source-Betriebssystem-Distributionen, die auf dem Linux-Betriebssystemkern aufbauen
sowie auf einem umfangreichen Universum von Softwarepaketen.

https://de.wikipedia.org/wiki/Linux
[ENDTERM]

## M
## N
## O

[TERM::OpenAPI]
Früher als Swagger Specification bekannt, ist ein Standard, der die Dokumentation
von RESTful APIs (Representational State Transfer) erleichtert. Es handelt sich um
eine maschinenlesbare Beschreibung einer API, die Entwicklern ermöglicht, schnell
zu verstehen, wie die API funktioniert, welche Ressourcen verfügbar sind, welche
Parameter erwartet werden und welche Antworten zurückgegeben werden können.
[ENDTERM]


## P

[TERM::Parameter]
Ein Platzhalter für ein [TERMREF::Argument], das man an etwas parametrisiertes übergeben kann.
Funktionen und Methoden haben in Python sehr oft ein oder mehrere Parameter.
In manchen Sprachen können auch andere Dinge parametrisiert sein, z.B. Klassen,
Makros, Module oder Pakete.
[ENDTERM]

[TERM::PATH]
Eine [TERMREF::Umgebungsvariable], die eine Liste von Verzeichnispfaden enthält,
durch Doppelpunkte getrennt.
Wenn für ein Kommando auf der [TERMREF::Kommandozeile] ein 
[TERMREF::Executable] benötigt wird, wird es in jedem dieser Verzeichnisse gesucht.
Beispiel: `PATH=/bin:/usr/bin:~/bin`
[ENDTERM]

[TERM::pip]
"Package installer for Python":
Das Programm, mit dem man üblicherweise externe Bibliotheken von einem entsprechenden
Server ("package index", meist wird pypi.org benutzt) lädt und installiert.

Dokumentation: https://pip.pypa.io/en/stable/getting-started/
[ENDTERM]

[TERM::Prompt]
Die Prompt ist eine Textzeichenfolge, die in der Kommandozeile angezeigt wird, um den
Benutzer zur Eingabe von Befehlen zu ermutigen. Sie enthält oft Informationen wie den
Benutzernamen, den Hostnamen, den aktuellen Pfad und möglicherweise andere relevante Informationen.

Bsp: student1@propra_pc:#$
[ENDTERM]

## Q

[TERM::Qualitätssicherung|QS]
Qualitätssicherung (QS) bezeichnet den Prozess, durch den sicherzustellen versucht wird, dass ein Produkt oder
eine Dienstleistung die festgelegten Qualitätsstandards erfüllt oder übertrifft. Dieser Prozess umfasst
verschiedene Aktivitäten wie Planung, Kontrolle, Überprüfung und Verbesserung, die darauf abzielen, Fehler zu
minimieren und die Kundenzufriedenheit zu maximieren.
Zusätzlich unterscheiden wir zwischen den zwei Bereichen [TERMREF::Dynamische analytische Qualitätssicherung] und
[TERMREF::Statische analytische Qualitätssicherung].
[ENDTERM]

## R

[TERM::RPA]
RPA (Robotic Process Automationdeutsch; Robotergesteuerte Prozessautomatisierung) bezieht sich 
auf die Anwendung von Software-Robotern oder "Bots", um menschenähnliche Aufgaben in Geschäftsprozessen
zu automatisieren. Diese Roboter agieren in der Regel auf der Benutzeroberfläche von Anwendungen,
indem sie Aktionen ausführen, Daten erfassen, Entscheidungen treffen und mit anderen Systemen
interagieren, ähnlich wie es ein menschlicher Bediener tun würde.
[ENDTERM]

## S

[TERM::Shebang|Shebang-Zeile]
Ein Mechanismus auf Unix-Systemen, der aus einer Datei, die Programmcode für eine interpretierte
Sprache enthält, eine ausführbare Datei macht:
Die erste Zeile der Datei hat das Format `#!/call/to/interpreter`, also beispielsweise
`#!/usr/bin/python` oder `#!/bin/env python`.

Steht dies z.B. in der Datei `a.py` und diese wird ausgeführt, so ist die Wirkung
ungefähr so wie beim Kommando `/usr/bin/python a.py`.
Der Rest der Datei `a.py` enthält also (hoffentlich) Python-Quellcode und das Verfahren ist
für alle Sprachen anwendbar, bei denen ein `#` am Zeilenanfang einen Kommentar anzeigt.
[ENDTERM]

[TERM::Shell|Unix-Shell|Linux-Shell|Kommandozeile]
Übliche Bezeichnung für die Kommandozeilen-Interpretierer auf [TERMREF2::Unix::--] oder [TERMREF2::Linux::--Systemen],
weil diese aus Sicht einer Benutzer_in wie eine "Schale" den Kern des Betriebssystems umhüllen.

https://de.wikipedia.org/wiki/Kommandozeile  
https://de.wikipedia.org/wiki/Unix-Shell
[ENDTERM]

[TERM::Statische analytische Qualitätssicherung]
Die statische analytische Qualitätssicherung bezieht sich auf den Prozess der Überprüfung von Softwareartefakten wie Code, Spezifikationen und Dokumentation, ohne dass die Software tatsächlich ausgeführt wird. Dabei werden Werkzeuge und Techniken wie Code-Reviews, statische Code-Analyse und formale Methoden eingesetzt, um potenzielle Fehler, Inkonsistenzen oder Verbesserungsmöglichkeiten frühzeitig zu identifizieren.
[ENDTERM]

## T

[TERM::Tutorial]
Ein kurzer Lehrgang (in der Regel in Schriftform, eventuell als Video)
zum Erlernen der Grundzüge eines klar abgegrenzten Themenbereichs,
meist der Benutzung einer Programmier- oder Kommandosprache,
einer [TERMREF::Bibliothek] oder eines [TERMREF2::Framework::-s].

Ein Tutorial führt den Lernende_n durch praktische Schritte,
die dieser selbst durchführen soll, um einen optimalen Lernerfolg zu erreichen.
Das ermöglicht zugleich, unterwegs direkt andere Varianten der Schritte auszuprobieren,
um das Lernpensum zu verbreitern.
[ENDTERM]


## U

[TERM::Umgebungsvariable|environment variable]
Ein Paar aus Name und Wert, das einem Prozess eines Unix-Betriebssystems zugeordnet ist
und an von diesem Prozess aus gestartete Unterprozesse weitergegeben wird und deshalb zur
Ausführungsumgebung beider Prozesse gezählt wird.

In der [TERMREF::Bash] kann man Umgebungsvariablen setzen, 
indem man das Kommando `export` benutzt
(Beispiel: `export HOME=/home/myusername`), 
und anzeigen mittels `echo`
(Beispiel: `echo $HOME`).
[ENDTERM]

[TERM::Unix|POSIX]
Eine große und lose Familie von Betriebssystemen, die auf unterschiedlichen Betriebssystemkernen aufbauen,
aber viele Grundkonzepte gemeinsam haben.

In einem weiteren Sinne des Wortes sind beiden wichtigsten Untergruppen 
die POSIX-kompatiblen Systeme und die [TERMREF::Linux]-Systeme.

Im engeren Sinne sind nur POSIX-Systeme Unix, 
alle anderen (inklusive Linux) werden dann meist "unixoid" genannt,
aber häufig spart man sich die Mühe dieser Unterscheidung einfach.

https://de.wikipedia.org/wiki/POSIX  
https://de.wikipedia.org/wiki/Unix
[ENDTERM]

[TERM::User Story]
Eine User Story ist eine kurze, informelle Beschreibung einer Funktion oder Anforderung aus der Perspektive eines Endbenutzers. Sie umfasst typischerweise wer die Funktion nutzt, was getan werden soll und warum es wichtig ist. User Stories dienen als Kommunikationsmittel zwischen Entwicklern, Kunden und anderen Stakeholdern, um Anforderungen klar zu definieren und das Verständnis zu verbessern. Oftmals werden zusätzlich [TERMREF:Akzeptanzkriterien] verwendet.
[ENDTERM]

## V

[TERM::venv|virtual environment]
Virtuelle Python-Umgebung:
Ein Dateibaum, der konzeptuell eine eigene Installation von Python enthält
sowie einen eigenen Unterdateibaum für installierte Pakete.

Wird ein `venv` aktiviert, was mittels `source myvenv/bin/activate` geschieht,
wird das Python-[TERMREF::Executable] des `venv` zuvorderst in den 
[TERMREF::PATH] geschrieben und benutzt dann die installierten Pakete des `venv`
anstatt (oder anstatt nur) der global installierten.

Der `venv`-Mechanismus erlaubt, für mehrere Python-Projekte, an denen man entwickelt,
separate Mengen installierter Pakete zu haben und bei Bedarf auch unterschiedliche Versionen
von Python selbst, sodass es insbesondere keine Probleme macht, falls verschiedene Projekte
das gleiche Paket X in unterschiedlichen Versionen benötigen.
[ENDTERM]

[TERM::Verifizierung]
Verifizierung oder Verifikation (von lateinisch veritas ‚Wahrheit' und facere ‚machen') ist
die Bestätigung durch Bereitstellung eines objektiven Nachweises, dass festgelegte
Anforderungen erfüllt worden sind.

https://glossary.istqb.org/de_DE/term/verifizierung
[ENDTERM]

[TERM::Versagen|Failure|Symptom]
Ein Versagen (engl. _failure_) ist das falsche Verhalten des Programms bezogen zur 
Spezifikation, der Anforderung oder den Erwartungen.
Da es genau dieses Phänomen ist, welches man bei einer Programmausführung bemerkt und zumeist 
nicht direkt auf die Ursache schließen kann, wird es in einigen Quellen auch 
Symptom (engl. _symptom_) genannt. 
[ENDTERM]

[TERM::Validierung]
Bestätigung durch Überprüfung, dass ein Arbeitsergebnis den Bedürfnissen eines Stakeholders entspricht.

https://glossary.istqb.org/de_DE/term/validierung-1
[ENDTERM]

## W
## X

[TERM::XML]
XML (eXtensible Markup Language) ist eine Auszeichnungssprache zur Darstellung
hierarchisch strukturierter Daten in einem menschenlesbaren Format. Entwickelt
wurde XML, um strukturierte Daten zwischen Computersystemen austauschen zu können.
Im Gegensatz zu [TERMREF::JSON] ist XML nicht auf eine bestimmte Programmiersprache
beschränkt und kann in einer Vielzahl von Anwendungen und Kontexten eingesetzt werden.
[ENDTERM]

## Y
## Z
