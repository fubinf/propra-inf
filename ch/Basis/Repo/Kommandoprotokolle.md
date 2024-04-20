title: Protokolle von Kommandos und Kommandoausgaben abgeben
stage: beta
timevalue: 0.5
difficulty: 2
explains: manpage
requires: Shellprompt
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
- Geben Sie der Reihe nach folgende Kommandos ein (eins davon schlägt fehl; das ist erwünscht):
    - `ls`
    - `uptime`
    - `whoami`
    - `whoareyou`
    - `uname -a`
    - `cat /etc/os-release`
    - `python -V; pip -V`
    - `exit`
- `exit` hat die neue Shell beendet und damit auch die Protokollierung.
- Das Protokoll steht jetzt in der Datei `typescript`
- Sehen Sie es sich mit `less typescript` an.
  So ungefähr wird das Ergebnis auch für die Tutor_in aussehen.
  (Verlassen mit 'q', Hilfe mit 'h'. `less` kann eine ganze Menge.)

Es ist möglich, den Dateinamen als Argument zu übergeben, und es bietet sich an, das an die
jeweilig bearbeitete Aufgabe anzupassen. Ein Aufruf von `script Kommandoprotokolle.txt` erzeugt
beispielsweise eine Datei "Kommandoprotokolle.txt" statt "typescript".


### Taktik für spätere Aufgaben

In den Aufgaben wird es später oft so sein, dass Sie zwischen den Kommandos A und B,
die ins Kommandoprotokoll sollen, andere Kommandos brauchen, sei es i) zur Vorbereitung von B
oder ii) weil Sie erst herausbekommen müssen, wie Kommando B überhaupt lautet, wenn es 
nicht angegeben, sondern nur umschrieben ist.

Es gibt grundsätzlich drei Arten, wie man damit umgehen kann:

1. Eine zweite Shell geöffnet haben, in der man diese Hilfsschritte zuführt.
   In der ersten Shell läuft währenddessen `script`, dort macht man nur A und B, sonst nichts.
   Dies ist die Methode der Wahl.
2. Sich erst einmal ohne laufendes `script` durcharbeiten und dann `script` erst starten,
   wenn man weiß, wie A und B gehen. 
   Das hilft allerdings nur im obigen Fall ii), nicht bei i).
3. Es ist auch möglich, ohne neue Shell die Befehle einzeln nach und nach zu protokollieren.
   Man ruft für jedes zu protokollierende Kommando einzeln `script -a -c 'mycmd myarg1'` auf
   (siehe `script --help`).  
   Leider wird dann im Protokoll jeder Kommandooutput von einer Start- und einer Endmeldung
   umschlossen und die farbigen Shellprompts fehlen, so dass dieses Format für die 
   Tutor_innen zu unübersichtlich ist und für das ProPra nicht in Frage kommt.


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
  Sie können alternativ auch ihre IDE benutzen, was einfacher sein dürfte.
  Allerdings ist es in vielen Notfällen hilfreich, `nano` bedienen zu können -- also
  vielleicht zumindest dieses eine Mal ausprobieren.
- Wie Sie sehen, sieht das Protokoll plötzlich viel komplizierter aus.
  Das liegt daran, dass Steuercodes jetzt sichtbar gemacht werden.
  Die im Terminal von diesen Steuercodes bewirkte Farbigkeit ist hingegen verschwunden.
- Schneiden Sie das Kommando `whoareyou` aus, samt des Shell-Prompts davor
  und der Fehlermeldung dahinter.
  Speichern Sie das Ergebnis und prüfen Sie es sorgfältig.
  Nichts zu viel oder zu wenig gelöscht? Prima. Dann abgeben:
  
[NOTICE]
Seien Sie sich bewusst, dass die Dateien möglicherweise Symbole beinhalten werden, die Ihnen nicht vertraut
sind. Diese dienen der Formatierung (also beispielsweise Farbe). 
Entfernen Sie daher nicht pauschal alle diese Symbole!
[ENDNOTICE]

[NOTICE]
Es ist auch möglich, einen anderen Texteditor als `nano` zu verwenden,
falls Sie mit einem anderen besser vertraut sind.
`nano` hat aber zwei Vorteile: Er ist anfängertauglich und auf so ziemlich jedem
Linux-System vorhanden.
(Allerdings kann `nano` auch nicht viel; man setzt ihn meist nur für einfache Zwecke ein.)
[ENDNOTICE]

[ENDSECTION]
[SECTION::submission::trace]

Falls Sie keinen geeigneten Ausgabedateinamen beim Aufruf von `script` angegeben haben,
nenennen Sie die Datei `typescript` in in eine Datei mit Endung `.txt` um.
Der Zielname ist in unserem Fall also `Kommandoprotokolle.txt` und Sie rufen auf:
`mv typescript Kommandoprotokolle.txt`.
Geben Sie diese Datei ab.

Analog werden wir das künftig bei vielen Aufgaben machen.

- Die sehen jeweils so aus, dass bei den Arbeitsschritten einige mit 
  [EC], [EC] usw. markiert sind.
- Genau diese Schritte sollen im abzugebenden Kommandoprotokoll stehen.
- Vor dem ersten solchen Kommando rufen Sie also **selbständig** `script` auf
  und nach dem letzten `exit`, dann benennen Sie die Ausgabedatei gegebenenfalls um.
  (Eine Datei namens `typescript` sollte selbst nie eingecheckt werden.)
- Oder Sie benutzen einzelne `script`-Aufrufe für jedes zu protokollierende Kommando.
- Falls Sie unterwegs Fehler gemacht haben, benutzen Sie nun den Editor,
  um diese Teile zu entfernen.
- Wenn anhand der Arbeitsschritte zu erkennen ist, dass Sie zwischen den
  markierten, ins Protokoll zu übernehmenden Arbeitsschritten weitere
  Kommandos brauchen werden, empfiehlt es sich, in einem separaten Fenster eine zweite Shell zu
  starten, in der Sie nur die Kommandos eingeben, die für das `typescript`
  gedacht sind und sonst nichts.

[ENDSECTION]

[INSTRUCTOR::Sichtung und Prüfung von Kommandoprotokollen]
Wir erwarten eine Datei, in der außer dem von `script` eingefügten Kopf und Fuß
optisch gesehen nur genau das steht, was obige Kommandos erzeugen sollen.
Faktisch sind vielleicht einige Backspaces etc. dabei, wenn welche eingegeben wurden,
aber im Wesentlichen ist das Ergebnis mit `less` gut lesbar.

Wenn bei der Korrektur zu viel, zu wenig oder das Falsche weggeschnitten wurde,
die Abgabe zurückweisen (und darauf hinweisen, dass es meist einfacher sein dürfte,
nochmal von vorn anzufangen, als die kaputte Abgabe zu reparieren).

Es muss jeweils ein Prompt dastehen, 
der den Anforderungen von [PARTREF::Shellprompt] genügt.
Bitte immer auf die Plausibilität dieser Prompts achten.
Insbesondere zeigt ein falscher Benutzername an, dass dieser Studi nicht wie
vorgesehen die Kommandosequenz selber durchgeturnt hat.
Solche Abgaben bitte immer zurückweisen.
[ENDINSTRUCTOR]
