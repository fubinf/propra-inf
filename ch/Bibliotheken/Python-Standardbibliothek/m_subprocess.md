title: "subprocess: Unterprozesse starten und ihre Ausgaben lesen"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: encoding-and-open
---

[SECTION::goal::trial]
Ich kann programmatisch von Python aus ein Shell-Kommando starten und kann bei Bedarf
seine Ausgaben verarbeiten.
[ENDSECTION]


[SECTION::background::default]
Oft gibt es für ein Teilproblem beim Programmieren schon eine Lösung X,
die sich aber nicht leicht direkt aus Python aufrufen lässt, 
z.B. weil sie in einer anderen Sprache geschrieben ist.
Ein häufiger Fall sind leistungsfähige Unix-Kommandozeilenprogramme.

Dann kommt manchmal infrage, das externe Programm X als Unterprozess zu starten,
programmatisch mit Eingaben zu versorgen und seine Ausgaben zu lesen und 
als Text zu verarbeiten. 
Das probieren wir in dieser Aufgabe aus.

Dadurch kann man manchmal in 5 Zeilen ein Problem lösen, das sonst
hunderte oder tausende von Zeilen verlangt hätte.
Sie können im Anschluss an diese Aufgabe ein Beispiel dafür kennenlernen:
[PARTREF::m_subprocess2]
[ENDSECTION]


[SECTION::instructions::detailed]
Wir nehmen uns vor, ein Programm zu schreiben, das ausgibt, wie viele 
interaktive bash-Shells gerade laufen.

Das kann man (wenn auch nicht ganz zuverlässig) mit dem Kommando `ps aux` herausbekommen.
`ps` listet auf Unix-Systemen Prozesse auf; jede Ausgabezeile beschreibt einen Prozess.
Ausgabezeilen von `ps aux`, die auf "bash" enden, zeigen (meist) eine interaktive
bash-Shell an.

[EC] Probieren Sie `ps aux` aus.


### Modul `subprocess`

[ER] Importieren Sie `subprocess`.

Überfliegen Sie die Dokumentation:
[HREF::https://docs.python.org/3/library/subprocess.html].
Ganz schön kompliziertes Modul!
Wir benutzen davon aber nur einen relativ einfachen Anwendungsfall.

[ER] Lesen Sie die Dokumentation von `Popen.communicate()`.
Schreiben Sie das Idiom in Ihr Programm, das dort angegeben ist, und verstehen Sie es.
Verstehen Sie insbesondere die Rolle des (unvollständigen) `Popen()`-Aufrufs darin.
Dafür müssen Sie ein wenig über den `Popen`-Konstruktor nachlesen.

[ER] Ergänzen Sie die nötigen Argumente des `Popen`-Aufrufs.
Wir brauchen `args`, `stdout` und `shell`.

[HINT::Welches Argument brauche ich für `args`?]
`"ps aux"` genügt.

Für ein ernsthaftes Programm wäre es besser, den ganzen _Pfadnamen_ des `ps`-Kommandos anzugeben,
damit man nicht versehentlich eine andere ausführbare Datei mit demselben Namen erwischt, die 
zufällig bei diesem Benutzer im [TERMREF::PATH] hängt.
Das Weglassen des Pfades kann den Vorteil haben, dass die [TERMREF::Executable] auf einem anderen 
Unix-System eventuell unter einem anderen Pfad sein kann und unser Programm ohne den Pfad somit 
plattformunabhängiger wäre.

Den Pfad zu `ps` bekommt man mit `which -a ps` oder mit `command -v ps` (was auf mehr 
Unix-Varianten funktioniert) heraus.  
Eine andere Möglichkeit: mit `shutil.which()` lässt sich der Programmpfad dynamisch auflösen, 
solang sich dieser in der PATH-Variable befindet.
So lässt sich auch der Fall abfangen, dass der Befehl auf dem ausführenden System nicht 
verfügbar ist.
[ENDHINT]

[HINT::Welches Argument brauche ich für `stdout`?]
`subprocess.PIPE`, damit `communicate()` die Ausgabe auffangen kann und sie nicht
auf der normalen Standardausgabe erscheinen.
[ENDHINT]

[HINT::Welches Argument brauche ich für `shell`?]
Bitte schlagen Sie nicht sämtliche Hinweise auf.
Selber nachdenken ist Trumpf!
[ENDHINT]

Nun haben wir in `out` die Ausgabe des Kommandos.

[ER] Die lesen wir nun zeilenweise durch,
suchen darin alle Zeilen, für die gilt `endswith(b"bash")`, und zählen sie.

[HINT::Wie geht die zeilenweise Schleife?]
Iterieren Sie über `out.split(b"\n")`
[ENDHINT]

[ER] Das Ergebnis geben wir mit `print()` aus. 

Das war's schon!

[EC] `python m_subprocess.py`


### Manchmal die kleine Lösung: `os.system()`

Gelegentlich reicht es einem, ein Kommando nur aufzurufen, ohne dabei Ein- und Ausgaben 
selber zu verarbeiten.
Warum? Entweder, weil die _Wirkung_ des Kommandos von Interesse ist oder weil seine Ausgaben
einfach auf der Standardausgabe erscheinen sollen.

Das geht mit der Funktion `system(cmd_string)` aus dem Modul `os`.
das kann man z.B. für die Aufgabe [PARTREF::mlh-gitac] gebrauchen.

[HREF::https://docs.python.org/3/library/os.html#os.system]
[ENDSECTION]


[SECTION::submission::trace,program]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Kommandoprotokoll prüfen]
Kommandoprotokoll prüfen.
Bei Abweichungen oder Auffälligkeiten zusätzlich den Code prüfen.

Beispiellösung siehe [TREEREF::/Bibliotheken/Python-Standardbibliothek/m_subprocess.py]

[INCLUDE::ALT:]

[PROT::ALT:m_subprocess.prot]
[ENDINSTRUCTOR]
