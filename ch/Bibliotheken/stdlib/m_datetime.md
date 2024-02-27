title: "datetime: Datum, Uhrzeit, Zeitintervalle verarbeiten"
stage: draft
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::trial]
- Ich habe eine Vorstellung, was das `datetime`-Modul kann und habe ein paar der Funktionen ausprobiert.
[ENDSECTION]
[SECTION::background::default]

In jeder größeren Software hat man früher oder später mit Zeit oder Datum zu tun.
Ohne gute Bibliothek ist das Thema super kompliziert, weshalb man sich mit diesen
Funktionen tunlichst auskennen sollte.

[ENDSECTION]
[SECTION::instructions::detailed]


### `import datetime as dt`

- Der Modulname `datetime` ist länger als die meisten in der Standardbibliothek.
  Außerdem gibt es darin eine Klasse, die ebenfalls `datetime` heißt: verwirrend.
- Deshalb importieren wir per Konvention das Modul stets so:  
  `import datetime as dt`
- Das Konstrukt `from datetime import *` is generell nicht zu empfehlen,
  weil man dann leicht etwas importiert, dass einen anderen Import überdeckt.
  Der Code wird auch schwerer lesbar.


### Aktuelle Zeit ausgeben

- Finden Sie in der 
  [Dokumentation](https://docs.python.org/3/library/datetime.html),
  wie man die aktuelle lokale Zeit abfragt.
- Falls Sie angesichts des Umfangs der Doku dabei verzweifeln:
  So etwas geht mit einer Web-Suche tatsächlich oft schneller.
  Allerdings muss man sich dann vor irreführenden oder veralteten Antworten in Acht nehmen
  und sollte die Information in der aktuellen Dokumentation nachprüfen.
- Finden Sie, mit welcher Operation man ein `datetime`-Objekt in folgendes Stringformat
  bringt:  
  `Sonntag, der 01. Dezember 2024, 13:09 Uhr`
- Legen Sie die Datei `datetime.py` an und erzeugen Sie dort eine solche Ausgabe für
  die aktuelle Zeit mit `print(...)  # Antwort 1`.
  Benutzen Sie die gleiche Datei auch für den Rest der Aufgabe und fügen Sie die
  Teile einfach skriptartig hintereinander, mit Leerzeile getrennt.
- Falls das nur fast klappt und Sie bekommen Monat und Wochentag in einer anderen Sprache,
  ist bei Ihnen eine andere "Locale" (Gebietsschema) eingestellt.
  Lesen Sie beim Modul 
  `[locale](https://docs.python.org/3/library/locale.html)`
  nach, was es damit auf sich hat -- aber wir lösen das jetzt hier nicht; 
  Ihre Ausgabe ist OK wie sie ist.


### Zeiten einlesen

- Finden Sie, wie der umgekehrte Weg funktioniert: Strings in `datetime`-Objekte wandeln.
- Wandeln Sie folgendes Format: `2024-12-15##13:09:44` und geben Sie das Ergebnis aus mit
  `print(...)  # Antwort 2`.


### Mit Zeiten rechnen: Mittelwert

- Nun wandeln Sie folgende drei Zeiten:  
  `datestrings = ["2024-12-15##13:09:44", "2024-03-31##01:29:22", "2025-11-11##11:12:13"]`
- Berechnen Sie den Mittelwert der drei Zeiten als `datetime`-Objekt.  
  Das geht recht einfach über den Umweg der Timestamp-Repräsentation.  
  Eine Mittelwertfunktion finden Sie im Modul `statistics`.
- Geben Sie das Ergebnis wie oben formatiert mit `print(...)  # Antwort 3` aus.


### Mit Zeiten rechnen: Addition

- Addieren Sie auf das Ergebnis 1024 Tage und 512 Minuten, Ergebnis ist erneut ein `datetime`-Objekt.
- Geben Sie das Ergebnis wie oben formatiert mit `print(...)  # Antwort 4` aus.


### Mit Zeiten rechnen: Zeitzonen

- Lesen Sie in der Doku die Konzepte "naive" (naiv) und "aware" (gewahr) nach.
- Ist Ihr letztes Objekt oben naiv oder gewahr?
- Sorgen Sie dafür, dass es in der hiesigen Zeitzone gewahr ist.
- Erzeugen Sie sodann ein zweites Objekt zum selben Zeitpunkt, aber in der Zeitzone
  von Caracas/Venezuela und geben Sie das Ergebnis aus.


### Programmlauf für die Abgabe

- [EC] Führen Sie das gesamte so erzeugte Programm einmal aus.

[ENDSECTION]
[SECTION::submission::information,program]

[INCLUDE::../../_include/Submission-Quellcode.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]

Den Code lesen und manuell auf Richtigkeit prüfen.
Das Kommandoprotokoll zur Unterstützung heranziehen.
Klare Defekte und sehr ungünstige Konstruktionen zurückweisen,
insbesondere solche, die zu wenig Gebrauch vom Können von `datetime` machen.

[ENDINSTRUCTOR]
