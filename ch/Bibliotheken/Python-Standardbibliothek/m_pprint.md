title: pprint - Daten leserlich formatiert ausgeben
stage: beta
timevalue: 1.0
difficulty: 2
explains:
assumes: m_json2, encoding-and-open
requires:
---
[SECTION::goal::trial]

Ich weiß, wie ich auch komplexere Datensätze über die Kommandozeile lesbar formatiert ausgeben kann.

[ENDSECTION]

[SECTION::background::default]

Daten über die Kommandozeile auszugeben ist wohl eines der grundlegendsten Features jeder Programmiersprache und
meistens das Erste, was man beim Erlernen einer neuen Programmiersprache lernt (HelloWorld). Möchte man aber komplexere
Datenstrukturen ausgeben, kann ein simpler `print()`-Befehl schnell unleserlich werden und das manuelle Formatieren der
Datenstruktur ist repetitiv und zeitaufwändig. Daher bietet die Standardbibliothek mit `pprint` (Pretty Print) ein Tool,
dass einem im Alltag einiges an Zeit und Arbeit sparen kann.

[ENDSECTION]

[SECTION::instructions::detailed]

### Vorbereitungen

- Legen Sie die Datei `m_pprint.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. 
  Fügen Sie ihre Python-Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile 
  getrennt.
- Kopieren Sie den folgenden Code-Block und speichern diesen in einer JSON-Datei im selben 
  Verzeichnis.  
```json
[INCLUDE::m_pprint_input.json]
```

### Unterschied von `print()` und `pprint`

- [ER] Importieren sie die Daten aus der JSON-Datei in ihrem Code mithilfe der `json`-Bibliothek.
- [EQ] Geben Sie das Objekt `data` zuerst einmal mit `print()` aus (Die Ausgabe soll nicht ins 
  Kommandoprotokoll). Finden Sie, die Ausgabe ist sinnvoll lesbar?
- [EQ] Beschreiben Sie, wie eine Funktion aussehen könnte, die mithilfe von `print()` eine besser 
  lesbare Ausgabe erzeugt. (nur beschreiben, nicht implementieren). Welche Herausforderungen 
  könnten dabei auftreten?
- [ER] Finden Sie in der [Dokumentation von pprint](https://docs.python.org/3/library/pprint.html) 
  eine Funktion, mit der Sie `data` lesbar formatiert ausgeben können. Rufen Sie sie auf:  
```python
print("pretty print:")
...
```

### `PrettyPrinter`-Objekte

Anstatt die Print-Funktion jedes Mal über das Modul selbst aufzurufen, kann ein eigenes
[`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)-Objekt 
erzeugt werden.  
Der Vorteil: Wenn dem Konstruktor die korrekten Parameter übergeben werden, müssen diese nicht 
bei jedem print erneut mit angegeben werden, sondern werden im Objekt gespeichert.

- [ER] Erzeugen Sie ein `PrettyPrinter`-Objekt. Dieses soll immer um vier Leerzeichen einrücken und 
  Verschachtelungen nicht detailliert ausgeben. Außerdem sollen Dictionaries in ihrer originalen 
  Sortierung gelassen werden.
- [ER] Geben Sie mit ihrem `PrettyPrinter` das zweite und vierte Element von `data` aus:  
```python
print("\nwith PrettyPrinter object:")
...
```

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_pprint.py` einmal aus.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch von `pprint` machen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_pprint.py]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
