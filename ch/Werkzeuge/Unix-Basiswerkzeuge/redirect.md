title: Der redirect-Operator (>)
stage: alpha
timevalue: 0.5
difficulty: 2
assumes:
---

[SECTION::goal::idea]
Ich verstehe, wie der redirect-Operator (>) funktioniert und wie ich diesen anwende.
[ENDSECTION]

[SECTION::background::default]
Mit dem redirect-Operator werden die Ausgaben, die Sie von Ihren Befehlen bekommen in einen 
anderen Befehl oder Datei umgeleitet.
Wir werden hier ein bisschen näher auf diesen Operator eingehen.
[ENDSECTION]

[SECTION::instructions::detailed]

Nehmen Sie sich zur Hilfe der Aufgaben diesen [Beitrag](https://wiki.ubuntuusers.de/Shell/Umleitungen/) von ubuntuusers über Umleitungen.

Der redirect-Operator (>) liest den Standardoutput und schreibt es in den darauffolgenden Befehl 
oder Datei.  

Führen Sie die nächsten genannten Befehle aus und beschreiben Sie was jeweils passiert ist.

- [EQ] `ls -l /usr/bin > ls-output.txt`
- [EQ] `> ls-output.txt`
- [EQ] `ls -l /bin/usr > ls-output.txt`
- [EQ] `ls -l /bin/usr &> ls-output.txt`
- [EQ] `ls -l /usr/bin &> ls-output.txt`
- [EQ] `ls -l /usr/bin >> ls-output.txt && ls -l /usr/sbin >> ls-output.txt`

Neuere Distributionen von Linux würden den nächsten Befehl verwerfen, aber angenommen Sie hätten 
ein älteres Linux ohne Sicherheitsmaßnahmen auf Ihrem System. Führen Sie den Befehl 
sicherheitshalber nicht auf Ihrem System aus.

- [EQ] Beschreiben Sie, mit den Erkenntnissen von oben, was hier passieren würde: `ls > less`

[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]
