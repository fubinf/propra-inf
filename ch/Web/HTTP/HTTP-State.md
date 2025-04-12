title: Zustand in HTTP
stage: draft
timevalue: 0
difficulty: 2
assumes: http-Response
---
[SECTION::goal::trial]

Ich verstehe, was es bedeutet, dass HTTP zustandslos ist und wie ich damit umgehen muss.

[ENDSECTION]
[SECTION::background::default]

Sie sollten durch die vorangegangen Aufgaben ein Verständnis dafür gewonnen haben, dass HTTP
im Kern immer einzelne Dateien anfragt und die Verbindung danach abschließt.

Eine Konsequenz daraus ist, dass beispielsweise beim Klick auf einen Link kein Bezug mehr zu
Ihrem Login auf die Webseite existiert. Für die Gegenstelle ist rein aufgrund der Anfrage
nicht ersichtlich, ob und als wer Sie eingeloggt sind.

[ENDSECTION]
[SECTION::instructions::detailed]

[EQ] Ein einfacher Weg, um dem Server Kontext darüber zu geben, wer Sie sind, ist die Verwendung
von Cookies. Wie funktioniert ein Cookie auf Ebene von HTTP? Erklären Sie entsprechende Aspekte
im Response und im Request.

[EQ] Es ist grundsätzlich möglich, im Cookie den Benutzernamen und das Passwort zu speichern, um
sich zu authentifizieren. Das ist zwar in Zeiten von HTTPS nicht mehr so problematisch wie bei
reinem HTTP, aber dennoch keine besonders gute Idee. Fällt Ihnen eine Möglichkeit ein, das ohne
diese Informationen zu ermöglichen?

Falls Ihnen keine Möglichkeit einfällt, erläutern Sie kurz eine nicht funktionierende Idee und
weshalb diese nicht funktionieren würde.

[HINT::vorhandene Verfahren]
Das Stichwort hierzu ist "Session". Es gibt Informationen zu "HTTP Sessions", die häufig nicht dem
entsprechen, was hier helfen würde. Besser ist, im Kontext einer Programmiersprache zu recherchieren.
Die Programmiersprache PHP beispielsweise liefert Unterstützung dafür in der Standardbibliothek.

Auch die explizite Spezifizierung davon, dass es sich um eine "Server-side Session" handelt, ist
zur Recherche sinnvoll.
[ENDHINT]

[ENDSECTION]
[SECTION::submission::information]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
