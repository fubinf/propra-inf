title: Rest API Test mit Python Request
stage: beta
timevalue: 2.0
difficulty: 2
assumes: WebAPIs, pip, requests
---
# Review
- Fragen zur Restful API: Finde ich als Lernaufgabe nicht so schön. Beispiel bauen ist super. Vielleicht findest du ja eine Möglichkeit, die anderen Dinge da auch irgendwie einzubauen? Also du lässt z.B. den API-Endpunkt so bauen, dass all die erkannten Grundsätze und Regeln da auch angewandt werden müssen.
- Ähnliches auch für den Teil zum Petstore.

Anmerkung Ruhe: Restful API Anteil wurde auf Grundlage Review 1 (Discord) mit aufgenommen.

[SECTION::goal::trial]

- Ich habe gelernt, was eine API-Schnittstelle ist
- Ich kenne die Eigenschaften einer RESTful-API
- Ich habe mit Python erste API-Schnittstellentests durchgeführt

[ENDSECTION]
[SECTION::background::default]

[TERMREF::API]s erleichtern die Integration von Funktionen einer Software in eine andere und ermöglichen
so die Entwicklung von Anwendungen, die auf bereits vorhandenen Diensten oder Plattformen aufbauen.
So können Sie zu jeder freigegebene Schnittstelle eigene Funktionalitäten, Programme oder Anwendungen
entwickeln, die mit diesen Schnittstellen kommunizieren.
Eine RESTful API baut auf den Prinzipien des REST-Architekturstils auf und ermöglicht die Kommunikation
zwischen Client und Server über **standardisierte** HTTP-Anfragen. Durch die Nutzung diese standardisierten
HTTP-Methoden bietet eine RESTful API eine flexible und effiziente Möglichkeit, Daten zwischen verschiedenen
Anwendungen auszutauschen.

[ENDSECTION]
[SECTION::instructions::loose]

### API - Was ist das?

Es gibt verschiedene Arten von APIs, darunter Web APIs, Bibliotheks-APIs und Betriebssystem-APIs.
Web APIs sind besonders verbreitet und ermöglichen die Kommunikation zwischen verschiedenen Anwendungen
über das Internet.
Sie basieren oft auf standardisierten Protokollen wie [TERMREF::HTTP] und können verschiedene
Datenformate wie [TERMREF::JSON] oder [TERMREF::XML] verwenden.

Eine API stellt normalerweise eine Sammlung von definierten Schnittstellen und Funktionen bereit,
die von Entwicklern genutzt werden können, um auf bestimmte Dienste oder Ressourcen zuzugreifen.
Eine solche Sammlung kann u.a. mit Hilfe
von [TERMREF::OpenAPI] dokumentiert werden. Diese Dokumentationshilfe wird uns in diesem Kapitel
dabei helfen, Schnittstellen anzusprechen und zu testen.

- [EQ] Werfen Sie einen Blick in ein beliebiges OpenAPI Projekt. Welche HTTP-Methoden finden Sie
  dort wieder?

### RESTful-API

Eine RESTful-API hat besondere Eigenschaften, die wir uns hier genauer anschauen. Recherchieren Sie
auf der [RESTful-API-Seite](https://restfulapi.net):

- [EQ] Was zeichnet eine RESTful-API Architektur aus?
- [EQ] Was sind die 6 grundlegenden Prinzipien?
- [EQ] Wie sieht ein REST-Endpunkt aus und werden Ressourcen-Endpunkte in Singular oder Plural bezeichnet?
- [EQ] Worin unterscheiden sich `PUT` und `POST`? Erstellen Sie jeweils ein Beispiel, um den
  Unterschied zu verdeutlichen.
- [EQ] Sind REST udn HTTP gleichzusetzen?

### Python Request - Wofür benötige ich das?

Das requests-Modul ist eine externe Bibliothek für Python, die die Arbeit mit HTTP-Anfragen vereinfacht.
Es bietet eine einfach zu bedienende API für das Senden von HTTP-Anfragen und das Verarbeiten von HTTP-Antworten.
Um die Petstore-Schnittstellen abzufragen, verwenden Sie das requests-Modul in Python.

- [EC] Wenn Sie das Paket noch nicht installiert haben, können Sie es mit folgendem Befehl
  `pip install requests` nachholen.

### Petstore kennenlernen

Für die kommenden Aufgaben werden wir die freie API Petstore verwenden, die uns unter [swagger.io](https://petstore.swagger.io) zur Verfügung steht. Machen Sie sich mit der Navigation und der Beschreibung des Petstores vertraut.
Lesen Sie den Artikel [REST Web Services](http://www.thomas-bayer.com/resources/rest/rest_webservices.pdf)
und beantworten Sie folgende Fragen:

- [EQ] Was versteht man unter REST?
- [EQ] Kann ich einen POST Request über einen Webbrowser absetzen?

### Petstore-Schnittstellen verwenden

Jetzt widmen wir uns den praktischen Aufgaben zu. nachdem Sie einen Blick in die Petstore-Dokumentation
geworfen haben, sind Ihnen bestimmt auch verschiedene Schnittstellen aufgefallen. Diese nutzen wir jetzt,
um Informationen zu erhalten.

- [EC] Nutzen Sie folgendes Script, um eine API Anfrage zu senden. Kommentieren und beschreiben Sie die
  enthaltenen TODOs:

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

- [EC] Im folgenden POST Request ist ein Fehler unterlaufen. Korrigieren Sie das Problem und Beschreiben
  Sie die Rückgabe (JSON Response).

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

- [ER] Erstellen Sie ein Update und ein Delete Request für eine beliebige existierende Pet-ID
  (Suchen Sie eigenständig nach einem vorhandenen Eintrag.)

[HINT::VisibleTitle]
Die OpenAPI Dokumentation bietet ebenfalls die Möglichkeit Anfragen zu senden. Dadurch erhalten Sie die
Möglichkeiten Ihren Response mit Hilfe Ihrer Scripte mit dem Response über OpenAPI zu vergleichen.  
[ENDHINT]

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]

[INSTRUCTOR::Pet-ID]

- [EREFR::1] Die gefundene Pet-Id kann von Fall zu Fall unterschiedlich sein, aber auch nicht mehr
  existieren, da diese Schnittstelle jedermann zugänglich ist und somit ständig unter Anwendung steht.

[ENDINSTRUCTOR]
