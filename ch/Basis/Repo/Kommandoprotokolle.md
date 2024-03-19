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
  
[NOTICE]
Es ist auch möglich, einzelne Befehle direkt zu protokollieren und sich das `exit` zu sparen. Schauen Sie sich hierzu wie erwähnt die Hilfe an.
[ENDNOTICE]

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
  
[NOTICE]
Es ist auch möglich, einen anderen Texteditor als `nano` zu verwenden. Seien Sie sich aber
bewusst, dass die Dateien möglicherweise Symbole beinhalten werden, die Ihnen nicht vertraut
sind. Diese dienen der Formatierung (also beispielsweise Farbe) und sind der Grund, aus dem
wir diesen Weg gegangen sind. Entfernen Sie diese daher nicht pauschal alle diese Symbole!
[ENDNOTICE]
[ENDSECTION]
[SECTION::submission::trace]

Benennen Sie die Datei `typescript` in die Form `*.txt` um.
Dabei steht der Stern für den Aufgabennamen.
Der Zielname ist in unserem Fall also `Kommandoprotokolle.txt` und Sie rufen auf:
`rename typescript Kommandoprotokolle.txt`.
Geben Sie diese Datei ab.

Analog werden wir das künftig bei vielen Aufgaben machen.

- Die sehen jeweils so aus, dass bei den Arbeitsschritten einige mit 
  [EC], [EC] usw. markiert sind.
- Genau diese Schritte sollen im abzugebenden Kommandoprotokoll stehen.
- Vor dem ersten solchen Kommando rufen Sie also selbständig `script` auf
  und nach dem letzten `exit`, dann benennen Sie die Datei `typescript` um.
  (Eine Datei namens `typescript` sollte selbst nie eingecheckt werden.)
- Falls Sie unterwegs Fehler gemacht haben, benutzen Sie nun den Editor,
  um diese Teile zu entfernen.
- Wenn anhand der Arbeitsschritte zu erkennen ist, dass Sie zwischen den
  markierten, ins Protokoll zu übernehmenden Arbeitsschritten weitere
  Kommandos brauchen werden, empfiehlt es sich, eine zweite Shell zu
  starten, in der Sie nur die Kommandos eingeben, die für das `typescript`
  gedacht sind und sonst nichts.

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
