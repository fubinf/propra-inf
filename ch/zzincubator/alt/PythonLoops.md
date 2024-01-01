title: Flow Control - Schleifen
stage: draft
timevalue: 0.5
difficulty: 1
assumes: PythonIfThenElse, PythonBooleans
---
Schleifen ermöglichen es bestimmte Arbeitsschritte zu wiederholen, solange bestimmte
Voraussetzungen erfüllt sind. Wenn zur Problemlösung solche Sätze fallen wie _"Solange X
wahr ist..."_ oder _"Für jedes Element aus Y..."_ ist eine Schleife der beste Ansatz.

!!! notice 
    Sehen Sie diese Aufgaben nicht nur als reine Textaufgaben an. Nutzen Sie die Zeit und spiele mit
    dem Gelernten etwas in der [TA2::PythonREPL::REPL] herum! Manchmal lassen sich Fragen auch
    einfacher klären, wenn man sie einfach direkt ausprobiert.

Die einfachste Form der Schleife ist die `while`-Schleife. 
Solange eine Bedingung _wahr_ ist, wird der Schleifenkörper immer wieder ausgeführt.  
Recherchiere in der
[Dokumentation](https://docs.python.org/3.8/reference/compound_stmts.html#the-if-statement) für sich
zu den folgenden Fragen:
  
- Wie sieht die Syntax einer `while`-Schleife aus?
- Mit welchen Befehl kann man die Schleife vorzeitig beenden?
- Mit welchem Befehl kann man wieder an den Anfang der Schleife springen?
- Brainteaser: Sehen Sie sich die folgenden Python-Code an. Die Bedingung für die `while`-Schleife
  wird zu `False`, bevor die Schleife durchgelaufen ist. Wird der `print()` ausgegeben?
       
        ```python
        condition = True
        while(condition):
          condition = False
          print("Wird das hier ausgegeben?")
        ```

Eine andere Form der Schleife ist die `for`-Schleife. Anstatt einen Wahrheitwert als Bedingungung
für die Bearbeitung der Schleife zu verlangen, wird der `for`-Schleife ein `iterable` (z. B. eine
Liste oder ein String) gegeben. Recherchieren Sie in der
[Dokumentation](https://docs.python.org/3.8/tutorial/controlflow.html#for-statements) zu folgenden
Fragen:

- Wie sieht die Syntax einer `for`-Schleife aus?
- Kann eine `for`-Schleife genauso wie die `while`-Schleife vorzeitig beendet werden?
- Was passiert, wenn in einer `for`-Schleife über einen Befehl, wie bei der `while`-Schleife, an
  den Anfang der Schleife gesprungen wird: Wird das selbe Element noch einmal behandelt oder wird
  das nächste Element gewählt?
- Lässt sich jede `for`-Schleife als `while`-Schleife schreiben? 
- Lässt sich jede `while`-Schleife als `for`-Schleife schreiben?
- Was passiert, wenn während der `for`-Schleife ein Element aus dem `iterable` gelöscht wird? Wie
  kann man dieses Problem umgehen?

!!! submission "Abgabeformat"
    Schreiben Sie eine `while`-Schleife, die die Zahlen von 1 bis 10 ausgibt. Es gibt aber zwei
    Sonderfälle: Die Zahl `3` soll übersprungen werden. Weiter soll die Schleife bevor die Zahl 7
    ausgegeben wird abbrechen. Benutzen Sie für die beiden Sonderfälle die oben recherchierten
    Befehle! 

    Schreiben Sie nun die gleiche Schleife noch ein zweites mal mit den selben Sonderfällen 
    mithilfe einer `for`-Schleife.

<!-- !!! notice
    Sie können für die Zahlen von 1 bis 10 die Funktion
    [`range()`](https://docs.python.org/3/library/stdtypes.html?highlight=range#ranges) benutzen.
    Das ist vor allem bei `for`-Schleifen hilfreich. -->