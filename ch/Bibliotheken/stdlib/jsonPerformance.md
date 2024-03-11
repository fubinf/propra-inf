title: Performance von JSON-Objekte
stage: alpha
timevalue: 1.5
difficulty: 2
explains: JSON
assumes: jsonExercise
requires: jsonBasic
---
[SECTION::goal::trial]

- Ich kann JSON-Objekte performant gestalten

[ENDSECTION]
[SECTION::background::default]

JSON bietet nicht nur eine einfache und flexible Möglichkeit, strukturierte Daten
zu speichern und zu übertragen, sondern zeichnet sich auch durch seine Effizienz
und Performance aus. Selbst bei sehr großen Datenmengen bleibt JSON dank seiner
textbasierten Natur leicht lesbar und komprimierbar, was die Speicher- und
Übertragungseffizienz verbessert.
Jedoch kann JSON bei sehr großen Datenmengen aufgrund seiner textbasierten Natur
und des Overheads bei der [TERMREF::Serialisierung] und [TERMREF::Deserialisierung] an Performance
verlieren. Insbesondere in Anwendungen, die eine hohe Verarbeitungsgeschwindigkeit erfordern,
wie beispielsweise bei Echtzeitkommunikation oder Big-Data-Analysen, sollte die
Verwendung von JSON kritisch betrachtet werden. Ein Beispiel dafür, wann JSON langsam
ist, wäre bei der Übertragung oder Verarbeitung von umfangreichen Datenbankabfragen mit
Tausenden von Datensätzen.

[ENDSECTION]
[SECTION::instructions::detailed]

### JSON Performance

Betrachten Sie folgenden Artikel auf [Medium](https://medium.com/data-science-community-srm/json-is-incredibly-slow-heres-what-s-faster-ca35d5aaf9e8)

- [EQ] Welcher entscheidende Nachteil wird hier adressiert und welche Gründe werden genannt?
- [EQ] Welche Tipps werden gegeben, um diesen Nachteil bestmöglich entgegen zu wirken?

### JSON Verschachtelung

In dem folgenden Beispiel ist die Struktur übermäßig komplex und tief verschachtelt. Das erschwert
nicht nur das Lesen und Verstehen des JSON-Codes, sondern kann auch zu Problemen bei der
Verarbeitung und Manipulation der Daten führen.

- [ER] Optimieren Sie die nachfolgende JSON.

```JSON
{
  "universität": {
    "fakultäten": {
      "informatik": {
        "studenten": {
          "student1": {
            "name": "Max Mustermann",
            "alter": 22,
            "kurse": {
              "kurs1": {
                "name": "Programmierung",
                "dozent": "Dr. Müller",
                "credits": 4
              },
              "kurs2": {
                "name": "Datenbanken",
                "dozent": "Prof. Schmidt",
                "credits": 3
              }
            }
          }
        }
      }
    }
  }
}
```

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]
