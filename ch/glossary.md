title: Begriffsverzeichnis
---

Auf dieser Seite werden wichtige Begriffe erläutert;
insbesondere solche, die für mehr als eine Aufgabe relevant sind.

Die Erläuterungen verweisen zurück auf die Aufgaben, in denen sie erwähnt werden,
sowie ggf. auf Aufgaben, die weitere Erläuterungen dazu enthalten.

[TOC] 

## A

[TERM::Account|Konto|Benutzeraccount|Benutzerkonto|Useraccount|Benutzer|User|Nutzer]
Synonyme für die Identität eines (menschlichen oder nichtmenschlichen) Benutzers
in einem Betriebssystem.
Ein Account ist mit einem Zugangsschutz versehen (z.B. Passwort) und verfügt
im System über gewisse Rechte (z.B. Zugriff auf bestimmte Dateien.)

Die Ausdrücke Benutzer, Nutzer oder User sind mehrdeutig und können auch die
menschliche Benutzer_in meinen oder mitmeinen, nicht nur deren Account.
Leider ist in Unix für Accounts die mehrdeutige Bezeichnung 'user' üblich.

[Zum Gebrauch der Wörter Nutzer/Benutzer/Anwender(in)](https://german.stackexchange.com/a/47502). 
[ENDTERM]

[TERM::ACL|ACLs]
Access Control Lists (ACLs) in Linux bieten eine erweiterte Möglichkeit, Berechtigungen für 
Dateien und Verzeichnisse zu verwalten. Im Gegensatz zum traditionellen Unix-Berechtigungssystem, 
das Berechtigungen für Besitzer, Gruppe und andere Benutzer definiert, ermöglichen ACLs die 
Zuweisung granularer Berechtigungen für einzelne Benutzer oder Gruppen.
[ENDTERM]

[TERM::Akzeptanzkriterien|acceptance criteria]
Spezifische, überprüfbare Bedingungen, die definieren,
wann eine User Story oder eine Funktion als vollständig und akzeptabel
(und hoffentlich korrekt) betrachtet wird.
Sie legen die Erwartungen und Anforderungen fest, die erfüllt sein müssen,
damit das Produkt oder die Funktion als erfolgreich betrachtet wird.
Akzeptanzkriterien dienen dazu, Missverständnisse zu vermeiden, indem sie
klare Richtlinien für die Entwicklung und das Testen geben.
[ENDTERM]

[TERM::Alias]
Ein alternativer Name (meist im Sinne einer Abkürzung) für ein Kommando
(meist mit Optionen und deshalb länger) in der [TERMREF::Shell].
Weniger flexibel, aber in einfachen Fällen bequemer hinzuschreiben als eine
[TERMREF::Shellfunktion].
[ENDTERM]

[TERM::API|Web-API|REST-API]
Application Programming Interface: 
Die Schnittstelle eines Objekts, einer Bibliothek, eines Plugin-Mechanismus oder eines Dienstes,
über die andere Software (Klient) deren Operationen benutzen kann.

Eigentlich stammt der Begriff aus der Welt der programmiersprachlichen Programmierung;
dann gilt eine API immer für eine ganz bestimmte Programmiersprache,
mit der der Klient auf die API zugreift.

Heute ist mit API sehr oft eine Web-API gemeint, bei der ein Aufruf 
an einen Dienst über das [TERMREF::Protokoll] [TERMREF::HTTP] erfolgt ("Web-API"),
das von einer beliebigen Programmiersprache aus angesprochen wird.
Die Daten werden in ebenfalls programmiersprachen-unabhängigen Formaten wie
[TERMREF2::JSON::--Objekten] oder [TERMREF::XML] übergeben.
Häufig wird dabei von einer REST API gesprochen (was eine bestimmte Form von Web-APIs meint),
obwohl die fragliche API die REST-Bedingungen gar nicht einhält.

[HREF::https://de.wikipedia.org/wiki/Programmierschnittstelle]  
[HREF::https://de.wikipedia.org/wiki/Representational_State_Transfer] (REST API)
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

[TERM::Arbeitsbereich]
[ENDTERM]

[TERM::Argument]
Der konkrete Wert, den man an einen [TERMREF::Parameter] übergibt,
z.B. in Form einer konkreten Variable.
[ENDTERM]

[TERM::Artefakt|Artifact]
Dabei handelt es sich um eine Datei oder eine Sammlung von Dateien,
die während eines Workflows erstellt werden und die für spätere Schritte oder für die Analyse nach
der Ausführung des Workflows verwendet werden können. Beispiele sind: Build-Ausgaben (Binärdateien
oder sogar vollständige [TERMREF::Release]-Versionen), Testberichte oder auch Dokumentationen
[ENDTERM]

[TERM::ASCII]
Der American Standard Code for Information Interchange, kurz ASCII, ist ein 
Zeichenkodierungsstandard, der Zahlen den Buchstaben des englischen Alphabets, Satzzeichen und 
Steuerzeichen zuordnet, um sie in Computern und anderen elektronischen Geräten darzustellen.
Die Kodierung definiert 128 Zeichen, bestehend aus 33 nicht druckbaren und 95 druckbaren 
Leerzeichen, beginnend mit dem Leerzeichen.  
In Code kann so z. B. der Buchstabe "A" auch durch seinen ASCII-Wert "65" dargestellt werden.
Eine ASCII-Tabelle finden Sie unter [HREF::https://www.asciitable.com/].
[ENDTERM]

[TERM::Assemblersprache|Assembly]
Eine Assemblersprache ist eine menschenlesbare Variante der
[TERMREF::Maschinensprache].
Assemblersprachen haben kaum Abstraktion.
Dadurch sind Assemblersprachen, genau wie Maschinensprachen, von
Prozessorarchitektur zu Prozessorarchitektur verschieden.
Programme in Assemblersprache können daher nicht ohne Veränderungen
auf eine andere Prozessorarchitektur portiert werden.
[ENDTERM]

[TERM::Assemblierer|Assembler]
Der Assembliere ist ein Programm, welches in [TERMREF::Assemblersprache]
verfassten Quellcode in [TERMREF::Maschinensprache] übersetzt.
Oftmals gehen [TERMREF::Übersetzer] und Assemblierer Hand in Hand.
[ENDTERM]

[TERM::async|await]
[ENDTERM]

[TERM::Auszeichnungssprache]
Eine Auszeichnungssprache ist eine formale Sprache, die verwendet wird, 
um die Struktur und Darstellung von Texten in einem Dokument zu definieren. 
Sie besteht aus Markierungen, die den Text umgeben und so 
dessen Bedeutung und Formatierung festlegen. 
Auszeichnungssprachen werden häufig in der Dokumentverarbeitung, im Webdesign und in der Datenbeschreibung verwendet.

Ein bekanntes Beispiel für eine Auszeichnungssprache ist [TERMREF::HTML], 
die zur Erstellung und Strukturierung von Inhalten im World Wide Web verwendet wird. 
HTML verwendet "Tags", um verschiedene Elemente wie Überschriften, Absätze und Links zu kennzeichnen.

[TERMREF::Markdown] ist ein weiteres Beispiel für eine Auszeichnungssprache. 
Es wird oft in Texteditoren und auf Plattformen wie GitHub verwendet, 
um einfache Textformatierungen wie Überschriften, Listen und Links zu erstellen. 
Markdown zeichnet sich durch eine einfache und leicht schreib- und lesbare Syntax aus.

Weitere Informationen: [HREF::https://de.wikipedia.org/wiki/Auszeichnungssprache]
[ENDTERM]

## B

[TERM::Bash|.bashrc]
Die meistbenutzte [TERMREF::Shell] auf Linux-Systemen.

Kommandos zur Initialisierung der Shell stehen in der Datei `.bashrc` im HOME-Verzeichnis
(das stimmt nur ungefähr, etwas genauer ist das in
[HREF::https://linuxize.com/post/bashrc-vs-bash-profile/] beschrieben).
Richtig genau steht es in der Dokumentation von Bash.
[ENDTERM]

[TERM::BDD|Behavior Driven Development]
Eine agile Softwareentwicklungsmethode, die sich auf die Zusammenarbeit
zwischen Entwicklern, Testern und nicht-technischen Stakeholdern konzentriert.
In BDD werden Anforderungen
in verständlichen, semi-natürlichsprachlichen Szenarien formuliert,
die dann mithilfe handgeschriebener Adapter als automatisierte Tests ausgeführt werden.

[HREF::https://docs.robotframework.org/docs/testcase_styles/bdd#what-is-bdd]  
[HREF::https://www.codecentric.de/wissens-hub/blog/givenwhenthen-and-example-tables-using-the-robot-framework]
[ENDTERM]

[TERM::Bibliothek|Library]
Eine Sammlung von Programmelementen (z.B. Klassen, Funktionen, Datentypen, Module, Pakete)
ohne Hauptprogramm; 
dazu bestimmt, von anderen Programmen oder anderen Bibliotheken benutzt zu werden.

Bibliotheken erlauben es, Programme weitgehend aus vorhandenen Bausteinen zusammenzusetzen
und nur noch wenig Code selbst schreiben zu müssen.
Sie sind das wirksamste Mittel für hohe Produktivität bei der Softwareentwicklung.
[ENDTERM]

[TERM::Binder|Linker]
Der Binder ist ein Programm, welches aus mehreren [TERMREF::Objekt-Dateien]
eine ausführbare Datei erzeugt.
Konkret findet sich dies bei [TERMREF2::Bibliothek::-en], deren Bestandteile
mittels des Binders in ein Programm eingebunden wird.
Ebenso ist der Binder daran beteiligt aus mehreren Quellcode-Dateien ein
fertiges Programm zu binden, die Quellcode-Dateien werden jeweils einzeln
übersetzt und abschließend zusammengebunden.
[ENDTERM]

[TERM::Blob (git)]

Ein Blob (Binary Large Object) ist einer von mehreren Objekttypen in Git und stellt den Inhalt 
einer Datei in einem bestimmten Zustand dar.

Blobs speichern reine Dateiinhalte – ohne Dateinamen, Metadaten oder Verzeichnisstruktur.
Jeder Blob ist durch einen Hash-Wert eindeutig identifizierbar.

Beim Ausführen von `git add` wird ein neuer Blob erzeugt (sofern sich der Inhalt geändert hat) und 
in der Objektdatenbank von Git gespeichert. 
Commits referenzieren über sogenannte Tree-Objekte auf diese Blobs.

Wichtig: Git speichert nicht die Veränderungen zwischen zwei Versionen, sondern immer den 
vollständigen Inhalt ([TERMREF::Snapshot (git)]) einer Datei in einem Blob.
[ENDTERM]

[TERM::Branch|Zweig]
Bei git: Eine eigene Versionsgeschichte.
Ein Zweig hat einen Namen und einen jüngsten Commit und durch dessen Vorgänger und Vorvorgänger
eine eigene Versionshistorie. 
Alle Zweige treffen sich, rückwärts gesehen, beim allerersten Commit.
Vorwärts gesehen verzweigt sich die Versionsgeschichte an manchen Stellen und aus einem Zweig werden zwei.
Allerdings ergibt das nicht zwingend einen Baum, denn Zweige können 
durch 'merge'-Commits auch wieder zusammengeführt werden.
Meist gibt man dabei den Namen des einen Zweiges auf. 
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
Das ist enorm nützlich, wenn man anschließend mittels 
[TERMREF::Refactoring] die Struktur der Software verbessern möchte.
[ENDTERM]

[TERM::CI/CD]
Steht für Continuous Integration (CI) und Continuous Deployment (CD) oder Continuous Delivery (CD),
und es handelt sich um eine Reihe von Praktiken und Prinzipien in der Softwareentwicklung,
die darauf abzielen, den Entwicklungsprozess zu automatisieren und zu optimieren.
[ENDTERM]

[TERM::CLI|Commandline Interface]
Textbasierte Bedienschnittstelle ([TERMREF::TUI]), bei der der Software nacheinander Kommandos
auf einer _Kommandozeile_ eingegeben werden.
Häufigste Sorte solcher Kommandozeilen-Interpretierer sind [TERMREF2::Shell::-s].
[ENDTERM]

[TERM::Code Convention|Programming Style|Programmierstil]
Ein Programmierstil und die Vorgaben dazu regeln, „wie“ ein Programm, d. h. sein Quellcode,
in formaler und struktureller Hinsicht gestaltet sein soll –
unabhängig davon, „was“ das Programm leisten soll.
[ENDTERM]

[TERM::Compiler|Übersetzer]
Ein Übersetzer ist ein Programm, welches Quellcode einer Sprache in eine andere
Sprache übersetzt.  
Zielsprachen können die [TERMREF::Maschinensprache], eine
[TERMREF::Zwischensprache] oder eine andere [TERMREF::Hochsprache] sein.
[ENDTERM]

[TERM::Conditional Breakpoint|Bedingter Haltepunkt]
Ein [TERMREF::Breakpoint], der erst ausgelöst wird, wenn eine vorgegebene Bedingung erfüllt ist.
[ENDTERM]

[TERM::Constraint]
In Bezug auf Datenbanken bezieht sich ein "Constraint" auf eine Regel oder Bedingung, die auf eine
oder mehrere Spalten einer Tabelle angewendet wird, um die Integrität der Datenbank zu gewährleisten.
Constraints dienen dazu, sicherzustellen, dass die Datenbankkonsistenz erhalten bleibt, indem sie
bestimmte Regeln erzwingen.
[ENDTERM]

[TERM::context manager|Kontextmanager]
Ein Objekt, das die Methoden `__enter__()` und `__exit__()` implementiert. Diese ermöglichen es, 
das Objekt in `with`-Statements zu verwenden.

[HREF::https://docs.python.org/3/glossary.html#term-context-manager]
[ENDTERM]

[TERM::CRUD|Create Read Update Delete]
Ein Ausdruck, der die grundlegenden Operationen bezeichnet, die auf Daten angewendet werden können:
Erstellen, Lesen, Ändern, Löschen. Diese vier CRUD-Operationen bilden die grundlegenden Funktionen
für die Interaktion mit Daten in den meisten Anwendungen. [TERMREF::Regressionstest]s beziehen sich
auf dieses Schema zum Testen von Daten und Objekten, um die Zuverlässigkeit einer Anwendung
sicherzustellen.
[ENDTERM]

[TERM::CSS|Cascading Style Sheets]
Eine deklarative Sprache, in der man ausdrücken kann, wie [TERMREF::HTML]-Seiten formatiert 
und angezeigt werden sollen.
CSS-Spezifikationen formulieren Regeln ("styles"), die dann auf einzelne Elemente
der HTML-Datei Anwendung finden.
Dadurch sind die Dokumentstruktur (ausgedrückt in HTML)
und die Formatierung (ausgedrückt in CSS) relativ gut voneinander getrennt
und man kann die Formatierung sehr schnell global über viele Dokumente hinweg anpassen,
indem man Styles ändert, die in allen diesen Dokumenten benutzt werden.
[ENDTERM]

[TERM::CSV|comma-separated values|character-separated values]
Ein einfaches und verbreitetes Dateiformat für tabellarische Daten 
mit einer beliebigen, aber festen Zahl von Spalten.
Jeder Datensatz belegt genau eine Zeile.
Die erste Zeile kann (oder auch nicht) die Spaltennamen enthalten.
Jedes Datenfeld ist vom nächsten durch ein Komma getrennt.
Statt Kommas können auch andere Trenner benutzt werden, meist TAB ("tab-separated values", TSV),
Semikolon oder senkrechter Strich (beides trotzdem meist bezeichnet als CSV).

Wenn in den Datenfeldwerten Kommas vorkommen, können die betreffenden Datenfelder in
Quotes eingeschlossen sein; da ist das Vorgehen aber uneinheitlich.

[HREF::https://de.wikipedia.org/wiki/CSV_(Dateiformat)]
[ENDTERM]

## D

[TERM::Dateiberechtigungen|Rechte|Leserecht|Schreibrecht]
Dateiberechtigungen in Unix legen fest, welche Aktionen (Lesen, Schreiben, Ausführen) für 
bestimmte Benutzer oder Benutzergruppen erlaubt sind. Volle Berechtigungen werden durch die 
Zeichenkette "rwx" dargestellt, wobei 
"r" (read) für Lesen, "w" (write) für Schreiben und "x" (execute) für Ausführen steht.
Ein "-" zeigt an, dass ein Recht nicht gegeben ist.
Bei Verzeichnissen ist "x" das Recht, die Dateien des Verzeichnisses aufzulisten.

Bei `ls -l` werden neun Stellen mit diesen Zeichen angegeben.
Die ersten drei Zeichen geben die Berechtigungen für den Nutzer an, dem die Datei gehört (owner, o),
die nächsten drei geben sie für die Gruppe an, der die Datei gehört (group, g), 
und die letzten drei geben sie für alle anderen Benutzer an (other, o).

Genaueres siehe z.B. [HREF::https://wiki.ubuntuusers.de/Rechte/].
[ENDTERM]

[TERM::Datensatz|Datensätze]
Ein Datensatz ist eine Gruppe von inhaltlich zusammenhängenden Datenfeldern mit einer logischen Struktur.
[ENDTERM]

[TERM::Datenstruktur|Datenstrukturen]
In der Informatik und Softwaretechnik ist eine Datenstruktur ein Objekt, welches zur Speicherung und Organisation von Daten dient.

[HREF::https://de.wikipedia.org/wiki/Datenstruktur]
[ENDTERM]

[TERM::de-morgansche Gesetze|de-morgansche Regeln]
Die de-morganschen Gesetze sind zwei grundlegende Regeln für logische Aussagen und gelten in 
allen booleschen Algebren und sind bedeutsam in der Aussagenlogik und Mengenlehre.

Sie lauten:
`nicht (a und b) ist äquivalent zu ((nicht a) oder (nicht b))`, sowie
`nicht (a oder b) ist äquivalent zu ((nicht a) und (nicht b))`.
[ENDTERM]

[TERM::Decorator|Dekorierer]
Eine Funktion in einer Programmiersprache, die eine andere Funktion oder eine Klasse
modifiziert oder erweitert. Es ermöglicht, das Verhalten einer Funktion oder Klasse zu ändern,
ohne deren Code direkt zu ändern. Durch Dekorierer können beispielsweise Funktionen mit
zusätzlicher Funktionalität versehen werden, wie das Hinzufügen von Logging oder das Implementieren
von Sicherheitsüberprüfungen.
[ENDTERM]

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
Eine Abweichung von den möglichen korrekten Strukturen.
"Korrekt" bezieht sich dabei manchmal auf eine genaue Spezifikation, oft aber auf eine viel weniger
konkrete und oft nirgends aufgeschriebene Erwartung.
Ein Defekt ist eine mögliche Folge eines menschlichen [TERMREF2::Fehler::-s] beim Programmieren;
viele (aber nicht alle) Defekte verursachen immer oder manchmal ein [TERMREF::Versagen].
Zur Korrektur eines Defekts wird in der Regel das Produkt (z.B. der Code) verändert.
[ENDTERM]

[TERM::Dependency Injection]
Dependency Injection ist ein Entwurfsmuster, bei dem externe Abhängigkeiten explizit an ein Objekt
oder eine Funktion übergeben werden – statt sie intern zu erstellen.
Beim Testen ermöglicht das den Austausch dieser Abhängigkeiten durch kontrollierte Mocks, Dummies
oder Stubs.
[ENDTERM]

[TERM::Deserialisierung]
Ein Mechanismus, der sich auf den Prozess bezieht, bei dem die serialisierten Daten
(s. [TERMREF::Serialisierung]) wieder in ihre ursprüngliche Form zurückkonvertiert werden. In Bezug
auf JSON bedeutet dies, dass die JSON-Zeichenkette in Datenstrukturen einer bestimmten
Programmiersprache zurücktransformiert wird. Auf diese Weise können die Daten nach dem Transfer
oder der Speicherung wieder von einer Anwendung gelesen und verwendet werden.
[ENDTERM]

[TERM::Design Pattern|Verhaltensmuster]
Design Patterns sind typische Lösungen für wiederkehrende Probleme im Softwareentwurf, ähnlich 
vorgefertigten Bauplänen. Sie dienen als allgemeine Konzepte zur Lösung spezifischer Probleme 
und ermöglichen Anpassungen an die Bedürfnisse deines eigenen Programms.  
Es wird zwischen Erzeugungsmustern (Creational Patterns), Strukturmustern (Structural Patterns) 
und Verhaltensmustern (Behavioral Patterns) unterschieden.
[ENDTERM]

[TERM::Dictionary|dict|Wörterbuch|Map]
Hierbei handelt es sich um eine Datenstruktur, die Werte einer Menge (genannt "Schlüssel"/"Keys")
auf Werte einer anderen (möglicherweise überschneidenden oder sogar deckungsgleichen) Menge
(genannt "Werte"/"Values") abbildet.  
Eine oft gesehene Notation ist `{key1: value1, key2: value2}`.  
Dieses konkrete Beispiel bildet den Schlüssel `key1` auf den Wert `value1` und `key2` auf
`value2` ab. Alle anderen möglichen Schlüssel werden nicht abgebildet, gelten also nicht als
Teil der Datenstruktur.  
Häufig sind die Schlüssel skalar (also beispielsweise Zahlen oder Zeichenketten), aber die
Werte beliebiger Natur (beispielsweise Listen).  
Zur Verwendung siehe [die Python-Dokumentation zu Dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
[ENDTERM]

[TERM::dig|Dig]
Dig, kurz für "Domain Information Groper", ist ein Befehlszeilenwerkzeug, das in Unix-basierten 
Betriebssystemen verwendet wird, um DNS-Abfragen durchzuführen. Es ermöglicht das Abfragen von 
DNS-Servern, um Informationen über DNS-Datensätze wie IP-Adressen, Nameserver und andere 
DNS-Ressourceneinträge für eine bestimmte Domain zu erhalten.
[ENDTERM]

[TERM::Django]
Django ist ein in Python geschriebenes Webframework zur schnellen Entwicklung von sicheren und wartbaren Webanwendungen. Mit Django lassen sich **moderne Webanwendungen** effizient umsetzen, ohne grundlegende Funktionen wie Formularverarbeitung, Datenbankzugriff oder Authentifizierung selbst schreiben zu müssen. Django folgt dem **MTV-Muster** (Model-Template-View), das dem bekannten MVC-Prinzip ähnelt, aber speziell auf die Webentwicklung mit Python abgestimmt ist.
Das Framework bringt viele Komponenten direkt mit, darunter ein **ORM**, ein **Admin-Interface**, ein **Routing-System** und eine **Vorlagen-Engine**. Django legt außerdem großen Wert auf **Sicherheit** und folgt dem Prinzip **Don't Repeat Yourself (DRY)** zur Vermeidung von redundanter Logik.
Typische Einsatzbereiche sind **Content-Management-Systeme**, **soziale Plattformen** oder **API-Backends**.
Gute Quellen für Django:
- [Offizielle Dokumentation](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN – Django lernen](https://developer.mozilla.org/de/docs/Learn/Server-side/Django)
[ENDTERM]

[TERM::DNS|Domain Name System]
DNS (Domain Name System) ist ein Dienst, der Internetadressen in [TERMREF2::IP-Adresse::-n] umwandelt. 
Es sorgt dafür, dass man statt einer Zahlenfolge (wie 192.168.0.1) einfach einen Domainnamen, wie 
www.beispiel.de, eingeben können, um eine Webseite zu erreichen. Vereinfacht gesagt ist DNS ein 
Telefonbuch fürs Internet.
[ENDTERM]

[TERM::DNS-Record-Types]
DNS-Record-Typen sind Einträge im Domain Name System (DNS), die Informationen über Domains und deren 
zugehörige Ressourcen speichern. Jeder Record-Typ hat eine spezifische Funktion und speichert 
unterschiedliche Arten von Daten. Zum Beispiel gibt der MX-Record den Mailserver an, der für den 
Empfang von E-Mails für eine Domain zuständig ist.
Eine Übersicht aller [TERMREF::DNS-Record-Types] findet man auf 
[nslookup.io](https://www.nslookup.io/learning/dns-record-types/).
[ENDTERM]

[TERM::Download unter WSL]
Wenn Sie unter Windows Dateien herunterladen, stehen diese zunächst nicht direkt in Ihrer 
Unix-Umgebung zur Verfügung.
In WSL werden jedoch Ihre Windows-Festplatten standardmäßig unter dem Pfad /mnt/ eingebunden.
Haben Sie die Datei beispielsweise im Windows-Ordner `Downloads` gespeichert, 
können Sie sie mit folgendem Befehl in Ihr Home-Verzeichnis der WSL-Umgebung kopieren:
`cp /mnt/c/Users/<username>/Downloads/<DATEI> /home/<username>/`
[ENDTERM]

[TERM::DRY|DRY-Prinzip|Don't repeat yourself]
DRY steht für "don't repeat yourself".
Das Prinzip besagt, man solle Redundanz vermeiden oder zumindest reduzieren,
also nicht gleiche Information (etwa bestimmte Strings) oder Anweisungen an mehreren Stellen
im Programm haben.  
DRY ist meist eine gute Idee, aber wie fast alles kann man es übertreiben
und handelt sich dann mehr Probleme ein als man damit löst. 
Das gegenteilige Verhalten wird [TERMREF::WET] genannt und ist meist (aber nicht immer) eine schlechte Idee.

[OAOO auf c2.com](https://wiki.c2.com/?OnceAndOnlyOnce)  
[DRY auf c2.com](https://wiki.c2.com/?DontRepeatYourself)  
[TwiceAndOnlyTwice](https://wiki.c2.com/?TwiceAndOnlyTwice)
[ENDTERM]

[TERM::DSL|Domänenspezifische Sprache]
Eine speziell auf einen bestimmten Anwendungsbereich ("Domäne") zugeschnittene Sprache.
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

[HREF::https://de.wikipedia.org/wiki/Zeichenkodierung]
[ENDTERM]

[TERM::Executable|ausführbare Datei]
Eine Datei, deren "executable"-Bit gesetzt ist (mit dem Kommando `chmod`)
und die entweder Maschinencode enthält
oder mit einer [TERMREF::Shebang-Zeile] beginnt.
[ENDTERM]

## F

[TERM::Fehler|Error]
Ein menschliches Verhalten, das u.U. zu einem [TERMREF::Defekt] führt.
Weitere Unterscheidungen:
  - Falschtun: So ein Fehler kann durch eine falsche Umsetzung erfolgen (commission)
  - Versäumnis: oder dadurch, das etwas gar nicht erst umgesetzt wurde (omission)
  - Irrtum: Weil man sich dessen nicht bewusst war (misconception)
  - Versehen: oder es anders machen wollte (blunder)
[ENDTERM]

[TERM::Fehlerzustand|invalid state]
Ein Fehlerzustand tritt auf, wenn das System aufgrund eines Fehlers in einen nicht beabsichtigten
oder inkonsistenten Zustand gerät. Das kann dazu führen, dass das System unerwartete Ergebnisse
produziert oder nicht ordnungsgemäß funktioniert.
[ENDTERM]

[TERM::Filedeskriptor|file descriptor]
Beschreibt auf unixoiden Betriebssystemen eine Ressource, auf der Daten geschrieben und gelesen 
werden können. Jeder Prozess hat seine eigenen Filedeskriptoren. 
Ein Filedeskriptor (FD) wird durch eine natürliche Zahl dargestellt.

Es gibt drei Standard-FDs (0: stdin, 1: stdout, 2: stderr), aber für jeden Prozess können 
beliebig viele weitere FDs existieren, die verschiedene Datenströme beschreiben (Dateien, 
Netzwerk Sockets etc.).

[HREF::https://en.wikipedia.org/wiki/File_descriptor]
[ENDTERM]

[TERM::Filter]
In Unix werden Programme, die von Standardeingabe (stdin) lesen und nach Standardausgabe (stdout)
schreiben, Filter genannt.
Bei Programmen wie `grep`, die Teile der Eingabe weglassen, leuchtet die Bezeichnung ein,
aber sie gilt auch für Programme wie `sort`, die die Eingabe nur umformen.
[ENDTERM]

[TERM::Firewall]
Eine **Firewall** ist ein Sicherheitsmechanismus, der den Netzwerkverkehr überwacht und filtert, 
um einen Computer oder ein Netzwerk vor unbefugtem Zugriff und schädlichen Daten zu schützen. 
Sie fungiert als digitale Barriere zwischen einem vertrauenswürdigen internen Netzwerk 
(z.B. einem Heim- oder Firmennetzwerk) und einem externen, weniger vertrauenswürdigen Netzwerk 
(meist dem restlichen Internet).

Firewalls arbeiten nach vordefinierten Regeln, die festlegen, welcher Datenverkehr zugelassen (erlaubt)
und welcher blockiert (verweigert) werden soll. 
Diese Regeln können auf verschiedenen Kriterien basieren:
fast immer Portnummern und Protokolle,
oft IP-Adressen oder Domainnamen,
und teilweise sogar dem Inhalt der Datenpakete.

Zu unterscheiden sind dabei

* **Software-Firewalls:** Diese sind auf einzelnen Geräten (wie einem PC oder Laptop) installiert und 
    schützen dieses spezifische Gerät.
* **Hardware-Firewalls:** Dies sind eigenständige Geräte (oft in Routern integriert), die ein ganzes 
    Netzwerk schützen und typischerweise in Unternehmen oder größeren Netzwerken eingesetzt werden.
[ENDTERM]

[TERM::first-class citizen|first-class Objekt]
In Programmiersprachen beschreibt man Objekte als first-class citizen, wenn sie die folgenden 
Eigenschaften unterstützen:

- Sie können als Parameter an Funktionen übergeben werden
- Sie können als Ergebnis einer Funktion zurückgegeben werden
- Sie können Variablen zugewiesen werden
- Sie können auf Äquivalenz getestet werden

In der Regel sind primäre Datentypen wie Integer, String oder Float first-class citizen. In einigen 
Programmiersprachen, wie Python, erfüllen aber auch Funktionen diese Eigenschaften, wodurch 
[TERMREF2::higher-order function::Funktionen höherer Ordnung] ermöglicht werden.
[ENDTERM]

[TERM::Flask]
Flask ist ein leichtgewichtiges und flexibles Web-Framework für Python, das es Entwicklern
ermöglicht, schnell und einfach Webanwendungen zu erstellen. Es folgt dem WSGI
(Web Server Gateway Interface) Standard und bietet eine einfache API, die es ermöglicht, Routen,
Templates und Formulare zu definieren.
[ENDTERM]

[TERM::Funktionale Programmierung]
Ein Programmierparadigma, bei dem die Verwendung von Funktionen im Mittelpunkt steht.
Anstelle von in imperativen Sprachen typischen Abfolgen von Befehlen, Schleifen und 
Variablenzuweisungen werden Funktionsverkettungen und Rekursionen verwendet.
Vorteile sind unter anderem eine bessere Modularität, Wiederverwendbarkeit sowie Vermeidung von 
Seiteneffekten.
[ENDTERM]

## G

[TERM::Gate|Gatekkeeper]
Der Begriff bezeichnet eine Kontroll- oder Entscheidungsstelle, die den Fortschritt eines
Softwareentwicklungsprozesses an bestimmten Punkten überprüft und steuert.
Gates werden häufig in [TERMREF::CI/CD]-Pipelines eingesetzt, um sicherzustellen, dass bestimmte
Kriterien erfüllt sind, bevor der Code in die nächste Phase des Entwicklungszyklus übergeht.
[ENDTERM]

[TERM::Git]
Das heute mit weitem Abstand verbreitetste 
[Versionsverwaltungssystem](https://de.wikipedia.org/wiki/Versionsverwaltung).
[ENDTERM]

[TERM::GitHub|github|Github|github.com]
GitHub ([HREF::https://github.com]) ist ein Dienst, der Zusammenarbeitsfunktionen bereitstellt, 
mit denen Teams ihre Arbeit auf Basis von [TERMREF::Git] organisieren können.
Für öffentliche Repositories ist GitHub seit jeher gratis.
Für private (d.h. nur einer festen Gruppe von Personen zugängliche) Repositories gilt das
seit einigen Jahren bis zu gewissen Grenzen ebenfalls.
[ENDTERM]

[TERM::Globbing]
Die Expansion von Dateinamensmustern in eine Liste von Dateinamen.
Dabei wird insbesondere das Zeichen `*` als Platzhalter für irgendeinen Dateinamens-Teil interpretiert,
sodass sich z.B. mittels `*.txt` alle Dateien mit dem Suffix `.txt` (im selben Verzeichnis)
zugleich ansprechen lassen.

Globbing ist insbesondere in allen gängigen [TERMREF2::Shell::-s] implementiert.

Kurzerläuterung: [HREF::https://tldp.org/LDP/abs/html/globbingref.html]
[ENDTERM]

[TERM::Glossar]
[Griechisch-lateinischer Ausdruck für](https://de.wikipedia.org/wiki/Glossar) Begriffsverzeichnis.
[ENDTERM]

[TERM::GUI|Graphical User Interface]
Grafische Bedienschnittstelle, die mit Maus oder Fingern bedient wird.
Gelegentlich auch als [WIMP](https://en.wikipedia.org/wiki/WIMP_(computing)) bezeichnet:
Windows, Icons, Menus, Pointer.

Gegensätze sind das [TERMREF::TUI]
und hier insbesondere das [TERMREF::CLI].

[HREF::https://en.wikipedia.org/wiki/Graphical_user_interface]
[ENDTERM]


## H
[TERM::Hardlink|Hardlinks]
Hardlinks sind Einträge auf eine Datei im Dateisystem. Hardlinks werden im System, wie die Datei 
an sich behandelt, weil die Links physisch auf die Datei auf die Festplatte zeigt.
[ENDTERM]

[TERM::Hashfunktion|kryptografische Hashfunktion]
Funktion, die beliebig große Eingabedaten annimmt und einen Wert in einer fest definierten 
Größe ausgibt (genannt _hash_ oder _digest_). Für sie gelten folgende Eigenschaften:

1. Die Eingabelänge kann beliebig lang sein.
2. Die Ausgabelänge ist fest.
3. Die Berechnung des Hashwertes ist für beliebige Eingaben effizient.

Für kryptografische Hashfunktionen gelten zusätzlich folgende Eigenschaften:

4. Einwegfunktion: Es ist praktisch unmöglich für einen gegebenen Ausgabewert einen passenden 
   Eingabewert für die Funktion zu finden.
5. Schwache Kollisionsresistenz: Es ist praktisch unmöglich, für eine feste Eingabe eine
   davon verschiedene Eingabe zu finden, die den gleichen Hashwert ergibt.
6. Starke Kollisionsresistenz: Es ist praktisch unmöglich, zwei beliebige und unterschiedliche 
   Eingaben zu finden, die den gleichen Hashwert ergeben.
7. Die Ausgabe der Hashfunktion ist pseudozufällig (statistisch nicht vorhersehbar).
[ENDTERM]

[TERM::Header|Header-Metadaten|HTTP-Header]
Ein Abschnitt, der am Anfang eines Dokuments, einer Nachricht oder einer
Datei steht und meist Metadaten, also Informationen über den Inhalt oder den Kontext bereitstellt.

Bei einer API-Antwort sind dies z.B. zusätzliche Informationen, die den Kontext der Antwort beschreiben
und wie sie interpretiert werden sollte.
Diese Metadaten werden z.B. bei [TERMREF::HTTP] in Form von Headerfeldern bereitgestellt,
die durch ein Schlüsselwort eingeleitet werden,
z.B. `Content-Type:`, `Set-Cookie:`, `Cache-Control:`.

[HREF::https://de.wikipedia.org/wiki/Liste_der_HTTP-Headerfelder]
[ENDTERM]

[TERM::higher-order function|Funktion höherer Ordnung]
Eine Funktion, die mindestens eine Funktion als Argument entgegennimmt oder wiederum eine 
Funktion als Rückgabewert zurückgibt.
[ENDTERM]

[TERM::Hilfsbereich]
Ein Verzeichnisbaum für Zwecke des ProPra, der außerhalb des Arbeitsbereichs liegt,
der nach git eingecheckt wird.
[ENDTERM]

[TERM::Hochsprache|höhere Programmiersprache]
Eine Hochsprache ist eine Programmiersprache, welche einen hohen Grad der
Abstraktion aufweist, d.h. Konstrukte, die weit entfernt sind von dem, was die CPU des Rechners
unmittelbar ausführen könnte.  
Eine Hochsprache ist deshalb nicht direkt ausführbar, sondern erfordert einen
[TERMREF::Übersetzer] oder [TERMREF::Interpretierer].
[ENDTERM]

[TERM::HTML|Hypertext Markup Language]
HTML steht für Hypertext Markup Language; es ist eine [TERMREF::Auszeichnungssprache].
In HTML wird dieses Prinzip umgesetzt, indem spezielle Zeichenfolgen ([TERMREF2::HTML-Tag::-s]) 
in den Text eingefügt werden. 
Diese Markierungen beschreiben eine Strukturierung des Inhalts, Hyperlinks und anderes mehr.

[HREF::https://wiki.selfhtml.org/wiki/HTML/Tutorials/Entstehung_und_Entwicklung]
[ENDTERM]

[TERM::HTML-Attribut]
Ein HTML-Attribut ist eine Eigenschaft eines [TERMREF2::HTML-Element::-s], 
die zusätzliche Informationen über dieses Element bereitstellt. 
Attribute werden innerhalb des Start-Tags eines HTML-Elements deklariert und bestehen aus einem Namen und einem Wert. 
Sie beeinflussen die Bedeutung oder das Erscheinungsbild des Elements. 
Ein Attribut besteht aus einem Namen, gefolgt von einem Gleichheitszeichen und einem Wert in Anführungszeichen:

```html
<a href="https://www.beispielseite.com" target="_blank">Besuche Beispielseite</a>
```
In diesem Beispiel gibt das `href`-Attribut die URL an, zu der der Link führt, 
und das `target`-Attribut bestimmt, dass der Link in einem neuen Tab oder Fenster geöffnet wird.
[ENDTERM]


[TERM::HTML-Tag|HTML-Element]
Eine Markierung in einem [TERMREF::HTML]-Dokument, die angibt, wo Teile eines Dokuments beginnen und enden. 
Ein solches Tag besteht am Beginn eines Dokumentteiles aus einem Namen, der in spitze Klammern eingeschlossen ist. 
Für das Ende steht wieder das gleiche Tag, jedoch mit einem Schrägstrich. 
Z.B. markiert das Tag `h1` die Haupt-Überschrift einer Seite:

```html
<h1>Erste Schritte in HTML</h1>
```

Das Anfangs-Tag, der Inhalt dazwischen und das Ende-Tag bilden zusammen ein HTML-Element.
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
[ENDTERM]

## I

[TERM::ICMP]
ICMP (Internet Control Message Protocol) ist ein Netzwerkprotokoll, das für den Austausch von 
Steuer- und Fehlermeldungen im Internet verwendet wird. 
Es ermöglicht Geräten, Informationen über den Status von Verbindungen zu senden, z. B. wenn ein 
Zielgerät nicht erreichbar ist oder ein Paket verloren gegangen ist. 
ICMP wird häufig von Netzwerktools wie "ping" verwendet, um die Erreichbarkeit eines Hosts zu 
überprüfen und die Netzwerkverbindung zu diagnostizieren. Es spielt eine wichtige Rolle bei der 
Verwaltung und Fehlersuche in IP-Netzwerken.
[ENDTERM]

[TERM::IDE|Integrated Development Environment]
Eine Kategorie komplexer interaktiver Softwarewerkzeuge.
Eine IDE bietet eine große Zahl von Funktionen an, um Programmcode zu erzeugen,
zu erkunden, zu modifizieren und damit zusammenhängende Operationen zu starten,
etwa Läufe automatisierter Tests, Inbetriebnahmen von Webanwendungen und viele andere mehr.

Wer eine IDE gut beherrscht, kann damit deutlich produktiver arbeiten als mit der
manuellen Kombination anderer Werkzeuge.
Dies gilt umso mehr, je größer die Codebasis wird.
[ENDTERM]

[TERM::Index]
Ein Index ist eine numerische oder symbolische Kennzeichnung, die verwendet wird, 
um gezielt auf ein Element innerhalb einer geordneten Datenstruktur zuzugreifen. 
Er kommt in vielen Kontexten vor – etwa bei Arrays, Listen, Zeichenketten oder Datenbanken – 
und dient dazu, Daten schnell und effizient zu lokalisieren oder zu referenzieren. 
In vielen Programmiersprachen beginnt ein numerischer Index bei 0 (nullbasiert).
Index beschreibt sowohl einen einzelnen Indexwert, 
als auch das Aggregat aller Indexwerte einer Datenstruktur.
[ENDTERM]

[TERM::Integrationstest|Integration Test]
Ein Test, der im Gegensatz zum [TERMREF::Modultest] das korrekte Zusammenspiel mehrerer
(evtl. sehr vieler) Module oder Komponenten prüfen will,
dafür aber im Gegensatz zum [TERMREF::Systemtest] programmatische Schnittstellen benutzt,
nicht solche für menschliche Benutzer_innen.
[ENDTERM]

[TERM::Interpreter|Interpretierer]
Ein Interpretierer (engl. "interpreter"), insbesondere der Python-Interpreter, ist ein Programm, 
das Quellcode in einer bestimmten Programmiersprache analysiert (insbesondere auf korrekte
Syntax und erlaubte Semantik) und ausführt.

Bei Python spricht man oft vom Interpretierer, obwohl das nicht ganz stimmt,
denn Python wird bei der Standardimplementation CPython 
von einem Python-Compiler in Bytecode übersetzt und erst der
wird dann interpretiert.

[HREF::https://devguide.python.org/internals/]
[ENDTERM]

[TERM::IP|Internet Protocol]
IP (Internet Protocol) ist das grundlegende Protokoll, das dafür sorgt, dass Daten über das Internet 
von einem Computer zum anderen gelangen. 
Es teilt die Daten in kleine Pakete auf und sorgt dafür, dass sie den richtigen Weg durch 
verschiedene Netzwerke finden, bis sie ihr Ziel erreichen. 
Jedes Gerät im Internet hat eine eindeutige [TERMREF::IP-Adresse], die wie eine digitale Adresse funktioniert, 
damit die Daten an den richtigen Ort gesendet werden.
[ENDTERM]

[TERM::IP-Adresse]
Eine IP-Adresse ist eine eindeutige Zahlenfolge, die jedem Gerät im Internet zugewiesen wird. 
Sie funktioniert wie eine digitale Adresse und hilft dabei, Daten an den richtigen Ort zu senden. 
Es gibt zwei Versionen von IP-Adressen: [TERMREF::IPv4] (z. B. 192.168.0.1) und 
[TERMREF::IPv6] (z. B. 2001:0db8:85a3::8a2e:0370:7334). 
Sie ermöglichen es Computern, Smartphones und anderen Geräten, miteinander zu kommunizieren und 
Informationen auszutauschen.
[ENDTERM]

[TERM::IPv4]
IPv4 (Internet Protocol Version 4) wird für die Identifizierung von Geräten im Internet verwendet.
Eine IPv4-Adresse besteht aus 32 Bit und wird in vier Zahlen dargestellt, die durch Punkte 
getrennt sind (z. B. 192.168.1.1). 
Diese Adressen helfen, Daten an den richtigen Ort zu senden. 
IPv4 kann etwa 4,3 Milliarden Adressen bereitstellen.
[ENDTERM]

[TERM::IPv6]
IPv6 (Internet Protocol Version 6) ist die neueste Version des Internetprotokolls, die entwickelt 
wurde, um das Problem der begrenzten IP-Adressen von IPv4 zu lösen. 
Eine IPv6-Adresse ist 128 Bit lang und wird meist in acht Gruppen von Hexadezimalzahlen dargestellt, 
die durch Doppelpunkte getrennt sind (z. B. 2001:0db8:85a3:0000:0000:8a2e:0370:7334). 
IPv6 stellt 2^128 (ungefähr 340 Sextillionen) Adressen bereit.
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

[TERM::Iterables|Iterables in Python]
Iterables in Python sind Objekte, die eine Sequenz von Elementen bereitstellen,
über die iteriert werden kann,
indem sie entweder die `__iter__()`-Methode implementieren oder ein Iterable zurückgeben.
Typische Beispiele für Iterables in Python sind Listen, Tupel, Sets und Dictionaries.
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

[TERM::KDT|Keyword-Driven Testing|Schlüsselwortgetriebenes Testen]
Eine Testautomatisierungsmethode, bei der Tests mithilfe von Schlüsselwörtern oder
Aktionen beschrieben werden, die von einem Testframework interpretiert und ausgeführt werden.

[HREF::https://de.wikipedia.org/wiki/Keyword-Driven_Testing]  
[HREF::https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates]
[ENDTERM]

[TERM::Kollision]
Ereignis, wenn bei einer [TERMREF::Hashfunktion] zwei unterschiedliche Eingaben den gleichen Hash 
erzeugen.
[ENDTERM]

[TERM::Kommandozeilenparameter]
Ein [TERMREF::Parameter] für ein ausführbares Programm, das per
[TERMREF::Shell]-Kommando aufgerufen wird,
oder für ein eingebautes Shell-Kommando
[ENDTERM]

## L

[TERM::Lazy Evaluation]
Ein Verfahren von Programmiersprachen, bei dem ein Ausdruck erst dann ausgewertet wird, wenn er 
benötigt wird. Diese 
Vorgehensweise kann sowohl die Laufzeit als auch die Speicherauslastung verringern, da unnötige 
Auswertungen erspart werden und berechnete Werte nicht im Speicher gehalten werden müssen, 
sondern erst bei Bedarf generiert werden.

In Python findet Lazy Evaluation beispielsweise in Verbindung mit 
[PARTREFMANUAL::py-Iterators::Iteratoren] statt.
[ENDTERM]

[TERM::Leistungstest|Performance Test]
Ein Test, der prüft, ob ein Programm schnell genug arbeitet und genügend große Datenmengen
verkraften kann.
[ENDTERM]

[TERM::Linter|Codeprüfer|Stilprüfer]
Linting ist die automatisierte statische Analyse von Programmcode, 
um den Code auf potenzielle Fehler, Stilprobleme oder Sicherheitsrisiken zu überprüfen.
Die zugehörigen Werkzeuge werden Linter genannt.
"lint" ist Englisch für Fussel oder Fluse; Linter sollen also helfen, störende Kleinigkeiten ("Flusen")
im Code zu entfernen.

Linting hilft Entwicklern, qualitativ hochwertigen und konsistenten Code zu schreiben. Es trägt dazu
bei, Fehler frühzeitig im Entwicklungsprozess zu erkennen, die Lesbarkeit des Codes zu verbessern
und die Einhaltung von Coding-Standards sicherzustellen. 
Linter stellen also Know-How und Detailaufmerksamkeit bereit, die die Entwickler_innen
dadurch nicht mehr immer selbst aufbringen müssen.
[ENDTERM]

[TERM::Linux|GNU/Linux]
Eine Familie von Open-Source-Betriebssystem-Distributionen, die auf dem Linux-Betriebssystemkern aufbauen
sowie auf einem umfangreichen Universum von Softwarepaketen.

[HREF::https://de.wikipedia.org/wiki/Linux]
[ENDTERM]

[TERM::Logfile|Logdatei]
Eine Textdatei (selten auch Binärdatei), in der Logdatensätze stehen,
die gewisse Abläufe protokollieren.

Beispielsweise führt ein Webserver 
eine Logdatei über alle HTTP-Requests, die er erhalten hat (`access.log`) und 
eine zweite über alle Fehler, die bei deren Bearbeitung aufgetreten sind (`error.log`).

Meistens besteht jeder Logdatensatz aus genau einer Zeile.
Oft haben alle Logdatensätze dasselbe Format oder 
es gibt jedenfalls nur eine handvoll verschiedener Formate.

Manchmal gibt es allerdings auch mehrzeilige Einträge in Logdateien,
deren Folgezeilen dann evtl. kein solches Standardformat haben.
[ENDTERM]


## M

[TERM::Main-Branch|Master-Branch]
Der Hauptzweig in einem git-Repository, welcher beim Initialisieren des Repos erstellt wird. 
Dieser wird je nach Client und Server entweder `main` oder `master` heißen. In der 
Debian-Installation von git wird weiterhin `master` verwendet, allerdings mit einem Verweis 
darauf, dass sich dieser in Zukunft ändern wird. Wann das sein wird, ist unklar.
Mit der Option `init.defaultBranch` lässt sich der Standardname permanent ändern.
[ENDTERM]

[TERM::manpage|manpages]
Eine Manpage ("manual page", Handbuch-Seite) gibt es zu (fast) jedem Unix-Kommando.
Man findet die für das Kommando `xy` mittels `man xy`.
Manpages sind kurze Referenzdokumentationen. 
Sie bieten eine strukturierte Zusammenfassung von Syntax, Optionen, Funktionalitäten und 
manchmal Beispielen für die Verwendung des betreffenden Befehls.

Fest in die Shell eingebaute Kommandos haben keine eigene Manpage; 
das Kommando `help` zeigt eine Kurzinformation dazu.
[ENDTERM]

[TERM::Markdown]
Ist eine [TERMREF::Auszeichnungssprache], die verwendet wird, um Text mit einer einfachen Syntax zu formatieren.
Sie wurde entwickelt, um das Schreiben von Texten für das Web zu erleichtern, ohne die Notwendigkeit
von komplexen HTML-Tags oder Formatierungsbefehlen.
[ENDTERM]

[TERM::Maschinensprache|Maschinencode]
Eine Maschinensprache ist die, von einem Prozessor direkt ausführbare,
Anweisungsreihenfolge.
Jede Anweisung an den Prozessor ist hier als eine Bytereihenfolge codiert.  
Maschinensprachen sind von Prozessorarchitektur zu Prozessorarchitektur
verschieden.
[ENDTERM]

[TERM::Median]
Der Median ist ein statistisches Maß, das in der Mitte einer sortierten Liste von Zahlen liegt.
Wenn eine Liste von Zahlen nach Größe sortiert ist, ist der Median der Wert, der genau in der Mitte
der Liste liegt. Das bedeutet, dass die Hälfte der Zahlen in der Liste größer als der Median ist
und die andere Hälfte kleiner ist.
[ENDTERM]

[TERM::Metadaten]
Metadaten sind Daten über Daten. Sie beschreiben Eigenschaften oder Merkmale über Daten.
Metadaten können z.B. sein aus welcher Quelle eine Information stammt oder eine Erläuterung einer Information.
[ENDTERM]

[TERM::Modul|Module]
"Modul" ist in der Softwaretechnik ein abstraktes Konzept.
Es beschreibt eine Sammlung von Programmelementen, die zusammen entworfen werden
und ein Innen (Einzelheiten des Moduls, Implementierungsdetails) 
von einem Außen trennen. 
Außerhalb des Moduls ist nur die Modulschnittstelle sichtbar.

In einer konkreten technischen Welt wie Python ist ein Modul ein technisches Konstrukt.
Ein Modul in Python ist etwas, das mit `import` in ein Python-Programm importiert
werden kann und meistens durch eine einzelne Datei oder einen ganzen Dateibaum 
von Python-Code realisiert wird.
Ziele bei der Gestaltung von Modulen sind meistens Abstraktion und oft Wiederverwendung.

[HREF::https://docs.python.org/3/tutorial/modules.html]
[ENDTERM]

[TERM::Modultest|Unit Test]
Ein Test, der das korrekte Funktionieren eines bestimmten Moduls prüfen soll.
Dabei wird entweder nur dieses eine Modul ausgeführt (weil es keine weiteren davon benötigten
Module gibt oder indem diese durch Attrappen ersetzt werden)
oder es wird zwar der ganze darunter hängende Teilgraph von benötigten Modulen
auch mit verwendet, aber die Testeingaben so ausgewählt, dass es voraussichtlich für das
Ergebnis nur auf das zu testende Modul ankommt.
[ENDTERM]

[TERM::Mutationstests|Mutation Testing]
Mutationstests sind eine Technik zur Bewertung der Qualität von Softwaretests. Dabei werden
absichtlich kleine Änderungen (Mutationen) am Quellcode vorgenommen, um zu prüfen, ob die
vorhandenen Tests diese Änderungen erkennen und fehlschlagen. Ziel ist es, Schwächen in den Tests
aufzudecken und sicherzustellen, dass sie robust genug sind, um Fehler im Code zu finden. Ein hoher
Anteil an erkannten Mutationen deutet auf gute Tests hin.
[ENDTERM]

## N

[TERM::Nameserver|Nameservers]
Ein Nameserver hat die Aufgabe, Webadresse in IP-Adressen zu übersetzen. Diese Übersetzung ist 
notwendig, weil Benutzer in der Regel leicht zu merkende Domainnamen (wie z.B. www.beispiel.de) 
verwenden, während Computer Netzwerke IP-Adressen (wie z.B. 192.0.2.1) benötigen, um die 
Kommunikation zu ermöglichen.
[ENDTERM]

[TERM::Negativtest|Negativszenario]
Ist eine Art von Softwaretest, der darauf abzielt, sicherzustellen, dass ein System korrekt auf
ungültige Eingaben oder unerwartete Bedingungen reagiert. Im Gegensatz zu Positivtests, die prüfen,
ob das System die erwarteten Ergebnisse auf gültige Eingaben liefert, testen Negativtests die
Handhabung von Fehlern oder ungültigen Daten.
[ENDTERM]

[TERM::Netzwerkport]
Ein Netzwerkport ist ein virtueller, logischer Punkt, an dem Netzwerkverbindungen beginnen und enden. 
Stellen Sie sich das, wie einen nummerierten Dock in einem geschäftigen Seehafen vor. 
So wie verschiedene Schiffe an bestimmten Docks ankommen, um bestimmte Arten von Fracht zu laden oder zu entladen, 
kommen Netzwerkdaten an bestimmten Ports an, um von bestimmten Anwendungen oder Diensten verarbeitet zu werden.

Wenn Ihr Computer Daten über ein Netzwerk sendet oder empfängt, verwendet er sowohl eine IP-Adresse, 
um das richtige Gerät zu finden, als auch eine Portnummer, um die richtige Anwendung auf diesem Gerät zu finden.

Es gibt 65536 Ports, die in drei Hauptkategorien unterteilt sind:

* **System Ports (0-1023):** Diese sind für gängige, weit verbreitete Dienste und Anwendungen reserviert. 
    Zum Beispiel verwenden Webbrowser typischerweise Port **80** für HTTP und Port **443** für HTTPS.
    Diese Ports sollten nicht genutzt werden, aber können mit Adminrechten geändert werden.
* **User Ports (1024-49151):** Diese können von Unternehmen oder Organisationen für ihre 
    spezifischen Anwendungen registriert werden. Diese sind frei nutzbar.
    [List von registrierten Ports](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Registered_ports)
* **Dynamic Ports (49152-65535):** Diese werden oft von Client-Programmen verwendet, 
    wenn sie eine Verbindung zu einem Dienst herstellen, oder von Anwendungen, die einen temporären 
    Port benötigen.
[ENDTERM]

## O

[TERM::OAOO|Once and only once]
Siehe [TERMREF::DRY].
[ENDTERM]

[TERM::Objekt-Code|Object-Code]
Als Objekt-Code wird Code in [TERMREF::Maschinensprache] bezeichnet, welcher
in [TERMREF2::Objekt-Datei::-en] enthalten ist.
[ENDTERM]

[TERM::Objekt-Datei|Object-File]
Eine Objekt-Datei ist eine Datei, welche Prozessoranweisungen in 
[TERMREF::Maschinensprache] enthält, selbst allerdings nicht ausführbar ist.
Objekt-Dateien werden von [TERMREF2::Übersetzer::-n] und
[TERMREF::Assemblierer] erzeugt und von [TERMREF2::Binder::-n]
weiterverarbeitet.
Dazu beinhalten Objekt-Dateien zusätzliche Metadaten.
[ENDTERM]

[TERM::OpenAPI|Swagger]
Ein Standard, der die Dokumentation
von RESTful APIs (Representational State Transfer) erleichtert.
Maschinenlesbare Beschreibung einer API, die Entwicklern ermöglicht, schnell
zu verstehen, welche Ressourcen verfügbar sind, welche
Parameter erwartet werden und welche Antworten zurückgegeben werden können.
[ENDTERM]

[TERM::Optionen|Option]
In Linux beziehen sich die Optionen zu Befehlen auf zusätzliche Parameter oder 
Argumente, die einem Befehl hinzugefügt werden können, um sein Verhalten zu 
steuern oder anzupassen. Diese Optionen ermöglichen es Benutzern, die 
Funktionalität eines Befehls auf verschiedene Weisen zu beeinflussen. Optionen 
werden in der Regel durch Buchstaben oder Wörter dargestellt und können durch 
Bindestriche oder doppelte Bindestriche eingeleitet werden.
Bei den meisten Befehlen geben die Optionen `-h` oder `--help` eine kurze Auflistung der meistgenutzten 
Optionen des Befehls.
Für Windows-Befehle ist es meistens die Option `/h`, die diese Hilfe anbietet.
[ENDTERM]

## P

[TERM::Pair Programming|Paarprogrammierung]
Eine agile Entwicklungsmethode, bei der zwei Entwickler gemeinsam an derselben Aufgabe arbeiten.
Gelungene Paarprogrammierung ist ein kontinuierlicher Dialog über Ideen, Vorschläge, Erkenntnisse
und Tätigkeiten, bei dem die Partner beim Denken ständig eng beieinander bleiben ("togetherness")
und deshalb schneller gute Ideen produzieren können und Denkfehler schneller und verlässlicher
aufdecken und lösen.

Paarprogrammierung wird in der professionellen Softwareentwicklung insbesondere dann benutzt,
wenn das Problem schwierig ist oder das Wissen von zwei Teammitgliedern zusammengeworfen werden muss.
In der Lehre ist es als motivierende und lernförderliche Verfahrensweise für vielerlei
Zwecke bekannt und als wirksam nachgewiesen.
[ENDTERM]

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

[TERM::PEP8|PEP 8|Python Enhancement Proposal 8]
Ist der offizielle Style-Guide für Python-Code. Sie wurde von Guido van Rossum, dem Schöpfer von
Python, sowie anderen führenden Entwicklern der Python-Community entwickelt. PEP 8 definiert eine
Reihe von Regeln und Best Practices für die Formatierung von Python-Code, um die Lesbarkeit zu
verbessern und eine konsistente und einheitliche Codebasis zu fördern.

Dokumentation: [HREF::https://peps.python.org/pep-0008/]
[ENDTERM]

[TERM::ping|Ping]
Ping ist ein Befehl, um die Erreichbarkeit einer anderen Ressource im Netzwerk zu überprüfen. Es 
sendet kleine Pakete an das Ziel und erwartet eine Antwort der Ressource. Die Antwortzeit und 
eventuelle Paketverluste werden gemessen, um die Netzwerkverbindung zu bewerten.
[ENDTERM]

[TERM::pip]
"Package installer for Python":
Das Programm, mit dem man üblicherweise externe Bibliotheken von einem entsprechenden
Server ("package index", meist wird pypi.org benutzt) lädt und installiert.

Dokumentation: [HREF::https://pip.pypa.io/en/stable/getting-started/]
[ENDTERM]

[TERM::Pipeline]
Das ist eine Abfolge von automatisierten Schritten oder Prozessen, die in einem
Workflow ausgeführt werden, um bestimmte Aufgaben oder Abläufe zu erledigen. Sie ermöglicht
die Automatisierung von komplexen Abläufen, indem sie verschiedene Schritte wie Builds, Tests,
Bereitstellungen und mehr integriert.
[ENDTERM]

[TERM::Pipes|Pipe]
Pipes dienen dazu, die Ausgabe einer Anwendung direkt als Eingabe für eine andere zu verwenden, 
ohne dass die Zwischenspeicherung in Dateien erforderlich ist. In Betriebssystemen wie Unix und 
Linux werden Pipes durch das vertikale Strichzeichen (|) dargestellt und ermöglichen die nahtlose 
Kommunikation zwischen verschiedenen Befehlen in der Kommandozeile.
[ENDTERM]

[TERM::Post Mortem|Post-Mortem-Analyse]
Eine Analyse, die nach Ende des zu analysierenden Ereignisses durchgeführt wird.
Dadurch lassen sich Vorfälle untersuchen, dokumentieren und zu Lernzwecken festhalten.
Sie hat keine feste Form, enthält aber in der Regel die Gründe für den Vorfall, die Lösung des 
Vorfalls und Nachbereitungen, die solche Vorfälle verhindern sollen.
[ENDTERM]

[TERM::Prompt]
Eine Textzeichenfolge, die in der Kommandozeile angezeigt wird, um den
Benutzer zur Eingabe eines Befehls aufzufordern. Sie enthält oft Informationen wie den
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

[TERM::Prüfsumme|Checksum]
Ergebnis einer (kryptografischen) [TERMREF::Hashfunktion], die auf Daten, z.B. in Form einer Datei, 
angewendet wurde.

Prüfsummen helfen dabei, die Integrität von Daten sicherzustellen. Hierfür wird eine Prüfsumme der
"originalen" Daten mit der Prüfsumme der vorhandenen Daten verglichen. Sind beide gleich, geht 
man davon aus, dass die Daten nicht verändert wurden, da es sehr unwahrscheinlich ist, dass zwei
unterschiedliche Dateien denselben Hash haben.
[ENDTERM]

[TERM::Public-Key-Kryptographie|Asymmetrische Kryptographie|Schlüsselpaar]
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

[TERM::Pull-Request|Merge-Request|PR|MR]
Ein Pull-Request ist ein Feature vieler git-Server welches, Nutzer_innen ermöglicht einfach 
Änderungsvorschläge zwischen zwei git-Branches zu vorzuschlagen, zu diskutieren und ggf. 
Änderungen vorzunehmen, um die bestmögliche Integrierung der Änderungen in die Haupt-Codebase zu 
gewährleisten. Im Pull-Request werden die Änderungen zwischen den Branches sowie eine Auflistung 
der Commits angezeigt. 
Weitere Informationen bietet [dieser GitHub-Artikel](https://docs.github.
com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-
requests/about-pull-requests).
[ENDTERM]

[TERM::PyCharm]
Leistungsfähige IDE von JetBrains, in die viel Spezialwissen über das Python-Universum 
eingebaut ist.
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

[TERM::redirect-Operator]
Die Verwendung des Operators kann die Ausgabe von Befehlen in Dateien umleiten, um Daten zu 
speichern oder zu protokollieren, sowie Eingabedaten aus Dateien lesen. Darüber hinaus ermöglicht 
der Redirect-Operator die Weiterleitung von Ausgaben an verschiedene Ziele wie andere Befehle, 
Netzwerkverbindungen oder Programme, was die Integration in komplexe Datenverarbeitungs- und 
Analyseworkflows erleichtert. 
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
[HREF::https://refactoring.com/].
[ENDTERM]

[TERM::Regressionstest]
Ein Regressionstest ist ein Typ von Softwaretest, der durchgeführt wird, um sicherzustellen,
dass früher funktionierende Teile einer Software nach einer Änderung weiterhin wie erwartet
funktionieren und somit unerwünschte Seiteneffekte schnellstmöglich erkannt werden.
[ENDTERM]

[TERM::Release]
In der Softwareentwicklung bezieht sich der Begriff Release auf die Veröffentlichung einer
bestimmten Version einer Softwareanwendung oder eines Softwareprodukts. Dabei ist ein Release stets
eindeutig zu kennzeichnen. Das wird mir einer Release-[TERMREF::Versionsnummer] durchgeführt.
Aber auch Releasebezeichner wie Alpha, Beta oder Stable-Version sind gängige praxis.
[ENDTERM]

[TERM::REPL]
REPL steht für eine "Read-Eval-Print-Loop", also die wiederholte Ausführung vom Auslesen einer
Eingabe des Benutzers, der Auswertung dieser Eingabe und dem Ausgeben des Ergebnisses.  
Wenn Sie `python` ohne weitere Argumente ausführen, landen Sie beispielsweise in einer solchen REPL
und können dort nach Belieben Code ausführen.
[ENDTERM]

[TERM::Request|Anfrage]
Nachricht, die im Rahmen eines [TERMREF2::Protokoll::-s] ein Client an einen Server sendet,
um Daten anzufordern oder eine Operation auszulösen.

Bei [TERMREF::HTTP] wird ein Request an eine spezifische _Ressource_ auf dem Server gesendet,
die durch einen URI/[TERMREF::URL] identifiziert wird.
[ENDTERM]

[TERM::Response|Antwort]
Die Daten, die im Rahmen eines [TERMREF2::Protokoll::-s]
ein Server an einen Client zurücksendet, als Reaktion auf eine [TERMREF::Anfrage],
die der Client zuvor gesendet hat.
Enthält den angeforderten Inhalt und/oder gibt Informationen darüber, ob die Anfrage erfolgreich war oder nicht.
[ENDTERM]

[TERM::Root-Nameserver]
Root-Nameserver sind zentrale Server im [TERMREF::DNS], die Informationen über die 
wichtigsten [TERMREF2::Top-Level-Domain::-s] (wie .com, .de oder .org) speichern. Sie stehen an der Spitze der 
DNS-Hierarchie und helfen dabei, DNS-Anfragen zu bearbeiten. 
Wenn ein DNS-Server die IP-Adresse einer Website nicht kennt, kann er einen Root-Nameserver 
anfragen, um die Adresse des zuständigen Nameservers für die nächste Ebene zu erhalten. 
Dieser Prozess ermöglicht es, die richtigen Webseiten im Internet zu finden.
[ENDTERM]

[TERM::RPA|Robotic Process Automation|Robotische Prozessautomatisierung]
Die Anwendung von Software-Robotern oder "Bots", um menschliche Aufgaben in Geschäftsprozessen
zu automatisieren. Diese Bots agieren in der Regel auf der Benutzeroberfläche von Anwendungen,
indem sie Aktionen ausführen, Daten erfassen, Entscheidungen treffen und mit anderen Systemen
interagieren, ähnlich wie es ein menschlicher Bediener tun würde.
[ENDTERM]

## S

[TERM::Schlüsselwort|Keyword]
Schlüsselwörter (Englisch: "keyword") nennt man reservierte Wörter oder Zeichenfolgen in Programmiersprachen.
Sie sind Teil der Sprachsyntax und haben eine vordefinierte Bedeutung, die in der Sprachbeschreibung
nachzulesen ist.
Das steht im Gegensatz zu Namen ("identifier") in Programmen, deren Bedeutung sich nicht aus der Programmiersprache
ergibt, sondern aus dem jeweiligen Programmtext.
Schlüsselwörter können nicht als Namen für Variablen oder Funktionen oder 
irgendwelche Elemente im Programm verwendet werden. 
[ENDTERM]

[TERM::Screenreader]
Ein Screenreader ist eine spezielle Software, die es Menschen mit Sehbehinderungen oder Blindheit ermöglicht, auf die Inhalte eines Computerbildschirms zuzugreifen. Der Screenreader liest den Text auf dem Bildschirm mittels synthetischer Sprache vor und/oder konvertiert ihn in Brailleschrift, die dann auf einer angeschlossenen Braillezeile angezeigt wird.
[ENDTERM]

[TERM::Serialisierung]
Ein Mechanismus, der sich auf den Prozess bezieht, bei dem Datenstrukturen in ein Format umgewandelt
werden, das für die Speicherung oder Übertragung geeignet ist. Im Falle von [TERMREF::JSON] bedeutet dies,
dass Datenstrukturen, wie zum Beispiel Objekte oder Arrays in einer Programmiersprache, in das
JSON-Format umgewandelt werden. Während der Serialisierung werden die Daten in eine Zeichenkette
konvertiert, die gemäß der JSON-Syntax strukturiert ist.
[ENDTERM]

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

[HREF::https://de.wikipedia.org/wiki/Kommandozeile]  
[HREF::https://de.wikipedia.org/wiki/Unix-Shell]
[ENDTERM]

[TERM::Shellfunktion|Shellprozedur]
Eine Prozedur, die in der [TERMREF::Unix-Shell] einmal definiert wird,
z.B. in [TERMREF::.bashrc] oder einem Shellskript,
und sich dann immer wieder aufrufen lässt.
Fasst mehrere Kommandos zu einem zusammen, ggf. auch mit Schleifen oder Fallunterscheidungen.
[ENDTERM]

[TERM::Slice (Golang)]
Ein Slice in Go ist eine dynamische Datenstruktur, die eine veränderbare Sequenz von Elementen gleichen Typs repräsentiert. 
Ein Slice besteht intern aus einem Zeiger auf ein zugrunde liegendes Array, einer Länge und einer Kapazität.
Grundsätzlich ist ein Slice eine "View" in das zugrunde liegende Array, welche dieses verändern darf.
Slices ermöglichen effizienten Zugriff auf Teilbereiche von Arrays und dienen als grundlegendes Werkzeug für die Verarbeitung von Datensammlungen in Go-Programmen. 
Sie werden mit der Notation `[]T` deklariert, wobei `T` den Elementtyp darstellt.

[HREF::https://go.dev/blog/slices-intro]
[ENDTERM]

[TERM::Slicing (Python)]
Slicing bezeichnet in Python das Auswählen eines Teilbereichs (Subsequenz) aus Sequenztypen wie Listen, Strings oder Tupeln. Die Syntax ist `seq[start:stop:step]`, wobei start (inklusive) der Startindex, stop (exklusiv) der Endindex und step die Schrittweite ist. Alle drei Parameter sind optional. Negative Indizes zählen vom Ende der Sequenz rückwärts.

[HREF::https://www.geeksforgeeks.org/python/python-list-slicing/]
[ENDTERM]

[TERM::Snapshot (git)]

Ein Snapshot ist das mentale Modell dafür, wie Git Inhalte speichert: 
anstatt nur Änderungen (Deltas) zu speichern, legt Git vollständige Abbilder aller getrackten 
Dateien zum Zeitpunkt eines Commits ab.

Diese Abbilder bestehen aus Verweisen auf [TERMREF::Blob]-Objekte, die in einem Tree-Objekt 
organisiert sind.

Ein Commit ist also nicht einfach nur eine Änderung, sondern eine vollständige Momentaufnahme 
des Projekts in diesem Zustand.
[ENDTERM]

[TERM::SOA|Start of Authority]
Der SOA-Record (Start of Authority) ist ein essenzieller Ressourceneintrag im Domain Name System 
(DNS), der die administrativen Parameter einer DNS-Zone definiert. Er dient als Kontrollzentrum 
für die Zonenverwaltung und ist entscheidend für die korrekte Funktion des Zonentransfers, bei dem 
DNS-Daten von einem primären zu sekundären Nameservern repliziert werden.
Der SOA-Record enthält detaillierte Informationen wie den primären Nameserver (MNAME), die 
E-Mail-Adresse des Zonenadministrators (RNAME) und eine Seriennummer (SERIAL), die bei jeder Zonenänderung 
inkrementiert wird, um sekundäre Nameserver über Aktualisierungen zu informieren.
[ENDTERM]

[TERM::SQL Injection]
Eine Angriffsmethode bei SQL Datenbanken, bei der durch geschickte Manipulation einer SQL Query 
Befehle auf der Datenbank ausgeführt werden können. Um solche Injections zu verhindern, 
sollten Vorkehrungen, wie die Bereinigung von User-Eingaben oder strikte Berechtigungsverwaltung,
getroffen werden.

[HREF::https://de.wikipedia.org/wiki/SQL-Injection]  
[HREF::https://xkcd.com/327/]
[ENDTERM]

[TERM::SSH]
Secure Shell (SSH) ist das meistgenutzte Protokoll, um sich auf entfernten Rechnern anzumelden. 
Es ermöglicht eine sichere Remote-Verwaltung und den Datenaustausch über unsichere Netzwerke, 
indem es Authentifizierung und Verschlüsselung verwendet.
[ENDTERM]

[TERM::SSH-Agent]
Ein SSH-Agent ist ein Programm, das deine SSH-Schlüssel verwaltet und sicher aufbewahrt. 
Es ermöglicht dir, dich mit Servern zu verbinden, ohne bei jeder Verbindung das Passwort für den 
Schlüssel erneut eingeben zu müssen. 
Der Agent speichert den Schlüssel während einer Sitzung im Speicher und sorgt so für mehr Komfort 
und Sicherheit.
[ENDTERM]

[TERM::Staging-Area|git-Index]
Die Staging Area, auch Index genannt, bezeichnet in git einen Zwischenspeicher, in dem neue Dateien,
Änderungen an bestehenden Dateien oder Löschungen vorgemerkt werden.
Dateien werden mit git add zur staging area hinzugefügt und können auch wieder entfernt werden.

Der Index funktioniert dabei wie, jetzt füge ich hier einige wörter ein eine Art Puffer oder
Merkzettel: Man bereitet damit gezielt vor, was im nächsten Commit landen soll.

Beim Erstellen eines git-Commits wird der Inhalt der Staging area zu einem Commit-Objekt
zusammengefasst und dauerhaft gespeichert.
Wichtig ist auch hierbei zu bedenken, dass git keine Änderungen speichert, sondern immer ein 
vollständiges Abbild (Snapshot) einer Datei anlegt.
Nachträgliche Änderungen an bestehenden Commits sind nicht ohne Weiteres möglich.
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

[TERM::Strategy Pattern|Strategie-Muster]
Das Strategy Pattern ist ein [TERMREF::Verhaltensmuster], das es ermöglicht, eine Familie von 
Algorithmen zu definieren, jeden von ihnen in eine separate Klasse zu setzen und ihre Objekte 
austauschbar zu machen.
[ENDTERM]

[TERM::su]
`su` steht für "Substitute User" und ist ein Befehl in Linux-Systemen, der es einem 
Benutzer ermöglicht, die Identität zu einem anderen Benutzer zu wechseln, normalerweise 
zum Superuser (Root), nach Eingabe des entsprechenden Passworts. Im Gegensatz zu `sudo` 
wechselt `su` vollständig zur Identität des anderen Benutzers und startet eine neue Shell.
Die dadurch veränderten Rechte bleiben aktiv, bis man die Shell beendet.
[ENDTERM]

[TERM::sudo]
`sudo` ist ein Befehl in Linux-Systemen, der es autorisierten Benutzern ermöglicht, 
vorübergehend erhöhte Rechte zu erhalten, um administrative Aufgaben auszuführen.
[ENDTERM]

[TERM::SUT|System Under Test]
Hierbei handelt es sich um ein Konzept in der Softwaretestung, das das System oder die Komponente
bezeichnet, die gerade getestet wird. Es ist das Hauptziel des Testprozesses und wird auf mögliche
Fehler, Schwachstellen oder Funktionsstörungen untersucht. Das SUT kann eine einzelne
Softwareanwendung, ein Modul, eine Funktion oder sogar ein gesamtes System umfassen.
[ENDTERM]

[TERM::Symlink|symbolischer Link]
Symbolische Links sind Verknüpfungen auf Dateien oder Verzeichnisse, die an einem anderen Ort ist, 
als die originale Datei. Sie bieten Flexibilität und ermöglichen es, auf Dateien oder 
Verzeichnisse zuzugreifen, unabhängig von ihrem physischen Speicherort.
[ENDTERM]

[TERM::Symmetrische Verschlüsselung]
Symmetrische Verschlüsselung ist ein Verfahren, bei dem der gleiche Schlüssel sowohl zum 
Verschlüsseln als auch zum Entschlüsseln von Daten verwendet wird. 
Sender und Empfänger müssen also denselben geheimen Schlüssel besitzen, um die verschlüsselten 
Informationen sicher austauschen zu können.
[ENDTERM]

[TERM::Systemtest|System Test]
Ein Test des Gesamtsystems unter Verwendung von dessen natürlichen Schnittstellen,
meist einem GUI.
Solche Tests sind aufwändig zu implementieren, brauchen komplizierte Testwerkzeuge,
laufen langsam und gehen beim Weiterentwickeln der Software häufig kaputt,
weil die GUI sich oft ändert.
[ENDTERM]


## T

[TERM::TCP]
TCP (Transmission Control Protocol) ist ein verbindungsorientiertes Netzwerkprotokoll, das den 
zuverlässigen Datenaustausch zwischen zwei Endgeräten über ein IP-Netzwerk gewährleistet. 
Bevor Daten gesendet werden, baut TCP eine stabile Verbindung zwischen Sender und Empfänger auf. 
Während der Übertragung teilt es die Daten in kleine Pakete auf, überprüft, ob diese korrekt 
angekommen sind, und stellt sicher, dass sie in der richtigen Reihenfolge zusammengesetzt werden. 
Geht ein Paket verloren oder wird beschädigt, fordert TCP dessen erneute Übertragung an. 
So wird eine vollständige und fehlerfreie Datenübertragung sichergestellt.
[ENDTERM]

[TERM::TDD|Test-Driven Development|Test-Driven Design|Testgetriebener Entwicklung]
Eine Softwareentwicklungsmethode, bei der [TERMREF2::Test::-s] vor der eigentlichen Implementierung
des Codes geschrieben werden. Der Prozess beginnt mit dem Schreiben eines Tests, der das
erwartete Verhalten der Funktionalität beschreibt. Dann wird der minimal notwendige Code
implementiert, um den Test erfolgreich durchzuführen. Dieser iterative Prozess von Schreiben
von Tests, Implementieren des Codes wird fortgesetzt, bis die gewünschte Funktionalität erreicht ist.
[ENDTERM]

[TERM::tee]
Der Unix-Befehl `tee` liest die Standardeingabe und schreibt sie sowohl in die Standardausgabe als 
auch in eine oder mehrere Dateien. Er wird oft verwendet, um die Ausgabe eines Befehls zu speichern 
und gleichzeitig anzuzeigen.
[ENDTERM]

[TERM::Test]
Das Ausprobieren von Software, um relevante Eigenschaften zu überprüfen;
meistens die Frage, ob die Software korrekte Ergebnisse liefert (Defekttest).
[ENDTERM]

[TERM::Testiteration]
Eine Testiteration bezieht sich auf einen Zyklus oder eine Runde von Testaktivitäten, die
durchgeführt werden, um bestimmte Aspekte einer Software zu überprüfen oder zu testen. Während
einer Testiteration wird ein Testfall mit einem festen Satz an Testdaten ausgeführt. Dieser
Testfall wird oftmals n-Mal ausgeführt, jedoch mit unterschiedlichen Werten ausgeführt. Das erhöht
die Testabdeckung mit minimalem Testerstellungsaufwand.
[ENDTERM]

[TERM::Testsammlung|Testsuite]
bezeichnet eine Sammlung von Testfällen, die dazu dienen, verschiedene Aspekte einer Softwareanwendung
zu testen, indem unterschiedliche Funktionen oder Eigenschaften der Software getestet werden. Diese
Sammlungen enthalten i.d.R. mehrere Testfälle und werden chronologisch durchgeführt.
[ENDTERM]

[TERM::Testszenario]
Hierbei handel es sich um eine detaillierte Beschreibung eines spezifischen Testfalls oder einer
Testsequenz, die darauf abzielt, eine bestimmte Funktionalität oder ein bestimmtes Verhalten einer
Software zu überprüfen. Ein Testszenario umfasst normalerweise eine Reihe von Schritten, die
ausgeführt werden müssen, um das gewünschte Ergebnis zu erzielen, sowie die erwarteten Ergebnisse
oder Verhaltensweisen der Software.
[ENDTERM]

[TERM::Time-Based One-Time Password|TOTP]
Dabei handelt es sich um ein zeitbasiertes, einmalig verwendbares Passwort, das oft in der
Zwei-Faktor-Authentifizierung (2FA) verwendet wird. Bei TOTP generiert eine Anwendung wie Google
Authenticator oder eine ähnliche App in regelmäßigen Intervallen (typischerweise 30 Sekunden) ein
neues Passwort basierend auf einem geheimen Schlüssel und der aktuellen Zeit. Dieses Passwort wird
dann für die Authentifizierung verwendet.
[ENDTERM]

[TERM::Top-Level-Domain]
Top-Level-Domains (TLDs) sind die letzten Teile einer Internet-Domain, die nach dem letzten Punkt 
in einer Webadresse erscheinen, wie z. B. .com, .org oder .de. 
Sie werden in zwei Hauptkategorien unterteilt: generische TLDs (gTLDs), die allgemein verwendet 
werden und keine speziellen Anforderungen haben, und länderspezifische TLDs (ccTLDs), die für 
bestimmte Länder oder Regionen stehen (z. B. .fr für Frankreich oder .jp für Japan). 
TLDs helfen, die Art und den Standort einer Website zu identifizieren und sind ein wichtiger 
Bestandteil des Domain Name Systems (DNS).
[ENDTERM]

[TERM::traceroute|Traceroute]
Der Unix-Befehl `traceroute` zeigt den Pfad an, den Datenpakete durch ein Netzwerk nehmen, um ein 
Ziel zu erreichen. Es listet die einzelnen Hops (Zwischenstationen) auf, die die Pakete durchlaufen, 
und misst die Antwortzeit zu jedem Hop. Dies ist nützlich, um Netzwerkprobleme zu diagnostizieren 
oder die Route zu einem Server zu analysieren.
[ENDTERM]

[TERM::Transaktion|transaction]
Eine Bündelung von mehreren Aktionen auf einer Datenbank. Nur bei erfolgreicher Durchführung 
aller Aktionen wird die Änderung auf die Datenbank geschrieben (Commit), andernfalls werden alle 
Änderungen rückgängig gemacht (Rollback). So wird die Konsistenz der Datenbank sichergestellt.

[HREF::https://www.datenbanken-verstehen.de/datenbank-grundlagen/dbms/datenbank-tansaktion/]
[ENDTERM]

[TERM::Transportprotokoll]
Ein Transportprotokoll ist ein Kommunikationsprotokoll, das den sicheren und zuverlässigen 
Austausch von Daten zwischen zwei Geräten in einem Netzwerk ermöglicht. 
Es sorgt dafür, dass die Daten korrekt und in der richtigen Reihenfolge ankommen, und verwaltet 
die Verbindungen zwischen den Geräten. Drei der bekanntesten Transportprotokolle sind [TERMREF::TCP] 
(Transmission Control Protocol), das eine zuverlässige Verbindung mit Fehlerkorrektur bietet, 
[TERMREF::UDP] (User Datagram Protocol), das schnellere, aber unzuverlässige Datenübertragungen 
ermöglicht und [TERMREF::ICMP] (Internet Control Message Protocol), welches für den Austausch von 
Steuer- und Fehlermeldungen im Internet verwendet wird.
Transportprotokolle spielen eine entscheidende Rolle bei der Gewährleistung der Datenintegrität 
und -effizienz im Internet.
[ENDTERM]

[TERM::TUI|Text-based User Interface]
Terminal-basierte Bedienschnittstelle, die mit Tastatur und Cursor benutzt wird.  
Wichtiger Spezialfall ist das [TERMREF::CLI].  
Gegensatz ist das [TERMREF::GUI].

[HREF::https://en.wikipedia.org/wiki/Text-based_user_interface]
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

[TERM::UDP]
UDP (User Datagram Protocol) ist ein schnelles, verbindungsloses Netzwerkprotokoll, das Daten ohne 
vorherige Verbindung zwischen Sender und Empfänger versendet. 
Es bietet keine Fehlerkorrektur, das bedeutet, dass Pakete verloren gehen oder in falscher 
Reihenfolge ankommen können, ohne dass sie neu gesendet werden.
[ENDTERM]

[TERM::Umgebungsvariable|Umgebungsvariablen|environment variable]
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

[HREF::https://de.wikipedia.org/wiki/POSIX]  
[HREF::https://de.wikipedia.org/wiki/Unix]
[ENDTERM]

[TERM::Urgrund|root cause|Urgrundanalyse|root cause analysis|Grundursachen-Analyse]
Eine Urgrundanalyse (Grundursachen-Analyse, root cause analysis) geht so:
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

[TERM::URL|URI]
Ein URL (Uniform Resource Locator) bzw. URI (Uniform Resource Identifier), wie es eigentlich offiziell
(aber weniger gebräuchlich) heißt,
ist die Adresse einer Ressource im Internet, etwa einer Webseite oder einer Datei. 
Ein URL besteht aus mehreren Teilen, 
darunter das Protokoll ("scheme", z.B. "http" oder "https"), 
der Domainname (z.B. "www.example.org"), 
möglicherweise ein Pfad zu einer spezifischen Seite oder Datei innerhalb der Website
(z.B. "/some/path/to/file.html") und
möglicherweise Anfrageparametern
("query", z.B. "?a=1&b=user").
URLs ermöglichen es [TERMREF::HTTP]-Klienten (z.B. Webbrowsern), Web-Ressourcen zu bezeichnen (zu "adressieren").
[ENDTERM]

[TERM::User Story|Userstory]
Kurze, informelle Beschreibung einer Funktion aus der Perspektive eines Endbenutzers.
Umfasst meist mindestens, wer die Funktion nutzt, was getan werden soll und wozu es relevant ist.

User Stories dienen als Kommunikationsmittel zwischen Entwicklern, Kunden und anderen Stakeholdern,
um Anforderungen klar zu definieren und das Verständnis zu verbessern.
Oft werden begleitend [TERMREF::Akzeptanzkriterien] definiert.
[ENDTERM]

## V

[TERM::Validierung]
Bestätigung durch Überprüfung, dass ein Arbeitsergebnis den Bedürfnissen eines Stakeholders entspricht.

[HREF::https://glossary.istqb.org/de_DE/term/validierung-1]
[ENDTERM]

[TERM::venv|virtualenv|virtual environment]
Virtuelle Python-Umgebung:
Ein Dateibaum, der konzeptuell eine eigene Installation von Python enthält
sowie einen eigenen Unterdateibaum für installierte Pakete.

Wird ein `venv` aktiviert, was mittels `source myvenv/bin/activate` geschieht,
wird das Python-[TERMREF::Executable] des `venv` zuvorderst in den
[TERMREF::PATH] geschrieben und benutzt dann die installierten Pakete des `venv`
anstatt (oder anstatt nur) der global installierten.

Der `venv`-Mechanismus erlaubt, für mehrere Python-Projekte, an denen man abwechselnd entwickelt,
separate Mengen installierter Pakete zu haben und bei Bedarf auch unterschiedliche Versionen
von Python selbst, sodass es insbesondere keine Probleme macht, falls verschiedene Projekte
das gleiche Paket X in unterschiedlichen Versionen benötigen.
[ENDTERM]

[TERM::Verifizierung|verifizieren]
Verifizierung oder Verifikation (von lateinisch veritas "Wahrheit" und facere "machen") ist
die Bestätigung durch Bereitstellung eines objektiven Nachweises, dass festgelegte
Anforderungen erfüllt worden sind.

[HREF::https://glossary.istqb.org/de_DE/term/verifizierung]  TODO_2_ruhe/prechelt: AchduliebeGüte!
[ENDTERM]

[TERM::Versagen|Failure|Symptom]
Falsches Verhalten eines Programms relativ zur
Spezifikation, der Anforderung oder den Erwartungen.
Ist ein Symptom eines [TERMREF2::Defekt::-s].
[ENDTERM]

[TERM::Versionsnummer|Versionierung]
Versionsnummern folgen in der Regel einem bestimmten Schema, das je nach den Anforderungen des
Projekts und den Praktiken des Entwicklungsteams variieren kann. Ein gängiges und weit
verbreitetes Schema ist das MAJOR.MINOR.PATCH-Schema. Gemeinsam haben aber alle, dass sie
Entwicklern und Benutzern ermöglichen, den Entwicklungsstand und die Stabilität einer
Softwareanwendung aufgrund ihrer Eindeutigkeit schnell erkennen.
[ENDTERM]

## W

[TERM::Werkzeugkette|Toolchain]
Eine Sammlung an Programmen und Skripten zur Erzeugung eines Produktes.
Beispiele: GCC, Clang, MSVC, aber auch [TERMREF::IDE]s können Bestandteil einer
Werkzeugkette sein.
[ENDTERM]

[TERM::WET|Write every time|Write everything twice]
Das Gegenteil zu [TERMREF::DRY].  
Während WET nicht als allgemein zu verfolgendes Prinzip gilt, 
ist es in Einzelfällen sehr wohl eine gute Variante, um Code 
lesbarer und wartbarer zu machen.
[ENDTERM]

## X

[TERM::xargs]
`xargs` nimmt die Standardeingabe (z.B. eine Liste von Dateinamen) und führt damit einen weiteren yBefehl 
aus. Es ist nützlich, um lange Listen von Argumenten zu verarbeiten, die sonst die Befehlszeilenlänge 
überschreiten würden.
[ENDTERM]

[TERM::XML]
XML (eXtensible Markup Language) ist eine [TERMREF::Auszeichnungssprache] zur Darstellung
hierarchisch strukturierter Daten in einem menschenlesbaren Format. Entwickelt
wurde XML, um strukturierte Daten zwischen Computersystemen austauschen zu können.
Genau wie [TERMREF::JSON] ist XML nicht auf eine bestimmte Programmiersprache
beschränkt und kann in einer Vielzahl von Anwendungen und Kontexten eingesetzt werden.
[ENDTERM]

## Y
## Z

[TERM::Zwischensprache]
Eine Zwischensprache ist eine, der [TERMREF::Maschinensprache] nähere,
Sprache.  
Zwischensprachen werden häufig eingesetzt, um ein Programm in einer
[TERMREF::Hochsprache] zu verfassen und auf mehreren unterschieldlichen
Prozessorarchitekturen (und somit Maschinensprache) auszuführen,
ohne dabei das Programm erneut zu übersetzen.  
Ein sehr bekanntes Beispiel ist hier Java (die Hochsprache), welches als
Java-Bytecode (die Zwischensprache) mittels der JVM (Quasi-Interpreter)
ausgeführt wird.
Hierbei muss nur die JVM in der, für die gewünschten Prozessorarchitektur,
Maschinensprache vorhanden sein.
[ENDTERM]