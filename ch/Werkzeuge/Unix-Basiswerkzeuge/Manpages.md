title: "Manpages: Die Unix-Handbuchseiten"
stage: beta
timevalue: 1.0
difficulty: 2
explains: manpage
---

[SECTION::goal::idea]
Ich verstehe wie ich mir Infos aus Manpages holen kann, wenn ich nicht mehr weiter komme.
[ENDSECTION]

[SECTION::background::default]
Die Unix Manual Pages (meist abgekürzt Man Pages und oft geschrieben als Manpages) 
sind ein mächtiges Hilfsmittel, um schnell _korrekte_ Informationen über Unix-Werkzeuge zu finden, 
wenn man weiß, wo man suchen muss.
[ENDSECTION]

[SECTION::instructions::detailed]

### Einlesen

Lesen Sie sich diesen kurzen
[Artikel über manpages](https://www.baeldung.com/linux/man-pages)
durch.
Damit kann man schon mal loslegen, aber wer Manpages gründlich verstehen will,
sollte bei diesem
[längeren Beitrag](https://itsfoss.com/linux-man-page-guide/) 
weiterlesen.


### Installieren

Auf manchen Varianten von Unix sind die Manpages nicht standardmäßig installiert.
Probieren Sie `man man`. 
Wenn das nicht funktioniert, führen Sie 
`sudo apt update && sudo apt install man-db manpages manpages-dev` aus.


### Ausprobieren

- [EQ] Schauen Sie sich die Manpages von `find` und von `grep` an.
  Nicht komplett durchlesen; nur einen Überblick über die Seite bekommen.
  Wie finden Sie diese Manpages?
- [EQ] Schauen Sie sich die manpage von `wc` an. 
  Wie finden Sie im Vergleich zu den vorherigen diese Manpage?

Informationen in manpages zu finden ist oft etwas mühsam und deswegen auch nicht 
empfehlenswert für den Anfang, da es zu viel Informationen auf einmal liefert, anstatt
Grundlegendes von Fortgeschrittenem zu trennen.
Manpages sind aber sehr nützlich, wenn man schon ungefähr weiß, wonach man sucht.


### Anzeige und Suche

Das `man`-Kommando gibt eigentlich die gesamte Manpage auf einen Rutsch aus.
Da das meist unpraktisch ist, ruft es bei interaktiver Verwendung automatisch
den `PAGER` auf (siehe `man man`), meistens das Programm `less` (siehe `man less`),
das Blättern und Stringsuche unterstützt.

Für eine Stringsuche nutzt man das Zeichen `/` gefolgt von 
dem Wort welches man sucht. Man muss auf die Groß- und Kleinschreibung achten, 
sonst findet man es unter Umständen nicht.


### Abschnittsstruktur der Manpages, Leseratschläge

- Manpages haben eine ungefähr einheitliche Abschnittstruktur, beginnend mit
  "Name", "Synopsis" und "Description".
  Ein oft sehr langer Abschnitt ist "Options".
- Manche (leider nur manche) Manpages haben Beispiele am Ende, im Abschnitt "Examples". 
  Sie helfen, um schneller einen Überblick des Kommandos zu bekommen
  und sind auch oft günstig, wenn man das Kommando _eigentlich_ schon kennt.
- Bevor man ein Kommando aufruft, dass man irgendwo im Netz oder in fremdem Code gefunden hat,
  sollte man prüfen, was die einzelnen Optionen bedeuten, 
  sonst kann man unschöne Überraschungen erleben. 
- Falls einem die Manpage-Anzeige im Terminal nicht zusagt, kann man Manpages auch online finden, 
  indem man `man <Kommando>` sucht.
  Aber Vorsicht: Von einer Unix-Variante zur andern gibt es oft kleine Unterschiede bei 
  vielen Kommandos.


### Üben

- [EQ] Mit einem der obigen drei Kommandos kann man unter anderem eine reine Liste der Namen
  aller `.md`-Dateien im aktuellen Verzeichnis ausgeben, die das Wort "meistens" enthalten.
  Finden Sie mittels der drei Manpages heraus, wie das geht.

[HINT::Lesetipp]
Häufig geht eine solche Suche am besten, wenn man sich auf die Langnamen der
Optionen konzentriert und die Seite durchblättert, anstatt eine Textsuche zu probieren.
Aber der erste Schritt ist immer, zu entscheiden, welches Kommando überhaupt das Richtige ist,
also auf welcher Manpage man suchen sollte.
[ENDHINT]


### Der Notnagel: `--help`

Viele Kommandos bieten eine Option `--help` an, die eine Hilfeausgabe macht,
die z.B. die (wichtigsten) Optionen sehr kurz erklärt.
Häufig reicht das, z.B. wenn einem nur der Optionsname entfallen war.

Bei Kommandos, die keine Manpage haben, ist die Option `--help` u.U. 
die einzige Information, die man schnell zur Hand hat.

[EQ] Probieren Sie das für das Kommando `cd` aus.
Was haben Sie neues darüber gelernt?

[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Wir haben geringe Ansprüche]
- Die Manpages von `grep` und `find` sind umfangreich und dementsprechend einschüchternd,
  mit der von `wc` sollte hingegen jeder klar kommen.
- `grep -l *.md`
[ENDINSTRUCTOR]