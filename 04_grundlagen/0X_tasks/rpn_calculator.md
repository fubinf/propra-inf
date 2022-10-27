id: rpn_calculator
title: RPN-Taschenrechner
hint: Ein Stack ist hier sehr nützlich.

RPN (Reverse Polish Notation) ist eine Suffix-Notation von arithmetischen Ausdrücken.
Im Gegensatz zu der bei uns geläufigen Infix-Notation werden die Operatoren hier hinter den Operanden geschrieben statt dazwischen.

Beispielsweise ist der Ausdruck `(1+2)*(3+4)` in RPN `1 2 + 3 4 + *`.
Es wird also erst `1+2` ausgerechnet, anschließend (3+4) und beide Ergebnisse multipliziert.

Entwickeln Sie einen RPN-Taschenrechner. Konzeptbedingt sind Klammern nicht notwendig. Sie dürfen frei entscheiden, ob die Division ganzzahlig sein soll oder nicht.

Es steht Ihnen auch frei, davon auszugehen, dass alle Eingabezahlen einstellig sind, also `10` für die Zahlen Eins und Null stehen, nicht für die Zahl Zehn. In diesem Fall dürfen Sie auch davon ausgehen, dass die Eingabe keine Leerzeichen enthält.

Falls Sie eine größere Herausforderung wollen, implementieren Sie die Evaluation mit einer Reduktion.
