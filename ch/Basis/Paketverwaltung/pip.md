title: pip, der Paketmanager von Python
stage: beta
timevalue: 0.5
difficulty: 2
explains: pip
requires: venv
---
[SECTION::goal::trial]
Ich weiß, wozu `pip` dient, und kann es benutzen.
[ENDSECTION]


[SECTION::background::default]
Auch wenn die Standardbibliothek von Python recht umfangreich ist,
braucht man doch sehr schnell weitere Bausteine jenseits der Standardbibliothek.
Sehr viele davon sind Open Source und damit frei verfügbar und benutzbar.

In der Python-Welt ist es üblich, Open-Source-Bibliotheken 
(und Frameworks und auch ganze Anwendungen, all dies wird "Paket" genannt) 
auf PyPI abzulegen, dem "Python Package Index":
[pypi.org](https://pypi.org).

Der Paketmanager `pip` kann 

- ein Python-Paket von PyPI (oder einem anderen Paketserver) holen,
- installieren (systemweit, benutzerspezifisch oder in ein `venv`),
- kann das installierte Paket wieder entfernen oder
- die Installation auf eine andere Version des Pakets aktualisieren
- und kann die installierten Pakete samt Versionsnummern auflisten.

`pip` ist selber auch ein PyPI-Paket und kann sich auch selbst aktualisieren.
[ENDSECTION]


[SECTION::instructions::loose]

[NOTICE]
Wer `pip` schon gut kennt, kann diese Aufgabe überspringen.
[ENDNOTICE]

Vergewissern Sie sich vor Beginn der Aufgabe, dass ihr `venv` aktiviert ist, sodass Pakete nur in ihrem virtuellen
Environment installiert werden.

### `pip install`

[EC] Überzeugen Sie sich davon, dass das Paket `colorama` _nicht_ installiert ist:  
`python -c "import colorama"`  
(Wie üblich gilt: Selber eintippen verbessert den Lernerfolg _erheblich_)

[EC] Rufen Sie `pip install colorama==0.4.4` auf, um die Version 0.4.4 von `colorama` zu installieren.

[EC] Überzeugen Sie sich davon, dass das Paket `colorama` nun installiert ist:  
`python -c "import colorama"`

[EC] Lesen Sie kurz nach, [wozu colorama dient](https://pypi.org/project/colorama/), und geben Sie ein Wort in Rot aus:  
`python -c "import colorama as c; print('Ich bin ein' + c.Fore.RED + ' rotes ' + c.Style.RESET_ALL + 'Wort')"`


### `pip freeze`

[EC] Betrachten Sie die Liste installierter Pakete:
`pip freeze`  
Hätte colorama Abhängigkeiten gehabt, also weitere Pakete, die installiert sein müssen,
damit colorama funktionieren kann, dann wären diese mit installiert worden
und die Liste hätte mehrere Einträge.


### `pip install --upgrade`

[EC] Meist gibt man beim Installieren von Paketen keine Versionsnummer an und bekommt dann die aktuellste Version.
Obige Version 0.4.4 ist für colorama nicht die aktuellste.
Benutzen Sie pip, um die Installation zu aktualisieren:  
`pip install --upgrade colorama`

[EC] Überzeugen Sie sich vom geänderten Stand:  
`pip freeze`


### `pip show`

[EC] pip kann auch ein paar Metadaten über ein installiertes Paket anzeigen,
darunter eine (meist _sehr_ kurze) Kurzbeschreibung.
Bitte ausprobieren:  
`pip show colorama`


### `pip uninstall`

[EC] Wenn man ein Paket nicht mehr braucht (z.B. weil man es nach dem Ausprobieren
doch nicht einsetzen möchte), sollte man es wieder deinstallieren,
 damit die Paketliste verständlich bleibt.
Auch das probieren wir jetzt aus:  
`pip uninstall colorama`

[EC] Und wieder das Ergebnis ansehen:  
`pip freeze`

### `requirements.txt`

Je größer das Projekt wird, an dem Sie arbeiten, desto mehr zusätzliche Pakete werden Sie in der Regel benötigen. 
Das kann schnell unübersichtlich werden, beispielsweise wenn Sie ihr Projekt auch auf einem anderen 
System einrichten wollen. 
Um zu dokumentieren, von welchen Paketen ihr Projekt abhängig ist, wird standardmäßig die Datei
`requirements.txt` verwendet.  
`pip` kann sowohl verwendet werden, um alle installierten Pakete in die Datei zu schreiben, als auch um alle benötigten
Pakete im Environment zu installieren.

Legen Sie die Datei `requirements.txt` in ihrem Repo an und fügen Sie `colorama` in eine Zeile ein.

[EC] Installieren Sie die Abhängigkeiten aus `requirements.txt`:  
`pip install -r requirements.txt`

[EC] Der Output von `pip freeze` kann auch direkt zur Erstellung der Textdatei verwendet werden.
Überschreiben Sie ihre aktuelle Textdatei:  
`pip freeze > requirements.txt`

[EC] Geben Sie den Inhalt der Datei mit `cat requirements.txt` aus.  
Die Datei enthält nun noch zusätzlich die Versionsnummer des Pakets. 
Die Angabe ist optional, kann aber helfen,
falls nicht alle Versionen eines Pakets mit ihrem Projekt kompatibel sind.

**Tipp:** Viele IDEs unterstützen die Verwendung von `requirements.txt` und bieten automatisch die Installation
benötigter Pakete im eingerichteten `venv` an.

Sie können, wenn Sie es aufgeräumt mögen, `colorama` nach Fertigstellung der Aufgabe wieder 
deinstallieren und aus der `requirements.txt` entfernen,
sofern es nicht von einer anderen Aufgabe benötigt wird.
[ENDSECTION]


[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]


[INSTRUCTOR::Passt alles zusammen?]
[PROT::ALT:pip.prot]
[ENDINSTRUCTOR]
