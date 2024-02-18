title: Debugging eines Einkaufslisten-Generators mit falschem Output
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: idedebugging
requires: Einkaufsliste-01
---
[SECTION::goal::trial,product]
Ich bin in der Lage mittels Debugger durch ein Programm zu navigieren und zielstrebig einen 
Defekt aufzufinden und zu beheben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Der nächste Bug: Falscher Output

Das Programm läuft jetzt vermeintlich fehlerfrei, allerdings ist die Ausgabe noch nicht 
wie erwartet.
Anstatt eine Auflistung der Zutaten sortiert nach Abteilung im Supermarkt zu erhalten, hat 
jede Zutat seinen eigenen Eintrag erhalten.
Vergleichen Sie dazu diese beiden Ausgaben.

[HINT::Aktueller Output für `0,0,4`]
```console
[INCLUDE::Einkaufsliste_Falscher-Output.inc]
```
[ENDHINT]

[HINT::Gewünschter Output für `0,0,4`]
```console
[INCLUDE::Einkaufsliste_Gewünschter-Output.inc]
```
[ENDHINT]

Während in [PARTREFMANUAL::Einkaufsliste-01::der ersten Aufgabe] noch ein [TERMREF::Defekt] zu 
beheben war, müssen wir 
hier ein [TERMREF::Versagen] beheben.

### Finden des Versagens

- [EQ] Beschreiben Sie kurz, warum es sich hier handelt um ein [TERMREF::Versagen] 
  und nicht um einen [TERMREF::Defekt] handelt.
- [EQ] Beschreiben Sie kurz, welche Konsequenz es die Programmausführung in diesem Fall hat, 
  dass es sich um ein [TERMREF::Versagen] handelt.
- [EQ] Wir wissen, dass sich um einen Fehler bei der Ausgabe des Programms handelt. 
  Finden und nennen Sie die Stelle(n) im Quellcode, die die Ausgabe des Programms regeln.
- [EQ] Beschreiben Sie den Aufbau dieser Funktion.
    - Was wird alles in dieser Funktion definiert?
    - Welche Variablen und Funktionen werden tatsächlich benutzt?
    - Welchen Inhalt haben diese Variablen?
    - Wo genau findet die Ausgabe der Zutaten statt?
- Setzen Sie einen [TERMREF::Breakpoint] an der für die Ausgabe zuständige Funktion und starten Sie 
  den 
  Debugger.
- Springen Sie mittels Debugger zum Anfang der Schleife, in der die Ausgabe generiert wird.
- [EQ] Stimmen die Inhalte der Variablen damit überein, was von ihnen verlangt wird?
- [EQ] An dieser Stelle sind für diesen Fall alle Informationen vorhanden, um das Versagen  
  aufzuklären. 
  Beschreiben Sie in eigenen Worten, wie das [TERMREF::Versagen] zustande kommt.
- [ER] Beheben Sie den zugrunde liegenden [TERMREF::Defekt].
- [EC] Führen Sie das Programm `grocery_list.py` im Terminal aus. 
  Geben Sie die Ausgabe des Programms mit der Eingabe `0,0,4` an.

[ENDSECTION]
[SECTION::submission::trace,snippet,information]
[INCLUDE::../../_include/Kommandoprotokoll.md]
[INCLUDE::../../_include/Markdowndokument.md]
Geben Sie außerdem den Quellcode der Funktion an, in der Sie den Fix implementiert haben, inklusive 
des Fixes.
[ENDSECTION]

[INSTRUCTOR::Inhalt der Abgabe]
Der Weg zum Ziel der Aufgabe ist sehr geradlinig beschrieben, alle Abgaben sollten in etwa die 
gleichen Inhalte haben.

Der geforderte Fix findet in nur einer Funktion statt.
[ENDINSTRUCTOR]
