title: pip, der Paketmanager von Python
stage: alpha
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
Sehr viele davon sind Open Source und also frei verfügbar und benutzbar.

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

### `pip install`

1. Überzeugen Sie sich davon, dass das Paket `colorama` _nicht_ installiert ist:
   `python -c "import colorama"`
   (Wie üblich gilt: Selbereintippen verbessert den Lernerfolg _erheblich_.)
2. Rufen Sie `pip install colorama=0.4.4` auf, um die Version 0.4.4 von `colorama`
   zu installieren.
3. Überzeugen Sie sich davon, dass das Paket `colorama` nun installiert ist:
   `python -c "import colorama"`.
4. Lesen Sie kurz nach, [wozu colorama dient](https://pypi.org/project/colorama/),
   und geben Sie ein Wort in Rot aus:  
   `python -c "import colorama as c; print('Ich bin ein' + c.Fore.RED + ' rotes ' + c.Style.RESET_ALL + 'Wort')"`


### `pip freeze`

5. Betrachten Sie die Liste installierter Pakete: `pip freeze`.
   Hätte colorama Abhängigkeiten gehabt, also weitere Pakete, die installiert sein müssen,
   damit colorama funktionieren kann, dann wären diese mit installiert worden
   und die Liste hätte mehrere Einträge.


### `pip install --upgrade`

6. Meist gibt man beim Installieren von Paketen keine Versionsnummer an und
   bekommt dann die aktuellste Version.
   Obige Version 0.4.4 ist für colorama nicht die aktuellste.
   Benutzen Sie pip, um die Installation zu aktualisieren:
   `pip install --upgrade colorama`
7. Überzeugen Sie sich vom geänderten Stand: `pip freeze`.


### `pip show`

8. pip kann auch ein paar Metadaten über ein installiertes Paket anzeigen,
   darunter eine (meist _sehr_ kurze) Kurzbeschreibung.
   Bitte ausprobieren:
   `pip show colorama`


### `pip uninstall`

9. Wenn man ein Paket nicht mehr braucht (oft, weil man es nach dem Ausprobieren
   doch nicht einsetzen möchte), sollte man es wieder deinstallieren,
   damit die Paketliste verständlich bleibt.
   Auch das probieren wir jetzt aus:
   `pip uninstall colorama`
10. Und wieder das Ergebnis ansehen: `pip freeze`

[WARNING]
Falls Sie PyCharm Community Edition unter Windows benutzen, dann verwenden Sie zwei
Python-Interpretierer: Einen unter WSL in der Shell, einen anderen unter PyCharm.
Wenn die sich beide gleich verhalten sollen (und das sollen sie natürlich),
dann braucht der unter PyCharm die gleichen pip-Pakete wie der unter WSL.

Sie müssen also jede Installation eines Python-Pakets mit `pip`, die Sie in der Shell vornehmen, 
in PyCharm von Hand nachvollziehen.
Das geht am einfachsten, wenn Sie die Paketnamen in eine Datei `requirements.txt`
in Ihrem Arbeitsverzeichnis eintragen, denn dann bietet PyCharm die Installation von
alleine an (am oberen Rand).

Bei einem richtig aufgesetzten PyCharm Professional
(das direkt mit einem WSL-`venv` arbeitet) tritt das Problem nicht auf.
Bei einem PyCharm (egal ob Community oder Professional), das direkt auf
Linux oder MacOS arbeitet (also in deren Fenstersystem), tritt es ebenfalls nicht auf.
[ENDWARNING]

[ENDSECTION]
[SECTION::submission::trace]

Geben Sie die Eingaben und Ausgaben der obigen Kommandos ab.

[ENDSECTION]

[INSTRUCTOR::Passt alles zusammen?]
Protokoll bitte auf Schlüssigkeit kontrollieren.
Wenn eine Ausgabe nicht zu den vorangegangenen Kommandos passt, die Abgabe zurückweisen.
[ENDINSTRUCTOR]
