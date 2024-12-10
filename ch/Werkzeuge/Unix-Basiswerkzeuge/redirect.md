title: Der redirect-Operator (>)
stage: alpha
timevalue: 1
difficulty: 2
---

[SECTION::goal::idea]
Ich verstehe, wie der redirect-Operator (>) funktioniert und wie ich diesen anwende.
[ENDSECTION]

[SECTION::background::default]
Mit dem [TERMREF::redirect-Operator] werden die Ausgaben, die Sie von Ihren Befehlen bekommen in 
eine Datei umgeleitet.
[ENDSECTION]

[SECTION::instructions::detailed]

Der [TERMREF::redirect-Operator] (>) in der Shell sorgt dafür, dass die Standardausgaben
des davorstehenden Kommandos in die dahinter angegebene Datei umgeleitet werden.  

Lesen Sie den Abschnitt **"Umleiten der Ausgabe mit >"** von 
[HREF::https://wiki.ubuntuusers.de/Shell/Umleitungen/].


### Funktionsweise des Operators

Führen Sie die nächsten genannten Befehle aus und beschreiben Sie mithilfe der Dokumentation,
was jeweils passiert ist.

- [EQ] `ls -l /usr/bin > redirect.out`
- [EQ] `> redirect.out`
- [EQ] `ls -l /bin/usr > redirect.out`
- [EQ] `ls -l /bin/usr &> redirect.out`
- [EQ] `ls -l /usr/bin &> redirect.out`
- [EQ] `ls -l /usr/bin >> redirect.out && ls -l /usr/sbin >> redirect.out`

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