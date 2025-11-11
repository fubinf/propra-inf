title: "re: Reguläre Ausdrücke in Python"
stage: alpha
timevalue: 2
difficulty: 3
assumes: re-Gruppen, m_datetime, py-Funktionale-Programmierung
---

[SECTION::goal::idea]
Ich kann in Python zum Suchen oder zum Suchen-und-Ersetzen reguläre Ausdrücke verwenden.
[ENDSECTION]


[SECTION::background::default]
Das Python-Modul `re` ist so handlich und leistungsstark, dass man es bei der Programmierung
für ungeheuer viele Zwecke einsetzt, weil es oft sehr kompakte Lösungen erlaubt.
[ENDSECTION]


[SECTION::instructions::detailed]

### Vorbereitung

Die `assumes`-Einträge dieser Aufgabe haben Sie ja hoffentlich beachtet und sind schon ganz
ungeduldig, Ihr Regexp-Wissen praktisch einzusetzen?
Dann können wir ja loslegen.

Machen Sie sich mit der [Dokumentation von `re`](https://docs.python.org/3/library/re.html) 
vertraut.
Eine etwas ausführlichere und einsteigerfreundliche Einführung finden Sie außerdem in dem folgenden
[How-To Artikel](https://docs.python.org/3/howto/regex.html#regex-howto).

Legen Sie die Datei `m_re.py` an und fügen Sie dort Ihre Lösungen für die folgenden 
Programmieraufgaben ein.

Als Beispiel werden wir in der Aufgabe Logging-Daten betrachten und mit `re` analysieren. 
Kopieren Sie den folgenden String in Ihre Datei:

```python
log = """2025-10-22T00:48:50.008Z server01 DatabaseConnector [Warn]: Operation failed for user 421
2025-10-22T07:30:24.452Z server01 UserService [Info]: Operation pending for user 592
2025-10-22T08:07:45.961Z server01 PaymentGateway [Error]: Operation completed for user 664
2025-10-22T09:13:36.468Z server01 PaymentGateway [Info]: Operation completed for user 737
2025-10-22T10:39:19.163Z server01 PaymentGateway [Debug]: Operation failed for user 68
2025-10-23T03:40:56.106Z server01 DatabaseConnector [Info]: Operation started for user 389
2025-10-25T20:00:28.501Z server01 PaymentGateway [Info]: Operation completed for user 141
2025-10-25T23:04:31.945Z server07 UserService [Warn]: Operation failed for user 999
2025-10-26T03:38:07.881Z server01 UserService [Warn]: Operation started for user 704
2025-10-26T20:17:23.887Z server10 UserService [Warn]: Operation failed for user 919
2025-10-27T01:04:47.393Z server10 PaymentGateway [Warn]: Operation failed for user 999
2025-10-27T07:43:45.078Z server01 AuthController [Debug]: Operation pending for user 447
2025-10-27T21:05:57.722Z server01 UserService [Info]: Operation completed for user 671
2025-10-28T01:46:13.661Z server01 UserService [Info]: Operation started for user 185
2025-10-28T08:08:37.915Z server01 AuthController [Error]: Operation started for user 212
"""
```


### Suchen und Vergleichen

Zum Suchen und Vergleichen bietet `re` mehrere Funktionen an, von denen nicht auf den 
ersten Blick erkennbar ist, was genau die Unterschiede sind und sich daher leicht verwechseln 
lassen.
Zu den Funktionen gehören:  
`match`, `fullmatch`, `search` und `findall`.

[EQ] Nennen Sie kurz die Unterschiede der Funktionen.

[EQ] Ordnen Sie den nachfolgenden Szenarios jeweils die Funktion zu, die Ihrer Meinung nach in 
dem Fall am besten geeignet ist (schreiben Sie noch keinen konkreten Code):

1. Zur Analyse einer Log-Datei sollen alle Vorkommen des Schlagwortes "Error" gesucht werden.
2. Für einen gegebenen String soll geprüft werden, ob es sich um eine gültige 
   E-Mail-Adresse handelt.
3. In einem Text wollen Sie prüfen, ob er ein Wort mit einem deutschen Umlaut enthält.
4. Für einen Artikelcode soll sichergestellt werden, dass er mit 4 Ziffern beginnt.


### regex-Patterns und Raw-Strings

Reguläre Ausdrücke verwenden Backslashes (`\`) als Metazeichen (z.B. `\w`, `\d`) sowie als 
Maskierungszeichen, um andere Metazeichen zu unterdrücken (z.B. `\[`, um nach der eckigen 
Klammer zu suchen anstatt eine Zeichenklasse zu definieren).
Python benutzt für Strings aber auch selbst `\` als Meta- und Maskierungszeichen, z.B. um mit 
`\n` Zeilenumbrüche darzustellen.

Das verschlechtert die Lesbarkeit von regulären Ausdrücken in normalen Strings:
Wenn z.B. direkt nach einem Backslash gesucht werden soll, müsste man das Literal dafür 
als `\\\\` schreiben. 
Der resultierende String enthält dann zwei Backslashes.
Dieser reguläre Ausdruck trifft auf einen Backslash zu.

Die bessere Alternative ist die Verwendung von Raw-Strings.
Diese kann man durch das Präfix `r` vor einem String erzeugen (z.B. `r"\\"`).
In einem Raw-String gibt es keine Metazeichen; `r"\\"` steht also für einen String,
der zwei Backslashes enthält.
Für reguläre Ausdrücke verwendet man in Python per Konvention immer Raw-Strings, sogar dann,
wenn der Ausdruck keinen einzigen Backslash benötigen sollte.
(Deshalb glauben manche Leute, das `r` stehe für "regular expression". Das ist nicht der Fall.)

[ER] Sie wollen im Log nach der ersten `[Error]`-Meldung suchen und daraus den Prozess/Service
extrahieren, der die Meldung erzeugt hat.
Schreiben Sie hierfür zuerst einen regulären Ausdruck, der genau dies matcht.
Verwenden Sie nun eine geeignete Funktion aus `re`, um den Ausdruck anzuwenden.
Speichern Sie den Rückgabewert der Funktion in einer Variable.


### Match-Objekte

Beim Suchen mit `re` erhalten Sie von der verwendeten Funktion ein 
[Match-Objekt](https://docs.python.org/3/library/re.html#match-objects) 
zurück (mit Ausnahme von `findall()` und `finditer()`, 
wo sie eine Liste bzw. einen Iterator aller Matches erhalten).
Wird keine Übereinstimmung gefunden, ist der Rückgabewert `None`.

[ER] Machen Sie eine Fallunterscheidung: Wenn in [EREFR::1] ein Match gefunden wurde, geben Sie den 
gefundenen String sowie seine Anfangs- und Endposition im Suchstring aus:  
`print("error found:", ..., "at position:", ...)`  
Ansonsten geben Sie nur `no error found` aus.

[ER] Erweitern Sie nun den regulären Ausdruck, sodass er nun sowohl `Error`, als auch 
`Warn`-Meldungen abfängt.
Außerdem soll der Ausdruck in zwei Gruppen unterteilt werden: eine mit dem Namen `service`, die den 
Servicenamen enthält und eine mit dem Namen `type`, die den Log-Typen (ohne eckige Klammern) 
enthält.  
Geben Sie vom gefundenen Match die einzelnen Gruppen sowie nochmal die Position aus:  
`print("\nlog type:", ..., "\nservice:", ..., "\nposition:", ...)`

[ER] Suchen Sie jetzt nach **allen** Vorkommen von Errors oder Warnings im Log.
Zählen Sie anschließend, welcher Service am häufigsten Fehler oder Warnungen gemeldet hat. 
`print("\nmost errors or warnings occurred in service:", ...)`

[ER] Jede Log-Zeile sollte nach demselben Schema aufgebaut sein:
Zeitstempel (im identischen Format), Server, Service, Log-Typ und eine Nachricht, die auf einer 
User-ID endet.
Erstellen Sie einen Ausdruck, der dieses Schema abbildet.  
Prüfen Sie nun, ob die erste Zeile des Logs dieses Schema erfüllt.
Geben Sie das Ergebnis entsprechend aus (`\nfirst line matches the schema` bzw. 
`\nfirst line doesn't match the schema`).


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
`print("\nmessages for user 999:")
...`

[ER] Prüfen Sie, ob am 23.10.2025 oder später noch einmal ein Error aufgetreten ist.
Erstellen Sie dafür einen Ausdruck, der den gesamten Inhalt der ersten gefundenen Zeile matcht, die 
die Error-Meldung enthält.
Geben Sie die gefundene Zeile ähnlich wie in [EREFR::2] aus.  
`print("\nfound error after Oct. 22:", ..., "\nat position:", ...)`


### Teilen und ersetzen

`re` bietet nicht nur die Möglichkeit zum Suchen, sondern auch zum Editieren von Strings.
`re.split()` und `re.sub()` bieten somit deutlich dynamischere Möglichkeiten zur Bearbeitung als 
z.B. Alternativen die `split()` und `replace()` Methoden des `string`-Moduls.

[ER] Teilen Sie zuerst das Log in seine einzelnen Zeilen auf (da das keinen regulären Ausdruck 
benötigt, dürfen Sie hier auch einen normalen String-Split verwenden).
Teilen Sie anschließend jede Zeile in Ihre Bestandteile auf, also Zeit, Server, Service, Log-Typ 
(ohne Klammern) und Nachricht.
Geben Sie von der letzten Log-Zeile alle Bestandteile als Liste aus.  
`print ("\nlast line:", ...)`

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
Zeit um eine Stunde vorgestellt wird (z.B. 8:00 → 9:00).
Geben Sie das gesamte konvertierte Log aus.  
`print("\nadjusted time zone:")
...`

[HINT::Welche Funktionen von `datetime` kann ich verwenden?]
Zum Konvertieren eines Strings in ein `datetime`-Objekt können Sie `datetime.datetime.strptime()` 
verwenden.
Eine Übersicht über die Formatierungszeichen finden Sie hier: 
[HREF::https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes].

Um auf das `datetime`-Objekt Zeiten zu addieren können Sie `datetime.timedelta` verwenden.

Zum Zurückwandeln in einen String gibt es die Funktion `datetime.datetime.strftime()`.
[ENDHINT]


### Programmlauf für die Abgabe

[EC] Führen Sie das gesamte so erzeugte Programm `m_re.py` einmal aus.


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
Code prüfen, ob er die geforderten Werkzeuge verwendet (Elemente aus `re`).
Das Kommandoprotokoll mit Muster vergleichen.
Bei Abweichungen gezielt im Code nachschauen, woran dies liegt.
Bei klaren Defekten und Abgaben, die nicht die in der Aufgabe geforderten Werkzeuge verwenden, 
zurückweisen.

Achten Sie darauf, dass die Studierenden Raw-Strings für reguläre Ausdrücke verwenden (`r"..."`),
um Kollisionen mit Python-Metazeichen und übermäßigen Gebrauch von Backslashes zu vermeiden.

Musterlösung siehe: [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_re.py]

[INCLUDE::ALT:]

### Kommandoprotokoll

[PROT::ALT:m_re.prot]
[ENDINSTRUCTOR]
