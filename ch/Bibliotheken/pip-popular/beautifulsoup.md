title: "BeautifulSoup: Informationen aus HTML (oder XML) extrahieren" 
stage: beta
timevalue: 1.0
difficulty: 2
explains: 
assumes: pip, HTMLErsteSchritte
---

[SECTION::goal::trial]

Ich kann für Web-Scraping eine komfortable Bibliothek einsetzen

[ENDSECTION]

[SECTION::background::default]

Immer wieder kommt es bei der Web-Programmierung dazu, dass man programmatisch Informationen abrufen möchte,
die zwar auf einer textuellen HTML-Seite zugänglich sind, aber nicht in strukturierter Form
über ein API oder eine Datenbank zur Verfügung stehen.

Dann greift man auf Web-Scraping ("Abschaben") zurück: 
Man pickt sich die Informationsbröckchen direkt aus der HTML-Repräsentation der Webseite heraus.
Das mit bloßem Python-Code oder nur mit einem HTML-Parser zu tun ist mühsam und fehleranfällig.
Es gibt Bibliotheken, die das weitaus einfacher und besser erledigen; damit kann Scraping regelrecht Spaß machen.
Eine davon probieren wir hier aus.

[ENDSECTION]

[SECTION::instructions::detailed]

Wir nehmen uns als Ziel vor, auf einer ProPra-Seite zu zählen, wie viele
sehr leichte und leichte Aufgaben dort vermerkt sind und welchen Zeitwert diese
Aufgaben zusammengenommen haben.

Das führt zu nur wenigen Zeilen Code, benutzt aber ein Gutteil der wichtigsten Funktionen 
unserer Bibliothek.

### `beautifulsoup4` installieren

Installieren Sie das Paket `beautifulsoup4` mit `pip`.
Achtung: Das Paket, das Sie zur Benutzung in Python importieren müssen, heißt nicht so,
sondern kürzer `bs4`.

Lesen Sie den Einstiegsabschnitt (bis vor die erste Zwischenüberschrift) der
[BeautifulSoup-Homepage](https://www.crummy.com/software/BeautifulSoup/)
und überfliegen Sie das Inhaltsverzeichnis der
[BeautifulSoup-Dokumentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).


### Webseite auswählen und studieren

Finden Sie eine Webseite des ProPra, auf der im Inhaltsverzeichnis sowohl mehrere
Aufgaben der Schwierigkeitsstufen '1:very low'/'2:low' verzeichnet sind
als auch mindestens eine mit '3:medium' oder '4:high'.

Zeigen Sie im Browser den Quelltext an (Ctrl-U) und verstehen Sie den Aufbau des
Inhaltsverzeichnisses mit der Liste der Kapitel, Aufgabengruppen und Aufgaben.

Ein einzelner Eintrag für eine Aufgabe hat, wenn man ihn hübscher formatiert, diesen Aufbau:
```
  <div class='indent2 stage-beta'>
      <a href='HTTP-GET.html'
         title="HTTP GET: Abrufen von Ressourcen (request, response, status codes)">HTTP-GET</a>
      <span class='difficulty2' title='Difficulty: low'>&#x26ab;&#xfe0e;</span>
      <span class='timevalue-decoration' title='Timevalue: 1.0 hours'>1.0</span>
      <span class='assumed-by-decoration' title='assumed by: m_requests'></span>
      <span class='assumes-decoration' title='assumes: apt, redirect'></span>
  </div>
```


### Hauptprogramm, Webseite abrufen

[ER] Legen Sie `beautifulsoup.py` an.
Rufen Sie (ggf. per Kommandozeilen-Argument) die ausgewählte Webseite
entweder mittels [PARTREF::m_requests] ab oder verfrachten Sie Ihren Quelltext
aus dem Browser mittels Copy/Paste in eine Datei und öffnen Sie im Programm dann diese.


### Difficulty-Einträge finden

Lesen Sie grob den Abschnitt "Quick Start" in der Dokumentation, um eine ungefähre
Vorstellung zu entwickeln, wie `bs4` funktioniert.

[ER] Legen Sie ein `soup`-Objekt an.
Das zweite Argument hängt davon ab, welche Parser (die oft nicht in Python geschrieben sind)
auf Ihrem System installiert sind.
Wenn `'html.parser'` nicht funktioniert, dann schreiben Sie zunächst `'html'` und lassen
sich dann zur Laufzeit in der Warnmeldung von `bs4` einen Parser empfehlen und geben den an.

`soup` repräsentiert das ganze HTML-Dokument. 
Später arbeiten wir mit _Tags_, die einzelne Teilbäume des Dokuments repräsentieren.
`bs4` behandelt beides fast überall gleich.

[ER] Nun wollen wir die `<span>`-Tags finden, in denen die _difficulty_ vermerkt ist,
aber nur die mit den Stufen 1 und 2.
Das geht mit einer einzigen Anweisung, wenn man zum Filtern der gewünschten Attributwerte
eine Funktion benutzt anstatt einen festen Wert. 
Lesen Sie in der Dokumentation nach, wie das geht, und schreiben Sie die Anweisung,
um eine Liste von Tags zu erhalten.

[HINT::Womit sucht man nach Tags?]
`find_all()`
[ENDHINT]

[HINT::Irgendwie funktioniert `class=...` bei mir nicht]
`class` ist in Python ein Schlüsselwort und deshalb nicht als Parametername erlaubt.
Sie müssen die `attr=` Notation benutzen.
[ENDHINT]

[HINT::Funktion zum Filtern? Wo steht das beschrieben?]
Siehe [HREF::https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function].
Aber Vorsicht, nicht verwirren lassen: Das Beispiel zeigt einen Filter für ein Tag.
Wir brauchen jedoch einen Filter für einen Attributwert.
[ENDHINT]

Dieses Vorgehen ist allerdings riskant:
Sollte es noch irgendwo anders als im Inhaltsverzeichnis solche `<span>`-Tags geben,
dann erwischen wir zu viele Einträge.

[ER] Finden Sie auf der Webseite ein Element, das nur genau das Inhaltsverzeichnis enthält.
Rufen Sie im Programm das passende Tag ab und machen Sie den Abruf nur darauf,
nicht auf der kompletten `soup`.

[ER] Geben Sie die Anzahl von Treffern aus:
`print("number of <span> tags declaring difficulty 1 or 2:", ...)`

Super, Schritt 1 ist geschafft.


### Zugehörige Zeitwerte finden

Um die Zeitwerte aufzusummieren, müssen wir die Tags mit
`<span class='timevalue-decoration' ...`
finden. Aber natürlich nicht alle, sondern nur die "bei" den eben gefundenen Difficulty-Tags.

Der sauberste Weg dafür ist es, von jedem Difficulty-Tag hochzugehen zum
umgebenden `<div>` und dann nur darin nach einem (und nur einem)
`<span class='timevalue-decoration' ...` zu suchen.
Das geht also nicht in einem Schritt, sondern wir brauchen eine Schleife.

Die Zeitwerte stehen im Textinhalt des `<span>`-Tags.
Wie man den abruft, haben wir schon im "Quick Start" gesehen.
Nun noch in `float` umwandeln und in `timevalues_total` aufsummieren.

[ER] Schreiben Sie diese Schleife und geben Sie das Ergebnis aus:  
`print("Their total timevalue: %.1f" % timevalues_total)`


### Aufrufen

[EC] Rufen Sie Ihr Programm einmal auf.

Voilà, Sie können Web-Scraping!

[ENDSECTION]

[SECTION::submission::program,trace]

[INCLUDE::/_include/Submission-Kommandoprotokoll.md]
[INCLUDE::/_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Code ansehen]

### Kommandoprotokoll

Das korrekte Ergebnis hängt davon ab, welche Webseite man aussucht.
Es sollen mehrere Treffer (sehr leicht, leicht) und mindestens ein Nichttreffer (mittel, schwer)
darauf sein.

### Quellcode

Im Quellcode bitte folgende Aspekte prüfen: 

- Suche nur im Inhaltsverzeichnis (tag ´nav´)
- Abruf der difficulty-spans mit nur einem Statement
- Dabei Filterung per Funktion und Suche auch nach 'very low', auch wenn es dazu keinen Treffer gibt
- Zugriff auf timevalue-Schwesterknoten mit `.parent()`, dann `.find()`
- Zugriff auf den eigentlichen timevalue per `.string` und nicht etwa aus dem `title`-Attribut

Musterlösung siehe [TREEREF::beautifulsoup.py].

[ENDINSTRUCTOR]
