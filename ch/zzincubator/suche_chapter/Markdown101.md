title: Das kleine Einmaleins von Markdown
stage: draft
timevalue: 0.5
difficulty: 1
---

[SECTION::goal::idea]

- Ich habe Überschriften, Listen, Codeblöcke und Blockzitate in Markdown kennengelernt
- Ich kann diese genannten Formatierungen in einem Markdown Dokument verwenden

[ENDSECTION]

[SECTION::background::default]

[TERMREF::Markdown] ist eine Markup-Sprache, die einfach schreibbar ist, einfach lesbar ist und es
erlaubt relativ schnell strukturierte Texte zu schreiben. Die Dateiendung für Markdown-Dateien ist
`.md`.
Sie finden [hier](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4)

[ENDSECTION]

[SECTION::instructions::loose]

### Welche Formatierungmöglichkeiten gibt es in Markdown?

#### Text Decoration

Texte können **fett**, *kursiv* oder ~~durchgestrichen~~ sein.

- [ER] Erstellen Sie einen Text mit diesen Dekoratoren

#### Überschriften

Bis zu diesem Zeitpunkt wurden vier Überschriftenebenen benutzt.

- [ER] Erstellen Sie ein Layout mit 5 Überschrift-Ebenen

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
    print("Das ist ein Codeblock!")
```

- [ER] Erstellen Sie ein `bash` Codeblock


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

[WARNING]
Es kann sein, dass Ihre Abgabe farblich nicht der Aufgabenseite gleicht. Lassen Sie sich nicht davon
stören, das ist nicht Teil der Aufgabe. Wichtig ist es sich mit der Struktur auseinanderzusetzen!
[ENDWARNING]

[ENDSECTION]

[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]
