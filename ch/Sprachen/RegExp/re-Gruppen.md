title: "Gruppen"
stage: beta
timevalue: 1.0
difficulty: 2
assumes: re-Quantoren
---

[SECTION::goal::idea]
Ich verstehe, wie man Gruppen, Alternatoren und Zeichenklassen benutzen kann, um komplexere
Muster zu beschreiben.
[ENDSECTION]


[SECTION::background::default]
Um das volle Potenzial von regulären Ausdrücken nutzen zu können, sind Gruppen wichtig, um
komplexere Sacheverhalte darstellen zu können.
Man kann damit ganze reguläre Ausdrücke wiederholen oder optional machen anstatt nur einzelne Zeichen.
[ENDSECTION]


[SECTION::instructions::loose]
Gruppen werden durch Klammern `()` angegeben.
Ein Klammerpaar enthält einen weiteren regulären Ausdruck.
Ein Quantor hinter einer schließenden Klammer bezieht sich auf den ganzen Ausdruck:
`(HA)+` sucht nach Zeichenketten, die `HA` ein- oder mehrmals wiederholen.

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
<!-- time estimate: 10 min -->


### Alternativen `|`

Es gibt oft mehrere Möglichkeiten, wie ein Text aufgebaut sein kann. Mit dem 
[Alternator (oder)](https://www.regular-expressions.info/alternation.html)
`|` kann man eine Auswahl zwischen mehreren Mustern treffen.
Ohne Gruppen und Quantoren bezieht sich ein `|` auf alles links und alles rechts davon,
was oft zu viel ist.
Der Operator ist deshalb meist nur mit Gruppen nützlich.  
[Einzelheiten zu `|`](https://www.regular-expressions.info/alternation.html) (meist reicht der erste Abschnitt).

[EQ] Treffen Sie entweder "Hund" oder "Katze".

[EQ] Treffen Sie Dateinamen mit Endung ".png" oder ".jpeg".
Der Dateiname selbst sollte nur aus alphanumerischen Zeichen bestehen und darf beliebig lang sein.
<!-- time estimate: 10 min -->


### Benutzerdefinierte Zeichenklassen: `[ ]`

Sie kennen bereits `\d`, `\w`, `\s`.
Benutzerdefinierte Zeichenklassen funktionieren ähnlich, aber Sie
definieren selbst die erlaubten Zeichen.

Zum Beispiel können Sie die Ziffern-Zeichenklasse `\d` durch die benutzerdefinierte Zeichenklasse
`[0-9]` darstellen.
Diese Klasse enthält also alle Zeichen zwischen 0 und 9 (einschließlich).
Eine andere Schreibweise für diese Klasse wäre `[0123456789]`

[EQ] Schreiben Sie eine Zeichenklasse, die alle Kleinbuchstaben von "a" bis "z" enthält.

[EQ] Treffen Sie 5 Kleinbuchstaben hintereinander.

[EQ] Schreiben Sie eine Zeichenklasse, die alle kleingeschriebenen deutschen Vokale (samt "ä","ö","ü") trifft.

[WARNING]
In [TERMREF::Unicode] gibt es noch massenhaft andere Vokale.
Nehmen Sie sich vor naiv selbst geschriebenen regulären Ausdrücken in acht,
wenn Ihre Daten vielfältig sein könnten!
Meist sind die eingebauten Zeichenklassen wie `\w` schlauer als selbst Hingeschriebenes.
[ENDWARNING]

Sie können außerdem eine Gruppe negieren, `[^0-9]` entspricht im Wesentlichen `\D`.

Wenn man scharf nachdenkt, werfen diese Sonderbedeutungen von `^` und `-` Fragen auf.
Wie schreibt man z.B. eine Zeichenklasse, die auf ein `-` zutrifft??  
Diese Fragen werden auf der Seite
[Zeichenklassen bei regular-expressions.info](https://www.regular-expressions.info/charclass.html)
in Abschnitten 1 bis 3 geklärt.

[EQ] Schreiben Sie eine Zeichenklasse, die keine Großbuchstaben des deutschen Alphabets trifft.

[EQ] Sie haben in [PARTREF::re-Metazeichen] bereits einen regulären Ausdruck geschrieben, um eine
Uhrzeit (z. B. "12:59") zu matchen.
Allerdings waren in dieser Lösung ungültige Uhrzeiten wie "25:01" oder "12:69" möglich.
Überlegen Sie sich, wie Sie mit Zeichenklassen und Alternation einen regulären Ausdruck schreiben können, 
der nur gültige Uhrzeiten in diesem Format trifft.

[EQ] Schreiben Sie einen regulären Ausdruck, der ein Datum im Format `DD.MM.YYYY` erkennt, unter folgenden Bedingungen:     
- `DD`: Tag von 01 bis 31       
- `MM`: Monat von 01 bis 12       
- `YYYY`: vierstellige Jahreszahl von 1000 bis 9999     
Einzelne Monatsgrenzen, wie z. B. dass der Februar 28 Tage hat, müssen Sie nicht beachten.

[EQ] Schreiben Sie einen regulären Ausdruck, der gültige E-Mail-Adressen trifft.  
Die Anforderungen für eine gültige E-Mail-Adresse sind:     
- Eine E-Mail-Adresse muss genau ein "@" enthalten.     
- Vor dem "@" dürfen Buchstaben (Groß- und Kleinbuchstaben), Ziffern, Punkte (.), Unterstriche (_) und Bindestriche (-) stehen.          
- Nach dem "@" kommt der Domain-Name, bestehend aus Buchstaben, Ziffern oder Bindestrichen.         
- Die Domain endet mit einem Punkt und einer Top-Level-Domain (z. B. ".com", ".de"), die nur Buchstaben enthält und mindestens 2 Zeichen lang ist.   

[WARNING]
Auch dies ist wieder recht naiv. 
Die echten Emailadressen-Regeln sind leider _weitaus_ komplizierter:
[HREF::https://en.wikipedia.org/wiki/Email_address].
[ENDWARNING]
<!-- time estimate: 30 min -->


### Rückwärtsreferenzen: `\1` etc.

Angenommen, wir suchen einen allgemeinen und knappen regulären Ausdruck, der die ersten beiden Zeilen
des folgenden Textblocks trifft, aber nicht die dritte:
```
Berlin: Die Berliner Regeln für den Verkauf von Quarkbällchen sind erquickend.
Brandenburg: Die Brandenburger Regeln für den Verkauf von Quarkbällchen sind erquickend.
Berlin: Die Brandenburger Regeln für den Verkauf von Quarkbällchen sind erquickend.
```
Der Ausdruck muss also sicherstellen, dass die Teiltreffer 1 und 2 gleich sind.
Wenn wir beide Male `(Berlin|Brandenburg)` hinschreiben, ist das nicht gewährleistet.
Kann man sowas ausdrücken?
Ja, man kann. Die Erklärung steht auf
[Rückwärtsreferenzen bei regular-expressions.info](https://www.regular-expressions.info/backref.html)
im ersten Abschnitt.

[EQ] Schreiben Sie den gesuchten Ausdruck in möglichst knapper Form. 
Er muss der Art nach nur für Berlin und Brandenburg funktionieren, nicht auch für z.B.
Hessen oder Niedersachsen
<!-- time estimate: 10 min -->
[ENDSECTION]


[SECTION::submission::information]
[INCLUDE::/_include/Submission-Quellcode.md]
[INCLUDE::/_include/Submission-Markdowndokument.md]
[ENDSECTION]


[INSTRUCTOR::Aufgaben im Großen und Ganzen korrekt?]
[INCLUDE::ALT:]
[ENDINSTRUCTOR]
