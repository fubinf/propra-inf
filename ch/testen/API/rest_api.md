title: Rest API Test mit Python Request
stage: alpha TODO_1 Durchsicht und Ergänzung
timevalue: 2.0
difficulty: 2
profiles: TEST
explains:
assumes:
requires:
---
[SECTION::goal::trial]

Das Ziel dieser Einheit ist es, den Begriff des API zu verstehen, Python requests zu verwenden und API Tests durchzuführen, damit ich ein Gespür dafür bekommen, wie man APIs testet.

[ENDSECTION]
[SECTION::background::default]

### API - Was ist das?
[TERMREF::API]s erleichtern die Integration von Funktionen einer Software in eine andere und ermöglichen so die Entwicklung von Anwendungen, die auf bereits vorhandenen Diensten oder Plattformen aufbauen.

Es gibt verschiedene Arten von APIs, darunter Web APIs, Bibliotheks-APIs und Betriebssystem-APIs. Web APIs sind besonders verbreitet und ermöglichen die Kommunikation zwischen verschiedenen Anwendungen über das Internet. Sie basieren oft auf standardisierten Protokollen wie [TERMREF::HTTP] und können verschiedene Datenformate wie [TERMREF:JSON] oder [TERMREF::XML] verwenden.

Eine API stellt normalerweise eine Sammlung von definierten Schnittstellen und Funktionen bereit, die von Entwicklern genutzt werden können, um auf bestimmte Dienste oder Ressourcen zuzugreifen. Eine solche Sammlung kann u.a. mit Hilfe
von [TERMREF:OpenAPI] dokumentiert werden. Diese Dokumentationshilfe wird uns in diesem Kapitel dabei helfen, Schnittstellen anzusprechen und zu testen. 

### Python Request - Wofür benötige ich das?

Das requests-Modul ist eine externe Bibliothek für Python, die die Arbeit mit HTTP-Anfragen vereinfacht. Es bietet eine einfach zu bedienende API für das Senden von HTTP-Anfragen und das Verarbeiten von HTTP-Antworten.

Um die Petstore-Schnittstellen abzufragen, verwenden Sie das requests-Modul in Python. Wenn Sie es noch nicht installiert haben. Sie können es mit dem Befehl ***pip install requests*** installieren.

[ENDSECTION]
[SECTION::instructions::loose]

### Petstore kennenlernen

Für die kommenden Aufgaben werden wir die freie API Petstore verwenden, die uns unter [swagger.io](https://petstore.swagger.io) zur Verfügung steht. Machen Sie sich mit der Navigation und der Beschreibung des Petstores vertraut.
Lesen Sie den Artikel [REST Web Services](http://www.thomas-bayer.com/resources/rest/rest_webservices.pdf) und beantworten Sie folgende Fragen:

1. Was versteht man unter REST?
2. Welche HTTP-Methoden werden verwendet? 
3. Kann ich einen POST Request über einen Webbrowser absetzen?

### Petstore-Schnittstellen verwenden

Jetzt widmen wir uns den praktischen Aufgaben zu. nachdem Sie einen Blick in die Petstore-Dokumemntation geworfen haben, sind Ihnen bestimmt auch verschiedene Schnittstellen aufgefallen. Diese nutzen wir jetzt, um Informationen zu erhalten. 

4. Nutzen Sie folgendes Script, um eine API Anfrage zu senden. Kommentieren und beschreiben Sie die fehlenden TODOs:

```Python
# todo 1
import requests

def get_pet_data():
    # todo 2
    api_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

    try:
        # todo 3
        response = requests.get(api_url)

        # todo 4
        if response.status_code == 200:
            # todo 5
            pet_data = response.json()
            print("Available pets:")
            print(pet_data)
        else:
            print(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")
    except Exception as e:
        print(f"Fehler bei der Anfrage: {str(e)}")

if __name__ == "__main__":
    get_pet_data()
```

5. Im folgenden POST Request ist ein Fehler unterlaufen. Korrigieren Sie das Problem und Beschreiben Sie die Rückgabe (JSON Response).

```Python
import requests

def create_pet():
    # URL der API
    api_url = "https://petstore.swagger.io/v2/pet"

    # Beispiel-Daten für den POST-Request (Sie können diese Daten anpassen)
    pet_data = {
        "id": 12345,
        "name": "Fluffy",
        "category": {
            "id": 1,
            "name": "Cats"
        },
        "photoUrls": [
            "https://example.com/fluffy.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "cute"
            }
        ],
        "status": "available"
    }

    try:
        # POST-Anfrage an die API senden
        response = requests.post(api_url, json=pet_data)

        # Überprüfen Sie den Statuscode der Antwort
        if response.status_code == 200:
            # Die Antwort als JSON-Daten analysieren
            created_pet_data = response.json()
            print("Pet erfolgreich erstellt. Neue Daten:")
            print(created_pet_data)
        else:
            print(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")
    except Exception as e:
        print(f"Fehler bei der Anfrage: {str(e)}")

if __name__ == "__main__":
    create_pet()
```

6. Erstellen Sie ein Update und ein Delete Request für eine beliebige existierene Pet-ID (Suchen Sie eigenständig nach einem vorhandenen Eintrag.)


[WARNING]
[ENDWARNING]
[HINT::VisibleTitle]
Die OpenAPI Dokumentaion bietet ebenfalls die Möglichkeit Anfragen zu senden. Dadurch erhalten Sie die Möglichkeiten Ihren Response mit Hilfe Ihrer Scripte mit dem Responser über OpenAPI zu vergleichen.  
[ENDHINT]

[ENDSECTION]
[SECTION::submission::reflection]

Die Abgabe besteht aus einem Markdown-Dokument mit den Antworten zu den oben gestellten Fragen.
Halten Sie die Antworten kurz.
Sie dürfen Code-Beispiele benutzen, wenn diese zur Antwort hilfreich sind.
Sollten Ihnen zur Erstellung der Bug-Reports Informationen Fehlen, dürfen Sie diese fiktiv belegen. Bitte mit (fiktiv) markieren.

[ENDSECTION]