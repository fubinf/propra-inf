title: Module und Pakete in Go
stage: draft
timevalue: 2
difficulty: 2
---

https://go.dev/blog/using-go-modules
https://go.dev/blog/publishing-go-modules
https://go.dev/blog/v2-go-modules

[SECTION::goal::idea,experience]
Ich weiß, wie Go-Module verwaltet und veröffentlicht werden.

[ENDSECTION]

[SECTION::background::default]
Manchmal reicht die Standardbibliothek nicht aus — dann greifen Programmierer auf externe Bibliotheken.

Oder Sie möchten selber ein gewisses Stück der Funktionalität in anderen Projekten wiederverwenden. 
Dann bietet es sich an, ein Modul anzulegen, das in zukünftigen Projekten importiert wird.

Doch wie werden Bibliotheken (beziehungsweise _Module_) öffentlich gemacht? Darum geht es in dieser Aufgabe.


[ENDSECTION]

[SECTION::instructions::detailed]

### Package/import

Dokumentation zur Programmiersprache finden Sie in der
[Go Spec](https://go.dev/ref/spec)
für definitive (Referenz-)Information und im
[Go User Manual](https://go.dev/doc/),
wenn Sie eher Anleitungscharakter suchen.

Alle Quellcodedateien müssen einem **Paket** zugeordnet sein.
Dieses wird am Anfang der Datei in der Zeile `package {xyz}` angegeben, wobei `{xyz}` der Name Ihres Pakets ist.

#### Paket

- ein Verzeichnis namens z.B. `xyz`, in dem alle Quellcodedateien mit der Zeile `package xyz` anfangen müssen.
- auf dieser Ebene wird Sichtbarkeit geregelt: Alle `lowercase` Deklarationen sind privat, alle `Capitalized`
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
und `test`, so beginnen die Quellcodedateien in den Verzeichnissen entsprechend mit den Zeilen `package src`, `package utils` oder
`package test`.

#### Modul

Eine übergeordnete Struktur, die mehrere Pakete beinhalten kann.
Ein Modul darf Abhängigkeiten von anderen Modulen haben und selber als Abhängigkeit importiert werden.

- ein Verzeichnis mit der Datei `go.mod`, wo Modulname, Abhängigkeiten und Go-Version (beispielsweise `go 1.23`) deklariert sind.
- in der Regel werden Sie ein Verzeichnis namens `your_module_name` anlegen und dort `go mod init your_module_name` ausführen — dies initialisiert ein Modul.
- die Datei `go.mod` kann auch manuell angelegt werden — unter [Anatomy of go.mod](https://encore.cloud/guide/go.mod) können Sie sich ein Beispiel anschauen.
- ein Modul ist nicht nötig, solange Ihr Programm keine externen Abhängigkeiten benutzt.
  Wenn Sie etwas schnell ausprobieren möchten, dürfen Sie alles unter `package main` schreiben und mit `go run` ausführen.

[NOTICE]

Falls Sie Ihr Modul veröffentlichen möchten, **muss** der Modulname mit der URL übereinstimmen, wo sich das Modul befindet.

**Beispiel:**

- Sie legen ein Repo namens `my_awesome_golang_module` auf [Github](https://github.com) an,
  welches dann über `https://github.com/username/my_awesome_golang_module` erreichbar ist.
- Sollte das Repo ein Modul sein, so muss die `my_awesome_golang_module/go.mod`-Datei mit der folgenden Zeile anfangen:
  `module github.com/username/my_awesome_golang_module`

[ENDNOTICE]


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
Am Anfang beinhaltet `go.mod` nur den Modulnamen und die Go-Version (beispielsweise `go 1.23`).
Die Datei `go.mod` kann auf zwei verschiedene Arten angelegt werden:

- entweder mittels des Kommandos `go mod init your_module_name`;
- oder manuell im Root-Verzeichnis (siehe Beispiel [Anatomy of go.mod](https://encore.cloud/guide/go.mod)).

Die Datei `main.go` soll folgendermaßen aussehen:

```go
package your_module_name

import "fmt"

func HiFromRemote() {
    fmt.Println("Hi from remote module!")
}
```

[ER] Kreieren Sie nun ein lokales Projekt/Modul. Dieses darf beliebig heißen.

[ER] Legen Sie eine Datei `go.mod` an (entweder per `go mod init` oder manuell).

[ER] Legen Sie eine weitere Datei `go-basics-i.go` an und kopieren Sie den folgenden Quellcodeabschnitt in diese Datei:

```go
package main

import m %"replace_with github.com/your_username/your_module_name"%

func main() {
    m.HiFromRemote()
}
```

Und jetzt im Root-Verzeichnis des lokalen Moduls folgende Befehle ausführen:

[EC] `go get`

[EC] `go run go-basics-i.go`

Die Ausgabe müsste "Hi from remote module!" sein.

### Versionierung

TODO_Brandes


[ENDSECTION]

[SECTION::submission::trace,program]

[INCLUDE::/_include/Submission-Quellcode.md]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]

Folgende Aspekte sind bei der Korrektur wichtig:

1. Funktionalität — das Programm tut, was es soll (siehe Kommandoprotokoll unten);
2. Fehlerbehandlung muss nicht alles abdecken, aber sie muss da sein.
   `Validate`-Funktionen sollten eine informative Nachricht in dem Fehler zurückgeben.
   Deren genaues Format ist in den Kommentaren zu den entsprechenden Funktionen vorgeschrieben.

Ansonsten ist dies eine Lernaufgabe.
Der Punkt ist, dass Studierende die oben vorgestellten Konzepte im Zusammenhang miteinander benutzen.

[PROT::ALT:go-basics-i.prot]
[ENDINSTRUCTOR]
