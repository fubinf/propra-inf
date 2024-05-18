title: Testabgrenzung zum Debugging
stage: alpha
timevalue: 1
difficulty: 3
assumes: Python1, Debuggingtools
---

[SECTION::goal::trial]

- Ich kann die Abgrenzungen des Testens zum Debuggen und zur [TERMREF::Qualitätssicherung] (QS)
  benennen und anwenden

[ENDSECTION]

[SECTION::background::default]

Testen und Debuggen gehören zur Qualitätssicherung, haben jedoch unterschiedliche Ziele und
Herangehensweisen, die wichtig sind zu verstehen, wenn man sie genau einordnen möchte.

[ENDSECTION]

[SECTION::instructions::detailed]

### Was ist .. ?

Recherchieren Sie selbstständig anhand der folgenden Leitfragen (falls notwendig):

- [EQ] Was versteht man unter Software-Testing?
- [EQ] Was versteht man unter Debugging?
- [EQ] Was versteht man unter QS?
- [EQ] Was ist der Unterschied zwischen der QS und dem Testen?

#### Reflektion

- [EQ] Sollten Tester jeden [TERMREF::Defekt] debuggen können?
- [EQ] Warum übernehmen Entwickler nicht auch die Rolle des Softwaretesten?

### Ein klein wenig Debugging

- [EQ] Debuggen Sie folgenden Python Code:
Geben Sie den/die gefundenen Fehler zusammengefasst wieder und beschreiben Sie Ihre Anpassung(en).

```Python
def add_numbers():
  num1 = input("Geben Sie die erste Zahl ein: ")
  num2 = input("Geben Sie die zweite Zahl ein: ")
  
  result = num1 + num2
  
  print("Das Ergebnis der Addition ist:", result)

add_numbers()
```

- [EQ] Debuggen Sie folgenden Python Code:
Geben Sie den/die gefundenen Fehler zusammengefasst wieder und beschreiben Sie Ihre Anpassung(en).

```Python
numbers = [0, 1, 2, 3, 4, 5]

for i in range(5):
    print(numbers[i])

```

*Betrachten Sie folgendes Szenario:*
In einem agilen Projekt mit 2 Testern wird nach einem QS Audit festgestellt, dass 20% aller
Testfälle nahezu identisch sind. Die Tester haben gemäß dem Testkonzept gearbeitet. Dieser sieht
vor, dass jeder Tester seine Testfälle selber schreibt und ausführt. Eine Zusammenarbeit unter den
Testern wurde hier nicht festgelegt.

- [EQ] Erarbeiten Sie ein Konzept zur Verbesserung dieser erkannten Problematik durch mindestens 2
  Prozessen. Beschreiben Sie, wie dadurch die Zusammenarbeit verbessert wird und warum doppelte
  Testfälle stark minimiert werden können.

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

- [EREFQ::1]: Prozess der Bewertung und Überprüfung, ob ein Softwareprodukt oder eine Anwendung das
  tut, was sie tun soll
- [EREFQ::2]: Ein Vorgang, Fehler oder unerwartetes Verhalten zu diagnostizieren und zu beheben.
- [EREFQ::3]: Sammelbegriff für unterschiedliche Ansätze und Maßnahmen zur Sicherstellung festgelegter Qualitätsanforderungen
- [EREFQ::4]: Testen ist mehr auf das Produkt ausgerichtet, während die Qualitätssicherung mehr auf
  den Prozess der Qualitätssicherung des Produkts ausgerichtet ist
- [EREFQ::5]: Tester sollten in der Lage sein, Defekte zu identifizieren und zu dokumentieren, aber
  es ist nicht zwingend notwendig, dass sie jeden Defekt debuggen können, da dies oft die Aufgabe der
  Entwickler ist.
- [EREFQ::6]: Entwickler übernehmen oft nicht die Rolle des Softwaretestens, da sie in der Regel sehr
  detailliert in dem ganz konkreten Funktionsaufbau stecken und dadurch 'blind' werden für Randtests
  und möglichen Problemen
- [EREFQ::7]: Eingabewerte sind vom Datentyp String und werden mit '+' kaskadiert und nicht addiert
- [EREFQ::8]: Array hat 6 Elemente, range(5) gibt nur die ersten 5 Elemente zurück
- [EREFQ::9]: Einführung eines Testfall-Review-Prozesses, bei dem jeder Tester die Testfälle des
  anderen überprüft; Testfall-Pair-Programming: gemeinsam ZTestfälle ertellen; Testfall-Refactopring:
  Gemeinsames Überabriten vorhandener Testfälle
  => fördert die Zusammenarbeit, findet schneller doppelte Testfälle, erhöht die Qualität zukünftiger
  Testfälle im Projekt

[ENDINSTRUCTOR]
