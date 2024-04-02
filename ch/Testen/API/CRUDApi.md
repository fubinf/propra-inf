title: API Tests nach CRUD 
stage: alpha
timevalue: 1.0
difficulty: 3
assumes: restApi, responseApi
---
[SECTION::goal::experience]

- Ich kenne die Vorteile von CRUD
- Ich kann Tests nach CRUD erstellen

[ENDSECTION]
[SECTION::background::default]

Indem [TERMREF2::Regressionstest::-s] speziell auf die CRUD-Operationen abgestimmt werden,
ermöglichen sie eine umfassende und tiefgreifende Analyse des Lebenszyklus eines Objekts. Diese
Herangehensweise erlaubt es, ein Objekt durch alle Phasen seines Daseins zu begleiten – von der Erstellung
über die Abfrage und Modifikation bis hin zur Löschung. Auf diese Weise wird eine maximale Abdeckung von
potenziellen Zuständen und Szenarien erreicht, die ein Objekt im Laufe seiner Existenz annehmen kann.

Das hat den entscheidenden Vorteil, dass eine Vielzahl von Testszenarien an einem einzigen Objekt durchgeführt
werden kann. Dadurch entfällt die Notwendigkeit, für unterschiedliche Testfälle jeweils neue Vorbedingungen zu
schaffen. Diese effiziente Methode spart nicht nur wertvolle Zeit und Ressourcen, sondern stellt auch sicher,
dass die Tests realitätsnahe und relevante Interaktionen mit dem Objekt abbilden. Somit werden die Entwicklungs-
und Testprozesse nicht nur ökonomischer, sondern auch qualitativ hochwertiger gestaltet, indem sie eine holistische
Sicht auf die Verhaltensweisen und Zustände der Objekte innerhalb der Anwendung bieten.

[ENDSECTION]
[SECTION::instructions::tricky]

### CRUD Testplan

Machen Sie sich [hier](https://codebots.com/crud/how-to-test-CRUD) mit dem Prinzip vertraut, wie CRUD am besten eingesetzt werden kann. Anschließend erstellen Sie einen Testplan für die im [Petstore](https://petstore.swagger.io)
hinterlegten `user`-Schnittstellen nach der CRUD-Methode.

- [EQ] Erstellen Sie den oben gewünschten Testplan nach CRUD für die Nutzer Schnittstellen im Petstore.

[HINT::Testabdeckung]
Sie müssen nicht jede vorhandenen Schnittstelle in Ihrem Testplan vorsehen.
[ENDHINT]

### Testplan umsetzen

Sie haben die ersten Schritte im Testdesign durchgeführt. Jetzt sollen Sie diesen Plan automatisieren.

- [ER] Erstellen ein Python Script, welches die API Schnittstellen regressiv testet.

[HINT::Modular]
Die Testfälle sollten modular erstellt werden, um sie flexibel aufrufen zu können. D.h., falls neue
Testfälle dazu geplant werden, sollte das für Ihr Script kein problem sein. Für die Übersicht bietet sich
das geordnete Auslagern der Python Methoden nach den HTTP-Methoden an.
[ENDHINT]

[ENDSECTION]

[SECTION::submission::trace]
[INCLUDE::../../_include/Submission-Markdowndokument.md]
[INCLUDE::../../_include/Submission-Kommandoprotokoll.md]
[ENDSECTION]
