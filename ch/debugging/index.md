---
Egal ob Sie bereits Programmiererfahrung haben oder bisher nur im Studium mit Computerprogrammen 
zu tun hatten: Sie werden Code produziert haben, der zumindest im ersten Versuch nicht das tat, 
was er tun sollte.
Allerdings ist dieser Gedanke auf mehrfache weise schwer so zu halten, denn Code ist eine 
Produktspezialisierung, die umfassend und präzise genug ist, um ein Programm zu erstellen.
Mit anderen Worten macht Ihr Code immer exakt das, was Sie ihm aufgetragen haben.

In diesem Kapitel geht es darum, zu lernen, wie man mit solchen Phänomenen umgeht. 
Da verschiedene Quellen aber bestimmte Sachverhalte unterschiedlich benennen, führen wir zunächst
eine Begriffsklärung durch:

- Ein **Versagen (engl. _failure_)** ist das falsche Verhalten des Programms bezogen zur 
  Spezifikation, 
  der Anforderung oder den Erwartungen.
  Da es genau dieses Phänomen ist, welches man bei einer Programmausführung bemerkt und zumeist 
  nicht direkt auf die Ursache schließen kann, wird es in einigen Quellen auch 
  **Symptom (engl. _symptom_)** genannt. 
- Ein **Defekt (engl. _defect, fault_)** verursacht ein Versagen.
  Häufig wird das Wort **Bug** synonym benutzt.
  Dies ist eine strukturelle Eigenschaft des Codes und kann damit auch nur in diesem behoben werden.
- Ein **Fehler (engl. _error_)** führt zum Defekt. 
  Es liegt ein falsches Verhalten (engl. _commission_) oder ein Versäumnis (engl. _omission_) vor.
  Damit entsteht ein Fehler immer während der Entwicklung, entweder im Code, bei den 
  Anforderungen oder beim Entwurf.

Wenn Sie bereits Berührungspunkte mit der Vorlesung "Softwaretechnik" haben, kommt Ihnen diese 
Terminologie vielleicht schon bekannt vor.
Während es in der Vorlesung um eine etwas abstraktere Herangehensweise an dieses Thema geht, 
wollen wir hier lernen, welches mentale Modell hinter den Techniken des Debuggings steckt und 
welche Techniken benutzt werden können.
Dieses Thema geht Hand in Hand mit dem Thema Testen, denn während man beim Testen das Versagen 
eines Programms aufdeckt, ist das Debugging der Prozess zur Lösung dieser Probleme.
