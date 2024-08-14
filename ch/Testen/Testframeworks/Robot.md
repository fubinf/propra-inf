title: Funktionale Tests mit dem Robot Framework
stage: alpha
timevalue: 1.5
difficulty: 3
explains: BDD
---

[SECTION::goal::experience,product]

- Ich verstehe den dreischichtigen Aufbau von Testfällen im Robot Framework
- Ich habe BDD kennengelernt

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

Robot Framework hat Komponenten zum Ansteuern vieler Arten von Software,
(z.B. Web-[TERMREF2::GUI::-s] im Browser, Desktop-GUIs, [TERMREF::SSH])
und Komponenten zur Erzeugung detaillierter Ablaufberichte in HTML.

[ENDSECTION]
[SECTION::instructions::loose]

### Einstieg: Umschauen

Installieren Sie Robot Framework:
`pip install robotframework`.
(Wir beschränken uns in dieser Aufgabe aber auf das Ausprobieren in einer
fertigen Online-Umgebung und nutzen diese Installation gar nicht.)

Überfliegen Sie die Einstiegs-Dokumentation
[HREF::https://robotframework.org/#getting-started].
Nutzen Sie den Online Editor/Laufzeitumgebung auf dieser Seite, 
um erste Schritte mit Robot-Testfällen zu machen.

Betrachten Sie das Beispiel **"Simple Example"**:

- [EQ] Was enthält jede der drei Dateien, die dieses Beispiel bilden?
- [EQ] Welche Testfälle beinhaltet das Beispiel?
- Lassen Sie den Test ablaufen
- [EQ] Erkunden Sie die Ausgabedatei `log.html`.
  Wie lautet der dritte Aufruf einer Operation aus `CustomLibrary.py`, der darin verzeichnet ist?

[HINT::Wo ist die Ausgabedatei?]
Nach dem Testlauf erscheinen am unteren Rand der Editorbox neue Links.
[ENDHINT]

Sie sollten jetzt ein (ungenaues) intuitives Verständnis dafür haben,
was die Notation in `TestSuite.robot` und `keywords.resource` bedeutet.


### Eigenen Testfall ergänzen und Syntax verstehen

- Ergänzen Sie den folgenden Testfall und lassen Sie _nur_ diesen laufen.

```python
Administrator login
    Connect to Server
    Login Admin
```

[HINT::Wie geht das?]
Der Code kann per copy and paste in die Web-Konsole eingefügt und mit dem 
"Run Test"-Link über dem Testfall separat ausgeführt werden.
Zur Erfüllung der Aufgaben ist es nicht nötig, `CustomLibrary.py` zu erweitern.
[ENDHINT]

- Vollziehen Sie in `log.html` nach, was der Testfall genau getan hat.
- [EQ] Ergänzen Sie folgenden Testfall und lassen Sie ihn ablaufen.
  Welche Fehlermeldung erhalten Sie?

```python
Request Userlist as User
    Connect to Server
    Login User            ironman    1234567890
    Get Userlist
    [Teardown]    Close Server Connection
```

- [EQ] Woher weiß Robot Framework, dass bei `Get Userlist` das Wort `Userlist`
  zum Kommandonamen gehört und nicht ein Argument ist (wie das `ironman` beim Kommando davor)?
  Sie finden die Antwort im Kapitel 2 des 
  [User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html).
  Zitieren Sie als Antwort den betreffenden Satz.

[HINT::Ich finde die Information in Kapitel 2 nicht]
Ja, leider ist die Dokumentation nicht gut formuliert.
Der natürliche Ort wäre laut Inhaltsverzeichnis der Abschnitt _"2.2.1 Test case syntax"_
(Bitte nachvollziehen).
Dort ist von "columns" die Rede (Bitte nachlesen). Doch was ist das?
Eine Textsuche nach "columns" hilft nicht (Bitte ausprobieren). Bäh!

Also nochmal in Inhaltsverzeichnis suchen: 
Abschnitt _"2.1 Test data syntax"_ klingt doch auch ganz vielversprechend?
Dessen Sub-Inhaltsverzeichnis (Bitte ansehen) führt unter 2.1.3 den Punkt _"Space separated format"_ auf.
Darin steht die gesuchte Information.

Man braucht etwas Übung im Umgang mit nicht-so-guten Dokumentationen, 
um dort zügig hinzufinden.
[ENDHINT]

- [EQ] Zurück zu unserem Testfall: Wo müsste das fehlende Kommando deklariert werden? Warum dort?
  Nehmen Sie an, dass `Get Userlist` nur ein Synonym von `Get All Users` sein soll
  und deklarieren Sie es in diesem Sinne.
  Probieren Sie Ihre Antwort aus und überzeugen Sie sich, dass der Testfall sich nun anders verhält.
  (Er schlägt aber immer noch fehl.)
- [EQ] Welches Versagen bekommen Sie für diesen Testfall nun?


### Zweites Beispiel: BDD-Example

Wechseln Sie oben in der Editorbox zum Beispiel **BDD-Example**.

- [EQ] Machen Sie sich mit dem Thema [TERMREF::BDD] vertraut, indem Sie das BDD-Example
  und seine Erläuterung studieren. 

[HINT::Was bedeuten `Given`, `When`, `Then`, `And`?]
Das stammt von der verwandten Sprache 
[Gherkin](https://en.wikipedia.org/wiki/Cucumber_(software)#Gherkin_language) 
des verwandten Werkzeugs `Cucumber` aus der Ruby-Welt.

Dort ist `Given`/`When`/`Then` eine fest vorgegebene Struktur eines jeden Tests.
`Given` beschreibt Vorbereitsungsschritte,
`When` beschreibt die Testoperationen und
`Then` beschreibt die Ergebnisprüfungen des Tests.
`And` fügt dem vorangegangenen Konstrukt einen weiteren Teil zu.

Bei Robot Framework werden diese Schlüsselworte einfach ignoriert,
sie stehen also sozusagen nur zur Dekoration da und man könnte z.b. auch `Given` statt `Then`
hinschreiben, ohne dass sich die Wirkung ändert -- was in der Praxis keine tolle Eigenschaft
ist, da es zu recht verwirrenden Formulierungen führen kann.
[ENDHINT]

- [EQ] Betrachten Sie `Calculator.py` und setzen Sie die vier `.robot`-Zeilen des Testfalls
  in vier Zeilen Python-Code auf Basis von `Calculator.py` um.

[HINT::Und was ist mit `Calc_keywords.resource`?]
Dort könnten Sie den genauen Zusammenhang von Testfall und Python-Code nachlesen,
aber der Testfall ist so einfach, dass die Aufgabe wahrscheinlich schneller erledigt ist,
wenn Sie die Python-Struktur selbst überlegen -- das spart nämlich viele Kontextwechsel.
[ENDHINT]

- [EQ] Ergänzen Sie in `Calculator_Test_Suite.robot` die Bedingung 
  `Then The Result Should Not Be "1"`.  
  Was müssen Sie in `Calc_keywords.resource` zufügen, damit der Testfall wieder ausführbar wird?

[HINT::Was kann ich denn dabei alles benutzen?]
In `Calc_keywords.resource` werden diverse "Schlüsselworte" (Kommandos) benutzt,
die von nirgendwo sichtbar importiert werden, sondern einfach so vorhanden sind.
Neben `Should Be Equal As Numbers` gibt es auch `Should Not Be Equal As Numbers`.
Beides stammt aus der umfangreichen
[`BuiltIns`-Standardbibliothek](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#standard-libraries),
die ohne Import verfügbar ist; ähnlich wie in Python.
[ENDHINT]


### BDD-Diskussion

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

[ENDSECTION]
[SECTION::submission::trace]

[INCLUDE::/_include/Submission-Markdowndokument.md]

[ENDSECTION]
[INSTRUCTOR::Musterlösung]

TODO_1_ruhe

[ENDINSTRUCTOR]
