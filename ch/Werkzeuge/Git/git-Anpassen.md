title: Git Anpassen
stage: alpha
timevalue: 0.1
difficulty: 2
assumes: git-Funktionsweise
---

[SECTION::goal::idea]

Ich lerne wie ich mir meine Git-Installation durch angepasste Konfiguration und Aliase zu eigen 
machen kan.

[ENDSECTION]

[SECTION::background::default]

Git bringt neben der Standardkonfiguration noch hunderte Optionen mit, welche man sich nach 
Belieben anpassen kann, manches spart Zeit, anderes Ärger und anderes ist wiederrum einfach nur 
persönliche Präferenz. Außerdem helfen Aliase einem Befehle welche man oft verwendet abzukürzen 
und machen einem so das Leben leichter. 

[WARNING]
Diese Aufgabe erfordert nicht wirklich Vorkenntnisse, allerdings empfiehlt es sich, sie 
erst im späteren Verlauf zu bearbeiten, da hier vor allem persönliche Präferenz gefragt ist. 
wenn man also noch nicht viel mit git gearbeitet hat, dann lässt sich hier nicht viel von 
ebendieser einbringen.
[ENDWARNING]

[ENDSECTION]

[SECTION::instructions::loose]

### git Konfiguration

Beginnen wir zuerst mit der git-Config. Diese erlaubt uns die gesetzten Standardwerte zu 
überschreiben und nach unseren Wünschen anzupassen. Dies kann auf globaler Ebene, also für alle 
Aufrufe im System, oder auf Repository-Ebene passieren.

Für das Bearbeiten dieser Aufgabe werden wir die [Git Book Seite über Customizing Git](https://
git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_git_config) zu Hilfe nehmen. Hier 
finden Sie eine Übersicht und entsprechende Erklärungen zu vielen Interessanten git 
Konfigurationseinstellungen. Einige, aus unserer Sicht, besonders wichtigen Einstellungen führen 
wir hier auf. Im Kern geht es aber darum, dass Sie sich selber einen Eindruck darüber 
verschaffen, was es für Anpassungsmöglichkeiten gibt und welche ihnen besonders nützlich 
erscheinen. 

Schauen wir nun also die etwas wichtigeren Einstellungen an. 
Leider ist die git book seite nicht besonders gut mit Links versehen deshalb referenzieren wir 
hier einfach nur die jeweiligen Einstellungen, benutzen Sie ggf. einfach die Suchfunktion ihres 
Browsers.

`core.autocrlf` erlaubt Git einem automatisch beim Pullen oder Pushen, Zeilenumbrüche an die Unix 
bzw. Windows konvention anzupassen. Gerade wenn man also zwischen diesen Systemen viel hin und her 
arbeitet, sollte man dieses Setting angeschaut haben.

`core.editor` ermöglicht einem den Editor festzulegen, welchen git beim Benutzen bestimmter Befehle 
(commit, rebase, etc.) öffnet.

`core.excludesfile` nimmt einen Pfad zu einer globalen [PARTREF::git-ignore]-Datei entgegen. 
Diese erlaubt automatisch bestimmte Dateien in *allen* Repos zu ignorieren. So bietet es sich 
z.B. an auf macOS Systemen die `.DS_Store` Ordner, welche Eigenschaften, Thumbnails und andere 
OS-spezifische Dinge enthält, automatisch zu ignorieren, da sie für unser Repo nicht interessant 
sind und im Zweifel nur für unnötigen Datenmüll sorgen.

Jetzt sind Sie gefragt. Lesen Sie die verlinkte Seite in Ruhe durch und recherchieren Sie im 
Internet. Welche weiteren nützlichen git-Einstellungen gibt es noch? 

[EC] Suchen Sie mindestens drei weitere git-Einstellungen und erklären Sie, warum gerade diese 
für Sie Interessant sind.

### Git Aliases

Ein weiteres sehr nützliches Boardmittel von git sind die sogenannten Aliase. Diese kennen Sie 
vielleicht bereits aus dem Bash/Unix-Teil dieses Kurses. Wenn nicht, ist das aber auch nicht 
schlimm, da wir alles nötige hier erklären und durchexerzieren werden.
Im Grunde sind Aliase einfach nur neue Namen für ausgewählte git Kommandos. Welche Kommandos und 
welche Namen können wir dabei komplett frei wählen.
So ließe sich z.B. ein eigener git-Befehl erstellen, welcher `git commit -m "message"` auf `git 
cm "message"` kürzt. Gerade für Befehle, welche man öfter benutzt, bietet es sich an eigene Aliase 
anzulegen.
Auch hierfür gibt es wieder [eine Seite im git Book](https://git-scm.
com/book/en/v2/Git-Basics-Git-Aliases) welche uns alles Wichtige nochmal gründlich erklärt.
Als Erstes lesen Sie einmal diese Seite komplett bis zum Ende.
Wenn ihnen dabei schon Aliase auffallen die Sie für Nützlich halten, können Sie diese natürlich 
gerne schon auf ihrem eigenen System einrichten.

Sie haben es vielleicht schon geahnt, aber auch hier geht es wieder um eine kleine "Recherche". 
Suchen Sie im Internet nach weiteren git Aliases. 

[EC] Suchen Sie mindestens drei weitere git-Aliase und erklären Sie, warum gerade diese 
für Sie Interessant sind.

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