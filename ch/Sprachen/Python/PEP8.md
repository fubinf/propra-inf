title: "PEP 8: Der Python-Codierstandard"
stage: beta
timevalue: 1.5
difficulty: 2
explains: PEP8
assumes: Python-mlh
---

[SECTION::goal::idea]

Ich kenne die Regeln (samt Begründungen) des Python-Codierstandards
und habe eine Haltung zu ihnen entwickelt.

[ENDSECTION]
[SECTION::background::default]

Das Lesen von fremdem Programmcode ist wesentlich weniger anstrengend, 
wenn er aussieht "wie gewohnt".
Deshalb ist es wertvoll, wenn sich ein Team auf einen Codierstil einigen kann.

Manche Sprachen haben eine Vorgabe für einen solchen Codierstil, die sehr verbreitet
genutzt wird.
Im Fall von Python steht diese im Python-Standard PEP 8.
Wer den nicht mindestens ungefähr kennt, ist nicht wirklich Python-Programmierer_in.

[ENDSECTION]
[SECTION::instructions::loose]

### Für wen?

Diese Aufgabe ergibt erst Sinn, wenn Sie genügend Python-Programmiererfahrung haben.
Aber wie viel ist "genug"? Schwer zu sagen!

Wenn Sie beispielsweise schon zwei bis drei der größeren Aufgaben der Gruppe
[PARTREF::Python-mlh] gemacht haben (oder irgendetwas anderes größeres), sollte das reichen.
Und wenn nicht? Hmm.

Wenn Sie nicht sicher sind, kann folgendes Vorgehen helfen:
Fangen Sie an, die Aufgabe zu bearbeiten. 
Wenn Sie unterwegs merken, dass Sie Ihr Wissen zu dünn finden, stellen Sie die Aufgabe so lange zurück,
bis Sie genug Erfahrung nachgelegt haben, und machen Sie dann damit weiter.

Machen Sie sich an geeigneter Stelle (vielleicht in einer Datei "TODO.md"?) eine passende Notiz.


### Überblick verschaffen

Lesen und verstehen Sie PEP 8: [HREF::https://peps.python.org/pep-0008/]

Sie brauchen nicht jeden Satz und jedes Codebeispiel genau nachzuvollziehen,
aber Sie sollten mindestens folgendes erreichen:

- Sie haben einen Überblick über die Themenkreise, die in PEP 8 behandelt werden
  und eine ungefähre Vorstellung über die Vorgaben in jedem Themenkreis.
- Sie haben insbesondere folgende Themen genau verstanden und einiges davon auch behalten:
    - Maximum Line Length
    - Whitespace in Expressions and Statements
    - Comments
    - Prescriptive: Naming Conventions
    - Programming Recommendations


### Eigene Haltung bilden

Vergleichen Sie Ihren eigenen Python-Code mit den Regeln von PEP 8.
Vermutlich weicht Ihr Code an vielen Stellen von PEP 8 ab.
Doch welche dieser Abweichungen sind wichtig (weil die Regel sinnvoll ist) und welche nicht?

[EQ] Nennen Sie durchnummeriert 6 bis 8 Detailregeln, die Sie bislang nicht (oder nicht konsequent) befolgen,
aber wertvoll finden und sich künftig angewöhnen wollen.  
Mit "nennen" ist gemeint, die Regel ausformuliert wiederzugeben, ob als wörtliches Zitat oder
in eigenen Worten. Ungefähre Bezeichnungen reichen nicht.
Ganze Themenkreise oder Gruppen von Regeln kommen also nicht in Frage.

[EQ] Nennen Sie durchnummeriert 2 bis 4 Detailregeln, die Sie nicht (oder nicht in der gegebenen Form)
sinnvoll finden. Begründen Sie.
Soweit im Standard diese Regeln eine Begründung haben, muss ihre Begründung darauf Bezug nehmen.

[ENDSECTION]
[SECTION::submission::reflection]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Erst konkret, dann begründet]

[EREFQ::1] Wir akzeptieren jede Angabe, die präzise ist.
Vage formulierte oder übermäßig pauschale Angaben weisen wir zurück.

[EREFQ::1] Wir akzeptieren jede Angabe, die in sich schlüssig ist und nicht auf einem Missverständnis 
der Regeln beruht.
Die Begründung muss mit dem Thema der Regel zusammenpassen.
Wir müssen der Begründung aber nicht unbedingt inhaltlich zustimmen (solange sie nicht total gaga ist).

[ENDINSTRUCTOR]
