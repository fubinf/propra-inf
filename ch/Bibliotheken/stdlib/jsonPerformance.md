title: Performance von JSON-Objekte
stage: alpha
timevalue: 1.0
difficulty: 2
explains: JSON
assumes: jsonExercise
requires: jsonBasic
---

TODO_1_ruhe

1)
Definition von Serialisierung und Deserialisierung fehlt.

2)
In der abzugebenden Aufgabe könnte man noch ineffiziente JSON-Objekte geben, sodass der Student diese Objekte anhand der Empfehlungen (mindestens die Punkte von 1 bis 4) aus dem Medium-Artikel/"Optimizing JSON Performance" effizienter macht. 

3)
In der abzugebenden Aufgabe könnte man auch nach den anderen erwähnten Serialisierungsformaten fragen und eventuell auch danach, warum JSON trotz aller Vorteile der anderen Formate immer noch beliebt und weit verbreitet ist, nur zur Sicherung, dass der Student die Eigenschaften von JSON gut verstanden hat. 

4)
Die geschätzte Bearbeitungszeit ist ein bisschen wenig, wenn man in Betrachtung nimmt, dass der Student den Medium-Artikel inkl. Abgabe ausführlich bearbeiten würde. Vielleicht 1.5 h ?

-----------------

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
