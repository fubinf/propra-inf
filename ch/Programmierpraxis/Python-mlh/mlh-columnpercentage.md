title: "My Little Helpers: columnpercentage --- Frequency of top values in a column of a table"
stage: beta
timevalue: 2.5
difficulty: 3
assumes: regex_einfuehrung, Shell-Grundlagen2
requires: mlh-lsnew
---

TODO_2_prechelt: assume: py-typing

[SECTION::goal::product]

Ich habe mir ein Hilfsprogramm für diverse spaltenweise Auswertungen von Tabellendaten gebaut.

[ENDSECTION]
[SECTION::background::default]

Um sich einen Überblick über größere Tabellen zu verschaffen, ist es oft hilfreich,
die ungefähre Häufigkeitsverteilung zu verstehen: Was sind gängige Einträge?

Das kann man mit einer passenden Unix-Pipeline in vielen Fällen hinbekommen, 
es wird aber schnell sehr umständlich.
Wir bauen uns dafür ein Werkzeug, das bequem und recht leistungsfähig ist.

[ENDSECTION]

[SECTION::instructions::loose]

### Aufrufformat

- Legen Sie die Datei `mlh/mlh/subcmds/columnpercentage.py` an.
- [ER] Legen Sie darin ein Unterkommando an, das folgende Aufrufe unterstützt:

```
usage: mlh columnpercentage [-h] [--sep separator_regexp] [--find match_regexp] [--round ndigits] 
                            [--ignore] [--numshow N]
                            column

positional arguments:
  column                name (->header) or number (->no header) of column from which to extract data

options:
  -h, --help            show this help message and exit
  --sep separator_regexp, -s separator_regexp
                        what marks start of next column; default: auto
  --find match_regexp, -f match_regexp
                        use only group 1 from regexp match as the value; skip non-matching
  --round ndigits, -r ndigits
                        round numerical values to ndigits decimal places before use
  --ignore, -i          skip line for non-matches (with --find) and non-numbers (with --round)
  --numshow N, -n N     show only top N entries (default: 10)
```

`columnpercentage` arbeitet als [TERMREF::Filter].


### Aufrufbeispiel

Bevor wir die Semantik genauer besprechen, hier ein Beispiel.

Wir benutzen verarbeiten einen Standardeingabe-Strom von 80 Datensätzen im
[TERMREF::CSV]-Format:
```
firstname,lastname,gender,email,birthdate
Shelby,Terrell,Male,elijah57@example.net,1945-10-26
Phillip,Summers,Female,bethany14@example.com,1910-03-24
Kristine,Travis,Male,bthompson@example.com,1992-07-02
...
```

Der Aufruf lautet `mlh columnpercentage --find '^(....)-' --round -1 birthdate`

Die Ausgabe sieht so aus (der Trenner ist ein TAB):
```
11.2%   2010
11.2%   1930
10.0%   1980
8.8%    2000
8.8%    1960
8.8%    1950
7.5%    2020
7.5%    1940
7.5%    1920
6.2%    1990
```
und kommt wie folgt zustande:

- `birthdate`: Verarbeitet wird von jedem Datensatz das fünfte Feld, ein Geburtsdatum im 
  [ISO 8601](https://de.wikipedia.org/wiki/ISO_8601)-Format `jjjj-mm-tt`.
- `--find '^(....)-'`: Darin wird nach einem Treffer der Form `....-` am Feldanfang gesucht,
  also vier beliebige Zeichen, gefolgt von einem Querstrich.
  Weiterbenutzt werden nur die vier Zeichen (nämlich die erste Regexp-Treffergruppe).
- `--round -1`: Diese vier Zeichen werden als Zahl interpretiert und auf minus eine Nachkommastelle
  gerundet, d.h. die Einserstelle wird weggerundet und es entstehen Jahrzehnt-Angaben.
- Von diesen Jahrzehnt-Angaben wird eine Häufigkeitszählung gemacht.
- Diese Häufigkeiten werden fallend sortiert und in Prozentwerte umgerechnet.
  Bei gleichem Prozentwert wird zusätzlich nach dem Datenwert sortiert, ebenfalls fallend.
- Davon werden die ersten 10 (Standardwert der Option `--numshow`) ausgegeben.
- Die Prozentwerte werden wie folgt gerundet: Bis 20 Eingabedatenwerte auf ganze Prozent,
  bis 200 mit 1 Nachkommastelle, darüber 2 Nachkommastellen.


### Bedeutung der Optionen

- `--sep regexp`: Feldtrenner-Ausdruck. 
  Pures CSV wäre hier `--sep ,`.
  Da das ein regulärer Ausdruck ist, kann man aber auch "luftiges" CSV verarbeiten,
  das Leerzeichen um die Kommas haben kann: `--sep ' ?, ?'`.
  Gibt man die Option nicht an, probiert das Kommando folgende Werte durch:
  `[r',', r';', r'\|', r'\t', r'  +']`.
  Benutzt wird davon derjenige, der für die ersten beiden Zeilen am meisten Sinn ergibt,
  d.h. am häufigsten vorkommt, aber unbedingt in beiden Zeilen gleich oft.
  Dadurch muss man in den allermeisten Fällen nicht angeben, welches Format die Daten haben,
  sondern das wird automatisch korrekt erkannt.
  Sogar ganz ohne sichtbaren Trenner geht es, wenn zwischen Feldern stets mehrere Blanks stehen
  und innerhalb von Feldern nie, siehe der letzte Standardtrenner-Ausdruck.
- `--find regexp`: Diese Regexp wird auf den Feldwert angewandt, muss zutreffen,
  und weiterverwendet wird dann nur die erste "matching group", also der Inhalt des ersten Klammerpaars.
- `--round ndigits`: Der Feldwert muss eine Zahl sein (Ziffernfolge mit oder ohne Dezimalpunkt)
  und der auf `ndigits` Nachkommastellen gerundete Wert wird weiterverwendet.
  Ist `ndigits` negativ, werden entsprechend viele Stellen _vor_ dem Dezimalpunkt genullt.
- `--ignore`: Bricht nicht ab, falls ein Feldwert von einem `--find`-Ausdruck nicht getroffen wird
  oder wenn `--round` auf eine Nicht-Zahl trifft, sondern überspringt und ignoriert die betreffende
  Zeile. (Siehe 'Fehlerfälle' unten.)
- `--numshow N`: Beschränkt die Ausgabe auf maximal N Häufigkeitswerte.
- `column`: Kann eine Ganzzahl sein oder ein String.
  Bei Ganzzahl N wird die N-te Spalte benutzt (gezählt ab 1) und die erste Zeile als Datensatz mitverarbeitet.
  Bei sonstigem String wird dieser als Spaltenname interpretiert und die erste Zeile als Header,
  also Liste der Spaltennamen.


### Fehlerfälle

In folgenden Fällen soll das Programm mit einer kurzen Fehlermeldung (auf stdout) abbrechen:

- Spalte nicht vorhanden (Spaltennamen-Liste mit ausgeben)
- find-Ausdruck nicht getroffen und kein ignore gewählt (Feldwert mit ausgeben)
- round auf Nicht-Zahl angewandt und kein ignore gewählt (Feldwert mit ausgeben)
- sep nicht angegeben und nur 1 Eingabezeile vorhanden


### Also los!

- [ER] Implementieren Sie das Kommando gemäß obiger Spezifikation

[HINT::Wie strukturiert man das?]
Ziehen Sie beispielsweise folgende Funktionen in Erwägung, mit denen sich 
die Hauptfunktion `execute()` gut erledigen lässt:

```python
def determine_separator(separator_re: str, data: tg.Sequence[str]) -> str:
    ...
def determine_colindex(colspec: str, firstline: str, separator_re: str) -> tuple[int, bool]:  # index, has_header
    ...
def determine_precision(ndata: int) -> int:
    ...
Result = tuple[float, str] 
def process(data: tg.Sequence[str], args: ap_sub.Namespace) -> tg.Sequence[Result]:
    ...
def _count_each(regexps: tg.Iterable[str], line: str) -> tg.Sequence[int]:  # Hilfsfunktion für determine_separator
    ...
def _rounded(percentage: float, precision: int) -> tg.Union[int,float]:
    ...
```

[HINT::Und wie spielen diese Teile zusammen?]
Ihre `execute`-Funktion _könnte_ z.B. so aussehen:
```python
def execute(args: ap_sub.Namespace):
    data = sys.stdin.readlines()  # bad idea for huge data, but makes logic much simpler
    if len(data) == 0:
        return  # avoid special cases
    args.sep_re = determine_separator(args.sep, data)
    args.colindex, has_header = determine_colindex(args.column, data[0].rstrip(), args.sep_re)
    startindex = 1 if has_header else 0
    precision = determine_precision(len(data)-startindex)
    results = process(data[startindex:], args)
    for percentage, item in sorted(results, reverse=True)[:args.numshow]:
        print(f"{_rounded(percentage, precision)}%\t{item}")
```
[ENDHINT]
[ENDHINT]


### Testen

Benutzen Sie nie die Option `--sep`, sondern immer die automatische Bestimmung.
Benutzen Sie diese Testdaten, stecken Sie sie in die Datei `mlh/tests/data/columnpercentage-in.csv`
und geben Sie diese mit ab:
[FOLDOUT::Testdaten]
```
[INCLUDE::ALT:/../itree.zip/Programmierpraxis/Python-mlh/mlh/tests/data/columnpercentage-in.csv]
```
[ENDFOLDOUT]
Die Datei enthält 80 Datensätze.

- [EC] `DATA=tests/data/columnpercentage-in.csv`
- [EC] Werten Sie die Geschlechterbalance aus: `python . columnpercentage gender <$DATA`

[HINT::Warum wird bei mir `mlh` nicht gefunden?]
Lesen Sie die Fehlermeldung genau; daraus ergibt sich, in welchem Verzeichnis das Kommando
auszuführen ist.

[HINT::Verstehe ich immer noch nicht]
"can't find '__main__' module" heißt, Sie müssen in dem Verzeichnis sein, 
in dem sich `__main__.py` befindet, denn `python .` bedeutet, Python soll das aktuelle Verzeichnis
als Python-Programm interpretieren.
[ENDHINT]

[ENDHINT]

- [EC] Stellen Sie das Beispiel vom Einstieg (Häufigkeit der Geburtsjahrzehnte) nach 
- [EC] Jetzt üben wir ein wenig reguläre Ausdrücke: 
  Welches sind die 6 häufigsten Anfangsbuchstaben von Nachnamen?
- [EC] Welches sind die 5 häufigsten zweiten Buchstaben von Vornamen?
- [EC] Welches sind die 5 häufigsten Domains der Email-Adressen? 
  (Nicht wundern: es gibt in den Daten gar keine 5 verschiedenen)
- [EC] Jetzt prüfen wir die Dateiformat-Automatik.
  Betrachten Sie  
  `sed 's/,/    /g' $DATA | head -3`:  
  Das `sed`-Kommando schreibt unsere Eingabedaten so um, dass nun vier Blanks als Feldtrenner verwendet werden.
  Wir wiederholen die Geschlechter-Abfrage und erwarten das gleiche Ergebnis wie oben:  
- [EC] `sed 's/,/    /g' $DATA | python . columnpercentage gender`
- [EC] Jetzt prüfen wir die Rundungs-Automatik: Wir benutzen die Eingabedaten dreifach,
  haben dann also über 200 Datensätze und erwarten folglich zwei Nachkommastellen:   
  `cat $DATA $DATA $DATA | python . columnpercentage gender`  
  (Der dadurch zweimal eingefügte Pseudo-Eintrag "gender" soll uns hier nicht stören.)
- [EC] Nochmal Rundungs-Automatik, außerdem Spalte per Nummer angegeben 
  (also entsteht wieder ein Pseudo-Eintrag). 
  Wir benutzen nur 10 der Eingabedaten und erwarten folglich null Nachkommastellen:  
  `head -10 $DATA | python . columnpercentage 3`  
- [EC] Zu guter Letzt prüfen wir noch eine der Fehlermeldungen:  
  `python . columnpercentage --round 1 gender <$DATA`
- [EC] und die `--ignore`-Option:  
  `python . columnpercentage --ignore --round 1 gender <$DATA`

[ENDSECTION]
[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]
[INSTRUCTOR::Okayer Programmierstil, richtiges Protokoll]

Möglicher Quellcode siehe [TREEREF::mlh/mlh/subcmds/columnpercentage.py].

Wenn die Lösung mehr als 50% länger ist oder keine Kommentare enthält 
(es gibt in der Logik ein paar nichttriviale Stellen)
oder kaum sprechende Namen enthält
oder zu monolithisch ist, ist das einen Hinweis und in krassen Fällen eine Zurückweisung wert.

Ansonsten halten wir uns für die Korrektur an das Kommandoprotokoll, das so aussehen müsste:
[PROT::ALT:mlh-columnpercentage.prot]

[ENDINSTRUCTOR]
