title: Module und Pakete in Go
stage: beta
timevalue: 2
difficulty: 3
assumes: go-basics
---

[SECTION::goal::idea,experience]
Ich weiß, wie Module in Go verwaltet, veröffentlicht und versioniert werden.
[ENDSECTION]

[SECTION::background::default]
Manchmal reicht die Standardbibliothek nicht aus — dann greifen Programmierer auf externe Bibliotheken zurück.
Manchmal wollen sie bestimmte Funktionalität in anderen Projekten wiederverwenden.
In solchen Fällen bietet es sich an, ein eigenes __Modul__ zu erstellen, das in zukünftigen Projekten importiert werden
kann.

Doch wie werden Bibliotheken — beziehungsweise __Module__ — öffentlich zugänglich gemacht?
Darum geht es in dieser Aufgabe.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]
Diese Aufgabe orientiert sich im Wesentlichen an diesen Beiträgen auf
[go.dev/blog](https://go.dev/blog/):

- [Using Go Modules](https://go.dev/blog/using-go-modules)
- [Publishing Go Modules](https://go.dev/blog/publishing-go-modules)
- [Go Modules: v2 and Beyond](https://go.dev/blog/v2-go-modules)

### Paket

Alle Quellcodedateien müssen einem **Paket** zugeordnet sein.
Dieses wird am Anfang der Datei in der Zeile `package xyz` angegeben, wobei `xyz` der Name Ihres Pakets ist.

Stichpunktartig:

- ein Paket ist ein Verzeichnis, in dem alle Quellcodedateien mit der Zeile `package xyz` anfangen.
  Konventionsmäßig heißt dann das Verzeichnis ebenfalls `xyz`, aber das ist nicht unbedingt notwendig.
- auf dieser Ebene wird Sichtbarkeit geregelt: Alle `lowercase` Deklarationen sind privat, alle `Capitalized`
  Deklarationen sind öffentlich (public/exported) und aus anderen Paketen sichtbar.
  **Merkhilfe:** Große Buchstaben geben große Sichtbarkeit.

Ein einziger Paketname unterliegt Sonderregeln: `main`.
Dieses Paket ist das Hauptpaket; darin liegt das ausführbare Programm.
Einstiegspunkt ist immer die Funktion `main()`.
Dies entspricht `public static void main(String[] args)` in Java oder `int main()` in C.

Alle anderen Paketnamen interpretiert die Go-Toolchain als Bibliotheken — diese können nicht mittels `go run` ausgeführt
werden.
Pakete entsprechen der Verzeichnisstruktur eines Moduls:
Gibt es in einem Modul `my_module` Verzeichnisse `src`, `utils` und `test`, so beginnen die Quellcodedateien in den
Verzeichnissen entsprechend mit den Zeilen `package src`, `package utils` oder `package test`.
Dies ist lediglich eine extrem starke Konvention — die Namen von Verzeichnissen und Paketen müssen nicht übereinstimmen.
Der Verzeichnisname bestimmt nur den Importpfad, wobei der Paketname beim Benutzen im Code verwendet wird.
Ein typisches Beispiel ist ein Verzeichnis namens `v2` (für eine neue Hauptversion), dessen Quellcodedateien dennoch mit
`package mylib` beginnen, um den Paketnamen stabil zu halten.

[EQ] Überlegen Sie: Welche Vor- und Nachteile hat es, dass Sichtbarkeit über Groß-/Kleinschreibung geregelt wird?

<!-- time estimate: 15 min -->


### Modul

Ein Modul ist eine übergeordnete Struktur, die mehrere Pakete beinhalten kann.
Ein Modul darf Abhängigkeiten von anderen Modulen haben und selber als Abhängigkeit importiert werden.

- ein Verzeichnis mit der Datei `go.mod`, wo Modulname, Abhängigkeiten und Go-Version (beispielsweise `go 1.23`)
  deklariert sind.
- in der Regel werden Sie ein Verzeichnis namens `your_module_name` anlegen und dort `go mod init your_module_name`
  ausführen — dies initialisiert ein Modul.
- die Datei `go.mod` kann auch manuell angelegt werden — unter
  [Anatomy of go.mod](https://encore.cloud/guide/go.mod)
  können Sie sich ein Beispiel anschauen.
- für einzelne `.go`-Dateien, die Sie schnell ausprobieren möchten, können Sie `go run file.go` ohne Modul ausführen.
- Sobald Ihr Projekt aus mehreren Dateien oder Paketen besteht, ist eine `go.mod` nötig.

[FOLDOUT::Wozu das Ganze?]
**Module** dienen Versionierung und Nachverfolgung externer Abhängigkeiten eines Projekts.
Explizite Versionierung stellt sicher, dass Builds reproduzierbar sind.

**Pakete** dienen dazu, Quellcode zu organisieren.
Darunter:

- Zusammengehörige Funktionen/Typen gruppieren
- Sichtbarkeit kontrollieren
- Wiederverwendbarkeit erleichtern

Häufig wird Ihr Projekt ein einziges Modul sein, welches mehrere Pakete enthält.
[ENDFOLDOUT]

[EQ] Überlegen Sie: Ab wann lohnt es sich, ein Modul anzulegen?

[EQ] Was passiert, wenn es in einem Verzeichnis sowohl Dateien mit `package abc` als auch mit `package xyz` gibt?
Probieren Sie aus.

<!-- time estimate: 15 min -->


### Wie werden Module/Pakete importiert?

Die Syntax einer Import-Anweisung:

```go
import (optionales Alias) "Paketpfad"
```

Beispiel:

```go
import "github.com/gen2brain/raylib-go/raylib"
```

Weitere Fälle betrachten wir anhand des folgenden Beispiel-Projekts:

    my_module/
    ├── go.mod
    ├── main.go
    ├── package_1/
    │   └── a.go
    └── package_2/
        └── b.go

`go.mod` deklariert ein Modul, `main.go` ist der Einstiegspunkt, und die Verzeichnisse
`package_1` und `package_2` sind Pakete.

`a.go` beginnt mit der Zeile `package package_1`,
`b.go` beginnt mit der Zeile `package package_2` (nach Konvention).


#### Importieren von Paketen innerhalb des eigenen Moduls

Stellen Sie sich vor, dass in `b.go` eine Funktion `Foo` definiert ist, die Sie in `a.go` verwenden wollen.
Dann sieht der Anfang von `a.go` folgendermaßen aus:

```go
package package_1

import "my_module/package_2"

func A() {
    package_2.Foo()
}
```

Dabei müssen Sie aufpassen, dass Ihr Abhängigkeitsgraph azyklisch bleibt.

[NOTICE]
Hieße die Funktion `foo`, hätte das nicht funktioniert, da kleingeschriebene Deklarationen in einem Paket privat sind.
[ENDNOTICE]

<!-- time estimate: 5 min -->


#### Importieren von externen Modulen

Dafür gibt es zwei Möglichkeiten:

- im Root-Verzeichnis des Moduls `go get Verzeichnis/wo/sich/das/Modul/befindet` ausführen und dann im Quellcode
  importieren;
- **oder** zuerst im Quellcode importieren (`import "Verzeichnis/wo/sich/das/Modul/befindet"`) und danach aus dem
  Root-Verzeichnis des Moduls `go get` ausführen.
  So werden alle nötigen Bibliotheken automatisch heruntergeladen.

Falls beim Importieren ein Alias verwendet wurde, so greift man auf das Paket über dieses Alias zu.
Schauen Sie sich folgende Beispiele an, wo Raylib einmal mit Alias und einmal ohne importiert wurde.

[FOLDOUT::Import mit Alias]
```go
import foo "github.com/gen2brain/raylib-go/raylib"

func main() {
    foo.InitWindow(620, 820, "Tetris")
    foo.SetTargetFPS(60)
}
```
[ENDFOLDOUT]

[FOLDOUT::Import ohne Alias]
```go
import "github.com/gen2brain/raylib-go/raylib"

func main() {
    rl.InitWindow(620, 820, "Tetris")
    rl.SetTargetFPS(60)
}
```

`rl` ist der eigentliche Paketname, da alle Dateien unter `github.com/gen2brain/raylib-go/raylib` mit `package rl`
anfangen.
[ENDFOLDOUT]

<!-- time estimate: 5 min -->


### Wie werden Module veröffentlicht?

Falls Sie Ihr Modul veröffentlichen möchten, **muss** der Modulname mit der URL übereinstimmen, wo sich das Modul
befindet.

**Beispiel:**

- Sie legen ein Repo namens `my_awesome_golang_module` auf 
  [Github](https://github.com)
  an, welches dann über 
  `https://github.com/username/my_awesome_golang_module`
  erreichbar ist.
- Sollte das Repo ein Modul sein, so muss die `my_awesome_golang_module/go.mod`-Datei mit der folgenden Zeile anfangen:
  `module github.com/username/my_awesome_golang_module`.

Das probieren Sie nun selber aus.

[ER] Legen Sie ein öffentliches Repo an (auf GitHub oder anderswo; ein privates sollte für unsere Zwecke auch gehen,
wenn Sie den Proxy abschalten, siehe unten).

[ER] Das Repo muss zwei Dateien beinhalten:
`go.mod` und eine Go-Quellcodedatei, die **nicht** `main.go` heißt — `main.go` impliziert eine ausführbare Datei, die
`func main()` enthält.
Ein passender Name wäre `remote.go` — diesen dürfen Sie übernehmen, müssen Sie aber nicht.
Am Anfang beinhaltet `go.mod` nur den Modulnamen und die Go-Version (beispielsweise `go 1.23`).
Die Datei `go.mod` kann auf zwei verschiedene Arten angelegt werden:

- entweder mittels des Kommandos `go mod init github.com/your_username/your_module_name`;
- oder manuell im Root-Verzeichnis (siehe Beispiel
  [Anatomy of go.mod](https://encore.cloud/guide/go.mod)).

Diese Quellcodedatei soll folgendermaßen aussehen:

```go
package your_packagename

import "fmt"

func PrintFromRemote() {
    fmt.Println("Hi from remote module!")
}
```
Der Paketname muss ein gültiger Bezeichner sein, kann also keine Doppelpunkte oder Schrägstriche enthalten.

[ER] Committen und pushen Sie anschließend die Änderungen auf Remote.

[ER] Legen Sie ein lokales Projekt/Modul an.
Dieses darf beliebig heißen.

[ER] Legen Sie eine Datei `go.mod` an (entweder per `go mod init` oder manuell).

[ER] Legen Sie eine weitere Datei `go-modules.go` an und kopieren Sie den folgenden Quellcodeabschnitt in diese Datei
(ersetzen Sie den Import-Pfad durch den richtigen):

```go
package main

import m "github.com/your_username/your_module_name"

func main() {
    m.PrintFromRemote()
}
```

Und führen Sie anschließend im Root-Verzeichnis des lokalen Moduls folgende Befehle aus:

[EC] `go get`

[EC] `go run go-modules.go`

Die Ausgabe müsste "Hi from remote module!" sein.

[WARNING]
Wir empfehlen, die Umgebungsvariable `GOPROXY` auf `direct` zu setzen
([Was dahintersteckt](https://proxy.golang.org/)).
Führen Sie dazu folgenden Befehl im Terminal aus:

    export GOPROXY=direct

Dadurch lassen sich Caching-Probleme vermeiden, etwa in Fällen wie:
_"Ich habe xyz gepusht, aber im lokalen Projekt ist die Änderung nicht sichtbar."_

Wenn Sie im Verlauf der Aufgabe den Eindruck haben, dass etwas nicht stimmt, sollte `export GOPROXY=direct` Ihr erster
Debugging-Schritt sein.
[ENDWARNING]

<!-- time estimate: 30 min -->


### Versionierung

Bibliotheken in Go unterliegen den Regeln semantischer Versionierung — Versionsnummern entsprechen dem Schema
`vMAJOR.MINOR.PATCH`.

[EQ] Finden Sie im [Artikel "Semantic Versioning 2.0.0"](https://semver.org/) eine Antwort auf die Frage:
Wodurch unterscheiden sich Major-, Minor- und Patch-Versionen?

<!-- time estimate: 5 min -->

Während der Entwicklung (v0) und beim ersten stabilen Release (v1) befindet sich der Quellcode im Root-Verzeichnis des
Moduls.

**Wichtig:**
Soll es v2, v3 oder höhere Versionen geben, so muss der Quellcode in Verzeichnissen `your_module_name/v2` und
`your_module_name/v3` liegen.
Die Unterverzeichnisse sind selbst vollständige Module und besitzen jeweils eine Datei `go.mod`, wo der Modulname als
`github.com/your_username/your_module_name/v2` beziehungsweise `.../v3` angegeben wird.

[NOTICE]
Major-Versionen höher als 1 müssen im Import-Pfad angegeben werden!

```go
import m3 "github.com/username/library/v3"
```
[ENDNOTICE]

Importieren eines Moduls besteht aus folgenden Schritten (Version `v2` als Beispiel):

1. Das git-Repo unter der Import-URL finden;
2. Major-Version aus der URL auslesen:
    - falls diese mit beispielsweise `v2` endet, so ist die Major-Version `2`;
    - wird keine `v2`-Endung gefunden, so ist die Major-Version `1`;
3. Das Repo nach einem Git-Tag (Versionstag) mit der Major-Version `v2` durchsuchen.
   Gibt es mehrere Minor-Versionen, so wird die größte benutzt;
4. Falls der Versionstag gefunden wurde, wird die spezifizierte Version heruntergeladen;
   ansonsten wird die Version aus dem Verzeichnis `/v2` heruntergeladen und mit einer
   [Pseudoversionsnummer](https://go.dev/doc/modules/version-numbers#pseudo-version-number)
   versehen.
   Diese Pseudoversionsnummer wird in `go.mod` des importierenden Moduls gespeichert;
5. Gibt es keinen passenden Git-Tag und kein passendes Verzeichnis,
   dann schlägt das Importieren fehl.

[ER] Finden Sie nun in diesem Eintrag über
[Git-Tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
Informationen darüber, wie:

- ein Git-Tag erstellt wird;
- ein Git-Tag gelöscht wird;
- ein Git-Tag auf ein Remote-Repo gepusht wird.

[ER] Taggen Sie den letzten Commit in `your_module_name` mit `v1.0.0` und pushen Sie den Git-Tag auf Remote.

Dadurch wird der Stand des Repos als `v1.0.0`-Version "versiegelt".
Alle Nutzer des Moduls, die das Modul mittels `import "github.com/your_username/your_module_name"` importieren,
erhalten genau den Repo-Stand, der nun mit `v1.0.0` getaggt wurde.

[ER] Laden Sie diese Version mittels `go get github.com/your_username/your_module_name@v1.0.0` herunter.

[ER] Kreieren Sie die nächste Major-Version: `v2`.
Legen Sie ein Verzeichnis `your_module_name/v2` an und kopieren Sie die Inhalte des Moduls (`go.mod` und die Quellcodedatei) in
dieses Verzeichnis.

[ER] Passen Sie den Modulnamen in der Datei `v2/go.mod` an:
Nun ist es `github.com/your_username/your_module_name/v2`.

[ER] Ändern Sie die Ausgabe der Funktion `PrintFromRemote`:
In dieser Version soll es `Hi from remote module v2!` sein.

[ER] Committen Sie die Änderungen und taggen Sie den Commit mit `v2.0.0` (vergessen Sie nicht, auf Remote zu pushen!).

[ER] Ersetzen Sie den Inhalt von `go-modules.go` durch den Quellcode unten.
Passen Sie die `import`s entsprechend an.

```go
package main

import m1 "github.com/your_username/your_module_name"
import m2 "github.com/your_username/your_module_name/v2"

func main() {
    m1.PrintFromRemote()
    m2.PrintFromRemote()
}
```

[EC] `go get`

[EC] `go run go-modules.go`

<!-- time estimate: 40 min -->
[ENDSECTION]

[SECTION::submission::information,trace,program]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
**Kommandoprotokoll**
[PROT::ALT:go-modules.prot]

**Lösungen**

[INCLUDE::ALT:]
[ENDINSTRUCTOR]
