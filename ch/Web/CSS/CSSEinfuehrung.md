title: Einführung in CSS
stage: alpha
timevalue: 1.0
difficulty: 2
requires: HTMLErsteSchritte
---

[SECTION::goal::experience]
- Ich kann CSS in HTML oder als separate Datei einbinden
- Ich kann CSS-Elemente identifizieren und einige einfache CSS-Eigenschaften anwenden.

[ENDSECTION]
[SECTION::background::default]

[TERMREF::CSS] wird benutzt um [TERMREF2::HTML::--Dokumente] mit Layout und Design zu versehen. 
Diese Aufgabe beschäftigt sich damit, wie CSS in HTML zur Anwendung kommt und mit ersten Selektoren und Eigenschaften.

[ENDSECTION]
[SECTION::instructions::detailed]

### CSS Syntax

CSS versteht sich als eine Liste von Eigenschaften, die HTML-Elementen zugewiesen wird.
Über einen Selektor werden ein oder meherere Elemente ausgewählt. Innerhalb der
geschweiften Klammern findet sich dann die durch Semikolon getrennte Liste der Eigenschaften.

```css
Selektor {
    eigenschaft: wert;
    zweite-eigenschaft: zahl;
}
```

Ein Beispiel:

```css
body {
  background-color: rgb(211, 211, 211); 
  color: #000000;
  font-size: small;
}

h1 {
  font-weight: bold;
  color: blue;
}
```

Die einzelnen Eigenschaften (engl. *properties*) sind dabei nicht willkürlich gewählt, 
sondern folgen der Definition des World Wide Web Consortiums (W3C),
damit Browser und Entwickler sich auf eine Darstellung einigen können.

### CSS Einbinden
Grundsätzlich gibt es drei verschiedene Varianten, wie CSS in HTML eingebunden werden kann.

1. **Als externes Stylesheet**: Dabei wird das CSS in eine separate Datei geschrieben, 
für gewöhnlich mit der Endung `.css`. In dieser Datei befindet sich dann ausschließlich CSS ohne HTML. 
Im HTML-Dokument wird innerhalb des `head`-Elements ein Element eingefügt, sodass der Browser weiß, wo nach der CSS-Datei zu suchen ist:

```html
    <link rel="stylesheet" type="text/css" href="beispiel.css">
```

Vorteil hierbei ist, dass derselbe CSS-Code für mehrere HTML-Dokumente verwendet werden kann. Dies ist daher auch der Standard zum Einbinden von CSS.

2. **Als internes Stylesheet**: Anstatt den CSS-Code in einer separaten Datei zu halten, kann der auch in der HTML-Datei Platz finden. Dies geschieht über die Verwendung des `style`-Elements:

```html
<head>
    <title>Beispiel</title>
    <style type="text/css">
        body { background-color: purple; }
    </style>
</head>
```

3. **Innerhalb von HTML-Tags**: Über das `style`-Attribut kann CSS direkt am Element platziert werden, für das die Eigenschaften gelten sollen. Hierbei entfällt dann der Selektor sowie die geschweiften Klammern:

```html
<p style="color: purple; text-decoration: underline;">Beispieltext</p>
```

### Aufgaben

Als Grundlage für das Experimentieren mit CSS soll das erstellte Dokument aus [PARTREF::HTMLErsteSchritte] verwendet werden.

[ER] Zunächst soll die Hauptüberschrift auf der Seite zentriert werden. Benutzen Sie dafür die CSS-Eigenschaft `text-align` mit dem Wert `center`. Ändern Sie außerdem die Schriftfarbe zu einem Python-gerechten Blau.

[ER] Mittels eines internen oder externen Stylesheets, ändern Sie die Hintergrundfarbe der Webseite. Um den gesamten Inhalt der Website zu beinflussen, ist es sinnvoll, das `body`-Element zu selektieren.

[ER] Ändern Sie Schriftart, Schriftgröße und Schriftstärke für Absätze und Listen auf der Seite.

[HINT::Einige Beispiele für Eigenschaften und mögliche Werte]

 * **font-size**: small, medium, large, x-large, 12px, 20px, 100%, 200%
 * **font-weight**: lighter, normal, bold, 200, 400, 900
 * **font-family**: serif, sans-serif, cursive, monospace
 * **color**: purple, lightgreen, steelblue, red, rgb(120,180,120), #666600

[ENDHINT]



[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]

Falls Sie eine HTML-Datei und CSS-Datei haben, geben Sie bitte beide Dateien ab.

[ENDSECTION]


[INSTRUCTOR::Visuelle Prüfung]
Unter Umständen reicht es bei dieser Aufgabe, die Seite im Browser zu öffnen und zu sehen, ob die Überschrift blau und zentriert ist und ob die Hintergrundfarben, die Farben der anderen Überschriften, die Textdarstellung etc. sich geändert haben.

[ENDINSTRUCTOR]
