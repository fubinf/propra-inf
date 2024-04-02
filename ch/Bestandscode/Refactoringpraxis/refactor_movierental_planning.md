title: Movie Rental - Codeerkundung
stage: alpha
timevalue: 1.5
difficulty: 4
---

[SECTION::goal::experience,trial]

- Ich bin in der Lage mir bisher unbekannten Code zu lesen dessen Funktion zu erklären.
- Ich bin in der Lage zu beschreiben, welche Probleme Code aufweist.
- Ich bin in der Lage zu formulieren, welche Refaktorierungen ich durchführen möchte.

[ENDSECTION]

[SECTION::background::default]

Sich in fremden Code einzuarbeiten ist gar keine leichte Aufgabe. 
Der Programmierstil kann für einen fremd wirken oder man kennt die verarbeiteten Konzepte (noch) 
nicht.  
In dieser Aufgabe dürfen Sie sich austoben: Es wird nur minimale Anleitung gegeben, damit eine 
Abgabe möglich ist. 
Die tatsächliche Lösung ist aber ganz Ihnen überlassen.

[ENDSECTION]

[SECTION::instructions::tricky]

[WARNING]
In dieser Aufgabe sind sie bis auf die Aufgabenstellung selbst sich selbst überlassen.
Wenn Sie zuerst eine geführte Variante einer Refaktorierung bearbeiten möchten, werden Sie in 
[PARTREFTITLE::01gildedrose_tests] und dessen Folgeaufgaben fündig.
[ENDWARNING]


- Laden Sie [PARTREF::movie_rental.zip] herunter und entpacken Sie das Zipfile in Ihr 
  Arbeitsverzeichnis.
- Die Datei `movie_rental.py` enthält ein Programm, dass in einer Videothek die Ausleihen 
  dokumentiert.
  Die Methode `Customer.statement()` gibt eine Zusammenfassung des Kontos aus. 
  Diese kann z. B. so aussehen:

```console
Rental Record for martin
  Ran 3.5
  Trois Couleurs: Bleu 2.0
Amount owed is 5.5
You earned 2 frequent renter points
```

- Die Datei `test_movie_rental.py` enthält einen Test für das Programm, allerdings ist der 
  Testumfang sehr mager.
- Ihre Aufgabe ist es die Ausgabe von `Customer.statement()` in eine HTML-Version umzuwandeln.
  Diese soll, auf Basis des Beispiels oben, so aussehen:

```html
<h1>Rental Record for <em>martin</em></h1>
<table>
  <tr><td>Ran</td><td>3.5</td></tr>
  <tr><td>Trois Couleurs: Bleu</td><td>2.0</td></tr>
</table>
<p>Amount owed is <em>5.5</em></p>
<p>You earned <em>2</em> frequent renter points</p>
```

- [EQ] Machen Sie sich mit dem Code vertraut und beschreiben Sie, welche Teile welche Funktion 
  im Code übernehmen.
- [EQ] Beschreiben Sie, worin die Probleme in dem Code liegen.  
  Was macht den Code schlecht wartbar?  
  Wieso ist der Code schlecht zu verstehen?  
  Begründen Sie Ihre Angaben kurz!
- [EQ] Gibt es Teile des Codes oder an der gewünschten Funktionalität, die Sie noch nicht 
  verstehen bzw. beherrschen?  
  Wenn ja, welche sind das? Recherchieren Sie dazu und beschreiben Sie Ihre Funde kurz.
- [EQ] Überlegen Sie sich einen Plan: Wie möchten Sie vorgehen, um den Code zu refaktorieren?  
  Wie sollen die Tests dazu aussehen?  
  Wie wird die Implementierung der HTML-Ausgabe in etwa funktionieren?
  Denken Sie daran, dass Sie die Schnittstellen des Programms für den Nutzer nicht verändern 
  dürfen (die Ausgabe des Programms darf sich aber so wie oben beschrieben ändern!)


[ENDSECTION]

[SECTION::submission::information,program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Probleme des Codes]
Der Code hat viele Problemstellen, u. a.:

- Die Verantwortlichkeiten sind schlecht getrennt, mehr Klassen können helfen.
- SOLID ist verletzt.
- Die Tests sind sehr unvollständig.
- Die Logik ist schwer durchschaubar.
- Die Dokumentation ist lückenhaft.
- Der Code ist nicht modular aufgebaut und damit schlecht wartbar.

Es geht nicht darum _alle_ diese Punkte zu finden, da sich einige Punkte auch beim Beheben 
anderer Punkte von alleine lösen. 
Diese Punkte sollen aber begründet sein. Ohne Begründung soll die Lösung zurückgewiesen werden.
[ENDINSTRUCTOR]
