title: PDB - Der Python DeBugger
stage: alpha
timevalue: 1.0
difficulty: 2
profiles:
explains:
assumes:
requires:
---
[SECTION::goal::idea]

- Ich verstehe, was ein Debugger ist.
- Ich kann pdb einsetzen, um meinen Code systematisch zu durchlaufen.

[ENDSECTION]


[SECTION::background::default]
Wenn es darum geht Code zu verstehen, entweder weil man ihn das erste mal erkundet oder weil man einen Bug fixen möchte,
kann es nützlich sein den Code Schritt für Schritt zu durchlaufen. 
Da das handschriftlich oder im Kopf schon bei relativ kleinen Programmen umständlich wird, kann ein Debugger
ein gutes Werkzeug darstellen.
In diesem Fall schauen wir uns "pdb" an. 
"pdb" ist ein interaktiver Debugger, der über das Terminal gesteuert wird.
Eine GUI-Variante eines Debuggers lernen Sie in [PARTREF::idedebugging] kennen.
[ENDSECTION]


[SECTION::instructions::detailed]
Mithilfe eines Tutorials lernen Sie den Umgang mit pdb.
Klonen Sie hierfür das [pdb-tutorial](https://github.com/spiside/pdb-tutorial/) und 
folgen Sie den Anweisungen in der README.md.
Lesen Sie dazu nicht nur die Anweisungen, sondern führen Sie diese selbst durch. 

## Ihre Aufgabe

Beschreiben Sie in eigenen Worten 

  - [EQ] wie Sie das Debugging mit pdb starten, 
  - [EQ] welche Kommandos Ihnen zur Steuerung von pdb zur Verfügung stehen,
  - [EQ] welche Voraussetzung erfüllt sein muss, um mittels "pdb" einen Bug zu finden und
  - [EQ] wie nützlich Sie das Debugging mit "pdb" empfinden. 
[ENDSECTION]


[SECTION::submission::information]

[INCLUDE::../../_include/Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Hinweise]
- Eine Abgabe ohne die Befehle "l", "s", "n", "b" und "r" ist auf jeden Fall unvollständig und zurückzuweisen.
- Um etwas zu finden, muss man wenigstens in etwa wissen, wo es liegt.
[ENDINSTRUCTOR]