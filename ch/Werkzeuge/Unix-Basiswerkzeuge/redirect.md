title: Der redirect-Operator (>)
stage: alpha
timevalue: 1
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe, wie der redirect-Operator (>) funktioniert und wie ich diesen anwende.
[ENDSECTION]

[SECTION::background::default]
Mit dem [TERMREF::redirect-Operator] werden die Ausgaben, die Sie von Ihren Befehlen bekommen in einen 
anderen Befehl oder Datei umgeleitet.
[ENDSECTION]

[SECTION::instructions::detailed]

Der [TERMREF::redirect-Operator] (>) liest den Standardoutput und schreibt es in den darauffolgenden Befehl 
oder Datei.  

Lesen Sie den Abschnitt **"Umleiten der Ausgabe mit >"** des 
[Beitrags](https://wiki.ubuntuusers.de/Shell/Umleitungen/) von ubuntuusers über Umleitungen.

### Funktionsweise des Operators

Führen Sie die nächsten genannten Befehle aus und beschreiben Sie was jeweils passiert ist.

- [EQ] `ls -l /usr/bin > ls-output.txt`
- [EQ] `> ls-output.txt`
- [EQ] `ls -l /bin/usr > ls-output.txt`
- [EQ] `ls -l /bin/usr &> ls-output.txt`
- [EQ] `ls -l /usr/bin &> ls-output.txt`
- [EQ] `ls -l /usr/bin >> ls-output.txt && ls -l /usr/sbin >> ls-output.txt`

Neuere Distributionen von Linux würden den unteren Befehl verwerfen. Führen Sie den Befehl 
sicherheitshalber nicht auf Ihrem System aus.  
Nehmen Sie an, Sie hätten ein älteres Linux mit weniger Sicherheitsmaßnahmen auf Ihrem System. 

- [EQ] Beschreiben Sie, mit den Erkenntnissen von oben, was hier passieren würde: `ls > less`

[ENDSECTION]

[SECTION::submission::reflection]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Erwartung]
[INCLUDE::/_include/Instructor-Auseinandersetzung.md]
[ENDINSTRUCTOR]