title: X11-Weiterleitung
stage: alpha
timevalue: 0.5
difficulty: 2
assumes: ssh
---

[SECTION::goal::idea]

- Ich weiß, was die X11-Weiterleitung ist und wie ich diese anwenden kann

[ENDSECTION]

[SECTION::background::default]

Die X11-Weiterleitung erlaubt es ihnen grafische Programme von einem entfernten Rechner oder 
WSL auf Ihrem System auszuführen.

[ENDSECTION]

[SECTION::instructions::detailed]

<replacement id='X11-Weiterleitung-targetserver'>
Zielserver = `andorra.imp.fu-berlin.de`
</replacement>

[NOTICE]
Wenn Sie WSL nutzen, brauchen Sie mindestens Windows 10 Build 19044 oder Windows 11. Wenn Sie trotzdem Probleme 
haben grafische Programm zu öffnen, könnte Ihnen der 
[Troubleshooting Guide](https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg) 
von Microsoft helfen.
[ENDNOTICE]

### X11 Weiterleitung

Stellen Sie sich vor, Sie arbeiten an einem CAD-Modell und brauchen dafür eine sehr hohe 
Rechenleistung. CAD-Modelle sind digitale, computergestützte Darstellungen von Objekten, die für Design, 
Analyse und Fertigung verwendet werden. Sie haben versucht das Modell auf ihrem Rechner zu starten, 
aber das Programm stürzt jedes Mal, wegen Resourcenmangel, ab.  
Als Veranschaulichung nehmen wir hier die `x11-apps`.

Lesen Sie die Optionen **-Y** und **-X** der ssh(1) [manpage](https://man.openbsd.org/ssh).

- [EQ] Erklären Sie den Unterschied der Optionen **-Y, -X**.

[NOTICE]
Verbinden Sie sich wenn möglich mit der sichereren Variante der beiden oben genannten Optionen.
[ENDNOTICE]

- [EC] Verbinden Sie sich mit dem Zielserver mit aktivierter X11-Weiterleitung.

Wenn keine Fehlermeldung kam und Sie sich erfolgreich auf dem Zielserver anmelden konnten, dann 
sollte die X11-Weiterleitung aktiv sein. Probieren wir es aus.

`xclock` ist ein Programm aus dem `x11-apps`-Paket. Es zeigt eine einfache Uhr an.

- [EC] Starten Sie `xclock`.
- [EC] Schließen Sie das Programm.

Sie haben gerade erfolgreich ein grafisches Programm von einem entfernten Rechner auf Ihrem System 
geöffnet.

[ENDSECTION]

[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Markdowndokument]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]

[INSTRUCTOR::Kommandoprotokoll]

[PROT::ALT:X11-Weiterleitung.prot] 

[ENDINSTRUCTOR]
