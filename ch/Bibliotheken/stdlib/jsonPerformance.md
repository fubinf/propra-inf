title: Performance von JSON-Objekte
stage: alpha
timevalue: 1.0
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
und des Overheads bei der Serialisierung und Deserialisierung an Performance verlieren.
Insbesondere in Anwendungen, die eine hohe Verarbeitungsgeschwindigkeit erfordern,
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

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
