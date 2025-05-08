title: Grundlagen von Go im Kontext von Python
stage: alpha
timevalue: 3.5
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
Soll das nicht der Fall sein, schlagen Sie auf [der offiziellen Webseite](https://go.dev/doc/install) nach, wie Go installiert werden soll.

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

- **Modul:** ein Verzeichnis mit der Datei `go.mod`, wo der Modulname, die Abhängigkeiten und die Version deklariert 
  sind. 
  Unter [Anatomy of go.mod](https://encore.cloud/guide/go.mod) können Sie sich ein Beispiel anschauen.
- **Paket:** ein Verzeichnis namens z.B. `xyz`, in dem alle Quellcodedateien mit der Zeile
  `package xyz` anfangen müssen.
  Auf dieser Ebene wird Sichtbarkeit geregelt: Alle `lowercase` Deklarationen sind privat, alle `Capitalized` 
  Deklarationen sind öffentlich (public/exported) und aus anderen Paketen sichtbar.
  Merkhilfe: Große Buchstaben geben große Sichtbarkeit.

[NOTICE]

Falls Sie Ihr Modul veröffentlichen möchten, **muss** der Modulname mit der URL übereinstimmen, wo sich das Modul befindet.

**Beispiel:**

- Sie legen ein Repo namens `my_awesome_golang_module` auf [Github](https://github.com) an,
  welches dann über `https://github.com/username/my_awesome_golang_module` erreichbar ist.
- Sollte das Repo ein Modul sein, so muss die `my_awesome_golang_module/go.mod`-Datei mit der folgenden Zeile anfangen: 
  `module github.com/username/my_awesome_golang_module`

[ENDNOTICE]

Ein Paketname unterliegt Sonderregeln: `main`.
Dieses Paket ist das Hauptpaket; darin liegt das ausführbare Programm.
Einstiegspunkt ist immer die Funktion `main()`.
Dies entspricht `public static void main(String[] args)` in Java oder 
`int main()` in C. 

Alle anderen Paketnamen interpretiert der Compiler als Bibliotheken — diese können nicht 
mittels `go run` ausgeführt werden. 
Pakete entsprechen der Verzeichnisstruktur eines Moduls: Gibt es in einem Modul `my_module` Verzeichnisse `src`, `utils`
und `test`, so beginnen die Quellcodedateien in den Verzeichnissen entsprechend mit den Zeilen `package src`, `package utils` oder 
`package test`.


#### Was ist der Zweck?

**Module** dienen der Versionierung und Nachverfolgung externer Abhängigkeiten eines Projekts.
Explizite Versionierung stellt sicher, dass Builds reproduzierbar sind.

**Pakete** dienen dazu, Quellcode zu organisieren. Darunter:

  - Zusammengehörige Funktionen/Typen gruppieren
  - Sichtbarkeit kontrollieren
  - Wiederverwendbarkeit erleichtern

Meistens wird Ihr Projekt ein einziges Modul sein, welches mehrere Pakete enthält.


#### Wie werden Module/Pakete importiert?

Die Syntax einer Import-Anweisung:

```go
import (optionales Alias) "Modulname"
```

Beispiel:

```go
import rl "github.com/gen2brain/raylib-go/raylib"
```

Hier gibt es zwei mögliche Fälle:

1. Importieren von Paketen innerhalb eines Moduls: `import module_name/package_name`.
   Dabei müssen Sie aufpassen, dass Ihr Abhängigkeitsgraph azyklisch bleibt.
2. Externe Module/Bibliotheken — beispielsweise ein Modul importieren, welches sich unter `github.com/username/module_name` befindet.
    - in dem Root-Verzeichnis des Moduls `go get github.com/username/module_name` ausführen und dann im Quellcode 
     importieren;
    - **oder** zuerst im Quellcode importieren (`import "github.com/username/module_name"`) und danach aus dem Root-Verzeichnis des Moduls `go get` ausführen. 
   So werden alle nötigen Bibliotheken automatisch heruntergeladen.


### Ausprobieren

[ER] Legen Sie ein öffentliches Github-Repo an. 
Den Modulnamen dürfen Sie beliebig wählen (um unerwartete Fehler zu vermeiden, benutzen Sie im Modulnamen keine Sonderzeichen).

[ER] Das Repo muss zwei Dateien beinhalten: `go.mod` und `main.go`. 
Bei der Datei `go.mod` dürfen Sie die obige Bemerkung durchspielen.
Die Datei `main.go` soll folgendermaßen aussehen:

```go
package %replace_with_your_module_name%

import "fmt"

func HiFromRemote() {
    fmt.Println("Hi from remote module!")
}
```

[ER] Kreieren Sie nun ein lokales Projekt/Modul. Dieses darf beliebig heißen.

[ER] Legen Sie eine Datei `go.mod` an, und deklarieren Sie dort den Modulnamen.

[ER] Legen Sie eine weitere Datei `main.go` an und kopieren Sie den folgenden Quellcodeabschnitt in diese Datei:

```go
package main

import m %"replace_with github.com/your_username/your_module"%

func main() {
    m.HiFromRemote()
}
```

Und jetzt im Root-Verzeichnis des lokalen Moduls folgende Befehle ausführen:

[EC] `go get`

[EC] `go run main.go`

Die Ausgabe müsste "Hi from remote module!" sein.


### Variablen und primitive Datentypen

Es existieren folgende Namenskonventionen:
- standardmäßig sind alle Variablen/Funktionen in `camelCase` definiert;
- falls eine Variable/Funktion öffentlich sein muss, so wird `PascalCase` benutzt.

Ähnlich zu Python gibt es 4 wichtigste primitive Datentypen:

* `int`: eine ganze Zahl mit Vorzeichen (signed).
  Die Größe eines `int` passt sich automatisch an die Systemarchitektur an:
    - 32 Bit (4 Bytes) auf 32-Bit-Systemen
    - 64 Bit (8 Bytes) auf 64-Bit-Systemen
* `float64`: eine Gleitkommazahl
* `string`: eine Zeichenkette
* `bool`: ein boolescher Wert, `true` oder `false`

[FOLDOUT::Warum gibt es ein `float64`, aber kein `int64`?]

Doch, gibt es. Hier ist die vollständige Liste:

* ganze Zahlen mit Vorzeichen: `int` , `int8` , `int16` , `int32` (`rune`) , `int64`;
* ganze Zahlen ohne Vorzeichen: `int` , `uint8` (`byte`), `uint16` , `uint32` , `uint64` , `uintptr`;
* Gleitkommazahlen: `float32` `float64`;
* Komplexe Zahlen: `complex64` `complex128`.

[ENDFOLDOUT]

In Go wird manchmal zwischen Deklaration und Definition unterschieden. 
Deklaration ist nichts anderes als Definition mit Default/Null-Werten: `0` für Zahlen, `""` für Zeichenketten, `false` für boolesche Werte.

```go
var myname string               // deklarieren
myname = "gopher"               // definieren
var myname string = "gopher"    // beide Aktionen kombiniert

myname := "gopher"              // oder den konkreten Datentyp
var myname = "gopher"           // herleiten lassen. Beide Formen sind gleichwertig

width, height := 1920, 1080     // mehrere Variablen auf einmal
```

In Go haben alle Variablen, deren Typ ein Interface ist, den Standardwert `nil`.
Später lernen Sie genauer von Interfaces, aber eins ist bereits hier erwähnenswert: das Interface `error`.

Dadurch, dass `error` ein Interface ist, werden alle Werte vom Typ `error` standardmäßig mit `nil` initialisiert.

Dies erklärt zahlreiche Zeilen `if err != nil { ... }` in dieser sowie den weiteren Aufgaben.

```go
var err error                       // err == nil
err = fmt.Errorf("some error")      // err != nil
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


#### Konstanten

Konstanten werden mit dem Schlüsselwort `const` deklariert und müssen bei Deklaration definiert werden. 
Sie dürfen außerdem nur primitive Datentypen beinhalten und müssen sich im Paketkontext befinden (auf Dateiebene).
Üblicherweise werden Konstanten ganz oben in der Datei deklariert.
`SCREAMING_SNAKE_CASE` gilt in Golang als nicht idiomatisch und wird in der [offiziellen Go-Stilkonvention](https://google.github.io/styleguide/go/guide) nicht empfohlen.

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
In Go dürfen `if` und `switch` eine **Initialisierungsanweisung** besitzen. 
Alle Variablen, die in der Initialisierungsanweisung definiert wurden, sind nur in dem `if`/`switch` Block erreichbar.

**Nachteil:** Der Ausdruck scheint auf den ersten Blick etwas komplizierter.

**Vorteil:** Begrenzung des Geltungsbereichs (Scoping). 
Was in der Initialisierungsanweisung definiert wurde, darf nur in dem entsprechenden Ausdruck benutzt werden.


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


### switch

`switch` darf ebenfalls eine Initialisierungsanweisung besitzen:

```go
switch x := randomIntUnder10(); x {
case 0: fmt.Println("it's 0!")
case 4: fmt.Println("it's 4!")
case 8: fmt.Println("it's 8!")
default: fmt.Println("it's something different...")
}
```

`if-elif-else`-Blöcke sind in der Regel flexibler; bei `switch` ist jedoch schneller zu erfassen, was da passiert.


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

```python
# Python
i = 0
while i < 10:
    ...
    i += 1
```


#### Das Schlüsselwort `range`

Für Iterationen über Listen und Maps wird das Schlüsselwort `range` benutzt:

```go
for ... := range list/dict { ... }
```

Dieser Ausdruck erkennt automatisch, wie viele Rückgabewerte erwartet werden, und verhält sich unterschiedlich:

- ein Rückgabewert: `range` gibt Index (bei Listen) oder Schlüssel (bei Maps) zurück;
- zwei Rückgabewerte: `range` gibt Index und Wert (bei Listen) oder Schlüssel und Wert (bei Maps) zurück.


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


### Typumwandlung

Generell lässt sich diese Prozedur in Go sowie in Python folgendermaßen beschreiben: 
_T(v)_ konvertiert den Wert _v_ zum Typen _T_. Das gilt vor allem für Zahlen:

```go
var x int8 = 42
y := int64(x)               // kein Problem

var x int64 = 42
y := int8(x)                // kann ein Problem werden
```

[WARNING]

Das Problem: 8 Bits können viel weniger Zahlen darstellen als 64 Bits.

Wenn ein `int64`-Wert zu einem `int8`-Wert umgewandelt wird, werden Zahlen aus dem Wertebereich von `int64` auf diese von `int8` abgebildet.
Dabei ist nicht garantiert, dass es am Ende dieselbe Zahl ist, und Go schmeißt keinen Fehler.
Das führt dazu, dass solche subtilen Über- oder Unterlauf-bezogenen Defekte doch in Ihrem Programm auftauchen können.  

Die Lösung:

1. Warum wird überhaupt ein Zahlentyp zu einem kleineren Zahlentyp umgewandelt? Ist das nötig?
2. Falls ja — denken Sie daran, den Erfolg Ihrer Typumwandlung zu überprüfen.

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
   Legen Sie außerdem eine Datei `main.go` an, die mit `package main` anfängt und die Funktion `main()` beinhaltet.
2. [ER] In `grade_converter`, erstellen Sie zwei weitere Verzeichnisse: `validator` und `converter`. 
   Kreieren Sie in den Verzeichnissen entsprechend zwei Dateien — `validator.go` und `converter.go`.
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
Der Punkt ist, dass Studierende die oben vorgestellten Konzepte im Zusammenhang miteinander benutzen.

[PROT::ALT:go-basics-i.prot]
[ENDINSTRUCTOR]
