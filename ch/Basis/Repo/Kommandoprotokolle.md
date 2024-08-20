title: Protokolle von Kommandos und Kommandoausgaben abgeben
stage: beta
timevalue: 0.5
difficulty: 2
requires: Shellprompt
---
[SECTION::goal::trial]

Ich kann d.h. Kommandoeingaben und -ausgaben für eine Abgabe als Kommandoprotokolldatei bereitstellen.

[ENDSECTION]
[SECTION::background::default]

Viele Aufgaben verlangen, dass Sie ein Protokoll von Geschehnissen in der Shell
abgeben: Sie rufen ein paar Kommandos auf und die Abgabe enthält diese Kommandos plus
deren jeweilige Ausgabe.
Aber auch nur dies.
"Verschmutzte" Abgaben bedeuten für die Tutor_innen hohen Mehraufwand und können zur
Zurückweisung einer Abgabe führen.
Deshalb üben wir hier das Anfertigen und die Kontrolle von Kommandoprotokollen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Kommandos ausführen

- Geben Sie der Reihe nach folgende Kommandos ein (eins davon schlägt fehl; das ist erwünscht):
    1. `ls`
    2. `uptime`
    3. `whoami`
    4. `whoareyou`
    4. `uname -a`
    5. `cat /etc/os-release`
    6. `python -V; pip -V`


### In Datei verfrachten

- Markieren Sie mit der Maus alle Kommandos und deren Ausgabe,
  also vom Beginn des Prompts vor dem `ls`-Kommando bis zum Ende der Ausgabe
  des Doppelkommandos `python -V; pip -V`.
- Kopieren Sie den markierten Block in die Zwischenablage.
  Auf Windows in Microsoft Terminal geht das mit der Tastenkombination Ctrl-C (Strg-C).
  Auf Mac OS ist es Command-C (Propeller-C).
  Auf Linux hängt es vom verwendeten Terminal ab; nötigenfalls bitte in dessen Hilfe schauen.
- Starten Sie einen Texteditor.
- Fügen Sie die Zwischenablage-Inhalte dort ein (meist mit Ctrl-V/Strg-V bzw. Command-V/Propeller-V).
  Die Farbe der Prompts geht dabei verloren, was den Text erheblich weniger übersichtlich macht.


### Bereinigen

Sie haben hoffentlich bemerkt, dass `whoareyou` nicht funktioniert hat?
Das Kommando gibt es nämlich gar nicht.
Wir tun jetzt so, als sei dies eine _versehentliche_ Fehleingabe gewesen.

So etwas wollen wir im Protokoll nicht haben, sondern es entfernen, damit es das
Verständnis des Protokolls nicht erschwert.

- Rufen Sie `nano typescript` auf.
  Nano ist ein einfacher Texteditor, der auf allen Linux-Systemen vorhanden ist.
  Die Bedienung ist in den unteren Zeilen erklärt. 
  (`^` steht für die Umschalttaste Ctrl-/Strg-, `M-` ("meta") steht für `Alt-`.)  
  Sie können alternativ auch ihre IDE benutzen, was einfacher sein dürfte.
  Allerdings ist es in vielen Notfällen hilfreich, `nano` bedienen zu können -- also
  vielleicht zumindest dieses eine Mal ausprobieren.
- Schneiden Sie das Kommando `whoareyou` aus, samt des Shell-Prompts davor
  und der Fehlermeldung dahinter.
  Speichern Sie das Ergebnis und prüfen Sie es sorgfältig.
  Nichts zu viel oder zu wenig gelöscht? Prima. Dann abgeben.
  
[NOTICE]
Es ist auch möglich, einen anderen Texteditor als `nano` zu verwenden,
falls Sie mit einem anderen besser vertraut sind.
`nano` hat aber zwei Vorteile: Er ist anfängertauglich und auf so ziemlich jedem
Linux-System vorhanden.
(Allerdings kann `nano` auch nicht viel; man setzt ihn meist nur für einfache Zwecke ein.)
[ENDNOTICE]

Allgemein gesprochen:

- Werfen Sie mit dem Editor aus dem Protokoll alles raus, was dort nicht hineingehört.
  Vertippt? Kommando ganz falsch ausgedacht? Vorher nötiges anderes Kommando vergessen?
  Löschen Sie in allen diesen Fällen den falschen Block heraus, vom Beginn des Prompts vor dem Kommando
  bis vor den Beginn des Prompts zum nächsten Kommando.
- Bereinigen Sie auch, falls Sie zwei Kommandos in einer falschen (aber ebenfalls technisch möglichen) 
  Reihenfolge durchgeführt haben: Block ausschneiden und an der richtigen Stelle wieder einsetzen.


### Speichern

- Speichern Sie schließlich die Datei als `*.prot` in Ihrem ProPra-Arbeitsverzeichnis ab.
  Wenn die Aufgabe XYZ heißt, sollte die Datei also in der Regel `XYZ.prot` heißen,
  falls nicht die Aufgabe ausnahmsweise etwas anderes festlegt.


### Taktik für spätere Aufgaben

In den Aufgaben wird es später oft so sein, dass Sie zwischen den Kommandos A und B,
die ins Kommandoprotokoll sollen, andere Kommandos brauchen, sei es 
i) zur Vorbereitung von B oder 
ii) weil Sie erst herausbekommen müssen, wie Kommando B überhaupt lautet, wenn es 
nicht angegeben, sondern nur umschrieben ist.

Es gibt grundsätzlich drei Arten, wie man damit umgehen kann:

1. Eine zweite Shell geöffnet haben, in der man die Hilfsschritte ausführt.
   In der ersten Shell macht man nur die Kommandos, die ins Protokoll sollen.
2. Sich erst einmal probehalber durch den ganzen Ablauf durcharbeiten und dann einen zweiten,
   sauberen Durchlauf machen, wenn man weiß, wie alle Kommandos gehen.
   Nur der zweite Durchlauf kommt ins Protokoll.
3. Sich irgendwie durch den ganzen Ablauf durchkämpfen, egal wie viele Fehler und Umwegen man
   unterwegs macht. Dann alles ins Protokoll übernehmen und alles sorgfältig bereinigen.

Von diesen Ansätzen funktioniert Nummer 1 für Leute gut, die extrem konzentriert arbeiten können.
Für die meisten wird der Ansatz Nummer 2 am einfachsten sein.
Ansatz Nummer 3 ist nicht empfohlen, denn das Bereinigen erfordert meist viel zu viel Konzentration.

Nicht ärgern, wenn man bei Ansatz 1 oder 2 trotzdem immer mal einen Fehler macht; das ist ganz normal.

[ENDSECTION]
[SECTION::submission::trace]

Sie sollten nun eine bereinigte Datei `Kommandoprotokolle.prot` erzeugt haben.
Geben Sie diese Datei ab.

Analog werden wir das künftig bei vielen Aufgaben machen.

- Die sehen jeweils so aus, dass bei den Arbeitsschritten einige mit 
  [EC], [EC] usw. markiert sind.
  (In unserer Aufgabe hier treten die Nummern im Abschnitt "Kommandos ausführen" an deren Stelle)
- Genau diese Schritte sollen im abzugebenden Kommandoprotokoll stehen.

Ein falsches Kommandoprotokoll kann sehr verwirrend sein.
Kontrollieren Sie deshalb vor dem Einchecken Ihr Protokoll bitte wie folgt:

- Rufen Sie `sedrila viewer` auf.
  Das startet einen Webserver.
- Besuchen Sie nun `http://localhost:8080` in Ihrem Browser.
  Sie erhalten ein Verzeichnislisting Ihres Arbeitsverzeichnisses.
- Klicken Sie `Kommandoprotokolle.prot` an.
  Das öffnet die Ansicht auf Ihr Protokoll, die Ihre Tutor_in benutzen wird.
- Überzeugen Sie sich, dass die Kommandonummern mit denen der Aufgabe übereinstimmen.
- Beenden Sie den Webserver in der Shell durch Eingabe von Ctrl-C (bzw. Strg-C bzw. Command-C).

War noch etwas verkehrt? Dann bitte nochmals korrigieren und kontrollieren.
Sie können den Webserver auch laufen lassen und nach der Korrektur die Ansicht im Webbrowser mit 
'Refresh' (F5) aktualisieren.

[ENDSECTION]

[INSTRUCTOR::Sichtung und Prüfung von Kommandoprotokollen]
Wir erwarten von Kommandoprotokollen folgendes:

1. Das Protokoll fängt in Zeile 1 mit einem Prompt an.
2. Dieser Prompt ist gemäß [PARTREF::Shellprompt], wird korrekt erkannt und entsprechend gerendert.
3. Bitte immer auf die Plausibilität dieser Prompts achten.
   Insbesondere zeigt ein falscher Benutzername an, dass dieser Studi nicht wie
   vorgesehen die Kommandosequenz selber durchgeturnt hat.
   Solche Abgaben bitte immer zurückweisen.
4. Die Nummerierung der Kommandos entspricht den [EREFC::1],[EREFC::2]-...-Markern aus der Aufgabe.
   Wenn bei der händischen Korrektur zu viel, viel zu wenig oder das Falsche weggeschnitten wurde,
   die Abgabe zurückweisen (und darauf hinweisen, dass es sehr oft einfacher sein dürfte,
   nochmal von vorn anzufangen, als die kaputte Abgabe zu reparieren).
5. Die Kommandos erfüllen den Zweck, der in der Aufgabe verfolgt wird, und zwar
   sowohl den inhaltlichen Zweck (Wirkung des Kommandos) als auch den Lernzweck (wegen dem
   bei manchen Aufgaben nicht jedes Kommando mit gleicher Wirkung akzeptabel ist).

In dieser Aufgabe sollte das Ergebnis mit `sedrila viewer` sinngemäß wie folgt aussehen
(Stand August 2024):

[PROT::ALT:Kommandoprotokolle.prot]

[ENDINSTRUCTOR]
