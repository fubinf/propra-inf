title: Git Anpassen
stage: alpha
timevalue: 1
difficulty: 2
assumes: git-Funktionsweise
---

[SECTION::goal::idea]

Ich lerne wie ich mir meine Git-Installation durch angepasste Konfiguration und Aliase zu eigen 
machen kan.

[ENDSECTION]

[SECTION::background::default]

Git ist stark anpassbar; es bringt hunderte Optionen für Konfiguration und Einstellungen mit.
Manche machen die nötigen Git-Kommandos kürzer, andere vermeiden Ärger und Fehler,
noch andere sind nur für spezielle Situationen relevant,
manche sind weitgehend Geschmackssache.

[WARNING]
Die Wahl von Einstellungen erfordert viele Entscheidungen.
Wenn man keine Erfahrung mit git hat, fehlt für solche Entscheidungen oft die Grundlage.
Bearbeiten Sie diese Aufgabe deshalb erst, wenn Sie eigene git-Erfahrung gesammelt haben.
[ENDWARNING]

[ENDSECTION]

[SECTION::instructions::loose]

Als Primärquellen für diese Aufgabe empfehlen wir sowohl die git Book Seite über die [git config]
(https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_git_config) als auch über 
[git Aliase](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases). Beide enthalten nützliche 
Informationen zu den jeweiligen Anpassungsmöglichkeiten ihrer git-Installation. 
Hauptziel der Aufgabe wird sein, ein paar besonders interessante Konfigurationsoptionen zu 
entdecken, welche sich in ihrem git-Alltag als nützlich erweisen könnten. Außerdem werden Sie 
diese Aufgabe hoffentlich als Inspiration nutzen, um ihre eigene git-Umgebung weiter anzupassen 
und im Internet nach weiteren interessanten Konfigurationen und Aliasen zu suchen.

Bevor wir dazu kommen, werfen wir aber erstmal einen Blick auf unsere bestehende config. Das 
machen wir ganz einfach mit dem Befehl `git config --global --list`.

[EQ] Beschreiben Sie die Funktion der einzelnen Argumente des oben genannten `git config` Befehls 
und welche Ausgabe Sie in ihrem Terminal erhalten. 
[EQ] Wann und wie haben wir diese Konfigurationseinstellungen gesetzt?
[EQ] Kann man auch Repository-spezifische Einstellungen setzen? Wenn ja, wie macht man das?

Nun, da wir gesehen haben wie wir unsere git Konfiguration betrachten können, schauen wir uns 
mal ein paar erweiterte Befehle an. 


## Standardprogramme

Für einige Befehle fällt git auf andere Programme des Systems zurück. Häufig kann es dabei 
passieren, dass dabei aber nicht die vom Nutzer präferierte Wahl getroffen wird. Git liefert uns 
gleich mehrere Optionen zum dauerhaften Überschreiben der Standardauswahl. So lässt sich mit 
`core.editor` der Standardeditor für z.B. Commit-Nachrichten oder Rebasing anpassen und mit 
`diff.tool` kann man ein externes Programm zum Betrachten von diffs festlegen.

[EQ] Welchen Standardeditor verwenden Sie im Terminal und warum?
[EQ] Welche alternativen diff-Tools gibt es?

## Globale .gitignore-Datei

Auf Windows und macOS legt der Dateiexplorer gerne unsichtbare Dateien an, um bestimmte 
Einstellungen zur Darstellung von Verzeichnissen festzulegen. Praktisch nie sind diese Dateien 
für ein git-Repository relevant oder sollten in dieses Eingecheckt werden.
Damit das nicht passiert bietet git den Befehl `core.excludesfile` an. Diese Option nimmt einen 
Pfad zu einer globalen [PARTREF::git-ignore]-Datei entgegen und erlaubt automatisch bestimmte 
Dateien in *allen* Repos zu ignorieren. 

[EQ] Welche Dateien möchte man auf Windows und macOS *unbedingt* zur `core.
excludesfile`-Einstellung hinzufügen?

## Windows und die Zeilenumbrüche

Anders als Unix-Artige Systeme wie macOS oder Linux verwendet Windows noch 
immer für Zeilenumbrüche die Sonderzeichen `\r\n` anstelle von nur `\n`. Arbeitet man nun 
entweder allein oder mit anderen Menschen auf verschiedenen Systemen, kann es nach dem Speichern 
im eigenen Editor leicht zu Problemen bzw. einfach unschönen Dateien kommen. Um dem Ganzen 
abhilfe zu schaffen, bietet git mehrere Optionen für das Handling von Zeilenumbrüchen an.
`core.autocrlf` und `core.eol`. Wenn wir also z.B. nie wieder Windows-Style Zeilenumbrüche haben 
wollen, können wir die Einstellungen wie folgt setzen:

```yaml
core.autocrlf=input
core.eol=lf
```

[EQ] Was tut `core.autocrlf` und warum setzen wir es auf `input`?
[EQ] Was tut `core.eol` und warum setzen wir es auf `lf`?
[EQ] Wie müssten die beiden Einstellungen aussehen, wenn wir ausschliesslich auf Windows-Systemen 
arbeiten und dementsprechend `\r\n`-Zeilenenden haben wollen würden?

## Aliase

Wie weiter oben bei den Quellenangaben bereits erwähnt bietet auch git die Möglichkeit 
sogenannte [TERMREF::Aliase::-e] anzulegen. 
Ein nützliches Beispiel wollen wir uns nun anschauen:

`alias.logll=log --pretty="%ad %<(10,trunc)%an %h %s" --date=format:%y%m%d`

[EQ] Erklären sie was dieses Alias tut und probieren Sie es in ihrer eigenen git-Umgebung aus.

## config-example 5



[ENDSECTION]

[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Hier gibt es kein richtig oder falsch. Zumindest die Funktionsweise sollte aber 
gezeigt werden]

Von den Studierenden sollte ein Markdowndokument mit den Konfigurationseinstellungen sowie den 
neuen Aliasen abgegeben werden. Dazu sollte es jeweils eine kurze Erklärung geben, warum gerade 
diese gewählt wurden. Lassen Sie sich im Zweifelsfall zeigen, was welche Einstellung bzw. 
welches Alias macht. 

[ENDINSTRUCTOR]