title: Testabgrenzungen
description: >
  Qualitätssciherung fängt nicht beim Testen an. Hier setzen wir uns mit anderen Möglichkeiten der Qualitätsoptimierung auseinander.
timevalue: 2
difficulty: 1
---

!!! goal
  Ziel dieser Einheit ist es sich mit den Abgrenzungen des Testens zum Debuggen und zur Qualitätssicherung (QS) (eng.: Quality Assurance (QA)) zu beschäftigen.

Testen, Debuggen und Qualitätssicherung (QS), Recherchieren Sie hierzu anhand der folgenden Leitfragen.
Geben Sie die benutzten Quellen an.

1. Debuggen Sie folgenden Python Code:
Geben Sie die gefundenen Fehlermeldungen zusammengefasst wieder und beschreiben Sie Ihre Anpassung(en).

```Python
def add_numbers():
    num1 = input("Geben Sie die erste Zahl ein: ")
    num2 = input("Geben Sie die zweite Zahl ein: ")
    
    result = num1 + num2
    
    print("Das Ergebnis der Addition ist:", result)

add_numbers()
```

2. Debuggen Sie folgenden Java Code:
Geben Sie die gefundenen Fehlermeldungen zusammengefasst wieder und beschreiben Sie Ihre Anpassung(en).

```Java
public class ArrayOutput {
    public static void main(String[] args) {
        int[] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;
        numbers[3] = 4;
        numbers[4] = 5;
        
        for (int i = 0; i <= 5; i++) {
            System.out.println(numbers[i]);
        }
    }
}
```

!!! submission
  Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
  Halten Sie die Antworten kurz.
  Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
