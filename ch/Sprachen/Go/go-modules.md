title: Module und Pakete in Go
stage: draft
timevalue: 3
difficulty: 2
---

[SECTION::goal::idea,experience]
Ich weiß, wie Module in Go verwaltet, veröffentlicht und versioniert werden.
[ENDSECTION]

[SECTION::background::default]
Manchmal reicht die Standardbibliothek nicht aus — dann greifen Programmierer
auf externe Bibliotheken.
Manchmal wollen die Programmierer selbst ein gewisses Stück der Funktionalität
in anderen Projekten wiederverwenden.
Dann bietet es sich an, ein Modul anzulegen, das in zukünftigen Projekten
importiert wird.

Doch wie werden Bibliotheken (beziehungsweise _Module_) öffentlich gemacht?
Darum geht es in dieser Aufgabe.
[ENDSECTION]

[TOC]

[SECTION::instructions::detailed]
Diese Aufgabe orientiert sich im Wesentlichen an diesen Einträgen auf
[go.dev/blog](https://go.dev/blog/)
:

- [Using Go Modules](https://go.dev/blog/using-go-modules)
- [Publishing Go Modules](https://go.dev/blog/publishing-go-modules)
- [Go Modules: v2 and Beyond](https://go.dev/blog/v2-go-modules)

Dokumentation zu den in der Aufgabe relevanten Kommandos bekommen Sie mit:

- `go help mod`
- `go help get`
- und generell `go help _command_`.


### Paket

Alle Quellcodedateien müssen einem **Paket** zugeordnet sein.
Dieses wird am Anfang der Datei in der Zeile `package {xyz}` angegeben, wobei
`{xyz}` der Name Ihres Pakets ist.

Stichpunktartig:

- ein Paket ist ein Verzeichnis namens z.B. `xyz`, in dem alle Quellcodedateien
  mit der Zeile `package xyz` anfangen müssen.
- auf dieser Ebene wird Sichtbarkeit geregelt: Alle `lowercase` Deklarationen
  sind privat, alle `Capitalized` Deklarationen sind öffentlich (public/exported)
  und aus anderen Paketen sichtbar.
  Merkhilfe: Große Buchstaben geben große Sichtbarkeit.

Ein Paketname unterliegt Sonderregeln: `main`.
Dieses Paket ist das Hauptpaket; darin liegt das ausführbare Programm.
Einstiegspunkt ist immer die Funktion `main()`.
Dies entspricht `public static void main(String[] args)` in Java oder
`int main()` in C.

Alle anderen Paketnamen interpretiert der Compiler als Bibliotheken — diese
können nicht mittels `go run` ausgeführt werden.
Pakete entsprechen der Verzeichnisstruktur eines Moduls: Gibt es in einem Modul
`my_module` Verzeichnisse `src`, `utils` und `test`, so beginnen die Quellcodedateien
in den Verzeichnissen entsprechend mit den Zeilen `package src`, `package utils`
oder `package test`.


### Modul

Eine übergeordnete Struktur, die mehrere Pakete beinhalten kann.
Ein Modul darf Abhängigkeiten von anderen Modulen haben und selber als Abhängigkeit
importiert werden.

- ein Verzeichnis mit der Datei `go.mod`, wo Modulname, Abhängigkeiten und Go-Version
  (beispielsweise `go 1.23`) deklariert sind.
- in der Regel werden Sie ein Verzeichnis namens `your_module_name` anlegen und
  dort `go mod init your_module_name` ausführen — dies initialisiert ein Modul.
- die Datei `go.mod` kann auch manuell angelegt werden — unter
  [Anatomy of go.mod](https://encore.cloud/guide/go.mod)
  können Sie sich ein Beispiel anschauen.
- ein Modul ist nicht nötig, solange Ihr Programm keine externen Abhängigkeiten benutzt.
  Wenn Sie etwas schnell ausprobieren möchten, dürfen Sie alles unter `package main`
  schreiben und mit `go run` ausführen.

[NOTICE]
Falls Sie Ihr Modul veröffentlichen möchten, **muss** der Modulname mit der URL
übereinstimmen, wo sich das Modul befindet.

**Beispiel:**

- Sie legen ein Repo namens `my_awesome_golang_module` auf [Github](https://github.com) an,
  welches dann über `https://github.com/username/my_awesome_golang_module`
  erreichbar ist.
- Sollte das Repo ein Modul sein, so muss die `my_awesome_golang_module/go.mod`-Datei
  mit der folgenden Zeile anfangen: `module github.com/username/my_awesome_golang_module`
[ENDNOTICE]


### Was ist der Zweck?

**Module** dienen Versionierung und Nachverfolgung externer Abhängigkeiten eines Projekts.
Explizite Versionierung stellt sicher, dass Builds reproduzierbar sind.

**Pakete** dienen dazu, Quellcode zu organisieren. Darunter:

- Zusammengehörige Funktionen/Typen gruppieren
- Sichtbarkeit kontrollieren
- Wiederverwendbarkeit erleichtern

Meistens wird Ihr Projekt ein einziges Modul sein, welches mehrere Pakete enthält.


### Wie werden Module/Pakete importiert?

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
2. Externe Module/Bibliotheken — beispielsweise ein Modul importieren, welches
   sich unter `github.com/username/module_name` befindet.
    - in dem Root-Verzeichnis des Moduls `go get github.com/username/module_name`
      ausführen und dann im Quellcode importieren;
    - **oder** zuerst im Quellcode importieren (`import "github.com/username/module_name"`)
      und danach aus dem Root-Verzeichnis des Moduls `go get` ausführen.
      So werden alle nötigen Bibliotheken automatisch heruntergeladen.

[NOTICE]
Ein weiterer nützlicher Befehl ist `go mod tidy`.
Er schaut sich Ihr Projekt und die Datei `go.mod` an und entfernt die
unbenutzten Module.
[ENDNOTICE]

[ER] Legen Sie ein öffentliches Github-Repo an.
Den Modulnamen dürfen Sie beliebig wählen (um unerwartete Fehler zu vermeiden,
benutzen Sie im Modulnamen keine Sonderzeichen).

[ER] Das Repo muss zwei Dateien beinhalten: `go.mod` und `main.go`.
Am Anfang beinhaltet `go.mod` nur den Modulnamen und die Go-Version
(beispielsweise `go 1.23`).
Die Datei `go.mod` kann auf zwei verschiedene Arten angelegt werden:

- entweder mittels des Kommandos `go mod init your_module_name`;
- oder manuell im Root-Verzeichnis (siehe Beispiel
  [Anatomy of go.mod](https://encore.cloud/guide/go.mod)
  ).

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

[ER] Legen Sie eine weitere Datei `go-modules.go` an und kopieren Sie den folgenden
Quellcodeabschnitt in diese Datei:

```go
package main

import m "github.com/your_username/your_module_name"

func main() {
    m.HiFromRemote()
}
```

Und jetzt im Root-Verzeichnis des lokalen Moduls folgende Befehle ausführen:

[EC] `go get`

[EC] `go run go-modules.go`

Die Ausgabe müsste "Hi from remote module!" sein.


#### Nützliche Kommandos

Erklären Sie jeweils, was die folgenden Befehle tun.

Fangen Sie Ihre Suche mit der Dokumentation an: `go help <command>`.
Falls das nicht ausreicht, dürfen Sie alle verfügbaren Quellen benutzen.

[EQ] `go mod tidy`

[EQ] `go mod download`

[EQ] `go mod vendor`

[EQ] `go mod edit -replace`


### Versionierung

Bibliotheken in Go unterliegen den Regeln
[semantischer Versionierung](https://semver.org/)
— Versionsnummer entsprechen dem Schema `vMAJOR.MINOR.PATCH`.

[EQ] Wodurch unterscheiden sich Major-, Minor- und Patch-Versionen?

Während der Entwicklung (v0) und beim ersten stabilen Release (v1) befindet sich
der Quellcode im Root-Verzeichnis des Moduls.

Soll es v2, v3 oder höhere Versionen geben, so muss der Quellcode in Verzeichnissen
`your_module_name/v2` und `your_module_name/v3` liegen — so lassen sich
Namenskonflikte vermeiden.
Die Unterverzeichnisse sind selbst vollständige Module und besitzen jeweils
eine Datei `go.mod`, wo der Modulname als `github.com/your_username/your_module_name/v2`
beziehungsweise `.../v3` angegeben wird.

Folgende Schritte finden statt, wenn ein Modul importiert wird (Version `v2` als Beispiel):

1. Das git-Repo unter der Import-URL finden;
2. Major-Version aus der URL auslesen:
    - falls diese mit beispielsweise `v2` endet, so ist die Major-Version `2`;
    - wird keine `v2`-Endung gefunden, so ist die Major-Version `1`;
3. Das Repo nach einem git-Tag (Versionstag) mit der größten stabilen Version durchsuchen,
   die immer noch der Major-Version entspricht (`v2.x.x`):
    - der Versionstag wurde gefunden — die spezifizierte Version herunterladen;
    - kein passender Versionstag wurde gefunden — agiere nach der Verzeichnisstruktur
      — die Version unter `/v2` wird heruntergeladen und mit einer
      [Pseudoversionsnummer](https://go.dev/doc/modules/version-numbers#pseudo-version-number)
      bezeichnet.
      Diese Pseudoversionsnummer wird in `go.mod` des importierenden Moduls gespeichert.

Lesen Sie nun diesen Eintrag über
[git-Tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
. Was Sie davon lernen sollen:

- wie ein git-Tag kreiert wird;
- wie ein git-Tag gelöscht wird;
- wie ein git-Tag auf Remote gepusht wird.

[WARNING]
Falls Sie merken, dass `go get` nicht die richtige Version Ihres Moduls
herunterlädt, kann das am Proxyserver liegen.

Um das auszuschließen, setzen Sie die `GOPROXY` Umgebungsvariable auf `direct`.
Führen Sie den Befehl im Terminal aus:

    export GOPROXY=direct
[ENDWARNING]

[ER] Taggen Sie den letzten Commit in Ihrem `your_module_name` mit `v1.0.0`
und pushen Sie den git-Tag auf Remote.
Dadurch wird der Stand des Repos als v1.0.0 Version "versiegelt".
Alle Nutzer des Moduls, die das Modul mittels
`import "github.com/your_username/your_module_name"` importieren, erhalten
genau den Repo-Stand, der mit `v1.0.0` getaggt wurde.
Diese Version können Sie mit dem Kommando
`go get github.com/your_username/your_module_name@v1.0.0`
oder `go get github.com/your_username/your_module_name@latest`
herunterladen.

[ER] Kreieren Sie die nächste Major-Version: `v2`.
Legen Sie ein Verzeichnis `your_module_name/v2` an und kopieren Sie die
Inhalte des Moduls (`go.mod` und `main.go`) in dieses Verzeichnis um.

[ER] Ändern Sie die Ausgabe der Funktion `PrintFromRemote`:
Nun soll es `Hi from remote module v2!` sein.

[ER] Committen Sie die Änderungen und taggen Sie den Commit mit `v2.0.0`
(nicht zu vergessen das auf Remote zu pushen!).

[ER] Passen Sie Ihr lokales Projekt so an, dass beide Versionen nebeneinander
benutzt werden und die Ausgabe folgendermaßen aussieht:

    Hi from remote module!
    Hi from remote module v2!    

[EC] `go run go-modules.go`
[ENDSECTION]

[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Hinweise]
[ENDINSTRUCTOR]
