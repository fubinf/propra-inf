title: Begriffsverzeichnis
---

Auf dieser Seite werden wichtige Begriffe erläutert;
insbesondere solche, die für mehr als eine Aufgabe relevant sind.

Die Erläuterungen verweisen zurück auf die Aufgaben, in denen sie erwähnt werden,
sowie ggf. auf Aufgaben, die weitere Erläuterungen dazu enthalten.

## A

[TERM::Akzeptanzkriterien|acceptance criteria]
Spezifische, messbare Bedingungen, die definieren,
wann eine User Story oder eine Funktion als abgeschlossen und akzeptiert betrachtet wird.
Sie legen die Erwartungen und Anforderungen fest, die erfüllt sein müssen,
damit das Produkt oder die Funktion als erfolgreich betrachtet wird.
Akzeptanzkriterien dienen dazu, Missverständnisse zu vermeiden, indem sie
klare Richtlinien für die Entwicklung und das Testen geben.
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

[TERM::API|Application Programming Interface]
Eine Schnittstelle,
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

[TERM::BDD|Behavior Driven Development]
Eine agile Softwareentwicklungsmethode, die sich auf die Zusammenarbeit
zwischen Entwicklern, Testern und nicht-technischen Stakeholdern konzentriert.
In BDD werden Anforderungen
in verständlichen, natürlichsprachlichen Szenarien formuliert (meist mittels "Gherkin"-Syntax),
die dann mechanisch ist automatisierte Tests übersetzt werden.

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

[TERM::Breakpoint|Haltepunkt]
Ein Breakpoint bezeichnet beim Debugging von Computerprogrammen eine besonders markierte Stelle 
im Programm. 
Erkennt ein Debugger beim Ausführen des Programms eine mit einem Breakpoint markierte Stelle, 
wird hier die Verarbeitung der Befehle angehalten.
[ENDTERM]

## C

[TERM::Charakterisierungstest|Characterization Test]
Ein [TERMREF2::Modultest::Modul-] oder [TERMREF::Integrationstest],
der aber nicht überprüft, ob das Verhalten korrekt ist,
sondern nur, ob es "wie bisher" ist.
Das beim Erstellen des Tests aktuell Verhalten der Software wird dabei
als korrekt angenommen und mit dem Test festgeschrieben.

Eine Menge solcher Tests, die den Eingaberaum gut abdeckt, _charakterisiert_
also das Verhalten der Software.
[ENDTERM]

[TERM::Code Convention|Programming Style|Programmierstil]
Ein Programmierstil und die Vorgaben dazu regeln, „wie“ ein Programm, d. h. sein Quellcode,
in formaler und struktureller Hinsicht gestaltet sein soll –
unabhängig davon, „was“ das Programm leisten soll.
[ENDTERM]

[TERM::Conditional Breakpoint|Bedingter Haltepunkt]
Ein [TERMREF::Breakpoint], der erst ausgelöst wird, wenn eine vorgegebene Bedingung erfüllt ist.
[ENDTERM]

[TERM::CRUD|Create Read Update Delete]
EIn Ausdruck der die grundlegenden Operationen bezeichnet, die auf Daten angewendet werden können:
Erstellen, Lesen, Ändern, Löschen. Diese vier CRUD-Operationen bilden die grundlegenden Funktionen
für die Interaktion mit Daten in den meisten Anwendungen. [TERMREF::Regressionstest]s beziehen sich
auf dieses Schema zum Testen von Daten und Objekten, um die Zugverlässigkeit einer Anwendung
sicherzustellen.
[ENDTERM]

## D

[TERM::Deduktion|deduktive Methode|deduktiver Schluss]
Der Prozess des Ziehens logisch zwingender Schlussfolgerungen.
Mittels Deduktion können aus Theorien Aussagen über Einzelfälle gewonnen werden.
[ENDTERM]

[TERM::Default|Defaultwert|Default-Argument]
Ein [TERMREF::Argument] zur Übergabe an einen [TERMREF::Parameter],
das implizit benutzt wird, wenn man nicht explizit ein Argument übergibt.
[ENDTERM]

[TERM::Defekt|Defect|Fault|Bug]
Eine strukturelle Eigenschaft des Produkts (meistens des Codes, aber es könnte auch z.B. eine
Entwurfs-, Test- oder Anforderungsbeschreibung betroffen sein):
Eine mögliche Folge eines menschlichen [TERMREF2::Fehler::-s] beim Programmieren;
verursacht meistens ein [TERMREF::Versagen].
Zur Korrektur eines Defekts wird in der Regel der Code verändert.
[ENDTERM]

[TERM::DSL|Domänenspezifische Sprache]
Eine speziell auf eine bestimmten Anwendungsbereich ("Domäne") zugeschnittene Sprache.
Im Gegensatz zu allgemeinen Programmiersprachen, die
für eine Vielzahl von Anwendungen geeignet sind, ist eine DSL darauf ausgerichtet, spezifische
Aufgaben oder Anforderungen in einem begrenzten Kontext besonders elegant zu adressieren.
[ENDTERM]

[TERM::Dynamische analytische Qualitätssicherung]
Die Überprüfung der Softwarequalität durch das Testen der Software.
Dazu gehören verschiedene Testmethoden wie [TERMREF::Modultest], [TERMREF::Integrationstest],
[TERMREF::Systemtest] und [TERMREF::Leistungstest].
[ENDTERM]

## E

[TERM::Encoding|Zeichenkodierung]
Die Art und Weise, wie eine Nachricht oder ein Zeichenvorrat als Folge von Bits oder von Bytes dargestellt wird.

https://de.wikipedia.org/wiki/Zeichenkodierung
[ENDTERM]

[TERM::Executable|ausführbare Datei]
Eine Datei, deren "executable"-Bit gesetzt ist (mit dem Kommando `chmod`)
und die entweder Maschinencode enthält
oder mit einer [TERMREF::Shebang-Zeile] beginnt.
[ENDTERM]

## F

[TERM::Fehler|Error]
Ein menschliches Verhalten, das u.U. zu einem [TERMREF::Defekt] führt.
Entweder ein falsches Verhalten (engl. _commission_) oder ein Versäumnis (engl. _omission_).
[ENDTERM]

## G

[TERM::Globbing]
Die Expansion von Dateinamensmustern in eine Liste von Dateinamen.
Dabei wird insbesondere das Zeichen `*` als Platzhalter für irgendeinen Dateinamens-Teil interpretiert,
sodass sich z.B. mittels `*.txt` alle Dateien mit dem Suffix `.txt` (im selben Verzeichnis)
zugleich ansprechen lassen.

Globbing ist insbesondere in allen gängigen [TERMREF2::Shell::-s] implementiert.

Kurzerläuterung: [https://tldp.org/LDP/abs/html/globbingref.html](https://tldp.org/LDP/abs/html/globbingref.html)
[ENDTERM]

## H

[TERM::Header|Header-Metadaten|HTTP-Header]
Ein Abschnitt, der am Anfang eines Dokuments, einer Nachricht oder einer
Datei steht und meist Metadaten, also Informationen über den Inhalt oder den Kontext bereitstellt.

Bei einer API-Antwort sind dies z.B. zusätzliche Informationen, die den Kontext der Antwort beschreiben
und wie sie interpretiert werden sollte.
Diese Metadaten werden z.B. bei [TERMREF::HTTP] in Form von Headerfeldern bereitgestellt,
die durch ein Schlüsselwort eingeleitet werden,
z.B. `Content-Type:`, `Set-Cookie:`, `Cache-Control:`.

https://de.wikipedia.org/wiki/Liste_der_HTTP-Headerfelder
[ENDTERM]

[TERM::HTTP|Hypertext Transfer Protocol]
Ein [TERMREF::Protokoll], das für die Übertragung von Daten im World Wide Web verwendet wird.
Ermöglicht die Kommunikation zwischen Client-Anwendungen (wie Webbrowsern) und Servern,
auf denen statische Ressourcen (wie Bilder) oder Anwendungen gehostet werden.
[ENDTERM]

[TERM::HTTP-Statuscode]
Ein HTTP-Statuscode ist eine dreistellige numerische Kennung, die von einem Webserver an den Client
gesendet wird, um den Status einer HTTP-Anfrage zu kennzeichnen. Diese Statuscodes geben an, ob eine
Anfrage erfolgreich war, eine Weiterleitung erforderlich ist, ein Fehler aufgetreten ist oder andere
Informationen über den Status der Anfrage liefern.
[ENDTERM]

[TERM::Hypothese]
Eine Hypothese im wissenschaftlichen Sinne ist eine auf dem Stand der Wissenschaft gegründete
Annahme, die zwar geeignet ist, bestimmte Erscheinungen zu erklären, deren Gültigkeit aber noch
nicht bewiesen oder verifiziert ist.

In der Logik werden Hypothesen in Form von logischen Aussagen formuliert.
In einem logischen Gespräch ist eine Hypothese die Prämisse eines Arguments, deren Wahrheit
zunächst ausgeklammert wird.
Dabei wirken Hypothesen als Implikationen, die der Verteidigung einer These dienen.
[ENDTERM]

## I

[TERM::Integrationstest|Integration Test]
Ein Test, der im Gegensatz zum [TERMREF::Modultest] das korrekte Zusammenspiel mehrerer
(evtl. sehr vieler) Module oder Komponenten prüfen will,
dafür aber im Gegensatz zum [TERMREF::Systemtest] programmatische Schnittstellen benutzt,
nicht solche für menschliche Benutzer_innen.
[ENDTERM]

[TERM::Issue Tracker|Bug Tracker|Defect Tracker|Defektdatenbank]
Ein Programm zur Koordination der Arbeit an bekannten (aber anfangs noch nicht bereinigten
und meist auch noch nicht lokalisierten) Defekten oder sonstigen Verbesserungswünschen (feature requests)
einer Software.

Ein Issue Tracker erlaubt insbesondere

- die Klassifikation der Einträge nach diversen verschiedenen Kriterien,
  sodass man schnell auf Teilmengen der Einträge zugreifen kann,
- die Markierung eines Eintrags als "offen" (open, in Bearbeitung) oder "geschlossen" (closed) und
- die Zuweisung zuständiger Personen für die Bearbeitung.
[ENDTERM]

## J

[TERM::JavaScript|Javascript|JS|ECMAScript|ES]
Eine dynamisch typisierte Programmiersprache mit einer Syntax, die der von Java ähnelt,
aber einer völlig anderen Semantik.
Ist in Webbrowsern implementiert und wird dort verwendet, um HTML-basierten Webseiten
dynamisches Verhalten zu geben.
Wird seit einigen Jahren auch außerhalb des Browsers verwendet, insbesondere auf der
Serverseite von Webanwendungen ("backend").
[ENDTERM]

[TERM::JSON|JavaScript Object Notation]
Leichtgewichtiges Datenaustauschformat.
Ursprünglich eine kleine Teilmenge der Programmiersprache [TERMREF::JavaScript],
heute aber in jeder gängigen Programmiersprache als [TERMREF::Bibliothek] implementiert
und sehr verbreitet für den Datenaustausch zwischen Anwendungen.
[ENDTERM]

## K

[TERM::Kommandozeilenparameter]
Ein [TERMREF::Parameter] für ein ausführbares Programm, das per
[TERMREF::Shell]-Kommando aufgerufen wird,
oder für ein eingebautes Shell-Kommando
[ENDTERM]

[TERM::KDT|Keyword-Driven Testing|Schlüsselwortgetriebenes Testen]
Eine Testautomatisierungsmethode, bei der Tests mithilfe von Schlüsselwörtern oder
Aktionen beschrieben werden, die von einem Testframework interpretiert und ausgeführt werden.

https://de.wikipedia.org/wiki/Keyword-Driven_Testing  
https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates
[ENDTERM]

## L

[TERM::Leistungstest|Performance Test]
Ein Test, der prüft, ob ein Programm schnell genug arbeitet und genügend große Datenmengen
verkraften kann.
[ENDTERM]

[TERM::Linux|GNU/Linux]
Eine Familie von Open-Source-Betriebssystem-Distributionen, die auf dem Linux-Betriebssystemkern aufbauen
sowie auf einem umfangreichen Universum von Softwarepaketen.

https://de.wikipedia.org/wiki/Linux
[ENDTERM]

## M

[TERM::Modultest|Unit Test]
Ein Test, der das korrekte Funktionieren eines bestimmten Moduls prüfen soll.
Dabei wird entweder nur dieses eine Modul ausgeführt (weil es keine weiteren davon benötigten
Module gibt oder indem diese durch Attrappen ersetzt werden)
oder es wird zwar der ganz darunter hängende Teilgraph von benötigten Modulen
auch mit verwendet, aber die Testeingaben so ausgewählt, dass es voraussichtlich für das
Ergebnis nur auf das zu testende Modul ankommt.
[ENDTERM]

## N
## O

[TERM::OpenAPI|Swagger]
Ein Standard, der die Dokumentation
von RESTful APIs (Representational State Transfer) erleichtert.
Maschinenlesbare Beschreibung einer API, die Entwicklern ermöglicht, schnell
zu verstehen, welche Ressourcen verfügbar sind, welche
Parameter erwartet werden und welche Antworten zurückgegeben werden können.
[ENDTERM]

## P

[TERM::Parameter]
Ein Platzhalter für ein [TERMREF::Argument], das man an etwas Parametrisiertes übergeben kann.
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

[TERM::Payload|HTTP-Body]
Der Teil einer Nachricht (insbesondere: einer API-Antwort),
der die tatsächlichen Daten oder Informationen enthält, die von der Anfrage zurückgegeben
werden.

Bei HTTP heißt die Payload "Rumpf" (body), davor stehen die [TERMREF::Header].
Der Rumpf kann z.B. JSON-, XML-, JPG-, PDF-, Text- oder beliebige Binärdaten enthalten.
Der Header `Content-Type:` gibt an, als was der Rumpf interpretiert werden soll.
[ENDTERM]

[TERM::pip]
"Package installer for Python":
Das Programm, mit dem man üblicherweise externe Bibliotheken von einem entsprechenden
Server ("package index", meist wird pypi.org benutzt) lädt und installiert.

Dokumentation: https://pip.pypa.io/en/stable/getting-started/
[ENDTERM]

[TERM::Pipeline]
Das ist eine Abfolge von automatisierten Schritten oder Prozessen, die in einem
Workflow ausgeführt werden, um bestimmte Aufgaben oder Abläufe zu erledigen. Sie ermöglicht
die Automatisierung von komplexen Abläufen, indem sie verschiedene Schritte wie Builds, Tests,
Bereitstellungen und mehr integriert.
[ENDTERM]

[TERM::Post Mortem|Post-Mortem-Analyse]
Eine Analyse, die nach Ende des zu analysierenden Ereignisses durchgeführt wird.
Dadurch lassen sich Vorfälle untersuchen, dokumentieren und zu Lernzwecken festhalten.
Sie hat keine feste Form, enthält aber in der Regel die Gründe für den Vorfall, die Lösung des 
Vorfalls und Nachbereitungen, die solche Vorfälle verhindern sollen.
[ENDTERM]

[TERM::Prompt]
Eine Textzeichenfolge, die in der Kommandozeile angezeigt wird, um den
Benutzer zur Eingabe eines Befehles aufzufordern. Sie enthält oft Informationen wie den
Benutzernamen, den Hostnamen, den aktuellen Pfad und möglicherweise andere relevante Informationen.

Beispiel: `student1@computer1 /my/dir/path/to/my/workdir 12:24:01  515`
[ENDTERM]

[TERM::Protokoll|Protocol]
Spezifikation einer Verfahrensweise.
In der Informatik ist damit meist ein Kommunikationsprotokoll gemeint,
das beschreibt, wie Kommunikationspartner Nachrichten austauschen.
Es legt fest, welche Nachrichtentypen es gibt, wie jeder Typ aufgebaut ist
und unter welchen Umständen welcher Nachrichtentyp gesendet werden darf oder muss.

Es gibt zahlreiche Kommunikationsprotokolle.
Hier im ProPra ist meist nur [TERMREF::HTTP] von Interesse.
[ENDTERM]

[TERM::Public-Key-Kryptographie|Assymetrische Kryptographie|Schlüsselpaar]
Asymmetrische Kryptographie, auch als Public-Key-Kryptographie bekannt, ist ein 
Verschlüsselungsverfahren, bei dem zwei unterschiedliche Schlüssel verwendet 
werden: ein öffentlicher Schlüssel zur Verschlüsselung von Daten und ein privater 
Schlüssel zur Entschlüsselung. Anders als bei symmetrischen Verfahren, bei denen 
ein einziger Schlüssel für beide Vorgänge genutzt wird, bietet die asymmetrische 
Kryptographie eine sicherere Lösung für den Datenaustausch, da der private Schlüssel 
geheim gehalten werden kann, während der öffentliche Schlüssel frei zugänglich ist. 
Diese Technik wird häufig für sichere Kommunikation, digitale Signaturen und 
Schlüsselaustauschmechanismen in der Informationssicherheit eingesetzt
[ENDTERM]

## Q

[TERM::Qualitätssicherung|QS|Quality Assurance|QA]
Alle Schritte, durch die man sicherstellen will, dass ein Produkt oder
eine Dienstleistung die festgelegten Qualitätsstandards erfüllt.
Umfasst Schritte zur Planung, Kontrolle, Überprüfung und Verbesserung, die darauf abzielen,
Mängel zu vermeiden oder zu beseitigen und die Kundenzufriedenheit zu maximieren.

Im ProPra interessieren uns vor allem zwei Bereiche der QS:
[TERMREF::Dynamische analytische Qualitätssicherung] und
[TERMREF::Statische analytische Qualitätssicherung].
[ENDTERM]

## R

[TERM::Rahmenwerk|Framework|Kontrollumkehr|Inversion of Control]
Eine [TERMREF::Bibliothek] (oder ein direkt lauffähiges Programm),
die nicht hauptsächlich vom Code der Benutzer_in aufgerufen wird,
sondern bei der der Benutzercode eigene Programmteile registriert,
die dann anschließend durch das Rahmenwerk aufgerufen werden.

Dieses Funktionsprinzip ist bekannt als Kontrollumkehr (inversion of control)
oder Hollywood-Prinzip: _"Don't call us, we'll call you"_.
[ENDTERM]

[TERM::Refactoring|Refaktorisierung]
Eine Veränderung der Struktur einer Software, die das Verhalten der
Software unverändert lässt. Dient zur Pflege der Struktur.

Wenn man eine Software viele Male ändert und erweitert, verfällt dabei
ihre Entwurfsstruktur, wenn man sich nicht aktiv dagegenstemmt.
Man muss also neben den gewünschten Änderungen am Verhalten der Software
zusätzlich welche machen, die "nur" der Strukturverbesserung dienen.

Es hat sich bewährt, diese beiden Sorten von Änderung nicht zu vermischen,
sondern strikt getrennt durchzuführen, denn wenn man nur die Struktur
verändert (nicht das Verhalten; das Verhalten wird lediglich "refaktorisiert")
bleiben vorhandene automatisierte Tests gültig
und man kann sich mir deren Hilfe versichern, dass man beim Strukturverändern
das Verhalten nicht versehentlich doch mitverändert hat.
Nur mit dieser Absicherung hat man den Mut, solche Refactorings
wirklich immer durchzuführen, wenn sie sinnvoll sind.

Es gibt einen weitgehend kanonischen Katalog von elementaren Refactoring-Operationen,
aus denen sich alle Refactorings zusammensetzen lassen:
https://refactoring.com/
[ENDTERM]

[TERM::Regressionstest]
Ein Regressionstest ist ein Typ von Softwaretest, der durchgeführt wird, um sicherzustellen,
dass früher funktionierende Teile einer Software nach einer Änderung weiterhin wie erwartet
funktionieren und somit unerwünschte Seiteneffekte schnellstmöglich erkannt werden.
[ENDTERM]

[TERM::Request|Anfrage]
Nachricht, die im Rahmen eines [TERMREF2::Protokoll::-s] ein Client an einen Server sendet,
um Daten anzufordern oder eine Operation auszulösen.

Bei [TERMREF::HTTP] wird ein Request an eine spezifische _Ressource_ auf dem Server gesendet,
die durch einen URI/URL identifiziert wird.
[ENDTERM]

[TERM::Response|Antwort]
Die Daten, die im Rahmen eines [TERMREF2::Protokoll::-s]
ein Server an einen Client zurücksendet, als Reaktion auf eine [TERMREF::Anfrage],
die der Client zuvor gesendet hat.
Enthält den angeforderten Inhalt und/oder gibt Informationen darüber, ob die Anfrage erfolgreich war oder nicht.
[ENDTERM]

[TERM::RPA|Robotic Process Automation|Robotische Prozessautomatisierung]
Die Anwendung von Software-Robotern oder "Bots", um menschliche Aufgaben in Geschäftsprozessen
zu automatisieren. Diese Bots agieren in der Regel auf der Benutzeroberfläche von Anwendungen,
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
für alle Sprachen anwendbar, bei denen ein `#` am Zeilenanfang einen Kommentar anzeigt
oder die erste Zeile gesondert behandelt wird.
[ENDTERM]

[TERM::Shell|Unix-Shell|Linux-Shell|Kommandozeile]
Übliche Bezeichnung für die Kommandozeilen-Interpretierer auf [TERMREF2::Unix::--] oder [TERMREF2::Linux::--Systemen],
weil diese aus Sicht einer Benutzer_in wie eine "Schale" den Kern des Betriebssystems umhüllen.

https://de.wikipedia.org/wiki/Kommandozeile  
https://de.wikipedia.org/wiki/Unix-Shell
[ENDTERM]

[TERM::Statische analytische Qualitätssicherung]
Überprüfung von Softwareartefakten wie Code, Spezifikationen und Dokumentation,
ohne dass die Software dabei ausgeführt wird.
Umfasst Techniken wie Code-Reviews, statische Code-Analyse und formale Methoden,
die potenzielle Fehler, Inkonsistenzen oder Verbesserungsmöglichkeiten identifizieren.

Kann (im Gegensatz zu [TERMREF2::Test::-s]) auch für nicht ausführbare Produkte benutzt werden.
Findet für Code im Vergleich zu Tests manche Sorten von Problem leichter, andere schwieriger,
sodass sich beide Verfahrensweisen gut ergänzen.
[ENDTERM]


[TERM::su]
`su` steht für "Substitute User" und ist ein Befehl in Linux-Systemen, der es einem 
Benutzer ermöglicht, die Identität zu einem anderen Benutzer zu wechseln, normalerweise 
zum Superuser (Root), nach Eingabe des entsprechenden Passworts. Im Gegensatz zu `sudo` 
wechselt `su` vollständig zur Identität des anderen Benutzers, und die erhöhten Rechte 
bleiben aktiv, bis der Benutzer sich explizit wieder ausloggt oder den Befehl exit eingibt.
[ENDTERM]

[TERM::sudo]
`sudo` ist ein Befehl in Linux-Systemen, der es autorisierten Benutzern ermöglicht, 
vorübergehend erhöhte Rechte zu erhalten, um administrative Aufgaben auszuführen.
[ENDTERM]

[TERM::Systemtest|System Test]
Ein Test des Gesamtsystems unter Verwendung von dessen natürlichen Schnittstellen,
meist einem GUI.
Solche Tests sind aufwändig zu implementieren, brauchen komplizierte Testwerkzeuge,
laufen langsam und gehen beim Weiterentwickeln der Software häufig kaputt,
weil die GUI sich oft ändert.
[ENDTERM]

## T

[TERM::Test]
Das Ausprobieren von Software, um relevante Eigenschaften zu überprüfen;
meistens die Frage, ob die Software korrekte Ergebnisse liefert (Defekttest).
[ENDTERM]

[TERM::TDD|Test Driven Development]
ist eine Softwareentwicklungsmethode, bei der [TERMREF2::Tests::-s] vor der eigentlichen Implementierung
des Codes geschrieben werden. Der Prozess beginnt mit dem Schreiben eines Tests, der das
erwartete Verhalten der Funktionalität beschreibt. Dann wird der minimal notwendige Code
implementiert, um den Test erfolgreich durchzuführen. Dieser iterative Prozess von Schreiben
von Tests, Implementieren des Codes wird fortgesetzt, bis die gewünschte Funktionalität erreicht ist.
[ENDTERM]

[TERM::Tutorial]
Ein kurzer Lehrgang (in der Regel in Schriftform, eventuell als Video)
zum Erlernen der Grundzüge eines klar abgegrenzten Themenbereichs,
meist der Benutzung einer Programmier- oder Kommandosprache,
einer [TERMREF::Bibliothek] oder eines [TERMREF2::Framework::-s].

Ein Tutorial führt den Lernende_n durch praktische Schritte,
die dieser selbst durchführen soll, um einen optimalen Lernerfolg zu erreichen.
Die Lernenden können Varianten der Schritte auszuprobieren,
um ihren Lernerfolg zu verbreitern.
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

[TERM::Urgrund|root cause|Urgrundanalyse|root cause analysis|Grundursachen-Analyse]
Eine Urgrund-Analyse (Grundursachen-Analyse, root cause analysis) geht so:
Ausgehend von einem Problem, z.B. einem [TERMREF::Versagen], stellt man die Frage
"Warum ist das passiert?".
Für die Antwort(en) stellt man die Frage erneut und immer so weiter.

Dann ist der Urgrund die letzte Antwort, für die noch gilt, dass man auf den betreffenden
Faktor nennenswert Einfluss nehmen kann, um künftige Probleme zu verhindern,
die vom gleichen Faktor ausgelöst werden könnten.

Simples Beispiel: Ich bin zu spät gekommen, weil ich zu spät losgefahren bin,
weil mir die Uhrzeit nicht genügend bewusst war, weil ich unkonzentriert war,
weil ich zu wenig geschlafen hatte, weil ich zu spät ins Bett gegangen bin,
weil ich so viel Spaß an der Party hatte.  
Den Spaß an der Party kann (oder will) man nicht sinnvoll verändern,
das zu späte Insbettgehen aber sehr wohl; also ist das der Urgrund.

Wenn man dann diesen Faktor tatsächlich passend verändert, ist
Urgrundanalyse eine hochwirksame Methode zur Vorbeugung von Problemen.
[ENDTERM]

[TERM::User Story]
Kurze, informelle Beschreibung einer Funktion aus der Perspektive eines Endbenutzers.
Umfasst typischerweise wer die Funktion nutzt, was getan werden soll und wozu es relevant ist.

User Stories dienen als Kommunikationsmittel zwischen Entwicklern, Kunden und anderen Stakeholdern,
um Anforderungen klar zu definieren und das Verständnis zu verbessern.
Oft werden begleitend [TERMREF:Akzeptanzkriterien] definiert.
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

[TERM::Verifizierung|verifizieren]
Verifizierung oder Verifikation (von lateinisch veritas ‚Wahrheit' und facere ‚machen') ist
die Bestätigung durch Bereitstellung eines objektiven Nachweises, dass festgelegte
Anforderungen erfüllt worden sind.

https://glossary.istqb.org/de_DE/term/verifizierung  TODO_2_ruhe/prechelt: AchduliebeGüte!
[ENDTERM]

[TERM::Versagen|Failure|Symptom]
Falsches Verhalten eines Programms relativ zur
Spezifikation, der Anforderung oder den Erwartungen.
Ist ein Symptom eines [TERMREF2::Defekt::-s].
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
Genau wie [TERMREF::JSON] ist XML nicht auf eine bestimmte Programmiersprache
beschränkt und kann in einer Vielzahl von Anwendungen und Kontexten eingesetzt werden.
[ENDTERM]

## Y
## Z
