title: Mängel bei Aufgaben mit Kommandoprotokoll-Abgabe
stage: beta
timevalue: 1.0
difficulty: 2
assumes: Kommandoprotokolle,Einreichungen,Markdown101
---

[SECTION::goal::idea]

Ich habe zwei Stellen identifiziert, wo Kommandoprotokollaufgaben nicht gut funktionieren,
und dafür Verbesserungen entwickelt.

[ENDSECTION]
[SECTION::background::default]

Vorgaben für Kommandos in Aufgaben ([EREFC::1], [EREFC::2], ...) können Schwächen haben:

- Vielleicht ein simpler Tippfehler oder ähnliches.
- Oder das Kommando funktioniert bei Ihrer Shelleinstellung nicht, obwohl die 
  nichts Exotisches an sich hat.
- Oder das Kommando ist verbal umschrieben, aber 
    - zu undeutlich für den angegebenen Schwierigkeitsgrad der Aufgabe oder 
    - unabsichtlich irreführend
- etc.

[ENDSECTION]
[SECTION::instructions::loose]

Gesucht sind zwei Aufgaben, bei denen  
a) ein Kommandoprotokoll abzugeben ist (neben ggf. anderen Sachen) und  
b) die Anweisungen zur Erstellung dieses Kommandoprotokolls nicht gut sind. 

Beschreiben Sie jeden dieser beiden Fälle wie folgt und lassen Sie diesmal die sonst
für Markdown-Abgaben üblichen Markierungen F1, F2 etc. weg.
Ziel des Formats ist, diese Einreichungen schnell überschauen zu können:

- [EQ] Level-1-Überschrift mit dem Namen der Aufgabe
- [EQ] Level-2-Überschrift "Problem"
- [EQ] Zitat aus dem aktuellen Aufgabentext, das das Problem enthält. 
  Formatiert als Blockzitat, gerade lang genug, dass man Problem und Kontext erkennen kann.
- [EQ] Erläuterung: Was ist da ungünstig? Was ist und wie entsteht der Effekt?
- [EQ] Level-2-Überschrift "Lösungsvorschlag"
- [EQ] Zitat aus dem künftigen Aufgabentext, wie der also aussehen _sollte_,
  damit er das Problem nicht mehr enthält.
  Formatiert als Blockzitat und analog zum obigen.
- [EQ] Ggf. Erläuterung, warum das eine sinnvolle Lösung ist (häufig nicht nötig).

Und dann das Gleiche erneut für die zweite Aufgabe.
Der zweite Fall muss aus einer anderen Aufgabe und einer anderen Aufgabengruppe stammen
als der erste.

[ENDSECTION]
[SECTION::submission::reflection]

Geben Sie Ihr Markdown-Dokument ab.

[ENDSECTION]
[INSTRUCTOR::Tauglichkeit prüfen]

Nachprüfen, ob beide Schwächen wirklich bestehen.  
Nachprüfen, ob die jeweils vorgeschlagene Lösung zumindest ungefähr tauglich ist.

[ENDINSTRUCTOR]
