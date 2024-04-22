title: PDB - Der Python DeBugger
stage: beta
timevalue: 1.0
difficulty: 2
---
[SECTION::goal::idea]

- Ich verstehe, was ein Debugger ist.
- Ich kann pdb einsetzen, um meinen Code systematisch zu durchlaufen.

[ENDSECTION]


[SECTION::background::default]
Wenn es darum geht Code zu verstehen, entweder weil man ihn das erste Mal erkundet oder weil man einen Bug fixen möchte,
kann es nützlich sein den Code Schritt für Schritt zu durchlaufen. 
Da das handschriftlich oder im Kopf schon bei relativ kleinen Programmen schwierig wird, kann ein Debugger
ein gutes Werkzeug darstellen.
In diesem Fall schauen wir uns "pdb" an. 
"pdb" ist ein interaktiver Debugger, der über das Terminal gesteuert wird.
Eine GUI-Variante eines Debuggers lernen Sie in [PARTREF::IDE_debugging] kennen.
[ENDSECTION]


[SECTION::instructions::detailed]
Mithilfe eines Tutorials lernen Sie den Umgang mit pdb.
Klonen Sie hierfür das [pdb-tutorial](https://github.com/spiside/pdb-tutorial/)
(natürlich außerhalb Ihres Arbeitsverzeichnisses) und 
folgen Sie den Anweisungen in der README.md.
_Lesen_ Sie die Anweisungen nicht nur, sondern führen Sie diese selbst durch. 

## Ihre Aufgabe

Beschreiben Sie in eigenen Worten:

  - [EQ] Was sind die beiden verschiedenen Methoden des Tutorials, wie Sie das Debugging mit pdb starten? 
  - [EQ] Welche wichtigsten Kommandos stehen Ihnen zur Steuerung von pdb zur Verfügung?
  - [EQ] Welche Voraussetzung sollte bei einem größeren Programm erfüllt sein, 
    um mittels "pdb" einen Defekt gut finden zu können?
  - [EQ] Wie nützlich finden Sie das Debugging mit "pdb"? Was gefällt Ihnen gut, was nicht? 
[ENDSECTION]


[SECTION::submission::information]

[INCLUDE::../../_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Mögliche Antworten]
- Start mit `python -m pdb program.py` oder per Einfügen von `breakpoint()` 
  (oder altmodisch: `import pdb; pdb.set_trace()`) in den Code und dann Laufenlassen.
- Kommandos: Mindestens müssen erwähnt sein "l", "s", "n", "b" und "r".
- Um etwas zu finden, muss man wenigstens in etwa wissen, wo es liegt.
- Die Übersicht, wenn man tiefe Aufrufverschachtelungen hat, ist nicht sehr gut.
[ENDINSTRUCTOR]