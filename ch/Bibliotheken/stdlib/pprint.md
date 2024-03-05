title: pprint - Daten leserlich formatiert ausgeben
stage: draft
timevalue: 0.5
difficulty: 2
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::trial]

Ich weiß, wie ich auch komplexere Datensätze über die Kommandozeile lesbar formatiert ausgeben kann.

[ENDSECTION]

[SECTION::background::default]

Daten über die Kommandozeile auszugeben ist wohl eines der grundlegendsten Features jeder Programmiersprache und
meistens das Erste, was man beim Erlernen einer neuen Programmiersprache lernt (HelloWorld). Möchte man aber komplexere
Datenstrukturen ausgeben kann ein simpler `print()`-Befehl schnell unleserlich werden, und das manuelle Formatieren der
Datenstruktur ist repetitiv und zeitaufwändig. Daher bietet die Standardbibliothek mit `pprint` (Pretty Print) ein Tool,
dass einem im Alltag einiges an Zeit und Arbeit sparen kann.

[ENDSECTION]

[SECTION::instructions::detailed]

- Legen Sie die Datei `pprint.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. Fügen Sie ihre Python
  Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.
- Laden Sie die Datei [PARTREF::pprint.zip] herunter und entpacken Sie sie in dasselbe Verzeichnis.
- Importieren sie die Daten aus der JSON-Datei in ihrem Code folgendermaßen:

```python
import json

with open('pprint.json') as f:
  data = json.load(f)
f.close()
```  
  Auf JSON-Dateien und die `with open(...)`-Syntax gehen wir hier nicht genauer ein. Hierfür können Sie sich die
  Aufgaben [PARTREF::jsonBasic], [PARTREF::jsonExercise] und [PARTREF::open] anschauen.

### Unterschied von `print()` und `pprint`

- Geben Sie das Objekt `data` zuerst einmal mit `print()` aus (Die Ausgabe muss nicht ins Kommandoprotokoll). Finden
  Sie, die Ausgabe ist sinnvoll lesbar?
- [EQ] Überlegen Sie, wie eine Funktion aussehen könnte, die mithilfe von `print()` eine besser lesbare Ausgabe erzeugt.
  (nur überlegen, nicht implementieren). Welche Herausforderungen könnten dabei auftreten?
- Finden Sie in der [Dokumentation von pprint](https://docs.python.org/3/library/pprint.html) eine Funktion, mit der sie
  `data` mithilfe der Bibliothek ausgeben können. Fügen Sie hinter ihrem Befehl den Kommentar `# Antwort 1` ein.

### `PrettyPrinter`-Objekte

- Anstatt die Print-Funktion jedes Mal über das Modul selbst aufzurufen, kann ein eigenes
  [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)-Objekt erzeugt werden.  
  Der Vorteil: Wenn dem Konstruktor die korrekten Parameter übergeben werden, müssen diese nicht bei jedem print erneut
  mit angegeben werden, sondern werden im Objekt gespeichert.
- Erzeugen Sie ein `PrettyPrinter`-Objekt. Dieses soll immer um vier Leerzeichen einrücken und Verschachtelungen nicht
  detailliert ausgeben. Außerdem sollen Dictionaries in ihrer originalen Sortierung gelassen werden.
- Geben Sie mit ihrem `PrettyPrinter` das zweite und vierte Element von `data` aus. Fügen Sie hinter ihren Befehlen den
  Kommentar `# Antwort 2` ein.

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `pprint.py` einmal aus.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `pprint` machen.

[ENDINSTRUCTOR]
