title: Debugging eines Einkaufslisten-Generators mit bedingungsabhängigem Defekt
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: idedebugging
requires: Einkaufsliste-02
---
[SECTION::goal::trial,product]
Ich bin in der Lage mittels Debugger durch ein Programm zu navigieren, kann 
bedingungsabhängige Defekte erkennen und beheben.
[ENDSECTION]

[SECTION::instructions::detailed]

### Der letzte Bug: Ein bedingungsabhängiger Bug

- [EQ] Testen Sie manuell alle möglichen Eingaben für das Programm einzeln, also erst `0`, dann 
  `1,`, usw.
  Bei welchen Eingaben erhalten Sie eine Fehlermeldung?
  Wie lautet die Fehlermeldung?
- [EQ] Die in den Fehlermeldungen genannte Stelle kommt uns aus der 
  [PARTREFMANUAL::Einkaufsliste-01::ersten Aufgabe] bekannt vor.
  Welche Zeile wird in der Fehlermeldung referenziert?
- Setzen Sie an der in der Fehlermeldung genannten Stelle im Quellcode einen Breakpoint.
  Da dieser Fehler innerhalb einer `for`-Schleife stattfindet und bisher nur bekannt ist, dass 
  ein bestimmter Variablenwert betroffen ist, müssen wir diese Bedingung formulieren.
  Nur so können wir den fehlerhaften Zustand untersuchen.
- [EQ] Wie lautet die Bedingung, an der der Debugger das Programm für uns anhalten soll?
- Setzen Sie einen [TERMREF::Conditional Breakpoint] in der in in [EREFQ::1] mit der in 
  [EREFQ::2] genannten Bedingung und starten Sie den Debugger.
- [EQ] Prüfen Sie den Zustand der Variablen. 
      - Welche Zutat wird in `ingr` gerade abgefragt?
      - Finden Sie diese Zutat in `all_ingredient_locs`? 
        Wenn nein, gibt es eine ähnlich klingende Zutat? Worin liegt der Unterschied?
- Es gibt hier, wie meistens, verschiedene Möglichkeiten den Defekt zu lösen. 
  Wenn Sie sich `ingredients.json`, aus der die Daten von `all_ingredient_locs` kommen, 
  anschauen, stellen Sie fest, dass alle Zutaten ähnlich geschrieben sind und nur die von Ihnen 
  identifizierte Stelle ein Ausreißer darstellt.
- [ER] Beheben Sie den falsch geschriebenen Dateneintrag.
- [EQ] Führen Sie das Programm mit den korrigierten Daten noch einmal aus. 
  Finden Sie noch eine Stelle, in der solch ein Fehler auftritt?
- [EC] Führen Sie das Programm `grocery_list.py` im Terminal aus. 
  Geben Sie die Ausgabe des Programms mit der Eingabe `5` an.

[NOTICE]
Wir haben in diesem Fall ein händisches Testen durchgeführt. 
Das funktioniert, wenn das Programm nicht allzu komplex ist und/oder es nur wenige mögliche 
Eingaben gibt. 
In der Realität möchte man dieses Vorgehen aber mit geeigneten Tests automatisieren.
Mehr dazu lernen Sie in der Aufgabengruppe [PARTREF::Unittests].
[ENDNOTICE]
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

Es gibt mehr als eine Eingabe, in der das Programm einen Fehler wirft.
[ENDINSTRUCTOR]
