title: Übung Testabgrenzungen
description: |
  Qualitätssicherung fängt nicht beim Testen an. Hier setzen wir uns mit anderen Möglichkeiten der Qualitätsoptimierung auseinander.
timevalue: 2.0
difficulty: 1
profiles: TEST
assumes:
requires:
---
[SECTION::goal::trial]

Das Ziel dieser Einheit ist es, die Abgrenzungen des Testens zum Debuggen und zur Qualitätssicherung (QS) in der Praxis zu verstehen.

[ENDSECTION]
[SECTION::background::default]

Testen, Debuggen und Qualitätssicherung (QS), Recherchieren Sie hierzu anhand der folgenden Leitfragen.

[ENDSECTION]
[SECTION::instructions::detailed]

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

  ```Python
  numbers = [1, 2, 3, 4, 5]

  for i in range(5):
      print(numbers[i])

  ```

3. Betrachten Sie folgendes Szenario: In einem agilen Projekt mit 2 Testern wird nach einem QS Audit festgestellt, dass 20% aller Testfälle nahezu identisch sind. Die Tester haben gem- dem Testkonzept gearbeitet. Dieser sieht vor, dass jeder Tester seine Testfälle selber schreibt und ausführt. Eine Zusammenarbeit unter den testern wurde hier nicht festgelegt. Erwarbeiten Sie ein Konzept zur Verbesserung dieser erkannten Problematik durch mindestens 2 Prozessen. Beschreiben Sie, wie dadurch die Zusammenarbeit verbessert wird und warum doppelte Testfälle stark minimiert werden können.
4. Betrachten Sie folgenden alten Testfall für eine Webseite in deutscher Sprache. Aktualisieren Sie diesen Testfall wenn nötig:
   **Titel:** Erfolgreiche Anmeldung

   **Beschreibung:** Der registrierte Nutzer hat die Möglichkeit sich mit seinem Benutzernamen oder seiner E-Mail Adresse am Portal anzumelden. Der Nutzer wird bei erfolgreicher Anmeldung auf sein Profil weitergeleitet.

   **Testfall-ID:** 1

   **Voraussetzung:** Der Nutzer ist im System regsitriert und aktiv. Der Nutzer befindet sich auf der Anmeldeseite des Portals.

   **Schritte:**

    1. Der Nutzer gibt seinen korrekten Anmeldenamen *benutzer1* und seine korrekte Emailadresse *benutzer1@portal.de* in die Benutzer-Anmeldemakse ein. **Erwartetest Ergebnis:** Der Anmeldename und die Emailadresse *benutzer1benutzer1@portal.de* werden im Klartext angezeigt.
    2. Der Nutzer gibt sein korrektes Passwort *pwd_benutzer1* in die Passwort-Anmeldemakse ein. **Erwartetest Ergebnis:** Das Passwort wird im Klartext angezeigt.
    3. Der Nutzer klickt auf Login. **Erwartetes Ergebnis:** Der Nutzer wird auf die Startseite des Portals weitergeleitet.

[WARNING]
[ENDWARNING]

[HINT::VisibleTitle]
[ENDHINT]

[ENDSECTION]
[SECTION::submission::reflection]

Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
Halten Sie die Antworten kurz.
Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
Geben Sie die benutzten Quellen an.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]