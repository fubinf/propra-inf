title: "My Little Helpers: pseudonymize: filter for replacing person-identifiable data, Teil 2"
stage: alpha
timevalue: 2.0
difficulty: 3
requires: mlh-pseudonymize
---

[SECTION::goal::product,experience]

Ich habe die `mlh pseudonymize`-Funktion komplettiert und damit für komplexere Fälle 
benutzungsfreundlicher gemacht.

[ENDSECTION]
[SECTION::background::default]

Die Optionen `--nomatch`, `--pseudonyms` und `--linetypes` von
`mlh pseudonymize` haben wir bislang nur postuliert, aber noch nicht mit Leben gefüllt.

[ENDSECTION]
[SECTION::instructions::loose]

### `--pseudonyms`

Diese Option soll eine Tabelle ausgeben, wie oft jede Pseudonymklasse benutzt wurde,
häufigste zuerst.

Beispielsweise sollte der Aufruf  
`python mlh pseudonymize --pseudonyms mlh/config/access.pseu <mlh/input/access.log >/dev/null`  
als Ausgabe (nach stderr) ergeben:

```
Pseudonym-class frequency:
   11  host
    2  username
```

[ER] Realisieren Sie diese Funktionalität und vergeben Sie für die Option einen passenden `help`-Text.


### `--linetypes`

(?P<groupname>\w+)  TODO_1

Diese Option soll eine Tabelle ausgeben, wie oft jeder Linetype benutzt wurde,
häufigster zuerst.

Beispielsweise sollte der Aufruf  
`python mlh pseudonymize --linetypes mlh/config/access.pseu <mlh/input/access.log >/dev/null`  
als Ausgabe (nach stderr) ergeben:

```
Linetype frequency:
   22  (?P<host>\S+) .+(GET|HEAD|POST) /[^~].+\n
    2  (?P<host>\S+) .+(GET|HEAD|POST) /~(?P<username>\w+).+\n
```

[ER] Realisieren Sie diese Funktionalität und vergeben Sie für die Option einen passenden `help`-Text.

[ER] Achtung, das benötigt für die eigentliche Ausgabe fast dieselbe Logik wie `--pseudonyms`.
Schreiben Sie eine wiederverwendbare Routine dafür.


### `--nomatch mode`

Beschreibt, was `pseudonymize` tut, falls es zu einer Eingabezeile keinen passenden
Linetype gibt:

- `echo`: Zeile un-pseudonymisiert ausgeben.
  Das ist nur sinnvoll, wenn man sicher weiß, dass alle solchen Zeilen keine 
  personenbezogene Information enthalten werden.
- `ignore`: Gar nichts ausgeben.
  Das ist sinnvoll, wenn man weiß, dass alle solchen Zeilen für die Weiterverarbeitung 
  nicht benötigt werden.
- `fixedmsg`: Den festen String "((nomatch))\n" ausgeben.
  Das ist sinnvoll, wenn man erwartet, dass solche Zeilen selten sind und für die Weiterverarbeitung 
  nicht benötigt werden.
- `fail`: Mit einer Fehlermeldung stoppen, dabei die Eingabezeile mit anzeigen.
  Das ist sinnvoll, wenn man die Liste der Linetypes noch vervollständigen muss.
  Man kann sich damit zügig von Linetype zu Linetype weiterhangeln, ohne welche zu übersehen.

[ER] Realisieren Sie diese Funktionalität und vergeben Sie für die Option einen passenden `help`-Text.
Default-Wert sollte `fixedmsg` sein.


### Testen mit komplexem Beispiel

Folgendes ist ein Stück einer Logdatei des Authentisierungssystems einer
Debian-Installation (übertragen Sie diese Daten in die Datei `mlh/inputs/auth.log`):

```
[INCLUDE::mlh-pseudonymize2-auth.log]
```

- Legen Sie eine leere Datei `mlh/config/auth.pseu` an.
- Arbeiten Sie sich dann Linetype für Linetype durch die Eingabe vor, indem Sie immer wieder  
  `python mlh pseudonymize --nomatch fail mlh/config/auth.pseu <mlh/input/auth.log >/dev/null`  
  aufrufen und zur fehlschlagenden Zeile einen Linetype ergänzen.
- Recherchieren Sie für die Zeilen, in denen die Felder  
  `logname`, `uid`, `euid`, `tty`, `ruser`, `rhost`  
  vorkommen, was diese einzelnen Abkürzungen bedeuten könnten und treffen Sie
  dann passende Entscheidungen, welche davon zu pseudonymisieren sind und in welche
  Pseudonymklasse das jeweils gehört.
- Achtung: Dies ist nur ein kleiner Ausschnitt aus einer Logdatei, die tausende Zeilen umfasst.  
  Rechnen Sie damit, dass es weitere Linetypes geben könnte, die Sie noch nicht gesehen haben.  
  Sie sollten deshalb vermeiden, zu große Zeilenabschnitte mittels `.*` einfach zu überspringen,
  denn es könnten sich darin weitere personenbezogene Informationen befinden, die Sie dann
  nie pseudonymisieren würden.
- Fassen Sie am Ende die beiden Linetypes mit "Failed password for" und "Connection closed by"
  in nur einem Linetype zusammen.
- [EC] Zeigen Sie am Ende einen erfolgreichen Lauf von  
  `python mlh pseudonymize --nomatch fail --pseudonyms --linetypes mlh/config/auth.pseu <mlh/input/auth.log >/dev/null`

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
Checken Sie auch `auth.log` und `auth.pseu` ein.

[ENDSECTION]

[INSTRUCTOR::Protokoll kontrollieren]

- `Pseudonym-class frequency:` Es muss mindestens Klassen wie `user`, `host` und `uid` geben.
  Die müssen aber nicht genauso heißen.  
  Die Daten am Anfang der Zeilen sollten erhalten bleiben (Datum, Uhrzeit, betroffener Host, Dienstname).  
  Es darf keine separate Klasse `euid` geben (sondern dafür ist erneut `uid` zu verwenden).  
  Zusätzliche Klassen wie `port` oder `pid` (process ID) sind streng genommen ungünstig (weil
  dadurch unnötig wertvolle Information verloren geht), wir betrachten Sie hier aber als unschädlich.
- `Linetype frequency:` Es sollte ungefähr 9 Linetypes geben, 
  insbesondere den, der die Zusammenfassung `(Failed password for|Connection closed by)` enthält.    
  Bei der muss zwischen username (z.B. `user`) und IP-Adresse (z.B. `host`) ein _optionales_
  `from` zugelassen werden, was eine Schwierigkeit bei der Programmierung darstellt.  
  Wenn jemand dort nicht etwas wie `(from )?` geschrieben hat, sondern etwas wie `.*`,
  die Lösung bitte mit Hinweis auf die obige Anmerkung 
  "Achtung: Dies ist nur ein kleiner Ausschnitt" zurückweisen, damit die Studis
  sich der Programmierschwierigkeit stellen müssen.

[ENDINSTRUCTOR]
