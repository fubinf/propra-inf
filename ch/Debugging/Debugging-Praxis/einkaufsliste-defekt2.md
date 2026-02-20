title: Debugging eines falschen Outputs
stage: beta
timevalue: 1.0
difficulty: 2
assumes: IDE-Debugging
requires: einkaufsliste-defekt
---
[SECTION::goal::trial,product]
Ich bin in der Lage, mittels Debugger durch ein Programm zu navigieren und zielstrebig einen 
[TERMREF::Versagen] aufzufinden und zu beheben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Der nächste Bug: Falscher Output

Das Programm läuft jetzt hoffentlich ohne Abstürze, allerdings ist die Ausgabe noch nicht 
wie erwartet.
Anstatt eine Auflistung der Zutaten sortiert nach Abteilung im Supermarkt zu erhalten, hat 
jede Zutat ihren eigenen Eintrag erhalten.
Vergleichen Sie dazu diese beiden Ausgaben.

[FOLDOUT::Aktueller Output für `0,0,4`]
```console
[INCLUDE::include/einkaufsliste-output-falsch.inc]
```
[ENDFOLDOUT]

[FOLDOUT::Gewünschter Output für `0,0,4`]
```console
[INCLUDE::include/einkaufsliste-output-korrekt.inc]
```
[ENDFOLDOUT]

Anders als bei einem Programmabsturz wie in der [PARTREF2::einkaufsliste-defekt::ersten Aufgabe]
ist hier nicht so klar, wo man mit der Suche nach dem [TERMREF::Defekt] anfangen soll.


### Finden des Versagens

- [EQ] Finden und nennen Sie die Stellen im Quellcode, die die Ausgabe des Programms regeln.
- [EQ] Beschreiben Sie den Aufbau dieser Funktion.
    - Was wird alles in dieser Funktion definiert?
    - Welche Variablen und Funktionen werden tatsächlich benutzt?
    - Welchen Inhalt haben diese Variablen?
    - Wo genau findet die Ausgabe der Zutaten statt?
- Setzen Sie einen [TERMREF::Breakpoint] bei der für die Ausgabe zuständigen Funktion und starten Sie 
  den Debugger.
- Springen Sie mittels Debugger zum Anfang der Schleife, in der die Ausgabe erzeugt wird.
- [EQ] Stimmen die Inhalte der Variablen damit überein, was von ihnen verlangt wird?
- [EQ] An dieser Stelle sind für diesen Fall alle Informationen vorhanden, um das Versagen  
  aufzuklären. 
  Beschreiben Sie in eigenen Worten, wie das [TERMREF::Versagen] zustande kommt.
- [ER] Beheben Sie den zugrunde liegenden [TERMREF::Defekt].
- [EC] Machen Sie einen separaten Commit des korrigierten Quellcodes und zeigen Sie dann
  `git -P show HEAD`.
- [EC] Führen Sie das Programm `grocery_list.py` im Terminal aus. 
  Geben Sie die Ausgabe des Programms mit der Eingabe `0,0,4` an.

[ENDSECTION]

[SECTION::submission::trace,snippet,information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Musterlösung]
[INCLUDE::ALT:]
[PROT::ALT:einkaufsliste-defekt2.prot]
[ENDINSTRUCTOR]
