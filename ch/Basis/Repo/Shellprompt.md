title: Ein hilfreicher Prompt für unsere Shell
stage: beta
timevalue: 0.5
difficulty: 2
explains: Prompt
assumes: Markdown
requires: Git101
---
[SECTION::goal::product]

Ich habe in meiner Shell einen informativen Prompt, der die Orientierung 
in meinen Terminalfenstern erleichtert.

[ENDSECTION]
[SECTION::background::default]

Um anzuzeigen, dass (und wo) man nun ein Kommando eingeben kann,
zeigt eine [TERMREF::Shell] einen String an, den man "Prompt" ("Aufforderung") nennt.

Wenn man nach Ausführung eines Shellkommandos, das eine längere Ausgabe macht,
den Anfang dieser Ausgabe finden möchte, muss man also seinen letzten Prompt suchen.
Dafür ist es hilfreich, wenn dieser recht auffällig ist, insbesondere farblich.

Wenn man mehrere Shells offen hat, verliert man ferner leicht die Übersicht,
was wo ist. Deshalb ist es hilfreich, wenn der Prompt darüber Auskunft gibt.

[ENDSECTION]
[SECTION::instructions::detailed]

### Prompt einstellen

Führen Sie in Ihrer Shell folgenden Befehl aus:
```
export PS1="\[\e[1;33m\]\u\[\e[1;31m\]@\h \[\e[0;32m\]\w \[\e[0;37m\]\t \[\e[44m\] \! \[\e[40m\]\n\$ "
```  

Obiges erzeugt einen Prompt, der für schwarzen Terminal-Hintergrund konzipiert ist.
Für einen weißen sollte man z.B. das "33m" auch durch "31m" ersetzen.
Er benutzt pro Promptausgabe _zwei_ Zeilen, um eine ungestörte Eingabe zu erlauben.


### Prompt verstehen

Der Prompt hat folgende Elemente:

- `\u@\h`: Benutzername und Hostname:  
  Die sind wichtig zur Orientierung, sobald man im Bereich Systemadministration unterwegs ist.
- `\w`: Aktuelles Verzeichnis:   
  Sehr oft wichtig, weil man das im normalen Leben oft ändert
  (im ProPra vergleichsweise selten).
- `\t`: Genaue Uhrzeit:  
  Dadurch kann man bei langlaufenden Kommandos nachvollziehen, wie lange
  sie gedauert haben.
  Wenn die Ausgaben-Historie des Terminals lang genug ist, kann man damit Kommandos nachvollziehen,
  die z.B. vor gewissen Commits stattgefunden haben oder die zur Erzeugung einer bestimmten
  Datei geführt haben.
- `\!`: Kommandonummer:  
  Eine fortlaufende Nummer.
  Die Shell kann mittels `history 30` die letzten z.B. 30 Kommandos anzeigen.
  Wenn man wissen will, welche Ausgabe eines davon gehabt hat, hilft die Kommandonummer im Prompt,
  die entsprechende Stelle in der Historie zügig wiederzufinden.

Außerdem benutzt der Prompt vier verschiedene Farben
(gesteuert mittels der sogenannten ANSI-Sequenzen, die den Bärenanteil des Prompts ausmachen).
Das hat den Effekt, dass er eine charakteristische visuelle Signatur hat, die man beim
Rückwärtsrollen schnell und verlässlich entdeckt, sodass das Finden der einzelnen
Abschnitte der Ausgabe wenig anstrengend ist.


### Wer Lust hat: Prompt modifizieren

Die Tutor_innen benutzen bei der Bewertung Ihrer Abgaben ein Hilfsprogramm,
in das die obige Struktur von Prompts fest eingebaut ist.
Es ist deshalb wichtig, dass Sie einen Prompt benutzen, der die obigen vier Elemente
in dieser Reihenfolge enthält.

Davon abgesehen dürfen Sie Ihren Prompt aber auch gern nach Geschmack verändern, 
was die Farbgestaltung angeht.
Sie können ggf. auch weitere Elemente am Anfang oder am Ende des Prompts zufügen.

Dazu können Sie entweder in einer
[kurzen](https://ss64.com/bash/syntax-prompt.html)
oder einer
[ausführlichen](https://www.gilesorr.com/bashprompt/howto/)
Anleitung nachlesen, was die einzelnen Elemente bedeuten.
Oder Sie benutzen einen interaktiven "Prompt Builder",
etwa den von 
[Giles Orr](https://www.gilesorr.com/bashprompt/bpb/)
oder
[einen anderen](https://duckduckgo.com/?q=bash+prompt+generator).

[WARNING]
Die genaue Anzeige der Farben hängt vom verwendeten Terminal (und u.U. dessen Einstellungen) ab.
Das Thema ist leider ziemlich kompliziert.
Versuchen Sie also besser kein Finetuning.
[ENDWARNING]

Sie können damit ruhig experimentieren und eigene Anpassungen vornehmen. 
Sollte etwas schiefgehen,
können Sie Ihre Shell einfach schließen und wieder öffnen, um die Situation von davor zu haben.


### Prompt persistieren

Wenn Sie einen Prompt haben, mit dem Sie zufrieden sind, sorgen Sie dafür, dass er auch für neue
Shell-Instanzen verwendet wird. 
Hierfür führen Sie folgende Befehle aus und setzen anstelle
der drei Punkte analog den Rest Ihres Prompts ein.

```
echo "" >> ~/.bashrc
echo "export PS1=\"\\[\\e...\"" >> ~/.bashrc
```

[WARNING]
Für das `echo "export PS1"` stehen wir vor einem klassischen Problem in der Software-Entwicklung:
Strings in Strings. Das übliche Vorgehen wird auch hier verwendet:
Setzen Sie zunächst ein zusätzliches Backslash vor alle vorhandenen (also "\[" wird "\\[") und
zusätzlich um die Stringseparatoren von dem Wert für PS1 (also PS1=\"...\" statt PS1="").
Anschließend werden Anführungszeichen um den gesamten Teil gesetzt (also "export PS1=...").

Sie können den zweiten Befehl ohne das abschließende `>> ~/.bashrc` ausführen, um zu überprüfen, ob
Ihre Anpassung korrekt ist. Es sollte exakt derselbe Text ausgegeben werden, mit dem Sie ihren
Prompt angepasst haben.
[ENDWARNING]

Falls noch nicht aktiv, aktivieren Sie den neuen Prompt durch Aufruf von `source ~/.bashrc`.

[ENDSECTION]
[SECTION::submission::reflection]

Geben Sie eine Markdown-Datei `Shellprompt.md` ab.
Beschreiben Sie ganz kurz, was Sie warum am Prompt verändert haben oder warum nichts.

[ENDSECTION]
[SECTION::background::default]

### Es geht _noch_ mehr

Da man in den Prompt auch Aufrufe beliebiger Kommandos einstreuen kann,
ist es auch z.B. möglich, den Status des Git-Repos anzuzeigen,
etwa den aktuell benutzten Zweig.

[Ein passendes Skript](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh)
gibt es beispielsweise direkt bei git.

Nachteile solcher Lösungen sind, dass sie den Prompt noch schwerer verständlich machen,
die Konfiguration der Shell komplizierter und viel schwerer verständlich machen,
hin und wieder kaputtgehen und
bei jedem einzelnen Kommando den Prompt verlangsamen.

[ENDSECTION]

[INSTRUCTOR::Prompt-Elemente vorhanden?]
Nur kontrollieren, ob die obigen Bedingungen von
"Prompt selber bauen" eingehalten sind.
Die Kontrolle erfolgt anhand der Abgabe zu [PARTREF::Kommandoprotokolle].
[ENDINSTRUCTOR]
