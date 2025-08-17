title: "Grundlagen von Go (erklärt aus Sicht von Python)"
stage: beta
timevalue: 2.5
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich habe mich mit den Grundlagen von Go auseinandergesetzt und kann nun:

- ein Programm ausführen;
- Variablen definieren;
- Kontrollflussstrukturen benutzen (if, switch, for).
[ENDSECTION]

[SECTION::background::default]
Sie haben sich entschieden, eine neue Programmiersprache zu erlernen — Go.
Gute Wahl!

Go wurde als eine pythonähnliche Alternative für die Entwickler bei Google konzipiert,
die C++ als zu komplex empfanden.
Daher sind die folgenden Merkmale entstanden:

- Statische Typisierung und Laufzeiteffizienz (wie C/C++);
- Lesbarkeit und Benutzerfreundlichkeit (wie Python);
- ein leistungsfähiges Nebenläufigkeits- und Parallelitätsmodell (besser als C/C++ und Python).

Insgesamt ergibt das eine flexible und ziemlich effiziente Programmiersprache,
die besonders in der Entwicklung von Programmierwerkzeugen (Docker/Kubernetes)
und Web-Backends beliebt geworden ist.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]
Dokumentation zur Programmiersprache finden Sie in der
[Go Spec](https://go.dev/ref/spec)
für definitive (Referenz-)Information und im
[Go User Manual](https://go.dev/doc/),
wenn Sie eher Anleitungscharakter suchen.


### Ein Go-Programm ausführen

Stellen Sie sicher, dass Sie eine gültige Go-Installation auf Ihrem Rechner haben.
Tippen Sie `go version` in die Kommandozeile:
Die Ausgabe soll wie `go version go1.xx.yy ...` aussehen.
Soll das nicht der Fall sein, schlagen Sie auf
der offiziellen Webseite nach, 
[wie Go installiert werden soll](https://go.dev/doc/install).

Ausführen besteht immer aus mindestens zwei Phasen — kompilieren und tatsächlich ausführen.
Go bietet zwei Möglichkeiten an:

1. `go run quellcode.go` — Ihr Go-Programm wird automatisch kompiliert und gleich im Anschluss
   ausgeführt.
   Das funktioniert nur für die Quellcodedateien, die mit der Zeile `package main` anfangen (siehe
   unten).
   Das Python-Äquivalent zu diesem Kommando ist `python3 quellcode.py`.
2. `go build -o binary quellcode.go` — aus `quellcode.go` wird eine Binärdatei erzeugt.
   Wenn `quellcode.go` mit `package main` beginnt, darf die Binärdatei ausgeführt werden.
   Dies geschieht mithilfe von `./binary`.
   Der Einstiegspunkt ist immer die Funktion `func main() {}`.

Dokumentation zu diesen Kommandos bekommen Sie mit `go help`.

[ER] Legen Sie eine Datei namens `go-basics1.go` an und kopieren Sie den Quellcodeabschnitt in 
diese Datei:

```go
[INCLUDE::include/hello_world.go]
```

[EC] Führen Sie nun das Programm mittels `go run go-basics1.go` aus.

Jetzt tanken wir Grundwissen und schreiben dann damit unser erstes Programm.
Wer mag, kann gern schon mal unten schauen, was für eine Aufgabe da kommt,
darüber nachdenken, was man dafür braucht, und dann beim Durcharbeiten der Theoriesachen
immer gleich den jeweiligen Teil hinschreiben.

Das Umgekehrte machen Sie aber bitte nicht: Loshacken und nur das Minimum lesen, 
was dafür unverzichtbar scheint.
Denn dann verpassen Sie viele der wichtigen und interessanten Eigenschaften von Go,
das nämlich seinen ganz eigenen Touch als Programmiersprache hat und diverse Eigenschaften mitbringt,
die schrullig wirken können, tatsächlich aber ziemlich schlau und praktisch sind.


### Variablen und primitive Datentypen

Es existieren folgende Namenskonventionen:

- standardmäßig sind alle Variablen/Funktionen in `camelCase` definiert;
- falls eine Variable/Funktion öffentlich sein soll, wird `PascalCase` benutzt;
- ebenso für Konstanten — `SCREAMING_SNAKE_CASE` gilt in Go als nicht idiomatisch und wird in der
  [offiziellen Go-Stilkonvention](https://google.github.io/styleguide/go/guide)
  nicht empfohlen.

Nun lesen Sie bitte die folgenden Punkte selbst nach und beantworten Sie dann die Fragen:

- [Variablen](https://go.dev/tour/basics/8)
- [Variablen mit Initialisierung](https://go.dev/tour/basics/9) 
- [kurze Variablendeklarationen](https://go.dev/tour/basics/10)

[EQ] Wo kann eine Variable mit `:=` initialisiert werden?

- [Primitive Datentypen](https://go.dev/tour/basics/11)
- [Nullwerte](https://go.dev/tour/basics/12)
- [Typinferenz](https://go.dev/tour/basics/14)
- [Konstanten](https://go.dev/tour/basics/15)

[EQ] Mit diesem Hintergrundwissen: Was ist der Fehler im folgenden Codeabschnitt?

```go
x := 42
var answer int32 = x
```

[HINT::Was ist der Typ von `x`?]
Der automatisch hergeleitete Typ für alle Ganzzahlen ist `int`, folglich ist `x` von Typ `int`.

[HINT::Was ist der Typ von `answer`?]
Der Typ von `answer` haben wir in dem Beispiel explizit angegeben — `int32`.
[ENDHINT]
[ENDHINT]


### Kontrollstrukturen (if/switch/for)

Kontrollstrukturen sind relativ ähnlich zu denen in Python, mit dem Unterschied:
In Go dürfen `if` und `switch` eine **Initialisierungsanweisung** besitzen.
Alle Variablen, die in der Initialisierungsanweisung definiert wurden, sind nur in dem `if`/`switch`
Block erreichbar.

**Nachteil:** Der Ausdruck wird komplizierter und die
Schreibweise ist zum Lesen gewöhnungsbedürftig.

**Vorteil:** Begrenzung des Geltungsbereichs (Scoping).
Was in der Initialisierungsanweisung definiert wurde, darf nur in dem entsprechenden Ausdruck
benutzt werden.


### if

Allgemeines Muster (`else`-Zweig und die Initialisierungsanweisung sind optional):

```go
if initialisation; condition {

} else {

}
```

Beispiel:

```go
// diese Funktion gibt zwei Werte zurück - ähnlich wie Funktionen in Python,
// können Funktionen in Go ein "tuple" zurückgeben
if data, err := client.RequestData(); err != nil {
    fmt.Println("received an error", err)
} else {
    fmt.Println("received data", data)
}
```

[NOTICE]
In dem obigen Beispiel wird `err != nil` überprüft. Warum?

Viele Funktionen in Go können einen `error` zurückgeben — einfach als zusätzlichen Rückgabewert.
Der Nullwert vom Typ `error` ist `nil`:
Ein solcher Check ist die Überprüfung, ob die anderen Rückgabewerte valide sind und benutzt werden
dürfen.

Falls etwas fehlgeschlagen ist, gibt es einen `error`; ansonsten ist `err == nil`.
[ENDNOTICE]


### switch

Ein Switch prüft den Wert einer Variable und führt je nach Wert verschiedene Code-Blöcke aus.

**Aufbau:**

* `switch` + (Initialisierungsanweisung) + Variable;
* `case` + Wert: Code der ausgeführt wird;
* (optional) `default`: wird ausgeführt, wenn kein `case` passt.

Lesen Sie selbstständig nach, wie ein Switch benutzt werden kann:

- [Switch](https://go.dev/tour/flowcontrol/9)
- [Auswertungsreihenfolge](https://go.dev/tour/flowcontrol/10)
- [switch true](https://go.dev/tour/flowcontrol/11)

[NOTICE]
`if-elif-else`-Blöcke sind in der Regel flexibler; bei `switch` ist jedoch schneller zu erfassen,
was da passiert.
[ENDNOTICE]


### for

Hier ist eine kurze Übersicht von for-Schleifen im Vergleich zu Python:


#### Endlosschleife

```go
// Go
for {
    ...
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python
while True:
    ...
```
[ENDFOLDOUT]


#### Eine pythonartige Schleife

```go
// Go
for i := range 5 {      // i aus der Menge {0, 1, 2, 3, 4}
    ...
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python
for i in range(5):
    ...
```
[ENDFOLDOUT]


#### Eine C-artige Schleife

```go
// Go
for i := 0; i < 10; i++ {
...
}

// oder
i := 0
for i < 10 {
...
i++
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python
i = 0
while i < 10:
    ...
    i += 1
```
[ENDFOLDOUT]


#### Das Schlüsselwort `range`

Für Iterationen über Zeichenketten, Listen, Maps und Kanäle (lernen Sie später kennen)
wird das Schlüsselwort `range` benutzt:

```go
for ... := range list/dict { ... }
```

Dieser Ausdruck erkennt automatisch, wie viele Rückgabewerte erwartet werden, und verhält sich
unterschiedlich:

- ein Rückgabewert: `range` gibt Index (bei Listen) oder Schlüssel (bei Maps) zurück;
- zwei Rückgabewerte: `range` gibt Index und Wert (bei Listen) oder Schlüssel und Wert (bei Maps)
  zurück.


#### Iteration über eine Liste

```go
// Go

// nur Indizes
for index := range someList {
    ...
}

// Indizes und Werte
for index, value := range someList {
    ...
}

// nur Werte — Index explizit ignorieren 
for _, value := range someList {
    ...
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python

# nur Indizes
for index in range(len(someList)):
    ...

# Indizes und Werte
for index, value in enumerate(someList):
    ...

# nur Werte
for value in someList:
    ...
```
[ENDFOLDOUT]


#### Iteration über eine Map (eine Hashtabelle/ein Wörterbuch)

```go
// Go

// nur Schlüssel
for key := range someHashMap {
    ...
}

// Schlüssel und Werte
for key, value := range someHashMap {
    ...
}

// nur Werte — Schlüssel explizit ignorieren
for _, value := range someHashMap {
    ...
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python

# nur Schlüssel
for key in some_dict:
    ...

# Schlüssel und Werte
for key, value in some_dict.items():
    ...

# nur Werte
for value in some_dict.values():
    ...
```
[ENDFOLDOUT]


### Rückgabewerte ignorieren

In Go müssen alle Variablen benutzt werden, sonst gibt es einen Kompilierungsfehler.
Falls eine Variable nirgendwo im Programm benutzt wird, muss sie explizit ignoriert werden.
Das geschieht mittels einer Zuweisung des Wertes **dem leeren Bezeichner** (blank identifier):

```go
// Die Funktion gibt ein Paar 'width, height' zurück
// 'height' wird nicht benutzt und muss explizit ignoriert werden
w, _ := getWidthAndHeight()
```

Dieses Konstrukt haben Sie bereits oben kennengelernt, für `for`-Schleifen:

```go
for _, value := range someList {
    ...
}
```

Der leere Bezeichner hat noch weitere Anwendungen:
[Effective Go: Blank Identifier](https://go.dev/doc/effective_go#blank).


### Typumwandlung

Generell lässt sich diese Prozedur in Go sowie in Python folgendermaßen beschreiben:
_T(v)_ konvertiert den Wert _v_ zum Typen _T_. Das gilt vor allem für Zahlen:

```go
var x int8 = 42
y := int64(x) // kein Problem

var x int64 = 420
y := int8(x) // kann ein Problem werden; y ist -92
```

[WARNING]
Das Problem: 8 Bits können viel weniger Zahlen darstellen als 64 Bits.

Wenn ein `int64`-Wert zu einem `int8`-Wert umgewandelt wird, werden Zahlen aus dem Wertebereich von
`int64` auf diese von `int8` abgebildet.
Dabei ist nicht garantiert, dass es am Ende dieselbe Zahl ist, und Go schmeißt keinen Fehler.
Das führt dazu, dass solche subtilen Über- oder Unterlauf-bezogenen Defekte doch in Ihrem Programm
auftauchen können.

Das ist bei dem obigen Beispiel passiert:

    x = 420 = 0001 1010 0100 (nur die unteren 12 Bits)
    y = int8(x) — nimmt die unteren 8 Bits
    y = 1010 0100 — das erste Bit ist 1, also muss die Zahl negativ sein 
    => Zweierkomplement
    => ~(1010 0100) + 1
    => 01011011 + 1 
    => 01011100 
    => 2^6 + 2^4 + 2^3 + 2^2 = 92 (-92, da negativ)

[Grundwissen zur Darstellung von negativen Zahlen: Rechnerarchitektur, Folien von Prof. Dr.-Ing. 
Jochen Schiller](https://ftp.mi.fu-berlin.de/pub/schiller/inverted/CA/TI%20II%20CH02%20Data%20Arithmetic.pdf)
(ab Folie 21).
[ENDWARNING]

Eine Typumwandlung von einer Zeichenkette zu einer Zahl ist immer kniffelig und kann sowohl in Go
als auch in Python fehlschlagen.

```go
// Go
stringValue := "42"
integerValue, err := strconv.ParseInt(stringValue, 10, 64) // Basis 10, 64-Bit Integer
if err != nil {
    // Typumwandlung fehlgeschlagen
}
```

[FOLDOUT::Python-Äquivalent]
```python
# Python
stringValue = "42"
try:
    integerValue = int(stringValue)
except ValueError as e:
    # Typumwandlung fehlgeschlagen
```
[ENDFOLDOUT]

Eine umgekehrte Typumwandlung geschieht einfacher — es wird eine neue Zeichenkette erstellt:

```go 
// Go
integerValue := 42
stringValue := fmt.Sprintf("%v", 42)
```

[FOLDOUT::Python-Äquivalent]
```python
# Python
integerValue = 42
stringValue = str(integerValue)
```
[ENDFOLDOUT]

`fmt.Sprintf()` ist eine Formatierungsfunktion, deren Syntax stark von `printf` in C inspiriert
wurde.
Sie bekommt eine Formatierungszeichenkette mit Platzhaltern und eine beliebige Anzahl von Werten,
die anstatt der Platzhalter angezeigt werden, und gibt eine formatierte Zeichenkette zurück.

`%v` ist ein universeller Platzhalter (steht für `value`), um den Wert einer Variable ausgeben zu
lassen.
Der Datentyp wird dann automatisch erkennt.

[FOLDOUT::Die anderen relativ oft benutzten Platzhalter]

- `%d` — eine Ganzzahl
- `%s` — eine Zeichenkette
- `%b` — eine Ganzzahl in Binärdarstellung
- `%p` — ein Zeiger als Integer-Adresse
- `%f` — eine Fließkommazahl
- `%T` — der Typ einer Variable

Die komplette Liste finden Sie in der
[Dokumentation von fmt: Package Overview](https://pkg.go.dev/fmt#pkg-overview).
[ENDFOLDOUT]

### Programmieren

[ER] Um alle oben genannten Konzepte auszuprobieren, implementieren Sie hier Fizzbuzz.

Spezifikation:

- Das Programm soll eine ganze Zahl _n_ von der Kommandozeile auslesen, mittels
  `strconv.ParseInt(input, 10, 64)` zu `int64` umwandeln und
- in einer `for`-Schleife alle ganzen Zahlen von 1 bis _n_ (inklusive) durchgehen und jeweils
    - "fizz" ausgeben, wenn die Zahl durch 3 teilbar ist
    - "buzz" ausgeben, wenn die Zahl durch 5 teilbar ist
    - "fizzbuzz" ausgeben, wenn die Zahl sowohl durch 3 als auch durch 5 teilbar ist
    - die Zahl selbst ausgeben, wenn die Zahl weder durch 3 noch durch 5 teilbar ist

Diese Vorlage dürfen Sie als Ausgangspunkt benutzen:

```go
[INCLUDE::include/go-basics1.go]
```

[NOTICE]
`strconv.ParseInt()` gibt zwei Werte zurück — eine Zahl und einen `error`.

In dieser Aufgabe dürfen Sie den zweiten Wert (`error`) explizit ignorieren.
[ENDNOTICE]

[EC] Führen Sie das Programm mittels `go run go-basics1.go` aus und geben Sie 20 ein.
[ENDSECTION]

[SECTION::submission::information,trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
**Kommandoprotokoll**
[PROT::ALT:go-basics1.prot]

**Lösungen**

[INCLUDE::ALT:]

Musterlösung der Programmieraufgabe siehe hier: [TREEREF::/Sprachen/Go0/go-basics1.go]
[ENDINSTRUCTOR]
