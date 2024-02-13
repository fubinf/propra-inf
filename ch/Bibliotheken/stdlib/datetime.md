title: datetime - Datum, Uhrzeit und Zeitdifferenzen
stage: draft
timevalue: 1.0
difficulty: 1
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich weiß, wie man in Python Zeit- und Datumswerte erstellen, ausgeben und diese miteinander verrechnen kann.
- Ich kenne außerdem den Unterschied zwischen aware und naive datetime.

[ENDSECTION]
[SECTION::background::default]

Das Arbeiten mit Zeit- und Datumsangaben ist in vielen Anwendungen essenziell. Eine dafür geeignete Datenstruktur
selbst zu erstellen ist jedoch aufwändiger, als man zuerst annehmen würde. Neben verschiedenen Datumsformaten (z.B.
amerikanische und deutsche Schreibweise) muss diese auch verschiedene Zeitzonen und auch Sommerzeiten mit 
berücksichtigen können. Die datetime Bibliothek bietet einige Werkzeuge, um mit den meisten dieser Anwendungsfälle
umgehen zu können. 

[ENDSECTION]
[SECTION::instructions::detailed]

### Verständnisfragen/-aufgaben

- [ER] Machen Sie sich mit der [Dokumentation von datetime](https://docs.python.org/3/library/datetime.html) vertraut.

- [ER] Geben Sie eine Python Funktion an, die eine datetime der aktuellen Zeit zurückgibt und geben Sie mithilfe von
strftime() das aktuelle Datum im deutschen Datumsformat aus (DD.MM.YYYY).
Bestimmen Sie das timedelta zum 01.01.2024 3:14 Uhr.

- [EQ] Bei datetime unterscheidet man zwischen aware und naive. Erklären Sie den Unterschied. Ist die in der oberen
Aufgabe erzeugte aktuelle datetime aware oder naive und woran können Sie das erkennen?

### Praxisbeispiel

- [ER] Sie haben aus einer log-Datei eine Liste von Start- und Endzeiten von mehreren Prozessen extrahiert und bereits
in eine Liste von Tupeln geschrieben. Diese sind folgendermaßen aufgebaut:

(Prozessnummer, Startzeit (True) oder Endzeit (False), Zeit im Format "Jahr-Monat-Tag-Stunden-Minuten-Sekunden")

Sie wollen nun herausfinden, wie lange jeder Prozess lief und welcher am längsten
gebraucht hat.

Vervollständigen Sie die Funktion compare_process_times und führen Sie sie anschließend mithilfe der Beispielliste aus.

```python
from datetime import datetime

def compare_process_times(logs):
    starttimes = {}
    result = {}
    for l in logs:
        if l[1]:
            starttimes[l[0]] = _____
        else:
            result[l[0]] = _____
            starttimes.pop(l[0])
    return result

mylogs = [(1, True, '2024-01-01-10-11-14'),
          (2, True, '2024-01-01-10-15-30'),
          (1, False, '2024-01-01-15-58-25'),
          (2, False, '2024-01-02-02-03-44')]

print(max(compare_process_times(mylogs)))
```

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Markdowndokument.md]
[INCLUDE::../../_include/Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::heading]
[ENDINSTRUCTOR]
