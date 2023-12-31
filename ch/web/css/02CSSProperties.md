title: CSS-Eigenschaften
timevalue: 1.5
difficulty: 2
assumes: 01CSSSelectors
profiles: WEB
---
!!! goal
    Ähnlich wie bei HTML gilt es hier, wesentliche Grundlagen zur Benutzung zu erlernen.
    
Ähnlich zu den Attributen aus HTML besitzt CSS auch Eigenschaften in Key-Value-Paaren (im
Englischen "Property"), die man den ausgewählten Elementen zuordnen kann.

!!! submission
    Beschreiben Sie kurz, welche Werte für die Eigenschaft `display` existieren und was sie
    jeweils tun. Wie kan man mit CSS erreichen, dass sich alle `span`-Tags in HTML wie `div`
    verhalten und umgekehrt?
    Geben Sie HTML-Code an, bei dem es bei einem von Ihnen ausgewählten Element unterschiedliche
    Ergebnisse entstehen zwischen `display: none;` und `visibility: hidden;`.

!!! notice
    Die `display`-Eigenschaft ist auch anwendbar auf das `style`-Tag! Es ist also möglich, das
    anzeigen zu lassen und mit dem `contenteditable`-Attribut auf "true" bearbeitbar zu machen,
    um direkt in der Seite zu experimentieren.

    ```html
      <html>
        <head>
          <style contenteditable="true" style="display: block";>
            CSS-Styles
          </style>
        </head>
        <body>
          ...
        </body>
      </html>
    ```
