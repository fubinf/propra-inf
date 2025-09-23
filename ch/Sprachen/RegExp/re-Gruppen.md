title: "Gruppen"
stage: draft
timevalue: 1.0
difficulty: 2
assumes: re-Quantoren
---

[SECTION::goal::idea]
Ich verstehe, wie man eigene Zeichenklassen schreiben kann und wie ich
Gruppen benutzen kann.
[ENDSECTION]


[SECTION::background::default]
Um das volle Potenzial von regulären Ausdrücken nutzen zu können, sind Gruppen wichtig zu verstehen.
[ENDSECTION]


[SECTION::instructions::loose]
Quantoren eignene sich nicht nur gut, um einzelne Zeichen eine bestimmte
Anzahl an Malen zu wiederholen.
Sie können damit auch *Gruppen an Zeichen wiederholen*.
Diese Gruppen können Sie in Klammern `()` festlegen.
Letztendlich enthalten die Klammern nur einen weiteren regulären Ausdruck,
das praktische ist jedoch, dass Sie diese z.B. nutzen können, um Sie mit Quantoren zu wiederholen:
`(HA)+` sucht nach Zeichenketten, die `HA` mindestens 1-mal wiederholt.

[EQ] Treffen Sie "Banana" mit mindestens zwei "na". 
("Banana", "Banananana" aber nicht "Ba" oder "Bana")

### Alternativen `|`

Es gibt oft mehrere Möglichkeiten, wie ein Text aufgebaut sein kann. Mit dem **Alternator (oder)** 
`|` kann man eine Auswahl zwischen mehreren Mustern treffen.

[EQ] Treffen Sie entweder "Hund" oder "Katze".

[EQ] Treffen Sie Dateinamen mit Endung ".png" oder ".jpeg" findet.
Der Dateiname selbst sollte nur aus alphanumerischen Zeichen bestehen und ist beliebig lang.
Dafür können Sie eine Gruppe in Kombination mit dem `|` verwenden.

### Benutzerdefinierte Zeichenklassen

Sie kennen bereits `\d`, `\w`, `\s`.
Benutzerdefinierte Zeichenklassen funktionieren ähnlich, aber Sie
definieren selbst die erlaubten Zeichen.

Zum Beispiel können Sie die Ziffern-Zeichenklasse `\d` durch die benutzerdefinierte Zeichenklasse
`[0-9]` darstellen.
Diese Klasse enthält also alle Zeichen zwischen 0 und 9 (einschließlich).
Eine andere Schreibweise für diese Klasse wäre `[0123456789]`

[EQ] Schreiben Sie einen Zeichenklasse, die alle Kleinbuchstaben von "a" bis "z" enthält.

[EQ] Treffen Sie 5 Kleinbuchstaben hintereinander.

[EQ] Schreiben Sie eine Zeichenklasse, die alle Vokale (samt "ä","ö","ü") trifft.

Sie können außerdem eine Gruppe negieren, `[^0-9]` wäre äquivalent zu `\D`.

[EQ] Schreiben Sie einen regulären Ausdruck, der jede Zeichenkette trifft, die eine Zahl zwischen 0 und 255 darstellt, unter folgenden Bedingungen:
Die Zahl "0" darf nur stehen, wenn sie alleine ist ("0" aber nicht "05").
Zahlen größer als 0 dürfen keine führenden Nullen haben (z.B. 01 ist nicht erlaubt).

[EQ] Sie haben in [PARTREF::re-Metazeichen] bereits einen Regulären Ausdruck geschrieben, um eine
Uhrzeit (z.B. "12:59") zu matchen.
Allerdings waren in dieser Lösung ungültige Uhrzeiten wie "25:01" oder "12:69" möglich.
Überlegen Sie sich wie Sie mithilfe von Zeichenklassen einen Regex schreiben können, der solche
Uhrzeiten trifft, aber nur solche die gültig sind.

[EQ] Schreiben Sie einen regulären Ausdruck, der ein Datum im Format `DD.MM.YYYY` erkennt, unter folgenden Bedingungen:
- `DD`: Tag von 01 bis 31    
- `MM`: Monat von 01 bis 12   
- `YYYY`: vierstellige Jahreszahl     
Einzelne Monatsgrenzen, wie z.B. dass der Februar 28 Tage hat müssen Sie nicht beachten.

[EQ] Schreiben Sie einen Regex, der gültige E-Mail-Adressen trifft.
Anforderungen:
- Vor dem @ dürfen Buchstaben (Groß- und Kleinbuchstaben), Ziffern, Punkte (.), Unterstriche (_) und Bindestriche (-) stehen.   
- Nach dem @ kommt der Domain-Name, bestehend aus Buchstaben, Ziffern oder Bindestrichen.      
- Die Domain endet mit einem Punkt und einer Top-Level-Domain (z.B. ".com", ".de"), die nur Buchstaben enthält und mindestens 2 Zeichen lang ist.   
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]

[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
