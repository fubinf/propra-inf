title: Tippfehler, Layoutfehler, Wortfehler etc.
stage: beta
timevalue: 1.0
difficulty: 2
---

[SECTION::goal::idea]

Ich habe zwölf Stellen identifiziert und beschrieben, 
wo auf ProPra-Webseiten Einzelheiten nicht in Ordnung sind.

[ENDSECTION]
[SECTION::background::default]

Beim Programmieren kommt es auf fast jede Kleinigkeit an.
Wer einen Blick dafür entwickelt, unstimmige Kleinigkeiten zu bemerken,
kommt sehr viel schneller voran.

[ENDSECTION]
[SECTION::instructions::detailed]

Gesucht sind mindestens 12 Stellen (in mindestens 6 verschiedenen Aufgaben), 
bei denen in der Aufgabenbeschreibung ein Detail nicht korrekt ist, z.B.

- Tippfehler
- Satzbaufehler
- Begriffe verwechselt
- Link kaputt
- Layout kaputt
- etc.

Beschreiben Sie jeden dieser Fälle wie folgt;
Ziel des Formats ist, diese Einreichungen schnell überschauen 
und die Mängel schnell korrigieren zu können:

- Jeder Fall wird beschrieben durch einen Abschnitt im abgegebenen Markdowndokument.
- Die Überschrift ist der URL der Webseite mit dem Problem.
- Der Rumpf ist eine Liste mit zwei Punkten.
- Der erste Aufzählungspunkt beginnt mit "Falsch: " und definiert das Problem.
- Der zweite beginnt mit "Richtig: " und definiert die Korrektur des Problems.

Das könnte dann z.B. so aussehen:

```
## https://www.unsere-uni.de/propra/eine-aufgabe.html
- Falsch: "Kommandozeilnprogramm"  
- Richtig: "Kommandozeilenprogramm"

## https://www.unsere-uni.de/propra/noch-eine-aufgabe.html
- Falsch: "Attribute eine Objekts"
- Richtig: "Attribute eines Objekts"

## https://www.unsere-uni.de/propra/noch-eine-aufgabe.html
- Falsch: "weil im else-Zweig return-Statement fehlt"  
- Richtig: "weil im else-Zweig das return-Statement fehlt"

## https://www.unsere-uni.de/propra/dritte-aufgabe.html
- Falsch: Aufzählung "- Attribute - Methoden - Properties" ist nicht als Aufzählung formatiert  
- Richtig: Markdown-Syntax der Liste korrigieren

## https://www.unsere-uni.de/propra/dritte-aufgabe.html
- Falsch: Das Ziel "Ich verstehe den Zweck von Metaklassen" steht doppelt da
- Richtig: Wiederholung entfernen
```

und so weiter.

Bei einem wörtlichen Zitat immer darauf achten, gerade genug Kontext mitzuliefern,
dass man damit nicht nur die betreffende Stelle finden,
sondern den Fehler auch klar als solchen erkennen kann.

[WARNING]
Nur richtige und noch vorhandene Fehler zählen.
Optionale Kommas und zulässige alternative Schreibweisen zählen nicht.
Fehler aus einer früheren Woche, die inzwischen korrigiert sind, zählen nicht mehr.
[ENDWARNING]

[ENDSECTION]
[SECTION::submission::reflection]

Geben Sie Ihr Markdown-Dokument ab.

[ENDSECTION]
[INSTRUCTOR::Nur zwei pro Aufgabe!]

- Alle URLs prüfen, ob jeder nur höchstens zweimal vorkommt.
- Zufällige drei der Fehler nachprüfen, ob sie wirklich (noch) existieren.

[ENDINSTRUCTOR]
