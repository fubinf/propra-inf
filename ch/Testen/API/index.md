title: API Tests
stage: alpha
---
Moderne Software besteht aus vielen unabhängigen Komponenten, die über [TERMREF::API]s miteinander
kommunizieren.
Weit verbreitet sind dabei [TERMREF2::REST-API::-s]: Sie nutzen standardisierte HTTP-Methoden
und liefern Antworten typischerweise im [TERMREF::JSON]-Format —
das macht sie gut testbar und ideal für den Einstieg ins automatisierte Testen.

In dieser Taskgroup lernen Sie, REST-APIs mit Python zu testen:
zuerst Grundlagen und erste Requests, dann das Verarbeiten von Antwortdaten,
und schließlich einen vollständigen Testdurchlauf nach dem CRUD-Prinzip.
