title: Grundlagen von Go im Kontext von Python
stage: alpha
timevalue: 2.5
difficulty: 2
requires: go-ide
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

Go wurde als eine pythonähnliche Alternative für die Entwickler bei Google konzipiert, die C++ als zu komplex empfanden. 
Daher sind die folgenden Merkmale entstanden:

- Statische Typisierung und Laufzeiteffizienz (wie C/C++);
- Lesbarkeit und Benutzerfreundlichkeit (wie Python);
- ein leistungsfähiges Nebenläufigkeits- und Parallelitätsmodell.

Insgesamt ergibt das eine flexible und ziemlich effiziente Programmiersprache, 
die besonders in der Entwicklung von Programmierwerkzeugen (Docker/Kubernetes) und Web-Backends beliebt geworden ist.

[ENDSECTION]

[SECTION::instructions::detailed]

### Ein Go-Programm ausführen

Stellen Sie sicher, dass Sie eine gültige Go-Installation auf Ihrem Rechner haben. 
Tippen Sie `go version` in die Kommandozeile:
Die Ausgabe soll wie `go version go1.xx.yy ...` aussehen. 
Soll das nicht der Fall sein, schlagen Sie in [PARTREF::go-ide] oder online nach, wie Go installiert werden soll.

Ausführen besteht immer aus mindestens zwei Phasen — kompilieren und tatsächlich ausführen.
Go bietet zwei Möglichkeiten an:

1. `go run quellcode.go` — Ihr Go-Programm wird automatisch kompiliert und gleich im Anschluss ausgeführt.
    Das funktioniert nur für die Quellcodedateien, die mit der Zeile `package main` anfangen (siehe unten).
    Das Python-Äquivalent zu diesem Kommando ist `python3 quellcode.py`. 
2. `go build -o binary quellcode.go` — aus `quellcode.go` wird eine Binärdatei erzeugt.
    Wenn `quellcode.go` mit `package main` beginnt, darf die Binärdatei ausgeführt werden.
   Dies geschieht mithilfe von `./binary`.

### Package/import

Alle Quellcodedateien müssen einem **Paket** zugeordnet sein.
Dieses wird am Anfang der Datei in der Zeile `package {xyz}` angegeben, wobei `{xyz}` der Name Ihres Pakets ist.

Die Paket- und Modulverwaltung in Go ähnelt derjenigen in Python.

- Modul
    - **Python:** eine Datei, die auf `.py` endet.
    - **Go:** ein Verzeichnis mit der Datei `go.mod`, wo der Modulname, die Abhängigkeiten und die Version deklariert 
      sind. TODO_1: Man möchte ein Beispiel sehen, ein Link reicht.
- Paket
    - **Python:** ein Verzeichnis mit mehreren `.py`-Dateien und optional einer `__init__.py` Datei.
      Diese Datei wird beim Importieren des Pakets ausgeführt.
    - **Go:** ein Verzeichnis namens z.B. `xyz`, in dem alle Quellcodedateien mit der Zeile
      `package xyz` anfangen müssen.
      Auf dieser Ebene wird Sichtbarkeit geregelt: Alle `lowercase` Deklarationen sind privat, alle `Capitalized` 
      Deklarationen sind öffentlich (public/exported) und aus anderen Paketen sichtbar.
      Merkhilfe: Große Buchstaben geben große Sichtbarkeit.

Ein Paketname unterliegt Sonderregeln: `main`.
Dieses Paket ist das Hauptpaket; darin liegt das ausführbare Programm.
Einstiegspunkt ist immer die Funktion `main()`.
Dies entspricht `public static void main(String[] args)` in Java oder 
`int main()` in C. 

Alle anderen Paketnamen interpretiert der Compiler als Bibliotheken — diese können nicht 
mittels `go run` ausgeführt werden. 
Pakete entsprechen der Verzeichnisstruktur eines Moduls: Gibt es in einem Modul `my_module` Verzeichnisse `src`, `utils`
und `test`, so beginnen die Quellcodedateien entsprechend mit den Zeilen `package src`, `package utils` oder 
`package test`.

TODO_1: Das ist also ganz anders als in Python? 
Dort sind Module klein, Pakete größer, aber Pakete sind auch Module. 
Hier sind Module größer und enthalten Pakete? Was ist jeweils deren Zweck? Erklären!

#### Wie werden Module/Pakete importiert?

Hier gibt es zwei mögliche Fälle:

1. Importieren von Paketen innerhalb eines Moduls: `import module_name/package_name`.
   Dabei müssen Sie aufpassen, dass Ihr Abhängigkeitsgraph azyklisch bleibt.
2. Externe Module/Bibliotheken
    - in dem Root-Verzeichnis des Moduls `go get example.com/some/package` ausführen und dann in dem Quellcode 
     importieren  TODO_1 verstehe ich nicht.
    - zuerst in dem Quellcode importieren und danach aus dem Root-Verzeichnis des Moduls `go get` ausführen. 
   So werden alle nötigen Bibliotheken automatisch heruntergeladen und installiert. 

TODO_1: Das sollte man jetzt ausprobieren, sonst wird das hier zu trocken und zu viel Theorie.

### Variablen und primitive Datentypen

Ähnlich zu Python gibt es 4 wichtigste primitive Datentypen:

* `int`: eine ganze Zahl mit Vorzeichen (signed);  TODO_1: Wie groß?
* `float64`: eine Gleitkommazahl;
* `string`: eine Zeichenkette;
* `bool`: ein boolescher Wert, `true` oder `false`;

und einen zusätzlichen `byte` (`uint8`): 8 Bits von Information (wichtig im Kontext von Dateioperationen oder Netzwerken).
TODO_1: D.h. z.B. 16-bit Integers gibt es gar nicht? So klingt obiger Satz: "einen zusätzlichen".

In Go wird manchmal zwischen Deklaration und Definition unterschieden. 
Deklaration ist nichts anderes als Definition mit Default/Null-Werten: `0` für Zahlen, `""` für Zeichenketten, `false` für boolesche Werte.

```go
var myname string             // deklarieren
myname = "gopher"             // definieren
var myname string = "gopher"  // beide Aktionen kombiniert

myname := "gopher"            // oder den konkreten Datentyp
var myname = "gopher"         // herleiten lassen  TODO_1: sind diese beiden Formen gleichwertig?

width, height := 1920, 1080 // mehrere Variablen auf einmal
```

[NOTICE]

Falls es sich um primitive Datentypen handelt, werden nur `int`, `float64` `string` und `bool` hergeleitet:
```go
// kurze Schreibweise               // volle Schreibweise
number := 42                        var number int = 42
pi := 3.1415                        var pi float64 = 42
name := "gopher"                    var name string = "gopher"
truth := true                       var truth bool = true
```

[ENDNOTICE]

[FOLDOUT::Warum gibt es ein `float64`, aber kein `int64`?]

Es gibt mehr Typen für Zahlen als oben angeführt sind. Hier ist die vollständige Liste:

* ganze Zahlen mit Vorzeichen: `int` , `int8` , `int16` , `int32` (`rune`) , `int64`;
* ganze Zahlen ohne Vorzeichen: `int` , `uint8` (`byte`), `uint16` , `uint32` , `uint64` , `uintptr`;
* Gleitkommazahlen: `float32` `float64`;
* Komplexe Zahlen: `complex64` `complex128`.

[ENDFOLDOUT]

Komplexere Datentypen werden ohne Ausnahmen hergeleitet, daher ist die kurze Schreibweise im Go-Universum bevorzugt.
TODO_1: Hergeleitet? Wie denn? Was denn? Wo denn?

#### Konstanten

Konstanten werden mit dem Schlüsselwort `const` deklariert und müssen bei Deklaration definiert werden. 
Sie dürfen außerdem nur primitive Datentypen beinhalten und müssen sich im Paketkontext befinden (auf Dateiebene).
Üblicherweise werden Konstanten ganz oben in der Datei deklariert.
Es gibt keine besonderen Namenskonventionen, daher gelten hier die gleichen Regeln wie bei normalen Variablen: 
`camelCase` oder `PascalCase`, je nachdem ob die Konstante öffentlich sein muss.
TODO_1: camelCase kannten wir bis hierher nicht; solche Konventionen sind aber wichtig.

```go
const pi = 3.1415926
const Pi float64 = 3.1415926

const pi float64  // --> error: Missing value in the const declaration
```

#### Als Block deklarieren

```go
const (
    pi  = 3.1415
    e   = 2.7183
    
    // da pi und e beide konstant sind, ist ihr Produkt ebenso konstant
    product = pi * e
)

var (
    name    = "Max"
    surname = "Mustermann"
)
```


### Kontrollstrukturen (if/switch/for)

Kontrollstrukturen sind relativ ähnlich zu denen in Python, mit dem Unterschied: 
In Go dürfen `if` und `switch` eine **Capture Group** definieren. 
Das ist eine oder mehrere Variablen, die nur in dem `if`/`switch` Block erreichbar sind. 

### if

Allgemeines Muster (`else`-Zweig und Capture Group sind optional):
```go
if capture_group; condition {

} else {

}
```

Beispiel:
```go
if data, err := client.RequestData(); err != nil {
    fmt.Println("received an error", err)
} else {
    fmt.Println("received data", data)
}
```
TODO_1: Sieht aus wie "eine komplizierte Zeile statt zwei einfache Zeilen". Was ist da toll dran?
Außerdem werden hier offenbar zwei Werte zurückgegeben: Kennen wir noch nicht. Ist das wie tuple in Python? 

### switch

Es gibt zwei Alternativen von `switch` im Python-Universum: `if-elif-else`-Block oder `match-case`.
`Switch` darf ebenfalls eine Capture Group besitzen.
TODO_1: Verwirrend ausgedrückt. Was hat denn nun `switch` mit `match-case` zu tun? Lieber Python nicht erwähnen?

```go
switch x := randomIntUnder10(); x {
case 0: fmt.Println("it's 0!")
case 4: fmt.Println("it's 4!")
case 8: fmt.Println("it's 8!")
default: fmt.Println("it's something different...")
}
```

`if-elif-else`-Blöcke sind in der Regel flexibler.
TODO_1: Bitte positiv ausdrücken: bei `switch` ist schneller zu erfassen, was da passiert.

[FOLDOUT::Benutzen auf eigene Gefahr]
TODO_1: Ziemlich verwirrender Exkurs. Swift? Kotlin? Häh?? Lieber weglassen.

Ein `if-else`-Block hat immer zwei Zweige — einen für `true` und einen für `false`. 
Bei einem `switch`-Block sind das eigentlich nur zwei mögliche Fälle:

```go
switch bool_value {
case true: ...
case false: ...
}
```

Könnte man die Bedingung invertieren? Eigentlich schon:

```go
switch true {
case 0 < x && x < 20: ...
case 20 <= x && x < 40: ...
case 40 <= x && x < 60: ...
}
```

Das ist eine kürzere Form von einem klassischen `if-elif-else`-Block.
Sie ist besonders vorteilhaft in Programmiersprachen, wo `switch`-Blöcke Werte zurückgeben dürfen (beispielsweise Swift 
oder Kotlin):
```swift
let message = switch true {
case age < 0: "you haven't been born yet"
case age >= 18: "you're an adult!"
default: "you're probably going to school"
}
```
[ENDFOLDOUT]

### for

Hier ist eine kurze Übersicht von for-Schleifen im Vergleich zu Python:

#### Endlosschleife
```go
// Go
for {
    ...
}
```

```python
# Python
while True:
    ...
```

#### Klassische C-Schleife
TODO_1: Die ist für unsere Studis nicht klassisch, sondern unbekannt.
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

```python
# Python
i = 0
while i < 10:
    ...
    i += 1
```

#### Iteration über Indizes einer Liste
```go
// Go
for index := range someList {
    ...
}
```

```python
# Python
for index in range(len(someList)):
    ...
```

#### Iteration über Indizes und Werte einer Liste
```go
// Go
for index, value := range someList {
    ...
}
```
TODO_1: Das ist verblüffend. Wieso taugt `range` für `index` ebenso wie für `index, value`? 

```python
# Python
for index, value in enumerate(someList):
    ...
```

#### Iteration über Schlüssel-Wert-Paare eines Wörterbuchs (einer Hashtabelle)
```go
// Go
for key, value := range someHashMap {
    ...
}
```

```python
# Python
for key, value in someHashMap.items():
    ...
```

### Typumwandlung

Generell lässt sich diese Prozedur in Go sowie in Python folgendermaßen beschreiben: 
_T(v)_ konvertiert den Wert _v_ zum Typen _T_. Das gilt vor allem für Zahlen.

[WARNING]
Go erlaubt Über- oder Unterlauf, wenn beispielsweise `int64` zu `int8` umgewandelt wird.
TODO_1: Was heißt das? Wirkung?

Falls eine solche Operation absolut notwendig ist, denken Sie daran, den Erfolg Ihrer Typumwandlung zu überprüfen.

[ENDWARNING]

Eine Typumwandlung von einer Zeichenkette zu einer Zahl ist immer kniffelig und kann sowohl in Go als auch in Python 
fehlschlagen.
```go
// Go
stringValue := "42"
integerValue, err := strconv.ParseInt(stringValue, 10, 64) // Basis 10, 64-Bit Integer
if err != nil {
    // Typumwandlung fehlgeschlagen
}
```

Python-Äquivalent:
```python
# Python
stringValue = "42"
try:
    integerValue = int(stringValue)
except ValueError as e:
    # Typumwandlung fehlgeschlagen
```

Eine umgekehrte Typumwandlung geschieht einfacher — es wird eine neue Zeichenkette erstellt:
```python
# Python
integerValue = 42
stringValue = str(integerValue)
```

```go 
// Go
integerValue := 42
stringValue := fmt.Sprintf("%d", 42)
```
[`fmt.Sprintf()`](https://pkg.go.dev/fmt#pkg-functions) ist eine Formatierungsfunktion, deren Syntax stark von `printf` in C inspiriert wurde.

### Programmierung

Nun ist es Zeit, die kennengelernten Konzepte in der Praxis einzusetzen.

Sie bekommen ein Python-Programm, welches eine Liste von Noten erhält und diese validiert.
Falls die Noten valide sind, wird der Durchschnitt für jede Person berechnet und als "sehr gut/gut/befriedigend/ausreichend" auf der Kommandozeile ausgegeben;
ansonsten wird eine Warnung ausgegeben und das Programm überspringt die ungültigen Daten.

Ihre Aufgabe besteht darin, dieses Python-Programm in Go zu übersetzen 
(das ist jedoch nicht notwendig; Sie dürfen das Programm auch nach der oben angegebenen Beschreibung implementieren).

Das Go-Programm wird aus 3 Paketen bestehen:

- `validator` - dort werden Sie zwei vordefinierte Funktionen implementieren müssen;
- `converter` - dort werden Sie ebenso zwei vordefinierte Funktionen implementieren müssen;
- `main` - das Hauptprogramm.

[NOTICE]

Für die folgende Aufgabe brauchen Sie ein bisschen Verständnis von Slices (Python: Listen) und Maps (Python: Dictionaries).

```go
// erstellen
s := make([]string)                 // Slice
m := make(map[string]float64)       // Map

// Element einfügen
s = append(s, "hi there")
m["hi there"] = 42.0
```

Später lernen Sie noch viel mehr dazu, aber für diese Aufgabe soll dieses Wissen schon ausreichen.
Viel Erfolg!

[ENDNOTICE]

1. [ER] Legen Sie ein Verzeichnis `grade_converter` an und führen Sie darin `go mod init grade_converter` aus. 
   So initialisieren Sie ein Modul.
   Legen Sie außerdem eine Datei `main.go` an, die mit `package main` anfängt und die Funktion `func main() {}` beinhaltet — das ist der Einstiegspunkt Ihres Programms.
2. [ER] In `grade_converter`, erstellen Sie zwei weitere Verzeichnisse: `validator` und `converter`. 
   Kreieren Sie in den Verzeichnissen entsprechend zwei Dateien — `validator.go` und `converter.go` (die Dateien dürfen beliebig heißen, solange sie unter den richtigen Verzeichnissen sind).
   Die Dateien müssen jeweils mit `package validator` und `package converter` anfangen.
3. [ER] `validator.go`-Vorlage:
```go
[INCLUDE::snippets/go-basics-validator.go]
```
4. [ER] `converter.go`-Vorlage:
```go
[INCLUDE::snippets/go-basics-converter.go]
```
5. [ER] `grade_converter.py` als Referenz
```python
[INCLUDE::snippets/go-basics-grades.py]
```
6. [ER] Kopieren Sie die `fake_csv` Zeichenkette als Konstante in Ihr Go-Programm und implementieren Sie die gewünschte Funktionalität. 
   `fake_csv` muss gleich bleiben.

### Testen

[EC] Führen Sie Ihr Programm mittels `go run grade_converter.go` aus.


[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Quellcode.md]

Geben Sie **eine** Quellcodedatei ab: `grade_converter.go`.
Kopieren Sie den kompletten Inhalt von `validator.go` und `converter.go` in diese Datei um und stellen Sie sicher, dass die Endstruktur ungefähr so aussieht:

```go
// region validator.go

package validator
...

// endregion

// region converter.go

package converter
...

// endregion

// region main

package main

func main() {
    ...
}

// endregion

```

Dies ist zwar keine valide Go-Quellcodedatei an sich, aber so ist die Abgabe viel einfacher.

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]

Folgende Aspekte sind bei der Korrektur wichtig:

1. Funktionalität — das Programm tut, was es soll;
2. Struktur — die drei Pakete müssen vorhanden sein und benutzt werden, 
   das erkennt man an Zeilen `import` und `package` in jeweiligen Bereichen der abgegebenen Datei `grade_converter.go`.
3. Fehlerbehandlung muss nicht alles abdecken, aber sie muss da sein.
   `Validate`-Funktionen sollten eine informative Nachricht in dem Fehler zurückgeben.

Ansonsten ist dies eine Lernaufgabe. 
Der Punkt ist, dass die Studierenden die oben vorgestellten Konzepte im Zusammenhang miteinander benutzen.
[ENDINSTRUCTOR]
