title: CSS-Pseudo-Klassen und -Elemente
timevalue: 1
difficulty: 2
assumes: 01CSSSelectors
profiles: WEB
---
!!! goal
    Es kommt vor, dass man mittels CSS etwas gestalten möchte, das keinem konkreten HTML-Element
    entspricht. Hier wird das Arsenal an Selektoren erweitert, um das zu ermöglichen.
    
Elemente auf Webseiten haben gerne Zustände, die aus ihnen keine neuen Elemente machen. So ist
ein Link, den man bereits besucht hat, beispielsweise gerne anders gefärbt als einer, bei dem
das nicht der Fall ist. Selektoren für derartige Fälle sind mit Pseudo-Klassen möglich.

Der Selektor `a` beschreibt beispielsweise alle Hyperlinks, `a:visited` hingegen nur diejenigen,
die bereits besucht wurden.

Es gibt auch die Möglichkeit, Dinge zu beschreiben, die Elemente sein könnten, aber aus
verschiedenen Gründen keine sind. So ist `p::first-line` beispielsweise ein Selektor, der
die ersten Zeilen aller Absätze beschreibt. Diese ersten Zeilen existieren selbstverständlich
so auf der Seite, allerdings ist der Inhalt unter anderem davon abhängig, wie groß das Fenster
und die Schriftgröße sind.

!!! submission
    Beschreiben Sie kurz 3 (weitere) Pseudo-_Klassen_ und wofür diese da sind. Sind diese für
    alle Elemente gedacht oder haben sie wie `:visited` eine Beschränkung auf spezifische Tags?

    Beschreiben Sie außerdem kurz 3 (weitere) Pseudo-_Elemente_ und wofür diese da sind.
