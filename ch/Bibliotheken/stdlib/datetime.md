title: datetime - Datum, Uhrzeit und Zeitdifferenzen
stage: alpha
timevalue: 1.0
difficulty: 2
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::trial]

- Ich weiß, wie man in Python Zeit- und Datumswerte erstellt, ausgibt und diese miteinander verrechnet.
- Ich kenne außerdem den Unterschied zwischen aware und naive datetime.

[ENDSECTION]

[SECTION::background::default]

Das Arbeiten mit Zeit- und Datumsangaben ist in vielen Anwendungen essenziell. Eine dafür geeignete Datenstruktur
selbst zu erstellen ist jedoch aufwändiger, als man zuerst annehmen würde. Neben verschiedenen Formaten (z.B.
amerikanische und deutsche Datumsschreibweise) muss diese auch verschiedene Zeitzonen und auch Sommerzeiten mit 
berücksichtigen können. Die `datetime` Bibliothek bietet einige Werkzeuge, um mit den meisten dieser Anwendungsfälle
umgehen zu können. 

[ENDSECTION]

[SECTION::instructions::detailed]

- Legen Sie die Datei `datetime.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. Fügen Sie ihre Python
  Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.

### `import datetime as dt`

- Der Modulname `datetime` ist länger als die meisten in der Standardbibliothek.
  Außerdem gibt es darin eine Klasse, die ebenfalls `datetime` heißt: verwirrend.
- Deshalb importieren wir per Konvention das Modul stets so:  
  `import datetime as dt`
- Das Konstrukt `from datetime import *` is generell nicht zu empfehlen,
  weil man dann leicht etwas importiert, dass einen anderen Import überdeckt.
  Der Code wird auch schwerer lesbar.

### Zeit-Objekte anlegen und ausgeben

- Finden Sie in der [Dokumentation](https://docs.python.org/3/library/datetime.html), wie man die aktuelle lokale Zeit abfragt und geben diese mit
  `print(...) # Antwort 1` aus.  
  Falls Sie angesichts des Umfangs der Doku dabei verzweifeln:
  So etwas geht mit einer Web-Suche oft schneller. Allerdings muss man sich dann vor irreführenden oder veralteten
  Antworten in Acht nehmen und sollte die Information in der aktuellen Dokumentation nachprüfen.
- Legen Sie nun ein `datetime`-Objekt an, welches den Zeitpunkt `01.12.2024, 13:09 Uhr` repräsentiert.
- Finden Sie eine Funktion, mit der Sie das oben angelegte `datetime`-Objekt als String im folgenden Format ausgeben
  können:  
  `Sonntag, der 01. Dezember 2024, 13:09 Uhr`  
  Geben Sie das Ergebnis der Funktion mit `print(...) # Antwort 2` aus.  
  Falls das nur fast klappt und Sie bekommen Monat und Wochentag in einer anderen Sprache,
  ist bei Ihnen eine andere "Locale" (Gebietsschema) eingestellt.
  Lesen Sie beim Modul `[locale](https://docs.python.org/3/library/locale.html)`
  nach, was es damit auf sich hat - aber wir lösen das jetzt hier nicht, Ihre Ausgabe ist OK wie sie ist.

### Zeiten einlesen

- Finden Sie heraus, wie der umgekehrte Weg funktioniert: Strings in `datetime`-Objekte wandeln.
- Wandeln Sie folgenden String: `2024-12-15##13:09:44` in ein `datetime`- Objekt um und geben Sie das Ergebnis aus mit
  `print(...)  # Antwort 3`.

### Zeitzonen

- Lesen Sie in der [Dokumentation](https://docs.python.org/3/library/datetime.html) die Konzepte "naive" (naiv) und "aware" (gewahr) nach.
- Ist Ihr letztes erzeugtes `datetime`-Objekt naiv oder gewahr?
- Sorgen Sie dafür, dass es in der hiesigen Zeitzone (Europe/Berlin) gewahr ist. Geben Sie das Ergebnis aus mit
  `print(...)  # Antwort 4`.  
  Für diese Aufgabe kann das Modul [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo) nützlich sein, welches eine konkrete Implementierung der Klasse
  `datetime.tzinfo` bietet. Andere Module von Drittanbietern sollen in dieser Aufgabe *nicht* verwendet werden.

### mit Zeiten rechnen

- Erzeugen Sie ein zweites Objekt zum selben Zeitpunkt wie das vorherige, aber in der Zeitzone
  "America/Caracas".
- Bestimmen Sie die Differenz zur UTC (koordinierte Weltzeit) als `timedelta`-Objekt.
- Ziehen Sie diese Differenz von der Zeit ab. Geben Sie dies mit `print(...)  # Antwort 5` aus.
- Addieren Sie auf das Ergebnis 1024 Tage und 512 Minuten, Ergebnis soll erneut ein `datetime`-Objekt sein. Geben Sie
  dies mit `print(...)  # Antwort 6` aus.

### Praxisbeispiel

- Sie wollen aus einem Log-File die durchschnittliche Ausführzeit mehrerer Tasks bestimmen. Das Auslesen aus der Datei
  haben Sie bereits implementiert und die Daten als Tupel-Liste wie folgt vorliegen:

```python
[('2024-01-01##10:11:14', 1, 'start'),
 ('2024-01-01##10:11:14', 2, 'start'),
 ('2024-01-01##10:11:14', 1, 'end'),
 ('2024-01-01##10:11:14', 2, 'end'),]
```

- Fügen Sie die folgende Funktion in ihre Datei ein und vervollständigen Sie sie, sodass sie die Ausführungszeit aller
  übergebenen Tasks berechnet und anschließend daraus den Durchschnitt bestimmt.
- Rufen Sie die Funktion anschließend mit der oben stehenden Beispielliste als Eingabe auf.

```python
def time_average(logs):
    start = {}
    diffs = []
    result = dt.timedelta(0)

    # convert strings and calculate difference
    for l in logs:
        if l[2] == 'start':
            start[l[1]] = _____
        elif l[2] == 'end':
            diffs.append(_____)

    # calculate average
    _____

    print(result)
```

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `datetime.py` einmal aus.

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Kommandoprotokoll.md]

[INCLUDE::../../_include/Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch vom Können von `datetime` machen.

[ENDINSTRUCTOR]
