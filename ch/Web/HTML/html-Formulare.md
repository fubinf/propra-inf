title: Formulare in HTML
stage: beta
timevalue: 1.5
difficulty: 2
assumes: html-erste-Schritte, html-Medien, html-Semantik, http-POST
---
[SECTION::goal::experience]

- Ich kann Formulare in HTML erstellen.
- Ich kann verschiedene Eingabebausteine wie Textfelder, Radio-Buttons und Checkboxen verwenden.
[ENDSECTION]


[SECTION::background::default]
Damit die Kommunikation im Web nicht nur einseitig ist (Browser ruft Webseiten ab),
brauchen wir eine Möglichkeit für den Benutzer,
Eingaben zu machen und diese an den Webserver zu übermitteln.
Dazu dienen HTML-Formulare.

In dieser Aufgabe, sehen wir uns nur an, wie man ein einfaches Formular _erstellt_,
das Formulardaten an den Server _versendet_. 
Für eine _Auswertung_ der Formulardaten braucht man eine jeweils passende Routine auf dem Webserver 
und daher betrachten wir diesen Aspekt in dieser Aufgabe nicht.
[ENDSECTION]


[SECTION::instructions::detailed]

In dieser Aufgabe wollen wir die Website der Softwareschmiede ProPy erneut um eine weitere Seite ergänzen. 
Diesmal geht es darum, ein Bestellformular zu entwickeln, in der wir bereits möglichst viele Dinge abfragen möchten,
um den Bestellvorgang so einfach wie möglich zu gestalten.

[ER] Erstellen Sie eine neue Webseite `HTMLFormulare.html` mit HTML-Grundstruktur, 
einer passenden Überschrift und einem Menü. 
Fügen Sie ein einfaches Formular hinzu, das es erlaubt, eine E-Mail-Adresse und einen Namen einzugeben.

Sie benötigen dazu die HTML-Elemente `form`, `input`, `button`. 
Wie diese zusammenspielen können Sie im Artikel 
[Was ist ein Webformular?](https://wiki.selfhtml.org/wiki/Formulare/Was_ist_ein_Webformular%3F) in SelfHTML nachlesen.

[ER] Wir wollen das Formular um eine Möglichkeit erweitern, eine mehrere Zeilen lange Beschreibung 
für den Auftrag einzugeben. 
Das ermöglicht das `textarea`-Element. 
Fügen Sie eine Beschriftung und das Eingabefeld hinzu. 
Lesen Sie zum Element in [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea).

[ER] Um herauszufinden, um was für eine Art von Auftrag es sich handelt 
(Neuentwicklung, Softwaretests, Debugging, Projektmanagement),
möchten wir eine Auswahlliste zur Verfügung stellen, in der unser potentieller Kunde 
die Auftragsart auswählen kann. 
Lesen Sie [Abschnitt 3 auf der Seite Auswahllisten](https://wiki.selfhtml.org/wiki/Formulare/Auswahllisten) in SelfHTML.

[ER] Der Benutzer sollte noch unseren Datenschutzbedingungen zustimmen. 
Dazu werden für gewöhnlich eine Checkbox oder zwei Radiobuttons verwendet.
Implementieren Sie beide Varianten.
Lesen Sie Abschnitt 1 und 2 der obigen Seite.

[ER] Fügen Sie ein Datumsfeld für Eingabe eines Fälligkeitsdatums hinzu.
Ferner ein Feld für einen Datei-Upload eines Dokuments mit näheren Erläuterungen.
Das `input`-Element kann für viele verschiedene Eingabetypen benutzt werden, abhängig vom `type`-Attribut.
Eine Liste gültiger Typen finden Sie in [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).
[ENDSECTION]


[SECTION::submission::program]
[INCLUDE::../../_include/Submission-Quellcode.md]
[ENDSECTION]


[INSTRUCTOR::Musterlösung]
Was das Formular absendet, kann z.B. über die 
[Developer-Konsole des Browsers](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/What_are_browser_developer_tools) 
(zu öffnen mit F12) inspiziert werden.

Eine Musterlösung findet sich in [TREEREF::/Web/HTML/html-Formulare.html].
[ENDINSTRUCTOR]
