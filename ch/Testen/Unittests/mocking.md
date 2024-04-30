title: Mocking in pytest
stage: beta
timevalue: 2.0
difficulty: 3
assumes: m_pytest, pytest102
---

[SECTION::goal::idea]

- Ich kann beschreiben, was "Mocks" sind und wie sie in pytest Anwendung finden.
- Ich kann "Mocks" von anderen Testmethoden abgrenzen.
- Ich kann begründen, wann die Anwendung von "Mocks" sinnvoll ist.

[ENDSECTION]
[SECTION::background::default]

Wenn Sie vor der Herausforderung stehen, Unittests für Code zu schreiben, der auf Datenbankzugriffe,
Nutzerverwaltung und externe [TERMREF::API]-Aufrufe angewiesen ist, aber keine echte Netzwerkverbindung oder
andere Ressourcen zur Verfügung haben, können Mocking-Techniken Ihnen dabei helfen, diese
Abhängigkeiten unter realen Bedingungen zu simulieren.

[ENDSECTION]
[SECTION::instructions::loose]

In dieser Aufgabe werden wir uns mit dem Konzept des "Code Mocking" und der Verwendung von pytest
als Testframework auseinandersetzen.

Recherchieren Sie hierzu anhand der folgenden Leitfragen.

- [EQ] Was versteht man genau unter dem Begriff "Code Mocking"?
- [EQ] Welches Problem versucht Code Mocking zu lösen?
- [EQ] Welchen Unterschied gibt es zwischen Mocking und Fixtures und
wie ergänzen sie sich gegenseitig?
- [EQ] Wie werden Mock-Objekte zur Nutzung in pytest erstellt?
- [EQ] In welchen Situationen sollten wir Mocks verwenden, und wann sollten wir auf echte
   Implementierungen zugreifen?
- [EQ] Können Sie sich vorstellen alle Ihre Testfälle zu mocken, oder gar keine Mocks einzusetzen?

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[ENDSECTION]
