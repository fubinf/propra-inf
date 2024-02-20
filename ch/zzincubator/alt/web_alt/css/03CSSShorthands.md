title: CSS-Shorthand-Properties
stage: draft
timevalue: 1
difficulty: 2
assumes: 02CSSProperties
profiles: WEB
---
!!! goal
    Es ist nicht nur nützlich, die CSS-Shorthands zu kennen, um sich Arbeit zu sparen, sondern
    auch, um Fehler zu vermeiden.
    
Es gibt in CSS einige Eigenschaften, die eine Gruppe anderer Eigenschaften entsprechen. Das
ist nützlich, um beispielsweise die Lesbarkeit durch verringerte Redundanz zu erhöhen und
Anpassungen konsistenter zu ermöglichen.

Ein häufiges Beispiel ist die CSS-Eigenschaft `margin` (Rand), die in sich die Ränder oben,
unten, links und rechts vereint. Man kann also statt `margin-top`, `margin-bottom`,
`margin-left` und `margin-right` anzugeben einfach nur `margin` definieren und das spezifiziert
alle 4 gleichzeitig.

Man kann in diesen Fällen häufig auch mehrere Werte angeben, um verschiedene zusammengefasste
Eigenschaften zu definieren. So definiert beispielsweise `margin: 1% 2%` einen Rand von 1%
oben und unten, aber 2% links und rechts.

Man muss allerdings aufpassen, da eine gleichzeitige Verwendung der Eigenschaften `margin` und
`margin-top` beispielsweise zu widersprüchlichen Definitionen und daraus resultierend auch
unerwartete Ergebnisse.

!!! submission
    Beschreiben Sie kurz, welche Eigenschaft das Shorthand `background` vereint und was diese
    jeweils bedeuten.

    Folgendes Styling ist fehlerhaft. Geben Sie eine korrekte Version an:

    ```css
      body {
        background-image: url('background.png');
        background: fixed;
      }
    ```
