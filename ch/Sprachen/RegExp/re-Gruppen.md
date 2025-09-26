title: "Gruppen"
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: re-Quantoren
---

[SECTION::goal::idea]
Ich verstehe, wie man Gruppen, Alternatoren und Zeichenklassen benutzen kann, um komplexere
Muster zu beschreiben.
[ENDSECTION]


[SECTION::background::default]
Um das volle Potenzial von regulären Ausdrücken nutzen zu können, sind Gruppen wichtig, um
komplexere Sacheverhalte darstellen zu können.
[ENDSECTION]


[SECTION::instructions::loose]
Quantoren eignen sich nicht nur gut, um einzelne Zeichen eine bestimmte
Anzahl an Malen zu wiederholen.
Sie können damit auch ganze Gruppen an Zeichen wiederholen.
Diese Gruppen werden in Klammern `()` angegeben.
Letztendlich enthalten die Klammern nur einen weiteren regulären Ausdruck,
das praktische ist jedoch, dass Sie diese z. B. nutzen können, um Sie mit Quantoren zu wiederholen:
`(HA)+` sucht nach Zeichenketten, die `HA` mindestens 1-mal wiederholt.

[EQ] Treffen Sie "Banana" mit mindestens zwei "na". 
("Banana", "Banananana" aber nicht "Ba" oder "Bana")

Sie können den folgenden Text nutzen, um Ihre regulären Ausdrücke zu testen:
```
Die Produktnamen Banana und Banananana enthalten mindestens zwei „na“-Folgen, während Ba und Bana dafür nicht ausreichen.  
In einem Bericht werden die Tiere Hund und Katze erwähnt.  
Die Bilddateien urlaub123.png und selfie42.jpeg sind korrekt benannt, wohingegen grafik.bmp nicht den Anforderungen entspricht.  
Eine Sequenz aus fünf Kleinbuchstaben wie abcde oder uvwxy erfüllt die Bedingung, außerdem treten Vokale wie a, e, i, o, u, ä, ö, ü im Text auf.  
Wörter in reiner Großschreibung wie NUR GROSSBUCHSTABEN unterscheiden sich von gemischten Varianten wie KleinUndGroß.  
Gültige Uhrzeiten im Format HH:MM sind zum Beispiel 00:00 und 12:59, ungültige dagegen 25:01 oder 12:69.  
Auch Daten wie 31.12.2025 und 01.01.1999 sind korrekt, während 32.13.2025 und 00.00.0000 ausgeschlossen werden müssen.  
Bei den E-Mail-Adressen gelten user.name-123@example.com und info@domain.de als gültig, nicht jedoch falsch@domain,com.
```


### Alternativen `|`

Es gibt oft mehrere Möglichkeiten, wie ein Text aufgebaut sein kann. Mit dem 
[Alternator (oder)](https://www.regular-expressions.info/alternation.html)
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

[EQ] Schreiben Sie eine Zeichenklasse, die alle Kleinbuchstaben von "a" bis "z" enthält.

[EQ] Treffen Sie 5 Kleinbuchstaben hintereinander.

[EQ] Schreiben Sie eine Zeichenklasse, die alle kleingeschriebenen Vokale (samt "ä","ö","ü") trifft.

Sie können außerdem eine Gruppe negieren, `[^0-9]` wäre äquivalent zu `\D`.

[EQ] Schreiben Sie eine Zeichenklasse, die keine Großbuchstaben des Alphabets trifft.

[EQ] Sie haben in [PARTREF::re-Metazeichen] bereits einen regulären Ausdruck geschrieben, um eine
Uhrzeit (z. B. "12:59") zu matchen.
Allerdings waren in dieser Lösung ungültige Uhrzeiten wie "25:01" oder "12:69" möglich.
Überlegen Sie sich, wie Sie mithilfe von Zeichenklassen einen regulären Ausdruck schreiben können, der nur
gültige Uhrzeiten in dem Format trifft.

[EQ] Schreiben Sie einen regulären Ausdruck, der ein Datum im Format `DD.MM.YYYY` erkennt, unter folgenden Bedingungen:     
- `DD`: Tag von 01 bis 31       
- `MM`: Monat von 01 bis 12       
- `YYYY`: vierstellige Jahreszahl        
Einzelne Monatsgrenzen, wie z. B. dass der Februar 28 Tage hat, müssen Sie nicht beachten.

[EQ] Schreiben Sie einen regulären Ausdruck, der gültige E-Mail-Adressen trifft.    
Die Anforderungen für eine gültige E-Mail-Adresse sind:      
- Eine E-Mail-Adresse muss genau ein "@" enthalten.     
- Vor dem "@" dürfen Buchstaben (Groß- und Kleinbuchstaben), Ziffern, Punkte (.), Unterstriche (_) und Bindestriche (-) stehen.          
- Nach dem "@" kommt der Domain-Name, bestehend aus Buchstaben, Ziffern oder Bindestrichen.         
- Die Domain endet mit einem Punkt und einer Top-Level-Domain (z. B. ".com", ".de"), die nur Buchstaben enthält und mindestens 2 Zeichen lang ist.   
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
