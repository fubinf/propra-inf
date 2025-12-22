title: Einführung in CSS
stage: beta
timevalue: 1.0
difficulty: 2
requires: html-erste-Schritte
---

[SECTION::goal::experience]

 - Ich kann CSS in HTML oder als separate Datei einbinden
 - Ich beschreibe CSS-Elemente und implementiere einige einfache CSS-Eigenschaften.

[ENDSECTION]
[SECTION::background::default]

[TERMREF::CSS] wird benutzt um [TERMREF2::HTML::HTML-Dokumente] mit Layout und Design zu versehen. 
Diese Aufgabe beschäftigt sich damit, wie CSS in HTML zur Anwendung kommt und mit ersten Selektoren und Eigenschaften.

[ENDSECTION]
[SECTION::instructions::detailed]

### CSS Syntax

CSS definiert Eigenschaften, die HTML-Elementen zugewiesen werden.
Über einen Selektor werden ein oder meherere HTML-Elemente ausgewählt. Innerhalb der
geschweiften Klammern steht dann die Liste der Eigenschaften.

```css
Selektor {
    eigenschaft: wert;
    zweite-eigenschaft: wert;
}
```

Die Liste möglicher Eigenschaften (engl. *properties*) ist lang und die möglichen Werte sind 
je nach Eigenschaft verschieden.
Beides folgt einem Standard des World Wide Web Consortiums (W3C).
Eine [gute CSS-Dokumentation](https://developer.mozilla.org/en-US/docs/Web/CSS) 
findet sich bei Mozilla.

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


### CSS Einbinden

Grundsätzlich gibt es drei verschiedene Varianten, wie CSS in HTML eingebunden werden kann.

1. **Als externes Stylesheet**: Dabei wird das CSS in eine separate Datei geschrieben, 
für gewöhnlich mit der Endung `.css`. In dieser Datei befindet sich dann ausschließlich CSS, kein HTML. 
Im HTML-Dokument wird innerhalb des `head`-Elements ein Element eingefügt, 
sodass der Browser weiß, wo nach der CSS-Datei zu suchen ist:

```html
  <link rel="stylesheet" type="text/css" href="beispiel.css">
```

Vorteil hierbei ist, dass derselbe CSS-Code für mehrere HTML-Dokumente verwendet werden kann. 
Dies ist daher auch der Standard zum Einbinden von CSS.

2. **Als internes Stylesheet**: Anstatt den CSS-Code in einer separaten Datei zu halten, 
kann der auch direkt in der HTML-Datei Platz finden. 
Dies geschieht über die Verwendung des `<style>`-Elements im `<head>`:

```html
<head>
    <title>Beispiel</title>
    <style type="text/css">
        body { background-color: purple; }
    </style>
</head>
```

3. **Innerhalb von HTML-Tags**: Über das `style`-[TERMREF2::HTML-Attribut::Attribut] kann CSS 
direkt im Element platziert werden, für das die Eigenschaften gelten sollen. 
Hierbei entfallen dann Selektor und geschweifte Klammern, denn der Bezug zum HTML-Element ist ja gegeben:

```html
  <p style="color: purple; text-decoration: underline;">Beispieltext</p>
```

### Ausprobieren!

Als Grundlage für das Experimentieren mit CSS soll das erstellte Dokument aus [PARTREF::html-erste-Schritte] verwendet werden. 
Erstellen Sie eine Kopie als `CSSEinfuehrung-index.html`.

[ER] Zunächst soll die Hauptüberschrift auf der Seite zentriert werden. 
Benutzen Sie dafür die CSS-Eigenschaft `text-align` mit dem Wert `center`. 
Ändern Sie außerdem die Schriftfarbe zu einem Python-gerechten Blau. Verwenden Sie ein `style`-Attribut.

[ER] Ändern Sie nun die Hintergrundfarbe der Webseite mittels eines externen Stylesheets `CSSEinfuehrung.css`. 
Um den gesamten Inhalt der Website zu beinflussen, kann man das `body`-Element selektieren.

[ER] Ändern Sie Schriftart, Schriftgröße und Schriftstärke für Absätze und Listen auf der Seite. 
Geben Sie den anderen Überschriften eine weitere Farbe.

[HINT::Einige Beispiele für Eigenschaften und mögliche Werte]

 * **font-size**: small, medium, large, x-large, 12px, 20px, 100%, 200%
 * **font-weight**: lighter, normal, bold, 200, 400, 900
 * **font-family**: serif, sans-serif, cursive, monospace
 * **color**: purple, lightgreen, steelblue, red, rgb(120,180,120), #666600

[ENDHINT]

[ENDSECTION]
[SECTION::submission::reflection,program]

[INCLUDE::/_include/Submission-Quellcode.md]
(HTML-Datei und CSS-Datei)

[ENDSECTION]
[INSTRUCTOR::Visuelle Prüfung]

Meist reicht es bei dieser Aufgabe, die Seite im Browser zu öffnen und zu sehen, 
ob die Überschrift blau und zentriert ist und ob die Hintergrundfarben, 
die Farben der anderen Überschriften, die Textdarstellung etc. sich geändert haben.

[ENDINSTRUCTOR]
