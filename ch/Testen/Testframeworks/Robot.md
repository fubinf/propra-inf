title: Funktionale Tests mit dem Robot Framework
stage: alpha
timevalue: 1.5
difficulty: 2
profiles: TEST
explains:
assumes:
requires:
---
[SECTION::goal::trial]

Das Ziel dieser Einheit ist es, das Robot Framework zu erkunden, um eine breite Test-Möglichkeit auf dem Gebiet der Testautomatisierung kennenzulernen.

[ENDSECTION]
[SECTION::background::default]

### Was ist das Robot Framework und wie kann ich es nutzen?

Das Robot Framework (RF) ist ein Open-Source-Automatisierungs-Framework für Software-Tests und RPA [TERMREF::RPA], welches in Python entwickelt wurde. 
Es ermöglicht die Erstellung von automatisierten Test- und Automatisierungsprozessen durch den Einsatz von einfach lesbaren, schlüsselwortbasierten [TERMREF::KDT] Testskripten. 
Schlüsselwörter dienen als Aktionen oder Anweisungen, die zusammengefügt werden, um Tests oder Automatisierungsaufgaben zu definieren und auszuführen. 
Das fördert eine leicht verständliche und wartbare Automatisierung.

Um das RF nutzen zu können, ist neben Python das Paket **"robotframework"** zu installieren:

```bash
pip install robotframework
```

Anschließend können automatisierte Prozesse erstellt und ausgeführt werden. Machen Sie sich dazu mit der Erstellung von Testfällen auf der offiziellen RF Seite vertraut.

[RF Seite](https://robotframework.org/#getting-started)

### Kann ich das Robotframework nur zum Testen verwenden?

Obwohl es ursprünglich für Softwaretests entwickelt wurde, hat es sich zu einem vielseitigen Automatisierungsframework entwickelt und kann für verschiedene Arten von Automatisierungsaufgaben
eingesetzt werden. Das Robot Framework kann verwendet werden, um wiederholbare Geschäftsprozesse zu automatisieren, indem es auf die Benutzeroberfläche von Anwendungen zugreift und
Aktionen durchführt. [TERMREF::RPA] Neben der GUI-Testautomatisierung kann das Robot Framework auch für die Automatisierung von API-Tests genutzt werden. Hierbei können HTTP-Anfragen an
APIs getestet und validiert werden. [TERMREF::API] Das Robot Framework kann eingesetzt werden, um Datenmigrationen zu automatisieren und sicherzustellen, dass Daten zwischen verschiedenen
Systemen korrekt übertragen und validiert werden. Weiterhin können automatisiere Tests für Systemfunktionalitäten, Netzwerkkonnektivität und andere infrastrukturelle Aspekte durchgeführt werden. 
Last but not least - und damit auch nicht die letzte Möglichkeit - kann das Robot Framework verwendet werden, um automatisiert Testberichte und Dokumentationen zu generieren, die den aktuellen
Stand und die Ergebnisse der Testläufe zu beschreiben. (Zum Beispiel um Testergebnisse aus einer Pipeline direkt in ein Managementsystem wie Jira zu importieren)


[ENDSECTION]
[SECTION::instructions::loose]

Nutzen Sie den Online Editor auf der Robot Framework Seite, um erste Schritte mit den Testfällen zu machen.

Betrachten Sie das Beispiel **"Simple Example"**:

1. Wieviele und welche Dateien werden für dieses Beispiel verwendet?
2. Wie heißen die Dateien, die nach einer Testausführung entstehen und einsehbar sind?
3. Welche Testfälle beinhaltet das Beispiel?
4. Ergänzen Sie den folgenden Testfall. Ist der Test erfolgreich durchgelaufen?

```python
Administrator login
    Connect to Server
    Login Admin
```

5. Implementieren Sie folgenden Testfall. Welche Fehlermeldung erhalten Sie? Was müsste passieren, um keinen Fehler zu erhalten?

```python
Request Userlist as User
    Connect to Server
    Login User            ironman    1234567890
    Get Userlist
    [Teardown]    Close Server Connection
```

```python
Get Userlist
    Get All Users
```

6. Implementieren Sie einen erfolgreichen Testfall für die Funktion 'get_server_version' aus der CustomLibrary.py. Eine Verifizierung [TERMREF:Verifizierung] des Ergebnisses ist nicht notwenid. 

Wechseln Sie zum Beispiel **"BDD-Example"**

7. Machen Sie sich mit dem Themma [TERMREF:BDD] vertraut. Beschreiben Sie den Aufbau des Testfalls unter 'Calculator_Test_Suite.robot'. 
8. Ergänzen Sie die Zeile **"Then The Result Should Not Be "1""** mit dem folgenden Testfall und erkären Sie, was dieser Testschritt prüft.

```python
The Result Should Not Be "${expected}"
    Log    Checking Result
    Should Not Be Equal As Numbers    ${result}    ${expected}
```

9. Ist es sinnvoll mehrer Schritte in einem Testfall zu nutzen, um Ergebnisse zu verifizieren? Wenn ja, gibt es ein Maximum?


[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
Die bereitgestellten Codeabschnitte können per copy and paste in die Web-Konsole eingefügt und ausgeführt werden. 
Zusätzlich ist es zur Erfüllung der Aufgaben nicht notwendig die CustomLibrary.py zu erweitern.
[ENDHINT]

[ENDSECTION]
[SECTION::submission::reflection]

Zu 5. wird erwartet zu erkennen, dass die Abfrage durch einen unberechtigten Nutzer durchgeführt wird. Ein Administrator jedoch die Möglichkeit hat. 
Daher kann ein fehlerfreier Test durch das ersetzen des Login User durch Login Admin realisiert werden, da diese Funktionalität beriets vorhanden ist.

[ENDSECTION]