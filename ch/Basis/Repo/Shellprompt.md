title: Ein hilfreicher Prompt für unsere Shell
stage: beta
timevalue: 0.5
difficulty: 2
explains: Prompt
requires: Git101, Markdown
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

Fügen Sie an die Datei `.bashrc` in Ihrem Homeverzeichnis (`~/.bashrc`)
folgende Zeile an:  
`export PS1="\[\e[1;33m\]\u\[\e[1;31m\]@\h \[\e[0;32m\]\w \[\e[0;37m\]\t \[\e[44m\] \! \[\e[40m\]\n\$ "`  
(Falls es bei Ihnen die Datei `~/.bash_profile` geben sollte, ist die Zeile hingegen dort richtig aufgehoben.)

Benutzen Sie dafür z.B. den Editor nano:
`nano ~/.bashrc`.
Wie man da wieder rauskommt, ist am unteren Bildschirmrand beschrieben
(`^` steht für die Umschalttaste Ctrl-/Strg-, `M-` ("meta") steht für `Alt-`.).

Obiges erzeugt einen Prompt, der für schwarzen Terminal-Hintergrund konzipiert ist.
Für einen weißen sollte man z.B. das "33m" auch durch "31m" ersetzen.
Er benutzt pro Promptausgabe _zwei_ Zeilen, um eine ungestörte Eingabe zu erlauben.

Aktivieren Sie den neuen Prompt durch Aufruf von `source ~/.bashrc`.


### Prompt verstehen

Der Prompt hat folgende Elemente:

- Benutzername und Hostname:  
  Die sind wichtig zur Orientierung, sobald man im Bereich Systemadministration unterwegs ist.
- Aktuelles Verzeichnis:  
  Sehr oft wichtig, weil man das im normalen Leben oft ändert
  (im ProPra vergleichsweise selten).
- Genaue Uhrzeit:  
  Dadurch kann man bei langlaufenden Kommandos nachvollziehen, wie lange
  sie gedauert haben.
  Wenn die Ausgaben-Historie des Terminals lang genug ist, kann man damit Kommandos nachvollziehen,
  die z.B. vor gewissen Commits stattgefunden haben oder die zur Erzeugung einer bestimmten
  Datei geführt haben.
- Kommandonummer:  
  Eine fortlaufende Nummer.
  Die Shell kann mittels `history 30` die letzten z.B. 30 Kommandos anzeigen.
  Wenn man wissen will, welche Ausgabe eines davon gehabt hat, hilft die Kommandonummer im Prompt,
  die entsprechende Stelle in der Historie zügig wiederzufinden.

Außerdem benutzt der Prompt vier verschiedene Farben.
Das hat den Effekt, dass er eine charakteristische visuelle Signatur hat, die man beim
Rückwärtsrollen schnell und verlässlich entdeckt, sodass das Finden der einzelnen
Abschnitte der Ausgabe wenig anstrengend ist.


### Prompt selber bauen

Sie dürfen Ihren Prompt gern nach Geschmack umbauen, was die Elemente,
ihre Reihenfolge und die Farbgestaltung angeht.

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

Falls Sie sich einen eigenen Prompt bauen, behalten Sie bitte mindestens folgende Elemente
des obigen Vorschlags bei, um den Tutor_innen die Arbeit zu erleichtern:

- Benutzername
- aktuelles Verzeichnis
- Uhrzeit (24h-Format, mit Sekunden)
- Kommandonummer
- mindestens zwei verschiedene Farben
- mindestens einen auffällig massivfarbenen Block

Der Prompt sollte ordentlich mit dunklem Bildschirmhintergrund funktionieren,
auch wenn Sie selbst vielleicht einen hellen einsetzen.

[ENDSECTION]
[SECTION::submission::reflection]

Geben Sie eine Markdown-Datei ab.
Begründen Sie entweder, warum Sie sich gegen ein Umbauen des vorgegebenen Prompts entschieden haben,
oder, wie ihr eigener Prompt aussieht und warum.

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
