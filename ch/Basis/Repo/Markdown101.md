title: Das kleine Einmaleins von Markdown
stage: beta
timevalue: 0.5
difficulty: 1
requires: Kommandoprotokolle
---

[SECTION::goal::idea]

Ich kann in Markdown Überschriften, Listen, Codeblöcke und Blockzitate ausdrücken

[ENDSECTION]

[SECTION::background::default]

Sie werden im gesamten ProPra neben Kommandoeingaben bzw. Kommandoausgaben 
auch an vielen Stellen selbst Texte schreiben, um etwas zu erklären 
oder über ein Thema zu reflektieren.

Dazu verwenden wir die schön simple Notation "Markdown".

[ENDSECTION]

[SECTION::instructions::loose]

[TERMREF::Markdown] ist eine Markup-Sprache, die einfach schreibbar und gut lesbar ist.
Man kann damit schnell und einfach strukturierte Texte schreiben. 
Die Dateiendung für Markdown-Dateien ist `.md`.
Lesen Sie diese
[Beschreibung der wichtigsten Elemente von Markdown-Dokumenten](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4).

Mit etwas Übung sind Markdown-Texte auch in ihrer Rohform gut lesbar.
Allerdings hilft es gerade am Anfang, direkt zu sehen, was das Markup im Text bewirkt.
Dafür gibt es in den gängigen Editoren Plugins, die direkt die "hübsche" Version zeigen.  
Damit Sie direkt sehen können, wie der von Ihnen geschriebene Markup-Text aussieht, 
können Sie gerne einen Online-Editor wie [StackEdit.io](https://stackedit.io/) verwenden.

- [EQ] Erstellen Sie die Datei `Markdown101.md` und machen Sie einen Commit mit dieser Datei.


### Welche Formatierungmöglichkeiten gibt es in Markdown?

#### Text Decoration

Texte können **fett**, *kursiv* oder ~~durchgestrichen~~ sein.

- [EQ] Schreiben Sie in der Datei Text wie den obigen.


#### Überschriften

Bis zu diesem Zeitpunkt wurden hier in diesem Dokument (das ursprünglich ebenfalls in Markdown geschrieben ist)
vier Überschriftenebenen benutzt.

- [EQ] Erstellen Sie ein Layout mit fünf Überschrift-Ebenen.


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
    a. Das ist die zweite Ebene.
        - Und eine dritte, ungeordnete Ebene gibt es auch!

- [EQ] Erstellen Sie eine Auflistung mit 5 Ebenen mit Zahlen, Buchstaben und Bullet-Points.
  Mindestens die Ebenen 1, 3, und 5 sollen mehrere Einträge haben.


#### Code-Blöcke

Häufig ist es nützlich, ein paar Code-Zeilen zu zeigen, z.B. folgenden Python-Code:.

```python
import antigravity

antigravity.fly()
```

- [EQ] Erstellen Sie einen Codeblock, der die Syntax von `bash` erwartet.


#### Blockzitate

> Manchmal will man etwas zitieren.
> > Manchmal will ein Zitat zitiert werden.

- [EQ] Erstellen Sie das Zitat `"Es ist nichts beständiger als die Unbeständigkeit.", Immanuel Kant.`


#### Was gibt es noch?

Man kann auch Bilder einfügen, Tabellen schreiben, per CSS das Aussehen der Markdown-Dateien ändern
und noch vieles mehr. Einige der Beispiele dafür finden Sie in der oben genannten Quelle. Wenn man
einen Markdown-Editor schreibt, kann man auch selbst Strukturen entwerfen.

Achtung: Es gibt leider eine Reihe von Dialekten von Markdown.
Lesen Sie ein paar
[Beispiele für Konstrukte, die mit GitHub-Markdown möglich sind](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4#github-treats).

[ENDSECTION]

[SECTION::submission::program]

Geben Sie das Dokument `Markdown101.md` mit den im Text unter [EREFR::1], [EREFR::2], ...
geforderten Markdown-Formatierungen ab.
Geben Sie die Marker mit an.

Dort, wo keine expliziten Texte gefordert sind, dürfen Sie diese frei wählen. 
Aber halten Sie diese kurz, es geht um die Formatierungen!

[ENDSECTION]
