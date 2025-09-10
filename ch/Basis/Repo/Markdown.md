title: Das kleine Einmaleins von Markdown
stage: beta
timevalue: 0.5
difficulty: 2
---

[SECTION::goal::idea]
Ich kann in Markdown Überschriften, Listen, Codeblöcke, Blockzitate
und Hyperlinks ausdrücken
[ENDSECTION]

[SECTION::background::default]
Sie werden im gesamten ProPra neben Kommandoeingaben bzw. Kommandoausgaben 
auch an vielen Stellen selbst Texte schreiben, um etwas zu erklären 
oder über ein Thema zu reflektieren.

Dazu verwenden wir die schön simple Notation "Markdown".

[NOTICE]
Wer Markdown schon kennt (halbwegs gut reicht), 
darf diese Aufgabe auch gern überspringen.
[ENDNOTICE]
[ENDSECTION]

[SECTION::instructions::loose]
[TERMREF::Markdown] ist eine Markup-Sprache, die (anders als [TERMREF::HTML]) 
einfach schreibbar und gut lesbar ist.
Man kann damit schnell und einfach strukturierte Texte schreiben. 
Die Dateiendung für Markdown-Dateien ist `.md`.
Lesen Sie diese
[Beschreibung der wichtigsten Elemente von Markdown-Dokumenten](https://gist.github.com/pixelspencil/87dfff9816e4bf41f5f6e5bf62eebff4).

Mit etwas Übung sind Markdown-Texte auch in ihrer Rohform gut lesbar.
Allerdings hilft es gerade am Anfang, direkt zu sehen, was das Markup im Text bewirkt.
Dafür gibt es in den gängigen Editoren Plugins, die direkt die "hübsche" Version zeigen.  
Damit Sie direkt sehen können, wie der von Ihnen geschriebene Markup-Text aussieht, 
können Sie gerne einen Online-Editor wie [StackEdit.io](https://stackedit.io/) verwenden.

- [EQ] Erstellen Sie die Datei `Markdown.md` und machen Sie einen Commit mit dieser Datei.


### Welche Formatierungmöglichkeiten gibt es in Markdown?

#### Text Decoration

Text kann **fett** oder *kursiv* sein.

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
    1. Das ist die zweite Ebene.
    1. Wieder zweite Ebene.
        1. Und eine dritte Ebene gibt es auch!
        1. Jawoll!

- Das ist die erste Ebene.
    - Das ist die zweite Ebene.
    - Wieder zweite Ebene.
        - Und eine dritte Ebene gibt es auch!
        - Jawoll!

[WARNING]
Markdown hat zahlreiche Dialekte, d.h.
nicht alle Markdown-Implementierungen [funktionieren gleich](https://johnmacfarlane.net/babelmark2/faq.html).
Wer halbwegs sicher sein will, sollte bei allen Verschachtelungen 
jeweils 4 zusätzliche Leerzeichen weit einrücken.

Eine "offizielle" Spezifikation gibt es nicht.
Am ehesten kommt noch die [Urfassung](https://daringfireball.net/projects/markdown/syntax)
infrage.
Eine besonders wichtige Variante ist 
[GitHub-Markdown](https://docs.github.com/en/get-started/writing-on-github)
[ENDWARNING]

- [EQ] Erstellen Sie eine verschachtelte Auflistung.


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

Man kann auch Bilder einfügen, Tabellen schreiben, 
per [TERMREF::CSS] das Aussehen der Markdown-Dateien ändern
und noch vieles mehr; 
siehe die oben genannten Quellen.
[ENDSECTION]

[SECTION::submission::program]
Geben Sie das Dokument `Markdown.md` mit den im Text unter [EREFQ::1], [EREFQ::2], ...
geforderten Markdown-Formatierungen ab.
Geben Sie die Marker mit an.

Dort, wo keine expliziten Texte gefordert sind, dürfen Sie diese frei wählen. 
Aber halten Sie diese kurz, es geht uns um die Formatierungen!
[ENDSECTION]

[INSTRUCTOR::Markdown prüfen]
Die abgegebene Markdown Datei sollte in irgendeiner Weise die folgenden Abschnitte enthalten:

[INCLUDE::ALT:]
[ENDINSTRUCTOR]