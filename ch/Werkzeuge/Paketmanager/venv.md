title: "venv: Separate Paketumgebungen für Python"
stage: beta
timevalue: 1.0
difficulty: 2
explains: venv
---
[SECTION::goal::product]

Ich verstehe, was ein Python `venv` ist und habe mir eines für meine Arbeit am ProPra angelegt.

[ENDSECTION]
[SECTION::background::default]

Ein `venv` (virtual environment) ist ein "Sandkasten", 
in dem man nach Herzenslust Python-Pakete installieren kann,
ohne die restliche Systemumgebung damit zu verändern.

Auf Debian-Systemen ist ein `venv` die einzige Möglichkeit, 
_überhaupt_ mit [TERMREF::pip] Pakete installieren zu können,
weil die restliche Systemumgebung vor Veränderungen geschützt sein soll, die der 
[TERMREF::Debian-Paketmanager] nicht kennt. 
Aber auch auf anderen Systemen wird jede ernsthafte Python-Entwickler_in
für so ziemlich jeden (selbst kleinen) Entwicklungszweck ein eigenes `venv` anlegen.

[ENDSECTION]
[SECTION::instructions::detailed]

0. Lesen Sie [TERMREF::venv] nach.


### `venv`-Dateibaum und neues `venv` anlegen

1. Wenn man mehrere `venv` hat, sollten diese in einem eigenen Unterdateibaum wohnen,
   damit nicht so viel Unordnung entsteht.
   Legen Sie einen solchen in Ihrem Home-Verzeichnis an: `mkdir ~/venv`.
2. Legen Sie nun darin ein neues `venv` für ihre Arbeit am Programmierpraktikum an:
   `python -m venv ~/venv/propra`


### `venv propra` aktivieren

3. [EC] Mit `which` kann man herausfinden, wo ein bestimmtes Kommando gefunden wird.
   Rufen Sie das für Python auf: `which python`.
4. [EC] Aktivieren Sie nun Ihr neues `venv`:
   `source ~/venv/propra/bin/activate`.
   Ihr Shell-Prompt müsste nun mit `(propra)` beginnen.
5. [EC] Überzeugen Sie sich, dass nun ein anderes Python-Executable aktiv ist:
   `which python`


### Abkürzung in `.bashrc` einfügen und ausprobieren

6. Den obigen `source`-Aufruf müssen Sie in jeder frischen Shell wiederholen.
   Das ist umständlich. Deshalb legen wir uns dafür jetzt ein bequemeres Shell-Kommando an:
   Öffnen Sie ihre [TERMREF::.bashrc] in ihrem Home-Verzeichnis und fügen Sie unten oder an
   geeigneter Stelle ungefähr folgende Shell-Funktion zu (mit angepassten Pfaden):

```bash
init_propra() {
    propra_dir=~/ws/propra
    cd $propra_dir
    source ~/venv/propra/bin/activate
}
```

7. Deaktivieren Sie das `venv` (mit `deactivate`)
   und überzeugen Sie sich von der Wirkung (mit `which python`).
8. Starten Sie eine neue Shell, damit das geänderte `.bashrc` eingelesen wird: `bash`
9. [EC] Aktivieren Sie das `venv` mit dem neuen Kommando: `init_propra`.
10. [EC] Überzeugen Sie sich von der Wirkung (mit `which python`).
11. Rufen Sie ab jetzt, wann immer Sie mit einer neuen Shell am ProPra arbeiten wollen,
    `init_propra` auf.

Das gleiche Spiel kann man nun mit beliebig vielen anderen Python-Projekten wiederholen
und hält deren Mengen installierter Pakete immer säuberlich getrennt voneinander
und vom Basissystem.

### `venv` in IDE verwenden

Mit den bisherigen Schritten können Sie ihr `venv` im Terminal verwenden. Ihre IDE verwendet aber aktuell noch ihr
System-Environment und hat somit noch keinen Zugriff auf die im virtuellen Environment installierte Pakete.

Die Einrichtung ihres `venv` als Interpreter hängt von ihrer verwendeten Plattform und der installierten IDE ab.
Daher verweisen wir hier auf die allgemeinen Anleitungen, die Sie ggf. für ihre Bedürfnisse anpassen müssen.

#### PyCharm

Richten Sie ihr `venv` in ihrer IDE mithilfe folgender Anleitung ein. Wählen Sie dabei ihr bereits angelegtes `venv`
aus.  
[HREF::https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html].

[WARNING]
Falls Sie PyCharm ohne Lizenz unter Windows benutzen, müssen Sie noch ein zweites `venv` 
einrichten, damit Sie ihren Code auch über die IDE in Windows ausführen können.
Dieses zweite `venv` sollte in einem geeigneten Ordner außerhalb des WSL liegen (z.B. 
`C:\User\<Benutzername>\venv`), um die beiden Environments besser auseinanderhalten zu
können.

Damit sich beide Interpreter gleich verhalten, müssen neue Pakete **immer in beiden `venv` installiert werden**.
Achten Sie darauf in Aufgabe [PARTREF::pip] und bei allen Aufgaben, die die Installation weiterer Pakete voraussetzen.
Die Verwendung einer Datei `requirements.txt` kann dabei helfen, ihre benötigten Abhängigkeiten
konsistent zu halten.
[ENDWARNING]

#### Visual Studio Code

Richten Sie ihr `venv` in ihrer IDE mithilfe folgender Anleitung ein. Wählen Sie dabei ihr bereits angelegtes `venv`
aus.  
[HREF::https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters].

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]

Zeigen Sie zusätzlich ihrem Tutor, dass Sie das `venv` in ihrer IDE eingerichtet haben.  
Wenn Sie keinen Laptop benutzen, machen Sie einen Screenshot von der Einstellung in ihrer IDE, in dem klar erkennbar
ist, dass ihr `venv` eingerichtet ist.

[ENDSECTION]

[INSTRUCTOR::Funktioniert es wirklich?]
Protokoll auf Schlüssigkeit kontrollieren.
Wenn eine Ausgabe nicht zu den vorangegangenen Kommandos passt, Abgabe zurückweisen,
denn wer schon diese grundlegende und genau vorgegebene Sache falsch macht, 
rennt sonst später wahrscheinlich in riesige Schwierigkeiten.
Tückisch ist an obigen Anweisungen, dass zwischen den zu protokollierenden Kommandos
andere kommen, die nicht ins Protokoll gehören.

Grob überprüfen, ob das venv auch korrekt in der IDE eingerichtet wurde, um Folgefehler bei darauf aufbauenden
Aufgaben zu vermeiden.
[ENDINSTRUCTOR]
