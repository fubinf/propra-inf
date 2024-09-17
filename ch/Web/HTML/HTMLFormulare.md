title: Formulare in HTML
stage: alpha
timevalue: 1.5
difficulty: 2
assumes: HTMLErsteSchritte, HTMLMedien, HTMLSemantik, HTTP-Methoden
---
[SECTION::goal::experience]

- Ich kann Formulare in HTML erstellen.
- Ich kann verschiedene Eingabebausteine wie Textfelder, Radio-Buttons und Checkboxen verwenden.

[ENDSECTION]
[SECTION::background::default]

Damit die Kommunikation im Web nicht nur einseitig ist, d.h. vom Webseitenersteller
zum Betrachter, ist es unerlässlich eine Möglichkeit für den Benutzer zu haben,
Eingaben zu machen und diese dann auch an den Webseitenersteller zu übermitteln.
An dieser Stelle kommen Formulare ins Spiel.

In dieser Aufgabe, sehen wir uns an, wie man ein einfaches Formular erstellt,
dass verschiedene Eingabetypen verwendet. Für eine Auswertung des Formulars reicht allerdings
reines HTML nicht mehr aus und daher betrachten wir diesen Aspekt in dieser Aufgabe nicht.

[ENDSECTION]
[SECTION::instructions::detailed]

In dieser Aufgabe wollen wir die Website der Softwareschmiede ProPy erneut um eine weitere Seite ergänzen. 
Diesmal geht es darum, ein Bestellformular zu entwickeln, in der wir bereits möglichst viele Dinge abfragen möchten,
um den Bestellvorgang so einfach wie möglich zu gestalten.

[ER] Erstellen Sie eine neue Website HTMLFormulare.html mit HTML-Grundstruktur, einer passenden Überschrift und einem Menü. 
Fügen Sie ein einfaches Formular hinzu, dass es erlaubt eine E-Mail-Adresse und einen Namen einzugeben.

Sie benötigen dazu die HTML-Elemente `form`, `input`, `button`. 
Wie diese zusammenspielen können Sie im Artikel 
[Was ist ein Webformular?](https://wiki.selfhtml.org/wiki/Formulare/Was_ist_ein_Webformular%3F) in SelfHTML nachlesen.

[ER] Wir wollen das Formular um eine Möglichkeit erweitern, eine Beschreibung für den Auftrag einzugeben. 
Dazu braucht es eine Möglichkeit einen längeren Text einzugeben. 
Diese liefert das `textarea`-Element. 
Fügen Sie eine Beschriftung und das Eingabefeld hinzu. 
Lesen Sie zum Element in [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea).

[ER] Um herauszufinden, um was für eine Art von Auftrag es sich handelt 
(Neuentwicklung, Softwaretests, Debugging, Projektmanagement),
möchten wir eine Auswahlliste zur Verfügung stellen, in der unser potentieller Kunde 
die richtige Auftragsart auswählen kann. 
Lesen Sie [Abschnitt 3 auf der Seite Auswahllisten](https://wiki.selfhtml.org/wiki/Formulare/Auswahllisten) in SelfHTML.

[ER] Der Benutzer sollte noch unseren Datenschutzbedinungen zustimmen. 
Dazu werden für gewöhnlich eine Checkbox oder zwei Radiobuttons verwendet.
Implementieren Sie beide Varianten.
Lesen Sie Abschnitt 1 und 2 der in [EREFR::3] verlinkten Seite.

[ER] Ist der Auftrag sonderlich eilig oder gibt es eine Deadline, so wäre es sicherlich sinnvoll dies auch zu erfahren.
Fügen Sie ein Feld für Eingabe eines Fälligkeitsdatums hinzu. 
Ergänzen Sie außerdem noch mindestens zwei weitere Eingabefelder, die verschiedene Werte verlangen.
Das `input`-Element kann für viele verschiedene Eingabetypen benutzt werden, abhängig vom `type`-Attribut.
Eine Liste von validen Typen finden sie in [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).


[ENDSECTION]
[SECTION::submission::program]

[INCLUDE::../../_include/Submission-Quellcode.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

Was das Formular absendet, kann z.B. über die Developer-Konsole des Browsers inspiziert werden.

Eine Musterlösung findet sich in [TREEREF::/Web/HTML/HTMLFormulare.html].

[ENDINSTRUCTOR]
