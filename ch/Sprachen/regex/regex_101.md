title: Einfühung in Regex
stage: draft
timevalue: 1.0
difficulty: 1
profiles:
explains:
---
[SECTION::goal::snippet]
Einstieg in Reguläre Ausdrücke. Ich verstehe die grundlegenden Operatoren von POSIX style Regex und kann einfache Matches selbst schreiben.
[ENDSECTION]

[SECTION::background::default]

[ENDSECTION]

[SECTION::instructions::loose]
Wir beginnen mit der Einführung auf folgender Seite: 
https://www.oreilly.com/content/an-introduction-to-regular-expressions/ und arbeiten diese komplett durch. 

Dort wird auch auf Möglichkeiten zum testen bzw. ausprobieren von Regulären Ausdrücken eingegangen. 
Dazu wird zu einen auf Websites wie https://regex101.com/ sowie das Python Paket `re` verwiesen.

Das referenzierte Minimalbeispiel sähe folgendermaßen aus:

```python
import re

result = re.fullmatch(pattern="[A-Z]{2}", string="TX")

if result:
    print("match")
else:
    print("Doesn't match")
```

Eine weitere gute Seite mit vielen nützlichen Informationen ist: https://regexr.com/ 
Dort lässt sich ebenso die Regex-Syntax auswählen und auch finden sich viele Erklärungen zu bestimmten Syntaxelementen.
Für die meisten Aufgaben in diesem Bereich werden Seiten wie regexr reichen. Jedoch ist zu Empfehlen trotzdem einmal 
die Nutzung in Python durchzuspielen, da sie doch eine der gängigsten Arten regex zu Nutzen darstellt.

### ...

- [EC] Kommando
- [EQ] Frage
- [ER] Anforderung

### ...

[ENDSECTION]

TODO_1_hüster sinnvolle abgabe überlegen

[SECTION::submission::snippet]

.

[ENDSECTION]

[INSTRUCTOR::heading]
.
[ENDINSTRUCTOR]
