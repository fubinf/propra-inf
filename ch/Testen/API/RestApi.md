title: Rest API Test mit Python Request
stage: alpha
timevalue: 1.0
difficulty: 2
assumes: pip, m_requests
---
[SECTION::goal::trial]

- Ich habe gelernt, was eine API-Schnittstelle ist
- Ich kenne die Eigenschaften einer RESTful-API
- Ich habe mit Python erste API-Schnittstellentests durchgeführt

[ENDSECTION]
[SECTION::background::default]

[TERMREF::API]s erleichtern die Integration von Funktionen einer Software in eine andere und ermöglichen
so die Entwicklung von Anwendungen, die auf bereits vorhandenen Diensten oder Plattformen aufbauen.
So können Sie zu jeder freigegebenen Schnittstelle eigene Funktionalitäten, Programme oder Anwendungen
entwickeln, die mit diesen Schnittstellen kommunizieren.
Eine RESTful-API baut auf den Prinzipien des REST-Architekturstils auf und ermöglicht die Kommunikation
zwischen Client und Server über **standardisierte** HTTP-Anfragen.
Durch die Nutzung dieser standardisierten HTTP-Methoden bietet eine RESTful-API eine flexible und
effiziente Möglichkeit, Daten zwischen verschiedenen Anwendungen auszutauschen.

[ENDSECTION]
[SECTION::instructions::loose]

### API - Was ist das?
<!-- time estimate: 10 min -->

Es gibt verschiedene Arten von APIs, darunter Web-APIs, Bibliotheks-APIs und Betriebssystem-APIs.
Web-APIs sind besonders verbreitet und ermöglichen die Kommunikation zwischen verschiedenen Anwendungen
über das Internet.
Sie basieren oft auf standardisierten Protokollen wie [TERMREF::HTTP] und können verschiedene
Datenformate wie [TERMREF::JSON] oder [TERMREF::XML] verwenden.

Eine API stellt normalerweise eine Sammlung von definierten Schnittstellen und Funktionen bereit,
die von Entwicklern genutzt werden können, um auf bestimmte Dienste oder Ressourcen zuzugreifen.
Eine solche Sammlung kann u.a. mit Hilfe von [TERMREF::OpenAPI] dokumentiert werden.
Diese Dokumentationshilfe wird uns in diesem Kapitel dabei helfen, Schnittstellen anzusprechen und zu testen.

- [EQ] Werfen Sie einen Blick in die
  [Petstore-Dokumentation](https://petstore.swagger.io).
  Welche HTTP-Methoden finden Sie dort wieder?

### RESTful-API
<!-- time estimate: 15 min -->

Eine RESTful-API hat besondere Eigenschaften, die wir uns hier genauer anschauen.
Recherchieren Sie auf der [RESTful-API-Seite](https://restfulapi.net):

- [EQ] Was zeichnet eine RESTful-API-Architektur aus?
- [EQ] Wie sieht ein REST-Endpunkt aus?
  Werden Ressourcen-Endpunkte in Singular oder Plural bezeichnet?
- [EQ] Worin unterscheiden sich `PUT` und `POST`?
  Erstellen Sie jeweils ein Beispiel, um den Unterschied zu verdeutlichen.
- [EQ] Sind REST und HTTP gleichzusetzen?

### Python requests
<!-- time estimate: 5 min -->

Das `requests`-Modul haben Sie bereits in [PARTREF::m_requests] kennengelernt.
Dort finden Sie auch die Dokumentation zu den verwendeten Funktionen.

- [EQ] Kann ich einen `POST`-Request direkt über einen Webbrowser absetzen?
  Warum brauche ich dafür ein Script?

Falls Sie das Paket noch nicht installiert haben, holen Sie das nach: `pip install requests`

### Petstore kennenlernen
<!-- time estimate: 5 min -->

Für die kommenden Aufgaben verwenden wir die freie API Petstore.
Sie steht uns unter
[petstore.swagger.io](https://petstore.swagger.io)
zur Verfügung.
Machen Sie sich mit der Navigation und der Beschreibung des Petstores vertraut.

- [EQ] Welche Ressourcen-Kategorien (z.B. `/pet`, `/store`, `/user`) bietet der Petstore an,
  und welche HTTP-Methoden sind jeweils verfügbar?

### Petstore-Schnittstellen verwenden
<!-- time estimate: 25 min -->

Nachdem Sie einen Blick in die Petstore-Dokumentation geworfen haben, sind Ihnen bestimmt auch
verschiedene Schnittstellen aufgefallen. Diese nutzen wir jetzt, um Informationen zu erhalten.

- [ER] Ersetzen Sie im folgenden Script die TODOs durch erklärende Kommentare,
  die beschreiben, was die jeweilige Zeile bzw. der jeweilige Block tut:

```python
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

- [EC] Führen Sie das annotierte Script aus.

- [ER] Im folgenden POST-Request ist ein Fehler unterlaufen. Korrigieren Sie ihn:

```python
import requests

def create_pet():
    api_url = "https://petstore.swagger.io/v2/pet"

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
        response = requests.post(api_url, data=pet_data)

        if response.status_code == 200:
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

- [EC] Führen Sie das korrigierte Script aus und beschreiben Sie die JSON-Rückgabe im Protokoll.

- [ER] Vervollständigen Sie die folgenden Script-Gerüste für ein `PUT`- und ein `DELETE`-Request.
  Verwenden Sie eine der IDs, die beim vorherigen GET-Request zurückgegeben wurden.

```python
import requests

def update_pet(pet_id):
    url = "https://petstore.swagger.io/v2/pet"
    pet_data = {
        "id": pet_id,
        # TODO: Ergänzen Sie weitere Felder analog zum POST-Request (name, status, ...)
    }
    # TODO: Senden Sie einen PUT-Request mit json=pet_data
    # TODO: Geben Sie Statuscode und Response aus

def delete_pet(pet_id):
    # TODO: Bauen Sie die URL mit der pet_id zusammen: .../pet/{pet_id}
    # TODO: Senden Sie einen DELETE-Request
    # TODO: Geben Sie den Statuscode aus

if __name__ == "__main__":
    pet_id = 0  # TODO: Ersetzen Sie 0 durch eine gültige ID aus dem GET-Request
    update_pet(pet_id)
    delete_pet(pet_id)
```

[HINT::Welche Petstore-Endpunkte sind gemeint?]
Für das Update: `PUT /pet` — der vollständige Pet-Datensatz wird als JSON-Body mitgegeben
(analog zum POST-Request, nur mit `requests.put()`).
Für das Löschen: `DELETE /pet/{petId}` — die ID gehört in die URL, nicht in den Body
(`requests.delete(url)`).
Die Petstore-Dokumentation ermöglicht auch direkt Testanfragen über die Oberfläche —
das ist nützlich, um Ihre Scripts mit der erwarteten API-Antwort zu vergleichen.
[ENDHINT]

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]
[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
