title: Flow Control - Bedingte Ausführung
timevalue: 0.25
difficulty: 1
assumes: PythonBooleans
---
Mithilfe der Auswertung von Booleans können sogenannte `if`/`then`/`else`-Ausdrücke benutzt werden
um zusteuern, ob Teile von Code ausgeführt werden sollen, wenn bestimmte Bedingungen erfüllt sind.

!!! notice 
    Sehen Sie diese Aufgaben nicht nur als reine Textaufgaben an. Nutzen Sie die Zeit und spiele mit
    dem Gelernten etwas in der [TA2::PythonREPL::REPL] herum! Manchmal lassen sich Fragen auch
    einfacher klären, wenn man sie einfach direkt ausprobiert.

Recherchiere in der Dokumentation 
[hier](https://docs.python.org/3.8/reference/compound_stmts.html#the-if-statement) und
[hier](https://docs.python.org/3.8/tutorial/controlflow.html#if-statements) zu den
folgenden Fragen:

  -  Wie sieht die Syntax eines `if`/`then`/`else`-Ausdruckes aus? 
  -  Lassen sich mehrere `if`/`then`/`else`-Ausdrücke verschachteln? Wenn ja, wie sieht die Syntax
     aus?
  -  Welche Teile eines `if`/`then`/`else`-Ausdruckes sind optional?

!!! submission
    Schreibe ein kleines Rate-Spiel in Python. 

    Das Programm fragt den Nutzer `Ist das ein Vogel?`. Wenn der Nutzer `ja` eintippt, gibt das 
    Programm `Das ist aber ein großer Vogel!` zurück.

    Sollte der Nutzer aber `nein` eintippen, stellt das Programm die nächste Frage `Ist es ein
    Flugzeug?`. Wenn der Nutzer `ja` eintippt, gibt das Programm `Das Flugzeug fliegt ziemlich
    schnell!` zurück. 

    Sollte der Nutzer aber `nein` eintippen, gibt das Programm `Es ist Superman!` zurück.

    Beschreibe was passiert, wenn der Nutzer nicht `ja` oder `nein` eintippt und schreib es in
    einen Kommentar in das Programm.

!!! notice
    Du kannst den Input eines Nutzers über die Funktion `input()` abfragen. Speichere den Input in
    einer Variable, damit du ihn z. B. in einer `if`-Abfrage benutzen kannst!