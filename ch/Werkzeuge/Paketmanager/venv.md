title: "venv: Separate Paketumgebungen für Python"
stage: alpha
timevalue: 0.5
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

Auf Debian-Systemen ist es die einzige Möglichkeit, 
_überhaupt_ mit [TERMREF::pip] Pakete installieren zu können,
weil die restliche Systemumgebung vor Veränderungen geschützt sein soll, die der 
[TERMREF::Debian-Paketmanager] nicht kennt. 
Aber auch auf anderen Systemen wird jede ernsthafte Python-Entwickler_in
für so ziemlich jeden (selbst kleinen) Entwicklungszweck ein eigenes `venv` anlegen.

[ENDSECTION]
[SECTION::instructions::detailed]

0. Lesen Sie [TERMREF::venv] nach.


### `venv`-Dateibaum und neues `venv` anlegen

1. Wenn man mehrere venvs hat, sollten diese in einem eigenen Unterdateibaum wohnen,
   damit nicht so viel Unordnung entsteht.
   Legen Sie einen solchen in Ihrem Homeverzeichnis an: `mkdir ~/venv`.
2. Legen Sie nun darin ein neues `venv` für ihre Arbeit am Programmierpraktikum an:
   `python -m venv ~/venv/propra`


### `venv propra` aktivieren

3. Mit `which` kann man herausfinden, wo ein bestimmtes Kommando gefunden wird.
   Rufen Sie das für Python auf: `which python`.
4. Aktivieren Sie nun Ihr neues `venv`:
   `source ~/venv/propra/bin/activate`.
   Ihr Shell-Prompt müsste nun mit `(propra)` beginnen.
5. Überzeugen Sie sich, dass nun ein anderes Python-Executable aktiv ist:
   `which python`


### Abkürzung in `.bashrc` einfügen und ausprobieren

6. Den obigen `source`-Aufruf müssen Sie in jeder frischen Shell wiederholen.
   Das ist umständlich. Deshalb legen wir uns dafür jetzt ein bequemeres Shell-Kommando an:
   Öffnen Sie die Datei `~/.bashrc` und fügen Sie unten oder an geeigneter Stelle 
   folgende Shell-Funktion zu:

```bash
  init_propra() {
      propra_d=~/ws/propra
      cd $propra_d
      source ~/venv/propra/bin/activate
  }
```

7. Deaktivieren Sie das `venv` (mit `deactivate`)
   und überzeugen Sie sich von der Wirkung (mit `which python`).
8. Starten Sie eine neue Shell, damit das geänderte `.bashrc` eingelesen wird: `bash`
9. Aktivieren Sie das `venv` mit dem neuen Kommando: `init_propra`.
10. Überzeugen Sie sich von der Wirkung (mit `which python`).
11. Rufen Sie ab jetzt, wann immer Sie mit einer neuen Shell am Propra arbeiten wollen,
    `init_propra` auf.

Das gleiche Spiel kann man nun mit beliebig vielen anderen Python-Projekten wiederholen
und hält deren Mengen installierter Pakete immer säuberlich getrennt voneinander
und vom Basissystem.

[ENDSECTION]
[SECTION::submission::trace]

Geben Sie ein Protokoll Ihrer oben ausgeführten Kommandos und derer Ausgaben ab.
Wenn unterwegs etwas schiefgegangen ist, lassen Sie diese Teile weg, sodass das Protokoll
nur die gewünschten erfolgreichen Kommandos widerspiegelt.
Ändern Sie sonst nichts ab.

[ENDSECTION]

[INSTRUCTOR::Funktioniert es wirklich?]
Protokoll auf Schlüssigkeit kontrollieren.
Wenn eine Ausgabe nicht zu den vorangegangenen Kommandos passt, Abgabe zurückweisen,
denn wer schon diese grundlegende und genau vorgegebene Sache falsch macht, 
rennt sonst später wahrscheinlich in riesige Schwierigkeiten.
[ENDINSTRUCTOR]
