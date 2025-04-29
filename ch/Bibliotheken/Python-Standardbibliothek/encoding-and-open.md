title: "open, decode: Dateien lesen oder schreiben und Encodings verstehen"
stage: beta
timevalue: 1.0
difficulty: 2
explains: Encoding
---
[SECTION::goal::trial,idea]

- Ich kann Dateien öffnen, lesen und schreiben.
- Ich verstehe, was ein Encoding ist, und kann Daten in verschiedenen Enkodierungen verarbeiten.

[ENDSECTION]
[SECTION::background::default]

Das Lesen und Schreiben von Dateien zählt beim Programmieren zu den wichtigsten
Verarbeitungsschritten und kommt in fast allen Zusammenhängen vor.

Dateien bestehen aus Bytes und Bytes aus je 8 Bit, es gibt also nur 256 verschiedene Bytes.
Es gibt aber weit mehr als 256 verschiedene Zeichen, die man in Dateien darstellen will,
wenn es um Text geht, und viele verschiedene Arten, wie man Zeichen auf Bytes
(und zurück) abbildet, die sogenannten Encodings.
Wer kein Stümper sein will, muss sich damit auskennen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Datei lesen, naiv

- Laden Sie die Datei [PARTREF::encoding.zip] herunter und packen Sie sie aus
  in das Verzeichnis `encoding` in Ihrem Arbeitsbereich.
- [ER] Legen Sie ein Programm `encoding-and-open.py` an.
- [ER] Schreiben Sie folgenden Code und lassen Sie ihn laufen:

```
with open("encoding/datei1", mode="rt") as f:
    content = f.read()
print(content)
```

Erläuterung:

- `open()` öffnet die Datei und liefert ein sogenanntes "File Handle", 
  mit dem man Lesen oder Schreiben kann. 
  Diese werden als Variablen häufig kurz `f` oder `fh` genannt.
  Der `mode` mit dem Wert "rt" steht für "read,text". 
  Statt "read" ginge auch "write" (Datei überschreiben) oder "append" (an Datei anfügen):
  Welche Operationen auf der Datei stattfinden sollen.
  Statt "text" ginge auch "binary": Wie die Daten in der Datei interpretiert werden sollen.
- `f.read()` liest den kompletten Inhalt der Datei und liefert ihn als String (bei Text)
  oder als `bytes` (bei Binärdaten). Wir bekommen also einen String.
- Das `with` benutzt das File Handle als [TERMREF::Kontextmanager] und sorgt dafür, dass die Datei
  am Ende des Blocks garantiert wieder geschlossen wird, sodass die davon belegten Ressourcen
  im Betriebssystem wieder freigegeben werden. 
  Das ist bei länger laufenden Programmen wichtig, um ein Erschöpfen dieser Ressourcen zu verhindern
  und klappt sogar, wenn im Rumpf eine Ausnahme geworfen wird.
- Ändern Sie den `mode` nach `"rb"`, lassen Sie den Code erneut laufen und vergleichen Sie die Ausgaben:
  Sie sind verschieden. Umlaut und ß sind kaputt.
  Das liegt daran, dass Umlaute und ß ein Encoding brauchen, um in Bytes dargestellt zu werden.
  Im Textmode wurde dieses Encoding benutzt, im Binärmode nicht.


### Datei lesen, ordentlich

- Dass der Inhalt beim Textmode korrekt herauskam, war Glückssache, denn es gibt viele mögliche Encodings:
  Die Datei ist beispielsweise mit Encoding X geschrieben,
  beim Lesen haben wir Encoding Y benutzt.
  Wenn X gleich Y ist, funktioniert alles richtig.
  Wenn sie verschieden sind, kann es je nach Kombination klappen (u.U. auch bei verschiedenen Dateiinhalten meistens) 
  oder auch nicht (u.U. sogar niemals).
- Unsere konkrete `datei1` ist mit dem Encoding UTF-8 geschrieben.
  Beim Lesen im Textmode benutzt modernes Python standardmäßig ebenfalls UTF-8, wenn man
  nicht gerade auf Windows unterwegs ist; dort muss man Python dazu erst ermuntern.
- Beim `print()` passiert das gleiche Spiel: Der String wird von Python
  nach den Regeln von UTF-8 in eine Bytefolge enkodiert und vom Terminal gemäß UTF-8 wieder als String
  interpretiert. Ist das Terminal auf ein anderes Encoding eingestellt, geht das Spiel nicht auf.
- Lesen Sie in der 
  [Dokumentation von `open`](https://docs.python.org/3/library/functions.html#open)
  alle Bedeutungen des Parameters `mode` und den Parameter `encoding` nach.
- [ER] Erweitern Sie obigen Code so, dass die Verwendung von UTF-8 beim `open()` explizit wird,
  siehe die 
  [Liste der Text-Encodings von Python](https://docs.python.org/3/library/codecs.html#text-encodings).


### Encodings bestimmen

- [ER] Jetzt bohren wir den obigen Code auf, um die Encodings aller vier Dateien zu verstehen,
  denn die sind alle verschieden:  
  `filenames = [f"encoding/datei{i+1}" for i in range(4)]`
- [ER] Schreiben Sie zwei verschachtelte Schleifen: Die äußere läuft über `filenames`,
- [ER] die innere läuft über folgende encodings:  
  `encodings = ['utf8', 'cp500', 'iso-8859-1', 'iso-8859-9', 'EBCDIC-CP-BE']`
- [ER] Geben Sie ein passendes Argument für `errors` an, um die bei diesem stumpfsinnigen Verfahren 
  unvermeidlichen Encodierungsfehler zu überstehen.
- [ER] Geben Sie beim `print()` Dateiname und Encoding mit aus.
- [EQ] Bestimmen Sie anhand der Ausgaben das vernünftigste Encoding zu jeder Datei.
  Lesen Sie dazu grob auf Wikipedia nach, was es mit jedem der Encodings auf sich hat.


### Erläuterung

- **UTF-8** ist inzwischen in weiten Teilen der Welt das vorherrschende Encoding,
  denn es kann [Unicode](https://en.wikipedia.org/wiki/Unicode)
  komplett darstellen.
  In Ostasien und auf Windows findet man auch UTF-16. 
- Die diversen **ISO-8859**-Encodings waren in den 1990er Jahren vorherrschend
  und sind seither allmählich auf dem Rückzug, begegnen einem aber noch häufig,
  vor allem bei älteren Daten und Programmen.
- **[EBCDIC](https://en.wikipedia.org/wiki/EBCDIC)** 
  war einst eine wichtige Kodierung (mit vielen Ländervarianten, ähnlich wie bei ISO-8859) 
  auf IBM-Großrechnern und ist dort auch
  immer noch in Gebrauch, aber im Rest der Softwarewelt ist es exotisch.


### Datentypen verstehen

Ohne das explizit zu merken, haben wir oben zwei verschiedene Datentypen von Python benutzt:

- Dekodierte Strings heißen auch Unicode-Strings.  
  Der Datentyp heißt `str` und umgangssprachlich sagt man in Python meist "String" dazu.  
  String-Literale werden als `"ein String"` geschrieben.  
  Strings können alle Unicode-Zeichen darstellen; ein riesiger Vorrat, der alle Sprachen der Welt 
  ausdrücken kann.
- Undekodierte Strings heißen auch Byte-Strings.  
  Der Datentyp heißt `bytes` und umgangssprachlich sagt man in Python "Bytestring" oder "Bytes" dazu.  
  Bytestring-Literale werden als `b"ein Bytestring"` geschrieben.    
  Bytestrings enthalten als Zeichen nur kleine Ganzzahlen von 0 bis 255, die man erst noch 
  interpretieren muss. 

Ein Encoding ist eine solche Interpretation für Bytestrings.
Bytestrings können den Regeln jedes beliebigen Encodings folgen.

Wenn Sie sich auf den Zeichenbereich 0 bis 127 beschränken, liegt oft das 
klassische Encoding "ascii" vor. 
In dem Fall kann man die Daten auch als irgendeines der ISO-8859-Encodings interpretieren
oder als UTF-8, ohne dass sich irgendetwas ändert.

Ascii ist sozusagen das Pidgin-English der Computerwelt: Man kann sich damit zwar nicht gerade
gewählt ausdrücken, kommt aber in den meisten Gegenden halbwegs zurecht.


### Selber machen!

Anstatt das Dekodieren des Encodings mit der Angabe `open(..., encoding=...)` Python zu überlassen,
können wir es auch selber machen, indem wir die Datei im Binärmode öffnen und dann
das dort als Bytestrom gelesene explizit dekodieren, umgefähr so:
`content.decode(myencoding)`

- [ER] Probieren Sie das aus, indem Sie ihr Programm entsprechend umbauen.

[ENDSECTION]
[SECTION::submission::information,program]

[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Die Encodings sollten stimmen]

- Die Antwort für die Encodings sollte richtig sein (utf8, iso8859-1, cp500/EBCDIC-CP-BE, iso8859-9).
- cp500 und EBCDIC-CP-BE sind ein- und dasselbe. 
  Wenn dazu keine Anmerkung in der Antwort steht, Studi darauf hinweisen, 
  sowas künftig aufzuklären und dann zu erklären.
- datei2 wird auch mit iso8859-9 (Latin-5, Türkisch) korrekt dargestellt, 
  aber das ergibt inhaltlich keinen Sinn,
  wenn man wie gewünscht auf Wikipedia nachgelesen hat und ist deshalb falsch.
- Der Code sollte vernünftiges Python sein, mit Schleifen über die Behälter.
  Zusätzliche Abstraktionen sind nicht nötig.

[ENDINSTRUCTOR]
