title: Funktionale Tests mit dem Robot Framework
stage: alpha
timevalue: 1.5
difficulty: 3
explains: BDD
---

[SECTION::goal::experience]

- Ich verstehe, wie im Robot Framework Testfälle, selbstdefinierte Keywords und Python-Bibliotheken zusammenspielen.
- Ich kann eigene Keywords definieren und das Testprotokoll `log.html` lesen.
- Ich habe BDD-artige Testfälle ausprobiert und weiß, was einen guten BDD-Test ausmacht.

[ENDSECTION]
[SECTION::background::default]

### Was ist das Robot Framework und wie kann ich es nutzen?

Das Robot Framework (RF) ist ein Open-Source-Automatisierungs-Framework für Software-Tests und
[TERMREF::Robotic Process Automation] (RPA), welches in Python entwickelt wurde.
Es ermöglicht die Erstellung automatisierter Tests durch den
Einsatz von einfach lesbaren Skripten für [TERMREF::Keyword-Driven Testing].
(Achtung: Diese "Schlüsselwörter" sind Kommandonamen, die oft aus mehreren Wörtern bestehen.)
Anstelle von Tests können die Skripte ebensogut Automatisierungsaufgaben in beliebigen
Geschäftsprozessen übernehmen.

Robot Framework hat Komponenten zum Ansteuern vieler Arten von Software
(z.B. Web-[TERMREF2::GUI::-s] im Browser, Desktop-GUIs, [TERMREF::SSH])
und Komponenten zur Erzeugung detaillierter Ablaufberichte in HTML.

[ENDSECTION]
[SECTION::instructions::loose]

### Einstieg: Das "Simple Example"

Wir arbeiten in dieser Aufgabe ausschließlich mit der Online-Umgebung von Robot Framework,
Sie müssen also nichts installieren.
(Lokal würde man es mit `pip install robotframework` installieren.)

Öffnen Sie die Einstiegsseite
[HREF::https://robotframework.org/#getting-started].
Dort gibt es einen Editor, in dem Sie Robot-Testfälle direkt im Browser bearbeiten und ausführen können.
Wählen Sie oben in der Editorbox das Beispiel **Simple Example** aus und sehen Sie sich die drei Dateien an.

- [EQ] Welche Aufgabe hat jede der drei Dateien? Ein Satz pro Datei genügt.

Starten Sie nun den Testlauf mit dem Knopf "Run".

[HINT::Wo ist die Ausgabedatei?]
Nach dem Testlauf erscheinen in der Editorbox die Knöpfe `log.html` und `report.html`.
[ENDHINT]

- [EQ] Öffnen Sie `log.html` und klappen Sie die Einträge des ersten Testfalls auf.
  Welches ist das dritte Keyword aus `CustomLibrary.py`, das dort aufgerufen wird?
  Welches Argument steht beim Aufruf, und welchen Wert hat es in diesem Testfall?

[HINT::Woran erkenne ich, woher ein Keyword stammt?]
In `log.html` steht vor jedem Keyword-Namen, aus welcher Bibliothek oder Resource-Datei es kommt,
z.B. `CustomLibrary . Connect` oder `keywords . Connect to Server`.
[ENDHINT]

Sie sollten jetzt ein grobes, intuitives Verständnis dafür haben,
was die Notation in `TestSuite.robot` und `keywords.resource` bedeutet.

<!-- time estimate: 20 min -->


### Eigene Testfälle ergänzen

Fügen Sie in `TestSuite.robot` am Ende des Abschnitts `*** Test Cases ***` diesen Testfall ein
und lassen Sie _nur_ ihn laufen:

```
Administrator login
    Connect to Server
    Login Admin
```

[HINT::Wie lasse ich nur einen Testfall laufen?]
Kopieren Sie den Code in den Editor.
Über jedem Testfall erscheint ein "Run Test"-Link, mit dem Sie ihn einzeln starten können.
`CustomLibrary.py` müssen Sie in dieser Aufgabe nirgends erweitern.
[ENDHINT]

Sehen Sie in `log.html` nach, was der Testfall im Einzelnen getan hat.
Fügen Sie dann noch diesen Testfall ein und lassen Sie ihn laufen:

```
Request Userlist as User
    Connect to Server
    Login User            ironman    1234567890
    Get Userlist
    [Teardown]    Close Server Connection
```

- [EQ] Welche Fehlermeldung erhalten Sie?
- [EQ] Woher weiß Robot Framework, dass bei `Get Userlist` das Wort `Userlist`
  zum Keyword-Namen gehört und nicht ein Argument ist (wie das `ironman` beim Keyword davor)?
  Sie finden die Antwort im Kapitel 2 des
  [User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html).
  Zitieren Sie als Antwort den betreffenden Satz.

[HINT::Ich finde die Information in Kapitel 2 nicht]
Ja, leider ist die Dokumentation hier nicht gut gegliedert.
Der naheliegende Ort wäre laut Inhaltsverzeichnis der Abschnitt _"2.2.1 Test case syntax"_
(bitte nachvollziehen).
Dort ist von "columns" die Rede, aber was damit gemeint ist, steht dort nicht.
Eine Textsuche nach "columns" hilft auch nicht weiter (bitte ausprobieren).

Also noch einmal ins Inhaltsverzeichnis schauen:
Abschnitt _"2.1 Test data syntax"_ klingt ebenfalls vielversprechend.
Dessen Unter-Inhaltsverzeichnis führt unter 2.1.3 den Punkt _"Space separated format"_ auf.
Dort steht die gesuchte Information.

Man braucht etwas Übung im Umgang mit nicht so guten Dokumentationen,
um zügig an die richtige Stelle zu finden.
[ENDHINT]

Zurück zu unserem Testfall.
Nehmen Sie an, dass `Get Userlist` nur ein anderer Name für das vorhandene Keyword `Get All Users` sein soll.

- [EQ] Definieren Sie das Keyword `Get Userlist` entsprechend.
  In welche Datei gehört die Definition am besten, und warum?
  Geben Sie Ihre Definition mit an.

[HINT::Wie definiere ich ein Keyword?]
Schauen Sie sich in `keywords.resource` an, wie z.B. `Login Admin` definiert ist:
Der Name steht am Zeilenanfang, die Schritte darunter sind eingerückt.
[ENDHINT]

- [EQ] Lassen Sie den Testfall erneut laufen.
  Er schlägt immer noch fehl, aber mit einer anderen Meldung.
  Wie lautet sie, und woran liegt das?

[HINT::Ich verstehe nicht, warum der Test fehlschlägt]
Lesen Sie in `CustomLibrary.py` den Docstring von `get_all_users` und
vergleichen Sie ihn mit dem Benutzer, der sich im Testfall anmeldet.
[ENDHINT]

<!-- time estimate: 35 min -->


### Zweites Beispiel: BDD-Example

Wechseln Sie oben in der Editorbox zum Beispiel **BDD-Example** und lesen Sie die zugehörige Erläuterung.
Der Testfall liest sich fast wie ein englischer Satz.
Genau darum geht es bei [TERMREF::BDD]:
Testfälle sollen so formuliert sein, dass auch Menschen ohne Programmierkenntnisse sie verstehen.

[HINT::Was bedeuten `Given`, `When`, `Then`, `And`?]
Das stammt von der Sprache
[Gherkin](https://en.wikipedia.org/wiki/Cucumber_(software)#Gherkin_language)
des verwandten Werkzeugs `Cucumber` aus der Ruby-Welt.

Dort ist `Given`/`When`/`Then` eine fest vorgegebene Struktur eines jeden Tests.
`Given` beschreibt Vorbereitungsschritte,
`When` beschreibt die Testoperationen und
`Then` beschreibt die Ergebnisprüfungen des Tests.
`And` fügt dem vorangegangenen Konstrukt einen weiteren Teil hinzu.

Robot Framework ignoriert diese Wörter einfach.
Sie stehen also nur zur Dekoration da, und man könnte z.B. auch `Given` statt `Then`
hinschreiben, ohne dass sich die Wirkung ändert.
In der Praxis ist das keine gute Eigenschaft, weil es zu recht verwirrenden Formulierungen führen kann.
[ENDHINT]

- [EQ] Betrachten Sie `Calculator.py`. Übersetzen Sie die vier Zeilen des Testfalls aus `Calculator_Test_Suite.robot`
  in vier Zeilen Python-Code, die `Calculator.py` benutzen.

[HINT::Und was ist mit `Calc_keywords.resource`?]
Dort könnten Sie den genauen Zusammenhang von Testfall und Python-Code nachlesen.
Der Testfall ist aber so einfach, dass Sie wahrscheinlich schneller sind,
wenn Sie sich die Python-Fassung selbst überlegen.
[ENDHINT]

In `Calc_keywords.resource` steht im Keyword `The User Enters The Term "${term}"`
die Zeile `Set Test Variable    ${term}`.

- [EQ] Setzen Sie ein `#` an den Anfang dieser Zeile, um sie auszukommentieren,
  und lassen Sie den Test laufen.
  Was passiert?
  Was schließen Sie daraus über die Sichtbarkeit von Variablen in Robot Framework?
  Entfernen Sie das `#` danach wieder.

- [EQ] Ergänzen Sie am Ende des Testfalls in `Calculator_Test_Suite.robot` die Zeile
  `And The Result Should Not Be "1"`.
  Was müssen Sie in `Calc_keywords.resource` hinzufügen, damit der Test wieder läuft?
  Geben Sie Ihr neues Keyword an.

[HINT::Was kann ich dafür benutzen?]
Schauen Sie sich an, wie `The Result Should Be "${expected}"` gebaut ist:
Der Wert in Anführungszeichen landet als Argument im Keyword.
Neben `Should Be Equal As Numbers` gibt es auch `Should Not Be Equal As Numbers`.
Beide stammen aus der
[`BuiltIn`-Standardbibliothek](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html),
die ohne Import verfügbar ist, ähnlich wie die eingebauten Funktionen in Python.
[ENDHINT]

<!-- time estimate: 25 min -->


### Was macht einen guten BDD-Test aus?

BDD ist nicht nur eine Syntax für Testfälle, sondern eine Methode dafür,
wie man Akzeptanztests formulieren sollte, die von nichttechnischen Menschen
verstanden werden können.

Viele Entwickler_innen haben diese Methode nicht verstanden und schreiben deshalb
schlechte (Pseudo-)BDD-Tests.
Hier ist eine gute Diskussion, wie es richtig geht:
[HREF::https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/]

Lesen Sie diese Quelle quer, bis Sie darin zwei Ideen entdeckt haben,
die Ihnen neu erscheinen.

- [EQ] Formulieren Sie diese zwei Ideen in eigenen Worten.

<!-- time estimate: 10 min -->

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]

[INSTRUCTOR::Prüfhilfen]

[INCLUDE::ALT:]

[ENDINSTRUCTOR]
