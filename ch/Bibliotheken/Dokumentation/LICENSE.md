title: Überblick über Open Source Lizenzen
stage: beta
timevalue: 1.5
difficulty: 2
---
[SECTION::goal::idea]

- Ich erkenne, welche Lizenz eine Bibliothek hat, und verstehe ungefähr, was das bedeutet.
- Ich kann für eine eigene Bibliothek eine Lizenz auswählen und dies begründen.

[ENDSECTION]
[SECTION::background::default]

Software ist durch das Urheberrecht geschützt:
Niemand außer den Urheber_innen darf zunächst mal damit irgendetwas tun.
Um das zu ändern, können die Urheber_innen dem Rest der Welt (oder Teilen davon)
eine Nutzungslizenz erteilen.

Bei kommerzieller Software muss man für eine solche Lizenz (oft) Geld zahlen
und die Rechte, die die Lizenz einräumt, sind sehr eingeschränkt.

Bei Open-Source-Software bekommt die ganze Welt eine Lizenz, muss dafür nichts zahlen
und darf mit der Software sehr vieles machen.

[ENDSECTION]
[SECTION::instructions::detailed]

### Aufschlauen!

- Lesen Sie [HREF::https://github.com/readme/guides/open-source-licensing]
  und nötigenfalls (oder bei Interesse) auch noch
  [HREF::https://opensource.org/licenses] und
  [HREF::https://tldrlegal.com/].


### Erklären!

- [EQ] Was ist der wichtigste Unterschied zwischen _Copyleft_-Lizenzen und 
  freizügigen ("_permissive_") Lizenzen? 
- [EQ] Warum sind manche _Creative Commons_-Lizenzen keine Open-Source-Lizenzen?
- [EQ] Was ist der wichtigste Unterschied zwischen der MIT-Lizenz und _Public Domain_?
- [EQ] Wie findet man (üblicherweise) heraus, welche Lizenz eine Open-Source-Bibliothek hat?

### Lizenzentscheidung

- Versetzen Sie sich in folgende Rolle:
  Sie schreiben eigenständig eine Python-Bibliothek B und stellen diese über GitHub zur Verfügung. 
- [EQ] Welche Open-Source-Lizenz wählen Sie? Warum? 


### Bibliotheken nutzen

- Einige Zeit später stellen Sie fest, dass die Python-Fremdbibliothek XY von GitHub eine gute Ergänzung
  für ihr Projekt darstellen würde.
- [EQ] Beschreiben Sie, was Sie bei der Benutzung von XY beachten müssen, wenn Sie die
  nachfolgenden Fälle vorfinden.
  Besprechen Sie dabei insbesondere, wann Sie für die Verwendung von XY ihre Lizenz für B ändern müssten.
  Können Sie sie dann auch tatsächlich ändern? Wollen Sie?
    - XY referenziert **keine** Lizenz.
    - XY unterliegt der MIT-Lizenz.
    - XY unterliegt der GNU GPLv3-Lizenz.
    - XY unterliegt der Apache Lizenz 2.0.

[ENDSECTION]
[SECTION::submission::information,reflection]

[INCLUDE::../../_include/Submission-Markdowndokument.md]
Halten Sie die Abgabe kurz und bündig.

[ENDSECTION]
[INSTRUCTOR::Hinweise]

Relevante Punkte sind nur:

- Copyleft-Lizenzen verlangen, dass man ggf. geänderte Fassungen des Produkts samt Quelltext
  und wieder unter der Copyleft-Lizenz weitergibt.
- Freizügige Lizenzen verlangen das nicht.
- Freizügige Lizenzen verweigern ausdrücklich jegliche Garantie von Eigenschaften des Produkts.
  Bei Public Domain bleibt diese Frage offen.
- Die Lizenz steht üblicherweise in einer Datei `LICENSE` oder `license.txt` o.ä. im 
  obersten Verzeichnis.
- Hat XY keine Lizenz, darf man es nicht benutzen.
- Die eigene Lizenz braucht man bei reinem Python in keinem Fall zu ändern,
  denn die oft behauptete "Viralität" der GPLv3 gibt es gar nicht.
  Das Copyleft betrifft nur Änderungen an XY, nicht B.
  (Komplizierter wäre die Frage, wenn man eine Binärdatei weitergäbe, die XY und B zusammen enthält.)

[ENDINSTRUCTOR]