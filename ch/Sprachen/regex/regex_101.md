title: Einfühung in Regex
stage: alpha
timevalue: 1.0
difficulty: 1
profiles:
explains:
---
[SECTION::goal::idea]
Einstieg in reguläre Ausdrücke. Ich verstehe die grundlegenden Operatoren von POSIX-style Regex 
und kann einfache Matches selbst schreiben.
[ENDSECTION]

[SECTION::background::default]

[ENDSECTION]

[SECTION::instructions::loose]
Wir beginnen mit der Einführung auf folgender Seite: 
https://www.oreilly.com/content/an-introduction-to-regular-expressions/ und arbeiten diese durch 
bis wir am Abschnitt der Prä- und Suffixe ankommen. Diese sind für das Grundverständnis nicht 
allzu wichtig.

Dort wird auch auf Möglichkeiten zum Testen bzw. Ausprobieren von regulären Ausdrücken eingegangen. 
Dazu wird zu einem auf Websites wie https://regex101.com/ sowie das Python-Paket `re` verwiesen.

Wenn Sie den Blogpost auf der O'Reilly-Seite durchgearbeitet haben bearbeiten Sie die folgenden 
Aufgaben.

1. Einfaches Abgleichen von Wörtern Teil 2 (Wortgrenzen)
    - Schreiben Sie einen regulären Ausdruck welcher alle Wörter findet welche auf das wort **end** 
   enden.
2. Einfaches Abgleichen von Zahlen (Kreditkartennummer)
    - Schreiben Sie einen regulären Ausdruck welcher Kreditkartennummern matcht. 
[NOTICE]
Zur Einfachheit nehmen wir an, dass Kreditkartennummern bis zu 16 Zeichen lang sind und, in 
4er-Blöcken, separiert durch Leerzeichen oder Bindestriche, auftreten können. 
z.B. `4544 4614 6932 1714`
[ENDNOTICE]
3. Jahreszahl aus Datum finden
    - Schreiben Sie einen regulären Ausdruck welcher die Jahreszahl aus verschiedenen Formaten zur 
   Darstellung von Daten erkennt.
    - Beschreiben Sie auch, wenn Sie merken, dass es hier zu Schwierigkeiten mit einer reinen 
   Regex-Lösung kommen sollte.
4. Hex-Farben finden
    - Schreiben Sie einen regulären Ausdruck welcher Hex-Farben erkennt.
5. Simpler E-Mail-Abgleich
    - Schreiben Sie einen regulären Ausdruck welcher einen simplen E-Mail-Abgleich vornimmt.
[NOTICE]
Simpel bedeutet, dass die E-Mail aus Zeichen vor dem @ Domainname sowie toplevel-Domain besteht. 
z.B. `name@example.com`.
[ENDNOTICE]
6. Simples HTML-Tag matching
    - Schreiben Sie einen regulären Ausdruck, welcher einfache HTML bzw. XML tags matchen kann.
[NOTICE]
Die Tags haben keine attribute und bestehen lediglich aus ihrem Bezeichner, z.B. `\<a\>` oder 
`\</br\>`. Diskutieren Sie auch warum sich reguläre Ausdrücke nicht zum vollständigen 
Parsen von HTML eignen.
[ENDNOTICE]

[ENDSECTION]

[SECTION::submission::reflection]

Ziel ist es jeweils einen regulären Ausdruck passend zur Aufgabenstellung, einige 
Beispiele zum Testen, sowie eine kurze Reflexion zur Vorgehensweise aufzuschreiben.

[ENDSECTION]

[INSTRUCTOR::heading]
Prüfen Sie, ob die regulären Ausdrücke die gegebenen Anforderungen erfüllen und ob aus der 
Beschreibung hervorgeht, dass die Studierenden selbst auf die Lösung gekommen sind.

1. Wortgrenzen
   - Mögliche Lösung: `\b\w*(end)\.?\b`
2. Kreditkartennummern
   - Mögliche Lösung: `(\d{4})\N?(\d{4})\N?(\d{4})\N?(\d{4})`
3. Jahreszahl
   - Mögliche Lösung: `(\d{4})`
   - **Allerdings:** Sobald das Jahr in Kurzschreibweise angegeben wird, ergeben sich 
     Schwierigkeiten beim Erkennen. So könnte 10.10.10 sowohl "Tag.Monat.Jahr" als auch 
     "Monat.Tag.Jahr" und natürlich auch "Jahr.Monat.Tag" sein. 
4. Hexfarben
   - Mögliche Lösung: `\#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})`
5. E-Mails
   - Mögliche Lösung: `([[:alnum:][:punct:]]+)\@([[:alnum:]-]+[^-])\.([\w\.]{1,63})`
   - Dieser Regex nimmt zwar eine gewisse "Validierung" der E-Mail, kann aber über die Wirkliche 
     Validität ebendieser nichts aussagen, da z.B. E-Mails mit Sonderzeichen vor dem @ durch 
     doppelte Anführungszeichen markiert werden müssten.
6. HTML
   - Mögliche Lösung: `\<(\\?\w+)\>`

Alle Beispiellösungen nutzen Groups zum Erkennen einzelner Teilabschnitte der gesuchten Objekte. 
In der Praxis ist dies häufig hilfreich, da diese Gruppen dann weiter genutzt werden könnten, 
zum Bestehen der Aufgabe aber nicht zwingend notwendig. 

[ENDINSTRUCTOR]
