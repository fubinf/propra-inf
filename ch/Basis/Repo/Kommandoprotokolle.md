title: Protokolle von Kommandos und Kommandoausgaben abgeben
stage: alpha
timevalue: 0.5
difficulty: 2
requires: Git101
---
[SECTION::goal::trial]

Ich kann das Unix-Kommando `script` anwenden, um Kommandoeingaben und -ausgaben 
für eine Abgabe zu protokollieren

[ENDSECTION]
[SECTION::background::default]

Viele Aufgaben verlangen, dass Sie ein Protokoll von Geschehnissen in der Shell
abgeben: Sie rufen ein paar Kommandos auf und die Abgabe enthält diese Kommandos plus
deren jeweilige Ausgabe.

Aber wie kommen diese Sachen in eine Abgabedatei?
Copy/paste ist dafür nicht gut geeignet, denn dabei geht sämtliche Farbe verloren,
so dass das Resultat für die Tutor_innen sehr unübersichtlich wird.

In dieser Aufgabe lernen wir eine bessere Lösung kennen und probieren sie aus.

[ENDSECTION]
[SECTION::instructions::detailed]

### `script` installieren

- Rufen Sie `script --help` auf.
- Wenn das Kommando nicht existiert, rufen sie `sudo apt install util-linux` auf,
  um es zu installieren.


### `script` ausprobieren

- Rufen Sie `script` auf.
  Es erscheint eine Meldung und es startet eine neue Shell.
  Jetzt werden _alle_ Eingaben und Ausgaben in der Datei `typescript` protokolliert.
- Geben Sie der Reihe nach folgende Kommandos ein:
  - `ls`
  - `uptime`
  - `whoami`
  - `whoareyou`
  - `uname -a`
  - `exit`
- `exit` hat die neue Shell beendet und damit auch die Protokollierung.
- Das Protokoll steht jetzt in der Datei `typescript`
- Sehen Sie es sich mit `less typescript` an.
  So ungefähr wird das Ergebnis auch für die Tutor_in aussehen.
  

### Protokoll korrigieren

Sie haben hoffentlich bemerkt, dass `whoareyou` nicht funktioniert hat?
Das Kommando gibt es nämlich gar nicht.
Wir tun so, als sei dies eine versehentliche Fehleingabe gewesen.

So etwas wollen wir im Protokoll nicht haben, sondern es entfernen, damit es das
Verständnis des Protokolls nicht erschwert.

- Rufen Sie `nano typescript` auf.
  Nano ist ein einfacher Texteditor, der auf allen Linux-Systemen vorhanden ist.
  Die Bedienung ist in den unteren Zeilen erklärt. 
  (`^` steht für die Umschalttaste Ctrl-/Strg-, `M-` ("meta") steht für `Alt-`.)
- Wie Sie sehen, sieht das Protokoll plötzlich viel komplizierter aus.
  Das liegt daran, dass die Steuercodes für die Farbänderungen jetzt sichtbar gemacht werden.
- Schneiden Sie das Kommando `whoareyou` aus, samt des Shell-Prompts davor
  und der Fehlermeldung dahinter.
  Speichern Sie das Ergebnis und prüfen Sie es sorgfältig.
  Nichts zu viel oder zu wenig gelöscht? Prima. Dann abgeben:
  
[ENDSECTION]
[SECTION::submission::trace]

Benennen Sie die Datei `typescript` in die Form `*.txt` um.
Dabei steht der Stern für den Aufgabennamen.
Der Zielname ist also `Kommandoprotokolle.txt`:
`rename typescript Kommandoprotokolle.txt`.
Geben Sie diese Datei ab.

Analog werden wir das künftig bei vielen Aufgaben machen.

[ENDSECTION]

[INSTRUCTOR::heading]
Wir erwarten eine Datei, in der außer dem von `script` eingefügten Kopf und Fuß
optisch gesehen nur genau das steht, was obige Kommandos erzeugen sollen.
Faktisch sind vielleicht einige Backspaces etc. dabei, wenn welche eingegeben wurden,
aber im wesentlichen ist das Ergebnis mit `less` gut lesbar.

Wenn bei der Korrektur zuviel, zuwenig oder das Falsche weggeschnitten wurde,
die Abgabe zurückweisen (und darauf hinweisen, dass es einfacher sein dürfte,
nochmal von vorn anzufangen, als die kaputte Abgabe zu reparieren).

Es muss jeweils ein Prompt dastehen, der den Anforderungen von
[PARTREF::Shellprompt] genügt.
[ENDINSTRUCTOR]
