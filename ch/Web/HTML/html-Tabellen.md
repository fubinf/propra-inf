title: Tabellen in HTML
stage: beta
timevalue: 1
difficulty: 2
assumes: html-erste-Schritte, html-Medien
---
[SECTION::goal::experience]

- Ich kann erklären, wie die Elemente "table", "tründ "tdßum Erstellen einer Tabelle
eingesetzt werden.
- Ich implementiere einfache Tabellen mit spalten- oder zeilenübergreifenden Zellen

[ENDSECTION]
[SECTION::background::default]

Tabellen sind eine Möglichkeit Text oder Daten in einer geordneten und übersichtlichen Art darzustellen. 
Vom Tafelwerk in der Schule bis zur Bundesligatabelle findet man sie im Alltag quasi überall. 
Deshalb beinhaltet natürlich auch HTML die Möglichkeit, Tabellen anzuzeigen.
Diese Aufgabe beschäftigt sich damit, Tabellen zu erstellen.

[ENDSECTION]
[SECTION::instructions::detailed]



[ER] Erstellen Sie eine Website `HTMLTabellen.html` mit passendem Menü und Überschrift. 
Tabellen benutzen das HTML-Element `<table>`.
Erstellen Sie eine einfache Tabelle mit zwei Zeilen und drei Spalten:

```text
|----------------------------------------------|
| Umsatz      | Gewinn       | Ausgaben        |
|-------------|--------------|-----------------|
| 5,000,000 € | 1,200,000 €  | 3,800,000 €     |
|----------------------------------------------|
```

Bei SelfHTML finden Sie unter 
[Aufbau einer Tabelle](https://wiki.selfhtml.org/wiki/HTML/Tabellen/Aufbau_einer_Tabelle)
einen Überblick, wie das funktioniert.

[ER] Für lange Tabellen, die beim Ausdrucken über mehrere Seiten gehen würden, 
kann es sinnvoll sein, wenn Spaltenköpfe oder -füße separat von den eigentlichen
Tabelleninhalten beschrieben sind. 
Dann können die Werkzeuge z.B. Spaltenköpfe auf jeder Seite wiederholen,
wenn man die Tabelle ausdruckt. 
Auch für Sehbehinderte ist diese Zusatzinformation hilfreich.
Dazu kann die Tabelle in Kopf, Hauptteil und Fuß aufgeteilt werden: `<thead>`, `<tbody>` und `<tfoot>`. 
Setzen Sie dies für Ihre Tabelle um.

[ER] Hin und wieder möchte man auch Tabellenzellen haben, die mehrere Spalten oder 
mehrere Zeilen überspannen. 
Dafür gibt es Lösungen mit den Attributen `colspan` und `rowspan`.
Ergänzen Sie Ihre Tabelle, sodass die untenstehende Tabelle abgebildet wird.
Eine Erklärung dazu finden Sie in Abschnitt zwei des SelfHTML-Dokuments
[Zellen verbinden](https://wiki.selfhtml.org/wiki/HTML/Tabellen/Zellen_verbinden#Zellen_verbinden).

```text
|-------------------------------------------------------|
| Finanzen                                              |
|--------|-------------|--------------|-----------------|
| Jahr   | Umsatz      | Gewinn       | Ausgaben        |
|--------|-------------|--------------|-----------------|
| 2022   | 5,000,000 € | 1,200,000 €  | 3,800,000 €     |
|        |-------------|--------------|                 |
|        | Veränderung zum VJ: +20%   |                 |
|--------|-------------|--------------|-----------------|
| 2023   | 6,500,000 € | 1,500,000 €  | 4,000,000 €     |
|        |-------------|--------------|                 |
|        | Veränderung zum VJ: +30%   |                 |
|--------|-------------|--------------|-----------------|
| Mittel | 5,750,000 € | 1,350,000 €  | 3,900,000 €     |
|--------|-------------|--------------|-----------------|
```

[HINT::Ich kann nicht erkennen, ob die Zellen verbunden sind]
Fügen Sie im `table`-Element ein Attribut `border` mit dem Wert `1` ein. 
Nun erhalten Sie einen Rahmen im Browser. 
Das hilft Ihnen das Ausmaß der Tabellenzellen zu erkennen.


Aber **Achtung**: Das `border`-Attribut ist im aktuellen HTML-Standard nicht mehr vorgesehen und
sollte deshalb *ausschließlich* für Entwicklungszwecke verwendet werden!
Um der Tabelle Rahmen und Styling zu geben, sollten Sie [TERMREF::CSS] verwenden.
[ENDHINT] 

[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]

[INSTRUCTOR::Musterlösung]

Eine Musterlösung findet sich in [TREEREF::/Web/HTML/html-Tabellen.html].
[ENDINSTRUCTOR]
