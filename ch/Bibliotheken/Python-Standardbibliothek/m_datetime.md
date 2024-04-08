title: datetime - Datum, Uhrzeit und Zeitdifferenzen
stage: beta
timevalue: 1.5
difficulty: 2
---
[SECTION::goal::trial]

- Ich kann in Python Zeit- und Datumswerte erstellen, formatieren und verrechnen.
- Ich kenne den Unterschied zwischen aware und naive `datetime`.

[ENDSECTION]

[SECTION::background::default]

Das Arbeiten mit Zeit- und Datumsangaben ist in vielen Anwendungen essenziell, aber frappierend kompliziert:
verschiedene Monatslängen, Schaltjahre, Zeitzonen; 
das alles bietet tausendfach Gelegenheit für Fehler und Verwirrung.
Die `datetime` Bibliothek geht souverän mit alldem um und gehört zum Grundstock dessen,
was man über die Standardbibliothek wissen muss. 

[ENDSECTION]

[SECTION::instructions::detailed]

- Legen Sie die Datei `m_datetime.py` an und benutzen Sie diese Datei für den Rest der Aufgabe. Fügen Sie ihre Python
  Kommandos skript-artig hintereinander in die Datei ein, mit Leerzeile getrennt.

### `import datetime as dt`

- Der Modulname `datetime` ist länger als die meisten in der Standardbibliothek.
  Außerdem gibt es darin eine Klasse, die ebenfalls `datetime` heißt: verwirrend.
- Deshalb importieren wir per Konvention das Modul stets so:  
  `import datetime as dt`.
  Die `datetime`-Klasse ist anschließend also als `dt.datetime` anzusprechen.
- Das Konstrukt `from datetime import *` ist (auch generell) nicht zu empfehlen,
  weil man dann leicht etwas importiert, das einen anderen Import überdeckt.
  Der Code wird auch schwerer lesbar.

### Zeit-Objekte anlegen und ausgeben

- Finden Sie in der [Dokumentation](https://docs.python.org/3/library/datetime.html), wie man die aktuelle lokale Zeit
  abfragt und geben diese mit `print("aktuelle Zeit:", ...)` aus.  
  Falls Sie angesichts des Umfangs der Doku dabei verzweifeln:
  So etwas geht mit einer Web-Suche oft schneller. Allerdings muss man sich dann vor irreführenden oder veralteten
  Antworten in Acht nehmen und sollte die Information in der aktuellen Dokumentation nachprüfen.
- Legen Sie nun ein `datetime`-Objekt an, welches den Zeitpunkt `01.12.2024, 13:09 Uhr` repräsentiert.
- Finden Sie eine Funktion, mit der Sie das oben angelegte `datetime`-Objekt als String im folgenden Format ausgeben
  können:  
  `Sonntag, der 01. Dezember 2024, 13:09 Uhr`  
  Geben Sie das Ergebnis der Funktion mit `print("formatierte Zeit:", ...)` aus.  
  Falls das nur fast klappt und Sie Monat und Wochentag in einer anderen Sprache ausgegeben bekommen, 
  ist bei Ihnen eine andere "locale" (Gebietsschema) eingestellt. 
  Ihre Ausgabe ist in dem Fall OK wie sie ist. 
  Bei Bedarf können Sie im Modul [`locale`](https://docs.python.org/3/library/locale.html) nachlesen, was es damit auf sich hat.

### Zeiten einlesen

- Finden Sie heraus, wie der umgekehrte Weg funktioniert: Strings in `datetime`-Objekte wandeln.
- Wandeln Sie den folgenden String: `2024-12-15##13:09:44` in ein `datetime`- Objekt um und geben Sie das Ergebnis mit
  `print("geparste Zeit:", ...)` aus.

### Zeitzonen

- Lesen Sie in der [Dokumentation](https://docs.python.org/3/library/datetime.html) die Konzepte "naive" (naiv) und
  "aware" (gewahr) nach. Ist Ihr letztes erzeugtes `datetime`-Objekt naiv oder gewahr?
- Sorgen Sie dafür, dass es in der hiesigen Zeitzone (Europe/Berlin) gewahr wird. Geben Sie das Ergebnis mit
  `print("Berliner Zeit:", ...)` aus.  
  Für diese Aufgabe kann das Modul [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo)
  nützlich sein, welches eine konkrete Implementierung der Klasse `datetime.tzinfo` bietet. Andere Module von
  Drittanbietern sollen in dieser Aufgabe *nicht* verwendet werden.
- Erzeugen Sie ein zweites Objekt zum textuell selben Zeitpunkt wie das vorherige, aber in der Zeitzone
  "America/Caracas".
- Bestimmen Sie die Differenz zur UTC (koordinierte Weltzeit) als `timedelta`-Objekt. Geben Sie dies mit
  `print("UTC-Abstand:", ...)` aus.

### Mit Zeiten rechnen

- Ziehen Sie diese Differenz von der Caracas-Zeit ab. 
  Geben Sie das Ergebnis mit `print("Caracas-nach-UTC:", ...)` aus.
- Addieren Sie auf das Ergebnis 1024 Tage und 512 Minuten, Ergebnis soll erneut ein `datetime`-Objekt sein.
  Geben Sie dies mit `print("+1024d+512m:", ...)` aus.

### Praxisbeispiel

- Sie wollen aus einem Log-File die durchschnittliche Ausführzeit mehrerer Tasks bestimmen. Das Auslesen aus der Datei
  haben Sie bereits implementiert und die Daten als Tupel-Liste wie folgt vorliegen:

```python
logs = [
  ('2024-01-01##10:11:14', 1, 'start'),
  ('2024-01-02##03:01:01', 2, 'start'),
  ('2024-01-03##00:11:15', 1, 'end'),
  ('2024-01-03##03:02:02', 2, 'end')
]
```

- Fügen Sie die folgende Funktion in ihre Datei ein und vervollständigen Sie sie, sodass sie die Ausführungszeit aller
  übergebenen Tasks berechnet und anschließend daraus den Durchschnitt als `timedelta` bestimmt.
- Rufen Sie die Funktion anschließend mit der oben stehenden Beispielliste als Eingabe auf
  und geben Sie das Ergebnis mit `print` aus.

```python
def time_average(logs: list[tuple[str,int,str]]) -> dt.timedelta:
    start = {}
    diffs = []

    # convert strings and calculate difference
    for timestamp, eventnumber, flag in logs:
        if flag == 'start':
            start[eventnumber] = _____
        elif flag == 'end':
            diffs.append(_____)

    # calculate average
    _____

    return _____
```

### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm `m_datetime.py` einmal aus.

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell ungefähr auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch vom Können von `datetime` machen.

[ENDINSTRUCTOR]
