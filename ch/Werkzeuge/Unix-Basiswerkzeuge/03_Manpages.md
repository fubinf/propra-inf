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
Lesen Sie sich diesen kurzen
[Artikel über manpages](https://www.baeldung.com/linux/man-pages)
durch.
Damit kann man schon mal loslegen, aber wer Manpages gründlich verstehen will,
sollte bei diesem
[längeren Beitrag](https://itsfoss.com/linux-man-page-guide/) 
weiterlesen.

- Schauen Sie sich die Manpages von `find` und von `grep` an.
  Nicht komplett durchlesen; nur einen Überblick über die Seite bekommen.
- [EQ] Wie finden Sie diese Manpages?
- Schauen Sie sich die manpage von `wc` an.
- [EQ] Wie finden Sie im Vergleich zu den vorherigen diese Manpage?
- [EQ] In welcher Manpage würden Sie persönlich eher Informationen finden?

Informationen in manpages zu finden ist oft etwas mühsam und deswegen auch nicht 
empfehlenswert für den Anfang, da es zu viel Informationen auf einmal liefert anstatt
Grundlegendes von Fortgeschrittenem zu trennen.
Manpages sind aber sehr nützlich, wenn man schon ungefähr weiß, wonach man sucht.

Um in Manpages schneller etwas zu finden, nutzt man das Zeichen `/` gefolgt von 
dem Wort welches man sucht. Man muss auf die Groß- und Kleinschreibung achten, 
sonst findet man es unter Umständen nicht.

Einige manpages haben Beispiele am Ende. Sie helfen, um einen Überblick des 
Kommandos zu bekommen. Daraufhin sollte man immer prüfen, was die einzelnen 
Optionen aussagen, sonst kann man ganz schnell Scheiße auf dem System bauen. 

Falls einem die Manpages in Linux nicht gefallen, kann man diese auch online 
finden, indem man `man <Kommando>` sucht.

- [EQ] Mit einem der obigen drei Kommandos kann man unter anderem eine Liste
  aller `.md`-Dateien im aktuellen Verzeichnis ausgeben, die das Wort "meistens" enthalten.
  Finden Sie mittels der drei Manpages heraus, wie das geht.

[HINT::Lesetipp]
Häufig geht eine solche Suche am besten, wenn man sich auf die Langnamen der
Optionen konzentriert und die Seite durchblättert, anstatt eine Textsuche zu probieren.
Aber der erste Schritt ist immer, zu entscheiden, welches Kommando überhaupt das Richtige ist,
also auf welcher Manpage man suchen sollte.
[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
