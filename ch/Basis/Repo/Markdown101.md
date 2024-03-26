title: Das kleine Einmaleins von Markdown
stage: alpha
timevalue: 0.5
difficulty: 1
requires: Kommandoprotokolle
---

[SECTION::goal::idea]

- Ich habe Überschriften, Listen, Codeblöcke und Blockzitate in Markdown kennengelernt
- Ich kann diese genannten Formatierungen in einem Markdown Dokument verwenden

[ENDSECTION]

[SECTION::background::default]

Sie werden im gesamten ProPra neben Kommandoeingaben bzw. Kommandoausgaben 
auch an vielen Stellen selbst Texte schreiben, um etwas zu erklären 
oder über ein Thema zu reflektieren.

Sollten Sie noch keinen Berührungspunkt mit Markdown gehabt haben, ist diese Aufgabe 
Ihre Chance das nachzuholen.

[ENDSECTION]

[SECTION::instructions::loose]

[TERMREF::Markdown] ist eine Markup-Sprache, die einfach schreibbar ist, einfach lesbar ist und es
erlaubt relativ schnell strukturierte Texte zu schreiben. 
Die Dateiendung für Markdown-Dateien ist `.md`.
Sie finden [hier](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4)
eine Beschreibung der Elemente und Strukturen eines Markdown-Dokuments.

Mit etwas Übung sind Markdown-Texte auch in ihrer Rohform gut lesbar.
Allerdings hilft es gerade am Anfang, direkt zu sehen, was das Markup im Text bewirkt.
Dafür gibt es in den gängigen Editoren Plugins, die direkt die "hübsche" Version zeigen.  
Damit Sie direkt sehen können, wie der von Ihnen geschriebene Markup-Text aussieht, 
können Sie gerne einen Online-Editor wie [StackEdit.io](https://stackedit.io/) verwenden.

- Erstellen Sie eine Datei `markdown101.md` und machen Sie einen Commit mit dieser Datei.

### Welche Formatierungmöglichkeiten gibt es in Markdown?

#### Text Decoration

Texte können **fett**, *kursiv* oder ~~durchgestrichen~~ sein.

- [ER] Erstellen Sie einen Text mit diesen Dekoratoren

#### Überschriften

Bis zu diesem Zeitpunkt wurden vier Überschriftenebenen benutzt.

- [ER] Erstellen Sie ein Layout mit fünf Überschrift-Ebenen.

#### Listen

Auflistungen sind wichtig. Manchmal sind sie ungeordnet.

- Sie erlauben Hervorhebung und Vergleiche.
- Sie erlauben auch Trennung von Gedanken.

Manchmal wollen wir aber Gedanken ordnen.

1. Das
2. funktioniert
3. so.

Man kann beide Arten von Listen auch verschachteln:

1. Das ist die erste Ebene.
    1. Das ist die zweite Ebene.
        - Und eine dritte, ungeordnete Ebene gibt es auch!

- [ER] Erstellen Sie eine Auflistung von bis zu 5 Ebenen mit Zahlen und Bullet-Points

#### Code-Blöcke

Häufig ist es nützlich wenige Code-Zeilen zu zeigen.

```python
import antigravity

antigravity.fly()
```

- [ER] Erstellen Sie ein `bash` Codeblock.


#### Blockzitate

> Manchmal will man etwas zitieren.
> > Manchmal will ein Zitat zitiert werden.

- [ER] Erstellen Sie das Zitat `"Es ist nichts beständiger als die Unbeständigkeit.", Immanuel Kant.`

#### Was gibt es noch?

Man kann auch Bilder einfügen, Tabellen schreiben, per CSS das Aussehen der Markdown-Dateien ändern
und noch vieles mehr. Einige der Beispiele dafür finden Sie in der oben genannten Quelle. Wenn man
einen Markdown-Editor schreibt, kann man auch selbst Strukturen entwerfen.
[Hier](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4#github-treats) stehen
ein paar Beispiele für Konstrukte, die auf GitHub möglich sind.

[ENDSECTION]

[SECTION::submission::program]

Geben Sie das Dokument `markdown101.md` mit den im Text unter [EREFR::1] bis [EREFR::5]
geforderten Markdown-Formatierungen ab.
Geben Sie die Marker mit an.

Dort, wo keine expliziten Texte gefordert sind, dürfen Sie diese frei wählen. 
Aber: Halten Sie diese kurz, es geht um die Formatierungen!

[ENDSECTION]
