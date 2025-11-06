title: "re: Reguläre Ausdrücke in Python"
stage: draft
timevalue: 2
difficulty: 3
assumes: re-Gruppen, m_datetime, py-Funktionale-Programmierung
---

[SECTION::goal::idea]
Ich kann reguläre Ausdrücke in Python verwenden
[ENDSECTION]


[SECTION::background::default]
**[TERMREF2::Regulärer Ausdruck::Regular Expressions]** oder auf Deutsch **Reguläre Ausdrücke** 
oder kurz **re**, **regex** oder **regexp** stellen ein wichtiges Werkzeug in der Informatik bzw.
der Softwareentwicklung dar.
Reguläre Ausdrücke sind vielseitig einsetzbar, beispielsweise um Vorkommen solcher Ausdrücke in 
Texten zu finden oder um die Integrität übergebener Daten zu prüfen (z.B. ob eine eingegebene 
E-Mail- oder IP-Adresse syntaktisch korrekt ist).
Python stellt `re` ein umfangreiches Modul für regex in der Standardbibliothek bereit, das 
suchen, überprüfen und sogar editieren von Strings ermöglicht.
[ENDSECTION]


[SECTION::instructions::detailed]

<!--
match, fullmatch, search, IGNORECASE, MULTILINE, DOTALL, sub (Ersetzung mit Gruppenreferenzen, 
Ersetzung mit Funktionsaufruf), split, findall ist aus meiner Sicht das Minimalpensum.
-->

### Vorbereitung

Machen Sie sich mit der [Dokumentation von `re`](https://docs.python.org/3/library/re.html) 
vertraut.
Eine etwas ausführlichere und einsteigerfreundliche Einführung finden Sie außerdem in dem folgenden
[How-To Artikel](https://docs.python.org/3/howto/regex.html#regex-howto).

Allgemein gehen wir in der Aufgabe davon aus, dass Sie bereits grundsätzlich mit regex umgehen 
können.
Für einen Einstieg in das Thema regex selbst empfehlen wir die Aufgabengruppe [PARTREF::RegExp]).
Zur Auffrischung der Syntax finden Sie auch eine Übersicht in der Doku

Legen Sie die Datei `m_re.py` an und fügen Sie dort Ihre Lösungen für die folgenden 
Programmieraufgaben ein.

Als Beispiel werden wir öfter ein Pseudo-Log betrachten und mit `re` ein wenig analysieren. 
Kopieren Sie den folgenden String in Ihre Datei:

```python
log = """2025-10-22T00:48:50.008Z server01 DatabaseConnector [Warn]: Operation failed for user 421
2025-10-22T07:30:24.452Z server01 UserService [Info]: Operation pending for user 592
2025-10-22T08:07:45.961Z server01 PaymentGateway [Error]: Operation completed for user 664
2025-10-22T09:13:36.468Z server01 PaymentGateway [Info]: Operation completed for user 737
2025-10-22T10:39:19.163Z server01 PaymentGateway [Debug]: Operation failed for user 68
2025-10-23T03:40:56.106Z server01 DatabaseConnector [Info]: Operation started for user 389
2025-10-25T20:00:28.501Z server01 PaymentGateway [Info]: Operation completed for user 141
2025-10-25T23:04:31.945Z server01 UserService [Debug]: Operation failed for user 70
2025-10-26T03:38:07.881Z server01 UserService [Warn]: Operation started for user 704
2025-10-26T20:17:23.887Z server01 UserService [Warn]: Operation failed for user 919
2025-10-27T01:04:47.393Z server01 PaymentGateway [Warn]: Operation failed for user 999
2025-10-27T07:43:45.078Z server01 AuthController [Debug]: Operation pending for user 447
2025-10-27T21:05:57.722Z server01 UserService [Info]: Operation completed for user 671
2025-10-28T01:46:13.661Z server01 UserService [Info]: Operation started for user 185
2025-10-28T08:08:37.915Z server01 AuthController [Error]: Operation started for user 212"""
```

<!--
In der Aufgabe wollen wir als kleines anschauliches Beispiel ein kleines Programm schreiben, dass 
den Quellcode einer Webseite analysiert.
Legen Sie dazu noch die Datei `m_re.html` an und kopieren Sie den Inhalt folgenden Foldouts in 
die Datei (hierbei handelt es sich um den HTML-Code der Basis-Kapitelseite des ProPras).
-->


### Suchen und vergleichen

Gerade zum Suchen und Vergleichen bietet `re` mehrere Funktionen an, von denen nicht auf den 
ersten Blick erkennbar ist, was genau die Unterschiede sind und sich daher leicht verwechseln 
lassen.
Zu den Funktionen gehören:  
`match`, `fullmatch`, `search` und `findall`.

[EQ] Nennen Sie kurz die Unterschiede der Funktionen.

[EQ] Ordnen Sie den nachfolgenden Szenarios jeweils die Funktion zu, die Ihrer Meinung nach in 
dem Fall am besten geeignet ist:

1. Zur Analyse einer Log-Datei sollen alle Vorkommen des Schlagwortes "Error" gesucht werden.
2. Für einen vom User eingegebenen String soll geprüft werden, ob es sich um eine gültige 
   E-Mail-Adresse handelt.
3. In einem Text wollen Sie prüfen, ob es ein Wort mit einem deutschen Umlaut enthält.
4. Für eine Artikelnummer soll geprüft werden, ob sie immer mit einer festen Anzahl an Ziffern 
   beginnt.

<!--
[#ER] Suchen Sie, ob es eine Error-Meldung am 22. Oktober 2025 gab.
`print("error on Oct 22:", (... is not None))`

[#ER] Prüfen Sie, ob jede Zeile des Logs mit demselben Schema beginnt: `Zeit Server Service 
[Nachrichtentyp]: Nachricht`.
-->

### regex-Pattern und Metazeichen

Bei regulären Ausdrücken in Python gibt es eine Besonderheit zu beachten:

Reguläre Ausdrücke verwenden Backslashes (`\`) als Metazeichen (z.B bei `\d` für alle Ziffern, 
äquivalent zu `[0-9]`) sowie als Maskierungszeichen, um andere Metazeichen zu unterdrücken (z.B. 
`\[`, um nach der eckigen Klammer zu suchen anstatt eine Zeichenklasse zu definieren).
Python benutzt für Strings aber auch selbst `\` als Meta- und Maskierungszeichen, z.B. um mit 
`\n` Zeilenumbrüche darzustellen.
Das führt natürlich zu Konflikten und verschlechtert die Lesbarkeit von Ausdrücken.
Wenn z.B. direkt nach einem Backslash gesucht werden soll, müsste man dieses als `\\\\` 
schreiben, um es sowohl in Python als auch in regex zu maskieren.

Die bessere Alternative ist die Verwendung von Raw-Strings.
Diese kann man durch das Präfix `r` vor einem String erzeugen (z.B. `r"\\"`).
So verwendet Python den String, ohne selbst Metazeichen zu interpretieren.

[ER] Sie wollen im Log nach der ersten `[Error]`-Meldung, sowie der nachfolgenden Textnachricht 
suchen.
Schreiben Sie hierfür zuerst einen regulären Ausdruck, der genau dies matcht.
Verwenden Sie nun eine geeignete Funktion aus `re`, um den Ausdruck anzuwenden.
Speichern Sie den Rückgabewert der Funktion in einer Variable.

# Match-Objekte

Beim Suchen mit `re` erhalten Sie von der verwendeten Funktion ein 
[Match-Objekt](https://docs.python.org/3/library/re.html#match-objects) zurück (mit Ausnahme von 
`findall()` und `finditer()`, wo sie eine Liste bzw. einen Iterator aller Matches erhalten).
Wird keine Übereinstimmung gefunden, ist der Rückgabewert `None`.

[ER] Machen Sie eine Fallunterscheidung: Wenn eim Match gefunden wurde, geben Sie den 
gefundenen String sowie seine Anfangs- und Endposition im Suchstring aus:  
`print("error message found:", ..., "at position:", ...)`  
Ansonsten geben Sie nur `no error found` aus.

[ER] Erweitern Sie nun den regulären Ausdruck, sodass er nun sowohl `Error`, als auch 
`Warn`-Meldungen abfängt.
Außerdem soll der Ausdruck in zwei Gruppen unterteilt werden: eine mit dem Namen `service`, die den 
Servicenamen enthält und eine mit dem Namen `type`, die den Log-Typen (ohne eckige Klammern) 
enthält.  
Geben Sie vom gefundenen Match die einzelnen Gruppen sowie nochmal die Position aus:  
`print("\nservice:", ..., "\nlog type:", ..., "\nposition:", ...)`

[ER] Suchen Sie jetzt nach allen Vorkommen von Errors oder Warnings im Log.
Zählen Sie anschließend, welcher Service am häufigsten Fehler oder Warnungen gemeldet hat. 
`print("\nmost errors or warnings occurred in service:", ...)`

[ER] Jede Log-Zeile sollte nach demselben Schema aufgebaut sein:
Zeitstempel (im identischen Format), Server, Service, Log-Typ und eine Nachricht, die auf einer 
User-ID endet.
Erstellen Sie einen Ausdruck, der dieses Schema abbildet.  
Prüfen Sie nun, ob die erste Zeile des Logs dieses Schema erfüllt.
Geben Sie das Ergebnis entsprechend aus (`\nfirst line matches the schema` bzw. 
`\nfirst line doesn't match the schema`).

<!--
[#ER] Erstellen Sie einen String mit einem regulären Ausdruck in Python.
Dieser soll immer das letzte Wort eines Satzes matchen, also das Wort, das auf einem Satzzeichen 
(`.!?`) endet (das Zeichen selbst über ein lookahead aus dem Match auszuschließen ist optional).

Beim Suchen mit `re` erhalten Sie von der verwendeten Funktion ein sog. Match-Objekt 
zurück. Gibt es keine Übereinstimmung, wird `None` zurückgegeben.

[#ER] Verwenden Sie nun `re.findall()`, um den Ausdruck auf den folgenden String anzuwenden.
Geben Sie vom erhaltenen Match-Objekt den ursprüglichen String, die Start- und Endposition, 
sowie das Match selbst aus.
-->

<!--
[#ER] Verwenden Sie das 
Dieser soll aus der Datei den Titel der Webseite finden (der im Tag `<title>...</tile>` steht).
Verwenden Sie `re.search()`, um es in der Datei zu finden.

[#ER] Suchen Sie alle Vorkommen von Links auf der Seite. Listen Sie den Link, sowie die Stelle an 
dem er gefunden wurde auf.

[#ER] Prüfen Sie, ob das Grundgerüst der Webseite korrekt ist (Doctype, html, head und body-Tag)
-->


### Flags

Reguläre Ausdrücke können neben dem eigentlichen Ausdruck noch zusätzliche Optionen 
erhalten, die das Verhalten des Ausdrucks beeinflussen, z.B. um festzulegen, ob 
Groß-/Kleinschreibung mit berücksichtigt werden soll.
In Python lassen sich diese Optionen als Flags zusammen mit dem Ausdruck übergeben.

[EQ] Nehmen Sie drei der Flags, von denen Sie denken, dass sie am häufigsten eingesetzt werden 
und schreiben Sie jeweils ein kurzes Beispiel auf, in denen sie sinnvoll verwendet werden könnten.

[ER] Suchen Sie alle Zeilen im Log, die Aktionen für den User 999 zeigen.
Dabei wollen Sie immer die gesamte Zeile matchen, um sie komplett auszugeben.
Geben Sie jedes Match in einer eigenen Zeile aus:  
`print("\nfound messages for user 999:")
...`

[ER] Prüfen Sie, ob am 23.10.2025 oder später noch einmal ein Error aufgetreten ist.
Erstellen Sie dafür einen Ausdruck, der den gesamten Inhalt der ersten Zeile matcht, die einen 
Error-Meldung enthält.
Geben Sie die gefundene Zeile ähnlich zu [EREFR::2] aus.  
`print("\nfound error after Oct. 22:", ..., "\nat position:", ...)`


### Teilen und ersetzen

`re` bietet nicht nur die Möglichkeit zum Suchen, sondern auch zum Editieren von Strings.
`re.split()` und `re.sub()` bieten somit deutlich dynamischere Möglichkeiten zur Bearbeitung als 
z.B. Alternativen die `split()` und `replace()` Methoden des `string`-Moduls.

[ER] Teilen Sie zuerst das Log in seine einzelnen Zeilen auf (da das keinen regulären Ausdruck 
benötigt, dürfen Sie hier auch einen normalen String-Split verwenden).
Teilen Sie anschließend jede Zeile in Ihre Bestandteile auf, also Zeit, Server, Service, Log-Typ 
und Nachricht.
Geben Sie von der letzten Log-Zeile alle Bestandteile als Liste aus.  
`print ("\nlast plit line:", ...)`

[ER] Sie wollen die Zeitangaben im Log-File in eine andere Zeitzone umrechnen.
Schreiben Sie zuerst einen regulären Ausdruck, der das Zeitformat der Log-Einträge matcht.  
Wir verwenden nun `re.sub()`, wobei wir als Replacement keinen statischen String, sondern eine 
Funktion übergeben wollen.
Schreiben Sie hierfür eine Funktion, die ein `match`-Objekt sowie die Anzahl an Stunden, die 
draufgerechnet bzw. abgezogen werden sollen, entgegennimmt und einen String mit demselben 
Datumsformat und der entsprechend angepassten Zeit zurückgibt. 
Verwenden Sie [`datetime`](https://docs.python.org/3/library/datetime.html), um die Zeit korrekt 
umzuwandeln, da ein manuelles Handling der Zeiten zu komplex werden würde. Verzichten sie auch 
auf die Verwendung echter Zeitzonen, sondern addieren Sie nur ein Zeitdelta zum `datetime`-Objekt.  
Verwenden Sie schließlich `re.sub()`, übergeben Sie ihre Funktion mit einem Zeitdelta, sodass die 
Zeit um eine Stunde nach vorne gestellt wird (z.B. 8:00 → 9:00).
Geben Sie das gesamte konvertierte Log aus.

[HINT::Welche Funktionen von `datetime` sollte ich verwenden?]
Zum Konvertieren eines Strings in ein `datetime`-Objekt können Sie `datetime.datetime.strptime()` 
verwenden. Eine Übersicht über die Formatierungszeichen finden Sie hier: 
[HREF::https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes].

Um auf das `datetime`-Objekt Zeiten zu addieren können Sie `datetime.timedelta` verwenden. 
Mit echten Zeitzonen zu arbeiten würde an der Stelle zu komplex werden.

Zum Zurückwandeln in einen String gibt es die Funktion `datetime.datetime.strftime()`.
[ENDHINT]


### Reguläre Ausdrücke kompilieren

Jeder RegEx-String, den Sie an eine Funktion von `re` übergeben, muss zuerst in einen Bytecode 
kompiliert werden, bevor er von der RegEx-Engine ausgewertet werden kann.
Dies geschieht im Hintergrund bei jedem Aufruf von z.B. `search()` oder `match()`, es sei denn der 
Ausdruck wurde schon einmal kompiliert und liegt noch im Cache vor.

Wird ein Ausdruck häufiger verwendet, lässt sich dieser auch im Vorfeld mit 
[`re.compile()`](https://docs.python.org/3/library/re.html#re.compile) kompilieren und das 
erhaltene Objekt anschließend beliebig oft auf unterschiedliche Eingaben anwenden.
Das kann vor allem bei Verwendung einer großen Anzahl an Ausdrücken, die auch mehrfach 
verwendet werden, effizienter sein.

[EQ] Wäre die Verwendung von `re.compile()` im Umfang dieser Aufgabe sinnvoll?
Begründen Sie Ihre Antwort.

[ENDSECTION]


[SECTION::submission::reflection,information,snippet,trace]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Codedurchsicht]
Achten Sie darauf, dass die Studierenden Raw-Strings für reguläre Ausdrücke verwenden (`r"..."`),
um Kollisionen mit Python-Metazeichen und übermäßigen Gebrauch von Backslashes zu vermeiden.

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
